---
title: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Data Management Developer Guide 20220928"
product_version: "V3.14.0"
doc_version: "20220928"
pdf_pages: 221
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Data Management Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.14.0/%E6%95%B0%E6%8D%AE%E5%BA%93/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.14.0%20Data%20Management%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.14.0 Data Management Developer Guide 20220928

## Table of Contents

- 1 Use ASAPI to call Apsara Stack SDKs
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
  - 2.1 List of operations by function
  - 2.2 User management
    - 2.2.1 RegisterUser
    - 2.2.2 DisableUser
    - 2.2.3 EnableUser
    - 2.2.4 UpdateUser
    - 2.2.5 DeleteUser
    - 2.2.6 ListUsers
    - 2.2.7 ListUserTenants
    - 2.2.8 GetUserActiveTenant
    - 2.2.9 GetUser
  - 2.3 Instance management
    - 2.3.1 RegisterInstance
    - 2.3.2 ListInstances
    - 2.3.3 GetInstance
    - 2.3.4 UpdateInstance
    - 2.3.5 DeleteInstance
  - 2.4 Operation logs
    - 2.4.1 GetOpLog
  - 2.5 Approval processes
    - 2.5.1 ListWorkFlowTemplates
    - 2.5.2 ListWorkFlowNodes
  - 2.6 Metadata of databases and tables
    - 2.6.1 SearchDatabase
    - 2.6.2 SearchTable
    - 2.6.3 ListDatabases
    - 2.6.4 ListLogicDatabases
    - 2.6.5 ListTables
    - 2.6.6 ListLogicTables
    - 2.6.7 ListColumns
    - 2.6.8 ListIndexes
    - 2.6.9 GetDatabase
    - 2.6.10 GetLogicDatabase
    - 2.6.11 GetMetaTableDetailInfo
    - 2.6.12 GetTableDBTopology
    - 2.6.13 GetMetaTableColumn
    - 2.6.14 SyncDatabaseMeta
    - 2.6.15 SyncInstanceMeta
  - 2.7 Ticket operations
    - 2.7.1 General
      - 2.7.1.1 ApproveOrder
      - 2.7.1.2 CloseOrder
      - 2.7.1.3 GetApprovalDetail
      - 2.7.1.4 GetOrderBaseInfo
      - 2.7.1.5 ListOrders
      - 2.7.1.6 SubmitOrderApproval
      - 2.7.1.7 CreateOrder
    - 2.7.2 Data changes
      - 2.7.2.1 ExecuteDataCorrect
      - 2.7.2.2 GetDataCorrectBackupFiles
      - 2.7.2.3 GetDataCorrectOrderDetail
    - 2.7.3 Schema design
      - 2.7.3.1 CreatePublishGroupTask
    - 2.7.4 Data export
      - 2.7.4.1 ExecuteDataExport
      - 2.7.4.2 GetDataExportDownloadURL
      - 2.7.4.3 GetDataExportOrderDetail
  - 2.8 Permission management
    - 2.8.1 RevokeUserPermission
    - 2.8.2 ListDatabaseUserPermssions
    - 2.8.3 SetOwners
    - 2.8.4 ListUserPermissions
    - 2.8.5 GrantUserPermission
  - 2.9 Security management
    - 2.9.1 ListSensitiveColumns
    - 2.9.2 ListSensitiveColumnsDetail
  - 2.10 Data query
    - 2.10.1 ExecuteScript

Apsara Stack SDKs

## 1 Use ASAPI to call Apsara Stack SDKs

SDKs

### 1.1 ASAPI Developer Guide

#### 1.1.1 ASAPI overview

This topic describes the architecture and features of the Apsara Stack API (ASAPI). The ASAPI is a unified ingress gateway for Apsara Stack services and a main component of the Apsara Uni-manager Management Console. The ASAPI provides a unified method for you to manage and make API calls. You can use Apsara Stack SDK to centrally make API calls to Apsara Stack services, including Elastic Compute Service (ECS) and Virtual Private Cloud (VPC). The ASAPI allows you to make API calls to manage and maintain Apsara Stack services. Make API calls to implement enterprise-grade management. For example, you can manage organizations, users, roles, resource sets, and logon policies. These operations are provided by the Apsara Stack SDKs Apsara Uni-manager Management Console. Make API calls to manage operations. For example, you can manage quotas, usage statistics, specifications, and password policies. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to manage resources. For example, you can create, delete, query, or modify cloud resources. These operations are provided by Apsara Stack services. If you call an API operation to create an ECS instance or a VPC, the API operation is provided by ECS or VPC. Make API calls to query monitoring metrics of Apsara Stack services. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to perform O&M. For example, you can manage monitoring and alerting, inventories, tasks, and physical servers. These operations are provided by the Apsara Uni-manager Operations Console. For more information, see the developer guide of the corresponding Apsara Stack service. For information about API operations used to manage organization users, see Apsara Uni-manager Management Console Developer Guide. For information about the API operation used to create an ECS instance, see ECS Developer Guide. Not e If the "Use Apsara Stack SDK to make API calls" section is included in the developer guide of an Apsara Stack service, the ASAPI is supported by the Apsara Stack service. In this case, you can make API calls based on the developer guide.

#### 1.1.2 Preparations

##### 1.1.2.1 Log on to the API Tool console

You can log on to the API Tool console from the Apsara Uni-manager Management Console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. Apsara Stack SDKs Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
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

This topic describes three methods used to generate an endpoint for the Apsara Stack API (ASAPI). Apsara Stack SDKs Method 1: Use Registration Vars of Services to generate an endpoint
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
Apsara Stack SDKs i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click O&M. iii. In the left-side navigation pane, choose Product Management > Product s. iv. In the Apsara Stack O&M section, click Apsara Inf rast ruct ure Management Framework.
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
root domain, contact Apsara Stack O&M personnel. Take note of this point: Use the internetdomain parameter instead of the intranet-domain parameter. If the region value is `cn-****-****-d01` and the int ernet -domain value is `inter.****.****.com` , the following endpoint can be generated: Apsara Stack SDKs

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

Apsara Stack SDKs

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

When you use Apsara Stack SDK for Node.js to make API calls, specify a region ID. You can obtain a region ID in the Apsara Uni-manager Management Console. Procedure Apsara Stack SDKs
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

Apsara Stack SDKs

| Paramet er | T ype | Required | Descript ion |
|---|---|---|---|
| Signature | String | Yes | The signature string of the current request. For more information about how signatures are calculated, see Request signatures. |
| SignatureMethod | String | Yes | The encryption method of the signature string. Valid values: HMAC- SHA1 and HMAC- SHA256. |
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Valid values: 1.0 and 2.0. |
| SignatureNonce | String | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the yyyy- MM-ddTHH:mm:ssZ format. The time must be in UTC. Sample value: 2018-01- 01T12:00:00Z. |
| Format | String | Yes | The format in which to return the response. Set the value to JSON. |

Apsara Stack SDKs Not e

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
Method 1: Create a Maven project in IntelliJ IDEA. Apsara Stack SDKs Method 2: Convert an existing project to a Maven project. a. Right-click the project that you want to convert and select Add Framework Support .... b. Select Maven and click OK.
4. Create a folder named libs in the root directory of the project. Then, add the JAR file of Apsara
Stack SDK for Java to the libs folder, as shown in the following figure. Apsara Stack SDKs
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
Apsara Stack SDKs If the information in the following figure appears, the dependencies are added. Use Apsara Stack SDK for Java You can use the GET or POST method to call API operations provided by the ASAPI. The following sample code shows how to call API operations: Apsara Stack SDKs

```java
// 1. Create a connection to an ASClient object. ASClient client = new ASClient(); // 2. Configure the identifier of the requester. This parameter is required and used only f or identification. You can set this parameter to a random value. client.setSdkSource("<The identifier of the requester>"); Map<String, Object> parameters = new HashMap<String, Object>(); // 3. Configure the parameters for authorization. The parameter values vary based on your e nvironment. // The AccessKey ID of your Apsara Stack tenant account. parameters.put("AccessKeyId","<AccessKey ID>"); // The AccessKey secret of your Apsara Stack tenant account. parameters.put("AccessKeySecret", "<AccessKey Secret>"); // The ID of the region. parameters.put("RegionId", "<your RegionID>"); // 4. Configure parameters for an API call. In this example, the Product, Action, and Versi on parameters are configured. parameters.put("Product", "<The name of the service>"); parameters.put("Action", "<The name of the API operation>"); parameters.put("Version", "<The version of the API operation>"); // 5. Configure operation-specific parameters. parameters.put("<The name of the operation-specific parameter>", "<The value of the operati on-specific parameter>"); // 6. Configure request headers and the encryption method for the signature string. Valid v alues of the SignatureMethod parameter: HMAC-SHA1 and HMAC-SHA256. By default, HMAC-SHA256 is used. Map<String, String> headers = new HashMap<String, String>(); //headers.put("SignatureMethod", "HMAC-SHA1"); headers.put("x-acs-regionid", "<your-regionid>"); headers.put("x-acs-resourcegroupid", "<your-resourcegroupid>"); headers.put("x-acs-organizationid", "<your-organizationid>"); headers.put("x-acs-instanceid", "<your-instanceid>"); // 7. Make an API call. We recommend that you use the doPost() method. // Configure the time-out period for a connection. //client.setConnectTimeout(10000); // Configure the time-out period for a request. // client.setSocketTimeout(10000); String result = client.doPost(endpoint, headers, parameters); System.out.println(result);
```

Configure a proxy If you need to use a proxy to make API calls, use the following sample code to configure the proxy:

```
Cloud cloud = new Cloud(); // Configure the IP address of the proxy. cloud.setConfig("proxy_host", "<IP>"); // Configure the port used by the proxy. cloud.setConfig("proxy_port", "<Port>"); // 1. Create a connection to an ASClient object. ASClient client = new ASClient(cloud);
```

Request headers Apsara Stack SDKs

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

Not e Replace `2.4.7` with the actual version of Apsara Stack SDK for Python. Sample requests You can use the GET or POST method to call API operations provided by the ASAPI. Apsara Stack SDKs

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

Apsara Stack SDKs Configure a proxy Perform the following steps to configure a proxy:
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

Use Apsara Stack SDK for Node.js The following sample code shows how to use Apsara Stack SDK for Node.js to make API calls: Apsara Stack SDKs

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

Apsara Stack SDKs Request headers

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

Apsara Stack SDKs Call examples The following sample code provides an example on how to use the RPC style to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05-26. Sample code:

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

Apsara Stack SDKs

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

Apsara Stack SDKs

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

This topic describes how to use Apsara Stack API (ASAPI) SDK for POP for Go. Prerequisites An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed. Background information Only the remote procedure call (RPC) style is supported for API calls. Call examples The following sample code provides an example on how to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05- 26. Apsara Stack SDKs Sample code:

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

Apsara Stack SDKs

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

This topic describes how to use Apsara Stack API (ASAPI) SDK for POP for Python. Prerequisites An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed. Background information Only the remote procedure call (RPC) style is supported for API calls. Apsara Stack SDKs Call examples The following sample code provides an example on how to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05- 26. Sample code:

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

Configure proxies Apsara Stack SDKs Set the HTTP_PROXY and HTTPS_PROXY environment variables. Sample code:

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

`https` : the protocol used to transmit the request. `public.asapi.aliyuns.com/asapi/v3` : the endpoint of the ASAPI. `Action=GetOrganizationList Product=ascm Version=2019-05-10` : the API operation to call. `Id` : the ID of the organization. `<Common parameters>` : the common parameters specified in the system. Apsara Stack SDKs Protocol The ASAPI supports only HTTPS. Endpoint For more information about how to obtain an endpoint, see Generate an endpoint for the ASAPI. To specify an API operation, use the `Action, Product, and Version` parameters. For example, set `Action` to GetOrganizationList, Product to ascm, and Version to 2019-05-10. You must also specify other operation-specific parameters and common parameters. For more information, see Common parameters.

##### 1.1.5.3 Request signatures

This topic describes how to sign HTTP API requests. ASAPI uses the request signature to verify the identity of the request sender. ASAPI implements symmetric encryption by using an AccessKey pair to verify the identity of the request sender. Not e An AccessKey pair consists of an AccessKey ID and an AccessKey secret, which are issued to each user or organization in the Apsara Uni-manager Management Console. The AccessKey ID is used to verify identities of users, and the AccessKey secret is used to encrypt and verify signature strings. You must keep your AccessKey secret confidential. ASAPI provides SDKs for Node.js, Python, and Java to facilitate complex signature calculation. For more information, see Obtain the core package for ASAPI. Step 1: Create a canonicalized query string
1. Arrange the request parameters in alphabetical order, including all common and operation-specific
parameters except the `Signature` parameter. Not e If you use the GET method to send a request,these parameters are connected by ampersands (&) and included in the request URL. The first request parameter follows a question mark (?).
2. Encode the request parameters and their values in UTF-8 based on RFC 3986. The following rules
apply in the encoding process: Letters, digits, and special characters such as hyphens ( `-` ), underscores ( `_` ), and periods ( `.` ) do not need to be encoded. Apsara Stack SDKs Other characters must be percent encoded in the %XY format. `XY` represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks ( `"` ) are encoded as %22 . Extended UTF-8 characters are encoded in the %XY%ZA… format. Spaces must be encoded as %20 . Do not encode spaces as plus signs ( `+` ). This encoding method is similar to but different from the `application/x-www-form-urlencoded` MIME encoding algorithm. If you use `java.net.URLEncoder` from the Java standard library, use `percentEncode` to encode request parameters and their values. In the encoded query string, replace the plus signs ( `+` ) with %20 , asterisks ( `*` ) with %2A , and %7E with tildes ( ~ ). This way, you can obtain an encoded string that matches the preceding encoding rules.

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

Apsara Stack SDKs Not e When you calculate the signature, the key value specified by RFC 2104 is your `AccessKey secret` plus an ampersand (&), which has an ASCII value of 38. For more information, see Obtain an AccessKey pair.
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

You can use browsers or tools such as cURL and Wget to initiate an HTTP request for calling the `DescribeRegions` operation to query the Alibaba Cloud region list. Example 2: Use t he st andard library of t he programming language Apsara Stack SDKs `GetOrganizationList` is used in this example to query regions. For example, `AccessKeyID` is set to testid, `AccessKeySecret` is set to testsecret, and all request parameters are stored in a Java `Map<String, String>` object.
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
Apsara Stack SDKs

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

Apsara Stack SDKs
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

### 2.1 List of operations by function

The following tables describe the API operations available for use in Data Management (DMS). User management

| API | Description |
|---|---|
| RegisterUser | Adds a user. |
| DisableUser | Disables a user. |
| EnableUser | Enables a user. |
| UpdateUser | Updates the information about a user. |
| DeleteUser | Deletes a user. |
| ListUsers | Queries the details about users. |
| ListUserTenants | Queries tenants. |
| GetUserActiveTenant | Queries the details about a tenant. |
| GetUser | Queries the details about a user. |

Instance management

| API | Description |
|---|---|
| RegisterInstance | Adds a database instance. |
| ListInstances | Queries the details about instances. |
| GetInstance | Queries the details about an instance. |
| UpdateInstance | Updates the information about an instance and checks the connectivity of the instance. |
| DeleteInstance | Deletes instances that are managed by DMS. |

Operation logs

| API | Description |
|---|---|
| GetOpLog | Queries the details about operation logs that are generated in a specified period of time. |

Approval processes

| API | Description |
|---|---|
| ListWorkFlowTemplates | Queries approval templates. |
| ListWorkFlowNodes | Queries approval nodes. |

Metadata of databases and tables

| API | Description |
|---|---|
| SearchDatabase | Queries the details about a database. |
| SearchTable | Queries the details about a table. |
| ListDatabases | Queries the details about databases in an instance. |
| ListLogicDatabases | Queries the details about logical databases. |
| ListTables | Queries the details about tables in a database. |
| ListLogicTables | Queries the details about logical tables in a logical database. |
| ListColumns | Queries the details about columns in a table. |
| ListIndexes | Queries the details about indexes in a table. |
| GetDatabase | Queries the details about a database. |
| GetLogicDatabase | Queries the details about a logic database. |
| GetMetaTableDetailInfo | Queries the details about fields and indexes in a table. |
| GetTableDBTopology | Queries the topology of a table. |
| GetMetaTableColumn | Queries the details about fields in a table. |
| SyncDatabaseMeta | Synchronizes the metadata of a database dictionary. |
| SyncInstanceMeta | Synchronizes the metadata of all database dictionaries in an instance. |

Ticket operations

| Category | API | Description |
|---|---|---|
| General | ApproveOrder | Reviews a ticket. |
|   | CloseOrder | Closes a ticket. |
|   | GetApprovalDetail | Queries the details about an approval process for a ticket. |
|   | GetOrderBaseInfo | Queries the basic information about a ticket. |

| ata Managem |   |   |
|---|---|---|
|   | ent | Developer Guide·API Referenc |
| Category | API | Description |
|   | ListOrders | Queries the details about tickets. |
|   | SubmitOrderApproval | Submits a ticket for approval. |
|   | CreateOrder | Creates a ticket. |
| Data change | ExecuteDataCorrect | Executes a ticket that is used to modify data. |
|   | GetDataCorrectBackupFiles | Queries the download URL of an attachment that includes the backup files of data changes. |
|   | GetDataCorrectOrderDetail | Queries the details about a ticket that is used to modify data. |
| Schema design | CreatePublishGroupTask | Executes a ticket that is used to modify the schema design of a database. |
| Data export | ExecuteDataExport | Executes a ticket that is used to export data. |
|   | GetDataExportDownloadURL | Queries the download URL of an attachment that includes the exported data. |
|   | GetDataExportOrderDetail | Queries the details about a ticket that is used to export data. |

Permission management

| API | Description |
|---|---|
| RevokeUserPermission | Revokes the permissions of a user. |
| ListDatabaseUserPermssions | Queries the details about user permissions on the resources of a database. |
| SetOwners | Sets the owners of a database or table. |
| ListUserPermissions | Queries the permissions of a user on databases and tables. |
| GrantUserPermission | Grants a user the permissions on a database or table. |

Security management

| API | Description |
|---|---|
| ListSensitiveColumns | Queries sensitive columns. |
| ListSensitiveColumnsDetail | Queries the details about sensitive columns. |

Data query

| API | Description |
|---|---|
| ExecuteScript | Executes an SQL script. |

### 2.2 User management

#### 2.2.1 RegisterUser

Adds a user to your enterprise. The administ rat or of Data Management (DMS) Enterprise can call this operation to add users to DMS Enterprise. To check the users that assume the administrator role, perform the following steps: Log on to the DMS Enterprise console and choose System Management > User Management. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RegisterUser | The operation that you want to perform. Set the value to Regist erUser. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| Uid | String | Yes | 12345678 | The ID of the Apsara Stack tenant account of the user that you want to add. |
| UserNick | String | No | dmstest | The name of the user. |
| RoleNames | String | No | USER,DBA | The roles that the user assumes. Valid values: USER: a common user DBA: a database administrator (DBA) ADMIN: an administrator SECURIT Y ADMIN: a security _ administrator Not e Default value: USER. You can specify one or more roles for the user. Separate multiple roles with commas (,). |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Mobile | String | No | 130000000xx | The contact number of the user. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | 403 | The returned error code. |
| ErrorMessage | String | The specified user already exists. | The returned error message. |
| RequestId | String | 34E01EDD-6A16- 4CF0-9541- C644D1BE01AA | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=RegisterUser &Tid=-1 &Uid=12345678 &UserNick=dmstest &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RegisterUserResponse>
      <RequestId>ADE24A7C-DB8B-4D32-94AD-E50E3B921197</RequestId>
      <Success>true</Success>
</RegisterUserResponse>
```

`JSON` format `{`

```json
    "RequestId": "34E01EDD-6A16-4CF0-9541-C644D1BE01AA",
    "Success": true
```

`}`

#### 2.2.2 DisableUser

Disables an Apsara Stack tenant account. This operation is related to the disable user feature of Data Management (DMS). To use this feature, perform the following steps: Log on to the DMS console, choose System Management > User Management. The administrator of DMS Enterprise can call this operation to disable an Apsara Stack tenant account that is temporarily not used in DMS Enterprise. After an Apsara Stack tenant account is disabled, the permissions that are granted to the Apsara Stack tenant account are revoked. The data owner configurations and database administrator (DBA) configurations are also disabled. Not e This operation only stops an Apsara Stack tenant account from logging on to your DMS Enterprise console. The Apsara Stack tenant account is not disabled After an Apsara Stack tenant account is disabled, you cannot use the account to log on to your DMS Enterprise console until the account is enabled again. However, the disabled account still exists in DMS Enterprise. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DisableUser | The operation that you want to perform. Set the value to DisableUser. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| Uid | String | Yes | 12345 | The ID of the Apsara Stack tenant account. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | 403 | The error code that is returned. |
| ErrorMessage | String | The specified user not exists. | The error message that is returned. |
| RequestId | String | 34E01EDD-6A16- 4CF0-9541- C644D1BE01AA | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeds. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DisableUser &Tid=-1 &Uid=12345 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DisableUserResponse>
    <RequestId>ADE24A7C-DB8B-4D32-94AD-E50E3B921197</RequestId>
    <Success>true</Success>
</DisableUserResponse>
```

`JSON` format `{`

```json
    "RequestId":"34E01EDD-6A16-4CF0-9541-C644D1BE01AA",
    "Success":true
```

`}`

#### 2.2.3 EnableUser

Enables a disabled Apsara Stack tenant account. This operation is related to the enable user feature of Data Management (DMS) Enterprise. To use this feature, perform the following steps: Log on to the DMS Enterprise console, choose System Management > User Management. The administrator of DMS Enterprise can call this operation to enable an Apsara Stack tenant account that is disabled in DMS Enterprise. After an Apsara Stack tenant account is enabled, you can use the account to log on to the DMS Enterprise console and perform the required operations. Not e This operation only removes the limit of a disabled Apsara Stack tenant account that cannot be used to log on to the DMS Enterprise console. Other operations that can be performed by the Apsara Stack tenant account are not affected. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | EnableUser | The operation that you want to perform. Set the value to EnableUser. |
| Tid | Long | Yes | -1 | The ID of the tenant. |

|   | Developer Guide·API | Reference |   |   | Data Managemen | t |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Uid | String | Yes | 12345 | The ID of the Apsara Stack tenant account. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | 403 | The returned error code. |
| ErrorMessage | String | The specified user not exists. | The returned error message. |
| RequestId | String | 34E01EDD-6A16- 4CF0-9541- C644D1BE01AA | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=EnableUser &Tid=-1 &Uid=12345 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<EnableUserResponse>
    <RequestId>ADE24A7C-DB8B-4D32-94AD-E50E3B921197</RequestId>
    <Success>true</Success>
</EnableUserResponse>
```

`JSON` format `{`

```json
    "RequestId": "34E01EDD-6A16-4CF0-9541-C644D1BE01AA",
    "Success": true
```

`}`

#### 2.2.4 UpdateUser

Updates the information of a user. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateUser | The operation that you want to perform. Set the value to Updat eUser. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| Uid | Long | Yes | 123456789 | The ID of the user. |
| UserNick | String | No | test | The name of the user. |
| RoleNames | String | No | ADMIN,DBA | The roles that the user assumes. For more information about the valid values, see the Regist erUser operation. |
| Mobile | String | No | 188xxxxxxxx | The DingTalk ID or mobile number of the user. |
| MaxExecuteCount | Long | No | 1000 | The maximum number of queries that can be performed each day. |
| MaxResultCount | Long | No | 1000 | The maximum number of rows that can be queried each day. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The error code that is returned. |
| ErrorMessage | String | UnknownError | The error message that is returned. |

|   | Developer Guide·AP | I Reference |   | Data Managemen | t |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | E9BEBF41-4F69- 4605-A5D5- A67955173941 | The ID of the request. |
| Success | Boolean | false | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=UpdateUser &Tid=-1 &Uid=123456789 &UserNick=test &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>E9BEBF41-4F69-4605-A5D5-A67955173941</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "E9BEBF41-4F69-4605-A5D5-A67955173941",
  "Success": true
```

`}`

#### 2.2.5 DeleteUser

Deletes an Apsara Stack tenant account. This operation is related to the delete user feature of Data Management (DMS). To use this feature, perform the following steps: Log on to the DMS console, choose System Management > User Management. The administrator of DMS Enterprise can call this operation to delete an Apsara Stack tenant account that is no longer used in DMS Enterprise. After an Apsara Stack tenant account is deleted, the permissions that are granted to the Apsara Stack tenant account are revoked. The data owner configurations and database administrator (DBA) configurations are disabled. Not e This operation only removes the relationship between an Apsara Stack tenant account and your DMS Enterprise. The Apsara Stack tenant account is not deleted. After you delete an Apsara Stack tenant account, you cannot use this account to log on to DMS Enterprise until the account is recreated. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteUser | The operation that you want to perform. Set the value to Delet eUser. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| Uid | String | Yes | 12345 | The ID of the Apsara Stack tenant account. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | 403 | The error code that is returned. |
| ErrorMessage | String | The specified user not exists. | The error message that is returned. |
| RequestId | String | 34E01EDD-6A16- 4CF0-9541- C644D1BE01AA | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeds. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteUser &Tid=-1 &Uid=12345 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteUserResponse>
    <RequestId>ADE24A7C-DB8B-4D32-94AD-E50E3B921197</RequestId>
    <Success>true</Success>
</DeleteUserResponse>
```

`JSON` format `{`

```json
    "RequestId":"34E01EDD-6A16-4CF0-9541-C644D1BE01AA",
    "Success":true
```

`}`

#### 2.2.6 ListUsers

Queries the details about users. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListUsers | The operation that you want to perform. Set the value to List Users. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| Role | String | No | DBA | The role of users. For more information, see the description of the Regist erUser operation. |
| UserState | String | No | NORMAL | The status of users. Valid values: NORMAL: Users are normal. DISABLE: Users are disabled. DELETE: Uses are deleted. |
| SearchKey | String | No | test | The keyword that is used to search for users. |
| PageNumber | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 50 | The number of entries to return on each page. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |

| ata Management |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | 98D35416-2B92- 4CE5-8FD2- B1E61E165536 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |
| TotalCount | Long | 1 | The total number of entries that are returned. |
| UserList | Array of User |   | The details about users. |
| User |   |   |   |
| CurExecuteCoun t | Long | 0 | The number of queries that are performed on the current day. |
| CurResultCount | Long | 0 | The number of rows that are queried on the current day. |
| LastLoginTime | String | 2020-02-02 00:00:00 | The last logon time. |
| MaxExecuteCou nt | Long | 1000 | The maximum number of queries that can be performed on the current day. |
| MaxResultCoun t | Long | 1000 | The maximum number of rows that can be queried on the current day. |
| Mobile | String | 188xxxxx | The DingTalk ID or mobile phone number of the user. |
| NickName | String | test | The name of the user. |
| ParentUid | String | 143214352 | The ID of the parent Apsara Stack tenant account of the user. |
| RoleIdList | List | 1 | The IDs of roles. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RoleNameList | List | ADMIN | The names of roles. |
| State | String | NORMAL | The status of the user. |
| Uid | String | 14324321533 | The ID of the Apsara Stack tenant account of the user. |
| UserId | String | 1 | The ID of the user. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListUsers &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UserList>
    <User>
        <RoleIdList>
            <RoleIds>3</RoleIds>
            <RoleIds>1</RoleIds>
        </RoleIdList>
        <State>NORMAL</State>
        <RoleNameList>
            <RoleNames>ADMIN</RoleNames>
            <RoleNames>USER</RoleNames>
        </RoleNameList>
        <NickName>xxx</NickName>
        <UserId>2</UserId>
        <Uid>111</Uid>
    </User>
    <User>
        <RoleIdList>
            <RoleIds>1</RoleIds>
            <RoleIds>3</RoleIds>
        </RoleIdList>
        <State>NORMAL</State>
        <RoleNameList>
            <RoleNames>USER</RoleNames>
            <RoleNames>ADMIN</RoleNames>
        </RoleNameList>
        <NickName>xxx[RAM user]</NickName>
        <ParentUid>111</ParentUid>
        <UserId>1</UserId>
        <Uid>111</Uid>
    </User>
</UserList> <TotalCount>2</TotalCount> <RequestId>2D346B20-BF4A-4C96-8295-DE8EB9BF5B90</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "UserList": {
    "User": [
```

`{`

```json
        "RoleIdList": {
          "RoleIds": [
```

`3,` `]` `},`

```json
        "State": "NORMAL",
        "RoleNameList": {
          "RoleNames": [
            "ADMIN",
            "USER"
```

`]` `},`

```json
        "NickName": "xxx",
        "UserId": 2,
        "Uid": "111"
```

`},` `{`

```json
        "RoleIdList": {
          "RoleIds": [
```

`1,` `]` `},`

```json
        "State": "NORMAL",
        "RoleNameList": {
          "RoleNames": [
            "USER",
            "ADMIN"
```

`]` `},`

```json
        "NickName": "xxx[RAM user]"
        "ParentUid": "111",
        "UserId": 1,
        "Uid": "111"
```

`}` `]` `},`

```json
  "TotalCount": 2,
  "RequestId": "2D346B20-BF4A-4C96-8295-DE8EB9BF5B90",
  "Success": true
```

`}`

#### 2.2.7 ListUserTenants

Queries tenants. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListUserTenants | The operation that you want to perform. Set the value to List UserT enant s. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where DMS resides. This parameter is used to call the operation. Not e Set this parameter to the ID of the region that is in proximity to your applications. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | CA1F4A4D-EE49- 472F-8DF9- F537101E263A | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |
| TenantList | Array of Tenant |   | The tenants. |
| Status | String | ACTIVE | The status of the tenant. Valid values: ACTIVE: active. All users belong to this tenant. IN ACTIVE: inactive _ |
| TenantName | String | test | The name of the tenant. |
| Tid | Long | -1 | The ID of the tenant. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListUserTenants &RegionId=cn-hangzhou &<Common Request Parameters>
```

Sample success responses `XML` format

```xml
<RequestId>CA1F4A4D-EE49-472F-8DF9-F537101E263A</RequestId> <TenantList>
    <Status>ACTIVE</Status>
    <TenantName>test1</TenantName>
    <Tid>-1</Tid>
</TenantList> <TenantList>
    <Status>IN_ACTIVE</Status>
    <TenantName>test2</TenantName>
    <Tid>-2</Tid>
</TenantList> <TenantList>
    <Status>IN_ACTIVE</Status>
    <TenantName>tes</TenantName>
    <Tid>-3</Tid>
</TenantList>
```

`JSON` format `{`

```json
  "RequestId": "CA1F4A4D-EE49-472F-8DF9-F537101E263A",
  "TenantList": [
```

`{`

```json
      "Status": "ACTIVE",
      "TenantName": "test1",
      "Tid": -1
```

`},` `{`

```json
      "Status": "IN_ACTIVE",
      "TenantName": "test2",
      "Tid": -2
```

`},` `{`

```json
      "Status": "IN_ACTIVE",
      "TenantName": "tes",
      "Tid": -3
```

`}` `]` `}`

#### 2.2.8 GetUserActiveTenant

Queries the details about a tenant. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetUserActiveTen ant | The operation that you want to perform. Set the value to Get UserAct iveT enant . |
| RegionId | String | No | cn-hangzhou | The ID of the region where Data Management (DMS) resides. Not e Set this parameter to the ID of the region that is in proximity to your applications. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | E20EAB9F-A3DB- 42EC-BD0C- 102A886340F5 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |
| Tenant | Struct |   | The details about the tenant. |
| Status | String | ACTIVE | The status of the tenant. Valid values: ACTIVE: active IN ACTIVE: inactive _ |
| TenantName | String | test | The name of the tenant. |
| Tid | Long | -1 | The ID of the tenant. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GetUserActiveTenant &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Tenant>
    <Status>ACTIVE</Status>
    <TenantName>test</TenantName>
    <Tid>-1</Tid>
</Tenant> <RequestId>E20EAB9F-A3DB-42EC-BD0C-102A886340F5</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "Tenant": {
    "Status": "ACTIVE",
    "TenantName": "test",
    "Tid": -1
```

`},`

```json
  "RequestId": "E20EAB9F-A3DB-42EC-BD0C-102A886340F5",
  "Success": true
```

`}`

#### 2.2.9 GetUser

Queries the details of a user. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetUser | The operation that you want to perform. Set the value to Get User. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| Uid | String | No | 123344235 | The ID of the Apsara Stack tenant account of the user. |
| UserId | String | No | 1343 | The ID of the user. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | CFF30064-5985- 4ACB-B3F9- 9557596913C8 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |
| User | Struct |   | The information about the user. |
| CurExecuteCoun t | Long | 0 | The number of queries that were issued on the current day. |
| CurResultCount | Long | 0 | The number of rows that were queried on the current day. |
| LastLoginTime | String | 2020-02-02 00:00:00 | The last logon time. |
| MaxExecuteCou nt | Long | 1000 | The maximum number of queries that can be performed on the current day. |
| MaxResultCoun t | Long | 1000 | The maximum number of rows that can be queried on the current day. |
| Mobile | String | 138xxxxxxxx | The mobile phone number of the user. |
| NickName | String | nickName | The name of the user. |
| ParentUid | Long | 12345352 | The ID of the Apsara Stack tenant account. |
| RoleIdList | List | 1 | The IDs of the roles. |
| RoleNameList | List | Common user | The names of the roles. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| State | String | NORMAL | The status of the user. |
| Uid | String | 1243215435 | The ID of the Apsara Stack tenant account of the user. |
| UserId | String | 122 | The ID of the user. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GetUser &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<User>
    <RoleIdList>
        <RoleIds>1</RoleIds>
        <RoleIds>4</RoleIds>
        <RoleIds>3</RoleIds>
        <RoleIds>2</RoleIds>
    </RoleIdList>
    <State>NORMAL</State>
    <RoleNameList>
        <RoleNames>Common user</RoleNames>
        <RoleNames>Security administrator</RoleNames>
        <AccountDescription>Administrator</AccountDescription>
        <RoleNames>DBA</RoleNames>
    </RoleNameList>
    <NickName>xxx</NickName>
    <ParentUid>114324325</ParentUid>
    <UserId>432143</UserId>
    <Uid>41234234324</Uid>
</User> <RequestId>CFF30064-5985-4ACB-B3F9-9557596913C8</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "User": {
    "RoleIdList": {
      "RoleIds": [
```

`1,` `4,` `3,` `]` `},`

```json
    "State": "NORMAL",
    "RoleNameList": {
      "RoleNames": [
        "Common user",
        "Security administrator",
        "Administrator",
        "DBA"
```

`]` `},`

```json
    "NickName": "xxx",
    "ParentUid": "114324325",
    "UserId": 432143,
    "Uid": "41234234324"
```

`},`

```json
  "RequestId": "CFF30064-5985-4ACB-B3F9-9557596913C8",
  "Success": true
```

`}`

### 2.3 Instance management

#### 2.3.1 RegisterInstance

Adds a database instance to your enterprise. The administ rat or and dat abase administ rat or (DBA) of Data Management (DMS) Enterprise can call this operation to add database instances to DMS Enterprise. To check users who assume the administrator or DBA role, perform the following steps: Log on to the DMS Enterprise console and choose System Management > User Management. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RegisterInstance | The operation that you want to perform. Set the value to Regist erInst ance. |
| Tid | Long | Yes | -1 | The ID of the tenant. |

| Developer Guide·API | Reference |   |   | Data Managemen |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| InstanceType | String | Yes | MySQL | The type of the database instance. Valid values: MySQL SQLServer PostgreSQL Oracle DRDS OceanBase Mongo Redis |
| InstanceSource | String | Yes | RDS | The source of the database instance. Valid values: PUBLIC OWN: a self-managed _ database that is created in the public network. RDS: an ApsaraDB RDS instance. ECS OWN: a self-managed _ database that is created on an Elastic Compute Service (ECS) instance. VPC IDC: a self-managed database _ that is created in the Internet data center (IDC) of a virtual private cloud (VPC). |
| NetworkType | String | Yes | VPC | The type of the network. |
| EnvType | String | Yes | product | The type of the environment. Valid values: product: production environment dev: development environment pre: staging environment test: test environment sit: SIT environment uat: UAT environment pet: stress testing environment stag: STAG environment |
| Host | String | Yes | dmstest.rds.aliyu n.com | The host address of the required database. |

| ata Management |   |   |   | Developer Guide·API Referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Port | Integer | Yes | 3306 | The number of the port that is used to connect to the required database. |
| DatabaseUser | String | Yes | dmstest | The username of the account that is used to log on to the database. |
| DatabasePasswor d | String | Yes | password | The password of the account. |
| InstanceAlias | String | Yes | Test instance | The name of the instance. Specify a name that can help you identify and locate the instance. |
| DbaUid | Long | Yes | 12345678 | The ID of the Apsara Stack tenant account for the database administrator (DBA) of the instance. |
| SafeRule | String | Yes | Test | The name of the security rule that belongs to your enterprise. |
| QueryTimeout | Integer | Yes | 60 | The timeout period for the query. Unit: seconds. |
| ExportTimeout | Integer | Yes | 600 | The timeout period for the export. Unit: seconds. |
| EcsInstanceId | String | No | i-xxxxxxxxx | The ID of the ECS instance. Not e This parameter is required if the Inst anceSource parameter is set to ECS OWN. _ |
| VpcId | String | No | vpc- xxxxxxxxxxxxxxxx xxxxx | The ID of the VPC. Not e This parameter is required if the Inst anceSource parameter is set to VPC IDC. _ |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| EcsRegion | String | No | cn-hangzhou | The region where the instance resides. Not e This parameter is required if the Inst anceSource parameter is set to RDS, ECS OWN, _ or VPC IDC. _ |
| Sid | String | No | dmstest | The system identifier (SID) of the database. Not e This parameter is required if the Inst anceT ype parameter is set to PostgreSQL or Oracle. |
| DataLinkName | String | No | dblink test _ | The name of the data link for cross- database queries. |
| DdlOnline | Integer | No | 2 | Specifies whether to enable the online data description language (DDL) service. This service is available only for the MySQL and PolarDB databases. 0: The service is disabled. 1: The native online DDL service takes precedence. 2: Data changes for the schema of lock-free DMS tables take precedence. |
| UseDsql | Integer | No | 1 | Specifies whether to enable the cross- database query feature for the instance. Valid values: 0: Disable the feature. 1: Enable the feature. |
| SkipTest | Boolean | No | true | Specifies whether to skip the connection test. Valid values: t rue: Skip the connection test. f alse: Perform the connection test. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | 404 | The returned error code. |
| ErrorMessage | String | The specified instance already exists. | The returned error message. |
| RequestId | String | F4E2A94B-604F- 43FF-93E7- F4EE3DCF412E | The ID of the request. Each request has a unique ID. |
| Success | Boolean | true | t rue: The request succeeded. f alse: The request failed. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=RegisterInstance &Tid=-1 &InstanceType=MySQL &InstanceSource=RDS &NetworkType=VPC &EnvType=product &Host=dmstest.rds.aliyun.com &Port=3306 &DatabaseUser=dmstest &DatabasePassword=password &InstanceAlias=Test instance &DbaUid=12345678 &SafeRule=Test &QueryTimeout=60 &ExportTimeout=600 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RegisterInstanceResponse>
      <RequestId>D4F02899-CE79-4DFD-9893-5217DA70B363</RequestId>
      <Success>true</Success>
</RegisterInstanceResponse>
```

`JSON` format `{`

```json
    "RequestId": "F4E2A94B-604F-43FF-93E7-F4EE3DCF412E",
    "Success": true
```

`}` SDK for Python example The following example shows how to add an instance that resides in VPC.

```
#coding=utf-8
from aliyunsdkcore.client import AcsClient from aliyunsdkdms_enterprise.request.v20181101.RegisterInstanceRequest import RegisterInsta nceRequest client = AcsClient(
    "<your-access-key-id>",
    "<your-access-key-secret>",
    "<your-region-id>"
```

`)`

```bash
# Example
request = RegisterInstanceRequest()
# The ID of the tenant.
request.set_Tid(1)
# The endpoint of the instance.
request.set_Host("192.168.16.113")
# The number of the port that is used to connect to the instance.
request.set_Port(3314)
# The type of the database, for example, MySQL.
request.set_InstanceType("MySQL")
# The source of the instance, for example, VPC_IDC.
request.set_InstanceSource("VPC_IDC")
# The network type, for example, VPC.
request.set_NetworkType("VPC") request.set_EnvType("PRODUCT")
# request.set_EcsInstanceId()
# The ID of the VPC to which the instance belongs.
request.set_VpcId("VPC ID of the instance")
# The region ID of the ECS instance in which the database resides, for example, cn-hangzhou
```

`.`

```bash
request.set_EcsRegion("Region ID of the ECS instance")
# request.set_Sid();
# The username of the account that is used to log on to the database.
request.set_DatabaseUser("Logon username of the database")
# The password of the account.
request.set_DatabasePassword("Logon password of the database")
# The alias of the instance. Specify an alias that helps you identify the related instance
in DMS Enterprise. request.set_InstanceAlias("Alias of the instance")
# The ID of the Apsara Stack tenant account for the database administrator (DBA) of the ins
tance. The user must first be added to DMS Enterprise by using the console or the required API operation. request.set_DbaUid(-1) request.set_SafeRule("Name of the security rule that is configured in DMS Enterprise") request.set_QueryTimeout(60) request.set_ExportTimeout(600) response = client.do_action_with_exception(request) print response
```

#### 2.3.2 ListInstances

Queries the details about instances. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListInstances | The operation that you want to perform. Set the value to List Inst ances. |
| Tid | Long | No | -1 | The ID of the tenant. |
| SearchKey | String | No | test | The keyword that is used to search for instances. |
| DbType | String | No | MySQL | The type of databases. |
| EnvType | String | No | product | The type of the environment to which instances belong. |
| InstanceSource | String | No | RDS | The source of instances. |
| NetType | String | No | VPC | The network environment of instances. For more information, see the description of the Regist erInst ance operation. |
| InstanceState | String | No | NORMAL | The status of instances. Valid values: NORMAL: Instances functions as expected. DISABLE: Instances are disabled. |
| PageNumber | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 50 | The number of entries to return on each page. Maximum value: 100. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The error code that is returned. |
| ErrorMessage | String | UnknownError | The error message that is returned. |
| InstanceList | Array of Instance |   | The instances. |
| Instance |   |   |   |
| DataLinkName | String | dblink test _ | The name of the data link for the instance. |
| DatabasePassw ord | String | ****** | The password of the account that is used to log on to the database. |
| DatabaseUser | String | dbUser | The username of the account that is used to log on to the database. |
| DbaId | String | 1 | The ID of the database administrator (DBA) for the instance. |
| DbaNickName | String | dbaName | The name of the DBA. |
| DdlOnline | Integer | 1 | The configuration of the online data description language (DDL) feature for the instance. |
| EcsInstanceId | String | xxx | The ID of the ECS instance. |
| EcsRegion | String | cn-hangzhou | The region to which the ECS instance belongs. |
| EnvType | String | product | The type of the environment to which the instance belongs. |
| ExportTimeout | Integer | 600 | The timeout period to export the instance. |
| Host | String | xxx.xxx.xxx.xxx | The endpoint of the instance. |
| InstanceAlias | String | test | The alias of the instance. |

| eveloper Guide·AP | I Reference |   | Data Managemen |
|---|---|---|---|
| Parameter | Type | Example | Description |
| InstanceId | String | 1 | The ID of the instance. |
| InstanceSource | String | RDS | The source of the instance. |
| InstanceType | String | mysql | The type of the database for the instance. |
| OwnerIdList | List | 1 | The IDs of the owners of the database. |
| OwnerNameList | List | 11 | The names of the owners of the database. |
| Port | Integer | 3306 | The number of the port that is used to connect to the instance. |
| QueryTimeout | Integer | 60 | The timeout period to query the instance. |
| SafeRuleId | String | 1 | The ID of the security rule for the instance. |
| Sid | String | test | The system identifier (SID) of the instance. |
| State | String | NORMAL | The status of the instance. |
| UseDsql | Integer | 1 | Indicates whether the cross-database query feature is enabled for the instance. |
| VpcId | String | xxx | The ID of the virtual private cloud (VPC) to which the instance belongs. |
| RequestId | String | B4B07137-F6AE- 4756-8474- 7F92BB6C4E04 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |
| TotalCount | Long | 0 | The total number of entries that are returned. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListInstances &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>7</TotalCount> <RequestId>98D35416-2B92-4CE5-8FD2-B1E61E165536</RequestId> <Success>true</Success> <InstanceList> </InstanceList>
```

`JSON` format `{`

```json
  "TotalCount": 7,
  "RequestId": "98D35416-2B92-4CE5-8FD2-B1E61E165536",
  "Success": true,
  "InstanceList": {
    "Instance": [
```

`]` `}` `}`

#### 2.3.3 GetInstance

Queries the details about an instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetInstance | The operation that you want to perform. Set the value to Get Inst ance. |
| Host | String | Yes | xxxx.mysql.rds.ali yuncs.com | The endpoint of the instance. |
| Port | Integer | Yes | 3306 | The number of the port that is used to connect to the instance. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| Sid | String | No | test | The system identifier (SID) of the instance. |

| D | eveloper Guide·API | Reference |   |   | Data Managemen | t |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The error code that is returned. |
| ErrorMessage | String | UnknownError | The error message that is returned. |
| Instance | Struct |   | The details about the instance. |
| DataLinkName | String | test | The name of the data link for the instance. |
| DatabasePassw ord | String | ****** | The logon password of the instance. |
| DatabaseUser | String | dbuser | The logon username of the instance. |
| DbaId | String | 1 | The ID of the database administrator (DBA) for the instance. You can call the ListUsers operation to obtain the ID. |
| DbaNickName | String | dbaname | The name of the DBA for the instance. |
| DdlOnline | Integer | 1 | Indicates whether the online data description language (DDL) service is enabled for the instance. |
| EcsInstanceId | String | xxx | The ID of the ECS instance. |
| EcsRegion | String | cn-hangzhou | The ID of the region in which the instance resides. |
| EnvType | String | test | The type of the environment to which the instance belongs. |
| ExportTimeout | Integer | 600 | The timeout period to export the instance. |

| ata Management |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Host | String | xxx.rwlb.rds.aliyuncs .com | The endpoint of the instance. |
| InstanceAlias | String | test | The alias of the instance. |
| InstanceId | String | 1 | The ID of the instance. |
| InstanceSource | String | RDS | The source of the instance. |
| InstanceType | String | polardb | The database type of the instance. |
| OwnerIdList | List | 88656 | The IDs of the owners of the instance. |
| OwnerNameList | List | xxx | The names of the owners of the instance. |
| Port | Integer | 3306 | The number of the port that is used to connect to the instance. |
| QueryTimeout | Integer | 60 | The timeout period to query the instance. |
| SafeRuleId | String | 1 | The ID of the security rule of the instance. |
| Sid | String | test | The SID of the instance. |
| State | String | NORMAL | The status of the instance. |
| UseDsql | Integer | 1 | Indicates whether the cross-database query feature is enabled for the instance. |
| VpcId | String | xxx | The ID of the VPC to which the instance belongs. |
| RequestId | String | 8BE73E78-76E2- 46AA-970D- A4579A16CD4A | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GetInstance &Host=xxxx.mysql.rds.aliyuncs.com &Port=3306 &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Instance>
    <SafeRuleId>1037</SafeRuleId>
    <UseDsql>1</UseDsql>
    <EcsInstanceId>pc-xxx</EcsInstanceId>
    <QueryTimeout>80</QueryTimeout>
    <Host>xxx.rwlb.rds.aliyuncs.com</Host>
    <InstanceAlias>test</InstanceAlias>
    <InstanceSource>RDS</InstanceSource>
    <InstanceId>24710</InstanceId>
    <DataLinkName>dblink_test</DataLinkName>
    <EnvType>dev</EnvType>
    <DdlOnline>0</DdlOnline>
    <VpcId>vpc-xxx</VpcId>
    <InstanceType>polardb</InstanceType>
    <DbaId>104442</DbaId>
    <Port>3306</Port>
    <DbaNickName>test[RAM user]</DbaNickName>
    <State>NORMAL</State>
    <DatabaseUser>dmstest</DatabaseUser>
    <DatabasePassword>******</DatabasePassword>
    <EcsRegion>cn-hangzhou</EcsRegion>
    <ExportTimeout>300</ExportTimeout>
</Instance> <RequestId>8BE73E78-76E2-46AA-970D-A4579A16CD4A</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "Instance": {
    "SafeRuleId": 1037,
    "UseDsql": "1",
    "EcsInstanceId": "pc-xxx",
    "QueryTimeout": 80,
    "Host": "xxx.rwlb.rds.aliyuncs.com",
    "InstanceAlias": "test",
    "InstanceSource": "RDS",
    "InstanceId": 24710,
    "DataLinkName": "dblink_test",
    "EnvType": "dev",
    "DdlOnline": 0,
    "VpcId": "vpc-xxx",
    "InstanceType": "polardb",
    "DbaId": 104442,
    "Port": 3306,
    "DbaNickName": <DbaNickName>test[RAM user]</DbaNickName>
    "State": "NORMAL",
    "DatabaseUser": "dmstest",
    "DatabasePassword": "******",
    "EcsRegion": "cn-hangzhou",
    "ExportTimeout": 300
```

`},`

```json
  "RequestId": "8BE73E78-76E2-46AA-970D-A4579A16CD4A",
  "Success": true
```

`}`

#### 2.3.4 UpdateInstance

Updates the information about a database instance and checks the connectivity of the instance. Before you call this operation to update the information about an instance, we recommend that you call the GetInstance operation to obtain the complete information about the instance. Then, you can set the required parameters based on the information that you obtain. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateInstance | The operation that you want to perform. Set the value to Updat eInst ance. |
| DatabasePasswor d | String | Yes | ****** | The password of the database account. |

| eveloper Guide·API | Reference |   |   | Data Managemen |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DatabaseUser | String | Yes | dbuser | The username of the database account. |
| DbaId | String | Yes | 1 | The ID of the database administrator (DBA) for the instance. You can call the List Users operation to query the ID. |
| EnvType | String | Yes | test | The type of the environment to which the instance belongs. |
| ExportTimeout | Integer | Yes | 600 | The timeout period to export of the instance. |
| Host | String | Yes | xxxx.mysql.rds.ali yuncs.com | The endpoint of the instance. |
| InstanceAlias | String | Yes | test | The alias of the instance. |
| InstanceId | String | Yes | 1 | The ID of the instance. You can call the Get Inst ance operation to query the ID. |
| InstanceSource | String | Yes | RDS | The source of the instance. You can call the Regist erInst ance operation to query the source. |
| InstanceType | String | Yes | MySQL | The type of the instance. You can call the Regist erInst ance operation to query the type. |
| Port | Integer | Yes | 3306 | The port of the instance. |
| QueryTimeout | Integer | Yes | 60 | The timeout period to query the instance. |
| SafeRuleId | String | Yes | 1 | The ID of the security rule of the instance. |
| Tid | Long | Yes | -1 | The ID of the tenant. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| EcsInstanceId | String | No | xxx | The ID of the ECS instance. |
| VpcId | String | No | xxx | The ID of the VPC to which the instance belongs. |
| EcsRegion | String | No | cn-hangzhou | The ID of the region in which the instance resides. |
| Sid | String | No | xxx | The system identifier (SID) of the instance. |
| DataLinkName | String | No | datalink test _ | The name of the data link for the instance. |
| DdlOnline | Integer | No | 1 | Specifies whether to enable the online data description language (DDL) service for the instance. For more information about the valid values, see the description of the Regist erInst ance operation. |
| UseDsql | Integer | No | 1 | Specifies whether to enable the cross- database query feature for the instance. |
| SkipTest | Boolean | No | true | Specifies whether to skip the connectivity check. Valid values: true: Skip the connectivity check. false: Perform the connectivity check. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The error code that is returned. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorMessage | String | UnknownError | The error message that is returned. |
| RequestId | String | E9BEBF41-4F69- 4605-A5D5- A67955173941 | The ID of the request. |
| Success | Boolean | false | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=UpdateInstance &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>E9BEBF41-4F69-4605-A5D5-A67955173941</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "E9BEBF41-4F69-4605-A5D5-A67955173941",
  "Success": true
```

`}`

#### 2.3.5 DeleteInstance

Removes a database instance from Data Management (DMS) Enterprise. This operation only removes a database instance from the DMS Enterprise console. The database instance is not disabled. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteInstance | The operation that you want to perform. Set the value to Delet eInst ance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Host | String | Yes | xxx.mysql.rds.aliy uncs.com | The endpoint of the database instance to be removed. |
| Port | Integer | Yes | 3306 | The connection port of the database instance to be removed. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| Sid | String | No | testSid | The SID of the database instance to be removed. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | B4B07137-F6AE- 4756-8474- 7F92BB6C4E04 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteInstance &Host=xxx.mysql.rds.aliyuncs.com &Port=3306 &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>B4B07137-F6AE-4756-8474-7F92BB6C4E04</RequestId> <ErrorCode>UnknownError</ErrorCode> <ErrorMessage>UnknownError</ErrorMessage> <Success>true</Success>
```

`JSON` format

```json
{"RequestId":"B4B07137-F6AE-4756-8474-7F92BB6C4E04","ErrorCode":"UnknownError","ErrorMessag e":"UnknownError","Success":"true"}
```

### 2.4 Operation logs

#### 2.4.1 GetOpLog

Queries the details about operation logs that are generated in a specified period. The administ rat or and securit y administ rat or roles of an account can all this operation. For more information about account roles, see User management. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetOpLog | The operation that you want to perform. Set the value to Get OpLog. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| StartTime | String | Yes | 2018-11-01 10:00:00 | The start of the time range to query. The time must be specified in the yyyy- MM-ddTHH:mm:ssZ format. |
| EndTime | String | Yes | 2018-11-01 11:00:00 | The end of the time range to query. The time must be specified in the yyyy- MM-ddTHH:mm:ssZ format. |
| PageNumber | Integer | Yes | 3 | The number of the page to return. Pages start from page 1. |
| PageSize | Integer | Yes | 30 | The number of entries to return on each page. Valid values: 30 50 100 |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Module | String | No | PERMISSION | The function module that specifies the type of operation logs that you want to return. If you do not set this parameter, all operation logs that are generated in the specified time range are returned. Valid values: PERMISSION: permissions OWNER: data owner SQL CONSOLE: data query _ SQL CONSOLE EXPORT : query _ _ result export DAT A CHANGE: data change _ DAT A EXPORT : data export _ SQL REVIEW: SQL review _ DT SYNC: database and table _ synchronization DT DET AIL: database and table _ details DB T ASK: task management _ INST ANCE MANAGE: instance _ management USER MANAGE: user management _ SECURIT Y RULE: security rules _ CONFIG MANAGE: configuration _ management RESOURCE AUT H: resource _ authorization ACCESS WHIT E IP: access to IP _ _ whitelists |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | 403 | The returned error code. |
| ErrorMessage | String | The specified request parameter is invalid. | The error message that is returned. |

| eveloper Guide·AP | I Reference |   | Data Managemen |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| OpLogDetails | Array of OpLogDetail |   | The details about operation logs. |
| OpLogDetail |   |   |   |
| Database | String | dmstest prod data _ _ base@dmstest.rds.. . [Test instance] | The endpoint of the database. A value is returned for this parameter only when the database type is set to LocalInst ance. Not e |
| Module | String | PERMISSION | The function module. |
| OpContent | String | Apply for permissions | The details about the operation. |
| OpTime | String | 2018-11-01 10:00:00 | The time when the operation was performed. |
| OrderId | Long | 1 | The ID of the ticket or task. Not e |
| UserId | Long | 12345678 | The ID of the Apsara Stack tenant account. |
| UserNick | String | dmstest | The name of the user. |
| RequestId | String | 47D56208-DB1D- 4FD3-BE32- 300E43185488 | The ID of the request. Each request has a unique ID. |
| Success | Boolean | true | Indicates whether the request succeeded. |
| TotalCount | Long | 22 | The total number of operation logs. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GetOpLog &Tid=-1 &StartTime=2018-11-01 10:00:00 &EndTime=2018-11-01 11:00:00 &PageNumber=3 &PageSize=30 &<Common request parameters>
```

Sample success response `XML` format

```xml
<OpLogDetails>
    <OpLogDetail>
        <OpContent>(Successful. Number of rows: 1.)SELECT (data_length + index_length) AS s
tore_capacity FROM information_schema.tables WHERE table_type = &amp;#39;BASE TABLE&amp;#39 ; AND `table_schema` = &amp;#39;dmstest_database&amp;#39; AND `table_name` = &amp;#39;multi _db_multi_tbl&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 20:04:10</OpTime>
        <Module>Data query</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(Successful. Number of rows: 1.)SELECT (data_length + index_length) AS s
tore_capacity FROM information_schema.tables WHERE table_type = &amp;#39;BASE TABLE&amp;#39 ; AND `table_schema` = &amp;#39;dmstest_database&amp;#39; AND `table_name` = &amp;#39;multi _db_multi_tbl&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 20:04:06</OpTime>
        <Module>Data query</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(Successful. Number of rows: 24.)show topology FROM multi_db_multi_tbl</
OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 20:03:55</OpTime>
        <Module>Data query</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(Successful. Number of rows: 1.)SELECT (data_length + index_length) AS s
tore_capacity FROM information_schema.tables WHERE table_type = &amp;#39;BASE TABLE&amp;#39 ; AND `table_schema` = &amp;#39;dmstest_database&amp;#39; AND `table_name` = &amp;#39;user_ log3&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 20:02:59</OpTime>
        <Module>Data query</Module>
```

`q` `y``/`

```xml
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(Successful. Number of rows: 1.)SELECT (data_length + index_length) AS s
tore_capacity FROM information_schema.tables WHERE table_type = &amp;#39;BASE TABLE&amp;#39 ; AND `table_schema` = &amp;#39;dmstest_database&amp;#39; AND `table_name` = &amp;#39;user_ log3&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 20:02:49</OpTime>
        <Module>Data query</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(Successful. Number of rows: 1.)show CREATE TABLE user_log3</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:34:05</OpTime>
        <Module>Data query</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(Successful. Number of rows: 9.)SELECT `TABLE_NAME` FROM information_sch
ema.tables WHERE TABLE_TYPE = &amp;#39;BASE TABLE&amp;#39; AND table_schema = &amp;#39;dmst est_database&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:33:54</OpTime>
        <Module>Data query</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>Creates an SQL task. Task ID: 5486.</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:26:57</OpTime>
        <Module>Task management</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>Creates an SQL task. Task ID: 5485.</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:23:55</OpTime>
        <Module>Task management</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>Creates an SQL task. Task ID: 5484.</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:23:30</OpTime>
        <Module>Task management</Module>
    </OpLogDetail>
```

```xml
    <OpLogDetail>
        <OpContent>Creates an SQL task. Task ID: 5483.</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:23:11</OpTime>
        <Module>Task management</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(Successful. Number of rows: 1.)show CREATE TABLE multi_db_single_tbl</O
pContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:22:30</OpTime>
        <Module>SQL_CONSOLE</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(Successful. Number of rows: 2.)SELECT `TABLE_NAME` FROM information_sch
ema.tables WHERE TABLE_TYPE = &amp;#39;BASE TABLE&amp;#39; AND table_schema = &amp;#39;dmst est_database&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:22:15</OpTime>
        <Module>Data query</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(Successful. Number of rows: 2.)SELECT `TABLE_NAME` FROM information_sch
ema.tables WHERE TABLE_TYPE = &amp;#39;BASE TABLE&amp;#39; AND table_schema = &amp;#39;dmst est_database&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:19:31</OpTime>
        <Module>Data query</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>Creates an SQL task. Task ID: 5482.</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:19:25</OpTime>
        <Module>Task management</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(Successful. Number of rows: 1.)SELECT `TABLE_NAME` FROM information_sch
ema.tables WHERE TABLE_TYPE = &amp;#39;BASE TABLE&amp;#39; AND table_schema = &amp;#39;dmst est_database&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:18:57</OpTime>
        <Module>Data query</Module>
```

```xml
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>Creates an SQL task. Task ID: 5481.</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:18:46</OpTime>
        <Module>Task management</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(Successful. Number of rows: 0.)SELECT `TABLE_NAME` FROM information_sch
ema.tables WHERE TABLE_TYPE = &amp;#39;BASE TABLE&amp;#39; AND table_schema = &amp;#39;dmst est_database&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:04:13</OpTime>
        <Module>Data query</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(Successful. Number of rows: 0.)SELECT `TABLE_NAME` FROM information_sch
ema.tables WHERE TABLE_TYPE = &amp;#39;BASE TABLE&amp;#39; AND table_schema = &amp;#39;dmst est_database&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:04:08</OpTime>
        <Module>Data query</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(Successful. Number of rows: 0.)SELECT `TABLE_NAME` FROM information_sch
ema.tables WHERE TABLE_TYPE = &amp;#39;BASE TABLE&amp;#39; AND table_schema = &amp;#39;dmst est_database&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 12:11:41</OpTime>
        <Module>Data query</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>The administrator or DBA changes the owner of a database. Database name:
dmstest_database@dmstest.rds...(test)</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 12:11:14</OpTime>
        <Module>Data owner</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>The administrator or DBA changes the owner of a database. Database name:
dmstest_prod_database@dmstest.rds...(test)</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_prod_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
OTi 20181122121107/OTi
```

```xml
        <OpTime>2018-11-22 12:11:07</OpTime>
        <Module>Data owner</Module>
    </OpLogDetail>
</OpLogDetails> <TotalCount>22</TotalCount> <RequestId>47D56208-DB1D-4FD3-BE32-300E43185488</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
 "OpLogDetails": {
  "OpLogDetail": [{
   "OpContent": "(Successful. Number of rows: 1.)SELECT (data_length + index_length) AS sto
re_capacity FROM information_schema.tables WHERE table_type = &#39;BASE TABLE&#39; AND `tab le_schema` = &#39;dmstest_database&#39; AND `table_name` = &#39;multi_db_multi_tbl&#39;",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 20:04:10",
   "Module": "Data query"
  }, {
   "OpContent": "(Successful. Number of rows: 1.)SELECT (data_length + index_length) AS sto
re_capacity FROM information_schema.tables WHERE table_type = &#39;BASE TABLE&#39; AND `tab le_schema` = &#39;dmstest_database&#39; AND `table_name` = &#39;multi_db_multi_tbl&#39;",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 20:04:06",
   "Module": "Data query"
  }, {
   "OpContent": "(Successful. Number of rows: 24.)show topology FROM multi_db_multi_tbl",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 20:03:55",
   "Module": "Data query"
  }, {
   "OpContent": "(Successful. Number of rows: 1.)SELECT (data_length + index_length) AS sto
re_capacity FROM information_schema.tables WHERE table_type = &#39;BASE TABLE&#39; AND `tab le_schema` = &#39;dmstest_database&#39; AND `table_name` = &#39;user_log3&#39;",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 20:02:59",
   "Module": "Data query"
  }, {
   "OpContent": "(Successful. Number of rows: 1.)SELECT (data_length + index_length) AS sto
re_capacity FROM information_schema.tables WHERE table_type = &#39;BASE TABLE&#39; AND `tab le_schema` = &#39;dmstest_database&#39; AND `table_name` = &#39;user_log3&#39;",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 20:02:49",
```

```json
   "Module": "Data query"
  }, {
   "OpContent": "(Successful. Number of rows: 1.)show CREATE TABLE user_log3",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 14:34:05",
   "Module": "Data query"
  }, {
   "OpContent": "(Successful. Number of rows: 9.)SELECT `TABLE_NAME` FROM information_schem
a.tables WHERE TABLE_TYPE = &#39;BASE TABLE&#39; AND table_schema = &#39;dmstest_database&# 39;",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 14:33:54",
   "Module": "Data query"
  }, {
   "OpContent": "Creates an SQL task. Task ID: 5486.",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 14:26:57",
   "Module": "Task management"
  }, {
   "OpContent": "Creates an SQL task. Task ID: 5485.",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 14:23:55",
   "Module": "Task management"
  }, {
   "OpContent": "Creates an SQL task. Task ID: 5484.",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 14:23:30",
   "Module": "Task management"
  }, {
   "OpContent": "Creates an SQL task. Task ID: 5483.",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 14:23:11",
   "Module": "Task management"
  }, {
   "OpContent": "(Successful. Number of rows:1)show CREATE TABLE multi_db_single_tbl",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 14:22:30",
   "Module": "Data query"
  }, {
   "OpContent": "(Successful. Number of rows: 2.)SELECT `TABLE_NAME` FROM information_schem
```

```json
a.tables WHERE TABLE_TYPE = &#39;BASE TABLE&#39; AND table_schema = &#39;dmstest_database&# 39;",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 14:22:15",
   "Module": "Data query"
  }, {
   "OpContent": "(Successful. Number of rows: 2.)SELECT `TABLE_NAME` FROM information_schem
a.tables WHERE TABLE_TYPE = &#39;BASE TABLE&#39; AND table_schema = &#39;dmstest_database&# 39;",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 14:19:31",
   "Module": "Data query"
  }, {
   "OpContent": "Creates an SQL task. Task ID: 5482.",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 14:19:25",
   "Module": "Task management"
  }, {
   "OpContent": "(Successful. Number of rows: 1.)SELECT `TABLE_NAME` FROM information_schem
a.tables WHERE TABLE_TYPE = &#39;BASE TABLE&#39; AND table_schema = &#39;dmstest_database&# 39;",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 14:18:57",
   "Module": "Data query"
  }, {
   "OpContent": "Creates an SQL task. Task ID: 5481.",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 14:18:46",
   "Module": "Task management"
  }, {
   "OpContent": "(Successful. Number of rows: 0.)SELECT `TABLE_NAME` FROM information_schem
a.tables WHERE TABLE_TYPE = &#39;BASE TABLE&#39; AND table_schema = &#39;dmstest_database&# 39;",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 14:04:13",
   "Module": "Data query"
  }, {
   "OpContent": "(Successful. Number of rows: 0.)SELECT `TABLE_NAME` FROM information_schem
a.tables WHERE TABLE_TYPE = &#39;BASE TABLE&#39; AND table_schema = &#39;dmstest_database&# 39;",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
```

`"U`

```
Id" 12345678
```

```json
   "UserId": 12345678,
   "OpTime": "2018-11-22 14:04:08",
   "Module": "Data query"
  }, {
   "OpContent": "(Successful. Number of rows: 0.)SELECT `TABLE_NAME` FROM information_schem
a.tables WHERE TABLE_TYPE = &#39;BASE TABLE&#39; AND table_schema = &#39;dmstest_database&# 39;",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 12:11:41",
   "Module": "Data query"
  }, {
   "OpContent": "The administrator or DBA edits the database owner. Database name: dmstest_
prod_database@dmstest.rds...",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 12:11:14",
   "Module": "Data owner"
  }, {
   "OpContent": "The administrator or DBA edits the database owner. Database name: dmstest_
prod_database@dmstest.rds...",
   "UserNick": "dmstest",
   "Database": "dmstest_prod_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 12:11:07",
   "Module": "Data owner"
```

`}]` `},`

```json
 "TotalCount": 22,
 "RequestId": "47D56208-DB1D-4FD3-BE32-300E43185488",
 "Success": true
```

`}` SDK example For more information about how to use the SDK, see the Alibaba Cloud SDK for Python. Example:

```
from aliyunsdkcore.client import AcsClient from aliyunsdkdms_enterprise.request.v20181101.GetOpLogRequest import GetOpLogRequest client = AcsClient(
    "<your-access-key-id>",
   "<your-access-key-secret>",
   "<your-region-id>"
```

`)`

```
request = GetOpLogRequest() request.set_Tid("Enter the tenant ID of your enterprise") request.set_StartTime("2018-11-20 00:00:00") request.set_EndTime("2018-11-23 00:00:00") request.set_PageNumber(1) request.set_PageSize(50) response = client.do_action_with_exception(request) print response
```

### 2.5 Approval processes

#### 2.5.1 ListWorkFlowTemplates

Queries the details about approval templates. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListWorkFlowTe mplates | The operation that you want to perform. Set the value to List WorkFlowT emplat es. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| SearchName | String | No | Admin | The name that is used to search for approval templates. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |

| D | eveloper Guide·AP | I Reference |   | Data Managemen | t |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 41067071-0243- 4AAB-B3CF- 4DE6D54F53B4 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |
| WorkFlowTemp lates | Array of WorkFlowTemp late |   | The approval templates. |
| WorkFlowTemp late |   |   |   |
| Comment | String | test | The remarks. |
| CreateUserId | Long | 1234 | The ID of the creator. |
| Enabled | String | Y | Indicates whether the approval template is enabled. Valid values: Y: enabled N: disabled |
| IsSystem | Integer | 1 | Indicates whether the approval template is predefined by the system. Valid values: 1: The approval template is predefined by the system. 0: The approval template is not predefined by the system. |
| TemplateId | Long | 12345 | The ID of the approval template. |
| TemplateName | String | Admin | The name of the approval template. |
| WorkflowNode s | Array of WorkflowNode |   | The details about approval nodes. |
| WorkflowNode |   |   |   |
| Comment | String | test | The remarks. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| CreateUserId | Long | 1234 | The ID of the creator. |
| NodeId | Long | 123 | The ID of the approval node. |
| NodeName | String | test | The name of the approval node. |
| NodeType | String | SYS | The type of the approval node. Valid values: SYS: The approval node is predefined by the system. USER LIST: The approval node is created _ by a user. |
| Position | Integer | 1 | The order. |
| TemplateId | Long | 12345 | The ID of the approval template. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListWorkFlowTemplates &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>41067071-0243-4AAB-B3CF-4DE6D54F53B4</RequestId> <Success>true</Success> <WorkFlowTemplates>
    <WorkFlowTemplate>
        <Comment>The system-defined approval workflow. Only an administrator is included in
the approval workflow to review requests.</Comment>
        <WorkFlowNodes>
            <WorkFlowNode>
                <Comment>The system-defined node that is dynamically generated. Requests ar
e reviewed by an administrator.</Comment>
                <NodeName>Admin</NodeName>
                <Position>0</Position>
                <NodeType>SYS</NodeType>
                <NodeId>3763</NodeId>
                <TemplateId>6243</TemplateId>
            </WorkFlowNode>
        </WorkFlowNodes>
```

`<T`

```
ltN >Adi</T ltN
```

`>`

```xml
        <TemplateName>Admin</TemplateName>
        <Enabled>Y</Enabled>
        <IsSystem>1</IsSystem>
        <TemplateId>6243</TemplateId>
    </WorkFlowTemplate>
    <WorkFlowTemplate>
        <Comment>The system-defined approval workflow. Each request must be reviewed by the
data owner, DBA, and admin in sequence.</Comment>
        <WorkflowNodes>
            <WorkFlowNode>
                <Comment>The system-defined node that is dynamically generated. The owner o
f the resources that you want to manage is required to review the related requests.</Commen
```

`t>`

```xml
                <NodeName>Owner</NodeName>
                <Position>0</Position>
                <NodeType>SYS</NodeType>
                <NodeId>3762</NodeId>
                <TemplateId>6244</TemplateId>
            </WorkFlowNode>
            <WorkFlowNode>
                <Comment>The system-defined node that is dynamically generated. The DBA of
the resources that you want to manage is required to review the related requests.</Comment>
                <NodeName>DBA</NodeName>
                <Position>0</Position>
                <NodeType>SYS</NodeType>
                <NodeId>3761</NodeId>
                <TemplateId>6244</TemplateId>
            </WorkFlowNode>
            <WorkFlowNode>
                <Comment>The system-defined node that is dynamically generated. Requests ar
e reviewed by an administrator.</Comment>
                <NodeName>Admin</NodeName>
                <Position>0</Position>
                <NodeType>SYS</NodeType>
                <NodeId>3763</NodeId>
                <TemplateId>6244</TemplateId>
            </WorkFlowNode>
        </WorkflowNodes>
        <TemplateName>Owner--&gt;DBA--&gt;Admin</TemplateName>
        <Enabled>Y</Enabled>
        <IsSystem>1</IsSystem>
        <TemplateId>6244</TemplateId>
    </WorkFlowTemplate>
</WorkFlowTemplates>
```

`JSON` format `{`

```json
  "RequestId": "41067071-0243-4AAB-B3CF-4DE6D54F53B4",
  "Success": true,
  "WorkFlowTemplates": {
    "WorkFlowTemplate": [
```

`{`

```json
        "Comment": "The system-defined approval workflow. Only an administrator is included
```

```json
in the approval workflow to review requests.",
        "WorkFlowNodes": {
          "WorkFlowNode": [
```

`{`

```json
              "Comment": "The system-defined node that is dynamically generated. Requests a
re reviewed by an administrator.",
              "NodeName": "Admin",
              "Position": 0,
              "NodeType": "SYS",
              "NodeId": 3763,
              "TemplateId": 6243
```

`}` `]` `},`

```json
        "TemplateName": "Admin",
        "Enabled": "Y",
        "IsSystem": 1,
        "TemplateId": 6243
```

`},` `{`

```json
        "Comment": "The system-defined approval workflow. Each request must be reviewed by
the data owner, DBA, and admin in sequence.",
        "WorkflowNodes": {
          "WorkFlowNode": [
```

`{`

```json
              "Comment": ">The system-defined node that is dynamically generated. The owner
of the resources that you want to manage is required to review the related requests.",
              "NodeName": "Owner",
              "Position": 0,
              "NodeType": "SYS",
              "NodeId": 3762,
              "TemplateId": 6244
```

`},` `{`

```json
              "Comment": "The system-defined node that is dynamically generated. The DBA of
the resources that you want to manage is required to review the related requests.",
              "NodeName": "DBA",
              "Position": 0,
              "NodeType": "SYS",
              "NodeId": 3761,
              "TemplateId": 6244
```

`},` `{`

```json
              "Comment": "The system-defined node that is dynamically generated. Requests a
re reviewed by an administrator.",
              "NodeName": "Admin",
              "Position": 0,
              "NodeType": "SYS",
              "NodeId": 3763,
              "TemplateId": 6244
```

`}` `]` `},`

```json
        "TemplateName": "Owner-->DBA-->Admin",
```

```json
        "Enabled": "Y",
        "IsSystem": 1,
        "TemplateId": 6244
```

`}` `]` `}` `}`

#### 2.5.2 ListWorkFlowNodes

Queries the details about approval nodes. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListWorkFlowNod es | The operation that you want to perform. Set the value to List WorkFlowNodes. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| SearchName | String | No | admin | The name that is used to search for approval nodes. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | CFD8FE00-36D9- 4C1B-940D- 65A7B73D9066 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |
| WorkflowNode s | Array of WorkflowNode |   | The details about approval nodes. |
| WorkflowNode |   |   |   |

| Data Management |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| AuditUsers | Array of AuditUser |   | The details about approvers. |
| AuditUser |   |   |   |
| NickName | String | test | The name of the approver. |
| RealName | String | test | The real name of the approver. |
| UserId | Long | 123 | The ID of the approver. The ID is different from the ID of the Apsara Stack tenant account of the approver. |
| Comment | String | test | The remarks. |
| CreateUserId | Long | 123 | The ID of the creator. The ID is different from the ID of the Apsara Stack tenant account of the creator. |
| CreateUserNick Name | String | test | The name of the creator. |
| NodeId | Long | 123 | The ID of the node. |
| NodeName | String | test | The name of the node. |
| NodeType | String | SYS | The type of the node. Valid values: SYS: The node is pre-defined by the system. USER LIST: The node is created by a user. _ |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListWorkFlowNodes &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<WorkFlowNodes>
    <WorkflowNode>
        <Comment>This is a system-defined node that is dynamically generated. All requests
are reviewed by an administrator.</Comment>
        <NodeName>Admin</NodeName>
        <NodeType>SYS</NodeType>
        <NodeId>3763</NodeId>
        <AuditUsers>
        </AuditUsers>
    </WorkflowNode>
</WorkFlowNodes> <RequestId>CFD8FE00-36D9-4C1B-940D-65A7B73D9066</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "WorkFlowNodes": {
    "WorkflowNode": [
```

`{`

```json
        "Comment": "This is a system-defined node that is dynamically generated. All reques
ts are reviewed by an administrator.",
        "NodeName": "Admin",
        "NodeType": "SYS",
        "NodeId": 3763,
        "AuditUsers": {
          "AuditUser": []
```

`}` `}` `]` `},`

```json
  "RequestId": "CFD8FE00-36D9-4C1B-940D-65A7B73D9066",
  "Success": true
```

`}`

### 2.6 Metadata of databases and tables

tables

#### 2.6.1 SearchDatabase

Queries the details about databases. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SearchDatabase | The operation that you want to perform. Set the value to SearchDat abase. |
| PageNumber | Integer | Yes | 1 | The number of the page to return. |
| SearchKey | String | Yes | testdb | The keyword that is used to search for databases. |
| Tid | Long | Yes | 1 | The ID of the tenant. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| EnvType | String | No | product | The environment of the database. |
| SearchRange | String | No | HAS PERMSSION _ | The range of databases. Valid values: HAS PERMSSION: databases on _ which the current user has permissions OWNER: databases that are owned by the current user MY FOCUS: databases that are _ followed by the current user UNKNOWN: all databases |
| SearchTarget | String | No | SINGLE DB _ | The category of databases. Valid values: DB: all databases. SINGLE DB: single databases. _ LOGIC DB: logical databases. _ |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DbType | String | No | MySQL | The type of databases. Valid values: MySQL SQLServer Post greSQL Oracle DRDS OceanBase Mongo Redis |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | E0D21075-CD3E- 4D98-8264- FD8AD04A63B6 | The ID of the request. |
| SearchDatabas eList | Array of SearchDatabas e |   | The details about databases. |
| SearchDatabas e |   |   |   |
| Alias | String | test | The alias of the database. |
| DatabaseId | String | 1 | The ID of the database. |
| DatalinkName | String | datalink name _ | The name of the data link for the database. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DbType | String | mysql | The type of the database. Valid values: MySQL SQLServer Post greSQL Oracle DRDS OceanBase Mongo Redis |
| DbaId | String | 1 | The ID of the database administrator (DBA) for the database. |
| Encoding | String | utf8 | The encoding of the database. |
| EnvType | String | product | The type of the environment to which the database belongs. |
| Host | String | xxx.xxx.xxx.xxx | The endpoint of the instance to which the database belongs. |
| Logic | Boolean | false | Indicates whether the database is a logical database. Valid values: t rue: The database is a logical database. f alse: The database is not a logical database. |
| OwnerIdList | List | 1 | The IDs of the owners of the database. |
| OwnerNameList | List | user1 | The names of the owners of the database. |
| Port | Integer | 3306 | The port number of the instance to which the database belongs. |
| SchemaName | String | test | The name of the database. |
| SearchName | String | test@xxx.xxx.xxx.xxx :3306 | The name that is used to search for the database. |

| Developer Guide·AP | I Reference |   | Data Managemen |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Sid | String | testSid | The system identifier (SID) of the instance to which the database belongs. |
| TotalCount | Long | 1 | The total number of entries that are returned. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SearchDatabase &PageNumber=1 &SearchKey=testdb &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>1</TotalCount> <RequestId>E0D21075-CD3E-4D98-8264-FD8AD04A63B6</RequestId> <SearchDatabaseList>
    <SearchDatabase>
        <Encoding>utf8mb4</Encoding>
        <Host>pc-xxx.mysql.polardb.rds.aliyuncs.com</Host>
        <DbType>polardb</DbType>
        <EnvType>dev</EnvType>
        <OwnerIdList>
            <OwnerIds>88653</OwnerIds>
            <OwnerIds>88656</OwnerIds>
            <OwnerIds>104442</OwnerIds>
        </OwnerIdList>
        <Logic>false</Logic>
        <DbaId>88653</DbaId>
        <OwnerNameList>
            <OwnerNames>dmstest</OwnerNames>
            <OwnerNames>xx</OwnerNames>
            <OwnerNames>xx[RAM user]</OwnerNames>
        </OwnerNameList>
        <Port>3306</Port>
        <DatabaseId>117567</DatabaseId>
        <Alias>xx offline database</Alias>
        <SearchName>xxx@pc-xxx.mysql.polardb.rds.aliyuncs.com:3306[xx offline database]</Se
archName>
        <DatalinkName>dblink_38</DatalinkName>
        <SchemaName>xxx_0000</SchemaName>
    </SearchDatabase>
</SearchDatabaseList> <Success>true</Success>
```

`JSON` format `{`

```json
  "TotalCount": 1,
  "RequestId": "E0D21075-CD3E-4D98-8264-FD8AD04A63B6",
  "SearchDatabaseList": {
    "SearchDatabase": [
```

`{`

```json
        "Encoding": "utf8mb4",
        "Host": "pc-xxx.mysql.polardb.rds.aliyuncs.com",
        "DbType": "polardb",
        "EnvType": "dev",
        "OwnerIdList": {
          "OwnerIds": [
            88653,
            88656,
            104442
```

`]` `},`

```json
        "Logic": false,
        "DbaId": 88653,
        "OwnerNameList": {
          "OwnerNames": [
            "dmstest",
            "xx",
            "xx[RAM user]"
```

`]` `},`

```json
        "Port": 3306,
        "DatabaseId": 117567,
        "Alias": "xx offline database",
        "SearchName": "xxx@pc-xxx.mysql.polardb.rds.aliyuncs.com:3306[xx offline database]"
```

`,`

```json
        "DatalinkName": "dblink_38",
        "SchemaName": "xxx_0000"
```

`}` `]` `},`

```json
  "Success": true
```

`}`

#### 2.6.2 SearchTable

Queries the details about tables. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SearchTable | The operation that you want to perform. Set the value to SearchT able. |

| D | ata Management |   |   |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Tid | Long | No | 1 | The ID of the tenant. |
| SearchKey | String | No | test | The keyword that is used to search for tables. |
| PageNumber | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| EnvType | String | No | PRODUCT | The type of the environment to which the database belongs. |
| SearchTarget | String | No | LOGIC TABLE _ | The type of tables to be queried. Valid values: T ABLE: all tables SINGLE T ABLE: physical tables _ LOGIC T ABLE: logical tables _ |
| SearchRange | String | No | OWNER | The permission that is required on tables to be queried. Valid values: HAS PERMSSION: tables on which _ the current user has permissions. OWNER: tables that are owned by the current user. MY FOCUS: tables that are _ followed by the current user. UNKNOWN: all tables. |
| DbType | String | No | MySQL | The type of the database. Valid values: MySQL SQLServer Post greSQL Oracle DRDS OceanBase Mongo Redis |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ReturnGuid | Boolean | No | false | Specifies whether to return the globally unique identifier (GUID) of each table. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | 1489257F-1B5D- 4B5B-89EF- 923C12CEEBD1 | The ID of the request. |
| SearchTableList | Array of SearchTable |   | The details about the tables. |
| SearchTable |   |   |   |
| DBSearchName | String | test | The name that is used to search for the database to which the table belongs. |
| DatabaseId | String | 1 | The ID of the database to which the table belongs. |
| DbName | String | test | The name of the database. |
| DbType | String | mysql | The type of the database. Valid values: MySQL SQLServer Post greSQL Oracle DRDS OceanBase Mongo Redis |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Description | String | test | The description. |
| Encoding | String | utf8 | The encoding of the table. |
| Engine | String | innodb | The engine of the table. |
| EnvType | String | test | The type of the environment. |
| Logic | Boolean | false | Indicates whether the table is a logical table. Valid values: t rue: The table is a logical table. f alse: The table is not a logical table. |
| OwnerIdList | List | 1 | The IDs of the owners of the table. |
| OwnerNameList | List | user | The names of the owners of the table. |
| TableGuid | String | IDB L 9032.db- _ _ test.yuyang test _ | The GUID of the table. |
| TableId | String | 1 | The ID of the table. |
| TableName | String | test table _ | The name of the table. |
| TableSchemaN ame | String | test@xxx.xxx.xxx.xxx :3306 | The name of the database to which the table belongs. |
| Success | Boolean | true | Indicates whether the request succeeded. |
| TotalCount | Long | 1 | The total number of entries that are returned. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SearchTable &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SearchTableList>
    <SearchTable>
        <TableGuid>IDB_L_9032.db-test.yuyang_test</TableGuid>
        <Logic>false</Logic>
        <TableSchemaName>xxx_0000</TableSchemaName>
        <OwnerNameList>
            <OwnerNames>xxx</OwnerNames>
            <OwnerNames>xxx</OwnerNames>
            <OwnerNames>xxx</OwnerNames>
        </OwnerNameList>
        <DBSearchName>xxx_0000@pc-xxx.mysql.polardb.rds.aliyuncs.com:3306[xxx offline datab
ase]</DBSearchName>
        <DatabaseId>117567</DatabaseId>
        <Encoding>utf8mb4</Encoding>
        <TableName>test_aaaa</TableName>
        <OwnerIdList>
            <OwnerIds>88653</OwnerIds>
            <OwnerIds>88656</OwnerIds>
            <OwnerIds>104442</OwnerIds>
        </OwnerIdList>
        <EnvType>dev</EnvType>
        <Engine>InnoDB</Engine>
        <TableId>18396767</TableId>
    </SearchTable>
</SearchTableList> <TotalCount>1</TotalCount> <RequestId>1489257F-1B5D-4B5B-89EF-923C12CEEBD1</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "SearchTableList": {
    "SearchTable": [
```

`{`

```json
        "TableGuid" : "IDB_L_9032.db-test.yuyang_test",
        "Logic": false,
        "TableSchemaName": "xxx_0000",
        "OwnerNameList": {
          "OwnerNames": [
            "xxx",
            "xxx",
            "xxx"
```

`]` `},`

```json
        "DBSearchName": "xxx_0000@pc-xxx.mysql.polardb.rds.aliyuncs.com:3306[xxx offline da
tabase]",
        "DatabaseId": 117567,
        "Encoding": "utf8mb4",
        "TableName": "test_aaaa",
        "OwnerIdList": {
          "OwnerIds": [
            88653,
            88656,
            104442
```

`]` `},`

```json
        "EnvType": "dev",
        "Engine": "InnoDB",
        "TableId": 18396767
```

`}` `]` `},`

```json
  "TotalCount": 1,
  "RequestId": "1489257F-1B5D-4B5B-89EF-923C12CEEBD1",
  "Success": true
```

`}`

#### 2.6.3 ListDatabases

Queries the details of databases in an instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListDatabases | The operation that you want to perform. Set the value to List Dat abases. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| InstanceId | String | Yes | 1 | The instance ID. You can obtain the instance ID from the instance information that is returned by the List Inst ances operation. The instance ID is different from the ID of an ApsaraDB RDS instance. |
| PageNumber | Integer | Yes | 1 | The number of the page to return. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DatabaseList | Array of Database |   | The details of databases. |
| Database |   |   |   |
| CatalogName | String | 1 | The name of the database catalog. Not e If the database type is PostgreSQL, the value indicates the name of the PostgreSQL database. |
| DatabaseId | String | 1 | The ID of the database. |
| DbType | String | mysql | The type of the database. |
| DbaId | String | 1 | The ID of the DBA to which the database belongs. |
| DbaName | String | dba user _ | The name of the DBA to which the database belongs. |

| ata Management |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Encoding | String | utf-8 | The encoding of the database. |
| EnvType | String | dev | The type of the environment to which the database belongs. |
| Host | String | xxx.xxx.xxx.xxx | The endpoint of the instance. |
| InstanceId | String | 1 | The ID of the instance to which the database belongs. |
| OwnerIdList | List | 1 | The IDs of database owners. |
| OwnerNameList | List | owner name _ | The names of database owners. |
| Port | Integer | 3306 | The connection port of the instance. |
| SchemaName | String | test | The name of the database. |
| SearchName | String | test@xxx.xxx.xxx.xxx :3306 | The name that is used to search for the database. |
| Sid | String | test | The ID of the instance to which the database belongs. |
| State | String | NORMAL | The status of the database. Valid values: NORMAL: The database is normal. DISABLE: The database is disabled. OFFLINE: The database is unpublished. NOT EXIST: The database does not exist. _ |
| ErrorCode | String | UnknownError | The error code that is returned. |
| ErrorMessage | String | UnknownError | The error message that is returned. |
| RequestId | String | 5541CDA6-F674- 435C-81BD- 40C2FB926CE3 | The ID of the request. |

| Developer Guide·AP | I Reference |   | Data Managemen |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request succeeds. |
| TotalCount | Long | 1 | The total number of databases that belong to the instance. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListDatabases &InstanceId=1 &PageNumber=1 &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>1</TotalCount> <RequestId>5541CDA6-F674-435C-81BD-40C2FB926CE3</RequestId> <Success>true</Success> <DatabaseList>
    <Database>
        <Encoding>utf8</Encoding>
        <Host>pc-xxx.rwlb.rds.aliyuncs.com</Host>
        <InstanceId>24710</InstanceId>
        <DbType>polardb</DbType>
        <EnvType>product</EnvType>
        <OwnerIdList>
            <OwnerIds>88653</OwnerIds>
        </OwnerIdList>
        <DbaId>104442</DbaId>
        <OwnerNameList>
            <OwnerNames>dmstest</OwnerNames>
        </OwnerNameList>
        <Port>3306</Port>
        <DatabaseId>116366</DatabaseId>
        <State>NORMAL</State>
        <SearchName>xxx_test@pc-xxx.rwlb.rds.aliyuncs.com:3306【xxx_test】</SearchName>
        <DbaName>xxx[RAM user]</DbaName>
        <SchemaName>xxx_test</SchemaName>
    </Database>
</DatabaseList>
```

`JSON` format `{`

```json
  "TotalCount": 1,
  "RequestId": "5541CDA6-F674-435C-81BD-40C2FB926CE3",
  "Success": true,
  "DatabaseList": {
    "Database": [
```

`{`

```json
        "Encoding": "utf8",
        "Host": "pc-xxx.rwlb.rds.aliyuncs.com",
        "InstanceId": 24710,
        "DbType": "polardb",
        "EnvType": "product",
        "OwnerIdList": {
          "OwnerIds": [
            88653
```

`]` `},`

```json
        "DbaId": 104442,
        "OwnerNameList": {
          "OwnerNames": [
            "dmstest"
```

`]` `},`

```json
        "Port": 3306,
        "DatabaseId": 116366,
        "State": "NORMAL",
        "SearchName": "xxx_test@pc-xxx.rwlb.rds.aliyuncs.com:3306【xxx_test】",
        "DbaName": "xxx[RAM user]",
        "SchemaName": "xxx_test"
```

`}` `]` `}` `}`

#### 2.6.4 ListLogicDatabases

Queries the details about logical databases. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListLogicDatabas es | The operation that you want to perform. Set the value to List LogicDat abases. |
| PageNumber | Integer | Yes | 1 | The number of the page to return. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Tid | Long | Yes | -1 | The ID of the tenant. |
| PageSize | Integer | No | 50 | The number of entries to return on each page. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The error code that is returned. |
| ErrorMessage | String | UnknownError | The error message that is returned. |
| LogicDatabaseL ist | Array of LogicDatabase |   | The details about logical databases. |
| LogicDatabase |   |   |   |
| DatabaseId | String | 1 | The ID of the logical database. |
| DbType | String | mysql | The type of the logical database. |
| EnvType | String | test | The type of the environment to which the logical database belongs. |
| Logic | Boolean | true | Indicates whether the database is a logical database. The value is set to true. |
| OwnerIdList | List | 1 | The IDs of the owners of the logical database. |
| OwnerNameList | List | owner name _ | The names of the owners of the logical database. |
| SchemaName | String | logic db _ | The name of the logical database. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| SearchName | String | loigc db _ | The name that is used to search for the logical database. |
| RequestId | String | BAD154C0-DA38- 48FA-97AB- E72912EEAA24 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |
| TotalCount | Long | 13 | The total number of logical databases. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListLogicDatabases &PageNumber=1 &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>13</TotalCount> <RequestId>BAD154C0-DA38-48FA-97AB-E72912EEAA24</RequestId> <LogicDatabaseList>
    <LogicDatabase>
        <Logic>true</Logic>
        <OwnerNameList>
            <OwnerNames>xxx</OwnerNames>
        </OwnerNameList>
        <DatabaseId>257</DatabaseId>
        <SearchName>test_db(This is a logical database.)</SearchName>
        <DbType>mysql</DbType>
        <OwnerIdList>
            <OwnerIds>88653</OwnerIds>
        </OwnerIdList>
        <EnvType>dev</EnvType>
        <SchemaName>test_db</SchemaName>
    </LogicDatabase>
    <LogicDatabase>
        <Logic>true</Logic>
        <OwnerNameList>
            <OwnerNames>xxx</OwnerNames>
            <OwnerNames>xxx</OwnerNames>
            <OwnerNames>xxx</OwnerNames>
        </OwnerNameList>
        <DatabaseId>258</DatabaseId>
        <SearchName>xxx_test(This is a logical database.)</SearchName>
        <DbType>mysql</DbType>
        <OwnerIdList>
            <OwnerIds>88656</OwnerIds>
            <OwnerIds>88653</OwnerIds>
            <OwnerIds>101252</OwnerIds>
        </OwnerIdList>
        <EnvType>product</EnvType>
        <SchemaName>idb_test</SchemaName>
    </LogicDatabase>
</LogicDatabaseList> <Success>true</Success>
```

`JSON` format `{`

```json
  "TotalCount": 13,
  "RequestId": "BAD154C0-DA38-48FA-97AB-E72912EEAA24",
  "LogicDatabaseList": {
    "LogicDatabase": [
```

`{`

```json
        "Logic": true,
        "OwnerNameList": {
          "OwnerNames": [
            "xxx"
```

`]` `},`

```json
        "DatabaseId": 257,
        "SearchName": "test_db(This is a logical database)",
        "DbType": "mysql",
        "OwnerIdList": {
          "OwnerIds": [
            88653
```

`]` `},`

```json
        "EnvType": "dev",
        "SchemaName": "test_db"
```

`},` `{`

```json
        "Logic": true,
        "OwnerNameList": {
          "OwnerNames": [
            "xxx",
            "xxx",
            "xxx"
```

`]` `},`

```json
        "DatabaseId": 258,
        "SearchName": "xxx_test(This is a logical database)",
        "DbType": "mysql",
        "OwnerIdList": {
          "OwnerIds": [
            88656,
            88653,
            101252
```

`]` `},`

```json
        "EnvType": "product",
        "SchemaName": "idb_test"
```

`}` `]` `},`

```json
  "Success": true
```

`}`

#### 2.6.5 ListTables

Queries the details of tables in a database. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListTables | The operation that you want to perform. Set the value to List T ables. |
| DatabaseId | String | Yes | 1 | The ID of the database. |
| PageNumber | Integer | Yes | 1 | The number of the page to return. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| SearchName | String | No | test | The keyword that is used to query tables. Prefix match is used. |
| ReturnGuid | Boolean | No | true | Specifies whether to return the GUID of the table. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | B16FB618-5E96- 4FFD-BB0D- 490C890A4030 | The ID of the request. |
| Success | Boolean | true | Indicates whether the call succeeded. |
| TableList | Array of Table |   | The details about the tables. |

| ata Management |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Table |   |   |   |
| DatabaseId | String | 1 | The ID of the database. |
| Description | String | test | The description of the table. |
| Encoding | String | utf8 | The encoding of the table. |
| Engine | String | innodb | The engine of the table. |
| NumRows | Long | 1 | The number of rows in the table. This is a statistical value and does not indicate the actual number of rows. |
| OwnerIdList | List | 1 | The IDs of the table owners. |
| OwnerNameList | List | owner name _ | The nicknames of the table owners. |
| StoreCapacity | Long | 1024 | The storage space that is occupied by the table. This is a statistical value and does not indicate the accurate storage space. |
| TableGuid | String | IDB 308302.yuyang _ _ test.test ch _ | The GUID of the table. |
| TableId | String | 1 | The ID of the table. |
| TableName | String | test | The name of the table. |
| TableSchemaN ame | String | test db _ | The name of the database to which the table belongs. |
| TableType | String | NORMAL | The type of the table. Default value: NORMAL. |
| TotalCount | Long | 12 | The total number of tables that meet the query conditions. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListTables &DatabaseId=1 &PageNumber=1 &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TableList>
    <Table>
        <TableSchemaName>yuyang_test</TableSchemaName>
        <OwnerNameList>
            <OwnerNames>xxx</OwnerNames>
            <OwnerNames>xxx</OwnerNames>
        </OwnerNameList>
        <DatabaseId>116367</DatabaseId>
        <Encoding>utf8mb4</Encoding>
        <NumRows>3</NumRows>
        <StoreCapacity>1</StoreCapacity>
        <TableName>base_user</TableName>
        <TableGuid>IDB_18396363.yuyang_test.base_user</TableGuid>
        <TableType>NORMAL</TableType>
        <OwnerIdList>
            <OwnerIds>88653</OwnerIds>
            <OwnerIds>104442</OwnerIds>
        </OwnerIdList>
        <Engine>InnoDB</Engine>
        <TableId>18396363</TableId>
    </Table>
    <Table>
        <TableSchemaName>yuyang_test</TableSchemaName>
        <OwnerNameList>
            <OwnerNames>xxx</OwnerNames>
            <OwnerNames>xxx</OwnerNames>
        </OwnerNameList>
        <DatabaseId>116367</DatabaseId>
        <Encoding>utf8mb4</Encoding>
        <NumRows>2</NumRows>
        <StoreCapacity>1</StoreCapacity>
        <TableName>biz_orders</TableName>
        <TableType>NORMAL</TableType>
        <OwnerIdList>
            <OwnerIds>88653</OwnerIds>
            <OwnerIds>104442</OwnerIds>
        </OwnerIdList>
        <Engine>InnoDB</Engine>
        <TableId>18390459</TableId>
    </Table>
</TableList> <TotalCount>12</TotalCount> <RequestId>B16FB618-5E96-4FFD-BB0D-490C890A4030</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "TableList": {
    "Table": [
```

`{`

```json
        "TableSchemaName": "yuyang_test",
        "OwnerNameList": {
```

```json
          "OwnerNames": [
            "xxx",
            "xxx"
```

`]` `},`

```json
        "DatabaseId": 116367,
        "Encoding": "utf8mb4",
        "NumRows": 3,
        "StoreCapacity": 1,
        "TableName": "base_user",
        "TableGuid": "IDB_18396363.yuyang_test.base_user",
        "TableType": "NORMAL",
        "OwnerIdList": {
          "OwnerIds": [
            88653,
            104442
```

`]` `},`

```json
        "Engine": "InnoDB",
        "TableId": 18396363
```

`},` `{`

```json
        "TableSchemaName": "yuyang_test",
        "OwnerNameList": {
          "OwnerNames": [
            "xxx",
            "xxx"
```

`]` `},`

```json
        "DatabaseId": 116367,
        "Encoding": "utf8mb4",
        "NumRows": 2,
        "StoreCapacity": 1,
        "TableName": "biz_orders",
        "TableType": "NORMAL",
        "OwnerIdList": {
          "OwnerIds": [
            88653,
            104442
```

`]` `},`

```json
        "Engine": "InnoDB",
        "TableId": 18390459
```

`}` `]` `},`

```json
  "TotalCount": 12,
  "RequestId": "B16FB618-5E96-4FFD-BB0D-490C890A4030",
  "Success": true
```

`}`

#### 2.6.6 ListLogicTables

Queries the details of logical tables in a logical database. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListLogicTables | The operation that you want to perform. Set the value to List LogicT ables. |
| DatabaseId | String | Yes | 1 | The ID of the logical database. |
| PageNumber | Integer | Yes | 1 | The number of the page to return. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| SearchName | String | No | test | The keyword that is used to query logical tables. Prefix match is used. |
| ReturnGuid | Boolean | No | true | Specifies whether to return the GUID of the table. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| LogicTableList | Array of LogicTable |   | The details of logical tables. |
| LogicTable |   |   |   |
| DatabaseId | String | 1 | The ID of the logical database. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Logic | Boolean | true | Indicates whether the table is a logical table. Default value: true. |
| OwnerIdList | List | 1 | The IDs of owners for the logical table. |
| OwnerNameList | List | owner name _ | The nicknames of owners for the logical table. |
| SchemaName | String | yuyang test _ | The logical database to which the logical table belongs. |
| TableCount | String | 4 | The number of subtables. |
| TableExpr | String | test[1-4] | The expression of the logical table. |
| TableGuid | String | IDB L 308302.yuyan _ _ g test.test ch _ _ | The GUID of the logical table. |
| TableId | String | 1 | The ID of the logical table. |
| TableName | String | test | The name of the logical table. |
| RequestId | String | F1E6484F-9DF1- 4406-9BDE- 0861C4629B69 | The ID of the request. |
| Success | Boolean | true | Indicates whether the call succeeded. |
| TotalCount | Long | 1 | The total number of logical tables that meet the query conditions. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListLogicTables &DatabaseId=1 &PageNumber=1 &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>1</TotalCount> <RequestId>F1E6484F-9DF1-4406-9BDE-0861C4629B69</RequestId> <LogicTableList>
    <LogicTable>
        <Logic>true</Logic>
        <OwnerNameList>
            <OwnerNames>xxx</OwnerNames>
            <OwnerNames>xxx</OwnerNames>
        </OwnerNameList>
        <TableExpr>t[1-4]</TableExpr>
        <DatabaseId>267</DatabaseId>
        <SchemaName>yuyang_test</SchemaName>
        <TableName>t</TableName>
        <TableGuid>IDB_L_3057.yuyang_test.t</TableGuid>
        <TableCount>4</TableCount>
        <OwnerIdList>
            <OwnerIds>88653</OwnerIds>
            <OwnerIds>104442</OwnerIds>
        </OwnerIdList>
        <TableId>3057</TableId>
    </LogicTable>
</LogicTableList> <Success>true</Success>
```

`JSON` format `{`

```json
  "TotalCount": 1,
  "RequestId": "F1E6484F-9DF1-4406-9BDE-0861C4629B69",
  "LogicTableList": {
    "LogicTable": [
```

`{`

```json
        "Logic": true,
        "OwnerNameList": {
          "OwnerNames": [
            "xxx",
            "xxx"
```

`]` `},`

```json
        "TableExpr": "t[1-4]",
        "DatabaseId": 267,
        "SchemaName": "yuyang_test",
        "TableName": "t",
        "TableGuid": "IDB_L_3057.yuyang_test.t",
        "TableCount": 4,
        "OwnerIdList": {
          "OwnerIds": [
            88653,
            104442
```

`]` `},`

```json
        "TableId": 3057
```

`}` `]` `},`

```json
  "Success": true
```

`}`

#### 2.6.7 ListColumns

Queries the details about columns in a table. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListColumns | The operation that you want to perform. Set the value to List Columns. |
| Logic | Boolean | Yes | false | Specifies whether the table is a logical table. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TableId | String | Yes | 1 | The ID of the table. |
| Tid | Long | Yes | 0 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ColumnList | Array of Column |   | The details about columns. |
| Column |   |   |   |
| AutoIncrement | Boolean | false | Indicates whether the column is an auto- increment column. Valid values: true: The column is an auto-increment column. false: The column is not an auto- increment column. |
| ColumnId | String | 1 | The ID of the column. |
| ColumnName | String | name | The name of the column. |
| ColumnType | String | varchar | The type of the column. |
| DataLength | Long | 32 | The length of the column. |
| DataPrecision | Integer | 0 | The precision of the column. |
| DataScale | Integer | 0 | The scale of the column. |
| DefaultValue | String | def value _ | The default value of the column. |
| Description | String | test | The description of the column. |

| Developer Guide·AP | I Reference |   | Data Managemen |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| FunctionType | String | default | The type of the masking algorithm that is used for the column. Valid values: null: No masking algorithm is used. DEFAULT: A full masking algorithm is used. FIX POS: The fixed position is masked. _ FIX CHAR: The fixed characters are _ replaced. |
| Nullable | Boolean | true | Indicates whether the column can be null. |
| SecurityLevel | String | INNER | The security level of the field. Valid values: INNER SENSITIVE CONFIDENTIAL |
| Sensitive | Boolean | false | Indicates whether the field is a sensitive field. |
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | 0AD9AC55-5873- 474A-9F33- 4285806A3619 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListColumns &Logic=false &TableId=1 &Tid=0 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ColumnList>
    <Column>
        <ColumnId>314036829</ColumnId>
        <DataScale>0</DataScale>
        <Sensitive>false</Sensitive>
        <Description>Primary key ID</Description>
        <DataPrecision>20</DataPrecision>
        <ColumnType>bigint(20) unsigned</ColumnType>
        <ColumnName>id</ColumnName>
        <SecurityLevel>INNER</SecurityLevel>
        <AutoIncrement>true</AutoIncrement>
        <Nullable>false</Nullable>
    </Column>
    <Column>
        <ColumnId>314036830</ColumnId>
        <Sensitive>false</Sensitive>
        <Description>Creation time</Description>
        <DefaultValue>CURRENT_TIMESTAMP</DefaultValue>
        <ColumnType>datetime</ColumnType>
        <ColumnName>gmt_create</ColumnName>
        <SecurityLevel>INNER</SecurityLevel>
        <AutoIncrement>false</AutoIncrement>
        <Nullable>false</Nullable>
    </Column>
    <Column>
        <ColumnId>314036831</ColumnId>
        <Sensitive>false</Sensitive>
        <Description>Modification time</Description>
        <DefaultValue>CURRENT_TIMESTAMP</DefaultValue>
        <ColumnType>datetime</ColumnType>
        <ColumnName>gmt_modified</ColumnName>
        <SecurityLevel>INNER</SecurityLevel>
        <AutoIncrement>false</AutoIncrement>
        <Nullable>false</Nullable>
    </Column>
    <Column>
        <ColumnId>314036832</ColumnId>
        <Sensitive>false</Sensitive>
        <Description>base_user</Description>
        <ColumnType>varchar(64)</ColumnType>
        <DataLength>64</DataLength>
        <ColumnName>user_name</ColumnName>
        <SecurityLevel>INNER</SecurityLevel>
        <AutoIncrement>false</AutoIncrement>
        <Nullable>true</Nullable>
    </Column>
</ColumnList> <RequestId>0AD9AC55-5873-474A-9F33-4285806A3619</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "ColumnList": {
    "Column": [
```

`{`

```json
        "ColumnId": 314036829,
        "DataScale": 0,
        "Sensitive": false,
        "Description": "Primary key ID",
        "DataPrecision": 20,
        "ColumnType": "bigint(20) unsigned",
        "ColumnName": "id",
        "SecurityLevel": "INNER",
        "AutoIncrement": true,
        "Nullable": false
```

`},` `{`

```json
        "ColumnId": 314036830,
        "Sensitive": false,
        "Description": "Creation time",
        "DefaultValue": "CURRENT_TIMESTAMP",
        "ColumnType": "datetime",
        "ColumnName": "gmt_create",
        "SecurityLevel": "INNER",
        "AutoIncrement": false,
        "Nullable": false
```

`},` `{`

```json
        "ColumnId": 314036831,
        "Sensitive": false,
        "Description": "Modification time",
        "DefaultValue": "CURRENT_TIMESTAMP",
        "ColumnType": "datetime",
        "ColumnName": "gmt_modified",
        "SecurityLevel": "INNER",
        "AutoIncrement": false,
        "Nullable": false
```

`},` `{`

```json
        "ColumnId": 314036832,
        "Sensitive": false,
        "Description": "base_user",
        "ColumnType": "varchar(64)",
        "DataLength": 64,
        "ColumnName": "user_name",
        "SecurityLevel": "INNER",
        "AutoIncrement": false,
        "Nullable": true
```

`}` `]` `},`

```json
  "RequestId": "0AD9AC55-5873-474A-9F33-4285806A3619",
  "Success": true
```

`}`

#### 2.6.8 ListIndexes

Queries the details of indexes for a table. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListIndexes | The operation that you want to perform. Set the value to List Indexes. |
| Logic | Boolean | Yes | false | Specifies whether the table is a logical table. |
| TableId | String | Yes | 1 | The ID of the table. |
| Tid | Long | Yes | 0 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The error code that is returned. |
| ErrorMessage | String | UnknownError | The error message that is returned. |
| IndexList | Array of Index |   | The details of indexes. |
| Index |   |   |   |
| IndexComment | String | test | The description of each index. |
| IndexId | String | 1 | The ID of the index. |
| IndexName | String | idx test _ | The name of the index. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| IndexType | String | Primary | The type of the index. Valid values: Primary Unique Normal FullText Spatial |
| TableId | String | 1 | The ID of the table. |
| RequestId | String | 1F4DE2F1-5B47- 462A-A973- E02EB7AF386B | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeds. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListIndexes &Logic=false &TableId=1 &Tid=0 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>1F4DE2F1-5B47-462A-A973-E02EB7AF386B</RequestId> <IndexList>
    <Index>
        <IndexComment/>
        <IndexType>Primary</IndexType>
        <IndexName>PRIMARY</IndexName>
        <IndexId>49331416</IndexId>
        <TableId>18396274</TableId>
    </Index>
</IndexList> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "1F4DE2F1-5B47-462A-A973-E02EB7AF386B",
  "IndexList": {
    "Index": [
```

`{`

```json
        "IndexComment": "",
        "IndexType": "Primary",
        "IndexName": "PRIMARY",
        "IndexId": 49331416,
        "TableId": 18396274
```

`}` `]` `},`

```json
  "Success": true
```

`}`

#### 2.6.9 GetDatabase

Queries the details about a database. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetDatabase | The operation that you want to perform. Set the value to Get Dat abase. |
| Host | String | Yes | xxx.xxx.xxx.xxx | The endpoint of the instance. |
| Port | Integer | Yes | 3306 | The port that is used to connect to the instance. |
| SchemaName | String | Yes | test db _ | The name of the database. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| Sid | String | No | test sid _ | The system identifier (SID) of the instance. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Database | Struct |   | The details about the database. |
| CatalogName | String | def | The name of the database catalog. Not e If the database type is PostgreSQL, the value indicates the name of the PostgreSQL database. |
| DatabaseId | String | 1 | The ID of the database. |
| DbType | String | mysql | The type of the database. |
| DbaId | String | 1 | The ID of the database administrator (DBA). |
| DbaName | String | dba name _ | The name of the DBA. |
| Encoding | String | utf8mb4 | The encoding of the database. |
| EnvType | String | test | The type of the environment to which the database belongs. |
| Host | String | xxx.xxx.xxx.xxx | The endpoint of the instance. |
| InstanceId | String | 1 | The ID of the instance. |
| OwnerIdList | List | 1 | The IDs of the owners of the database. |
| OwnerNameList | List | test | The names of the owners of the database. |
| Port | Integer | 3306 | The number of the port that is used to connect to the instance. |
| SchemaName | String | test db _ | The name of the schema. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| SearchName | String | test db@xxx.xxx.xxx _ .xxx:3306 | The name that is used to search for the database. |
| Sid | String | test sid _ | The system identifier (SID) of the instance. |
| State | String | NORMAL | The status of the database. For more information about the valid values, see the List Dat abases operation. |
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | 3CDB8601-AD74- 4A47-8114- 08E08CD6319D | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GetDatabase &Host=xxx.xxx.xxx.xxx &Port=3306 &SchemaName=test_db &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Database>
    <Encoding>utf8mb4</Encoding>
    <Host>pc-xxx.rwlb.rds.aliyuncs.com</Host>
    <InstanceId>24710</InstanceId>
    <DbType>polardb</DbType>
    <OwnerIdList>
        <OwnerIds>88653</OwnerIds>
        <OwnerIds>104442</OwnerIds>
    </OwnerIdList>
    <EnvType>product</EnvType>
    <DbaId>104442</DbaId>
    <OwnerNameList>
        <OwnerNames>xxx</OwnerNames>
        <OwnerNames>xxx[RAM user]</OwnerNames>
    </OwnerNameList>
    <Port>3306</Port>
    <DatabaseId>116367</DatabaseId>
    <State>NORMAL</State>
    <SearchName>xxx_test@pc-xxx.rwlb.rds.aliyuncs.com:3306[xxx_test]</SearchName>
    <DbaName>xxx[RAM user]</DbaName>
    <SchemaName>xxx_test</SchemaName>
</Database> <RequestId>3CDB8601-AD74-4A47-8114-08E08CD6319D</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "Database": {
    "Encoding": "utf8mb4",
    "Host": "pc-xxx.rwlb.rds.aliyuncs.com",
    "InstanceId": 24710,
    "DbType": "polardb",
    "OwnerIdList": {
      "OwnerIds": [
        88653,
        104442
```

`]` `},`

```json
    "EnvType": "product",
    "DbaId": 104442,
    "OwnerNameList": {
      "OwnerNames": [
        "xxx",
        "xxx[RAM user]"
```

`]` `},`

```json
    "Port": 3306,
    "DatabaseId": 116367,
    "State": "NORMAL",
    "SearchName": <SearchName>xxx_test@pc-xxx.rwlb.rds.aliyuncs.com:3306[xxx_test]</SearchN
ame>
    "DbaName": "xxx[RAM user]"
    "SchemaName": "xxx_test"
```

`},`

```json
  "RequestId": "3CDB8601-AD74-4A47-8114-08E08CD6319D",
  "Success": true
```

`}`

#### 2.6.10 GetLogicDatabase

Queries the details about a logical database. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetLogicDatabas e | The operation that you want to perform. Set the value to Get LogicDat abase. |
| DbId | String | Yes | 1 | The ID of the logical database. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Tid | Long | Yes | 0 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| LogicDatabase | Struct |   | The details about the logical database. |
| DatabaseId | String | 1 | The ID of the logical database. |
| DbType | String | mysql | The type of the database. |
| EnvType | String | dev | The type of the environment to which the database belongs. |
| Logic | Boolean | true | Indicates whether the database is a logical database. The value is fixed to true. |
| OwnerIdList | List | 1 | The IDs of the owners of the database. |
| OwnerNameList | List | owner name _ | The names of the owners of the database. |
| SchemaName | String | test logic db _ _ | The name of the logical database. |
| SearchName | String | test logic db[xxx] _ _ | The name that is used to search for the logical database. |
| RequestId | String | 90260530-565C- 42B9-A6E8- 893481FE6AB6 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GetLogicDatabase &DbId=1 &Tid=0 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<LogicDatabase>
    <Logic>true</Logic>
    <OwnerNameList>
        <OwnerNames>xxx</OwnerNames>
        <OwnerNames>xxx</OwnerNames>
        <OwnerNames>xxx</OwnerNames>
    </OwnerNameList>
    <DatabaseId>265</DatabaseId>
    <SearchName>test_logic_db(xxx)</SearchName>
    <DbType>mysql</DbType>
    <OwnerIdList>
        <OwnerIds>88653</OwnerIds>
        <OwnerIds>97787</OwnerIds>
        <OwnerIds>88654</OwnerIds>
    </OwnerIdList>
    <EnvType>dev</EnvType>
    <SchemaName>test_logic_db</SchemaName>
</LogicDatabase> <RequestId>90260530-565C-42B9-A6E8-893481FE6AB6</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "LogicDatabase": {
    "Logic": true,
    "OwnerNameList": {
      "OwnerNames": [
        "xxx",
        "xxx",
        "xxx"
```

`]` `},`

```json
    "DatabaseId": 265,
    "SearchName": "test_logic_db(xxx)",
    "DbType": "mysql",
    "OwnerIdList": {
      "OwnerIds": [
        88653,
        97787,
        88654
```

`]` `},`

```json
    "EnvType": "dev",
    "SchemaName": "test_logic_db"
```

`},`

```json
  "RequestId": "90260530-565C-42B9-A6E8-893481FE6AB6",
  "Success": true
```

`}`

#### 2.6.11 GetMetaTableDetailInfo

Queries the details of a table. These details include columns and indexes. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetMetaTableDet ailInfo | The operation that you want to perform. Set the value to Get Met aT ableDet ailInf o. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TableGuid | String | Yes | IDB L 9032.db- _ _ test.yuyang test _ | The globally unique identifier (GUID) of the table in DMS. Not e To obtain the GUID of a logical database, set the Ret urnGuid parameter to t rue when you call the List LogicT ables operation. To obtain the GUID of a logical database, set the Ret urnGuid parameter to t rue when you call the List T ables operation. |
| Tid | Long | No | 123 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DetailInfo | Struct |   | The details of the table. |
| ColumnList | Array of Column |   | The columns. |
| AutoIncrement | Boolean | true | Indicates whether the column is an auto- increment column. Valid values: true: The column is an auto-increment column. false: The column is not an auto- increment column. |
| ColumnId | String | 191234849 | The ID of the column. |
| ColumnName | String | id | The name of the column. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ColumnType | String | bigint(20) unsigned | The data type of the column. Example: Bigint ,Int , or Varchar. |
| DataLength | Integer | 0 | The length of the column. |
| DataPrecision | Integer | 0 | The precision of the column. |
| DataScale | Integer | 0 | The scale of the column. |
| Description | String | test | The description of the column. |
| Nullable | Boolean | false | Indicates whether the column is nullable. Valid values: true: The column is nullable. false: The column is not nullable. |
| Position | String | 1 | The position of the column in the table. |
| IndexList | Array of Index |   | The indexes. |
| IndexColumns | List | id,name | The indexed columns. |
| IndexId | String | 123 | The ID of the index. |
| IndexName | String | PRIMARY | The name of the index. |
| IndexType | String | Primary | The type of the index. Example: Primary, Unique, or Normal. |
| Unique | Boolean | false | Indicates whether the index is unique. Valid values: true: The index is unique. false: The index is not unique. |
| ErrorCode | String | UnknownError | The error code that is returned. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorMessage | String | UnknownError | The error message that is returned. |
| RequestId | String | E881CB2F-DE42- 42E5-90EB- 8B3173DCB9B9 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeds. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GetMetaTableDetailInfo &TableGuid=IDB_L_9032.db-test.yuyang_test &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>E881CB2F-DE42-42E5-90EB-8B3173DCB9B9</RequestId> <DetailInfo>
    <ColumnList>
        <ColumnId>191234849</ColumnId>
        <ColumnName>id</ColumnName>
        <Description>test</Description>
        <ColumnType>bigint(20) unsigned</ColumnType>
        <Position>1</Position>
        <AutoIncrement>true</AutoIncrement>
        <DataScale>0</DataScale>
        <DataPrecision>20</DataPrecision>
        <Nullable>false</Nullable>
    </ColumnList>
    <ColumnList>
        <ColumnId>191234850</ColumnId>
        <ColumnName>gmt_create</ColumnName>
        <Description>test</Description>
        <ColumnType>datetime</ColumnType>
        <Position>2</Position>
        <AutoIncrement>false</AutoIncrement>
        <Nullable>false</Nullable>
    </ColumnList>
    <ColumnList>
        <ColumnId>191234851</ColumnId>
        <ColumnName>gmt_modified</ColumnName>
        <Description>test</Description>
        <ColumnType>datetime</ColumnType>
        <Position>3</Position>
        <AutoIncrement>false</AutoIncrement>
        <Nullable>false</Nullable>
    </ColumnList>
    <IndexList>
        <IndexName>PRIMARY</IndexName>
        <IndexId>33008763</IndexId>
        <IndexColumns>id</IndexColumns>
        <Unique>false</Unique>
        <IndexType>Primary</IndexType>
    </IndexList>
</DetailInfo> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "E881CB2F-DE42-42E5-90EB-8B3173DCB9B9",
  "DetailInfo": {
    "ColumnList": [
```

`{`

```json
        "ColumnId": 191234849,
        "ColumnName": "id",
        "Description": "test",
        "ColumnType": "bigint(20) unsigned",
        "Position": 1,
        "AutoIncrement": true,
        "DataScale": 0,
        "DataPrecision": 20,
        "Nullable": false
```

`},` `{`

```json
        "ColumnId": 191234850,
        "ColumnName": "gmt_create",
        "Description": "test",
        "ColumnType": "datetime",
        "Position": 2,
        "AutoIncrement": false,
        "Nullable": false
```

`},` `{`

```json
        "ColumnId": 191234851,
        "ColumnName": "gmt_modified",
        "Description": "test",
        "ColumnType": "datetime",
        "Position": 3,
        "AutoIncrement": false,
        "Nullable": false
```

`}` `],`

```json
    "IndexList": [
```

`{`

```json
        "IndexName": "PRIMARY",
        "IndexId": 33008763,
        "IndexColumns": [
          "id"
```

`],`

```json
        "Unique": false,
        "IndexType": "Primary"
```

`}` `]` `},`

```json
  "Success": true
```

`}`

#### 2.6.12 GetTableDBTopology

Queries the topology of a table. This operation is available only for logical databases. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetTableDBTopol ogy | The operation that you want to perform. Set the value to Get T ableDBT opology. |
| TableGuid | String | Yes | IDB L 9032.db- _ _ test.yuyang test _ | The globally unique identifier (GUID) of a table in Data Management (DMS). Not e To obtain the GUID of a table in a logical database, set the Ret urnGuid parameter to t rue when you call the List LogicT ables operation. To obtain the GUID of a table in a physical database, set the Ret urnGuid parameter to t rue when you call the List T ables operation. |
| Tid | Long | No | 123 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The ID of the region where Data Management (DMS) resides. Not e Set this parameter to the ID of the region that is in proximity to your applications. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBTopology | Struct |   | The topology information about the database. |
| DataSourceList | Array of DataSource |   | The data sources. |

| ata Management |   |   | Developer Guide·API Referenc |
|---|---|---|---|
| Parameter | Type | Example | Description |
| DatabaseList | Array of Database |   | The physical databases. |
| DbId | String | 489347 | The ID of the database. |
| DbName | String | db-test | The name of the database. |
| DbType | String | mysql | The type of the database. |
| EnvType | String | pre | The type of the environment. Valid values: product: production environment dev: development environment pre: staging environment test: test environment sit: SIT environment uat: UAT environment pet: stress testing environment stag: STAG environment |
| TableList | Array of Table |   | The physical tables. |
| TableId | String | 151977812 | The ID of the table. |
| TableName | String | yuyang test 0000 _ _ | The name of the table. |
| TableType | String | NORMAL | The type of the table. This is a reserved parameter. |
| DbType | String | mysql | The type of the database. |
| Host | String | xxx.mysql.polardb.r ds.aliyuncs.com | The endpoint of the data source. |
| Port | Integer | 3306 | The port that is used to connect to the data source. |
| Sid | String | def | The system identifier (SID) of the data source. |

| Developer Guide·AP | I Reference |   | Data Managemen |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| TableGuid | String | IDB L 9032.db- _ _ test.yuyang test _ | The GUID of the table in DMS. |
| TableName | String | yuyang test _ | The name of the table. Not e If a logical table is queried, the name of the logical table is returned. If a physical table is queried, the name of the physical table is returned. |
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | 853F7FD4-D922- 4EFB-931C- D253EF159E06 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GetTableDBTopology &TableGuid=IDB_L_9032.db-test.yuyang_test &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>55B7CF50-4610-4707-B2B2-5EF2BE000367</RequestId> <DBTopology>
    <TableName>yuyang_test</TableName>
    <TableGuid>IDB_L_9032.db-test.yuyang_test</TableGuid>
    <DataSourceList>
        <DatabaseList>
            <DbId>489347</DbId>
            <DbName>db-test</DbName>
            <TableList>
                <TableId>151977811</TableId>
                <TableName>yuyang_test_0000</TableName>
            </TableList>
            <TableList>
                <TableId>151977812</TableId>
                <TableName>yuyang_test_0001</TableName>
            </TableList>
            <TableList>
                <TableId>151977813</TableId>
                <TableName>yuyang_test_0002</TableName>
            </TableList>
            <TableList>
                <TableId>151977814</TableId>
                <TableName>yuyang_test_0003</TableName>
            </TableList>
            <TableList>
                <TableId>151977815</TableId>
                <TableName>yuyang_test_0004</TableName>
            </TableList>
            <EnvType>dev</EnvType>
            <DbType>polardb</DbType>
        </DatabaseList>
        <Port>3306</Port>
        <Host>xxx.mysql.polardb.rds.aliyuncs.com</Host>
        <DbType>polardb</DbType>
    </DataSourceList>
</DBTopology> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "55B7CF50-4610-4707-B2B2-5EF2BE000367",
  "DBTopology": {
    "TableName": "yuyang_test",
    "TableGuid": "IDB_L_9032.db-test.yuyang_test",
    "DataSourceList": [
```

`{`

```json
        "DatabaseList": [
```

`{`

```json
            "DbId": 489347,
            "DbName": "db-test",
            "TableList": [
```

`{`

```json
                "TableId": 151977811,
                "TableName": "yuyang_test_0000"
```

`},` `{`

```json
                "TableId": 151977812,
                "TableName": "yuyang_test_0001"
```

`},` `{`

```json
                "TableId": 151977813,
                "TableName": "yuyang_test_0002"
```

`},` `{`

```json
                "TableId": 151977814,
                "TableName": "yuyang_test_0003"
```

`},` `{`

```json
                "TableId": 151977815,
                "TableName": "yuyang_test_0004"
```

`}` `],`

```json
            "EnvType": "dev",
            "DbType": "polardb"
```

`}` `],`

```json
        "Port": 3306,
        "Host": "xxx.mysql.polardb.rds.aliyuncs.com",
        "DbType": "polardb"
```

`}` `]` `},`

```json
  "Success": true
```

`}`

#### 2.6.13 GetMetaTableColumn

Queries the details about columns in a table. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetMetaTableCol umn | The operation that you want to perform. Set the value to Get Met aT ableColumn. |
| TableGuid | String | Yes | IDB L 11345.yuya _ _ ng test.base use _ _ r | The globally unique identifier (GUID) of a table in Data Management (DMS). Not e To obtain the GUID of a table in a logical database, set the Ret urnGuid parameter to t rue when you call the List LogicT ables operation. To obtain the GUID of a table in a physical database, set the Ret urnGuid parameter to t rue when you call the List T ables operation. |
| Tid | Long | No | 123 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ColumnList | Array of Column |   | The columns. |
| AutoIncrement | Boolean | true | Indicates whether the column is an auto- increment column. Valid values: t rue: The column is an auto-increment column. f alse: The column is not an auto- increment column. |
| ColumnId | String | 191234849 | The ID of the column. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ColumnName | String | id | The name of the column. |
| ColumnType | String | bigint(20) unsigned | The data type of the column. Examples: Bigint , Int , and Varchar. |
| DataLength | Integer | 0 | The length of the column. |
| DataPrecision | Integer | 0 | The precision of data in the column. |
| DataScale | Integer | 0 | The scale of data in the column. |
| Description | String | test | The description of the column. |
| Nullable | Boolean | false | Indicates whether the column is empty. Valid values: t rue: The column is empty. f alse: The column is not empty. |
| Position | Integer | 1 | The order of the column in the table. |
| PrimaryKey | String | true | Indicates whether the column is the primary key. t rue: The column is the primary key. f alse: The column is not the primary key. |
| SecurityLevel | String | INNER | The sensitivity level of the column. Valid values: INNER SENSIT IVE CONFIDENT IAL |
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | 2B581A5E-D4FE- 4F77-BADE- DD944D7BEBE2 | The ID of the request. |

|   | Data Management |   |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GetMetaTableColumn &TableGuid=IDB_L_11345.yuyang_test.base_user &<Common request parameters>
```

Sample success responses `XML` format

```xml
<GetMetaTableColumnResponse>
      <RequestId>2B581A5E-D4FE-4F77-BADE-DD944D7BEBE2</RequestId>
      <ErrorCode>UnknownError</ErrorCode>
      <ColumnList>
            <ColumnId>191234849</ColumnId>
            <ColumnName>id</ColumnName>
            <Description>test</Description>
            <ColumnType>bigint(20) unsigned</ColumnType>
            <Position>1</Position>
            <AutoIncrement>true</AutoIncrement>
            <SecurityLevel>INNER</SecurityLevel>
            <DataScale>0</DataScale>
            <DataLength>0</DataLength>
            <DataPrecision>0</DataPrecision>
            <PrimaryKey>true</PrimaryKey>
            <Nullable>false</Nullable>
      </ColumnList>
      <ErrorMessage>UnknownError</ErrorMessage>
      <Success>true</Success>
</GetMetaTableColumnResponse>
```

`JSON` format `{`

```json
 "RequestId": "2B581A5E-D4FE-4F77-BADE-DD944D7BEBE2",
 "ErrorCode": "UnknownError",
 "ColumnList": [{
  "ColumnId": "191234849",
  "ColumnName": "id",
  "Description": "test",
  "ColumnType": "bigint(20) unsigned",
  "Position": "1",
  "AutoIncrement": "true",
  "SecurityLevel": "INNER",
  "DataScale": "0",
  "DataLength": "0",
  "DataPrecision": "0",
  "PrimaryKey": "true",
  "Nullable": "false"
 }],
 "ErrorMessage": "UnknownError",
 "Success": "true"
```

`}`

#### 2.6.14 SyncDatabaseMeta

Synchronizes the metadata of a database dictionary. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SyncDatabaseMet a | The operation that you want to perform. Set the value to SyncDat abaseMet a. |
| DbId | String | Yes | 123 | The ID of the database. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| Logic | Boolean | No | false | Specifies whether the database is a logical database. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The error code that is returned. |
| ErrorMessage | String | UnknownError | The error message that is returned. |
| RequestId | String | A99CD576-1E18- 4E86-931E- C3CCE56DC030 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SyncDatabaseMeta &DbId=123 &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>A99CD576-1E18-4E86-931E-C3CCE56DC030</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "A99CD576-1E18-4E86-931E-C3CCE56DC030",
  "Success": true
```

`}`

#### 2.6.15 SyncInstanceMeta

Synchronizes the metadata of all database dictionaries in an instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SyncInstanceMeta | The operation that you want to perform. Set the value to SyncInst anceMet a. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| InstanceId | String | Yes | 1234 | The ID of the instance. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| IgnoreTable | Boolean | No | true | Specifies whether to skip synchronization for the metadata of table dictionaries. Valid values: true false |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | A99CD576-1E18- 4E86-931E- C3CCE56DC030 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SyncInstanceMeta &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>A99CD576-1E18-4E86-931E-C3CCE56DC030</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "A99CD576-1E18-4E86-931E-C3CCE56DC030",
  "Success": true
```

`}`

### 2.7 Ticket operations

#### 2.7.1 General

##### 2.7.1.1 ApproveOrder

Reviews a ticket. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ApproveOrder | The operation that you want to perform. Set the value to ApproveOrder. |
| ApprovalType | String | Yes | agree | The action that you want to perform on the ticket. Valid values: AGREE CANCEL REJECT |
| Tid | Long | Yes | -1 | The ID of the tenant. Not e To view the ID of the tenant, perform the following steps: Log on to the Data Management (DMS) console. Move the pointer over the profile picture in the upper-right corner of the page. |
| WorkflowInstanc eId | Long | Yes | 1234 | The ID of the approval process. You can call the Get OrderBaseInf o operation to obtain the ID. The ID is available only for a ticket that is pending approval. The value of this parameter is an integer that is greater than zero. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | No | cn-hangzhou | The region ID. |
| Comment | String | No | test | The remarks. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ApproveOrder &ApprovalType=agree &Tid=-1 &WorkflowInstanceId=1234 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>427688B8-ADFB-4C4E-9D45-EF5C1FD6E23D</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "427688B8-ADFB-4C4E-9D45-EF5C1FD6E23D",
  "Success": true
```

`}`

##### 2.7.1.2 CloseOrder

Closes a ticket. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CloseOrder | The operation that you want to perform. Set the value to CloseOrder. |
| CloseReason | String | Yes | close reason | The reason why the ticket is closed. |
| OrderId | Long | Yes | 1343 | The ID of the ticket. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The error code that is returned. |
| ErrorMessage | String | UnknownError | The error message that is returned. |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | The ID of the request. |
| Success | Boolean | true | Indicates whether the call succeeds. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CloseOrder &CloseReason=close reason &OrderId=1343 &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>427688B8-ADFB-4C4E-9D45-EF5C1FD6E23D</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "427688B8-ADFB-4C4E-9D45-EF5C1FD6E23D",
  "Success": true
```

`}`

##### 2.7.1.3 GetApprovalDetail

Queries the approval details of a ticket. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetApprovalDetai l | The operation that you want to perform. Set the value to Get ApprovalDet ail. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| WorkflowInstanc eId | Long | Yes | 12345 | The ID of the approval process. You can call the Get OrderBaseInf o operation to obtain the ID. The ID is available only for a ticket that is pending approval. The value of this parameter is an integer that is greater than zero. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ApprovalDetail | Struct |   | The details of the approval process. |
| AuditId | Long | 277 | The ID of the approval process. |
| CurrentHandler s | Array of CurrentHandler |   | The information of the reviewer. |

| ata Management |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| CurrentHandler |   |   |   |
| Id | Long | 1 | The ID of the user. |
| NickName | String | nickName | The name of the user. |
| Description | String | test | The description of the approval process. |
| OrderId | Long | 1234 | The ID of the ticket. |
| OrderType | String | DATA EXPORT _ | The type of the ticket. |
| ReasonList | List | ["reason1"] | The reason for the review result. |
| Title | String | Data export ticket- 1234 | The title of the approval process. |
| WorkflowInsCo de | String | APPROVED | The status code of the approval process. |
| WorkflowNode s | Array of WorkflowNode |   | The details of approval nodes. |
| WorkflowNode |   |   |   |
| AuditUserIdList | List | 104442 | The IDs of reviewers. |
| NodeName | String | DBA | The name of the approval node. |
| OperateComme nt | String | Reason: approved | The remarks of the review. |
| OperateTime | String | 2019-10-15 13:47:54 | The time when the ticket was reviewed. |
| OperatorId | Long | 13434 | The ID of the reviewer. |
| WorkflowInsCo de | String | APPROVED | The status code of the approval process. |
| ErrorCode | String | UnknownError | The returned error code. |

| Developer Guide·AP | I Reference |   | Data Managemen |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GetApprovalDetail &Tid=-1 &WorkflowInstanceId=12345 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ApprovalDetail>
    <Description>xxx</Description>
    <WorkflowInsCode>APPROVED</WorkflowInsCode>
    <CurrentHandlers>
    </CurrentHandlers>
    <OrderId>737047</OrderId>
    <OrderType>DATA_EXPORT</OrderType>
    <ReasonList>
        <Reasons>xxx</Reasons>
    </ReasonList>
    <AuditId>277</AuditId>
    <Title>Data export ticket-737047</Title>
    <WorkflowNodes>
        <WorkflowNode>
            <OperatorId>104442</OperatorId>
            <WorkflowInsCode>APPROVED</WorkflowInsCode>
            <OperateComment>Reason: approved</OperateComment>
            <AuditUserIdList>
                <AuditUserIds>104442</AuditUserIds>
            </AuditUserIdList>
            <OperateTime>2019-10-15 13:47:54</OperateTime>
            <NodeName>DBA</NodeName>
        </WorkflowNode>
    </WorkflowNodes>
</ApprovalDetail> <RequestId>FE8EE2F1-4880-46BC-A704-5CF63EAF9A04</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "ApprovalDetail": {
    "Description": "xxx",
    "WorkflowInsCode": "APPROVED",
    "CurrentHandlers": {
      "CurrentHandler": []
```

`},`

```json
    "OrderId": 737047,
    "OrderType": "DATA_EXPORT",
    "ReasonList": {
      "Reasons": [
        "xxx"
```

`]` `},`

```json
    "AuditId": 277,
    "Title": "Data export ticket-737047",
    "WorkflowNodes": {
      "WorkflowNode": [
```

`{`

```json
          "OperatorId": 104442,
          "WorkflowInsCode": "APPROVED",
          "OperateComment": "Reason: approved",
          "AuditUserIdList": {
            "AuditUserIds": [
              104442
```

`]` `},`

```json
          "OperateTime": "2019-10-15 13:47:54",
          "NodeName": "DBA"
```

`}` `]` `}` `},`

```json
  "RequestId": "FE8EE2F1-4880-46BC-A704-5CF63EAF9A04",
  "Success": true
```

`}`

##### 2.7.1.4 GetOrderBaseInfo

Queries the basic information about a ticket. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetOrderBaseInfo | The operation that you want to perform. Set the value to Get OrderBaseInf o. |

| eveloper Guide·API | Reference |   |   | Data Managemen |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| OrderId | Long | Yes | 12345 | The ID of the ticket. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| OrderBaseInfo | Struct |   | The basic information about the ticket. |
| Comment | String | test | The remarks. |
| Committer | String | xxx | The applicant. |
| CommitterId | Long | 1 | The ID of the applicant. Note: The ID is different from the Apsara Stack tenant account ID of the applicant. |
| CreateTime | String | 2019-10-10 00:00:00 | The time when the ticket was created. |
| LastModifyTim e | String | 2019-10-10 00:00:00 | The last time when the ticket was modified. |
| OrderId | Long | 12345 | The ID of the ticket. |
| PluginType | String | DC COMMON _ | The type of the ticket. For more information, see the "Request parameters" section of the Creat eOrder topic. |
| RelatedUserList | List | 1,2,3 | The IDs of the operators that are related to the ticket. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RelatedUserNic kList | List | a,b,c | The names of the operators that are related to the ticket. |
| StatusCode | String | success | The status code of the ticket. Valid values: new: The ticket is created. toaudit: The ticket is being reviewed. Approved: The ticket is approved. reject: The ticket is rejected. processing: The request to create the ticket is being processed. success: The request to create the ticket is processed. closed: The ticket is closed. |
| StatusDesc | String | success | The description of the status. |
| WorkflowInstan ceId | Long | 1 | The ID of the approval process. |
| WorkflowStatu sDesc | String | approved | The description of the approval process. |
| RequestId | String | 7133DF67-5B25- 460F-8285- C4CC93472C2F | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GetOrderBaseInfo &OrderId=12345 &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<OrderBaseInfo>
    <Comment>test</Comment>
    <CreateTime>2019-10-10 00:00:00</CreateTime>
    <LastModifyTime>2019-10-10 00:00:00</LastModifyTime>
    <OrderId>12345</OrderId>
    <CommitterId>1</CommitterId>
    <PluginType>DC_COMMON</PluginType>
    <StatusCode>success</StatusCode>
    <RelatedUserNickList>
        <UserNicks>a,b,c</UserNicks>
    </RelatedUserNickList>
    <StatusDesc>success</StatusDesc>
    <WorkflowStatusDesc>approved</WorkflowStatusDesc>
    <WorkflowInstanceId>1</WorkflowInstanceId>
    <Committer>xxx</Committer>
    <RelatedUserList>
        <UserIds>1,2,3</UserIds>
    </RelatedUserList>
</OrderBaseInfo> <RequestId>7133DF67-5B25-460F-8285-C4CC93472C2F</RequestId> <ErrorCode>UnknownError</ErrorCode> <ErrorMessage>UnknownError</ErrorMessage> <Success>true</Success>
```

`JSON` format

```json
{"OrderBaseInfo":{"Comment":"test","CreateTime":"2019-10-10 00:00:00","LastModifyTime":"201 9-10-10 00:00:00","OrderId":"12345","CommitterId":"1","PluginType":"DC_COMMON","StatusCode" :"success","RelatedUserNickList":{"UserNicks":"a,b,c"},"StatusDesc":"success","WorkflowStat usDesc":"approved","WorkflowInstanceId":"1","Committer":"xxx","RelatedUserList":{"UserIds": "1,2,3"}},"RequestId":"7133DF67-5B25-460F-8285-C4CC93472C2F","ErrorCode":"UnknownError","Er rorMessage":"UnknownError","Success":"true"}
```

##### 2.7.1.5 ListOrders

Queries the details of tickets. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListOrders | The operation that you want to perform. Set the value to List Orders. |
| Tid | Long | No | -1 | The ID of the tenant. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PluginType | String | No | DC COMMON _ | The type of tickets. Valid values: PERM APPLY: the tickets that are _ used to apply for permissions. OWNER APPLY: the tickets that are _ used to assume the ownership of resources. DATA CORRECT: the tickets that are _ used to change data. NDDL: the tickets that are used to change the schema design of databases. DATA TRACK: the tickets that are _ used to trace data. TABLE SYNC: the tickets that are _ used to synchronize databases or tables. DATA EXPORT: the tickets that are _ used to export data. SENSITIVITY: the tickets that are used to change the level of sensitive columns. |
| OrderResultType | String | No | AS ADMIN _ | The range of tickets to be queried. Valid values: AS ADMIN: all tickets. _ AS COMMITTER: the tickets that are _ submitted by the current user. AS HANDLER: the tickets to be _ processed by the current user. AS OWNER: the tickets that are _ processed by the current user. AS Related: the tickets that are _ related to the current user. |
| SearchDateType | String | No | CREATE TIME _ | The time condition. Valid values: CREATE TIME: the time when tickets _ are created. MODIFY TIME: the time when tickets _ are modified. |
| StartTime | String | No | 2019-10-10 00:00:00 | The start of the time range. |
| EndTime | String | No | 2019-10-10 00:00:00 | The end of the time range. |

| D | eveloper Guide·API | Reference |   |   | Data Managemen | t |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SearchContent | String | No | test | The keyword that is used to search for tickets. |
| OrderStatus | String | No | ALL | The status of tickets. Valid values: ALL: The tickets of all statuses are included. FINISHED: The tickets are completed. RUNNING: The tickets are being processed. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| PageNumber | Integer | No | 1 | The number of the page to return. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| Orders | Array of Order |   | The details about the tickets. |
| Order |   |   |   |
| Comment | String | test | The remarks of the ticket. |
| Committer | String | test | The user who submitted the ticket. |
| CommitterId | Long | 1 | The ID of the user who submitted the ticket. |
| CreateTime | String | 2019-10-10 00:00:00 | The time when the ticket was created. |
| LastModifyTim e | String | 2019-10-10 00:00:00 | The last time when the ticket was modified. |

| Data Management |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| OrderId | Long | 1432 | The ID of the ticket. |
| PluginType | String | DC COMMON _ | The type of the ticket. |
| StatusCode | String | success | The status of the ticket. |
| StatusDesc | String | success | The status description of the ticket. |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |
| TotalCount | Long | 100 | The total number of entries that are returned. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListOrders &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>5</TotalCount> <RequestId>7AC17A86-9E6F-484B-AE8D-F9416986A108</RequestId> <Orders>
    <Order>
        <StatusCode>success</StatusCode>
        <PluginType>DC_COMMON</PluginType>
        <Committer>xxx[RAM user]</Committer>
        <StatusDesc>Data is changed.</StatusDesc>
        <LastModifyTime>2019-11-19 13:53:05</LastModifyTime>
        <CreateTime>2019-11-19 13:52:36</CreateTime>
        <OrderId>737160</OrderId>
        <Comment>A test ticket that is used to change data</Comment>
        <CommitterId>104442</CommitterId>
    </Order>
    <Order>
        <StatusCode>new</StatusCode>
        <PluginType>DC_COMMON</PluginType>
        <Committer>xxx[RAM user]</Committer>
<Stt
```

`D`

```
>Th tikti
```

`t` `b`

```
bittdf l</Stt
```

`D` `>`

```xml
        <StatusDesc>The ticket is to be submitted for approval.</StatusDesc>
        <LastModifyTime>2019-10-29 20:51:37</LastModifyTime>
        <CreateTime>2019-10-29 20:51:36</CreateTime>
        <OrderId>737116</OrderId>
        <Comment>Create a test ticket to change data</Comment>
        <CommitterId>104442</CommitterId>
    </Order>
    <Order>
        <StatusCode>closed</StatusCode>
        <PluginType>DC_COMMON</PluginType>
        <Committer>xxx[RAM user]</Committer>
        <StatusDesc>The ticket is closed: Database-level operations are not supported.</Sta
tusDesc>
        <LastModifyTime>2019-10-20 22:09:38</LastModifyTime>
        <CreateTime>2019-10-20 22:08:19</CreateTime>
        <OrderId>737089</OrderId>
        <Comment>The test ticket that is used to create a database</Comment>
        <CommitterId>104442</CommitterId>
    </Order>
    <Order>
        <StatusCode>new</StatusCode>
        <PluginType>DC_COMMON</PluginType>
        <Committer>xxx[RAM user]</Committer>
        <StatusDesc>Failed to perform the pre-check.</StatusDesc>
        <LastModifyTime>2019-09-30 16:58:35</LastModifyTime>
        <CreateTime>2019-09-30 16:58:34</CreateTime>
        <OrderId>737016</OrderId>
        <Comment>Test</Comment>
        <CommitterId>104442</CommitterId>
    </Order>
    <Order>
        <StatusCode>success</StatusCode>
        <PluginType>DC_COMMON</PluginType>
        <Committer>xxx[RAM user]</Committer>
        <StatusDesc>Data is changed.</StatusDesc>
        <LastModifyTime>2019-08-17 14:07:54</LastModifyTime>
        <CreateTime>2019-08-17 14:07:42</CreateTime>
        <OrderId>736774</OrderId>
        <Comment>The ticket that is used to change common data</Comment>
        <CommitterId>104442</CommitterId>
    </Order>
</Orders> <Success>true</Success>
```

`JSON` format `{`

```json
  "TotalCount": 5,
  "RequestId": "7AC17A86-9E6F-484B-AE8D-F9416986A108",
  "Orders": {
    "Order": [
```

`{`

```json
        "StatusCode": "success",
        "PluginType": "DC_COMMON",
```

```json
        "Committer": "xxx[RAM user]"
        "StatusDesc": "Data is changed.",
        "LastModifyTime": "2019-11-19 13:53:05",
        "CreateTime": "2019-11-19 13:52:36",
        "OrderId": 737160,
        "Comment": "The test ticket that is used to change data",
        "CommitterId": 104442
```

`},` `{`

```json
        "StatusCode": "new",
        "PluginType": "DC_COMMON",
        "Committer": "xxx[RAM user]"
        "StatusDesc": "The ticket is to be submitted for approval.",
        "LastModifyTime": "2019-10-29 20:51:37",
        "CreateTime": "2019-10-29 20:51:36",
        "OrderId": 737116,
        "Comment": "Create a test ticket to change data",
        "CommitterId": 104442
```

`},` `{`

```json
        "StatusCode": "closed",
        "PluginType": "DC_COMMON",
        "Committer": "xxx[RAM user]"
        "StatusDesc": "The ticket is closed: Database-level operations are not supported.",
        "LastModifyTime": "2019-10-20 22:09:38",
        "CreateTime": "2019-10-20 22:08:19",
        "OrderId": 737089,
        "Comment": "A test ticket that is used to create a database",
        "CommitterId": 104442
```

`},` `{`

```json
        "StatusCode": "new",
        "PluginType": "DC_COMMON",
        "Committer": "xxx[RAM user]"
        "StatusDesc": "Failed to perform the pre-check.",
        "LastModifyTime": "2019-09-30 16:58:35",
        "CreateTime": "2019-09-30 16:58:34",
        "OrderId": 737016,
        "Comment": "Test",
        "CommitterId": 104442
```

`},` `{`

```json
        "StatusCode": "success",
        "PluginType": "DC_COMMON",
        "Committer": "xxx[RAM user]"
        "StatusDesc": "Data is changed.",
        "LastModifyTime": "2019-08-17 14:07:54",
        "CreateTime": "2019-08-17 14:07:42",
        "OrderId": 736774,
        "Comment": "The ticket that is used to change common data",
        "CommitterId": 104442
```

`}` `]` `},`

```json
  "Success": true
```

`}`

##### 2.7.1.6 SubmitOrderApproval

Submits a ticket for approval. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SubmitOrderAppr oval | The operation that you want to perform. Set the value to Submit OrderApproval. |
| OrderId | Long | Yes | 12345 | The ID of the ticket. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The error code that is returned. |
| ErrorMessage | String | UnknownError | The error message that is returned. |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SubmitOrderApproval &OrderId=12345 &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>7AC17A86-9E6F-484B-AE8D-F9416986A108</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "7AC17A86-9E6F-484B-AE8D-F9416986A108",
  "Success": true
```

`}`

##### 2.7.1.7 CreateOrder

Creates a ticket. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateOrder | The operation that you want to perform. Set the value to Creat eOrder. |
| Comment | String | Yes | test | The description of the ticket. |
| PluginParam | Json | Yes | {} | The parameter that is used to create a ticket. This parameter consists of a set of parameters that are included in a JSON string. The settings of these parameters are subject to the type of the ticket. For more information, see the "Instructions for the PluginParam parameter" section. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PluginType | String | Yes | DATA EXPORT _ | The type of the ticket. Valid values: DC COMMON: a ticket that is used to _ change common data. DC CHUNK: a ticket that is used to _ change lock-free data. DC CRON CLEAR: a ticket that is _ _ used to change historical data. NDDL: a ticket that is used to change the schema design. DATA EXPORT: a ticket that is used _ to export data. PERM APPLY: a ticket that is used to _ request a permission. OWNER APPLY: a ticket that is used _ to request the ownership of a resource. |
| RelatedUserList | String | Yes | 1,2,3 | The IDs of the operators that are related to the ticket. Separate multiple IDs with commas (,). |
| Tid | Long | No | -1 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Instructions for the PluginParam parameter

```json
json
# Change common data
"pluginParam" : {
    "classify" : "Test", // The classification of the reason.
    "estimateAffectRows" : 1, // The estimated number of affected rows.
    "execSql" : "update base_op_log set id=1 where id=1;", // The SQL statement to be execu
ted.
    "dbItemList" : [ { // The details of databases on which the operation is performed.
      "dbId" : 179694,
      "logic" : false
    } ],
    "rbSQL" : "update base_op_log set id=1 where id=1;", // The SQL statement to run for ro
llback.
    "rbAttachmentName" : null, // The attachment of the SQL statement to run for rollback.
    "sqlType" : "TEXT", // The type of the SQL file to run for data change. Valid values: T
EXT and ATTACHMENT.
    "rbSQLType" : "TEXT", // The type of the SQL file to run for rollback. Valid values: TE
XT and ATTACHMENT.
    "attachmentName" : // The attachment of the SQL statement to run for data change.
```

`}`

```json
# Change lock-free data
"pluginParam" : {
    "Classify":"Test"
    "execSQL" : "update base_op_log set op_type=op_type where 1=1;", // The SQL statement t
o be executed.
    "dbItemList" : [ {
      "dbId": 179719, // The ID of the database from which data is exported.
      "logic" : false
    } ]
```

`}`

```json
# Clear historical data
"pluginParam" : {
    "duration" : 10, // The duration. Unit: hours. Default value: 0.
    "specifyDuration" : true, // Specifies whether to set a duration. Valid values: true (y
es) and false (no). Default value: false.
    "Classify":"Test"
    "cronFormat" : "0 1 21 * * ?", // The expression that is used to schedule the execution
of the operation.
    "execSql" : null,
    "dbItemList" : [ {
      "dbId": 179719, // The ID of the database on which the operation is performed.
      "logic" : false
    } ],
    "cronClearItemList" : [ {
      "filterSQL" : null, // The filter conditions.
      "columnName" : "gmt_create", // The time field.
      "remainDays" : 60, // The retention period.
      "tableName" : "base_app" // The table name.
    } ]
```

`}`

```json
json
# Change the schema design
"pluginParam": {
    "title": "test", // The title.
    "description": "test", // The description.
    "dbId": 118989, // The ID of the required database.
    "logic": false, // Specifies whether the database is a logical database.
    "relatedIds": [], // The IDs of operators that are related to the change.
```

`}`

```json
json
# Export data
"pluginParam" : {
  "classify": "Classification of the reason", // The classification of the reason.
  "dbId": 179719, // The ID of the database from which data is exported.
  "exeSQL": "select 1", // Export data by using the SQL statement.
  "logic": false, // Specifies whether the database is a logical database.
  "ignoreAffectRows": false, // Specifies whether to ignore the affected rows.
  "affectRows": 1, // The estimated number of affected rows.
  "ignoreAffectRowsReason": "" // Specifies whether to ignore the affected rows.
```

`}` Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CreateOrderRes ult | List | 123 | The ID of the ticket that is created. |
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | The ID of the request. |
| Success | Boolean | true | Indicates whether the call succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateOrder &Comment=test &PluginParam={} &PluginType=DATA_EXPORT &RelatedUserList=1,2,3 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>427688B8-ADFB-4C4E-9D45-EF5C1FD6E23D</RequestId> <CreateOrderResult>
    <OrderIds>123</OrderIds>
</CreateOrderResult> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "427688B8-ADFB-4C4E-9D45-EF5C1FD6E23D",
  "CreateOrderResult": {
    "OrderIds": [123]
```

`},`

```json
  "Success": true
```

`}`

#### 2.7.2 Data changes

##### 2.7.2.1 ExecuteDataCorrect

Creates a ticket to modify data. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ExecuteDataCorre ct | The operation that you want to perform. Set the value to Execut eDat aCorrect . |
| OrderId | Long | Yes | 123 | The ID of the ticket. |
| Tid | String | No | -1 | The ID of the tenant. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ActionDetail | Json | No | { "startTime" : null, "endTime" : null, "transaction" : false, "backupData" : true } | The parameters that are required to perform the operation. json "actionDetail" : { "startTime" : null, // The start of the required time range. If you want to immediately modify data , you do not need to set the parameter. "endTime" : null, // The end of the required time range. If you want to immediately modify data , you do not need to set the parameter. "transaction" : false, // Specifies whether to run the modification task as a transaction. "backupData" : true // Specifies whether to back up data. } |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The error code that is returned. |
| ErrorMessage | String | UnknownError | The error message that is returned. |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ExecuteDataCorrect &OrderId=123 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>7133DF67-5B25-460F-8285-C4CC93472C2F</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "7133DF67-5B25-460F-8285-C4CC93472C2F",
  "Success": true
```

`}`

##### 2.7.2.2 GetDataCorrectBackupFiles

Queries the download URL of an attachment that includes the backup files of data changes. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetDataCorrectBa ckupFiles | The operation that you want to perform. Set the value to Get Dat aCorrect BackupFiles. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| OrderId | Long | Yes | 12345 | The ID of the ticket. |
| Tid | Long | No | -1 | The ID of the tenant. |
| ActionDetail | Json | No | {} | The parameters that are required to perform the operation. You do not need to specify this parameter. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataCorrectBac kupFiles | List | xxx | The download URL of the attachment that includes backup files. |
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GetDataCorrectBackupFiles &OrderId=12345 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DataCorrectBackupFiles>
    <FileUrl>https://xxx.oss-cn-hangzhou.aliyuncs.com/xxx.zip?Expires=1574382979&amp;OSSAcc
essKeyId=wSa97B52GzF4fGqu&amp;Signature=ykWSysajKcQjXjG0X4ApOQvlIXQ%3D</FileUrl> </DataCorrectBackupFiles> <RequestId>4AFF4109-FEFB-44E8-96A3-923B1FA8C46E</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "DataCorrectBackupFiles": {
    "FileUrl": [
      "https://xxx.oss-cn-hangzhou.aliyuncs.com/xxx.zip?Expires=1574382979&OSSAccessKeyId=w
Sa97B52GzF4fGqu&Signature=ykWSysajKcQjXjG0X4ApOQvlIXQ%3D"
```

`]` `},`

```json
  "RequestId": "4AFF4109-FEFB-44E8-96A3-923B1FA8C46E",
  "Success": true
```

`}`

##### 2.7.2.3 GetDataCorrectOrderDetail

Queries the details about a ticket that is used to modify data. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetDataCorrectOr derDetail | The operation that you want to perform. Set the value to Get Dat aCorrect OrderDet ail. |
| OrderId | Long | Yes | 12345 | The ID of the ticket. |
| Tid | Long | No | -1 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataCorrectOrd erDetail | Struct |   | The details about the ticket. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DatabaseList | Array of Database |   | The details about the database whose data is modified. |
| Database |   |   |   |
| DbId | Integer | 123456 | The ID of the database. |
| DbType | String | mysql | The type of the database. |
| EnvType | String | product | The type of the environment to which the database belongs. |
| Logic | Boolean | false | Indicates whether the database is a logical database. |
| SearchName | String | xxx@xxx:3306 | The name that is used to search for the logical database. |
| OrderDetail | Struct |   | The details about the ticket. |
| ActualAffectRo ws | Long | 100 | The number of rows that are affected by the system check. |
| AttachmentNa me | String | xxx | The attachment that includes the executed SQL statement. |
| Classify | String | test | The category of the reason for the data change. |
| EstimateAffect Rows | Long | 100 | The estimated number of affected rows. |
| ExeSQL | String | update t1 set name = 'xxx' where id <= 100 | The SQL statement that is executed. |
| IgnoreAffectRo ws | Boolean | false | Indicates whether the pre-check is ignored. |
| IgnoreAffectRo wsReason | String | test | The reason why the pre-check is ignored. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RbAttachment Name | String | test | The attachment that includes the SQL statement used to roll back the updated data. |
| RbSQL | String | empty | The SQL statement that is specified to roll back the updated data. |
| RbSQLType | String | text | The type of the attachment file. Valid values: TEXT ATTACHMENT |
| SqlType | String | text | The type of the SQL statement. Valid values: TEXT ATTACHMENT |
| PreCheckDetail | Array of TaskCheckDO |   | The details about the precheck task. |
| TaskCheckDO |   |   |   |
| CheckStatus | String | SUCCESS | The status of the precheck task. Valid values: WAITING: The ticket is pending check. RUNNING: The ticket is being checked. SUCCESS: The ticket is checked. FAIL: The ticket fails to be checked. |
| CheckStep | String | PERMISSION CHECK _ | The check step. Valid values: SQL PARSE: The system parses the SQL _ statement. SQL TYPE CHECK: The system checks the _ _ type of the SQL statement. PERMISSION CHECK: The system checks the _ permissions of the SQL statement. ROW CHECK: The system checks the _ number of rows. |
| UserTip | String | tip messsage | The message that appears when a check step is executed. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GetDataCorrectOrderDetail &OrderId=12345 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>ACE263E5-CF5F-44DD-A7B1-42C5E78E9650</RequestId> <DataCorrectOrderDetail>
    <PreCheckDetail>
        <TaskCheckDO>
            <CheckStatus>SUCCESS</CheckStatus>
            <CheckStep>SQL_PARSE</CheckStep>
        </TaskCheckDO>
        <TaskCheckDO>
            <CheckStatus>SUCCESS</CheckStatus>
            <CheckStep>SQL_TYPE_CHECK</CheckStep>
        </TaskCheckDO>
        <TaskCheckDO>
            <CheckStatus>SUCCESS</CheckStatus>
            <CheckStep>PERMISSION_CHECK</CheckStep>
        </TaskCheckDO>
        <TaskCheckDO>
            <CheckStatus>SUCCESS</CheckStatus>
            <UserTip>This is a statistical value that is generated by the system. The actua
l number of affected rows is subject to the SQL statement that is executed.</UserTip>
            <CheckStep>ROW_CHECK</CheckStep>
        </TaskCheckDO>
    </PreCheckDetail>
    <OrderDetail>
        <ActualAffectRows>0</ActualAffectRows>
        <RbSQLType>TEXT</RbSQLType>
        <ExeSQL>update base_user set id = 1 where id = 1;</ExeSQL>
        <EstimateAffectRows>1</EstimateAffectRows>
        <SqlType>TEXT</SqlType>
        <Classify>test</Classify>
        <IgnoreAffectRowsReason/>
    </OrderDetail>
</DataCorrectOrderDetail> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "ACE263E5-CF5F-44DD-A7B1-42C5E78E9650",
  "DataCorrectOrderDetail": {
    "PreCheckDetail": {
      "TaskCheckDO": [
```

`{`

```json
          "CheckStatus": "SUCCESS",
          "CheckStep": "SQL_PARSE"
```

`},` `{`

```json
          "CheckStatus": "SUCCESS",
          "CheckStep": "SQL_TYPE_CHECK"
```

`},` `{`

```json
          "CheckStatus": "SUCCESS",
          "CheckStep": "PERMISSION_CHECK"
```

`},` `{`

```json
          "CheckStatus": "SUCCESS",
          "UserTip": "This is a statistical value that is generated by the system. The actu
al number of affected rows is subject to the SQL statement that is executed.",
          "CheckStep": "ROW_CHECK"
```

`}` `]` `},`

```json
    "OrderDetail": {
      "ActualAffectRows": 0,
      "RbSQLType": "TEXT",
      "ExeSQL": "update base_user set id = 1 where id = 1;",
      "EstimateAffectRows": 1,
      "SqlType": "TEXT",
      "Classify": "test",
      "IgnoreAffectRowsReason": ""
```

`}` `},`

```json
  "Success": true
```

`}`

#### 2.7.3 Schema design

##### 2.7.3.1 CreatePublishGroupTask

Creates a ticket to modify the schema design of a database. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreatePublishGro upTask | The operation that you want to perform. Set the value to Creat ePublishGroupT ask. |
| DbId | Integer | Yes | 12345 | The ID of the database for which you want to modify the schema design. |
| Logic | Boolean | Yes | false | Specifies whether the database is a logical database. |
| OrderId | Long | Yes | 142435 | The ID of the ticket. |
| PublishStrategy | String | Yes | IMMEDIATELY | The policy to modify the schema design. Valid values: IMMEDIATELY: immediately modifies the schema design. REGULARLY: modifies the schema design at a scheduled time. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| PlanTime | String | No | 2019-10-10 00:00:00 | The time to modify the schema design. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The error code that is returned. |
| ErrorMessage | String | UnknownError | The error message that is returned. |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| TaskId | Long | 413452 | The ID of the task. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreatePublishGroupTask &DbId=12345 &Logic=false &OrderId=142435 &PublishStrategy=IMMEDIATELY &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>78C93646-D9B1-4E6E-B5FD-C69F94A7905A</RequestId> <Success>true</Success> <TaskId>13424</TaskId>
```

`JSON` format `{`

```json
  "RequestId": "78C93646-D9B1-4E6E-B5FD-C69F94A7905A",
  "Success": true,
  "TaskId": 13424
```

`}`

#### 2.7.4 Data export

##### 2.7.4.1 ExecuteDataExport

Executes a ticket to export data. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ExecuteDataExpo rt | The operation that you want to perform. Set the value to Execut eDat aExport . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ActionDetail | Json | Yes | { "fileType": "CSV", "encoding": "" } | The parameters that are required to perform the operation: json { "fileType": "CSV", // The format of the file to which the data is exported. "encoding": "" // The encoding of the file. } |
| OrderId | Long | Yes | 1234 | The ID of the ticket. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | FE8EE2F1-4880- 46BC-A704- 5CF63EAF9A04 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?ActionDetail={ "fileType": "CSV", "encoding": "" } &OrderId=1234 &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>FE8EE2F1-4880-46BC-A704-5CF63EAF9A04</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "FE8EE2F1-4880-46BC-A704-5CF63EAF9A04",
  "Success": true
```

`}`

##### 2.7.4.2 GetDataExportDownloadURL

Queries the download URL of the file that includes export results for a data export ticket. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetDataExportDo wnloadURL | The operation that you want to perform. Set the value to Get Dat aExport DownloadURL. |
| OrderId | Long | Yes | 12345 | The ID of the ticket. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DownloadURLR esult | Struct |   | The details about the file that includes export results. |
| HasResult | Boolean | true | Indicates whether a file is available for download. |
| TipMessage | String | tip message | The message that indicates an exception. |
| URL | String | xxx | The download URL of the file that includes export results. |

| Data Management |   |   | Developer Guide·API Referenc |
|---|---|---|---|
| Parameter | Type | Example | Description |

| ErrorCode | String | UnknownError | The error code that is returned. |
|---|---|---|---|
| ErrorMessage | String | UnknownError | The error message that is returned. |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GetDataExportDownloadURL &OrderId=12345 &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DownloadURLResult>
    <URL>https://dms-idb-hangzhou.oss-cn-hangzhou.aliyuncs.com/xxx.zip?Expires=1574384313&a
mp;OSSAccessKeyId=wSa97B52GzF4fGqu&amp;Signature=HQQWBRSKiVV6cupugh1/eAVSqXg%3D</URL>
    <HasResult>true</HasResult>
</DownloadURLResult> <RequestId>4BF24EA5-9013-4C85-AE68-6C23AF5E0097</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "DownloadURLResult": {
    "URL": "https://dms-idb-hangzhou.oss-cn-hangzhou.aliyuncs.com/xxx.zip?Expires=157438431
3&OSSAccessKeyId=wSa97B52GzF4fGqu&Signature=HQQWBRSKiVV6cupugh1/eAVSqXg%3D",
    "HasResult": true
```

`},`

```json
  "RequestId": "4BF24EA5-9013-4C85-AE68-6C23AF5E0097",
  "Success": true
```

`}`

##### 2.7.4.3 GetDataExportOrderDetail

Queries the details about a ticket that is used to export data. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetDataExportOr derDetail | The operation that you want to perform. Set the value to Get Dat aExport OrderDet ail. |
| OrderId | Long | Yes | 123456 | The ID of the ticket. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataExportOrd erDetail | Struct |   | The details about the ticket. |
| KeyInfo | Struct |   | The status information. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| JobStatus | String | EXPORT SUCCESS _ | The status of the ticket. Valid values: PRE CHECKING: The ticket is being pre- _ checked. PRE CHECK SUCCESS: The ticket is pre- _ _ checked. PRE CHECK FAIL: The ticket fails to be pre- _ _ checked. WAITING APPLY AUDIT: The ticket is being _ _ submitted for approval. APPLY AUDIT SUCESS: The ticket is _ _ submitted for approval. ENABLE EXPORT: The ticket is approved. _ Data can be exported. WAITING EXPORT: The data is pending _ export. DOING EXPORT: The data is being _ exported. EXPORT FAIL: The data fails to be _ exported. EXPORT SUCCESS: The data is exported. _ |
| PreCheckId | Long | 123 | The ID of the precheck task. |
| OrderDetail | Struct |   | The details about the ticket. |
| ActualAffectRo ws | Long | 1 | The number of rows that are affected by the system check. |
| Classify | String | text | The category of the reason for the data export. |
| Database | String | xxx@xxx:3306 | The database from which data is exported. |
| DbId | Integer | 123 | The ID of the database. |
| EnvType | String | test | The type of the environment to which the database belongs. |
| ExeSQL | String | select 1 | The SQL statement that is executed to export data. |

| Developer Guide·AP | I Reference |   | Data Managemen |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| IgnoreAffectRo ws | Boolean | false | Indicates whether the affected rows are skipped. |
| IgnoreAffectRo wsReason | String | empty | The reason why the pre-check is skipped. |
| Logic | Boolean | false | Indicates whether the database is a logical database. |
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GetDataExportOrderDetail &OrderId=123456 &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DataExportOrderDetail>
    <KeyInfo>
        <PreCheckId>15544</PreCheckId>
        <JobStatus>EXPORT_SUCCESS</JobStatus>
    </KeyInfo>
    <OrderDetail>
        <Logic>false</Logic>
        <ActualAffectRows>1</ActualAffectRows>
        <ExeSQL>select 1;</ExeSQL>
        <Database>yuyang_test@xxx:3306[yuyang_test_xxx]China (Hangzhou) non-modular databas
e</Database>
        <IgnoreAffectRows>false</IgnoreAffectRows>
        <DbId>116367</DbId>
        <Classify>Test</Classify>
        <EnvType>product</EnvType>
    </OrderDetail>
</DataExportOrderDetail> <RequestId>78C93646-D9B1-4E6E-B5FD-C69F94A7905A</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "DataExportOrderDetail": {
    "KeyInfo": {
      "PreCheckId": 15544,
      "JobStatus": "EXPORT_SUCCESS"
```

`},`

```json
    "OrderDetail": {
      "Logic": false,
      "ActualAffectRows": 1,
      "ExeSQL": "select 1;",
      "Database": <Database>yuyang_test@xxx:3306[yuyang_test_xxx]China (Hangzhou) non-modul
ar database</Database>
      "IgnoreAffectRows": false,
      "DbId": 116367,
      "Classify": "Test",
      "EnvType": "product"
```

`}` `},`

```json
  "RequestId": "78C93646-D9B1-4E6E-B5FD-C69F94A7905A",
  "Success": true
```

`}`

### 2.8 Permission management

#### 2.8.1 RevokeUserPermission

Revokes the permissions on a specified resource from a user. Request parameters q p

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RevokeUserPermi ssion | The operation that you want to perform. Set the value to RevokeUserPermission. |
| DbId | String | Yes | 142345 | The ID of the database. |
| DsType | String | Yes | DATABASE | The type of resources. For more information, see the description of the Grant UserPermission operation. |
| PermTypes | String | Yes | QUERY | The type of permissions. For more information, see the description of the Grant UserPermission operation. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| UserAccessId | String | Yes | 123 | The ID of the user permission. |
| UserId | String | Yes | 1234 | The ID of the user. You can call the Get User operation to obtain the ID. Not e The ID is different from the ID of the Apsara Stack tenant account of the user. |
| Logic | Boolean | No | false | Specifies whether the database is a logical database. Valid values: true false |
| TableId | String | No | 1342345 | The ID of the table. This parameter is required if you grant permissions on a table to a user. |
| TableName | String | No | table name _ | The name of the table. This parameter is required if you grant permissions on a table to a user. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The error code that is returned. |
| ErrorMessage | String | UnknownError | The error message that is returned. |
| RequestId | String | A99CD576-1E18- 4E86-931E- C3CCE56DC030 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=RevokeUserPermission &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>A99CD576-1E18-4E86-931E-C3CCE56DC030</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "A99CD576-1E18-4E86-931E-C3CCE56DC030",
  "Success": true
```

`}`

#### 2.8.2 ListDatabaseUserPermssions

Queries the permissions of users on a database. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListDatabaseUser Permssions | The operation that you want to perform. Set the value to List Dat abaseUserPermssions. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DbId | String | Yes | 123 | The ID of the database. |
| PermType | String | Yes | DATABASE | The type of the permission. Valid values: DATABASE: permissions on databases. TABLE: permissions on tables. COLUMN: permissions on columns. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| Logic | Boolean | No | false | Specifies whether the database is a logical database. |
| UserName | String | No | search user nam _ _ e | The nickname of the user. |
| PageNumber | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The error code that is returned. |
| ErrorMessage | String | UnknownError | The error message that is returned. |
| RequestId | String | 68075D06-7406- 4887-83A7- F558A4D28C13 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeds. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Long | 1 | The total number of entries that meet the query conditions. |
| UserPermission s | Array of UserPermission |   | The details of user permissions. |
| UserPermission |   |   |   |
| Alias | String | instance alias _ | The alias of the instance. |
| ColumnName | String | column name _ | The name of the field. |
| DbId | String | 1234 | The ID of the database. |
| DbType | String | mysql | The type of the database. |
| DsType | String | DATABASE | The type of resources on which the user has permissions. |
| EnvType | String | product | The type of the environment to which the database belongs. |
| InstanceId | String | 1443 | The ID of the instance. |
| Logic | Boolean | false | Specifies whether the database is a logical database. |
| PermDetails | Array of PermDetail |   | The details of permissions. |
| PermDetail |   |   |   |
| CreateDate | String | 2019-12-12 00:00:00 | The time when the permission was created. |
| ExpireDate | String | 2020-12-12 00:00:00 | The time when the permission expires. |
| ExtraData | String | DEFAULT | The extra information. This parameter is reserved. |
| OriginFrom | String | xxx grant | The entity that authorizes the permission. |

| Developer Guide·AP | I Reference |   | Data Managemen |
|---|---|---|---|
| Parameter | Type | Example | Description |

| PermType | String | QUERY | The type of the permission. Valid values: QUERY: the query permission. EXPORT: the export permission. CORRECT: the change permission. |
|---|---|---|---|
| UserAccessId | String | 13434 | The ID of the authorization record. |
| SchemaName | String | xxx@xxxx:3306 | The name of the schema. |
| SearchName | String | xxx | The name that is used to search for the database. |
| TableId | String | 42345 | The ID of the table. |
| TableName | String | table name _ | The name of the table. |
| UserId | String | 14324 | The ID of the user. |
| UserNickName | String | user nick name _ _ | The name of the user. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListDatabaseUserPermssions &DbId=123 &PermType=DATABASE &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UserPermissions>
    <UserPermission>
        <Logic>false</Logic>
        <UserNickName>xxx</UserNickName>
        <DsType>DATABASE</DsType>
        <Alias>beihe_ent_prod</Alias>
        <PermDetails>
            <PermDetail>
                <ExpireDate>2020-10-31 00:00:00</ExpireDate>
                <UserAccessId>390915</UserAccessId>
                <PermType>QUERY</PermType>
                <OriginFrom>xxx</OriginFrom>
                <CreateDate>2019-11-21 15:07:45</CreateDate>
            </PermDetail>
            <PermDetail>
                <ExpireDate>2020-10-31 00:00:00</ExpireDate>
                <UserAccessId>390916</UserAccessId>
                <PermType>EXPORT</PermType>
                <OriginFrom>xxx</OriginFrom>
                <CreateDate>2019-11-21 15:07:45</CreateDate>
            </PermDetail>
            <PermDetail>
                <ExpireDate>2020-10-31 00:00:00</ExpireDate>
                <UserAccessId>390917</UserAccessId>
                <PermType>CORRECT</PermType>
                <OriginFrom>xxx</OriginFrom>
                <CreateDate>2019-11-21 15:07:45</CreateDate>
            </PermDetail>
        </PermDetails>
        <InstanceId>1434</InstanceId>
        <SearchName>xxx@xxxx:3306</SearchName>
        <DbId>123434</DbId>
        <UserId>432423</UserId>
        <DbType>drds</DbType>
        <EnvType>product</EnvType>
        <SchemaName>xxx</SchemaName>
    </UserPermission>
</UserPermissions> <TotalCount>1</TotalCount> <RequestId>68075D06-7406-4887-83A7-F558A4D28C13</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "UserPermissions": {
    "UserPermission": [
```

`{`

```json
        "Logic": false,
        "UserNickName": "xxx",
        "DsType": "DATABASE",
        "Alias": "beihe_ent_prod",
        "PermDetails": {
          "PermDetail": [
```

`{`

```json
              "ExpireDate": "2020-10-31 00:00:00",
              "UserAccessId": "390915",
              "PermType": "QUERY",
              "OriginFrom": "xxx",
              "CreateDate": "2019-11-21 15:07:45"
```

`},` `{`

```json
              "ExpireDate": "2020-10-31 00:00:00",
              "UserAccessId": "390916",
              "PermType": "EXPORT",
              "OriginFrom": "xxx",
              "CreateDate": "2019-11-21 15:07:45"
```

`},` `{`

```json
              "ExpireDate": "2020-10-31 00:00:00",
              "UserAccessId": "390917",
              "PermType": "CORRECT",
              "OriginFrom": "xxx",
              "CreateDate": "2019-11-21 15:07:45"
```

`}` `]` `},`

```json
        "InstanceId": 1434,
        "SearchName": "xxx@xxxx:3306",
        "DbId": 123434,
        "UserId": 432423,
        "DbType": "drds",
        "EnvType": "product",
        "SchemaName": "xxx"
```

`}` `]` `},`

```json
  "TotalCount": 1,
  "RequestId": "68075D06-7406-4887-83A7-F558A4D28C13",
  "Success": true
```

`}`

#### 2.8.3 SetOwners

Sets the owners of a database or a table. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetOwners | The operation that you want to perform. Set the value to Set Owners. |
| OwnerIds | String | Yes | 123, 456 | The IDs of the owners. Separate multiple IDs with commas (,). |
| OwnerType | String | Yes | DATABASE | The type of the owner. Valid values: DATABASE: an owner of physical databases. LOGIC DATABASE: an owner of _ logical databases. TABLE: an owner of physical tables. LOGIC TABLE: an owner of logical _ tables. |
| ResourceId | String | Yes | 123 | The ID of the resource. The ID is based on the value of the OwnerT ype parameter. Valid values for the OwnerT ype parameter: DATABASE: physical databases. LOGIC DATABASE: logical databases. _ TABLE: physical tables. LOGIC TABLE: logical tables. _ |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | A99CD576-1E18- 4E86-931E- C3CCE56DC030 | The ID of the request. |

|   | Developer Guide·AP | I Reference |   | Data Managemen | t |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SetOwners &OwnerIds=123, 456 &OwnerType=DATABASE &ResourceId=123 &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>A99CD576-1E18-4E86-931E-C3CCE56DC030</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "A99CD576-1E18-4E86-931E-C3CCE56DC030",
  "Success": true
```

`}`

#### 2.8.4 ListUserPermissions

Queries the permissions of a user on databases and tables. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListUserPermissio ns | The operation that you want to perform. Set the value to List UserPermissions. |
| PermType | String | Yes | DATABASE | The type of resources on which the user has permissions. For more information, see List Dat abaseUserPermssions. |
| Tid | Long | Yes | -1 | The ID of the tenant. |

| ata Management |   |   |   | Developer Guide·API Referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| UserId | String | Yes | 13435 | The ID of the user. The user ID is the same as the user ID that is specfied in the Get User operation. The user ID is different from the ID of your Apsara Stack tenant account. |
| DatabaseName | String | No | db name _ | The name of the database. |
| Logic | Boolean | No | false | Specifies whether the database is a logical database. Valid values: true false |
| EnvType | String | No | dev | The type of the environment to which the database belongs. |
| DbType | String | No | MySQL | The type of the database. |
| PageNumber | Integer | No | 1 | The number of the page to return |
| PageSize | Integer | No | 1 | The number of entries to return on each page. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | C51420E3-144A- 4A94-B473- 8662FCF4AD10 | The ID of the request. |
| Success | Boolean | true | Indicates whether the call succeeded. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Long | 6 | The total number of entries that meet the query conditions. |
| UserPermission s | Array of UserPermission |   | The details of user permissions. |
| UserPermission |   |   |   |
| Alias | String | instance alias _ | The alias of the instance. |
| ColumnName | String | column name _ | The name of the field. |
| DbId | String | 1324 | The ID of the database. |
| DbType | String | mysql | The type of the database. |
| DsType | String | DATABASE | The type of resources on which the user has permissions. |
| EnvType | String | dev | The type of the environment to which the database belongs. |
| InstanceId | String | 134 | The ID of the instance. |
| Logic | Boolean | false | Indicates whether the database is a logical database. Valid values: true false |
| PermDetails | Array of PermDetail |   | The details of permissions. |
| PermDetail |   |   |   |
| CreateDate | String | 2019-12-12 00:00:00 | The time when the permission was authorized. |
| ExpireDate | String | 2020-12-12 00:00:00 | The time when the permission expires. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ExtraData | String | xxx | The additional data. This parameter is reserved. |
| OriginFrom | String | xxx | The entity that authorizes the permission. |
| PermType | String | QUERY | The type of the permission. |
| UserAccessId | String | 1345 | The ID of the authorization record. |
| SchemaName | String | test db _ | The name of a database. |
| SearchName | String | test db@xxx:3306 _ | The name that is used to search for the database. |
| TableId | String | 13434 | The ID of the table. |
| TableName | String | test table _ | The name of the table. |
| UserId | String | 423245 | The ID of the user. |
| UserNickName | String | nick name _ | The name of the user. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListUserPermissions &PermType=DATABASE &Tid=-1 &UserId=13435 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UserPermissions>
    <UserPermission>
        <Logic>false</Logic>
        <UserNickName>xxx</UserNickName>
        <DsType>DATABASE</DsType>
        <Alias>xxx_ent_dev</Alias>
        <PermDetails>
            <PermDetail>
                <ExpireDate>2020-10-31 00:00:00</ExpireDate>
                <UserAccessId>390913</UserAccessId>
                <PermType>EXPORT</PermType>
                <OriginFrom>xxx</OriginFrom>
                <CreateDate>2019-11-21 15:07:45</CreateDate>
            </PermDetail>
            <PermDetail>
                <ExpireDate>2020-10-31 00:00:00</ExpireDate>
                <UserAccessId>390914</UserAccessId>
                <PermType>CORRECT</PermType>
                <OriginFrom>xxx</OriginFrom>
                <CreateDate>2019-11-21 15:07:45</CreateDate>
            </PermDetail>
        </PermDetails>
        <InstanceId>24671</InstanceId>
        <SearchName>xxx@xxx:3306</SearchName>
        <DbId>111369</DbId>
        <UserId>88658</UserId>
        <DbType>drds</DbType>
        <EnvType>dev</EnvType>
        <SchemaName>xxx_ent_dev</SchemaName>
    </UserPermission>
</UserPermissions> <TotalCount>6</TotalCount> <RequestId>C51420E3-144A-4A94-B473-8662FCF4AD10</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "UserPermissions": {
    "UserPermission": [
```

`{`

```json
        "Logic": false,
        "UserNickName": "xxx",
        "DsType": "DATABASE",
        "Alias": "xxx_ent_dev",
        "PermDetails": {
          "PermDetail": [
```

`{`

```json
              "ExpireDate": "2020-10-31 00:00:00",
              "UserAccessId": "390913",
              "PermType": "EXPORT",
              "OriginFrom": "xxx",
              "CreateDate": "2019-11-21 15:07:45"
```

`},` `{`

```json
              "ExpireDate": "2020-10-31 00:00:00",
              "UserAccessId": "390914",
              "PermType": "CORRECT",
              "OriginFrom": "xxx",
              "CreateDate": "2019-11-21 15:07:45"
```

`}` `]` `},`

```json
        "InstanceId": 24671,
        "SearchName": "xxx@xxx:3306",
        "DbId": 111369,
        "UserId": 88658,
        "DbType": "drds",
        "EnvType": "dev",
        "SchemaName": "xxx_ent_dev"
```

`}` `]` `},`

```json
  "TotalCount": 6,
  "RequestId": "C51420E3-144A-4A94-B473-8662FCF4AD10",
  "Success": true
```

`}`

#### 2.8.5 GrantUserPermission

Grants permissions on a database or a table to a user. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GrantUserPermiss ion | The operation that you want to perform. Set the value to Grant UserPermission. |
| DbId | String | Yes | 1234 | The ID of the database. |
| DsType | String | Yes | DATABASE | The type of the permissions. Valid values: DATABASE: permissions on physical databases LOGIC DATABASE: permissions on _ logical databases TABLE: permissions on physical databases LOGIC TABLE: permissions on logical _ tables |
| ExpireDate | String | Yes | 2019-12-12 00:00:00 | The time when the permissions expire. |
| PermTypes | String | Yes | QUERY, EXPORT, CORRECT | The type of the permission. Separate multiple permission types with commas (,). Valid values: QUERY: the query permission EXPORT: the export permission CORRECT: the change permission |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| UserId | String | Yes | 12345 | The ID of the user. You can call the Get User operation to obtain the user ID. The user ID is different from the Apsara Stack tenant account ID of the user. |
| Logic | Boolean | No | false | Specifies whether the database is a logical database. |
| TableId | String | No | 1324245 | The ID of the table. This parameter is required when you grant permissions on a table. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TableName | String | No | table name _ | The name of the table. This parameter is required when you grant permissions on a table. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | A99CD576-1E18- 4E86-931E- C3CCE56DC030 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GrantUserPermission &DbId=1234 &DsType=DATABASE &ExpireDate=2019-12-12 00:00:00 &PermTypes=QUERY, EXPORT, CORRECT &Tid=-1 &UserId=12345 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>A99CD576-1E18-4E86-931E-C3CCE56DC030</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "A99CD576-1E18-4E86-931E-C3CCE56DC030",
  "Success": true
```

`}`

### 2.9 Security management

#### 2.9.1 ListSensitiveColumns

Queries sensitive columns. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListSensitiveColu mns | The operation that you want to perform. Set the value to List Sensit iveColumns. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| SchemaName | String | No | test | The name of the database. |
| TableName | String | No | test | The name of the table. |
| ColumnName | String | No | test | The name of the column. |
| SecurityLevel | String | No | SENSITIVE | The sensitivity level of the column. Valid values: INNER SENSITIVE CONFIDENTIAL |
| PageNumber | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | 0E714EF1-E617- 4BBC-A3D2- 9552063BA942 | The ID of the request. |
| SensitiveColum nList | Array of SensitiveColum n |   | The sensitive columns. |
| SensitiveColum n |   |   |   |
| ColumnCount | Long | 1 | The number of columns. |
| ColumnName | String | test | The name of the column. |
| FunctionType | String | DEFAULT | The type of the desensitization algorithm. Valid values: DEFAULT: All characters are masked. This is the default value. FIX POS: The fixed position is masked. _ FIX CHAR: The fixed characters are _ masked. |
| SchemaName | String | test | The name of the database. |
| SecurityLevel | String | SENSITIVE | The sensitivity level of the column. |
| TableName | String | test | The name of the table. |
| Success | Boolean | true | Indicates whether the request succeeded. |
| TotalCount | Long | 10 | The total number of entries that are returned. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListSensitiveColumns &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>5</TotalCount> <RequestId>0E714EF1-E617-4BBC-A3D2-9552063BA942</RequestId> <SensitiveColumnList>
    <SensitiveColumn>
        <TableName>yuyang_test</TableName>
        <ColumnName>c1</ColumnName>
        <ColumnCount>0</ColumnCount>
        <SecurityLevel>SENSITIVE</SecurityLevel>
        <SchemaName>testdb</SchemaName>
    </SensitiveColumn>
    <SensitiveColumn>
        <TableName>yuyang_test_luanma</TableName>
        <ColumnName>c1</ColumnName>
        <ColumnCount>0</ColumnCount>
        <SecurityLevel>SENSITIVE</SecurityLevel>
        <SchemaName>testdb</SchemaName>
    </SensitiveColumn>
    <SensitiveColumn>
        <TableName>yuyang_test</TableName>
        <ColumnName>id</ColumnName>
        <ColumnCount>0</ColumnCount>
        <SecurityLevel>SENSITIVE</SecurityLevel>
        <SchemaName>testdb</SchemaName>
    </SensitiveColumn>
    <SensitiveColumn>
        <TableName>yuyang_test_luanma</TableName>
        <ColumnName>id</ColumnName>
        <ColumnCount>0</ColumnCount>
        <SecurityLevel>SENSITIVE</SecurityLevel>
        <SchemaName>testdb</SchemaName>
    </SensitiveColumn>
    <SensitiveColumn>
        <TableName>yuyang_test_json</TableName>
        <ColumnName>id</ColumnName>
        <ColumnCount>0</ColumnCount>
        <SecurityLevel>CONFIDENTIAL</SecurityLevel>
        <SchemaName>test_demo</SchemaName>
    </SensitiveColumn>
</SensitiveColumnList> <Success>true</Success>
```

`JSON` format `{`

```json
  "TotalCount": 5,
  "RequestId": "0E714EF1-E617-4BBC-A3D2-9552063BA942",
  "SensitiveColumnList": {
    "SensitiveColumn": [
```

`{`

```json
        "TableName": "yuyang_test",
        "ColumnName": "c1",
        "ColumnCount": 0,
        "SecurityLevel": "SENSITIVE",
        "SchemaName": "testdb"
```

`},` `{`

```json
        "TableName": "yuyang_test_luanma",
        "ColumnName": "c1",
        "ColumnCount": 0,
        "SecurityLevel": "SENSITIVE",
        "SchemaName": "testdb"
```

`},` `{`

```json
        "TableName": "yuyang_test",
        "ColumnName": "id",
        "ColumnCount": 0,
        "SecurityLevel": "SENSITIVE",
        "SchemaName": "testdb"
```

`},` `{`

```json
        "TableName": "yuyang_test_luanma",
        "ColumnName": "id",
        "ColumnCount": 0,
        "SecurityLevel": "SENSITIVE",
        "SchemaName": "testdb"
```

`},` `{`

```json
        "TableName": "yuyang_test_json",
        "ColumnName": "id",
        "ColumnCount": 0,
        "SecurityLevel": "CONFIDENTIAL",
        "SchemaName": "test_demo"
```

`}` `]` `},`

```json
  "Success": true
```

`}`

#### 2.9.2 ListSensitiveColumnsDetail

Queries the details of sensitive fields. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListSensitiveColu mnsDetail | The operation that you want to perform. Set the value to List Sensit iveColumnsDet ail. |
| ColumnName | String | Yes | test | The name of the field. |
| SchemaName | String | Yes | test | The name of the database. |
| TableName | String | Yes | test | The name of the table. |
| Tid | Long | Yes | 1 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | 7629888F-C9FB- 4D16-A7D3- B443FE06FBD4 | The ID of the request. |
| SensitiveColum nsDetailList | Array of SensitiveColum nsDetail |   | The details about the sensitive fields. |
| SensitiveColum nsDetail |   |   |   |
| ColumnDescript ion | String | test | The description of the field. |
| ColumnName | String | test | The name of the field. |
| ColumnType | String | varchar(32) | The data type of the field. |
| DbId | Long | 124 | The ID of the database. |

| Data Management |   |   | Developer Guide·API Referenc |
|---|---|---|---|
| Parameter | Type | Example | Description |
| DbType | String | mysql | The type of the database. |
| EnvType | String | product | The type of the environment to which the database belongs. |
| Logic | Boolean | false | Indicates whether the database is a logical database. |
| SchemaName | String | test | The name of the database. |
| SearchName | String | test@xxx:3306 | The name that is used to search for the database. |
| TableName | String | test | The name of the table. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListSensitiveColumnsDetail &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>7629888F-C9FB-4D16-A7D3-B443FE06FBD4</RequestId> <SensitiveColumnsDetailList>
    <SensitiveColumnsDetail>
        <TableName>king_info</TableName>
        <ColumnName>mobile</ColumnName>
        <ColumnType>varchar(64)</ColumnType>
        <SearchName>p***@xxx.mysql.rds.aliyuncs.com:3306【xxx】</SearchName>
        <ColumnDescription>mobile</ColumnDescription>
        <DbId>8511149</DbId>
        <Logic>false</Logic>
        <SchemaName>poc_prod</SchemaName>
        <EnvType>product</EnvType>
        <DbType>mysql</DbType>
    </SensitiveColumnsDetail>
</SensitiveColumnsDetailList> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "7629888F-C9FB-4D16-A7D3-B443FE06FBD4",
  "SensitiveColumnsDetailList": {
    "SensitiveColumnsDetail": [
```

`{`

```json
        "TableName": "king_info",
        "ColumnName": "mobile",
        "ColumnType": "varchar(64)",
        "SearchName": "p***@xxx.mysql.rds.aliyuncs.com:3306【xxx】",
        "ColumnDescription": "mobile",
        "DbId": 8511149,
        "Logic": false,
        "SchemaName": "poc_prod",
        "EnvType": "product",
        "DbType": "mysql"
```

`}` `]` `},`

```json
  "Success": true
```

`}`

### 2.10 Data query

#### 2.10.1 ExecuteScript

Executes SQL statements. This operation is available only for instances that are managed in the security collaboration mode. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ExecuteScript | The operation that you want to perform. Set the value to Execut eScript . |
| DbId | Integer | Yes | 123 | The ID of the database. Not e You can obtain the database ID from the Dat abaseId parameter that is returned by the Get Dat abase operation. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Logic | Boolean | Yes | false | A Boolean value that indicates whether the database to be affected is a logical database. |
| Script | String | Yes | select dt from report daily _ | The SQL statements to be executed. Data query language (DQL) statements, data definition language (DDL) statements, and data manipulation language (DML) statements are supported. The control mode of the instance that you want to query determines whether you can execute DDL and DML statements. |
| Tid | Long | No | 234 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The error code that is returned. |
| ErrorMessage | String | UnknownError | The error message that is returned. |
| RequestId | String | FE8EE2F1-4880- 46BC-A704- 5CF63EAF9A04 | The ID of the request. |
| Results | Array of Result |   | The results that are returned by the SQL statements in the format of an array. Each entry in the array indicates the result of an SQL statement. |
| ColumnNames | List | ["col1", "col2"] | The fields that are returned by the SQL statement. |
| Message | String | UnknownError | The error message that is returned if the call fails. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RowCount | Long | 1 | The total number of entries that are returned. |
| Rows | List | [{"col1": "value1", "col2":"value2"}] | The rows that are returned by the SQL statement. |
| Success | Boolean | true | Indicates whether the SQL statement is executed. |
| Success | Boolean | true | Indicates whether the call succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ExecuteScript &DbId=123 &Logic=false &Script=select dt from report_daily &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>FE8EE2F1-4880-46BC-A704-5CF63EAF9A04</RequestId> <Results>
    <Message>UnknownError</Message>
    <RowCount>1</RowCount>
    <Success>true</Success>
</Results> <Results>
    <ColumnNames>["col1", "col2"]</ColumnNames>
    <Rows>[{"col1": "value1", "col2":"value2"}]</Rows>
</Results> <ErrorCode>UnknownError</ErrorCode> <ErrorMessage>UnknownError</ErrorMessage> <Success>true</Success>
```

`JSON` format

```json
{"RequestId":"FE8EE2F1-4880-46BC-A704-5CF63EAF9A04","Results":[{"Message":"UnknownError","R owCount":"1","Success":"true"},{"ColumnNames":"[\"col1\", \"col2\"]","Rows":"[{\"col1\": \" value1\", \"col2\":\"value2\"}]"}],"ErrorCode":"UnknownError","ErrorMessage":"UnknownError" ,"Success":"true"}
```
