---
title: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 ApsaraDB for MongoDB Developer Guide 20220928"
product_version: "V3.14.0"
doc_version: "20220928"
pdf_pages: 211
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 ApsaraDB for MongoDB Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.14.0/%E6%95%B0%E6%8D%AE%E5%BA%93/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.14.0%20ApsaraDB%20for%20MongoDB%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.14.0 ApsaraDB for MongoDB Developer Guide 20220928

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
- 2 List of operations by function
- 3 API Reference
  - 3.1 Lifecycle management
    - 3.1.1 CreateDBInstance
    - 3.1.2 ModifyDBInstanceSpec
    - 3.1.3 DeleteDBInstance
    - 3.1.4 CreateShardingDBInstance
    - 3.1.5 CreateNode
    - 3.1.6 DeleteNode
    - 3.1.7 ModifyNodeSpec
  - 3.2 Region management
    - 3.2.1 MigrateToOtherZone
    - 3.2.2 DescribeRegions
    - 3.2.3 MigrateAvailableZone
  - 3.3 Resource management
    - 3.3.1 DescribeAvailableResource
  - 3.4 Connection management
    - 3.4.1 AllocatePublicNetworkAddress
    - 3.4.2 ReleasePublicNetworkAddress
    - 3.4.3 ModifyInstanceVpcAuthMode
    - 3.4.4 DescribeShardingNetworkAddress
    - 3.4.5 ModifyDBInstanceConnectionString
    - 3.4.6 ReleaseNodePrivateNetworkAddress
  - 3.5 Instance information query
    - 3.5.1 DescribeReplicaSetRole
    - 3.5.2 DescribeKernelReleaseNotes
    - 3.5.3 DescribeAvailableEngineVersion
    - 3.5.4 DescribeDBInstances
    - 3.5.5 DescribeDBInstanceAttribute
    - 3.5.6 DescribeRoleZoneInfo
  - 3.6 Instance management
    - 3.6.1 RestartDBInstance
    - 3.6.2 ModifyDBInstanceMaintainTime
    - 3.6.3 ModifyDBInstanceDescription
    - 3.6.4 SwitchDBInstanceHA
    - 3.6.5 UpgradeDBInstanceEngineVersion
    - 3.6.6 UpgradeDBInstanceKernelVersion
    - 3.6.7 ModifyDBInstanceNetExpireTime
  - 3.7 Account management
    - 3.7.1 DescribeAccounts
    - 3.7.2 ResetAccountPassword
    - 3.7.3 ModifyAccountDescription
  - 3.8 IP whitelists and security groups
    - 3.8.1 DescribeSecurityGroupConfiguration
    - 3.8.2 ModifySecurityGroupConfiguration
    - 3.8.3 DescribeSecurityIps
    - 3.8.4 ModifySecurityIps
  - 3.9 Key management
    - 3.9.1 DescribeDBInstanceTDEInfo
    - 3.9.2 ModifyDBInstanceTDE
  - 3.10 SSL encryption
    - 3.10.1 ModifyDBInstanceSSL
    - 3.10.2 DescribeDBInstanceSSL
  - 3.11 Audit logs
    - 3.11.1 DescribeAuditRecords
    - 3.11.2 DescribeAuditFiles
    - 3.11.3 DescribeAuditPolicy
    - 3.11.4 ModifyAuditLogFilter
    - 3.11.5 DescribeAuditLogFilter
    - 3.11.6 ModifyAuditPolicy
  - 3.12 Log management
    - 3.12.1 DescribeSlowLogRecords
    - 3.12.2 DescribeErrorLogRecords
    - 3.12.3 DescribeRunningLogRecords
  - 3.13 Performance monitoring management
    - 3.13.1 DescribeDBInstancePerformance
    - 3.13.2 DescribeDBInstanceMonitor
  - 3.14 Parameter management
    - 3.14.1 DescribeParameterModificationHistory
    - 3.14.2 DescribeParameters
    - 3.14.3 ModifyParameters
  - 3.15 Backup and recovery
    - 3.15.1 DescribeBackupPolicy
    - 3.15.2 ModifyBackupPolicy
    - 3.15.3 CreateBackup
    - 3.15.4 DescribeBackups
    - 3.15.5 RestoreDBInstance
    - 3.15.6 DescribeBackupDBs
  - 3.16 Instance states

Apsara Stack SDKs

## 1 Use ASAPI to call Apsara Stack SDKs

SDKs

### 1.1 ASAPI Developer Guide

#### 1.1.1 ASAPI overview

This topic describes the architecture and features of the Apsara Stack API (ASAPI). The ASAPI is a unified ingress gateway for Apsara Stack services and a main component of the Apsara Uni-manager Management Console. The ASAPI provides a unified method for you to manage and make API calls. You can use Apsara Stack SDK to centrally make API calls to Apsara Stack services, including Elastic Compute Service (ECS) and Virtual Private Cloud (VPC). The ASAPI allows you to make API calls to manage and maintain Apsara Stack services. Make API calls to implement enterprise-grade management. For example, you can manage organizations, users, roles, resource sets, and logon policies. These operations are provided by the Apsara Stack SDKs Apsara Uni-manager Management Console. Make API calls to manage operations. For example, you can manage quotas, usage statistics, specifications, and password policies. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to manage resources. For example, you can create, delete, query, or modify cloud resources. These operations are provided by Apsara Stack services. If you call an API operation to create an ECS instance or a VPC, the API operation is provided by ECS or VPC. Make API calls to query monitoring metrics of Apsara Stack services. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to perform O&M. For example, you can manage monitoring and alerting, inventories, tasks, and physical servers. These operations are provided by the Apsara Uni-manager Operations Console. For more information, see the developer guide of the corresponding Apsara Stack service. For information about API operations used to manage organization users, see Apsara Uni-manager Management Console Developer Guide. For information about the API operation used to create an ECS instance, see ECS Developer Guide. If the "Use Apsara Stack SDK to make API calls" section is included in the developer guide of an Apsara Stack service, the ASAPI is supported by the Apsara Stack service. In this case, you can make API calls based on the developer guide.

#### 1.1.2 Preparations

##### 1.1.2.1 Log on to the API Tool console

You can log on to the API Tool console from the Apsara Uni-manager Management Console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. Apsara Stack SDKs The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
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
The AccessKey pair that consists of an AccessKey ID and an AccessKey secret is the credential for you to have full permissions on Apsara Stack resources. Keep your AccessKey pair confidential. Obtain the AccessKey pair of an account that has permissions on an organization To obtain the AccessKey pair of an account that has permissions on an organization, perform the following operations:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane of the Ent erprise page, click Organizat ions.
4. In the Organizations navigation tree, click the name of the organization that you want to manage.
5. On the right side of the page, click Obt ain AccessKey Pair.
6. In the message that appears, obtain the AccessKey pair of the account that has permissions on the
organization. The system automatically allocates an AccessKey pair to the account that has permissions on the level-1 organization. The same AccessKey pair is used by the accounts that have permissions on the subordinate organizations.

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

Apsara Stack SDKs

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

Replace `1.0.6-RELEASE` with the actual version of Apsara Stack SDK for Java.
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

Replace `2.4.7` with the actual version of Apsara Stack SDK for Python. Sample requests You can use the GET or POST method to call API operations provided by the ASAPI. Apsara Stack SDKs

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

Not ice If you send a request over HTTPS, you must enable the request to ignore SSL certificate validation.

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

This topic describes how to sign HTTP API requests. ASAPI uses the request signature to verify the identity of the request sender. ASAPI implements symmetric encryption by using an AccessKey pair to verify the identity of the request sender. An AccessKey pair consists of an AccessKey ID and an AccessKey secret, which are issued to each user or organization in the Apsara Uni-manager Management Console. The AccessKey ID is used to verify identities of users, and the AccessKey secret is used to encrypt and verify signature strings. You must keep your AccessKey secret confidential. ASAPI provides SDKs for Node.js, Python, and Java to facilitate complex signature calculation. For more information, see Obtain the core package for ASAPI. Step 1: Create a canonicalized query string
1. Arrange the request parameters in alphabetical order, including all common and operation-specific
parameters except the `Signature` parameter. If you use the GET method to send a request,these parameters are connected by ampersands (&) and included in the request URL. The first request parameter follows a question mark (?).
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

Apsara Stack SDKs When you calculate the signature, the key value specified by RFC 2104 is your `AccessKey secret` plus an ampersand (&), which has an ASCII value of 38. For more information, see Obtain an AccessKey pair.
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

2. Predefine the time format for the `Timestamp` parameter. Specify the `Timestamp` parameter in
the ISO 8601 format. The time must be in UTC+0.

```java
private static final String ISO8601_DATE_FORMAT = "yyyy-MM-dd'T'HH:mm:ss'Z'"; private static String formatIso8601Date(Date date) {
    SimpleDateFormat df = new SimpleDateFormat(ISO8601_DATE_FORMAT);
    df.setTimeZone(new SimpleTimeZone(0, "GMT"));
    return df.format(date);
```

3. Create a request string.
Apsara Stack SDKs

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

by function

## 2 List of operations by function

The following tables list API operations available for use in ApsaraDB for MongoDB. Lifecycle management

| Operation | Description |
|---|---|
| CreateDBInstance | Creates and clones an ApsaraDB for MongoDB instance. |
| ModifyDBInstanceSpec | Modifies the specifications or storage capacity of an ApsaraDB for MongoDB standalone or replica set instance. |
| DeleteDBInstance | Releases an ApsaraDB for MongoDB instance. |
| CreateShardingDBInstance | Creates or clones an ApsaraDB for MongoDB sharded cluster instance. |
| CreateNode | Creates a shard or mongos node for an ApsaraDB for MongoDB sharded cluster instance. |
| DeleteNode | Deletes a shard or mongos node in an ApsaraDB for MongoDB sharded cluster instance. |
| ModifyNodeSpec | Modifies the specifications or storage capacity of an ApsaraDB for MongoDB sharded cluster instance. |

Region management

| Operation | Description |
|---|---|
| MigrateToOtherZone | Migrates an ApsaraDB for MongoDB instance to another zone. |
| DescribeRegions | Views the regions and zones that an ApsaraDB for MongoDB instance can be created. |
| MigrateAvailableZone | Changes the zone of an ApsaraDB for MongoDB instance. |

Resource management

| Operation | Description |
|---|---|
| DescribeAvailableResource | Views the instances that can be created in a specified zone. |

Connection management

| Operation | Description |
|---|---|
| AllocatePublicNetworkAddress | Applies for a public endpoint of an ApsaraDB for MongoDB instance. |
| ReleasePublicNetworkAddress | Releases the public endpoint of an ApsaraDB for MongoDB instance. |

| eveloper Guide·List of operations | ApsaraDB for MongoD |
|---|---|

by function

| Operation | Description |
|---|---|
| ModifyInstanceVpcAuthMode | Enables or disables password-free access to an ApsaraDB for MongoDB instance from the same VPC. |
| DescribeShardingNetworkAddress | Views the connection information of an ApsaraDB for MongoDB sharded cluster instance. |
| ModifyDBInstanceConnectionStrin g | Modifies the connection string of an ApsaraDB for MongoDB instance. |
| ReleaseNodePrivateNetworkAddr ess | Releases the internal endpoint of the shard or Configserver node of a sharded cluster instance. |

Instance information query

| Operation | Description |
|---|---|
| DescribeReplicaSetRole | Views the roles of an ApsaraDB for MongoDB instance and their connection information. |
| DescribeKernelReleaseNotes | Views the release notes of the minor database engine versions of an ApsaraDB for MongoDB instance. |
| DescribeAvailableEngineVersion | Views the database engine versions that an ApsaraDB for MongoDB instance can be upgraded to. |
| DescribeDBInstances | Views the list of ApsaraDB for MongoDB instances. |
| DescribeDBInstanceAttribute | Views the details of an ApsaraDB for MongoDB instance. |
| DescribeRoleZoneInfo | Views the roles and zones of nodes in an ApsaraDB for MongoDB instance. |

Instance management

| Operation | Description |
|---|---|
| RestartDBInstance | Restarts an ApsaraDB for MongoDB instance. |
| ModifyDBInstanceMaintainTime | Modifies the maintenance window of an ApsaraDB for MongoDB instance. |
| ModifyDBInstanceDescription | Changes the name of an ApsaraDB for MongoDB instance. |
| SwitchDBInstanceHA | Switches between the primary and secondary nodes in an ApsaraDB for MongoDB instance. |
| UpgradeDBInstanceEngineVersion | Upgrades the database engine version of an ApsaraDB for MongoDB instance. |
| UpgradeDBInstanceKernelVersion | Upgrades the minor database engine version of an ApsaraDB for MongoDB instance. |

| psaraDB for MongoDB | Developer Guide·List of operations by functio |
|---|---|

| Operation | Description |
|---|---|
| ModifyDBInstanceNetExpireTime | Extends the retention period of the classic network endpoint of an ApsaraDB for MongoDB instance. |

Account management

| Operation | Description |
|---|---|
| DescribeAccounts | Views the database accounts of an ApsaraDB for MongoDB instance. |
| ResetAccountPassword | Resets the password of the root account of an ApsaraDB for MongoDB instance. |
| ModifyAccountDescription | Modifies the description of the root account of an ApsaraDB for MongoDB instance. |

Whitelists and security groups

| Operation | Description |
|---|---|
| DescribeSecurityGroupConfigurati on | Views the ECS security groups to which an ApsaraDB RDS instance is added. |
| ModifySecurityGroupConfiguratio n | Modifies an ECS security group to which an ApsaraDB RDS instance is added. |
| DescribeSecurityIps | Views the IP whitelists of an ApsaraDB for MongoDB instance. |
| ModifySecurityIps | Modifies an IP whitelist of an ApsaraDB for MongoDB instance. |

Key management

| Operation | Description |
|---|---|
| DescribeDBInstanceTDEInfo | Views whether TDE is enabled for an ApsaraDB for MongoDB instance. |
| ModifyDBInstanceTDE | Modifies the transparent data encryption (TDE) status of an ApsaraDB for MongoDB instance. |

SSL encryption

| Operation | Description |
|---|---|
| ModifyDBInstanceSSL | Modifies the SSL settings of an ApsaraDB for MongoDB instance. |
| DescribeDBInstanceSSL | Views the SSL settings of an ApsaraDB for MongoDB instance. |

Audit logs by function

| Operation | Description |
|---|---|
| DescribeAuditRecords | View the audit log entries of an ApsaraDB for MongoDB instance. |
| DescribeAuditFiles | Views the audit log files of an ApsaraDB for MongoDB instance. |
| DescribeAuditPolicy | Views whether the audit log feature is enabled for an ApsaraDB for MongoDB instance. |
| ModifyAuditLogFilter | Modifies the type of audit log entries that you want to collect for an ApsaraDB for MongoDB instance. |
| DescribeAuditLogFilter | Views the types of audit log entries collected for an ApsaraDB for MongoDB instance. |
| ModifyAuditPolicy | Enables or disables the audit log feature or set the log retention period for an ApsaraDB for MongoDB instance. |

Log management

| Operation | Description |
|---|---|
| DescribeSlowLogRecords | Views the slow query log entries of an ApsaraDB for MongoDB instance. |
| DescribeErrorLogRecords | Views the error log entries of an ApsaraDB for MongoDB instance. |
| DescribeRunningLogRecords | Views the operational log entries of an ApsaraDB for MongoDB instance. |

Performance monitoring management

| Operation | Description |
|---|---|
| DescribeDBInstancePerformance | Views the performance data of an ApsaraDB for MongoDB instance. |
| DescribeDBInstanceMonitor | Views the collection frequency of monitoring data for an ApsaraDB for MongoDB instance. |

Parameter management

| Operation | Description |
|---|---|
| DescribeParameterModificationHi story | Views the modification records of ApsaraDB for MongoDB instance parameters. |
| DescribeParameters | Views parameter configurations of an ApsaraDB for MongoDB instance. |
| ModifyParameters | Modifies the parameters of an AsparaDB for MongoDB instance. |

Backup and recovery by function

| Operation | Description |
|---|---|
| DescribeBackupPolicy | Views the backup policy of an ApsaraDB for MongoDB instance. |
| ModifyBackupPolicy | Modifies the backup policy of an ApsaraDB for MongoDB instance. |
| CreateBackup | Manually backs up an ApsaraDB for MongoDB instance. |
| DescribeBackups | Views the backup sets of an ApsaraDB for MongoDB instance. |
| RestoreDBInstance | Restores data to the current ApsaraDB for MongoDB instance. |
| DescribeBackupDBs | Views the databases at a specified point in time or the databases in a specified backup set before you restore a database for an ApsaraDB for MongoDB instance. |

## 3 API Reference

### 3.1 Lifecycle management

#### 3.1.1 CreateDBInstance

You can call this operation to create or clone an ApsaraDB for MongoDB replica set instance. For more information about instance types, see Inst ance t ypes in ApsaraDB for MongoDB Product Introduction. To create sharded cluster instances, you can call the Creat eShardingDBInst ance operation. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateDBInstance | The operation that you want to perform. Set the value to Creat eDBInst ance. |
| ClientToken | String | Yes | ETnLKlblzczshOT UbOCzxxxxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| Engine | String | Yes | MongoDB | The database engine. Set the value to MongoDB. |
| EngineVersion | String | Yes | 4.0 | The database engine version of the instance. Valid values: 3.2, 3.4, 4.0, and 4.2. Not e To call this operation to clone an instance, set this value to the engine version of the source instance. |
| DBInstanceClass | String | Yes | dds.mongo.stan dard | The instance type. For more information, see Inst ance t ypes in ApsaraDB for MongoDB Product Introduction. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceStorag e | Integer | Yes | 10 | The storage capacity of the instance. Valid values: 10 to 3000. Unit: GB. The value must be a multiple of 10 GB. Not e For more information about instance types, see Inst ance t ypes in ApsaraDB for MongoDB Product Introduction. |
| ZoneId | String | No | cn-hangzhou-b | The zone ID of the instance. You can call the DescribeRegions operation to view the zones where the instance can be created. |
| DBInstanceDescri ption | String | No | Test database 1 | The name of the instance. It must be 2 to 256 characters in length. The name must start with a letter, and can contain digits, letters, underscores ( ), _ and hyphens (-). |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SecurityIPList | String | No | 10.23.12.24/24 | The whitelist that contains the IP addresses that are allowed to access the instance. Separate multiple IP addresses with commas (,). Each IP address must be unique. A maximum of 1,000 IP addresses can be added. You can enter IP addresses such as 10.23.12.24 and Classless Inter- Domain Routing (CIDR) blocks such as 10.23.12.24/24. /24 indicates the length of the IP address prefix in the CIDR block. An IP address prefix can contain 1 to 32 bits. You can also enter the percent sign (%) or 0.0.0.0/0. Not e If you enter the percent sign (%) or 0.0.0.0/0, all IP addresses can access the instance. This may introduce security risks to the instance. |
| AccountPassword | String | No | Alitest! 159 | The password of the root account. The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include ! # $ % ^ & * ( ) + - = _ #$%^&amp;*() +-= _ The password must be 8 to 32 characters in length. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ChargeType | String | No | PrePaid | The billing method of the instance. Valid values: Post paid: pay-as-you-go Prepaid: subscription Default value: pay-as-you-go Not e If you set this parameter to PrePaid, you must also specify the Period parameter. |
| Period | Integer | No | 1 | The subscription period of the instance. Unit: months. Valid values: 1 to 9, 12, 24, and 36. Not e This parameter is valid and required only if you set the ChargeT ype parameter to PrePaid. |
| NetworkType | String | No | VPC | The network type of the new instance. Valid values: classic vpc Default value: classic. Not e If you set this parameter to VPC, you must also specify the VpcId and VSwit chId parameters. |
| VpcId | String | No | vpc-bpxxxxxxxx | The ID of the VPC. Not e This parameter is valid only if you set the Net workT ype parameter to VPC. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VSwitchId | String | No | vsw-bpxxxxxxxx | The ID of the vSwitch in the specified VPC. Not e This parameter is valid only if you set the Net workT ype parameter to VPC. |
| SrcDBInstanceId | String | No | dds-bpxxxxxxxx | The ID of the source instance. This parameter can only be specified when this operation is called to clone instances. You must also specify the BackupId parameter or Rest oreT ime parameter. |
| BackupId | String | No | 32994xxxx | The ID of the specific backup set. This parameter can only be specified when this operation is called to clone instances. You must also specify the SrcDBInst anceId parameter. Not e You can call DescribeBackups to view the backup ID. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RestoreTime | String | No | 2019-03- 13T12:11:14Z | The point in time of the clone operation. After you set this parameter, the data of the source instance at the specified point in time is used to create an instance. Specify the time in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. Not e This parameter can only be specified when this operation is called to clone instances. You must also specify the SrcDBInst anceId parameter and the BackupId parameter. You can clone instances to any restore time in the past seven days. |
| BusinessInfo | String | No | {“ActivityId":"00 0000000"} | The business information. It is an additional parameter. |
| CouponNo | String | No | youhuiquan pro _ motion option id _ _ for blank _ _ | The coupon code. Default value: youhuiquan promot ion opt ion id _ _ _ _ f or blank. _ |
| AutoRenew | String | No | true | Indicates whether automatic renewal is enabled for the instance. Valid values: t rue: enables automatic renewal. f alse: disables automatic renewal. You must renew the instance manually. Default value: false. Not e This parameter is valid only if you set the ChargeType parameter to PrePaid. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DatabaseNames | String | No | mongodbtest | The name of the database. Not e When calling this operation to clone instances, you can set the database that is specified by this parameter for cloning. Otherwise, all the databases of the instances will be cloned. |
| StorageEngine | String | No | WiredTiger | The storage engine of the instance. It must be WiredT iger. Not e If you do not specify this parameter, WiredT iger is used. |
| ReplicationFactor | String | No | 3 | The number of nodes in the replica set instance. Valid values: 3, 5, and 7. Default value: 3. |
| ReadonlyReplicas | String | No | 1 | The number of read-only nodes. Valid values: 1 t o 5. Not e By default, this parameter is not specified and no read-only node is created. |
| ResourceGroupId | String | No | rg-axxxxxxxx | The ID of the resource group. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | dds-bpxxxxxxxx | The ID of the instance. |
| OrderId | String | 2033xxxxxxxxxxxx | The ID of the order. |
| RequestId | String | D8F1D721-6439- 4257-A89C- F1E8E9C9624D | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=CreateDBInstance &ClientToken=ETnLKlblzczshOTUbOCzxxxxxxxxxx &Engine=MongoDB &EngineVersion=4.0 &DBInstanceClass=dds.mongo.standard &DBInstanceStorage=10 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateDBInstanceResponse>
   <DBInstanceId>dds-bpxxxxxxxx</DBInstanceId>
   <OrderId>2033xxxxxxxxxxxx</OrderId>
   <RequestId>D8F1D721-6439-4257-A89C-F1E8E9C9624D</RequestId>
</CreateDBInstanceResponse>
```

`JSON` format `{`

```json
 "DBInstanceId": "dds-bpxxxxxxxx",
 "OrderId": "2033xxxxxxxxxxxx",
 "RequestId": "D8F1D721-6439-4257-A89C-F1E8E9C9624D"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InsufficientBalance | Your account does not have enough balance. | The error message returned when your account does not have sufficient balance. Top up and try again. |
| 403 | RealNameAuthentica tionError | Your account has not passed the real-name authentication yet. | The error message returned when the specified user has not performed real-name authentication. Perform real- name authentication and try again. |
| 400 | InvalidCapacity.NotF ound | The Capacity provided does not exist in our records. | The error message returned when the configured capacity is invalid. Check the specified parameter. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | IdempotentParamet erMismatch | Request uses a client token in a previous request but is not identical to that request. | The error message returned because the two specified requests use the same ClientToken. |

#### 3.1.2 ModifyDBInstanceSpec

You can call this operation to modify the specifications or storage capacity of an ApsaraDB for MongoDB replica set instance. This operation is applicable only to replica set instances. You can call the Modif yNodeSpec, Creat eNode, or Delet eNode operation to modify the configurations of a sharded cluster instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstance Spec | The operation that you want to perform. Set the value toModif yDBInst anceSpec. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| DBInstanceClass | String | No | dds.mongo.stan dard | The instance type. For more information, see Inst ance t ypes in ApsaraDB for MongoDB Product Introduction. Not e You must specify either this parameter or the DBInst anceSt orage parameter. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceStorag e | String | No | 50 | The storage capacity of the instance. Valid values: 10 to 3000. Unit: GB. The values of this parameter are dependent on the instance types. For more information, see Inst ance t ypes in ApsaraDB for MongoDB Pro duct Introduction. The value must be a multiple of 10 GB. Not e You must specify either this parameter or theDBInst anceSt orage parameter. Storage capacity can be scaled down only on subscription replica set instances. The new storage capacity you specify must be greater than the used storage space. |
| OrderType | String | No | UPGRADE | The type of configuration changes performed. Default value: DOWNGRADE. Valid values: UPGRADE: The specifications are upgraded. DOWNGRADE: The specifications are downgraded. Not e This parameter is only applicable to instances whose billing method is subscription. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AutoPay | Boolean | No | true | Specifies whether automatic payment is enabled for the instance. Valid values: t rue: enables automatic payment. Make sure that your account has sufficient balance. f alse: Automatic payment is not enabled. You must make payments in the console. Payment instructions: Log on to the console. In the upper- right corner, click Billing Management and select Billing Management from the drop-down list. The Billing Management page appears. In the left-side navigation pane, click Bills. On the Unpaid tab, click Make a Payment in the Actions column corresponding to the bill you want to pay. Default value: t rue. |
| BusinessInfo | String | No | {“ActivityId":"00 0000000"} | The business information. |
| ReplicationFactor | String | No | 3 | The number of nodes in the instance. Valid values for a replica set instance: 3, 5, and 7. Valid values for a standalone instance: 1. |
| CouponNo | String | No | youhuiquan pro _ motion option id _ _ for blank _ _ | The coupon code. Default value:youhuiquan promot ion opt i _ _ on id f or blank. _ _ _ |
| EffectiveTime | String | No | Immediately | The time when the modified configuration values take effect. Valid values: Immediat ely: The settings take effect immediately. Maint ainT ime: The settings will take effect during the maintenance period of the instance. Default value: Immediat ely. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | No | cn-hangzhou | The region ID of the instance. You can call the DescribeDBInst anceAt t ribut e operation to view the region ID of the instance. |
| ReadonlyReplicas | String | No | 1 | The number of read-only nodes. Valide values: 1 to 5. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| OrderId | String | 2033xxxxxxxx | The ID of the order. |
| RequestId | String | C5662998-62BE- 4C7F-961D- 7DFE775DD813 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyDBInstanceSpec &DBInstanceId=dds-bpxxxxxxxx &DBInstanceStorage=50 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceSpecResponse>
      <OrderId>2033xxxxxxxx</OrderId>
      <RequestId>C5662998-62BE-4C7F-961D-7DFE775DD813</RequestId>
</ModifyDBInstanceSpecResponse>
```

`JSON` format `{`

```json
    "OrderId": "2033xxxxxxxx",
    "RequestId": "C5662998-62BE-4C7F-961D-7DFE775DD813"
```

#### 3.1.3 DeleteDBInstance

You can call this operation to release an ApsaraDB for MongoDB instance. The instance must be in the running state when you call this operation. After an instance is released, all the data in the instance is lost and cannot be retrieved. Proceed with caution. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteDBInstance | The operation that you want to perform. Set the value to Delet eDBInst ance. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxxxx | The client token that is used to ensure idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 72651AF9-7897- 41A7-8B67- 6C15C7F26A0A | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DeleteDBInstance &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteDBInstanceResponse>
   <RequestId>72651AF9-7897-41A7-8B67-6C15C7F26A0A</RequestId>
</DeleteDBInstanceResponse>
```

`JSON` format `{`

```json
 "RequestId": "72651AF9-7897-41A7-8B67-6C15C7F26A0A"
```

#### 3.1.4 CreateShardingDBInstance

You can call this operation to create or clone a sharded cluster instance. For more information about instance types, see Inst ance t ypes in ApsaraDB for MongoDB Product Introduction. To create replica set instances, you can call the Creat eDBInst ance operation. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateShardingDB Instance | The operation that you want to perform. Set the value toCreat eShardingDBInst ance. |
| AccountPassword | String | Yes | Alitest! 159 | The password of the root account. The password must contain at least three types of the following characters: uppercase letters, lowercase letters, digits, and special characters. Special characters include ! # $ % ^ & * ( ) + - = _ The password must be 8 to 32 characters in length. |
| Engine | String | Yes | MongoDB | The database engine. Set the value to MongoDB. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| EngineVersion | String | Yes | 4.0 | The database engine version of the instance. Valid values: 3.0, 3.4, 4.0, and 4.2. Not e To call this operation to clone an instance, set this value to the engine version of the source instance. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. You can call the DescribeRegions operation to view the region ID of the instance. |
| ZoneId | String | No | cn-hangzhou-b | The zone ID of the instance. You can call the DescribeRegions operation to view the zone ID of the instance. |
| Mongos.N.Class | String | No | dds.mongos.stan dard | The specifications of the mongos node. For more information, see Inst ance t ypes in ApsaraDB for MongoDB Product Introduction. N: the specifications of the nth mongos node. For example, Mongos.1.Class specifies the specifications of the first mongos node. Mongos.2.Class specifies the specifications of the second mongos node. Not e You can configure the specifications of 2 to 32 mongos nodes. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ReplicaSet.N.Clas s | String | No | dds.shard.standa rd | The specifications of the shard node. For more information, see Inst ance t ypes in ApsaraDB for MongoDB Product Introduction. Nspecifies the serial number of the shard for which the specifications are specified. For example, ReplicaSet .1.Class specifies the specifications of the first shard. ReplicaSet .2.Class specifies the specifications of the second shard. Not e You can specify the specifications of 2 to 32 shards. |
| ReplicaSet.N.Stor age | Integer | No | 20 | The storage space of shard N. Valid values: 10 to 2000. Unit: GB. You can only specify this value in 10 GB increments. Not e For more information about instance types, see Inst ance t ypes in ApsaraDB for MongoDB Product Introduction. Nspecifies the serial number of the shard for which storage space is specified. For example, ReplicaSet .1.St orage specifies the storage space of the first shard. ReplicaSet .2.St orage specifies the storage space of the second shard. |
| ConfigServer.N.Cl ass | String | No | dds.cs.mid | The specifications of the Configserver node. Valid value:dds.cs.mid. Not e Set the specifications to one CPU core and 2 GB. You can specify the specifications of only one Configserver node. For example, set the Conf igServer.1.Class parameter to dds.cs.mid. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ConfigServer.N.St orage | Integer | No | 20 | The storage space of the Configserver node. Set the value to 20. Not e You can set this parameter to 20 GB only. For example, set the Conf igServer.1.St orage parameter to 20. |
| DBInstanceDescri ption | String | No | Test database 1 | The name of the instance. It must be 2 to 256 characters in length. The name must start with a letter, and can contain digits, letters, underscores ( ), _ and hyphens (-). |
| SecurityIPList | String | No | 10.23.12.24/24 | The whitelist that contains the IP addresses that are allowed to access the instance. Separate multiple IP addresses with commas (,). Each IP address must be unique. A maximum of 1,000 IP addresses can be added. You can enter IP addresses such as 10.23.12.24 and Classless Inter- Domain Routing (CIDR) blocks such as 10.23.12.24/24. /24 indicates the length of the CIDR block prefix. The prefix can be 1 to 32 bits in length. You can also enter the percent sign (%) or 0.0.0.0/0. Not e If you enter the percent sign (%) or 0.0.0.0/0, all IP addresses can access the instance. This may introduce security risks to the instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ChargeType | String | No | PrePaid | The billing method of the instance. Valid values: Post paid: pay-as-you-go Prepaid: subscription Default value: pay-as-you-go Not e If you specify this parameter to PrePaid, you must also specify the Period parameter. |
| Period | Integer | No | 1 | The subscription period of the instance. Unit: months. Valid values: 1 to 9, 12, 24, and 36. Not e This parameter is valid and required only if you set the ChargeT ype parameter to PrePaid. |
| NetworkType | String | No | VPC | The network type of the instance. Valid values: Default value: CLASSIC. CLASSIC VPC Not e If you specify this parameter to VPC, you must also specify the VpcId parameter and theVSwit chId parameter. |
| VpcId | String | No | vpc-bpxxxxxxxx | The ID of the VPC. Not e This parameter is valid only if you set theNet workT ype parameter to VPC. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VSwitchId | String | No | vsw-bpxxxxxxxx | The ID of the vSwitch in the specified VPC. Not e This parameter is valid only if you set theNet workT ype parameter to VPC. |
| SrcDBInstanceId | String | No | dds-bpxxxxxxxx | The ID of the source instance. This parameter can only be specified when this operation is called to clone instances. You must also specify the Rest oreT ime parameter. |
| RestoreTime | String | No | 2019-03- 08T02:30:25Z | The point in time at which the instance to be cloned will be restored. After you set this parameter, the data of the source instance at the specified point in time is used to create an instance. Specify the time in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. This parameter can be specified only if this operation is called to clone instances. You must also specify theSrcDBInst anceId parameter. Not e You can clone instances to any restore time in the past seven days. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| StorageEngine | String | No | WiredTiger | The storage engine of the database. Only WiredT iger is supported. |
| AutoRenew | String | No | false | Specifies whether to enable automatic renewal for the instance. Valid values: t rue: enables automatic renewal. f alse: disables automatic renewal. You must renew the instance manually. Default value: f alse. Not e This parameter is valid only if you set the ChargeType parameter to PrePaid. |
| ResourceGroupId | String | No | rg-axxxxxxxx | The ID of the resource group. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | dds-bpxxxxxxxx | The ID of the instance. |
| OrderId | String | 2033xxxxxxxxxxxx | The ID of the order. |
| RequestId | String | D8F1D721-6439- 4257-A89C- F1E8E9C9623D | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=CreateShardingDBInstance &Engine=MongoDB &EngineVersion=4.0 &AccountPassword=Alitest! 159 &ZoneId=cn-hangzhou-b &ClientToken=ETnLKlblzczshOTUbOCzxxxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateDBInstanceResponse>
      <DBInstanceId>dds-bpxxxxxxxx</DBInstanceId>
      <OrderId>2033xxxxxxxxxxxx</OrderId>
      <RequestId>D8F1D721-6439-4257-A89C-F1E8E9C9623D</RequestId>
</CreateDBInstanceResponse>
```

`JSON` format `{`

```json
    "DBInstanceId": "dds-bpxxxxxxxx",
    "OrderId": "2033xxxxxxxxxxxx",
    "RequestId": "D8F1D721-6439-4257-A89C-F1E8E9C9623D"
```

#### 3.1.5 CreateNode

You can call this operation to create the shard or mongos node for an ApsaraDB for MongoDB sharded cluster instances. This operation is applicable only to sharded cluster instances. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateNode | The operation that you want to perform. Set the value to Creat eNode. |
| NodeClass | String | Yes | dds.shard.mid | The specification of the shard or mongos node. For more information, see Instance types. |
| NodeType | String | Yes | shard | The type of the node. Valid values: shard mongos |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the sharded cluster instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| NodeStorage | Integer | No | 10 | The storage capacity of the node. You must specify this parameter if you set the NodeT ype parameter to shard. Valid values: 10 to 2000. Unit: GB. The value must be a multiple of 10 GB. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxxxx | The client token that is used to ensure idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| FromApp | String | No | OpenApi | The source of the request. Valid values: OpenApi: the ApsaraDB for MongoDB API mongo buy: the ApsaraDB for _ MongoDB console |
| AutoPay | Boolean | No | true | Specifies whether to enable automatic payment for the instance. Valid values: t rue: enables automatic payment. Make sure that your account has sufficient balance. f alse: disables automatic payment. You must perform the following operations to pay for the instance: Log on to the ApsaraDB for MongoDB console. In the top navigation bar, click Expenses. The Billing Management page appears. In the left-side navigation pane, click Bills. On the Unpaid tab, click Make a Payment in the Actions column for the bill that you want to pay. Default value: t rue. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| NodeId | String | d-bpxxxxxxxxxxxxxx | The ID of the node. |

| Developer Guide·AP | I Reference |   | ApsaraDB for MongoD |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| OrderId | String | 2034xxxxxxxx | The ID of the order. |
| RequestId | String | 7D48FB19-20CA- 4725-A870- 3D8F5CE69F14 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=CreateNode &NodeClass=dds.shard.mid &NodeType=shard &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateNodeResponse>
   <OrderId>2034xxxxxxxx</OrderId>
   <RequestId>7D48FB19-20CA-4725-A870-3D8F5CE69F14</RequestId>
</CreateNodeResponse>
```

`JSON` format `{`

```json
 "OrderId": "2034xxxxxxxx",
 "RequestId": "7D48FB19-20CA-4725-A870-3D8F5CE69F14"
```

#### 3.1.6 DeleteNode

You can call this operation to delete a shard or mongos in an ApsaraDB for MongoDB sharded cluster instance. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. A sharded cluster instance is used. The number of shard or mongos nodes in the instance must be greater than two. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteNode | The operation that you want to perform. Set the value to Delet eNode. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| NodeId | String | Yes | s-bpxxxxxxxx | The ID of the shard or mongos node to be deleted. You can call the DescribeDBInstanceAttribute operation to view the ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| OrderId | String | 2033xxxxxxxxxxxx | The ID of the order. |
| RequestId | String | 9F9BDE64-BF30- 41F3-BD29- C19CE4AB3404 | The ID of the request. |
| TaskId | Integer | 111111111 | The ID of the task. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DeleteNode &NodeId=s-bpxxxxxxxx &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteNodeResponse>
   <RequestId>9F9BDE64-BF30-41F3-BD29-C19CE4AB3404</RequestId>
   <TaskId>111111111</TaskId>
</DeleteNodeResponse>
```

`JSON` format `{`

```json
    "RequestId": "9F9BDE64-BF30-41F3-BD29-C19CE4AB3404",
    "TaskId": 111111111
```

#### 3.1.7 ModifyNodeSpec

You can call this operation to modify the specifications and storage capacity of the nodes in an ApsaraDB for MongoDB sharded cluster instance. This operation is applicable only to sharded cluster instances. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyNodeSpec | The operation that you want to perform. Set the value to Modif yNodeSpec. |
| NodeId | String | Yes | d-bpxxxxxxxx | The ID of the shard or mongos node in the sharded cluster instance. You can call the DescribeDBInst anceAt t ribut e operation to view the ID. Not e If you set this parameter to the ID of a shard, you must also specify the NodeSt orage parameter. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| NodeClass | String | No | dds.shard.standa rd | The specifications of the mongos node. For more information, see Inst ance t ypes in ApsaraDB for MongoDB Product Introduction. Not e You must specify this parameter or the NodeSt orage parameter. |
| NodeStorage | Integer | No | 20 | The storage capacity for the shard node. Valid values: 10 to 2000. Unit: GB. The value must be a multiple of 10 GB. Not e You must specify this parameter or the NodeClass parameter. This parameter is valid only if you set the NodeId parameter to the ID of a shard. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AutoPay | Boolean | No | true | Specifies whether to enable automatic payment for the instance. Valid values: t rue: enables automatic payment. Make sure that your account has sufficient balance. f alse: disables automatic payment. You must perform the following operations to pay for the instance: Log on to the ApsaraDB for MongoDB console. In the top navigation bar, click Expenses. The Billing Management page appears. In the left-side navigation pane, click Bills. On the Unpaid tab, click Make a Payment in the Actions column for the bill that you want to pay. Default value: t rue. |
| EffectiveTime | String | No | Immediately | The time when the new settings take effect. Valid values: Immediat ely: The settings take effect immediately. Maint ainT ime: The settings take effect during the maintenance period of the instance. Default value: Immediat ely. |
| FromApp | String | No | OpenApi | The source of the request. Valid values: OpenApi: the ApsaraDB for MongoDB API mongo buy: the ApsaraDB for _ MongoDB console |
| OrderType | String | No | UPGRADE | The type of the order. Valid values: UPGRADE DOWNGRADE |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| OrderId | String | 2033xxxxxxxxx | The ID of the order. |
| RequestId | String | EFFC5788-8BB5- 41B5-9F15- 9CFC5A0E8FCC | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.aliyuncs.com/? Action=ModifyNodeSpec &NodeId=d-bpxxxxxxxx &DBInstanceId=dds-bpxxxxxxxx &NodeClass=dds.shard.standard &NodeStorage=20 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyNodeSpecResponse>
   <OrderId>2033xxxxxxxxx</OrderId>
   <RequestId>EFFC5788-8BB5-41B5-9F15-9CFC5A0E8FCC</RequestId>
</ModifyNodeSpecResponse>
```

`JSON` format `{`

```json
    "OrderId": "2033xxxxxxxx",
    "RequestId": "EFFC5788-8BB5-41B5-9F15-9CFC5A0E8FCC"
```

### 3.2 Region management

#### 3.2.1 MigrateToOtherZone

You can call this operation to migrate an ApsaraDB for MongoDB instance to another zone. This operation is applicable only to replica set instances, but not to sharded cluster instances. If you have applied for a public endpoint of the instance, you must first call the ReleasePublicNet workAddress operation to release the public endpoint. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | MigrateToOtherZ one | The operation that you want to perform. Set the value to Migrat eT oOt herZone. |
| InstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Not e You must specify the Vswit ch parameter if the network type of the instance is VPC. |
| ZoneId | String | Yes | cn-hangzhou-b | The ID of the destination zone to which you want to migrate the MongoDB instance. Not e The destination and source zones are in the same region. You can call the DescribeRegions operation to query the zone IDs. |
| EffectiveTime | String | No | Immediately | The time when the instance is migrated to the destination zone. Valid values: Immediat ely Maint ainT ime: The instance will be migrated during the maintenance period of the instance. Default value: Immediat ely. |
| VSwitchId | String | No | vsw-bpxxxxxxxx | The ID of the vSwitch in the destination zone. Not e This parameter can be used only when the network type of the instance is VPC. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0FDDC511-7252- 4A4A-ADDA- 5CB1BF63873D | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=MigrateToOtherZone &DBInstanceId=dds-bpxxxxxxxx &ZoneId=cn-hangzhou-b &EffectiveTime=Immediately &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>0FDDC511-7252-4A4A-ADDA-5CB1BF63873D</RequestId>
```

`JSON` format `{`

```json
 "RequestId": "0FDDC511-7252-4A4A-ADDA-5CB1BF63873D"
```

#### 3.2.2 DescribeRegions

You can call this operation to view the regions and zones that an ApsaraDB for MongoDB instance can be created. Before you call the CreateDBInstance or CreateShardingDBInstance operation to create an instance, you must call this operation to view the regions and zones that the that ApsaraDB for MongoDB instance can be created. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRegions | The operation that you want to perform. Set the value to DescribeRegions. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Regions | Array of DdsRegion |   | An array that consists of the information of regions. |
| DdsRegion |   |   |   |
| RegionId | String | cn-qingdao | The ID of the region. |
| Zones | Array of Zone |   | An array that consists of the information of zones. |
| Zone |   |   |   |
| VpcEnabled | Boolean | true | Indicates whether VPC is supported. Valid values: t rue f alse |
| ZoneId | String | cn-hangzhou-b | The ID of the zone. |
| RequestId | String | 4E46C22C-D3B7- 4DB8-9C76- 63851BE68E20 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeRegions &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeRegionsResponse>
   <RequestId>4E46C22C-D3B7-4DB8-9C76-63851BE68E20</RequestId>
   <Regions>
      <DdsRegion>
         <RegionId>cn-hangzhou</RegionId>
         <Zones>
            <Zone>
               <VpcEnabled>true</VpcEnabled>
               <ZoneId>cn-hangzhou-i</ZoneId>
            </Zone>
            <Zone>
               <VpcEnabled>true</VpcEnabled>
               <ZoneId>cn-hangzhou-b</ZoneId>
            </Zone>
            <Zone>
               <VpcEnabled>true</VpcEnabled>
               <ZoneId>cn-hangzhou-d</ZoneId>
            </Zone>
            <Zone>
               <VpcEnabled>true</VpcEnabled>
               <ZoneId>cn-hangzhou-f</ZoneId>
            </Zone>
            <Zone>
               <VpcEnabled>true</VpcEnabled>
               <ZoneId>cn-hangzhou-MAZ5(b,e,f)</ZoneId>
            </Zone>
            <Zone>
               <VpcEnabled>true</VpcEnabled>
               <ZoneId>cn-hangzhou-g</ZoneId>
            </Zone>
         </Zones>
      </DdsRegion>
   </Regions>
</DescribeRegionsResponse>
```

`JSON` format `{`

```json
 "RequestId": "4E46C22C-D3B7-4DB8-9C76-63851BE68E20",
 "Regions": {
  "DdsRegion": [
```

`{`

```json
    "RegionId": "cn-hangzhou",
    "Zones": {
     "Zone": [
```

`{`

```json
       "VpcEnabled": true,
       "ZoneId": "cn-hangzhou-i"
```

`},` `{`

```json
       "VpcEnabled": true,
       "ZoneId": "cn-hangzhou-b"
```

`},` `{`

```json
       "VpcEnabled": true,
       "ZoneId": "cn-hangzhou-d"
```

`},` `{`

```json
       "VpcEnabled": true,
       "ZoneId": "cn-hangzhou-f"
```

`},` `{`

```json
       "VpcEnabled": true,
       "ZoneId": "cn-hangzhou-MAZ5(b,e,f)"
```

`},` `{`

```json
       "VpcEnabled": true,
       "ZoneId": "cn-hangzhou-g"
```

`]` `]`

#### 3.2.3 MigrateAvailableZone

You can call this operation to change the zone of an ApsaraDB for MongoDB instance. This operation is applicable only to replica set instances, but not to sharded cluster instances. If you have applied for a public endpoint of the instance, you must first call ReleasePublicNet workAddress to release the public endpoint. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | MigrateAvailable Zone | The operation that you want to perform. Set the value to Migrat eAvailableZone. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Not e You must specify the Vswit ch parameter if the network type of the instance is VPC. |
| ZoneId | String | Yes | cn-hangzhou-b | The ID of the destination zone to which you want to migrate the ApsaraDB for MongoDB instance. Not e The destination zone must be in the same region as the current zone of the instance. You can call the DescribeRegions operation to view the zone IDs. |
| Vswitch | String | No | vsw-bpxxxxxxxx | The ID of the vSwitch in the destination zone. Not e This parameter can be used only when the network type of the instance is VPC. |
| EffectiveTime | String | No | Immediately | The time when the instance is migrated to the destination zone. Valid values: Immediat ely: The instance will be migrated immediately. Maint ainT ime: The instance will be migrated during the maintenance period of the instance. Default value: Immediat ely. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0FDDC511-7252- 4A4A-ADDA- 5CB1BF63873D | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=MigrateAvailableZone &DBInstanceId=dds-bpxxxxxxxx &ZoneId=cn-hangzhou-b &EffectiveTime=Immediately &<Common request parameters>
```

Sample success responses `XML` format

```xml
<MigrateAvailableZoneResponse>
   <RequestId>0FDDC511-7252-4A4A-ADDA-5CB1BF63873D</RequestId>
</MigrateAvailableZoneResponse>
```

`JSON` format `{`

```json
 "RequestId": "0FDDC511-7252-4A4A-ADDA-5CB1BF63873D"
```

### 3.3 Resource management

#### 3.3.1 DescribeAvailableResource

You can call this operation to view the ApsaraDB for MongoDB instances that can be created in a specified zone. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAvailable Resource | The operation that you want to perform. Set the value to DescribeAvailableResource. |
| RegionId | String | Yes | cn-hangzhou | The region ID. You can call the DescribeRegions operation to view the region IDs. |

| A | psaraDB for MongoD | B |   |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ZoneId | String | No | cn-hangzhou-h | The zone ID of the instance. You can call the DescribeRegions operation to view the zone IDs. |
| InstanceChargeTy pe | String | No | PrePaid | The billing method. Valid values: PrePaid: subscription. PostPaid: pay-as-you-go. Not e Default value: PrePaid. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 344EE51D-8850- 4935-B68B- 58A8F4DCE3BD | The ID of the request. |
| SupportedDBTy pes | Array of SupportedDBTy pe |   | The database type supported. |
| SupportedDBTy pe |   |   |   |
| AvailableZones | Array of AvailableZone |   | The zone ID of the instance. |
| AvailableZone |   |   |   |
| RegionId | String | cn-hangzhou | The region ID of the instance. |
| SupportedEngi neVersions | Array of SupportedEngi neVersion |   | The versions of the storage engine. |
| SupportedEngi neVersion |   |   |   |
| SupportedEngi nes | Array of SupportedEngi ne |   | The storage engine supported. |
| SupportedEngi ne |   |   |   |

| D | eveloper Guide·AP | I Reference |   | ApsaraDB for MongoD | B |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Engine | String | WiredTiger | The storage engine of the instance. |
| SupportedNod eTypes | Array of SupportedNod eType |   | The instance types supported. |
| SupportedNod eType |   |   |   |
| AvailableResour ces | Array of AvailableResour ce |   | The details of available resources. |
| AvailableResour ce |   |   |   |
| InstanceClass | String | dds.mongo.2xlarge | The category of the instance. |
| InstanceClassRe mark | String | 8 vCPUs, 32 GiB (maximum connections: 8000 IOPS: 14000) | The instance type. |
| NetworkTypes | String | VPC | The network type of the instance. |
| NodeType | String | 3 | The number of nodes in the instance. |
| Version | String | 4.0 | The database engine version of the instance. |
| ZoneId | String | cn-hangzhou-h | The zone ID of the instance. |
| DbType | String | sharding | The database engine of the instance. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeAvailableResource &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>344EE51D-8850-4935-B68B-58A8F4DCE3BD</RequestId> <SupportedDBTypes>
    <DbType>sharding</DbType>
</SupportedDBTypes> <SupportedDBTypes>
    <AvailableZones>
        <ZoneId>cn-hangzhou-h</ZoneId>
        <RegionId>cn-hangzhou</RegionId>
    </AvailableZones>
    <AvailableZones>
        <SupportedEngineVersions>
            <Version>4.0</Version>
        </SupportedEngineVersions>
        <SupportedEngineVersions>
            <SupportedEngines>
                <Engine>WiredTiger</Engine>
            </SupportedEngines>
            <SupportedEngines>
                <SupportedNodeTypes>
                    <NetworkTypes>VPC</NetworkTypes>
                    <NodeType>3</NodeType>
                </SupportedNodeTypes>
                <SupportedNodeTypes>
                    <AvailableResources>
                        <InstanceClassRemark>8 vCPUs, 32 GiB (maximum connections: 8000 IOP
S: 14000)</InstanceClassRemark>
                        <InstanceClass>dds.mongo.2xlarge</InstanceClass>
                    </AvailableResources>
                </SupportedNodeTypes>
            </SupportedEngines>
        </SupportedEngineVersions>
    </AvailableZones>
</SupportedDBTypes>
```

`JSON` format `{`

```json
    "RequestId":"344EE51D-8850-4935-B68B-58A8F4DCE3BD",
    "SupportedDBTypes":[
```

`{`

```json
            "DbType":"sharding"
```

`},` `{`

```json
            "AvailableZones":[
```

`{`

```json
                    "ZoneId":"cn-hangzhou-h",
                    "RegionId":"cn-hangzhou"
```

`},` `{`

```json
                    "SupportedEngineVersions":[
```

`{`

```json
                            "Version":"4.0"
```

`},` `{`

```json
                            "SupportedEngines":[
```

`{`

```json
                                    "Engine":"WiredTiger"
```

`},` `{`

```json
                                    "SupportedNodeTypes":[
```

`{`

```json
                                            "NetworkTypes":"VPC",
                                            "NodeType":"3"
```

`},` `{`

```json
                                            "AvailableResources":[
```

`{`

```json
                                                    "InstanceClassRemark":"8 vCPUs, 32 GiB
(maximum connections: 8000 IOPS: 14000)",
                                                    "InstanceClass":"dds.mongo.2xlarge"
```

`]` `]` `]` `]` `]` `]`

### 3.4 Connection management

#### 3.4.1 AllocatePublicNetworkAddress

You can call this operation to assign a public endpoint to an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AllocatePublicNet workAddress | The operation that you want to perform. Set the value to Allocat ePublicNet workAddress. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Not e If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| NodeId | String | No | s-bpxxxxxxxx | The ID of the mongos, shard, or Configserver node in the sharded cluster instance. Not e This parameter is valid only if you set the DBInst anceId parameter to the ID of a sharded cluster instance. You can call the DescribeDBInstanceAttribut e operation to view the ID of the mongos, shard, or Configserver node. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B6D17591-B48B- 4D31-9CD6- 9B9796B2270A | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.aliyuncs.com/? Action=AllocatePublicNetworkAddress &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AllocatePublicNetworkAddressResponse>
   <RequestId>B6D17591-B48B-4D31-9CD6-9B9796B2270A</RequestId>
</AllocatePublicNetworkAddressResponse>
```

`JSON` format `{`

```json
 "RequestId": "B6D17591-B48B-4D31-9CD6-9B9796B2270A"
```

#### 3.4.2 ReleasePublicNetworkAddress

You can call this operation to release the public endpoint of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ReleasePublicNet workAddress | The operation that you want to perform. Set the value to ReleasePublicNet workAddress. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Not e If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| NodeId | String | No | s-bpxxxxxxxx | A sharded cluster instance consists of three components: mongos, shard, and Configserver. Not e This parameter is valid only if you set the DBInst anceId parameter to the ID of a sharded cluster instance. You can call the DescribeDBInst anceAt t ri but e operation to view the ID of the mongos, shard, or Configserver node. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1D6AFE36-1AF5- 4DE4-A954- 672159D4CC69 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ReleasePublicNetworkAddress &DBInstanceId=dds-bpxxxxxxxx &s-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ReleasePublicNetworkAddressResponse>
   <RequestId>B6D17591-B48B-4D31-9CD6-9B9796B2270A</RequestId>
</ReleasePublicNetworkAddressResponse>
```

`JSON` format `{`

```json
 "RequestId": "1D6AFE36-1AF5-4DE4-A954-672159D4CC69"
```

#### 3.4.3 ModifyInstanceVpcAuthMode

You can call this operation to enable or disable password-free access from the same VPC as an ApsaraDB for MongoDB instance. Before you call this operation, make sure that the following requirements are met: A replica set or sharded cluster instance is used. The database engine version of the instance is MongoDB 4.0 or 4.2. You can call the DescribeDBInst anceAt t ribut e operation to view the database engine version of the instance. If necessary, you can call the UpgradeDBInst anceEngineVersion operation to upgrade the database engine. The network type of the instance must be VPC. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyInstanceVp cAuthMode | The operation that you want to perform. Set the value to Modif yInst anceVpcAut hMode. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| RegionId | String | No | cn-hangzhou | The region ID of the instance. You can call the DescribeDBInst anceAt t ribut e operation to view the region ID of the instance. |
| NodeId | String | No | s-bpxxxxxxxx | The ID of the mongos node in the sharded cluster instance. Not e This parameter is valid only if you select a sharded cluster instance. |
| VpcAuthMode | String | No | Open | Specifies whether to enable password- free access within the VPC. Valid values: Open: enables password-free access within the VPC. Close: disables password-free access within the VPC. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | BA51E9D9-B14A- 4542-B6E6- 7DE00BECCB8C | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyInstanceVpcAuthMode &DBInstanceId=dds-bpxxxxxxxx &VpcAuthMode=Open &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyInstanceVpcAuthModeResponse>
      <RequestId>BA51E9D9-B14A-4542-B6E6-7DE00BECCB8C</RequestId>
</ModifyInstanceVpcAuthModeResponse>
```

`JSON` format `{`

```json
    "RequestId": "BA51E9D9-B14A-4542-B6E6-7DE00BECCB8C"
```

#### 3.4.4 DescribeShardingNetworkAddress

You can call this operation to view the connection information of an ApsaraDB for MongoDB sharded cluster instance. This operation supports sharded cluster instances only. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSharding NetworkAddress | The operation that you want to perform. Set the value to DescribeShardingNet workAddress. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos, shard, and Configserver node in the sharded cluster instance. Not e You can call the DescribeDBInst anceAt t ribut e operation to view the ID of the mongos, shard, or Configserver node. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CompatibleCon nections | Array of CompatibleCon nection |   | An array that consists of the endpoints of DynamoDB instances. |
| CompatibleCon nection |   |   |   |
| ExpiredTime | String | 2591963 | The remaining period of the classic network endpoint. Unit: seconds. |
| IPAddress | String | 10.140.xxx.xx | The IP address of the instance. |
| NetworkAddres s | String | dds- bpxxxxxxxxxxxxxx.m ongodb.rds.aliyuncs .com | The endpoint of the instance. |
| NetworkType | String | VPC | The network type of the endpoint. Valid values: VPC Classic Public |
| Port | String | 3717 | The port number. |
| VPCId | String | vpc-bpxxxxxxxx | The ID of the VPC. Not e This parameter is returned when the network type is VPC. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| VswitchId | String | vsw-bpxxxxxxxx | The ID of the vSwitch in the specified VPC. Not e This parameter is returned when the network type is VPC. |
| NetworkAddres ses | Array of NetworkAddres s |   | An array that consists of the endpoints of ApsaraDB for MongoDB instances. |
| NetworkAddres s |   |   |   |
| ExpiredTime | String | 2591963 | The remaining period of the classic network endpoint. Unit: seconds. |
| IPAddress | String | 10.140.xxx.xx | The IP address of the instance. |
| NetworkAddres s | String | s- bpxxxxxxxx.mongod b.rds.aliyuncs.com | The endpoint of the instance. |
| NetworkType | String | VPC | The network type of the endpoint. VPC Classic Public |
| NodeId | String | s-bpxxxxxxxx | The ID of the mongos node. |
| NodeType | String | mongos | The type of the node. Valid values: mongos shard conf igserver |
| Port | String | 3717 | The port number. |
| Role | String | Primary | The role of the node. Valid values: Primary Secondary |

| Parameter | Type | Example | Description |
|---|---|---|---|
| VPCId | String | vpc-bpxxxxxxxx | The ID of the VPC. Not e This parameter is returned when the network type is VPC. |
| VswitchId | String | vsw-bpxxxxxxxx | The ID of the vSwitch in the specified VPC. Not e This parameter is returned when the network type is VPC. |
| RequestId | String | 18D8AAFD-6BEB- 420F-8164- 810CB0C0AA39 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeShardingNetworkAddress &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CompatibleConnections>
    <NetworkAddress>dds-bpxxxxxxxxxxxxxx.mongodb.rds.aliyuncs.com</NetworkAddress>
    <VPCId>vpc-bpxxxxxxxx</VPCId>
    <NetworkType>VPC</NetworkType>
    <ExpiredTime>2591963</ExpiredTime>
    <Port>3717</Port>
    <IPAddress>10.140.xxx.xx</IPAddress>
    <VswitchId>vsw-bpxxxxxxxx</VswitchId>
</CompatibleConnections> <RequestId>18D8AAFD-6BEB-420F-8164-810CB0C0AA39</RequestId> <NetworkAddresses>
    <Role>Primary</Role>
    <NetworkAddress>s-bpxxxxxxxx.mongodb.rds.aliyuncs.com</NetworkAddress>
    <VPCId>vpc-bpxxxxxxxx</VPCId>
    <NetworkType>VPC</NetworkType>
    <NodeType>mongos</NodeType>
    <ExpiredTime>2591963</ExpiredTime>
    <Port>3717</Port>
    <NodeId>s-bpxxxxxxxx</NodeId>
    <IPAddress>10.140.xxx.xx</IPAddress>
    <VswitchId>vsw-bpxxxxxxxx</VswitchId>
</NetworkAddresses>
```

`JSON` format `{`

```json
    "CompatibleConnections":[
```

`{`

```json
            "NetworkAddress":"dds-bpxxxxxxxxxxxxxx.mongodb.rds.aliyuncs.com",
            "VPCId":"vpc-bpxxxxxxxx",
            "NetworkType":"VPC",
            "ExpiredTime":"2591963",
            "Port":"3717",
            "IPAddress":"10.140.xxx.xx",
            "VswitchId":"vsw-bpxxxxxxxx"
```

`],`

```json
    "RequestId":"18D8AAFD-6BEB-420F-8164-810CB0C0AA39",
    "NetworkAddresses":[
```

`{`

```json
            "Role":"Primary",
            "NetworkAddress":"s-bpxxxxxxxx.mongodb.rds.aliyuncs.com",
            "VPCId":"vpc-bpxxxxxxxx",
            "NetworkType":"VPC",
            "NodeType":"mongos",
            "ExpiredTime":"2591963",
            "Port":"3717",
            "NodeId":"s-bpxxxxxxxx",
            "IPAddress":"10.140.xxx.xx",
            "VswitchId":"vsw-bpxxxxxxxx"
```

`]`

#### 3.4.5 ModifyDBInstanceConnectionString

You can call this operation to modify the connection string of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstance ConnectionString | The operation that you want to perform. Set the value to Modif yDBInst anceConnect ionSt ring . |
| CurrentConnectio nString | String | Yes | s- bpxxxxxxxx.mong odb.rds.aliyuncs. com | The current connection string, which is to be modified. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Not e If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| NewConnectionSt ring | String | Yes | aliyuntest111 | The new connection string. It must be 8 to 64 characters in length and can contain letters and digits. It must start with a lowercase letter. Not e You only need to specify the prefix of the connection string. The content other than the prefix cannot be modified. |
| NodeId | String | No | s-bpxxxxxxxx | The ID of the mongos node in the sharded cluster instance. Only one mongos ID can be specified in each call. Not e This parameter is valid only if you set the DBInst anceId parameter to the ID of a sharded cluster instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | FF36A84C-0694- 42D0-861D- C383E8E4FAAF | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyDBInstanceConnectionString &CurrentConnectionString=s-bpxxxxxxxx.mongodb.rds.aliyuncs.com &NewConnectionString=aliyuntest111 &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceConnectionStringResponse>
   <RequestId>FF36A84C-0694-42D0-861D-C383E8E4FAAF</RequestId>
</ModifyDBInstanceConnectionStringResponse>
```

`JSON` format `{`

```json
 "RequestId": "FF36A84C-0694-42D0-861D-C383E8E4FAAF"
```

#### 3.4.6 ReleaseNodePrivateNetworkAddress

You can call this operation to release the internal endpoint of the shard or Configserver node of a sharded cluster instance. This operation is only applicable to sharded cluster instances. For more information, see Release endpoints of shard or Configserver nodes. This operation releases the internal endpoint of the node. If you have also applied for a public endpoint of the node and want to release it, you can call the ReleasePublicNetworkAddress operation to release the public endpoint. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ReleaseNodePriva teNetworkAddres s | The operation that you want to perform. Set the value to ReleaseNodePrivat eNet workAddre ss. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the sharded cluster instance. |
| NodeId | String | Yes | d-bpxxxxxxxx | The ID of the shard or Configserver node. Not e You can call the DescribeDBInstanceAttribute operation to query the ID of the shard or Configserver node. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| NetworkType | String | Yes | VPC | The network type of the internal endpoint. Valid values: VPC Classic Not e You can call the Describeshardingendpoint address operation to query the network type of the internal endpoint. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0FDDC511-7252- 4A4A-ADDA- 5CB1BF63873D | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.aliyuncs.com/? Action=ReleaseNodePrivateNetworkAddress &DBInstanceId=dds-bpxxxxxxxx &NodeId=d-bpxxxxxxxx &NetworkType=VPC &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ReleaseNodePrivateNetworkAddressResponse>
   <RequestId>EFD65226-08CC-4C4D-B6A4-CB3C382F67B0</RequestId>
</ReleaseNodePrivateNetworkAddressResponse>
```

`JSON` format `{`

```json
 "RequestId":"0FDDC511-7252-4A4A-ADDA-5CB1BF63873D"
```

### 3.5 Instance information query

#### 3.5.1 DescribeReplicaSetRole

You can call this operation to view the role and connection information of an ApsaraDB for MongoDB instance. This operation is applicable only to replica set instances, but not to sharded cluster instances. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeReplicaS etRole | The operation that you want to perform. Set the value to DescribeReplicaSet Role. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DB4A0595-FCA9- 437F-B2BB- 25DBFC009D3E | The ID of the request. |
| DBInstanceId | String | dds-bpxxxxxxxx | The ID of the instance. |
| ReplicaSets | Array of ReplicaSet |   | An array that consists of the information of replica set instance roles. |
| ReplicaSet |   |   |   |
| ConnectionDom ain | String | dds- bpxxxxxxxx.mongod b.rds.aliyuncs.com | The endpoint of the node. |
| ConnectionPort | String | 3717 | The port of the node. |
| ExpiredTime | String | 1209582 | The remaining period of the classic network endpoint. Unit: seconds. |
| NetworkType | String | VPC | The network type of the endpoint. Valid values: VPC Classic Public |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ReplicaSetRole | String | Primary | The role of the node in the replica set instance. Primary Secondary |
| RoleId | String | 651xxxxx | The role ID of the node. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeReplicaSetRole &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeReplicaSetRoleResponse>
   <RequestId>7762D0FF-F34D-4DAF-9D06-6C1C28CC98CD</RequestId>
   <DBInstanceId>dds-bpxxxxxxxx</DBInstanceId>
   <ReplicaSets>
      <ReplicaSet>
         <NetworkType>Classic</NetworkType>
         <ConnectionPort>3717</ConnectionPort>
         <ReplicaSetRole>Primary</ReplicaSetRole>
         <ConnectionDomain>dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com</ConnectionDomain>
         <ExpiredTime>12xxxxx</ExpiredTime>
         <RoleId>55xxxxx</RoleId>
      </ReplicaSet>
      <ReplicaSet>
         <NetworkType>Classic</NetworkType>
         <ConnectionPort>3717</ConnectionPort>
         <ReplicaSetRole>Secondary</ReplicaSetRole>
         <ConnectionDomain>dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com</ConnectionDomain>
         <ExpiredTime>12xxxxx</ExpiredTime>
         <RoleId>55xxxxx</RoleId>
      </ReplicaSet>
      <ReplicaSet>
         <NetworkType>VPC</NetworkType>
         <ConnectionPort>3717</ConnectionPort>
         <ReplicaSetRole>Primary</ReplicaSetRole>
         <ConnectionDomain>dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com</ConnectionDomain>
         <RoleId>55xxxxx</RoleId>
      </ReplicaSet>
      <ReplicaSet>
         <NetworkType>VPC</NetworkType>
         <ConnectionPort>3717</ConnectionPort>
         <ReplicaSetRole>Secondary</ReplicaSetRole>
         <ConnectionDomain>dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com</ConnectionDomain>
         <RoleId>55xxxxx</RoleId>
      </ReplicaSet>
   </ReplicaSets>
</DescribeReplicaSetRoleResponse>
```

`JSON` format `{`

```json
 "RequestId": "7762D0FF-F34D-4DAF-9D06-6C1C28CC98CD",
 "DBInstanceId": "dds-bpxxxxxxxx",
 "ReplicaSets": {
  "ReplicaSet": [
```

`{`

```json
    "NetworkType": "Classic",
    "ConnectionPort": "3717",
    "ReplicaSetRole": "Primary",
    "ConnectionDomain": "dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com",
    "ExpiredTime": "12xxxxx",
    "RoleId": "55xxxxx"
```

`},` `{`

```json
    "NetworkType": "Classic",
    "ConnectionPort": "3717",
    "ReplicaSetRole": "Secondary",
    "ConnectionDomain": "dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com",
    "ExpiredTime": "12xxxxx",
    "RoleId": "55xxxxx"
```

`},` `{`

```json
    "NetworkType": "VPC",
    "ConnectionPort": "3717",
    "ReplicaSetRole": "Primary",
    "ConnectionDomain": "dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com",
    "RoleId": "55xxxxx"
```

`},` `{`

```json
    "NetworkType": "VPC",
    "ConnectionPort": "3717",
    "ReplicaSetRole": "Secondary",
    "ConnectionDomain": "dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com",
    "RoleId": "55xxxxx"
```

`]`

#### 3.5.2 DescribeKernelReleaseNotes

You can call this operation to view the release notes of the minor database versions of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeKernelRel easeNotes | The operation that you want to perform. Set the value to DescribeKernelReleaseNot es. |
| KernelVersion | String | No | mongodb 20180 _ 522 0.4.8 _ | The minor version of the database. Example: mongodb 20180522 0.4.8. _ _ If you specify this parameter, a list of versions later than the version specified is returned. If you do not specify this parameter, a list of all versions is returned. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ReleaseNotes | Array of ReleaseNote |   | An array that consists of the information of version release notes. |
| ReleaseNote |   |   |   |
| KernelVersion | String | mongodb 20180619 _ 0.4.9 _ | The version of the database. |
| ReleaseNote | String | Released the balancer switch limit for a sharded set | The release notes. |
| RequestId | String | F01D4DDA-CB72- 4083-B399- AF4642294FE6 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeKernelReleaseNotes &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>F01D4DDA-CB72-4083-B399-AF4642294FE6</RequestId> <ReleaseNotes>
    <ReleaseNote>
        <KernelVersion>mongodb_20180619_0.4.9</KernelVersion>
        <ReleaseNote>Released the balancer switch limit for a sharded set</ReleaseNote>
    </ReleaseNote>
</ReleaseNotes>
```

`JSON` format `{`

```json
    "RequestId":"F01D4DDA-CB72-4083-B399-AF4642294FE6",
    "ReleaseNotes":
```

`{`

```json
        "ReleaseNote":[
```

`{`

```json
                "KernelVersion":"mongodb_20180619_0.4.9",
                "ReleaseNote":"Released the balancer limit for a sharded set"
```

`]`

#### 3.5.3 DescribeAvailableEngineVersion

You can call this operation to view the database engine versions that an ApsaraDB for MongoDB instance can be upgraded to. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAvailable EngineVersion | The operation that you want to perform. Set the value to DescribeAvailableEngineVersion. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 52507B6B-003B- 47A3-A0A3- 9FE992C7A243 | The ID of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| EngineVersions | List | {"EngineVersion": ["4.0" ]} | The databse engine versions that the ApsaraDB for MongoDB instance can be upgraded to. Not e An empty string is returned if the latest version is being used. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeAvailableEngineVersion &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeAvailableEngineVersionResponse>
   <EngineVersions>
      <EngineVersion>4.0</EngineVersion>
   </EngineVersions>
   <RequestId>52507B6B-003B-47A3-A0A3-9FE992C7A243</RequestId>
</DescribeAvailableEngineVersionResponse>
```

`JSON` format `{`

```json
 "EngineVersions": {
  "EngineVersion": [
   "4.0"
```

`]` `},`

```json
 "RequestId": "52507B6B-003B-47A3-A0A3-9FE992C7A243"
```

#### 3.5.4 DescribeDBInstances

You can call this operation to query the list of ApsaraDB for MongoDB instances. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstan ces | The operation that you want to perform. Set the value to DescribeDBInst ances. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be a positive integer. Default value: 1. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| ReplicationFactor | String | No | 3 | The number of nodes in a replica set instance. Valid values: 3, 5, and 7. |
| DBInstanceType | String | No | replicate | The architecture type of the instance. Valid values: sharding: sharded cluster instance replicat e: replica set or standalone instance Default value: replicat e |
| Engine | String | No | MongoDB | The database engine. Valid value: MongoDB. |
| DBInstanceId | String | No | dds-bpxxxxxxxx | The ID of the instance. |
| DBInstanceDescri ption | String | No | Test database | The description of the instance. |
| ExpireTime | String | No | 2019-12- 26T16:00Z | The time when the instance expires. |
| DBInstanceStatus | String | No | ACTIVATION | The status of the instance. For more information, see Inst ance st at es. |
| DBInstanceClass | String | No | dds.mongo.mid | The instance type. For more information, see Inst ance t ypes in ApsaraDB for MongoDB Product Introduction. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| EngineVersion | String | No | 4.0 | The database engine version of the instance. Valid values: 3.2 3.4 4.0 4.2 |
| NetworkType | String | No | VPC | The network type of the instances. Valid values: Classic VPC |
| VpcId | String | No | vpc-bpxxxxxxxx | The ID of the VPC. |
| VSwitchId | String | No | vsw-bpxxxxxxxx | The ID of the vSwitch in the specified VPC. |
| ChargeType | String | No | PostPaid | The billing method of the instance. Valid values: PrePaid: subscription Post Paid: pay-as-you-go |
| ZoneId | String | No | cn-hangzhou-b | The zone ID of the instance. You can call the DescribeRegions operation to query the zone IDs. |
| Expired | String | No | true | Specifies whether the instance has expired. Valid values: t rue: The instance has expired. f alse: The instance has not expired. |
| ResourceGroupId | String | No | rg-axxxxxxxx | The ID of the resource group. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Tag.N.Key | String | No | testdatabase | The key of the instance tag. Valid values of N: 1 to 20. The tag key can be up to 64 characters in length. It cannot start with aliyun , acs: , http:// , or https:// . Not e It cannot be an empty string. |
| Tag.N.Value | String | No | apitest | The value of the instance tag. Valid values of N: 1 to 20. The tag value can be up to 128 characters in length. It cannot start with aliyun , acs: , http:// , or https:// . Not e Tag.N.Value can be an empty string. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number of the returned page. |
| TotalCount | Integer | 1 | The number of the instances in the query results. |
| PageSize | Integer | 30 | The number of entries return on each page. |
| RequestId | String | A10B8ECB-0BA0- 4EC6-93A5- C65FDEDA07CB | The ID of the request. |
| DBInstances | Array of DBInstance |   | An array that consists of the information of instances. |
| DBInstance |   |   |   |
| ChargeType | String | PostPaid | The billing method of the instance. PrePaid: subscription Post Paid: pay-as-you-go |

| Parameter | Type | Example | Description |
|---|---|---|---|
| CreationTime | String | 2018-09- 25T06:33:07Z | The time when the instance was created. The time is in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| DBInstanceClas s | String | dds.mongo.mid | The instance type |
| DBInstanceDesc ription | String | Test database | The description of the instance. |
| DBInstanceId | String | dds-bpxxxxxxxx | The ID of the instance. |
| DBInstanceStat us | String | Running | The status of the instance. |
| DBInstanceStor age | Integer | 20 | The storage capacity of the instance. |
| DBInstanceType | String | sharding | The architecture type of the instance. sharding: sharded cluster instance replicat e: replica set instance |
| DestroyTime | String | 2019-03- 05T11:26:02Z | The time when the instance was released. The time is in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. Not e Subscription instances are released seven days after expiration. After an instance is released, its data is deleted and cannot be restored. Pay-as-you-go instances will be locked when the payment is overdue for more than 24 hours. The instance will be released when it is overdue for more than seven days. The data of released instances will be deleted and cannot be recovered. |
| Engine | String | MongoDB | The database engine of the instance |

| Parameter | Type | Example | Description |
|---|---|---|---|
| EngineVersion | String | 4.0 | The version of the database engine. |
| ExpireTime | String | 2019-11-25T16:00Z | The time when the instance expires. The time is in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. |
| KindCode | String | 1 | The kind code of the instance. Valid values: 0: physical machine 1: Elastic Compute Service (ECS) 2: Docker cluster 18: Kubernetes cluster |
| LastDowngrade Time | String | 20190308 | The last time when the instance was downgraded. |
| LockMode | String | Unlock | Indicates whether the instance is locked. Unlock: The instance is not locked. ManualLock: The instance has been manually locked. LockByExpirat ion: The instance has been locked upon expiration. LockByRest orat ion: The instance has been locked for a rollback. LockByDiskQuot a: The instance has been automatically locked because its storage space is exhausted. Released: The instance has been released. You cannot unlock a released instance. After an instance is released, you can only use a backup to restore the data of the instance to a new instance. This process requires a long time. |
| MongosList | Array of MongosAttribut e |   | An array that consists of the information of mongos nodes. Not e This parameter is returned if the instance is a sharded cluster instance. |
| MongosAttribut e |   |   |   |

| eveloper Guide·AP | I Reference |   | ApsaraDB for MongoD |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| NodeClass | String | dds.mongos.mid | The specifications of the mongos node. |
| NodeDescriptio n | String | Test mongos | The description of the mongos node. |
| NodeId | String | s-bpxxxxxxxx | The ID of the mongos node. |
| NetworkType | String | VPC | The network type of the instance. Classic VPC |
| RegionId | String | cn-hangzhou | The region ID of the instance. |
| ReplicationFact or | String | 3 | The number of the nodes in the instance. Not e This parameter is returned if the instance is a replica set instance. |
| ResourceGroupI d | String | rg-axxxxxxxx | The ID of the resource group. |
| ShardList | Array of ShardAttribute |   | An array that consists of the information of shard nodes. Not e This parameter is returned if the instance is a sharded cluster instance. |
| ShardAttribute |   |   |   |
| NodeClass | String | dds.shard.mid | The specifications of the shard node. |
| NodeDescriptio n | String | Test shard | The description of the shard node. |
| NodeId | String | d-bpxxxxxxxx | The ID of the shard node. |
| NodeStorage | Integer | 20 | The storage capacity of the shard node. Unit: GB. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Tags | Array of Tag |   | An array that consists of the information of instance tags. |
| Tag |   |   |   |
| Key | String | test | The key of the instance tag. |
| Value | String | api | The value of the instance tag. |
| VpcAuthMode | String | close | Indicates whether password-free access within the VPC is enabled. Valid values: Open: Password-free access is enabled. Close: Password-free access is disabled. |
| ZoneId | String | cn-hangzhou-b | The zone ID of the instance. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeDBInstances &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>1</TotalCount> <PageSize>30</PageSize> <RequestId>A10B8ECB-0BA0-4EC6-93A5-C65FDEDA07CB</RequestId> <PageNumber>1</PageNumber> <DBInstances>
    <EngineVersion>4.0</EngineVersion>
    <ReplicationFactor>3</ReplicationFactor>
    <DBInstanceStatus>Running</DBInstanceStatus>
    <ZoneId>cn-hangzhou-b</ZoneId>
    <ResourceGroupId>rg-axxxxxxxx</ResourceGroupId>
    <DBInstanceClass>dds.mongo.mid</DBInstanceClass>
    <DestroyTime>2019-03-05T11:26:02Z</DestroyTime>
    <DBInstanceType>sharding</DBInstanceType>
    <LockMode>Unlock</LockMode>
    <DBInstanceId>dds-bpxxxxxxxx</DBInstanceId>
    <VpcAuthMode>close</VpcAuthMode>
    <NetworkType>VPC</NetworkType>
    <ChargeType>PostPaid</ChargeType>
    <LastDowngradeTime>20190308</LastDowngradeTime>
    <DBInstanceStorage>20</DBInstanceStorage>
    <CreationTime>2018-09-25T06:33:07Z</CreationTime>
    <RegionId>cn-hangzhou</RegionId>
    <ExpireTime>2019-11-25T16:00Z</ExpireTime>
    <KindCode>1</KindCode>
    <Engine>MongoDB</Engine>
    <DBInstanceDescription>Test database</DBInstanceDescription>
</DBInstances> <DBInstances>
    <ShardList>
        <NodeStorage>20</NodeStorage>
        <NodeId>d-bpxxxxxxxx</NodeId>
        <NodeClass>dds.shard.mid</NodeClass>
        <NodeDescription>Test shard</NodeDescription>
    </ShardList>
    <MongosList>
        <NodeId>s-bpxxxxxxxx</NodeId>
        <NodeClass>dds.mongos.mid</NodeClass>
        <NodeDescription>Test mongos</NodeDescription>
    </MongosList>
    <Tags>
        <Value>api</Value>
        <Key>test</Key>
    </Tags>
</DBInstances>
```

`JSON` format `{`

```json
 "TotalCount": "1",
 "PageSize": "30",
 "RequestId": "A10B8ECB-0BA0-4EC6-93A5-C65FDEDA07CB",
 "PageNumber": "1",
 "DBInstances": [{
  "EngineVersion": "4.0",
  "ReplicationFactor": "3",
  "DBInstanceStatus": "Running",
  "ZoneId": "cn-hangzhou-b",
  "ResourceGroupId": "rg-axxxxxxxx",
  "DBInstanceClass": "dds.mongo.mid",
  "DestroyTime": "2019-03-05T11:26:02Z",
  "DBInstanceType": "sharding",
  "LockMode": "Unlock",
  "DBInstanceId": "dds-bpxxxxxxxx",
  "VpcAuthMode": "close",
  "NetworkType": "VPC",
  "ChargeType": "PostPaid",
  "LastDowngradeTime": "20190308",
  "DBInstanceStorage": "20",
  "CreationTime": "2018-09-25T06:33:07Z",
  "RegionId": "cn-hangzhou",
  "ExpireTime": "2019-11-25T16:00Z",
  "KindCode": "1",
  "Engine": "MongoDB",
  "DBInstanceDescription": "Test database",
 }, {
  "ShardList": [{
   "NodeStorage": "20",
   "NodeId": "d-bpxxxxxxxx",
   "NodeClass": "dds.shard.mid",
   "NodeDescription": "Test shard"
  }],
  "MongosList": [{
   "NodeId": "s-bpxxxxxxxx",
   "NodeClass": "dds.mongos.mid",
   "NodeDescription": "Test mongos"
  }],
  "Tags": [{
   "Value": "api",
   "Key": "test"
```

`}]` `}]`

#### 3.5.5 DescribeDBInstanceAttribute

You can call this operation to view the details of a MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstan ceAttribute | The operation that you want to perform. Set the value to DescribeDBInst anceAt t ribut e. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| Engine | String | No | MongoDB | The database engine. Set the value to MongoDB. |
| ResourceGroupId | String | No | rg-axxxxxxxx | The ID of the resource group. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C373EED9-5125- 4DD9-89DB- FB1ECD2C2B4F | The ID of the request. |
| DBInstances | Array of DBInstance |   | An array that consists of the information of the instance. |
| DBInstance |   |   |   |
| ChargeType | String | PostPaid | The billing method of the instance. PrePaid: subscription Post Paid: pay-as-you-go |
| ConfigserverLis t | Array of ConfigserverAtt ribute |   | An array that consists of the information of Configserve nodes. Not e This parameter is returned if the instance type is sharded cluster. |
| ConfigserverAtt ribute |   |   |   |
| ConnectString | String | mongodb://root:** **@dds- bpxxxxxxxxxxxxxx- cs1730- pub.mongodb.rds.al iyuncs.com:3717 | The connection string URI of the Configserver node. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| MaxConnection s | Integer | 0 | The maximum number of connections of the Configserver node. |
| MaxIOPS | Integer | 1000 | The maximum input/output operations per second (IOPS) of the Configserver node. |
| NodeClass | String | dds.cs.mid | The specifications of the Configserver node. |
| NodeDescriptio n | String | testConfigserver | The name of the Configserver node. |
| NodeId | String | dds- bpxxxxxxxxxxxxxx-cs | The ID of the Configserver node. |
| NodeStorage | Integer | 20 | The storage capacity of the Configserver node. |
| Port | Integer | 3717 | The port of the Configserver node. |
| CreationTime | String | 2018-11- 21T05:10:00Z | The time when the instance was created. The time is in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. |
| CurrentKernelV ersion | String | mongodb 20180914 _ 1.1.5 _ | The minor version of the current database of the instance. |
| DBInstanceClas s | String | dds.mongo.mid | The instance type. |
| DBInstanceDesc ription | String | Test | The name of the instance. |
| DBInstanceId | String | dds-bpxxxxxxxx | The ID of the instance. |
| DBInstanceRele aseProtection | Boolean | true | Indicates whether release protection is enabled for the instance. Valid values: t rue: Release protection is enabled. f alse: Release protection is disabled. |
| DBInstanceStat us | String | Running | The status of the instance. For more information, see Inst ance t ypes in ApsaraDB for MongoDB Product Introduction. |

| D | eveloper Guide·AP | I Reference |   | ApsaraDB for MongoD | B |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceStor age | Integer | 10 | The storage capacity of the instance. |
| DBInstanceType | String | replicate | The architecture type of the instance. replicat e: replica set instance sharding: sharded cluster instance |
| Engine | String | MongoDB | The database engine of the instance. |
| EngineVersion | String | 3.4 | The version of the database engine. |
| ExpireTime | String | 2019-04-08T16:00Z | The time when the subscription instance expires. The time is in the yyyy-MM- ddTHH:mmZ format. The time is displayed in UTC. Not e This parameter is returned if the instance billing method is subscription. |
| KindCode | String | 1 | The kind code of the instance. Valid values: 0: physical machine 1: Elastic Compute Service (ECS) 2: Docker cluster 18: Kubernetes cluster |
| LastDowngrade Time | String | 2019-03-08 | The last time when the instance was downgraded. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| LockMode | String | Unlock | Indicates whether the instance is locked. Valid values: Unlock: The instance is not locked. ManualLock: The instance has been manually locked. LockByExpirat ion: The instance has been locked upon expiration. LockByRest orat ion: The instance has been locked for a rollback. LockByDiskQuot a: The instance has been automatically locked because its storage space is exhausted. Released: The instance has been released. You cannot unlock a released instance. After an instance is released, you can only use a backup to restore the data of the instance to a new instance. This process requires a long time. |
| MaintainEndTim e | String | 03:00Z | The end time of the maintenance window. The time is in the HH:mmZ format. The time is displayed in UTC. |
| MaintainStartTi me | String | 02:00Z | The start time of the maintenance window. The time is in the HH:mmZ format. The time is displayed in UTC. |
| MaxConnection s | Integer | 500 | The maximum number of connections of the instance. |
| MaxIOPS | Integer | 1000 | The maximum IOPS of the instance. |
| MongosList | Array of MongosAttribut e |   | An array that consists of the information of mongos nodes. Not e This parameter is returned if the instance type is sharded cluster. |
| MongosAttribut e |   |   |   |
| ConnectSting | String | s- bpxxxxxxxx.mongod b.rds.aliyuncs.com | The endpoint of the mongos node. |

| eveloper Guide·AP | I Reference |   | ApsaraDB for MongoD |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| MaxConnection s | Integer | 1000 | The maximum number of connections of the mongos node. |
| MaxIOPS | Integer | 0 | The maximum IOPS of the mongos node. |
| NodeClass | String | dds.mongos.mid | The specifications of the mongos node. |
| NodeDescriptio n | String | mongos1 | The name of the mongos node. |
| NodeId | String | s-bpxxxxxxxx | The ID of the mongos node. |
| Port | Integer | 3717 | The port of the mongos node. |
| VPCId | String | vpc- bp1xxxxxxxxxxxxxxx xxx | The VPC ID of the mongos node. |
| VSwitchId | String | vsw- bp1xxxxxxxxxxxxxxx xxx | The vSwitch ID of the mongos node. |
| VpcCloudInstan ceId | String | s-bp1xxxxxxxxxxxxx | The ID of the VPC instance for the mongos ID. |
| NetworkType | String | VPC | The network type of the instance. Valid values: Classic VPC |
| ProtocolType | String | mongodb | The access protocol type of the instance. Valid values: mongodb: the MongoDB protocol dynamodb: the DynamoDB protocol |
| ReadonlyReplic as | String | 0 | The number of read-only nodes in the instance. |
| RegionId | String | cn-hangzhou | The region ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ReplacateId | String | bls-mxxxxxxxx | The BLS channel ID of the instance. |
| ReplicaSetNam e | String | mgset-10xxxxxxxx | The name of the replica set instance. Not e This parameter is returned if the instance type is replica set. |
| ReplicaSets | Array of ReplicaSet |   | The information list of the replica set. Not e This parameter is returned if the instance type is replica set. |
| ReplicaSet |   |   |   |
| ConnectionDom ain | String | dds- bpxxxxxxxx.mongod b.rds.aliyuncs.com | The endpoint of the node. |
| ConnectionPort | String | ConnectionPort | The port of the node. |
| NetworkType | String | VPC | The network type of the node. Valid values: Classic VPC |
| ReplicaSetRole | String | Primary | The role of the node. Primary Secondary |
| VPCCloudInstan ceId | String | vpc-xxxxxxxx | The ID of the VPC instance for the node. |
| VPCId | String | vpc-bpxxxxxxxx | The VPC ID of the node. |
| VSwitchId | String | vsw-bpxxxxxxxx | The vSwitch ID of the node. |
| ReplicationFact or | String | 3 | The number of nodes in the instance. Not e This parameter is returned if the instance type is replica set. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ResourceGroupI d | String | rg-axxxxxxxx | The ID of the resource group to which the instance belongs. |
| ShardList | Array of ShardAttribute |   | An array that consists of the information of shard nodes. Not e This parameter is returned if the instance type is sharded cluster. |
| ShardAttribute |   |   |   |
| ConnectString | String | d- bpxxxxxxxxxxxxxxxxx x.mongodb.rds.aliyu ncs.com | The endpoint of the shard node. |
| MaxConnection s | Integer | 8000 | The maximum number of connections of the shard node. |
| MaxIOPS | Integer | 8000 | The maximum IOPS of the shard node. |
| NodeClass | String | dds.shard.mid | The specifications of the shard node. |
| NodeDescriptio n | String | testshard | The name of the shard node. |
| NodeId | String | d-bpxxxxxxxx | The ID of the shard node. |
| NodeStorage | Integer | 10 | The storage capacity of the shard node. |
| Port | Integer | 3717 | The port of the shard node. |
| StorageEngine | String | WiredTiger | The storage engine of the instance. |
| Tags | Array of Tag |   | An array that consists of the information of instance tags. |
| Tag |   |   |   |
| Key | String | test | The key of the instance tag. |

| A | psaraDB for Mong | oDB |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Value | String | api | The value of the instance tag. |
| VPCCloudInstan ceIds | String | s-bp1xxxxxxxxxxxxx | The ID of the VPC instance for the instance. |
| VPCId | String | vpc-bpxxxxxxxx | The ID of the VPC. |
| VSwitchId | String | vsw-bpxxxxxxxx | The ID of the vSwitch in the specified VPC. |
| VpcAuthMode | String | Open | Indicates whether password-free access within the VPC is enabled. Valid values: Open: Password-free access is enabled. Close: Password-free access is disabled. Not Support : Password-free access is not supported. |
| ZoneId | String | cn-hangzhou-b | The zone ID of the instance. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeDBInstanceAttribute &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>C373EED9-5125-4DD9-89DB-FB1ECD2C2B4F</RequestId> <DBInstances>
    <VPCCloudInstanceIds>s-bp1xxxxxxxxxxxxx</VPCCloudInstanceIds>
    <ResourceGroupId>rg-axxxxxxxx</ResourceGroupId>
    <DBInstanceType>replicate</DBInstanceType>
    <ReplicaSetName>mgset-10xxxxxxxx</ReplicaSetName>
    <StorageEngine>WiredTiger</StorageEngine>
    <MaintainEndTime>03:00Z</MaintainEndTime>
    <DBInstanceId>dds-bpxxxxxxxx</DBInstanceId>
    <NetworkType>VPC</NetworkType>
    <LastDowngradeTime>2019-03-08</LastDowngradeTime>
    <DBInstanceStorage>10</DBInstanceStorage>
    <MaintainStartTime>02:00Z</MaintainStartTime>
    <Engine>MongoDB</Engine>
    <DBInstanceDescription>Test</DBInstanceDescription>
    <ReplacateId>bls-mxxxxxxxx</ReplacateId>
<DBInstanceReleaseProtection>true</DBInstanceReleaseProtection>
```

```xml
    <DBInstanceReleaseProtection>true</DBInstanceReleaseProtection>
    <EngineVersion>3.4</EngineVersion>
    <MaxConnections>500</MaxConnections>
    <ReadonlyReplicas>0</ReadonlyReplicas>
    <ReplicationFactor>3</ReplicationFactor>
    <DBInstanceStatus>Running</DBInstanceStatus>
    <ZoneId>cn-hangzhou-b</ZoneId>
    <VPCId>vpc-bpxxxxxxxx</VPCId>
    <DBInstanceClass>dds.mongo.mid</DBInstanceClass>
    <VSwitchId>vsw-bpxxxxxxxx</VSwitchId>
    <LockMode>Unlock</LockMode>
    <MaxIOPS>1000</MaxIOPS>
    <VpcAuthMode>Open</VpcAuthMode>
    <ProtocolType>mongodb</ProtocolType>
    <CurrentKernelVersion>mongodb_20180914_1.1.5</CurrentKernelVersion>
    <ChargeType>PostPaid</ChargeType>
    <CreationTime>2018-11-21T05:10:00Z</CreationTime>
    <RegionId>cn-hangzhou</RegionId>
    <ExpireTime>2019-04-08T16:00Z</ExpireTime>
    <KindCode>1</KindCode>
</DBInstances> <DBInstances>
    <ShardList>
        <NodeClass>dds.shard.mid</NodeClass>
        <NodeDescription>testshard</NodeDescription>
        <MaxConnections>8000</MaxConnections>
        <Port>3717</Port>
        <NodeStorage>10</NodeStorage>
        <NodeId>d-bpxxxxxxxx</NodeId>
        <ConnectString>d-bpxxxxxxxxxxxxxxxxxx.mongodb.rds.example.com</ConnectString>
        <MaxIOPS>8000</MaxIOPS>
    </ShardList>
    <ConfigserverList>
        <NodeClass>dds.cs.mid</NodeClass>
        <NodeDescription>testConfigserver</NodeDescription>
        <MaxConnections>0</MaxConnections>
        <Port>3717</Port>
        <NodeStorage>20</NodeStorage>
        <NodeId>dds-bpxxxxxxxxxxxxxx-cs</NodeId>
        <ConnectString>mongodb://root:****@dds-bpxxxxxxxxxxxxxx-cs1730-pub.mongodb.rds.exam
ple.com:3717</ConnectString>
        <MaxIOPS>1000</MaxIOPS>
    </ConfigserverList>
    <MongosList>
        <ConnectSting>s-bpxxxxxxxx.mongodb.rds.example.com</ConnectSting>
        <NodeClass>dds.mongos.mid</NodeClass>
        <NodeDescription>mongos1</NodeDescription>
        <MaxConnections>1000</MaxConnections>
        <VPCId>vpc-bp1xxxxxxxxxxxxxxxxxx</VPCId>
        <VSwitchId>vsw-bp1xxxxxxxxxxxxxxxxxx</VSwitchId>
        <Port>3717</Port>
        <NodeId>s-bpxxxxxxxx</NodeId>
        <VpcCloudInstanceId>s-bp1xxxxxxxxxxxxx</VpcCloudInstanceId>
        <MaxIOPS>0</MaxIOPS>
    </MongosList>
```

`/` `g`

```xml
    <Tags>
        <Value>api</Value>
        <Key>test</Key>
    </Tags>
    <ReplicaSets>
        <ConnectionDomain>dds-bpxxxxxxxx.mongodb.rds.example.com</ConnectionDomain>
        <ReplicaSetRole>Primary</ReplicaSetRole>
        <VPCCloudInstanceId>vpc-xxxxxxxx</VPCCloudInstanceId>
        <VPCId>vpc-bpxxxxxxxx</VPCId>
        <ConnectionPort>ConnectionPort</ConnectionPort>
        <NetworkType>VPC</NetworkType>
        <VSwitchId>vsw-bpxxxxxxxx</VSwitchId>
    </ReplicaSets>
</DBInstances>
```

`JSON` format `{`

```json
    "RequestId":"C373EED9-5125-4DD9-89DB-FB1ECD2C2B4F",
    "DBInstances":[
```

`{`

```json
            "VPCCloudInstanceIds":"s-bp1xxxxxxxxxxxxx",
            "ResourceGroupId":"rg-axxxxxxxx",
            "DBInstanceType":"replicate",
            "ReplicaSetName":"mgset-10xxxxxxxx",
            "StorageEngine":"WiredTiger",
            "MaintainEndTime":"03:00Z",
            "DBInstanceId":"dds-bpxxxxxxxx",
            "NetworkType":"VPC",
            "LastDowngradeTime":"2019-03-08",
            "DBInstanceStorage":"10",
            "MaintainStartTime":"02:00Z",
            "Engine":"MongoDB",
            "DBInstanceDescription":"Test",
            "ReplacateId":"bls-mxxxxxxxx",
            "DBInstanceReleaseProtection":"true",
            "EngineVersion":"3.4",
            "MaxConnections":"500",
            "ReadonlyReplicas":"0",
            "ReplicationFactor":"3",
            "DBInstanceStatus":"Running",
            "ZoneId":"cn-hangzhou-b",
            "VPCId":"vpc-bpxxxxxxxx",
            "DBInstanceClass":"dds.mongo.mid",
            "VSwitchId":"vsw-bpxxxxxxxx",
            "LockMode":"Unlock",
            "MaxIOPS":"1000",
            "VpcAuthMode":"Open",
            "ProtocolType":"mongodb",
            "CurrentKernelVersion":"mongodb_20180914_1.1.5",
            "ChargeType":"PostPaid",
            "CreationTime":"2018-11-21T05:10:00Z",
            "RegionId":"cn-hangzhou",
```

`"E` `i` `Ti`

```
""20190408T1600Z"
```

```json
            "ExpireTime":"2019-04-08T16:00Z",
            "KindCode":"1"
```

`},` `{`

```json
            "ShardList":[
```

`{`

```json
                    "NodeClass":"dds.shard.mid",
                    "NodeDescription":"testshard",
                    "MaxConnections":"8000",
                    "Port":"3717",
                    "NodeStorage":"10",
                    "NodeId":"d-bpxxxxxxxx",
                    "ConnectString":"d-bpxxxxxxxxxxxxxxxxxx.mongodb.rds.example.com",
                    "MaxIOPS":"8000"
```

`],`

```json
            "ConfigserverList":[
```

`{`

```json
                    "NodeClass":"dds.cs.mid",
                    "NodeDescription":"testConfigserver",
                    "MaxConnections":"0",
                    "Port":"3717",
                    "NodeStorage":"20",
                    "NodeId":"dds-bpxxxxxxxxxxxxxx-cs",
                    "ConnectString":"mongodb://root:****@dds-bpxxxxxxxxxxxxxx-cs1730-pub.mo
ngodb.rds.example.com:3717",
                    "MaxIOPS":"1000"
```

`],`

```json
            "MongosList":[
```

`{`

```json
                    "ConnectSting":"s-bpxxxxxxxx.mongodb.rds.example.com",
                    "NodeClass":"dds.mongos.mid",
                    "NodeDescription":"mongos1",
                    "MaxConnections":"1000",
                    "VPCId":"vpc-bp1xxxxxxxxxxxxxxxxxx",
                    "VSwitchId":"vsw-bp1xxxxxxxxxxxxxxxxxx",
                    "Port":"3717",
                    "NodeId":"s-bpxxxxxxxx",
                    "VpcCloudInstanceId":"s-bp1xxxxxxxxxxxxx",
                    "MaxIOPS":"0"
```

`],`

```json
            "Tags":[
```

`{`

```json
                    "Value":"api",
                    "Key":"test"
```

`],`

```json
            "ReplicaSets":[
```

`{`

```json
                    "ConnectionDomain":"dds-bpxxxxxxxx.mongodb.rds.example.com",
                    "ReplicaSetRole":"Primary",
                    "VPCCloudInstanceId":"vpc-xxxxxxxx",
"VPCId":"vpc-bpxxxxxxxx"
```

```json
                    VPCId:vpcbpxxxxxxxx,
                    "ConnectionPort":"ConnectionPort",
                    "NetworkType":"VPC",
                    "VSwitchId":"vsw-bpxxxxxxxx"
```

`]` `]`

#### 3.5.6 DescribeRoleZoneInfo

You can call this operation to view the roles and zones of nodes in an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRoleZon eInfo | The operation that you want to perform. Set the value to DescribeRoleZoneInf o. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 728B9A96-E262- 4AE5-915E- 3A51CCE2FDA9 | The ID of the request. |
| ZoneInfos | Array of ZoneInfo |   | An array that consists of information of nodes in the zone. |
| ZoneInfo |   |   |   |
| InsName | String | dds-bpxxxxxxxx | The ID of the node. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| NodeType | String | normal | The type of the node. Valid values: normal conf igServer shard mongos Not e Valid value for replica set instances: normal. Valid values for sharded cluster instances: conf igServer, shard, and mongos. |
| RoleId | String | 83xxxxx | The ID of the role. |
| RoleType | String | Primary | The role of the node. Valid values: Primary Secondary Hidden |
| ZoneId | String | cn-hangzhou-e | The zone ID. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeRoleZoneInfo &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeRoleZoneInfoResponse>
   <ZoneInfos>
      <ZoneInfo>
         <RoleType>Primary</RoleType>
         <NodeType>normal</NodeType>
         <InsName>dds-bpxxxxxxxx</InsName>
         <ZoneId>cn-hangzhou-e</ZoneId>
         <RoleId>83xxxxx</RoleId>
      </ZoneInfo>
      <ZoneInfo>
         <RoleType>Secondary</RoleType>
         <NodeType>normal</NodeType>
         <InsName>dds-bpxxxxxxxx</InsName>
         <ZoneId>cn-hangzhou-f</ZoneId>
         <RoleId>83xxxxx</RoleId>
      </ZoneInfo>
      <ZoneInfo>
         <RoleType>Hidden</RoleType>
         <NodeType>normal</NodeType>
         <InsName>dds-bpxxxxxxxx</InsName>
         <ZoneId>cn-hangzhou-b</ZoneId>
         <RoleId>83xxxxx</RoleId>
      </ZoneInfo>
   </ZoneInfos>
   <RequestId>728B9A96-E262-4AE5-915E-3A51CCE2FDA9</RequestId>
</DescribeRoleZoneInfoResponse>
```

`JSON` format `{`

```json
 "ZoneInfos": {
  "ZoneInfo": [
```

`{`

```json
    "RoleType": "Primary",
    "NodeType": "normal",
    "InsName": "dds-bpxxxxxxxx",
    "ZoneId": "cn-hangzhou-e",
    "RoleId": "83xxxxx"
```

`},` `{`

```json
    "RoleType": "Secondary",
    "NodeType": "normal",
    "InsName": "dds-bpxxxxxxxx",
    "ZoneId": "cn-hangzhou-f",
    "RoleId": "83xxxxx"
```

`},` `{`

```json
    "RoleType": "Hidden",
    "NodeType": "normal",
    "InsName": "dds-bpxxxxxxxx",
    "ZoneId": "cn-hangzhou-b",
    "RoleId": "83xxxxx"
```

`]` `},`

```json
 "RequestId": "728B9A96-E262-4AE5-915E-3A51CCE2FDA9"
```

### 3.6 Instance management

#### 3.6.1 RestartDBInstance

You can call this operation to restart an ApsaraDB for MongoDB instance. This operation can also be used to restart a shard or mongos node in a replica set instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RestartDBInstanc e | The operation that you want to perform. Set the value to Rest art DBInst ance. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| NodeId | String | No | d-bpxxxxxxxx | The ID of the shard or mongos node in the sharded cluster instance. Not e The sharded cluster instance will be restarted if this parameter is not specified. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 149C517D-B586- 47BE-A107- 8673E0ED77C6 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=RestartDBInstance &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RestartDBInstanceResponse>
   <RequestId>149C517D-B586-47BE-A107-8673E0ED77C6</RequestId>
</RestartDBInstanceResponse>
```

`JSON` format `{`

```json
 "RequestId": "149C517D-B586-47BE-A107-8673E0ED77C6"
```

#### 3.6.2 ModifyDBInstanceMaintainTime

You can call this operation to modify the maintenance window of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstance MaintainTime | The operation that you want to perform. Set the value to Modif yDBInst anceMaint ainT ime. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| MaintainEndTime | String | Yes | 02:00Z | The end time of the maintenance window. Specify the time in the HH:mmZ format. The time must be in UTC. Not e The difference between the start time and end time must be one hour. For example, if Maint ainSt art T ime is 01:00Z, Maint ainEndT ime must be 02:00Z. |
| MaintainStartTim e | String | Yes | 01:00Z | The start time of the maintenance window. Specify the time in the HH:mmZ format. The time must be in UTC. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | A9310426-C763- 42A2-A3AD- 70A8DA204531 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyDBInstanceMaintainTime &MaintainStartTime=01:00Z &MaintainEndTime=02:00Z &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceMaintainTimeResponse>
   <RequestId>A9310426-C763-42A2-A3AD-70A8DA204531</RequestId>
</ModifyDBInstanceMaintainTimeResponse>
```

`JSON` format `{`

```json
 "RequestId": "A9310426-C763-42A2-A3AD-70A8DA204531"
```

#### 3.6.3 ModifyDBInstanceDescription

You can call this operation to change the name of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstance Description | The operation that you want to perform. Set the value to Modif yDBInst anceDescript ion. |
| DBInstanceDescri ption | String | Yes | testdata | The name of the instance. Not e The name cannot start with http:// or https://. The name must start with a letter. It can contain letters, underscores ( ), hyphens (- _ ), and digits. It must be 2 to 256 characters in length. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Not e If you want to modify the name of a shard or mongos node in a sharded cluster instance, you must also specify the NodeId parameter. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the shard or mongos node in the sharded cluster instance. Not e This parameter is valid only if you set the DBInst anceId parameter to the ID of a sharded cluster instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 06F8F642-4009- 4FFC-80C4- 9D67DBF7B74E | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyDBInstanceDescription &DBInstanceDescription=testdata &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceDescriptionResponse>
   <RequestId>06F8F642-4009-4FFC-80C4-9D67DBF7B74E</RequestId>
</ModifyDBInstanceDescriptionResponse>
```

`JSON` format `{`

```json
 "RequestId": "06F8F642-4009-4FFC-80C4-9D67DBF7B74E"
```

#### 3.6.4 SwitchDBInstanceHA

You can call this operation to switch between the primary and secondary nodes in an ApsaraDB for MongoDB instance. The instance must be in the running state when you call this operation. On replica set instances, the switch is performed between primary and secondary instances. On sharded cluster instances, the switch is performed between primary and secondary shard nodes. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SwitchDBInstance HA | The operation that you want to perform. Set the value to Swit chDBInst anceHA. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the shard node in the sharded cluster instance. Not e If you set the DBInst anceId parameter to the ID of a sharded cluster instance, you must specify this parameter. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RoleIds | String | No | 972xxxx,972xxxx | The IDs of the roles that you want to switch. You can call the DescribeRoleZoneInf o operation to view the IDs and information of roles of nodes. Not e Separate role IDs with commas (,). If this parameter is not specified, the primary and secondary nodes are switched. If you set the DBInst anceId parameter to the ID of a sharded cluster instance, the roles to be switched must belong to one shard node. |
| SwitchMode | Integer | No | 0 | The time when roles of the primary and secondary nodes are switched. Valid values: 0: The roles are switched immediately. 1: The roles are switched during the maintenance period. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 26BD4E5F-BDB4- 47BA-B232- 413AA78CFA8F | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=SwitchDBInstanceHA &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SwitchDBInstanceHAResponse>
   <RequestId>26BD4E5F-BDB4-47BA-B232-413AA78CFA8F</RequestId>
</SwitchDBInstanceHAResponse>
```

`JSON` format `{`

```json
 "RequestId": "26BD4E5F-BDB4-47BA-B232-413AA78CFA8F"
```

#### 3.6.5 UpgradeDBInstanceEngineVersion

You can call this operation to upgrade the database version of an ApsaraDB for MongoDB instance. The instance must be in the running state when you call this operation. The available database versions are subject to the storage engine used by the instance. You can call the DescribeAvailableEngineVersion operation to view the available database versions. The database version cannot be downgraded after it is upgraded. The instance is automatically restarted for two to three times during the upgrade process. Make sure that you upgrade the instance during off-peak hours. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpgradeDBInstan ceEngineVersion | The operation that you want to perform. Set the value to UpgradeDBInst anceEngineVersion. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| EngineVersion | String | Yes | 4.2 | The new database engine version of the instance. Valid values: 3.4, 4.0, and 4.2. Not e The new database engine version must be later than the current version. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C4907B00-A208- 4E0C-A636- AA85140E406C | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=UpgradeDBInstanceEngineVersion &EngineVersion=4.0 &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UpgradeDBInstanceEngineVersionResponse>
   <RequestId>C4907B00-A208-4E0C-A636-AA85140E406C</RequestId>
</UpgradeDBInstanceEngineVersionResponse>
```

`JSON` format `{`

```json
 "RequestId": "C4907B00-A208-4E0C-A636-AA85140E406C"
```

#### 3.6.6 UpgradeDBInstanceKernelVersion

You can call this operation to upgrade the minor database version of an ApsaraDB for MongoDB instance. The instance must be in the running state when you call this operation. The instance will be restarted once during the upgrade. Perform this operation during off-peak hours. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpgradeDBInstan ceKernelVersion | The operation that you want to perform. Set the value to UpgradeDBInst anceKernelVersion. |
| DBInstanceId | String | No | dds-bpxxxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 27B9A130-7C4B- 40D9-84E8- 2FC081097AAC | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=UpgradeDBInstanceKernelVersion &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UpgradeDBInstanceKernelVersionResponse>
   <RequestId>27B9A130-7C4B-40D9-84E8-2FC081097AAC</RequestId>
</UpgradeDBInstanceKernelVersionResponse>
```

`JSON` format `{`

```json
 "RequestId": "27B9A130-7C4B-40D9-84E8-2FC081097AAC"
```

#### 3.6.7 ModifyDBInstanceNetExpireTime

You can call this operation to extend the retention period of the classic network of an ApsaraDB for MongoDB instance. Before you call this operation, make sure that the following requirements are met: The instance must be running. The network of the instance is in hybrid access mode. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstance NetExpireTime | The operation that you want to perform. Set the value to Modif yDBInst anceNet ExpireT ime. |
| ClassicExpendExpi redDays | Integer | Yes | 30 | The retention period of the original classic network address. Valid values: 14, 30, 60, and 120. Unit: day. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| ConnectionString | String | No | dds- bpxxxxxxxx.mong odb.rds.aliyuncs. com | The connection address of the instance |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 459E7D5C-38DA- 4E14-9C82- 5B5AF693DBAB | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyDBInstanceNetExpireTime &ClassicExpendExpiredDays=30 &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceNetExpireTimeResponse>
   <RequestId>459E7D5C-38DA-4E14-9C82-5B5AF693DBAB</RequestId>
</ModifyDBInstanceNetExpireTimeResponse>
```

`JSON` format `{`

```json
 "RequestId": "459E7D5C-38DA-4E14-9C82-5B5AF693DBAB"
```

### 3.7 Account management

#### 3.7.1 DescribeAccounts

You can call this operation to view the information of the database account of an ApsaraDB for MongoDB instance. This operation can display only the information of the root account. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAccounts | The operation that you want to perform. Set the value to DescribeAccount s. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| AccountName | String | No | root | The name of the account. Set the value to root . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Accounts | Array of Account |   | An array that consists of the information of accounts. |
| Account |   |   |   |
| AccountDescrip tion | String | Administrator | The description of the account. |
| AccountName | String | root | The name of the account. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AccountStatus | String | Available | The status of the account. Unavailable Available |
| CharacterType | String | normal | The role of the account. Valid values: db: the shard node cs: the Configserver node mongos: the mongos node logic: the sharded cluster instance normal: the replica set instance |
| DBInstanceId | String | dds-bpxxxxxxxx | The name of the instance to which the account belongs. |
| RequestId | String | B562A65B-39AB- 4EE8-8635- 5A222054FB35 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeAccounts &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeAccountsResponse>
   <Accounts>
      <Account>
         <AccountStatus>Available</AccountStatus>
         <AccountDescription>Administrator</AccountDescription>
         <DBInstanceId>dds-bpxxxxxxxx</DBInstanceId>
         <AccountName>root</AccountName>
      </Account>
   </Accounts>
   <RequestId>A806B0FC-CFCC-48D8-8AEC-34C892806B40</RequestId>
</DescribeAccountsResponse>
```

`JSON` format `{`

```json
    "Accounts": {
        "Account": [
```

`{`

```json
                "AccountStatus": "Available",
                "AccountDescription": "Administrator",
                "DBInstanceId": "dds-bpxxxxxxxx",
                "AccountName": "root"
```

`]` `},`

```json
    "RequestId": "A806B0FC-CFCC-48D8-8AEC-34C892806B40"
```

#### 3.7.2 ResetAccountPassword

You can call this operation to reset the password of the root account of an ApsaraDB for MongoDB instance. This operation can reset only the password of the root account of an instance. Request parameters

| Parameter | Type | Required |   | Example | Description |   |
|---|---|---|---|---|---|---|
| Action | String | Yes |   | ResetAccountPas sword | The operation that you want to perform. Set the value to Reset Account Password. |   |
| AccountName | String | Yes |   | root | The account for which you want to reset the password. Set the value to root . |   |
| AccountPassword | String | Yes |   | Ali! 123456 | The new password. The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include ! # $ % ^ & * ( ) + _ - = #$%^&*() +-= _ The password must be 8 to 32 characters in length. |   |
|   |   |   |   |   |   | ! # $ % ^ & * ( ) + _ |
|   |   |   |   |   | - = #$%^&*() +-= _ |   |
| DBInstanceId | String | Yes |   | dds-bpxxxxxxxx | The ID of the instance. |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 06CBD06E-ABC9- 4121-AB93- 3C3820B3E7E6 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ResetAccountPassword &AccountName=root &AccountPassword=Ali! 123456 &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ResetAccountPasswordResponse>
   <RequestId>06CBD06E-ABC9-4121-AB93-3C3820B3E7E6</RequestId>
</ResetAccountPasswordResponse>
```

`JSON` format `{`

```json
 "RequestId": "06CBD06E-ABC9-4121-AB93-3C3820B3E7E6"
```

#### 3.7.3 ModifyAccountDescription

You can call this operation to modify the description of the root account of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyAccountDe scription | The operation that you want to perform. Set the value to Modif yAccount Descript ion. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AccountDescripti on | String | Yes | superadmin | The description of the account. It cannot start with http:// or https://. The description must start with a letter. It must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), and hyphens _ (-). |
| AccountName | String | Yes | root | The name of the account for which you want to modify the description. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 59DE9FC2-7B40- 45CF-9011- 7327A8A771A2 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyAccountDescription &AccountName=root &AccountDescription=superadmin &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RestoreDBInstanceResponse>
   <RequestId>59DE9FC2-7B40-45CF-9011-7327A8A771A2</RequestId>
</RestoreDBInstanceResponse>
```

`JSON` format `{`

```json
 "RequestId": "59DE9FC2-7B40-45CF-9011-7327A8A771A2"
```

### 3.8 IP whitelists and security groups

#### 3.8.1 DescribeSecurityGroupConfiguration

You can call this operation to view ECS security groups to which an ApsaraDB for MongoDB instance is added. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSecurityG roupConfiguratio n | The operation that you want to perform. Set the value to DescribeSecurit yGroupConf igurat io n. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | Array of RdsEcsSecurity GroupRel |   | The information list of the ECS security group. |
| RdsEcsSecurity GroupRel |   |   |   |
| NetType | String | vpc | The network type of the ECS security group. Valid values: vpc classic |
| RegionId | String | cn-hangzhou | The region ID of the ECS security group. |
| SecurityGroupId | String | sg-bpxxxxxxxx | The ID of the ECS security group. |
| RequestId | String | 3C4A2494-85C4- 45C5-93CF- 548DB3375193 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeSecurityGroupConfiguration &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Items>
    <RdsEcsSecurityGroupRel>
        <SecurityGroupId>sg-bpxxxxxxxx</SecurityGroupId>
        <RegionId>cn-hangzhou</RegionId>
        <NetType>classic</NetType>
    </RdsEcsSecurityGroupRel>
</Items> <RequestId>D18F5B88-ACA6-470E-9493-384412EDD902</RequestId>
```

`JSON` format `{`

```json
 "Items": {
  "RdsEcsSecurityGroupRel": [
```

`{`

```json
    "SecurityGroupId": "sg-bpxxxxxxxx",
    "RegionId": "cn-hangzhou",
    "NetType": "classic"
```

`]` `},`

```json
 "RequestId": "D18F5B88-ACA6-470E-9493-384412EDD902"
```

#### 3.8.2 ModifySecurityGroupConfiguration

You can call this operation to modify the ECS Security group that is bound to an ApsaraDB for MongoDB instance. For a sharded cluster instance, the bound ECS security group takes effect only for the mongos node. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySecurityGr oupConfiguration | The operation that you want to perform. Set the value toModif ySecurit yGroupConf igurat i on. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| SecurityGroupId | String | Yes | sg-bpxxxxxxxx | The ID of the ECS security group. Not e Only one ECS Security Group can be bound to an instance. You can view the security groups in the specified region by calling theDescribeSecurit yGrou p operation of ECS. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | E062C482-1A4B- 469E-938C- 96D28CFAE42E | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ModifySecurityGroupConfiguration &DBInstanceId=dds-bpxxxxxxxx &SecurityGroupId=sg-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>E062C482-1A4B-469E-938C-96D28CFAE42E</RequestId>
```

`JSON` format `{`

```json
    "RequestId": "E062C482-1A4B-469E-938C-96D28CFAE42E"
```

#### 3.8.3 DescribeSecurityIps

You can call this operation to view the IP whitelist of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSecurityI ps | The operation that you want to perform. Set the value to DescribeSecurit yIps. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| SecurityIpGroup s | Array of SecurityIpGroup |   | An array that consists of the information of IP whitelists. |
| SecurityIpGroup |   |   |   |
| SecurityIpGroup Attribute | String | hidden | The attribute of the IP whitelist. This parameter is empty by default. |
| SecurityIpGroup Name | String | default | The name of the whitelist. |
| SecurityIpList | String | 47.xxx.xxx.xx,100.xxx .xxx.0/24 | The IP addresses in the whitelist. |
| SecurityIps | String | 47.xxx.xxx.xx,100.xxx .xxx.0/24 | The IP addresses in the default whitelist. |
| RequestId | String | FC724D23-2962- 479E-ABB1- 606C935AE7FD | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeSecurityIps &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeSecurityIpsResponse>
   <SecurityIpGroups>
      <SecurityIpGroup>
         <SecurityIpList>114.xxx.xxx.xx</SecurityIpList>
         <SecurityIpGroupAttribute></SecurityIpGroupAttribute>
         <SecurityIpGroupName>allowserver</SecurityIpGroupName>
      </SecurityIpGroup>
      <SecurityIpGroup>
         <SecurityIpList>47.xxx.xxx.xx,100.xxx.xxx.0/24</SecurityIpList>
         <SecurityIpGroupAttribute></SecurityIpGroupAttribute>
         <SecurityIpGroupName>default</SecurityIpGroupName>
      </SecurityIpGroup>
   </SecurityIpGroups>
   <SecurityIps>47.xxx.xxx.xx,100.xxx.xxx.0/24</SecurityIps>
   <RequestId>FC724D23-2962-479E-ABB1-606C935AE7FD</RequestId>
</DescribeSecurityIpsResponse>
```

`JSON` format `{`

```json
 "SecurityIpGroups": {
  "SecurityIpGroup": [
```

`{`

```json
    "SecurityIpList": "114.xxx.xxx.xx",
    "SecurityIpGroupAttribute": "",
    "SecurityIpGroupName": "allowserver"
```

`},` `{`

```json
    "SecurityIpList": "47.xxx.xxx.xx,100.xxx.xxx.0/24",
    "SecurityIpGroupAttribute": "",
    "SecurityIpGroupName": "default"
```

`]` `},`

```json
 "SecurityIps": "47.xxx.xxx.xx,100.xxx.xxx.0/24",
 "RequestId": "FC724D23-2962-479E-ABB1-606C935AE7FD"
```

#### 3.8.4 ModifySecurityIps

You can call this operation to modify the IP whitelist of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySecurityIps | The operation that you want to perform. Set the value to Modif ySecurit yIps. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| SecurityIps | String | Yes | 10.23.12.24/24,1 0.22.22.22 | The IP addresses in an IP whitelist. Separate multiple IP addresses with commas (,). You can add a maximum of 1,000 different IP addresses to a whitelist. You can add IP addresses in one of the following two formats: IP addresses. Example: 10.23.12.24. Classless Inter-Domain Routing (CIDR) blocks, such as 10.23.12.24/24. /24 indicates the length of the IP address prefix in the CIDR block. An IP address prefix can contain 1 to 32 bits. |
| ModifyMode | String | No | Append | The method of modification. Valid values: Cover: overwrites the whitelist. Append: appends data to the whitelist. Delet e: deletes the whitelist. The default value is Cover. |
| SecurityIpGroupN ame | String | No | allowserver | The name of the IP whitelist to be modified. The default value is def ault . |
| SecurityIpGroupAt tribute | String | No | test | The attributes of an IP whitelist. It can contain a maximum of 120 characters in length and can contain uppercase letters, lowercase letters, and digits. This parameter is empty by default. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 61B05CCF-EBAB- 4BF3-BA67- D77256A721E2 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ModifySecurityIps &SecurityIps=10.23.12.24/24,10.22.22.22 &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifySecurityIpsResponse>
   <RequestId>61B05CCF-EBAB-4BF3-BA67-D77256A721E2</RequestId>
</ModifySecurityIpsResponse>
```

`JSON` format `{`

```json
 "RequestId": "61B05CCF-EBAB-4BF3-BA67-D77256A721E2"
```

### 3.9 Key management

#### 3.9.1 DescribeDBInstanceTDEInfo

You can call this operation to view whether TDE is enabled for an ApsaraDB for MongoDB instance. Before you call this operation, make sure that the following requirements are met: A replica set or sharded cluster instance is used. The storage engine of the instance is WiredTiger. The database engine version of the instance is 4.0 or 4.2. If the database engine version of your instance is earlier than 4.0, you can call the UpgradeDBInst anceEngineVersion operation to upgrade the database engine. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstan ceTDEInfo | The operation that you want to perform. Set the value to DescribeDBInst anceT DEInf o. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F4DD0E29-361B- 42F2-9301- B0048CCCE5D6 | The ID of the request. |
| TDEStatus | String | enabled | The TDE status. Valid values: enabled disabled |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeDBInstanceTDEInfo &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TDEStatus>enabled</TDEStatus> <RequestId>F4DD0E29-361B-42F2-9301-B0048CCCE5D6</RequestId>
```

`JSON` format `{`

```json
    "TDEStatus":"enabled",
    "RequestId":"F4DD0E29-361B-42F2-9301-B0048CCCE5D6"
```

#### 3.9.2 ModifyDBInstanceTDE

You can call this operation to modify the transparent data encryption (TDE) status of an ApsaraDB for MongoDB instance. Before data files are written to disks, transparent data encryption (TDE) encrypts the data files. When data files are loaded from disks to the memory, TDE decrypts the data files. After TDE is enabled, it cannot be disabled. Before you call this operation, make sure that the following requirements are met: A replica set or sharded cluster instance is used. The storage engine of the instance is WiredTiger. The database engine version of the instance is 4.0 or 4.2. If the database engine version is earlier than 4.0, you can call the UpgradeDBInst anceEngineVersion operation to upgrade the database engine. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstance TDE | The operation that you want to perform. Set the value to Modif yDBInst anceT DE. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| TDEStatus | String | Yes | enabled | The TDE status. Set the value to Enabled. Not e After TDE is enabled, it cannot be disabled. Proceed with caution. |
| EncryptorName | String | No | aes-256-cbc | The encryption method. Set the value to aes-256-cbc. Not e This parameter is valid only when you set the T EDSt at us parameter to enabled. |
| EncryptionKey | String | No | 749c1df7-xxxx- xxxx-xxxx- xxxxxxxxxxxx | The custom key. |

| Parameter | Type |   | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|---|
| RoleARN | String |   |   |   | The ARN of the role. It is in the format of acs:ram::$accountID:role/$roleN ame . Not e $accountID : indicates the ID of the Alibaba Cloud account that owns the RAM role. To view the account ID, log on to the Alibaba Cloud Management Console, move your pointer over your profile picture in the upper-right corner, and then click Security Settings. $roleName : indicates the name of the RAM role. To view the RAM role name, perform the following steps: Log on to the RAM console. In the left-side navigation pane, click RAM Roles. In the RAM Role Name column on the page that appears, you can view the name of the RAM role. |   |   |
|   |   |   |   |   |   | acs:ram::$accountID:role/$roleN |   |
|   |   |   |   |   | ame |   |   |
|   |   |   | No | acs:ram::123456 789012****:role/ adminrole |   |   |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 434D7127-6229- 4355-BA50- 7A3685A725DF | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyDBInstanceTDE &DBInstanceId=dds-bpxxxxxxxx &TDEStatus=enabled &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceTDEResponse>
   <RequestId>434D7127-6229-4355-BA50-7A3685A725DF</RequestId>
</ModifyDBInstanceTDEResponse>
```

`JSON` format `{`

```json
 "RequestId": "434D7127-6229-4355-BA50-7A3685A725DF"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | IncorrectDBInstanceS tate | Current DB instance state does not support this operation. | The error message returned because the operation is not supported while the instance is in its current state. Check whether the specified parameters are correct. |
| 403 | IncorrectDBInstanceL ockMode | Current DB instance lock mode does not support this operation. | The error message returned because the instance is locked. |

### 3.10 SSL encryption

#### 3.10.1 ModifyDBInstanceSSL

You can call this operation to modify the SSL settings of an ApsaraDB for MongoDB instance. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. A replica set instance is used. The database engine version of the instance is 3.4, 4.0, or 4.2. Whenever you enable or disable SSL encryption, or update the SSL certificate, the instance will restart. We recommend that you call this operation during off-peak hours. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstance SSL | The operation that you want to perform. Set the value to DescribeDBInst anceSSL. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SSLAction | String | Yes | Open | The operation that you perform for the SSL feature. Valid values: Open: enables SSL encryption. Close: disables SSL encryption. Updat e: updates the SSL certificate. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6D806B11-078F- 4154-BF9F- 844F56D08964 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyDBInstanceSSL &DBInstanceId=dds-bpxxxxxxxx &SSLAction=Open &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceSSLResponse>
   <RequestId>6D806B11-078F-4154-BF9F-844F56D08964</RequestId>
</ModifyDBInstanceSSLResponse>
```

`JSON` format `{`

```json
 "RequestId": "6D806B11-078F-4154-BF9F-844F56D08964"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | IncorrectDBInstanceS tate | Current DB instance state does not support this operation. | The error message returned because the operation is not supported while the instance is in its current state. Check whether the specified parameters are correct. |
| 403 | IncorrectDBInstanceL ockMode | Current DB instance lock mode does not support this operation. | The error message returned because the instance is locked. |

#### 3.10.2 DescribeDBInstanceSSL

You can call this operation to view the SSL settings of an ApsaraDB for MongoDB instance. Before you call this operation, make sure that the following requirements are met: The primary instance must be in the Running state. A replica set instance is used. The database engine version of the instance is 3.4, 4.0, or 4.2. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstan ceSSL | The operation that you want to perform. Set the value to DescribeDBInst anceSSL. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| SSLExpiredTime | String | 2020-03- 11T02:28:25Z | The time when the SSL certificate expires. The time is in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| RequestId | String | 36BB1BC2-789C- 4BBA-A519- C5B388E4B0D4 | The ID of the request. |
| SSLStatus | String | Open | The status of the SSL feature. Valid values: Open: The SSL feature is enabled. Closed: The SSL feature is disabled. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| CertCommonNa me | String | dds- bpxxxxxxxx.mongod b.rds.example.com | The name of the SSL certificate. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeDBInstanceSSL &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeDBInstanceSSLResponse>
   <SSLExpiredTime>2020-03-11T02:28:25Z</SSLExpiredTime>
   <RequestId>36BB1BC2-789C-4BBA-A519-C5B388E4B0D4</RequestId>
   <SSLStatus>Open</SSLStatus>
   <CertCommonName>dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com</CertCommonName>
</DescribeDBInstanceSSLResponse>
```

`JSON` format `{`

```json
    "SSLExpiredTime":"2020-03-11T02:28:25Z",
    "SSLStatus":"Open",
    "RequestId":"36BB1BC2-789C-4BBA-A519-C5B388E4B0D4",
    "CertCommonName":"dds-bpxxxxxxxx.mongodb.rds.example.com"
```

### 3.11 Audit logs

#### 3.11.1 DescribeAuditRecords

You can call this operation to view the audit logs of ApsaraDB for MongoDB instances. When you call this operation, ensure that the audit log feature of the instance is enabled. Otherwise, the operation returns an empty audit log. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAuditRec ords | The operation that you want to perform. Set the value to DescribeAudit Records. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Not e If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| EndTime | String | Yes | 2019-03- 13T13:11:14Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the yyyy- MM-ddTHH:mm:ssZ format. The time must be in UTC. |
| StartTime | String | Yes | 2019-03- 13T12:11:14Z | The beginning of the time range to query. Specify the time in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard node in the sharded cluster instance. Not e This parameter is valid only if you set the DBInst anceId parameter to the ID of a sharded cluster instance. |
| Database | String | No | testdatabase | The name of the database. If you do not specify this parameter, this operation returns audit logs of all databases. |
| User | String | No | root | The account of the database. If you do not specify this parameter, this operation returns audit logs of all accounts. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Form | String | No | Stream | The form of the audit log entry returend. Valid values: File: returns a log file. If this parameter is set to File, only common parameters are returned. In this case, you must call the DescribeAudit Files operation to view the download URL of the log file. St ream: returns data streams. Default value: St ream. |
| QueryKeywords | String | No | slow | The keywords used for a query. Separate multiple keywords with spaces. You can specify a maximum of 10 keywords. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be a positive integer. Default value: 1. |
| OrderType | String | No | asc | The order of time in which the log entries to return are sorted. Valid values: asc: The log entries are sorted by time in ascending order. desc: The log entries are sorted by time in descending order. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | Array of SQLRecord |   | An array that consists of the information of the audit log entries. |
| SQLRecord |   |   |   |
| AccountName | String | root | The account of the database. |

| eveloper Guide·AP | I Reference |   | ApsaraDB for MongoD |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBName | String | test123 | The name of the database. |
| ExecuteTime | String | 2019-03- 11T03:30:27Z | The time when the statement was executed. The time is in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| HostAddress | String | 11.xxx.xxx.xxx | The IP address of the client. |
| ReturnRowCoun ts | Long | 2 | The number of entries returned. |
| Syntax | String | { \"atype\" : \"createCollection\" , \"param\" : { \"ns\" : \"123.test1\" }, \"result\": \"OK\" } | The statement that was executed. |
| TableName | String | C1 | The name of the collection. |
| ThreadID | String | 140682188297984 | The ID of the thread. |
| TotalExecution Times | Long | 700 | The duration of the statement execution. Unit: microseconds. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCou nt | Integer | 30 | The maximum number of records on the current page. |
| RequestId | String | 3278BEB8-503B- 4E46-8F7E- D26E040C9769 | The ID of the request. |
| TotalRecordCo unt | Integer | 40 | The total number of entries. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeAuditRecords &StartTime=2019-03-13T12:11:14Z &EndTime=2019-03-13T13:11:14Z &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalRecordCount>40</TotalRecordCount> <PageRecordCount>30</PageRecordCount> <RequestId>3278BEB8-503B-4E46-8F7E-D26E040C9769</RequestId> <PageNumber>1</PageNumber> <Items>
    <TableName>C1</TableName>
    <ThreadID>140682188297984</ThreadID>
    <ExecuteTime>2019-03-11T03:30:27Z</ExecuteTime>
    <ReturnRowCounts>2</ReturnRowCounts>
    <DBName>test123</DBName>
    <TotalExecutionTimes>700</TotalExecutionTimes>
    <Syntax>{ \"atype\" : \"createCollection\", \"param\" : { \"ns\" : \"123.test1\" }, \"r
esult\": \"OK\" }</Syntax>
    <HostAddress>11.xxx.xxx.xxx</HostAddress>
    <AccountName>root</AccountName>
</Items>
```

`JSON` format `{`

```json
    "TotalRecordCount":"40",
    "PageRecordCount":"30",
    "RequestId":"3278BEB8-503B-4E46-8F7E-D26E040C9769",
    "PageNumber":"1",
    "Items":[
```

`{`

```json
            "TableName":"C1",
            "ThreadID":"140682188297984",
            "ExecuteTime":"2019-03-11T03:30:27Z",
            "ReturnRowCounts":"2",
            "DBName":"test123",
            "TotalExecutionTimes":"700",
            "Syntax":"{ \\\"atype\\\" : \\\"createCollection\\\", \\\"param\\\" : { \\\"ns\
\\" : \\\"123.test1\\\" }, \\\"result\\\": \\\"OK\\\" }",
            "HostAddress":"11.xxx.xxx.xxx",
            "AccountName":"root"
```

`]` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidEndTime.Form at | Specified end time is not valid. | The error message returned when the end time is invalid. Check the format of the specified time. |

#### 3.11.2 DescribeAuditFiles

You can call this operation to view the audit log files of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAuditFile s | The operation that you want to perform. Set the value to DescribeAudit Files. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard node in the specified cluster instance. Not e If you do not specify this parameter, the audit logs of all mongos and shard nodes will be returned. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be a positive integer. Default value: 1. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | Array of LogFile |   | An array that consists of the information of audit log files. |
| LogFile |   |   |   |
| FileID | Integer | 406505 | The ID of the file. |
| LogDownloadU RL | String | http://xxxxxxxx.oss -cn- hangzhou.aliyuncs.c om/custinsxxxxxx/c ustinsxxxxxx xxxxxx. _ csv | The download URL for audit log files. Not e If the download URL is unavailable, this parameter is empty. |
| LogEndTime | String | 2019-03- 12T09:23:15Z | The end of the time range for the audit log files displayed. The time is in the yyyy-MM- ddTHH:mmZ format. The time is displayed in UTC. |
| LogSize | Long | 98 | The size of the audit log file. Unit: bytes. |
| LogStartTime | String | 2019-03- 11T08:19:29Z | The beginning of the time range for the audit log files displayed. The time is in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. |
| LogStatus | String | Success | The status of the audit log file. Success: The audit log file is archived. Failed: The audit log file failed to be archived. Generat ing: The audit log file is being archived. Init ializing: Archiving is not started. |
| PageNumber | Integer | 1 | The page number of the page returned. |
| PageRecordCou nt | Integer | 1 | The number of entries on the current page. |
| RequestId | String | F8CA8312-530A- 413A-9129- F2BB32A8D404 | The ID of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalRecordCo unt | Integer | 1 | The total number of entries. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeAuditFiles &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeAuditFilesResponse>
   <Items>
      <LogFile>
         <LogStartTime>2019-03-11T08:19:29Z</LogStartTime>
         <LogEndTime>2019-03-12T09:23:15Z</LogEndTime>
         <LogStatus>Success</LogStatus>
         <FileID>406505</FileID>
         <LogDownloadURL>http://xxxxxxxx.oss-cn-hangzhou.aliyuncs.com/custinsxxxxxx/custins
xxxxxx_xxxxxx.csv</LogDownloadURL>
         <LogSize>98</LogSize>
      </LogFile>
   </Items>
   <PageNumber>1</PageNumber>
   <TotalRecordCount>1</TotalRecordCount>
   <RequestId>F8CA8312-530A-413A-9129-F2BB32A8D404</RequestId>
   <PageRecordCount>1</PageRecordCount>
</DescribeAuditFilesResponse>
```

`JSON` format `{`

```json
 "Items": {
  "LogFile": [
```

`{`

```json
    "LogStartTime": "2019-03-11T08:19:29Z",
    "LogEndTime": "2019-03-12T09:23:15Z",
    "LogStatus": "Success",
    "FileID": 406505,
    "LogDownloadURL": "http://xxxxxxxx.oss-cn-hangzhou.aliyuncs.com/custinsxxxxxx/custinsxx
xxxx_xxxxxx.csv",
    "LogSize": 98
```

`]` `},`

```json
 "PageNumber": 1,
 "TotalRecordCount": 1,
 "RequestId": "F8CA8312-530A-413A-9129-F2BB32A8D404",
 "PageRecordCount": 1
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidDBInstanceCla ss.NotFound | Specified DB instance class is not found. | The error message returned because the specified instance type does not exist. Verify the specified instance type. |
| 403 | IncorrectDBInstance Type | Current DB instance type does not support this operation. | The error message returned because the operation is not supported by the current instance type. |

#### 3.11.3 DescribeAuditPolicy

You can call this operation to view whether the log audit feature is enabled for an ApsaraDB for MongoDB instance. The instance must be in the running state when you call this operation. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAuditPoli cy | The operation that you want to perform. Set the value to DescribeAudit Policy. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| LogAuditStatus | String | Enable | The status of the log audit feature. Valid values: Enable Disabled Default value: Disabled. |
| RequestId | String | 111E7B16-0A87- 4CBA-B271- F34AD61E099F | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeAuditPolicy &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeAuditPolicyResponse>
   <LogAuditStatus>Enable</LogAuditStatus>
   <RequestId>111E7B16-0A87-4CBA-B271-F34AD61E099F</RequestId>
</DescribeAuditPolicyResponse>
```

`JSON` format `{`

```json
 "LogAuditStatus": "Enable",
 "RequestId": "111E7B16-0A87-4CBA-B271-F34AD61E099F"
```

#### 3.11.4 ModifyAuditLogFilter

You can call this operation to modify the type of audit logs to be collected from ApsaraDB for MongoDB instances. The instance must be in the running state when you call this operation. This operation is applicable only to replica set instances, but not to sharded cluster instances. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyAuditLogFi lter | The operation that you want to perform. Set the value to Modif yAudit LogFilt er. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| Filter | String | Yes | insert,query,upda te,delete | The type of the audit log entries to be collected. Valid values: admin: O&M and management operations slow: slow queries query: query operations insert : insert operations updat e: update operations delet e: delete operations command: protocol commands such as the aggregate method |
| RoleType | String | No | primary | The role of the node in the instance. Valid values: primary secondary |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | E209BE2B-F264- 4B9D-81F6- A5A5FB1FBF28 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyAuditLogFilter &Filter=insert,query,update,delete &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyAuditLogFilterResponse>
   <RequestId>E209BE2B-F264-4B9D-81F6-A5A5FB1FBF28</RequestId>
</ModifyAuditLogFilterResponse>
```

`JSON` format `{`

```json
 "RequestId": "E209BE2B-F264-4B9D-81F6-A5A5FB1FBF28"
```

#### 3.11.5 DescribeAuditLogFilter

You can call this operation to view the types of audit logs collected from ApsaraDB for MongoDB instances. The instance must be in the running state when you call this operation. This operation is applicable only to replica set instances, but not to sharded cluster instances. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAuditLog Filter | The operation that you want to perform. Set the value to DescribeAudit LogFilt er. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| RoleType | String | No | primary | The role of the node in the instance. Valid values: primary secondary |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Filter | String | admin,slow,insert,q uery,update,delete, command | The type of the audit log entries. Valid values: admin: O&M and management operations slow: slow queries query: query operations insert : insert operations updat e: update operations delet e: delete operations command: protocol commands such as the aggregate method |
| RequestId | String | D7C8BA0C-9350- 487D-9B70- D69AF27FB1EB | The ID of the request. |
| RoleType | String | primary | The role of the node. |

Examples Sample requests

```
http(s)://mongodb.aliyuncs.com/? Action=DescribeAuditLogFilter &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeAuditLogFilterResponse>
   <Filter>admin,slow,insert,query,update,delete,command</Filter>
   <RoleType></RoleType>
   <RequestId>D7C8BA0C-9350-487D-9B70-D69AF27FB1EB</RequestId>
</DescribeAuditLogFilterResponse>
```

`JSON` format `{`

```json
 "Filter": "admin,slow,insert,query,update,delete,command",
 "RoleType": "",
 "RequestId": "D7C8BA0C-9350-487D-9B70-D69AF27FB1EB"
```

#### 3.11.6 ModifyAuditPolicy

You can call this operation to enable or disable the audit log feature or set the retention period of audit logs for an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyAuditPolicy | The operation that you want to perform. Set the value to Modif yAudit Policy. |
| AuditStatus | String | Yes | enable | The status of the audit log feature. Valid values: enable disabled |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| StoragePeriod | Integer | No | 30 | The retention period of audit logs. Unit: day. Valid values: 1 to 30. Default value: 30. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DC04D812-F18D- 4568-9B88- F260D9590116 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyAuditPolicy &AuditStatus=enable &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyAuditPolicyResponse>
   <RequestId>DC04D812-F18D-4568-9B88-F260D9590116</RequestId>
</ModifyAuditPolicyResponse>
```

`JSON` format `{`

```json
 "RequestId": "DC04D812-F18D-4568-9B88-F260D9590116"
```

### 3.12 Log management

#### 3.12.1 DescribeSlowLogRecords

You can call this operation to view the slow operation log details of the ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSlowLog Records | The operation that you want to perform. Set the value to DescribeSlowLogRecords. |
| StartTime | String | Yes | 2019-02- 24T12:10Z | The beginning of the time range to query. Specify the time in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |
| EndTime | String | Yes | 2019-02- 26T12:10Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the yyyy- MM-ddTHH:mmZ format. The time must be in UTC. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Not e If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the shard. Not e This parameter is only valid when you set the DBInst anceId parameter to the ID of a sharded cluster instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBName | String | No | mongodbtest | The name of the database. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30 to 100. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be a positive integer. Default value: 1. |
| OrderType | String | No | asc | The order of time in which the log entries to return are sorted. Valid values: asc: The log entries are sorted by time in ascending order. desc: The log entries are sorted by time in descending order. |
| ResourceGroupId | String | No | rg-axxxxxxxx | The ID of the resource group. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Engine | String | MongoDB | The database engine. |
| Items | Array of LogRecords |   | An array that consists of the information of operational log entries. |
| LogRecords |   |   |   |
| AccountName | String | root | The name of the user who performed the operation. |
| DBName | String | mongodbtest | The name of the database. |
| DocsExamined | Long | 1000000 | The number of documents scanned during the operation. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ExecutionStartT ime | String | 2019-02- 25T01:41:28Z | The start time of the operation. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. |
| HostAddress | String | 47.xxx.xxx.xx | The host IP address that you use to connect to a database. |
| KeysExamined | Long | 0 | The data records that are scanned during indexing. |
| QueryTimes | String | 600 | The execution duration of the statement. Unit: milliseconds. |
| ReturnRowCoun ts | Long | 0 | The number of entries returned. |
| SQLText | String | {\"op\":\"query\",\" ns\":\"mongodbtes t.customer\",\"quer y\": {\"find\":\"custome r\",\"filter\": {\"name\":\"jack\"}}} | The SQL statement that is executed during the slow query operation. |
| TableName | String | C1 | The name of the collection. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCou nt | Integer | 1 | The number of slow query log entries returned on the page. |
| RequestId | String | 414A4E5-4C36- 4461-95FC- 23757A20B5F8 | The ID of the request. |
| TotalRecordCo unt | Integer | 1 | The total number of entries. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeSlowLogRecords &StartTime=2019-02-24T12:10Z &EndTime=2019-02-26T12:10Z &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalRecordCount>1</TotalRecordCount> <PageRecordCount>1</PageRecordCount> <RequestId>414A4E5-4C36-4461-95FC-23757A20B5F8</RequestId> <PageNumber>1</PageNumber> <Items>
    <LogRecords>
        <TableName>C1</TableName>
        <QueryTimes>600</QueryTimes>
        <ExecutionStartTime>2019-02-25T01:41:28Z</ExecutionStartTime>
        <ReturnRowCounts>0</ReturnRowCounts>
        <KeysExamined>0</KeysExamined>
        <DBName>mongodbtest</DBName>
        <DocsExamined>1000000</DocsExamined>
        <HostAddress>47.xxx.xxx.xx</HostAddress>
        <AccountName>root</AccountName>
        <SQLText>{\"op\":\"query\",\"ns\":\"mongodbtest.customer\",\"query\":{\"find\":\"cu
stomer\",\"filter\":{\"name\":\"jack\"}}}</SQLText>
    </LogRecords>
</Items> <Engine>MongoDB</Engine>
```

`JSON` format `{`

```json
 "TotalRecordCount": "1",
 "PageRecordCount": "1",
 "RequestId": "414A4E5-4C36-4461-95FC-23757A20B5F8",
 "PageNumber": "1",
 "Items": {
  "LogRecords": [{
   "TableName": "C1",
   "QueryTimes": "600",
   "ExecutionStartTime": "2019-02-25T01:41:28Z",
   "ReturnRowCounts": "0",
   "KeysExamined": "0",
   "DBName": "mongodbtest",
   "DocsExamined": "1000000",
   "HostAddress": "47.xxx.xxx.xx",
   "AccountName": "root",
   "SQLText": "{\\\"op\\\":\\\"query\\\",\\\"ns\\\":\\\"mongodbtest.customer\\\",\\\"query\
\\":{\\\"find\\\":\\\"customer\\\",\\\"filter\\\":{\\\"name\\\":\\\"jack\\\"}}}"
```

`}]` `},`

```json
 "Engine": "MongoDB"
```

#### 3.12.2 DescribeErrorLogRecords

You can call this operation to view the error logs of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeErrorLog Records | The operation that you want to perform. Set the value to DescribeErrorLogRecords. |
| StartTime | String | Yes | 2019-01- 01T12:10Z | The beginning of the time range to query. Specify the time in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |
| EndTime | String | Yes | 2019-01- 02T12:10Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the yyyy- MM-ddTHH:mmZ format. The time must be in UTC. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Not e If you specify this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard node in the sharded cluster instance. Not e This parameter is valid only if you set the DBInst anceId parameter to the ID of a sharded cluster instance. |
| RoleType | String | No | primary | The role of the node in the instance. Valid values: primary secondary Not e If you set NodeId to the ID of a mongos node, the value of this parameter must be primary. |
| DBName | String | No | mongodbtest | The name of the database. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30 to 100 |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be a positive integer. Default value: 1. |
| ResourceGroupId | String | No | rg-axxxxxxxx | The ID of the resource group. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Engine | String | MongoDB | The database engine. |
| Items | Array of LogRecords |   | An array that consists of the information of log entries. |
| LogRecords |   |   |   |
| Category | String | NETWORK | The category of the log entry. |
| ConnInfo | String | conn18xxxxxx | The log connection information. |
| Content | String | xxxxxxxx | The content of the log entry. |
| CreateTime | String | 2019-02- 26T12:09:34Z | The time when the log entry was generated. The time is in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| Id | Integer | 1111111111 | The ID of the log entry. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCou nt | Integer | 1 | The number of entries returned on each page. |
| RequestId | String | 68BCBEC2-1E66- 471F-A1A8- E3C60C0A80B0 | The ID of the request. |
| TotalRecordCo unt | Integer | 1 | The total number of entries. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeErrorLogRecords &StartTime=2019-01-01T12:10Z &EndTime=2019-01-02T12:10Z &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeErrorLogRecordsResponse>
   <Items>
      <LogRecords>
         <Category>NETWORK</Category>
         <CreateTime>2019-02-26T12:09:34Z</CreateTime>
         <ConnInfo>conn18xxxxxx</ConnInfo>
         <Content>xxxxxxxx</Content>
      </LogRecords>
   </Items>
   <PageNumber>1</PageNumber>
   <TotalRecordCount>2</TotalRecordCount>
   <RequestId>68BCBEC2-1E66-471F-A1A8-E3C60C0A80B0</RequestId>
</DescribeErrorLogRecordsResponse>
```

`JSON` format `{`

```json
    "TotalRecordCount":"1",
    "PageRecordCount":"1",
    "RequestId":"68BCBEC2-1E66-471F-A1A8-E3C60C0A80B0",
    "PageNumber":"1",
    "Items":{
        "LogRecords":[
```

`{`

```json
                "ConnInfo":"conn18xxxxxx",
                "Category":"NETWORK",
                "Id":"1111111111",
                "Content":"xxxxxxxx",
                "CreateTime":"2019-02-26T12:09:34Z"
```

`]`

```
    },"Engine":"MongoDB"
```

#### 3.12.3 DescribeRunningLogRecords

You can call this operation to view the operational logs of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRunningL ogRecords | The operation that you want to perform. Set the value to DescribeRunningLogRecords. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| StartTime | String | Yes | 2019-01- 01T12:10Z | The beginning of the time range to query. Specify the time in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |
| EndTime | String | Yes | 2019-01- 02T12:10Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the yyyy- MM-ddTHH:mmZ format. The time must be in UTC. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Not e If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard node in the sharded cluster instance. Not e This parameter is valid only if you set the DBInst anceId parameter to the ID of a sharded cluster instance. |
| DBName | String | No | mongodbtest | The name of the database. |
| RoleType | String | No | primary | The role of the node in the instance. Valid values: primary secondary Not e If you set NodeId to the ID of a mongos node, the value of RoleT ype must be primary. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30 to 100 |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be a positive integer. Default value: 1. |
| OrderType | String | No | asc | The order of time in which the log entries to return are sorted. Valid values: asc: The log entries are sorted by time in ascending order. desc: The log entries are sorted by time in descending order. |
| ResourceGroupId | String | No | rg-axxxxxxx | The ID of the resource group. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Engine | String | MongoDB | The database engine. |
| Items | Array of LogRecords |   | An array that consists of the information of log entries. |
| LogRecords |   |   |   |
| Category | String | NETWORK | The category of the log entry. |
| ConnInfo | String | conn18xxxxxx | The log connection information. |
| Content | String | end connection 11.xxx.xxx.xx:3xxxx (0 connections now open)\n | The content of the log entry. |
| CreateTime | String | 2019-02- 26T12:09:34Z | The time when the log entry was generated. The time is in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| Id | Integer | 1111111111 | The ID of the log entry. |

| A | psaraDB for Mong | oDB |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number of the page returned. |
| PageRecordCou nt | Integer | 30 | The number of entries returned on each page. |
| RequestId | String | 45D2B592-DEBA- 4347-BBF3- 47FF6C97DBBC | The ID of the request. |
| TotalRecordCo unt | Integer | 2 | The total number of entries. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeRunningLogRecords &StartTime=2019-01-01T12:10Z &EndTime=2019-01-02T12:10Z &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeRunningLogRecordsResponse>
   <Items>
      <LogRecords>
         <Category>-</Category>
         <CreateTime>2019-02-26T12:09:34Z</CreateTime>
         <ConnInfo>conn18xxxxxx</ConnInfo>
         <Content>
    end connection 11.xxx.xxx.xx:3xxxx (0 connections now open)
   </Content>
      </LogRecords>
      <LogRecords>
         <Category>NETWORK</Category>
         <CreateTime>2019-02-26T12:09:34Z</CreateTime>
         <ConnInfo>thread1</ConnInfo>
         <Content>connection accepted from 11.xxx.xxx.xx:3xxxx #1862051 (11 connections now
open)</Content>
      </LogRecords>
   </Items>
   <PageNumber>1</PageNumber>
   <TotalRecordCount>2</TotalRecordCount>
   <RequestId>45D2B592-DEBA-4347-BBF3-47FF6C97DBBC</RequestId>
</DescribeRunningLogRecordsResponse>
```

`JSON` format `{`

```json
    "Items": {
        "LogRecords": [
```

`{`

```json
                "Category": "-",
                "CreateTime": "2019-02-26T12:09:34Z",
                "ConnInfo": "conn18xxxxxx",
                "Content": "end connection 11.xxx.xxx.xx:3xxxx (0 connections now open)\n"
```

`},` `{`

```json
                "Category": "NETWORK",
                "CreateTime": "2019-02-26T12:09:34Z",
                "ConnInfo": "thread1",
                "Content": "connection accepted from 11.xxx.xxx.xx:3xxxx #1862051 (11 conne
ctions now open)"
```

`]` `},`

```json
    "PageNumber": 1,
    "TotalRecordCount": 2,
    "RequestId": "45D2B592-DEBA-4347-BBF3-47FF6C97DBBC"
```

### 3.13 Performance monitoring management

management

#### 3.13.1 DescribeDBInstancePerformance

You can call this operation to view the performance data of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstan cePerformance | The operation that you want to perform. Set the value to DescribeDBInst ancePerf ormance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Key | String | Yes | MongoDB Detaile _ dSpaceUsage | The performance metric. Valid values: CpuUsage: the CPU utilization percentage MemoryUsage: the memory usage percentage MongoDB IOPS: the IOPS usage _ IOPSUsage: the IOPS usage percentage. MongoDB Det ailedSpaceUsage: _ the disk usage. DiskUsage : the disk usage percentage MongoDB Opcount ers : the _ operation QPS MongoDB Connect ions : the _ number of connections MongoDB Cursors : the number of _ cursors MongoDB Net work : the network _ traffic MongoDB Global Lock Current _ _ _ _ Queue : the global lock waiting queues MongoDB Wt Cache : the _ _ WiredTiger storage Not e Separate multiple metrics with commas (,). |
| StartTime | String | Yes | 2019-03- 11T12:30Z | The beginning of the time range to query. Specify the time in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |
| EndTime | String | Yes | 2019-03- 11T12:30Z | The end of the time range to query. Specify the time in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. The end time must be later than the start time. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Not e If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard node in a sharded cluster instance. You can specify this parameter to view the performance of a single node. Not e This parameter is valid only if you set the DBInst anceId parameter to the ID of a sharded cluster instance. |
| ReplicaSetRole | String | No | Primary | The role of the node. Valid values: Primary Secondary Not e If you set the DBInst anceId parameter to the ID of a standalone instance, the value of this parameter can only be Primary. |
| RoleId | String | No | 60xxxxx | The role ID of a node in a instance. You can call the DescribeReplicaSet Role operation to view role IDs. Not e This parameter is valid only if you set the DBInstanceId parameter to the ID of a sharded cluster instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 267F98DC-367D- 4F20-B137- 8B5B664D1C5D | The ID of the request. |

| psaraDB for Mong | oDB |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| StartTime | String | 2019-03-11T12:20Z | The beginning of the time range to query. The time is in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. |
| EndTime | String | 2019-03-11T12:30Z | The beginning of the time range to query. The time is in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. |
| PerformanceKe ys | Array of PerformanceKe y |   | An array that consists of the information of performance metrics. |
| PerformanceKe y |   |   |   |
| Key | String | MongoDB DetailedS _ paceUsage | Performance metric. |
| PerformanceVa lues | Array of PerformanceVa lue |   | An array that consists of the values of performance metrics. |
| PerformanceVa lue |   |   |   |
| Date | String | 2019-03- 11T12:21:51Z | The date and time when the value is generated. |
| Value | String | 0.6 | The value of a performance metric. |
| Unit | String | MB | The unit of the performance metric. |
| ValueFormat | String | cpu usage _ | The format of the performance metric value. If the performance metric contains multiple fields, the fields are separated with ampersands (& ). For example, if you query disk usage, the returned ValueFormat is ins size& amp;dat a size& amp;log size. _ _ _ |
| DBInstanceId | String | dds-bpxxxxxxxx | The ID of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Engine | String | MongoDB | The database engine. It is fixed to MongoDB. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeDBInstancePerformance &Key=MongoDB_DetailedSpaceUsage &StartTime=2019-03-11T12:30Z &EndTime=2019-03-11T12:30Z &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<PerformanceKeys>
    <ValueFormat>cpu_usage</ValueFormat>
    <Unit>MB</Unit>
    <Key>MongoDB_DetailedSpaceUsage</Key>
</PerformanceKeys> <PerformanceKeys>
    <PerformanceValues>
        <Value>0.6</Value>
        <Date>2019-03-11T12:21:51Z</Date>
    </PerformanceValues>
</PerformanceKeys> <EndTime>2019-03-11T12:30Z</EndTime> <RequestId>267F98DC-367D-4F20-B137-8B5B664D1C5D</RequestId> <DBInstanceId>dds-bpxxxxxxxx</DBInstanceId> <StartTime>2019-03-11T12:20Z</StartTime> <Engine>MongoDB</Engine>
```

`JSON` format `{`

```json
    "PerformanceKeys":[
```

`{`

```json
            "ValueFormat":"cpu_usage",
            "Unit":"MB",
            "Key":"MongoDB_DetailedSpaceUsage"
```

`},` `{`

```json
            "PerformanceValues":[
```

`{`

```json
                    "Value":"0.6",
                    "Date":"2019-03-11T12:21:51Z"
```

`]` `],`

```json
    "EndTime":"2019-03-11T12:30Z",
    "RequestId":"267F98DC-367D-4F20-B137-8B5B664D1C5D",
    "DBInstanceId":"dds-bpxxxxxxxx",
    "StartTime":"2019-03-11T12:20Z",
    "Engine":"MongoDB"
```

#### 3.13.2 DescribeDBInstanceMonitor

You can call this operation to set the collection frequency of monitoring data for an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstan ceMonitor | The operation that you want to perform. Set the value to DescribeDBInst anceMonit or. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Granularity | String | 300 | The collection frequency of monitoring data. The value is fixed to 300 . Unit: seconds. |
| RequestId | String | EFD65226-08CC- 4C4D-B6A4- CB3C382F67B0 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeDBInstanceMonitor &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Granularity>300</Granularity> <RequestId>EFD65226-08CC-4C4D-B6A4-CB3C382F67B0</RequestId>
```

`JSON` format `{`

```json
 "Granularity": 300,
 "RequestId": "EFD65226-08CC-4C4D-B6A4-CB3C382F67B0"
```

### 3.14 Parameter management

#### 3.14.1 DescribeParameterModificationHistory

You can call this operation to view the parameter modification records of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeParamet erModificationHis tory | The operation that you want to perform. Set the value to DescribeParamet erModif icat ionHis t roy. |
| StartTime | String | Yes | 2019-01- 01T12:10Z | The beginning of the time range to query. Specify the time in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |
| EndTime | String | Yes | 2019-01- 02T12:10Z | The end of the time range to query. Specify the time in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. The end time must be later than the start time. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Not e If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| CharacterType | String | Yes | db | The role of the instance. Valid values: db: the shard node cs: the Configserver node mongos: the mongos node logic: the sharded cluster instance |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard in the specified sharded cluster instance. Not e This parameter is valid only if you set the DBInst anceId parameter to the ID of a sharded cluster instance. |
| RegionId | String | No | cn-hangzhou | The region ID of the instance. You can call the DescribeDBInst anceAt t ribut e operation to query the region ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| HistoricalParam eters | Array of HistoricalParam eter |   | An array that consists of the information of parameter modification records. |
| HistoricalParam eter |   |   |   |
| ModifyTime | String | 2019-03- 12T07:58:24Z | The time when the parameter was modified. The time is in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| NewParameter Value | String | 200 | The parameter value after modification. |

| Developer Guide·AP | I Reference |   | ApsaraDB for MongoD |
|---|---|---|---|
| Parameter | Type | Example | Description |
| OldParameterV alue | String | 100 | The parameter value before modification. |
| ParameterNam e | String | operationProfiling.sl owOpThresholdMs | The name of the modified parameter. |
| RequestId | String | B1BB6E0E-B4EF- 4145-81FA- A07719860248 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeParameterModificationHistory &StartTime=2019-01-01T12:10Z &EndTime=2019-01-02T12:10Z &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeParameterModificationHistoryResponse>
   <HistoricalParameters>
      <HistoricalParameter>
         <OldParameterValue>100</OldParameterValue>
         <ModifyTime>2019-03-12T07:58:24Z</ModifyTime>
         <NewParameterValue>200</NewParameterValue>
         <ParameterName>operationProfiling.slowOpThresholdMs</ParameterName>
      </HistoricalParameter>
   </HistoricalParameters>
   <RequestId>B1BB6E0E-B4EF-4145-81FA-A07719860248</RequestId>
</DescribeParameterModificationHistoryResponse>
```

`JSON` format `{`

```json
 "HistoricalParameters": {
  "HistoricalParameter": [
```

`{`

```json
    "OldParameterValue": "100",
    "ModifyTime": "2019-03-12T07:58:24Z",
    "NewParameterValue": "200",
    "ParameterName": "operationProfiling.slowOpThresholdMs"
```

`]` `},`

```json
 "RequestId": "B1BB6E0E-B4EF-4145-81FA-A07719860248"
```

#### 3.14.2 DescribeParameters

You can call this operation to view parameter configurations of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeParamet ers | The operation that you want to perform. Set the value toDescribeParamet ers. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Not e If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard in the specified sharded cluster instance. Not e This parameter is only valid when you set theDBInst anceIdparameter to the ID of a sharded cluster instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| CharacterType | String | No | mongos | The type of the database account. Valid values: mongos: The account that can be used to log on to a mongos node shard: The account that can be used to log on to a shard node |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ConfigParamet ers | Array of Parameter |   | An array that consists of the information of configured parameters. |
| Parameter |   |   |   |
| CheckingCode | String | [0-65536] | The valid values of the parameter. |
| ForceRestart | Boolean | true | Indicates whether a restart is required for parameter modifications to take effect. f alse: A restart is not required. Modifications take effect immediately after they are made. t rue: A restart is required for modifications to take effect. |
| ModifiableStat us | Boolean | true | Indicates whether the parameter is modifiable. f alse t rue |
| ParameterDescr iption | String | The threshold in milliseconds at which the database profiler considers a query slow, default is 100. | The description of the parameter. |
| ParameterNam e | String | operationProfiling.sl owOpThresholdMs | The name of the parameter. |
| ParameterValu e | String | 200 | The value of the parameter. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 3ADD0C7D-2D2A- 4F15-88FF- E7AC9B9FDCC8 | The ID of the request. |
| RunningParame ters | Array of Parameter |   | An array that consists of the information of instance parameters that have taken effect. |
| Parameter |   |   |   |
| CheckingCode | String | [33554432- 268435456] | The valid values of the parameter. |
| ForceRestart | String | false | Indicates whether a restart is required for parameter modifications to take effect. f alse: A restart is not required. Modifications take effect immediately after they are made. t rue: A restart is required for modifications to take effect. |
| ModifiableStat us | String | true | Indicates whether the parameter is modifiable. f alse t rue |
| ParameterDescr iption | String | The maximum memory bytes that sort stage may use, default is 33554432(i.e. 32MB) | The description of the parameter. |
| ParameterNam e | String | setParameter.intern alQueryExecMaxBloc kingSortBytes | The name of the parameter. |
| ParameterValu e | String | 33554432 | The value of the parameter. |
| EngineVersion | String | 4.0 | The engine version of the instance. |
| Engine | String | mongodb | The database engine of the instance. Default value: mongodb. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeParameters &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeParametersResponse>
      <ConfigParameters>
            <Parameter>
                  <ParameterDescription>The threshold in milliseconds at which the database
profiler considers a query slow, default is 100. </ParameterDescription>
                  <ParameterValue>200</ParameterValue>
                  <CheckingCode>[0-65536]</CheckingCode>
                  <ForceRestart>false</ForceRestart>
                  <ModifiableStatus>true</ModifiableStatus>
                  <ParameterName>operationProfiling.slowOpThresholdMs</ParameterName>
            </Parameter>
      </ConfigParameters>
      <RequestId>3ADD0C7D-2D2A-4F15-88FF-E7AC9B9FDCC8</RequestId>
      <RunningParameters>
            <Parameter>
                  <ParameterDescription></ParameterDescription>
                  <ParameterValue>zlib</ParameterValue>
                  <CheckingCode>snappy|zlib|disabled</CheckingCode>
                  <ForceRestart>true</ForceRestart>
                  <ModifiableStatus>true</ModifiableStatus>
                  <ParameterName>net.compression.compressors</ParameterName>
            </Parameter>
            <Parameter>
                  <ParameterDescription>The level of database profiling, which inserts info
rmation about operation performance into the system.profile collection. 'off' for no profil ing, 'slowOp' for only includes slow operations, 'all' for includes all operations, default is 'slowOp'. </ParameterDescription>
                  <ParameterValue>slowOp</ParameterValue>
                  <CheckingCode>off|slowOp|all</CheckingCode>
                  <ForceRestart>false</ForceRestart>
                  <ModifiableStatus>true</ModifiableStatus>
                  <ParameterName>operationProfiling.mode</ParameterName>
            </Parameter>
            <Parameter>
                  <ParameterDescription>The threshold in milliseconds at which the database
profiler considers a query slow, default is 100. </ParameterDescription>
                  <ParameterValue>220</ParameterValue>
                  <CheckingCode>[0-65536]</CheckingCode>
                  <ForceRestart>false</ForceRestart>
                  <ModifiableStatus>true</ModifiableStatus>
                  <ParameterName>operationProfiling.slowOpThresholdMs</ParameterName>
            </Parameter>
            <Parameter>
                  <ParameterDescription>The expiration threshold in milliseconds for idle c
ursors before MongoDB removes them; i.e. MongoDB removes cursors that have been idle for th e specified cursorTimeoutMillis. default is 600000(i.e. 10 minutes)</ParameterDescription>
```

`p` `(` `)``/` `p`

```xml
                  <ParameterValue>600000</ParameterValue>
                  <CheckingCode>[1-2147483647]</CheckingCode>
                  <ForceRestart>false</ForceRestart>
                  <ModifiableStatus>true</ModifiableStatus>
                  <ParameterName>setParameter.cursorTimeoutMillis</ParameterName>
            </Parameter>
            <Parameter>
                  <ParameterDescription>The maximum memory bytes that sort stage may use, d
efault is 33554432(i.e. 32MB)</ParameterDescription>
                  <ParameterValue>33554432</ParameterValue>
                  <CheckingCode>[33554432-268435456]</CheckingCode>
                  <ForceRestart>false</ForceRestart>
                  <ModifiableStatus>true</ModifiableStatus>
                  <ParameterName>setParameter.internalQueryExecMaxBlockingSortBytes</Parame
terName>
            </Parameter>
      </RunningParameters>
      <EngineVersion>4.0</EngineVersion>
      <Engine>mongodb</Engine>
</DescribeParametersResponse>
```

`JSON` format `{`

```json
    "ConfigParameters": {
        "Parameter": [
```

`{`

```json
                "ParameterDescription": "The threshold in milliseconds at which the databas
e profiler considers a query slow, default is 100.",
                "ParameterValue": "200",
                "CheckingCode": "[0-65536]",
                "ForceRestart": false,
                "ModifiableStatus": true,
                "ParameterName": "operationProfiling.slowOpThresholdMs"
```

`]` `},`

```json
    "RequestId": "3ADD0C7D-2D2A-4F15-88FF-E7AC9B9FDCC8",
    "RunningParameters": {
        "Parameter": [
```

`{`

```json
                "ParameterDescription": "",
                "ParameterValue": "zlib",
                "CheckingCode": "snappy|zlib|disabled",
                "ForceRestart": "true",
                "ModifiableStatus": "true",
                "ParameterName": "net.compression.compressors"
```

`},` `{`

```json
                "ParameterDescription": "The level of database profiling, which inserts inf
ormation about operation performance into the system.profile collection. 'off' for no profi ling, 'slowOp' for only includes slow operations, 'all' for includes all operations, defaul t is 'slowOp'.",
```

`"P` `t` `V``l` `"` `"``l` `O``"`

```json
                "ParameterValue": "slowOp",
                "CheckingCode": "off|slowOp|all",
                "ForceRestart": "false",
                "ModifiableStatus": "true",
                "ParameterName": "operationProfiling.mode"
```

`},` `{`

```json
                "ParameterDescription": "The threshold in milliseconds at which the databas
e profiler considers a query slow, default is 100.",
                "ParameterValue": "220",
                "CheckingCode": "[0-65536]",
                "ForceRestart": "false",
                "ModifiableStatus": "true",
                "ParameterName": "operationProfiling.slowOpThresholdMs"
```

`},` `{`

```json
                "ParameterDescription": "The expiration threshold in milliseconds for idle
cursors before MongoDB removes them; i.e. MongoDB removes cursors that have been idle for t he specified cursorTimeoutMillis. default is 600000(i.e. 10 minutes)",
                "ParameterValue": "600000",
                "CheckingCode": "[1-2147483647]",
                "ForceRestart": "false",
                "ModifiableStatus": "true",
                "ParameterName": "setParameter.cursorTimeoutMillis"
```

`},` `{`

```json
                "ParameterDescription": "The maximum memory bytes that sort stage may use,
default is 33554432(i.e. 32MB)",
                "ParameterValue": "33554432",
                "CheckingCode": "[33554432-268435456]",
                "ForceRestart": "false",
                "ModifiableStatus": "true",
                "ParameterName": "setParameter.internalQueryExecMaxBlockingSortBytes"
```

`]` `},`

```json
    "EngineVersion": "4.0",
    "Engine": "mongodb"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidDBInstanceCla ss.NotFound | Specified DB instance class is not found. | The error message returned when the specified instance type does not exists. Verify the specified instance type. |
| 403 | IncorrectDBInstance Type | Current DB instance type does not support this operation. | The error message returned when the current operation is not supported by the instance type of the specified instance. |

#### 3.14.3 ModifyParameters

You can call this operation to modify the parameters of an AsparaDB for MongoDB instance. The instance must be in the running state when you call this operation. If some of the modified parameters take effect only after the instance is restarted, the instance is automatically restarted after the operation is complete. You can call the DescribeParamet erT emplat es operation to query the parameters that take effect only after the instance is restarted. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyParameter s | The operation that you want to perform. Set the value toModif yParamet ers. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Not e If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| Parameters | String | Yes | {"operationProfili ng.slowOpThresh oldMs":"300"} | The parameters to be modified and their new values. Set this parameter to a JSON string. For example, set the parameter in the {"name":"value","name":"value2"} format. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard node in the specified sharded cluster instance. Not e This parameter is only valid when you set the DBInst anceId parameter to the ID of a sharded cluster instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| CharacterType | String | No | db | The role of the instance. Valid values: db: the shard node cs: the Configserver node mongos: the mongos node logic: the sharded cluster instance |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 36923CC2-DDAB- 4B48-A144- DA92C1E19537 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyParameters &DBInstanceId=dds-bpxxxxxxxx &Parameters={"operationProfiling.slowOpThresholdMs":"300"} &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyParametersResponse>
      <RequestId>36923CC2-DDAB-4B48-A144-DA92C1E19537</RequestId>
</ModifyParametersResponse>
```

`JSON` format `{`

```json
    "RequestId": "36923CC2-DDAB-4B48-A144-DA92C1E19537"
```

### 3.15 Backup and recovery

#### 3.15.1 DescribeBackupPolicy

You can call this operation to view the backup policy of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackupP olicy | The operation that you want to perform. Set the value to DescribeBackupPolicy. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupRetentio nPeriod | String | 7 | The backup retention period. Unit: days. |
| PreferredBacku pPeriod | String | Monday,Wednesday, Friday,Sunday | The period of backup. Valid values: Monday T uesday T hursday Friday Sat urday Sunday |
| PreferredBacku pTime | String | 20:00Z-21:00Z | The time when the data was backed up. The time is in the HH:mmZ-HH:mmZ format. The time is displayed in UTC. |
| PreferredNextB ackupTime | String | 2020-05-13T22:56Z | The next backup time. The time is in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. |
| RequestId | String | C2C283A1-1CC4- 4DD9-B985- 3811E0244A45 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeBackupPolicy DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<PreferredBackupPeriod>Monday,Wednesday,Friday,Sunday</PreferredBackupPeriod> <RequestId>C2C283A1-1CC4-4DD9-B985-3811E0244A45</RequestId> <PreferredBackupTime>20:00Z-21:00Z</PreferredBackupTime> <PreferredNextBackupTime>2020-05-13T22:56Z</PreferredNextBackupTime> <BackupRetentionPeriod>7</BackupRetentionPeriod>
```

`JSON` format `{`

```json
    "PreferredBackupPeriod":"Monday,Wednesday,Friday,Sunday",
    "RequestId":"C2C283A1-1CC4-4DD9-B985-3811E0244A45",
    "PreferredBackupTime":"20:00Z-21:00Z",
    "PreferredNextBackupTime":"2020-05-13T22:56Z",
    "BackupRetentionPeriod":"7"
```

#### 3.15.2 ModifyBackupPolicy

You can call this operation to modify the backup policy of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyBackupPoli cy | The operation that you want to perform. Set the value to Modif yBackupPolicy. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| PreferredBackupP eriod | String | Yes | Monday,Wednesd ay,Friday,Sunday | The period of backup. Valid values: Monday T uesday Wednesday T hursday Friday Sat urday Sunday Not e Separate multiple values with commas (,). |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PreferredBackupT ime | String | Yes | 03:00Z-04:00Z | The time to back up data. Specify the time in the HH:mmZ-HH:mmZ format. The time must be in UTC. Not e The maximum period is 1 hour. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 644A359C-B871- 4DD3-97B5- ED91EF5809C2 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyBackupPolicy &DBInstanceId=dds-bpxxxxxxxx &PreferredBackupPeriod=Monday,Wednesday,Friday,Sunday &PreferredBackupTime=03:00Z-04:00Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyBackupPolicyResponse>
   <RequestId>644A359C-B871-4DD3-97B5-ED91EF5809C2</RequestId>
</ModifyBackupPolicyResponse>
```

`JSON` format `{`

```json
 "RequestId": "644A359C-B871-4DD3-97B5-ED91EF5809C2"
```

#### 3.15.3 CreateBackup

You can call this operation to manually back up an ApsaraDB for MongoDB instance. The instance must be in the running state when you call this operation. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateBackup | The operation that you want to perform. Set the value to Creat eBackup. |
| DBInstanceId | String | Yes | d-bpxxxxxxxx | The ID of the instance. |
| BackupMethod | String | No | Logical | The backup method of the instance. Default value: Physical. Valid values: Logical Physical |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupId | String | 5664xxxx | The ID of the backup set. |
| RequestId | String | 7016B12F-7F64- 40A4-BAFF- 013F02AC82FC | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=CreateBackup DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateBackupResponse>
   <RequestId>7016B12F-7F64-40A4-BAFF-013F02AC82FC</RequestId>
   <BackupId>5664xxxx</BackupId>
</CreateBackupResponse>
```

`JSON` format `{`

```json
    "RequestId": "7016B12F-7F64-40A4-BAFF-013F02AC82FC",
    "BackupId": "5664xxxx"
```

#### 3.15.4 DescribeBackups

You can call this operation to view the backups of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackups | The operation that you want to perform. Set the value to DescribeBackups. |
| StartTime | String | Yes | 2019-03- 12T12:00Z | The beginning of the time range to query. Specify the time in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |
| EndTime | String | Yes | 2019-03- 13T12:00Z | The end of the time range to query. Specify the time in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. The end time must be later than the start time. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Not e If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the shard node in the sharded cluster instance. Not e This parameter is valid only if you set the DBInst anceId parameter to the ID of a sharded cluster instance. |
| BackupId | String | No | 12345678 | The ID of the backup set. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be a positive integer. Default value: 1. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 30 | The number of entries returned per page. |
| RequestId | String | 8925E66F-1971- 4C8C-90A7- F93BF1867E25 | The ID of the request. |
| TotalCount | Integer | 1 | The total number of backup sets. |
| Backups | Array of Backup |   | An array that consists of the information of backup sets. |
| Backup |   |   |   |
| BackupDBName s | String | mongodbtest,new,t est | The name of the database that has been backed up. |
| BackupDownlo adURL | String | http://xxxxx.oss- cn- hangzhou.aliyuncs.c om/xxxxx/hinsxxxxx data xxxxx.tar.gz _ _ | The Internet download URL of the backup file. If the download URL is unavailable, this parameter is an empty string. |
| BackupEndTime | String | 2019-03- 13T04:34:57Z | The end of the backup time range. The time is in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| BackupId | Integer | 11111111 | The ID of the backup set. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupIntranet DownloadURL | String | http://xxxxx.oss- cn-hangzhou- internal.example.co m/xxxxx/xxxxx.tar.g z | The internal download URL of the backup file. Not e You can download the backup file by using this URL on the Elastic Compute Service (ECS) instance that is connected to the ApsaraDB for MongoDB instance. The ECS instance and ApsaraDB for MongoDB instance must be in the classic network of the same region or in the same virtual private cloud (VPC). |
| BackupMethod | String | Physical | The backup method. Valid values: Snapshot Physical Logical |
| BackupMode | String | Automated | The backup mode. Valid values: Aut omat ed Manual |
| BackupSize | Long | 335520510 | The size of the backup file. Unit: bytes. |
| BackupStartTim e | String | 2019-03- 13T04:32:42Z | The beginning of the backup time range. The time is in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| BackupStatus | String | Success | The status of the backup. Valid values: Success: The backup task is successful. Failed: The backup task failed. |
| BackupType | String | FullBackup | The backup type. Valid values: FullBackup: full backup. Increment alBackup: incremental backup. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeBackups &StartTime=2019-03-12T12:00Z &EndTime=2019-03-13T12:00Z &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>1</TotalCount> <PageSize>30</PageSize> <RequestId>8925E66F-1971-4C8C-90A7-F93BF1867E25</RequestId> <PageNumber>1</PageNumber> <Backups>
    <BackupMethod>Physical</BackupMethod>
    <BackupDownloadURL>http://xxxxx.oss-cn-hangzhou.aliyuncs.com/xxxxx/hinsxxxxx_data_xxxxx
.tar.gz</BackupDownloadURL>
    <BackupIntranetDownloadURL>http://xxxxx.oss-cn-hangzhou-internal.example.com/xxxxx/xxxx
x.tar.gz</BackupIntranetDownloadURL>
    <BackupSize>335520510</BackupSize>
    <BackupMode>Automated</BackupMode>
    <BackupEndTime>2019-03-13T04:34:57Z</BackupEndTime>
    <BackupStartTime>2019-03-13T04:32:42Z</BackupStartTime>
    <BackupType>FullBackup</BackupType>
    <BackupId>11111111</BackupId>
    <BackupDBNames>mongodbtest,new,test</BackupDBNames>
    <BackupStatus>Success</BackupStatus>
</Backups>
```

`JSON` format `{`

```json
    "TotalCount":"1",
    "PageSize":"30",
    "RequestId":"8925E66F-1971-4C8C-90A7-F93BF1867E25",
    "PageNumber":"1",
    "Backups":[
```

`{`

```json
            "BackupMethod":"Physical",
            "BackupDownloadURL":"http://xxxxx.oss-cn-hangzhou.aliyuncs.com/xxxxx/hinsxxxxx_
data_xxxxx.tar.gz",
            "BackupIntranetDownloadURL":"http://xxxxx.oss-cn-hangzhou-internal.example.com/
xxxxx/xxxxx.tar.gz",
            "BackupSize":"335520510",
            "BackupMode":"Automated",
            "BackupEndTime":"2019-03-13T04:34:57Z",
            "BackupStartTime":"2019-03-13T04:32:42Z",
            "BackupType":"FullBackup",
            "BackupId":"11111111",
            "BackupDBNames":"mongodbtest,new,test",
            "BackupStatus":"Success"
```

`]`

#### 3.15.5 RestoreDBInstance

You can call this operation to restore data to the current ApsaraDB for MongoDB instance. This operation is applicable only to replica set instances, but not to standalone instances or sharded cluster instances. You also can use the following methods to clone an instance: Create an instance from a backup to clone a standalone instance. Call the CreateShardingDBInstance operation to clone a sharded cluster instance. This operation overwrites the data of the current instance, and the data cannot be recovered. Proceed with caution. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RestoreDBInstanc e | The operation that you want to perform. Set the value to Rest oreDBInst ance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| BackupId | Integer | Yes | 11111111 | The ID of the backup set. Not e You can call the DescribeBackups operation to view the backup ID. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 973DCB8F-56B3- 4102-8777- 3A90495927F7 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=RestoreDBInstance &BackupId=11111111 &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RestoreDBInstanceResponse>
   <RequestId>973DCB8F-56B3-4102-8777-3A90495927F7</RequestId>
</RestoreDBInstanceResponse>
```

`JSON` format `{`

```json
 "RequestId": "973DCB8F-56B3-4102-8777-3A90495927F7"
```

#### 3.15.6 DescribeBackupDBs

You can call this operation to view the databases at a specified time or the databases in a specified backup set before you restore a database for an ApsaraDB for MongoDB instance. You can call the Creat eDBInst ance operation to restore a database for an ApsaraDB for MongoDB instance. Before you call this operation, make sure that the following requirements are met: A replica set instance is used. The database engine version of the instance must be 3.0, 3.4, 4.0, or 4.2. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackupD Bs | The operation that you want to perform. Set the value to DescribeBackupDBs. |
| SourceDBInstance | String | Yes | dds-bpxxxxxxxx | The ID of the source instance. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be a positive integer. Default value: 1. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| RestoreTime | String | No | 2019-08- 22T12:00:00Z | The point in time at which the instance will be restored. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Not e It can be any time within the past seven days. The time must be earlier than the current time, but later than the time when the database was created. You must specify either this parameter or the BackupId parameter. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| BackupId | String | No | 5664xxxx | The ID of the backup set. Not e You can call the DescribeBackups operation to view the backup ID. You must specify this parameter or the Rest oreT ime parameter. |
| ResourceGroupId | String | No | rg-axxxxxxxx | The ID of the resource group. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Databases | Array of Database |   | An array that consists of inforamtion of databases. |
| Database |   |   |   |
| DBName | String | mongodbtest | The name of the database. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| TotalCount | Integer | 5 | The number of databases. |
| PageSize | Integer | 30 | The number of entries returned on each page. |
| RequestId | String | 1AF0AD89-ED4F- 44AD-B65F- BFC1D5CD9455 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeBackupDBs &SourceDBInstance=dds-bpxxxxxxxx &RestoreTime=2019-08-22T12:00:00Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>5</TotalCount> <Databases>
    <DBName>mongodbtest</DBName>
</Databases> <PageSize>30</PageSize> <RequestId>1AF0AD89-ED4F-44AD-B65F-BFC1D5CD9455</RequestId> <PageNumber>1</PageNumber>
```

`JSON` format `{`

```json
    "TotalCount":"5",
    "Databases":[
```

`{`

```json
            "DBName":"mongodbtest"
```

`],`

```json
    "PageSize":"30",
    "RequestId":"1AF0AD89-ED4F-44AD-B65F-BFC1D5CD9455",
    "PageNumber":"1"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | IncorrectDBInstance Type | Current DB instance type does not support this operation. | The error message returned when the current operation is not supported by the instance type of the specified instance. |

### 3.16 Instance states

This topic descries the instance states of ApsaraDB for MongoDB instances.

| State | Description |
|---|---|
| Creating | The instance is being created. |
| DBInstanceClassChanging | The instance specifications are being changed. |

| eveloper Guide·API Reference | ApsaraDB for MongoD |
|---|---|

| State | Description |
|---|---|
| DBInstanceNetTypeChanging | The network type of the instance is being changed. |
| Deleting | The instance is being deleted. |
| EngineVersionUpgrading | The database engine version of the instance is being upgraded. |
| GuardSwitching | The instance is undergoing a disaster-triggered failover. |
| HASwitching | The instance is undergoing a primary/secondary switching. |
| Importing | Data is being imported into the instance. |
| ImportingFromOthers | A database is being imported into the instance. |
| LinkSwitching | The instance is undergoing a link switching. |
| MinorVersionUpgrading | The minor version of the instance is being upgraded. |
| NET CREATING _ | A network connection to the instance is being created. |
| NET DELETING _ | A network connection to the instance is being deleted. |
| NodeCreating | A node is being created in the instance. |
| NodeDeleting | A node is being deleted in the instance. |
| Rebooting | The instance is being restarted. |
| Restoring | The cluster is being restored from the backup. |
| Running | The cluster is running. |
| SSLModifying | The SSL status of the instance is changing. |
| TempDBInstanceCreating | A node is being deleted in the instance. |
| Transing | The instance is being migrated. |
| TransingToOthers | A database in the instance is being migrated. |
