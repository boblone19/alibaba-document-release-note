---
title: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Container Service for Kubernetes Developer Guide 20220928"
product_version: "V3.14.0"
doc_version: "20220928"
pdf_pages: 214
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Container Service for Kubernetes Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.14.0/%E5%BC%B9%E6%80%A7%E8%AE%A1%E7%AE%97/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.14.0%20Container%20Service%20for%20Kubernetes%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.14.0 Container Service for Kubernetes Developer Guide 20220928

## Table of Contents

- 1 Use ASAPI to call the Apsara Stack SDK
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
- 2 Container Service API invocation
  - 2.1 Overview
  - 2.2 Common parameters
  - 2.3 Request syntax
  - 2.4 Response parameters
  - 2.5 Sign API requests
- 3 Cluster API list
  - 3.1 Clusters
    - 3.1.1 CreateCluster
    - 3.1.2 ScaleOutCluster
    - 3.1.3 DeleteCluster
    - 3.1.4 DescribeClusterUserKubeconfig
    - 3.1.5 Query
      - 3.1.5.1 DescribeClustersV1
      - 3.1.5.2 DescribeClusterDetail
      - 3.1.5.3 DescribeClusterResources
      - 3.1.5.4 DescribeClusterNamespaces
      - 3.1.5.5 DescribeExternalAgent
      - 3.1.5.6 DescribeUserQuota
      - 3.1.5.7 DescribeClusterLogs
      - 3.1.5.8 DescribeKubernetesVersionMetadata
    - 3.1.6 Modify
      - 3.1.6.1 ModifyCluster
      - 3.1.6.2 ModifyClusterTags
    - 3.1.7 Upgrade
      - 3.1.7.1 UpgradeCluster
      - 3.1.7.2 GetUpgradeStatus
      - 3.1.7.3 PauseClusterUpgrade
      - 3.1.7.4 CancelClusterUpgrade
      - 3.1.7.5 ResumeUpgradeCluster
  - 3.2 Nodes
    - 3.2.1 DescribeClusterNodes
    - 3.2.2 RemoveClusterNodes
    - 3.2.3 AttachInstances
    - 3.2.4 DescribeClusterAttachScripts
    - 3.2.5 Node pools
      - 3.2.5.1 CreateClusterNodePool
      - 3.2.5.2 ScaleClusterNodePool
      - 3.2.5.3 ModifyClusterNodePool
      - 3.2.5.4 DescribeClusterNodePools
      - 3.2.5.5 DescribeClusterNodePoolDetail
      - 3.2.5.6 DeleteClusterNodepool
  - 3.3 Templates
    - 3.3.1 CreateTemplate
    - 3.3.2 DeleteTemplate
    - 3.3.3 DescribeTemplates
    - 3.3.4 DescribeTemplateAttribute
    - 3.3.5 UpdateTemplate
  - 3.4 Add-ons
    - 3.4.1 InstallClusterAddons
    - 3.4.2 DescribeAddons
    - 3.4.3 DescribeClusterAddonsVersion
    - 3.4.4 DescribeClusterAddonsUpgradeStatus
    - 3.4.5 UpgradeClusterAddons
    - 3.4.6 UnInstallClusterAddons
  - 3.5 Commonly used parameters
  - 3.6 Error codes

he Apsara Stack SDK

## 1 Use ASAPI to call the Apsara Stack SDK

Stack SDK

### 1.1 ASAPI Developer Guide

#### 1.1.1 ASAPI overview

This topic describes the architecture and features of the Apsara Stack API (ASAPI). The ASAPI is a unified ingress gateway for Apsara Stack services and a main component of the Apsara Uni-manager Management Console. The ASAPI provides a unified method for you to manage and make API calls. You can use Apsara Stack SDK to centrally make API calls to Apsara Stack services, including Elastic Compute Service (ECS) and Virtual Private Cloud (VPC). The ASAPI allows you to make API calls to manage and maintain Apsara Stack services. Make API calls to implement enterprise-grade management. For example, you can manage organizations, users, roles, resource sets, and logon policies. These operations are provided by the he Apsara Stack SDK Apsara Uni-manager Management Console. Make API calls to manage operations. For example, you can manage quotas, usage statistics, specifications, and password policies. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to manage resources. For example, you can create, delete, query, or modify cloud resources. These operations are provided by Apsara Stack services. If you call an API operation to create an ECS instance or a VPC, the API operation is provided by ECS or VPC. Make API calls to query monitoring metrics of Apsara Stack services. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to perform O&M. For example, you can manage monitoring and alerting, inventories, tasks, and physical servers. These operations are provided by the Apsara Uni-manager Operations Console. For more information, see the developer guide of the corresponding Apsara Stack service. For information about API operations used to manage organization users, see Apsara Uni-manager Management Console Developer Guide. For information about the API operation used to create an ECS instance, see ECS Developer Guide. Not e If the "Use Apsara Stack SDK to make API calls" section is included in the developer guide of an Apsara Stack service, the ASAPI is supported by the Apsara Stack service. In this case, you can make API calls based on the developer guide.

#### 1.1.2 Preparations

##### 1.1.2.1 Log on to the API Tool console

You can log on to the API Tool console from the Apsara Uni-manager Management Console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. he Apsara Stack SDK Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
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

This topic describes three methods used to generate an endpoint for the Apsara Stack API (ASAPI). he Apsara Stack SDK Method 1: Use Registration Vars of Services to generate an endpoint
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
he Apsara Stack SDK i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click O&M. iii. In the left-side navigation pane, choose Product Management > Product s. iv. In the Apsara Stack O&M section, click Apsara Inf rast ruct ure Management Framework.
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
root domain, contact Apsara Stack O&M personnel. Take note of this point: Use the internetdomain parameter instead of the intranet-domain parameter. If the region value is `cn-****-****-d01` and the int ernet -domain value is `inter.****.****.com` , the following endpoint can be generated: he Apsara Stack SDK

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

he Apsara Stack SDK

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

When you use Apsara Stack SDK for Node.js to make API calls, specify a region ID. You can obtain a region ID in the Apsara Uni-manager Management Console. Procedure he Apsara Stack SDK
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

he Apsara Stack SDK

| Paramet er | T ype | Required | Descript ion |
|---|---|---|---|
| Signature | String | Yes | The signature string of the current request. For more information about how signatures are calculated, see Request signatures. |
| SignatureMethod | String | Yes | The encryption method of the signature string. Valid values: HMAC- SHA1 and HMAC- SHA256. |
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Valid values: 1.0 and 2.0. |
| SignatureNonce | String | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the yyyy- MM-ddTHH:mm:ssZ format. The time must be in UTC. Sample value: 2018-01- 01T12:00:00Z. |
| Format | String | Yes | The format in which to return the response. Set the value to JSON. |

he Apsara Stack SDK Not e

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
Method 1: Create a Maven project in IntelliJ IDEA. he Apsara Stack SDK Method 2: Convert an existing project to a Maven project. a. Right-click the project that you want to convert and select Add Framework Support .... b. Select Maven and click OK.
4. Create a folder named libs in the root directory of the project. Then, add the JAR file of Apsara
Stack SDK for Java to the libs folder, as shown in the following figure. he Apsara Stack SDK
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
he Apsara Stack SDK If the information in the following figure appears, the dependencies are added. Use Apsara Stack SDK for Java You can use the GET or POST method to call API operations provided by the ASAPI. The following sample code shows how to call API operations: he Apsara Stack SDK

```java
// 1. Create a connection to an ASClient object. ASClient client = new ASClient(); // 2. Configure the identifier of the requester. This parameter is required and used only f or identification. You can set this parameter to a random value. client.setSdkSource("<The identifier of the requester>"); Map<String, Object> parameters = new HashMap<String, Object>(); // 3. Configure the parameters for authorization. The parameter values vary based on your e nvironment. // The AccessKey ID of your Apsara Stack tenant account. parameters.put("AccessKeyId","<AccessKey ID>"); // The AccessKey secret of your Apsara Stack tenant account. parameters.put("AccessKeySecret", "<AccessKey Secret>"); // The ID of the region. parameters.put("RegionId", "<your RegionID>"); // 4. Configure parameters for an API call. In this example, the Product, Action, and Versi on parameters are configured. parameters.put("Product", "<The name of the service>"); parameters.put("Action", "<The name of the API operation>"); parameters.put("Version", "<The version of the API operation>"); // 5. Configure operation-specific parameters. parameters.put("<The name of the operation-specific parameter>", "<The value of the operati on-specific parameter>"); // 6. Configure request headers and the encryption method for the signature string. Valid v alues of the SignatureMethod parameter: HMAC-SHA1 and HMAC-SHA256. By default, HMAC-SHA256 is used. Map<String, String> headers = new HashMap<String, String>(); //headers.put("SignatureMethod", "HMAC-SHA1"); headers.put("x-acs-regionid", "<your-regionid>"); headers.put("x-acs-resourcegroupid", "<your-resourcegroupid>"); headers.put("x-acs-organizationid", "<your-organizationid>"); headers.put("x-acs-instanceid", "<your-instanceid>"); // 7. Make an API call. We recommend that you use the doPost() method. // Configure the time-out period for a connection. //client.setConnectTimeout(10000); // Configure the time-out period for a request. // client.setSocketTimeout(10000); String result = client.doPost(endpoint, headers, parameters); System.out.println(result);
```

Configure a proxy If you need to use a proxy to make API calls, use the following sample code to configure the proxy:

```
Cloud cloud = new Cloud(); // Configure the IP address of the proxy. cloud.setConfig("proxy_host", "<IP>"); // Configure the port used by the proxy. cloud.setConfig("proxy_port", "<Port>"); // 1. Create a connection to an ASClient object. ASClient client = new ASClient(cloud);
```

Request headers he Apsara Stack SDK

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

Not e Replace `2.4.7` with the actual version of Apsara Stack SDK for Python. Sample requests You can use the GET or POST method to call API operations provided by the ASAPI. he Apsara Stack SDK

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

he Apsara Stack SDK Configure a proxy Perform the following steps to configure a proxy:
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

Use Apsara Stack SDK for Node.js The following sample code shows how to use Apsara Stack SDK for Node.js to make API calls: he Apsara Stack SDK

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
value of the operation-specific parameter>" // 5. Configure request headers. AsapiClient.addHeader('x-acs-caller-sdk-source', '<The identifier of the requester>') AsapiClient.addHeader('x-acs-roleid', '<The ID of the role>') AsapiClient.addHeader('x-acs-userid', '<The ID of the user>') AsapiClient.addHeader('x-acs-organizationid', '<your-organizationid>') AsapiClient.addHeadert("x-acs-regionid", "<your-regionid>"); AsapiClient.addHeader("x-acs-resourcegroupid", "<your-resourcegroupid>"); AsapiClient.addHeader("x-acs-instanceid", "<your-instanceid>"); // 6. Make an API call and obtain the response. try {
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

Disable certificate validation The following sample code shows how to disable certificate validation:

```
Configure the environment variable. NODE_TLS_REJECT_UNAUTHORIZED=0
```

he Apsara Stack SDK Request headers

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

he Apsara Stack SDK Call examples The following sample code provides an example on how to use the RPC style to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05-26. Sample code:

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

he Apsara Stack SDK

```java
                System.out.println(instance.getInstanceId());
                System.out.println(instance.getInstanceName());
        } catch (Exception e) {
            e.printStackTrace();
```

The following sample code provides an example on how to use the ROA style to make an API call. In this example, the GetNamespaceList operation of Container Registry is called, and the API version is 2016- 06-07. Sample code:

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

he Apsara Stack SDK

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

Not ice If you send a request over HTTPS, you must enable the request to ignore SSL certificate validation.

###### 1.1.4.4.2 SDK for Go

This topic describes how to use Apsara Stack API (ASAPI) SDK for POP for Go. Prerequisites An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed. Background information Only the remote procedure call (RPC) style is supported for API calls. Call examples The following sample code provides an example on how to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05- 26. he Apsara Stack SDK Sample code:

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

he Apsara Stack SDK

```
    if err != nil {
        panic(err)
 fmt.Print(endpoint)
```

Configure proxies You can configure proxies in one of the following ways: Configure proxies by using environment variables. Set the HTTP_PROXY and HTTPS_PROXY environment variables, or set the NO_PROXY environment variable. Sample code:

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

Configure proxies on the client. Sample code:

```
// The proxies that are configured on the client take precedence over those that are conf igured by using environment variables. client.SetHttpProxy("http://x.x.x.x:xxxx") // Configure the HTTP proxy. client.GetHttpProxy() // Query the HTTP proxy. client.SetHttpsProxy("https://x.x.x.x:xxxx") // Configure the HTTPS proxy. client.GetHttpsProxy() // Query the HTTPS proxy. client.SetNoProxy("127.0.0.1,localhost") // Configure the proxy whitelist. client.GetNoProxy() // Query the proxy whitelist.
```

###### 1.1.4.4.3 SDK for Python

This topic describes how to use Apsara Stack API (ASAPI) SDK for POP for Python. Prerequisites An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed. Background information Only the remote procedure call (RPC) style is supported for API calls. he Apsara Stack SDK Call examples The following sample code provides an example on how to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05- 26. Sample code:

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

Configure proxies he Apsara Stack SDK Set the HTTP_PROXY and HTTPS_PROXY environment variables. Sample code:

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

`https` : the protocol used to transmit the request. `public.asapi.aliyuns.com/asapi/v3` : the endpoint of the ASAPI. `Action=GetOrganizationList Product=ascm Version=2019-05-10` : the API operation to call. `Id` : the ID of the organization. `<Common parameters>` : the common parameters specified in the system. he Apsara Stack SDK Protocol The ASAPI supports only HTTPS. Endpoint For more information about how to obtain an endpoint, see Generate an endpoint for the ASAPI. To specify an API operation, use the `Action, Product, and Version` parameters. For example, set `Action` to GetOrganizationList, Product to ascm, and Version to 2019-05-10. You must also specify other operation-specific parameters and common parameters. For more information, see Common parameters.

##### 1.1.5.3 Request signatures

This topic describes how to sign HTTP API requests. ASAPI uses the request signature to verify the identity of the request sender. ASAPI implements symmetric encryption by using an AccessKey pair to verify the identity of the request sender. Not e An AccessKey pair consists of an AccessKey ID and an AccessKey secret, which are issued to each user or organization in the Apsara Uni-manager Management Console. The AccessKey ID is used to verify identities of users, and the AccessKey secret is used to encrypt and verify signature strings. You must keep your AccessKey secret confidential. ASAPI provides SDKs for Node.js, Python, and Java to facilitate complex signature calculation. For more information, see Obtain the core package for ASAPI. Step 1: Create a canonicalized query string
1. Arrange the request parameters in alphabetical order, including all common and operation-specific
parameters except the `Signature` parameter. Not e If you use the GET method to send a request,these parameters are connected by ampersands (&) and included in the request URL. The first request parameter follows a question mark (?).
2. Encode the request parameters and their values in UTF-8 based on RFC 3986. The following rules
apply in the encoding process: Letters, digits, and special characters such as hyphens ( `-` ), underscores ( `_` ), and periods ( `.` ) do not need to be encoded. he Apsara Stack SDK Other characters must be percent encoded in the %XY format. `XY` represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks ( `"` ) are encoded as %22 . Extended UTF-8 characters are encoded in the %XY%ZA… format. Spaces must be encoded as %20 . Do not encode spaces as plus signs ( `+` ). This encoding method is similar to but different from the `application/x-www-form-urlencoded` MIME encoding algorithm. If you use `java.net.URLEncoder` from the Java standard library, use `percentEncode` to encode request parameters and their values. In the encoded query string, replace the plus signs ( `+` ) with %20 , asterisks ( `*` ) with %2A , and %7E with tildes ( ~ ). This way, you can obtain an encoded string that matches the preceding encoding rules.

```java
private static final String ENCODING = "UTF-8"; private static String percentEncode(String value) throws UnsupportedEncodingException
```

`{`

```
    return value != null ? URLEncoder.encode(value, ENCODING).replace("+", "%20").rep
lace("*", "%2A").replace("%7E", "~") : null;
```

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

he Apsara Stack SDK Not e When you calculate the signature, the key value specified by RFC 2104 is your `AccessKey secret` plus an ampersand (&), which has an ASCII value of 38. For more information, see Obtain an AccessKey pair.
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

You can use browsers or tools such as cURL and Wget to initiate an HTTP request for calling the `DescribeRegions` operation to query the Alibaba Cloud region list. Example 2: Use t he st andard library of t he programming language he Apsara Stack SDK `GetOrganizationList` is used in this example to query regions. For example, `AccessKeyID` is set to testid, `AccessKeySecret` is set to testsecret, and all request parameters are stored in a Java `Map<String, String>` object.
1. Predefine an encoding method.

```java
private static final String ENCODING = "UTF-8"; private static String percentEncode(String value) throws UnsupportedEncodingException {
        return value != null ? URLEncoder.encode(value, ENCODING).replace("+", "%20").r
eplace("*", "%2A").replace("%7E", "~") : null;
```

2. Predefine the time format for the `Timestamp` parameter. Specify the `Timestamp` parameter in
the ISO 8601 format. The time must be in UTC+0.

```java
private static final String ISO8601_DATE_FORMAT = "yyyy-MM-dd'T'HH:mm:ss'Z'"; private static String formatIso8601Date(Date date) {
    SimpleDateFormat df = new SimpleDateFormat(ISO8601_DATE_FORMAT);
    df.setTimeZone(new SimpleTimeZone(0, "GMT"));
    return df.format(date);
```

3. Create a request string.
he Apsara Stack SDK

```
final String HTTP_METHOD = "GET"; Map parameters = new HashMap(); // Specify request parameters. parameters.put("Product", "ascm"); parameters.put("Action", "GetOrganizationList"); parameters.put("Version", "2019-05-10"); parameters.put("AccessKeyId", "testid"); parameters.put("RegionId", "cn-region-test"); parameters.put("Timestamp", formatIso8601Date(new Date())); parameters.put("SignatureMethod", "HMAC-SHA1"); parameters.put("SignatureVersion", "1.0"); parameters.put("SignatureNonce", UUID.randomUUID().toString()); parameters.put("Format", "JSON"); parameters.put("Id", "1"); // Arrange request parameters. String[] sortedKeys = parameters.keySet().toArray(new String[]{}); Arrays.sort(sortedKeys); final String SEPARATOR = "&"; // Create a string-to-sign. StringBuilder stringToSign = new StringBuilder(); stringToSign.append(HTTP_METHOD).append(SEPARATOR); stringToSign.append(percentEncode("/")).append(SEPARATOR); StringBuilder canonicalizedQueryString = new StringBuilder(); for(String key : sortedKeys) {
    // Encode the key and the value.
    canonicalizedQueryString.append("&")
    .append(percentEncode(key)).append("=")
    .append(percentEncode(parameters.get(key)));
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

he Apsara Stack SDK
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

`]` Sample error response If a request fails, the following information is returned. For more information, see the developer guide of the corresponding Apsara Stack service. `{`

```json
    "code": "asapi.server.api.notfound",// The error code.
    "eagleEyeTraceId": "xxx-xxx-xxx-xxx", // The trace ID provided by EagleEye.
    "asapiSuccess": false, // Indicates whether the request is successful.
    "hostId": "xxxx", // The ID of the host.
    "message": "Failed to ....", // The message returned.
    "asapiErrorMessage": "Failed to ....", // The error message provided by the ASAPI.
    "asapiErrorCode": "asapi.server.api.notfound" // The error code provided by the ASAPI.
```

API invocation

## 2 Container Service API invocation

invocation

### 2.1 Overview

To use the APIs provided by Container Service, you can send HTTP requests to the endpoint of Container Service APIs and include specific parameters in the requests. The system returns a response after processing the request.
2. Request structure

### 2.2 Common parameters

This topic lists the common request headers, common response headers, and common parameters that are required in Apsara Stack API (ASAPI) requests when you make Container Service API requests. Common request headers Common request parameters must be included in all Container Service API requests.

| Parameter | Description | Required |
|---|---|---|
| Authorization | The authentication information that is used to check the authenticity of a request. The string must follow the AccessKeyId:Signature format. | Yes |
| Content-Length | The length of the HTTP request content. This length is specified in RFC 2616. | Yes |
| Content-Type | The type of HTTP request content. This type must follow the format that is specified in RFC 2616. | Yes |
| Content-MD5 | The 128-bit MD5 hash value of the HTTP message body. The hash value is encoded in the Base64 format. We recommend that you set this parameter for all requests to prevent parameter tampering. | Yes |

API invocation

| Parameter | Description | Required |
|---|---|---|
| Date | The time when a request is created. The time must be in GMT. If the time between when the request is sent and when the request is received exceeds 15 minutes, the request is deemed invalid. | Yes |
| Host | The host to which the request is sent, for example, diku.aliyuncs.com. | Yes |
| Accept | The type of response that is required by the client. Valid values: application/json and application/xml. | Yes |
| x-acs-version | The version number of the API. Set the value to 2015-12-15. | Yes |
| x-acs-region-id | The region where the Elastic Compute Service (ECS) instance is deployed. | Yes |
| x-acs-signature-nonce | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. | Yes |
| x-acs-signature-method | The encryption method of the signature string. Set the value to HMAC-SHA1. | Yes |

Examples

```
GET /clusters HTTP/1.1 Host: cs.aliyuncs.com Accept: application/json User-Agent: cs-sdk-python/0.0.1 (Darwin/15.2.0/x86_64;2.7.10) x-acs-signature-nonce: f63659d4-10ac-483b-99da-ea8fde61eae3 Authorization: acs <yourAccessKeyId>:<yourSignature> x-acs-signature-version: 1.0 Date: Wed, 16 Dec 2015 11:18:47 GMT x-acs-signature-method: HMAC-SHA1 Content-Type: application/json;charset=utf-8 X-Acs-Region-Id: cn-beijing Content-Length: 0
```

Common parameters required in ASAPI requests Additional common parameters are required when you make ASAPI requests. The following table lists these common parameters. API invocation

| Parameter | Description | Required |
|---|---|---|
| x-ascm-product-ak | The AccessKey pair. You can check your AccessKey pair in the Alibaba Cloud Management Console. | Yes |
| x-ascm-product-name | The name of the service that supports the API. Set the value to cs for Container Service. | Yes |
| x-ascm-product-version | The version number of the API. Set the value to 2015-12-15. | Yes |
| x-acs-regionid | The ID of the region where the Container Service cluster is deployed. | Yes |
| x-acs-organizationid | The ID of the organization to which the Container Service cluster belongs. | Yes |
| x-acs-resourceGroupId | The ID of the resource set of the Container Service cluster. | Yes |
| x-acs-roleid | The ID of the role. | Yes |

Common response parameters Every response returns a unique request ID regardless of whether the call is successful. Examples XML format:

```
<? xml version="1.0" encoding="UTF-8"? > <!—Result Root Node--> <Interface Name + Response>
 | <! -Returned Request Tag -->
 | <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
 | <! -Return Result Data -->
<Interface Name+Response>
```

JSON format `{`

```json
    "RequestId": "4C467B38-3910-447D-87BC-AC049166F216"
    /* Return Result Data */
```

### 2.3 Request syntax

This topic describes the syntax that you must follow when you make Container Service API requests. API invocation Endpoint The endpoints of the API operations are classified into the following types:

| cs.${global:internet-domain} |   |   |
|---|---|---|
| on: | cs.${global:region}.${global:internet-domain} |   |

You must add the /roa prefix to the endpoint that you use to make an Apsara Stack API (ASAPI) request. For example, if the /clusters endpoint is used to create a cluster, you must include /roa/clust ers in your ASAPI request. Protocols HTTP and HTTPS are supported. We recommend that you send requests over HTTPS to enhance security. Request methods The following HTTP methods are supported: PUT, POST, GET, and DELETE. Request parameters Each request must contain common request parameters and parameters unique to specific operations. Request encoding All requests and responses are encoded in the UTF-8 format.

### 2.4 Response parameters

The response data is returned in a unified format. If status code `2xx` is returned, it indicates that the API call is successful. If status code `4xx` or `5xx` is returned, it indicates that the API call has failed. For successful API calls, response data is returned in XML or JSON format. You can pass a parameter to specify the format when you call the API. The default format is XML. The following example is formatted for readability. The actual result is not formatted with line feeds or indentation.

### 2.5 Sign API requests

This topic describes how to sign API requests to protect Container Service from unauthorized access. Introduction Apsara Stack issues an AccessKey pair to each Apsara Stack tenant account. Each AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey ID is used to verify the identity of the user. The AccessKey secret is used to encrypt and verify the signature string. You must keep your AccessKey secret confidential. You can obtain and manage the AccessKey pair in the Apsara Unimanager Management Console. Container Service verifies every request it receives. All requests to Container Service must contain signature information. Container Service implements symmetric encryption with an AccessKey pair to verify the identity of the request sender. Container Service accepts only requests that are validated by verification codes. Invalid requests are rejected and the HTTP status code 403 is returned. You can add the Authorization header to every HTTP request and include the signature in the header. API invocation You must add the signature to the Authorization header in the following format: `Authorization: acs`

```
[Access Key Id]:[Signature] .
```

The `Signature` is calculated based on the following rules:

```
Signature = base64(hmac-sha1(VERB + "\n"
            + ACCEPT + "\n"
            + Content-MD5 + "\n"
            + Content-Type + "\n"
            + Date + "\n"
            + CanonicalizedHeaders + "\n"
            + CanonicalizedResource))
```

| VERB | in |
|---|---|
| ACCEPT |   |

`VERB` indicates the HTTP method. Example: `PUT` . `ACCEPT` specifies the type of response that is required by the client. Valid values: application/json and application/xml.

| Content-MD5 |   | i |
|---|---|---|
| Content-Type |   |   |
| Date | indicate |   |

`Content-MD5` indicates the MD5 hash value of the request content. `Content-Type` indicates the type of request content. `Date` indicates the time when the request was sent. This parameter is required. The time must be in GMT. If the time between when the request was sent and when the request was received exceeds 15 minutes, the request is deemed invalid and the HTTP status code 400 is returned. For example, `Thu,` `17 Mar 2012 18:49:58 GMT` can be used. `CanonicalizedHeaders` indicates the header fields that are prefixed with `x-acs-` in the request. `CanonicalizedResource` indicates the URI of the requested resource. For example, /clusters? na `me=my-clusters&resource=new` can be used. `CanonicalizedHeaders` (headers that start with `x-acs-` ) must comply with the following specifications before the signature is verified:

| x-acs- | to lowercase lette |
|---|---|
| x-acs-meta-name: TaoBao |   |

1. Convert the names of all HTTP request headers prefixed with `x-acs-` to lowercase letters. For
example, you must convert `X-ACS-Meta-Name: TaoBao` into `x-acs-meta-name: TaoBao` . Header field names are case-insensitive. We recommend that you use lowercase letters.
2. If a header field value is too long, replace specific delimiters with spaces. The delimiters include \t
, \n , \r , and \f .
3. Sort all HTTP request headers that are obtained from the preceding step in alphabetical order.
4. Delete spaces from each side of a delimiter between the request header and its content. For
example, convert `x-acs-meta-name: TaoBao,Alipay` into `x-acs-meta-name:TaoBao,Alipay` .
5. Separate all headers and content with delimiters ( \n ) to form the final canonicalized headers.
Not e `CanonicalizedResource` must follow this format: `CanonicalizedResource` specifies the URIs of the requested resources. You must sort sub-resources in alphabetical order and combine them with the `&` delimiter to form a string. In the following example, the string that follows the question mark ( ? ) indicates CanonicalizedResource.

```
http://cs.aliyuncs.com/clusters?name=my-clusters&resource=new
```

API invocation The value of `CanonicalizedResource` must be in the following format:

```
/clusters? name=my-clusters&resource=new
```

The following example shows how to sign an API request. The `access_key_id` and `access_key_secret` fields separately specify the AccessKey ID and AccessKey secret that are used in the example. We recommend that you use your own program to construct an API request. You can then calculate the signature that is used in the following example. Sample request:

```json
POST http://cs.aliyuncs.com/clusters?param1=value1&param2=value2 HTTP/1.1 Accept-Encoding: identity Content-Length: 210 Content-MD5: 6U4ALMkKSj0PYbeQSHqgmA== x-acs-version: 2015-12-15 Accept: application/json User-Agent: cs-sdk-python/0.0.1 (Darwin/15.2.0/x86_64;2.7.10) x-acs-signature-nonce: fbf6909a-93a5-45d3-8b1c-3e03a7916799 x-acs-signature-version: 1.0 Date: Wed, 16 Dec 2015 12:20:18 GMT x-acs-signature-method: HMAC-SHA1 Content-Type: application/json;charset=utf-8 X-Acs-Region-Id: cn-beijing Authorization: acs <yourAccessKeyId>:<yourSignature> {"password": "Just$****","instance_type": "ecs.m2.medium","name": "my-test-cluster-9708**** ","size": 1,"network_mode": "vpc","data_disk_category": "cloud","data_disk_size": 10,"ecs_i mage_id": "m-253l****l"}
```

Const ruct t he request Calculate the values of `Content-Length` and `Content-MD5` . `Content-Length` specifies the length of the content body. Not e The body cannot start with a space or line feed.

```json
body: {"password": "Just$****","instance_type": "ecs.m2.medium","name": "my-test-cluster-97 08****","size": 1,"network_mode": "vpc","data_disk_category": "cloud","data_disk_size": 10, "ecs_image_id": "m-253ll****"} Content-Length: 210
```

`Content-MD5` : The MD5 value is calculated based on the following rules: API invocation

```json
body: {"password": "Just$****","instance_type": "ecs.m2.medium","name": "my-test-cluster-97 08****","size": 1,"network_mode": "vpc","data_disk_category": "cloud","data_disk_size": 10, "ecs_image_id": "m-253ll****"}
# Calculate the MD5 value of the body
md5(body): e94e002cc90a4a3d0f61b790487aa098
# Convert the MD5 hash value into a byte array. Convert every two hexadecimal digits into o
ne byte.
# Example: e9 -> 11111111111111111111111111101001 -> -23
bytes(md5(body)): {[-23], [78], [0], [44], [-55], [10], [74], [61], [15], [97], [-73], [-11 2], [72], [122], [-96], [-104]}
# Convert the byte array into a string that is encoded in the Base64 format.
base64(bytes(md5(body))): 6U4ALMkKSj0PYbeQSHqgmA== Content-MD5: 6U4ALMkKSj0PYbeQSHqgmA==
```

Process `CanonicalizedHeaders`

```bash
# List all header fields prefixed with 'x-acs-'
x-acs-version: 2015-12-15 x-acs-signature-nonce: ca480402-7689-43ba-acc4-4d2013d9d8d4 x-acs-signature-version: 1.0 x-acs-signature-method: HMAC-SHA1 X-Acs-Region-Id: cn-beijing
# Convert the header field name to lowercase, delete the spaces at the start and end of eac
h line, and sort the header fields in lexicographical order. Delete spaces from each side o f a delimiter between the request header and its content.
# Note: No line feed in the last line.
x-acs-region-id:cn-beijing x-acs-signature-method:HMAC-SHA1 x-acs-signature-nonce:fbf6909a-93a5-45d3-8b1c-3e03a7916799 x-acs-signature-version:1.0 x-acs-version:2015-12-15
```

Calculate `CanonicalizedResource` In this example, the length of the `CanonicalizedResource` field value is 27 bytes. Not e A line feed \n exists at the end of the first line.

```
/clusters? param1=value1&param2=value2
```

Calculate `Signature` Construct the value of `SignatureString` . In this example, the length of the signature string is 307 bytes. Apart from the last line, each line has a line feed \n at the end. API invocation

```
POST application/json 6U4ALMkKSj0PYbeQSHqgmA== application/json;charset=utf-8 Wed, 16 Dec 2015 12:20:18 GMT x-acs-region-id:cn-beijing x-acs-signature-method:HMAC-SHA1 x-acs-signature-nonce:fbf6909a-93a5-45d3-8b1c-3e03a7916799 x-acs-signature-version:1.0 x-acs-version:2015-12-15 /clusters? param1=value1&param2=value2
```

Calculate `Signature` base on the following rules:

```bash
# Use the AccessKey secret to encrypt the value of SignatureString. In this example, access
_key_secret specifies the AccessKey secret. hmac-sha1(SignatureString): fee03d405e421ebaf514adec881038c4b313584d
#  Convert the encrypted string into a byte array, which is similar to calculating Content-
MD5.
# Convert the byte array into a string that is encoded in the Base64 format. The output is
the signature string. base64(bytes(hmac-sha1(SignatureString))): ZmVlMDNkNDA1ZTQyMWViYWY1MTRhZGVjODgxMDM4YzRiMzEz NTg0ZA== Signature: ZmVlMDNkNDA1ZTQyMWViYWY1MTRhZGVjODgxMDM4YzRiMzEzNTg0ZA==
```

The signature string is calculated. Add other header fields to your request and set the value of Signature to the calculated signature string. The following sample code shows the signed API request.

```json
POST http://cs.aliyuncs.com/clusters?param1=value1&param2=value2 HTTP/1.1 Accept-Encoding: identity Content-Length: 210 Content-MD5: 6U4ALMkKSj0PYbeQSHqgmA== x-acs-version: 2015-12-15 Accept: application/json User-Agent: cs-sdk-python/0.0.1 (Darwin/15.2.0/x86_64;2.7.10) x-acs-signature-nonce: fbf6909a-93a5-45d3-8b1c-3e03a7916799 x-acs-signature-version: 1.0 Date: Wed, 16 Dec 2015 12:20:18 GMT x-acs-signature-method: HMAC-SHA1 Content-Type: application/json;charset=utf-8 X-Acs-Region-Id: cn-beijing Authorization: acs <yourAccessKeyId>:<yourSignature> {"password": "Just$****","instance_type": "ecs.m2.medium","name": "my-test-cluster-9708**** ","size": 1,"network_mode": "vpc","data_disk_category": "cloud","data_disk_size": 10,"ecs_i mage_id": "m-253ll****"}
```

## 3 Cluster API list

### 3.1 Clusters

#### 3.1.1 CreateCluster

Creates a standard dedicated Kubernetes cluster. Request syntax

```
POST /clusters HTTP/1.1
```

`{`

```json
  "name" : "String",
  "region_id" : "String",
  "cluster_type" : "String",
  "kubernetes_version" : "String",
  "runtime" : {
    "name" : "String",
    "version" : "String"
```

`},`

```json
  "vpcid" : "String",
  "container_cidr" : "String",
  "service_cidr" : "String",
  "security_group_id" : "String",
  "is_enterprise_security_group" : Boolean,
  "snat_entry" : Boolean,
  "endpoint_public_access" : Boolean,
  "ssh_flags" : Boolean,
  "timezone" : "String",
  "node_cidr_mask" : "String",
  "user_ca" : "String",
  "user_data" : "String",
  "cluster_domain" : "String",
  "tags" : [ {
    "key" : "String",
    "value" : "String"
  } ],
  "addons" : [ {
    "name" : "String",
    "config" : "String",
    "disabled" : Boolean
  } ],
  "taints" : [ {
    "key" : "String",
    "value" : "String",
    "effect" : "String"
  } ],
  "cloud_monitor_flags" : Boolean,
  "platform" : "String",
  "os_type" : "String",
  "cpu_policy" : "String",
```

`"` `d``"`

```
"Sti
```

`"`

```json
  "proxy_mode" : "String",
  "node_port_range" : "String",
  "login_password" : "String",
  "master_count" : Long,
  "master_vswitch_ids" : [ "String" ],
  "master_instance_types" : [ "String" ],
  "master_system_disk_category" : "String",
  "master_system_disk_size" : Long,
  "num_of_nodes" : Long,
  "vswitch_ids" : [ "String" ],
  "worker_vswitch_ids" : [ "String" ],
  "worker_instance_types" : [ "String" ],
  "worker_system_disk_category" : "String",
  "worker_system_disk_size" : Long,
  "worker_data_disks" : [ {
    "category" : "String",
    "size" : Long,
    "encrypted" : "String",
    "auto_snapshot_policy_id" : "String"
  } ],
  "instances" : [ "String" ],
  "format_disk" : Boolean,
  "keep_instance_name" : Boolean,
  "deletion_protection" : Boolean,
  "disable_rollback" : Boolean,
  "timeout_mins" : Long
```

Request parameters Request body parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| name | String | Yes | cluster-demo | The name of the cluster. The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). It cannot start with a hyphen. |
| region id _ | String | Yes | cn-beijing | The ID of the region where you want to deploy the cluster. |
| cluster type _ | String | Yes | Kubernetes | The type of cluster. Valid values: Kubernetes : dedicated Kubernetes cluster. ManagedKubernetes : managed edge Kubernetes cluster. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| kubernetes versi _ on | String | No | 1.16.9-aliyun.1 | The version of the cluster. The cluster versions provided by Container Service are consistent with the open source versions. We recommend that you select the latest version. If you do not specify this parameter, the latest version is used. You can create clusters of the latest two versions in the Container Service console. You can create clusters of earlier versions by calling API operations. |
| runtime | runtime | No | {"name": "docker", "version": "19.03.5"} | The container runtime of the cluster. The following runtimes are supported: containerd , Docker , and Sandboxed-Container . The default runtime is Docker . You must specify the name and version of the container runtime. name : the name of the container runtime. version : the version of the container runtime. |
| vpcid | String | Yes | vpc- 2zeik9h3ahvv2zz 95**** | The virtual private cloud (VPC) where the cluster is deployed. You must specify a VPC when you create the cluster. |
| container cidr _ | String | Yes | 172.20.0.0/16 | The CIDR block of pods. This CIDR block cannot overlap with the CIDR block of the VPC where the cluster is deployed. If the VPC is automatically created by the system, the CIDR block of pods is set to 172.16.0.0/16 by default. Not ice This parameter is required if the cluster uses the Flannel plug-in. This parameter is not required if the cluster uses the Terway plug-in. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| service cidr _ | String | Yes | 172.21.0.0/20 | The CIDR block of Services. Valid values: 10.0.0.0/16-24, 172.16- 31.0.0/16-24, and 192.168.0.0/16-24. The CIDR block of Services cannot overlap with the CIDR block of the VPC (10.1.0.0/21) or the CIDR blocks of existing clusters in the VPC. You cannot modify the CIDR block of Services after the cluster is created. By default, the CIDR block of Services is set to 172.19.0.0/20. |
| is enterprise sec _ _ urity group _ | Boolean | No | true | Specifies whether to create an advanced security group. This parameter takes effect only if security group id is left empty. _ _ Not e To use a basic security group, make sure that the sum of the number of nodes in the cluster plus the number of pods that use Terway does not exceed 2,000. Therefore, we recommend that you specify an advanced security group for a cluster that has Terway installed. true : creates an advanced security group. false : does not create an advanced security group. Default value: true . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| snat entry _ | Boolean | No | true | Specifies whether to configure Source Network Address Translation (SNAT) rules for the VPC where your cluster is deployed. Valid values: true: automatically creates a Network Address Translation (NAT) gateway and configures SNAT rules. Set this parameter to true if nodes and applications in the cluster need to access the Internet. false: does not create a NAT gateway or configure SNAT rules. In this case, nodes and applications in the cluster cannot access the Internet. Default value: true. |
| endpoint public _ _ access | Boolean | No | true | Specifies whether to enable Internet access for the cluster. You can use an elastic IP address (EIP) to expose the API server. This way, you can access the cluster over the Internet. true : enables Internet access. false : disables Internet access. If you set this parameter to false, the API server cannot be accessed over the Internet. Default value: false . |
| ssh flags _ | Boolean | No | true | Specifies whether to enable Secure Shell (SSH) logon over the Internet. true : enables SSH logon over the Internet. false : disables SSH logon over the Internet. Default value: false . |
| node cidr mask _ _ | String | No | 25 | The maximum number of IP addresses that can be assigned to nodes. This number is determined by the specified pod CIDR block. This parameter takes effect only if the cluster uses the Flannel plug-in. Default value: 26 . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| user ca _ | String | No | -----BEGIN CERTIFICATE----- **** | The custom Certificate Authority (CA) certificate for the cluster. |
| user data _ | String | No | IyEvdXNyL2Jpbi9i YXNoCmVjaG8gIk hlbGxvIEFD**** | The user-defined data of the node. For more information, see the User- defined data chapter in the Elastic Compute Service (ECS) documentation. |
| cluster domain _ | String | No | cluster.local | The domain name of the cluster. The domain name consists of one or more parts that are separated with periods (.).Each part cannot exceed 63 characters in length, and can contain lowercase letters, digits, and hyphens (-). Each part must start and end with a lowercase letter or digit. |
| image id _ | String | No | m- bp16z7xko3vvv8 gt**** | Specifies a custom image for nodes. By default, the system image is used. You can select a custom image to replace the default image. |
| tags | Array of tag | No |   | The labels to be added to nodes. Labeling rules: Each label consists of a case- sensitive key-value pair. You can add up to 20 labels. When you add a label, you must specify a unique key but you can leave the value empty. A key cannot exceed 64 characters in length and a value cannot exceed 128 characters in length. Keys and values cannot start with aliyun, acs:, https://, or http://. |
|   |   |   |   | The list of add-ons to be installed. When you create a cluster, you can set the addons parameter to install specific add-ons. Net work plug-in: required. Supported network plug-ins are Flannel and Terway. Select one of the plug-ins for the cluster. Specify the Flannel plug-in in the following format: |

|   | Parameter | Type | Required | Example | [{"name":"flannel","config":""}]. Description Specify the Terway plug-in in the |
|---|---|---|---|---|---|
|   | addons | Array of addon | No |   | following format: [{"name": "terway-eniip","config": ""}]. Volume plug-in: required. Supported volume plug-ins are CSI and FlexVolume . Specify the CSI plug-in in the following format: [{"name":"csi- plugin","config": ""},{"name": "csi- provisioner","config": ""}]. Specify the FlexVolume plug-in in the following format: [{"name": "flexvolume","config": ""}]. Log Service component : optional. We recommend that you enable Log Service. If Log Service is disabled, you cannot use the cluster auditing feature. To use an existing Log Service p roject , specify the component in the following format: [{"name": "logtail-ds","config": " {\"IngressDashboardEnabled\":\"tru e\",\"sls project name\":\"your sls _ _ _ project name\"}"}]. _ _ To create a Log Service project , specify the component in the following format: [{"name": "logtail-ds","config": " {\"IngressDashboardEnabled\":\"tru e\"}"}]. Ingress cont roller: optional. By default, the nginx-ingress- controller component is installed for dedicated Kubernetes clusters. To install nginx-ingress-controller and enable Internet access, specify the component in the following format: [{"name":"nginx-ingress- controller","config":" {\"IngressSlbNetworkType\":\"intern et\"}"}]. To disable the automatic installation of nginx-ingress-controller, specify the component in the following format: [{"name": "nginx-ingress- controller","config": "","disabled": true}]. Event cent er: optional. By default, the event center feature is enabled. |

| Log Service p |   |
|---|---|

|   | roject |
|---|---|

| nginx-ingress- |   |
|---|---|

| Parameter | Type | Required | Example | The event center feature allows you to Description log Kubernetes events, query events, |
|---|---|---|---|---|
|   |   |   |   | and configure alerts for the events. Logstores that are associated with the Kubernetes event center are free of charge for the first 90 days. Enable the ack-node-problem-detector component in the following format: [{"name":"ack-node-problem- detector","config":" {\"sls project name\":\"your sls proje _ _ _ _ ct name\"}"}]. _ |
| taints | Array of taint | No |   | The taints to be added to nodes. Taints are added to nodes to prevent pods from being scheduled to inappropriate nodes. However, toleration rules allow pods to be scheduled to nodes with matching taints. |
| cloud monitor fl _ _ ags | Boolean | No | true | Specifies whether to install the CloudMonitor agent. Valid values: true : installs the CloudMonitor agent. false : does not install the CloudMonitor agent. Default value: false . |
| platform | String | No | CentOS | The release version of the operating system. Valid values: CentOS AliyunLinux QbootAliyunLinux Qboot Windows WindowsCore Default value: AliyunLinux . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| os type _ | String | No | Linux | The type of operating system. Valid values: Windows Linux Default value: Linux . |
| cpu policy _ | String | No | none | The CPU policy. The following policies are supported if the cluster version is 1.12.6 or later. static : This policy allows pods with specific resource characteristics on the node to be granted with enhanced CPU affinity and exclusivity. none : This policy indicates that the default CPU affinity is used. Default value: none . |
| proxy mode _ | String | No | ipvs | The kube-proxy mode. iptables : iptables is a kube- proxy mode. It uses iptables rules to conduct Service discovery and load balancing. The performance of this mode is limited by the size of the cluster. This mode is suitable for clusters that run a small number of Services. IPVS is a high-performance kube-proxy mode. It uses Linux IP Virtual Server (IPVS) to conduct Service discovery and load balancing. This mode is suitable for clusters that run a large number of Services. We recommend that you use this mode in scenarios where high-performance load balancing is required. Default value: ipvs . |
| node port range _ _ | String | No | 30000~32767 | The node port range. Valid values: 30000 to 65535. Default value: 30000-32767 . |

| eveloper Guide·Clus | ter API list |   |   | Container Service for Kubernete |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| login password _ | String | Yes | Hello@1234 | The password for SSH logon. You must set this parameter or the key pair _ parameter. The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. |
| master count _ | Long | No | 3 | The number of master nodes to be created. Valid values: 3 and 5 . Default value: 3 . |
| master vswitch i _ _ ds | Array of String | Yes | vsw- 2ze3ds0mdip0hd z8i**** | The IDs of vSwitches. |
| master instance _ _ types | Array of String | Yes | ecs.n4.xlarge | The instance types of master nodes. For more information, see the Instance types chapter of ECS User Guide. |
| master system d _ _ isk category _ | String | Yes | cloud ssd _ | The type of system disk that is specified for master nodes. Valid values: cloud efficiency : ultra disk. _ cloud ssd : standard SSD. _ cloud essd : enhanced SSD. _ Default value: cloud ssd . The _ default value may vary in different zones. |
| master system d _ _ isk size _ | Long | Yes | 120 | The size of the system disk that is specified for master nodes. Valid values: 40 to 500. Unit: GiB. Default value: 120 . |
| num of nodes _ _ | Long | Yes | 3 | The number of worker nodes to be created. Valid values: 0 to 100. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| worker vswitch i _ _ ds | Array of String | Yes | vsw- 2ze3ds0mdip0hd z8i**** | The list of vSwitch IDs. You can specify 1 to 20 vSwitches. We recommend that you select vSwitches in different zones to ensure high availability. |
| worker instance _ _ types | Array of String | Yes | ecs.n4.large | The instance types of worker nodes. You must specify at least one instance type. For more information, see the Instance types chapter of ECS User Guide. Not e The instance types are listed in descending order of priority. If worker nodes fail to be created based on the instance type of the highest priority, the system attempts to create worker nodes by using the instance type of the next highest priority. |
| worker system d _ _ isk category _ | String | Yes | cloud efficiency _ | The type of system disk that is specified for worker nodes. Valid values: cloud efficiency : ultra disk. _ cloud ssd : standard SSD. _ Default value: cloud ssd . _ |
| worker system d _ _ isk size _ | Long | Yes | 120 | The size of the system disk that is specified for worker nodes. Unit: GiB. Valid values: 40 to 500. The value of this parameter must be at least 40 and greater than or equal to the size of the image. Default value: 120. |
| worker data disk _ _ s | Array | No |   | The configurations of data disks that are mounted to worker nodes. Each configuration includes disk type and disk size. |
| instances | Array of String | No | i- 2ze4zxnm36vq00 xn**** | The names of instances. |

|   | Developer Guide·Clus | ter API list |   |   | Container Service for Kubernete | s |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| format disk _ | Boolean | No | false | Specifies whether to mount a data disk to nodes that are created on existing ECS instances. Valid values: true : stores the data of containers and images on a data disk. The original data on the disk will be overwritten. Back up data before you mount the disk. false : does not store the data of containers and images on a data disk. Default value: false . How to mount a data disk: If the ECS instances have data disks mounted and the file system of the last data disk is not initialized, the system automatically formats the data disk to ext4. Then, the system mounts the data disk to /var/lib/docker and /var/lib/kubelet. The system does not create and mount a new data disk if no data disk has been mounted to the ECS instances. |
| keep instance na _ _ me | Boolean | No | true | Specifies whether to retain the names of existing ECS instances that are used in the cluster. true : retains the names. false : does not retain the names. The new names are assigned by the system. Default value: true . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| deletion protecti _ on | Boolean | No | true | Specifies whether to enable deletion protection for the cluster. After deletion protection is enabled, the cluster cannot be deleted in the console or by calling API operations. Valid values: true : enables deletion protection for the cluster. This way, the cluster cannot be deleted in the console or by calling API operations. false : disables deletion protection for the cluster. This way, the cluster can be deleted in the console or by calling API operations. Default value: false . |
| disable rollback _ | Boolean | No | true | Specifies whether to perform a rollback when the cluster fails to be created. Valid values: true : performs a rollback when the cluster fails to be created. false : does not perform a rollback when the cluster fails to be created. Default value: true . |
| timeout mins _ | Long | No | 60 | Specifies the timeout period of cluster creation. Unit: minutes. Default value: 60 . |

Response syntax

```
HTTP/1.1 200
```

`{`

```json
  "cluster_id" : "String",
  "request_id" : "String",
  "task_id" : "String"
```

Response parameters Response body parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| cluster id _ | String | cb95aa626a47740af bf6aa099b650**** | The ID of the cluster. |
| request id _ | String | 687C5BAA-D103- 4993-884B- C35E4314A1E1 | The ID of the request. |
| task id _ | String | T- 5a54309c80282e39e a00002f | The ID of the task. |

Examples Sample requests

```
POST /clusters
```

`{`

```json
    "cluster_type":"Kubernetes",
    "name":"dedicated Kubernetes cluster",
    "region_id":"cn-zhangjiakou",
    "disable_rollback":true,
    "timeout_mins":60,
    "kubernetes_version":"1.18.8-aliyun.1",
    "snat_entry":true,
    "endpoint_public_access":true,
    "ssh_flags":true,               // Specifies whether master nodes in the cluster can be
accessed by using SSH.
    "cloud_monitor_flags":true,
    "deletion_protection":true,
    "node_cidr_mask":"26",
    "user_ca":"-----BEGIN CERTIFICATE-----\n***", // The custom CA certificate.
    "proxy_mode":"ipvs",
    "timezone":"Asia/Shanghai",
    "tags":[
```

`{`

```json
            "key":"tag-k",
            "value":"tag-v"
```

`],`

```json
    "addons":[
```

`{`

```json
            "name":"flannel"
```

`},` `{`

```json
            "name":"arms-prometheus"
```

`},` `{`

```json
            "name":"csi-plugin"
```

`},` `{`

```json
            "name":"csi-provisioner"
```

`},` `{`

```json
            "name":"logtail-ds",
            "config":"{"IngressDashboardEnabled":"true"}"
```

`},` `{`

```json
            "name":"ack-node-problem-detector",
            "config":"{"sls_project_name":""}"
```

`},` `{`

```json
            "name":"nginx-ingress-controller",
            "config":"{"IngressSlbNetworkType":"internet"}"
```

`],`

```json
    "os_type":"Linux",
    "platform":"AliyunLinux",
    "user_data":"IyEvdXNyL2Jpbi9iYXNoCmVjaG8gIkhlbGxvIEFDSyEi",
    "node_port_range":"30000-32767",      // The node port range. Valid values: 30000 to 65
535.
    "login_password":"Hello1234",
    "worker_auto_renew":true,
    "worker_auto_renew_period":1,
    "cpu_policy":"none",
    "cluster_domain":"cluster.local",
    "api_audiences":"kubernetes.default.svc",
    "taints":[
```

`{`

```json
            "key":"key",
            "value":"value",
            "effect":"NoSchedule"
```

`],`

```json
    "master_count":3,                 // The number of master nodes. Valid values: 3 and 5.
    "master_vswitch_ids":[            // The IDs of the vSwitches that are specified for ma
ster nodes.
        "vsw-8vbmoffowsztjaawjtyzo",
        "vsw-8vbmoffowsztjaawjtyzo",
        "vsw-8vbmoffowsztjaawjtyzo"
```

`],`

```json
    "master_instance_types":[         // The instance types of master nodes.
        "ecs.c6.large",
        "ecs.c6.large",
        "ecs.c6.large"
```

`],`

```json
    "master_system_disk_category":"cloud_essd",   // The type of system disk that is specif
ied for master nodes.
    "master_system_disk_size":120,                // The size of the system disk that is sp
ecified for master nodes. Valid values: 40 to 500.
    "runtime":{
        "name":"docker",
        "version":"19.03.5"
```

`},`

```json
    "worker_instance_types":[
        "ecs.g5.large"
```

`],`

```json
    "num_of_nodes":3,
    "worker_system_disk_category":"cloud_essd",
    "worker_system_disk_size":120,
    "worker_system_disk_performance_level":"PL1",
    "vpcid":"vpc-8vbh3b9a2f38urhlsw9jh",
    "worker_vswitch_ids":[
        "vsw-8vbmoffowsztjaawjtyzo"
```

`],`

```json
    "security_group_id":"sg-8vb7grbyvlb10j0ih46n",
    "is_enterprise_security_group":true,
    "container_cidr":"172.20.0.0/16",
    "service_cidr":"172.21.0.0/20",
    "image_id":"CentOS-xxx",
    "instances": [
        "i-dewgagxdfa****",
        "i-3kjaf9q43l****"
```

`],`

```json
    "format_disk": false,
    "keep_instance_name": true
```

Sample success responses `XML` format

```xml
<cluster_id>cb95aa626a47740afbf6aa099b650****</cluster_id> <task_id>T-5a54309c80282e39ea00002f</task_id> <request_id>687C5BAA-D103-4993-884B-C35E4314A1E1</request_id>
```

`JSON` format `{`

```json
    "cluster_id": "cb95aa626a47740afbf6aa099b650****",
    "task_id": "T-5a54309c80282e39ea00002f",
    "request_id": "687C5BAA-D103-4993-884B-C35E4314A1E1"
```

Error codes You can check further details of error codes. For more information, see Error codes.

#### 3.1.2 ScaleOutCluster

Adds worker nodes to a Container Service cluster. The worker nodes can be deployed in multiple zones. Request syntax

```
POST /api/v2/clusters/ClusterId HTTP/1.1
```

`{`

```json
  "count" : Long,
  "login_password" : "String",
  "vswitch_ids" : [ "String" ],
  "worker_instance_types" : [ "String" ],
  "worker_system_disk_category" : "String",
  "worker_system_disk_size" : Long,
  "worker_data_disks" : [ {
    "category" : "String",
    "size" : Long,
    "encrypted" : "String",
    "auto_snapshot_policy_id" : "String"
  } ],
  "cloud_monitor_flags" : Boolean,
  "cpu_policy" : "String",
  "image_id" : "String",
  "user_data" : "String",
  "rds_instances" : [ "String" ],
  "tags" : [ {
    "key" : "String",
    "value" : "String"
  } ],
  "taints" : [ {
    "key" : "String",
    "value" : "String",
    "effect" : "String"
  } ],
  "runtime" : {
    "name" : "String",
    "version" : "String"
```

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClusterId | String | Yes | c82e6987e2961 451182edacd74 faf**** | The ID of the cluster. |

Request body parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| count | Long | Yes | 3 | The number of worker nodes that you want to add. |

| eveloper Guide·Clu | ster API list |   |   | Container Service for Kubernete |
|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |

| login password _ | String | Yes | Hello@1234 | The Secure Shell (SSH) logon password. The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. |
|---|---|---|---|---|
| vswitch ids _ | Array of String | Yes | vsw- 2ze4jvvvade1yk 899**** | The IDs of the vSwitches that are specified for the nodes that you want to add. Before you scale out a cluster, the cluster uses the vSwitches that are specified when the cluster is created. |
| worker instance _ types _ | Array of String | Yes | ecs.c5.xlarge | The instance types of worker nodes. You must specify at least one instance type. For more information, see the Instance type chapter in Elastic Compute Service (ECS) User Guide. Not e The instance types are listed in descending order of priority. If worker nodes fail to be created based on the instance type of the highest priority, the system attempts to create worker nodes by using the instance type of the next highest priority. |
| worker system _ _ disk category _ | String | Yes | cloud efficiency _ | The type of system disk that is specified for worker nodes. Valid values: cloud efficiency : ultra _ disk. cloud ssd : standard SSD. _ cloud essd : enhanced SSD. _ Default value: cloud ssd . _ |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| worker system _ _ disk size _ | Long | Yes | 120 | The size of the system disk that is specified for worker nodes. Unit: GiB. Valid values: 40 to 500. Default value: 120 . |
| worker data di _ _ sks | Array of data di _ sk | No |   | The configurations of the data disks that are mounted to worker nodes. Each configuration includes disk type and disk size. |
| cloud monitor _ _ flags | Boolean | No | true | Specifies whether to install the CloudMonitor agent. Valid values: true : installs the CloudMonitor agent. false : does not install the CloudMonitor agent. Default value: false . |
| cpu policy _ | String | No | none | The CPU policy. The following policies are supported if the cluster version is 1.12.6 or later. static : This policy allows pods with specific resource characteristics on the node to be granted with enhanced CPU affinity and exclusivity. none : This policy indicates that the default CPU affinity is used. Default value: none . |
| image id _ | String | No | m- bp16z7xko3vvv 8gt**** | Specifies a custom image for nodes. By default, the system image is used. You can select a custom image to replace the default image. |
| user data _ | String | No | IyEvdXNyL2Jpbi9 iYXNoCmVjaG8g IkhlbGxvIEFD**** | The user-defined data. For more information, see the User-defined data chapter in the ECS documentation. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| rds instances _ | Array of String | No | rm- 2zev748xi27xc** ** | The names of the Relational Database Service (RDS) instances. |
| tags | Array of | No |   | The labels to be added to nodes. Labeling rules: Each label consists of a case- sensitive key-value pair. You can add up to 20 labels. When you add a label, you must specify a unique key but you can leave the value empty. A key cannot exceed 64 characters in length and a value cannot exceed 128 characters in length. Keys and values cannot start with aliyun, acs:, https://, or http://. |
| taints | Array of taint | No |   | The taints to be added to nodes. Taints are added to nodes to prevent pods from being scheduled to inappropriate nodes. However, toleration rules allow pods to be scheduled to nodes with matching taints. |
| runtime | runtime | No |   | The container runtime. |

Response syntax

```
HTTP/1.1 200
```

`{`

```json
  "cluster_id" : "String",
  "request_id" : "String",
  "task_id" : "String"
```

Response parameters Response body parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| cluster id _ | String | c82e6987e29614511 82edacd74faf**** | The ID of the cluster. |

| ontainer Service fo | r Kubernetes |   | Developer Guide·Cluster API lis |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| request id _ | String | 687C5BAA-D103- 4993-884B- C35E4314A1E1 | The ID of the request. |
| task id _ | String | T- 5a54309c80282e39e a00002f | The ID of the task. |

Examples Sample requests

```
POST /api/v2/clusters/c82e6987e2961451182edacd74faf**** HTTP/1.1
```

`{`

```json
  "count" : 3,
  "login_password" : "Hello@1234",
  "vswitch_ids" : [ "vsw-2ze4jvvvade1yk899****" ],
  "worker_instance_types" : [ "ecs.c5.xlarge" ],
  "worker_system_disk_category" : "cloud_efficiency",
  "worker_system_disk_size" : 120,
  "worker_data_disks" : [ {
    "category" : "cloud_ssd",
    "size" : 40,
    "encrypted" : "true",
    "auto_snapshot_policy_id" : "sp-2zej1nogjvovnz4z****"
  } ],
  "cloud_monitor_flags" : true,
  "cpu_policy" : "none",
  "image_id" : "m-bp16z7xko3vvv8gt****",
  "user_data" : "IyEvdXNyL2Jpbi9iYXNoCmVjaG8gIkhlbGxvIEFD****",
  "rds_instances" : [ "rm-2zev748xi27xc****" ],
  "tags" : [ {
    "key" : "env",
    "value" : "prod"
  } ],
  "taints" : [ {
    "key" : "key",
    "value" : "value",
    "effect" : "NoSchedule"
  } ],
  "runtime" : {
    "name" : "docker",
    "version" : "19.03.5"
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <cluster_id>c82e6987e2961451182edacd74faf****</cluster_id> <request_id>687C5BAA-D103-4993-884B-C35E4314A1E1</request_id> <task_id>T-5a54309c80282e39ea00002f</task_id>
```

`JSON` format

```
HTTP/1.1 200 OK
```

`{`

```json
  "cluster_id" : "c82e6987e2961451182edacd74faf****",
  "request_id" : "687C5BAA-D103-4993-884B-C35E4314A1E1",
  "task_id" : "T-5a54309c80282e39ea00002f"
```

Error codes You can check further details of error codes. For more information, see Error codes.

#### 3.1.3 DeleteCluster

Deletes a Container Service cluster by ID and releases all nodes in the cluster. Request syntax

```
DELETE /clusters/ClusterId?retain_all_resources=Boolean&keep_slb=Boolean&retain_resources=[ "String"] HTTP/1.1
```

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClusterId | String | Yes | c905d1364c2dd 4b6284a3f4179 0c4**** | The ID of the cluster. |

Request query parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| retain all resou _ _ rces | Boolean | No | false | Specifies whether to retain all resources. If you set the parameter to true , the retain resources parameter is _ ignored. true : retains all resources. false : does not retain all resources. Default value: false . |
| keep slb _ | Boolean | No | false | Specifies whether to retain the Server Load Balancer (SLB) instances that are created for the cluster. true : retains the SLB instances that are created for the cluster. false : does not retain the SLB instances that are created for the cluster. Default value: false . |
| retain resources _ | Array of String | No | sg- 2ze6ess9kho6f dn9**** | The names of the resources that you want to retain. |

Response syntax

```
HTTP/1.1 200 OK
```

Response parameters No response parameters. Examples Sample requests

```
DELETE /clusters/c905d1364c2dd4b6284a3f41790c4****?retain_all_resources=false&keep_slb=fals e&retain_resources=["sg-2ze6ess9kho6fdn9****"] HTTP/1.1 Host:cs.aliyuncs.com
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK
```

Error codes You can check further details of error codes. For more information, see Error codes.

#### 3.1.4 DescribeClusterUserKubeconfig

Obtains the kubeconfig file of a specified Container Service cluster. The kubeconfig file contains detailed information about the current user and is used to configure access to the cluster. Request syntax

```
GET /k8s/ClusterId/user_config?PrivateIpAddress=Boolean&TemporaryDurationMinutes=Long HTTP/
```

### 1.1 ASAPI Developer Guide

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClusterId | String | Yes | c5b5e80b0b64a 4bf6939d2d8fb bc5**** | The ID of the cluster. |

Request query parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PrivateIpAddres s | Boolean | No | true | Specifies whether to obtain the credential that is used to connect to the cluster over the internal network. Valid values: true : obtains the credential that is used to connect to the cluster over the internal network. false : obtains the credential that is used to connect to the cluster over the Internet. Default value: false . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TemporaryDurat ionMinutes | Long | No | 15 | The validity period of a temporary kubeconfig file. Unit: minutes. Valid values: 15 to 4320. Not e If you specify this parameter, the returned kubeconfig file will expire at the time specified by expirat ion . If you do not specify this parameter, the returned kubeconfig file is permanently valid. |

| expirat |   |
|---|---|

Response syntax

```
HTTP/1.1 200 OK
```

`{`

```json
  "config" : "String",
  "expiration" : "String"
```

Response parameters Response body parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| config | String | apiVersion: v1**** | The content of the kubeconfig file. |
| expiration | String | 2024-03- 10T09:56:17Z | The expiration time of the kubeconfig file. The value is in the RFC3339 format and is displayed in UTC. |

Examples Sample requests

```
GET /k8s/c5b5e80b0b64a4bf6939d2d8fbbc5****/user_config?PrivateIpAddress=true&TemporaryDurat ionMinutes=15 HTTP/1.1 Host:cs.aliyuncs.com
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <config> apiVersion: v1 clusters:
- cluster:
... </config> <expiration>2021-03-25T10:01:20Z</expiration>
```

`JSON` format

```
HTTP/1.1 200 OK
```

`{`

```json
  "config" : "\napiVersion: v1\nclusters:\n- cluster:\n...\n",
  "expiration" : "2021-03-25T10:01:20Z"
```

Error codes You can check further details of error codes. For more information, see Error codes.

#### 3.1.5 Query

##### 3.1.5.1 DescribeClustersV1

Queries the details of a specified Container Service cluster. Request syntax

```
GET /api/v1/clusters?name=String&cluster_type=String&page_size=Long&page_number=Long HTTP/1
```

`.1` Request parameters Request query parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| name | String | No | cluster-demo | The name of the cluster. The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). It cannot start with a hyphen. |
| cluster type _ | String | No | Kubernetes | The type of cluster. Valid values: Kubernetes : dedicated Kubernetes cluster. ManagedKubernetes : managed edge Kubernetes cluster. |
| page size _ | Long | No | 10 | The number of entries to return on each page. |
| page number _ | Long | No | 3 | The number of pages to return. |

Response syntax

```
HTTP/1.1 200
```

`{`

```json
  "clusters" : [ {
    "cluster_id" : "String",
    "cluster_type" : "String",
    "created" : "String",
    "init_version" : "String",
    "current_version" : "String",
    "next_version" : "String",
    "deletion_protection" : Boolean,
    "docker_version" : "String",
    "external_loadbalancer_id" : "String",
    "master_url" : "String",
    "meta_data" : "String",
    "name" : "String",
    "network_mode" : "String",
    "private_zone" : Boolean,
    "profile" : "String",
    "region_id" : "String",
    "resource_group_id" : "String",
    "security_group_id" : "String",
    "size" : Long,
    "state" : "String",
    "subnet_cidr" : "String",
    "tags" : [ {
      "key" : "String",
      "value" : "String"
    } ],
    "updated" : "String",
    "vpc_id" : "String",
    "vswitch_id" : "String",
    "worker_ram_role_name" : "String",
    "zone_id" : "String",
  } ],
  "page_info" : {
    "page_number" : Integer,
    "page_size" : Integer,
    "total_count" : Integer
```

Response parameters Response body parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| clusters | Array |   | The list of the details of the queried cluster. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| cluster id _ | String | c3fb96524f9274b44 95df0f12a6b5**** | The ID of the queried cluster. |
| cluster type _ | String | Kubernetes | The type of cluster. Valid values: Kubernetes : dedicated Kubernetes cluster. ManagedKubernetes : managed edge Kubernetes cluster. |
| created | String | 2020-08- 20T10:51:29+08:00 | The time when the cluster was created. |
| init version _ | String | 1.16.9-aliyun.1 | The version of the cluster. The cluster versions provided by Container Service are consistent with the open source versions. We recommend that you select the latest version. If you do not specify this parameter, the latest version is used. You can create clusters of the latest two Kubernetes versions in the Container Service console. You can create clusters of earlier versions by calling API operations. |
| current version _ | String | 1.16.9-aliyun.1 | The Kubernetes version of the cluster. |
| next version _ | String | 1.18.8-aliyun.1 | The Kubernetes version to which the cluster can be upgraded. |
| deletion prote _ ction | Boolean | true | Indicates whether deletion protection is enabled for the cluster. After deletion protection is enabled, the cluster cannot be deleted in the console or by calling API operations. Valid values: true : Deletion protection is enabled for the cluster. This way, the cluster cannot be deleted in the console or by calling API operations. false : Deletion protection is disabled for the cluster. You can delete the cluster in the console or by calling the API. |
| docker version _ | String | 19.03.5 | The Docker version that is used by the cluster. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| external loadb _ alancer id _ | String | lb- 2vcrbmlevo6kjpgch* *** | The ID of the Server Load Balancer (SLB) instance that is used for the Ingress of the cluster. The default SLB specification is slb.s1.small, which belongs to the high-performance instance type. |
| master url _ | String | {\"api server endpoi _ _ nt\":\"\",\"intranet _ api server endpoint _ _ \":\"https://192.16 8.0.251:6443\"} | The address of the cluster API server. It includes an internal endpoint and a public endpoint. |
| meta data _ | String | {\"Addons\": [{\"config\":***} | The metadata of the cluster. |
| name | String | cluster-demo | The name of the cluster. The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). It cannot start with a hyphen (-). |
| network mode _ | String | vpc | The network mode of the cluster. Valid values: classic : classic network. vpc : virtual private cloud (VPC). overlay : overlay network. calico : network powered by Calico. |
| private zone _ | Boolean | false | Indicates whether Alibaba Cloud DNS PrivateZone is enabled. Valid values: true : indicates that Alibaba Cloud DNS PrivateZone is enabled. false : indicates that Alibaba Cloud DNS PrivateZone is disabled. |
| profile | String | Default | The identifier of the cluster. Valid values: Edge : indicates that the cluster is a managed edge Kubernetes cluster. Default : indicates that the cluster is not a managed edge Kubernetes cluster. |
| region id _ | String | cn-beijing | The ID of the region where the cluster is deployed. |

| ontainer Service fo | r Kubernetes |   | Developer Guide·Cluster API lis |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| resource group _ id _ | String | rg- acfmyvw3wjm**** | The ID of the resource group to which the cluster belongs. |
| security group _ _ id | String | sg- 2vcgwsrwgt5mp0yi* *** | The ID of the security group to which the instances of the cluster belong. |
| size | Long | 5 | The number of nodes in the cluster. Master nodes and worker nodes are included. |
| state | String | running | The state of the cluster. Valid values: initial : The cluster is being created. failed : The cluster failed to be created. running : The cluster is running. updating : The cluster is being upgraded. updating failed : The cluster failed _ to be upgraded. scaling : The cluster is being scaled. stopped : The cluster is stopped. deleting : The cluster is being deleted. deleted : The cluster is deleted. delete failed : The cluster failed to _ be deleted. |
| subnet cidr _ | String | 172.21.0.0/16 | The pod CIDR block. It must be a valid and private CIDR block, and must be one of the following CIDR blocks or their subnets: 10.0.0.0/8 172.16-31.0.0/12-16 192.168.0.0/16 The CIDR block of pods cannot overlap with the CIDR block of the VPC in which the cluster is deployed and the CIDR blocks of existing clusters in the VPC. You cannot modify the pod CIDR block after the cluster is created. |
| tags | Array of tag |   | The labels of the cluster. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| updated | String | 2020-09- 16T11:09:55+08:00 | The time when the cluster was updated. |
| vpc id _ | String | vpc- 2vcg932hsxsxuqbgl* *** | The ID of the VPC where the cluster is deployed. This parameter is required when you create a cluster. |
| vswitch id _ | String | vsw- 2vc41xuumx5z2rdm a****,vsw- 2vc41xuumx5z2rdm a**** | The IDs of the vSwitches. You can select one to three vSwitches when you create a cluster. We recommend that you select vSwitches in different zones to ensure high availability. |
| worker ram rol _ _ e name _ | String | KubernetesWorkerR ole-ec87d15b-edca- 4302-933f- c8a16bf0**** | The name of the Resource Access Management (RAM) role. The RAM role is assigned to the worker nodes that are created on Elastic Compute Service (ECS) instances. |
| zone id _ | String | cn-beijing-b | The ID of the zone where the cluster is deployed. |
| page info _ | object |   | The pagination details. |
| page number _ | Integer | 3 | The page number of the returned page. |
| page size _ | Integer | 20 | The number of entries returned per page. |
| total count _ | Integer | 50 | The total number of entries returned. |

Examples Sample requests

```
GET /api/v1/clusters?name=cluster-demo&cluster_type=Kubernetes&page_size=10&page_number=3 H TTP/1.1
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <clusters>
    <cluster_id>c3fb96524f9274b4495df0f12a6b5****</cluster_id>
    <cluster_type>Kubernetes</cluster_type>
    <created>2020-08-20T10:51:29+08:00</created>
    <init_version>1.16.9-aliyun.1</init_version>
    <current_version>1.16.9-aliyun.1</current_version>
    <next_version>1.18.8-aliyun.1</next_version>
    <deletion_protection>true</deletion_protection>
    <docker_version>19.03.5</docker_version>
    <external_loadbalancer_id>lb-2vcrbmlevo6kjpgch****</external_loadbalancer_id>
    <master_url>{\"api_server_endpoint\":\"\",\"intranet_api_server_endpoint\":\"https://19
2.168.0.251:6443\"}</master_url>
    <meta_data>{\"Addons\":[{\"config\":***}</meta_data>
    <name>cluster-demo</name>
    <network_mode>vpc</network_mode>
    <private_zone>false</private_zone>
    <profile>Default</profile>
    <region_id>cn-beijing</region_id>
    <resource_group_id>rg-acfmyvw3wjm****</resource_group_id>
    <security_group_id>sg-2vcgwsrwgt5mp0yi****</security_group_id>
    <size>5</size>
    <state>running</state>
    <subnet_cidr>172.21.0.0/16</subnet_cidr>
    <tags>
        <key>env</key>
        <value>prod</value>
    </tags>
    <updated>2020-09-16T11:09:55+08:00</updated>
    <vpc_id>vpc-2vcg932hsxsxuqbgl****</vpc_id>
    <vswitch_id>vsw-2vc41xuumx5z2rdma****,vsw-2vc41xuumx5z2rdma****</vswitch_id>
    <worker_ram_role_name>KubernetesWorkerRole-ec87d15b-edca-4302-933f-c8a16bf0****</worker
_ram_role_name>
    <zone_id>cn-beijing-b</zone_id>
</clusters> <page_info>
    <page_number>3</page_number>
    <page_size>20</page_size>
    <total_count>50</total_count>
</page_info>
```

`JSON` format

```
HTTP/1.1 200 OK
```

`{`

```json
  "clusters" : [ {
    "cluster_id" : "c3fb96524f9274b4495df0f12a6b5****",
    "cluster_type" : "Kubernetes",
    "created" : "2020-08-20T10:51:29+08:00",
    "init_version" : "1.16.9-aliyun.1",
    "current_version" : "1.16.9-aliyun.1",
    "next_version" : "1.18.8-aliyun.1",
    "deletion_protection" : true,
    "docker_version" : "19.03.5",
    "external_loadbalancer_id" : "lb-2vcrbmlevo6kjpgch****",
    "master_url" : "{\\\"api_server_endpoint\\\":\\\"\\\",\\\"intranet_api_server_endpoint\
\\":\\\"https://192.168.0.251:6443\\\"}",
    "meta_data" : "{\\\"Addons\\\":[{\\\"config\\\":***}",
    "name" : "cluster-demo",
    "network_mode" : "vpc",
    "private_zone" : false,
    "profile" : "Default",
    "region_id" : "cn-beijing",
    "resource_group_id" : "rg-acfmyvw3wjm****",
    "security_group_id" : "sg-2vcgwsrwgt5mp0yi****",
    "size" : 5,
    "state" : "running",
    "subnet_cidr" : "172.21.0.0/16",
    "tags" : [ {
      "key" : "env",
      "value" : "prod"
    } ],
    "updated" : "2020-09-16T11:09:55+08:00",
    "vpc_id" : "vpc-2vcg932hsxsxuqbgl****",
    "vswitch_id" : "vsw-2vc41xuumx5z2rdma****,vsw-2vc41xuumx5z2rdma****",
    "worker_ram_role_name" : "KubernetesWorkerRole-ec87d15b-edca-4302-933f-c8a16bf0****",
    "zone_id" : "cn-beijing-b",
  } ],
  "page_info" : {
    "page_number" : 3,
    "page_size" : 20,
    "total_count" : 50
```

Error codes You can check further details of error codes. For more information, see Error codes.

##### 3.1.5.2 DescribeClusterDetail

Queries the details of a specific Container Service cluster by the cluster ID. Request syntax

```
GET /clusters/ClusterId HTTP/1.1
```

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClusterId | String | Yes | cdde1f21ae22e 483ebcb068a6e b7f**** | The ID of the cluster. |

Response syntax

```
HTTP/1.1 200
```

`{`

```json
  "cluster_id" : "String",
  "cluster_type" : "String",
  "created" : "String",
  "init_version" : "String",
  "current_version" : "String",
  "next_version" : "String",
  "deletion_protection" : Boolean,
  "docker_version" : "String",
  "external_loadbalancer_id" : "String",
  "meta_data" : "String",
  "name" : "String",
  "network_mode" : "String",
  "region_id" : "String",
  "resource_group_id" : "String",
  "security_group_id" : "String",
  "size" : Long,
  "state" : "String",
  "tags" : [ {
    "key" : "String",
    "value" : "String"
  } ],
  "updated" : "String",
  "vpc_id" : "String",
  "vswitch_id" : "String",
  "subnet_cidr" : "String",
  "zone_id" : "String",
  "master_url" : "String",
  "private_zone" : Boolean,
  "profile" : "String",
  "worker_ram_role_name" : "String",
```

Response parameters Response body parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| cluster id _ | String | c82e6987e29614511 82edacd74faf**** | The ID of the cluster. |
| cluster type _ | String | Kubernetes | The type of cluster. Valid values: Kubernetes : dedicated Kubernetes cluster. ManagedKubernetes : managed edge Kubernetes cluster. |
| created | String | 2019-11- 25T15:50:20+08:00 | The time when the cluster was created. |
| init version _ | String | 1.16.6-aliyun.1 | The Kubernetes version that is initially used by the cluster. |
| current version _ | String | 1.16.6-aliyun.1 | The Kubernetes version of the cluster. |
| next version _ | String | 1.18.8-aliyun.1 | The Kubernetes version to which the cluster can be upgraded. |
| deletion prote _ ction | Boolean | true | Indicates whether deletion protection is enabled for the cluster. If deletion protection is enabled, the cluster cannot be deleted in the console or by calling API operations. Valid values: true : Deletion protection is enabled for the cluster. This way, the cluster cannot be deleted in the console or by calling API operations. false : Deletion protection is disabled for the cluster. You can delete the cluster in the console or by calling API operations. |
| docker version _ | String | 19.03.5 | The Docker version that is used by the cluster. |
| external loadb _ alancer id _ | String | lb- 2ze3buguz3gx9920 z**** | The ID of the Server Load Balancer (SLB) instance that is used for the Ingress of the cluster. |
| meta data _ | String | \"Addons\":*** | The metadata of the cluster. |

| C | ontainer Service fo | r Kubernetes |   | Developer Guide·Cluster API lis | t |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| name | String | cluster-demo | The name of the cluster. The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). It cannot start with a hyphen. |
| network mode _ | String | vpc | The network mode of the cluster. Valid values: classic : classic network. vpc : virtual private cloud (VPC). overlay : overlay network. calico : network powered by Calico. Default value: vpc . |
| region id _ | String | cn-beijing | The ID of the region where the cluster is deployed. |
| resource group _ id _ | String | rg- acfmyvw3wjm**** | The ID of the resource group to which the cluster belongs. |
| security group _ _ id | String | sg-25yq**** | The ID of the security group to which the instances of the cluster belong. |
| size | Long | 5 | The number of nodes in the cluster. Master nodes and worker nodes are included. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| state | String | running | The state of the cluster. Valid values: initial : The cluster is being created. failed : The cluster failed to be created. running : The cluster is running. updating : The cluster is being upgraded. updating failed : The cluster failed _ to be upgraded. scaling : The cluster is being scaled. stopped : The cluster is stopped. deleting : The cluster is being deleted. deleted : The cluster is deleted. delete failed : The cluster failed to _ be deleted. |
| tags | Array of tag |   | The labels of the cluster. |
| updated | String | 2020-01- 13T23:01:03+08:00 | The time when the cluster was updated. |
| vpc id _ | String | vpc- 2zecuu62b9zw7a7q n**** | The ID of the VPC where the cluster is deployed. This parameter is required when you create a cluster. |
| vswitch id _ | String | vsw- 2zete8s4qocqg0mf 6****,vsw- 2zete8s4qocqg0mf 6**** | The IDs of vSwitches. You can select one to three vSwitches when you create a cluster. We recommend that you select vSwitches in different zones to ensure high availability. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| subnet cidr _ | String | 172.20.0.0/16 | The pod CIDR block. It must be a valid and private CIDR block, and must be one of the following CIDR blocks or their subnets: 10.0.0.0/8 172.16-31.0.0/12-16 192.168.0.0/16 The pod CIDR block cannot overlap with the CIDR block of the VPC or the CIDR blocks of the clusters in the VPC. |
| zone id _ | String | cn-beijing-a | The ID of the zone where the cluster is deployed. |
| master url _ | String | {\"intranet api serv _ _ er endpoint\":\"htt _ ps://192.168.0.251: 6443\"***} | The address of the cluster. It includes an internal endpoint and a public endpoint. |
| private zone _ | Boolean | false | Indicates whether Alibaba Cloud DNS PrivateZone is enabled. true : indicates that Alibaba Cloud DNS PrivateZone is enabled. false : indicates that Alibaba Cloud DNS PrivateZone is disabled. |
| profile | String | Default | Indicates the scenario in which the cluster is used. Valid values: Default : indicates that the cluster is used in non-edge computing scenarios. Edge : indicates that the cluster is used in edge computing scenarios. |
| worker ram rol _ _ e name _ | String | KubernetesWorkerR ole-ec87d15b-edca- 4302-933f- c8a16bf0**** | The name of the Resource Access Management (RAM) role. The RAM role is assigned to the worker nodes that are created on Elastic Compute Service (ECS) instances. |

Examples Sample requests

```
GET /clusters/cdde1f21ae22e483ebcb068a6eb7f**** HTTP/1.1
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <cluster_id>c82e6987e2961451182edacd74faf****</cluster_id> <cluster_type>Kubernetes</cluster_type> <created>2019-11-25T15:50:20+08:00</created> <init_version>1.16.6-aliyun.1</init_version> <current_version>1.16.6-aliyun.1</current_version> <next_version>1.18.8-aliyun.1</next_version> <deletion_protection>true</deletion_protection> <docker_version>19.03.5</docker_version> <external_loadbalancer_id>lb-2ze3buguz3gx9920z****</external_loadbalancer_id> <meta_data>\"Addons\":***</meta_data> <name>cluster-demo</name> <network_mode>vpc</network_mode> <region_id>cn-beijing</region_id> <resource_group_id>rg-acfmyvw3wjm****</resource_group_id> <security_group_id>sg-25yq****</security_group_id> <size>5</size> <state>running</state> <tags>
    <key>env</key>
    <value>prod</value>
</tags> <updated>2020-01-13T23:01:03+08:00</updated> <vpc_id>vpc-2zecuu62b9zw7a7qn****</vpc_id> <vswitch_id>vsw-2zete8s4qocqg0mf6****,vsw-2zete8s4qocqg0mf6****</vswitch_id> <subnet_cidr>172.20.0.0/16</subnet_cidr> <zone_id>cn-beijing-a</zone_id> <master_url>{\"intranet_api_server_endpoint\":\"https://192.168.0.251:6443\"***}</master_ur
```

`l>`

```xml
<private_zone>false</private_zone> <profile>Default</profile> <worker_ram_role_name>KubernetesWorkerRole-ec87d15b-edca-4302-933f-c8a16bf0****</worker_ram _role_name>
```

`JSON` format

```
HTTP/1.1 200 OK
```

`{`

```json
  "cluster_id" : "c82e6987e2961451182edacd74faf****",
  "cluster_type" : "Kubernetes",
  "created" : "2019-11-25T15:50:20+08:00",
  "init_version" : "1.16.6-aliyun.1",
  "current_version" : "1.16.6-aliyun.1",
  "next_version" : "1.18.8-aliyun.1",
  "deletion_protection" : true,
  "docker_version" : "19.03.5",
  "external_loadbalancer_id" : "lb-2ze3buguz3gx9920z****",
  "meta_data" : "\\\"Addons\\\":***",
  "name" : "cluster-demo",
  "network_mode" : "vpc",
  "region_id" : "cn-beijing",
  "resource_group_id" : "rg-acfmyvw3wjm****",
  "security_group_id" : "sg-25yq****",
  "size" : 5,
  "state" : "running",
  "tags" : [ {
    "key" : "env",
    "value" : "prod"
  } ],
  "updated" : "2020-01-13T23:01:03+08:00",
  "vpc_id" : "vpc-2zecuu62b9zw7a7qn****",
  "vswitch_id" : "vsw-2zete8s4qocqg0mf6****,vsw-2zete8s4qocqg0mf6****",
  "subnet_cidr" : "172.20.0.0/16",
  "zone_id" : "cn-beijing-a",
  "master_url" : "{\\\"intranet_api_server_endpoint\\\":\\\"https://192.168.0.251:6443\\\"*
**}",
  "private_zone" : false,
  "profile" : "Default",
  "worker_ram_role_name" : "KubernetesWorkerRole-ec87d15b-edca-4302-933f-c8a16bf0****",
```

Error codes You can check further details of error codes. For more information, see Error codes.

##### 3.1.5.3 DescribeClusterResources

Queries all resources in a specified Container Service cluster. Request syntax

```
GET /clusters/ClusterId/resources HTTP/1.1
```

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClusterId | String | Yes | cb95aa626a477 40afbf6aa099b 65**** | The ID of the cluster. |

Response syntax

```json
HTTP/1.1 200 [ {
  "cluster_id" : "String",
  "created" : "String",
  "instance_id" : "String",
  "resource_info" : "String",
  "resource_type" : "String",
  "state" : "String"
} ]
```

Response parameters Response body parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
|   | Array |   | The list of resources in the cluster. |
| cluster id _ | String | cb95aa626a47740af bf6aa099b65**** | The ID of the cluster. |
| created | String | 2020-09- 11T10:11:54+08:00 | The time when the resource was created. |
| instance id _ | String | lb- wz9poz4r0ymh8u0u f**** | The ID of the resource. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| resource info _ | String | {\"Id\":\"k8s master _ slb\",\"Name\":\"k _ 8s master slb\",\"T _ _ ype\":\"ALIYUN::SL B::LoadBalancer\",\ "Status\":\"CREATE _ COMPLETE\",\"Statu sReason\":\"state changed\",\"Update d\":\"2020-05- 21T13:25:02\",\"Ph ysicalId\":\"lb- wz9poz4r0ymh8u0u f****\"} | The information about the resource. |
| resource type _ | String | ALIYUN::SLB::LoadB alancer | The type of resource. |
| state | String | CREATE COMPLETE _ | The state of the resource. Valid values: CREATE COMPLETE : The resource is _ created. CREATE FAILED : The resource failed _ to be created. CREATE IN PROGRESS : The resource is _ _ being created. DELETE FAILED : The resource failed _ to be deleted. DELETE IN PROGRESS : The resource is _ _ being deleted. ROLLBACK COMPLETE : The resource is _ rolled back. ROLLBACK FAILED : The resource failed _ to be rolled back. ROLLBACK IN PROGRESS : The resource _ _ is being rolled back. |

Examples Sample requests

```
GET /clusters/cb95aa626a47740afbf6aa099b65****/resources HTTP/1.1
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <0>
    <cluster_id>cb95aa626a47740afbf6aa099b65****</cluster_id>
    <created>2020-09-11T10:11:54+08:00</created>
    <instance_id>lb-wz9poz4r0ymh8u0uf****</instance_id>
    <resource_info>{\"Id\":\"k8s_master_slb\",\"Name\":\"k8s_master_slb\",\"Type\":\"ALIYUN
::SLB::LoadBalancer\",\"Status\":\"CREATE_COMPLETE\",\"StatusReason\":\"state changed\",\"U pdated\":\"2020-05-21T13:25:02\",\"PhysicalId\":\"lb-wz9poz4r0ymh8u0uf****\"}</resource_inf
```

`o>`

```xml
    <resource_type>ALIYUN::SLB::LoadBalancer</resource_type>
    <state>CREATE_COMPLETE</state>
</0>
```

`JSON` format

```json
HTTP/1.1 200 OK [ {
  "cluster_id" : "cb95aa626a47740afbf6aa099b65****",
  "created" : "2020-09-11T10:11:54+08:00",
  "instance_id" : "lb-wz9poz4r0ymh8u0uf****",
  "resource_info" : "{\\\"Id\\\":\\\"k8s_master_slb\\\",\\\"Name\\\":\\\"k8s_master_slb\\\"
,\\\"Type\\\":\\\"ALIYUN::SLB::LoadBalancer\\\",\\\"Status\\\":\\\"CREATE_COMPLETE\\\",\\\" StatusReason\\\":\\\"state changed\\\",\\\"Updated\\\":\\\"2020-05-21T13:25:02\\\",\\\"Phys icalId\\\":\\\"lb-wz9poz4r0ymh8u0uf****\\\"}",
  "resource_type" : "ALIYUN::SLB::LoadBalancer",
  "state" : "CREATE_COMPLETE"
} ]
```

Error codes You can check further details of error codes. For more information, see Error codes.

##### 3.1.5.4 DescribeClusterNamespaces

Queries the namespaces of a specified cluster. Request syntax

```
GET /k8s/ClusterId/namespaces HTTP/1.1
```

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClusterId | String | Yes | c68069cade53b 4558924a924b4 15f**** | The ID of the cluster. |

Response syntax

```json
HTTP/1.1 200 OK [ "String" ]
```

Response parameters Response body parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
|   | Array of String | kube-system | The names of the namespaces. |

Examples

```
GET /k8s/c68069cade53b4558924a924b415f****/namespaces HTTP/1.1 Host:cs.aliyuncs.com
```

Sample success responses `XML` format

```
HTTP/1.1 200 OK Content-Type:application/xml <0>kube-system</0>
```

`JSON` format

```json
HTTP/1.1 200 OK [ "kube-system" ]
```

Error codes You can check further details of error codes. For more information, see Error codes.

##### 3.1.5.5 DescribeExternalAgent

Obtains the agent configurations of an external cluster that is registered in the Container Service console. You can deploy the agent configurations in an external cluster. This allows you to access the API server of the cluster. Request syntax

```
GET /k8s/ClusterId/external/agent/deployment?PrivateIpAddress=String HTTP/1.1
```

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClusterId | String | Yes | c106f377e16f34 eb1808d6b9362 c9**** | The ID of the cluster. |

Request query parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PrivateIpAddres s | String | No | true | Specifies whether to obtain the credential that is used to access the internal network. true : obtains the credential that is used to access the internal network. false : obtains the credential that is used to access the Internet. Default value: false . |

Response syntax

```
HTTP/1.1 200
```

`{`

```json
  "config" : "String"
```

Response parameters Response body parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| config | String | apiVersion: v1**** | The agent configurations in the YAML format. |

Examples Sample requests

```
GET /k8s/c106f377e16f34eb1808d6b9362c9****/external/agent/deployment?PrivateIpAddress=true HTTP/1.1
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <config>apiVersion: v1****</config>
```

`JSON` format

```
HTTP/1.1 200 OK
```

`{`

```json
  "config" : "apiVersion: v1****"
```

##### 3.1.5.6 DescribeUserQuota

Queries resource quotas. Request parameter types This operation uses only common request parameters. For more information, see the Common request parameters topic. Request structure

```
 http://provision.cs.aliyun-inc.com http
```

Request parameters Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| cluster quota _ | Long | "20" | The quota of dedicated Kubernetes clusters. Default value: 20. To increase the quota, submit a ticket. |
| ask cluster qu _ _ ota | Long | 3 | The quota of serverless Kubernetes (ASK) clusters. |

| Developer Guide·Cl | uster API list |   | Container Service for Kubernete |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| cluster nodepo _ ol quota _ | Long | "10" | The quota of node pools in an ACK cluster. |
| cluster quota _ | Long | "50" | The quota of ACK clusters for all types. |
| node quota _ | Long | "100" | The quota of nodes in an ACK cluster. |

Examples Sample requests

```
GET /quota HTTP/1.1 Common request parameters
```

Sample success responses `XML` format

```xml
<amk_cluster_quota>20</amk_cluster_quota> <cluster_nodepool_quota>10</cluster_nodepool_quota> <cluster_quota>50</cluster_quota> <node_quota>100</node_quota> <ask_cluster_quota>3</ask_cluster_quota>
```

`JSON` format `{`

```json
    "amk_cluster_quota": "20",
    "cluster_nodepool_quota": "10",
    "cluster_quota": "50",
    "node_quota": "100",
    "ask_cluster_quota": "3"
```

Error codes You can check further details of error codes. For a list of error codes, visit the Error codes.

##### 3.1.5.7 DescribeClusterLogs

Queries the logs of a specified Container Service cluster. Request syntax

```
GET /clusters/ClusterId/logs HTTP/1.1
```

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClusterId | String | Yes | c106f377e16f34 eb1808d6b9362 c9**** | The ID of the cluster. |

Response syntax

```json
HTTP/1.1 200 [ {
  "ID" : Long,
  "cluster_id" : "String",
  "cluster_log" : "String",
  "log_level" : "String",
  "created" : "String",
  "updated" : "String"
} ]
```

Response parameters Response body parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
|   | Array |   | The list of the returned logs. |
| ID | Long | 590749245 | The ID of the log. |
| cluster id _ | String | c23421cfa74454bc8 b37163fd19af*** | The ID of the cluster. |
| cluster log _ | String | start to update cluster status to CREATE COMPLETE _ | The content of the log. |
| log level _ | String | 0004 | The level of the log. |
| created | String | 2020-09- 11T10:11:51+08:00 | The time when the log was generated. |
| updated | String | 2020-09- 11T10:11:51+08:00 | The time when the log was updated. |

Examples Sample requests

```
GET /clusters/c106f377e16f34eb1808d6b9362c9****/logs HTTP/1.1
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <0>
    <ID>590749245</ID>
    <cluster_id>c23421cfa74454bc8b37163fd19af***</cluster_id>
    <cluster_log>start to update cluster status to CREATE_COMPLETE</cluster_log>
    <log_level>0004</log_level>
    <created>2020-09-11T10:11:51+08:00</created>
    <updated>2020-09-11T10:11:51+08:00</updated>
</0>
```

`JSON` format

```json
HTTP/1.1 200 OK [ {
  "ID" : 590749245,
  "cluster_id" : "c23421cfa74454bc8b37163fd19af***",
  "cluster_log" : "start to update cluster status to CREATE_COMPLETE",
  "log_level" : "0004",
  "created" : "2020-09-11T10:11:51+08:00",
  "updated" : "2020-09-11T10:11:51+08:00"
} ]
```

Error codes You can check further details of error codes. For more information, see Error codes.

##### 3.1.5.8 DescribeKubernetesVersionMetadata

Queries the details of a Container Service for Kubernetes (ACK) cluster version. Request parameter types This operation uses only common request parameters. For more information, see the Common request parameters topic. Request structure

```
get /api/v1/metadata/versions http|https
```

Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Region | String | Yes | cn-beijing | The ID of the region where the ACK cluster is deployed. |
| MultiAZ | Boolean | No | false | Specifies whether to query a multi- zone ACK cluster. |
| ClusterType | String | Yes | Kubernetest | The type of ACK cluster. Valid values: |
| KubernetesVersio n | String | No | 1.16.9-aliyun.1 | The version of the ACK cluster, such as 1.16.9-aliyun.1. |
| Profile | String | No | Default | The identifier of an edge cluster. Default: The ACK cluster is not an edge cluster. Edge: The ACK cluster is an edge cluster. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
|   | Array of data |   | The returned data. |
| capabilities | Object | N/A | The features of the ACK cluster version. |
| images | Array |   | The system images of the Elastic Compute Service (ECS) instances. |
| image id _ | String | "centos 7 7 x64 20 _ _ _ _ G alibase 20200426 _ _ .vhd" | The ID of the snapshot. |
| image name _ | String | "CentOS 7.7" | The name of the image. |
| image type _ | String | "centos 7 7 2" _ _ _ | The type of image. |
| os type _ | String | "Linux" | The type of operating system. Valid values: Windows and Linux. Default value: Linux. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| os version _ | String | "7.7" | The version number of the operating system. |
| platform | String | "CentOS" | The release version of the operating system. Valid values: CentOS, AliyunLinux, Windows, and WindowsCore. |
| meta data _ | Object | N/A | The metadata of the ACK cluster version. |
| multi az _ | String | "false" | Indicates whether the ACK cluster is a multi- zone cluster. |
| runtimes | Array |   | The configuration of the container runtime. |
| name | String | "docker" | The name of the container runtime. |
| version | String | "19.05.3" | The version of the container runtime. |
| version | String | "1.16.9-aliyun.1" | The version of the ACK cluster. |

Examples Sample requests

```
GET /api/v1/metadata/versions HTTP/1.1
```

`{`

```json
    "Region":"cn-beijing",
    "ClusterType":"Kubernetes",
    "MultiAZ":false,
    "KubernetestVersion":"1.16.9-aliyun.1"
```

Sample success responses `XML` format

```xml
<0>
    <version>1.14.8-aliyun.1</version>
    <multi_az>false</multi_az>
    <capabilities>
        <VpcCidr>192.168.0.0/16</VpcCidr>
        <ZoneId/>
    </capabilities>
    <meta_data>
        <KubernetesVersion>1.14.8-aliyun.1</KubernetesVersion>
    </meta_data>
    <runtimes>
        <name>docker</name>
        <version>19.03.5</version>
    </runtimes>
    <images>
        <image_id>centos_7_7_x64_20G_alibase_20200426.vhd</image_id>
        <image_name>CentOS 7.7</image_name>
        <image_type>centos_7_7_20</image_type>
        <image_category>system</image_category>
        <platform>CentOS</platform>
        <os_type>Linux</os_type>
        <os_version>7.7</os_version>
    </images>
</0>
```

`JSON` format `[` `{`

```json
        "version":"1.14.8-aliyun.1",
        "multi_az":false,
        "capabilities":{
            "VpcCidr":"192.168.0.0/16",
            "ZoneId":""
```

`},`

```json
        "meta_data":{
            "KubernetesVersion":"1.14.8-aliyun.1"
```

`},`

```json
        "runtimes":[
```

`{`

```json
                "name":"docker",
                "version":"19.03.5"
```

`],`

```json
        "images":[
```

`{`

```json
                "image_id":"centos_7_7_x64_20G_alibase_20200426.vhd",
                "image_name":"CentOS 7.7",
                "image_type":"centos_7_7_20",
                "image_category":"system",
                "platform":"CentOS",
                "os_type":"Linux",
                "os_version":"7.7"
```

`]` `]` Error codes You can check further details of error codes. For a list of error codes, visit the Error codes.

#### 3.1.6 Modify

##### 3.1.6.1 ModifyCluster

Modifies the configurations of a specified Container Service cluster. Request syntax

```
PUT /api/v2/clusters/ClusterId HTTP/1.1
```

`{`

```json
  "api_server_eip" : Boolean,
  "api_server_eip_id" : "String",
  "deletion_protection" : Boolean,
  "instance_deletion_protection" : Boolean,
  "ingress_domain_rebinding" : "String",
  "ingress_loadbalancer_id" : "String",
  "resource_group_id" : "String",
```

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClusterId | String | Yes | cb95aa626a477 40afbf6aa099b 65**** | The ID of the cluster. |

Request body parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| api server eip _ _ | Boolean | No | true | Specifies whether to associate an elastic IP address (EIP) with the cluster API server. This enables Internet access for the cluster. Valid values: true : associates an EIP with the cluster API server. false : does not associate an EIP with the cluster API server. |
| api server eip i _ _ _ d | String | No | eip- wz9fnasl6dsfh mvci**** | The ID of the EIP that you want to associate with the cluster API server. The parameter takes effect only if api server eip is set to _ _ true . |

|   | api server eip _ _ |
|---|---|
| true |   |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| deletion protec _ tion | Boolean | No | true | Specifies whether to enable deletion protection for the cluster. After deletion protection is enabled, the cluster cannot be deleted in the console or by calling API operations. Valid values: true : enables deletion protection for the cluster. This way, the cluster cannot be deleted in the console or by calling API operations. false : disables deletion protection for the cluster. This way, the cluster can be deleted in the console or by calling API operations. Default value: false . |
| instance deletio _ n protection _ | Boolean | No | true | Specifies whether to enable deletion protection for the nodes in the cluster. If deletion protection is enabled, the nodes in the cluster cannot be deleted in the console or by calling API operations. Valid values: true : The nodes in the cluster cannot be deleted in the console or by calling API operations. false : The nodes in the cluster can be deleted in the console or by calling API operations. Default value: false . |
| ingress domain _ rebinding _ | String | No | true | Specifies whether to remap the test domain name of the cluster. Valid values: true : remaps the test domain name of the cluster. false : does not remap the test domain name of the cluster. Default value: false . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ingress loadbal _ ancer id _ | String | No | lb- wz97kes8tnndk podw**** | The ID of the Server Load Balancer (SLB) instance that is associated with the cluster. |
| resource group _ id _ | String | No | rg- acfmyvw3wjm** ** | The ID of the resource group to which the cluster belongs. |

Response syntax

```
HTTP/1.1 200
```

`{`

```json
  "cluster_id" : "String",
  "request_id" : "String",
  "task_id" : "String"
```

Response parameters Response body parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| cluster id _ | String | cb95aa626a47740af bf6aa09**** | The ID of the cluster. |
| request id _ | String | 687C5BAA-D103- 4993-884B- C35E4314**** | The ID of the request. |
| task id _ | String | T- 5a54309c80282e39e a00**** | The ID of the task. |

Examples Sample requests

```
PUT /api/v2/clusters/cb95aa626a47740afbf6aa099b65**** HTTP/1.1
```

`{`

```json
  "api_server_eip" : true,
  "api_server_eip_id" : "eip-wz9fnasl6dsfhmvci****",
  "deletion_protection" : true,
  "instance_deletion_protection" : true,
  "ingress_domain_rebinding" : "true",
  "ingress_loadbalancer_id" : "lb-wz97kes8tnndkpodw****",
  "resource_group_id" : "rg-acfmyvw3wjm****",
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <cluster_id>cb95aa626a47740afbf6aa09****</cluster_id> <request_id>687C5BAA-D103-4993-884B-C35E4314****</request_id> <task_id>T-5a54309c80282e39ea00****</task_id>
```

`JSON` format

```
HTTP/1.1 200 OK
```

`{`

```json
  "cluster_id" : "cb95aa626a47740afbf6aa09****",
  "request_id" : "687C5BAA-D103-4993-884B-C35E4314****",
  "task_id" : "T-5a54309c80282e39ea00****"
```

Error codes You can check further details of error codes. For more information, see Error codes.

##### 3.1.6.2 ModifyClusterTags

Modifies the labels of a specified Container Service cluster. Request syntax

```json
POST /clusters/ClusterId/tags HTTP/1.1 [ {
  "key" : "String",
  "value" : "String"
} ]
```

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClusterId | String | Yes | c106f377e16f34 eb1808d6b9362 c9**** | The ID of the cluster. |

Request body parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
|   | Array of tag | No |   | The data of the labels that you want to modify. |

Response syntax

```
HTTP/1.1 200 OK
```

Response parameters No response parameters. Examples Sample requests

```json
POST /clusters/c106f377e16f34eb1808d6b9362c9****/tags HTTP/1.1 [ {
  "key" : "env",
  "value" : "prod"
} ]
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK
```

Error codes You can check further details of error codes. For more information, see Error codes.

#### 3.1.7 Upgrade

##### 3.1.7.1 UpgradeCluster

Upgrades a specified Container Service cluster. Request syntax

```
POST /api/v2/clusters/ClusterId/upgrade HTTP/1.1
```

`{`

```json
  "component_name" : "String",
  "next_version" : "String",
  "version" : "String"
```

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClusterId | String | Yes | c82e6987e2961 451182edacd74 faf**** | The ID of the cluster. |

Request body parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| component na _ me | String | No | k8s | The name of the component. Set the value to k8s . |
| next version _ | String | No | 1.16.9-aliyun.1 | The Kubernetes version to which the cluster can be upgraded. |
| version | String | No | 1.14.8-aliyun.1 | The Kubernetes version of the cluster. |

Response syntax

```
HTTP/1.1 200 OK
```

Response parameters No response parameters. Examples Sample requests

```
POST /api/v2/clusters/c82e6987e2961451182edacd74faf****/upgrade HTTP/1.1
```

`{`

```json
  "component_name" : "k8s",
  "next_version" : "1.16.9-aliyun.1",
  "version" : "1.14.8-aliyun.1"
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK
```

Error codes You can check further details of error codes. For more information, see Error codes.

##### 3.1.7.2 GetUpgradeStatus

Queries the upgrade status of a specified Container Service cluster. Request syntax

```
GET /api/v2/clusters/ClusterId/upgrade/status HTTP/1.1
```

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClusterId | String | Yes | c106f377e16f34 eb1808d6b9362 c9**** | The ID of the cluster. |

Response syntax

```
HTTP/1.1 200
```

`{`

```json
  "error_message" : "String",
  "precheck_report_id" : "String",
  "status" : "String",
  "upgrade_step" : "String",
  "upgrade_task" : {
    "status" : "String",
    "message" : "String"
```

Response parameters Response body parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| error message _ | String | subject to actual return | The error message returned during the upgrade. |
| precheck repor _ t id _ | String | be4c8eb72de94d45 9ea7ace7c811d119 | The ID of the precheck report. |
| status | String | running | The state of the upgrade. |
| upgrade step _ | String | prechecking | The current phase of the upgrade. |
| upgrade task _ | object |   | The details of the upgrade task. |
| status | String | running | The state of the upgrade task. |
| message | String | subject to actual return | The description of the upgrade task. |

Examples Sample requests

```
GET /api/v2/clusters/c106f377e16f34eb1808d6b9362c9****/upgrade/status HTTP/1.1
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <error_message>subject to actual return</error_message> <precheck_report_id>be4c8eb72de94d459ea7ace7c811d119</precheck_report_id> <status>running</status> <upgrade_step>prechecking</upgrade_step> <upgrade_task>
    <status>running</status>
    <message>subject to actual return</message>
</upgrade_task>
```

`JSON` format

```
HTTP/1.1 200 OK
```

`{`

```json
  "error_message" : "subject to actual return",
  "precheck_report_id" : "be4c8eb72de94d459ea7ace7c811d119",
  "status" : "running",
  "upgrade_step" : "prechecking",
  "upgrade_task" : {
    "status" : "running",
    "message" : "subject to actual return"
```

Error codes You can check further details of error codes. For more information, see Error codes.

##### 3.1.7.3 PauseClusterUpgrade

Suspends the upgrade of a specified Container Service cluster. Request syntax

```
POST /api/v2/clusters/ClusterId/upgrade/pause HTTP/1.1
```

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClusterId | String | Yes | c82e6987e2961 451182edacd74 faf**** | The ID of the cluster. |

Response syntax

```
HTTP/1.1 200 OK
```

Response parameters No response parameters. Examples Sample requests

```
POST /api/v2/clusters/c82e6987e2961451182edacd74faf****/upgrade/pause HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK
```

Error codes You can check further details of error codes. For more information, see Error codes.

##### 3.1.7.4 CancelClusterUpgrade

Cancels the upgrade of a specified Container Service cluster. Request syntax

```
POST /api/v2/clusters/ClusterId/upgrade/cancel HTTP/1.1
```

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClusterId | String | Yes | c106f377e16f34 eb1808d6b9362 c9**** | The ID of the cluster. |

Response syntax

```
HTTP/1.1 200 OK
```

Response parameters No response parameters. Examples Sample requests

```
POST /api/v2/clusters/c106f377e16f34eb1808d6b9362c9****/upgrade/cancel HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK
```

Error codes You can check further details of error codes. For more information, see Error codes.

##### 3.1.7.5 ResumeUpgradeCluster

Resumes the upgrade of a specified Container Service cluster. Request syntax

```
POST /api/v2/clusters/ClusterId/upgrade/resume HTTP/1.1
```

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClusterId | String | Yes | c82e6987e2961 451182edacd74 faf**** | The ID of the cluster. |

Response syntax

```
HTTP/1.1 200 OK
```

Response parameters No response parameters. Examples Sample requests

```
POST /api/v2/clusters/c82e6987e2961451182edacd74faf****/upgrade/resume HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK
```

Error codes You can check further details of error codes. For more information, see Error codes.

### 3.2 Nodes

#### 3.2.1 DescribeClusterNodes

Queries information about the nodes in a specified Container Service cluster. Request headers This operation uses only common request headers. For more information, see the Common request parameters topic. Request syntax

```
get /clusters/{ClusterId}/nodes http|https
```

Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClusterId | String | Yes | c82e6987e29614 51182edacd74faf **** | The ID of the cluster. |
| pageSize | String | No | 3 | The number of entries to return on each page. |
| pageNumber | String | No | 50 | The number of the page to return. |
| nodepool id _ | String | No | np*** | The ID of the node pool. |
| state | String | No | all | The state of the nodes in the cluster. You can filter the nodes by state. Valid values: all: Query all nodes in the cluster. running: Query nodes that are running in the cluster. removing: Query nodes that are being removed from the cluster. initial: Query nodes that are initializing in the cluster. failed: Query nodes that failed to be created in the cluster. |

Response

| Parameter | Type | Example | Description |
|---|---|---|---|
| nodes | Array of node |   | The details of the nodes in the cluster. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| creation time _ | String | "2020-08- 25T11:25:35+08:00 " | The time when the node was created. |
| error message _ | String | "***" | The error message generated when the node was created. |
| expired time _ | String | "2099-12- 31T23:59:00+08:00 " | The expiration time of the node. |
| host name _ | String | "iZ2vcckdmxp7u0urj 2k****" | The name of the host. |
| image id _ | String | "aliyun 2 1903 x64 _ _ _ _ 20G alibase 202005 _ _ 29.vhd" | The ID of the system image that is used by the node. |
| instance charg _ e type _ | String | "PostPaid" | The billing method of the node. |
| instance id _ | String | "i- 2vcckdmxp7u0urj2k2 rw" | The ID of the Elastic Compute Service (ECS) instance on which the node is created. |
| instance name _ | String | "worker-k8s-for-cs- c5cdf7e3938bc4f8e b0e44b21a80f****" | The name of the node. |
| instance role _ | String | "Worker" | The type of node. Valid values: Master: master node. Worker: worker node. |
| instance status _ | String | "Running" | The state of the node. |
| instance type _ | String | "ecs.c5.xlarge" | The instance type of the node. |
| instance type f _ _ amily | String | "ecs.c5" | The ECS instance family of the node. |
| ip address _ | Array of String |   | The IP address of the node. |
| is aliyun node _ _ | Boolean | "true" | Indicates whether the instance is provided by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| node name _ | String | "cn- chengdu.192.168.0.3 6" | The name of the node. This name is the identifier of the node in the cluster. |
| node status _ | String | "Ready" | Indicates whether the node is ready. |
| nodepool id _ | String | "np0794239424a84e b7a95327369d56*** *" | The ID of the node pool to which the node belongs. |
| source | String | "ess attach" _ | The source of the node. You can add a node to a cluster in the Container Service console or Resource Orchestration Service (ROS) console. |
| state | String | "running" | The state of the node. |
| page | Object |   | The pagination details. |
| page number _ | Integer | "1" | The page number of the returned page. |
| page size _ | Integer | "10" | The number of entries returned per page. |
| total count _ | Integer | "5" | The total number of entries returned. |

Sample requests

```
GET /clusters/[ClusterId]/nodes HTTP/1.1 Common request headers
```

`{`

```json
    "ClusterId":" c82e6987e2961451182edacd74faf****"
```

Sample success responses `XML` format

```xml
<nodes>
    <creation_time>2020-08-25T11:25:35+08:00</creation_time>
    <error_message/>
    <instance_name>worker-k8s-for-cs-c5cdf7e3938bc4f8eb0e44b21a80f****</instance_name>
    <node_status>Ready</node_status>
    <is_aliyun_node>true</is_aliyun_node>
    <node_name>cn-chengdu.192.168.0.36</node_name>
    <expired_time>2099-12-31T23:59:00+08:00</expired_time>
    <ip_address>192.168.0.36</ip_address>
    <source>ess_attach</source>
    <instance_type_family>ecs.c5</instance_type_family>
    <instance_id>i-2vcckdmxp7u0urj2k2rw</instance_id>
    <instance_charge_type>PostPaid</instance_charge_type>
    <instance_role>Worker</instance_role>
    <instance_status>Running</instance_status>
    <state>running</state>
    <image_id>aliyun_2_1903_x64_20G_alibase_20200529.vhd</image_id>
    <instance_type>ecs.c5.xlarge</instance_type>
    <nodepool_id>np0794239424a84eb7a95327369d56****</nodepool_id>
    <host_name>iZ2vcckdmxp7u0urj2k****</host_name>
</nodes> <page>
    <page_number>1</page_number>
    <total_count>5</total_count>
    <page_size>10</page_size>
</page>
```

`JSON` format `{`

```json
    "nodes": [
```

`{`

```json
            "creation_time": "2020-08-25T11:25:35+08:00",
            "error_message": "",
            "instance_name": "worker-k8s-for-cs-c5cdf7e3938bc4f8eb0e44b21a80f****",
            "node_status": "Ready",
            "is_aliyun_node": "true",
            "node_name": "cn-chengdu.192.168.0.36",
            "expired_time": "2099-12-31T23:59:00+08:00",
            "ip_address": "192.168.0.36",
            "source": "ess_attach",
            "instance_type_family": "ecs.c5",
            "instance_id": "i-2vcckdmxp7u0urj2k2rw",
            "instance_charge_type": "PostPaid",
            "instance_role": "Worker",
            "instance_status": "Running",
            "state": "running",
            "image_id": "aliyun_2_1903_x64_20G_alibase_20200529.vhd",
            "instance_type": "ecs.c5.xlarge",
            "nodepool_id": "np0794239424a84eb7a95327369d56****",
            "host_name": "iZ2vcckdmxp7u0urj2k****"
```

`],`

```json
    "page": {
        "page_number": "1",
        "total_count": "5",
        "page_size": "10"
```

Error codes You can check further details of error codes. For more information, see Error codes.

#### 3.2.2 RemoveClusterNodes

Removes nodes from a specified Container Service cluster. Not e When you remove a node, the pods that run on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours. Unknown errors may occur when you remove nodes. Before you remove nodes, we recommend that you back up the data of these nodes. Nodes remain in the Unschedulable state when they are being removed. You can remove only worker nodes by calling this operation. Request headers This operation uses only common request headers. For more information, see Common parameters. Request syntax

```
POST /api/v2/clusters/{ClusterId}/nodes/remove
```

Request parameters

| Parameter | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c82e6987e2961 451182edacd74 faf**** | The ID of the cluster. |
|   | Object | Body | No |   | Specifies whether to release the Elastic Compute Service (ECS) instances when they are removed from the cluster. |
| drain node _ | Boolea n | Body | No | true | Specifies whether to remove all pods from the nodes that you want to remove. |
| nodes | Array of String | Body | Yes | cn- shenzhen.10.1. 0.1 | The names of the nodes that you want to remove. |
| release node _ | Boolea n | Body | No | false | Specifies whether to release the ECS instances when they are removed from the cluster. |

Examples Sample requests

```
POST /api/v2/clusters/c82e6987e2961451182edacd74faf****/nodes/remove Common request headers
```

`{`

```json
    "release_node":false,
    "nodes":[
        "cn-shenzhen.192.168.x.x"
```

`],`

```json
    "drain_node":false
```

Error codes You can check further details of error codes. For more information, see Error codes.

#### 3.2.3 AttachInstances

Adds existing Elastic Compute Service (ECS) instances to a specified Container Service cluster. Request syntax

```
POST /clusters/ClusterId/attach HTTP/1.1
```

`{`

```json
  "instances" : [ "String" ],
  "key_pair" : "String",
  "password" : "String",
  "format_disk" : Boolean,
  "keep_instance_name" : Boolean,
  "is_edge_worker" : Boolean,
  "nodepool_id" : "String",
  "image_id" : "String",
  "cpu_policy" : "String",
  "user_data" : "String",
  "rds_instances" : [ "String" ],
  "runtime" : {
    "name" : "String",
    "version" : "String"
```

`},`

```json
  "tags" : [ {
    "key" : "String",
    "value" : "String"
  } ]
```

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClusterId | String | Yes | c106f377e16f34 eb1808d6b9362 c9**** | The ID of the cluster. |

Request body parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| instances | Array of String | Yes | i- 2zed0sswuau6o 89b**** | The IDs of the ECS instances that you want to add. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| key pair _ | String | Yes | secrity-key | The name of the key pair that is used to log to the ECS instances. You must set this parameter or the login password parameter. _ |
| password | String | Yes | Hello1234 | The Secure Shell (SSH) logon password that is used to log on to the ECS instances. You must set this parameter or the key pair _ parameter. The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. It cannot contain backward slashes (\) or double quotation marks ("). For security considerations, the password is encrypted during data transfer. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| format disk _ | Boolean | No | false | Specifies whether to store the data of containers and images on a data disk. Valid values: true : stores the data of containers and images on a data disk. false : does not store the data of containers and images on a data disk. Default value: false . How to mount a data disk: If the ECS instances have data disks mounted and the file system of the last data disk is not initialized, the system automatically formats the data disk to ext4. Then, the system mounts the data disk to /var/lib/docker and /var/lib/kubelet. The system does not create and mount a new data disk if no data disk has been mounted to the ECS instances. Not e If you mount a data disk to the ECS instances and write data to the data disk, the original data on the disk is erased. Back up data before you mount a data disk. |
| keep instance n _ _ ame | Boolean | No | true | Specifies whether to retain the names of the ECS instances. Valid values: true : retains the instances names. false : does not retain the instance names. Default value: true . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| is edge worker _ _ | Boolean | No | false | Specifies whether the instances that you want to add are Edge Node Service (ENS) nodes. Valid values: true : The instances that you want to add are ENS nodes. false : The instances that you want to add are not ENS nodes. Default value: false . Not e : If the instances that you want to add are ENS nodes, you must set this parameter to true . This allows you to identify these ENS nodes. |
| nodepool id _ | String | No | np615c0e09661 24216a0412e10 afe0**** | The ID of the node pool to which the instances are added. If you do not set this parameter, the instances are added to a default node pool. |
| image id _ | String | No | aliyun 2 1903 x _ _ _ 64 20G alibase _ _ 20200529.vhd _ | The ID of the custom image. If you do not set this parameter, the default system image is used. Not e : If you specify a custom image, the custom image is used to deploy the operating systems on the system disks of the instances. |

| Parameter | Type | Required | Example | Description |   |   |   |
|---|---|---|---|---|---|---|---|
| cpu policy _ | String | No | none | The CPU policy. The following policies are supported if the cluster version is 1.12.6 or later. static : This policy allows pods with specific resource characteristics on the node to be granted with enhanced CPU affinity and exclusivity. none : This policy indicates that the default CPU affinity is used. Default value: none . |   |   |   |
| user data _ | String | No | IyEvdXNyL2Jpbi9 iYXNoCmVjaG8g IkhlbGxvIEFDSyEi | The user-defined data. For more information, see the User-defined data chapter in the ECS documentation. |   |   |   |
| rds instances _ | Array of String | No | rm- 67yawhau**** | The IDs of the Relational Database Service (RDS) instances. |   |   |   |
| runtime | runtime | No |   | The container runtime. |   |   |   |
| tags | Array of tag | No |   | The labels to be added to nodes. Labeling rules: Each label consists of a case- sensitive key-value pair. You can add up to 20 labels. When you add a label, you must specify a unique key but you can leave the value empty. A key cannot exceed 64 characters in length and a value cannot exceed 128 characters in length. Keys and values cannot start with al iyun , acs: , https:// , or http:// . |   |   |   |
|   |   |   |   |   |   | al |   |
|   |   |   |   |   | https:// |   |   |

Response syntax

```
HTTP/1.1 200
```

`{`

```json
  "list" : [ {
    "code" : "String",
    "instanceId" : "String",
    "message" : "String"
  } ],
  "task_id" : "String"
```

Response parameters Response body parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| list | Array of list |   | The details of the added instances. |
| code | String | 200 | The code that indicates the task result. |
| instanceId | String | i- 2ze0lgm3y6iylcbt*** * | The IDs of the added ECS instances. |
| message | String | successful | Indicates whether the ECS instances are added to the specified cluster. |
| task id _ | String | T- 5a544aff80282e39e a000039 | The ID of the task. |

Examples Sample requests

```
POST /clusters/c106f377e16f34eb1808d6b9362c9****/attach HTTP/1.1
```

`{`

```json
  "instances" : [ "i-2zed0sswuau6o89b****" ],
  "key_pair" : "secrity-key",
  "password" : "Hello1234",
  "format_disk" : false,
  "keep_instance_name" : true,
  "is_edge_worker" : false,
  "nodepool_id" : "np615c0e0966124216a0412e10afe0****",
  "image_id" : "aliyun_2_1903_x64_20G_alibase_20200529.vhd",
  "cpu_policy" : "none",
  "user_data" : "IyEvdXNyL2Jpbi9iYXNoCmVjaG8gIkhlbGxvIEFDSyEi",
  "rds_instances" : [ "rm-67yawhau****" ],
  "runtime" : {
    "name" : "docker",
    "version" : "19.03.5"
```

`},`

```json
  "tags" : [ {
    "key" : "env",
    "value" : "prod"
  } ]
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <list>
    <code>200</code>
    <instanceId>i-2ze0lgm3y6iylcbt****</instanceId>
    <message>successful</message>
</list> <task_id>T-5a544aff80282e39ea000039</task_id>
```

`JSON` format

```
HTTP/1.1 200 OK
```

`{`

```json
  "list" : [ {
    "code" : "200",
    "instanceId" : "i-2ze0lgm3y6iylcbt****",
    "message" : "successful"
  } ],
  "task_id" : "T-5a544aff80282e39ea000039"
```

Error codes You can check further details of error codes. For more information, see Error codes.

#### 3.2.4 DescribeClusterAttachScripts

Adds an existing instance to a specified Container Service cluster. This operation returns a unique executable script. You can run this script on an existing instance to add the instance to the specified cluster. Request syntax

```
POST /clusters/ClusterId/attachscript HTTP/1.1
```

`{`

```json
  "nodepool_id" : "String",
  "format_disk" : Boolean,
  "keep_instance_name" : Boolean,
  "rds_instances" : [ "String" ],
  "arch" : "String",
  "options" : "String"
```

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClusterId | String | Yes | ca375a93a3047 4552ad2a0ebe1 83e**** | The ID of the cluster. |

Request body parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| nodepool id _ | String | No | np1c9229d9be2 d432c93f77a88f ca0**** | The ID of the node pool to which the existing instance is added. You can specify this parameter to add the existing instance to a specific node pool. |

| Parameter | Type | Required |   | Example | Description |   |
|---|---|---|---|---|---|---|
| format disk _ | Boolean | No |   | false | Specifies whether to mount data disks to the existing instance when the instance is added to the cluster. You can add data disks to store the data of containers and images. Valid values: true : mounts data disks to the existing instance. If you mount a data disk to the instance and write data to the data disk, the original data on the disk is erased. Back up data before you mount a data disk. false : does not mount data disks to the existing instance. Default value: false . How to mount a data disk: If the existing Elastic Compute Service (ECS) instance has data disks mounted and the file system of the last data disk is not initialized, the system automatically formats the data disk to ext4. Then, the system mounts the data disk to /var/lib/docker and /var/lib/kubelet. The system does not create and mount a new data disk if no data disk has been mounted to the ECS instance. |   |
| keep instance n _ _ ame | Boolean | No |   |   | Specifies whether to retain the name of the existing instance when the instance is added to the cluster. If you do not retain the instance name, the instance is named in the worker-k8s-for-cs- <clusterid> format. Valid values: true : retains the instance name. false : does not retain the instance name. Default value: true . |   |
|   |   |   |   |   |   | worker-k8s-for-cs- |
|   |   |   |   |   | <clusterid> |   |
|   |   |   |   | true |   |   |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| rds instances _ | Array of String | No | rm-xxx | The names of the Relational Database Service (RDS) instances. |
| arch | String | No | amd64 | The CPU architecture of the node. Valid values: amd64 , arm , and arm64 . Default value: amd64 . Not e This parameter is required if the existing instance is added to a managed edge Kubernetes cluster. |
| options | String | No | {\"enableIptabl es\": true,\"manageR untime\": true,\"quiet\": true,\"allowedC lusterAddons\": [\"kube- proxy\",\"flann el\",\"coredns\" ]} | The connection configurations of the existing instance that you want to add. Not e This parameter is required if the existing instance is added to a managed edge Kubernetes cluster. |

|   | amd64 |
|---|---|
| arm64 |   |

Response syntax

```
HTTP/1.1 200
```

`{`

```json
  "result" : "String"
```

Response parameters Response body parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
|   | String | "wget http://aliacs- k8s-cn- hangzhou.oss-cn- hangzhou.aliyuncs.c om/public/pkg/run/ attach/1.12.6- aliyunedge.1/edgea dm -O edgeadm; chmod u+x edgeadm; ./edgeadm join -- openapi-token=XXX --node-spec=" {\"flannelIface\":\"e th0\",\"enableIptabl es\":true,\"assume Yes\":true,\"manag eRuntime\":true,\"n odeNameStrategy\" :\"hostname\",\"en abledAddons\": [\"kube- proxy\",\"flannel\",\ "coredns\"]}"" | The returned script that is used to add an existing instance to the specified cluster. |

Examples Sample requests

```
POST /clusters/ca375a93a30474552ad2a0ebe183e****/attachscript HTTP/1.1
```

`{`

```json
  "nodepool_id" : "np1c9229d9be2d432c93f77a88fca0****",
  "format_disk" : false,
  "keep_instance_name" : true,
  "rds_instances" : [ "rm-xxx" ],
  "arch" : "amd64",
  "options" : "{\\\"enableIptables\\\": true,\\\"manageRuntime\\\": true,\\\"quiet\\\": tru
e,\\\"allowedClusterAddons\\\": [\\\"kube-proxy\\\",\\\"flannel\\\",\\\"coredns\\\"]}"
```

Description of the sample request

```
When you add an existing instance to a managed edge Kubernetes cluster, you must set option s and arch. The following content describes the parameters of options:
```
```

`{`

```json
    "options":"{
        "allowedClusterAddons": The name of the component.
        "enableIptables": Specifies whether to enable iptables. Default value: true.
        "flannelIface": the network interface controller (NIC) that is used by the Flannel
plug-in. By default, this parameter is set to the name of the NIC that is specified in the default route entry of the node.
        "gpuVersion": Specifies whether the node to be added is a GPU-accelerated node. By
default, this parameter is empty. Valid values: Nvidia_Tesla_T4, Nvidia_Tesla_P4, and Nvidi a_Tesla_P100.
        "manageRuntime": Specifies whether to use edgeadm to install and check the runtime.
Default value: false.
        "nodeNameOverride": Specifies how the node is named. A pair of quotation marks ("")
indicates the host name is used as the node name. This is the default value. An asterisk (* ) indicates that a random string that contains six characters is used as the node name.The string "*.XXX" indicates that a random string that is followed by a suffix is used as the n ode name. The random string contains six characters.
        "quiet": Specifies whether to enable the silent installation mode.
```
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <result>"wget http://aliacs-k8s-cn-hangzhou.oss-cn-hangzhou.aliyuncs.com/public/pkg/run/att ach/1.12.6-aliyunedge.1/edgeadm -O edgeadm; chmod u+x edgeadm; ./edgeadm join --openapi-tok en=XXX --node-spec="{\"flannelIface\":\"eth0\",\"enableIptables\":true,\"assumeYes\":true,\ "manageRuntime\":true,\"nodeNameStrategy\":\"hostname\",\"enabledAddons\":[\"kube-proxy\",\ "flannel\",\"coredns\"]}""</result>
```

`JSON` format

```
HTTP/1.1 200 OK
```

`{`

```json
  "result" : "\"wget http://aliacs-k8s-cn-hangzhou.oss-cn-hangzhou.aliyuncs.com/public/pkg/
run/attach/1.12.6-aliyunedge.1/edgeadm -O edgeadm; chmod u+x edgeadm; ./edgeadm join --open api-token=XXX --node-spec=\"{\\\"flannelIface\\\":\\\"eth0\\\",\\\"enableIptables\\\":true, \\\"assumeYes\\\":true,\\\"manageRuntime\\\":true,\\\"nodeNameStrategy\\\":\\\"hostname\\\" ,\\\"enabledAddons\\\":[\\\"kube-proxy\\\",\\\"flannel\\\",\\\"coredns\\\"]}\"\""
```

Description of the sample response

```
If the cluster is not a managed edge Kubernetes cluster, the following script is returned: "curl http://aliacs-k8s-cn-chengdu.oss-cn-chengdu-internal.aliyuncs.com/public/pkg/run/atta ch/1.16.9-aliyun.1/attach_node.sh | bash -s -- --node-name-mode nodeip --cms-enabled --cmsversion 1.3.7 --openapi-token **** --addon-names flannel,csi-plugin,csi-provisioner,logtail -ds,ack-node-problem-detector,nginx-ingress-controller,kube-flannel-ds --cpu-policy none -node-cidr-mask 26 --node-port-range 30000-32767 --runtime docker --runtime-version 19.03.5" If the cluster is a managed edge Kubernetes cluster, the following script is returned: "wget http://aliacs-k8s-cn-hangzhou.oss-cn-hangzhou.aliyuncs.com/public/pkg/run/attach/1.12 .6-aliyunedge.1/edgeadm -O edgeadm; chmod u+x edgeadm; ./edgeadm join --openapi-token=*** - -node-spec="{\"flannelIface\":\"eth0\",\"enableIptables\":true,\"assumeYes\":true,\"manageR untime\":true,\"nodeNameStrategy\":\"hostname\",\"enabledAddons\":[\"kube-proxy\",\"flannel \",\"coredns\"]}""
```

Error codes You can check further details of error codes. For more information, see Error codes.

#### 3.2.5 Node pools

##### 3.2.5.1 CreateClusterNodePool

Creates a node pool for a Container Service cluster. Request syntax

```
POST /clusters/ClusterId/nodepools HTTP/1.1
```

`{`

```json
  "auto_scaling" : {
    "enable" : Boolean,
    "max_instances" : Long,
    "min_instances" : Long,
    "type" : "String",
```

`},`

```json
  "kubernetes_config" : {
    "cms_enabled" : Boolean,
    "cpu_policy" : "String",
    "labels" : [ {
      "key" : "String",
      "value" : "String"
    } ],
    "runtime" : "String",
    "runtime_version" : "String",
    "taints" : [ {
      "key" : "String",
      "value" : "String",
      "effect" : "String"
    } ],
    "user_data" : "String"
```

`},`

```json
  "nodepool_info" : {
```

```json
    "name" : "String",
```

`},`

```json
  "scaling_group" : {
    "data_disks" : [ {
      "category" : "String",
      "size" : Long,
      "encrypted" : "String",
      "auto_snapshot_policy_id" : "String"
    } ],
    "image_id" : "String",
    "instance_charge_type" : "String",
    "instance_types" : [ "String" ],
    "login_password" : "String",
    "platform" : "String",
    "rds_instances" : [ "String" ],
    "scaling_policy" : "String",
    "system_disk_category" : "String",
    "system_disk_size" : Long,
    "tags" : [ {
      "key" : "String",
      "value" : "String"
    } ],
    "vswitch_ids" : [ "String" ],
```

`},`

```json
  "tee_config" : {
    "tee_enable" : Boolean
```

`},`

```json
  "count" : Long
```

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClusterId | String | Yes | c61da77e8bfbc 4c4c999af2b51 b65**** | The ID of the cluster. |

Request body parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| auto scaling _ | Object | No |   | The configuration of auto scaling. |

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| enable | Boolean | Yes | true | Specifies whether to enable auto scaling. Valid values: true : enables auto scaling for the node pool. false : disables auto scaling for the node pool. If you set the parameter to false, the auto s _ caling parameter does not take effect. Default value: false . |   |   |
|   |   |   |   |   | auto s _ |   |
| max instances _ | Long | Yes | 10 | The maximum number of Elastic Compute Service (ECS) instances in the scaling group. |   |   |
| min instances _ | Long | Yes | 1 | The minimum number of ECS instances in the scaling group. |   |   |
| type | String | No | cpu | The type of instances that are specified for auto scaling. Valid values: cpu : regular instance. gpu : GPU-accelerated instance. gpushare : instance that uses shared GPUs. spot : preemptible instance. Default value: cpu . |   |   |
| kubernetes con _ fig | Object | No |   | The configuration of the cluster. |   |   |

|   | caling |
|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| cms enabled _ | Boolean | No | true | Specifies whether to install the CloudMonitor agent on ECS instances. After the CloudMonitor agent is installed on ECS instances, you can view monitoring information about the instances in the CloudMonitor console. We recommend that you install the CloudMonitor agent. Valid values: true : installs the CloudMonitor agent on ECS instances. false : does not install the CloudMonitor agent on ECS instances. Default value: false . |
| cpu policy _ | String | No | none | The CPU policy. The following policies are supported if the cluster version is 1.12.6 or later. static : This policy allows pods with specific resource characteristics on the node to be granted with enhanced CPU affinity and exclusivity. none : This policy indicates that the default CPU affinity is used. Default value: none . |
| labels | Array of tag | No |   | The labels of the cluster. You can add labels to the nodes in the cluster. |
| runtime | String | Yes | docker | The container runtime. |
| runtime version _ | String | Yes | 19.03.5 | The version of the container runtime. |
| taints | Array of taint | No |   | The taints of the nodes in the cluster. |
| user data _ | String | No | dGhpcyBpcyBhIG V4YW1wbGU= | The user-defined data. |

| eveloper Guide·Clu | ster API list |   |   | Container Service for Kubernete |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| nodepool info _ | Object | No |   | The configuration of the node pool. |
| name | String | Yes | cluster-demo | The name of the node pool. |
| scaling group _ | Object | No |   | The configuration of the scaling group. |
| data disks _ | Array of data di _ sk | No |   | The configurations of data disks that are mounted to the nodes in the node pool. |
| image id _ | String | No | aliyun 2 1903 x _ _ _ 64 20G alibase _ _ 20200529.vhd _ | The ID of a custom image. By default, the system image is used. |
| instance charge _ type _ | String | Yes | PrePaid | The billing method of the nodes in the node pool. Valid values: PrePaid : subscription. PostPaid : pay-as-you-go. Default value: PostPaid . |
| instance types _ | Array of String | Yes | ecs.d1ne.2xlarg e | The instance types of the nodes in the node pool. |
| login password _ | String | No | Hello1234 | The Secure Shell (SSH) logon password. The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| platform | String | Yes | Linux | The release version of the operating system. Valid values: CentOS AliyunLinux Windows WindowsCore Default value: AliyunLinux. |
| rds instances _ | Array of String | No | rds-**** | The IDs of the Relational Database Service (RDS) instances. |
| scaling policy _ | String | No | release | The scaling mode of the scaling group. Valid values: release : the standard mode. Auto scaling is implemented by creating or releasing ECS instances based on the requested resources. recycle : the swift mode. Auto scaling is implemented by creating, stopping, and starting ECS instances. This mode accelerates scaling activities. When an ECS instance is stopped, you are charged only the storage fees. This does not apply to ECS instances that use local disks. Default value: release . |
| system disk cat _ _ egory | String | Yes | cloud efficiency _ | The type of system disk that is specified for the nodes in the node pool. Valid values: cloud efficiency : ultra _ disk. cloud ssd : standard SSD. _ cloud essd : enhanced SSD. _ Default value: cloud efficiency. _ |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| system disk siz _ _ e | Long | Yes | 120 | The size of the system disk that is specified for the nodes in the node pool. Unit: GiB. Valid values: 40 to 500. |
| tags | Array | No |   | The labels of ECS instances. You can add labels to only ECS instances. The key of each label must be unique and cannot exceed 128 characters in length. Keys and values cannot start with aliyun or acs:. Keys and values cannot contain https:// or http://. |
| key | String | No | node-k-1 | The key of the label. |
| value | String | No | node-v-1 | The value of the label. |
| vswitch ids _ | Array of String | Yes | vsw- wz9mfnhmssud 6eicu**** | The IDs of vSwitches. |
| tee config _ | Object | No |   | The configuration of confidential computing. |
| tee enable _ | Boolean | Yes | true | Specifies whether to enable confidential computing for the cluster. |
| count | Long | No | 1 | The number of nodes in the node pool. |

Response syntax

```
HTTP/1.1 200
```

`{`

```json
  "nodepool_id" : "String"
```

Response parameters Response body parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| nodepool id _ | String | np31da1b38983f451 1b490fc62108a**** | The ID of the node pool. |

Examples Sample requests

```
POST /clusters/c61da77e8bfbc4c4c999af2b51b65****/nodepools HTTP/1.1
```

`{`

```json
  "auto_scaling" : {
    "enable" : true,
    "max_instances" : 10,
    "min_instances" : 1,
    "type" : "cpu",
```

`},`

```json
  "kubernetes_config" : {
    "cms_enabled" : true,
    "cpu_policy" : "none",
    "labels" : [ {
      "key" : "env",
      "value" : "prod"
    } ],
    "runtime" : "docker",
    "runtime_version" : "19.03.5",
    "taints" : [ {
      "key" : "key",
      "value" : "value",
      "effect" : "NoSchedule"
    } ],
    "user_data" : "dGhpcyBpcyBhIGV4YW1wbGU="
```

`},`

```json
  "nodepool_info" : {
    "name" : "cluster-demo",
```

`},`

```json
  "scaling_group" : {
    "data_disks" : [ {
      "category" : "cloud_ssd",
      "size" : 40,
      "encrypted" : "true",
      "auto_snapshot_policy_id" : "sp-2zej1nogjvovnz4z****"
    } ],
    "image_id" : "aliyun_2_1903_x64_20G_alibase_20200529.vhd",
    "instance_charge_type" : "PrePaid",
    "instance_types" : [ "ecs.d1ne.2xlarge" ],
    "login_password" : "Hello1234",
    "platform" : "Linux",
    "rds_instances" : [ "rds-***" ],
    "scaling_policy" : "release",
    "system_disk_category" : "cloud_efficiency",
    "system_disk_size" : 120,
    "tags" : [ {
```

`g`

```json
      "key" : "node-k-1",
      "value" : "node-v-1"
    } ],
    "vswitch_ids" : [ "vsw-wz9mfnhmssud6eicu****" ],
```

`},`

```json
  "tee_config" : {
    "tee_enable" : true
```

`},`

```json
  "count" : 1
```

Description of the sample request

```
Create a node pool that supports auto scaling:
```

`{`

```json
    "ClusterId":"c61da77e8bfbc4c4c999af2b51b65****",
    "nodepool_info":{
        "name":"autoScale-demo",
```

`},`

```json
    "scaling_group":{
        "vswitch_ids":[
            "vsw-wz9mfnhmssud6eic****"
```

`],`

```json
        "system_disk_category":"cloud_efficiency",
        "system_disk_size":120,
        "data_disks":[
```

`],`

```json
        "instance_types":[
            "ecs.t6-c1m2.large"
```

`],`

```json
        "vpc_id":"vpc-wz984yvbd6lck22z3****",
        "tags":[
```

`],`

```json
        "instance_charge_type":"PostPaid",
        "login_password":"****",
        "platform":"AliyunLinux",
        "image_id":"aliyun_2_1903_x64_20G_alibase_20200529.vhd",
        "rds_instances":[
```

`],`

```json
        "scaling_policy":"release"
```

`},`

```json
    "kubernetes_config":{
        "cpu_policy":"none",
        "cms_enabled":false,
        "labels":[
```

`{`

```json
                "key":"workload_type",
                "value":"cpu"
```

`],`

```json
        "taints":[
```

`],`

```json
        "user_data":"",
        "runtime":"docker",
        "runtime_version":"19.03.5"
```

`},`

```json
    "tee_config":{
        "tee_enable":true
```

`},`

```json
    "auto_scaling":{
        "enable":true,
        "max_instances":10,
        "min_instances":1,
        "type":"cpu"
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <nodepool_id>np31da1b38983f4511b490fc62108a****</nodepool_id>
```

`JSON` format

```
HTTP/1.1 200 OK
```

`{`

```json
  "nodepool_id" : "np31da1b38983f4511b490fc62108a****"
```

Error codes You can check further details of error codes. For more information, see Error codes.

##### 3.2.5.2 ScaleClusterNodePool

Scales out a node pool. Request syntax

```
POST /clusters/ClusterId/nodepools/NodepoolId HTTP/1.1
```

`{`

```json
  "count" : Long
```

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClusterId | String | Yes | c23421cfa74454 bc8b37163fd19 af**** | The ID of the cluster to which the node pool belongs. |
| NodepoolId | String | Yes | np31da1b38983 f4511b490fc621 08a**** | The ID of the node pool. |

Request body parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| count | Long | No | 1 | The number of nodes that you want to add to the node pool. You can add at most 500 nodes in one API call. The maximum number of nodes that can be added is limited by the quota of nodes in the cluster. |

Response syntax

```
HTTP/1.1 200
```

`{`

```json
  "task_id" : "String"
```

Response parameters Response body parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| task id _ | String | T- 5faa48fb31b6b8078 d00**** | The ID of the task. |

Examples Response example

```
POST /clusters/c23421cfa74454bc8b37163fd19af****/nodepools/np31da1b38983f4511b490fc62108a**
** HTTP/1.1
```

`{`

```json
  "count" : 1
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <task_id>T-5faa48fb31b6b8078d00****</task_id>
```

`JSON` format

```
HTTP/1.1 200 OK
```

`{`

```json
  "task_id" : "T-5faa48fb31b6b8078d00****"
```

Error codes You can check further details of error codes. For more information, see Error codes.

##### 3.2.5.3 ModifyClusterNodePool

Updates the configuration of a node pool. Request syntax

```
PUT /clusters/ClusterId/nodepools/NodepoolId HTTP/1.1
```

`{`

```json
  "auto_scaling" : {
    "enable" : Boolean,
    "max_instances" : Long,
    "min_instances" : Long,
    "type" : "String"
```

`},`

```json
  "kubernetes_config" : {
    "cms_enabled" : Boolean,
    "cpu_policy" : "String",
    "labels" : [ {
      "key" : "String",
      "value" : "String"
    } ],
    "runtime" : "String",
    "runtime_version" : "String",
    "taints" : [ {
      "key" : "String",
      "value" : "String",
      "effect" : "String"
    } ],
    "user_data" : "String"
```

`},`

```json
  "nodepool_info" : {
    "name" : "String",
    "resource_group_id" : "String"
```

`},`

```json
  "scaling_group" : {
    "data_disks" : [ {
      "category" : "String",
      "size" : Long,
      "encrypted" : "String",
      "auto_snapshot_policy_id" : "String"
    } ],
    "instance_charge_type" : "String",
```

```json
    "platform" : "String",
    "image_id" : "String",
    "instance_types" : [ "String" ],
    "login_password" : "String",
    "rds_instances" : [ "String" ],
    "scaling_policy" : "String",
    "system_disk_category" : "String",
    "system_disk_size" : Long,
    "tags" : [ {
      "key" : "String",
      "value" : "String"
    } ],
    "vswitch_ids" : [ "String" ],
```

`},`

```json
  "tee_config" : {
    "tee_enable" : Boolean
```

`},`

```json
  "update_nodes" : Boolean
```

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClusterId | String | Yes | c23421cfa74454 bc8b37163fd19 af**** | The ID of the cluster to which the node pool belongs. |
| NodepoolId | String | Yes | p31da1b38983f 4511b490fc621 08a**** | The ID of the node pool. |

Request body parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| auto scaling _ | Object | No |   | The configuration of auto scaling. |

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| enable | Boolean | No | true | Specifies whether to enable auto scaling. Valid values: true : enables auto scaling for the node pool. false : disables auto scaling for the node pool. If you set this parameter to false, the auto s _ caling parameter does not take effect. Default value: false . |   |   |
|   |   |   |   |   | auto s _ |   |
| max instances _ | Long | No | 10 | The maximum number of Elastic Compute Service (ECS) instances. |   |   |
| min instances _ | Long | No | 2 | The minimum number of ECS instances. |   |   |
| type | String | No | cpu | The type of instances that are specified for auto scaling. Valid values: cpu : regular instance. gpu : GPU-accelerated instance. gpushare : instance that uses shared GPUs. spot : preemptible instance. Default value: cpu . |   |   |
| kubernetes con _ fig | Object | No |   | The configuration of the cluster. |   |   |

|   | caling |
|---|---|

| Parameter | Type | Required | Example | Description |   |   |   |
|---|---|---|---|---|---|---|---|
| cms enabled _ | Boolean | No | true | Specifies whether to install the CloudMonitor agent on ECS instances. After the CloudMonitor agent is installed on ECS instances, you can view monitoring information about the instances in the CloudMonitor console. We recommend that you install the CloudMonitor agent. Valid values: true : installs the CloudMonitor agent on ECS instances. false : does not install the CloudMonitor agent on ECS instances. Default value: false . |   |   |   |
| cpu policy _ | String | No | none | The CPU policy. The following policies are supported if the cluster version is 1.12.6 or later. static : This policy allows pods with specific resource characteristics on the node to be granted with enhanced CPU affinity and exclusivity. none : This policy indicates that the default CPU affinity is used. Default value: none . |   |   |   |
| labels | Array of tag | No |   | The labels of nodes. You can add labels to the nodes in the cluster. Labeling rules: Each label consists of a case- sensitive key-value pair. You can add up to 20 labels. When you add a label, you must specify a unique key but you can leave the value empty. A key cannot exceed 64 characters in length and a value cannot exceed 128 characters in length. Keys and values cannot start with al iyun , acs: , https:// , or http:// . |   |   |   |
|   |   |   |   |   |   | al |   |
|   |   |   |   |   | https:// |   |   |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| runtime | String | No | docker | The name of the container runtime. |
| runtime version _ | String | No | 19.03.5 | The version of the container runtime. |
| taints | Array of taint | No |   | The taints to be added to the nodes in the node pool. |
| user data _ | String | No | IyEvdXNyL2Jpbi9 iYXNoCmVjaG8g IkhlbGxvIEFDSyEi | The user-defined data of the node pool. For more information, see the User-defined data chapter in the ECS documentation. |
| nodepool info _ | Object | No |   | The configuration of the node pool. |
| name | String | No | default- nodepool | The name of the node pool. The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). It cannot start with a hyphen. |
| resource group _ id _ | String | No | rg- acfmyvw3wjm** ** | The ID of the resource group to which the node pool belongs. |
| scaling group _ | Object | No |   | The configuration of the scaling group. |
| data disks _ | Array of data di _ sk | No |   | The configurations of the data disks that are mounted to the nodes in the node pool. You can mount 0 to 10 data disks. You can mount at most 10 data disks to the nodes in the node pool. |
| platform | String | No | AliyunLinux | The operating system. Valid values: AliyunLinux CentOS Windows WindowsCore |

| Parameter | Type | Required |   | Example | Description |   |   |
|---|---|---|---|---|---|---|---|
| image id _ | String | No |   | aliyun 2 1903 x _ _ _ | The ID of the custom image. You can call the DescribeKubernetesVersionMet adata operation to query the supported images. By default, the latest image is used. |   |   |
|   |   |   |   |   |   | DescribeKubernetesVersionMet |   |
|   |   |   |   | 64 20G alibase _ _ 20200904.vhd | adata |   |   |
|   |   |   |   | _ |   |   |   |
| instance types _ | Array of String | No |   | ecs.c6.large | The instance types of the nodes in the node pool. For more information, see the Instance types chapter in ECS User Guide. |   |   |
| login password _ | String | No |   | Hello1234 | The Secure Shell (SSH) logon password. The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. |   |   |
| rds instances _ | Array of String | No |   | rds-xxx | The IDs of the Relational Database Service (RDS) instances. After you specify the list of RDS instances, the ECS instances in the cluster are automatically added to the whitelist of the RDS instances. |   |   |
| scaling policy _ | String | No |   | release | The scaling mode of the scaling group. Valid values: release : the standard mode. Auto scaling is implemented by creating or releasing ECS instances based on the requested resources. recycle : the swift mode. Auto scaling is implemented by creating, stopping, and starting ECS instances. This mode accelerates scaling activities. When an ECS instance is stopped, you are charged only the storage fees. This does not apply to ECS instances that use local disks. |   |   |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| system disk cat _ _ egory | String | No | cloud efficiency _ | The type of system disk that is specified for the nodes in the node pool. Valid values: cloud efficiency : ultra _ disk. cloud ssd : standard SSD. _ Default value: cloud ssd . _ |
| system disk siz _ _ e | Long | No | 120 | The size of the system disk that is specified for the nodes in the node pool. Unit: GiB. Valid values: 20 to 500. The value of this parameter must be no less than the greater value between 20 and the image size. Default value: the greater value between 40 and the image size. |
| tags | Array of tag | No |   | The labels of ECS instances. You can add labels to only ECS instances. The key of each label must be unique and cannot exceed 128 characters in length. Keys and values cannot start with aliyun, acs:, https://, or http://. |
| vswitch ids _ | Array of String | No | vsw- wz9uwxhawmt zg7u9h**** | The IDs of vSwitches. |
| tee config _ | Object | No |   | The configuration of confidential computing. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| tee enable _ | Boolean | No | false | Specifies whether to enable confidential computing for the cluster. true : enables confidential computing. false : disables confidential computing. Default value: false . |
| update nodes _ | Boolean | No | true | Specifies whether to update node information, such as labels and taints. |

Response syntax

```
HTTP/1.1 200
```

`{`

```json
  "task_id" : "String",
  "nodepool_id" : "String"
```

Response parameters Response body parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| task id _ | String | T- 5fd211e924e1d0078 7000293 | The ID of the task. |
| nodepool id _ | String | np737c3ac1ac68470 3b9e10673aa2c**** | The ID of the node pool. |

Examples Sample requests

```
PUT /clusters/c23421cfa74454bc8b37163fd19af****/nodepools/p31da1b38983f4511b490fc62108a**** HTTP/1.1
```

`{`

```json
  "auto_scaling" : {
    "enable" : true,
    "max_instances" : 10,
    "min_instances" : 2,
"type":"cpu"
```

```
    type : cpu
```

`},`

```json
  "kubernetes_config" : {
    "cms_enabled" : true,
    "cpu_policy" : "none",
    "labels" : [ {
      "key" : "env",
      "value" : "prod"
    } ],
    "runtime" : "docker",
    "runtime_version" : "19.03.5",
    "taints" : [ {
      "key" : "key",
      "value" : "value",
      "effect" : "NoSchedule"
    } ],
    "user_data" : "IyEvdXNyL2Jpbi9iYXNoCmVjaG8gIkhlbGxvIEFDSyEi"
```

`},`

```json
  "nodepool_info" : {
    "name" : "default-nodepool",
    "resource_group_id" : "rg-acfmyvw3wjm****"
```

`},`

```json
  "scaling_group" : {
    "data_disks" : [ {
      "category" : "cloud_ssd",
      "size" : 40,
      "encrypted" : "true",
      "auto_snapshot_policy_id" : "sp-2zej1nogjvovnz4z****"
    } ],
    "instance_charge_type" : "PostPaid",
    "platform" : "AliyunLinux",
    "image_id" : "aliyun_2_1903_x64_20G_alibase_20200904.vhd",
    "instance_types" : [ "ecs.c6.large" ],
    "login_password" : "Hello1234",
    "rds_instances" : [ "rds-xxx" ],
    "scaling_policy" : "release",
    "system_disk_category" : "cloud_efficiency",
    "system_disk_size" : 120,
    "tags" : [ {
      "key" : "env",
      "value" : "prod"
    } ],
    "vswitch_ids" : [ "vsw-wz9uwxhawmtzg7u9h****" ],
```

`},`

```json
  "tee_config" : {
    "tee_enable" : false
```

`},`

```json
  "update_nodes" : true
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <task_id>T-5fd211e924e1d00787000293</task_id> <nodepool_id>np737c3ac1ac684703b9e10673aa2c****</nodepool_id>
```

`JSON` format

```
HTTP/1.1 200 OK
```

`{`

```json
  "task_id" : "T-5fd211e924e1d00787000293",
  "nodepool_id" : "np737c3ac1ac684703b9e10673aa2c****"
```

Error codes You can check further details of error codes. For more information, see Error codes.

##### 3.2.5.4 DescribeClusterNodePools

Queries node pools in a specified Container Service cluster. Request syntax

```
GET /clusters/ClusterId/nodepools HTTP/1.1
```

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClusterId | String | Yes | cc0f87de0b8fb 403f86e10e204f 83**** | The ID of the cluster. |

Response syntax

```
HTTP/1.1 200
```

`{`

```json
  "nodepools" : [ {
    "auto_scaling" : {
      "enable" : Boolean,
      "max_instances" : Long,
      "min_instances" : Long,
      "type" : "String"
```

`},`

```json
    "kubernetes_config" : {
      "cms_enabled" : Boolean,
```

```json
      "cpu_policy" : "String",
      "labels" : [ {
        "key" : "String",
        "value" : "String"
      } ],
      "runtime" : "String",
      "runtime_version" : "String",
      "taints" : [ {
        "key" : "String",
        "value" : "String",
        "effect" : "String"
      } ],
      "user_data" : "String"
```

`},`

```json
    "nodepool_info" : {
      "created" : "String",
      "is_default" : Boolean,
      "name" : "String",
      "nodepool_id" : "String",
      "region_id" : "String",
      "resource_group_id" : "String",
      "type" : "String",
      "updated" : "String"
```

`},`

```json
    "scaling_group" : {
      "data_disks" : [ {
        "category" : "String",
        "size" : Long,
        "encrypted" : "String",
        "auto_snapshot_policy_id" : "String"
      } ],
      "image_id" : "String",
      "instance_charge_type" : "String",
      "instance_types" : [ "String" ],
      "platform" : "String",
      "ram_policy" : "String",
      "rds_instances" : [ "String" ],
      "scaling_group_id" : "String",
      "scaling_policy" : "String",
      "security_group_id" : "String",
      "system_disk_category" : "String",
      "system_disk_size" : Long,
      "tags" : [ {
        "key" : "String",
        "value" : "String"
      } ],
      "vswitch_ids" : [ "String" ],
      "login_password" : "String",
```

`},`

```json
    "status" : {
      "failed_nodes" : Long,
      "healthy_nodes" : Long,
      "initial_nodes" : Long,
      "offline_nodes" : Long,
```

```json
      "removing_nodes" : Long,
      "serving_nodes" : Long,
      "state" : "String",
      "total_nodes" : Long
```

`},`

```json
    "tee_config" : {
      "tee_enable" : Boolean
```

`},`

```
  } ]
```

Response parameters Response body parameters

| Parameter | Type | Example | Description |   |   |
|---|---|---|---|---|---|
| nodepools | Array |   | The list of node pools in the cluster. |   |   |
| auto scaling _ | Object |   | The configuration of auto scaling. |   |   |
| enable | Boolean | true | Indicates whether auto scaling is enabled. Valid values: true : Auto scaling is enabled for the node pool. false : Auto scaling is disabled for the node pool. If you set this parameter to false , the auto scaling parameter _ does not take effect. |   |   |
| max instances _ | Long | 10 | The maximum number of Elastic Compute Service (ECS) instances. |   |   |
| min instances _ | Long | 2 | The minimum number of ECS instances. |   |   |
| type | String | cpu | The type of instances that are specified for auto scaling. Valid values: cpu : regular instance. gpu : GPU-accelerated instance. gpushare : instance that uses shared GPUs. spot : preemptible instance. |   |   |
| kubernetes con _ fig | Object |   | The configuration of the cluster. |   |   |

| D | eveloper Guide·Cl | uster API list |   | Container Service for Kubernete | s |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |   |   |
|---|---|---|---|---|---|
| cms enabled _ | Boolean | true | Indicates whether the CloudMonitor agent is installed on ECS instances. After the CloudMonitor agent is installed on ECS instances, you can view monitoring information about the instances in the CloudMonitor console. We recommend that you install the CloudMonitor agent. Valid values: true : The CloudMonitor agent is installed on ECS instances. false : The CloudMonitor agent is not installed on ECS instances. |   |   |
| cpu policy _ | String | none | The CPU policy. The following policies are supported if the cluster version is 1.12.6 or later. static : This policy allows pods with specific resource characteristics on the node to be granted with enhanced CPU affinity and exclusivity. none : This policy indicates that the default CPU affinity is used. |   |   |
| labels | Array of tag |   | The labels of nodes. You can add labels to the nodes in the cluster. Labeling rules: Each label consists of a case-sensitive key-value pair. You can add up to 20 labels. When you add a label, you must specify a unique key but you can leave the value empty. A key cannot exceed 64 characters in length and a value cannot exceed 128 characters in length. Keys and values cannot start with aliyun , acs: , https:// , or http:// . |   |   |
| runtime | String | docker | The name of the container runtime. |   |   |
| runtime version _ | String | 19.03.5 | The version of the container runtime. |   |   |

|   | aliyun |
|---|---|
| http:// |   |

| ontainer Service fo | r Kubernetes |   | Developer Guide·Cluster API lis |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| taints | Array of taint |   | The taints that are added to nodes. Taints are added to nodes to prevent pods from being scheduled to inappropriate nodes. However, toleration rules allow pods to be scheduled to nodes with matching taints. |
| user data _ | String | IyEvYmluL3NoCmVja G8gIkhlbGxvIEFD**** | The user-defined data of the node pool. For more information, see the User-defined data chapter in the ECS documentation. |
| nodepool info _ | Object |   | The information about the node pool. |
| created | String | 2020-09- 27T19:14:09.156823 496+08:00 | The time when the node pool was created. |
| is default _ | Boolean | true | Indicates whether the node pool is a default node pool. By default, a cluster has only one default node pool. Valid values: true : The node pool is a default node pool. false : The node pool is not a default node pool. |
| name | String | default-nodepool | The name of the node pool. The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). It cannot start with a hyphen. |
| nodepool id _ | String | np615c0e096612421 6a0412e10afe0**** | The ID of the node pool. |
| region id _ | String | cn-beijing | The ID of the region where the node pool is deployed. |
| resource group _ id _ | String | rg- acfmyvw3wjm**** | The ID of the resource group to which the node pool belongs. |
| type | String | ess | The type of node pool. |
| updated | String | 2020-09- 27T20:37:46+08:00 | The time when the node pool was updated. |

| eveloper Guide·Cl | uster API list |   | Container Service for Kubernete |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| scaling group _ | Object |   | The configuration of the scaling group. |
| data disks _ | Array of data disk _ |   | The configurations of the data disks that are mounted to the nodes in the node pool. Each configuration includes disk type and disk size. |
| image id _ | String | aliyun 2 1903 x64 2 _ _ _ _ 0G alibase 2020052 _ _ 9.vhd | The ID of the custom image. You can call the DescribeKubernetesVersionMetadata operation to query the supported images. |
| instance charg _ e type _ | String | PostPaid | The billing method of the nodes in the node pool. Valid values: PrePaid : subscription. PostPaid : pay-as-you-go. |
| instance types _ | Array of String | ecs.n4.large | The instance types of nodes. |
| platform | String | AliyunLinux | The release version of the operating system. Valid values: CentOS AliyunLinux Windows WindowsCore |
| ram policy _ | String | KubernetesWorkerR ole-021dc54f-929b- 437a-8ae0- 34c24d3e**** | The name of the Resource Access Management (RAM) role. The RAM role is assigned to the worker nodes that are created on ECS instances. |
| rds instances _ | Array of String | rm-xxx | The Relational Database Service (RDS) instances. |
| scaling group i _ _ d | String | asg- 2ze8n5qw4atggut8* *** | The ID of the scaling group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| scaling policy _ | String | release | The scaling mode of the scaling group. Valid values: release : the standard mode. Auto scaling is implemented by creating or releasing ECS instances based on the requested resources. recycle : the swift mode. Auto scaling is implemented by creating, stopping, and starting ECS instances. This mode accelerates scaling activities. When an ECS instance is stopped, you are charged only the storage fees. This does not apply to ECS instances that use local disks. |
| security group _ _ id | String | sg- 2ze1iuk12m2sb4c4* *** | The ID of the security group to which the instances of the cluster belong. |
| system disk ca _ _ tegory | String | cloud efficiency _ | The type of system disk that is specified for the nodes in the node pool. Valid values: cloud efficiency : ultra disk. _ cloud ssd : standard SSD. _ |
| system disk si _ _ ze | Long | 120 | The size of the system disk that is specified for the nodes in the node pool. Unit: GiB. Valid values: 20 to 500. |
| tags | Array of tag |   | The labels of ECS instances. You can add labels to only ECS instances. The key of each label must be unique and cannot exceed 128 characters in length. Keys and values cannot start with aliyun, acs:, https://, or http://. |
| vswitch ids _ | Array of String | vsw- 2ze3ds0mdip0hdz8i **** | The IDs of vSwitches. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| login passwor _ d | String | ****** | The Secure Shell (SSH) logon password. The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. For security considerations, the password is encrypted during data transfer. |
| status | Object |   | The status of the node pool. |
| failed nodes _ | Long | 0 | The number of failed nodes. |
| healthy nodes _ | Long | 3 | The number of healthy nodes. |
| initial nodes _ | Long | 0 | The number of nodes that are being created. |
| offline nodes _ | Long | 0 | The number of offline nodes. |
| removing node _ s | Long | 0 | The number of nodes that are being removed. |
| serving nodes _ | Long | 3 | The number of running nodes. |
| state | String | active | The state of the node pool. Valid values: active : The node pool is activated. scaling : The node pool is being scaled. removing : The node pool is removing nodes. deleting : The node pool is being deleted. updating : The node pool is being updated. |
| total nodes _ | Long | 3 | The number of nodes in the node pool. |
| tee config _ | Object |   | The configuration of confidential computing. |

| ontainer Service fo | r Kubernetes |   | Developer Guide·Cluster API lis |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| tee enable _ | Boolean | false | Indicates whether confidential computing is enabled for the cluster. Valid values: true : Confidential computing is enabled for the cluster. false : Confidential computing is disabled for the cluster. |

Examples Sample requests

```
GET /clusters/cc0f87de0b8fb403f86e10e204f83****/nodepools HTTP/1.1
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <nodepools>
    <auto_scaling>
        <enable>true</enable>
        <max_instances>10</max_instances>
        <min_instances>2</min_instances>
        <type>cpu</type>
    </auto_scaling>
    <kubernetes_config>
        <cms_enabled>true</cms_enabled>
        <cpu_policy>none</cpu_policy>
        <labels>
            <key>env</key>
            <value>prod</value>
        </labels>
        <runtime>docker</runtime>
        <runtime_version>19.03.5</runtime_version>
        <taints>
            <key>key</key>
            <value>value</value>
            <effect>NoSchedule</effect>
        </taints>
        <user_data>IyEvYmluL3NoCmVjaG8gIkhlbGxvIEFD****</user_data>
    </kubernetes_config>
    <nodepool_info>
        <created>2020-09-27T19:14:09.156823496+08:00</created>
        <is_default>true</is_default>
        <name>default-nodepool</name>
        <nodepool_id>np615c0e0966124216a0412e10afe0****</nodepool_id>
        <region_id>cn-beijing</region_id>
        <resource_group_id>rg-acfmyvw3wjm****</resource_group_id>
```

```xml
        <type>ess</type>
        <updated>2020-09-27T20:37:46+08:00</updated>
    </nodepool_info>
    <scaling_group>
        <data_disks>
            <category>cloud_ssd</category>
            <size>40</size>
            <encrypted>true</encrypted>
            <auto_snapshot_policy_id>sp-2zej1nogjvovnz4z****</auto_snapshot_policy_id>
        </data_disks>
        <image_id>aliyun_2_1903_x64_20G_alibase_20200529.vhd</image_id>
        <instance_charge_type>PostPaid</instance_charge_type>
        <instance_types>ecs.n4.large</instance_types
        <platform>AliyunLinux</platform>
        <ram_policy>KubernetesWorkerRole-021dc54f-929b-437a-8ae0-34c24d3e****</ram_policy>
        <rds_instances>rm-xxx</rds_instances>
        <scaling_group_id>asg-2ze8n5qw4atggut8****</scaling_group_id>
        <scaling_policy>release</scaling_policy>
        <security_group_id>sg-2ze1iuk12m2sb4c4****</security_group_id>
        <system_disk_category>cloud_efficiency</system_disk_category>
        <system_disk_size>120</system_disk_size>
        <tags>
            <key>env</key>
            <value>prod</value>
        </tags>
        <vswitch_ids>vsw-2ze3ds0mdip0hdz8i****</vswitch_ids>
        <login_password>******</login_password>
    </scaling_group>
    <status>
        <failed_nodes>0</failed_nodes>
        <healthy_nodes>3</healthy_nodes>
        <initial_nodes>0</initial_nodes>
        <offline_nodes>0</offline_nodes>
        <removing_nodes>0</removing_nodes>
        <serving_nodes>3</serving_nodes>
        <state>active</state>
        <total_nodes>3</total_nodes>
    </status>
    <tee_config>
        <tee_enable>false</tee_enable>
    </tee_config>
</nodepools>
```

`JSON` format

```
HTTP/1.1 200 OK
```

`{`

```json
  "nodepools" : [ {
    "auto_scaling" : {
      "enable" : true,
      "max_instances" : 10,
      "min_instances" : 2,
      "type" : "cpu"
```

`yp` `p` `},`

```json
    "kubernetes_config" : {
      "cms_enabled" : true,
      "cpu_policy" : "none",
      "labels" : [ {
        "key" : "env",
        "value" : "prod"
      } ],
      "runtime" : "docker",
      "runtime_version" : "19.03.5",
      "taints" : [ {
        "key" : "key",
        "value" : "value",
        "effect" : "NoSchedule"
      } ],
      "user_data" : "IyEvYmluL3NoCmVjaG8gIkhlbGxvIEFD****"
```

`},`

```json
    "nodepool_info" : {
      "created" : "2020-09-27T19:14:09.156823496+08:00",
      "is_default" : true,
      "name" : "default-nodepool",
      "nodepool_id" : "np615c0e0966124216a0412e10afe0****",
      "region_id" : "cn-beijing",
      "resource_group_id" : "rg-acfmyvw3wjm****",
      "type" : "ess",
      "updated" : "2020-09-27T20:37:46+08:00"
```

`},`

```json
    "scaling_group" : {
      "data_disks" : [ {
        "category" : "cloud_ssd",
        "size" : 40,
        "encrypted" : "true",
        "auto_snapshot_policy_id" : "sp-2zej1nogjvovnz4z****"
      } ],
      "image_id" : "aliyun_2_1903_x64_20G_alibase_20200529.vhd",
      "instance_charge_type" : "PostPaid",
      "instance_types" : [ "ecs.n4.large" ],
      "platform" : "AliyunLinux",
      "ram_policy" : "KubernetesWorkerRole-021dc54f-929b-437a-8ae0-34c24d3e****",
      "rds_instances" : [ "rm-xxx" ],
      "scaling_group_id" : "asg-2ze8n5qw4atggut8****",
      "scaling_policy" : "release",
      "security_group_id" : "sg-2ze1iuk12m2sb4c4****",
      "system_disk_category" : "cloud_efficiency",
      "system_disk_size" : 120,
      "tags" : [ {
        "key" : "env",
        "value" : "prod"
      } ],
      "vswitch_ids" : [ "vsw-2ze3ds0mdip0hdz8i****" ],
      "login_password" : "******",
```

`},`

```json
    "status" : {
      "failed_nodes" : 0,
```

```json
      "healthy_nodes" : 3,
      "initial_nodes" : 0,
      "offline_nodes" : 0,
      "removing_nodes" : 0,
      "serving_nodes" : 3,
      "state" : "active",
      "total_nodes" : 3
```

`},`

```json
    "tee_config" : {
      "tee_enable" : false
```

`},`

```
  } ]
```

Error codes You can check further details of error codes. For more information, see Error codes.

##### 3.2.5.5 DescribeClusterNodePoolDetail

Queries the details of a specified node pool. Request syntax

```
GET /clusters/ClusterId/nodepools/NodepoolId HTTP/1.1
```

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClusterId | String | Yes | c23421cfa74454 bc8b37163fd19 af**** | The ID of the cluster to which the node pool belongs. |
| NodepoolId | String | Yes | np31da1b38983 f4511b490fc621 08a**** | The ID of the node pool. |

Response syntax

```
HTTP/1.1 200
```

`{`

```json
  "auto_scaling" : {
    "enable" : Boolean,
    "max_instances" : Long,
    "min_instances" : Long,
    "type" : "String"
```

`},`

```json
  "kubernetes_config" : {
    "cms_enabled" : Boolean,
    "cpu_policy" : "String",
    "labels" : [ {
      "key" : "String",
      "value" : "String"
    } ],
    "runtime" : "String",
    "runtime_version" : "String",
    "taints" : [ {
      "key" : "String",
      "value" : "String",
      "effect" : "String"
    } ],
    "user_data" : "String"
```

`},`

```json
  "nodepool_info" : {
    "created" : "String",
    "is_default" : Boolean,
    "name" : "String",
    "nodepool_id" : "String",
    "region_id" : "String",
    "resource_group_id" : "String",
    "type" : "String",
    "updated" : "String"
```

`},`

```json
  "scaling_group" : {
    "data_disks" : [ {
      "category" : "String",
      "size" : Long,
      "encrypted" : "String",
      "auto_snapshot_policy_id" : "String"
    } ],
    "image_id" : "String",
    "instance_charge_type" : "String",
    "instance_types" : [ "String" ],
    "platform" : "String",
    "ram_policy" : "String",
    "rds_instances" : [ "String" ],
    "scaling_group_id" : "String",
    "scaling_policy" : "String",
    "security_group_id" : "String",
    "system_disk_category" : "String",
    "system_disk_size" : Long,
    "tags" : [ {
      "key" : "String",
      "value" : "String"
    } ],
    "vswitch_ids" : [ "String" ],
    "login_password" : "String",
```

`},`

```json
  "status" : {
    "failed_nodes" : Long,
    "healthy_nodes" : Long,
"iiil
```

`d` `"`

```json
    "initial_nodes" : Long,
    "offline_nodes" : Long,
    "removing_nodes" : Long,
    "serving_nodes" : Long,
    "state" : "String",
    "total_nodes" : Long
```

`},`

```json
  "tee_config" : {
    "tee_enable" : Boolean
```

`},` Response parameters Response body parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| auto scaling _ | Object |   | The configuration of auto scaling. |
| enable | Boolean | true | Indicates whether auto scaling is enabled for the node pool. true : Auto scaling is enabled for the node pool. false : Auto scaling is disabled for the node pool. If you set this parameter to false, the auto scaling parameter _ does not take effect. |
| max instances _ | Long | 10 | The maximum number of Elastic Compute Service (ECS) instances. |
| min instances _ | Long | 1 | The minimum number of ECS instances. |
| type | String | cpu | The type of instances that are specified for auto scaling. Valid values: cpu : regular instance. gpu : GPU-accelerated instance. gpushare : instance that uses shared GPUs. spot : preemptible instance. |
| kubernetes con _ fig | Object |   | The configuration of the cluster. |

| Parameter | Type | Example | Description |   |   |
|---|---|---|---|---|---|
| cms enabled _ | Boolean | true | Indicates whether the CloudMonitor agent is installed on ECS instances. After the CloudMonitor agent is installed on ECS instances, you can view monitoring information about the instances in the CloudMonitor console. We recommend that you install the CloudMonitor agent. Valid values: true : The CloudMonitor agent is installed on ECS instances. false : The CloudMonitor agent is not installed on ECS instances. |   |   |
| cpu policy _ | String | none | The CPU policy. The following policies are supported if the cluster version is 1.12.6 or later. static : This policy allows pods with specific resource characteristics on the node to be granted with enhanced CPU affinity and exclusivity. none : This policy indicates that the default CPU affinity is used. |   |   |
| labels | Array of tag |   | The labels of nodes. You can add labels to the nodes in the cluster. Labeling rules: Each label consists of a case-sensitive key-value pair. You can add up to 20 labels. When you add a label, you must specify a unique key but you can leave the value empty. A key cannot exceed 64 characters in length and a value cannot exceed 128 characters in length. Keys and values cannot start with aliyun , acs: , https:// , or http:// . |   |   |
| runtime | String | docker | The name of the container runtime. |   |   |
| runtime version _ | String | 19.03.5 | The version of the container runtime. |   |   |

|   | aliyun |
|---|---|
| http:// |   |

| Parameter | Type | Example | Description |
|---|---|---|---|
| taints | Array of taint |   | The taints that are added to nodes. Taints are added to nodes to prevent pods from being scheduled to inappropriate nodes. However, toleration rules allow pods to be scheduled to nodes with matching taints. For more information, see taint-and- toleration. |
| user data _ | String | IyEvYmluL3NoCmVja G8gIkhlbGxvIEFDSyEi | The user-defined data of the node pool. For more information, see the User-defined data chapter in the ECS documentation. |
| nodepool info _ | Object |   | The configuration of the node pool. |
| created | String | 2020-09- 27T19:14:09.156823 496+08:00 | The time when the node pool was created. |
| is default _ | Boolean | true | Indicates whether the node pool is a default node pool. By default, a cluster has only one default node pool. Valid values: true : The node pool is a default node pool. false : The node pool is not a default node pool. |
| name | String | default-nodepool | The name of the node pool. The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). It cannot start with a hyphen. |
| nodepool id _ | String | np615c0e096612421 6a0412e10afe0**** | The ID of the node pool. |
| region id _ | String | cn-beijing | The ID of the region where the node pool is deployed. |
| resource group _ id _ | String | rg- acfmyvw3wjmb**** | The ID of the resource group to which the node pool belongs. |
| type | String | ess | The type of node pool. |

| ontainer Service fo | r Kubernetes |   | Developer Guide·Cluster API lis |
|---|---|---|---|
| Parameter | Type | Example | Description |
| updated | String | 2020-09- 27T20:37:46+08:00 | The time when the node pool was updated. |
| scaling group _ | Object |   | The configuration of the scaling group. |
| data disks _ | Array of data disk _ |   | The configurations of the data disks that are mounted to the nodes in the node pool. Each configuration includes disk type and disk size. |
| image id _ | String | aliyun 2 1903 x64 2 _ _ _ _ 0G alibase 2020052 _ _ 9.vhd | The ID of the custom image. You can call the DescribeKubernetesVersionMetadata operation to query the supported images. |
| instance types _ | Array of String | ecs.n4.large | The instance types of nodes. |
| platform | String | AliyunLinux | The release version of the operating system. Valid values: CentOS AliyunLinux Windows WindowsCore |
| ram policy _ | String | KubernetesWorkerR ole-021dc54f-929b- 437a-8ae0- 34c24d3e**** | The name of the Resource Access Management (RAM) role. The RAM role is assigned to the worker nodes that are created on ECS instances. |
| rds instances _ | Array of String | rm-xxx | The Relational Database Service (RDS) instances. |
| scaling group i _ _ d | String | asg- 2zeieod8giqmov7z* *** | The ID of the scaling group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| scaling policy _ | String | release | The scaling mode of the scaling group. Valid values: release : the standard mode. Auto scaling is implemented by creating or releasing ECS instances based on the requested resources. release : the swift mode. Auto scaling is implemented by creating, stopping, and starting ECS instances. This mode accelerates scaling activities. When an ECS instance is stopped, you are charged only the storage fees. This does not apply to ECS instances that use local disks. |
| security group _ _ id | String | sg- 2ze60ockeekspl3d** ** | The ID of the security group to which the instances of the cluster belong. |
| system disk ca _ _ tegory | String | cloud efficiency _ | The type of system disk that is specified for the nodes in the node pool. Valid values: cloud efficiency : ultra disk. _ cloud ssd : standard SSD. _ |
| system disk si _ _ ze | Long | 120 | The size of the system disk that is specified for the nodes in the node pool. Unit: GiB. Valid values: 20 to 500. |
| tags | Array of tag |   | The labels of ECS instances. You can add labels to only ECS instances. The key of each label must be unique and cannot exceed 128 characters in length. Keys and values cannot start with aliyun , acs: , https:// , or http:// . |
| vswitch ids _ | Array of String | vsw- 2ze3ds0mdip0hdz8i **** | The IDs of vSwitches. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| login passwor _ d | String | ******** | The Secure Shell (SSH) logon password. The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. For security considerations, the password is encrypted during data transfer. |
| status | Object |   | The status of the node pool. |
| failed nodes _ | Long | 0 | The number of failed nodes. |
| healthy nodes _ | Long | 3 | The number of healthy nodes. |
| initial nodes _ | Long | 0 | The number of nodes that are being created. |
| offline nodes _ | Long | 0 | The number of offline nodes. |
| removing node _ s | Long | 0 | The number of nodes that are being removed. |
| serving nodes _ | Long | 3 | The number of running nodes. |
| state | String | active | The state of the node pool. Valid values: active : The node pool is activated. scaling : The node pool is being scaled. removing : The node pool is removing nodes. deleting : The node pool is being deleted. updating : The node pool is being updated. |
| total nodes _ | Long | 3 | The total number of nodes in the node pool. |
| tee config _ | Object |   | The configuration of confidential computing. |

| Developer Guide·Cl | uster API list |   | Container Service for Kubernete |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| tee enable _ | Boolean | false | Indicates whether confidential computing is enabled for the cluster. true : Confidential computing is enabled for the cluster. false : Confidential computing is disabled for the cluster. |

Examples Sample requests

```
GET /clusters/c23421cfa74454bc8b37163fd19af****/nodepools/np31da1b38983f4511b490fc62108a***
* HTTP/1.1
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <auto_scaling>
    <enable>true</enable>
    <max_instances>10</max_instances>
    <min_instances>1</min_instances>
    <type>cpu</type>
</auto_scaling> <kubernetes_config>
    <cms_enabled>true</cms_enabled>
    <cpu_policy>none</cpu_policy>
    <labels>
        <key>env</key>
        <value>prod</value>
    </labels>
    <runtime>docker</runtime>
    <runtime_version>19.03.5</runtime_version>
    <taints>
        <key>key</key>
        <value>value</value>
        <effect>NoSchedule</effect>
    </taints>
    <user_data>IyEvYmluL3NoCmVjaG8gIkhlbGxvIEFDSyEi</user_data>
</kubernetes_config> <nodepool_info>
    <created>2020-09-27T19:14:09.156823496+08:00</created>
    <is_default>true</is_default>
    <name>default-nodepool</name>
    <nodepool_id>np615c0e0966124216a0412e10afe0****</nodepool_id>
    <region_id>cn-beijing</region_id>
    <resource_group_id>rg-acfmyvw3wjmb****</resource_group_id>
```

```xml
    <type>ess</type>
    <updated>2020-09-27T20:37:46+08:00</updated>
</nodepool_info> <scaling_group>
    <data_disks>
        <category>cloud_ssd</category>
        <size>40</size>
        <encrypted>true</encrypted>
        <auto_snapshot_policy_id>sp-2zej1nogjvovnz4z****</auto_snapshot_policy_id>
    </data_disks>
    <image_id>aliyun_2_1903_x64_20G_alibase_20200529.vhd</image_id>
    <instance_charge_type>PostPaid</instance_charge_type>
    <instance_types>ecs.n4.large</instance_types>
    <platform>AliyunLinux</platform>
    <ram_policy>KubernetesWorkerRole-021dc54f-929b-437a-8ae0-34c24d3e****</ram_policy>
    <rds_instances>rm-xxx</rds_instances>
    <scaling_group_id>asg-2zeieod8giqmov7z****</scaling_group_id>
    <scaling_policy>release</scaling_policy>
    <security_group_id>sg-2ze60ockeekspl3d****</security_group_id>
    <system_disk_category>cloud_efficiency</system_disk_category>
    <system_disk_size>120</system_disk_size>
    <tags>
        <key>env</key>
        <value>prod</value>
    </tags>
    <vswitch_ids>vsw-2ze3ds0mdip0hdz8i****</vswitch_ids>
    <login_password>********</login_password>
</scaling_group> <status>
    <failed_nodes>0</failed_nodes>
    <healthy_nodes>3</healthy_nodes>
    <initial_nodes>0</initial_nodes>
    <offline_nodes>0</offline_nodes>
    <removing_nodes>0</removing_nodes>
    <serving_nodes>3</serving_nodes>
    <state>active</state>
    <total_nodes>3</total_nodes>
</status> <tee_config>
    <tee_enable>false</tee_enable>
</tee_config>
```

`JSON` format

```
HTTP/1.1 200 OK
```

`{`

```json
  "auto_scaling" : {
    "enable" : true,
    "max_instances" : 10,
    "min_instances" : 1,
    "type" : "cpu"
```

`},`

```json
  "kubernetesconfig" : {
```

`_` `g`

```json
    "cms_enabled" : true,
    "cpu_policy" : "none",
    "labels" : [ {
      "key" : "env",
      "value" : "prod"
    } ],
    "runtime" : "docker",
    "runtime_version" : "19.03.5",
    "taints" : [ {
      "key" : "key",
      "value" : "value",
      "effect" : "NoSchedule"
    } ],
    "user_data" : "IyEvYmluL3NoCmVjaG8gIkhlbGxvIEFDSyEi"
```

`},`

```json
  "nodepool_info" : {
    "created" : "2020-09-27T19:14:09.156823496+08:00",
    "is_default" : true,
    "name" : "default-nodepool",
    "nodepool_id" : "np615c0e0966124216a0412e10afe0****",
    "region_id" : "cn-beijing",
    "resource_group_id" : "rg-acfmyvw3wjmb****",
    "type" : "ess",
    "updated" : "2020-09-27T20:37:46+08:00"
```

`},`

```json
  "scaling_group" : {
    "data_disks" : [ {
      "category" : "cloud_ssd",
      "size" : 40,
      "encrypted" : "true",
      "auto_snapshot_policy_id" : "sp-2zej1nogjvovnz4z****"
    } ],
    "image_id" : "aliyun_2_1903_x64_20G_alibase_20200529.vhd",
    "instance_charge_type" : "PostPaid",
    "instance_types" : [ "ecs.n4.large" ],
    "platform" : "AliyunLinux",
    "ram_policy" : "KubernetesWorkerRole-021dc54f-929b-437a-8ae0-34c24d3e****",
    "rds_instances" : [ "rm-xxx" ],
    "scaling_group_id" : "asg-2zeieod8giqmov7z****",
    "scaling_policy" : "release",
    "security_group_id" : "sg-2ze60ockeekspl3d****",
    "system_disk_category" : "cloud_efficiency",
    "system_disk_size" : 120,
    "tags" : [ {
      "key" : "env",
      "value" : "prod"
    } ],
    "vswitch_ids" : [ "vsw-2ze3ds0mdip0hdz8i****" ],
    "login_password" : "********",
```

`},`

```json
  "status" : {
    "failed_nodes" : 0,
    "healthy_nodes" : 3,
    "initial_nodes" : 0,
```

```json
    "offline_nodes" : 0,
    "removing_nodes" : 0,
    "serving_nodes" : 3,
    "state" : "active",
    "total_nodes" : 3
```

`},`

```json
  "tee_config" : {
    "tee_enable" : false
```

`},` Error codes You can check further details of error codes. For more information, see Error codes.

##### 3.2.5.6 DeleteClusterNodepool

Deletes a node pool. Request syntax

```
DELETE /clusters/ClusterId/nodepools/NodepoolId HTTP/1.1
```

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClusterId | String | Yes | c61da77e8bfbc 4c4c999af2b51 b65**** | The ID of the cluster. |
| NodepoolId | String | Yes | np30db56bcac7 843dca90b999c 8928**** | The ID of the node pool. |

Response syntax

```
HTTP/1.1 200 OK
```

Response parameters No response parameters. Examples Sample requests

```
DELETE /clusters/c61da77e8bfbc4c4c999af2b51b65****/nodepools/np30db56bcac7843dca90b999c8928
**** HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK
```

Error codes You can check further details of error codes. For more information, see Error codes.

### 3.3 Templates

#### 3.3.1 CreateTemplate

Creates an orchestration template. Request syntax

```
POST /templates HTTP/1.1
```

`{`

```json
  "name" : "String",
  "template" : "String",
  "tags" : "String",
  "description" : "String",
  "template_type" : "String"
```

Request parameters Request body parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| name | String | Yes | service- account- template | The name of the template. The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). It cannot start with a hyphen. |

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| template | String | Yes | apiVersion: v1\nkind: ServiceAccount\ nmetadata:\n name: test-sa | The template content in the YAML format. |   |   |
| tags | String | No | test | The label of the template. |   |   |
| description | String | No | this is test | The description of the template. |   |   |
| template type _ | String | No | kubernetes | The type of template. You can set the parameter to a custom value. If you set the parameter to kub ernetes , the template is displayed on the Templates page in the Container Service console. If you set the parameter to com pose , the template is not displayed in the console. We recommend that you set the parameter to kubernetes . Default value: compose . |   |   |
|   |   |   |   |   | kub |   |

|   | ernetes |
|---|---|

| com |   |
|---|---|

|   | pose |
|---|---|

Response syntax

```
HTTP/1.1 200
```

`{`

```json
  "template_id" : "String"
```

Response parameters Response body parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| template id _ | String | ba1fe77b-b01e- 4640-b77e- 8f1b80e3e3cf | The ID of the template. |

Examples Sample requests

```
POST /templates HTTP/1.1
```

`{`

```json
  "name" : "service-account-template",
  "template" : "apiVersion: v1\\nkind: ServiceAccount\\nmetadata:\\n  name: test-sa",
  "tags" : "test",
  "description" : "this is test",
  "template_type" : "kubernetes"
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <template_id>ba1fe77b-b01e-4640-b77e-8f1b80e3e3cf</template_id>
```

`JSON` format

```
HTTP/1.1 200 OK
```

`{`

```json
  "template_id" : "ba1fe77b-b01e-4640-b77e-8f1b80e3e3cf"
```

Error codes You can check further details of error codes. For more information, see Error codes.

#### 3.3.2 DeleteTemplate

Deletes an orchestration template. Request syntax

```
DELETE /templates/TemplateId HTTP/1.1
```

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TemplateId | String | Yes | 20663627-81ee- 4cfe-9b69- c96fcb84a674 | The ID of the template. |

Response syntax

```
HTTP/1.1 200 OK
```

Response parameters No response parameters. Examples Sample requests

```
DELETE /templates/20663627-81ee-4cfe-9b69-c96fcb84a674
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK
```

Error codes You can check further details of error codes. For more information, see Error codes.

#### 3.3.3 DescribeTemplates

Queries all orchestration templates. Request syntax

```
GET /templates?template_type=String&page_num=Long&page_size=Long HTTP/1.1
```

Request parameters Request query parameters

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| template type _ | String | Yes | kubernetes | The type of template. You can set this parameter to a custom value. If you set the parameter to kub ernetes , the template is displayed on the Templates page in the Container Service console. If you set the parameter to com pose , the template is not displayed on the Templates page in the console. Default value: kubernetes . |   |   |
|   |   |   |   |   | kub |   |

|   | ernetes |
|---|---|

| com |   |
|---|---|

|   | pose |
|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| page num _ | Long | No | 1 | The number of the page to return. Default value: 1. |
| page size _ | Long | No | 10 | The number of entries to return on each page. Default value: 10. |

Response syntax

```
HTTP/1.1 200
```

`{`

```json
  "templates" : [ {
    "acl" : "String",
    "id" : "String",
    "name" : "String",
    "description" : "String",
    "tags" : "String",
    "template" : "String",
    "template_type" : "String",
    "created" : "String",
    "updated" : "String",
    "template_with_hist_id" : "String"
  } ],
  "page_info" : {
    "page_number" : Long,
    "page_size" : Long,
    "total_count" : Long
```

Response parameters Response body parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| templates | Array of template |   | The list of returned templates. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| acl | String | private | The access control policy of the template. Valid values: private : The template is private. public : The template is public. shared : The template can be shared. Default value: private . |
| id | String | 874ec485-e7e6- 4373-8a3b- 47bde8ae789f | The ID of the template. |
| name | String | webserver | The name of the template. |
| description | String | a web server | The description of the template. |
| tags | String | kubernetes | The label of the template. By default, the value is the name of the template. |
| template | String | apiVersion: apps/v1\nkind: Deployment\nmeta data:\n name: nginx-deployment- basic\n labels:\n app: nginx\nspec:\n replicas: 2\n selector:\n matchLabels:\n app: nginx\n template:\n metadata:\n labels:\n app: nginx\n spec:\n containers:\n - name: nginx\n image: busybox:latest\n ports:\n - containerPort: 80 | The template content in the YAML format. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| template type _ | String | kubernetes | The type of template. You can set this parameter to a custom value. If you set the parameter to kubernetes , the template is displayed on the Templates page in the Container Service console. If you set the parameter to compose , the template is displayed on the Container Service - Swarm page in the console. However, Container Service for Swarm is deprecated. |
| created | String | 2020-06- 10T16:30:16+08:00 | The time when the template was created. |
| updated | String | 2020-06- 10T16:30:16+08:00 | The time when the template was updated. |
| template with _ _ hist id _ | String | ad81d115-7c8b- 47e7-a222- 9c28d7f6e588 | The ID of the parent template. The value of template with hist id is the same for _ _ _ each template version. This allows you to manage different template versions. |
| page info _ | Object |   | The pagination details. |
| page number _ | Long | 20 | The page number of the returned page. |
| page size _ | Long | 3 | The maximum number of entries returned per page. |
| total count _ | Long | 50 | The total number of entries returned. |

Examples Sample requests

```
GET /templates?template_type=kubernetes&page_num=1&page_size=10 HTTP/1.1
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <templates>
    <acl>private</acl>
    <id>874ec485-e7e6-4373-8a3b-47bde8ae789f</id>
    <name>webserver</name>
    <description>a web server</description>
    <tags>kubernetes</tags>
    <template>apiVersion: apps/v1\nkind: Deployment\nmetadata:\n  name: nginx-deployment-ba
sic\n labels:\n app: nginx\nspec:\n replicas: 2\n selector:\n matchLabels:\n app: nginx\n template:\n metadata:\n labels:\n app: nginx\n spec:\n containers:\n - name: nginx\n image: busybox:latest\n ports:\n containerPort: 80</template>
    <template_type>kubernetes</template_type>
    <created>2020-06-10T16:30:16+08:00</created>
    <updated>2020-06-10T16:30:16+08:00</updated>
    <template_with_hist_id>ad81d115-7c8b-47e7-a222-9c28d7f6e588</template_with_hist_id>
</templates> <page_info>
    <page_number>20</page_number>
    <page_size>3</page_size>
    <total_count>50</total_count>
</page_info>
```

`JSON` format

```
HTTP/1.1 200 OK
```

`{`

```json
  "templates" : [ {
    "acl" : "private",
    "id" : "874ec485-e7e6-4373-8a3b-47bde8ae789f",
    "name" : "webserver",
    "description" : "a web server",
    "tags" : "kubernetes",
    "template" : "apiVersion: apps/v1\\nkind: Deployment\\nmetadata:\\n  name: nginx-deploy
ment-basic\\n labels:\\n app: nginx\\nspec:\\n replicas: 2\\n selector:\\n matchLa bels:\\n app: nginx\\n template:\\n metadata:\\n labels:\\n app: nginx \\n spec:\\n containers:\\n - name: nginx\\n image: busybox:latest\\n ports:\\n - containerPort: 80",
    "template_type" : "kubernetes",
    "created" : "2020-06-10T16:30:16+08:00",
    "updated" : "2020-06-10T16:30:16+08:00",
    "template_with_hist_id" : "ad81d115-7c8b-47e7-a222-9c28d7f6e588"
  } ],
  "page_info" : {
    "page_number" : 20,
    "page_size" : 3,
    "total_count" : 50
```

Error codes You can check further details of error codes. For more information, see Error codes.

#### 3.3.4 DescribeTemplateAttribute

Queries the details of a specified orchestration template. Request syntax

```
GET /templates/TemplateId?template_type=String HTTP/1.1
```

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TemplateId | String | Yes | 874ec485-e7e6- 4373-8a3b- 47bde8a**** | The ID of the template. |

Request query parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| template type _ | String | No | kubernetes | The type of template. The value can be a custom value. If the value is kubernetes , the template is displayed on the Templates page in the Container Service console. If the value is compose , the template is displayed on the Container Service - Swarm page in the console. However, Container Service for Swarm is deprecated. If the value of the parameter is not kubernetes , the template is not displayed on the Templates page in the console. We recommend that you set the parameter to kubernetes . Default value: kubernetes . |

Response syntax

```json
HTTP/1.1 200 [ {
  "id" : "String",
  "acl" : "String",
  "name" : "String",
  "template" : "String",
  "template_type" : "String",
  "description" : "String",
  "tags" : "String",
  "template_with_hist_id" : "String",
  "created" : "String",
  "updated" : "String"
} ]
```

Response parameters Response body parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
|   | Array of template info _ |   | The details of the queried template. |
| id | String | 72d20cf8-a533- 4ea9-a10d- e7630d3d**** | The ID of the template. When you update a template, a new template ID is generated. |
| acl | String | private | The access control policy of the template. |
| name | String | web | The name of the template. |
| template | String | apiVersion: V1\n*** | The template content in the YAML format. |

| Parameter | Type | Example | Description |   |   |
|---|---|---|---|---|---|
| template type _ | String | kubernetes | The type of template. The value can be a custom value. If the value is kubernetes , the template is displayed on the Templates page in the Container Service console. If the value is compose , the template is displayed on the Container Service - Swarm page in the console. However, Container Service for Swarm is deprecated. If the value of the parameter is not kube rnetes , the template is not displayed on the Templates page in the console. We recommend that you set the parameter to kubernetes . Default value: kubernetes . |   |   |
|   |   |   |   | kube |   |
| description | String | test template | The description of the template. |   |   |
| tags | String | sa | The label of the template. |   |   |
| template with _ _ hist id _ | String | 874ec485-e7e6- 4373-8a3b- 47bde8ae**** | The unique ID of the template. The value remains unchanged after the template is updated. |   |   |
| created | String | 2020-09- 16T19:21:29+08:00 | The time when the template was created. |   |   |
| updated | String | 2020-09- 16T19:21:29+08:00 | The time when the template was updated. |   |   |

|   | rnetes |
|---|---|

Examples Sample requests

```
GET /templates/874ec485-e7e6-4373-8a3b-47bde8a****?template_type=kubernetes HTTP/1.1
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <0>
    <id>72d20cf8-a533-4ea9-a10d-e7630d3d****</id>
    <acl>private</acl>
    <name>web</name>
    <template>apiVersion: V1\n***</template>
    <template_type>kubernetes</template_type>
    <description>test template</description>
    <tags>sa</tags>
    <template_with_hist_id>874ec485-e7e6-4373-8a3b-47bde8ae****</template_with_hist_id>
    <created>2020-09-16T19:21:29+08:00</created>
    <updated>2020-09-16T19:21:29+08:00</updated>
</0>
```

`JSON` format

```json
HTTP/1.1 200 OK [ {
  "id" : "72d20cf8-a533-4ea9-a10d-e7630d3d****",
  "acl" : "private",
  "name" : "web",
  "template" : "apiVersion: V1\\n***",
  "template_type" : "kubernetes",
  "description" : "test template",
  "tags" : "sa",
  "template_with_hist_id" : "874ec485-e7e6-4373-8a3b-47bde8ae****",
  "created" : "2020-09-16T19:21:29+08:00",
  "updated" : "2020-09-16T19:21:29+08:00"
} ]
```

Error codes You can check further details of error codes. For more information, see Error codes.

#### 3.3.5 UpdateTemplate

Updates an orchestration template. Request syntax

```
PUT /templates/TemplateId HTTP/1.1
```

`{`

```json
  "description" : "String",
  "name" : "String",
  "tags" : "String",
  "template" : "String",
  "template_type" : "String"
```

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TemplateId | String | Yes | 72d20cf8-a533- 4ea9-a10d- e7630d3d2708 | The ID of the template. |

Request body parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| description | String | No | web server cluster | The description of the template. |
| name | String | No | webserver01 | The name of the template. |
| tags | String | No | web | The label of the template. |
| template | String | No | apiVersion: apps/v1\\nkind : Deployment\\n metadata:\\n name: nginx- deployment- basic\\n labels:\\n app: nginx\\nspec:\\ n replicas: 2\\n selector:\\n matchLabels:\\ n app: nginx\\n template:\\n metadata:\\n labels:\\n app: nginx\\n spec:\\n containers:\\n - name: nginx\\n image: busybox:latest\ \n ports:\\n - containerPort: 8080 | The template content in the YAML format. |

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| template type _ | String | No | kubernetes | The type of template. You can set this parameter to a custom value. If you set the parameter to kub ernetes , the template is displayed on the Templates page in the Container Service console. If you set the parameter to com pose , the template is displayed on the Container Service - Swarm page in the console. However, Container Service for Swarm is deprecated. |   |   |
|   |   |   |   |   | kub |   |

|   | ernetes |
|---|---|

| com |   |
|---|---|

|   | pose |
|---|---|

Response syntax

```
HTTP/1.1 200 OK
```

Response parameters No response parameters. Examples Sample requests

```
PUT /templates/72d20cf8-a533-4ea9-a10d-e7630d3d2708 HTTP/1.1
```

`{`

```json
  "description" : "web server cluster",
  "name" : "webserver01",
  "tags" : "web",
  "template" : "apiVersion: apps/v1\\\\nkind: Deployment\\\\nmetadata:\\\\n  name: nginx-de
ployment-basic\\\\n labels:\\\\n app: nginx\\\\nspec:\\\\n replicas: 2\\\\n selector: \\\\n matchLabels:\\\\n app: nginx\\\\n template:\\\\n metadata:\\\\n labe ls:\\\\n app: nginx\\\\n spec:\\\\n containers:\\\\n - name: nginx\\\\n image: busybox:latest\\\\n ports:\\\\n - containerPort: 8080",
  "template_type" : "kubernetes"
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK
```

Error codes You can check further details of error codes. For more information, see Error codes.

### 3.4 Add-ons

#### 3.4.1 InstallClusterAddons

Installs a component in a specified Container Service cluster. Request syntax

```json
POST /clusters/ClusterId/components/install HTTP/1.1 [ {
  "name" : "String",
  "version" : "String",
  "config" : "String"
} ]
```

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClusterId | String | Yes | c82e6987e2961 451182edacd74 faf**** | The ID of the cluster. |

Request body parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
|   | Array | No |   | The request body parameters. |
| name | String | Yes | ags-metrics- collector | The name of the component that you want to install. |
| version | String | Yes | v1.0.0.2- cc3b2d6-aliyun | The version of the component. Not e You can call the DescribeClusterAddonsVersion operation to query the version of the component. For more information, see DescribeClusterAddonsVersion. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| config | String | No | {\"IngressDashb oardEnabled\": \"true\",\"sls p _ roject name\":\ _ "your sls projec _ _ t name\"}"} _ | The configuration of the component. |

Response syntax

```
HTTP/1.1 200 OK
```

Response parameters No response parameters. Examples Sample requests

```json
POST /clusters/c82e6987e2961451182edacd74faf****/components/install HTTP/1.1 [ {
  "name" : "ags-metrics-collector",
  "version" : "v1.0.0.2-cc3b2d6-aliyun",
  "config" : "{\\\"IngressDashboardEnabled\\\":\\\"true\\\",\\\"sls_project_name\\\":\\\"yo
ur_sls_project_name\\\"}\"}" } ]
```

Description of the sample request

```
POST /clusters/c3fb96524f9274b4495df0f12a6b5****/components/install?RegionId=cn-hangzhou -header "Content-Type=application/json;" --body '[{"name":"ack-node-problem-detector"}]'
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK
```

Error codes You can check further details of error codes. For more information, see Error codes.

#### 3.4.2 DescribeAddons

Queries the details of the components that are installed in a specified Container Service cluster. Request syntax

```
GET /clusters/components/metadata?region=String&cluster_type=String HTTP/1.1
```

Request parameters Request query parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| region | String | Yes | cn-beijing | The ID of the region where the cluster is deployed. |
| cluster type _ | String | No | Kubernetes | The type of cluster. Valid values: Kubernetes : dedicated Kubernetes cluster. ManagedKubernetes : managed edge Kubernetes cluster. |

Response syntax

```
HTTP/1.1 200
```

`{`

```json
  "ComponentGroups" : [ {
    "group_name" : "String",
    "items" : [ {
      "name" : "String"
    } ]
  } ],
  "StandardComponents" : {
    "key" : {
      "name" : "String",
      "version" : "String",
      "description" : "String",
      "required" : "String",
      "disabled" : Boolean
```

Response parameters Response body parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ComponentGro ups | Array of ComponentGro up |   | The list of the returned components. |
| group name _ | String | storage | The name of the component group. |
| items | Array of item |   | The names of the components in the component group. |
| name | String | flexvolume | The name of the component. |
| StandardComp onents | Map |   | Standard components. |
|   | object |   | The details of the standard components. |
| name | String | ack-arena | The name of the component. |
| version | String | 0.5.0 | The version of the component. |
| description | String | test | The description of the component. |
| required | String | false | Indicates whether the component is required in a Container Service cluster. Valid values: true : The component is required and must be installed when a cluster is created. false : The component is optional. After a cluster is created, you can go to the Add-ons page to install the component. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| disabled | Boolean | false | Indicates whether the automatic installation of the component is disabled. By default, some optional components, such as components for logging and Ingresses, are installed when a cluster is created. You can set this parameter to disable the automatic installation of a component. Valid values: true : disables the automatic installation of the component. false : allows the automatic installation of the component. |

Examples Sample requests

```
GET /clusters/components/metadata?region=cn-beijing &cluster_type=kubernetes HTTP/1.1
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <StandardComponents>
    <cloud-controller-manager>
        <name>cloud-controller-manager</name>
        <version>v1.9.3.339-g9830b58-aliyun</version>
        <disabled>false</disabled>
        <required>true</required>
        <description>name: Cloud Controller Manager introduction: Using Cloud Controller Ma
nager to create load balancers for k8s applications and manage node route entries doc:en: h ttps://www.alibabacloud.com/help/doc-detail/94925.htm</description>
    </cloud-controller-manager>
    <csi-plugin>
        <name>csi-plugin</name>
        <version>v1.16.9.43-f36bb540-aliyun</version>
        <disabled>false</disabled>
        <required>false</required>
        <description>csi-plugin</description>
    </csi-plugin>
</StandardComponents> <ComponentGroups>
    <group_name>storage</group_name>
    <items>
        <name>flexvolume</name>
    </items>
    <items>
        <name>alicloud-disk-controller</name>
</items>
```

```xml
    </items>
    <items>
        <name>csi-plugin</name>
    </items>
    <items>
        <name>csi-provisioner</name>
    </items>
</ComponentGroups> <ComponentGroups>
    <group_name>network</group_name>
    <items>
        <name>kube-flannel-ds</name>
    </items>
    <items>
        <name>terway</name>
    </items>
    <items>
        <name>terway-eni</name>
    </items>
    <items>
        <name>terway-eniip</name>
    </items>
    <items>
        <name>nginx-ingress-controller</name>
    </items>
    <items>
        <name>coredns</name>
    </items>
    <items>
        <name>managed-kube-proxy</name>
    </items>
</ComponentGroups>
```

`JSON` format

```
HTTP/1.1 200 OK
```

`{`

```json
  "StandardComponents" : {
    "cloud-controller-manager" : {
      "name" : "cloud-controller-manager",
      "version" : "v1.9.3.339-g9830b58-aliyun",
      "disabled" : false,
      "required" : "true",
      "description" : "name: Cloud Controller Manager introduction: Using Cloud Controller
Manager to create load balancers for k8s applications and manage node route entries doc:en: https://www.alibabacloud.com/help/doc-detail/94925.htm"
```

`},`

```json
    "csi-plugin" : {
      "name" : "csi-plugin",
      "version" : "v1.16.9.43-f36bb540-aliyun",
      "disabled" : false,
      "required" : "false",
      "description" : "csi-plugin"
```

`},`

```json
  "ComponentGroups" : [ {
    "group_name" : "storage",
    "items" : [ {
      "name" : "flexvolume"
    }, {
      "name" : "alicloud-disk-controller"
    }, {
      "name" : "csi-plugin"
    }, {
      "name" : "csi-provisioner"
    } ]
  }, {
    "group_name" : "network",
    "items" : [ {
      "name" : "kube-flannel-ds"
    }, {
      "name" : "terway"
    }, {
      "name" : "terway-eni"
    }, {
      "name" : "terway-eniip"
    }, {
      "name" : "nginx-ingress-controller"
    }, {
      "name" : "coredns"
    }, {
      "name" : "managed-kube-proxy"
    } ]
  } ]
```

Error codes You can check further details of error codes. For more information, see Error codes.

#### 3.4.3 DescribeClusterAddonsVersion

Queries the details of all components that are installed in a specified Container Service cluster. Request syntax

```
GET /clusters/ClusterId/components/version HTTP/1.1
```

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClusterId | String | Yes | c82e6987e2961 451182edacd74 faf**** | The ID of the cluster. |

Response syntax

```
HTTP/1.1 200
```

`{`

```json
  "key" : {
    "component_name" : "String",
    "version" : "String",
    "next_version" : "String",
    "changed" : "String",
    "can_upgrade" : Boolean,
    "policy" : "String",
    "ready_to_upgrade" : "String",
    "exist" : Boolean,
    "required" : Boolean,
    "message" : "String",
    "value" : "String"
```

Response parameters Response body parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
|   | Map |   | The response body parameters. |

| eveloper Guide·Cl | uster API list |   | Container Service for Kubernete |
|---|---|---|---|
| Parameter | Type | Example | Description |
|   | Object |   | The details of the component. |
| component na _ me | String | ack-node-problem- detector | The name of the component. |
| version | String | 1.2.1 | The current version of the component. |
| next version _ | String | 1.2.1 | The version to which the component can be upgraded. |
| changed | String | false | Indicates whether the component was upgraded. Valid values: true : The component was upgraded. false : The component was not upgraded. |
| can upgrade _ | Boolean | false | Indicates whether the component is upgradable. Valid values: true : The component is upgradable. false : The component is not upgradable. |
| policy | String | overwrite | The upgrade policy of the component. overwrite : The component configurations of the later version overwrite those of the earlier version. Default value: overwrite . |
| ready to upgra _ _ de | String | false | Indicates whether the component meets the upgrade conditions. Valid values: true : The component meets the upgrade conditions. false : The component does not meet the upgrade conditions. |
| exist | Boolean | true | Indicates whether the component was installed. Valid values: true : The component was installed. false : The component was not installed. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| required | Boolean | false | Indicates whether the component is required in a Container Service cluster. Valid values: true : The component is required in a Container Service cluster. false : The component is not required in a Container Service cluster. |
| message | String | A plug-in that detects exceptions and reports them to the Kubernetes event center. | Additional information about whether the component is upgradable. |
| value | String | npd:\n # Custom monitor definitions to add to Node Problem Detector **** | The custom parameter setting. When you install a component, you can customize parameter settings for the component. |

Examples Sample requests

```
GET /clusters/c82e6987e2961451182edacd74faf****/components/version HTTP/1.1
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <ack-node-problem-detector>
    <exist>true</exist>
    <component_name>ack-node-problem-detector</component_name>
    <can_upgrade>false</can_upgrade>
    <ready_to_upgrade>false</ready_to_upgrade>
    <message>A plug-in that detects node exceptions and reports them to the Kubernetes even
t center.</message>
    <version>1.2.1</version>
    <value>npd:
  # Custom monitor definitions to add to Node Problem Detector ****</value>
    <required>false</required>
    <next_version>1.2.1</next_version>
    <changed>false</changed>
    <policy>overwrite</policy>
</ack-node-problem-detector>
```

`JSON` format

```
HTTP/1.1 200 OK
```

`{`

```json
  "ack-node-problem-detector" : {
    "exist" : "true",
    "component_name" : "ack-node-problem-detector",
    "can_upgrade" : "false",
    "ready_to_upgrade" : "false",
    "message": "A plug-in that detects node exceptions and reports them to the Kubernetes e
vent center.",
    "version" : "1.2.1",
    "value" : "npd:\n  # Custom monitor definitions to add to Node Problem Detector ****",
    "required" : "false",
    "next_version" : "1.2.1",
    "changed" : "false",
    "policy" : "overwrite"
```

Error codes You can check further details of error codes. For more information, see Error codes.

#### 3.4.4 DescribeClusterAddonsUpgradeStatus

Queries the upgrade status of the specified components in a Container Service cluster. Request syntax

```
GET /clusters/[ClusterId]/components/upgradestatus?componentIds=["String"] HTTP/1.1
```

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClusterId | String | Yes | c23421cfa74454 bc8b37163fd19 af**** | The ID of the cluster. |

Request query parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| componentIds | Array of String | No | metric-server | The names of the components that you want to query. |

Response syntax

```
HTTP/1.1 200
```

`{`

```json
  "key" : {
    "addon_info" : {
      "component_name" : "String",
      "version" : "String",
      "ready_to_upgrade" : "String"
```

`},`

```json
    "tasks" : {
      "created_at" : "String",
      "finished_at" : "String",
      "status" : "String",
      "is_canceled" : Boolean
```

Response parameters Response body parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
|   | Map |   | The returned data. |
|   | Object |   | The details of the upgrade status of the queried components. |
| addon info _ | Object |   | The information about the component. |
| component na _ me | String | cloud-controller- manager | The name of the component. |
| version | String | v1.9.3.340- g9830b58-aliyun | The current version of the component. |
| ready to upgra _ _ de | String | true | Indicates whether the component is upgradable. Valid values: true : The component is upgradable. false : The component is not upgradable. |
| tasks | Object |   | The details of the upgrade task. |

| Developer Guide·Cl | uster API list |   | Container Service for Kubernete |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| created at _ | String | 2020-12- 28T17:00:50Z | The beginning time of the task. |
| finished at _ | String | 2020-12- 28T17:05:36Z | The end time of the task. |
| status | String | Success | The state of the upgrade task. |
| is canceled _ | Boolean | false | Indicates whether the upgrade task was canceled. Valid values: true : The upgrade task was canceled. false : The upgrade task was not canceled. |

Examples Sample requests

```
GET /clusters/[ClusterId]/components/upgradestatus?componentIds=["metric-server"] HTTP/1.1
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <cloud-controller-manager>
    <tasks>
        <created_at>2020-12-28T17:01:55Z</created_at>
        <finished_at>2020-12-28T17:05:11Z</finished_at>
        <is_canceled>false</is_canceled>
        <status>Success</status>
    </tasks>
    <addon_info>
        <component_name>cloud-controller-manager</component_name>
        <version>v1.9.3.340-g9830b58-aliyun</version>
        <ready_to_upgrade>true</ready_to_upgrade>
    </addon_info>
</cloud-controller-manager> <metric-server>
    <tasks>
        <created_at>2020-12-28T17:00:32Z</created_at>
        <finished_at>2020-12-28T17:05:54Z</finished_at>
        <is_canceled>false</is_canceled>
        <status>Success</status>
    </tasks>
    <addon_info>
        <component_name>metric-server</component_name>
        <version/>
        <ready_to_upgrade>true</ready_to_upgrade>
    </addon_info>
</metric-server>
```

`JSON` format

```
HTTP/1.1 200 OK
```

`{`

```json
  "cloud-controller-manager" : {
    "tasks" : {
      "created_at" : "2020-12-28T17:01:55Z",
      "finished_at" : "2020-12-28T17:05:11Z",
      "is_canceled" : false,
      "status" : "Success"
```

`},`

```json
    "addon_info" : {
      "component_name" : "cloud-controller-manager",
      "version" : "v1.9.3.340-g9830b58-aliyun",
      "ready_to_upgrade" : "true"
```

`},`

```json
  "metric-server" : {
    "tasks" : {
      "created_at" : "2020-12-28T17:00:32Z",
      "finished_at" : "2020-12-28T17:05:54Z",
      "is_canceled" : false,
      "status" : "Success"
```

`},`

```json
    "addon_info" : {
      "component_name" : "metric-server",
      "version" : "",
      "ready_to_upgrade" : "true"
```

Error codes You can check further details of error codes. For more information, see Error codes.

#### 3.4.5 UpgradeClusterAddons

Upgrades a specified component of a Container Service cluster to the required version. Request syntax

```json
POST /clusters/ClusterId/components/upgrade HTTP/1.1 [ {
  "component_name" : "String",
  "next_version" : "String",
  "version" : "String"
} ]
```

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClusterId | String | Yes | cf4299b79b3e3 4226abfdc80a4 bda**** | The ID of the cluster. |

Request body parameters

| Parameter | Type | Required |   | Example | Description |   |
|---|---|---|---|---|---|---|
|   | Array | No |   |   | The request parameters. |   |
| component na _ me | String | Yes |   | coredns | The name of the component that you want to upgrade. |   |
| next version _ | String | Yes |   | 1.6.7 | The version to which the component can be upgraded. You can call DescribeClusterAddonsVersion to query the version to which the component can be upgraded. |   |
|   |   |   |   |   |   | DescribeClusterAddonsVersion |
| version | String | Yes |   | v1.6.2 | The current version of the component. |   |

Response syntax

```
HTTP/1.1 200 OK
```

Response parameters No response parameters. Examples Sample requests

```json
POST /clusters/cf4299b79b3e34226abfdc80a4bda****/components/upgrade HTTP/1.1 [ {
  "component_name" : "coredns",
  "next_version" : "1.6.7",
  "version" : "v1.6.2"
} ]
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK
```

Error codes You can check further details of error codes. For more information, see Error codes.

#### 3.4.6 UnInstallClusterAddons

Uninstalls components from a specified Container Service cluster. Request syntax

```json
POST /clusters/ClusterId/components/uninstall HTTP/1.1 [ {
  "name" : "String"
} ]
```

Request parameters Request path parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClusterId | String | Yes | c5b5e80b0b64a 4bf6939d2d8fb bc5**** | The ID of the cluster. |

Request body parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
|   | Array | No |   | The list of components that you want to uninstall. The list is an array. |
| name | String | No | ack-node- problem- detector | The name of the component. |

Response syntax

```
HTTP/1.1 200 OK
```

Response parameters No response parameters. Examples Sample requests

```json
POST /clusters/c5b5e80b0b64a4bf6939d2d8fbbc5****/components/uninstall HTTP/1.1 Host:cs.aliyuncs.com [ {
  "name" : "ack-node-problem-detector"
} ]
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK
```

Error codes You can check further details of error codes. For more information, see Error codes.

### 3.5 Commonly used parameters

addon Configurations of cluster components.

| Paramet er | T ype | Example | Descript ion |
|---|---|---|---|
| name | String | nginx-ingress- controller | The name of a component. |
| config | String | {\"IngressSlbNetw orkType\":\"intern et\"} | The configuration of a component. |

| Paramet er | T ype | Example | Descript ion |
|---|---|---|---|
| disabled | Boolean | false | Specifies whether a component is automatically installed in a newly created cluster. In addition to the required components, some optional components, such as Log Service components, are also installed when you create a cluster. You can set this parameter to disable the automatic installation of an optional component. You can install the component in the console or by calling the API after the cluster is created. Valid values: true : disables the automatic installation of a component. false : allows the automatic installation of a component. |

data_disk Configurations of data disks that are mounted to nodes.

| Paramet er | T ype | Example | Descript ion |
|---|---|---|---|

| Paramet er | T ype | Example | Descript ion |
|---|---|---|---|
| category | String | cloud ssd _ | The type of data disk. Valid values: cloud : basic disk. cloud efficiency : _ ultra disk. cloud ssd : standard _ SSD. cloud essd : enhanced _ SSD. Default value: cloud efficiency . _ |
| size | Long | 40 | The size of a data disk. Unit: GiB. Valid values: 40 to 32768. Default value: 120 . |
| encrypted | String | true | Specifies whether to encrypt a data disk. Valid values: true : encrypts the data disk. false : does not encrypt the data disk. Default value: false . |
| auto snapshot policy id _ _ _ | String | sp- 2zej1nogjvovnz4z **** | The ID of an automatic snapshot policy. Automatic backup is performed for disks based on the specified automatic snapshot policy. By default, this parameter is empty. This indicates that automatic backup is disabled. |

runtime Configurations of container runtimes.

| Paramet er | T ype | Example | Descript ion |
|---|---|---|---|
| name | String | docker | The name of a container runtime. The following types of runtimes are supported by Container Service. Sandboxed- Container.runv : runs sandboxed containers and provides improved isolation for application containers. docker . containerd . Default value: docker . |
| version | String | 19.03.5 | The version of a container runtime. By default, the latest version is used. |

tag Configurations of labels.

| Paramet er | T ype | Example | Descript ion |
|---|---|---|---|
| key | String | env | The key of a label. |
| value | String | prod | The value of a label. |

taint Configurations of node taints.

| Paramet er | T ype | Example | Descript ion |
|---|---|---|---|
| key | String | key | The key of a taint. |
| value | String | value | The value of a taint. |
| effect | String | NoSchedule | The scheduling policy. Valid values: NoSchedule : Pods that do not tolerate this taint are not scheduled to nodes with this taint. This policy affects only the scheduling process and takes effect for only pods to be scheduled. Scheduled pods are not affected. NoExecute : Pods that do not tolerate this taint are evicted after this taint is added to the node. PreferNoSchedule : a preferable policy on pods. Scheduled pods are not affected. If this taint is added to a node, the system tries not to schedule pods that do not tolerate this taint to the node. Default value: NoSchedule . |

### 3.6 Error codes

This topic describes the error codes that are returned when you fail to call API operations of Container Service for Kubernetes (ACK).

| Error code | Error message | Description |
|---|---|---|
| ErrorRegionConfigNotFound? | region (%s) dockerVersion (%s) config not found in our records | The error message returned because the specified container version is unavailable in the current region. |
| ErrorValidateParameters | nvalid CIDR, 192.168.X.0/24 or 172.18.X.0/24 ~ 172.31.X.0/24 are accepted | The error message returned because the specified request parameters that are used to manage to the ACK cluster are invalid. |
| ErrorInvalidInstanceType | instanceType (%s) invalid | The error message returned because the specified instance type is invalid. |
| ErrorInitClusterTask | init cluster task failed | The error message returned because the ACK cluster is failed to be initialized. |
| ErrorClusterNotFound | cluster (%s) not found in our records | The error message returned because the specified cluster does not exist. |
| ErrorGenerateShorTermAccessKey s | N/A | The error message returned because an error has occurred when the system attempted to retrieve the AccessKey information. |
| ErrorMissingClusterName | N/A | The error message returned because the cluster name is missing from the request parameters. |
| 502 | N/A | The error message returned because the current request failed. Refresh the page or try again later. |
| LB SLB HTTPS PORT MUST CREA _ _ _ _ _ TE FIRST _ | N/A | The error message returned because an SSL certificate must be created and specified before you configure the HTTPS listening port for the Server Load Balancer (SLB) instance. |
| HOST NOT FOUND _ _ | N/A | The error message returned because the specified host is not found. |

| Error code | Error message | Description |
|---|---|---|
| ROUTING INVALID DOMAIN _ _ | N/A | The error message returned because the specified URL that is used by the service contains an invalid domain name. |
| ErrorClusterNameAlreadyExist | N/A | The error message returned because the specified cluster name already exists. Modify the cluster name and try again. |
| ErrorMissingClusterID | N/A | The error message returned because the cluster ID is missing from the request parameters. |
| CLUSTER IMAGE NEEDED _ _ | N/A | The error message returned because an image must be specified for the ACK cluster. |
| LB HOST PORT NOT SPECIFIED _ _ _ _ | N/A | The error message returned because a host port that is mapped to the container port must be specified when you configure the SLB instance. |
| 403 | N/A | The error message returned because you are not authorized to perform the specified operation. If you use a Resource Access Management (RAM) user, contact the owner of the Alibaba Cloud account to authorize the RAM user. |
| 504 | N/A | The error message returned because the internal gateway timed out. |
| PROJECT NAME EXIST _ _ | N/A | The error message returned because the specified application name already exists. |
| ROUTING DUPLICATE COMBO _ _ | N/A | The error message returned because the specified URL exists. Check whether the URL is used by another service of the ACK cluster. |
| CONTAINER NOT FOUND _ _ | N/A | The error message returned because the specified container does not exist. |

| Error code | Error message | Description |
|---|---|---|
| InternalError | N/A | The error message returned because an internal service error has occurred. Try again later. |
| ErrorCheckAcl | N/A | The error message returned because the specified operation is not supported when the ACK cluster is in the current state. |
| ErrorNotSupport | N/A | The error message returned because the cluster scale-in operation is not supported. |
| PROJECT VERSION NEEDED _ _ | N/A | The error message returned because the application version must be specified. |
| ROUTING CONVERT TO PORT FAI _ _ _ _ LED | N/A | The error message returned because the port that is used by the service is failed to be parsed. |
| SERVER ERROR CODE _ _ | N/A | The error message returned because the service is busy. Refresh the service and try again. |
| ROUTING CONTEXT ROOT TOO L _ _ _ _ ONG | N/A | The error message returned because the length of the specified path in the URL that is used by the service exceeds the upper limit. |
| CLUSTER RAMAK INVLIAD _ _ | N/A | The error message returned because the specified AccessKey pair of the ACK cluster is invalid. Activate the RAM service and request another AccessKey pair. |
| ServiceUnavailable | N/A | The error message returned because the service is temporarily unavailable due to a brief exception. |
| ErrorQuerySecurityGroup | N/A | The error message returned because the system failed to query the security group. |
| LB INVLIAD PROTOCOL _ _ | N/A | The error message returned because the specified protocol of the listening port is invalid when you configure the SLB instance. |

| Error code | Error message | Description |
|---|---|---|
| ROUTING INVALID CONTEXT ROO _ _ _ T | N/A | The error message returned because the specified path in the URL that is used by the service is invalid. |
| ROUTING DOMAIN NAME TOO LO _ _ _ _ NG | N/A | The error message returned because the length of the domain name in the URL that is used by the service exceeds the upper limit. |
| 505 | N/A | The error message returned because the specified HTTP version is not supported. |
| ErrorMissingIP | N/A | The error message returned because the IP address is missing from the request parameters. |
| ErrorAttachInstance | N/A | The error message returned because the specified instance failed to be manually added. |
| LB SLB NAME OR ID NOT FOUND _ _ _ _ _ _ | N/A | The error message returned because the specified name and ID of the SLB instance cannot be found. |
| ErrorInvalidNodeId | N/A | The error message returned because the specified node ID in the request parameters is invalid. |
| 503 | N/A | The error message returned because the current request failed. Refresh the page or try again later. |
| LB INVLIAD CONTAINER PORT _ _ _ | N/A | The error message returned because the specified container port is invalid when you configure the SLB instance. |
| ErrorInvalidClusterName | N/A | The error message returned because the format of the specified cluster name is invalid. |
| ErrorNoAttachEcsInstance | N/A | The error message returned because the manually added instance is invalid. |
| ErrorCheckClusterStatus | N/A | The error message returned because the specified ACK cluster exists. |

| eveloper Guide·Cluster API list |   | Container Service for Kubernete |
|---|---|---|

| Error code | Error message | Description |
|---|---|---|
| LB SLB SHARED BETWEEN SERVIC _ _ _ _ ES | N/A | The error message returned because different services cannot share the same SLB instance when you configure the SLB instance. |
| InvalidParameter | N/A | The error message returned because the specified parameter is invalid. |
| ErrorUpdateClusterName | N/A | The error message returned because the ACK cluster name failed to be updated. |
| ROUTING FULLY QUALIFIED DOMAI _ _ _ N NAME NEEDED _ _ | N/A | The error message returned because the URL that is used by the HTTPS service must be a fully qualified domain name. |
| ErrorQueryRegionConfig | N/A | The error message returned because the configurations that are specified in the request to create an ACK cluster are invalid. |
| ErrorMissingInstanceID | N/A | The error message returned because the instance ID is missing from the request parameters. |
| ROUTING COMBO ALREADY EXIST _ _ _ | N/A | The error message returned because the specified URL has been used by another service of the ACK cluster. |
