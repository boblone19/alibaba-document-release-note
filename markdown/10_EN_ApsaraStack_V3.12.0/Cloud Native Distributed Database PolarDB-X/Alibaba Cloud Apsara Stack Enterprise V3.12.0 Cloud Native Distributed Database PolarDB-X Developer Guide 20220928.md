---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Cloud Native Distributed Database PolarDB-X Developer Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 229
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Cloud Native Distributed Database PolarDB-X Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E6%95%B0%E6%8D%AE%E5%BA%93/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20Cloud%20Native%20Distributed%20Database%20PolarDB-X%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 Cloud Native Distributed Database PolarDB-X Developer Guide 20220928

## Table of Contents

- 1 Developer Guide (1.0)
  - 1.1 API reference
    - 1.1.1 List of operations by function
    - 1.1.2 Make API requests
    - 1.1.3 Common parameters
    - 1.1.4 Request signature
    - 1.1.5 Database management
      - 1.1.5.1 ChangeAccountPassword
      - 1.1.5.2 CheckDrdsDbName
      - 1.1.5.3 CheckExpandStatus
      - 1.1.5.4 CheckSqlAuditEnableStatus
      - 1.1.5.5 CreateDrdsDB
      - 1.1.5.6 CreateShardTask
      - 1.1.5.7 DatalinkReplicationPrecheck
      - 1.1.5.8 DeleteShardTasks
      - 1.1.5.9 DescribeBackMenu
      - 1.1.5.10 DescribeBackupDbs
      - 1.1.5.11 DescribeBackupTimes
      - 1.1.5.12 DescribeBroadcastTables
      - 1.1.5.13 DescribeDbInstanceDbs
      - 1.1.5.14 DescribeDbInstances
      - 1.1.5.15 DescribeDrdsDB
      - 1.1.5.16 DescribeDrdsDbInstance
      - 1.1.5.17 DescribeDrdsDbInstances
      - 1.1.5.18 DescribeDrdsDbRdsNameList
      - 1.1.5.19 DescribeDrdsDbRdsRelationInfo
      - 1.1.5.20 DescribeDrdsDbTasks
      - 1.1.5.21 DescribeDrdsInstanceDbMonitor
      - 1.1.5.22 DescribeDrdsShardingDbs
      - 1.1.5.23 DescribeDrdsSlowSqls
      - 1.1.5.24 DescribeDrdsSqlAuditStatus
      - 1.1.5.25 DescribeExpandLogicTableInfoList
      - 1.1.5.26 DescribeGlobalBroadcastType
      - 1.1.5.27 DescribeHotDbList
      - 1.1.5.28 DescribeInstDbLogInfo
      - 1.1.5.29 DescribeRDSPerformance
      - 1.1.5.30 DescribeRdsPerformanceSummary
      - 1.1.5.31 DescribeRdsSuperAccountInstances
      - 1.1.5.32 DescribeRecycleBinStatus
      - 1.1.5.33 DescribeRecycleBinTables
      - 1.1.5.34 DescribeShardTaskInfo
      - 1.1.5.35 DescribeShardTaskList
      - 1.1.5.36 DescribeSqlFlashbakTask
      - 1.1.5.37 DescribeTable
      - 1.1.5.38 DescribeTableListByType
      - 1.1.5.39 DescribeTables
      - 1.1.5.40 DisableSqlAudit
      - 1.1.5.41 ModifyAccountPrivilege
      - 1.1.5.42 ModifyDrdsIpWhiteList
      - 1.1.5.43 ModifyRdsReadWeight
      - 1.1.5.44 DescribeDbInstances
      - 1.1.5.45 ReleaseHiStoreInstance
      - 1.1.5.46 RemoveBackupsSet
      - 1.1.5.47 RemoveDrdsDbFailedRecord
      - 1.1.5.48 RemoveRecycleBinTable
      - 1.1.5.49 ResetDrdsToRdsConnections
      - 1.1.5.50 SetupBroadcastTables
      - 1.1.5.51 SetupRecycleBinStatus
      - 1.1.5.52 SetupTable
      - 1.1.5.53 StartRestore
      - 1.1.5.54 SubmitCleanTask
      - 1.1.5.55 SubmitSmoothExpandPreCheck
      - 1.1.5.56 SubmitSmoothExpandPreCheckTask
      - 1.1.5.57 SubmitSmoothExpandTask
      - 1.1.5.58 SubmitSwitchTask
      - 1.1.5.59 ValidateShardTask
      - 1.1.5.60 RemoveDrdsDb
      - 1.1.5.61 RefreshDrdsAtomUrl
    - 1.1.6 Instance management
      - 1.1.6.1 CreateInstanceAccount
      - 1.1.6.2 DescribeDrdsDBs
      - 1.1.6.3 DescribeDrdsInstance
      - 1.1.6.4 DescribeDrdsInstanceLevelTasks
      - 1.1.6.5 DescribeDrdsInstanceMonitor
      - 1.1.6.6 DescribeDrdsInstances
      - 1.1.6.7 DescribeDrdsInstanceVersion
      - 1.1.6.8 DescribeDrdsParams
      - 1.1.6.9 DescribeDrdsTasks
      - 1.1.6.10 DescribeHiStoreInstanceInfo
      - 1.1.6.11 DescribeInstanceAccounts
      - 1.1.6.12 DescribeInstanceMenuSwitch
      - 1.1.6.13 DescribeInstDbSlsInfo
      - 1.1.6.14 DescribePreCheckResult
      - 1.1.6.15 DescribeStorageInstanceSubDbInfo
      - 1.1.6.16 EnableSqlAudit
      - 1.1.6.17 EnableSqlFlashbackMatchSwitch
      - 1.1.6.18 FlashbackRecycleBinTable
      - 1.1.6.19 ModifyAccountDescription
      - 1.1.6.20 ModifyDrdsInstanceDescription
      - 1.1.6.21 RemoveDrdsInstance
      - 1.1.6.22 RemoveInstanceAccount
      - 1.1.6.23 RestartDrdsInstance
      - 1.1.6.24 RollbackInstanceVersion
      - 1.1.6.25 SetBackupPolicy
      - 1.1.6.26 SetupDrdsParams
      - 1.1.6.27 SubmitRollbackTask
      - 1.1.6.28 SubmitSqlFlashbackTask
      - 1.1.6.29 SwitchGlobalBroadcastType
      - 1.1.6.30 UpgradeInstanceVersion
  - 1.2 Call SDKs for cloud services by using ASAPI
    - 1.2.1 Overview
    - 1.2.2 Log on to the API Tool console
    - 1.2.3 View the information about API operations
    - 1.2.4 Obtain the endpoint of ASAPI
    - 1.2.5 Obtain the core package for ASAPI
    - 1.2.6 Obtain an AccessKey pair
    - 1.2.7 Query the region ID
    - 1.2.8 Call PolarDB-X SDK for Java
    - 1.2.9 Call PolarDB-X SDK for Node.js
    - 1.2.10. (Optional) Use POP SDK to call ASAPI API operations

## 1 Developer Guide (1.0)

### 1.1 API reference

#### 1.1.1 List of operations by function

The following tables list API operations available for use in Cloud Native Distributed Database PolarDB- X. Database management

| API | Description |
|---|---|
| ChangeAccountPassword | Resets the password of a PolarDB-X 1.0 database. |
| CheckDrdsDbName | Checks whether the name of a PolarDB-X 1.0 database is valid. |
| DescribeRdsPerformanceSummary | Queries the performance metrics of ApsaraDB RDS for MySQL instances for a PolarDB-X instance, including the CPU utilization, input/output operations per second (IOPS), and active sessions. |
| DescribeRecycleBinStatus | Queries the status of the table recycle bin for a PolarDB-X database. |
| DescribeRecycleBinTables | Queries the tables that can be recycled for a PolarDB-X database. |
| DescribeRdsSuperAccountInstances | Queries the privileged accounts of ApsaraDB RDS for MySQL instances for a PolarDB-X instance. |
| DescribeDrdsSlowSqls | Queries slow SQL statements of a PolarDB-X 1.0 database. |
| DescribeDrdsDbInstance | Queries the details about an ApsaraDB RDS for MySQL instance of a PolarDB-X 1.0 database. |
| DescribeDrdsDbInstances | Queries the ApsaraDB RDS for MySQL instances of a PolarDB-X 1.0 database. |
| DescribeDrdsDbRdsNameList | Queries the storage instances of a PolarDB-X 1.0 database. |
| DescribeDrdsDbRdsRelationInfo | Queries the structure information of storage instances for a PolarDB-X 1.0 database. |
| DescribeDrdsDbTasks | Queries incomplete tasks for a PolarDB-X 1.0 database. |
| DescribeDrdsInstanceDbMonitor | Queries the performance monitoring data of a PolarDB-X 1.0 database. |

| eveloper Guide·Developer Guide ( .0) | Cloud Native Distributed Database PolarDB- |
|---|---|

| API | Description |
|---|---|
| SubmitCleanTask | Submits a cleanup task for smooth scale-out of a PolarDB-X database. |
| SubmitSmoothExpandPreCheckTask | Submits a precheck task for smooth scale-out of a PolarDB-X database. |
| ValidateShardTask | Verifies whether a partitioning task of a PolarDB-X database is valid. |
| SubmitSmoothExpandPreCheck | Submits a precheck task for smooth scale-out of a PolarDB-X database. |
| StartRestore | Starts a backup-based recovery task for a PolarDB-X instance. |
| RefreshDrdsAtomUrl | Refreshes the connection between the PolarDB-X 1.0 instance and the ApsaraDB RDS for MySQL instance whose network type is changed to ensure that the connection is smooth. |
| ModifyRdsReadWeight | Modifies the read weights of ApsaraDB RDS for MySQL instances. |
| RemoveDrdsDbFailedRecord | Removes database creation failure records from a PolarDB-X instance. |
| RemoveDrdsDb | Removes a database from a PolarDB-X 1.0 instance. |
| RemoveBackupsSet | Removes a backup set from a PolarDB-X instance. |
| ReleaseHiStoreInstance | Releases a columnar storage instance, namely, a HiStore instance of a PolarDB-X instance. |
| DescribeBroadcastTables | Queries the broadcast tables in a PolarDB-X database. |
| RemoveRecycleBinTable | Removes tables from the recycle bin for a PolarDB-X database. |
| DescribeBackMenu | Queries whether a PolarDB-X instance supports backup and recovery. |
| DescribeDrdsSqlAuditStatus | Queries the details about SQL audit for a PolarDB-X 1.0 instance. |
| DescribeTables | Queries the details about tables in a PolarDB-X database. |
| DescribeBackupTimes | Queries the point in time to which a PolarDB-X instance can be restored. |

| API | Description |
|---|---|
| DescribeGlobalBroadcastType | Queries whether the table in a PolarDB-X database is a broadcast table. |
| DescribeExpandLogicTableInfoList | Queries the shard key of a PolarDB-X database. |
| DescribeTableListByType | Queries type-specific tables of a PolarDB-X database. |
| DisableSqlAudit | Disables SQL audit of a PolarDB-X database. |
| DescribeShardTaskList | Queries the partitioning tasks of a PolarDB-X database. |
| DescribeTable | Queries the table schema of a PolarDB-X database. |
| DescribeInstDbLogInfo | Queries the time range of historical SQL data that can be imported to a PolarDB-X database. |
| ResetDrdsToRdsConnections | Resets the number of connections from the PolarDB-X 1.0 instance to ApsaraDB RDS for MySQL instances. |
| DatalinkReplicationPrecheck | Prechecks a partitioning task of a PolarDB-X database. |
| DescribeRDSPerformance | Queries the performance data of ApsaraDB RDS for MySQL instances for a PolarDB-X instance. |
| CreateShardTask | Creates a partitioning task for a PolarDB-X database. |
| DescribeShardTaskInfo | Queries details about a partitioning task of a PolarDB-X database. |
| DescribeBackupDbs | Queries the databases that can be restored for a PolarDB-X instance. |
| DeleteShardTasks | Deletes partitioning tasks from a PolarDB-X database. |
| ModifyDrdsIpWhiteList | Modifies the IP address whitelist of a PolarDB-X database. |
| PutStartBackup | Submits a data backup task for a PolarDB-X instance. |
| DescribeSqlFlashbakTask | Queries the flashback tasks of a PolarDB-X database. |
| CheckExpandStatus | Verifies whether scale-out operations such as smooth scale-out can be performed on a PolarDB-X 1.0 database. |

| D 1 | eveloper Guide·Developer Guide ( .0) | Cloud Native Distributed Database PolarDB- | X |
|---|---|---|---|

| API | Description |
|---|---|
| CheckSqlAuditEnableStatus | Verifies whether SQL audit is enabled for a PolarDB- X 1.0 logical database. |
| SetupBroadcastTables | Configures a broadcast table for a PolarDB-X database. |
| SetupRecycleBinStatus | Enables the table recycle bin for a PolarDB-X database. |
| SetupTable | Enables full table scan for a PolarDB-X database. |
| ModifyAccountPrivilege | Modifies account permissions for a PolarDB-X instance. |
| DescribeDrdsShardingDbs | Queries details about a horizontally partitioned PolarDB-X 1.0 database. |
| CreateDrdsDB | Creates a PolarDB-X 1.0 database. |
| DescribeDbInstances | Queries the storage instances of a PolarDB-X instance. |
| DescribeDrdsDB | Queries the details about a database on a PolarDB-X instance. |
| DescribeDbInstanceDbs | Queries the databases on a storage instance of a PolarDB-X instance. |
| SubmitSmoothExpandTask | Submits a smooth scale-out task for a PolarDB-X database. |
| SubmitSwitchTask | Submits a switchover task for smooth scale-out of a PolarDB-X database. |

Instance management

| API | Description |
|---|---|
| DescribeDrdsDBs | Queries the details about databases on a PolarDB-X 1.0 instance. |
| DescribeDrdsInstance | Queries the details about a PolarDB-X 1.0 instance. |
| DescribeDrdsInstanceLevelTasks | Queries incomplete tasks for a PolarDB-X 1.0 instance. |
| DescribeDrdsInstanceMonitor | Queries the monitoring data of a PolarDB-X 1.0 instance. |
| DescribeDrdsInstances | Queries PolarDB-X 1.0 instances that meet specific criteria in a region. |

| C P | loud Native Distributed Database olarDB-X | Developer Guide·Developer Guide 1.0 | ( ) |
|---|---|---|---|

| API | Description |
|---|---|
| DescribeDrdsInstanceVersion | Queries the versions of a PolarDB-X 1.0 instance. |
| DescribeDrdsParams | Queries the parameters of a PolarDB-X 1.0 instance or database. |
| RollbackInstanceVersion | Rolls back the version of a PolarDB-X 1.0 instance. |
| UpgradeInstanceVersion | Upgrades the version of the PolarDB-X 1.0 instance. |
| SubmitRollbackTask | Submits a smooth scale-out rollback task for a PolarDB-X database. |
| SwitchGlobalBroadcastType | Switches the broadcast table in a PolarDB-X database from the multi-write mode to the asynchronous link mode. |
| SubmitSqlFlashbackTask | Submits an SQL flashback task for a PolarDB-X instance. |
| RemoveDrdsInstance | Releases a PolarDB-X 1.0 instance. |
| DescribeDrdsTasks | Queries the change tasks of a PolarDB-X instance. |
| RestartDrdsInstance | Restarts a PolarDB-X instance. |
| DescribePreCheckResult | Queries precheck results of a PolarDB-X instance. |
| DescribeHiStoreInstanceInfo | Queries the details about a HiStore instance of a PolarDB-X instance. |
| DescribeStorageInstanceSubDbInfo | Queries the details about a storage instance of a PolarDB-X database. |
| RemoveInstanceAccount | Deletes the instance management account of a PolarDB-X instance. |
| DescribeInstanceMenuSwitch | Queries the switch configuration of a PolarDB-X instance. |
| DescribeInstanceAccounts | Queries the account information of a PolarDB-X instance. |
| DescribeInstDbSlsInfo | Queries the names of the Log Service project and Logstore used by SQL audit. |
| SetBackupPolicy | Configures a backup policy for a PolarDB-X instance. |
| EnableSqlAudit | Enables SQL audit for a PolarDB-X database. |

| API | Description |
|---|---|
| EnableSqlFlashbackMatchSwitch | Enables SQL flashback matching. After it is enabled, the query information is added to the ApsaraDB RDS for MySQL binary logs that are used by the PolarDB- X 1.0 database to precisely restore data. |
| SetupDrdsParams | Configures parameters for a PolarDB-X 1.0 instance or database. |
| FlashbackRecycleBinTable | Restores a logical table in the recycle bin. |
| ModifyAccountDescription | Modifies the account description of a PolarDB-X instance. |
| ModifyDrdsInstanceDescription | Modifies the description of a PolarDB-X instance. |
| CreateInstanceAccount | Creates an account for a PolarDB-X 1.0 instance. |

#### 1.1.2 Make API requests

To send a Cloud Native Distributed Database PolarDB-X API request, you must send an HTTP GET request to the Cloud Native Distributed Database PolarDB-X endpoint. You must add the request parameters that correspond to the API operation being called. After you call the API operation, the system returns a response. The request and response are encoded in UTF-8. Request syntax Cloud Native Distributed Database PolarDB-X API operations use the RPC protocol. You can call Cloud Native Distributed Database PolarDB-X API operations by sending HTTP GET requests. The request syntax is as follows:

```
http://Endpoint/?Action=xx&Parameters
```

Endpoint: the endpoint of Cloud Native Distributed Database PolarDB-X. For more information about how to obtain the endpoint, see Obtain the endpoint of ASAPI. Action: the name of the operation being performed. For example, to query tables in a Cloud Native Distributed Database PolarDB-X database, you must set the Action parameter to DescribeTables. Version: the version of the API. For example, the version of the Cloud Native Distributed Database PolarDB-X API is `2019-01-23` . Parameters: the request parameters for the operation. Separate multiple parameters with ampersands (&). Request parameters include both common parameters and operation-specific parameters. Common parameters are used for all PolarDB-X API calls regardless of the operation. For more information, see Common parameters. The following example demonstrates how to call the DescribeTables operation in Cloud Native Distributed Database PolarDB-X:

```
https://drds.aliyuncs.com/?Action=DescribeTables &Format=xml &Version=2019-01-23 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15xxxxxxxxx396 &SignatureVersion=1.0 &AccessKeyId=key-test &TimeStamp=2012-06-01T12:00:00Z ...
```

#### 1.1.3 Common parameters

Common request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Format | String | No | The format in which the response is returned. Valid values: JSON (default) and XML. |
| Version | String | Yes | The version number of the API, in the format of YYYY-MM-DD. Valid value: 2019-01-23. |
| AccessKeyId | String | Yes | The AccessKey ID provided to you by Apsara Stack. |
| Signature | String | Yes | The signature string of the current request. |
| SignatureMethod | String | Yes | The encryption method of the signature string. Set the value to HMAC- SHA1. |
| Timestamp | String | Yes | The time at which the quest is signed. Specify the UTC time in the ISO 8601 standard in the YYYY-MM- DDThh:mm:ssZ format. For example, 20:00:00 on January 10, 2013 (UTC+8) is written as 2013-01-10T12:00:00Z. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Set the value to 1.0. |
| SignatureNonce | String | Yes | A unique and random number used to prevent replay attacks. You must use different numbers for different requests. |
| ResourceOwnerAccount | String | No | The owner account (the logon username) of the resource you want to access by using this API request. |

Common response parameters Responses can be returned in either the JSON or XML format. You can specify the response format in the request. The default response format is XML. Each time you send a request to call an API operation, the system returns a unique identifier RequestId, regardless of whether the request is successful or not. An HTTP status code of `2xx` indicates that the call succeeds. An HTTP status code of `4xx` or `5xx` indicates that the call failed. The following are sample responses:

```json
<? xml version="1.0" encoding="utf-8"? >
    <!—Result root node-->
    <API operation name+response>
        <!—Returned request tag-->
        <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
        <!—Response data-->
    </API name+Response>
    "RequestId":"4C467B38-3910-447D-87BC-AC049166F216",
    /*Response data*/
```

#### 1.1.4 Request signature

This topic describes how to sign the request when you send an API request. AccessKey ID and AccessKey secret PolarDB-X 1.0 verifies the identity of each API request sender. Therefore, whether you send an HTTP request or an HTTPS request, the request must contain the signature generated by an AccessKey ID and an AccessKey secret. An AccessKey ID and an AccessKey secret are issued to visitors by Alibaba Cloud. Visitors can apply for and manage an AccessKey pair on the Alibaba Cloud official website. The AccessKey ID is used to verify the identity of the visitor. The AccessKey secret is used to encrypt the signature string on the client and verify the signature string on the server. You must keep your AccessKey secret strictly confidential. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair. Signature method When you send an API request, take the following steps to sign the request:
1. Create a canonicalized query string by arranging the request parameters.
i. Arrange the request parameters (including all common and operation-specific parameters except Signature) in alphabetical order. Not ice When you use the GET method to submit requests, these parameters constitute the parameter field of the request URI. They come after the question mark (?) in the request URI and are connected by ampersands (&). ii. Encode the name and value of each request parameter. The parameter names and values must be URL encoded by using UTF-8. The URL encoding rules are described as follows: Uppercase letters, lowercase letters, digits, and some special characters such as hyphens (-), underscores (_), periods (.), and tildes (~) do not need to be encoded. Other characters must be percent encoded in %XY format. XY represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks (") are encoded as %22. Extended UTF-8 characters are encoded in %XY%ZA… format. Spaces must be encoded as %20. Do not encode spaces as plus signs (+). Not e Libraries that support URL encoding, such as the java.net.URLEncoder class in Java, encode strings in compliance with the requirements of the "application/x-wwwform-urlencoded" Multipurpose Internet Mail Extensions (MIME) type. If you use this encoding method, you can replace plus signs (+) with %20, asterisks (*) with %2A, and %7E with tildes (~) in the encoded string to obtain the required string. iii. Connect the encoded parameter names and values with equal signs (=). iv. Sort the parameter name and value pairs connected by equal signs (=) in alphabetical order and connect the pairs with ampersands (&).
2. Use the created canonicalized query string to construct a string-to-sign based on the following
rules:

```
StringToSign=
 HTTPMethod + "&" +
 percentEncode("/") + "&" +
 percentEncode(CanonicalizedQueryString)
```

HTTPMethod specifies the HTTP method that is used to submit a request, such as GET. percentEncode("/") specifies the encoded value (%2F) for the forward slash (/) based on the URL encoding rules described in step 1.b. percentEncode(CanonicalizedQueryString) is the string as a result of encoding the canonicalized query string created in step 1 based on the URL encoding rules described in step 1.b.
3. Follow RFC 2104 to calculate the HMAC value of the string-to-sign by using the AccessKey secret
as the key. Not ice The key used for calculating the signature is your AccessKey secret followed by an ampersand (&). The SHA1 algorithm is used for the calculation.
4. Encode the HMAC value in Base64 to obtain the signature string.
5. Add the signature string to the request as the Signature parameter.
Not ice When the signature string is submitted to the PolarDB-X 1.0 server as the final request parameter value, the string must be URL encoded like other parameters based on the rules defined in RFC 3986. DescribeDrdsInstances is used in this example. The canonicalized query string is as follows:

```
AccessKeyId=testid&Action=DescribeDrdsInstances&Format=XML&RegionId=cn-hangzhou&SignatureMe thod=HMAC-SHA1&SignatureNonce=ae5bdbeb-9b44-40a1-8bb4-b40784bff686&SignatureVersion=1.0&Tim estamp=2016-01-20T14%3A26%3A15Z&Version=2015-04-13
```

Encode the canonicalized query string in UTF-8 to create the following StringToSign:

```
GET&%2F&AccessKeyId%3Dtestid&Action%3DDescribeDrdsInstances&Format%3DXML&RegionId%3Dcn-hang zhou&SignatureMethod%3DHMAC-SHA1&SignatureNonce%3Dae5bdbeb-9b44-40a1-8bb4-b40784bff686&Sign atureVersion%3D1.0&Timestamp%3D2016-01-20T14%253A26%253A15Z&Version%3D2015-04-13
```

Assume that the AccessKey ID is testid, the AccessKey secret is testsecret, and the key used for HMAC calculation is testsecret&. The calculated signature value is as follows:

```
h/ka/jNO+WZv8Tqgo4a75sp6eTs=
```

The signed request URL that includes the Signature parameter is as follows:

```
http://drds.example.com/?AccessKeyId=testid&Action=DescribeDrdsInstances&Format=XML&RegionI d=cn-hangzhou&SignatureMethod=HMAC-SHA1&SignatureNonce=ae5bdbeb-9b44-40a1-8bb4-b40784bff686 &SignatureVersion=1.0&Timestamp=2016-01-20T14%3A26%3A15Z&Version=2015-04-13&Signature=h%xxx xxxxxxxxxxxxxxxxxxxxxxxxxxx
```

An example of calling the DescribeDrdsInstances operation in Java is as follows:

```
public static void drdsOpenAPI() throws NoSuchAlgorithmException, InvalidKeyException, IOEx ception {
        //AccessKey ID and AccessKey secret
        String accessKey = "testid";
StringaccessSecret="testsecret";
```

```java
        String accessSecret  testsecret;
        //Common parameters
        Map<String, String> parameters = new TreeMap<String, String>();
        parameters.put("Format", "JSON");
        parameters.put("Action", "DescribeDrdsInstances");//Call the DescribeDrdsInstances
operation
        parameters.put("Version", "2015-04-13");
        parameters.put("AccessKeyId", accessKey);
        parameters.put("SignatureMethod", "HMAC-SHA1");
        parameters.put("Timestamp", getISO8601Time());
        parameters.put("SignatureVersion", "1.0");
        parameters.put("SignatureNonce", UUID.randomUUID().toString());
        parameters.put("RegionId", "cn-hangzhou");
        StringBuilder paramStr = new StringBuilder();
        //Concatenate request parameters
        for(Map.Entry<String, String> entry : parameters.entrySet()) {
          paramStr.append(percentEncode(entry.getKey())).append("=").append(percentEncode(e
ntry.getValue())).append("&");
        paramStr.deleteCharAt(paramStr.length()-1);
        //Calculate the signature
        StringBuilder stringToSign = new StringBuilder();
            stringToSign.append("GET").append("&").append(percentEncode("/"))
                  .append("&").append(percentEncode(paramStr.toString()));
            Mac mac = Mac.getInstance("HmacSHA1");
        mac.init(new SecretKeySpec((accessSecret + "&").getBytes("UTF-8"),"HmacSHA1"));
        byte[] signData = mac.doFinal(stringToSign.toString().getBytes("UTF-8"));
        String signStr = Base64Helper.encode(signData);
        //Concatenate the request URL
        String requestUrl = "http://drds.example.com/?" + paramStr.toString() +
            "&Signature=" +  percentEncode(signStr);
        //Prepare to send HTTP requests
        URL url = new URL(requestUrl);
        HttpURLConnection httpConn = (HttpURLConnection)url.openConnection();
        httpConn.setRequestMethod("GET");
        httpConn.setDoOutput(true);
        httpConn.setDoInput(true);
        httpConn.setUseCaches(false);
        httpConn.connect();
        InputStream content = httpConn.getInputStream();
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        byte[] buff = new byte[1024];
        while(true) {
           final int read = content.read(buff);
           if(read == -1) break;
           outputStream.write(buff,0,read);
        System.out.println(new String(outputStream.toByteArray()));;
  public static String percentEncode(String value) throws UnsupportedEncodingException{
        return value ! = null ? URLEncoder.encode(value, "UTF-8").replace("+", "%20")
                .replace("*", "%2A").replace("%7E", "~") : null;
  static String getISO8601Time() {
        SimpleDateFormat df = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss'Z'");
```

```
        df.setTimeZone(new SimpleTimeZone(0, "GMT"));
        return df.format(new Date());
```

#### 1.1.5 Database management

##### 1.1.5.1 ChangeAccountPassword

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

```json
http(s)://[Endpoint]/? Action=ChangeAccountPassword &AccountName=test &DrdsInstanceId=drdsxxxxxxxxxx &Password=Test123 <ChangeAccountPasswordResponse>
      <RequestId>DSSDF-SEWE-23ERW</RequestId>
</ChangeAccountPasswordResponse>
    "RequestId":"DSSDF-SEWE-23ERW",
    "Success":true
```

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | ActionUnauthorized | The specified action is not available for you | The error message returned because you are not authorized to perform this action. Perform RAM authorization first. |

##### 1.1.5.2 CheckDrdsDbName

Checks whether the name of a PolarDB-X 1.0 database is valid.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CheckDrdsDbNam e | The operation that you want to perform. Set the value to CheckDrdsDbNam e. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DbName | String | Yes | testdb | The name of the PolarDB-X 1.0 database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DSSDF-SEWE-23ERW | The ID of the request. |
| Result | Boolean | true | Indicates whether the name of the PolarDB-X database is valid. Valid values: true: valid false: invalid |
| Success | Boolean | true | Indicates whether the request was successful. |

```json
http(s)://[Endpoint]/? Action=CheckDrdsDbName &DbName=testdb &DrdsInstanceId=drdsxxxxxxxxxxx <CheckDrdsDbNameResponse>
      <Result>true</Result>
      <RequestId>CF38538C-68BD-4278-B58F-EDE96FA8A5CE</RequestId>
</CheckDrdsDbNameResponse>
    "Result":true,
    "RequestId":"CF38538C-68BD-4278-B58F-EDE96FA8A5CE",
    "Success":true
```

##### 1.1.5.3 CheckExpandStatus

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
| RequestId | String | drds sample request i _ _ _ d | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```json
http(s)://[Endpoint]/? Action=CheckExpandStatus &DbName=testdb &DrdsInstanceId=drdsxxxxxxxxxxx <CheckExpandStatus>
      <Data>
            <IsActive>true</IsActive>
            <Msg></Msg>
      </Data>
      <RequestId>7CDBA7D5-8D62-4D24-9C65-510D621278DB</RequestId>
</CheckExpandStatus>
    "Data":{
        "IsActive":true,
        "Msg":""
```

`},`

```json
    "RequestId":"7CDBA7D5-8D62-4D24-9C65-510D621278DB",
    "Success":true
```

##### 1.1.5.4 CheckSqlAuditEnableStatus

Verifies whether SQL audit is enabled for a PolarDB-X 1.0 logical database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CheckSqlAuditEna bleStatus | The operation that you want to perform. Set the value to CheckSqlAuditEna bleStatus. |
| DbName | String | Yes | drds db _ | The name of the PolarDB-X database. |

| loud Native Distribute olarDB-X | d Database |   | Developer G | uide·Developer Guide 1.0 |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | drds sample request i _ _ _ d | The ID of the request. |
| Status | String | enabled | Indicates whether SQL audit was enabled for the logical database. Valid values: enabled and disabled. |
| Success | Boolean | true | Indicates whether the request was successful. |

```json
http(s)://[Endpoint]/? Action=CheckSqlAuditEnableStatus &DbName=drds_db &DrdsInstanceId=drdsxxxxxxxxxxx <CheckSqlAuditEnableStatus>
      <Status>"disabled"</Status>
      <RequestId>FF13E47D-4E38-4A5A-BA68-32A554E6FE10</RequestId>
</CheckSqlAuditEnableStatus>
    "Status":"\"disabled\"",
    "RequestId":"FF13E47D-4E38-4A5A-BA68-32A554E6FE10",
    "Success":true
```

##### 1.1.5.5 CreateDrdsDB

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
| RdsInstance.N | RepeatList | No | ["rds id1", _ "rds id2"] _ | This parameter is required only for horizontal partitioning. It is a JSON array string. |
| RdsSuperAccount. N.AccountName | String | No | rdsuser | The name of the ApsaraDB RDS for MySQL privileged account. |

| loud Native Distribute olarDB-X | d Database |   | Developer G | uide·Developer Guide 1.0 |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
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

```json
    "RequestId":"FF13E47D-4E38-4A5A-BA68-32A554E610EF",
    "Success":true
```

##### 1.1.5.6 CreateShardTask

Creates a partitioning task for a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateShardTask | The operation that you want to perform. Set the value to CreateShardTask. |
| DbName | String | Yes | test db _ | The name of the PolarDB-X database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| SourceTableName | String | Yes | student tb1 _ | The name of the source table. |
| TargetTableName | String | Yes | student tb2 _ | The name of the destination table. |
| TaskType | String | Yes | SINGLE TO SHARD _ _ | The type of the task. Valid values: SHARD TO SINGLE, _ _ SINGLE TO SHARD, _ _ and SHARD TO SHARD. _ _ |
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Boolean | true | Indicates whether the partitioning task was created. |
| RequestId | String | F8997D95-94AD-416A- AE70-E24D087045ED | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```json
http(s)://[Endpoint]/? Action=CreateShardTask &DbName=test_db &DrdsInstanceId=drdsxxxxxxxxxxxx &SourceTableName=student_tb1 &TargetTableName=student_tb2 &TaskType=SINGLE_TO_SHARD <CreateShardTaskResponse>
      <Data>true</Data>
      <RequestId>F8997D95-94AD-416A-AE70-E24D087045ED</RequestId>
</CreateShardTaskResponse>
    "Data":true,
    "RequestId":"F8997D95-94AD-416A-AE70-E24D087045ED",
    "Success":true
```

##### 1.1.5.7 DatalinkReplicationPrecheck

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

```json
<DatalinkReplicationPrecheckResponse>
      <Data>20190886</Data>
      <RequestId>F8997D95-94AD-416A-AE70-E24D087045ED</RequestId>
</DatalinkReplicationPrecheckResponse>
    "Data":20190886,
    "RequestId":"F8997D95-94AD-416A-AE70-E24D087045ED",
    "Success":true
```

##### 1.1.5.8 DeleteShardTasks

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

```json
http(s)://[Endpoint]/? Action=DeleteShardTasks &DbName=test_db &DrdsInstanceId=drdsxxxxxxxxxx <DeleteShardTasksResponse>
      <Data>true</Data>
      <RequestId>F8997D95-94AD-416A-AE70-E24D087045ED</RequestId>
</DeleteShardTasksResponse>
    "Data":true,
    "RequestId":"F8997D95-94AD-416A-AE70-E24D087045ED",
    "Success":true
```

##### 1.1.5.9 DescribeBackMenu

Queries whether a PolarDB-X instance supports backup and recovery.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackMenu | The operation that you want to perform. Set the value to DescribeBackMenu . |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | xxxxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| List | - | - | The list of supported items. |
| list | - | - | The details about a supported item. |
| MenuName | String | phy | The mode of the backup. Valid values: logic: logical backup phy: physical backup |
| Support | Boolean | true | Indicates whether the PolarDB-X instance supports backup and recovery. |
| RequestId | String | 60C21BE4-EDFE-454C- 95ED-3A5C7493D74A | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```
http(s)://[Endpoint]/? Action=DescribeBackMenu &DrdsInstanceId=drdsxxxxxxxxxxxx
```

```json
<DescribeBackMenuResponse>
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
    "RequestId":"60C21BE4-EDFE-454C-95ED-3A5C7493D74A",
    "Success":true,
    "List":[
            "MenuName":"phy",
            "Support":true
```

`},`

```json
            "MenuName":"logic",
            "Support":true
```

`]`

##### 1.1.5.10 DescribeBackupDbs

Queries the databases that can be restored for a PolarDB-X instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackupDb s | The operation that you want to perform. Set the value to DescribeBackupDb s. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
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

```json
    "RequestId":"9EF10719-C34F-4E64-8260-D29C1A78B5DD",
    "DbNames":{
        "dbName":[]
```

`},`

```json
    "Success":true
```

##### 1.1.5.11 DescribeBackupTimes

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

| Parameter | Type | Example | Description |
|---|---|---|---|
| StartTime | String | 1568632853000 | The timestamp that specifies the beginning of the time range to query. |
| Success | Boolean | true | Indicates whether the request was successful. |

```json
http(s)://[Endpoint]/? Action=DescribeBackupTimes &DrdsInstanceId=drdsxxxxxxxxxxx <DescribeBackupTimesResponse>
      <RequestId>4780A19F-5ECB-4C56-AD20-966A3FF99772</RequestId>
      <RestoreTime>
            <EndTime>1568636922671</EndTime>
            <StartTime>1568632853000</StartTime>
      </RestoreTime>
</DescribeBackupTimesResponse>
    "RestoreTime":{
        "EndTime":"1568636922671",
        "StartTime":"1568632853000"
```

`},`

```json
    "RequestId":"4780A19F-5ECB-4C56-AD20-966A3FF99772",
    "Success":true
```

##### 1.1.5.12 DescribeBroadcastTables

Queries the broadcast tables in a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBroadcast Tables | The operation that you want to perform. Set the value to DescribeBroadcast Tables. |
| DbName | String | Yes | test db _ | The name of the PolarDB-X database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| Query | String | Yes | tb1 | The query content. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| IsShard | Boolean | true | Indicates whether the table was partitioned. |
| List | - | - | The list of broadcast tables. |
| Broadcast | Boolean | true | Indicates whether the table is a broadcast table. |
| BroadcastType | String | 1 | The type of the broadcast table. Valid values: 1: multi-write mode 2: synchronous link mode |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DbInstType | Integer | 0 | The type of the storage instance. The value 0 indicates RDS. |
| IsShard | Boolean | false | Indicates whether the table was partitioned. |
| Status | Integer | 1 | The status of the broadcast table. Valid values: 1: activated 2: activating 3: activation exception |
| Table | String | nation | The name of the table. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 40 | The number of entries returned per page. |
| RequestId | String | 86E420ED-43F2-4788- A58C-9218491FFB09 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |
| Total | Integer | 2 | The total number of entries. |

```
http(s)://[Endpoint]/? Action=DescribeBroadcastTables &DbName=test_db &DrdsInstanceId=drdsxxxxxxxxxx &Query=tb1
```

```json
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
    "PageNumber":1,
    "PageSize":40,
    "RequestId":"86E420ED-43F2-4788-A58C-9218491FFB09",
    "Success":true,
    "List":[
            "Status":1,
            "IsShard":false,
            "BroadcastType":1,
            "Broadcast":true,
            "Table":"nation",
            "DbInstType":0
```

`},`

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

##### 1.1.5.13 DescribeDbInstanceDbs

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

```json
                  <DbName>db_newsudbv</DbName>
            </Database>
      </Databases>
      <total>1</total>
      <RequestId>E9F3D991-08DE-4B74-BE0E-06B80958F5DC</RequestId>
</DescribeDbInstanceDbsResponse>
    "total":1,
    "Databases":{
        "Database":[
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

##### 1.1.5.14 DescribeDbInstances

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

| Developer Guide·Developer | Guide ( | Cloud N | ative Distributed Database |
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

```json
    "Items":{
        "DBInstance":[
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

##### 1.1.5.15 DescribeDrdsDB

Queries the details about a database on a PolarDB-X instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDrdsDB | The operation that you want to perform. Set the value to DescribeDrdsDB. |
| DbName | String | Yes | db test _ | The name of the PolarDB-X database. |

| eveloper Guide·Deve .0) | loper Guide ( |   | Cloud Native | Distributed Database PolarDB- |
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

```json
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

##### 1.1.5.16 DescribeDrdsDbInstance

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

| loud Native Distributed Da olarDB-X | tabase | Develo | per Guide·Developer Guide 1.0 |
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

| D 1 | eveloper Guide·Developer .0) | Guide ( | Cloud N | ative Distributed Database PolarDB- | X |
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

##### 1.1.5.17 DescribeDrdsDbInstances

Queries the ApsaraDB RDS for MySQL instances of a PolarDB-X 1.0 database. When you query the primary ApsaraDB RDS for MySQL instances of a PolarDB-X 1.0 database, the ReadOnlyInstances attribute of each primary ApsaraDB RDS for MySQL instance specifies the list of read-only ApsaraDB RDS for MySQL instances used by this primary ApsaraDB RDS for MySQL instance for the current database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DbName | String | Yes | dbname | The name of the PolarDB-X 1.0 database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | ASU6xxxxxxxxxxxx xxxx | The AccessKey ID provided to you by Alibaba Cloud. |

| loud Native Distribute | d Database |   | Developer G | uide·Developer Guide |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageNumber | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. |

| DbInstances | - | - | The list of ApsaraDB RDS for MySQL instances of the PolarDB-X 1.0 database. |
|---|---|---|---|
| DbInstance | - | - | The details about a ApsaraDB RDS for MySQL instance in the PolarDB-X 1.0 database. |
| ConnectUrl | String | rm- m5xxxxxxxxx82.mysql.rd s.aliyuncs.com | The URL of the ApsaraDB RDS for MySQL instance, which is returned when the corresponding API operation of the ApsaraDB RDS for MySQL is called. |
| DBInstanceId | String | rm-m5xxxxxxxxx82 | The ID of the ApsaraDB RDS for MySQL instance. |

| DBInstanceStatus | String | 1 | The status of the ApsaraDB RDS for MySQL instance. Valid values: 0: creating 1: running 3: deleting 5: restarting 6: changing specifications 7: backing up 8: switching between classic and Virtual Private Cloud (VPC) networks 9: migrating 11: migrating data 12: generating a disaster recovery instance 13: importing data 14: Data is being imported from other ApsaraDB RDS for MySQL instances. 15: switching for disaster recovery 16: creating a temporary instance 17: creating the network 18: cloning the instance 19: switching the link 20: migrating the read-only instance |
|---|---|---|---|
| DbInstType | String | RDS | The type of the ApsaraDB RDS for MySQL instance. Currently, only ApsaraDB for RDS instances are supported. |
| Engine | String | MySQL | The engine that the ApsaraDB RDS for MySQL instance runs. Valid value: MySQL. |

| EngineVersion | String | 5.7 | The version of the engine that the storage instance runs. Valid values: MySQL 5.7, MySQL 5.6, and MySQL 5.5. |
|---|---|---|---|
| ExpireTime | String | 1237486127634 | The time when the ApsaraDB RDS for MySQL instance expires. |
| NetworkType | String | VPC | The network type of the ApsaraDB RDS for MySQL instance. Not e Apsara Stack does not support VPC networks. |
| Port | Integer | 3306 | The port of the ApsaraDB RDS for MySQL instance. |
| RdsInstType | String | Primary | Indicates whether the ApsaraDB RDS for MySQL instance is a primary instance or a read-only instance. |
| ReadOnlyInstances | - | - | The list of read-only ApsaraDB RDS for MySQL instances. |
| ReadOnlyInstance | - | - | The details about a read-only ApsaraDB RDS for MySQL instance. |
| ConnectUrl | String | rm- m5xxxxxxxxx82.mysql.rd s.aliyuncs.com | The URL of the read- only ApsaraDB RDS for MySQL instance, which is returned when the corresponding API operation of the ApsaraDB RDS for MySQL is called. |
| DBInstanceStatus | String | 1 | The status of the read- only ApsaraDB RDS for MySQL instance. |

| DbInstType | String | RDS | The type of the read- only ApsaraDB RDS for MySQL instance. |
|---|---|---|---|
| Engine | String | MySQL | The engine that the read-only ApsaraDB RDS for MySQL instance runs. |
| EngineVersion | String | 5.7 | The version of the engine that the read- only ApsaraDB RDS for MySQL instance runs. |
| ExpireTime | String | 123421352351234 | The timestamp when the read-only ApsaraDB RDS for MySQL instance expires. |
| InstanceName | String | rm-m5xxxxxxxxx82 | An invalid parameter. |
| NetworkType | String | VPC | The network type of the read-only ApsaraDB RDS for MySQL instance. |
| PayType | String | Postpaid | The billing method of the read-only ApsaraDB RDS for MySQL instance. |
| Port | Integer | 3306 | The port of the read- only ApsaraDB RDS for MySQL instance. |
| RdsInstType | String | RDS | The type of the read- only ApsaraDB RDS for MySQL instance. |
| ReadWeight | Integer | 70 | The read weight of the read-only ApsaraDB RDS for MySQL instance. |
| RemainDays | Integer | 0 | The remaining number of days before the read-only ApsaraDB RDS for MySQL instance expires. |
| ReadWeight | Integer | 30 | The read weight of the read-only ApsaraDB RDS for MySQL instance in the PolarDB-X 1.0 database. |

| RemainDays | Integer | 0 | The remaining number of days before the prepaid read-only ApsaraDB RDS for MySQL instance expires. |
|---|---|---|---|
| PageNumber | String | 1 | The number of the page returned. |
| PageSize | String | 10 | The number of entries returned per page. |
| RequestId | String | 2F7F8080-9132-4279- 85D0-B7E5C4305162 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |
| Total | String | 1 | The total number of primary read-only ApsaraDB RDS for MySQL instances. |

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

```json
    "PageNumber":1,
    "PageSize":10,
    "RequestId":"658B6F25-442A-4996-8AAE-F77DAFBC9BAA",
    "DbInstances":{
        "DbInstance":[
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

##### 1.1.5.18 DescribeDrdsDbRdsNameList

Queries the IDs of the storage instances of a PolarDB-X 1.0 database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDrdsDbRd sNameList | The operation that you want to perform. Set the value to DescribeDrdsDbRd sNameList. |
| DbName | String | Yes | drds test _ | The name of the PolarDB-X 1.0 database. |

| 1 | Developer Guide·Deve .0) | loper Guide ( |   | Cloud Native | Distributed Database PolarDB- | X |
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

##### 1.1.5.19 DescribeDrdsDbRdsRelationInfo

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

```json
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
    "Data":{
        "Data":[
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

##### 1.1.5.20 DescribeDrdsDbTasks

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

| loud Native Distributed Da olarDB-X | tabase | Develo | per Guide·Developer Guide 1.0 |
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

```json
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
    "RequestId":"7E54C57C-DF5A-4FE8-8E25-DC888817B54D",
    "Tasks":{
        "Task":[
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

##### 1.1.5.21 DescribeDrdsInstanceDbMonitor

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

| 1 | Developer Guide·Developer .0) | Guide ( | Cloud N | ative Distributed Database PolarDB- | X |
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

```json
    "Data":[
            "Values":[
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

##### 1.1.5.22 DescribeDrdsShardingDbs

Queries details about a horizontally partitioned PolarDB-X 1.0 database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDrdsShard ingDbs | The operation that you want to perform. Set the value to DescribeDrdsShard ingDbs. |
| DbName | String | Yes | drds test _ | The name of the PolarDB-X 1.0 database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |

| eveloper Guide·Deve .0) | loper Guide ( |   | Cloud Native | Distributed Database PolarDB- |
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

| loud Native Distributed Da olarDB-X | tabase | Develo | per Guide·Developer Guide 1.0 |
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

##### 1.1.5.23 DescribeDrdsSlowSqls

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

| Developer Guide·Developer | Guide ( | Cloud N | ative Distributed Database |
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

##### 1.1.5.24 DescribeDrdsSqlAuditStatus

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

| Developer Guide·Developer .0) | Guide ( | Cloud N | ative Distributed Database PolarDB- |
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

##### 1.1.5.25 DescribeExpandLogicTableInfoList

Queries the shard keys of a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeExpandLo gicTableInfoList | The operation that you want to perform. Set the value to DescribeExpandLo gicTableInfoList. |
| DbName | String | Yes | drds db _ | The name of the PolarDB-X database. |

| loud Native Distribute | d Database |   | Developer G | uide·Developer Guide |
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

##### 1.1.5.26 DescribeGlobalBroadcastType

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

| C P | loud Native Distributed Da olarDB-X | tabase | Develo | per Guide·Developer Guide 1.0 | ( ) |
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

##### 1.1.5.27 DescribeHotDbList

Queries the available databases for hot-spot scale-out of a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeHotDbList | The operation that you want to perform. Set the value to DescribeHotDbList . |
| DbName | String | Yes | test | The name of the PolarDB-X database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |

| eveloper Guide·Deve .0) | loper Guide ( |   | Cloud Native | Distributed Database PolarDB- |
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

##### 1.1.5.28 DescribeInstDbLogInfo

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

| 1 | Developer Guide·Developer .0) | Guide ( | Cloud N | ative Distributed Database PolarDB- | X |
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

##### 1.1.5.29 DescribeRDSPerformance

Queries the performance data of ApsaraDB RDS for MySQL instances for a PolarDB-X instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRDSPerfor mance | The operation that you want to perform. Set the value to DescribeRDSPerfor mance. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |

| loud Native Distribute olarDB-X | d Database |   | Developer G | uide·Developer Guide 1.0 |
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

| Developer Guide·Developer .0) | Guide ( | Cloud N | ative Distributed Database PolarDB- |
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

##### 1.1.5.30 DescribeRdsPerformanceSummary

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

```json
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
    "successResponse":true,
    "requestId":"395533CB-12E8-4FDC-8934-127FD2024C0A",
    "data":{
        "RequestId":"395533CB-12E8-4FDC-8934-127FD2024C0A",
        "RdsPerformanceInfos":[
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

##### 1.1.5.31 DescribeRdsSuperAccountInstances

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

```json
http(s)://[Endpoint]/? Action=DescribeRdsSuperAccountInstances &DrdsInstanceId=drdsxxxxxxxxxx &RdsInstance.1=['rm-bp1xxxxxxxxxxx','rm-bp1xxxxxxxxxx'] <DescribeRdsSuperAccountInstancesResponse>
      <code>200</code>
      <data>
            <RequestId>62CA96F4-B94F-4059-B23E-A58CCF318D3E</RequestId>
            <DbInstances></DbInstances>
      </data>
      <requestId>62CA96F4-B94F-4059-B23E-A58CCF318D3E</requestId>
      <successResponse>true</successResponse>
</DescribeRdsSuperAccountInstancesResponse>
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

##### 1.1.5.32 DescribeRecycleBinStatus

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

```json
<DescribeRecycleBinStatusResponse>
      <code>200</code>
      <data>
            <Status>enable</Status>
            <RequestId>E7D9B458-2C2D-44E3-BD55-92AD2172303F</RequestId>
      </data>
      <requestId>E7D9B458-2C2D-44E3-BD55-92AD2172303F</requestId>
      <successResponse>true</successResponse>
</DescribeRecycleBinStatusResponse>
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

##### 1.1.5.33 DescribeRecycleBinTables

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

```json
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
    "successResponse":true,
    "requestId":"EC985705-2D6B-4B84-9732-BF8F5DCA247A",
    "data":{
        "Data":[
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

##### 1.1.5.34 DescribeShardTaskInfo

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

| C P | loud Native Distributed Da olarDB-X | tabase | Develo | per Guide·Developer Guide 1.0 | ( ) |
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

##### 1.1.5.35 DescribeShardTaskList

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

| loud Native Distributed Da | tabase | Develo | per Guide·Developer Guide |
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

```json
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
    "successResponse":true,
    "requestId":"890BB376-5746-4145-A088-A455F8D359D0",
    "data":{
        "PageNumber":1,
        "PageSize":10,
        "RequestId":"890BB376-5746-4145-A088-A455F8D359D0",
        "Success":true,
        "List":[
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

##### 1.1.5.36 DescribeSqlFlashbakTask

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

| eveloper Guide·Developer .0) | Guide ( | Cloud N | ative Distributed Database PolarDB- |
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

```json
    "successResponse":true,
    "requestId":"11449CF1-6D32-4759-8F93-EAF36F176C41",
    "data":{
        "RequestId":"11449CF1-6D32-4759-8F93-EAF36F176C41",
        "SqlFlashbackTasks":{
            "SqlFlashbackTask":[
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

##### 1.1.5.37 DescribeTable

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

```json
    "successResponse":true,
    "requestId":"5DC75BC2-3F3F-4FE5-8DC9-2A808B9AA401",
    "data":{
        "Data":{
            "List":[
                    "IsPk":"YES",
                    "Extra":"auto_increment",
                    "Index":"PRI",
                    "IsAllowNull":"NO",
                    "ColumnType":"bigint(20)",
                    "ColumnName":"Id"
```

`},`

```json
                    "IsPk":"NO",
                    "Extra":"",
                    "Index":"",
                    "IsAllowNull":"NO",
                    "ColumnType":"varchar(20)",
                    "ColumnName":"Name"
```

`},`

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

##### 1.1.5.38 DescribeTableListByType

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

```json
    "successResponse":true,
    "requestId":"B360F47B-59E3-4D1C-BA03-6BFB1C993F88",
    "data":{
        "PageNumber":1,
        "PageSize":10,
        "RequestId":"B360F47B-59E3-4D1C-BA03-6BFB1C993F88",
        "Success":true,
        "List":[
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

##### 1.1.5.39 DescribeTables

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

```json
    "successResponse":true,
    "requestId":"83AC3D7E-461C-4D87-8ACD-6CC295178C6F",
    "data":{
        "PageNumber":1,
        "PageSize":40,
        "RequestId":"83AC3D7E-461C-4D87-8ACD-6CC295178C6F",
        "Success":true,
        "List":[
                "IsLocked":false,
                "IsShard":false,
                "ShardKey":"null",
                "Broadcast":false,
                "Table":"employee_split",
                "DbInstType":0,
                "AllowFullTableScan":false
```

`},`

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

##### 1.1.5.40 DisableSqlAudit

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

##### 1.1.5.41 ModifyAccountPrivilege

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

```json
http(s)://[Endpoint]/? Action=ModifyAccountPrivilege &AccountName=mytest@% &DrdsInstanceId=drdsxxxxxxxxxxxx <ModifyAccountPrivilegeResponse>
      <RequestId>40E313AD-3B7C-4E34-B3BF-58AD0174D638</RequestId>
</ModifyAccountPrivilegeResponse>
    "RequestId":"40E313AD-3B7C-4E34-B3BF-58AD0174D638",
    "Success":true
```

##### 1.1.5.42 ModifyDrdsIpWhiteList

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

```json
http(s)://[Endpoint]/? Action=ModifyDrdsIpWhiteList &DbName=test &DrdsInstanceId=drdsxxxxxxxxxx &IpWhiteList=127.xx.xx.1,10.xx.xx.1
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

##### 1.1.5.43 ModifyRdsReadWeight

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

```json
<ModifyRdsReadWeightResponse>
      <RequestId>B12FC174-D5CE-4A6E-83C1-0F8F864FF70A</RequestId>
</ModifyRdsReadWeightResponse>
    "RequestId":"B12FC174-D5CE-4A6E-83C1-0F8F864FF70A",
    "Success":"true"
```

##### 1.1.5.44 DescribeDbInstances

Queries the storage instances, namely, ApsaraDB RDS for MySQL instances of a PolarDB-X instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDbInstanc es | The operation that you want to perform. Set the value to DescribeDbInstanc es. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | Yes | testxxxxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |
| DbInstType | String | No | RDS | The type of the storage instance. Set the value to RDS. |
| PageNumber | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |

| loud Native Distribute | d Database |   | Developer G | uide·Developer Guide |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Search | String | No | pc- bp1xxxxxxxxxxxx | Query by storage instance ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | - | - | The list of returned storage instances. |
| DBInstance | - | - | The details about a storage instance. |
| DBInstanceDescription | String | pc-bp1xxxxxxxxxxxxxx | The description of the storage instance. |
| DBInstanceId | String | pc-bp1xxxxxxxxxxxxxx | The ID of the storage instance. |
| DBInstanceStatus | Integer | 1 | The status of the storage instance. Valid values: 0: creating 1: running 3: deleting 5: restarting 6: changing specifications 7: recovering 8: switching between the classic network and VPC network |
| DBInstanceType | String | RDS | The type of the storage instance. Example: RDS. |
| Engine | String | mysql | The engine that the storage instance runs. |
| EngineVersion | String | 5.6 | The version of the engine that the storage instance runs. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| InstanceNetworkType | String | CLASSIC | The network type of the storage instance. Valid values: CLASSIC: classic network VPC: Virtual Private Cloud (VPC) network Not e Apsara Stack does not support VPC networks. |
| ReadOnlyDBInstanceId | - | [] | The list of read-only storage instances. |
| ReadOnlyDBInstanceId | - | - | The details about a read-only storage instance. |
| RegionId | String | cn-hangzhou | The ID of the region where the storage instance is located. |
| ZoneId | String | cn-hangzhou-a | The ID of the zone where the storage instance is located. |
| RequestId | String | 05670C01-093E-4DF4- 99FA-0C63FF60250D | The ID of the request. |

```
http(s)://[Endpoint]/? Action=DescribeDbInstances &DrdsInstanceId=drdsxxxxxxxxxxx
```

```json
<DescribeDbInstancesResponse>
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
    "Items":{
        "DBInstance":[
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

##### 1.1.5.45 ReleaseHiStoreInstance

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

```json
    "RequestId":"B12FC174-D5CE-4A6E-83C1-0F8F864FF70A",
    "Success":"true"
```

##### 1.1.5.46 RemoveBackupsSet

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

```json
http(s)://[Endpoint]/? Action=RemoveBackupsSet &BackupId=c778036f-d464-11e9-8d45-7370dca6206b &DrdsInstanceId=drdsxxxxxxxxxx <RemoveBackupsSetResponse>
      <RequestId>B12FC174-D5CE-4A6E-83C1-0F8F864FF70A</RequestId>
</RemoveBackupsSetResponse>
    "RequestId":"B12FC174-D5CE-4A6E-83C1-0F8F864FF70A",
    "Success":"true"
```

##### 1.1.5.47 RemoveDrdsDbFailedRecord

Removes database creation failure records from a PolarDB-X instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RemoveDrdsDbFail edRecord | The operation that you want to perform. Set the value to RemoveDrdsDbFail edRecord. |
| DbName | String | Yes | db test _ | The name of the PolarDB-X database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxx | The ID of the PolarDB-X instance. |

| loud Native Distribute | d Database |   | Developer G | uide·Developer Guide |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AccessKeyId | String | No | LTAI8Gxxxxxxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5D64DE5944A1E541E0CB 908A | The ID of the request. |
| Result | Boolean | true | Indicates whether the database creation failure records were removed from the PolarDB-X instance. |
| Success | Boolean | true | Indicates whether the request was successful. |

```xml
http(s)://[Endpoint]/? Action=RemoveDrdsDbFailedRecord &DbName=db_test &DrdsInstanceId=drdsxxxxxxxxxx <RemoveDrdsDbFailedRecordResponseponse>
      <code>200</code>
      <data>
            <RequestId>B12FC174-D5CE-4A6E-83C1-0F8F864FF70A</RequestId>
            <Result>true</Result>
      </data>
      <requestId>B12FC174-D5CE-4A6E-83C1-0F8F864FF70A</requestId>
      <successResponse>true</successResponse>
</RemoveDrdsDbFailedRecordResponseponse>
```

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

##### 1.1.5.48 RemoveRecycleBinTable

Removes tables from the recycle bin for a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RemoveRecycleBin Table | The operation that you want to perform. Set the value to RemoveRecycleBin Table. |
| DbName | String | Yes | my drds db _ _ | The name of the PolarDB-X 1.0 database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| TableName | String | Yes | buy order _ | The name of the PolarDB-X 1.0 logical table. |
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Boolean | true | Indicates whether tables were removed from the table recycle bin. |
| RequestId | String | 6F70CE62-5077-4B7B- 95BC-4DAC45614DBE | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```json
http(s)://[Endpoint]/? Action=RemoveRecycleBinTable &DbName=my_drds_db &DrdsInstanceId=drdsxxxxxxxxxx &TableName=buy_order <RemoveRecycleBinTableResponse>
      <RequestId>A3140FC7-B78B-4D8E-B0C8-926D28669934</RequestId>
      <Data>true</Data>
</RemoveRecycleBinTableResponse>
    "Data":true,
    "RequestId":"A3140FC7-B78B-4D8E-B0C8-926D28669934",
    "Success":true
```

##### 1.1.5.49 ResetDrdsToRdsConnections

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

```
http(s)://[Endpoint]/? Action=ResetDrdsToRdsConnections &DbName=test_my_db &DrdsInstanceId=drdsxxxxxxxxxxx
```

```json
<ResetDrdsToRdsConnectionsResponse>
      <RequestId>A3140FC7-B78B-4D8E-B0C8-926D28669934</RequestId>
      <Result>true</Result>
</ResetDrdsToRdsConnectionsResponse>
    "Result":true,
    "RequestId":"A3140FC7-B78B-4D8E-B0C8-926D28669934",
    "Success":true
```

##### 1.1.5.50 SetupBroadcastTables

Configures a broadcast table for a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetupBroadcastTa bles | The operation that you want to perform. Set the value to SetupBroadcastTa bles. |
| Active | Boolean | Yes | true | Specifies whether to turn on the broadcast table switch. |
| DbName | String | Yes | test db _ | The name of the PolarDB-X 1.0 database. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| TableName.N | RepeatList | Yes | tb1 | The name of the PolarDB-X 1.0 table. |
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |

| Developer Guide·Deve .0) | loper Guide ( |   | Cloud Native | Distributed Database PolarDB- |
|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |

```json
http(s)://[Endpoint]/? Action=SetupBroadcastTables &Active=true &DbName=test_db &DrdsInstanceId=drdsxxxxxxxxxxxxx &TableName.1=tb1 <SetupBroadcastTablesResponse>
        <RequestId>A3140FC7-B78B-4D8E-B0C8-926D28669934</RequestId>
        <Data>true</Data>
</SetupBroadcastTablesResponse>
    "Data":true,
    "RequestId":"A3140FC7-B78B-4D8E-B0C8-926D28669934",
    "Success":true
```

##### 1.1.5.51 SetupRecycleBinStatus

Enables the table recycle bin for a PolarDB-X database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

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

```json
<SetupRecycleBinStatusResponse>
        <RequestId>A3140FC7-B78B-4D8E-B0C8-926D28669934</RequestId>
        <Data>true</Data>
</SetupRecycleBinStatusResponse>
    "Data":"true",
    "RequestId":"A3140FC7-B78B-4D8E-B0C8-926D28669934",
    "Success":true
```

##### 1.1.5.52 SetupTable

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

```json
http(s)://[Endpoint]/? Action=SetupTable &AllowFullTableScan=true &DbName=dbtest &DrdsInstanceId=drdsxxxxxxxxx &TableName.1=tbtest <SetupTableResponse>
        <RequestId>A3140FC7-B78B-4D8E-B0C8-926D28669934</RequestId>
        <Data>true</Data>
</SetupTableResponse>
    "Data":"true",
    "RequestId":"A3140FC7-B78B-4D8E-B0C8-926D28669934",
    "Success":true
```

##### 1.1.5.53 StartRestore

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

```json
http(s)://[Endpoint]/? Action=StartRestore &DrdsInstanceId=drds43dsaew1 <StartRestoreResponse>
     <Result>success</Result>
     <RequestId>FE104D26-AC19-49B5-AC67-947F6915E07E</RequestId>
</StartRestoreResponse>
    "Result":"success",
    "RequestId":"721C71DD-D3D0-4327-BFDD-67832698F55B",
    "Success":true
```

##### 1.1.5.54 SubmitCleanTask

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

```json
http(s)://[Endpoint]/? Action=SubmitCleanTask &DbName=test1 &DrdsInstanceId=drdsxxxxxxxxxxx &ExpandType=smooth_expand &JobId=123 &ParentJobId=123 <SubmitCleanTaskResponse>
      <RequestId>DSSDF-SEWE-23ERW</RequestId>
</SubmitCleanTaskResponse>
    "RequestId":"DSSDF-SEWE-23ERW",
    "Success":true
```

##### 1.1.5.55 SubmitSmoothExpandPreCheck

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

```json
<SubmitSmoothExpandPreCheckResponse>
     <Msg>success</Msg>
     <RequestId>FE104D26-AC19-49B5-AC67-947F6915E07E</RequestId>
     <TaskId>97358</TaskId>
</SubmitSmoothExpandPreCheckResponse>
    "RequestId":"FE104D26-AC19-49B5-AC67-947F6915E07E",
    "Msg":"success",
    "TaskId":97358,
    "Success":true
```

##### 1.1.5.56 SubmitSmoothExpandPreCheckTask

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

```json
http(s)://[Endpoint]/? Action=SubmitSmoothExpandPreCheckTask &DbName=test &DrdsInstanceId=drdsxxxxxxxxxx <SubmitSmoothExpandPreCheckTaskResponse>
     <Msg>success</Msg>
     <RequestId>FE104D26-AC19-49B5-AC67-947F6915E07E</RequestId>
     <TaskId>97358</TaskId>
</SubmitSmoothExpandPreCheckTaskResponse>
    "RequestId":"FE104D26-AC19-49B5-AC67-947F6915E07E",
    "Msg":"success",
    "TaskId":97358,
    "Success":true
```

##### 1.1.5.57 SubmitSmoothExpandTask

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

| Developer Guide·Deve | loper Guide ( |   | Cloud Native | Distributed Database |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TransferTaskInfos. N.InstanceType | String | No | RDS | The type of the instance to be migrated. Set the value to ApsaraDB RDS for MySQL. |
| TransferTaskInfos. N.SrcInstanceNam e | String | No | rm-m23xxxxxxxxxx | The ID of the instance to be migrated. |

```json
http(s)://[Endpoint]/? Action=SubmitSmoothExpandTask &DbName=test &DrdsInstanceId=drdsxxxxxxxxxx <SubmitSmoothExpandTaskResponse>
     <RequestId>DSSDF-SEWE-23ERW</RequestId>
</SubmitSmoothExpandTaskResponse>
    "RequestId":"DSSDF-SEWE-23ERW",
    "success":true
```

##### 1.1.5.58 SubmitSwitchTask

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

```json
http(s)://[Endpoint]/? Action=SubmitSwitchTask &DbName=test &DrdsInstanceId=drdsxxxxxxxxx &ExpandType=smooth_expand &JobId=123 &ParentJobId=123 <SubmitSwitchTaskResponse>
      <RequestId>DSSDF-SEWE-23ERW</RequestId>
</SubmitSwitchTaskResponse>
    "RequestId":"DSSDF-SEWE-23ERW",
    "Success":true
```

##### 1.1.5.59 ValidateShardTask

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

```json
    "RequestId":"DSSDF-SEWE-23ERW",
    "List":[
            "Result":0,
            "Item":"has_data"
```

`},`

```json
            "result":0,
            "item":"same_schema"
```

`},`

```json
            "result":0,
            "item":"uk_in_source_table"
```

`},`

```json
            "result":0,
            "item":"uk_in_target_table"
```

`],`

```json
    "success":true
```

##### 1.1.5.60 RemoveDrdsDb

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

```json
http(s)://[Endpoint]/? Action=RemoveDrdsDb &DbName=db_test &DrdsInstanceId=drds****c6vxxyzd <RemoveDrdsDbResponse>
      <RequestId>B12FC174-D5CE-4A6E-83C1-0F8F864FF70A</RequestId>
</RemoveDrdsDbResponse>
    "RequestId":"B12FC174-D5CE-4A6E-83C1-0F8F864FF70A",
    "Success":true
```

##### 1.1.5.61 RefreshDrdsAtomUrl

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

```json
<RefreshDrdsAtomUrlResponse>
      <RequestId>B12FC174-D5CE-4A6E-83C1-0F8F864FF70A</RequestId>
</RefreshDrdsAtomUrlResponse>
    "RequestId":"B12FC174-D5CE-4A6E-83C1-0F8F864FF70A",
    "Success":"true"
```

#### 1.1.6 Instance management

##### 1.1.6.1 CreateInstanceAccount

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

```json
http(s)://[Endpoint]/? Action=CreateInstanceAccount &AccountName=drds_sample_account &DrdsInstanceId=drdsxxxxxxxxxxxxxx &Password=password &DbPrivilege=[{"DbName":"testdb", "Privilege":"RW"}] <CreateInstanceAccount>
      <RequestId>FF13E47D-4E38-4A5A-BA68-4E610EF35A25</RequestId>
</CreateInstanceAccount>
    "RequestId":"FF13E47D-4E38-4A5A-BA68-4E610EF35A25",
    "Success":true
```

##### 1.1.6.2 DescribeDrdsDBs

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

| loud Native Distributed Da olarDB-X | tabase | Develo | per Guide·Developer Guide 1.0 |
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

```json
    "Data":{
        "Db":[
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

##### 1.1.6.3 DescribeDrdsInstance

Queries the details about a PolarDB-X 1.0 instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDrdsInsta nce | The operation that you want to perform. Set the value to DescribeDrdsInsta nce. |
| DrdsInstanceId | String | Yes | drdssexxxxxxxx | The ID of the PolarDB-X 1.0 instance. |

| loud Native Distribute olarDB-X | d Database |   | Developer G | uide·Developer Guide 1.0 |
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

| loud Native Distributed Da | tabase | Develo | per Guide·Developer Guide |
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

| .0) |   |   | PolarDB- |
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

##### 1.1.6.4 DescribeDrdsInstanceLevelTasks

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

| loud Native Distributed Da olarDB-X | tabase | Develo | per Guide·Developer Guide 1.0 |
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

```json
    "RequestId":"1BEEBC05-437E-456D-94A4-CEE1F5676BCF",
    "Tasks":{
        "Task":[
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

##### 1.1.6.5 DescribeDrdsInstanceMonitor

Queries the monitoring data of a PolarDB-X 1.0 instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDrdsInsta nceMonitor | The operation that you want to perform. Set the value to DescribeDrdsInsta nceMonitor. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| EndTime | Long | Yes | 1568705520000 | The timestamp that specifies the end of the time range to query. |
| Key | String | Yes | cpu | The monitoring metric. |

| loud Native Distribute olarDB-X | d Database |   | Developer G | uide·Developer Guide 1.0 |
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

```json
    "Data":[
            "Values":[
                    "Value":"1.00",
                    "Date":1568703720000
```

`},`

```json
                    "Value":"0.93",
                    "Date":1568703780000
```

`},`

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

##### 1.1.6.6 DescribeDrdsInstances

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

| loud Native Distributed Da | tabase | Develo | per Guide·Developer Guide |
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

| C P | loud Native Distributed Da olarDB-X | tabase | Develo | per Guide·Developer Guide 1.0 | ( ) |
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

```json
    "PageNumber":1,
    "PageSize":20,
    "RequestId":"8734773E-7B21-4A22-9106-CBD245F8AF7D",
    "Instances":{
        "Instance":[
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

##### 1.1.6.7 DescribeDrdsInstanceVersion

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

```json
<DescribeDrdsInstanceVersion>
      <RequestId>88AFEF28-DF04-4E21-9CE9-277D3C19E3CD</RequestId>
      <Data>
            <InstanceVersion>5.3.12-15682777</InstanceVersion>
            <NewestVersion>5.3.12-15682777</NewestVersion>
      </Data>
</DescribeDrdsInstanceVersion>
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

##### 1.1.6.8 DescribeDrdsParams

Queries the parameters of a PolarDB-X 1.0 instance or database.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDrdsPara ms | The operation that you want to perform. Set the value to DescribeDrdsPara ms. |
| DrdsInstanceId | String | Yes | DescribeDrdsPara ms | The ID of the PolarDB-X 1.0 instance. |

| D 1 | eveloper Guide·Deve .0) | loper Guide ( |   | Cloud Native | Distributed Database PolarDB- | X |
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

| loud Native Distributed Da olarDB-X | tabase | Develo | per Guide·Developer Guide 1.0 |
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

```json
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
    "RequestId":"29D7422F-24DD-42D8-A04E-EBCE4B4A416A",
    "Success":true,
    "List":[
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

`},`

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

`},`

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

`},`

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

##### 1.1.6.9 DescribeDrdsTasks

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

##### 1.1.6.10 DescribeHiStoreInstanceInfo

Queries the details about a HiStore instance of a PolarDB-X instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeHiStoreIns tanceInfo | The operation that you want to perform. Set the value to DescribeHiStoreIns tanceInfo. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |

| Developer Guide·Deve | loper Guide ( |   | Cloud Native | Distributed Database |
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

##### 1.1.6.11 DescribeInstanceAccounts

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

| Developer Guide·Developer | Guide ( | Cloud N | ative Distributed Database |
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

##### 1.1.6.12 DescribeInstanceMenuSwitch

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

##### 1.1.6.13 DescribeInstDbSlsInfo

Queries the names of the Log Service project and Logstore used by SQL audit.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeInstDbSlsI nfo | The operation that you want to perform. Set the value to DescribeInstDbSlsI nfo. |
| DbName | String | Yes | drdsdb | The name of the PolarDB-X database. |

| Developer Guide·Deve .0) | loper Guide ( |   | Cloud Native | Distributed Database PolarDB- |
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

##### 1.1.6.14 DescribePreCheckResult

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

| Developer Guide·Developer .0) | Guide ( | Cloud N | ative Distributed Database PolarDB- |
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

##### 1.1.6.15 DescribeStorageInstanceSubDbInfo

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

| .0) |   |   | PolarDB- |
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

```json
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
    "successResponse":true,
    "requestId":"78BA6289-5E03-4A31-8CB8-FC298DB63184",
    "data":{
        "Data":{
            "WarningLevel":0,
            "TipsType":0,
            "RdsInstanceId":"rm-bp1xxxxxxxxxxxxxxx",
            "SubDbList":{
                "SubDb":[
                        "WarningLevel":0,
                        "SubDbName":"drds_flashback_b8cd_0005",
```

```json
                        "Use":0
```

`},`

```json
                        "WarningLevel":0,
                        "SubDbName":"drds_flashback_b8cd_0004",
                        "Use":0
```

`},`

```json
                        "WarningLevel":0,
                        "SubDbName":"drds_flashback_b8cd_0003",
                        "Use":0
```

`},`

```json
                        "WarningLevel":0,
                        "SubDbName":"drds_flashback_b8cd_0002",
                        "Use":0
```

`},`

```json
                        "WarningLevel":0,
                        "SubDbName":"drds_flashback_b8cd_0007",
                        "Use":0
```

`},`

```json
                        "WarningLevel":0,
                        "SubDbName":"drds_flashback_b8cd_0006",
                        "Use":0
```

`},`

```json
                        "WarningLevel":0,
                        "SubDbName":"drds_flashback_b8cd_0001",
                        "Use":0
```

`},`

```json
                        "WarningLevel":0,
                        "SubDbName":"drds_flashback_b8cd_0000",
                        "Use":0
```

`},`

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

##### 1.1.6.16 EnableSqlAudit

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

```json
http(s)://[Endpoint]/? Action=EnableSqlAudit &DbName=tpch_50g_4c32gx4 &DrdsInstanceId=drdsxxxxxxxxxxxx <EnableSqlAuditResponse>
      <Result>true</Result>
      <RequestId>463A5F0F-12AD-4544-A902-B2B983CD2C11</RequestId>
</EnableSqlAuditResponse>
    "Result":true,
    "RequestId":"463A5F0F-12AD-4544-A902-B2B983CD2C11",
    "Success":true
```

##### 1.1.6.17 EnableSqlFlashbackMatchSwitch

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

```json
<EnableSqlFlashbackMatchSwitchResponse>
      <Result>true</Result>
      <RequestId>463A5F0F-12AD-4544-A902-B2B983CD2C11</RequestId>
</EnableSqlFlashbackMatchSwitchResponse>
    "Result":true,
    "RequestId":"463A5F0F-12AD-4544-A902-B2B983CD2C11",
    "Success":true
```

##### 1.1.6.18 FlashbackRecycleBinTable

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

```json
http(s)://[Endpoint]/? Action=FlashbackRecycleBinTable &DbName=testdb &DrdsInstanceId=drdsxxxxxxxxxxxxxx &TableName=test <FlashbackRecycleBinTableResponse>
      <Result>true</Result>
      <RequestId>463A5F0F-12AD-4544-A902-B2B983CD2C11</RequestId>
</FlashbackRecycleBinTableResponse>
    "Result":true,
    "RequestId":"463A5F0F-12AD-4544-A902-B2B983CD2C11",
    "Success":true
```

##### 1.1.6.19 ModifyAccountDescription

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

```json
    "RequestId":"2F93CCD5-806F-4470-BBC7-20476AC48DC6",
    "Success":true
```

##### 1.1.6.20 ModifyDrdsInstanceDescription

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

```json
http(s)://[Endpoint]/? Action=ModifyDrdsInstanceDescription &Description=Long occupied &DrdsInstanceId=drdsxxxxxxxxxxxxx <ModifyDrdsInstanceDescriptionResponse>
      <RequestId>C44CA24C-C7C4-4C0F-8AC9-1343F279B09C</RequestId>
</ModifyDrdsInstanceDescriptionResponse>
    "RequestId":"C44CA24C-C7C4-4C0F-8AC9-1343F279B09C",
    "Success":true
```

##### 1.1.6.21 RemoveDrdsInstance

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

```json
http(s)://[Endpoint]/? Action=RemoveDrdsInstance &DrdsInstanceId=drdsxxxxxxxxxxxxx <RemoveDrdsInstanceResponse>
      <RequestId>A3140FC7-B78B-4D8E-B0C8-926D28669934</RequestId>
</RemoveDrdsInstanceResponse>
    "RequestId":"A3140FC7-B78B-4D8E-B0C8-926D28669934",
    "Success":true
```

##### 1.1.6.22 RemoveInstanceAccount

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

```json
http(s)://[Endpoint]/? Action=RemoveInstanceAccount &AccountName=testaccount &DrdsInstanceId=drdsxxxxxxxxxxxxx <RemoveInstanceAccountResponse>
      <RequestId>A3140FC7-B78B-4D8E-B0C8-926D28669934</RequestId>
</RemoveInstanceAccountResponse>
    "RequestId":"A3140FC7-B78B-4D8E-B0C8-926D28669934",
    "Success":true
```

##### 1.1.6.23 RestartDrdsInstance

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

```json
<RestartDrdsInstanceResponse>
      <RequestId>A3140FC7-B78B-4D8E-B0C8-926D28669934</RequestId>
      <TaskId>1</TaskId>
</RestartDrdsInstanceResponse>
    "RequestId":"A3140FC7-B78B-4D8E-B0C8-926D28669934",
    "TaskId":1,
    "Success":true
```

##### 1.1.6.24 RollbackInstanceVersion

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

```json
http(s)://[Endpoint]/? Action=RollbackInstanceVersion &DrdsInstanceId=drdsxxxxxxxxxxx <RollbackInstanceVersionResponse>
      <RequestId>DSSDF-SEWE-23ERW</RequestId>
      <Data>True</Data>
</RollbackInstanceVersionResponse>
    "Data":"true",
    "RequestId":"DSSDF-SEWE-23ERW"
```

##### 1.1.6.25 SetBackupPolicy

Configures a backup policy for a PolarDB-X instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetBackupPolicy | The operation that you want to perform. Set the value to SetBackupPolicy. |
| DrdsInstanceId | String | Yes | drdsxxxxxxxxxxx | The ID of the PolarDB-X 1.0 instance. |
| AccessKeyId | String | No | fafdsxxxxxxxxxxx | The AccessKey ID provided to you by Alibaba Cloud. |
| BackupDbNames | String | No | db test1,db test2 _ _ | The name of the database involved in the backup. |

| eveloper Guide·Deve | loper Guide ( |   | Cloud Native | Distributed Database |
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

```json
http(s)://[Endpoint]/? Action=SetBackupPolicy &DrdsInstanceId=drdsxxxxxxxxxxx <SetBackupPolicyResponse>
        <RequestId>A3140FC7-B78B-4D8E-B0C8-926D28669934</RequestId>
        <Result>success</Result>
</SetBackupPolicyResponse>
    "Result":"success",
    "RequestId":"A3140FC7-B78B-4D8E-B0C8-926D28669934",
    "Success":true
```

##### 1.1.6.26 SetupDrdsParams

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

| loud Native Distribute olarDB-X | d Database |   | Developer G | uide·Developer Guide 1.0 |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Data.N.ParamVaria bleName | String | No | FORBID EXECUTE D _ _ ML ALL _ | The name of the variable, which is specific to the program. |
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |

```json
http(s)://[Endpoint]/? Action=SetupDrdsParams &DrdsInstanceId=drdsxxxxxxxxxxx &ParamLevel=DB <SetupDrdsParamsResponse>
        <RequestId>A3140FC7-B78B-4D8E-B0C8-926D28669934</RequestId>
        <Data>true</Data>
</SetupDrdsParamsResponse>
    "Data":true,
    "RequestId":"A3140FC7-B78B-4D8E-B0C8-926D28669934",
    "Success":true
```

##### 1.1.6.27 SubmitRollbackTask

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

```json
http(s)://[Endpoint]/? Action=SubmitRollbackTask &DbName=test &DrdsInstanceId=drdsxxxxxxxxxx &ExpandType=smooth_expand &JobId=123 &ParentJobId=123 <SubmitRollbackTaskResponse>
      <RequestId>DSSDF-SEWE-23ERW</RequestId>
</SubmitRollbackTaskResponse>
    "RequestId":"DSSDF-SEWE-23ERW",
    "Success":true
```

##### 1.1.6.28 SubmitSqlFlashbackTask

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

| loud Native Distribute olarDB-X | d Database |   | Developer G | uide·Developer Guide 1.0 |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SqlType | String | No | INSERT,UPDATE | The type of the SQL statement. Valid values: INSERT, UPDATE, and DELETE. Separate multiple values with comma (,). |
| TableName | String | No | tb1 | The name of the table on which you want to perform SQL flashback. |
| TraceId | String | No | asenw3sa | The trace ID of the flashback SQL statement. You can query it in the PolarDB-X 1.0 SQL audit results. |

```json
http(s)://[Endpoint]/? Action=SubmitSqlFlashbackTask &DbName=testdb &DrdsInstanceId=drdsxxxxxxxxxx &EndTime=2019-09-10 23:23:23 &RecallRestoreType=0 &StartTime=2019-09-10 20:23:23 <SubmitSqlFlashbackTaskResponse>
      <RequestId>DSSDF-SEWE-23ERW</RequestId>
      <TaskId>2323</TaskId>
</SubmitSqlFlashbackTaskResponse>
    "RequestId":"DSSDF-SEWE-23ERW",
    "TaskId":2323,
    "Success":true
```

##### 1.1.6.29 SwitchGlobalBroadcastType

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

```json
http(s)://[Endpoint]/? Action=SwitchGlobalBroadcastType &DbName=testdb &DrdsInstanceId=drdsxxxxxxxxx <ValidateShardTaskResponse>
     <RequestId>DSSDF-SEWE-23ERW</RequestId>
     <Data>true</Data>
</ValidateShardTaskResponse>
    "Data":true,
    "RequestId":"DSSDF-SEWE-23ERW",
    "success":true
```

##### 1.1.6.30 UpgradeInstanceVersion

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

```json
http(s)://[Endpoint]/? Action=UpgradeInstanceVersion &DrdsInstanceId=drdsxxxxxxxxxx <UpgradeInstanceVersionResponse>
      <RequestId>DSSDF-SEWE-23ERW</RequestId>
      <Data>True</Data>
</UpgradeInstanceVersionResponse>
    "Data":"true",
    "RequestId":"DSSDF-SEWE-23ERW"
```

### 1.2 Call SDKs for cloud services by using ASAPI

using ASAPI

#### 1.2.1 Overview

This topic describes the architecture and features of Apsara Stack API (ASAPI). ASAPI is a platform that integrates all features and is the only portal to connect to Apsara Stack. ASAPI can categorize, audit, and manage API operations. It can also assemble and customize existing operations and adapt to your operations. Each cloud service can call ASAPI for required data and features, which avoids inconsistent operations caused by different calling methods and separate encapsulation. This can ensure the operation program integrity and improve development efficiency and code portability. ASAPI allows you to manage and call operations in a centralized manner and customize development. ASAPI supports access to most cloud services deployed in Apsara Stack and supports passthrough or encapsulation of different backend APIs. This way, operations can be called using the same method. ASAPI allows you to use SDKs and API portals to call APIs registered on ASAPI, customize SDKs, and manage versions of Apsara Stack, services, and APIs.

#### 1.2.2 Log on to the API Tool console

You can log on to the API Tool console through the Apsara Stack Cloud Management (ASCM) console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. In the top navigation bar, choose Product s > Ot hers > API T ool.

#### 1.2.3 View the information about API operations

You must obtain a service name, API operation name, and API version. All the information is required when you use SDKs. Procedure
1. Log on to the API Tool console.
2. In the left-side navigation pane, click API f old.
3. On the API Direct ory page, select the target service from the drop-down list, enter the API
operation name in the search box, and then click the search icon.
4. View and remember the service name, API operation name, and API version.

#### 1.2.4 Obtain the endpoint of ASAPI

This topic describes how to obtain the endpoint of ASAPI in the Apsara Stack Operations console. Procedure
1. In the address bar, enter the URL region-id.aso.intranet-domain-id.com and press the Enter key.
Not e You can select a language from the drop-down list in the upper-right corner of the page.
2. Enter your username and password.
Not e Obtain the username and password for logging on to the ASO console from the deployment personnel or an administrator. When you log on to the ASO console for the first time, you must change the password of your username as prompted. To enhance security, a password must meet the following requirements: It must contain uppercase and lowercase letters. It must contain digits. It must contain special characters such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%). It must be 10 to 20 characters in length.
3. Click Log On to go to the ASO console.
4. In the left-side navigation pane, choose Product s > Product List > Apsara Inf rast ruct ure
Management Framework to go to the Apsara Infrastructure Management Framework console.
5. In the left-side navigation pane of the Apsara Infrastructure Management Framework console, click
Report s.
6. On the All Report s page, search for Regist rat ion Vars of Services. Click Regist rat ion Vars of
Services.
7. On the Regist rat ion Vars of Services page, move the pointer over Service and click the
icon next to it. In the dialog box that appears, search for asapi.
8. Right-click the Service Regist rat ion column corresponding to ASAPI and select Show More.
9. In the Det ails dialog box, the value of asapi.gat eway.endpoint is the logon URL of the Apsara
ASAPI Management platform.

#### 1.2.5 Obtain the core package for ASAPI

Apsara Stack uses Apsara Stack API (ASAPI) as a unified portal for all Apsara Stack products that are connected to ASAPI. ASAPI also provides SDKs to call product APIs. For more information about how to obtain the core package for ASAPI, see Apsara Stack documentation.

#### 1.2.6 Obtain an AccessKey pair

An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey pair is used to implement symmetric encryption to verify the identity of the requester. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. This topic describes how to obtain the AccessKey pair of an organization. Prerequisites Only operations administrators and level-1 organization administrators can obtain the AccessKey pair of an organization. Obtain the AccessKey pair of an organization To obtain the AccessKey pair of an organization, perform the following operations:
1. Log on to the Apsara Stack Cloud Management (ASCM) console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane of the Ent erprise page, click Organizat ions.
4. In the Organizations navigation tree, click the
icon on the right of the organization to be added.
5. Select AccessKey.
6. In the message that appears, view the AccessKey pair of the organization.
Not e An AccessKey pair is automatically allocated to a level-1 organization. Subordinate organizations use the same AccessKey pair as their level-1 organization. Obtain the AccessKey pair of a personal account To obtain the AccessKey pair of a personal account, perform the following operations:
1. Log on to the ASCM console as an administrator.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and click User
Inf ormat ion.
3. In the Apsara St ack AccessKey Pair section of the User Information page, view your AccessKey
pair. Not e The AccessKey pair consists of an AccessKey ID and an AccessKey secret. They allow you to access Apsara Stack resources with full permissions for your account. You must keep them confidential.

#### 1.2.7 Query the region ID

You must specify the region ID when you call Apsara Stack SDK for Node.js. You must query the region ID in the Apsara Stack Cloud Management (ASCM) console. Procedure
1. Log on to the ASCM console as an administrator.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and click User
Inf ormat ion.
3. In the Apsara St ack AccessKey Pair section, you can view the region ID.

#### 1.2.8 Call PolarDB-X SDK for Java

This topic describes how to obtain and use Cloud Native Distributed Database PolarDB-X (PolarDB-X) SDK for Java. Prerequisites You must have an Apsara Stack tenant account and an AccessKey pair (AccessKey ID and AccessKey secret) to use PolarDB-X SDK for Java. For more information about how to obtain and view your AccessKey pair in the Apsara Stack Cloud Management (ASCM) console, see Obtain an AccessKey pair. You have obtained the endpoint of Apsara Stack API (ASAPI). For more information, see Obtain the endpoint of Asapi. The version of PolarDB-X SDK for Java is 1.6 or later. Add the dependency Add the following dependency to pom.xml:

```xml
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>asapi</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <scope>system</scope>
    <systemPath>${project.basedir}/lib/aliyun-java-sdk-asapi.jar</systemPath>
</dependency>
```

Use SDK for Java You can call ASAPI API operations by sending GET and POST requests. GET request

```
 ASClient client = new ASClient();
// Form 1 String result = client.doGet(endpoint, parameters); // Form 2 String result = client.doRequest(endpoint, parameters);
```

POST request

```
// Set the endpoint of ASAPI. String endpoint = "http://xxx/asapi/v3"; // Set request parameters. Map<String, String> parameters = new HashMap<String, String>(); // Set product parameters. parameters.put("Product", "ascm"); // The product name, which must be the same as that displayed on the APIs page. parameters.put("Action", "AddUser"); // The API operation, which is case-sensiti ve and must be the same as that on the APIs page. parameters.put("Version", "2019-05-10"); // The API version. // Set authorization parameters. parameters.put("AccessKeyId", "<your-access-key-id>"); // The AccessKey ID of th e authorized account. parameters.put("AccessKeySecret", "<your-access-key-secret>"); // The AccessKey secret o f the authorized account. // Set service parameters. parameters.put("username", "<your-username>"); // The username used to l og on to the ASCM console parameters.put("password", "<your-password>"); // The password used to l og on to the ASCM console JSONObject jsonObject = new JSONObject(); jsonObject.put("param1", "json parameter 1"); jsonObject.put("param2", "json parameter 2"); parameters.put("json", jsonObject.toJSONString()); // Create an ASClient instance for initiating requests. ASClient client = new ASClient(); // Add the request header. client.addHeader("x-acs-resourceGroupId", "112233"); // Initiate the request and obtain the response. String result = client.doPost(endpoint, parameters);
```

#### 1.2.9 Call PolarDB-X SDK for Node.js

This topic describes how to obtain and use Cloud Native Distributed Database PolarDB-X (PolarDB-X) SDK for Node.js. Prerequisites You must have an Apsara Stack tenant account and an AccessKey pair (AccessKey ID and AccessKey secret) to use PolarDB-X SDK for Node.js. For more information, see Obtain an AccessKey pair. You have obtained the endpoint of Apsara Stack API (ASAPI). For more information, see Obtain the endpoint of Asapi. You have obtained the region ID. For more information, see Query the region ID. Add the dependency
1. Install SDK for Node.js.

```
 tnpm install --save @ali/asapi-nodejs-sdk
```

2. If mocha.opts depends on Egg.js, configure mocha.opts as follows:

```
--recursive --colors --timeout 60000 --reporter mochawesome --require co-mocha --require egg-ts-helper/register --require espower-typescript/guess --require intelli-espower-loader
```

Use SDK for Node.js The following example shows the three main steps of calling SDK for Node.js:
1. Create an ASClient instance. When you create an ASClient instance, set the region ID, endpoint,
AccessKey ID, and AccessKey secret in the config.ts file. See the following example:

```
local: {
    regionId: the region ID.
    API_GATEWAY: the endpoint of ASAPI.
    accessKeyId: the AccessKey ID.
    accessKeySecret: the AccessKey secret.
```

`},`
2. Create an API request and configure parameters.
3. Initiate the API request and handle the response or exception.

```
// Set the endpoint of ASAPI. const API_GATEWAY = "http://xxxx/asapi/v3" // Create an RPC client. const asapiClient = ctx.service.sdk.rpcClient; // Set parameters. let params = {
    Action: 'DescribeDrdsDbInstances',
    Product: 'PolarDB-X',
    regionId: 'cn-qingdao-env12-d01',
    accessKeyId: 'xxxxxxx',
    accessKeySecret: 'xxxxxxx',
    Version: '2019-01-23',
```

};

```
// Set parameters in the request header. asapiClient.addHeader("x-acs-regionId", "cn-qingdao-env12-d01"); // Initiate the request and obtain the response. const result = await asapiClient.doRequest(API_GATEWAY, params, {});
```

1.2.10. (Optional) Use POP SDK to call ASAPI API operations If an application used POP SDK to call Cloud Native Distributed Database PolarDB-X (PolarDB-X), you must switch the gateway to Apsara Stack API (ASAPI). Procedure
1. Switch the gateway to ASAPI and add common parameters required by the API operation to the
request header, so the API operation can be called in a transparent manner.
2. Add the Product field to the request header.
The following code is an example of calling a PolarDB-X API operation.

```java
        try {
            DescribeDrdsDbInstancesResponse response = client.getAcsResponse(request);
            System.out.println(new Gson().toJson(response));
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            System.out.println("ErrCode:" + e.getErrCode());
            System.out.println("ErrMsg:" + e.getErrMsg());
            System.out.println("RequestId:" + e.getRequestId());
```
