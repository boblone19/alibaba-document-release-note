---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 ApsaraDB for MongoDB Developer Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 64
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 ApsaraDB for MongoDB Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E6%95%B0%E6%8D%AE%E5%BA%93/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20ApsaraDB%20for%20MongoDB%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 ApsaraDB for MongoDB Developer Guide 20220928

## Table of Contents

- 1 Developer Guide
  - 1.1 API reference
    - 1.1.1 List of operations by function
      - 1.1.1.1 Lifecycle management
      - 1.1.1.2 Instance management
      - 1.1.1.3 Account management
      - 1.1.1.4 Database security management
      - 1.1.1.5 Backup and restoration management
      - 1.1.1.6 Monitoring alert management
    - 1.1.2 Make API requests
      - 1.1.2.1 Request structure
      - 1.1.2.2 Common parameters
        - 1.1.2.2.1 Common request parameters
        - 1.1.2.2.2 Common response parameters
          - 1.1.2.2.2.1 Responses
      - 1.1.2.3 Sign signatures
    - 1.1.3 Lifecycle management
      - 1.1.3.1 CreateDBInstance
        - 1.1.3.1.1 Description
        - 1.1.3.1.2 Request parameters
        - 1.1.3.1.3 Response parameters
      - 1.1.3.2 ModifyDBInstanceSpec
        - 1.1.3.2.1 Description
        - 1.1.3.2.2 Request parameters
        - 1.1.3.2.3 Response parameters
      - 1.1.3.3 DeleteDBInstance
        - 1.1.3.3.1 Description
        - 1.1.3.3.2 Request parameters
        - 1.1.3.3.3 Response parameters
      - 1.1.3.4 RenewDBInstance
        - 1.1.3.4.1 Description
        - 1.1.3.4.2 Request parameters
        - 1.1.3.4.3 Response parameters
    - 1.1.4 Instance management
      - 1.1.4.1 DescribeRegions
        - 1.1.4.1.1 Description
        - 1.1.4.1.2 Request parameters
        - 1.1.4.1.3 Response parameters
          - 1.1.4.1.3.1 Region data structure
          - 1.1.4.1.3.2 Zones
      - 1.1.4.2 DescribeDBInstances
        - 1.1.4.2.1 Description
        - 1.1.4.2.2 Request parameters
        - 1.1.4.2.3 Response parameters
          - 1.1.4.2.3.1 DBInstance data structure
          - 1.1.4.2.3.2 Mongos
          - 1.1.4.2.3.3 Shard
      - 1.1.4.3 RestartDBInstance
        - 1.1.4.3.1 Description
        - 1.1.4.3.2 Request parameters
        - 1.1.4.3.3 Response parameters
      - 1.1.4.4 ModifyDBInstanceMaintainTime
        - 1.1.4.4.1 Description
        - 1.1.4.4.2 Request parameters
        - 1.1.4.4.3 Response parameters
      - 1.1.4.5 ModifyDBInstanceDescription
        - 1.1.4.5.1 Description
        - 1.1.4.5.2 Request parameters
        - 1.1.4.5.3 Response parameters
      - 1.1.4.6 DescribeInstanceAttribute
        - 1.1.4.6.1 Description
        - 1.1.4.6.2 Request parameters
        - 1.1.4.6.3 Response parameters
          - 1.1.4.6.3.1 DBInstance parameters
      - 1.1.4.7 DescribeReplicaSetRole
        - 1.1.4.7.1 Description
        - 1.1.4.7.2 Request parameters
        - 1.1.4.7.3 Response parameters
          - 1.1.4.7.3.1 ReplicaSetRole data structure
      - 1.1.4.8 ModifyDBInstanceNetworkType
        - 1.1.4.8.1 Description
        - 1.1.4.8.2 Request parameters
        - 1.1.4.8.3 Response parameters
      - 1.1.4.9 ModifyDBInstanceNetExpireTime
        - 1.1.4.9.1 Description
        - 1.1.4.9.2 Request parameters
        - 1.1.4.9.3 Response parameters
    - 1.1.5 Account management
      - 1.1.5.1 ResetAccountPassword
        - 1.1.5.1.1 Description
        - 1.1.5.1.2 Request parameters
        - 1.1.5.1.3 Response parameters
      - 1.1.5.2 DescribeAccounts
        - 1.1.5.2.1 Description
        - 1.1.5.2.2 Request parameters
        - 1.1.5.2.3 Response parameters
          - 1.1.5.2.3.1 Account data structure
      - 1.1.5.3 ModifyAccountDescription
        - 1.1.5.3.1 Description
        - 1.1.5.3.2 Request parameters
        - 1.1.5.3.3 Response parameters
    - 1.1.6 Database security management
      - 1.1.6.1 DescribeSecurityIps
        - 1.1.6.1.1 Description
        - 1.1.6.1.2 Request parameters
        - 1.1.6.1.3 Response parameters
      - 1.1.6.2 ModifySecurityIps
        - 1.1.6.2.1 Description
        - 1.1.6.2.2 Request parameters
        - 1.1.6.2.3 Response parameters
      - 1.1.6.3 DescribeAuditRecords
        - 1.1.6.3.1 Description
        - 1.1.6.3.2 Request parameters
        - 1.1.6.3.3 Response parameters
      - 1.1.6.4 DescribeAuditFiles
        - 1.1.6.4.1 Description
        - 1.1.6.4.2 Request parameters
        - 1.1.6.4.3 Response parameters
    - 1.1.7 Backup and restoration management
      - 1.1.7.1 DescribeBackupPolicy
        - 1.1.7.1.1 Description
        - 1.1.7.1.2 Request parameters
        - 1.1.7.1.3 Response parameters
      - 1.1.7.2 ModifyBackupPolicy
        - 1.1.7.2.1 Description
        - 1.1.7.2.2 Request parameters
        - 1.1.7.2.3 Response parameters
      - 1.1.7.3 CreateBackup
        - 1.1.7.3.1 Description
        - 1.1.7.3.2 Request parameters
        - 1.1.7.3.3 Response parameters
      - 1.1.7.4 DescribeBackups
        - 1.1.7.4.1 Description
        - 1.1.7.4.2 Request parameters
        - 1.1.7.4.3 Response parameters
      - 1.1.7.5 RestoreDBInstance
        - 1.1.7.5.1 Description
        - 1.1.7.5.2 Request parameters
        - 1.1.7.5.3 Response parameters
    - 1.1.8 Performance monitoring management
      - 1.1.8.1 DescribeDBInstancePerformance
        - 1.1.8.1.1 Description
        - 1.1.8.1.2 Request parameters
        - 1.1.8.1.3 Response parameters
    - 1.1.9 Appendix
      - 1.1.9.1 Error codes
  - 1.2 Call SDKs for cloud services by using ASAPI
    - 1.2.1 Overview
    - 1.2.2 Log on to the API Tool console
    - 1.2.3 View the information about API operations
    - 1.2.4 Obtain the endpoint of ASAPI
    - 1.2.5 Obtain the core package for ASAPI
    - 1.2.6 Obtain an AccessKey pair
    - 1.2.7 Query the region ID
    - 1.2.8 Call PolarDB-X SDK for Java
    - 1.2.9 Call SDK for Node.js
    - 1.2.10. (Optional) Use POP SDK to call ASAPI

## 1 Developer Guide

### 1.1 API reference

#### 1.1.1 List of operations by function

##### 1.1.1.1 Lifecycle management

| API | Description |
|---|---|
| CreateDBInstance | Creates a replica set instance. |
| ModifyDBInstanceSpec | Modifies specifications for a replica set instance. |
| DeleteDBInstance | Releases a replica set instance. |
| RenewDBInstance | Renews a replica set instance. |

##### 1.1.1.2 Instance management

| API | Description |
|---|---|
| DescribeRegions | Queries the list of available regions. |
| DescribeDBInstances | Queries the list of instances. |
| RestartDBInstance | Restarts an instance. |
| ModifyDBInstanceMaintainTime | Modifies the maintenance time of an instance. |
| ModifyDBInstanceDescription | Modifies the description of an instance. |
| DescribeDBInstanceAttribute | Queries the details of an instance. |
| ModifyDBInstanceNetworkType | Modifies the network type of an instance. |
| ModifyDBInstanceNetExpireTime | Prolongs the retention period of the classic network endpoint. |

##### 1.1.1.3 Account management

| Operation | Description |
|---|---|
| DescribeAccounts | Queries accounts. |
| ResetAccountPassword | Resets the password of an account. |

##### 1.1.1.4 Database security management

| API | Description |
|---|---|
| DescribeSecurityIps | Queries the IP address whitelist for an instance. |
| ModifySecurityIps | Modifies the IP address whitelist for an instance. |
| DescribeAuditRecords | Queries audit logs. |
| DescribeAuditFiles | Queries audit log files. |

##### 1.1.1.5 Backup and restoration management

| API | Description |
|---|---|
| DescribeBackupPolicy | Queries a backup policy. |
| ModifyBackupPolicy | Modifies a backup policy. |
| CreateBackup | Creates a backup. |
| DescribeBackups | Queries the list of backups. |
| RestoreDBInstance | Restores a backup set to an instance. |

##### 1.1.1.6 Monitoring alert management

| API | Description |
|---|---|
| DescribeDBInstancePerformance | Queries the instance performance data. |

#### 1.1.2 Make API requests

##### 1.1.2.1 Request structure

Endpoints The service endpoint of ApsaraDB for MongoDB APIs is mongodb.example.com. Protocols You can send requests over HTTP or HTTPS. We recommend that you use HTTPS for enhanced security. Methods The HTTP GET method can be used to send requests. Request parameters must be included in the request URL. Parameters Each request must specify the action to be performed (such as CreateDBInstance) in the Action parameter. Each action must include both the common request parameters that are used for all API requests as well as the specific request parameters of the API being called. Encoding Requests and responses are encoded in UTF-8.

##### 1.1.2.2 Common parameters

Common request parameters must be included in the request of each API.

###### 1.1.2.2.1 Common request parameters

Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Format | String | Yes | The format of the returned data. Valid values: JSON and XML. Default value: XML. |
| Version | String | Yes | The API version, in the format of YYYY-MM-DD. The current version is 2015-12-01. |
| AccessKeyId | String | Yes | The AccessKey ID provided by Alibaba Cloud for you to access services. |
| Signature | String | Yes | The signature result string. For more information about signature calculation methods, see the "Sign signatures" topic. |
| SignatureMethod | String | Yes | The algorithm used to create the request signature. Valid value: HMAC-SHA1. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| Timestamp | String | Yes | The request timestamp. The timestamp uses UTC and complies with the ISO8601 standard. The format is YYYY-MM- DDThh:mm:ssZ. Example: 2016-01- 01T12:00:00Z. |
| SignatureVersion | String | Yes | The signature algorithm version. The current version is 1.0. |
| SignatureNonce | String | Yes | A unique, randomly generated number used to prevent network replay attacks. You must use a different random number for each request. |

Examples

```
https://mongodb.example.com/ ? Format=json &Version=2015-12-01 &Signature=Pc5WBxxxxxxxx &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2016-01-01T12:00:00Z
```

###### 1.1.2.2.2 Common response parameters

The system returns a unique RequestId for each API request, regardless of whether the API operation is successful. Examples

```xml
<? xml version="1.0" encoding="utf-8"? > <!—Result root node--> <API name + response> <!—Returned request tag--> <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId> <!—Response--> </API name + response>
```

###### 1.1.2.2.2.1 Responses

The response data for API requests is displayed in a uniform format. In the response data, HTTP status code 2xx indicates that the API operation is successful. HTTP status code 4xx or 5xx indicates that the API operation fails. The response data for called API operations is returned in either the XML or JSON format. You can add parameters to an API request to specify the format of the response data. Response data uses the XML format by default. The response examples in this topic are formatted with line breaks or indents for a clear view. Actual response data is not formatted in the same manner as these examples. Successful response examples Responses in the XML format include information about whether the operation is successful, and details specific to the operation. Examples:

```xml
<? xml version="1.0" encoding="utf-8"? > <!—Result root node--> <API name + response> <!—Returned request tag--> <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId> <!—Response--> </API name + response>
```

JSON f ormat `{`

```json
"RequestId": "4C4fdsf38-3910-447D-87AD-AC078932216", /* Response */
```

`}` Error response examples If you experience an error when calling APIs, no response data is returned. You can locate the cause of the error on the server by referring to Appendix Error codes. When an error occurs on an HTTP request for an API operation, HTTP status code 4xx or 5xx is returned. The response body contains the error code, the error message, a globally unique request ID (RequestId), and the ID of the site accessed by the request (HostId). You can contact Alibaba Cloud customer service when the cause of the error cannot be found. We recommend that you provide the HostId and RequestId of the request to help us resolve the issue at the earliest opportunity. Examples:

```xml
<? xml version="1.0" encoding="UTF-8"? > <Error> <RequestId>8906582E-6722-409A-A6C4-0E7863B733A5</RequestId> <HostId>mongodb.example.com</HostId> <Code>UnsupportedOperation</Code> <Message>The specified action is not supported. </Message> </Error>
```

JSON f ormat `{`

```json
"RequestId": "7463B73D-35CC-4D19-A010-6B8D65D242EF", "HostId": " mongodb.example.com", "Code": "UnsupportedOperation", "Message": "The specified action is not supported."
```

`}`

##### 1.1.2.3 Sign signatures

ApsaraDB for MongoDB authenticates the sender identity of each request that it receives. Therefore, you must include a signature in HTTP or HTTPS requests. ApsaraDB for MongoDB performs symmetric encryption to verify the request sender's identity by using the AccessKey ID and AccessKey Secret. The AccessKey ID and AccessKey Secret are officially issued to visitors by Alibaba Cloud. Visitors can apply for and manage them on the official Alibaba Cloud website. The AccessKey ID indicates the identity of the visitor. The AccessKey Secret is used by the client to encrypt signature strings and used by the server to verify signature strings. You must keep your AccessKey Secret confidential. Perform the following steps to sign an access request:
1. Use request parameters to construct a canonicalized query string.
i. To construct a canonicalized query string, sort all request parameters by name in alphabetic order. These parameters include common request parameters and customized API request parameters , but do not include the Signature parameter. Not ice If a request is submitted using the GET method, these parameters are placed in the request section after a question mark (?) in the request URI and connected with ampersands (&). ii. Encode the name and value of each request parameter. Perform UTF-8 URL encoding on the names and values of each request parameter. The URL encoding rules are described as follows: Uppercase letters (A–Z), lowercase letters (a–z), digits (0–9), hyphens (-), underscores (_), periods (.), and tildes (~) are not encoded. Extended UTF-8 characters are encoded in the %XY%ZA… format. A space is encoded as %20, rather than the plus sign (+). Not ice Most libraries that support URL encoding, such as java.net.URLEncoder, comply with the MIME encoding rules of application/x-www-form-urlencoded. If this encoding method is used, replace the plus signs (+) in the encoded strings with %20, the asterisks (*) with %2A, and %7E with a tilde (~) to conform to the encoding rules. iii. Connect the encoded parameter names and values with equal signs (=). iv. Sort the equal sign-connected strings by their parameter names alphabetically and connect them with ampersands (&).
2. Use the created canonicalized query string to construct a string for signature calculation based on
the following rules:

```
 StringToSign=
 HTTPMethod + "&" +
 percentEncode("/") + "&" +
 percentEncode(CanonicalizedQueryString)
```

In the preceding example, HTTPMethod indicates the HTTP method that is used to submit a request, such as GET. percentEncode("/") is the encoded value ("%2F") of a forward slash (/). The encoding follows the URL encoding rules described in the previous step. percentEncode(CanonicalizedQueryString) is the string constructed using the canonicalized query string. The encoding follows the URL encoding rules described in the previous step.
3. Use the signature string to calculate the HMAC value of the signature as defined by RFC 2104.
Not ice The key used for signature calculation is your AccessKey Secret with an ampersand (&) added at the end. The corresponding number of an ampersand (&) is 38 in ASCII codes. The string is then hashed with the SHA1 hash algorithm.
4. Encode the HMAC value into a string based on the Base64 encoding rules. This encoded string is the
signature value.
5. Add the signature value as the Signature parameter value to the request parameters to complete
the request signing process. Not ice When the obtained signature value is submitted to the RDS server as the final request parameter value, the value must undergo URL encoding based on RFC 3986 rules like other parameters. DescribeCdnService is used here as an example. The request URL before signing is:

```
http://mongodb.example.com/?Timestamp=2016-01-01T10:33:56Z&Format=XML&AccessKeyId=testi d&Action=DescribeInstances&SignatureMethod=HMAC-SHA1&RegionId=region1&SignatureNonce=Nw DAxvLU6tFE0DVb&Version=2015-12-01&SignatureVersion=1.0
```

The StringToSign placed after the signature is as follows:

```
GET&%2F&AccessKeyId%3Dtestid&Action%3DDescribeInstances&Format%3DXML&RegionId%3Dregion1 &SignatureMethod%3DHMAC-SHA1&SignatureNonce%3DNwDAxvLU6tFE0DVb&SignatureVersion%3D1.0&T imestamp%3D2013-06-01T10%253A33%253A56Z&Version%3D2015-01-01
```

Assume that the AccessKey ID is testid, the AccessKey Secret is testsecret, and the Key used for HMAC calculation is testsecret&. The calculated signature value is as follows: BIPOMlu8LXBeZtLQkJTw6iFvw1E= The signed request URL with the Signature parameter added is as follows:

```
 http://mongodb.example.com/?TimeStamp=2016-01-01T10%3A33%3A56Z&Format=XML&AccessKeyId=
testid&Action=DescribeInstances&SignatureMethod=HMAC-SHA1&RegionId=region1&SignatureNon ce=NwDAxvLU6tFE0DVb&SignatureVersion=1.0&Version=2015-12-01&Signature=Pc5WBxxxxxxxx
```

#### 1.1.3 Lifecycle management

##### 1.1.3.1 CreateDBInstance

###### 1.1.3.1.1 Description

This API supports both data restoration and instance clone functions.

###### 1.1.3.1.2 Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateDBInstance. |
| RegionId | String | Yes | The region ID of the instance. It can be up to 50 characters in length. You can call the DescribeRegions operation to query the latest region list. |
| ZoneId | String | No | The zone ID of the instance. You can call the DescribeRegions operation to query the latest zone list. |
| Engine | String | Yes | The type of the database. Set the value to MongoDB. |
| EngineVersi on | String | Yes | The version of the database. Set the value to 3.2. |
| StorageEngi ne | String | No | The storage engine. Valid values: WiredTiger and RocksDB. Default value: WiredTiger. |
| DBInstanceC lass | String | Yes | The specifications of the instance. For more information, see Instance specifications. |
| DBInstanceS torage | Integer | Yes | The custom storage space. Valid values: 5 to 1000 for ApsaraDB for MongoDB instances. You can only specify this value in 5 GB increments. Unit: GB. |
| DBInstanceD escription | String | No | The description of the instance. This parameter must be 2 to 256 characters in length. It must start with a letter and can contain letters, digits, underscores ( ), and hyphens (-). _ |
| SecurityIPLis t | String | No | The IP addresses in an IP address whitelist. Separate multiple IP addresses with commas (,). You can add a maximum of 1,000 different IP addresses to a whitelist. Supported formats of IP addresses are IP addresses such as %, 0.0.0.0/0 and 10.23.12.24 or Classless Inter-Domain Routing (CIDR) blocks such as 10.23.12.24/24. /24 indicates the length of the IP address prefix. The IP address prefix can consist of 1 to 32 bits. 0.0.0.0/0 indicates that all IP addresses are allowed. Default value: 0.0.0.0/0. |
| AccountPas sword | String | No | The password of the root account. The password must be 6 to 32 characters in length and can contain letters, digits, and underscores ( ). _ |

| Parameter | Type | Required | Description |
|---|---|---|---|
| ChargeType | String | No | The billing method of the instance. Valid values: PrePaid and PostPaid. PrePaid: subscription. PostPaid: pay-as-you-go. Default value: PostPaid. |
| Period | Integer | No | The expiration time of a subscription instance. This parameter must be specified when ChargeType is set to PrePaid. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, and 36. Unit: month. |
| ClientToken | String | Yes | The client token that is used to ensure idempotence of the request. The value of this parameter is generated by the client and is unique among different requests. The maximum length is 64 ASCII characters. For more information, see How to ensure idempotence. |
| NetworkTyp e | String | No | The network type of the instance. Valid values: Classic and VPC. Default value: Classic. |
| VpcId | String | No | The ID of the VPC. If NetworkType is set to VPC, this parameter is required. |
| VSwitchId | String | No | The ID of the VSwitch. If NetworkType is set to VPC, this parameter is required. |
| DBInstanceI d | String | No | The ID of the source instance. This parameter can only be specified when this operation is called to clone instances. |
| BackupId | String | No | The ID of the specified backup set. |
| RestoreTim e | String | No | The time when the cloned instance is restored. |

###### 1.1.3.1.3 Response parameters

| Parameter | Type | Description |
|---|---|---|
| Common response parameters | - | For more information, see the "Common response parameters" topic. |
| DBInstanceId | String | The ID of the instance to be queried. |
| OrderId | String | The ID of an order. |

##### 1.1.3.2 ModifyDBInstanceSpec

###### 1.1.3.2.1 Description

###### 1.1.3.2.2 Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceSpec. |
| DBInstanceId | String | Yes | The ID of the instance whose configuration is to be modified. |
| DBInstanceClass | String | No | The specifications of the instance. For more information, see Appendix Instance specifications. |
| OrderType | String | No | The type of the configuration change. Valid values: UPGRADE and DOWNGRADE. Default value: DOWNGRADE. This parameter is applicable to subscription instances only. |
| DBInstanceStorage | Integer | No | The storage capacity of the instance. Valid values: 5 to 1,000. Unit: GB. The value can be increased in increments of 5 GB. |

###### 1.1.3.2.3 Response parameters

| Parameter | Type | Description |
|---|---|---|
| Common response parameters | - | For more information, see the "Common response parameters" topic. |
| OrderId | String | The ID of an order. |

##### 1.1.3.3 DeleteDBInstance

###### 1.1.3.3.1 Description

###### 1.1.3.3.2 Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteDBInstance. |
| DBInstanceId | String | Yes | The ID of the instance to be deleted. |

###### 1.1.3.3.3 Response parameters

| Parameter | Type | Description |
|---|---|---|
| Common response parameters | - | For more information, see the "Common response parameters" topic. |

##### 1.1.3.4 RenewDBInstance

###### 1.1.3.4.1 Description

This API supports replica set instances only.

###### 1.1.3.4.2 Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to RenewDBInstance. |
| DBInstanceId | String | Yes | The ID of the instance to be renewed. |
| Period | Integer | Yes | The renewal period of the instance. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, and 36. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| ClientToken | String | Yes | The token used to guarantee the idempotence of requests. |

###### 1.1.3.4.3 Response parameters

| Parameter | Type | Description |
|---|---|---|
| Common response parameters | - | For more information, see the "Common response parameters" topic. |
| OrderId | String | The ID of an order. |

#### 1.1.4 Instance management

##### 1.1.4.1 DescribeRegions

###### 1.1.4.1.1 Description

This API supports replica set instances only.

###### 1.1.4.1.2 Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeRegions. |
| RegionId | String | No | The ID of the region to be queried. |
| ZoneId | String | No | The ID of the zone in the target region. |

###### 1.1.4.1.3 Response parameters

| Parameter | Type | Description |
|---|---|---|
| Common response parameters | - | For more information, see the "Common response parameters" topic. |

###### 1.1.4.1.3.1 Region data structure

| Parameter | Type | Description |
|---|---|---|
| RegionId | String | The ID of the region where an instance resides, such as cn- beijing. |
| Zones | List<Zones> | The list of zones. |

###### 1.1.4.1.3.2 Zones

| Parameter | Type | Description |
|---|---|---|
| ZoneId | String | The ID of the zone, such as cn- beijing-a. |
| VpcEnabled | String | Indicates whether the VPC is available. |

##### 1.1.4.2 DescribeDBInstances

###### 1.1.4.2.1 Description

This API supports replica set instances only.

###### 1.1.4.2.2 Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDBInstances. |
| RegionId | String | Yes | The ID of the region where an instance resides. You can use the DescribeRegions function to view available regions. |
| Engine | String | No | The database type of the instance. Valid value: MongoDB. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| DBInstanceType | String | No | The queried instance type. Valid values: sharding and replicate. Default value: replicate. |
| PageSize | Integer | No | The number of records on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNumber | Integer | No | The page number to request, which must be any integer greater than 0. Default value: 1. |

###### 1.1.4.2.3 Response parameters

| Parameter | Type | Description |
|---|---|---|
| Common response parameters | - | For more information, see the "Common response parameters" topic. |
| DBInstances | List<DBInstance> | The array consisting of ApsaraDB for MongoDB instances. |

###### 1.1.4.2.3.1 DBInstance data structure

| Parameter | Type | Description |
|---|---|---|
| DBInstanceId | String | The ID of the instance. |
| DBInstanceDescription | String | The description of the instance. |
| RegionId | String | The region ID of the instance. |
| ZoneId | String | The zone ID of the instance. |
| Engine | String | The database type of the instance. |
| EngineVersion | String | The database version of the instance. |
| DBInstanceClass | String | The specifications of the instance. |
| DBInstanceStorage | Integer | The storage capacity of the instance. |

| psaraDB for MongoDB |   | Developer Guide·Developer Guid |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| DBInstanceStatus | String | The status of the instance. For more information, see Instance states. |
| ChargeType | String | The billing method of the instance. Valid values: PrePaid and PostPaid. PrePaid: subscription. PostPaid: pay-as- you-go. |
| NetworkType | String | The network type of the instance. Valid values: Classic and VPC. |
| CreationTime | String | The time when the instance was created. The time is in the yyyy- MM-ddTHH:mm:ssZ format and displayed in UTC. |
| ExpireTime | String | The time that the instance is scheduled to expire. |
| DBInstanceType | String | The instance type. Valid values: sharding and replicate. |
| MongosList | List<Mongos> | The array that consists of mongos nodes. |
| ShardList | List<Shard> | The array that consists of shard nodes. |
| LastDowngradeTime | Integer | The time of the last configuration downgrade. |

###### 1.1.4.2.3.2 Mongos

| Parameter | Type | Description |
|---|---|---|
| NodeId | String | The ID of a mongos node. |
| NodeDescription | String | The description of the mongos node. |
| NodeClass | String | The specifications of the mongos node. |

###### 1.1.4.2.3.3 Shard

| Parameter | Type | Description |
|---|---|---|
| NodeId | String | The ID of a shard node. |
| NodeDescription | String | The description of the shard node. |
| NodeClass | String | The specifications of the shard node. |
| NodeStorage | Integer | The storage capacity of the shard node. |

##### 1.1.4.3 RestartDBInstance

###### 1.1.4.3.1 Description

This API supports replica set instances only.

###### 1.1.4.3.2 Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to RestartDBInstance. |
| DBInstanceId | String | Yes | The ID of the instance to be restarted. |

###### 1.1.4.3.3 Response parameters

| Parameter | Type | Description |
|---|---|---|
| Common response parameters | - | For more information, see the "Common response parameters" topic. |

##### 1.1.4.4 ModifyDBInstanceMaintainTime

###### 1.1.4.4.1 Description

This API supports replica set instances only.

###### 1.1.4.4.2 Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceMainta inTime. |
| DBInstanceId | String | Yes | The ID of the instance for which to modify maintenance time. |
| StartTime | String | Yes | The start time of the maintenance period. |
| EndTime | String | Yes | The end time of the maintenance period. |

###### 1.1.4.4.3 Response parameters

| Parameter | Type | Description |
|---|---|---|
| Common response parameters | - | For more information, see the "Common response parameters" topic. |

##### 1.1.4.5 ModifyDBInstanceDescription

###### 1.1.4.5.1 Description

This API supports replica set instances only.

###### 1.1.4.5.2 Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to ModifyDBInstanceDescri ption. |
| DBInstanceId | String | Yes | The name of the instance. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| DBInstanceDescription | String | Yes | The description of the instance. The description cannot start with http:// or https://. It must start with a letter. It must be 2 to 256 characters in length and can contain letters, underscores ( ), hyphens (-), and _ digits. |

###### 1.1.4.5.3 Response parameters

| Parameter | Type | Description |
|---|---|---|
| Common response parameters | - | For more information, see the "Common response parameters" topic. |

##### 1.1.4.6 DescribeInstanceAttribute

###### 1.1.4.6.1 Description

This API supports replica set instances only.

###### 1.1.4.6.2 Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDBInstanceAttri bute. |
| DBInstanceId | String | Yes | The ID of one or more instances to be queried. You can enter a maximum of 30 IDs at a time. Separate multiple IDs by using commas (,). |

###### 1.1.4.6.3 Response parameters

###### 1.1.4.6.3.1 DBInstance parameters

| Parameter | Type | Description |
|---|---|---|
| DBInstanceId | String | The ID of the instance to be queried. |
| DBInstanceDescription | String | The description of the instance. |
| RegionId | String | The ID of the region where the instance resides. |
| ZoneId | String | The ID of the zone to which the instance belongs. |
| Engine | String | The database type of the instance. |
| EngineVersion | String | The database version of the instance. |
| DBInstanceClass | String | The specifications of the instance. |
| DBInstanceStorage | String | The storage capacity of the instance. |
| DBInstanceStatus | String | The status of the instance. For more information, see Appendix Instance statuses. |
| ChargeType | String | The billing method of the instance. Valid values: PrePaid and PostPaid. |
| ReplicaSetName | String | The name of the replica set for the instance. |
| CreationTime | String | The time when the instance is created. |
| ExpireTime | String | The time that the instance is scheduled to expire. Pay-As-You- Go instances never expire. |
| MaintainStartTime | String | The start time of instance maintenance. |
| MaintainEndTime | String | The end time of instance maintenance. |
| NetworkType | String | The network type of the instance. Valid values: Classic and VPC. |

| eveloper Guide·Developer Guide |   | ApsaraDB for MongoD |
|---|---|---|
| Parameter | Type | Description |
| DBInstanceType | String | The instance type. Valid values: sharding and replicate. |
| LastDowngradeTime | Integer | The time of the most recent configuration downgrade. |

##### 1.1.4.7 DescribeReplicaSetRole

###### 1.1.4.7.1 Description

This API supports replica set instances only.

###### 1.1.4.7.2 Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeReplicaSetRole. |
| DBInstanceId | String | Yes | The ID of the instance to be queried. |

###### 1.1.4.7.3 Response parameters

| Parameter | Type | Description |
|---|---|---|
| Common response parameters | - | For more information, see the "Common response parameters" topic. |
| DBInstanceId | String | The ID of the instance to be queried. |
| ReplicaSets | List<ReplicaSet> | The list of replica set roles. |

###### 1.1.4.7.3.1 ReplicaSetRole data structure

| Parameter | Type | Description |
|---|---|---|
| ReplicaSetRole | String | The role of the replica set instance node. Valid values: Primary and Secondary. |

| Parameter | Type | Description |
|---|---|---|
| ConnectionDomain | String | The domain name used to connect the instance. |
| ConnectionPort | String | The port used to connect the instance. |
| ExpiredTime String | String | The remaining duration of the classic network address of the current instance. Unit: seconds. |
| NetworkType | String | The network type of the instance. VPC Classic Public |
| ReplicaSets | List<ReplicaSet> | A list of roles that belong to the replica set instance node. |

##### 1.1.4.8 ModifyDBInstanceNetworkType

###### 1.1.4.8.1 Description

This API supports replica set instances only.

###### 1.1.4.8.2 Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceNetwo rkType. |
| DBInstanceId | String | Yes | The ID of the instance for which you want to modify the network type. |
| RetainClassic | String | No | Indicates whether to retain the classic network endpoint. Valid values: True and False. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| ClassicExpiredDays | Integer | No | The retention period of the classic network endpoint. Unit: day. Maximum value: 180. When RetainClassic is set to True, this parameter must be specified. |
| VpcId | String | No | The ID of the VPC to which the instance belongs. This parameter must be specified if you are changing the network type of an instance from classic network to VPC. |
| VSwitchId | String | No | The ID of the VSwitch. This parameter must be specified if you are changing the network type of an instance from classic network to VPC. |

###### 1.1.4.8.3 Response parameters

| Parameter | Type | Description |
|---|---|---|
| Common response parameters | - | For more information, see the "Common response parameters" topic. |

##### 1.1.4.9 ModifyDBInstanceNetExpireTime

###### 1.1.4.9.1 Description

This API supports replica set instances only.

###### 1.1.4.9.2 Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceNetEx pireTime. |
| DBInstanceId | String | Yes | The ID of the instance for which the endpoint expiration time is to be modified. |
| ConnectionString | String | Yes | The domain name used to connect to the instance. |
| ClassicExpendExpiredDa ys | Integer | Yes | The number of days for which the classic network endpoint is retained. |

###### 1.1.4.9.3 Response parameters

| Parameter | Type | Description |
|---|---|---|
| Common response parameters | - | For more information, see the "Common response parameters" topic. |

#### 1.1.5 Account management

##### 1.1.5.1 ResetAccountPassword

###### 1.1.5.1.1 Description

This API supports replica set instances only.

###### 1.1.5.1.2 Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ResetAccountPassword. |
| DBInstanceId | String | Yes | The ID of the instance. |

| Developer Guide·Developer | Guide |   | ApsaraDB for MongoD |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| AccountName | String | Yes | The name of the account. |
| AccountPassword | String | Yes | The new password. It must be 6 to 32 characters in length and can contain letters, digits, and underscores ( ). _ |

###### 1.1.5.1.3 Response parameters

| Parameter | Type | Description |
|---|---|---|
| Common response parameters | - | For more information, see the "Common response parameters" topic. |

##### 1.1.5.2 DescribeAccounts

###### 1.1.5.2.1 Description

This API supports replica set instances only.

###### 1.1.5.2.2 Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeAccounts. |
| DBInstanceId | String | Yes | The ID of the instance to be queried. |
| AccountName | String | Yes | The name of the account used to access the instance. |

###### 1.1.5.2.3 Response parameters

| Parameter | Type | Description |
|---|---|---|
| Accounts | List<Account> | The array consisting of accounts. |

###### 1.1.5.2.3.1 Account data structure

| Parameter | Type | Description |
|---|---|---|
| DBInstanceId | String | The ID of the instance. |
| AccountName | String | The name of the account. |
| AccountStatus | String | The status of the account. Valid values: Unavailable and Available. |
| AccountDescription | String | The description of the account. |

##### 1.1.5.3 ModifyAccountDescription

###### 1.1.5.3.1 Description

This API supports replica set instances only.

###### 1.1.5.3.2 Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyAccountDescripti on. |
| DBInstanceId | String | Yes | The ID of the instance. |
| AccountName | String | Yes | The name of the account. |
| AccountDescription | String | Yes | The description of the account. The description cannot start with http:// or https://. It must start with a letter. It must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), and _ hyphens (-). |

###### 1.1.5.3.3 Response parameters

| Parameter | Type | Description |
|---|---|---|
| Common response parameters | - | For more information, see the "Common response parameters" topic. |

#### 1.1.6 Database security management

##### 1.1.6.1 DescribeSecurityIps

###### 1.1.6.1.1 Description

This API supports replica set instances only.

###### 1.1.6.1.2 Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSecurityIps. |
| DBInstanceId | String | Yes | The ID of the instance to be queried. |

###### 1.1.6.1.3 Response parameters

Response parameters

| Parameter | Type | Description |
|---|---|---|
| Common response parameters | - | For more information, see Common response parameters. |
| SecurityIps | String | The default whitelist. |
| SecurityIpGroups | List<SecurityIpGroup> | The list of IP address groups. |

SecurityIpGroup parameters

| Parameter | Type | Description |
|---|---|---|
| SecurityIpGroupName | String | The name of the IP whitelist. |

| psaraDB for MongoDB |   | Developer Guide·Developer Guid |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| SecurityIpList | String | The list of IP addresses. |
| SecurityIpAttribute | String | The attribute of the IP whitelist. The default value is an empty string. |

##### 1.1.6.2 ModifySecurityIps

###### 1.1.6.2.1 Description

This API supports replica set instances only.

###### 1.1.6.2.2 Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to ModifySecurityIps. |
| DBInstanceId | String | Yes | The ID of the instance. |
| SecurityIps | String | Yes | The IP addresses in an IP address whitelist. Separate multiple IP addresses with commas (,). You can add a maximum of 1,000 different IP addresses to a whitelist. Supported formats of IP addresses are IP addresses such as 0.0.0.0/0 and 10.23.12.24, or Classless Inter-Domain Routing (CIDR) blocks such as 10.23.12.24/24. /24 indicates the length of the IP address prefix. The IP address prefix can consist of 1 to 32 bits. |
| ModifyMode | String | Yes | The modification mode. Valid values: - Cover, - Add, and - Delete. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| SecurityIpGroupName | String | No | The name of the group to be modified. Default value: default. |
| SecurityIpGroupAttribut e | String | No | The attribute of the IP address group. Default value: null. |

###### 1.1.6.2.3 Response parameters

| Parameter | Type | Description |
|---|---|---|
| Common response parameters | - | For more information, see the "Common response parameters" topic. |

##### 1.1.6.3 DescribeAuditRecords

###### 1.1.6.3.1 Description

This API supports replica set instances only.

###### 1.1.6.3.2 Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeAuditRecords. |
| DBInstanceId | String | Yes | The ID of the instance. |
| NodeId | String | No | The ID of mongos or shard. If this parameter is not specified, no result is returned. You do not need to specify this parameter for nodes of replica set instances. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| StartTime | String | Yes | The beginning of the time range to query. Specify the time in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |
| EndTime | String | Yes | The end of the time range to query. Specify the time in the yyyy- MM-ddTHH:mm:ssZ format. The time must be in UTC. |
| Database | String | No | The database to be queried. By default, all databases are queried. |
| User | String | No | The username to be queried. By default, all users are queried. |
| Form | String | No | The file or stream to be downloaded. If you set this parameter to File, only common parameters are returned. In this case, you need to call the DescribeSQLLogFiles operation to obtain the final URL to download the file. If you set this parameter to Stream, the data stream is returned. Default value: Stream. |
| QueryKeywords | String | No | The keywords used for a query. Use spaces to separate multiple keywords. You can specify a maximum of 10 keywords. |
| PageSize | Integer | No | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| PageNumber | Integer | No | The number of the page to return. Valid values: any non-zero positive integer. Default value: 1. |

###### 1.1.6.3.3 Response parameters

| Parameter | Type | Description |
|---|---|---|
| Common response parameters | - | For more information, see Common response parameters. |
| TotalRecordCount | Integer | The total number of entries. |
| PageNumber | Integer | The number of the current page. |
| PageRecordCount | Integer | The number of SQL logs on the current page. |
| Items | List<SQLRecord> | The array that consists of SQLRecord data. |
| TotalRecordCount | Integer | The total number of entries. |

SQLRecord parameters

| Parameter | Type | Description |
|---|---|---|
| DBName | String | The name of the database. |
| AccountName | String | The name of the account. |
| HostAddress | String | The IP address of the client. |
| Syntax | String | The executed statement. |
| TotalExecutionTimes | Long | The amount of time taken to execute the operation. Unit: microseconds. |
| ReturnRowCounts | Long | The number of entries returned. |
| ExecuteTime | String | The execution time. The time is in the yyyy-MM-ddTHH:mm:ssZ format and displayed in UTC. |
| ThreadID | String | The ID of the thread. |

| Parameter | Type | Description |
|---|---|---|
| Node | String | The node on which the statement is executed. If you specify this parameter, the information about primary and secondary nodes is returned for a replica set instance, while for a sharded cluster instance the information about each mongos is returned. |

##### 1.1.6.4 DescribeAuditFiles

###### 1.1.6.4.1 Description

This API supports replica set instances only.

###### 1.1.6.4.2 Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeAuditFiles. |
| DBInstanceId | String | Yes | The ID of the instance for which to describe audit files. |
| NodeId | String | No | The ID of a mongos or shard node in a sharded cluster instance. If this parameter is not specified, both a mongos ID and a shard ID are displayed. This parameter cannot be used for replica set instances. |

###### 1.1.6.4.3 Response parameters

| Parameter | Type | Description |
|---|---|---|
| Common response parameters | - | For more information, see Common parameters. |
| TotalRecordCount | Integer | The total number of records. |

| eveloper Guide·Developer Guide |   | ApsaraDB for MongoD |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| PageNumber | Integer | The number of the current page. |
| PageRecordCount | Integer | The number of records on the current page. |
| Items | List<LogFile> | An array that consists of LogFile data. |

LogFile parameters

| Parameter | Type | Description |
|---|---|---|
| FileID | Integer | The ID of the file. |
| DBInstanceId | String | The name of the instance. |
| LogStatus String | String | Success: The log file is archived. - Failed: The log file failed to be archived. - Generating: The log file is being archived. - Initializing: Log archiving has not started yet. |
| LogStartTime | String | The beginning of the time range where the log audit was executed. |
| LogEndTime | String | The end of the time range where the log audit was executed. |
| LogDownloadURL | String | The URL to download audit logs. If the download URL is unavailable, this parameter will be empty. |
| LogSize | Long | The size of the audit log file. Unit: Byte. |

#### 1.1.7 Backup and restoration management

##### 1.1.7.1 DescribeBackupPolicy

###### 1.1.7.1.1 Description

This API supports replica set instances only.

###### 1.1.7.1.2 Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeBackupPolicy. |
| DBInstanceId | String | Yes | The ID of the instance for which to describe the backup policy. |

###### 1.1.7.1.3 Response parameters

| Parameter | Type | Description |
|---|---|---|
| Common response parameters | - | For more information, see Common parameters. |
| BackupRetentionPeriod | String | The number of days for which backup files can be retained. |
| PreferredBackupTime | String | The period of time to execute backup. The format is HH:mmZ- HH:mm Z. |
| PreferredBackupPeriod | String | The time cycle to execute backup. Valid values: Monday Tuesday Wednesday Thursday Friday Saturday Sunday |

##### 1.1.7.2 ModifyBackupPolicy

###### 1.1.7.2.1 Description

This API supports replica set instances only.

###### 1.1.7.2.2 Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to ModifyBackupPolicy. |
| DBInstanceId | String | Yes | The ID of the instance. |
| PreferredBackupTime | String | Yes | The period of time to execute backup. Specify the time in the HH:mmZ-HH:mmZ format. |
| PreferredBackupPeriod | String | Yes | The time cycle to execute backup. Valid values: Monday Tuesday Wednesday Thursday Friday Saturday Sunday |

###### 1.1.7.2.3 Response parameters

| Parameter | Type | Description |
|---|---|---|
| Common response parameters | - | For more information, see the "Common response parameters" topic. |

##### 1.1.7.3 CreateBackup

###### 1.1.7.3.1 Description

This API supports replica set instances only.

###### 1.1.7.3.2 Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateBackup. |

| psaraDB for MongoDB |   | Devel | oper Guide·Developer Guid |
|---|---|---|---|
| Parameter | Type | Required | Description |

| DBInstanceId | String | Yes | The ID of the instance for which to create a backup. |
|---|---|---|---|

###### 1.1.7.3.3 Response parameters

| Parameter | Type | Description |
|---|---|---|
| Common response parameters | - | For more information, see the "Common response parameters" topic. |
| BackupId | String | The ID of a backup. |

##### 1.1.7.4 DescribeBackups

###### 1.1.7.4.1 Description

This API supports replica set instances only.

###### 1.1.7.4.2 Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeBackups. |
| DBInstanceId | String | Yes | The ID of the instance to be queried. |
| StartTime | String | Yes | The start time of data returned by a query. The format is YYYYMM- DD'T'HH:mmZ. Example: 2011-06- 11T15:00Z. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| EndTime | String | Yes | The end time of data returned by a query. The format is YYYYMM- DD'T'HH:mmZ. Example: 2011-06- 11T16:00Z. |
| BackupId | Integer | No | The ID of a backup. |
| NodeId | String | No | The ID of a shard node. This parameter applies only to sharded cluster instances. |
| PageSize | Integer | No | The number of records on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNumber | Integer | No | The page number to request, which must be any integer greater than 0. Default value: 1. |

###### 1.1.7.4.3 Response parameters

| Parameter | Type | Description |
|---|---|---|
| Common response parameters | - | For more information, see Common response parameters. |
| Items | List<Backup> | The array that consists of backups. |
| PageNumber | Integer | The number of the returned page. |
| TotalCount | Integer | The total number of backups. |
| PageSize | Integer | The number of entries returned per page. |

Backup data structure

| Parameter | Type | Description |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| BackupDBNames (TBD) | String | The list of databases in a backup set. Separate multiple databases with commas (,), such as "Db1,Db2,Db3…". It is used to check whether a full backup is performed. |
| BackupId | Integer | The ID of a backup. |
| BackupStatus | String | The status of the backup task. Valid values: Success: The backup task is completed. Failed: The backup task fails. |
| BackupStartTime | String | The beginning of the backup time range. The time is in the yyyy- MM-ddTHH:mm:ssZ format and displayed in UTC. |
| BackupEndTime | String | The end of the backup time range. The time is in the yyyy- MM-ddTHH:mm:ssZ format and displayed in UTC. |
| BackupType | String | The type of the backup. Valid values: FullBackup IncrementalBackup |
| BackupMode | String | The backup mode. Valid values: Automated: indicates an automatic backup. Manual: indicates a manual backup. |
| BackupMethod | String | The method of the backup. Valid values: Logical Physical |
| BackupDownloadURL | String | The download URL of the backup file. If the download URL is unavailable, the value is an empty string. |
| BackupSize | Long | The size of the backup file. Unit: Byte. |

##### 1.1.7.5 RestoreDBInstance

###### 1.1.7.5.1 Description

This API supports replica set instances only.

###### 1.1.7.5.2 Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to RestoreDBInstance. |
| DBInstanceId | String | Yes | The ID of the instance to be queried. Only replica set instances are supported. |
| BackupId | String | Yes | The ID of a backup. |

###### 1.1.7.5.3 Response parameters

| Parameter | Type | Description |
|---|---|---|
| Common response parameters | - | For more information, see the "Common response parameters" topic. |

#### 1.1.8 Performance monitoring management

##### 1.1.8.1 DescribeDBInstancePerformance

###### 1.1.8.1.1 Description

This API supports replica set instances only.

###### 1.1.8.1.2 Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDBInstancePerf ormance. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| DBInstanceId | String | Yes | The ID of the instance. |
| StartTime | String | Yes | The beginning of the time range to query. Specify the time in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |
| EndTime | String | Yes | The end of the time range to query. Specify the time in the yyyy- MM-ddTHH:mm:ssZ format. The time must be in UTC. |
| ReplicaSetRole | String | Yes | The role of a replica set. Valid values: Primary and Secondary. |
| Key | String | Yes | The monitoring metrics for database performance. Separate multiple metrics with commas (,). For more information about the metrics, see Performance metrics. |

###### 1.1.8.1.3 Response parameters

| Parameter | Type | Description |
|---|---|---|
| Common response parameters | - | For more information, see Common response parameters. |
| DBInstanceId | String | The ID of the instance. |
| Engine | String | The database type of the instance. |
| StartTime | String | The beginning of the time range to query. The time is in the yyyy- MM-ddTHH:mm:ssZ format and displayed in UTC. |
| EndTime | String | The end of the time range to query. The time is in the yyyy-MM- ddTHH:mm:ssZ format and displayed in UTC. |

| Developer Guide·Developer Guide |   | ApsaraDB for MongoD |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| PerformanceKeys | List<PerformanceKey> | The array that consists of performance metrics. It is in the {perf1, perf2, perf3, ...} format. |

PerformanceKey parameters

| Parameter | Type | Description |
|---|---|---|
| Key | String | The name of a metric. |
| Unit | String | The unit of a metric. |
| ValueFormat | String | The format of a value. If a value is null, VALUE will be returned. If multiple metrics return in the parameter value, these metrics will be separated with ampersands (&), such as com delete&com insert&com _ _ _ insert select&com replace. _ _ |
| Values | List<PerformanceValue> | The array that consists of the metric values. It is in the {value1, value2, ...} format. |

PerformanceValue parameters

| Parameter | Type | Description |
|---|---|---|
| Value | String | The value of a metric. |
| date | String | The calculation time. The time is in the yyyy-MM-ddTHH:mm:ssZ format and displayed in UTC. |

#### 1.1.9 Appendix

##### 1.1.9.1 Error codes

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because RAM users are not authorized to call the API. | Forbidden.RAM | User not authorized to operate on the specified resource, or this API doesn’t support RAM. | 403 |

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because this operation is not allowed in RAM mode. | Forbedden.NotSupport RAM | This action does not support accessed by RAM mode. | 403 |
| The error message returned because an exception occurred on the server. | ServiceUnavailable | The request has failed due to a temporary failure of the server. | 503 |
| The error message returned because the specified instance status does not exist. | InvalidStatus.NotFound | The Status provided does not exist in our records. | 404 |
| The error message returned because the specified parameter is invalid | InvalidParameter | The specified parameter "InstanceName" is not valid. | 400 |
| The error message returned because you are not authorized to call the administrator- specific API. | Forbbiden.NotAdminUse r | User not authorized to operate on the specified API as you are not the administrator. | 403 |
| The error message returned because a required parameter is not specified. | MissingParameter | Specified parameter is missing. | 400 |
| The error message returned because neither of the InstanceName and NewPassword parameters is specified. | MissingParameter | InstanceName/NewPass word at least one is mandatory for this action. | 400 |
| The error message returned because the required OwnerId parameter is not specified for this operation. | MissingParameter | The input parameter OwnerId,OwnerAccount that is mandatory for processing this request is not supplied. | 403 |
| The error message returned because the specified Token parameter is invalid. | InvalidToken.Malformed | The Specified parameter \”Token\” is not valid. | 400 |

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the specified InstanceName parameter is invalid. | InvalidInstanceName.Ma lformed | The Specified parameter \”InstanceName\” is not valid. | 400 |
| The error message returned because the specified Password parameter is invalid. | InvalidPassword.Malfor med | The Specified parameter \”Password\” is not valid.” | 400 |
| The error message returned because the specified Instances parameter is invalid. | InvalidInstances.Malfor med | The Specified parameter \”Instances\” is not valid. | 400 |
| The error message returned because the specified StartTime parameter is invalid. | InvalidStartTime.Malfor med | The Specified parameter \”StartTime\” is not valid. | 400 |
| The error message returned because the specified EndTime parameter is invalid. | InvalidEndTime.Malform ed | The Specified parameter \”EndTime\” is not valid. | 400 |
| The error message returned because the specified InstanceIds parameter is invalid. | InvalidInstanceIds.Malfo rmed | The Specified parameter \”InstanceIds\” is not valid. | 400 |
| The error message returned because your balance is insufficient to perform the current operation. | InsufficientBalance | Your account does not have enough balance. | 400 |
| The error message returned because your account fails to pass real-name verification. | RealNameAuthenticatio nError | Your account has not passed the real-name authentication yet. | 403 |
| The error message returned because the purchase amount exceeds the limit for each subscription. | QuotaExceed | Living afterpay instances quota exceeded. | 400 |
| The error message returned because the capacity configuration is invalid. | InvalidCapacity.NotFoun d | The Capacity provided does not exist in our records. | 400 |

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the two specified requests use the same ClientToken. | IdempotentParameterMi smatch | Request uses a client token in a previous request but is not identical to that request. | 400 |
| The error message returned because the available inventory in the specified zone is insufficient. | QuotaNotEnough | Quota not enough in this zone. | 400 |
| The error message returned because you are not authorized to call the subscription service API. | Forbbiden.SubUser | The specified action is not available for you. | 403 |
| The error message returned because the Alibaba Cloud risk control system rejects this access request. | Forbidden.RiskControl | This operation is forbidden by Aliyun Risk Control system. | 403 |
| The error message returned because the specified region ID does not exist. | InvalidRegion.NotFound | The RegionId or ZoneId provided does not exist in our records. | 404 |
| The error message returned because the specified ZoneId parameter is invalid. | InvalidZoneId.NotFound | The ZoneId provided is invalid. | 400 |
| The error message returned because the specified instance ID does not exist. | InvalidInstanceId.NotFou nd | The InstanceId provided does not exist in our records. | 404 |
| The error message returned because the provided password is incorrect. | IncorrectPassword | The Password provided is not correct. | 400 |
| The error message returned because the service is unavailable. | ServiceNotSupported | The specified service is not supported. | 400 |

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because this instance has a subscription renewal order that has not gone into effect. | HasRenewChangeOrder | This instance has a renewChange order. | 400 |
| The error message returned because an internal error occurs. | InternalError | The request processing has failed due to some unknown error. | 500 |
| The error message returned because the specified backup time is invalid. | InvalidPreferredBackupT ime | Specified preferred backup time is not valid. | 400 |
| The error message returned because the specified backup type is invalid. | InvalidBackupType.Form at | Specified backup type is not valid. | 400 |
| The error message returned because the specified backup method is invalid. | InvalidBackupMethod.Fo rmat | Specified backup method is not valid. | 400 |
| The error message returned because the backup task already exists. | BackupJobExists | A backup job already exists in the specified DB instance. | 400 |
| The error message returned because the maximum number of daily backup operations has been reached. | BackupTimesExceeded | Exceeding the daily backup times of this DB instance. | 400 |
| The error message returned because no parameters are specified. | ParameterLeastAssociat e | Must input at least one optional parameter. | 400 |
| The error message returned because the specified backup retention period is invalid. | InvalidBackupRetentionP eriod.Malformed | Specified backup retention period is not valid. | 400 |
| The error message returned because the specified next backup time is invalid. | InvalidPreferredBackupT ime.Format | Specified preferred backup time is not valid. | 400 |

| psaraDB for MongoDB |   | Devel | oper Guide·Developer Guid |
|---|---|---|---|

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the specified backup period is invalid. | InvalidPreferredBackupP eriod.Malformed | Specified backup period is not valid. | 400 |
| The error message returned because the current instance type does not support this operation. | IncorrectDBInstanceTyp e | Current DB instance type does not support this operation. | 400 |
| The error message returned because the specified key is invalid. | InvalidKey.Malformed | Specified key is not valid. | 400 |
| The error message returned because the signature nonce requested has already been used and cannot be used again. | SignatureNonceUsed | Specified signature nonce was used already. | 400 |
| The error message returned because no available virtual IP addresses can be allocated. | AllocateVpcIp.NotEnoug h | Ip resource is not enough | 400 |
| The error message returned because the current zone does not support instances of the specified type. | Zone.NotSupport | Specified zone does not support creating with instance class. | 400 |
| The error message returned because the instance type is invalid. | MissingClassCode | Capacity or InstanceClass is mandatory for this action. | 400 |
| The error message returned because the specified instance type is not supported. | InvalidDBInstanceClass.N otFound | Specified DB instance class is not found. | 404 |
| The error message returned because the instance is locked. | IncorrectDBInstanceLock Mode | Current DB instance lock mode does not support this operation. | 400 |
| The error message returned because the specified backup set ID does not exist. | InvalidBackupSetID.NotF ound | Specified backup set ID does not exist. | 400 |

| eveloper Guide·Developer | Guide |   | ApsaraDB for MongoD |
|---|---|---|---|

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the instance is in a state that does not support the current operation. | IncorrectDBInstanceStat e | Current DB instance state does not support this operation. | 400 |
| The error message returned because the available capacity in the specified instance is insufficient. | InsufficientResourceCap acity | There is insufficient capacity available for the requested instance. | 400 |
| The error message returned because the specified end time is invalid. | InvalidEndTime.Format | Specified end time is not valid. | 400 |
| The error message returned because the specified retention period of the classic network endpoint is invalid. | InvalidClassicExpiredDay s.Format | The specified classicExpiredDays format is not valid. | 400 |
| The error message returned because the backup set is in a state that does not support the current operation. | IncorrectBackupSetStat e | Current backup set state does not support operations. | 400 |
| The error message returned because the specified whitelist format is invalid. | InvalidSecurityIPList.For mat | Specified security IP list format is not valid. | 400 |

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

#### 1.2.9 Call SDK for Node.js

This topic describes how to obtain and use Apsara Stack SDK for Node.js. Prerequisites An authorized account and an AccessKey pair (AccessKey ID and AccessKey secret) are obtained. For more information, see Obtain an AccessKey pair. The endpoint of Apsara Stack API (ASAPI) is obtained. For more information, see Obtain the endpoint of Asapi. The region ID is obtained. For more information about how to query the region ID, see Query the region ID. Add dependencies
1. Install Apsara Stack SDK for Node.js.

```
 tnpm install --save @ali/asapi-nodejs-sdk
```

2. Add the following configurations to mocha.opts if mocha.opts depends on eggjs:

```
--recursive --colors --timeout 60000 --reporter mochawesome --require co-mocha --require egg-ts-helper/register --require espower-typescript/guess --require intelli-espower-loader
```

Use SDK for Node.js The following example shows how to call Apsara Stack SDK for Node.js.
1. Create a client instance. To create a client instance, you must set the region ID, endpoint,
AccessKey ID, and AccessKey secret in the config.ts file. Example:

```
local: {
    regionId: 'obtained region ID',
    API_GATEWAY: 'obtained endpoint',
    accessKeyId: 'your AccessKey ID',
    accessKeySecret: 'your AccessKey secret',
```

`},`
2. Create an API request and configure parameters.
3. Initiate the request and handle any responses or exceptions.

```
// Specify the ASAPI endpoint. const API_GATEWAY = "http://xxxx/asapi/v3" // Create the rpc client. const asapiClient = ctx.service.sdk.rpcClient; // Set request parameters. let params = {
    Action: 'CreateDBInstance',
    Product: 'MongoDB',
    regionId: 'cn-qingdao-env12-d01',
    accessKeyId: 'xxxxxxx',
    accessKeySecret: 'xxxxxxx',
    Version: '2015-12-01',
```

};

```
// Set parameters in the request header. asapiClient.addHeader("x-acs-regionId", "cn-qingdao-env12-d01"); // Initiate the request and obtain the response. const result = await asapiClient.doRequest(API_GATEWAY, params, {});
```

#### 1.2.10. (Optional) Use POP SDK to call ASAPI

This topic describes how to switch the gateway to ASAPI if an application uses POP SDK to call cloud products. Procedure
1. Switch the gateway to ASAPI and add common parameters required by the API operation to the
request header, so that the API operation can be called in a transparent manner.
2. Add the Product Name field to the request header.
Sample code An API operation of ApsaraDB for MongoDB is called in the following example:

```java
try {
            ModifyDBInstanceDescriptionResponse response = client.getAcsResponse(request);
            System.out.println(new Gson().toJson(response));
```

`}`

```
catch (ServerException e) {
            e.printStackTrace();
```

`}`

```java
catch (ClientException e) {
            System.out.println("ErrCode:" + e.getErrCode());
            System.out.println("ErrMsg:" + e.getErrMsg());
            System.out.println("RequestId:" + e.getRequestId());
```

`}`
