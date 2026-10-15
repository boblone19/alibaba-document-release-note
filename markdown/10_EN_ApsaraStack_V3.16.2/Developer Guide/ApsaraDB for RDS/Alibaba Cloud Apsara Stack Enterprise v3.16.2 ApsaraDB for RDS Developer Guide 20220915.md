---
title: "Alibaba Cloud Apsara Stack Enterprise v3.16.2 ApsaraDB for RDS Developer Guide 20220915"
product_version: "V3.16.2"
doc_version: "20220915"
pdf_pages: 402
source_pdf: "78c71c9c0d614e30_Alibaba Cloud Apsara Stack Enterprise v3.16.2 ApsaraDB for RDS Developer Guide 20220915.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/20230221/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20v3.16.2%20ApsaraDB%20for%20RDS%20Developer%20Guide%2020220915.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack Enterprise v3.16.2 ApsaraDB for RDS Developer Guide 20220915

## Table of Contents

- 1 Use ASAPI to call Apsara Stack SDKs
  - 1.1 Preparations
    - 1.1.1 Log on to the API Tool console
    - 1.1.2 Obtain API information
    - 1.1.3 Obtain an AccessKey pair
    - 1.1.4 Obtain common header parameters
    - 1.1.5 Obtain an STS AccessKey pair
  - 1.2 Use POP to make API calls
    - 1.2.1 Preparations
    - 1.2.2 SDK for Java
    - 1.2.3 SDK for Go
    - 1.2.4 SDK for Python
  - 1.3 Use ASAPI to make API calls
    - 1.3.1 ASAPI overview
    - 1.3.2 Generate an endpoint for ASAPI
    - 1.3.3 Obtain Apsara Stack SDKs
    - 1.3.4 Common parameters
    - 1.3.5 SDK description
      - 1.3.5.1 SDK for Java
      - 1.3.5.2 SDK for Python
      - 1.3.5.3 SDK for Node.js
    - 1.3.6 HTTP requests
      - 1.3.6.1 Overview
      - 1.3.6.2 Request structure
      - 1.3.6.3 Request signatures
      - 1.3.6.4 Responses
- 2 API reference
  - 2.1 Instance management
    - 2.1.1 CreateDBInstance
    - 2.1.2 DeleteDBInstance
    - 2.1.3 RestartDBInstance
    - 2.1.4 DescribeDBInstanceAttribute
    - 2.1.5 DescribeDBInstances
    - 2.1.6 ModifyDBInstanceSpec
    - 2.1.7 DescribeRegions
    - 2.1.8 MigrateToOtherZone
    - 2.1.9 ModifyDBInstanceDescription
    - 2.1.10 ModifyDBInstanceMaintainTime
    - 2.1.11 DescribeCharacterSetName
    - 2.1.12 DescribeDBInstanceIpHostname
    - 2.1.13 ModifyResourceGroup
  - 2.2 Read-only instances
    - 2.2.1 CreateReadOnlyDBInstance
    - 2.2.2 DescribeReadDBInstanceDelay
  - 2.3 Version upgrade
    - 2.3.1 ModifyDBInstanceAutoUpgradeMinorVersion
    - 2.3.2 UpgradeDBInstanceKernelVersion
  - 2.4 Network and endpoint management
    - 2.4.1 AllocateInstancePublicConnection
    - 2.4.2 ReleaseInstancePublicConnection
    - 2.4.3 SwitchDBInstanceNetType
    - 2.4.4 DescribeDBInstanceNetInfo
    - 2.4.5 ModifyDBInstanceConnectionString
    - 2.4.6 ReleaseInstanceConnection
    - 2.4.7 ModifyDBInstanceNetworkType
    - 2.4.8 SwitchDBInstanceVpc
    - 2.4.9 ModifyDBInstanceNetworkExpireTime
  - 2.5 Database management
    - 2.5.1 CreateDatabase
    - 2.5.2 DeleteDatabase
    - 2.5.3 DescribeDatabases
    - 2.5.4 ModifyDBDescription
    - 2.5.5 CopyDatabaseBetweenInstances
  - 2.6 Account management
    - 2.6.1 CreateAccount
    - 2.6.2 DeleteAccount
    - 2.6.3 CheckAccountNameAvailable
    - 2.6.4 CheckDBNameAvailable
    - 2.6.5 DescribeAccounts
    - 2.6.6 GrantAccountPrivilege
    - 2.6.7 RevokeAccountPrivilege
    - 2.6.8 ModifyAccountDescription
    - 2.6.9 ResetAccountPassword
    - 2.6.10 ResetAccount
    - 2.6.11 GrantOperatorPermission
    - 2.6.12 LockAccount
    - 2.6.13 RevokeOperatorPermission
    - 2.6.14 UnlockAccount
  - 2.7 Backup and restoration
    - 2.7.1 CreateBackup
    - 2.7.2 CloneDBInstance
    - 2.7.3 DescribeBackups
    - 2.7.4 DescribeBackupPolicy
    - 2.7.5 ModifyBackupPolicy
    - 2.7.6 DeleteBackup
    - 2.7.7 DeleteBackupFile
    - 2.7.8 DescribeBackupTasks
    - 2.7.9 DescribeLogBackupFiles
    - 2.7.10 DescribeMetaList
    - 2.7.11 RestoreTable
    - 2.7.12 DescribeDetachedBackups
  - 2.8 Database proxy
    - 2.8.1 CalculateDBInstanceWeight
    - 2.8.2 DescribeDBInstanceProxyConfiguration
    - 2.8.3 DescribeDBProxy
    - 2.8.4 DescribeDBProxyEndpoint
    - 2.8.5 DescribeDBProxyPerformance
    - 2.8.6 ModifyDBProxy
    - 2.8.7 ModifyDBProxyEndpoint
    - 2.8.8 ModifyDBProxyInstance
    - 2.8.9 ModifyReadWriteSplittingConnection
    - 2.8.10 ReleaseReadWriteSplittingConnection
  - 2.9 Primary/secondary high availability and data replication
    - 2.9.1 DescribeDBInstanceHAConfig
    - 2.9.2 ModifyDBInstanceHAConfig
    - 2.9.3 DescribeDBInstanceSwitchLog
    - 2.9.4 DescribeHASwitchConfig
    - 2.9.5 Switch workloads over between primary and secondary ApsaraDB RDS instances
    - 2.9.6 Enable or disable automatic primary/secondary switchovers
  - 2.10 Security and encryption
    - 2.10.1 DescribeDBInstanceIPArrayList
    - 2.10.2 ModifySecurityIps
    - 2.10.3 DescribeDBInstanceEncryptionKey
    - 2.10.4 ModifyDTCSecurityIpHostsForSQLServer
    - 2.10.5 DescribeDTCSecurityIpHostsForSQLServer
    - 2.10.6 DescribeDBInstanceSSL
    - 2.10.7 ModifyDBInstanceSSL
    - 2.10.8 ModifyDBInstanceTDE
    - 2.10.9 DescribeDBInstanceTDE
  - 2.11 Monitoring management
    - 2.11.1 DescribeResourceUsage
    - 2.11.2 DescribeDBInstancePerformance
    - 2.11.3 DescribeDBInstanceMonitor
    - 2.11.4 ModifyDBInstanceMonitor
  - 2.12 Parameter management
    - 2.12.1 DescribeParameters
    - 2.12.2 ModifyParameter
    - 2.12.3 DescribeModifyParameterLog
  - 2.13 Log management
    - 2.13.1 DescribeSlowLogs
    - 2.13.2 DescribeSlowLogRecords
    - 2.13.3 DescribeErrorLogs
    - 2.13.4 DescribeBinlogFiles
    - 2.13.5 DescribeSQLCollectorPolicy
    - 2.13.6 ModifySQLCollectorPolicy
    - 2.13.7 DescribeSQLLogRecords
    - 2.13.8 DescribeSQLLogFiles
    - 2.13.9 DescribeSQLLogReportList
    - 2.13.10 PurgeDBInstanceLog
  - 2.14 Event history management
    - 2.14.1 DescribeActionEventPolicy
    - 2.14.2 DescribeEvents
    - 2.14.3 ModifyActionEventPolicy
  - 2.15 Performance optimization and diagnostics (CloudDBA)
    - 2.15.1 CreateDiagnosticReport
    - 2.15.2 DescribeDiagnosticReportList
  - 2.16 Data migration
    - 2.16.1 CreateUploadPathForSQLServer
    - 2.16.2 DescribeFilesForSQLServer
    - 2.16.3 ImportDatabaseBetweenInstances
    - 2.16.4 CancelImport
    - 2.16.5 CreateMigrateTask
    - 2.16.6 DescibeImportsFromDatabase
    - 2.16.7 DescribeMigrateTaskById
    - 2.16.8 DescribeMigrateTasks
    - 2.16.9 DescribeOssDownloads
  - 2.17 Tag management
    - 2.17.1 TagResources
    - 2.17.2 AddTagsToResource
    - 2.17.3 ListTagResources
    - 2.17.4 UntagResources
  - 2.18 RAM authorization
  - 2.19 Appendix
    - 2.19.1 Error codes on the client
      - 2.19.1.1 Common errors
      - 2.19.1.2 Specific errors
    - 2.19.2 Error codes on the server
    - 2.19.3 Instance states
    - 2.19.4 Performance parameters
    - 2.19.5 Forbidden keywords
    - 2.19.6 Instance types

Apsara Stack SDKs

## 1 Use ASAPI to call Apsara Stack SDKs

SDKs

### 1.1 Preparations

#### 1.1.1 Log on to the API Tool console

You can log on to the API Tool console from the Apsara Uni-manager Management Console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment personnel. A browser is available. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press Enter.
2. Enter your username and password.
Obtain the username and password that are used to log on to the Apsara Uni-manager Management Console from the operations administrator. When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, which include ! @ # $ %
3. Click Log On.
4. If your account has multi-factor authentication (MFA) enabled, perform corresponding operations
in the following scenarios: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click Log On. c. Enter a six-digit MFA verification code and click Aut hent icat e. You have enabled MFA and bound an MFA device. Enter a six-digit MFA verification code and click Aut hent icat e. For more information, see the Bind a virtual MFA device to enable MFA topic in A psara Uni-manager Management Console User Guide. Apsara Stack SDKs
5. In the top navigation bar, choose Product s > Ot hers > API T ool.

#### 1.1.2 Obtain API information

To call API operations by using an SDK, you must first obtain information about the service name, API operation name, and API version. Context The information on the API Directory page of the Apsara Uni-manager Management Console is for reference only. For more information about how to call API operations, see the developer guides of cloud services. If the information on the API Directory page is different from that in the developer guide of a cloud service, the information in the developer guide prevails. Procedure
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click Product s and choose Ot hers > API T ool.
3. In the left-side navigation pane, click API Direct ory.
4. On the API Direct ory page, select the required cloud service from the Product Name drop-down
list, enter a keyword of an operation name in the search box, and then click Search.
5. In the search result, you can view the cloud service name, API operat ion name, and API
version.

#### 1.1.3 Obtain an AccessKey pair

AccessKey credentials are assigned by Resource Access Management (RAM) or Security Token Service (STS). You need to provide only a single type of AccessKey credentials for authentication when you call API operations. This topic describes how to obtain an AccessKey pair that is assigned by RAM. Context An AccessKey pair is used to verify the identity of a request sender. An AccessKey pair consists of an AccessKey ID and an AccessKey secret that are used to implement symmetric encryption. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. You can use RAM or STS to assign an AccessKey pair for authentication. An AccessKey pair that is assigned by RAM to a third party consists of an AccessKey ID and an AccessKey secret. An AccessKey 3-tuple that is assigned by STS to a third party consists of an AccessKey ID, an AccessKey secret, and a security token. For more information, see Obtain an STS AccessKey pair. The Apsara Uni-manager Management Console provides AccessKey pairs to personal accounts or organizations. Only the administrators of level-1 organizations and operations administrators can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the operations provided by the Apsara Uni-manager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the header parameters that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions may occur. Apsara Stack SDKs Warning The AccessKey pair of a personal account is managed by the permission system of the Apsara Uni-manager Management Console. If you need to obtain the AccessKey pair of an organization, make sure that your operation is allowed by an administrator. This ensures security.

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. Example: cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For more information about how to obtain organization IDs, see GetOrganizationList in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For more information about how to obtain resource set IDs, see ListResourceGroup in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance that you want to manage. If you want to obtain the ID of an Elastic Compute Service (ECS) instance, you can obtain the ID from the ECS instance list. |

Obtain the AccessKey pair of a personal account To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, click the profile picture and then select User
Inf ormat ion.
3. In the AccessKey Pair section, view the AccessKey pair of the personal account.
An AccessKey pair consists of an AccessKey ID and an AccessKey secret. These credentials provide full permissions on cloud resources within your account. You must keep the AccessKey pair confidential. Obtain the AccessKey pair of an organization To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click Ent erprise.
Apsara Stack SDKs
3. In the left-side navigation pane, choose Resources > Organizat ions.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you want
to obtain.
5. Click Management AccessKey on the right side of the page.
6. In the dialog box that appears, view the AccessKey pair of the organization.

#### 1.1.4 Obtain common header parameters

You must provide multiple header parameters when you call API operations. This topic describes how to obtain common header parameters and describes specific response parameters after you call API operations. Obtain a region ID
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane, choose Resources > Regions.
4. Click the name of the organization whose region ID you want to view.
5. View the region ID in the Regions section.
Obtain an organization ID You can call the GetOrganizationList operation to obtain the organization ID. For more information, see GetOrganizationList in Apsara Uni-manager Management Console Developer Guide. Obtain a resource set ID You can call the ListResourceGroup operation to obtain the resource set ID. For more information, see ListResourceGroup in Apsara Uni-manager Management Console Developer Guide. Obtain an instance ID You can obtain the ID of an instance in a service console of the Apsara Uni-manager Management Console. In this example, the ApsaraDB RDS console is used. Perform the following operations to obtain the ID of an RDS instance:
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose Product s > Dat abase Services > ApsaraDB RDS.
3. In the left-side navigation pane, choose Inst ances.
4. View the inst ance ID in the instance list.
Response parameters The following additional response parameters are returned by default when you call operations to query the instances of cloud services.

| Parameter | Description |
|---|---|
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The ID of the resource set. |

| psaraDB for RDS | Apsara Stack SDK |
|---|---|
| Parameter | Description |
| DepartmentName | The name of the organization. |
| Department | The ID of the organization. |

#### 1.1.5 Obtain an STS AccessKey pair

This topic describes how to use Security Token Service (STS) to call API operations. Context STS allows you to manage temporary credentials to your Apsara Stack resources. You can use STS to call API operations. An STS AccessKey 3-tuple consists of an AccessKey ID, an AccessKey secret, and a security token. When you use STS to call API operations, you must specify an STS AccessKey 3-tuple. Procedure
1. Obtain the `RAM role` .
i. Log on to the Apsara Uni-manager Management Console. ii. In the upper-right corner of the homepage, click the profile picture and then select User Inf ormat ion. iii. Click View Current Role Policy. In the View Policies of Current Role dialog box, view your `RAM role` .
2. Obtain the STS AccessKey 3-tuple.
In the following sample code, replace the parameters with the actual values. Delete the angle brackets (<>) in the final code. Parameters: <yourRegionID>: Replace the parameter with the region ID. <yourAccessKeyID>: Replace the parameter with your AccessKey ID. <yourAccessKeySecret>: Replace the parameter with your AccessKey secret. <yourRoleSessionName>: Replace the parameter with the name of the current session. <yourRoleArn>: Replace the parameter with the ARN of your RAM role. "sts.aliyuns.com": Replace the parameter with the endpoint of STS. Apsara Stack SDKs

```
public static void main(String[] args) {
    // Create and initialize a DefaultAcsClient instance.
    // Specify the region ID, AccessKey ID, and AccessKey secret.
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourAccessKe
yID>", "<yourAccessKeySecret>");
    HttpClientConfig clientConfig = HttpClientConfig.getDefault();
    clientConfig.setIgnoreSSLCerts(true);
    clientConfig.setProtocolType(ProtocolType.HTTPS);
    profile.setHttpClientConfig(clientConfig);
    IAcsClient client = new DefaultAcsClient(profile);
    String assumeRole = callAssumeRole(client);
    if (StringUtils.isEmpty(assumeRole)) return;
    JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
    JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
    // Obtain the STS AccessKey 3-tuple.
    String stsAK = credentials.getString("AccessKeyId");
    String stsSK = credentials.getString("AccessKeySecret");
    String stsToken = credentials.getString("SecurityToken");
```

`}`

```java
private static String callAssumeRole(IAcsClient client) {
    CommonRequest request = new CommonRequest();
    // Replace "sts.aliyuns.com" with the endpoint of STS. The format of an STS endpoin
t is sts-vpc.${global:region}.${global:internet-domain}.
    request.setSysDomain("sts.aliyuns.com");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
    // Replace "<yourRoleSessionName>" with the name of the current session.
    request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
    // Replace "<yourRoleArn>" with the actual ARN obtained for the RAM role in the pre
ceding step.
    request.putQueryParameter("RoleArn", "<yourRoleArn>");
    try {
        CommonResponse response = client.getCommonResponse(request);
        return response.getData();
    } catch (ServerException e) {
        System.out.println(e.getErrCode());
        System.out.println(e.getErrMsg());
    } catch (ClientException e) {
        System.out.println(e.getErrCode());
        System.out.println(e.getErrMsg());
```

`}`

```
    return null;
```

`}`
3. Use the STS AccessKey 3-tuple to call an API operation of a cloud service. The following sample
code provides an example on how to call the `DescribeRegions` operation of ApsaraDB RDS. Apsara Stack SDKs In the following sample code, replace the parameters with the actual values. Delete the angle brackets (<>) in the final code. Parameters: <yourRegionID>: Replace the parameter with the region ID. <yourStsAccesskeyID>: Replace the parameter with your STS AccessKey ID. <yourStsAccessKeySecret>: Replace the parameter with your STS AccessKey secret. <yourStsToken>: Replace the parameter with your security token. <yourResourceGroupID>: Replace the parameter with the resource set ID. <yourRegionID>: Replace the parameter with the organization ID.

```java
public static void main(String[] args) {
    // Replace "<yourRegionID>" with the region ID.
    // Replace "<yourStsAccessKeyID>" and "<yourStsAccessKeySecret>" with the AccessKey
ID and AccessKey secret of the 3-tuple obtained in the previous step.
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourStsAcces
skey>", "<yourStsAccessSecret>");
    HttpClientConfig clientConfig = HttpClientConfig.getDefault();
    clientConfig.setIgnoreSSLCerts(true);
    clientConfig.setProtocolType(ProtocolType.HTTPS);
    profile.setHttpClientConfig(clientConfig);
    IAcsClient client = new DefaultAcsClient(profile);
    CommonRequest request = new CommonRequest();
    request.setSysDomain("rds.aliyuns.com");
    request.setSysProduct("RDS");
    request.setSysAction("DescribeRegions");
    request.setSysVersion("2014-08-15");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
    // Replace "<yourRegionID>" with the region ID.
    request.putHeadParameter("x-acs-regionid", "<yourRegionID>");
    // Replace "<yourStsToken>" with the security token of the 3-tuple obtained in the
previous step.
    request.putQueryParameter("SecurityToken", "<yourStsToken>");
    // Optional. Replace the parameter with the resource set ID.
    // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
    // Required. Replace the parameter with the organization ID.
    request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>");
    try {
        CommonResponse response = client.getCommonResponse(request);
        System.out.println(response.getData());
    } catch (ServerException e) {
        System.out.println(e.getErrCode());
        System.out.println(e.getErrMsg());
    } catch (ClientException e) {
        System.out.println(e.getErrCode());
        System.out.println(e.getErrMsg());
```

`}` `}` Apsara Stack SDKs

### 1.2 Use POP to make API calls

#### 1.2.1 Preparations

Like in the public cloud, you can use the point of presence (POP) gateway to call API operations in Apsara Stack. This topic describes the preparations before you use the POP gateway to call API operations. Background information In Apsara Stack, you can use both Apsara Stack API (ASAPI) and the POP gateway to call API operations. To ensure that you can use Apsara Stack in the same manner as you use the public cloud, we recommend that you use the POP gateway to call API operations in Apsara Stack. Obtain service endpoints To use the POP gateway to call API operations, you must use the service endpoints. You can obtain service endpoints from Apsara Stack onsite O&M engineers. You can also obtain service endpoints by yourself. The following example shows how to obtain a service endpoint. Elastic Compute Service (ECS) is used in this example.
1. Log on to the Apsara Infrastructure Management console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose Product s > Base/Plat f orms > Apsara Inf rast ruct ure Management Framework.
2. In the left-side navigation pane, click Report s.
3. On the All Report s page, search for `Registration Vars of Services` and click the report name.
4. On the Regist rat ion Vars of Services page, click the
icon next to Service and search for `ECS` .
5. Find the `ecs-yaochi` service, right-click the Service Regist rat ion column, and then select Show
More. Apsara Stack SDKs On the Det ails page, view the int ernal.openapi.endpoint value, which is the `endpoint` . Obtain common parameters You must obtain the parameters required when you use the POP gateway to call API operations, such as the organization ID, resource set ID, region ID, and instance ID. For more information, see Obtain common header parameters.

#### 1.2.2 SDK for Java

Before you use POP SDK for Java to make API calls, you must first understand the RPC and ROA styles. Prerequisites An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed. SSL certificate validation is ignored for requests over HTTPS. Call examples The following sample code provides an example on how to use the RPC style to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05-26. Sample code:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class DescribeInstances {
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile("<your-regionid>", "<yourAccessK
eyId>", "<yourAccessSecret>");
        // Ignore SSL certificate validation.
        // HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        // clientConfig.setIgnoreSSLCerts(true);
        // Configure the time-out period for a connection.
        // clientConfig.setConnectionTimeoutMillis(3000L);
        // Set the read timeout period.
        // clientConfig.setReadTimeoutMillis(10000L);
        // profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and configure the parameters.
        CommonRequest request = new CommonRequest();
```

Apsara Stack SDKs

```java
        // Specify the request method.
        request.setSysMethod(MethodType.POST);
        // Set the service endpoint.
        request.setSysDomain("<ecsEndpoint>");
        // Specify the version of the API operation.
        request.setSysVersion("2014-05-26");
        // Specify the name of the service that you want to access and the region where the
service resides.
        request.setSysLocationProduct("Ecs");
        // Specify the name of the API operation.
        request.setSysAction("DescribeInstances");
        // When you use the STS AccessKey ID to call RPC API operations, you must add the S
ecurityToken parameter to the header.
        // request.putBodyParameter("SecurityToken", "<your-SecurityToken>");
        // Configure operation-specific parameters.
        request.putBodyParameter("PageSize", "10");
        request.putBodyParameter("PageNumber", "1");
        // Required. The call source.
        request.putHeadParameter("x-acs-caller-sdk-source", "ApiTestDemo");
        // Optional. For the historical versions before Enterprise Edition V3.15.0.
        request.putHeadParameter("x-acs-regionid", "<your-regionid>");
        // Optional. The resource set ID.
        request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>");
        // Required. The organization ID.
        request.putHeadParameter("x-acs-organizationid", "<your-organizationid>");
        // Optional. For the modify and delete operations.
        // request.putHeadParameter("x-acs-instanceid", "<your-instanceid>");
        try {
            // Initiate the request and handle the response or exceptions.
            CommonResponse response = client.getCommonResponse(request);
            System.out.println(response.getData());
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            System.out.println("ErrCode:" + e.getErrCode());
            System.out.println("ErrMsg:" + e.getErrMsg());
            System.out.println("RequestId:" + e.getRequestId());
```

`}` `}` `}` The following sample code provides an example on how to use the ROA style to make an API call. In this example, the GetNamespaceList operation of Container Registry is called, and the API version is 2016- 06-07. Sample code:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse;
```

Apsara Stack SDKs

```java
import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class GetNamespaceList {
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile("<your-regionid>", "<yourAccessK
eyId>", "<yourAccessSecret>");
        // Ignore SSL certificate validation.
        // HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        // clientConfig.setIgnoreSSLCerts(true);
        // Configure the time-out period for a connection.
        // clientConfig.setConnectionTimeoutMillis(3000L);
        // Set the read timeout period.
        // clientConfig.setReadTimeoutMillis(10000L);
        // profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and configure the parameters.
        CommonRequest request = new CommonRequest();
        // Set the request protocol to HTTPS.
        request.setSysProtocol(ProtocolType.HTTP);
        // Specify the request method.
        request.setSysMethod(MethodType.GET);
        // Set the service endpoint.
        request.setSysDomain("<crEndpoint>");
        // Specify the version of the API operation.
        request.setSysVersion("2016-06-07");
        // Configure the uriPattern parameter, which is required for the ROA style.
        request.setSysUriPattern("/namespace");
        // Specify the name of the service that you want to access and the region where the
service resides.
        request.setSysLocationProduct("cr");
        // Specify the name of the API operation.
        request.setSysAction("GetNamespaceList");
        // Required. The call source.
        request.putHeadParameter("x-acs-caller-sdk-source", "ApiTestDemo");
        // Optional. For the historical versions before Enterprise Edition V3.15.0.
        request.putHeadParameter("x-acs-regionid", "<your-regionid>");
        // Optional. The resource set ID.
        request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>");
        // Required. The organization ID.
        request.putHeadParameter("x-acs-organizationid", "<your-organizationid>");
        // Optional. For the modify and delete operations.
        // request.putHeadParameter("x-acs-instanceid", "<your-instanceid>");
```

Apsara Stack SDKs

```java
        // When you use the STS AccessKey ID to call ROA API operations, you must add the x
-acs-security-token parameter to the header.
        // request.putHeadParameter("x-acs-security-token", "<your-securitytoken>");
        try {
            // Initiate the request and handle the response or exceptions.
            CommonResponse response = client.getCommonResponse(request);
            System.out.println(response.getData());
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            System.out.println("ErrCode:" + e.getErrCode());
            System.out.println("ErrMsg:" + e.getErrMsg());
            System.out.println("RequestId:" + e.getRequestId());
```

`}` `}` `}` Not ice If you send a request over HTTPS, you must enable the request to ignore SSL certificate validation.

#### 1.2.3 SDK for Go

This topic describes how to use POP SDK for Go. Prerequisites An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed. Background information Both RPC and ROA styles are supported for API calls. Call examples The following sample code provides an example on how to use the RPC style to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05-26. Sample code: Apsara Stack SDKs

```java
package main import (
    "fmt"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

`)`

```
func main() {
    client, err := sdk.NewClientWithAccessKey("<your-RegionID>", "<AccessKey ID>", "<Access
Key Secret>")
    request := requests.NewCommonRequest()
    request.Method = "POST"
    request.Domain = "<ECSEndpoint>"
    request.Version = "2014-05-26"
    request.ApiName = "DescribeInstances"
    request.Product = "Ecs"
    // When you use the STS AccessKey ID to call RPC API operations, you must add the Secur
ityToken parameter to the header.
    // request.QueryParams["SecurityToken"]="<your-SecurityToken>"
    // Required. The call source.
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
    // Optional. For the historical versions before Enterprise Edition V3.15.0.
    request.Headers["x-acs-regionid"] = "<your-RegionID>"
    // Optional. The resource set ID.
    request.Headers["x-acs-resourcegroupid"] = "<your-ResourceGroupID>"
    // Required. The organization ID.
    request.Headers["x-acs-organizationid"] = "<your-OrganizationID>"
    // Optional. For the modify and delete operations.
    // request.Headers["x-acs-instanceid"] = "<your-InstanceID>"
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
```

`}`

```
    fmt.Print(response.GetHttpContentString())
```

`}` The following sample code provides an example on how to use the ROA style to make an API call. In this example, the GetNamespaceList operation of Container Registry is called, and the API version is 2016- 06-07. The following sample code shows how to call API operations: Apsara Stack SDKs

```java
package main import (
 "fmt"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
 "os"
```

`)`

```
func main() {
    client, err := sdk.NewClientWithAccessKey("<your-regionid>", "<yourAccessKeyId>", "<you
rAccessSecret>")
 request := requests.NewCommonRequest()
 request.Method = "GET"
 request.Domain = "<crEndpoint>"
 request.Version = "2016-06-07"
 request.ApiName = "GetNamespaceList"
 request.Product = "cr"
 request.PathPattern = "/namespace"
 // When you use the STS AccessKey ID to call ROA API operations, you must add the x-acs-se
curity-token parameter to the header.
 // request.Headers["x-acs-security-token"] = "<your-SecurityToken>"
 // Required. The call source.
 request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
    // Optional. For the historical versions before Enterprise Edition V3.15.0.
    request.Headers["x-acs-regionid"] = "<your-RegionID>"
    // Optional. The resource set ID.
    request.Headers["x-acs-resourcegroupid"] = "<your-ResourceGroupID>"
    // Required. The organization ID.
    request.Headers["x-acs-organizationid"] = "<your-OrganizationID>"
 // Optional. For the modify and delete operations.
 // request.Headers["x-acs-instanceid"] = "<your-InstanceID>"
 response, err := client.ProcessCommonRequest(request)
 if err != nil {
  panic(err)
```

`}`

```
 fmt.Print(response.GetHttpContentString())
```

`}` Configure proxies You can configure proxies in one of the following ways when you call API operations: Configure proxies as environment variables. Set the HTTP_PROXY and HTTPS_PROXY environment variables, or set the NO_PROXY environment variable. Sample code: Apsara Stack SDKs

```java
import (
    "os"
```

`)`

```
func main(){
 os.Setenv("HTTP_PROXY", "http://x.x.x.x:xxxx") // Configure the HTTP_PROXY environment v
ariable.
 os.Setenv("HTTPS_PROXY", "https://x.x.x.x:xxxx") // Configure the HTTPS_PROXY environmen
t variable.
```

`}` Configure proxies on the client. Sample code:

```
// The proxies that are configured on the client take precedence over those that are conf igured by using environment variables. client.SetHttpProxy("http://x.x.x.x:xxxx") // Configure the HTTP proxy. client.GetHttpProxy() // Query the HTTP proxy. client.SetHttpsProxy("https://x.x.x.x:xxxx") // Configure the HTTPS proxy. client.GetHttpsProxy() // Query the HTTPS proxy. client.SetNoProxy("127.0.0.1,localhost") // Configure the proxy whitelist. client.GetNoProxy() // Query the proxy whitelist.
```

#### 1.2.4 SDK for Python

This topic describes how to use POP SDK for Python. Prerequisites An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed. Background information Only the remote procedure call (RPC) style is supported for API calls. Call examples The following sample code provides an example on how to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05- 26. Sample code:

```java
from aliyunsdkcore.client import AcsClient import os from aliyunsdkcore.request import CommonRequest
# Create an AcsClient object.
client = AcsClient(
    "<AccessKey ID>",
    "<AccessKey Secret>",
    "<your-RegionID>",
timeot1000
#Setthetimeotperiod
```

Apsara Stack SDKs

```
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
    request = CommonRequest()
    # When you use the STS AccessKey ID to call RPC API operations, you must add the Securi
tyToken parameter to the header.
    # params = {"PageSize":"10","PageNumber":"1","SecurityToken":"<your-SecurityToken>"};
    params = {"PageSize":"10","PageNumber":"1"};
    request.set_body_params(params)
    headers = {
        # Required. The call source.
        "x-acs-caller-sdk-source":"ApiTestDemo",
        # Optional. For the historical versions before Enterprise Edition V3.15.0.
        "x-acs-regionid":"<your-RegionID>",
        # Optional. The resource set ID.
        "x-acs-resourcegroupid":"<your-ResourceGroupID>",
        # Required. The organization ID.
        "x-acs-organizationid":"<your-OrganizationID>"
        # Optional. For the modify and delete operations.
        # "x-acs-instanceid":"<your-InstanceID>"
```

`}`

```python
    request.set_headers(headers)
    request.set_version("2014-05-26")
    request.set_action_name("DescribeInstances")
    request.set_endpoint("<ecsEndpoint>") // Replace ecsEndpoint with the real endpoint.
    request.set_product("Ecs")
    request.set_method("POST")
    # Initiate the API request and obtain the response.
    response = client.do_action_with_exception(request)
    print(response)
if __name__ == '__main__':
    print("Hello Aliyun OpenApi!")
    hello_ecs_instance()
```

Configure proxies You can configure HTTP_PROXY and HTTPS_PROXY environment variables when you call API operations. Sample code: Apsara Stack SDKs

```bash
# Configure the HTTPS proxy.
os.environ["HTTPS_PROXY"] = "http://x.x.x.x:xxxx"
# Configure the HTTP proxy.
os.environ["HTTP_PROXY"] = "https://x.x.x.x:xxxx"
```

### 1.3 Use ASAPI to make API calls

#### 1.3.1 ASAPI overview

This topic describes the architecture and features of the Apsara Stack API (ASAPI). The ASAPI is a unified ingress gateway for Apsara Stack services and a main component of the Apsara Uni-manager Management Console. The ASAPI provides a unified method for you to manage and make API calls. You can use Apsara Stack SDK to centrally make API calls to Apsara Stack services, including Elastic Compute Service (ECS) and Virtual Private Cloud (VPC). The ASAPI allows you to make API calls to manage and maintain Apsara Stack services. Make API calls to implement enterprise-grade management. For example, you can manage Apsara Stack SDKs organizations, users, roles, resource sets, and logon policies. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to manage operations. For example, you can manage quotas, usage statistics, specifications, and password policies. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to manage resources. For example, you can create, delete, query, or modify cloud resources. These operations are provided by Apsara Stack services. If you call an API operation to create an ECS instance or a VPC, the API operation is provided by ECS or VPC. Make API calls to query monitoring metrics of Apsara Stack services. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to perform O&M. For example, you can manage monitoring and alerting, inventories, tasks, and physical servers. These operations are provided by the Apsara Uni-manager Operations Console. For more information, see the developer guide of the corresponding Apsara Stack service. For information about API operations used to manage organization users, see Apsara Uni-manager Management Console Developer Guide. For information about the API operation used to create an ECS instance, see ECS Developer Guide. If the "Use Apsara Stack SDK to make API calls" section is included in the developer guide of an Apsara Stack service, the ASAPI is supported by the Apsara Stack service. In this case, you can make API calls based on the developer guide.

#### 1.3.2 Generate an endpoint for ASAPI

This topic describes three methods used to generate an endpoint for Apsara Stack API (ASAPI). Method 1: Use Registration Vars of Services to generate an endpoint
1. Log on to the Apsara Infrastructure Management console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose Products > Base/Plat f orms > Apsara Inf rast ruct ure Management Framework.
2. In the left-side navigation pane, click Report s.
3. On the All Report s page, search for Registration Vars of Services and click the report name.
Apsara Stack SDKs
4. On the Regist rat ion Vars of Services page, click the
icon next to Service and search for `as` `api` .
5. Find the asapi service, right-click in the Service Regist rat ion column, and then select Show More
from the shortcut menu. In the Det ails dialog box, obtain the value of asapi.public.endpoint .
6. Generate an endpoint in the following format for ASAPI:

```
https://<asapi.public.endpoint>/asapi/v3
```

Method 2: Use cluster resources to generate an endpoint
1. Log on to the Apsara Infrastructure Management console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose Products > Base/Plat f orms > Apsara Inf rast ruct ure Management Framework.
2. Go to the Clusters page.
i. In the left-side navigation pane, choose Operat ions > Clust er Operat ions. ii. In the Clust er field, enter `ascm` . iii. Find the cluster that you want to manage and click Operat ions in the Act ions column.
3. Obtain the value of the domain parameter.
i. Click the Cluster Resources tab. ii. In the Name field, search for `asapi_dns_public` . iii. Click Det ails in the Applicat ion Paramet er column. In the Applicat ion Paramet er message, view the value of domain.
4. Generate an endpoint in the following format for ASAPI:

```
https://<domain>/asapi/v3
```

Method 3: Concatenate strings to generate an endpoint You can also concatenate strings to generate an endpoint in the following format:

```
https://public.asapi.<region>.<internet-domain>/asapi/v3
```

Apsara Stack SDKs
1. Replace <region> with your actual region ID. For information about how to query a region ID, see
Obtain a region ID.
2. Replace <internet-domain> with the root domain of your Apsara Stack service. To obtain the root
domain, contact Apsara Stack O&M personnel. Take note of this point: Use the internet-domain parameter instead of the intranet-domain parameter. Assume that the value of region is cn-****-****-d01 and the value of int ernet -domain is inter.****.****.com. A complete sample endpoint is provided for reference:

```
https://public.asapi.cn-****-****-d01.inter.****.****.com/asapi/v3
```

#### 1.3.3 Obtain Apsara Stack SDKs

Apsara Stack API (ASAPI) is a unified portal provided by Apsara Stack. You can use the ASAPI to connect to all Apsara Stack services. Apsara Stack provides SDKs for API calls. You can go to Apsara Stack documentation and download the Apsara Stack SDKs in the Ot her Resources section at the lower part of the page.

#### 1.3.4 Common parameters

Common request parameters must be included in all API requests. Common request parameters The following table describes the common request parameters that are used when you call API operations supported by Apsara Stack API (ASAPI).

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. |
| Product | String | Yes | The name of the service. |
| Version | String | Yes | The version of the operation. |
| RegionId | String | Yes | The ID of the region. For more information, see Obtain a region ID. |
| AccessKeyId | String | Yes | The AccessKey ID that is used to access the service. For more information, see Obtain an AccessKey pair. |
| Signature | String | Yes | The signature string. For more information, see Request signatures. |

Apsara Stack SDKs

| Parameter | Type | Required | Description |
|---|---|---|---|
| SignatureMethod | String | Yes | The encryption algorithm of the signature string. Valid values: HMAC- SHA1 and HMAC-SHA256. |
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Valid values: 1.0 and 2.0. |
| SignatureNonce | String | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Example: 2018-01- 01T12:00:00Z. |
| Format | String | Yes | The format in which to return the response. Set the value to JSON. |

```
The Signature , SignatureMethod , SignatureVersion , SignatureNonce ,
```

`Timestamp` , and `Format` parameters are encapsulated into Apsara Stack SDK. You do not need to specify these parameters.

#### 1.3.5 SDK description

##### 1.3.5.1 SDK for Java

This topic describes how to obtain and use Apsara Stack SDK for Java to call API operations. Prerequisites An Apsara Stack tenant account that has the required permissions and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret are obtained. You can obtain and view your AccessKey pair in the Apsara Uni-manager Management Console. For more information, see Obtain an AccessKey pair. The endpoint of Apsara Stack API (ASAPI) is obtained. For more information, see Generate an endpoint for ASAPI. Apsara Stack SDK for Java 1.8 or later is installed. Background information The help center of Apsara Stack provides Maven dependencies and JAR files for Apsara Stack SDK for Java. You can write code to use Apsara Stack SDK for Java to call API operations. In this example, the Windows 10 64-bit OS and IntelliJ IDEA are used. Procedure Apsara Stack SDKs
1. Use one of the following methods to configure Maven in IntelliJ IDEA. Maven is a tool used for
project management. Use Maven that is integrated in IntelliJ IDEA. Download Maven based on your OS from the official website and configure Maven. For more information, see Downloading Apache Maven 3.8.6.
2. Obtain the Maven dependencies for Apsara Stack SDK for Java from the official website. For more
information, see Obtain Apsara Stack SDKs.
3. Use one of the following methods to create a Maven project:
Method 1: Create a Maven project in IntelliJ IDEA. Method 2: Convert an existing project to a Maven project. a. Right-click the project that you want to convert and select Add Framework Support .... Apsara Stack SDKs b. Select Maven and click OK.
4. Create a folder named libs in the root directory of the project. Then, add the JAR file of Apsara
Stack SDK for Java to the libs folder, as shown in the following figure.
5. Add the dependencies of Apsara Stack SDK for Java to the pom.xml file in the project directory.
Apsara Stack SDKs

```xml
<dependencies>
    <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>asapi</artifactId>
        <version>1.0.6.4-RELEASE</version>
        <scope>system</scope>
        <systemPath>${project.basedir}/libs/asapi-1.0.6.4-RELEASE.jar</systemPath>
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
    <dependency>
    <groupId>org.apache.httpcomponents</groupId>
    <artifactId>httpclient</artifactId>
    <version>4.5.7</version>
    <systemPath>${project.basedir}/libs/httpclient-4.5.7.jar</systemPath>
  </dependency>
</dependencies>
```

Replace `1.0.6.4-RELEASE` with the actual version of Apsara Stack SDK for Java.
6. On the right side of IntelliJ IDEA, view information in the Maven section.
If the information in the following figure appears, the dependencies are added. Use Apsara Stack SDK for Java You can use the GET or POST method to call API operations provided by ASAPI. The following sample code shows how to call API operations: Apsara Stack SDKs

```java
// 1. Create a connection to an ASClient object. ASClient client = new ASClient(); // 2. Configure the identifier of the requester. This parameter is required and used only f or identification. You can set this parameter to a random value. client.setSdkSource("<The identifier of the requester>"); Map<String, Object> parameters = new HashMap<String, Object>(); // 3. Configure the parameters for authorization. The parameter values vary based on your e nvironment. // The AccessKey ID of your Apsara Stack tenant account. parameters.put("AccessKeyId","<AccessKey ID>"); // The AccessKey secret of your Apsara Stack tenant account. parameters.put("AccessKeySecret", "<AccessKey Secret>"); // The ID of the region. parameters.put("RegionId", "<your RegionID>"); // 4. Configure parameters for an API call. In this example, the Product, Action, and Versi on parameters are configured. parameters.put("Product", "<The name of the service>"); parameters.put("Action", "<The name of the API operation>"); parameters.put("Version", "<The version of the API operation>"); // When you use the Security Token Service (STS) AccessKey ID to call remote procedure call (RPC) API operations, you must add the SecurityToken parameter to the header. // parameters.put("SecurityToken", "<your-securitytoken>"); // When you use the STS AccessKey ID to call resource-oriented architecture (ROA) API opera tions, you must add the x-acs-security-token parameter to the header. // headers.put("x-acs-security-token", "<your-securitytoken>"); // 5. Configure operation-specific parameters. parameters.put("<The name of the operation-specific parameter>", "<The value of the operati on-specific parameter>"); // 6. Configure request headers and the encryption method for the signature string. Valid v alues of the SignatureMethod parameter: HMAC-SHA1 and HMAC-SHA256. By default, HMAC-SHA256 is used. Map<String, String> headers = new HashMap<String, String>(); //headers.put("SignatureMethod", "HMAC-SHA1"); headers.put("x-acs-regionid", "<your-regionid>"); headers.put("x-acs-resourcegroupid", "<your-resourcegroupid>"); headers.put("x-acs-organizationid", "<your-organizationid>"); headers.put("x-acs-instanceid", "<your-instanceid>"); // 7. Call the API operation. We recommend that you use the doPost() method. // Configure the timeout period for a connection. //client.setConnectTimeout(10000); // Configure the timeout period for a request. // client.setSocketTimeout(10000); String result = client.doPost(endpoint, headers, parameters); System.out.println(result);
```

Configure proxies If you need to use a proxy to call API operations, use the following sample code to configure the proxy: Apsara Stack SDKs

```
Cloud cloud = new Cloud(); // Configure the IP address of the proxy. cloud.setConfig("proxy_host", "<IP>"); // Configure the port used by the proxy. cloud.setConfig("proxy_port", "<Port>"); // Create a connection to an ASClient object. ASClient client = new ASClient(cloud);
```

Header parameters

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. For more information about how to obtain a region ID, see Obtain a region ID. |
| x-acs-organizat ionid | The ID of the organization in the Apsara Uni- manager Management Console. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. |
| x-acs-inst anceid | The ID of the instance on which you want to perform the operation. |

##### 1.3.5.2 SDK for Python

This topic describes how to obtain and use Apsara Stack SDK for Python to call API operations. Prerequisites An Apsara Stack tenant account that has the required permissions and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret are obtained. For more information about how to obtain an AccessKey pair in the Apsara Uni-manager Management Console, see Obtain an AccessKey pair. The endpoint of Apsara Stack API (ASAPI) is obtained. For more information, see Generate an endpoint for ASAPI. Install Apsara Stack SDK for Python
1. Download the required version of Apsara Stack SDK for Python. For more information, see Obtain
Apsara Stack SDKs.
2. Upload the compressed file of Apsara Stack SDK for Python to the host from which you want to
send API requests and extract the file. Then, run the following code in the directory of the extracted file to install Apsara Stack SDK for Python:

```bash
# Install Apsara Stack SDK for Python 2.x.
pip install aliyun-python2-sdk-asapi-2.4.7.tar.gz
# Install Apsara Stack SDK for Python 3.x.
pip3 install aliyun-python3-sdk-asapi-2.4.7.tar.gz
```

Apsara Stack SDKs Replace `2.4.7` with the actual version of Apsara Stack SDK for Python. Call examples You can use the GET or POST method to call API operations provided by ASAPI.

```python
# 1. Add dependencies.
   from aliyunsdkasapi.ASClient import ASClient
   from aliyunsdkasapi.AsapiRequest import AsapiRequest
   if __name__ == '__main__':
    # 2. Create a request. The Product parameter specifies the name of the service. The Ver
sion parameter specifies the version of the API operation. The Action parameter specifies t he operation that you want to perform. The asapi-endpoint parameter specifies the endpoint of ASAPI.
    req = AsapiRequest("<Product>", "<Version>", "<Action>", "<asapi-endpoint>")
    # 3. Configure operation-specific parameters.
    req.add_body_params("<key>", "<value>")
 # When you use the Security Token Service (STS) AccessKey ID to call remote procedure call
(RPC) API operations, you must add the SecurityToken parameter to the header.
 # req.add_body_params("SecurityToken", "<your-securitytoken>");
 # When you use the STS AccessKey ID to call resource-oriented architecture (ROA) API opera
tions, you must add the x-acs-security-token parameter to the header.
 # req.add_header("x-acs-security-token", "<your-securitytoken>");
    # 4. Configure request headers.
    req.add_header("x-acs-resourcegroupid", "<your-resourcegroupid>");
    req.add_header("x-acs-organizationid", "<your-organizationid>");
    req.add_header("x-acs-regionid", "<your-regionid>");
    req.add_header("x-acs-instanceid", "<your-instanceid>");
    # 5. Configure a request method.
    req.set_method("POST")
    # 6. Configure initialization parameters for an ASClient object. The parameter values v
ary based on your environment. The timeout parameter specifies the timeout period for a req uest. The cert_file parameter specifies the certificate. The verify parameter specifies whe ther to verify the certificate.
    as_client = ASClient("<accesskeyid>", "<accesskeysecret>", "<regionid>",timeout=1000,
            cert_file=None,
            verify=False)
    # Configure the identifier of the requester. This parameter is required and used only f
or identification. You can set this parameter to a random value.
    as_client.setSdkSource("<The identifier of the requester>")
    response = as_client.do_request(req)
    print(response)
```

Header paramet ers Apsara Stack SDKs

| Paramet er | Descript ion |
|---|---|
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. |
| x-acs-regionid | The ID of the region. For more information about how to obtain a region ID, see Obtain a region ID. |
| x-acs-instanceid | The ID of the instance on which you want to perform the operation. |

Configure proxies Perform the following steps to configure a proxy:
1. Import OS dependencies.

```java
import os
```

2. Configure one or more proxies.

```bash
# Before you make an API call, configure one or more proxies.
os.environ['http_proxy'] = "http://x.x.x.x:xxxx" os.environ['https_proxy'] = "https://x.x.x.x:xxxx"
```

##### 1.3.5.3 SDK for Node.js

After you install Apsara Stack SDK for Node.js, you can write code to call API operations by using Apsara Stack API (ASAPI). Prerequisites An AccessKey pair or an STS AccessKey 3-tuple is obtained. We recommend that you use an AccessKey pair or an STS AccessKey 3-tuple for personal accounts to call API operations of the Apsara Uni-manager Management Console and cloud services. For more information, see Obtain an AccessKey pair. The endpoint of ASAPI is obtained. For more information, see Generate an endpoint for ASAPI. If the endpoint of ASAPI uses the HTTPS protocol, you can ignore certificates by setting `NODE_TLS_REJECT_UNAUTHORIZED` to 0. The package of Apsara Stack SDK for Node.js is obtained. For more information, see Obtain Apsara Stack SDKs. Install dependencies Apsara Stack SDKs The asapi-nodejs-sdk.t gz package contained in the Apsara Stack SDK package includes Apsara Stack SDK for Node.js and relevant dependencies. You can install SDK for Node.js no matter whether the Internet is accessible.
1. Obtain the asapi-nodejs-sdk.t gz package from the Apsara Stack SDK package.
2. Run the following command to decompress the asapi-nodejs-sdk.t gz package. Store the
extracted asapi-nodejs-sdk folder to the root directory of the Node.js project. We recommend that you use Node.js of an LTS version.

```
tar -zxf asapi-nodejs-sdk.tgz
```

3. In the root directory of the Node.js project, run the following command to install Apsara Stack SDK
for Node.js.

```
npm i ./asapi-nodejs-sdk --save
```

Common templates The following code provides a common template to call API operations by using Apsara Stack SDK for Node.js:

```
// Import the SDK dependencies. const Controller = require('egg').Controller; const ASAPIClient = require('@ali/asapi-nodejs-sdk'); // Configure the endpoint of ASAPI and authorization credentials. const cnofig = {
  API_GATEWAY: '<The endpoint of ASAPI>',
  regionId: '<yourRegionId>',
  accessKeyId: '<yourAccessKeyId>',
  accessKeySecret: '"<yourAccessKeySecret>'
```

};

```json
// Initialize the ASAPI client. const AsapiClient = new ASAPIClient(cnofig, this.ctx); // Configure request parameters. const params = {
  "Action": "<The name of the API operation>",
  "Product": "<The name of the service>",
  "Version": "<The version of the API operation>",
  "regionId": "<yourRegionId>",
  // When you use an STS AccessKey 3-tuple to call an API operation, you must add the Secur
ityToken field to the request parameters.
  // "SecurityToken": "<yourSecurityToken>"
  // Configure operation-specific parameters.
  "<The name of the operation-specific parameter>": "<The value of the operation-specific p
arameter>"
```

`}`

```
// Configure header parameters. // Configure the identifier of the requester. This parameter is required and used only for identification. You can set this parameter to a random value. AsapiClient.addHeader('x-acs-caller-sdk-source', '<The identifier of the requester>') // The API of a cloud service requires multiple common header parameters, including x-acs-r egionid, x-acs-organizationid, x-acs-resourcegroupid, and x-acs-instanceid. For more inform ation, see Obtain the values of common header parameters in the Developer Guide. AsapiClient.addHeader("x-acs-resourcegroupid", "<yourResourceGroupId>");
```

`A`

```
iCli
```

`t`

```
ddH
```

`d` `("` `i` `ti`

```
id"
```

`"<` `O` `i` `ti`

```
Id>")
```

Apsara Stack SDKs

```
AsapiClient.addHeader("x-acs-organizationid", "<yourOrganizationId>"); AsapiClient.addHeader("x-acs-regionid", "<yourRegionId>"); AsapiClient.addHeader("x-acs-instanceid", "<yourInstanceId>"); // Initiate a call and obtain the response. try {
  const res = await AsapiClient.doRequest(cnofig.API_GATEWAY, params, {
    method: 'POST', // Specify a request method.
    formatParams: false, // Specify whether to format parameters and capitalize the first l
etter of each parameter.
    enableProxy: false, // Specify whether to configure a proxy. If the parameter is set to
true, you must configure a proxy. If the parameter is set to false, null can be used.
    proxy: 'http://x.x.x.x:xxxx', // Specify a proxy endpoint.
    timeout: 10000 // Specify a timeout period.
    //ca: fs.readFileSync(path.resolve(__dirname, keys_dir,'ca.crt'), 'utf8')
    // (Optional) Configure a CA certificate. For more information, see https://nodejs.org/
api/https.html#https_https_request_options_callback.
```

`})`

```
  console.log(res)
} catch (e) {
  console.log(e)
```

`}` Call examples The following code provides an example on how to call the `GetOrganizationList` operation by using SDK for Node.js: Apsara Stack SDKs

```
// Import the SDK dependencies. const Controller = require('egg').Controller; const ASAPIClient = require('@ali/asapi-nodejs-sdk'); // Configure the endpoint of ASAPI and authorization credentials. const cnofig = {
  API_GATEWAY: '<The endpoint of ASAPI>',
  regionId: '<yourRegionId>',
  accessKeyId: '<yourAccessKeyId>',
  accessKeySecret: '"<yourAccessKeySecret>'
```

};

```json
// Initialize the ASAPI client. const AsapiClient = new ASAPIClient(cnofig, this.ctx); // Configure request parameters. const params = {
  "Action": "GetOrganizationList",
  "Product": "ascm",
  "Version": "2019-05-10",
  "regionId": "<yourRegionId>",
  // Configure operation-specific parameters.
  "id": 3
```

`}`

```
// Configure header parameters. AsapiClient.addHeader('x-acs-caller-sdk-source', '<The identifier of the requester>') // Initiate a call and obtain the response. try {
  const res = await AsapiClient.doRequest(cnofig.API_GATEWAY, params, {
    method: 'POST', // Specify a request method.
    formatParams: false, // Specify whether to format parameters and capitalize the first l
etter of each parameter.
    enableProxy: false, // Specify whether to configure a proxy. If the parameter is set to
true, you must configure a proxy. If the parameter is set to false, null can be used.
    proxy: 'http://x.x.x.x:xxxx', // Specify a proxy endpoint.
    timeout: 10000 // Specify a timeout period.
    //ca: fs.readFileSync(path.resolve(__dirname, keys_dir,'ca.crt'), 'utf8')
    // (Optional) Configure a CA certificate. For more information, see https://nodejs.org/
api/https.html#https_https_request_options_callback.
```

`})`

```
  console.log(res)
} catch (e) {
  console.log(e)
```

`}` Configure proxies If a network proxy exists between your environment and ASAPI, you must configure a proxy by using the following parameters:

```
enableProxy: true, // Specify whether to configure a proxy. If the parameter is set to true , you must configure a proxy. If the parameter is set to false, null can be used. proxy: 'http://x.x.x.x:xxxx', // Specify a proxy endpoint. Replace x.x.x.x:xxxx with the IP address and port number of the proxy. timeout: 10000, // Specify a timeout period.
```

Apsara Stack SDKs

#### 1.3.6 HTTP requests

##### 1.3.6.1 Overview

This topic describes how to call Apsara Stack APIs registered with ASAPI by sending HTTP requests. We recommend that you use SDKs to call API operations instead of using HTTP requests. Currently, ASAPI provides SDKs for Node.js, Python, and Java, which save you from the signing process. If you use an SDK to initiate requests, you can skip this topic. The request URL consists of different parameters but has a fixed request structure. The URL contains common request parameters, your signature, and operation-specific parameters. Sample request URLs are provided for each API operation. These URLs are not encoded, which makes them easy to read. Before you initiate a request, you must encode the request URL. After the request is verified, the results are returned. Response parameters are returned if the call is successful, whereas an error message is returned if the call fails. You can troubleshoot issues based on the error message.

##### 1.3.6.2 Request structure

Apsara Stack API (ASAPI) allows you to initiate HTTP GET requests based on URLs. Each URL must contain request parameters. This topic describes the syntax of HTTP GET requests and provides the endpoint of ASAPI. Sample requests GetOrganizationList is used in the following unencoded URL request:

```
https://public.asapi.aliyuns.com/asapi/v3?Action=GetOrganizationList&Product=ascm&Version=2 019-05-10&Id=<Organization ID>&<Common request parameters>
```

`https` specifies the protocol that is used to send the request. `public.asapi.aliyuns.com/asapi/v3` specifies the endpoint of ASAPI. `Action=GetOrganizationList Product=ascm Version=2019-05-10` specifies the API operation. `Id` specifies the ID of the organization. For more information, see the "Obtain an organization ID" section of the Obtain common header parameters topic. `<Common request parameters>` specifies the common parameters in the system. For more information, see Common parameters. Protocols ASAPI supports only HTTPS. Endpoints Apsara Stack SDKs For more information about how to obtain the endpoint of ASAPI, see Generate an endpoint for ASAPI. You must use the `Action, Product, and Version` parameters to specify an API operation. For example, you can set `Action to GetOrganizationList, Product to ascm, and Version to 2019-05-10` . You must also specify other operation-specific parameters and common request parameters. For more information, see relevant API operations and Common parameters.

##### 1.3.6.3 Request signatures

This topic describes how to sign HTTP API requests. Apsara Stack uses the request signature to verify the identity of the requester. Specifically, Apsara Stack uses an AccessKey pair to perform symmetric encryption and verify the identity of the requester. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey pair is issued to each user or organization in the Apsara Uni-manager Management Console. The AccessKey ID is used to verify the identities of users, and the AccessKey secret is used to encrypt and verify signature strings. You must store the AccessKey secret in a secure location. Step 1: Create a canonicalized query string
1. Sort the request parameters in alphabetical order, including all common and operation-specific
parameters except for `Signature` . If you use the GET method to send a request, the request parameters are included as part of the request URL. The parameters follow the question mark (?) and are connected by ampersands (&) in the URL.
2. Encode the names and values of the request parameters in UTF-8 based on RFC 3986.
Letters, digits, hyphens ( `-` ), underscores ( `_` ), and periods ( `.` ) do not need to be encoded. Other characters must be percent-encoded in the %XY format. `XY` represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks ( `"` ) are encoded as %22 . Extended UTF-8 characters are encoded in the %XY%ZA… format. Spaces must be encoded as %20 . Do not encode spaces as plus signs ( `+` ). Apsara Stack SDKs The preceding encoding method is similar to but slightly different from the `application/x-www-form-urlencoded` MIME-type encoding algorithm. If you use `java.net.URLEncoder` in the Java standard library, use `percentEncode` to encode request parameters and their values. In the encoded query string, replace plus signs ( `+` ) with %20 , asterisks ( `*` ) with %2A , and %7E with tildes ( ~ ). This way, you can obtain an encoded string that matches the preceding encoding rules.

```java
private static final String ENCODING = "UTF-8"; private static String percentEncode(String value) throws UnsupportedEncodingException
```

`{`

```
    return value != null ? URLEncoder.encode(value, ENCODING).replace("+", "%20").rep
lace("*", "%2A").replace("%7E", "~") : null;
```

`}`
3. Use equal signs ( `=` ) to connect the name and value of an encoded parameter.
4. Use ampersands ( `&` ) to connect the encoded request parameters. These parameters must be
arranged in the same order as those in Step 1. Then, a canonicalized query string that follows the request structure is obtained. For more information, see Request structure. Step 2: Create a string-to-sign
1. Create a string-to-sign ( `StringToSign` ). You can also use `percentEncode` to encode the
canonicalized query string that is generated in Step 1. When you create a string-to-sign, take note of the following rules:

```
StringToSign=
    HTTPMethod + "&" + //HTTPMethod: the HTTP method that is used to send the request,
such as GET.
    percentEncode("/") + "&" + //percentEncode("/"): Encode the forward slash (/) in UT
F-8 as %2F.
    percentEncode(CanonicalizedQueryString) // Encode the canonicalized query string cr
eated in Step 1.
```

2. Calculate the HMAC-SHA1 or HMAC-256 value of `StringToSign` based on RFC 2104. In this
example, the Java Base64 encoding method is used.

```
String signature = Base64.getEncoder().encodeToString(signData);
```

When you calculate the signature, the key value specified by RFC 2104 is your `AccessKey secret` plus an ampersand (&), which has an ASCII value of 38. For more information, see Obtain an AccessKey pair. Apsara Stack SDKs
3. Encode the `Signature` parameter based on RFC 3986 and add the parameter to the
canonicalized query string. Example 1: Concat enat e paramet ers `GetOrganizationList` is used in this example to query regions. For example, `AccessKeyID` is set to testid and `AccessKeySecret` is set to testsecret. Perform the following operations:
1. Construct a canonicalized query string.

```
https://public.asapi.aliyuns.com/asapi/v3/?AccessKeyId=testid&Action=GetOrganizationLis t&Format=JSON&Id=1&Product=ascm&RegionId=cn-region-test&SignatureMethod=HMAC-SHA1&Signa tureNonce=43967c6e-e3ad-44fa-b06b-fcf3db5f39d2&SignatureVersion=1.0&Timestamp=2020-09-1 5T08%3A50%3A40Z&Version=2019-05-10
```

2. Create a string-to-sign ( `StringToSign` ).

```
GET&%2F&AccessKeyId%3Dtestid%26Action%3DGetOrganizationList%26Format%3DJSON%26Id%3D1%26 Product%3Dascm%26RegionId%3Dcn-region-test%26SignatureMethod%3DHMAC-SHA1%26SignatureNon ce%3D43967c6e-e3ad-44fa-b06b-fcf3db5f39d2%26SignatureVersion%3D1.0%26Timestamp%3D2020-0 9-15T08%253A50%253A40Z%26Version%3D2019-05-10
```

3. Calculate the signature.
Calculate the signature. If `AccessKeySecret` is set to testsecret, `testsecret&` is used as the key value to calculate the signature. The calculated signature is `OLeaidS1JvxuMvnyHOwuJ+uX5qY=` . In this example, the Java Base64 encoding method is used.

```
 String signature = Base64.getEncoder().encodeToString(signData);  Encode
```

`Signature=hvqv9Ll5RE6kQ4YsQXFAf9VuRIY=` based on RFC 3986 and add it to the canonicalized query string.

```
https://public.asapi.aliyuns.com/asapi/v3/?AccessKeyId=testid&Action=GetOrganizationLis t&Format=JSON&Id=1&Product=ascm&RegionId=cn-region-test&SignatureMethod=HMAC-SHA1&Signa tureNonce=43967c6e-e3ad-44fa-b06b-fcf3db5f39d2&SignatureVersion=1.0&Timestamp=2020-09-1 5T08%3A50%3A40Z&Version=2019-05-10
```

The new URL allows you to send an HTTP request from a browser or a tool such as cURL and Wget to call the `DescribeRegions` operation, which is used to query Alibaba Cloud regions. Example 2: Use t he st andard library of t he programming language `GetOrganizationList` is used in this example to query regions. For example, `AccessKeyID` is set to testid, `AccessKeySecret` is set to testsecret, and all request parameters are stored in a Java `Map<String, String>` object.
1. Predefine the encoding method.
Apsara Stack SDKs

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
3. Create a query string.

```
final String HTTP_METHOD = "GET"; Map parameters = new HashMap(); // Configure request parameters. parameters.put("Product", "ascm"); parameters.put("Action", "GetOrganizationList"); parameters.put("Version", "2019-05-10"); parameters.put("AccessKeyId", "testid"); parameters.put("RegionId", "cn-region-test"); parameters.put("Timestamp", formatIso8601Date(new Date())); parameters.put("SignatureMethod", "HMAC-SHA1"); parameters.put("SignatureVersion", "1.0"); parameters.put("SignatureNonce", UUID.randomUUID().toString()); parameters.put("Format", "JSON"); parameters.put("Id", "1"); // Sort the request parameters. String[] sortedKeys = parameters.keySet().toArray(new String[]{}); Arrays.sort(sortedKeys); final String SEPARATOR = "&"; // Create a string-to-sign. StringBuilder stringToSign = new StringBuilder(); stringToSign.append(HTTP_METHOD).append(SEPARATOR); stringToSign.append(percentEncode("/")).append(SEPARATOR); StringBuilder canonicalizedQueryString = new StringBuilder(); for(String key : sortedKeys) {
    // Encode the key and the value.
    canonicalizedQueryString.append("&")
    .append(percentEncode(key)).append("=")
    .append(percentEncode(parameters.get(key)));
```

`}`

```
// Encode the canonicalized query string. stringToSign.append(percentEncode( canonicalizedQueryString.toString().substring(1)));
```

Apsara Stack SDKs
4. Calculate the signature. If `AccessKeySecret` is set to testsecret, `testsecret&` is used as the
key value to calculate the signature. The calculated signature is

```
 OLeaidS1JvxuMvnyHOwuJ%2BuX5qY%3D .
// The following sample code shows how to calculate the signature: final String ALGORITHM = "HmacSHA1"; final String ENCODING = "UTF-8"; key = "testsecret&"; Mac mac = Mac.getInstance(ALGORITHM); mac.init(new SecretKeySpec(key.getBytes(ENCODING), ALGORITHM)); byte[] signData = mac.doFinal(stringToSign.getBytes(ENCODING)); String signature = Base64.getEncoder().encodeToString(signData);
```

Encode the Signature parameter based on RFC 3986 and add the result to the canonicalized query string. The following URL is obtained:

```
https://public.asapi.aliyuns.com/asapi/v3/?AccessKeyId=testid&Action=GetOrganizationLis t&Format=JSON&Id=1&Product=ascm&RegionId=cn-region-test&SignatureMethod=HMAC-SHA1&Signa tureNonce=43967c6e-e3ad-44fa-b06b-fcf3db5f39d2&SignatureVersion=1.0&Timestamp=2020-09-1 5T08%3A50%3A40Z&Version=2019-05-10
```

5. Use a browser or a tool such as cURL or Wget to send an HTTP request.

##### 1.3.6.4 Responses

Responses are returned only in the JSON format. If a return code is greater than or equal to 200 and less than 300, a success response is returned. Otherwise, an error response is returned. Sample success responses If a request is successful, the request ID and operation-specific parameter values are returned. Apsara Stack SDKs `{`

```json
   "successResponse":true,
  "eagleEyeTraceId":"xxxxxxxxxxxxxx",
  "asapiSuccess":true,
  "code":"200",
  "cost":12,
  "asapiRequestId":"xxxxxxxxxxxxxx",
  "data":[
```

`{`

```json
      "muserId":"aliyuntest",
      "internal":false,
      "level":"0",
      "supportRegions":"cn-*",
      "personNum":100,
      "mtime":1553247962000,
      "uuid":"1",
      "parentId":0,
      "supportRegionList":[
        "cn-*"
```

`],`

```json
      "name":"root",
      "alias":"root",
      "ctime":1553247962000,
      "id":1,
      "resourceGroupNum":100,
      "cuserId":"aliyuntest"
```

`}` `],`

```json
  "requestId":"xxxxxxxxxxxxxx",
  "success":true,
  "message":"success"
```

`}` Sample error responses If a request fails, the following information is returned: `{`

```json
    "asapi.server.api.notfound",// The error code.
    "eagleEyeTraceId": "xxx-xxx-xxx-xxx", // The trace ID provided by EagleEye.
    "asapiSuccess": false, // Indicates whether the request is successful.
    "hostId": "xxxx", // The ID of the host.
    "message": "Failed to ....", // The message returned.
    "asapiErrorMessage": "Failed to ....", // The error message provided by ASAPI.
    "asapiErrorCode": "asapi.server.api.notfound" // The error code provided by ASAPI.
```

`}`

## 2 API reference

### 2.1 Instance management

#### 2.1.1 CreateDBInstance

Creates an ApsaraDB RDS instance. For more information about the instance types of ApsaraDB RDS instances, see Inst ance t ypes in ApsaraDB RDS Product Int roduct ion. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateDBInstance | The operation that you want to perform. Set the value to Creat eDBInst ance. |
| DBInstanceClass | String | Yes | rds.mysql.s1.sma ll | The instance type of the instance. For more information, see Inst ance t ypes in ApsaraDB RDS Product Int roduct ion. You can call the DescribeAvailableResource operation to query the available instance types in a region. |
| DBInstanceNetTy pe | String | Yes | Internet | The network connection type of the instance. Valid values: Int ernet : Internet Int ranet : internal network |
| DBInstanceStorag e | Integer | Yes | 20 | The storage capacity of the instance. Unit: GB. The storage capacity increases in increments of 5 GB. For more information, see Inst ance t ypes in ApsaraDB RDS Product Int roduct ion. You can also call the DescribeAvailableResource operation to query the storage capacity range that is available for a specific instance type in a region. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Engine | String | Yes | MySQL | The database engine of the instance. Valid values: MySQL SQLServer Post greSQL POLARDB |
| EngineVersion | String | Yes | 5.6 | The version of the database engine. Valid values when Engine is set to MySQL: 5.5, 5.6, 5.7, and 8.0 Valid values when Engine is set to SQL Server: 2008r2, 08r2 ent ha, _ _ 2012, 2012 ent ha, _ _ 2012 st d ha, 2012 web, _ _ _ 2014 st d ha, 2016 ent ha, _ _ _ _ 2016 st d ha, 2016 web, _ _ _ 2017 st d ha, 2017 ent , _ _ _ 2019 st d ha, and 2019 ent _ _ _ Valid values when Engine is set to PostgreSQL: 9.4, 10.0, 11.0, 12.0, and 13.0 Set the value to 11 when Engine is set to POLARDB. |
| PayType | String | Yes | Postpaid | The billing method of the instance. Set the value to Post paid. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SecurityIPList | String | Yes | 10.23.12.27/24 | The IP address whitelist of the instance. If the IP address whitelist contains more than one entry, separate the entries with commas (,). Each entry must be unique. The IP address whitelist can contain up to 1,000 entries. The entries in the IP address whitelist must be in one of the following formats: IP address. Example: 10.23.12.24. CIDR block. Example: 10.23.12.24/24. In this example, 24 indicates that the prefix of the CIDR block is 24 bits in length. You can replace 24 with a value within the range of 1 to 32. |
| DBInstanceStorag eType | String | No | cloud ssd _ | The storage type of the instance. Valid values: local ssd: local SSD. This is the _ recommended storage type. cloud ssd: standard SSD. _ |
| SystemDBCharset | String | No | gbk | An invalid parameter. |
| DBInstanceDescri ption | String | No | Test database | The name of the instance. The name must be 2 to 255 characters in length and can contain letters, digits, underscores ( ), and hyphens (-). _ Not e The name cannot start with http:// or https://. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ZoneId | String | No | cn-hangzhou-b | The zone ID of the primary instance. Not e If you specify a virtual private cloud (VPC) and a vSwitch, you must specify the ZoneId parameter. If you specify the RDS High-availability Edition, you must also specify the ZoneIdSlave1 parameter, which specifies whether to use the single-zone deployment method or the multi-zone deployment method. If you specify the RDS Enterprise Edition, you must also specify the ZoneIdSlave1 and ZoneIdSlave2 parameters, which specify whether to use the single- zone deployment method or the multi-zone deployment method. |
| InstanceNetwork Type | String | No | Classic | The network type of the instance. Default value: Classic. Valid values: VPC Classic |
| ConnectionMode | String | No | Standard | The connection mode of the instance. Valid values: St andard: standard mode Saf e: database proxy mode Not e SQL Server 2012, SQL Server 2016, and SQL Server 2017 support only the standard mode. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VPCId | String | No | vpc-xxxxxxxxxxxx | The ID of the VPC. Not e If you set the Inst anceNet workT ype parameter to VPC, you must specify the VPCId parameter. |
| VSwitchId | String | No | vsw-xxxxxxxxxxx | The ID of the vSwitch. If you specify more than one vSwitch ID, separate the vSwitch IDs with commas (,). Not e If you set the Inst anceNet workT ype parameter to VPC, you must specify the VSwitchId parameter. |
| PrivateIpAddress | String | No | 172.16.201.69 | The internal IP address of the instance. The internal IP address must be within the CIDR block that is supported by the specified vSwitch. The system automatically assigns an internal IP address to the instance based on the VPCId and VSwit chId values. |
| UsedTime | String | No | None | An invalid parameter. |
| Period | String | No | None | An invalid parameter. |
| ResourceGroupId | String | No | rg- acfmyxxxxxxxxxx | The ID of the resource group. |
| TunnelId | String | No | None | An invalid parameter. |
| Category | String | No | HighAvailability | The RDS edition of the instance. Valid values: Basic: Basic Edition HighAvailabilit y: High-availability Edition AlwaysOn: Cluster Edition Finance: Enterprise Edition |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ZoneIdSlave1 | String | No | cn-hangzhou-c | The zone ID of the secondary instance. If you set the ZoneIdSlave1 parameter to the same value as the ZoneId parameter, the single-zone deployment method is used. If you set the ZoneIdSlave1 parameter to a different value from the ZoneId parameter, the multi-zone deployment method is used. |
| ZoneIdSlave2 | String | No | cn-hangzhou-d | The zone ID of the logger instance. If you set the ZoneIdSlave2 parameter to the same value as the ZoneId parameter, the single-zone deployment method is used. If you set the ZoneIdSlave2 parameter to a different value from the ZoneId parameter, the multi-zone deployment method is used. |
| EncryptionKey | String | No | 0d24xxxx-da7b- 4786-b981- 9a164dxxxxxx | The ID of the key that is used to encrypt data on standard SSDs in the region of the instance. You can obtain the ID of the key from the Key Management Service (KMS) console. You can also create a key. Not e If you specify the EncryptionKey parameter, disk encryption is automatically enabled. In this case, you must also specify the RoleARN parameter. Disk encryption cannot be disabled after it is enabled. |
| RoleARN | String | No | acs:ram::1406xx xxxx:role/aliyunr dsinstanceencryp tiondefaultrole | The Alibaba Cloud Resource Name (ARN) that is provided by your Alibaba Cloud account for Resource Access Management (RAM) users. RAM users can use the ARN to connect from ApsaraDB RDS to KMS. |
| DedicatedHostGr oupId | String | No | None | An invalid parameter. |
| TargetDedicated HostIdForMaster | String | No | None | An invalid parameter. |

| psaraDB for RDS |   |   |   | Developer Guide·API referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TargetDedicated HostIdForSlave | String | No | None | An invalid parameter. |
| TargetDedicated HostIdForLog | String | No | None | An invalid parameter. |
| MultiAVZExParam | String | No | None | An invalid parameter. |
| License mode _ | String | No | None | An invalid parameter. |
| BucketUrlImage | String | No | None | An invalid parameter. |
| BucketUrlPsuPatc h | String | No | None | An invalid parameter. |
| BucketUrlOpatchT ool | String | No | None | An invalid parameter. |
| DBName | String | No | None | An invalid parameter. |
| Port | String | No | None | An invalid parameter. |
| CharacterSetNam e | String | No | None | An invalid parameter. |
| DBNationalCharac terSet | String | No | None | An invalid parameter. |
| BackupRetentionP eriod | String | No | None | An invalid parameter. |
| SwitchMode | String | No | None | An invalid parameter. |
| SyncMode | String | No | None | An invalid parameter. |
| TdeStatus | Integer | No | 0 | An invalid parameter. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | rm- uf6wjk5xxxxxxxxxx | The ID of the instance. |

|   | Developer Guide·AP | I reference |   | ApsaraDB for RD | S |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| OrderId | String | 1007893702xxxxx | The ID of the order. |
| ConnectionStrin g | String | rm- uf6wjk5xxxxxxx.mys ql.rds.aliyuncs.com | The endpoint of the instance. Not e The DBInst anceNet T ype parameter indicates whether the endpoint is an internal endpoint or a public endpoint. |
| Port | String | 3306 | The port that is used to connect to the instance. Not e The DBInst anceNet T ype parameter indicates whether the port is an internal port or a public port. |
| RequestId | String | 1E43AAE0-BEE8- 43DA-860D- EAF2AA0724DC | The ID of the request. |

In the new version of SDK, the default timeout period on the client side is different from the default timeout period on the instance. If you use the new version of SDK to call this operation, a timeout error may be reported even if the operation is successfully called. To prevent this issue, you can set the ReadTimeout parameter to 20000 before you call this operation. Examples Sample requests

```
http(s)://rds.example.com/?Action=CreateDBInstance &RegionId=cn-hangzhou &Engine=MySQL &EngineVersion=5.6 &DBInstanceClass=rds.mysql.s1.small &DBInstanceStorage=20 &DBInstanceNetType=Internet &PayType=Postpaid &SecurityIPList=10.23.12.27/24 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateDBInstanceResponse>
      <OrderId>1007893702xxxxx</OrderId>
      <ConnectionString>rm-uf6wjk5xxxxxxx.mysql.rds.aliyuncs.com</ConnectionString>
      <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
      <Port>3306</Port>
      <RequestId>1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC</RequestId>
</CreateDBInstanceResponse>
```

`JSON` format `{`

```json
    "OrderId": "1007893702xxxxx",
    "ConnectionString": "rm-uf6wjk5xxxxxxx.mysql.rds.aliyuncs.com",
    "DBInstanceId": "rm-uf6wjk5xxxxxxx",
    "Port": "3306",
    "RequestId": "1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC"
```

`}` Error codes

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidZoneId.NotSu pported | The Specified vpc Zone not supported. | The error message returned because the specified zone does not allow you to create an instance in a VPC. Specify a different zone and try again. |
| 400 | InvalidZone.NotSup ported | The Specified Zone not supported. | The error message returned because the specified region is invalid. |

#### 2.1.2 DeleteDBInstance

Releases an ApsaraDB RDS instance. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The read/write splitting feature is disabled for the instance. The instance is a primary, read-only, disaster recovery, or temporary instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteDBInstance | The operation that you want to perform. Set the value to Delet eDBInst ance. |
| DBInstanceId | String | Yes | rm- uf6wjk5********** | The ID of the instance. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCz********** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DeleteDBInstance &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteDBInstanceResponse>
  <RequestId>65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
  <RegionId>ap-southeast-1</RegionId>
</DeleteDBInstanceResponse>
```

`JSON` format `{`

```json
  "RequestId":"65BDA532-28AF-4122-AA39-B382721EEE64",
  "RegionId":"ap-southeast-1"
```

`}`

#### 2.1.3 RestartDBInstance

Restarts an ApsaraDB RDS instance. If a large number of transactions need to be submitted or rolled back, the restart process may be delayed for a minute. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance does not have ongoing backup tasks. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RestartDBInstanc e | The operation that you want to perform. Set the value to Rest art DBInst ance. |
| DBInstanceId | String | Yes | rm-uf6wjk5xxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | The ID of the request. |

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

Queries the details of one or more ApsaraDB RDS instances. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstan ceAttribute | The operation that you want to perform. Set the value to DescribeDBInst anceAt t ribut e. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxxxx x | The ID of the instance. You can specify up to 30 instance IDs in a single request. Separate multiple instance IDs with commas (,). |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Expired | String | No | False | Specifies whether the instance has expired. Valid values: T rue: The instances are expired. False: The instances are not expired. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | Array of DBInstanceAttri bute |   | Details of the attributes of the instances returned. |
| DBInstanceAttri bute |   |   |   |
| DBInstanceId | String | rm- uf6wjk5xxxxxxxxxx | The ID of the instance. |
| PayType | String | Postpaid | The billing method of the instance. Valid values: Post paid: pay-as-you-go Prepaid: subscription |
| DBInstanceType | String | Primary | The role of the instance. Valid values: Primary: primary instance Readonly: read-only instance Guard: disaster recovery instance T emp: temporary instance |
| Category | String | Basic | The RDS edition of the instance. Valid values: Basic: Basic Edition HighAvailabilit y: High-availability Edition AlwaysOn: Cluster Edition Finance: Enterprise Edition |
| InstanceNetwor kType | String | Classic | The network type of the instance. Valid values: Classic VPC |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RegionId | String | cn-hangzhou | The ID of the region. |
| ZoneId | String | cn-hangzhou-a | The ID of the zone. |
| ConnectionStrin g | String | rm- uf6wjk5xxxxxxxxxx. mysql.rds.aliyuncs.c om | The internal endpoint of the instance. |
| Port | String | 3306 | The internal port that is used to connect to the instance. |
| Engine | String | MySQL | The database engine of the instance. |
| EngineVersion | String | 5.5 | The version of the database engine. |
| DBInstanceClas sType | String | s | The instance family of the instance. Valid values: s: shared instance family x: general-purpose instance family d: dedicated instance family h: dedicated host instance family |
| DBInstanceClas s | String | rds.mys2.small | The instance type of the instance. For more information, see Inst ance t ypes in ApsaraDB RDS Product Int roduct ion. |
| DBInstanceMem ory | Long | 4096 | The memory capacity of the instance. Unit: MB. |
| DBInstanceStor age | Integer | 10 | The storage capacity of the instance. Unit: GB. |
| DBInstanceNetT ype | String | Internet | The network connection type of the instance. Valid values: Int ernet : Internet Int ranet : internal network |
| DBInstanceStat us | String | Running | The state of the instance. For more information, see Instance states. |

| psaraDB for RDS |   |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceDesc ription | String | Test database | The description of the instance. |
| LockMode | String | Unlock | The lock state of the instance. Valid values: Unlock: The instance is not locked. ManualLock: The instance is manually locked. LockByExpirat ion: The instance is automatically locked after it expires. LockByRest orat ion: The instance is automatically locked before it is rolled back. LockByDiskQuot a: The instance is automatically locked after the storage space is exhausted. LockReadInst anceByDiskQuot a: The instance is a read-only instance that is automatically locked after the storage space is exhausted. |
| LockReason | String | instance expired _ | The reason why the instance is locked. |
| DBMaxQuantity | Integer | 200 | The maximum number of databases that can be created on an instance. |
| AccountMaxQu antity | Integer | 50 | The maximum number of accounts that can be created on an instance. |
| CreationTime | String | 2011-05- 30T12:11:04Z | The time when the instance was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| ExpireTime | String | 2019-03- 27T16:00:00Z | The expiration time of the instance. The time follows the ISO 8601 standard in the yyyy- MM-ddTHH:mm:ssZ format. The time is displayed in UTC. Not e Pay-as-you-go instances never expire. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| MaintainTime | String | 00:00Z-02:00Z | The maintenance window of the instance. The time is displayed in UTC. In the ApsaraDB RDS console, the maintenance window is displayed in UTC+8. |
| AvailabilityValu e | String | 100.0% | The availability of the instance. Unit: %. |
| MaxIOPS | Integer | 150 | The maximum number of I/O requests processed by the instance per second. |
| MaxConnection s | Integer | 60 | The maximum number of concurrent connections allowed by the instance. |
| MasterInstanceI d | String | rm- uf6wjk5xxxxxxxxxx | The ID of the primary instance. If this parameter is not returned, the instance is a primary instance. |
| IncrementSourc eDBInstanceId | String | rm- uf6wjk5xxxxxxxxxx | The ID of the instance from which incremental data comes. The incremental data of a disaster recovery instance or read- only instance comes from its primary instance. If this parameter is not returned, the instance is a primary instance. |
| GuardDBInstanc eId | String | rm- uf64zsuxxxxxxxxxx | The ID of the disaster recovery instance attached to the primary instance. |
| TempDBInstanc eId | String | rm- uf64zsuxxxxxxxxxx | The ID of the temporary instance attached to the primary instance. |
| ReadOnlyDBInst anceIds | Array of ReadOnlyDBInst anceId |   | The IDs of the read-only instances attached to the primary instance. |
| ReadOnlyDBInst anceId |   |   |   |
| DBInstanceId | String | rm-bpxxxxxxxxx | The ID of the read-only instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AdvancedFeatu res | String | LinkedServer | The advanced features that are separated by commas (,). This parameter is applicable only to instances that run SQL Server. Valid values: LinkedServer Dist ribut eT ransact ion |
| AutoUpgradeMi norVersion | String | Auto | The method that is used to update the minor engine version of the instance. Valid values: Auto: automatic update. Manual: manual update. ApsaraDB RDS automatically updates the current minor engine version of the instance only when the current minor engine version is phased out. |
| Collation | String | Chinese PRC CI AS _ _ _ | The character set collation of the instance. |
| ConnectionMod e | String | Standard | The connection mode of the instance. Valid values: St andard: standard mode Saf e: database proxy mode |
| ConsoleVersion | String | 2 | The type of the proxy that is enabled on the instance. Valid values: 1: shared proxy 2: dedicated proxy Not e We recommend that you do not use this parameter. Use the ProxyT ype parameter instead. |
| CurrentKernelV ersion | String | rds 20181010 _ | The minor engine version of the instance. |
| DBInstanceStor ageType | String | local ssd _ | The storage type of the instance. Valid values: local ssd/ephemeral ssd: local SSD _ _ cloud ssd: standard SSD _ |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DispenseMode | String | None | An invalid parameter. |
| EncryptionKey | String | None | An invalid parameter. |
| EncryptionKey | String | None | An invalid parameter. |
| Extra | Struct |   | An invalid parameter. |
| ActiveReplicaDB InstanceID | String | None | An invalid parameter. |
| DBInstanceId | List | None | An invalid parameter. |
| ReplicaGroupID | String | None | An invalid parameter. |
| ReplicaGroupSt atus | String | None | An invalid parameter. |
| LatestKernelVer sion | String | rds 20201031 _ | The latest minor engine version that is supported by the instance. |
| MasterZone | String | 5454284 | The ID of the primary zone. |
| ProxyType | Integer | 1 | The type of the proxy that is supported by the instance. Valid values: 0: The instance does not support database proxies. 1: The instance supports shared proxies, which are known as the multi-tenant mode. 2: The instance supports dedicated proxies, which are known as the single- tenant mode. |
| ReadonlyInstan ceSQLDelayedTi me | String | 30 | The latency of data replication to the read- only instances. The read-only instances replicate data from the primary instance at the latency that is specified by the ReadonlyInst anceSQLDelayedT ime parameter. Unit: seconds. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ResourceGroupI d | String | rg-acfmyxxxxxxxxxx | The ID of the resource group. |
| SecurityIPMode | String | normal | The whitelist mode of the instance. Valid values: normal: standard whitelist mode saf et y: enhanced whitelist mode |
| SlaveConnectio nString | String | None | An invalid parameter. |
| SlaveZones | Array of SlaveZone |   | Details of secondary zones. |
| SlaveZone |   |   |   |
| ZoneId | String | cn-hangzhou-a | The zone ID of the instance. |
| TimeZone | String | Central Standard Time | The time zone of the instance. |
| VSwitchId | String | vsw-xxxxxx | The ID of the vSwitch. |
| VpcCloudInstan ceId | String | vpc-23rsxdfxxxxxxx | The ID of the instance. This parameter is returned only when the instance resides in a virtual private cloud (VPC). |
| VpcId | String | vpc-xxxxxxxxx | The ID of the VPC. |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeDBInstanceAttribute &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeDBInstanceAttributeResponse>
  <RequestId>BD3A30D8-32E7-40CF-AAEA-6BFD4E3DC55E</RequestId>
```

`It`

```xml
  <Items>
        <DBInstanceAttribute>
              <DBInstanceMemory>8192</DBInstanceMemory>
              <ResourceGroupId>rg-acfmyxxxxxxxxxx</ResourceGroupId>
              <Port>3306</Port>
              <MasterZone>cn-hangzhou-h</MasterZone>
              <LatestKernelVersion>rds_20201031</LatestKernelVersion>
              <DBInstanceType>Primary</DBInstanceType>
              <ConsoleVersion>2</ConsoleVersion>
              <InstanceNetworkType>VPC</InstanceNetworkType>
              <DBInstanceClassType>x</DBInstanceClassType>
              <DBInstanceId>rm-uf6wjk5xxxxxxxxxx</DBInstanceId>
              <AutoUpgradeMinorVersion>Auto</AutoUpgradeMinorVersion>
              <DBInstanceStorage>150</DBInstanceStorage>
              <AvailabilityValue>100.0%</AvailabilityValue>
              <Engine>MySQL</Engine>
              <DBInstanceDescription>test1</DBInstanceDescription>
              <IPType>IPv4</IPType>
              <EngineVersion>8.0</EngineVersion>
              <DBInstanceStatus>Running</DBInstanceStatus>
              <MaxConnections>2000</MaxConnections>
              <DBInstanceClass>rds.mysql.s3.large</DBInstanceClass>
              <AccountMaxQuantity>99999</AccountMaxQuantity>
              <VSwitchId>vsw-xxxxxx</VSwitchId>
              <PayType>Prepaid</PayType>
              <LockMode>Unlock</LockMode>
              <GuardDBInstanceId>rm-uf64zsuxxxxxxxxxx</GuardDBInstanceId>
              <SupportCreateSuperAccount>No</SupportCreateSuperAccount>
              <InsId>1</InsId>
              <VpcId>vpc-xxxxxxxxx</VpcId>
              <CurrentKernelVersion>rds_20200831</CurrentKernelVersion>
              <TempUpgradeTimeStart>2021-01-10 00:00:00</TempUpgradeTimeStart>
              <TempUpgradeTimeEnd>2021-06-18 00:00:00</TempUpgradeTimeEnd>
              <CreationTime>2020-06-17T09:03:57Z</CreationTime>
              <ConnectionMode>Standard</ConnectionMode>
              <VpcCloudInstanceId>vpc-23rsxdfxxxxxxx</VpcCloudInstanceId>
              <ProxyType>2</ProxyType>
              <ConnectionString>rm-uf6wjk5xxxxxxxxxx.mysql.rds.aliyuncs.com</ConnectionStri
ng>
              <ExpireTime>2021-06-17T16:00:00Z</ExpireTime>
              <DBMaxQuantity>99999</DBMaxQuantity>
              <Category>HighAvailability</Category>
              <DBInstanceNetType>Intranet</DBInstanceNetType>
              <SuperPermissionMode></SuperPermissionMode>
              <DedicatedHostGroupId></DedicatedHostGroupId>
              <DBInstanceCPU>4</DBInstanceCPU>
              <GuardDBInstanceName>rm-m5xxxxx</GuardDBInstanceName>
              <SecurityIPList>42.xx.xx.xx</SecurityIPList>
              <OriginConfiguration></OriginConfiguration>
              <ReadOnlyDBInstanceIds>
        </ReadOnlyDBInstanceIds>
              <SecurityIPMode>normal</SecurityIPMode>
              <MaintainTime>23:00Z-00:00Z</MaintainTime>
              <DispenseMode>MultiAVZDispenseMode</DispenseMode>
<ZoneId>cn-hangzhou-h</ZoneId>
```

```xml
              <ZoneId>cn-hangzhou-h</ZoneId>
              <DBInstanceStorageType>local_ssd</DBInstanceStorageType>
              <AccountType>Mix</AccountType>
              <MaxIOPS>5000</MaxIOPS>
              <SupportUpgradeAccountType>No</SupportUpgradeAccountType>
              <SlaveZones>
                    <SlaveZone>
                          <ZoneId>cn-hangzhou-h</ZoneId>
                    </SlaveZone>
              </SlaveZones>
              <Extra>
                    <DBInstanceIds>
            </DBInstanceIds>
              </Extra>
              <CanTempUpgrade>true</CanTempUpgrade>
              <RegionId>cn-hangzhou</RegionId>
        </DBInstanceAttribute>
  </Items>
</DescribeDBInstanceAttributeResponse>
```

`JSON` format `{`

```json
    "RequestId": "BD3A30D8-32E7-40CF-AAEA-6BFD4E3DC55E",
    "Items": {
        "DBInstanceAttribute": [
```

`{`

```json
                "DBInstanceMemory": 8192,
                "ResourceGroupId": "rg-acfmyxxxxxxxxxx",
                "Port": "3306",
                "MasterZone": "cn-hangzhou-h",
                "LatestKernelVersion": "rds_20201031",
                "DBInstanceType": "Primary",
                "ConsoleVersion": "2",
                "InstanceNetworkType": "VPC",
                "DBInstanceClassType": "x",
                "DBInstanceId": "rm-uf6wjk5xxxxxxxxxx",
                "AutoUpgradeMinorVersion": "Auto",
                "DBInstanceStorage": 150,
                "AvailabilityValue": "100.0%",
                "Engine": "MySQL",
                "DBInstanceDescription": "test1",
                "IPType": "IPv4",
                "EngineVersion": "8.0",
                "DBInstanceStatus": "Running",
                "MaxConnections": 2000,
                "DBInstanceClass": "rds.mysql.s3.large",
                "AccountMaxQuantity": 99999,
                "VSwitchId": "vsw-xxxxxx",
                "PayType": "Prepaid",
                "LockMode": "Unlock",
                "GuardDBInstanceId": "rm-uf64zsuxxxxxxxxxx",
                "SupportCreateSuperAccount": "No",
                "InsId": 1,
```

```json
                "VpcId": "vpc-xxxxxxxxx",
                "CurrentKernelVersion": "rds_20200831",
                "TempUpgradeTimeStart": "2021-01-10 00:00:00",
                "TempUpgradeTimeEnd": "2021-06-18 00:00:00",
                "CreationTime": "2020-06-17T09:03:57Z",
                "ConnectionMode": "Standard",
                "VpcCloudInstanceId": "vpc-23rsxdfxxxxxxx",
                "ProxyType": 2,
                "ConnectionString": "rm-uf6wjk5xxxxxxxxxx.mysql.rds.aliyuncs.com",
                "ExpireTime": "2021-06-17T16:00:00Z",
                "DBMaxQuantity": 99999,
                "Category": "HighAvailability",
                "DBInstanceNetType": "Intranet",
                "SuperPermissionMode": "",
                "DedicatedHostGroupId": "",
                "DBInstanceCPU": "4",
                "GuardDBInstanceName": "rm-m5xxxxx",
                "SecurityIPList": "42.xx.xx.xx",
                "OriginConfiguration": "",
                "ReadOnlyDBInstanceIds": {
                    "ReadOnlyDBInstanceId": []
```

`},`

```json
                "SecurityIPMode": "normal",
                "MaintainTime": "23:00Z-00:00Z",
                "DispenseMode": "MultiAVZDispenseMode",
                "ZoneId": "cn-hangzhou-h",
                "DBInstanceStorageType": "local_ssd",
                "AccountType": "Mix",
                "MaxIOPS": 5000,
                "SupportUpgradeAccountType": "No",
                "SlaveZones": {
                    "SlaveZone": [
```

`{`

```json
                            "ZoneId": "cn-hangzhou-h"
```

`}` `]` `},`

```json
                "Extra": {
                    "DBInstanceIds": {
                        "DBInstanceId": []
```

`}` `},`

```json
                "CanTempUpgrade": true,
                "RegionId": "cn-hangzhou"
```

`}` `]` `}` `}`

#### 2.1.5 DescribeDBInstances

Queries one or more ApsaraDB RDS instances that meet the specified conditions. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstan ces | The operation that you want to perform. Set the value to DescribeDBInst ances. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| proxyId | String | No | API | The ID of the proxy mode. |
| Engine | String | No | MySQL | The database engine of the instance. Valid values: MySQL SQLServer Post greSQL PolarDB By default, this operation returns the instances that run any of the supported database engines. |
| ZoneId | String | No | cn-hangzhou-a | The ID of the zone. |
| ResourceGroupId | String | No | rg-acfmyxxxxx | The ID of the resource group. |
| DBInstanceStatus | String | No | Running | The state of the instance. For more information, see Instance states. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Expired | String | No | True | Specifies whether to query the instances that have expired. Valid values: T rue: The instances are expired. False: The instances are not expired. |
| SearchKey | String | No | rm-uf6w | The keywords that are parts of the IDs or descriptions of the instances. |
| DBInstanceId | String | No | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| DBInstanceType | String | No | Primary | The role of the instance. Valid values: Primary: primary instance Readonly: read-only instance Guard: disaster recovery instance T emp: temporary instance By default, this operation returns the instances that assume any of the supported roles. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 1 to 100. Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |
| InstanceNetwork Type | String | No | Classic | The network type of the instance. Valid values: VPC Classic By default, this operation returns the instances that reside in the classic network and virtual private clouds (VPCs). |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VpcId | String | No | vpc- uf6f7l4fg90xxxxx xxxxx | The ID of the VPC. |
| VSwitchId | String | No | vsw- uf6adz52c2pxxxx xxxxxx | The ID of the vSwitch. |
| DBInstanceClass | String | No | rds.mys2.small | The instance type of the instance. For more information, see Inst ance t ypes in ApsaraDB RDS Product Int roduct ion. |
| EngineVersion | String | No | 5.7 | The version of the database engine. |
| PayType | String | No | Postpaid | The billing method of the instance. Valid values: Post paid: pay-as-you-go Prepaid: subscription |
| ConnectionMode | String | No | Standard | The connection mode of the instance. Valid values: St andard: standard mode Saf e: database proxy mode By default, this operation returns the instances that are connected in standard mode and database proxy mode. |
| Tag.1.key | String | No | testkey1 | The first tag key. |
| Tag.2.key | String | No | testkey2 | The second tag key. |
| Tag.3.key | String | No | testkey3 | The third tag key. |
| Tag.4.key | String | No | testkey4 | The fourth tag key. |
| Tag.5.key | String | No | testkey5 | The fifth tag key. |
| Tag.1.value | String | No | testvalue1 | The value of the first tag key. |

| eveloper Guide·API r | eference |   |   | ApsaraDB for RD |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Tag.2.value | String | No | testvalue2 | The value of the second tag key. |
| Tag.3.value | String | No | testvalue3 | The value of the third tag key. |
| Tag.4.value | String | No | testvalue4 | The value of the fourth tag key. |
| Tag.5.value | String | No | testvalue5 | The value of the fifth tag key. |
| Tags | String | No | {"key1":"value1"} | The tags that are added to the instance. Each tag is a key-value pair that consists of two parts: TagKey and TagValue. You can specify a maximum of five tags in the following format for each request: {"key1":"value1","key2":"value2"...}. |
| DedicatedHostGr oupId | String | No | dhg-7a9xxxxxxxx | The ID of the dedicated cluster to which the instance belongs. |
| DedicatedHostId | String | No | i-bpxxxxxxx | The ID of the host to which the instance belongs in the specified dedicated cluster. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageRecordCou nt | Integer | 10 | The number of instances returned on the current page. |
| TotalRecordCo unt | Integer | 100 | The total number of entries returned. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| Items | Array of DBInstance |   | Details of the instances. |
| DBInstance |   |   |   |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | rm- uf6wjk5xxxxxxxxxx | The ID of the instance. |
| DBInstanceDesc ription | String | Test database | The description of the instance. |
| PayType | String | Postpaid | The billing method of the instance. Valid value: Post paid. |
| DBInstanceType | String | Primary | The role of the instance. Valid values: Primary: primary instance ReadOnly: read-only instance Guard: disaster recovery instance T emp: temporary instance |
| InstanceNetwor kType | String | Classic | The network type of the instance. Valid values: Classic VPC |
| ConnectionMod e | String | Performance | The connection mode of the instance. Valid values: St andard: standard mode Saf e: database proxy mode |
| RegionId | String | cn-hangzhou | The ID of the region. |
| ExpireTime | String | 2019-02- 27T16:00:00Z | The expiration time of the instance. The time follows the ISO 8601 standard in the yyyy- MM-ddTHH:mm:ssZ format. The time is displayed in UTC. Not e Pay-as-you-go instances never expire. |
| DBInstanceStat us | String | Running | The state of the instance. For more information, see Instance states. |
| Engine | String | MySQL | The database engine of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceNetT ype | String | Internet | The type of network connection to the instance. Valid values: Int ernet : Internet Int ranet : internal network |
| LockMode | String | Unlock | The lock status of the instance. Valid values: Unlock: The instance is not locked. ManualLock: The instance is manually locked. LockByExpirat ion: The instance is automatically locked after it expires. LockByRest orat ion: The instance is automatically locked before it is rolled back. LockByDiskQuot a: The instance is automatically locked after the storage space is exhausted. Released: The instance is released. After an instance is released, the instance cannot be unlocked. You can only restore the backup data of the instance to a new instance. This process requires a long period of time. |
| LockReason | String | instance expired _ | The reason why the instance is locked. |
| MasterInstanceI d | String | rm- uf6wjk5xxxxxxxxxx | The ID of the primary instance. If the value of this parameter is null, the instance is a primary instance. |
| GuardDBInstanc eId | String | rm- uf64zsuxxxxxxxxxx | The ID of the disaster recovery instance. This parameter is returned only when the instance is a primary instance and has a disaster recovery instance attached. |
| TempDBInstanc eId | String | rm- uf64zsuxxxxxxxxxx | The ID of the temporary instance. This parameter is returned only when the instance is a primary instance and has a temporary instance attached. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Category | String | Basic | The RDS edition of the instance. Valid values: Basic: Basic Edition HighAvailabilit y: High-availability Edition Finance: Enterprise Edition |
| CreateTime | String | 2018-11- 05T11:26:02Z | The time when the instance was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| DBInstanceClas s | String | rds.mys2.small | The instance type of the instance. For more information, see Inst ance t ypes in ApsaraDB RDS Product Int roduct ion. |
| DBInstanceStor ageType | String | ModuleList.4.Module Code | The storage type of the instance. |
| DestroyTime | String | 2018-11- 05T11:26:02Z | The time when the instance was destroyed. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| DispenseMode | String | None | The deployment method of the instance. |
| EngineVersion | String | 5.7 | The version of the database engine. |
| InsId | Integer | 0 | An invalid parameter. |
| MasterZone | String | None | An invalid parameter. |
| MutriORsignle | Boolean | true | Indicates whether the multi-zone deployment method is used for the instance. Valid values: t rue and f alse. |
| ReadOnlyDBInst anceIds | Array of ReadOnlyDBInst anceId |   | The IDs of read-only instances if the primary instance has read-only instances attached. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ReadOnlyDBInst anceId |   |   |   |
| DBInstanceId | String | rr-uf6wjk5xxxxxxx | The ID of the read-only instance. |
| ReplicateId | String | None | An invalid parameter. |
| ResourceGroupI d | String | rg-acfmyxxxxxxx | The ID of the resource group. |
| SlaveZones | Array of SlaveZone |   | The IDs of zones where the secondary instances reside. |
| SlaveZone |   |   |   |
| ZoneId | String | cn-hangzhou-h | The ID of the zone where the secondary instance resides. |
| VSwitchId | String | vsw- uf6adz52c2pxxxxxxx | The ID of the vSwitch. |
| VpcCloudInstan ceId | String | rm-uf6wjk5xxxxxxx | The ID of the instance. This parameter is returned only when the instance resides in a VPC. |
| VpcId | String | vpc- uf6f7l4fg90xxxxxxx | The ID of the VPC. |
| ZoneId | String | cn-hangzhou-a | The ID of the zone. |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeDBInstances &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeDBInstancesResponse>
  <TotalRecordCount>1</TotalRecordCount>
  <PageRecordCount>1</PageRecordCount>
  <RequestId>B4309486-26EF-47B3-ADDE-6140B4C1109D</RequestId>
  <PageNumber>1</PageNumber>
  <Items>
        <DBInstance>
              <ResourceGroupId>rg-acxxxxx</ResourceGroupId>
              <DBInstanceNetType>Intranet</DBInstanceNetType>
              <DBInstanceType>Primary</DBInstanceType>
              <MutriORsignle>false</MutriORsignle>
              <InstanceNetworkType>VPC</InstanceNetworkType>
              <DBInstanceId>rm-bpxxxxx</DBInstanceId>
              <ReadOnlyDBInstanceIds>
        </ReadOnlyDBInstanceIds>
              <LockReason></LockReason>
              <DBInstanceDescription>test</DBInstanceDescription>
              <Engine>MySQL</Engine>
              <EngineVersion>8.0</EngineVersion>
              <DBInstanceStatus>Running</DBInstanceStatus>
              <ZoneId>cn-hangzhou-h</ZoneId>
              <DBInstanceClass>rds.mysql.s3.large</DBInstanceClass>
              <CreateTime>2020-06-17T09:03:57Z</CreateTime>
              <VSwitchId>vsw-bpxxxxx</VSwitchId>
              <PayType>Prepaid</PayType>
              <LockMode>Unlock</LockMode>
              <GuardDBInstanceId>rm-m5xxxxx</GuardDBInstanceId>
              <InsId>1</InsId>
              <VpcId>vpc-bpxxxxx</VpcId>
              <VpcName>test-huadong</VpcName>
              <ConnectionMode>Standard</ConnectionMode>
              <VpcCloudInstanceId>rm-bpxxxxx-1</VpcCloudInstanceId>
              <RegionId>cn-hangzhou</RegionId>
              <ExpireTime>2021-06-17T16:00:00Z</ExpireTime>
        </DBInstance>
  </Items>
</DescribeDBInstancesResponse>
```

`JSON` format `{`

```json
    "TotalRecordCount": 1,
    "PageRecordCount": 1,
    "RequestId": "B4309486-26EF-47B3-ADDE-6140B4C1109D",
    "PageNumber": 1,
    "Items": {
        "DBInstance": [
```

`{`

```json
                "ResourceGroupId": "rg-acxxxxx",
                "DBInstanceNetType": "Intranet",
                "DBInstanceType": "Primary",
                "MutriORsignle": false,
                "InstanceNetworkType": "VPC",
                "DBInstanceId": "rm-bpxxxxx",
                "ReadOnlyDBInstanceIds": {
                    "ReadOnlyDBInstanceId": []
```

`},`

```json
                "LockReason": "",
                "DBInstanceDescription": "test",
                "Engine": "MySQL",
                "EngineVersion": "8.0",
                "DBInstanceStatus": "Running",
                "ZoneId": "cn-hangzhou-h",
                "DBInstanceClass": "rds.mysql.s3.large",
                "CreateTime": "2020-06-17T09:03:57Z",
                "VSwitchId": "vsw-bpxxxxx",
                "PayType": "Prepaid",
                "LockMode": "Unlock",
                "GuardDBInstanceId": "rm-m5xxxxx",
                "InsId": 1,
                "VpcId": "vpc-bpxxxxx",
                "VpcName": "test-huadong",
                "ConnectionMode": "Standard",
                "VpcCloudInstanceId": "rm-bpxxxxx-1",
                "RegionId": "cn-hangzhou",
                "ExpireTime": "2021-06-17T16:00:00Z"
```

`}` `]` `}` `}` Error codes

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidDBInstanceTy pe.ValueNotSupport | The specified parameter"DBInstanceType" is not valid. | The error message returned because the specified instance type is invalid. Specify a valid instance type. |

#### 2.1.6 ModifyDBInstanceSpec

Changes the instance type or storage capacity of an ApsaraDB RDS instance. This operation is supported for primary and read-only instances. This operation is not supported for disaster recovery or temporary instances. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance does not have ongoing backup tasks. At least one of the DBInstanceClass and DBInstanceStorage parameters is specified in the request. If you want to decrease the storage capacity, the specified storage capacity is greater than or equal to 1.1 times the used storage capacity. The instance is a primary or read-only instance. If you want to upgrade the RDS edition of the instance, for example, from the Basic Edition to the High-availability Edition, you need only to select a proper instance type. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstance Spec | The operation that you want to perform. Set the value to Modif yDBInst anceSpec. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| PayType | String | Yes | Postpaid | The billing method of the instance. Set the value to Post paid. |
| DBInstanceClass | String | No | rds.mys2.small | The instance type of the instance. For more information, see Inst ance t ypes in ApsaraDB RDS Product Int roduct ion. You can call the DescribeAvailableClasses operation to query the instance types that are available in a region. Not e You must specify at least one of the DBInstanceClass and DBInst anceSt orage parameters. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceStorag e | Integer | No | 20 | The storage capacity of the instance. Unit: GB. The storage capacity increases in increments of 5 GB. For more information, see Inst ance t ypes in ApsaraDB RDS Product Int roduct ion. You can also call the DescribeAvailableClasses operation to query the storage capacity range that is available for a specific instance type in a region. Not e You must specify at least one of the DBInstanceStorage and DBInst anceClass parameters. If the instance runs MySQL on RDS High-availability Edition with local SSDs, you can decrease the storage capacity in decrements of 5 GB. |
| EffectiveTime | String | No | MaintainTime | The time when you want the specified settings to take effect. Valid values: Immediat e: The settings take effect immediately. Maint ainT ime: The settings take effect during the maintenance window of the instance. Default value: Immediat e. |
| SourceBiz | String | No | None | An invalid parameter. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Category | String | No | HighAvailability | The RDS edition of the instance. Valid values: Basic: Basic Edition HighAvailabilit y: High-availability Edition Finance: Enterprise Edition |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 3C5CFDEE-F774- 4DED-89A2- 1D76EC63C575 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ModifyDBInstanceSpec &DBInstanceId=rm-uf6wjk5xxxxxxx &PayType=Postpaid &DBInstanceClass=rds.mys2.small &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceSpecResponse>
  <RequestId>3C5CFDEE-F774-4DED-89A2-1D76EC63C575</RequestId>
  <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
  <OrderId>207938506080728</OrderId>
</ModifyDBInstanceSpecResponse>
```

`JSON` format `{`

```json
    "RequestId": "3C5CFDEE-F774-4DED-89A2-1D76EC63C575",
    "DBInstanceId": "rm-uf6wjk5xxxxxxx",
    "OrderId": 207938506080728
```

`}`

#### 2.1.7 DescribeRegions

Queries the details of the regions that are available to ApsaraDB RDS. Before you call the CreateDBInstance operation to create an instance, you can call the DescribeRegions operation to query the available regions and zones. If a zone supports the multi-zone deployment method, the value of the ZoneId parameter for the zone contains an MAZ part. Examples: cn-hangzhou-MAZ6(b,f) and cnhangzhou-MAZ5(b,e,f). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRegions | The operation that you want to perform. Set the value to DescribeRegions. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Regions | Array of RDSRegion |   | Details of the available regions and zones. |
| RDSRegion |   |   |   |
| RegionId | String | cn-hangzhou | The ID of the region. |
| ZoneId | String | cn-hangzhou-b | The ID of the zone. |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | The ID of the request. |

Examples Sample requests

```
https://rds.example.com/?Action=DescribeRegions &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeRegionsResponse>
  <RequestId>1CE1DC20-7EFC-464F-9583-0AB8915C5697</RequestId>
  <Regions>
        <RDSRegion>
              <ZoneId>cn-hangzhou-h</ZoneId>
              <RegionId>cn-hangzhou</RegionId>
              <LocalName>China (Hangzhou)</LocalName>
              <RegionEndpoint>rds.aliyuncs.com</RegionEndpoint>
        </RDSRegion>
        <RDSRegion>
              <ZoneId>cn-hangzhou-MAZ10(h,i)</ZoneId>
              <RegionId>cn-hangzhou</RegionId>
              <LocalName>China (Hangzhou)</LocalName>
              <RegionEndpoint>rds.aliyuncs.com</RegionEndpoint>
        </RDSRegion>
        <RDSRegion>
              <ZoneId>cn-hangzhou-MAZ8(f,g)</ZoneId>
              <RegionId>cn-hangzhou</RegionId>
              <LocalName>China (Hangzhou)</LocalName>
              <RegionEndpoint>rds.aliyuncs.com</RegionEndpoint>
        </RDSRegion>
  </Regions>
</DescribeRegionsResponse>
```

`JSON` format `{`

```json
  "RequestId": "1CE1DC20-7EFC-464F-9583-0AB8915C5697",
  "Regions": {
    "RDSRegion": [
```

`{`

```json
        "ZoneId": "cn-hangzhou-h",
        "RegionId": "cn-hangzhou",
        "LocalName": "China (Hangzhou)",
        "RegionEndpoint": "rds.aliyuncs.com"
```

`},` `{`

```json
        "ZoneId": "cn-hangzhou-MAZ10(h,i)",
        "RegionId": "cn-hangzhou",
        "LocalName": "China (Hangzhou)",
        "RegionEndpoint": "rds.aliyuncs.com"
```

`},` `{`

```json
        "ZoneId": "cn-hangzhou-MAZ8(f,g)",
        "RegionId": "cn-hangzhou",
        "LocalName": "China (Hangzhou)",
        "RegionEndpoint": "rds.aliyuncs.com"
```

`}` `]` `}` `}`

#### 2.1.8 MigrateToOtherZone

Migrates an ApsaraDB RDS instance across zones within the same region. For example, if an instance is located in Hangzhou Zone A, you can call this operation to migrate the instance to Hangzhou Zone B. You can migrate the instance between zones only within the same region. For example, you cannot migrate the instance from a zone in the China (Hangzhou) region to a zone in the China (Qingdao) region. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | MigrateToOtherZ one | The operation that you want to perform. Set the value to Migrat eT oOt herZone. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxxxx x | The ID of the instance. |

| psaraDB for RDS |   |   |   | Developer Guide·API referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ZoneId | String | Yes | cn-hangzhou-b | The ID of the destination zone. You can call the DescribeRegions operation to query the most recent region list. |
| EffectiveTime | String | No | Immediate | The time when you want the change to take effect. Valid values: Immediat e: The change takes effect immediately. Maint ainT ime: The change takes effect during the maintenance window of the instance. Default value: Immediat e. |
| VSwitchId | String | No | vsw- uf6adz52c2pxxxx xxx | The ID of the vSwitch. Not e This parameter must be specified when the instance resides in a virtual private cloud (VPC). |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=MigrateToOtherZone &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &ZoneId=cn-hangzhou-b &<Common request parameters>
```

Sample success responses `XML` format

```xml
<MigrateToOtherZoneResponse>
      <RequestId> 65BDA532-28AF-4122-AA39-B382721EEE64</RequestId></MigrateToOtherZoneRespo
nse>
```

`JSON` format `{`

```json
  "RequestId": " 65BDA532-28AF-4122-AA39-B382721EEE64"
```

`}` Error codes

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | IncorrectDBInstanceL ockMode.ValueNotS upported | The Current DB instance lock mode does not support this operation. | The error message returned because the lock mode of the instance does not support this operation. |
| 403 | OperationDenied.Ou tofUsage | The resource is out of usage. | The error message returned because the specified zone does not provide sufficient resources. Select another zone and try again. |
| 404 | InvalidVPCId.NotFou nd | Specified virtual vpc is not found. | The error message returned because the specified VPC ID does not exist. Check whether the VPC ID is correct. |

#### 2.1.9 ModifyDBInstanceDescription

Modifies the name of an ApsaraDB RDS instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstance Description | The operation that you want to perform. Set the value to Modif yDBInst anceDescript ion. |
| DBInstanceDescri ption | String | Yes | Instance in Alibaba Cloud test environment | The name of the instance. Not e The name must be 2 to 64 characters in length. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxxxx x | The ID of the instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 17F57FEE-EA4F- 4337-8D2E- 9C23CAA63D74 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ModifyDBInstanceDescription &DBInstanceDescription=Instance in Alibaba Cloud test environment &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceDescriptionResponse>
           <RequestId>17F57FEE-EA4F-4337-8D2E-9C23CAA63D74</RequestId>
</ModifyDBInstanceDescriptionResponse>
```

`JSON` format `{`

```json
    "RequestId": " 17F57FEE-EA4F-4337-8D2E-9C23CAA63D74"
```

`}`

#### 2.1.10 ModifyDBInstanceMaintainTime

Modifies the maintenance window of an ApsaraDB RDS instance. You can set the maintenance window to a period of time during off-peak hours. Apsara Stack performs routine maintenance within the maintenance window to minimize impacts on your business. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstance MaintainTime | The operation that you want to perform. Set the value to Modif yDBInst anceMaint ainT ime. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| MaintainTime | String | Yes | 22:00Z-02:00Z | The maintenance window of the instance. Specify the time in the HH:mmZ-HH:mmZ format. The time must be in UTC. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ModifyDBInstanceMaintainTime &DBInstanceId=rm-uf6wjk5xxxxxxx &MaintainTime=22:00Z-02:00Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceMaintainTimeResponse>
           <RequestId>65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
</ModifyDBInstanceMaintainTimeResponse>
```

`JSON` format `{`

```json
  "RequestId": " 65BDA532-28AF-4122-AA39-B382721EEE64"
```

`}`

#### 2.1.11 DescribeCharacterSetName

Queries the character sets that are supported for an ApsaraDB RDS instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCharacte rSetName | The operation that you want to perform. Set the value to DescribeCharact erSet Name. |
| Engine | String | Yes | mysql | The database engine of the instance. Valid values: mysql mssql Post greSQL MariaDB |
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. You can call the DescribeRegions operation to query the most recent region list. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CharacterSetNa meItems | List | ["gbk","utf8","euckr" ,"ascii"] | Details of the character sets that are supported for the instance. |
| Engine | String | mysql | The database engine of the instance. |
| RequestId | String | 1E43AAE0-BEE8- 43DA-860D- EAF2AA0724DC | The ID of the request. |

Examples Sample requests

```
http(s)://example/?Action=DescribeCharacterSetName &Engine=mysql &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC</RequestId> <CharacterSetNameItems>
    <CharacterSetName>["gbk","utf8","euckr","ascii"]</CharacterSetName>
</CharacterSetNameItems> <Engine>mysql</Engine>
```

`JSON` format `{`

```json
    "RequestId": "1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC",
    "CharacterSetNameItems": {
        "CharacterSetName": "[\"gbk\",\"utf8\",\"euckr\",\"ascii\"]"
```

`},`

```json
    "Engine": "mysql"
```

`}`

#### 2.1.12 DescribeDBInstanceIpHostname

Queries the hostname of the Elastic Compute Service (ECS) instance where an ApsaraDB RDS instance resides. ApsaraDB RDS instances are deployed based on ECS instances. This operation is used to query the hostname of the ECS instance where an ApsaraDB RDS instance resides. The hostname is required when you configure a distributed transaction whitelist. This operation is applicable only to ApsaraDB RDS High-availability Edition instances that run one of the following SQL Server versions: 2012 SE, 2012 EE, 2014 SE, 2016 SE, 2016 EE, and 2017 SE. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstan ceIpHostname | The operation that you want to perform. Set the value to DescribeDBInst anceIpHost name. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the ApsaraDB RDS instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | The ID of the ApsaraDB RDS instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| IpHostnameInf os | String | 172.16.xx.xx,sdxxxxx xxxB;172.16.xx.xx,sd xxxxxxxxA | The internal IP addresses and hostnames of the ECS instances where the primary and secondary ApsaraDB RDS instances reside. Format: IP address 1,Hostname 1;IP address 2,Hostname 2. |
| RequestId | String | 67CD4719-51E3- 4A76-A38C- 02F45FAE7E36 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeDBInstanceIpHostname &DBInstanceId=rm-uf6wjk5xxxxxxx &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeDBInstanceIpHostnameResponse>
  <IpHostnameInfos>172.16.xx.xx,sdxxxxxxxxB;172.16.xx.xxx,sdxxxxxxxxA</IpHostnameInfos>
      <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
      <RequestId>67CD4719-51E3-4A76-A38C-02F45FAE7E36</RequestId>
</DescribeDBInstanceIpHostnameResponse>
```

`JSON` format `{`

```json
    "IpHostnameInfos": "172.16.xx.xx,sdxxxxxxxxB;172.16.xx.xx,sdxxxxxxxxA",
    "DBInstanceId": "rm-uf6wjk5xxxxxxx",
    "RequestId": "67CD4719-51E3-4A76-A38C-02F45FAE7E36"
```

`}`

#### 2.1.13 ModifyResourceGroup

Migrates an ApsaraDB RDS instance to a specified resource group. Resource Management enables you to build an organizational structure for resources based on your business needs. You can use a resource directory, folders, accounts, and resource groups to hierarchically organize and manage resources. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyResourceG roup | The operation that you want to perform. Set the value to Modif yResourceGroup. |
| DBInstanceId | String | Yes | rm-bpxxxxx | The ID of the instance. |
| ResourceGroupId | String | Yes | rg-acxxxxx | The ID of the resource group. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ModifyResourceGroup &DBInstanceId=rm-bpxxxxx &ResourceGroupId=rg-acxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyResourceGroupResponse>
  <RequestId>65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
</ModifyResourceGroupResponse>
```

`JSON` format `{`

```json
    "RequestId": "65BDA532-28AF-4122-AA39-B382721EEE64"
```

`}` Error codes

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | ResourceGroupId.InV alid | The Specified resource group id is not found. | The error message returned because the specified resource group ID does not exist. Check whether the ID is correct. |

### 2.2 Read-only instances

#### 2.2.1 CreateReadOnlyDBInstance

Creates a read-only instance for a primary ApsaraDB RDS instance. Bef ore you call t his operat ion, make sure t hat t he f ollowing requirement s are met : The primary instance cannot belong to a dedicated cluster and must run one of the following database engine versions and RDS editions: MySQL 8.0 on RDS High-availability Edition or Enterprise Edition MySQL 5.7 on RDS High-availability Edition or Enterprise Edition MySQL 5.6 SQL Server 2017 EE PostgreSQL 10, 11, or 12 on RDS High-availability Edition (If the primary instance runs PostgreSQL 10, it must be equipped with local SSDs.) If the primary instance runs MySQL, the number of read-only instances that are created cannot reach the upper limit. If the memory capacity of the primary instance is greater than or equal to 64 GB, up to 10 readonly instances can be created. If the memory capacity of the primary instance is less than 64 GB, up to five read-only instances can be created. If the primary instance runs SQL Server, up to seven read-only instances can be created. If the primary instance runs PostgreSQL with local SSDs, up to five read-only instances can be created. If the primary instance runs PostgreSQL with standard SSDs, up to 32 read-only instances can be created. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateReadOnlyD BInstance | The operation that you want to perform. Set the value to Creat eReadOnlyDBInst ance. |
| DBInstanceClass | String | Yes | rds.mys2.small | The instance type of the read-only instance. For more information, see Instance types in ApsaraDB RDS Product Int roduct ion. We recommend that you specify an instance type higher than or equal to that of the primary instance. If the instance type of the read-only instance is lower than that of the primary instance, the read-only instance may encounter issues such as high latency or heavy load. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the primary instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| DBInstanceStorag e | Integer | Yes | 20 | The storage capacity of the read-only instance. Valid values: 5 t o 3000. Unit: GB. The storage capacity increases in increments of 5 GB. Not e The supported storage capacity range varies based on the RDS edition that is used. For more information, see the buy page of read-only instances. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| EngineVersion | String | Yes | 5.6 | The major engine version of the read- only instance. The read-only instance must run the same major engine version as the primary instance. If the read-only instance runs MySQL, set this parameter to 5.6, 5.7, or 8.0. If the read-only instance runs SQL Server, set this parameter to 2017 ent or 2019 ent . _ _ If the read-only instance runs PostgreSQL, set this parameter to 10.0, 11.0, or 12.0. |
| PayType | String | Yes | Postpaid | The billing method of the read-only instance. Set the value to Post paid. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region. The read-only instance and the primary instance must reside in the same region. You can call the DescribeRegions operation to query the most recent region list. |
| ZoneId | String | Yes | cn-hangzhou-b | The ID of the zone. You can call the DescribeRegions operation to query the most recent zone list. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceStorag eType | String | No | local ssd _ | The storage type of the read-only instance. Valid values: local ssd: local SSD _ cloud ssd: standard SSD _ Not e ApsaraDB RDS for MySQL supports only local SSDs. ApsaraDB RDS for SQL Server supports only standard SSDs. |
| DBInstanceDescri ption | String | No | Test read-only instance | The description of the read-only instance. The description must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), _ and hyphens (-). The description must start with a letter. Not e The description cannot start with http:// or https://. |
| InstanceNetwork Type | String | No | Classic | The network type of the read-only instance. Valid values: VPC Classic Default value: VPC. If you set this parameter to VPC, you must also specify the VPCId and VSwit chId parameters. Not e The network type of the read-only instance can be different from that of the primary instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VPCId | String | No | vpc- uf6f7l4fg90xxxxx xxxxx | The virtual private cloud (VPC) ID of the read-only instance. If you leave the Inst anceNet workT ype parameter empty or set this parameter to VPC, you must specify the VPCId parameter. Not e If local SSDs are used for the primary instance, the read-only instance can belong to a VPC different from that of the primary instance. If standard SSDs are used for the primary instance, the read-only instance must belong to the same VPC as the primary instance. |
| VSwitchId | String | No | vsw- uf6adz52c2pxxxx xxxxxx | The ID of the vSwitch of the read-only instance. If you leave the Inst anceNet workT ype parameter empty or set this parameter to VPC, you must specify the VSwitchId parameter. |
| PrivateIpAddress | String | No | 172.16.201.69 | The internal IP address of the read- only instance. The internal IP address must be within the CIDR block that is supported by the specified vSwitch. The system automatically assigns an internal IP address to the instance based on the VPCId and VSwit chId values. |
| ResourceGroupId | String | No | rg- acfmyxxxxxxxxxx | The ID of the resource group. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Category | String | No | HighAvailability | The RDS edition of the read-only instance. Valid values: Basic: Basic Edition HighAvailabilit y: High-availability Edition Not e If the read-only instance runs PostgreSQL with standard SSDs, you must set this parameter to Basic. |
| DedicatedHostGr oupId | String | No | None | An invalid parameter. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | rr-uf6wjk5xxxxxxx | The ID of the read-only instance. |
| OrderId | String | 10078937xxxxx | The ID of the order. |
| ConnectionStrin g | String | rr- xxxxx.mysql.rds.aliy uncs.com | The internal endpoint of the read-only instance. |
| Port | String | 3306 | The internal port number of the read-only instance. |
| RequestId | String | 1E43AAE0-BEE8- 43DA-860D- EAF2AA0724DC | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=CreateReadOnlyDBInstance &RegionId=cn-hangzhou &ZoneId=cn-hangzhou-b &DBInstanceId=rm-uf6wjk5xxxxxxx &DBInstanceClass=rds.mys2.small &DBInstanceStorage=20 &EngineVersion=5.6 &PayType=Postpaid &VPCId=vpc-uf6f7l4fg90xxxxxxxxxx &VSwitchId=vsw-uf6adz52c2pxxxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateReadOnlyDBInstanceResponse>
      <OrderId>10078937xxxxx</OrderId>
      <ConnectionString>rm-uf6wjk5xxxxxxx.mysql.rds.aliyuncs.com</ConnectionString>
      <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
      <Port>3306</Port>
      <RequestId>1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC</RequestId>
</CreateReadOnlyDBInstanceResponse>
```

`JSON` format `{`

```json
    "CreateReadOnlyDBInstanceResponse": {
        "OrderId": "10078937xxxxx",
        "ConnectionString": "rm-uf6wjk5xxxxxxx.mysql.rds.aliyuncs.com",
        "DBInstanceId": "rm-uf6wjk5xxxxxxx",
        "Port": 3306,
        "RequestId": "1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC"
```

`}` `}` Error codes

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidEngineVersion. Malformed | The specified parameter "EngineVersion" is not valid. | The error message returned because the specified engine version is invalid. |
| 400 | InvalidSecurityIPList. Malformed | The specified parameter "SecurityIPList" is not valid. | The error message returned because the IP address whitelist of the instance is invalid. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidSecurityIPList. Duplicate | The Security IP address is not in the available range or occupied. | The error message returned because the specified IP address is in use or is not within the valid range. Specify a valid IP address. |
| 400 | InvalidParameter | The specified parameter "dbInstanceId" is not valid. | The error message returned because the specified instance ID is invalid. Specify a valid instance ID. |
| 403 | OperationDenied.Pri maryDBInstanceStat us | The operation is not permitted due to status of primary instance. | The error message returned because the instance belongs to a dedicated cluster and is not in the running state. |
| 400 | OperationDenied | VPC IP is in use, please check. | The error message returned because the specified IP address in the VPC is already in use. |
| 404 | IncorrectDBInstanceC onnType | Current DB instance conn type does not support this operation. | The error message returned because the network connection type of the instance does not support this operation. |
| 400 | InvalidZoneId.NotSu pported | The Specified vpc Zone not supported. | The error message returned because the specified zone does not allow you to create an instance in a VPC. Specify a different zone and try again. |

#### 2.2.2 DescribeReadDBInstanceDelay

Queries the latency of data replication between a primary ApsaraDB RDS instance and its read-only instance. Before you call this operation, make sure that the following requirements are met: The instance runs MySQL, PostgreSQL, or PolarDB. The primary instance has a read-only instance attached. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeReadDBIn stanceDelay | The operation that you want to perform. Set the value to DescribeReadDBInst anceDelay. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm-bpxxxxxxx | The ID of the primary instance. |
| ReadInstanceId | String | Yes | rr-bpxxxxxxx | The ID of the read-only instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | rm-bpxxxxxxx | The ID of the primary instance. |
| DelayTime | Integer | 0 | The latency of data replication between the primary instance and the read-only instance. |
| Items | Array of Items |   | Details of the latency information. |
| Items |   |   |   |
| DBInstanceId | String | rm-bpxxxxxxx | The ID of the primary instance. |
| ReadDBInstance Names | List | "ReadDBInstanceNa me": ["rr-bpxxxxx"] | The name of the read-only instance. Not e This parameter is returned only when the primary instance runs the MySQL database engine. |
| ReadDelayTime s | List | "ReadDelayTime": ["0"] | The latency of data replication. Not e This parameter is returned only when the primary instance runs the MySQL database engine. |
| ReadonlyInstan ceDelay | Array of ReadonlyInstan ceDelay |   | Details of the write-ahead log (WAL) latency. Not e This parameter is returned only when the primary instance runs the PostgreSQL or PPAS database engine. |
| ReadonlyInstan ceDelay |   |   |   |

| D | eveloper Guide·AP | I reference |   | ApsaraDB for RD | S |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| FlushLag | String | 0 | The duration that is allowed for the latency in the persistence of WAL data. Unit: seconds. |
| FlushLatency | String | 0 | The data size that is allowed for the latency in the persistence of WAL data. Unit: MB. |
| ReadDBInstance Name | String | rr-bpxxxxxxx | The name of the read-only instance. |
| ReplayLag | String | 0 | The duration that is allowed for the latency in the playback of WAL data. Unit: seconds. |
| ReplayLatency | String | 0 | The data size that is allowed for the latency in the playback of WAL data. Unit: MB. |
| SendLatency | String | 0 | The data size that is allowed for the latency in the sending of WAL data. Unit: MB. |
| WriteLag | String | 0 | The duration that is allowed for the latency in the write-back of WAL data. Unit: seconds. |
| WriteLatency | String | 0 | The data size that is allowed for the latency in the write-back of WAL data. Unit: MB. |
| ReadDBInstance Id | String | rr-bpxxxxxxx | The ID of the read-only instance. |
| RequestId | String | F1BDDEA8-452D- 450B-AB10- CD5C5BAFC5DF | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeReadDBInstanceDelay &RegionId=cn-hangzhou &DBInstanceId=rm-bpxxxxxxx &ReadInstanceId=rr-bpxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeReadDBInstanceDelayResponse>
  <RequestId>11152741-D854-4E18-920E-64E75D484D57</RequestId>
  <DBInstanceId>rm-bpxxxxx</DBInstanceId>
  <Items>
        <Items>
              <ReadDBInstanceNames>
                    <ReadDBInstanceName>rr-bpxxxxx</ReadDBInstanceName>
              </ReadDBInstanceNames>
              <ReadDelayTimes>
                    <ReadDelayTime>0</ReadDelayTime>
              </ReadDelayTimes>
              <DBInstanceId>rm-bpxxxxx</DBInstanceId>
              <ReadonlyInstanceDelay>
        </ReadonlyInstanceDelay>
        </Items>
  </Items>
  <DelayTime>0</DelayTime>
</DescribeReadDBInstanceDelayResponse>
```

`JSON` format `{`

```json
    "RequestId": "11152741-D854-4E18-920E-64E75D484D57",
    "DBInstanceId": "rm-bpxxxxx",
    "Items": {
        "Items": [
```

`{`

```json
                "ReadDBInstanceNames": {
                    "ReadDBInstanceName": [
                        "rr-bpxxxxx"
```

`]` `},`

```json
                "ReadDelayTimes": {
                    "ReadDelayTime": [
                        "0"
```

`]` `},`

```json
                "DBInstanceId": "rm-bpxxxxx",
                "ReadonlyInstanceDelay": {
                    "ReadonlyInstanceDelay": []
```

`}` `}` `]` `},`

```json
    "DelayTime": "0"
```

`}`

### 2.3 Version upgrade

2.3.1.

#### ModifyDBInstanceAutoUpgradeMinorVersion

Changes the method used to update the minor engine version of an ApsaraDB RDS instance. This operation is supported only for instances that run MySQL. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstance AutoUpgradeMin orVersion | The operation that you want to perform. Set this value to Modif yDBInst anceAut oUpgradeMin orVersion. |
| AutoUpgradeMin orVersion | String | Yes | Auto | The method that is used to update the minor engine version of the instance. Valid values: Aut o: automatic update. Manual: manual update. ApsaraDB RDS automatically updates the current minor engine version of the instance only when the current minor engine version is phased out. |
| DBInstanceId | String | Yes | rm-uf6wjk5xxx | The ID of the instance. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | A31818D5-0550- 4A81-8D13- B45948D7193F | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ModifyDBInstanceAutoUpgradeMinorVersion &DBInstanceId=rm-uf6wjk5xxx &AutoUpgradeMinorVersion=Auto &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceAutoUpgradeMinorVersionResponse>
    <RequestId>A31818D5-0550-4A81-8D13-B45948D7193F</RequestId>
</ModifyDBInstanceAutoUpgradeMinorVersionResponse>
```

`JSON` format `{`

```json
    "RequestId": "A31818D5-0550-4A81-8D13-B45948D7193F"
```

`}`

#### 2.3.2 UpgradeDBInstanceKernelVersion

Updates the minor engine version of an ApsaraDB RDS instance. An update to the minor engine version enhances performance, introduces new features, and fixes known bugs. This operation is supported only for instances that run the MySQL, SQL Server, or PostgreSQL database engine. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpgradeDBInstan ceKernelVersion | The operation that you want to perform. Set the value to UpgradeDBInst anceKernelVersion. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm-bpxxxxx | The ID of the instance. This operation is supported only for instances that run the MySQL, SQL Server, or PostgreSQL database engine. Not e If your instance runs PostgreSQL, you must make sure that the instance uses st andard SSDs. If your instance uses local SSDs, you can call the RestartDBInstance operation to restart the instance. In this case, your instance can automatically update to the latest minor engine version. If your instance runs SQL Server, you must make sure that the instance runs SQL Server 2019. |
| SwitchTime | String | No | 2020-01- 15T00:00:00Z | The specific point in time when you want to perform the update. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Not e This parameter takes effect only when you set the UpgradeT ime parameter to Specif yT ime. |
| SwitchTimeMode | String | No | Immediately | The method that is used to update the minor engine version. Valid values: Immediat ely: immediately updates the minor engine version. Maint ainT ime: updates the minor engine version during the maintenance window of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceNam e | String | rm-bpxxxxx | The ID of the instance. |
| RequestId | String | DA2ECBA0-4745- 4491-9166- 799FF8984AC9 | The ID of the request. |
| TargetMinorVer sion | String | xcluster80 2021030 _ 5 | The new minor engine version of the instance. |
| TaskId | String | 226917711 | The ID of the task. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=UpgradeDBInstanceKernelVersion &DBInstanceId=rm-bpxxxxx &UpgradeTime=SpecifyTime &SwitchTime=2020-01-15T00:00:00Z &TargetMinorVersion=xcluster80_20210305 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UpgradeDBInstanceKernelVersion>
      <TaskId>226917711</TaskId>
      <RequestId>DA2ECBA0-4745-4491-9166-799FF8984AC9</RequestId>
      <TargetMinorVersion>xcluster80_20210305</TargetMinorVersion>
      <DBInstanceName>rm-bpxxxxx</DBInstanceName>
</UpgradeDBInstanceKernelVersion>
```

`JSON` format `{`

```json
 "TaskId": "226917711",
 "RequestId": "DA2ECBA0-4745-4491-9166-799FF8984AC9",
 "TargetMinorVersion": "xcluster80_20210305",
 "DBInstanceName": "rm-bpxxxxx"
```

`}`

### 2.4 Network and endpoint management

management

#### 2.4.1 AllocateInstancePublicConnection

Applies for a public endpoint for an ApsaraDB for RDS instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AllocateInstanceP ublicConnection | The operation that you want to perform. Set the value to Allocat eInst ancePublicConnect ion. |
| ConnectionString Prefix | String | Yes | test1234 | The prefix of the public endpoint. A complete public endpoint must be in the following format: <Prefix>. <Database engine name>.rds.aliyuncs.com. Example: test1234.mysql.rds.aliyuncs.com. Not e The prefix must be 5 to 40 characters in length and can contain letters, digits, and hyphens (-).It cannot contain the following special characters: ~ ! # % ^ & * = + \| { } ; : ' " , < > / ? |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| Port | String | Yes | 3306 | The public port of the instance. Valid values: 1000 t o 5999. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=AllocateInstancePublicConnection &ConnectionStringPrefix=test1234 &DBInstanceId=rm-uf6wjk5xxxxxxx &Port=3306 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AllocateInstancePublicConnectionResponse>
         <RequestId>65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
</AllocateInstancePublicConnectionResponse>
```

`JSON` format `{`

```json
  "RequestId": " 65BDA532-28AF-4122-AA39-B382721EEE64"
```

`}`

#### 2.4.2 ReleaseInstancePublicConnection

Releases the public endpoint of an ApsaraDB RDS instance. When you do not need to connect to an instance over the Internet, you can release its public endpoint to ensure data security. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ReleaseInstanceP ublicConnection | The operation that you want to perform. Set the value to ReleaseInst ancePublicConnect ion. |
| CurrentConnectio nString | String | Yes | rm- uf6wjk5xxxx.mys ql.rds.aliyuncs.co m | The public endpoint. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ReleaseInstancePublicConnection &DBInstanceId=rm-uf6wjk5xxxxxxx &CurrentConnectionString=rm-uf6wjk5xxxx.mysql.rds.aliyuncs.com &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ReleaseInstancePublicConnectionResponse>
         <RequestId>65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
</ReleaseInstancePublicConnectionResponse>
```

`JSON` format `{`

```json
  "RequestId": " 65BDA532-28AF-4122-AA39-B382721EEE64"
```

`}`

#### 2.4.3 SwitchDBInstanceNetType

Switches an ApsaraDB RDS instance between its internal and public endpoints. To save endpoint resources, you can call this operation to switch an instance between its internal and public endpoints. After the endpoint that is used to connect to the instance is changed, you must update the endpoint information in the code of your application and restart the application. Before you call this operation, make sure that the following requirements are met: The instance is connected by using its internal or public endpoint. The instance is in the running state. The number of times that you have switched the instance between its internal and public endpoints within the last 24 hours does not reach 20. The instance resides in the classic network. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SwitchDBInstance NetType | The operation that you want to perform. Set the value to Swit chDBInst anceNet T ype. |
| ConnectionString Prefix | String | Yes | test1234 | The prefix of the endpoint. The prefix must be 8 to 64 characters in length and can contain letters and digits. It must start with a lowercase letter. A complete endpoint must be in the following format: <Prefix>.<Database engine name>.rds.aliyuncs.com. Example: test1234.mysql.rds.aliyuncs.com. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| Port | String | No | 3306 | The number of the port that is used to connect to the instance. Valid values: 3001 t o 3999. |
| ConnectionString Type | String | No | Normal | The type of the endpoint. Valid values: Normal ReadWrit eSplit t ing If this parameter is not specified, the system returns both types of endpoints. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=SwitchDBInstanceNetType &DBInstanceId=rm-uf6wjk5xxxxxxx &ConnectionStringPrefix=rm-xxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SwitchDBInstanceNetTypeResponse>
      <RequestId> 65BDA532-28AF-4122-AA39-B382721EEE64</RequestId></SwitchDBInstanceNetType
Response>
```

`JSON` format `{`

```json
  "RequestId": " 65BDA532-28AF-4122-AA39-B382721EEE64"
```

`}`

#### 2.4.4 DescribeDBInstanceNetInfo

Queries the connection information of an ApsaraDB RDS instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstan ceNetInfo | The operation that you want to perform. Set the value to DescribeDBInst anceNet Inf o. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| Flag | String | No | N/A | The hidden parameter. |

| psaraDB for RDS |   |   |   | Developer Guide·API referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceNetRW SplitType | String | No | Normal | The type of the endpoint. Valid values: Normal ReadWrit eSplit t ing Not e By default, the system returns both types of endpoints. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceNetI nfos | Array of DBInstanceNetI nfo |   | Details of the instance connection information. |
| DBInstanceNetI nfo |   |   |   |
| ConnectionStrin g | String | rm- uf6wxxxxx.mysql.rd s.aliyuncs.com | The endpoint of the instance. |
| IPAddress | String | 192.168.12.84 | The IP address of the instance. |
| IPType | String | Public | The network type of the instance. Valid values when the instance resides in the classic network: Inner: internal network Public: Internet Valid values when the instance resides in a virtual private cloud (VPC): Privat e: internal network Public: Internet |
| Port | String | 3306 | The port that is used to connect to the instance. |
| VPCId | String | vpc- uf6f7l4fg90xxxxxxxx xx | The ID of the VPC. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| VSwitchId | String | vsw- uf6adz52c2pxxxxxxx xxx | The ID of the vSwitch. |
| ConnectionStrin gType | String | Normal | The type of the endpoint. Valid values: Normal ReadWrit eSplit t ing |
| MaxDelayTime | String | 12 | The latency threshold. This parameter is returned only for a read/write splitting endpoint. Unit: seconds. Not e If the latency on a read- only instance exceeds the specified threshold, ApsaraDB RDS no longer routes read requests to the read-only instance. |
| DistributionTyp e | String | Standard | The policy that is used to allocate read weights. This parameter is returned only for a read/write splitting endpoint. Valid values: St andard: ApsaraDB RDS allocates a read weight to each instance based on the instance specifications. Cust om: You must manually assign a read weight to each instance. |
| DBInstanceWeig hts | Array of DBInstanceWeig ht |   | Details of the weight. This parameter is returned only when the read/write splitting feature is enabled for the instance. |
| DBInstanceWeig ht |   |   |   |
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | The ID of the instance. |
| DBInstanceType | String | Master | The role of the instance. Valid values: Mast er: primary instance Readonly: read-only instance |
| Weight | String | 100 | The weight of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Availability | String | Unavailable | The availability of the instance. Valid values: Unavailable Available |
| ExpiredTime | String | 1209534 | The remaining time of the classic network in hybrid access mode. Unit: seconds. |
| SecurityIPGroup s | Array of securityIPGroup |   | Details of the IP address whitelist. |
| securityIPGroup |   |   |   |
| SecurityIPGroup Name | String | Default | The name of the IP address whitelist. |
| SecurityIPs | String | 127.0.0.1 | The IP addresses contained in the IP address whitelist. |
| Upgradeable | String | Disabled | Indicates whether the IP version can be updated. Valid values: Enable and Disabled. Not e The IP version can be updated from IPv4 to IPv6. |
| InstanceNetwor kType | String | VPC | The network type. Valid values: Classic VPC |
| RequestId | String | 777C4593-8053- 427B-99E2- 105593277CAB | The ID of the request. |
| SecurityIPMode | String | safety | The whitelist mode of the instance. Valid values: normal: standard whitelist mode saf et y: enhanced whitelist mode |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeDBInstanceNetInfo &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
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

#### 2.4.5 ModifyDBInstanceConnectionString

Modifies the endpoint and port number of an ApsaraDB RDS instance. ApsaraDB RDS provides the internal and public endpoints. It allows hybrid access by using both a Virtual Private Cloud (VPC) endpoint and a classic network endpoint. You can modify only the prefix of an endpoint. The read/write splitting endpoint cannot be modified. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstance ConnectionString | The operation that you want to perform. Set the value to Modif yDBInst anceConnect ionSt ring . |
| ConnectionString Prefix | String | Yes | rm-xxxxxx | The prefix of the endpoint. Only the prefix of the Current Connect ionSt ring parameter value can be modified. Not e The prefix must be 8 to 64 characters in length and can contain letters, digits, and hyphens (-).It cannot contain the following special characters: ~ ! # % ^ & * = + \ \| { } ; : ' " , < > / ? |
| CurrentConnectio nString | String | Yes | rm- uf6wjk5xxxxxxx.m ysql.rds.aliyuncs. com | The endpoint of the instance. It can be an internal endpoint, a public endpoint, or a classic network endpoint in hybrid access mode. Not e The read/write splitting endpoint cannot be modified. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| Port | String | Yes | 3306 | The new port number of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ModifyDBInstanceConnectionString &DBInstanceId=rm-uf6wjk5xxxxxxx &CurrentConnectionString=rm-uf6wjk5xxxxxxx.mysql.rds.aliyuncs.com &ConnectionStringPrefix=rm-xxxxxx &Port=3306 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceConnectionStringResponse>
         <RequestId>65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
</ModifyDBInstanceConnectionStringResponse>
```

`JSON` format `{`

```json
  "RequestId": " 65BDA532-28AF-4122-AA39-B382721EEE64"
```

`}`

#### 2.4.6 ReleaseInstanceConnection

Releases the endpoint of an ApsaraDB RDS instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ReleaseInstanceC onnection | The operation that you want to perform. Set the value to ReleaseInst anceConnect ion. |
| CurrentConnectio nString | String | Yes | rm- uf6wjk5xxxx.mys ql.rds.aliyuncs.co m | The public endpoint of the instance. |

| A | psaraDB for RDS |   |   |   | Developer Guide·API referenc | e |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| InstanceNetwork Type | String | Yes | Classic | The network type of the instance. Valid values: VPC Classic |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ReleaseInstanceConnection &CurrentConnectionString=rm-uf6wjk5xxxx.mysql.rds.aliyuncs.com &DBInstanceId=rm-uf6wjk5xxxxxxx &InstanceNetworkType=Classic &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ReleaseInstanceConnectionResponse>
      <RequestId>65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
</ReleaseInstanceConnectionResponse>
```

`JSON` format `{`

```json
    "RequestId":"65BDA532-28AF-4122-AA39-B382721EEE64"
```

`}`

#### 2.4.7 ModifyDBInstanceNetworkType

Changes the network type of an ApsaraDB RDS instance. This operation is used to switch the network type of an instance between Virtual Private Cloud (VPC) and classic network. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstance NetworkType | The operation that you want to perform. Set the value to Modif yDBInst anceNet workT ype. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| InstanceNetwork Type | String | Yes | Classic | The new network type of the instance. Valid values: VPC Classic |
| RetainClassic | String | No | True | Specifies whether to retain the classic network endpoint. Valid values: T rue: retains the classic network endpoint. False: does not retain the classic network endpoint. Default value: False. Not e This parameter is valid when the network type is changed from classic network to VPC. |
| ClassicExpiredDay s | String | No | 7 | The number of days for which you want to retain the classic network endpoint. Valid values: 1 t o 120. Default value: 7. Not e This parameter is required if Ret ainClassic is set to T rue. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ReadWriteSplittin gClassicExpiredDa ys | Integer | No | 7 | The number of days for which you want to retain the read/write splitting endpoint of the classic network type. Valid values: 1 t o 120. Default value: 7. Not e This parameter is valid when a read/write splitting endpoint of the classic network type exists and when Ret ainClassic is set to T rue. |
| VPCId | String | No | vpc- uf6f7l4fg90xxxxx x | The ID of the VPC. |
| VSwitchId | String | No | vsw- uf6adz52c2pxxxx x | The ID of the vSwitch. This parameter is required if the VPCId parameter is specified. |
| PrivateIpAddress | String | No | 172.10.40.25 | The internal IP address of the instance, which must be within the CIDR block supported by the specified vSwitch. The system automatically assigns an internal IP address to the instance based on the VPCId and VSwit chId values. |
| ReadWriteSplittin gPrivateIpAddres s | String | No | 192.168.0.22 | The internal IP address corresponding to the read/write splitting endpoint of the instance, which must be within the CIDR block supported by the specified vSwitch. The system automatically assigns an internal IP address to the instance based on the VPCId and VSwit chId values. Not e This parameter is valid when a read/write splitting endpoint of the classic network type exists. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | The ID of the request. |
| TaskId | String | 1025486523574 | The ID of the task. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ModifyDBInstanceNetworkType &DBInstanceId=rm-uf6wjk5xxxxxxx &InstanceNetworkType=Classic &<Common request parameters>
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

`}` Error codes

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | NetTypeExists | Specified network type already exists. | The error message returned because the specified network type is the same as the original network type of the specified instance. |
| 403 | OperationDenied.DBI nstanceConnType | The current DB instance connection type does not support this operation. | The error message returned because the current network connection type does not support this operation. |

#### 2.4.8 SwitchDBInstanceVpc

Changes the virtual private cloud (VPC) or vSwitch of an ApsaraDB RDS instance. This operation is supported only for ApsaraDB RDS for PostgreSQL instances that use standard SSDs or ApsaraDB RDS for MySQL instances. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SwitchDBInstance Vpc | The operation that you want to perform. Set the value to Swit chDBInst anceVpc. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. Not e The instance must run PostgreSQL with standard SSDs or run MySQL. The instance must be in the running state. The instance must reside in a VPC. The instance cannot be a temporary instance or a shared instance. |
| VPCId | String | No | vpc- uf6f7l4fg90xxxxx xxxxx | The ID of the VPC. Not e The VPC must belong to the same region as the instance. You can change the VPC of the instance only when the instance runs MySQL with local SSDs. |
| VSwitchId | String | No | vsw- uf6adz52c2pxxxx xxxxxx | The ID of the vSwitch. Not e The vSwitch must belong to the same zone as the instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PrivateIpAddress | String | No | 10.23.xx.xx | The internal IP address of the instance, which must be within the CIDR block supported by the vSwitch specified by the VSwit chId parameter. Not e You can call the DescribeVSwitches operation to query available vSwitches. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 777C4593-8053- 427B-99E2- 10xxxxxxxxxx | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=SwitchDBInstanceVpc &DBInstanceId=rm-uf6wjk5xxxxxxx &VPCId=vpc-uf6f7l4fg90xxxxxxxxxx &VSwitchId=vsw-uf6adz52c2pxxxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>777C4593-8053-427B-99E2-10xxxxxxxxxx </RequestId>
```

`JSON` format `{`

```json
    "RequestId": "777C4593-8053-427B-99E2-10xxxxxxxxxx"
```

`}`

#### 2.4.9 ModifyDBInstanceNetworkExpireTime

Changes the expiration time of an endpoint for an ApsaraDB RDS instance. When an ApsaraDB RDS instance runs in hybrid access mode and provides both a VPC endpoint and a classic network endpoint, this operation is used to extend the expiration time of the retained classic network endpoint. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstance NetworkExpireTi me | The operation that you want to perform. Set the value to Modif yDBInst anceNet workExpireT i me. |
| ConnectionString | String | Yes | rm- uf6wjk5xxxxx.mys ql.rds.aliyuncs.co m | The classic network endpoint whose expiration time you want to extend. Valid values: Internal endpoint of the classic network Read/write splitting endpoint of the classic network |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| ClassicExpiredDay s | Integer | No | 7 | The number of days for which you want to extend the expiration time of the classic network endpoint. Valid values: 1 t o 120. |
| RdsClassicexpired | String | No | None | An invalid parameter. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4C467B38-3910- 447D-87BC- AC049166F216 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ModifyDBInstanceNetworkExpireTime &DBInstanceId=rm-uf6wjk5xxxxxxx &ConnectionString=rm-uf6wjk5xxxxx.mysql.rds.aliyuncs.com &ClassicExpiredDays=7 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceNetworkExpireTimeResponse>
      <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
    </ModifyDBInstanceNetworkExpireTimeResponse>
```

`JSON` format `{`

```json
    "RequestId": "4C467B38-3910-447D-87BC-AC049166F216"
```

`}`

### 2.5 Database management

#### 2.5.1 CreateDatabase

Creates a database on an ApsaraDB RDS instance. If you want to perform data management tasks such as data change and schema design, use Data Management System (DMS). Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The maximum number of databases in the instance is not reached. You can call the DescribeDBInstanceAttribute operation to query the maximum number of databases. The instance is not a read-only instance. This operation is not supported for instances that run PostgreSQL with local SSDs or SQL Server 2017 EE. You can execute the CREATE DATABASE statement to create a database. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateDatabase | The operation that you want to perform. Set the value to Creat eDat abase. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| CharacterSetNam e | String | Yes | gbk | The character set. Valid values for MySQL databases: ut f 8, gbk, lat in1, and ut f 8mb4 Valid values for SQL Server databases: Chinese PRC CI AS, _ _ _ Chinese PRC CS AS, _ _ _ SQL Lat in1 General CP1 CI AS, _ _ _ _ _ SQL Lat in1 General CP1 CS AS, _ _ _ _ _ and Chinese PRC BIN _ _ Valid values for PostgreSQL databases: KOI8U, UT F8, WIN866, WIN874, WIN1250, WIN1251, WIN1252, WIN1253, WIN1254, WIN1255, WIN1256, WIN1257, WIN1258, EUC CN, EUC KR, _ _ EUC T W, EUC JP, EUC JIS 2004, _ _ _ _ KOI8R, MULE INT ERNAL, LAT IN1, _ LAT IN2, LAT IN3, LAT IN4, LAT IN5, LAT IN6, LAT IN7, LAT IN8, LAT IN9, LAT IN10, ISO 8859 5, _ _ ISO 8859 6, ISO 8859 7, _ _ _ _ ISO 8859 8, and SQL ASCII _ _ _ |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxxxx x | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| DBName | String | Yes | rds mysql _ | The name of the database. Not e The name must be 2 to 64 characters in length. The name must start with a lowercase letter and end with a lowercase letter or a digit. The name can contain lowercase letters, digits, underscores ( ), and _ hyphens (-). The name must be unique within the instance. For information about invalid characters, see Forbidden keywords. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBDescription | String | No | Test database | The description of the database. It must be 2 to 256 characters in length. It must start with a letter and can contain letters, digits, underscores ( ), _ and hyphens (-). Not e The description cannot start with http:// or https:// . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5A77D650-27A1- 4E08-AD9E- 59008EDB6927 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=CreateDatabase &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &DBName=rds_mysql &CharacterSetName=gbk &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateDatabaseResponse>
    <RequestId>5A77D650-27A1-4E08-AD9E-59008EDB6927</RequestId>
</CreateDatabaseResponse>
```

`JSON` format `{`

```json
    "RequestID":"5A77D650-27A1-4E08-AD9E-59008EDB6927"
```

`}`

#### 2.5.2 DeleteDatabase

Deletes a database from an ApsaraDB RDS instance. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance is a primary instance. The instance runs the MySQL or SQL Server database engine. This operation is not supported for instances that run PostgreSQL. You can execute the DROP DATABASE statement to delete a database. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteDatabase | The operation that you want to perform. Set the value to Delet eDat abase. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| DBName | String | Yes | testdb01 | The name of the database. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 07F6177E-6DE4- 408A-BB4F- 0723301340F3 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DeleteDatabase &DBInstanceId=rm-uf6wjk5xxxxxxx &DBName=testdb01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteDatabaseResponse>
      <RequestId>07F6177E-6DE4-408A-BB4F-0723301340F3</RequestId></DeleteDatabaseResponse>
```

`JSON` format `{`

```json
    "RequestId":"07F6177E-6DE4-408A-BB4F-0723301340F3"
```

`}`

#### 2.5.3 DescribeDatabases

Queries the details of databases on an ApsaraDB RDS instance. If the request parameters are incorrectly specified, the response is null. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDatabas es | The operation that you want to perform. Set the value to DescribeDat abases. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| DBName | String | No | testDB01 | The name of the database. |
| DBStatus | String | No | Creating | The state of the database. Valid values: Creat ing Running Delet ing |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30 50 100 Default value: 30 |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Databases | Array of Database |   | Details of the databases. |

| psaraDB for RDS |   |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Database |   |   |   |
| DBName | String | testDB01 | The name of the database. |
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | The ID of the instance to which the database belongs. |
| Engine | String | MySQL | The database engine of the instance to which the database belongs. |
| DBStatus | String | Creating | The state of the database. Valid values: Creat ing Running Delet ing |
| CharacterSetNa me | String | utf8 | The name of the character set. |
| DBDescription | String | Test database | The description of the database. |
| Accounts | Array of AccountPrivileg eInfo |   | Details of the account that has specific permissions on the database. |
| AccountPrivileg eInfo |   |   |   |
| Account | String | test | The name of the account. |
| AccountPrivileg e | String | DMLOnly | The permissions that the account has on the database. Valid values: ReadWrit e: read and write permissions ReadOnly: read-only permissions DMLOnly: DML-only permissions DDLOnly: DDL-only permissions |
| RequestId | String | 2603CA96-B17D- 4903-BC04- 61A2C829CD94 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeDatabases &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeDatabasesResponse>
      <RequestId>2603CA96-B17D-4903-BC04-61A2C829CD94</RequestId>
      <Databases>
            <Database>
                  <Engine>MySQL</Engine>
                  <CharacterSetName>utf8</CharacterSetName>
                  <DBStatus>Creating</DBStatus>
                  <DBDescription></DBDescription>
                  <DBInstanceId>rdsaiiabnaiiabn</DBInstanceId>
                  <Accounts></Accounts>
                  <DBName>testdb</DBName>
            </Database>
            <Database>
                  <Engine>MySQL</Engine>
                  <CharacterSetName>gbk</CharacterSetName>
                  <DBStatus>Creating</DBStatus>
                  <DBDescription></DBDescription>
                  <DBInstanceId>rdsaiiabnaiiabn</DBInstanceId>
                  <Accounts></Accounts>
                  <DBName>testdb2</DBName>
            </Database>
      </Databases></DescribeDatabasesResponse>
```

`JSON` format `{`

```json
    "RequestId": "2603CA96-B17D-4903-BC04-61A2C829CD94",
    "Databases": {
        "Database": [
```

`{`

```json
                "Engine": "MySQL",
                "CharacterSetName": "utf8",
                "DBStatus": "Creating",
                "DBDescription": "",
                "DBInstanceId": "rdsaiiabnaiiabn",
                "Accounts": {
                    " AccountPrivilegeInfo": []
```

`},`

```json
                "DBName": "testdb"
```

`},` `{`

```json
                "Engine": "MySQL",
                "CharacterSetName": "gbk",
                "DBStatus": "Creating",
                "DBDescription": "",
                "DBInstanceId": "rdsaiiabnaiiabn",
                "Accounts": {
                    " AccountPrivilegeInfo": []
```

`},`

```json
                "DBName": "testdb2"
```

`}` `]` `}` `}`

#### 2.5.4 ModifyDBDescription

Modifies the description of a database. This operation is not supported for instances that run PostgreSQL or PolarDB. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBDescript ion | The operation that you want to perform. Set the value to Modif yDBDescript ion. |
| DBDescription | String | Yes | Test database A | The description of the database. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| DBName | String | Yes | testDB01 | The name of the database. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 17F57FEE-EA4F- 4337-8D2E- 9C23CAA63D74 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ModifyDBDescription &DBDescription=Test database A &DBInstanceId=rm-uf6wjk5xxxxxxx &DBName=testDB01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBDescriptionResponse>
      <RequestId> 17F57FEE-EA4F-4337-8D2E-9C23CAA63D74</RequestId>
</ModifyDBDescriptionResponse>
```

`JSON` format `{`

```json
  "RequestId": " 17F57FEE-EA4F-4337-8D2E-9C23CAA63D74"
```

`}`

#### 2.5.5 CopyDatabaseBetweenInstances

Copies databases across ApsaraDB RDS instances. This operation can also be used to restore specific databases to an existing instance by point in time or backup set. Before you call this operation, make sure that the following requirements are met: The source and destination instances belong to the same Apsara Stack tenant account. The source and destination instances run the same version of database engine. The source and destination instances reside in the same region and use the same network type. Their zones can be different. The destination instance does not have databases whose names are the same as those of the databases that you want to copy. The available storage capacity of the destination instance is larger than the size of the databases that you want to copy from the source instance. This operation is applicable only to ApsaraDB RDS for SQL Server 2012 or 2016. You can restore specific databases or tables of an ApsaraDB RDS for MySQL instance to the original instance or a new instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CopyDatabaseBet weenInstances | The operation that you want to perform. Set the value to CopyDat abaseBet weenInst ances. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the source instance. |
| DbNames | String | Yes | {"test1":"test2"} | The names of the databases to be copied. Format: {"Source instance database name":"Destination instance database name"}. |
| TargetDBInstance Id | String | Yes | rm- ut5ajk3xxxxxxx | The ID of the destination instance, which must differ from the ID of the source instance. |
| BackupId | String | No | 1065238746521 | The ID of the backup set by which you want to restore databases of the source instance. You can call the DescribeBackups operation to obtain the IDs of backup sets. Not e You can specify one of BackupId and Rest oreT ime. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RestoreTime | String | No | 2011-06- 11T16:00:00Z | The point in time to which you want to restore databases of the source instance. You can select a point in time within the backup retention period. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. Not e You can specify one of BackupId and Rest oreT ime. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | rm- uf6wjk5xxxxxxxxxx | The ID of the destination instance. |
| RequestId | String | 803D11AF-C370- 465B-AB46- CB3A642DC303 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=CopyDatabaseBetweenInstances &DBInstanceId=rm-uf6wjk5xxxxxxx &TargetDBInstanceId=rm-ut5ajk3xxxxxxx &DbNames={"test1":"test2"} &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CopyDatabaseBetweenInstancesResponse>
      <RequestId>803D11AF-C370-465B-AB46-CB3A642DC303</RequestId>
</CopyDatabaseBetweenInstancesResponse>
```

`JSON` format `{`

```json
    "RequestId": "803D11AF-C370-465B-AB46-CB3A642DC303"
```

`}`

### 2.6 Account management

#### 2.6.1 CreateAccount

Creates an account that is used to manage databases on an ApsaraDB RDS instance. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The database is in the running state. The number of accounts that are created on the instance does not exceed the maximum number of accounts that are allowed for each instance. This operation is supported only for instances that run MySQL, PostgreSQL, or SQL Server. This operation is not supported for instances that run SQL Server 2017 EE or SQL Server 2019 EE. You can create multiple privileged accounts and multiple standard accounts for each ApsaraDB RDS instance that runs PostgreSQL with standard SSDs. You can create only a single privileged account for each ApsaraDB RDS instance that runs PostgreSQL 9.4 or PostgreSQL 10.0 with local SSDs. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateAccount | The operation that you want to perform. Set the value to Creat eAccount . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AccountName | String | Yes | test1 | The name of the account. Not e The name must be unique. The name must start with a letter and end with a letter or a digit. The name can contain lowercase letters, digits, and underscores ( ). _ The length of the name must meet the following requirements: If the instance runs MySQL 5.6, the name must be 2 to 16 characters in length. If the instance runs MySQL 5.7 or MySQL 8.0, the name must be 2 to 32 characters in length. If the instance runs SQL Server, the name must be 2 to 64 characters in length. If the instance runs PostgreSQL with standard SSDs, the name must be 2 to 63 characters in length. If the instance runs PostgreSQL with local SSDs, the name must be 2 to 16 characters in length. For information about invalid characters, see Forbidden keywords. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AccountPassword | String | Yes | Test123456 | The password of the account. Not e The password must be 8 to 32 characters in length. The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password can contain the following special characters: ! @ # $ % ^ & * ( ) + - = _ |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| AccountDescripti on | String | No | Test account A | The description of the account. The description must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), and _ hyphens (-). The description must start with a letter. Not e The description cannot start with http:// or https://. |
| AccountType | String | No | Normal | The type of the account. Valid values: Normal: standard account Super: privileged account Default value: Normal. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D4D4BE8A-DD46- 440A-BFCD- EE31DA81C9DD | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=CreateAccount &DBInstanceId=rm-uf6wjk5xxxxxxx &AccountName=test1 &AccountPassword=Test123456 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateAccountResponse>
         <RequestId>D4D4BE8A-DD46-440A-BFCD-EE31DA81C9DD</RequestId>
</CreateAccountResponse>
```

`JSON` format `{`

```json
    "RequestId":"D4D4BE8A-DD46-440A-BFCD-EE31DA81C9DD"
```

`}`

#### 2.6.2 DeleteAccount

Deletes an account from an ApsaraDB for RDS instance. Before you call this operation, make sure that the instance is in the running state. This operation is not supported for instances that run SQL Server 2017 EE or PostgreSQL with local SSDs. If the instance runs PostgreSQL with standard SSDs and the account to be deleted has permissions on databases, tables, or other objects, this operation only locks the account. To delete the account, you must revoke the permissions. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteAccount | The operation that you want to perform. Set the value to Delet eAccount . |
| AccountName | String | Yes | test1 | The name of the account. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 91E855E5-7E80- 4955-929B- C74EE1D38C66 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DeleteAccount &DBInstanceId=rm-uf6wjk5xxxxxxx &AccountName=test1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteAccountResponse>
      <RequestID>91E855E5-7E80-4955-929B-C74EE1D38C66</RequestID>
</DeleteAccountResponse>
```

`JSON` format `{`

```json
    "RequestID":"91E855E5-7E80-4955-929B-C74EE1D38C66"
```

`}`

#### 2.6.3 CheckAccountNameAvailable

Queries whether the name of the account that you want to create on an ApsaraDB RDS instance is available. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CheckAccountNa meAvailable | The operation that you want to perform. Set the value to CheckAccount NameAvailable. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AccountName | String | Yes | DatabaseTest | The name of the account that you want to create. |
| DBInstanceId | String | Yes | rm-uf6wjk5xxxxx | The ID of the instance. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5E4AA101-1EE5- 41C0-AE6D- 0F066331AC1C | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=CheckAccountNameAvailable &AccountName=DatabaseTest &DBInstanceId=rm-uf6wjk5xxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CheckAccountNameAvailableResponse>
      <RequestId>5E4AA101-1EE5-41C0-AE6D-0F066331AC1C</RequestId>
</CheckAccountNameAvailableResponse>
```

`JSON` format `{`

```json
    "RequestId":"5E4AA101-1EE5-41C0-AE6D-0F066331AC1C"
```

`}`

#### 2.6.4 CheckDBNameAvailable

Checks whether a database name is unique and conforms to the naming conventions on an ApsaraDB RDS instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CheckDBNameAva ilable | The operation that you want to perform. Set the value to CheckDBNameAvailable. |
| DBInstanceId | String | Yes | rm-t4n3axxxxx | The ID of the instance. |
| DBName | String | Yes | test1 | The database name to check. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6EF82B07-28D2- 48D1-B5D6- 7E78FED277C7 | The ID of the request. Not e If this operation returns only the ID of the request, the database name can be used. Otherwise, an error message is returned to indicate that the database name is duplicate or does not conform to the naming conventions. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=CheckDBNameAvailable &DBInstanceId=rm-t4n3axxxxx &DBName=test1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CheckDBNameAvailableResponse>
  <RequestId>6EF82B07-28D2-48D1-B5D6-7E78FED277C7</RequestId>
</CheckDBNameAvailableResponse>
```

`JSON` format

```json
{"RequestId":"6EF82B07-28D2-48D1-B5D6-7E78FED277C7"}
```

#### 2.6.5 DescribeAccounts

Queries the details of accounts created on an ApsaraDB RDS instance. This operation is not supported for instances that run SQL Server 2017 EE or PostgreSQL. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAccounts | The operation that you want to perform. Set the value to DescribeAccount s. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| AccountName | String | No | test1 | The name of the account. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Accounts | Array of DBInstanceAcco unt |   | Details of the accounts. |
| DBInstanceAcco unt |   |   |   |
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | The ID of the instance to which the account belongs. |
| AccountName | String | test1 | The name of the account. |
| AccountStatus | String | Available | The state of the account. Valid values: Unavailable Available |
| AccountDescrip tion | String | Test account | The description of the account. |
| DatabasePrivile ges | Array of DatabasePrivile ge |   | Details of the permissions that are granted to the account. |
| DatabasePrivile ge |   |   |   |
| DBName | String | test1 | The name of the database. |
| AccountPrivileg e | String | ReadWrite | The type of permissions that are granted to the account. Valid values: ReadWrit e: read and write permissions ReadOnly: read-only permissions DDLOnly: DDL-only permissions DMLOnly: DML-only permissions Cust om: custom permissions (which can be modified by using SQL commands) |
| AccountPrivileg eDetail | String | SELECT,INSERT | The permissions that are granted to the account. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AccountType | String | Normal | The type of the account. Valid values: Normal: standard account Super: privileged account Sysadmin: superuser account that has the system administrator permissions |
| PrivExceeded | String | 0 | Indicates whether the number of databases that are managed by the account exceeds the upper limit. Valid values: 1: yes 0: no |
| RequestId | String | A2E94301-D07F- 4457-9B49- 6AA2BB388C85 | The ID of the request. |
| SystemAdminA ccountFirstActiv ationTime | String | 2020-02- 06T11:00:00Z | The first time when the superuser account was enabled. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. Not e This parameter is returned only when you set the SysadminAccount parameter to True. |
| SystemAdminA ccountStatus | String | True | Indicates whether the superuser account is enabled. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeAccounts &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeAccountsResponse>
   <Accounts>
      <DBInstanceAccount>
         <DatabasePrivileges>
            <DatabasePrivilege>
               <AccountPrivilege>ReadWrite</AccountPrivilege>
               <AccountPrivilegeDetail>SELECT,INSERT,UPDATE,DELETE,CREATE,DROP,REFERENCES,I
NDEX,ALTER,CREATE TEMPORARY TABLES,LOCK TABLES,CREATE VIEW,SHOW VIEW,CREATE ROUTINE,ALTER R OUTINE,EXECUTE,EVENT,TRIGGER</AccountPrivilegeDetail>
               <DBName>testdb</DBName>
            </DatabasePrivilege>
         </DatabasePrivileges>
         <AccountStatus>Available</AccountStatus>
         <AccountDescription></AccountDescription>
         <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
         <AccountName>testacc02</AccountName>
         <PrivExceeded>0</PrivExceeded>
         <AccountType>Normal</AccountType>
      </DBInstanceAccount>
   </Accounts>
   <RequestId>A2E94301-D07F-4457-9B49-6AA2BB388C85</RequestId>
</DescribeAccountsResponse>
```

`JSON` format `{`

```json
    "Accounts": {
        "DBInstanceAccount": [
```

`{`

```json
                "DatabasePrivileges": {
                    "DatabasePrivilege": [
```

`{`

```json
                            "AccountPrivilege": "ReadWrite",
                            "AccountPrivilegeDetail": "SELECT,INSERT,UPDATE,DELETE,CREATE,D
ROP,REFERENCES,INDEX,ALTER,CREATE TEMPORARY TABLES,LOCK TABLES,CREATE VIEW,SHOW VIEW,CREATE ROUTINE,ALTER ROUTINE,EXECUTE,EVENT,TRIGGER",
                            "DBName": "testdb"
```

`}` `]` `},`

```json
                "AccountStatus": "Available",
                "AccountDescription": "",
                "DBInstanceId": "rm-uf6wjk5xxxxxxx",
                "AccountName": "testacc02",
                "PrivExceeded": "0",
                "AccountType": "Normal"
```

`}` `]` `},`

```json
    "RequestId": "A2E94301-D07F-4457-9B49-6AA2BB388C85"
```

`}`

#### 2.6.6 GrantAccountPrivilege

Grants an account the permissions on a database of an ApsaraDB for RDS instance. Each account can be granted permissions on one or more databases. Before you call this operation, make sure that the instance is in the running state. This operation is not supported for instances that run PostgreSQL with local SSDs, SQL Server 2017 EE, or PolarDB. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GrantAccountPrivi lege | The operation that you want to perform. Set the value to Grant Account Privilege. |
| AccountName | String | Yes | test1 | The name of the account. |
| AccountPrivilege | String | Yes | ReadWrite | The permissions of the account. Default value: ReadWrit e: read and write permissions ReadOnly: read-only permissions DDLOnly: DDL-only permissions DMLOnly: DML-only permissions DBOwner: database owner permissions Not e If the instance runs MySQL, you can set this parameter to ReadWrit e, ReadOnly, DDLOnly, or DMLOnly. If the instance runs SQL Server, you can set this parameter to ReadWrit e, ReadOnly, or DBOwner. If the instance runs PostgreSQL with standard SSDs, you can set this parameter to DBOwner. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxxxx x | The ID of the instance. |
| DBName | String | Yes | testDB | The name of the database on which you want to grant permissions. |
| KillConnection | String | No | None | An invalid parameter. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 81BC9559-7B22- 4B7F-B705- 5F56DEECDEA7 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=GrantAccountPrivilege &DBInstanceId=rm-uf6wjk5xxxxxxx &AccountName=test1 &DBName=test &AccountPrivilege=ReadWrite &<Common request parameters>
```

Sample success responses `XML` format

```xml
<GrantAccountPrivilegeResponse>
      <RequestId>81BC9559-7B22-4B7F-B705-5F56DEECDEA7</RequestId>
</GrantAccountPrivilegeResponse>
```

`JSON` format `{`

```json
       "RequestId":"81BC9559-7B22-4B7F-B705-5F56DEECDEA7"
```

`}`

#### 2.6.7 RevokeAccountPrivilege

Revokes database access permissions of an account. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The database is in the running state. The permissions that can be revoked include SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, REFERENCES, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, EVENT, and TRIGGER. This operation is not supported for instances that run PostgreSQL, SQL Server 2017 EE, or PolarDB. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RevokeAccountPri vilege | The operation that you want to perform. Set the value to RevokeAccount Privilege. |
| AccountName | String | Yes | test1 | The name of the account. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| DBName | String | Yes | testDB | The name of the database. You can revoke all permissions of the account on this database. Separate multiple databases with commas (,). |
| KillConnection | String | No | None | An invalid parameter. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | E22099CA-A61E- 4992-A0B7- CE82DC175626 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=RevokeAccountPrivilege &DBInstanceId=rm-uf6wjk5xxxxxxx &AccountName=test1 &DBName=testDB &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RevokeAccountPrivilegeResponse>
   <RequestId>E22099CA-A61E-4992-A0B7-CE82DC175626</RequestId>
</RevokeAccountPrivilegeResponse>
```

`JSON` format `{`

```json
       "RequestId":"E22099CA-A61E-4992-A0B7-CE82DC175626"
```

`}`

#### 2.6.8 ModifyAccountDescription

Modifies the description of a database account. This operation is not supported for instances that run PostgreSQL, SQL Server 2017 EE, or PolarDB. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyAccountDe scription | The operation that you want to perform. Set the value to Modif yAccount Descript ion. |
| AccountDescripti on | String | Yes | Test account A | The description of the account. The description must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), and _ hyphens (-). The description must start with a letter. Not e The description cannot start with http:// or https://. |
| AccountName | String | Yes | test1 | The name of the account. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 17F57FEE-EA4F- 4337-8D2E- 9C23CAA63D74 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ModifyAccountDescription &AccountDescription=Test account A &AccountName=test1 &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyAccountDescriptionResponse>
      <RequestId> 17F57FEE-EA4F-4337-8D2E-9C23CAA63D74</RequestId>
</ModifyAccountDescriptionResponse>
```

`JSON` format `{`

```json
  "RequestId": " 17F57FEE-EA4F-4337-8D2E-9C23CAA63D74"
```

`}`

#### 2.6.9 ResetAccountPassword

Resets the password of an account on an ApsaraDB RDS instance. Before you call this operation, make sure that the instance is in the running state. This operation is not supported for accounts that are created by using SQL statements on instances that run PostgreSQL, SQL Server 2017 EE, or PolarDB. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ResetAccountPas sword | The operation that you want to perform. Set the value to Reset Account Password. |
| AccountName | String | Yes | test1 | The name of the account. |

| psaraDB for RDS |   |   |   | Developer Guide·API referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AccountPassword | String | Yes | Test123456 | The new password for the account. Not e The password must be 8 to 32 characters in length. The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password can contain the following special characters: ! @ # $ & % ^ * ( ) + - = _ |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D4D4BE8A-DD46- 440A-BFCD- EE31DA81C9DD | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ResetAccountPassword &DBInstanceId=rm-uf6wjk5xxxxxxx &AccountName=test1 &AccountPassword=Test123456 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ResetAccountPasswordResponse>
      <RequestId>D4D4BE8A-DD46-440A-BFCD-EE31DA81C9DD</RequestId>
</ResetAccountPasswordResponse>
```

`JSON` format `{`

```json
       "RequestId":"D4D4BE8A-DD46-440A-BFCD-EE31DA81C9DD"
```

`}`

#### 2.6.10 ResetAccount

Resets permissions of the privileged account. This operation is not supported for instances that run SQL Server 2008 R2 because they do not have privileged accounts. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ResetAccount | The operation that you want to perform. Set the value to Reset Account . |
| AccountName | String | Yes | test1 | The name of the privileged account. |
| AccountPassword | String | Yes | Test123456 | The new password of the privileged account. Not e The password must be 8 to 32 characters in length. The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password can contain the following special characters: ! @ # $ & % ^ * ( ) + - = _ |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 81BC9559-7B22- 4B7F-B705- 5F56DEECDEA7 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ResetAccount &AccountName=test1 &AccountPassword=Test123456 &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ResetAccountResponse>
      <RequestId>81BC9559-7B22-4B7F-B705-5F56DEECDEA7</RequestId>
</ResetAccountResponse>
```

`JSON` format `{`

```json
       "RequestId":"81BC9559-7B22-4B7F-B705-5F56DEECDEA7"
```

`}`

#### 2.6.11 GrantOperatorPermission

Grants permissions to the service account of an ApsaraDB RDS instance. When you seek help from Alibaba Cloud technical support to troubleshoot instance exceptions, you must grant permissions to the service account of your instance. The service account is used by Alibaba Cloud technical support to perform operations on the databases of your instance. This operation is available only when your instance runs one of the following database engines: MySQL SQL Server PostgreSQL Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GrantOperatorPer mission | The operation that you want to perform. Set the value to GrantOperatorPermission. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| ExpiredTime | String | Yes | 2019-03- 27T16:00:00Z | The expiration time of the permissions. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |
| Privileges | String | Yes | Control | The permissions that you want to grant to the service account. Valid values: Cont rol: the configuration permissions, which allow you to view and modify configurations of the instance. Dat a: the data permissions, which allow you to view schemas, indexes, and SQL statements of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 842B73C8-5776- 4BD9-9872- 69C8C46DD7D3 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=GrantOperatorPermission &DBInstanceId=rm-uf6wjk5xxxxxxx &ExpiredTime=2019-03-27T16:00:00Z &Privileges=Control &<Common request parameters>
```

Sample success responses `XML` format

```xml
<GrantOperatorPermissionResponse>
      <RequestId>842B73C8-5776-4BD9-9872-69C8C46DD7D3</RequestId>
</GrantOperatorPermissionResponse>
```

`JSON` format `{`

```json
    "RequestId":"842B73C8-5776-4BD9-9872-69C8C46DD7D3"
```

`}`

#### 2.6.12 LockAccount

Locks an account of an ApsaraDB RDS for PostgreSQL instance. ApsaraDB RDS for PostgreSQL instances that use standard SSDs allow you to lock accounts. Locked accounts cannot be used to log on to an instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | LockAccount | The operation that you want to perform. Set the value to LockAccount . |
| AccountName | String | Yes | testaccount | The account that you want to lock. You can lock only a single account at a time. |
| DBInstanceId | String | Yes | pgm-bpxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1B291C4B-DDCD- 4D0A-8F6D- 7F3241DE9228 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=LockAccount &AccountName=testaccount &DBInstanceId=pgm-bpxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<LockAccountResponse>
    <RequestId>1B291C4B-DDCD-4D0A-8F6D-7F3241DE9228</RequestId>
</LockAccountResponse>
```

`JSON` format `{`

```json
    "RequestId": "1B291C4B-DDCD-4D0A-8F6D-7F3241DE9228"
```

`}`

#### 2.6.13 RevokeOperatorPermission

Revokes permissions from the service account of an ApsaraDB RDS instance. After Alibaba Cloud technical support resolves the issues on your instance, you can revoke permissions from the service account of your instance. This operation is available only when your instance runs one of the following database engines: MySQL SQL Server PostgreSQL Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RevokeOperatorP ermission | The operation that you want to perform. Set the value to RevokeOperat orPermission. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 842B73C8-5776- 4BD9-9872- 69C8C46DD7D3 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=RevokeOperatorPermission &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RevokeOperatorPermissionResponse>
      <RequestId>842B73C8-5776-4BD9-9872-69C8C46DD7D3</RequestId>
</RevokeOperatorPermissionResponse>
```

`JSON` format `{`

```json
    "RequestId":"842B73C8-5776-4BD9-9872-69C8C46DD7D3"
```

`}`

#### 2.6.14 UnlockAccount

Unlocks an account of an ApsaraDB RDS for PostgreSQL instance. You cannot use a locked account to log on to the corresponding ApsaraDB RDS for PostgreSQL instance that uses standard SSDs. You must first unlock the account. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UnlockAccount | The operation that you want to perform. Set the value to UnlockAccount . |
| AccountName | String | Yes | testaccount | The account that you want to unlock. You can unlock only a single account at a time. |
| DBInstanceId | String | Yes | pgm-bpxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | AA65190D-852A- 4C9B-88DA- E92698CAA350 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=UnlockAccount &AccountName=testaccount &DBInstanceId=pgm-bpxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UnlockAccountResponse>
  <RequestId>AA65190D-852A-4C9B-88DA-E92698CAA350</RequestId>
</UnlockAccountResponse>
```

`JSON` format `{`

```json
    "RequestId": "AA65190D-852A-4C9B-88DA-E92698CAA350"
```

`}`

### 2.7 Backup and restoration

#### 2.7.1 CreateBackup

Creates a backup set for an ApsaraDB RDS instance. This operation uses the backup feature of ApsaraDB RDS to create a backup set. You can also use an operation of Database Backup (DBS) to create a backup schedule. For more information, see List of operat ions by f unct ion in Dat abase Backup Developer Guide. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance does not have ongoing backup tasks. The number of backup sets that are created per day for an instance cannot exceed 20. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateBackup | The operation that you want to perform. Set the value to Creat eBackup. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| DBName | String | No | rds mysql _ | The name of the database whose data you want to back up. Separate multiple database names with commas (,). Not e You can specify this parameter when you perform a logical backup on individual databases of an ApsaraDB RDS for MySQL instance. You can also specify this parameter when you perform a full physical backup on individual databases of an ApsaraDB RDS for SQL Server instance. |
| BackupStrategy | String | No | db | The backup policy of the instance. Valid values: db: database backup inst ance: instance backup Not e You can specify this parameter when you perform a logical backup on an ApsaraDB RDS for MySQL instance. You can also specify this parameter when you perform a full physical backup on an ApsaraDB RDS for SQL Server instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| BackupMethod | String | No | Physical | The backup type of the instance. Valid values: Logical: logical backup Physical: physical backup Snapshot : snapshot backup Default value: Physical. Not e You can perform a logical backup only when databases are created on the instance. For more information about backup types supported by instances that run different database engines, see User Guide of the corresponding database engines. When you perform a snapshot backup on an ApsaraDB RDS for SQL Server instance that uses standard SSDs, you must set this parameter to Snapshot . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| BackupType | String | No | Auto | The backup method of the instance. Valid values: Aut o: full or incremental backup that is automatically selected FullBackup: full backup Default value: Aut o. Not e You must set this parameter only when the instance runs the SQL Server database engine. This parameter is valid only when the BackupMet hod parameter is set to Physical. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupJobId | String | 5073731 | The ID of the backup task. |
| RequestId | String | 2C125605-266F- 41CA-8AC5- 3A643D4F42C5 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=CreateBackup &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateBackupResponse>
   <RequestId>2C125605-266F-41CA-8AC5-3A643D4F42C5</RequestId>
   <BackupJobId>5073731</BackupJobId>
</CreateBackupResponse>
```

`JSON` format `{`

```json
    "RequestId": "2C125605-266F-41CA-8AC5-3A643D4F42C5",
    "BackupJobId": "5073731"
```

`}`

#### 2.7.2 CloneDBInstance

Restores the data of an ApsaraDB RDS instance to a new instance. The new instance is also called a cloned instance. Before you call this operation, make sure that the following requirements are met: The original instance is in the running state. The original instance does not have ongoing migration tasks. The log backup feature is enabled for the original instance to support point-in-time restoration. The primary instance has at least one completed backup set before you clone the instance by backup set. RAM users can be used to create cloned instances. Make sure that your RAM users have been granted permissions to clone instances. Take note of the following information: The new instance has the same IP address whitelist, SQL Explorer (SQL Audit), alert threshold, backup, and parameter settings as the original instance. The data and account information of the new instance is the same as that indicated by the backup set or point in time used for restoration of the original instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CloneDBInstance | The operation that you want to perform. Set the value to CloneDBInst ance. |
| PayType | String | Yes | Postpaid | The billing method of the new instance. Set the value to Post paid. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceClass | String | No | mysql.n1.micro.1 | The instance type of the new instance. For more information, see Inst ance t ypes in ApsaraDB RDS Product Int roduct ion. Not e The default value is the instance type of the original instance. |
| DBInstanceStorag e | Integer | No | 1000 | The storage capacity of the new instance. Unit: GB. The storage capacity must be in 5 GB increments. For more information, see Inst ance t ypes in ApsaraDB RDS Product Int roduct ion. Not e The default value is the storage capacity of the original instance. |
| InstanceNetwork Type | String | No | VPC | The network type of the new instance. Valid values: VPC Classic Not e The default value is the network type of the original instance. |
| DBInstanceId | String | No | rm- uf6wjk5xxxxxxxxx x | The ID of the original instance. You can call the DescribeDBInstances operation to query the IDs of instances. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| BackupId | String | No | 9026262 | The ID of the backup set by which you want to restore the original instance. You can call the DescribeBackups operation to query the backup set list. Not e You must specify at least one of BackupId and Rest oreT ime. |
| RestoreTime | String | No | 2011-06- 11T16:00:00Z | The point in time to which you want to restore the original instance. You can select a point in time within the backup retention period. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. Not e You must specify at least one of BackupId and Rest oreT ime. |
| VPCId | String | No | vpc- uf6f7l4fg90xxxxx xxxxx | The ID of the virtual private cloud (VPC). Not e The VPC must belong to the specified region. |
| VSwitchId | String | No | vsw- uf6adz52c2pxxxx xxxxxx | The ID of the vSwitch. Not e The vSwitch must belong to the specified VPC and region. |
| PrivateIpAddress | String | No | 172.16.201.69 | The internal IP address of the new instance, which must be within the CIDR block supported by the specified vSwitch. The system automatically assigns an internal IP address to the instance based on the VPCId and VSwit chId values. |
| UsedTime | String | No | None | An invalid parameter. |

| psaraDB for RDS |   |   |   | Developer Guide·API referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Period | String | No | None | An invalid parameter. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | The ID of the new instance. |
| OrderId | String | 100789370xxxxx | The ID of the order. |
| RequestId | String | 1E43AAE0-BEE8- 43DA-860D- EAF2AA0724DC | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=CloneDBInstance &PayType=Postpaid &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &DBInstanceStorageType=cloud_essd &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CloneDBInstanceResponse>
      <OrderId>100789370xxxxx</OrderId>
      <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
      <RequestId>1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC</RequestId>
</CloneDBInstanceResponse>
```

`JSON` format `{`

```json
    "OrderId": "100789370xxxxx",
    "DBInstanceId": "rm-uf6wjk5xxxxxxx",
    "RequestId": "1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC"
```

`}`

#### 2.7.3 DescribeBackups

Queries the backup sets of an ApsaraDB RDS instance. A backup set can be used to restore data only when its BackupSt at us value is Success. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackups | The operation that you want to perform. Set the value to DescribeBackups. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| BackupId | String | No | 327329803 | The ID of the backup set. |
| BackupStatus | String | No | Success | The status of the backup set. Valid values: Success Failed |
| BackupMode | String | No | Automated | The backup mode. Valid values: Aut omat ed Manual |
| StartTime | String | No | 2011-06- 01T16:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. |
| EndTime | String | No | 2011-06- 15T16:00Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30 50 100 Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalRecordCo unt | String | 100 | The total number of entries returned. |
| PageNumber | String | 1 | The page number of the returned page. |
| PageRecordCou nt | String | 30 | The number of backup sets on the page. |
| Items | Array of Backup |   | Details of the backup sets. |
| Backup |   |   |   |
| BackupId | String | 321020562 | The ID of the backup set. |
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | The ID of the instance. |
| HostInstanceID | String | 5882781 | The No. of the instance that generates the backup set. This parameter is used to indicate whether the instance that generates the backup set is a primary instance or a secondary instance. |
| BackupStatus | String | Success | The status of the backup set. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupStartTim e | String | 2019-02- 03T12:20:00Z | The start time of the backup. The time follows the ISO 8601 standard in the yyyy- MM-ddTHH:mmZ format. The time is displayed in UTC. |
| BackupEndTime | String | 2019-02- 13T12:20:00Z | The end time of the backup. The time follows the ISO 8601 standard in the yyyy- MM-ddTHH:mmZ format. The time is displayed in UTC. |
| BackupType | String | FullBackup | The backup type. Valid values: FullBackup Increment alBackup |
| BackupMode | String | Automated | The backup mode. Valid values: Aut omat ed Manual |
| BackupMethod | String | Physical | The backup method. Valid values: Logical Physical Snapshot |
| BackupDownlo adURL | String | http://rdsbak-hz- v3.oss-cn- hangzhou.aliyuncs.c om/xxxxx | The URL that is used to download the backup file over the Internet. If the backup file cannot be downloaded over the Internet, null is returned. Not e For example, if the instance runs SQL Server and the BackupMethod parameter is set to Snapshot , null is returned. |
| BackupIntranet DownloadURL | String | http://rdsbak-hz- v3.oss-cn- hangzhou- internal.aliyuncs.co m/xxxxx | The URL that is used to download the backup file over an internal network. If the backup file cannot be downloaded over the Internet, null is returned. Not e For example, if the instance runs SQL Server and the BackupMethod parameter is set to Snapshot , null is returned. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupSize | Long | 2167808 | The size of the backup set. Unit: byte. |
| StoreStatus | String | Disabled | Indicates whether the backup set can be deleted. Valid values: Enabled: The backup set can be deleted. Disabled: The backup set cannot be deleted. |
| MetaStatus | String | OK | The status of the backup set that is used to restore individual databases or tables. Valid values: OK: The backup set is normal. LARGE: The backup set contains an abnormally large number of tables. It cannot be used to restore individual databases or tables. EMPT Y: The backup set is generated from a failed backup task. Not e If an empty string is returned, the backup set cannot be used to restore individual databases or tables. |
| SlaveStatus | String | None | An invalid parameter. |
| RequestId | String | 1A6D328C-84B8- 40DC-BF49- 6C73984D7494 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeBackups &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeBackupsResponse>
      <TotalRecordCount>100</TotalRecordCount>
      <TotalEcsSnapshotSize>0</TotalEcsSnapshotSize>
      <PageRecordCount>30</PageRecordCount>
      <RequestId>1A6D328C-84B8-40DC-BF49-6C73984D7494</RequestId>
      <PageNumber>1</PageNumber>
      <Items>
            <Backup>
                  <BackupMethod>Physical</BackupMethod>
                  <BackupInitiator>System</BackupInitiator>
                  <StorageClass>0</StorageClass>
                  <BackupIntranetDownloadURL>http://rdsbak-hz-v3.oss-cn-hangzhou-internal.a
liyuncs.com/xxxxx</BackupIntranetDownloadURL>
                  <BackupSize>2167808</BackupSize>
                  <BackupMode>Automated</BackupMode>
                  <BackupId>321020562</BackupId>
                  <IsAvail>1</IsAvail>
                  <Encryption>{}</Encryption>
                  <HostInstanceID>5882781</HostInstanceID>
                  <StoreStatus>Disabled</StoreStatus>
                  <BackupDownloadURL>http://rdsbak-hz-v3.oss-cn-hangzhou.aliyuncs.com/xxxxx
</BackupDownloadURL>
                  <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
                  <CopyOnlyBackup>0</CopyOnlyBackup>
                  <BackupEndTime>2019-02-13T12:20:00Z</BackupEndTime>
                  <ConsistentTime>1576506856</ConsistentTime>
                  <BackupStartTime>2019-02-03T12:20:00Z</BackupStartTime>
                  <MetaStatus>OK</MetaStatus>
                  <BackupType>FullBackup</BackupType>
                  <BackupStatus>Success</BackupStatus>
                  <BackupDownloadLinkByDB>
                        <BackupDownloadLinkByDB>
                              <DownloadLink>https://cn-hangzhou.bak.rds.aliyuncs.com/custin
s53664665/hins18676859_2021072909473127987849.zip?Expires=*****&amp;dbList=tb1</DownloadLin
```

`k>`

```xml
                              <IntranetDownloadLink>https://cn-hangzhou-internal.bak.rds.al
iyuncs.com/custins53664665/hins18676859_2021072909473127987849.zip?Expires=*****&amp;dbList =tb1</IntranetDownloadLink>
                              <DataBase>dbs</DataBase>
                        </BackupDownloadLinkByDB>
                  </BackupDownloadLinkByDB>
            </Backup>
      </Items>
</DescribeBackupsResponse>
```

`JSON` format `{`

```json
    "DescribeBackupsResponse": {
        "TotalRecordCount": 100,
        "TotalEcsSnapshotSize": 0,
        "PageRecordCount": 30,
        "RequestId": "1A6D328C-84B8-40DC-BF49-6C73984D7494",
        "PageNumber": 1,
        "Items": {
            "Backup": {
                "BackupMethod": "Physical",
                "BackupInitiator": "System",
                "StorageClass": 0,
                "BackupIntranetDownloadURL": "http://rdsbak-hz-v3.oss-cn-hangzhou-internal.
aliyuncs.com/xxxxx",
                "BackupSize": 2167808,
                "BackupMode": "Automated",
                "BackupId": 321020562,
                "IsAvail": 1,
                "Encryption": "{}",
                "HostInstanceID": 5882781,
                "StoreStatus": "Disabled",
                "BackupDownloadURL": "http://rdsbak-hz-v3.oss-cn-hangzhou.aliyuncs.com/xxxx
x",
                "DBInstanceId": "rm-uf6wjk5xxxxxxx",
                "CopyOnlyBackup": 0,
                "BackupEndTime": "2019-02-13T12:20:00Z",
                "ConsistentTime": 1576506856,
                "BackupStartTime": "2019-02-03T12:20:00Z",
                "MetaStatus": "OK",
                "BackupType": "FullBackup",
                "BackupStatus": "Success",
                "BackupDownloadLinkByDB": {
                    "BackupDownloadLinkByDB": {
                        "DownloadLink": "https://cn-hangzhou.bak.rds.aliyuncs.com/custins53
664665/hins18676859_2021072909473127987849.zip?Expires=*****&amp;dbList=tb1",
                        "IntranetDownloadLink": "https://cn-hangzhou-internal.bak.rds.aliyu
ncs.com/custins53664665/hins18676859_2021072909473127987849.zip?Expires=*****&amp;dbList=tb 1",
                        "DataBase": "dbs"
```

`}` `}` `}` `}` `}` `}`

#### 2.7.4 DescribeBackupPolicy

Queries the backup settings of an ApsaraDB RDS instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackupP olicy | The operation that you want to perform. Set the value to DescribeBackupPolicy. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| BackupPolicyMod e | String | No | DataBackupPolicy | The backup type. Valid values: Dat aBackupPolicy: data backup LogBackupPolicy: log backup |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupRetentio nPeriod | Integer | 7 | The number of days for which data backup files are retained. |
| PreferredBacku pTime | String | 15:00Z-16:00Z | The time when a data backup is performed. The time follows the ISO 8601 standard in the HH:mmZ-HH:mmZ format. The time is displayed in UTC. |
| PreferredBacku pPeriod | String | Monday,Wednesday, Friday,Sunday | The cycle based on which data backups are performed. If more than one day of the week is specified, the days of the week are separated by commas (,). Valid values: Monday T uesday Wednesday T hursday Friday Sat urday Sunday |
| BackupLog | String | Enable | Indicates whether the log backup feature is enabled. Value values: Enable and Disabled. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| LogBackupRete ntionPeriod | Integer | 7 | The number of days for which log backup files are retained. |
| EnableBackupL og | String | 1 | Indicates whether the log backup feature can be enabled. Valid values: 1: enables the feature. 0: disables the feature. |
| HighSpaceUsag eProtection | String | Enable | Indicates whether the log backup deletion feature is enabled. If the disk usage exceeds 80% or the remaining disk space is less than 5 GB on the instance, this feature deletes log backup files. Valid values: Disable Enable |
| LocalLogRetent ionHours | Integer | 0 | The number of hours for which log backup files are retained on the instance. |
| LocalLogRetent ionSpace | String | 30 | The maximum disk usage that is allowed for log backup files on the instance. |
| LogBackupFreq uency | String | LogInterval | The frequency at which log backups are performed. Valid values: LogInt erval: Log backups are performed every 30 minutes. Default value: same as the value of the Pref erredBackupPeriod parameter. Not e The LogBackupFrequency parameter is supported only when the instance runs SQL Server. |
| PreferredNextB ackupTime | String | 2018-01-19T15:15Z | The time when the next backup is performed. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. |
| RequestId | String | B87E2AB3-B7C9- 4394-9160- 7F639F732031 | The ID of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ArchiveBackupK eepCount | String | 1 | The number of archived backup files that are retained. |
| ArchiveBackupK eepPolicy | String | ByMonth | The cycle based on which archived backup files are retained. |
| ArchiveBackupR etentionPeriod | String | 365 | The number of days for which archived backup files are retained. |
| CompressType | Integer | 1 | The format that is used to compress backup data. Valid values: 0: Backup data is not compressed. 1: Backup data is compressed by using zlib. 2: Backup data is compressed by using zlib that invokes more than one thread in parallel for each backup. 4: Backup data is compressed by using QuickLZ and can be used to restore individual databases or tables. 8: Backup data is compressed by using QuickLZ but cannot be used to restore individual databases or tables. This value is available only when the instance runs MySQL 8.0. |
| Duplication | String | None | An invalid parameter. |
| DuplicationCont ent | String | None | An invalid parameter. |
| DuplicationLoca tion | Struct |   | An invalid parameter. |
| Location | Struct |   | An invalid parameter. |
| Bucket | String | None | An invalid parameter. |
| Endpoint | String | None | An invalid parameter. |
| Sotrage | String | None | An invalid parameter. |

| psaraDB for RDS |   |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| LogBackupLoca lRetentionNum ber | Integer | 60 | The number of log backup files that are retained on the instance. |
| ReleasedKeepP olicy | String | None | The policy that is used to retain archived backup files if the instance is released. Valid values: None: No archived backup files are retained. Last est : Only the last archived backup file is retained. All: All archived backup files are retained. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeBackupPolicy &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeBackupPolicyResponse>
  <Category>Standard</Category>
  <ArchiveBackupRetentionPeriod>0</ArchiveBackupRetentionPeriod>
  <RequestId>292884FE-D689-47A2-9829-C05E63366201</RequestId>
  <Duplication></Duplication>
  <ReleasedKeepPolicy>None</ReleasedKeepPolicy>
  <ArchiveBackupKeepPolicy>ByMonth</ArchiveBackupKeepPolicy>
  <PreferredBackupTime>00:00Z-01:00Z</PreferredBackupTime>
  <LocalLogRetentionHours>18</LocalLogRetentionHours>
  <PreferredNextBackupTime>2021-01-07T00:40Z</PreferredNextBackupTime>
  <DuplicationLocation>
        <Sotrage>OSS</Sotrage>
        <Location>
              <Endpoint></Endpoint>
              <Bucket></Bucket>
        </Location>
  </DuplicationLocation>
  <HighSpaceUsageProtection>Enable</HighSpaceUsageProtection>
  <CompressType>1</CompressType>
  <LogBackupFrequency>LogInterval</LogBackupFrequency>
  <PreferredBackupPeriod>Tuesday,Thursday,Saturday</PreferredBackupPeriod>
  <ArchiveBackupKeepCount>1</ArchiveBackupKeepCount>
  <LogBackupRetentionPeriod>7</LogBackupRetentionPeriod>
  <LogBackupLocalRetentionNumber>60</LogBackupLocalRetentionNumber>
  <BackupLog>Enable</BackupLog>
  <EnableBackupLog>1</EnableBackupLog>
  <SupportReleasedKeep>0</SupportReleasedKeep>
  <SupportVolumeShadowCopy>1</SupportVolumeShadowCopy>
  <LocalLogRetentionSpace>30</LocalLogRetentionSpace>
  <BackupRetentionPeriod>10</BackupRetentionPeriod>
  <DuplicationContent></DuplicationContent>
  <BackupInterval>30</BackupInterval>
</DescribeBackupPolicyResponse>
```

`JSON` format `{`

```json
    "Category": "Standard",
    "ArchiveBackupRetentionPeriod": 0,
    "RequestId": "292884FE-D689-47A2-9829-C05E63366201",
    "Duplication": "",
    "ReleasedKeepPolicy": "None",
    "ArchiveBackupKeepPolicy": "ByMonth",
    "PreferredBackupTime": "00:00Z-01:00Z",
    "LocalLogRetentionHours": "18",
    "PreferredNextBackupTime": "2021-01-07T00:40Z",
    "DuplicationLocation": {
        "Sotrage": "OSS",
        "Location": {
            "Endpoint": "",
            "Bucket": ""
```

`}` `},`

```json
    "HighSpaceUsageProtection": "Enable",
    "CompressType": "1",
    "LogBackupFrequency": "LogInterval",
    "PreferredBackupPeriod": "Tuesday,Thursday,Saturday",
    "ArchiveBackupKeepCount": 1,
    "LogBackupRetentionPeriod": "7",
    "LogBackupLocalRetentionNumber": 60,
    "BackupLog": "Enable",
    "EnableBackupLog": "1",
    "SupportReleasedKeep": 0,
    "SupportVolumeShadowCopy": 1,
    "LocalLogRetentionSpace": "30",
    "BackupRetentionPeriod": 10,
    "DuplicationContent": "",
    "BackupInterval": "30"
```

`}`

#### 2.7.5 ModifyBackupPolicy

Modifies the backup settings of an ApsaraDB RDS instance. Before you call this operation, make sure that the following requirements are met: The instance is not a read-only instance. The instance is in the running state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyBackupPoli cy | The operation that you want to perform. Set the value to Modif yBackupPolicy. |

| Developer Guide·API r | eference |   |   | ApsaraDB for RD |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| BackupPolicyMod e | String | No | DataBackupPolicy | The type of backup that you want to perform for the instance. Valid values: Dat aBackupPolicy: data backup LogBackupPolicy: log backup |
| PreferredBackupT ime | String | No | 00:00Z-01:00Z | The time to execute the backup task. Specify the time in the ISO 8601 standard in the HH:mmZ-HH:mmZ format. The time must be in UTC. Not e This parameter is required when you set the BackupPolicyMode parameter to Dat aBackupPolicy. This parameter is valid only when you set the BackupPolicyMode parameter to Dat aBackupPolicy. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PreferredBackupP eriod | String | No | Monday | The cycle based on which you want to perform backups. Specify at least two days of the week and separate these days with commas (,). Valid values: Monday T uesday Wednesday T hursday Friday Sat urday Sunday Not e A backup policy is specified by this parameter and the BackupInt erval parameter. For example, if you set this parameter to Saturday,Sunday and the BackupInt erval parameter to 30, a backup is performed once every 30 minutes on every Saturday and Sunday. This parameter is required when you set the BackupPolicyMode parameter to Dat aBackupPolicy. This parameter is valid only when you set the BackupPolicyMode parameter to Dat aBackupPolicy. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| BackupRetentionP eriod | String | No | 7 | The number of days for which you want to retain data backup files. Valid values: 7 t o 730. Not e This parameter is required when you set the BackupPolicyMode parameter to Dat aBackupPolicy. This parameter is valid only when you set the BackupPolicyMode parameter to Dat aBackupPolicy. |
| BackupLog | String | No | Enable | Specifies whether to enable log backup. Valid values: Enable Disabled Not e This parameter is required when you set the BackupPolicyMode parameter to Dat aBackupPolicy. This parameter is valid only when you set the BackupPolicyMode parameter to Dat aBackupPolicy. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| LogBackupRetenti onPeriod | String | No | 7 | The number of days for which you want to retain log backup files. Valid values: 7 t o 730. The log backup retention period cannot be longer than the data backup retention period. Not e If you enable the log backup feature, you can specify the log backup retention period. This applies only when the instance runs MySQL or PostgreSQL. This parameter is valid when you set the BackupPolicyMode parameter to Dat aBackupPolicy or LogBackupPolicy. |
| EnableBackupLog | String | No | 1 | Specifies whether to enable log backup. Valid values: T rue or 1: enables log backup. False or 0: disables log backup. Not e This parameter is required when you set the BackupPolicyMode parameter to LogBackupPolicy. This parameter is valid only when you set the BackupPolicyMode parameter to LogBackupPolicy. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| LocalLogRetentio nHours | String | No | 18 | The number of hours for which you want to retain log backup files on the instance. Valid values: 0 t o 7 × 24. The value 0 specifies not to retain log backup files on the instance. Not e This parameter is required when you set the BackupPolicyMode parameter to LogBackupPolicy. This parameter is valid only when you set the BackupPolicyMode parameter to LogBackupPolicy. |
| LocalLogRetentio nSpace | String | No | 30 | The maximum storage usage that is allowed for log backup files on the instance. If the storage usage for log backup files exceeds the value of this parameter, ApsaraDB RDS deletes earlier log backup files until the storage usage falls below the value of this parameter. Valid values: 0 t o 50. You can retain the default value. Not e This parameter is required when you set the BackupPolicyMode parameter to LogBackupPolicy. This parameter is valid only when you set the BackupPolicyMode parameter to LogBackupPolicy. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HighSpaceUsageP rotection | String | No | Enable | Specifies whether to forcibly delete log backup files when the storage usage of the instance exceeds 80% or the remaining storage space is less than 5 GB. Valid values: Enable and Disable. You can retain the default value. Not e This parameter is required when you set the BackupPolicyMode parameter to LogBackupPolicy. This parameter is valid only when you set the BackupPolicyMode parameter to LogBackupPolicy. |
| Duplication | String | No | None | An invalid parameter. |
| DuplicationConte nt | String | No | None | An invalid parameter. |
| DuplicationLocati on | String | No | None | An invalid parameter. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| LogBackupFreque ncy | String | No | LogInterval | The frequency at which you want to perform log backups. Valid values: LogInt erval: performs log backups every 30 minutes. Default value: same as the data backup frequency. Not e The value LogInt erval is supported only when the instance runs SQL Server. This parameter is valid only when you set the BackupPolicyMode parameter to Dat aBackupPolicy. |
| CompressType | String | No | 4 | The format that is used to compress backups. Valid values: 1: The zlib tool is used to compress backups into .tar.gz files. 4: The QuickLZ tool is used to compress data into .xb.gz files. This compression format is supported only when the instance runs MySQL 5.6 or 5.7. Backup files in this compression format can be used to restore individual databases or tables. 8: The QuickLZ tool is used to compress data into .xb.gz files. This compression format is supported only when the instance runs MySQL 8.0. This compression format cannot be used to restore individual databases or tables. Not e This parameter is valid only when you set the BackupPolicyMode parameter to Dat aBackupPolicy. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ReleasedKeepPoli cy | String | No | None | The policy that is used to retain archived backup files if the instance is released. Default value: None. Valid values: None: No archived backup files are retained. Last est : Only the last archived backup file is retained. All:: All archived backup files are retained. Not e This parameter is valid only when you set the BackupPolicyMode parameter to Dat aBackupPolicy. |
| LogBackupLocalR etentionNumber | Integer | No | 60 | The number of log backup files that you want to retain on the instance. Default value: 60. Valid values: 6 to 100. Not e This parameter is valid only when you set the BackupPolicyMode parameter to LogBackupPolicy. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| CompressType | String | 4 | The format that is used to compress backups. Valid values: 0: Backups are not compressed. 1: Backups are compressed by using the zlib tool. 2: Backups are compressed in parallel by using the zlib tool. 4: Backups are compressed by using the QuickLZ tool and can be used to restore individual databases or tables. 8: Backups are compressed by using the QuickLZ tool but cannot be used to restore individual databases or tables. This value is supported only when the instance runs MySQL 8.0. |
| DBInstanceID | String | rm-uf6wjk5xxxxxxx | The ID of the instance. |
| EnableBackupL og | String | 1 | Indicates whether log backup is enabled. Valid values: 1: Log backup is enabled. 0: Log backup is disabled. |
| HighSpaceUsag eProtection | String | Disable | Indicates whether log backup files are forcibly deleted when the storage usage of the instance exceeds 80% or the remaining storage space is less than 5 GB. |
| LocalLogRetent ionHours | Integer | 18 | The number of hours for which log backup files are retained on the instance. |
| LocalLogRetent ionSpace | String | 30 | The maximum storage usage for log backup files on the instance. |
| LogBackupLoca lRetentionNum ber | Integer | 60 | The number of log backup files that are retained on the instance. |
| RequestId | String | DA147739-AEAD- 4417-9089- 65E9B1D8240D | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ModifyBackupPolicy &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyBackupPolicyResponse>
        <HighSpaceUsageProtection>Disable</HighSpaceUsageProtection>
      <DBInstanceID>rm-bp1z3xxxxx</DBInstanceID>
      <RequestId>E4BF5598-ED12-4406-AAA4-F375428BE741</RequestId>
      <LocalLogRetentionHours>18</LocalLogRetentionHours>
      <EnableBackupLog>1</EnableBackupLog>
      <LocalLogRetentionSpace>30</LocalLogRetentionSpace>
      <LogBackupLocalRetentionNumber>60</LogBackupLocalRetentionNumber>
</ModifyBackupPolicyResponse>
```

`JSON` format `{`

```json
    "HighSpaceUsageProtection": "Disable",
    "DBInstanceID": "rm-bp1z3xxxxx",
    "RequestId": "E4BF5598-ED12-4406-AAA4-F375428BE741",
    "LocalLogRetentionHours": "18",
    "EnableBackupLog": "1",
    "LocalLogRetentionSpace": "30",
    "LogBackupLocalRetentionNumber": 60
```

`}`

#### 2.7.6 DeleteBackup

Deletes backup sets of an ApsaraDB RDS instance. Backup sets of only the instance itself are deleted. Backup sets of the associated instances such as read-only, disaster recovery, and cloned instances are not deleted. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance is of the High-availability Edition and runs MySQL or PostgreSQL. If the log backup feature is disabled, ApsaraDB RDS instances cannot be restored by point in time. You can delete data backup sets that are retained for more than seven days. If the log backup feature is enabled and the retention period of log backups is shorter than the retention period of data backups, the data backup sets that are retained for longer than the retention period of log backups can be deleted. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteBackup | The operation that you want to perform. Set the value to Delet eBackup. |
| BackupId | String | Yes | 324909958 | The ID of the backup set. You can call the DescribeBackups operation to query the IDs of backup sets. Up to 100 IDs can be specified in a single request. Separate multiple IDs with commas (,). Not e Only the backup sets whose St oreSt at us is Enabled when you call the DescribeBackups operation can be deleted. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 37441409-FFD1- 40AA-8EC5- 9ECF5E2F7C29 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DeleteBackup &DBInstanceId=rm-uf6wjk5xxxxxxx &BackupId=324909958 &<Common request parameters>
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

#### 2.7.7 DeleteBackupFile

Deletes backup sets of an ApsaraDB RDS for SQL Server instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteBackupFile | The operation that you want to perform. Set the value to Delet eBackupFile. |
| DBInstanceId | String | Yes | rm- bp6wjk5xxxxxx | The ID of the instance. |
| RegionId | String | No | cn-hangzhou | The region ID of the instance. Not e You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| BackupId | String | No | 293044600 | The ID of the backup set. You can specify up to 100 backup set IDs. Separate multiple backup set IDs with commas (,). Not e For ApsaraDB RDS for SQL Server instances, you can specify backup set IDs only for individual databases. You can call the DescribeBackups operation to query the IDs of backup sets. |
| DBName | String | No | testdb | The name of the database. |
| BackupTime | String | No | 2011-06- 11T16:00:00Z | The point in time before which the backup sets that you want to delete are created. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DeletedBaksetI ds | Integer | 293044600 | The IDs of the deleted backup sets. |
| RequestId | String | C7B3A91C-0ACD- 4948-ACAE- xxxxxxxD4069 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DeleteBackupFile &DBInstanceId=rm-bp6wjk5xxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>C7B3A91C-0ACD-4948-ACAE-xxxxxxxD4069</RequestId> <DeletedBaksetIds>
    <DeletedBaksetIds>1111</DeletedBaksetIds>
</DeletedBaksetIds>
```

`JSON` format

```json
{"RequestId":"C7B3A91C-0ACD-4948-ACAE-xxxxxxxD4069","DeletedBaksetIds":{"DeletedBaksetIds": "1111"}}
```

#### 2.7.8 DescribeBackupTasks

Queries the backup tasks of an ApsaraDB RDS instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackupT asks | The operation that you want to perform. Set the value to DescribeBackupT asks. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| Flag | String | No | None | A hidden parameter. |
| BackupJobId | String | No | 4762614 | The ID of the backup task. |

| Developer Guide·API r | eference |   |   | ApsaraDB for RD |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| BackupMode | String | No | Automated | The backup mode. Valid values: Aut omat ed Manual |
| BackupJobStatus | String | No | NoStart | The state of the backup task. Valid values: NoSt art Progressing By default, this operation returns backup tasks in both states. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | Array of BackupJob |   | Details of the backup tasks. |
| BackupJob |   |   |   |
| BackupId | String | 346650271 | The ID of the backup set that is generated by the backup task. Not e You can obtain the ID of the backup set only if you specify the BackupJobId parameter after the value of Finished is returned for the BackupSt at us parameter. |
| BackupJobId | String | 4762614 | The ID of the backup task. |
| BackupProgress Status | String | NoStart | The state of the backup program. Valid values: NoSt art Preparing Wait ing Uploading Checking Finished |

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupStatus | String | NoStart | The state of the backup task. Valid values: NoSt art Checking Preparing Wait ing Uploading Finished Failed Not e This parameter is returned only when a backup task is executed. |
| JobMode | String | Automated | The backup mode. Valid values: Aut omat ed Manual |
| Process | String | 25 | The progress of the backup task in percentage. |
| TaskAction | String | NormalBackupTask | The type of the backup task. Valid values: T empBackupT ask: temporary backup task NormalBackupT ask: regular backup task |
| RequestId | String | 90496720-2319- 42A8-87CD- FCE4DF95EBED | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeBackupTasks &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeBackupTasksResponse>
      <Items>
            <BackupJob>
                  <JobMode>Automated</JobMode>
                  <BackupProgressStatus>NoStart</BackupProgressStatus>
                  <TaskAction>NormalBackupTask</TaskAction>
                  <BackupStatus>NoStart</BackupStatus>
                  <BackupJobId>4762614</BackupJobId>
            </BackupJob>
      </Items>
      <RequestId>90496720-2319-42A8-87CD-FCE4DF95EBED</RequestId>
</DescribeBackupTasksResponse>
```

`JSON` format `{`

```json
    "Items": {
        "BackupJob": [
```

`{`

```json
                "JobMode": "Automated",
                "BackupProgressStatus": "NoStart",
                "TaskAction": "NormalBackupTask",
                "BackupStatus": "NoStart",
                "BackupJobId": 4762614
```

`}` `]` `},`

```json
    "RequestId": "90496720-2319-42A8-87CD-FCE4DF95EBED"
```

`}`

#### 2.7.9 DescribeLogBackupFiles

Queries the log backup files of an ApsaraDB RDS instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLogBack upFiles | The operation that you want to perform. Set the value to DescribeLogBackupFiles. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| EndTime | String | Yes | 2018-10- 31T08:40Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |
| StartTime | String | Yes | 2018-10- 01T08:40Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30 to 1000. Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | Array of BinLogFile |   | The log backup files. |
| BinLogFile |   |   |   |
| DownloadLink | String | http://rdsbak-hz- v3.oss-cn- hangzhou.aliyuncs.c om/xxxxx | The HTTP download URL. If the backup file cannot be downloaded, an empty string is returned. |
| FileSize | Long | 788480 | The size of the log backup file. Unit: byte. |
| IntranetDownlo adLink | String | http://rdsbak-hz- v3.oss-cn- hangzhou.aliyuncs.c om/xxxxx | The URL that is used to download the log backup file over an internal network. If the backup file cannot be downloaded, an empty string is returned. This URL is valid for 1 hour. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| LinkExpiredTim e | String | 2019-03- 01T15:04:13Z | The expiration time of the URL. The time follows the ISO 8601 standard in the yyyy- MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| LogBeginTime | String | 2018-10-31T08:40Z | The start time of the log backup file. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. |
| LogEndTime | String | 2018-10-31T08:40Z | The end time of the log backup file. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCou nt | Integer | 100 | The number of log backup files on the current page. |
| RequestId | String | F8EC669C-FC85- 43D7-AF06- C3641626B37E | The ID of the request. |
| TotalFileSize | Long | 2300 | The total size of log backup files. Unit: byte. |
| TotalRecordCo unt | Integer | 17 | The total number of log backup files. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeLogBackupFiles &DBInstanceId=rm-uf6wjk5xxxxxxx &StartTime=2018-10-01T08:40Z &EndTime=2018-10-31T08:40Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeLogBackupFilesResponse>
      <Items></Items>
      <PageNumber>1</PageNumber>
      <TotalRecordCount>0</TotalRecordCount>
      <RequestId>F8EC669C-FC85-43D7-AF06-C3641626B37E</RequestId>
      <PageRecordCount>0</PageRecordCount>
</DescribeLogBackupFilesResponse>
```

`JSON` format `{`

```json
    "Items": {
        "BinLogFile": [ ]
```

`},`

```json
    "PageNumber": 1,
    "TotalRecordCount": 0,
    "RequestId": "F8EC669C-FC85-43D7-AF06-C3641626B37E",
    "PageRecordCount": 0
```

`}`

#### 2.7.10 DescribeMetaList

Queries the information of the restorable databases and tables in a specific backup set. Before you call the RestoreTable operation to restore individual databases or tables of an ApsaraDB RDS for MySQL instance, you can call this operation to query the information of the restorable databases and tables. This operation is supported only for instances that run MySQL 8.0, MySQL 5.7, or MySQL 5.6 on RDS High-availability Edition with local SSDs. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMetaList | The operation that you want to perform. Set the value to DescribeMet aList . |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| RestoreType | String | No | BackupSetID | The method that is used to restore data. Valid values: BackupSet ID: Data is restored from a backup set. If you use this value, you must also specify the BackupSet ID parameter. Rest oreT ime: Data is restored to a specific point in time. If you use this value, you must also specify the Rest oreT ime parameter. Default value: BackupSet ID. |
| BackupSetID | String | No | 14358 | The ID of the backup set from which you want to restore data. You can call the DescribeBackups operation to query the IDs of backup sets. Not e This parameter is required when you set the Rest oreT ype parameter to BackupSet ID. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RestoreTime | String | No | 2019-05- 30T03:29:10Z | The point in time to which you want to restore data. The specified point in time must be earlier than the current time. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. You can call the DescribeBackups operation to query the restorable time range. Not e This parameter is required when you set the Rest oreT ype parameter to Rest oreT ime. |
| GetDbName | String | No | testdb1 | The name of the database to query. ApsaraDB RDS implements exact match based on the value of this parameter and returns the name of the matched database and the names of all tables contained in the database. Not e If you leave this parameter unspecified, ApsaraDB RDS returns all databases that are created on the instance. |
| Pattern | String | No | test | The keyword in the name of the database to query. ApsaraDB RDS implements fuzzy match based on the value of this parameter and returns only the names of the matched databases. Not e For example, if you set the value to test , ApsaraDB RDS returns testdb1 and testdb2 . Then, you can specify the Get DbName parameter to query tables in the required database. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageSize | String | No | 1 | The number of entries to return on each page. Default value: 1. Not e This parameter is valid only when you specify the PageIndex parameter. |
| PageIndex | String | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. Not e This parameter is valid only when you specify the PageSize parameter. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceNam e | String | rm-uf6wjk5xxxxxxx | The name of the instance. |
| Items | Array of Meta |   | The information of the databases and tables contained in the backup set. |
| Meta |   |   |   |
| Database | String | testdb1 | The name of the database. |
| Size | String | 64 | The size of the tables. Unit: KB. |
| Tables | String | test1 | The names of the tables. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCou nt | Integer | 1 | The number of entries returned on the current page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 60F9A12A-16B8- 4728-B099- 4CA38D32C31C | The ID of the request. |
| TotalPageCoun t | Integer | 1 | The total number of pages returned. |
| TotalRecordCo unt | Integer | 1 | The total number of entries returned. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeMetaList &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeMetaList>
      <TotalPageCount>1</TotalPageCount>
      <TotalRecordCount>1</TotalRecordCount>
      <PageRecordCount>1</PageRecordCount>
      <RequestId>60F9A12A-16B8-4728-B099-4CA38D32C31C</RequestId>
      <PageNumber>1</PageNumber>
      <Items>
            <Meta>
                  <Size>64</Size>
                  <Database>testdb1</Database>
                  <Tables>test1</Tables>
            </Meta>
      </Items>
      <DBInstanceName>rm-uf6wjk5xxxxxxx</DBInstanceName>
</DescribeMetaList>
```

`JSON` format `{`

```json
    "TotalPageCount": "1",
    "TotalRecordCount": "1",
    "PageRecordCount": "1",
    "RequestId": "60F9A12A-16B8-4728-B099-4CA38D32C31C",
    "PageNumber": "1",
    "Items": {
        "Meta": [{
            "Size": "64",
            "Database": "testdb1",
            "Tables": "test1"
```

`}]` `},`

```json
    "DBInstanceName": "rm-uf6wjk5xxxxxxx"
```

`}`

#### 2.7.11 RestoreTable

Restores individual databases or tables for an ApsaraDB RDS instance. ApsaraDB RDS for MySQL allows you to restore individual databases or tables. If one or more databases or tables of an ApsaraDB RDS instance are accidentally deleted, you can use a backup set to restore the databases or tables. For more information, see Restore individual databases and tables for an ApsaraDB RDS for MySQL instance. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance does not have ongoing migration tasks. If you want to restore data to a specific point in time, the log backup feature is enabled for the instance. The restoration of individual databases or tables is enabled, and new backups are created. The instance does not contain tables that have the same names as the new tables. This operation is supported only for instances that run MySQL. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RestoreTable | The operation that you want to perform. Set the value to Rest oreT able. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxxxx x | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |

| A | psaraDB for RDS |   |   |   | Developer Guide·API referenc | e |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| BackupId | String | No | 9026262 | The ID of the backup set. You can call the DescribeBackups operation to obtain the IDs of backup sets. Not e You must specify at least one of BackupId and Rest oreT ime. |
| RestoreTime | String | No | 2011-06- 11T16:00:00Z | The point in time to which you want to restore databases within the backup retention period. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. Not e You must specify at least one of BackupId and Rest oreT ime. The log backup feature must be enabled. |
|   |   |   |   | The databases and tables that you want to restore. Format: |

| Parameter | Type | Required | Example |   | De[s{c"rtipytpioen":"db","name":"<The name of Database 1 on the |   |
|---|---|---|---|---|---|---|
| TableMeta | String | No | [{"type":"db","na me":"testdb1","n ewname":"testd b1 new","tables" _ : [{"type":"table"," name":"testdb1t able1","newname ":"testdb1table1 new"}]}] _ | source instance>","newname":" <The name of Database 1 on the destination instance>","tables": [{"type":"table","name":"<The name of Table 1 in Database 1 on the source instance>","newname":"<The name of Table 1 in Database 1 on the destination instance>"}, {"type":"table","name":"<The name of Table 2 in Database 1 on the source instance>","newname":"<The name of Table 2 in Database 1 on the destination instance>"}]}, {"type":"db","name":"<The name of Database 2 on the source instance>","newname":" <The name of Database 2 on the destination instance>","tables": [{"type":"table","name":"<The name of Table 3 in Database 2 on the source instance>","newname":"<The name of Table 3 in Database 2 on the destination instance>"}, {"type":"table","name":"<The name of Table 4 in Database 2 on the source instance>","newname":"<The name of Table 4 in Database 2 on the destination instance>"}]}] | source instance>","newname":" <The name of Database 1 on the destination instance>","tables": [{"type":"table","name":"<The name of Table 1 in Database 1 on the source instance>","newname":"<The name of Table 1 in Database 1 on the destination instance>"}, {"type":"table","name":"<The name of Table 2 in Database 1 on the source instance>","newname":"<The name of Table 2 in Database 1 on the destination instance>"}]}, {"type":"db","name":"<The name of Database 2 on the source instance>","newname":" <The name of Database 2 on the destination instance>","tables": [{"type":"table","name":"<The name of Table 3 in Database 2 on the source instance>","newname":"<The name of Table 3 in Database 2 on the destination instance>"}, {"type":"table","name":"<The name of Table 4 in Database 2 on the source instance>","newname":"<The name of Table 4 in Database 2 on the destination instance>"}]}] |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | EA2D4F34-01A7- 46EB-A339- D80882135206 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=RestoreTable &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &RestoreTime=2019-08-20T16:00:00Z &TableMeta=[{"type":"db","name":"dtstestdata","newname":"dtstestdata","tables":[{"type":"ta ble","name":"customer_old","newname":"customer_old123"},{"type":"table","name":"order","new name":"order123"}]}] &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RestoreTableResponse>
  <RequestId>EA2D4F34-01A7-46EB-A339-D80882135206</RequestId>
</RestoreTableResponse>
```

`JSON` format `{`

```json
    "RequestId": "EA2D4F34-01A7-46EB-A339-D80882135206"
```

`}`

#### 2.7.12 DescribeDetachedBackups

Queries the backup sets of an ApsaraDB RDS instance that is deleted. This operation is supported for instances that run MySQL and use local SSDs. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDetache dBackups | The operation that you want to perform. Set the value to DescribeDet achedBackups. |
| Region | String | Yes | cn-hangzhou | The region ID of the instance. |

| D | eveloper Guide·API r | eference |   |   | ApsaraDB for RD | S |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceId | String | No | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| BackupId | String | No | 327xxxxx3 | The ID of the backup set. |
| BackupLocation | String | No | cn-hangzhou | The region where the backup set resides. |
| BackupStatus | String | No | Success | The state of the backup set. Valid values: Success Failed |
| BackupMode | String | No | Automated | The backup mode. Valid values: Aut omat ed Manual |
| StartTime | String | No | 2021-03- 01T16:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. |
| EndTime | String | No | 2021-03- 15T16:00Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Default value: 30. Valid values: 30 50 100 |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |

| psaraDB for RDS |   |   |   | Developer Guide·API referenc |
|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Backup | Array of Items |   | Details of backup sets. |
| Items |   |   |   |
| BackupDBName s | String | testdb | The names of databases. |
| BackupDownlo adURL | String | http://rdsbak-hz- v3.oss-cn- hangzhou.aliyuncs.c om/xxxxx | The URL that is used to download the backup set over the Internet. If the backup set cannot be downloaded, an empty string is returned. |
| BackupEndTime | String | 2019-02- 13T12:20:00Z | The end time of the backup task. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. |
| BackupExtractio nStatus | String | None | The state of all backup sets. |
| BackupId | String | 327xxxxx3 | The ID of the backup set. |
| BackupIntranet DownloadURL | String | http://rdsbak-hz- v3.oss-cn- hangzhou- internal.aliyuncs.co m/xxxxx | The URL that is used to download the backup set over an internal network. If the backup set cannot be downloaded, an empty string is returned. |
| BackupLocation | String | cn-hangzhou | The region where the backup set resides. |
| BackupMethod | String | Physical | The method that is used to generate the backup set. Valid values: Logical Physical |

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupMode | String | Automated | The backup mode. Valid values: Aut omat ed Manual |
| BackupScale | String | None | The scalability of the backup set. |
| BackupSize | Long | 2167808 | The size of the backup set. Unit: byte. |
| BackupStartTim e | String | 2019-02- 03T12:20:00Z | The start time of the backup task. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. |
| BackupStatus | String | Success | The state of the backup set. |
| BackupType | String | FullBackup | The backup type. Valid values: FullBackup Increment alBackup |
| ConsistentTime | Long | 1576506856 | The point in time at which the data in the backup set is consistent. The value of this parameter is a timestamp. Not e This parameter is supported only for instances that run MySQL 5.6. If the instance does not run MySQL 5.6, the value 0 is returned. |
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | The ID of the instance. |
| HostInstanceId | String | 5882781 | The No. of the instance that generates the backup set. This parameter is used to indicate whether the instance that generates the backup set is a primary instance or a secondary instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| MetaStatus | String | OK | The state of the backup set that is used to restore individual databases or tables. Valid values: OK: The backup set is normal. LARGE: The backup set contains an abnormally large number of tables. It cannot be used to restore individual databases or tables. EMPT Y: The backup set is generated from a failed backup task. |
| SlaveStatus | String | None | The state of the secondary instance. |
| StoreStatus | String | Disabled | Indicates whether the backup set can be deleted. Valid values: Enabled: The backup set can be deleted. Disabled: The backup set cannot be deleted. |
| TotalBackupSiz e | Long | 2167808 | The size of all files in the backup set. Unit: byte. |
| PageNumber | String | 1 | The page number of the returned page. |
| PageRecordCou nt | String | 30 | The number of backup sets on the current page. |
| RequestId | String | 1A6D328C-84B8- 40DC-BF49- 6C73984D7494 | The ID of the request. |
| TotalBackupSiz e | Long | 2167808 | The size of all files in all backup sets. Unit: byte. |
| TotalRecordCo unt | String | 100 | The total number of entries returned. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeDetachedBackups &Region=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeDetachedBackupsResponse>
    <TotalRecordCount>1</TotalRecordCount>
    <PageRecordCount>1</PageRecordCount>
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
</DescribeDetachedBackupsResponse>
```

`JSON` format `{`

```json
    "TotalRecordCount": 1,
    "PageRecordCount": 1,
    "RequestId": "B0BBC25A-6B3E-4BFD-A052-48664294E20D",
    "PageNumber": 1,
    "Items": {
        "Backup": [
```

`{`

```json
          "BackupMethod":"Physical",
                    "BackupIntranetDownloadURL":"http://...",
                    "BackupMode":"Automated",
                    "BackupSize":9405440,
                    "BackupId":509538643,
                    "IsAvail":1,
                    "HostInstanceID":100453678,
                    "BackupDBNames":"",
                    "StoreStatus":"Enabled",
                    "DBInstanceId":"rm-uf6wjk5xxxxxxx",
                    "BackupDownloadURL":"https://...",
                    "BackupEndTime":"2020-09-04T02:55:36Z",
                    "BackupStartTime":"2020-09-04T02:54:04Z",
                    "ConsistentTime":"1599188049",
                    "BackupType":"FullBackup",
                    "MetaStatus":"OK",
                    "BackupScale":"DBInstance",
                    "BackupStatus":"Success",
                    "BackupLocation":"OSS"
```

`}` `]` `},`

```json
    "TotalBackupSize": "161061273600"
```

`}`

### 2.8 Database proxy

#### 2.8.1 CalculateDBInstanceWeight

Queries the read weights of a primary ApsaraDB RDS instance and its read-only instances. When the read/write splitting feature is enabled, this operation is used to calculate system-assigned read weights. For more information about custom read weights, see DescribeDBInstanceNetInfo. Before you call this operation, make sure that the following requirements are met: The shared proxy feature is enabled for the primary instance. The primary instance runs one of the following database engine versions and RDS editions: MySQL 5.7 on RDS High-availability Edition (with local SSDs) MySQL 5.6 SQL Server 2017 EE Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CalculateDBInstan ceWeight | The operation that you want to perform. Set the value to Calculat eDBInst anceWeight . |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the primary instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | Array of DBInstanceWeig ht |   | Details of the system-assigned read weights. |
| DBInstanceWeig ht |   |   |   |
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | The ID of the instance. |
| DBInstanceType | String | Master | The role of the instances. Valid values: Mast er: primary instance Readonly: read-only instance |
| Weight | String | 100 | The read weight that ApsaraDB RDS calculates in real time for the instance. |
| ReadonlyInstan ceSQLDelayedTi me | String | 30 | The latency of data replication to the read- only instances that are attached to the primary instance. The read-only instances replicate data from the primary instance at the latency that is specified by the ReadonlyInst anceSQLDelayedT ime parameter. Unit: seconds. |
| RequestId | String | C816A4BF-A6EC- 4722-95F9- 2055859CCFD2 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=CalculateDBInstanceWeight &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CalculateDBInstanceWeightResponse>
      <items>
            <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
            <DBInstanceType>Master</DBInstanceType>
            <Weight></Weight>
            <Availability></Availability>
      </items>
      <requestId>C816A4BF-A6EC-4722-95F9-2055859CCFD2</requestId>
</CalculateDBInstanceWeightResponse>
```

`JSON` format `{`

```json
    "items": [
```

`{`

```json
            "DBInstanceId": "rm-uf6wjk5xxxxxxx",
            "DBInstanceType": "Master",
            "Weight": "",
            "Availability": ""
```

`}` `],`

```json
    "requestId": "C816A4BF-A6EC-4722-95F9-2055859CCFD2"
```

`}`

#### 2.8.2 DescribeDBInstanceProxyConfiguration

Queries the shared proxy settings on an ApsaraDB RDS instance. This operation is used to query the original shared proxy settings rather than the latest dedicated proxy settings. For more information about how to query the dedicated proxy settings, see DescribeDBProxy. Before you call this operation, make sure that the following requirements are met: The shared proxy feature is enabled for the instance. The read/write splitting feature is enabled for the instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstan ceProxyConfigura tion | The operation that you want to perform. Set the value to DescribeDBInst anceProxyConf igura t ion. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxxxx x | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| AttacksProtecti onConfiguratio n | String | {\"check interval se _ _ conds\":\"0\",\"ma x failed login atte _ _ _ mpts\":\"0\",\"bloc king seconds\":\"0\ _ ",\"status\":\"Disabl e\"} | Indicates whether the mechanism that is used to prevent brute-force attacks is enabled. Valid values: Enable Disable The return value is a JSON string. Example: {"status":"Disable", "check interval seconds": 60, _ _ "max failed login attempts": 60, _ _ _ "blocking seconds": 600} _ Description: Each client allows {max failed login attempts} logon _ _ _ attempts that fail due to incorrect passwords within {check interval seconds} _ _ seconds. If one more such attempt is conducted, the client must wait {blocking seconds} seconds before you _ can try again. Valid values: check interval seconds: 30 t o 600. _ _ Unit: seconds. max failed login attempts: 10 t o _ _ _ 5000. blocking seconds: 30 t o 3600. Unit: _ seconds. |
| PersistentConn ectionsConfigur ation | String | {\"status\":\"Disabl e\"} | Indicates whether the short-lived connection optimization feature is enabled. Valid values: Enable Disable The return value is a JSON string. Example: {"status":"Disable"}. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| TransparentSwi tchConfiguratio n | String | {\"status\":\"Enable \"} | Indicates whether the transparent switchover feature is enabled. Valid values: Enable Disable The return value is a JSON string. Example: {"status":"Enable"}. |
| RequestId | String | E9DD55F4-1A5F- 48CA-BA57- DFB3CA8C4C34 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?DBInstanceId=rm-uf6wjk5xxxxxxxxxx &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeDBInstanceProxyConfigurationResponse>
      <PersistentConnectionsConfiguration>{"status":"Disable"}</PersistentConnectionsConfig
uration>
      <TransparentSwitchConfiguration>{"status":"Enable"}</TransparentSwitchConfiguration>
      <AttacksProtectionConfiguration>{"check_interval_seconds":"0","max_failed_login_attem
pts":"0","blocking_seconds":"0","status":"Disable"}</AttacksProtectionConfiguration>
      <RequestId>E9DD55F4-1A5F-48CA-BA57-DFB3CA8C4C34</RequestId>
</DescribeDBInstanceProxyConfigurationResponse>
```

`JSON` format `{`

```json
    "PersistentConnectionsConfiguration": "{\"status\":\"Disable\"}",
    "TransparentSwitchConfiguration": "{\"status\":\"Enable\"}",
    "AttacksProtectionConfiguration": "{\"check_interval_seconds\":\"0\",\"max_failed_login
_attempts\":\"0\",\"blocking_seconds\":\"0\",\"status\":\"Disable\"}",
    "RequestId": "E9DD55F4-1A5F-48CA-BA57-DFB3CA8C4C34"
```

`}`

#### 2.8.3 DescribeDBProxy

Queries the details of the dedicated proxy of an ApsaraDB RDS instance. ApsaraDB RDS provides the dedicated proxy feature to deliver capabilities such as read/write splitting and short-lived connection optimization. Before you call this operation, make sure that the instance runs one of the following database engine versions and RDS editions: MySQL 8.0 on RDS Enterprise Edition (minor version of 20191204 or later) MySQL 8.0 on RDS High-availability Edition (minor version of 20190915 or later) MySQL 5.7 on RDS Enterprise Edition (minor version of 20191128 or later) MySQL 5.7 on RDS High-availability Edition (minor version of 20190925 or later) MySQL 5.6 on RDS High-availability Edition (minor version of 20200229 or later) Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBProxy | The operation that you want to perform. Set the value to DescribeDBProxy. |
| DBInstanceId | String | Yes | rm- bp1ja4f56s7us*** * | The ID of the instance. |
| RegionId | String | No | cn-hangzhou | The region ID of the instance. You can call the DescribeRegions operation to query the most recent region list. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBProxyConnec tStringItems | Array of DBProxyConnec tStringItems |   | Details of the configured proxy endpoints. |
| DBProxyConnec tStringItems |   |   |   |
| DBProxyConnec tString | String | gos787jog2wk0ye1* ***- rw4rm.rwlb.rds.aliyu ncs.com | The endpoint of the proxy terminal. |
| DBProxyConnec tStringNetType | String | InnerString | The network type of the proxy endpoint. Valid values: InnerSt ring: internal network Out erSt ring: Internet |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBProxyConnec tStringNetWork Type | String | 1 | The network type of the proxy endpoint. Valid values: 0: Internet 1: classic network 2: VPC |
| DBProxyConnec tStringPort | String | 3306 | The port that is used to connect to the proxy endpoint. |
| DBProxyEndpoi ntId | String | 20**** | The ID of the proxy terminal to which the proxy endpoint belongs. |
| DBProxyEndpoi ntName | String | gos787jog2wk0ye1* *** | The name of the proxy terminal to which the proxy endpoint belongs. |
| DBProxyVpcInst anceId | String | rm- bp145737x5****1311 61274792**** | The ID of the proxy instance. |
| DBProxyInstanc eCurrentMinorV ersion | String | 1.13.11 | The dedicated proxy version that is running on the instance. |
| DBProxyInstanc eLatestMinorVe rsion | String | 1.13.12 | The latest dedicated proxy version that is available to the instance. |
| DBProxyInstanc eNum | Integer | 1 | The number of proxy instances that are enabled on the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBProxyInstanc eStatus | String | Running | The state of the proxy instance. Valid values: CREAT ING: The proxy instance is being created. ACT IVAT ION: The proxy instance is running. DELET ING: The proxy instance is being deleted. REST ART ING: The proxy instance is restarting. CLASS CHANGING: The specifications of _ the proxy instance are being changed. T RANSING: The proxy instance is being migrated. MINOR VERSION UPGRADING: The _ _ minor version of the proxy instance is being updated. |
| DBProxyInstanc eType | String | 2 | The type of the proxy enabled on the instance. Valid values: 1: shared proxy 2: dedicated proxy |
| DBProxyService Status | String | Startup | The state of the dedicated proxy feature. St art up: enabled Shut down: disabled |
| RequestId | String | 909A69EE-71C8- 4417-A0B9- FF085407E1E3 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeDBProxy &DBInstanceId=rm-bp1ja4f56s7us**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeDBProxyResponse>
      <DBProxyInstanceName>gos787jog2wk0ye1****</DBProxyInstanceName>
      <DBProxyInstanceCurrentMinorVersion>1.13.11</DBProxyInstanceCurrentMinorVersion>
      <DBProxyServiceStatus>Startup</DBProxyServiceStatus>
      <DBProxyInstanceNum>1</DBProxyInstanceNum>
      <DBProxyInstanceLatestMinorVersion>1.13.12</DBProxyInstanceLatestMinorVersion>
      <RequestId>909A69EE-71C8-4417-A0B9-FF085407E1E3</RequestId>
      <DbProxyEndpointItems>
            <DbProxyEndpointItems>
                  <DbProxyEndpointName>gos787jog2wk0ye1****</DbProxyEndpointName>
                  <DbProxyEndpointAliases>proxy-test</DbProxyEndpointAliases>
                  <DbProxyEndpointType>RWSplit</DbProxyEndpointType>
                  <DbProxyReadWriteMode>ReadWrite</DbProxyReadWriteMode>
            </DbProxyEndpointItems>
      </DbProxyEndpointItems>
      <DBProxyConnectStringItems>
            <DBProxyConnectStringItems>
                  <DBProxyConnectString>gos787jog2wk0ye1****-rw4rm.rwlb.rds.aliyuncs.com</D
BProxyConnectString>
                  <DBProxyEndpointId>209090</DBProxyEndpointId>
                  <DBProxyEndpointName>gos787jog2wk0ye1****</DBProxyEndpointName>
                  <DBProxyConnectStringNetWorkType>2</DBProxyConnectStringNetWorkType>
                  <DBProxyConnectStringNetType>InnerString</DBProxyConnectStringNetType>
                  <DBProxyConnectStringPort>3306</DBProxyConnectStringPort>
                  <DBProxyVpcInstanceId>rm-bp145737x5****131161274792****</DBProxyVpcInstan
ceId>
            </DBProxyConnectStringItems>
      </DBProxyConnectStringItems>
      <DBProxyInstanceStatus>Running</DBProxyInstanceStatus>
      <DBProxyInstanceType>2</DBProxyInstanceType>
</DescribeDBProxyResponse>
```

`JSON` format `{`

```json
    "DBProxyInstanceName": "gos787jog2wk0ye1****",
    "DBProxyInstanceCurrentMinorVersion": "1.13.11",
    "DBProxyServiceStatus": "Startup",
    "DBProxyInstanceNum": 1,
    "DBProxyInstanceLatestMinorVersion": "1.13.12",
    "RequestId": "909A69EE-71C8-4417-A0B9-FF085407E1E3",
    "DbProxyEndpointItems": {
        "DbProxyEndpointItems": [
```

`{`

```json
                "DbProxyEndpointName": "gos787jog2wk0ye1****",
                "DbProxyEndpointAliases": "proxy-test",
                "DbProxyEndpointType": "RWSplit",
                "DbProxyReadWriteMode": "ReadWrite"
```

`}` `]` `},`

```json
    "DBProxyConnectStringItems": {
        "DBProxyConnectStringItems": [
```

`{`

```json
                "DBProxyConnectString": "gos787jog2wk0ye1****-rw4rm.rwlb.rds.aliyuncs.com",
                "DBProxyEndpointId": 209090,
                "DBProxyEndpointName": "gos787jog2wk0ye1****",
                "DBProxyConnectStringNetWorkType": 2,
                "DBProxyConnectStringNetType": "InnerString",
                "DBProxyConnectStringPort": "3306",
                "DBProxyVpcInstanceId": "rm-bp145737x5****131161274792****"
```

`}` `]` `},`

```json
    "DBProxyInstanceStatus": "Running",
    "DBProxyInstanceType": "2"
```

`}`

#### 2.8.4 DescribeDBProxyEndpoint

Queries the dedicated proxy endpoint of an ApsaraDB RDS instance. ApsaraDB RDS provides the dedicated proxy feature to deliver capabilities such as read/write splitting and short-lived connection optimization. Before you call this operation, make sure that the instance runs one of the following database engine versions and RDS editions: MySQL 8.0 on RDS Enterprise Edition (minor version of 20191204 or later) MySQL 8.0 on RDS High-availability Edition (minor version of 20190915 or later) MySQL 5.7 on RDS Enterprise Edition (minor version of 20191128 or later) MySQL 5.7 on RDS High-availability Edition (minor version of 20190925 or later) MySQL 5.6 on RDS High-availability Edition (minor version of 20200229 or later) Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBProxyE ndpoint | The operation that you want to perform. Set the value to DescribeDBProxyEndpoint . |
| DBInstanceId | String | Yes | rm- bp1ja4f56s7us*** * | The ID of the instance. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. You can call the DescribeRegions operation to query the most recent region list. |
| DBProxyEndpointI d | String | No | keaxncrjluwu0gue **** | The name of the proxy terminal. |
| DBProxyConnectS tring | String | No | testproxy****.rwl b.rds.aliyuncs.co m | The proxy endpoint to query. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBProxyConnec tString | String | testproxy****.rwlb.r ds.aliyuncs.com | The proxy endpoint queried. |
| DBProxyConnec tStringNetType | String | InnerString | The network type of the proxy endpoint. Valid values: InnerSt ring: internal network Out erSt ring: Internet |
| DBProxyConnec tStringPort | String | 3306 | The port that is used to connect to the proxy endpoint. |
| DBProxyEndpoi ntId | String | keaxncrjluwu0gue*** * | The ID of the proxy endpoint. You can call this operation to query the ID of a proxy endpoint. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBProxyFeature s | String | TransactionReadSql RouteOptimizeStatu s:1;ConnectionPersi st:0;ReadWriteSpliti ng:1 | The configuration of the proxy terminal. The configuration is in the JSON format and contains the following parameters: T ransact ionReadSqlRout eOpt imizeSt at us: the status of the transaction splitting feature. Valid values: 0 and 1. The value 0 indicates that this feature is disabled. The value 1 indicates that this feature is enabled. Connect ionPersist : the status of the connection pool feature. Valid values: 0, 1, and 2. The value 0 indicates that this feature is disabled. The value 1 indicates that the session connection pool feature is enabled. The value 2 indicates that the transaction connection pool feature is enabled. ReadWrit eSplit ing: the status of the read/write splitting feature. Valid values: 0 and 1. The value 0 indicates that this feature is disabled. The value 1 indicates that this feature is enabled. |
| ReadOnlyInstan ceDistributionT ype | String | Standard | The policy that is used to assign read weights. Valid values: St andard: ApsaraDB RDS automatically assigns read weights to the primary and read-only instances based on the specifications of these instances. Cust om: You must manually assign read weights to the primary and read-only instances. |
| ReadOnlyInstan ceMaxDelayTim e | String | 30 | The latency threshold that is allowed for read/write splitting. If the latency on a read- only instance exceeds the specified threshold, ApsaraDB RDS no longer routes read requests to the read-only instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ReadOnlyInstan ceWeight | String | [{\"Availability\":\"A vailable\",\"DBInsta nceId\":\"rr- bp176984qewd8**** \",\"DBInstanceType \":\"ReadOnly\",\"W eight\":400}, {\"Availability\":\"Av ailable\",\"DBInstan ceId\":\"rm- bp1ja4f56s7us****\" ,\"DBInstanceType\" :\"Master\",\"Weigh t\":0}] | The read weights of the primary and read- only instances. The value of this parameter is in the JSON format and contains the following parameters: DBInst anceId: the ID of the instance. DBInst anceT ype: the role of the instance. Valid values: Mast er and ReadOnly. Weight : the read weight of the instance. The read weight must increase in increments of 100 and cannot exceed 10000. Not e If the primary instance is not attached with read-only instances, this operation returns null for this parameter. |
| RequestId | String | 847BA085-B377- 4BFA-8267- F82345ECE1D2 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeDBProxyEndpoint &DBInstanceId=rm-bp1ja4f56s7us**** &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeDBProxyEndpointResponse>
      <DbProxyEndpointReadWriteMode>ReadWrite</DbProxyEndpointReadWriteMode>
      <ReadOnlyInstanceDistributionType>Standard</ReadOnlyInstanceDistributionType>
      <DBProxyConnectString>testproxy****.rwlb.rds.aliyuncs.com</DBProxyConnectString>
      <RequestId>336E33D5-8C02-4265-9627-704BF9F3954B</RequestId>
      <DBProxyEndpointId>keaxncrjluwu0guehzae</DBProxyEndpointId>
      <DbProxyEndpointAliases>proxyterminal-test</DbProxyEndpointAliases>
      <DBProxyFeatures>TransactionReadSqlRouteOptimizeStatus:1;ConnectionPersist:0;ReadWrit
eSpliting:1;PinPreparedStmt:0</DBProxyFeatures>
      <ReadOnlyInstanceWeight>[{"Availability":"Available","DBInstanceId":"rr-bp176984qewd8
****","DBInstanceType":"ReadOnly","Weight":400},{"Availability":"Available","DBInstanceId":
"rm-bp1ja4f56s7us****","DBInstanceType":"Master","Weight":0}]</ReadOnlyInstanceWeight>
      <ReadOnlyInstanceMaxDelayTime>30</ReadOnlyInstanceMaxDelayTime>
      <DBProxyConnectStringNetType>InnerString</DBProxyConnectStringNetType>
      <EndpointConnectItems>
            <EndpointConnectItems>
                  <DbProxyEndpointNetType>2</DbProxyEndpointNetType>
                  <DbProxyEndpointPort>3306</DbProxyEndpointPort>
                  <DbProxyEndpointConnectString>testproxy****.rwlb.rds.aliyuncs.com</DbProx
yEndpointConnectString>
            </EndpointConnectItems>
            <EndpointConnectItems>
                  <DbProxyEndpointNetType>0</DbProxyEndpointNetType>
                  <DbProxyEndpointPort>3306</DbProxyEndpointPort>
                  <DbProxyEndpointConnectString>test****.rwlb.rds.aliyuncs.com</DbProxyEndp
ointConnectString>
            </EndpointConnectItems>
      </EndpointConnectItems>
      <DBProxyConnectStringPort>3306</DBProxyConnectStringPort>
</DescribeDBProxyEndpointResponse>
```

`JSON` format `{`

```json
    "DbProxyEndpointReadWriteMode": "ReadWrite",
    "ReadOnlyInstanceDistributionType": "Standard",
    "DBProxyConnectString": "testproxy****.rwlb.rds.aliyuncs.com",
    "RequestId": "336E33D5-8C02-4265-9627-704BF9F3954B",
    "DBProxyEndpointId": "keaxncrjluwu0guehzae",
    "DbProxyEndpointAliases": "proxyterminal-test",
    "DBProxyFeatures": "TransactionReadSqlRouteOptimizeStatus:1;ConnectionPersist:0;ReadWri
teSpliting:1;PinPreparedStmt:0",
    "ReadOnlyInstanceWeight": "[{\"Availability\":\"Available\",\"DBInstanceId\":\"rr-bp176
984qewd8****\",\"DBInstanceType\":\"ReadOnly\",\"Weight\":400},{\"Availability\":\"Availabl e\",\"DBInstanceId\":\"rm-bp1ja4f56s7us****\",\"DBInstanceType\":\"Master\",\"Weight\":0}]"
```

`,`

```json
    "ReadOnlyInstanceMaxDelayTime": "30",
    "DBProxyConnectStringNetType": "InnerString",
    "EndpointConnectItems": {
        "EndpointConnectItems": [
```

`{`

```json
                "DbProxyEndpointNetType": "2",
                "DbProxyEndpointPort": "3306",
                "DbProxyEndpointConnectString": "testproxy****.rwlb.rds.aliyuncs.com"
```

`},` `{`

```json
                "DbProxyEndpointNetType": "0",
                "DbProxyEndpointPort": "3306",
                "DbProxyEndpointConnectString": "test****.rwlb.rds.aliyuncs.com"
```

`}` `]` `},`

```json
    "DBProxyConnectStringPort": "3306"
```

`}` Error codes

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | Endpoint.NotFound | Specified endpoint is not found. | The error message returned because the port used to connect to the dedicated proxy endpoint is not found. |

#### 2.8.5 DescribeDBProxyPerformance

Queries the performance data of the dedicated proxy for an ApsaraDB RDS instance. ApsaraDB RDS provides the dedicated proxy feature to deliver capabilities such as read/write splitting and short-lived connection optimization. Before you call this operation, make sure that the following requirements are met: The dedicated proxy feature is enabled on the instance. The instance runs one of the following database engine versions and RDS editions: MySQL 8.0 on RDS Enterprise Edition (minor version of 20191204 or later) MySQL 8.0 on RDS High-availability Edition (minor version of 20190915 or later) MySQL 5.7 on RDS Enterprise Edition (minor version of 20191128 or later) MySQL 5.7 on RDS High-availability Edition (minor version of 20190925 or later) MySQL 5.6 on RDS High-availability Edition (minor version of 20200229 or later) Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBProxyP erformance | The operation that you want to perform. Set the value to DescribeDBProxyPerf ormance. |
| DBInstanceId | String | Yes | rm-t4n3axxxxx | The ID of the instance. |
| EndTime | String | Yes | 2019-09- 21T18:00:00Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |
| MetricsName | String | Yes | Maxscale CpuUsa _ ge | The performance metrics to query. These performance metrics are determined by the DBProxyInst anceT ype parameter. If you set the DBProxyInst anceT ype parameter to Dedicat edProxy, you can query only the Maxscale CpuUsage performance _ metric, which indicates CPU utilization. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. You can call the DescribeRegions operation to query the most recent region list. |
| StartTime | String | Yes | 2019-09- 19T01:00:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBProxyInstanceT ype | String | No | DedicatedProxy | The type of the proxy enabled on the instance. Set the value to Dedicat edProxy. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | lsmexxxxxxx | The ID of the instance. |
| EndTime | String | 2019-09- 21T18:00:00Z | The end time of the query. |
| PerformanceKe ys | Array of PerformanceKe y |   | Details of the performance data. |
| PerformanceKe y |   |   |   |
| Key | String | cpu ratio _ | The name of the performance metric. |
| ValueFormat | String | docker container cp _ _ u | The format that the value of the performance metric follows. |
| Values | Array of PerformanceVa lue |   | An array that consists of performance metric values in the following format: {value1, value2, ...}. |
| PerformanceVa lue |   |   |   |
| Date | String | 2019-10- 10T09:00:00Z | The time when the performance metric value is recorded. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| Value | String | 2.83 | The value of the performance metric. |
| RequestId | String | DD31056F-A0CE- 41D7-AD39- 689B6ABAE982 | The ID of the request. |
| StartTime | String | 2019-09- 19T01:00:00Z | The start time of the query. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeDBProxyPerformance &RegionId=cn-hangzhou &DBInstanceId=rm-t4n3axxxxx &MetricsName=Maxscale_CpuUsage &StartTime=2019-09-19T01:00:00Z &EndTime=2019-09-21T18:00:00Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeDBProxyPerformanceResponse>
  <DBInstanceId>lsmexxxxxxx</DBInstanceId>
  <RequestId>DD31056F-A0CE-41D7-AD39-689B6ABAE982</RequestId>
  <PerformanceKeys>
        <PerformanceKey>
              <Values>
                    <PerformanceValue>
                          <Value>2.83</Value>
                          <Date>2019-10-10T09:00:00Z</Date>
                    </PerformanceValue>
              </Values>
              <Key>cpu_ratio</Key>
              <ValueFormat>docker_container_cpu</ValueFormat>
        </PerformanceKey>
  </PerformanceKeys>
  <EndTime>2019-10-10T09:39:28Z</EndTime>
  <StartTime>2019-10-01T09:39:28Z</StartTime>
</DescribeDBProxyPerformanceResponse>
```

`JSON` format `{`

```json
 "DBInstanceId": "lsmexxxxxxx",
 "RequestId": "DD31056F-A0CE-41D7-AD39-689B6ABAE982",
 "PerformanceKeys": {
  "PerformanceKey": [
```

`{`

```json
    "Values": {
     "PerformanceValue": [
```

`{`

```json
       "Value": "2.83",
       "Date": "2019-10-10T09:00:00Z"
```

`}` `]` `},`

```json
    "Key": "cpu_ratio",
    "ValueFormat": "docker_container_cpu"
```

`}` `]` `},`

```json
 "EndTime": "2019-10-10T09:39:28Z",
 "StartTime": "2019-10-01T09:39:28Z"
```

`}` Error codes

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | Endpoint.NotFound | Specified endpoint is not found. | The error message returned because the port used to connect to the dedicated proxy endpoint is not found. |

#### 2.8.6 ModifyDBProxy

Enables or disables the dedicated proxy feature for an ApsaraDB RDS instance. ApsaraDB RDS provides the dedicated proxy feature to deliver capabilities such as read/write splitting and short-lived connection optimization. Before you call this operation, make sure that the instance runs one of the following database engine versions and RDS editions: MySQL 8.0 on RDS Enterprise Edition (minor version of 20191204 or later) MySQL 8.0 on RDS High-availability Edition (minor version of 20190915 or later) MySQL 5.7 on RDS Enterprise Edition (minor version of 20191128 or later) MySQL 5.7 on RDS High-availability Edition (minor version of 20190925 or later) MySQL 5.6 on RDS High-availability Edition (minor version of 20200229 or later) Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBProxy | The operation that you want to perform. Set the value to Modif yDBProxy. |
| ConfigDBProxySer vice | String | Yes | Startup | Specifies whether to enable or disable the dedicated proxy feature. Valid values: St art up: enables the dedicated proxy feature. Shut down: disables the dedicated proxy feature. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| DBProxyInstanceN um | String | No | 1 | The number of enabled proxy instances. Valid values: 1 to 60. Default value: 1. Not e The capability to process requests increases in proportion with the number of enabled proxy instances. You can specify an appropriate number of proxy instances based on the monitoring information of database loads. |
| RegionId | String | No | cn-hangzhou | The region ID of the instance. You can call the DescribeRegions operation to query the most recent region list. |
| InstanceNetwork Type | String | No | VPC | The network type of the instance. Set the value to VPC. |
| VPCId | String | No | vpc-xxxxxxxxxxxx | The ID of the VPC in which the instance resides. |
| VSwitchId | String | No | CloudInstanceId | The ID of the vSwitch to which the instance is connected. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | FC452BB1-EED8- 4278-95C7- 0324B3710DF1 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ModifyDBProxy &DBInstanceId=rm-uf6wjk5xxxxxxx &ConfigDBProxyService=Startup &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBProxyResponse>
    <RequestId>FC452BB1-EED8-4278-95C7-0324B3710DF1</RequestId>
</ModifyDBProxyResponse>
```

`JSON` format `{`

```json
    "RequestId": "FC452BB1-EED8-4278-95C7-0324B3710DF1"
```

`}`

#### 2.8.7 ModifyDBProxyEndpoint

Modifies the proxy terminal settings of an ApsaraDB RDS instance. ApsaraDB RDS provides the dedicated proxy feature to deliver capabilities such as read/write splitting and connection pooling. Before you call this operation, make sure that the following requirements are met: The dedicated proxy feature is enabled on the instance. The instance runs one of the following database engine versions and RDS editions: MySQL 8.0 on RDS Enterprise Edition (minor version of 20191204 or later) MySQL 8.0 on RDS High-availability Edition (minor version of 20190915 or later) MySQL 5.7 on RDS Enterprise Edition (minor version of 20191128 or later) MySQL 5.7 on RDS High-availability Edition (minor version of 20190925 or later) MySQL 5.6 on RDS High-availability Edition (minor version of 20200229 or later) Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBProxyEn dpoint | The operation that you want to perform. Set the value to Modif yDBProxyEndpoint . |
| DBInstanceId | String | Yes | rm- bp145737x5bi6** ** | The ID of the instance. |
| DBProxyEndpointI d | String | Yes | gos787jog2wk0y* *** | The ID of the proxy endpoint. You can call the DescribeDBProxyEndpoint operation to query the proxy endpoints of a proxy terminal. Not e This parameter is required if you set the DbEndpoint Operat or parameter to Delet e or Modif y. |
| ConfigDBProxyFea tures | String | No | ReadWriteSpliting :1;ConnectionPer sist:0; | The features that you want to enable for the proxy endpoint. If you specify more than one feature, separate them with semicolons (;). Format: Feature 1:Status;Feature 2:Status;... Valid feature values: ReadWrit eSplit ing: read/write splitting Connect ionPersist : connection pooling T ransact ionReadSqlRout eOpt imi zeSt at us: transaction splitting Valid status values: 1: enabled 0: disabled |
| RegionId | String | No | cn-hangzhou | The region ID of the instance. You can call the DescribeRegions operation to query the most recent region list. |

|   |   | Feature |
|---|---|---|
|   | 1:Status;Feature 2:Status;... |   |

| Parameter |   | Type | Required |   | Example | Description |   |   |
|---|---|---|---|---|---|---|---|---|
| ReadOnlyInstance MaxDelayTime |   | String | No |   | 30 | The latency threshold that is allowed for read/write splitting. If the latency on a read-only instance exceeds the specified threshold, ApsaraDB RDS no longer routes read requests to the read-only instance. If you do not specify this parameter, the original value of this parameter is retained. Valid values: 30 to 3600. Default value: 30. Not e You must specify this parameter only when the read/write splitting feature is enabled. |   |   |
| ReadOnlyInstance DistributionType |   | String | No |   | Standard | The policy that is used to assign read weights. Valid values: St andard: ApsaraDB RDS automatically assigns read weights to the primary and read-only instances based on the specifications of these instances. Cust om: You must manually assign read weights to the primary and read-only instances. Not e You must specify this parameter only when the read/write splitting feature is enabled. |   |   |
| ReadOnlyInstance Weight |   |   |   |   | {"rm- | The read weights assigned to the primary instance and its read-only instances. Read weights increase in increments of 100 and the maximum read weight is 10000. Format: {"Instance ID 1":"Read |   |   |
|   |   |   |   |   |   |   | {"Instance ID 1":"Read |   |
|   |   |   |   |   | uf6wjk5xxxx":"50 | weight","Instance ID 2":"Read |   |   |
|   |   | String | No |   | 0","rr- tfhfgk5xxx":"200 | weight"...} |   |   |
|   |   |   |   |   | "...} |   |   |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6B50D92C-1960- 4D4F-A290- AFADD6B1A5C8 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ModifyDBProxyEndpoint &DBInstanceId=rm-bp145737x5bi6**** &DBProxyEndpointId=gos787jog2wk0y**** &ConfigDBProxyFeatures=ReadWriteSpliting:1;ConnectionPersist:1; &ReadOnlyInstanceMaxDelayTime=30 &ReadOnlyInstanceDistributionType=Standard &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBProxyEndpointResponse>
    <RequestId>6B50D92C-1960-4D4F-A290-AFADD6B1A5C8</RequestId>
</ModifyDBProxyEndpointResponse>
```

`JSON` format `{`

```json
 "RequestId": "6B50D92C-1960-4D4F-A290-AFADD6B1A5C8"
```

`}`

#### 2.8.8 ModifyDBProxyInstance

Modifies the dedicated proxy settings of an ApsaraDB RDS instance. ApsaraDB RDS provides the dedicated proxy feature to deliver capabilities such as read/write splitting and short-lived connection optimization. Before you call this operation, make sure that the following requirements are met: The dedicated proxy feature is enabled on the instance. The instance runs one of the following database engine versions and RDS editions: MySQL 8.0 on RDS Enterprise Edition (minor version of 20191204 or later) MySQL 8.0 on RDS High-availability Edition (minor version of 20190915 or later) MySQL 5.7 on RDS Enterprise Edition (minor version of 20191128 or later) MySQL 5.7 on RDS High-availability Edition (minor version of 20190925 or later) MySQL 5.6 on RDS High-availability Edition (minor version of 20200229 or later) Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBProxyIns tance | The operation that you want to perform. Set the value to Modif yDBProxyInst ance. |
| DBInstanceId | String | Yes | rm-t4n3axxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| DBProxyInstanceN um | String | Yes | 2 | The number of proxy instances. A value of 0 indicates that the dedicated proxy feature is disabled for the instance. Valid values: 0 to 60. Not e The capability to process requests increases in proportion with the number of enabled proxy instances. You can specify an appropriate number of proxy instances based on the monitoring information of database loads. |
| DBProxyInstanceT ype | String | Yes | DedicatedProxy | The type of the proxy enabled on the instance. Set the value to Dedicat edProxy. |
| EffectiveTime | String | No | MaintainTime | The time when you want the new settings to take effect. Valid values: Immediat e: The new settings take effect immediately. Maint ainT ime: The new settings take effect within the maintenance window. Specif icT ime: The new settings take effect at the specified point in time. Default value: Maint ainT ime. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| EffectiveSpecificT ime | String | No | 2019-07- 10T13:15:12Z | The point in time when the new settings take effect. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. Not e This parameter is required when the Ef f ect iveT ime parameter is set to Specif icT ime. |
| RegionId | String | No | cn-hangzhou | The region ID of the instance. You can call the DescribeRegions operation to query the most recent region list. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 65C55572-530E- 4A53-BE03- 1D08CAF0F046 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ModifyDBProxyInstance &DBInstanceId=rm-t4n3axxxxx &DBProxyInstanceType=DedicatedProxy &DBProxyInstanceNum=2 &EffectiveTime=Immediate &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBProxyInstanceResponse>
    <RequestId>65C55572-530E-4A53-BE03-1D08CAF0F046</RequestId>
</ModifyDBProxyInstanceResponse>
```

`JSON` format `{`

```json
    "RequestId": "65C55572-530E-4A53-BE03-1D08CAF0F046"
```

`}`

#### 2.8.9 ModifyReadWriteSplittingConnection

Modifies the latency threshold that is allowed for read/write splitting and the read weights of a primary ApsaraDB RDS instance and its read-only instances. Before you call this operation, make sure that the following requirements are met: The shared proxy feature is enabled for the primary instance. The read/write splitting feature is enabled for the primary instance. The primary instance runs one of the following database engine versions and RDS editions: MySQL 5.7 on RDS High-availability Edition (with local SSDs) MySQL 5.6 SQL Server 2017 EE Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyReadWrite SplittingConnecti on | The operation that you want to perform. Set the value to Modif yReadWrit eSplit t ingConnect i on. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the primary instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| ConnectionString Prefix | String | No | rm- m5xxxxxxxxrw.my sql.rds.aliyuncs.c om | The prefix of the read/write splitting endpoint. The prefix must be unique. It can be up to 30 characters in length and can contain lowercase letters and hyphens (-). It must start with a lowercase letter. Not e The default prefix consists of the name of the primary instance followed by rw. |
| Port | String | No | 3306 | The port that is connected to the read/write splitting endpoint. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| MaxDelayTime | String | No | 12 | The latency threshold that is allowed for read/write splitting. Unit: seconds. If the latency on a read-only instance exceeds the specified threshold, ApsaraDB RDS no longer routes read requests to the read-only instance. If you do not specify this parameter, the default latency threshold is used. Not e The MaxDelayT ime parameter is not supported for instances that run SQL Server 2017 on RDS Cluster Edition. You must specify at least one of MaxDelayT ime and Dist ribut ionT ype. |
| DistributionType | String | No | Standard | The method that is used to assign read weights. Valid values: St andard: ApsaraDB RDS automatically assigns read weights to the primary and read-only instances based on the specifications of these instances. Cust om: You must manually assign read weights to the primary and read-only instances. Not e You must specify at least one of MaxDelayT ime and Dist ribut ionT ype. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Weight | String | No | null | The read weights of the primary instance and its read-only instances. A read weight must be a multiple of 100 and cannot exceed 10000. Format: {"Instanceid1":"Weight","Instanceid2":" Weight"...}. Not e This parameter is required if you set the Dist ribut ionT ype parameter to Cust om. This parameter is invalid if you set the Dist ribut ionT ype parameter to St andard. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5A77D650-27A1- 4E08-AD9E- 59008EDB6927 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ModifyReadWriteSplittingConnection &DistributionType=Standard &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyReadWriteSplittingConnectionResponse>
      <RequestID>5A77D650-27A1-4E08-AD9E-59008EDB6927</RequestID>
</ModifyReadWriteSplittingConnectionResponse>
```

`JSON` format `{`

```json
    "RequestID":"5A77D650-27A1-4E08-AD9E-59008EDB6927"
```

`}`

#### 2.8.10 ReleaseReadWriteSplittingConnection

Releases the read/write splitting endpoint of a primary ApsaraDB RDS instance. Before you call this operation, make sure that the following requirements are met: The shared proxy feature is enabled for the primary instance. The read/write splitting feature is enabled for the primary instance. The primary instance runs one of the following database engine versions and RDS editions: MySQL 5.7 on RDS High-availability Edition (with local SSDs) MySQL 5.6 SQL Server 2017 EE Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ReleaseReadWrit eSplittingConnect ion | The operation that you want to perform. Set the value to ReleaseReadWrit eSplit t ingConnect ion. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the primary instance. You can call the DescribeDBInstances operation to query the IDs of instances. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5A77D650-27A1- 4E08-AD9E- 59008EDB6927 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ReleaseReadWriteSplittingConnection &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ReleaseReadWriteSplittingConnectionResponse>
      <RequestID>5A77D650-27A1-4E08-AD9E-59008EDB6927</RequestID>
</ReleaseReadWriteSplittingConnectionResponse>
```

`JSON` format `{`

```json
    "RequestID":"5A77D650-27A1-4E08-AD9E-59008EDB6927"
```

`}`

### 2.9 Primary/secondary high availability and data replication

availability and data replication

#### 2.9.1 DescribeDBInstanceHAConfig

Queries the high availability mode and data replication mode of an ApsaraDB RDS instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstan ceHAConfig | The operation that you want to perform. Set the value to DescribeDBInst anceHAConf ig. |
| DBInstanceId | String | Yes | rm-uf6wjk5xxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | rm-uf6wjk5xxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| HAMode | String | RPO | The high availability mode of the instance. Valid values: RPO: Data consistency is preferred. The instance ensures data reliability to minimize data loss. If you have high requirements on data consistency, select this mode. RT O: Service availability is preferred. The instance restores the database service at the earliest opportunity to ensure service availability. If you have high requirements on service availability, select this mode. Not e This parameter is returned only for instances that run MySQL. |
| SyncMode | String | Sync | The data replication mode of the instance. Valid values: Sync Semi-sync Async Not e This parameter is returned only for instances that run MySQL. |
| HostInstanceInf os | Array of NodeInfo |   | Details of the primary and secondary instances. |
| NodeInfo |   |   |   |
| NodeId | String | 3397027 | The ID of the instance. |
| NodeType | String | Master | The role of the instance. Valid values: Mast er: primary instance Slave: secondary instance |
| RegionId | String | cn-hangzhou | The region ID of the instance. |
| ZoneId | String | cn-hangzhou-b | The zone ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| SyncStatus | String | NotAvailable | The synchronization status of the instance. Valid values: Not Available: The synchronization fails. This means that faults occur. Syncing: The synchronization is in process. In this case, a primary/secondary switchover may cause data loss. Synchronized: The synchronization is complete. Not Support : The database engine or version does not involve the synchronization between the primary and secondary instances. |
| LogSyncTime | String | 2018-05- 05T15:15:00Z | The time when the secondary instance received logs from the primary instance. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| DataSyncTime | String | 2018-05- 05T15:15:00Z | The time when the data synchronization between the primary and secondary instances was complete. The time follows the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time is displayed in UTC. |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | The ID of the request. |
| SwitchMode | String | None | An invalid parameter. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeDBInstanceHAConfig &DBInstanceId=rm-uf6wjk5xxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeDBInstanceHAConfigResponse>
  <RequestId>103D4ACC-F2F9-4A7E-9ACC-14B0A25613E0</RequestId>
  <DBInstanceId>rm-uf6wjk5xxxxxx</DBInstanceId>
  <HAMode>RPO</HAMode>
  <HostInstanceInfos>
        <NodeInfo>
              <DataSyncTime></DataSyncTime>
              <ZoneId>cn-hangzhou-h</ZoneId>
              <LogSyncTime></LogSyncTime>
              <NodeType>Slave</NodeType>
              <NodeId>13567431</NodeId>
              <SyncStatus>NotSupport</SyncStatus>
              <RegionId>cn-hangzhou</RegionId>
        </NodeInfo>
        <NodeInfo>
              <DataSyncTime></DataSyncTime>
              <ZoneId>cn-hangzhou-h</ZoneId>
              <LogSyncTime></LogSyncTime>
              <NodeType>Master</NodeType>
              <NodeId>14565107</NodeId>
              <SyncStatus>NotSupport</SyncStatus>
              <RegionId>cn-hangzhou</RegionId>
        </NodeInfo>
  </HostInstanceInfos>
  <SyncMode>Semi-sync</SyncMode>
</DescribeDBInstanceHAConfigResponse>
```

`JSON` format `{`

```json
    "RequestId": "103D4ACC-F2F9-4A7E-9ACC-14B0A25613E0",
    "DBInstanceId": "rm-uf6wjk5xxxxxx",
    "HAMode": "RPO",
    "HostInstanceInfos": {
        "NodeInfo": [
```

`{`

```json
                "DataSyncTime": "",
                "ZoneId": "cn-hangzhou-h",
                "LogSyncTime": "",
                "NodeType": "Slave",
                "NodeId": "13567431",
                "SyncStatus": "NotSupport",
                "RegionId": "cn-hangzhou"
```

`},` `{`

```json
                "DataSyncTime": "",
                "ZoneId": "cn-hangzhou-h",
                "LogSyncTime": "",
                "NodeType": "Master",
                "NodeId": "14565107",
                "SyncStatus": "NotSupport",
                "RegionId": "cn-hangzhou"
```

`}` `]` `},`

```json
    "SyncMode": "Semi-sync"
```

`}`

#### 2.9.2 ModifyDBInstanceHAConfig

Changes the high availability mode and data replication mode of an ApsaraDB RDS instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstance HAConfig | The operation that you want to perform. Set the value to Modif yDBInst anceHAConf ig. |
| DbInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SyncMode | String | No | Sync | The data replication mode of the instance. Valid values: Sync Semi-sync Async Not e This parameter is not supported for instances that run SQL Server 2017 EE. |
| HAMode | String | No | RPO | The high availability mode of the instance. Valid values: RPO: Data consistency is preferred. The instance ensures data reliability to minimize data loss. If you have high requirements on data consistency, select this mode. RT O: Service availability is preferred. The instance restores the database service at the earliest opportunity to ensure service availability. If you have high requirements on service availability, select this mode. |
| SwitchMode | String | No | 0 | The time when primary/secondary switchovers are performed. Valid values: 0: Primary/secondary switchovers are performed immediately. 1: Primary/secondary switchovers are performed within the maintenance window. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D4D4BE8A-DD46- 440A-BFCD- EE31DA81C9DD | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ModifyDBInstanceHAConfig &DbInstanceId=rm-uf6wjk5xxxxxxx &HAMode=RPO &SyncMode=Sync &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceHAConfigResponse>
      <RequestId>D4D4BE8A-DD46-440A-BFCD-EE31DA81C9DD</RequestId>
</ModifyDBInstanceHAConfigResponse>
```

`JSON` format `{`

```json
    "RequestId":"D4D4BE8A-DD46-440A-BFCD-EE31DA81C9DD"
```

`}`

#### 2.9.3 DescribeDBInstanceSwitchLog

Queries the primary/secondary switchover logs of an ApsaraDB RDS instance. This operation is supported for instances that run MySQL, SQL Server, PostgreSQL, or PolarDB. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstan ceSwitchLog | The operation that you want to perform. Set the value to DescribeDBInst anceSwit chLog. |
| EndTime | String | Yes | 2018-06- 11T15:00Z | The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. Example: 2011-06-11T16:00Z. The end time must be later than the start time. |
| StartTime | String | Yes | 2014-06- 11T15:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. Example: 2011-06-11T15:00Z. |
| DBInstanceId | String | No | rdsaiiabnaiiabn | The ID of the instance. |

| eveloper Guide·API r | eference |   |   | ApsaraDB for RD |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. Valid values: 1 to 30. Default value: 1. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceNam e | String | rdsaiiabnaiiabn | The name of the instance. |
| Items | Array of Item |   | Details of primary/secondary switchover logs. |
| Item |   |   |   |
| AffectedSessio ns | String | None | The number of affected sessions during the switchover. |
| HAStatus | String | None | None |
| SwitchCauseCo de | String | None | The cause for the switchover. |
| SwitchFinishTim e | String | None | The end time of the switchover. |
| SwitchId | String | None | The ID of the switchover task. |
| SwitchStartTim e | String | None | The start time of the switchover. |
| TotalSessions | String | None | The total number of sessions during the switchover. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCou nt | Integer | 60 | The number of entries returned per page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D1CA494F-CC13- 4EB6-8C4D- 5352EE4045BD | The ID of the request. |
| TotalRecordCo unt | Integer | 5 | The total number of entries returned. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeDBInstanceSwitchLog &EndTime=2018-06-11T15:00Z &StartTime=2014-06-11T15:00Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeDBInstanceSwitchLogResponse>
      <Items></Items>
      <PageNumber>1</PageNumber>
      <TotalRecordCount>5</TotalRecordCount>
      <RequestId>D1CA494F-CC13-4EB6-8C4D-5352EE4045BD</RequestId>
      <PageRecordCount>60</PageRecordCount>
      <DBInstanceName>rm-m5el220b25im05g7g</DBInstanceName></DescribeDBInstanceSwitchLogRes
ponse>
```

`JSON` format `{`

```json
    "Items": {},
    "PageNumber": 1,
    "TotalRecordCount": 5,
    "RequestId": "D1CA494F-CC13-4EB6-8C4D-5352EE4045BD",
    "PageRecordCount": 60,
    "DBInstanceName": "rm-m5el220b25im05g7g"
```

`}`

#### 2.9.4 DescribeHASwitchConfig

Queries the automatic primary/secondary switchover settings of an ApsaraDB RDS instance. After the switchover, the original primary instance becomes the secondary instance. This operation is supported only for instances that run the High-availability Edition, Enterprise Edition, or Cluster Edition. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeHASwitch Config | The operation that you want to perform. Set the value to DescribeHASwit chConf ig. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxxxx x | The ID of the instance. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. You can call the DescribeRegions operation to query the most recent region list. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| HAConfig | String | Manual | The primary/secondary switchover mode of the instance. Valid values: Aut o: The automatic primary/secondary switchover feature is enabled. The system automatically switches over workloads from the primary to secondary instances in the event of a fault. Manual: You must manually perform a primary/secondary switchover in the event of a fault. |
| ManualHATime | String | 2019-08- 29T15:00:00Z | The time when the automatic primary/secondary switchover feature is disabled. |
| RequestId | String | 4FDF4B79-2741- 4C5F-8C76- 4B953FC5C2B1 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeHASwitchConfig &RegionId=cn-hangzhou &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeHASwitchConfigResponse>
   <ManualHATime>2019-08-29T15:00:00Z</ManualHATime>
   <RequestId>4FDF4B79-2741-4C5F-8C76-4B953FC5C2B1</RequestId>
   <HAConfig>Manual</HAConfig>
</DescribeHASwitchConfigResponse>
```

`JSON` format `{`

```json
    "ManualHATime": "2019-08-29T15:00:00Z",
    "RequestId": "4FDF4B79-2741-4C5F-8C76-4B953FC5C2B1",
    "HAConfig": "Manual"
```

`}`

#### 2.9.5 Switch workloads over between primary and secondary ApsaraDB RDS instances

and secondary ApsaraDB RDS instances You can call the SwitchDBInstanceHA operation to switch workloads over between a primary ApsaraDB RDS instance and its secondary instance. This operation switches workloads over between the primary and secondary ApsaraDB RDS instances that do not run RDS Basic Edition. After the switchover, the secondary RDS instance serves as the primary RDS instance. Precaut ions Data is synchronized between the primary RDS instance and the secondary RDS instance in real time. The secondary RDS instance serves only as a read-only RDS instance or standby. We recommend that you do not modify the data of the secondary RDS instance. If you modify the data of the secondary RDS instance, the data of the primary RDS instance may be accidentally deleted or overwritten, which may cause irreparable business loss. If the secondary RDS instance serves as a read-only RDS instance, the secondary RDS instance serves as the new primary RDS instance after a primary/secondary switchover. We recommend that you plan the read and write workloads for the new primary RDS instance before the switchover. During a primary/secondary switchover, a transient connection may occur. Make sure that your application is configured to automatically reconnect to your database system. After a primary/secondary switchover, the read-only RDS instances that are attached to the primary RDS instance must re-establish the connections that are used to replicate data and synchronize incremental data from the primary RDS instance. As a result, the data on the read-only RDS instances shows latencies of a few minutes. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SwitchDBInstance HA | The operation that you want to perform. Set the value to Swit chDBInst anceHA. |

| D | eveloper Guide·API r | eference |   |   | ApsaraDB for RD | S |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxxxx x | The ID of the primary instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| NodeId | String | Yes | 349054 | The unique identifier of the secondary instance. You can call the DescribeDBInstanceHAConfig operation to query the No. of the secondary instance. |
| Operation | String | No | None | An invalid parameter. |
| Force | String | No | No | Specifies whether to enable forced switchover. Valid values: Yes No Default value: No. |
| EffectiveTime | String | No | Immediate | The time at which you want the switchover to take effect. Valid values: Immediat e: The switchover takes effect immediately. Maint ainT ime: The switchover takes effect within the maintenance window. Default value: Immediat e. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1E43AAE0-BEE8- 43DA-860D- EAF2AA0724DC | The ID of the request. |

Examples Sample request

```
http(s)://rds.example.com/?Action=SwitchDBInstanceHA &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &NodeId=349054 &<Common request parameters>
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

#### 2.9.6 Enable or disable automatic primary/secondary switchovers

primary/secondary switchovers You can call the ModifyHASwitchConfig operation to enable or disable the automatic primary/secondary switchover feature for an ApsaraDB RDS instance. This operation switches workloads over between the primary and secondary ApsaraDB RDS instances that do not run RDS Basic Edition. After the switchover, the secondary RDS instance serves as the primary RDS instance. Precaut ions Data is synchronized between the primary RDS instance and the secondary RDS instance in real time. The secondary RDS instance serves only as a read-only RDS instance or standby. We recommend that you do not modify the data of the secondary RDS instance. If you modify the data of the secondary RDS instance, the data of the primary RDS instance may be accidentally deleted or overwritten, which may cause irreparable business loss. If the secondary RDS instance serves as a read-only RDS instance, the secondary RDS instance serves as the new primary RDS instance after a primary/secondary switchover. We recommend that you plan the read and write workloads for the new primary RDS instance before the switchover. During a primary/secondary switchover, a transient connection may occur. Make sure that your application is configured to automatically reconnect to your database system. After a primary/secondary switchover, the read-only RDS instances that are attached to the primary RDS instance must re-establish the connections that are used to replicate data and synchronize incremental data from the primary RDS instance. As a result, the data on the read-only RDS instances shows latencies of a few minutes. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyHASwitchC onfig | The operation that you want to perform. Set the value to Modif yHASwit chConf ig. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxxxx x | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. You can call the DescribeRegions operation to query the most recent region list. |
| HAConfig | String | No | Manual | The mode of the automatic primary/secondary switchover feature. Valid values: Aut o: The automatic primary/secondary switchover feature is enabled. The system automatically switches your workloads over from the instance to its secondary instance in the event of a fault. Manual: The automatic primary/secondary switchover feature is disabled. You must manually switch your workloads over from the instance to its secondary instance in the event of a fault. Default value: Aut o. Not e If you set this parameter to Manual, you must specify the ManualHAT ime parameter. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ManualHATime | String | No | 2019-08- 29T15:00:00Z | The time to disable the automatic primary/secondary switchover feature. The time can range from the current time to 23:59:59 seven days later. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. Not e This parameter takes effect only when you set the HAConf ig parameter to Manual. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B6AE1448-D846- 4831-B1C7- CFF3E99D5470 | The ID of the request. |

Examples Sample request

```
http(s)://rds.example.com/?Action=ModifyHASwitchConfig &RegionId=cn-hangzhou &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &HAConfig=Manual &ManualHATime=2019-08-28T15:00:00 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyHASwitchConfigResponse>
   <RequestId>B6AE1448-D846-4831-B1C7-CFF3E99D5470</RequestId>
</ModifyHASwitchConfigResponse>
```

`JSON` format `{`

```json
 "RequestId": "B6AE1448-D846-4831-B1C7-CFF3E99D5470"
```

`}` Error codes

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | HaConfig.Format | The value of HaConfig must be auto or manual | The error message returned because the value of the HAConfig parameter is invalid. The HAConfig parameter must be set to Auto or Manual. |
| 400 | HaConfigIsNull | HaConfig is null. | The error message returned because the value of the HAConfig parameter is null. |

### 2.10 Security and encryption

#### 2.10.1 DescribeDBInstanceIPArrayList

Queries the IP address whitelists of an ApsaraDB RDS instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstan ceIPArrayList | The operation that you want to perform. Set the value to DescribeDBInst anceIPArrayList . |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| WhitelistNetwork Type | String | No | VPC | The network type of the IP address whitelist. Valid values: Classic: classic network in enhanced whitelist mode VPC: virtual private cloud (VPC) in enhanced whitelist mode MIX: standard whitelist mode By default, this operation returns IP address whitelists of all network types. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | Array of DBInstanceIPArr ay |   | Details of the IP address whitelist. |
| DBInstanceIPArr ay |   |   |   |
| DBInstanceIPArr ayName | String | rds default _ | The name of the IP address whitelist. |
| DBInstanceIPArr ayAttribute | String | hidden | The attribute of the IP address whitelist. By default, this parameter is empty. Not e The IP address whitelists that have the hidden attribute are not displayed in the ApsaraDB RDS console. These IP address whitelists are used to access Alibaba Cloud services such as Data Transmission Service (DTS). |
| SecurityIPList | String | 192.168.1.0/24 | The IP addresses in the IP address whitelist. |
| SecurityIPType | String | IPv4 | The type of the IP address. Valid values: IPv4 IPv6 |
| RequestId | String | E2B6AF71-DC32- 4055-B477- 43B348798D10 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeDBInstanceIPArrayList &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeDBInstanceIPArrayListResponse>
      <Items>
            <DBInstanceIPArray>
                  <DBInstanceIPArrayName>rds_default</DBInstanceIPArrayName>
                  <DBInstanceIPArrayAttribute></DBInstanceIPArrayAttribute>
                  <WhitelistNetworkType>VPC</WhitelistNetworkType>
                  <SecurityIPList>192.168.1.0/24</SecurityIPList>
                  <SecurityIPType>IPv4</SecurityIPType>
            </DBInstanceIPArray>
      </Items>
      <RequestId>E2B6AF71-DC32-4055-B477-43B348798D10</RequestId>
</DescribeDBInstanceIPArrayListResponse>
```

`JSON` format `{`

```json
    "Items": {
        "DBInstanceIPArray": [
```

`{`

```json
                "DBInstanceIPArrayName": "rds_default",
                "DBInstanceIPArrayAttribute": "",
                "WhitelistNetworkType": "VPC",
                "SecurityIPList": "192.168.1.0/24",
                "SecurityIPType": "IPv4"
```

`}` `]` `},`

```json
    "RequestId": "E2B6AF71-DC32-4055-B477-43B348798D10"
```

`}`

#### 2.10.2 ModifySecurityIps

Modifies an IP address whitelist of an ApsaraDB RDS instance. This operation allows you to add more IP addresses to a whitelist to allow their access to the instance. Before you call this operation, make sure that the instance is in the running state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySecurityIps | The operation that you want to perform. Set the value to Modif ySecurit yIps. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |

| psaraDB for RDS |   |   |   | Developer Guide·API referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SecurityIps | String | Yes | 10.23.12.24 | The IP addresses that you want to add to the IP address whitelist. Separate multiple IP addresses with commas (,). Each IP address in the IP address whitelist must be unique. Both IPv4 and IPv6 IP addresses are allowed. They support the following formats: IP addresses, such as 10.23.12.24. Classless Inter-Domain Routing (CIDR) blocks, such as 10.23.12.0/24. In this case, /24 indicates that the prefix of each IP address is 24-bit long. You can replace 24 with a value within the range of 1 to 32. Not e A maximum of 1,000 IP addresses and CIDR blocks can be configured for each instance. If you want to add a large number of IP addresses, we recommend that you merge them into CIDR blocks, such as 10.23.12.0/24. |
| DBInstanceIPArray Name | String | No | test | The name of the IP address whitelist that you want to modify. Default value: Default. Not e A maximum of 200 IP address whitelists can be configured for each instance. |
| DBInstanceIPArray Attribute | String | No | hidden | The attribute of the IP address whitelist. By default, this parameter is empty. Not e The IP address whitelists that have the hidden attribute are not displayed in the ApsaraDB RDS console. These IP address whitelists are used to access Alibaba Cloud services such as Data Transmission Service (DTS). |
| SecurityIPType | String | No | IPv4 | The type of the IP address. |

| Developer Guide·API r | eference |   |   | ApsaraDB for RD |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SecurityGroupId | String | No | sg-xxxxxxx | The ID of the security group. |
| ModifyMode | String | No | Cover | The method that is used to modify the IP address whitelist. Valid values: Cover: uses the Securit yIps value to overwrite the existing entries in the IP address whitelist. Append: adds the IP addresses and CIDR blocks that are specified in the Securit yIps parameter to the IP address whitelist. Delet e: deletes IP addresses and CIDR blocks that are specified in the Securit yIps parameter from the IP address whitelist. You must retain at least one IP address or CIDR block. Default value: Cover. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | The ID of the request. |
| TaskId | String | 115855279 | The ID of the task. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ModifySecurityIps &DBInstanceId=rm-uf6wjk5xxxxxxx &SecurityIps=10.23.12.24 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifySecurityIpsResponse>
      <RequestId> 1AD222E9-E606-4A42-BF6D-8A4442913CEF</RequestId>
      <TaskId>115855279</TaskId>
</ModifySecurityIpsResponse>
```

`JSON` format

|   | { "RequestId": " 1AD222E9-E606-4A42-BF6D-8A4442913CEF", "TaskId": 115855279 } |
|---|---|

#### 2.10.3 DescribeDBInstanceEncryptionKey

Queries the status of disk encryption and the details of keys on an ApsaraDB RDS instance. This operation is supported for instances that run MySQL, SQL Server, or PostgreSQL. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstan ceEncryptionKey | The operation that you want to perform. Set the value to DescribeDBInst anceEncrypt ionKey. |
| DBInstanceId | String | No | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| EncryptionKey | String | No | 749c1df7-xxxx- xxxx-xxxx- xxxxxxxxxxxx | The ID of the custom key that is used for disk encryption. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Creator | String | 1443*****9604 | The creator of the key. |
| DeleteDate | String | 2022-05- 08T08:14:16Z | The scheduled time at which the key is deleted. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| Description | String | Description of the key | The description of the key. |
| EncryptionKey | String | 5306d1b6-7fd3- 42d9-9511-xxxxxxx | The ID of the key. |
| EncryptionKeyS tatus | String | Enabled | The status of the key. Valid values: Enabled Disabled |

| Developer Guide·AP | I reference |   | ApsaraDB for RD |
|---|---|---|---|
| Parameter | Type | Example | Description |
| KeyUsage | String | ENCRYPT/DECRYPT | The purpose of the key. |
| MaterialExpireTi me | String | 2021-10- 18T08:14:16Z | The time at which the key expires. The time follows the ISO 8601 standard in the yyyy- MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| Origin | String | Aliyun KMS _ | The source of the key. |
| RequestId | String | 3BC2768E-DEDA- 40FC-BBE9- 6B884F3626AF | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeDBInstanceEncryptionKey &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeDBInstanceEncryptionKeyResponse>
      <Origin>Aliyun_KMS</Origin>
      <Description>Description of the key</Description>
      <EncryptionKeyStatus>Enabled</EncryptionKeyStatus>
      <RequestId>3BC2768E-DEDA-40FC-BBE9-6B884F3626AF</RequestId>
      <MaterialExpireTime>2021-10-18T08:14:16Z</MaterialExpireTime>
      <KeyUsage>ENCRYPT/DECRYPT</KeyUsage>
      <EncryptionKey>5306d1b6-7fd3-42d9-9511-xxxxxxx</EncryptionKey>
      <Creator>1443*****9604</Creator>
      <DeleteDate>2022-05-08T08:14:16Z</DeleteDate>
</DescribeDBInstanceEncryptionKeyResponse>
```

`JSON` format `{`

```json
    "Origin": "Aliyun_KMS",
    "Description": "Description of the key",
    "EncryptionKeyStatus": "Enabled",
    "RequestId": "3BC2768E-DEDA-40FC-BBE9-6B884F3626AF",
    "MaterialExpireTime": "2021-10-18T08:14:16Z",
    "KeyUsage": "ENCRYPT/DECRYPT",
    "EncryptionKey": "5306d1b6-7fd3-42d9-9511-xxxxxxx",
    "Creator": "1443*****9604",
    "DeleteDate": "2022-05-08T08:14:16Z"
```

`}`

#### 2.10.4 ModifyDTCSecurityIpHostsForSQLServer

Configures a distributed transaction whitelist for an ApsaraDB RDS instance. Distributed transaction whitelists allow for distributed transactions between an Elastic Compute Service (ECS) instance and an ApsaraDB RDS instance. This operation is applicable only to ApsaraDB RDS High-availability Edition instances that run one of the following SQL Server versions: 2012 SE, 2012 EE, 2014 SE, 2016 SE, 2016 EE, and 2017 SE. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDTCSecurit yIpHostsForSQLS erver | The operation that you want to perform. Set the value to Modif yDT CSecurit yIpHost sForSQLS erver. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the ApsaraDB RDS instance. |
| SecurityIpHosts | String | Yes | 192.168.1.100,k3 ecstest | The IP address of the ECS instance and the hostname of the Windows computer. Format: IP address,Hostname. Separates multiple values with semicolons (;). |
| WhiteListGroupNa me | String | Yes | test1 | The name of the IP address whitelist. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | The ID of the ApsaraDB RDS instance. |

| Developer Guide·AP | I reference |   | ApsaraDB for RD |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| DTCSetResult | String | Success | The result of the IP address whitelist configuration. Valid values: Success Fail |
| RequestId | String | 671B6D32-B907- 4EFF-A3B7- 94D2EAD5E3A3 | The ID of the request. |
| TaskId | String | 178968983 | The ID of the task. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ModifyDTCSecurityIpHostsForSQLServer &DBInstanceId=rm-uf6wjk5xxxxxxx &RegionId=cn-hangzhou &SecurityIpHosts=192.168.1.100,k3ecstest &WhiteListGroupName=test1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDTCSecurityIpHostsForSQLServerResponse>
  <RequestId>671B6D32-B907-4EFF-A3B7-94D2EAD5E3A3</RequestId>
      <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
      <DTCSetResult>Success</DTCSetResult>
      <TaskId>178968983</TaskId>
</ModifyDTCSecurityIpHostsForSQLServerResponse>
```

`JSON` format `{`

```json
    "RequestId": "671B6D32-B907-4EFF-A3B7-94D2EAD5E3A3",
    "DBInstanceId": "rm-uf6wjk5xxxxxxx",
    "DTCSetResult": "Success",
    "TaskId": 178968983
```

`}`

#### 2.10.5 DescribeDTCSecurityIpHostsForSQLServer

Queries the distributed transaction whitelists of an ApsaraDB RDS instance. This operation is supported only for ApsaraDB RDS High-availability Edition instances that run one of the following SQL Server versions: 2012 SE, 2012 EE, 2014 SE, 2016 SE, 2016 EE, and 2017 SE. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDTCSecur ityIpHostsForSQL Server | The operation that you want to perform. Set the value to DescribeDT CSecurit yIpHost sForSQL Server. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | The ID of the instance. |
| IpHostPairNum | String | 1 | The number of distributed transaction whitelists. |
| Items | Array of WhiteListGroup s |   | Details of distributed transaction whitelists. |
| WhiteListGroup s |   |   |   |
| SecurityIpHosts | String | 192.168.1.100,k3ecs test | The IP address of the Elastic Compute Service (ECS) instance and the hostname of the Windows computer. Format: IP address,Hostname. Separates multiple values with semicolons (;). |
| WhitelistGroup Name | String | test1 | The name of the distributed transaction whitelist. |
| RequestId | String | 2CA62A70-2203- 45C6-8E90- 8971D5ACC0C2 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeDTCSecurityIpHostsForSQLServer &DBInstanceId=rm-uf6wjk5xxxxxxx &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeDTCSecurityIpHostsForSQLServerResponse>
  <Items>
      <WhiteListGroups>
         <WhitelistGroupName>test1</WhitelistGroupName>
         <SecurityIpHosts>192.168.1.100,k3ecstest</SecurityIpHosts>
      </WhiteListGroups>
   </Items>
   <IpHostPairNum>1</IpHostPairNum>
   <RequestId>2CA62A70-2203-45C6-8E90-8971D5ACC0C2</RequestId>
</DescribeDTCSecurityIpHostsForSQLServerResponse>
```

`JSON` format `{`

```json
 "Items": {
  "WhiteListGroups": [
```

`{`

```json
    "WhitelistGroupName": "test1",
    "SecurityIpHosts": "192.168.1.100,k3ecstest"
```

`}` `]` `},`

```json
 "IpHostPairNum": 1,
 "RequestId": "2CA62A70-2203-45C6-8E90-8971D5ACC0C2"
```

`}`

#### 2.10.6 DescribeDBInstanceSSL

Queries Secure Sockets Layer (SSL) settings of an ApsaraDB RDS instance. This operation is supported only for instances that run MySQL 5.6, MySQL 5.7 on RDS High-availability Edition with local SSDs, MySQL 8.0 on RDS High-availability Edition with local SSDs, SQL Server, or PostgreSQL with standard SSDs. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstan ceSSL | The operation that you want to perform. Set the value to DescribeDBInst anceSSL. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ConnectionStrin g | String | rm- uf6wjk5xxxxxx.mysq l.rds.aliyuncs.com | The endpoint that is protected by SSL encryption. |
| SSLExpireTime | String | 2022-05- 08T08:14:16Z | The time when the server certificate expires. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| RequireUpdate | String | Yes | Indicates whether the server certificate needs to be updated. Valid values for ApsaraDB RDS for MySQL or ApsaraDB RDS for SQL Server: No Yes Valid values for ApsaraDB RDS for PostgreSQL: 0: no 1: yes |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | The ID of the request. |
| RequireUpdate Reason | String | - | The reason why the server certificate needs to be updated. This parameter is supported only when the instance runs PostgreSQL with standard SSDs. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeDBInstanceSSL &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ClientCertRevocationList>-----BEGIN X509 CRL-----MIIB****19mg==-----END X509 CRL-----</Cli entCertRevocationList> <RequestId>1AD222E9-E606-4A42-BF6D-8A4442913CEF</RequestId> <RequireUpdateItem>-</RequireUpdateItem> <CAType>aliyun</CAType> <LastModifyStatus>setting</LastModifyStatus> <ACL>cert</ACL> <RequireUpdate>Yes</RequireUpdate> <ModifyStatusReason>Modify DB Instance SSL Config.</ModifyStatusReason> <ClientCACertExpireTime>-</ClientCACertExpireTime> <ServerKey>-----BEGIN PRIVATE KEY-----MIIE****ihfg==-----END PRIVATE KEY-----</ServerKey> <SSLExpireTime>2022-05-08T08:14:16Z</SSLExpireTime> <SSLCreateTime>-</SSLCreateTime> <ServerCert>-----BEGIN CERTIFICATE-----MIID*****QqEP-----END CERTIFICATE-----</ServerCert> <SSLEnabled>on</SSLEnabled> <ClientCACert>-----BEGIN CERTIFICATE-----MIID*****viXk=-----END CERTIFICATE-----</ClientCAC ert> <ReplicationACL>cert</ReplicationACL> <RequireUpdateReason>-</RequireUpdateReason> <ConnectionString>rm-uf6wjk5xxxxxx.mysql.rds.aliyuncs.com</ConnectionString> <ServerCAUrl>-</ServerCAUrl>
```

`JSON` format `{`

```json
    "ClientCertRevocationList": "-----BEGIN X509 CRL-----MIIB****19mg==-----END X509 CRL---
--",
    "RequestId": "1AD222E9-E606-4A42-BF6D-8A4442913CEF",
    "RequireUpdateItem": "-",
    "CAType": "aliyun",
    "LastModifyStatus": "setting",
    "ACL": "cert",
    "RequireUpdate": "Yes",
    "ModifyStatusReason": "Modify DB Instance SSL Config.",
    "ClientCACertExpireTime": "-",
    "ServerKey": "-----BEGIN PRIVATE KEY-----MIIE****ihfg==-----END PRIVATE KEY-----",
    "SSLExpireTime": "2022-05-08T08:14:16Z",
    "SSLCreateTime": "-",
    "ServerCert": "-----BEGIN CERTIFICATE-----MIID*****QqEP-----END CERTIFICATE-----",
    "SSLEnabled": "on",
    "ClientCACert": "-----BEGIN CERTIFICATE-----MIID*****viXk=-----END CERTIFICATE-----",
    "ReplicationACL": "cert",
    "RequireUpdateReason": "-",
    "ConnectionString": "rm-uf6wjk5xxxxxx.mysql.rds.aliyuncs.com",
    "ServerCAUrl": "-"
```

`}`

#### 2.10.7 ModifyDBInstanceSSL

Modifies the SSL encryption settings of an ApsaraDB RDS instance. This operation is used to configure SSL encryption for an instance. This operation is supported only for instances that run MySQL 5.6, MySQL 5.7 on RDS Highavailability Edition with local SSDs, MySQL 8.0 on RDS High-availability Edition with local SSDs, SQL Server, or PostgreSQL with standard SSDs. SSL encryption is not supported for connections to read/write splitting endpoints. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstance SSL | The operation that you want to perform. Set the value to Modif yDBInst anceSSL. |
| ConnectionString | String | Yes | rm- uf6wjk5xxxxx.mys ql.rds.aliyuncs.co m | The internal or public endpoint for which the server certificate needs to be created or updated. |

|   | Developer Guide·API r | eference |   |   | ApsaraDB for RD | S |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| SSLEnabled | Integer | No | 1 | Specifies whether to enable or disable SSL encryption. Valid values: 1: enables SSL encryption. 0: disables SSL encryption. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 777C4593-8053- 427B-99E2- 105593277CAB | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ModifyDBInstanceSSL &ConnectionString=rm-uf6wjk5xxxxx.mysql.rds.aliyuncs.com &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>777C4593-8053-427B-99E2-105593277CAB</RequestId>
```

`JSON` format `{`

```json
    "RequestId": "777C4593-8053-427B-99E2-105593277CAB"
```

`}`

#### 2.10.8 ModifyDBInstanceTDE

Enables the Transparent Data Encryption (TDE) feature for an ApsaraDB RDS instance. TDE performs real-time I/O encryption and decryption on data files. Data is encrypted before it is written to a disk. Data is also decrypted when it is read from a disk and written to the memory. Before you call this operation, make sure that the following requirements are met: Key Management Service (KMS) is activated. If KMS is not activated, you can activate it when you enable TDE. The instance runs one of the following database engines and RDS editions: MySQL 5.6 MySQL 5.7 on RDS High-availability Edition with local SSDs SQL Server 2019 SE or an Enterprise Edition of SQL Server Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstance TDE | The operation that you want to perform. Set the value to Modif yDBInst anceT DE. |
| DBInstanceId | String | Yes | rm-uf6wjk5**** | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| TDEStatus | String | Yes | Enabled | Specifies whether to enable TDE. Valid values: Enabled Disabled |
| DBName | String | No | testDB | The name of the database for which you want to enable TDE. You can specify up to 50 names in a single request. Separate multiple names with commas (,). Not e This parameter is available and required only when the instance runs SQL Server 2019 SE or an Enterprise Edition of SQL Server. |
| EncryptionKey | String | No | 749c1df7-****- ****-****-**** | The ID of the custom key. Not e This parameter can be specified only for instances that run MySQL. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RoleArn | String | No | acs:ram::140692 6****:role/aliyunr dsinstanceencryp tiondefaultrole | The Alibaba Cloud Resource Name (ARN) of the role. An ARN is the global resource identifier of a role. Not e This parameter can be specified only for instances that run MySQL. |
| EncryptAlgorithm | String | No | SM4 | The encryption method for TDE. Valid values: SM4 AES 256 CBC _ _ |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 777C4593-8053- 427B-99E2- 105593277CAB | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ModifyDBInstanceTDE &DBInstanceId=rm-uf6wjk5**** &TDEStatus=Enabled &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceTDEResponse>
      <RequestId>777C4593-8053-427B-99E2-105593277CAB</RequestId>
</ModifyDBInstanceTDEResponse>
```

`JSON` format `{`

```json
    "ModifyDBInstanceTDEResponse": {
        "RequestId": "777C4593-8053-427B-99E2-105593277CAB"
```

`}` `}`

#### 2.10.9 DescribeDBInstanceTDE

Queries the data encryption status of an ApsaraDB RDS instance. This operation is used to view the Transparent Data Encryption (TDE) configuration of an instance. This operation is supported only for instances that run MySQL 5.6, SQL Server 2019 SE, or SQL Server EE. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstan ceTDE | The operation that you want to perform. Set the value to DescribeDBInst anceT DE. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| TDEStatus | String | Enabled | The TDE status at the instance level. Valid value: Enabled and Disabled |
| Databases | Array of Database |   | Details of the TDE status at the database level. Not e For the instances that run SQL Server 2019 SE or SQL Server EE, you can specify whether to enable TDE at the database level when you enable TDE at the instance level. |
| Database |   |   |   |
| DBName | String | test02 | The name of the database. |
| TDEStatus | String | Enabled | The TDE status at the database level. Valid value: Enabled and Disabled |

| Parameter | Type | Example | Description |
|---|---|---|---|
| EncryptAlgorith m | String | AES 256 CBC _ _ | The encryption method of the TDE. Valid values: SM4 AES 256 CBC _ _ |
| RequestId | String | C816A4BF-A6EC- 4722-95F9- 2055859CCFD2 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeDBInstanceTDE &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeDBInstanceTDEResponse>
   <TDEStatus>Enabled</TDEStatus>
   <Databases>
      <DBName>test02</DBName>
      <TDEStatus>Enabled</TDEStatus>
   </Databases>
   <requestId>C816A4BF-A6EC-4722-95F9-2055859CCFD2</requestId>
</DescribeDBInstanceTDEResponse>
```

`JSON` format `{`

```json
    "TDEStatus": "Enabled",
    "Databases": [
```

`{`

```json
            "DBName": "test02",
            "TDEStatus": "Enabled"
```

`}` `],`

```json
    "requestId": "C816A4BF-A6EC-4722-95F9-2055859CCFD2"
```

`}`

### 2.11 Monitoring management

#### 2.11.1 DescribeResourceUsage

Queries the storage usage of an ApsaraDB RDS instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeResource Usage | The operation that you want to perform. Set the value to DescribeResourceUsage. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | The ID of the instance. |
| Engine | String | MySQL | The database engine of the instance. |
| DiskUsed | Long | 2337275904 | The storage space occupied by both data files and log files. Unit: byte. A value of -1 indicates that no data files or log files are stored on the instance. |
| DataSize | Long | 1292094741 | The storage space occupied by data files. Unit: byte. A value of -1 indicates that no data files are stored on the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| LogSize | Long | 1045181163 | The storage space occupied by log files. Unit: byte. A value of -1 indicates that no log files are stored on the instance. |
| BackupSize | Long | 53002759 | The storage space occupied by backup data. Unit: byte. A value of -1 indicates that no backup data is stored on the instance. |
| ColdBackupSize | Long | 2337275904 | The storage space occupied by cold backup files. Unit: byte. A value of -1 indicates that no cold backup files are stored on the instance. |
| SQLSize | Long | 315052751 | The storage space occupied by SQL data. Unit: byte. A value of -1 indicates that no SQL data is stored on the instance. |
| BackupOssData Size | Long | 8821760 | The size of data backup files that are stored in Object Storage Service (OSS) buckets. Unit: byte. A value of 0 indicates that no data backup files are stored in OSS buckets. |
| BackupOssLogS ize | Long | 44180999 | The size of log backup files that are stored in OSS buckets. Unit: byte. A value of 0 indicates that no log backup files are stored in OSS buckets. |
| RequestId | String | F937E173-559C- 4498-8D90- 38D32342B9E4 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeResourceUsage &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeResourceUsageResponse>
  <PaidBackupSize>0</PaidBackupSize>
  <RequestId>28E73580-103C-4925-A48D-9A7E25F24297</RequestId>
  <BackupSize>51305057407</BackupSize>
  <ArchiveBackupSize>0</ArchiveBackupSize>
  <ColdBackupSize>-1</ColdBackupSize>
  <LogSize>2097152</LogSize>
  <BackupOssLogSize>48565375</BackupOssLogSize>
  <DBInstanceId> rm-uf6wjk5xxxxxxx</DBInstanceId>
  <BackupDataSize>51256492032</BackupDataSize>
  <DataSize>3198156800</DataSize>
  <BackupLogSize>48565375</BackupLogSize>
  <BackupOssDataSize>0</BackupOssDataSize>
  <SQLSize>446228522</SQLSize>
  <DiskUsed>3200253952</DiskUsed>
  <Engine>MySQL</Engine>
</DescribeResourceUsageResponse>
```

`JSON` format `{`

```json
 "PaidBackupSize": 0,
 "RequestId": "28E73580-103C-4925-A48D-9A7E25F24297",
 "BackupSize": 51305057407,
 "ArchiveBackupSize": 0,
 "ColdBackupSize": -1,
 "LogSize": 2097152,
 "BackupOssLogSize": "48565375",
 "DBInstanceId": " rm-uf6wjk5xxxxxxx",
 "BackupDataSize": 51256492032,
 "DataSize": 3198156800,
 "BackupLogSize": 48565375,
 "BackupOssDataSize": "0",
 "SQLSize": 446228522,
 "DiskUsed": 3200253952,
 "Engine": "MySQL"
```

`}`

#### 2.11.2 DescribeDBInstancePerformance

Queries the performance metrics of an ApsaraDB RDS instance. You can query the performance of an instance over a specific time range based on its performance metrics. Performance metrics are generated by using one of the following methods based on the database engine and version, RDS edition, monitoring frequency (ModifyDBInstanceMonitor), and query time range: Instances that run MySQL: 5-second monitoring frequency If the query time range is greater than seven days, performance metrics are collected at 1-day intervals. If the query time range is greater than one day but less than or equal to seven days, performance metrics are collected at 1-hour intervals. If the query time range is greater than or equal to an hour but less than or equal to one day, performance metrics are collected at 1-minute intervals. If the query time range is less than an hour, performance metrics are collected at 5-second intervals. 60-second monitoring frequency If the query time range is greater than 30 days, performance metrics are collected at 1-day intervals. If the query time range is greater than seven days but less than or equal to 30 days, performance metrics are collected at 1-hour intervals. If the query time range is less than or equal to seven days, performance metrics are collected at 1-minute intervals. 300-second monitoring frequency If the query time range is greater than 30 days, performance metrics are collected at 1-day intervals. If the query time range is greater than seven days but less than or equal to 30 days, performance metrics are collected at 1-hour intervals. If the query time range is less than or equal to seven days, performance metrics are collected at 5-minute intervals. Instances that run PostgreSQL with local SSDs or standard SSDs: If the query time range is less than or equal to an hour, performance metrics are collected at 5second intervals. If the query time range is less than or equal to 2 hours, performance metrics are collected at 10second intervals. If the query time range is less than or equal to 6 hours, performance metrics are collected at 30second intervals. If the query time range is less than or equal to 12 hours, performance metrics are collected at 1minute intervals. If the query time range is less than or equal to one day, performance metrics are collected at 2minute intervals. If the query time range is less than or equal to five days, performance metrics are collected at 10minute intervals. If the query time range is less than or equal to 15 days, performance metrics are collected at 30minute intervals. If the query time range is less than or equal to 30 days, performance metrics are collected at 1hour intervals. If the query time range is greater than 30 days, performance metrics are collected at 1-day intervals. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstan cePerformance | The operation that you want to perform. Set the value to DescribeDBInst ancePerf ormance. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| Key | String | Yes | MySQL Sessions _ | The performance metrics that you want to query. Separate multiple performance metrics with commas (,). For more information, see Performance parameters. Not e If you set the Key parameter to MySQL SpaceUsage or _ SQLServer SpaceUsage, you can _ query the performance metric only over one day. |
| StartTime | String | Yes | 2012-06- 08T15:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. Not e The time span between the beginning time and the end time must be longer than the monitoring frequency. Otherwise, this operation may return an empty parameter. |
| EndTime | String | Yes | 2012-06- 18T15:00Z | The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. Not e The time span between the beginning time and the end time must be longer than the monitoring frequency. Otherwise, this operation may return an empty parameter. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | rm- uf6wjk5xxxxxxxxxx | The ID of the instance. |
| Engine | String | MySQL | The database engine of the instance. |
| StartTime | String | 2012-06-10T15:00Z | The start time of the query. The time follows the ISO 8601 standard in the yyyy- MM-ddTHH:mmZ format. The time is displayed in UTC. |
| EndTime | String | 2012-06-19T15:00Z | The end time of the query. The time follows the ISO 8601 standard in the yyyy-MM- ddTHH:mmZ format. The time is displayed in UTC. |
| PerformanceKe ys | Array of PerformanceKe y |   | Details of the performance metrics. |
| PerformanceKe y |   |   |   |
| Key | String | MySQL Sessions _ | The name of the performance metric. |
| Unit | String | KB | The unit of the performance metric. |
| ValueFormat | String | recv k&sent k _ _ | The format that the value of the performance metric follows. Multiple values of the performance metric are separated by the &amp; string. Example: com delete&amp;com insert&amp;com ins _ _ _ ert select&amp;com replace. _ _ |
| Values | Array of PerformanceVa lue |   | An array that consists of values of the performance metric in the following format: {value1, value2, ...}. |
| PerformanceVa lue |   |   |   |
| Value | String | 0.0&13.6 | The value of the performance metric. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Date | String | 2011-05- 30T03:29:00Z | The date and time when the value of the performance metric was recorded. The time follows the ISO 8601 standard in the yyyy- MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| RequestId | String | A5409D02-D661- 4BF3-8F3D- 0A814D0574E7 | The ID of the request. |

Sample requests

```
http(s)://rds.example.com/?Action=DescribeDBInstancePerformance &DBInstanceId= rm-uf6wjk5xxxxxxx &Key=MySQL_Sessions &StartTime=2012-06-08T15:00Z &EndTime=2012-06-18T15:00Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeDBInstancePerformanceResponse>
      <RequestId>A5409D02-D661-4BF3-8F3D-0A814D0574E7</RequestId>
      <DBInstanceID> rm-uf6wjk5xxxxxxx</DBInstanceID>
      <StartTime>2012-06-11T15:00Z</StartTime>
      <EndTime>2013-10-17T15:00Z</EndTime>
      <Engine>MySQL</Engine>
      <PerformanceKeys>
            <PerformanceKey>
                  <Key>MySQL_NetworkTraffic</Key>
                  <Unit>KB</Unit>
                  <ValueFormat>recv_k&amp;sent_k</ValueFormat>
                  <Values></Values>
            </PerformanceKey>
      </PerformanceKeys>
</DescribeDBInstancePerformanceResponse>
```

`JSON` format `{`

```json
    "RequestId": "A5409D02-D661-4BF3-8F3D-0A814D0574E7",
    "DBInstanceID": " rm-uf6wjk5xxxxxxx",
    "StartTime": "2012-06-11T15:00Z",
    "EndTime": "2013-10-17T15:00Z",
    "Engine": "MySQL",
    "PerformanceKeys": {
        "PerformanceKey": [
```

`{`

```json
                "Key": "MySQL_NetworkTraffic",
                "Unit": "KB",
                "ValueFormat": "recv_k&sent_k",
                "Values": {
                    "PerformanceValue": []
```

`}` `}` `]` `}` `}`

#### 2.11.3 DescribeDBInstanceMonitor

Queries the monitoring frequency of an ApsaraDB RDS instance. This operation is not supported for instances that run PostgreSQL. The query granularity of these instances is self-adaptive based on the query time range. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstan ceMonitor | The operation that you want to perform. Set the value to DescribeDBInst anceMonit or. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Period | String | 60 | The monitoring frequency. Unit: seconds. |
| RequestId | String | 30829FD4-1A84- 4C2A-A625- 2EADECB95CA3 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeDBInstanceMonitor &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeDBInstanceMonitorResponse>
      <period>60</period>
      <requestId>30829FD4-1A84-4C2A-A625-2EADECB95CA3</requestId>
</DescribeDBInstanceMonitorResponse>
```

`JSON` format `{`

```json
    "period": "60",
    "requestId": "30829FD4-1A84-4C2A-A625-2EADECB95CA3"
```

`}`

#### 2.11.4 ModifyDBInstanceMonitor

Modifies the monitoring frequency of an ApsaraDB RDS instance. ApsaraDB RDS provides different monitoring frequency settings for different instances. For more information, see Set a monit oring f requency in ApsaraDB RDS User Guide. This operation is not supported for instances that run PostgreSQL. The query granularity of these instances is self-adaptive based on the query time range. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstance Monitor | The operation that you want to perform. Set the value to Modif yDBInst anceMonit or. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| Period | String | Yes | 60 | The new monitoring frequency. Valid values: 5 10 60 300 Unit: seconds. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 52B9805C-432C- 4ED1-83FD- 2F916B6D2733 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ModifyDBInstanceMonitor &DBInstanceId=rm-uf6wjk5xxxxxxx &Period=60 &<Common request parameters>
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

`}` Error codes

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidDBInstanceId. NotFound | The DBInstanceId provided does not exist in our records. | The error message returned because the specified instance does not exist. |

### 2.12 Parameter management

#### 2.12.1 DescribeParameters

Queries the parameter configurations of an ApsaraDB RDS instance. Before you call this operation, make sure that the instance runs one of the following database engines: MySQL SQL Server PostgreSQL PolarDB Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeParamet ers | The operation that you want to perform. Set the value to DescribeParamet ers. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Engine | String | MySQL | The database engine of the instance. |
| EngineVersion | String | 5.7 | The database engine version of the instance. |
| RunningParame ters | Array of DBInstancePara meter |   | The running parameters of the instance. |
| DBInstancePara meter |   |   |   |
| ParameterNam e | String | fill factor | The name of the parameter. |
| ParameterValu e | String | 0 | The value of the parameter. |
| ParameterDescr iption | String | This option sets the default fill factor value within the server scope. A fill factor is provided to optimize index data storage and performance. | The description of the parameter. |
| ConfigParamet ers | Array of DBInstancePara meter |   | The parameters that are being synchronized. After you modify and submit parameters, you must wait for the parameters to be synchronized to the instance. After the synchronization is complete, these parameters are removed from the list. |
| DBInstancePara meter |   |   |   |

| psaraDB for RDS |   |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ParameterNam e | String | fill factor | The name of the parameter. |
| ParameterValu e | String | 50 | The value of the parameter. |
| ParameterDescr iption | String | This option sets the default fill factor value within the server scope. A fill factor is provided to optimize index data storage and performance. | The description of the parameter. |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeParameters &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeParametersResponse>
   <ConfigParameters>
      <DBInstanceParameter>
         <ParameterDescription> This option sets the default fill factor value within the s
erver scope. A fill factor is provided to optimize index data storage and performance. </Pa rameterDescription>
         <ParameterName>fill factor</ParameterName>
         <ParameterValue>50</ParameterValue>
      </DBInstanceParameter>
   </ConfigParameters>
   <Engine>mssql</Engine>
   <EngineVersion>2008r2</EngineVersion>
   <RunningParameters>
      <DBInstanceParameter>
         <ParameterDescription> This option sets the default fill factor value within the s
erver scope. A fill factor is provided to optimize index data storage and performance. </Pa rameterDescription>
         <ParameterName>fill factor</ParameterName>
         <ParameterValue>0</ParameterValue>
      </DBInstanceParameter>
   </RunningParameters>
   <RequestId>2A748162-8040-4D6B-813E-6910C8C033F1</RequestId>
</DescribeParametersResponse>
```

`JSON` format `{`

```json
  "ConfigParameters": {
      "DBInstanceParameter": [
```

`{`

```json
              "ParameterDescription": "This parameter sets the default fill factor value wi
thin the server scope. A fill factor is provided to optimize index data storage and perform ance.",
              "ParameterName": "fill factor",
              "ParameterValue": "50"
```

`}` `]` `},`

```json
  "Engine": "mysql",
  "EngineVersion": "5.7",
  "RunningParameters": {
      "DBInstanceParameter": [
```

`{`

```json
              "ParameterDescription": "This parameter sets the default fill factor value wi
thin the server scope. A fill factor is provided to optimize index data storage and perform ance.",
              "ParameterName": "fill factor",
              "ParameterValue": "0"
```

`}` `]` `},`

```json
  "RequestId": "2A748162-8040-4D6B-813E-6910C8C033F1"
```

`}`

#### 2.12.2 ModifyParameter

Modifies the parameters of an ApsaraDB RDS instance. You can modify the parameters directly or by using a parameter template. After you submit the parameter modification request, ApsaraDB RDS starts a task to apply the new parameter values to the instance. If a new parameter value takes effect only after the instance restarts, ApsaraDB RDS restarts the instance. Before you execute a parameter modification task, ApsaraDB RDS checks whether the parameters exist, whether they are editable, and whether the new parameter values are valid. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyParameter | The operation that you want to perform. Set the value to Modif yParamet er. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| Parameters | String | No | {"delayed insert _ _ timeout":"600"," max length for _ _ _ sort data":"2048 _ "} | The JSON strings of parameters and their values. All the parameter values are of the string type. Format: {"Parameter name 1":"Parameter value 1","Parameter name 2":"Parameter value 2"...} Not e If you specify this parameter, you do not need to specify the Paramet erGroupId parameter. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| Forcerestart | Boolean | No | false | Specifies whether to restart the instance for a new parameter value to take effect. Valid values: t rue: The system forcibly restarts the instance. If a new parameter value takes effect only after the instance starts, you must set this parameter to true. Otherwise, the new parameter value cannot take effect. f alse: The system does not forcibly restart the instance. Default value: f alse. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ParameterGroupI d | String | No | rpg-xxxxxxxxx | The ID of the parameter template. Not e If you specify this parameter, you do not need to specify the Paramet ers parameter. If the parameter template applies only after you restart the instance, you must specify the Forcerest art parameter. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 542BB8D6-4268- 45CC-A557- B03EFD7AB30A | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ModifyParameter &DBInstanceId=rm-uf6wjk5xxxxxxx &Parameters={"delayed_insert_timeout":"600","max_length_for_sort_data":"2048"} &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyParameterResponse>
         <RequestId>542BB8D6-4268-45CC-A557-B03EFD7AB30A</RequestId>
</ModifyParameterResponse>
```

`JSON` format `{`

```json
       "RequestId":"542BB8D6-4268-45CC-A557-B03EFD7AB30A"
```

`}`

#### 2.12.3 DescribeModifyParameterLog

Queries the parameter modification logs of an ApsaraDB RDS instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeModifyPa rameterLog | The operation that you want to perform. Set the value to DescribeModif yParamet erLog. |
| DBInstanceId | String | Yes | rm-uf6wjk5xxxxx | The ID of the instance. |
| StartTime | String | Yes | 2020-03- 01T00:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. |
| EndTime | String | Yes | 2020-03- 01T10:00Z | The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30 50 100 Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | rm-uf6wjk5xxxxx | The ID of the instance. |
| Engine | String | mysql | The database engine of the instance. |
| EngineVersion | String | 5.6 | The database engine version of the instance. |
| Items | Array of ParameterChan geLog |   | Details of parameter modification log entries. |
| ParameterChan geLog |   |   |   |
| ModifyTime | String | 1584076066000 | The time when the parameter was modified. This value is a UNIX timestamp. Unit: milliseconds. |
| NewParameter Value | String | 3 | The new value of the parameter. |
| OldParameterV alue | String | 8 | The original value of the parameter. |
| ParameterNam e | String | innodb stats sampl _ _ e pages _ | The name of the parameter. |
| Status | String | Syncing | The status of the new value specified for the parameter. Valid values: Applied: The new value has taken effect. Syncing: The new value is being applied and has not taken effect. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCou nt | Integer | 1 | The number of entries returned per page. |
| RequestId | String | C8E88DED-533F- 4B3C-9207- 731FBF394CCA | The ID of the request. |
| TotalRecordCo unt | Integer | 1 | The total number of entries returned. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeModifyParameterLog &DBInstanceId=rm-uf6wjk5xxxxx &StartTime=2020-03-01T00:00Z &EndTime=2020-03-01T10:00Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeModifyParameterLogResponse>
  <EngineVersion>5.6</EngineVersion>
  <Engine>mysql</Engine>
  <RequestId>C8E88DED-533F-4B3C-9207-731FBF394CCA</RequestId>
  <DBInstanceId>rm-uf6wjk5xxxxx</DBInstanceId>
  <PageNumber>1</PageNumber>
  <PageRecordCount>1</PageRecordCount>
  <TotalRecordCount>1</TotalRecordCount>
  <Items>
        <ParameterChangeLog>
              <Status>Syncing</Status>
              <ModifyTime>1584076066000</ModifyTime>
              <NewParameterValue>3</NewParameterValue>
              <OldParameterValue>8</OldParameterValue>
              <ParameterName>innodb_stats_sample_pages</ParameterName>
        </ParameterChangeLog>
  </Items>
</DescribeModifyParameterLogResponse>
```

`JSON` format

```json
{"EngineVersion":"5.6",
   "Engine":"mysql",
   "RequestId":"C8E88DED-533F-4B3C-9207-731FBF394CCA",
   "DBInstanceId":"rm-uf6wjk5xxxxx",
   "PageNumber":"1",
   "PageRecordCount":"1",
   "TotalRecordCount":"1",
   "Items":
    {"ParameterChangeLog":
      [{"Status":"Syncing",
        "ModifyTime":"1584076066000",
        "NewParameterValue":"3",
        "OldParameterValue":"8",
        "ParameterName":"innodb_stats_sample_pages"}]}
```

`}`

### 2.13 Log management

#### 2.13.1 DescribeSlowLogs

Queries the summary of slow query logs of an ApsaraDB RDS instance. Before you call this operation, make sure that the ApsaraDB RDS instance runs one of the following database engine versions and RDS editions: MySQL (except MySQL 5.7 on RDS Basic Edition) SQL Server 2008 R2 PolarDB Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSlowLog s | The operation that you want to perform. Set the value to DescribeSlowLogs. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| EndTime | String | Yes | 2011-05-30Z | The end of the time range to query. It must be later than the beginning time. The time span between the beginning time and the end time must be equal to or less than 31 days. Specify the time in the yyyy-MM-ddZ format. |
| StartTime | String | Yes | 2011-05-01Z | The beginning of the time range to query. Specify the time in the yyyy-MM- ddZ format. |
| DBName | String | No | RDS MySQL _ | The name of the database. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SortKey | String | No | TotalExecutionCo unts | The dimension based on which to sort the query results. Valid values: T ot alExecut ionCount s: sorts the query results based on the total number of executions. T ot alQueryT imes: sorts the query results based on the total execution duration. T ot alLogicalReads: sorts the query results based on the total number of logical reads. T ot alPhysicalReads: sorts the query results based on the total number of physical reads. Not e This parameter is supported only for instances that run SQL Server 2008 R2. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid value: 30 to 100. Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. Pages start from page 1. Default value: 1. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Engine | String | MySQL | The database engine of the instance. |
| StartTime | String | 2011-05-30Z | The start date of the query. |
| EndTime | String | 2011-05-30Z | The end date of the query. |
| TotalRecordCo unt | Integer | 5 | The total number of entries returned. |
| PageNumber | Integer | 1 | The page number of the returned page. |

| psaraDB for RDS |   |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageRecordCou nt | Integer | 10 | The number of SQL statements returned on the current page. |
| Items | Array of SQLSlowLog |   | Details of the slow query logs. |
| SQLSlowLog |   |   |   |
| DBName | String | RDS MySQL _ | The name of the database. |
| SQLText | String | select id,name from tb table _ | The SQL statement returned. |
| SQLServerTotal ExecutionCount s | Long | 1 | The total executions of the SQL statement if the instance runs SQL Server. |
| MySQLTotalExe cutionCounts | Long | 1 | The total executions of the SQL statement if the instance runs MySQL. |
| SQLServerTotal ExecutionTimes | Long | 1000 | The total execution duration of the SQL statement if the instance runs SQL Server. Unit: milliseconds. |
| MySQLTotalExe cutionTimes | Long | 1 | The total execution duration of the SQL statement if the instance runs MySQL. Unit: seconds. |
| MaxExecutionTi me | Long | 60 | The longest execution duration of the SQL statement among all logged execution durations. Unit: seconds. |
| ReportTime | String | 2011-05-30Z | The date when the data report was generated. |
| TotalLockTime s | Long | 0 | The total lock duration. Unit: seconds. |
| MaxLockTime | Long | 0 | The longest lock duration. Unit: seconds. |
| ParseTotalRow Counts | Long | 1 | The total number of rows parsed by the SQL statement. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ParseMaxRowC ount | Long | 1 | The maximum number of rows parsed by the SQL statement. |
| ReturnTotalRo wCounts | Long | 1 | The total number of rows returned by the SQL statement. |
| ReturnMaxRow Count | Long | 1 | The maximum number of rows returned by the SQL statement. |
| CreateTime | String | 2011-05-30Z | The date when the data was generated. |
| AvgExecutionTi me | Long | 1 | The average execution duration. Unit: seconds. |
| SQLHASH | String | U2FsdGVkxxxx | The unique ID of the SQL statement in the slow query log statistics. You can use the unique ID to query the details of slow query logs on the SQL statement. |
| SQLId | Long | 1111 | The ID of the SQL statement. |
| SQLIdStr | String | 521584 | The ID of the SQL statement in the statistical template of slow query logs. This parameter is replaced by the SQLHASH parameter. |
| SlowLogId | Long | 26584213 | The ID of slow query summary. |
| TotalLogicalRe adCounts | Long | 1 | The total number of logical reads. |
| TotalPhysicalRe adCounts | Long | 1 | The total number of physical reads. |
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | The ID of the instance. |
| RequestId | String | 2553A660-E4EB- 4AF4-A402- 8AFF70A49143 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeSlowLogs &DBInstanceId=rm-uf6wjk5xxxxxxx &StartTime=2011-05-01Z &EndTime=2011-05-30Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeSlowLogsResponse>
    <RequestId>A5409D02-D661-4BF3-8F3D-0A814D0574E7</RequestId>
    <DBInstanceID>rm-uf6wjk5xxxxxxx</DBInstanceID>
    <Engine>SQLServer</Engine>
    <StartTime>2011-06-11Z</StartTime>
    <EndTime>2011-12-11Z</EndTime>
    <TotalRecordCount>1</TotalRecordCount>
    <PageNumber>1</PageNumber>
    <PageRecordCount>1</PageRecordCount>
    <Items>
        <SQLSlowLog>
          <SQLText>update test.zxb set id=0 limit 1</SQLText>
          <SQLServerTotalExecutionCounts>178</SQLServerTotalExecutionCounts>
          <SQLServerTotalExecutionTimes>189</SQLServerTotalExecutionTimes>
          <TotalLogicalReadcounts>89</TotalLogicalReadcounts>
          <TotalPhysicalReadcounts>90</TotalPhysicalReadcounts>
          <ReportTime>2013-11-12Z</ReportTime>
       </SQLSlowLog>
    </Items>
</DescribeSlowLogsResponse>
```

`JSON` format `{`

```json
    "DescribeSlowLogs": {
        "RequestId": "A5409D02-D661-4BF3-8F3D-0A814D0574E7",
        "DBInstanceID": "rm-uf6wjk5xxxxxxx",
        "Engine": "SQLServer",
        "StartTime": "2011-06-11Z",
        "EndTime": "2011-12-11Z",
        "TotalRecordCount": "1",
        "PageNumber": "1",
        "PageRecordCount": "1",
        "Items": {
            "SQLSlowLog": {
                "SQLText": "update test.zxb set id=0 limit 1",
                "SQLServerTotalExecutionCounts": "178",
                "SQLServerTotalExecutionTimes": "189",
                "TotalLogicalReadcounts": "89",
                "TotalPhysicalReadcounts": "90",
                "ReportTime": "2013-11-12Z"
```

`}` `}` `}` `}`

#### 2.13.2 DescribeSlowLogRecords

Queries the details of slow query logs of an ApsaraDB RDS instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSlowLog Records | The operation that you want to perform. Set the value to DescribeSlowLogRecords. |
| DBInstanceId | String | Yes | rm-uf6wjk5xxxxxx | The ID of the instance. |
| EndTime | String | Yes | 2020-06- 18T16:00Z | The end of the time range to query. The end time must be later than the start time. The time span between the start time and the end time must be less than 31 days. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| StartTime | String | Yes | 2020-06- 17T16:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. |
| SQLHASH | String | No | U2FsdGVkxxxx | The unique ID of the SQL statement in the slow query log statistics. You can use the unique ID to query the details of slow query logs on the SQL statement. |
| SQLId | Long | No | 1111 | The ID of the SQL statement. |
| DBName | String | No | RDS MySQL _ | The name of the database. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid value: 30 to 100. Default value: 30 |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Engine | String | MySQL | The database engine of the instance. |
| TotalRecordCo unt | Integer | 1 | The total number of entries returned. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCou nt | Integer | 1 | The number of SQL statements returned on the current page. |
| Items | Array of SQLSlowRecord |   | Details of slow query logs. |
| SQLSlowRecord |   |   |   |

|   | Developer Guide·AP | I reference |   | ApsaraDB for RD | S |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| HostAddress | String | xxx[xxx] @ [1xx.xxx.xxx.xx] | The name and IP address of the client that is connected to the database. |
| DBName | String | testDB | The name of the database. |
| SQLText | String | select sleep(2) | Details of the SQL statement. |
| QueryTimes | Long | 2 | The execution duration of the slow query. Unit: seconds. |
| LockTimes | Long | 0 | The lock duration of the slow query. Unit: seconds. |
| ParseRowCount s | Long | 1 | The number of entries parsed. |
| ReturnRowCoun ts | Long | 1 | The number of entries returned. |
| ExecutionStartT ime | String | 2020-06- 18T01:40:44Z | The time when the SQL statement started to be executed. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | The ID of the instance. |
| RequestId | String | 4DBB1BB0-E5D8- 4D41-B1C9- 142364DB4986 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeSlowLogRecords &DBInstanceId=rm-uf6wjk5xxxxxxx &StartTime=2020-06-17T16:00Z &EndTime=2020-06-18T16:00Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
</DescribeSlowLogRecordsResponse> <TotalRecordCount>1</TotalRecordCount> <PageRecordCount>1</PageRecordCount> <RequestId>4DBB1BB0-E5D8-4D41-B1C9-142364DB4986</RequestId> <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId> <PageNumber>1</PageNumber> <Items>
    <SQLSlowRecord>
        <QueryTimes>2</QueryTimes>
        <ExecutionStartTime>2020-07-20T02:03:10Z</ExecutionStartTime>
        <ReturnRowCounts>1</ReturnRowCounts>
        <LockTimes>0</LockTimes>
        <DBName>testDB</DBName>
        <ParseRowCounts>1</ParseRowCounts>
        <HostAddress>test1[test1] @  [100.xxx.xxx.xxx]</HostAddress>
        <QueryTimeMS>2000</QueryTimeMS>
        <SQLText>select sleep(2)</SQLText>
    </SQLSlowRecord>
</Items> <Engine>MySQL</Engine> </DescribeSlowLogRecordsResponse>
```

`JSON` format `{`

```json
    "TotalRecordCount": 1,
    "PageRecordCount": 1,
    "RequestId": "4DBB1BB0-E5D8-4D41-B1C9-142364DB4986",
    "DBInstanceId": "rm-uf6wjk5xxxxxxx",
    "PageNumber": 1,
    "Items": {
        "SQLSlowRecord": [
```

`{`

```json
                "QueryTimes": 2,
                "ExecutionStartTime": "2020-07-20T02:03:10Z",
                "ReturnRowCounts": 1,
                "LockTimes": 0,
                "DBName": "testDB",
                "ParseRowCounts": 1,
                "HostAddress": "test1[test1] @  [100.xxx.xxx.xxx]",
                "QueryTimeMS": 2000,
                "SQLText": "select sleep(2)"
```

`}` `]` `},`

```json
    "Engine": "MySQL"
```

`}`

#### 2.13.3 DescribeErrorLogs

Queries the error logs of an ApsaraDB RDS instance within a specific time range. Error logs contain the time when they were generated and the error messages. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeErrorLog s | The operation that you want to perform. Set the value to DescribeErrorLogs. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| EndTime | String | Yes | 2011-05- 30T20:10Z | The end of the time range to query. The end time must be later than the start time. The time span between the start time and the end time must be less than 31 days. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |
| StartTime | String | Yes | 2011-05- 01T20:10Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid value: 30 to 100. Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalRecordCo unt | Integer | 100 | The total number of entries returned. |
| PageNumber | Integer | 1 | The page number of the returned page. |

| psaraDB for RDS |   |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageRecordCou nt | Integer | 30 | The number of error logs on the current page. |
| Items | Array of ErrorLog |   | Details of error logs. |
| ErrorLog |   |   |   |
| ErrorInfo | String | spid52 DBCC TRACEON 3499, server process ID (SPID) 52. This is an informational message only; no user action is required | The error message. |
| CreateTime | String | 2011-05- 30T12:11:04Z | The time when the error log was generated. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| RequestId | String | 98504E07-BB0E- 40FC-B152- E4882615812C | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeErrorLogs &DBInstanceId=rm-uf6wjk5xxxxxxx &StartTime=2011-05-01T20:10Z &EndTime=2011-05-30T20:10Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeErrorLogsResponse>
      <RequestId>98504E07-BB0E-40FC-B152-E4882615812C</RequestId>
      <PageNumber>1</PageNumber>
      <TotalRecordCount>1</TotalRecordCount>
      <PageRecordCount>1</PageRecordCount>
      <Items>
            <ErrorLog>
                  <ErrorInfo>spid52 DBCC TRACEON 3499, server process ID (SPID) 52. This is
an informational message only; no user action is required</ErrorInfo>
                  <CreateTime>2013-06-04T15:00:00</CreateTime>
            </ErrorLog>
      </Items>
</DescribeErrorLogsResponse>
```

`JSON` format `{`

```json
"RequestId":"98504E07-BB0E-40FC-B152-E4882615812C", "PageNumber":1, "TotalRecordCount":1, "PageRecordCount":1, "Items": {"ErrorLog":
```

`[` `{`

```json
"ErrorInfo":"spid52 DBCC TRACEON 3499, server process ID (SPID) 52. This is an informationa l message only; no user action is required", "CreateTime":"2013-06-04T15:00:00"
```

`}` `]` `}` `}`

#### 2.13.4 DescribeBinlogFiles

Queries the log backup files of an ApsaraDB RDS instance. If the DownloadLink value is null, ApsaraDB RDS does not provide a download URL. If the DownloadLink value is not null, ApsaraDB RDS provides a download URL for a log backup file. The expiration time of the URL is specified by the LinkExpiredT ime parameter. You must download the log backup file before the expiration time. This operation returns SQL log entries that are generated over a specific time range. The beginning of the time range must be earlier than or equal to the time that is specified by the LogEndTime parameter. In addition, the end of the time range must be later than or equal to the time that is specified by the LogBeginTime parameter. This operation is not supported for instances that run SQL Server. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBinlogFil es | The operation that you want to perform. Set the value to DescribeBinlogFiles. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| EndTime | String | Yes | 2011-06- 20T15:00:00Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |
| StartTime | String | Yes | 2011-06- 01T15:00:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid value: 30 to 100. Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalRecordCo unt | Integer | 100 | The total number of log backup files returned. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCou nt | Integer | 30 | The number of log backup files returned on the current page. |
| Items | Array of BinLogFile |   | Details of log backup files. |

| D | eveloper Guide·AP | I reference |   | ApsaraDB for RD | S |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| BinLogFile |   |   |   |
| FileSize | Long | 2269410 | The size of the log backup file. Unit: byte. |
| LogBeginTime | String | 2019-02- 09T17:45:21Z | The start time of the log data recorded in the log backup file. The time follows the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time is displayed in UTC. |
| LogEndTime | String | 2019-02- 15T13:10:28Z | The end time of the log data recorded in the log backup file. The time follows the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time is displayed in UTC. |
| DownloadLink | String | http://rdsxxxxx.oss. aliyuncs.com/xxxxxx | The HTTP download URL. If this parameter is set to null, no download link is available. |
| HostInstanceID | String | 5841973 | The number of the instance to which the log backup file belongs. This parameter is used to indicate whether the log backup file is generated on a primary instance or a secondary instance. |
| LinkExpiredTim e | String | 2013-06- 09T18:00:00Z | The expiration time of the URL. The time follows the ISO 8601 standard in the yyyy- MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| Checksum | String | 18358304393468701 857 | The checksum. |
| IntranetDownlo adLink | String | http://rdslog-hz- v3.oss-cn- hangzhou- internal.aliyuncs.co m/xxxxxx | The download URL that is used over an internal network. |
| LogFileName | String | 00000004000000000 0000019 | The name of the log backup file. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | ED169A3E-1657- 4104-82AB- 24EA8CD0DB75 | The ID of the request. |
| TotalFileSize | Long | 2269410 | The total size of the log backup files returned. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeBinlogFiles &DBInstanceId=rm-uf6wjk5xxxxxxx &StartTime=2011-06-01T15:00:00Z &EndTime=2011-06-20T15:00:00Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeBinlogFilesResponse>
      <Items></Items>
      <PageNumber>1</PageNumber>
      <TotalRecordCount>0</TotalRecordCount>
      <TotalFileSize>0</TotalFileSize>
      <RequestId>ED169A3E-1657-4104-82AB-24EA8CD0DB75</RequestId>
      <PageRecordCount>0</PageRecordCount>
</DescribeBinlogFilesResponse>
```

`JSON` format `{`

```json
    "Items": {
        "BinLogFile": []
```

`},`

```json
    "PageNumber": 1,
    "TotalRecordCount": 0,
    "TotalFileSize": "0",
    "RequestId": "ED169A3E-1657-4104-82AB-24EA8CD0DB75",
    "PageRecordCount": 0
```

`}`

#### 2.13.5 DescribeSQLCollectorPolicy

Queries the status of the SQL Explorer (SQL Audit) feature on an ApsaraDB RDS instance. Before you call this operation, make sure that the ApsaraDB RDS instance runs one of the following database engines: MySQL SQL Server PostgreSQL PolarDB Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSQLColle ctorPolicy | The operation that you want to perform. Set the value to DescribeSQLCollect orPolicy. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| SQLCollectorSt atus | String | Enable | The status of the SQL Explorer (SQL Audit) feature. Valid values: Enable Disabled |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | The ID of the request. |
| StoragePeriod | Integer | 0 | None |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeSQLCollectorPolicy &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeSQLCollectorPolicyResponse>
      <requestId>C3565F9F-76E9-4F7E-A662-D1B2488EC2FC</requestId>
      <SQLCollectorStatus>Enable</SQLCollectorStatus></DescribeSQLCollectorPolicyResponse>
```

`JSON` format `{`

```json
    "requestId": "C3565F9F-76E9-4F7E-A662-D1B2488EC2FC",
    "SQLCollectorStatus": "Enable"
```

`}`

#### 2.13.6 ModifySQLCollectorPolicy

Enables or disables the SQL Explorer (SQL Audit) feature for an ApsaraDB RDS instance. Before you call this operation, make sure that the ApsaraDB RDS instance runs one of the following database engines: MySQL SQL Server PostgreSQL PolarDB Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySQLCollect orPolicy | The operation that you want to perform. Set the value to Modif ySQLCollect orPolicy. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| SQLCollectorStat us | String | Yes | Enable | Specifies whether to enable or disable the SQL Explorer (SQL Audit) feature. Valid values: Enable and Disabled. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| StoragePeriod | Integer | No | 0 | An invalid parameter. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ModifySQLCollectorPolicy &DBInstanceId=rm-uf6wjk5xxxxxxx &SQLCollectorStatus=Enable &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifySQLCollectorPolicyResponse>
      <requestId>C3565F9F-76E9-4F7E-A662-D1B2488EC2FC</requestId>
</ModifySQLCollectorPolicyResponse>
```

`JSON` format `{`

```json
    "requestId": "C3565F9F-76E9-4F7E-A662-D1B2488EC2FC",
```

`}`

#### 2.13.7 DescribeSQLLogRecords

Queries the logs that are generated by the SQL Explorer (SQL Audit) feature on an ApsaraDB RDS instance. Before you call this operation, make sure that the ApsaraDB RDS instance runs one of the following database engines: MySQL SQL Server PostgreSQL PolarDB Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSQLLogR ecords | The operation that you want to perform. Set the value to DescribeSQLLogRecords. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| EndTime | String | Yes | 2011-06- 11T15:00:00Z | The end of the time range to query. The end time must be later than the start time. The time span between the start time and the end time must be less than 31 days. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |
| StartTime | String | Yes | 2011-06- 01T15:00:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| SQLId | Long | No | 25623548 | The unique ID of the SQL statement. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| QueryKeywords | String | No | rds | The keywords that are used for the query. Separate multiple keywords with spaces. A maximum of 10 keywords are allowed. |
| Database | String | No | Database | The name of the database. If you specify this parameter, this operation returns only the log entries that are generated for the specified database. If you do not specify this parameter, this operation returns the log entries that are generated for all databases on the instance. |
| User | String | No | user | The name of the database account to query. If you specify this parameter, this operation returns only the log entries that are generated for the specified database account. If you do not specify this parameter, this operation returns the log entries that are generated for all database accounts on the instance. |
| Form | String | No | Stream | Specifies whether to generate SQL audit log files or return SQL audit log entries. Default value: Stream. Valid values: File: generates audit log files. If you set this parameter to File, only common response parameters are returned. You must call the DescribeSQLLogFiles operation to obtain the download URL of audit log files. St ream: returns SQL audit log entries. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid value: 30 to 100. Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalRecordCo unt | Integer | 100 | The total number of entries returned. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCou nt | Integer | 30 | The number of SQL audit logs on the current page. |
| Items | Array of SQLRecord |   | Details of SQL audit logs. |
| SQLRecord |   |   |   |
| DBName | String | testDB | The name of the database. |
| AccountName | String | accounttest | The name of the account that was used to execute the SQL statement. |
| HostAddress | String | 192.168.0.121 | The IP address of the client that was connected to the database. |
| SQLText | String | update test.zxb set id=0 limit 1 | The SQL statement returned. |
| TotalExecution Times | Long | 600 | The execution duration of the SQL statement. Unit: microseconds. |
| ReturnRowCoun ts | Long | 30 | The number of entries returned. |
| ThreadID | String | 1025865428 | The thread ID. |
| ExecuteTime | String | 2011-06- 11T15:00:23Z | The time when the SQL statement was executed. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| RequestId | String | 08A3B71B-FE08- 4B03-974F- CC7EA6DB1828 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeSQLLogRecords &DBInstanceId=rm-uf6wjk5xxxxxx &StartTime=2011-06-01T15:00:00Z &EndTime=2011-06-11T15:00:00Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeSQLLogRecordsResponse>
      <PageNumber>1</PageNumber>
      <TotalRecordCounts>1</TotalRecordCounts>
      <ItemsCounts>1</ItemsCounts>
      <SQLItems>
            <SQLItem>
                  <DBName>test</DBName>
                  <AccountName>accounttest</AccountName>
                  <HostAddress>192.168.0.121</HostAddress>
                  <SQLText>update test.zxb set id=0 limit 1</SQLText>
                  <TotalExecutionTimes>12</TotalExecutionTimes>
                  <ReturnRowCounts>34</ReturnRowCounts>
                  <ExecuteTime>2011-06-11T15:00:23Z</ExecuteTime>
            </SQLItem>
      </SQLItems>
      <RequestId>08A3B71B-FE08-4B03-974F-CC7EA6DB1828</RequestId>
</DescribeSQLLogRecordsResponse>
```

`JSON` format `{`

```json
"PageNumber":1, "TotalRecordCounts":1, "ItemsCounts":1, "SQLItems": {"SQLItem":
```

`[` `{`

```json
"DBName":"test", "AccountName":"accounttest", "HostAddress":"192.168.0.121", "SQLText":"update test.zxb set id=0 limit 1", "TotalExecutionTimes":12, "ReturnRowCounts":34, "ExecuteTime":"2011-06-11T15:00:23Z"
```

`}` `]` `},`

```json
"RequestId": "08A3B71B-FE08-4B03-974F-CC7EA6DB1828"
```

`}`

#### 2.13.8 DescribeSQLLogFiles

Queries the audit log files that the SQL Explorer (SQL Audit) feature generates for an ApsaraDB RDS instance. Before you call this operation, make sure that the ApsaraDB RDS instance runs one of the following database engines: MySQL SQL Server 2008 R2 PostgreSQL PolarDB Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSQLLogFi les | The operation that you want to perform. Set the value to DescribeSQLLogFiles. |
| DBInstanceId | String | Yes | rm-uf6wjk5xxxxxx | The ID of the instance. |
| FileName | String | No | custinsxxxxx.csv | The name of the audit log file. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. Valid value: 30 t o 200. Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. Valid values: 1 t o 100000. Default value: 1. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalRecordCo unt | Integer | 10 | The total number of entries returned. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCou nt | Integer | 10 | The number of entries returned on the current page. |

| Developer Guide·AP | I reference |   | ApsaraDB for RD |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | Array of LogFile |   | Details of audit log files. |
| LogFile |   |   |   |
| FileID | String | custinsxxxxx.csv | The name of the audit log file. |
| LogStatus | String | Success | The state of the audit log file. Valid values: Success Failed Generat ing |
| LogStartTime | String | 2015-05- 23T07:00:00Z | The beginning of the time range within which audit logs were recorded. The time follows the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time is displayed in UTC. |
| LogEndTime | String | 2015-05- 24T07:00:00Z | The end of the time range within which audit logs were recorded. The time follows the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time is displayed in UTC. |
| LogDownloadU RL | String | http://rdslog-hz- v3.oss-cn- hangzhou.aliyuncs.c om/xxxxx | The download URL. If audit log files cannot be downloaded, this parameter is empty. |
| LogSize | String | 3000 | The size of the audit log file. Unit: byte. |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeSQLLogFiles &DBInstanceId=rm-uf6wjk5xxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeSQLLogFilesResponse>
      <items>
            <FileID>ZUBaS964T3OYtxxxxxxxx</FileID>
            <LogStatus>Success</LogStatus>
            <LogStartTime>2015-05-23T07:00:00Z</LogStartTime>
            <LogEndTime>2015-05-23T07:00:00Z</LogEndTime>
            <LogDownloadURL>xxxxxx.cn-hangzhou.oss.aliyun-inc.com/xxxxx</LogDownloadURL>
            <LogSize>257</LogSize>
      </items>
      <pageRecordCount>1</pageRecordCount>
      <requestId> 1AD222E9-E606-4A42-BF6D-8A4442913CEF</requestId>
      <totalRecordCount>1</totalRecordCount>
</DescribeSQLLogFilesResponse>
```

`JSON` format `{`

```json
    "items": [
```

`{`

```json
            "FileID": "ZUBaS964T3OYtxxxxxxxx",
            "LogStatus": "Success",
            "LogStartTime": "2015-05-23T07:00:00Z",
            "LogEndTime": "2015-05-23T07:00:00Z",
            "LogDownloadURL": "xxxxxx.cn-hangzhou.oss.aliyun-inc.com/xxxxx",
            "LogSize": "257"
```

`}` `],`

```json
    "pageRecordCount": 1,
    "requestId": " 1AD222E9-E606-4A42-BF6D-8A4442913CEF",
    "totalRecordCount": 1
```

`}`

#### 2.13.9 DescribeSQLLogReportList

Queries the SQL log reports of an ApsaraDB RDS instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSQLLogR eportList | The operation that you want to perform. Set the value to DescribeSQLLogReport List . |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |

| D | eveloper Guide·API r | eference |   |   | ApsaraDB for RD | S |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| EndTime | String | Yes | 2021-03- 18T16:00:00Z | The end of the time range to query. Specify the time in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. Not e The end time must be later than the start time. |
| StartTime | String | Yes | 2021-03- 13T16:00:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30 50 100 Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer greater than 0. Default value: 1. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | Array of Item |   | Details of SQL log reports. |
| Item |   |   |   |
| LatencyTopNIte ms | Array of LatencyTopNIte m |   | Details of the SQL statements executed with the highest latency. |
| LatencyTopNIte m |   |   |   |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AvgLatency | Long | 500 | The average amount of time that is required to execute the SQL statement. Unit: milliseconds. |
| SQLExecuteTim es | Long | 5 | The number of SQL statement executions. |
| SQLText | String | SELECT * FROM table name; _ | The SQL statement returned. Not e Only the first 128 characters of the SQL statement are returned. In addition, only the SQL statements that take longer than 100 milliseconds to execute are returned. |
| QPSTopNItems | Array of QPSTopNItem |   | Details of the SQL statements executed the most frequently. |
| QPSTopNItem |   |   |   |
| SQLExecuteTim es | Long | 5 | The number of SQL statement executions. |
| SQLText | String | SELECT * FROM table name; _ | The SQL statement returned. Not e Only the first 128 characters of the SQL statement are returned. In addition, only the SQL statements that take longer than 5 milliseconds to execute are returned. |
| ReportTime | String | 2019-03- 27T16:00:00Z | The time when the report was generated. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCou nt | Integer | 30 | The number of SQL log reports on the current page. |
| RequestId | String | 08A3B71B-FE08- 4B03-974F- CC7EA6DB1828 | The ID of the request. |

| Developer Guide·AP | I reference |   | ApsaraDB for RD |
|---|---|---|---|
| Parameter | Type | Example | Description |

| TotalRecordCo unt | Integer | 60 | The total number of entries returned. |
|---|---|---|---|

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeSQLLogReportList &DBInstanceId=rm-uf6wjk5xxxxxxx &EndTime=2021-03-18T16:00:00Z &StartTime=2021-03-13T16:00:00Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeSQLLogReportListResponse>
      <TotalRecordCount>60</TotalRecordCount>
      <PageRecordCount>30</PageRecordCount>
      <RequestId>08A3B71B-FE08-4B03-974F-CC7EA6DB1828    </RequestId>
      <PageNumber>1</PageNumber>
      <Items>
            <Item>
                  <ReportTime>2019-03-27T16:00:00Z</ReportTime>
                  <LatencyTopNItems>
                        <LatencyTopNItem>
                              <AvgLatency>500</AvgLatency>
                              <SQLExecuteTimes>5</SQLExecuteTimes>
                              <SQLText>SELECT * FROM table_name;</SQLText>
                        </LatencyTopNItem>
                  </LatencyTopNItems>
                  <QPSTopNItems>
                        <QPSTopNItem>
                              <SQLExecuteTimes>5</SQLExecuteTimes>
                              <SQLText>SELECT * FROM table_name;</SQLText>
                        </QPSTopNItem>
                  </QPSTopNItems>
            </Item>
      </Items>
</DescribeSQLLogReportListResponse>
```

`JSON` format `{`

```json
    "TotalRecordCount": "60",
    "PageRecordCount": "30",
    "RequestId": "08A3B71B-FE08-4B03-974F-CC7EA6DB1828\t",
    "PageNumber": "1",
    "Items": {
        "Item": [{
            "ReportTime": "2019-03-27T16:00:00Z",
            "LatencyTopNItems": {
                "LatencyTopNItem": [{
                    "AvgLatency": "500",
                    "SQLExecuteTimes": "5",
                    "SQLText": "SELECT * FROM table_name;"
```

`}]` `},`

```json
            "QPSTopNItems": {
                "QPSTopNItem": [{
                    "SQLExecuteTimes": "5",
                    "SQLText": "SELECT * FROM table_name;"
```

`}]` `}` `}]` `}` `}`

#### 2.13.10 PurgeDBInstanceLog

Deletes log backup files from an ApsaraDB RDS instance. ApsaraDB RDS allows an instance to automatically upload log backup files to Object Storage Service (OSS) buckets. If the remaining storage space of an instance is insufficient, you can also manually upload the log backup files of the instance to OSS buckets. After the log backup files of an instance are uploaded, ApsaraDB RDS deletes these files from the instance to release storage space. When this operation is called, log backup files are uploaded from an instance to OSS buckets, and then are deleted from the instance. If the instance runs SQL Server, transaction log backup files are compressed before they are uploaded. This operation is supported only for instances that run MySQL or SQL Server. When you upload log backup files, the data restoration feature is not affected. This operation is called to release storage space. The backup storage usage is not reduced. The OSS buckets to which log backup files are uploaded are provided by ApsaraDB RDS. You do not need to purchase these OSS buckets. In addition, you cannot access these OSS buckets. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | PurgeDBInstanceL og | The operation that you want to perform. Set the value to PurgeDBInst anceLog. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=PurgeDBInstanceLog &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<PurgeDBInstanceLogResponse>
      <RequestId> 65BDA532-28AF-4122-AA39-B382721EEE64</RequestId></PurgeDBInstanceLogRespo
nse>
```

`JSON` format `{`

```json
  "RequestId": " 65BDA532-28AF-4122-AA39-B382721EEE64"
```

`}`

### 2.14 Event history management

#### 2.14.1 DescribeActionEventPolicy

Queries the status of the event history feature for an ApsaraDB RDS instance. The event history feature enables you to view the events that occurred within a region over a specific time range. Such historical events include instance creation and parameter modification. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeActionEv entPolicy | The operation that you want to perform. Set the value to DescribeAct ionEvent Policy. |
| RegionId | String | Yes | cn-hangzhou | The region ID. You can call the DescribeRegions operation to query the most recent region list. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| EnableEventLog | String | True | Indicates whether the event history feature was enabled for the region. |
| RegionId | String | cn-hangzhou | The ID of the region. |
| RequestId | String | CCECD3CD-AB2D- 4F6D-BEDE- 47BC90A398D2 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeActionEventPolicy &Region=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeActionEventPolicyResponse>
  <RequestId>CCECD3CD-AB2D-4F6D-BEDE-47BC90A398D2</RequestId>
      <RegionId>cn-hangzhou</RegionId>
      <EnableEventLog>True</EnableEventLog>
    </DescribeActionEventPolicyResponse>
```

`JSON` format `{`

```json
    "RequestId": "CCECD3CD-AB2D-4F6D-BEDE-47BC90A398D2",
    "RegionId": "cn-hangzhou",
    "EnableEventLog": "True"
```

`}`

#### 2.14.2 DescribeEvents

Queries the events of ApsaraDB RDS instances within a region. The event history feature enables you to view the events that occurred within a region over a specific time range. Such historical events include instance creation and parameter modification. Before you call this operation, make sure that the event history feature is enabled. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeEvents | The operation that you want to perform. Set the value to DescribeEvent s. |
| RegionId | String | Yes | cn-hangzhou | The region ID. You can call the DescribeRegions operation to query the most recent region list. |
| ResourceType | String | No | instance | The type of the resource associated with an event. Set the value to inst ance. |
| ResourceName | String | No | rm- bp1z306********** | The name of the resource associated with an event. Set the value to an instance ID. |
| StartTime | String | No | 2019-06- 11T15:00:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| EndTime | String | No | 2019-06- 12T15:00:00Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30 50 100 Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| EventItems | Array of EventItems |   | Details of the events. |
| EventItems |   |   |   |
| EventId | Integer | 11000053 | The ID of the event. |
| EventName | String | ModifySecurityIPList | The name of the event. |
| EventPayload | String | {\"Domain\": \"rds- inc- share.aliyuncs.com\ ", \"Api\": \"ReleaseInstancePu blicConnection\"} | The request or context parameters of the event. |
| EventReason | String | FROM USER _ | The source of the event. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| EventRecordTi me | String | 2019-08- 20T01:12:49Z | The time when the event was recorded. The time is slightly later than the time when the event occurred. |
| EventTime | String | 2019-08- 20T01:08:22Z | The time when the event occurred. |
| EventType | String | NetworkManageme nt | The type of the event. |
| EventUserType | String | SYSTEM | The type of the user who executed the event. |
| RegionId | String | cn-hangzhou | The ID of the region. |
| ResourceName | String | rm- bp1z3065m9976ix8a | The name of the resource associated with the event. Only an instance ID is supported. |
| ResourceType | String | instance | The type of the resource associated with the event. Only instances are supported for this parameter. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 30 | The number of entries returned per page. |
| RequestId | String | A103039D-B1B2- 4C57-B989- 7D7C0DA95426 | The ID of the request. |
| TotalRecordCo unt | Integer | 40 | The total number of entries returned. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeEvents &Region=cn-hangzhou &StartTime=2019-08-20T01:30:00Z &EndTime=2019-08-20T01:35:00Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeEventsResponse>
  <EventItems>
            <EventItems>
                  <EventName>ModifySecurityIPList</EventName>
                  <EventUserType>SYSTEM</EventUserType>
                  <ResourceType>instance</ResourceType>
                  <EventPayload></EventPayload>
                  <EventTime>2019-08-20T01:33:43Z</EventTime>
                  <RegionId>cn-hangzhou</RegionId>
                  <EventRecordTime>2019-08-20T01:33:57Z</EventRecordTime>
                  <EventReason>FROM_SYSTEM</EventReason>
                  <EventId>11000048</EventId>
                  <ResourceName>rm-bpxxxxxxx</ResourceName>
                  <EventType>SecurityManagement</EventType>
            </EventItems>
            <EventItems>
                  <EventName>ModifySecurityIPList</EventName>
                  <EventUserType>SYSTEM</EventUserType>
                  <ResourceType>instance</ResourceType>
                  <EventPayload></EventPayload>
                  <EventTime>2019-08-20T01:33:43Z</EventTime>
                  <RegionId>cn-hangzhou</RegionId>
                  <EventRecordTime>2019-08-20T01:33:57Z</EventRecordTime>
                  <EventReason>FROM_SYSTEM</EventReason>
                  <EventId>11000047</EventId>
                  <ResourceName>rm-bpxxxxxxx</ResourceName>
                  <EventType>SecurityManagement</EventType>
            </EventItems>
      </EventItems>
      <TotalRecordCount>2</TotalRecordCount>
      <PageNumber>1</PageNumber>
      <PageSize>2</PageSize>
      <RequestId>B5FF9EE6-830E-4DBE-8498-9890A62D2875</RequestId>
</DescribeEventsResponse>
```

`JSON` format `{`

```json
    "EventItems": {
        "EventItems": [
```

`{`

```json
                "EventName": "ModifySecurityIPList",
                "EventUserType": "SYSTEM",
                "ResourceType": "instance",
                "EventPayload": "",
                "EventTime": "2019-08-20T01:33:43Z",
                "RegionId": "cn-hangzhou",
                "EventRecordTime": "2019-08-20T01:33:57Z",
                "EventReason": "FROM_SYSTEM",
                "EventId": 11000048,
                "ResourceName": "rm-bpxxxxxxx",
                "EventType": "SecurityManagement"
```

`},` `{`

```json
                "EventName": "ModifySecurityIPList",
                "EventUserType": "SYSTEM",
                "ResourceType": "instance",
                "EventPayload": "",
                "EventTime": "2019-08-20T01:33:43Z",
                "RegionId": "cn-hangzhou",
                "EventRecordTime": "2019-08-20T01:33:57Z",
                "EventReason": "FROM_SYSTEM",
                "EventId": 11000047,
                "ResourceName": "rm-bpxxxxxxx",
                "EventType": "SecurityManagement"
```

`}` `]` `},`

```json
    "TotalRecordCount": 2,
    "PageNumber": 1,
    "PageSize": 2,
    "RequestId": "B5FF9EE6-830E-4DBE-8498-9890A62D2875"
```

`}` Error codes

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidStartTime.For mat | Specified start time is not valid. | The error message returned because the specified start time is invalid. |

#### 2.14.3 ModifyActionEventPolicy

Enables or disables the event history feature for an ApsaraDB RDS instance. The event history feature enables you to view the events that occurred within a region over a specific time range. Such historical events include instance creation and parameter modification. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyActionEven tPolicy | The operation that you want to perform. Set the value to Modif yAct ionEvent Policy. |
| EnableEventLog | String | Yes | True | Specifies whether to enable the event history feature. Valid values: T rue and False. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region for which you want to enable the event history feature. You can call the DescribeRegions operation to query the most recent region list. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| EnableEventLog | String | True | Indicates whether the event history feature was enabled for the region. |
| RegionId | String | cn-hangzhou | The ID of the region. |
| RequestId | String | BAC0952C-0EB3- 4DE7-A567- B83269BFE43F | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ModifyActionEventPolicy &Region=cn-hangzhou &EnableEventLog=True &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyActionEventPolicyResponse>
   <RequestId>BAC0952C-0EB3-4DE7-A567-B83269BFE43F</RequestId>
   <RegionId>cn-hangzhou</RegionId>
   <EnableEventLog>True</EnableEventLog>
</ModifyActionEventPolicyResponse>
```

`JSON` format `{`

```json
    "RequestId": "BAC0952C-0EB3-4DE7-A567-B83269BFE43F",
    "RegionId": "cn-hangzhou",
    "EnableEventLog": "True"
```

`}`

### 2.15 Performance optimization and diagnostics (CloudDBA)

diagnostics (CloudDBA)

#### 2.15.1 CreateDiagnosticReport

Creates a diagnostic report for an ApsaraDB RDS instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateDiagnostic Report | The operation that you want to perform. Set the value to Creat eDiagnost icReport . |
| DBInstanceId | String | Yes | rm-uf6wjk5xxxxxx | The ID of the instance. |
| StartTime | String | Yes | 2018-06- 11T15:00Z | The start time of the monitoring data that is included in the generated diagnostic report. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |
| EndTime | String | Yes | 2018-06- 12T15:00Z | The end time of the monitoring data that is included in the generated diagnostic report. Specify the time in the ISO 8610 standard in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ReportId | String | 10166270 | The ID of the diagnostic report. |
| RequestId | String | 8DA8956A-53DA- 423E-9540- 387428ED37FF-5711 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=CreateDiagnosticReport &DBInstanceId=rm-uf6wjk5xxxxxx &StartTime=2018-06-11T15:00Z &EndTime=2018-06-12T15:00Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateDiagnosticReportResponse>
   <reportId>10166270</reportId>
   <requestId>8DA8956A-53DA-423E-9540-387428ED37FF-5711</requestId></CreateDiagnosticReport
Response>
```

`JSON` format `{`

```json
    "reportId": "10166270",
    "requestId": "8DA8956A-53DA-423E-9540-387428ED37FF-5711"
```

`}`

#### 2.15.2 DescribeDiagnosticReportList

Queries diagnostic reports of an ApsaraDB RDS instance. This operation returns the details of diagnostic reports such as the time range of monitoring data, report generation time, and download URL. The diagnostic reports are retained for 15 days. This operation is not supported for instances that run SQL Server 2017 EE. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDiagnosti cReportList | The operation that you want to perform. Set the value to DescribeDiagnosticReportList. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B7E9A79C-DE1B- 4398-845F- D654FC0958BD | The ID of the request. |
| ReportList | Array of Report |   | Details of the diagnostic reports. |
| DiagnosticTime | String | 2018-01- 17T12:46:09Z | The time when the diagnostic report was generated. |
| DownloadURL | String | http://rdsreport- hz-v3.oss-cn- hangzhou.aliyuncs.c om/xxxxx | The public download URL. If the diagnostic report cannot be downloaded, this parameter returns an empty string. |
| EndTime | String | 2018-01- 10T15:31:00Z | The end time of the monitoring data. |
| Score | Integer | 100 | The diagnostic score. |
| StartTime | String | 2018-01- 10T15:30:00Z | The start time of the monitoring data. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeDiagnosticReportList &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeDiagnosticReportListResponse>
      <reportList>
            <diagnosticTime>2018-01-17T12:46:09Z</diagnosticTime>
            <downloadURL>http://rdsreport-hzi-v2.oss-cn-hangzhou-i.aliyuncs.com/xxxxx</down
loadURL>
            <endTime>2018-01-10T15:31:00Z</endTime>
            <score>100</score>
            <startTime>2018-01-10T15:30:00Z</startTime>
      </reportList>
      <requestId>B7E9A79C-DE1B-4398-845F-D654FC0958BD</requestId></DescribeDiagnosticReport
ListResponse>
```

`JSON` format `{`

```json
    "reportList": [
```

`{`

```json
            "diagnosticTime": "2018-01-17T12:46:09Z",
            "downloadURL": "http://rdsreport-hzi-v2.oss-cn-hangzhou-i.aliyuncs.com/xxxxx",
            "endTime": "2018-01-10T15:31:00Z",
            "score": 100,
            "startTime": "2018-01-10T15:30:00Z"
```

`}` `],`

```json
    "requestId": "B7E9A79C-DE1B-4398-845F-D654FC0958BD"
```

`}`

### 2.16 Data migration

#### 2.16.1 CreateUploadPathForSQLServer

Obtains the information used to upload files. This operation is supported only for instances that run SQL Server. You can call this operation to create a username and password to log on to the file server, and a path to upload files. This information can be used to upload data files. After the upload is complete, you can migrate external data. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The database is in the running state. Up to 20 files can be created for a single database per day. A 24-hour period is considered a single day. For example, if the last creation time was 2012-03-15 18:30:12, the next creation time must be later than 2012-03-16 18:30:12. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateUploadPat hForSQLServer | The operation that you want to perform. Set the value to Creat eUploadPat hForSQLServer. |
| DBInstanceId | String | Yes | rm-bp1********** | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| DBName | String | Yes | test | The name of the database. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| InternetFtpServ er | String | 10.230.239.1 | The IP address of the file server on the Internet. |
| InternetPort | Integer | 3021 | The port of the file server on the Internet. |
| UserName | String | test | The username used to log on to the file server. |
| Password | String | test12345 | The password used to log on to the file server. |
| FileName | String | testdb01 13705724 _ 75975.bak | The name of the data file with the extension. |
| IntranetFtpserv er | String | None | The IP address of the file server on the internal network. |
| Intranetport | Integer | 0 | The port of the file server on the internal network. |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=CreateUploadPathForSQLServer &DBInstanceId=rdsaiiabnaiiabn &DBName=RDS_MySQL &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateUploadPathForSQLServerResponse>
         <RequestId>66816822-CEC1-4C8D-AB26-2530A7D4DCA5</RequestId>
         <InternetFtpServer>10.230.239.1</InternetFtpServer>
         <InternetPort>3021</InternetPort>
         <IntranetFtpServer></IntranetFtpServer>
         <IntranetPort></IntranetPort>
         <UserName>test</UserName>
         <Password>test12345</Password>
         <FileName>testdb01_1370572475975.bak</FileName>
</CreateUploadPathForSQLServerResponse>
```

`JSON` format `{`

```json
    "CreateUploadPathForSQLServerResponse": {
        "RequestId": "66816822-CEC1-4C8D-AB26-2530A7D4DCA5",
        "InternetFtpServer": "10.230.239.1",
        "InternetPort": "3021",
        "UserName": "test",
        "Password": "test12345",
        "FileName": "testdb01_1370572475975.bak"
```

`}` `}` Error codes

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 403 | FTPServiceUnavailabl e | The request has failed due to a temporary failure of the FTP server. | The error message returned because an FTP server error occurred. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 403 | OperationDenied.DB Status | The operation is not permitted due to status of database. | The error message returned because this operation is not supported when the instance or database is in the read-only state. Before you call this operation on an ApsaraDB RDS for SQL Server instance of the dedicated instance family, make sure that the following requirements are met: 1. The instance is in the running state. 2. The instance does not have temporary backup tasks. 3. The instance does not have migration tasks. 4. The instance does not have restoration tasks. 5. Files have been uploaded and are valid. |

#### 2.16.2 DescribeFilesForSQLServer

Queries the details of data files for an ApsaraDB RDS instance. This operation returns the username used to log on to the file server. After data files are uploaded, their states are updated. This operation also returns the states of data files. If data files are available, you can migrate the data files and view their migration progress information. This operation is supported only for instances that run SQL Server. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeFilesForS QLServer | The operation that you want to perform. Set the value to DescribeFilesForSQLServer. |
| DBInstanceId | String | Yes | rm- bp1842vmucoa5 w874 | The ID of the instance. |
| StartTime | String | Yes | 2011-06- 11T16:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| EndTime | String | Yes | 2011-06- 11T16:00Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNumber | Integer | No | 5 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | rdsaiiabnaiiabn | The ID of the instance. |
| TotalRecordCo unt | Integer | 1 | The total number of entries returned. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCou nt | Integer | 1 | The number of SQL statements on the current page. |
| Items | Array of SQLServerUploa dFile |   | Details of the data files. |
| SQLServerUploa dFile |   |   |   |
| DBName | String | testdb01 | The name of the database. |
| FileName | String | testdb01 13705724 _ 75975.bak | The name of the data file with the extension. |
| FileSize | Long | 1243435 | The size of the data file. Unit: byte. |

| eveloper Guide·AP | I reference |   | ApsaraDB for RD |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| InternetFtpServ er | String | 10.230.239.1 | The IP address of the file server on the Internet. |
| InternetPort | Integer | 3021 | The port of the file server on the Internet. |
| IntranetFtpserv er | String | Empty | The IP address of the file server on the internal network. |
| Intranetport | Integer | 0 | The port of the file server on the internal network. |
| UserName | String | MKEakJbyG | The username used to log on to the file server. |
| Password | String | aT2Y XN1GGnOLzm _ | The password used to log on to the file server. |
| FileStatus | String | Success | The state of the data file. Valid values: Unavailable Available NotStarted Uploading UploadFailed Virus Deleted Success |
| CreationTime | String | 2014-06- 11T15:02:40Z | The time when the FTP file was generated. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Description | String | 2 | The description of the file status. Valid values: 0: The file upload is not started. 1: The file is being uploaded. 2: The file is uploaded and can be migrated. 3: The file failed to be uploaded because the upload is canceled or a network error occurred. You can upload the file again. 4: The file is uploaded but a virus is detected. 5: The file is deleted. |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | The ID of the request. |

Examples Sample requests

```
https://rds.example.com/?Action=DescribeFilesForSQLServer &DBInstanceId=rm-bp1842vmucoa5w874 &EndTime=2011-06-11T16:00Z &StartTime=2011-06-11T16:00Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeFilesForSQLServerResponse>
      <PageNumber>1</PageNumber>
      <TotalRecordCount>1</TotalRecordCount>
      <PageRecordCount>1</PageRecordCount>
      <Items>
            <SQLServerUploadFile>
                  <DBName>testdb01</DBName>
                  <FileName>testdb01_1370572475975.bak</FileName>
                  <FileSize>1243435</FileSize>
                  <InternetFtpServer>10.230.239.1</InternetFtpServer>
                  <InternetPort>3021</InternetPort>
                  <IntranetFtpServer></IntranetFtpServer>
                  <IntranetPort></IntranetPort>
                  <UserName>MKEakJbyG</UserName>
                  <Password>aT2Y_XN1GGnOLzm</Password>
                  <FileStatus>Success </FileStatus>
                  <CreationTime>2014-06-11T15:02:40Z</CreationTime>
            </SQLServerUploadFile>
      </Items>
      <RequestId>08A3B71B-FE08-4B03-974F-CC7EA6DB1828</RequestId></DescribeFilesForSQLServe
rResponse>
```

`JSON` format `{`

```json
    "PageNumber":1,
    "TotalRecordCount":1,
    "PageRecordCount":1,
    "Items":{
        "SQLServerUploadFile":[
```

`{`

```json
                "DBName":"testdb01",
                "FileName":"testdb01_1370572475975.bak",
                "FileSize ":"1243435",
                "InternetFtpServer ":"10.230.239.1",
                "InternetPort":3021,
                "IntranetFtpServer":"",
                "IntranetPort":"",
                "UserName":"MKEakJbyG",
                "Password":"aT2Y_XN1GGnOLzm",
                "FileStatus":"Success ",
                "CreationTime":"2014-06-11T15:02:40Z"
```

`}` `]` `},`

```json
    "RequestId":"08A3B71B-FE08-4B03-974F-CC7EA6DB1828"
```

`}` Error codes

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 403 | FTPServiceUnavailabl e | The request has failed due to a temporary failure of the FTP server. | The error message returned because an FTP server error occurred. |

#### 2.16.3 ImportDatabaseBetweenInstances

Migrates data across ApsaraDB RDS instances. We recommend that you use Data Transmission Service (DTS). DTS provides data migration, subscription, and synchronization features to help you establish stable and secure transmission links. During migration, the source instance changes to the Migrat ing state and the destination instance changes to the Import ing Dat a state. Before you call this operation, make sure that the following requirements are met: The source and destination instances run SQL Server and belong to the dedicated or dedicated host instance family. For more information about instance types, see Inst ance t ypes in ApsaraDB RDS Product Int roduct ion. The source and destination instances are created by using the same user credentials. The source and destination instances are in the running state. The source and destination databases are in the running state. The remaining storage space of the destination instance is greater than the storage space occupied by the source database. This operation is not supported for instances that run SQL Server 2017 EE. You can migrate the data of multiple databases at a time. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ImportDatabaseB etweenInstances | The operation that you want to perform. Set the value to Import Dat abaseBet weenInst ances. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInfo | String | Yes | {"DBNames": ["mydb","mydb2" ]} | The names of the source and destination databases. The value of this parameter is a JSON string. Not e For the source and destination instances that run SQL Server, the value of this parameter consists of one or more key-value pairs. In each key-value pair, the key specifies the name of the source database, and the value specifies the name of the destination database. A source database can have a different name from its destination database. Example: {"DBNames": {"srcdb":"destdb","srcdb2" :"destmydb2"}} In the preceding example, the data of the source database srcdb is migrated to the destination database destdb, and the data of the source database srcdb2 is migrated to the destination database destmydb2. The name of each source or destination database must be unique. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the destination instance. |
| SourceDBInstance Id | String | Yes | rm- g4a1jk8xxxxxxx | The ID of the source instance. The source and destination instances cannot have the same ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ImportId | String | 85265475235 | The ID of the migration task. |
| RequestId | String | 5A77D650-27A1- 4E08-AD9E- 59008EDB6927 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ImportDatabaseBetweenInstances &DBInstanceId=rm-uf6wjk5xxxxxxx &SourceDBInstanceId=rm-g4a1jk8xxxxxxx &DBInfo={"DBNames":["mydb","mydb2"]} &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ImportDatabaseBetweenInstancesResponse>
           <ImportId>2122321</ImportId>
         <RequestId>5A77D650-27A1-4E08-AD9E-59008EDB6927</RequestId>
</ImportDatabaseBetweenInstancesResponse>
```

`JSON` format `{`

```json
       "ImportId":2122321,
       "RequestId":"5A77D650-27A1-4E08-AD9E-59008EDB6927"
```

`}`

#### 2.16.4 CancelImport

Cancels a migration task of an ApsaraDB RDS instance. This operation is supported for instances that run SQL Server and belong to the dedicated or dedicated host instance family. This operation is not supported for instances that run SQL Server 2017 EE. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CancelImport | The operation that you want to perform. Set the value to CancelImport . |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ImportId | Integer | Yes | 8562584 | The ID of the migration task. Not e This parameter is returned when the migration task is initiated. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 17F57FEE-EA4F- 4337-8D2E- 9C23CAA63D74 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=CancelImport &DBInstanceId=rm-uf6wjk5xxxxxxx &ImportId=8562584 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CancelImportResponse>
         <RequestId>17F57FEE-EA4F-4337-8D2E-9C23CAA63D74</RequestId>
</CancelImportResponse>
```

`JSON` format `{`

```json
  "RequestId": " 17F57FEE-EA4F-4337-8D2E-9C23CAA63D74"
```

`}`

#### 2.16.5 CreateMigrateTask

Creates a backup data migration task from Object Storage Service (OSS) to ApsaraDB RDS for SQL Server. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateMigrateTas k | The operation that you want to perform. Set the value to Creat eMigrat eT ask. |
| BackupMode | String | Yes | FULL | The type of the backup data migration task. Valid values: FULL: The backup data migration task migrates full backup files. UPDF: The backup data migration task migrates incremental or log backup files. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| DBName | String | Yes | testDB | The name of the destination database. |
| IsOnlineDB | String | Yes | True | Specifies whether to make the restored database data available for user access. Valid values: T rue False Not e Set the value to T rue for instances that run SQL Server 2008 R2. |
| CheckDBMode | String | No | AsyncExecuteDBC heck | The consistency check method for the database. Valid values: SyncExecut eDBCheck: synchronous database check AsyncExecut eDBCheck: asynchronous database check Default value: AsyncExecut eDBCheck (compatible with SQL Server 2008 R2). Not e This parameter is valid when IsOnlineDB is set to T rue. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| OssObjectPositio ns | String | No | oss-ap- southeast- 1.aliyuncs.com:rd smssqlsingapore :autotest 2008R _ 2 TestMigration _ _ FULL.bak | The location of the backup file in the OSS bucket. The parameter consists of the following parts that are separated by colons (:): The endpoint of the OSS bucket: oss-ap-southeast-1.aliyuncs.com. The name of the OSS bucket: rdsmssqlsingapore. The key of the backup file in the OSS bucket: autotest 2008R2 TestMigration FUL _ _ _ L.bak. Not e This parameter is optional for instances that run SQL Server 2008 R2. This parameter is required for instances that run a database engine later than SQL Server 2008 R2. |
| OSSUrls | String | No | check cdn oss.sh _ _ www.xxxxxx.mob i | The shared URL of the backup file in the OSS bucket. The URL must be encoded. If you specify multiple URLs, separate them with vertical bars (\|) and then encode them. Not e This parameter is required for instances that run SQL Server 2008 R2. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupMode | String | FULL | The type of the backup data migration task. Valid values: FULL: The backup data migration task migrates full backup files. UPDF: The backup data migration task migrates incremental or log backup files. |
| DBInstanceId | String | rm-uf6wjk5xxxxx | The ID of the instance. |
| DBName | String | test02 | The name of the database. |
| MigrateTaskId | String | 564563256 | The ID of the backup data migration task. |
| RequestId | String | 866F5EB8-4650- 4061-87F0- 379F6F968BCE | The ID of the request. |
| TaskId | String | 5451225 | The ID of the task. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=CreateMigrateTask &DBInstanceId=rm-uf6wjk5xxxxxxx &DBName=testDB &BackupMode=FULL &IsOnlineDB=True &OssObjectPositions=oss-ap-southeast-1.aliyuncs.com:rdsmssqlsingapore:autotest_2008R2_TestM igration_FULL.bak &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateMigrateTaskResponse>
      <MigrateTaskId>135847</MigrateTaskId>
      <DBInstanceId>rm-bp178grbxxxxxxx</DBInstanceId>
      <RequestId>5F2B3757-BD56-40B3-B5F2-FCDD9FA0E2E2</RequestId>
      <BackupMode>UPDF</BackupMode>
      <TaskId>128301751</TaskId>
      <DBName>test02</DBName>
</CreateMigrateTaskResponse>
```

`JSON` format `{`

```json
    "MigrateTaskId": "135847",
    "DBInstanceId": "rm-bp178grbxxxxxxx",
    "RequestId": "5F2B3757-BD56-40B3-B5F2-FCDD9FA0E2E2",
    "BackupMode": "UPDF",
    "TaskId": "128301751",
    "DBName": "test02"
```

`}` Error codes

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidDBName | The instance does not have the specified DB name. | The error message returned because the specified destination database does not exist. Check the name and state of the destination database or specify another database. |
| 400 | InvalidOSSURL | The Specified OSS URL is not valid | The error message returned because the specified OSS URL is invalid. |

#### 2.16.6 DescibeImportsFromDatabase

Queries the details of migration tasks for an ApsaraDB RDS instance. This operation is supported only for instances that run MySQL or SQL Server. For information about how to initiate a migration task, see ImportDatabaseBetweenInstances. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescibeImportsFr omDatabase | The operation that you want to perform. Set the value to DescibeImport sFromDat abase. |
| DBInstanceId | String | Yes | rm-bpxxxxx | The ID of the instance. |
| EndTime | String | Yes | 2011-06- 11T16:00Z | The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Engine | String | Yes | MySQL | The database engine of the instance. Valid values: MySQL SQLServer |
| StartTime | String | Yes | 2011-06- 11T15:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| ImportId | Integer | No | 123 | The ID of the migration task. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30 50 100 Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | Array of ImportResultFr omDB |   | Details of the migration tasks. |
| ImportResultFr omDB |   |   |   |

| D | eveloper Guide·AP | I reference |   | ApsaraDB for RD | S |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ImportDataStat us | String | NotStart | The state of the migration task. Valid values: Not St art : The migration task is not started. FullExport ing: The migration task is exporting full data. FullImport ing: The migration task is importing full data. Success: The migration task is successful. Failed: The migration task failed. Canceled: The migration task has been canceled. Canceling: The migration task is being canceled. Increment alWait ing: The migration task is waiting to synchronize incremental data. Increment alImport ing: The migration task is synchronizing incremental data. St opSyncing: The migration task has stopped synchronizing data. |
| ImportDataStat usDescription | String | Description | The description of the migration task. |
| ImportDataTyp e | String | Full | The type of the migration task. Valid values: Full: The migration task migrates full data. Increment al: The migration task migrates incremental data. |
| ImportId | Integer | 123 | The ID of the migration task. |
| IncrementalImp ortingTime | String | 2011-06-11T15:00Z | The time when the migration task synchronized incremental data. The time follows the ISO 8601 standard in the yyyy- MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| PageNumber | Integer | 1 | The page number of the returned page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageRecordCou nt | Integer | 1 | The number of entries returned per page. |
| RequestId | String | B000AA91-393D- 46F9-8D9B- 098E28931A3A | The ID of the request. |
| TotalRecordCo unt | Integer | 1 | The total number of entries returned. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescibeImportsFromDatabase &DBInstanceId=rm-bpxxxxx &EndTime=2011-06-11T16:00Z &Engine=MySQL &StartTime=2011-06-11T15:00Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescibeImportsFromDatabaseResponse>
  <TotalRecordCount>0</TotalRecordCount>
  <PageRecordCount>30</PageRecordCount>
  <RequestId>B000AA91-393D-46F9-8D9B-098E28931A3A</RequestId>
  <PageNumber>1</PageNumber>
  <Items>
        <ImportResultFromDB>
              <ImportId>123</ImportId>
              <ImportDataType>Full</ImportDataType>
              <ImportDataStatus>NotStart</ImportDataStatus>
              <ImportDataStatusDescription>Description</ImportDataStatusDescription>
              <IncrementalImportingTime></IncrementalImportingTime>
        </ImportResultFromDB>
  </Items>
</DescibeImportsFromDatabaseResponse>
```

`JSON` format `{`

```json
  "TotalRecordCount": 0,
  "PageRecordCount": 30,
  "RequestId": "B000AA91-393D-46F9-8D9B-098E28931A3A",
  "PageNumber": 1,
  "Items": {
    "ImportResultFromDB": [
```

`{`

```json
        "ImportId":"123",
        "ImportDataType":"Full",
        "ImportDataStatus":"NotStart",
        "ImportDataStatusDescription":"Description",
        "IncrementalImportingTime":""
```

`}` `]` `}` `}` Error codes

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 403 | OperationDenied.DBI nstanceType | The operation is not permitted due to type of instance. | The error message returned because this operation is not supported when the instance is not a primary instance. |

#### 2.16.7 DescribeMigrateTaskById

Queries a backup data migration task for an ApsaraDB RDS for SQL Server instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMigrateT askById | The operation that you want to perform. Set the value to DescribeMigrateTaskById. |
| DBInstanceId | String | Yes | rm- bp11e1tzgxxxx4o x | The ID of the instance. |
| MigrateTaskId | String | Yes | 235943 | The ID of the backup data migration task. You can call the DescribeMigrateTasks operation to query the IDs of migration tasks. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupMode | String | FULL | The type of the backup data migration task. Valid values: FULL: The backup data migration task migrates full backup files. UPDF: The backup data migration task migrates incremental or log backup files. |
| CreateTime | String | 2020-05- 30T12:11:04Z | The time when the backup data migration task was created. The time follows the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time is displayed in UTC. |
| DBInstanceNam e | String | rm- uf6wjk5xxxxxxxxxx | The ID of the instance. |
| DBName | String | mytestdb | The name of the database. |
| Description | String | Success to DBCC checkdb asynchronously | The description of the backup data migration task. |
| EndTime | String | 2021-05- 30T12:11:04Z | The time when the backup data migration task was complete. The time follows the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time is displayed in UTC. |
| IsDBReplaced | String | False | Indicates whether the imported data overwrites the existing data. Valid values: False T rue |
| MigrateTaskId | String | 235943 | The ID of the backup data migration task. |
| RequestId | String | 6ED3635A-01F9- 47BD-B9C8- CB3FD70A336E | The ID of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | String | Success | The state of the backup data migration task. Valid values: NoSt art : The backup data migration task is not started. Running: The backup data migration task is running. Success: The backup data migration task is successful. Failed: The migration task failed. Wait ing: The backup data migration task is waiting for an incremental backup file to be imported. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeMigrateTaskById &DBInstanceId=rm-bp11e1tzgxxxx4ox &MigrateTaskId=235943 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeMigrateTaskByIdResponse>
    <Status>Success</Status>
    <Description>Success to DBCC checkdb asynchronously</Description>
    <RequestId>B994DF29-44A1-43FD-A693-917930DFEBCE</RequestId>
    <EndTime>2021-03-04T13:50:23Z</EndTime>
    <MigrateTaskId>235943</MigrateTaskId>
    <CreateTime>2021-03-04T13:47:17Z</CreateTime>
    <BackupMode>FULL</BackupMode>
    <DBName>mytestdb</DBName>
    <DBInstanceName>rm-bp11e1tzgxxxxx4ox</DBInstanceName>
</DescribeMigrateTaskByIdResponse>
```

`JSON` format `{`

```json
  "Status": "Success",
  "Description": "Success",
  "RequestId": "6ED3635A-01F9-47BD-B9C8-CB3FD70A336E",
  "EndTime": "2021-03-04T13:47:58Z",
  "MigrateTaskId": "235943",
  "CreateTime": "2021-03-04T13:47:17Z",
  "BackupMode": "FULL",
  "DBName": "mytestdb",
  "DBInstanceName": "rm-bp11e1tzgxxxxx4ox"
```

`}`

#### 2.16.8 DescribeMigrateTasks

Queries backup data migration tasks for an ApsaraDB RDS for SQL Server instance. This operation allows you to query the backup data migration tasks that are created for an instance within the last week. This operation is supported only for full backup files. This operation is not supported for instances that run SQL Server 2017 EE. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMigrateT asks | The operation that you want to perform. Set the value to DescribeMigrat eT asks. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| EndTime | String | Yes | 2017-10- 25T01:00Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |
| StartTime | String | Yes | 2017-10- 20T01:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid value: 30 to 100. Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | The ID of the instance. |
| Items | Array of MigrateTask |   | The backup data migration tasks. |
| MigrateTask |   |   |   |
| BackupMode | String | FULL | The type of the backup data migration task. Valid values: FULL: The backup data migration task migrates full backup files. UPDF: The backup data migration task migrates incremental or log backup files. |
| CreateTime | String | 2017-05- 30T12:11:04Z | The time when the backup data migration task was created. The time follows the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time is displayed in UTC. |
| DBName | String | testDB | The name of the database. |
| Description | String | Api description | The description of the backup data migration task. |
| EndTime | String | 2017-05- 30T13:11:04Z | The time when the backup data migration task was complete. The time follows the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time is displayed in UTC. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| IsDBReplaced | String | True | Indicates whether the imported data overwrites the existing data. |
| MigrateTaskId | String | 564522545 | The ID of the backup data migration task. |
| Status | String | Success | The state of the backup data migration task. Valid values: NoSt art : The backup data migration task is not started. Running: The backup data migration task is running. Success: The backup data migration task is successful. Failed: The migration task failed. Wait ing: The backup data migration task is waiting for an incremental backup file to be imported. |
| PageRecordCou nt | Integer | 10 | The number of entries returned per page. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| RequestId | String | 4E356DDF-6B83- 45DB-99D5- 4B1E8A0D286B | The ID of the request. |
| TotalRecordCo unt | Integer | 30 | The total number of entries returned. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeMigrateTasks &DBInstanceId=rm-uf6wjk5xxxxxxx &StartTime=2017-10-20T01:00Z &EndTime=2017-10-25T01:00Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeMigrateTasksResponse>
      <RequestId>A5409D02-D661-4BF3-8F3D-0A814D0574E7</RequestId>
      <PageRecordCount>1</PageRecordCount>
      <PageNumber>1</PageNumber>
      <TotalRecordCount>10</TotalRecordCount>
      <Items>
            <MigrateTaskId>rm-bp1842vxxxxx</MigrateTaskId>
            <DBName>test02</DBName>
            <CreateTime>2017-05-30 T12:11:4Z</CreateTime>
            <EndTime>2017-05-30 T12:11:4Z</EndTime>
            <IsDBReplaced>True</IsDBReplaced>
            <Status>Success</Status>
            <BackupMode>FULL</BackupMode>
            <Description>Api description</Description>
      </Items>
</DescribeMigrateTasksResponse>
```

`JSON` format `{`

```json
    "RequestId": "A5409D02-D661-4BF3-8F3D-0A814D0574E7",
    "PageRecordCount": 1,
    "PageNumber": 1,
    "TotalRecordCount": 10,
    "Items": {
        "MigrateTaskId": "rm-bp1842vxxxxx",
        "DBName": "test02",
        "CreateTime": "2017-05-30 T12:11:4Z",
        "EndTime": "2017-05-30 T12:11:4Z",
        "IsDBReplaced": "True",
        "Status": "Success",
        "BackupMode": "FULL",
        "Description": "Api description"
```

`}` `}`

#### 2.16.9 DescribeOssDownloads

Queries the backup file details of a backup data migration task for an ApsaraDB RDS for SQL Server instance. This operation is not supported for instances that run SQL Server 2017 EE or SQL Server 2019 EE. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeOssDown loads | The operation that you want to perform. Set the value to DescribeOssDownloads. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| MigrateTaskId | String | Yes | 5625458541 | The ID of the backup data migration task. You can call the DescribeMigrateTasks operation to query the IDs of migration tasks. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | The ID of the instance. |
| Items | Array of OssDownload |   | Details of the backup files. |
| OssDownload |   |   |   |
| BackupMode | String | Database | The backup type. Valid values: Dat abase: full backup files Dif f erent ial Dat abase: incremental _ backup files T ransact ion Log: log backup files _ |
| CreateTime | String | 2017-08- 17T12:45:15Z | The time when the backup file was created in the download list. The time follows the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time is displayed in UTC. |
| Description | String | App description | The description of the backup file. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| FileName | String | test | The name of the backup file stored in Object Storage Service (OSS). |
| FileSize | String | 2 | The size of the backup file. Unit: MB |
| IsAvailable | String | True | Indicates whether the backup file is available. Valid values: T rue and False. |
| Status | String | Finished | The state of the backup file. Valid values: NoSt art Downloading Finished DownloadFailed Verif yFailed Delet ed Delet eFailed CheckSuccess CheckFailed Rest oring Rest ored Rest oredFailed |
| MigrateTaskId | String | 562154852 | The ID of the backup data migration task. |
| RequestId | String | A5409D02-D661- 4BF3-8F3D- 0A814D0574E7 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=DescribeOssDownloads &DBInstanceId=rm-uf6wjk5xxxxxxx &MigrateTaskId=5625458541 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeDBInstancesResponse>
      <RequestId>A5409D02-D661-4BF3-8F3D-0A814D0574E7</RequestId>
      <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
      <MigrateTaskId>562154852</MigrateTaskId>
      <Items>
            <OssDownload>
                  <Status>Finished</Status>
                  <Description>App description</Description>
                  <EndTime>2017-08-27T12:45:15Z</EndTime>
                  <IsAvailable>True</IsAvailable>
                  <BackupMode>Database</BackupMode>
                  <CreateTime>2017-08-17T12:45:15Z</CreateTime>
                  <FileName>test</FileName>
                  <FileSize>2</FileSize>
            </OssDownload>
      </Items>
</DescribeDBInstancesResponse>
```

`JSON` format `{`

```json
    "DescribeDBInstancesResponse": {
        "RequestId": "A5409D02-D661-4BF3-8F3D-0A814D0574E7",
        "DBInstanceId": "rm-uf6wjk5xxxxxxx",
        "MigrateTaskId": 562154852,
        "Items": {
            "OssDownload": {
                "Status": "Finished",
                "Description": "App description",
                "EndTime": "2017-08-27T12:45:15Z",
                "IsAvailable": "True",
                "BackupMode": "Database",
                "CreateTime": "2017-08-17T12:45:15Z",
                "FileName": "test",
                "FileSize": 2
```

`}` `}` `}` `}`

### 2.17 Tag management

#### 2.17.1 TagResources

Creates and adds tags to ApsaraDB RDS instances. If you have a large number of instances, you can create multiple tags and add these tags to the instances. Then, you can filter the instances by tag. A tag consists of a key and a value. Each key must be unique within a region for an Apsara Stack account. Different keys can be mapped to the same value. If the tag that you specify does not exist, this tag is automatically created and added to the specified instance. If the key of the specified tag is the same as that of an existing tag, the specified tag overwrites the existing tag. You can add up to 20 tags to each instance. You can add tags to up to 50 instances at a time. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | TagResources | The operation that you want to perform. Set the value to T agResources. |
| RegionId | String | Yes | cn-hangzhou | The region ID. You can call the DescribeRegions operation to query the most recent region list. |
| ResourceId.N | RepeatLi st | Yes | rm- uf6wjk5xxxxxxx | The ID of Instance N. You can add tags to N instances at a time. Valid values of N: 1 to 50. |
| ResourceType | String | Yes | INSTANCE | The type of the resource. Set the value to INST ANCE. |
| Tag.N.Key | String | No | testkey1 | The key of Tag N. You can create N tag keys at a time. Valid values of N: 1 to 20. This parameter cannot be an empty string. |
| Tag.N.Value | String | No | testvalue1 | The value of Tag N. You can create N tag values at a time. Valid values of N: 1 to 20. This parameter can be an empty string. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 224DB9F7-3100- 4899-AB9C- C938BCCB43E7 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=TagResources &RegionId=cn-hangzhou &ResourceType=INSTANCE &ResourceId.1=rm-uf6wjk5xxxxxxx &Tag.1.Key=testkey1 &Tag.1.Value=testvalue1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TagResourcesResponse>
  <RequestId>224DB9F7-3100-4899-AB9C-C938BCCB43E7</RequestId>
</TagResourcesResponse>
```

`JSON` format `{`

```json
    "RequestId":"224DB9F7-3100-4899-AB9C-C938BCCB43E7"
```

`}`

#### 2.17.2 AddTagsToResource

Adds existing or new tags to an ApsaraDB RDS instance. This operation has the following limits: Each tag consists of a tag key and a tag value. The tag key is required, and the tag value is optional. Tag keys and tag values cannot start with aliyun. Tag keys and tag values are not case-sensitive. Each tag key can be up to 64 characters in length, and each tag value can be up to 128 characters in length. Up to 10 tags can be added to each instance. The tag keys of these tags must be unique. If you add two tags that have the same tag value to an instance, the new tag overwrites the existing tag. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddTagsToResou rce | The operation that you want to perform. Set the value to AddT agsT oResource. |
| RegionId | String | Yes | cn-hagnzhou | The region ID. You can call the DescribeRegions operation to query the most recent region list. |

| D | eveloper Guide·API r | eference |   |   | ApsaraDB for RD | S |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. Not e You can specify up to 30 instance IDs in a single request. Separate multiple instance IDs with commas (,). |
| Tags | String | No | {"key1":"value1"," key2":""} | The tags that you want to add. Each tag consists of a tag key and a tag value. You can specify up to five tags in a single request. Format: {"key1":"value1","key2":"value2"...}. Not e The tag key is required, and the tag value is optional. |
| Tag.1.key | String | No | key1 | The key of the first tag that you want to add. Each tag consists of a tag key and a tag value. You can specify up to five tags in a single request. The tag key is required, and the tag value is optional. |
| Tag.2.key | String | No | key2 | The key of the second tag that you want to add. Each tag consists of a tag key and a tag value. You can specify up to five tags in a single request. The tag key is required, and the tag value is optional. |
| Tag.3.key | String | No | key3 | The key of the third tag that you want to add. Each tag consists of a tag key and a tag value. You can specify up to five tags in a single request. The tag key is required, and the tag value is optional. |
| Tag.4.key | String | No | key4 | The key of the fourth tag that you want to add. Each tag consists of a tag key and a tag value. You can specify up to five tags in a single request. The tag key is required, and the tag value is optional. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Tag.5.key | String | No | key5 | The key of the fifth tag that you want to add. Each tag consists of a tag key and a tag value. You can specify up to five tags in a single request. The tag key is required, and the tag value is optional. |
| Tag.1.value | String | No | value1 | The value of the first tag that you want to add. Each tag consists of a tag key and a tag value. You can specify up to five tags in a single request. The tag key is required, and the tag value is optional. |
| Tag.2.value | String | No | value2 | The value of the second tag that you want to add. Each tag consists of a tag key and a tag value. You can specify up to five tags in a single request. The tag key is required, and the tag value is optional. |
| Tag.3.value | String | No | value3 | The value of the third tag that you want to add. Each tag consists of a tag key and a tag value. You can specify up to five tags in a single request. The tag key is required, and the tag value is optional. |
| Tag.4.value | String | No | value4 | The value of the fourth tag that you want to add. Each tag consists of a tag key and a tag value. You can specify up to five tags in a single request. The tag key is required, and the tag value is optional. |
| Tag.5.value | String | No | value5 | The value of the fifth tag that you want to add. Each tag consists of a tag key and a tag value. You can specify up to five tags in a single request. The tag key is required, and the tag value is optional. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| proxyId | String | No | API | The ID of the proxy mode. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 224DB9F7-3100- 4899-AB9C- C938BCCB43E7 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=AddTagsToResource &RegionId=cn-hagnzhou &DBInstanceId=rm-uf6wjk5xxxxxxx &Tags=%7B%22test%22%3A%221%22%7D &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AddTagsToResourceResponse>
      <requestId>224DB9F7-3100-4899-AB9C-C938BCCB43E7</requestId>
</AddTagsToResourceResponse>
```

`JSON` format `{`

```json
    "requestId": "224DB9F7-3100-4899-AB9C-C938BCCB43E7"
```

`}`

#### 2.17.3 ListTagResources

Queries the tags that are added to ApsaraDB RDS instances. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListTagResources | The operation that you want to perform. Set the value to List T agResources. |
| RegionId | String | Yes | cn-hangzhou | The region ID. You can call the DescribeRegions operation to query the most recent region list. |
| ResourceId.N | RepeatLi st | Yes | rm- uf6wjk5xxxxxxx | The ID of Instance N. You can query the tags that are added to N instances at a time. Valid values of N: 1 to 50. Not e You must specify at least one of the ResourceId.N and T ag.N.Key parameters. |
| ResourceType | String | Yes | INSTANCE | The type of the resource. Set the value to INST ANCE. |
| NextToken | String | No | 212db86sca4384 811e0b5e8707ec 21345 | The token required to obtain more results. This parameter is not required in the first query. If a query does not return all results, in the next query, you can specify the token returned from the previous query to obtain more results. |
| Tag.N.Key | String | No | testkey1 | The key of Tag N. You can query N tag keys at a time. Valid values of N: 1 to 20. This parameter cannot be an empty string. Not e You must specify at least one of the ResourceId.N and T ag.N.Key parameters. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Tag.N.Value | String | No | testvalue1 | The value of Tag N. You can specify N tag values at a time. Valid values of N: 1 to 20. This parameter can be an empty string. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| NextToken | String | 212db86sca4384811 e0b5e8707ec21345 | The token required to obtain more results. If this query does not return all results, in the next query, you can specify the token returned from this query to obtain more results. |
| RequestId | String | 47A514A1-4B77- 4E30-B4C5- 2A880650B3FD | The ID of the request. |
| TagResources | Array of TagResource |   | Details of the tags. |
| TagResource |   |   |   |
| ResourceId | String | rm-uf6wjk5xxxxxxx | The ID of the instance. |
| ResourceType | String | ALIYUN::RDS::INSTA NCE | The resource type. The value ALIYUN::RDS::INSTANCE indicates ApsaraDB RDS instances. |
| TagKey | String | testkey1 | The key of the tag. |
| TagValue | String | testvalue1 | The value of the tag. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=ListTagResources &RegionId=cn-hangzhou &ResourceType=INSTANCE &ResourceId.1=rm-uf6wjk5xxxxxxx &Tag.1.Key=testkey1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ListTagResourcesResponse>
  <TagResources>
        <TagResource>
              <ResourceType>ALIYUN::RDS::INSTANCE</ResourceType>
              <TagValue>testvalue1</TagValue>
              <ResourceId>rm-uf6wjk5xxxxxxx</ResourceId>
              <TagKey>testkey1</TagKey>
        </TagResource>
  </TagResources>
  <RequestId>47A514A1-4B77-4E30-B4C5-2A880650B3FD</RequestId>
</ListTagResourcesResponse>
```

`JSON` format `{`

```json
    "TagResources":{
        "TagResource":[
```

`{`

```json
                "ResourceType":"ALIYUN::RDS::INSTANCE",
                "TagValue":"testvalue1",
                "ResourceId":"rm-uf6wjk5xxxxxxx",
                "TagKey":"testkey1"
```

`}` `]` `},`

```json
    "RequestId":"47A514A1-4B77-4E30-B4C5-2A880650B3FD"
```

`}`

#### 2.17.4 UntagResources

Removes tags from ApsaraDB RDS instances. Up to 20 tags can be removed at a time. If a tag is removed from an instance and is not added to other instances, the tag is deleted. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UntagResources | The operation that you want to perform. Set the value to Unt agResources. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The region ID. You can call the DescribeRegions operation to query the most recent region list. |
| ResourceId.N | RepeatLi st | Yes | rm- uf6wjk5xxxxxxx | The ID of Instance N. You can remove tags from N instances at a time. Valid values of N: 1 to 50. |
| ResourceType | String | Yes | INSTANCE | The type of the resource. Set the value to INST ANCE. |
| TagKey.N | RepeatLi st | No | testkey1 | The key of Tag N. You can remove N tag keys at a time. Valid values of N: 1 to 20. This parameter cannot be an empty string. |
| All | Boolean | No | false | Specifies whether to remove all tags from the instance. Valid values: t rue f alse Default value: f alse. Not e This parameter is valid when T agKey.N is not specified. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 601B6F25-21E7- 4484-99D5- 3EF2625C0088 | The ID of the request. |

Examples Sample requests

```
http(s)://rds.example.com/?Action=UntagResources &RegionId=cn-hangzhou &ResourceType=INSTANCE &ResourceId.1=rm-uf6wjk5xxxxxxx &TagKey.1=testkey1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UntagResourcesResponse>
        <RequestId>601B6F25-21E7-4484-99D5-3EF2625C0088</RequestId>
</UntagResourcesResponse>
```

`JSON` format `{`

```json
    "RequestId":"601B6F25-21E7-4484-99D5-3EF2625C0088"
```

`}`

### 2.18 RAM authorization

Use RAM for RDS resource authorization All RDS instances created through an Apsara Stack tenant account are resources owned by that account. By default, you have full operation permissions on the resources under your account. Resource Access Management (RAM) allows you to grant RAM users the access and management permissions on RDS resources owned by an Apsara Stack tenant account. If you do not need to use RAM, ignore this topic. Resource types in RAM The only type of RDS resources that can be authorized through RAM is dbinstance. The following table lists the resource description method when the resources are authorized through RAM.

| Resource | Resource description in authorization policy |
|---|---|
| Instance | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid acs:rds:$regionid:$accountid:dbinstance/ acs:rds:::dbinstance/ |

The $regionid field must be the ID of a region or an asterisk (*). The $instanceid field must be the ID of an instance or an asterisk (*). Similarly, $account-id is the numerical ID of your Apsara Stack tenant account, which can be replaced by an asterisk (*). Authorization operations in RAM In RAM, the following operations can be authorized to an RDS resource.

| Operation 1 | Operation 2 |
|---|---|
| CreateDBInstance | ModifyDBInstanceSpec |
| DeleteDBInstance | CreateReadonlyDBInstance |

| eveloper Guide·API reference | ApsaraDB for RD |
|---|---|

| Operation 1 | Operation 2 |
|---|---|
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

All operations except DescribeRegions and DescribeParameterTemplates can be authorized. RAM authentication rules of API operations When you call API operations to access resources as a RAM user, the RDS backend checks whether the RAM user is granted the required permissions by querying RAM. The permissions to be checked are determined by the resources used by the API operation. The following table lists the authentication rules for each API operation.

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
| DescribeOptimizeAdviceOnMissIndex | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeParameters | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CreatePrepaidDBInstanceForChannel | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifyPrepaidDBInstanceSpec | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CreatePostpaidDBInstanceForChannel | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |

| eveloper Guide·API reference | ApsaraDB for RD |
|---|---|

| Operation | Authentication rule |
|---|---|
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
| ModifyeParameter | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |

### 2.19 Appendix

#### 2.19.1 Error codes on the client

##### 2.19.1.1 Common errors

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
| Forbidden.RiskControl | This operation is forbidden by Aliyun Risk Control system. | 403 |
| InsufficientBalance | Your account does not have enough balance. | 400 |
| Forbidden.Authentication | This operation is forbidden by Aliyun Realname Authentication system. | 403 |
| Invalid<parameter name>.ValueNotSupporte d | The specified parameter “parameter name” is not valid. | 400 |

| Error code | Error message | HTTP status code |
|---|---|---|
| Invalid<parameter name>.Malformed | The specified parameter "parameter name n" is not valid. | 400 |
| InvalidParameter | The specified parameter " parameter name n " is not valid. | 400 |

##### 2.19.1.2 Specific errors

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
| MissingParameter | The input parameters "DBInstanceClass" and "DBInstanceStorage" all blank or no change. | 400 |
| OperationDenied.DBInstanceType | The operation is not permitted due to type of instance. | 400 |
| OperationDenied.DBInstanceStorageR educe | The operation is not permitted due to reduce storage. | 403 |
| OperationDenied.DBInstanceStatus | The operation is not permitted due to instance status. | 403 |

| A | psaraDB for RDS | Developer Guid | e·API referenc | e |
|---|---|---|---|---|

| Error code | Error message | HTTP status code |
|---|---|---|
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
| FTPServiceUnavailable | The request has failed due to a temporary failure of the FTP server. | 403 |
| QuotaExceeded.Upload | The quota of file exceeds. | 403 |
| InvalidFileName.NotCompleted | The specified "FileName" is not completed. | 404 |
| InvalidFileName.NotAvailable | The specified "FileName" is not Available. | 404 |
| QuotaExceeded.FileSize | The quota of file size exceeds. | 403 |
| QuotaExceeded.DBInstanceStorage | The quota of instance storage exceeds. | 403 |

| D | eveloper Guide·API reference | A | psaraDB for RD | S |
|---|---|---|---|---|

| Error code | Error message | HTTP status code |
|---|---|---|
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
| OperationDenied.NoDatabase | The operation is not permitted due to no database. | 403 |
| InvalidStartTimeAndEndTime.Malform ed | The end time must be greater than the start time | 400 |
| OperationDenied.BackupJobExists | The operation is not permitted due to backup job exist. | 403 |
| InvalidBackupId.NotFound | The BackupId provided does not exist in our records. | 404 |

| psaraDB for RDS | Developer Guid | e·API referenc |
|---|---|---|

| Error code | Error message | HTTP status code |
|---|---|---|
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
| InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist in our records. | 400 |
| InvalidDBInstanceId.QuotaExceeded | The quota of instance id exceeds. | 400 |
| InvalidDBInstanceNetType.NotFound | The Specified DB instance net type is not found. | 404 |
| InvalidDBinstanceNetType.ValueNotSu pport | The specified parameter "DBinstanceNetType" is not valid. | 400 |

| Error code | Error message | HTTP status code |
|---|---|---|
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
| OperationDenied.LockMode | The operation is not permitted due to lock of instance. | 403 |
| OperationDenied.Switch | Specified instance cannot be switched. | 400 |
| OperationDenied.Switch | Specified instance cannot be switched to VPC. | 403 |
| OperationDenied.SwitchToVPC | Specified instance cannot be switched to VPC. | 403 |
| OperationDenied | The resource is out of usage. | 403 |

| A | psaraDB for RDS | Developer Guid | e·API referenc | e |
|---|---|---|---|---|

| Error code | Error message | HTTP status code |
|---|---|---|
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
| bpcIzNoNotEqualsRdsMultIzNo | Specified vpc IzNo not equal rds IzNo. | 400 |

#### 2.19.2 Error codes on the server

| Error code | Error message | HTTP status code |
|---|---|---|
| ServiceUnavailable | The request has failed due to a temporary failure of the server. | 503 |

| D | eveloper Guide·API re | ference Ap | saraDB for RD | S |
|---|---|---|---|---|

| Error code | Error message | HTTP status code |
|---|---|---|
| InternalError | The request processing has failed due to some unknown error, exception or failure. | 500 |

#### 2.19.3 Instance states

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

#### 2.19.4 Performance parameters

ApsaraDB RDS for MySQL

| API parameter | Description |
|---|---|
| MySQL NetworkTraffic _ | The average inbound traffic to a MySQL instance per second and average outbound traffic from a MySQL instance per second. Unit: KB. |

| A | psaraDB for RDS | Developer Guide·API referenc | e |
|---|---|---|---|

| API parameter | Description |
|---|---|
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
| MySQL MemCpuUsage _ | The CPU utilization and memory usage of a MySQL instance within the entire operating system. |
| MySQL IOPS _ | The IOPS of a MySQL instance. |
| MySQL DetailedSpaceUsage _ | The disk space occupied by a MySQL instance, including ins size (total _ space), data size (data space), log size (log space), tmp size (temporary _ _ _ space), and other size (system space). _ |

| eveloper Guide·API reference | ApsaraDB for RD |
|---|---|
| API parameter | Description |
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

#### 2.19.5 Forbidden keywords

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

#### 2.19.6 Instance types

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
| Document | Version: 202 | 20915 |   |   |   |   | 39 |

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
|   |   | 20915 |   |   |   |   |   |   |

| RDS edition | Postgre SQL version | Instance | Instance type | CPU and memory | Maximu m connecti ons | Maximu m IOPS | Storage capacity | Zone- disaster recovery deploy ment |
|---|---|---|---|---|---|---|---|---|
|   |   | family |   |   |   |   |   |   |
|   |   | Dedicat ed host | rds.pg.s t.h43 | 60 cores, 470 GB | 4,000 | 50,000 |   |   |
