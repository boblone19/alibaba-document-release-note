---
title: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Cloud Native Distributed Database PolarDB-X Developer Guide 20220928"
product_version: "V3.14.0"
doc_version: "20220928"
pdf_pages: 245
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Cloud Native Distributed Database PolarDB-X Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.14.0/%E6%95%B0%E6%8D%AE%E5%BA%93/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.14.0%20Cloud%20Native%20Distributed%20Database%20PolarDB-X%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.14.0 Cloud Native Distributed Database PolarDB-X Developer Guide 20220928

## Table of Contents

- 1 Call SDKs for cloud services by using ASAPI
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
  - 2.2 Database management
    - 2.2.1 ChangeAccountPassword
    - 2.2.2 CheckDrdsDbName
    - 2.2.3 CheckExpandStatus
    - 2.2.4 CheckSqlAuditEnableStatus
    - 2.2.5 CreateDrdsDB
    - 2.2.6 CreateShardTask
    - 2.2.7 DatalinkReplicationPrecheck
    - 2.2.8 DeleteShardTasks
    - 2.2.9 DescribeBackMenu
    - 2.2.10 DescribeBackupDbs
    - 2.2.11 DescribeBackupTimes
    - 2.2.12 DescribeBroadcastTables
    - 2.2.13 DescribeDbInstanceDbs
    - 2.2.14 DescribeDbInstances
    - 2.2.15 DescribeDrdsDB
    - 2.2.16 DescribeDrdsDbInstance
    - 2.2.17 DescribeDrdsDbInstances
    - 2.2.18 DescribeDrdsDbRdsNameList
    - 2.2.19 DescribeDrdsDbRdsRelationInfo
    - 2.2.20 DescribeDrdsDbTasks
    - 2.2.21 DescribeDrdsInstanceDbMonitor
    - 2.2.22 DescribeDrdsShardingDbs
    - 2.2.23 DescribeDrdsSlowSqls
    - 2.2.24 DescribeDrdsSqlAuditStatus
    - 2.2.25 DescribeExpandLogicTableInfoList
    - 2.2.26 DescribeGlobalBroadcastType
    - 2.2.27 DescribeHotDbList
    - 2.2.28 DescribeInstDbLogInfo
    - 2.2.29 DescribeRDSPerformance
    - 2.2.30 DescribeRdsPerformanceSummary
    - 2.2.31 DescribeRdsSuperAccountInstances
    - 2.2.32 DescribeRecycleBinStatus
    - 2.2.33 DescribeRecycleBinTables
    - 2.2.34 DescribeShardTaskInfo
    - 2.2.35 DescribeShardTaskList
    - 2.2.36 DescribeSqlFlashbakTask
    - 2.2.37 DescribeTable
    - 2.2.38 DescribeTableListByType
    - 2.2.39 DescribeTables
    - 2.2.40 DisableSqlAudit
    - 2.2.41 ModifyAccountPrivilege
    - 2.2.42 ModifyDrdsIpWhiteList
    - 2.2.43 ModifyRdsReadWeight
    - 2.2.44 PutStartBackup
    - 2.2.45 ReleaseHiStoreInstance
    - 2.2.46 RemoveBackupsSet
    - 2.2.47 RemoveDrdsDbFailedRecord
    - 2.2.48 RemoveRecycleBinTable
    - 2.2.49 ResetDrdsToRdsConnections
    - 2.2.50 SetupBroadcastTables
    - 2.2.51 SetupRecycleBinStatus
    - 2.2.52 SetupTable
    - 2.2.53 StartRestore
    - 2.2.54 SubmitCleanTask
    - 2.2.55 SubmitSmoothExpandPreCheck
    - 2.2.56 SubmitSmoothExpandPreCheckTask
    - 2.2.57 SubmitSmoothExpandTask
    - 2.2.58 SubmitSwitchTask
    - 2.2.59 ValidateShardTask
    - 2.2.60 RemoveDrdsDb
    - 2.2.61 RefreshDrdsAtomUrl
  - 2.3 Instance management
    - 2.3.1 CreateInstanceAccount
    - 2.3.2 DescribeDrdsDBs
    - 2.3.3 DescribeDrdsInstance
    - 2.3.4 DescribeDrdsInstanceLevelTasks
    - 2.3.5 DescribeDrdsInstanceMonitor
    - 2.3.6 DescribeDrdsInstances
    - 2.3.7 DescribeDrdsInstanceVersion
    - 2.3.8 DescribeDrdsParams
    - 2.3.9 DescribeDrdsTasks
    - 2.3.10 DescribeHiStoreInstanceInfo
    - 2.3.11 DescribeInstanceAccounts
    - 2.3.12 DescribeInstanceMenuSwitch
    - 2.3.13 DescribeInstDbSlsInfo
    - 2.3.14 DescribePreCheckResult
    - 2.3.15 DescribeStorageInstanceSubDbInfo
    - 2.3.16 EnableSqlAudit
    - 2.3.17 EnableSqlFlashbackMatchSwitch
    - 2.3.18 FlashbackRecycleBinTable
    - 2.3.19 ModifyAccountDescription
    - 2.3.20 ModifyDrdsInstanceDescription
    - 2.3.21 RemoveDrdsInstance
    - 2.3.22 RemoveInstanceAccount
    - 2.3.23 RestartDrdsInstance
    - 2.3.24 RollbackInstanceVersion
    - 2.3.25 SetBackupPolicy
    - 2.3.26 SetupDrdsParams
    - 2.3.27 SubmitRollbackTask
    - 2.3.28 SubmitSqlFlashbackTask
    - 2.3.29 SwitchGlobalBroadcastType
    - 2.3.30 UpgradeInstanceVersion

services by using ASAPI

## 1 Call SDKs for cloud services by using ASAPI

by using ASAPI

### 1.1 ASAPI Developer Guide

#### 1.1.1 ASAPI overview

This topic describes the architecture and features of the Apsara Stack API (ASAPI). The ASAPI is a unified ingress gateway for Apsara Stack services and a main component of the Apsara Uni-manager Management Console. The ASAPI provides a unified method for you to manage and make API calls. You can use Apsara Stack SDK to centrally make API calls to Apsara Stack services, including Elastic Compute Service (ECS) and Virtual Private Cloud (VPC). The ASAPI allows you to make API calls to manage and maintain Apsara Stack services. Make API calls to implement enterprise-grade management. For example, you can manage organizations, users, roles, resource sets, and logon policies. These operations are provided by the services by using ASAPI Apsara Uni-manager Management Console. Make API calls to manage operations. For example, you can manage quotas, usage statistics, specifications, and password policies. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to manage resources. For example, you can create, delete, query, or modify cloud resources. These operations are provided by Apsara Stack services. If you call an API operation to create an ECS instance or a VPC, the API operation is provided by ECS or VPC. Make API calls to query monitoring metrics of Apsara Stack services. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to perform O&M. For example, you can manage monitoring and alerting, inventories, tasks, and physical servers. These operations are provided by the Apsara Uni-manager Operations Console. For more information, see the developer guide of the corresponding Apsara Stack service. For information about API operations used to manage organization users, see Apsara Uni-manager Management Console Developer Guide. For information about the API operation used to create an ECS instance, see ECS Developer Guide. Not e If the "Use Apsara Stack SDK to make API calls" section is included in the developer guide of an Apsara Stack service, the ASAPI is supported by the Apsara Stack service. In this case, you can make API calls based on the developer guide.

#### 1.1.2 Preparations

##### 1.1.2.1 Log on to the API Tool console

You can log on to the API Tool console from the Apsara Uni-manager Management Console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. services by using ASAPI Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
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

This topic describes three methods used to generate an endpoint for the Apsara Stack API (ASAPI). services by using ASAPI Method 1: Use Registration Vars of Services to generate an endpoint
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
services by using ASAPI i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click O&M. iii. In the left-side navigation pane, choose Product Management > Product s. iv. In the Apsara Stack O&M section, click Apsara Inf rast ruct ure Management Framework.
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
root domain, contact Apsara Stack O&M personnel. Take note of this point: Use the internetdomain parameter instead of the intranet-domain parameter. If the region value is `cn-****-****-d01` and the int ernet -domain value is `inter.****.****.com` , the following endpoint can be generated: services by using ASAPI

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

services by using ASAPI

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

When you use Apsara Stack SDK for Node.js to make API calls, specify a region ID. You can obtain a region ID in the Apsara Uni-manager Management Console. Procedure services by using ASAPI
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

services by using ASAPI

| Paramet er | T ype | Required | Descript ion |
|---|---|---|---|
| Signature | String | Yes | The signature string of the current request. For more information about how signatures are calculated, see Request signatures. |
| SignatureMethod | String | Yes | The encryption method of the signature string. Valid values: HMAC- SHA1 and HMAC- SHA256. |
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Valid values: 1.0 and 2.0. |
| SignatureNonce | String | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the yyyy- MM-ddTHH:mm:ssZ format. The time must be in UTC. Sample value: 2018-01- 01T12:00:00Z. |
| Format | String | Yes | The format in which to return the response. Set the value to JSON. |

services by using ASAPI Not e

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
Method 1: Create a Maven project in IntelliJ IDEA. services by using ASAPI Method 2: Convert an existing project to a Maven project. a. Right-click the project that you want to convert and select Add Framework Support .... b. Select Maven and click OK.
4. Create a folder named libs in the root directory of the project. Then, add the JAR file of Apsara
Stack SDK for Java to the libs folder, as shown in the following figure. services by using ASAPI
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
services by using ASAPI If the information in the following figure appears, the dependencies are added. Use Apsara Stack SDK for Java You can use the GET or POST method to call API operations provided by the ASAPI. The following sample code shows how to call API operations: services by using ASAPI

```java
// 1. Create a connection to an ASClient object. ASClient client = new ASClient(); // 2. Configure the identifier of the requester. This parameter is required and used only f or identification. You can set this parameter to a random value. client.setSdkSource("<The identifier of the requester>"); Map<String, Object> parameters = new HashMap<String, Object>(); // 3. Configure the parameters for authorization. The parameter values vary based on your e nvironment. // The AccessKey ID of your Apsara Stack tenant account. parameters.put("AccessKeyId","<AccessKey ID>"); // The AccessKey secret of your Apsara Stack tenant account. parameters.put("AccessKeySecret", "<AccessKey Secret>"); // The ID of the region. parameters.put("RegionId", "<your RegionID>"); // 4. Configure parameters for an API call. In this example, the Product, Action, and Versi on parameters are configured. parameters.put("Product", "<The name of the service>"); parameters.put("Action", "<The name of the API operation>"); parameters.put("Version", "<The version of the API operation>"); // 5. Configure operation-specific parameters. parameters.put("<The name of the operation-specific parameter>", "<The value of the operati on-specific parameter>"); // 6. Configure request headers and the encryption method for the signature string. Valid v alues of the SignatureMethod parameter: HMAC-SHA1 and HMAC-SHA256. By default, HMAC-SHA256 is used. Map<String, String> headers = new HashMap<String, String>(); //headers.put("SignatureMethod", "HMAC-SHA1"); headers.put("x-acs-regionid", "<your-regionid>"); headers.put("x-acs-resourcegroupid", "<your-resourcegroupid>"); headers.put("x-acs-organizationid", "<your-organizationid>"); headers.put("x-acs-instanceid", "<your-instanceid>"); // 7. Make an API call. We recommend that you use the doPost() method. // Configure the time-out period for a connection. //client.setConnectTimeout(10000); // Configure the time-out period for a request. // client.setSocketTimeout(10000); String result = client.doPost(endpoint, headers, parameters); System.out.println(result);
```

Configure a proxy If you need to use a proxy to make API calls, use the following sample code to configure the proxy:

```
Cloud cloud = new Cloud(); // Configure the IP address of the proxy. cloud.setConfig("proxy_host", "<IP>"); // Configure the port used by the proxy. cloud.setConfig("proxy_port", "<Port>"); // 1. Create a connection to an ASClient object. ASClient client = new ASClient(cloud);
```

Request headers services by using ASAPI

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

Not e Replace `2.4.7` with the actual version of Apsara Stack SDK for Python. You can use the GET or POST method to call API operations provided by the ASAPI. services by using ASAPI

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

services by using ASAPI Configure a proxy Perform the following steps to configure a proxy:
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

Use Apsara Stack SDK for Node.js The following sample code shows how to use Apsara Stack SDK for Node.js to make API calls: services by using ASAPI

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

services by using ASAPI Request headers

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

services by using ASAPI Call examples The following sample code provides an example on how to use the RPC style to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05-26. Sample code:

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

services by using ASAPI

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

services by using ASAPI

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

This topic describes how to use Apsara Stack API (ASAPI) SDK for POP for Go. Prerequisites An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed. Background information Only the remote procedure call (RPC) style is supported for API calls. Call examples The following sample code provides an example on how to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05- 26. services by using ASAPI Sample code:

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

services by using ASAPI

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

This topic describes how to use Apsara Stack API (ASAPI) SDK for POP for Python. Prerequisites An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed. Background information Only the remote procedure call (RPC) style is supported for API calls. services by using ASAPI Call examples The following sample code provides an example on how to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05- 26. Sample code:

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

Configure proxies services by using ASAPI Set the HTTP_PROXY and HTTPS_PROXY environment variables. Sample code:

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

`https` : the protocol used to transmit the request. `public.asapi.aliyuns.com/asapi/v3` : the endpoint of the ASAPI. `Action=GetOrganizationList Product=ascm Version=2019-05-10` : the API operation to call. `Id` : the ID of the organization. `<Common parameters>` : the common parameters specified in the system. services by using ASAPI Protocol The ASAPI supports only HTTPS. Endpoint For more information about how to obtain an endpoint, see Generate an endpoint for the ASAPI. To specify an API operation, use the `Action, Product, and Version` parameters. For example, set `Action` to GetOrganizationList, Product to ascm, and Version to 2019-05-10. You must also specify other operation-specific parameters and common parameters. For more information, see Common parameters.

##### 1.1.5.3 Request signatures

This topic describes how to sign HTTP API requests. ASAPI uses the request signature to verify the identity of the request sender. ASAPI implements symmetric encryption by using an AccessKey pair to verify the identity of the request sender. Not e An AccessKey pair consists of an AccessKey ID and an AccessKey secret, which are issued to each user or organization in the Apsara Uni-manager Management Console. The AccessKey ID is used to verify identities of users, and the AccessKey secret is used to encrypt and verify signature strings. You must keep your AccessKey secret confidential. ASAPI provides SDKs for Node.js, Python, and Java to facilitate complex signature calculation. For more information, see Obtain the core package for ASAPI. Step 1: Create a canonicalized query string
1. Arrange the request parameters in alphabetical order, including all common and operation-specific
parameters except the `Signature` parameter. Not e If you use the GET method to send a request,these parameters are connected by ampersands (&) and included in the request URL. The first request parameter follows a question mark (?).
2. Encode the request parameters and their values in UTF-8 based on RFC 3986. The following rules
apply in the encoding process: Letters, digits, and special characters such as hyphens ( `-` ), underscores ( `_` ), and periods ( `.` ) do not need to be encoded. services by using ASAPI Other characters must be percent encoded in the %XY format. `XY` represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks ( `"` ) are encoded as %22 . Extended UTF-8 characters are encoded in the %XY%ZA… format. Spaces must be encoded as %20 . Do not encode spaces as plus signs ( `+` ). This encoding method is similar to but different from the `application/x-www-form-urlencoded` MIME encoding algorithm. If you use `java.net.URLEncoder` from the Java standard library, use `percentEncode` to encode request parameters and their values. In the encoded query string, replace the plus signs ( `+` ) with %20 , asterisks ( `*` ) with %2A , and %7E with tildes ( ~ ). This way, you can obtain an encoded string that matches the preceding encoding rules.

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

services by using ASAPI Not e When you calculate the signature, the key value specified by RFC 2104 is your `AccessKey secret` plus an ampersand (&), which has an ASCII value of 38. For more information, see Obtain an AccessKey pair.
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

You can use browsers or tools such as cURL and Wget to initiate an HTTP request for calling the `DescribeRegions` operation to query the Alibaba Cloud region list. Example 2: Use t he st andard library of t he programming language services by using ASAPI `GetOrganizationList` is used in this example to query regions. For example, `AccessKeyID` is set to testid, `AccessKeySecret` is set to testsecret, and all request parameters are stored in a Java `Map<String, String>` object.
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
services by using ASAPI

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

services by using ASAPI
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

## 2 API reference

### 2.1 API overview

The following tables list API operations available for use in Cloud Native Distributed Database PolarDB- X. Database management

| API | Description |
|---|---|
| ChangeAccountPassword | Resets the password of an account that is used to log on to a specified PolarDB-X 1.0 instance. |
| CheckDrdsDbName | Checks whether the name of a PolarDB-X 1.0 database is valid. |
| DescribeRdsPerformanceSummary | Queries the performance metrics of one or more ApsaraDB RDS for MySQL instances that are used by a PolarDB-X instance. These metrics include CPU utilization, input/output operations per second (IOPS), and active sessions. |
| DescribeRecycleBinStatus | Queries the status of the table recycle bin of a PolarDB-X database. |
| DescribeRecycleBinTables | Queries the tables that can be recycled for a PolarDB-X database. |
| DescribeRdsSuperAccountInstances | Queries the privileged accounts of one or more ApsaraDB RDS for MySQL instances that are used by a PolarDB-X instance. |
| DescribeDrdsSlowSqls | Queries the slow SQL statements that are executed on a PolarDB-X 1.0 database. |
| DescribeDrdsDbInstance | Queries the details about an ApsaraDB RDS for MySQL instance that is used by a PolarDB-X 1.0 database. |
| DescribeDrdsDbInstances | Queries the ApsaraDB RDS for MySQL instances that are used by a PolarDB-X 1.0 database. |
| DescribeDrdsDbRdsNameList | Queries the IDs of the storage instances for a PolarDB-X 1.0 database. |
| DescribeDrdsDbRdsRelationInfo | Queries the structure information about the storage instances for a PolarDB-X 1.0 database. |
| DescribeDrdsDbTasks | Queries incomplete tasks for a PolarDB-X 1.0 database. |

| eveloper Guide·API reference | Cloud Native Distributed Database |
|---|---|

| API | Description |
|---|---|
| DescribeDrdsInstanceDbMonitor | Queries the performance monitoring data of a PolarDB-X 1.0 database. |
| SubmitCleanTask | Submits a cleanup task for the smooth scale-out of a PolarDB-X database. |
| SubmitSmoothExpandPreCheckTask | Submits a precheck task for the smooth scale-out of a PolarDB-X database. |
| ValidateShardTask | Checks whether a sharding task is valid. |
| SubmitSmoothExpandPreCheck | Submits a precheck task for the smooth scale-out of a PolarDB-X database. |
| StartRestore | Starts a backup-based restoration task. |
| RefreshDrdsAtomUrl | Refreshes the connection between a PolarDB-X 1.0 instance and an ApsaraDB RDS for MySQL instance whose network type is changed. This operation can ensure connectivity. |
| ModifyRdsReadWeight | Modifies the read/write weights of one or more ApsaraDB RDS for MySQL instances for a PolarDB-X database. |
| RemoveDrdsDbFailedRecord | Deletes the failure records of creating a database. |
| RemoveDrdsDb | Removes a database from a PolarDB-X 1.0 instance. |
| RemoveBackupsSet | Deletes a backup set. |
| RemoveRecycleBinTable | Clears the tables in the recycle bin of a PolarDB-X database. |
| DescribeBackMenu | Checks whether an instance supports backup and restoration. |
| DescribeDrdsSqlAuditStatus | Queries the SQL audit details for a PolarDB-X 1.0 instance. |
| DescribeTables | Queries the details about the tables in a PolarDB-X database. |
| DescribeBackupTimes | Queries the point in time to which a PolarDB-X instance can be restored. |
| DescribeGlobalBroadcastType | Checks whether the tables in a PolarDB-X database are broadcast tables. |
| DescribeHotDbList | Queries the available databases for a hot-spot scale-out operation. |

| loud Native Distributed Database | Developer Guide·API referenc |
|---|---|

| API | Description |
|---|---|
| DescribeExpandLogicTableInfoList | Queries the shard key of a PolarDB-X database. |
| DescribeTableListByType | Queries the tables of a PolarDB-X database based on types. |
| DisableSqlAudit | Disables the SQL audit feature for a PolarDB-X database. |
| DescribeShardTaskList | Queries the sharding tasks for a PolarDB-X database. |
| DescribeTable | Queries the table schema of a PolarDB-X database. |
| DescribeInstDbLogInfo | Queries the time range of historical SQL data that can be imported to a PolarDB-X database. |
| ResetDrdsToRdsConnections | Resets the number of connections from a PolarDB-X 1.0 instance to ApsaraDB RDS for MySQL instances. |
| DatalinkReplicationPrecheck | Performs a precheck for a sharding task on a PolarDB-X database. |
| DescribeRDSPerformance | Queries the performance data of a specified ApsaraDB RDS for MySQL instance that is used by a PolarDB-X instance. |
| CreateShardTask | Creates a sharding task for a PolarDB-X database. |
| DescribeShardTaskInfo | Queries the details about a sharding task for a specified PolarDB-X database. |
| DescribeBackupDbs | Queries the databases that can be restored for a PolarDB-X instance. |
| DeleteShardTasks | Deletes sharding tasks from a PolarDB-X database. |
| ModifyDrdsIpWhiteList | Modifies the IP address whitelist of a PolarDB-X database. |
| DescribeSqlFlashbakTask | Queries the flashback tasks for a PolarDB-X database. |
| CheckExpandStatus | Checks whether scale-out operations such as smooth scale-outs can be performed on a PolarDB- X 1.0 database. |
| CheckSqlAuditEnableStatus | Checks whether the SQL audit feature is enabled for a PolarDB-X 1.0 logical database. |
| SetupBroadcastTables | Configures broadcast tables for a PolarDB-X database. |

| eveloper Guide·API reference | Cloud Native Distributed Database |
|---|---|

| API | Description |
|---|---|
| SetupRecycleBinStatus | Enables the table recycle bin for a PolarDB-X database. |
| SetupTable | Enables the full-table scan feature for a PolarDB-X database. |
| ModifyAccountPrivilege | Modifies the permissions of a specified account for a PolarDB-X instance. |
| DescribeDrdsShardingDbs | Queries the details about a horizontally split PolarDB-X 1.0 database. |
| CreateDrdsDB | Creates a PolarDB-X 1.0 database. |
| DescribeDbInstances | Queries the storage instances of a PolarDB-X instance. |
| DescribeDrdsDB | Queries the details about the databases for a PolarDB-X instance. |
| DescribeDbInstanceDbs | Queries the databases on a storage instance that is used by a specified PolarDB-X instance. |
| SubmitSmoothExpandTask | Submits a smooth scale-out task for a PolarDB-X database. |
| SubmitSwitchTask | Submits a switchover task for the smooth scale-out of a PolarDB-X database. |

Instance management

| API | Description |
|---|---|
| DescribeDrdsDBs | Queries the details about the databases that are created in a PolarDB-X 1.0 instance. |
| DescribeDrdsInstance | Queries the details about a PolarDB-X 1.0 instance. |
| DescribeDrdsInstanceLevelTasks | Queries incomplete tasks for a PolarDB-X 1.0 instance. |
| DescribeDrdsInstanceMonitor | Queries the monitoring data of a PolarDB-X 1.0 instance. |
| DescribeDrdsInstances | Queries the PolarDB-X 1.0 instances that meet specific criteria in a region. |
| DescribeDrdsInstanceVersion | Queries the version information for a PolarDB-X 1.0 instance. |
| DescribeDrdsParams | Queries the parameters of a PolarDB-X 1.0 instance or database. |

| loud Native Distributed Database olarDB-X | Developer Guide·API referenc |
|---|---|
| API | Description |
| RollbackInstanceVersion | Rolls back the version of a PolarDB-X 1.0 instance. |
| UpgradeInstanceVersion | Upgrades the version of the PolarDB-X 1.0 instance. |
| SubmitRollbackTask | Submits a smooth scale-out rollback task for a PolarDB-X database. |
| SwitchGlobalBroadcastType | Switches the broadcast tables in a PolarDB-X database from the multi-write mode to the asynchronous link mode. |
| SubmitSqlFlashbackTask | Submits an SQL flashback task for a PolarDB-X instance. |
| RemoveDrdsInstance | Releases a PolarDB-X 1.0 instance. |
| DescribeDrdsTasks | Queries the change tasks for an instance. |
| RestartDrdsInstance | Restarts an instance. |
| DescribePreCheckResult | Queries the precheck results of a PolarDB-X instance. |
| DescribeStorageInstanceSubDbInfo | Queries the details about a storage instance that is used by a specified PolarDB-X database. |
| RemoveInstanceAccount | Deletes a management account of a PolarDB-X instance. |
| DescribeInstanceMenuSwitch | Queries the switch configuration of a PolarDB-X instance. |
| DescribeInstanceAccounts | Queries the account information about a PolarDB-X instance. |
| DescribeInstDbSlsInfo | Queries the names of the Log Service project and the Logstore used by the SQL audit feature. |
| SetBackupPolicy | Configures the backup policy for a PolarDB-X instance. |
| EnableSqlAudit | Enables the SQL audit feature for a PolarDB-X database. |
| EnableSqlFlashbackMatchSwitch | Enables the SQL flashback matching feature for a PolarDB-X database. After this feature is enabled, the query information is added to the binary logs of the ApsaraDB RDS for MySQL instances that are used by the PolarDB-X 1.0 database. This helps restore data in a precise manner. |
| SetupDrdsParams | Configures parameters for a PolarDB-X 1.0 instance or database. |

| D | eveloper Guide·API reference | Cloud Native Distributed Database PolarDB- | X |
|---|---|---|---|

| API | Description |
|---|---|
| FlashbackRecycleBinTable | Restores a logical table in the recycle bin of a PolarDB-X database. |
| ModifyAccountDescription | Modifies the description of an account for a PolarDB-X instance. |
| ModifyDrdsInstanceDescription | Modifies the description of a PolarDB-X instance. |
| CreateInstanceAccount | Creates an account for a PolarDB-X 1.0 instance. |

### 2.2 Database management

#### 2.2.1 ChangeAccountPassword

Resets the password of a PolarDB-X 1.0 database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AccountName | String | Yes | test | The name of the account. |
| Action | String | Yes | ChangeAccountPasswor d | The operation that you want to perform. Set the value to ChangeAccountPasswor d. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| Password | String | Yes | Test123 | The new password. |
| AccessKeyId | String | No | sdfgssdsf | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DSSDF-SEWE-23ERW | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=ChangeAccountPassword &AccountName=test &DrdsInstanceId=drdsxxxxxxxxxx &Password=Test123 <ChangeAccountPasswordResponse>
      <RequestId>DSSDF-SEWE-23ERW</RequestId>
</ChangeAccountPasswordResponse>
```

JSON format `{`

```json
    "RequestId":"DSSDF-SEWE-23ERW",
    "Success":true
```

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | ActionUnauthorized | The specified action is not available for you | The error message returned because you are not authorized to perform this action. Perform RAM authorization first. |

#### 2.2.2 CheckDrdsDbName

Checks whether the name of a PolarDB-X 1.0 database is valid.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CheckDrdsDbNam e | The operation that you want to perform. Set the value to CheckDrdsDbNam e. |
| DbName | String | Yes | testdb | The name of the PolarDB-X 1.0 database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DSSDF-SEWE-23ERW | The ID of the request. |
| Result | Boolean | true | Indicates whether the name of the PolarDB-X database is valid. Valid values: true: valid false: invalid |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=CheckDrdsDbName &DbName=testdb &DrdsInstanceId=drdsxxxxxxxxxxx <CheckDrdsDbNameResponse>
      <Result>true</Result>
      <RequestId>CF38538C-68BD-4278-B58F-EDE96FA8A5CE</RequestId>
</CheckDrdsDbNameResponse>
```

JSON format `{`

```json
    "Result":true,
    "RequestId":"CF38538C-68BD-4278-B58F-EDE96FA8A5CE",
    "Success":true
```

#### 2.2.3 CheckExpandStatus

Verifies whether scale-out operations such as smooth scale-out can be performed on a PolarDB-X 1.0 database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CheckExpandStatu s | The operation that you want to perform. Set the value to CheckExpandStatu s. |
| DbName | String | Yes | testdb | The name of the PolarDB-X database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | - | - | The verification result. |
| IsActive | Boolean | true | Indicates whether scale- out is supported. The value true indicates that scale-out is supported. The value false indicates that scale-out is not supported. |
| Msg | String | success | The additional information. |

| Developer Guide·API refere | nce | Cloud N | ative Distributed Database PolarDB- |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | drds sample request i _ _ _ d | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=CheckExpandStatus &DbName=testdb &DrdsInstanceId=drdsxxxxxxxxxxx <CheckExpandStatus>
      <Data>
            <IsActive>true</IsActive>
            <Msg></Msg>
      </Data>
      <RequestId>7CDBA7D5-8D62-4D24-9C65-510D621278DB</RequestId>
</CheckExpandStatus>
```

JSON format `{`

```json
    "Data":{
        "IsActive":true,
        "Msg":""
```

`},`

```json
    "RequestId":"7CDBA7D5-8D62-4D24-9C65-510D621278DB",
    "Success":true
```

#### 2.2.4 CheckSqlAuditEnableStatus

Verifies whether SQL audit is enabled for a PolarDB-X 1.0 logical database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CheckSqlAuditEna bleStatus | The operation that you want to perform. Set the value to CheckSqlAuditEna bleStatus. |
| DbName | String | Yes | drds db _ | The name of the PolarDB-X database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | drds sample request i _ _ _ d | The ID of the request. |
| Status | String | enabled | Indicates whether SQL audit was enabled for the logical database. Valid values: enabled and disabled. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=CheckSqlAuditEnableStatus &DbName=drds_db &DrdsInstanceId=drdsxxxxxxxxxxx <CheckSqlAuditEnableStatus>
      <Status>"disabled"</Status>
      <RequestId>FF13E47D-4E38-4A5A-BA68-32A554E6FE10</RequestId>
</CheckSqlAuditEnableStatus>
```

JSON format `{`

```json
    "Status":"\"disabled\"",
    "RequestId":"FF13E47D-4E38-4A5A-BA68-32A554E6FE10",
    "Success":true
```

#### 2.2.5 CreateDrdsDB

Creates a PolarDB-X 1.0 database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateDrdsDB | The operation that you want to perform. Set the value to CreateDrdsDB. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| DbInstType | String | No | RDS | The type of the storage instance. Only ApsaraDB RDS for MySQL instances are supported. |
| DbInstanceIsCreati ng | Boolean | No | false | Indicates whether ApsaraDB RDS for MySQL instances involved in database creation are being created. |
| DbName | String | No | drds db _ | The name of the PolarDB-X database. |
| Encode | String | No | drds sample enc _ _ ode | The database encoding. |
| Password | String | No | drds sample pass _ _ word | The logon password of the PolarDB-X database. |

| C P | loud Native Distribute olarDB-X | d Database |   | Develop | er Guide·API referenc | e |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RdsInstance.N | RepeatList | No | ["rds id1", _ "rds id2"] _ | This parameter is required only for horizontal partitioning. It is a JSON array string. |
| RdsSuperAccount. N.AccountName | String | No | rdsuser | The name of the ApsaraDB RDS for MySQL privileged account. |
| RdsSuperAccount. N.DbInstanceId | String | No | rds id _ | The ID of the ApsaraDB RDS for MySQL instance. |
| RdsSuperAccount. N.Password | String | No | rds password _ | The password of the ApsaraDB RDS for MySQL privileged account. |
| Type | String | No | HORIZONTAL | The partition mode of the database. Set the value to HORIZONTAL. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | drds sample request i _ _ _ d | The ID of the request. |
| Success | Boolean | true | Indicates whether the PolarDB-X database was created. |

```xml
http(s)://[Endpoint]/? Action=CreateDrdsDB &DrdsInstanceId=drdsxxxxxxxxxxx &DbName=drds_db &Encode=utf8mb4 &Password=drds_sample_password &RdsInstance=["rds_id1", "rds_id2"] &Type=HORIZONTAL &DbInstType=RDS &DbInstanceIsCreating=false <CreateDrdsDB>
      <RequestId>FF13E47D-4E38-4A5A-BA68-32A554E610EF</RequestId>
</CreateDrdsDB>
```

JSON format `{`

```json
    "RequestId":"FF13E47D-4E38-4A5A-BA68-32A554E610EF",
    "Success":true
```

#### 2.2.6 CreateShardTask

Creates a partitioning task for a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateShardTask | The operation that you want to perform. Set the value to CreateShardTask. |
| DbName | String | Yes | test db _ | The name of the PolarDB-X database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |

| loud Native Distribute olarDB-X | d Database |   | Develop | er Guide·API referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SourceTableName | String | Yes | student tb1 _ | The name of the source table. |
| TargetTableName | String | Yes | student tb2 _ | The name of the destination table. |
| TaskType | String | Yes | SINGLE TO SHARD _ _ | The type of the task. Valid values: SHARD TO SINGLE, _ _ SINGLE TO SHARD, _ _ and SHARD TO SHARD. _ _ |
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Boolean | true | Indicates whether the partitioning task was created. |
| RequestId | String | F8997D95-94AD-416A- AE70-E24D087045ED | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```
http(s)://[Endpoint]/? Action=CreateShardTask &DbName=test_db &DrdsInstanceId=drdsxxxxxxxxxxxx &SourceTableName=student_tb1 &TargetTableName=student_tb2 &TaskType=SINGLE_TO_SHARD
```

```xml
<CreateShardTaskResponse>
      <Data>true</Data>
      <RequestId>F8997D95-94AD-416A-AE70-E24D087045ED</RequestId>
</CreateShardTaskResponse>
```

JSON format `{`

```json
    "Data":true,
    "RequestId":"F8997D95-94AD-416A-AE70-E24D087045ED",
    "Success":true
```

#### 2.2.7 DatalinkReplicationPrecheck

Prechecks a partitioning task of a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DatalinkReplicatio nPrecheck | The operation that you want to perform. Set the value to DatalinkReplicatio nPrecheck. |
| DbName | String | Yes | test db _ | The name of the PolarDB-X database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| DstTableName | String | Yes | student 1 _ | The name of the destination table. |
| SrcTableName | String | Yes | student 2 _ | The name of the source table. |
| AccessKeyId | String | No | XXXXXX | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Long | 20190886 | The ID of the precheck task. |
| RequestId | String | F8997D95-94AD-416A- AE70-E24D087045ED | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```
http(s)://[Endpoint]/? Action=DatalinkReplicationPrecheck &DbName=test_db &DrdsInstanceId=drdsxxxxxxxx &DstTableName=student_1 &SrcTableName=student_2
```

JSON format

```xml
<DatalinkReplicationPrecheckResponse>
      <Data>20190886</Data>
      <RequestId>F8997D95-94AD-416A-AE70-E24D087045ED</RequestId>
</DatalinkReplicationPrecheckResponse>
```

JSON format `{`

```json
    "Data":20190886,
    "RequestId":"F8997D95-94AD-416A-AE70-E24D087045ED",
    "Success":true
```

#### 2.2.8 DeleteShardTasks

Deletes partitioning tasks from a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteShardTasks | The operation that you want to perform. Set the value to DeleteShardTasks. |
| DbName | String | Yes | test db _ | The name of the PolarDB-X database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |
| TableName.N.Sour ceTableName | String | No | student 1 _ | The name of the source table. |
| TableName.N.Tar getTableName | String | No | student 2 _ | The name of the destination table. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Boolean | true | Indicates whether partitioning tasks were deleted. |
| RequestId | String | F8997D95-94AD-416A- AE70-E24D087045ED | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```
http(s)://[Endpoint]/? Action=DeleteShardTasks &DbName=test_db &DrdsInstanceId=drdsxxxxxxxxxx
```

```xml
<DeleteShardTasksResponse>
      <Data>true</Data>
      <RequestId>F8997D95-94AD-416A-AE70-E24D087045ED</RequestId>
</DeleteShardTasksResponse>
```

JSON format `{`

```json
    "Data":true,
    "RequestId":"F8997D95-94AD-416A-AE70-E24D087045ED",
    "Success":true
```

#### 2.2.9 DescribeBackMenu

Queries whether a PolarDB-X instance supports backup and recovery.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackMenu | The operation that you want to perform. Set the value to DescribeBackMenu . |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | xxxxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| List | - | - | The list of supported items. |
| list | - | - | The details about a supported item. |

|   |   | Cloud N | ative Distributed Database |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| MenuName | String | phy | The mode of the backup. Valid values: logic: logical backup phy: physical backup |
| Support | Boolean | true | Indicates whether the PolarDB-X instance supports backup and recovery. |
| RequestId | String | 60C21BE4-EDFE-454C- 95ED-3A5C7493D74A | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=DescribeBackMenu &DrdsInstanceId=drdsxxxxxxxxxxxx <DescribeBackMenuResponse>
      <List>
            <MenuName>phy</MenuName>
            <Support>true</Support>
      </List>
      <List>
            <MenuName>logic</MenuName>
            <Support>true</Support>
      </List>
      <RequestId>60C21BE4-EDFE-454C-95ED-3A5C7493D74A</RequestId>
</DescribeBackMenuResponse>
```

JSON format `{`

```json
    "RequestId":"60C21BE4-EDFE-454C-95ED-3A5C7493D74A",
    "Success":true,
    "List":[
```

`{`

```json
            "MenuName":"phy",
            "Support":true
```

`},` `{`

```json
            "MenuName":"logic",
            "Support":true
```

`]`

#### 2.2.10 DescribeBackupDbs

Queries the databases that can be restored for a PolarDB-X instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackupDb s | The operation that you want to perform. Set the value to DescribeBackupDb s. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | xxxxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |
| BackupId | String | No | 201908367 | Query by backup set. |
| PreferredRestoreTi me | String | No | 1568632541236 | Query by restoration time. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DbNames | - | ["db1","db2"] | The list of returned databases. |
| dbName | - | - | The details about a database. |
| RequestId | String | 9EF10719-C34F-4E64- 8260-D29C1A78B5DD | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=DescribeBackupDbs &DrdsInstanceId=drdsxxxxxxxxx <DescribeBackupDbsResponse>
      <DbNames></DbNames>
      <RequestId>9EF10719-C34F-4E64-8260-D29C1A78B5DD</RequestId>
</DescribeBackupDbsResponse>
```

JSON format `{`

```json
    "RequestId":"9EF10719-C34F-4E64-8260-D29C1A78B5DD",
    "DbNames":{
        "dbName":[]
```

`},`

```json
    "Success":true
```

#### 2.2.11 DescribeBackupTimes

Queries the point in time to which a PolarDB-X instance can be restored.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackupTi mes | The operation that you want to perform. Set the value to DescribeBackupTi mes. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | xxxxxxxxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4780A19F-5ECB-4C56- AD20-966A3FF99772 | The ID of the request. |
| RestoreTime | - | - | The point in time to which the PolarDB-X instance can be restored. |
| EndTime | String | 1568636922671 | The timestamp that specifies the end of the time range to query. |
| StartTime | String | 1568632853000 | The timestamp that specifies the beginning of the time range to query. |
| Success | Boolean | true | Indicates whether the request was successful. |

```
http(s)://[Endpoint]/? Action=DescribeBackupTimes &DrdsInstanceId=drdsxxxxxxxxxxx
```

```xml
<DescribeBackupTimesResponse>
      <RequestId>4780A19F-5ECB-4C56-AD20-966A3FF99772</RequestId>
      <RestoreTime>
            <EndTime>1568636922671</EndTime>
            <StartTime>1568632853000</StartTime>
      </RestoreTime>
</DescribeBackupTimesResponse>
```

JSON format `{`

```json
    "RestoreTime":{
        "EndTime":"1568636922671",
        "StartTime":"1568632853000"
```

`},`

```json
    "RequestId":"4780A19F-5ECB-4C56-AD20-966A3FF99772",
    "Success":true
```

#### 2.2.12 DescribeBroadcastTables

Queries the broadcast tables in a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBroadcast Tables | The operation that you want to perform. Set the value to DescribeBroadcast Tables. |
| DbName | String | Yes | test db _ | The name of the PolarDB-X database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| Query | String | Yes | tb1 | The query content. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| IsShard | Boolean | true | Indicates whether the table was partitioned. |
| List | - | - | The list of broadcast tables. |
| Broadcast | Boolean | true | Indicates whether the table is a broadcast table. |
| BroadcastType | String | 1 | The type of the broadcast table. Valid values: 1: multi-write mode 2: synchronous link mode |
| DbInstType | Integer | 0 | The type of the storage instance. The value 0 indicates RDS. |
| IsShard | Boolean | false | Indicates whether the table was partitioned. |
| Status | Integer | 1 | The status of the broadcast table. Valid values: 1: activated 2: activating 3: activation exception |
| Table | String | nation | The name of the table. |

| Developer Guide·API refere | nce | Cloud N | ative Distributed Database PolarDB- |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 40 | The number of entries returned per page. |
| RequestId | String | 86E420ED-43F2-4788- A58C-9218491FFB09 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |
| Total | Integer | 2 | The total number of entries. |

```
http(s)://[Endpoint]/? Action=DescribeBroadcastTables &DbName=test_db &DrdsInstanceId=drdsxxxxxxxxxx &Query=tb1
```

```xml
<DescribeBroadcastTablesResponse>
      <PageSize>40</PageSize>
      <RequestId>86E420ED-43F2-4788-A58C-9218491FFB09</RequestId>
      <PageNumber>1</PageNumber>
      <Total>2</Total>
      <List>
            <Status>1</Status>
            <DbInstType>0</DbInstType>
            <IsShard>false</IsShard>
            <Table>nation</Table>
            <Broadcast>true</Broadcast>
            <BroadcastType>1</BroadcastType>
      </List>
      <List>
            <Status>1</Status>
            <DbInstType>0</DbInstType>
            <IsShard>false</IsShard>
            <Table>region</Table>
            <Broadcast>true</Broadcast>
            <BroadcastType>1</BroadcastType>
      </List>
</DescribeBroadcastTablesResponse>
```

JSON format `{`

```json
    "PageNumber":1,
    "PageSize":40,
    "RequestId":"86E420ED-43F2-4788-A58C-9218491FFB09",
    "Success":true,
    "List":[
```

`{`

```json
            "Status":1,
            "IsShard":false,
            "BroadcastType":1,
            "Broadcast":true,
            "Table":"nation",
            "DbInstType":0
```

`},` `{`

```json
            "Status":1,
            "IsShard":false,
            "BroadcastType":1,
            "Broadcast":true,
            "Table":"region",
            "DbInstType":0
```

`],`

```json
    "Total":2
```

#### 2.2.13 DescribeDbInstanceDbs

Queries the databases on a storage instance of a PolarDB-X instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDbInstanc eDbs | The operation that you want to perform. Set the value to DescribeDbInstanc eDbs. |
| DbInstanceId | String | Yes | pc- bpxxxxxxxxxxxxxx | The ID of the storage instance. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | xxxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. For more information, see Common parameters. |
| AccountName | String | No | supper account _ | The username of the privileged account. Leave this parameter blank if no privileged account exists. |
| DbInstType | String | No | RDS | The type of the storage instance. Valid values: POLARDB and RDS. |
| Password | String | No | Pass 123456 _ | The password of the privileged account. Leave this parameter blank if no privileged account exists. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Databases | - | - | The list of returned databases. |
| Database | - | - | The details about a database. |
| DbName | String | db newsudbv _ | The name of the database. |
| Description | String | Created by PolarDB-X 1.0, do NOT change password | The description of the database. |
| Status | Integer | 1 | The status of the database. 0: creating 1: available 3: deleting |
| RequestId | String | E9F3D991-08DE-4B74- BE0E-06B80958F5DC | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |
| Total | String | 1 | The total number of databases. |

```
http(s)://[Endpoint]/? Action=DescribeDbInstanceDbs &DbInstanceId=pc-bpxxxxxxxxxxxxxx &DrdsInstanceId=drdsxxxxxxxxxxxx
```

```xml
<DescribeDbInstanceDbsResponse>
      <Databases>
            <Database>
                  <Status>1</Status>
                  <Description>Created by PolarDB-X 1.0, do NOT change password</Descriptio
```

`n>`

```xml
                  <DbName>db_newsudbv</DbName>
            </Database>
      </Databases>
      <total>1</total>
      <RequestId>E9F3D991-08DE-4B74-BE0E-06B80958F5DC</RequestId>
</DescribeDbInstanceDbsResponse>
```

JSON format `{`

```json
    "total":1,
    "Databases":{
        "Database":[
```

`{`

```json
                "Status":1,
                "Description":"Created by PolarDB-X 1.0, do NOT change password",
                "DbName":"db_newsudbv"
```

`]` `},`

```json
    "RequestId":"E9F3D991-08DE-4B74-BE0E-06B80958F5DC",
    "Success":true
```

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | ActionUnauthorized | The specified action is not available for you | The error message returned because you are not authorized to perform this action. Perform RAM authorization first. |

#### 2.2.14 DescribeDbInstances

Queries the storage instances, namely, ApsaraDB RDS for MySQL instances of a PolarDB-X instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDbInstanc es | The operation that you want to perform. Set the value to DescribeDbInstanc es. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | Yes | testxxxxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |
| DbInstType | String | No | RDS | The type of the storage instance. Set the value to RDS. |
| PageNumber | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| Search | String | No | pc- bp1xxxxxxxxxxxx | Query by storage instance ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | - | - | The list of returned storage instances. |
| DBInstance | - | - | The details about a storage instance. |
| DBInstanceDescription | String | pc-bp1xxxxxxxxxxxxxx | The description of the storage instance. |
| DBInstanceId | String | pc-bp1xxxxxxxxxxxxxx | The ID of the storage instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceStatus | Integer | 1 | The status of the storage instance. Valid values: 0: creating 1: running 3: deleting 5: restarting 6: changing specifications 7: recovering 8: switching between the classic network and VPC network |
| DBInstanceType | String | RDS | The type of the storage instance. Example: RDS. |
| Engine | String | mysql | The engine that the storage instance runs. |
| EngineVersion | String | 5.6 | The version of the engine that the storage instance runs. |
| InstanceNetworkType | String | CLASSIC | The network type of the storage instance. Valid values: CLASSIC: classic network VPC: Virtual Private Cloud (VPC) network Not e Apsara Stack does not support VPC networks. |
| ReadOnlyDBInstanceId | - | [] | The list of read-only storage instances. |
| ReadOnlyDBInstanceId | - | - | The details about a read-only storage instance. |
| RegionId | String | cn-hangzhou | The ID of the region where the storage instance is located. |

| loud Native Distributed Da | tabase | De | veloper Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ZoneId | String | cn-hangzhou-a | The ID of the zone where the storage instance is located. |
| RequestId | String | 05670C01-093E-4DF4- 99FA-0C63FF60250D | The ID of the request. |

```xml
http(s)://[Endpoint]/? Action=DescribeDbInstances &DrdsInstanceId=drdsxxxxxxxxxxx <DescribeDbInstancesResponse>
      <RequestId>05670C01-093E-4DF4-99FA-0C63FF60250D</RequestId>
      <Items>
            <DBInstance>
                  <EngineVersion>5.6</EngineVersion>
                  <DBInstanceStatus>1</DBInstanceStatus>
                  <DBInstanceId>pc-bp1xxxxxxxxxxxxxx</DBInstanceId>
                  <ReadOnlyDBInstanceId></ReadOnlyDBInstanceId>
                  <DBInstanceType>Primary</DBInstanceType>
                  <RegionId>cn-hangzhou</RegionId>
                  <DBInstanceDescription>pc-bp1xxxxxxxxxxxxxx</DBInstanceDescription>
                  <Engine>POLARDB</Engine>
                  <InstanceNetworkType>VPC</InstanceNetworkType>
            </DBInstance>
      </Items>
</DescribeDbInstancesResponse>
```

JSON format `{`

```json
    "Items":{
        "DBInstance":[
```

`{`

```json
                "RegionId":"cn-hangzhou",
                "DBInstanceType":"Primary",
                "DBInstanceId":"pc-bp1xxxxxxxxxxxxxx",
                "InstanceNetworkType":"VPC",
                "DBInstanceDescription":"pc-bp1xxxxxxxxxxxxxx",
                "EngineVersion":"5.6",
                "DBInstanceStatus":1,
                "Engine":"POLARDB",
                "ReadOnlyDBInstanceId":{
                    "ReadOnlyDBInstanceId":[]
```

`]` `},`

```json
    "RequestId":"05670C01-093E-4DF4-99FA-0C63FF60250D"
```

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | ActionUnauthorized | The specified action is not available for you | The error message returned because you are not authorized to perform this action. Perform RAM authorization first. |

#### 2.2.15 DescribeDrdsDB

Queries the details about a database on a PolarDB-X instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDrdsDB | The operation that you want to perform. Set the value to DescribeDrdsDB. |
| DbName | String | Yes | db test _ | The name of the PolarDB-X database. |

| loud Native Distribute olarDB-X | d Database |   | Develop | er Guide·API referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxx | The ID of PolarDB- X instance. |
| AccessKeyId | String | No | xxxxxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | - | - | The details about the database. |
| CreateTime | String | 1568949855000 | The timestamp when the database was created. |
| DbInstType | String | RDS | The type of the storage instance. Example: RDS. |
| DbName | String | db 0 _ | The name of the database. |
| InstRole | String | MASTER | The type of the storage instance. Valid values: MASTER: primary instance. SLAVE: read-only instance. |
| Mode | String | HORIZONTAL | The partition mode of the database. Set the value to HORIZONTAL. |
| Schema | String | db 0 xxxxxxxxxxxxwpyh _ _ | The name of a physical database after partitioning. |
| Status | String | NORMAL | The status of the database. Valid values: TO BE INIT: creating _ _ NORMAL: running |
| RequestId | String | 05203D07-8447-48D0- BED5-2F00BFD40630 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=DescribeDrdsDB &DbName=db_test &DrdsInstanceId=drdsxxxxxxxxxxxx <DescribeDrdsDBResponse>
      <RequestId>45203D07-8447-48D0-BED5-2F00BFD40630</RequestId>
      <Data>
            <Status>NORMAL</Status>
            <DbInstType>RDS</DbInstType>
            <InstRole>MASTER</InstRole>
            <Schema>db_0_xxxxxxxxxxxxwpyh</Schema>
            <CreateTime>1568949855000</CreateTime>
            <Mode>HORIZONTAL</Mode>
            <DbName>db_0</DbName>
      </Data>
</DescribeDrdsDBResponse>
```

JSON format `{`

```json
    "Data":{
        "Status":"NORMAL",
        "DbName":"db_0",
        "CreateTime":1568949855000,
        "Schema":"db_0_xxxxxxxxxxxxwpyh",
        "DbInstType":"RDS",
        "Mode":"HORIZONTAL",
        "InstRole":"MASTER"
```

`},`

```json
    "RequestId":"45203D07-8447-48D0-BED5-2F00BFD40630",
    "Success":true
```

#### 2.2.16 DescribeDrdsDbInstance

Queries the details about an ApsaraDB RDS for MySQL instance of a PolarDB-X 1.0 database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDrdsDbIns tance | The operation that you want to perform. Set this parameter to DescribeDrdsDbIns tance. |
| DbInstanceId | String | Yes | rm-bpxxxxxxxxxxx | The ID of ApsaraDB RDS for MySQL instance of the PolarDB-X 1.0 instance. |
| DbName | String | Yes | drds test _ | The name of the PolarDB-X 1.0 database. |
| DrdsInstanceId | String | Yes | rm-drdsxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | ASU678xxxxxxxxxx xxxx | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DbInstance | - | - | The details about the ApsaraDB RDS for MySQL instance of the PolarDB-X 1.0 database. |
| ConnectUrl | String | rm- bp1uxxxxxxxxxxx.mysql. rds.aliyuncs.com | The connection URL. |
| DBInstanceId | String | rm-bp1xxxxxxxxxxxxx | The ID of the ApsaraDB RDS for MySQL instance. |
| DBInstanceStatus | String | 1 | The status of the ApsaraDB RDS for MySQL instance. |
| DbInstType | String | Primary | The type of the ApsaraDB RDS for MySQL instance. |
| Engine | String | MySQL | The engine that the ApsaraDB RDS for MySQL instance runs. |

| eveloper Guide·API refere | nce | Cloud N | ative Distributed Database PolarDB- |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| EngineVersion | String | 5.7 | The version of the engine that the ApsaraDB RDS for MySQL instance runs. |
| ExpireTime | String | 12341434315 | The timestamp when the ApsaraDB RDS for MySQL instance expires. |
| NetworkType | String | VPC | The network type of the ApsaraDB RDS for MySQL instance. |
| PayType | String | Postpaid | The billing method of the ApsaraDB RDS for MySQL instance. |
| Port | Integer | 3306 | The port of the ApsaraDB RDS for MySQL instance. |
| RdsInstType | String | RDS | The type of the ApsaraDB RDS for MySQL instance. |
| ReadOnlyInstances | - | - | The list of read-only ApsaraDB RDS for MySQL instances. |
| ReadOnlyInstance | - | - | The details about a read-only ApsaraDB RDS for MySQL instance. |
| ConnectUrl | String | rm- bp1xxxxxxxxxxxxx.mysql .rds.aliyuncs.com | The connection URL. |
| DBInstanceId | String | rm-bp1xxxxxxxxxxxxx | The ID of the read-only ApsaraDB RDS for MySQL instance. |
| DBInstanceStatus | String | 1 | The status of the read- only ApsaraDB RDS for MySQL instance. |
| DbInstType | String | RDS | The type of the read- only ApsaraDB RDS for MySQL instance. |
| Engine | String | MySQL | The engine that the read-only ApsaraDB RDS for MySQL instance runs. |

| C P | loud Native Distributed Da olarDB-X | tabase | De | veloper Guide·API referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| EngineVersion | String | 5.7 | The version of the engine that the read- only ApsaraDB RDS for MySQL instance runs. |
| ExpireTime | String | 1823487328173 | The timestamp when the read-only ApsaraDB RDS for MySQL instance expires. |
| NetworkType | String | VPC | The network type of the read-only ApsaraDB RDS for MySQL instance. |
| PayType | String | Postpaid | The billing method of the read-only ApsaraDB RDS for MySQL instance. |
| Port | Integer | 3306 | The port of the read- only ApsaraDB RDS for MySQL instance. |
| RdsInstType | String | RDS | The type of the read- only ApsaraDB RDS for MySQL instance. |
| ReadWeight | Integer | 30 | The read weight of the read-only ApsaraDB RDS for MySQL instance. |
| RemainDays | String | 0 | The remaining number of days before the read-only ApsaraDB RDS for MySQL instance expires. |
| VersionAction | Integer | 0 | An invalid parameter. |
| ReadWeight | Integer | 70 | The read weight of the read-only ApsaraDB RDS for MySQL instance. |
| RemainDays | String | 0 | The remaining number of days before the read-only ApsaraDB RDS for MySQL instance expires. |
| RequestId | String | 2F7F8080-9132-4279- 85D0-B7E5C4305162 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=DescribeDrdsDbInstance &DbInstanceId=rm-bp1xxxxxxxxxxxxx &DbName=drds_test &DrdsInstanceId=rm-drdsxxxxxxxx <DescribeDrdsDbInstance>
      <RequestId>2F7F8080-9132-4279-85D0-B7E5C4305162</RequestId>
      <DbInstance>
            <DbInstType>RDS</DbInstType>
            <ReadOnlyInstances></ReadOnlyInstances>
            <EngineVersion>5.7</EngineVersion>
            <DBInstanceStatus>1</DBInstanceStatus>
            <Port>3306</Port>
            <PayType>Postpaid</PayType>
            <ReadWeight>100</ReadWeight>
            <ConnectUrl>rm-bp1xxxxxxxxxxxxx.mysql.rds.aliyuncs.com</ConnectUrl>
            <DBInstanceId>rm-bp1xxxxxxxxxxxxx</DBInstanceId>
            <NetworkType>VPC</NetworkType>
            <RdsInstType>Primary</RdsInstType>
            <ExpireTime></ExpireTime>
            <RemainDays>0</RemainDays>
            <Engine>MySQL</Engine>
      </DbInstance>
</DescribeDrdsDbInstance>
```

JSON format `{`

```json
    "DbInstance":{
        "RemainDays":0,
        "ReadOnlyInstances":{
            "ReadOnlyInstance":[]
```

`},`

```json
        "DBInstanceId":"rm-bp1ub71ct9skc3y",
        "ReadWeight":100,
        "RdsInstType":"Primary",
        "DbInstType":"RDS",
        "ConnectUrl":"rm-bp1ub71ct9skc3y.mysql.rds.aliyuncs.com",
        "Engine":"MySQL",
        "NetworkType":"VPC",
        "Port":3306,
        "ExpireTime":"",
        "EngineVersion":"5.7",
        "DBInstanceStatus":1,
        "PayType":"Postpaid"
```

`},`

```json
    "RequestId":"2F7F8080-9132-4279-85D0-B7E5C4305162",
    "Success":true
```

#### 2.2.17 DescribeDrdsDbInstances

Queries ApsaraDB RDS for MySQL instances in a PolarDB-X 1.0 database. You can query primary ApsaraDB RDS for MySQL instances in a PolarDB-X 1.0 database. Each primary ApsaraDB RDS for MySQL instance has a ReadOnlyInstances attribute. This attribute specifies the readonly ApsaraDB RDS for MySQL instances that are used in the current database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DbName | String | Yes | dbname | The name of the PolarDB-X 1.0 database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | ASU6xxxxxxxxxxxx xxxx | The AccessKey ID provided by Alibaba Cloud for you to connect to services. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageNumber | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DbInstances | - | - | The instances used for storage in the PolarDB- X 1.0 database. |
| DbInstance | - | - | The instances used for storage in the PolarDB- X 1.0 database. |
| ConnectUrl | String | rm- m5xxxxxxxxx82.mysql.rd s.aliyuncs.com | The URL of the instance used for storage. The value is returned when you call API operations to connect to the instance used for storage. ApsaraDB RDS for MySQL instances can be used for storage. |
| DBInstanceId | String | rm-m5xxxxxxxxx82 | The ID of the instance used for storage. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceStatus | String | 1 | The running status of the instance: 0: The instance is being created. 1: The instance is running. 3: The instance is being deleted. 5: The instance is being restarted. 6: The instance is being upgraded or downgraded. 7: The instance is being backed up. 8: The network type is being changed. 9: The instance is being migrated. 11: Data is being migrated. 12: A disaster recovery instance is being generated. 13: Data is being imported. 14: Data is being imported from other ApsaraDB RDS for MySQL instances. 15: A switchover is being performed. 16: A temporary instance is being created. 17: A network is being created. 18: The instance is being cloned. 19: The link is being changed. 20: The read-only instance is being migrated. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DbInstType | String | RDS | The type of the instance used for storage. Only ApsaraDB RDS for MySQL instances are supported. |
| Engine | String | MySQL | The engine of the instance used for storage. For example, MySQL. |
| EngineVersion | String | 5.7 | The engine version of the instance used for storage. For example, MySQL 5.7, MySQL 5.6, and MySQL 5.5. |
| ExpireTime | String | 1237486127634 | The time when the instance used for storage expires. |
| NetworkType | String | VPC | The type of the network. Not e Apsara Stack does not support virtual private clouds (VPCs). |
| Port | Integer | 3306 | The port number. |
| RdsInstType | String | Primary | Indicates whether the ApsaraDB RDS for MySQL instance is primary or read-only. |
| ReadOnlyInstances | - | - | The read-only instances used for storage. |
| ReadOnlyInstance | - | - | The read-only instances used for storage. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ConnectUrl | String | rm- m5xxxxxxxxx82.mysql.rd s.aliyuncs.com | The URL of the instance used for storage. The value is returned when you call API operations to connect to the instance used for storage. ApsaraDB RDS for MySQL instances can be used for storage. |
| DBInstanceStatus | String | 1 | The status of the instance used for storage. |
| DbInstType | String | RDS | The type of the instance used for storage. |
| Engine | String | MySQL | The engine of the instance used for storage. |
| EngineVersion | String | 5.7 | The engine version of the instance used for storage. |
| ExpireTime | String | 123421352351234 | The timestamp when the instance used for storage expires. |
| InstanceName | String | rm-m5xxxxxxxxx82 | The invalid field. |
| NetworkType | String | VPC | The network type of the instance. |
| PayType | String | Postpaid | The billing method. |
| Port | Integer | 3306 | The port used to connect to the instance. |
| RdsInstType | String | RDS | The type of the instance. |
| ReadWeight | Integer | 70 | The read ratio of the instance. |
| RemainDays | Integer | 0 | The number of remaining days before the instance expires. |
| ReadWeight | Integer | 30 | The weight of the read requests in the PolarDB- X 1.0 database. |

| Developer Guide·API refere | nce | Cloud N | ative Distributed Database PolarDB- |
|---|---|---|---|
| Parameter | Type | Example | Description |
| RemainDays | Integer | 0 | The number of remaining days before the subscription instance expires. |
| PageNumber | String | 1 | The page number of the returned page. |
| PageSize | String | 10 | The number of entries returned on each page. |
| RequestId | String | 2F7F8080-9132-4279- 85D0-B7E5C4305162 | The ID of the request. |
| Success | Boolean | true | Indicates whether the operation is successful. |
| Total | String | 1 | The total number of the primary ApsaraDB RDS for MySQL instances. |

```
http(s)://[Endpoint]/? Action=DescribeDrdsDbInstances &DbName=dbname &DrdsInstanceId=drdsxxxxxxxxx
```

```xml
<DescribeDrdsDbInstances>
      <PageSize>10</PageSize>
      <RequestId>658B6F25-442A-4996-8AAE-F77DAFBC9BAA</RequestId>
      <PageNumber>1</PageNumber>
      <Total>1</Total>
      <DbInstances>
            <DbInstance>
                  <DbInstType>RDS</DbInstType>
                  <ReadOnlyInstances></ReadOnlyInstances>
                  <EngineVersion>5.7</EngineVersion>
                  <DBInstanceStatus>1</DBInstanceStatus>
                  <Port>3306</Port>
                  <PayType>Postpaid</PayType>
                  <ReadWeight>100</ReadWeight>
                  <ConnectUrl>rm-m5xxxxxxxxx82.mysql.rds.aliyuncs.com</ConnectUrl>
                  <DBInstanceId>rm-m5xxxxxxxxx82</DBInstanceId>
                  <NetworkType>VPC</NetworkType>
                  <RdsInstType>Primary</RdsInstType>
                  <ExpireTime></ExpireTime>
                  <RemainDays>0</RemainDays>
                  <Engine>MySQL</Engine>
            </DbInstance>
      </DbInstances>
</DescribeDrdsDbInstances>
```

JSON format `{`

```json
    "PageNumber":1,
    "PageSize":10,
    "RequestId":"658B6F25-442A-4996-8AAE-F77DAFBC9BAA",
    "DbInstances":{
        "DbInstance":[
```

`{`

```json
                "RemainDays":0,
                "ReadOnlyInstances":{
                    "ReadOnlyInstance":[]
```

`},`

```json
                "DBInstanceId":"rm-m5xxxxxxxxx82",
                "ReadWeight":100,
                "RdsInstType":"Primary",
                "DbInstType":"RDS",
                "ConnectUrl":"rm-m5xxxxxxxxx82.mysql.rds.aliyuncs.com",
                "Engine":"MySQL",
                "NetworkType":"VPC",
                "Port":3306,
                "ExpireTime":"",
                "EngineVersion":"5.7",
                "DBInstanceStatus":1,
                "PayType":"Postpaid"
```

`]` `},`

```json
    "Success":true,
    "Total":1
```

#### 2.2.18 DescribeDrdsDbRdsNameList

Queries the IDs of the storage instances of a PolarDB-X 1.0 database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDrdsDbRd sNameList | The operation that you want to perform. Set the value to DescribeDrdsDbRd sNameList. |
| DbName | String | Yes | drds test _ | The name of the PolarDB-X 1.0 database. |

| C P | loud Native Distribute olarDB-X | d Database |   | Develop | er Guide·API referenc | e |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DrdsInstanceId | String | Yes | drdsxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | ASU67xxxxxxxxxxx xxxx | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| InstanceNameList | - | rm-m5xxxxxxxxx82 | The IDs of storage instances. |
| InstanceName | - | - | The ID of a storage instance. |
| RequestId | String | 37537B38-A663-45CB- A81F-E3B202BB2415 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=DescribeDrdsDbRdsNameList &DbName=drds_test &DrdsInstanceId=drdsxxxxxxxxx <DescribeDrdsDbRdsNameList>
      <RequestId>37537B38-A663-45CB-A81F-E3B202BB2415</RequestId>
      <InstanceNameList>
            <InstanceName>rm-m5xxxxxxxxx82</InstanceName>
      </InstanceNameList>
</DescribeDrdsDbRdsNameList>
```

JSON format `{`

```json
    "InstanceNameList":{
        "InstanceName":[
            "rm-m5xxxxxxxxx82"
```

`]` `},`

```json
    "RequestId":"37537B38-A663-45CB-A81F-E3B202BB2415",
    "Success":true
```

#### 2.2.19 DescribeDrdsDbRdsRelationInfo

Queries the structure information of storage instances for a PolarDB-X 1.0 database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDrdsDbRd sRelationInfo | The operation that you want to perform. Set the value to DescribeDrdsDbRd sRelationInfo. |
| DbName | String | Yes | drds test _ | The name of the PolarDB-X 1.0 database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | ASU67xxxxxxxxxxx x | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | - | - | The structure information about the storage instances of the PolarDB-X 1.0 database. Each item corresponds to a primary storage instance. |
| Data | - | - | The details about a primary storage instance of the PolarDB- X 1.0 database. |
| RdsInstanceId | String | rm-m5xxxxxxxxx82 | The ID of the primary storage instance. |
| ReadOnlyInstanceInfo | - | rm-m5xxxxxxxxx82 | The information about read-only storage instances of the primary storage instance. |
| ReadOnlyInstanceIds | - | - | The IDs of the read-only storage instances. |
| UsedInstanceId | String | rm-m5xxxxxxxxx82 | The ID of the used storage instance. For the primary PolarDB-X 1.0 instance, the used storage instance is the primary storage instance. For the read- only PolarDB-X 1.0 instance, the used storage instance is the optional storage instance. |
| UsedInstanceType | String | RDS | The type of the used storage instance. |
| RequestId | String | 2F7F8080-9132-4279- 85D0-B7E5C4305162 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=DescribeDrdsDbRdsRelationInfo &DbName=drds_test &DrdsInstanceId=drdsxxxxxxxxx <DescribeDrdsDbRdsRelationInfo>
      <RequestId>E827BEE8-A8BE-4E86-992A-E6400B263CB1</RequestId>
      <Data>
            <Data>
                  <ReadOnlyInstanceInfo>
                        <ReadOnlyInstanceIds>rm-m5xxxxxxxxx82</ReadOnlyInstanceIds>
                  </ReadOnlyInstanceInfo>
                  <UsedInstanceId>rm-m5xxxxxxxxx82</UsedInstanceId>
                  <UsedInstanceType>RDS</UsedInstanceType>
                  <RdsInstanceId>rm-m5xxxxxxxxx82</RdsInstanceId>
            </Data>
      </Data>
</DescribeDrdsDbRdsRelationInfo>
```

JSON format `{`

```json
    "Data":{
        "Data":[
```

`{`

```json
                "UsedInstanceType":"RDS",
                "RdsInstanceId":"rm-m5xxxxxxxxx82",
                "UsedInstanceId":"rm-m5xxxxxxxxx82",
                "ReadOnlyInstanceInfo":{
                    "ReadOnlyInstanceIds":[
                        "rm-m5xxxxxxxxx82"
```

`]` `]` `},`

```json
    "RequestId":"E827BEE8-A8BE-4E86-992A-E6400B263CB1",
    "Success":true
```

#### 2.2.20 DescribeDrdsDbTasks

Queries incomplete tasks for a PolarDB-X 1.0 database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDrdsDbTa sks | The operation that you want to perform. Set the value to DescribeDrdsDbTa sks. |
| DbName | String | Yes | drds test _ | The name of the PolarDB-X 1.0 database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | ASU678Uxxxxxxxxx xxxx | The AccessKey ID provided to you by Alibaba Cloud. |
| TaskType | String | No | create db _ | The type of the task. If this parameter is not specified, all types of tasks are queried. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 2F7F8080-9132-4279- 85D0-B7E5C4305162 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |
| Tasks | - | - | The list of returned tasks. |
| Task | - | - | The details about a task. |
| AllowCancel | Boolean | false | Indicates whether the task can be canceled. |
| ExpandType | String | hot expand _ | The type of the scale- out task. Valid values: smooth expand and _ hot expand. _ |

| eveloper Guide·API refere | nce | Cloud N | ative Distributed Database PolarDB- |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| GmtCreate | Long | 123978138412341 | The timestamp when the task was created. |
| Label | String | create db _ | The type of the task. |
| ParentJobId | String | 123214 | The ID of the parent task. |
| Progress | Integer | 99 | The task progress. Valid values: 0 to 100. |
| ShowProgress | Boolean | true | Indicates whether the task progress was displayed. |
| TargetId | Long | 12312 | The ID of the incomplete task. |
| TaskDetail | String | {} | The details about the task. Example: the details about a smooth scale-out task. |
| TaskName | String | Database creation task | The name of the incomplete task. |
| TaskPhase | String | 1 | The current phase of the incomplete task. |
| TaskStatus | Integer | 1 | The status of the incomplete task. Valid values: 0: running 1: success 2: failed 3: canceled |
| TaskType | Integer | 8 | The type of the incomplete task. |

```
http(s)://[Endpoint]/? Action=DescribeDrdsDbTasks &DbName=drds_test &DrdsInstanceId=drdsxxxxxxxxxx
```

```xml
<DescribeDrdsDbTasks>
      <Tasks>
            <Task>
                  <AllowCancel>false</AllowCancel>
                  <ExpandType></ExpandType>
                  <GmtCreate>1568696422000</GmtCreate>
                  <Label>create_db</Label>
                  <ParentJobId>123</ParentJobId>
                  <Progress>90</Progress>
                  <ShowProgress>true</ShowProgress>
                  <TargetId>154</TargetId>
                  <TaskDetail></TaskDetail>
                  <TaskName>Database creation task</TaskName>
                  <TaskPhase>1</TaskPhase>
                  <TaskStatus>0</TaskStatus>
                  <TaskType>8</TaskType>
            </Task>
      </Tasks>
      <RequestId>7E54C57C-DF5A-4FE8-8E25-DC888817B54D</RequestId>
</DescribeDrdsDbTasks>
```

JSON format `{`

```json
    "RequestId":"7E54C57C-DF5A-4FE8-8E25-DC888817B54D",
    "Tasks":{
        "Task":[
```

`{`

```json
                "ParentJobId":123,
                "AllowCancel":false,
                "GmtCreate":1568696422000,
                "TaskName":"Database creation task",
                "Progress":90,
                "TargetId":154,
                "ExpandType":"",
                "ShowProgress":true,
                "TaskDetail":"",
                "TaskPhase":1,
                "TaskStatus":0,
                "Label":"create_db",
                "TaskType":8
```

`]` `},`

```json
    "Success":true
```

#### 2.2.21 DescribeDrdsInstanceDbMonitor

Queries the performance monitoring data of a PolarDB-X 1.0 database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDrdsInsta nceDbMonitor | The operation that you want to perform. Set the value to DescribeDrdsInsta nceDbMonitor. |
| DbName | String | Yes | drds test _ | The name of the PolarDB-X 1.0 database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| EndTime | Long | Yes | 1568705520000 | The timestamp that specifies the end of the time range to query. |
| Key | String | Yes | qps | The monitoring metric. |
| StartTime | Long | Yes | 1568701920000 | The timestamp that specifies the beginning of the time range to query. |
| AccessKeyId | String | No | ASU67xxxxxxxxxxx xxxxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | - | - | The list of returned monitoring data. |
| Key | String | qps | The monitoring metric. |

| C P | loud Native Distributed Da olarDB-X | tabase | De | veloper Guide·API referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Unit | String | qps | The unit of the monitoring metric. |
| Values | - | - | The obtained values of the monitoring metric. |
| Date | Long | 1568705520000 | The timestamp when the value was obtained. |
| RequestId | String | 2F7F8080-9132-4279- 85D0-B7E5C4305162 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=DescribeDrdsInstanceDbMonitor &DbName=drds_test &DrdsInstanceId=drdsxxxxxxxxxxx &EndTime=1568705520000 &Key=qps &StartTime=1568701920000 <DescribeDrdsInstanceDbMonitor>
      <RequestId>D6A88429-BA1E-4294-BE37-E82167355122</RequestId>
      <Data>
            <Values>
                  <Date>1568705520000</Date>
                  <Value>10000</Value>
            </Values>
            <Unit>qps</Unit>
            <Key>qps</Key>
      </Data>
</DescribeDrdsInstanceDbMonitor>
```

JSON format `{`

```json
    "Data":[
```

`{`

```json
            "Values":[
```

`{`

```json
                    "Value":10000,
                    "Date":1568705520000
```

`],`

```json
            "Key":"qps",
            "Unit":"qps"
```

`],`

```json
    "RequestId":"D6A88429-BA1E-4294-BE37-E82167355122",
    "Success":true
```

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | ActionUnauthorized | The specified action is not available for you | The error message returned because you are not authorized to perform this action. Perform RAM authorization first. |

#### 2.2.22 DescribeDrdsShardingDbs

Queries details about a horizontally partitioned PolarDB-X 1.0 database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDrdsShard ingDbs | The operation that you want to perform. Set the value to DescribeDrdsShard ingDbs. |
| DbName | String | Yes | drds test _ | The name of the PolarDB-X 1.0 database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |

| loud Native Distribute olarDB-X | d Database |   | Develop | er Guide·API referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AccessKeyId | String | No | test | The AccessKey ID provided to you by Alibaba Cloud. |
| DbNamePattern | String | No | test | The matching pattern of the database name. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 509BDE17-505A-4B3B- 854D-30D3F092502F | The ID of the request. |
| ShardingDbs | - | - | The list of database shards. |
| ShardingDb | - | - | The details about a database shard. |
| BlockingTimeout | Integer | 5000 | The length of time that a transaction waits to obtain a lock. |
| ConnectUrl | String | 100.xx.xx.100:11569 | The connection URL. |
| ConnectionProperties | String | connectTimeout=3000; autoReconnect=true;fai lOverReadOnly=false;so cketTimeout=900000;re writeBatchedStatement s=true;characterEncodin g=utf8 | The properties of the connection string. |
| DbInstanceId | String | rm-bp1xxxxxxxxxxx | The ID of the ApsaraDB RDS for MySQL instance to which the database shard belongs. |
| DbStatus | String | running | The status of the database shard. |
| DbType | String | mysql | The type of the database shard. |
| GroupName | String | TEMP1 1568171495522S _ ABE KUP4 0000 _ _ | The name of the table shard. |
| IdleTimeOut | Integer | 30 | The idle connection timeout. |

| Developer Guide·API refere | nce | Cloud N | ative Distributed Database PolarDB- |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| MaxPoolSize | Integer | 60 | The maximum size of the connection pool. |
| MinPoolSize | Integer | 5 | The minimum size of the connection pool. |
| PreparedStatementCach eSize | Integer | 0 | The size of the result cache. |
| ShardingDbName | String | temp1 zhk1 0000 _ _ | The name of the database shard. |
| UserName | String | pg284mi8 | The username used to connect to the ApsaraDB RDS for MySQL instance. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=DescribeDrdsShardingDbs &DbName=drds_test &DrdsInstanceId=drdsxxxxxxxxx <DescribeDrdsShardingDbsResponse>
      <RequestId>509BDE17-505A-4B3B-854D-30D3F092502F</RequestId>
      <ShardingDbs>
            <ShardingDb>
                  <ShardingDbName>temp1_zhk1_0000</ShardingDbName>
                  <GroupName>TEMP1_1568171495522SABE_KUP4_0000</GroupName>
                  <MinPoolSize>5</MinPoolSize>
                  <IdleTimeOut>30</IdleTimeOut>
                  <DbStatus>RW</DbStatus>
                  <MaxPoolSize>60</MaxPoolSize>
                  <UserName>pg284mi8</UserName>
                  <ConnectUrl>100.xx.xx.101:11569</ConnectUrl>
                  <DbType>mysql</DbType>
                  <DbInstanceId>rm-bp1hxxxxxxxxxxx</DbInstanceId>
                  <BlockingTimeout>5000</BlockingTimeout>
                  <PreparedStatementCacheSize>0</PreparedStatementCacheSize>
                  <ConnectionProperties>connectTimeout=3000;autoReconnect=true;failOverRead
Only=false;socketTimeout=900000;rewriteBatchedStatements=true;characterEncoding=utf8</Conne ctionProperties> </Sh
```

`di`

```
Db>
```

```xml
            </ShardingDb>
            <ShardingDb>
                  <ShardingDbName>temp1_zhk1_0001</ShardingDbName>
                  <GroupName>TEMP1_1568171495522SABE_KUP4_0001</GroupName>
                  <MinPoolSize>5</MinPoolSize>
                  <IdleTimeOut>30</IdleTimeOut>
                  <DbStatus>RW</DbStatus>
                  <MaxPoolSize>60</MaxPoolSize>
                  <UserName>pg284mi8</UserName>
                  <ConnectUrl>100.xx.xx.101:11569</ConnectUrl>
                  <DbType>mysql</DbType>
                  <DbInstanceId>rm-bp1hxxxxxxxxxxx</DbInstanceId>
                  <BlockingTimeout>5000</BlockingTimeout>
                  <PreparedStatementCacheSize>0</PreparedStatementCacheSize>
                  <ConnectionProperties>connectTimeout=3000;autoReconnect=true;failOverRead
Only=false;socketTimeout=900000;rewriteBatchedStatements=true;characterEncoding=utf8</Conne ctionProperties>
            </ShardingDb>
            <ShardingDb>
                  <ShardingDbName>temp1_zhk1_0002</ShardingDbName>
                  <GroupName>TEMP1_1568171495522SABE_KUP4_0002</GroupName>
                  <MinPoolSize>5</MinPoolSize>
                  <IdleTimeOut>30</IdleTimeOut>
                  <DbStatus>RW</DbStatus>
                  <MaxPoolSize>60</MaxPoolSize>
                  <UserName>pg284mi8</UserName>
                  <ConnectUrl>100.xx.xx.101:11569</ConnectUrl>
                  <DbType>mysql</DbType>
                  <DbInstanceId>rm-bp1hxxxxxxxxxxx</DbInstanceId>
                  <BlockingTimeout>5000</BlockingTimeout>
                  <PreparedStatementCacheSize>0</PreparedStatementCacheSize>
                  <ConnectionProperties>connectTimeout=3000;autoReconnect=true;failOverRead
Only=false;socketTimeout=900000;rewriteBatchedStatements=true;characterEncoding=utf8</Conne ctionProperties>
            </ShardingDb>
            <ShardingDb>
                  <ShardingDbName>temp1_zhk1_0003</ShardingDbName>
                  <GroupName>TEMP1_1568171495522SABE_KUP4_0003</GroupName>
                  <MinPoolSize>5</MinPoolSize>
                  <IdleTimeOut>30</IdleTimeOut>
                  <DbStatus>RW</DbStatus>
                  <MaxPoolSize>60</MaxPoolSize>
                  <UserName>pg284mi8</UserName>
                  <ConnectUrl>100.xx.xx.101:11569</ConnectUrl>
                  <DbType>mysql</DbType>
                  <DbInstanceId>rm-bp1hxxxxxxxxxxx</DbInstanceId>
                  <BlockingTimeout>5000</BlockingTimeout>
                  <PreparedStatementCacheSize>0</PreparedStatementCacheSize>
                  <ConnectionProperties>connectTimeout=3000;autoReconnect=true;failOverRead
Only=false;socketTimeout=900000;rewriteBatchedStatements=true;characterEncoding=utf8</Conne ctionProperties>
            </ShardingDb>
            <ShardingDb>
                  <ShardingDbName>temp1_zhk1_0004</ShardingDbName>
<GroupName>TEMP11568171495522SABEKUP40004</GroupName>
```

```xml
                  <GroupName>TEMP1_1568171495522SABE_KUP4_0004</GroupName>
                  <MinPoolSize>5</MinPoolSize>
                  <IdleTimeOut>30</IdleTimeOut>
                  <DbStatus>RW</DbStatus>
                  <MaxPoolSize>60</MaxPoolSize>
                  <UserName>pg284mi8</UserName>
                  <ConnectUrl>100.xx.xx.101:11569</ConnectUrl>
                  <DbType>mysql</DbType>
                  <DbInstanceId>rm-bp1hxxxxxxxxxxx</DbInstanceId>
                  <BlockingTimeout>5000</BlockingTimeout>
                  <PreparedStatementCacheSize>0</PreparedStatementCacheSize>
                  <ConnectionProperties>connectTimeout=3000;autoReconnect=true;failOverRead
Only=false;socketTimeout=900000;rewriteBatchedStatements=true;characterEncoding=utf8</Conne ctionProperties>
            </ShardingDb>
            <ShardingDb>
                  <ShardingDbName>temp1_zhk1_0005</ShardingDbName>
                  <GroupName>TEMP1_1568171495522SABE_KUP4_0005</GroupName>
                  <MinPoolSize>5</MinPoolSize>
                  <IdleTimeOut>30</IdleTimeOut>
                  <DbStatus>RW</DbStatus>
                  <MaxPoolSize>60</MaxPoolSize>
                  <UserName>pg284mi8</UserName>
                  <ConnectUrl>100.xx.xx.101:11569</ConnectUrl>
                  <DbType>mysql</DbType>
                  <DbInstanceId>rm-bp1hxxxxxxxxxxx</DbInstanceId>
                  <BlockingTimeout>5000</BlockingTimeout>
                  <PreparedStatementCacheSize>0</PreparedStatementCacheSize>
                  <ConnectionProperties>connectTimeout=3000;autoReconnect=true;failOverRead
Only=false;socketTimeout=900000;rewriteBatchedStatements=true;characterEncoding=utf8</Conne ctionProperties>
            </ShardingDb>
            <ShardingDb>
                  <ShardingDbName>temp1_zhk1_0006</ShardingDbName>
                  <GroupName>TEMP1_1568171495522SABE_KUP4_0006</GroupName>
                  <MinPoolSize>5</MinPoolSize>
                  <IdleTimeOut>30</IdleTimeOut>
                  <DbStatus>RW</DbStatus>
                  <MaxPoolSize>60</MaxPoolSize>
                  <UserName>pg284mi8</UserName>
                  <ConnectUrl>100.xx.xx.101:11569</ConnectUrl>
                  <DbType>mysql</DbType>
                  <DbInstanceId>rm-bp1hxxxxxxxxxxx</DbInstanceId>
                  <BlockingTimeout>5000</BlockingTimeout>
                  <PreparedStatementCacheSize>0</PreparedStatementCacheSize>
                  <ConnectionProperties>connectTimeout=3000;autoReconnect=true;failOverRead
Only=false;socketTimeout=900000;rewriteBatchedStatements=true;characterEncoding=utf8</Conne ctionProperties>
            </ShardingDb>
            <ShardingDb>
                  <ShardingDbName>temp1_zhk1_0007</ShardingDbName>
                  <GroupName>TEMP1_1568171495522SABE_KUP4_0007</GroupName>
                  <MinPoolSize>5</MinPoolSize>
                  <IdleTimeOut>30</IdleTimeOut>
                  <DbStatus>RW</DbStatus>
```

`/`

```xml
                  <MaxPoolSize>60</MaxPoolSize>
                  <UserName>pg284mi8</UserName>
                  <ConnectUrl>100.xx.xx.101:11569</ConnectUrl>
                  <DbType>mysql</DbType>
                  <DbInstanceId>rm-bp1hxxxxxxxxxxx</DbInstanceId>
                  <BlockingTimeout>5000</BlockingTimeout>
                  <PreparedStatementCacheSize>0</PreparedStatementCacheSize>
                  <ConnectionProperties>connectTimeout=3000;autoReconnect=true;failOverRead
Only=false;socketTimeout=900000;rewriteBatchedStatements=true;characterEncoding=utf8</Conne ctionProperties>
            </ShardingDb>
      </ShardingDbs>
</DescribeDrdsShardingDbsResponse>
```

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | ActionUnauthorized | The specified action is not available for you | The error message returned because you are not authorized to perform this action. Perform RAM authorization first. |

#### 2.2.23 DescribeDrdsSlowSqls

Queries slow SQL statements of a PolarDB-X 1.0 database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDrdsSlow Sqls | The operation that you want to perform. Set the value to DescribeDrdsSlow Sqls. |
| DbName | String | Yes | tempdb | The name of the PolarDB-X database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| EndTime | Long | Yes | 1568289311 | The end of the time range to query. |
| ExeTime | Long | Yes | 1568289311 | The SQL execution time. |
| StartTime | Long | Yes | 1568267711 | The beginning of the time range to query. |
| AccessKeyId | String | No | test | The AccessKey ID provided to you by Alibaba Cloud. |
| PageNumber | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | - | - | The list of returned slow SQL statements. |
| Item | - | - | The details about a slow SQL statement. |
| Host | String | 10.xx.xx.26 | The IP address of the host where the slow SQL statement is executed. |
| ResponseTime | Long | 1568267711 | The response time. |
| Schema | String | user | The schema of the PolarDB-X database. |
| SendTime | Long | 1568267711 | The time when the slow SQL statement was sent. |
| Sql | String | SELECT count(1) from payment order where _ order status = '08'; _ | The content of the slow SQL statement. |

| loud Native Distributed Da | tabase |   |   |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| RequestId | String | 509BDE17-505A-4B3B- 854D-30D3F092502F | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |
| Total | Integer | 1 | The total number of slow SQL statements. |

```xml
http(s)://[Endpoint]/? Action=DescribeDrdsSlowSqls <DescribeDrdsSlowSqlsResponse>
      <Items>
            <Item>
                  <Host> 10.xx.xx.26 </Host>
                  <ResponseTime>2019-09-12 13:55:00</ResponseTime>
                  <Schema>user</Schema>
                  <SendTime>2019-09-12 13:55:00</SendTime>
                  <Sql>SELECT count(1) from  payment_order where  order_status = '08';</Sql
```

`>`

```xml
            </Item>
      </Items>
      <PageNumber>1</PageNumber>
      <PageSize>30</PageSize>
      <RequestId>B2493C08-AB69-44AB-8C1D-6AB17C2CF48F</RequestId>
      <Total>0</Total>
</DescribeDrdsSlowSqlsResponse>
```

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | ActionUnauthorized | The specified action is not available for you | The error message returned because you are not authorized to perform this action. Perform RAM authorization first. |

#### 2.2.24 DescribeDrdsSqlAuditStatus

Queries the details about SQL audit for a PolarDB-X 1.0 instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDrdsSqlAu ditStatus | The operation that you want to perform. Set the value to DescribeDrdsSqlAu ditStatus. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | test | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | - | - | The returned data set. |
| Data | - | - | The SQL audit details about a database. |
| DbName | String | table1 | The name of the database. |
| Detailed | String | test | The details about SQL audit. |
| Enabled | String | true | Indicates whether SQL audit was enabled for the database. |

| loud Native Distributed Da olarDB-X | tabase | De | veloper Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DC3ABA3E-0F8A-4596- 9104-F5155C34315B | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=DescribeDrdsSqlAuditStatus <DescribeGlobalBroadcastTypeResponse>
      <Data>
            <DbName>table1</DbName>
            <Detailed>test</Detailed>
            <Enabled>true</Enabled>
      </Data>
      <RequestId>DC3ABA3E-0F8A-4596-9104-F5155C34315B</RequestId>
</DescribeGlobalBroadcastTypeResponse>
```

#### 2.2.25 DescribeExpandLogicTableInfoList

Queries the shard keys of a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeExpandLo gicTableInfoList | The operation that you want to perform. Set the value to DescribeExpandLo gicTableInfoList. |
| DbName | String | Yes | drds db _ | The name of the PolarDB-X database. |

| eveloper Guide·API re | ference |   | Cloud Native | Distributed Database |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxxx x | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | test | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | - | - | The returned data set. |
| data | - | - | The details about shard keys. |
| ShardDbKey | String | id | The database shard key. |
| ShardTbKey | String | address | The table shard key. |
| TableName | String | employee split2 _ | The name of the table. |
| RequestId | String | 0B6B7BDC-575D-4A77- A4F8-24B7EF027B75 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```
http(s)://[Endpoint]/? Action=DescribeExpandLogicTableInfoList
```

```xml
<DescribeExpandLogicTableInfoListResponse>
      <Data>
            <data>
                  <ShardDbKey>id</ShardDbKey>
                  <TableName>employee_split2</TableName>
                  <ShardTbKey>address</ShardTbKey>
            </data>
      </Data>
      <RequestId>0B6B7BDC-575D-4A77-A4F8-24B7EF027B75</RequestId>
</DescribeExpandLogicTableInfoListResponse>
```

#### 2.2.26 DescribeGlobalBroadcastType

Queries whether the table in a PolarDB-X database is a broadcast table.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeGlobalBro adcastType | The operation that you want to perform. Set the value to DescribeGlobalBro adcastType. |
| DbName | String | Yes | drds db _ | The name of the PolarDB-X database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | - | - | The returned data set. |
| IsSyncType | Boolean | false | Indicates whether the table is a broadcast table. |

|   | Developer Guide·API refere | nce | Cloud N | ative Distributed Database PolarDB- | X |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DC3ABA3E-0F8A-4596- 9104-F5155C34315B | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=DescribeGlobalBroadcastType <DescribeGlobalBroadcastTypeResponse>
      <Data>
            <IsSyncType>false</IsSyncType>
      </Data>
      <RequestId>DC3ABA3E-0F8A-4596-9104-F5155C34315B</RequestId>
</DescribeGlobalBroadcastTypeResponse>
```

#### 2.2.27 DescribeHotDbList

Queries the available databases for hot-spot scale-out of a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeHotDbList | The operation that you want to perform. Set the value to DescribeHotDbList . |
| DbName | String | Yes | test | The name of the PolarDB-X database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |

| loud Native Distribute olarDB-X | d Database |   | Develop | er Guide·API referenc |
|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |
| AccessKeyId | String | No | test | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | - | - | The returned data set. |
| List | - | - | The list of returned items. |
| InstanceDb | - | - | The details about an item. |
| HotDbList | - | test,test | The list of hot-spot databases. |
| data | - | - | The details about a hot-spot database. |
| RandomCode | String | 989fdsf | The random code. |
| Msg | String | msg | The message. |
| RequestId | String | DSSDF-SEWE-23ERW | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```
http(s)://[Endpoint]/? Action=DescribeHotDbList
```

```xml
<DescribeHotDbListResponse>
      <RequestId>DSSDF-SEWE-23ERW</RequestId>
      <Msg>msg</Msg>
      <RandomCode>msg</RandomCode>
      <Data>
            <List>
                  <HotDbList></HotDbList>
            </List>
      </Data>
</DescribeHotDbListResponse>
```

#### 2.2.28 DescribeInstDbLogInfo

Queries the time range of historical SQL data that can be imported to a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeInstDbLog Info | The operation that you want to perform. Set the value to DescribeInstDbLog Info. |
| DbName | String | Yes | drds test _ | The name of the PolarDB-X database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | test | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| LogTimeRange | - | - | The supported time range. |
| SupportLatestTime | Long | 1568267711 | The beginning of the time range. |

| C P | loud Native Distributed Da olarDB-X | tabase | De | veloper Guide·API referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| SupportOldestTime | Long | 1568267711 | The end of the time range. |
| RequestId | String | DC3ABA3E-0F8A-4596- 9104-F5155C34315B | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=DescribeInstDbLogInfo <DescribeInstDbLogInfoResponse>
      <LogTimeRange>
            <SupportLatestTime>1568267711</SupportLatestTime>
            <SupportOldestTime>1568267711</SupportOldestTime>
      </LogTimeRange>
      <RequestId>DC3ABA3E-0F8A-4596-9104-F5155C34315B</RequestId>
</DescribeInstDbLogInfoResponse>
```

#### 2.2.29 DescribeRDSPerformance

Queries the performance data of ApsaraDB RDS for MySQL instances for a PolarDB-X instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRDSPerfor mance | The operation that you want to perform. Set the value to DescribeRDSPerfor mance. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |

| eveloper Guide·API re | ference |   | Cloud Native | Distributed Database PolarDB- |
|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |

| Keys | String | Yes | cpu | The performance metrics. |
|---|---|---|---|---|
| RdsInstanceId | String | Yes | rm- hbxxxxxxxxxxxx | The ID of the ApsaraDB RDS for MySQL instance. |
| AccessKeyId | String | No | test | The AccessKey ID provided to you by Alibaba Cloud. |
| DbInstType | String | No | mysql | The type of the ApsaraDB RDS for MySQL database. |
| EndTime | Long | No | 1568267711 | The end of the time range to query. |
| StartTime | Long | No | 1568267711 | The beginning of the time range to query. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | - | - | The returned data set. |
| Key | String | cpuusage | The performance metric. |
| NodeName | String | cpu | The name of the performance metric. |
| NodeNum | Integer | 1 | The number of nodes. |
| Unit | String | % | The unit of the performance metric. |
| Values | - | - | The value set. |
| Date | Long | 1568625038000 | The time when the value was obtained. |
| Value | String | 0.65 | The value of the performance metric. |

| loud Native Distributed Da olarDB-X | tabase | De | veloper Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F06B92ED-EF1B-4F8E- 8ACA-ECEFD5E4271C | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=DescribeRDSPerformance <DescribeRDSPerformanceResponse>
      <Data>
            <Key>cpuusage</Key>
            <NodeName>1</NodeName>
            <Unit>%</Unit>
            <Values>
              <Date>1568625038000</Date>
              <Value>0.65</Value>
            </Values>
      </Data>
      <RequestId>DC3ABA3E-0F8A-4596-9104-F5155C34315B</RequestId>
</DescribeRDSPerformanceResponse>
```

#### 2.2.30 DescribeRdsPerformanceSummary

Queries the performance metrics of ApsaraDB RDS for MySQL instances for a PolarDB-X instance, including CPU, input/output operations per second (IOPS), and active sessions.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRdsPerfor manceSummary | The operation that you want to perform. Set the value to DescribeRdsPerfor manceSummary. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| RdsInstanceId.N | RepeatList | Yes | ['rm- bp1xxxxxxxxxxxx',' rm- bp1xxxxxxxxxxx'] | The list of ApsaraDB RDS for MySQL instances. |
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RdsPerformanceInfos | - | - | The collection of RdsPerformanceInfos objects. |
| ActiveSessions | Integer | 0 | The number of active sessions on the current ApsaraDB RDS for MySQL instance. |
| Cpu | Float | 0.65 | The CPU utilization of the ApsaraDB RDS for MySQL instance. |
| Iops | Float | 10.56 | The IOPS of the ApsaraDB RDS for MySQL instance. |
| RdsId | String | rm-bp1xxxxxxxxxxxx | The ID of the ApsaraDB RDS for MySQL instance. |
| TotalSessions | Integer | 241 | The total number of sessions on the current ApsaraDB RDS for MySQL instance. |
| RequestId | String | 5D64DE5944A1E541E0CB 908A | The unique ID of the request. If any problem occurs, provide this request ID for troubleshooting. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=DescribeRdsPerformanceSummary &DrdsInstanceId=drdsxxxxxxxxxxx &RdsInstanceId.1=['rm-bp1xxxxxxxxxxxx','rm-bp1xxxxxxxxxxx'] <DescribeRdsPerformanceSummaryResponse>
        <code>200</code>
        <data>
                <RequestId>395533CB-12E8-4FDC-8934-127FD2024C0A</RequestId>
                <RdsPerformanceInfos>
                        <TotalSessions>241</TotalSessions>
                        <Cpu>0.65</Cpu>
                        <Iops>10.56</Iops>
                        <RdsId>rm-bp1xxxxxxxxxxxx</RdsId>
                        <ActiveSessions>0</ActiveSessions>
                </RdsPerformanceInfos>
        </data>
        <requestId>395533CB-12E8-4FDC-8934-127FD2024C0A</requestId>
        <successResponse>true</successResponse>
</DescribeRdsPerformanceSummaryResponse>
```

JSON format `{`

```json
    "successResponse":true,
    "requestId":"395533CB-12E8-4FDC-8934-127FD2024C0A",
    "data":{
        "RequestId":"395533CB-12E8-4FDC-8934-127FD2024C0A",
        "RdsPerformanceInfos":[
```

`{`

```json
                "Cpu":0.65,
                "RdsId":"rm-bp1xxxxxxxxxxxx",
                "TotalSessions":241,
                "Iops":10.56,
                "ActiveSessions":0
```

`],`

```json
        "Success":true
```

`},`

```json
    "code":"200"
```

#### 2.2.31 DescribeRdsSuperAccountInstances

Queries the privileged accounts of ApsaraDB RDS for MySQL instances for a PolarDB-X instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRdsSuper AccountInstances | The operation that you want to perform. Set the value to DescribeRdsSuper AccountInstances. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| RdsInstance.N | RepeatList | Yes | ['rm- bp1xxxxxxxxxxx','r m-bp1xxxxxxxxxx'] | The list of ApsaraDB RDS for MySQL instances. |
| AccessKeyId | String | No | **** | The AccessKey ID provided to you by Alibaba Cloud. |
| DbInstType | String | No | RDS | The type of the database instance. Default value: RDS. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DbInstances | - | rm-bp1xxxxxxxxxxx | The ID of the ApsaraDB RDS for MySQL instance. |
| DbInstance | - | - | The list of privileged accounts. |
| RequestId | String | 5D64DE5944A1E541E0CB 908A | The unique ID of the request. If any problem occurs, provide this request ID for troubleshooting. |

```xml
http(s)://[Endpoint]/? Action=DescribeRdsSuperAccountInstances &DrdsInstanceId=drdsxxxxxxxxxx &RdsInstance.1=['rm-bp1xxxxxxxxxxx','rm-bp1xxxxxxxxxx'] <DescribeRdsSuperAccountInstancesResponse>
      <code>200</code>
      <data>
            <RequestId>62CA96F4-B94F-4059-B23E-A58CCF318D3E</RequestId>
            <DbInstances></DbInstances>
      </data>
      <requestId>62CA96F4-B94F-4059-B23E-A58CCF318D3E</requestId>
      <successResponse>true</successResponse>
</DescribeRdsSuperAccountInstancesResponse>
```

JSON format `{`

```json
    "successResponse":true,
    "requestId":"62CA96F4-B94F-4059-B23E-A58CCF318D3E",
    "data":{
        "RequestId":"62CA96F4-B94F-4059-B23E-A58CCF318D3E",
        "DbInstances":{
            "DbInstance":[]
```

`},`

```json
    "code":"200"
```

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | ActionUnauthorized | The specified action is not available for you | The error message returned because you are not authorized to perform this action. Perform RAM authorization first. |

#### 2.2.32 DescribeRecycleBinStatus

Queries the status of the table recycle bin for a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRecycleBin Status | The operation that you want to perform. Set the value to DescribeRecycleBin Status. |
| DbName | String | Yes | tpch db _ | The name of PolarDB-X 1.0 database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5D64DE5944A1E541E0CB 908A | The unique ID of the request. If any problem occurs, provide this request ID for troubleshooting. |
| Status | String | disable | The status of the table recycle bin. Valid values: disable enable |
| Success | Boolean | true | Indicates whether the request was successful. |

```
http(s)://[Endpoint]/? Action=DescribeRecycleBinStatus &DbName=tpch_db &DrdsInstanceId=drdsxxxxxxxxxxx
```

```xml
<DescribeRecycleBinStatusResponse>
      <code>200</code>
      <data>
            <Status>enable</Status>
            <RequestId>E7D9B458-2C2D-44E3-BD55-92AD2172303F</RequestId>
      </data>
      <requestId>E7D9B458-2C2D-44E3-BD55-92AD2172303F</requestId>
      <successResponse>true</successResponse>
</DescribeRecycleBinStatusResponse>
```

JSON format `{`

```json
    "successResponse":true,
    "requestId":"E7D9B458-2C2D-44E3-BD55-92AD2172303F",
    "data":{
        "Status":"enable",
        "RequestId":"E7D9B458-2C2D-44E3-BD55-92AD2172303F",
        "Success":true
```

`},`

```json
    "code":"200"
```

#### 2.2.33 DescribeRecycleBinTables

Queries the tables that can be recycled for a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRecycleBin Tables | The operation that you want to perform. Set the value to DescribeRecycleBin Tables. |
| DbName | String | Yes | drds db _ | The name of the PolarDB-X database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | - | - | The returned data set. |
| CreateTime | String | 2019-09-16 14:42:06 | The time when the table was created. |
| OriginalTableName | String | BIN T4AG3CY5WWXPKHI _ TCHJY | The original name of the table. |
| TableName | String | drds params _ | The current name of the table. |
| RequestId | String | 5D64DE5944A1E541E0CB 908A | The unique ID of the request. If any problem occurs, provide this request ID for troubleshooting. |
| Success | Boolean | true | Indicates whether the request was successful. |

```
http(s)://[Endpoint]/? Action=DescribeRecycleBinTables
```

```xml
<DescribeRecycleBinTablesResponse>
      <code>200</code>
      <data>
            <RequestId>EC985705-2D6B-4B84-9732-BF8F5DCA247A</RequestId>
            <Data>
                  <OriginalTableName>drds_params</OriginalTableName>
                  <TableName>BIN_T4AG3CY5WWXPKHITCHJY</TableName>
                  <CreateTime>2019-09-16 14:42:06</CreateTime>
            </Data>
      </data>
      <requestId>EC985705-2D6B-4B84-9732-BF8F5DCA247A</requestId>
      <successResponse>true</successResponse>
</DescribeRecycleBinTablesResponse>
```

JSON format `{`

```json
    "successResponse":true,
    "requestId":"EC985705-2D6B-4B84-9732-BF8F5DCA247A",
    "data":{
        "Data":[
```

`{`

```json
                "OriginalTableName":"drds_params",
                "CreateTime":"2019-09-16 14:42:06",
                "TableName":"BIN_T4AG3CY5WWXPKHITCHJY"
```

`],`

```json
        "RequestId":"EC985705-2D6B-4B84-9732-BF8F5DCA247A",
        "Success":true
```

`},`

```json
    "code":"200"
```

#### 2.2.34 DescribeShardTaskInfo

Queries details about a partitioning task of a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeShardTas kInfo | The operation that you want to perform. Set the value to DescribeShardTas kInfo. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DbName | String | Yes | drds db _ | The name of the PolarDB-X database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| SourceTableName | String | Yes | a1 | The name of the source table. |
| TargetTableName | String | Yes | a2 | The name of the destination table. |
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | - | - | The returned data set. |
| Expired | String | 0 | The number of remaining days before the task expires. |
| Full | - | - | The full migration task. |
| Expired | Integer | 0 | The number of remaining days before the full migration task expires. |
| Progress | Integer | 100 | The full migration progress. |
| StartTime | String | 2019-09-16 15:11:53 | The start time of the full migration task. |
| Total | Integer | 2 | The total number of full migration tasks. |
| Tps | Integer | 0 | The current TPS of the full migration task. |
| FullCheck | - | - | The full check task. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Expired | Integer | 0 | The number of remaining days before the full check task expires. |
| Progress | Integer | 0 | The full check progress. |
| StartTime | String | 2019-09-16 15:12:53 | The start time of the full check task. |
| Total | Integer | 0 | The total number of full check tasks. |
| Tps | Integer | 0 | The current TPS of the full check task. |
| FullRevise | - | - | The full correction task. |
| Expired | Integer | 0 | The number of remaining days before the full correction task expires. |
| Progress | Integer | 0 | The full correction progress. |
| StartTime | String | 2019-09-16 15:12:53 | The start time of the full correction task. |
| Total | Integer | 0 | The total number of full correction tasks. |
| Tps | Integer | 0 | The current TPS of the full correction task. |
| Increment | - | - | The increment. |
| Delay | Integer | 1568617906 | The latency of the incremental synchronization. |
| StartTime | String | 2019-09-16 15:12:53 | The start time of the incremental synchronization. |
| Tps | Integer | 0 | The current TPS of the incremental synchronization. |
| Progress | String | 0 | The incremental synchronization progress. |

| D | eveloper Guide·API refere | nce | Cloud N | ative Distributed Database PolarDB- | X |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Review | - | - | The review task. |
| Expired | Integer | 0 | The number of remaining days before the review task expires. |
| Progress | Integer | 0 | The review progress. |
| StartTime | String | 2019-09-16 15:12:53 | The start time of the review task. |
| Total | Integer | 0 | The total number of review tasks. |
| Tps | Integer | 0 | The current TPS of the review task. |
| SourceTableName | String | a1 | The name of the source table. |
| Stage | String | 2 | The current stage of the task. |
| Status | String | Incremental synchronization | The status of the task. |
| TargetTableName | String | a2 | The name of the destination table. |
| RequestId | String | 5D64DE5944A1E541E0CB 908A | The unique ID of the request. If any problem occurs, provide this request ID for troubleshooting. |
| Success | Boolean | true | Indicates whether the request was successful. |

```
http(s)://[Endpoint]/? Action=DescribeShardTaskInfo
```

```xml
<DescribeShardTaskInfoResponse>
      <code>200</code>
      <data>
            <RequestId>42A9A85B-60F3-4858-88CD-2EE75251D19F</RequestId>
            <Data>
                  <Status>Incremental synchronization</Status>
                  <SourceTableName>a1</SourceTableName>
                  <Progress>0</Progress>
                  <FullCheck>
                        <Progress>0</Progress>
                        <Tps>0</Tps>
                        <Total>0</Total>
                        <Expired>0</Expired>
                  </FullCheck>
                  <Increment>
                        <Tps>0</Tps>
                        <StartTime>2019-09-16 15:12:53</StartTime>
                        <Delay>1568617906</Delay>
                  </Increment>
                  <FullRevise>
                        <Progress>0</Progress>
                        <Tps>0</Tps>
                        <Total>0</Total>
                        <Expired>0</Expired>
                  </FullRevise>
                  <Stage>2</Stage>
                  <Expired>0</Expired>
                  <Review>
                        <Progress>0</Progress>
                        <Tps>0</Tps>
                        <Total>0</Total>
                        <Expired>0</Expired>
                  </Review>
                  <TargetTableName>a2</TargetTableName>
                  <Full>
                        <Progress>100</Progress>
                        <Tps>0</Tps>
                        <Total>2</Total>
                        <StartTime>2019-09-16 15:11:53</StartTime>
                        <Expired>0</Expired>
                  </Full>
            </Data>
      </data>
      <requestId>42A9A85B-60F3-4858-88CD-2EE75251D19F</requestId>
      <successResponse>true</successResponse>
</DescribeShardTaskInfoResponse>
```

JSON format `{`

```json
    "successResponse":true,
    "requestId":"42A9A85B-60F3-4858-88CD-2EE75251D19F",
    "data":{
        "Data":{
            "Status":"Incremental synchronization",
            "FullRevise":{
                "Tps":0,
                "Expired":0,
                "Total":0,
                "Progress":0
```

`},`

```json
            "Full":{
                "Tps":0,
                "Expired":0,
                "StartTime":"2019-09-16 15:11:53",
                "Total":2,
                "Progress":100
```

`},`

```json
            "Increment":{
                "Tps":0,
                "Delay":1568617906,
                "StartTime":"2019-09-16 15:12:53"
```

`},`

```json
            "Expired":"0",
            "SourceTableName":"a1",
            "FullCheck":{
                "Tps":0,
                "Expired":0,
                "Total":0,
                "Progress":0
```

`},`

```json
            "Review":{
                "Tps":0,
                "Expired":0,
                "Total":0,
                "Progress":0
```

`},`

```json
            "TargetTableName":"a2",
            "Stage":"2",
            "Progress":"0"
```

`},`

```json
        "RequestId":"42A9A85B-60F3-4858-88CD-2EE75251D19F",
        "Success":true
```

`},`

```json
    "code":"200"
```

#### 2.2.35 DescribeShardTaskList

Queries the partitioning tasks of a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeShardTas kList | The operation that you want to perform. Set the value to DescribeShardTas kList. |
| DbName | String | Yes | testdb | The name of the PolarDB-X database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| Query | String | Yes | a1 | The query criteria. |
| TaskType | String | Yes | SINGLE TO SHARD _ _ | The type of the task. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| List | - | - | The list of returned objects. |
| Delay | Integer | 0 | The latency of the task. |
| Expired | String | 0 | The time when the task expired. |

|   |   | Cloud N | ative Distributed Database |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Expired | Long | 0 | The number of remaining days before the task expires. |
| Progress | Integer | 0 | The progress of the task. |
| SourceTableName | String | a1 | The name of the source table. |
| Stage | Integer | 1 | The current stage of the task. |
| TargetTableName | String | a2 | The name of the destination table. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 890BB376-5746-4145- A088-A455F8D359D0 | The unique ID of the request. If any problem occurs, provide this request ID for troubleshooting. |
| Success | Boolean | true | Indicates whether the request was successful. |
| Total | Integer | 1 | The total number of tables. |

```
http(s)://[Endpoint]/? Action=DescribeShardTaskList
```

```xml
<DescribeShardTaskListResponse>
      <code>200</code>
      <data>
            <PageSize>10</PageSize>
            <RequestId>890BB376-5746-4145-A088-A455F8D359D0</RequestId>
            <PageNumber>1</PageNumber>
            <Total>1</Total>
            <List>
                  <SourceTableName>a1</SourceTableName>
                  <Progress>0</Progress>
                  <Stage>1</Stage>
                  <Expired>0</Expired>
                  <TargetTableName>a2</TargetTableName>
                  <Delay>0</Delay>
            </List>
      </data>
      <requestId>890BB376-5746-4145-A088-A455F8D359D0</requestId>
      <successResponse>true</successResponse>
</DescribeShardTaskListResponse>
```

JSON format `{`

```json
    "successResponse":true,
    "requestId":"890BB376-5746-4145-A088-A455F8D359D0",
    "data":{
        "PageNumber":1,
        "PageSize":10,
        "RequestId":"890BB376-5746-4145-A088-A455F8D359D0",
        "Success":true,
        "List":[
```

`{`

```json
                "Delay":0,
                "Expired":0,
                "SourceTableName":"a1",
                "TargetTableName":"a2",
                "Stage":1,
                "Progress":0
```

`],`

```json
        "Total":1
```

`},`

```json
    "code":"200"
```

#### 2.2.36 DescribeSqlFlashbakTask

Queries the flashback tasks of a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSqlFlashb akTask | The operation that you want to perform. Set the value to DescribeSqlFlashb akTask. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | ***** | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5D64DE5944A1E541E0CB 908A | The unique ID of the request. If any problem occurs, provide this request ID for troubleshooting. |
| SqlFlashbackTasks | - | - | The list of returned flashback tasks. |
| SqlFlashbackTask | - | - | The details about a flashback task. |
| DbName | String | drds flashback _ | The name of the PolarDB-X database for the flashback task. |
| DownloadUrl | String | http://... | The download URL. |
| ExpireTime | Long | 1569216270000 | The time when the download URL expires. |
| GmtCreate | Long | 1568611408000 | The time when the task was created. |
| GmtModified | Long | 1568611469000 | The time when the task was modified. |
| Id | Long | 238 | The ID of the primary key. |

| loud Native Distributed Da olarDB-X | tabase | De | veloper Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| InstId | String | drdsxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| RecallProgress | Integer | 10 | The progress of the reverse call. |
| RecallRestoreType | Integer | 0 | The recovery type. Valid values: image restoration and reverse restoration. |
| RecallStatus | Integer | 1 | The status of the data recall task. |
| RecallType | Integer | 1 | The recall type. Valid values: exact match and fuzzy match. |
| SearchEndTime | Long | 1568609597000 | The end time of the query. |
| SearchStartTime | Long | 1568609597000 | The start time of the query. |
| SqlCounter | Long | 0 | The number of restored data rows. |
| SqlPk | String | id | The value of the SQL primary key. |
| SqlType | String | Insert,Update,Delete | The type of the SQL statement. |
| TableName | String | drds params _ | The name of the table to which data belongs. |
| TraceId | String | trace | The trace ID of the SQL statement. |
| Success | Boolean | true | Indicates whether the request was successful. |

```
http(s)://[Endpoint]/? Action=DescribeSqlFlashbakTask &DrdsInstanceId=drdsxxxxxxxxxx
```

```xml
<DescribeSqlFlashbakTaskResponse>
      <code>200</code>
      <data>
            <SqlFlashbackTasks>
                  <SqlFlashbackTask>
                        <GmtModified>1568611469000</GmtModified>
                        <SearchEndTime>1568611397000</SearchEndTime>
                        <RecallStatus>2</RecallStatus>
                        <SqlPk></SqlPk>
                        <RecallRestoreType>0</RecallRestoreType>
                        <TableName>drds_params</TableName>
                        <GmtCreate>1568611408000</GmtCreate>
                        <SearchStartTime>1568609597000</SearchStartTime>
                        <InstId>drdsxxxxxxxxxxx</InstId>
                        <RecallType>1</RecallType>
                        <TraceId></TraceId>
                        <DbName>drds_flashback</DbName>
                        <SqlType>Insert,Update,Delete</SqlType>
                        <Id>238</Id>
                        <ExpireTime>1569216270000</ExpireTime>
                        <SqlCounter>0</SqlCounter>
                        <RecallProgress>100</RecallProgress>
                        <DownloadUrl></DownloadUrl>
                  </SqlFlashbackTask>
            </SqlFlashbackTasks>
            <RequestId>11449CF1-6D32-4759-8F93-EAF36F176C41</RequestId>
      </data>
      <requestId>11449CF1-6D32-4759-8F93-EAF36F176C41</requestId>
      <successResponse>true</successResponse>
</DescribeSqlFlashbakTaskResponse>
```

JSON format `{`

```json
    "successResponse":true,
    "requestId":"11449CF1-6D32-4759-8F93-EAF36F176C41",
    "data":{
        "RequestId":"11449CF1-6D32-4759-8F93-EAF36F176C41",
        "SqlFlashbackTasks":{
            "SqlFlashbackTask":[
```

`{`

```json
                    "SearchStartTime":1568609597000,
                    "DbName":"drds_flashback",
                    "RecallStatus":2,
                    "InstId":"drdsxxxxxxxxxxx",
                    "SqlType":"Insert,Update,Delete",
                    "SqlPk":"",
                    "RecallProgress":100,
                    "GmtCreate":1568611408000,
                    "GmtModified":1568611469000,
                    "RecallRestoreType":0,
                    "ExpireTime":1569216270000,
                    "DownloadUrl":"",
                    "TraceId":"",
                    "Id":238,
                    "TableName":"drds_params",
                    "SqlCounter":0,
                    "SearchEndTime":1568611397000,
                    "RecallType":1
```

`]` `},`

```json
        "Success":true
```

`},`

```json
    "code":"200"
```

#### 2.2.37 DescribeTable

Queries the table schema of a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeTable | The operation that you want to perform. Set the value to DescribeTable. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DbName | String | Yes | drds db _ | The name of the PolarDB-X database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| TableName | String | Yes | employee split _ | The name of the table. |
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | - | - | The returned data set. |
| List | - | - | The details about the table structure. |
| ColumnName | String | Id | The name of the column. |
| ColumnType | String | bigint(20) | The type of the column. |
| Extra | String | auto increment _ | The extra information. |
| Index | String | PRI | The primary key. |
| IsAllowNull | String | NO | Indicates whether the column can be empty. |
| IsPk | String | YES | Indicates whether it is a primary key. |
| RequestId | String | 5DC75BC2-3F3F-4FE5- 8DC9-2A808B9AA401 | The unique ID of the request. If any problem occurs, provide this request ID for troubleshooting. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=DescribeTable <DescribeTableResponse>
      <code>200</code>
      <data>
            <RequestId>5DC75BC2-3F3F-4FE5-8DC9-2A808B9AA401</RequestId>
            <Data>
                  <List>
                        <ColumnName>Id</ColumnName>
                        <ColumnType>bigint(20)</ColumnType>
                        <Extra>auto_increment</Extra>
                        <IsAllowNull>NO</IsAllowNull>
                        <IsPk>YES</IsPk>
                        <Index>PRI</Index>
                  </List>
                  <List>
                        <ColumnName>Name</ColumnName>
                        <ColumnType>varchar(20)</ColumnType>
                        <Extra></Extra>
                        <IsAllowNull>NO</IsAllowNull>
                        <IsPk>NO</IsPk>
                        <Index></Index>
                  </List>
                  <List>
                        <ColumnName>Address</ColumnName>
                        <ColumnType>varchar(20)</ColumnType>
                        <Extra></Extra>
                        <IsAllowNull>NO</IsAllowNull>
                        <IsPk>NO</IsPk>
                        <Index></Index>
                  </List>
            </Data>
      </data>
      <requestId>5DC75BC2-3F3F-4FE5-8DC9-2A808B9AA401</requestId>
      <successResponse>true</successResponse>
</DescribeTableResponse>
```

JSON format `{`

```json
    "successResponse":true,
    "requestId":"5DC75BC2-3F3F-4FE5-8DC9-2A808B9AA401",
    "data":{
        "Data":{
            "List":[
```

`{`

```json
                    "IsPk":"YES",
                    "Extra":"auto_increment",
                    "Index":"PRI",
                    "IsAllowNull":"NO",
                    "ColumnType":"bigint(20)",
                    "ColumnName":"Id"
```

`},` `{`

```json
                    "IsPk":"NO",
                    "Extra":"",
                    "Index":"",
                    "IsAllowNull":"NO",
                    "ColumnType":"varchar(20)",
                    "ColumnName":"Name"
```

`},` `{`

```json
                    "IsPk":"NO",
                    "Extra":"",
                    "Index":"",
                    "IsAllowNull":"NO",
                    "ColumnType":"varchar(20)",
                    "ColumnName":"Address"
```

`]` `},`

```json
        "RequestId":"5DC75BC2-3F3F-4FE5-8DC9-2A808B9AA401",
        "Success":true
```

`},`

```json
    "code":"200"
```

#### 2.2.38 DescribeTableListByType

Queries type-specific tables of a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeTableList ByType | The operation that you want to perform. Set the value to DescribeTableList ByType. |
| DbName | String | Yes | drds db _ | The name of the PolarDB-X database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| Query | String | Yes | drdsxxxxxxxxxxxx | The search field. |
| TableType | String | Yes | SINGLE | The type of the table. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| List | - | - | The list of returned tables. |
| Property | String | single | The property. |
| TableName | String | employee split _ | The name of the table. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B360F47B-59E3-4D1C- BA03-6BFB1C993F88 | The unique ID of the request. If any problem occurs, provide this request ID for troubleshooting. |
| Success | Boolean | true | Indicates whether the request was successful. |
| Total | Integer | 1 | The total number of tables. |

```xml
http(s)://[Endpoint]/? Action=DescribeTableListByType <DescribeTableListByTypeResponse>
      <code>200</code>
      <data>
            <PageSize>10</PageSize>
            <RequestId>B360F47B-59E3-4D1C-BA03-6BFB1C993F88</RequestId>
            <PageNumber>1</PageNumber>
            <Total>1</Total>
            <List>
                  <TableName>employee_split</TableName>
                  <Property>single</Property>
            </List>
      </data>
      <requestId>B360F47B-59E3-4D1C-BA03-6BFB1C993F88</requestId>
      <successResponse>true</successResponse>
</DescribeTableListByTypeResponse>
```

JSON format `{`

```json
    "successResponse":true,
    "requestId":"B360F47B-59E3-4D1C-BA03-6BFB1C993F88",
    "data":{
        "PageNumber":1,
        "PageSize":10,
        "RequestId":"B360F47B-59E3-4D1C-BA03-6BFB1C993F88",
        "Success":true,
        "List":[
```

`{`

```json
                "TableName":"employee_split",
                "Property":"single"
```

`],`

```json
        "Total":1
```

`},`

```json
    "code":"200"
```

#### 2.2.39 DescribeTables

Queries the details about tables in a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeTables | The operation that you want to perform. Set the value to DescribeTables. |
| DbName | String | Yes | drds db _ | The name of the PolarDB-X database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| Query | String | Yes | drdsxxxxxxxxxxxx | The query criteria. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| List | - | - | The list of returned objects. |
| Broadcast | Boolean | false | Indicates whether the table is a broadcast table. |
| DbInstType | Integer | 0 | The type of the database instance. |
| IsLocked | Boolean | false | Indicates whether the table was locked. |
| IsShard | Boolean | false | Indicates whether the table was partitioned. |
| ShardKey | String | null | The shard key of the table. |
| Table | String | employee split _ | The name of the table. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 83AC3D7E-461C-4D87- 8ACD-6CC295178C6F | The unique ID of the request. If any problem occurs, provide this request ID for troubleshooting. |
| Success | Boolean | true | Indicates whether the request was successful. |
| Total | Integer | 1 | The total number of tables. |

```xml
http(s)://[Endpoint]/? Action=DescribeTables <DescribeTablesResponse>
      <code>200</code>
      <data>
            <PageSize>40</PageSize>
            <RequestId>83AC3D7E-461C-4D87-8ACD-6CC295178C6F</RequestId>
            <PageNumber>1</PageNumber>
            <Total>2</Total>
            <List>
                  <DbInstType>0</DbInstType>
                  <IsShard>false</IsShard>
                  <Table>employee_split</Table>
                  <Broadcast>false</Broadcast>
                  <ShardKey>null</ShardKey>
                  <IsLocked>false</IsLocked>
                  <AllowFullTableScan>false</AllowFullTableScan>
            </List>
            <List>
                  <DbInstType>0</DbInstType>
                  <IsShard>true</IsShard>
                  <Table>employee_split2</Table>
                  <Broadcast>false</Broadcast>
                  <ShardKey>["id"]</ShardKey>
                  <IsLocked>false</IsLocked>
                  <AllowFullTableScan>true</AllowFullTableScan>
            </List>
      </data>
      <requestId>83AC3D7E-461C-4D87-8ACD-6CC295178C6F</requestId>
      <successResponse>true</successResponse>
</DescribeTablesResponse>
```

JSON format `{`

```json
    "successResponse":true,
    "requestId":"83AC3D7E-461C-4D87-8ACD-6CC295178C6F",
    "data":{
        "PageNumber":1,
        "PageSize":40,
        "RequestId":"83AC3D7E-461C-4D87-8ACD-6CC295178C6F",
        "Success":true,
        "List":[
```

`{`

```json
                "IsLocked":false,
                "IsShard":false,
                "ShardKey":"null",
                "Broadcast":false,
                "Table":"employee_split",
                "DbInstType":0,
                "AllowFullTableScan":false
```

`},` `{`

```json
                "IsLocked":false,
                "IsShard":true,
                "ShardKey":"[\"id\"]",
                "Broadcast":false,
                "Table":"employee_split2",
                "DbInstType":0,
                "AllowFullTableScan":true
```

`],`

```json
        "Total":2
```

`},`

```json
    "code":"200"
```

#### 2.2.40 DisableSqlAudit

Disables SQL audit for a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DisableSqlAudit | The operation that you want to perform. Set the value to DisableSqlAudit. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DbName | String | Yes | drds db _ | The name of the PolarDB-X 1.0 database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | ***** | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5D64DE5944A1E541E0CB 908A | The unique ID of the request. If any problem occurs, provide this request ID for troubleshooting. |
| Result | Boolean | true | Indicates whether SQL audit was disabled for the PolarDB-X database. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=DisableSqlAudit <DisableSqlAuditResponse>
      <code>200</code>
      <data>
            <RequestId>5F72CB0C-7A49-458E-AAC7-F53BCDAACEEF</RequestId>
            <Result>true</Result>
      </data>
      <requestId>5F72CB0C-7A49-458E-AAC7-F53BCDAACEEF</requestId>
      <successResponse>true</successResponse>
</DisableSqlAuditResponse>
```

JSON format `{`

```json
    "successResponse":true,
    "requestId":"5F72CB0C-7A49-458E-AAC7-F53BCDAACEEF",
    "data":{
        "Result":true,
        "RequestId":"5F72CB0C-7A49-458E-AAC7-F53BCDAACEEF",
        "Success":true
```

`},`

```json
    "code":"200"
```

#### 2.2.41 ModifyAccountPrivilege

Modifies account permissions for a PolarDB-X instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AccountName | String | Yes | mytest@% | The name of the account. |
| Action | String | Yes | ModifyAccountPriv ilege | The operation that you want to perform. Set the value to ModifyAccountPriv ilege. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | 2zAEvsxxxxxxxxxxx x | The AccessKey ID provided to you by Alibaba Cloud. |
| DbPrivilege.N.DbN ame | String | No | ddltest | The name of the PolarDB-X database whose permissions will be changed. |
| DbPrivilege.N.Privil ege | String | No | RW | The database permissions that the account has. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 40E313AD-3B7C-4E34- B3BF-58AD0174D638 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=ModifyAccountPrivilege &AccountName=mytest@% &DrdsInstanceId=drdsxxxxxxxxxxxx <ModifyAccountPrivilegeResponse>
      <RequestId>40E313AD-3B7C-4E34-B3BF-58AD0174D638</RequestId>
</ModifyAccountPrivilegeResponse>
```

JSON format `{`

```json
    "RequestId":"40E313AD-3B7C-4E34-B3BF-58AD0174D638",
    "Success":true
```

#### 2.2.42 ModifyDrdsIpWhiteList

Modifies the IP address whitelist of a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDrdsIpWhit eList | The operation that you want to perform. Set the value to ModifyDrdsIpWhit eList. |
| DbName | String | Yes | test | The name of the PolarDB-X database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxx | The ID of the PolarDB-X instance. |
| IpWhiteList | String | Yes | 127.xx.xx.1,10.xx.x x.1 | The IP address whitelist after modification. Not e Use commas (,) to separate multiple IP addresses. |
| AccessKeyId | String | No | LTAIxxxxxxxxxxxxx xx | The AccessKey ID provided to you by Alibaba Cloud. |
| GroupAttribute | String | No | Group 1 | The attribute of an IP address group in the whitelist. |
| GroupName | String | No | drds group _ | The name of an IP address group in the whitelist. |
| Mode | Boolean | No | false | The modification mode. Valid values: true: appending false: overwriting |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5D64DE5944A1E541E0CB 908A | The unique ID of the request. If any problem occurs, provide this request ID for troubleshooting. |
| Success | Boolean | true | Indicates whether the request was successful. |

```
http(s)://[Endpoint]/? Action=ModifyDrdsIpWhiteList &DbName=test &DrdsInstanceId=drdsxxxxxxxxxx &IpWhiteList=127.xx.xx.1,10.xx.xx.1
```

JSON format `{`

```json
    "successResponse":true,
    "requestId":"CAC59657-4B81-478E-BB68-6C8FF8FFDF22",
    "data":{
        "RequestId":"CAC59657-4B81-478E-BB68-6C8FF8FFDF22",
        "Success":true
```

`},`

```json
    "code":"200"
```

#### 2.2.43 ModifyRdsReadWeight

Modifies the read weights of ApsaraDB RDS for MySQL instances.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DbName | String | Yes | db test _ | The name of the PolarDB-X database. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| InstanceNames | String | Yes | rm- bp1xxxxxxxxxxxxx, rm- bp1xxxxxxxxxxxxx | The list of ApsaraDB RDS for MySQL instances. Use commas (,) to separate multiple RDS instances. |
| Weights | String | Yes | 14,86 | The weight of each ApsaraDB RDS for MySQL instance. Use commas (,) to separate multiple weights. |
| AccessKeyId | String | No | LTAI8Gxxxxxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5D64DE5944A1E541E0CB 908A | The unique ID of the request. If any problem occurs, provide this request ID for troubleshooting. |
| Success | Boolean | true | Indicates whether the request was successful. |

```
http(s)://[Endpoint]/? Action=ModifyRdsReadWeight &DbName=db_test &DrdsInstanceId=drdsxxxxxxxxxx &InstanceNames=rm-bp1qxxxxxxxxxx,rm-bp1xxxxxxxxxxx &Weights=14,86
```

```xml
<ModifyRdsReadWeightResponse>
      <RequestId>B12FC174-D5CE-4A6E-83C1-0F8F864FF70A</RequestId>
</ModifyRdsReadWeightResponse>
```

JSON format `{`

```json
    "RequestId":"B12FC174-D5CE-4A6E-83C1-0F8F864FF70A",
    "Success":"true"
```

#### 2.2.44 PutStartBackup

Submits a data backup task for a PolarDB-X instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | PutStartBackup | The operation that you want to perform. Set the value to PutStartBackup. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | LTAI8Gxxxxxxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |
| BackupDbNames | String | No | db 1, db 2 _ _ | The names of the databases to be backed up. For database backups, you must specify the databases to be backed up. Use commas (,) to separate multiple database names. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| BackupLevel | String | No | db | The level of the backup. Valid values: instance database |
| BackupMode | String | No | phy | The mode of the backup. Valid values: phy: the quick backup logic: the consistent backup |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5D64DE5944A1E541E0CB 908A | The unique ID of the request. If any problem occurs, provide this request ID for troubleshooting. |
| Result | String | success | Indicates whether the backup task was submitted. |
| Success | Boolean | true | Indicates whether the request was successful. |

```
http(s)://[Endpoint]/? Action=PutStartBackup &DrdsInstanceId=drdsxxxxxxxxx
```

JSON format `{`

```json
    "successResponse":true,
    "requestId":"07D9CC74-2707-4234-BC5A-1F11AEB9AD7C",
    "data":{
        "Result":"success",
        "RequestId":"07D9CC74-2707-4234-BC5A-1F11AEB9AD7C",
        "Success":true
```

`},`

```json
    "code":"200"
```

#### 2.2.45 ReleaseHiStoreInstance

Releases a columnar storage instance, namely, a HiStore instance of a PolarDB-X instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| HistoreInstanceId | String | Yes | hi-hbgxxxxxxxxx | The ID of the HiStore instance. |
| RegionId | String | No | cn-beijing | The region ID of the PolarDB-X 1.0 instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5D64DE5944A1E541E0CB 908A | The unique ID of the request. If any problem occurs, provide this request ID for troubleshooting. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=ReleaseHiStoreInstance &DrdsInstanceId=drdsxxxxxxxxxx &HistoreInstanceId=hi-hbgxxxxxxxxx <ReleaseHiStoreInstanceResponse>
      <RequestId>B12FC174-D5CE-4A6E-83C1-0F8F864FF70A</RequestId>
</ReleaseHiStoreInstanceResponse>
```

JSON format `{`

```json
    "RequestId":"B12FC174-D5CE-4A6E-83C1-0F8F864FF70A",
    "Success":"true"
```

#### 2.2.46 RemoveBackupsSet

Removes a backup set from a PolarDB-X instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RemoveBackupsSe t | The operation that you want to perform. Set the value to RemoveBackupsSe t. |
| BackupId | String | Yes | c778036f-d464- 11e9-8d45- 7370dca6206b | The ID of the backup set. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | LTAI8xxxxxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5D64DE5944A1E541E0CB 908A | The unique ID of the request. If any problem occurs, provide this request ID for troubleshooting. |
| Result | String | success | Indicates whether the backup set was removed. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=RemoveBackupsSet &BackupId=c778036f-d464-11e9-8d45-7370dca6206b &DrdsInstanceId=drdsxxxxxxxxxx <RemoveBackupsSetResponse>
      <RequestId>B12FC174-D5CE-4A6E-83C1-0F8F864FF70A</RequestId>
</RemoveBackupsSetResponse>
```

JSON format `{`

```json
    "RequestId":"B12FC174-D5CE-4A6E-83C1-0F8F864FF70A",
    "Success":"true"
```

#### 2.2.47 RemoveDrdsDbFailedRecord

Removes database creation failure records from a PolarDB-X instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RemoveDrdsDbFail edRecord | The operation that you want to perform. Set the value to RemoveDrdsDbFail edRecord. |
| DbName | String | Yes | db test _ | The name of the PolarDB-X database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxx | The ID of the PolarDB-X instance. |
| AccessKeyId | String | No | LTAI8Gxxxxxxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5D64DE5944A1E541E0CB 908A | The ID of the request. |
| Result | Boolean | true | Indicates whether the database creation failure records were removed from the PolarDB-X instance. |
| Success | Boolean | true | Indicates whether the request was successful. |

```
http(s)://[Endpoint]/? Action=RemoveDrdsDbFailedRecord &DbName=db_test &DrdsInstanceId=drdsxxxxxxxxxx
```

```xml
<RemoveDrdsDbFailedRecordResponseponse>
      <code>200</code>
      <data>
            <RequestId>B12FC174-D5CE-4A6E-83C1-0F8F864FF70A</RequestId>
            <Result>true</Result>
      </data>
      <requestId>B12FC174-D5CE-4A6E-83C1-0F8F864FF70A</requestId>
      <successResponse>true</successResponse>
</RemoveDrdsDbFailedRecordResponseponse>
```

JSON format `{`

```json
    "successResponse":true,
    "requestId":"B12FC174-D5CE-4A6E-83C1-0F8F864FF70A",
    "data":{
        "Result":true,
        "RequestId":"B12FC174-D5CE-4A6E-83C1-0F8F864FF70A",
        "Success":true
```

`},`

```json
    "code":"200"
```

#### 2.2.48 RemoveRecycleBinTable

Removes tables from the recycle bin for a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RemoveRecycleBin Table | The operation that you want to perform. Set the value to RemoveRecycleBin Table. |
| DbName | String | Yes | my drds db _ _ | The name of the PolarDB-X 1.0 database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TableName | String | Yes | buy order _ | The name of the PolarDB-X 1.0 logical table. |
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Boolean | true | Indicates whether tables were removed from the table recycle bin. |
| RequestId | String | 6F70CE62-5077-4B7B- 95BC-4DAC45614DBE | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=RemoveRecycleBinTable &DbName=my_drds_db &DrdsInstanceId=drdsxxxxxxxxxx &TableName=buy_order <RemoveRecycleBinTableResponse>
      <RequestId>A3140FC7-B78B-4D8E-B0C8-926D28669934</RequestId>
      <Data>true</Data>
</RemoveRecycleBinTableResponse>
```

JSON format `{`

```json
    "Data":true,
    "RequestId":"A3140FC7-B78B-4D8E-B0C8-926D28669934",
    "Success":true
```

#### 2.2.49 ResetDrdsToRdsConnections

Resets the number of connections from the PolarDB-X 1.0 instance to ApsaraDB RDS for MySQL instances.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ResetDrdsToRdsC onnections | The operation that you want to perform. Set the value to ResetDrdsToRdsC onnections. |
| DbName | String | Yes | test my db _ _ | The name of the PolarDB-X 1.0 database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | fab3xxxxxxxxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6F70CE62-5077-4B7B- 95BC-4DAC45614DBE | The ID of the request. |
| Result | String | true | Indicates whether the number of connections from the PolarDB-X instance to ApsaraDB RDS for MySQL instances was reset. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=ResetDrdsToRdsConnections &DbName=test_my_db &DrdsInstanceId=drdsxxxxxxxxxxx <ResetDrdsToRdsConnectionsResponse>
      <RequestId>A3140FC7-B78B-4D8E-B0C8-926D28669934</RequestId>
      <Result>true</Result>
</ResetDrdsToRdsConnectionsResponse>
```

JSON format `{`

```json
    "Result":true,
    "RequestId":"A3140FC7-B78B-4D8E-B0C8-926D28669934",
    "Success":true
```

#### 2.2.50 SetupBroadcastTables

Configures a broadcast table for a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetupBroadcastTa bles | The operation that you want to perform. Set the value to SetupBroadcastTa bles. |
| Active | Boolean | Yes | true | Specifies whether to turn on the broadcast table switch. |
| DbName | String | Yes | test db _ | The name of the PolarDB-X 1.0 database. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| TableName.N | RepeatList | Yes | tb1 | The name of the PolarDB-X 1.0 table. |
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |

```xml
http(s)://[Endpoint]/? Action=SetupBroadcastTables &Active=true &DbName=test_db &DrdsInstanceId=drdsxxxxxxxxxxxxx &TableName.1=tb1 <SetupBroadcastTablesResponse>
        <RequestId>A3140FC7-B78B-4D8E-B0C8-926D28669934</RequestId>
        <Data>true</Data>
</SetupBroadcastTablesResponse>
```

JSON format `{`

```json
    "Data":true,
    "RequestId":"A3140FC7-B78B-4D8E-B0C8-926D28669934",
    "Success":true
```

#### 2.2.51 SetupRecycleBinStatus

Enables the table recycle bin for a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetupRecycleBinSt atus | The operation that you want to perform. Set the value to SetupRecycleBinSt atus. |
| DbName | String | Yes | db1 | The name of the PolarDB-X database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| StatusAction | String | Yes | enable | Specifies whether to enable the recycle bin. Valid values: enable disable |
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Boolean | true | The returned results. |
| RequestId | String | 6F70CE62-5077-4B7B- 95BC-4DAC45614DBE | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```
http(s)://[Endpoint]/? Action=SetupRecycleBinStatus &DbName=db1 &DrdsInstanceId=drdsxxxxxxxxxxxx &StatusAction=enable
```

```xml
<SetupRecycleBinStatusResponse>
        <RequestId>A3140FC7-B78B-4D8E-B0C8-926D28669934</RequestId>
        <Data>true</Data>
</SetupRecycleBinStatusResponse>
```

JSON format `{`

```json
    "Data":"true",
    "RequestId":"A3140FC7-B78B-4D8E-B0C8-926D28669934",
    "Success":true
```

#### 2.2.52 SetupTable

Enables full table scan for a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetupTable | The operation that you want to perform. Set the value to SetupTable. |
| AllowFullTableSca n | Boolean | Yes | true | Specifies whether to enable full table scan. |
| DbName | String | Yes | dbtest | The name of the PolarDB-X database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| TableName.N | RepeatList | Yes | tbtest | The name of the destination table. |
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Boolean | true | Indicates whether the full table scan was enabled. |
| RequestId | String | 6F70CE62-5077-4B7B- 95BC-4DAC45614DBE | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=SetupTable &AllowFullTableScan=true &DbName=dbtest &DrdsInstanceId=drdsxxxxxxxxx &TableName.1=tbtest <SetupTableResponse>
        <RequestId>A3140FC7-B78B-4D8E-B0C8-926D28669934</RequestId>
        <Data>true</Data>
</SetupTableResponse>
```

JSON format `{`

```json
    "Data":"true",
    "RequestId":"A3140FC7-B78B-4D8E-B0C8-926D28669934",
    "Success":true
```

#### 2.2.53 StartRestore

Starts a backup-based recovery task for a PolarDB-X instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | StartRestore | The operation that you want to perform. Set the value to StartRestore. |
| DrdsInstanceId | String | Yes | drdsxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | sdj23xxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |
| PreferredBackupTi me | String | No | 2019-09-10 20:18:! 8 | The point in time to which the PolarDB-X instance is restored. It is in the yyyy-MM-dd HH:mm:ss format. |
| BackupLevel | String | No | - | The backup level. |
| BackupMode | String | No | - | The backup mode. |
| BackupDbNames | String | No | test1,test2 | The names of databases to be restored. Use commas (,) to separate multiple names. If you do not configure this parameter, all databases on the PolarDB-X instance are restored by default. |
| BackupId | String | No | 23443 | The ID of the PolarDB-X 1.0 backup set. If this parameter is left blank, databases are restored based on PreferredBackupTi me by default. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 721C71DD-D3D0-4327- BFDD-67832698F55B | The ID of the request. |
| Result | String | success | Indicates whether the recovery task was successful. If success was returned, the recovery task was successful. If an error message was returned, the recovery task failed. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=StartRestore &DrdsInstanceId=drds43dsaew1 <StartRestoreResponse>
     <Result>success</Result>
     <RequestId>FE104D26-AC19-49B5-AC67-947F6915E07E</RequestId>
</StartRestoreResponse>
```

JSON format `{`

```json
    "Result":"success",
    "RequestId":"721C71DD-D3D0-4327-BFDD-67832698F55B",
    "Success":true
```

#### 2.2.54 SubmitCleanTask

Submits a cleanup task for smooth scale-out of a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SubmitCleanTask | The operation that you want to perform. Set the value to SubmitCleanTask. |
| DbName | String | Yes | test1 | The name of the PolarDB-X database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| ExpandType | String | Yes | smooth expand _ | The scale-out type. Valid values: smooth expan _ d: smooth scale-out. hot expand: _ hot-spot scale- out Not e Apsara Stack Enterprise Edition does not support hot-spot scale-out. |
| JobId | String | Yes | 123 | The job ID of the smooth scale-out task. The value of this parameter is the same as that of the ParentJobId parameter. |
| ParentJobId | String | Yes | 123 | The ID of the smooth scale-out task. This parameter is returned when you send a request for the smooth scale-out task. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AccessKeyId | String | No | sejkxxxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DSSDF-SEWE-23ERW | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=SubmitCleanTask &DbName=test1 &DrdsInstanceId=drdsxxxxxxxxxxx &ExpandType=smooth_expand &JobId=123 &ParentJobId=123 <SubmitCleanTaskResponse>
      <RequestId>DSSDF-SEWE-23ERW</RequestId>
</SubmitCleanTaskResponse>
```

JSON format `{`

```json
    "RequestId":"DSSDF-SEWE-23ERW",
    "Success":true
```

#### 2.2.55 SubmitSmoothExpandPreCheck

Submits a precheck task for smooth scale-out of a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SubmitSmoothExp andPreCheck | The operation that you want to perform. Set the value to SubmitSmoothExp andPreCheck. |
| DbInstType | String | Yes | RDS | The type of the database instance. Set the value to ApsaraDB RDS for MySQL. |
| DbName | String | Yes | test | The name of the PolarDB-X 1.0 database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | sdjwxxxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Msg | String | true | Indicates whether the precheck task was submitted. |
| RequestId | String | DSSDF-SEWE-23ERW | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |
| TaskId | Long | 2321 | The ID of the precheck task. |

```
http(s)://[Endpoint]/? Action=SubmitSmoothExpandPreCheck &DbInstType=RDS &DbName=test &DrdsInstanceId=drdsxxxxxxxxx
```

```xml
<SubmitSmoothExpandPreCheckResponse>
     <Msg>success</Msg>
     <RequestId>FE104D26-AC19-49B5-AC67-947F6915E07E</RequestId>
     <TaskId>97358</TaskId>
</SubmitSmoothExpandPreCheckResponse>
```

JSON format `{`

```json
    "RequestId":"FE104D26-AC19-49B5-AC67-947F6915E07E",
    "Msg":"success",
    "TaskId":97358,
    "Success":true
```

#### 2.2.56 SubmitSmoothExpandPreCheckTask

Submits a precheck task for smooth scale-out of a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SubmitSmoothExp andPreCheckTask | The operation that you want to perform. Set the value to SubmitSmoothExp andPreCheckTask. |
| DbName | String | Yes | test | The name of the PolarDB-X 1.0 database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | kswxxxxxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Msg | String | scucess | Indicates whether the precheck task was submitted. |
| RequestId | String | DSSDF-SEWE-23ERW | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |
| TaskId | Long | 2321 | The ID of the precheck task. |

```xml
http(s)://[Endpoint]/? Action=SubmitSmoothExpandPreCheckTask &DbName=test &DrdsInstanceId=drdsxxxxxxxxxx <SubmitSmoothExpandPreCheckTaskResponse>
     <Msg>success</Msg>
     <RequestId>FE104D26-AC19-49B5-AC67-947F6915E07E</RequestId>
     <TaskId>97358</TaskId>
</SubmitSmoothExpandPreCheckTaskResponse>
```

JSON format `{`

```json
    "RequestId":"FE104D26-AC19-49B5-AC67-947F6915E07E",
    "Msg":"success",
    "TaskId":97358,
    "Success":true
```

#### 2.2.57 SubmitSmoothExpandTask

Submits a smooth scale-out task for a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SubmitSmoothExp andTask | The operation that you want to perform. Set the value to SubmitSmoothExp andTask. |
| DbName | String | Yes | test | The name of the PolarDB-X 1.0 database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | swdxxxxxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |
| DbInstanceIsCreati ng | Boolean | No | true | Specifies whether the target ApsaraDB RDS for MySQL instance is created in the PolarDB-X 1.0 console. |
| RdsSuperInstances .N.AccountName | String | No | test drds _ | The privileged account of the ApsaraDB RDS for MySQL instance. |
| RdsSuperInstances .N.Password | String | No | Test1234 | The password of the privileged account of the ApsaraDB RDS for MySQL instance. |
| RdsSuperInstances .N.RdsName | String | No | rm-s34xxxxxxxxxx | The ID of the ApsaraDB RDS for MySQL instance in privileged mode. |
| TransferTaskInfos. N.DbName | String | No | test abds 0001 _ _ | The name of the physical database shard to be migrated. |
| TransferTaskInfos. N.DstInstanceNam e | String | No | rm-s34xxxxxxxxxx | The ID of the destination instance. |

| loud Native Distribute | d Database |   |   |   |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TransferTaskInfos. N.InstanceType | String | No | RDS | The type of the instance to be migrated. Set the value to ApsaraDB RDS for MySQL. |
| TransferTaskInfos. N.SrcInstanceNam e | String | No | rm-m23xxxxxxxxxx | The ID of the instance to be migrated. |

```xml
http(s)://[Endpoint]/? Action=SubmitSmoothExpandTask &DbName=test &DrdsInstanceId=drdsxxxxxxxxxx <SubmitSmoothExpandTaskResponse>
     <RequestId>DSSDF-SEWE-23ERW</RequestId>
</SubmitSmoothExpandTaskResponse>
```

JSON format `{`

```json
    "RequestId":"DSSDF-SEWE-23ERW",
    "success":true
```

#### 2.2.58 SubmitSwitchTask

Submits a switchover task for smooth scale-out of a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SubmitSwitchTask | The operation that you want to perform. Set the value to SubmitSwitchTask . |
| DbName | String | Yes | test | The name of the PolarDB-X 1.0 database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| ExpandType | String | Yes | smooth expand _ | The scale-out type. Valid values: smooth expan _ d: smooth scale-out. hot expand: _ hot-spot scale- out Not e Apsara Stack does not support hot- spot scale- out. |
| JobId | String | Yes | 123 | The job ID of the smooth scale-out task. The value of this parameter is the same as that of the ParentJobId parameter. |
| ParentJobId | String | Yes | 123 | The parent job ID of the smooth scale-out task. The value of this parameter is the same as that of the JobId parameter. |
| AccessKeyId | String | No | sejkwxxxxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |

```xml
http(s)://[Endpoint]/? Action=SubmitSwitchTask &DbName=test &DrdsInstanceId=drdsxxxxxxxxx &ExpandType=smooth_expand &JobId=123 &ParentJobId=123 <SubmitSwitchTaskResponse>
      <RequestId>DSSDF-SEWE-23ERW</RequestId>
</SubmitSwitchTaskResponse>
```

JSON format `{`

```json
    "RequestId":"DSSDF-SEWE-23ERW",
    "Success":true
```

#### 2.2.59 ValidateShardTask

Verifies whether a partitioning task of a PolarDB-X database is valid.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ValidateShardTask | The operation that you want to perform. Set the value to ValidateShardTask . |
| DbName | String | Yes | test | The name of the PolarDB-X 1.0 database. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DrdsInstanceId | String | Yes | drdsxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| SourceTableName | String | Yes | buyer | The name of the source table. |
| TargetTableName | String | Yes | buyer new _ | The name of the destination table. |
| TaskType | String | Yes | SINGLE TO SHARD _ _ | The type of the task. Valid values: SINGLE TO SHA _ _ RD: converts a single table to a table shard. SHARD TO SING _ _ LE: converts a table shard to a single table. SHARD TO SHA _ _ RD: converts a table shard to another table shard. |
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| List | - | - | The list of returned check results. |
| Item | String | same schema _ | The details about a check item. |
| Result | Integer | 0 | The check result. Valid values: 0: passed. 1: failed. |
| RequestId | String | DSSDF-SEWE-23ERW | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=ValidateShardTask &DbName=test &DrdsInstanceId=drds23dser21 &SourceTableName=buyer &TargetTableName=buyer_new &TaskType=SINGLE_TO_SHARD <ValidateShardTaskResponse>
     <List>
          <element>
               <Item>has_data</Item>
               <Result>0</Result>
          </element>
          <element>
               <item>same_schema</item>
               <result>0</result>
          </element>
          <element>
               <item>uk_in_source_table</item>
               <result>0</result>
          </element>
          <element>
               <item>uk_in_target_table</item>
               <result>0</result>
          </element>
     </List>
     <RequestId>DSSDF-SEWE-23ERW</RequestId>
</ValidateShardTaskResponse>
```

JSON format `{`

```json
    "RequestId":"DSSDF-SEWE-23ERW",
    "List":[
```

`{`

```json
            "Result":0,
            "Item":"has_data"
```

`},` `{`

```json
            "result":0,
            "item":"same_schema"
```

`},` `{`

```json
            "result":0,
            "item":"uk_in_source_table"
```

`},` `{`

```json
            "result":0,
            "item":"uk_in_target_table"
```

`],`

```json
    "success":true
```

#### 2.2.60 RemoveDrdsDb

Deletes a database from a PolarDB-X 1.0 instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RemoveDrdsDb | The operation that you want to perform. Set the value to RemoveDrdsDb. |
| DbName | String | Yes | db test _ | The name of the database to be deleted. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance from which the database will be deleted. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AccessKeyId | String | No | LTAI8xxxxxxxxxxxx x | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5D64DE5944A1E541E0CB 908A | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=RemoveDrdsDb &DbName=db_test &DrdsInstanceId=drds****c6vxxyzd <RemoveDrdsDbResponse>
      <RequestId>B12FC174-D5CE-4A6E-83C1-0F8F864FF70A</RequestId>
</RemoveDrdsDbResponse>
```

JSON format `{`

```json
    "RequestId":"B12FC174-D5CE-4A6E-83C1-0F8F864FF70A",
    "Success":true
```

#### 2.2.61 RefreshDrdsAtomUrl

Refreshes the connection between the PolarDB-X 1.0 instance and the ApsaraDB RDS for MySQL instance whose network type is changed to ensure that the connection is smooth.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RefreshDrdsAtom Url | The operation that you want to perform. Set the value to RefreshDrdsAtom Url. |
| DbName | String | Yes | db test _ | The name of the PolarDB-X database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | LTAI8xxxxxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5D64DE5944A1E541E0CB 908A | The unique ID of the request. If any problem occurs, provide this request ID for troubleshooting. |
| Result | Boolean | true | Indicates whether the connection after refresh was smooth. |
| Success | Boolean | true | Indicates whether the request was successful. |

```
http(s)://[Endpoint]/? Action=RefreshDrdsAtomUrl &DbName=db_test &DrdsInstanceId=drds****c6vxxyzd
```

```xml
<RefreshDrdsAtomUrlResponse>
      <RequestId>B12FC174-D5CE-4A6E-83C1-0F8F864FF70A</RequestId>
</RefreshDrdsAtomUrlResponse>
```

JSON format `{`

```json
    "RequestId":"B12FC174-D5CE-4A6E-83C1-0F8F864FF70A",
    "Success":"true"
```

### 2.3 Instance management

#### 2.3.1 CreateInstanceAccount

Creates an account for a PolarDB-X 1.0 instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AccountName | String | Yes | drds sample acco _ _ unt | The name of the account. |
| Action | String | Yes | CreateInstanceAcc ount | The operation that you want to perform. Set the value to CreateInstanceAcc ount. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxxx x | The ID of the PolarDB-X 1.0 instance. |
| Password | String | Yes | password | The password of the account. |
| DbPrivilege.N.DbN ame | String | No | testdb | The name of the PolarDB-X database. |
| DbPrivilege.N.Privil ege | String | No | RW | The access permissions that the account has on the PolarDB-X database. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | drds sample request i _ _ _ d | The ID of the request. |
| Success | Boolean | true | Indicates whether the account was created. |

```xml
http(s)://[Endpoint]/? Action=CreateInstanceAccount &AccountName=drds_sample_account &DrdsInstanceId=drdsxxxxxxxxxxxxxx &Password=password &DbPrivilege=[{"DbName":"testdb", "Privilege":"RW"}] <CreateInstanceAccount>
      <RequestId>FF13E47D-4E38-4A5A-BA68-4E610EF35A25</RequestId>
</CreateInstanceAccount>
```

JSON format `{`

```json
    "RequestId":"FF13E47D-4E38-4A5A-BA68-4E610EF35A25",
    "Success":true
```

#### 2.3.2 DescribeDrdsDBs

Queries the details about databases on a PolarDB-X 1.0 instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDrdsDBs | The operation that you want to perform. Set the value to DescribeDrdsDBs. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | DJKSJKF12831283 | The AccessKey ID provided to you by Alibaba Cloud. |
| PageNumber | Integer | No | 1 | The number of the page to return. Pages start from page 1. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | - | - | The returned data set. |
| Db | - | - | The details about a PolarDB-X 1.0 database. |
| CreateTime | String | 1563773824000 | The timestamp when the PolarDB-X 1.0 database was created. |
| DbInstType | String | RDS | The type of the PolarDB-X 1.0 database. |
| DbName | String | drds test _ | The name of the PolarDB-X 1.0 database. |
| Mode | String | HORIZONTAL | The partition mode of the PolarDB-X 1.0 database. |
| Schema | String | drds test 15637738711 _ _ 18kxqd | The partitioning configuration ID of the PolarDB-X 1.0 database. |
| Status | String | NORMAL | The status of the PolarDB-X 1.0 database. |

| Developer Guide·API refere | nce | Cloud N | ative Distributed Database PolarDB- |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | String | 1 | The page number of the returned page. |
| PageSize | String | 10 | The number of entries returned on the page. |
| RequestId | String | 006B7D19-8CDB-4AA6- AAE7-23C1075276E1 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |
| Total | String | 1 | The total number of databases. |

```xml
http(s)://[Endpoint]/? Action=DescribeDrdsDBs &DrdsInstanceId=drdsxxxxxxxxxx <DescribeDrdsDBs>
      <PageSize>10</PageSize>
      <RequestId>006B7D19-8CDB-4AA6-AAE7-23C1075276E1</RequestId>
      <PageNumber>1</PageNumber>
      <Total>1</Total>
      <Data>
            <Db>
                  <Status>NORMAL</Status>
                  <DbInstType>RDS</DbInstType>
                  <Schema>george_1563773871118kxqd</Schema>
                  <CreateTime>1563773824000</CreateTime>
                  <Mode>HORIZONTAL</Mode>
                  <DbName>george</DbName>
            </Db>
      </Data>
</DescribeDrdsDBs>
```

JSON format `{`

```json
    "Data":{
        "Db":[
```

`{`

```json
                "Status":"NORMAL",
                "DbName":"george",
                "CreateTime":1563773824000,
                "Schema":"george_1563773871118kxqd",
                "DbInstType":"RDS",
                "Mode":"HORIZONTAL"
```

`]` `},`

```json
    "PageNumber":1,
    "PageSize":10,
    "RequestId":"006B7D19-8CDB-4AA6-AAE7-23C1075276E1",
    "Success":true,
    "Total":1
```

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | ActionUnauthorized | The specified action is not available for you | The error message returned because you are not authorized to perform this action. Perform RAM authorization first. |

#### 2.3.3 DescribeDrdsInstance

Queries the details about a PolarDB-X 1.0 instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDrdsInsta nce | The operation that you want to perform. Set the value to DescribeDrdsInsta nce. |
| DrdsInstanceId | String | Yes | drdssexxxxxxxx | The ID of the PolarDB-X 1.0 instance. |

| eveloper Guide·API re | ference |   | Cloud Native | Distributed Database PolarDB- |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AccessKeyId | String | No | ASU678xxxxxxxxxx xx | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | - | - | The details about the PolarDB-X 1.0 instance. |
| CommodityCode | String | drdsPost | The commodity code. |
| CreateTime | Long | 1568620311000 | The timestamp when the PolarDB-X instance was created. |
| Description | String | drds test _ | The description of the PolarDB-X instance. |
| DrdsInstanceId | String | drdsxxxxxxxxx | The ID of the PolarDB-X instance. |
| ExpireDate | Long | 4724323200000 | The timestamp when the PolarDB-X instance expires. |
| InstRole | String | MASTER | The role of the PolarDB- X instance. Valid values: MASTER: the primary instance. SLAVE: the analytic read-only instance. SLAVE FLOW: the _ concurrent read-only instance. |
| InstanceSeries | String | drds.sn2.4c16g | The instance type family. |
| InstanceSpec | String | drds.sn2.4c16g.8C32G | The specifications of the PolarDB-X instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Label | String | NORMAL | The label of the PolarDB-X instance. Valid values: NORMAL: the normal instance. HA: the high- availability instance. VPC: the Virtual Private Cloud (VPC) instance. Not e Apsara Stack does not support VPC instances. |
| MachineType | String | ecs | The type of the machine where the PolarDB-X instance is deployed. Set the value to ECS. |
| MasterInstanceId | String | drdsxxxxxxxxx | The ID of the primary instance. This parameter is returned only for read-only instances. |
| NetworkType | String | CLASSIC | The network type of the PolarDB-X instance. Valid values: CLASSIC: the classic network. VPC: the VPC network. |
| OrderInstanceId | String | drdsxxxxxxxxx | The ID of the purchased PolarDB-X instance. |
| ReadOnlyDBInstanceIds | - | drdsxxxxxxxxx | The list of read-only PolarDB-X instances. |
| ReadOnlyDBInstanceId | - | - | The details about of a read-only PolarDB-X instance. |
| RegionId | String | cn-hangzhou | The region of the PolarDB-X instance. |

| eveloper Guide·API refere | nce | Cloud N | ative Distributed Database |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | String | RUN | The status of the PolarDB-X instance. |
| Type | String | PRIVATE | The type of the PolarDB-X instance. Valid values: PRIVATE: the dedicated instance. PUBLIC: the shared instance. |
| Version | Long | 0 | The version of the PolarDB-X instance. This parameter is empty. |
| VersionAction | String | Upgradeable | The available action for the PolarDB-X instance version. |
| Vips | - | - | The list of returned virtual IP addresses (VIPs). |
| Vip | - | - | The details about a VIP. |
| Dns | String | drdsxxxxxxxxx.drds.aliyu ncs.com | The domain name bound to the VIP. |
| ExpireDays | Long | 0 | The number of days before the VIP expires. |
| Port | String | 3306 | The open port of the VIP. |
| Type | String | intranet | The type of the VIP. Valid values: intranet internet |
| VpcId | String | vpc-bpxxxxxxxxxxxy | The ID of the VPC network connected to the instance. |
| VswitchId | String | vsw-bpxxxxxxxxxxxxx96 | The ID of the virtual switch (VSwitch). |
| VpcCloudInstanceId | String | drdsxxxxxxxxx | The ID of the PolarDB-X instance in the VPC cluster. |
| ZoneId | String | cn-hangzhou-e | The ID of the zone. |

| olarDB-X |   |   |   |
|---|---|---|---|
| Parameter | Type | Example | Description |
| RequestId | String | B4F76641-BA45-4320- BE7C-9C62CFDAC9B2 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=DescribeDrdsInstance &DrdsInstanceId=drdsxxxxxxxxx <DescribeDrdsInstance>
      <RequestId>B4F76641-BA45-4320-BE7C-9C62CFDAC9B2</RequestId>
      <Data>
            <Status>RUN</Status>
            <Description>drds_test</Description>
            <InstanceSpec>drds.sn2.4c16g.8C32G</InstanceSpec>
            <ZoneId>cn-hangzhou-e</ZoneId>
            <ExpireDate>4724323200000</ExpireDate>
            <CreateTime>1568620311000</CreateTime>
            <MachineType>ecs</MachineType>
            <Label>NORMAL</Label>
            <InstanceSeries>drds.sn2.4c16g</InstanceSeries>
            <VersionAction>Can_Be_Rolled_Back</VersionAction>
            <Type>PRIVATE</Type>
            <DrdsInstanceId>drdsxxxxxxxxx</DrdsInstanceId>
            <OrderInstanceId>drdsxxxxxxxxx</OrderInstanceId>
            <InstRole>MASTER</InstRole>
            <NetworkType>CLASSIC</NetworkType>
            <CommodityCode>drdsPost</CommodityCode>
            <RegionId>cn-hangzhou</RegionId>
            <Vips>
                  <Vip>
                        <Type>intranet</Type>
                        <VpcId></VpcId>
                        <Port>3306</Port>
                        <Dns>drdsxxxxxxxxx.drds.aliyuncs.com</Dns>
                  </Vip>
            </Vips>
      </Data>
</DescribeDrdsInstance>
```

JSON format `{`

```json
    "Data":{
        "MachineType":"ecs",
        "Description":"drds_test",
        "OrderInstanceId":"drdsxxxxxxxxx",
        "Type":"PRIVATE",
        "ZoneId":"cn-hangzhou-e",
        "InstRole":"MASTER",
        "NetworkType":"CLASSIC",
        "Status":"RUN",
        "ExpireDate":4724323200000,
        "Vips":{
            "Vip":[
```

`{`

```json
                    "Dns":"drdsxxxxxxxxx.drds.aliyuncs.com",
                    "Port":3306,
                    "Type":"intranet",
                    "VpcId":""
```

`]` `},`

```json
        "VersionAction":"Can_Be_Rolled_Back",
        "RegionId":"cn-hangzhou",
        "CommodityCode":"drdsPost",
        "InstanceSpec":"drds.sn2.4c16g.8C32G",
        "CreateTime":1568620311000,
        "InstanceSeries":"drds.sn2.4c16g",
        "Label":"NORMAL",
        "DrdsInstanceId":"drdsxxxxxxxxx"
```

`},`

```json
    "RequestId":"B4F76641-BA45-4320-BE7C-9C62CFDAC9B2",
    "Success":true
```

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | ActionUnauthorized | The specified action is not available for you | The error message returned because you are not authorized to perform this action. Perform RAM authorization first. |

#### 2.3.4 DescribeDrdsInstanceLevelTasks

Queries incomplete tasks for a PolarDB-X 1.0 instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDrdsInsta nceLevelTasks | The operation that you want to perform. Set the value to DescribeDrdsInsta nceLevelTasks. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | ASU67xxxxxxxxxxx xx | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 2F7F8080-9132-4279- 85D0-B7E5C4305162 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |
| Tasks | - | - | The list of returned incomplete tasks. |
| Task | - | - | The details about an incomplete task. |
| AllowCancel | Boolean | false | Indicates whether the task can be canceled. |
| ErrMsg | String | The status of the instance is abnormal. | The error message of the task. |
| GmtCreate | Long | 1568705520000 | The timestamp when the task was created. |
| Progress | Integer | 99 | The task progress. Valid values: 0 to 100. |
| ProgressDescription | String | Executing | The description of the task execution progress. |
| ShowProgress | Boolean | true | Indicates whether the progress was displayed. |
| TaskName | String | upgrade instance _ | The name of the task. |

| Developer Guide·API refere | nce | Cloud N | ative Distributed Database PolarDB- |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| TaskPhase | String | 1 | The phase of the task. |
| TaskStatus | Integer | 0 | The status of the task. Valid values: 0: executing 1: successful 2: failed 3: canceled |
| TaskType | Integer | 11 | The type of the task. |

```xml
http(s)://[Endpoint]/? Action=DescribeDrdsInstanceLevelTasks &DrdsInstanceId=drdsxxxxxxxxxx <DescribeDrdsInstanceLevelTasks>
      <Tasks>
            <Task>
                  <AllowCancel>false</AllowCancel>
                  <GmtCreate>1568696422000</GmtCreate>
                  <Progress>90</Progress>
                  <ShowProgress>true</ShowProgress>
                  <TargetId>154</TargetId>
                  <TaskDetail></TaskDetail>
                  <ProgressDescription>Executing</ProgressDescription>
                  <TaskName>Upgrade task</TaskName>
                  <TaskPhase>1</TaskPhase>
                  <TaskStatus>0</TaskStatus>
                  <TaskType>11</TaskType>
                  <ErrMsg></ErrMsg>
            </Task>
      </Tasks>
      <RequestId>1BEEBC05-437E-456D-94A4-CEE1F5676BCF</RequestId>
</DescribeDrdsInstanceLevelTasks>
```

JSON format `{`

```json
    "RequestId":"1BEEBC05-437E-456D-94A4-CEE1F5676BCF",
    "Tasks":{
        "Task":[
```

`{`

```json
                "ShowProgress":true,
                "TaskPhase":1,
                "TaskDetail":"",
                "ErrMsg":"",
                "TaskStatus":0,
                "TaskType":11,
                "TaskName":"Upgrade task",
                "GmtCreate":1568696422000,
                "AllowCancel":false,
                "ProgressDescription":"Executing",
                "TargetId":154,
                "Progress":90
```

`]` `},`

```json
    "Success":true
```

#### 2.3.5 DescribeDrdsInstanceMonitor

Queries the monitoring data of a PolarDB-X 1.0 instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDrdsInsta nceMonitor | The operation that you want to perform. Set the value to DescribeDrdsInsta nceMonitor. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| EndTime | Long | Yes | 1568705520000 | The timestamp that specifies the end of the time range to query. |
| Key | String | Yes | cpu | The monitoring metric. |

| eveloper Guide·API re | ference |   | Cloud Native | Distributed Database PolarDB- |
|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |
| RegionId | String | Yes | cn-hangzhou | The region ID of the PolarDB-X instance. |
| StartTime | Long | Yes | 1568701920000 | The timestamp that specifies the beginning of the time range to query. |
| AccessKeyId | String | No | ASU6xxxxxxxxxxxx xxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |
| PeriodMultiple | Integer | No | 1 | The multiple of the monitoring data period. By default, the monitoring data period is 5 minutes. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | - | - | The list of returned monitoring data. |
| Key | String | cpu | The monitoring metric. |
| NodeNum | Integer | 1 | The number of the PolarDB-X 1.0 nodes. |
| Unit | String | % | The unit of the monitoring metric. |
| Values | - | - | The obtained values of the monitoring metric. |
| Date | Long | 1568703720000 | The timestamp when the value was obtained. |
| Value | String | 1.00 | The metric value. |
| RequestId | String | 2F7F8080-9132-4279- 85D0-B7E5C4305162 | The ID of the request. |

```xml
http(s)://[Endpoint]/? Action=DescribeDrdsInstanceMonitor &DrdsInstanceId=drdsxxxxxxxxxx &EndTime=1568705520000 &Key=cpu &RegionId=cn-hangzhou &StartTime=1568701920000 <DescribeDrdsInstanceMonitor>
      <RequestId>0EB04DD8-A3C8-4C40-A7DC-865BE490216B</RequestId>
      <Data>
            <NodeNum>1</NodeNum>
            <Values>
                  <Value>1.00</Value>
                  <Date>1568703720000</Date>
            </Values>
            <Values>
                  <Value>0.93</Value>
                  <Date>1568703780000</Date>
            </Values>
            <Values>
                  <Value>0.67</Value>
                  <Date>1568703840000</Date>
            </Values>
            <Unit>%</Unit>
            <Key>cpu</Key>
      </Data>
</DescribeDrdsInstanceMonitor>
```

JSON format `{`

```json
    "Data":[
```

`{`

```json
            "Values":[
```

`{`

```json
                    "Value":"1.00",
                    "Date":1568703720000
```

`},` `{`

```json
                    "Value":"0.93",
                    "Date":1568703780000
```

`},` `{`

```json
                    "Value":"0.67",
                    "Date":1568703840000
```

`],`

```json
            "Key":"cpu",
            "NodeNum":1,
            "Unit":"%"
```

`],`

```json
    "RequestId":"0EB04DD8-A3C8-4C40-A7DC-865BE490216B"
```

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | ActionUnauthorized | The specified action is not available for you | The error message returned because you are not authorized to perform this action. Perform RAM authorization first. |

#### 2.3.6 DescribeDrdsInstances

Queries PolarDB-X 1.0 instances that meet specific criteria in a region.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDrdsInsta nces | The operation that you want to perform. Set the value to DescribeDrdsInsta nces. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The region ID of the PolarDB-X instance. |
| AccessKeyId | String | No | ASU678xxxxxxxxxx xxxxx | The AccessKey ID provided to you by Alibaba Cloud. |
| Description | String | No | drds test _ | The description of the PolarDB-X 1.0 instance. |
| Expired | Boolean | No | false | Specifies whether the instance expires. |
| PageNumber | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. |
| Tag.N.Key | String | No | acs:newretail:do main | The key of the Nth tag. |
| Tag.N.Value | String | No | NEW RETAIL _ | The value of the Nth tag. |
| Type | String | No | 1 | The type of the PolarDB-X instance. Valid values: 0: the shared instance. 1: the dedicated instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Instances | - | - | The list of returned PolarDB-X instances. |
| Instance | - | - | The details about a PolarDB-X instance. |

| eveloper Guide·API refere | nce | Cloud N | ative Distributed Database |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| CommodityCode | String | drdsPost | The commodity code. |
| CreateTime | Long | 1568620311000 | The timestamp when the PolarDB-X instance was created. |
| Description | String | drds test _ | The description of the PolarDB-X instance. |
| DrdsInstanceId | String | drdsxxxxxxxxxx | The ID of the PolarDB-X instance. |
| ExpireDate | Long | 4724323200000 | The timestamp when the PolarDB-X instance expires. |
| InstRole | String | MASTER | The role of the PolarDB- X instance. MASTER: the primary instance. SLAVE: the analytic read-only instance. SLAVE FLOW: the _ concurrent read-only instance. |
| InstanceSeries | String | drds.sn2.4c16g | The instance type family. |
| InstanceSpec | String | drds.sn2.4c16g.8C32G | The specifications of the PolarDB-X instance. |
| Label | String | NORMAL | The label of the PolarDB-X instance. Valid values: NORMAL: the normal instance. HA: the high- availability instance. VPC: the Virtual Private Cloud (VPC) instance. |
| MachineType | String | ecs | The type of machine where the PolarDB-X instance is deployed. Set the value to ECS. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| MasterInstanceId | String | drdsxxxxxxxxxx | The ID of the primary instance. This parameter is only available for read-only instances. |
| NetworkType | String | CLASSIC | The network type of the PolarDB-X instance. Valid values: CLASSIC: the classic network. VPC: the VPC network. Not e Apsara Stack does not support VPC networks. |
| OrderInstanceId | String | drdsxxxxxxxxxx | The ID of the created PolarDB-X instance. |
| ReadOnlyDBInstanceIds | - | drdsxxxxxxxxxx | The list of read-only PolarDB-X instances. |
| ReadOnlyDBInstanceId | - | - | The details about of a read-only PolarDB-X instance. |
| RegionId | String | cn-hangzhou | The region ID of the PolarDB-X instance. |
| Status | String | RUN | The status of the PolarDB-X instance. |
| Type | String | PRIVATE | The type of the PolarDB-X instance. Valid values: PUBLIC: the shared instance. PRIVATE: the dedicated instance. |
| Version | Long | 0 | The version of the PolarDB-X instance. |
| VersionAction | String | Upgradable | The available actions for the PolarDB-X instance version. |

| D | eveloper Guide·API refere | nce | Cloud N | ative Distributed Database PolarDB- | X |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Vips | - | - | The list of returned virtual IP addresses (VIPs). |
| Vip | - | - | The details about a VIP. |
| IP | String | 10.xx.xx.51 | The IP address. |
| Port | String | 3306 | The open port of the VIP. |
| Type | String | intranet | The type of the VIP. Valid values: intranet internet |
| VpcId | String | vpc-bpxxxxxxxxxxxy | The ID of the VPC network connected to the instance. |
| VswitchId | String | vsw-bpxxxxxxxxxxxxx96 | The ID of the virtual switch (VSwitch). |
| VpcCloudInstanceId | String | drdsxxxxxxxxxx | The ID of the instance in the VPC cluster. |
| VpcId | String | vpc-bpxxxxxxxxxxxy | The ID of the VPC network connected to the instance. |
| ZoneId | String | vsw-bpxxxxxxxxxxxxx96 | The ID of the VSwitch. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 20 | The number of entries returned on the page. |
| RequestId | String | 2F7F8080-9132-4279- 85D0-B7E5C4305162 | The ID of the request. |
| Total | Integer | 1 | The total number of PolarDB-X instances. |

```
http(s)://[Endpoint]/? Action=DescribeDrdsInstances &RegionId=cn-hangzhou
```

```xml
<DescribeDrdsInstances>
      <Instances>
            <Instance>
                  <Status>RUN</Status>
                  <Description>drds_test</Description>
                  <InstanceSpec>drds.sn2.4c16g.8C32G</InstanceSpec>
                  <ZoneId>cn-hangzhou-e</ZoneId>
                  <ExpireDate>4724323200000</ExpireDate>
                  <CreateTime>1568620311000</CreateTime>
                  <MachineType>ecs</MachineType>
                  <Label>NORMAL</Label>
                  <InstanceSeries>drds.sn2.4c16g</InstanceSeries>
                  <VersionAction>Upgradable</VersionAction>
                  <Type>PRIVATE</Type>
                  <VpcId></VpcId>
                  <DrdsInstanceId>drdsxxxxxxxxxx</DrdsInstanceId>
                  <OrderInstanceId>drdsxxxxxxxxxx</OrderInstanceId>
                  <InstRole>MASTER</InstRole>
                  <NetworkType>CLASSIC</NetworkType>
                  <CommodityCode>drdsPost</CommodityCode>
                  <RegionId>cn-hangzhou</RegionId>
                  <Vips></Vips>
            </Instance>
      </Instances>
      <PageSize>20</PageSize>
      <RequestId>8734773E-7B21-4A22-9106-CBD245F8AF7D</RequestId>
      <PageNumber>1</PageNumber>
      <Total>1</Total>
</DescribeDrdsInstances>
```

JSON format `{`

```json
    "PageNumber":1,
    "PageSize":20,
    "RequestId":"8734773E-7B21-4A22-9106-CBD245F8AF7D",
    "Instances":{
        "Instance":[
```

`{`

```json
                "MachineType":"ecs",
                "Description":"drds_test",
                "OrderInstanceId":"drdsxxxxxxxxxx",
                "Type":"PRIVATE",
                "ZoneId":"cn-hangzhou-e",
                "VpcId":"",
                "InstRole":"MASTER",
                "NetworkType":"CLASSIC",
                "Status":"RUN",
                "ExpireDate":4724323200000,
                "Vips":{
                    "Vip":[]
```

`},`

```json
                "VersionAction":"Upgradable",
                "RegionId":"cn-hangzhou",
                "CommodityCode":"drdsPost",
                "InstanceSpec":"drds.sn2.4c16g.8C32G",
                "CreateTime":1568620311000,
                "InstanceSeries":"drds.sn2.4c16g",
                "Label":"NORMAL",
                "DrdsInstanceId":"drdsxxxxxxxxxx"
```

`]` `},`

```json
    "Total":1
```

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | ActionUnauthorized | The specified action is not available for you | The error message returned because you are not authorized to perform this action. Perform RAM authorization first. |

#### 2.3.7 DescribeDrdsInstanceVersion

Queries the versions of a PolarDB-X 1.0 instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDrdsInsta nceVersion | The operation that you want to perform. Set the value to DescribeDrdsInsta nceVersion. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | ASU6xxxxxxxxxxxx xxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | - | - | The version data of the PolarDB-X 1.0 instance. |
| InstanceVersion | String | 5.3.12-15682777 | The current version of the PolarDB-X instance. |
| NewestVersion | String | 5.3.12-15682777 | The latest version of the PolarDB-X instance. |
| RequestId | String | 2F7F8080-9132-4279- 85D0-B7E5C4305162 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```
http(s)://[Endpoint]/? Action=DescribeDrdsInstanceVersion &DrdsInstanceId=drdsxxxxxxxxxx
```

```xml
<DescribeDrdsInstanceVersion>
      <RequestId>88AFEF28-DF04-4E21-9CE9-277D3C19E3CD</RequestId>
      <Data>
            <InstanceVersion>5.3.12-15682777</InstanceVersion>
            <NewestVersion>5.3.12-15682777</NewestVersion>
      </Data>
</DescribeDrdsInstanceVersion>
```

JSON format `{`

```json
    "Data":{
        "InstanceVersion":"5.3.12-15682777",
        "NewestVersion":"5.3.12-15682777"
```

`},`

```json
    "RequestId":"88AFEF28-DF04-4E21-9CE9-277D3C19E3CD",
    "Success":true
```

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | ActionUnauthorized | The specified action is not available for you | The error message returned because you are not authorized to perform this action. Perform RAM authorization first. |

#### 2.3.8 DescribeDrdsParams

Queries the parameters of a PolarDB-X 1.0 instance or database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDrdsPara ms | The operation that you want to perform. Set the value to DescribeDrdsPara ms. |
| DrdsInstanceId | String | Yes | DescribeDrdsPara ms | The ID of the PolarDB-X 1.0 instance. |

| C P | loud Native Distribute olarDB-X | d Database |   | Develop | er Guide·API referenc | e |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ParamLevel | String | Yes | INSTANCE | The parameter level. Valid values: INSTANCE: the instance level. DB: the database level. |
| DbName | String | No | drds test _ | The name of the PolarDB-X 1.0 database. |
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| List | - | - | The details about the parameters that were queried. |
| DbName | String | drds test _ | The name of the PolarDB-X 1.0 database. |
| NeedRestart | Boolean | true | Indicates whether to restart the database. |
| ParamDefaultValue | String | 1000 | The default value of the parameter. |
| ParamDesc | String | The slow SQL query threshold (unit: ms) | The description of the parameter. |
| ParamEnglishName | String | SLOW SQL TIME _ _ | The English name of the parameter. |
| ParamLevel | String | INSTANCE | The parameter level. |
| ParamName | String | SLOW SQL TIME _ _ | The name of the parameter. |
| ParamRanges | String | [1000-900000] | The value range of the parameter. |
| ParamType | String | CONFIG | The type of the parameter. |
| ParamValue | String | 1000 | The value of the parameter. |

| Developer Guide·API refere | nce | Cloud N | ative Distributed Database PolarDB- |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ParamVariableName | String | slowSqlTime | The name of the parameter variable. |
| RequestId | String | 2F7F8080-9132-4279- 85D0-B7E5C4305162 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=DescribeDrdsParams &DrdsInstanceId=DescribeDrdsParams &ParamLevel=INSTANCE <DescribeDrdsParams>
      <RequestId>29D7422F-24DD-42D8-A04E-EBCE4B4A416A</RequestId>
      <List>
            <ParamLevel>INSTANCE</ParamLevel>
            <ParamRanges>[1000-900000]</ParamRanges>
            <ParamVariableName>slowSqlTime</ParamVariableName>
            <ParamEnglishName>SLOW_SQL_TIME</ParamEnglishName>
            <NeedRestart>false</NeedRestart>
            <ParamValue>1000</ParamValue>
            <ParamDefaultValue>1000</ParamDefaultValue>
            <DbName></DbName>
            <UserVisible>true</UserVisible>
            <ParamName>SLOW_SQL_TIME</ParamName>
            <ParamType>CONFIG</ParamType>
            <ParamDesc>The slow SQL query threshold (unit: ms)</ParamDesc>
      </List>
      <List>
            <ParamLevel>INSTANCE</ParamLevel>
            <ParamRanges>[3600000-86400000]</ParamRanges>
            <ParamVariableName>idleTimeout</ParamVariableName>
            <ParamEnglishName>LOGIC_IDLE_TIMEOUT</ParamEnglishName>
            <NeedRestart>false</NeedRestart>
            <ParamValue>28800000</ParamValue>
            <ParamDefaultValue>28800000</ParamDefaultValue>
            <DbName></DbName>
            <UserVisible>true</UserVisible>
            <ParamName>LOGIC_IDLE_TIMEOUT</ParamName>
            <ParamType>CONFIG</ParamType>
            <ParamDesc>The idle timeout for the connection between applications and PolarDB
-X 1.0 (unit: ms)</ParamDesc>
```

```xml
      </List>
      <List>
            <ParamLevel>INSTANCE</ParamLevel>
            <ParamRanges>[4194304-33554432]</ParamRanges>
            <ParamVariableName>maxAllowedPacket</ParamVariableName>
            <ParamEnglishName>MAX_ALLOWED_PACKET</ParamEnglishName>
            <NeedRestart>false</NeedRestart>
            <ParamValue>16777216</ParamValue>
            <ParamDefaultValue>16777216</ParamDefaultValue>
            <DbName></DbName>
            <UserVisible>true</UserVisible>
            <ParamName>MAX_ALLOWED_PACKET</ParamName>
            <ParamType>CONFIG</ParamType>
            <ParamDesc>The maximum network packet for the interaction between applications
and PolarDB-X 1.0 (unit: byte).</ParamDesc>
      </List>
      <List>
            <ParamLevel>INSTANCE</ParamLevel>
            <ParamRanges>[1073741824-6442450944]</ParamRanges>
            <ParamVariableName>GLOBAL_MEMORY_LIMIT</ParamVariableName>
            <ParamEnglishName>GLOBAL_MEMORY_LIMIT</ParamEnglishName>
            <NeedRestart>false</NeedRestart>
            <ParamValue>2147483648</ParamValue>
            <ParamDefaultValue>2147483648</ParamDefaultValue>
            <DbName></DbName>
            <UserVisible>true</UserVisible>
            <ParamName>GLOBAL_MEMORY_LIMIT</ParamName>
            <ParamType>CONFIG</ParamType>
            <ParamDesc>The maximum size of the memory pool for a read-only instance. If the
memory usage on an instance exceeds the value, an error occurs and the query fails.</ParamD esc>
      </List>
</DescribeDrdsParams>
```

JSON format `{`

```json
    "RequestId":"29D7422F-24DD-42D8-A04E-EBCE4B4A416A",
    "Success":true,
    "List":[
```

`{`

```json
            "NeedRestart":false,
            "ParamEnglishName":"SLOW_SQL_TIME",
            "ParamDesc":"The slow SQL query threshold (unit: ms).",
            "ParamName":"SLOW_SQL_TIME",
            "DbName":"",
            "ParamValue":"1000",
            "ParamType":"CONFIG",
            "ParamLevel":"INSTANCE",
            "UserVisible":true,
            "ParamDefaultValue":"1000",
            "ParamVariableName":"slowSqlTime",
"ParamRanges":"[1000-900000]"
```

`a``a`

```
ages:[000900000]
```

`},` `{`

```json
            "NeedRestart":false,
            "ParamEnglishName":"LOGIC_IDLE_TIMEOUT",
            "ParamDesc":"The idle timeout for the connection between users and PolarDB-X 1.
0 (unit: ms).",
            "ParamName":"LOGIC_IDLE_TIMEOUT",
            "DbName":"",
            "ParamValue":"28800000",
            "ParamType":"CONFIG",
            "ParamLevel":"INSTANCE",
            "UserVisible":true,
            "ParamDefaultValue":"28800000",
            "ParamVariableName":"idleTimeout",
            "ParamRanges":"[3600000-86400000]"
```

`},` `{`

```json
            "NeedRestart":false,
            "ParamEnglishName":"MAX_ALLOWED_PACKET",
            "ParamDesc":"The maximum network packet for the interaction between users and P
olarDB-X 1.0 (unit: byte).",
            "ParamName":"MAX_ALLOWED_PACKET",
            "DbName":"",
            "ParamValue":"16777216",
            "ParamType":"CONFIG",
            "ParamLevel":"INSTANCE",
            "UserVisible":true,
            "ParamDefaultValue":"16777216",
            "ParamVariableName":"maxAllowedPacket",
            "ParamRanges":"[4194304-33554432]"
```

`},` `{`

```json
            "NeedRestart":false,
            "ParamEnglishName":"GLOBAL_MEMORY_LIMIT",
            "ParamDesc":"The maximum size of the memory pool for a read-only instance. If t
he memory usage on an instance exceeds the value, an error occurs and the query fails.",
            "ParamName":"GLOBAL_MEMORY_LIMIT",
            "DbName":"",
            "ParamValue":"2147483648",
            "ParamType":"CONFIG",
            "ParamLevel":"INSTANCE",
            "UserVisible":true,
            "ParamDefaultValue":"2147483648",
            "ParamVariableName":"GLOBAL_MEMORY_LIMIT",
            "ParamRanges":"[1073741824-6442450944]"
```

`]`

#### 2.3.9 DescribeDrdsTasks

Queries the change tasks of a PolarDB-X instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDrdsTasks | The operation that you want to perform. Set the value to DescribeDrdsTasks . |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | test | The AccessKey ID provided to you by Alibaba Cloud. |
| DbName | String | No | test | The name of the PolarDB-X database. |
| TaskType | String | No | test | The type of the task. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CD412DF7-F21D-44CE- 88FF-ED24917174A8 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |
| Tasks | - | - | The list of returned tasks. |
| Task | - | - | The details about a task. |
| Content | String | upgrade instance _ | The content of the task. |
| Id | Long | 64148 | The ID of the task. |
| State | String | FAILED | The status of the task. |

```xml
http(s)://[Endpoint]/? Action=DescribeDrdsTasks <DescribeDrdsTasksResponse>
      <RequestId>CD412DF7-F21D-44CE-88FF-ED24917174A8</RequestId>
      <Tasks>
            <Task>
                  <State>FAILED</State>
                  <Id>64148</Id>
                  <Content>upgrade_instance</Content>
            </Task>
      </Tasks>
</DescribeDrdsTasksResponse>
```

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | ActionUnauthorized | The specified action is not available for you | The error message returned because you are not authorized to perform this action. Perform RAM authorization first. |

#### 2.3.10 DescribeHiStoreInstanceInfo

Queries the details about a HiStore instance of a PolarDB-X instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeHiStoreIns tanceInfo | The operation that you want to perform. Set the value to DescribeHiStoreIns tanceInfo. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |

| loud Native Distribute | d Database |   |   |   |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HistoreInstanceId | String | Yes | hi-hbxxxxxxxxxxx | The ID of the HiStore instance. |
| AccessKeyId | String | No | test | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| HiStoreInstanceInfo | - | - | The details about the HiStore instance. |
| RequestId | String | 509BDE17-505A-4B3B- 854D-30D3F092502F | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=DescribeHiStoreInstanceInfo <DescribeHiStoreInstanceInfoResponse>
      <RequestId>509BDE17-505A-4B3B-854D-30D3F092502F</RequestId>
          <HiStoreInstanceInfo>
                <DiskSize>100</DiskSize>
                <GmtCreate>1568267711</GmtCreate>
                <HistoreInstanceId>test</HistoreInstanceId>
                <MachineSpec>4C8G</MachineSpec>
                <RpmVersion>1.0.15</RpmVersion>
          </HiStoreInstanceInfo>
</DescribeHiStoreInstanceInfoResponse>
```

#### 2.3.11 DescribeInstanceAccounts

Queries the account information of a PolarDB-X instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeInstanceA ccounts | The operation that you want to perform. Set the value to DescribeInstanceA ccounts. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxxx xxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | ABCxxxxxxxxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| InstanceAccounts | - | - | The returned list of instance accounts. |
| InstanceAccount | - | - | The details about an instance account. |
| AccountName | String | drdsuser | The name of the account. |
| AccountType | Integer | 1 | The type of the account. |
| DbPrivileges | - | - | The database permissions that the account has. |
| DbPrivilege | - | - | The details about the database permission. |
| DbName | String | drdsdb | The name of the database. |
| Privilege | String | root | The permission. |
| Description | String | Permission | The description of the permission. |
| Host | String | % | The IP address of the instance. |

| loud Native Distributed Da | tabase | De | veloper Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 2D77B55F-50C4-4FC5- A89A-7746B7D5781D | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=DescribeInstanceAccounts <DescribeInstanceAccountsResponse>
      <InstanceAccounts>
            <InstanceAccount>
                  <Description>Created by DRDS</Description>
                  <DbPrivileges>
                        <DbPrivilege>
                              <DbName>drdsdb</DbName>
                              <Privilege>ROOT</Privilege>
                        </DbPrivilege>
                  </DbPrivileges>
                  <Host>%</Host>
                  <AccountName>drdsuser</AccountName>
                  <AccountType>0</AccountType>
            </InstanceAccount>
      </InstanceAccounts>
      <RequestId>2D77B55F-50C4-4FC5-A89A-7746B7D5781D</RequestId>
</DescribeInstanceAccountsResponse>
```

| HttpCode | Error codes | Error message | Description |
|---|---|---|---|
| 400 | ActionUnauthorized | The specified action is not available for you | The error message returned because you are not authorized to perform this action. Perform RAM authorization first. |

#### 2.3.12 DescribeInstanceMenuSwitch

Queries the switch configuration of a PolarDB-X instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeInstanceM enuSwitch | The operation that you want to perform. Set the value to DescribeInstanceM enuSwitch. |

```xml
http(s)://[Endpoint]/? Action=DescribeInstanceMenuSwitch <DescribeInstanceMenuSwitchResponse>
      <RequestId>DSSDF-SEWE-23ERW</RequestId>
      <Config>Config</Config>
</DescribeInstanceMenuSwitchResponse>
```

#### 2.3.13 DescribeInstDbSlsInfo

Queries the names of the Log Service project and Logstore used by SQL audit.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeInstDbSlsI nfo | The operation that you want to perform. Set the value to DescribeInstDbSlsI nfo. |
| DbName | String | Yes | drdsdb | The name of the PolarDB-X database. |

| loud Native Distribute olarDB-X | d Database |   | Develop | er Guide·API referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | test | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AuditInfo | - | - | The SQL audit details. |
| LogStore | String | test1 | The Logstore used by SQL audit. |
| Project | String | test2 | The Log Service project used by SQL audit. |
| RequestId | String | DC3ABA3E-0F8A-4596- 9104-F5155C34315B | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=DescribeInstDbSlsInfo <DescribeInstDbSlsInfoResponse>
      <AuditInfo>
            <LogStore>test</LogStore>
            <Project>test2</Project>
      </AuditInfo>
      <RequestId>DC3ABA3E-0F8A-4596-9104-F5155C34315B</RequestId>
</DescribeInstDbSlsInfoResponse>
```

#### 2.3.14 DescribePreCheckResult

Queries precheck results of a PolarDB-X instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePreCheckR esult | The operation that you want to perform. Set the value to DescribePreCheckR esult. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxx | The ID of the PolarDB-X 1.0instance. |
| TaskId | String | Yes | 4561 | The ID of the precheck task. |
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PreCheckResult | - | - | The precheck result. |
| PreCheckName | String | Does a unique key exist | The name of the precheck task. |
| State | String | FAIL | The status of the precheck task. |
| SubCheckItems | - | - | The details about a precheck item. |
| ErrorMsgCode | String | 1004 | The error code. |
| ErrorMsgParams | - | table1 | The error parameter. |
| PreCheckItemName | String | Unique key | The name of the precheck item. |
| State | String | SUCCESS | The status of the precheck item. |
| RequestId | String | DSSDF-SEWE-23ERW | The ID of the request. |

| loud Native Distributed Da olarDB-X | tabase | De | veloper Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=DescribePreCheckResult <DescribePreCheckResultResponse>
      <RequestId>DSSDF-SEWE-23ERW</RequestId>
      <PreCheckResult>
        <PreCheckName>Whether a unique key exists</PreCheckName>
        <State>FAIL</State>
        <SubCheckItems>
              <ErrorMsgCode>1004</ErrorMsgCode>
              <ErrorMsgParams>table1</ErrorMsgParams>
              <PreCheckItemName>Shard key</PreCheckItemName>
              <State>SUCCESS</State>
        </SubCheckItems>
      </PreCheckResult>
      <PreCheckResult></PreCheckResult>
</DescribePreCheckResultResponse>
```

#### 2.3.15 DescribeStorageInstanceSubDbInfo

Queries the details about a storage instance of a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeStorageIn stanceSubDbInfo | The operation that you want to perform. Set the value to DescribeStorageIn stanceSubDbInfo. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DbName | String | Yes | drds flashback _ | The name of the PolarDB-X database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| InstanceId | String | Yes | rm- bp1xxxxxxxxxxxxxx x | The ID of the storage instance, namely, ApsaraDB RDS for MySQL instance. |
| AccessKeyId | String | No | ****** | The AccessKey ID provided to you by Alibaba Cloud. |
| InstType | String | No | null | The type of the instance. This parameter is currently unavailable. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | - | - | The returned data object. |
| Capacity | Long | 194560 | The capacity of the ApsaraDB RDS for MySQL instance. |
| RdsInstanceId | String | rm-bp1xxxxxxxxxxxxxxx | The ID of the ApsaraDB RDS for MySQL instance. |
| SubDbList | - | - | The returned list of database shards. |
| SubDb | - | - | The details about a database shard. |
| SubDbName | String | drds flashback b8cd 0 _ _ _ 005 | The name of the database shard. |
| Use | Long | 0 | Indicates whether the database shard was in use. |
| WarningLevel | Integer | 0 | The alert level. |

| olarDB-X |   | De | veloper Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| TipsType | Integer | 0 | The type of the tip. |
| Use | Long | 2293 | The usage of the database shard. |
| WarningLevel | Integer | 0 | The alert level. |
| RequestId | String | 78BA6289-5E03-4A31- 8CB8-FC298DB63184 | The unique ID of the request. If any problem occurs, provide this request ID for troubleshooting. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=DescribeStorageInstanceSubDbInfo <DescribeStorageInstanceSubDbInfoResponse>
      <code>200</code>
      <data>
            <RequestId>78BA6289-5E03-4A31-8CB8-FC298DB63184</RequestId>
            <Data>
                  <SubDbList>
                        <SubDb>
                              <WarningLevel>0</WarningLevel>
                              <Use>0</Use>
                              <SubDbName>drds_flashback_b8cd_0005</SubDbName>
                        </SubDb>
                        <SubDb>
                              <WarningLevel>0</WarningLevel>
                              <Use>0</Use>
                              <SubDbName>drds_flashback_b8cd_0004</SubDbName>
                        </SubDb>
                        <SubDb>
                              <WarningLevel>0</WarningLevel>
                              <Use>0</Use>
                              <SubDbName>drds_flashback_b8cd_0003</SubDbName>
                        </SubDb>
                        <SubDb>
                              <WarningLevel>0</WarningLevel>
                              <Use>0</Use>
                              <SubDbName>drds_flashback_b8cd_0002</SubDbName>
```

```xml
                        </SubDb>
                        <SubDb>
                              <WarningLevel>0</WarningLevel>
                              <Use>0</Use>
                              <SubDbName>drds_flashback_b8cd_0007</SubDbName>
                        </SubDb>
                        <SubDb>
                              <WarningLevel>0</WarningLevel>
                              <Use>0</Use>
                              <SubDbName>drds_flashback_b8cd_0006</SubDbName>
                        </SubDb>
                        <SubDb>
                              <WarningLevel>0</WarningLevel>
                              <Use>0</Use>
                              <SubDbName>drds_flashback_b8cd_0001</SubDbName>
                        </SubDb>
                        <SubDb>
                              <WarningLevel>0</WarningLevel>
                              <Use>0</Use>
                              <SubDbName>drds_flashback_b8cd_0000</SubDbName>
                        </SubDb>
                        <SubDb>
                              <WarningLevel>3</WarningLevel>
                              <Use>2293</Use>
                              <SubDbName>other data</SubDbName>
                        </SubDb>
                  </SubDbList>
                  <WarningLevel>0</WarningLevel>
                  <Capacity>194560</Capacity>
                  <Use>2293</Use>
                  <TipsType>0</TipsType>
                  <RdsInstanceId>rm-bp1xxxxxxxxxxxxxxx</RdsInstanceId>
            </Data>
      </data>
      <requestId>78BA6289-5E03-4A31-8CB8-FC298DB63184</requestId>
      <successResponse>true</successResponse>
</DescribeStorageInstanceSubDbInfoResponse>
```

JSON format `{`

```json
    "successResponse":true,
    "requestId":"78BA6289-5E03-4A31-8CB8-FC298DB63184",
    "data":{
        "Data":{
            "WarningLevel":0,
            "TipsType":0,
            "RdsInstanceId":"rm-bp1xxxxxxxxxxxxxxx",
            "SubDbList":{
                "SubDb":[
```

`{`

```json
                        "WarningLevel":0,
                        "SubDbName":"drds_flashback_b8cd_0005",
```

```json
                        "Use":0
```

`},` `{`

```json
                        "WarningLevel":0,
                        "SubDbName":"drds_flashback_b8cd_0004",
                        "Use":0
```

`},` `{`

```json
                        "WarningLevel":0,
                        "SubDbName":"drds_flashback_b8cd_0003",
                        "Use":0
```

`},` `{`

```json
                        "WarningLevel":0,
                        "SubDbName":"drds_flashback_b8cd_0002",
                        "Use":0
```

`},` `{`

```json
                        "WarningLevel":0,
                        "SubDbName":"drds_flashback_b8cd_0007",
                        "Use":0
```

`},` `{`

```json
                        "WarningLevel":0,
                        "SubDbName":"drds_flashback_b8cd_0006",
                        "Use":0
```

`},` `{`

```json
                        "WarningLevel":0,
                        "SubDbName":"drds_flashback_b8cd_0001",
                        "Use":0
```

`},` `{`

```json
                        "WarningLevel":0,
                        "SubDbName":"drds_flashback_b8cd_0000",
                        "Use":0
```

`},` `{`

```json
                        "WarningLevel":3,
                        "SubDbName":"other data",
                        "Use":2293
```

`]` `},`

```json
            "Capacity":194560,
            "Use":2293
```

`},`

```json
        "RequestId":"78BA6289-5E03-4A31-8CB8-FC298DB63184",
        "Success":true
```

`},`

```json
    "code":"200"
```

#### 2.3.16 EnableSqlAudit

Enables SQL audit for a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | EnableSqlAudit | The operation that you want to perform. Set the value to EnableSqlAudit. |
| DbName | String | Yes | tpch 50g 4c32gx4 _ _ | The name of the PolarDB-X database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | 2zAEvxxxxxxxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |
| IsRecall | Boolean | No | true | Specifies whether to backtrack historical SQL statements for auditing. |
| RecallEndTimesta mp | String | No | 1568875132000 | The end time of the backtracking. |
| RecallStartTimest amp | String | No | 1568875132000 | The start time of the backtracking. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 463A5F0F-12AD-4544- A902-B2B983CD2C11 | The ID of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Result | Boolean | true | Indicates whether SQL audit was enabled for the database. Valid values: true: enabled. false: failed. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=EnableSqlAudit &DbName=tpch_50g_4c32gx4 &DrdsInstanceId=drdsxxxxxxxxxxxx <EnableSqlAuditResponse>
      <Result>true</Result>
      <RequestId>463A5F0F-12AD-4544-A902-B2B983CD2C11</RequestId>
</EnableSqlAuditResponse>
```

JSON format `{`

```json
    "Result":true,
    "RequestId":"463A5F0F-12AD-4544-A902-B2B983CD2C11",
    "Success":true
```

#### 2.3.17 EnableSqlFlashbackMatchSwitch

Enables SQL flashback matching. After it is enabled, the query information is added to the ApsaraDB RDS for MySQL binary logs that are used by the PolarDB-X 1.0 database to precisely restore data.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | EnableSqlFlashbac kMatchSwitch | The operation that you want to perform. Set the value to EnableSqlFlashbac kMatchSwitch. |
| DbName | String | Yes | testdb | The name of the PolarDB-X database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxxx | The ID of the PolarDB-X instance. |
| AccessKeyId | String | No | 2zAEvsxxxxxxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 463A5F0F-12AD-4544- A902-B2B983CD2C11 | The ID of the request. |
| Result | Boolean | true | Indicates whether SQL flashback matching was enabled for the database. Valid values: true: enabled. false: failed. |
| Success | Boolean | true | Indicates whether the request was successful. |

```
http(s)://[Endpoint]/? Action=EnableSqlFlashbackMatchSwitch &DbName=testdb &DrdsInstanceId=drdsxxxxxxxxxxxxx
```

```xml
<EnableSqlFlashbackMatchSwitchResponse>
      <Result>true</Result>
      <RequestId>463A5F0F-12AD-4544-A902-B2B983CD2C11</RequestId>
</EnableSqlFlashbackMatchSwitchResponse>
```

JSON format `{`

```json
    "Result":true,
    "RequestId":"463A5F0F-12AD-4544-A902-B2B983CD2C11",
    "Success":true
```

#### 2.3.18 FlashbackRecycleBinTable

Restores a logical table in the recycle bin.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | FlashbackRecycleB inTable | The operation that you want to perform. Set the value to FlashbackRecycleB inTable. |
| DbName | String | Yes | testdb | The name of the database where the target table is located. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxxx x | The ID of the PolarDB-X instance where the target table is located. |
| TableName | String | Yes | test | The name of the logical table to be restored. |
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Boolean | true | Indicates whether the restoration was enabled. Valid values: true: enabled. false: failed. |
| RequestId | String | 463A5F0F-12AD-4544- A902-B2B983CD2C11 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=FlashbackRecycleBinTable &DbName=testdb &DrdsInstanceId=drdsxxxxxxxxxxxxxx &TableName=test <FlashbackRecycleBinTableResponse>
      <Result>true</Result>
      <RequestId>463A5F0F-12AD-4544-A902-B2B983CD2C11</RequestId>
</FlashbackRecycleBinTableResponse>
```

JSON format `{`

```json
    "Result":true,
    "RequestId":"463A5F0F-12AD-4544-A902-B2B983CD2C11",
    "Success":true
```

#### 2.3.19 ModifyAccountDescription

Modifies the account description of a PolarDB-X instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AccountName | String | Yes | testuser | The name of the account. |
| Action | String | Yes | ModifyAccountDes cription | The operation that you want to perform. Set the value to ModifyAccountDes cription. |
| Description | String | Yes | Created by PolarDB-X 1.0 | The description of the account. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxx | The ID of the PolarDB-X instance. |
| AccessKeyId | String | No | 2zAEvxxxxxxxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 2F93CCD5-806F-4470- BBC7-20476AC48DC6 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=ModifyAccountDescription &AccountName=testuser &Description=Created by PolarDB-X 1.0 &DrdsInstanceId=drdsxxxxxxxxxxxx <ModifyAccountDescriptionResponse>
      <RequestId>2F93CCD5-806F-4470-BBC7-20476AC48DC6</RequestId>
</ModifyAccountDescriptionResponse>
```

JSON format `{`

```json
    "RequestId":"2F93CCD5-806F-4470-BBC7-20476AC48DC6",
    "Success":true
```

#### 2.3.20 ModifyDrdsInstanceDescription

Modifies the description of a PolarDB-X instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDrdsInstanc eDescription | The operation that you want to perform. Set the value to ModifyDrdsInstanc eDescription. |
| Description | String | Yes | Long occupied | The description of the PolarDB-X instance. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | 2zAEvsxxxxxxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C44CA24C-C7C4-4C0F- 8AC9-1343F279B09C | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=ModifyDrdsInstanceDescription &Description=Long occupied &DrdsInstanceId=drdsxxxxxxxxxxxxx <ModifyDrdsInstanceDescriptionResponse>
      <RequestId>C44CA24C-C7C4-4C0F-8AC9-1343F279B09C</RequestId>
</ModifyDrdsInstanceDescriptionResponse>
```

JSON format `{`

```json
    "RequestId":"C44CA24C-C7C4-4C0F-8AC9-1343F279B09C",
    "Success":true
```

#### 2.3.21 RemoveDrdsInstance

Releases a PolarDB-X 1.0 instance. Not e You cannot release a PolarDB-X instance that is changing configuration or has associated databases.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RemoveDrdsInstan ce | The operation that you want to perform. Set the value to RemoveDrdsInstan ce. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | f32safdxxxxxxxxxx xxxx | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6F70CE62-5077-4B7B- 95BC-4DAC45614DBE | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=RemoveDrdsInstance &DrdsInstanceId=drdsxxxxxxxxxxxxx <RemoveDrdsInstanceResponse>
      <RequestId>A3140FC7-B78B-4D8E-B0C8-926D28669934</RequestId>
</RemoveDrdsInstanceResponse>
```

JSON format `{`

```json
    "RequestId":"A3140FC7-B78B-4D8E-B0C8-926D28669934",
    "Success":true
```

#### 2.3.22 RemoveInstanceAccount

Deletes the instance management account of a PolarDB-X instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AccountName | String | Yes | testaccount | The name of the account. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RemoveInstanceAc count | The operation that you want to perform. Set the value to RemoveInstanceAc count. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | f3d13xxxxxxxxxxxx xxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6F70CE62-5077-4B7B- 95BC-4DAC45614DBE | The ID of the request. |
| Success | Boolean | true | Indicates whether the instance management account was deleted. |

```xml
http(s)://[Endpoint]/? Action=RemoveInstanceAccount &AccountName=testaccount &DrdsInstanceId=drdsxxxxxxxxxxxxx <RemoveInstanceAccountResponse>
      <RequestId>A3140FC7-B78B-4D8E-B0C8-926D28669934</RequestId>
</RemoveInstanceAccountResponse>
```

JSON format `{`

```json
    "RequestId":"A3140FC7-B78B-4D8E-B0C8-926D28669934",
    "Success":true
```

#### 2.3.23 RestartDrdsInstance

Restarts a PolarDB-X instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RestartDrdsInstan ce | The operation that you want to perform. Set the value to RestartDrdsInstan ce. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | fds14xxxxxxxxxxxx xx | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6F70CE62-5077-4B7B- 95BC-4DAC45614DBE | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |
| TaskId | Long | 1 | The ID of the task. |

```
http(s)://[Endpoint]/? Action=RestartDrdsInstance &DrdsInstanceId=drdsxxxxxxxxxxxxx
```

```xml
<RestartDrdsInstanceResponse>
      <RequestId>A3140FC7-B78B-4D8E-B0C8-926D28669934</RequestId>
      <TaskId>1</TaskId>
</RestartDrdsInstanceResponse>
```

JSON format `{`

```json
    "RequestId":"A3140FC7-B78B-4D8E-B0C8-926D28669934",
    "TaskId":1,
    "Success":true
```

#### 2.3.24 RollbackInstanceVersion

Rolls back the version of a PolarDB-X 1.0 instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RollbackInstanceV ersion | The operation that you want to perform. Set the value to RollbackInstanceV ersion. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | true | Indicates whether the request was successful. |
| RequestId | String | DSSDF-SEWE-23ERW | The ID of the request. |

```xml
http(s)://[Endpoint]/? Action=RollbackInstanceVersion &DrdsInstanceId=drdsxxxxxxxxxxx <RollbackInstanceVersionResponse>
      <RequestId>DSSDF-SEWE-23ERW</RequestId>
      <Data>True</Data>
</RollbackInstanceVersionResponse>
```

JSON format `{`

```json
    "Data":"true",
    "RequestId":"DSSDF-SEWE-23ERW"
```

#### 2.3.25 SetBackupPolicy

Configures a backup policy for a PolarDB-X instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetBackupPolicy | The operation that you want to perform. Set the value to SetBackupPolicy. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | fafdsxxxxxxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |
| BackupDbNames | String | No | db test1,db test2 _ _ | The name of the database involved in the backup. |

| loud Native Distribute | d Database |   |   |   |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| BackupLevel | String | No | db | The level of the backup. Valid values: db: the database level. instance: the instance level. |
| BackupLog | String | No | 1 | Specifies whether the backup log function is enabled. Valid values: 1: enabled. 0: disabled. |
| BackupMode | String | No | phy | The mode of the backup. Valid values: logic: the logical backup. phy: the physical backup. |
| DataBackupRetenti onPeriod | String | No | 1 | The retention period of the data backup. Unit: days. |
| LogBackupRetenti onPeriod | String | No | 1 | The retention period of the data backup. Unit: days. |
| PreferredBackupEn dTime | String | No | 12:30:30 | The end time of the backup. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PreferredBackupPe riod | String | No | 0 | The backup period. Valid values: 0: Monday. 1: Tuesday. 2: Wednesday. 3: Thursday. 4: Friday. 5: Saturday. 6: Sunday. |
| PreferredBackupSt artTime | String | No | 11:30:30 | The start time of the backup. |

```xml
http(s)://[Endpoint]/? Action=SetBackupPolicy &DrdsInstanceId=drdsxxxxxxxxxxx <SetBackupPolicyResponse>
        <RequestId>A3140FC7-B78B-4D8E-B0C8-926D28669934</RequestId>
        <Result>success</Result>
</SetBackupPolicyResponse>
```

JSON format `{`

```json
    "Result":"success",
    "RequestId":"A3140FC7-B78B-4D8E-B0C8-926D28669934",
    "Success":true
```

#### 2.3.26 SetupDrdsParams

Configures parameters for a PolarDB-X 1.0 instance or database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetupDrdsParams | The operation that you want to perform. Set the value to SetupDrdsParams. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| ParamLevel | String | Yes | DB | The parameter level. Valid values: INSTANCE: the instance level. DB: the database level. |
| Data.N.DbName | String | No | test db _ | The name of the database corresponding to the parameter. The database name is valid only for database-level parameters. |
| Data.N.ParamRang es | String | No | [true\|false] | The valid values of the parameter. |
| Data.N.ParamType | String | No | ATOM | The type of the parameter. Valid values: ATOM: the configuration item in the layer-3 data source. CONFIG: the configuration item in ConfigServer. DIAMOND: the configuration item in Diamond. |
| Data.N.ParamValu e | String | No | true | The value of the parameter. |

| Developer Guide·API re | ference |   | Cloud Native | Distributed Database PolarDB- |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Data.N.ParamVaria bleName | String | No | FORBID EXECUTE D _ _ ML ALL _ | The name of the variable, which is specific to the program. |
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |

```xml
http(s)://[Endpoint]/? Action=SetupDrdsParams &DrdsInstanceId=drdsxxxxxxxxxxx &ParamLevel=DB <SetupDrdsParamsResponse>
        <RequestId>A3140FC7-B78B-4D8E-B0C8-926D28669934</RequestId>
        <Data>true</Data>
</SetupDrdsParamsResponse>
```

JSON format `{`

```json
    "Data":true,
    "RequestId":"A3140FC7-B78B-4D8E-B0C8-926D28669934",
    "Success":true
```

#### 2.3.27 SubmitRollbackTask

Submits a smooth scale-out rollback task for a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SubmitRollbackTa sk | The operation that you want to perform. Set the value to SubmitRollbackTa sk. |
| DbName | String | Yes | test | The name of the PolarDB-X 1.0 database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| ExpandType | String | Yes | smooth expand _ | The scale-out type. Valid values: smooth expan _ d: smooth scale-out. hot expand: _ hot-spot scale- out Not e The hot-spot scale-out is not supported. |
| JobId | String | Yes | 123 | The job ID of the smooth scale-out task. The value of this parameter is the same as that of the ParentJobId parameter. |
| ParentJobId | String | Yes | 123 | The parent job ID of the smooth scale-out task. The value of this parameter is the same as that of the JobId parameter. |
| AccessKeyId | String | No | sejkwe21234sd | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DSSDF-SEWE-23ERW | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=SubmitRollbackTask &DbName=test &DrdsInstanceId=drdsxxxxxxxxxx &ExpandType=smooth_expand &JobId=123 &ParentJobId=123 <SubmitRollbackTaskResponse>
      <RequestId>DSSDF-SEWE-23ERW</RequestId>
</SubmitRollbackTaskResponse>
```

JSON format `{`

```json
    "RequestId":"DSSDF-SEWE-23ERW",
    "Success":true
```

#### 2.3.28 SubmitSqlFlashbackTask

Submits an SQL flashback task for a PolarDB-X instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SubmitSqlFlashba ckTask | The operation that you want to perform. Set the value to SubmitSqlFlashba ckTask. |
| DbName | String | Yes | testdb | The name of the PolarDB-X 1.0 database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| EndTime | String | Yes | 2019-09-10 23:23:23 | The time when the SQL flashback task ends. |
| RecallRestoreType | Integer | Yes | 0 | Specifies whether to implement exact match or fuzzy match. Valid values: 0: the exact match. 1: the fuzzy match. |
| StartTime | String | Yes | 2019-09-10 20:23:23 | The time when the SQL flashback task starts. |
| AccessKeyId | String | No | Accexxxxxxxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |
| RecallType | Integer | No | 0 | Specifies whether to implement exact match or fuzzy match. Valid values: 0: the exact match. 1: the fuzzy match. |
| SqlPk | String | No | 23423 | The primary key of the flashback SQL statement. |

| Developer Guide·API re | ference |   | Cloud Native | Distributed Database PolarDB- |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SqlType | String | No | INSERT,UPDATE | The type of the SQL statement. Valid values: INSERT, UPDATE, and DELETE. Separate multiple values with comma (,). |
| TableName | String | No | tb1 | The name of the table on which you want to perform SQL flashback. |
| TraceId | String | No | asenw3sa | The trace ID of the flashback SQL statement. You can query it in the PolarDB-X 1.0 SQL audit results. |

```xml
http(s)://[Endpoint]/? Action=SubmitSqlFlashbackTask &DbName=testdb &DrdsInstanceId=drdsxxxxxxxxxx &EndTime=2019-09-10 23:23:23 &RecallRestoreType=0 &StartTime=2019-09-10 20:23:23 <SubmitSqlFlashbackTaskResponse>
      <RequestId>DSSDF-SEWE-23ERW</RequestId>
      <TaskId>2323</TaskId>
</SubmitSqlFlashbackTaskResponse>
```

JSON format `{`

```json
    "RequestId":"DSSDF-SEWE-23ERW",
    "TaskId":2323,
    "Success":true
```

#### 2.3.29 SwitchGlobalBroadcastType

Switches the broadcast table in a PolarDB-X database from the multi-write mode to the asynchronous link mode.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SwitchGlobalBroa dcastType | The operation that you want to perform. Set the value to SwitchGlobalBroa dcastType. |
| DbName | String | Yes | testdb | The name of the PolarDB-X 1.0 database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Boolean | true | Indicates whether the broadcast table was switched from multi- write mode to asynchronous link mode. |
| RequestId | String | DSSDF-SEWE-23ERW | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=SwitchGlobalBroadcastType &DbName=testdb &DrdsInstanceId=drdsxxxxxxxxx <ValidateShardTaskResponse>
     <RequestId>DSSDF-SEWE-23ERW</RequestId>
     <Data>true</Data>
</ValidateShardTaskResponse>
```

JSON format `{`

```json
    "Data":true,
    "RequestId":"DSSDF-SEWE-23ERW",
    "success":true
```

#### 2.3.30 UpgradeInstanceVersion

Upgrades the version of the PolarDB-X 1.0 instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpgradeInstanceV ersion | The operation that you want to perform. Set the value to UpgradeInstanceV ersion. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxx | The ID of the PolarDB-X 1.0instance. |
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | true | Indicates whether the request was successful. |
| RequestId | String | DSSDF-SEWE-23ERW | The ID of the request. |

```xml
http(s)://[Endpoint]/? Action=UpgradeInstanceVersion &DrdsInstanceId=drdsxxxxxxxxxx <UpgradeInstanceVersionResponse>
      <RequestId>DSSDF-SEWE-23ERW</RequestId>
      <Data>True</Data>
</UpgradeInstanceVersionResponse>
```

JSON format `{`

```json
    "Data":"true",
    "RequestId":"DSSDF-SEWE-23ERW"
```
