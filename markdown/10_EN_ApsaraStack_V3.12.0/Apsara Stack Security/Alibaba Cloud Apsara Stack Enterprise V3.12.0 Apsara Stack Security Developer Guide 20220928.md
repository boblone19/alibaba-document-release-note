---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Apsara Stack Security Developer Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 755
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Apsara Stack Security Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E5%85%B6%E4%BB%96/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20Apsara%20Stack%20Security%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 Apsara Stack Security Developer Guide 20220928

## Table of Contents

- 1 API overview
- 2 Apsara Stack Security Console
  - 2.1 List of operations
  - 2.2 Make API requests
    - 2.2.1 Request structure
    - 2.2.2 Request signatures
    - 2.2.3 Common parameters
    - 2.2.4 Response structure
  - 2.3 APIs
    - 2.3.1 DescribeAliyunAccounts
    - 2.3.2 ModifyAliyunAccount
    - 2.3.3 DescribeFeatures
- 3 Threat Detection Service (TDS)
  - 3.1 List of operations by function
  - 3.2 Make API requests
    - 3.2.1 Request structure
    - 3.2.2 Signature mechanism
    - 3.2.3 Common request parameters
    - 3.2.4 Response structure
  - 3.3 Asset management
    - 3.3.1 DescribeAllEntity
    - 3.3.2 DescribeFieldStatistics
    - 3.3.3 DescribeGroupedTags
    - 3.3.4 DescribeAllGroups
    - 3.3.5 DeleteGroup
    - 3.3.6 CreateOrUpdateAssetGroup
    - 3.3.7 ModifyTagWithUuid
    - 3.3.8 DescribeInstanceStatistics
    - 3.3.9 DescribeCloudProductFieldStatistics
    - 3.3.10 DescribeDomainCount
    - 3.3.11 DescribeDomainList
    - 3.3.12 DescribeDomainDetail
    - 3.3.13 DescribeCloudCenterInstances
    - 3.3.14 DescribeSummaryInfo
    - 3.3.15 DescribeSearchCondition
    - 3.3.16 DescribeAssetDetailByUuid
    - 3.3.17 DescribeSasAssetStatisticsColumn
    - 3.3.18 DescribePropertyUsageNewest
    - 3.3.19 DeleteTagWithUuid
    - 3.3.20 ModifyPushAllTask
    - 3.3.21 DescribeCriteria
    - 3.3.22 DescribeExportInfo
    - 3.3.23 ModifyLoginSwitchConfig
    - 3.3.24 ModifyLoginBaseConfig
    - 3.3.25 DeleteLoginBaseConfig
    - 3.3.26 DescribeAssetDetailByUuids
  - 3.4 Secure score
    - 3.4.1 DescribeSecureSuggestion
  - 3.5 Security alerts
    - 3.5.1 HandleSecurityEvents
    - 3.5.2 DescribeSecurityStatInfo
    - 3.5.3 DescribeAlarmEventList
    - 3.5.4 DescribeAlarmEventDetail
    - 3.5.5 DescribeSuspEvents
    - 3.5.6 DescribeSuspEventDetail
    - 3.5.7 HandleSimilarSecurityEvents
    - 3.5.8 DescribeSecurityEventOperations
    - 3.5.9 DescribeSecurityEventOperationStatus
    - 3.5.10 CreateSimilarSecurityEventsQueryTask
    - 3.5.11 DescribeSimilarSecurityEvents
    - 3.5.12 DescribeSimilarEventScenarios
    - 3.5.13 DescribeUserLayoutAuthorization
    - 3.5.14 RollbackSuspEventQuaraFile
    - 3.5.15 DescribeSuspEventQuaraFiles
  - 3.6 Configuration assessment
    - 3.6.1 DescribeRiskItemType
    - 3.6.2 StartBaselineSecurityCheck
    - 3.6.3 DescribeRiskCheckSummary
    - 3.6.4 ModifyRiskCheckStatus
    - 3.6.5 DescribeRiskCheckResult
    - 3.6.6 DescribeSecurityCheckScheduleConfig
    - 3.6.7 ModifyRiskSingleResultStatus
    - 3.6.8 ModifySecurityCheckScheduleConfig
    - 3.6.9 DescribeRiskCheckItemResult
  - 3.7 Brute-force attacks protection
    - 3.7.1 CreateAntiBruteForceRule
    - 3.7.2 ModifyAntiBruteForceRule
  - 3.8 Vulnerability management
    - 3.8.1 ModifyVulTargetConfig
    - 3.8.2 ModifyStartVulScan
    - 3.8.3 DescribeVulList
    - 3.8.4 DescribeEmgVulGroup
    - 3.8.5 DescribeVulWhitelist
    - 3.8.6 DescribeConcernNecessity
    - 3.8.7 DescribeGroupedVul
    - 3.8.8 ModifyCreateVulWhitelist
    - 3.8.9 ModifyEmgVulSubmit
    - 3.8.10 DescribeAutoDelConfig
    - 3.8.11 ModifyOperateVul
  - 3.9 Baseline check
    - 3.9.1 DescribeCheckWarningSummary
    - 3.9.2 DescribeStratety
    - 3.9.3 DescribeStrategyExecDetail
    - 3.9.4 DescribeCheckWarnings
    - 3.9.5 DescribeCheckWarningDetail
    - 3.9.6 DescribeWarningMachines
    - 3.9.7 DescribeUserBaselineAuthorization
    - 3.9.8 ValidateHcWarnings
    - 3.9.9 FixCheckWarnings
  - 3.10 Asset fingerprints
    - 3.10.1 DescribePropertyCount
    - 3.10.2 DescribePropertyPortDetail
    - 3.10.3 DescribePropertyProcDetail
    - 3.10.4 DescribePropertyPortItem
    - 3.10.5 DescribePropertyProcItem
    - 3.10.6 DescribePropertySoftwareDetail
    - 3.10.7 DescribePropertySoftwareItem
    - 3.10.8 DescribePropertyUserDetail
    - 3.10.9 DescribePropertyUserItem
    - 3.10.10 DescribeModuleConfig
  - 3.11 Notifications
    - 3.11.1 DescribeDingTalk
    - 3.11.2 DescribeNoticeConfig
  - 3.12 Agent client
    - 3.12.1 SasInstallCode
    - 3.12.2 PauseClient
  - 3.13 Export check results
    - 3.13.1 ExportRecord
  - 3.14 Virus detection
    - 3.14.1 OperateSuspiciousTargetConfig
- 4 Server Guard
  - 4.1 List of operations
  - 4.2 Make API requests
    - 4.2.1 Request structure
    - 4.2.2 Signature mechanism
    - 4.2.3 Common request parameters
    - 4.2.4 Response structure
  - 4.3 Asset management
    - 4.3.1 CreateGroup
    - 4.3.2 DescribeGroupSummary
    - 4.3.3 DescribeGroupStruct
    - 4.3.4 DeleteGroup
    - 4.3.5 DescribeAllTag
    - 4.3.6 DescribeBetachTag
    - 4.3.7 ModifyBetachTag
    - 4.3.8 DeleteTag
    - 4.3.9 DescribeAllEntity
    - 4.3.10 DescribeEntityList
    - 4.3.11 ModifyEntityGroup
    - 4.3.12 DescribeMachines
    - 4.3.13 DescribeMachineDetail
    - 4.3.14 DescribePropertyScheduleConfig
    - 4.3.15 ModifyPropertyScheduleConfig
    - 4.3.16 DescribePropertyStatistic
    - 4.3.17 DescribePropertyPortItem
    - 4.3.18 DescribePropertyPortDetail
    - 4.3.19 DescribePropertyPortDiff
    - 4.3.20 DescribePropertyProcItem
    - 4.3.21 DescribePropertyProcDetail
    - 4.3.22 DescribePropertyProcDiff
    - 4.3.23 DescribePropertySoftwareItem
    - 4.3.24 DescribePropertySoftwareDetail
    - 4.3.25 DescribePropertySoftwareDiff
    - 4.3.26 DescribePropertyUserItem
    - 4.3.27 DescribePropertyUserDetail
    - 4.3.28 DescribePropertyUserDiff
    - 4.3.29 PushAllTask
    - 4.3.30 DescribeTopRiskyAssets
    - 4.3.31 UnbindAegis
    - 4.3.32 UninstallAegis
  - 4.4 Vulnerability management
    - 4.4.1 DescribeTarget
    - 4.4.2 ModifyVulTarget
    - 4.4.3 DescribeVulTargetStatistics
    - 4.4.4 DescribeTargetConfig
    - 4.4.5 ModifyTargetConfig
    - 4.4.6 DescribeVulConfig
    - 4.4.7 ModifyVulConfig
    - 4.4.8 DescribeAutoDelConfig
    - 4.4.9 ModifyAutoDelConfig
    - 4.4.10 DescribeVulLevel
    - 4.4.11 ModifyVulLevel
    - 4.4.12 CreateVulWhitelist
    - 4.4.13 DescribeVulWhitelist
    - 4.4.14 DeleteVulWhitelist
    - 4.4.15 DescribeGroupedVul
    - 4.4.16 DescribeVulList
    - 4.4.17 DescribeVulDetails
    - 4.4.18 DescribeVulNumStatistics
    - 4.4.19 DescribeVulLevelStatistics
    - 4.4.20 DescribeVulMachineList
    - 4.4.21 OperateVul
    - 4.4.22 ModifyBatchIgnoreVul
    - 4.4.23 DeleteVulBatch
    - 4.4.24 ExportVul
    - 4.4.25 DescribeVulExportInfo
  - 4.5 Baseline check
    - 4.5.1 DescribeStrategy
    - 4.5.2 DescribeStratetyDetail
    - 4.5.3 ModifyStrategy
    - 4.5.4 DeleteStrategy
    - 4.5.5 DescribeStrategyTarget
    - 4.5.6 ModifyStrategyTarget
    - 4.5.7 DescribeUuidConfig
    - 4.5.8 ModifyMachineConfig
    - 4.5.9 DescribeUserSetting
    - 4.5.10 CreateUserSetting
    - 4.5.11 DescribeRiskWhiteList
    - 4.5.12 BatchDeleteWhiteList
    - 4.5.13 CreateUserWhiteList
    - 4.5.14 DescribeStratety
    - 4.5.15 DescribeStrategyExecDetail
    - 4.5.16 DescribeRiskType
    - 4.5.17 Describesummary
    - 4.5.18 OperateWarning
    - 4.5.19 ExportWarning
    - 4.5.20 DescribeExportInfo
  - 4.6 Unusual logon detection
    - 4.6.1 DescribeBaseConfigs
    - 4.6.2 ModifyBaseConfig
    - 4.6.3 DeleteBaseConfig
    - 4.6.4 DescribeSwitchConfigs
    - 4.6.5 ModifySwitchConfig
    - 4.6.6 DescribeConfigTarget
  - 4.7 Webshell detection
    - 4.7.1 DescribeWebPath
    - 4.7.2 ModifyWebPath
    - 4.7.3 DescribeCategoryCount
    - 4.7.4 DescribeWebshell
    - 4.7.5 OperateTrojan
    - 4.7.6 DescribeQuaraFile
    - 4.7.7 RollbackQuaraFile
  - 4.8 Exception detection on hosts
    - 4.8.1 DescribeSuspEventTypes
    - 4.8.2 DescribeSuspTrendStatistics
    - 4.8.3 OperateSuspiciousEvent
    - 4.8.4 OperateLoginLog
    - 4.8.5 CreateSuspiciousExport
    - 4.8.6 DescribeSuspiciousExportInfo
    - 4.8.7 DescribeVirusInfo
  - 4.9 Retrieval of host logs
    - 4.9.1 CreateLogQuery
    - 4.9.2 DescribeLogQuery
    - 4.9.3 DeleteLogQuery
    - 4.9.4 DescribeFilterFields
    - 4.9.5 DescribeHistogram
    - 4.9.6 DescribeLogInfo
    - 4.9.7 DescribeLogItems
- 5 Anti-DDoS
  - 5.1 List of operations
  - 5.2 Make API requests
    - 5.2.1 Request structure
    - 5.2.2 Signature mechanism
    - 5.2.3 Common request parameters
    - 5.2.4 Response structure
  - 5.3 APIs
    - 5.3.1 CheckIpSegment
    - 5.3.2 DescribeRegionName
    - 5.3.3 CreateIpSegment
    - 5.3.4 DescribeIpSegment
    - 5.3.5 DeleteIpSegment
    - 5.3.6 ModifyIpSegment
    - 5.3.7 CreateDdosPolicy
    - 5.3.8 DescribeDdosPolicies
    - 5.3.9 DeleteDdosPolicy
    - 5.3.10 ModifyDdosPolicy
    - 5.3.11 DescribeBlockSwitchs
    - 5.3.12 ModifyBlockSwitchs
    - 5.3.13 DescribeDdosEvents
    - 5.3.14 DescribeFlowAnalysisResult
    - 5.3.15 DescribeFlowDetails
    - 5.3.16 CancelCleanStatus
    - 5.3.17 CreateWhiteList
    - 5.3.18 DescribeWhiteList
    - 5.3.19 DeleteWhiteList
    - 5.3.20 DescribeConsoleDdosPolicies
- 6 Cloud Firewall
  - 6.1 List of operations by function
  - 6.2 Make API requests
    - 6.2.1 Request structure
    - 6.2.2 Signature mechanism
    - 6.2.3 Common request parameters
    - 6.2.4 Response structure
  - 6.3 Access control
    - 6.3.1 DescribePolicyPriorUsed
    - 6.3.2 ModifyControlPolicyPosition
    - 6.3.3 DescribeControlPolicy
    - 6.3.4 AddControlPolicy
    - 6.3.5 DeleteControlPolicy
    - 6.3.6 ModifyControlPolicy
    - 6.3.7 VPC firewalls
      - 6.3.7.1 CreateVpcFirewallControlPolicy
      - 6.3.7.2 DescribeVpcFirewallControlPolicy
      - 6.3.7.3 ModifyVpcFirewallControlPolicy
      - 6.3.7.4 ModifyVpcFirewallControlPolicyPosition
      - 6.3.7.5 DeleteVpcFirewallControlPolicy
      - 6.3.7.6 DescribeVpcFirewallPolicyPriorUsed
      - 6.3.7.7 DescribeVpcFirewallAclGroupList
      - 6.3.7.8 ResetVpcFirewallRuleHitCount
  - 6.4 Firewall switch
    - 6.4.1 PutEnableFwSwitch
    - 6.4.2 PutDisableFwSwitch
    - 6.4.3 PutEnableAllFwSwitch
    - 6.4.4 PutDisableAllFwSwitch
  - 6.5 Address books
    - 6.5.1 AddAddressBook
    - 6.5.2 DeleteAddressBook
    - 6.5.3 ModifyAddressBook
    - 6.5.4 DescribeAddressBook
- 7 Sensitive Data Discovery and Protection
  - 7.1 List of operations by function
  - 7.2 Make API requests
    - 7.2.1 Request structure
    - 7.2.2 Request signatures
    - 7.2.3 Common parameters
    - 7.2.4 Responses
  - 7.3 APIs
    - 7.3.1 DescribeDataAssets
    - 7.3.2 DescribeInstances
    - 7.3.3 DescribeTables
    - 7.3.4 DescribePackages
    - 7.3.5 DescribeColumns
    - 7.3.6 DescribeOssObjects
    - 7.3.7 DescribeOssObjectDetail
    - 7.3.8 DescribeDeparts
    - 7.3.9 DescribeAccounts
    - 7.3.10 DescribeAccountDetail
    - 7.3.11 DescribePrivileges
    - 7.3.12 DescribeEventTypes
    - 7.3.13 DescribeEvents
    - 7.3.14 DescribeEventDetail
    - 7.3.15 ModifyEventStatus
    - 7.3.16 ModifyEventTypeStatus
    - 7.3.17 ModifyDefaultLevel
    - 7.3.18 DescribeRules
    - 7.3.19 CreateRule
    - 7.3.20 ModifyRule
    - 7.3.21 ModifyRuleStatus
    - 7.3.22 DeleteRule
    - 7.3.23 DescribeDataLimitSet
    - 7.3.24 CreateDataLimit
    - 7.3.25 DeleteDataLimit
  - 7.4 Data dictionaries
    - 7.4.1 Operation type definition
    - 7.4.2 Resource type definition
    - 7.4.3 Risk level definition
- 8 Security Operations Center
  - 8.1 List of operations by function
  - 8.2 Request method
    - 8.2.1 Request syntax
    - 8.2.2 Sign API requests
    - 8.2.3 Common parameters
    - 8.2.4 Response structure
  - 8.3 Operations
    - 8.3.1 QueryDataCount
    - 8.3.2 GetAssetCount
    - 8.3.3 GetEcsProtectCount
    - 8.3.4 DescribeAttacks
    - 8.3.5 DescribeAlarms
    - 8.3.6 DescribeVulFrangs
    - 8.3.7 DescribeHcFrangs
    - 8.3.8 DescribePBLineFrangs
    - 8.3.9 QueryDataEnum
    - 8.3.10 QueryDataCodeValue
    - 8.3.11 QueryDataDistribution
    - 8.3.12 SaveOrUpdateSocReportTask
    - 8.3.13 QuerySocReportTasks
    - 8.3.14 DelSocReportTask
    - 8.3.15 QuerySocReportRecords
    - 8.3.16 GetDeptMap
    - 8.3.17 GetRegionMap
    - 8.3.18 DownloadFile
    - 8.3.19 GetEcsList
    - 8.3.20 GetDiskList
    - 8.3.21 GetSecurityGroupList
    - 8.3.22 GetEcsInfo
    - 8.3.23 GetRdsList
    - 8.3.24 GetRdsInstanceIPArrayList
    - 8.3.25 GetRdsInfo
    - 8.3.26 GetOssList
    - 8.3.27 GetSlbList
    - 8.3.28 GetEipList
    - 8.3.29 GetAlarmConfig
    - 8.3.30 UpdateAlarmConfig
    - 8.3.31 GetAlarmContacts
    - 8.3.32 AddAlarmContacts
    - 8.3.33 DeleteAlarmContacts
    - 8.3.34 SendAlarm
    - 8.3.35 QuerySource
    - 8.3.36 QueryType
    - 8.3.37 QueryLog
    - 8.3.38 GetVpcList
    - 8.3.39 GetMachineList
    - 8.3.40 GetMachineInfo
    - 8.3.41 DescribeSocUsers
    - 8.3.42 DeleteSocUser
    - 8.3.43 SaveOrUpdateSocUser
- 9 Error codes

## 1 API overview

This document introduces all of the operations that you can call by using Apsara Stack Security service APIs. rity Console

## 2 Apsara Stack Security Console

### 2.1 List of operations

This topic introduces all of the Apsara Stack Security console operations that you can call. For more information, see the corresponding operation description.

| Operation | Description |
|---|---|
| DescribeAliyunAccounts | Queries Alibaba Cloud accounts. |
| ModifyAliyunAccount | Modifies the information of an Alibaba Cloud account. |
| DescribeFeatures | Queries the deployed Apsara Stack Security features. |

### 2.2 Make API requests

#### 2.2.1 Request structure

Apsara Stack Security API operations use the RPC protocol. This topic describes the structure of API requests. You can call Apsara Stack Security API operations by sending HTTP requests. The request syntax is as follows:

```
http://endpoint/?Action=xx&parameters
```

where:

| endpoint |   | : the endpoint used to call a cloud service |
|---|---|---|
| console is | yundunprivate.[ RegionId].example.com |   |

Not e example.com indicates the domain name of Apsara Stack. `Action` : the name of the operation being performed. For example, to obtain Apsara Stack Security features that have been deployed, you must set the Action parameter to DescribeFeatures. `parameters` : the request parameters for the operation. Separate multiple parameters with ampersands (&). Request parameters include both common parameters and operation-specific parameters. Common parameters include information such as the API version and authentication information. For more information about operation-specific parameters, see the corresponding operation description. rity Console Call the DescribeFeatures operation to query the Apsara Stack Security features that are deployed.

```
https://yundunprivate.[ RegionId].example.com/?Action=DescribeFeatures&AccessKeyId=key-test &Format=JSON&SecureTransport=true&SignatureMethod=HMAC-SHA1&SignatureNonce=15215528852396&S ignatureVersion=1.0&SourceIp=1xxxx6&Timestamp=2018-03-02Txxxxxxx&Version=2018-01-16&Signatu re=xxxx%xxxx%3D
```

API requests are presented in the following easy-to-read format in this document:

```
https://yundunprivate.[ RegionId].example.com/?Action=DescribeFeatures &Format=JSON &Version=2018-01-16 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2012-06-01T12:00:00Z
```

#### 2.2.2 Request signatures

Apsara Stack Security authenticates each access request. You need to include a signature for the submitted HTTP or HTTPS request. Authorization To ensure the security of your account, we recommend that you use a Resource Access Management (RAM) user to call operations. Before you use a RAM user to call an API operation, you must grant the RAM user the corresponding permission to call the operation by creating an authorization policy and attaching the policy to the RAM user. Signature You must sign all API requests to ensure security. Alibaba Cloud uses the request signature to verify the identity of the API caller. When you manually make an API request, you need to use the AccessKey Secret to calculate the signature, that is, the hash-based message authentication code (HMAC) value, based on the encoded and sorted request string. For more information, see the definition in RFC 2104. This section uses the raw access parameters in the following table to describe how to create an operation signature.

| Parameter | Description |
|---|---|
| Access point | http://tds.[ RegionId].example.com/? |
| Operation-specific parameters | Action=DescribeFeatures |

rity Console

| Parameter | Description |
|---|---|
| Common parameters except Signature | &Timestamp=2018-12-24T12:46:24Z &Format=JSON &AccessKeyId=<yourAccessKeyId> &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2018-12-03 &SignatureVersion=1.0 |
| AccessKey Secret | <yourAccessKeySecret> |

1. Create a canonicalized query string by arranging the request parameters.
Not e The request parameters include operation-specific parameters and all common request parameters except Signature. i. Sort the parameters. Sort the request parameters in alphabetical order. ii. Encode the parameters. Use UTF-8 to URL-encode the parameter names and values. The encoding rules are as follows: Uppercase letters, lowercase letters, digits, and some special characters such as hyphens (-), underscores (_), periods (.), and tildes (~) do not need to be encoded. Other characters must be percent encoded in %XY format. XY represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks (") are encoded as %22. Extended UTF-8 characters are encoded in %XY%ZA... format. Spaces must be encoded as %20. Do not encode spaces as plus signs (+). iii. Connect the encoded parameter names and values with equal signs (=). iv. Then, sort the parameter name and value pairs connected by equal signs in alphabetical order. Connect them with ampersands (&) to canonicalize a query string.
2. Use the canonicalized query string to construct the string for signature calculation based on the
following rules:

```
StringToSign=HTTPMethod + "&" + percentEncode("/") + "&" + percentEncode(CanonicalizedQueryString)
```

3. Calculate the HMAC value of the StringToSign based on the definition in RFC 2104.
Not e The key used for signature calculation is your AccessKey Secret jointed with an ampersand (&) (ASCII 38). Secure Hash Algorithm 1 (SHA1) is used as the hash algorithm.
4. Encode the HMAC value in Base64 to obtain the signature string.

```
LEW8N4y7Uasop******
```

rity Console
5. Add the signature string to the request as the Signature parameter.

#### 2.2.3 Common parameters

Common request parameters must be included in all Apsara Stack Security API requests, such as the API version number and authentication information.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Version | String | Yes | The version number of the API. The value is in the format of YYYY-MM-DD. Set the value to 2018-01-16. |
| AccessKeyId | String | Yes | The AccessKey ID provided to you by Alibaba Cloud. |
| Signature | String | Yes | The signature string of the current request. |
| SignatureMethod | String | Yes | The encryption method of the signature string. Set the value to HMAC-SHA1. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC. For example, 2014-05-26T12:00:00Z indicates 20:00:00 on May 26, 2014 (UTC+8). |
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Set the value to 1.0. |
| SignatureNonce | String | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |
| ResourceOwnerAc count | String | No | The owner account (the logon username) of the resource you want to access by using this API request. |
| Format | String | No | The format of the response. Valid values: JSON and XML. Default value: XML. |

#### 2.2.4 Response structure

rity Console Apsara Stack Security API responses can be returned in either the XML or JSON format. Every response returns a unique ID (indicated by RequestId) regardless of whether the call is successful. Sample responses (XML format)

```xml
<? xml version="1.0" encoding="UTF-8"? > <! --The root node of the result--> <Operation name+Response>
    <! --Returned request ID-->
    <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
    <! --Returned data-->
</Operation name+Response>
```

Sample responses (JSON format)

```json
"RequestId": "4C467B38-3910-447D-87BC-AC049166F216", /* Returned data */
```

### 2.3 APIs

#### 2.3.1 DescribeAliyunAccounts

You can call this operation to query Alibaba Cloud accounts.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeAliyunAccounts. |
| CurrentPage | Integer | Yes | The number of the page to return. |
| PageSize | Integer | Yes | The number of records to return on each page. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| CurrentPage | Integer | The number of the current page returned. |

| psara Stack Security |   | Developer Guide·Apsara Stack Sec rity Consol |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| PageSize | Integer | The number of records returned on each page. |
| TotalCount | Integer | The total number of returned pages. |
| HttpStatusCode | Integer | The HTTP status code returned. |
| AliyunAccounts | Array | The Alibaba Cloud accounts. For more information, see the following descriptions. |
| Id | Integer | The account record ID. |
| Aliuid | Long | The ID of the Alibaba Cloud account. |
| Account | String | The name of the Alibaba Cloud account. |
| AccessKey | String | The AccessKey ID of the Alibaba Cloud account. |
| AccessSecret | String | The AccessKey secret of the Alibaba Cloud account. |
| DataSecret | String | The DataSecret of the Alibaba Cloud account. |
| LicenseAegisNum | Integer | The number of Server Guard licenses. |
| LicenseTime | Long | The time when the licenses expire, in timestamp format. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://yundunprivate.[ RegionId].example.com/?Action=DescribeAliyunAccounts &CurrentPage=1 &PageSize=10
```

Sample response (JSON format) rity Console

```json
 "TotalCount":1,
 "PageSize":30,
 "RequestId":"7E33A454-20AA-49B1-8A9B-8979EFBDEDFC",
 "CurrentPage":1,
 "AliyunAccounts":[
   "Account":"1113454564",
   "AccessSecret":"*****",
   "AccessKey":"<yourAccessKeyId>",
   "Id":2,
   "LicenseAegisNum":0,
   "Aliuid":1441871509587522,
   "LicenseTime":1589596257000,
   "DataSecret":"*****"
```

`],`

```json
 "HttpStatusCode":200
```

#### 2.3.2 ModifyAliyunAccount

You can call this operation to modify the information of an Alibaba Cloud account with a specified account record ID.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to ModifyAliyunAccount. |
| Id | Integer | Yes | The account record ID. |
| Aliuid | Long | No | The ID of the Alibaba Cloud account. |
| Account | String | No | The name of the Alibaba Cloud account. |
| AccessKey | String | No | The AccessKey ID of the Alibaba Cloud account. |
| AccessSecret | String | No | The AccessKey secret of the Alibaba Cloud account. |

rity Console

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://yundunprivate.[ RegionId].example.com/?Action=ModifyAliyunAccount &Id=2 &Account=1113454564 &Aliuid=1441871509587522 &AccessKey=<yourAccessKeyId> &AccessSecret=xxxxxxxxx
```

Sample response (JSON format)

```json
 "RequestId":"C92B6187-603B-4E01-B0D7-74817F43852D"
```

#### 2.3.3 DescribeFeatures

You can call this operation to obtain a list of the deployed Apsara Stack Security features.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeFeatures. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Features | List | The list of the deployed Apsara Stack Security features. |

For more information about the error codes that this operation can return, see Error codes. rity Console Sample requests

```
https://yundunprivate.[ RegionId].example.com/?Action=DescribeFeatures
```

Sample responses (JSON format)

```json
 "RequestId":"BAEF6CE3-9990-4BDA-A056-4D269A724817",
 "Features":[
  "Basic",
  "Audit",
  "Sas",
  "Waf"
```

`]`

## 3 Threat Detection Service (TDS)

### 3.1 List of operations by function

The following tables list API operations available for use in Threat Detection Service. Cloud service configuration checks Baseline checks Cloud service configuration checks

| API operation | Description |
|---|---|
| DescribeRiskItemType | Queries the types of items for cloud service configuration checks. |
| StartBaselineSecurityCheck | Starts the baseline check. |
| DescribeRiskCheckSummary | Queries check results. |
| ModifyRiskCheckStatus | Modifies the status of a check result. |
| DescribeRiskCheckResult | Queries the result of a check item. |
| DescribeSecurityCheckScheduleCo nfig | Queries the custom check cycle and time period. |
| ModifyRiskSingleResultStatus | Modifies the status of an asset affected by a check item. |

Security alerts

| API operation | Description |
|---|---|
| DescribeAlarmEventDetail | Queries the details of an alert event. |
| DescribeSuspEventDetail | Queries the details of an unusual event. |
| DescribeAlarmEventList | Queries alert events of the security alert module. |
| DescribeSuspEvents | Queries exceptions. |

Vulnerability management

| API operation | Description |
|---|---|
| DescribeVulList | Queries vulnerabilities. |

| ervice (TDS) |   |
|---|---|
| API operation | Description |

| DescribeEmgVulGroup | Queries urgent vulnerabilities by group. |
|---|---|
| DescribeVulWhitelist | Queries the vulnerability whitelist by page. |
| DescribeGroupedVul | Queries vulnerabilities by group. |
| ModifyCreateVulWhitelist | Creates a vulnerability whitelist. |
| DescribeAutoDelConfig | Queries the configurations of automatic vulnerability deletion. |
| ModifyOperateVul | Manages a detected vulnerability. For example, you can verify, ignore, or fix a vulnerability. |

Baseline checks

| API operation | Description |
|---|---|
| DescribeWarningMachines | Queries information about servers where baseline check policies are performed. |
| DescribeStrategyExecDetail | Queries detailed results of the last baseline check. |
| DescribeCheckWarnings | Queries specified risk items and check items on a specified server. |
| DescribeCheckWarningDetail | Queries the details of a specified check item. |
| DescribeCheckWarningSummary | Queries the statistics of baseline check results. |
| DescribeStratety | Queries the configurations of baseline check policies. |

Asset management

| API operation | Description |
|---|---|
| DescribeFieldStatistics | Queries asset instances. |
| DescribeGroupedTags | Queries tag statistics. |
| DescribeAllGroups | Queries information about all asset groups. |
| DeleteGroup | Deletes a server group. |
| CreateOrUpdateAssetGroup | Modifies the relationship between an asset and an asset group. |
| ModifyTagWithUuid | Modifies the relationship between a tag and a server or a cloud service. |
| DescribeInstanceStatistics | Queries the statistics of an asset. |

| psara Stack Security | Developer Guide·Threat Detection |
|---|---|

| API operation | Description |
|---|---|
| DescribeCloudProductFieldStatisti cs | Queries the statistics of a cloud service. |
| DescribeDomainCount | Queries the number of domain assets. |
| DescribeDomainList | Queries domain assets. |
| DescribeDomainDetail | Queries the details of a domain asset. |
| DescribeCloudCenterInstances | Queries the asset information on the Assets page, such as the name and region of an asset instance. |
| DescribeSummaryInfo | Queries the security score of assets, the number of protected assets, and the number of unprotected assets. |

Asset fingerprints

| API operation | Description |
|---|---|
| DescribePropertyCount | Queries asset fingerprints. You can query the following types of asset fingerprints: process, port, software, and account. |
| DescribePropertyPortDetail | Queries the details of a specific port. |
| DescribePropertyProcDetail | Queries the details of a specific process. |
| DescribePropertyPortItem | Queries port information. |
| DescribePropertyProcItem | Queries process information. |
| DescribePropertySoftwareDetail | Queries the details of a software asset. |
| DescribePropertySoftwareItem | Queries software assets. |
| DescribePropertyUserDetail | Queries the details of a specific account. |
| DescribePropertyUserItem | Queries account information. |

### 3.2 Make API requests

#### 3.2.1 Request structure

Apsara Stack Security API operations use the RPC protocol. This topic describes the structure of API requests. You can call Apsara Stack Security API operations by sending HTTP requests. The request syntax is as follows:

```
http://endpoint/?Action=xx&parameters
```

where: `endpoint` : the endpoint of the Threat Detection Service API is `tds.[RegionId].example.com` . `Action` : the name of the operation being performed. For example, to query the Apsara Stack Security features that are deployed, you must set the Action parameter to DescribeFeatures. `parameters` : the request parameters for the operation. Separate multiple parameters with ampersands (&). Request parameters include both common parameters and operation-specific parameters. Common parameters include information such as the API version and identity authentication. For more information about operation-specific parameters, see the corresponding operation description. The following example demonstrates how to call the DescribeFeatures operation to query the Apsara Stack Security features that are deployed.

```
https://yundunprivate.[RegionId].example.com/?Action=DescribeFeatures&AccessKeyId=key-test& Format=JSON&SecureTransport=true&SignatureMethod=HMAC-SHA1&SignatureNonce=15215528852396&Si gnatureVersion=1.0&SourceIp=1xxxx6&Timestamp=2018-03-02Txxxxxxx&Version=2018-01-16&Signatur e=xxxx%xxxx%3D
```

API requests are presented in the following easy-to-read format in this document:

```
https://yundunprivate.[RegionId].example.com/?Action=DescribeFeatures &Format=JSON &Version=2018-01-16 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2012-06-01T12:00:00Z
```

#### 3.2.2 Signature mechanism

Apsara Stack Security authenticates each access request. You need to include a signature for the submitted HTTP or HTTPS request. API authorization To ensure the security of your account, we recommend that you use a Resource Access Management (RAM) user to call API operations. Before using a RAM user to call an API operation, you must grant the RAM user the corresponding permission to call the API by creating an authorization policy and attaching the policy to the RAM user. API signature To ensure secure calls to the API, Alibaba Cloud authenticates each API request through the signature. When you manually make an API request, you need to use AccessKey Secret to calculate the signature, that is, the hash-based message authentication code (HMAC) value, based on the encoded and sorted request string. For more information, see the definition in RFC 2104. This topic uses the raw access parameters in the following table to describe how to create an API signature.

| Parameter | Description |
|---|---|
| Access point | http://semawaf.[ RegionId].example.com/? |
| API-specific parameters | Action=DescribeFeatures |
| Common parameters (excluding the Signature parameter) | &Timestamp=2016-02-23T12:46:24Z &Format=JSON &AccessKeyId=<yourAccessKeyId> &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2018-01-16 &SignatureVersion=1.0 |
| AccessKey secret | <yourAccessKeySecret> |

1. Use the request parameters to construct a canonicalized query string.
Not e The request parameters include common request parameters (excluding the Signature parameter) and API-specific parameters. i. Sort the parameters. Sort the request parameters in alphabetical order. ii. Encode the parameters. Use UTF-8 to URL-encode the parameter names and values. The encoding rules are as follows: Letters, digits, hyphens (-), underscores (_), periods (.), and tildes (~) are not encoded. Other characters are encoded in the %XY format, where XY is the hexadecimal representation of the character in ASCII. For example, the double quotation mark (") is encoded as %22. Extended UTF-8 characters are encoded in the %XY%ZA… format. Note that a space is encoded as %20, instead of a plus sign (+). iii. Connect the encoded parameter names and values with equal signs (=). iv. Then, sort the parameter name and value pairs connected by equal signs in alphabetical order, and connect them with ampersands (&) to produce the canonicalized query string.
2. Use the canonicalized query string to construct the string for signature calculation based on the
following rules:

```
StringToSign=HTTPMethod + “&” + percentEncode(“/”) + ”&” + percentEncode(CanonicalizedQueryString)
```

3. Calculate the HMAC value of the StringToSign string according to the definition in RFC 2104.
Not e The key used for signature calculation is your AccessKey secret adding the ampersand (&) (ASCII 38). Secure Hash Algorithm 1 (SHA1) is used as the hash algorithm.
4. Encode the preceding HMAC value into a string based on Base64 encoding rules to obtain the
signature value.

```
LEW8N4y7Uasop******
```

5. Set the Signature parameter in the request parameters to this signature value to sign the request.

#### 3.2.3 Common request parameters

The following table describes the common request parameters that are used to indicate information such as the API version and authentication information.

| Name | Type | Required | Description |
|---|---|---|---|
| Version | String | Yes | The API version in the format of YYYY- MM-DD. Set the value to 2018-01-16. |
| AccessKeyId | String | Yes | The key ID that Alibaba Cloud assigns to a user for service access. |
| Signature | String | Yes | The signature string. |
| SignatureMethod | String | Yes | The signature method. Set the value to HMAC-SHA1. |
| Timestamp | String | Yes | The timestamp of the request. Follow the ISO 8601 standard to specify the date and use the offset from Coordinated Universal Time (UTC) to specify the time zone. The format is YYYY-MM- DDThh:mm:ssZ . For example, 2014-05-26T12:00:00Z indicates 20:00:00 on May 26, 2014, Beijing time. |
| SignatureVersion | String | Yes | The signature algorithm version. Set the value to 1.0. |

|   |   | YYYY-MM- |
|---|---|---|
|   | DDThh:mm:ssZ |   |

| psara Stack Security |   |   | Developer Guide·Threat Detection Service (TDS |
|---|---|---|---|

| Name | Type | Required | Description |
|---|---|---|---|
| SignatureNonce | String | Yes | The unique random number used to prevent network replay attacks. You must use different random numbers for different requests. |
| ResourceOwnerAc count | String | No | The owner account of the resource to be accessed through this API request, that is, the logon username. |
| Format | String | No | The format of the response. Set the value to JSON or XML. Not e Default value: XML. |

#### 3.2.4 Response structure

Apsara Stack Security API responses support both the XML and JSON formats. The system always returns a unique identification code RequestId each time you send a request to call an operation, no matter whether the call is successful or not. Sample responses (XML format)

```xml
<? xml version="1.0" encoding="UTF-8"? > <! -- The root node of the result --> <Operation name+Response>
    <! -- Returned request ID -->
    <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
    <! -- Returned data -->
</Operation name+Response>
```

Sample responses (JSON format)

```json
"RequestId": "4C467B38-3910-447D-87BC-AC049166F216", /* Returned data */
```

### 3.3 Asset management

#### 3.3.1 DescribeAllEntity

Queries information about all assets, such as asset group IDs and asset names.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAllEntity | The operation that you want to perform. Set the value to DescribeAllEntity. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | The ID of the request. |
| EntityList | Array | - | The list of instances. |
| GroupId | Integer | 281801 | The ID of the group. |
| InstanceName | String | wasdsfasfdasfds | The name of the instance. |
| Ip | String | 10.0.0.183 | The IP address of the server. |
| Uuid | String | edc897d6-xxxxx- xxxxx-xxxxx-xxxxx | The UUID of the server. |
| InternetIp | String | 101.202.20.20 | The public IP address of the server. |
| IntranetIp | String | 10.10.10.10 | The private IP address of the server. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeAllEntity
```

Sample success responses `XML` format

```xml
<code>200</code> <data>
    <EntityList>
        <InstanceName>wasdsfasfdasfds</InstanceName>
        <Uuid>edc897d6-xxxxx-xxxxx-xxxxx-xxxxx</Uuid>
        <IntranetIp>10.10.10.10</IntranetIp>
        <InternetIp>101.202.20.20</InternetIp>
        <Ip>10.0.0.183</Ip>
        <GroupId>281801</GroupId>
    </EntityList>
</data> <requestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</requestId>
```

`JSON` format

```json
  "code": 200,
  "data": {
    "EntityList": [{
      "InstanceName": "wasdsfasfdasfds",
      "Uuid": "edc897d6-xxxxx-xxxxx-xxxxx-xxxxx",
      "IntranetIp": "10.10.10.10",
      "InternetIp": "101.202.20.20",
      "Ip": "10.0.0.183",
      "GroupId": 281801
```

`}]` `},`

```json
  "requestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F"
```

For a list of error codes, see Error codes.

#### 3.3.2 DescribeFieldStatistics

Queries statistics of the assets.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeFieldStati stics | The operation that you want to perform. Set the value to DescribeFieldStatistics. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| MachineTypes | String | No | ecs | The types of the assets. If the asset type is not specified, the statistics of all types of assets are queried. ecs: an ECS instance cloud product : a cloud service _ |

| Parameter | Type | Example | Description |
|---|---|---|---|
| GroupedFields | - | - | The asset information. |
| GroupCount | Integer | 20 | The number of server groups. |
| InstanceCount | Integer | 100 | The total number of assets. |
| NewInstanceCo unt | Integer | 10 | The number of new servers. |
| NotRunningStat usCount | Integer | 10 | The number of servers that are not started. |
| OfflineInstance Count | Integer | 21 | The number of offline servers. |
| RegionCount | Integer | 11 | The number of regions to which the servers belong. |
| RiskInstanceCou nt | Integer | 90 | The number of assets that are at risk. |
| UnprotectedIns tanceCount | Integer | 10 | The number of unprotected assets. |
| VpcCount | Integer | 5 | The number of VPCs. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeFieldStatistics
```

Sample success responses `XML` format

```xml
<DescribeFieldStatistics>
  <RequestId>20CB6B41-0ED9-4679-BF5D-B84B8F7E70FC</RequestId>
  <GroupedFields>
        <InstanceCount>216</InstanceCount>
        <GroupCount>3</GroupCount>
        <NewInstanceCount>11</NewInstanceCount>
        <VpcCount>109</VpcCount>
        <RiskInstanceCount>121</RiskInstanceCount>
        <OfflineInstanceCount>48</OfflineInstanceCount>
        <UnprotectedInstanceCount>48</UnprotectedInstanceCount>
        <RegionCount>25</RegionCount>
        <NotRunningStatusCount>9</NotRunningStatusCount>
  </GroupedFields>
</DescribeFieldStatistics>
```

`JSON` format

```json
 "RequestId":"20CB6B41-0ED9-4679-BF5D-B84B8F7E70FC",
 "GroupedFields":{
  "InstanceCount":216,
  "NewInstanceCount":11,
  "GroupCount":3,
  "VpcCount":109,
  "RiskInstanceCount":121,
  "UnprotectedInstanceCount":48,
  "OfflineInstanceCount":48,
  "RegionCount":25,
  "NotRunningStatusCount":9
```

For a list of error codes, see Error codes.

#### 3.3.3 DescribeGroupedTags

Queries the statistics of asset tags.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeGrouped Tags | The operation that you want to perform. Set the value to DescribeGroupedTags. |
| MachineTypes | String | No | ecs | The types of the assets. If the asset type is not specified, the statistics of all asset tags are queried. ecs: an ECS instance cloud product : a cloud service _ |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 2 | The number of entries returned on the current page. |
| GroupedFileds | Array |   | The statistics of the asset tag. |
| Count | String | 2 | The number of assets to which a tag attaches. |
| Name | String | test | The name of the tag. |
| TagId | Integer | 8704 | The ID of the tag. |
| HttpStatusCod e | Integer | 200 | The HTTP status code of the returned results. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. t rue: successful f alse: failed |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeGroupedTags
```

Sample success responses `XML` format

```xml
<DescribeGroupedTags>
  <HttpStatusCode>200</HttpStatusCode>
  <Count>1</Count>
  <RequestId>DD5AFF52-0827-4FC9-B6EA-B233FF3AFF91</RequestId>
  <Success>true</Success>
  <GroupedFileds>
        <Name>test</Name>
        <Count>167</Count>
        <TagId>8704</TagId>
  </GroupedFileds>
</DescribeGroupedTags>
```

`JSON` format

```json
 "HttpStatusCode":200,
 "Count":1,
 "RequestId":"DD5AFF52-0827-4FC9-B6EA-B233FF3AFF91",
 "Success":true,
 "GroupedFileds":[
   "Name":"test",
   "Count":"167",
   "TagId":8704
```

`]` For a list of error codes, see Error codes.

#### 3.3.4 DescribeAllGroups

Queries the grouping information about servers.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAllGroup s | The operation that you want to perform. Set the value to DescribeAllGroups. |

| S | Developer Guide·Thre ervice (TDS) | at Detection |   |   | Apsara Stack Securit | y |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 2 | The number of entries returned on the current page. |
| Groups | Array |   | The grouping information about the servers. |
| GroupFlag | Integer | 1 | The type of the server group. 0: default group 1: other groups |
| GroupId | Integer | 8834224 | The ID of the server group. |
| GroupName | String | test | The name of the server group. |
| RequestId | String | "requestId": "7E0618A9-D5EF- 4220-9471- C42B5E92719F", | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeAllGroups
```

Sample success responses `XML` format

```xml
<DescribeAllGroups>
  <Groups>
        <GroupFlag>0</GroupFlag>
        <GroupName>Ungrouped</GroupName>
        <GroupId>4120080</GroupId>
  </Groups>
  <Groups>
        <GroupFlag>1</GroupFlag>
        <GroupName>leaves</GroupName>
        <GroupId>8831497</GroupId>
  </Groups>
  <Groups>
        <GroupFlag>1</GroupFlag>
        <GroupName>test</GroupName>
        <GroupId>8834224</GroupId>
  </Groups>
  <Count>3</Count>
  <RequestId>9DD4B19B-CA32-41DA-AED7-77B4F84A91D5</RequestId>
</DescribeAllGroups>
```

`JSON` format

```json
 "Groups":[
   "GroupFlag":0,
   "GroupName":"Ungrouped",
   "GroupId":4120080
```

`},`

```json
   "GroupFlag":1,
   "GroupName":"leaves",
   "GroupId":8831497
```

`},`

```json
   "GroupFlag":1,
   "GroupName":"test",
   "GroupId":8834224
```

`],`

```json
 "Count":3,
 "RequestId":"9DD4B19B-CA32-41DA-AED7-77B4F84A91D5"
```

For a list of error codes, see Error codes.

#### 3.3.5 DeleteGroup

Deletes a server group.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteGroup | The operation that you want to perform. Set the value to Delet eGroup. |
| GroupId | Long | Yes | 11111 | The ID of the server group. Not e To delete a server group, you must provide the ID of the server group. You can call the DescribeAllGroups operation to obtain the ID. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteGroup &GroupId=1111
```

Sample success responses `XML` format

```xml
<DeleteGroup>
      <code>200</code>
      <requestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</requestId>
      <success>true</success>
    </DeleteGroup>
```

`JSON` format

```json
  "code": 200,
  "requestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F",
  "success": true
```

For a list of error codes, see Error codes.

#### 3.3.6 CreateOrUpdateAssetGroup

Modifies the relationship between an asset and an asset group. For example, you can modify the group to which the asset belongs or the list of assets.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateOrUpdateA ssetGroup | The operation that you want to perform. Set the value to Creat eOrUpdat eAsset Group. |
| Uuids | String | No | aq12-***,s23*** | The ID of the asset. Not e To modify the relationship between an asset and an asset group, you must provide the ID of the asset. You can call the DescribeCloudCenterInstances operation to obtain the ID. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| GroupName | String | No | test | The name of the asset group. Not e To modify the relationship between an asset and an asset group, you must provide the name of the asset group. You can call the DescribeAllGroups operation to obtain the name. If GroupId is not specified, you must specify GroupName. |
| GroupId | Long | No | 111111 | The ID of the asset group. Not e To modify the relationship between an asset and an asset group, you must provide the ID of the asset group. You can call the DescribeAllGroups operation to obtain the ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=CreateOrUpdateAssetGroup &GroupName=test
```

Sample success responses `XML` format

```xml
<CreateOrUpdateAssetGroupResponse>
  <RequestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</RequestId>
</CreateOrUpdateAssetGroupResponse>
```

`JSON` format

```json
  "RequestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F"
```

For a list of error codes, see Error codes.

#### 3.3.7 ModifyTagWithUuid

Modifies the relationship between tags and servers or cloud services.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyTagWithUu id | The operation that you want to perform. Set the value to Modif yT agWit hUuid. |
| TagList | String | Yes | ac,ad | The list of tags. Not e To modify the relationship between tags and assets, you must provide the list of tags. You can call the DescribeGroupedTags operation to obtain the list. |
| UuidList | String | No | 111-xx,aa-bb | The IDs of the assets. Not e To modify the relationship between tags and assets, you must provide the lDs of the assets. You can call the DescribeCloudCenterInstances operation to obtain the IDs. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TagId | String | No | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | The ID of the tag. Not e To modify the relationship between a tag and an asset, you must provide the ID of the tag. You can call the DescribeGroupedTags operation to obtain the ID. |
| MachineTypes | String | No | ecs | The types of the assets. Valid values: ecs: an ECS instance cloud product : a cloud service _ |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyTagWithUuid &TagList=ac,ad
```

Sample success responses `XML` format

```xml
<ModifyTagWithUuidResponse>
      <requestId>70C4B40D-D55E-4B7B-9992-8535E396B2F4</requestId>
</ModifyTagWithUuidResponse>
```

`JSON` format

```json
    "RequestId": "70C4B40D-D55E-4B7B-9992-8535E396B2F4"
```

For a list of error codes, see Error codes.

#### 3.3.8 DescribeInstanceStatistics

Queries risk information about an asset.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| From | String | Yes | sas | The source of the data. Set the value to sas. |
| Uuid | String | Yes | a51cec37-ed73- 4c53-b467-*** | The IDs of the assets. Separate multiple IDs with commas (,). Not e To query the risk information about an asset, you must provide the ID of the asset. You can call the DescribeCloudCenterInstances operation to obtain the ID. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | The ID of the request. |
| Data | Array |   | The risk information about the asset. |
| Uuid | String | us1233****** | The ID of the asset. |
| Account | Integer | 1 | The type of the asset group. Valid values: 0: default group 1: other groups |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Health | Integer | 1 | The number of issues detected by the baseline check. |
| Trojan | Integer | 1 | The number of trojans. |
| Suspicious | Integer | 2 | The number of alerts. |
| Vul | Integer | 4 | The total number of vulnerabilities: CveNum + EmgNum + SysNum + CmsNum + AppNum. |
| CveNum | Integer | 1 | The number of Linux software vulnerabilities. |
| EmgNum | Integer | 0 | The number of emergency vulnerabilities. |
| SysNum | Integer | 1 | The number of Windows vulnerabilities. |
| CmsNum | Integer | 2 | The number of Web CMS vulnerabilities. |
| AppNum | Integer | 0 | The number of application vulnerabilities. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeInstanceStatistics &From=sas &Uuid=a51cec37-ed73-4c53-b467-***
```

Sample success responses `XML` format

```xml
<DescribeInstanceStatisticsResponse>
  <Data>
        <SysNum>1</SysNum>
        <Uuid>a51cec37-ed73-4c53-b467-***</Uuid>
        <CveNum>1</CveNum>
        <Suspicious>1</Suspicious>
        <Trojan>0</Trojan>
        <Account>0</Account>
        <CmsNum>1</CmsNum>
        <EmgNum>1</EmgNum>
        <Health>0</Health>
        <AppNum>1</AppNum>
        <Vul>5</Vul>
  </Data>
  <Data>
        <SysNum>2</SysNum>
        <Uuid>33f107a3-4653-4228-a428-***</Uuid>
        <CveNum>1</CveNum>
        <Suspicious>2</Suspicious>
        <Trojan>0</Trojan>
        <Account>0</Account>
        <CmsNum>1</CmsNum>
        <EmgNum>2</EmgNum>
        <Health>0</Health>
        <AppNum>1</AppNum>
        <Vul>7</Vul>
  </Data>
  <RequestId>44AE72D4-2DDF-4CEC-9957-64C470CC90FC</RequestId>
</DescribeInstanceStatisticsResponse>
```

`JSON` format

```json
    "Data": [
            "SysNum": 1,
            "Uuid": "a51cec37-ed73-4c53-b467-***",
            "CveNum": 1,
            "Suspicious": 1,
            "Trojan": 0,
            "Account": 0,
            "CmsNum": 1,
            "EmgNum": 1,
            "Health": 0,
            "AppNum": 1,
            "Vul": 5
```

`},`

```json
            "SysNum": 2,
            "Uuid": "33f107a3-4653-4228-a428-***",
            "CveNum": 1,
            "Suspicious": 2,
            "Trojan": 0,
            "Account": 0,
            "CmsNum": 1,
            "EmgNum": 2,
            "Health": 0,
            "AppNum": 1,
            "Vul": 7
```

`],`

```json
    "RequestId": "44AE72D4-2DDF-4CEC-9957-64C470CC90FC"
```

For a list of error codes, see Error codes.

#### 3.3.9 DescribeCloudProductFieldStatistics

Queries the statistics of cloud services that are protected by Threat Detection Service.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCloudPro ductFieldStatistic s | The operation that you want to perform. Set the value to DescribeCloudProductFieldStatistics. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | The ID of the request. |
| GroupedFields | Struct |   | The statistics of cloud services that are protected by Threat Detection Service. |
| RiskInstanceCou nt | Integer | 90 | The number of assets that are at risk. |
| InstanceCount | Integer | 100 | The total number of assets. |
| CategoryCount | String | [{"MachineType":1," Count":11}] | The statistics of different types of assets. MachineT ype represents the type of the asset. Count represents the number of assets of a specific type. Valid values of MachineT ype: 1: Server Load Balancer 2: NAT Gateway 3: ApsaraDB for RDS 4: ApsaraDB for MongoDB |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCloudProductFieldStatistics
```

Sample success responses `XML` format

```xml
<DescribeCloudProductFieldStatistics>
      <code>200</code>
      <data>
            <GroupedFields>
                  <InstanceCount>100</InstanceCount>
                  <RiskInstanceCount>90</RiskInstanceCount>
                  <categoryCount>
                        <MachineType>1</MachineType>
                        <Count>11</Count>
                  </categoryCount>
            </GroupedFields>
      </data>
      <requestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</requestId>
      <success>true</success>
</DescribeCloudProductFieldStatistics>
```

`JSON` format

```json
  "code": 200,
  "data": {
    "GroupedFields": {
      "InstanceCount": 100,
      "RiskInstanceCount": 90,
      "categoryCount":[{"MachineType":1,"Count":11}]
```

`},`

```json
  "requestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F",
  "success": true
```

For a list of error codes, see Error codes.

#### 3.3.10 DescribeDomainCount

Queries the number of domain assets.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDomainC ount | The operation that you want to perform. Set the value to DescribeDomainCount. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6FAFB857-FE24- 4226-A09F- 52EA5023C987 | The ID of the request. |
| RootDomainsC ount | Integer | 27 | The number of returned root domains. |
| TotalDomainsC ount | Integer | 1 | The number of subdomains. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeDomainCount
```

Sample success responses `XML` format

```xml
<DescribeDomainCount>
   <code>200</code>
   <data>
      <TotalDomainsCount>27</TotalDomainsCount>
      <RootDomainsCount>1</RootDomainsCount>
   </data>
   <requestId>6FAFB857-FE24-4226-A09F-52EA5023C987</requestId>
   <success>true</success>
    </DescribeDomainCount>
```

`JSON` format

```json
 "requestId":"6FAFB857-FE24-4226-A09F-52EA5023C987",
 "data":{
  "TotalDomainsCount":27,
  "RootDomainsCount":1
```

`},`

```json
 "code":200,
 "success":true
```

For a list of error codes, see Error codes.

#### 3.3.11 DescribeDomainList

Queries information about domain assets.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| FuzzyDomain | String | No | sas | The information used to query domains by fuzzy match. |
| DomainType | String | No | root | The type of the domain. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0B48AB3C-84FC- 424D-A01D- B9270EF46038 | The ID of the request. |
| DomainListResp onseList | Array |   | The information about the domain asset. |
| Domain | String | tst.com | The name of the domain or website. |
| IpList | String | 1.2.3.4,1.2.3.5 | The list of IP addresses that correspond to the domain. |
| PageInfo | Struct |   | The page information. |
| Count | Integer | 10 | The number of entries returned on the current page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| TotalCount | Integer | 27 | The total number of entries in the list of domain assets. |

|   |   |   | Developer Guide·Threat Detection |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| CurrentPage | Integer | 1 | The page number of the current page. |

Sample requests

```
http(s)://[Endpoint]/? Action=DescribeDomainList
```

Sample success responses `XML` format

```xml
<DomainListResponseList>
    <Domain>tst.com</Domain>
</DomainListResponseList> <DomainListResponseList>
    <Domain>p.tst.com</Domain>
</DomainListResponseList> <DomainListResponseList>
    <IpList>1.2.3.4,1.2.3.5</IpList>
    <Domain>b.tst.com</Domain>
</DomainListResponseList> <DomainListResponseList>
    <Domain>r.tst.com</Domain>
</DomainListResponseList> <DomainListResponseList>
    <Domain>t.tst.com</Domain>
</DomainListResponseList> <DomainListResponseList>
    <Domain>k.tst.com</Domain>
</DomainListResponseList> <DomainListResponseList>
    <Domain>{a.tst.com</Domain>
</DomainListResponseList> <DomainListResponseList>
    <Domain>w.tst.com</Domain>
</DomainListResponseList> <DomainListResponseList>
    <Domain>l.tst.com</Domain>
</DomainListResponseList> <DomainListResponseList>
    <Domain>v.tst.com</Domain>
</DomainListResponseList> <PageInfo>
    <TotalCount>27</TotalCount>
    <PageSize>10</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>10</Count>
</PageInfo> <requestId>0B48AB3C-84FC-424D-A01D-B9270EF46038</requestId>
```

`JSON` format

```json
    "DomainListResponseList":[
            "Domain":"tst.com"
```

`},`

```json
            "Domain":"p.tst.com"
```

`},`

```json
            "IpList":"1.2.3.4,1.2.3.5",
            "Domain":"b.tst.com"
```

`},`

```json
            "Domain":"r.tst.com"
```

`},`

```json
            "Domain":"t.tst.com"
```

`},`

```json
            "Domain":"k.tst.com"
```

`},`

```json
            "Domain":"{a.tst.com"
```

`},`

```json
            "Domain":"w.tst.com"
```

`},`

```json
            "Domain":"l.tst.com"
```

`},`

```json
            "Domain":"v.tst.com"
```

`],`

```json
    "PageInfo":{
        "TotalCount":27,
        "PageSize":10,
        "CurrentPage":1,
        "Count":10
```

`},`

```json
    "requestId":"0B48AB3C-84FC-424D-A01D-B9270EF46038"
```

For a list of error codes, see Error codes.

#### 3.3.12 DescribeDomainDetail

Queries details about a domain asset.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDomainD etail | The operation that you want to perform. Set the value to DescribeDomainDet ail. |
| DomainName | String | Yes | *.test.com | The name of the domain or website. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 3A85CFCF-05C8- 451A-9E41- C0D5E96BA407 | The ID of the request. |
| Domain | String | b.tst.com | The name of the returned domain. |
| RootDomain | String | tst.com | The name of the root domain that corresponds to the returned domain. |
| DomainDetailIte ms | Array |   | The details about the domain asset. |
| InternetIp | String | 1.2.3.1 | The public IP address of the asset instance. |
| InstanceId | String | i- m5e6w7dzsktt6mz4 yime | The ID of the asset instance. |
| Uuid | String | lb- bp1g9dohoyin9cjhn 6itt | The UUID of the asset instance. |
| AssetType | String | 0 | The type of the asset. Valid values: 0: Elastic Compute Service (ECS) instance 1: Server Load Balancer 2: NAT Gateway 3: ApsaraDB for RDS 4: ApsaraDB for MongoDB |

| Parameter | Type | Example | Description |
|---|---|---|---|
| InstanceName | String | iZm5e6w7dzsktt6m z4yimeZ-60288 | The name of the asset. |
| IntranetIp | String | 1.2.3.2 | The private IP address of the asset. |

Sample requests

```
http(s)://[Endpoint]/? Action=DescribeDomainDetail &DomainName=*.test.com
```

Sample success responses `XML` format

```xml
<DescribeDomainDetailResponse>
  <Domain>b.***tst.com</Domain>
  <DomainDetailItems>
        <InstanceName>iZm5e6***</InstanceName>
        <AssetType>0</AssetType>
        <Uuid>d664e15e-488b-4f3c-a80f-***</Uuid>
        <InternetIp>1.2.3.1</InternetIp>
        <InstanceId>i-m5e***e</InstanceId>
        <IntranetIp>1.2.3.2</IntranetIp>
  </DomainDetailItems>
  <DomainDetailItems>
        <InstanceName>iZ***</InstanceName>
        <AssetType>0</AssetType>
        <Uuid>0d804403-8d36-4642-a5f1-***</Uuid>
        <InternetIp>1.2.3.3</InternetIp>
        <InstanceId>i-m5ehn8ugwvsp2k4xdzok</InstanceId>
        <IntranetIp>1.2.3.5</IntranetIp>
  </DomainDetailItems>
  <DomainDetailItems>
        <AssetType>2</AssetType>
        <Uuid>eip-wz9***</Uuid>
        <InternetIp>1.2.3.6</InternetIp>
        <InstanceId>eip-wz9***</InstanceId>
  </DomainDetailItems>
  <DomainDetailItems>
        <InstanceName>***test</InstanceName>
        <AssetType>1</AssetType>
        <Uuid>lb-bp***</Uuid>
        <InternetIp>1.2.3.7</InternetIp>
        <InstanceId>lb-bp***</InstanceId>
  </DomainDetailItems>
  <RootDomain>***tst.com</RootDomain>
  <requestId>3A85CFCF-05C8-451A-9E41-C0D5E96BA407</requestId>
</DescribeDomainDetailResponse>
```

`JSON` format

```json
    "Domain":"b.***tst.com",
    "DomainDetailItems":[
                "InstanceName":"iZm5e6***",
                "AssetType":"0",
                "Uuid":"d664e15e-488b-4f3c-a80f-***",
                "InternetIp":"1.2.3.1",
                "InstanceId":"i-m5e***e",
                "IntranetIp":"1.2.3.2"
```

`},`

```json
                "InstanceName":"iZ***",
                "AssetType":"0",
                "Uuid":"0d804403-8d36-4642-a5f1-***",
                "InternetIp":"1.2.3.3",
                "InstanceId":"i-m5ehn8ugwvsp2k4xdzok",
                "IntranetIp":"1.2.3.5"
```

`},`

```json
                "AssetType":"2",
                "Uuid":"eip-wz9***",
                "InternetIp":"1.2.3.6",
                "InstanceId":"eip-wz9***"
```

`},`

```json
                "InstanceName":"***test",
                "AssetType":"1",
                "Uuid":"lb-bp***",
                "InternetIp":"1.2.3.7",
                "InstanceId":"lb-bp***"
```

`],`

```json
    "RootDomain":"***tst.com",
    "requestId":"3A85CFCF-05C8-451A-9E41-C0D5E96BA407"
```

For a list of error codes, see Error codes.

#### 3.3.13 DescribeCloudCenterInstances

Queries the asset information on the Assets page, such as the name and region of an asset instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCloudCen terInstances | The operation that you want to perform. Set the value to DescribeCloudCenterInstances. |
| Criteria | String | No | [{"name":"riskSta tus","value":"YES "}, {"name":"internet Ip","value":"1.2."} ] | Specifies the search conditions, such as instance IDs, instance names, VPC IDs, regions, and IP addresses. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| LogicalExp | String | No | OR | The logical relationship between search conditions. Valid values: OR: The logical relationship between search conditions is OR. AND: The logical relationship between search conditions is AND. |
| MachineTypes | String | No | ecs | The type of the asset. ecs: an Elastic Compute Service (ECS) instance cloud product : a cloud service _ |
| NoPage | Boolean | No | true | Specifies whether to enable paged query. Valid values: t rue: enables paged query. f alse: disables paged query. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Instances | Array |   | The asset details. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AlarmStatus | String | NO | Indicates whether alerts are configured for the asset instance. Valid values: YES NO |
| AssetType | String | ecs | The type of the asset. |
| ClientStatus | String | online | Indicates whether the asset instance is protected by the agent. Valid values: online: The protection status of the asset is Enabled. of f line: The protection status of the asset is Disabled. pause: The protection status of the asset is Paused. |
| Flag | Integer | 0 | Indicates whether the asset instance is provided by Alibaba Cloud. Valid values: 0: The asset instance is provided by Alibaba Cloud. 1: The asset instance is not provided by Alibaba Cloud. |
| GroupId | String | 4120080 | The ID of the group to which the asset instance belongs. |
| HcStatus | String | YES | Indicates whether the asset instance is exposed to baseline risks. Valid values: YES NO |
| HealthCheckCo unt | Integer | 1 | The number of issues that are detected in baseline checks. |
| InstanceId | String | i-m5*** | The ID of the asset instance. |
| InstanceName | String | yztest-l*** | The name of the asset instance. |
| InternetIp | String | 1.2.3.4 | The public IP address of the asset instance. |

| eveloper Guide·Th | reat Detection |   | Apsara Stack Securit |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| IntranetIp | String | 1.2.3.0 | The private IP address of the asset instance. |
| Ip | String | 1.2.3.4 | The public IP address of the asset instance. |
| Os | String | Linux | The operating system of the asset instance. |
| OsName | String | CentOS 7.6 64-bit | The kernel version of the asset instance. |
| Region | String | cn-hangzhou-cm***- *** | The region where the asset instance is deployed. |
| RegionId | String | cn-hanghzou | The ID of the region where the asset instance is deployed. |
| RegionName | String | China (Qingdao) | The name of the region where the asset instance is deployed. |
| RiskStatus | String | NO | Indicates whether the asset instance is exposed to security risks. Valid values: YES NO |
| SafeEventCount | Integer | 5 | The number of alerts detected on the asset instance. |
| Status | String | Running | The status of the asset instance. Valid values: Running: The instance is running. not Running: The instance is not running. |
| Tag | String | InternetIp | The tag of the asset instance. |
| Uuid | String | c9107c04-942f- 40c1-981a-f1c1*** | The ID of the asset instance. |
| VpcInstanceId | String | classic | The ID of the VPC to which the asset instance belongs. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| VulCount | Integer | 2 | The number of vulnerabilities detected on the asset instance. |
| VulStatus | String | YES | Indicates whether the asset instance is exposed to vulnerabilities. Valid values: YES NO |
| PageInfo |   |   | The page information. |
| Count | Integer | 10 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| TotalCount | Integer | 50 | The total number of entries. |
| RequestId | String | 32A73759-4C0F- 4801-BE98- 901223ACEE9A | The ID of the request. |
| Success | Boolean | true | Indicates whether the request is successful. t rue: successful f alse: failed |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCloudCenterInstances
```

Sample success responses `XML` format

```xml
<DescribeCloudCenterInstances>
  <RequestId>32A73759-4C0F-4801-BE98-901223ACEE9A</RequestId>
  <PageInfo>
        <Count>0</Count>
        <TotalCount>691</TotalCount>
```

```xml
        <PageSize>20</PageSize>
        <CurrentPage>1</CurrentPage>
  </PageInfo>
  <Instances>
        <RiskStatus>NO</RiskStatus>
        <Uuid>88f7ce77-595e-4580-b655-3***</Uuid>
        <Ip>1.2.3.4</Ip>
        <Flag>0</Flag>
        <RegionName>China (Hangzhou)</RegionName>
        <OsName>CentOS 7.6 64-bit</OsName>
        <AssetType>0</AssetType>
        <InstanceId>i-m5e50***</InstanceId>
        <InternetIp>1.2.3.4</InternetIp>
        <HealthCheckCount>0</HealthCheckCount>
        <HcStatus>NO</HcStatus>
        <Os>linux</Os>
        <ClientStatus>online</ClientStatus>
        <Status>Running</Status>
        <Region>cn-hangzhou-cm***-***</Region>
        <VpcInstanceId>classic</VpcInstanceId>
        <VulStatus>NO</VulStatus>
        <Tag>InternetIp</Tag>
        <RegionId>cn-hangzhou</RegionId>
        <IntranetIp>1.2.3.0</IntranetIp>
        <AlarmStatus>NO</AlarmStatus>
        <VulCount>0</VulCount>
        <SafeEventCount>0</SafeEventCount>
        <InstanceName>yztest-l***</InstanceName>
  </Instances>
  <Instances>
        <RiskStatus>NO</RiskStatus>
        <Uuid>7a4735d6-75a4-4555-a18f-b***</Uuid>
        <Ip>1.2.3.4</Ip>
        <Flag>0</Flag>
        <RegionName>China (Hangzhou)</RegionName>
        <OsName>CentOS 7.6 64-bit</OsName>
        <AssetType>0</AssetType>
        <InstanceId>i-m5e5***</InstanceId>
        <InternetIp>1.2.3.4</InternetIp>
        <HealthCheckCount>0</HealthCheckCount>
        <HcStatus>NO</HcStatus>
        <Os>linux</Os>
        <ClientStatus>online</ClientStatus>
        <Status>Running</Status>
        <Region>cn-hangzhou-cm***-***</Region>
        <VpcInstanceId>classic</VpcInstanceId>
        <VulStatus>NO</VulStatus>
        <Tag>InternetIp</Tag>
        <RegionId>cn-hangzhou</RegionId>
        <IntranetIp>1.2.3.0</IntranetIp>
        <AlarmStatus>NO</AlarmStatus>
        <VulCount>0</VulCount>
        <SafeEventCount>0</SafeEventCount>
        <InstanceName>yztest-l***</InstanceName>
</I
```

`t` `>`

```xml
  </Instances>
  <Success>true</Success>
</DescribeCloudCenterInstances>
```

`JSON` format

```json
 "RequestId":"32A73759-4C0F-4801-BE98-901223ACEE9A",
 "Instances":[
   "RiskStatus":"NO",
   "Uuid":"88f7ce77-595e-4580-b655-3***",
   "Ip":"1.2.3.4",
   "Flag":0,
   "RegionName":"China (Hangzhou)",
   "OsName":"CentOS 7.6 64-bit",
   "AssetType":"0",
   "InstanceId":"i-m5e50***",
   "InternetIp":"1.2.3.4",
   "HealthCheckCount":0,
   "HcStatus":"NO",
   "Os":"linux",
   "Status":"Running",
   "ClientStatus":"online",
   "Region":"cn-hangzhou-cm***-***",
   "VpcInstanceId":"classic",
   "Tag":"InternetIp",
   "VulStatus":"NO",
   "IntranetIp":"1.2.3.0",
   "RegionId":"cn-hangzhou",
   "AlarmStatus":"NO",
   "VulCount":0,
   "InstanceName":"yztest-l***",
   "SafeEventCount":0
```

`},`

```json
   "RiskStatus":"NO",
   "Uuid":"7a4735d6-75a4-4555-a18f-b***",
   "Ip":"1.2.3.4",
   "Flag":0,
   "RegionName":"China (Hangzhou)",
   "OsName":"CentOS 7.6 64-bit",
   "AssetType":"0",
   "InstanceId":"i-m5e5***",
   "InternetIp":"1.2.3.4",
   "HealthCheckCount":0,
   "HcStatus":"NO",
   "Os":"linux",
   "Status":"Running",
   "ClientStatus":"online",
   "Region":"cn-hangzhou-cm***-***",
   "VpcInstanceId":"classic",
   "Tag":"InternetIp",
   "VulStatus":"NO",
```

```json
   "IntranetIp":"1.2.3.0",
   "RegionId":"cn-hangzhou",
   "AlarmStatus":"NO",
   "VulCount":0,
   "InstanceName":"yztest-l***",
   "SafeEventCount":0
```

`],`

```json
 "PageInfo":{
  "Count":0,
  "TotalCount":691,
  "PageSize":20,
  "CurrentPage":1
```

`},`

```json
 "Success":true
```

For a list of error codes, see Error codes.

#### 3.3.14 DescribeSummaryInfo

Queries the security information about an asset, such as the security score and the numbers of protected and unprotected assets.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSummary Info | The operation that you want to perform. Set the value to DescribeSummaryInfo. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AegisClientOffli neCount | Integer | 12 | The number of unprotected assets. |

| psara Stack Securi | ty |   | Developer Guide·Threat Detection |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| AegisClientOnli neCount | Integer | 127 | The number of protected assets. |
| RequestId | String | D40198E1-6EA8- 482E-B3C7- D9573D75C0CA | The ID of the request. |
| SecurityScore | Integer | 44 | The security score of assets. Valid values: 95 to 100: The assets are secure. 85 to 94: The assets are exposed to a few security risks. We recommend that you reinforce your security system as soon as possible. 70 to 84: The assets are exposed to many security risks. We recommend that you reinforce your security system as soon as possible. 69 or lower: The current security system is unable to protect the assets against attacker intrusions. We recommend that you reinforce your security system as soon as possible. |
| Success | Boolean | true | Indicates whether the request is successful. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSummaryInfo
```

Sample success responses `XML` format

```xml
<DescribeSummaryInfo>
  <SecurityScore>44</SecurityScore>
  <AegisClientOnlineCount>127</AegisClientOnlineCount>
  <RequestId>D40198E1-6EA8-482E-B3C7-D9573D75C0CA</RequestId>
  <Success>true</Success>
  <AegisClientOfflineCount>12</AegisClientOfflineCount>
</DescribeSummaryInfo>
```

`JSON` format

```json
 "AegisClientOnlineCount":127,
 "SecurityScore":44,
 "RequestId":"D40198E1-6EA8-482E-B3C7-D9573D75C0CA",
 "Success":true,
 "AegisClientOfflineCount":12
```

For a list of error codes, see Error codes.

#### 3.3.15 DescribeSearchCondition

Queries the filter conditions of specified assets.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSearchCo ndition | The operation that you want to perform. Set the value to DescribeSearchCondition |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| Type | String | No | ecs | The type of the asset that you want to query. Valid values: ecs: ECS instances cloud product : cloud services _ |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 3AEC47AF-8CFA- 485E-AC9A- 3A8ABC06EA7F | The ID of the request. |
| ConditionList | Array |   | The information about the filter conditions. |

| psara Stack Securi | ty |   | Developer Guide·Threat Detection Service (TDS |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Name | String | Running | The name of the condition. |
| FilterConditions | String | {\"filterParams\": [{\"labelKey\":\"a\|b\ ",\"value\":\" {\\\"name\\\":\\\"s adsasd\\\",\\\"valu e\\\":\\\"dasdsdas \\\"}\"}],\"LogicalEx p\":\"OR\"} | Filter conditions. |
| NameKey | String | stop machine _ | The key of the condition name. |
| ConditionType | String | system | The type of the filter condition. Valid values: syst em: default filter conditions user: custom filter conditions |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSearchCondition
```

Sample success responses `XML` format

```xml
<code>200</code> <data>
    <ConditionList>
        <FilterConditions>{"filterParams":[{"labelKey":"aaaaaaaa|bbbbbbb","value":"{\"name\
":\"sadsasd\",\"value\":\"dasdsdas\"}"}],"LogicalExp":"OR"}</FilterConditions>
        <ConditionType>system</ConditionType>
        <NameKey>stop_machine</NameKey>
    </ConditionList>
    <ConditionList>
        <FilterConditions>{"filterParams":[{"labelKey":"aaaaaaaa|bbbbbbb","value":"{\"name\
":\"sadsasd\",\"value\":\"dasdsdas\"}"}],"LogicalExp":"OR"}</FilterConditions>
        <ConditionType>system</ConditionType>
        <NameKey>new_machine_has_risk</NameKey>
    </ConditionList>
    <ConditionList>
        <FilterConditions>{"filterParams":[{"label":"At risk or not: At risk","value":"{\"n
ame\":\"aaaaaa\",\"value\":\"YES\"}"}],"LogicalExp":"OR"}</FilterConditions>
        <ConditionType>user</ConditionType>
        <Name>Running</Name>
    </ConditionList>
</data> <requestId>3AEC47AF-8CFA-485E-AC9A-3A8ABC06EA7F</requestId>
```

`JSON` format

```json
  "code": 200,
  "data": {
    "ConditionList": [
        "FilterConditions": "{\"filterParams\":[{\"labelKey\":\"aaaaaaaa|bbbbbbb\",\"value\
":\"{\\\"name\\\":\\\"sadsasd\\\",\\\"value\\\":\\\"dasdsdas\\\"}\"}],\"LogicalExp\":\"OR\" }",
        "ConditionType": "system",
        "NameKey": "stop_machine"
```

`},`

```json
        "FilterConditions": "{\"filterParams\":[{\"labelKey\":\"aaaaaaaa|bbbbbbb\",\"value\
":\"{\\\"name\\\":\\\"sadsasd\\\",\\\"value\\\":\\\"dasdsdas\\\"}\"}],\"LogicalExp\":\"OR\" }",
        "ConditionType": "system",
        "NameKey": "new_machine_has_risk"
```

`},`

```json
        "FilterConditions": "{\"filterParams\":[{\"label\":\"At risk or not: At risk\",\"va
lue\":\"{\\\"name\\\":\\\"aaaaaa\\\",\\\"value\\\":\\\"YES\\\"}\"}],\"LogicalExp\":\"OR\"}"
```

`,`

```json
        "ConditionType": "user",
        "Name": "Running"
```

`]` `},`

```json
  "requestId": "3AEC47AF-8CFA-485E-AC9A-3A8ABC06EA7F"
```

For a list of error codes, see Error codes

#### 3.3.16 DescribeAssetDetailByUuid

Queries details and extended information about a server based on its UUID.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAssetDet ailByUuid | The operation that you want to perform. Set the value to DescribeAssetDetailByUuid. |
| Uuid | String | Yes | 123213-13dwe- 2412431-dafadfa | The UUID of the server. |

| D S | eveloper Guide·Thre ervice (TDS) | at Detection |   |   | Apsara Stack Securit | y |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F7BA0B6C-4D33- 49A7-AB7B- A221B2E40817 | The ID of the request. |
| AssetDetail | Struct |   | The details of the server. |
| InternetIp | String | 10.10.10.10 | The public IP address of the server. |
| IntranetIp | String | 10.0.0.211 | The internal IP address of the server. |
| InstanceName | Integer | 1312412341 | The name of the server. |
| InstanceId | Integer | 1234124124 | The ID of the server. |
| Ip | String | 10.10.10.101 | The IP address of the ECS instance. |
| Uuid | String | 1234214-ujuj- weqweq-111-vbbbb | The UUID of the server. |
| AssetType | String | 0 | The type of the server. |
| Os | String | linux | The type of the operating system. |
| ClientStatus | String | online | The status of the agent. |
| Region | String | shanghaixxxxxx | The region where the server is deployed. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RegionName | String | China (Shanghai) | The name of the region. |
| Tag | String | InternetIp | The tag attached to the server. |
| GroupTrace | String | Ungrouped | The grouping information. |
| Cpu | Integer | 2 | The number of CPU cores. |
| CpuInfo | String | Intel(R) Xeon(R) Platinum 8163 CPU @ 2.50GHz | The CPU details. |
| Kernel | String | 4.18.0- 80.11.2.el8 0.x86 64 _ _ | The kernel version. |
| OsDetail | String | Linux 64bit | The operating system version and architecture. |
| Mem | Integer | 0 | The memory size. |
| SysInfo | String | CentOS Linux 8.0.1905 | The operating system. |
| HostName | String | qewrqwerqsadas | The hostname. |
| OsName | String | CentOS 8.0 64-bit | The name of the operating system. |
| VpcInstanceId | String | i-xxxx-xxxx-xxxxx- xxxxx | The ID of the VPC. |
| OsName | String | CentOS 8.0 64-bit | The name of the operating system. |
| IpList | List | [ "10.0.0.123" ] | The IP address of the host. |
| MacList | List | [ "00:11:3e:20:38" ] | The Media Access Control (MAC) address of the host. |
| DiskInfoList | List | [ { "diskName": "/dev/vda1", "totalSize": 20, "useSize": 2 } ] | The disk information. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeAssetDetailByUuid
```

Sample success responses `XML` format

```xml
<code>200</code> <data>
    <AssetDetail>
        <GroupName>Ungrouped</GroupName>
        <ClientStatus>online</ClientStatus>
        <Os>linux</Os>
        <InstanceId>rqreqwrq</InstanceId>
        <IpList>10.0.0.123</IpList>
        <CpuInfo>Intel(R) Xeon(R) Platinum 8163 CPU @ 2.50GHz</CpuInfo>
        <Ip>10.10.10.101</Ip>
        <OsName>CentOS 8.0 64-bit</OsName>
        <Cpu>2</Cpu>
        <SysInfo>CentOS Linux 8.0.1905</SysInfo>
        <OsDetail>Linux 64bit</OsDetail>
        <IntranetIp>10.0.0.211</IntranetIp>
        <DiskInfoList>
            <diskName>/dev/vda1</diskName>
            <totalSize>20</totalSize>
            <useSize>2</useSize>
        </DiskInfoList>
        <MacList>00:11:3e:20:38</MacList>
        <InstanceName>wqreqwerqwer</InstanceName>
        <AssetType>0</AssetType>
        <Uuid>1234214-ujuj-weqweq-111-vbbbb</Uuid>
        <Mem>8</Mem>
        <InternetIp>10.10.10.10</InternetIp>
        <RegionName>China (Shanghai)</RegionName>
        <Region>shanghaixxxxxx</Region>
        <Tag>InternetIp</Tag>
        <Kernel>4.18.0-80.11.2.el8_0.x86_64</Kernel>
        <HostName>qewrqwerqsadas</HostName>
    </AssetDetail>
</data> <requestId>F7BA0B6C-4D33-49A7-AB7B-A221B2E40817</requestId>
```

`JSON` format

```json
  "code": 200,
  "data": {
    "AssetDetail": {
      "GroupTrace": "Ungrouped",
      "ClientStatus": "online",
      "Os": "linux",
      "InstanceId": "rqreqwrq",
      "IpList": [
        "10.0.0.123"
```

`],`

```json
      "CpuInfo": "Intel(R) Xeon(R) Platinum 8163 CPU @ 2.50GHz",
      "Ip": "10.10.10.101",
      "OsName": "CentOS 8.0 64-bit",
      "Cpu": 2,
      "SysInfo": "CentOS Linux 8.0.1905",
      "OsDetail": "Linux 64bit",
      "IntranetIp": "10.0.0.211",
      "DiskInfoList": [
          "diskName": "/dev/vda1",
          "totalSize": 20,
          "useSize": 2
```

`],`

```json
      "MacList": [
        "00:11:3e:20:38"
```

`],`

```json
      "InstanceName": "wqreqwerqwer",
      "AssetType": "0",
      "Uuid": "1234214-ujuj-weqweq-111-vbbbb",
      "Mem": 8,
      "InternetIp": "10.10.10.10",
      "RegionName": "China (Shanghai)",
      "Region": "shanghaixxxxxx",
      "Tag": "InternetIp",
      "Kernel": "4.18.0-80.11.2.el8_0.x86_64",
      "HostName": "qewrqwerqsadas"
```

`},`

```json
  "requestId": "F7BA0B6C-4D33-49A7-AB7B-A221B2E40817"
```

For a list of error codes, see Error codes.

#### 3.3.17 DescribeSasAssetStatisticsColumn

Queries asset details based on the displayed columns on the Server tab. The detailed information includes the server information, tag, VPC, operating system, and region. The Server tab displays columns based on the column filter. Displayed columns include the default and custom columns.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSasAsset StatisticsColumn | The operation that you want to perform. Set the value to DescribeSasAsset St at ist icsColumn. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | FA04081D-25A1- 486C-822A- 61108E85B3BD | The ID of the request. |
| StatisticsColum n | String | ServerInfo,tag,vpc,o s,region | The information in the displayed columns on the Server tab. The Server tab displays columns based on the column filter. Displayed columns include the default and custom columns. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSasAssetStatisticsColumn
```

Sample success responses `XML` format

```xml
<DescribeSasAssetStatisticsColumnResponse>
      <RequestId>EB28FE45-2E90-4F01-A5FF-EF5C1591104F</RequestId>
      <StatisticsColumn>serverInfo,tag,vpc,os,region,defense,riskStatus,operate,alarm,hc,vu
l</StatisticsColumn> </DescribeSasAssetStatisticsColumnResponse>
```

`JSON` format

```json
    "RequestId": "EB28FE45-2E90-4F01-A5FF-EF5C1591104F",
    "StatisticsColumn": "serverInfo,tag,vpc,os,region,defense,riskStatus,operate,alarm,hc,v
ul"
```

For a list of error codes, see Error codes.

#### 3.3.18 DescribePropertyUsageNewest

Queries information about five most recently created accounts.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeProperty UsageNewest | The operation that you want to perform. Set the value to DescribePropertyUsageNewest. |
| Type | String | No | user | The type of the account. Valid values: user system |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 27C78A20-0833- 4519-B392- F7963CCFC6AC | The ID of the request. |
| ItemCount | Integer | 5 | The number of accounts. |
| Type | String | user | The type of the account created on the server. Set the value to user, which indicates user accounts. |
| NewestStatistic Items | Array |   | The account information. |
| Name | String | root | The name of the account. |

| Developer Guide·Th ervice (TDS) | reat Detection |   | Apsara Stack Securit |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Create | Long | 1566178646000 | The timestamp when the account was created. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertyUsageNewest
```

Sample success responses `XML` format

```xml
<code>200</code> <data>
    <NewestStatisticItems>
        <Create>1566178646000</Create>
        <Name>dbus</Name>
    </NewestStatisticItems>
    <NewestStatisticItems>
        <Create>1566178646000</Create>
        <Name>halt</Name>
    </NewestStatisticItems>
    <NewestStatisticItems>
        <Create>1566178646000</Create>
        <Name>root</Name>
    </NewestStatisticItems>
    <NewestStatisticItems>
        <Create>1566178646000</Create>
        <Name>postfix</Name>
    </NewestStatisticItems>
    <NewestStatisticItems>
        <Create>1566178646000</Create>
        <Name>operator</Name>
    </NewestStatisticItems>
    <Type>user</Type>
    <ItemCount>5</ItemCount>
</data> <requestId>27C78A20-0833-4519-B392-F7963CCFC6AC</requestId> <success>true</success>
```

`JSON` format

```json
    "code":200,
    "data":{
        "NewestStatisticItems":[
                "Create":1566178646000,
                "Name":"dbus"
```

`},`

```json
                "Create":1566178646000,
                "Name":"halt"
```

`},`

```json
                "Create":1566178646000,
                "Name":"root"
```

`},`

```json
                "Create":1566178646000,
                "Name":"postfix"
```

`},`

```json
                "Create":1566178646000,
                "Name":"operator"
```

`],`

```json
        "Type":"user",
        "ItemCount":5
```

`},`

```json
    "requestId":"27C78A20-0833-4519-B392-F7963CCFC6AC",
    "success":true
```

For a list of error codes, see Error codes.

#### 3.3.19 DeleteTagWithUuid

Removes tags from the assets on the Assets page.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteTagWithUu id | The operation that you want to perform. Set the value to Delet eT agWit hUuid. |
| TagName | String | Yes | aaaa | The name of the tag. |

| Developer Guide·Thre ervice (TDS) | at Detection |   |   | Apsara Stack Securit |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| UuidList | String | No | 111-xx,aa-bb | The list of server UUIDs. Not e If UuidList is specified, Threat Detection Service removes the tag from the servers whose UUIDs are specified in the list. If UuidList is not specified, Threat Detection Service removes the tag from all servers. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteTagWithUuid &TagName=aaaa
```

Sample success responses `XML` format

```xml
<DeleteTagWithUuidResponse>
      <requestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</requestId>
</DeleteTagWithUuidResponse>
```

`JSON` format

```json
  "requestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F"
```

For a list of error codes, see Error codes.

#### 3.3.20 ModifyPushAllTask

Dispatches all security check tasks.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyPushAllTas k | The operation that you want to perform. Set the value to ModifyPushAllTask. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Uuids | String | No | uuid1,uuid2,uuid3 | The list of server UUIDs. |
| Tasks | String | No | HEALTH CHECK,O _ VAL ENTITY _ | The list of tasks. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 91EB4AC7-7FEF- 4C72-BE49- 4414E459AEC2 | The ID of the request. |
| PushTaskRsp | Struct |   | The result of the task dispatch. |
| PushTaskResult List | Array |   | The list of tasks failed to be dispatched. |
| InstanceId | String | i-xxxsasssss | The ID of the server. |
| OsVersion | String | linux | The version of the operating system. |
| InstanceName | String | Pay-as-you-go online monitoring | The name of the server. |
| Success | Boolean | false | The result of the task dispatch. |
| GroupId | Long | 226 | The ID of the group. |
| Ip | String | 127.0.0.1 | The IP address of the server. |
| Online | Boolean | true | Indicates whether the agent is connected. |

| Developer Guide·Th | reat Detection |   | Apsara Stack Securit |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | {\"code\":\"clinent _ offline\",\"message \":\"The agent is disconnected",\"suc cess\":false} | The message indicating task details. |
| Region | String | cn-beijing-ss-10 | The region where the server is deployed. |
| Uuid | String | inet-xxxxx-xxxx- xxxx-xxx-xxx | The UUID of the server. |

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyPushAllTask
```

Sample success responses `XML` format

```xml
<PushTaskRsp>
    <PushTaskResultList>
        <GroupId>336</GroupId>
        <InstanceId>i-xxxsasssss</InstanceId>
        <InstanceName>Pay-as-you-go online monitoring</InstanceName>
        <Ip>127.0.0.1</Ip>
        <Message>{"code":"clinent_offline","message":"The agent is disconnected","success":
false}</Message>
        <Online>false</Online>
        <OsVersion>linux</OsVersion>
        <Region>cn-beijing-ss-10</Region>
        <Success>false</Success>
        <Uuid>inet-xxxxx-xxxx-xxxx-xxx-xxx</Uuid>
    </PushTaskResultList>
</PushTaskRsp> <RequestId>91EB4AC7-7FEF-4C72-BE49-4414E459AEC2</RequestId>
```

`JSON` format

```json
  "PushTaskRsp":{
    "PushTaskResultList":[{
      "GroupId":336,
      "InstanceId":"i-xxxsasssss",
      "InstanceName":"Pay-as-you-go online monitoring",
      "Ip":"127.0.0.1",
      "Message":"{\"code\":\"clinent_offline\",\"message\":\"The agent is disconnected\",\"
success\":false}",
      "Online":false,
      "OsVersion":"linux",
      "Region":"cn-beijing-ss-10",
      "Success":false,
      "Uuid":"inet-xxxxx-xxxx-xxxx-xxx-xxx"
```

`}]` `},`

```json
  "RequestId":"91EB4AC7-7FEF-4C72-BE49-4414E459AEC2"
```

For a list of error codes, see Error codes.

#### 3.3.21 DescribeCriteria

Queries fuzzy match conditions that return the properties of a queried asset.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCriteria | The operation that you want to perform. Set the value to DescribeCriteria. |
| MachineTypes | String | No | ecs | The type of the asset that you want to query. Valid values: ecs: Elastic Compute Service (ECS) instances cloud product : cloud services _ except ECS |
| Value | String | No | xxx | The value of the fuzzy match condition. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 3F6E4741-6CE6- 47CA-80E8- CF5CB145DBE2 | The ID of the request. |
| CriteriaList | Array |   | The list of search conditions. |
| Values | String | NO,YES,UNKNOWN | If the search condition is an option, the value of the option is returned. If the search condition is an input, no value is returned. |
| Name | String | riskStatus | The names of all properties queried by the search conditions. |
| Type | String | input | The type of the search condition. Valid values: input : an input. The search condition is manually set. select : an option. The search condition is selected from a drop-down list. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCriteria
```

Sample success responses `XML` format

```xml
<code>200</code> <data>
    <CriteriaList>
        <Type>input</Type>
        <Values/>
        <Name>internetIp</Name>
    </CriteriaList>
    <CriteriaList>
        <Type>select</Type>
        <Values>NO,YES</Values>
        <Name>vulStatus</Name>
    </CriteriaList>
</data> <requestId>3F6E4741-6CE6-47CA-80E8-CF5CB145DBE2</requestId>
```

`JSON` format

```json
  "code": 200,
  "data": {
    "CriteriaList": [
        "Type": "input",
        "Values": "",
        "Name": "internetIp"
```

`},`

```json
        "Type": "select",
        "Values": "NO,YES",
        "Name": "vulStatus"
```

`]` `},`

```json
  "requestId": "3F6E4741-6CE6-47CA-80E8-CF5CB145DBE2"
```

For a list of error codes, see Error codes.

#### 3.3.22 DescribeExportInfo

Queries the progress of the task to export baseline check results.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeExportInf o | The operation that you want to perform. Set the value to DescribeExportInfo. |
| ExportId | Long | Yes | 111 | The ID of the export task. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4C1AE3F3-18FA- 4108-BBB9- AFA1A032756C | The ID of the request. |
| Id | Long | 11 | The ID of the export task. |

| S | Developer Guide·Th ervice (TDS) | reat Detection |   | Apsara Stack Securit | y |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| FileName | String | health check export _ _ 20171123 _ | The name of the exported Excel file. |
| CurrentCount | Integer | 1 | The number of the entries that have been exported. |
| TotalCount | Integer | 1 | The total number of the entries in the Excel file. |
| Progress | Integer | 100 | The progress of the export task. |
| ExportStatus | String | success | The status of the export task. Valid values: init : The export task is initializing. export ing: The export task is in progress. success: The export task is completed. |
| Message | String | success | The message that shows the task result. Set the value to success, which indicates the export task is completed. |
| Link | String | http://www.aliyun. com | The URL at which you can download the exported Excel file. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeExportInfo
```

Sample success responses `XML` format

```xml
<code>200</code> <data>
    <TotalCount>1</TotalCount>
    <GmtCreate>1511439067000</GmtCreate>
    <Progress>100</Progress>
    <Message>success</Message>
    <ExportStatus>success</ExportStatus>
    <FileName>health_check_export_20171123</FileName>
    <CurrentCount>1</CurrentCount>
    <Id>11</Id>
    <Link>http://www.aliyun.com</Link>
</data> <requestId>4C1AE3F3-18FA-4108-BBB9-AFA1A032756C</requestId>
```

`JSON` format

```json
  "code": "200",
  "data": {
    "TotalCount":1,
    "GmtCreate":1511439067000,
    "Progress":100,
    "Message":"success",
    "ExportStatus":"success",
    "FileName":"health_check_export_20171123",
    "CurrentCount":1,
    "Id":11,
    "Link":"http://www.aliyun.com"
```

`},`

```json
  "requestId": "4C1AE3F3-18FA-4108-BBB9-AFA1A032756C"
```

For a list of error codes, see Error codes.

#### 3.3.23 ModifyLoginSwitchConfig

Enables or disables the logon security settings for a specific asset.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyLoginSwitc hConfig | The operation that you want to perform. Set the value to: Modif yLoginSwit chConf ig. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Item | String | Yes | login common a _ _ ccount | The type of the alert that you want to enable or disable. Valid values: login common ip: uncommon _ _ logon IP address alerts login common t ime: uncommon _ _ logon time alerts login common account : _ _ uncommon logon account alerts |
| Status | Integer | Yes | 0 | The status of the logon security settings. Valid values: 0: disabled 1: enabled |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B256A525-7E42- 4BB9-A27C- 9017FDDFF1A2 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyLoginSwitchConfig &Item=login_common_account &Status=0
```

Sample success responses `XML` format

```xml
<ModifyLoginSwitchConfigResponse>
      <requestId>B256A525-7E42-4BB9-A27C-9017FDDFF1A2</requestId>
</ModifyLoginSwitchConfigResponse>
```

`JSON` format

```json
  "requestId": "B256A525-7E42-4BB9-A27C-9017FDDFF1A2"
```

For a list of error codes, see Error codes.

#### 3.3.24 ModifyLoginBaseConfig

Modifies the logon security settings for a specific asset.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyLoginBase Config | The operation that you want to perform. Set the value to Modif yLoginBaseConf ig. |
| Config | String | Yes | {"startTime":"00: 00","endTime":"0 2:00"} | The logon security settings for the specified asset. |
| Target | String | Yes | i-ecs-ssssasss- xxxx | The UUID of the server whose settings you want to modify. |
| Type | String | Yes | login common ti _ _ me | The type of the common logon that you want to modify. Valid values: login common ip: common logon _ _ IP addresses login common t ime: common _ _ logon time login common account : _ _ common logon accounts |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6BD40006-2A29- 4769-8AB5- BC0F0E25C273 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyLoginBaseConfig &Config={"startTime":"00:00","endTime":"02:00"} &Target=i-ecs-ssssasss-xxxx &Type=login_common_time
```

Sample success responses `XML` format

```xml
<ModifyLoginBaseConfigResponse>
      <requestId>6BD40006-2A29-4769-8AB5-BC0F0E25C273</requestId>
</ModifyLoginBaseConfigResponse>
```

`JSON` format

```json
    "requestId":"6BD40006-2A29-4769-8AB5-BC0F0E25C273"
```

For a list of error codes, see Error codes.

#### 3.3.25 DeleteLoginBaseConfig

Deletes basic configurations in the logon security settings for a specific asset.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteLoginBaseC onfig | The operation that you want to perform. Set the value to Delet eLoginBaseConf ig. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Config | String | Yes | {"startTime":"06: 00:00","endTime" :"16:00:00"} | The detailed configurations. The configurations depend on logon types. Valid values: login common ip: common logon _ _ IP addresses Example: {"ip":"10.23.23.23"}. login common t ime: common _ _ logon time Example: {"startTime":"06:00:00", "endTime":"16:00:00"}. login common account : _ _ common logon accounts Example: {"account":"test account 001"}. _ _ login common locat ion: _ _ common logon locations Example: {"location":"Shanghai"}. |
| Type | String | Yes | login common ti _ _ me | The type of the common logon that you want to delete. Valid values: login common ip: common logon _ _ IP addresses login common t ime: common _ _ logon time login common account : _ _ common logon accounts login common locat ion: _ _ common logon locations |
| Target | String | No | 123-abc | The UUID of the server whose settings you want to delete. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteLoginBaseConfig &Config={"startTime":"06:00:00","endTime":"16:00:00"} &Type=login_common_time
```

Sample success responses `XML` format

```xml
<DeleteLoginBaseConfigResponse>
      <requestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</requestId>
</DeleteLoginBaseConfigResponse>
```

`JSON` format

```json
  "requestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F"
```

For a list of error codes, see Error codes.

#### 3.3.26 DescribeAssetDetailByUuids

Queries the details of specific ECS instances.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAssetDet ailByUuids | The operation that you want to perform. Set the value to: DescribeAsset Det ailByUuids. |
| Uuids | String | Yes | 0687b17f-2a36- 4e5c-b3d9 | The list of ECS instances. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AssetList | Array |   | The details of the assets. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AssetType | String | 0 | The type of the assets. Set the value to 0, which indicates ECS instances. |
| ClientStatus | String | online | The status of the agent. Valid values: online of f line |
| InstanceId | Integer | 1312332131 | The ID of the ECS instance. |
| InstanceName | Integer | 11 | The name of the ECS instance. |
| InternetIp | String | 10.10.10.10 | The public IP address of the ECS instance. |
| IntranetIp | String | 10.10.10.10 | The private IP address of the ECS instance. |
| Ip | String | 10.10.10.10 | The public IP address of the ECS instance, which is the same as the Int ernet Ip parameter. |
| Os | String | linux | The type of the operating system run by the ECS instance. |
| OsName | String | CentOS 7.6 64-bit | The name of the operating system run by the ECS instance. |
| Region | String | cn-huhehaote-123- 323 | The region where the ECS instance is deployed. |
| RegionName | String | China (Hohhot) | The name of the region. |
| Uuid | String | 01111-asdad-assd | The UUID of the ECS instance. |
| VpcInstanceId | String | 13231-331331 | The ID of the VPC. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 92016EC8-D52D- 49D8-9FF7- 9EA340A950B9 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeAssetDetailByUuids &Uuids=0687b17f-2a36-4e5c-b3d9
```

Sample success responses `XML` format

```xml
<DescribeAssetDetailByUuidsResponse>
  <AssetDetail>
        <ClientStatus>online</ClientStatus>
        <Os>linux</Os>
        <InstanceId>1312332131</InstanceId>
        <Ip>10.10.10.10</Ip>
        <OsName>CentOS 7.6 64-bit</OsName>
        <OsDetail>Linux 64bit</OsDetail>
        <IntranetIp>100.10.10.10</IntranetIp>
        <InstanceName>Server 1</InstanceName>
        <AssetType>0</AssetType>
        <Uuid>01111-asdad-assd</Uuid>
        <InternetIp>10.10.10.10</InternetIp>
        <RegionName>China (Hohhot)</RegionName>
        <Region>cn-huhehaote-123-323</Region>
  </AssetDetail>
  <requestId>92016EC8-D52D-49D8-9FF7-9EA340A950B9</requestId>
</DescribeAssetDetailByUuidsResponse>
```

`JSON` format

```json
    "AssetDetail": {
        "ClientStatus": "online",
        "Os": "linux",
        "InstanceId": "1312332131",
        "Ip": "10.10.10.10",
        "OsName": "CentOS 7.6 64bit",
        "OsDetail": "Linux 64bit",
        "IntranetIp": "100.10.10.10",
        "InstanceName": "Server 1",
        "AssetType": "0",
        "Uuid": "01111-asdad-assd",
        "InternetIp": "10.10.10.10",
        "RegionName": "China (Hohhot)",
        "Region": "cn-huhehaote-123-323"
```

`},`

```json
    "requestId": "92016EC8-D52D-49D8-9FF7-9EA340A950B9"
```

For a list of error codes, see Error codes.

### 3.4 Secure score

#### 3.4.1 DescribeSecureSuggestion

Queries detailed suggestions about how to manage the security risks related to the security score.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSecureSu ggestion | The operation that you want to perform. Set the value to DescribeSecureSuggestion. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F35F45B0-5D6B- 4238-BE02- A62D0760E840 | The ID of the request. |
| Suggestions | Array |   | The list of risk management suggestions. |
| Detail | Array |   | The details of the suggestion for security risk mitigation. |
| Description | String | You have four ApsaraDB for RDS instances at risk. | The description of the suggestion for security risk mitigation. |
| SubType | String | CLOUD HC RDS _ _ | The type of the unhandled security risk. |
| Title | String | The check on security policies of ApsaraDB for RDS instances has failed. The instances are at risk. | The name of the unhandled security risk. |
| Points | Integer | 40 | The penalty points of each item. |
| SuggestType | String | SS ALARM _ | The type of the unhandled security risk. Valid values: SS REINFORCE: Key features, such as the _ anti-virus feature, are not configured. SS ALARM: unhandled alerts. _ SS VUL: unhandled vulnerabilities. _ SS HC: baseline check risks. _ SS AK: AccessKey pair leaks. _ SS CLOUD HC: configuration risks in _ _ Alibaba Cloud services. OT HER: other risks. |
| TotalCount | Integer | 15 | The total number of unhandled security risks. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSecureSuggestion
```

Sample success responses `XML` format

```xml
<DescribeSecureSuggestionResponse>
  <Suggestions>
        <Points>40</Points>
        <SuggestType>SS_ALARM</SuggestType>
        <Detail>
              <Description>You have 691 security alerts, which affects 56 assets.</Descript
ion>
              <SubType>ALARM_HIGH</SubType>
              <Title>You have unhandled high-risk alerts</Title>
        </Detail>
        <Detail>
              <Description>You have 501 security alerts, which affects 119 assets.</Descrip
tion>
              <SubType>ALARM_MEDIUM</SubType>
              <Title>You have unhandled middle-risk alerts</Title>
        </Detail>
  </Suggestions>
  <Suggestions>
        <Points>12</Points>
        <SuggestType>SS_VUL</SuggestType>
        <Detail>
              <Description>You have five vulnerabilities.</Description>
              <SubType>VUL_CMS</SubType>
              <Title>You have unhandled CMS vulnerabilities</Title>
        </Detail>
        <Detail>
              <Description>You have 107 vulnerabilities, which affects 68 servers.</Descrip
tion>
              <SubType>VUL_WIN</SubType>
              <Title>You have unhandled Windows host vulnerabilities</Title>
        </Detail>
        <Detail>
              <Description>You have 701 vulnerabilities, which affects 87 servers.</Descrip
tion>
              <SubType>VUL_LINUX</SubType>
              <Title>You have unhandled Linux host vulnerabilities</Title>
        </Detail>
        <Detail>
              <Description>You have one unhandled emergency vulnerability.</Description>
              <SubType>VUL_EMR_UNFIX</SubType>
              <Title>You have unhandled emergency vulnerabilities</Title>
        </Detail>
  </Suggestions>
  <Suggestions>
        <Points>2</Points>
        <SuggestType>SS_HC</SuggestType>
        <Detail>
```

```xml
              <Description>You have 46 baseline check risks, which affects 260 servers.</De
scription>
              <SubType>HC_WARN</SubType>
              <Title>You have unhandled baseline risks</Title>
        </Detail>
  </Suggestions>
  <Suggestions>
        <Points>30</Points>
        <SuggestType>SS_AK</SuggestType>
        <Detail>
              <Description>You have 12 AccessKey pair leaks.</Description>
              <SubType>ACCESSKEY_LEAK</SubType>
              <Title>You have potential AccessKey pair leaks</Title>
        </Detail>
  </Suggestions>
  <Suggestions>
        <Points>35</Points>
        <SuggestType>SS_CLOUD_HC</SuggestType>
        <Detail>
              <Description>You have four ApsaraDB for RDS instances at risk.</Description>
              <SubType>CLOUD_HC_RDS</SubType>
              <Title>The check on security policies of ApsaraDB for RDS instances failed. T
he instances are at risk</Title>
        </Detail>
        <Detail>
              <Description>You have three unhandled high configuration risks for Alibaba Cl
oud services.</Description>
              <SubType>CLOUD_HC_HIGH_LEVEL</SubType>
              <Title>You have high configuration risks for Alibaba Cloud services</Title>
        </Detail>
        <Detail>
              <Description>You have 28 unhandled medium or low configuration risks for Alib
aba Cloud services.</Description>
              <SubType>CLOUD_HC_OTHER_LEVEL</SubType>
              <Title>You have medium or low configuration risks for Alibaba Cloud services<
/Title>
        </Detail>
  </Suggestions>
  <Suggestions>
        <Points>5</Points>
        <SuggestType>OTHER</SuggestType>
        <Detail>
              <Description>You have been attacked 5,767 times.</Description>
              <SubType>OTHER_ATTACH</SubType>
              <Title>You are under attack</Title>
        </Detail>
  </Suggestions>
  <TotalCount>12</TotalCount>
  <requestId>F35F45B0-5D6B-4238-BE02-A62D0760E840</requestId>
</DescribeSecureSuggestionResponse>
```

`JSON` format

|   | { "Suggestions": [{ "Points": 40, "SuggestType": "SS ALARM", _ "Detail": [{ "Description": "You have 691 security alerts, which affects 56 assets", "SubType": "ALARM HIGH", _ "Title": "You have unhandled high-risk alerts" }, { "Description": "You have 501 security alerts, which affects 119 assets", "SubType": "ALARM MEDIUM", _ "Title": "You have unhandled medium-risk alerts" }] }, { "Points": 12, "SuggestType": "SS VUL", _ "Detail": [{ "Description": "You have five vulnerabilities", "SubType": "VUL CMS", _ "Title": "You have unhandled CMS vulnerabilities." }, { "Description": "You have 107 vulnerabilities, which affects 68 servers", "SubType": "VUL WIN", _ "Title": "You have unhandled Windows host vulnerabilities" }, { "Description": "You have 701 vulnerabilities, which affects 87 servers", "SubType": "VUL LINUX", _ "Title": "You have unhandled Linux host vulnerabilities" }, { "Description": "You have one unhandled emergency vulnerability", "SubType": "VUL EMR UNFIX", _ _ "Title": "You have unhandled emergency vulnerabilities" }] }, { "Points": 2, "SuggestType": "SS HC", _ "Detail": [{ "Description": "You have 46 baseline check risks, which affects 260 servers", "SubType": "HC WARN", _ "Title": "You have baseline check risks" }] }, { "Points": 30, "SuggestType": "SS AK", _ "Detail": [{ "Description": "You have 12 potential AccessKey pair leaks", "SubType": "ACCESSKEY LEAK", _ "Title": "You have potential AccessKey pair leaks" }] }, { "Points": 35, "SuggestType": "SS CLOUD HC", _ _ "Detail": [{ "Description": "You have four ApsaraDB for RDS instances at risk", "SubType": "CLOUD HC RDS" |   |
|---|---|---|

```json
            SubType: CLOUD_HC_RDS,
            "Title": "The check on security policies of ApsaraDB for RDS instances has fail
ed. The instances are at risk"
        }, {
            "Description": "You have three high configuration risks for Alibaba Cloud servi
ces",
            "SubType": "CLOUD_HC_HIGH_LEVEL",
            "Title": "You have high configuration risks for Alibaba Cloud services"
        }, {
            "Description": "You have 28 medium or low configuration risks for Alibaba Cloud
services",
            "SubType": "CLOUD_HC_OTHER_LEVEL",
            "Title": "You have medium or low configuration risks for Alibaba Cloud services
```

`"` `}]`

```json
    }, {
        "Points": 5,
        "SuggestType": "OTHER",
        "Detail": [{
            "Description": "You have been attacked 5,767 times",
            "SubType": "OTHER_ATTACH",
            "Title": "You are under attack"
```

`}]`

```json
    }],
    "TotalCount": 12,
    "requestId": "F35F45B0-5D6B-4238-BE02-A62D0760E840"
```

For a list of error codes, see Error codes.

### 3.5 Security alerts

#### 3.5.1 HandleSecurityEvents

Handles alerts.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| SecurityEventIds. N | RepeatLi st | No | ["909361"] | The ID of the alert. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| OperationCode | String | No | ignore | The operation that is performed to handle alerts of the same type at a time. Valid values: deal: quarantines the source file of the malicious process. kill and quara: kills the malicious _ _ process and quarantines the source file. kill virus: deletes the source file of _ the malicious process. block ip: blocks the source IP _ addresses. ignore: ignores the alerts. mark mis inf o: marks the alerts as _ _ false positives by adding them to the whitelist. rm mark mis inf o: cancels false _ _ _ positives by removing the alerts from the whitelist. of f line handled: marks the alerts _ as handled. |
| OperationParams | String | No | {"expireTime":15 78475919533} | The parameter values of the operation that is performed to handle alerts of the same type at a time. This parameter must be specified if the OperationCode parameter is set to the following values: kill and quara _ _ block ip _ |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D929B6F9-EE5E- 4F26-A22F- 65D4088B6F24 | The ID of the request. |
| HandleSecurityE ventsResponse | Struct |   | The response of the processing result. |

| Developer Guide·Th | reat Detection |   |   |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| TaskId | Long | 3187 | The ID of the task to handle the alerts. |

Sample requests

```
http(s)://[Endpoint]/?Action=HandleSecurityEvents
```

Sample success responses `XML` format

```xml
<HandleSecurityEventsResponse>
    <TaskId>3817</TaskId>
</HandleSecurityEventsResponse> <requestId>D929B6F9-EE5E-4F26-A22F-65D4088B6F24</requestId>
```

`JSON` format

```json
    "HandleSecurityEventsResponse": {
            "TaskId": 3817
```

`},`

```json
    "requestId": "D929B6F9-EE5E-4F26-A22F-65D4088B6F24"
```

For a list of error codes, see Error codes.

#### 3.5.2 DescribeSecurityStatInfo

Queries the statistics on each security check item and the daily statistics in the trend chart based on each security check item.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSecurityS tatInfo | The operation that you want to perform. Set the value to DescribeSecurit ySt at Inf o. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

| psara Stack Security |   |   |   | Developer Guide·Threat Detection Service (TDS |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AttackEvent | Struct |   | The detailed attack statistics. |
| DateArray | List | ["2020-01-04", "2020-01-05", "2020-01-06", "2020-01-07", "2020-01-08", "2020-01-09", "2020-01-10"] | The time points when attack data is collected in the trend chart. |
| TotalCount | Integer | 1096 | The number of attacks detected on the current day. |
| ValueArray | List | [2620, 10405, 2377, 2411, 11146, 2057, 1096] | The number of attacks at each time point. |
| HealthCheck | Struct |   | The detailed statistics on baseline risks. |
| DateArray | List | ["2020-01-04", "2020-01-05", "2020-01-06", "2020-01-07", "2020-01-08", "2020-01-09", "2020-01-10"] | The time points when baseline risk data is collected in the trend chart. |
| HighCount | Integer | 10 | The number of high-level baseline risks on the current day. |
| HighList | List | [11, 11, 11, 10, 10, 10, 10] | The number of high-level baseline risks at each time point. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| LevelsOn | List | [ "high", "low", "medium" ] | The list of baseline risk levels. Valid values: high medium low |
| LowCount | Integer | 0 | The number of low-level baseline risks on the current day. |
| LowList | List | [0, 0, 0, 0, 0, 0, 0] | The number of low-level baseline risks at each time point. |
| MediumCount | Integer | 21 | The number of medium-level baseline risks on the current day. |
| MediumList | List | [21, 21, 21, 21, 21, 21, 21] | The number of medium-level baseline risks at each time point. |
| TotalCount | Integer | 32 | The total number of baseline risks on the current day. |
| ValueArray | List | [32, 32, 32, 31, 31, 31, 31] | The total number of baseline risks at each time point. |
| RequestId | String | A3E61730-85E2- 4789-8017- B9B1B70F0568 | The ID of the request. |
| SecurityEvent | Struct |   | The details of pending alerts. |
| DateArray | List | ["2020-01-04", "2020-01-05", "2020-01-06", "2020-01-07", "2020-01-08", "2020-01-09", "2020-01-10"] | The time points when data of pending alerts is collected in the trend chart. |
| LevelsOn | List | ["remind", "suspicious", "serious"] | The level of the pending alerts. Valid values: remind suspicious serious |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RemindCount | Integer | 0 | The number of remind alerts on the current day. |
| RemindList | List | [5, 5, 0, 0, 0, 0, 0] | The number of remind alerts at each time point. |
| SeriousCount | Integer | 404 | The number of serious alerts on the current day. |
| SeriousList | List | [315, 350, 336, 378, 384, 398, 404] | The number of serious alerts at each time point. |
| SuspiciousCoun t | Integer | 148 | The number of suspicious alerts on the current day. |
| SuspiciousList | List | [124, 133, 111, 123, 135, 145, 148] | The number of suspicious alerts at each time point. |
| TotalCount | Integer | 552 | The total number of pending alerts on the current day. |
| ValueArray | List | [444, 488, 447, 501, 519, 543, 552] | The number of pending alerts at each time point. |
| Success | Boolean | true | The status of the request. Valid values: t rue: The request succeeded. f alse: The request failed. |
| Vulnerability | Struct |   | The detailed statistics on pending vulnerabilities. |
| AsapCount | Integer | 109 | The number of high-risk pending vulnerabilities on the current day. |
| AsapList | List | [60, 65, 63, 97, 103, 109, 109] | The number of high-risk pending vulnerabilities at each time point. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DateArray | List | ["2020-01-04", "2020-01-05", "2020-01-06", "2020-01-07", "2020-01-08", "2020-01-09", "2020-01-10"] | The time points when data of pending vulnerabilities is collected in the trend chart. |
| LaterCount | Integer | 275 | The number of medium-risk pending vulnerabilities on the current day. |
| LaterList | List | [0, 0, 0, 0, 0, 275, 275] | The number of medium-risk pending vulnerabilities at each time point. |
| LevelsOn | List | ["asap", "later","Nntf"] | The risk level of the pending vulnerabilities. Valid values: asap : high-risk lat er : medium-risk Nnt f : low-risk |
| NntfCount | Integer | 0 | The number of low-risk pending vulnerabilities on the current day. |
| NntfList | List | [0, 0, 0, 0, 0, 0, 0] | The number of low-risk pending vulnerabilities at each time point. |
| TotalCount | Integer | 384 | The number of pending vulnerabilities on the current day. |
| ValueArray | List | [60, 65, 63, 97, 103, 384, 384] | The number of pending vulnerabilities at each time point. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSecurityStatInfo
```

Sample success responses `XML` format

```xml
<DescribeSecurityStatInfoResponse>
      <SecurityEvent>
```

```xml
            <SuspiciousList>124</SuspiciousList>
            <SuspiciousList>133</SuspiciousList>
            <SuspiciousList>111</SuspiciousList>
            <SuspiciousList>123</SuspiciousList>
            <SuspiciousList>135</SuspiciousList>
            <SuspiciousList>145</SuspiciousList>
            <SuspiciousList>148</SuspiciousList>
            <LevelsOn>remind</LevelsOn>
            <LevelsOn>suspicious</LevelsOn>
            <LevelsOn>serious</LevelsOn>
            <TotalCount>552</TotalCount>
            <SuspiciousCount>148</SuspiciousCount>
            <SeriousList>315</SeriousList>
            <SeriousList>350</SeriousList>
            <SeriousList>336</SeriousList>
            <SeriousList>378</SeriousList>
            <SeriousList>384</SeriousList>
            <SeriousList>398</SeriousList>
            <SeriousList>404</SeriousList>
            <RemindCount>0</RemindCount>
            <ValueArray>444</ValueArray>
            <ValueArray>488</ValueArray>
            <ValueArray>447</ValueArray>
            <ValueArray>501</ValueArray>
            <ValueArray>519</ValueArray>
            <ValueArray>543</ValueArray>
            <ValueArray>552</ValueArray>
            <SeriousCount>404</SeriousCount>
            <RemindList>5</RemindList>
            <RemindList>5</RemindList>
            <RemindList>0</RemindList>
            <RemindList>0</RemindList>
            <RemindList>0</RemindList>
            <RemindList>0</RemindList>
            <RemindList>0</RemindList>
            <DateArray>2020-01-04</DateArray>
            <DateArray>2020-01-05</DateArray>
            <DateArray>2020-01-06</DateArray>
            <DateArray>2020-01-07</DateArray>
            <DateArray>2020-01-08</DateArray>
            <DateArray>2020-01-09</DateArray>
            <DateArray>2020-01-10</DateArray>
      </SecurityEvent>
      <HealthCheck>
            <LevelsOn>high</LevelsOn>
            <LevelsOn>low</LevelsOn>
            <LevelsOn>medium</LevelsOn>
            <TotalCount>31</TotalCount>
            <HighList>11</HighList>
            <HighList>11</HighList>
            <HighList>11</HighList>
            <HighList>10</HighList>
            <HighList>10</HighList>
            <HighList>10</HighList>
```

```xml
            <HighList>10</HighList>
            <HighCount>10</HighCount>
            <LowList>0</LowList>
            <LowList>0</LowList>
            <LowList>0</LowList>
            <LowList>0</LowList>
            <LowList>0</LowList>
            <LowList>0</LowList>
            <LowList>0</LowList>
            <MediumList>21</MediumList>
            <MediumList>21</MediumList>
            <MediumList>21</MediumList>
            <MediumList>21</MediumList>
            <MediumList>21</MediumList>
            <MediumList>21</MediumList>
            <MediumList>21</MediumList>
            <LowCount>0</LowCount>
            <ValueArray>32</ValueArray>
            <ValueArray>32</ValueArray>
            <ValueArray>32</ValueArray>
            <ValueArray>31</ValueArray>
            <ValueArray>31</ValueArray>
            <ValueArray>31</ValueArray>
            <ValueArray>31</ValueArray>
            <MediumCount>21</MediumCount>
            <DateArray>2020-01-04</DateArray>
            <DateArray>2020-01-05</DateArray>
            <DateArray>2020-01-06</DateArray>
            <DateArray>2020-01-07</DateArray>
            <DateArray>2020-01-08</DateArray>
            <DateArray>2020-01-09</DateArray>
            <DateArray>2020-01-10</DateArray>
      </HealthCheck>
      <Vulnerability>
            <LevelsOn>asap</LevelsOn>
            <LevelsOn>later</LevelsOn>
            <TotalCount>384</TotalCount>
            <AsapList>60</AsapList>
            <AsapList>65</AsapList>
            <AsapList>63</AsapList>
            <AsapList>97</AsapList>
            <AsapList>103</AsapList>
            <AsapList>109</AsapList>
            <AsapList>109</AsapList>
            <LaterList>0</LaterList>
            <LaterList>0</LaterList>
            <LaterList>0</LaterList>
            <LaterList>0</LaterList>
            <LaterList>0</LaterList>
            <LaterList>275</LaterList>
            <LaterList>275</LaterList>
            <LaterCount>275</LaterCount>
            <AsapCount>109</AsapCount>
            <NntfList>0</NntfList>
<NntfList>0</NntfList>
```

```xml
            <NntfList>0</NntfList>
            <NntfList>0</NntfList>
            <NntfList>0</NntfList>
            <NntfList>0</NntfList>
            <NntfList>0</NntfList>
            <NntfList>0</NntfList>
            <ValueArray>60</ValueArray>
            <ValueArray>65</ValueArray>
            <ValueArray>63</ValueArray>
            <ValueArray>97</ValueArray>
            <ValueArray>103</ValueArray>
            <ValueArray>384</ValueArray>
            <ValueArray>384</ValueArray>
            <NntfCount>0</NntfCount>
            <DateArray>2020-01-04</DateArray>
            <DateArray>2020-01-05</DateArray>
            <DateArray>2020-01-06</DateArray>
            <DateArray>2020-01-07</DateArray>
            <DateArray>2020-01-08</DateArray>
            <DateArray>2020-01-09</DateArray>
            <DateArray>2020-01-10</DateArray>
      </Vulnerability>
      <AttackEvent>
            <TotalCount>1096</TotalCount>
            <ValueArray>2620</ValueArray>
            <ValueArray>10405</ValueArray>
            <ValueArray>2377</ValueArray>
            <ValueArray>2411</ValueArray>
            <ValueArray>11146</ValueArray>
            <ValueArray>2057</ValueArray>
            <ValueArray>1096</ValueArray>
            <DateArray>2020-01-04</DateArray>
            <DateArray>2020-01-05</DateArray>
            <DateArray>2020-01-06</DateArray>
            <DateArray>2020-01-07</DateArray>
            <DateArray>2020-01-08</DateArray>
            <DateArray>2020-01-09</DateArray>
            <DateArray>2020-01-10</DateArray>
      </AttackEvent>
      <requestId>9C92EF15-B9F7-4DCF-BCE3-5B2B85927744</requestId>
      <success>true</success>
</DescribeSecurityStatInfoResponse>
```

`JSON` format

```json
        "SecurityEvent": {
            "SuspiciousList": [
                124,
                133,
                111,
                123,
                135,
                145,
```

`],`

```json
            "LevelsOn": [
                "remind",
                "suspicious",
                "serious"
```

`],`

```json
            "TotalCount": 552,
            "SuspiciousCount": 148,
            "SeriousList": [
                315,
                350,
                336,
                378,
                384,
                398,
```

`],`

```json
            "RemindCount": 0,
            "ValueArray": [
                444,
                488,
                447,
                501,
                519,
                543,
```

`],`

```json
            "SeriousCount": 404,
            "RemindList": [
```

`5,` `5,` `0,` `0,` `0,` `0,` `],`

```json
            "DateArray": [
                "2020-01-04",
                "2020-01-05",
                "2020-01-06",
                "2020-01-07",
                "2020-01-08",
                "2020-01-09",
                "2020-01-10"
```

`]` `},`

```json
        "HealthCheck": {
            "LevelsOn": [
                "high",
                "low",
                "medium"
```

`],`

```json
            "TotalCount": 31,
            "HighList": [
                11,
                11,
                11,
                10,
                10,
                10,
```

`],`

```json
            "HighCount": 10,
            "LowList": [
```

`0,` `0,` `0,` `0,` `0,` `0,` `],`

```json
            "MediumList": [
                21,
                21,
                21,
                21,
                21,
                21,
```

`],`

```json
            "LowCount": 0,
            "ValueArray": [
                32,
                32,
                32,
                31,
                31,
                31,
```

`],`

```json
            "MediumCount": 21,
            "DateArray": [
                "2020-01-04",
                "2020-01-05",
                "2020-01-06",
                "2020-01-07",
                "2020-01-08",
                "2020-01-09",
                "2020-01-10"
```

`]` `},`

```json
        "Vulnerability": {
            "LevelsOn": [
                "asap",
                "later"
```

`]` `],`

```json
            "TotalCount": 384,
            "AsapList": [
                60,
                65,
                63,
                97,
                103,
                109,
```

`],`

```json
            "LaterList": [
```

`0,` `0,` `0,` `0,` `0,`

```
                275,
```

`],`

```json
            "LaterCount": 275,
            "AsapCount": 109,
            "NntfList": [
```

`0,` `0,` `0,` `0,` `0,` `0,` `],`

```json
            "ValueArray": [
                60,
                65,
                63,
                97,
                103,
                384,
```

`],`

```json
            "NntfCount": 0,
            "DateArray": [
                "2020-01-04",
                "2020-01-05",
                "2020-01-06",
                "2020-01-07",
                "2020-01-08",
                "2020-01-09",
                "2020-01-10"
```

`]` `},`

```json
        "AttackEvent": {
            "TotalCount": 1096,
            "ValueArray": [
2620,
```

```
                2620,
                10405,
                2377,
                2411,
                11146,
                2057,
```

`],`

```json
            "DateArray": [
                "2020-01-04",
                "2020-01-05",
                "2020-01-06",
                "2020-01-07",
                "2020-01-08",
                "2020-01-09",
                "2020-01-10"
```

`]` `},`

```json
        "requestId": "9C92EF15-B9F7-4DCF-BCE3-5B2B85927744",
        "success": true
```

For a list of error codes, see Error codes.

#### 3.5.3 DescribeAlarmEventList

Queries alert events on the Alerts page. An alert event consists of alerts and exceptions. Each alert event is related to multiple exceptions.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAlarmEve ntList | The operation that you want to perform. Set the value to DescribeAlarmEventList. |
| CurrentPage | Integer | Yes | 1 | The page number of the current page. Pages start from page 1. Default value: 1. |
| From | String | Yes | sas | The ID of the request source. Set the value to sas. |
| PageSize | String | Yes | 20 | The number of entries to return on each page. Default value: 20. |

| eveloper Guide·Thre | at Detection |   |   | Apsara Stack Securit |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| Dealed | String | No | Y | The status of the alert event. Valid values: N: unhandled Y: handled |
| Levels | String | No | serious | The severity levels of the alert events. Separate multiple levels with commas (,). Valid values: serious suspicious remind |
| Remark | String | No | database server _ | The name of the alert, or the asset information. |
| GroupId | String | No | tst*** | The group ID of the affected asset. |
| AlarmEventName | String | No | DDoS trojans | The name of the alert event. |
| AlarmEventType | String | No | Malicious process (cloud threat detection) | The type of the alert event. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| OperateErrorCode List.N | RepeatLi st | No | ignore. Success | Alert handling result code N. The value is in the format of Operation type.Operation result code. Operation types include: Common: performs common operations. deal: handles the alert. ignore: ignores the alert. offline handled: marks the alert as _ handled. mark mis info: marks the alerts as _ _ false positives by adding them to the whitelist. rm mark mis info: cancels false _ _ _ positives by removing the alerts from the whitelist. quara: quarantines the source file of the malicious process. kill and quara: kills the malicious _ _ process and quarantines the source file. kill virus: deletes the source file of _ the malicious process. block ip: blocks the source IP _ addresses. manual handled: manually handles _ the alert. Operation result codes: Success: The operation is successful. Failure: The operation fails. AgentOffline: The agent is offline. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 28267723-D857- 4DD8-B295- 013100000000 | The ID of the request. |
| SuspEvents | Array |   | The information about the alert event. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AlarmUniqueInf o | String | 8df914418f4211fbf 756efe7a6f40cbc | The ID of the alert event. |
| Solution | String | Check the malicious URLs that have been listed in the alert. Check the directory for malicious files. Terminate the malicious processes. If you manually run the processes, you can mark them as false positives in the console. | The solution to handle the alert event. |
| Level | String | serious | The severity level of the alert event. Valid values: serious suspicious remind |
| CanBeDealOnLin e | Boolean | true | Indicates whether the online processing of the alert event is supported, such as quarantining the source file of the malicious process, adding the alert event to the whitelist, and ignoring the alert event. true: Online processing is supported. false: Online processing is not supported. |
| Description | String | After an attacker accesses a victim server, to keep the malicious programs running, the attacker may have imported malicious shell scripts into scheduled tasks such as crontab and systemd. | The description of the alert event. |
| StartTime | Long | 1543740301000 | The time when the alert event starts. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| EndTime | Long | 1543740301000 | The time when the alert event ends. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| AlarmEventTyp e | String | Suspicious processes | The type of the alert event. |
| SuspiciousEvent Count | Integer | 1 | The number of exceptions related to the alert event. |
| Uuid | String | 47900178-885d- 4fa4-9d77-*** | The ID of the related asset. |
| InstanceName | String | Test server | The name of the affected asset. |
| InternetIp | String | 1.2.3.4 | The public IP address of the affected asset. |
| IntranetIp | String | 1.2.3.5 | The private IP address of the affected asset. |
| AlarmEventNa me | String | Running malicious commands | The name of the alert event. |
| SaleVersion | String | 1 | The version in which the alert event detection can be enabled. Valid values: 0: Basic Edition 1: Enterprise Edition |
| DataSource | String | aegis *** _ | The source of data. |
| CanCancelFault | Boolean | false | Indicates whether you can cancel marking this alert event as a false positive. |
| Dealed | Boolean | false | Indicates whether the alert has been handled. Valid values: true: handled false: unhandled |

| Parameter | Type | Example | Description |
|---|---|---|---|
| GmtModified | Long | 1569235879000 | The last time when the alert was triggered. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| HasTraceInfo | Boolean | true | Indicates whether the alert has trace information. true: The alert has trace information. false: The alert does not have trace information. |
| SecurityEventId s | String | 270789 | The ID of the related exception. |
| OperateErrorCo de | String | kill and quara.Succe _ _ ss | The handling result code of the alert event. |
| AlarmEventNa meOriginal | String | Precise defense against malicious commands | The original parent name of the alert event. |
| InstanceId | String | i-e*** | The ID of the affected asset. |
| PageInfo | Struct |   | The page information. |
| Count | Integer | 1 | The number of entries returned on the current page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| TotalCount | Integer | 1 | The total number of the alert events. |
| CurrentPage | Integer | 1 | The page number of the current page. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeAlarmEventList &CurrentPage=1 &From=sas &PageSize=20
```

Sample success responses `XML` format

```xml
<DescribeAlarmEventList>
  <RequestId>1D7FB2DD-4B80-41F4-94CF-C484EF6A5CAC</RequestId>
  <PageInfo>
        <Count>1</Count>
        <TotalCount>58</TotalCount>
        <PageSize>1</PageSize>
        <CurrentPage>1</CurrentPage>
  </PageInfo>
  <SuspEvents>
        <Uuid>c4678332-ef35-4ad4-8358-681ebbc0ccab</Uuid>
        <Dealed>true</Dealed>
        <SecurityEventIds>261401</SecurityEventIds>
        <Description>Cloud threat detection (mining programs)</Description>
        <CanCancelFault>false</CanCancelFault>
        <InstanceId>i-bp***</InstanceId>
        <OperateErrorCode></OperateErrorCode>
        <InternetIp>1.2.3.5</InternetIp>
        <GmtModified>1572524936000</GmtModified>
        <SuspiciousEventCount>1</SuspiciousEventCount>
        <HasTraceInfo>false</HasTraceInfo>
        <AlarmUniqueInfo>8b59e7bd134797758709983c26ece2a2</AlarmUniqueInfo>
        <AlarmEventName>Mining programs</AlarmEventName>
        <AlarmEventType>Precise defense</AlarmEventType>
        <IntranetIp>1.2.3.4</IntranetIp>
        <Level>serious</Level>
        <EndTime>1572524936000</EndTime>
        <StartTime>1572524936000</StartTime>
        <AlrmEventNameOriginal>Precise defense against mining programs</AlarmEventNameOrigi
nal>
        <SaleVersion>0</SaleVersion>
        <CanBeDealOnLine>false</CanBeDealOnLine>
        <InstanceName>cit***</InstanceName>
  </SuspEvents>
</DescribeAlarmEventList>
```

`JSON` format

```json
    "RequestId": "1D7FB2DD-4B80-41F4-94CF-C484EF6A5CAC",
    "PageInfo": {
        "Count": 1,
        "TotalCount": 58,
        "PageSize": 1,
        "CurrentPage": 1
```

`},`

```json
    "SuspEvents": [
            "Uuid": "c4678332-ef35-4ad4-8358-681ebbc0ccab",
            "Dealed": true,
            "SecurityEventIds": "261401",
            "Description": "Cloud threat detection (mining programs)",
            "CanCancelFault": false,
            "InstanceId": "i-bp***",
            "OperateErrorCode": "",
            "InternetIp": "1.2.3.5",
            "GmtModified": 1572524936000,
            "SuspiciousEventCount": 1,
            "HasTraceInfo": false,
            "AlarmUniqueInfo": "8b59e7bd134797758709983c26ece2a2",
            "AlarmEventName": "Mining programs",
            "AlarmEventType": "Precise defense",
            "IntranetIp": "1.2.3.4",
            "Level": "serious",
            "EndTime": 1572524936000,
            "StartTime": 1572524936000,
            "AlarmEventNameOriginal": "Precise defense against mining programs",
            "SaleVersion": "0",
            "CanBeDealOnLine": false,
            "InstanceName": "cit***"
```

`]` For a list of error codes, see Error codes.

#### 3.5.4 DescribeAlarmEventDetail

Queries details of an alert event. An alert event consists of alerts and exceptions. Each alert event contains multiple exceptions.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAlarmEve ntDetail | The operation that you want to perform. Set the value to DescribeAlarmEvent Det ail. |
| AlarmUniqueInfo | String | Yes | 8df914418f4211f bf756efe7a6f40c bc | The ID of the alert event. Not e To query details of an alert event, you must specify the ID of the alert event. You can call the DescribeAlarmEventList operation to obtain the ID. |
| From | String | Yes | sas | The ID of the request source. Set the value to sas. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Struct |   | The details of the alert event. |
| AlarmEventAlia sName | String | Suspicious process behavior-execution of suspicious commands in scheduled Linux tasks | The complete name of the alert event. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AlarmEventDes c | String | After an attacker accesses a victim server, to keep the malicious programs running, the attacker may have imported malicious shell scripts into scheduled tasks such as crontab and systemd. | The description of the alert event. |
| AlarmUniqueInf o | String | 8df914418f4211fbf 756efe700000000 | The ID of the alert event. |
| CanBeDealOnLin e | Boolean | false | Indicates whether processing alert events online is supported, such as blocking an alert, adding an alert to the whitelist, and ignoring an alert. Valid values: t rue: Online processing is supported. f alse: Online processing is not supported. |
| CanCancelFault | Boolean | false | Indicates whether you can cancel labelling this alert event as a false positive. Valid values: t rue: You can cancel labeling this alert event as a false positive. f alse: You cannot cancel labeling this alert event as a false positive. |
| CauseDetails | Array |   | The cause of the alert event (the information used to trace the alert). |
| Key | String | item | The format of the text. Valid values: t ext ht ml |
| Value | Array |   | The value of the field displaying the information used to trace alerts. |
| Name | String | Solutions | The key of the field displaying the information used to trace alerts. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Type | String | html | The format of the field displaying the information used to trace alerts. |
| Value | String | Check for the exploited pages of your Web services and vulnerabilities in parameter configuration, and resolve these issues. | The value of the field displaying the information used to trace alerts. |
| DataSource | String | aegis *** _ | The source of data. |
| EndTime | Long | 1542366542000 | The end time of the alert event. |
| InstanceName | String | Test server | The name of the associated instance. |
| InternetIp | String | 1.2.3.1 | The public IP address of the associated instance. |
| IntranetIp | String | 1.2.3.5 | The private IP address of the associated instance. |
| Level | String | serious | The level of the alert event. Valid values: serious suspicious remind |
| Solution | String | Check the malicious URLs that have been listed in the alert. Check the directory for malicious file downloads. Stop the malicious processes that are running. If you trust the processes, mark the alert as a false positive in the console, and submit a ticket to security engineers. | The solution to the alert event. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| StartTime | Long | 1542378601000 | The timestamp when the alert event was detected. |
| Type | String | Suspicious network connections | The type of the alert event. |
| Uuid | String | 47900178-885d- 4fa4-9d77- XXXXXXXXXXXX | The ID of the related instance. |
| RequestId | String | 5A1DDB3C-798C- 4A84-BF6E- 3DC700000000 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeAlarmEventDetail &AlarmUniqueInfo=8df914418f4211fbf756efe7a6f40cbc &From=sas
```

Sample success responses `XML` format

```xml
<DescribeAlarmEventDetailResponse>
  <Data>
        <Uuid>47900178-885d-4fa4-9d77-XXXXXXXXXXXX</Uuid>
        <AlarmEventAliasName>Suspicious Process - Command Exceptions in Scheduled Linux Tas
ks</AlarmEventAliasName>
        <Type>Suspicious process behavior</Type>
        <InternetIp>1.2.3.1</InternetIp>
        <AlarmEventDesc>After accessing a victim server, the attacker may have imported mal
icious shell scripts into scheduled tasks such as crontab and systemd, to enable persistent execution of malicious backdoor programs. </AlarmEventDesc>
        <IntranetIp>1.2.3.5</IntranetIp>
        <CauseDetails>
              <Value>
                    <Type>text</Type>
                    <Value>An attacker has logged on to your server and has written webshel
ls by editing the configuration file.</Value>
                    <Name>Intrusion cause</Name>
              </Value>
              <Value>
                    <Type>text</Type>
                    <Value>2018-11-16 19:09:02</Value>
                    <Name>Attack time</Name>
              </Value>
              <Value>
                    <Type>text</Type>
                    <Value>N/A</Value>
                    <Name>Source IP of attack</Name>
              </Value>
              <Value>
                    <Type>text</Type>
                    <Value>N/A</Value>
                    <Name>Payload of attack</Name>
              </Value>
              <Value>
                    <Type>text</Type>
                    <Value>Check for the exploited pages of your Web services and vulnerabi
lities in parameter configuration, and resolve these issues. </Value>
                    <Name>Solutions</Name>
              </Value>
              <Key>item</Key>
        </CauseDetails>
        <Level>serious</Level>
        <EndTime>1543741201000</EndTime>
        <StartTime>1543312803000</StartTime>
        <CanBeDealOnLine>false</CanBeDealOnLine>
        <InstanceName>serve***</InstanceName>
  </Data>
  <RequestId>5A1DDB3C-798C-4A84-BF6E-3DC7F7D7EB4A</RequestId>
</DescribeAlarmEventDetailResponse>
```

`JSON` format

```json
    "Data": {
        "Uuid": "47900178-885d-4fa4-9d77-XXXXXXXXXXXX",
        "AlarmEventAliasName": "Suspicious process behavior-execution of suspicious command
s in scheduled Linux tasks",
        "Type": "Suspicious process behavior",
        "InternetIp": "1.2.3.1",
        "AlarmEventDesc": "After an attacker accesses a victim server, to keep the maliciou
s programs running, the attacker may have imported malicious shell scripts into scheduled t asks such as crontab and systemd.",
        "IntranetIp": "1.2.3.5",
        "CauseDetails": [
                "Value": [
                        "Type": "text",
                        "Value": "An attacker has logged on to your ECS instance and has wr
itten webshells by editing files.",
                        "Name": "Intrusion cause"
```

`},`

```json
                        "Type": "text",
                        "Value": "2018-11-16 19:09:02",
                        "Name": "Time of attack"
```

`},`

```json
                        "Type": "text",
                        "Value": "N/A",
                        "Name": "Source IP of attack"
```

`},`

```json
                        "Type": "text",
                        "Value": "N/A",
                        "Name": "Payload of attack"
```

`},`

```json
                        "Type": "text",
                        "Value": "Check for the exploited pages of your Web services and vu
lnerabilities in parameter configuration, and resolve these issues.",
                        "Name": "Solutions"
```

`],`

```json
                "Key": "item"
```

`],`

```json
        "Level": "serious",
        "EndTime": 1543741201000,
        "StartTime": 1543312803000,
        "CanBeDealOnLine": false,
        "InstanceName": "serve***"
```

`},`

```json
    "RequestId": "5A1DDB3C-798C-4A84-BF6E-3DC7F7D7EB4A"
```

For a list of error codes, see Error codes.

#### 3.5.5 DescribeSuspEvents

Queries information about exceptions. An alert event consists of alerts and exceptions. Each alert event is related to multiple exceptions.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSuspEven ts | The operation that you want to perform. Set the value to DescribeSuspEvent s. |
| From | String | Yes | sas | The data source on which the exception is detected. Set the value to sas. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Dealed | String | No | N | The status of the exception. Valid values: N: unhandled Y: handled |
| Name | String | No | ecs-xxx | The name of the exception or the affected server. Fuzzy match is supported. |
| Levels | String | No | serious | The severity levels of the alert events. Separate multiple levels with commas (,). The following levels are listed in descending order. serious suspicious remind |
| ParentEventTypes | String | No | Webshells | The type of the alert event to which the exception is related. |
| Remark | String | No | Test server | The IP address or name of the server. |

| D S | eveloper Guide·Thre ervice (TDS) | at Detection |   |   | Apsara Stack Securit | y |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageSize | String | No | 20 | The number of entries to return on each page. Default value: 20. |
| CurrentPage | String | No | 1 | The page number of the current page. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| AlarmUniqueInfo | String | No | 8df914418f4211f bf*** | The alert event to which the exception is related. Not e To query details about exceptions of an alert event, you must provide the ID of the alert event. You can call the DescribeAlarmEventList operation to obtain the ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 43F670F3-AB40- 4E91-BC7D- C57400000000 | The ID of the request. |
| Count | Integer | 1 | The number of entries returned on the current page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| TotalCount | Integer | 100 | The total number of the exceptions. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| SuspEvents | Array |   | The details of the exception. |
| LastTime | String | 2018-09-26 01:51:01 | The last time when the exception occurred. |

| A | psara Stack Securi | ty |   | Developer Guide·Threat Detection Service (TDS | ) |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| OccurrenceTim e | String | 2018-09-26 01:51:01 | The first time when the exception occurred. |
| Id | Long | 1000 | The ID of the exception to query. |
| UniqueInfo | String | e17e*** | The ID of the exception. |
| InstanceName | String | nginx | The name of the related asset. |
| InternetIp | String | 1.2.3.1 | The public IP address of the related asset. |
| IntranetIp | String | 1.2.3.5 | The private IP address of the related asset. |
| Uuid | String | bf6b30d3-eea8- 4924-9f0a-*** | The ID of the related asset. |
| Name | String | Malicious processes (cloud threat detection) - XOR DDoS trojan | The complete name of the exception. |
| EventSubType | String | XorDDoS trojan | The name of the exception. |
| Level | String | serious | The severity level of the exception. Valid values: serious suspicious remind |
| EventStatus | Integer | 1 | The status of the exception. Valid values: 1: unhandled 2: ignored 4: confirmed 8: marked as false positive 16: handling 32: handled 64: expired |
| Desc | String | webshell | The impact of the exception. |

| Developer Guide·Th | reat Detection |   | Apsara Stack Securit |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| OperateMsg | String | success | The operation remarks of the exception. |
| DataSource | String | aegis suspicious *** _ _ | The data source. |
| CanBeDealOnLin e | Boolean | true | Indicates whether the online processing of the exception is supported. The processing includes quarantining the exception. Valid values: t rue: Online processing is supported. f alse: Online processing is not supported. |
| SaleVersion | String | 1 | The version in which the exception detection can be enabled. Valid values: 0: Basic Edition 1: Enterprise Edition |
| AlarmEventTyp e | String | Suspicious processes | The type of the alert event. |
| AlarmEventNa me | String | Suspicious command running in scheduled Linux tasks | The name of the alert event. |
| AlarmUniqueInf o | String | 8df914418f*** | The ID of the alert event. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSuspEvents &From=saas
```

Sample success responses `XML` format

```xml
<DescribeSuspEvents>
  <TotalCount>3</TotalCount>
  <Count>2</Count>
  <PageSize>20</PageSize>
  <RequestId>0C7FAD74-83FA-4671-9250-A5F2A64F437A</RequestId>
  <CurrentPage>1</CurrentPage>
  <SuspEvents>
        <EventStatus>1</EventStatus>
        <SaleVersion>1</SaleVersion>
        <IntranetIp>1.2.3.4</IntranetIp>
        <EventSubType>XOR DDoS trojan</EventSubType>
        <Name>Malicious processes (cloud threat detection) - XOR DDoS trojan</Name>
        <DataSource>aegis_suspiciou***</DataSource>
        <OccurrenceTime>2018-09-26 01:51:01</OccurrenceTime>
        <InstanceName>server01</InstanceName>
        <Desc>After accessing the server, XOR DDoS trojan may have injected malicious code
into Linux scheduled tasks. </Desc>
        <CanBeDealOnLine>false</CanBeDealOnLine>
        <Uuid>bf6b30d3-eea8-4924***</Uuid>
        <InternetIp>1.2.3.4</InternetIp>
        <Level>serious</Level>
        <Id>3682</Id>
        <LastTime>2018-10-24 21:06:01</LastTime>
  </SuspEvents>
  <SuspEvents>
        <EventStatus>1</EventStatus>
        <SaleVersion>1</SaleVersion>
        <IntranetIp>1.2.3.5</IntranetIp>
        <EventSubType>XOR DDoS trojan</EventSubType>
        <Name>Malicious processes (cloud threat detection) - XOR DDoS trojan</Name>
        <DataSource>aegis_suspiciou***</DataSource>
        <OccurrenceTime>2018-09-26 02:01:01</OccurrenceTime>
        <InstanceName>server01</InstanceName>
        <Desc>After accessing the server, XOR DDoS trojan may have injected malicious code
into Linux scheduled tasks. </Desc>
        <CanBeDealOnLine>false</CanBeDealOnLine>
        <Uuid>bf6b30d3-eea8-4924-***</Uuid>
        <InternetIp>1.2.3.4</InternetIp>
        <Level>serious</Level>
        <Id>3683</Id>
        <LastTime>2018-10-24 21:01:01</LastTime>
  </SuspEvents>
</DescribeSuspEvents>
```

`JSON` format

```json
    "TotalCount": 3,
    "Count": 2,
    "PageSize": 20,
    "RequestId": "0C7FAD74-83FA-4671-9250-A5F2A64F437A",
    "CurrentPage": 1,
    "SuspEvents": [
            "EventStatus": 1,
            "SaleVersion": "1",
            "IntranetIp": "1.2.3.4",
            "EventSubType": "XOR DDoS trojan"
            "Name": "Malicious processes (cloud threat detection) - XOR DDoS trojan",
            "DataSource": "aegis_suspiciou***",
            "OccurrenceTime": "2018-09-26 01:51:01",
            "InstanceName": "server01",
            "Desc": "After accessing the server, XOR DDoS trojan may have injected maliciou
s code into Linux scheduled tasks.",
            "CanBeDealOnLine": false,
            "Uuid": "bf6b30d3-eea8-4924***",
            "InternetIp": "1.2.3.4",
            "Level": "serious",
            "Id": 3682,
            "LastTime": "2018-10-24 21:06:01"
```

`},`

```json
            "EventStatus": 1,
            "SaleVersion": "1",
            "IntranetIp": "1.2.3.5",
            "EventSubType": "XOR DDoS trojan"
            "Name": "Malicious processes (cloud threat detection) - XOR DDoS trojan",
            "DataSource": "aegis_suspiciou***",
            "OccurrenceTime": "2018-09-26 02:01:01",
            "InstanceName": "server01",
            "Desc": "After accessing the server, XOR DDoS trojan may have injected maliciou
s code into Linux scheduled tasks.",
            "CanBeDealOnLine": false,
            "Uuid": "bf6b30d3-eea8-4924-***",
            "InternetIp": "1.2.3.4",
            "Level": "serious",
            "Id": 3683,
            "LastTime": "2018-10-24 21:01:01"
```

`]` For a list of error codes, see Error codes.

#### 3.5.6 DescribeSuspEventDetail

Queries details of a specific exception. An alert event consists of alerts and exceptions. Each alert event is related to multiple exceptions.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSuspEven tDetail | The operation that you want to perform. Set the value to DescribeSuspEvent Det ail. |
| From | String | Yes | sas | The data source on which the exception is detected. Set the value to sas. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| SuspiciousEventId | Integer | No | 1 | The ID of the exception to query. Not e To query the details of an exception, you must provide the ID of the exception. You can call the DescribeSuspEvents operation to obtain the ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1 | The ID of the request. |
| LastTime | String | 2018-10-30 11:43:46 | The last time when the exception occurred. |
| Id | Integer | 1991 | The ID of the exception to query. |
| InstanceName | String | ca cpm test1 _ _ | The name of the related asset. |

| eveloper Guide·Th ervice (TDS) | reat Detection |   | Apsara Stack Securit |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| InternetIp | String | 1.2.3.5 | The public IP address of the related asset. |
| IntranetIp | String | 1.2.3.1 | The private IP address of the related asset. |
| Uuid | String | bffb12c3-590a- 4db2-b538-*** | The ID of the related asset. |
| EventDesc | String | This file may have been uploaded by an attacker that has intruded into your website. Check the validity of this file. | The description of the exception. |
| EventTypeDesc | String | Webshell - Webshell | The type of the exception. |
| Level | String | serious | The severity level of the exception. Valid values: serious suspicious remind |
| EventStatus | String | 1 | The status of the exception. Valid values: 1: unhandled 2: ignored 4: confirmed 8: marked as false positive 16: handling 32: handled 64: expired |
| SaleVersion | String | 1 | The version in which exception detection can be enabled. Valid values: 0: Basic Edition 1: Enterprise Edition |
| DataSource | String | aegis suspicious *** _ _ | The data source on which the exception is detected. |
| OperateMsg | String | success | The operation remarks of the exception. |

| psara Stack Securi | ty |   | Developer Guide·Threat Detection Service (TDS |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| SasId | String | 1sdeswdd**** | The ID of the service in Threat Detection Service. |
| EventName | String | WEBSHELL | The name of the exception. |
| CanBeDealOnLin e | Boolean | true | Indicates whether the online processing of the exception is supported. Valid values: true: Online processing is supported. false: Online processing is not supported. |
| Details | Array |   | The details of the exception. |
| Name | String | The update time. | The name in the exception details. |
| Type | String | html | The format in the exception details. Valid values: t ext ht ml |
| InfoType | String | download url _ | The type of the icon. |
| Value | String | 2018-12-12 12:00:00 | The content in the exception details. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSuspEventDetail &From=sas
```

Sample success responses `XML` format

```xml
<DescribeSuspEventDetailResponse>
  <RequestId>43F670F3-AB40-4E91-BC7D-C57468834F67</RequestId>
  <EventDesc>This file may have been uploaded by an attacker that has intruded into your we
bsite. Check the validity of this file. </EventDesc>
  <EventTypeDesc>Webshell - Webshell</EventTypeDesc>
  <EventStatus>1</EventStatus>
  <EventName>WEBSHELL</EventName>
  <SaleVersion>1</SaleVersion>
<IntranetIp>1234</IntranetIp>
```

```xml
  <IntranetIp>1.2.3.4</IntranetIp>
  <DataSource>aegis_suspicious_***</DataSource>
  <InstanceName>ca_***</InstanceName>
  <CanBeDealOnLine>true</CanBeDealOnLine>
  <OperateMsg></OperateMsg>
  <Uuid>bffb12c3-590a-4db2-b538-***</Uuid>
  <Details>
        <Type>text</Type>
        <Value>/data/ftpUser/pub/***</Value>
        <InfoType>trojan_path</InfoType>
        <Name>Trojan path</Name>
  </Details>
  <Details>
        <Type>text</Type>
        <Value>--</Value>
        <Name>Affected domain</Name>
  </Details>
  <Details>
        <Type>text</Type>
        <Value>2018-10-30 05:00:56</Value>
        <InfoType>frist_found_time</InfoType>
        <Name>First detected time<Name>
  </Details>
  <Details>
        <Type>text</Type>
        <Value>2018-10-30 11:43:45</Value>
        <InfoType>update_time</InfoType>
        <Name>Update time</Name>
  </Details>
  <Details>
        <Type>text</Type>
        <Value>Webshell</Value>
        <InfoType>trojan_type</InfoType>
        <Name>Trojan type</Name>
  </Details>
  <Details>
        <Type>html</Type>
        <Value>&lt;a href="http:// bucket*"&gt; Download&lt;/a&gt;</Value>
        <InfoType>download_url</InfoType>
        <Name>Source file download</Name>
  </Details>
  <InternetIp>1.2.3.5</InternetIp>
  <Level>serious</Level>
  <Id>129636</Id>
  <LastTime>2018-10-30 11:43:46</LastTime>
  <SasId>39938056</SasId>
</DescribeSuspEventDetailResponse>
```

`JSON` format

```json
    "RequestId": "43F670F3-AB40-4E91-BC7D-C57468834F67",
    "EventDesc": "This file may have been uploaded by an attacker that has intruded into yo
ur website. Check the validity of this file.",
```

```json
    "EventTypeDesc": "Webshell - Webshell",
    "EventStatus": 1,
    "EventName": "WEBSHELL",
    "SaleVersion": "1",
    "IntranetIp": "1.2.3.4",
    "DataSource": "aegis_suspicious_***",
    "InstanceName": "ca_***",
    "CanBeDealOnLine": true,
    "OperateMsg": "",
    "Uuid": "bffb12c3-590a-4db2-b538-***",
    "Details": [
            "Type": "text",
            "Value": "/data/ftpUser/pub/***",
            "InfoType": "trojan_path",
            "Name": "Trojan path",
```

`},`

```json
            "Type": "text",
            "Value": "--",
            "Name": "Affected domain",
```

`},`

```json
            "Type": "text",
            "Value": "2018-10-30 05:00:56",
            "InfoType": "frist_found_time",
            "Name": "First detected time",
```

`},`

```json
            "Type": "text",
            "Value": "2018-10-30 11:43:45",
            "InfoType": "update_time",
            "Name": "Update time",
```

`},`

```json
            "Type": "text",
            "Value": "Webshell",
            "InfoType": "trojan_type",
            "Name": "Trojan type",
```

`},`

```json
            "Type": "html",
            "Value": "<a href=\" http:// ${* \"> Download </a>",
            "InfoType": "download_url",
            "Name":"Source file download",
```

`],`

```json
    "InternetIp": "1.2.3.5",
    "Level": "serious",
    "Id": 129636,
    "LastTime": "2018-10-30 11:43:46",
    "SasId": "39938056"
```

For a list of error codes, see Error codes.

#### 3.5.7 HandleSimilarSecurityEvents

Handles alerts triggered by the same rule or rules of the same type at a time.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | HandleSimilarSec urityEvents | The operation that you want to perform. Set the value to HandleSimilarSecurityEvents. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| TaskId | Long | No | 113 | The ID of the task that handles multiple alerts of the same type at a time. |
| OperationCode | String | No | ignore | The operation that is performed to handle alerts of the same type at a time. Valid values: deal: quarantines the source file of the malicious process. kill and quara: kills the malicious _ _ processes and quarantines the source file. kill virus: removes the source file _ of the malicious process. block ip: blocks the source IP _ addresses. ignore: ignores the alerts. mark mis inf o: marks the alerts as _ _ false positives by adding them to the whitelist. rm mark mis inf o: cancels false _ _ _ positives by removing the alerts from the whitelist. of f line handled: marks the alerts _ as handled. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| OperationParams | String | No | {"expireTime":15 78475919533} | The parameter values of the operation that is performed to handle alerts of the same type at a time. This parameter must be specified if the OperationCode parameter is set to one of the following values: kill and quara _ _ block ip _ |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1B080663-F4E6- 4736-89B9- 48FC43E160A7 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=HandleSimilarSecurityEvents
```

Sample success responses `XML` format

```xml
<requestId>1B080663-F4E6-4736-89B9-48FC43E160A7</requestId>
```

`JSON` format

```json
  "requestId": "1B080663-F4E6-4736-89B9-48FC43E160A7"
```

For a list of error codes, see Error codes.

#### 3.5.8 DescribeSecurityEventOperations

Queries operations that can be performed to handle alerts.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSecurityE ventOperations | The operation that you want to perform. Set the value to DescribeSecurityEventOperations. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| SecurityEventId | Long | No | 89621 | The ID of the alert. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F661324F-F381- 4218-A0F4- 7A901FB39EED | The ID of the request. |
| SecurityEventO perationsRespo nse | Array |   | The operation performed on the alert. |
| OperationCode | String | ignore | The code of the operation performed on the alert. |
| OperationPara ms | String | qqqqq | The operation parameters. |
| UserCanOperat e | Boolean | true | Indicates whether you can handle the alert. Valid values: true: You can handle the alert. false: You cannot handle the alert. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSecurityEventOperations
```

Sample success responses `XML` format

```xml
<code>200</code> <data>
    <SecurityEventOperationsResponse>
        <OperationCode>mark_mis_info</OperationCode>
        <UserCanOperate>true</UserCanOperate>
    </SecurityEventOperationsResponse>
    <SecurityEventOperationsResponse>
        <OperationCode>ignore</OperationCode>
        <UserCanOperate>true</UserCanOperate>
    </SecurityEventOperationsResponse>
</data> <requestId>F661324F-F381-4218-A0F4-7A901FB39EED</requestId>
```

`JSON` format

```json
  "code": 200,
  "data": {
    "SecurityEventOperationsResponse": [
        "OperationCode": "mark_mis_info",
        "UserCanOperate": true
```

`},`

```json
        "OperationCode": "ignore",
        "UserCanOperate": true
```

`]` `},`

```json
  "requestId": "F661324F-F381-4218-A0F4-7A901FB39EED"
```

For a list of error codes, see Error codes.

#### 3.5.9 DescribeSecurityEventOperationStatus

Queries the processing status of alerts that are triggered by the same rule or rules of the same type.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSecurityE ventOperationSta tus | The operation that you want to perform. Set the value to DescribeSecurityEventOperationStatus. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| TaskId | Long | No | 12121 | The ID of the task that handles the alerts. |
| SecurityEventIds. N | RepeatLi st | No | ["909361"] | The list of alert IDs. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1683940A-E4AE- 4473-8C40- F4075434B76B | The ID of the request. |
| SecurityEventO perationStatus Response | Struct |   | The response of the request. |
| TaskStatus | String | Success | The status of the task that handles the alerts. Valid values: Processing: The task is running. Success: The task is successful. Failure: The task failed. Pending: The task is pending. |
| SecurityEventO perationStatus es | Array |   | The list of the processing status of the alerts. |
| SecurityEventId | String | 12321 | The ID of the alert. |
| Status | String | Success | The processing status of the alert. Valid values: Processing: The task is running. Success: The task is successful. Failed: The task failed. |
| ErrorCode | String | ignore.Success | The code that indicates the processing result of the alert. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSecurityEventOperationStatus
```

Sample success responses `XML` format

```xml
<SecurityEventOperationStatusResponse>
    <SecurityEventOperationStatuses>
        <Status>Success</Status>
        <SecurityEventId>908872</SecurityEventId>
        <ErrorCode>ignore.Success</ErrorCode>
    </SecurityEventOperationStatuses>
    <SecurityEventOperationStatuses>
        <Status>Success</Status>
        <SecurityEventId>909758</SecurityEventId>
        <ErrorCode>ignore.Success</ErrorCode>
    </SecurityEventOperationStatuses>
    <SecurityEventOperationStatuses>
        <Status>Success</Status>
        <SecurityEventId>910655</SecurityEventId>
        <ErrorCode>ignore.Success</ErrorCode>
    </SecurityEventOperationStatuses>
    <TaskStatus>Success</TaskStatus>
</SecurityEventOperationStatusResponse> <requestId>1683940A-E4AE-4473-8C40-F4075434B76B</requestId>
```

`JSON` format

```json
    "SecurityEventOperationStatusResponse": {
        "SecurityEventOperationStatuses": [{
            "Status": "Success",
            "SecurityEventId": 908872,
            "ErrorCode": "ignore.Success"
        }, {
            "Status": "Success",
            "SecurityEventId": 909758,
            "ErrorCode": "ignore.Success"
        }, {
            "Status": "Success",
            "SecurityEventId": 910655,
            "ErrorCode": "ignore.Success"
        }],
        "TaskStatus": "Success"
```

`},`

```json
    "requestId": "1683940A-E4AE-4473-8C40-F4075434B76B"
```

For a list of error codes, see Error codes.

#### 3.5.10 CreateSimilarSecurityEventsQueryTask

Creates a task to query alerts triggered by the same rule or rules of the same type.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateSimilarSecu rityEventsQueryT ask | The operation that you want to perform. Set the value to CreateSimilarSecurityEventsQueryTask. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| SecurityEventId | Long | No | 14323 | The ID of the alert. |
| SimilarEventScena rioCode | String | No | default | The codes of alerts that are triggered by the same rule or rules of the same type. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5861EE3E-F0B3- 48B8-A5DC- A5080BFBE052 | The ID of the request. |
| CreateSimilarSe curityEventsQue ryTaskRespons e | Struct |   | The response of the task that queries alerts of the same type. |
| TaskId | Long | 2915 | The ID of the task. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | String | DataRetrieved | The status of the task. New: The task is new. Ret rievingDat a: Data is being retrieved. Dat aRet rieved: Data is retrieved. Processing: The task is running. Success: The task is successful. Failed: The task failed. Part ialFailed: The task is partially failed. |

Sample requests

```
http(s)://[Endpoint]/?Action=CreateSimilarSecurityEventsQueryTask
```

Sample success responses `XML` format

```xml
<code>200</code> <data>
    <CreateSimilarSecurityEventsQueryTaskResponse>
        <Status>DataRetrieved</Status>
        <TaskId>2915</TaskId>
    </CreateSimilarSecurityEventsQueryTaskResponse>
</data> <requestId>5861EE3E-F0B3-48B8-A5DC-A5080BFBE052</requestId>
```

`JSON` format

```json
  "code": 200,
  "data": {
    "CreateSimilarSecurityEventsQueryTaskResponse": {
      "Status": "DataRetrieved",
      "TaskId": 2915
```

`},`

```json
  "requestId": "5861EE3E-F0B3-48B8-A5DC-A5080BFBE052"
```

For a list of error codes, see Error codes.

#### 3.5.11 DescribeSimilarSecurityEvents

Queries alerts triggered by the same rule or rules of the same type.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSimilarSe curityEvents | The operation that you want to perform. Set the value to DescribeSimilarSecurityEvents. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| TaskId | Long | No | 111 | The ID of the task. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| PageSize | Integer | No | 5 | The number of entries to return on each page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 97B9CBC6-F869- 4860-9CBC- A7310F85AE8E | The ID of the request. |
| SecurityEventsR esponse | Array |   | The list of alerts that are of the same type. |
| SecurityEventId | Long | 123 | The ID of the alert. |
| Uuid | String | qweeqq-13232- daweq-wqeqe | The UUID of the server. |
| EventType | String | Suspicious network connections | The type of the alert. |
| EventName | String | Visiting malicious domains | The name of the alert. |

| psara Stack Securi | ty |   | Developer Guide·Threat Detection Service (TDS |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| OccurrenceTim e | Long | 1577379820000 | The timestamp when the first exception occurred. |
| LastTime | Long | 1577441301000 | The timestamp when the exception last occurred. |
| PageInfo | Struct |   | The page information. |
| Count | Integer | 12 | The number of entries returned on the current page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| TotalCount | Integer | 23 | The number of alerts that are of the same type. |
| CurrentPage | Integer | 1 | The page number of the current page. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSimilarSecurityEvents
```

Sample success responses `XML` format

```xml
<code>200</code> <data>
    <PageInfo>
        <TotalCount>2</TotalCount>
        <PageSize>5</PageSize>
        <CurrentPage>1</CurrentPage>
        <Count>2</Count>
    </PageInfo>
    <SecurityEventsResponse>
        <OccurrenceTime>1576686364000</OccurrenceTime>
        <SecurityEventId>124</SecurityEventId>
        <Uuid>123-aasd-dsa-dadsa</Uuid>
        <EventType>Suspicious network connections</EventType>
        <EventName>Visiting malicious domains</EventName>
        <LastTime>1577063771000</LastTime>
    </SecurityEventsResponse>
    <SecurityEventsResponse>
        <OccurrenceTime>1577379820000</OccurrenceTime>
        <SecurityEventId>123</SecurityEventId>
        <Uuid>ewqeqweq-12311-sdfasf-afafsa</Uuid>
        <EventType>Suspicious network connections</EventType>
        <EventName>Visiting malicious domains</EventName>
        <LastTime>1577441301000</LastTime>
    </SecurityEventsResponse>
</data> <requestId>97B9CBC6-F869-4860-9CBC-A7310F85AE8E</requestId>
```

`JSON` format

```json
  "code": 200,
  "data": {
    "PageInfo": {
      "TotalCount": 2,
      "PageSize": 5,
      "CurrentPage": 1,
      "Count": 2
```

`},`

```json
    "SecurityEventsResponse": [
        "OccurrenceTime": 1576686364000,
        "SecurityEventId": 124,
        "Uuid": "123-aasd-dsa-dadsa",
        "EventType": "Suspicious network connections",
        "EventName": "Visiting malicious domains",
        "LastTime": 1577063771000
```

`},`

```json
        "OccurrenceTime": 1577379820000,
        "SecurityEventId": 123,
        "Uuid": "qweeqq-13232-daweq-wqeqe",
        "EventType": "Suspicious network connections",
        "EventName": "Visiting malicious domains",
        "LastTime": 1577441301000
```

`]` `},`

```json
  "requestId": "97B9CBC6-F869-4860-9CBC-A7310F85AE8E"
```

For a list of error codes, see Error codes.

#### 3.5.12 DescribeSimilarEventScenarios

Queries the scenarios where alerts triggered by the same rule or rules of the same type are managed.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSimilarEv entScenarios | The operation that you want to perform. Set the value to DescribeSimilarEventScenarios. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

| S | Developer Guide·Thre ervice (TDS) | at Detection |   |   | Apsara Stack Securit | y |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SecurityEventId | Long | No | 12321 | The ID of the alert. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | FDF7B8D9-8493- 4B90-8D13- E0C1FFCE5F97 | The ID of the request. |
| Scenarios | Array |   | The list of scenarios where alerts triggered by the same rule or rules of the same type are managed. |
| Code | String | same url _ | The code of the scenario. Valid values: def ault : the same alert type same f ile cont ent : the same file _ _ content rule same ip: the same IP address rule _ same url: the same URL rule _ |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSimilarEventScenarios
```

Sample success responses `XML` format

```xml
<Scenarios>
    <Code>same_url</Code>
</Scenarios> <Scenarios>
    <Code>default</Code>
</Scenarios> <requestId>FDF7B8D9-8493-4B90-8D13-E0C1FFCE5F97</requestId>
```

`JSON` format

```json
    "Scenarios": [{
        "Code": "same_url"
    }, {
        "Code": "default"
    }],
    "requestId": "FDF7B8D9-8493-4B90-8D13-E0C1FFCE5F97"
```

For a list of error codes, see Error codes.

#### 3.5.13 DescribeUserLayoutAuthorization

Queries whether the brute-force attacks protection feature has been authorized. The brute-force attacks protection feature cannot be used without authorization.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeUserLayo utAuthorization | The operation that you want to perform. Set the value to DescribeUserLayout Aut horizat ion. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Authorized | Boolean | false | The result of the query. Valid values: t rue: authorized f alse: not authorized |
| RequestId | String | 4A80EE8F-2175- 49DA-B8BF- FAE1B3D52E4C | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeUserLayoutAuthorization
```

Sample success responses `XML` format

```xml
<DescribeUserLayoutAuthorizationResponse>
      <Authorized>false</Authorized>
      <requestId>4A80EE8F-2175-49DA-B8BF-FAE1B3D52E4C</requestId>
</DescribeUserLayoutAuthorizationResponse>
```

`JSON` format

```json
    "Authorized": false,
    "requestId": "4A80EE8F-2175-49DA-B8BF-FAE1B3D52E4C"
```

For a list of error codes, see Error codes.

#### 3.5.14 RollbackSuspEventQuaraFile

Removes a quarantined file from the quarantine box.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RollbackSuspEven tQuaraFile | The operation that you want to perform. Set the value to RollbackSuspEvent QuaraFile. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| QuaraFileId | Integer | No | 3921797 | The ID of the quarantined file. Not e If this parameter is not set, the operation does not remove a quarantined file from the quarantine box. You can call the DescribeSuspEventQuaraFiles operation to obtain the ID of the target quarantined file. |
| From | String | No | sas | The ID of the request source. Set the value to sas. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 52A3AEE6-114A- 499D-8990- 4BA9B27FE0AA | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=RollbackSuspEventQuaraFile
```

Sample success responses `XML` format

```xml
<RollbackSuspEventQuaraFileResponse>
      <RequestId>52A3AEE6-114A-499D-8990-4BA9B27FE0AA</RequestId>
</RollbackSuspEventQuaraFileResponse>
```

`JSON` format

```json
    "RequestId": "52A3AEE6-114A-499D-8990-4BA9B27FE0AA"
```

For a list of error codes, see Error codes.

#### 3.5.15 DescribeSuspEventQuaraFiles

Queries the quarantined files by page.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSuspEven tQuaraFiles | The operation that you want to perform. Set the value to DescribeSuspEvent QuaraFiles. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| PageSize | String | No | 20 | The number of quarantined files to return on each page. |
| Status | String | No | quaraDone | The status of the quarantined files to be queried. Valid values: quaraFailed: The system failed to quarantine the file. quaraDone: The system has quarantined the file. quaraing: The file is being quarantined. rollbackFailed: The system failed to cancel the quarantine. rollbackDone: The system has canceled the quarantine. rollbacking: The quarantine is being canceled. |
| CurrentPage | String | No | 1 | The number of pages to be returned. |
| From | String | No | sas | The service of the request. Set the value to sas. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 1 | The total number of pages returned. |

| psara Stack Securi | ty |   | Developer Guide·Threat Detection Service (TDS |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| CurrentPage | Integer | 1 | The page number of the current page. |
| PageSize | Integer | 20 | The number of quarantined files returned per page. |
| QuaraFiles | Array |   | The list of quarantined files. |
| EventName | String | WEBSHELL | The name of the event. |
| EventType | String | WebshellQuaraEvent Type | The type of the event. |
| Id | Integer | 3920516 | The ID of the quarantined file. |
| InstanceName | String | abc | The ID of the server where the file is located. |
| InternetIp | String | 47.XX.XX.131 | The public IP address of the server where the file is located. |
| Ip | String | 47.XX.XX.131 | The public IP address of the server where the file is located. |
| Md5 | String | 5ddebe926acc7ed3 9a664409bfd0ec10 | The MD5 value of the file. |
| ModifyTime | String | 2020-06-11 20:37:08 | The update time. |
| Path | String | /var/www/html/we bshell-sample- master/others/defc 3e21bab59e2a2ab4 9f7eda99f65f83d4d 349.jpg | The path where the quarantined file is stored on the server. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | String | rollbackDone | The status of quarantine. Valid values: quaraFailed: The system failed to quarantine the file. quaraDone: The system has quarantined the file. quaraing: The file is being quarantined. rollbackFailed: The system failed to cancel the quarantine. rollbackDone: The system has canceled the quarantine. rollbacking: The quarantine is being canceled. |
| Tag | String | 228f890e56eae9eec 6a42c7ea801b538 | The ID of the event. |
| Uuid | String | 04a0e735-ad32- 4835-b635- 0458d77b**** | The UUID of the server. |
| RequestId | String | 6AD0BA1B-0129- 498F-B82A- 17C7B8368A08 | The ID of the request. |
| TotalCount | Integer | 20 | The total number of quarantined files. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSuspEventQuaraFiles
```

Sample success responses `XML` format

```xml
<DescribeSuspEventQuaraFilesResponse>
      <TotalCount>20</TotalCount>
      <RequestId>6AD0BA1B-0129-498F-B82A-17C7B8368A08</RequestId>
      <PageSize>20</PageSize>
      <CurrentPage>1</CurrentPage>
      <QuaraFiles>
            <Path>/var/www/html/webshell-sample-master/others/defc3e21bab59e2a2ab49f7eda99f
65f83d4d349.jpg</Path>
            <InstanceName>abc</InstanceName>
            <Status>rollbackDone</Status>
            <ModifyTime>2020-06-11 20:37:08</ModifyTime>
            <Uuid>04a0e735-ad32-4835-b635-0458d77b****</Uuid>
            <InternetIp>47.XX.XX.131</InternetIp>
            <EventType>WebshellQuaraEventType</EventType>
            <Ip>47.XX.XX.131</Ip>
            <EventName>WEBSHELL</EventName>
            <Id>3920516</Id>
            <Tag>228f890e56eae9eec6a42c7ea801b538</Tag>
            <Md5>5ddebe926acc7ed39a664409bfd0ec10</Md5>
      </QuaraFiles>
      <Count>1</Count>
</DescribeSuspEventQuaraFilesResponse>
```

`JSON` format

```json
    "TotalCount": "20",
    "RequestId": "6AD0BA1B-0129-498F-B82A-17C7B8368A08",
    "PageSize": "20",
    "CurrentPage": "1",
    "QuaraFiles": [{
        "Path": "/var/www/html/webshell-sample-master/others/defc3e21bab59e2a2ab49f7eda99f6
5f83d4d349.jpg",
        "InstanceName": "abc",
        "Status": "rollbackDone",
        "ModifyTime": "2020-06-11 20:37:08",
        "Uuid": "04a0e735-ad32-4835-b635-0458d77b****",
        "InternetIp": "47.XX.XX.131",
        "EventType": "WebshellQuaraEventType",
        "Ip": "47.XX.XX.131",
        "EventName": "WEBSHELL",
        "Id": "3920516",
        "Tag": "228f890e56eae9eec6a42c7ea801b538",
        "Md5": "5ddebe926acc7ed39a664409bfd0ec10"
    }],
    "Count": "1"
```

For a list of error codes, see Error codes.

### 3.6 Configuration assessment

#### 3.6.1 DescribeRiskItemType

Queries types of check items for cloud service configurations. Each check item is categorized into a type. Types of check items include identity authentication and permissions, network access control, log auditing, data security, monitoring and alerting, and basic security protection.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRiskItem Type | The operation that you want to perform. Set the value to DescribeRiskItemType. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| List | Array |   | The information about the check item. |
| Id | Long | 1 | The ID of the check item. |
| Title | String | Identity authentication and permissions | The type of the check item. Example: Identity authentication and permissions. |
| RequestId | String | 3B3F3A90-46A5- 4023-A2D8- D68B14262F96 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeRiskItemType
```

Sample success responses `XML` format

```xml
<DescribeRiskItemType>
   <RequestId>3B3F3A90-46A5-4023-A2D8-D68B14262F96</RequestId>
   <List>
      <Title>Identity authentication and permissions</Title>
      <Id>1</Id>
   </List>
   <List>
      <Title>Network access control</Title>
      <Id>2</Id>
   </List>
   <List>
      <Title>Log auditing</Title>
      <Id>3</Id>
   </List>
   <List>
      <Title>Data security</Title>
      <Id>4</Id>
   </List>
   <List>
      <Title>Basic security protection</Title>
      <Id>6</Id>
   </List>
    </DescribeRiskItemType>
```

`JSON` format

```json
 "RequestId":"3B3F3A90-46A5-4023-A2D8-D68B14262F96",
 "List":[
   "Id":1,
   "Title":"Identity authentication and permissions"
```

`},`

```json
   "Id":2,
   "Title":"Network access control"
```

`},`

```json
   "Id":3,
   "Title":"Log auditing"
```

`},`

```json
   "Id":4,
   "Title":"Data security"
```

`},`

```json
   "Id":6,
   "Title":"Basic security protection"
```

`]` For a list of error codes, see Error codes.

#### 3.6.2 StartBaselineSecurityCheck

Checks cloud service configurations. You can check all items or a specific item, and you can verify whether an item is already checked.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | StartBaselineSecu rityCheck | The operation that you want to perform. Set the value to St art BaselineSecurit yCheck. |
| Type | String | Yes | check | The type of the check task. Valid values: check verify |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| ItemIds.N | RepeatLi st | No | 1 | The ID of the check item. Not e To perform the check task on cloud service configurations, you must provide the ID of the check item. You can call the DescribeRiskItemType operation to obtain the ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 48D2E9A9-A1B0- 4295-B727- 0995757C47E9 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=StartBaselineSecurityCheck &Type=check
```

Sample success responses `XML` format

```xml
<StartBaselineSecurityCheckResponse>
  <RequestId>48D2E9A9-A1B0-4295-B727-0995757C47E9</RequestId>
</StartBaselineSecurityCheckResponse>
```

`JSON` format

```json
    "RequestId":"48D2E9A9-A1B0-4295-B727-0995757C47E9"
```

For a list of error codes, see Error codes.

#### 3.6.3 DescribeRiskCheckSummary

Queries the summary of check items for cloud service configurations. The operation returns the following information: the number of risk items, the risk rate, the number of affected assets, the last check time, and the statistics of each type of check items.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRiskChec kSummary | The operation that you want to perform. Set the value to DescribeRiskCheckSummary. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 291B49F9-1685- 4005-9D34- 606B6F78740F | The ID of the request. |
| RiskCheckSumm ary | Struct |   | The summary of check items for cloud service configurations. |
| RiskCount | Integer | 1 | The number of risk items. |
| PreviousCount | Integer | 0 | The number of risk items in the last check. |
| ItemCount | Integer | 4 | The number of check items. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RiskRate | Float | 0.25 | The proportion of risk items in the total number to check items. |
| AffectedAssetC ount | Integer | 0 | The number of affected assets. |
| PreviousTime | Long | 1545012926000 | The timestamp of the last check. |
| EnabledRiskCou nt | Integer | 3 | The number of check items that passed the check. |
| DisabledRiskCo unt | Integer | 0 | The number of risk items that failed to pass the check. |
| RiskLevelCount | Array |   | The number of risk items for each level. high medium low |
| Key | String | medium | The severity level of the risk item. |
| Count | Integer | 1 | The number of risk items. |
| Groups | Array |   | The types of check items. |
| Id | Long | 1 | The type ID of the check item. |
| Title | String | Identity authentication and permissions | The type of the check item. |
| Status | String | finish | Indicates whether the check is finished. f inish: The check is finished. Running: The check is in process. wait ing: The check is pending. NoSt art : The check is not started. |
| RemainingTime | Integer | 0 | The time when the next check will be performed. |

| S | Developer Guide·Th ervice (TDS) | reat Detection |   | Apsara Stack Securit | y |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Sort | Integer | 1 | The sequence number of the check item type in the All T ypes drop-down list in the console. |
| CountByStatus | Array |   | The statistics of check results. |
| Status | String | pass | The status of the check item after the check is finished. Valid values: pass: The check item is normal. f ailed: The check item is at risk. |
| Count | Integer | 2 | The number of risk items. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeRiskCheckSummary
```

Sample success responses `XML` format

```xml
<DescribeRiskCheckSummary>
      <RequestId>291B49F9-1685-4005-9D34-606B6F78740F</RequestId>
      <RiskCheckSummary>
            <RiskCount>1</RiskCount>
            <RiskRate>0.25</RiskRate>
            <PreviousTime>1545012926000</PreviousTime>
            <ItemCount>4</ItemCount>
            <AffectedAssetCount>0</AffectedAssetCount>
            <RiskLevelCount>
                  <Count>1</Count>
                  <Key>medium</Key>
            </RiskLevelCount>
            <Groups>
                  <Status>finish</Status>
                  <CountByStatus>
                        <Status>exception</Status>
                        <Count>2</Count>
                  </CountByStatus>
                  <RemainingTime>0</RemainingTime>
                  <Sort>1</Sort>
                  <Title>Identity authentication and permissions</Title>
                  <Id>1</Id>
            </Groups>
<Groups>
```

```xml
            <Groups>
                  <Status>finish</Status>
                  <CountByStatus>
                        <Status>exception</Status>
                        <Count>5</Count>
                  </CountByStatus>
                  <RemainingTime>0</RemainingTime>
                  <Sort>2</Sort>
                  <Title>Network access control</Title>
                  <Id>2</Id>
            </Groups>
            <Groups>
                  <Status>finish</Status>
                  <CountByStatus>
                        <Status>pass</Status>
                        <Count>1</Count>
                  </CountByStatus>
                  <RemainingTime>0</RemainingTime>
                  <Sort>3</Sort>
                  <Title>Log auditing</Title>
                  <Id>3</Id>
            </Groups>
            <Groups>
                  <Status>finish</Status>
                  <CountByStatus>
                        <Status>exception</Status>
                        <Count>2</Count>
                  </CountByStatus>
                  <RemainingTime>0</RemainingTime>
                  <Sort>4</Sort>
                  <Title>Data security</Title>
                  <Id>4</Id>
            </Groups>
            <Groups>
                  <Status>finish</Status>
                  <CountByStatus>
                        <Status>exception</Status>
                        <Count>2</Count>
                  </CountByStatus>
                  <RemainingTime>0</RemainingTime>
                  <Sort>6</Sort>
                  <Title>Basic security protection</Title>
                  <Id>6</Id>
            </Groups>
            <PreviousCount>0</PreviousCount>
      </RiskCheckSummary>
    </DescribeRiskCheckSummary>
```

`JSON` format

```json
  "RequestId": "291B49F9-1685-4005-9D34-606B6F78740F",
  "RiskCheckSummary": {
    "RiskCount": 1,
```

```json
    "RiskRate": 0.25,
    "PreviousTime": 1545012926000,
    "ItemCount": 4,
    "AffectedAssetCount": 0,
    "RiskLevelCount": [
        "Count": 1,
        "Key": "medium"
```

`],`

```json
    "Groups": [
        "Status": "finish",
        "CountByStatus": [
            "Status": "exception",
            "Count": 2
```

`],`

```json
        "RemainingTime": 0,
        "Sort": 1,
        "Title": "Identity authentication and permissions",
        "Id": 1
```

`},`

```json
        "Status": "finish",
        "CountByStatus": [
            "Status": "exception",
            "Count": 5
```

`],`

```json
        "RemainingTime": 0,
        "Sort": 2,
        "Title": "Network access control",
        "Id": 2
```

`},`

```json
        "Status": "finish",
        "CountByStatus": [
            "Status": "pass",
            "Count": 1
```

`],`

```json
        "RemainingTime": 0,
        "Sort": 3,
        "Title": "Log auditing",
        "Id": 3
```

`},`

```json
        "Status": "finish",
        "CountByStatus": [
"Status":"exception"
```

```json
            "Status": "exception",
            "Count": 2
```

`],`

```json
        "RemainingTime": 0,
        "Sort": 4,
        "Title": "Data security",
        "Id": 4
```

`},`

```json
        "Status": "finish",
        "CountByStatus": [
            "Status": "exception",
            "Count": 2
```

`],`

```json
        "RemainingTime": 0,
        "Sort": 6,
        "Title": "Basic security protection",
        "Id": 6
```

`],`

```json
    "PreviousCount": 0
```

For a list of error codes, see Error codes.

#### 3.6.4 ModifyRiskCheckStatus

Modifies the status of a check result. You can ignore a result or mark a result as a false positive.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyRiskCheckS tatus | The operation that you want to perform. Set the value to Modif yRiskCheckSt at us. |
| ItemId | Long | Yes | 1 | The ID of the check item. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Status | String | Yes | ignored | The method to process the check result. Valid values: ignored reset |
| TaskId | Long | Yes | 57 | The ID of the check task to which the check item belongs. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 48D2E9A9-A1B0- 4295-B727- 0995757C47E9 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyRiskCheckStatus &ItemId=1 &TaskId=57 &Status=ignored
```

Sample success responses `XML` format

```xml
<ModifyRiskCheckStatusResponse>
      <RequestId>48D2E9A9-A1B0-4295-B727-0995757C47E9</RequestId>
</ModifyRiskCheckStatusResponse>
```

`JSON` format

```json
    "RequestId":"48D2E9A9-A1B0-4295-B727-0995757C47E9"
```

For a list of error codes, see Error codes.

#### 3.6.5 DescribeRiskCheckResult

Queries the results of check items by type or name.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRiskChec kResult | The operation that you want to perform. Set the value to DescribeRiskCheckResult . |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| GroupId | Long | No | 21000 | The type ID of the check item. Valid values: 1: identity authentication and permissions 2: network access control 3: log auditing 4: data security 5: monitoring and alerting 6: basic security protection |
| CurrentPage | Integer | No | 1 | The page number of the current page. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RiskLevel | String | No | high | The severity level of the check item. Valid values: high medium low |
| Status | String | No | pass | The status of the check result. Valid values: pass f ailed running wait ing ignored f alsePosit ive |
| ItemIds.N | RepeatLi st | No | sde*** | The ID of the check item. For more information about the description of the check items specified by this parameter, see the check item table in the "Response parameters" section of this topic. |
| AssetType | String | No | RDS | The type of the cloud service. For more information about the description of the cloud services specified by this parameter, see the check item table in the "Response parameters" section of this topic. |
| Name | String | No | Cloud platform - Multi-factor authentication configuration of Apsara Stack tenant accounts | The name of the check item. For more information about the description of the check item name, see the check item table in the "Response parameters" section of this topic. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 10 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| List | Array |   | The information about the check item. |
| AffectedCount | Integer | 0 | The number of the affected assets. |
| CheckTime | Long | 1543991525000 | The timestamp when the last check was performed. |
| ItemId | Long | 1 | The ID of the check item. For more information about the description of the check item ID specified by this parameter, see the check item table in the "Response parameters" section of this topic. |
| RemainingTime | Integer | 0 | The time when the next check will be performed. |
| RepairStatus | String | disabled | Indicates whether the risk of the check item can be fixed. Valid values: enabled: The risk can be fixed. disabled: The risk cannot be fixed. |
| RiskAssertType | String | ECS | The type of the affected asset. |
| RiskItemResour ces | Array |   | The details of the check item. |
| ContentResourc e | Json | {"type": "link", "value": "Risk: Multi- factor authentication is disabled\n", "url": "https://***.aliyun.c om/#/secure\n" } | The content in the check item details. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ResourceName | String | bestPractice | The title in the check item details. Valid values: best Pract ice: description inf luence: risk suggest ion: solution helpResource: reference |
| RiskLevel | String | high | The severity level of the check item. Valid values: high medium low |
| Sort | Integer | 1 | The sequence number of the check result. The check items are sorted based on the sequence number. |
| StartStatus | String | enabled | Indicates whether the check item is supported by the cloud service. Valid values: enabled: supported disable: unsupported |
| Status | String | pass | The status of the check result. Valid values: pass f ailed running wait ing ignored f alsePosit ive |
| TaskId | Long | 647189 | The ID of the check task. |
| Title | String | Cloud platform - Multi-factor authentication configuration of Apsara Stack tenant accounts | The name of the check item. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Type | String | Identity authentication and permissions | The type of the check item. Valid values: Ident it y aut hent icat ion and permissions Net work access cont rol Log audit ing Dat a securit y Monit oring and alert ing Basic securit y prot ect ion |
| PageCount | Integer | 20 | The total number of pages returned. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | AD271C07-4ACE- 413D-AA9B- F14FD3B7717F | The ID of the request. |
| TotalCount | Integer | 12 | The total number of entries returned. |

The following table describes the check items supported by the cloud platform, including the ID, name, type, risk level, and service type.

| ID | Name | Type | Severity level | Service type | Description |
|---|---|---|---|---|---|

| ID | Name | Type | Severity level | Service type | Description |
|---|---|---|---|---|---|
| 1 | ActionTrail - Logging configuration | 3: log auditing | medium | ActionTrail | Checks whether you enable ActionTrail to record operations logs on the cloud and save the logs to Object Storage Service (OSS) buckets. |
| 2 | ApsaraDB for RDS - Database security policy | 4: data security | medium | RDS | Checks whether you enable Secure Sockets Layer (SSL), Transparent Data Encryption (TDE), and SQL audit services for each ApsaraDB for RDS instance. |

| ID | Name | Type | Severity level | Service type | Description |
|---|---|---|---|---|---|
| 3 | Apsara Stack tenant account security - Multi-factor authentication | 1: identity authentication and permissions | high | RAM | Checks whether MFA is enabled for Apsara Stack tenant accounts. |
| 4 | Apsara Stack Security - Anti- DDoS Pro or Anti-DDoS Premium back- to-origin configuration | 2: network access control | high | DDOS | Checks whether actual IP addresses of backend servers are hidden after you use Anti- DDoS Pro or Anti-DDoS Premium. If the actual IP addresses are hidden, attackers cannot directly access the actual IP addresses. <note> To hide the actual IP addresses, you can configure whitelist policies, for example, when the actual IP addresses are the IP addresses of Server Load Balancer (SLB) instances. When the IP addresses are the IP addresses of Elastic Compute Service (ECS) instances, you can configure |

| ID | Name | Type | Severity level | Service type | access control pDoesli crieipst fioonr ECS security |
|---|---|---|---|---|---|
|   |   |   |   |   | groups. All these policies allow access from only back-to-origin IP addresses of Anti-DDoS Pro or Anti- DDoS Premium. </note> |
| 5 | ApsaraDB for RDS - Whitelist configuration | 2: network access control | high | RDS | Checks whether the RDS access control policy is set to 0.0.0.0/0, which allows requests from all IP addresses. We recommend that you limit the access scope to a specific range of IP addresses |
|   |   |   |   |   | rather than exposing database services to the Internet. |
| 6 | SLB - High-risk port | 2: network access control | high | SLB | Checks whether SLB forwards requests from high-risk ports to the Internet. |

| ID | Name | Type | Severity level | Service type | Description |
|---|---|---|---|---|---|
| 7 | Apsara Stack Security - Web Application Firewall (WAF) back-to-origin configuration | 2: network access control | high | WAF | Checks whether the actual IP addresses of backend servers are hidden after you use WAF. If the actual IP addresses are hidden, attackers cannot directly access the actual IP addresses. To hide the actual IP addresses, you can configure whitelist policies, for example, when the actual IP addresses are the IP addresses of Server Load Balancer (SLB) instances. When the IP addresses are the IP addresses of Elastic Compute Service (ECS) instances, you can configure access control policies for ECS security groups. All these policies allow access from only back-to-origin IP addresses of WAF. |

| ID | Name | Type | Severity level | Service type | Description |
|---|---|---|---|---|---|
| 8 | Apsara Stack Security - Threat Detection Service agent online status | 6: basic security protection | high | ECS | Checks whether the Threat Detection Service agent on the ECS instance is always online and provides protection. |
| 12 | OSS - Bucket access permissions | 4: data security | high | OSS | Checks whether the access permissions on your OSS buckets is public-read or public-read- write. If yes, the check fails. |
| 13 | Threat Detection Service - AccessKey leak detection | 5: monitoring and alerting | medium | RAM | Checks whether AccessKey leak detection is enabled. If no, the check fails. |
|   |   |   |   |   | Checks whether the whitelist is enabled for ApsaraDB for MongDB |
| 14 | ApsaraDB for MongoDB - Whitelist configuration | 2: network access control | high | MongoDB | instances. If the whitelist is enabled and set to 0.0.0.0/0, which allows access from all devices, the check fails. |

| ID | Name | Type | Severity level | Service type | Description |
|---|---|---|---|---|---|
| 15 | RAM - MFA configuration for RAM users | 1: identity authentication and permissions | medium | RAM | Checks whether MFA is enabled for RAM users. |
| 16 | OSS - Logging configuration | 4: data security | medium | OSS | Checks whether the logging feature is enabled for all OSS buckets. If no, the check fails. |
| 17 | OSS - Cross- region replication configuration | 4: data security | low | OSS | Checks whether the cross-region replication is enabled for all OSS buckets. If no, the check fails. |
| 18 | ApsaraDB for RDS - Backup configuration | 4: data security | medium | RDS | Checks whether database backup is enabled for ApsaraDB for RDS instances. If no, the check fails. |
| 19 | KVStore for Redis - Whitelist configuration | 2: network access control | high | Redis | Checks access control configurations of KVStore for Redis. |
| 20 | ECS - SSH key pairs | 1: identity authentication and permissions | medium | ECS | Checks whether SSH key pair-based logons are enabled for ECS instances. |

| ID | Name | Type | Severity level | Service type | Description |
|---|---|---|---|---|---|
| 21 | SLB - Health status | 5: monitoring and alerting | low | SLB | Checks the health status of SLB instances. |
| 22 | PolarDB - Whitelist configuration | 2: network access control | medium | POLARDB | Checks the whitelist configured for PolarDB. If the whitelist is enabled and set to 0.0.0.0/0, which allows access from all devices, the check fails. |
| 23 | AnalyticDB for PostgreSQL - Whitelist configuration | 2: network access control | medium | PostgreSQL | Checks the whitelist of the AnalyticDB for PostgreSQL instance. If the whitelist is enabled and set to 0.0.0.0/0, which allows access from all devices, the check fails. |
| 24 | ECS - Storage encryption | 4: data security | low | ECS | Checks whether storage encryption is enabled. If no, the check fails. |

| ID | Name | Type | Severity level | Service type | Description |
|---|---|---|---|---|---|
| 25 | SLB - Whitelist configuration | 2: network access control | medium | SLB | Checks SLB whitelist configurations . If the whitelist is enabled and set to 0.0.0.0/0, which allows access from all devices, the check fails. |
| 26 | SLB - Certificate expiration | 5: monitoring and alerting | medium | SLB | Checks whether the SLB certificate has expired. |
| 27 | ECS - Automatic snapshot policy | 4: data security | medium | ECS | Checks whether automatic snapshot policies are enabled for ECS instances. |
| 28 | SSL certificate - Expiration check | 4: data security | medium | SSL | Checks whether the SSL certificate is within its validity period. |
| 30 | OSS - Server- side encryption | 4: data security | low | OSS | Checks whether server-side encryption is enabled for OSS buckets. |
| 31 | OSS - Hotlinking protection | 2: network access control | low | OSS | Checks whether hotlinking protection is configured for OSS buckets. |

| ID | Name | Type | Severity level | Service type | Description |
|---|---|---|---|---|---|
| 32 | ApsaraDB for RDS - Cross- region backup configuration | 4: data security | low | RDS | Checks whether cross-region backup is enabled for ApsaraDB for RDS instances. |
| 33 | ApsaraDB for MongoDB - Backup configuration | 4: data security | medium | MongoDB | Checks whether data backup is enabled for ApsaraDB for MongoDB instances. |
| 34 | ApsaraDB for MongoDB - Log auditing | 3: log auditing | medium | MongoDB | Checks whether log auditing is enabled for ApsaraDB for MongoDB instances. |
| 35 | ApsaraDB for MongoDB - SSL certificate | 4: data security | medium | MongoDB | Checks whether SSL certificate checks are enabled for ApsaraDB for MongoDB instances. |
| 36 | Cloud Monitor - Host monitoring plug-in | 5: monitoring and alerting | medium | CloudMonitor | Checks whether the status of the Cloud Monitor agent is normal. |

| ID | Name | Type | Severity level | Service type | Description |
|---|---|---|---|---|---|
| 37 | ECS - Security group policies | 2: network access control | medium | ECS | Checks the ECS security group policies. |
| 38 | VPC - DNAT management port mapping | 2: network access control | medium | VPC | Checks whether a VPC DNAT rule is configured to map management ports to the Internet. |
| 39 | KVStore for Redis - Backup configuration | 4: data security | medium | Redis | Checks whether data backup is enabled for KVStore for Redis. |
| 40 | Container Registry - Repository permission configurations | 4: data security | high | CR | Checks whether permissions are correctly configured for the repository in Container Registry. |
| 41 | Container Registry - Security scan | 6: basic security protection | low | CR | Checks whether security scan is enabled for Container Registry. |
| 42 | SLB - Access logging configuration | 3: log auditing | medium | SLB | Checks whether access logging is configured for SLB instances. |

| ID | Name | Type | Severity level | Service type | Description |
|---|---|---|---|---|---|
| 43 | KVStore for Redis - Log auditing | 3: log auditing | low | Redis | Checks whether log auditing is configured for KVStore for Redis. |
| 44 | OSS - Authorization policy | 1: identity authentication and permissions | medium | OSS | Checks whether correct authorization policies are enabled for OSS. |
| 46 | PolarDB - Backup configuration | 4: data security | medium | POLARDB | Checks whether the backup configuration is enabled for PolarDB. |
| 47 | PolarDB - SQL explorer | 3: log auditing | medium | POLARDB | Checks whether SQL Explorer is enabled for PolarDB. |
| 48 | Apsara Stack tenant account security - AccessKey pair | 1: identity authentication and permissions | medium | RAM | Checks whether the AccessKey pair is enabled for your Apsara Stack tenant account. |
| 50 | CDN - Real- time logging | 3: log auditing | medium | CDN | Checks whether real- time logging push is enabled for CDN. |

| ID | Name | Type | Severity level | Service type | Description |
|---|---|---|---|---|---|
| 51 | KVStore for Redis - SSL certificate | 4: data security | medium | Redis | Checks whether KVStore for Redis uses SSL certificates. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeRiskCheckResult &GroupId=1 &RiskLevel=high
```

Sample success responses `XML` format

```xml
<DescribeRiskCheckResultResponse>
      <TotalCount>12</TotalCount>
      <RequestId>AD271C07-4ACE-413D-AA9B-F14FD3B7717F</RequestId>
      <PageCount>20</PageCount>
      <PageSize>10</PageSize>
      <CurrentPage>1</CurrentPage>
      <List>
            <Status>pass</Status>
            <CheckTime>1543991525000</CheckTime>
            <TaskId>647189</TaskId>
            <RemainingTime>0</RemainingTime>
            <Title>Cloud platform - MFA configuration of Apsara Stack tenant accounts</Titl
```

`e>`

```xml
            <ItemId>1</ItemId>
            <RiskAssertType>ECS</RiskAssertType>
            <Type>Identity authentication and permissions</Type>
            <StartStatus>enabled</StartStatus>
            <AffectedCount>0</AffectedCount>
            <Sort>1</Sort>
            <RepairStatus>disabled</RepairStatus>
            <RiskLevel>high</RiskLevel>
            <RiskItemResources>
                  <ContentResource>{   "type": "link",   "value": "Risk: Multi-factor authe
ntication is disabled\n", "url": "https://***.aliyun.com/#/secure\n" }</ContentResource>
                  <ResourceName>bestPractice</ResourceName>
            </RiskItemResources>
      </List>
      <Count>10</Count>
</DescribeRiskCheckResultResponse>
```

`JSON` format

```json
    "TotalCount": "12",
    "RequestId": "AD271C07-4ACE-413D-AA9B-F14FD3B7717F",
    "PageCount": "20",
    "PageSize": "10",
    "CurrentPage": "1",
    "List": {
            "Status": "pass",
            "CheckTime": "1543991525000",
            "TaskId": "647189",
            "RemainingTime": "0",
            "Title": "Cloud platform - MFA configuration of Apsara Stack tenant accounts",
            "ItemId": "1",
            "RiskAssertType": "ECS",
            "Type": "Identity authentication and permissions",
            "StartStatus": "enabled",
            "AffectedCount": "0",
            "Sort": "1",
            "RepairStatus": "disabled",
            "RiskLevel": "high",
            "RiskItemResources": {
                "ContentResource": "{   \"type\": \"link\",   \"value\": \"Risk: Multi-fact
or authentication is disabled\\n\", \"url\": \"https://***.aliyun.com/#/secure\\n\" }",
                "ResourceName": "bestPractice"
```

`},`

```json
    "Count": "10"
```

For a list of error codes, see Error codes.

#### 3.6.6 DescribeSecurityCheckScheduleConfig

Queries the custom check cycle and time period.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSecurityC heckScheduleCon fig | The operation that you want to perform. Set the value to DescribeSecurityCheckScheduleConfig. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 48D2E9A9-A1B0- 4295-B727- 0995757C47E9 | The ID of the request. |
| RiskCheckJobCo nfig |   |   | The settings of scheduled checks. |
| DaysOfWeek | String | 1,2,3 | The days when checks are performed every week. You can specify multiple days. Separate multiple days with commas (,). Valid values: 1: Monday 2: Tuesday 3: Wednesday 4: Thursday 5: Friday 6: Saturday 7: Sunday |
| EndTime | Integer | 12 | The time period during which the configuration check ends. Valid values: 6: 00:00 to 06:00 12: 06:00 to 12:00 18: 12:00 to 18:00 24: 18:00 to 24:00 |

| Parameter | Type | Example | Description |
|---|---|---|---|
| StartTime | Integer | 6 | The time period during which the configuration check starts. Valid values: 0: 00:00 to 06:00 6: 06:00 to 12:00 12: 12:00 to 18:00 18: 18:00 to 24:00 |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSecurityCheckScheduleConfig
```

Sample success responses `XML` format

```xml
<DescribeSecurityCheckScheduleConfig>
  <RiskCheckJobConfig>
        <DaysOfWeek>1,2,3</DaysOfWeek>
        <EndTime>12</EndTime>
        <StartTime>6</StartTime>
  </RiskCheckJobConfig>
  <RequestId>C17F3C01-0AFD-4898-A950-AA0129025B41</RequestId>
</DescribeSecurityCheckScheduleConfig>
```

`JSON` format

```json
 "RequestId":"C17F3C01-0AFD-4898-A950-AA0129025B41",
 "RiskCheckJobConfig":{
  "DaysOfWeek":"1,2,3",
  "EndTime":12,
  "StartTime":6
```

For a list of error codes, see Error codes.

#### 3.6.7 ModifyRiskSingleResultStatus

Changes the status of an asset affected by a check item. You can ignore an asset or mark an asset as false positive.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyRiskSingleR esultStatus | The operation that you want to perform. Set the value to ModifyRiskSingleResultStatus. |
| TaskId | Long | Yes | 57 | The ID of the check task to which the affected asset belongs. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| Ids.N | RepeatLi st | No | 1 | The ID of the affected asset. |
| Status | String | No | ignored | The status of the affected asset. Valid values: ignored: ignores the asset. f ailed: marks the asset as a false positive. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 3B3F3A90-46A5- 4023-A2D8- D68B14262F96 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyRiskSingleResultStatus &Ids.1=4 &Status=ignored &TaskId=57
```

Sample success responses `XML` format

```xml
<ModifyRiskSingleResultStatusResponse>
  <RequestId>3B3F3A90-46A5-4023-A2D8-D68B14262F96</RequestId>
</ModifyRiskSingleResultStatusResponse>
```

`JSON` format

```json
    "RequestId":"3B3F3A90-46A5-4023-A2D8-D68B14262F96"
```

For a list of error codes, see Error codes.

#### 3.6.8 ModifySecurityCheckScheduleConfig

Configures the time to automatically run a configuration check. For example, you can specify the time period during a day of the week.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySecurityCh eckScheduleConfi g | The operation that you want to perform. Set the value to ModifySecurityCheckScheduleConfig. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DaysOfWeek | String | No | 1,2,3 | The days on which the configuration check runs. You can specify multiple days. Separate multiple days with commas (,). Valid values: 1: Monday 2: Tuesday 3: Wednesday 4: Thursday 5: Friday 6: Saturday 7: Sunday |
| StartTime | Integer | No | 6 | The time period during which the configuration check starts. Valid values: 0: 00:00 to 06:00 6: 06:00 to 12:00 12: 12:00 to 18:00 18: 18:00 to 24:00 |
| EndTime | Integer | No | 12 | The time period during which the configuration check ends. 0: 00:00 to 06:00 6: 06:00 to 12:00 12: 12:00 to 18:00 18: 18:00 to 24:00 |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 48D2E9A9-A1B0- 4295-B727- 0995757C47E9 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=ModifySecurityCheckScheduleConfig &DaysOfWeek=1,2,3 &StartTime=6 &EndTime=12
```

Sample success responses `XML` format

```xml
<ModifySecurityCheckScheduleConfig>
  <RequestId>48D2E9A9-A1B0-4295-B727-0995757C47E9</RequestId>
</ModifySecurityCheckScheduleConfig>
```

`JSON` format

```json
    "RequestId":"48D2E9A9-A1B0-4295-B727-0995757C47E9"
```

For a list of error codes, see Error codes.

#### 3.6.9 DescribeRiskCheckItemResult

Queries the assets that have configuration risks based on a specific check item. Results are returned on different pages.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRiskChec kItemResult | The operation that you want to perform. Set the value to DescribeRiskCheckIt emResult . |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| ItemId | Long | No | 2 | The ID of the check item. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageContentRe source | Struct |   | The affected assets listed on each page. |
| ContentResourc e | Json | { "resultStatus": [{ "id": 32183150, "status": "failed" }], "columns": [{ "title": "Zone", "key": "RegionId" }, { "title": "Database instance ID", "key": "DBInstanceId" }, { "title": "Error entry value", "key": "VulValue" }], "values": [{ "DBInstanceId": { "type": "link", "value": "dds- bp144b42843fed14\ n", "url": "https://mongodb. console.aliyun.com/ replicate/cn- hangzhou/instances /dds- bp144b42843fed14/ basicInfo" }, "VulValue": { "type": "link", "value": "0.0.0.0/0", "url": "https://mongodb. console.aliyun.com/ replicate/cn- hangzhou/instances /dds- bp144b42843fed14/ whiteList" }, "RegionId": { "type": "text", "value": "China(Hangzhou)\n " } }], "emptyGridValue": { "type": "text", "value": "No data found" }, "type": "grid" } | The data of affected assets displayed on each page in a dynamic table. |
| Count | Integer | 1 | The number of entries returned on the current page. |

| S | Developer Guide·Th ervice (TDS) | reat Detection |   | Apsara Stack Securit | y |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| CurrentPage | Integer | 1 | The page number of the current page. |
| PageCount | Integer | 3 | The total number of returned pages. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| TotalCount | Integer | 1 | The total number of entries. |
| RequestId | String | 3BFB4989-A108- 46A4-954E- FF7EF02D1078 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeRiskCheckItemResult
```

Sample success responses `XML` format

```xml
<DescribeRiskCheckItemResultResponse>
      <PageContentResource>
            <TotalCount>1</TotalCount>
            <ContentResource>
                  <resultStatus>
                        <id>32183150</id>
                        <status>failed</status>
                  </resultStatus>
                  <columns>
                        <title>Zone</title>
                        <key>RegionId</key>
                  </columns>
                  <columns>
                        <title>Database instance ID</title>
                        <key>DBInstanceId</key>
                  </columns>
                  <columns>
                        <title>Error entry value</title>
                        <key>VulValue</key>
                  </columns>
                  <values>
                        <DBInstanceId>
                              <type>link</type>
                              <value>dds-bp144b42843xxxxx</value>
                              <url>https://mongodb.console.aliyun.com/replicate/cn-hangzhou
/instances/dds-bp144b42843fed14/basicInfo</url>
                        </DBInstanceId>
                        <VulValue>
                              <type>link</type>
                              <value>0.0.0.0/0</value>
                              <url>https://mongodb.console.aliyun.com/replicate/cn-hangzhou
/instances/dds-bp144b42843fed14/whiteList</url>
                        </VulValue>
                        <RegionId>
                              <type>text</type>
                              <value>China (Hangzhou)</value>
                        </RegionId>
                  </values>
                  <emptyGridValue>
                        <type>text</type>
                        <value>No data found</value>
                  </emptyGridValue>
                  <type>grid</type>
            </ContentResource>
            <PageCount>1</PageCount>
            <PageSize>10</PageSize>
            <CurrentPage>1</CurrentPage>
            <Count>1</Count>
      </PageContentResource>
      <requestId>3BFB4989-A108-46A4-954E-FF7EF02D1078</requestId>
</DescribeRiskCheckItemResultResponse>
```

`JSON` format

| { "PageContentResource": { "TotalCount": 1, "ContentResource": { "resultStatus": [{ "id": 32183150, "status": "failed" }], "columns": [{ "title": "Zone", "key": "RegionId" }, { "title": "Database instance ID", "key": "DBInstanceId" }, { "title": "Error entry value", "key": "VulValue" }], "values": [{ "DBInstanceId": { "type": "link", "value": "dds-bp144b42843xxxxx\n", "url": "https://mongodb.console.aliyun.com/replicate/cn-hangzhou/instances/ dds-bp144b42843fed14/basicInfo" }, "VulValue": { "type": "link", "value": "0.0.0.0/0", "url": "https://mongodb.console.aliyun.com/replicate/cn-hangzhou/instances/ dds-bp144b42843fed14/whiteList" }, "RegionId": { "type": "text", "value": "China (Hangzhou)\n" } }], "emptyGridValue": { "type": "text", "value": "No data found" }, "type": "grid" }, "PageCount": 1, "PageSize": 10, "CurrentPage": 1, "Count": 1 }, "requestId": "3BFB4989-A108-46A4-954E-FF7EF02D1078" } |   |
|---|---|

For a list of error codes, see Error codes.

### 3.7 Brute-force attacks protection

#### 3.7.1 CreateAntiBruteForceRule

Creates a defense rule against brute-force attacks protection.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateAntiBruteF orceRule | The operation that you want to perform. Set the value to Creat eAnt iBrut eForceRule. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Name | String | No | The defense rules against brute-force attacks protection. | The name of the defense rule. |
| Span | Integer | No | 15 | The time period during which the number of logon attempts are calculated. |
| FailCount | Integer | No | 10 | The maximum number of logon attempts specified in the defense rule. |
| ForbiddenTime | Integer | No | 10 | The time period during which logons from the blocked IP address are blocked. |
| UuidList.N | RepeatLi st | No | uuid-1312133- ssas,uuid-1234- qwer-dss | The list of servers to which the defense rule is applied. |
| DefaultRule | Boolean | No | true | Specifies whether to set the defense rule as the default rule. Valid values: t rue: The defense rule is set as the default rule. f alse: The defense rule is not set as the default rule. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| CreateAntiBrute ForceRule | Struct |   | The returned result of the defense rule. |
| RuleId | Long | 6363 | The ID of the defense rule. |
| RequestId | String | FB3E435F-4116- 46F9-A5DE- C338DDA04F47 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=CreateAntiBruteForceRule
```

Sample success responses `XML` format

```xml
<CreateAntiBruteForceRuleResponse>
  <CreateAntiBruteForceRule>
        <RuleId>6363</RuleId>
  </CreateAntiBruteForceRule>
  <requestId>FB3E435F-4116-46F9-A5DE-C338DDA04F47</requestId>
</CreateAntiBruteForceRuleResponse>
```

`JSON` format

```json
    "CreateAntiBruteForceRule": {
        "RuleId": 6363
```

`},`

```json
    "requestId": "FB3E435F-4116-46F9-A5DE-C338DDA04F47"
```

For a list of error codes, see Error codes.

#### 3.7.2 ModifyAntiBruteForceRule

Modifies the defense rule against brute-force attacks protection.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyAntiBruteF orceRule | The operation that you want to perform. Set the value to ModifyAntiBruteForceRule. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Id | Long | No | 6263 | The ID of the defense rule. |
| Name | String | No | Best practices | The name of the defense rule. |
| Span | Integer | No | 10 | The time period during which the number of logon attempts are calculated. |
| FailCount | Integer | No | 10 | The maximum number of logon attempts specified in the defense rule. |
| ForbiddenTime | Integer | No | 12 | The time period during which logons from the blocked IP address are blocked. |
| UuidList.N | RepeatLi st | No | uuid-13213- dasda | The list of servers to which the defense rule is applied. |
| DefaultRule | Boolean | No | true | Specifies whether to set the defense rule as the default rule. t rue: The defense rule is set as the default rule. f alse: The defense rule is not set as the default rule. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F35F45B0-5D6B- 4238-BE02- A62D0760E840 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyAntiBruteForceRule
```

Sample success responses `XML` format

```xml
<ModifyAntiBruteForceRuleResponse>
  <requestId>F35F45B0-5D6B-4238-BE02-A62D0760E840</requestId>
</ModifyAntiBruteForceRuleResponse>
```

`JSON` format

```json
    "requestId": "F35F45B0-5D6B-4238-BE02-A62D0760E840"
```

### 3.8 Vulnerability management

#### 3.8.1 ModifyVulTargetConfig

Configures vulnerability detection on a server.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVulTarget Config | The operation that you want to perform. Set the value to ModifyVulTargetConfig. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Type | String | No | vul | The type of the configuration. |
| Uuid | String | No | xxxx-xxxx-xxxx- xxxxx-xxxxxx | The UUID of the server. |
| Config | String | No | cms | The details of the configuration items. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 3A85CFCF-05C8- 451A-9E41- C0D5E96BA407 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyVulTargetConfig
```

Sample success responses `XML` format

```xml
<requestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</requestId>
```

`JSON` format

```json
  "requestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F"
```

For a list of error codes, see Error codes.

#### 3.8.2 ModifyStartVulScan

Scans vulnerabilities on the Vulnerabilities page.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyStartVulSc an | The operation that you want to perform. Set the value to Modif ySt art VulScan. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Types | String | No | "cve,sys,cms,app, emg" | The types of vulnerabilities that can be detected by Threat Detection Service. Valid values: cve: Linux software vulnerabilities sys: Windows vulnerabilities cms: Web CMS vulnerabilities app: application vulnerabilities emg: emergency vulnerabilities image: container image vulnerabilities Not e If this parameter is not specified, all types of vulnerabilities are detected. |
| Uuids | String | No | {"i-sdada- xxxxx","i- ifaedada- sfsasdxxx"} | The list of servers. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4066CAC3-F83A- 4729-9995- A5558A61B546 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyStartVulScan
```

Sample success responses `XML` format

```xml
<ModifyStartVulScanResponse>
      <requestId>4066CAC3-F83A-4729-9995-A5558A61B546</requestId>
</ModifyStartVulScanResponse>
```

`JSON` format

```json
    "requestId": "4066CAC3-F83A-4729-9995-A5558A61B546"
```

For a list of error codes, see Error codes.

#### 3.8.3 DescribeVulList

Queries vulnerabilities by type.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVulList | The operation that you want to perform. Set the value to DescribeVulList . |
| Type | String | Yes | cve | The type of the vulnerability. Valid values: cve: Linux software vulnerabilities sys: Windows vulnerabilities cms: Web CMS vulnerabilities app: application vulnerabilities emg: emergency vulnerabilities |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| Remark | String | No | 1.2.3.4 | The tag to query, which can be the internal IP address, public IP address, or name of the asset. |
| Uuids | String | No | 1587bedb-fdb4- 48c4-9330- ************ | The ID of the asset. Separate multiple IDs with commas (,). |
| AliasName | String | No | RHSA-2019:0230- Important: polkit security update | The alias of the vulnerability. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Necessity | String | No | asap,later,nntf | The priority to fix vulnerabilities. Separate multiple priorities with commas (,). Valid values: asap: high lat er: medium nnt f : low |
| Dealed | String | No | n | Specifies whether the vulnerability is handled. Valid values: y: handled n: unhandled |
| CurrentPage | Integer | No | 1 | The page number of the current page. Pages start from page 1. Default value: 1. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. Default value: 20. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | ECDE6715-6286- 40E6-A32D- 3094051FD74D | The ID of the request. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| TotalCount | Integer | 2 | The total number of entries returned. |
| VulRecords | Array |   | The vulnerability information. |
| AliasName | String | RHSA-2017:0574: gnutls security, bug fix, and enhancement update | The alias of the vulnerability. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ExtendContentJ son | Struct |   | The extended information. |
| AbsolutePath | String | /roo/www/web | The package path of the software that has the vulnerability. |
| AliasName | String | RHSA-2017:0574: gnutls security, bug fix, and enhancement update | The alias of the vulnerability. |
| Ip | String | 1.2.3.1 | The public IP address of the asset that is affected by the vulnerability. |
| LastTs | Long | 1554189334000 | The timestamp when the vulnerability was last detected. |
| Necessity | Struct |   | Indicates whether the vulnerability needs to be fixed. |
| Assets factor _ | String | 1 | The asset score. |
| Cvss factor _ | String | 7.8 | The Common Vulnerability Scoring System (CVSS) score. |
| Enviroment fac _ tor | String | 1.0 | The environmental score. |
| Gmt create _ | String | 20190331 | The creation time. |
| Is calc _ | String | 1 | Indicates whether the vulnerability severity score is calculated. Valid values: 0: The score is not calculated. 1: The score is calculated. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | String | normal | The status of the vulnerability severity score. Valid values: none: No score is generated. pending: The score is pending calculation. miss: The score failed to be calculated. normal: The calculation is normal. |
| Time factor _ | String | 1.0 | The temporal score. |
| Total score _ | String | 7.8 | The total vulnerability severity score. We recommend that you apply the following rules: Critical: The severity score is between 13.5 and 15, which typically represents a high-risk vulnerability. Important: The severity score is between 7.1 and 13.5, which typically represents a medium-risk vulnerability. Moderate: The severity score is below 7, which typically represents a low-risk vulnerability. |
| Os | String | centos | The operating system. |
| OsRelease | String | 7 | The version of the operating system. |
| PrimaryId | Long | 111 | The ID of the vulnerability. |
| RpmEntityList | Array |   | The details about the RPM package. |
| FullVersion | String | 3.10.0-693.2.2.el7 | The complete version number. |
| MatchDetail | String | python-perf version less than 0:3.10.0- 693.21.1.el7 | The detailed matching information of the vulnerability. |
| Name | String | python-perf | The name of the RPM package. |
| Path | String | /usr/lib64/python2. 7/site-packages | The path of the software that has the vulnerability. |

| psara Stack Securi | ty |   | Developer Guide·Threat Detection Service (TDS |
|---|---|---|---|
| Parameter | Type | Example | Description |
| UpdateCmd | String | *** update python- perf | The command that can be run to fix the vulnerability. |
| Version | String | 3.10.0 | The version of the operating system. |
| Status | Integer | 1 | The status of the vulnerability. Valid values: 1: unfixed 2: fix failed 3: rollback failed 4: fixing 5: rolling back 6: verifying 7: fixed 8: fixed and to be restarted 9: rolled back 10: ignored 11: rolled back and to be restarted 12: not found 20: expired |
| Tag | String | oval | The tag of the vulnerability. |
| cveList | List | ["CVE-2016-8610", "CVE-2017-5335" ] | The Common Vulnerabilities and Exposures (CVEs) list. |
| FirstTs | Long | 1554189334000 | The first time when the vulnerability was detected. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| GroupId | Integer | 281801 | The ID of the asset group. |
| InstanceId | String | i-bp18t*** | The ID of the asset instance. |
| InstanceName | String | Test ECS | The name of the asset instance. |
| InternetIp | String | 1.2.3.1 | The public IP address of the asset. |

| eveloper Guide·Th ervice (TDS) | reat Detection |   | Apsara Stack Securit |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| IntranetIp | String | 1.2.3.4 | The private IP address of the asset. |
| LastTs | Long | 1541207563000 | The timestamp when the vulnerability was last detected. |
| ModifyTs | Long | 1541207563000 | The timestamp when the vulnerability was modified. |
| Name | String | oval:com.redhat.rhs a:def:20170574 | The name of the vulnerability. |
| Necessity | String | asap | The priority to fix vulnerabilities. Valid values: asap: high lat er: medium nnt f : low Not e We recommend that you fix the high-level vulnerabilities as soon as possible. |
| Online | Boolean | true | Indicates whether the asset instance is online. Valid values: t rue: online f alse: offline |
| OsVersion | String | linux | The version of the operating system. |
| PrimaryId | Long | 101162078 | The ID of the vulnerability. |
| Related | String | CVE-2017-7518,CVE- 2017-12188 | The list of CVEs related to the vulnerability. Separate multiple CVEs with commas (,). |
| RepairTs | Long | 1541207563000 | The timestamp when the vulnerability was fixed. |
| ResultCode | String | 0 | The result code returned after the vulnerability is fixed. |

| psara Stack Securi | ty |   | Developer Guide·Threat Detection |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ResultMessage | String | timeout | The message returned after the vulnerability is fixed. |
| Status | Integer | 1 | The status of the vulnerability. Valid values: 1: unfixed 2: fix failed 3: rollback failed 4: fixing 5: rolling back 6: verifying 7: fixed 8: fixed and to be restarted 9: rolled back 10: ignored 11: rolled back and to be restarted 12: not found 20: expired |
| Tag | String | oval | The tag of the vulnerability. |
| Type | String | cve | The type of the vulnerability. Valid values: cve: Linux vulnerabilities sys: Windows vulnerabilities cms: Web CMS vulnerabilities emg: emergency vulnerabilities app: application vulnerabilities |
| Uuid | String | 04c56617-23fc- 43a5-ab9b- ************ | The ID of the asset. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVulList &Type=cve
```

Sample success responses `XML` format

```xml
<DescribeVulListResponse>
```

|   | <DescribeVulListResponse> <TotalCount>2</TotalCount> <RequestId>ECDE6715-6286-40E6-A32D-3094051FD74D</RequestId> <PageSize>20</PageSize> <VulRecords> <Status>1</Status> <InstanceId>i-bp18t***</InstanceId> <OsVersion>linux</OsVersion> <LastTs>1541207563000</LastTs> <Necessity>asap</Necessity> <ResultMessage>timeout</ResultMessage> <IntranetIp>1.2.3.4</IntranetIp> <Name>oval:com.redhat.rhsa:def:20170574</Name> <GroupId>281801</GroupId> <RepairTs>1541207563000</RepairTs> <InstanceName>Test ECS</InstanceName> <Type>cve</Type> <FirstTs>1554189334000</FirstTs> <Uuid>04c56617-23fc-43a5-ab9b-************</Uuid> <Related>CVE-2017-7518,CVE-2017-12188</Related> <ModifyTs>1541207563000</ModifyTs> <InternetIp>1.2.3.1</InternetIp> <AliasName>RHSA-2017:0574: gnutls security, bug fix, and enhancement update</Al iasName> <Tag>oval</Tag> <Online>true</Online> <PrimaryId>101162078</PrimaryId> <ResultCode>0</ResultCode> </VulRecords> <VulRecords> <ExtendContentJson> <Status>1</Status> <Os>centos</Os> <AliasName>RHSA-2017:0574: gnutls security, bug fix, and enhancement upda te</AliasName> <Ip>1.2.3.1</Ip> <LastTs>1554189334000</LastTs> <cveList>["CVE-2016-8610", "CVE-2017-5335" ]</cveList> <Necessity> <Status>normal</Status> <Total score>7.8</Total score> _ _ <Gmt create>20190331</Gmt create> _ _ <Cvss factor>7.8</Cvss factor> _ _ <Time factor>1.0</Time factor> _ _ <Is calc>1</Is calc> _ _ <Enviroment factor>1.0</Enviroment factor> _ _ <Assets factor>1</Assets factor> _ _ </Necessity> <RpmEntityList> <Path>/usr/lib64/python2.7/site-packages</Path> <UpdateCmd>*** update python-perf</UpdateCmd> <Version>3.10.0</Version> <FullVersion>3.10.0-693.2.2.el7</FullVersion> <MatchDetail>python-perf version less than 0:3.10.0-693.21.1.el7</M atchDetail> |   |
|---|---|---|

```xml
                        <Name>python-perf</Name>
                  </RpmEntityList>
                  <Tag>oval</Tag>
                  <OsRelease>7</OsRelease>
                  <AbsolutePath>/roo/www/web</AbsolutePath>
                  <PrimaryId>111</PrimaryId>
            </ExtendContentJson>
      </VulRecords>
      <CurrentPage>1</CurrentPage>
</DescribeVulListResponse>
```

`JSON` format

```json
        "TotalCount": "2",
        "RequestId": "ECDE6715-6286-40E6-A32D-3094051FD74D",
        "PageSize": "20",
        "VulRecords": [{
            "Status": "1",
            "InstanceId": "i-bp18t***",
            "OsVersion": "linux",
            "LastTs": "1541207563000",
            "Necessity": "asap",
            "ResultMessage": "timeout",
            "IntranetIp": "1.2.3.4",
            "Name": "oval:com.redhat.rhsa:def:20170574",
            "GroupId": "281801",
            "RepairTs": "1541207563000",
            "InstanceName": "Test ECS",
            "Type": "cve",
            "FirstTs": "1554189334000",
            "Uuid": "04c56617-23fc-43a5-ab9b-************",
            "Related": "CVE-2017-7518,CVE-2017-12188",
            "ModifyTs": "1541207563000",
            "InternetIp": "1.2.3.1",
            "AliasName": "RHSA-2017:0574: gnutls security, bug fix, and enhancement update"
```

`,`

```json
            "Tag": "oval",
            "Online": "true",
            "PrimaryId": "101162078",
            "ResultCode": "0"
        }, {
            "ExtendContentJson": {
                "Status": "1",
                "Os": "centos",
                "AliasName": "RHSA-2017:0574: gnutls security, bug fix, and enhancement upd
ate",
                "Ip": "1.2.3.1",
                "LastTs": "1554189334000",
                "cveList": "[\"CVE-2016-8610\", \"CVE-2017-5335\" ]",
                "Necessity": {
                    "Status": "normal",
                    "Total_score": "7.8",
"Gmtcreate":"20190331"
```

```json
                    "Gmt_create": "20190331",
                    "Cvss_factor": "7.8",
                    "Time_factor": "1.0",
                    "Is_calc": "1",
                    "Enviroment_factor": "1.0",
                    "Assets_factor": "1"
```

`},`

```json
                "RpmEntityList": [{
                    "Path": "/usr/lib64/python2.7/site-packages",
                    "UpdateCmd": "*** update python-perf",
                    "Version": "3.10.0",
                    "FullVersion": "3.10.0-693.2.2.el7",
                    "MatchDetail": "python-perf version less than 0:3.10.0-693.21.1.el7",
                    "Name": "python-perf"
                }],
                "Tag": "oval",
                "OsRelease": "7",
                "AbsolutePath": "/roo/www/web",
                "PrimaryId": "111"
        }],
        "CurrentPage": "1"
```

For a list of error codes, see Error codes.

#### 3.8.4 DescribeEmgVulGroup

Queries emergency vulnerabilities by group.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeEmgVulG roup | The operation that you want to perform. Set the value to DescribeEmgVulGroup. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Example | Description |
|---|---|---|---|
| EmgVulGroupLi st | Array |   | The information about the group of emergency vulnerabilities. |
| AliasName | String | Jenkins High-risk Remote Security Vulnerability (CVE - 2018 - 1999001 and CVE - 2018 - 1999002) | The alias of the vulnerability. |
| Description | String | Jenkins is an open- source program written in Java. It can be used to monitor continuous and duplicate jobs for continuous software integration. \n\nJenkins contains an arbitrary file read vulnerability. Attackers can remotely send malicious HTTP requests to the Jenkins Web server and obtain the specified file content from responses returned by the server. | The description of the vulnerability. |
| GmtPublish | Long | 1532592480000 | The timestamp when the vulnerability was released. |
| Name | String | scan:ACSV-2018- 072601 | The name of the vulnerability. |
| PendingCount | Integer | 0 | The number of pending vulnerabilities. |
| Type | String | scan | How the vulnerability is exploited. scan: scans data by using plug-ins. python: scans data by using scripts. |
| RequestId | String | E836EDA2-DBFB- 489E-8FD3- 5B141EB81A9C | The ID of the request. |

| S | Developer Guide·Th ervice (TDS) | reat Detection |   | Apsara Stack Securit | y |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Integer | 2 | The total number of vulnerabilities. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeEmgVulGroup
```

Sample success responses `XML` format

```xml
<DescribeEmgVulGroup>
  <TotalCount>2</TotalCount>
  <EmgVulGroupList>
        <Name>scan:ACSV-2018-072601</Name>
        <Status>30</Status>
        <Description>Jenkins is an open-source program written in Java. It can be used to m
onitor continuous and duplicate jobs for continuous software integration. Jenkins contains an arbitrary file read vulnerability. Attackers can remotely send maliciou s HTTP requests to the Jenkins Web server and obtain the specified file content from respon ses returned by the server. </Description>
        <PendingCount>0</PendingCount>
        <AliasName>Jenkins High-risk Remote Security Vulnerability (CVE - 2018 - 1999001 an
d CVE - 2018 - 1999002)</AliasName>
        <Type>scan</Type>
        <GmtPublish>1532592480000</GmtPublish>
  </EmgVulGroupList>
  <EmgVulGroupList>
        <Name>scan:acsv-2018-082001</Name>
        <Status>30</Status>
        <Description>Recently, security researchers revealed multiple high-risk Metinfo vul
nerabilities, such as arbitrary file read, XML External Entity (XXE), and sensitive informa tion leak. </Description>
        <PendingCount>0</PendingCount>
        <AliasName>Metinfo Multiple High-risk Vulnerabilities</AliasName>
        <Type>scan</Type>
        <GmtPublish>1534767031000</GmtPublish>
  </EmgVulGroupList>
  <RequestId>E836EDA2-DBFB-489E-8FD3-5B141EB81A9C</RequestId>
</DescribeEmgVulGroup>
```

`JSON` format

```json
 "TotalCount":2,
 "EmgVulGroupList":[
   "Name":"scan:ACSV-2018-072601",
   "Status":30,
   "Description":"Jenkins is an open-source program written in Java. It can be used to moni
tor continuous and duplicate jobs for continuous software integration. \n\nJenkins contains an arbitrary file read vulnerability. Attackers can remotely send malicious HTTP requests t o the Jenkins Web server and obtain the specified file content from responses returned by t he server.",
   "PendingCount":0,
   "AliasName":"Jenkins High-risk Remote Security Vulnerability (CVE - 2018 - 1999001 and C
VE - 2018 - 1999002)",
   "Type":"scan",
   "GmtPublish":1532592480000
```

`},`

```json
   "Name":"scan:acsv-2018-082001",
   "Status":30,
   "Description":"Recently, security researchers revealed multiple high-risk Metinfo vulner
abilities, such as arbitrary file read, XML External Entity (XXE), and sensitive informatio n leak.
   "PendingCount":0,
   "AliasName":"Metinfo Multiple High-risk Vulnerabilities",
   "Type":"scan",
   "GmtPublish":1534767031000
```

`],`

```json
 "RequestId":"E836EDA2-DBFB-489E-8FD3-5B141EB81A9C"
```

For a list of error codes, see Error codes.

#### 3.8.5 DescribeVulWhitelist

Queries the whitelist of vulnerabilities by page.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVulWhite list | The operation that you want to perform. Set the value to DescribeVulWhitelist. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| CurrentPage | Integer | No | 1 | The number of the page to return. Pages start from page 1. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Default value: 20. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| CurrentPage | Integer | 1 | The page number of the current page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 74F97EF7-B543- 43FD-A4E9- 18456731F9C5 | The ID of the request. |
| TotalCount | Integer | 1 | The total number of returned entries. |
| VulWhitelists | Array |   | The information about the vulnerability whitelist. |
| AliasName | String | RHSA-2017:3263: curl security update | The alias of the vulnerability. |
| Name | String | oval:com.redhat.rhs a:def:20173263 | The name of the vulnerability. |
| Reason | String | Not urgent | The reason for adding the vulnerability to the whitelist. |
| Type | String | cve | The type of the vulnerability. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVulWhitelist
```

Sample success responses `XML` format

```xml
<DescribeVulWhitelist>
  <TotalCount>1</TotalCount>
  <VulWhitelists>
        <Name>oval:com.redhat.rhsa:def:20173263</Name>
        <AliasName>RHSA-2017:3263: curl security update</AliasName>
        <Type>cve</Type>
        <Reason>Not urgent</Reason>
  </VulWhitelists>
  <PageSize>3</PageSize>
  <RequestId>74F97EF7-B543-43FD-A4E9-18456731F9C5</RequestId>
  <CurrentPage>1</CurrentPage>
</DescribeVulWhitelist>
```

`JSON` format

```json
 "TotalCount":1,
 "PageSize":3,
 "VulWhitelists":[
   "Name":"oval:com.redhat.rhsa:def:20173263",
   "AliasName":"RHSA-2017:3263: curl security update",
   "Type":"cve",
   "Reason":"Not urgent"
```

`],`

```json
 "RequestId":"74F97EF7-B543-43FD-A4E9-18456731F9C5",
 "CurrentPage":1
```

For a list of error codes, see Error codes.

#### 3.8.6 DescribeConcernNecessity

Queries the priority to fix the vulnerability.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeConcern Necessity | The operation that you want to perform. Set the value to DescribeConcernNecessity. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ConcernNecessi ty | List | [ "asap", "later", "nntf"] | The priority to fix the vulnerability. Valid values: asap: high later: medium nntf: low |
| RequestId | String | 9139DAF6-5CE0- 49A0-926E- 07243A290F70 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeConcernNecessity &Lang=zh
```

Sample success responses `XML` format

```xml
<DescribeConcernNecessity>
  <ConcernNecessity>asap</ConcernNecessity>
  <ConcernNecessity>later</ConcernNecessity>
  <ConcernNecessity>nntf</ConcernNecessity>
  <RequestId>9139DAF6-5CE0-49A0-926E-07243A290F70</RequestId>
</DescribeConcernNecessity>
```

`JSON` format

```json
 "ConcernNecessity":[
  "asap",
  "later",
  "nntf"
```

`],`

```json
 "RequestId":"9139DAF6-5CE0-49A0-926E-07243A290F70"
```

For a list of error codes, see Error codes.

#### 3.8.7 DescribeGroupedVul

Queries information about vulnerabilities by group.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeGrouped Vul | The operation that you want to perform. Set the value to DescribeGroupedVul. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| Type | String | No | cve | The type of the vulnerability. Valid values: cve: Linux vulnerabilities sys: Windows vulnerabilities cms: Web CMS vulnerabilities app: application vulnerabilities emg: emergency vulnerabilities |
| Uuids | String | No | d42f938c-d962- 48a0-90f9- 05e4ea****** | The IDs of the asset instances. Separate multiple IDs with commas (,). |
| AliasName | String | No | RHSA-2019:0230- Important: polkit security update | The alias of the vulnerability. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Necessity | String | No | asap,later,nntf | The priority to fix the vulnerability. Separate multiple priorities with commas (,). Valid values: asap: high lat er: medium nnt f : low |
| Dealed | String | No | n | Specifies whether the vulnerability is handled. y: handled n: unhandled |
| CurrentPage | Integer | No | 1 | The page number of the current page. Pages start from page 1. Default value: 1. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. Default value: 20. |
| GroupId | String | No | weds**** | The ID of the asset group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0DFCADBA-7065- 42DA-AF17- 6868B9C2A8CF | The ID of the request. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| TotalCount | Integer | 2 | The total number of entries returned. |
| GroupedVulIte ms | Array |   | Details about vulnerabilities by group. |
| Name | String | ***glibc security and bug fixes | The name of the vulnerability. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AliasName | String | RHSA-2019:0230- Important: polkit security update | The alias of the vulnerability. |
| Type | String | cve | The type of the vulnerability. Valid values: cve: Linux vulnerabilities sys: Windows vulnerabilities cms: Web CMS vulnerabilities app: application vulnerabilities emg: emergency vulnerabilities |
| GmtLast | Long | 1554185744000 | The time when the vulnerability was last detected. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| AsapCount | Integer | 0 | The number of high-priorit y vulnerabilities. |
| LaterCount | Integer | 0 | The number of medium-priorit y vulnerabilities. |
| NntfCount | Integer | 59 | The number of low-priorit y vulnerabilities. |
| HandledCount | Integer | 0 | The total number of handled vulnerabilities. |
| Tags | String | Force restart | The tag of the vulnerability. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeGroupedVul &Lang=zh &Type=cve &AliasName=RHSA-2019:0230-Important: polkit security update &Necessity=asap,later,nntf &Dealed=n &CurrentPage=1 &PageSize=20
```

Sample success responses `XML` format

```xml
<DescribeGroupedVul>
  <GroupedVulItems>
        <Tags></Tags>
        <LaterCount>0</LaterCount>
        <AliasName>RHSA-2019:0230-Important: polkit security update</AliasName>
        <AsapCount>0</AsapCount>
        <Type>cve</Type>
        <NntfCount>59</NntfCount>
        <GmtLast>1554185744000</GmtLast>
        <HandledCount>0</HandledCount>
  </GroupedVulItems>
  <GroupedVulItems>
        <Tags></Tags>
        <LaterCount>0</LaterCount>
        <AliasName>RHSA-2019:0368-Important: systemd security update</AliasName>
        <AsapCount>0</AsapCount>
        <Type>cve</Type>
        <NntfCount>59</NntfCount>
        <GmtLast>1554185744000</GmtLast>
        <HandledCount>0</HandledCount>
  </GroupedVulItems>
  <TotalCount>432</TotalCount>
  <PageSize>2</PageSize>
  <RequestId>0DFCADBA-7065-42DA-AF17-6868B9C2A8CF</RequestId>
  <CurrentPage>1</CurrentPage>
</DescribeGroupedVul>
```

`JSON` format

```json
    "GroupedVulItems": [
            "Tags": "",
            "LaterCount": 0,
            "AliasName": "RHSA-2019:0230-Important: polkit security update",
            "AsapCount": 0,
            "Type": "cve",
            "NntfCount": 59,
            "GmtLast": 1554185744000,
            "HandledCount": 0
```

`},`

```json
            "Tags": "",
            "LaterCount": 0,
            "AliasName": "RHSA-2019:0368-Important: systemd security update",
            "AsapCount": 0,
            "Type": "cve",
            "NntfCount": 59,
            "GmtLast": 1554185744000,
            "HandledCount": 0
```

`],`

```json
    "TotalCount": 432,
    "PageSize": 2,
    "RequestId": "0DFCADBA-7065-42DA-AF17-6868B9C2A8CF",
    "CurrentPage": 1
```

For a list of error codes, see Error codes.

#### 3.8.8 ModifyCreateVulWhitelist

Creates a vulnerability whitelist. Vulnerabilities added to the whitelist no longer trigger alerts.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyCreateVul Whitelist | The operation that you want to perform. Set the value to ModifyCreateVulWhitelist. |
| Reason | String | No | The vulnerability does not pose any threat. | The reason for adding the vulnerability to the whitelist. |

| Developer Guide·Thre | at Detection |   |   | Apsara Stack Securit |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Whitelist | String | No | [{"name":"oval:c om.redhat.rhsa:d ef:20173263","ty pe":"cve","aliasN ame":"RHSA- 2017:3263: curl security update"}] | The information about the vulnerability added to the whitelist, in the JSON format. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DFE4F166-1AC9- 4FAC-A4E4- F0608AD705A6 | The ID of the request. |

Sample requests

```
/?Action=ModifyCreateVulWhitelist &Reason=The vulnerability does not pose any threat. &Whitelist=[{"name":"oval:com.redhat.rhsa:def:20173263","type":"cve","aliasName":"RHSA-2017 :3263: curl security update"}]
```

Sample success responses `XML` format

```xml
<ModifyCreateVulWhitelist>
  <RequestId>DFE4F166-1AC9-4FAC-A4E4-F0608AD705A6</RequestId>
</ModifyCreateVulWhitelist>
```

`JSON` format

```json
 "RequestId":"DFE4F166-1AC9-4FAC-A4E4-F0608AD705A6"
```

For a list of error codes, see Error codes.

#### 3.8.9 ModifyEmgVulSubmit

Performs a scan task for emergency vulnerabilities.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyEmgVulSu bmit | The operation that you want to perform. Set the value to Modif yEmgVulSubmit . |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| Name | String | No | scan:ASCV-2019- 032401 | The name of the vulnerability. |
| UserAgreement | String | No | yes | Specifies whether you want to perform a scan task. Valid values: yes no |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 52A3AEE6-114A- 499D-8990- 4BA9B27FE0AA | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyEmgVulSubmit
```

Sample success responses `XML` format

```xml
<ModifyEmgVulSubmitResponse>
      <RequestId>52A3AEE6-114A-499D-8990-4BA9B27FE0AA</RequestId>
</ModifyEmgVulSubmitResponse>
```

`JSON` format

```json
    "RequestId": "52A3AEE6-114A-499D-8990-4BA9B27FE0AA"
```

For a list of error codes, see Error codes.

#### 3.8.10 DescribeAutoDelConfig

Queries the configurations for automatic vulnerability deletion.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAutoDelC onfig | The operation that you want to perform. Set the value to DescribeAut oDelConf ig. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 43186B14-5A39- 44E0-860E- 8B24D1EF82CC | The ID of the request. |
| Days | Integer | 7 | The number of days that a detected vulnerability is retained. |

Sample requests

```
/?Action=DescribeAutoDelConfig
```

Sample success responses `XML` format

```xml
<DescribeAutoDelConfig>
  <RequestId>43186B14-5A39-44E0-860E-8B24D1EF82CC</RequestId>
  <Days>7</Days>
</DescribeAutoDelConfig>
```

`JSON` format

```json
    "RequestId": "43186B14-5A39-44E0-860E-8B24D1EF82CC",
    "Days": 7
```

For a list of error codes, see Error codes.

#### 3.8.11 ModifyOperateVul

Performs operations on detected vulnerabilities, including verifying, ignoring, fixing.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyOperateVu l | The operation that you want to perform. Set the value to ModifyOperateVul. |
| Info | String | No | [{"name":"oval:c om.redhat.rhsa:d ef:20171100","uu id":"e49fb179- bbe7-4b6c-ab65- e106fb58d235","t ag":"oval"}] | The information required to manage vulnerabilities. It is a JSON string that consists of the UUID, name, and tag fields. |
| OperateType | String | No | vul ignore _ | The operation that you want to perform on the vulnerability. vul fix: fixes the vulnerability. _ vul verify: verifies the vulnerability. _ vul rebooted: verifies the _ vulnerability after the server is restarted. vul rollback: rolls back the _ vulnerability. vul ignore: ignores the vulnerability. _ vul undo ignore: cancels the ignore _ _ operation on the vulnerability. vul delete: deletes the vulnerability. _ |
| Reason | String | No | Postpone the fix | The reason why the vulnerability is ignored. |
| Type | String | No | cve | The type of the vulnerability. cve: Linux software vulnerabilities sys: Windows vulnerabilities cms: Web CMS vulnerabilities emg: emergency vulnerabilities |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DFE4F166-1AC9- 4FAC-A4E4- F0608AD705A6 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyOperateVul &Info=[{"name":"oval:com.redhat.rhsa:def:20171100","uuid":"e49fb179-bbe7-4b6c-ab65-e106fb58 d235","tag":"oval"}] &OperateType=vul_ignore &Type=cve &Reason=Postpone the fix
```

Sample success responses `XML` format

```xml
<ModifyOperateVul>
  <RequestId>DFE4F166-1AC9-4FAC-A4E4-F0608AD705A6</RequestId>
</ModifyOperateVul>
```

`JSON` format

```json
 "RequestId":"DFE4F166-1AC9-4FAC-A4E4-F0608AD705A6"
```

For a list of error codes, see Error codes.

### 3.9 Baseline check

#### 3.9.1 DescribeCheckWarningSummary

Queries the statistical information about baseline check results. The information includes the number of servers on which a baseline check is performed, the number of baseline check items, and the last check pass rate.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCheckWa rningSummary | The operation that you want to perform. Set the value to DescribeCheckWarningSummary. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| RiskName | String | No | Redis security baseline check | The name of the risk item. |
| RiskStatus | Integer | No | 1 | The status of the baseline check. Valid values: 1: failed 3: passed |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Status | String | No | 1 | The status of the check item. Valid values: 1: failed 2: verifying 3: passed 5: expired 6: ignored |
| StrategyId | Long | No | 1 | The ID of the baseline check policy. |
| TypeName | String | No | database | The level-1 type of check items. |
| Uuids | String | No | f03259d8-1e81- 4fae-bcbb- 275fb5****** | The ID of the server. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 10 | The number of check items returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 00BD7CE2-284A- 4534-BD09- FB69836DD750 | The ID of the request. |
| TotalCount | Integer | 100 | The total number of baseline check items. |
| WarningSumma rys | Array |   | The statistics of check items. |
| CheckCount | Integer | 10 | The number of check items. |
| HighWarningCo unt | Integer | 1 | The number of high-risk items. |
| LastFoundTime | String | 2019-01-01 12:23:00 | The time when the last baseline check was performed. |
| Level | String | high | The severity level of the risk item. Valid values: High Medium Low |
| LowWarningCo unt | Integer | 3 | The number of low-risk check items. |
| MediumWarnin gCount | Integer | 2 | The number of medium-risk check items. |
| RiskId | Long | 1 | The ID of the risk item. |
| RiskName | String | Redis password | The name of the risk item. |

|   |   |   | Developer Guide·Threat Detection |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| SubTypeAlias | String | Redis | The level-2 type of the risk item. |
| TypeAlias | String | Database | The type of the check item. Valid values: database, system, weak password, and middleware. |
| WarningMachin eCount | Integer | 11 | The number of assets on which risk items are detected. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCheckWarningSummary &Lang=zh &TypeName=database &Status=1 &RiskStatus=1 &RiskName=Redis security baseline check &StrategyId=1 &Uuids=f03259d8-1e81-4fae-bcbb-275fb55efb34 &CurrentPage=1 &PageSize=20
```

Sample success responses `XML` format

```xml
<DescribeCheckWarningSummary>
   <TotalCount>25</TotalCount>
   <PageSize>20</PageSize>
   <RequestId>DFA6CDC5-E826-4D18-A499-BEF9DA31F1AD</RequestId>
   <CurrentPage>1</CurrentPage>
   <Count>20</Count>
   <WarningSummarys>
      <RiskId>43</RiskId>
      <LastFoundTime>2019-04-10 00:33:00</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>3</WarningMachineCount>
      <CheckCount>16</CheckCount>
      <HighWarningCount>8</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>
   CentOS Linux 7 security baseline check
                              </SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>
```

```xml
   CentOS Linux 7 security baseline check
                              </RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>47</RiskId>
      <LastFoundTime>2019-04-10 00:58:11</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>2</WarningMachineCount>
      <CheckCount>15</CheckCount>
      <HighWarningCount>7</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>CentOS Linux 7 security standard compliance - MLPS level-3</SubTypeAlia
```

`s>`

```xml
      <LowWarningCount>0</LowWarningCount>
      <RiskName>CentOS Linux 7 security standard compliance - MLPS level-3</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>48</RiskId>
      <LastFoundTime>2019-04-10 00:58:11</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>2</WarningMachineCount>
      <CheckCount>12</CheckCount>
      <HighWarningCount>6</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>CentOS Linux 7 security standard compliance - MLPS level-2</SubTypeAlia
```

`s>`

```xml
      <LowWarningCount>0</LowWarningCount>
      <RiskName>CentOS Linux 7 security standard compliance - MLPS level-2</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>3</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>1</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>1</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Database</TypeAlias>
      <SubTypeAlias>Redis security baseline check</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Redis security baseline check</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>19</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>1</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>1</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Weak password</TypeAlias>
      <SubTypeAlias>Linux weak password</SubTypeAlias>
```

```xml
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Linux weak password</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>12</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>1</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>1</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Weak password</TypeAlias>
      <SubTypeAlias>Anonymous FTP logon</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Anonymous FTP logon</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>13</RiskId>
      <LastFoundTime>2019-04-10 06:58:58</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>1</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>1</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Weak password</TypeAlias>
      <SubTypeAlias>Windows weak password</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Windows weak password</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>23</RiskId>
      <LastFoundTime>2019-04-10 14:00:17</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>8</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>Middleware</TypeAlias>
      <SubTypeAlias>Apache Tomcat security baseline check</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Apache Tomcat security baseline check</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>2</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Weak password</TypeAlias>
      <SubTypeAlias>PostgreSQL weak password</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>PostgreSQL weak password</RiskName>
</WarningSmmars>
```

```xml
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>11</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Weak password</TypeAlias>
      <SubTypeAlias>MySQL weak password</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>MySQL weak password</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>20</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Weak password</TypeAlias>
      <SubTypeAlias>FTP weak password</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>FTP weak password</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>17</RiskId>
      <LastFoundTime>2019-04-10 06:58:58</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Weak password</TypeAlias>
      <SubTypeAlias>Microsoft SQL Server weak password</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Microsoft SQL Server weak password</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>24</RiskId>
      <LastFoundTime>2019-04-10 06:52:05</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>2</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>Database</TypeAlias>
      <SubTypeAlias>Memcached security baseline check</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Memcached security baseline check</RiskName>
   </WarningSummarys>
   <WarningSummarys>
<RiskId>42</RiskId>
```

```xml
      <RiskId>42</RiskId>
      <LastFoundTime>2019-02-19 14:59:17</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>16</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>CentOS Linux 6 security baseline check</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>CentOS Linux 6 security baseline check</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>49</RiskId>
      <LastFoundTime>2019-02-19 14:59:17</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>12</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>CentOS Linux 6 security standard compliance - MLPS level-2</SubTypeAlia
```

`s>`

```xml
      <LowWarningCount>0</LowWarningCount>
      <RiskName>CentOS Linux 6 security standard compliance - MLPS level-2</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>50</RiskId>
      <LastFoundTime>2019-02-19 14:59:17</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>15</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>CentOS Linux 6 security standard compliance - MLPS level-3</SubTypeAlia
```

`s>`

```xml
      <LowWarningCount>0</LowWarningCount>
      <RiskName>CentOS Linux 6 security standard compliance - MLPS level-3</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>55</RiskId>
      <LastFoundTime>2019-02-19 12:57:23</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>14</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>Linux Ubuntu security standard compliance - MLPS level-2</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Linux Ubuntu security standard compliance - MLPS level-2</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>56</RiskId>
```

```xml
      <LastFoundTime>2019-02-19 12:57:23</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>15</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>Linux Ubuntu security standard compliance - MLPS level-3</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Linux Ubuntu security standard compliance - MLPS level-3</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>54</RiskId>
      <LastFoundTime>2019-02-19 12:57:23</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>16</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>Linux Ubuntu security baseline check</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Linux Ubuntu security baseline check</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>51</RiskId>
      <LastFoundTime>2019-02-19 12:44:58</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>12</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>Windows 2012 R2 security baseline check</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Windows 2012 R2 security baseline check</RiskName>
   </WarningSummarys>
</DescribeCheckWarningSummary>
```

`JSON` format

```json
 "Count":20,
 "TotalCount":25,
 "WarningSummarys":[
   "SubTypeAlias":"CentOS Linux 7 security baseline check\n
\n ",
   "HighWarningCount":8,
   "WarningMachineCount":3,
   "RiskName":"CentOS Linux 7 security baseline check\n                                \n
```

`",`

```json
   "LowWarningCount":0,
"CheckCont"16
```

```json
   "CheckCount":16,
   "RiskId":43,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"System",
   "LastFoundTime":"2019-04-10 00:33:00"
```

`},`

```json
   "SubTypeAlias":"CentOS Linux 7 security standard compliance - MLPS level-3",
   "HighWarningCount":7,
   "WarningMachineCount":2,
   "RiskName":"CentOS Linux 7 security standard compliance - MLPS level-3",
   "LowWarningCount":0,
   "CheckCount":15,
   "RiskId":47,
   "Level":"medium",
   "MediumWarningCount":0,
   "TypeAlias":"System",
   "LastFoundTime":"2019-04-10 00:58:11"
```

`},`

```json
   "SubTypeAlias":"CentOS Linux 7 security standard compliance - MLPS level-2",
   "HighWarningCount":6,
   "WarningMachineCount":2,
   "RiskName":"CentOS Linux 7 security standard compliance - MLPS level-2",
   "LowWarningCount":0,
   "CheckCount":12,
   "RiskId":48,
   "Level":"medium",
   "MediumWarningCount":0,
   "TypeAlias":"System",
   "LastFoundTime":"2019-04-10 00:58:11"
```

`},`

```json
   "SubTypeAlias":"Redis security baseline check",
   "HighWarningCount":1,
   "WarningMachineCount":1,
   "RiskName":"Redis security baseline check",
   "LowWarningCount":0,
   "CheckCount":1,
   "RiskId":3,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"Database",
   "LastFoundTime":"2019-04-10 08:31:32"
```

`},`

```json
   "SubTypeAlias":"Linux weak password",
   "HighWarningCount":1,
   "WarningMachineCount":1,
   "RiskName":"Linux weak password",
   "LowWarningCount":0,
   "CheckCount":1,
   "RiskId":19,
"Level":"high",
```

```json
   Level:high,
   "MediumWarningCount":0,
   "TypeAlias":"Weak password",
   "LastFoundTime":"2019-04-10 08:31:32"
```

`},`

```json
   "SubTypeAlias":"Anonymous FTP logon",
   "HighWarningCount":1,
   "WarningMachineCount":1,
   "RiskName":"Anonymous FTP logon",
   "LowWarningCount":0,
   "CheckCount":1,
   "RiskId":12,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"Weak password",
   "LastFoundTime":"2019-04-10 08:31:32"
```

`},`

```json
   "SubTypeAlias":"Windows weak password",
   "HighWarningCount":1,
   "WarningMachineCount":1,
   "RiskName":"Windows weak password",
   "LowWarningCount":0,
   "CheckCount":1,
   "RiskId":13,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"Weak password",
   "LastFoundTime":"2019-04-10 06:58:58"
```

`},`

```json
   "SubTypeAlias":"Apache Tomcat security baseline check",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"Apache Tomcat security baseline check",
   "LowWarningCount":0,
   "CheckCount":8,
   "RiskId":23,
   "Level":"medium",
   "MediumWarningCount":0,
   "TypeAlias":"Middleware",
   "LastFoundTime":"2019-04-10 14:00:17"
```

`},`

```json
   "SubTypeAlias":"PostgreSQL weak password",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"PostgreSQL weak password",
   "LowWarningCount":0,
   "CheckCount":1,
   "RiskId":2,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"Weak password",
```

`yp` `p` `,`

```json
   "LastFoundTime":"2019-04-10 08:31:32"
```

`},`

```json
   "SubTypeAlias":"MySQL weak password",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"MySQL weak password",
   "LowWarningCount":0,
   "CheckCount":1,
   "RiskId":11,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"Weak password",
   "LastFoundTime":"2019-04-10 08:31:32"
```

`},`

```json
   "SubTypeAlias":"FTP weak password",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"FTP weak password",
   "LowWarningCount":0,
   "CheckCount":1,
   "RiskId":20,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"Weak password",
   "LastFoundTime":"2019-04-10 08:31:32"
```

`},`

```json
   "SubTypeAlias":"Microsoft SQL Server weak password",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"Microsoft SQL Server weak password",
   "LowWarningCount":0,
   "CheckCount":1,
   "RiskId":17,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"Weak password",
   "LastFoundTime":"2019-04-10 06:58:58"
```

`},`

```json
   "SubTypeAlias":"Memcached security baseline check",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"Memcached security baseline check",
   "LowWarningCount":0,
   "CheckCount":2,
   "RiskId":24,
   "Level":"medium",
   "MediumWarningCount":0,
   "TypeAlias":"Database",
   "LastFoundTime":"2019-04-10 06:52:05"
```

`},`

```json
   "SubTypeAlias":"CentOS Linux 6 security baseline check",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"CentOS Linux 6 security baseline check",
   "LowWarningCount":0,
   "CheckCount":16,
   "RiskId":42,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"System",
   "LastFoundTime":"2019-02-19 14:59:17"
```

`},`

```json
   "SubTypeAlias":"CentOS Linux 6 security standard compliance - MLPS level-2",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"CentOS Linux 6 security standard compliance - MLPS level-2",
   "LowWarningCount":0,
   "CheckCount":12,
   "RiskId":49,
   "Level":"medium",
   "MediumWarningCount":0,
   "TypeAlias":"System",
   "LastFoundTime":"2019-02-19 14:59:17"
```

`},`

```json
   "SubTypeAlias":"CentOS Linux 6 security standard compliance - MLPS level-3",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"CentOS Linux 6 security standard compliance - MLPS level-3",
   "LowWarningCount":0,
   "CheckCount":15,
   "RiskId":50,
   "Level":"medium",
   "MediumWarningCount":0,
   "TypeAlias":"System",
   "LastFoundTime":"2019-02-19 14:59:17"
```

`},`

```json
   "SubTypeAlias":"Linux Ubuntu security standard compliance - MLPS level-2",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"Linux Ubuntu security standard compliance - MLPS level-2",
   "LowWarningCount":0,
   "CheckCount":14,
   "RiskId":55,
   "Level":"medium",
   "MediumWarningCount":0,
   "TypeAlias":"System",
   "LastFoundTime":"2019-02-19 12:57:23"
```

`},`

```json
   "SubTypeAlias":"Linux Ubuntu security standard compliance - MLPS level-3",
```

```json
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"Linux Ubuntu security standard compliance - MLPS level-3",
   "LowWarningCount":0,
   "CheckCount":15,
   "RiskId":56,
   "Level":"medium",
   "MediumWarningCount":0,
   "TypeAlias":"System",
   "LastFoundTime":"2019-02-19 12:57:23"
```

`},`

```json
   "SubTypeAlias":"Linux Ubuntu security baseline check",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"Linux Ubuntu security baseline check",
   "LowWarningCount":0,
   "CheckCount":16,
   "RiskId":54,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"System",
   "LastFoundTime":"2019-02-19 12:57:23"
```

`},`

```json
   "SubTypeAlias":"Windows 2012 R2 security baseline check",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"Windows 2012 R2 security baseline check",
   "LowWarningCount":0,
   "CheckCount":12,
   "RiskId":51,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"System",
   "LastFoundTime":"2019-02-19 12:44:58"
```

`],`

```json
 "PageSize":20,
 "RequestId":"DFA6CDC5-E826-4D18-A499-BEF9DA31F1AD",
 "CurrentPage":1
```

For a list of error codes, see Error codes.

#### 3.9.2 DescribeStratety

Queries the configurations of baseline check policies.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeStratety | The operation that you want to perform. Set the value to DescribeStratety. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| StrategyIds | String | No | test1,test2,test3 | The IDs of the baseline check policies. Separate multiple IDs with commas (,). |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 16B9826C-B99F- 4F8A-8048- EA81D6D3DE8B | The ID of the request. |
| Strategies | Array |   | The information about the baseline check policy. |
| ConfigTargets | Array |   | The information about the group associated with the baseline check policy. |
| Flag | String | add | The related ID. |
| Target | String | 3259405 | The ID of the related group. |
| TargetType | String | groupId | The type of the related group. |
| CycleDays | Integer | 1 | The cycle of the baseline check. 1: every second day 3: every fourth day 7: every eighth day 30: every 31st day |

| Parameter | Type | Example | Description |
|---|---|---|---|
| CycleStartTime | Integer | 6 | The time when the baseline check starts. Valid values: 0, 6, 12, and 18. |
| EcsCount | Integer | 5 | The number of servers on which baseline checks were performed based on the specified baseline check policy. |
| ExecStatus | Integer | 1 | The execution status of the baseline check. Valid values: 1: The baseline check is not running. 2: The baseline check is running. |
| Id | Integer | 212635 | The ID of the policy. |
| Name | String | test | The name of the policy. |
| PassRate | Integer | 80 | The pass rate of the latest baseline check. |
| ProcessRate | Integer | 80 | The progress of the baseline check. |
| RiskCount | Integer | 5 | The number of selected check items. |
| Type | Integer | 1 | The type of the baseline check policy. Valid values: 1: default policy 2: custom policy |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeStratety ? Lang=zh &SourceIp=127.0.0.1 &StrategyIds=1,2,3
```

Sample success responses `XML` format

```xml
<DescribeStratety>
   <RequestId>ACAFE09B-3346-433B-BDA8-369AB3D9B4F9</RequestId>
   <Strategies>
      <CycleStartTime>6</CycleStartTime>
      <EcsCount>0</EcsCount>
      <Type>2</Type>
      <ExecStatus>1</ExecStatus>
      <ProcessRate>0</ProcessRate>
      <CycleDays>3</CycleDays>
      <Id>15161</Id>
      <ConfigTargets>
         <Target>4361221</Target>
         <TargetType>groupId</TargetType>
         <Flag>add</Flag>
      </ConfigTargets>
      <RiskCount>1</RiskCount>
      <Name>test</Name>
   </Strategies>
   <Strategies>
      <CycleStartTime>0</CycleStartTime>
      <EcsCount>17</EcsCount>
      <PassRate>81</PassRate>
      <Type>1</Type>
      <ExecStatus>1</ExecStatus>
      <ProcessRate>0</ProcessRate>
      <CycleDays>1</CycleDays>
      <Id>20</Id>
      <ConfigTargets>
         <Target>281801</Target>
         <TargetType>groupId</TargetType>
         <Flag>del</Flag>
      </ConfigTargets>
      <ConfigTargets>
         <Target>4790960</Target>
         <TargetType>groupId</TargetType>
         <Flag>del</Flag>
      </ConfigTargets>
      <RiskCount>13</RiskCount>
      <Name>Default policy</Name>
   </Strategies>
</DescribeStratety>
```

`JSON` format

```json
 "RequestId":"ACAFE09B-3346-433B-BDA8-369AB3D9B4F9",
 "Strategies":[
   "Name":"test",
   "RiskCount":1,
   "CycleDays":3,
   "Type":2,
   "CycleStartTime":6,
   "ConfigTargets":[
     "Flag":"add",
     "Target":"4361221",
     "TargetType":"groupId"
```

`],`

```json
   "ProcessRate":0,
   "Id":15161,
   "ExecStatus":1,
   "EcsCount":0
```

`},`

```json
   "Name":"Default policy",
   "RiskCount":13,
   "PassRate":81,
   "CycleDays":1,
   "Type":1,
   "CycleStartTime":0,
   "ConfigTargets":[
     "Flag":"del",
     "Target":"281801",
     "TargetType":"groupId"
```

`},`

```json
     "Flag":"del",
     "Target":"4790960",
     "TargetType":"groupId"
```

`],`

```json
   "ProcessRate":0,
   "Id":20,
   "ExecStatus":1,
   "EcsCount":17
```

`]` For a list of error codes, see Error codes.

#### 3.9.3 DescribeStrategyExecDetail

Queries the details of the latest baseline check by using a baseline check policy. The details include the time when the check is performed, the number of risk items, and the baseline risk details.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeStrategy ExecDetail | The operation that you want to perform. Set the value to DescribeStrategyExecDetail. |
| StrategyId | Integer | Yes | 1 | The ID of the baseline check policy. Not e To query the results of a baseline check that uses only one policy, you must specify the ID of the policy. You can call the DescribeStratety operation to obtain the ID. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| EndTime | String | 2019-01-08 20:11:20 | The time when the baseline check ends. |
| FailCount | Integer | 94 | The number of risk items that failed to pass the baseline check. |
| FailedEcsList | Array |   | The list of servers on which risk items were detected. |
| IP | String | 1.2.3.4 | The IP address of the instance on which the baseline check was performed. |
| InstanceName | String | Test-20180703 | The name of the instance. |
| IntranetIp | String | 1.2.3.5 | The internal IP address. |

| psara Stack Securi | ty |   | Developer Guide·Threat Detection Service (TDS |
|---|---|---|---|
| Parameter | Type | Example | Description |

| Reason | String | Detect timeout | The cause of the baseline check failure. |
|---|---|---|---|
| InProcessCount | Integer | 0 | The number of baseline check tasks that are running. |
| Percent | String | 100% | The progress of the baseline check. |
| RequestId | String | 09322632-4668- 4AD9-BD0D- 32757DEFBBA6 | The ID of the request. |
| Source | String | Manual | The type of the baseline check. Schedule Manual |
| StartTime | String | 2019-01-08 19:41:12 | The time when the baseline check starts. |
| SuccessCount | Integer | 81 | The number of check items that passed the baseline check. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeStrategyExecDetail &StrategyId=1
```

Sample success responses `XML` format

```xml
<DescribeStrategyExecDetail>
   <RequestId>6489FA6A-D241-4380-9D8C-A8804484CA40</RequestId>
   <EndTime>2019-04-10 00:58:30</EndTime>
   <Percent>100%</Percent>
   <FailCount>1</FailCount>
   <StartTime>2019-04-10 00:19:01</StartTime>
   <SuccessCount>1</SuccessCount>
   <Source>Schedule</Source>
   <FailedEcsList>
      <InstanceName>health-check002</InstanceName>
      <IP>1.2.3.4</IP>
      <IntranetIp>1.2.3.5</IntranetIp>
      <Reason>Agent offline</Reason>
   </FailedEcsList>
   <InProcessCount>0</InProcessCount>
</DescribeStrategyExecDetail>
```

`JSON` format

```json
 "Source":"Schedule",
 "InProcessCount":0,
 "SuccessCount":1,
 "RequestId":"6489FA6A-D241-4380-9D8C-A8804484CA40",
 "Percent":"100%",
 "FailedEcsList":[
   "IntranetIp":"1.2.3.5",
   "IP":"1.2.3.4",
   "InstanceName":"health-check002",
   "Reason":"Agent offline"
```

`],`

```json
 "EndTime":"2019-04-10 00:58:30",
 "StartTime":"2019-04-10 00:19:01",
 "FailCount":1
```

For a list of error codes, see Error codes.

#### 3.9.4 DescribeCheckWarnings

Queries specified risk items and check items of a specified server.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCheckWa rnings | The operation that you want to perform. Set the value to DescribeCheckWarnings. |
| RiskId | Long | Yes | 1 | The ID of the risk item. Not e To query specified risk items and check items of a specified server, you must specify the IDs of the risk items. You can call the DescribeCheckWarningSummary operation to obtain the IDs. |
| Uuid | String | Yes | d42f938c-d962- 48a0-90f9- 05********** | The ID of the server on which a baseline check is performed. The ID of the risk item. Not e To query specified risk items and check items of a specified server, you must specify the ID of the server on which the baseline check is run. You can call the DescribeWarningMachines operation to obtain the IDs. |
| CurrentPage | Integer | No | 1 | The number of the current page. Pages start from page 1. The default value is 1, which indicates that the first page is displayed. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| PageSize | Integer | No | 20 | The number of entries to return on each page. The default value is 20, which indicates that 20 entries are returned on each page. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| CheckWarnings | Array |   | The information about the check item. |
| CheckId | Long | 1 | The ID of the check item. |
| CheckWarningId | Long | 10 | The ID of the alert. |
| Item | String | Password expiration alert | The name of the check item. |
| Level | String | high | The severity level of the risk item. Valid values: high medium low |
| Status | Integer | 1 | The status of the check item. Valid values: 1: failed 2: verifying 3: passed 5: expired 6: ignored |
| Type | String | Identity authentication | The type of the check item. |
| Uuid | String | d42f938c-d962- 48a0-90f9- *********** | The ID of the server on which the baseline check was performed. |
| Count | Integer | 10 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| PageSize | Integer | 20 | The number of entries returned per page. |

| psara Stack Securi | ty |   | Developer Guide·Threat Detection Service (TDS |
|---|---|---|---|
| Parameter | Type | Example | Description |

| RequestId | String | 0DFCADBA-7065- 42DA-AF17- 6868B9C2A8CF | The ID of the request. |
|---|---|---|---|
| TotalCount | Integer | 100 | The total number of entries. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCheckWarnings &RiskId=1 &Uuid=d42f938c-d962-48a0-90f9-05e4eaf92e34 &Lang=zh &SourceIp=127.0.0.1 &CurrentPage=1 &PageSize=20
```

Sample success responses `XML` format

```xml
<DescribeCheckWarnings>
  <TotalCount>16</TotalCount>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Check accounts without passwords in the system
                            </Item>
        <Type>Identity authentication</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>1</CheckId>
        <CheckWarningId>1393768</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Check password complexity</Item>
        <Type>Identity authentication</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>52</CheckId>
        <CheckWarningId>1393774</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Make sure that root is the only account whose UID is 0</Item>
        <Type>Identity authentication</Type>
```

```xml
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>15</CheckId>
        <CheckWarningId>1393773</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Enable address space layout randomization</Item>
        <Type>Intrusion prevention</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>14</CheckId>
        <CheckWarningId>1393772</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Specify user permissions on file configurations</Item>
        <Type>File permissions</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>13</CheckId>
        <CheckWarningId>1393767</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Specify permissions on the access control configuration file</Item>
        <Type>File permissions</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>12</CheckId>
        <CheckWarningId>1393771</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Make sure that SSH LogLevel is set to INFO</Item>
        <Type>Service configuration</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>11</CheckId>
        <CheckWarningId>1393766</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Make sure that the rsyslog service is enabled</Item>
        <Type>Security auditing</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>10</CheckId>
        <CheckWarningId>1393770</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Specify the timeout period for SSH idle connections</Item>
        <Type>Service configuration</Type>
```

```xml
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>8</CheckId>
        <CheckWarningId>1393765</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Make sure that SSH V2 is used</Item>
        <Type>Service configuration</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>7</CheckId>
        <CheckWarningId>1393764</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Make sure that SSH MaxAuthTries is set to a value from 3 to 6</Item>
        <Type>Service configuration</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>6</CheckId>
        <CheckWarningId>1393763</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Make sure that alerts are triggered at least seven days before passwords expi
re</Item>
        <Type>Identity authentication</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>5</CheckId>
        <CheckWarningId>1393769</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Set the shortest interval between password changes</Item>
        <Type>Identity authentication</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>4</CheckId>
        <CheckWarningId>1393761</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Set the password validity period</Item>
        <Type>Identity authentication</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>3</CheckId>
        <CheckWarningId>1393760</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Disable SSH logon for accounts without specified passwords
```

```xml
                            </Item>
        <Type>Service configuration</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>2</CheckId>
        <CheckWarningId>1393762</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Check whether password reuse is limited</Item>
        <Type>Identity authentication</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>58</CheckId>
        <CheckWarningId>1393775</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <PageSize>20</PageSize>
  <RequestId>C1E6C4FE-DE00-4B75-A01E-FCAB55A36449</RequestId>
  <CurrentPage>1</CurrentPage>
  <Count>16</Count>
</DescribeCheckWarnings>
```

`JSON` format

```json
 "Count":16,
 "TotalCount":16,
 "PageSize":20,
 "RequestId":"C1E6C4FE-DE00-4B75-A01E-FCAB55A36449",
 "CurrentPage":1,
 "CheckWarnings":[
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393768,
   "Item":"Check accounts without passwords in the system\r\n
\r\n ",
   "Type":"Identity authentication",
   "Level":"high",
   "CheckId":1
```

`},`

```json
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393774,
   "Item":"Check password complexity",
   "Type":"Identity authentication",
   "Level":"high",
   "CheckId":52
```

`},`

```json
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
```

```json
   "CheckWarningId":1393773,
   "Item":"Make sure that root is the only account whose UID is 0",
   "Type":"Identity authentication",
   "Level":"high",
   "CheckId":15
```

`},`

```json
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393772,
   "Item":"Enable address space layout randomization",
   "Type":"Intrusion prevention",
   "Level":"high",
   "CheckId":14
```

`},`

```json
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393767,
   "Item":"Specify user permissions on file configurations",
   "Type":"File permissions",
   "Level":"high",
   "CheckId":13
```

`},`

```json
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393771,
   "Item":"Specify the permissions on the access control configuration file",
   "Type":"File permissions",
   "Level":"high",
   "CheckId":12
```

`},`

```json
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393766,
   "Item":"Make sure that SSH LogLevel is set to INFO",
   "Type":"Service configuration",
   "Level":"high",
   "CheckId":11
```

`},`

```json
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393770,
   "Item":"Make sure that the rsyslog service is enabled",
   "Type":"Security auditing",
   "Level":"high",
   "CheckId":10
```

`},`

```json
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
```

```json
   "CheckWarningId":1393765,
   "Item":"Specify the timeout period for SSH idle connections",
   "Type":"Service configuration",
   "Level":"high",
   "CheckId":8
```

`},`

```json
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393764,
   "Item":"Make sure that SSH V2 is used",
   "Type":"Service configuration",
   "Level":"high",
   "CheckId":7
```

`},`

```json
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393763,
   "Item":"Make sure that SSH MaxAuthTries is set to a value from 3 to 6",
   "Type":"Service configuration",
   "Level":"high",
   "CheckId":6
```

`},`

```json
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393769,
   "Item":"Make sure that alerts are triggered at least seven days before passwords expire"
```

`,`

```json
   "Type":"Identity authentication",
   "Level":"high",
   "CheckId":5
```

`},`

```json
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393761,
   "Item":"Set the shortest interval between password changes",
   "Type":"Identity authentication",
   "Level":"high",
   "CheckId":4
```

`},`

```json
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393760,
   "Item":"Set the password validity period",
   "Type":"Identity authentication",
   "Level":"high",
   "CheckId":3
```

`},`

```json
   "Uuid":"974af549-3248-44dd-9180-***",
"Stt
```

`"``6`

```json
   "Status":6,
   "CheckWarningId":1393762,
   "Item":"Disable SSH logon for accounts without specified passwords
\r\n \r\n \r\n
```

`",`

```json
   "Type":"Service configuration",
   "Level":"high",
   "CheckId":2
```

`},`

```json
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393775,
   "Item":"Check whether password reuse is limited",
   "Type":"Identity authentication",
   "Level":"high",
   "CheckId":58
```

`]` For a list of error codes, see Error codes.

#### 3.9.5 DescribeCheckWarningDetail

Queries the details of a specific check item.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCheckWa rningDetail | The operation that you want to perform. Set the value to DescribeCheckWarningDetail. |
| CheckWarningId | Long | Yes | 1 | The ID of the alert triggered by the check item. Not e To query the details of a specific check item, you must specify the ID of the alert triggered by the check item. You can call the DescribeCheckWarnings operation to obtain the alert ID. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Advice | String | Fix now | The suggestion for the management of the risk item. |
| CheckId | Long | 1 | The ID of the check item. |
| Description | String | Password expiring | The additional details about the risk item. |
| Item | String | Password expiration alert | The name of the check item. |
| Level | String | high | The severity level of the risk item. high: The item is a high-risk one and highlighted in red. medium: The item is a medium-risk one and highlighted in orange. low: The item is a low-risk one and highlighted in gray. |
| Prompt | String | Password expiration alert | The prompt for the risk item. |
| RequestId | String | 09969D2C-4FAD- 429E-BFBF- 9A60DEF8BF6F | The ID of the request. |
| Type | String | Identity authentication | The type of the check item. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCheckWarningDetail &CheckWarningId=1 &SourceIp=127.0.0.1 &Lang=zh
```

Sample success responses `XML` format

```xml
<DescribeCheckWarningDetail>
   <Item>Specify user permissions on file configurations</Item>
   <Type>File permissions</Type>
   <Description>Specify user permissions on file configurations</Description>
   <RequestId>9F2361B3-B7C3-4189-8DB5-C6D1F67BC225</RequestId>
   <CheckId>13</CheckId>
   <Prompt></Prompt>
   <Level>high</Level>
   <Advice>Run the following five commands
  chown root:root /etc/passwd /etc/shadow /etc/group /etc/gshadow
  chmod 0644 /etc/group
  chmod 0644 /etc/passwd
  chmod 0400 /etc/shadow
 chmod 0400 /etc/gshadow  </Advice>
</DescribeCheckWarningDetail>
```

`JSON` format

```json
 "Prompt":"",
 "Description":"Specify user permissions on file configurations",
 "Item":"Specify user permissions on file configurations",
 "Type":"File permissions",
 "RequestId":"9F2361B3-B7C3-4189-8DB5-C6D1F67BC225",
 "Advice":"Run the following five commands\r\nchown root:root /etc/passwd /etc/shadow /etc/
group /etc/gshadow\r\nchmod 0644 /etc/group \r\nchmod 0644 /etc/passwd \r\nchmod 0400 /et c/shadow \r\nchmod 0400 /etc/gshadow ",
 "Level":"high",
 "CheckId":13
```

For a list of error codes, see Error codes.

#### 3.9.6 DescribeWarningMachines

Queries information about servers on which a baseline check is performed. The information includes the statistics and status of risk items and IDs of the servers.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeWarning Machines | The operation that you want to perform. Set the value to DescribeWarningMachines. |
| RiskId | Long | Yes | 1 | The ID of the risk item. Not e To query information about servers on which a baseline check is performed, you must specify the ID of the risk item that is related to the baseline check. You can call the DescribeCheckWarningSummary operation to obtain the ID. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| MachineName | String | No | test ecs172 _ | The name of the server on which a baseline check is performed. |
| Uuids | String | No | xxx-aaa-bbb-ccc | The ID of the server on which a baseline check is performed. Separate multiple IDs with commas (,). |
| StrategyId | Long | No | 1 | The ID of the baseline check policy. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| CurrentPage | Integer | No | 1 | The number of the current page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 10 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The number of the current page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 00BDE2-284A-4534- BD09-FB69836DD750 | The ID of the request. |
| TotalCount | Integer | 100 | The total number of returned entries. |
| WarningMachin es | Array |   | The information about the servers that generate alerts. |
| HighWarningCo unt | Integer | 10 | The number of high-risk check items. |
| InstanceId | String | i- m5ee8b9nr3h30mhb **** | The instance ID of the server. |
| InstanceName | String | aaawebtest | The name of the instance. |
| InternetIp | String | 1.2.3.4 | The public IP address of the server. |
| IntranetIp | String | 1.2.3.5 | The private IP address of the server. |
| LowWarningCo unt | Integer | 3 | The number of low-risk check items. |
| MediumWarnin gCount | Integer | 2 | The number of medium-risk check items. |
| PassCount | Integer | 10 | The number of items that have passed the baseline check. |
| RegionId | String | cn-qingdao | The region ID of the server. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | Integer | 1 | The verification status of the risk items that are fixed. Valid values: 1: completed 2: verifying |
| Uuid | String | xxx-aaa-bbb-ccc | The ID of the server on which a baseline check is performed. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeWarningMachines &RiskId=1
```

Sample success responses `XML` format

```xml
<DescribeWarningMachinesResponse>
      <TotalCount>100</TotalCount>
      <RequestId>00BDE2-284A-4534-BD09-FB69836DD750</RequestId>
      <PageSize>10</PageSize>
      <CurrentPage>1</CurrentPage>
      <WarningMachines>
            <InstanceName>aaawebtest</InstanceName>
            <Status>1</Status>
            <MediumWarningCount>2</MediumWarningCount>
            <Uuid>xxx-aaa-bbb-ccc</Uuid>
            <InternetIp>1.2.3.4</InternetIp>
            <InstanceId>i-m5ee8b9nr3h30mhb****</InstanceId>
            <HighWarningCount>10</HighWarningCount>
            <RegionId>cn-qingdao</RegionId>
            <PassCount>10</PassCount>
            <IntranetIp>1.2.3.5</IntranetIp>
            <LowWarningCount>3</LowWarningCount>
      </WarningMachines>
      <Count>10</Count>
</DescribeWarningMachinesResponse>
```

`JSON` format

```json
    "TotalCount": "100",
    "RequestId": "00BDE2-284A-4534-BD09-FB69836DD750",
    "PageSize": "10",
    "CurrentPage": "1",
    "WarningMachines": [{
        "InstanceName": "aaawebtest",
        "Status": "1",
        "MediumWarningCount": "2",
        "Uuid": "xxx-aaa-bbb-ccc",
        "InternetIp": "1.2.3.4",
        "InstanceId": "i-m5ee8b9nr3h30mhb****",
        "HighWarningCount": "10",
        "RegionId": "cn-qingdao",
        "PassCount": "10",
        "IntranetIp": "1.2.3.5",
        "LowWarningCount": "3"
    }],
    "Count": "10"
```

For a list of error codes, see Error codes.

#### 3.9.7 DescribeUserBaselineAuthorization

Queries whether Threat Detection Service has the permissions to access a cloud resource.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeUserBase lineAuthorization | The operation that you want to perform. Set the value to DescribeUserBaselineAuthorization. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0AF20EB0-EBBC- 4B94-9B84- F3BAFAC53EDE | The ID of the request. |
| UserBaselineAu thorization | Struct |   | The information about whether Threat Detection Service has the permissions to run configuration checks on a cloud resource. |
| Status | Integer | 1 | Indicates whether Threat Detection Service is authorized to run configuration checks on a cloud resource. 0: permission denied. Threat Detection Service does not have the permissions to run configuration checks on the cloud platform. 1: permission granted. Threat Detection Service has the permissions to run configuration checks on the cloud platform. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeUserBaselineAuthorization
```

Sample success responses `XML` format

```xml
<data>
    <UserBaselineAuthorization>
        <Status>1</Status>
    </UserBaselineAuthorization>
</data> <requestId>0AF20EB0-EBBC-4B94-9B84-F3BAFAC53EDE</requestId>
```

`JSON` format

```json
  "data": {
    "UserBaselineAuthorization": {
      "Status": 1
```

`},`

```json
  "requestId": "0AF20EB0-EBBC-4B94-9B84-F3BAFAC53EDE"
```

For a list of error codes, see Error codes.

#### 3.9.8 ValidateHcWarnings

Verifies multiple risk items of the baseline check at a time. The verification operation verifies whether risk items of the baseline check have been fixed. If a risk item is verified, the risk item status is updated to Passed.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ValidateHcWarnin gs | The operation that you want to perform. Set the value to Validat eHcWarnings. |
| RiskIds | String | Yes | 43 | The ID list of risk items that need to be verified. If the list has multiple risk item IDs, separate them with commas (,). |
| Uuids | String | Yes | 78645c8e-2e89- 441b- 8eb,a9622a6b- adb5-4dd3- 929e,0136460a- 1cb5-44e8-**** | The UUID list of servers that contain risk items to be verified. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 722C4F88-7867- 4E7B-8ADE-7451053 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=ValidateHcWarnings &RiskIds=43 &Uuids=78645c8e-2e89-441b-8eb,a9622a6b-adb5-4dd3-929e,0136460a-1cb5-44e8-****
```

Sample success responses `XML` format

```xml
<ValidateHcWarningsResponse>
  <RequestId>722C4F88-7867-4E7B-8ADE-7451053</RequestId>
</ValidateHcWarningsResponse>
```

`JSON` format

```json
   "RequestId":"722C4F88-7867-4E7B-8ADE-7451053"
```

For a list of error codes, see Error codes.

#### 3.9.9 FixCheckWarnings

Fixes risk items detected in the baseline check.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | FixCheckWarnings | The operation that you want to perform. Set the value to FixCheckWarnings. |
| CheckParams | String | Yes | [{"checkId":8,"rule s": [{"ruleId":"rule.ss h Idle.interval","v _ alue":1,"paramLis t": [{"paramName":" range val","value _ ":"600"}, {"paramName":"r ange val","value" _ :"600"}]}, {"ruleId":"rule.ssh Idle.count","valu _ e":1,"paramList": [{"paramName":" range val","value _ ":"3"}]}]}] | The parameters for the risk item to be fixed. Descriptions of the parameters: checkId: the ID of the check item. rules: the rules applied to fixes, in the array format. value: specifies whether the fix method is selected. Valid values:0: not selected.1: selected. ruleId: specifies the ID of the fix method. paramList : the list of fix methods, in the array format. paramName: the name of the fix method. value: the value of the fix method. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RiskId | Long | Yes | 12 | The ID of the risk item to be fixed. |
| Uuids | String | Yes | uuid-abcd- 1234,uuid-abcd- 2345 | The UUID list of the servers that have risk items. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Example | Description |
|---|---|---|---|
| BatchId | Long | 52370 | The IDs of the returned risk items that have been fixed. |
| RequestId | String | 76C1D7FD-DB1E- 45EA-B804- 3FBD9A1DD9C0 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=FixCheckWarnings &CheckParams=[{"checkId":8,"rules":[{"ruleId":"rule.ssh_Idle.interval","value":1,"paramList ":[{"paramName":"range_val","value":"600"},{"paramName":"range_val","value":"600"}]},{"rule Id":"rule.ssh_Idle.count","value":1,"paramList":[{"paramName":"range_val","value":"3"}]}]}] &RiskId=12 &Uuids=uuid-abcd-1234,uuid-abcd-2345
```

Sample success responses `XML` format

```xml
<FixCheckWarningsResponse>
      <BatchId>52370</BatchId>
      <requestId>76C1D7FD-DB1E-45EA-B804-3FBD9A1DD9C0</requestId>
</FixCheckWarningsResponse>
```

`JSON` format

```json
    "BatchId": 52370,
    "requestId": "76C1D7FD-DB1E-45EA-B804-3FBD9A1DD9C0"
```

For a list of error codes, see Error codes.

### 3.10 Asset fingerprints

#### 3.10.1 DescribePropertyCount

Queries the statistics of asset fingerprints, including the numbers of processes, ports, software, users, and scheduled tasks.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeProperty Count | The operation that you want to perform. Set the value to DescribePropertyCount. |
| Type | String | No | port | The type of the asset fingerprint. Valid values: user sof t ware process port cron: scheduled tasks Not e If you do not specify a type, all types of asset fingerprints are queried. |
| UuidList | String | No | [c4678332- ef3**,c46***] | The IDs of the assets, which are unique. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Cron | Integer | 261 | The number of scheduled tasks. |

| psara Stack Securi | ty |   | Developer Guide·Threat Detection Service (TDS |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Port | Integer | 163 | The number of listening ports. |
| Process | Integer | 367 | The number of running processes. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | The ID of the request. |
| Software | Integer | 5073 | The number of software assets. |
| User | Integer | 114 | The number of users. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertyCount
```

Sample success responses `XML` format

```xml
<DescribePropertyCount>
  <User>340</User>
  <Software>2598</Software>
  <Port>265</Port>
  <Process>395</Process>
  <RequestId>3D93ABAB-0AC2-4A27-A03B-35C0E4AA0443</RequestId>
  <Cron>261</Cron>
</DescribePropertyCount>
```

`JSON` format

```json
 "User":340,
 "Software":2598,
 "Port":265,
 "RequestId":"3D93ABAB-0AC2-4A27-A03B-35C0E4AA0443",
 "Process":395,
 "Cron":261
```

For a list of error codes, see Error codes.

#### 3.10.2 DescribePropertyPortDetail

Queries the details of a port.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeProperty PortDetail | The operation that you want to perform. Set the value to DescribePropert yPort Det ail. |
| Remark | String | No | 1.2.3.4 | The name or IP address of the server. |
| Port | String | No | 22 | The port of the server. |
| ProcName | String | No | sshd | The name of the process. |
| Uuid | String | No | 50d213b4-3a35- 427a-b8a5-*** | The ID of the asset, which is unique. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| PageSize | Integer | No | 6 | The number of entries to return on each page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | FAA793EF-5B14- 4CDD-B3E0- B14D4342C422 | The ID of the request. |
| Propertys | Array |   | Details of the port. |
| BindIp | String | 1.2.3.4 | The IP addresses bound to the port. |
| Port | String | 22 | The port number. |
| InstanceName | String | test-*** | The name of the asset related to the port. |

| psara Stack Securi | ty |   | Developer Guide·Threat Detection Service (TDS |
|---|---|---|---|
| Parameter | Type | Example | Description |
| Proto | String | tcp | The network protocol. |
| Ip | String | 1.2.3.1 | The public IP address of the asset. |
| Create | String | 2019-05-13T10:39Z | The time when the data is last collected. |
| CreateTimesta mp | Long | 1557715141000 | The timestamp of last data collection. |
| ProcName | String | sshd | The name of the process that is using the port. |
| Uuid | String | 50d213b4-3a35- 427a-b8a5- 04b0c7e1f4d2" | The ID of the asset related to the port. |
| InstanceId | String | 50d213b4-3a35- 427a-b8a5- 04b0c7e1f4d2" | The ID of the asset related to the port. |
| IntranetIp | String | 1.2.3.2 | The private IP address of the asset. |
| InternetIp | String | 1.2.3.1 | The public IP address of the asset. |
| PageInfo | Struct |   | The page information. |
| Count | Integer | 5 | The number of entries returned on the current page. |
| PageSize | Integer | 5 | The number of entries returned per page. |
| TotalCount | Integer | 762 | The total number of returned entries. |
| CurrentPage | Integer | 1 | The page number of the current page. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertyPortDetail
```

Sample success responses `XML` format

```xml
<DescribePropertyPortDetailResponse>
  <Propertys>
        <InstanceName>centos-xx</InstanceName>
        <Uuid>00274759-73ef-485a-ae40-c2b5972f50cd</Uuid>
        <Proto>tcp</Proto>
        <InternetIp>101.xx.xx.104</InternetIp>
        <InstanceId>i-2ze645t5u9jo4txxx</InstanceId>
        <Create>2020-01-09T13:53Z</Create>
        <Port>22</Port>
        <Ip>101.xx.xx.104</Ip>
        <ProcName>sshd</ProcName>
        <CreateTimestamp>1578549227000</CreateTimestamp>
        <IntranetIp>192.xx.xx.96</IntranetIp>
        <BindIp>0.0.0.0</BindIp>
  </Propertys>
  <Propertys>
        <InstanceName>paas-xxx-test1122</InstanceName>
        <Uuid>007ecd45-e90f-4290-9eac-758407aa1509</Uuid>
        <Proto>tcp</Proto>
        <InternetIp>118.xx.xx.7</InternetIp>
        <InstanceId>i-m5e56ycm6xx7if43xx</InstanceId>
        <Create>2020-02-18T15:52Z</Create>
        <Port>10251</Port>
        <Ip>118.xx.xx.7</Ip>
        <ProcName>kube-scheduler</ProcName>
        <CreateTimestamp>1582012349000</CreateTimestamp>
        <IntranetIp>192.xx.xx.192</IntranetIp>
        <BindIp>::</BindIp>
  </Propertys>
  <Propertys>
        <InstanceName>paas-xx-2</InstanceName>
        <Uuid>007ecd45-e9xx-4290-9eac-758407aa15xx</Uuid>
        <Proto>tcp</Proto>
        <InternetIp>118.xx.xx.7</InternetIp>
        <InstanceId>i-m5e56ycm6s0xxf43maxx</InstanceId>
        <Create>2020-02-18T15:52Z</Create>
        <Port>10252</Port>
        <Ip>118.xx.xx.7</Ip>
        <ProcName>kube-controller-manager</ProcName>
        <CreateTimestamp>1582012349000</CreateTimestamp>
        <IntranetIp>192.xx.xx.192</IntranetIp>
        <BindIp>::</BindIp>
  </Propertys>
  <Propertys>
        <InstanceName>paas-xx-2</InstanceName>
        <Uuid>007ecd45-e90f-42xx-9eac-758407aa15xx</Uuid>
        <Proto>tcp</Proto>
        <InternetIp>118.xx.xx.7</InternetIp>
        <InstanceId>i-m5e56ycmxx07if43maxx</InstanceId>
        <Create>2020-02-18T15:52Z</Create>
        <Port>2379</Port>
```

`o``t`

```xml
379/ot
        <Ip>118.xx.xx.7</Ip>
        <ProcName>etcd</ProcName>
        <CreateTimestamp>1582012349000</CreateTimestamp>
        <IntranetIp>192.xx.xx.192</IntranetIp>
        <BindIp>::</BindIp>
  </Propertys>
  <Propertys>
        <InstanceName>paas-xx-2</InstanceName>
        <Uuid>007ecd45-e90f-4290-9exx-758407aa15xx</Uuid>
        <Proto>tcp</Proto>
        <InternetIp>118.xx.xx.7</InternetIp>
        <InstanceId>i-m5e56ycm6s07if43maxx</InstanceId>
        <Create>2020-02-18T15:52Z</Create>
        <Port>6443</Port>
        <Ip>118.xx.xx.7</Ip>
        <ProcName>kube-apiserver</ProcName>
        <CreateTimestamp>1582012349000</CreateTimestamp>
        <IntranetIp>192.xx.xx.192</IntranetIp>
        <BindIp>::</BindIp>
  </Propertys>
  <PageInfo>
        <Count>5</Count>
        <PageSize>5</PageSize>
        <TotalCount>762</TotalCount>
        <CurrentPage>1</CurrentPage>
  </PageInfo>
  <requestId>FAA793EF-5B14-4CDD-B3E0-B14D4342C422</requestId>
</DescribePropertyPortDetailResponse>
```

`JSON` format

```json
  "Propertys": [
       "InstanceName": "centos-xx",
              "Uuid": "00274759-73ef-485a-ae40-c2b5972f50cd",
             "Proto": "tcp",
             "InternetIp": "101.xx.xx.104",
             "InstanceId": "i-2ze645t5u9jo4txxx",
             "Create": "2020-01-09T13:53Z",
             "Port": "22",
             "Ip": "101.xx.xx.104",
             "ProcName": "sshd",
             "CreateTimestamp": 1578549227000,
             "IntranetIp": "192.xx.xx.96",
           "BindIp": "0.0.0.0"
```

`},`

```json
       "InstanceName": "paas-xxx-test1122",
             "Uuid": "007ecd45-e90f-4290-9eac-758407aa1509",
             "Proto": "tcp",
              "InternetIp": "118.xx.xx.7",
             "InstanceId": "i-m5e56ycm6xx7if43xx",
```

`"C` `t``"`

```
"20200218T1552Z"
```

```json
             "Create": "2020-02-18T15:52Z",
             "Port": "10251",
             "Ip": "118.xx.xx.7",
             "ProcName": "kube-scheduler",
             "CreateTimestamp": 1582012349000,
             "IntranetIp": "192.xx.xx.192",
             "BindIp": "::"
```

`},`

```json
       "InstanceName": "paas-xx-2",
             "Uuid": "007ecd45-e9xx-4290-9eac-758407aa15xx",
             "Proto": "tcp",
             "InternetIp": "118.xx.xx.7",
             "InstanceId": "i-m5e56ycm6s0xxf43maxx",
             "Create": "2020-02-18T15:52Z",
             "Port": "10252",
             "Ip": "118.xx.xx.7",
             "ProcName": "kube-controller-manager",
             "CreateTimestamp": 1582012349000,
             "IntranetIp": "192.xx.xx.192",
             "BindIp": "::"
```

`},`

```json
            "InstanceName": "paas-xx-2",
            "Uuid": "007ecd45-e90f-42xx-9eac-758407aa15xx",
            "Proto": "tcp",
            "InternetIp": "118.xx.xx.7",
            "InstanceId": "i-m5e56ycmxx07if43maxx",
            "Create": "2020-02-18T15:52Z",
            "Port": "2379",
            "Ip": "118.xx.xx.7",
            "ProcName": "etcd",
            "CreateTimestamp": 1582012349000,
            "IntranetIp": "192.xx.xx.192",
            "BindIp": "::"
```

`},`

```json
            "InstanceName": "paas-xx-2",
            "Uuid": "007ecd45-e90f-4290-9exx-758407aa15xx",
            "Proto": "tcp",
            "InternetIp": "118.xx.xx.7",
            "InstanceId": "i-m5e56ycm6s07if43maxx",
            "Create": "2020-02-18T15:52Z",
            "Port": "6443",
            "Ip": "118.xx.xx.7",
            "ProcName": "kube-apiserver",
            "CreateTimestamp": 1582012349000,
            "IntranetIp": "192.xx.xx.192",
            "BindIp": "::"
```

`],`

```json
"PageInfo": {
      "Count": 5,
      "PageSize": 5,
"TotalCount":762
```

```json
      TotalCount: 762,
      "CurrentPage": 1
```

`},`

```json
  "requestId": "FAA793EF-5B14-4CDD-B3E0-B14D4342C422"
```

For a list of error codes, see Error codes.

#### 3.10.3 DescribePropertyProcDetail

Queries the details of a process.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeProperty ProcDetail | The operation that you want to perform. Set the value to DescribePropertyProcDetail. |
| Cmdline | String | No | . /8888 | The parameter that is used to start the process. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| Name | String | No | 8888 | The name of the process. |
| PageSize | Integer | No | 5 | The number of entries to return on each page. |
| Remark | String | No | 1.2.3.4 | The name or IP address of the server. |
| User | String | No | root | The user who runs the process. |
| Uuid | String | No | c4678332-ef35- 4ad4-*** | The ID of the asset related to the process. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageInfo |   |   | The page information. |

| D S | eveloper Guide·Th ervice (TDS) | reat Detection |   | Apsara Stack Securit | y |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 1 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| PageSize | Integer | 5 | The number of entries returned per page. |
| TotalCount | Integer | 1 | The total number of returned entries. |
| Propertys | Array |   | The returned process information. |
| Cmdline | String | . /8888 | The parameter that was used to start the process. |
| Create | String | 2019-05-15T11:08Z | The last time when the data was collected. |
| CreateTimesta mp | Long | 1565686951000 | The timestamp of last data collection. |
| EuidName | String | root | The permission to run the process. |
| InstanceId | String | c4678332-ef35- 4ad4-8358-*** | The ID of the asset. |
| InstanceName | String | test-*** | The name of the asset. |
| InternetIp | String | 1.2.3.1 | The public IP address of the asset. |
| IntranetIp | String | 1.2.3.2 | The private IP address of the asset. |
| Md5 | String | N/A | The MD5 value of the file. |
| Name | String | 8888 | The name of the process. |
| Path | String | /root/Oracle/Middle ware/***/8888 | The path of the process. |
| Pid | String | 12826 | The ID of the process. |

| A | psara Stack Securi | ty |   | Developer Guide·Threat Detection Service (TDS | ) |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Pname | String | start***.s | The parent name of the process. |
| StartTime | String | 2019-08-07 10:09:05 | The time when the process started. |
| User | String | root | The user who runs the process. |
| Uuid | String | c4678332-ef35- 4ad4-8358-6*** | The ID of the asset related to the process. |
| RequestId | String | 64388374-A309- 4191-8606- 3346CCA364B0 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertyProcDetail
```

Sample success responses `XML` format

```xml
<DescribePropertyProcDetail>
   <RequestId>64388374-A309-4191-8606-3346CCA364B0</RequestId>
   <PageInfo>
      <Count>2</Count>
      <TotalCount>8184</TotalCount>
      <PageSize>2</PageSize>
      <CurrentPage>1</CurrentPage>
   </PageInfo>
   <Propertys>
      <User>N/A</User>
      <Uuid>90d4cc6a-806f-***</Uuid>
      <Md5>N/A</Md5>
      <CreateTimestamp>1557889713000</CreateTimestamp>
      <InstanceId>i-bp1***</InstanceId>
      <InternetIp></InternetIp>
      <Path>N/A</Path>
      <Name>N/A</Name>
      <IntranetIp>1.2.3.4</IntranetIp>
      <Create>2019-05-15T11:08Z</Create>
      <Pname>N/A</Pname>
      <EuidName>N/A</EuidName>
      <StartTime>N/A</StartTime>
      <Pid>0</Pid>
      <InstanceName>test_***</InstanceName>
      <Cmdline>N/A</Cmdline>
   </Propertys>
   <Propertys>
      <User>N/A</User>
      <Uuid>90d4cc6a-806f-4***</Uuid>
      <Md5>N/A</Md5>
      <CreateTimestamp>1557889713000</CreateTimestamp>
      <InstanceId>i-b***</InstanceId>
      <InternetIp></InternetIp>
      <Path>N/A</Path>
      <Name>N/A</Name>
      <IntranetIp>1.2.3.5</IntranetIp>
      <Create>2019-05-15T11:08Z</Create>
      <Pname>N/A</Pname>
      <EuidName>N/A</EuidName>
      <StartTime>N/A</StartTime>
      <Pid>4</Pid>
      <InstanceName>tsy_***</InstanceName>
      <Cmdline>N/A</Cmdline>
   </Propertys>
</DescribePropertyProcDetail>
```

`JSON` format

```json
 "RequestId":"64388374-A309-4191-8606-3346CCA364B0",
 "PageInfo":{
  "Count":2,
  "TotalCount":8184,
  "PageSize":2,
  "CurrentPage":1
```

`},`

```json
 "Propertys":[
   "User":"N/A",
   "Uuid":"90d4cc6a-806f-***",
   "Md5":"N/A",
   "CreateTimestamp":1557889713000,
   "InstanceId":"i-bp1***",
   "InternetIp":"",
   "Path":"N/A",
   "Name":"N/A",
   "IntranetIp":"1.2.3.4",
   "Create":"2019-05-15T11:08Z",
   "Pname":"N/A",
   "StartTime":"N/A",
   "EuidName":"N/A",
   "Pid":"0",
   "Cmdline":"N/A",
   "InstanceName":"test_***"
```

`},`

```json
   "User":"N/A",
   "Uuid":"90d4cc6a-806f-4***",
   "Md5":"N/A",
   "CreateTimestamp":1557889713000,
   "InstanceId":"i-b***",
   "InternetIp":"",
   "Path":"N/A",
   "Name":"N/A",
   "IntranetIp":"1.2.3.5",
   "Create":"2019-05-15T11:08Z",
   "Pname":"N/A",
   "StartTime":"N/A",
   "EuidName":"N/A",
   "Pid":"4",
   "Cmdline":"N/A",
   "InstanceName":"tsy_***"
```

`]` For a list of error codes, see Error codes.

#### 3.10.4 DescribePropertyPortItem

Queries information about ports.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeProperty PortItem | The operation that you want to perform. Set the value to DescribePropert yPort It em. |
| ForceFlush | Boolean | No | true | Specifies whether to force refresh the data that you want to query. |
| Port | String | No | 22 | The port number. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| PageSize | Integer | No | 5 | The number of entries to return on each page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | The ID of the request. |
| PropertyItems | Array |   | Details of the port. |
| Port | String | 22 | The number of the listener port. |
| Proto | String | tcp | The network protocol of the port. |
| Count | Integer | 495 | The number of servers that use the port. |
| PageInfo | Struct |   | The page information. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 5 | The number of entries returned on the current page. |
| PageSize | Integer | 5 | The number of entries returned per page. |
| TotalCount | Integer | 163 | The total number of entries. |
| CurrentPage | Integer | 1 | The page number of the current page. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertyPortItem
```

Sample success responses `XML` format

```xml
<DescribePropertyPortItemResponse>
        <RequestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</RequestId>
        <PropertyItems>
                <Port>22</Port>
                <Proto>tcp</Proto>
                <Count>495</Count>
        </PropertyItems>
        <PropertyItems>
                <Port>111</Port>
                <Proto>tcp</Proto>
                <Count>43</Count>
        </PropertyItems>
        <PropertyItems>
                <Port>6000</Port>
                <Proto>tcp</Proto>
                <Count>2</Count>
        </PropertyItems>
        <PropertyItems>
                <Port>53</Port>
                <Proto>tcp</Proto>
                <Count>1</Count>
        </PropertyItems>
        <PropertyItems>
                <Port>80</Port>
                <Proto>tcp</Proto>
                <Count>38</Count>
        </PropertyItems>
        <PageInfo>
                <Count>5</Count>
                <PageSize>5</PageSize>
                <TotalCount>163</TotalCount>
                <CurrentPage>1</CurrentPage>
        </PageInfo>
</DescribePropertyPortItemResponse>
```

`JSON` format

```json
  "requestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F",
  "PropertyItems": [
        "Port": "22",
        "Proto": "tcp",
        "Count": 495
```

`},`

```json
        "Port": "111",
        "Proto": "tcp",
        "Count": 43
```

`},`

```json
        "Port": "6000",
        "Proto": "tcp",
        "Count": 2
```

`},`

```json
        "Port": "53",
        "Proto": "tcp",
        "Count": 1
```

`},`

```json
        "Port": "80",
        "Proto": "tcp",
        "Count": 38
```

`],`

```json
  "PageInfo": {
      "Count": 5,
      "PageSize": 5,
      "TotalCount": 163,
      "CurrentPage": 1
```

For a list of error codes, see Error codes.

#### 3.10.5 DescribePropertyProcItem

Queries information about all processes.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeProperty ProcItem | The operation that you want to perform. Set the value to DescribePropertyProcItem. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| ForceFlush | Boolean | No | true | Specifies whether to force refresh the data that you want to query. |
| Name | String | No | test | The name of the process. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageInfo |   |   | The page information. |
| Count | Integer | 5 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| PageSize | Integer | 5 | The number of entries returned per page. |
| TotalCount | Integer | 372 | The total number of entries. |
| PropertyItems | Array |   | The process information. |
| Count | Integer | 8888 | The number of servers on which the process runs. |
| Name | String | .ss | The name of the process. |
| RequestId | String | BD8AD4C6-A169- 4FA3-BA1F- ED40ED52973B | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertyProcItem
```

Sample success responses `XML` format

```xml
<DescribePropertyProcItem>
  <PropertyItems>
        <Name>(sd-**)</Name>
        <Count>7</Count>
  </PropertyItems>
  <PropertyItems>
        <Name>6Cm***</Name>
        <Count>1</Count>
  </PropertyItems>
  <RequestId>BD8AD4C6-A169-4FA3-BA1F-ED40ED52973B</RequestId>
  <PageInfo>
        <Count>2</Count>
        <TotalCount>395</TotalCount>
        <PageSize>2</PageSize>
        <CurrentPage>1</CurrentPage>
  </PageInfo>
</DescribePropertyProcItem>
```

`JSON` format

```json
 "RequestId":"BD8AD4C6-A169-4FA3-BA1F-ED40ED52973B",
 "PropertyItems":[
   "Name":"(sd-**)",
   "Count":7
```

`},`

```json
   "Name":"6Cm***",
   "Count":1
```

`],`

```json
 "PageInfo":{
  "Count":2,
  "TotalCount":395,
  "PageSize":2,
  "CurrentPage":1
```

For a list of error codes, see Error codes.

#### 3.10.6 DescribePropertySoftwareDetail

Queries details of a software asset.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeProperty SoftwareDetail | The operation that you want to perform. Set the value to DescribePropertySoftwareDetail. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| Name | String | No | tes*** | The name of the software. |
| PageSize | Integer | No | 5 | The number of entries to return on each page. |
| Path | String | No | /etc/test | The directory where the software is installed. |
| Remark | String | No | 1.2.3.4 | The name or IP address of the server. |
| SoftwareVersion | String | No | 11 | The version of the software. |
| Uuid | String | No | 50d213b4-3a35- 427a-b8a5-*** | The ID of the software asset. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageInfo |   |   | The page information. |
| Count | Integer | 2 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| PageSize | Integer | 2 | The number of entries returned per page. |

| psara Stack Securi | ty |   | Developer Guide·Threat Detection Service (TDS |
|---|---|---|---|
| Parameter | Type | Example | Description |

| TotalCount | Integer | 23 | The total number of entries. |
|---|---|---|---|
| Propertys | Array |   | The details of the software. |
| Create | Long | 1565539587000 | The last time when the data was collected. |
| CreateTimesta mp | Long | 1565539587000 | The timestamp of last data collection. |
| InstallTime | String | 2017-09-07 10:54:49 | The time when the software was installed. |
| InstanceId | String | i-uf*** | The ID of the asset. |
| InstanceName | String | test | The name of the asset. |
| InternetIp | String | 1.2.3.1 | The public IP address of the asset. |
| IntranetIp | String | 1.2.3.2 | The private IP address of the asset. |
| Ip | String | 1.2.3.1 | The public IP address of the asset. |
| Name | String | aaa base _ | The name of the software. |
| Path | String | /etc/test | The directory where the software is installed. |
| Uuid | String | 4ef1115b-e423- 4b4b-b930-*** | The UUID of the software version. |
| Version | String | 11 | The version of the software. |
| RequestId | String | 9C5AE850-7140- 4DE6-B892- 055EB0D9F28A | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertySoftwareDetail
```

Sample success responses `XML` format

```xml
<DescribePropertySoftwareDetail>
  <RequestId>9C5AE850-7140-4DE6-B892-055EB0D9F28A</RequestId>
  <PageInfo>
        <Count>2</Count>
        <TotalCount>35795</TotalCount>
        <PageSize>2</PageSize>
        <CurrentPage>1</CurrentPage>
  </PageInfo>
  <Propertys>
        <Uuid>04c56617-23fc-***</Uuid>
        <Name>abrt</Name>
        <Ip>1.2.3.1</Ip>
        <CreateTimestamp>1561330240000</CreateTimestamp>
        <IntranetIp>1.2.3.3</IntranetIp>
        <InstanceId>i-bp***</InstanceId>
        <Create>2019-06-24T06:50Z</Create>
        <InternetIp>1.2.3.1</InternetIp>
        <InstallTime>2014-08-14 21:18:50</InstallTime>
        <Version>2.0.8</Version>
        <InstanceName>Test***</InstanceName>
        <Path>/etc/abrt</Path>
  </Propertys>
  <Propertys>
        <Uuid>c038fd42-3151-4***</Uuid>
        <Name>abrt</Name>
        <Ip>1.2.3.5</Ip>
        <CreateTimestamp>1562283761000</CreateTimestamp>
        <IntranetIp>1.2.3.6</IntranetIp>
        <InstanceId>i-b***</InstanceId>
        <Create>2019-07-05T07:42Z</Create>
        <InternetIp>1.2.3.5</InternetIp>
        <InstallTime>2014-11-21 18:23:32</InstallTime>
        <Version>2.1.11</Version>
        <InstanceName>Test***</InstanceName>
        <Path>/etc/abrt</Path>
  </Propertys>
</DescribePropertySoftwareDetail>
```

`JSON` format

```json
 "RequestId":"9C5AE850-7140-4DE6-B892-055EB0D9F28A",
 "PageInfo":{
  "Count":2,
  "TotalCount":35795,
  "PageSize":2,
  "CurrentPage":1
```

`},`

```json
 "Propertys":[
   "Name":"abrt",
   "Uuid":"04c56617-23fc-***",
   "Ip":"1.2.3.1",
   "CreateTimestamp":1561330240000,
   "Create":"2019-06-24T06:50Z",
   "InstanceId":"i-bp***",
   "IntranetIp":"1.2.3.3",
   "InternetIp":"1.2.3.1",
   "InstallTime":"2014-08-14 21:18:50",
   "Version":"2.0.8",
   "InstanceName":"test****",
   "Path":"/etc/abrt"
```

`},`

```json
   "Name":"abrt",
   "Uuid":"c038fd42-3151-4***",
   "Ip":"1.2.3.5",
   "CreateTimestamp":1562283761000,
   "Create":"2019-07-05T07:42Z",
   "InstanceId":"i-b***",
   "IntranetIp":"1.2.3.6",
   "InternetIp":"1.2.3.5",
   "InstallTime":"2014-11-21 18:23:32",
   "Version":"2.1.11",
   "InstanceName":"Test****",
   "Path":"/etc/abrt"
```

`]` For a list of error codes, see Error codes.

#### 3.10.7 DescribePropertySoftwareItem

Queries information about all software assets.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeProperty SoftwareItem | The operation that you want to perform. Set the value to DescribePropert ySof t wareIt em. |
| ForceFlush | Boolean | No | true | Specifies whether to force refresh the data that you want to query. |
| Name | String | No | test | The name of the software. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 3A85CFCF-05C8- 451A-9E41- C0D5E96BA407 | The ID of the request. |
| PropertyItems | Array |   | The returned software assets. |
| Name | String | aaa base _ | The name of the returned software asset. |
| Count | Integer | 23 | The number of servers on which the software is installed. |
| PageInfo | Struct |   | The page information. |
| Count | Integer | 2 | The number of entries returned on the current page. |
| PageSize | Integer | 2 | The number of entries returned per page. |
| TotalCount | Integer | 5037 | The total number of returned entries. |

| psara Stack Securi | ty |   | Developer Guide·Threat Detection |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| CurrentPage | Integer | 1 | The page number of the current page. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertySoftwareItem
```

Sample success responses `XML` format

```xml
<DescribePropertySoftwareItemResponse>
      <PageInfo>
                <Count>2</Count>
                <PageSize>2</PageSize>
                <TotalCount>5037</TotalCount>
                <CurrentPage>1</CurrentPage>
      </PageInfo>
      <PropertyItems>
                <Name>a11y-profile-manager-indicator</Name>
                <Count>1</Count>
      </PropertyItems>
      <PropertyItems>
                <Name>aaa_base</Name>
                <Count>23</Count>
      </PropertyItems>
      <requestId>3A85CFCF-05C8-451A-9E41-C0D5E96BA407</requestId>
</DescribePropertySoftwareItemResponse>
```

`JSON` format

```json
  "PageInfo": {
      "Count": 2,
      "PageSize": 2,
      "TotalCount": 5037,
      "CurrentPage": 1
```

`},`

```json
    "PropertyItems": [
        "Name": "a11y-profile-manager-indicator",
        "Count": 1
```

`},`

```json
        "Name": "aaa_base",
        "Count": 23
```

`],`

```json
     "requestId": "3A85CFCF-05C8-451A-9E41-C0D5E96BA407"
```

For a list of error codes, see Error codes.

#### 3.10.8 DescribePropertyUserDetail

Queries the details of an account in the account list.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeProperty UserDetail | The operation that you want to perform. Set the value to DescribePropert yUserDet ail. |
| Remark | String | No | 0.0.0.0 | The name or IP address of the server. |
| User | String | No | test | The name of the account that you want to query. |
| IsRoot | String | No | 0 | Specifies whether the account has root permissions. Valid values: 0: The account does not have root permissions. 1: The account has root permissions. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Uuid | String | No | 50d213b4-3a35- 427a-b8a5- 04b0c7e1f4d2 | The UUID of the asset. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 2 | The number of entries to return on each page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | FAA793EF-5B14- 4CDD-B3E0- B14D4342C422 | The ID of the request. |
| Propertys | Array |   | The returned account details. |
| LastLoginTime | String | xxxx | The time of the last logon. |
| IsRoot | String | 0 | Indicates whether the account has root permissions. 0: The account does not have root permissions. 1: The account has root permissions. |
| InstanceName | String | null | The name of the asset. |
| AccountsExpira tionDate | String | never | The expiration date of the account. |
| PasswordExpira tionDate | String | never | The expiration date of the account password. |
| Ip | String | null | The IP address of the asset. |
| Create | String | 1565644643000 | The timestamp when the last asset fingerprint was collected. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| CreateTimesta mp | Long | 1565644643000 | The timestamp generated for the asset fingerprint. |
| User | String | adm | The name of the account. |
| Uuid | String | 02c4a5dc-c2d2- 483a-9015- f972b44d2cd9 | The UUID of the asset. |
| LastLoginIp | String | N/A | The source IP address of the last logon. |
| InstanceId | String | 02c4a5dc-c2d2- 483a-9015- f972b44d2cd9 | The ID of the asset. |
| IntranetIp | String | 0.0.0.0 | The private IP address of the asset. |
| InternetIp | String | 0.0.0.0 | The public IP address of the asset. |
| Status | String | 0 | The logon status of the account. Valid values: 0: The account cannot log on. 1: The account can log on. |
| GroupNames | List | adm | The name of the user group. |
| PageInfo | Struct |   | The page information. |
| Count | Integer | 2 | The number of entries returned on the current page. |
| PageSize | Integer | 2 | The number of entries returned per page. |
| TotalCount | Integer | 384 | The total number of returned entries. |
| CurrentPage | Integer | 1 | The page number of the returned page. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertyUserDetail
```

Sample success responses `XML` format

```xml
<DescribePropertyUserDetailResponse>
  <requestId>FAA793EF-5B14-4CDD-B3E0-B14D4342C422</requestId>
  <PageInfo>
        <Count>2</Count>
        <PageSize>2</PageSize>
        <TotalCount>384</TotalCount>
        <CurrentPage>1</CurrentPage>
  </PageInfo>
  <Propertys>
        <LastLoginTime>N/A</LastLoginTime>
        <GroupName>adm</GroupName>
        <IsRoot>0</IsRoot>
        <InstanceName></InstanceName>
        <AccountsExpirationDate>never</AccountsExpirationDate>
        <PasswordExpirationDate>never</PasswordExpirationDate>
        <Ip></Ip>
        <Create>1565644643000</Create>
        <Status>0</Status>
        <User>adm</User>
        <Uuid>00ea0155-548e-4f32-bb53-3a000110b30d</Uuid>
        <LastLoginIp>N/A</LastLoginIp>
  </Propertys>
  <Propertys>
        <LastLoginTime>N/A</LastLoginTime>
        <GroupName>adm</GroupName>
        <IsRoot>0</IsRoot>
        <InstanceName></InstanceName>
        <AccountsExpirationDate>never</AccountsExpirationDate>
        <PasswordExpirationDate>never</PasswordExpirationDate>
        <Ip></Ip>
        <Create>1565652008000</Create>
        <Status>0</Status>
        <User>adm</User>
        <Uuid>02c4a5dc-c2d2-483a-9015-f972b44d2cd9</Uuid>
        <LastLoginIp>N/A</LastLoginIp>
  </Propertys>
</DescribePropertyUserDetailResponse>
```

`JSON` format

```json
    "requestId": "FAA793EF-5B14-4CDD-B3E0-B14D4342C422",
    "PageInfo": {
      "Count": 2,
      "PageSize": 2,
      "TotalCount": 384,
      "CurrentPage": 1
```

`},`

```json
    "Propertys": [
        "LastLoginTime": "N/A",
        "GroupName": [
          "adm"
```

`],`

```json
        "IsRoot": "0",
        "InstanceName": null,
        "AccountsExpirationDate": "never",
        "PasswordExpirationDate": "never",
        "Ip": null,
        "Create": 1565644643000,
        "Status": 0,
        "User": "adm",
        "Uuid": "00ea0155-548e-4f32-bb53-3a000110b30d",
        "LastLoginIp": "N/A"
```

`},`

```json
        "LastLoginTime": "N/A",
        "GroupName": [
          "adm"
```

`],`

```json
        "IsRoot": "0",
        "InstanceName": null,
        "AccountsExpirationDate": "never",
        "PasswordExpirationDate": "never",
        "Ip": null,
        "Create": 1565652008000,
        "Status": 0,
        "User": "adm",
        "Uuid": "02c4a5dc-c2d2-483a-9015-f972b44d2cd9",
        "LastLoginIp": "N/A"
```

`]` For a list of error codes, see Error codes.

#### 3.10.9 DescribePropertyUserItem

Queries the account information about an asset. q p

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeProperty UserItem | The operation that you want to perform. Set the value to DescribePropertyUserItem. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| ForceFlush | Boolean | No | true | Specifies whether to force refresh the data that you want to query. |
| PageSize | Integer | No | 2 | The number of entries to return on each page. |
| User | String | No | adm | The account information about the asset fingerprint. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageInfo |   |   | The page information. |
| Count | Integer | 2 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| PageSize | Integer | 2 | The number of entries returned per page. |
| TotalCount | Integer | 114 | The total number of returned entries. |
| PropertyItems | Array |   | The account information. |
| Count | Integer | 384 | The number of servers that belong to the current account. |
| User | String | adm | The name of the account. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 76068BE2-F9C4- 4EDD-967B- F503B8CCDD3D | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertyUserItem
```

Sample success responses `XML` format

```xml
<DescribePropertyUserItem>
  <PropertyItems>
        <User>a123456</User>
        <Count>1</Count>
  </PropertyItems>
  <PropertyItems>
        <User>aaaa</User>
        <Count>1</Count>
  </PropertyItems>
  <PropertyItems>
        <User>aaaa1</User>
        <Count>1</Count>
  </PropertyItems>
  <RequestId>76068BE2-F9C4-4EDD-967B-F503B8CCDD3D</RequestId>
  <PageInfo>
        <Count>3</Count>
        <TotalCount>340</TotalCount>
        <PageSize>3</PageSize>
        <CurrentPage>1</CurrentPage>
  </PageInfo>
</DescribePropertyUserItem>
```

`JSON` format

```json
 "RequestId":"76068BE2-F9C4-4EDD-967B-F503B8CCDD3D",
 "PropertyItems":[
   "User":"a123456",
   "Count":1
```

`},`

```json
   "User":"aaaa",
   "Count":1
```

`},`

```json
   "User":"aaaa1",
   "Count":1
```

`],`

```json
 "PageInfo":{
  "Count":3,
  "TotalCount":340,
  "PageSize":3,
  "CurrentPage":1
```

For a list of error codes, see Error codes.

#### 3.10.10 DescribeModuleConfig

Queries the configurations of asset fingerprint modules.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeModuleC onfig | The operation that you want to perform. Set the value to DescribeModuleConfig. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | The ID of the request. |
| Success | Boolean | true | Indicates whether the request is successful. |

| S | Developer Guide·Th ervice (TDS) | reat Detection |   | Apsara Stack Securit | y |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 2 | The number of module configurations. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| ModuleConfigLi st | Array |   | The list of module configurations. |
| ConfigName | String | timescan | The name of the configuration. |
| ModuleName | String | alihids | The name of the template. |
| Items | Array |   | The list of configuration items. |
| InstanceId | String | lb-xxx | The ID of the instance. |
| InstanceName | String | ssxxxxxxxx | The name of the instance. |
| GroupId | Integer | 173 | The ID of the group. |
| Ip | String | 2.2.2.2 | The IP address of the instance. |
| Region | String | outside-of-aliyun | The region where the instance is deployed. |
| Uuid | String | lb-xxxx-xxxx-xxxx- xxxx | The UUID of the server. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeModuleConfig
```

Sample success responses `XML` format

```xml
<code>200</code> <data>
    <Count>2</Count>
    <ModuleConfigList>
        <ConfigName>timescan</ConfigName>
        <ModuleName>alihids</ModuleName>
        <Items>
            <InstanceName>ssxxxxxxxx</InstanceName>
            <Uuid>lb-xxxx-xxxx-xxxx-xxxx</Uuid>
            <InstanceId>lb-xxx</InstanceId>
            <Ip>2.2.2.2</Ip>
            <Region>cn-qingdao</Region>
            <GroupId>173</GroupId>
        </Items>
        <Items>
            <InstanceName>3a04702ca5a0</InstanceName>
            <Uuid>inet-db626549-870c-4d3e-b0b5-4d8a5c7268a6</Uuid>
            <Ip>192.1.2.3</Ip>
            <Region>outside-of-aliyun</Region>
            <GroupId>343</GroupId>
        </Items>
    </ModuleConfigList>
    <ModuleConfigList>
        <ConfigName>sysvulfix</ConfigName>
        <ModuleName>alihids</ModuleName>
        <Items>
            <InstanceName>xx</InstanceName>
            <Uuid>lb-xxx</Uuid>
            <InstanceId>lb-xxx</InstanceId>
            <Ip>2.2.2.2</Ip>
            <Region>cn-qingdao</Region>
            <GroupId>173</GroupId>
        </Items>
        <Items>
            <InstanceName>3a04702ca5a0</InstanceName>
            <Uuid>inet-db626549-870c-4d3e-b0b5-4d8a5c7268a6</Uuid>
            <Ip>192.168.5.3</Ip>
            <Region>outside-of-aliyun</Region>
            <GroupId>343</GroupId>
        </Items>
    </ModuleConfigList>
</data> <requestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</requestId> <success>true</success>
```

`JSON` format

```json
  "code": 200,
  "data": {
    "Count": 2,
    "ModuleConfigList": [{
        "ConfigName": "timescan",
        "ModuleName": "alihids",
        "Items": [{
            "InstanceName": "ssxxxxxxxx",
            "Uuid": "lb-xxxx-xxxx-xxxx-xxxx",
            "InstanceId": "lb-xxx",
            "Ip": "2.2.2.2",
            "Region": "cn-qingdao",
            "GroupId": 173
```

`},`

```json
            "InstanceName": "3a04702ca5a0",
            "Uuid": "inet-db626549-870c-4d3e-b0b5-4d8a5c7268a6",
            "Ip": "192.1.2.3",
            "Region": "outside-of-aliyun",
            "GroupId": 343
```

`]` `},`

```json
        "ConfigName": "sysvulfix",
        "ModuleName": "alihids",
        "Items": [{
            "InstanceName": "xx",
            "Uuid": "lb-xxx",
            "InstanceId": "lb-xxx",
            "Ip": "2.2.2.2",
            "Region": "cn-qingdao",
            "GroupId": 173
```

`},`

```json
            "InstanceName": "3a04702ca5a0",
            "Uuid": "inet-db626549-870c-4d3e-b0b5-4d8a5c7268a6",
            "Ip": "192.168.5.3",
            "Region": "outside-of-aliyun",
            "GroupId": 343
```

`]` `]` `},`

```json
  "requestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F",
  "success": true
```

For a list of error codes, see Error codes.

### 3.11 Notifications

#### 3.11.1 DescribeDingTalk

Queries DingTalk notifications.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDingTalk | The operation that you want to perform. Set the value to DescribeDingTalk. |
| RuleActionName | String | No | Vulnerability notification | The name of the notification. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B256A525-7E42- 4BB9-A27C- 9017FDDFF1A2 | The ID of the request. |
| ActionList | Array |   | The list of notifications. |
| GmtModified | Long | 1550828400000 | The timestamp when the notification was modified. |
| Id | Integer | 1 | The ID of the notification. |
| AliUid | Long | 12312412341 | The UID of the user. |
| GmtCreate | Long | 1550828400000 | The timestamp when the notification was created. |
| Url | String | https://oapi.dingtal k.com/robot/send | The parameters of the notification. |

| Developer Guide·Th ervice (TDS) | reat Detection |   | Apsara Stack Securit |
|---|---|---|---|
| Parameter | Type | Example | Description |
| IntervalTime | Integer | 1000 | The notification interval. |
| ActionName | String | Alert notification | The name of the notification. |
| Status | Integer | 1 | The status of the notification. Valid values: 0: disabled 1: enabled |
| ConfigList | String | [{\"type\":\"vul\",\" configItemList\": [{\"key\":\"key\", \"valueList\":\"123\ "}]}] | The list of notification settings. |
| GroupIdList | String | "123,456" | GroupidList. |
| DingTalkLang | String | zh | The natural language of notifications. Valid values: zh: Chinese en: English |
| PageInfo | Struct |   | The page information. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| TotalCount | Integer | 1 | The number of notifications. |
| CurrentPage | Integer | 1 | The page number of the current page. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeDingTalk
```

Sample success responses `XML` format

```xml
<data >
    <PageInfo>
        <PageSize>20</PageSize>
        <CurrentPage>1</CurrentPage>
        <TotalCount>1</TotalCount>
    </PageInfo>
    <ActionList>
        <ActionName>Alert notification</ActionName>
        <GmtCreate>1550828400000</GmtCreate>
        <GmtModified>1550828400000</GmtModified>
        <IntervalTime>1000</IntervalTime>
        <Id>1</Id>
        <Url>https://oapi.dingtalk.com/robot/send</Url>
        <AliUid>12312412341</AliUid>
        <configList>[{"type":"vul","configItemList":[{"key":"key", "valueList":"123"}]}]</c
onfigList>
        <groupIdList>123,456</groupIdList>
    </ActionList>
</data > <requestId>B256A525-7E42-4BB9-A27C-9017FDDFF1A2</requestId>
```

`JSON` format

```json
  "data ": {
    "PageInfo": {
      "PageSize": 20,
      "CurrentPage": 1,
      "TotalCount":1
```

`},`

```json
    "ActionList": [{
      "ActionName": "Alert notification",
      "GmtCreate": "1550828400000",
      "GmtModified": "1550828400000",
      "IntervalTime": 1000,
      "Id": 1,
      "Url": "https://oapi.dingtalk.com/robot/send",
      "AliUid": 12312412341,
      "configList":"[{\"type\":\"vul\",\"configItemList\":[{\"key\":\"key\", \"valueList\":
\"123\"}]}]",
      "groupIdList":"123,456"
```

`}]` `},`

```json
  "requestId": "B256A525-7E42-4BB9-A27C-9017FDDFF1A2"
```

For a list of error codes, see Error codes.

#### 3.11.2 DescribeNoticeConfig

Queries the notification settings.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeNoticeCo nfig | The operation that you want to perform. Set the value to DescribeNoticeConfig. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D185B7FF-E24C- 422D-83D3- C2A25C7A2727 | The ID of the request. |
| NoticeConfigLis t | Array |   | Details of the notification settings. |
| TimeLimit | Integer | 1 | The time period during which notifications can be sent to the recipients. Valid values: 0: any time 1: 08:00 to 22:00 |
| Route | Integer | 7 | The notification method. |
| Project | String | sas suspicious _ | The project identifier. |
| AliUid | Long | 121234141424 | The UID of the user. |
| CurrentPage | Integer | 1 | The page number of the current page. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeNoticeConfig
```

Sample success responses `XML` format

```xml
<code>200</code> <data>
    <RequestId>D185B7FF-E24C-422D-83D3-C2A25C7A2727</RequestId>
    <NoticeConfigList>
        <Project>sas_suspicious</Project>
        <CurrentPage>1</CurrentPage>
        <TimeLimit>1</TimeLimit>
        <Route>7</Route>
        <AliUid>1049769453489698</AliUid>
    </NoticeConfigList>
    <NoticeConfigList>
        <Project>sas_healthcheck</Project>
        <CurrentPage>1</CurrentPage>
        <TimeLimit>1</TimeLimit>
        <Route>7</Route>
        <AliUid>1049769453489698</AliUid>
    </NoticeConfigList>
</data>
```

`JSON` format

```json
  "code": 200,
  "data": {
  "RequestId":"D185B7FF-E24C-422D-83D3-C2A25C7A2727",
  "NoticeConfigList":[
      "Project":"sas_suspicious",
      "CurrentPage":1,
      "TimeLimit":1,
      "Route":7,
      "AliUid":10497611111111
```

`},`

```json
      "Project":"sas_healthcheck",
      "CurrentPage":1,
      "TimeLimit":1,
      "Route":7,
      "AliUid":10422222222
```

`]` For a list of error codes, see Error codes.

### 3.12 Agent client

#### 3.12.1 SasInstallCode

Queries the verification key used to run the agent installation command.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SasInstallCode | The operation that you want to perform. Set the value to SasInstallCode. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B256A525-7E42- 4BB9-A27C- 9017FDDFF1A2 | The ID of the request. |
| data | String | eDkhGP | The verification key used to run the installation command when you manually install the Threat Detection Service agent. |

Sample requests

```
http(s)://[Endpoint]/?Action=SasInstallCode
```

Sample success responses `XML` format

```xml
<SasInstallCodeResponse>
  <requestId>B256A525-7E42-4BB9-A27C-9017FDDFF1A2</requestId>
  <data>eDkhGP</data>
</SasInstallCodeResponse>
```

`JSON` format

```json
  "requestId": "B256A525-7E42-4BB9-A27C-9017FDDFF1A2",
  "data":"eDkhGP"
```

For a list of error codes, see Error codes.

#### 3.12.2 PauseClient

Enables or disables the Threat Detection Service agent.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | PauseClient | The operation that you want to perform. Set the value to PauseClient . |
| Uuids | String | Yes | uuid-1211-sadsd- 2131 | The UUIDs of servers for which the Threat Detection Service agent needs to be enabled or disabled. |
| Value | String | Yes | 1 | The status of the Threat Detection Service agent. Valid values: 0: disabled 1: enabled |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6673D49C-A9AB- 40DD-B4A2- B92306701AE7 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=PauseClient &Uuids=uuid-1211-sadsd-2131 &Value=1
```

Sample success responses `XML` format

```xml
<PauseClientResponse>
  <requestId>6673D49C-A9AB-40DD-B4A2-B92306701AE7</requestId>
</PauseClientResponse>
```

`JSON` format

```json
 "requestId": "6673D49C-A9AB-40DD-B4A2-B92306701AE7"
```

For a list of error codes, see Error codes.

### 3.13 Export check results

#### 3.13.1 ExportRecord

Exports baseline check, asset fingerprint check, and AccessKey leak check results to Excel files.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ExportRecord | The operation that you want to perform. Set the value to Export Record. |
| ExportType | String | Yes | accessKey | The type of the check whose result can be exported. Valid values: baseline: Alibaba Cloud service baseline asset Inst ance: assets at t ack: attack analysis accessKey: AccessKey pair leaks user: the accounts covered by asset fingerprints port : the ports covered by asset fingerprints process: the processes covered by asset fingerprints sof t ware: the software covered by asset fingerprints |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Params | String | No | {"level":"high"} | The conditions to filter check results in the files to which the check results are exported. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| FileName | String | cms 20171101.xlsx _ | The name of the exported file. |
| Id | Long | 131231 | The ID of the exported file. |
| RequestId | String | 6673D49C-A9AB- 40DD-B4A2- B92306701AE7 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=ExportRecord &ExportType=accessKey
```

Sample success responses `XML` format

```xml
<ExportRecordResponse>
  <Id>131231</Id>
  <FileName>cms_20171101.xlsx</FileName>
  <requestId>6673D49C-A9AB-40DD-B4A2-B92306701AE7</requestId>
</ExportRecordResponse>
```

`JSON` format

```json
    "Id": 131231,
    "FileName" : "cms_20171101.xlsx",
    "requestId": "6673D49C-A9AB-40DD-B4A2-B92306701AE7"
```

For a list of error codes, see Error codes.

### 3.14 Virus detection

#### 3.14.1 OperateSuspiciousTargetConfig

Configures virus detection.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | OperateSuspiciou sTargetConfig | The operation that you want to perform. Set the value to Operat eSuspiciousT arget Conf ig. |
| TargetOperations | String | Yes | " [{\"targetType\": \"uuid\",\"target \":\"0585f81a- dd84-4ddf-9971- f59d12345678\", \"flag\":\"add\"} , {\"targetType\":\ "uuid\",\"target\ ":\"01acfd9d- e6a4-4e61-b9eb- aae012345678\", \"flag\":\"add\"} , {\"targetType\":\ "uuid\",\"target\ ":\"04a0e735- ad32-4835-b635- 045812345678\", \"flag\":\"add\"} ]" | The parameters required to configure virus detection for the server. Set the following parameters: t arget T ype: the dimension on which viruses are blocked. UUIDs are supported. Set the value to uuid. t arget : the UUID of the server on which you want to configure virus detection. f lag: enables or disables virus detection for the server. Valid values: add and del. add specifies to enable the feature and del specifies to disable the feature. |
| TargetType | String | Yes | uuid | The operating dimension on which you manage virus detection. You can manage virus detection only by UUID. Set the value to uuid. |
| Type | String | Yes | auto breaking _ | The method of virus detection. Set the value to aut o breaking, _ which specifies that the system automatically blocks viruses. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | ABCD-PSD2-5256- 1DSA-4222-JHBN | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=OperateSuspiciousTargetConfig &TargetOperations="[{\"targetType\":\"uuid\",\"target\":\"0585f81a-dd84-4ddf-9971-f59d12345 678\",\"flag\":\"add\"},{\"targetType\":\"uuid\",\"target\":\"01acfd9d-e6a4-4e61-b9eb-aae01 2345678\",\"flag\":\"add\"},{\"targetType\":\"uuid\",\"target\":\"04a0e735-ad32-4835-b635-0 45812345678\",\"flag\":\"add\"}]" &TargetType=uuid &Type=auto_breaking
```

Sample success responses `XML` format

```xml
<OperateSuspiciousTargetConfigResponse>
  <RequestId>ABCD-PSD2-5256-1DSA-4222-JHBN</RequestId>
</OperateSuspiciousTargetConfigResponse>
```

`JSON` format

```json
    "RequestId":"ABCD-PSD2-5256-1DSA-4222-JHBN"
```

For a list of error codes, see Error codes.

## 4 Server Guard

### 4.1 List of operations

This topic introduces all the Server Guard operations that you can call. For more information, see the corresponding operation description. Asset management operations

| Operation | Description |
|---|---|
| CreateGroup | Creates an asset group. |
| DescribeGroupSummary | Obtains a list of asset groups. |
| DescribeGroupStruct | Queries the structure of an asset group. |
| DeleteGroup | Deletes an asset group. |
| DescribeAllTag | Queries the tag information of all servers. |
| DescribeBetachTag | Queries the tag information of a specified server. |
| ModifyBetachTag | Modifies the tags of multiple specified servers. |
| DeleteTag | Deletes the tag of a server. |
| DescribeAllEntity | Queries information about all servers. |
| DescribeEntityList | Queries a type of servers. |
| ModifyEntityGroup | Modifies the asset group information for a specified server. |
| DescribeMachines | Queries servers that match the specified criteria. |
| DescribeMachineDetail | Queries the detailed information about the specified server. |
| DescribePropertyScheduleConfig | Queries the update cycle of server information. |
| ModifyPropertyScheduleConfig | Modifies the synchronization cycle of host asset information. |
| DescribePropertyStatistic | Queries server statistics. |
| DescribePropertyPortItem | Obtains a list of listener ports on servers. |
| DescribePropertyPortDetail | Queries detailed listening port information. |
| DescribePropertyPortDiff | Queries listening port changes. |
| DescribePropertyProcItem | Obtains a list of server processes. |

| psara Stack Security | Developer Guide·Server Guar |
|---|---|

| Operation | Description |
|---|---|
| DescribePropertyProcDetail | Queries server process details. |
| DescribePropertyProcDiff | Queries process changes of servers. |
| DescribePropertySoftwareItem | Queries servers that have been installed with the specified application. |
| DescribePropertySoftwareDetail | Obtains the details of application software installed on a server. |
| DescribePropertySoftwareDiff | Queries changes of applications that have been installed on servers. |
| DescribePropertyUserItem | Queries user account information. |
| DescribePropertyUserDetail | Queries user account details. |
| DescribePropertyUserDiff | Queries user account changes. |
| PushAllTask | Performs a quick security check on specified servers. |
| DescribeTopRiskyAssets | Obtains a list of top N vulnerable servers. |
| UnbindAegis | Disables Server Guard for a specified server. |
| UninstallAegis | Uninstalls the Server Guard client from a specified server. |

Vulnerability management operations

| Operation | Description |
|---|---|
| DescribeTarget | Queries the servers that are checked for the specified type of risks in vulnerability management. |
| ModifyVulTarget | Modifies the servers for detecting a specified type of vulnerability in the vulnerability management settings. |
| DescribeVulTargetStatistics | Queries the information about target hosts for which vulnerability detection is enabled in the vulnerability management configuration. |
| DescribeTargetConfig | Queries the vulnerability scanning configuration information of a specified server. |
| ModifyTargetConfig | Modifies the vulnerability scanning configuration for a specified server. |
| DescribeVulConfig | Queries the global scanning configuration for each vulnerability type. |

| eveloper Guide·Server Guard | Apsara Stack Securit |
|---|---|
| Operation | Description |
| ModifyVulConfig | Modifies the global vulnerability scanning configuration. |
| DescribeAutoDelConfig | Queries the number of days that an invalid vulnerability is kept for before it is automatically deleted in the vulnerability management settings. |
| ModifyAutoDelConfig | Modifies the number of days that an invalid vulnerability is kept for before it is automatically deleted in the vulnerability management settings. |
| DescribeVulLevel | Queries the vulnerability severities that require attention. |
| ModifyVulLevel | Changes the vulnerability severities that require attention. |
| CreateVulWhitelist | Adds a specified vulnerability to the whitelist. |
| DescribeVulWhitelist | Obtains the whitelist of vulnerabilities. |
| DeleteVulWhitelist | Deletes a specified vulnerability from the vulnerability whitelist. |
| DescribeGroupedVul | Queries information about the specified vulnerability group. |
| DescribeVulList | Obtains a list of application vulnerabilities. |
| DescribeVulDetails | Queries detailed information about a vulnerability. |
| DescribeVulNumStatistics | Queries vulnerability statistics. |
| DescribeVulLevelStatistics | Obtains the statistics on vulnerabilities by vulnerability severity. |
| DescribeVulMachineList | Queries the vulnerability statistics of a specified server. |
| OperateVul | Handles detected vulnerabilities. |
| ModifyBatchIgnoreVul | Ignores multiple vulnerabilities. |
| DeleteVulBatch | Deletes a specified batch of vulnerabilities. |
| ExportVul | Exports vulnerability records that match the specified criteria. |
| DescribeVulExportInfo | Queries the information about vulnerability record export tasks. |

Baseline check operations

| Operation | Description |
|---|---|
| DescribeStrategy | Obtains a list of baseline check policies. |
| DescribeStratetyDetail | Queries the details of a specified baseline check policy. |

| psara Stack Security | Developer Guide·Server Guar |
|---|---|

| Operation | Description |
|---|---|
| ModifyStrategy | Modifies the basic information of a baseline check policy. |
| DeleteStrategy | Deletes a specified baseline check policy. |
| DescribeStrategyTarget | Queries the information about asset groups to which a specified baseline check policy applies. |
| ModifyStrategyTarget | Modifies the information about the asset groups that a specified baseline check policy applies to. |
| DescribeUuidConfig | Checks whether baseline check is enabled for a specified server. |
| ModifyMachineConfig | Configures whether to apply a specified baseline check policy to a specified server. |
| DescribeUserSetting | Queries the number of days an invalid risk is kept for before it is automatically deleted in baseline check. |
| CreateUserSetting | Specifies the number of days an invalid risk is kept for before it is automatically deleted in baseline check. |
| DescribeRiskWhiteList | Obtains the whitelist of risk items that are exempt from the baseline check. |
| BatchDeleteWhiteList | Deletes multiple risks from the whitelist for baseline check. |
| CreateUserWhiteList | Adds a specified risk to the baseline check whitelist. |
| DescribeStratety | Queries the execution details of a specified baseline check policy. |
| DescribeStrategyExecDetail | Queries the execution details of a baseline check policy. |
| DescribeRiskType | Queries all types of risks detected in baseline check and view the number of risks that have been detected by a baseline check policy or on the specified servers for a specific risk type. |
| Describesummary | Queries the risks detected in baseline check by risk type. |
| OperateWarning | Handles the risk alert records detected during the baseline check. |
| ExportWarning | Exports risks that match the specified criteria from baseline check. |

| Operation | Description |
|---|---|
| DescribeExportInfo | Queries export task information, including the export progress and the download link of the exported file. |

Unusual logon detection operations

| Operation | Description |
|---|---|
| DescribeBaseConfigs | Queries the logon security settings. |
| ModifyBaseConfig | Modifies logon security settings. |
| DeleteBaseConfig | Deletes a logon security setting, such as an approved logon location or IP address. |
| DescribeSwitchConfigs | Queries the logon security configuration records in the logon security settings. |
| ModifySwitchConfig | Modifies the setting about whether to enable a logon security configuration record to identify a valid logon to a host in the logon security settings. |
| DescribeConfigTarget | Queries the information about host assets to which a specified logon security configuration record applies. |

Webshell detection operations

| Operation | Description |
|---|---|
| DescribeWebPath | Queries the Web directories defined in webshell settings. |
| ModifyWebPath | Modifies the Web directory in webshell settings. |
| DescribeCategoryCount | Queries the number of webshells detected by Server Guard. |
| DescribeWebshell | Queries records of webshell files that have been detected by Server Guard, including the detection time and webshell file path. |
| OperateTrojan | Handles the detected webshells. |
| DescribeQuaraFile | Obtains a list of quarantined files. |
| RollbackQuaraFile | Restores a quarantined file. |

Suspicious server detection operations

| Operation | Description |
|---|---|
| DescribeSuspEventTypes | Queries the unusual event types. |
| DescribeSuspTrendStatistics | Queries the chart data on different types of unusual server events on each day. |
| OperateSuspiciousEvent | Handles detected unusual events. |
| OperateLoginLog | Labels a detected unusual logon event as handled. |
| CreateSuspiciousExport | Exports the information about server unusual events based on search conditions. |
| DescribeSuspiciousExportInfo | Queries an unusual event export task. |

Server log retrieval operations

| Operation | Description |
|---|---|
| CreateLogQuery | Creates or saves server log search conditions. |
| DescribeLogQuery | Queries the saved server log search conditions. |
| DeleteLogQuery | Deletes the saved server log search conditions. |
| DescribeFilterFields | Queries the filter fields of a specified server log search condition. |
| DescribeHistogram | Obtains the statistics on server logs generated within a specified time frame. |
| DescribeLogInfo | Queries the host log fields based on specified query conditions. |
| DescribeLogItems | Queries the server log details that are returned by a query. |

### 4.2 Make API requests

#### 4.2.1 Request structure

Apsara Stack Security API is based on Remote Procedure Call (RPC). This topic describes the structure of the API requests. You can send an HTTP request to call an API operation. The URL of the request must be in the following format:

```
http://endpoint/?Action=xx&parameters
```

Where:

|   | endpoint |   | : the endpoint used t |
|---|---|---|---|
| aegis.[ RegionId].example.com |   |   |   |
|   | Action | : the operation that yo |   |

`endpoint` : the endpoint used to call a cloud service. The endpoint for the Server Guard service is For example, you can set this parameter to DescribeFeatures to query the deployed Apsara Stack Security features. `parameters` : the request parameters. Request parameters include common request parameters and custom request parameters. Request parameters must be separated with ampersands (&). Common request parameters include information such as the API version and authentication information. For more information about the custom request parameters, see the corresponding operation description. Call the DescribeFeatures operation to query the deployed Apsara Stack Security features.

```
https://yundunprivate.[ RegionId].example.com/?Action=DescribeFeatures&AccessKeyId=key-test &Format=JSON&SecureTransport=true&SignatureMethod=HMAC-SHA1&SignatureNonce=15215528852396&S ignatureVersion=1.0&SourceIp=1xxxx6&Timestamp=2018-03-02Txxxxxxx&Version=2018-01-16&Signatu re=xxxx%xxxx%3D
```

API requests are presented in the following easy-to-read format in this document:

```
https://yundunprivate.[ RegionId].example.com/?Action=DescribeFeatures &Format=JSON &Version=2018-01-16 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2012-06-01T12:00:00Z
```

#### 4.2.2 Signature mechanism

Apsara Stack Security authenticates each access request. You need to include a signature for the submitted HTTP or HTTPS request. API authorization To ensure the security of your account, we recommend that you use a Resource Access Management (RAM) user to call API operations. Before using a RAM user to call an API operation, you must grant the RAM user the corresponding permission to call the API by creating an authorization policy and attaching the policy to the RAM user. API signature To ensure secure calls to the API, Alibaba Cloud authenticates each API request through the signature. When you manually make an API request, you need to use AccessKey Secret to calculate the signature, that is, the hash-based message authentication code (HMAC) value, based on the encoded and sorted request string. For more information, see the definition in RFC 2104. This topic uses the raw access parameters in the following table to describe how to create an API signature.

| Parameter | Description |
|---|---|
| Access point | http://semawaf.[ RegionId].example.com/? |
| API-specific parameters | Action=DescribeFeatures |
| Common parameters (excluding the Signature parameter) | &Timestamp=2016-02-23T12:46:24Z &Format=JSON &AccessKeyId=<yourAccessKeyId> &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2018-01-16 &SignatureVersion=1.0 |
| AccessKey secret | <yourAccessKeySecret> |

1. Use the request parameters to construct a canonicalized query string.
Not e The request parameters include common request parameters (excluding the Signature parameter) and API-specific parameters. i. Sort the parameters. Sort the request parameters in alphabetical order. ii. Encode the parameters. Use UTF-8 to URL-encode the parameter names and values. The encoding rules are as follows: Letters, digits, hyphens (-), underscores (_), periods (.), and tildes (~) are not encoded. Other characters are encoded in the %XY format, where XY is the hexadecimal representation of the character in ASCII. For example, the double quotation mark (") is encoded as %22. Extended UTF-8 characters are encoded in the %XY%ZA… format. Note that a space is encoded as %20, instead of a plus sign (+). iii. Connect the encoded parameter names and values with equal signs (=). iv. Then, sort the parameter name and value pairs connected by equal signs in alphabetical order, and connect them with ampersands (&) to produce the canonicalized query string.
2. Use the canonicalized query string to construct the string for signature calculation based on the
following rules:

```
StringToSign=HTTPMethod + “&” + percentEncode(“/”) + ”&” + percentEncode(CanonicalizedQueryString)
```

3. Calculate the HMAC value of the StringToSign string according to the definition in RFC 2104.
Not e The key used for signature calculation is your AccessKey secret adding the ampersand (&) (ASCII 38). Secure Hash Algorithm 1 (SHA1) is used as the hash algorithm.
4. Encode the preceding HMAC value into a string based on Base64 encoding rules to obtain the
signature value.

```
LEW8N4y7Uasop******
```

5. Set the Signature parameter in the request parameters to this signature value to sign the request.

#### 4.2.3 Common request parameters

The following table describes the common request parameters that are used to indicate information such as the API version and authentication information.

| Name | Type | Required | Description |
|---|---|---|---|
| Version | String | Yes | The API version in the format of YYYY- MM-DD. Set the value to 2016-11-11. |
| AccessKeyId | String | Yes | The key ID that Alibaba Cloud assigns to a user for service access. |
| Signature | String | Yes | The signature string. |
| SignatureMethod | String | Yes | The signature method. Set the value to HMAC-SHA1. |
| Timestamp | String | Yes | The timestamp of the request. Follow the ISO 8601 standard to specify the date and use the offset from Coordinated Universal Time (UTC) to specify the time zone. The format is YYYY-MM- DDThh:mm:ssZ . For example, 2014-05-26T12:00:00Z indicates 20:00:00 on May 26, 2014, Beijing time. |
| SignatureVersion | String | Yes | The signature algorithm version. Set the value to 1.0. |

|   |   | YYYY-MM- |
|---|---|---|
|   | DDThh:mm:ssZ |   |

| psara Stack Security |   |   | Developer Guide·Server Guar |
|---|---|---|---|
| Name | Type | Required | Description |
| SignatureNonce | String | Yes | The unique random number used to prevent network replay attacks. You must use different random numbers for different requests. |
| ResourceOwnerAc count | String | No | The owner account of the resource to be accessed through this API request, that is, the logon username. |
| Format | String | No | The format of the response. Set the value to JSON or XML. Not e Default value: XML. |

#### 4.2.4 Response structure

Apsara Stack Security API responses support both the XML and JSON formats. The system always returns a unique identification code RequestId each time you send a request to call an operation, no matter whether the call is successful or not. Sample responses (XML format)

```xml
<? xml version="1.0" encoding="UTF-8"? > <! -- The root node of the result --> <Operation name+Response>
    <! -- Returned request ID -->
    <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
    <! -- Returned data -->
</Operation name+Response>
```

Sample responses (JSON format)

```json
"RequestId": "4C467B38-3910-447D-87BC-AC049166F216", /* Returned data */
```

### 4.3 Asset management

#### 4.3.1 CreateGroup

You can call this operation to create an asset group.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateGroup. |
| GroupFather | Long | Yes | The parent asset group ID. |
| GroupFlag | Integer | Yes | The asset group type. Valid values: 0: indicates a default group. 1: indicates a custom group. |
| GroupIndex | Integer | Yes | The sequence number of the asset group. |
| GroupName | String | Yes | The name of the asset group. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=CreateGroup &GroupFather=0 &GroupFlag=1 &GroupIndex=1 &GroupName=Web group
```

Sample responses (JSON format)

```json
 "RequestId":"415AE1FC-3C11-4AA9-A06F-DE13D3430366"
```

#### 4.3.2 DescribeGroupSummary

You can call this operation to obtain a list of asset groups.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeGroupSummary. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Count | Integer | The number of asset groups. |
| Groups | List | The information about asset groups. For more information, see the following parameter descriptions. |
| GroupId | Long | The asset group ID. |
| GroupIndex | Integer | The sequence number of the asset group. |
| GroupLevel | Integer | The level of the asset group. |
| GroupName | String | The name of the asset group. |
| GroupFather | Integer | The ID of the parent asset group. |
| GroupFlag | Integer | The type of the asset group. Valid values: 1: indicates a non-leaf node group that contains child asset groups. 0: indicates a leaf node group. |
| MachineNum | Integer | The number of ECS instances contained in the group. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeGroupSummary
```

Sample responses (JSON format)

```json
 "Groups":[
   "GroupFlag":1,
   "GroupName":"Test group 21",
   "GroupIndex":1,
   "MachineNum":0,
   "GroupId":346
```

`},`

```json
   "GroupFlag":1,
   "GroupName":"Test group 1",
   "GroupIndex":2,
   "MachineNum":0,
   "GroupId":343
```

`},`

```json
   "GroupFlag":1,
   "GroupName":"Test group 2",
   "GroupIndex":3,
   "MachineNum":0,
   "GroupId":345
```

`},`

```json
   "GroupFlag":0,
   "GroupName":"Not grouped",
   "GroupIndex":100,
   "MachineNum":1,
   "GroupId":336
```

`],`

```json
 "Count":4,
 "RequestId":"B9FB5483-3CA6-4520-9F89-068ED6AAC6EE"
```

#### 4.3.3 DescribeGroupStruct

You can call this operation to query the asset group structure.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeGroupStruct. |
| Mark | String | No | The IP address or instance name of the server. |

| A | psara Stack Security |   |   | Developer Guide·Server Guar | d |
|---|---|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| TagIdList | String | No | The server tag ID. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| GroupFather | Integer | The ID of the parent asset group. |
| GroupId | Long | The ID of the asset group. |
| Groups | List | The asset groups. For more information, see the following descriptions. |
| GroupId | Long | The ID of the asset group. |
| GroupIndex | Integer | The sequence number of the asset group. |
| GroupLevel | Integer | The level of the asset group. |
| GroupName | String | The name of the asset group. |
| GroupFather | Integer | The ID of the parent asset group. |
| GroupFlag | Integer | The type of the asset group. Valid values: 1: indicates a non-leaf node group that contains child asset groups. 0: indicates a leaf node group. |
| ChildGroups | List | The child asset groups. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribeGroupStruct &remark=x.x.x.x &tagIdList=123
```

Sample response (JSON format)

```json
    "Groups":[
            "groupIndex":2,
            "groupFather":0,
            "groupId":343,
            "groupName":"****",
            "groupLevel":1,
            "groupFlag":1,
            "childGroups":[]
```

`},`

```json
            "groupIndex":3,
            "groupFather":0,
            "groupId":345,
            "groupName":"****",
            "groupLevel":1,
            "groupFlag":1,
            "childGroups":[
                    "groupIndex":1,
                    "groupFather":345,
                    "groupId":346,
                    "groupName":"****",
                    "groupLevel":2,
                    "groupFlag":1,
                    "childGroups":[]
```

`]` `},`

```json
            "groupIndex":100,
            "groupFather":0,
            "groupId":336,
            "groupName":"****",
            "groupFlag":0,
            "childGroups":[]
```

`],`

```json
    "RequestId":"C4490A16-DDE4-4351-A366-57F9FCDC188F",
    "GroupFather":0,
    "GroupId":0
```

#### 4.3.4 DeleteGroup

You can call this operation to delete a specified asset group.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteGroup. |
| GroupFlag | Integer | Yes | The type of the asset group. Valid values: 0: indicates a default group. 1: indicates a custom group. |
| GroupId | Long | Yes | The ID of the asset group. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DeleteGroup &GroupFlag=1 &GroupId=123
```

Sample responses (JSON format)

```json
 "RequestId":"415AE1FC-3C11-4AA9-A06F-DE13D3430366"
```

#### 4.3.5 DescribeAllTag

You can call this operation to query the tag information of all servers.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeAllTag. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| EntityList | Array | The tag information of all servers. For more information, see the following parameter descriptions. |
| AliUid | Long | The Alibaba Cloud account ID. |
| GmtCreate | Long | The creation time of the asset tag. |
| GmtModified | Long | The last modification time of the asset tag. |
| Id | Long | The ID of the asset tag. |
| TagName | String | The name of the asset tag. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeAllTag
```

Sample responses (JSON format)

```json
 "RequestId":"09D7C349-5306-4335-849A-10916F89E769",
 "EntityList":[
   "AliUid":"123",
   "GmtCreate":"1508897933000",
   "GmtModified":"1508897933000",
   "Id":"1",
   "TagName":"test"
```

`},` `]`

#### 4.3.6 DescribeBetachTag

You can call this operation to query the tag information of a specified server.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeBetachTag. |
| UuidList | String | No | The UUID of the server. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TagInfoList | Array | The tag information of the specified server. For more information, see the following parameter descriptions. |
| AliUid | Long | The Alibaba Cloud account ID. |
| GmtCreate | Long | The creation time of the asset tag. |
| GmtModified | Long | The last modification time of the asset tag. |
| Id | Long | The ID of the asset tag. |
| TagName | String | The name of the asset tag. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeBetachTag &UuidList=inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818
```

Sample responses (JSON format)

```json
 "RequestId":"09D7C349-5306-4335-849A-10916F89E769",
 "EntityList":[
   "AliUid":"123",
   "GmtCreate":"1508897933000",
   "GmtModified":"1508897933000",
   "Id":"1",
   "TagName":"test"
```

`},` `]`

#### 4.3.7 ModifyBetachTag

You can call this operation to modify the tags of multiple specified servers.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyBetachTag. |
| TagList | String | Yes | The server tag. Separate multiple tags with commas (,). |
| UuidList | String | Yes | The UUID of the server. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=ModifyBetachTag &UuidList=inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818 &TagList=test,test2
```

Sample responses (JSON format)

```json
 "RequestId":"09D7C349-5306-4335-849A-10916F89E769",
```

#### 4.3.8 DeleteTag

You can call this operation to delete a server tag.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteTag. |
| Id | Long | No | The ID of the server tag. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DeleteTag &Id=123
```

Sample responses (JSON format)

```json
 "RequestId":"415AE1FC-3C11-4AA9-A06F-DE13D3430366"
```

#### 4.3.9 DescribeAllEntity

You can call this operation to query information about all servers.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeAllEntity. |
| GroupId | Long | No | The ID of the asset group. |
| Os | String | No | The operating system of the server. Valid values: win: indicates the Windows operating system. linux: indicates the Linux operating system. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Count | Integer | The number of returned records. |
| EntityList | Array | The servers. For more information, see the following descriptions. |
| GroupId | Integer | The ID of the asset group. |
| Uuid | String | The universally unique identifier (UUID) of the server. |
| InstanceName | String | The instance name of the server. |
| Ip | String | The IP address of the server. Not e The public IP address of the server is displayed preferentially. If no public IP address is assigned to the server, the private IP address of the server is displayed. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribeAllEntity &GroupId=123 &Os=win
```

Sample response (JSON format)

```json
    "Count":2,
    "RequestId":"09D7C349-5306-4335-849A-10916F89E769",
    "EntityList":[
            "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
            "Ip":"x.x.x.x",
            "GroupId":336,
            "InstanceName":"****"
```

`},`

```
        ......
```

`]`

#### 4.3.10 DescribeEntityList

You can call this operation to query servers of a specified type. For example, you can query servers by security event type.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeEntityList. |
| PageSize | Integer | No | The number of records to return on each page. Default value: 20. |
| CurrentPage | Integer | No | The number of the page to return. Default value: 1. |
| RegionNo | String | No | The ID of the region. |
| GroupId | Long | No | The ID of the asset group. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| Os | String | No | The operating system of the server. Valid values: win: indicates the Windows operating system. linux: indicates the Linux operating system. |
| Account | String | No | Queries servers with unusual logons detected. Set this parameter to remoteLogin. |
| Health | String | No | Queries servers with baseline check issues detected. Set this parameter to exception. |
| Patch | String | No | Queries servers with vulnerabilities detected. Set this parameter to vul. |
| Suspicious | String | No | Queries servers with unusual events detected. Set this parameter to exception. |
| Trojan | String | No | Queries servers with webshells detected. Valid values: webshell: indicates trojan files. process: indicates trojan processes. |
| Status | String | No | The status of the Server Guard Agent. Valid values: offline: indicates that the Server Guard Agent is offline. pause: indicates that the Server Guard Agent is disabled. |
| TagIdList | String | No | The server tag ID. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |

| psara Stack Security |   | Developer Guide·Server Guar |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| TotalCount | Integer | The number of returned records. |
| EntityList | Array | The servers. For more information, see the following descriptions. |
| AegisOnline | Boolean | Indicates whether the Server Guard Agent is online. |
| AegisVersion | String | The version of the Server Guard Agent. |
| BuyVersion | String | The version of the Server Guard package. |
| GroupId | Integer | The ID of the asset group. |
| ClientStatus | Boolean | Indicates whether the server is protected. A value of false indicates that the protection for the server is paused. |
| Flag | Integer | The type of the server. Valid values: 0: indicates an Alibaba Cloud ECS instance. 1: indicates an external server. |
| Uuid | String | The universally unique identifier (UUID) of the server. |
| InstanceName | String | The instance name of the server. |
| Os | String | The type of the operating system. |
| Region | String | The ID of the region. |
| Ip | String | The IP address of the server. Not e The public IP address of the server is displayed preferentially. If no public IP address is assigned to the server, the private IP address of the server is displayed. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribeEntityList &Account=remoteLogin &CurrentPage=1 &GroupId=1 &Health=exception &Os=windows &PageSize=20 &Patch=vul &RegionNo=**** &Remark=x.x.x.x &Status=offline &Suspicious=exception &TagIdList=1,2,3 &Trojan=webshell
```

Sample response (JSON format)

```json
    "TotalCount":1,
    "PageSize":1,
    "RequestId":"8BFB5273-6582-446A-9E0B-BAC0A1A468EA",
    "CurrentPage":1,
    "EntityList":[
            "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
            "Os":"linux",
            "ClientStatus":false,
            "Ip":"x.x.x.x",
            "Region":"****",
            "Flag":0,
            "BuyVersion":"4",
            "GroupId":336,
            "InstanceName":"****"
```

`]`

#### 4.3.11 ModifyEntityGroup

You can call this operation to modify the asset group information for a specified server.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyEntityGroup. |

| psara Stack Security |   |   | Developer Guide·Server Guar |
|---|---|---|---|
| Name | Type | Required | Description |

| GroupId | Long | No | The modified asset group ID. |
|---|---|---|---|
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=ModifyEntityGroup &GroupId=11 &Uuids=inet-db626549-870c-4d3e-b0b5-4d8a5c7268a6,inet-db626549-870c-4d3e-b0b5-4d8a5c7268a
```

Sample responses (JSON format)

```json
 "RequestId":"C4490A16-DDE4-4351-A366-57F9FCDC188F",
```

#### 4.3.12 DescribeMachines

You can call this operation to query servers that match the specified criteria. For example, you can query all servers in an asset group.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeMachines. |

| D | eveloper Guide·Serve | r Guard |   | Apsara Stack Securit | y |
|---|---|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| GroupId | Long | No | The ID of the asset group. |
| TagIdList | String | No | The server tag ID. |
| Mark | String | No | The IP address or instance name of the server. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Count | Integer | The number of returned records. |
| Machines | Array | The servers. For more information, see the following descriptions. |
| GroupId | Integer | The ID of the asset group. |
| InstanceName | String | The instance name of the server. |
| Os | String | The type of the operating system. |
| Ip | String | The IP address of the server. Not e The public IP address of the server is displayed preferentially. If no public IP address is assigned to the server, the private IP address of the server is displayed. |
| Uuid | String | The universally unique identifier (UUID) of the server. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribeMachines &GroupId=123
```

Sample response (JSON format)

```json
    "Count":1,
    "Machines":[
            "groupId":336,
            "os":"linux",
            "instanceName":"****",
            "uuid":"inet-db626549-870c-4d3e-b0b5-4d8a5c7268a6",
            "ip":"192.168.x.x"
```

`],`

```json
    "RequestId":"C984123D-C8E0-4974-9CEE-ADD0596C46DB"
```

#### 4.3.13 DescribeMachineDetail

You can call this operation to query the detailed information about a specified server.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeMachineDetail. |
| Uuid | String | No | The universally unique identifier (UUID) of the server. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| MachineDetail | Array | The detailed information about the server. For more information, see the following descriptions. |
| AegisOnline | Boolean | Indicates whether the Server Guard Agent is online. |
| AegisVersion | String | The version of the Server Guard Agent. |
| BuyVersion | String | The version of the Server Guard package. |
| GroupId | Integer | The ID of the asset group. |

| Parameter | Type | Description |
|---|---|---|
| ClientStatus | Boolean | Indicates whether the server is protected. A value of false indicates that the protection for the server is paused. |
| Flag | Integer | The type of the server. Valid values: 0: indicates an Alibaba Cloud ECS instance. 1: indicates an external server. |
| GroupId | Long | The ID of the asset group. |
| GroupTrace | String | The full path of the asset group. |
| InstanceId | String | The instance ID of the server. |
| InstanceName | String | The instance name of the server. |
| Os | String | The type of the operating system. |
| Region | String | The ID of the region. |
| Ip | String | The IP address of the server. Not e The public IP address of the server is displayed preferentially. If no public IP address is assigned to the server, the private IP address of the server is displayed. |
| IntranetIp | String | The private IP address of the server. |
| Uuid | String | The UUID of the server. |
| Tag | String | The server tag ID. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribeMachineDetail &Uuid=6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac
```

Sample response (JSON format)

```json
    "RequestId":"5D5D6F8F-6986-4996-9321-8EEA9FC048D1",
    "MachineDetail":{
        "Uuid":"inet-db626549-870c-4d3e-b0b5-4d8a5c7268a6",
        "Ip":"192.168.x.x",
        "GroupTrace":"Not grouped",
        "Os":"linux",
        "ClientStatus":true,
        "Region":"outside-of-aliyun",
        "Tag":"",
        "AegisOnline":false,
        "InstanceName":"****"
```

#### 4.3.14 DescribePropertyScheduleConfig

You can call this operation to query the update cycle of server information.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribePropertyScheduleConfig. |
| Type | String | No | The type of the server information. Valid values: scheduleraccount period: indicates _ _ the user information. schedulerport period: indicates the _ _ port information. schedulerprocess period: indicates _ _ the process information. schedulersoftwareperiod: indicates _ _ the application software information. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Config | String | The update cycle in hours. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertyScheduleConfig &Type=scheduler_account_period
```

Sample responses (JSON format)

```json
 "RequestId":"C528C153-33E6-4CF5-8C90-A2E6FFD6191C",
 "Config": "2"
```

#### 4.3.15 ModifyPropertyScheduleConfig

You can call this operation to modify the synchronization cycle of server information.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyPropertyScheduleConfig. |
| Type | String | Yes | The type of asset information whose synchronization cycle is to be modified. Valid values: schedulersoftwareperiod: indicates _ _ the synchronization cycle of application software information. scheduleraccount period: indicates _ _ the synchronization cycle of user account information. schedulerport period: indicates the _ _ synchronization cycle of port information. schedulerprocess period: indicates _ _ the synchronization cycle of process information. |
| ScheduleTime | String | Yes | The new synchronization cycle. Unit: hours. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| ModifyResult | Boolean | Indicates whether the modification is successful. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=ModifyPropertyScheduleConfig &Type=scheduler_software_period &ScheduleTime=24
```

Sample responses (JSON format)

```json
 "ModifyResult":true,
 "RequestId":"2932CB78-51FB-459C-A3E8-76BE2968069A"
```

#### 4.3.16 DescribePropertyStatistic

You can call this operation to query the server statistics.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribePropertyStatistic. |
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

| eveloper Guide·Server Gua | rd | Apsara Stack Securit |
|---|---|---|

| Name | Type | Description |
|---|---|---|
| PropertyStatistics | Array | The list of server statistics. For more information, see the following parameter descriptions. |
| PortCount | String | The number of enabled ports. |
| PortGetDate | String | The port information update time. |
| ProcCount | String | The number of running processes. |
| ProcGetDate | String | The process information update time. |
| RootUserCount | String | The number of user accounts with root permission. |
| UserCount | String | The total number of user accounts. |
| UserGetDate | String | The user account information update time. |
| Uuid | String | The UUID of the server. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertyStatistic &Uuids=inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818
```

Sample responses (JSON format)

```json
 "PropertyStatistics":[
   "UserGetDate":1514373155000,
   "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
   "RootUserCount":1,
   "UserCount":33,
   "ProcCount":89,
   "PortGetDate":1514115614000,
   "PortCount":6,
   "ProcGetDate":1514373133000
```

`],`

```json
 "RequestId":"C1CACE7E-E868-4E44-A52E-4CB1463B62BB"
```

#### 4.3.17 DescribePropertyPortItem

p You can call this operation to obtain a list of listener ports on hosts.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribePropertyPortItem. |
| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query output. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |
| Port | String | No | The port number. |
| ProcName | String | No | The process name. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of returned records. |
| Count | Integer | The number of records on the current page. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| PropertyPortItems | Array | The list of listener ports on hosts. For more information, see the following parameter descriptions. |
| Count | Integer | The number of hosts that have enabled the specified port. |
| Port | String | The port number. |
| Proto | String | The network protocol, such as TCP or UDP. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertyPortItem &Port=22
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "PageSize":20,
 "RequestId":"9D38986A-F145-4FA8-AE1C-1DB1C2BDF4C0",
 "CurrentPage":1,
 "PropertyPortItems":[
   "Proto":"tcp",
   "Port":"22",
   "Count":2
```

`],`

```json
 "Count":1
```

#### 4.3.18 DescribePropertyPortDetail

You can call this operation to query detailed information about a listening port.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribePropertyPortDetail. |
| PageSize | Integer | No | The number of records to return on each page. Default value: 20. |
| CurrentPage | Integer | No | The number of the page to return. Default value: 1. |
| GroupId | Long | No | The ID of the asset group. |
| Ip | String | No | The IP address of the server. |

| psara Stack Security |   |   | Developer Guide·Server Guar |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| Port | String | No | The port number. |
| Extend | String | No | Indicates whether fuzzy match is enabled to search for port numbers. Valid values: 1: indicates that fuzzy match is enabled. 0: indicates that fuzzy match is disabled. |
| ProcName | String | No | The name of the process. |
| Mark | String | No | The IP address or instance name of the server. Not e Fuzzy match is supported. |
| TagIdListString | String | No | The server tag ID. |
| Uuid | String | No | The universally unique identifier (UUID) of the server. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The number of returned records. |
| Count | Integer | The number of records returned on the current page. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| PropertyPorts | Array | The information about the listening port. For more information, see the following descriptions. |
| BindIp | String | The IP address bound to the port. |
| Create | String | The time when the port was enabled. |
| InstanceName | String | The instance name of the server. |
| Ip | String | The IP address of the server. |

| Developer Guide·Server Gua | rd | Apsara Stack Securit |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| Port | String | The port number. |
| ProcName | String | The name of the process. |
| Proto | String | The network protocol, such as TCP and UDP. |
| Uuid | String | The UUID of the server. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertyPortDetail &Uuid=inet-f6ac9a93-0818-4052-90e2-d24f18ee198b
```

Sample response (JSON format)

```json
    "TotalCount":1,
    "PageSize":20,
    "RequestId":"D85484BB-4DC2-44EC-AD67-0B3765EC9213",
    "CurrentPage":1,
    "PropertyPorts":[
            "InstanceName":"****",
            "Uuid":"inet-f6ac9a93-0818-4052-90e2-d24f18ee198b",
            "Proto":"tcp",
            "Create":1514373168000,
            "Ip":"x.x.x.x",
            "Port":"22",
            "ProcName":"sshd",
            "BindIp":"0.0.0.0"
```

`],`

```json
    "Count":1
```

#### 4.3.19 DescribePropertyPortDiff

You can call this operation to query listening port changes.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribePropertyPortDiff. |
| PageSize | Integer | No | The number of records to return on each page. Default value: 20. |
| CurrentPage | Integer | No | The number of the page to return. Default value: 1. |
| DiffStatus | String | No | The type of the listening port change. Valid values: start: indicates that the listening port is enabled. stop: indicates that the listening port is disabled. |
| Ip | String | No | The IP address of the server. |
| Port | String | No | The port number. |
| Extend | String | No | Indicates whether fuzzy match is enabled to search for port numbers. Valid values: 1: indicates that fuzzy match is enabled. 0: indicates that fuzzy match is disabled. |
| ProcName | String | No | The name of the process. |
| Mark | String | No | The IP address or instance name of the server. Not e Fuzzy match is supported. |
| TagIdListString | String | No | The server tag ID. |
| Uuid | String | No | The universally unique identifier (UUID) of the server. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The number of returned records. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| PropertyPortDiffs | Array | The listening port changes. For more information, see the following descriptions. |
| BindIp | String | The IP address bound to the port. |
| Create | String | The time when the port was enabled. |
| DiffKeyList | String | The port fields that have been changed, including Proto, ProcName, and BindIp. |
| DiffStatus | String | The type of the listening port change. Valid values: start: indicates that the listening port is enabled. stop: indicates that the listening port is disabled. |
| InstanceName | String | The instance name of the server. |
| Ip | String | The IP address of the server. |
| ProcName | String | The name of the process. |
| Port | String | The port number. |
| Proto | String | The network protocol, such as TCP and UDP. |
| Uuid | String | The UUID of the server. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertyPortDiff &Uuid=inet-f6ac9a93-0818-4052-90e2-d24f18ee198b
```

Sample response (JSON format)

```json
    "TotalCount":1,
    "PageSize":20,
    "RequestId":"AFC431E3-F8E3-4652-91CB-9FF4053F282A",
    "CurrentPage":1,
    "PropertyPortDiffs":[
            "InstanceName":"****",
            "Uuid":"inet-f6ac9a93-0818-4052-90e2-d24f18ee198b",
            "Proto":"tcp",
            "Create":1514366856000,
            "Ip":"x.x.x.x",
            "Port":"22",
            "ProcName":"sshd",
            "DiffKeyList":"proto,procName,bindIp",
            "DiffStatus":"stop",
            "BindIp":"0.0.0.0"
```

`]`

#### 4.3.20 DescribePropertyProcItem

You can call this operation to obtain a list of server processes.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribePropertyProcItem. |
| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query output. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |
| Name | String | No | The process name. |
| User | String | No | The user who started the process. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of returned records. |
| Count | Integer | The number of records on the current page. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| PropertyProcItems | Array | The list of server processes. For more information, see the following parameter descriptions. |
| Count | Integer | The number of servers on which the process is running. |
| Name | String | The process name. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertyProcItem &Name=init
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "PropertyProcItems":[
   "Count":2,
   "Name":"init"
```

`],`

```json
 "PageSize":20,
 "RequestId":"8BE95FB1-66B7-4509-AF82-3AA67368A5D8",
 "CurrentPage":1,
 "Count":1
```

#### 4.3.21 DescribePropertyProcDetail

You can call this operation to query server process details.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribePropertyProcDetail. |
| PageSize | Integer | No | The number of records to return on each page. Default value: 20. |
| CurrentPage | Integer | No | The number of the page to return. Default value: 1. |
| GroupId | Long | No | The ID of the asset group. |
| Ip | String | No | The IP address of the server. |
| Name | String | No | The name of the process. |
| Extend | String | No | Indicates whether fuzzy match is enabled to search for process names. Valid values: 1: indicates that fuzzy match is enabled. 0: indicates that fuzzy match is disabled. |
| User | String | No | The user who started the process. |
| Mark | String | No | The IP address or instance name of the server. Not e Fuzzy match is supported. |
| Cmdline | String | No | The process parameter. |
| TagIdListString | String | No | The server tag ID. |
| Uuid | String | No | The universally unique identifier (UUID) of the server. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The number of returned records. |
| Count | Integer | The number of records returned on the current page. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| PropertyProcs | Array | The details of the server process. For more information, see the following descriptions. |
| Cmdline | String | The process parameter. |
| Create | String | The time when the information was reported. |
| EuidName | String | The permissions that the process has to access resources and files. |
| InstanceName | String | The instance name of the server. |
| Md5 | String | The MD5 value of the executable file. |
| Name | String | The name of the process. |
| Path | String | The path of the process. |
| Pid | String | The ID of the process. |
| ProcName | String | The name of the process. |
| Pname | String | The name of the parent process. |
| StartTime | String | The time when the process was started. |
| User | String | The user who started the process. |
| Uuid | String | The UUID of the server. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertyProcDetail &Uuid=inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818
```

Sample response (JSON format)

```json
    "PropertyProcs":[
            "InstanceName":"****",
            "Path":"/sbin/init",
            "Pname":"N/A",
            "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
            "User":"root",
            "Create":1514373133000,
            "StartTime":"2017-12-26 22:34:45",
            "Pid":"1",
            "EuidName":"root",
            "Cmdline":"/sbin/init",
            "Name":"init",
            "Md5":"70023aaf3f480d198d3b078d8c39****"
```

`],`

```json
    "TotalCount":1,
    "PageSize":20,
    "RequestId":"AB20A6D4-43EB-44E2-AD64-E03EAC1C14D9",
    "CurrentPage":1,
    "Count":1
```

#### 4.3.22 DescribePropertyProcDiff

You can call this operation to query process changes of a server.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribePropertyProcDiff. |
| PageSize | Integer | No | The number of records to return on each page. Default value: 20. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| CurrentPage | Integer | No | The number of the page to return. Default value: 1. |
| DiffStatus | String | No | The type of the process change. Valid values: start: indicates that the process is started. stop: indicates that the process is stopped. |
| Ip | String | No | The IP address of the server. |
| Name | String | No | The name of the process. |
| User | String | No | The user who started the process. |
| Mark | String | No | The IP address or instance name of the server. Not e Fuzzy match is supported. |
| Uuid | String | No | The universally unique identifier (UUID) of the server. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The number of returned records. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| PropertyProcDiffs | Array | The server process changes. For more information, see the following descriptions. |
| Cmdline | String | The process parameter. |
| Create | String | The time when the information was reported. |
| DiffKeyList | String | The names of the fields that have been changed. |
| DiffStatus | String | The type of the process change. |

| psara Stack Security |   | Developer Guide·Server Guar |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| EuidName | String | The permissions that the process has to access resources and files. |
| InstanceName | String | The instance name of the server. |
| Ip | String | The IP address of the server. |
| Md5 | String | The MD5 value of the executable file. |
| Name | String | The name of the process. |
| Path | String | The path of the process. |
| Pid | String | The ID of the process. |
| Pname | String | The name of the parent process. |
| StartTime | String | The time when the process was started. |
| Uuid | String | The UUID of the server. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertyProcDiff &Uuid=inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818
```

Sample response (JSON format)

```json
    "TotalCount":1,
    "PageSize":20,
    "RequestId":"D0951162-E933-4E2B-BDE2-B8FD806CEF9F",
    "CurrentPage":1,
    "PropertyProcDiffs":[
            "Pname":"N/A",
            "Ip":"x.x.x.x",
            "StartTime":"2017-12-26 22:34:45",
            "Pid":"1",
            "DiffKeyList":"startTime,path,user,pid,pname,md5,uid,cmdline,euidName",
            "DiffStatus":"start",
            "Name":"init",
            "InstanceName":"****",
            "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
            "Create":1514366744000,
            "Cmdline":"/sbin/init",
            "Euidname":"root",
            "Md5":"70023aaf3f480d198d3b078d8c39****"
```

`},` `]`

#### 4.3.23 DescribePropertySoftwareItem

You can call this operation to query servers that have been installed with the specified application.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribePropertySoftwareItem. |
| PageSize | Integer | No | The maximum number of records displayed on a page. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |
| Name | String | No | The name of the application. |
| Path | String | No | The application installation path. |

| A | psara Stack Security |   |   | Developer Guide·Server Guar | d |
|---|---|---|---|---|---|

| Name | Type | Required | Description |
|---|---|---|---|
| SoftwareVersion | String | No | The version of the application. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The number of returned records. |
| Count | Integer | The number of records on the current page. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| PropertySoftwareItems | Array | A list of servers that have been installed with the application. For more information, see the following parameter descriptions. |
| Count | Integer | The number of servers that have been installed with the application. |
| Name | String | The name of the application. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertySoftwareItem &Name=spice-vdagent
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "PropertySoftwareItems":[
   "count":2,
   "Name":"spice-vdagent"
```

`],`

```json
 "PageSize":20,
 "RequestId":"0F2A3DEA-A5B3-4C2A-8BFC-4724A205E28B",
 "CurrentPage":1,
 "count": 1,
```

#### 4.3.24 DescribePropertySoftwareDetail

You can call this operation to query the details of software installed on a server.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribePropertySoftwareDetail. |
| PageSize | Integer | No | The number of records to return on each page. Default value: 20. |
| CurrentPage | Integer | No | The number of the page to return. Default value: 1. |
| Ip | String | No | The IP address of the server. |
| Name | String | No | The name of the software. |
| Extend | String | No | Indicates whether fuzzy match is enabled to search for software names.. Valid values: 1: indicates that fuzzy match is enabled. 0: indicates that fuzzy match is disabled. |
| Path | String | No | The installation path of the software. |

| psara Stack Security |   |   | Developer Guide·Server Guar |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| Remark | String | No | The IP address or instance name of the server. Not e Fuzzy match is supported. |
| SoftwareVersion | String | No | The version of the software. |
| Uuid | String | No | The universally unique identifier (UUID) of the server. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The number of returned records. |
| Count | Integer | The number of records returned on the current page. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| PropertySoftwares | Array | The details of software installed on the server. For more information, see the following descriptions. |
| Create | String | The time when the information was reported. |
| InstallTime | String | The time when the software was installed. |
| InstanceName | String | The instance name of the server. |
| Ip | String | The IP address of the server. |
| Path | String | The installation path of the software. |
| Version | String | The version of the software. |
| Uuid | String | The UUID of the server. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertySoftwareDetail &Uuid=inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818
```

Sample response (JSON format)

```json
    "TotalCount":1,
    "PropertySoftwares":[
            "InstanceName":"****",
            "Path":"/usr/libexec/gvfs-gphoto2-volume-monitor",
            "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
            "InstallTime":"2016-06-29 06:55:22",
            "Version":"1.4.3",
            "Create":1514172615000,
            "Ip":"x.x.x.x"
```

`],`

```json
    "PageSize":20,
    "RequestId":"31409246-AB88-4B36-A2B8-16D21BA9E170",
    "CurrentPage":1,
    "Count":1
```

#### 4.3.25 DescribePropertySoftwareDiff

You can call this operation to query changes of applications that have been installed on servers.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribePropertySoftwareDiff. |
| PageSize | Integer | No | The maximum number of records displayed on a page. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |

| Name | Type | Required | Description |
|---|---|---|---|
| DiffStatus | String | No | The type of the application changes. Valid values: create: indicates an installation. delete: indicates an uninstallation. modified: indicates a modification. |
| Ip | String | No | The IP address of the server. |
| Name | String | No | The name of the application. |
| Path | String | No | The path where the application is installed. |
| SoftwareVersion | String | No | The version of the application. |
| Mark | String | No | The IP address or instance name of the server. Not e Fuzzy match is supported. |
| Uuid | String | No | The UUID of the server. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The number of returned records. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| PropertySoftwareDiffs | Array | The application changes. For more information, see the following parameter descriptions. |
| Create | String | The time when the application change was reported. |
| DiffKeyList | String | The name of the fields that have been changed. |
| DiffStatus | String | The type of the changes. |
| InstanceName | String | The instance name of the server. |

| Developer Guide·Server Gua | rd | Apsara Stack Securit |
|---|---|---|

| Name | Type | Description |
|---|---|---|
| Ip | String | The IP address of the server. |
| Name | String | The name of the application. |
| Path | String | The path where the application is installed. |
| Version | String | The version of the application. |
| Uuid | String | The UUID of the server. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertySoftwareDiff &Uuid=inet-f6ac9a93-0818-4052-90e2-d24f18ee198b
```

Sample responses (JSON format)

```json
 "TotalCount":1398,
 "PageSize":2,
 "RequestId":"3A0814BA-1A5D-43DC-A6E9-3B52EDD3700E",
 "CurrentPage":1,
 "PropertySoftwareDiffs":[
   "Path":"/etc/ghostscript",
   "Uuid":"inet-f6ac9a93-0818-4052-90e2-d24f18ee198b",
   "Version":"8.70",
   "Create":1514172428000,
   "DiffKeyList":"version,path",
   "DiffStatus":"create",
   "Name":"ghostscript"
```

`},`

```json
   "Path":"/usr/sbin/brctl",
   "Uuid":"inet-f6ac9a93-0818-4052-90e2-d24f18ee198b",
   "Version":"1.2",
   "Create":1514172428000,
   "DiffKeyList":"version,path",
   "DiffStatus":"create",
   "Name":"bridge-utils"
```

`]`

#### 4.3.26 DescribePropertyUserItem

You can call this operation to query user account information.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribePropertyUserItem. |
| PageSize | Integer | No | The maximum number of records displayed on a page. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |
| User | String | No | The username of the account. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The number of returned records. |
| Count | Integer | The number of records on the current page. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| PropertyUserItems | Array | The returned user account information. For more information, see the following parameter descriptions. |
| Count | Integer | The number of servers under the account. |
| Name | String | The username of the account. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertyUserItem
```

Sample responses (JSON format)

```json
 "TotalCount":2,
 "PropertyUserItems":[
   "User":"abrt",
   "Count": 2
```

`},`

```json
   "User":"adm",
   "Count": 2
```

`],`

```json
 "PageSize":20,
 "RequestId":"E80981C2-AD12-4C60-9976-6927C1FE449B",
 "CurrentPage":1,
 "Count": 2
```

#### 4.3.27 DescribePropertyUserDetail

You can call this operation to query user account details.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribePropertyUserDetail. |
| PageSize | Integer | No | The number of records to return on each page. Default value: 20. |
| CurrentPage | Integer | No | The number of the page to return. Default value: 1. |
| GroupId | Long | No | The ID of the asset group. |
| Ip | String | No | The IP address of the server. |

| psara Stack Security |   |   | Developer Guide·Server Guar |
|---|---|---|---|
| Parameter | Type | Required | Description |
| IsRoot | String | No | Indicates whether the user account is a root account. Valid values: 1: indicates yes. 0: indicates no. |
| User | String | No | The name of the user account. |
| Extend | String | No | Indicates whether fuzzy match is enabled to search for user accounts. Valid values: 1: indicates that fuzzy match is enabled. 0: indicates that fuzzy match is disabled. |
| Mark | String | No | The IP address or instance name of the server. Not e Fuzzy match is supported. |
| TagIdListString | String | No | The server tag ID. |
| Uuid | String | No | The universally unique identifier (UUID) of the server. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The number of returned records. |
| Count | Integer | The number of records returned on the current page. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| PropertyUsers | Array | The details of the user account. For more information, see the following descriptions. |
| AccountsExpirationDate | String | The time when the user account expires. |
| Create | String | The time when the information was reported. |

| eveloper Guide·Server Gua | rd | Apsara Stack Securit |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| GroupName | String | The information about the user group. |
| InstanceName | String | The instance name of the server. |
| Ip | String | The IP address of the server. |
| IsRoot | String | Indicates whether the user account is a root account. |
| LastLoginIp | String | The last IP address that is used by the user account to log on to the server. |
| LastLoginTime | String | The last logon time of the user account. |
| PasswordExpirationDate | String | The time when the password of the user account expires. |
| User | String | The name of the user account. |
| Uuid | String | The UUID of the server. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertyUserDetail &Uuid=inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818
```

Sample response (JSON format)

```json
    "TotalCount":66,
    "PageSize":2,
    "RequestId":"2EEAE2A6-1662-471C-A5E5-8A6190B01AFF",
    "CurrentPage":1,
    "Count":1,
    "PropertyUsers":[
            "GroupName":[
                "root"
```

`],`

```json
            "InstanceName":"****",
            "IsRoot":"1",
            "LastLoginTime":"2017-12-27 10:22:25",
            "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
            "User":"root",
            "LastLoginIp":"192.168.x.x",
            "Create":1514373155000,
            "Ip":"x.x.x.x",
            "AccountsExpirationDate":"never",
            "PasswordExpirationDate":"never"
```

`]`

#### 4.3.28 DescribePropertyUserDiff

You can call this operation to query user account changes.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribePropertyUserDiff. |
| PageSize | Integer | No | The number of records to return on each page. Default value: 20. |
| CurrentPage | Integer | No | The number of the page to return. Default value: 1. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| DiffStatus | String | No | The type of the user account change. Valid values: create: indicates that a new account has been added. delete: indicates that an account has been deleted. modified: indicates that an account has been modified. |
| IsRoot | String | No | Indicates whether the user account is a root account. Valid values: 1: indicates yes. 0: indicates no. |
| User | String | No | The name of the user account. |
| Mark | String | No | The IP address or instance name of the server. Not e Fuzzy match is supported. |
| Uuid | String | No | The universally unique identifier (UUID) of the server. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The number of returned records. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| PropertyUserDiffs | Array | The user account changes. For more information, see the following descriptions. |
| AccountsExpirationDate | String | The time when the user account expires. |
| Create | String | The time when the information was reported. |
| DiffKeyList | String | The names of the fields that have been changed. |
| DiffStatus | String | The type of the user account change. |

| A | psara Stack Security |   | Developer Guide·Server Guar | d |
|---|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| GroupName | String | The information about the user group. |
| InstanceName | String | The instance name of the server. |
| Ip | String | The IP address of the server. |
| IsRoot | String | Indicates whether the user account is a root account. |
| PasswordExpirationDate | String | The time when the password of the user account expires. |
| User | String | The name of the user account. |
| Uuid | String | The UUID of the server. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertyUserDiff &Uuid=inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818
```

Sample response (JSON format)

```json
    "TotalCount":1,
    "PageSize":20,
    "RequestId":"20903EB6-E695-44A4-85C2-B9DFE4376F1F",
    "CurrentPage":1,
    "PropertyUserDiffs":[
            "GroupName":[
                "root"
```

`],`

```json
            "InstanceName":"****",
            "IsRoot":"0",
            "User":"****",
            "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
            "Create":1514020942000,
            "Ip":"x.x.x.x",
            "AccountsExpirationDate":"never",
            "DiffKeyList":"isRoot,groupName,accountsExpirationDate,passwordExpirationDate
```

`",`

```json
            "DiffStatus":"create",
            "PasswordExpirationDate":"never"
```

`]`

#### 4.3.29 PushAllTask

You can call this operation to perform a quick security check on specified servers.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to PushAllTask. |
| Uuids | String | No | The universally unique identifier (UUID) of the server. Separate multiple UUIDs with commas (,). |

| Parameter | Type | Required | Description |
|---|---|---|---|
| Tasks | String | No | The type of the security check task. Valid values: OVALENTITY: indicates all security _ check tasks. CMS: indicates a check for CMS vulnerabilities. SYSVUL: indicates a check for system software vulnerabilities. HEALTHCHECK: indicates a baseline _ check. WEBSHELL: indicates a check for webshells. PROCSNAPSHOT: indicates a check on _ process data. PORT SNAPSHOT: indicates a check on _ port data. ACCOUNT SNAPSHOT: indicates a _ check on account data. SOFTWARESNAPSHOT: indicates a _ check on application data. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| PushTaskRsp | Struct | The task delivery result. For more information, see the following descriptions. |
| PushTaskResultList | Array | The tasks that fail to be delivered. For more information, see the following descriptions. |
| GroupId | String | The ID of the asset group. |
| InstanceId | String | The instance ID of the server. |
| InstanceName | String | The instance name of the server. |
| Ip | String | The IP address of the server. |
| Message | String | The details of the task delivery result. |
| Online | String | Indicates whether the Server Guard client is online. |
| OsVersion | String | The version of the operating system. |
| Region | String | The region where the server resides. |

| Developer Guide·Server Gua | rd | Apsara Stack Securit |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| Success | String | The task delivery result. |
| Uuid | String | The UUID of the server. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=PushAllTask &Tasks=OVAL_ENTITY &Uuids=inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5****
```

Sample response (JSON format)

```json
    "RequestId":"8A773295-DB9C-423D-979E-C0E8B9F88FEA",
    "PushTaskRsp":{
        "PushTaskResultList":[
                "InstanceName":"****",
                "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5****",
                "Message":"{\"code\":\"clinent_offline\",\"message\":\"The client is offl
ine\",\"success\":false}",
                "InstanceId":"i-25l6r****",
                "Ip":"x.x.x.x",
                "OsVersion":"linux",
                "Region":"cn-****-a01",
                "Online":false,
                "Success":false,
                "GroupId":336
```

`]`

#### 4.3.30 DescribeTopRiskyAssets

You can call this operation to query top N vulnerable servers.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeTopRiskyAssets. |
| PageSize | Integer | No | The number of records to return, that is, the top N vulnerable servers. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The number of returned records. |
| TopRiskyAssets | Array | The top N vulnerable servers. For more information, see the following descriptions. |
| HcCount | String | The number of at-risk items detected in the baseline check. |
| Ip | String | The IP address of the server. |
| Uuid | String | The universally unique identifier (UUID) of the server. |
| VulCount | String | The number of detected vulnerabilities. |
| WarningCount | String | The number of detected security events. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribeTopRiskyAssets &PageSize=1
```

Sample response (JSON format)

```json
    "TotalCount": 1,
    "RequestId": "5D8D4058-2EE3-4599-9951-BDAA3340AD4D",
    "TopRiskyAssets": [
            "Ip": "192.168.x.x",
            "Uuid": "inet-dsljaoe-jjdsklaj****",
            "VulCount": 2,
            "HcCount": 1,
            "WarningCount": 2
```

`]`

#### 4.3.31 UnbindAegis

You can call this operation to disable Server Guard for a specified server. Not e After this operation, Server Guard is not able to detect any security events on this server.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to UnbindAegis. |
| Uuids | String | Yes | The UUID of the server. Separate multiple UUIDs with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=UnbindAegis &Uuids=6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac,6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac
```

Sample responses (JSON format)

```json
 "RequestId":"8BFB5273-6582-446A-9E0B-BAC0A1A468EA"
```

#### 4.3.32 UninstallAegis

You can call this operation to uninstall the Server Guard client from a specified server. Not e After the client is uninstalled, Server Guard is not able to detect the security events on this server.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to UninstallAegis. |
| Uuids | String | Yes | The UUID of the server. Separate multiple UUIDs with commas (,). |
| Reason | String | No | The reason for uninstalling the client. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=UninstallAegis &Reason=Suspend the feature &Uuids=6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac,6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac
```

Sample responses (JSON format)

```json
 "RequestId":"8BFB5273-6582-446A-9E0B-BAC0A1A468EA"
```

### 4.4 Vulnerability management

#### 4.4.1 DescribeTarget

You can call this operation to query the servers that are checked for the specified type of risks in vulnerability management.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeTarget. |
| Type | String | No | The type of the risks. For example, vul represents vulnerabilities. |
| Config | String | No | The type of the vulnerabilities in JSON format. For example, {"vulType":"cve"} represents Linux software vulnerabilities. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The number of returned records. |
| Targets | Array | A list of servers that are checked for the specified type of risks. For more information, see the following parameter descriptions. |
| TargetType | String | Valid values: groupId: indicates the ID of an asset group. uuid: indicates the UUID of a server. |
| Target | String | The asset group ID or server UUID. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeTarget &Config={"vulType":"cve"} &Type=vul
```

Sample responses (JSON format)

```json
    "TotalCount":2,
    "RequestId":"1FF54D56-47ED-47FB-B4DB-2BDF3857D526",
    "Targets":[
            "Target":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
            "TargetType":"uuid"
```

`},`

```json
            "Target":"336",
            "TargetType":"groupId"
```

`]`

#### 4.4.2 ModifyVulTarget

You can call this operation to modify the servers for detecting a specified type of vulnerability in the vulnerability management settings.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyVulTarget. |
| Config | String | No | The vulnerability type information, in JSON format. For example, {"vulType":"cve"} indicates Linux software vulnerabilities. |
| Target | String | No | The specified server, in JSON format. For more information, see the sample request. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=ModifyVulTarget &Config={"vulType":"cve"} &Target={"target":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818","targetType":"uuid","flag": "add"}
```

Sample responses (JSON format)

```json
 "RequestId":"1FF54D56-47ED-47FB-B4DB-2BDF3857D526"
```

#### 4.4.3 DescribeVulTargetStatistics

You can call this operation to query the information about target hosts for which vulnerability detection is enabled in the vulnerability management configuration.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVulTargetStatistics. |
| Type | String | No | The vulnerability type. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CurrentPage | Integer | The current page number. |

| psara Stack Security |   | Developer Guide·Server Guar |
|---|---|---|
| Name | Type | Description |
| PageSize | Integer | The maximum number of records displayed on a page. |
| TotalCount | Integer | The total number of returned records. |
| TargetStats | Array | The list of target hosts for which vulnerability detection is enabled. For more information, see the following parameter descriptions. |
| VulType | String | The vulnerability type. |
| Targets | Array | The information about target hosts. For more information, see the following parameter descriptions. |
| Flag | String | Indicates whether vulnerability detection is enabled. |
| TargetType | String | The type of the Target parameter value. Valid values: groupId: indicates an asset group ID. uuid: indicates a host asset UUID. |
| Target | String | The asset group ID or host asset UUID. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeVulTargetStatistics &Type=cve
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "TargetStats":[
   "VulType":"cve","Targets":[]
```

`},`

```json
 "PageSize":10,
 "RequestId":"89DD84B4-B592-476C-A6C0-51D56B3E8EAC",
 "CurrentPage":1
```

#### 4.4.4 DescribeTargetConfig

You can call this operation to query the vulnerability scanning configuration information of a specified server.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeTargetConfig. |
| Type | String | No | The type of the vulnerability. |
| Uuid | String | No | The UUID of the server. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of the returned records. |
| TargetConfigs | Array | The list of vulnerability scanning configuration information. For more information, see the following parameter descriptions. |
| Type | String | The type of the vulnerability. |
| Config | String | Whether vulnerability scanning is enabled. Valid values: on and off. |
| OverAllConfig | String | Whether global vulnerability scanning is enabled. Valid values: on and off. Not e The global vulnerability scanning configuration overrides the vulnerability scanning configuration for a single server. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeTargetConfig &Type=cve &Uuid=inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "RequestId":"092094BF-910F-4CE6-BE93-C3989B607977",
 "TargetConfigs":[
   "Config":"off",
   "Type":"cve",
   "OverAllConfig":"off"
```

`]`

#### 4.4.5 ModifyTargetConfig

You can call this operation to modify the vulnerability scanning configuration for a specified server.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyTargetConfig. |
| Type | String | No | The type of the vulnerability. |
| Uuid | String | No | The UUID of the server. |
| Config | String | No | The vulnerability scanning configuration. Valid values: on: indicates enabled. off: indicates disabled. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=ModifyTargetConfig &Config=on &Type=cms &Uuid=46ef7c05-0c53-486c-b446-ef6ff972551c
```

Sample responses (JSON format)

```json
 "RequestId":"092094BF-910F-4CE6-BE93-C3989B607977"
```

#### 4.4.6 DescribeVulConfig

You can call this operation to query the global scanning configuration for each vulnerability type.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVulConfig. |
| Type | String | No | The type of the vulnerability. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of returned records. |
| TargetConfigs | Array | The list of global vulnerability scanning configurations. For more information, see the following parameter descriptions. |
| Type | String | The type of the vulnerability. |
| Config | String | The global scanning configuration for the vulnerability type. Valid values: on and off. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeVulConfig &Type=cve
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "RequestId":"A8E09216-31DF-45B6-A76B-E3F053752C07",
 "TargetConfigs":[
   "Config":"off",
   "Type":"cve"
```

#### 4.4.7 ModifyVulConfig

You can call this operation to modify the global vulnerability scanning configuration. Not e The global vulnerability scanning configuration overrides the vulnerability scanning configuration for a single server.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyVulConfig. |
| Type | String | No | The type of the vulnerability. |
| Config | String | No | The vulnerability scanning configuration. Valid values: on: indicates enabled. off: indicates disabled. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=ModifyVulConfig &Config=on &Type=cms
```

Sample responses (JSON format)

```json
 "RequestId":"A8E09216-31DF-45B6-A76B-E3F053752C07"
```

#### 4.4.8 DescribeAutoDelConfig

You can call this operation to query the number of days that an invalid vulnerability is kept for before it is automatically deleted in the vulnerability management settings.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeAutoDelConfig. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Days | Integer | The number of days that an invalid vulnerability is kept for. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeAutoDelConfig
```

Sample responses (JSON format)

```json
 "RequestId":"E3785090-CFF4-4C53-82E4-08F902586053",
 "Days":7
```

#### 4.4.9 ModifyAutoDelConfig

You can call this operation to modify the number of days that an invalid vulnerability is kept for before it is automatically deleted in the vulnerability management settings.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyAutoDelConfig. |
| Days | Integer | No | The number of days that an invalid vulnerability is kept for. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=ModifyAutoDelConfig &Days=7
```

Sample responses (JSON format)

```json
 "RequestId":"E3785090-CFF4-4C53-82E4-08F902586053"
```

#### 4.4.10 DescribeVulLevel

escpto You can call this operation to query the vulnerability severities that require attention.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVulLevel. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| ConcernLevels | List | The list of vulnerability severities that require attention. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeVulLevel
```

Sample responses (JSON format)

```json
 "RequestId":"7935CB7A-D1B7-4EE6-93D0-FF3D040CF19B",
 "ConcernLevels":["high","medium"]
```

#### 4.4.11 ModifyVulLevel

You can call this operation to change the vulnerability severities that require attention.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyVulLevel. |

| psara Stack Security |   |   | Developer Guide·Server Guar |
|---|---|---|---|

| Name | Type | Required | Description |
|---|---|---|---|
| ConcernLevels | String | No | The vulnerability severities that require attention. Separate multiple severities with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=ModifyVulLevel &ConcernLevel=high,medium
```

Sample responses (JSON format)

```json
 "RequestId":"7935CB7A-D1B7-4EE6-93D0-FF3D040CF19B"
```

#### 4.4.12 CreateVulWhitelist

You can call this operation to add a specified vulnerability to the whitelist. Server Guard does not report the vulnerabilities on the whitelist.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateVulWhitelist. |
| Reason | String | No | The reason for adding the vulnerability to the whitelist. |
| Whitelist | String | No | The vulnerability to be whitelisted, in JSON format. For more information, see the sample request. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=CreateVulWhitelist &Reason=The vulnerability is not harmful. &Whitelist=[{"name":"oval:com.redhat.rhsa:def:20173263","type":"cve","aliasName":"RHSA-20 17:3263: curl security update"}]
```

Sample responses (JSON format)

```json
 "RequestId":"E3785090-CFF4-4C53-82E4-08F902586053"
```

#### 4.4.13 DescribeVulWhitelist

You can call this operation to obtain the whitelist of vulnerabilities.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVulWhitelist. |
| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query output. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| TotalCount | Integer | The total number of returned records. |
| VulWhitelists | Array | The vulnerability whitelist. For more information, see the following parameter descriptions. |
| AliasName | String | The alias of the vulnerability. |
| Name | String | The name of the vulnerability. |
| Reason | String | The reason for adding the vulnerability to the whitelist. |
| Type | String | The vulnerability type. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeVulWhitelist &CurrentPage=1 &PageSize=20
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "VulWhitelists":[
   "Name":"oval:com.redhat.rhsa:def:20173263",
   "AliasName":"RHSA-2017:3263: curl security update",
   "Type":"cve",
   "Reason":"Not fixed at present"
```

`],`

```json
 "PageSize":3,
 "RequestId":"74F97EF7-B543-43FD-A4E9-18456731F9C5",
 "CurrentPage":1
```

#### 4.4.14 DeleteVulWhitelist

You can call this operation to delete a specified vulnerability from the vulnerability whitelist. After this operation, Server Guard re-detects and reports the vulnerability.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DeleteVulWhitelist. |
| Whitelist | String | No | The vulnerability to be deleted from the whitelist, in JSON format. For more information, see the sample request. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DeleteVulWhitelist &Whitelist=[{"name":"oval:com.redhat.rhsa:def:20173263","type":"cve","aliasName":"RHSA-20 17:3263: curl security update"}]
```

Sample response (JSON format)

```json
 "RequestId":"E3785090-CFF4-4C53-82E4-08F902586053"
```

#### 4.4.15 DescribeGroupedVul

You can call this operation to query information about the specified vulnerability group. The vulnerability management feature can display detected vulnerability records by group. A vulnerability group contains all servers with a specific vulnerability detected by Server Guard.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeGroupedVul. |
| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query output. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |
| Dealed | String | No | Indicates whether the vulnerability has been handled. Valid values: Y: indicates that the vulnerability has been handled. N: indicates that the vulnerability has not been handled. |
| Direction | String | No | The sorting mode of vulnerabilities in the vulnerability group. Valid values: asc: indicates sorting in ascending order. desc: indicates sorting in descending order. |
| LastTsEnd | Long | No | The end time of the last detection of the vulnerability. |
| LastTsStart | Long | No | The start time of the last detection of the vulnerability. |
| Level | String | No | The severity of the vulnerability. Valid values: serious: critical high: important medium: moderate low: low |
| Name | String | No | The name of the vulnerability. |

| Name | Type | Required | Description |
|---|---|---|---|
| Necessity | String | No | The necessity for fixing the vulnerability. Valid values: asap: indicates that the vulnerability must be fixed as soon as possible. later: indicates that the vulnerability can be fixed later. nntf: indicates that the vulnerability can be ignored. |
| OrderBy | String | No | The field based on which the vulnerabilities in the vulnerability group are sorted. You can specify other request parameters for sorting order. |
| PatchId | Long | No | The ID of the patch used to fix the vulnerability. |
| Product | String | No | The product where the vulnerability exists. |

| Name | Type | Required | Description |
|---|---|---|---|
| StatusList | String | No | The status of the vulnerability. Valid values: 1: indicates that the vulnerability has not been fixed. 2: indicates that the vulnerability fix failed. 3: indicates that the server has failed to be rolled back to the version before the vulnerability fix. 4: indicates that the vulnerability is being fixed. 5: indicates that the server is being rolled back to the version before the vulnerability fix. 6: indicates that the vulnerability fix is being verified. 7: indicates that the vulnerability has been fixed successfully. 8: indicates that the vulnerability has been fixed successfully, and that the server is waiting for restart. 9: indicates that the server has been rolled back to the version before the vulnerability fix. 10: indicates that the vulnerability has been ignored. 11: indicates that the server has been rolled back to the version before the vulnerability fix, and that the server is waiting for restart. 12: indicates that the vulnerability does not exist. 20: indicates that the vulnerability is invalid. Not e The statuses are specified in a single parameter, separated with commas (,). |
| Type | String | No | The type of the vulnerability. |
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| TotalCount | Integer | The total number of returned records. |
| GroupedVulItems | Array | The information about the vulnerability group. For more information, see the following parameter descriptions. |
| AliasName | String | The alias of the vulnerability. |
| AsapCount | Integer | The number of assets to be fixed as soon as possible. |
| Count | Integer | The total number of vulnerabilities. |
| GmtLast | Long | The last time when the vulnerability was detected. |
| HandledCount | Integer | The total number of vulnerabilities handled. |
| Level | String | The severity of the vulnerability. |
| Name | String | The name of the vulnerability. |
| PendingCount | Integer | The number of vulnerabilities that have not been handled. |
| Product | String | The product affected by the vulnerability. |
| Status | Integer | The status of the vulnerability. |
| TotalCount | Integer | The total number of vulnerabilities. |
| Type | String | The type of the vulnerability. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeGroupedVul &CurrentPage=1 &Dealed=y &Direction=asc &LastTsEnd=1517414400000 &LastTsStart=1517414500000 &Level=high &Name=oval:com.redhat.rhsa:def:20170817 &Necessity=asap &OrderBy=name &PageSize=20 &PatchId=27001 &Product=redhat &SourceIp= &StatusList=1,2 &Type=cve &Uuids=46ef7c05-0c53-486c-b446-ef6ff972551c,b688bf9f-1fd9-42c8-bb34-28697f562dc5
```

Sample responses (JSON format)

```json
 "GroupedVulItems":[
   "Name":"oval:com.redhat.rhsa:def:20170817",
   "Status":7,
   "Count":0,
   "TotalCount":1,
   "PendingCount":0,
   "AliasName":"RHSA-2017:0817: kernel security, bug fix, and enhancement update",
   "AsapCount":0,
   "Type":"cve",
   "GmtLast":1513695612000,
   "Level":"high",
   "HandledCount":1
```

`},` `],`

```json
 "TotalCount":1,
 "PageSize":10,
 "RequestId":"6FCF95BE-7A78-4AD8-811C-BF12FC34AC34",
 "CurrentPage":1
```

#### 4.4.16 DescribeVulList

You can call this operation to obtain the vulnerability list of the specified host asset.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVulList. |
| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query output. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |
| Dealed | String | No | Indicates whether the vulnerability has been handled. Valid values: Y: indicates that the vulnerability has been handled. N: indicates that the vulnerability has not been handled. |
| Level | String | No | The severity of the vulnerability. Valid values: serious: critical high: important medium: moderate low: low |
| Name | String | No | The name of the vulnerability. |
| Necessity | String | No | The necessity for fixing the vulnerability. Valid values: asap: indicates that the vulnerability must be fixed as soon as possible. later: indicates that the vulnerability can be fixed later. nntf: indicates that the vulnerability can be ignored. |
| Type | String | No | The type of the vulnerability. |

| Name | Type | Required | Description |
|---|---|---|---|
| StatusList | String | No | The status of the vulnerability. Valid values: 1: indicates that the vulnerability has not been fixed. 2: indicates that the vulnerability fix failed. 3: indicates that the host has failed to be rolled back to the version before the vulnerability fix. 4: indicates that the vulnerability is being fixed. 5: indicates that the host is being rolled back to the version before the vulnerability fix. 6: indicates that the vulnerability fix is being verified. 7: indicates that the vulnerability has been fixed successfully. 8: indicates that the vulnerability has been fixed successfully, and that the host is waiting for restart. 9: indicates that the host has been rolled back to the version before the vulnerability fix. 10: indicates that the vulnerability has been ignored. 11: indicates that the host has been rolled back to the version before the vulnerability fix, and that the host is waiting for restart. 12: indicates that the vulnerability does not exist. 20: indicates that the vulnerability is invalid. Not e Note: The statuses are specified in a single parameter, separated with commas (,). |
| Uuids | String | No | The UUID of the host asset. Separate multiple host asset UUIDs with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| TotalCount | Integer | The total number of records returned from the query. |
| VulRecords | Array | The list of vulnerabilities. For more information, see the following parameter descriptions. |
| AliasName | String | The alias of the vulnerability. |
| ExtendContent | String | The extended information of the vulnerability. |
| ExtendContentJson | String | The extended information of the vulnerability (JSON format). |
| FirstTs | Long | The first time when the vulnerability was detected. |
| ModifyTs | Long | The last time when the vulnerability was updated. |
| LastTs | Long | The last time when the vulnerability was detected. |
| Level | String | The severity of the vulnerability. |
| Name | String | The name of the vulnerability. |
| Necessity | String | The necessity for fixing the vulnerability. Valid values: asap: indicates that the vulnerability must be fixed as soon as possible. later: indicates that the vulnerability can be fixed later. nntf: indicates that the vulnerability can be ignored. |
| PrimaryId | Long | The ID of the primary key. |
| Product | String | The product affected by the vulnerability. |
| RecordId | Long | The ID of the vulnerability record. |
| Related | String | The CVE ID of the vulnerability. |
| RepairTs | Long | The time when the vulnerability was fixed. |
| ResultCode | String | The code of the vulnerability handling result. |

| psara Stack Security |   | Developer Guide·Server Guar |
|---|---|---|
| Name | Type | Description |
| ResultMessage | String | The message of the vulnerability handling result. |
| RiskDesc | String | The risk description of the vulnerability. |
| RiskLevel | Integer | The risk level of the vulnerability. |
| Status | Integer | The status of the vulnerability. Valid values: 1: indicates that the vulnerability is to be handled. 2: indicates that the vulnerability has been ignored. 3: indicates that the vulnerability has been confirmed. 8: indicates that the vulnerability has been marked as a false positive. 16: indicates that the vulnerability is being handled. 32: indicates that the vulnerability has been handled. |
| Tag | String | The tag of the vulnerability. |
| Type | String | The type of the vulnerability. |
| Uuid | String | The UUID of the host asset. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeVulList &CurrentPage=1 &Dealed=n &Level=serious &Name=RHSA-2017:1100: nss and nss-util security update &Necessity=asap &PageSize=20 &StatusList=1 &Type=cve &Uuids=f293ade2-e5b1-4cc0-99a6-cc993a4158cc
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "PageSize":20,
 "RequestId":"2E35F7F7-DA6D-46A5-BA9D-8751BDAE7710",
 "CurrentPage":1,
 "VulRecords":[
   "Uuid":"b688bf9f-1fd9-42c8-bb34-28697f562dc5",
   "Necessity":"nntf",
   "ModifyTs":1512949391000,
   "Type":"cve",
   "FirstTs":1499321694000,
   "Related":"CVE-2016-1248",
   "ExtendContentJson":{"Necessity":{"Cvss_factor":"6.8","Total_score":"6.799999965526585
","Status":"normal","Enviroment_factor":"1.0","Time_factor":"0.9999999949303802","Assets_ factor":"1","Gmt_create":"20171210","Is_calc":"1"},"Os":"centos","cveList":["CVE-2016-124 8"],"RpmEntityList":[{"Name":"vim-minimal","Version":"7.4.160","FullVersion":"7.4.160-1.e l7","MatchDetail":"vim-minimal version less than 2:7.4.160-1.el7_3.1","UpdateCmd":"yum up date vim-minimal","Path":"/etc/virc"}],"OsRelease":"7"},
   "Name":"oval:com.redhat.rhsa:def:20162972",
   "Status":1,
   "LastTs":1512949391000,
   "AliasName":"RHSA-2016:2972: vim security update (Moderate)",
   "Tag":"oval",
   "PrimaryId":281156,
   "Level":"high"
```

`]`

#### 4.4.17 DescribeVulDetails

You can call this operation to query detailed information about a vulnerability.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVulDetails. |
| Type | Integer | Yes | The type of the vulnerability. |
| Name | String | Yes | The name of the vulnerability. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Cves | Array | The vulnerability details. For more information, see the following parameter descriptions. |
| Classify | String | The vulnerability type code. |
| Classifys | Array | The detailed vulnerability information. For more information, see the following parameter descriptions. |
| Classify | String | The vulnerability type code. |
| Description | String | The description of the vulnerability type. |
| DemoVideoUrl | String | The URL of the vulnerability video demo. |
| CnvdId | String | The CNVD ID. |
| Complexity | String | The complexity. |
| Content | String | The vulnerability details. |
| ExtendContentJson | String | The additional information about the vulnerability (JSON format). |
| CveId | String | The CVE ID. |
| CvssScore | String | The CVSS score. |
| CvssVector | String | The CVSS score string. |
| OtherId | String | The ID of the vulnerability. |
| Poc | String | The proof of concept (POC) method. |
| PocCreateTime | Long | The time when the POC method was created. |
| PocDisclosureTime | Long | The time when the POC method was revealed. |
| Service | String | The products that are affected by the vulnerability. |
| Reference | String | The corresponding reference. |
| ReleaseTime | Long | The time when the vulnerability was revealed. |
| Solution | String | The solution for fixing the vulnerability. |
| Summary | String | The vulnerability summary. |
| Title | String | The title of the vulnerability. |

| Developer Guide·Server Gua | rd | Apsara Stack Securit |
|---|---|---|

| Name | Type | Description |
|---|---|---|
| Vendor | String | The vendors that are affected by the vulnerability. |
| VulLevel | String | The severity level of the vulnerability. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeVulDetails &Name=oval:com.redhat.rhsa:def:20170036 &Type=cve
```

Sample responses (JSON format)

```json
 "Cves": [{
  "CvssVector": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
  "OtherId": "CVE-2016-7117",
  "Classifys": [],
  "Vendor": "Linux",
  "CvssScore": "10.0",
  "CnvdId": "CNVD-2016-09362",
  "Reference": "http://www.securityfocus.com/bid/93304",
  "Solution": "<p>The vendor has released a patch to fix this vulnerability. Download the
patch from: \n<br />https://bugzilla.redhat.com/show_bug.cgi?id=1382268</p>\n",
  "CveId": "CVE-2016-7117",
  "ReleaseTime": 1476028800000,
  "VulLevel": "serious",
  "Title": "The use-after-free vulnerability in __sys_recvmmsg function in the Linux kern
el",
  "Summary": "The Linux kernel is released by the Linux Foundation of the United States f
or Linux operating systems. The use-after-free vulnerability is found in the net/socket.c file in \n\nLinux kernel 4.5.2 and earlier versions. It allows remote attackers to execut e arbitrary code."
 }],
 "RequestId": "70DEE6B7-A167-4B5D-ADAA-3631443D5190"
```

#### 4.4.18 DescribeVulNumStatistics

You can call this operation to query vulnerability statistics.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVulNumStatistics. |
| StartTs | Long | No | The start time for statistics collection. |
| EndTs | Long | No | The end time for statistics collection. |
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CmsDealedTotalNum | Integer | The number of CMS vulnerabilities handled. |
| CmsNum | Integer | The number of CMS vulnerabilities. |
| CveNum | Integer | The number of CVE vulnerabilities. |
| EmgNum | Integer | The number of other vulnerabilities. |
| SysNum | Integer | The number of Windows OS vulnerabilities. |
| VulAsapSum | Integer | The number of vulnerabilities that need to be handled as soon as possible. |
| VulDealedTotalNum | Integer | The total number of vulnerabilities handled. |
| VulSeriousTotal | Integer | The total number of critical vulnerabilities. |
| VulHighTotal | Integer | The total number of important vulnerabilities. |
| VulMediumTotal | Integer | The total number of moderate vulnerabilities. |
| VulLowTotal | Integer | The total number of low vulnerabilities. |
| VulLaterSum | Integer | The number of vulnerabilities that can be handled later. |
| VulNntfSum | Integer | The number of vulnerabilities that do not need to be fixed temporarily. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeVulNumStatistics &EndTs=1514736000000 &StartTs=1514736000000 &Uuids=46ef7c05-0c53-486c-b446-ef6ff972551c
```

Sample responses (JSON format)

```json
    "VulHighTotal":0,
    "CveNum":1,
    "VulMediumTotal":0,
    "EmgNum":0,
    "VulLowTotal":0,
    "VulNntfSum":1,
    "VulAsapSum":0,
    "SysNum":0,
    "VulDealedTotalNum":1,
    "RequestId":"093C121C-2981-4E69-8309-CD1BDD8C872A",
    "CmsNum":0,
    "VulSeriousTotal":0,
    "CmsDealedTotalNum":0,
    "VulLaterSum":0
```

#### 4.4.19 DescribeVulLevelStatistics

You can call this operation to obtain the statistics on vulnerabilities by vulnerability severity.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVulLevelStatistics. |
| StartTs | Long | No | The start time of the time frame specified for query. |
| EndTs | Long | No | The end time of the time frame specified for query. |
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of returned records. |
| LevelStatistics | Array | The vulnerability statistics. For more information, see the following parameter descriptions. |
| CmsDealedTotalNum | Integer | The number of handled CMS vulnerabilities. |
| CmsNum | Integer | The number of CMS vulnerabilities. |
| CveNum | Integer | The number of CVE vulnerabilities. |
| EmgNum | Integer | The number of other vulnerabilities. |
| Level | String | The severity of the vulnerability. |
| SysNum | Integer | The number of Windows vulnerabilities. |
| VulAsapSum | Integer | The number of high-priority vulnerabilities. |
| VulDealedTotalNum | Integer | The total number of handled vulnerabilities. |
| VulSeriousTotal | Integer | The total number of critical-risk vulnerabilities. |
| VulHighTotal | Integer | The total number of important-risk vulnerabilities. |
| VulMediumTotal | Integer | The total number of moderate-risk vulnerabilities. |
| VulLowTotal | Integer | The total number of low-risk vulnerabilities. |
| VulLaterSum | Integer | The number of medium-priority vulnerabilities. |
| VulNntfSum | Integer | The number of low-priority vulnerabilities. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeVulLevelStatistics &EndTs=1514736000000 &StartTs=1514736000000 &Uuids=46ef7c05-0c53-486c-b446-ef6ff972551c,b688bf9f-1fd9-42c8-bb34-28697f562dc5
```

Sample responses (JSON format)

```json
 "TotalCount":0,
 "LevelStatistics":[
   "VulHighTotal":0,
   "CveNum":0,
   "VulMediumTotal":0,
   "EmgNum":0,
   "VulLowTotal":0,
   "VulNntfSum":0,
   "VulAsapSum":0,
   "SysNum":0,
   "VulDealedTotalNum":0,
   "CmsNum":0,
   "Level":"high",
   "VulSeriousTotal":0,
   "CmsDealedTotalNum":0,
   "VulLaterSum":0
```

`},`

```json
   "VulHighTotal":0,
   "CveNum":0,
   "VulMediumTotal":0,
   "EmgNum":0,
   "VulLowTotal":0,
   "VulNntfSum":0,
   "VulAsapSum":0,
   "SysNum":0,
   "VulDealedTotalNum":0,
   "CmsNum":0,
   "Level":"low",
   "VulSeriousTotal":0,
   "CmsDealedTotalNum":0,
   "VulLaterSum":0
```

`],`

```json
 "RequestId":"9B062D3F-AD5A-4D3E-9A7A-45CAC2713FC0"
```

#### 4.4.20 DescribeVulMachineList

You can call this operation to query the vulnerability statistics of a specified server.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVulMachineList. |

| psara Stack Security |   |   | Developer Guide·Server Guar |
|---|---|---|---|

| Name | Type | Required | Description |
|---|---|---|---|
| StartTs | Long | No | The start time of the time frame during which the statistics were collected. |
| EndTs | Long | No | The end time of the time frame during which the statistics were collected. |
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of the returned records. |
| MachineStatistics | Array | The vulnerability statistics. For more information, see the following parameter descriptions. |
| CmsDealedTotalNum | Integer | The number of CMS vulnerabilities that have been handled. |
| CmsNum | Integer | The number of CMS vulnerabilities. |
| CveNum | Integer | The number of CVE vulnerabilities. |
| EmgNum | Integer | The number of other vulnerabilities. |
| SysNum | Integer | The number of Windows vulnerabilities. |
| VulAsapSum | Integer | The number of high-priority vulnerabilities. |
| VulDealedTotalNum | Integer | The total number of vulnerabilities that have been handled. |
| VulSeriousTotal | Integer | The total number of critical-risk vulnerabilities. |
| VulHighTotal | Integer | The total number of important-risk vulnerabilities. |
| VulMediumTotal | Integer | The total number of moderate-risk vulnerabilities. |
| VulLowTotal | Integer | The total number of low-risk vulnerabilities. |
| VulLaterSum | Integer | The number of medium-priority vulnerabilities. |
| VulNntfSum | Integer | The number of low-priority vulnerabilities. |
| Uuid | String | The UUID of the server. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeVulMachineList &EndTs=1514736000000 &StartTs=1514736000000 &Uuids=46ef7c05-0c53-486c-b446-ef6ff972551c
```

Sample responses (JSON format)

```json
 "TotalCount":0,
 "MachineStatistics":[
   "Uuid":"577f9886-bf66-4c3c-88ac-28c938cb527b",
   "VulHighTotal":0,
   "CveNum":1,
   "VulMediumTotal":0,
   "EmgNum":0,
   "VulLowTotal":0,
   "VulNntfSum":0,
   "VulAsapSum":0,
   "SysNum":0,
   "VulDealedTotalNum":0,
   "CmsNum":0,
   "VulSeriousTotal":0,
   "CmsDealedTotalNum":0,
   "VulLaterSum":0
```

`],`

```json
 "RequestId":"A3F8BE63-9BA1-450D-BB5D-CE9205E6645D"
```

#### 4.4.21 OperateVul

You can call this operation to handle detected vulnerabilities.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to OperateVul. |

| Name | Type | Required | Description |
|---|---|---|---|
| Info | String | No | The vulnerability information, in JSON format. For more information, see the sample request. |
| OperateType | String | No | The type of the operation. Valid values: vulfix: indicates an operation to fix _ the vulnerability. vulverify: indicates an operation to _ verify the vulnerability fix. vulrebooted: indicates an operation _ to verify the vulnerability fix after the server is restarted. vulrollback: indicates an operation to _ undo the vulnerability fix. vulignore: indicates an operation to _ ignore the vulnerability. vulundo ignore: indicates an _ _ operation to unignore the vulnerability. vuldelete: indicates an operation to _ delete the vulnerability record. |
| Reason | String | No | The reason why the vulnerability is ignored if the OperateType parameter is set to vul ignore. _ |
| Type | String | No | The type of the vulnerability. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=OperateVul &Info=[{"name":"oval:com.redhat.rhsa:def:20171100","uuid":"e49fb179-bbe7-4b6c-ab65-e106fb 58d235","tag":"oval"}] &OperateType=vul_ignore &Reason=Postpone the fix &Type=cve
```

Sample responses (JSON format)

```json
 "RequestId":"A3F8BE63-9BA1-450D-BB5D-CE9205E6645D"
```

#### 4.4.22 ModifyBatchIgnoreVul

You can call this operation to ignore multiple vulnerabilities.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyBatchIgnoreVul. |
| Info | String | No | The vulnerabilities to be ignored, in JSON format. For more information, see the sample request. |
| Reason | String | No | The reason for ignoring the vulnerabilities. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=ModifyBatchIgnoreVul &Info=[{"name":"oval:com.redhat.rhsa:def:20162972","type":"cve","aliasName":"RHSA-2016:29 72: vim security update (Moderate)"}] &Reason=Postpone handling
```

Sample responses (JSON format)

```json
 "RequestId":"E3785090-CFF4-4C53-82E4-08F902586053"
```

#### 4.4.23 DeleteVulBatch

You can call this operation to delete a specified batch of vulnerabilities.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteVulBatch. |
| BatchName | String | No | The name of the vulnerability batch. |
| Resource | String | No | The scenario of the vulnerability batch. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DeleteVulBatch &BatchName=Vulnerabilities managed by network security team &Resource=vulnerability
```

Sample responses (JSON format)

```json
 "RequestId":"E3785090-CFF4-4C53-82E4-08F902586053"
```

#### 4.4.24 ExportVul

You can call this operation to export vulnerability records that match the specified criteria.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ExportVul. |
| AliasName | String | No | The alias of the vulnerability. |
| BatchName | String | No | The name of the vulnerability fix batch. |
| Dealed | String | No | Indicates whether the vulnerability has been handled. Valid values: Y: indicates that the vulnerability has been handled. N: indicates that the vulnerability has not been handled. |
| Level | String | No | The severity of the vulnerability. |
| Name | String | No | The name of the vulnerability. |
| Necessity | String | No | The priority of the vulnerability. Valid values: asap: indicates that the vulnerability must be fixed as soon as possible. later: indicates that the vulnerability can be fixed later. nntf: indicates that the vulnerability can be ignored. |
| Resource | String | No | The source of the vulnerability fixing batch. |
| StatusList | String | No | The status of the vulnerability. Valid values: 1: indicates that the vulnerability is pending. 2: indicates that the vulnerability has been ignored. 3: indicates that the vulnerability has been confirmed. 8: indicates that the vulnerability has been marked as a false positive. 16: indicates that the vulnerability is being handled. 32: indicates that the vulnerability has been handled. You can specify multiple statuses and separate them with commas (,). |
| Type | String | No | The type of the vulnerability. |

| psara Stack Security |   |   | Developer Guide·Server Guar |
|---|---|---|---|
| Name | Type | Required | Description |
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CurrentCount | Integer | The number of records that have been exported. |
| ExportStatus | String | The status of the export task. Valid values: init: indicates that the export task is being initialized. pending: indicates that the export task is pending for summarization. exporting: indicates that the export task is being executed. success: indicates that the export task has been completed. fail: indicates that the export task has failed. |
| Message | String | The status description or failure information of the export task. |
| FileName | String | The name of the exported file. |
| Id | Integer | The ID of the export task. |
| Link | String | The download link of the exported file. |
| Progress | Integer | The export progress. |
| TotalCount | Integer | The total number of records that have been exported. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=ExportVul for example, RHSA-2016:2972: vim security update (Moderate), and trigger another vulnerab ility scan. &BatchName=Security group test &Dealed=y &Level=low &Name=oval:com.redhat.rhsa:def:20162972 &Necessity=later &Resource=vulnerability &StatusList=1 &Type=cve &Uuids=46ef7c05-0c53-486c-b446-ef6ff972551c
```

Sample responses (JSON format)

```json
 "FileName":"cve_20180303",
 "RequestId":"3B3C79B1-617E-4081-903B-86EA4AC0213F",
 "Id":36
```

#### 4.4.25 DescribeVulExportInfo

You can call this operation to query a vulnerability record export task.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeVulExportInfo. |
| ExportId | Long | No | The ID of the vulnerability record export task. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| CurrentCount | Integer | The number of records that have been exported. |

| Parameter | Type | Description |
|---|---|---|
| ExportStatus | String | The status of the export task. Valid values: init: indicates that the export task is being initialized. pending: indicates that the export task is pending. exporting: indicates that the export task is being executed. success: indicates that the export task has been completed. fail: indicates that the export task has failed. |
| Message | String | The status description or failure information of the export task. |
| FileName | String | The name of the exported file. |
| Id | Integer | The ID of the export task. |
| Link | String | The download link of the exported file. |
| Progress | Integer | The export progress. |
| TotalCount | Integer | The total number of records that have been exported. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribeVulExportInfo &ExportId=10
```

Sample response (JSON format)

```json
 "Status":"success",
 "Link":"http://jiangzhi.oss-cn-shanghai.example.com/export/sys_20171124_1511510709277.zi
p?Expires=1511514309&OSSAccessKeyId=<yourAccessKeyId>&Signature=xxxx%xxxx%3D",
 "TotalCount":2,
 "Message":"success",
 "FileName":"sys_20171124",
 "RequestId":"9C689776-0F8B-4290-8C11-D9242A86C75B",
 "CurrentCount":1,
 "Id":17,
 "Progress":100
```

### 4.5 Baseline check

#### 4.5.1 DescribeStrategy

You can call this operation to obtain a list of baseline check policies.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeStrategy. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Count | Integer | The total number of the returned records. |
| Strategies | Array | The list of baseline check policies. For more information, see the following parameter descriptions. |
| CycleDays | Integer | The cycle of policy execution. |
| CycleStartTime | Integer | The start time of policy execution. Valid values: 0: indicates the period from 00:00 to 06:00. 6: indicates the period from 06:00 to 12:00. 12: indicates the period from 12:00 to 18:00. 18: indicates the period from 18:00 to 24:00. |
| EcsCount | Integer | The number of hosts using the policy. |
| Id | Integer | The ID of the policy. |
| Name | String | The name of the policy. |
| RiskCount | Integer | The number of at-risk items contained in the policy. |
| Type | Integer | The policy type. Valid values: 1: indicates a system default policy. 2: indicates a custom policy. |

| Name | Type | Description |
|---|---|---|
| ConfigTargets | Array | The information about asset groups using the policy. For more information, see the following parameter descriptions. |
| Flag | String | A flag that indicates whether the policy applies to the specified asset group. Valid values: add: indicates the whitelist mode, that is, the policy applies to the asset group. del: indicates the blacklist mode, that is, the policy does not apply to the asset group. Not e Generally, the blacklist mode is used for system default policies, and the whitelist mode is used for custom policies. |
| TargetType | String | The return value is fixed to groupId, which indicates that the value of the Target parameter is an asset group ID. |
| Target | String | The ID of the asset group. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeStrategy
```

Sample responses (JSON format)

```json
    "Count": 2,
    "RequestId": "4F914046-4358-4BA9-BE42-83AA1FD1FF52",
    "Strategies": [
            "Name": "test",
            "RiskCount": 2,
            "CycleDays": 3,
            "Type": 2,
            "CycleStartTime": 6,
            "ConfigTargets": [
                    "Target": "4361221",
                    "Flag": "add",
                    "TargetType": "groupId"
```

`],`

```json
            "Id": 15161,
            "EcsCount": 0
```

`},`

```json
            "Name": "Default policy",
            "RiskCount": 14,
            "CycleDays": 1,
            "Type": 1,
            "CycleStartTime": 0,
            "ConfigTargets": [
                    "Target": "none",
                    "Flag": "del",
                    "TargetType": "flag_item"
```

`],`

```json
            "Id": 20,
            "EcsCount": 48
```

`]`

#### 4.5.2 DescribeStratetyDetail

You can call this operation to query the details of a specified baseline check policy.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeStratetyDetail. |

| psara Stack Security |   |   | Developer Guide·Server Guar |
|---|---|---|---|

| Name | Type | Required | Description |
|---|---|---|---|
| Id | String | No | The ID of the baseline check policy. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Strategy | Array | The details of the baseline check policy. For more information, see the following parameter descriptions. |
| CycleDays | Integer | The cycle of policy execution. |
| CycleStartTime | Integer | The start time of policy execution. Valid values: 0: indicates the period from 00:00 to 06:00. 6: indicates the period from 06:00 to 12:00. 12: indicates the period from 12:00 to 18:00. 18: indicates the period from 18:00 to 24:00. |
| Id | Integer | The ID of the policy. |
| Name | String | The name of the policy. |
| Type | Integer | The type of the policy. Valid values: 1: indicates a system default policy. 2: indicates a custom policy. |
| RiskTypeWhiteListQuery ResultList | Array | The risk information contained in the policy. For more information, see the following parameter descriptions. |
| Alias | String | The name of the risk category. |
| On | Boolean | Indicates whether to check for risks of the specified category. |
| TypeName | String | The code of the risk category. |
| SubTypes | Array | The list of risk subcategories. For more information, see the following parameter descriptions. |
| Alias | String | The name of the risk subcategory. |
| TypeName | String | The code of the risk subcategory. |
| On | Boolean | Indicates whether to check for risks of the specified subcategory. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeStratetyDetail &Id=1
```

Sample responses (JSON format)

```json
     "RequestId": "99F17C4B-2E23-4B41-BBEB-C03963B06EB4",
     "Strategy": {
  "Name": "Yunwu testing",
             "CycleDays": 1,
             "CycleStartTime": 18,
             "Type": 2,
             "Id": 12,
             "RiskTypeWhiteListQueryResultList": [
                     "On": false,
                     "Alias": "Compliance with Security Standards",
                     "TypeName": "cis",
                     "SubTypes": [
                              "On": true,
                              "Alias": "Memcached",
                              "TypeName": "memcached-check"
```

`},`

```json
                              "On": true,
                              "Alias": "CentOS 7",
                              "TypeName": "centos7"
```

`},`

```json
                              "On": false,
                              "Alias": "Tomcat 7",
                              "TypeName": "tomcat7"
```

`},`

```json
                              "On": false,
                              "Alias": "MongoDB",
                              "TypeName": "mongodb-check"
```

`]` `]`

#### 4.5.3 ModifyStrategy

You can call this operation to modify the basic information of a baseline check policy.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyStrategy. |
| CycleDays | String | No | The baseline check cycle. |
| CycleStartTime | String | No | The time when the baseline check starts. Valid values: 0: starts at 00:00 and ends at 06:00. 6: starts at 06:00 and ends at 12:00. 12: starts at 12:00 and ends at 18:00. 18: starts at 18:00 and ends at 24:00. |
| Id | String | No | The ID of the baseline check policy. Not e If this parameter is set to null, a baseline check policy is added. |
| Name | String | No | The name of the baseline check policy. |
| RiskSubTypeName | String | No | The sub-risk types in the baseline check policy. Separate multiple sub-risk types with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Result | Struct | The returned information. For more information, see the following parameter descriptions. |
| StrategyId | Integer | The ID of the baseline check policy. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=ModifyStrategy &CycleDays=1 &CycleStartTime=8 &Id=52 &Name=Web server &RiskSubTypeName=redis_check,linux_password
```

Sample responses (JSON format)

```json
 "RequestId":"161F1BEE-5268-4935-9763-C39A2F7F65DD",
 "Result":2
  "StrategyId":52
```

#### 4.5.4 DeleteStrategy

You can call this operation to delete a specified baseline check policy.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteStrategy. |
| Id | String | No | The ID of the baseline check policy. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DeleteStrategy &Id=123456
```

Sample responses (JSON format)

```json
    "RequestId": "43F670F3-AB40-4E91-BC7D-C57468834F67"
```

#### 4.5.5 DescribeStrategyTarget

You can call this operation to query the information about asset groups to which a specified baseline check policy applies.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeStrategyTarget. |
| Config | String | No | The policy configuration information. The baseline check policy ID is specified in JSON format, for example, {"strategyId":15161} . |
| Type | String | No | The configuration type. Set the value to hcstrategy. _ |
| Target | String | No | The ID of the asset group to which the baseline check policy applies. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Count | Integer | The total number of returned records. |
| StrategyTargets | Array | The information about asset groups to which the policy applies. For more information, see the following parameter descriptions. |

| Name | Type | Description |
|---|---|---|
| Flag | String | Indicates whether the policy applies to the specified asset group. Valid values: add: indicates the whitelist mode, that is, the policy applies to the asset group. del: indicates the blacklist mode, that is, the policy does not apply to the asset group. Not e Generally, the blacklist mode is used for system default policies, and the whitelist mode is used for custom policies. |
| TargetType | String | The return value is fixed to groupId, indicating that the value of the Target parameter is the ID of the asset group. |
| Target | String | The asset group ID. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeStrategyTarget &Config={"strategyId":15161} &Type=hc_strategy
```

Sample responses (JSON format)

```json
        "Count": 1,
        "StrategyTargets":[
                "Flag": "del",
                "Target": "281801",
                "TargetType": "groupId"
```

`]`

```json
 "requestId": "B44F545D-15CF-4A57-B8BF-4340D15D0507"
```

#### 4.5.6 ModifyStrategyTarget

You can call this operation to modify the information about the asset groups that a specified baseline check policy applies to.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyStrategyTarget. |
| Config | String | No | The policy configuration information. The baseline check policy ID is specified in JSON format, for example, {"strategyId":15161} . |
| Type | String | No | The configuration type. Set the value to hcstrategy. _ |
| Target | String | No | The information about asset groups that the baseline check policy applies to. For more information, see the sample request. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=ModifyStrategyTarget &Type=hc_strategy &Config={"strategyId":36071} &Target=[{"targetType":"groupId","target":"1111","flag":"add"}]
```

Sample responses (JSON format)

```json
 "RequestId": "B44F545D-15CF-4A57-B8BF-4340D15D0507"
```

#### 4.5.7 DescribeUuidConfig

You can call this operation to check whether baseline check is enabled for a specified server.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeUuidConfig. |
| Uuid | String | No | The UUID of the server. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Data | Struct | The baseline check configuration. For more information, see the following parameter descriptions. |
| Flag | String | Indicates whether baseline check is enabled. Valid values: add: indicates enabled. del: indicates disabled. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeUuidConfig &uuid=4bc19998-e100-4b04-ab11-1e677418d311
```

Sample responses (JSON format)

```json
    "Data": {
        "Flag": "del"
```

`},`

```json
    "RequestId": "A89978FE-BC35-427E-A4B1-7AEEAE741CC2",
```

#### 4.5.8 ModifyMachineConfig

You can call this operation to configure whether to apply a specified baseline check policy to a specified server.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyMachineConfig. |
| Type | String | No | The configuration type. Set the value to hcswitch, indicating the _ baseline check policy switch. |
| Target | String | No | The specified server, in JSON format. For more information, see the sample request. |
| Config | String | No | The policy configuration information. The baseline check policy ID is specified in JSON format, for example, {"strategyId":15161} . |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=ModifyMachineConfig &target={"targetType":"uuid","target":"2738e842-7d46-42f7-acb4-e6796b051ddc","ip":"x.x.x. x","flag":"del"} &type=hc_switch &config={"strategyId":15161}
```

Sample responses (JSON format)

```json
    "RequestId": "A89978FE-BC35-427E-A4B1-7AEEAE741CC2",
```

#### 4.5.9 DescribeUserSetting

You can call this operation to query the number of days an invalid risk is kept for before it is automatically deleted in baseline check.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeUserSetting. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| InvalidWarningKeepDays | Integer | The number of days that an invalid risk is kept for. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeUserSetting
```

Sample responses (JSON format)

```json
 "InvalidWarningKeepDays":90,
 "RequestId":"0A079FE2-0D1B-4A4D-A4EF-D02B5DDE12A7"
```

#### 4.5.10 CreateUserSetting

You can call this operation to specify the number of days an invalid risk is kept for before it is automatically deleted in baseline check.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateUserSetting. |
| InvalidWarningKee pDays | Integer | No | The number of days an invalid risk is kept for. Valid values: 7: indicates that the invalid risk item is to be deleted in seven days. 30: indicates that the invalid risk item is to be deleted in 30 days. 90: indicates that the invalid risk item is to be deleted in 90 days. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=CreateUserSetting &InvalidWarningKeepDays=90
```

Sample responses (JSON format)

```json
    "RequestId": "43F670F3-AB40-4E91-BC7D-C57468834F67",
```

#### 4.5.11 DescribeRiskWhiteList

You can call this operation to obtain the whitelist of risk items that are exempt from the baseline check.

| Name | Type | Required | Description |
|---|---|---|---|

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeRiskWhiteList. |
| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query output. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |
| RiskName | String | No | The name of the risk item. This parameter supports fuzzy match. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of returned records. |
| Count | Integer | The number of records on the current page. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| WhiteLists | Array | The risk item whitelist. For more information, see the following parameter descriptions. |
| Reason | String | The reason for adding the risk item to the whitelist. |
| RiskId | Long | The ID of the risk item. |
| RiskName | String | The name of the risk item. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeRiskWhiteList &RiskName=SSH logon baseline check
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "PageSize":20,
 "RequestId":"B452E97A-7DFA-44FC-915D-5D590A702846",
 "CurrentPage":1,
 "WhiteLists":[
   "RiskName":"SSH logon baseline check",
   "RiskId":1
```

`],`

```json
 "Count":1
```

#### 4.5.12 BatchDeleteWhiteList

You can call this operation to delete multiple risks from the whitelist for baseline check.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to BatchDeleteWhiteList. |
| RiskIdList | String | No | The ID of the risk to be deleted from the whitelist. Separate multiple IDs with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=BatchDeleteWhiteList &RiskIdList=1,2,3
```

Sample responses (JSON format)

```json
 "RequestId":"E3785090-CFF4-4C53-82E4-08F902586053"
```

#### 4.5.13 CreateUserWhiteList

You can call this operation to add a specified risk to the baseline check whitelist. After this operation, the risk is not reported during baseline check.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateUserWhiteList. |
| RiskIdList | String | No | The ID of the risk to be added to the whitelist. Separate multiple IDs with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=CreateUserWhiteList &RiskIdList=1,2,3
```

Sample responses (JSON format)

```json
 "RequestId":"E3785090-CFF4-4C53-82E4-08F902586053"
```

#### 4.5.14 DescribeStratety

You can call this operation to query the execution details of a specified baseline check policy.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeStratety. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Strategies | Array | The list of baseline check policies. For more information, see the following parameter descriptions. |
| CycleDays | Integer | The execution cycle of the policy. |
| CycleStartTime | Integer | The start time of policy execution. |
| EcsCount | Integer | The number of hosts to which the policy applies. |
| ExecStatus | Integer | The current execution status of the policy. Valid values: 1: indicates that the policy has been executed. 2: indicates that the policy is being executed. |
| Id | Integer | The ID of the policy. |
| Name | String | The name of the policy. |
| ProcessRate | Integer | The progress of policy execution. Unit: percentage. |
| RiskCount | Integer | The number of risk items contained in the policy. |
| ConfigTargets | Array | The asset group to which the policy applies. For more information, see the following parameter descriptions. |

| Name | Type | Description |
|---|---|---|
| Flag | String | Indicates whether the policy applies to the specified asset group. Valid values: add: indicates the whitelist mode, that is, the policy applies to the asset group. del: indicates the blacklist mode, that is, the policy does not apply to the asset group. Not e Generally, the blacklist mode is used for system default policies, and the whitelist mode is used for custom policies. |
| TargetType | String | The return value is fixed to groupId, indicating that the value of the Target parameter is the ID of the asset group. |
| Target | String | The asset group ID. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeStratety
```

Sample responses (JSON format)

```json
        "requestId": "751BEDD8-A16F-49CE-A3C4-605849645D79",
    "Strategies": [
                "Name": "Threat Detection Service No. 12345",
                "RiskCount": 4,
                "CycleDays": 1,
                "CycleStartTime": 6,
                "Type": 2,
                "ProcessRate": 0,
                "ConfigTargets": [
                        "Flag": "add",
                        "Target": "5078483",
                        "TargetType": "groupId"
```

`],`

```json
                "Id": 36071,
                "ExecStatus": 1,
                "EcsCount": 2
```

`]`

#### 4.5.15 DescribeStrategyExecDetail

You can call this operation to query the execution details of a baseline check policy.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeStrategyExecDetail. |
| StrategyId | Integer | No | The ID of the baseline check policy. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| EndTime | String | The time when the baseline check was complete. |
| FailCount | Integer | The number of servers that failed to pass the check. |

| eveloper Guide·Server Gua | rd | Apsara Stack Securit |
|---|---|---|

| Name | Type | Description |
|---|---|---|
| FailedEcsList | Array | A list of servers that failed to pass the check. For more information, see the following parameter descriptions. |
| Ip | String | The IP address of the server. |
| InstanceName | String | The instance name of the server. |
| IntranetIp | String | The private IP address of the server. |
| Reason | String | The reason that causes the baseline check failure. |
| InProcessCount | Integer | The number of servers that are being checked. |
| percent | String | The baseline check progress in percentage. |
| Source | String | The baseline check mode: automatic or manual. |
| StartTime | String | The time when the baseline check started. |
| SuccessCount | Integer | The number of servers that have passed the check. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeStrategyExecDetail &StrategyId=1
```

Sample responses (JSON format)

```json
     "requestId": "751BEDD8-A16F-49CE-A3C4-605849645D79",
       "Source": "Schedule",
       "InProcessCount": 0,
       "SuccessCount": 1,
       "Percent": 100,
       "EndTime": "2018-04-08 12:15:20",
       "FailedEcsList": [],
       "StartTime": "2018-04-08 12:15:10",
       "FailCount": 0,
```

#### 4.5.16 DescribeRiskType

You can call this operation to query all types of risks detected in baseline check and view the number of risks that have been detected by a baseline check policy or on the specified servers for a specific risk type.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeRiskType. |
| StrategyId | Long | No | The ID of the baseline check policy. |
| Uuids | String | No | The UUID of the server. Multiple UUIDs are separated with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Count | Integer | The number of risk types. |
| RiskTypes | Array | A list of risk types. For more information, see the following parameter descriptions. |
| Alias | String | The name of the risk type. |
| TypeName | String | The code of the risk type. |
| WarnCount | String | The number of risks that have been detected. |
| SubTypes | Array | A list of sub-risk types. For more information, see the following parameter descriptions. |
| Alias | String | The name of the sub-risk type. |
| TypeName | String | The code of the sub-risk type. |
| WarnCount | String | The number of risks that have been detected. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeRiskType &StrategyId=10
```

Sample responses (JSON format)

```json
 "RequestId":"11D3993A-02B8-4FD9-9116-922BCDE53A80",
 "RiskTypes":[
   "TypeName":"system",
   "SubTypes":[
     "TypeName":"group_policy",
     "Alias":"Group policy",
     "WarnCount":0
```

`},`

```json
     "TypeName":"baseline",
     "Alias":"Baseline policy",
     "WarnCount":0
```

`},`

```json
     "TypeName":"register",
     "Alias":"Registry",
     "WarnCount":0
```

`],`

```json
   "Alias":"System",
   "WarnCount":0
```

`],`

```json
 "count": 1,
```

#### 4.5.17 Describesummary

You can call this operation to query the risks detected in baseline check by risk type.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to Describesummary. |
| PageSize | Integer | No | The number of records displayed on a page. Default value: 20. |

| Name | Type | Required | Description |
|---|---|---|---|
| CurrentPage | Integer | No | The current page number. Default value: 1. |
| Dealed | String | No | Indicates whether the risk has been handled. Valid values: Y: indicates that the risk has been handled. N: indicates that the risk has not been handled. |
| RiskLevels | String | No | The risk level. Separate multiple risk levels with commas (,). |
| RiskName | String | No | The name of the risk. Not e Fuzzy match is supported. |
| StatusList | String | No | The status of the risk. Valid values: 1: indicates that the risk is pending. 2: indicates that the risk has been ignored. 3: indicates that the risk has been confirmed. 8: indicates that the risk has been marked as a false positive. 16: indicates that the risk is being handled. 32: indicates that the risk has been handled. You can specify multiple statuses and separate them with commas (,). |
| StrategyId | Long | No | The ID of the baseline check policy. |
| TypeNames | String | No | The type of the risk. Separate multiple risk types with commas (,). |
| SubTypeNames | String | No | The type of the sub-risk. Separate multiple sub-risk types with commas (,). |
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The number of returned records. |
| Count | Integer | The number of returned risk records. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| WarningSummarys | Array | A list of risks. For more information, see the following parameter descriptions. |
| LastFoundTime | String | The latest time when the risk was detected. |
| Level | String | The risk level. |
| PendingCount | Integer | The number of pending risks. |
| RiskDetail | String | The risk details. |
| RiskId | Long | The ID of the risk. |
| RiskName | String | The name of the risk. |
| TypeAlias | String | The type of the risk. |
| SubTypeAlias | String | The type of the sub-risk. |
| TotalCount | Integer | The total number of risks. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=Describesummary &CurrentPage=20 &Dealed=Y &PageSize=10 &StrategyId=1 &Uuid=2738e842-7d46-42f7-acb4-e6796b051ddc
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "PageSize":20,
 "RequestId":"38AAFEEE-F52F-4B2E-9F28-FC4A35F8D432",
 "CurrentPage":1,
 "count": 1,
 "WarningSummarys":[
   "RiskId":1,
   "LastFoundTime":"2018-04-08 16:51:26",
   "RiskDetail":"The SSH logon security policy checks the following configurations: \n1.
Checks whether the logon port is the default port 22\n2 and whether the root account is a llowed\n3. Checks whether the SSH V1 protocol is used\n4. Checks whether the RSH protocol is used\n5. Checks whether authentication-based logon is performed\n Solution: \n Edit /e tc/ssh/sshd_config\n1. Port (not 22)\n2. PermitRootLogin (no)\n3. Protocol (2)\n4. Ignore Rhosts (yes)\n5. e) HostbasedAuthentication (no)
   "Level":"low",
   "TypeAlias":"System",
   "SubTypeAlias":"Baseline check policy",
   "RiskName":"SSH logon baseline check"
```

`]`

#### 4.5.18 OperateWarning

You can call this operation to handle the risk alert records detected during the baseline check.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to OperateWarning. |
| RiskWarningIds | String | No | The risk alert record ID. Separate multiple risk alert record IDs with commas (,). |

| Name | Type | Required | Description |
|---|---|---|---|
| OperateType | String | No | The type of the operation. Valid values: verify: indicates an operation to verify the risk alert. ignore: indicates an operation to ignore the risk alert. cancelIgnore: indicates an operation to cancel the ignore operation on the risk alert. delete: indicates an operation to delete the risk alert record. |
| Reason | String | No | The reason why the risk alert record is ignored if the OperateType parameter is set to ignore. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=OperateWarning &OperateType=verify &RiskWarningIds=22,45
```

Sample responses (JSON format)

```json
 "RequestId":"38AAFEEE-F52F-4B2E-9F28-FC4A35F8D432"
```

#### 4.5.19 ExportWarning

You can call this operation to export risks that match the specified criteria from baseline check.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ExportWarning. |
| IsSummaryExport | String | No | Indicates whether to export the summary page. Valid values: 1: exports the summary page. 0: does not export the summary page. |
| Dealed | String | No | Indicates whether the risk has been handled. Valid values: Y: indicates that the risk has been handled. N: indicates that the risk has not been handled. |
| RiskLevels | String | No | The risk level. Multiple risk levels are separated with commas (,). |
| RiskName | String | No | The name of the risk. Not e Fuzzy match is supported. |
| StrategyId | Integer | No | The ID of the baseline check policy. |
| TypeNames | String | No | The risk type. |
| SubTypeNames | String | No | The sub-risk type. |
| Uuids | String | No | The UUID of the server. Multiple UUIDs are separated with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| FileName | String | The name of the exported file. |
| Id | Integer | The ID of the export task. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=ExportWarning &Dealed=n &RiskLevels=serious,high,medium,low &RiskName=Weak FTP password &StrategyId=15161 &SubTypeNames=centos7 &TypeNames=cis &Uuids=6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac
```

Sample responses (JSON format)

```json
     "FileName": "health_check_export_20180306",
     "RequestId": "F2F08DED-C788-430F-91F2-11991818BE2D",
     "Id": 16719
```

#### 4.5.20 DescribeExportInfo

You can call this operation to query the export task information, including the export progress and the download link of the exported file.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeExportInfo. |
| ExportId | Long | No | The ID of the export task. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| CurrentCount | Integer | The number of records that have been exported. |
| FileName | String | The name of the exported file. |
| Id | Integer | The ID of the export task. |
| GmtCreate | Long | The time when the export task was created. |

| psara Stack Security |   | Developer Guide·Server Guar |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| Link | String | The download link of the exported file. |
| Progress | Integer | The export progress. |
| TotalCount | Integer | The total number of records that have been exported. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribeExportInfo &ExportId=1
```

Sample response (JSON format)

```json
    "Link": "http://hc-export.oss-cn-shanghai.example.com/export_hc/health_check_export_2
0180303_1520065303578.zip?Expires=1520670103&OSSAccessKeyId=<yourAccessKeyId>&Signature=x xxx%xxxx%3D",
    "TotalCount": 82,
    "FileName": "health_check_export_20180303",
    "RequestId": "00F89798-3370-4C20-8506-B2BC3970EC5A",
    "CurrentCount": 82,
    "Id": 16678,
    "GmtCreate": 1520065302000,
    "Progress": 100
```

### 4.6 Unusual logon detection

#### 4.6.1 DescribeBaseConfigs

You can call this operation to query the logon security settings.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeBaseConfigs. |

| eveloper Guide·Serve | r Guard |   | Apsara Stack Securit |
|---|---|---|---|

| Name | Type | Required | Description |
|---|---|---|---|
| Type | String | Yes | The type of the logon security configuration record. Valid values: logincommonlocation: indicates an _ _ approved logon location. logincommonip: indicates an _ _ approved logon IP address. logincommontime: indicates an _ _ approved logon time period. logincommonaccount: indicates an _ _ approved logon account. |
| Target | String | No | The specified server. Not e You must specify this parameter to query the logon security settings of a specified server. For more information about the format, see the sample request. |
| PageSize | Integer | No | The maximum number of records to be displayed on each page. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| TotalCount | Integer | The total number of the returned records. |
| BaseConfigs | Array | The logon security settings. For more information, see the following parameter descriptions. |
| Account | String | The approved logon account. |
| EndTime | String | The end time of the approved logon time period. |

| psara Stack Security |   | Developer Guide·Server Guar |
|---|---|---|

| Name | Type | Description |
|---|---|---|
| Ip | String | The approved logon IP address. |
| Location | String | The approved logon location. |
| StartTime | String | The start time of the approved logon time period. |
| TotalCount | Integer | The total number of servers. |
| UuidCount | Integer | The number of servers to which the specified configuration record applies. |
| TargetList | Array | The information about servers to which the specified configuration record applies. For more information, see the following parameter descriptions. |
| TargetType | String | The type of the Target parameter value. Valid values: groupId: indicates an asset group ID. uuid: indicates a server UUID. |
| Target | String | The asset group ID or server UUID. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeBaseConfigs &CurrentPage=1 &PageSize=20 &Target=[{"targetType":"uuid","target":"6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac"}] &Type=login_common_location
```

Sample responses (JSON format)

```json
 "BaseConfigs": [{
  "totalCount": 9,
  "location": "United States",
  "uuidCount": 1,
  "targetList": [{
   "target": "6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac",
   "targetType": "uuid"
```

`}]`

```json
 }],
 "TotalCount": 1,
 "PageSize": 5,
 "RequestId": "485ABE58-4E27-4416-997C-F8F3B8748EB6",
 "CurrentPage": 1
```

#### 4.6.2 ModifyBaseConfig

You can call this operation to modify logon security settings.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyBaseConfig. |
| Type | String | Yes | The type of the logon security settings. Valid values: logincommonlocation: indicates _ _ approved logon locations. logincommonip: indicates approved _ _ logon IP addresses. logincommontime: indicates _ _ approved logon time periods. logincommonaccount: indicates _ _ approved logon accounts. |
| Target | String | No | The target server. Not e You must set this parameter when you need to query the logon security settings for a server. For more information about the format, see the following sample request. |

| Name | Type |   | Required |   | Description |   |   |
|---|---|---|---|---|---|---|---|
| Config | String |   | No |   | The logon security settings. The formats for all the settings are as follows: Approved logon locations: {"locat ion":"Ganzhou City"} Approved logon IP addresses: {"ip" :"x.x.x.x"} Approved logon time periods: {"st |   |   |
|   |   |   |   |   |   | {"st |   |
|   |   |   |   |   | artTime":"16:18","endTime":"16:1 |   |   |
|   |   |   |   |   | 8"} |   |   |

|   | ion":"Ganzhou City"} |
|---|---|

| {"ip" |   |
|---|---|

|   | :"x.x.x.x"} |
|---|---|

| {"accou |   |
|---|---|

|   | nt":"dbaadmin"} |
|---|---|

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=ModifyBaseConfig &Config={"startTime":"16:18","endTime":"16:18"} &Target=[{"targetType":"uuid","target":"0c797eb1-e6b9-4b5a-8917-a7e6cbbb4b2e","flag":"add "},{"targetType":"uuid","target":"1759b0ea-6dd7-438b-b60d-c90179bd9ebc","flag":"del"}] &Type=login_common_location
```

Sample responses (JSON format)

```json
 "RequestId":"BB8F5902-BD50-49AB-B124-18E9CA92BB99"
```

#### 4.6.3 DeleteBaseConfig

You can call this operation to delete a logon security setting, such as an approved logon location or IP address.

| Parameter | Type |   | Required |   | Description |   |
|---|---|---|---|---|---|---|
| Action | String |   | Yes |   | The operation that you want to perform. Set this parameter to DeleteBaseConfig. |   |
| Config | String |   | Yes |   | The logon security setting. The formats of the logon security settings and examples are as follows: Approved logon location: {"locati on":"Ganzhou City"} Approved logon IP address: {"ip": " x.x.x.x"} Approved logon time range: {"star |   |
|   |   |   |   |   | tTime":"16:18","endTime":"16:18" |   |
|   |   |   |   |   | } |   |
| Type | String |   | Yes |   | The type of the logon security setting. Valid values: logincommonlocation: indicates an _ _ approved logon location. logincommonip: indicates an _ _ approved logon IP address. logincommontime: indicates an _ _ approved logon time range. logincommonaccount: indicates an _ _ approved logon account. |   |
| Target | String |   | No |   | The target server. Not e You must set this parameter if you want to delete a logon security setting for a server. For more information about the format, see the following sample request. |   |

|   | on":"Ganzhou City"} |
|---|---|

| {"ip": |   |
|---|---|

|   | " x.x.x.x"} |
|---|---|

| {"accoun |   |
|---|---|

|   | t":"dbaa****"} |
|---|---|

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DeleteBaseConfig &Config={"location":"Ganzhou City"} &Target=[{"targetType":"uuid","target":"6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac"}] &Type=login_common_location
```

Sample response (JSON format)

```json
    "RequestId":"E3785090-CFF4-4C53-82E4-08F902586053"
```

#### 4.6.4 DescribeSwitchConfigs

You can call this operation to query the logon security configuration records in the logon security settings.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSwitchConfigs. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Count | Integer | The total number of returned records. |
| ConfigList | Array | The statuses of the logon security configuration items. For more information, see the following parameter descriptions. |

| Name | Type | Description |
|---|---|---|
| Item | String | The logon security configuration items. Valid values: logincommonlocation: indicates an approved _ _ logon location. logincommonip: indicates an approved logon IP _ _ address. logincommontime: indicates an approved _ _ logon time range. logincommonaccount: indicates an approved _ _ logon account. |
| Status | Integer | The status of the configuration item. Valid values: 1: indicates enabled. 0: indicates disabled. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeSwitchConfigs
```

Sample responses (JSON format)

```json
 "Count":3,
 "RequestId":"3F2C126D-870B-4AE4-8604-58BDECF873F4",
 "ConfigList":[
   "Status":1,
   "Item":"login_common_ip"
```

`},`

```json
   "Status":0,
   "Item":"login_common_account"
```

`},`

```json
   "Status":0,"Item":"login_common_time"
```

`]`

#### 4.6.5 ModifySwitchConfig

You can call this operation to modify the setting about whether to enable a logon security configuration record to identify a valid logon to a server in the logon security settings.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifySwitchConfig. |
| Item | String | Yes | The logon security configuration items. Valid values: logincommonlocation: indicates an _ _ approved logon location. logincommonip: indicates an _ _ approved logon IP address. logincommontime: indicates an _ _ approved logon time range. logincommonaccount: indicates an _ _ approved logon account. |
| Status | Integer | Yes | The status of the logon security configuration switch. Valid values: 1: indicates enabled. 0: indicates disabled. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Count | Integer | The total number of returned records. |
| ConfigList | Array | The status of the logon security configuration switch. For more information, see the following parameter descriptions. |
| Item | String | The logon security configuration items. Valid values: logincommonlocation: indicates an approved _ _ logon location. logincommonip: indicates an approved logon IP _ _ address. logincommontime: indicates an approved _ _ logon time range. logincommonaccount: indicates an approved _ _ logon account. |

| Name | Type | Description |
|---|---|---|
| Status | Integer | The status of the logon security configuration switch. Valid values: 1: indicates enabled. 0: indicates disabled. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=ModifySwitchConfig &Item=login_common_location &Status=1
```

Sample responses (JSON format)

```json
 "RequestId":"3F2C126D-870B-4AE4-8604-58BDECF873F4"
```

#### 4.6.6 DescribeConfigTarget

You can call this operation to query the information about servers to which a specified logon security configuration record applies.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeConfigTarget. |

| Name | Type | Required | Description |
|---|---|---|---|
| Type | String | Yes | The logon security configuration record used to identify a valid logon to a server. Valid values: logincommonlocation: indicates an _ _ approved logon location. logincommonip: indicates an _ _ approved logon IP address. logincommontime: indicates an _ _ approved logon time range. logincommonaccount: indicates an _ _ approved logon account. |
| Target | String | No | The specified server. Not e You need to specify this parameter to query the logon security configuration records of a specified server. For more information about the format, see the sample request. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Count | Integer | The total number of returned records. |
| TargetList | Array | The information about server to which the specified configuration record applies. For more information, see the following parameter descriptions. |
| TargetType | String | The type of the Target parameter value. Valid values: groupId: indicates an asset group ID. uuid: indicates a server UUID. |
| Target | String | The asset group ID or server UUID. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeConfigTarget &Config={"uuidCount":1,"location":"Ganzhou"} &Target=[{"targetType":"uuid","target":"6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac"}] &Type=login_common_location
```

Sample responses (JSON format)

```json
  "TargetList": [{
   "Target": "inet-e53455ec-a134-4d46-9ff5-c4f3a5fe0f02",
   "TargetType": "uuid"
  }, {
   "Target": "inet-25f4ef74-29c7-49fd-85cc-b4543a2489a8",
   "TargetType": "uuid"
 "Count": 2,
 "RequestId": "B8064EA4-9472-4D03-B7D1-6684DB5CD0BE",
```

### 4.7 Webshell detection

#### 4.7.1 DescribeWebPath

You can call this operation to query the Web directories defined in webshell settings.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeWebPath. |
| PageSize | Integer | No | The number of records to return on each page. Default value: 20. |
| CurrentPage | Integer | No | The number of the page to return. Default value: 1. |
| Type | String | No | The type of the settings. Set this parameter to webpath to _ specify the Web directory settings. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The number of returned records. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| Count | Integer | The number of Web directories. |
| ConfigList | Array | The Web directories. For more information, see the following descriptions. |
| WebPath | String | The path of the Web directory. |
| TargetList | Array | The servers that the Web directory has been applied to. For more information, see the following descriptions. |
| TargetType | String | This parameter always returns a value of uuid, which means that the Target parameter returns the universally unique identifier (UUID) of the server. |
| Target | String | The UUID of the server. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribeWebPath
```

Sample response (JSON format)

```json
 "TotalCount":1,
 "PageSize":5,
 "RequestId":"7B6AD7C9-0F8D-4126-B8AA-6DC308B0B534",
 "CurrentPage":1,
 "Count":1,
 "ConfigList":[
   "TargetList":[
     "Target":"inet-f6ac9a93-0818-4052-90e2-d24f18ee198b",
     "TargetType":"uuid"
```

`],`

```json
   "WebPath":"/usr/local/tomcat/webroot18"
```

`]`

#### 4.7.2 ModifyWebPath

You can call this operation to modify the Web directory in webshell settings.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyWebPath. |
| Type | String | No | The configuration type. Set the value to webpath, indicating the _ web directory configuration. |
| Config | String | No | The Web directory configuration, in JSON format. For more information, see the sample request. |
| Target | String | No | The list of target servers to which the Web directory configuration applies, in JSON format. For more information, see the sample request. |

| Name | Type | Description |
|---|---|---|

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=ModifyWebPath &Type=web_path &Config={"webPath":"/test"} &Target={"targetType":"uuid","target":"0c797eb1-e6b9-4b5a-8917-a7e6cbbb4b2e","flag":"add"
```

Sample responses (JSON format)

```json
 "RequestId":"7B6AD7C9-0F8D-4126-B8AA-6DC308B0B534"
```

#### 4.7.3 DescribeCategoryCount

You can call this operation to query the number of webshells detected by Server Guard.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeCategoryCount. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Webshell | Integer | The number of webshells. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeCategoryCount
```

Sample responses (JSON format)

```json
    "RequestId": "43F670F3-AB40-4E91-BC7D-C57468834F67",
    "Webshell": 2
```

#### 4.7.4 DescribeWebshell

You can call this operation to query records of webshell files that have been detected by Server Guard, including the detection time and webshell file path.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeWebshell. |
| GroupId | Integer | No | The ID of the asset group. |
| Mark | String | No | The IP address or instance name of the server. |
| Tag | Integer | No | The server tag ID. |
| Dealed | String | No | The status of the webshell event. Valid values: n: indicates that the event is pending. y: indicates that the event has been handled. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| WebshellList | Array | The webshell events. For more information, see the following descriptions. |
| Os | String | The operating system of the server. |

| psara Stack Security |   | Developer Guide·Server Guar |
|---|---|---|
| Parameter | Type | Description |
| InstanceName | String | The instance name of the server. |
| GroupId | Long | The ID of the asset group. |
| Ip | String | The IP address of the server. Not e The public IP address of the server is displayed preferentially. If no public IP address is assigned to the server, the private IP address of the server is displayed. |
| Uuid | String | The universally unique identifier (UUID) of the server. |
| FoundTime | String | The time when the webshell file was detected. |
| InstanceId | String | The instance ID of the server. |
| TrojanType | String | The type of the webshell file. |
| FirstFoundTime | String | The time when the webshell file was detected for the first time. |
| TrojanSize | Long | The size of the webshell file. |
| Domain | String | The domain name associated with the server. |
| TrojanPath | String | The path of the webshell file. |
| Region | String | The region where the server resides. |
| Status | Integer | The status of the webshell event. Valid values: 1: indicates that the event is pending. 2: indicates that the event has been ignored. 3: indicates that the event has been confirmed. 8: indicates that the event has been labeled as a false positive. 16: indicates that the event is being handled. 32: indicates that the event has been handled. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribeWebshell &Dealed=n &GroupId=1 &Remark=xx.xx.xx.xx &Tag=11
```

Sample response (JSON format)

```json
    "WebshellList": [{
        "Uuid": "aa46dbe9-d35d-4b77-a4d9-10bc6b1b****",
        "FoundTime": "2018-02-27 03:23:18",
        "Ip": "xx.xx.xx.xx",
        "FirstFoundTime": "2017-12-24 03:36:03",
        "Domain": "",
        "TrojanType": "Webshell",
        "InstanceId": "i-bp15xtqydmbujgep****",
        "TrojanPath": "c:/zhb/wamp/wamp/www/My.php",
        "GroupId": 3259405,
        "Os": "windows",
        "Status": 1,
        "Region": "cn-hangzhou-dg-a01",
        "TrojanSize": 0,
        "InstanceName": "win08****"
    }, {
        "Uuid": "aa46dbe9-d35d-4b77-a4d9-10bc6b1bb610",
        "FoundTime": "2017-12-25 03:53:22",
        "Ip": "x.x.x.x",
        "FirstFoundTime": "2017-12-24 03:36:01",
        "Domain": "",
        "TrojanType": "Webshell",
        "InstanceId": "i-bp15xtqydmbujgepdbev",
        "TrojanPath": "c:/zhb/wamp/../wamp/wamp/www/abc/My.php",
        "GroupId": 3259405,
        "Os": "windows",
        "Status": 9,
        "Region": "cn-hangzhou-dg-a01",
        "TrojanSize": 0,
        "InstanceName": "win08-zhb"
    }],
    "RequestId": "E4B254AE-5CB1-4810-8B51-A08DF5697F25"
```

#### 4.7.5 OperateTrojan

You can call this operation to handle detected webshells.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to OperateTrojan. |
| Info | String | No | The webshell information, in JSON format. For more information, see the sample request. |
| OperateType | String | No | The type of the operation. Valid values: isolate: indicates an operation to quarantine the file. trust: indicates an operation to trust the file. untrust: indicates an operation to cancel trusting the file. restore: indicates an operation to restore the file. |
| Type | Integer | No | The type of the trojan. Set the value to 1. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| FailedCount | Integer | The number of failed operations. |
| SuccessCount | Integer | The number of successful operations. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=OperateTrojan &Info=[{"uuid":"97988c2b-de9d-4159-90ab-7cc73561c64c","filePath":"/home/test/Z02.php","we bshellId":""}] &OperateType=trust &Type=1
```

Sample responses (JSON format)

```json
    "RequestId": "43F670F3-AB40-4E91-BC7D-C57468834F67",
    "FailedCount": 0,
    "SuccessCount": 1
```

#### 4.7.6 DescribeQuaraFile

You can call this operation to obtain the list of quarantined files.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeQuaraFile. |
| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query result. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of returned records. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| QuaraFiles | Array | The list of quarantined files. For more information, see the following parameter descriptions. |
| EventName | String | The name of the unusual event. |
| EventType | String | The type of the unusual event. |

| Name | Type | Description |
|---|---|---|
| FileStatus | String | The status of the quarantined file. Valid values: quaraFailed("0"): indicates that the file failed to be quarantined. rollbackFailed("1"): indicates that the file failed to be rolled back to a previous version. quaraDone("2"): indicates that the file has been quarantined. rollbackDone("3"): indicates that the file has been rolled back to a previous version. quaraing("4"): indicates that the file is being quarantined. rollbacking("5"): indicates that the file is being rolled back to a previous version. |
| Md5 | String | The MD5 value of the file. |
| Online | Boolean | Indicates whether the Server Guard agent on the server is online. |
| Path | String | The file path. |
| Tag | String | The unique identifier of the unusual event. |
| Uuid | String | The UUID of the server. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeQuaraFile
```

Sample responses (JSON format)

```json
    "TotalCount":1,
    "PageSize":20,
    "RequestId":"0C7FAD74-83FA-4671-9250-A5F2A64F437A",
    "CurrentPage":1,
    "QuaraFiles":[
            "Path":"/bin/ping",
            "Uuid":"9b0c4d55-2f1f-4766-a90a-2c9d8a0b7642",
            "FileStatus":"quaraDone",
            "EventType":"Parent class of cloud scanning events (test ping)",
            "EventName":"Sub-class of cloud scanning events (test ping)",
            "Tag":"1d791175ad0bffd973b039248d6086e0",
            "Online":false,
            "Md5":"1421d9ad2b0031483f396154d48161f1"
```

`]`

#### 4.7.7 RollbackQuaraFile

You can call this operation to restore a specified quarantined file.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to RollbackQuaraFile. |
| EventName | String | No | The name of the unusual event. |
| EventType | String | No | The type of the unusual event. |
| Tag | String | No | The GUID of the unusual event. |
| Uuid | String | No | The UUID of the server. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=RollbackQuaraFile &EventName=DDoS trojan &EventType=Malicious process &Tag=a50f96f958fbd59f68e4bca4d90679d6 &Uuid=00f11fcb-1a9a-4fd5-a48a-e0e5bd12a6a4
```

Sample responses (JSON format)

```json
 "RequestId":"0C7FAD74-83FA-4671-9250-A5F2A64F437A",
```

### 4.8 Exception detection on hosts

#### 4.8.1 DescribeSuspEventTypes

You can call this operation to query the unusual event types.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSuspEventTypes. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of returned records. |
| EventTypes | Array | The list of unusual event types. For more information, see the following parameter descriptions. |
| AliseEventType | String | The name of the unusual event type. |
| EventType | String | The identifier of the unusual event type. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeSuspEventTypes
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "RequestId":"66BE7091-BC00-4943-8A0D-B3DCE90AD7B5",
 "EventTypes":[
   "EventType":"Suspicious process",
   "AliseEventType":"Suspicious process"
```

`]`

#### 4.8.2 DescribeSuspTrendStatistics

You can call this operation to query the chart data on different types of unusual server events on each day.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSuspTrendStatistics. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Interval | Integer | The time length of the the time frame specified for query. |
| StartTime | Integer | The start time of the time frame specified for query. |
| SuspiciousItems | List | The statistics on numbers of different types of suspicious events. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeSuspTrendStatistics
```

Sample responses (JSON format)

```json
 "RequestId":"66BE7091-BC00-4943-8A0D-B3DCE90AD7B5",
 "Start":-28800000,
 "Interval":86400000,
 "SuspiciousItems":[ ]
```

#### 4.8.3 OperateSuspiciousEvent

You can call this operation to handle detected unusual events.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to OperateSuspiciousEvent. |
| Data | String | No | The unusual event to be handled, in JSON format. For more information, see the sample request. |
| OperateType | String | No | The type of the operation. Valid values: deal: indicates an operation to handle the unusual event. confirm: indicates an operation to mark the unusual event as handled. markmisinformation: indicates an _ operation to mark the unusual event as false positive. unmarkmisinformation: indicates an _ operation to remove the false positive mark of the unusual event. ignore: indicates an operation to ignore the unusual event. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=OperateSuspiciousEvent &OperateType=ignore &Data={"uuid":"97988c2b-de9d-4159-90ab-7cc73561c64c","tag":"f87eb0ee5934f6f65343ec601ce71 c2f","eventType":"Malicious processes (malware checking)","eventName":"DDoS Trojan},{"uui d":"97988c2b-de9d-4159-90ab-7cc73561c64c","tag":"95347a77b8c0d6dae99a23ab69aa90f4","event Type":"Malicious processes (malware checking)","eventName":"GateDDoS Trojan"}
```

Sample responses (JSON format)

```json
 "RequestId":"654A6FD8-B55D-4D6B-AAFF-4122503D108B"
```

#### 4.8.4 OperateLoginLog

You can call this operation to label a detected unusual logon event as handled.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to OperateLoginLog. |
| Ids | String | Yes | The ID of the unusual logon log. Separate multiple log IDs with commas (,). |
| OperateType | String | Yes | The type of the operation. Set the value to confirm, indicating that the event has been handled. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=OperateLoginLog &Ids=2006434 &OperateType=confirm
```

Sample responses (JSON format)

```json
 "RequestId":"BE391ABB-6B7C-4C41-9F6C-862C1DEE3905"
```

#### 4.8.5 CreateSuspiciousExport

You can call this operation to export the information about unusual events on servers based on search conditions.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateSuspiciousExport. |
| Dealed | String | No | Indicates whether the unusual event has been handled. Valid values: Y: indicates that the event has been handled. N: indicates that the event has not been handled. |
| EventNameRemark | String | No | The name of the event. Fuzzy matching is supported. |

| Name | Type | Required | Description |
|---|---|---|---|
| EventType | String | No | The name of the event type. Valid values: Unusual logon Suspicious process Suspicious account Sensitive file tampering Suspicious network connection Unusual event Suspicious file Malicious process |
| GroupId | String | No | The ID of the asset group. |
| Level | String | No | The risk level of the event. Valid values: Critical: indicates a critical-risk event. Important: indicates an important-risk event. Moderate: indicates a moderate-risk event. low: indicates a low-risk event. You can specify multiple event levels and separate them with commas (,). |
| Remark | String | No | The name or IP address of the server. Fuzzy matching is supported. |
| StatusList | String | No | The handling status of the event. Valid values: 1: indicates that the event is to be handled. 2: indicates that the event has been ignored. 3: indicates that the event has been confirmed. 8: indicates that the event has been labeled as a false positive. 16: indicates that the event is being handled. 32: indicates that the event has been handled. You can specify multiple statuses and separate them with commas (,). |
| Tag | String | No | The tag of the server. |
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| FileName | String | The name of the exported file. |
| Id | Long | The ID of the export task. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=CreateSuspiciousExport &Remark=23 &EventType=Suspicious process &Level=serious,high,medium,low &Dealed=n
```

Sample responses (JSON format)

```json
    "RequestId": "43F670F3-AB40-4E91-BC7D-C57468834F67",
    "FileName": "suspicious_20180408",
    "Id": 387
```

#### 4.8.6 DescribeSuspiciousExportInfo

You can call this operation to query an unusual event export task.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeSuspiciousExportInfo. |
| ExportId | Long | No | The ID of the export task. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| CurrentCount | Integer | The number of records that have been exported. |
| ExportStatus | String | The status of the export task. Valid values: init: indicates that the export task is being initialized. pending: indicates that the export task is pending. exporting: indicates that the export task is being executed. success: indicates that the export task has been completed. fail: indicates that the export task has failed. |
| Message | String | The status description or failure information of the export task. |
| FileName | String | The name of the exported file. |
| Id | Integer | The ID of the export task. |
| GmtCreate | Long | The time when the export task was created. |
| Link | String | The download link of the exported file. |
| Progress | Integer | The export progress. |
| TotalCount | Integer | The total number of records that have been exported. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribeSuspiciousExportInfo &ExportId=1
```

Sample response (JSON format)

```json
 "TotalCount":30,
 "GmtCreate":1518071546000,
 "Progress":100,
 "Message":"success",
 "RequestId":"654A6FD8-B55D-4D6B-AAFF-4122503D108B",
 "FileName":"suspicious_20180208",
 "ExportStatus":"success",
 "CurrentCount":30,
 "Id":11,
 "Link":"http://suspicious-export.oss-cn-shanghai.example.com/export/suspicious_20180208_
1518071576098.zip?Expires=1518075176&OSSAccessKeyId=<yourAccessKeyId>&Signature=xxxx%xxxx %3D"
```

#### 4.8.7 DescribeVirusInfo

You can call this operation to upload the MD5 values of files and use Alibaba Cloud Antivirus to determine whether the files are malicious programs.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVirusInfo. |
| Md5 | String | Yes | The MD5 value of the file. |
| Lang | String | No | The language attribute of the file, such as zh. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Data | Boolean | Indicates whether the file is malicious. Valid values: True: Indicates that the file is malicious. False: Indicates that the file is not malicious. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].aliyuncs.com/?Action= DescribeVirusInfo &Md5=6f6628d923f9018b28acc5f905e03244
```

Sample responses (JSON format)

```json
 "RequestId": "A2423F39-3272-4491-804E-D0EBDE3E894D",
 "Data": true
```

### 4.9 Retrieval of host logs

#### 4.9.1 CreateLogQuery

You can call this operation to create or save server log search conditions.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateLogQuery. |
| Conditions | String | No | The log search condition. |
| QueryDetail | String | No | The log search sub-conditions. |
| QueryName | String | No | The saved search name. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=CreateLogQuery &Conditions=aegis-log-login@warn_port:22 &QueryDetail=[[{"itemForm":{},"d":{"name":"Logons","id":"aegis-log-login","fields":[{"nam e":"ip","type":"string","desc":"IP address","text":"IP(IP address)"}]] &QueryName=test
```

Sample responses (JSON format)

```json
 "RequestId":"415AE1FC-3C11-4AA9-A06F-DE13D3430366"
```

#### 4.9.2 DescribeLogQuery

You can call this operation to query the saved server log search conditions.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeLogQuery. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| ListTotal | Integer | The total number of returned records. |
| QueryItems | Array | The details of log search conditions. For more information, see the following parameter descriptions. |
| Conditions | String | The log search conditions. |
| QueryDetail | String | The log search sub-conditions. |
| QueryName | String | The name of the log search task. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeLogQuery
```

Sample responses (JSON format)

```json
 "RequestId":"65802B9B-4D30-40F0-8691-F126652DBEBE",
 "ListTotal":1,
 "QueryItems":[
   "QueryDetail":"[[{\"itemForm\":{},\"d\":{\"name\":\"Account snapshot\",\"id\":\"aegis-
snapshot-host\",\"fields\":[{\"name\":\"ip\",\"type\":\"string\",\"desc\":\"IP address\"} ,{\"name\":\"uuid\",\"type\":\"string\",\"desc\":\"Client ID\"},{\"name\":\"perm\",\"type \":\"string\",\"desc\":\"Root permission availability\"},{\"name\":\"home_dir\",\"type\": \"string\",\"desc\":\"Home directory\"},{\"name\":\"warn_time\",\"type\":\"string\",\"des c\":\"Password expiration reminder time\"},{\"name\":\"groups\",\"type\":\"array\",\"desc \":\"User group\"},{\"name\":\"login_ip\",\"type\":\"string\",\"desc\":\"Last logon IP\"} ,{\"name\":\"last_chg\",\"type\":\"string\",\"desc\":\"Last password change time\"},{\"na me\":\"shell\",\"type\":\"string\",\"desc\":\"Linux shell command\"},{\"name\":\"domain\" ,\"type\":\"string\",\"desc\":\"Windows domain\"},{\"name\":\"tty\",\"type\":\"string\",\ "desc\":\"Logon terminal\"},{\"name\":\"account_expire\",\"type\":\"string\",\"desc\":\"A ccount expiration time\"},{\"name\":\"passwd_expire\",\"type\":\"string\",\"desc\":\"Pass word expiration time\"},{\"name\":\"last_logon\",\"type\":\"string\",\"desc\":\"Last logo n time\"},{\"name\":\"user\",\"type\":\"string\",\"desc\":\"User\"},{\"name\":\"status\", \"type\":\"string\",\"desc\":\"User status: 0-disabled, 1-enabled\"}]},\"searchFields\":[ {\"name\":\"ip\",\"type\":\"string\",\"desc\":\"IP address\"},{\"name\":\"uuid\",\"type\" :\"string\",\"desc\":\"Client ID\"},{\"name\":\"perm\",\"type\":\"string\",\"desc\":\"Roo t permission availability\"},{\"name\":\"home_dir\",\"type\":\"string\",\"desc\":\"Home d irectory\"},{\"name\":\"warn_time\",\"type\":\"string\",\"desc\":\"Password expiration re minder time\"},{\"name\":\"groups\",\"type\":\"array\",\"desc\":\"User group\"},{\"name\" :\"login_ip\",\"type\":\"string\",\"desc\":\"Last logon IP\"},{\"name\":\"last_chg\",\"ty pe\":\"string\",\"desc\":\"Last password change time\"},{\"name\":\"shell\",\"type\":\"st ring\",\"desc\":\"Linux shell command\"},{\"name\":\"domain\",\"type\":\"string\",\"desc\ ":\"Windows domain\"},{\"name\":\"tty\",\"type\":\"string\",\"desc\":\"Logon terminal\"}, {\"name\":\"account_expire\",\"type\":\"string\",\"desc\":\"Account expiration time\"},{\ "name\":\"passwd_expire\",\"type\":\"string\",\"desc\":\"Password expiration time\"},{\"n ame\":\"last_logon\",\"type\":\"string\",\"desc\":\"Last logon time\"},{\"name\":\"user\" ,\"type\":\"string\",\"desc\":\"User\"},{\"name\":\"status\",\"type\":\"string\",\"desc\" :\"User status: 0-disabled, 1-enabled\"}],\"f\":{\"name\":\"ip\",\"type\":\"string\",\"de sc\":\"IP address\"},\"searchLimit\":[{\"name\":\"Including\",\"value\":\":\"}],\"l\":\": \",\"kw\":\"string\"}]]",
   "Conditions":"aegis-snapshot-host@ip:string",
   "QueryName":"aa"
```

`]`

#### 4.9.3 DeleteLogQuery

You can call this operation to delete the saved server log search conditions.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteLogQuery. |
| QueryName | String | No | The name of the saved search. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DeleteLogQuery &QueryName=test
```

Sample responses (JSON format)

```json
 "RequestId":"415AE1FC-3C11-4AA9-A06F-DE13D3430366"
```

#### 4.9.4 DescribeFilterFields

You can call this operation to query the filter fields of a specified server log search condition.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeFilterFields. |
| Query | String | No | The log search condition. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Total | String | The total number of search conditions. |
| LogFilterList | Array | The filter field information. For more information, see the following parameter descriptions. |
| Fields | String | The filter fields. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeFilterFields &Query=aegis-log-login@warn_port:22
```

Sample responses (JSON format)

```json
 "LogFilterList":[
   "Fields":"IP;IP address,UUID;Client ID","fieldsName":"default"
```

`],`

```json
 "Total":"20",
 "RequestID":"883e1e3d-4443-4206-871c-6c0625c01332"
```

#### 4.9.5 DescribeHistogram

You can call this operation to obtain the statistics on server logs generated within a specified time frame.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeHistogram. |
| Query | String | Yes | The log query conditions. |

| psara Stack Security |   |   | Developer Guide·Server Guar |
|---|---|---|---|

| Name | Type | Required | Description |
|---|---|---|---|
| EndTime | String | Yes | The end time of the time frame specified for query. |
| StartTime | String | Yes | The start time of the time frame specified for query. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Categories | String | The timeline information. |
| Items | Array | The log quantity statistics. For more information, see the following parameter descriptions. |
| Data | List | The number of logs. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeHistogram &EndTime=2018-03-03 17:41:03 &Query=aegis-log-login@warn_port:22 &StartTime=2018-03-02 17:41:03
```

Sample responses (JSON format)

```json
 "RequestId":"82D245FB-7A5D-4155-B59F-5B084CE93B6B",
 "Categories":[
  "1519983663000,1519984800000",
  "1519984800000,1519986600000",
  "1519986600000,1519988400000",
  "1519988400000,1519990200000",
  "1519990200000,1519992000000",
  "1519992000000,1519993800000",
  "1519993800000,1519995600000"
```

`],`

```json
 "Items":[
   "Data":[
```

`0,` `0,` `0,` `0,` `0,` `0,` `]` `]`

#### 4.9.6 DescribeLogInfo

You can call this operation to query the server log fields based on specified query conditions.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeLogInfo. |
| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query result. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |
| Query | String | Yes | The log query conditions. |

| psara Stack Security |   |   | Developer Guide·Server Guar |
|---|---|---|---|

| Name | Type | Required | Description |
|---|---|---|---|
| EndTime | String | Yes | The end time of the query. |
| StartTime | String | Yes | The start time of the query. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of returned records. |
| LogInfoItems | Array | The information about server log fields. For more information, see the following parameter descriptions. |
| Id | String | The ID of the log source. |
| Name | String | The name of the log source. |
| Fields | Array | The list of server log fields. For more information, see the following parameter descriptions. |
| Name | String | The ID of the log field. |
| Desc | String | The name of the log field. |
| Type | String | The type of the log field. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeLogInfo &CurrentPage=1 &EndTime=2018-03-03 17:41:03 &PageSize=20 &Query=aegis-log-login@warn_port:22 &StartTime=2018-03-02 17:41:03
```

Sample responses (JSON format)

```json
    "TotalCount":1,
    "RequestId":"3A7CFB73-C24C-4711-B7D9-2BE74EBFFE78",
    "LogInfoItems":[
            "Fields":[
                    "Desc":"IP address",
                    "Type":"string",
                    "Name":"ip"
```

`},`

```json
                    "Desc":"Client number",
                    "Type":"string",
                    "Name":"uuid"
```

`},`

```json
                    "Desc":"Logon source IP address",
                    "Type":"string",
                    "Name":"warn_ip"
```

`},`

```json
                    "Desc":"Logon port",
                    "Type":"string",
                    "Name":"warn_port"
```

`},`

```json
                    "Desc":"Logon username",
                    "Type":"string",
                    "Name":"warn_user"
```

`},`

```json
                    "Desc":"Logon type",
                    "Type":"string",
                    "Name":"warn_type"
```

`},`

```json
                    "Desc":"Logon count",
                    "Type":"string",
                    "Name":"warn_count"
```

`],`

```json
            "Id":"aegis-log-login",
            "Name":"Logon serial number"
```

`},` `]`

#### 4.9.7 DescribeLogItems

You can call this operation to query the server log details that are returned by a query.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeLogItems. |
| PageSize | Integer | No | The number of records displayed on a page. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |
| Query | String | No | The log query criterion. |
| AccountSnapshot Offset | Integer | No | The offset of the account snapshot log. |
| CrackOffset | Integer | No | The offset of the brute force password cracking log. |
| LoginOffset | Integer | No | The offset of the logon log. |
| NetworkOffset | Integer | No | The offset of the network connection log. |
| PortSnapshotOffs et | Integer | No | The offset of the listening port snapshot log. |
| ProcessOffset | Integer | No | The offset of the process startup log. |
| ProcessSnapshotO ffset | Integer | No | The offset of the process snapshot log. |
| EndTime | String | Yes | The end time of the time frame specified for query. |
| StartTime | String | Yes | The start time of the time frame specified for query. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The number of returned records. |

| eveloper Guide·Server Gua | rd | Apsara Stack Securit |
|---|---|---|

| Name | Type | Description |
|---|---|---|
| CurrentPage | Integer | The current page number. |
| SetPageSize | Integer | The maximum number of records displayed on a page. |
| AccountSnapshotOffset | Integer | The offset of the account snapshot log. |
| AccountSnapshotTotalC ount | Integer | The total number of account snapshot log entries. |
| CrackOffset | Integer | The offset of the brute force password cracking log. |
| CrackTotalCount | Integer | The total number of brute force password cracking log entries. |
| LoginTotalCount | Integer | The total number of logon log entries. |
| NetworkOffset | Integer | The offset of the network connection log. |
| NetworkTotalCount | Integer | The total number of network connection log entries. |
| PortSnapshotOffset | Integer | The offset of the listening port snapshot log. |
| PortSnapshotTotalCoun t | Integer | The total number of listening port snapshot log entries. |
| ProcessOffset | Integer | The offset of the process startup log. |
| ProcessTotalCount | Integer | The total number of process startup log entries. |
| ProcessSnapshotOffset | Integer | The offset of the process snapshot log. |
| ProcessSnapshotTotalC ount | Integer | The total number of process snapshot log entries. |
| LogsList | Array | A list of host log details. For more information, see the following parameter descriptions. |
| LogSourceID | String | The ID of the log source. |
| LogSource | String | The name of the log source. |
| MLogTime | String | The time when the log entry was created. |
| MContents | Array | A list of host log entries. For more information, see the following parameter descriptions. |
| MKey | String | The log entry. |
| MValue | String | The value of the log entry. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeLogItems &CurrentPage=1 &PageSize=100 &AccountSnapshotOffset=1000 &CrackOffset=1000 &EndTime=2018-03-05 11:46:07 &LoginOffset=1000 &NetworkOffset=1000 &PortSnapshotOffset=1000 &ProcessOffset=1000 &ProcessSnapshotOffset=1000 &Query=aegis-log-login@warn_port:22 &StartTime=2018-03-02 17:41:03
```

Sample responses (JSON format)

```json
 "RequestId":"BE391ABB-6B7C-4C41-9F6C-862C1DEE3905",
 "PageSize":100,
 "AccountSnapshotTotalCount":0,
 "LogsList":[],
 "CrackOffset":0,
 "ProcessOffset":0,
 "NetworkOffset":0,
 "ProcessSnapshotOffset":0,
 "LoginTotalCount":0,
 "CurrentPage":1,
 "PortSnapshotOffset":0,
 "NetworkTotalCount":0,
 "AccountSnapshotOffset":0,
 "CrackTotalCount":0,
 "PortSnapshotTotalCount":0,
 "ProcessSnapshotTotalCount":0,
 "ProcessTotalCount":0
```

## 5 Anti-DDoS

### 5.1 List of operations

This topic introduces all the Apsara Stack Security Anti-DDoS operations that you can call. For more information, see the corresponding operation description.

| Operation | Description |
|---|---|
| CheckIpSegment | Checks whether a CIDR block to be added for monitoring is valid. |
| DescribeRegionName | Queries the regions of the CIDR blocks where traffic data collection and analysis is performed. |
| CreateIpSegment | Adds a specified CIDR block to be monitored. |
| DescribeIpSegment | Obtains a list of CIDR blocks under traffic monitoring. |
| DeleteIpSegment | Deletes a CIDR block whose traffic is collected and monitored based on the CIDR block record ID. |
| ModifyIpSegment | Modifies a monitored CIDR block with a specified record ID. |
| CreateDdosPolicy | Adds an anti-DDoS policy for a specified IP address or CIDR block. |
| DescribeDdosPolicies | Queries the configured DDoS protection policies. |
| DeleteDdosPolicy | Deletes an anti-DDoS policy for a specified CIDR block. |
| ModifyDdosPolicy | Modifies a specified anti-DDoS policy. |
| DescribeBlockSwitchs | Queries the status of the traffic block switch in anti-DDoS. |
| ModifyBlockSwitchs | Changes the status of the block switch in DDoS settings. |
| DescribeDdosEvents | Obtains the list of DDoS events that meet the specified search criteria. |
| DescribeFlowAnalysisResult | Queries the analysis result of the traffic sent to an IP address. |
| DescribeFlowDetails | Queries the detailed traffic information for a specified IP address. |
| CancelCleanStatus | Disables DDoS traffic scrubbing for a specified IP address. |
| CreateWhiteList | Adds a whitelist of trusted IP addresses that are exempt from traffic security monitoring. |
| DescribeWhiteList | Queries the IP addresses that have been added to a whitelist. |

| A | psara Stack Security | Developer Guide·Anti-DDo | S |
|---|---|---|---|

| Operation | Description |
|---|---|
| DeleteWhiteList | Deletes multiple risks from the whitelist for baseline check. |
| DescribeConsoleDdosPolicies | Obtains the records of anti-DDoS policies, including the system default policies. |

### 5.2 Make API requests

#### 5.2.1 Request structure

Apsara Stack Security API is based on Remote Procedure Call (RPC). This topic describes the structure of the API requests. You can send an HTTP request to call an API operation. The URL of the request must be in the following format:

```
http://endpoint/?Action=xx&parameters
```

Where:

|   | endpoint |   | : the endpoint used to ca |
|---|---|---|---|
| osprivate.[ RegionId].example.com |   |   |   |
|   | Action | : the operation that you wa |   |

`endpoint` : the endpoint used to call a cloud service. The endpoint for the Anti-DDoS service is `dd` For example, you can set this parameter to DescribeFeatures to query the deployed Apsara Stack Security features. `parameters` : the request parameters. Request parameters include common request parameters and custom request parameters. Request parameters must be separated with ampersands (&). Common request parameters include information such as the API version and authentication information. For more information about the custom request parameters, see the corresponding operation description. Call the DescribeFeatures operation to query the deployed Apsara Stack Security features.

```
https://yundunprivate.[ RegionId].example.com/?Action=DescribeFeatures&AccessKeyId=key-test &Format=JSON&SecureTransport=true&SignatureMethod=HMAC-SHA1&SignatureNonce=15215528852396&S ignatureVersion=1.0&SourceIp=1xxxx6&Timestamp=2018-03-02Txxxxxxx&Version=2018-01-16&Signatu re=xxxx%xxxx%3D
```

API requests are presented in the following easy-to-read format in this document:

```
https://yundunprivate.[ RegionId].example.com/?Action=DescribeFeatures &Format=JSON &Version=2018-01-16 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2012-06-01T12:00:00Z
```

#### 5.2.2 Signature mechanism

Apsara Stack Security authenticates each access request. You need to include a signature for the submitted HTTP or HTTPS request. API authorization To ensure the security of your account, we recommend that you use a Resource Access Management (RAM) user to call API operations. Before using a RAM user to call an API operation, you must grant the RAM user the corresponding permission to call the API by creating an authorization policy and attaching the policy to the RAM user. API signature To ensure secure calls to the API, Alibaba Cloud authenticates each API request through the signature. When you manually make an API request, you need to use AccessKey Secret to calculate the signature, that is, the hash-based message authentication code (HMAC) value, based on the encoded and sorted request string. For more information, see the definition in RFC 2104. This topic uses the raw access parameters in the following table to describe how to create an API signature.

| Parameter | Description |
|---|---|
| Access point | http://semawaf.[ RegionId].example.com/? |
| API-specific parameters | Action=DescribeFeatures |
| Common parameters (excluding the Signature parameter) | &Timestamp=2016-02-23T12:46:24Z &Format=JSON &AccessKeyId=<yourAccessKeyId> &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2018-01-16 &SignatureVersion=1.0 |
| AccessKey secret | <yourAccessKeySecret> |

1. Use the request parameters to construct a canonicalized query string.
Not e The request parameters include common request parameters (excluding the Signature parameter) and API-specific parameters. i. Sort the parameters. Sort the request parameters in alphabetical order. ii. Encode the parameters. Use UTF-8 to URL-encode the parameter names and values. The encoding rules are as follows: Letters, digits, hyphens (-), underscores (_), periods (.), and tildes (~) are not encoded. Other characters are encoded in the %XY format, where XY is the hexadecimal representation of the character in ASCII. For example, the double quotation mark (") is encoded as %22. Extended UTF-8 characters are encoded in the %XY%ZA… format. Note that a space is encoded as %20, instead of a plus sign (+). iii. Connect the encoded parameter names and values with equal signs (=). iv. Then, sort the parameter name and value pairs connected by equal signs in alphabetical order, and connect them with ampersands (&) to produce the canonicalized query string.
2. Use the canonicalized query string to construct the string for signature calculation based on the
following rules:

```
StringToSign=HTTPMethod + “&” + percentEncode(“/”) + ”&” + percentEncode(CanonicalizedQueryString)
```

3. Calculate the HMAC value of the StringToSign string according to the definition in RFC 2104.
Not e The key used for signature calculation is your AccessKey secret adding the ampersand (&) (ASCII 38). Secure Hash Algorithm 1 (SHA1) is used as the hash algorithm.
4. Encode the preceding HMAC value into a string based on Base64 encoding rules to obtain the
signature value.

```
LEW8N4y7Uasop******
```

5. Set the Signature parameter in the request parameters to this signature value to sign the request.

#### 5.2.3 Common request parameters

The following table describes the common request parameters that are used to indicate information such as the API version and authentication information.

| Name | Type | Required | Description |
|---|---|---|---|
| Version | String | Yes | The API version in the format of YYYY- MM-DD. Set the value to 2018-01-16. |

| Name | Type | Required | Description |
|---|---|---|---|
| AccessKeyId | String | Yes | The key ID that Alibaba Cloud assigns to a user for service access. |
| Signature | String | Yes | The signature string. |
| SignatureMethod | String | Yes | The signature method. Set the value to HMAC-SHA1. |
| Timestamp | String | Yes | The timestamp of the request. Follow the ISO 8601 standard to specify the date and use the offset from Coordinated Universal Time (UTC) to specify the time zone. The format is YYYY-MM- DDThh:mm:ssZ . For example, 2014-05-26T12:00:00Z indicates 20:00:00 on May 26, 2014, Beijing time. |
| SignatureVersion | String | Yes | The signature algorithm version. Set the value to 1.0. |
| SignatureNonce | String | Yes | The unique random number used to prevent network replay attacks. You must use different random numbers for different requests. |
| ResourceOwnerAc count | String | No | The owner account of the resource to be accessed through this API request, that is, the logon username. |
| Format | String | No | The format of the response. Set the value to JSON or XML. Not e Default value: XML. |

|   |   | YYYY-MM- |
|---|---|---|
|   | DDThh:mm:ssZ |   |

#### 5.2.4 Response structure

Apsara Stack Security API responses support both the XML and JSON formats. The system always returns a unique identification code RequestId each time you send a request to call an operation, no matter whether the call is successful or not. Sample responses (XML format)

```xml
<? xml version="1.0" encoding="UTF-8"? > <! -- The root node of the result --> <Operation name+Response>
    <! -- Returned request ID -->
    <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
    <! -- Returned data -->
</Operation name+Response>
```

Sample responses (JSON format)

```json
"RequestId": "4C467B38-3910-447D-87BC-AC049166F216", /* Returned data */
```

### 5.3 APIs

#### 5.3.1 CheckIpSegment

You can call this operation to check whether a CIDR block to be added for monitoring is valid. If a success result is returned through this API, the CIDR block specified in the request can be added.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CheckIpSegment. |
| IpSegmentName | String | Yes | The CIDR block to be checked, in x.x.x.x/x format. For example, 172.21.23.222/24. |
| InfoType | String | No | The CIDR block information type. For example, a value of distribution indicates the region information. |
| InfoName | String | No | The information describing the CIDR block based on the value of the InfoType parameter. For example, if the InfoType parameter is set to distribution, you can set the InfoName parameter to DXJF, indicating that the CIDR block belongs to the region where the Daxing IDC is located. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://ddosprivate.[ RegionId].example.com/?Action=CheckIpSegment &IpSegmentName=192.1.1.1/24 &InfoType=distribution &InfoName=DXJF
```

Sample responses (JSON format)

```json
 "RequestId":"71064826-726F-4ADA-B879-05D8055476FB"
```

#### 5.3.2 DescribeRegionName

You can call this operation to query the regions of the CIDR blocks where traffic data collection and analysis is performed.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeRegionName. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| RegionNameList | Array | A list of regions. For more information, see the following parameter descriptions. |
| Id | Integer | The ID of the region. |

| A | psara Stack Security |   | Developer Guide·Anti-DDo | S |
|---|---|---|---|---|

| Name | Type | Description |
|---|---|---|
| Description | String | The region of the CIDR block. |
| CodeType | String | The type of the CIDR block information. For example, distribution indicates the region information. |
| Code | String | This parameter is used with the CodeType parameter to specify the code of the corresponding information. For example, if the CodeType parameter is set to distribution and the Code parameter is set to DXJF, this indicates that the CIDR block belongs to the region where the Daxing data center is located. |
| CodeName | String | This parameter is used with the CodeType parameter to specify the name of the corresponding information. |
| GmtCreate | String | The time when the CIDR block was created. |
| GmtModified | String | The latest time when the CIDR block was modified. |
| Seq | Integer | The sequence number of the region record. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://ddosprivate.[ RegionId].example.com/?Action=DescribeRegionName
```

Sample responses (JSON format)

```json
 "RegionNameList":[
   "GmtCreate":1463367238000,
   "Description":"Hybrid cloud data center list",
   "CodeName":"Daxing data center",
   "GmtModified":1463367238000,
   "CodeType":"distribution",
   "Id":17,
   "Code":"am1",
   "Seq":1
```

`},`

```json
   "GmtCreate":1463367238000,
   "Description":"Hybrid cloud data center list",
   "CodeName":"Not specified",
"GmtModified"1463367238000
```

```json
   "GmtModified":1463367238000,
   "CodeType":"distribution",
   "Id":32,
   "Code":"UNKNOWN",
   "Seq":4
```

`},`

```json
   "GmtCreate":1485069049000,
   "Description": "Data center list",
   "CodeName":"Beijing data center",
   "GmtModified":1485069049000,
   "CodeType":"distribution",
   "Id":50,
   "RegionId": "cn-beijing-btc-a01",
   "Seq":2
```

`},`

```json
   "GmtCreate":1485069106000,
   "Description": "Data center list",
   "CodeName":"Hangzhou data center",
   "GmtModified":1485069104000,
   "CodeType":"distribution",
   "Id":51,
   "Code":"cn-hangzhou-dg-a01",
   "Seq":3
```

`},`

```json
   "GmtCreate":1463367238000,
   "Description":"Hybrid cloud data center list",
   "CodeName":"Daxing data center",
   "GmtModified":1463367238000,
   "CodeType":"distribution",
   "Id":52,
   "Code":"DD_DXJF",
   "Seq":1
```

`],`

```json
 "RequestId":"26738B34-6680-4BD7-BBF8-EF8DE53D52F6"
```

#### 5.3.3 CreateIpSegment

You can call this operation to add a specified CIDR block to be monitored.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateIpSegment. |

| psara Stack Security |   |   | Developer Guide·Anti-DDo |
|---|---|---|---|

| Name | Type | Required | Description |
|---|---|---|---|
| IpSegmentName | String | Yes | The CIDR block to be added for monitoring, in x.x.x.x/x format. For example, 172.21.23.222/24. |
| InfoType | String | No | The CIDR block information type. For example, a value of distribution indicates the region information. |
| InfoName | String | No | The information describing the CIDR block based on the value of the InfoType parameter. For example, if the InfoType parameter is set to distribution, you can set the InfoName parameter to DXJF, indicating that the CIDR block belongs to the region where the Daxing data center is located. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://ddosprivate.[ RegionId].example.com/?Action=CreateIpSegment &IpSegmentName=172.21.13.222/24 &InfoType=distribution &InfoName=DXJF
```

Sample responses (JSON format)

```json
 "RequestId":"6C91B447-DAA5-40DB-B818-E10820D99DEC"
```

#### 5.3.4 DescribeIpSegment

You can call this operation to query Classless Inter-Domain Routing (CIDR) blocks under traffic monitoring.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeIpSegment. |
| CurrentPage | Integer | No | The number of the page to return. |
| PageSize | Integer | No | The number of records to return on each page. |
| InfoType | String | No | The type of the CIDR block information. For example, a value of distribution indicates the region information. |
| Distribution | String | No | The ID of the region. For example, a value of DXJF indicates the region where the Daxing IDC is located. |
| IpSegment | String | No | The CIDR block, in x.x.x.x/x format. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| TotalCount | Integer | The total number of returned pages. |
| IpSegmentList | Array | The CIDR blocks for traffic collection. For more information, see the following descriptions. |
| GmtCreate | Long | The time when the CIDR block for traffic collection was created. |
| GmtModified | Long | The time when the CIDR block for traffic collection was last modified. |
| Id | Integer | The ID of the CIDR block for traffic collection. |
| RegionName | String | The region name of the CIDR block. |
| InfoType | String | The type of the CIDR block information. For example, a value of distribution indicates the region information. |

| Parameter | Type | Description |
|---|---|---|
| InfoName | String | The information describing the CIDR block based on the value of the InfoType parameter. For example, if the value of the InfoType parameter is distribution, the value of the InfoName parameter can be DXJF, indicating that the CIDR block belongs to the region where the Daxing IDC is located. |
| IpExpressions | String | The CIDR block for traffic collection, in x.x.x.x/x format. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://ddosprivate.[ RegionId].example.com/?Action=DescribeIpSegment &CurrentPage=1 &Distribution=DXJF &InfoType=distribution &IpSegment=x.x.x.x/x &PageSize=20
```

Sample response (JSON format)

```json
    "TotalCount":1,
    "PageSize":20,
    "RequestId":"AC51224B-3730-4C6B-B444-2307C7F73E84",
    "IpSegmentList":[
            "IpExpressions":"192.168.x.x/24",
            "GmtCreate":1520565939000,
            "RegionName":"Daxing IDC",
            "GmtModified":1520565939000,
            "InfoName":"****",
            "Id":9,
            "InfoType":"distribution1"
```

`],`

```json
    "CurrentPage":1
```

#### 5.3.5 DeleteIpSegment

You can call this operation to delete a CIDR block whose traffic is collected and monitored based on the CIDR block record ID. Not e You must obtain the record ID of the monitored CIDR block to be deleted before calling this operation.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteIpSegment. |
| IpId | String | Yes | The record ID of the monitored CIDR block to be deleted. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://ddosprivate.[ RegionId].example.com/?Action=DeleteIpSegment &IpId=1
```

Sample responses (JSON format)

```json
 "RequestId":"9C40FE9D-EE39-4162-8E94-7C0A32F276D8"
```

#### 5.3.6 ModifyIpSegment

You can call this operation to modify a monitored Classless Inter-Domain Routing (CIDR) block with a specified record ID. Not e You must know the record ID of the monitored CIDR block to be modified before calling this operation.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to ModifyIpSegment. |
| IpId | Integer | Yes | The record ID of the monitored CIDR block to be modified. |
| InfoName | String | Yes | The region to which the CIDR block belongs. For example, a value of DXJF indicates that the CIDR block belongs to the region where the Daxing IDC is located. |
| IpSegmentName | String | Yes | The CIDR block, in x.x.x.x/x format. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://ddosprivate.[ RegionId].example.com/?Action=ModifyIpSegment &InfoName=**** &InfoType=distribution &IpId=11 &IpSegmentName=192.168.x.x/24
```

Sample response (JSON format)

```json
    "RequestId":"5FFE58AA-355B-4E0E-A742-0BB5554BA959"
```

#### 5.3.7 CreateDdosPolicy

You can call this operation to add an anti-DDoS policy for a specified IP address or Classless Inter- Domain Routing (CIDR) block.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to CreateDdosPolicy. |
| ExternalServiceIP | String | Yes | The IP address or CIDR block to which the anti-DDoS policy applies, in x.x.x.x or x.x.x.x/x format. |
| FlowRate | Integer | Yes | The traffic rate threshold. Unit: Mbit/s. Not e The value of this parameter must be greater than 0. |
| HttpRate | Integer | Yes | The HTTP request rate threshold. Unit: queries per second (QPS). Not e The value of this parameter must be greater than 50. |
| PackageRate | Integer | Yes | The packet rate threshold. Unit: packets per second (PPS). Not e The value of this parameter must be greater than 0. |
| UserId | Long | No | The user ID of the request sender. The parameter is automatically set by the system. |
| UserName | String | Yes | The username of the request sender. The parameter is automatically set by the system. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://ddosprivate.[ RegionId].example.com/?Action=CreateDdosPolicy &ExternalServiceIP=192.168.x.x/32 &FlowRate=1 &HttpRate=60 &PackageRate=1
```

Sample response (JSON format)

```json
    "RequestId":"CA179B61-DD6D-4FE3-A410-CC16AC705DF4"
```

#### 5.3.8 DescribeDdosPolicies

You can call this operation to query the configured DDoS protection policies.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDdosPolicies. |
| CurrentPage | Integer | No | The current page number. |
| PageSize | Integer | No | The maximum number of records displayed on a page. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| TotalCount | Integer | The total number of pages returned. |

| Name | Type | Description |
|---|---|---|
| DdosPolicies | Array | A list of DDoS protection policies. For more information, see the following parameter descriptions. |
| Code | String | The region code of the CIDR block that the DDoS protection policy is applied to. |
| CodeName | String | The region name of the CIDR block that the DDoS protection policy is applied to. |
| DepartmentName | String | The department of the user AliUID that created the DDoS protection policy. |
| ExternalServiceIP | String | The IP address or CIDR block that the DDoS protection policy is applied to. |
| FlowRate | Integer | The bandwidth threshold. Unit: Mbit/s. |
| HttpRate | Integer | The HTTP request threshold. Unit: QPS. |
| PackageRate | Integer | The packet threshold. Unit: PPS. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://ddosprivate.[ RegionId].example.com/?Action=DescribeDdosPolicies &CurrentPage=1 &PageSize=10
```

Sample responses (JSON format)

```json
    "TotalCount":1,
    "PageSize": 10,
    "RequestId": "179E1AA9-1BC2-4A66-9E4B-1640EDDE7D1C",
    "CurrentPage": 1,
    "DdosPolicies": [
            "PackageRate": 200,
            "HttpRate": 0,
            "CodeName":"Daxing data center",
            "ExternalServiceIP": "x.x.x.x/x",
            "DepartmentName": "Department 1",
            "Code": "DD_DXJF",
            "FlowRate": 900,
            "AliUid": 0
```

`]`

#### 5.3.9 DeleteDdosPolicy

You can call this operation to delete an anti-DDoS policy for a specified Classless Inter-Domain Routing (CIDR) block.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DeleteDdosPolicy. |
| RegionCode | String | Yes | The ID of the region. For example, cn- hangzhou-env6-d01. |
| ExternalServiceIP | String | Yes | The IP address or CIDR block to which the anti-DDoS policy applies, in x.x.x.x or x.x.x.x/x format. |
| FlowRate | Integer | No | The traffic rate threshold. Unit: Mbit/s. Not e The value of this parameter must be greater than 0. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| HttpRate | Integer | No | The HTTP request rate threshold. Unit: queries per second (QPS). Not e The value of this parameter must be greater than 50. |
| PackageRate | Integer | No | The packet rate threshold. Unit: packets per second (PPS). Not e The value of this parameter must be greater than 0. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://ddosprivate.[ RegionId].example.com/?Action=DeleteDdosPolicy &ExternalServiceIP=192.168.x.x/24 &RegionCode=cn-****-env6-d01 &FlowRate=55 &HttpRate=55 &PackageRate=55
```

Sample response (JSON format)

```json
    "RequestId":"8C9B8735-18BA-451B-AE9D-1428554CA360"
```

#### 5.3.10 ModifyDdosPolicy

You can call this operation to modify a specified anti-DDoS policy.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to ModifyDdosPolicy. |
| Distribution | String | Yes | The ID of the region. For example, a value of DXJF indicates the region where the Daxing IDC is located. |
| ExternalServiceIP | String | Yes | The IP address or Classless Inter-Domain Routing (CIDR) block to which the anti- DDoS policy applies, in x.x.x.x or x.x.x.x/x format. |
| FlowRate | Integer | Yes | The traffic rate threshold. Unit: Mbit/s. Not e The value of this parameter must be greater than 0. |
| HttpRate | Integer | Yes | The HTTP request rate threshold. Unit: queries per second (QPS). Not e The value of this parameter must be greater than 50. |
| PackageRate | Integer | Yes | The packet rate threshold. Unit: packets per second (PPS). Not e The value of this parameter must be greater than 0. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://ddosprivate.[ RegionId].example.com/?Action=ModifyDdosPolicy &Distribution=**** &ExternalServiceIP=192.168.x.x/32 &FlowRate=1 &HttpRate=60 &PackageRate=1
```

Sample response (JSON format)

```json
    "RequestId":"CA179B61-DD6D-4FE3-A410-CC16AC705DF4"
```

#### 5.3.11 DescribeBlockSwitchs

You can call this operation to query the status of the traffic block switch in anti-DDoS.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeBlockSwitchs. |
| CurrentPage | Integer | No | The current page number. |
| PageSize | Integer | No | The maximum number of records displayed on a page. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| TotalCount | Integer | The total number of pages returned. |
| BlockSwitchs | Array | The traffic block switch information. For more information, see the following parameter descriptions. |

| A | psara Stack Security |   | Developer Guide·Anti-DDo | S |
|---|---|---|---|---|

| Name | Type | Description |
|---|---|---|
| Code | String | The code of the block switch, which uniquely identifies a block switch. |
| Description | String | The brief description of the block switch. |
| Id | Integer | The ID of the block switch. |
| Mode | Integer | The status of the block switch. Valid values: 0: indicates disabled. 1: indicates enabled. |
| ModeName | String | The status name of the block switch. Valid values: Disabled Enabled |
| Name | String | The name of the block switch. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://ddosprivate.[ RegionId].example.com/?Action=DescribeBlockSwitchs &CurrentPage=1 &PageSize=20
```

Sample responses (JSON format)

```json
 "PageSize": 10,
 "RequestId":"95F2F4C8-7623-48B7-A976-30B48F3A25EB",
 "CurrentPage":1,
 "BlockSwitchs":[
   "Description": "test",
   "Mode":0,
   "ModeName":"Disabled",
   "id": 1,
   "Code":"UPGRADE_SWITCH",
   "Name":"Upgrade channel switch"
```

`},`

```json
   "Description":"Automatic upgrade switch",
   "Mode":1,
   "ModeName":"Enabled",
   "Id":2,
   "Code":"AUTO_UPGRADE_SWITH",
   "Name":"Automatic upgrade switch"
```

`]`

#### 5.3.12 ModifyBlockSwitchs

You can call this operation to change the status of the block switch in DDoS settings.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyBlockSwitch. |
| Id | Integer | Yes | The ID of the block switch. |
| Mode | Integer | Yes | The status of the block switch. Valid values: 0: indicates disabled. 1: indicates enabled. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://ddosprivate.[ RegionId].example.com/?Action=ModifyBlockSwitch &Id=1 &Mode=1
```

Sample responses (JSON format)

```json
 "RequestId":"B7FA97F0-082D-4611-A3C4-867011E2A106"
```

#### 5.3.13 DescribeDdosEvents

You can call this operation to query distributed denial of service (DDoS) events that meet the specified search criteria.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeDdosEvents. |
| CurrentPage | Integer | No | The number of the page to return. |
| PageSize | Integer | No | The number of records to return on each page. |
| StartRow | Integer | No | The sequence number of the first record to return on the current page. |
| Distribution | String | No | The ID of the region. For example, a value of DXJF indicates the region where the Daxing IDC is located. |
| VmIP | String | No | The IP address of the victim server. |
| StartDay | Long | No | The beginning of the time range where data is queried. |
| EndDay | Long | No | The end of the time range where data is queried. |

| D | eveloper Guide·Anti- | DDoS |   | Apsara Stack Securit | y |
|---|---|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| SearchReason | String | No | The reason why the DDoS event is triggered. Valid values: bps, pps, and qps. You can query events triggered by multiple reasons. For example, you can enter "bps,pps" to query the DDoS events that are triggered when the traffic rate threshold or the packet transmission rate threshold is exceeded. |
| SelectStatus | String | No | The status of the DDoS event. Valid values: Scrubbing Scrubbing completed |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| TotalCount | Integer | The total number of returned pages. |
| DdosEvents | Array | The DDoS events. For more information, see the following descriptions. |
| Id | Long | The ID of the event. |
| GmtCreate | Long | The time when the event was created. |
| GmtModified | Long | The time when the event was updated. |
| Aliuid | Long | The AliUid of the asset owner. |
| AttackType | String | The type of the attack. Not e In the current version, only the value of defence is supported. |

| Parameter | Type | Description |
|---|---|---|
| Caller | String | The name of the system that calls the operation. Not e Currently, the fixed value is beaverdj, indicating Network Traffic Monitoring _ System. |
| Category | Integer | The number of the security event category. |
| CategoryName | String | The name of the security event category. |
| VmIp | String | The IP address of the victim server. |
| Code | String | The scrubbing status of the event. Valid values: Scrubbing Scrubbing completed |
| Bps | Long | The traffic rate threshold. Unit: Mbit/s. |
| Pps | Long | The packet rate threshold. Unit: packets per second (PPS). |
| Qps | Long | The HTTP request rate threshold. Unit: queries per second (QPS). |
| Conn | Integer | The threshold of concurrent connections. Not e This response parameter has been deprecated. |
| NewConn | Integer | The threshold of new connections. Not e This response parameter has been deprecated. |
| Reason | String | The reason why the event was reported. |
| Distribution | String | The ID of the region. |
| DistributionDisplay | String | The name of the region. |

| Parameter | Type | Description |
|---|---|---|
| IsFinished | Boolean | Indicates whether the attack has finished. Valid values: true: indicates that the attack has finished. false: indicates that the attack has not finished. |
| OccurrenceTime | Long | The time when the event occurred. |
| EndTime | Long | The time when the attack finished. |
| LocationAdd | String | The location where the event was added. Not e This response parameter is invalid in Apsara Stack. |
| LocationDel | String | The location where the event was canceled. Not e This response parameter is invalid in Apsara Stack. |
| Status | Integer | The status of the IP address where the DDoS event occurred. Valid values: 0: indicates that the IP address has not expired. 1: indicates that the IP address has expired. |
| Successful | Integer | Indicates whether the attack succeeds. Valid values: 0: indicates that the attack has failed. 1: indicates that the attack succeeded. |
| NeedIgnore | Integer | Indicates whether you need to ignore the event. Valid values: 0: indicates that you do not need to ignore the event. 1: indicates that the event has been reported repeatedly and you need to ignore the event. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://ddosprivate.[ RegionId].example.com/?Action=DescribeDdosEvents &CurrentPage=1 &Distribution=DXJF $StartDay=1381079107176 $EndDay=1481079107176 &PageSize=10
```

Sample response (JSON format)

```json
 "TotalCount":1,
 "RequestId":"AD525B06-F5F7-4319-94F4-45154D5B0750",
 "DdosEvents":[
   "NewConn":0,
   "Status":0,
   "LocationDel":"nulllocal",
   "Category":21,
   "Bps":5,
   "EndTime":1573233588000,
   "Zone":"default",
   "GmtModified":1484372333000,
   "AttackType":"0",
   "Conn":0,
   "Code":"Scrubbing",
   "DistributionDisplay":"Daxing IDC",
   "Reason":"bps",
   "OccurrenceTime":1473233588000,
   "GmtCreate":1484369068000,
   "Pps":450,
   "Caller":"beaver_dj",
   "Qps":0,
   "Distribution":"am1",
   "LocationAdd":"local",
   "CategoryName":"DDOS_DEFENSE",
   "Id":3,
   "IsFinished":false,
   "NeedIgnore":0
```

`],`

```json
 "CurrentPage":1
```

#### 5.3.14 DescribeFlowAnalysisResult

You can call this operation to query the analysis result of the traffic sent to an IP address.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeFlowAnalysisResult. |
| Distribution | String | Yes | The ID of the region. For example, a value of DXJF indicates the region where the Daxing IDC is located. |
| VmIP | String | Yes | The IP address of the victim server. |
| StartDate | Long | Yes | The beginning of the time range where traffic is analyzed. |
| SearchReason | String | No | The reason why the distributed denial of service (DDoS) event is triggered. Valid values: bps, pps, and qps. You can query events triggered by multiple reasons. For example, you can enter "bps,pps" to query the DDoS events that are triggered when the traffic rate threshold or the packet transmission rate threshold is exceeded. |
| SelectStatus | String | No | The status of the DDoS event. Valid values: Scrubbing Scrubbing completed |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TopAttackers | Array | The analysis on the top 10 attackers. For more information, see the following descriptions. |
| Ip | String | The IP address of the attacker. |
| Count | Float | The percentage of attacks launched to the IP address compared to the total attacks. |

| Parameter | Type | Description |
|---|---|---|
| TopProtocols | Array | The analysis on the composition of the attack traffic. For more information, see the following descriptions. Not e The traffic composition analysis shows traffic of different protocols, including TCP, ICMP, and UDP. |
| Protocol | String | The protocol. |
| Count | Float | The percentage of the traffic of the specified protocol compared to the total amount of traffic. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://ddosprivate.[ RegionId].example.com/?Action=DescribeFlowAnalysisResult &Distribution=DD_DXJF &startDate=123123312000 &VmIp=x.x.x.x
```

Sample response (JSON format)

```json
    "TopAttackers":["Ip":"x.x.x.x","Count":"1.00"],
    "RequestId":"B2488F1F-930D-4906-AC76-61045B4F1EF2",
    "TopProtocols":["Protocol":"tcp","Count":"1.00"]
```

#### 5.3.15 DescribeFlowDetails

You can call this operation to query the detailed traffic information for a specified IP address.

| Parameter | Type | Required | Description |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeFlowDetails. |
| Distribution | String | Yes | The ID of the region. For example, a value of DXJF indicates the region where the Daxing IDC is located. |
| VmIP | String | Yes | The IP address of the victim server. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| HttpStatusCode | Integer | The HTTP status code. |
| FlowDetail | Struct | The detailed traffic information. For more information, see the following descriptions. |
| AliUid | Long | The ID of the Alibaba Cloud account. |
| Distribution | String | The ID of the region. |
| DistributionDisplay | String | The name of the region. |
| ExternalServiceIp | String | The IP address or Classless Inter-Domain Routing (CIDR) block. |
| FlowRate | Integer | The flow rate. Unit: Mbit/s. |
| HttpRate | Integer | The HTTP request rate. Unit: queries per second (QPS). |
| PackageRate | Integer | The packet rate. Unit: packets per second (PPS). |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://ddosprivate.[ RegionId].example.com/?Action=DescribeFlowDetails &Distribution=**** &VmIp=10.0.x.x
```

Sample response (JSON format)

```json
    "RequestId":"8491DBFD-48C0-4E11-B6FC-6F38921244A9",
    "FlowDetail":{
        "PackageRate":200,
        "HttpRate":0,
        "ExternalServiceIP":"10.0.x.x/32",
        "Distribution":"DXJF",
        "DistributionDisplay":"Daxing IDC",
        "FlowRate":900,
        "AliUid":0
```

`},`

```json
    "HttpStatusCode":200
```

#### 5.3.16 CancelCleanStatus

You can call this operation to disable DDoS traffic scrubbing for a specified IP address.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to CancelCleanStatus. |
| Distribution | String | Yes | The ID of the region. For example, a value of DXJF indicates the region where the Daxing IDC is located. |
| VmIp | String | Yes | The IP address of the instance, in x.x.x.x format. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://ddosprivate.[ RegionId].example.com/?Action=CancelCleanStatus &Distribution=DXJF &SourceIp=10.0.x.x &VmIp=172.16.x.x
```

Sample response (JSON format)

```json
    "RequestId":"208B016D-4CB9-4A85-96A5-0B8ED1EBF271"
```

#### 5.3.17 CreateWhiteList

You can call this operation to add a whitelist of trusted IP addresses that are exempt from traffic security monitoring.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to CreateWhiteList. |
| Type | Integer | Yes | The type of the whitelist. Valid values: 6: indicates a server brute-force attack whitelist. 12: indicates a BWAF source IP address whitelist. 15: indicates an application attack whitelist. |
| Username | String | No | The username used to add the whitelist. |
| DestinationIp | String | No | The destination IP address. Not e When you add a BWAF source IP address whitelist (that is, the Type parameter is set to 12), the DestinationIp parameter must be set to the default value 0.0.0.0. |
| SourceIpStr | String | No | The source IP address. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://ddosprivate.[ RegionId].example.com/?Action=CreateWhiteList &Type=15 &DestinationIp=192.168.xx.xx &SourceIpStr=192.168.xx.xx &Username=test
```

Sample response (JSON format)

```json
    "RequestId":"208B016D-4CB9-4A85-96A5-0B8ED1EBF271"
```

#### 5.3.18 DescribeWhiteList

You can call this operation to query the IP addresses that have been added to a whitelist.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeWhiteList. |
| DestinationIp | String | No | The destination IP address. |
| SourceIpStr | String | No | The source IP address. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| Type | Integer | No | The type of the whitelist. Valid values: 6: indicates a server brute-force attack whitelist. 12: indicates a BWAF source IP address whitelist. 15: indicates an application attack whitelist. |
| Username | String | No | The username. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| TotalCount | Integer | The total number of returned pages. |
| WhiteLists | List | The whitelist records. For more information, see the following descriptions. |
| SourceIp | String | The source IP address. |
| Id | Integer | The ID of the whitelist record. |
| Type | Integer | The type of the whitelist. Valid values: 6: indicates a server brute-force attack whitelist. 12: indicates a BWAF source IP address whitelist. 15: indicates an application attack whitelist. |
| Username | String | The username. |
| DestinationIp | String | The destination IP address. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://ddosprivate.[ RegionId].example.com/?Action=DescribeWhiteList &Type=15 &DestinationIp=172.16.xx.xx &SourceIpStr=172.17.xx.xx &Username=test
```

Sample response (JSON format)

```json
    "CurrentPage":1,
    "PageSize":20,
    "RequestId":"430A3687-B9EC-4F71-B472-EE24ED609863",
    "Success":true,
    "TotalCount":0,
    "WhiteLists":[{
        "DestinationIp":"172.16.xx.xx",
        "Id":6,
        "SourceIp":"172.17.xx.xx",
        "Type":15,
        "Username":"****"
```

`}]`

#### 5.3.19 DeleteWhiteList

You can call this operation to delete a specified whitelist entry.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteWhiteList. |
| Id | Integer | Yes | The ID of the whitelist entry. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://ddosprivate.[ RegionId].example.com/?Action=DeleteWhiteList &Id=15
```

Sample responses (JSON format)

```json
 "RequestId":"208B016D-4CB9-4A85-96A5-0B8ED1EBF271"
```

#### 5.3.20 DescribeConsoleDdosPolicies

You can call this operation to obtain the records of anti-DDoS policies, including the system default policies.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeConsoleDdosPolicies. |
| AliUid | Long | Yes | The ID of the Alibaba Cloud account. |
| CurrentPage | Integer | No | The number of the page to return. |
| PageSize | Integer | No | The number of records to return on each page. |
| StartRow | Integer | No | The start row to return. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| TotalCount | Integer | The total number of returned pages. |
| ThresholdList | List | The anti-DDoS policies. For more information, see the following descriptions. |
| DepartmentName | String | The department name of the current user. |

| psara Stack Security |   | Developer Guide·Anti-DDo |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| ExternalServiceIP | String | The IP address or Classless Inter-Domain Routing (CIDR) block. Not e A value of default is returned if the system default policy is used. |
| Code | String | The IDC ID corresponding to the CIDR block. |
| CodeName | Sting | The IDC name corresponding to the CIDR block. |
| FlowRate | Integer | The threshold for the traffic rate. Unit: Mbit/s. |
| HttpRate | Integer | The threshold for the HTTP request rate. Unit: queries per second (QPS). |
| PackageRate | Integer | The threshold for the packet rate. Unit: packets per second (PPS). |
| AliUid | Long | The Alibaba Cloud account ID corresponding to the policy. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://ddosprivate.[ RegionId].example.com/?Action=DescribeConsoleDdosPolicies &AliUid=**** &CurrentPage=1 &PageSize=10 &SourceIp=xx.xx.xx.xx
```

Sample response (JSON format)

```json
    "CurrentPage":1,
    "HttpStatusCode":200,
    "PageSize":20,
    "RequestId":"7C3AC882-E5A8-4855-BE77-B6837B695EF1",
    "ThresholdList":[
            "AliUid":151971404963****,
            "Code":"DD_DXJF",
            "CodeName":"DD_DXJF",
            "DepartmentName":"****Cloud",
            "ExternalServiceIP":"1.1.xx.xx/32",
            "FlowRate":1,
            "HttpRate":52,
            "PackageRate":1
```

`},`

```json
            "AliUid":151971404963****,
            "Code":"DD_DXJF",
            "CodeName":"DD_DXJF",
            "DepartmentName":"****Cloud",
            "ExternalServiceIP":"2.2.xx.xx/32",
            "FlowRate":1,
            "HttpRate":51,
            "PackageRate":1
```

`},`

```json
            "AliUid":-1,
            "Code":"DD_DXJF",
            "CodeName":"DD_DXJF",
            "ExternalServiceIP":"default",
            "FlowRate":900,
            "HttpRate":0,
            "PackageRate":200
```

`],`

```json
    "TotalCount":3
```

## 6 Cloud Firewall

### 6.1 List of operations by function

The following tables list API operations available for use in Cloud Firewall. Access control

| API operation | Description |
|---|---|
| DescribePolicyPriorUsed | Queries the priority range of access control policies that match specific query conditions. |
| ModifyControlPolicyPosition | Modifies the priority of an access control policy. |
| DescribeControlPolicy | Queries information about all the access control policies that match specific query conditions. |
| AddControlPolic | Creates an access control policy. |
| DeleteControlPolicy | Deletes an access control policy. |
| ModifyControlPolicy | Modifies the configurations of an access control policy. |

Address book

| API operation | Description |
|---|---|
| AddAddressBook | Creates an access control address book. Supported address book types are IP address books, Elastic Compute Service (ECS) tag address books, port address books, and domain address books. |
| DeleteAddressBook | Deletes an access control address book. |
| ModifyAddressBook | Modifies an access control address book. |
| DescribeAddressBook | Queries detailed information about access control address books. |

### 6.2 Make API requests

#### 6.2.1 Request structure

Apsara Stack Security APIs are based on RPC. This chapter describes the structure of the API requests. Request structure description You can send an HTTP request to call an API. The URL of the request must be in the following format:

```
http://endpoint/?Action=xx&parameters
```

Where: `endpoint` : An endpoint is used to call a cloud service. The endpoint for the Web Application Firewall (WAF) service is `wafprivate.[ RegionId].example.com` . `Action` : The operation that you want to perform. For example, you can set the value to DescribeFeatures to query the deployed Apsara Stack Security features. `parameters` : The request parameters that are contained in the request. Request parameters include common request parameters and custom request parameters. Request parameters must be separated with ampersands (&). Common request parameters are used to indicate information such as the API version and authentication information. For more information, see Common request parameters. For more information about the custom request parameters, see the corresponding operation description. Call the DescribeFeatures operation to query the deployed Apsara Stack Security features.

```
https://yundunprivate.[ RegionId].example.com/?Action=DescribeFeatures&AccessKeyId=key-test &Format=JSON&SecureTransport=true&SignatureMethod=HMAC-SHA1&SignatureNonce=15215528852396&S ignatureVersion=1.0&SourceIp=1xxxx6&Timestamp=2018-03-02Txxxxxxx&Version=2018-01-16&Signatu re=xxxx%xxxx%3D
```

API requests are presented in the following easy-to-read form in this document:

```
https://yundunprivate.[ RegionId].example.com/?Action=DescribeFeatures &Format=JSON &Version=2018-05-01 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2012-06-01T12:00:00Z
```

#### 6.2.2 Signature mechanism

Apsara Stack Security authenticates each access request. You need to include a signature for the submitted HTTP or HTTPS request. API authorization To ensure the security of your account, we recommend that you use a Resource Access Management (RAM) user to call API operations. Before using a RAM user to call an API operation, you must grant the RAM user the corresponding permission to call the API by creating an authorization policy and attaching the policy to the RAM user. API signature To ensure secure calls to the API, Alibaba Cloud authenticates each API request through the signature. When you manually make an API request, you need to use AccessKey Secret to calculate the signature, that is, the hash-based message authentication code (HMAC) value, based on the encoded and sorted request string. For more information, see the definition in RFC 2104. This topic uses the raw access parameters in the following table to describe how to create an API signature.

| Parameter | Description |
|---|---|
| Access point | http://semawaf.[ RegionId].example.com/? |
| API-specific parameters | Action=DescribeFeatures |
| Common parameters (excluding the Signature parameter) | &Timestamp=2016-02-23T12:46:24Z &Format=JSON &AccessKeyId=<yourAccessKeyId> &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2018-01-16 &SignatureVersion=1.0 |
| AccessKey secret | <yourAccessKeySecret> |

1. Use the request parameters to construct a canonicalized query string.
Not e The request parameters include common request parameters (excluding the Signature parameter) and API-specific parameters. i. Sort the parameters. Sort the request parameters in alphabetical order. ii. Encode the parameters. Use UTF-8 to URL-encode the parameter names and values. The encoding rules are as follows: Letters, digits, hyphens (-), underscores (_), periods (.), and tildes (~) are not encoded. Other characters are encoded in the %XY format, where XY is the hexadecimal representation of the character in ASCII. For example, the double quotation mark (") is encoded as %22. Extended UTF-8 characters are encoded in the %XY%ZA… format. Note that a space is encoded as %20, instead of a plus sign (+). iii. Connect the encoded parameter names and values with equal signs (=). iv. Then, sort the parameter name and value pairs connected by equal signs in alphabetical order, and connect them with ampersands (&) to produce the canonicalized query string.
2. Use the canonicalized query string to construct the string for signature calculation based on the
following rules:

```
StringToSign=HTTPMethod + “&” + percentEncode(“/”) + ”&” + percentEncode(CanonicalizedQueryString)
```

3. Calculate the HMAC value of the StringToSign string according to the definition in RFC 2104.
Not e The key used for signature calculation is your AccessKey secret adding the ampersand (&) (ASCII 38). Secure Hash Algorithm 1 (SHA1) is used as the hash algorithm.
4. Encode the preceding HMAC value into a string based on Base64 encoding rules to obtain the
signature value.

```
LEW8N4y7Uasop******
```

5. Set the Signature parameter in the request parameters to this signature value to sign the request.

#### 6.2.3 Common request parameters

The following table describes the common request parameters that are used to indicate information such as the API version and authentication information.

| Name | Type | Required | Description |
|---|---|---|---|
| Version | String | Yes | The API version in the format of YYYY- MM-DD. Set the value to 2018-01-16. |
| AccessKeyId | String | Yes | The key ID that Alibaba Cloud assigns to a user for service access. |
| Signature | String | Yes | The signature string. |
| SignatureMethod | String | Yes | The signature method. Set the value to HMAC-SHA1. |
| Timestamp | String | Yes | The timestamp of the request. Follow the ISO 8601 standard to specify the date and use the offset from Coordinated Universal Time (UTC) to specify the time zone. The format is YYYY-MM- DDThh:mm:ssZ . For example, 2014-05-26T12:00:00Z indicates 20:00:00 on May 26, 2014, Beijing time. |
| SignatureVersion | String | Yes | The signature algorithm version. Set the value to 1.0. |

|   |   | YYYY-MM- |
|---|---|---|
|   | DDThh:mm:ssZ |   |

| psara Stack Security |   |   | Developer Guide·Cloud Firewal |
|---|---|---|---|
| Name | Type | Required | Description |
| SignatureNonce | String | Yes | The unique random number used to prevent network replay attacks. You must use different random numbers for different requests. |
| ResourceOwnerAc count | String | No | The owner account of the resource to be accessed through this API request, that is, the logon username. |
| Format | String | No | The format of the response. Set the value to JSON or XML. Not e Default value: XML. |

#### 6.2.4 Response structure

Apsara Stack Security API responses support both the XML and JSON formats. The system always returns a unique identification code RequestId each time you send a request to call an operation, no matter whether the call is successful or not. Sample responses (XML format)

```xml
<? xml version="1.0" encoding="UTF-8"? > <! -- The root node of the result --> <Operation name+Response>
    <! -- Returned request ID -->
    <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
    <! -- Returned data -->
</Operation name+Response>
```

Sample responses (JSON format)

```json
"RequestId": "4C467B38-3910-447D-87BC-AC049166F216", /* Returned data */
```

### 6.3 Access control

#### 6.3.1 DescribePolicyPriorUsed

Queries the priority range of access control policies that match specific query conditions.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePolicyPri orUsed | The operation that you want to perform. Set the value to DescribePolicyPriorUsed. |
| Direction | String | Yes | in | The traffic direction to which the access control policy applies. Valid values: in: inbound traffic out : outbound traffic |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Example | Description |
|---|---|---|---|
| End | Integer | 150 | The lowest priority of the access control policy. |
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |
| Start | Integer | 1 | The highest priority of the access control policy. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePolicyPriorUsed &Direction=in
```

Sample success responses `XML` format

```xml
<DescribePolicyPriorUsedResponse>
      <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D</RequestId>
      <Start>1</Start>
      <End>150</End>
</DescribePolicyPriorUsedResponse>
```

`JSON` format

```json
    "RequestId": "CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D",
    "Start": 1,
    "End": 150
```

For a list of error codes, see Error codes.

#### 6.3.2 ModifyControlPolicyPosition

Modifies the priority of an access control policy.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyControlPoli cyPosition | The operation that you want to perform. Set the value to ModifyControlPolicyPosition. |
| Direction | String | Yes | in | The direction of the traffic to which the access control policy applies. Valid values: in: inbound traffic out : outbound traffic |
| NewOrder | String | Yes | 1 | The new priority of the access control policy. |
| OldOrder | String | Yes | 5 | The original priority of the access control policy. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 850A84D6-0DE4- 4797-A1E8- 00090125EEB1 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyControlPolicyPosition &Direction=in &NewOrder=1 &OldOrder=5
```

Sample success responses `XML` format

```xml
<ModifyControlPolicyPosition>
   <RequestId>850A84D6-0DE4-4797-A1E8-00090125EEB1</RequestId>
</ModifyControlPolicyPosition>
```

`JSON` format

```json
 "RequestId":"850A84D6-0DE4-4797-A1E8-00090125EEB1"
```

For a list of error codes, see Error codes.

#### 6.3.3 DescribeControlPolicy

Queries information about all the access control policies.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeControlP olicy | The operation that you want to perform. Set the value to DescribeCont rolPolicy. |
| CurrentPage | String | Yes | 1 | The page number of the current page. Default value: 1. |
| Direction | String | Yes | in | The direction of the traffic to which the access control policy applies. Valid values: in: inbound traffic out : outbound traffic |
| PageSize | String | Yes | 10 | The number of entries to return on each page. Maximum value: 50. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Source | String | No | 1.2.3.5 | The source address in the access control policy. Fuzzy match is supported. Valid values: If the SourceType parameter is set to net , the value of this parameter is the source CIDR block. Example: 10.0.1.0/24. If the SourceType parameter is set to group , the value of this parameter is the name of the source address book. Example: db group. _ If the SourceType parameter is set to location , the value of this parameter is the source location. Example: beijing. If the SourceType parameter is not specified, all source addresses are queried. Not e The valid values of this parameter depend on the value of the SourceType parameter. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Destination | String | No | 1.2.3.0 | The destination address in the access control policy. Fuzzy match is supported. Valid values: If the DestinationType parameter is set to net , the value of this parameter is the destination CIDR block. Example: 10.0.3.0/24. If the DestinationType parameter is set to domain , the value of this parameter is the destination domain. Example: aliyun. If the DestinationType parameter is set to group , the value of this parameter is the name of the destination address book. Example: db group. _ If the DestinationType parameter is set to location , the value of this parameter is the destination location. Example: beijing. If the DestinationType parameter is not specified, all destination addresses are queried. Not e The valid values of this parameter depend on the value of the DestinationType parameter. |
| Description | String | No | test | The description of the access control policy. Fuzzy match is supported. Not e If this parameter is not specified, the descriptions of all access control policies are queried. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Proto | String | No | TCP | The type of protocol in the access control policy. Valid values: TCP UDP ICMP ANY, which indicates all types of protocols |
| AclAction | String | No | accept | The action that Cloud Firewall performs on the traffic. Valid values: accept : allows the traffic. drop: denies the traffic. log: monitors the traffic. If this parameter is not specif ied, access control policies that specify the preceding actions are queried. |
| Release | String | No | true | Specifies whether the access control policy is enabled. By default, an access control policy is enabled after it is created. Valid values: t rue: The access control policy is enabled. f alse: The access control policy is disabled. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNo | String | 1 | The page number of the current page. |
| PageSize | String | 10 | The number of entries returned per page. |
| Policys | Array |   | The information about the access control policy. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AclAction | String | accept | The action that Cloud Firewall performs on the traffic. Valid values: accept : allows the traffic. drop: denies the traffic. log: monitors the traffic. |
| AclUuid | String | 00281255-d220- 4db1-8f4f- c4df221ad84c | The ID of the access control policy. |
| ApplicationId | String | 10*** | The application ID in the access control policy. |
| ApplicationNa me | String | HTTP | The type of the application that the access control policy supports. Valid values: FTP HTTP HTTPS Memcache MongoDB MQTT MySQL RDP Redis SMTP SMTPS SSH SSL VNC ANY, which indicates all types of applications |
| Description | String | test | The description of the access control policy. |
| DestPort | String | 80 | The destination port in the access control policy. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DestPortGroup | String | my port group _ _ | The name of the destination port address book in the access control policy. |
| DestPortGroup Ports | List | [80,443] | The ports in the destination port address book. |
| DestPortType | String | port | The type of the destination port in the access control policy. Valid values: port group: port address book |
| Destination | String | 1.2.3.4/24 | The destination address in the access control policy. Valid values: If the Dest inat ionT ype parameter is set to net , the value of this parameter is the destination IP address or CIDR block. Example: 10.0.3.0/24. If the Dest inat ionT ype parameter is set to domain, the value of this parameter is the destination domain. Example: aliyuncs.com. If the Dest inat ionT ype parameter is set to group, the value of this parameter is the name of the destination address book. Example: db group. _ If the Dest inat ionT ype parameter is set to locat ion, the value of this parameter is the destination location. For more information about location codes, see AddControlPolicy. Example: ["BJ11", "ZB"]. Not e The valid values of this parameter depend on the value of the DestinationType parameter. |
| DestinationGro upCidrs | List | ["1.2.3.0/24", "1.2.3.1/32"] | The CIDR blocks in the destination address book. |

| A | psara Stack Securi | ty |   | Developer Guide·Cloud Firewal | l |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| DestinationGro upType | String | ip | The type of the destination address book in the access control policy. Valid values: ip: an address book that includes one or more IP addresses t ag: an address book that includes one or more IP addresses with Elastic Compute Service (ECS) tags domain: an address book that includes one or more domain names t hreat : an address book that includes one or more malicious IP addresses or domain names backsrc: an address book that includes one or more back-to-origin addresses of Anti-DDoS Pro or Anti-DDoS Premium instances or WAF instances |
| DestinationTyp e | String | net | The type of the destination address in the access control policy. Valid values: net : destination CIDR block group: destination address book domain: destination domain name locat ion: destination location |
| Direction | String | in | The direction of the traffic to which the access control policy applies. Valid values: in: inbound traffic out : outbound traffic |
| DnsResult | String | 1.1.1.1,2.2.2.2 | The DNS resolution result. |
| DnsResultTime | Long | 1579261141 | The timestamp of the DNS resolution result. |
| HitTimes | Integer | 100 | The number of hits for the access control policy. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Order | Integer | 1 | The priority of the access control policy. The priority value starts from 1. A smaller value indicates a higher priority. Not e The value -1 indicates the lowest priority. |
| Proto | String | TCP | The type of the security protocol in the access control policy. Valid values: ANY TCP UDP ICMP |
| Release | String | true | Indicates whether the access control policy is enabled. By default, an access control policy is enabled after it is created. Valid values: t rue: The access control policy is enabled. f alse: The access control policy is disabled. |

| Parameter | Type | Example | Description |   |   |
|---|---|---|---|---|---|
| Source | String | 1.2.3.0/24 | The source address in the access control policy. Valid values: If the SourceType parameter is set to ne t , the value of this parameter is the source CIDR block. Example: 10.0.1.0/24. If the SourceType parameter is set to gr oup , the value of this parameter is the name of the source address book. Example: db group. _ If t he Sourcet T ype paramet er is set t o locat ion, t he value of t his paramet er is t he source location. For more inf ormat ion about locat ion codes, see AddCont rolPolicy. Example: ["BJ11", "ZB"]. |   |   |
|   |   |   |   | gr |   |
| SourceGroupCid rs | List | ["10.0.0.0/24", "10.0.0.1/32"] | The CIDR blocks in the source address book. |   |   |
| SourceGroupTy pe | String | ip | The type of the source address book in the access control policy. Valid values: ip: an address book that includes one or more IP addresses t ag: an address book that includes one or more IP addresses with ECS tags domain: an address book that includes one or more domain names t hreat : an address book that includes one or more malicious IP addresses or domain names backsrc: an address book that includes one or more back-to-origin addresses of Anti-DDoS Pro or Anti-DDoS Premium instances or WAF instances |   |   |

| ne |   |
|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| SourceType | String | net | The type of the source address in the access control policy. Valid values: net : source CIDR block group: source address book locat ion: source location |
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |
| TotalCount | String | 100 | The total number of the returned access control policies. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeControlPolicy &CurrentPage=1 &Direction=in &PageSize=10
```

Sample success responses `XML` format

```xml
<DescribeControlPolicyResponse>
  <TotalCount>58</TotalCount>
  <PageNo>1</PageNo>
  <PageSize>10</PageSize>
  <RequestId>A08BC58F-A83D-43EB-BC31-2F0D723929CC</RequestId>
  <Policys>
        <ApplicationName>RDP</ApplicationName>
        <Description>11</Description>
        <HitTimes>0</HitTimes>
        <DestinationType>net</DestinationType>
        <SourceType>net</SourceType>
        <Proto>TCP</Proto>
        <Order>5</Order>
        <ApplicationId>27</ApplicationId>
        <Direction>in</Direction>
        <DestPortType>port</DestPortType>
        <Source>1.1.1.1/32</Source>
        <DestPort>1/1</DestPort>
        <AclAction>accept</AclAction>
        <AclUuid>53d82f0e-9bf1-4761-ab3b-a070b4811234</AclUuid>
        <Destination>1.1.1.1/32</Destination>
        <DnsResult>1.1.1.1,2.2.2.2</DnsResult>
        <DnsResultTime>1579261141</DnsResultTime>
  </Policys>
</DescribeControlPolicyResponse>
```

`JSON` format

```json
    "TotalCount":58,
    "PageNo":1,
    "PageSize":10,
    "RequestId":"A08BC58F-A83D-43EB-BC31-2F0D723929CC",
    "Policys":[
            "DestinationGroupCidrs":[
```

`],`

```json
            "SourceGroupCidrs":[
```

`],`

```json
            "ApplicationName":"RDP",
            "Description":"11",
            "HitTimes":0,
            "DestinationType":"net",
            "SourceType":"net",
            "Proto":"TCP",
            "Order":5,
            "ApplicationId":"27",
            "Direction":"in",
            "DestPortType":"port",
            "Source":"1.1.1.1/32",
            "DestPort":"1/1",
            "AclAction":"accept",
            "DestPortGroupPorts":[
```

`],`

```json
            "AclUuid":"53d82f0e-9bf1-4761-ab3b-a070b4811234",
            "Destination":"1.1.1.1/32",
            "DnsResult": "1.1.1.1,2.2.2.2",
            "DnsResultTime": 1579261141
```

`]` For a list of error codes, see Error codes.

#### 6.3.4 AddControlPolicy

Creates an access control policy.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AclAction | String | Yes | accept | The action that Cloud Firewall performs on the traffic. Valid values: accept : allows the traffic. drop: denies the traffic. log: monitors the traffic. |
| Action | String | Yes | AddControlPolicy | The operation that you want to perform. Set the value to AddControlPolicy. |
| ApplicationName | String | Yes | HTTP | The type of applications to which the policy is applied. Valid values: ANY HT T P HT T PS MySQL SMT P SMT PS RDP VNC SSH Redis MQT T MongoDB Memcache SSL Not e ANY, which indicates all types of applications |
| Description | String | Yes | test | The description of the access control policy. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Destination | String | Yes | 1.2.3.4/24 | The destination address in the access control policy. If the DestinationType parameter is set to net, the value of this parameter is the destination CIDR block. Example: 1.2.3.4/24. If the DestinationType parameter is set to group, the value of this parameter is the name of the destination address book. Example: db group. _ If the DestinationType parameter is set to domain, the value of this parameter is the destination domain name. Example: *.aliyuncs.com. If the DestinationType parameter is set to location, the value of this parameter is the destination location. For more information about the location codes, see the following section. Example: ["BJ11", "ZB"]. |
| DestinationType | String | Yes | net | The type of the destination address in the access control policy. net: CIDR block group: destination address book domain: destination domain name location: destination location |
| Direction | String | Yes | in | The direction of the traffic to which the access control policy applies. Valid values: in: inbound traffic out : outbound traffic |
| NewOrder | String | Yes | -1 | The priority of the access control policy. The priority value starts from 1. A smaller value indicates a higher priority. Not e The value -1 indicates the lowest priority. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Proto | String | Yes | TCP | The type of the security protocol in the access control policy. If you are not sure about the protocol type, you can set this parameter to ANY. ANY TCP UDP ICMP |
| Source | String | Yes | 1.2.3.0/24 | The source address in the access control policy. If the SourceType parameter is set to net, the value of this parameter is the source CIDR block. Example: 1.2.3.0/24. If the SourceType parameter is set to group, the value of this parameter is the name of the source address book. Example: db group. _ If the SourceType parameter is set to location, the value of this parameter is the source location. For more information about the location codes, see the following section. Example: ["BJ11", "ZB"]. |
| SourceType | String | Yes | net | The type of the source address in the access control policy. Valid values: net: source CIDR block group: source address book location: source location |
| DestPort | String | No | 80 | The destination port in the access control policy. Not e If the DestPortType parameter is set to port, you must specify this parameter. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DestPortGroup | String | No | my port group _ _ | The name of the destination port address book in the access control policy. Not e If the DestPortType parameter is set to group, you must specify this parameter. |
| DestPortType | String | No | port | The type of the destination port in the access control policy. Valid values: port group: port address book |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| SourceIp | String | No | 1.2.3.5 | The source IP address of the request. |

The following section lists the location codes. China: ZD Beijing: BJ11 Tianjin: TJ12 Hebei: HB13 Shanxi: SX14 Liaoning: LN21 Jilin Province: JL22 Shanghai: SH31 Jiangsu: JS32 Zhejiang: ZJ33 Anhui: AH34 Fujian: FJ35 Jiangxi: JX36 Shandong: SD37 Henan: HN41 Hubei: HB42 Hunan: HN43 Guangdong: GD44 Hainan: HN46 Chongqing: CQ50 Sichuan: SC51 Guizhou: GZ52 Yunnan: YN53 Shaanxi: SX61 Gansu: GS62 Qinghai: QH63 Heilongjiang: HLJ23 Xizang: XZ54 Guangxi: GX45 Nei Mongol: NMG15 Ningxia: NX64 Xinjiang: XJ65 Taiwan: TW Hong Kong S.A.R: HK Macao S.A.R: MO Areas outside China: ZB Asia (excluding China): ZC Europe: EU Africa: AF North America: NA South America: LA Oceania: OA Antarctica: AQ

| Parameter | Type | Example | Description |
|---|---|---|---|
| AclUuid | String | 00281255-d220- 4db1-8f4f- c4df221ad84c | The ID of the access control policy. |
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=AddControlPolicy &AclAction=accept &ApplicationName=ANY &Description=demo_rule_1 &Destination=1.2.3.4/24 &DestinationType=net &Direction=in &NewOrder=-1 &Proto=TCP &Source=1.2.3.0/24 &SourceType=net
```

Sample success responses `XML` format

```xml
<AddControlPolicy>
   <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D</RequestId>
   <AclUuid>00281255-d220-4db1-8f4f-c4df221ad84c</AclUuid>
</AddControlPolicy>
```

`JSON` format

```json
 "RequestId":"CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D",
 "AclUuid":"00281255-d220-4db1-8f4f-c4df221ad84c"
```

For a list of error codes, see Error codes.

#### 6.3.5 DeleteControlPolicy

Deletes an access control policy.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteControlPoli cy | The operation that you want to perform. Set the value to Delet eCont rolPolicy. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AclUuid | String | Yes | 00281255-d220- 4db1-8f4f- c4df221ad84c | The ID of the access control policy. To delete an access control policy, you must specify the ID of the policy. You can call the DescribeControlPolicy operation to obtain the ID. |
| Direction | String | Yes | in | The direction of the traffic to which the access control policy applies. Valid values: in: inbound traffic out : outbound traffic |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the traffic. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteControlPolicy &AclUuid=00281255-d220-4db1-8f4f-c4df221ad84c &Direction=in
```

Sample success responses `XML` format

```xml
<DeleteControlPolicyResponse>
  <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D</RequestId>
</DeleteControlPolicyResponse>
```

`JSON` format

```json
    "RequestId": "CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D"
```

For a list of error codes, see Error codes.

#### 6.3.6 ModifyControlPolicy

Modifies the configuration of an access control policy.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AclAction | String | Yes | accept | The action that Cloud Firewall performs on the traffic. Valid values: accept : allows the traffic. drop: denies the traffic. log: monitors the traffic. |
| AclUuid | String | Yes | 00281255-d220- 4db1-8f4f- c4df221ad84c | The ID of the access control policy. To modify the access control policy, you must specify the ID of the policy. You can call the DescribeControlPolicy operation to obtain the ID. |
| Action | String | Yes | ModifyControlPoli cy | The operation that you want to perform. Set the value to ModifyControlPolicy. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ApplicationName | String | Yes | HTTP | The type of the application that the access control policy supports. Valid values: ANY HT T P HT T PS MySQL SMT P SMT PS RDP VNC SSH Redis MQT T MongoDB Memcache SSL Not e ANY, which all types of applications |
| Description | String | Yes | test | The description of the access control policy. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Destination | String | Yes | 1.2.3.4/24 | The destination address in the access control policy. If the DestinationType parameter is set to net, this parameter specifies the destination CIDR block. Example: 1.2.3.4/24. If the DestinationType parameter is set to group, this parameter specifies the name of the destination address book. Example: db group. _ If the DestinationType parameter is set to domain, this parameter specifies the destination domain name. Example: *.aliyuncs.com. If the DestinationType parameter is set to location, the value of this parameter is the destination location. Example: ["BJ11", "ZB"]. |
| DestinationType | String | Yes | net | The type of the destination address in the access control policy. Valid values: net: destination CIDR block group: destination address book domain: destination domain name location: destination location |
| Direction | String | Yes | in | The direction of the traffic to which the access control policy applies. Valid values: in: inbound traffic out : outbound traffic |
| Proto | String | Yes | TCP | The type of the security protocol in the access control policy. If you are not sure about the protocol type, you can set this parameter to ANY. Valid values: ANY TCP UDP ICMP |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Source | String | Yes | 1.2.3.0/24 | The source address in the access control policy. If the SourceType parameter is set to net, the value of this parameter is the source CIDR block. Example: 1.2.3.0/24. If the SourceType parameter is set to group, the value of this parameter is the name of the source address book. Example: db group. _ If the SourceType parameter is set to location, the value of this parameter is the source location. Example: ["BJ11", "ZB"]. |
| SourceType | String | Yes | net | The type of the source address in the access control policy. Valid values: net: source CIDR block group: source address book location: source location |
| DestPort | String | No | 80 | The destination port in the access control policy. |
| DestPortGroup | String | No | my port group _ _ | The name of the destination port address book in the access control policy. |
| DestPortType | String | No | port | The type of the destination port in the access control policy. Valid values: port group: port address book |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| SourceIp | String | No | 1.2.3.5 | The source IP address of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyControlPolicy &AclAction=accept &AclUuid=00281255-d220-4db1-8f4f-c4df221ad84c &ApplicationName=ANY &Description=demo_rule_1 &Destination=1.2.3.4/24 &DestinationType=net &Direction=in &Proto=TCP &Source=1.2.3.0/24 &SourceType=net
```

Sample success responses `XML` format

```xml
<ModifyControlPolicy>
   <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D</RequestId>
</ModifyControlPolicy>
```

`JSON` format

```json
 "RequestId":"CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D"
```

For a list of error codes, see Error codes.

#### 6.3.7 VPC firewalls

##### 6.3.7.1 CreateVpcFirewallControlPolicy

Creates an access control policy to a specific policy group for a VPC firewall. Not e The VPC firewall instances that are used to protect each Cloud Enterprise Network (CEN) instance and each Express Connect use different access control policies.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVpcFirewal lControlPolicy | The operation that you want to perform. Set the value to Creat eVpcFirewallCont rolPolicy. |
| AclAction | String | Yes | accept | The action that the VPC firewall performs on the traffic. Valid values: accept : allows the traffic. drop: denies the traffic. log: monitors the traffic. |
| ApplicationName | String | Yes | HTTP | The type of the application to which the access control policy applies. Valid values: FTP HTTP HTTPS MySQL SMTP SMTPS RDP VNC SSH Redis MQTT MongoDB Memcache SSL ANY, which indicates all types of applications |
| Description | String | Yes | test | The description of the access control policy. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Destination | String | Yes | 80 | The destination port in the access control policy. Not e If t he Dest Port T ype parameter is set to port , you must specify this parameter. |
| DestinationType | String | Yes | net | The type of the destination address in the access control policy. net : CIDR block group: destination address book domain: destination domain name |
| NewOrder | String | Yes | -1 | The priority of the access control policy. The priority value starts from 1. A smaller value indicates a higher priority. Not e The value -1 indicates the lowest priority. |
| Proto | String | Yes | TCP | The type of the security protocol in the access control policy. If you are not sure about the protocol type, you can set this parameter to ANY. TCP UDP ICMP |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Source | String | Yes | 10.2.3.0/24 | The source address in the access control policy. If the SourceType parameter is set to net , the value of this parameter is the source CIDR block. Example: 10.2.3.0/24. If the SourceType parameter is set to group , the value of this parameter is the name of the source address book. Example: db group. _ |
| SourceType | String | Yes | net | The type of the source address in the access control policy. Valid values: net : source CIDR block group: source address book |
| VpcFirewallId | String | Yes | vfw- a42bbb7b887148 c9**** | The ID of the access control policy group. You can call the DescribeVpcFirewallAclGroupList operation to obtain the ID. Valid values: If the VPC firewall is used to protect a Cloud Enterprise Network (CEN) instance, the ID of the CEN instance is used. Example: cen- ervw5jbw1234*****. If the VPC firewall is used to protect an Express Connect, the ID of the VPC firewall instance is used. Example: vfw- a42bbb748c91234*****. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DestPort | String | No | 80 | The destination port in the access control policy. Not e If the DestPortType parameter is set to port , you must specify this parameter. |
| DestPortType | String | No | net | The type of the destination port in the access control policy. port group: port address book |
| DestPortGroup | String | No | my port group _ _ | The name of the destination port address book in the access control policy. Not e If the DestPortType parameter is set to group , you must specify this parameter. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AclUuid | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |
| RequestId | String | 00281255-d220- 4db1-8f4f- c4df221ad84c | The ID of the access control policy. |

Sample requests

```
http(s)://[Endpoint]/?Action=CreateVpcFirewallControlPolicy &VpcFirewallId=vfw-a42bbb7b887148c9**** &AclAction=accept &ApplicationName=ANY &Description=demo_rule_1 &Destination=10.2.3.0/24 &DestinationType=net &NewOrder=-1 &Proto=TCP &Source=10.2.3.0/24 &SourceType=net
```

Sample success responses `XML` format

```xml
<CreateVpcFirewallControlPolicyResponse>
  <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D</RequestId>
  <AclUuid>00281255-d220-4db1-8f4f-c4d*********</AclUuid>
</CreateVpcFirewallControlPolicyResponse>
```

`JSON` format

```json
    "RequestId": "CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D",
    "AclUuid": "00281255-d220-4db1-8f4f-c4d*********"
```

For a list of error codes, see Error codes.

##### 6.3.7.2 DescribeVpcFirewallControlPolicy

Queries the information of the access control policies for a specific VPC firewall. Not e The VPC firewall instances that are used to protect each Cloud Enterprise Network (CEN) instance and each Express Connect use different access control policies.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpcFirew allControlPolicy | The operation that you want to perform. Set the value to DescribeVpcFirewallCont rolPolicy. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| CurrentPage | String | Yes | 1 | The page number of the current page. Default value: 1. |
| PageSize | String | Yes | 10 | The number of entries to return on each page. Maximum value: 50. |
| VpcFirewallId | String | Yes | vfw- a42bbb7b887148 c9**** | The ID of the access control policy group. You can call the DescribeVpcFirewallAclGroupList operation to obtain the ID. Valid values: If the VPC firewall is used to protect a CEN instance, the ID of the CEN instance is used. Example: cen-ervw0g12b5jbw****. If the VPC firewall is used to protect an Express Connect, the ID of the VPC firewall instance is used. Example: vfw- a42bbb7b887148c9****. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Source | String | No | 10.0.1.0/24 | The source address in the access control policy. Fuzzy match is supported. Valid values: If the SourceT ype parameter is set to net , the value of this parameter is the source CIDR block. Example: 10.0.1.0/24. If the SourceT ype parameter is set to group , the value of this parameter is the name of the source address book. Example: db group. _ If the SourceType parameter is not specified, all sources are queried. Not e The valid values of this parameter depend on the value of the SourceType parameter. |

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| Destination | String | No | 10.0.3.0 | The destination address in the access control policy. Fuzzy match is supported. Valid values: If the Dest inat ionT ype parameter is set to net , the value of this parameter is the destination CIDR block. Example: 10.0.3.0/24. If the Dest inat ionT ype is set to d omain , the value of this parameter is the destination domain name. Example: aliyun.com. If the Dest inat ionT ype parameter is set to group , the value of this parameter is the name of the destination address book. Example: db group. _ If the DestinationType parameter is not specified, all destination addresses are queried. Not e The valid values of this parameter depend on the value of the DestinationType parameter. |   |   |
|   |   |   |   |   | d |   |
| Description | String | No | test | The description of the access control policy. Fuzzy match is supported. Not e If this parameter is not specified, the descriptions of all access control policies are queried. |   |   |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Proto | String | No | TCP | The type of the protocol in the access control policy. Valid values: TCP UDP ICMP ANY, which indicates all types of protocols |
| AclAction | String | No | accept | The action that Cloud Firewall performs on the traffic. Valid values: accept : allows the traffic. drop: denies the traffic. log: monitors the traffic. If this parameter is not specif ied, access control policies that specify all the preceding actions are queried. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Policys | Array |   | The information of the access control policy. |
| AclAction | String | accept | The action that Cloud Firewall performs on the traffic. Valid values: accept : allows the traffic. drop: denies the traffic. log: monitors the traffic. |
| AclUuid | String | 00281255-d220- 4db1-8f4f- c4df221a**** | The ID of the access control policy. |
| ApplicationId | String | 10** | The application ID in the access control policy. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ApplicationNa me | String | HTTP | The type of the application that the access control policy supports. Valid values: HTTP HTTPS MySQL SMTP SMTPS RDP VNC SSH Redis MQTT MongoDB Memcache SSL ANY, which indicates all types of applications |
| Description | String | test | The description of the access control policy. |
| DestPort | String | 80 | The destination port in the access control policy. |
| DestPortGroup | String | my port group _ _ | The name of the destination port address book in the access control policy. |
| DestPortGroup Ports | List | [80,443] | The ports in the destination port address book. |
| DestPortType | String | port | The type of the destination port in the access control policy. Valid values: port group: port address book |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Destination | String | 10.0.3.0/24 | The destination address in the access control policy. Valid values: If the Dest inat ionT ype parameter is set to net , the value of this parameter is the destination CIDR block. Example: 10.0.3.0/24. If the Dest inat ionT ype parameter is set to domain , the value of this parameter is the destination domain name. Example: aliyuncs.com. If the Dest inat ionT ype parameter is set to group , the value of this parameter is the name of the destination address book. Example: db group. _ Not e The valid values of this parameter depend on the value of the DestinationType parameter. |
| DestinationGro upCidrs | List | ["10.0.4.0/24", "10.0.0.1/32"] | The CIDR blocks in the destination address book. |
| DestinationTyp e | String | net | The type of the destination address in the access control policy. Valid values: net : destination CIDR block group: destination address book domain: destination domain name |
| Direction | String | in | The direction of traffic to which the access control policy applies. Valid values: in: inbound traffic out : outbound traffic |
| HitTimes | Integer | 100 | The number of hits for the access control policy. |

| eveloper Guide·Cl | oud Firewall |   | Apsara Stack Securit |
|---|---|---|---|

| Parameter | Type | Example | Description |   |   |
|---|---|---|---|---|---|
| Order | Integer | 1 | The priority of the access control policy. The priority value starts from 1. A smaller value indicates a higher priority. The value -1 indicates the lowest priority. |   |   |
| Proto | String | TCP | The type of the protocol in the access control policy. Valid values: TCP UDP ICMP ANY, which indicates all types of protocols |   |   |
| Source | String | 10.0.6.0/24 | The source address in the access control policy. Valid values: If the SourceT ype parameter is set to n et , the value of this parameter is the source CIDR block. Example: 10.0.6.0/24. If the SourceT ype parameter is set to g roup , the value of this parameter is the name of the source address book. Example: db group. _ Not e The valid values of this parameter depend on the value of the SourceType parameter. |   |   |
|   |   |   |   | g |   |
| SourceGroupCid rs | List | ["10.0.6.0/24", "10.0.0.2/32"] | The CIDR blocks in the source address book of the access control policy. |   |   |
| SourceType | String | net | The type of the source address in the access control policy. Valid values: net : source CIDR block group: source address book |   |   |

| n |   |
|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |
| TotalCount | String | 20 | The total number of the access control policies. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVpcFirewallControlPolicy &VpcFirewallId=vfw-a42bbb7b887148c9**** &CurrentPage=1 &PageSize=10
```

Sample success responses `XML` format

```xml
<DescribeVpcFirewallControlPolicyResponse>
  <TotalCount>1</TotalCount>
  <PageNo>1</PageNo>
  <PageSize>10</PageSize>
  <RequestId>A08BC58F-A83D-43EB-BC31-2F0D723929CC</RequestId>
  <Policys>
        <ApplicationName>HTTP</ApplicationName>
        <Description>11</Description>
        <HitTimes>0</HitTimes>
        <DestinationType>net</DestinationType>
        <SourceType>net</SourceType>
        <Proto>TCP</Proto>
        <Order>5</Order>
        <ApplicationId>27</ApplicationId>
        <DestPortType>port</DestPortType>
        <Source>10.1.1.1/32</Source>
        <DestPort>80/80</DestPort>
        <AclAction>accept</AclAction>
        <AclUuid>53d82f0e-9bf1-4761-ab3b-a070b4811234</AclUuid>
        <Destination>10.2.1.1/32</Destination>
  </Policys>
</DescribeVpcFirewallControlPolicyResponse>
```

`JSON` format

```json
    "TotalCount":1,
    "PageNo":1,
    "PageSize":10,
    "RequestId":"A08BC58F-A83D-43EB-BC31-2F0D723929CC",
    "Policys":[
            "DestinationGroupCidrs":[
```

`],`

```json
            "SourceGroupCidrs":[
```

`],`

```json
            "ApplicationName":"HTTP",
            "Description":"11",
            "HitTimes":0,
            "DestinationType":"net",
            "SourceType":"net",
            "Proto":"TCP",
            "Order":5,
            "ApplicationId":"27",
            "DestPortType":"port",
            "Source":"10.1.1.1/32",
            "DestPort":"80/80",
            "AclAction":"accept",
            "DestPortGroupPorts":[
```

`],`

```json
            "AclUuid":"53d82f0e-9bf1-4761-ab3b-a070b4811234",
            "Destination":"10.2.1.1/32"
```

`]` For a list of error codes, see Error codes.

##### 6.3.7.3 ModifyVpcFirewallControlPolicy

Modifies the configuration of an access control policy in a specific policy group for a VPC firewall. Not e The VPC firewall instances that are used to protect each Cloud Enterprise Network (CEN) instance and each Express Connect use different access control policies.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVpcFirewal lControlPolicy | The operation that you want to perform. Set the value to Modif yVpcFirewallCont rolPolicy. |
| AclAction | String | Yes | accept | The action that Cloud Firewall performs on the traffic. Valid values: accept : allows the traffic. drop: denies the traffic. log: monitors the traffic. |
| AclUuid | String | Yes | 00281255-d220- 4db1-8f4f- c4df221ad84c | The ID of the access control policy. To modify the configuration of an access control policy, you must provide the ID of the policy. You can call the DescribeVpcFirewallControlPolicy operation to obtain the ID. |
| ApplicationName | String | Yes | HTTP | The type of applications to which the access control policy applies. Valid values: ANY FTP HTTP HTTPS MySQL SMTP SMTPS RDP VNC SSH Redis MQTT MongoDB Memcache SSL ANY, which indicates all types of applications |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Description | String | Yes | test | The description of the access control policy. |
| Destination | String | Yes | 10.2.3.0/24 | The destination address in the access control policy. If the Dest inat ionT ype parameter is set to net , the value of this parameter is the destination CIDR block. Example: 10.2.3.0/24. If the Dest inat ionT ype parameter is set to group , the value of this parameter is the name of the destination address book. Example: db group. _ If the Dest inat ionT ype parameter is set to domain , the value of this parameter is the destination domain name. Example: *.aliyuncs.com. |
| DestinationType | String | Yes | net | The type of the destination address in the access control policy. Valid values: net : CIDR block group: destination address book domain: destination domain name |
| Proto | String | Yes | TCP | The type of the security protocol in the access control policy. Valid values: ANY, which indicates all types of protocols TCP UDP ICMP |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Source | String | Yes | 10.2.4.0/24 | The source address in the access control policy. Valid values: If the SourceT ype parameter is set to net , the value of this parameter is the source CIDR block. Example: 10.2.4.0/24 If the SourceT ype parameter is set to group , the value of this parameter is the name of the source address book. Example: db group _ |
| SourceType | String | Yes | net | The type of the source address in the access control policy. Valid values: net : source CIDR block. group: source address book |
| VpcFirewallId | String | Yes | vfw- a42bbb7b887148 c9**** | The ID of the access control policy group. You can call the DescribeVpcFirewallAclGroupList operation to obtain the ID. If the VPC firewall is used to protect a Cloud Enterprise Network (CEN) instance, the ID of the CEN instance is used. Example: cen-ervw0g12b5jbw****. If the VPC firewall is used to protect an Express Connect, the ID of the VPC firewall instance is used. Example: vfw- a42bbb7b887148c9****. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DestPort | String | No | 80 | The destination port in the access control policy. |
| DestPortType | String | No | port | The type of the destination port in the access control policy. port group: port address book |
| DestPortGroup | String | No | my port group _ _ | The name of the destination port address book in the access control policy. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyVpcFirewallControlPolicy &VpcFirewallId=vfw-a42bbb7b887148c9**** &AclAction=accept &AclUuid=00281255-d220-4db1-8f4f-c4df221ad84c &ApplicationName=ANY &Description=demo_rule_1 &Destination=10.2.3.0/24 &DestinationType=net &Proto=TCP &Source=10.2.4.0/24 &SourceType=net
```

Sample success responses `XML` format

```xml
<ModifyVpcFirewallControlPolicyResponse>
  <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D</RequestId>
</ModifyVpcFirewallControlPolicyResponse>
```

`JSON` format

```json
    "RequestId": "CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D"
```

For a list of error codes, see Error codes.

##### 6.3.7.4 ModifyVpcFirewallControlPolicyPosition

Modifies the priority of an access control policy in a specific policy group for a VPC firewall.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVpcFirewal lControlPolicyPosi tion | The operation that you want to perform. Set the value to Modif yVpcFirewallCont rolPolicyPo sit ion. |
| NewOrder | String | Yes | 1 | The new priority of the access control policy. |
| OldOrder | String | Yes | 5 | The original priority of the access control policy. |
| VpcFirewallId | String | Yes | vfw- a42bbb7b887148 c9**** | The ID of the access control policy group. You can call the DescribeVpcFirewallAclGroupList operation to obtain the ID. Valid values: If the VPC firewall is used to protect a Cloud Enterprise Network (CEN) instance, the ID of the CEN instance is used. Example: cen-ervw0g12b5jbw****. If the VPC firewall is used to protect an Express Connect, the ID of the VPC firewall instance is used. Example: vfw- a42bbb7b887148c9****. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 850A84D6-0DE4- 4797-A1E8- 00090125EEB1 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyVpcFirewallControlPolicyPosition &VpcFirewallId=vfw-a42bbb7b887148c9**** &NewOrder=1 &OldOrder=5
```

Sample success responses `XML` format

```xml
<ModifyVpcFirewallControlPolicyPositionResponse>
  <RequestId>850A84D6-0DE4-4797-A1E8-00090125EEB1</RequestId>
</ModifyVpcFirewallControlPolicyPositionResponse>
```

`JSON` format

```json
    "RequestId": "850A84D6-0DE4-4797-A1E8-00090125EEB1"
```

For a list of error codes, see Error codes.

##### 6.3.7.5 DeleteVpcFirewallControlPolicy

Deletes an access control policy from a specific policy group for a VPC firewall. Not e The VPC firewall instances that are used to protect each Cloud Enterprise Network (CEN) instance and each Express Connect use different access control policies.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVpcFirewal lControlPolicy | The operation that you want to perform. Set the value to Delet eVpcFirewallCont rolPolicy. |
| AclUuid | String | Yes | 00281255-d220- 4db1-8f4f- c4df2214**** | The ID of the access control policy. To delete an access control policy, you must specify the ID of the policy. You can call the DescribeVpcFirewallCont rolPolicy operation to obtain the ID. |
| VpcFirewallId | String | Yes | vfw- a42bbb7b887148 c91**** | The ID of the access control policy group. You can call the DescribeVpcFirewallAclGroupList operation to obtain the ID. Valid values: If the VPC firewall is used to protect a CEN instance, the ID of the CEN instance is used. Example: cen-ervw0g12b5jbw****. If the VPC firewall is used to protect an Express Connect, the ID of the VPC firewall instance is used. Example: vfw- a42bbb7b887148c9****. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteVpcFirewallControlPolicy &VpcFirewallId=vfw-a42bbb7b887148c9**** &AclUuid=00281255-d220-4db1-8f4f-c4df221ad84c
```

Sample success responses `XML` format

```xml
<DeleteVpcFirewallControlPolicyResponse>
  <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D</RequestId>
</DeleteVpcFirewallControlPolicyResponse>
```

`JSON` format

```json
    "RequestId": "CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D"
```

For a list of error codes, see Error codes.

##### 6.3.7.6 DescribeVpcFirewallPolicyPriorUsed

Queries the priority range of the access control policies in a specific policy group for a VPC firewall.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpcFirew allPolicyPriorUsed | The operation that you want to perform. Set the value to DescribeVpcFirewallPolicyPriorUse d. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VpcFirewallId | String | Yes | vfw- a42bbb7b887148 c9**** | The ID of the access control policy group. You can call the DescribeVpcFirewallAclGroupList operation to obtain the ID. Valid values: If the VPC firewall is used to protect a Cloud Enterprise Network (CEN) instance, the ID of the CEN instance is used. Example: cen-ervw0g12b5jbw****. If the VPC firewall is used to protect an Express Connect, the ID of the VPC firewall instance is used. Example: vfw- a42bbb7b887148c9****. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Example | Description |
|---|---|---|---|
| End | Integer | 150 | The lowest priority for the access control policy. |
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |
| Start | Integer | 1 | The highest priority for the access control policy. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVpcFirewallPolicyPriorUsed &VpcFirewallId=vfw-a42bbb7b887148c9****
```

Sample success responses `XML` format

```xml
<DescribeVpcFirewallPolicyPriorUsedResponse>
  <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D</RequestId>
  <Start>1</Start>
  <End>150</End>
</DescribeVpcFirewallPolicyPriorUsedResponse>
```

`JSON` format

```json
    "RequestId": "CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D",
    "Start": 1,
    "End": 150
```

For a list of error codes, see Error codes.

##### 6.3.7.7 DescribeVpcFirewallAclGroupList

Queries information about all access control policy groups for a VPC firewall.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpcFirew allAclGroupList | The operation that you want to perform. Set the value to DescribeVpcFirewallAclGroupList . |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| FirewallConfigure Status | String | No | configured | Specifies whether VPC firewalls are configured. not conf igured: VPC firewalls are not configured. conf igured: VPC firewalls are configured. If you do not specify this parameter, all access control policy groups are queried. |
| CurrentPage | String | No | 1 | The page number of the current page. Default value: 1 |
| PageSize | String | No | 10 | The number of entries to return on each page. Maximum value: 50. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AclGroupList | Array |   | The information about the access control policy group. |
| AclGroupId | String | vfw- a42bbb7b887148c9* *** | The ID of the access control policy group. You can call the DescribeVpcFirewallAclGroupList operation to obtain the ID. Valid values: If the VPC firewall is used to protect a Cloud Enterprise Network (CEN) instance, the ID of the CEN instance is used. Example: cen-ervw0g12b5jbw****. If the VPC firewall is used to protect an Express Connect, the ID of the VPC firewall instance is used. Example: vfw-a42bbb7b887148c9****. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AclGroupName | String | group test _ | The name of the access control policy group. If the VPC firewall is used to protect a CEN instance, the name of the CEN instance is used. If the VPC firewall is used to protect an Express Connect, the name of the VPC firewall is used. |
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |
| TotalCount | Integer | 1 | The total number of access control policy groups. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVpcFirewallAclGroupList &FirewallConfigureStatus=configured
```

Sample success responses `XML` format

```xml
<DescribeVpcFirewallAclGroupListResponse>
  <TotalCount>1</TotalCount>
  <AclGroupList>
        <AclGroupId>vfw-a42bbb7b887148c9****</AclGroupId>
        <AclGroupName>group_test</AclGroupName>
  </AclGroupList>
</DescribeVpcFirewallAclGroupListResponse>
```

`JSON` format

```json
{"TotalCount":1,"AclGroupList":[{"AclGroupId":"vfw-a42bbb7b887148c9****","AclGroupName":"gr oup_test"}]}
```

For a list of error codes, see Error codes.

##### 6.3.7.8 ResetVpcFirewallRuleHitCount

Resets the count on hits of an access control policy in a specific policy group for a VPC firewall.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ResetVpcFirewall RuleHitCount | The operation that you want to perform. Set the value to Reset VpcFirewallRuleHit Count . |
| AclUuid | String | Yes | 00281255-d220- 4db1-8f4f- c4df221ad84c | The ID of the access control policy. To delete an access control policy, you must specify the ID of the policy. You can call the DescribeVpcFirewallControlPolicy operation to obtain the ID. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=ResetVpcFirewallRuleHitCount &AclUuid=00281255-d220-4db1-8f4f-c4df221a1234
```

Sample success responses `XML` format

```xml
<ResetVpcFirewallRuleHitCountResponse>
  <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D</RequestId>
</ResetVpcFirewallRuleHitCountResponse>
```

`JSON` format

```json
    "RequestId": "CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D"
```

For a list of error codes, see Error codes.

### 6.4 Firewall switch

#### 6.4.1 PutEnableFwSwitch

Turns on a firewall switch.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | PutEnableFwSwit ch | The operation that you want to perform. Set the value to PutEnableFwSwitch. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| IpaddrList.N | RepeatLi st | No | ["1.2.3.4","5.6.7.8 "] | The list of IP addresses. |
| RegionList.N | RepeatLi st | No | ["cn- hangzhou","cn- shanghai"] | The list of regions. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ResourceTypeList .N | RepeatLi st | No | ["EcsPublicIp","Na tEip"] | The list of asset types. Valid values: BastionHostIP: the IP address of a bastion host EcsEIP: the EIP of an ECS instance EcsPublicIP: the public IP address of an ECS instance EIP EniEIP: the EIP of an ENI NatEIP: the EIP of a NAT gateway SlbEIP: the EIP of an SLB instance SlbPublicIP: the public IP address of an SLB instance NatPublicIP: the public IP address of a NAT gateway HAVIP: the HA VIP |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B2841452-CB8D- 4F7D-B247- 38E1CF7334F8 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=PutEnableFwSwitch&IpaddrList=["1.2.3.4","5.6.7.8"]
```

Sample success responses `XML` format

```xml
<RequestId>B2841452-CB8D-4F7D-B247-38E1CF7334F8</RequestId>
```

`JSON` format

```json
    "RequestId":"B2841452-CB8D-4F7D-B247-38E1CF7334F8"
```

For a list of error codes, see Error codes.

#### 6.4.2 PutDisableFwSwitch

Turns off a firewall switch.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | PutDisableFwSwit ch | The operation that you want to perform. Set the value to PutDisableFwSwitch. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| IpaddrList.N | RepeatLi st | No | ["1.2.3.4","5.6.7.8 "] | The list of IP addresses. |
| RegionList.N | RepeatLi st | No | ["cn- hangzhou","cn- shanghai"] | The list of regions. |
| ResourceTypeList .N | RepeatLi st | No | ["EcsPublicIp","Na tEip"] | The list of asset types. Valid values: BastionHostIP: the IP address of a bastion host EcsEIP: the EIP of an ECS instance EcsPublicIP: the public IP address of an ECS instance EIP EniEIP: the EIP of an ENI NatEIP: the EIP of a NAT gateway SlbEIP: the EIP of an SLB instance SlbPublicIP: the public IP address of an SLB instance NatPublicIP: the public IP address of a NAT gateway HAVIP: the HA VIP |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B2841452-CB8D- 4F7D-B247- 38E1CF7334F8 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=PutDisableFwSwitch&IpaddrList=["1.2.3.4","5.6.7.8"]
```

Sample success responses `XML` format

```xml
<RequestId>B2841452-CB8D-4F7D-B247-38E1CF7334F8</RequestId>
```

`JSON` format

```json
    "RequestId":"B2841452-CB8D-4F7D-B247-38E1CF7334F8"
```

For a list of error codes, see Error codes.

#### 6.4.3 PutEnableAllFwSwitch

Turns on all firewall switches.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | PutEnableAllFwS witch | The operation that you want to perform. Set the value to PutEnableAllFwSwitch. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B2841452-CB8D- 4F7D-B247- 38E1CF7334F8 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=PutEnableAllFwSwitch
```

Sample success responses `XML` format

```xml
<RequestId>B2841452-CB8D-4F7D-B247-38E1CF7334F8</RequestId>
```

`JSON` format

```json
    "RequestId":"B2841452-CB8D-4F7D-B247-38E1CF7334F8"
```

For a list of error codes, see Error codes.

#### 6.4.4 PutDisableAllFwSwitch

Turns off all firewall switches.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | PutDisableAllFwS witch | The operation that you want to perform. Set the value to PutDisableAllFwSwitch. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B2841452-CB8D- 4F7D-B247- 38E1CF7334F8 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=PutDisableAllFwSwitch
```

Sample success responses `XML` format

```xml
<RequestId>B2841452-CB8D-4F7D-B247-38E1CF7334F8</RequestId>
```

`JSON` format

```json
    "RequestId":"B2841452-CB8D-4F7D-B247-38E1CF7334F8"
```

For a list of error codes, see Error codes.

### 6.5 Address books

#### 6.5.1 AddAddressBook

Creates an address book for access control. Supported address book types are IP address books, Elastic Compute Service (ECS) tag address books, port address books, and domain address books.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddAddressBook | The operation that you want to perform. Set the value to AddAddressBook. |
| Description | String | Yes | DEMO address book | The description of the address book. |
| GroupName | String | Yes | demo address b _ _ ook | The name of the address book. |
| GroupType | String | Yes | ip | The type of the address book. Valid values: ip: IP address book domain: domain address book port : port address book t ag: ECS tag address book |
| AddressList | String | No | 1.2.3.4/32, 1.2.3.0/24 | The addresses you want to add to the address book. Separate multiple addresses with commas (,). Not e If the GroupType parameter is set to ip, port or domain, this parameter is required. If the GroupType parameter is set to ip, the value of this parameter is the IP addresses. Example: 1.2.3.4/32,1.2.3.0/24. If the GroupType parameter is set to port, the value of this parameter is the ports or port ranges. Example: 80,100/200. If the GroupType parameter is set to domain, the value of this parameter is the domain names. Example: demo1.aliyun.com,demo2.aliyun.co m. |
| AutoAddTagEcs | String | No | 1 | Specifies whether to automatically add public IP addresses of ECS instances to the address book if they match the specific tags. Valid values: 1: yes 0: no |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| TagList.N.TagKey | String | No | key1 | The key of ECS tag N you want to match. |
| TagList.N.TagVal ue | String | No | value1 | The value of ECS tag N you want to match. |
| TagRelation | String | No | and | The logical relation among ECS tags you want to mach. Valid values: and: Only the public IP addresses of ECS instances that match all the specific tags can be added to the address book. or: The public IP addresses of ECS instances that match any of the specific tags can be added to the address book. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| GroupUuid | String | f04ac7ce-628b- 4cb7-be61- 310222b718e8 | The ID of the returned address book |
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=AddAddressBook &Description=DEMO address book &GroupName=demo_address_book &GroupType=ip &AddressList=1.2.3.4/32,1.2.3.0/24
```

Sample success responses `XML` format

```xml
<AddAddressBook>
      <RequestId>B2841452-CB8D-4F7D-B247-38E1CF7334F8</RequestId>
      <GroupUuid>0580bbd0-24cd-47ae-9e5a-f5a099251e32</GroupUuid>
    </AddAddressBook>
```

`JSON` format

```json
    "RequestId":"B2841452-CB8D-4F7D-B247-38E1CF7334F8",
    "GroupUuid":"0580bbd0-24cd-47ae-9e5a-f5a099251e32"
```

For a list of error codes, see Error codes.

#### 6.5.2 DeleteAddressBook

Deletes an address book for access control.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteAddressBo ok | The operation that you want to perform. Set the value to DeleteAddressBook. |
| GroupUuid | String | Yes | 0657ab9d-fe8b- 4174-b2a6- 6baf358ea4ad | The ID of the address book. To delete the address book, you must specify the ID of the address book. You can call the DescribeAddressBook operation to obtain the ID. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteAddressBook &GroupUuid=0657ab9d-fe8b-4174-b2a6-6baf358ea4ad
```

Sample success responses `XML` format

```xml
<DeleteAddressBook>
   <RequestId>850A84D6-0DE4-4797-A1E8-00090125EEB1</RequestId>
</DeleteAddressBook>
```

`JSON` format

```json
 "RequestId":"850A84D6-0DE4-4797-A1E8-00090125EEB1"
```

For a list of error codes, see Error codes.

#### 6.5.3 ModifyAddressBook

Modifies an address book for the access control.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyAddressBo ok | The operation that you want to perform. Set the value to ModifyAddressBook. |
| Description | String | Yes | DEMO address book | The description of the address book. |
| GroupName | String | Yes | demo address b _ _ ook | The name of the address book. |
| GroupUuid | String | Yes | 0657ab9d-fe8b- 4174-b2a6- 6baf358ea4ad | The ID of the address book. To modify the address book, you must specify the ID of the address book. You can call the DescribeAddressBook operation to obtain the ID. |
| AddressList | String | No | 1.1.1.1/32, 2.2.2.0/24 | The addresses you want to add to the address book. Separate multiple addresses with commas (,). Not e If the GroupType parameter is set to ip, port, or domain, this parameter is required. If the GroupType parameter is set to ip, the value of this parameter is the IP addresses. Example: 1.2.3.4/32,1.2.3.0/24. If the GroupType parameter is set to port, the value of this parameter is the ports or port ranges. Example: 80,100/200. If the GroupType parameter is set to domain, the value of this parameter is the domain names. Example: demo1.aliyun.com,demo2.aliyun.co m. |
| AutoAddTagEcs | String | No | 1 | Specifies whether to automatically add the public IP addresses of ECS instances to the address book if they match the specific tags. Valid values: 1: yes 0: no |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| TagList.N.TagKey | String | No | key1 | The key of ECS tag N you want to match. |
| TagList.N.TagVal ue | String | No | value1 | The value of ECS tag N you want to match. |
| TagRelation | String | No | and | The logical relation among ECS tags. Valid values: and: Only the public IP addresses of ECS instances that match all the specific tags can be added to the address book. or: The public IP addresses of ECS instances that match any of the specific tags can be added to the address book. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyAddressBook &GroupUuid=0657ab9d-fe8b-4174-b2a6-6baf358ea4ad &Description=DEMO address book &GroupName=demo_address_book &GroupType=ip &AddressList=1.1.1.1/32,2.2.2.0/24
```

Sample success responses `XML` format

```xml
<ModifyAddressBook>
      <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D</RequestId>
</ModifyAddressBook>
```

`JSON` format

```json
    "RequestId":"CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D"
```

For a list of error codes, see Error codes.

#### 6.5.4 DescribeAddressBook

Queries the details of an address book for the access control.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAddressB ook | The operation that you want to perform. Set the value to DescribeAddressBook. |
| ContainPort | String | No | 80 | Details about the address book that contains ports.This parameter only takes effect when the GroupT ype parameter is set to port . |
| CurrentPage | String | No | 1 | The number of the page to return. Default value: 1. |
| GroupType | String | No | ip | The type of the address book. Valid values: ip: IP address book domain: domain address book port : port address book t ag: ECS tag address book |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| PageSize | String | No | 50 | The number of entries to return on each page. Maximum value: 50. |
| Query | String | No | 1.2.3.0 | The query condition that specifies the address book. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Acls | Array |   | The information about the address book. |
| AddressList | List | [ "1.2.3.4/32", "0.0.0.0/0" ] | The addresses in the address book. |
| AddressListCou nt | Integer | 2 | The number of addresses in the address book. |
| AutoAddTagEc s | Integer | 1 | Indicates whether to automatically add the public IP addresses of ECS instances to the address book if they match the specific tags. Valid values: 1: yes 0: no |
| Description | String | DEMO address book | The description of the address book. |
| Global | Integer | 0 | Indicates whether the address book is global. Valid values: 1: yes 0: no |
| GroupName | String | demo address boo _ _ k | The name of the address book. |

| eveloper Guide·Cl | oud Firewall |   | Apsara Stack Securit |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| GroupType | String | ip | The type of the address book. Valid values: ip: IP address book domain: domain address book port : port address book t ag: ECS tag address book |
| GroupUuid | String | f04ac7ce-628b- 4cb7-be61- 310222b718e8 | The ID of the address book. |
| ReferenceCount | Integer | 3 | The number of times the address book is referenced. |
| TagList | Array |   | Details about the ECS tags that can be automatically added to the address book. |
| TagKey | String | key1 | The key of ECS tag N you want to match. |
| TagValue | String | value1 | The value of ECS tag N you want to match. |
| TagRelation | String | and | The logical relation among ECS tags. Valid values: and: Only the public IP addresses of ECS instances that match all the specific tags can be added to the address book. or: The public IP addresses of ECS instances that match any of the specific tags can be added to the address book. |
| PageNo | String | 1 | The number of the current page. |
| PageSize | String | 10 | The number of entries returned per page. |
| RequestId | String | B36F150A-1E27- 43AA-B72C- D2AC712F09DA | The ID of the request. |
| TotalCount | String | 100 | The number of address books. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeAddressBook
```

Sample success responses `XML` format

```xml
<DescribeAddressBook>
   <TotalCount>123</TotalCount>
   <PageSiNo>1</PageSiNo>
   <PageSize>1</PageSize>
   <RequestId>B36F150A-1E27-43AA-B72C-D2AC712F09DA</RequestId>
   <Acls>
      <Description>9-3 IP address book</Description>
      <GroupType>ip</GroupType>
      <AddressList>1.2.3.4/32</AddressList>
      <AddressList>0.0.0.0/0</AddressList>
      <GroupName>9-3 IP address book</GroupName>
      <AutoAddTagEcs>0</AutoAddTagEcs>
      <TagValue></TagValue>
      <TagRelation></TagRelation>
      <ReferenceCount>0</ReferenceCount>
      <TagKey></TagKey>
      <AddressListCount>2</AddressListCount>
      <GroupUuid>a3c5e-018e-4c08-bea8-eafc95d1a54e</GroupUuid>
      <Global>0</Global>
   </Acls>
</DescribeAddressBook>
```

`JSON` format

```json
 "TotalCount":123,
 "PageSize":1,
 "RequestId":"B36F150A-1E27-43AA-B72C-D2AC712F09DA",
 "Acls":[
   "Description":"9-3 IP address book",
   "GroupType":"ip",
   "AddressList":[
    "1.2.3.4/32",
    "0.0.0.0/0"
```

`],`

```json
   "GroupName":"9-3 IP address book",
   "AutoAddTagEcs":0,
   "TagValue":"",
   "TagRelation":"",
   "TagList":[],
   "ReferenceCount":0,
   "TagKey":"",
   "AddressListCount":2,
   "GroupUuid":"a3c5e-018e-4c08-bea8-eafc95d1a54e",
   "Global":0
```

`],`

```json
 "PageSiNo":1
```

For a list of error codes, see Error codes. covery and Protection

## 7 Sensitive Data Discovery and Protection

Protection

### 7.1 List of operations by function

The following tables lists API operations available for use in Sensitive Data Discovery and Protection (SDDP).

| Operation | Description |
|---|---|
| DescribeDataAssets |   |
| DescribeInstances |   |
| DescribeTables |   |
| DescribePackages |   |
| DescribeColumns |   |
| DescribeOssObjects |   |
| DescribeOssObjectDetail |   |
| DescribeDeparts |   |
| DescribeAccounts |   |
| DescribeAccountDetail |   |
| DescribePrivileges |   |
| DescribeEventTypes |   |
| DescribeEvents |   |
| DescribeEventDetail |   |
| ModifyEventStatus |   |
| ModifyEventTypeStatus |   |
| ModifyDefaultLevel |   |
| DescribeRules |   |
| CreateRule |   |
| ModifyRule |   |
| ModifyRuleStatus |   |

| overy and Protection | Apsara Stack Securit |
|---|---|

| Operation | Description |
|---|---|
| DeleteRule |   |
| DescribeDataLimitSet |   |
| CreateDataLimit |   |
| DeleteDataLimit |   |

### 7.2 Make API requests

#### 7.2.1 Request structure

Apsara Stack Security API operations use the Remote Procedure Call (RPC) protocol. This topic describes the API request syntax. You can call API operations by sending HTTP requests. The request syntax is as follows:

```
http://endpoint/?Action=xx&parameters
```

Where:

|   | endpoint |   | : the endpoi |
|---|---|---|---|
| RegionId].example.com |   |   |   |
|   | Action | : the name of t |   |

`endpoint` : the endpoint of the Sensitive Data Discovery and Protection (SDDP) API is `sddp-api.[` `Action` : the name of the operation being performed. For example, to query data assets, you must set the Action parameter to DescribeDataAssets.

| parameters |   | : th |
|---|---|---|
| ampersands ( | & |   |

`parameters` : the request parameters for the operation. Separate multiple parameters with ampersands ( `&` ). Request parameters include both common parameters and operation-specific parameters. Common parameters include information such as the API version and authentication information. For more information about operation-specific parameters, see the corresponding operation description. The following example demonstrates how to call the DescribeDataAssets operation to query data assets:

```
https://sddp-api.[ RegionId].example.com/?Action=DescribeDataAssets&CurrentPage=1&PageSize= 10&AccessKeyId=key-test&Format=JSON&SecureTransport=true&SignatureMethod=HMAC-SHA1&Signatur eNonce=15215528852396&SignatureVersion=1.0&SourceIp=1xxxx6&Timestamp=2019-04-19Txxxxxxx&Ver sion=2019-01-03&Signature=xxxx%xxxx%3D
```

API requests are presented in the following easy-to-read format in this document: covery and Protection

```
https://sddp-api.[ RegionId].example.com/?Action=DescribeDataAssets &CurrentPage=1 &PageSize=10 &Format=JSON &Version=2019-01-03 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2019-04-19T12:00:00Z
```

#### 7.2.2 Request signatures

Apsara Stack Security authenticates each access request. Therefore, each request must contain signature information, regardless of whether it is sent through HTTP or HTTPS. API authorization To ensure the security of your account, we recommend that you use a Resource Access Management (RAM) user to call API operations. Before using a RAM user to call an API operation, you must grant the RAM user the corresponding permission to call the operation by creating an authorization policy and attaching the policy to the RAM user. API signature To ensure security, Apsara Stack authenticates each API request through the signature. When you manually make an API request, you must use the AccessKey secret to calculate the signature, that is, the hash-based message authentication code (HMAC) value, based on the encoded request string. For more information, see the definition in RFC 2104. This topic uses the raw access parameters in the following table to describe how to create an API signature.

| Parameter | Description |
|---|---|
| Endpoint | http://yundunprivate.[ RegionId].example.com/? |
| Operation-specific parameters | Action=DescribeFeatures |
| Common parameters except Signature | &Timestamp=2016-02-23T12:46:24Z &Format=JSON &AccessKeyId=<yourAccessKeyId> &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2018-01-16 &SignatureVersion=1.0 |
| AccessKey secret | <yourAccessKeySecret> |

covery and Protection
1. Create a canonicalized query string by arranging the request parameters.
Not e The request parameters include all common and operation-specific parameters except Signature. i. Arrange the parameters. Arrange the request parameters in alphabetical order. ii. Encode the parameters. Parameter names and values in the request URL must be encoded in UTF-8. The encoding rules are as follows: Uppercase letters, lowercase letters, digits, and some special characters such as ampersands (&), hyphens (-), underscores (_), periods (.), and tildes (~) do not need to be encoded. Other characters must be percent encoded in %XY format. XY represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks (") are encoded as %22. Extended UTF-8 characters are encoded in %XY%ZA... format. Spaces must be encoded as %20. Do not encode spaces as plus signs (+). iii. Connect the encoded parameter names and values with equal signs (=). iv. Arrange the parameter name and value pairs connected by equal signs in alphabetical order, and connect them with ampersands (&) to produce the canonicalized query string.
2. Create a string-to-sign from the encoded canonicalized query string.

```
StringToSign=HTTPMethod + "&" + percentEncode("/") + "&" + percentEncode(CanonicalizedQueryString)
```

3. Calculate the HMAC value of the string-to-sign according to the definition in RFC 2104.
Not e The key used for signature calculation is your AccessKey secret plus the ampersand (&) (ASCII 38). Secure Hash Algorithm 1 (SHA1) is used as the hash algorithm.
4. Encode the HMAC value in Base64 to obtain the signature string.

```
LEW8N4y7Uasop******
```

5. Add the signature string to the request as the Signature parameter.

#### 7.2.3 Common parameters

Common request parameters, such as the API version number and authentication information, must be included in all API requests.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Version | String | Yes | The version number of the API, in the format of YYYY-MM-DD. Set the value to 2019-01-03. |

| psara Stack Security |   |   | Developer Guide·Sensitive Data Di covery and Protectio |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| AccessKeyId | String | Yes | The AccessKey ID provided to you by Apsara Stack. |
| Signature | String | Yes | The signature string of the current request. |
| SignatureMethod | String | Yes | The encryption method of the signature string. Set the value to HMAC-SHA1. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard. The time must be in UTC. Format: YYYY-MM-DDThh:mm:ssZ . For example, 2014-05-26T12:00:00Z indicates 20:00:00 on May 26, 2014 (UTC+8). |
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Set the value to 1.0. |
| SignatureNonce | String | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |
| ResourceOwnerAc count | String | No | The name of the account that owns the resource to be accessed through this API request. |
| Format | String | No | The format of the response. Set the value to JSON or XML. Not e Default value: XML. |

#### 7.2.4 Responses

Apsara Stack Security APIs can return responses in XML or JSON format. The system returns a unique identifier specified by RequestId each time you send a request to call an API operation, no matter whether the call is successful or not. Sample response in XML format covery and Protection

```xml
<? xml version="1.0" encoding="UTF-8"? > <! --Root node of the response --> <Operation name+Response>
    <! --Returned request ID-->
    <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
    <! --Returned results-->
</Operation name+Response>
```

Sample response in JSON format

```json
"RequestId": "4C467B38-3910-447D-87BC-AC049166F216", /* Returned results */
```

### 7.3 APIs

#### 7.3.1 DescribeDataAssets

You can call this operation to query data assets globally based on the specified conditions.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDataAssets. |
| RangeId | Integer | Yes | The type of the assets to query. Valid values: 1: MaxCompute project. 2: MaxCompute table. 3: MaxCompute package. 21: Object Storage Service (OSS) bucket. 22: OSS object. 31: Table Store instance. 32: Table Store table. 51: Relational Database Service (RDS) database. 52: RDS table. |
| CurrentPage | Integer | Yes | The number of the page to return. |

| psara Stack Security |   |   | Developer Guide·Sensitive Data Di |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| PageSize | Integer | Yes | The number of entries to return on each page. |
| Name | String | No | The search keyword. Fuzzy match is supported. |
| RuleId | Long | No | The ID of the rule. |
| RiskLevels | String | No | The ID of the risk level. Separate multiple IDs with commas (,). |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The total number of returned pages. |
| CurrentPage | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| Items | Array | The list of assets. |
| Owner | String | The account of the asset owner. |
| ProductCode | String | The code of the big data service, for example, RDS or OSS. |
| Acl | String | The access control list (ACL) for the OSS bucket. |
| RiskLevelId | Long | The ID of the risk level. |
| RiskLevelName | String | The name of the risk level. |
| DepartName | String | The name of the department. |
| Name | String | The name of the asset. |
| Labelsec | Boolean | The label security flag of the MaxCompute asset. |
| CreationTime | Long | The time when the asset was created. Unit: milliseconds. |
| Id | Long | The ID of the primary key. |
| Protection | Boolean | The protection flag of the MaxCompute asset. |
| RuleName | String | The name of the hit rule. |

| Developer Guide·Sensitive D | ata Dis | Apsara Stack Securit |
|---|---|---|

covery and Protection

| Parameter | Type | Description |
|---|---|---|
| ObjectKey | String | The key of the OSS object. |

For a list of error codes, see Error codes. Sample request

```
https://sddp-api.[ RegionId].example.com/?Action=DescribeDataAssets &RangeId=1 &CurrentPage=1 &PageSize=10
```

Sample success response in JSON format

```json
    "RequestId":"71064826-726F-4ADA-B879-05D8055476FB"
    "TotalCount":4,
    "PageSize":10,
    "CurrentPage":1,
    "Items":[
            "Owner":"dtdep-239-153536994****",
            "ProductCode":"ODPS",
            "ProductId":1,
            "Acl":"",
            "RiskLevelId":2,
            "RiskLevelName":"Internal",
            "DepartName":"DemoCenter",
            "Name":"****data",
            "Labelsec":false,
            "CreationTime":1536751124000,
            "Sensitive":true,
            "Id":268,
            "Protection":false,
            "RuleName":"Hit rule"
            "ObjectKey":"Internal"
```

`]`

#### 7.3.2 DescribeInstances

You can call this operation to query instances, databases, projects, or buckets based on the specified conditions. covery and Protection

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeInstances. |
| ProductCode | String | Yes | The code of the big data service, for example, RDS or OSS. |
| CurrentPage | Integer | Yes | The number of the page to return. |
| PageSize | Integer | Yes | The number of entries to return on each page. |
| Name | String | No | The search keyword. Fuzzy match is supported. |
| RuleId | Long | No | The ID of the rule. |
| RiskLevelId | Long | No | The ID of the risk level. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The total number of returned pages. |
| CurrentPage | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| Items | Array | The list of instances. |
| Owner | String | The account of the instance owner. |
| ProductCode | String | The code of the big data service, for example, RDS or OSS. |
| Acl | String | The access control list (ACL) for the OSS bucket. |
| RiskLevelId | Long | The ID of the risk level. |
| RiskLevelName | String | The name of the risk level. |
| DepartName | String | The name of the department. |
| Name | String | The name of the asset. |
| Labelsec | Boolean | The label security flag of the MaxCompute asset. |

| c | Developer Guide·Sensitive D overy and Protection | ata Dis | Apsara Stack Securit | y |
|---|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| CreationTime | Long | The time when the instance was created. Unit: milliseconds. |
| Id | Long | The ID of the primary key. |
| Protection | Boolean | The protection flag of the MaxCompute asset. |

For a list of error codes, see Error codes. Sample request

```
https://sddp-api.[ RegionId].example.com/?Action=DescribeInstances &CurrentPage=1 &PageSize=10 &ProductCode=ODPS
```

Sample success response in JSON format

```json
    "RequestId":"71064826-726F-4ADA-B879-05D8055476FB"
    "TotalCount":4,
    "PageSize":10,
    "CurrentPage":1,
    "Items":[
            "Owner":"dtdep-239-153536994****",
            "ProductCode":"ODPS",
            "ProductId":1,
            "Acl":"",
            "RiskLevelId":2,
            "RiskLevelName":"Internal",
            "DepartName":"DemoCenter",
            "Name":"****data",
            "Labelsec":false,
            "CreationTime":1536751124000,
            "Sensitive":true,
            "Id":268,
            "Protection":false
```

`]`

#### 7.3.3 DescribeTables

covery and Protection Queries data asset tables of MaxCompute, ApsaraDB for RDS, and Table Store that SDDP is authorized to scan.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeTables. |
| InstanceId | Long | Yes | The ID of the instance. |
| CurrentPage | Integer | Yes | The number of the page to return. |
| PageSize | Integer | Yes | The number of entries to return on each page. |
| Name | String | No | The keyword. Fuzzy match is supported. |
| RuleId | Long | No | The ID of the rule. |
| RiskLevelId | Long | No | The ID of the risk level. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The total number of returned pages. |
| CurrentPage | Integer | The number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| Items | Array | The list of instances. |
| Owner | String | The account that owns the instance. |
| ProductCode | String | The code of the service, for example, RDS or OSS. |
| Acl | String | The access control list (ACL) for the OSS bucket. |
| RiskLevelId | Long | The ID of the risk level. |
| RiskLevelName | String | The name of the risk level. |
| DepartName | String | The name of the department. |
| Name | String | The name of the asset. |
| Labelsec | Boolean | The label security tag of the MaxCompute asset. |

| c | Developer Guide·Sensitive D overy and Protection | ata Dis | Apsara Stack Securit | y |
|---|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| CreationTime | Long | The time when the table was created. Unit: milliseconds. |
| Id | Long | The ID of the primary key. |
| Protection | Boolean | The protection tag of the MaxCompute asset. |

For a list of error codes, see Error codes. Sample requests

```
https://sddp-api.[ RegionId].example.com/?Action=DescribeInstances &CurrentPage=1 &PageSize=10 &ProductCode=ODPS
```

Sample success responses in JSON format

```json
    "RequestId":"71064826-726F-4ADA-B879-05D8055476FB"
    "TotalCount":4,
    "PageSize":10,
    "CurrentPage":1,
    "Items":[
            "Owner":"dtdep-239-153536994****",
            "ProductCode":"ODPS",
            "ProductId":1,
            "Acl":"",
            "RiskLevelId":2,
            "RiskLevelName":"Internal",
            "DepartName":"DemoCenter",
            "Name":"****data",
            "Labelsec":false,
            "CreationTime":1536751124000,
            "Sensitive":true,
            "Id":268,
            "Protection":false
```

`]`

#### 7.3.4 DescribePackages

covery and Protection You can call this operation to query MaxCompute packages based on the specified conditions.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribePackages. |
| InstanceId | Long | Yes | The ID of the instance. |
| CurrentPage | Integer | Yes | The number of the page to return. |
| PageSize | Integer | Yes | The number of entries to return on each page. |
| Name | String | No | The search keyword. Fuzzy match is supported. |
| RuleId | Long | No | The ID of the rule. |
| RiskLevelId | Long | No | The ID of the risk level. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The total number of returned pages. |
| CurrentPage | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| Items | Array | The list of packages. |
| Owner | String | The account of the package owner. |
| RiskLevelId | Long | The ID of the risk level. |
| RiskLevelName | String | The name of the risk level. |
| DepartName | String | The name of the department. |
| Name | String | The name of the asset. |
| CreationTime | Long | The time when the package was created. Unit: milliseconds. |
| Id | Long | The ID of the primary key. |
| InstanceId | Long | The ID of the instance. |

covery and Protection For a list of error codes, see Error codes. Sample request

```
https://sddp-api.[ RegionId].example.com/?Action=DescribePackages &CurrentPage=1 &PageSize=20 &InstanceId=1
```

Sample success response in JSON format

```json
    "RequestId":"769FB3C1-F4C9-42DF-9B72-7077A8989C13",
    "TotalCount":4,
    "PageSize":10,
    "CurrentPage":1,
    "Items":[
            "Owner":"dtdep-239-153536994****",
            "ProductCode":"ODPS",
            "ProductId":1,
            "Acl":"",
            "RiskLevelId":2,
            "RiskLevelName":"Internal",
            "DepartName":"DemoCenter",
            "Name":"****data",
            "CreationTime":1536751124000,
            "Sensitive":true,
            "Id":268,
            "InstanceId":1
```

`]`

#### 7.3.5 DescribeColumns

Queries columns in tables of MaxCompute, ApsaraDB for RDS, and Table Store that SDDP is authorized to scan.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeColumns. |

| A | psara Stack Security |   |   | Developer Guide·Sensitive Data Di covery and Protectio | s n |
|---|---|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| InstanceId | Long | Yes | The ID of the instance. |
| TableId | Long | Yes | The ID of the table. |
| CurrentPage | Integer | Yes | The number of the page to return. |
| PageSize | Integer | Yes | The number of entries to return on each page. |
| Name | String | No | The keyword. Fuzzy match is supported. |
| RuleId | Long | No | The ID of the rule. |
| RiskLevelId | Long | No | The ID of the risk level. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The total number of returned pages. |
| CurrentPage | Integer | The number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| Items | Array | The list of packages. |
| Owner | String | The account that owns the package. |
| RiskLevelId | Long | The ID of the risk level. |
| RiskLevelName | String | The name of the risk level. |
| DepartName | String | The name of the department. |
| Name | String | The name of the asset. |
| CreationTime | Long | The time when the column was created. |
| Id | Long | The ID of the primary key. |
| RuleId | Long | The ID of the matched rule. |
| RuleName | String | The name of the matched rule. |
| TableId | Long | The ID of the table. |
| InstanceId | Long | The ID of the instance. |

covery and Protection For a list of error codes, see Error codes. Sample requests

```
https://sddp-api.[ RegionId].example.com/?Action=DescribeColumns &CurrentPage=1 &PageSize=20 &InstanceId=1 &TableId=1
```

Sample success responses in JSON format

```json
    "RequestId":"769FB3C1-F4C9-42DF-9B72-7077A8989C13",
    "TotalCount":4,
    "PageSize":10,
    "CurrentPage":1,
    "Items":[
            "Owner":"dtdep-239-153536994****",
            "ProductCode":"ODPS",
            "ProductId":1,
            "Acl":"",
            "RiskLevelId":2,
            "RiskLevelName":"Internal",
            "DepartName":"DemoCenter",
            "Name":"****data",
            "CreationTime":1536751124000,
            "Sensitive":true,
            "Id":268,
            "RuleId":1,
            "RuleName":"Hit rule",
            "InstanceId":1,
            "TableId":1
```

`]`

#### 7.3.6 DescribeOssObjects

You can call this operation to query Object Storage Service (OSS) objects based on the specified conditions. covery and Protection

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeOssObjects. |
| InstanceId | Long | Yes | The ID of the instance. |
| CurrentPage | Integer | Yes | The number of the page to return. |
| PageSize | Integer | Yes | The number of entries to return on each page. |
| Name | String | No | The search keyword. Fuzzy match is supported. |
| RuleId | Long | No | The ID of the rule. |
| RiskLevelId | Long | No | The ID of the risk level. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The total number of returned pages. |
| CurrentPage | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| Items | Array | The list of packages. |
| RiskLevelId | Long | The ID of the risk level. |
| RiskLevelName | String | The name of the risk level. |
| DepartName | String | The name of the department. |
| Name | String | The name of the asset. |
| Id | Long | The ID of the primary key. |
| RegionId | String | The ID of the region. |

For a list of error codes, see Error codes. Sample request covery and Protection

```
https://sddp-api.[ RegionId].example.com/?Action=DescribeOssObjects &CurrentPage=1 &PageSize=20 &InstanceId=1
```

Sample success response in JSON format

```json
    "RequestId":"769FB3C1-F4C9-42DF-9B72-7077A8989C13",
    "TotalCount":4,
    "PageSize":10,
    "CurrentPage":1,
    "Items":[
            "RiskLevelName":"Internal",
            "Id":17383,
            "RiskLevelId":2,
            "RegionId":"cn-hangzhou",
            "Name":"obj****"
```

`]`

#### 7.3.7 DescribeOssObjectDetail

You can call this operation to query the details of an Object Storage Service (OSS) object that SDDP is authorized to access.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeOssObjectDetail. |
| Id | Long | Yes | The ID of the OSS object. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| OssObjectDetail | Object | The details of the OSS object. |
| RiskLevelId | Long | The ID of the risk level. |
| RiskLevelName | String | The name of the risk level. |

| psara Stack Security |   | covery and Protectio |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| Name | String | The name of the asset. |
| Id | Long | The ID of the primary key. |
| RegionId | String | The ID of the region. |
| CategoryName | String | The type of the OSS object. |
| RuleList | Array | A list of the matched rules. |
| RuleName | String | The name of the matched rule. |
| Count | Integer | The number of matches. |

For a list of error codes, visit the Error codes. Sample requests

```
https://sddp-api.[ RegionId].example.com/?Action=DescribeOssObjectDetail &Id=12
```

Sample success responses in JSON format

```json
    "RequestId":"769FB3C1-F4C9-42DF-9B72-7077A8989C13",
    "OssObjectDetail":{
        "RegionId":"cn-hangzhou",
        "BucketName":"",
        "RiskLevelName":"Internal",
        "Id":17383,
        "RiskLevelId":2,
        "CategoryName":"MAC address",
        "Name":"obj_id",
        "RuleList":[
                "RuleName":"ID card number",
                "Count":10
```

`]`

#### 7.3.8 DescribeDeparts

You can call this operation to query departments based on the specified conditions. covery and Protection

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDeparts. |
| CurrentPage | Integer | Yes | The number of the page to return. |
| PageSize | Integer | Yes | The number of entries to return on each page. |
| Key | String | No | The search keyword. Fuzzy match is supported. |
| AccountType | Integer | No | The type of the query. Valid values: 1: department query. 2: account query. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| CurrentPage | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| TotalCount | Integer | The total number of returned pages. |
| Items | Array | The list of departments. |
| Id | Long | The ID of the primary key. |
| DepartName | String | The name of the department. |
| DepartId | Long | The ID of the department. |

For a list of error codes, see Error codes. Sample request

```
https://sddp-api.[ RegionId].example.com/?Action=DescribeDeparts &CurrentPage=1 &PageSize=10
```

covery and Protection Sample success response in JSON format

```json
    "RequestId":"769FB3C1-F4C9-42DF-9B72-7077A8989C13",
    "PageSize":10,
    "CurrentPage":1
    "TotalCount":1,
    "Items":[
            "Id":283,
            "DepartId":2,
            "DepartName":"Development"
```

`]`

#### 7.3.9 DescribeAccounts

You can call this operation to query accounts based on the specified conditions.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeAccounts. |
| CurrentPage | Integer | Yes | The number of the page to return. |
| PageSize | Integer | Yes | The number of entries to return on each page. |
| Key | String | No | The search keyword. Fuzzy match is supported. |
| DepartId | Long | No | The ID of the department. |
| QueryType | Integer | No | The type of the resource. Valid values: 1: instance. 2: table. 3: package. 4: column. 5: table in a package. |
| ProductCode | String | No | The code of the service. Valid values: MaxCompute RDS OTS |

| eveloper Guide·Sensi overy and Protection | tive Data Dis |   | Apsara Stack Securit |
|---|---|---|---|
| Parameter | Type | Required | Description |
| OperationId | Integer | No | The type of the operation. For more information, see Operation type definition. |
| InstanceId | Long | No | The ID of the instance. |
| TableId | Long | No | The ID of the table. |
| PackageId | Long | No | The ID of the package. |
| ColumnId | Long | No | The ID of the column. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| CurrentPage | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| TotalCount | Integer | The total number of returned pages. |
| Items | Array | The list of accounts. |
| Id | Long | The ID of the primary key. |
| LongName | String | The name of the account. |
| Email | String | The email address. |
| CreateTime | Long | The time when the account was created. Unit: milliseconds. |
| LoginDataTime | Long | The last logon time of the account. Unit: milliseconds. |
| UserId | Long | The ID of the account. |
| FullName | String | The display name. |
| CellphoneNum | String | The mobile phone number. |
| TelephoneNum | String | The landline phone number. |
| AccountTypeId | Integer | The type of the account. Valid values: 2: Apsara Stack Console account. 3: Resource Access Management (RAM) account. |

covery and Protection For a list of error codes, see Error codes. Sample request

```
https://sddp-api.[ RegionId].example.com/?Action=DescribeAccounts &CurrentPage=1 &PageSize=10
```

Sample success response in JSON format

```json
    "RequestId":"769FB3C1-F4C9-42DF-9B72-7077A8989C13",
    "PageSize":10,
    "CurrentPage":1
    "TotalCount":1,
    "Items":[
            "LoginName":"sddp_****",
            "Email":"test@example.com",
            "CreateTime":1543300900000,
            "LoginDataTime":1544493748000,
            "UserId":10****,
            "FullName":"sddp****",
            "Id":1091,
            "CellphoneNum":"1300000****",
            "TelephoneNum":"0571-6000****",
            "AccountTypeId":1
```

`]`

#### 7.3.10 DescribeAccountDetail

You can call this operation to query the details of an account based on the account ID and account type.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeAccountDetail. |
| UserId | Long | Yes | The ID of the account. |

| eveloper Guide·Sensi | tive Data Dis |   |   |
|---|---|---|---|

covery and Protection

| Parameter | Type | Required | Description |
|---|---|---|---|
| AccountTypeId | Integer | Yes | The type of the account. Valid values: 2: Apsara Stack Console account. 3: Resource Access Management (RAM) account. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Account | Object | The details of the account. |
| Id | Long | The ID of the primary key. |
| LongName | String | The name of the account. |
| Email | String | The email address. |
| CreateTime | Long | The time when the account was created. Unit: milliseconds. |
| LoginDataTime | Long | The last logon time of the account. Unit: milliseconds. |
| UserId | Long | The ID of the account. |
| FullName | String | The display name. |
| CellphoneNum | String | The mobile phone number. |
| TelephoneNum | String | The landline phone number. |
| PrivilegeList | Array | The list of available accounts. |
| ProdcutName | String | The service that the account can operate. Separate multiple services with forward slashes (/). |
| UseAccountName | String | The name of the used account. |
| UseAccountId | Long | The ID of the used account. |
| UseAccountType | Integer | The type of the used account. |
| UseAccountCreateTime | Long | The time when the used account was created. Unit: milliseconds. |

For a list of error codes, see Error codes. covery and Protection Sample request

```
https://sddp-api.[ RegionId].example.com/?Action=DescribeAccountDetail &UserId=1 &AccountTypeId=2
```

Sample success response in JSON format

```json
    "RequestId":"769FB3C1-F4C9-42DF-9B72-7077A8989C13",
    "Account":{
        "LoginName":"yundun****",
        "Email":"kf@example.com",
        "CreateTime":1543384996000,
        "LoginDataTime":1543385065000,
        "UserId":1045,
        "FullName":"yundun****",
        "Id":882,
        "CellphoneNum":"1300000****",
        "TelephoneNum":"0571-6000****",
        "PrivilegeList":[
                "UseAccountType":2,
                "ProductName":"OSS/ODPS",
                "UseAccountCreateTime":1546413235000,
                "UseAccountName":"ram_****",
                "UseAccountId":259
```

`]`

#### 7.3.11 DescribePrivileges

You can call this operation to query permissions of an account based on the account ID and other specified conditions.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribePrivileges. |
| CurrentPage | Integer | Yes | The number of the page to return. |

covery and Protection

| Parameter | Type | Required | Description |
|---|---|---|---|
| PageSize | Integer | Yes | The number of entries to return on each page. |
| AccountId | Long | Yes | The ID of the account. |
| UseAccountId | Long | No | The ID of the used account. |
| Key | String | No | The search keyword. Fuzzy match is supported. |
| DataTypeIds | String | No | The type of the resource. For more information, see Resource type definition. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| CurrentPage | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| TotalCount | Integer | The total number of returned pages. |
| Items | Array | The list of permissions. |
| Id | Long | The ID of the primary key. |
| AccountId | Long | The ID of the account. |
| AccountType | Integer | The type of the account. Valid values: 2: Apsara Stack Console account. 3: Resource Access Management (RAM) account. |
| UseAccountId | Long | The ID of the used account. |
| UseAccountType | Long | The type of the used account. Valid values: 2: Apsara Stack Console account. 3: RAM account. |
| DataType | String | The type of the resource. For more information, see Resource type definition |
| DataTypeId | Integer | The ID of the resource type. For more information, see Resource type definition |
| DataInstance | String | The instance. A value of * indicates all instances. |

| A | psara Stack Security |   | Developer Guide·Sensitive Data Di covery and Protectio | s n |
|---|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| DataTable | String | The table. A value of * indicates all tables. |
| DataColumn | String | The column. A value of * indicates all columns. |
| DataPackage | String | The package. A value of * indicates all packages. |
| ResourceName | String | The name of the resource. |
| ResourcePath | String | The path of the resource. |
| Operation | String | The operation permission. Separate multiple permissions with semicolons (;). |
| PolicyCondition | String | The usage conditions. |
| Sensitive | Boolean | Indicates whether the permission is sensitive. |

For a list of error codes, see Error codes. Sample request

```
https://sddp-api.[RegionId].example.com/?Action=DescribePrivileges &CurrentPage=1 &PageSize=20 &AccountId=1
```

Sample success response in JSON format covery and Protection

```json
    "RequestId":"769FB3C1-F4C9-42DF-9B72-7077A8989C13",
    "PageSize":10,
    "CurrentPage":1
    "TotalCount":1,
    "Items":[
            "UseAccountType":2,
            "DataInstance":"341",
            "AccountId":259,
            "ResourceName":"bucket****",
            "Operation":"GET;OPEARETE",
            "AccountType":2,
            "ResourcePath":"kf",
            "DataTypeId":21,
            "Sensitive":false,
            "DataType":"OSS_BUCKET",
            "Id":1,
            "UseAccountId":259
```

`]`

#### 7.3.12 DescribeEventTypes

You can call this operation to query types of anomalous activities based on the specified conditions.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeEventTypes. |
| ParentTypeId | Long | No | The ID of the type. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |

covery and Protection

| Parameter | Type | Description |
|---|---|---|
| EventTypeList | Array | The list of types. Not e If you do not set the ParentTypeId parameter, the system returns the type list. Otherwise, the system returns the list of subtypes under the specified type. |
| Id | Long | The ID of the type. |
| Code | String | The code of the type. |
| Name | String | The name of the type. |
| SubTypeList | Array | The list of subtypes. |
| Id | Long | The ID of the subtype. |
| Code | String | The code of the subtype. |
| Name | String | The name of the subtype. |
| Status | String | The status of the subtype. Valid values: 1: enabled. 2: disabled. |

For a list of error codes, see Error codes. Sample request

```
https://sddp-api.[RegionId].example.com/?Action=DescribeEventTypes &ParentTypeId=1
```

Sample success response in JSON format covery and Protection

```json
    "RequestId":"769FB3C1-F4C9-42DF-9B72-7077A8989C13",
    "EventTypeList":[
            "SubTypeList":[
                    "Id":1,
                    "Code":"010001",
                    "Name":"Incorrect configuration - Sensitive MaxCompute projects are n
ot protected",
                    "Status":1
```

`],`

```json
            "Id":1,
            "Code":"01",
            "Name":"Anomalous permission access"
```

`]`

#### 7.3.13 DescribeEvents

You can call this operation to query anomalous activities based on the specified conditions.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeEvents. |
| CurrentPage | Integer | Yes | The number of the page to return. |
| PageSize | Integer | Yes | The number of entries to return on each page. |
| TypeCode | String | No | The ID of the type of the anomalous activity. |
| UserId | Long | No | The account ID of the operator of the anomalous activity. |
| DealUserId | Long | No | The account ID of the handler of the anomalous activity. |

covery and Protection

| Parameter | Type | Required | Description |
|---|---|---|---|
| Status | Integer | No | The status of the anomalous activity. Valid values: 0: unprocessed. 1: confirmed as a violation. 2: excluded as a false positive. |
| SubTypeCode | String | No | The ID of the subtype of the anomalous activity. |
| StartTime | Long | No | The beginning of the time range to query. Unit: milliseconds. |
| EndTime | Long | No | The end of the time range to query. Unit: milliseconds. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| CurrentPage | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| TotalCount | Integer | The total number of returned pages. |
| Items | Array | The list of anomalous activities. |
| Id | Long | The ID of the anomalous activity. |
| UserId | Long | The account ID of the operator. |
| LoginName | String | The account name of the operator. |
| DisplayName | String | The account display name of the operator. |
| ProductCode | String | The code of the service where the anomalous activity occurred. |
| TypeCode | String | The ID of the type. |
| TypeName | String | The name of the type. |
| SubTypeCode | String | The ID of the subtype. |
| SubTypeName | String | The name of the subtype. |
| AlertTime | Long | The time when the anomalous activity occurred. |

| eveloper Guide·Sensitive D | ata Dis | Apsara Stack Securit |
|---|---|---|

covery and Protection

| Parameter | Type | Description |
|---|---|---|
| EventTime | Long | The time when the alert was reported. |
| Status | Integer | The status of the anomalous activity. Valid values: 0: unprocessed. 1: confirmed as a violation. 2: excluded as a false positive. |
| DealUserId | Long | The account ID of the handler. |
| DealLoginName | String | The account name of the handler. |
| DealDisplayName | String | The account display name of the handler. |
| DealTime | Long | The time when the anomalous activity was processed. Unit: milliseconds. |
| Backed | Boolean | Indicates whether the processing result of the anomalous activity was returned as a feedback to the detection algorithm. |

For a list of error codes, see Error codes. Sample request

```
https://sddp-api.[RegionId].example.com/?Action=DescribeEvents &CurrentPage=1 &TypeCode=01 &PageSize=10
```

Sample success response in JSON format covery and Protection

```json
    "RequestId":"769FB3C1-F4C9-42DF-9B72-7077A8989C13",
    "PageSize":10,
    "CurrentPage":1
    "TotalCount":1,
    "Items":[
            "Status":0,
            "TypeName":"Anomalous data flow",
            "Backed":false,
            "TypeCode":"02",
            "ProductCode":"ODPS",
            "SubTypeName":"Download sensitive data in an abnormal geographical location",
            "EventTime":1545829129000,
            "UserId":22915744338501****,
            "LoginName":"det****",
            "DisplayName":"yundun****",
            "Id":4,
            "SubTypeCode":"020001",
            "AlertTime":1545829129000,
            "StatusName":"To be processed",
            "DealUserId":229157443385014132,
            "DealLoginName":"det****",
            "DeaulDisplayName":"yundun****",
            "DepartName":"kf"
```

`]`

#### 7.3.14 DescribeEventDetail

You can call this operation to query the details of an anomalous activity based on the specified ID.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeEventDetail. |
| Id | Long | Yes | The ID of the anomalous activity. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Event | Object | The details of the anomalous activity. |

| overy and Protection |   |   |
|---|---|---|
| Parameter | Type | Description |
| Id | Long | The ID of the anomalous activity. |
| UserId | Long | The account ID of the operator. |
| LoginName | String | The account name of the operator. |
| DisplayName | String | The account display name of the operator. |
| ProductCode | String | The code of the service where the anomalous activity occurred. |
| TypeCode | String | The ID of the type. |
| TypeName | String | The name of the type. |
| SubTypeCode | String | The ID of the subtype. |
| SubTypeName | String | The name of the subtype. |
| AlertTime | Long | The time when the anomalous activity occurred. |
| EventTime | Long | The time when the alert was reported. |
| Status | Integer | The status of the anomalous activity. Valid values: 0: unprocessed. 1: confirmed as a violation. 2: excluded as a false positive. |
| DealUserId | Long | The account ID of the handler. |
| DealLoginName | String | The account name of the handler. |
| DealDisplayName | String | The account display name of the handler. |
| DealTime | Long | The time when the anomalous activity was processed. Unit: milliseconds. |
| Backed | Boolean | Indicates whether the processing result of the anomalous activity was returned as a feedback to the detection algorithm. |
| Detail | Object | The detailed content of the anomalous activity. |
| Content | Array | The content. |
| Label | String | The title. |
| Value | String | The description. |
| Chart | Array | The baseline. |

| psara Stack Security |   | Developer Guide·Sensitive Data Di covery and Protectio |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| XLabel | String | The X-axis title. |
| YLabel | String | The Y-axis title. |
| Data | Object | The content of the baseline. |
| X | Array | The array of data along the X-axis. |
| Y | Array | The array of data along the Y-axis. |

For a list of error codes, see Error codes. Sample request

```
https://sddp-api.[RegionId].example.com/?Action=DescribeEventDetail &Id=1
```

Sample success response in JSON format

```json
    "RequestId": "769FB3C1-F4C9-42DF-9B72-7077A8989C13",
    "Event": {
        "Status": 0,
        "TypeName": "Anomalous data flow",
        "Backed": false,
        "TypeCode": "02",
        "ProductCode": "ODPS",
        "SubTypeName": "Download sensitive data in an abnormal geographical location",
        "EventTime": 1545829129000,
        "UserId": 22915744338501****,
        "LoginName": "det****",
        "DisplayName": "yundun****",
        "Id": 4,
        "SubTypeCode": "020001",
        "AlertTime": 1545829129000,
        "StatusName": "To be processed",
        "DealUserId": 22915744338501****,
        "DealLoginName": "det****",
        "DealDisplayName": "yundun****",
        "DepartName": "kf",
        "Detail": {
            "Content": [
                    "Value": "This anomalous activity may cause exposure of sensitive dat
a to risks and damage to the security baseline.",
                    "Label": "Risk exposure"
```

`],` covery and Protection

```json
            "Chart": [
                    "YLabel": "Value",
                    "Label": "Event baseline",
                    "Data": {
                        "X": [
```

`1,` `2,` `3,` `4,` `5,` `],`

```json
                        "Y": [
```

`1,` `2,` `3,` `4,` `5,` `]` `},`

```json
                    "XLabel": "Days"
```

`]` `},`

```json
        "DealReason": "Confirmed violation"
```

#### 7.3.15 ModifyEventStatus

You can call this operation to process an anomalous activity.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyEventStatus. |
| Id | Long | Yes | The ID of the anomalous activity. |
| Status | Integer | Yes | The status of the anomalous activity. Valid values: 1: confirmed as a violation. 2: excluded as a false positive. |
| DealReason | String | Yes | The processing comments. |

| psara Stack Security |   |   | covery and Protectio |
|---|---|---|---|
| Parameter | Type | Required | Description |
| Backed | Boolean | No | Specifies whether to return the processing result of the anomalous activity as a feedback to the detection algorithm. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |

For a list of error codes, see Error codes. Sample request

```
https://sddp-api.[RegionId].example.com/?Action=ModifyEventStatus &Id=1 &Status=1 &DealReason=Confirmed violation
```

Sample success response in JSON format

```json
    "RequestId":"8491DBFD-48C0-4E11-B6FC-6F38921244A9"
```

#### 7.3.16 ModifyEventTypeStatus

Enables detection of exceptions of subtypes.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyEventTypeStatus. |
| SubTypeIds | String | Yes | The subtype IDs of exceptions. Separate multiple IDs with commas (,). |

covery and Protection

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |

For a list of error codes, see Error codes. Sample requests

```
https://sddp-api.[ RegionId].example.com/?Action=ModifyEventTypeStatus &SubTypeIds=1,2,3,4
```

Sample success responses in JSON format

```json
    "RequestId":"208B016D-4CB9-4A85-96A5-0B8ED1EBF271"
```

#### 7.3.17 ModifyDefaultLevel

You can call this operation to set the default risk level or modify the risk levels of sensitive data.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyDefaultLevel. |
| DefaultId | Long | No | The ID of the default risk level. |
| SensitiveIds | String | No | The ID of the risk level of sensitive data. Separate multiple IDs with commas (,). |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |

For a list of error codes, see Error codes. covery and Protection Sample request

```
https://sddp-api.[RegionId].example.com/?Action=ModifyDefaultLevel &Type=15 &DefaultId=2 &SensitiveIds=3,4
```

Sample success response in JSON format

```json
    "RequestId":"208B016D-4CB9-4A85-96A5-0B8ED1EBF271"
```

#### 7.3.18 DescribeRules

You can call this operation to query rules based on the specified conditions.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeRules. |
| Name | String | No | The search keyword. Fuzzy match is supported. |
| RiskLevelId | Long | No | The ID of the risk level. |
| Category | Integer | No | The type of the rule. Valid values: 0: keyword. 2: regular expression. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| CurrentPage | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| TotalCount | Integer | The total number of returned pages. |
| Items | Array | The list of rules. |
| Id | Long | The ID of the rule. |

| D c | eveloper Guide·Sensitive D overy and Protection | ata Dis | Apsara Stack Securit | y |
|---|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| Name | String | The name of the rule. |
| Content | String | The content of the rule. |
| Description | String | The description of the rule. |
| RiskLevelId | Long | The ID of the risk level. |
| Status | Integer | The status of the rule. Valid values: 0: disabled. 1: enabled. |
| Category | Integer | The type of the rule. Valid values: 0: keyword. 2: regular expression. |
| CategoryName | String | The name of the rule type. |
| UserId | Long | The account ID of the rule creator. |
| LoginName | String | The account name of the rule creator. |
| DisplayName | String | The account display name of the rule creator. |

For a list of error codes, see Error codes. Sample request

```
https://sddp-api.[RegionId].example.com/?Action=DescribeRules
```

Sample success response in JSON format covery and Protection

```json
    "RequestId":"769FB3C1-F4C9-42DF-9B72-7077A8989C13",
    "Items":[
            "Description":"IP address",
            "Category":2,
            "GmtModified":1545277010000,
            "RiskLevelId":2,
            "Name":"IP address",
            "GmtCreate":1545277010000,
            "UserId":0,
            "Status":1, //0: disabled. 1: enabled.
            "Content":"(?:\\D|^)((?:(?:25[0-4]|2[0-4]\\d|1\\d{2}|[1-9]\\d{1})\\.)(?:(?:25
[0-5]|2[0-4]\\d|[01]? \\d? \\d)\\.){2} (?:25[0-5]|2[0-4]\\d|1[0-9]\\d|[1-9]\\d|[1-9]))(?: \\D|$)",
            "CategoryName":"Regular expression",
            "RiskLevelName":"Internal",
            "DepartName":"KF",
            "LoginName":"det****",
            "Id":2000
```

`],`

```json
    "TotalCount":18,
    "PageSize":10,
    "CurrentPage":1
```

#### 7.3.19 CreateRule

You can call this operation to create a custom rule.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateRule. |
| Name | String | Yes | The name of the rule. |
| Content | String | Yes | The content of the rule. |
| Category | Integer | Yes | The type of the rule. Valid values: 0: keyword. 2: regular expression. |
| RiskLevelId | Long | Yes | The ID of the risk level. |

covery and Protection

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |

For a list of error codes, see Error codes. Sample request

```
https://sddp-api.[RegionId].aliyuncs.com/?Action=CreateRule &Name=Mobile phone number &Category=0 &Content=1300000**** &RiskLevelId=4
```

Sample success response in JSON format

```json
    "RequestId":"208B016D-4CB9-4A85-96A5-0B8ED1EBF271"
```

#### 7.3.20 ModifyRule

You can call this operation to modify a custom rule.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyRule. |
| Id | Long | Yes | The ID of the rule. |
| Name | String | Yes | The name of the rule. |
| Content | String | Yes | The content of the rule. |
| Category | Integer | Yes | The type of the rule. Valid values: 0: keyword. 2: regular expression. |
| RiskLevelId | Long | Yes | The ID of the risk level. |

covery and Protection

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |

For a list of error codes, see Error codes. Sample request

```
https://sddp-api.[RegionId].example.com/?Action=ModifyRule &Id=1 &Name=Mobile phone number &Category=0 &Content=1300000**** &RiskLevelId=4
```

Sample success response in JSON format

```json
    "RequestId":"208B016D-4CB9-4A85-96A5-0B8ED1EBF271"
```

#### 7.3.21 ModifyRuleStatus

You can call this operation to enable or disable a rule.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyRuleStatus. |
| Id | Long | Yes | The ID of the rule. |
| Status | Integer | Yes | The status of the rule. Valid values: 0: disabled. 1: enabled. |

covery and Protection

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |

For a list of error codes, see Error codes. Sample request

```
https://sddp-api.[RegionId].example.com/?Action=ModifyRuleStatus &Id=1 &Status=1
```

Sample success response in JSON format

```json
    "RequestId":"208B016D-4CB9-4A85-96A5-0B8ED1EBF271"
```

#### 7.3.22 DeleteRule

You can call this operation to delete a custom rule.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteRule. |
| Id | Long | Yes | The ID of the rule. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |

For a list of error codes, see Error codes. Sample request covery and Protection

```
https://sddp-api.[RegionId].example.com/?Action=DeleteRule &Id=1
```

Sample success response in JSON format

```json
    "RequestId":"208B016D-4CB9-4A85-96A5-0B8ED1EBF271"
```

#### 7.3.23 DescribeDataLimitSet

You can call this operation to query the instances, databases, or buckets of a specified service that Sensitive Data Discovery and Protection (SDDP) is authorized to scan.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDataLimitSet. |
| ResourceType | Integer | Yes | The ID of the service. Valid values: 1: MaxCompute. 2: Object Storage Service (OSS). 5: Relational Database Service (RDS). |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| DataLimitList | Array | The list of instances that SDDP is authorized to scan. |
| Id | Long | The ID of the primary key. |
| RegionId | String | The ID of the region. |
| LocalName | String | The name of the region. |
| ParentId | String | The name of the instance. |
| UserName | String | The username. |
| Password | String | The password. |
| Connector | String | The connection string of the database. |

| D c | eveloper Guide·Sensitive D overy and Protection | ata Dis | Apsara Stack Securit | y |
|---|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| OssBucketList | Array | The list of existing OSS buckets. |
| RegionId | String | The ID of the region. |
| BucketName | String | The name of the OSS bucket. |
| RegionList | Array | The list of regions. |
| RegionId | String | The ID of the region. |
| LocalName | String | The name of the region. |

For a list of error codes, see Error codes. Sample request

```
https://sddp-api.[RegionId].example.com/?Action=DescribeDataLimitSet &ResourceType=1
```

Sample success response in JSON format covery and Protection

```json
    "RequestId":"769FB3C1-F4C9-42DF-9B72-7077A8989C13",
    "DataLimitSet":{
        "ResourceType":1,
        "DataLimitList":[
                "Id":1,
                "RegionId":"cn-hangzhou",
                "LocalName":"China (Hangzhou)",
                "ParentId":"oss-bucket",
                "UserName":"Username",
                "Password":"Password",
                "Connector":"Connection string"
```

`],`

```json
        "OssBucketList":[
                "RegionId":"cn-hangzhou",
                "BucketName":"oss-bucket"
```

`],`

```json
        "RegionList":[
                "RegionId":"cn-hangzhou",
                "LocalName":"Hangzhou"
```

`]`

#### 7.3.24 CreateDataLimit

Authorizes SDDP to scan instances, databases, or buckets of a specified service.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateDataLimit. |
| ResourceType | Integer | Yes | The ID of the service. Valid values: 1: MaxCompute 2: OSS 5: RDS |
| ResourceType | String | Yes | The ID of the region. |

| Developer Guide·Sensi | tive Data Dis |   | Apsara Stack Securit |
|---|---|---|---|

covery and Protection

| Parameter | Type | Required | Description |
|---|---|---|---|
| ParentId | String | Yes | The name of the instance. |
| UserName | String | Yes | The username. |
| Password | String | Yes | The password. |
| Connector | String | Yes | The connection string of the database. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |

For a list of error codes, see Error codes. Sample requests

```
https://sddp-api.[ RegionId].example.com/?Action=CreateDataLimit &ResourceType=1 &ServiceRegionId=cn-hangzhou &ParentId=test &UserName=<userName> &Password=<passWord> @Connector=jdbc:mysql://localhost:3306/test
```

Sample success responses in JSON format

```json
    "RequestId":"7C3AC882-E5A8-4855-BE77-B6837B695EF1"
```

#### 7.3.25 DeleteDataLimit

Revokes permissions granted to SDDP for scanning instances, databases, or buckets of a specified service.

| Parameter | Type | Required | Description |
|---|---|---|---|

covery and Protection

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteDataLimit. |
| Id | Long | Yes | The authorization ID. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |

For a list of error codes, see Error codes. Sample requests

```
https://sddp-api.[ RegionId].example.com/?Action=DeleteDataLimit &Id=1
```

Sample success responses in JSON format

```json
    "RequestId":"208B016D-4CB9-4A85-96A5-0B8ED1EBF271"
```

### 7.4 Data dictionaries

#### 7.4.1 Operation type definition

| ID | Description |
|---|---|
| 1 | Get |
| 2 | CreateDelete |
| 3 | Operate |
| 4 | Read |
| 5 | Write |
| 6 | List |
| 7 | CreateTable |

| D c | eveloper Guide·Sensitive Data Dis overy and Protection | Apsara Stack Securit | y |
|---|---|---|---|

| ID | Description |
|---|---|
| 8 | CreateInstance |
| 9 | CreateFunction |
| 10 | CreateResource |
| 11 | CreateJob |
| 12 | CreateVolume |
| 13 | CreateOfflineModel |
| 14 | CreateXflow |
| 15 | All |
| 16 | Describe |
| 17 | Select |
| 18 | Alter |
| 19 | Update |
| 20 | Drop |
| 21 | Create |
| 22 | Delete |
| 23 | Modify |
| 24 | Insert |
| 201 | CreateBucket |
| 202 | ModifyBucket |
| 203 | GetBucket |
| 204 | DeleteBucket |
| 205 | CreateObject |
| 206 | ModifyObject |
| 207 | GetObject |
| 208 | DeleteObject |
| 301 | LoadData |

| psara Stack Security | Developer Guide·Sensitive Data Di covery and Protectio |
|---|---|

| ID | Description |
|---|---|
| 302 | DumpData |
| 303 | Show |

#### 7.4.2 Resource type definition

| ID | Name | Description |
|---|---|---|
| 1 | ODPS PROJECT _ | MaxCompute project |
| 2 | ODPS TABLE _ | MaxCompute table |
| 3 | ODPS PACKAGE _ | MaxCompute package |
| 4 | ODPS PACKAGE TABLE _ _ | Table in a MaxCompute package |
| 5 | ODPS COLUMN _ | MaxCompute column |
| 21 | OSS BUCKET _ | OSS bucket |
| 31 | OTS INSTANCE _ | Table Store instance |
| 32 | OTS TABLE _ | Table Store table |

#### 7.4.3 Risk level definition

| ID | Name | Description |
|---|---|---|
| 1 | S1 | Weak risk level |
| 2 | S2 | Medium risk level |
| 3 | S3 | High risk level |
| 4 | S4 | Highest risk level |

s Center

## 8 Security Operations Center

### 8.1 List of operations by function

The following tables list API operations available for use in Security Operations Center (SOC). For more information, see the corresponding operation description.

| Operation | Description |
|---|---|
| QueryDataCount | You can call this operation to query data on attacks, alerts, security risks, and protected departments. |
| GetAssetCount | You can call this operation to query the information of assets added within a specified time range and the information of all assets. |
| GetEcsProtectCount | You can call this operation to query the number of ECS instances with an online Server Guard agent and the number of ECS instances with an offline agent. |
| DescribeAttacks |   |
| DescribeAlarms |   |
| DescribeVulFrangs |   |
| DescribeHcFrangs |   |
| DescribePBLineFrangs | You can call this operation to query the baseline risks on the platform. |
| QueryDataEnum | You can call this operation to query the types of attacks, alerts, and security risks. |
| QueryDataCodeValue | You can call this operation to query the code of a specified server configuration type. |
| QueryDataDistribution | You can call this operation to query the number of a specified type of security issue. |
| SaveOrUpdateSocReportTask | You can call this operation to create or modify report tasks. |
| QuerySocReportTasks | You can call this operation to query report tasks. |
| DelSocReportTask | You can call this operation to delete a report task. |
| QuerySocReportRecords | You can call this operation to query the report records of a specified report task. |
| GetDeptMap | You can call this operation to obtain a list of departments. |
| GetRegionMap | You can call this operation to obtain a list of regions to which your assets belong. |

| psara Stack Security | Developer Guide·Security Operatio s Cente |
|---|---|
| Operation | Description |
| DownloadFile | You can call this operation to export a report on the assets. |
| GetEcsList | You can call this operation to obtain a list of ECS instances. |
| GetDiskList | You can call this operation to query disk information of ECS instances. |
| GetSecurityGroupList | You can call this operation to obtain a list of security groups. |
| GetEcsInfo | You can call this operation to query the details of a specified ECS instance. |
| GetRdsList | You can call this operation to query ApsaraDB RDS instances. |
| GetRdsInstanceIPArrayList | You can call this operation to query the whitelists configured for an ApsaraDB RDS instance. |
| GetRdsInfo | You can call this operation to obtain a list of OSS buckets. |
| GetOssList | You can call this operation to obtain a list of OSS buckets. |
| GetSlbList | You can call this operation to obtain a list of SLB instances. |
| GetEipList | You can call this operation to obtain a list of Elastic IP addresses. |
| GetAlarmConfig | You can call this operation to query the alert configuration. |
| UpdateAlarmConfig | You can call this operation to update the alert configuration. |
| GetAlarmContacts | You can call this operation to obtain a list of alert recipients. |
| AddAlarmContacts | You can call this operation to add an alert recipient or modify alert recipient information. |
| DeleteAlarmContacts | You can call this operation to delete alert recipients. |
| SendAlarm | You can call this operation to send an alert. |
| QuerySource | You can call this operation to query log sources. |
| QueryType | You can call this operation to query the types of logs from a specified log source. |
| QueryLog | You can call this operation to query log records from a specified log source. |
| GetVpcList | You can call this operation to obtain a list of VPCs. |
| GetMachineList | You can call this operation to obtain a list of assets. |
| GetMachineInfo | You can call this operation to query asset information. |

| s | Developer Guide·Security Operation Center | Apsara Stack Securit | y |
|---|---|---|---|

| Operation | Description |
|---|---|
| DescribeSocUsers | You can call this operation to query users. |
| DeleteSocUser | You can call this operation to delete a user. |
| SaveOrUpdateSocUser | You can call this operation to add a user or modify user information. |

### 8.2 Request method

#### 8.2.1 Request syntax

where:

| endpoint | : the e |
|---|---|

`endpoint` : the endpoint of the Security Operations Center (SOC) API is `yundunnewsoc-pop.[ Regio`

```
nId].example.com .
```

Not e `Action` : the name of the operation being performed. For example, if `Action=GetEcsProtectCount` ,You can call this operation to query the number of ECS instances with an online Server Guard agent and the number of ECS instances with an offline agent.

#### 8.2.2 Sign API requests

Apsara Stack Security authenticates each access request. Therefore, a request must contain signature information regardless of whether it is sent over HTTP or HTTPS. Authorization To ensure the security of your account, we recommend that you use a RAM user to call API operations. Before you use a RAM user to call an API operation, you must grant the RAM user the required permissions by creating an policy and attaching the policy to the RAM user. API signature You must sign all API requests to ensure security. Alibaba Cloud uses the request signature to verify the identity of the API caller. When you manually make an API request, you must use the AccessKey secret to calculate an HMAC value based on the encoded and sorted request string. The HMAC value is the signature. For more information, see the definition in RFC 2104. The following parameters are used in the following procedure to describe how to calculate a signature.

| Parameter | Description |
|---|---|
| Endpoint | http://yundunnewsoc-pop.[ RegionId].example.com/? |

| psara Stack Security | s Cente |
|---|---|

| Parameter | Description |
|---|---|
| Operation-specific parameters | Action=GetEcsProtectCount |
| Common parameters except Signature | &Timestamp=2016-02-23T12:46:24Z &Format=JSON &AccessKeyId=<yourAccessKeyId> &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2019-07-23 &SignatureVersion=1.0 |
| AccessKey secret | <yourAccessKeySecret> |

1. Create a canonicalized query string by arranging the request parameters.
Not e The request parameters include operation-specific parameters and all common request parameters except Signature. i. Sort the request parameters. Sort the request parameters in alphabetical order. ii. Encode the parameters. Encode the canonicalized query string in UTF-8 based on the following rules: Uppercase letters, lowercase letters, digits, and some special characters such as hyphens (-), underscores (_), periods (.), and tildes (~) do not need to be encoded. Other characters must be percent encoded in the %XY format. XY represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks (") are encoded as %22. Extended UTF-8 characters are encoded in the %XY%ZA… format. Spaces must be encoded as %20. Do not encode spaces as plus signs (+). iii. Connect the encoded parameter names and values by using equal signs (=). iv. Sort the pairs of parameter names and values that are connected by using equal signs (=) in alphabetical order. Connect the pairs with ampersands (&) to create a canonicalized query string.
2. Create a string-to-sign from the encoded canonicalized query string based on the following rule:

```
StringToSign=HTTPMethod + "&" + percentEncode("/") + "&" + percentEncode(CanonicalizedQueryString)
```

3. Calculate the HMAC value of the string-to-sign based on the HMAC definition in RFC 2104.
Not e Your AccessKey secret in combination with an ampersand (&) (ASCII:38) is used as the key for the HMAC calculation. The SHA1 algorithm is used to calculate the HMAC value of the string-to-sign. s Center
4. Encode the HMAC value in Base64 to obtain the signature string.

```
LEW8N4y7Uasop******
```

5. Add the signature string to the request as the Signature parameter. The result is the signed API
request.

#### 8.2.3 Common parameters

Common request parameters must be included in all Apsara Stack Security API requests, such as the API version number and authentication information.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Version | String | Yes | The version number of the API. The value is in the format of YYYY-MM-DD. Set the value to 2019-07-23. |
| AccessKeyId | String | Yes | The AccessKey ID provided to you by Alibaba Cloud. |
| Signature | String | Yes | The signature string of the current request. |
| SignatureMethod | String | Yes | The encryption method of the signature string. Set the value to HMAC-SHA1. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC. For example, 2014-05-26T12:00:00Z indicates 20:00:00 on May 26, 2014 (UTC+8). |
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Set the value to 1.0. |
| SignatureNonce | String | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |
| ResourceOwnerAc count | String | No | The owner account (the logon username) of the resource you want to access by using this API request. |
| Format | String | No | The format of the response. Valid values: JSON and XML. Default value: XML. |

s Center

#### 8.2.4 Response structure

Apsara Stack Security API responses can be returned in either the XML or JSON format. Every response returns a unique ID (indicated by RequestId) regardless of whether the call is successful. Sample responses (XML format)

```xml
<? xml version="1.0" encoding="UTF-8"? > <! --The root node of the result--> <Operation name+Response>
    <! --Returned request ID-->
    <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
    <! --Returned data-->
</Operation name+Response>
```

Sample responses (JSON format)

```json
"RequestId": "4C467B38-3910-447D-87BC-AC049166F216", /* Returned data */
```

### 8.3 Operations

#### 8.3.1 QueryDataCount

You can call this operation to query data on attacks, alerts, security risks, and protected departments.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to QueryDataCount. |

s Center

| Parameter | Type | Required | Description |
|---|---|---|---|
| ApiName | String | Yes | The object to query. Valid values: describeNewAttackCount: the number of new attacks describeAttackCount: the total number of attacks describeNewAlarmCount: the number of new alerts describeAlarmCount: the total number of alerts describeUnProcessedAlarmCount: the number of unhandled alerts describeNewFrangCount: the number of new security risks describeFrangCount: the total number of security risks describeUnprocessedFrangCount: the number of unhandled security risks describeUserCount: the number of protected departments |
| TimeSpan | String | No | The time range to query. 0: past 24 hours 1: last seven days 2: last 30 days |

| Parameter | Type | Description |
|---|---|---|
| Count | Long | The result of the query. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=QueryDataCount &TimeSpan=0 &ApiName=describeAttackCount
```

Sample success responses in JSON format s Center

```json
    "code":200,
    "data":{
        "Data":{"Count":5011}
```

`},`

```json
    "requestId":"E404ADE2-D7FB-43B5-BDC9-31CBEF3EEDAC",
    "success":true
```

For a list of error codes, visit the Error codes.

#### 8.3.2 GetAssetCount

You can call this operation to query the information of assets added within a specified time range and the information of all assets.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GetAssetCount. |
| Aliuid | Long | Yes | The ID of the user. |
| StartDate | Long | No | The beginning of the time range where the assets to query were created. |
| EndDate | Long | No | The end of the time range where the assets to query were added. |
| TimeSpan | Integer | No | The unit of the time range. Valid values: 0: day 1: week 2: month |

| Parameter | Type | Description |
|---|---|---|
| AllAsset | Array | A list of all assets. |
| └Value | String | The number of assets. |
| └Key | String | The type of the asset. |
| NewAsset | Array | A list of new assets. |
| └Value | String | The number of new assets. |

| Center |   | Apsara Stack Securit |
|---|---|---|
| Parameter | Type | Description |
| └Key | String | The type of the new asset. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetAssetCount &TimeSpan=0
```

Sample success responses in JSON format s Center

```json
   "RequestId":"DBA8A3BC-5C61-494D-9B11-6DDC6E14D92C",
  "Data":{
    "NewAsset":[//A list of assets added within the period from StartDate to EndDate
        "Value":"49",
        "Key":"ecsCount"
```

`},`

```json
        "Value":"54",
        "Key":"rdsCount"
```

`},`

```json
        "Value":"68",
        "Key":"ossCount"
```

`},`

```json
        "Value":"20",
        "Key":"eipCount"
```

`},`

```json
        "Value":"20",
        "Key":"slbCount"
```

`],`

```json
    "AllAsset":[//A list of all assets
        "Value":"49",
        "Key":"ecsCount"
```

`},`

```json
        "Value":"54",
        "Key":"rdsCount"
```

`},`

```json
        "Value":"68",
        "Key":"ossCount"
```

`},`

```json
        "Value":"20",
        "Key":"eipCount"
```

`},`

```json
        "Value":"20",
        "Key":"slbCount"
```

`]` For a list of error codes, visit the Error codes. s Center

#### 8.3.3 GetEcsProtectCount

You can call this operation to query the number of ECS instances with an online Server Guard agent and the number of ECS instances with an offline agent.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GetEcsProtectCount. |

| Parameter | Type | Description |
|---|---|---|
| Total | Integer | The total number of entries. |
| Items | Array | The ECS protection data. |
| └Key | String | The protection status of the ECS instance. Valid values: ecsCount: The ECS instance is protected. offlineCount: The ECS instance is not protected. Not e If the value is offlineCount, the ECS instance is online, but the Server Guard agent is offline. |
| └Value | Integer | The number of ECS instances. If Key is ecsCount, this parameter indicates the number of protected ECS instances. If Key is offlineCount, this parameter indicates the number of unprotected ECS instances. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetEcsProtectCount
```

Sample success responses in JSON format s Center

```json
    "RequestId":"4D1E89E0-3140-46F2-808D-7D7940F65087",
    "Data":{
        "Total":1,
        "Items":[
                "Value":"0",//The number of ECS instances on which the Server Guard agent i
s offline.
                "Key":"offlineCount"//The number of ECS instances on which the Server Guard
agent is offline.
```

`},`

```json
                "Value":"0",//The number of ECS instances.
                "Key":"ecsCount"//The number of ECS instances.
```

`]` For a list of error codes, visit the Error codes.

#### 8.3.4 DescribeAttacks

You can call this operation to query attacks on users or on the platform based on specified conditions.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeAttacks. |
| DataScope | Integer | Yes | Specifies whether the attacks on users or on the platform are queried. Valid values: 0: platform 1: users |
| SourceFrom | Integer | No | The source of attack data. |
| UserId | Long | No | The ID of the department to query. |
| PageSize | Integer | Yes | The number of attacks to return on each page. |
| PageNo | Integer | Yes | The number of the page to return. |
| AttackType | String | No | The type of the attacks to query. |

| eveloper Guide·Secur | ity Operation |   |   |
|---|---|---|---|

s Center

| Parameter | Type | Required | Description |
|---|---|---|---|
| ProcessState | Integer | No | The processing status of the attacks to query. 0: An alert has been generated on the attack. 1: The attack has been blocked. 3: The attack traffic is being scrubbed. 4: The attack traffic has been scrubbed. |
| StartTime | Long | No | The beginning of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| EndTime | Long | No | The end of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| KeyWord | String | No | The keyword of the attack name or asset name. |

| Parameter | Type | Description |
|---|---|---|
| PageNo | Integer | The page number of the returned page. |
| PageSize | Integer | The number of attacks returned per page. |
| Total | Integer | The total number of records. |
| RequestId | String | The ID of the request. |
| AttackName | String | The name of the attack. |
| AttackId | Long | The ID of the attack. |
| AssetType | Integer | The type of the asset. |
| Asset | String | The ID of the asset. |
| UserName | String | The name of the department. |
| RaisedTime | Long | The time of the attack. |
| ProcessState | Integer | The processing status of the attack. |

| A | psara Stack Security |   | Developer Guide·Security Operatio s Cente | n r |
|---|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| UserId | Long | The ID of the user or department. |
| AttackType | String | The type of the attack. |
| SourceFrom | Integer | The data source of the attack. |
| AttackerIp | String | The IP address of the attacker. |
| AssetName | String | The name of the asset. |
| AssetPublicIps | String | The public IP address of the affected asset. |
| AssetPrivateIps | String | The internal IP address of the affected asset. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=DescribeAttacks &DataScope=1 &PageSize=20 &PageNo=1
```

Sample success responses in JSON format s Center

```json
    "code":200,
    "data":{
        "Data":{
            "PageSize":20,
            "Total":222,
            "Items":[
                    "UserName":"yundun****",
                    "SourceFrom":46,
                    "AttackType":"Brute-force",
                    "AttackerIp":"172. *. *.105",
                    "AssetName":"monodb****",
                    "SourceFromIp":"172. *. *.105",
                    "AssetPrivateIps":"172. *. *.92",
                    "AssetType":"ECS",
                    "UserId":163957166417****,
                    "AssetPublicIps":"",
                    "Asset":"0fbc7e34-b1f6-4eeb-b100-130c15eb1c3b",
            "RaisedTime":1572921381000
```

`],`

```json
            "PageNo":1
```

`},`

```json
    "requestId":"69C66589-F448-4A47-BFEA-EC12F55DCB53",
    "success":true
```

For a list of error codes, visit the Error codes.

#### 8.3.5 DescribeAlarms

You can call this operation to query security alerts on users or on the platform based on specified conditions.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeAlarms. |
| DataScope | Integer | Yes | Specifies whether the alerts on users or the platform are queried. Valid values: 0: platform 1: users |
| SourceFrom | Integer | No | The data source of security alerts. |

| A | psara Stack Security |   |   | Developer Guide·Security Operatio s Cente | n r |
|---|---|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| UserId | Long | No | The ID of the department to query. |
| PageSize | Integer | Yes | The number of alerts to return on each page. |
| PageNo | Integer | Yes | The number of the page to return. |
| AlarmType | String | No | The type of the alerts to query. |
| ProcessState | Integer | No | The processing status of the alerts to query. |
| KeyWord | String | No | The keywords of the alerts or keywords in the ID or names of assets related to the alerts. |
| RiskLevels | List<Integer> | No | The risk levels of the alerts to query. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| AlarmId | Long | The ID of the alert. |
| RiskLevel | Integer | The risk level of the alert. |
| AlarmName | String | The name of the alert. |
| AssetType | String | The type of the asset. |
| Asset | String | The ID of the asset. |
| UserName | String | The user name. |
| UserId | Long | The ID of the user or platform. |
| RaisedTime | Long | The time when the alert was generated. |
| ProcessState | Integer | The processing status of the alert. |
| AlarmType | String | The type of the alert. |
| SourceFrom | Integer | The data source of the alert. |
| AttackerIp | String | The IP address of the attacker. |
| AssetName | String | The name of the asset. |
| AssetPublicIps | String | The public IP address of the affected asset. |

| D s | eveloper Guide·Security O Center | peration | Apsara Stack Securit | y |
|---|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| AssetPrivateIps | String | The internal IP address of the affected asset. |
| AlarmUniqueInfo | String | The unique key of the alert. |
| LastTime | String | The last time when the alert was generated. |
| Total | Integer | The total number of entries returned. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=DescribeAlarms &RiskLevels=[0,1,2] &DataScope=1 &PageSize=20 &PageNo=1
```

Sample success responses in JSON format s Center

```json
    "code":200,
    "data":{
        "Data":{
            "PageSize":20,
            "Total":177,
            "Items":[
                    "AlarmId":30307,
                    "UserName":"yundun****",
                    "AlarmType":"Malicious Process",
                    "SourceFrom":20,
                    "AssetName":"yun****",
                    "AssetPrivateIps":"192. *. *.1",
                    "ProcessState":1,
                    "AssetType":"ECS",
                    "AlarmName":"Mining process",
                    "UserId":1****,
                    "AlarmUniqueInfo":"34dsa1",
                    "AssetPublicIps":"10. *. *.1",
                    "Asset":"2f43eb69-****",
                    "RaisedTime":1571826361000,
                    "RiskLevel":2,
                    "LastTime":1573021501000
```

`],`

```json
            "PageNo":1
```

`},`

```json
    "requestId":"B2C5D1EB-202F-4132-A763-2D16538B****",
    "success":true
```

For a list of error codes, visit the Error codes.

#### 8.3.6 DescribeVulFrangs

You can call this operation to query vulnerabilities.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVulFrangs. |
| UserId | Long | No | The ID of the department to query. |
| RiskLevels | Integer | No | The severity of the vulnerabilities to query. |

| D s | eveloper Guide·Secur Center | ity Operation |   | Apsara Stack Securit | y |
|---|---|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| ProcessState | Integer | No | The processing status of the vulnerabilities to query. |
| Page | Integer | Yes | The number of the page to return. |
| PageSize | Integer | Yes | The number of entries to return on each page. |
| VulType | String | No | The type of the vulnerabilities to query. |
| KeyWord | String | No | The name of the vulnerability or asset to query. |
| DataScope | Integer | Yes | Specifies whether the data of users or the platform is queried. Valid values: 0: platform 1: users |
| NeedFix | String | No | Specifies whether the vulnerabilities to query require fixes. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| PageSize | Integer | The number of entries returned per page. |
| PageNo | Integer | The page number of the returned page. |
| Total | Integer | The number of entries returned. |
| Items | Array | The list of vulnerabilities. |
| └LastTime | Long | The last time when the vulnerability was detected. |
| └RiskLevel | Integer | The severity of the vulnerability. |
| └ProcessState | Integer | The processing status of the vulnerability. |
| └AssetType | String | The type of the affected asset. |
| └NeedFix | String | Indicates whether the vulnerability requires a fix. |
| └VulRelated | String | The ID of the vulnerability details. |
| └Asset | String | The ID of the asset affected by the vulnerability. |
| └SourceFrom | Integer | The data source. |

| A | psara Stack Security |   | Developer Guide·Security Operatio s Cente | n r |
|---|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| └Id | Long | The ID of the vulnerability. |
| └RaisedTime | Long | The first time when the vulnerability was detected. |
| └VulName | String | The name of the vulnerability. |
| └VulType | String | The type of the vulnerability. |
| └AssetPublicIps | String | The public IP address of the affected asset. |
| └AssetPrivateIps | String | The internal IP address of the affected asset. |
| └AssetName | String | The name of the affected asset. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=DescribeVulFrangs &DataScope=1 &PageSize=20 &Page=1
```

Sample success responses in JSON format s Center

```json
    "code":200,
    "data":{
        "Data":{
            "PageSize":20,
            "Total":445,
            "Items":[
                    "ProcessState":1,
                    "AssetType":"ECS",
                    "NeedFix":"later",
                    "VulRelated":"CVE-2016-5195",
                    "Asset":"eb9ea4b0-****",
                    "SourceFrom":1,
                    "Id":6370,
                    "RaisedTime":2019,
                    "RiskLevel":1,
                    "VulName":"RHSA-2017:0372: kernel-aarch64 security and bug fix update",
                    "LastTime":"2019-11-05 17:12:12",
                    "VulType":"cve"
```

`],`

```json
            "PageNo":1
```

`},`

```json
    "requestId":"32B57B56-958C-49C5-BB49-0BABE2060305",
    "success":true
```

For a list of error codes, visit the Error codes.

#### 8.3.7 DescribeHcFrangs

You can call this operation to query the risks in the server configurations set by the user.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeHcFrangs. |
| ProcessState | Integer | No | The processing status of the risks to query. |
| HcType | String | No | The type of server configuration risks to query. |
| Page | Integer | Yes | The number of the page to return. |

| psara Stack Security |   |   | Developer Guide·Security Operatio |
|---|---|---|---|

s Center

| Parameter | Type | Required | Description |
|---|---|---|---|
| PageSize | Integer | Yes | The number of entries to return on each page. |
| KeyWord | String | No | The server baseline name or asset name. |
| DataScope | Integer | Yes | Specifies whether the data of users or the platform is queried. Valid values: 0: platform 1: users |
| UserId | Long | No | The ID of the department to query. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| PageSize | Integer | The number of entries returned per page. |
| PageNo | Integer | The page number of the returned page. |
| Total | Integer | The total number of the returned entries. |
| Items | Array | The list of servers that SOC is authorized to scan. |
| └lastFoundTime | Long | The last time when risks were detected. |
| └RiskLevel | Integer | The level of the risk. Valid values: 0: low 1: medium 3: high |
| └ProcessState | Integer | The processing status of the risk. 1: handled 2: unhandled |
| └HcName | String | The name of the server configuration risk. |
| └HcType | String | The type of the server configuration risk. |
| └UserName | String | The name of the department to which the affected asset belongs. |
| └UserId | Long | The ID of the department to which the affected asset belongs. |
| └SourceFrom | Integer | The data source. |

| D s | eveloper Guide·Security O Center | peration | Apsara Stack Securit | y |
|---|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| └Id | Long | The ID of the entry. |
| └Asset | String | The ID of the affected asset. |
| └AssetType | String | The type of the affected asset. |
| └AssetName | String | The name of the affected asset. |
| └AssetPublicIps | String | The public IP address of the affected asset. |
| └AssetPrivateIps | String | The internal IP address of the affected asset. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=DescribeHcFrangs &DataScope=1 &PageSize=20 &Page=1
```

Sample success responses in JSON format s Center

```json
    "code":200,
    "data":{
        "Data":{
            "PageSize":20,
            "Total":47,
            "Items":[
                    "UserName":"yun****",
                    "SourceFrom":2,
                    "HcType":"Alibaba Cloud",
                    "AssetName":"yun3 ",
                    "LastFoundTime":"2019-11-06 01:03:55",
                    "AssetPrivateIps":"192. *. *.1",
                    "ProcessState":1,
                    "HcName":"Alibaba Cloud Standard",
                    "AssetType":"ECS",
                    "UserId":11424,
                    "AssetPublicIps":"10. *. *.1",
                    "Asset":"71513dfc ",
                    "Id":111,
                    "RiskLevel":2
```

`],`

```json
            "PageNo":1
```

`},`

```json
    "requestId":"FE7137B7-84D8-4AF7-969B-C0DF5118****",
    "success":true
```

For a list of error codes, visit the Error codes.

#### 8.3.8 DescribePBLineFrangs

You can call this operation to query the baseline risks on the platform.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribePBLineFrangs. |
| BLType | String | No | The risk type to query. |
| Keyword | String | No | The name of the platform baseline to query. |
| BLLevel | Integer | No | The risk level to query. |

| D s | eveloper Guide·Secur Center | ity Operation |   | Apsara Stack Securit | y |
|---|---|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| ProcessState | Integer | No | The processing status of the baseline risks to query. |
| Page | Integer | Yes | The number of the page to return. |
| PageSize | Integer | Yes | The number of entries to return on each page. |
| DataScope | Integer | Yes | Specifies whether the data of users or the platform is queried. Valid values: 0: platform 1: users |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| BLLevel | Integer | The level of the risk. |
| ProcessState | Integer | The processing status of the risk. |
| UserName | String | The name of the department affected by the risk. |
| UserId | Long | The ID of the department affected by the risk. |
| BLName | String | The name of the baseline. |
| SourceFrom | Integer | The data source. |
| Id | Long | The ID of the entry. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=DescribePBLineFrangs &BLType=Network Security &DataScope=0 &PageSize=20 &Page=1
```

Sample success responses in JSON format s Center

```json
    "code":200,
    "data":{
        "Data":{
            "PageSize":20,
            "Total":1,
            "Items":[
                    "BLLevel":1,
                    "ProcessState":1,
                    "BLType":"Network Security",
                    "UserName":"Platform",
                    "UserId":-1,
                    "BLName":"VPC Isolation Audit",
                    "SourceFrom":5,
                    "Id":6572
```

`],`

```json
            "PageNo":1
```

`},`

```json
    "requestId":"FDAB3658-E2CD-4C95-BFF5-D0CF204C57D8",
    "success":true
```

For a list of error codes, visit the Error codes.

#### 8.3.9 QueryDataEnum

You can call this operation to query the types of attacks, alerts, and security risks.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to QueryDataEnum. |
| ApiName | String | Yes | The object to query. Valid values: alarmType: types of alerts attackType: types of attacks frangVulInnerType: types of vulnerabilities frangPBlineInnerType: types of baseline risks on the cloud platform |

s Center

| Parameter | Type | Required | Description |
|---|---|---|---|
| DataScope | Integer | Yes | Specifies whether the data of users or the platform is queried. Valid values: 0: platform 1: users |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Value | String | The query result. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=QueryDataEnum &ApiName=frangPBlineRisk &DataScope=0
```

Sample success responses in JSON format s Center

```json
    "code":200,
    "data":{
        "Data":[
                "Value":"Suspicious Process"
```

`},`

```json
                "Value":"System Backdoor"
```

`},`

```json
                "Value":"Suspicious User Operation"
```

`},`

```json
                "Value":"Suspicious Process"
```

`},`

```json
                "Value":"Malicious Process"
```

`},`

```json
                "Value":"Webshell"
```

`},`

```json
                "Value":"Unusual Network Connection"
```

`]` `},`

```json
    "requestId":"47738BF3-5F11-437C-88EC-27E91D0E3158",
    "success":true
```

For a list of error codes, visit the Error codes.

#### 8.3.10 QueryDataCodeValue

You can call this operation to query the code of a specified server configuration type.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to QueryDataCodeValue. |
| ApiName | String | Yes | The object to query. Valid values: The object to query. Set the value to frangHcInnerType. |

s Center

| Parameter | Type | Required | Description |
|---|---|---|---|
| DataScope | Integer | Yes | Specifies whether the data of users or the platform is queried. Valid values: 0: platform 1: users |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Value | String | The type of server configuration. |
| Code | String | The code of the server configuration type. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=QueryDataCodeValue &ApiName=frangHcInnerType &DataScope=0
```

Sample success responses in JSON format

```json
    "code": 200,
    "data": {
        "Data": [{
            "Value": "Ubuntu security baseline check based on Alibaba Cloud standard",
            "Code": "xxx"
        }, {
            "Value": "Ubuntu 14 Security Baseline Check based on CIS Standard",
            "Code": "yyy"
```

`}]` `},`

```json
    "requestId": "7B773594-74A7-4920-9D3D-4EAFA45BC248",
    "success": true
```

For a list of error codes, visit the Error codes.

#### 8.3.11 QueryDataDistribution

You can call this operation to query the number of a specified type of security issue. s Center

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to QueryDataDistribution. |
| ApiName | String | Yes | The type of the security issue to query. Valid values: frangVulRisk: vulnerabilities frangHcRisk: server configuration risks alarmRisk: alerts frangPBlineRisk: platform baseline risks |
| DataScope | Integer | Yes | Specifies whether the issues on users or on the platform are queried. Valid values: 0: platform 1: users |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Type | Integer | The risk level of the issue. |
| Count | Integer | The number of the queried issue. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=QueryDataDistribution &ApiName=frangPBlineRisk &DataScope=0
```

Sample success responses in JSON format s Center

```json
    "code":200,
    "data":{
        "Data":[
                "Type":1,
                "Count":1
```

`]` `},`

```json
    "requestId":"6A50A942-15FC-45ED-8242-E88710749B2F",
    "success":true
```

For a list of error codes, visit the Error codes.

#### 8.3.12 SaveOrUpdateSocReportTask

You can call this operation to create or modify report tasks.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to SaveOrUpdateSocReportTask. |
| Id | Long | No. If you want to modify a report task, this parameter is required. | The ID of the report task. Not e This parameter is optional when you create a report task. This parameter is required when you modify a report task. |

s Center

| Parameter | Type | Required | Description |
|---|---|---|---|
| Name | String | No. If you want to create a report task, this parameter is required. | The name of the report task. Not e This parameter is required when you create a report task. This parameter is optional when you modify a report task. |
| Type | String | No. If you want to create a report task, this parameter is required. | The type of the report. Valid values: day: daily report week: weekly report month: monthly report Not e This parameter is required when you create a report task. This parameter is optional when you modify a report task. |
| DeptIds | String | No | The ID of the department related to the report. Separate multiple department IDs with commas (,). |
| Emails | String | No. If you want to create a report task, this parameter is required. | The email address that is used to receive reports. Separate multiple email addresses with commas (,). Not e This parameter is required when you create a report task. This parameter is optional when you modify a report task. |
| Aliuid | Long | Yes | The ID of the department to which the report creator belongs. |

s Center

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Code | Integer | The HTTP status code. |
| Message | String | Indicates whether the operation is successful. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=SaveOrUpdateSocReportTask &Name=AAA**** &Type=day &Emails=1999****@qq.com,1888****@163.com &DeptIds=1231231,123123,1231231 &Aliuid=12312****
```

Sample success responses in JSON format

```json
    "code":200,
    "data":{},
    "requestId":"FDAB3658-E2CD-4C95-BFF5-D0CF204C57D8",
    "success":true
```

For a list of error codes, visit the Error codes.

#### 8.3.13 QuerySocReportTasks

You can call this operation to query report tasks.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to QuerySocReportTasks. |
| PageNo | Integer | Yes | The number of the page to return. |
| PageSize | Integer | Yes | The number of entries to return on each page. |

s Center

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| PageNo | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| Total | Integer | The total number of entries. |
| GmtModified | Long | The time when the report was modified. |
| CreatorName | String | The user name of the report creator. |
| CreatorId | Long | The user ID of the report creator. |
| Type | String | The type of the report task. |
| GmtCreate | Long | The time when the report was created. |
| RecordNum | Integer | The number of reports generated by the report task. |
| Emails | String | The email address that receives reports. |
| Name | String | The name of the report task. |
| Id | Long | The ID of the report task. |
| LastFinishExcuteTime | String | The last time when the report task finished generating a report. |
| NextBeginExcuteTime | String | The next time when the report task begins to generate a report. |
| LastFinishExcuteTimeSta mp | Long | The last timestamp when the report task finished generating a report. |
| NextBeginExcuteTimeSt amp | Long | The next timestamp when the report task begins to generate a report. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=QuerySocReportTasks &PageNo=1 &PageSize=10
```

Sample success responses in JSON format s Center

```json
    "code":200,
    "data":{
        "Data":{
            "PageSize":10,
            "Total":8,
            "Items":[
                    "PageSize":10,
                    "CreatorId":114247173828****,
                    "GmtModified":"2019-11-06T10:04Z",
                    "NextBeginExcuteTime":"2019-11-07T00:00Z",
                    "Lang":"zh",
                    "Name":"New report asdasd",
                    "DeptIds":"176597162720****,163957166417****",
                    "Type":"day",
                    "GmtCreate":"2019-11-06T10:04Z",
                    "NextBeginExcuteTimeStamp":1573084800000,
                    "PageNo":1,
                    "Emails":"as****@qq.com",
                    "Id":11,
                    "CreatorName":"dtdep-5-157173828****"
```

`],`

```json
            "PageNo":1
```

`},`

```json
    "requestId":"3051F0D5-4F6D-4239-BE25-8150784BECCB",
    "success":true
```

For a list of error codes, visit the Error codes.

#### 8.3.14 DelSocReportTask

You can call this operation to delete a report task.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DelSocReportTask. |
| Id | Integer | Yes | The ID of the report task. You can call the QuerySocReportTasks operation to query the ID of a report task. |

s Center

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=DelSocReportTask &Id=12
```

Sample success responses in JSON format

```json
    "code":200,
    "data":{},
    "requestId":"0AE9A558-A193-4E72-B2CE-6A351BFABDEF",
    "success":true
```

For a list of error codes, visit the Error codes.

#### 8.3.15 QuerySocReportRecords

You can call this operation to query the report records of a specified report task.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to QuerySocReportRecords. |
| PageNo | Integer | Yes | The number of the page to return. |
| PageSize | Integer | Yes | The number of entries to return on each page. |
| Id | Integer | Yes | The ID of the report task. You can call the QuerySocReportTasks operation to query the ID of a report task. |

s Center

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| BeginTimeStamp | Long | The start timestamp of the record. |
| ReportLink | String | The unique key of the report. |
| TaskId | Integer | The ID of the report task. |
| FinishTime | String | The end time of the record. |
| TaskName | String | The name of the report task. |
| BeginTime | String | The start time of the record. |
| FinishTimeStamp | Long | The end timestamp of the record. |
| Id | Integer | The ID of the record. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=QuerySocReportRecords &PageNo=1 &PageSize=10 &Id=5
```

Sample success responses in JSON format s Center

```json
    "code":200,
    "data":{
        "Data":{
            "PageSize":10,
            "Total":1
            "Items":[
                    "BeginTimeStamp":1572833105000,
                    "ReportLink":"5_week_2019-11-04",
                    "TaskId":5,
                    "FinishTime":"2019-11-04T02:05Z",
                    "PageSize":10,
                    "TaskName":"Weekly report 1024",
                    "BeginTime":"2019-11-04T02:05Z",
                    "FinishTimeStamp":1572833108000,
                    "PageNo":1,
                    "Id":131
```

`],`

```json
            "PageNo":1
```

`},`

```json
    "requestId":"58294830-FD53-415B-AADE-F189CA9B2E72",
    "success":true
```

For a list of error codes, visit the Error codes.

#### 8.3.16 GetDeptMap

You can call this operation to obtain a list of departments.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GetDeptMap. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Items | Array | The list of departments. |
| └Key | Long | The ID of the department. |

| s | Developer Guide·Security O Center | peration | Apsara Stack Securit | y |
|---|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| └Value | String | The name of the department. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetDeptMap
```

Sample success responses in JSON format

```json
    "code":200,
    "data":{
        "Data":{
            "PageSize":0,
            "Total":8,
            "Items":[
                    "Value":"admin",
                    "Key":"176597162720****"
```

`},`

```json
                    "Value":"yundun",
                    "Key":"163957166417****"
```

`],`

```json
            "PageNo":0
```

`},`

```json
    "requestId":"CA964E09-D0B5-4B34-93C8-35E882E8DD04",
    "success":true
```

For a list of error codes, visit the Error codes.

#### 8.3.17 GetRegionMap

You can call this operation to obtain a list of regions to which your assets belong.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GetRegionMap. |
| UserId | Long | No | The ID of the department. |

|   |   |   | s Cente |
|---|---|---|---|
| Parameter | Type | Required | Description |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Items | Array | The list of regions. |
| └Key | String | The ID of the region. |
| └Value | String | The name of the region. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetRegionMap
```

Sample success responses in JSON format

```json
    "RequestId":"DF618C9E-6B58-43A0-8E8A-B91162F198F4",
    "data":{
        "items":[
                "key":"cn-qingdao",
                "value":"China (Qingdao)"
```

`},`

```json
                "key":"cn-beijing",
                "value":"China (Beijing)"
```

`],`

```json
        "total":2
```

For a list of error codes, visit the Error codes.

#### 8.3.18 DownloadFile

You can call this operation to export a report on the assets. s Center

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DownloadFile. |
| Aliuid | Long | No | The ID of the department. |
| Region | String | No | The region to query. |
| PageNo | Integer | No | The number of the page to return. Default value: 1 |
| PageSize | Integer | No | The number of entries to return on each page. Default value: 10 |
| ProcessState | Integer | No | The processing state of the assets to query. |
| SartDate | String | No | The beginning of the time range during which the instances to query were created. |
| EendDate | String | No | The end of the time range during which the instances to query were created. |
| Kyword | Integer | No | The keywords for query. |
| AsetType | String | Yes | The type of the assets to query. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Key | String | The identifier of the link from which you can download the report. |
| Value | String | The link from which you can download the report. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=DownloadFile &Asettype=ecs
```

Sample success responses in JSON format s Center

```json
   "RequestId":"A4823F6E-5A22-4603-BC68-AF60CE038149",
    "Data":{
        "Value":"http://11. *. *.6:18080/download_file.do?assetType=ecs&pageNo=1&pageSize=1
0&lang=zh&sortWord=instance_create_time&sortType=desc",
        "Key":"downloadUrl"
```

For a list of error codes, visit the Error codes.

#### 8.3.19 GetEcsList

You can call this operation to obtain a list of ECS instances.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GetEcsList. |
| Aliuid | Long | No | The ID of the department. |
| Region | String | No | The region to query. |
| StartDate | String | No | The beginning of the time range during which the instances to query were created. |
| EndDate | String | No | The end of the time range during which the instances to query were created. |
| ProcessState | Integer | No | The processing state of the instances to query. |
| PageNo | Integer | No | The number of the page to return. |
| PageSize | Integer | No | The number of entries to return on each page. |
| KeyWord | String | No | The keywords for the query. |
| SecurityGroupId | String | No | The ID of the security group to which the instances to query belong. |

s Center

| Parameter | Type | Required | Description |
|---|---|---|---|
| InstanceStatus | String | No | The states of the instances to query. By default, all states are selected. Running Starting Stopping Stopped |
| EventFlag | Boolean | No | Specifies whether the instances to query are related to security events. |
| VulFlag | Boolean | No | Specifies whether the instances to query have vulnerabilities. |
| FrangFlag | Boolean | No | Specifies whether the instances to query have security risks. |
| ScurityGroupFlag | Boolean | No | Specifies whether the instances to query belong to suspicious security groups. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| PageNo | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| Total | Integer | The total number of entries. |
| Items | Array | The list of instances. |
| └Uuid | Long | The UUID of the ECS instance. |
| └reationTime | String | The time when the instance was created. |
| └InstanceCreateTime | Long | The time when the instance was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| └eate | Long | The name of the baseline associated with the instance. |
| └Eip | String | The Elastic IP address associated with the instance. |
| └encryptedDisk | String | The disk encryption information. |

s Center

| Parameter | Type | Description |
|---|---|---|
| └eventCount | Integer | The number of security events related to the instance. |
| └innerIps | String | The internal IP address of the instance. |
| └instanceId | String | The ID of the instance. |
| └instanceName | String | The name of the instance. |
| └instanceStatus | String | The status of the instance. |
| └loginName | String | The username. |
| └osType | String | The operating system of the instance. |
| └publicIps | String | The public IP address of the instance. |
| └privateIps | String | The internal IP address of the instance. |
| └securityGroupIds | String | The IDs of the security groups. |
| └suspectSecurityGroup Count | Integer | The number of suspicious security groups. |
| └vulCount | Integer | The number of vulnerabilities detected on the instance. |
| └frangCount | Integer | The number of security risks detected on the instance. |
| └vpcId | String | The ID of the VPC network connected to the instance. |
| └aegisOnlineStatus | String | Indicates whether the Server Guard client is online. |
| └hostname | String | The name of the server. |
| └Cpu | Integer | The number of CPU cores. |
| └Memery | Integer | The size of memory. |
| └instanceNetworkType | String | The network type of the ECS instance. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetEcsList &PageNo=1 &PageSize=20
```

s Center Sample success responses in JSON format

```json
    "code":200,
    "data":{
        "Data":{
            "PageSize":1,
            "Total":41,
            "Items":[
                    "LoginName":"dtdep-4-157166417****",
                    "EventCount":6,
                    "InstanceCreateTime":1572228180000,
                    "Cpu":1,
                    "InstanceNetworkType":"vpc",
                    "EncryptedDisk":"0/1",
                    "OsType":"linux",
                    "InstanceStatus":"Running",
                    "DeptName":"yundun",
                    "Aliuid":163957166417****,
                    "Status":1,
                    "AegisOnlineStatus":"online",
                    "InstanceId":"i-3zn05zrit4i77ucl****",
                    "Hostname":"iZ3zn05zrit4i77ucl2****",
                    "SecurityGroupIds":"sg-3zn05zrit4i45cm4****",
                    "Eip":"",
                    "VulCount":0,
                    "Memery":2048,
                    "InstanceName":"sastestcenteros",
                    "Uuid":"325491ec-a64d-4d93-82d3-296314a9e8d5",
                    "VpcId":"vpc-3znsfwch9ilwlc0tk****",
                    "FrangCount":0,
                    "PrivateIps":"172. *. *.98",
                    "CreationTime":"2019-10-28T02:03Z",
                    "SuspectSecurityGroupCount":1,
                    "RegionId":"cn-qingdao-env8d****"
```

`],`

```json
            "PageNo":1
```

`},`

```json
    "requestId":"BBF5CA91-4D69-4A57-8F0C-42989CA4E60F",
    "success":true
```

For a list of error codes, visit the Error codes.

#### 8.3.20 GetDiskList

You can call this operation to query disk information of ECS instances. s Center

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GetDiskList. |
| Aliuid | Long | No | The department to query. |
| Region | String | No | The region to query. |
| PageNo | Integer | No | The number of the page to return. Default value: 1 |
| PageSize | Integer | No | The number of entries to return on each page. Default value: 10 |
| ProcessState | Integer | No | The state of the disk. |
| Keyword | Integer | No | The keywords for query. |
| InstanceId | String | No | The ID of the ECS instance to query. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Total | Integer | The total number of entries. |
| Items | Array | The list of disks. |
| └DeptNmae | String | The name of the department. |
| └Device | String | The mount point of the disk. |
| └diskId | String | The ID of the disk. |
| └diskName | String | The name of the disk. |
| └diskStatus | String | The usage status of the disk. |
| └Encrypted | Integer | Indicates whether the disk is encrypted. Valid values: 0: no 1: yes |
| └instanceId | String | The ID of the instance to which the disk belongs. |
| └InstanceName | String | The name of the instance to which the disk belongs. |

| Developer Guide·Security O | peration | Apsara Stack Securit |
|---|---|---|

s Center

| Parameter | Type | Description |
|---|---|---|
| └Size | Integer | The size of the disk. |
| └snapshotsCount | Integer | The number of snapshots. |
| └snapshotsTime | String | The time when the latest snapshot was created. |
| └Type | String | The type of the disk. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetDiskList
```

Sample success responses in JSON format

```json
    "RequestId":"DF618C9E-6B58-43A0-8E8A-B91162F198F4",
    "data":{
        "items":[
                "deptName":"cbctestdept****",
                "device":"/dev/xvdc",
                "diskId":"d-m5ef1im6qv2airbkocd2",
                "diskName":"cbctest",
                "diskStatus":"In_use",
                "encrypted":0,
                "instanceId":"i-m5eg3vpxqgaf9wox****",
                "instanceName":"cbctestinstance****",
                "size":20,
                "snapshotsCount":7,
                "snapshotsTime":"1536662000",
                "type":"data"
```

`],`

```json
        "total":1
```

For a list of error codes, visit the Error codes.

#### 8.3.21 GetSecurityGroupList

You can call this operation to obtain a list of security groups. s Center

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GetSecurityGroupList. |
| Aliuid | Long | No | The department to query. |
| Region | String | No | The region to query. |
| PageNo | Integer | No | The number of the page to return. Default value: 1 |
| PageSize | Integer | No | The number of entries to return on each page. Default value: 10 |
| ProcessState | Integer | No | The processing state of the security groups to query. |
| Keyword | Integer | No | The keywords for query. |
| ScurityGroupIds | List | No | The list of security group IDs. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the instance. |
| Total | Integer | The total number of entries. |
| Items | Array | The list of security groups. |
| └Create | Long | The ID of the user that created the security group. |
| └createTime | String | The time when the security group was created. |
| └instanceCreateTime | Long | The time when the instance in the security group was created. |
| └DeptName | String | The name of the department. |
| └Description | String | The description of the security group. |
| └instanceCount | Integer | The number of instances in the security group. |
| └networkType | String | The network type of the security group. |
| └permissionsCount | Integer | The number of rules configured for the security group. |
| └regionId | String | The ID of the region. |
| └securityGroupId | String | The ID of the security group. |

| s | Developer Guide·Security O Center | peration | Apsara Stack Securit | y |
|---|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| └securityGroupName | String | The name of the security group. |
| └suspectRule | String | Indicates whether the security group is related to suspicious rules. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetSecurityGroupList
```

Sample success responses in JSON format

```json
    "RequestId":"DF618C9E-6B58-43A0-8E8A-B91162F198F4",
    "data":{
        "items":[
                "create":1533110868000,
                "createTime":"2017-02-06T07:28:00Z",
                "instanceCreateTime":1537177380000,
                "deptName":"cbcTestDeptName",
                "description":"System created security group.",
                "instanceCount":3,
                "networkType":"vpc",
                "permissionsCount":8,
                "regionId":"cn-qingdao",
                "securityGroupId":"sg-m5e1f71l9kck0zh8pfry",
                "securityGroupName":"cbcgroup2",
                "suspectRule":true
```

`],`

```json
        "total":1
```

For a list of error codes, visit the Error codes.

#### 8.3.22 GetEcsInfo

You can call this operation to query the details of a specified ECS instance.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GetEcsInfo. |

| psara Stack Security |   |   | Developer Guide·Security Operatio s Cente |
|---|---|---|---|
| Parameter | Type | Required | Description |
| Uuid | String | Yes | The UUID of the ECS instance to query. |
| IstanceId | String | No | The ID of the ECS instance to query. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Aliuid | Long | The ID of the user to which the ECS instance belongs. |
| Uuid | Long | The UUID of the ECS instance. |
| reationTime | String | The time when the instance was created. |
| InstanceCreateTime | Long | The timestamp when the instance was created. |
| eate | Long | The name of the baseline. |
| Eip | String | The Elastic IP address bound to the ECS instance. |
| encryptedDisk | String | The disk encryption status. |
| eventCount | Integer | The number of security events detected on the instance. |
| innerIps | String | The internal IP address of the instance. |
| instanceId | String | The ID of the instance. |
| instanceName | String | The name of the instance. |
| instanceStatus | String | The status of the instance. |
| loginName | String | The name of the user. |
| osType | String | The operating system of the instance. |
| publicIps | String | The public IP address of the instance. |
| privateIps | String | The internal IP address of the instance. |
| securityGroupIds | String | The IDs of the security groups to which the instance belongs. |
| suspectSecurityGroupCo unt | Integer | The number of suspicious security groups. |

s Center

| Parameter | Type | Description |
|---|---|---|
| vulCount | Integer | The number of vulnerabilities detected on the instance. |
| frangCount | Integer | The number of security risks detected on the instance. |
| vpcId | String | The ID of the VPC to which the ECS instance is connected. |
| aegisOnlineStatus | String | Indicates whether the Server Guard client is online. |
| hostname | String | The name of the server. |
| Cpu | Integer | The number of CPU cores. |
| Memery | Integer | The size of memory. |
| instanceNetworkType | String | The network type of the ECS instance. |
| SecurityGroupIdList | Array | The information of the security group to which the ECS instance belongs. |
| Disks | Array | The disk information. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetEcsInfo &Uuid=7e77b1db-c29a-4548-8b32-533e3ae859da
```

Sample success responses in JSON format

```json
    "RequestId":"52734A7E-8E8B-46B1-822D-512A2A3085D3",
    "Data":{
        "Status":1,
        "LoginName":"bluecat****",
        "EventCount":0,
        "InstanceId":"i-m5eg3vpxqgaf9wox****",
        "InstanceCreateTime":1536564900000,
        "hostName":"m5e0hm705p9bhnd****",//The server name.
        "cpu":3,//The number of CPU cores.
        "memery":1024//The memory size.
        "instanceNetworkType":"vpc",//The network type.
        "SecurityGroupIdList":[
                "InstanceCount":0,
                "Description":"System created security group.",
                "SecurityGroupName":"cbcgroup1",
                "PermissionsCount":0,
```

s Center

```json
                "Create":1564045933000,
                "SecurityGroupId":"sg-m5e0hm705p9bhnd4xrsl",
                "DeptName":"Front end",
                "RegionId":"cn-qingdao"
```

`],`

```json
        "SecurityGroupIds":"sg-m5e0hm705p9bhnd4xrsl,sg-m5e8f3oy2h9b0hc8u6as",
        "Eip":"",
        "VulCount":0,
        "InstanceName":"cbctestinst****",
        "Uuid":"7e77b1db-c29a-4548-8b32-533e3ae859da",
        "PublicIps":"47. *. *.111",
        "OsType":"linux",
        "PrivateIps":"172. *. *.117",
        "InstanceStatus":"Stopped",
                "VpcId": "sg-m5e0",//vpcid
        "CreationTime":"2018-09-10T07:35Z",
        "Disks":[{"deptName": "cbctestdeptName",
            "device": "/dev/xvdc",
            "diskId": "d-m5ef1im6qv2airbk****",
            "diskName": "cbctest",
            "diskStatus": "In_use",
            "encrypted": 0,
            "instanceId": "i-m5eg3vpxqgaf9wox****",
            "instanceName": "cbctestinstanceName",
            "size": 20,
            "snapshotsCount": 7,
            "snapshotsTime": "1536662000",
            "type": "data"
        }],
        "DeptName":"Technical Department",
        "SuspectSecurityGroupCount":2,
        "RegionId":"cn-qingdao",
        "Aliuid":31234****
```

For a list of error codes, visit the Error codes.

#### 8.3.23 GetRdsList

You can call this operation to query ApsaraDB RDS instances.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GetRdsList. |

| eveloper Guide·Secur | ity Operation |   | Apsara Stack Securit |
|---|---|---|---|

s Center

| Parameter | Type | Required | Description |
|---|---|---|---|
| Aliuid | Long | No | The ID of the department. |
| Region | String | No | The region where the instances to query are located. |
| PageNo | Integer | No | The number of the page to return. Default value: 1 |
| PageSize | Integer | No | The number of entries to return on each page. Default value: 10 |
| ProcessState | Integer | No | The processing state of the instances to query. |
| Keyword | Integer | No | The keywords for query. |
| StartDate | String | No | The beginning of the time range during which the instances to query were created. |
| EndDate | String | No | The end of the time range during which the instances to query were created. |

s Center

| Parameter | Type | Required | Description |
|---|---|---|---|
| InstanceStatus | String | No | The state of the instances to query. By default, all states are selected. Creating Running Deleting Rebooting DBInstanceClassChanging: queries instances that are being upgraded or downgraded. TRANSING: queries instances that are being migrated. EngineVersionUpgrading: queries instances that are being upgraded. TransingToOthers: queries instances whose data is being migrated to other instances. GuardDBInstanceCreating: queries instances for which a disaster recovery instance is being created. Restoring: queries instances that are restoring backup data. Importing: queries instances that are importing data. ImportingFromOthers: queries instances that are importing data from other ApsaraDB RDS instances. DBInstanceNetTypeChanging: queries instances that are switching between the internal network and the Internet. GuardSwitching: queries instances under disaster recover failover. INSCLONING: queries instances that _ are being cloned. |
| whitelistIPLevel | String | No | The strictness degree of the whitelists to query. By default, all degrees are selected. rds whitelistiplevellow: loose _ _ rds whitelistiplevelmiddle: moderate _ _ rds whitelistiplevelhigh: strict _ _ |

s Center

| Parameter | Type | Required | Description |
|---|---|---|---|
| tdeFlag | Integer | No | Specifies whether Transparent Data Encryption (TDE) is enabled for the instances to query. By default, all options are selected. 0: disabled 1: enabled |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Id | Integer | The total number of entries. |
| deptName | String | The name of the department. |
| backupRetentionPeriod | Integer | The number of retained backups. |
| backupTimes | String | The frequency at which the instance data is backed up. |
| create | Long | The timestamp when the instance was created. |
| instanceCreateTime | Long | The time when the instance was created. |
| creationTime | String | The time when the data in this instance was synchronized to SOC. |
| dbInstanceDescription | String | The name of the instance. |
| dbInstanceId | String | The ID of the instance. |
| dbInstanceStatus | String | The status of the instance. |
| Engine | String | The database engine used by the instance. |
| instanceNetworkType | String | The network type of the instance. |
| sslFlag | Integer | Indicates whether SSL encryption is enabled. Valid values: 0: disabled 1: enabled |
| tdeFlag | Integer | Indicates whether TDE is enabled. Valid values: 0: disabled 1: enabled |
| whitelistIPLevel | String | The strictness degree of the IP address whitelist. |

s Center Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetRdsList
```

Sample success responses in JSON format

```json
    "code": 200,
    "data": {
        "items": [{
            "id": 10,//The primary key of the instance, which can be used to query details.
            "deptName": "cbcdept",//The department name.
            "backupRetentionPeriod": "7",//The number of backups.
            "backupTimes": "4/7",//The frequency at which the instance data is backed up.
            "create": 1536725464000,//The time when the data in this instance was synchroni
zed to SOC.
            "instanceCreateTime": 1537177380000,//The time when the instance was created.
            "creationTime": "2018-09-12T12:11:4Z",
            "dbInstanceDescription": "cbctestrdsvpc2",//The instance name.
            "dbInstanceId": "rm-m5es6x22suia0****",//The instance ID.
            "dbInstanceStatus": "Running",//The instance status.
            "engine": "MySQL",//The database engine used by the instance.
            "instanceNetworkType": "vpc",//The network type of the instance.
            "sslFlag": 0,//Indicates that SSL encrytion is disabled.
            "tdeFlag": 1,//Indicates that TDE is enabled.
            "whitelistIPLevel": "rds_whitelistiplevel_middle"//The strictness degree of the
IP address whitelist.
        }, {
            "id": 9,//The primary key of the instance.
            "deptName": "cbcdept",//The department name.
            "backupRetentionPeriod": "7",
            "backupTimes": "4/7",
            "create": 1536725464000,
            "creationTime": "2018-09-12T12:11:4Z",
            "dbInstanceDescription": "cbctestrdsvpc",
            "dbInstanceId": "rm-m5ekf1602691f****",
            "dbInstanceStatus": "Running",
            "engine": "MySQL",
            "instanceNetworkType": "VPC",
            "sslFlag": 1,
            "tdeFlag": 0,
            "whitelistIPLevel": "rds_whitelistiplevel_middle"
        }],
        "total": 2
```

`},`

```json
    "message": "successful",
    "success": true
```

s Center For a list of error codes, visit the Error codes.

#### 8.3.24 GetRdsInstanceIPArrayList

You can call this operation to query the whitelists configured for an ApsaraDB RDS instance.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GetRdsInstanceIPArrayList. |
| instanceId | Long | Yes | The ID of the ApsaraDB RDS instance to query. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| dbInstanceIPArrayName | String | The name of the IP address whitelist. |
| securityIPList | String | The IP addresses in the whitelist. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetRdsInstanceIPArrayList &InstanceId=12
```

Sample success responses in JSON format

```json
    "RequestId":"DF618C9E-6B58-43A0-8E8A-B91162F198F4",
    "data": {
        "items": [{
            "dbInstanceIPArrayName": "cbctestwhitelistgroup",//The whitelist name.
            "securityIPList": "172. *. *.117,192. *. *.1"//The IP addresses in the whitelis
```

`t.` `}{`

```json
            "dbInstanceIPArrayName": "default",
            "securityIPList": "127.0.0.1"
        }],
        "total": 2
```

s Center For a list of error codes, visit the Error codes.

#### 8.3.25 GetRdsInfo

You can call this operation to query the details of an ApsaraDB RDS instance.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GetRdsInfo. |
| DbInstanceId | String | Yes | The ID of the ApsaraDB RDS instance to query. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TdeFlag | Integer | Indicates whether Transparent Data Encryption (TDE) is enabled. 0: disabled 1: enabled |
| BackupTimes | String | The frequency at which the instance data is backed up. |
| DbInstanceStatus | String | The status of the instance. |
| SslFlag | Integer | Indicates whether SSL encryption is enabled. Valid values: 0: disabled 1: enabled |
| InstanceNetworkType | Long | The network type of the instance. |
| Create | String | The timestamp when the instance was created. |
| CreationTime | String | The time when the instance was created. |
| WhitelistIPLevel | String | Indicates the risk level of the IP address in the whitelist. rds whitelistiplevellow: low _ _ rds whitelistiplevelmiddle: medium _ _ rds whitelistiplevelhigh: high _ _ |

s Center

| Parameter | Type | Description |
|---|---|---|
| DeptName | String | The name of the department. |
| DbInstanceDescription | Integer | The name of the instance. |
| BackupRetentionPeriod | String | The period for which the backup data is retained. Unit: days |
| Aliuid | String | The ID of the department. |
| DbInstanceId | String | The ID of the instance. |
| Engine | String | The database engine used by the instance. |
| RdsWhiteipList | Array | The IP address whitelists configured for the ApsaraDB RDS instance. |
| └DbInstanceIPArrayNa me | String | The name of the IP address whitelist. |
| └SecurityIPList | String | The IP addresses in the whitelist. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetRdsInfo &DbInstanceId=123
```

Sample success responses in JSON format s Center

```json
    "RequestId":"60796AED-1FD6-4769-85FF-322B7990EA99",
    "Data":{
        "TdeFlag":0,
        "BackupTimes":"3/7",
        "DbInstanceStatus":"Running",
        "SslFlag":1,
        "InstanceNetworkType":"vpc",
        "Create":1537521344000,
        "CreationTime":"2018-09-12T16:30Z",
        "WhitelistIPLevel":"rds_whitelistiplevel_high",
        "DeptName":"waf-dept",
        "DbInstanceDescription":"cbctestrdsvpc2",
        "BackupRetentionPeriod":7,
        "Aliuid":12****,
        "DbInstanceId":"rm-m5es6x22suia0****",
        "Engine":"MySQL",
        "RdsWhiteipList":[
                "DbInstanceIPArrayName":"cbctestwhitelistgroup",
                "SecurityIPList":"172. *. *.117,192. *. *.1"
```

`},`

```json
                "DbInstanceIPArrayName":"default",
                "SecurityIPList":"127.0.0.1"
```

`]` For a list of error codes, visit the Error codes.

#### 8.3.26 GetOssList

You can call this operation to obtain a list of OSS buckets.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GetOssList. |
| Aliuid | Long | No | The ID of the department. |
| Region | String | No | The region where the buckets to query are located. |
| PageNo | Integer | No | The number of the page to return. Default value: 1 |

| D s | eveloper Guide·Secur Center | ity Operation |   | Apsara Stack Securit | y |
|---|---|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| PageSize | Integer | No | The number of entries to return on each page. Default value: 10 |
| Keyword | Integer | No | The keywords for query. |
| StartDate | String | No | The beginning of the time range during which the buckets to query were created. |
| EndDate | String | No | The end of the time range during which the buckets to query were created. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Total | Integer | The total number of entries. |
| allowEmptyReferer | Integer | Indicates whether the OSS bucket allows an access request with an empty Referer header. Valid values: 0: no 1: yes |
| bucketName | String | The name of the instance. |
| cannedACL | String | The ACL permission of the bucket. |
| configRefererList | Integer | Indicates whether a Referer header whitelist is configured. 0: no 1: yes |
| regionId | String | The region where the bucket is located. |
| Size | Integer | The used storage space. |
| instanceCreateTime | Long | The time when the bucket was created. |
| deptName | String | The name of the department. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetOssList
```

s Center Sample success responses in JSON format

```json
    "RequestId":"DF618C9E-6B58-43A0-8E8A-B91162F198F4",
    "data": {
        "items": [{
            "allowEmptyReferer": 1,//Indicates whether the OSS bucket allows an access requ
est with an empty Referer header.
            "bucketName": "cbctestoss",//The bucket name.
            "cannedACL": "private",//The ACL permission of the bucket.
            "configRefererList": 1,//Indicates whether a Referer header whitelist is config
ured.
            "instanceCreateTime": 1537177380000,//The timestamp when the bucket was created
```

`.`

```json
            "deptName": "cbcTestDept",//The department name.
            "regionId": "oss-cn-qingdao",//The region.
            "size": 3278531//The used storage space. Unit: Byte
        }, {
            "allowEmptyReferer": 0,
            "bucketName": "cbctestoss2",
            "cannedACL": "public-read",
            "configRefererList": 0,
            "instanceCreateTime": 1536828385000,
            "deptName": "cbcTestDept",
            "regionId": "oss-cn-qingdao",
            "size": 1618792
        }],
        "total": 2
```

For a list of error codes, visit the Error codes.

#### 8.3.27 GetSlbList

You can call this operation to obtain a list of SLB instances.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GetSlbList. |
| Aliuid | Long | No | The ID of the department to query. |
| Region | String | No | The region to query. |
| PageNo | Integer | No | The number of the page to return. Default value: 1 |

| eveloper Guide·Secur Center | ity Operation |   | Apsara Stack Securit |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| PageSize | Integer | No | The number of entries to return on each page. Default value: 10 |
| Keyword | Integer | No | The keywords for query. |
| StartDate | String | No | The beginning of the time range during which the instances to query were created. |
| EndDate | String | No | The end of the time range during which the instances to query were created. |
| instanceStatus | String | No | The status of the instances to query. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Total | Integer | The total number of entries. |
| address | String | The IP address of the SLB instance. |
| addressType | Long | The network type of the SLB IP address. |
| createTime | Long | The time when the instance was created. |
| instanceCreateTime | Long | The timestamp when the instance was created. |
| DeptName | String | The name of the department. |
| listenerPortAndProtocol | String | The listening protocol and listening port. |
| loadBalancerId | String | The ID of the SLB instance. |
| loadBalancerName | String | The name of the SLB instance. |
| loadBalancerStatus | String | The status of the SLB instance. |
| networkType | String | The network type of the SLB instance. |
| regionId | String | The region where the SLB instance is located. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetSlbList
```

s Center Sample success responses in JSON format

```json
    "RequestId":"DF618C9E-6B58-43A0-8E8A-B91162F198F4",
    "data": {
        "items": [{
            "address": "10. *. *.158",//The IP address of the SLB instance.
            "addressType": "intranet",//The network type of the instance IP address.
            "create": 1574222416000,//The time when the instance was created.
            "createTime": 2019-11-20T03:21:47Z,
            "instanceCreateTime": 1574220107000,//The timestamp when the instance was creat
ed.
            "deptName": "cbcTestDept",//The department name.
            "listenerPortAndProtocol": "notConfiged",//The listening protocol and listening
port.
            "loadBalancerId": "lb-m5egfr9bph8ki4ork****",//The instance ID.
            "loadBalancerName": "cbc_slb_2",//The instance name.
            "loadBalancerStatus": "inactive",//The instance status.
            "networkType": "classic",//The network type of the instance.
            "regionId": "cn-qingdao"//The region of the instance.
        }, {
            "address": "118. *. *.174",
            "addressType": "internet",
            "create": 1537168200000,
            "createTimeStamp": 1537168251000,
            "deptName": "cbcTestDept",
            "listenerPortAndProtocol": "http:8080@tcp:80",//The listening protocol and list
ening port.
            "loadBalancerId": "lb-m5e6yqpi4r34lxh5q****",
            "loadBalancerName": "cbc_slb_1",
            "loadBalancerStatus": "active",
            "networkType": "classic",
            "regionId": "cn-qingdao"
        }],
        "total": 2
```

For a list of error codes, visit the Error codes.

#### 8.3.28 GetEipList

You can call this operation to obtain a list of Elastic IP addresses.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GetEipList. |

| D s | eveloper Guide·Secur Center | ity Operation |   | Apsara Stack Securit | y |
|---|---|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| Aliuid | Long | No | The ID of the department to query. |
| Region | String | No | The region to query. |
| PageNo | Integer | No | The number of the page to return. Default value: 1 |
| PageSize | Integer | No | The number of entries to return on each page. Default value: 10 |
| Keyword | Integer | No | The keywords for query. |
| StartDate | String | No | The beginning of the time range during which the instances to query were created. |
| EndDate | String | No | The end of the time range during which the instances to query were created. |
| instanceStatus | String | No | The status of the instances to query. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Total | Integer | The total number of entries. |
| Items | Aray | The list of Elastic IP addresses. |
| └allocationId | Long | The ID of the user who created the instance. |
| └allocationTime | String | The time when the user applied for the instance. |
| └create | Long | The timestamp when the user applied for the instance. |
| └instanceCreateTime | String | The time when the instance was created. |
| └deptName | String | The name of the department. |
| └instanceId | String | The ID of the instance. |
| └instanceName | String | The name of the instance. |
| └instanceType | Integer | The type of the instance. |
| └ipAddress | String | The Elastic IP address. |

s Center

| Parameter | Type | Description |
|---|---|---|
| └Bandwidth | String | The peak bandwidth of the Elastic IP address. Unit: Mbit/s. |
| └regionId | String | The region where the instance is located. |
| └eipStatus | String | The status of the Elastic IP address. Valid values: Associating: The Elastic IP address is being bound to an ECS instance. Unassociating: The Elastic IP address is being unbound from an ECS instance. InUse: The Elastic IP address is bound to an instance. Available: The Elastic IP address is available. |
| └status | Integer | Indicates whether the Elastic IP address is valid. Valid values: 1: valid 0: invalid |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetEipList
```

Sample success responses in JSON format

```json
    "RequestId":"DF618C9E-6B58-43A0-8E8A-B91162F198F4",
    "data":{
        "items":[
                "allocationId":"eip-m5eg8x8npvmarymgg****",
                "allocationTime":"2018-09-17T09:22:10Z",
                "create":1537147330000,
                "instanceCreateTime":1537177380000,
                "deptName":"cbcTestDept",
                "instanceId":"",
                "instanceName":"cbctestInstance",
                "instanceType":"",
                "ipAddress":"47. *. *.200",
                "regionId":"cn-qingdao",
                "status":"Available"
```

`],`

```json
        "total":1
```

s Center For a list of error codes, visit the Error codes.

#### 8.3.29 GetAlarmConfig

You can call this operation to query the alert configuration.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GetAlarmConfig. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Total | Integer | The total number of entries. |
| PageSize | Integer | The number of entries returned per page. |
| PageNo | Integer | The page number of the returned page. |
| Items | Array | The alert configuration. |
| └Dingding | Integer | Indicates whether to send alerts by DingTalk. Valid values: 1: yes 0: no |
| └Description | String | The description of the alert type. |
| └Mail | String | Indicates whether to send alerts by email. Valid values: 1: yes 0: no |
| └AlarmIdentify | Integer | The identifier of the alert configuration. |
| └Sms | Integer | Indicates whether to send alerts by SMS. Valid values: 1: yes 0: no |
| └Title | Integer | The name of the alert type. |
| └Level | String | The risk level of the alert. |

| psara Stack Security |   | s Cente |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| └Id | Integer | The ID of the configuration. |
| └category | Integer | Indicates whether the alert source is a user or the platform. Valid values: 1: user 2: platform |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetAlarmConfig
```

Sample success responses in JSON format

```json
    "RequestId":"385333D5-1796-41EC-A62F-239881EC75E6",
    "Data":{
        "PageSize":10,
        "Total":1,
        "Items":[
                "Dingding":0,
                "Description":"Attackers have intruded into the tenant system by webshells,
malicious code, and suspicious processes.",
                "Mail":0,
                "AlarmIdentify":"USER_ALARM",
                "Sms":0,
                "Title":"Security Alerts",
                "Level":"",
                "Id":7,
                "category":1
```

`],`

```json
        "PageNo":1
```

For a list of error codes, visit the Error codes.

#### 8.3.30 UpdateAlarmConfig

You can call this operation to update the alert configuration. s Center

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to UpdateAlarmConfig. |
| Configs | String | Yes | The updated alert configuration. The value is a JSON array. Each object in this array specifies a parameter, such as id, mail, sms, and dingding. //Example [{\"id\":7,\"mail\":1,\"sms\":1 ,\"dingding\":1,\"alarmIdentify \":\"USER ALARM\"}] _ |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Data | String | The result of the operation. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=UpdateAlarmConfig
```

Sample success responses in JSON format

```json
    "RequestId":"15BFC394-3316-4948-BF54-E6B8875DA023",
    "Data":"succes"
```

For a list of error codes, visit the Error codes.

#### 8.3.31 GetAlarmContacts

You can call this operation to obtain a list of alert recipients.

| Parameter | Type | Required | Description |
|---|---|---|---|

s Center

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GetAlarmContacts. |
| PageSize | Integer | No | The number of entries to return on each page. Default value: 10 |
| PageNo | Integer | No | The number of the page to return. Default value: 1 |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Total | Interger | The total number of entries. |
| PageSize | Integer | The number of entries returned per page. |
| PageNo | Integer | The page number of the returned page. |
| Items | Array | The list of alert recipients. |
| └Dingding | Integer | The DingTalk username of the alert recipient. |
| └Mail | String | The email address of the alert recipient. |
| └Id | Integer | The ID of the alert recipient. |
| └Mobile | String | The mobile phone number of the alert recipient. |
| └Name | String | The name of the alert recipient. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetAlarmContacts
```

Sample success responses in JSON format s Center

```json
    "RequestId":"4DC990E4-2A59-4F4A-BDE6-CC35B5C730F1",
    "Data":{
        "PageSize":10,
        "Total":1,
        "Items":[
                "Dingding":"dingding",//The Dingtalk username of the alert recipient.
                "Mail":"test@****.com",//The email address of the alert recipient.
                "Id":1,//The ID of the alert recipient.
                "Mobile":"1380000****",//The mobile phone number of the alert recipient.
                "Name":"test"//The name of the alert recipient.
```

`],`

```json
        "PageNo":1
```

For a list of error codes, visit the Error codes.

#### 8.3.32 AddAlarmContacts

You can call this operation to add an alert recipient or modify alert recipient information.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to AddAlarmContacts. |
| Name | String | Yes | The name of the alert recipient. |
| Mobile | String | No | The mobile phone number of the alert recipient. |
| Id | Long | No | The ID of the alert recipient. This parameter is optional when you add an alert recipient. This parameter is required when you modify an alert recipient. |
| Dingding | String | Yes | The DingTalk username of the alert recipient. |

s Center

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Data | String | The result of the operation. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=AddAlarmContacts &Name=aaa &Dingding=123123
```

Sample success responses in JSON format

```json
    "RequestId":"DF618C9E-6B58-43A0-8E8A-B91162F198F4",
    "data": “sucess”
```

For a list of error codes, visit the Error codes.

#### 8.3.33 DeleteAlarmContacts

You can call this operation to delete alert recipients.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteAlarmContacts. |
| Id | Long | Yes | The ID of the alert recipient to delete. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Data | String | Indicates whether the alert recipient is deleted. |

Sample requests s Center

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=DeleteAlarmContacts &Id=123
```

Sample success responses in JSON format

```json
    "RequestId":"DF618C9E-6B58-43A0-8E8A-B91162F198F4",
    "data":”sucess”
```

For a list of error codes, visit the Error codes.

#### 8.3.34 SendAlarm

You can call this operation to send an alert.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to SendAlarm. |
| AlarmIdentify | String | Yes | The identifier of the alert configuration. USERATTACK indicates an attack on a _ user. USERALARM indicates a security alert _ on a user. USERFRANG indicates a security risk _ on a user. PLATFORMATTACK indicates an attack _ on the platform. PLATFORMALARM indicates a security _ alert on the platform. PLATFORMFRANG indicates a security _ risk on the platform. |
| Message | String | Yes | The alert message. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Data | String | Indicates whether the alert is sent. |

s Center Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=SendAlarm &AlarmIdentify=USER_ATTACK &Message=aaaaaaaaaa
```

Sample success responses in JSON format

```json
    "RequestId":"DF618C9E-6B58-43A0-8E8A-B91162F198F4",
    "data":”sucess”
```

For a list of error codes, visit the Error codes.

#### 8.3.35 QuerySource

You can call this operation to query log sources.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to QuerySource. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| PageSize | Integer | The number of entries returned per page. |
| PageNo | Integer | The page number of the returned page. |
| Total | Integer | The total number of entries. |
| Items | Array | The list of log sources. |
| └SourceFrom | String | The Chinese name of the log source. |
| └Source | String | The name of the log source. |

Sample requests s Center

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=QuerySource
```

Sample success responses in JSON format

```json
    "RequestId":"E2E67B85-0CCA-4C5F-90FE-382F4580C2D9",
    "Data":{
        "PageSize":1,
        "Total":1,
        "Items":[
                "SourceName":"Server Guard",
                "Source":"aegis"
```

`],`

```json
        "PageNo":1
```

For a list of error codes, visit the Error codes.

#### 8.3.36 QueryType

You can call this operation to query the types of logs from a specified log source.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to QueryType. |
| Source | String | Yes | The log source. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| PageSize | Integer | The number of entries to return on each page. |
| PageNo | Integer | The number of the page to return. |
| Total | Integer | The total number of entries. |
| Items | Array | The list of log types. |

| psara Stack Security |   | Developer Guide·Security Operatio |
|---|---|---|

s Center

| Parameter | Type | Description |
|---|---|---|
| └Id | Long | The ID of the log type. |
| └Topic | String | The name of the log type. |
| └TopicName | String | The Chinese name of the log type. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=QueryType &Source=beaver
```

Sample success responses in JSON format

```json
    "RequestId":"2D884100-06C5-42BE-B534-FD26A5454FE2",
    "Data":{
        "PageSize":1,
        "Total":1,
        "Items":[
                "Id":1,
                "Topic":"T_MSG_SOFTWARE_INSTALL",
                "TopicName":"Installation software information"
```

`],`

```json
        "PageNo":1
```

For a list of error codes, visit the Error codes.

#### 8.3.37 QueryLog

You can call this operation to query log records from a specified log source.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to QueryLog. |
| Id | Long | Yes | The ID of the log source. |
| keyword | String | No | The keywords of the log records. |

| Center |   |   | Apsara Stack Securit |
|---|---|---|---|
| Parameter | Type | Required | Description |
| From | Long | Yes | The beginning of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| To | Long | Yes | The end of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| pageSize | Integer | Yes | The number of entries to return on each page. |
| PageNo | Integer | Yes | The number of the page to return. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| LogList | String | The log content. |
| HistogramList | List | The data in the graph displayed in the console. |
| KeyList | List | A list of the keys of all log records. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=QueryLog &Id=9 &From=1574149923989 &To=1574236323989 &PageSize=10 &PageNo=1
```

Sample success responses in JSON format

```json
    "LogList":[
            "LogTime":1566273660000,
            "ColumnList":[
                    "Value":"rpm",
                    "TokenList":[
```

`]` s Center `],`

```json
                    "Key":"type"
```

`},`

```json
                    "Value":"inet-f74289a3-87fc-4a2d-8d04-b68b21489dd1",
                    "TokenList":[
```

`],`

```json
                    "Key":"uuid"
```

`],`

```json
            "Source":"T_MSG_SOFTWARE_INSTALL"
```

`},`

```json
            "LogTime":1566273660000,
            "ColumnList":[
                    "Value":"success",
                    "TokenList":[
```

`],`

```json
                    "Key":"status"
```

`],`

```json
            "Source":"T_MSG_SOFTWARE_INSTALL"
```

`],`

```json
    "TotalCount":891,
    "HistogramList":[
            "EndTime":1566292920000,
            "Completed":true,
            "StartTime":1566288000000,
            "Count":0
```

`],`

```json
    "PageSize":2,
    "RequestId":"4F183A8B-402C-4BE4-83FD-000676AE00DE",
    "KeyList":[
        "app_version",
        "safe_mode",
        "update",
        "task_id",
        "bit",
        "type",
        "uuid",
        "cmd_idx",
        "path",
        "sys_version",
        "execresult",
        "vendor",
        "action",
        "exectime",
        "install_date",
        "seq",
        "etm",
"app",
```

s Center

```
        app,
        "traceId",
        "product",
        "module_type",
        "ip",
        "os_version",
        "sys_kernel",
        "stm",
        "version",
        "module_id",
        "sys_product",
        "pro_version",
        "sys_vendor",
        "status"
```

`]` For a list of error codes, visit the Error codes.

#### 8.3.38 GetVpcList

You can call this operation to obtain a list of VPCs.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GetVpcList. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Data | List | The list. |
| Items | List | The information of VPCs. |
| Total | Integer | The total number of entries. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetVpcList
```

Sample success responses in JSON format s Center

```json
    "RequestId":"D533DCF9-2BFA-490C-99CF-DBA2A4BA6747",
    "Data":{
        "Total":3,
        "Items":[
                "Value":"1",//vpcid
                "Key":"1"//vpcid
```

`},`

```json
                "Value":"vpc-*********************",
                "Key":"vpc-*********************"
```

`]` For a list of error codes, visit the Error codes.

#### 8.3.39 GetMachineList

You can call this operation to obtain a list of assets.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GetMachineList. |
| aliUid | Long | No | The AliUid of the department. |
| Region | String | No | The region to query. |
| pageNo | Integer | No | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | The number of entries to return on each page. Default value: 10. |
| StartDate | String | No | The beginning of the time range during which the servers to query were created. |
| EndDate | String | No | The end of the time range during which the servers to query were created. |
| Keyword | String | No | The keyword of the assets to query. |
| EventFlag | Boolean | No | Specifies whether the assets to query are related to alert events. |

| D s | eveloper Guide·Secur Center | ity Operation |   | Apsara Stack Securit | y |
|---|---|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| VulFlag | Boolean | No | Specifies whether the assets to query have vulnerabilities. |
| FrangFlag | Boolean | No | Specifies whether the assets to query have security risks. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Data | List | The list. |
| Items | List | The asset information. |
| Total | Integer | The total number of entries. |
| pageNo | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetMachineList &PageSize=10 &PageNo=1 &keyword=aaa
```

Sample success responses in JSON format s Center

```json
    "RequestId":"B06F0BC3-29AE-461A-9C2C-F50319C2FD1B",
    "Data":{
        "PageSize":10,
        "Total":1,
        "Items":[
                        "ClientStatus":"offline",//Indicates whether the Server Guard clien
t is online.
                        "Uuid":"inet-8a0569b3-15f8-482d-9a9e-cf85760c3b3a",//The UUID of th
e asset.
                        "InternetIp":"*. *. *. *",//The public IP address of the asset.
                        "IntranetIp":"*. *. *. *",//The internal IP address of the asset.
                        "FrangCount":0,//The number of security risks.
                    "MachineName":"*. *. *. *",//The name of the server.
                        "Os":"linux",//The operating system.
                        "EventCount":0,//The number of attack events.
                        "Aliuid":123456789,//The default AliUid of a physical server is 123
456789. "MachineIp":"*. *. *. *",//The IP address of the server.
                        "VulCount":0//The number of alert events.
```

`],`

```json
        "PageNo":1
```

For a list of error codes, visit the Error codes.

#### 8.3.40 GetMachineInfo

You can call this operation to query asset information.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GetMachineInfo. |
| uuid | Long | Yes | The UUID of the asset. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| ClientStatus | String | Indicates whether the Server Guard client is online. |

| D s | eveloper Guide·Security O Center | peration | Apsara Stack Securit | y |
|---|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| Uuid | String | The UUID of the asset. |
| InternetIp | String | The public IP address of the asset. |
| IntranetIp | String | The internal IP address of the asset. |
| FrangCount | Integer | The number of vulnerabilities on the asset. |
| MachineName | String | The name of the server. |
| Os | String | The operating system of the server. |
| EventCount | Integer | The number of attack events. |
| GroupId | Integer | The ID of the group. |
| Modified | Long | The time when the asset was modified. |
| Create | Long | The time when the asset was created. |
| MachineRegion | String | The region to which the server belongs. |
| Aliuid | Long | The AliUid of the department. |
| MachineIp | String | The IP address of the server. |
| VulCount | Integer | The number of alert events. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetMachineInfo &Uuid=inet-8a0569b3-15f8-482d-9a9e-cf85760c3b3a
```

Sample success responses in JSON format s Center

```json
    "RequestId":"E0283B3D-C202-4EDD-9FF4-1BD5FF3F35FE",
    "Data":{
                "ClientStatus":"offline",//Indicates whether the Server Guard client is onl
ine.
                "Uuid":"inet-8a0569b3-15f8-482d-9a9e-cf85760c3b3a",//The UUID of the asset.
"InternetIp":"*. *. *. *",//The public IP address of the server.
                "IntranetIp":"*. *. *. *",//The internal IP address of the server.
                "FrangCount":0,//The number of security risks.
"MachineName":"*. *. *. *",//The name of the server.
                "Os":"linux",//The operating system.
                "EventCount":0,//The number of attack events.
                "GroupId":18,//The ID of the group.
                "Modified":1573716945000,//The time when the server was modified.
                "Create":1573716945000,//The time when the server was created.
                "MachineRegion":"outside-of-aliyun",//The region to which the server belong
```

`s.`

```json
                "Aliuid":123456789,//The default AliUid of a physical server is 123456789.
"MachineIp":"*. *. *. *",//The IP address of the server.
                "VulCount":0//The number of alert events.
```

For a list of error codes, visit the Error codes.

#### 8.3.41 DescribeSocUsers

You can call this operation to query users.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSocUsers. |
| Aliuid | Long | No | The AliUid of the department. |
| DeptName | String | No | The name of the department. |
| Level | Integer | No | The level of the department. |
| LoginName | String | No | The logon username. |
| Source | String | No | The data source. Valid values: DT ASCM openApi |

s Center

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Items | Array | A list of the users. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=DescribeSocUsers
```

Sample success responses in JSON format

```json
    "RequestId":"EDDB2FAF-2FFD-4D08-BB25-93BFC96BF7BB",
    "Data":[
                    "AccountSystemName":"***",
                    "LoginName":"***bc",
                    "Modified":1548661368000,
                    "Create":1543318601000,
                    "Level":1,
                    "DeptName":"Legal Department",
                    "Id":2,
                    "ParentDeptId":1,
                    "Aliuid":1782421049074576,
                    "DeptId":2,
                    "ParentDeptName":"root",
                    "Source":"DT"
```

`},`

```json
                    "AccountSystemName":"a***te",
                    "LoginName":"b**t",
                    "Modified":1548661368000,
                    "Create":1543318601000,
                    "Level":1,
                    "DeptName":"Technical Department",
                    "Id":3,
                    "ParentDeptId":1,
                    "Aliuid":1461680564,
                    "DeptId":3,
                    "ParentDeptName":"root",
                    "Source":"DT"
```

`],`

```json
    "Success":true
```

s Center For a list of error codes, visit the Error codes.

#### 8.3.42 DeleteSocUser

You can call this operation to delete a user.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteSocUser. |
| Aliuid | Long | Yes | The AliUid of the department. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Success | Boolean | The value of True indicates a success. The value of False indicates a failure. |

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=DeleteSocUser &Aliuid=12312312312
```

Sample success responses in JSON format

```json
    "RequestId":"A3B53D56-C6CA-48F1-AF91-B5E28557DCAD",
    "Data":[
```

`],`

```json
    "Success":true
```

For a list of error codes, visit the Error codes.

#### 8.3.43 SaveOrUpdateSocUser

You can call this operation to add a user or modify user information. s Center

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to SaveOrUpdateSocUser. |
| Aliuid | Long | Yes | The AliUid of the department. |
| DeptId | Long | Yes | The ID of the department. |
| DeptName | String | Yes | The name of the department. |
| Level | Integer | No | The level of the department. |
| LoginName | String | No | The logon username. |
| ParentDeptId | Long | No | The ID of the parent department. |
| ParentDeptName | String | No | The name of the parent department. |
| AccountSystemNa me | String | No | The name of the system account to add or modify. |
| AccessKey | String | No | The AccessKey ID. Not e This parameter is required when you add a new user but optional when you modify user information. |
| AccessSecret | String | No | The AccessKey secret. Not e This parameter is required when you add a new user but optional when you modify user information. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Success | Boolean | The value of True indicates a success. The value of False indicates a failure. |

Sample requests s Center

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=SaveorupdateSocUser
```

Sample success responses in JSON format

```json
    "RequestId":"A3B53D56-C6CA-48F1-AF91-B5E28557DCAD",
    "Data":[
```

`],`

```json
    "Success":true
```

For a list of error codes, visit the Error codes.

## 9 Error codes

This topic describes the error codes returned by operations for Alibaba Cloud Security. Common error codes of Apsara Stack Security

| Error code | Error message | Description |
|---|---|---|
| yd.error.all.10001 | Authorization required. | The error message returned because you are not authorized to perform the operation. Check the account permissions. |
| yd.error.all.10002 | A system error has occurred. Try again later. | The error message returned because a system error has occurred. Try again later. |
| yd.error.all.10003 | The parameter is invalid. | The error message returned because the specified request parameter is invalid. Check the request parameter and try again. |
| yd.error.all.other | A system error has occurred. | The error message returned because a system error has occurred. Try again later. |
| yd.error.all.ConsoleSystemError 1 _ 001 | An internal error has occurred. | The error message returned because a system error has occurred. Try again later. |
| yd.error.all.ConsoleSystemError 1 _ 007 | The specified API is unavailable. | The error message returned because the operation has been brought offline. Contact Alibaba Cloud technical support. |
| yd.error.all.ConsoleSystemError 1 _ 008 | An error occurred while verifying postOnly. | The error message returned because the verification has failed. Check the common request parameters and try again. |
| yd.error.all.ConsoleSystemError 1 _ 009 | csrfToken must not be empty. | The error message returned because the csrfToken field is empty. Check the common request parameters and try again. |
| yd.error.all.ConsoleSystemError 1 _ 010 | An error occurred while verifying csrfToken. | The error message returned because the verification has failed. Check the common request parameters and try again. |

| Error code | Error message | Description |
|---|---|---|
| yd.error.all.ConsoleSystemError 1 _ 011 | The Region ID must not be empty. | The error message returned because the RegionId request parameter is empty. Check the parameter. |
| yd.error.all.ConsoleSystemError 1 _ 012 | The specified region ID format is invalid. | The error message returned because the specified region ID format is invalid. Check the RegionId parameter. |
| yd.error.all.ConsoleSystemError 1 _ 013 | The parameter is null. | The error message returned because the specified request parameter is empty. Check the request parameter and try again. |
| yd.error.all.ConsoleSystemError 1 _ 014 | The specified parameter format is invalid. | The error message returned because the specified parameter format is invalid. Check the request parameter and try again. |
| yd.error.all.ConsoleNeedLogin | You are not logged on. | The error message returned because you are not authorized to perform the operation. Check the account permissions. |
| yd.error.all.InvalidApi | The API is invalid. | The error message returned because an operation exception has occurred. Try again later. |
| yd.error.all.InvalidParameter | The parameter is invalid. | The error message returned because the specified request parameter is invalid. Check the request parameter and try again. |
| yd.error.all.InvalidResult | The return value is invalid. | The error message returned because the return value is invalid. Try again later. |
| yd.error.all.PropertyConvertFailed | An error occurred during conversion. | The error message returned because property conversion has failed. Try again later. |
| yd.error.all.NoPermission | Authorization required. | The error message returned because you are not authorized to perform the operation. Check the account permissions. |
| yd.error.all.ServerError | A server error has occurred. | The error message returned because a server error has occurred. Try again later or contact Alibaba Cloud technical support. |

| Error code | Error message | Description |
|---|---|---|
| yd.error.all.UnkownError | An internal error has occurred. | The error message returned because an unknown error has occurred. Try again later or contact Alibaba Cloud technical support. |

Error codes of Threat Detection Service

| Error code | Error message | Description |
|---|---|---|
| yd.error.sas.1 | The specified field has not been found in the metadata. | The error message returned because the field you queried does not exist in the metadata. Check the request and try again. |
| yd.error.sas.2 | An error occurred while invoking the task engine. Try again later. | The error message returned because the system has failed to call the task engine. Try again later. |
| yd.error.sas.3 | An error occurred while starting the task. Try again later. | The error message returned because the system has failed to start the task. Try again later. |
| yd.error.sas.4 | An error occurred while stopping the task. Try again later. | The error message returned because the system has failed to stop the task. Try again later. |
| yd.error.sas.5 | An error occurred while restarting the task. Try again later. | The error message returned because the system has failed to restart the task. Try again later. |
| yd.error.sas.6 | An error occurred while obtaining the task status. Try again later. | The error message returned because the system has failed to obtain the task status. Try again later. |
| yd.error.sas.7 | An error occurred while deleting the task. Try again later. | The error message returned because the system has failed to delete the task. Try again later. |
| yd.error.sas.8 | The specified table does not contain metadata. | The error message returned because the table you queried does not contain metadata. Check the request and try again. |
| yd.error.sas.100 | Request failed. Refresh the page and try again. | The error message returned because the request has failed. Try again later. |

| Error code | Error message | Description |
|---|---|---|
| yd.error.sas.101 | The parameter is invalid. | The error message returned because the specified parameter is invalid. Check the request and try again. |
| yd.error.sas.103 | Request failed. | The error message returned because the request has failed. Try again later. |
| yd.error.sas.400 | The specified asset is under protection. Uninstall the Server Guard client and try again. | The error message returned because the asset you want to delete is protected. Uninstall the Server Guard agent from the server and try again. |
| yd.error.sas.500 | A system error has occurred. | The error message returned because a system error has occurred. Contact Alibaba Cloud technical support. |
| yd.error.sas.501 | The function is not available in the current version. | The error message returned because the version you used does not support this feature. |
| yd.error.sas.502 | You are not authorized to access the instance. | The error message returned because you are not authorized to operate the server. |

Error codes of Anti-DDoS

| Error code | Error message | Description |
|---|---|---|
| yd.error.ddos.400 | An error occurred while accessing the server. Try again later. | The error message returned because the system has failed to access the server. Check the request and try again. |
| yd.error.ddos.500 | An error occurred on the server. | The error message returned because a server error has occurred. Contact Alibaba Cloud technical support. |
| yd.error.ddos.UNKNOWN EXCEPTI _ ON | An internal error occurred. | The error message returned because an unknown error has occurred. Contact Alibaba Cloud technical support. |
| yd.error.ddos.REQUEST TIMEOUT _ | The request has timed out. | The error message returned because the request has timed out. Try again later. |

| Error code | Error message | Description |
|---|---|---|
| yd.error.ddos.SERVER FAILED _ | An operation error occurred. | The error message returned because the operation has failed. Contact Alibaba Cloud technical support. |
| yd.error.ddos.NOT AUTHORIZED _ | You are not authorized to perform this operation. | The error message returned because you are not authorized to perform the operation. Check the account permissions. |
| yd.error.ddos.PARAMETER INVALI _ D | The specified parameter is invalid or missing. | The error message returned because the specified request parameter is invalid. Check the request parameter and try again. |
| yd.error.ddos.IP SEGMENT INVALI _ _ D | The specified CIDR block is invalid. | The error message returned because the specified CIDR block is invalid. Check the CIDR block specified in the request parameter. |
| yd.error.ddos.IP SEGMENT REPEA _ _ T | One CIDR block cannot be used in different regions. Enter another CIDR block. | The error message returned because one CIDR block belongs to multiple regions. Check the CIDR block specified in the request parameter. |
| yd.error.ddos.IP SEGMENT ALREA _ _ DY | The specified CIDR block already exists. | The error message returned because the specified CIDR block has been used. Check the CIDR block specified in the request parameter. |
| yd.error.ddos.IP SEGMENT MASK _ _ _ LENGTH ERR _ | The prefix length must be less than 24 bits. | The error message returned because the mask contains more than 24 bits. Check the CIDR block mask specified in the request parameter. |
| yd.error.ddos.QUERY REGION LIST _ _ ERR _ | An error occurred while obtaining the region list. | The error message returned because the system has failed to obtain the region list. Try again later. |
| yd.error.ddos.IP SEGMENT OPERA _ _ TION ERR _ | An error occurred while performing the operation on the CIDR block. | The error message returned because the system has failed to process the CIDR block. Try again later. |
| yd.error.ddos.QUERY IP SEGMENT _ _ ERR _ | An error occurred while obtaining the CIDR block. | The error message returned because the system has failed to obtain information of the CIDR block. Try again later. |

| psara Stack Security |   | Developer Guide·Error code |
|---|---|---|

| Error code | Error message | Description |
|---|---|---|
| yd.error.ddos.MODIFY IP SEGMEN _ _ T ERR _ | An error occurred while modifying the CIDR block. | The error message returned because the system has failed to modify the information of the CIDR block. Try again later. |
| yd.error.ddos.IP SEGMENT TYPE _ _ _ ERR | Check whether the type of the CIDR block (internal or external) is specified. | The error message returned because the CIDR block type is not specified. Check the CIDR block type and try again. |
| yd.error.ddos.CANCEL FLOW CLEA _ _ N ERR _ | An error occurred while canceling traffic scrubbing. Check the network connection to Beaver. | The error message returned because the system has failed to cancel traffic scrubbing. Check the network connection to Network Traffic Monitoring System and try again. |
| yd.error.ddos.QUERY FLOW ANAL _ _ YSIS ERR _ | An error occurred while obtaining the traffic analysis result. Check the network connection to Beaver. | The error message returned because the system has failed to obtain the traffic analysis result. Check the network connection to Network Traffic Monitoring System and try again. |
| yd.error.ddos.QUERY BEAVER URL _ _ ERR _ | An error occurred while obtaining the Beaver URL. | The error message returned because the system has failed to obtain the URL of Network Traffic Monitoring System. Check the network connection to Network Traffic Monitoring System and try again. |
| yd.error.ddos.SET VALVE INVALID _ _ | The specified thresholds are invalid. | The error message returned because the threshold verification has failed. Check the thresholds and try again. |
| yd.error.ddos.VALVE DEFAULT AL _ _ READY | You cannot add the default threshold again. | The error message returned because the system has failed to add the default threshold, which can only be modified. |
| yd.error.ddos.NOT BELONG BEAV _ _ ER IP SEGMENT _ _ | Check whether the specified CIDR block belongs to the internal network of Beaver. | The error message returned because the CIDR block you entered is not in the internal CIDR block of Network Traffic Monitoring System. Check the CIDR block. |

| Error code | Error message | Description |
|---|---|---|
| yd.error.ddos.VALVE DELETE ERR _ _ | Do not delete the threshold. | The error message returned because the system has failed to delete the default threshold or the threshold of 128.0.0.0/1, which cannot be deleted. |
| yd.error.ddos.QUERY CODE ERR _ _ | An error occurred while obtaining the product configuration. | The error message returned because the system has failed to obtain the dictionary. Try again later. |
| yd.error.ddos.IS OPENED _ | Enabled. | The error message returned because the specified switch has been turned on. |
| yd.error.ddos.IS CLOSED _ | Disabled. | The error message returned because the specified switch has been turned off. |

Error codes of Server Guard

| Error code | Error message | Description |
|---|---|---|
| yd.error.aqs.REQUEST FAILED _ | Request failed. Try again later. | The error message returned because the request has failed. Try again later. |

Error codes of Security Audit Error codes of Sync Center
