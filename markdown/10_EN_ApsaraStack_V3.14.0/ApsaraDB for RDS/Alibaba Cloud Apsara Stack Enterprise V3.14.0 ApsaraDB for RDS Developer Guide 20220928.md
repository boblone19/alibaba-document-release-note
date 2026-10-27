---
title: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 ApsaraDB for RDS Developer Guide 20220928"
product_version: "V3.14.0"
doc_version: "20220928"
pdf_pages: 174
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 ApsaraDB for RDS Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/20230221/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.14.0%20ApsaraDB%20for%20RDS%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.14.0 ApsaraDB for RDS Developer Guide 20220928

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
- 2 API reference
  - 2.1 Instance management
    - 2.1.1 CreateDBInstance
    - 2.1.2 DeleteDBInstance
    - 2.1.3 RestartDBInstance
    - 2.1.4 DescribeDBInstanceAttribute
    - 2.1.5 DescribeDBInstances
    - 2.1.6 ModifyDBInstanceSpec
    - 2.1.7 DescribeDBInstanceNetInfo
    - 2.1.8 ModifyDBInstanceConnectionString
    - 2.1.9 ModifyDBInstanceNetworkType
    - 2.1.10 DescribeDBInstanceIPArrayList
    - 2.1.11 ModifySecurityIps
    - 2.1.12 DescribeRegions
    - 2.1.13 DescribeDBInstanceHAConfig
    - 2.1.14 MigrateToOtherZone
    - 2.1.15 PurgeDBInstanceLog
    - 2.1.16 ModifyDBInstanceDescription
    - 2.1.17 ModifyDBInstanceMaintainTime
    - 2.1.18 ModifyDBInstanceHAConfig
    - 2.1.19 SwitchDBInstanceHA
    - 2.1.20 CreateReadOnlyDBInstance
    - 2.1.21 DescribeDBInstanceSSL
    - 2.1.22 ModifyDBInstanceSSL
    - 2.1.23 DescribeDBInstanceTDE
    - 2.1.24 ModifyDBInstanceTDE
  - 2.2 Database management
    - 2.2.1 CreateDatabase
    - 2.2.2 DeleteDatabase
    - 2.2.3 DescribeDatabases
    - 2.2.4 ModifyDBDescription
  - 2.3 Account management
    - 2.3.1 CreateAccount
    - 2.3.2 DeleteAccount
    - 2.3.3 DescribeAccounts
    - 2.3.4 GrantAccountPrivilege
    - 2.3.5 RevokeAccountPrivilege
    - 2.3.6 ModifyAccountDescription
    - 2.3.7 ResetAccountPassword
    - 2.3.8 ResetAccount
  - 2.4 Backup and restoration
    - 2.4.1 CreateBackup
    - 2.4.2 CloneDBInstance
    - 2.4.3 DescribeBackups
    - 2.4.4 CreateTempDBInstance
    - 2.4.5 DescribeBackupPolicy
    - 2.4.6 ModifyBackupPolicy
    - 2.4.7 RestoreDBInstance
    - 2.4.8 DeleteBackup
  - 2.5 Monitoring management
    - 2.5.1 DescribeResourceUsage
    - 2.5.2 DescribeDBInstancePerformance
    - 2.5.3 DescribeDBInstanceMonitor
    - 2.5.4 ModifyDBInstanceMonitor
  - 2.6 Parameter management
    - 2.6.1 DescribeParameterTemplates
    - 2.6.2 DescribeParameters
    - 2.6.3 ModifyParameter
  - 2.7 Log management
    - 2.7.1 DescribeSlowLogs
    - 2.7.2 DescribeSlowLogRecords
    - 2.7.3 DescribeErrorLogs
    - 2.7.4 DescribeBinlogFiles
    - 2.7.5 DescribeSQLCollectorPolicy
    - 2.7.6 ModifySQLCollectorPolicy
    - 2.7.7 DescribeSQLLogRecords
    - 2.7.8 DescribeSQLLogFiles
  - 2.8 Data migration
    - 2.8.1 CreateUploadPathForSQLServer
    - 2.8.2 DescribeFilesForSQLServer
    - 2.8.3 ImportDatabaseBetweenInstances
    - 2.8.4 CancelImport
  - 2.9 Tag management
    - 2.9.1 AddTagsToResource
    - 2.9.2 DescribeTags
    - 2.9.3 RemoveTagsFromResource
  - 2.10 RAM authorization
  - 2.11 Appendix
    - 2.11.1 Error codes on the client
      - 2.11.1.1 Common errors
      - 2.11.1.2 Specific errors
    - 2.11.2 Error codes on the server
    - 2.11.3 Instance states
    - 2.11.4 Performance parameters
    - 2.11.5 Forbidden keywords
    - 2.11.6 Instance types

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

`https` : the protocol used to transmit the request. `public.asapi.aliyuns.com/asapi/v3` : the endpoint of the ASAPI. `Action=GetOrganizationList Product=ascm Version=2019-05-10` : the API operation to call. `Id` : the ID of the organization. `<Common parameters>` : the common parameters specified in the system. Apsara Stack SDKs Protocol The ASAPI supports only HTTPS. Endpoint For more information about how to obtain an endpoint, see Generate an endpoint for the ASAPI. Parameter To specify an API operation, use the `Action, Product, and Version` parameters. For example, set `Action` to GetOrganizationList, Product to ascm, and Version to 2019-05-10. You must also specify other operation-specific parameters and common parameters. For more information, see Common parameters.

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

## 2 API reference

### 2.1 Instance management

#### 2.1.1 CreateDBInstance

Description Creates an ApsaraDB RDS instance. For information about instance types, see Instance types in Appendix. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to CreateDBInstance. |
| RegionId | Strin g | Yes | The region ID of the instance. It can be up to 50 characters in length. You can call the DescribeRegions operation to query the most recent region list. |
| ZoneId | Strin g | No | The zone ID of the instance. You can call the DescribeRegions operation to query the most recent zone list. |
| Engine | Strin g | Yes | The engine of the database. Valid values: MySQL SQLServer PostgreSQL POLARDB |
| EngineVersion | Strin g | Yes | The engine version of the database. Valid values: MySQL: 5.6, 5.7, and 8.0 SQL Server: 2008 R2, 2012 ent ha, 2012 std ha, 2016 ent ha, _ _ _ _ _ _ and 2016 std ha _ _ PostgreSQL: 9.4 and 10.0 PolarDB: 11 |
| DBInstanceClass | Strin g | Yes | The instance type. |
| DBInstanceStorag e | Integ er | Yes | The user-defined storage space. Valid values: MySQL High-availability Edition: 5 to 2000 PolarDB High-availability Edition: 5 to 2000 This value must be in 5 GB increments. Unit: GB. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| DBInstanceNetTy pe | Strin g | Yes | The network connection type of the instance. Valid values: Internet Intranet |
| DBInstanceDescri ption | Strin g | No | The description of the instance. It must be 2 to 256 bytes in length , https:// and can contain letters, digits, underscores ( ), _ and hyphens (-). It must start with a letter and cannot start with http:// or https://. |
| SecurityIPList | Strin g | Yes | The IP addresses that are allowed to access all databases on the instance. You can add a maximum of 1,000 IP addresses and separate them with commas (,). Format: %, 0.0.0.0/0, IP address (example: 10.23.12.24), or CIDR block (example: 10.23.12.24/24). /24 indicates that the prefix of each IP address is 24-bit long. You can replace 24 with a value within the range of 1 to 32. 0.0.0.0/0 indicates that the instance can be accessed by all devices. |
| ClientToken | Strin g | Yes | The client token that is used to ensure the idempotence of the request. |
| InstanceNetwork Type | Strin g | No | The network type of the instance. Valid values: VPC and Classic. Default value: Classic. |
| ConnectionMode | Strin g | No | The access mode of the instance. Valid values: Performance and Safe. If no value is specified, the system assigns an access mode. |
| VPCId | Strin g | No | The ID of the VPC. |
| VSwitchId | Strin g | No | The ID of the vSwitch. |
| PrivateIpAddress | Strin g | No | The VPC IP address that belongs to the specified vSwitch. If no value is specified, the system assigns a VPC IP address. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |
| DBInstanceId | String | The ID of the instance. |
| OrderId | String | The ID of the order. |
| ConnectionString | String | The endpoint that is used to connect to the database. |
| Port | String | The port that is used to connect to the database. |

Examples XML format Sample success responses

```xml
<CreateDBInstanceResponse> <OrderId>100789370xxxxx</OrderId> <ConnectionString>xxxxx.mysql.rds.aliyuncs.com </ConnectionString> <DBInstanceId>rds-xxxxx</DBInstanceId> <port>3306</port> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CreateDBInstanceResponse>
```

JSON format

```json
{ "OrderId": "100789370230206", "ConnectionString": "rds-xxxxx.mysql.rds.aliyuncs.com", "DBInstanceId": "rds-xxxxx", "Port": "3306", "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.1.2 DeleteDBInstance

Releases an ApsaraDB RDS instance. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The read/write splitting feature is disabled for the instance. The instance is a primary, read-only, disaster recovery, or temporary instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteDBInstance | The operation that you want to perform. Set the value to DeleteDBInstance. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxxxx x | The ID of the instance. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | N/A | Common response parameters. |

Examples Sample request s

```
https://rds.example.com/?Action=DeleteDBInstance &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &<[Common request parameters]>
```

Sample success responses XML format

```xml
<DeleteDBInstanceResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </DeleteDBInstanceResponse>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 2.1.3 RestartDBInstance

Restarts an ApsaraDB RDS instance. If a large number of transactions need to be submitted or rolled back, the restart process may be delayed for a minute. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance does not have ongoing backup tasks. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RestartDBInstanc e | The operation that you want to perform. Set the value to RestartDBInstance. |
| DBInstanceId | String | Yes | rm-uf6wjk5xxxxxx | The ID of the instance. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | N/A | Common response parameters. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=RestartDBInstance &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RestartDBInstanceResponse>
      <RequestId> 65BDA532-28AF-4122-AA39-B382721EEE64</RequestId></RestartDBInstanceRespon
se>
```

`JSON` format `{`

```json
    "RequestId": " 65BDA532-28AF-4122-AA39-B382721EEE64"
```

`}`

#### 2.1.4 DescribeDBInstanceAttribute

Description You can call this operation to query attributes of an instance. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDBInstanceAttribute. |
| DBInstanceI d | String | Yes | The ID of the instance. Up to 30 IDs can be entered at a time. Separate multiple IDs with commas (,). |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items |   |   | The array that consists of DBInstanceAttribute data. |

| eveloper Guide·API r | eference |   | ApsaraDB for RD |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| └DBInstanceId | String | rm-bpvxxxxx | The ID of the instance. |
| └ DBInstanceType | String | Primary | The role of the instance. Valid values: Primary: primary instance Readonly: read-only instance Guard: disaster recovery instance Temp: temporary instance |
| └Category | String | Basic | The RDS edition of the instance. Valid values: Basic: Basic Edition Standard: High-availability Edition Enterprise: Enterprise Edition |
| └InstanceNetwor kType | String | Classic | The network type of the instance. Valid values: Classic VPC |
| └RegionId | String | cn-hangzhou | The region ID of the instance. |
| └ZoneId | String | cn-hangzhou-a | The zone ID of the instance. |
| └ConnectionStrin g | String | rds- xxxxx.mysql.rds.al iyuncs.com | The endpoint used to connect to the instance. |
| └Port | String | 3306 | The port used to connect to the instance. |
| └Engine | String | MySQL | The engine of the database. |
| └EngineVersion | String | 5.5 | The engine version of the database. |
| └DBInstanceClass Type | String | s | The family of the instance. Valid values: s: shared instance x: general-purpose instance d: dedicated instance h: dedicated host |
| └DBInstanceClass | String | rds.mys2.small | The type of the instance. |
| └DBInstanceMem ory | Long | 240 | The memory capacity of the instance. Unit: MB. |
| └DBInstanceStora ge | Integer | 10 | The storage space of the instance. Unit: GB. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| └DBInstanceNetT ype | String | Internet | The network connection type of the instance. Valid values: Internet Intranet |
| └DBInstanceStatu s | String | Running | The status of the instance. For more information, see Instance states in Appendix. |
| └DBInstanceDescr iption | String | Test instance | The description of the instance. |
| └LockMode | String | Unlock | The lock status of the instance. Valid values: Unlock: normal ManualLock: locked manually LockByExpiration: locked automatically upon expiration LockByRestoration: locked automatically before instance rollback LockByDiskQuota: locked automatically due to full disk space |
| └LockReason | String | None | The reason why the instance is locked. |
| └DBMaxQuantity | Integer | 200 | The maximum number of databases that can be created for an instance. |
| └AccountMaxQua ntity | Integer | 50 | The maximum number of accounts that can be created for an instance. |
| └CreationTime | String | 2011-05- 30T12:11:4Z | The time when the instance was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. Example: 2011-05-30T12:11:4Z . |
| └ExpireTime | String | None | The expiration time of the instance. This parameter is not returned for pay-as-you-go instances. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| └MaintainTime | String | 00:00Z-02:00Z | The scheduled maintenance window of the instance. For example, 00:00Z-02:00Z indicates that routine maintenance can be performed from 00:00 to 02:00. |
| └AvailabilityValue | String | 100.0% | The availability status of the instance. Unit: %. |
| └MaxIOPS | Integer | 150 | The maximum number of I/O operations per second (IOPS). |
| └MaxConnections | Integer | 60 | The maximum number of concurrent connections to the instance. |
| └MasterInstanceI d | String | null | The ID of the primary instance. If this parameter is not returned (null), the instance is a primary instance. |
| └IncrementSourc eDBInstanceId | String | null | The instance ID of the incremental data source. For example, the incremental data source of a disaster recovery instance or read-only instance is the primary instance, and the incremental data source of the primary instance is null. |
| └GuardDBInstanc eId | String | None | The ID of the disaster recovery instance attached to the instance. |
| └TempDBInstanc eId | String | None | The ID of the temporary instance attached to the instance. |
| └ReadOnlyDBInst anceIds |   | rr-xxxxx | The IDs of the read-only instances attached to the instance. |
| └DBInstanceId | String | rm-bpxxxxx | The ID of the instance. |
| └VpcCloudInstan ceId | String | vpc-xxxxx | The ID of the VPC. |
| └ResourceGroupI d | String | 3653788125 | The ID of the resource group. |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | The ID of the request. |

DBInstanceAttribute parameters Not e You can call the DescribeDBInstanceHAConfig operation to query information of the primary and secondary instances. Examples Sample request s

```
https://rds.example.com/?Action=DescribeDBInstanceAttribute &DBInstanceId=rds-xxxxx &<Common request parameters>
```

Sample success responses JSON format

```json
{ "Items":
    { "DBInstanceAttribute":
        [ { "LockMode": "Unlock",
            "ConnectionString": "rds-xxxxx.mysql.rds.aliyuncs.com",
            "CreationTime": "2014-10-10T10:28:48Z",
            "DBInstanceNetType": "Internet",
            "ReadOnlyDBInstanceIds": { "ReadOnlyDBInstanceId": [] },
            "MaxConnections": 60,
            "LockReason": "",
            "Engine": "MySQL",
            "AvailabilityValue": "100.0%",
            "AccountMaxQuantity": 50,
            "DBMaxQuantity": 200,
            "RegionId": "cn-hangzhou",
            "TempDBInstanceId": "",
            "DBInstanceMemory": 240,
            "MaxIOPS": 150,
            "DBInstanceType": "Primary",
            "DBInstanceStatus": "Running",
            "MasterInstanceId": "",
            "EngineVersion": "5.6",
            "IncrementSourceDBInstanceId": "",
            "GuardDBInstanceId": "",
            "DBInstanceStorage": 10,
            "DBInstanceDescription": "",
            "DBInstanceId": "rdsfnjfquxxxxx",
            "PayType": "Postpaid",
            "ExpireTime": "",
            "MaintainTime": "",
            "DBInstanceClass": "rds.mys2.small",
            "SecurityIPList": "11.11.11.11",
            "Port": "3306" } ] },
    "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

Sample error responses JSON format

```json
{ "Code":"UnsupportedOperation", "HostId":"rds.aliyuncs.com", "Message":"The specified action is not supported.", "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.1.5 DescribeDBInstances

Description You can call this operation to query instances and RAM-authorized instances. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstanc es | The operation that you want to perform. Set the valuer to DescribeDBInstanc es. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. |
| ConnectionMode | String | No | Performance | The access mode of the instance. Valid values: Performance: standard access mode Safe: safe access mode If no value is specified, instances in both access modes are returned. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceType | String | No | Primary | The role of the instance. Valid values: Primary: primary instance Readonly: read- only instance Guard: disaster recovery instance Temp: temporary instance If no value is specified, instance of all roles are returned. |
| InstanceNetworkT ype | String | No | Classic | The network type of the instance. Valid values: VPC: VPC instance Classic: classic network instance If no value is specified, instance of both network types are returned. |
| PageNumber | Integer | No | 1 | The number of the page to return. Pages start from page 1 but must be equal to or smaller than the maximum Integer value. Default value: 1. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| Tags | String | No | {“key1”:”value 1”} | The tag of the instance, in the JSON format. The tag includes a key-value pair of TagKey and TagValue. TagValue can be left empty, but TagValue cannot. Example: {“key1”:”value 1”}. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The number of the page returned. |
| TotalRecordCount | Integer | 1 | The total number of entries. |
| PageRecordCount | Integer | 1 | The number of instances on the current page. |
| Items |   |   | The array that consists of instance data. |
| └DBInstanceId | String | rm-xxxxx | The ID of the instance. |
| └DBInstanceDescription | String | testforRemarks | The description of the instance. |
| └PayType | String | Postpaid | The billing method of the instance. Valid values: Postpaid: pay-as- you-go Prepaid: subscription |

| Parameter | Type | Example | Description |
|---|---|---|---|
| └DBInstanceType | String | Primary | The role of the instance. Valid values: Primary: primary instance ReadOnly: read-only instance Guard: disaster recovery instance Temp: temporary instance |
| └InstanceNetworkType | String | Classic | The network type of the instance. Valid values: Classic: classic network instance VPC: VPC instance |
| └ConnectionMode | String | Performance | The access mode of the instance. Valid values: Performance: standard access mode Safe: safe access mode |
| └RegionId | String | cn-hangzhou | The region ID of the instance. |
| └ExpireTime | String | None | The expiration time of the instance. This parameter is not returned for pay-as- you-go instances. |
| └DBInstanceStatus | String | Intranet | The status of the instance. For more information, see Instance states in Appendix. |
| └Engine | String | MySQL | The type of the database. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| └DBInstanceNetType | String | Internet | The network connection type of the instance. Valid values: Internet: public network Intranet: internal network |
| └LockMode | String | Unlock | The lock status of the instance. Valid values: Unlock: normal ManualLock: locked manually LockByExpiration: locked automatically upon expiration LockByRestoration: locked automatically before instance rollback LockByDiskQuota: locked automatically for full disk space |
| └LockReason | String | None | The reason why the instance is locked. |
| └MasterInstanceId | String | null | The ID of the primary instance. If this parameter is not returned (null), the instance is a primary instance. |
| └GuardDBInstanceId | String | None | The ID of the disaster recovery instance attached to the instance. |
| └TempDBInstanceId | String | None | The ID of the temporary instance attached to the instance. |
| └VpcCloudInstanceId | String | vpc-xxxxx | The ID of the VPC instance. |
| └ReadOnlyDBInstanceId s |   |   | None |
| └DBInstanceId | String | rm-xxxxx | The ID of the instance. |

| A | psaraDB for RDS |   | De | veloper Guide·API referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1AD222E9-E606-4A42- BF6D-8A4442913CEF | The ID of the request. |

Examples Sample request s

```
https://rds.example.com/?Action=DescribeDBInstances &RegionId=cn-hangzhou &Engine=MySQL &<Common request parameters>
```

Sample success responses XML format

```xml
<DescribeDBInstancesResponse> <PageRecordCount>2</PageRecordCount> <Items> <DBInstance> <DBInstanceDescription>testforRemarks</DBInstanceDescription> <ExpireTime>2014-10-10T16:00:00Z</ExpireTime> <DBInstanceId>rdsmjfirxxxxx</DBInstanceId> <DBInstanceNetType>Internet</DBInstanceNetType> <PayType>Prepaid</PayType> <DBInstanceStatus>Running</DBInstanceStatus> <DBInstanceType>Primary</DBInstanceType> <Engine>MySQL</Engine> <LockMode>Unlock</LockMode> <LockReason/> <RegionId>cn-hangzhou</RegionId> <ZoneId>cn-hangzhou-a</ZoneId> <MasterInstanceId/> <GuardDBInstanceId/> <TempDBInstanceId/> <ReadOnlyDBInstanceIds> <ReadOnlyDBInstanceId/> </ReadOnlyDBInstanceIds> </DBInstance> </Items> <PageNumber>1</PageNumber> <TotalRecordCount>2</TotalRecordCount> <RequestId>2553A660-E4EB-4AF4-A402-8AFF70A49143</RequestId> </DescribeDBInstancesResponse>
```

JSON format

```json
{ "Items":
    { "DBInstance":
        [ { "DBInstanceDescription":"testforRemarks",
            "DBInstanceId":"rdsmjfirxxxxx",
            "DBInstanceNetType":"Internet",
            "DBInstanceStatus":"Running",
            "DBInstanceType":"Primary",
            "Engine":"MySQL",
            "ExpireTime":"2014-10-10T16:00:00Z",
            "GuardDBInstanceId ":"",
            "LockMode":"Unlock",
            "LockReason":"",
            "MasterInstanceId":"",
            "PayType":"Prepaid",
            "ReadOnlyDBInstanceIds":{ "ReadOnlyDBInstanceId":[] },
            "RegionId":"cn-hangzhou",
            "TempDBInstanceId":"",
            "ZoneId":"cn-hangzhou-a" },
        ] },
    "PageNumber":1,
    "PageRecordCount":2,
    "RequestId":"2553A660-E4EB-4AF4-A402-8AFF70A49143",
    "TotalRecordCount":2
```

`}` Sample error responses JSON format

```json
{ "Code":"UnsupportedOperation", "HostId":"rds.aliyuncs.com", "Message":"The specified action is not supported.", "RequestId":"7463B73D-35CC-4D19-A010-6B8D65D242EF"}
```

#### 2.1.6 ModifyDBInstanceSpec

Description You can call this operation to change the type or storage space of an instance. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance is not performing a backup task. One of the instance type (DBInstanceClass) and storage space (DBInstanceStorage) parameters is specified in the request. When you downgrade the disk space configuration, the input disk space is no less than 1.1 times the actually used space. Only primary and read-only instances allow specification changes. Specifications of disaster recovery and temporary instances cannot be changed.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstance Spec | The operation that you want to perform. Set the value to ModifyDBInstance Spec. |
| DBInstanceId | String | Yes | rm-bpxxxx | The ID of the instance. |
| AccessKeyId | String | No | LTAIKw8gqxxxxx | The AccessKey ID provided by Alibaba Cloud. |
| ClientToken | String | No | ETnLKlblzczshOTU bOCziJZNwHlYBQ | The client token that is used to ensure idempotence of the request. |
| DBInstanceClass | String | No | rds.mys2.small | The instance type. For more information, see Instance types in Appendix. |
| DBInstanceStorage | Integer | No | 20 | The user-defined storage space. Unit: GB. This value must be in 5 GB increments. For more information, see the Instance types topic in the User Guide of ApsaraDB RDS. |
| EffectiveTime | String | No | Immediate | The time when the changes take effect. Valid values: Immediate and MaintainTime. Default value: Immediate. |
| OwnerAccount | String | No | testuser@aliyun.c om | The Apsara Stack tenant account. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1AD222E9-E606-4A42- BF6D-8A4442913CEF | The ID of the request. |

Examples Sample request s

```
https://rds.example.com/?Action=ModifyDBInstanceSpec &DBInstanceId=rds-xxxxx &PayType=Postpaid &DBInstanceStorage=10 &<Common request parameters>
```

Sample success responses XML format

```xml
<ModifyDBInstanceSpecResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyDBInstanceSpecResponse>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

Sample error responses JSON format

```json
{ "Code":"UnsupportedOperation", "HostId":"rds.aliyuncs.com", "Message":"The specified action is not supported.", "RequestId":"7463B73D-35CC-4D19-A010-6B8D65D242EF"}
```

#### 2.1.7 DescribeDBInstanceNetInfo

Queries the connection information of an instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstan ceNetInfo | The operation that you want to perform. Set the value to DescribeDBInst anceNet Inf o. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| Flag | String | No | N/A | A hidden parameter. |
| DBInstanceNetRW SplitType | String | No | Normal | The type of the endpoint. Valid values: Normal ReadWrit eSplit t ing Not e By default, the system returns both types of endpoints. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceNetI nfos | Array |   | Details about the instance endpoint. |
| DBInstanceNetI nfo |   |   |   |
| ConnectionStrin g | String | rm- uf6wxxxxx.mysql.rd s.aliyuncs.com | The endpoint of the instance. |
| IPAddress | String | 192.168.12.84 | The IP address of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| IPType | String | Public | The network type of the instance. Valid values when the instance resides in the classic network: Inner: internal network Public: Internet Valid values when the instance resides in a virtual private cloud (VPC): Privat e: internal network Public: Internet |
| Port | String | 3306 | The port that is used to connect to the instance. |
| VPCId | String | vpc- uf6f7l4fg90xxxxxxxx xx | The ID of the VPC. |
| VSwitchId | String | vsw- uf6adz52c2pxxxxxxx xxx | The ID of the vSwitch. |
| ConnectionStrin gType | String | Normal | The type of the endpoint. Valid values: Normal ReadWrit eSplit t ing |
| MaxDelayTime | String | 12 | The latency threshold. This parameter is returned only for a read/write splitting endpoint. Unit: seconds. Not e If the latency on a read- only instance exceeds the specified threshold, ApsaraDB RDS no longer routes read requests to the read-only instance. |
| DistributionTyp e | String | Standard | The policy that is used to allocate read weights. This parameter is returned only for a read/write splitting endpoint. Valid values: St andard: ApsaraDB RDS allocates a read weight to each instance based on the instance specifications. Cust om: You must manually assign a read weight to each instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceWeig hts | Array |   | Details about the weight. This parameter is returned only when the read/write splitting feature is enabled for the instance. |
| DBInstanceWeig ht |   |   |   |
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | The ID of the instance. |
| DBInstanceType | String | Master | The role of the instance. Valid values: Mast er: primary instance Readonly: read-only instance |
| Weight | String | 100 | The weight of the instance. |
| Availability | String | Unavailable | The availability of the instance. Valid values: Unavailable Available |
| ExpiredTime | String | 1209534 | The remaining time of the classic network in hybrid access mode. Unit: seconds. |
| SecurityIPGroup s | Array |   | Details about the IP address whitelist. |
| securityIPGroup |   |   |   |
| SecurityIPGroup Name | String | Default | The name of the IP address whitelist. |
| SecurityIPs | String | 127.0.0.1 | The IP addresses contained in the IP address whitelist. |
| Upgradeable | String | Disabled | Indicates whether the IP version can be updated. Valid values: Enable and Disabled. Not e The IP version can be updated from IPv4 to IPv6. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| InstanceNetwor kType | String | VPC | The network type of the instance. Valid values: Classic VPC |
| RequestId | String | 777C4593-8053- 427B-99E2- 105593277CAB | The ID of the request. |
| SecurityIPMode | String | safety | The whitelist mode of the instance. Valid values: normal: standard whitelist mode saf et y: enhanced whitelist mode |

Examples Sample requests

```
https://rds.example.com/?Action=DescribeDBInstanceNetInfo &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeDBInstanceNetInfoResponse>
      <dBInstanceNetInfos>
            <connectionString>rm-uf6wjk5xxxxxxx.mysql.rds.aliyuncs.com</connectionString>
            <connectionStringType>Normal</connectionStringType>
            <iPAddress>192.168.xx.xx</iPAddress>
            <iPType>Public</iPType>
            <port>3306</port>
            <upgradeable>Disabled</upgradeable>
            <vPCId></vPCId>
      </dBInstanceNetInfos>
      <instanceNetworkType>Classic</instanceNetworkType>
      <requestId>777C4593-8053-427B-99E2-105593277CAB</requestId>
</DescribeDBInstanceNetInfoResponse>
```

`JSON` format `{`

```json
    "dBInstanceNetInfos": [
```

`{`

```json
            "connectionString": "rm-uf6wjk5xxxxxxx.mysql.rds.aliyuncs.com",
            "connectionStringType": "Normal",
            "dBInstanceWeights": [],
            "iPAddress": "192.168.xx.xx",
            "iPType": "Public",
            "port": "3306",
            "securityIPGroups": [],
            "upgradeable": "Disabled",
            "vPCId": ""
```

`}` `],`

```json
    "instanceNetworkType": "Classic",
    "requestId": "777C4593-8053-427B-99E2-105593277CAB"
```

`}`

#### 2.1.8 ModifyDBInstanceConnectionString

Description You can call this operation to modify the endpoint and port of a connection string. ApsaraDB RDS provides the internal and public endpoints and allows both types to coexist in a specific access mode. Request parameters

| Parameter | Ty pe | Requir ed | Description |
|---|---|---|---|
| Action | Stri ng | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceConnectionString. |
| DBInstanceId | Stri ng | Yes | The ID of the instance. |
| CurrentConnectionS tring | Stri ng | Yes | The endpoint used by the instance. |
| ConnectionStringPr efix | Stri ng | No | The endpoint to be used by the instance. |
| Port | Stri ng | No | The port to be used by the instance. |

Response parameters This operation returns only common response parameters.

#### 2.1.9 ModifyDBInstanceNetworkType

Changes the network type of an ApsaraDB RDS instance. This operation is used to switch the network type of an instance between VPC and classic network. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstance NetworkType | The operation that you want to perform. Set the value to Modif yDBInst anceNet workT ype. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| InstanceNetwork Type | String | Yes | Classic | The new network type of the instance. Valid values: VPC Classic |
| VPCId | String | No | vpc- uf6f7l4fg90xxxxx x | The ID of the VPC. |
| VSwitchId | String | No | vsw- uf6adz52c2pxxxx x | The ID of the vSwitch. This parameter is required if the value of VPCId is specified. |
| PrivateIpAddress | String | No | 172.10.40.25 | The internal IP address of the instance, which must be within the CIDR block supported by the specified vSwitch. The system assigns an internal IP address based on the VPCId and VSwit chId parameters. |

Response parameters This operation returns only common response parameters. Examples Sample requests

```
https://rds.example.com/?Action=ModifyDBInstanceNetworkType &DBInstanceId=rm-uf6wjk5xxxxxxx &InstanceNetworkType=Classic &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceNetworkTypeResponse>
      <RequestId> 65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
</ModifyDBInstanceNetworkTypeResponse>
```

`JSON` format `{`

```json
  "RequestId": " 65BDA532-28AF-4122-AA39-B382721EEE64"
```

`}` Error codes For more information, see Common errors.

#### 2.1.10 DescribeDBInstanceIPArrayList

Description You can call this operation to query the IP whitelist of an instance. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDBInstanceIPArrayList. |
| DBInstanceId | String | Yes | The ID of the instance whose IP whitelist is queried. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | Common response parameters. |
| Items | List<DBInstanceIPAr ray> | The array that consists of DBInstanceIPArray data. |

DBInstanceIPArray parameters

| Parameter | Type | Description |
|---|---|---|
| DBInstanceIPArrayNam e | String | The name of the IP whitelist. |
| DBInstanceIPArrayAttri bute | String | The attribute of the IP whitelist. Default value: null. Whitelists tagged with "hidden" are not displayed in the console. |

|   | Developer Guide·API refer | ence | ApsaraDB for RD | S |
|---|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| SecurityIPList | String | The IP addresses in an IP address whitelist. Separate multiple IP addresses with commas (,). You can add a maximum of 1,000 different IP addresses to a whitelist. Supported formats of IP addresses are IP addresses such as 0.0.0.0/0 and 10.23.12.24, or Classless Inter-Domain Routing (CIDR) blocks such as 10.23.12.24/24. /24 indicates the length of the IP address prefix. The IP address prefix can consist of 1 to 32 bits. |

#### 2.1.11 ModifySecurityIps

Modifies an IP address whitelist of an instance. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance is not locked by the system. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySecurityIps | The operation that you want to perform. Set the value to ModifySecurityIps. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| SecurityIps | String | Yes | 10.23.12.24 | The IP addresses in an IP address whitelist. Separate multiple IP addresses with commas (,). Each IP address in the IP address whitelist must be unique. You can add IP addresses in the following formats: IP addresses, such as 10.23.12.24. Classless Inter-Domain Routing (CIDR) blocks, such as 10.23.12.0/24. In this case, /24 indicates that the prefix of each IP address is 24-bit long. You can replace 24 with a value within the range of 1 to 32. Not e A maximum of 1,000 IP addresses and CIDR blocks can be configured for each instance. If you want to add a large number of IP addresses, we recommend that you merge them into CIDR blocks, such as 10.23.12.0/24. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceIPArray Name | String | No | test | The name of the IP address whitelist to be modified. Default value: Default. Not e A maximum of 200 IP address whitelists can be configured for each instance. |
| DBInstanceIPArray Attribute | String | No | hidden | The attribute of the IP address whitelist. This parameter is empty by default. Not e The IP address whitelists that have the hidden attribute are not displayed in the ApsaraDB RDS console. These IP address whitelists are used to access Alibaba Cloud services such as Data Transmission Service (DTS). |

Response parameters This operation returns only common response parameters. Examples Sample request s

```
https://rds.example.com/?Action=ModifySecurityIps &DBInstanceId=rds-xxxxx &SecurityIps=192.168.1.2 &<Common request parameters>
```

Sample success responses XML format

```xml
<ModifySecurityIpsResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifySecurityIpsResponse>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.1.12 DescribeRegions

You can call this operation to query the available RDS regions and zones. Before you call the CreateInstance operation, call this operation to query region IDs. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeRegions. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |
| Regions | List<RDSRegion> | The array that consists of RDSRegion data. |

RDSRegion parameters

| Parameter | Type | Description |
|---|---|---|
| RegionId | String | The region ID. |
| ZoneId | String | The zone ID. |

Examples Sample request s

```
https://rds.example.com/?Action=DescribeRegions &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeRegionsResponse> <Regions> <RDSRegion> <RegionId>cn-hangzhou</RegionId> <ZoneId>cn-hangzhou-a</RegionId> </RDSRegion> <RDSRegion> <RegionId>cn-hangzhou</RegionId ><ZoneId>cn-hangzhou-b</ZoneId> </RDSRegion> </Regions> <RequestId>A36D9720-7902-42A4-B8B9-014A2135E6C3</RequestId> </DescribeRegionsResponse>
```

JSON format

```json
{ "Regions":
    { "RDSRegion":
        [ {"RegionId": "cn-hangzhou",
            "ZoneId":"cn-hangzhou-a"},
          {"RegionId": "cn-hangzhou",
            "ZoneId":"cn-hangzhou-b"},
             ]},
    "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"
```

`}`

#### 2.1.13 DescribeDBInstanceHAConfig

Queries the high availability mode and data replication mode of an ApsaraDB RDS instance. Request parameters

| Parameter | Type | Require d | Exam ple | Description |
|---|---|---|---|---|
| Action | String | Yes | Descri beDBI nstan ceHAC onfig | The operation that you want to perform. Set the value to DescribeDBInstanceHAConfig. |
| DBInstanceI d | String | Yes | rm- uf6wj k5xxxx xx | The ID of the instance. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | N/A | Common response parameters. |
| DBInstanceId | String | The ID of the instance. |
| SyncMode | String | The synchronization mode. Valid values: Semi-sync and Async. |
| HAMode | String | The high availability mode. RPO: Data persistence is preferred. RTO: Instance availability is preferred. |
| HostInstanceInfos | List<NodeI nfo> | Details about primary and secondary instances. |

NodeInfo parameters

| Parameter | Type | Description |
|---|---|---|
| NodeId | String | The unique ID of the primary or secondary instance. |
| NodeType | String | The role of the instance. Master: primary instance. Slave: secondary instance. |
| RegionId | String | The region ID of the instance. |
| ZoneId | String | The zone ID of the instance. |
| SyncStatus | String | The synchronization status of the instance. NotAvailable: Synchronization is unavailable because a failure has occurred. Syncing: Synchronization is in process, with a probability of data loss during failovers. Synchronized: Synchronization is complete. NotSupport: Synchronization is not supported by the engine type or version. |
| LogSyncTime | String | The time when the secondary instance receives logs. |
| DataSyncTime | String | The time when the secondary instance receives data. |

Examples Sample requests

```
https://rds.example.com/?Action=DescribeDBInstanceHAConfig &DBInstanceId=rm-uf6wjk5xxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeDBInstanceHAConfigResponse>
      <dBInstanceId>rm-uf6wjk5xxxxxx</dBInstanceId>
      <hAMode>RPO</hAMode>
      <hostInstanceInfos>
            <logSyncTime>2018-01-19T12:33:06Z</logSyncTime>
            <nodeId>3397027</nodeId>
            <nodeType>Slave</nodeType>
            <regionId>cn-shenzhen</regionId>
            <syncStatus>Syncing</syncStatus>
            <zoneId>cn-shenzhen-b</zoneId>
      </hostInstanceInfos>
      <hostInstanceInfos>
            <logSyncTime>2018-01-19T12:33:06Z</logSyncTime>
            <nodeId>3397029</nodeId>
            <nodeType>Master</nodeType>
            <regionId>cn-shenzhen</regionId>
            <syncStatus>Syncing</syncStatus>
            <zoneId>cn-shenzhen-a</zoneId>
      </hostInstanceInfos>
      <requestId>F051AEB2-7655-4F0A-BC46-7E0C18A7910C</requestId>
      <syncMode>Semi-sync</syncMode>
</DescribeDBInstanceHAConfigResponse>
```

`JSON` format `{`

```json
    "dBInstanceId": "rm-uf6wjk5xxxxxx",
    "hAMode": "RPO",
    "hostInstanceInfos": [
```

`{`

```json
            "logSyncTime": "2018-01-19T12:33:06Z",
            "nodeId": "3397027",
            "nodeType": "Slave",
            "regionId": "cn-shenzhen",
            "syncStatus": "Syncing",
            "zoneId": "cn-shenzhen-b"
```

`},` `{`

```json
            "logSyncTime": "2018-01-19T12:33:06Z",
            "nodeId": "3397029",
            "nodeType": "Master",
            "regionId": "cn-shenzhen",
            "syncStatus": "Syncing",
            "zoneId": "cn-shenzhen-a"
```

`}` `],`

```json
    "requestId": "F051AEB2-7655-4F0A-BC46-7E0C18A7910C",
    "syncMode": "Semi-sync"
```

`}`

#### 2.1.14 MigrateToOtherZone

Migrates an ApsaraDB RDS instance across zones within the same region. For example, if Instance 1 is located in Hangzhou Zone A, you can call this operation to migrate the instance to Hangzhou Zone B. Not e In cross-zone migration, instances must be migrated within the same region. For example, instances in a zone of the China (Hangzhou) region cannot be migrated to a zone of the China (Qingdao) region. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | MigrateTo OtherZone | The operation that you want to perform. Set the value to MigrateToOtherZone. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxx xxxxxxx | The ID of the instance. |
| ZoneId | String | Yes | cn- hangzhou- b | The ID of the destination zone. You can call the operation to query available zones. |

Response parameters This operation returns only common response parameters. Examples Sample request s

```
https://rds.example.com/?Action=MigrateToOtherZone &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &ZoneId=cn-hangzhou-b &<Common request parameters>
```

Sample success responses XML format

```xml
<MigrateToOtherZoneResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </MigrateToOtherZoneResponse>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.1.15 PurgeDBInstanceLog

Clears logs of an ApsaraDB RDS instance. For an ApsaraDB RDS for MySQL instance, this operation clears all binlogs of the instance. For an ApsaraDB RDS for SQL Server instance, this operation generates a temporary backup and compresses transaction logs to release space. Not e This operation is available only for instances that run MySQL or SQL Server. Request parameters

| Parameter | Type | Required | Exampl e | Description |
|---|---|---|---|---|
| Action | String | Yes | PurgeD BInstan ceLog | The operation that you want to perform. Set the value to PurgeDBInstanceLog. |
| DBInstanceId | String | Yes | rm- uf6wjk5 xxxxxxx | The ID of the instance. |

Response parameters This operation returns only common response parameters. Examples Sample request s

```
https://rds.example.com/?Action=PurgeDBInstanceLog &DBInstanceId=rds-xxxxx &<Common request parameters>
```

Sample success responses XML format

```xml
<PurgeDBInstanceLogResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </PurgeDBInstanceLogResponse>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.1.16 ModifyDBInstanceDescription

Description You can call this operation to modify the description of an instance to identify the instance easily. For example, you can modify the description of an instance to Alibaba Cloud testing environment instance.

| Parameter | Type | Require d | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceDescription. |
| DBInstanceId | Strin g | Yes | The ID of the instance whose description is modified. |
| DBInstanceDescri ption | Sting | Yes | The description of the instance. |

Response parameters This operation returns only common response parameters. Examples Sample request s

```
https://rds.example.com/?Action=ModifyDBInstanceDescription &DBInstanceId=rds-xxxxx &DBInstanceDescription=testdescribe &<Common request parameters>
```

Sample responses XML format

```xml
<ModifyDBInstanceDescriptionResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyDBInstanceDescriptionResponse>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.1.17 ModifyDBInstanceMaintainTime

Modifies the maintenance time of an ApsaraDB RDS instance. You can set the maintenance time to a period of time during off-peak hours. Alibaba Cloud performs routine maintenance within the maintenance window to minimize impacts on your business. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstance MaintainTime | The operation that you want to perform. Set the value to ModifyDBInstanceMaintainTime. |

| psaraDB for RDS |   |   |   | Developer Guide·API referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| MaintainTime | String | Yes | 22:00Z-02:00Z | The maintenance window of the instance. Specify the time in the ISO 8601 standard in the HH:mmZ-HH:mmZ format. The time must be in UTC. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters This operation returns only common response parameters. Examples Sample request s

```
https://rds.example.com/?Action=ModifyDBInstanceMaintainTime &DBInstanceId=rds-xxxxx &MaintainTime=22:00Z-02:00Z &<Common request parameters>
```

Sample success responses XML format

```xml
<ModifyDBInstanceMaintainTimeResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyDBInstanceMaintainTimeResponse>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 2.1.18 ModifyDBInstanceHAConfig

Description You can call this operation to modify the instance data replication mode and high availability switching rules.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceHAConfig. |
| DBInstanceI d | String | Yes | The ID of the instance. |
| SyncMode | String | Yes | The synchronization mode of the instance. Valid values: Semi-sync and Async. |
| HAMode | String | Yes | The HA mode of the instance. RPO: Data persistence is preferred. RTO: Instance availability is preferred. |

Response parameters This operation returns only common response parameters.

#### 2.1.19 SwitchDBInstanceHA

Switches services between a primary ApsaraDB RDS instance and its secondary instance. This operation switches services between the primary and secondary ApsaraDB RDS instances that do not run the Basic Edition. After the switchover, the secondary instance takes over services as the primary instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SwitchDBInstance HA | The operation that you want to perform. Set the value to SwitchDBInstanceHA. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxxxx x | The ID of the primary instance. |
| NodeId | String | Yes | 349054 | The unique ID of the secondary instance. |
| Force | String | No | No | Specifies whether to enable forced switching. Valid values: Yes: forced No: unforced Default value: No |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| EffectiveTime | String | No | Immediate | The time when you want the specified settings to take effect. Valid values: Immediate: The switching immediately takes effect. MaintainTime: The switching takes effect during the maintenance window. Default value: Immediate. |

Response parameters This operation returns only common response parameters. Examples Sample requests

```
https://rds.example.com/?Action=SwitchDBInstanceHA &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &NodeId=349054 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SwitchDBInstanceHAResponse>
      <RequestId>1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC</RequestId>
</SwitchDBInstanceHAResponse>
```

`JSON` format `{`

```json
    "RequestId": "1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC"
```

`}`

#### 2.1.20 CreateReadOnlyDBInstance

Description Creates a read-only instance for a primary ApsaraDB RDS instance. Before you call this operation, make sure that the following requirements are met: The primary instance is in the running state, but not in the failover state. The read-only instance and the primary instance are in the same region. A primary ApsaraDB RDS instance can have up to five read-only instances.

| Parameter | Type | Require d | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateReadOnlyDBInstance. |
| RegionId | String | Yes | The region ID of the instance. It can be up to 50 characters in length. You can call the DescribeRegions operation to query the most recent region list. |
| ZoneId | String | Yes | The zone ID of the instance. You can call the DescribeRegions operation to query the most recent zone list. |
| DBInstanceId | String | Yes | The ID of the primary instance. |
| EngineVersion | String | Yes | The database engine version that the read-only instance runs. The read-only instance must run the same engine version as the primary instance. Valid values: 8.0 5.7 5.6 |
| DBInstanceClass | String | Yes | The instance type. |
| DBInstanceStorag e | Intege r | Yes | The user-defined storage capacity. Valid values: 5 to 1000. This value must be in 5 GB increments. Unit: GB. |
| DBInstanceDescri ption | String | No | The description of the instance. It must be 2 to 256 bytes in length , https:// and can contain letters, digits, underscores ( ), _ and hyphens (-). It must start with a letter and cannot start with http:// or https://. |
| ClientToken | String | Yes | The client token that is used to ensure idempotence of the request. |
| InstanceNetwork Type | String | No | The network type of the instance. Valid values: VPC and Classic. Default value: Classic. |
| VPCId | String | No | The ID of the VPC. |
| VSwitchId | String | No | The ID of the vSwitch. |
| PrivateIpAddress | String | No | The IP address of the VPC that belongs to VSwitchId. If no value is specified, the system allocates a VPC IP address based on VPCId and VSwitchId. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |

| psaraDB for RDS |   | Developer Guide·API referenc |
|---|---|---|
| Parameter | Type | Description |
| DBInstanceId | String | The ID of the instance. |
| OrderId | String | The ID of the order. |
| ConnectionStrin g | String | The endpoint that is used to connect to the database. |
| Port | String | The port that is used to connect to the database. |

Examples Sample request s

```
https://rds.example.com/?Action=CreateReadOnlyDBInstance &RegionId=cn-hangzhou &ZoneId=cn-hangzhou-b &DBInstanceId=rds-xxxxx &EngineVersion=5.6 &DBInstanceClass=rds.mys2.small &DBInstanceStorage=10 &PayType=Postpaid &ClientToken=ETnLKxxxxx &<[Common request parameters]>
```

Sample success responses XML format

```xml
<CreateDBInstanceResponse> <OrderId>10078937xxxxx</OrderId> <ConnectionString>rds-xxxxx.mysql.rds.aliyuncs.com </ConnectionString> <DBInstanceId>rds-xxxxx</DBInstanceId> <port>3306</port> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CreateDBInstanceResponse>
```

JSON format

```json
{ "OrderId": "100789370230206", "ConnectionString": "rds-xxxxx.mysql.rds.aliyuncs.com", "DBInstanceId": "rds-xxxxx", "Port": "3306", "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 2.1.21 DescribeDBInstanceSSL

Queries Secure Sockets Layer (SSL) settings of an ApsaraDB RDS instance. This operation is available for instances that run MySQL 5.6, MySQL 5.7, or SQL Server.

| Parameter | Type | Required | Examp le | Description |
|---|---|---|---|---|
| Action | String | Yes | Descri beDBI nstanc eSSL | The operation that you want to perform. Set the value to DescribeDBInstanceSSL. |
| DBInstanceId | String | Yes | rm- uf6wjk 5xxxxx xx | The ID of the instance. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | N/A | Common response parameters. |
| ConnectionString | String | The endpoint that is protected by SSL encryption. |
| SSLExpireTime | String | The expiration time of the SSL certificate. This time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. |
| RequireUpdate | String | Indicates whether an immediate update is required. Valid values: Yes and No. |
| RequireUpdateRea son | String | The reason why an update is required. |

Examples Sample requests

```
https://rds.example.com/?Action=DescribeDBInstanceSSL &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeDBInstanceSSLResponse>
      <items>
            <ConnectionString>rm-uf6wjk5xxxxxx.mysql.rds.aliyuncs.com</ConnectionString>
            <SSLExpireTime>2018-01-17T12:18:15Z</SSLExpireTime>
            <RequireUpdate>Yes</RequireUpdate>
            <RequireUpdateReason></RequireUpdateReason>
      </items>
      <requestId>1AD222E9-E606-4A42-BF6D-8A4442913CEF</requestId>
</DescribeDBInstanceSSLResponse>
```

`JSON` format `{`

```json
    "items": [
```

`{`

```json
            "ConnectionString": "rm-uf6wjk5xxxxxx.mysql.rds.aliyuncs.com",
            "SSLExpireTime": "2018-01-17T12:18:15Z",
            "RequireUpdate": "Yes",
            "RequireUpdateReason": ""
```

`}` `],`

```json
    "requestId": "1AD222E9-E606-4A42-BF6D-8A4442913CEF"
```

`}`

#### 2.1.22 ModifyDBInstanceSSL

Description You can call this operation to modify the SSL link of an instance. Request parameters

| Parameter | Type | Requ ired | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceSSL. |
| DBInstanceI d | Strin g | Yes | The ID of the instance. |
| ConnectionS tring | Strin g | Yes | Each instance can only have one endpoint protected by the SSL certificate. The SSL certificate can be created or updated for the endpoint. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |
| SSLExpireTime | String | The expiration time of the SSL certificate. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. |

#### 2.1.23 DescribeDBInstanceTDE

Queries the Transparent Data Encryption (TDE) status of an ApsaraDB RDS instance. This operation is available only for instances that run MySQL 5.6 or SQL Server EE.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeD BInstance TDE | The operation that you want to perform. Set the value to DescribeDBInstanceTDE. |
| DBInstanceI d | String | Yes | rm- uf6wjk5x xxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | N/A | Common response parameters. |
| TDEStatus | String | The TDE status of the instance. Valid values: Enabled and Disabled. |
| Databases | List<DataBase> | Details about the database. |

Database parameters

| Parameter | Type | Description |
|---|---|---|
| DBName | String | The name of the database. |
| TDEStatus | String | The TDE status of the database. Valid values: Enabled and Disabled. |

#### 2.1.24 ModifyDBInstanceTDE

Enables or disables the Transparent Data Encryption (TDE) feature for an ApsaraDB RDS instance. This operation is available only for instances that run MySQL 5.6, MySQL 5.7, or SQL Server 2008 R2. For instances that run MySQL 5.6 or MySQL 5.7, TDE can be enabled only on instances and cannot be disabled. You cannot specify the DBName value to modify the TDE status of a database. For instances that run SQL Server 2008 R2, TDE can be enabled or disabled only on databases. When TDE is enabled on a database, the TDE feature of the instance is enabled and cannot be disabled. Request parameters

| Parameter | Type | Requir ed | Examp le | Description |
|---|---|---|---|---|
| Action | String | Yes | Modif yDBIns tance TDE | The operation that you want to perform. Set the value to ModifyDBInstanceTDE. |

| psaraDB for RDS |   |   |   | Developer Guide·API referenc |
|---|---|---|---|---|

| Parameter | Type | Requir ed | Examp le | Description |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm- uf6wjk 5xxxxx xx | The ID of the instance. |
| TDEStatus | String | Yes | Enable d | The TDE status of the instance. Valid values: Enabled and Disabled. |
| DBName | String | No | testDB | The name of the database for which you want to enable TDE. Up to 50 names can be entered in a single request. Separate multiple names with commas (,). |

Response parameters This operation returns only common response parameters. Examples Sample requests

```
https://rds.example.com/?Action=ModifyDBInstanceTDE &DBInstanceId=rm-uf6wjk5xxxxxxx &TDEStatus=Enabled &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceTDEResponse>
      <requestId>777C4593-8053-427B-99E2-105593277CAB</requestId>
</ModifyDBInstanceTDEResponse>
```

`JSON` format `{`

```json
    "requestId": "777C4593-8053-427B-99E2-105593277CAB"
```

`}`

### 2.2 Database management

#### 2.2.1 CreateDatabase

Description You can call this operation to create a new database in an instance. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance is not locked. The maximum number of databases in the instance is not reached. The instance is a primary instance. Not e This operation is not supported on PolarDB. You can create databases in PolarDB instances by executing CREATE DATABASE statements. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateDatabase. |
| DBInstanceId | String | Yes | The ID of the instance. |
| DBName | String | Yes | The unique name of the database. The name can be up to 64 characters in length and can contain lowercase letters, digits, and underscores ( ). It must start with a letter. _ For information about invalid characters, see Forbidden keywords. |
| CharacterSet Name | String | Yes | The character set. Valid values: MySQL: utf8, gbk, latin1, and utf8mb4 SQL Server: Chinese PRC CI AS, Chinese PRC CS AS, _ _ _ _ _ _ SQL Latin1 General CP1 CI AS, _ _ _ _ _ SQL Latin1 General CP1 CS AS, and Chinese PRC BIN _ _ _ _ _ _ _ |
| DBDescription | String | No | The description of the database. It must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), and hyphens (-). _ It must start with a letter and cannot start with http:// or https://. |

Response parameters This operation returns only common response parameters. Examples Sample request s

```
https://rds.example.com/?Action=CreateDatabase &CharacterSetName=gbk &DBName=testDB &DBInstanceId=rds-xxxxx &<[Common request parameters]>
```

Sample success responses XML format

```xml
<CreateDatabaseResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CreateDatabaseResponse>
```

JSON format

```json
{ "RequestID":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 2.2.2 DeleteDatabase

Description You can call this operation to delete a database from an instance. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance is a primary instance. Not e This operation is not supported on PolarDB. You can delete databases from PolarDB instances by executing DROP DATABASE statements. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteDatabase. |
| DBInstanceI d | String | Yes | The ID of the instance. |
| DBName | String | Yes | The name of the database. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |

Examples Sample request s

```
https://rds.example.com/?Action=DeleteDatabase &DBName=testDB &DBInstanceId=rds-xxxxx &<[Common request parameters]>
```

Sample success responses XML format

```xml
<DeleteDatabaseResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </DeleteDatabaseResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 2.2.3 DescribeDatabases

Description You can call this operation to query the databases of a specified instance or information of a specified database. If the request parameters are entered incorrectly, an error prompt is returned, and the returned data is empty. Not e This operation is not supported on PolarDB. Request parameters

| Paramete r | Type | Requir ed | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDatabases. |
| DBInstanc eId | String | Yes | The ID of the instance. |
| DBName | String | No | The name of the database. |
| DBStatus | String | No | The state of the database. Valid values: Creating, Running, and Deleting. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |

| psaraDB for RDS |   | Developer Guide·API referenc |
|---|---|---|
| Parameter | Type | Description |

| Databases | List<Database> | The array that consists of Database data. |
|---|---|---|

Database parameters

| Parameter | Type | Description |
|---|---|---|
| DBName | String | The name of the database. |
| DBInstanceId | String | The ID of the instance to which the database belongs. |
| Engine | String | The engine of the database. |
| DBStatus | String | The status of the database. Valid values: Creating, Running, and Deleting. |
| CharacterSetN ame | String | The character set. |
| DBDescription | String | The description of the database. |
| Accounts | List<AccountPrivilegeI nfo> | The array that consists of AccountPrivilegeInfo data. |
| Account | String | The name of the account. |
| AccountPrivileg e | String | The permissions of the account on the database. |

AccountPrivilegeInfo parameters

| Parameter | Type | Description |
|---|---|---|
| Account | String | The name of the account. |
| AccountPrivilege | String | The permissions of the account on the database. |

Examples Sample request s

```
https://rds.example.com/?Action=DescribeDatabases &DBInstanceId=rds-xxxxx &<Common request parameters>
```

Sample success responses XML format

```xml
<DescribeDatabasesResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <Databases> <Database> <Engine>MySQL</Engine> <DBName>testdb</DBName> <CharacterSetName>utf8</CharacterSetName> <DBStatus>Creating</DBStatus> <DBInstanceId>rds-xxxxx</DBInstanceId> <Accounts> <AccountPrivilegeInfo></AccountPrivilegeInfo> <Accounts> </Database> </Databases> </DescribeDatabasesResponse>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC", "Databases":
    { "Database":
        [ { "Engine": "MySQL",
            "CharacterSetName": "utf8",
            "DBStatus": "Creating",
            "DBDescription": "",
            "DBInstanceId": "rds-xxxxx",
            "Accounts": { " AccountPrivilegeInfo": [] },
            "DBName": "testdb" }] }
```

`}`

#### 2.2.4 ModifyDBDescription

Description You can call this operation to modify the description of a database to facilitate user records. For example, you can modify the description of a database to Database A for Alibaba Cloud testing environment. Not e This operation is not supported on PolarDB. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyDBDescription. |
| DBInstanceId | String | Yes | The ID of the instance. |
| DBName | String | Yes | The name of the database. |

| A | psaraDB for RDS |   |   | Developer Guide·API referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| DBDescription | String | Yes | The description of the database. |

Response parameters This operation returns only common response parameters. Examples Sample request s

```
https://rds.example.com/?Action=ModifyDBDescription &DBInstanceId=rds-xxxxx &DBInstanceDescription=testDBdescribe &<Common request parameters>
```

Sample success responses XML format

```xml
<ModifyDBDescriptionResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyDBDescriptionResponse>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

### 2.3 Account management

#### 2.3.1 CreateAccount

Description In the same instance, one account can manage multiple databases by using different permissions. You can call this operation to create an account for a database. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The database is in the running state. The instance is not locked. The maximum number of accounts for a single instance is not reached.

| Parameter | Type | Requi red | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to CreateAccount. |
| DBInstanceId | Strin g | Yes | The ID of the instance. |
| AccountName | Strin g | Yes | The unique name of the account. The name can be up to 16 characters in length and can contain lowercase letters, digits, and underscores ( ). It must start with a letter. For information about invalid _ characters, see Forbidden keywords. |
| AccountPassw ord | Strin g | Yes | The password for the account. It must be 6 to 32 characters in length and can contain letters, digits, and underscores ( ). _ |
| AccountType | Strin g | No | The type of the account. Valid values: Normal and Super. Default value: Normal. PolarDB can have only a single initial account. You must use the initial account to log on to the database and create other types of accounts. |
| AccountDescri ption | Strin g | No | The description of the account. It must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), and hyphens (-). _ It must start with a letter and cannot start with http:// or https://. |

Response parameters This operation returns only common response parameters. Examples Sample request s

```
https://rds.example.com/?Action=CreateAccount &AccountName=testacc02 &AccountPassword=pwxxxxx &DBInstanceId=rds-xxxxx &<[Common request parameters]>
```

Sample success responses XML format

```xml
<CreateAccountResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CreateAccountResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 2.3.2 DeleteAccount

Description You can call this operation to delete a database account. The instance must be in the running state. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteAccount. |
| DBInstanceId | String | Yes | The ID of the instance to which the database belongs. |
| AccountNam e | String | Yes | The unique name of the account. The name can be up to 16 characters in length and can contain lowercase letters, digits, and underscores ( ). It must start with a letter. For more _ information about invalid characters, see Forbidden keywords. |

Response parameters This operation returns only common response parameters. Examples Sample request s

```
https://rds.example.com/?Action=DeleteAccount &DBInstanceId=rds-xxxxx &AccountName=testacc01 &<[Common request parameters]>
```

Sample responses XML format

```xml
<DeleteAccountResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </DeleteAccountResponse>
```

JSON format

```json
{ "RequestID":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 2.3.3 DescribeAccounts

Description You can call this operation to query the accounts for a specified instance and database or the information of a specified account.

| Parameter | Typ e | Required | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to DescribeAccounts. |
| DBInstanceI d | Strin g | Yes | The ID of the instance. |
| AccountNa me | Strin g | Yes | The name of the account. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | Common response parameters. |
| Accounts | List<DBInstanceAccount> | The array that consists of DBInstanceAccount data. |

DBInstanceAccount parameters

| Parameter | Type | Description |
|---|---|---|
| DBInstanceId | String | The ID of the instance to which the account belongs. |
| AccountName | String | The name of the database account. |
| AccountStatus | String | The account status. Valid values: Unavailable and Available. |
| AccountDescription | String | The description of the account. |
| DatabasePrivileges | List<DatabasePrivileg e> | The array that consists of DatabasePrivileges data. |
| AccountType | String | The type of the account. Valid values: Normal and Super. |

DatabasePrivilege parameters

| Parameter | Type | Description |
|---|---|---|
| DBName | String | The name of the database. |
| AccountPrivilege | String | The name of the database account. |

Examples Sample request s

```
https://rds.example.com/?Action=DescribeAccounts &DBInstanceId=rds-xxxxx &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeAccountsResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <Accounts> <DBInstanceAccount> <AccountName>MySQL</AccountName> <DBInstanceId>testdb</DBInstanceId> <AccountStatus>utf8</AccountStatus> <AccountDescription> </AccountDescription> <DatabasePrivileges> <DatabasePrivilege></DatabasePrivilege> </DatabasePrivileges> <DBInstanceAccount> </Accounts> </DescribeAccountsResponse>
```

JSON format

```json
{ "Accounts":
    { "DBInstanceAccount":
        [ { "AccountDescription": "",
            "DBInstanceId": "rds-xxxxx",
            "DatabasePrivileges": { "DatabasePrivilege": [] },
            "AccountStatus": "Unavailable",
            "AccountName": "testaccount" } ] },
    "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 2.3.4 GrantAccountPrivilege

Grants database permissions to an account. The instance must be in the running state. Not e An account can be authorized to access one or more databases. If the specified account already has access permissions on the specified database, the operation directly returns a successful response. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GrantAcc ountPrivi lege | The operation that you want to perform. Set the value to GrantAccountPrivilege. |
| DBInstanceId | String | Yes | rm- uf6wjk5x xxxxxx | The ID of the instance. |
| AccountName | String | Yes | test1 | The name of the account. |
| DBName | String | Yes | testDB | The name of the database to be accessed by the account. |
| AccountPrivile ge | String | Yes | ReadOnl y | The permissions of the database account. Valid values: ReadOnly ReadWrite |

Response parameters This operation returns only common response parameters. Examples Sample request s

```
https://rds.example.com/?Action=GrantAccountPrivilege &AccountName=testacc02 &AccountPrivilege=readwrite &DBName=testdb03 &DBInstanceId=rds-xxxxx &<Common request parameters>
```

Sample success responses XML format

```xml
<GrantAccountPrivilegeResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </GrantAccountPrivilegeResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.3.5 RevokeAccountPrivilege

Revokes database permissions of an account. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The database is in the running state.

| Parameter | Type | Requir ed | Exam ple | Description |
|---|---|---|---|---|
| Action | Strin g | Yes | Revo keAc coun tPrivil ege | The operation that you want to perform. Set the value to RevokeAccountPrivilege. |
| DBInstanc eId | Strin g | Yes | rm- uf6w jk5xx xxxxx | The ID of the instance. |
| AccountN ame | Strin g | Yes | test1 | The name of the account. |
| DBName | Strin g | Yes | testD B | The name of the database. |

Response parameters This operation returns only common response parameters. Examples Sample request s

```
https://rds.example.com/?Action=RevokeAccountPrivilege &AccountName=testacc02 &DBName=testdb03 &DBInstanceId=rds-xxxxx &<Common request parameters>
```

Sample success responses XML format

```xml
<RevokeAccountPrivilegeResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </RevokeAccountPrivilegeResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.3.6 ModifyAccountDescription

You can call this operation to modify the description of an account to facilitate user records. For example, you can modify the description of an account to Account A for Alibaba Cloud testing environment. Request parameters

| Parameter | Typ e | Required | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to ModifyAccountDescription. |
| DBInstanceId | Strin g | Yes | The ID of the instance for which the account description is modified. |
| AccountName | Strin g | Yes | The unique name of the account. The name can be up to 16 characters in length and can contain lowercase letters, digits, and underscores ( ). It must start with a letter. For more information _ about invalid characters, see Forbidden keywords. |
| AccountDescri ption | Strin g | Yes | The description of the account. It can be up to 256 characters in length and can contain letters, digits, underscores ( ), and hyphens _ (-). It cannot start with http:// or https://. It must start with a letter. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |

Examples Sample request s

```
https://rds.example.com/?Action=ModifyAccountDescription &DBInstanceId=rds-xxxxx &AccountName=testacc01 &AccountDescription=testAccoutdescribe &<Common request parameters>
```

Sample responses XML format

```xml
<ModifyAccountDescription> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyAccountDescription>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.3.7 ResetAccountPassword

Resets the password of an account on an ApsaraDB RDS instance. Description Before you call this operation, make sure that the following requirements are met: The instance is in the running state and not locked by the system. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ResetAccountPas sword | The operation that you want to perform. Set the value to Reset Account Password. |
| AccountName | String | Yes | test1 | The name of the account. |
| AccountPassword | String | Yes | Test123456 | The new password for the account. Not e The password must be 8 to 32 characters in length. The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include !@ # $ & ; % ^ * ( ) + - = _ |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |

Response parameters This operation returns only common response parameters. Examples Sample request s

```
https://rds.example.com/?Action=ResetAccountPassword &AccountName=testacc02 &AccountPassword=pwxxxxx &DBInstanceId=rds-xxxxx &<Common request parameters>
```

Sample success responses XML format

```xml
<ResetAccountPasswordResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ResetAccountPasswordResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.3.8 ResetAccount

Description You can call this operation to reset the initial account of an instance. Request parameters

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ResetAccount. |
| DBInstanceId | String | Yes | The ID of the instance. |
| AccountNam e | String | Yes | The name of the account. |
| AccountPass word | String | Yes | The password of the account. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |

### 2.4 Backup and restoration

#### 2.4.1 CreateBackup

You can call this operation to manually create a backup. Up to 10 backups can be created for an instance in a single day. Before you call this operation, ensure that the following requirements are met: The instance is in the running state. The most recent backup has been completed. Request parameters

| Parameter | Type | Requ ired | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateBackup. |
| DBInstance Id | String | Yes | The ID of the instance. |
| BackupMet hod | String | No | The backup method. Valid values: Logical and Physical. Default value: Physical. Logical backup cannot be used for instances without databases. SQL Server instances only support physical backup. |
| BackupStr ategy | String | No | The logical backup range. Valid values: db: single-database backup. instance: instance backup. This parameter is valid only when BackupMethod is set to Logical. |
| DBName | String | No | The name of the database for logical single-database backup. This parameter is valid only when BackupMethod is set to Logical and BackupStrategy is set to db. |
| BackupTyp e | String | No | The backup type. Valid values: Auto: specifies whether it is a full backup or an incremental backup through automatic calculation. FullBackup: specifies a full backup. Default value: Auto. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | N/A | Common response parameters. |

Examples Sample request s

```
https://rds.example.com/?Action= CreateBackup &DBInstanceId=rds-xxxxx &<Common request parameters>
```

Sample success responses XML format

```xml
<CreateBackupResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CreateBackupResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.4.2 CloneDBInstance

Restores the data of an original ApsaraDB RDS instance to a new instance. The new instance is called a cloned instance. Before you call this operation, make sure that the following requirements are met: The original instance is in the running state. The original instance does not have ongoing migration tasks. The log backup feature is enabled for the original instance to support point-in-time recovery. Not e The new instance has the same whitelist, SQL audit, alert threshold, backup, and parameter settings as the original instance. The data in the new instance is the same as historical data in the backup file. The clone feature is available only for instances that run MySQL. Database account information varies based on the following account types: If the original instance has a privileged account, instances that are cloned from it also carry the same privileged account information. If the original instance has only standard accounts, instances that are cloned from it also carry the information of the account used when the backup file is generated or at the specified point in time. Request parameters

| Parameter | Type | Requir ed | Exam ple | Description |
|---|---|---|---|---|
| Action | String | Yes | Clone DBIns tance | The operation that you want to perform. Set the value to CloneDBInstance. |
| DBInstanceId | String | Yes | rm- uf6wj k5xxx xxxxx xx | The ID of the instance. |

| Parameter | Type | Requir ed | Exam ple | Description |
|---|---|---|---|---|
| PayType | String | Yes | Postp aid | The billing method of the instances. Valid values: Postpaid: pay-as-you-go Prepaid: subscription |
| ClientToken | String | Yes | ETnLK lblzcz shOT UbOC zxxxx xxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| BackupId | String | No | 90262 62 | The ID of the backup set. You can call the DescribeBackups operation to query backup set IDs. |
| RestoreTime | String | No | 2011- 06- 11T1 6:00: 00Z | A point in time within the backup retention period to obtain a backup set from. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2011-06-11T16:00:00Z. You must specify at least one of BackupId and RestoreTime. |
| DBInstanceClas s | String | No | mysql .n1.mi cro.1 | Optional. The instance type of the instance. For more information, see Instance types in Appendix. If this parameter is not specified, the new instance is of the same instance type as the original instance. |
| DBInstanceStor age | String | No | 1000 | The disk space. Unit: GB. This value must be in 5 GB increments and is the same as that of the primary instance by default. Set the value to 3000 for ApsaraDB RDS instances that are of the dedicated host instance family. Valid values for ApsaraDB RDS instances that are of other instance families: 5 to 2000. |
| InstanceNetwo rkType | String | No | VPC | The network type of the new instance. Valid values: VPC Classic Not e The default value is the network type of the original instance. |
| VPCId | String | No | vpc- uf6f7l 4fg90 xxxxx xxxxx | The ID of the virtual private cloud (VPC). |

| Parameter | Type | Requir ed | Exam ple | Description |
|---|---|---|---|---|
| VSwitchId | String | No | vsw- uf6ad z52c2 pxxxx xxxxx x | The ID of the vSwitch. |
| PrivateIpAddre ss | String | No | 172.1 6.201. 69 | The internal IP address of the new instance, which must be within the CIDR block supported by the specified vSwitch. The system assigns an internal IP address based on the VPCId and VSwit chId parameters. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | N/A | Common response parameters. |
| DBInstanceId | String | The ID of the instance. |
| OrderId | Integer | The ID of the order. |

Examples Sample requests

```
https://rds.example.com/?Action=CloneDBInstance &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &PayType=Postpaid &ClientToken=ETnLKlblzczshOTUbOCzxxxxxxx &<[Common request parameters]>
```

Sample success responses XML format

```xml
<CloneDBInstanceResponse>
      <OrderId>100789370xxxxx</OrderId>
      <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
      <RequestId>1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC</RequestId>
</CloneDBInstanceResponse>
```

JSON format `{`

```json
    "OrderId": "100789370xxxxx",
    "DBInstanceId": "rm-uf6wjk5xxxxxxx",
    "RequestId": "1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC"
```

`}`

#### 2.4.3 DescribeBackups

Queries the backup sets of an ApsaraDB RDS instance. Only backup sets in the Backup Succeeded state can be used for database restoration. ApsaraDB RDS allows you to download backup files. If DownloadLink is NULL, ApsaraDB RDS does not provide a download URL. If DownloadLink is not NULL, you can use the provided URL to download backup files by using Wget (with double quotation marks), a browser, or a user program. The expiration time for this URL is specified by LinkExpiredTime. Use it before the expiration time. If the URL has expired, the following error code is displayed:

```xml
<?xml version="1.0" encoding="UTF-8" ?><Error><Code>AccessDenied</Code><Message>Request h as expired.</Message><Expires>2012-12-25T09:47:52.000Z</Expires><ServerTime>2012-12-25T09 :49:00.000Z</ServerTime><RequestId>50D9768CA801C2F102005C70</RequestId><HostId>oss-test.a liyun-inc.com</HostId></Error>
```

Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackups | The operation that you want to perform. Set the value to DescribeBackups. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| BackupId | String | No | 327329803 | The ID of the backup set. |
| BackupStatus | String | No | Success | The status of the backup set. Valid values: Success Failed |
| BackupMode | String | No | Automated | The backup mode. Valid values: Automated Manual |
| StartTime | String | No | 2011-06- 01T16:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. |
| EndTime | String | No | 2011-06- 15T16:00Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30 50 100 Default value: 30 |
| PageNumber | Integer | No | 1 | The number of the page to return. Valid values: non-zero positive integers. Default value: 1. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| TotalRecordCount | String | The total number of entries returned. |
| PageNumber | String | The page number of the returned page. |
| PageRecordCount | String | The number of backup sets on the page. |
| Items | Array | Details about the backup set. |
| Backup |   |   |
| BackupId | String | The ID of the backup set. |
| DBInstanceId | String | The ID of the instance. |
| HostInstanceID | String | The No. of the instance that generates the backup set. This parameter is used to indicate whether the primary or secondary instance generates the backup set. |
| BackupStatus | String | The status of the backup set. |
| BackupStartTime | String | The start time of the backup. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. |
| BackupEndTime | String | The end time of the backup. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. |
| BackupType | String | The backup type. Valid values: FullBackup IncrementalBackup |

| psaraDB for RDS |   | Developer Guide·API referenc |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| BackupMode | String | The backup mode. Valid values: Automated Manual |
| BackupMethod | String | The backup method. Valid values: Logical Physical |
| BackupDownloadURL | String | The URL that is used to download the backup file over the Internet. If the URL is unavailable, an empty string is returned. |
| BackupIntranetDownl oadURL | String | The URL that is used to download the backup file over an internal network. If the URL is unavailable, an empty string is returned. |
| BackupSize | Long | The size of the backup set. Unit: bytes. |
| StoreStatus | String | Indicates whether the backup set can be deleted. Valid values: Enabled: The backup set can be deleted. Disabled: The backup set cannot be deleted. |
| BackupInitiator | String | The initiator of the backup task. Valid values: System User |
| ConsistentTime | Long | The point in time at which the data in the backup set is consistent. The value of this parameter is a timestamp. Not e If the instance runs MySQL 5.6, a timestamp is returned. Otherwise, the value 0 is returned. |
| CopyOnlyBackup | String | The backup mode. Valid values: 0: the standard mode. This mode supports full backup and incremental backup. 1: the copy-only mode. This mode supports only full backup. Not e If the instance runs SQL Server, this parameter is returned. |

| Parameter | Type | Description |
|---|---|---|
| IsAvail | Integer | Indicates whether the backup set is available. Valid values: 0: unavailable 1: available |
| MetaStatus | String | The status of the backup set that is used to restore individual databases or tables. Valid values: OK: The backup set is normal. LARGE: The backup set contains an abnormally large number of tables. It cannot be used to restore individual databases or tables. EMPTY: The backup set is generated from a failed backup task. Not e If an empty string is returned, the backup set cannot be used to restore individual databases or tables. |
| StorageClass | String | The storage media that is used to store the backup set. Valid values: 0: normal storage 1: archived storage |
| RequestId | String | The ID of the request. |
| TotalEcsSnapshotSiz e | Long | The size of the snapshot chain of the instance. Unit: bytes. |

Examples Sample requests

```
https://rds.example.com/?Action=DescribeBackups &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeBackupsResponse>
  <TotalRecordCount>1</TotalRecordCount>
  <PageRecordCount>1</PageRecordCount>
  <TotalEcsSnapshotSize>0</TotalEcsSnapshotSize>
  <RequestId>B0BBC25A-6B3E-4BFD-A052-48664294E20D</RequestId>
  <PageNumber>1</PageNumber>
  <Items>
        <Backup>
              <BackupMethod>Snapshot</BackupMethod>
              <BackupInitiator>System</BackupInitiator>
              <StorageClass>0</StorageClass>
              <BackupMode>Automated</BackupMode>
              <BackupSize>161061273600</BackupSize>
              <BackupId>677987116</BackupId>
              <IsAvail>1</IsAvail>
              <HostInstanceID>9232003</HostInstanceID>
              <BackupDBNames></BackupDBNames>
              <StoreStatus>Disabled</StoreStatus>
              <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
              <BackupDownloadURL></BackupDownloadURL>
              <BackupEndTime>2020-07-11T05:07:33Z</BackupEndTime>
              <BackupStartTime>2020-07-11T05:07:33Z</BackupStartTime>
              <ConsistentTime>0</ConsistentTime>
              <BackupType>FullBackup</BackupType>
              <MetaStatus></MetaStatus>
              <BackupScale>DBInstance</BackupScale>
              <BackupStatus>Success</BackupStatus>
              <BackupLocation>OSS</BackupLocation>
        </Backup>
  </Items>
  <TotalBackupSize>161061273600</TotalBackupSize>
</DescribeBackupsResponse>
```

`JSON` format `{`

```json
    "TotalRecordCount": 1,
    "PageRecordCount": 1,
    "TotalEcsSnapshotSize": "0",
    "RequestId": "B0BBC25A-6B3E-4BFD-A052-48664294E20D",
    "PageNumber": 1,
    "Items": {
        "Backup": [
```

`{`

```json
                "BackupMethod": "Snapshot",
                "BackupInitiator": "System",
                "StorageClass": "0",
                "BackupMode": "Automated",
                "BackupSize": 161061273600,
                "BackupId": 677987116,
                "IsAvail": 1,
                "HostInstanceID": 9232003,
                "BackupDBNames": "",
                "StoreStatus": "Disabled",
                "DBInstanceId": "rm-uf6wjk5xxxxxxx",
                "BackupDownloadURL": "",
                "BackupEndTime": "2020-07-11T05:07:33Z",
                "BackupStartTime": "2020-07-11T05:07:33Z",
                "ConsistentTime": "0",
                "BackupType": "FullBackup",
                "MetaStatus": "",
                "BackupScale": "DBInstance",
                "BackupStatus": "Success",
                "BackupLocation": "OSS"
```

`}` `]` `},`

```json
    "TotalBackupSize": "161061273600"
```

`}`

#### 2.4.4 CreateTempDBInstance

Description Not e You can create a temporary instance based on a backup set or a point in time within the past seven days. When a temporary instance is created, accounts and databases inherit the backup set data. You can call this operation to create a temporary instance. Before you call this operation, ensure that the following requirements are met: The instance is in the running state. The instance is not undergoing any migration tasks. The instance is not locked by the system. The current status of the instance backup set is Success.

| Parameter | Type | Require d | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateTempDBInstance. |
| DBInstanceId | String | Yes | The ID of the instance to be created. |
| BackupId | Integer | No | The ID of the backup set. |
| RestoreTime | String | No | The restoration time of the backup set. It can be any time within the past seven days that is more than 30 minutes before the current time. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Example: 2011-06-11T16:00:00Z. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | Common response parameters. |
| TempDBInstanceId | String | The ID of the temporary instance. |

Examples Sample request s

```
https://rds.example.com/?Action=CreateTempDBInstance &BackupId=90262 &DBInstanceId=rds-xxxxx &<Common request parameters>
```

Sample responses XML format

```xml
<CreateTempDBInstanceResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <TempDBInstanceId>sub-xxxxx</TempDBInstanceId> </CreateTempDBInstanceResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC", "TempDBInstanceId":"sub-xxxxx"}
```

#### 2.4.5 DescribeBackupPolicy

You can call this operation to query the backup policy configured for the system. RDS periodically backs up an instance based on the user-defined system configuration.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeBackupPolicy. |
| DBInstanceId | String | Yes | The ID of the instance for which the backup policy is queried. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | Common response parameters. |
| BackupRetentionPerio d | String | The data backup retention period. Unit: days. Valid values: 1 to 30. |
| PreferredBackupTime | String | The backup time. The time is in the HH:mmZ to HH:mmZ format. |
| PreferredBackupPerio d | String | The backup day. Valid values: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, and Sunday. |
| BackupLog | String | The log backup status. Valid values: Enable and Disabled. |
| LogBackupRetentionP eriod | String | The log backup retention period. Unit: days. Valid values: 1 to 30. |

#### 2.4.6 ModifyBackupPolicy

Description You can call this operation to modify a backup policy. RDS periodically backs up instances based on the user-defined system configuration. Request parameters

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyBackupPolicy. |
| DBInstanceId | String | Yes | The ID of the instance for which the backup policy is modified. |
| PreferredBackupTime | String | Yes | The backup time. Format: HH:mmZ to HH:mmZ. |

| psaraDB for RDS |   |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| PreferredBackupPerio d | String | Yes | The backup day. Valid values: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, and Sunday. |
| BackupRetentionPerio d | String | No | The data backup retention period. Unit: days. Valid values: 1 to 30. Default value: 7. |
| BackupLog | String | No | The log backup status. Valid values: Enable and Disabled. Default value: Enable. |
| LogBackupRetentionP eriod | String | No | The log backup retention period. It cannot exceed BackupRetentionPeriod. Unit: days. Valid values: 1 to 30. When you enable log backup, you can configure the log backup retention period. This operation is only supported on MySQL, PostgreSQL, and PPAS. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |

Examples Sample request s

```
https://rds.example.com/?Action=ModifyBackupPolicy &DBInstanceId=rds-xxxxx &PreferredBackupTime=00:00Z—01:00Z &PreferredBackupPeriod=Monday &<Common request parameters>
```

Sample responses XML format

```xml
<ModifyBackupPolicyResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyBackupPolicyResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.4.7 RestoreDBInstance

Restores a backup set to an instance. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance is not undergoing migration tasks. The instance is not locked by the system. The backup set is in the Backup Succeeded state. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to RestoreDBInstance. |
| DBInstanceId | String | Yes | The ID of the instance. |
| BackupId | Integer | Yes | The ID of the backup set. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |

Examples Sample request s

```
https://rds.example.com/?Action=RestoreDBInstance &BackupId=103312 &DBInstanceId=rds-xxxxx &<Common request parameters>
```

Sample success responses XML format

```xml
<RestoreDBInstanceResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </RestoreDBInstanceResponse>
```

JSON format

```json
{"RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.4.8 DeleteBackup

Deletes backup sets of an instance. Backup sets of only the instance itself are deleted. Backup sets of the associated instances such as read-only, disaster recovery, and cloned instances are not deleted. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance runs MySQL, PostgreSQL, or PolarDB. If the log backup feature is disabled, ApsaraDB RDS instances cannot be restored by point in time. You can delete data backup sets that are retained for more than seven days. If the log backup feature is enabled and the retention period of log backups is less than the retention period of data backups, the data backup sets that are retained for more than the retention period of log backups can be deleted. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteBackup | The operation that you want to perform. Set the value to DeleteBackup. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| BackupId | String | Yes | 324909958 | The ID of the backup set. You can call the DescribeBackups operation to query the backup set IDs. You can enter up to 100 backup set IDs in a single request. Separate multiple IDs with commas (,). Among the query results of DescribeBackups, you can delete backup sets that are only in the enabled state. |

Response parameters This operation returns only common response parameters. Examples Sample requests

```
https://rds.example.com/?Action=DeleteBackup &DBInstanceId=rm-uf6wjk5xxxxxxx &BackupId=324909958 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteBackupResponse>
      <RequestId>37441409-FFD1-40AA-8EC5-9ECF5E2F7C29</RequestId>
</DeleteBackupResponse>
```

`JSON` format `{`

```json
    "RequestId": "37441409-FFD1-40AA-8EC5-9ECF5E2F7C29"
```

`}`

### 2.5 Monitoring management

#### 2.5.1 DescribeResourceUsage

Description You can call this operation to query the resource usage information of an instance. When this operation is called, the system returns the amount of space occupied by the specified instance. DBInstanceId is used to obtain instance resource usage information. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeResourceUsage. |
| DBInstanceId | String | Yes | The ID of the instance for which the resource usage information is queried. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | Common response parameters. |
| DBInstanceId | String | The ID of the instance for which the resource usage information was queried. |
| Engine | String | The type of the database. |
| DiskUsed | Integer | The total space occupied by both data files and log files. Unit: Byte. -1 indicates no data. |
| DataSize | Integer | The disk space that is used to store user data. Unit: Byte. -1 indicates no data. |
| LogSize | Integer | The disk space that is used to store log files. Unit: Byte. -1 indicates no data. |
| BackupSize | Integer | The total space occupied by backup data. Unit: Byte. -1 indicates no data. |

| psaraDB for RDS |   | Developer Guide·API referenc |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| ColdBackupSize | Integer | The total space occupied by cold backup data. Unit: Byte. -1 indicates no data. |
| SQLSize | Integer | The total space occupied by SQL data. Unit: Byte. -1 indicates no data. |

#### 2.5.2 DescribeDBInstancePerformance

Description You can call this operation to query the performance metrics of an instance over a specified period of time based on the performance parameters. There are three output formats based on different query time ranges: When the query time range is less than or equal to one day, performance metrics are displayed at one-minute intervals. Queries with the time range from one to seven days are not supported. When the query time range is greater than seven days but less than or equal to 15 days, performance metrics are displayed at one-hour intervals. Queries with the time range greater than 15 days but less than 30 days are not supported. When the query time range is greater than or equal to 30 days but less than or equal to one year, performance metrics are displayed at one-day intervals. Not e When the instance space usage key is MySQL_SpaceUsage or SQLServer_SpaceUsage, performance metrics can be queried only when the time range is less than or equal to one day. Request parameters

| Parameter | Type | Require d | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDBInstancePerformance. |
| DBInstanc eId | String | Yes | The ID of the instance. |
| Key | Intege r | Yes | The performance metrics. Separate performance metrics with commas (,). For more information, see Performance parameters. |
| StartTime | String | Yes | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the YYYY-MM-DDTHH:mmZ format. Example: 2012- 06-11T15:00Z. |
| EndTime | String | Yes | The end of the time range to query. Specify the time in the ISO 8601 standard in the YYYY-MM-DDTHH:mmZ format. Example: 2012-06- 11T15:00Z. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | N/A | Common response parameters |
| DBInstanceId | String | The ID of the instance. |
| Engine | String | The engine of the database. |
| StartTime | String | The beginning of the time range where the query was executed. The time follows the ISO 8601 standard in the YYYY-MM-DDTHH:mmZ format. Example: 2011-05-30T03:29Z. |
| EndTime | String | The end of the time range where the query was executed. The time follows the ISO 8601 standard in the YYYY-MM-DDTHH:mmZ format. Example: 2011- 05-30T03:29Z. The end time must be later than the start time. |
| PerformanceKeys | List<PerformanceKey> | The array that consists of PerformanceKey data. Format: {perf1, perf2, perf3, ...}. |

Examples Sample request s

```
https://rds.example.com/?Action=DescribeDBInstancePerformance &DBInstanceId=rds-xxxxx &key= MySQL_xxxxx &StartTime=2013-01-11T15:00:00Z &EndTime=2013-06-05T15:00:00Z &<Common request parameters>
```

Sample success responses XML format

```xml
<DescribeDBInstancePerformanceResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <DBInstanceID>rds-xxxxx</DBInstanceID> <StartTime>2013-01-11T15:00:00Z</StartTime> <EndTime>2013-10-17T15:00Z</EndTime> <Engine>MySQL</Engine> <PerformanceKeys> <PerformanceKey> <Key>MySQL_xxxxx</Key> <Unit>KB</Unit> <ValueFormat>recv_k&amp;sent_k</ValueFormat> <Values><Values/> </PerformanceKey> </PerformanceKeys> </DescribeDBInstancePerformanceResponse>
```

JSON format

```json
{ "RequestId"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC, "DBInstanceID": rds-xxxxx, "StartTime": "2012-06-11T15:00Z", "EndTime": "2013-10-17T15:00Z", "Engine": "MySQL", "PerformanceKeys":
    { PerformanceKey[ {
        "Key": "MySQL_xxxxx",
        "Unit": "KB",
        "ValueFormat": "recv_k&sent_k",
        "Values": { "PerformanceValue":[] } } ] }}
```

#### 2.5.3 DescribeDBInstanceMonitor

Description You can call this operation to query the monitoring behavior of an instance. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDBInstanceMonitor. |
| DBInstanceI d | String | Yes | The ID of the instance for which the monitoring behavior is queried. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |

| Developer Guide·API reference |   | ApsaraDB for RD |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| Period | String | The monitoring period. Unit: seconds. |

#### 2.5.4 ModifyDBInstanceMonitor

Changes the monitoring frequency of an ApsaraDB RDS instance. Request parameters

| Parameter | Type | Required | Exampl e | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyD BInstanc eMonito r | The operation that you want to perform. Set the value to ModifyDBInstanceMonitor. |
| DBInstanceId | String | Yes | rm- uf6wjk5 xxxxxxx | The ID of the instance. |
| Period | String | Yes | 60 | The monitoring frequency. Valid values: 60 300 Unit: seconds. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | N/A | Common response parameters. |

Examples Sample requests

```
https://rds.example.com/?Action=ModifyDBInstanceMonitor &DBInstanceId=rm-uf6wjk5xxxxxxx &Period=60 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceMonitorResponse>
      <requestId>52B9805C-432C-4ED1-83FD-2F916B6D2733</requestId>
</ModifyDBInstanceMonitorResponse>
```

`JSON` format `{`

```json
    "requestId": "52B9805C-432C-4ED1-83FD-2F916B6D2733"
```

`}`

### 2.6 Parameter management

#### 2.6.1 DescribeParameterTemplates

Description You can call this operation to query the parameter template list. The list includes parameter names, default parameter values, whether they can be modified, whether the database must be restarted for the parameters to take effect, and regular expressions acting as parameter validation rules. Request parameters

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to DescribeParameterTemplates. |
| Engine | Strin g | Yes | The engine of the database. Valid values: mysql: MySQL mssql: SQL Server PostgreSQL: PostgreSQL POLARDB: PolarDB |
| EngineVersi on | Strin g | Yes | The engine version of the database. Valid values: MySQL: 5.6 and 5.7 SQL Server: 2008 R2 PostgreSQL: 9.4 and 10.0 PolarDB: 11 |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |
| Engine | String | The engine of the database. |

|   | Developer Guide·API re | ference | ApsaraDB for RD | S |
|---|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| EngineVersion | String | The engine version of the database. |
| ParameterCount | Integer | The number of parameters. |
| Parameters | List<TemplateRecord> | The array that consists of TemplateRecord data. Format: {parameter1, parameter2, parameter3, ...}. |

Examples Sample request s

```
https://rds.example.com/?Action=DescribeParameterTemplates &Engine=MySQL &EngineVersion=5.6 &<Common request parameters>
```

Sample success responses XML format

```xml
<DescribeParameterTemplatesResponse> <Engine>mysql</Engine> <EngineVersion>5.6</EngineVersion> <ParameterCount>1</ParameterCount> <Parameters> <TemplateRecord> <CheckingCode>[0-100]</CheckingCode> <ForceRestart>True</ForceRestart> <Factor>1</Factor> <ParameterDescription>test</ParameterDescription> <ParameterName>fill factor</ParameterName> <ParameterValue>0</ParameterValue> <ForceModify>True</ForceModify> <Unit>INT</Unit> </TemplateRecord> </Parameters> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </DescribeParameterTemplatesResponse>
```

JSON format

```json
{"Engine": "mysql", "EngineVersion": "5.6", "ParameterCount":1, "Parameters":
    { "TemplateRecord": [ {
        "ParameterDescription": "test",
        "ForceRestart": "True",
        "CheckingCode": "[0-100]"
        "Factor":"1",
        "ParameterName":"fill factor",
        "ParameterValue":"0",
        "ForceModify":"True",
        "Unit":"INT" } ] },
"RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.6.2 DescribeParameters

Description You can call this operation to query the current instance parameter configuration. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeParameters. |
| DBInstanceId | String | Yes | The ID of the instance. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | N/A | Common response parameters. |
| Engine | String | The engine of the database. |
| EngineVersion | String | The engine version of the database. |
| RunningParameters | List<DBInstanceParameter> | The array that consists of running DBInstanceParameter data. Format: {parameter1,parameter2,paramete r3, ...}. |

| ConfigParameters | List<DBInstanceParameter> | The array that consists of synchronizing DBInstanceParameter data. Format: {parameter1,parameter2,paramete r3, ...}. |
|---|---|---|

DBInstanceParameter parameters

| Parameter | Type | Description |
|---|---|---|
| ParameterName | String | The name of the parameter. |
| ParameterValue | String | The value of the parameter. |
| ParameterDescription | String | The description of the parameter. |

Examples Sample request s

```
https://rds.example.com/?Action=DescribeParameters &DBInstanceId=rds-xxxxx &<Common request parameters>
```

Sample success responses XML format

```xml
<DescribeParametersResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <Engine>mysql</Engine > <EngineVersion>5.6</EngineVersion> <RunningParameters> <DBInstanceParameter> <ParameterDescription>test</ParameterDescription> <ParameterName>fill factor</ParameterName> <ParameterValue>0</ParameterValue> </DBInstanceParameter> </RunningParameters> <ConfigParameters> <DBInstanceParameter> <ParameterDescription>test1</ParameterDescription> <ParameterName>fill factor</ParameterName> <ParameterValue>50</ParameterValue> </DBInstanceParameter> </ConfigParameters> </DescribeParametersResponse>
```

JSON format

```json
{ "ConfigParameters": {
    "DBInstanceParameter": [ {
        "ParameterDescription": "test",
        "ParameterName": "fill factor",
        "ParameterValue": "50" } ] },
    "Engine": "mysql",
    "EngineVersion": "5.6",
    "RunningParameters": {
        "DBInstanceParameter": [ {
            "ParameterDescription": "test1",
            "ParameterName": "fill factor",
            "ParameterValue": "0" } ] },
    "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.6.3 ModifyParameter

Description You can call this operation to modify instance parameters. After you submit a request, RDS assigns a task to apply new parameters to the instance. If there are any parameter modifications that require the database to be restarted, RDS restarts the database. Before you call this operation, ensure that the following requirements are met: The instance is in the running state. The instance is not locked by the system. There are three types of parameter values: 1 to 65,535: indicates a numerical range. Regular identification is used to extract the minimum and maximum values. The input parameter is then verified based on the extracted minimum and maximum values. The parameter must be a multiple of a divisible factor. utf8 | gbk | latin1: indicates a set value determination rule. Regular identification is used to extract the fixed value. The input parameter is then verified based on these fixed values. Others: These must be implemented with regular expressions. Before assigning the task, RDS checks the parameter as follows:
1. Whether the parameter exist.
2. Whether the parameter can be modified.
3. Whether the parameter is valid.
If the parameter is invalid, RDS returns the 400 HTTP status code and information about the invalid parameter. Example:

```json
{"HttpStatusCode":400, "Code":"InvalidParameter.Format", "Message":"Specified parameter is not valid.[auto_increment_increment:a,character_set_c lient:41]"}
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyParameter. |
| DBInstanceId | String | Yes | The ID of the instance for which parameters are modified. |
| Parameters | String | Yes | The JSON string for the parameter and its value. The parameter value must be of the string type. {"auto increment increment":"1", _ _ "character set client":"utf8"}. _ _ |
| Forcerestart | String | No | Specifies whether to forcibly restart the database. Valid values: true and false. If a parameter can take effect only after database restart, Forcerestart must be set to true. Otherwise, the parameter modification will not take effect. Default value: false. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |

Examples Sample request s

```
https://rds.example.com/?Action=ModifyeParameter &DBInstanceId=rds-xxxxx &Parameters={"key_buffer_size":"456","character_set_client":"gbk"} &<Common request parameters>
```

Sample responses XML format

```xml
<ModifyeParameterResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyeParameterResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC",}
```

### 2.7 Log management

#### 2.7.1 DescribeSlowLogs

You can call this operation to query the slow log summary of the databases in a specified instance over a specified period of time. This operation supports paged query. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSlowLogs. |
| DBInstanc eId | String | Yes | The ID of the instance. |
| StartTime | String | Yes | The beginning of the time range to query. Specify the date in the ISO 8601 standard in the YYYY-MM-DDZ format. Example: 2011- 05-30Z. |
| EndTime | String | Yes | The end of the time range to query. The end date must be later than the start date. Specify the date in the ISO 8601 standard in the YYYY-MM-DDZ format. Example: 2011-05-30Z. |
| DBName | String | No | The name of the database. |
| SortKey | String | No | The basis on which query results are sorted. Valid values: TotalExecutionCounts: in descending order of execution times. TotalQueryTimes: in descending order of the total execution duration. TotalLogicalReads: in descending order of the total number of logical reads. TotalPhysicalReads: in descending order of the total number of physical reads. This parameter is applicable to SQL Server instances. It must be used when you query SQL Server Instances. |
| PageSize | Integer | No | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNum ber | Integer | No | The number of the page to return. Pages start from page 1. Default value: 1. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | Common response parameters. |
| Engine | String | The engine of the database. |
| StartTime | String | The beginning of the time range where the query was executed. The date follows the ISO 8601 standard in the YYYY-MM-DDZ format. Example: 2011-05-30Z. |
| EndTime | String | The end of the time range where the query was executed. The date follows the ISO 8601 standard in the YYYY-MM-DDZ format. Example: 2011-05-30Z. |
| TotalRecordCou nt | Integer | The total number of entries. |
| PageNumber | Integer | The page number of the returned page. |
| PageRecordCoun t | Integer | The number of SQL slow queries on the current page. |
| Items | List<SQLSlowL og> | The list of slow logs. |

Examples Sample request s

```
https://rds.example.com/?Action=DescribeSlowLogs &DBInstanceId=rds-xxxxx &StartTime=2011-06-11Z &EndTime=2011-12-11Z &SortKey= Totaxxxxx &<Common request parameters>
```

Sample success responses XML format

```xml
<DescribeSlowLogsResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <DBInstanceID>rds-xxxxx</DBInstanceID> <Engine>MySQL</Engine> <StartTime>2011-06-11Z</StartTime> <EndTime>2011-12-11Z</EndTime> <TotalRecordCount>1</TotalRecordCount> <PageNumber>1</PageNumber> <PageRecordCount>1</PageRecordCount> <Items> <SQLSlowLog> <SQLText>update test.zxb set id=0 limit 1</SQLText> <MySQLTotalExecutionCounts>178</MySQLTotalExecutionCounts> <MySQLTotalExecutionTimes>189</MySQLTotalExecutionTimes> <TotalLogicalReadcounts>89</TotalLogicalReadcounts> <TotalPhysicalReadcounts>90</TotalPhysicalReadcounts> <ReportTime>2013-11-12Z</ReportTime> </SQLSlowLog> </Items> </DescribeSlowLogsResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC", "StartTime":"2011-06-11Z ", "EndTime":"2011-12-11Z ", "Engine":"MySQL", "PageNumber":1, "PageRecordCount":1, "TotalRecordCount":1, "Items":{
    "SQLSlowLog":[{
        "SQLText":”update test.zxb set id=0 limit 1”,
        "MySQLTotalExecutionCounts":178,
        "MySQLTotalExecutionTimes":189,
        "TotalLogicalReadcounts":89,
        "TotalPhysicalReadcounts":90,
        "ReportTime":"2013-11-12Z " }]}}
```

#### 2.7.2 DescribeSlowLogRecords

Description You can call this operation to query the slow log details of the databases in a specified instance over a specified period of time. This operation is only supported on MySQL instances. Request parameters

| Parameter | Type | Require d | Description |
|---|---|---|---|

| Parameter | Type | Require d | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSlowLogRecords. |
| DBInstanc eId | String | Yes | The ID of the instance to which the database belongs. |
| StartTime | String | Yes | The beginning of the time range where the query is performed. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2011-06- 11T15:00Z. |
| EndTime | String | Yes | The end of the time range where the query is performed. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2011-06- 11T16:00Z. |
| DBName | String | No | The name of the database. |
| PageSize | Integer | No | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNum ber | Integer | No | The number of the page to return. Pages start from page 1 but must be equal to or smaller than the maximum Integer value. Default value: 1. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | Common response parameters. |
| Engine | String | The type of the database. |
| TotalRecordCount | Integer | The total number of entries. |
| PageNumber | Integer | The number of the page returned. |
| PageRecordCount | Integer | The number of SQL slow queries on the current page. |
| Items | List<SQLSlowRecord> | - |

SQLSlowLog parameters

| Parameter | Type | Description |
|---|---|---|
| HostAddress | String | The host address to connect the database. |
| DBName | String | The name of the database. |
| SQLText | String | The query statement. |

| psaraDB for RDS |   | Developer Guide·API referenc |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| QueryTimes | Long | The execution time of the slow query. Unit: seconds. |
| LockTimes | Long | The lock time of the slow query. Unit: seconds. |
| ParseRowCounts | Long | The number of entries parsed. |
| ReturnRowCounts | Long | The number of entries returned. |
| ExecutionStartTim e | String | The beginning of the time range where the query was executed. The time is in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2011-06-11T15:00:08Z. |

Examples Sample request s

```
https://rds.example.com/?Action=DescribeSlowLogRecords &DBInstanceId=rds-xxxxx &StartTime=2011-06-11T15:00Z &EndTime=2011-06-11T16:00Z &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeSlowLogRecordsResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <DBInstanceID>rds-xxxxx</DBInstanceID> <Engine>MySQL</Engine> <TotalRecordCount>1</TotalRecordCount> <PageNumber>1</PageNumber> <PageRecordCount>1</PageRecordCount> <Items> <SQLSlowRecord> <HostAddress>192.168.0.123</HostAddress> <DBName>test</DBName> <SQLText>update test.zxb set id=0 limit 1</SQLText> <QueryTimes>123</QueryTimes> <LockTimes>12</LockTimes> <ParseRowCounts>125</ParseRowCounts> <ReturnRowCounts>1</ReturnRowCounts> <ExecutionStartTime>2011-06-11T15:00:08Z</ExecutionStartTime> </SQLSlowRecord> </Items> </DescribeSlowLogRecordsResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC", "Engine":"MySQL", "PageNumber":1, "PageRecordCount":1, "TotalRecordCount":1, "Items":{
    "SQLSlowRecord":[{
        HostAddress:”192.168.0.123”,
        DBName:”test”,
        SQLText:”update test.zxb set id=0 limit 1”,
        QueryTimes:”123”,
        LockTimes:”12”,
        ParseRowCounts:”125”,
        ReturnRowCounts:”1”,
        ExecutionStartTime:”2011-06-11T15:00:08Z”}]}}
```

#### 2.7.3 DescribeErrorLogs

Description You can call this operation to query the error logs generated for an instance over a specified period of time. Request parameters

| Parameter | Typ e | Requir ed | Description |
|---|---|---|---|
| Action | Stri ng | Yes | The operation that you want to perform. Set the value to DescribeErrorLogs. |
| DBInstanceI d | Stri ng | Yes | The ID of the instance for which error logs are queried. |
| StartTime | Stri ng | Yes | The beginning of the time range where the query is performed. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2011-05- 30T12:10Z. |
| EndTime | Stri ng | Yes | The end of the time range where the query is performed. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2011-05-30T20:10Z. |
| PageSize | Inte ger | No | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNumb er | Inte ger | No | The number of the page to return. Pages start from page 1 but must be equal to or smaller than the maximum Integer value. Default value: 1. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | Common response parameters. |
| TotalRecordCount | Integer | The total number of entries. |
| PageNumber | Integer | The number of the page returned. |
| PageRecordCount | Integer | The number of error logs on the current page. |
| Items | List<ErrorLogs> | - |

ErrorLogs parameters

| Parameter | Type | Description |
|---|---|---|
| ErrorInfo | String | The error log information. |
| CreateTime | String | The time when the error log was generated. The time is in the yyyy-MM- ddTHH:mm:ssZ format. Example: 2011-05-30T12:11:4Z. |

Examples Sample request s

```
https://rds.example.com/?Action=DescribeErrorLogs. &DBInstanceId=rds-xxxxx &StartTime=2011-06-11T15:00Z &EndTime=2011-06-11T20:00Z &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeErrorLogsResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <TotalRecordCount>1</TotalRecordCount> <PageNumber>1</PageNumber> <PageRecordCount>1<PageRecordCount> <Items> <ErrorLog> <ErrorInfo>spid52 DBCC TRACEON 3499, server process ID (SPID) 52. This is an informationa l message only; no user action is required</ErrorInfo> <CreateTime>2013-06-04T15:00:00</CreateTime> </ErrorLog> </Items> </DescribeErrorLogsResponse>
```

JSON format

```json
{"RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC", "PageNumber":1, "TotalRecordCount":1, "PageRecordCount":1, "Items":{
    "ErrorLog":[{
        ErrorInfo:”spid52 DBCC TRACEON 3499, server process ID (SPID) 52. This is an info
rmational message only; no user action is required”,
        CreateTime:”2013-06-04T15:00:00”}]}}
```

#### 2.7.4 DescribeBinlogFiles

Description You can call this operation to query binlogs of a MySQL instance. This operation supports querying by page. RDS provides binlog files for you to download. When the DownloadLink is NULL, RDS does not provide a download URL. When DownloadLink is not NULL, you can use this URL to download the backup file through Wget (with double quotation marks), a browser, or a user program. The expiration time for this URL is specified by LinkExpiredTime. Use it before the expiration time. If the BackupSet has expired, the following error code is displayed:

```xml
<Error> <Code>AccessDenied</Code> <Message>Request has expired. </Message> <Expires>2012-12-25T09:47:52.000Z</Expires> <ServerTime>2012-12-25T09:49:00.000Z</ServerTime> <RequestId>50D9768CA801C2F102005C70</RequestId> <HostId>oss-test.aliyun-inc.com</HostId> </Error>
```

Request parameters

| Parameter | Type | Require d | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeBinlogFiles. |
| DBInstanceId | String | Yes | The ID of the instance for which binlogs are queried. |
| StartTime | String | Yes | The beginning of the time range where the query is performed. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. |
| EndTime | String | Yes | The end of the time range where the query is performed. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The end time must be later than the start time. |
| PageSize | Integer | No | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |

| psaraDB for RDS |   |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Require d | Description |
|---|---|---|---|
| PageNumber | Integer | No | The number of the page to return. Pages start from page 1 but must be equal to or smaller than the maximum Integer value. Default value: 1. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |
| TotalRecordCount | Integer | The total number of binlog files. |
| PageNumber | Integer | The number of the page returned. |
| PageRecordCount | Integer | The number of binlog files on the current page. |
| Items | List<BinLogFile> | - |

BinLogFile parameters

| Parameter | Type | Description |
|---|---|---|
| FileSize | Long | The size of a binlog file. Unit: Byte. |
| LogBeginTime | String | The beginning of the time range where the binlog was executed. |
| LogEndTime | String | The end of the time range where the binlog was executed. |
| DownloadLink | String | The HTTP-compliant download URL. If this parameter is set to NULL, no download URL exists. |
| HostInstanceID | String | The ID of the instance to which the binlog belongs. This parameter indicates whether the binlog is from the primary or secondary instance. |
| LinkExpiredTime | String | The URL expiration time. The time is in the yyyy-MM- ddTHH:mm:ssZ format. Example: 2011-06-11T15:00:00Z. |

Examples Sample request s

```
https://rds.example.com/?Action=DescribeBinlogFiles &DBInstanceId=rds-xxxxx &StartTime=2011-06-11T15:00:00Z &EndTime=2013-06-05T15:00:00Z &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeBinlogFilesResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <TotalRecordCount>1</TotalRecordCount> <PageNumber>1</PageNumber> <PageRecordCount>1<PageRecordCount> <Items> <BinLogFile> <FileSize>123</FileSize> <LogBeginTime>2013-06-01T15:00:00Z</LogBeginTime> <LogEndTime>2013-06-02T18:00:00Z</LogEndTime> <DownloadLink>http://rdslog-real.oss.aliyuncs.com/custins47742/hostins46770/mysql-bin. 00 0120.zip?spm=0.0.0.0.eMQKjs&OSSAccessKeyId=c9gzsqpauxxxxx&Expires=1384916927&Signature=07 TMgM3xxxxx</DownloadLink> <LinkExpiredTime>2013-06-09T18:00:00Z</LinkExpiredTime> </BinLogFile> </Items> </DescribeBinlogFilesResponse>
```

JSON format

```json
{ "RequestId":"66816822-CEC1-4C8D-AB26-2530A7D4DCA5", "PageNumber":1, "TotalRecordCount":1, "PageRecordCount":1, "Items":{
    "BinLogFile":[{
        FileSize:”123”,
        LogBeginTime:”2013-06-01T15:00:00Z”,
        LogEndTime:”2013-06-02T18:00:00Z”,
        DownloadLink:”http://rdslog-real.oss.aliyuncs.com/custinsxxxxx/hostinsxxxxx/mysql
-bin. 000120.zip?spm=0.0.0.0.eMQKjs&OSSAccessKeyId=c9gzsqpauxxxxx&Expires=1384916927&Sign ature=07TMgM3xxxxx”,
        LinkExpiredTime”2013-06-09T18:00:00Z”}]}}
```

#### 2.7.5 DescribeSQLCollectorPolicy

Description You can call this operation to check whether SQL collection is enabled for a specified RDS instance. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSQLCollectorPolicy. |
| DBInstanceId | String | Yes | The ID of the instance for which SQL collection is enabled or disabled. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | Common response parameters. |
| SQLCollectorStatu s | String | Indicates whether SQL collection is enabled. Valid values: Enable and Disabled. |

#### 2.7.6 ModifySQLCollectorPolicy

Description You can call this operation to enable or disable SQL collection for the specified RDS instance. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifySQLCollectorPolicy. |
| DBInstanceId | String | Yes | The ID of the instance for which SQL collection is enabled or disabled. |
| SQLCollectorS tatus | String | Yes | Specifies whether to enable SQL collection. Valid values: Enable and Disabled. |

Response parameters This operation returns only common response parameters.

#### 2.7.7 DescribeSQLLogRecords

Description You can call this operation to query the SQL audit logs generated for an instance. Request parameters

| Parameter | Typ e | Requir ed | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to DescribeSQLLogRecords. |
| DBInstanceI d | Strin g | Yes | The ID of the instance for which SQL audit logs are queried. |

| D | eveloper Guide | ·API ref | erence | ApsaraDB for RD | S |
|---|---|---|---|---|---|

| Parameter | Typ e | Requir ed | Description |
|---|---|---|---|
| Database | Strin g | No | The name of the database. All databases are selected by default. |
| User | Strin g | No | The name of the user. All users are selected by default. |
| Form | Strin g | No | The file generation form for audit logs. Valid values: File and Stream. If this parameter is set to File, only common parameters are returned, and you must call the DescribeSQLLogFiles operation to obtain the final download file address. If this parameter is set to Stream, data streams are returned. Default value: Stream. |
| QueryKeyw ords | Strin g | No | The keywords used for query. Up to 10 keywords can be entered at a time. Separate multiple keywords with spaces. |
| StartTime | Strin g | Yes | The beginning of the time range where the query is performed. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. |
| EndTime | Strin g | Yes | The end of the time range where the query is performed. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The end time must be later than the start time. |
| PageSize | Inte ger | No | The number of entries to return on each page. Valid values: 30, 50, 100, and 200. Default value: 100. |
| PageNumb er | Inte ger | No | The number of the page to return. Pages start from page 1 but must be equal to or smaller than the maximum Integer value. Default value: 1. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |
| TotalRecordCount | Integer | The total number of entries. |
| PageNumber | Integer | The number of the page returned. |
| PageRecordCount | Integer | The number of SQL logs on the current page. |
| Items | List<SQLRecord> | The array that consists of SQLRecord data. |

SQLRecord parameters

| Parameter | Type | Description |
|---|---|---|
| DBName | String | The name of the database. |
| AccountName | String | The name of the account. |

| A | psaraDB for RDS |   | Developer Guide·API referenc | e |
|---|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| HostAddress | String | The IP address of the client. |
| SQLText | String | The SQL statement. |
| TotalExecutionTimes | Long | The amount of time taken to execute the operation. Unit: microseconds. |
| ReturnRowCounts | Long | The number of entries returned. |
| ThreadID | String | The thread ID. |
| ExecuteTime | String | The execution time. The time is in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2011-05-30T12:11:20Z. |

Examples Sample request s

```
https://rds.example.com/?Action=DescribeSQLLogRecords &DBInstanceId=rds-xxxxx &StartTime=2011-06-11T15:00:00Z &EndTime=2013-06-05T15:00:00Z &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeSQLLogRecordsResponse> <PageNumber>1</PageNumber>
    <RequestId>08A3B71B-FE08-4B03-974F-CC7EA6DB1828</RequestId>
    <TotalRecordCounts>1</TotalRecordCounts>
    <SQLItems>
        <SQLItem>
            <ReturnRowCounts>34</ReturnRowCounts>
            <TotalExecutionTimes>12</TotalExecutionTimes>
            <HostAddress>192.168.xx.xx</HostAddress>
            <ExecuteTime>2011-06-11T15:00:23Z</ExecuteTime>
            <SQLText>update test.zxb set id=0 limit 1</SQLText>
            <AccountName>accounttest</AccountName>
            <DBName>test</DBName>
        </SQLItem>
    </SQLItems>
    <ItemsCounts>1</ItemsCounts>
</DescribeSQLLogRecordsResponse>
```

JSON format

```json
{"PageNumber":1,
    "RequestId":"08A3B71B-FE08-4B03-974F-CC7EA6DB1828",
    "TotalRecordCounts":1,
    "SQLItems":{
        "SQLItem":[
```

`{`

```json
                "ReturnRowCounts":34,
                "TotalExecutionTimes":12,
                "HostAddress":"192.168.xx.xx",
                "ExecuteTime":"2011-06-11T15:00:23Z",
                "SQLText":"update test.zxb set id=0 limit 1",
                "AccountName":"accounttest",
                "DBName":"test"
```

`}` `]` `},`

```json
    "ItemsCounts":1
```

`}`

#### 2.7.8 DescribeSQLLogFiles

Description You can call this operation to query SQL audit files. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSQLLogFiles. |
| DBInstanceId | String | Yes | The ID of the instance for which SQL audit files are queried. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | Common response parameters. |
| TotalRecordCount | Integer | The total number of entries. |
| PageNumber | Integer | The number of the page returned. |
| PageRecordCount | Integer | The number of entries on the current page. |
| Items | List<LogFile> | The array that consists of audit file data. |

LogFile parameters

| Parameter | Type | Description |
|---|---|---|
| FileID | Integer | The ID of an audit log file. |
| DBInstanceId | String | The ID of the instance for which SQL audit files were queried. |
| LogStatus | String | The status of SQL audit files. Valid values: Success Failed Generating |
| LogStartTime | String | The beginning of the time range where the audit log was executed. |
| LogEndTime | String | The end of the time range where the audit log was executed. |
| LogDownloadUR L | String | The file download URL. If the download URL is unavailable, this parameter will be empty. |
| LogSize | Long | The size of an audit log file. Unit: Byte. |

### 2.8 Data migration

#### 2.8.1 CreateUploadPathForSQLServer

Description You can call this operation to create the account and password of the file server and the file path. Based on this information, you can upload data files. After the upload is complete, you can migrate external data. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateUploadPathForSQLServer. |
| DBInstanceId | String | Yes | The ID of the instance. |
| DBName | String | Yes | The name of the database. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |
| InternetFtpServer | String | The IP address of the file server on the public network. |

|   | Developer Guide·API ref | erence | ApsaraDB for RD | S |
|---|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| InternetPort | Integer | The port of the file server on the public network. |
| IntranetFtpServer | String | The IP address of the file server on the internal network. |
| IntranetPort | Integer | The port of the file server on the internal network. |
| UserName | String | The username used to log on to the file server. |
| Password | String | The password used to log on to the file server. |
| FileName | String | The name of the data file with the extension. |

Examples Sample request s

```
https://rds.example.com/?Action= CreateUploadPathForSQLServer &DBInstanceId=rds-xxxxx &DBName=testdb01 &<Common request parameters>
```

Sample success responses XML format

```xml
<CreateUploadPathForSQLServerResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <InternetFtpServer>10.230.239.1</InternetFtpServer> <InternetPort>3021</InternetPort> <IntranetFtpServer></IntranetFtpServer> <UserName>userxxx</UserName> <Password>pwxxxxx</Password> <FileName>testdb01_xxxxx.bak</FileName> </CreateUploadPathForSQLServerResponse>
```

JSON format

```json
{"RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC",
 "InternetFtpServer ":"10.230.239.1",
 "InternetPort":3021,
 "IntranetFtpServer":"",
 "UserName":"userxxx",
 "Password":"pwxxxxx",
 "FileName":"testdb01_xxxxx.bak"}
```

#### 2.8.2 DescribeFilesForSQLServer

Description You can call this operation to query files on the file server. SQLServer users can obtain their accounts to upload data files to the file server by calling the CreateUploadPathForSQLServer operation. After the data files are uploaded, RDS updates their status. You can also call this operation to check whether the data files are available. If they are available, you can import data and obtain the information about the import process. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeFilesForSQLServer. |
| DBInstanceId | String | Yes | The ID of the instance for which files are queried. |
| StartTime | String | Yes | The beginning of the time range where the query is performed. Specify the time in the yyyy-MM- ddTHH:mm:ssZ format. Example: 2011-06-11T15:00Z. |
| EndTime | String | Yes | The end of the time range where the query is performed. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2011-06-11T16:00Z. The end time must be later than the start time. |
| PageSize | Integer | No | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNumber | Integer | No | The number of the page to return. Pages start from page 1 but must be equal to or smaller than the maximum Integer value. Default value: 1. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| DBInstanceId | String | The ID of the instance for which files were queried. |
| TotalRecordCount | Integer | The total number of entries. |
| PageNumber | Integer | The number of the page returned. |
| PageRecordCount | Integer | The number of SQL slow queries on the current page. |
| Items | List<SQLServerUploadFile> | - |

SQLServerUploadFile parameters

| Parameter | Type | Description |
|---|---|---|
| DBName | String | The name of the database. |

| D | eveloper Guide· | API referenc | e ApsaraDB for RD | S |
|---|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| FileName | String | The name of the data file, with the extension. |
| FileSize | Long | The size of the data file. Unit: bytes. |
| InternetFtpS erver | String | The file server. |
| InternetPort | Integer | The port of the file server on the public network. |
| IntranetFtpse rver | String | The IP address of the file server on the internal network. |
| Intranetport | Integer | The port of the file server on the internal network. |
| UserName | String | The username used to log on to the file server. |
| Password | String | The password used to log on to the file server. |
| FileStatus | String | The file status. Valid values: Unavailable, Available, NotStarted, Uploading, UploadFailed, Virus, Deleted, and Success. |
| CreationTime | String | The time when the FTP file was created. The time is in the yyyy-MM- ddThh:mmZ format. Example: 2011-05-30 T12:11:4Z. |

Examples Sample request s

```
https://rds.example.com/?Action=DescribeFilesForSQLServer &DBInstanceId=rds-xxxxx &StartTime=2014-06-11T15:00Z &EndTime=2014-06-11T16:00Z &<Common request parameter>
```

Sample responses XML format

```xml
<DescribeFilesForSQLServerResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <TotalRecordCount>1</TotalRecordCount> <PageNumber>1</PageNumber> <PageRecordCount>1</PageRecordCount> <Items> <SQLServerUploadFile> <DBName>testdb01</DBName> <FileName>testdb01_xxxxx.bak</FileName> <FileSize>1243435</FileSize> <InternetFtpServer>10.xxx. 239.1</InternetFtpServer> <InternetPort>3021</InternetPort> <IntranetFtpServer></IntranetFtpServer> <UserName>userxxx</UserName> <Password>pwxxxxx</Password> <FileStatus>Success</FileStatus> <CreationTime>2014-06-11T15:02:40Z</CreationTime> </SQLServerUploadFile> </Items> </DescribeFilesForSQLServerResponse>
```

JSON format

```json
{"PageNumber":1, "TotalRecordCount":1, "PageRecordCount":1, "Items":{
 "SQLServerUploadFile":[{
  "DBName":"testdb01",
  "FileName":"testdb01_xxxxx.bak",
  "FileSize ":"1243435",
  "InternetFtpServer":"10.xxx. 239.1",
  "InternetPort":3021,
  "IntranetFtpServer":"",
  "UserName":"userxxx",
  "Password":"pwxxxxx",
  "FileStatus":"Success",
  "CreationTime":"2014-06-11T15:02:40Z"} ]},
"RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.8.3 ImportDatabaseBetweenInstances

Description You can call this operation to migrate data from one ApsaraDB RDS instance to another. This operation is supported only on dedicated ApsaraDB RDS for MySQL instances. ApsaraDB RDS for MySQL instances support batch database migration. During migration, the source instance status changes to Migrating and the destination instance status changes to Importing Data. Database migration is performed between different instances that belong to the same user. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The database is in the running state. The destination instance is not locked by the system. The reserved storage space of the destination instance is greater than the space calculated by the following formula: Space occupied by the destination instance - Database space of the destination instance + Database space of the source instance. Databases to be migrated exist in both the source and destination instances and are activated. ApsaraDB RDS for SQL Server instances support batch database migration. During migration, the source instance status changes to Migrating and the destination instance status changes to Importing Data. Database migration is performed between different instances that belong to the same user. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The database is in the running state. The destination instance is not locked by the system. The reserved storage space of the destination instance is greater than the space calculated by the following formula: Space occupied by the destination instance - Database space of the destination instance + Database space of the source instance. Request parameters

| Parameter | Type | Require d | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ImportDatabaseBetweenInstances. |
| DBInstanceId | String | Yes | The ID of the instance. |
| SourceDBInstanc eId | String | Yes | The ID of the source instance. It cannot be the same as that of the destination instance. |
| DBInfo | String | Yes | The information of the database to be migrated. Specify this parameter in the JSON format. For ApsaraDB RDS for MySQL instances, the parameter value is an array. Example: {"DBNames":["mydb","mydb2"]}. The names of the source and destination databases must be the same. In this example, data is migrated from the mydb and mydb2 databases. These databases must exist in both the source and destination instances. |

DBInfo parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| DBNames | List | Yes | The names of databases to be migrated. Example: ["mydb","mydb2"]. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | Common response parameters. |
| ImportId | Integer | The ID of the destination instance. |

Examples Sample request s

```
https://rds.example.com/?Action=ImportDatabaseBetweenInstances &DBInstanceId=rds-xxxxx &SourceDBInstanceId=rds-xxxxx &{"DBNames":["mydb","mydb2"]} &<Common request parameters>
```

Sample success responses XML format

```xml
<ImportDatabaseBetweenInstancesResponse>
 <ImportId>2122321</ImportId>
 <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId>
 </ImportDatabaseBetweenInstancesResponse>
```

JSON format

```json
{"ImportId":2122321",
 RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.8.4 CancelImport

Description You can call this operation to cancel migration tasks from ApsaraDB RDS for MySQL instances. Migration tasks from MySQL instances can be canceled. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CancelImport. |
| DBInstanceId | String | Yes | The ID of the instance. |
| ImportId | Integer | Yes | The migration task ID. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |

Examples Sample request s

```
https://rds.example.com/?Action=CancelImport &DBInstanceId=rds-xxxxx &ImportId=127562 &<Common request parameters>
```

Sample success responses XML format

```xml
<CancelImportResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CancelImportResponse>
```

JSON format

```json
{"RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

### 2.9 Tag management

#### 2.9.1 AddTagsToResource

Description You can call this operation to bind existing or newly created tags to instances. Before you call this operation, ensure that the following requirements are met: Each tag is composed of a TagKey and a TagValue. The TagKey cannot be blank, but the TagValue can. The values of TagKey and TagValue cannot start with aliyun. The values of TagKey and TagValue are not case sensitive. The maximum length of TagKey is 64 characters and the maximum length of TagValue is 128 characters. Each instance can only be bound to a maximum of 10 tags. Each tag bound to the same instance must have a unique TagKey. If tags with duplicate TagKeys are bound to the same instance, the tag bound last overwrites the existing tag. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to AddTagsToResource. |
| RegionId | String | Yes | The region ID of the instance for which a tag is be bound. |
| DBInstanceId | String | Yes | The ID of the instance for which a tag is be bound. Up to 30 IDs can be entered in a single request. Separate multiple IDs with commas (,) Format: instance1,instance2,instance3. |
| Tags | JSON string | Yes | The tag pair to be bound. This parameter must include a TagKey, but does not need to include a corresponding TagValue. Up to five tag pairs can be entered in a single request. The TagKey is required, and TagValue is optional. Format: {“key1”:”value1”,“key2”:””}. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |

#### 2.9.2 DescribeTags

Description You can call this operation to view the bound tag information of an RDS instance belonging to the current account. This operation must meet the following requirements: If a specified instance ID is provided, all tags bound to this instance are queried and the other filter criteria are ignored. If the TagKey of a key is provided without a TagValue, the results of all tags matching the TagKey criteria are returned. If both TagKey and TagValue are provided, only the results that match both parameters are returned. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeTags. |
| RegionId | String | Yes | The region ID of the instance. |

| Developer Guid | e·API referen | ce | ApsaraDB for RD |
|---|---|---|---|

| Name | Type | Required | Description |
|---|---|---|---|
| DBInstanceI d | String | No | The name of the instance. If this parameter is provided, all the other filter criteria are ignored. |
| Tags | Json string | No | The tag pair. This parameter must include a TagKey, but does not need to include a corresponding TagValue. The TagKey cannot be blank, but the TagValue can. Format: {"key1":"value1 "}. |

Response parameters

| Name | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |
| Items | List<TagInfos> | The array that consists of tag data. |

TagInfos parameters

| Name | Type | Description |
|---|---|---|
| TagKey | String | The TagKey. |
| TagValue | String | The TagValue. |
| DBInstanceIds | List<DBInstanceId> | The IDs of instances bound to this tag. |

DBInstanceIds parameters

| Name | Type | Description |
|---|---|---|
| DBInstanceId | String | The name of the instance. |

#### 2.9.3 RemoveTagsFromResource

Description You can call this operation to unbind tags from an instance. This operation must meet the following requirements: A maximum of 10 tags can be unbound in a single request. If a tag is unbound from all of its bound instances, the tag itself is automatically deleted. If the TagKey of a key is provided without a TagValue, all tags matching the TagKey criteria are unbound.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to RemoveTagsFromResource. |
| RegionId | String | Yes | The region ID of the instance. |
| DBInstanceId | String | Yes | The name of the instance. |
| Tags | Json string | Yes | The tag pair to be unbound. This parameter must include a TagKey, but does not need to include a corresponding TagValue. The TagKey cannot be blank, but the TagValue can. Format: {"key1":"value1 "}. |

Response parameters

| Name | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |

### 2.10 RAM authorization

Use RAM for RDS resource authorization All RDS instances created through an Apsara Stack tenant account are resources owned by that account. By default, you have full operation permissions on the resources under your account. Resource Access Management (RAM) allows you to grant RAM users the access and management permissions on RDS resources owned by an Apsara Stack tenant account. If you do not need to use RAM, ignore this topic. Resource types in RAM The only type of RDS resources that can be authorized through RAM is dbinstance. The following table lists the resource description method when the resources are authorized through RAM.

| Resource | Resource description in authorization policy |
|---|---|
| Instance | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid acs:rds:$regionid:$accountid:dbinstance/ acs:rds:::dbinstance/ |

The $regionid field must be the ID of a region or an asterisk (*). The $instanceid field must be the ID of an instance or an asterisk (*). Similarly, $account-id is the numerical ID of your Apsara Stack tenant account, which can be replaced by an asterisk (*). Authorization operations in RAM In RAM, the following operations can be authorized to an RDS resource.

| Operation 1 | Operation 2 |
|---|---|
| CreateDBInstance | ModifyDBInstanceSpec |
| DeleteDBInstance | CreateReadonlyDBInstance |
| DescribeDBInstances | DescribeDBInstanceAttribute |
| SwitchDBInstanceNetType | RestartDBInstance |
| ModifyDBInstanceDescription | ModifySecurityIps |
| ModifyDBInstanceMaintainTime | UpgradeDBInstanceEngineVersion |
| PurgeDBInstanceLog | CreateDatabase |
| DeleteDatabase | DescribeDatabases |
| ModifyDBDescription | ModifyeParameter |
| DescribeParameters | DescribeOptimizeAdviceByDBA |
| DescribeOptimizeAdviceOnMissIndex | ImportDataBaseBetweenInstances |
| CancelImport | CreateAccount |
| ResetAccountPassword | GrantAccountPrivilege |
| RevokeAccountPrivilege | DescribeAccounts |
| DeleteAccount | ModifyAccountDescription |
| CreateBackup | DescribeBackups |
| CreateTempDBInstance | DescribeBackupPolicy |
| ModifyBackupPolicy | DescribeResourceUsage |
| DescribeDBInstancePerformance | DescribeSlowLogs |
| DescribeSlowLogRecords | DescribeErrorLogs |
| DescribeBinlogFiles | DescribeSQLLogReports |
| DescribeSQLLogRecords | DescribeOptimizeAdviceOnStorage |
| DescribeOptimizeAdviceOnMissPK | DescribeOptimizeAdviceOnExcessIndex |

Not e All operations except DescribeRegions and DescribeParameterTemplates can be authorized. RAM authentication rules of API operations When you call API operations to access resources as a RAM user, the RDS backend checks whether the RAM user is granted the required permissions by querying RAM. The permissions to be checked are determined by the resources used by the API operation. The following table lists the authentication rules for each API operation.

| Operation | Authentication rule |
|---|---|
| CreateDBInstance | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DeleteDBInstance | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeDBInstances | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| SwitchDBInstanceNetType | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifyDBInstanceDescription | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifyDBInstanceMaintainTime | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| PurgeDBInstanceLog | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DeleteDatabase | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifyDBDescription | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CancelImport | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ResetAccountPassword | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| RevokeAccountPrivilege | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DeleteAccount | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CreateBackup | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CreateTempDBInstance | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifyBackupPolicy | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeDBInstancePerformance | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeSlowLogRecords | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeBinlogFiles | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeSQLLogRecords | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeOptimizeAdviceOnMissPK | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |

| eveloper Guide·API reference | ApsaraDB for RD |
|---|---|

| Operation | Authentication rule |
|---|---|
| DescribeOptimizeAdviceOnMissIndex | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeParameters | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CreatePrepaidDBInstanceForChannel | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifyPrepaidDBInstanceSpec | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CreatePostpaidDBInstanceForChannel | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifyPostpaidDBInstanceSpec | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeDBInstanceAttribute | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| RestartDBInstance | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifySecurityIps | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| UpgradeDBInstanceEngineVersion | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CreateDatabase | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeDatabases | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ImportDataBaseBetweenInstances | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CreateAccount | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| GrantAccountPrivilege | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeAccounts | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifyAccountDescription | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeBackups | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeBackupPolicy | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeResourceUsage | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeSlowLogs | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeErrorLogs | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeSQLLogReports | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeOptimizeAdviceOnStorage | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeOptimizeAdviceOnExcessIndex | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeOptimizeAdviceByDBA | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |

| psaraDB for RDS | Developer Guide·API referenc |
|---|---|

| Operation | Authentication rule |
|---|---|
| ModifyeParameter | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |

### 2.11 Appendix

#### 2.11.1 Error codes on the client

##### 2.11.1.1 Common errors

| Error code | Error message | HTTP status code |
|---|---|---|
| MissingParameter | The input parameter "parameter name" that is mandatory for processing this request is not supplied. | 400 |
| InvalidParameter | The specified parameter "Action or Version" is not valid. | 400 |
| InvalidAccessKeyId.NotFou nd | The Access Key ID provided does not exist in our records. | 404 |
| IncompleteSignature | The request signature does not conform to Aliyun standards. | 400 |
| IllegalTimestamp | The input parameter "Timestamp" that is mandatory for processing this request is not supplied. | 400 |
| InvalidOwnerId | The specified OwnerId is not valid. | 400 |
| InvalidOwnerAccount | The specified OwnerAccount is not valid. | 400 |
| InvalidOwner | OwnerId and OwnerAccount can't be used at one API access. | 400 |
| Throttling | Request was denied due to request throttling. | 400 |
| InvalidAction | The specified action is not valid. | 403 |
| ActionUnauthorized | The specified action is not available for you | 403 |
| UnsupportedHTTPMethod | This http method not supported. | 403 |
| UnsupportedParameter | The parameter "<parameter name>" is not supported. | 400 |
| Forbidden.InstanceNotFou nd | The specified Instance is not found. | 404 |
| Forbidden.RAM | User not authorized to operate on the specified resource, or this API doesn't support RAM. | 403 |
| Forbedden.NotSupportRA M | This action does not support accessed by RAM mode. | 403 |

| eveloper Guide·API reference | Ap | saraDB for RD |
|---|---|---|

| Error code | Error message | HTTP status code |
|---|---|---|
| Forbidden.RiskControl | This operation is forbidden by Aliyun Risk Control system. | 403 |
| InsufficientBalance | Your account does not have enough balance. | 400 |
| Forbidden.Authentication | This operation is forbidden by Aliyun Realname Authentication system. | 403 |
| Invalid<parameter name>.ValueNotSupporte d | The specified parameter “parameter name” is not valid. | 400 |
| Invalid<parameter name>.Malformed | The specified parameter "parameter name n" is not valid. | 400 |
| InvalidParameter | The specified parameter " parameter name n " is not valid. | 400 |

##### 2.11.1.2 Specific errors

| Error code | Error message | HTTP status code |
|---|---|---|
| InvalidRegionId.NotFound | The DBInstanceId provided does not exist in our records. | 404 |
| InvalidSecurityIPList.Duplicate | The Security IP address is not in the available range or occupied. | 400 |
| InvalidSecurityIPListLength.Malformed | The quota of security ip exceeds. | 400 |
| InvalidEngineVersionInRegion.NotAvail able | The EngineVersion in the Region is not available. | 403 |
| InvaildEngineInRegion.NotAvailable | The Engine in the Region is not available. | 403 |
| InvaildDBInstanceClassInRegion.NotAv ailable | The DBInstanceClass in the Region is not available. | 403 |
| OperationDenied | The resource is out of usage. | 403 |
| RegionUnauthorized | There is no authority to create instance in the specified region. | 403 |
| QuotaExceeded.CreateInstance | The quota of create instance exceeds. | 403 |
| InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist in our records. | 404 |

| Error code | Error message | HTTP status code |
|---|---|---|
| MissingParameter | The input parameters "DBInstanceClass" and "DBInstanceStorage" all blank or no change. | 400 |
| OperationDenied.DBInstanceType | The operation is not permitted due to type of instance. | 400 |
| OperationDenied.DBInstanceStorageR educe | The operation is not permitted due to reduce storage. | 403 |
| OperationDenied.DBInstanceStatus | The operation is not permitted due to instance status. | 403 |
| DependencyViolation | The operation is not permitted due to instance mount read only or guard instance. | 403 |
| InvalidConnectionStringPrefix.Duplicat e | The connection string is not in the available range or occupied. | 400 |
| QuotaExceeded.SwitchTime | The quota of switch time exceed. | 400 |
| OperationDenied.LockMode | The operation is not permitted due to lock of instance. | 403 |
| InvalidSecurityIps.Duplicate | The quota of security ip exceeds. | 400 |
| OperationDenied.CurrentEngineVersion | The operation is not permitted due to specified current version. | 400 |
| OperationDenied.ReadOnlyDBInstance Lower | The operation is not permitted due to higher read only instance version. | 403 |
| OperationDenied.GuardDBInstanceLow er | The operation is not permitted due to higher guard instance version. | 403 |
| OperationDenied.MasterDBInstanceSta te | The operation is not permitted due to status of master instance. | 403 |
| QuotaExceeded.DBName | The quota of db exceeds. | 400 |
| InvalidDBName.Duplicate | The Security db Name is not in the available range or occupied. | 400 |
| InvalidParameter.Keyword | The specified parameter "DBName" is keyword | 400 |
| OperationDenied.DBStatus | The operation is not permitted due to status of database. | 403 |
| OperationDenied.DBInstanceEngine | The operation is not permitted due to engine of instance. | 403 |

| eveloper Guide·API reference | A | psaraDB for RD |
|---|---|---|

| Error code | Error message | HTTP status code |
|---|---|---|
| FTPServiceUnavailable | The request has failed due to a temporary failure of the FTP server. | 403 |
| QuotaExceeded.Upload | The quota of file exceeds. | 403 |
| InvalidFileName.NotCompleted | The specified "FileName" is not completed. | 404 |
| InvalidFileName.NotAvailable | The specified "FileName" is not Available. | 404 |
| QuotaExceeded.FileSize | The quota of file size exceeds. | 403 |
| QuotaExceeded.DBInstanceStorage | The quota of instance storage exceeds. | 403 |
| InvalidDBInfo.Malformed | The specified parameter "DBInfo" is not valid or db not exist. | 400 |
| OperationDenied.Region | The operation is not permitted due to different region. | 403 |
| OperationDenied.Engine | The operation is not permitted due to different engine. | 403 |
| OperationDenied.DBInstanceId | The operation is not permitted due to DBInstanceId and SourceDBInstanceId is same. | 403 |
| InvalidTaskId.NotFound | The ImportId provided does not exist in our records. | 400 |
| OperationDenied.IncorrectTaskStatus | The operation is not permitted due to status of import. | 403 |
| InvalidAccountName.keyword | The specified parameter "AccountName" is a keyword. | 400 |
| InvalidAccountName.Duplicate | The Security db Name is not in the available range or occupied. | 400 |
| QuotaExceeded.AccountName | The quota of account exceeds. | 403 |
| OperationDenied.AccountStatus | The operation is not permitted due to status of account. | 403 |
| InvalidDBName.NotFound | The DBName provided does not exist in our records. | 404 |
| OperationDenied.AccountType | The operation is not permitted due to type of account. | 403 |
| OperationDenied.BackupJobExists | The operation is not permitted due to backup job exist. | 403 |

| A | psaraDB for RDS | Developer Guid | e·API referenc | e |
|---|---|---|---|---|

| Error code | Error message | HTTP status code |
|---|---|---|
| OperationDenied.NoDatabase | The operation is not permitted due to no database. | 403 |
| InvalidStartTimeAndEndTime.Malform ed | The end time must be greater than the start time | 400 |
| OperationDenied.BackupJobExists | The operation is not permitted due to backup job exist. | 403 |
| InvalidBackupId.NotFound | The BackupId provided does not exist in our records. | 404 |
| OperationDenied.NotFoundBackup | The operation is not permitted due to no backup. | 403 |
| OperationDenied.BackupStatus | The operation is not permitted due to type of backup. | 403 |
| OperationDenied.BackupMethod | The operation is not permitted method of backup. | 403 |
| OperationDenied.TempDBInstanceExis ts | The operation is not permitted due to temp instance exist. | 403 |
| Forbidden.Authentication | The operation is forbidden by Aliyun Realname Authentication System. | 403 |
| IncorrectDBInstanceConnType | Current DB instance conn type does not support this operation. | 404 |
| IncorrecttVpcId.Mismatch | The specified parameter "VpcId" is not valid. | 400 |
| IntranetNetTypeNotExists | Current DB instance net type does not support this operation. | 404 |
| InvalidDBInstanceName.NotFound | The DBInstanceId provided does not exist in our records. | 403 |
| InvalidConnectionMode.ValueNotSupp orted | The specified parameter "ConnectionMode" is not valid. | 400 |
| InvalidConnectionString.Duplicate Specified | connection string already exists in the Aliyun RDS. | 403 |
| InvalidConnectionString.Duplicate Specified | connection string or port want to be modified is the same with current net type. | 400 |
| InvalidConnectionStringPrefix.Duplicat ed | Specified connection string already exists in the Aliyun RDS. | 403 |
| InvalidCurrentConnectionString.NotFo und | Specified current connection string doesn't exist. | 400 |

| D | eveloper Guide·API reference | A | psaraDB for RD | S |
|---|---|---|---|---|

| Error code | Error message | HTTP status code |
|---|---|---|
| InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist in our records. | 400 |
| InvalidDBInstanceId.QuotaExceeded | The quota of instance id exceeds. | 400 |
| InvalidDBInstanceNetType.NotFound | The Specified DB instance net type is not found. | 404 |
| InvalidDBinstanceNetType.ValueNotSu pport | The specified parameter "DBinstanceNetType" is not valid. | 400 |
| InvalidDBInstanceType.ValueNotSupp ort | The specified parameter "DBInstanceType" is not valid. | 400 |
| InvalidEngineVersion.Malformed | The specified parameter "EngineVersion" is not valid. | 400 |
| InvalidInstanceNetworkType.ValueNot Supported | The specified parameter "InstanceNetworkType" is not valid. | 400 |
| InvalidParameter | The specified parameter "dbInstanceId" is not valid. | 400 |
| InvalidPort.Malformed | Specified port is not valid. | 400 |
| InvalidPrivateIpAddress.Duplicated | Specified private IP address is duplicated. | 400 |
| InvalidPrivateIpAddress.Mismatch | Specified private IP address is not in the CIDR block of virtual switch. | 400 |
| InvalidVPCId.NotFound | Specified virtual vpc is not found. | 400 |
| InvalidVSwitchId.Mismatch | Specified instance and virtual switch are not in the same zone. | 400 |
| InvalidVSwitchId.NotFound | Specified virtual switch is not found in specified VPC. | 400 |
| NetTypeExists | Specified net type already existed. | 400 |
| NetTypeExists | Specified public net type already existed. | 403 |
| OperationDenied.DBInstanceNetType | The operation is not permitted due to net type of instance. | 403 |
| OperationDenied.DBInstanceStatus | The operation is not permitted due to status of instance. | 403 |
| OperationDenied.DBInstanceType | The operation is not permitted due to type of instance. | 403 |

| psaraDB for RDS | Developer Guid | e·API referenc |
|---|---|---|

| Error code | Error message | HTTP status code |
|---|---|---|
| OperationDenied.LockMode | The operation is not permitted due to lock of instance. | 403 |
| OperationDenied.Switch | Specified instance cannot be switched. | 400 |
| OperationDenied.Switch | Specified instance cannot be switched to VPC. | 403 |
| OperationDenied.SwitchToVPC | Specified instance cannot be switched to VPC. | 403 |
| OperationDenied | The resource is out of usage. | 403 |
| OperationDenied | The vpc cloudinstanceIp is use, please check params. | 406 |
| OperationDenied | The vpc service is error, please check params. | 400 |
| PARAMETER ERROR _ | The vpc request parameter may not be null. | 406 |
| PARAMETER MUST NOT NULL _ _ _ | The parameter must not be null. | 406 |
| PublicConnectionExists | PublicConnection exists. | 403 |
| bpcIzNoNotEqualsRdsMultIzNo | Specified vpc IzNo not equal rds IzNo. | 400 |
| OperationDenied.DBInstanceStatus | The operation is not permitted due to status of instance. | 403 |
| OperationDenied.DBInstanceType | The operation is not permitted due to type of instance. | 403 |
| OperationDenied.LockMode | The operation is not permitted due to lock of instance. | 403 |
| OperationDenied.Switch | Specified instance cannot be switched. | 400 |
| OperationDenied.SwitchToVPC | Specified instance cannot be switched to VPC. | 403 |
| OperationDenied | The resource is out of usage. | 403 |
| OperationDenied | The vpc cloudinstanceIp is use, please check params. | 406 |
| OperationDenied | The vpc service is error, please check params. | 400 |
| PARAMETER ERROR _ | The vpc request parameter may not be null. | 406 |
| PARAMETER MUST NOT NULL _ _ _ | The parameter must not be null. | 406 |
| PublicConnectionExists | PublicConnection exists. | 403 |

| eveloper Guide·API reference | A | psaraDB for RD |
|---|---|---|

| Error code | Error message | HTTP status code |
|---|---|---|
| bpcIzNoNotEqualsRdsMultIzNo | Specified vpc IzNo not equal rds IzNo. | 400 |

#### 2.11.2 Error codes on the server

| Error code | Error message | HTTP status code |
|---|---|---|
| ServiceUnavailable | The request has failed due to a temporary failure of the server. | 503 |
| InternalError | The request processing has failed due to some unknown error, exception or failure. | 500 |

#### 2.11.3 Instance states

| State | Description |
|---|---|
| Creating | An instance is being created. |
| Running | An instance is in the running state. |
| Deleting | An instance is being deleted. |
| Rebooting | An instance is being restarted. |
| DBInstanceClassChanging | An instance is being upgraded or downgraded. |
| TRANSING | Data is being migrated. |
| EngineVersionUpgrading | Engine version is being upgraded. |
| TransingToOthers | Data is being migrated to other RDS instances. |
| GuardDBInstanceCreating | A disaster recovery instance is being created. |
| Restoring | A backup is being restored. |
| Importing | Data is being imported. |
| ImportingFromOthers | Data is being imported from other RDS instances. |
| DBInstanceNetTypeChanging | The network type is being switched between Intranet and Internet. |
| GuardSwitching | The instance is undergoing disaster recover failover. |
| INS CLONING _ | The instance is being cloned. |

#### 2.11.4 Performance parameters

ApsaraDB RDS for MySQL

| API parameter | Description |
|---|---|
| MySQL NetworkTraffic _ | The average inbound traffic to a MySQL instance per second and average outbound traffic from a MySQL instance per second. Unit: KB. |
| MySQL QPSTPS _ | The average number of SQL statements executed per second and average number of transactions per second. |
| MySQL Sessions _ | The number of active connections and total number of current connections. |
| MySQL InnoDBBufferRatio _ | The read hit rate of the InnoDB buffer pool, utilization of the InnoDB buffer pool, and percentage of dirty data blocks in the InnoDB buffer pool. |
| MySQL InnoDBDataReadWrit _ en | The average volume of data that InnoDB reads per second and average volume of data that InnoDB writes per second. Unit: KB. |
| MySQL InnoDBLogRequests _ | The average number of reads from the InnoDB buffer pool per second and average number of writes to the InnoDB buffer pool per second. |
| MySQL InnoDBLogWrites _ | The average number of log write requests per second, average number of physical writes performed on log files per second, and average number of fsync() writes to log files per second. |
| MySQL TempDiskTableCreat _ es | The number of temporary tables automatically created in the hard disk when MySQL statements are executed. |
| MySQL MyISAMKeyBufferRati _ o | The average key buffer utilization of MyISAM per second, average key buffer read hit rate of MyISAM per second, and average key buffer write hit rate of MyISAM per second. |
| MySQL MyISAMKeyReadWrite _ s | The average number of data reads from the buffer pool by MyISAM per second, average number of data writes to the buffer pool by MyISAM per second, average number of data reads from the hard disk by MyISAM per second, and average number of data writes to the hard disk by MyISAM per second. |
| MySQL COMDML _ | The average number of DELETE statements executed per second, average number of INSERT statements executed per second, average number of INSERT SELECT statements executed per second, average number of _ REPLACE statements executed per second, and average number of REPLACE SELECT statements executed per second, average number of _ SELECT statements executed per second, and average number of UPDATE statements executed per second. |
| MySQL RowDML _ | The average number of rows read from the InnoDB table per second, average number of rows updated in the InnoDB table per second, average number of rows deleted from the InnoDB table per second, average number of rows inserted into the InnoDB table per second, and average number of physical writes to log files per second. |

| API parameter | Description |
|---|---|
| MySQL MemCpuUsage _ | The CPU utilization and memory usage of a MySQL instance within the entire operating system. |
| MySQL IOPS _ | The IOPS of a MySQL instance. |
| MySQL DetailedSpaceUsage _ | The disk space occupied by a MySQL instance, including ins size (total _ space), data size (data space), log size (log space), tmp size (temporary _ _ _ space), and other size (system space). _ |
| slavestat | The latency of read-only instances. |

ApsaraDB RDS for SQL Server

| API parameter | Description |
|---|---|
| SQLServer Transactions _ | The average number of transactions per second. |
| SQLServer Sessions _ | The total number of current connections. |
| SQLServer BufferHit _ | The buffer hit rate. |
| SQLServer FullScans _ | The average number of full table scans per second. |
| SQLServer SQLCompilations _ | The number of SQL compilations per second. |
| SQLServer CheckPoint _ | The number of checkpoints written to pages per second. |
| SQLServer Logins _ | The number of logons per second. |
| SQLServer LockTimeout _ | The number of lock timeouts per second. |
| SQLServer Deadlock _ | The number of deadlocks per second. |
| SQLServer LockWaits _ | The number of lock waits per second. |
| SQLServer NetworkTraffic _ | The average inbound/outbound traffic to/from an SQL Server instance per second. Unit: KB. |
| SQLServer QPS _ | The average number of SQL statements executed per second. |
| SQLServer InstanceCPUUsage _ | The CPU utilization of an SQL Server instance within the entire operating system. |
| SQLServer IOPS _ | The IOPS of an SQL server instance. |
| SQLServer SpaceUsage _ | The space usage of an SQL Server instance within the entire operating system. |

#### 2.11.5 Forbidden keywords

ApsaraDB RDS for MySQL

| Parameter field | Keyword description |
|---|---|
| DBName/ AccountName | admin, aurora, replicator, xtrabak, root(MySQL5.5/5.6), mysql, test, eagleye, information schema, guest, add, analyze, asc, between, blob, call, c _ hange,check,condition,continue,cross,current timestamp,database,day microsecon _ _ d,dec,default,desc,distinct,double,e ach,enclosed,exit,fetch,float8,foreign,goto,having,hour minute,ignore,infile,insensiti _ ve,int1,int4,interval,iterate,keys,lea ding,like,lines,localtimestamp,longblob,low priority,mediumint,minute microsecon _ _ d,modifies,no write to binlog,on, _ _ _ optionally,out,precision,purge,read,references,rename,require,revoke,schema,select ,set,spatial,sqlexception,sql big re _ _ sult,ssl,table,tinyblob,to,true,unique,update,using,utc timestamp,varchar,when,wit _ h,xor,all,and,asensitive,bigint,both,c ascade,char,collate,connection,convert,current date,current user,databases,day mi _ _ _ nute,decimal,delayed,describe,dis tinctrow,drop,else,escaped,explain,float,for,from,grant,high priority,hour second,in _ _ ,inner,insert,int2,int8,into,join,kill,le ave,limit,load,lock,longtext,match,mediumtext,minute second,natural,null,optimize _ ,or,outer,primary,raid0,reads,regex p,repeat,restrict,right,schemas,sensitive,show,specific,sqlstate,sql calc found row _ _ _ s,starting,terminated,tinyint,trailing, undo,unlock,usage,utc date,values,varcharacter,where,write,year month,alter,as,be _ _ fore,binary,by,case,character,colu mn,constraint,create,current time,cursor,day hour,day second,declare,delete,deter _ _ _ ministic,div,dual,elseif,exists,false, float4,force,fulltext,group,hour microsecond,if,index,inout,int,int3,integer,is,key,lab _ el,left,linear,localtime,long,loop,me diumblob,middleint,mod,not,numeric,option,order,outfile,procedure,range,real,rele ase,replace,return,rlike,second mi _ crosecond,separator,smallint,sql,sqlwarning,sql small result,straight join,then,tinyt _ _ _ ext,trigger,union,unsigned,use,utc _ time,varbinary,varying,while,x509,zerofill,galaxy |

ApsaraDB RDS for SQL Server

| Parameter field | Keyword description |
|---|---|

| Parameter field | Keyword description |
|---|---|
| DBName/ AccountName | root,admin,eagleye,master,aurora,sa,sysadmin,administrator,mssqld,public,securityadmi n,serveradmin,setupadmin,pr ocessadmin,diskadmin,dbcreator,bulkadmin,tempdb,msdb,model,distribution,mssqlsyst emresource,guest,add,except, percent,all,exec,plan,alter,execute,precision,and,exists,primary,any,exit,print,as,fetch,pro c,asc,file,procedure,authorizati on,fillfactor,public,backup,for,raiserror,begin,foreign,read,between,freetext,readtext,bre ak,freetexttable,reconfigure,br owse,from,references,bulk,full,replication,by,function,restore,cascade,goto,restrict,case, grant,return,check,group,rev oke,checkpoint,having,right,close,holdlock,rollback,clustered,identity,rowcount,coalesce,i dentity insert,rowguidcol,coll _ ate,identitycol,rule,column,if,save,commit,in,schema,compute,index,select,constraint,inn er,session user,contains,insert, _ set,containstable,intersect,setuser,continue,into,shutdown,convert,is,some,create,join,st atistics,cross,key,system user, _ current,kill,table,current date,left,textsize,current time,like,then,current timestamp,linen _ _ _ o,to,current user,load,top,cur _ sor,national,tran,database,nocheck,transaction,dbcc,nonclustered,trigger,deallocate,not, truncate,declare,null,tsequal, default,nullif,union,delete,of,unique,deny,off,update,desc,offsets,updatetext,disk,on,us e,distinct,open,user,distributed, opendatasource,values,double,openquery,varying,drop,openrowset,view,dummy,openx ml,waitfor,dump,option,when, else,or,where,end,order,while,errlvl,outer,with,escape,over,writetext,galaxy |

#### 2.11.6 Instance types

Instances of different editions, versions, and instance types each perform differently from one another. ApsaraDB RDS for MySQL instance types

| RDS edition | Instance family | Instance type | CPU and memory | Maxim um conne ctions | Maxim um IOPS | Storage capacity | Zone- disaster recovery deploy ment |
|---|---|---|---|---|---|---|---|

| RDS edition | Instance family | Instance type | CPU and memory | Maxim um conne ctions | Maxim um IOPS | Storage capacity | Zone- disaster recovery deploy ment |
|---|---|---|---|---|---|---|---|
| High- availabili ty Edition | Dedicate d (X8) | 5.6, 5.7, and 8.0 mysql.x8.medium.2 | 2 cores, 16 GB | 2,500 | 4,500 | 50−1,000 GB (in 5 GB increments) | Single- data center deploy ment and dual- data center deploy ment |
|   |   | 5.6, 5.7, and 8.0 mysql.x8.large.2 | 4 cores, 32 GB | 5,000 | 9,000 | 50–1,000 GB (in 5 GB increments) |   |
|   |   | 5.6, 5.7, and 8.0 mysql.x8.xlarge.2 | 8 cores, 64 GB | 10,000 | 18,00 0 | 500–3,000 GB (in 5 GB increments) |   |
|   |   | 5.6, 5.7, and 8.0 mysql.x8.2xlarge.2 | 16 cores, 128 GB | 20,000 | 36,00 0 | 500–3,000 GB (in 5 GB increments) |   |
|   |   | 5.6, 5.7, and 8.0 mysql.x8.4xlarge.2 | 32 cores, 256 GB | 40,000 | 72,00 0 | 1,000–6,000 GB |   |
|   |   | 5.6, 5.7, and 8.0 mysql.x8.8xlarge.2 | 64 cores, 512 GB | 80,000 | 144,0 00 |   |   |
|   | Dedicate | 5.6, 5.7, and 8.0 mysql.x4.large.2 | 4 cores, 16 GB | 2,500 | 4,500 | 50−1,000 GB (in 5 GB increments) |   |
|   |   | 5.6, 5.7, and 8.0 mysql.x4.xlarge.2 | 8 cores, 32 GB | 5,000 | 9,000 | 500–3,000 GB (in 5 GB increments) |   |

|   |   | rence Apsa |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
| RDS edition | d (X4) Instance family | Instance type | CPU and memory | Maxim um conne ctions | Maxim um IOPS | Storage capacity | Zone- disaster recovery deploy ment |
|   |   | 5.6, 5.7, and 8.0 mysql.x4.2xlarge.2 | 16 cores, 64 GB | 10,000 | 18,00 0 | 500–3,000 GB (in 5 GB increments) |   |
|   |   | 5.6, 5.7, and 8.0 mysql.x4.4xlarge.2 | 32 cores, 128 GB | 20,000 | 36,00 0 | 500–3,000 GB (in 5 GB increments) |   |
|   | Dedicate d host | 5.6, 5.7, and 8.0 rds.mysql.st.v52 | 90 cores, 720 GB | 150,00 0 | 140,0 00 | 1,000–6,000 GB |   |
|   |   | 5.6 and 5.7 rds.mysql.st.h43 | 60 cores, 470 GB | 150,00 0 | 120,0 00 |   |   |
|   | Dedicate d (with a large number of cores) | 5.7 mysql.x4.large.25 | 4 cores, 16 GB | 2,500 | 4,500 | 50−1,000 GB (in 5 GB increments) |   |
|   |   | 5.7 mysql.x4.xlarge.25 | 8 cores, 32 GB | 5,000 | 9,000 | 500–3,000 GB (in 5 GB increments) |   |
|   |   | 5.7 mysql.x4.2xlarge.2 5 | 16 cores, 64 GB | 10,000 | 18,00 0 | 500–3,000 GB (in 5 GB increments) |   |
|   |   | 5.7 mysql.x4.4xlarge.2 5 | 32 cores, 128 GB | 20,000 | 36,00 0 | 1,000–3,000 GB (in 5 GB increments) |   |

|   |   | Developer Guide· |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
| RDS edition | Instance family | Instance type | CPU and memory | Maxim um conne ctions | Maxim um IOPS | Storage capacity | Zone- disaster recovery deploy ment |
| Enterpris |   | 5.7 mysql.x8.medium.2 5 | 2 cores, 16 GB | 2,500 | 4,500 | 50−1,000 GB (in 5 GB increments) | Single- data center Enterpri se Edition and |
|   |   | 5.7 mysql.x8.xlarge.25 | 4 cores, 32 GB | 5,000 | 9,000 | 50−1,000 GB (in 5 GB increments) |   |
| e Edition | Dedicate d (with a large memory capacity ) |   |   |   |   |   | triple- data center disaster recovery deploy ment |
|   |   | 5.7 mysql.x8.xlarge.25 | 8 cores, 64 GB | 10,000 | 18,00 0 | 500–3,000 GB (in 5 GB increments) |   |
|   |   | 5.7 mysql.x8.2xlarge.2 5 | 16 cores, 128 GB | 20,000 | 36,00 0 |   |   |
|   |   | 5.7 mysql.x8.4xlarge.2 5 | 32 cores, 256 GB | 40,000 | 72,00 0 | 1,000–3,000 GB (in 5 GB increments) |   |
|   | Dedicate d host | 5.7 mysql.st.8xlarge.2 5 | 60 cores, 470 GB | 100,00 0 | 120,0 00 | 1,000–6,000 GB (in 5 GB increments) |   |
|   |   | 5.7 mysql.st.12xlarge. 25 | 90 cores, 720 GB | 150,00 0 | 140,0 00 | 1,000–6,000 GB (in 5 GB increments) |   |
| Document | Version: 202 | 20928 |   |   |   |   | 16 |

| RDS edition | Instance family | Instance type | CPU and memory | Maxim um conne ctions | Maxim um IOPS | Storage capacity | Zone- disaster recovery deploy ment |
|---|---|---|---|---|---|---|---|
| Read- only instance |   | 5.6, 5.7, and 8.0 mysqlro.x8.mediu m.1 | 2 cores, 16 GB | 2,500 | 4,500 | 50−1,000 GB (in 5 GB increments) | Single- data center deploy ment and dual- data center deploy ment |
|   | Dedicate d (X8) |   |   |   |   |   |   |
|   |   | 5.6, 5.7, and 8.0 mysqlro.x8.large.1 | 4 cores, 32 GB | 5,000 | 9,000 | 50−1,000 GB (in 5 GB increments) |   |
|   |   | 5.6, 5.7, and 8.0 mysqlro.x8.xlarge. 1 | 8 cores, 64 GB | 10,000 | 18,00 0 | 500–3,000 GB (in 5 GB increments) |   |
|   |   | 5.6, 5.7, and 8.0 mysqlro.x8.2xlarge .1 | 16 cores, 128 GB | 20,000 | 36,00 0 | 500–3,000 GB (in 5 GB increments) |   |
|   |   | 5.6, 5.7, and 8.0 mysqlro.x8.4xlarge .1 | 32 cores, 256 GB | 40,000 | 72,00 0 | 1,000–6,000 GB (in 5 GB increments) |   |
|   |   | 5.6, 5.7, and 8.0 mysqlro.x8.8xlarge .1 | 64 cores, 512 GB | 80,000 | 14,40 0 | 1,000–6,000 GB (in 5 GB increments) |   |
|   |   | 5.6, 5.7, and 8.0 mysqlro.x4.large.1 | 4 cores, 16 GB | 2,500 | 4,500 | 50−1,000 GB (in 5 GB increments) |   |

|   |   | Developer Guide· |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
| RDS edition | Instance family | Instance type | CPU and memory | Maxim um conne ctions | Maxim um IOPS | Storage capacity | Zone- disaster recovery deploy ment |
|   | Dedicate d (X4) | 5.6, 5.7, and 8.0 mysqlro.x4.xlarge. 1 | 8 cores, 32 GB | 5,000 | 9,000 | 50−1,000 GB (in 5 GB increments) |   |
|   |   | 5.6, 5.7, and 8.0 mysqlro.x4.2xlarge .1 | 16 cores, 64 GB | 10,000 | 18,00 0 | 500–3,000 GB (in 5 GB increments) |   |
|   |   | 5.6, 5.7, and 8.0 mysqlro.x4.4xlarge .1 | 32 cores, 128 GB | 20,000 | 36,00 0 | 500–3,000 GB (in 5 GB increments) |   |
|   | Dedicate d host | 5.6, 5.7, and 8.0 rds.mysql.st.v52 | 90 cores, 720 GB | 150,00 0 | 140,0 00 | 1,000–6,000 GB (in 5 GB increments) |   |
|   |   | 5.6 and 5.7 rds.mysql.st.h43 | 60 cores, 470 GB | 100,00 0 | 120,0 00 |   |   |

ApsaraDB RDS for SQL Server instance types

| RDS edition | SQL Serve r versi on | Instanc e family | Instance type | CPU and memory | Maxi mum conn ectio ns | Maxi mum IOPS | Storage capacity | Zone- disaste r recover y deploy ment |
|---|---|---|---|---|---|---|---|---|

| RDS edition | SQL Serve r versi on | Instanc e family | Instance type | CPU and memory | Maxi mum conn ectio ns | Maxi mum IOPS | Storage capacity | Zone- disaste r recover y deploy ment |
|---|---|---|---|---|---|---|---|---|
|   | 2008 R2 | Dedicat ed | mssql.x8.mediu m.2 | 2 cores, 16 GB | 2,500 | 4,500 | 250 GB | Single- data center deploy ment and dual- data center deploy ment. This instanc e type is not availab le in new data centers , and does not suppor t V5 servers . |
|   |   |   | mssql.x8.large.2 | 4 cores, 32 GB | 5,000 | 9,000 | 500 GB |   |
|   |   |   | mssql.x8.xlarge.2 | 8 cores, 64 GB | 10,00 0 | 18,00 0 | 1,000 GB |   |
|   |   |   | mssql.x8.2xlarge. 2 | 16 cores, 128 GB | 20,00 0 | 36,00 0 | 2,000 GB |   |
|   |   | Dedicat ed host | rds.mssql.st.d13 | 30 cores, 220 GB | 64,00 0 | 20,00 0 | 2 TB |   |
|   |   |   | mssql.x4.mediu m.e2 | 2 cores, 8 GB |   |   |   |   |
|   |   |   | mssql.x8.mediu m.e2 | 2 cores, 16 GB |   |   |   |   |
|   |   |   | mssql.x4.large.e 2 | 4 cores, 16 GB |   |   |   |   |
|   |   |   | mssql.x8.large.e 2 | 4 cores, 32 GB |   |   |   |   |
|   |   |   | mssql.x4.xlarge.e 2 | 8 cores, 32 GB |   |   |   |   |
|   |   |   | mssql.x8.xlarge.e 2 | 8 cores, 64 GB |   |   |   |   |

| RDS edition | 2012 ESEQ:L 2S0e1rv2e rent _ _ hvearsi on 2016 | Instanc e family Dedicat ed | Instance type | CPU and memory | Maxi mum conn ectio ns | Maxi mum IOPS | Storage capacity | Zone- disaste r recover y deploy ment |
|---|---|---|---|---|---|---|---|---|
|   | EE: |   |   |   |   |   |   |   |
| High- availabi lity Edition | 2016 ent _ _ ha |   | mssql.x4.2xlarge. e2 | 16 cores, 64 GB | Unlim ited | Depe nden t on the perfo rman ce of cloud disks | 20–4,000 GB | Single- data center deploy ment |
|   |   |   | mssql.x8.2xlarge. e2 | 16 cores, 128 GB |   |   |   |   |
|   |   |   | mssql.x4.3xlarge. e2 | 24 cores, 96 GB |   |   |   |   |
|   |   |   | mssql.x4.4xlarge. e2 | 32 cores, 128 GB |   |   |   |   |
|   |   |   | mssql.x8.4xlarge. e2 | 32 cores, 256 GB |   |   |   |   |
|   |   |   | mssql.x8.7xlarge. e2 | 56 cores, 480 GB |   |   |   |   |
|   |   |   | mssql.x4.8xlarge. e2 | 64 cores, 256 GB |   |   |   |   |
|   |   |   | mssql.x8.8xlarge. e2 | 64 cores, 512 GB |   |   |   |   |
|   | 2012 SE: 2012 std _ _ ha 2016 SE: 2016 std _ _ ha | Dedicat ed | mssql.x4.mediu m.s2 | 2 cores, 8 GB |   |   |   |   |
|   |   |   | mssql.x8.mediu m.s2 | 2 cores, 16 GB |   |   |   |   |
|   |   |   | mssql.x4.large.s2 | 4 cores, 16 GB |   |   |   |   |
|   |   |   | mssql.x8.large.s2 | 4 cores, 32 GB |   |   |   |   |
|   |   |   | mssql.x4.xlarge.s 2 | 8 cores, 32 GB |   |   |   |   |
|   |   |   | mssql.x8.xlarge.s 2 | 8 cores, 64 GB |   |   |   |   |
|   |   |   | mssql.x4.2xlarge. s2 | 16 cores, 64 GB |   |   |   |   |
|   |   |   | mssql.x8.2xlarge. s2 | 16 cores, 128 GB |   |   |   |   |

| RDS edition | SQL Serve r versi on | Instanc e family | Instance type | CPU and memory | Maxi mum conn ectio ns | Maxi mum IOPS | Storage capacity | Zone- disaste r recover y deploy ment |
|---|---|---|---|---|---|---|---|---|
|   |   |   | mssql.x4.3xlarge. s2 | 24 cores, 96 GB |   |   |   |   |

PolarDB instance types

| RDS edition | PolarDB version | Instance family | Instance type | CPU and memory | Maximu m connecti ons | Maximu m IOPS | Storage capacity | Zone- disaster recovery deploy ment |
|---|---|---|---|---|---|---|---|---|
| High- availabili ty Edition | 11 | Dedicat ed | polardb. x4.small .2 | 1 core, 4 GB | 200 | 5,000 | 250 GB | Single- data center deploy ment and dual- data center deploy ment |
|   |   |   | polardb. x4.medi um.2 | 2 cores, 8 GB | 400 | 10,000 |   |   |
|   |   |   | polardb. x8.medi um.2 | 2 cores, 16 GB | 2,500 | 15,000 |   |   |
|   |   |   | polardb. x4.large. 2 | 4 cores, 16 GB | 2,500 | 20,000 | 250–500 GB (in 5 GB increme nts) |   |
|   |   |   | polardb. x8.large. 2 | 4 cores, 32 GB | 5,000 | 30,000 |   |   |
|   |   |   | polardb. x4.xlarg e.2 | 8 cores, 32 GB | 5,000 | 40,000 | 500– 1,000 GB (in 5 GB increme nts) |   |
|   |   |   | polardb. x8.xlarg e.2 | 8 cores, 64 GB | 10,000 | 60,000 |   |   |
|   |   |   | polardb. x4.2xlar ge.2 | 16 cores, 64 GB | 10,000 | 80,000 | 1,000– 2,000 GB |   |
|   |   |   | polardb. x8.2xlar ge.2 | 16 cores, 128 GB | 12,000 | 120,000 |   |   |
|   |   |   |   |   |   |   | ment Versio |   |

|   |   |   |   |   |   | Devel | oper Guide· |   |
|---|---|---|---|---|---|---|---|---|
| RDS edition | PolarDB version | Instance family | Instance type | CPU and memory | Maximu m connecti ons | Maximu m IOPS | (in 5 GB increme nS tso)rage capacity | Zone- disaster recovery deploy ment |
|   |   |   | polardb. x4.4xlar ge.2 | 32 cores, 128 GB | 12,000 | 160,000 | 2,000– 3,000 GB (in 5 GB increme nts) |   |
|   |   |   | polardb. x8.4xlar ge.2 | 32 cores, 256 GB | 12,000 | 240,000 |   |   |
|   |   | Dedicat ed host | rds.pola rdb.st.h 43 | 60 cores, 470 GB | 12,000 | 450,000 | 6,000 GB |   |

ApsaraDB RDS for PostgreSQL instance types

| RDS | Postgre | Instance | Instance type | CPU and memory | Maximu m connecti ons | Maximu m IOPS | Storage capacity | Zone- disaster |
|---|---|---|---|---|---|---|---|---|
| edition | SQL version | family |   |   |   |   |   | recovery deploy ment |
| High- availabili ty Edition or read- only instance | 9.4/10 | Dedicat ed (with a large memory capacity ) | pg.x8.m edium.2 | 2 cores, 16 GB | 2,500 | 4,500 | 20– 6,000 GB (in 5 GB increme nts) | Single- data center deploy ment and dual- data center deploy ment |
|   |   |   | pg.x8.la rge.2 | 4 cores, 32 GB | 5,000 | 9,000 |   |   |
|   |   |   | pg.x8.xl arge.2 | 8 cores, 64 GB | 10,000 | 18,000 |   |   |
|   |   |   | pg.x8.2x large.2 | 16 cores, 128 GB | 12,000 | 36,000 |   |   |
|   |   | Dedicat ed (with a large number of cores) | pg.x4.la rge.2 | 4 cores, 16 GB | 2,500 | 4,500 |   |   |
|   |   |   | pg.x4.xl arge.2 | 8 cores, 32 GB | 5,000 | 9,000 |   |   |
|   |   |   | pg.x4.2x large.2 | 16 cores, 64 GB | 10,000 | 18,000 |   |   |
|   |   |   | pg.x4.4x large.2 | 32 cores, 128 GB | 12,000 | 36,000 |   |   |
|   |   | 20928 |   |   |   |   |   |   |

| RDS edition | Postgre SQL version | Instance | Instance type | CPU and memory | Maximu m connecti ons | Maximu m IOPS | Storage capacity | Zone- disaster recovery deploy ment |
|---|---|---|---|---|---|---|---|---|
|   |   | family |   |   |   |   |   |   |
|   |   | Dedicat ed host | rds.pg.s t.h43 | 60 cores, 470 GB | 4,000 | 50,000 |   |   |
