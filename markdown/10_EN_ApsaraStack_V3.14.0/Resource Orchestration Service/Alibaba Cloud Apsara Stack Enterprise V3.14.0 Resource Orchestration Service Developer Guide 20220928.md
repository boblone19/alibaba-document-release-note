---
title: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Resource Orchestration Service Developer Guide 20220928"
product_version: "V3.14.0"
doc_version: "20220928"
pdf_pages: 194
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Resource Orchestration Service Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.14.0/%E5%BC%B9%E6%80%A7%E8%AE%A1%E7%AE%97/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.14.0%20Resource%20Orchestration%20Service%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.14.0 Resource Orchestration Service Developer Guide 20220928

## Table of Contents

- 1 API Reference
  - 1.1 List of operations by function
  - 1.2 Make API calls
  - 1.3 Request signatures
  - 1.4 Common parameters
  - 1.5 RAM authorization
  - 1.6 Common error codes
  - 1.7 Stack operations
    - 1.7.1 CreateStack
    - 1.7.2 ContinueCreateStack
    - 1.7.3 UpdateStack
    - 1.7.4 CancelUpdateStack
    - 1.7.5 GetStack
    - 1.7.6 DeleteStack
    - 1.7.7 ListStacks
    - 1.7.8 PreviewStack
    - 1.7.9 ListStackEvents
  - 1.8 Resource operations
    - 1.8.1 GetResourceTypeTemplate
    - 1.8.2 ListStackResources
    - 1.8.3 GetStackResource
    - 1.8.4 GetResourceType
    - 1.8.5 ListResourceTypes
  - 1.9 Template operations
    - 1.9.1 GetTemplateEstimateCost
    - 1.9.2 ValidateTemplate
    - 1.9.3 GetTemplate
    - 1.9.4 DeleteTemplate
    - 1.9.5 ListTemplates
    - 1.9.6 CreateTemplate
    - 1.9.7 UpdateTemplate
    - 1.9.8 GetTemplateSummary
  - 1.10 Stack policy operations
    - 1.10.1 SetStackPolicy
    - 1.10.2 GetStackPolicy
  - 1.11 Other operations
    - 1.11.1 DescribeRegions
    - 1.11.2 SignalResource
    - 1.11.3 SetDeletionProtection
    - 1.11.4 ListStackOperationRisks
- 2 Use ASAPI to call Apsara Stack SDKs
  - 2.1 ASAPI Developer Guide
    - 2.1.1 ASAPI overview
    - 2.1.2 Preparations
      - 2.1.2.1 Log on to the API Tool console
      - 2.1.2.2 View information about API operations
      - 2.1.2.3 Generate an endpoint for the ASAPI
      - 2.1.2.4 Obtain Apsara Stack SDKs
      - 2.1.2.5 Obtain an AccessKey pair
      - 2.1.2.6 Query a region ID
    - 2.1.3 Common parameters
    - 2.1.4 SDK description
      - 2.1.4.1 Use Apsara Stack SDK for Java to call API operations
      - 2.1.4.2 Use Apsara Stack SDK for Python to call API operations
      - 2.1.4.3 Use Apsara Stack SDK for Node.js to call API operations
      - 2.1.4.4 SDK for POP
        - 2.1.4.4.1 SDK for Java
        - 2.1.4.4.2 SDK for Go
        - 2.1.4.4.3 SDK for Python
    - 2.1.5 HTTP requests
      - 2.1.5.1 Overview
      - 2.1.5.2 Request syntax
      - 2.1.5.3 Request signatures
      - 2.1.5.4 Response

## 1 API Reference

### 1.1 List of operations by function

The following tables describe the API operations available for use in Resource Orchestration Service (ROS). Stack operations

| API | Description |
|---|---|
| CreateStack | Creates a stack. |
| ContinueCreateStack | Creates a stack based on the template of the previous stack that fails to be created. |
| UpdateStack | Updates a stack. |
| CancelUpdateStack | Cancels the update of a stack. |
| GetStack | Queries information of a stack. |
| DeleteStack | Deletes a stack. |
| ListStacks | Queries the list of stacks. |
| PreviewStack | Previews the stack to be created by using a specified template. |
| ListStackEvents | Queries stacks and their resource events. |

Resource operations

| API | Description |
|---|---|
| GetResourceTypeTemplate | Queries the template of a resource by resource type. |
| ListStackResources | Queries the resource list of a specific stack. |
| GetStackResource | Queries information of a resource in a specific stack. |
| GetResourceType | Queries detailed information of a resource type. |
| ListResourceTypes | Queries the list of supported resource types. |

Template operations

| API | Description |
|---|---|
| GetTemplateEstimateCost | Queries estimated prices of resources to be created based on a template. |

| eveloper Guide·API Reference | Resource Orchestration Servic |
|---|---|

| API | Description |
|---|---|
| ValidateTemplate | Validates a template that is used to create a stack. |
| GetTemplate | Queries detailed information of a template, including stacks and change sets associated with the template. |
| DeleteTemplate | Deletes a template. |
| ListTemplates | Queries the list of templates. |
| CreateTemplate | Creates a custom template. |
| UpdateTemplate | Updates a template. |
| GetTemplateSummary | Queries information of a new or existing template. |

Stack policy operations

| API | Description |
|---|---|
| SetStackPolicy | Configures a stack policy. |
| GetStackPolicy | Queries information of a stack policy. |

Other operations

| API | Description |
|---|---|
| DescribeRegions | Queries available regions. |
| SignalResource | Sends signals. |
| SetDeletionProtection | Configures deletion protection on a stack. |
| ListStackOperationRisks | Detects the resources that may face high risks caused by a stack deletion operation, and queries the reason for each risk. |

### 1.2 Make API calls

To call the ROS API, you must send HTTP GET requests to the endpoint of the ROS API. You must add the request parameters that correspond to the API operation being called. After you call the API operation, the system returns a response. The request and response are both encoded in UTF-8. Request syntax ROS API operations use the RPC protocol. You can call ROS API operations by sending HTTP GET requests. The following example describes the request syntax of a ROS API request:

```
http://Endpoint/?Action=xx&Parameters
```

The following table describes the parameters in the request syntax.

| Parameter | Description |
|---|---|
| Endpoint | The endpoint of the ROS API. Set the value to ros.aliyuncs.com. |
| Action | The name of the operation being performed. For example, to query the list of stacks, set the value to ListStacks. |
| Parameters | The request parameters for the operation. Separate multiple parameters with ampersands (&). Request parameters include both common parameters and operation-specific parameters. Common parameters include information such as the API version number and authentication information. For more information, see Common parameters. |

Sample requests The following example demonstrates how to call the ListStacks operation to query the list of stacks: Not e The sample requests in this topic are formatted for better readability.

```
http(s)://ros.aliyuncs.com/? Action=ListStacks &RegionId=cn-hangzhou &Format=JSON &Version=2019-09-10 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=1521552885**** &SignatureVersion=1.0 &AccessKeyId=LTAI******************** &TimeStamp=2020-05-01T12:00:00Z
```

…

### 1.3 Request signatures

You must sign all API requests to ensure security. Alibaba Cloud uses the request signature to verify the identity of the API caller. Each API request must contain the signature, regardless of whether the request is sent over HTTP or HTTPS. Overview You must add the signature to the ROS API request in the following format:

```
https://Endpoint/?SignatureVersion=1.0&SignatureMethod=HMAC-SHA1&Signature=CT9X0VtwR86fNWSn sc6v8YGOjuE%3D&SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf
```

A signature contains the following parameters: SignatureMethod: the encryption method of the signature string. Set the value to HMAC-SHA1. SignatureVersion: the version of the signature encryption algorithm. Set the value to 1.0. SignatureNonce: a unique, random number used to prevent replay attacks. You must use different random numbers for different requests. We recommend that you use universally unique identifiers (UUIDs). Signature: the signature generated after the request has been symmetrically encrypted by using the AccessKey secret. The signature encryption algorithm complies with RFC 2104 HMAC-SHA1 specifications. The AccessKey secret is used to calculate the hash-based message authentication code (HMAC) value of the encoded and sorted query string, and the HMAC value is used as the signature string. Request signatures include operation-specific parameters. Therefore, the signature of a request varies based on the request parameters. To calculate a signature, follow the steps in this topic.

```
Signature = Base64( HMAC-SHA1( AccessKey Secret, UTF-8-Encoding-Of(StringToSign)) )
```

Step 1: Compose and encode a string-to-sign
1. Create a canonicalized query string by using the request parameters.
i. Create a canonicalized query string by arranging the request parameters (including all common and operation-specific parameters except Signature) in alphabetical order. Not e If you use the GET method to submit the request, these parameters are the part located after the question mark (?) and connected by the ampersands (&) in the request uniform resource identifier (URI). ii. Encode the names and values of the arranged request parameters in the request URL by using the unicode transformation format (UTF)-8 character set. The following table describes the encoding rules.

| Character | Encoding rule |
|---|---|
| Uppercase letters, lowercase letters, digits, hyphens (-), underscores ( ), periods (.), _ and tildes (~) | These characters do not need to be encoded. |
| Other characters | These characters must be percent encoded in %XY format. XY represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks (") are encoded as %22 . |
| Extended ASCII characters (UTF-8) | These characters are encoded in %XY%ZA... format. |
| Spaces | Spaces must be encoded as %20 . Do not encode spaces as plus signs (+). This encoding method is different from the application/x-ww w-form-urlencoded MIME encoding algorithm (such as the j ava.net.URLEncoder class provided by the Java standard library). However, you can apply the encoding algorithm and replace the plus sign (+) in the encoded string with %20 , the asterisk (*) with %2A , and the tilde (~) with %7E . You can use the following percentEncode method to implement this algorithm: private static final String ENCODING = "UTF-8"; private static String percentEncode(String value) throws UnsupportedEncodingException { return value ! = null ? URLEncoder.encode(value, ENCODING).replace("+", "%20").replace("*", "%2A").replace("%7E", "~") : null; } |

|   |   | w-form-urlencoded |
|---|---|---|

|   | %20 |
|---|---|
| %7E |   |

iii. Connect the encoded parameter names and their values by using equal signs (=). iv. Sort the connected parameter name and value pairs in the order specified in step i and connect the pairs by using ampersands (&) to obtain the canonicalized query string.
2. Create a string-to-sign from the encoded canonicalized query string in the following way:

```
StringToSign=
      HTTPMethod + "&" +
      percentEncode("/") + "&" +
       percentEncode(CanonicalizedQueryString)
```

A string-to-sign contains the following parameters: HTTPMethod: the HTTP method used to submit a request, such as GET. percentEncode("/"): specifies the encoded value (%2F) of a forward slash (/). The encoding follows the URL encoding rules. percentEncode(CanonicalizedQueryString): specifies the encoded canonicalized query string based on the URL encoding rules. Step 2: Calculate the signature string
1. Calculate the HMAC value of the string-to-sign based on RFC 2104.
Not e Use the SHA1 algorithm to calculate the HMAC value of the string-to-sign. The combination of your AccessKey secret and an ampersand (&) (ASCII code 38) that follows the secret is used as the key for the HMAC calculation.
2. Encode the HMAC value in Base64 to obtain the signature string.
3. Add the signature string to the request as the Signature parameter.
Not e When the obtained signature value is submitted as the final request parameter value, the value must be URL-encoded that is similar to other parameters based on rules defined in RFC 3986.

| DescribeRegions |   |   |
|---|---|---|
| n | AccessKeyID | is |

The `DescribeRegions` operation is used in this example. This example shows the signature process when `AccessKeyID` is set to testid and `AccessKeySecret` is set to testsecret:
1. Create a canonicalized query string.

```
http://ros.aliyuncs.com/?Timestamp=2019-08-23T12%3A46%3A24Z&Format=XML&AccessKeyId=test id&Action=DescribeRegions&SignatureMethod=HMAC-SHA1&SignatureNonce=3ee8c1b8-83d3-44af-a 94f-4e0ad82fd6cf&Version=2019-09-10&SignatureVersion=1.0
```

2. Create a string-to-sign.

```
GET&%2F&AccessKeyId%3Dtestid%26Action%3DDescribeRegions%26Format%3DXML%26SignatureMetho d%3DHMAC-SHA1%26SignatureNonce%3D3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf%26SignatureVersio n%3D1.0%26Timestamp%3D2019-08-23T12%253A46%253A24Z%26Version%3D2019-09-10
```

3. Calculate the signature. Because `AccessKeySecret` is set to testsecret, the key value used for
calculation is `testsecret&` . The calculated signature is `OLeaidS1JvxuMvnyHOwuJ+uX5qY=` . The Java Base64 encoding method is used in this example.

```
Signature = Base64( HMAC-SHA1( AccessSecret, UTF-8-Encoding-Of(StringToSign) ) )
```

4. Add the Signature=OLeaidS1JvxuMvnyHOwuJ%2BuX5qY%3D string that has been encoded based on
RFC 3986 to the URL in Step 1.

```
http://ros.aliyuncs.com/?SignatureVersion=1.0&Action=DescribeRegions&Format=XML&Signatu reNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf&Version=2019-09-10&AccessKeyId=testid&Sign ature=OLeaidS1JvxuMvnyHOwuJ%2BuX5qY%3D&SignatureMethod=HMAC-SHA1&Timestamp=2019-08-23T1 2%253A46%253A24Z
```

You can use browsers or tools such as cURL and Wget to initiate an HTTP request by using the new URL. The HTTP request calls the `DescribeRegions` operation to query the Alibaba Cloud region list.

### 1.4 Common parameters

This topic describes the common request and response parameters. Common request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Format | String | No | The format in which to return the response. Default value: JSON. Valid values: JSON XML |
| Version | String | Yes | The API version of the service. Specify the version number in the YYYY-MM-DD format. Set the value to 2019- 09-10. |
| AccessKeyId | String | Yes | The AccessKey ID used to connect to the service. The AccessKey ID is provided by Alibaba Cloud for authentication. |
| Signature | String | Yes | The signature string of the request. For more information about how signatures are calculated, see Request signatures. |
| SignatureMethod | String | Yes | The encryption method of the signature string. Set the value to HMAC- SHA1. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the YYYY- MM-DDThh:mm:ssZ format. The time must be in UTC. Example: 2020-01- 10T12:00:00Z. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Set the value to 1.0. |
| SignatureNonce | String | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |

Sample requests

```
http(s)://ros.aliyuncs.com/? Action=XXXXXX &Format=xml &Version=2019-09-10 &Signature=Pc5WB8gokVn0xfeu%2FZV%2BiNM1dgI%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=1521552885**** &SignatureVersion=1.0 &AccessKeyId=LTAI******************** &TimeStamp=2020-05-01T12:00:00Z
```

Common response parameters Responses can be returned in the JSON or XML format. You can specify the response format in the request. The default response format is JSON. Every response returns a unique RequestId value regardless of whether the call is successful. A `2xx` HTTP status code indicates a successful call. A `4xx` or `5xx` HTTP status code indicates a failed call. Sample responses XML format

```xml
<? xml version="1.0" encoding="utf-8"? >
    <!—Result Root Node-->
    <Interface Name+Response>
        <!—Return Request Tag-->
        <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
        <!—Return Result Data-->
    </Interface Name+Response>
```

JSON format `{`

```json
    "RequestId":"4C467B38-3910-447D-87BC-AC049166F216"
    /*Return Result Data*/
```

`}`

### 1.5 RAM authorization

Before you use a RAM user account to call an Alibaba Cloud API, you must use an Alibaba Cloud account to create an authorization policy to assign permissions to the RAM user account. Resource authorization By default, a RAM user account is not authorized to call Alibaba Cloud APIs to create or modify cloud resources. Before you use a RAM user to call an API, you must grant the RAM user account the permission to call the API by creating an authorization policy and attaching the policy to the RAM user account. When you create the authorization policy, you can specify the resource to authorize by its Alibaba Resource Name (ARN). An ARN is used to identify the resource to authorize. ARNs are in the following format:

```
acs:service-name:region:account-id:resource-relative-id
```

An ARN contains the following parameters: acs: the abbreviation for Alibaba Cloud Service. service-name: the name of an Alibaba Cloud service, such as ECS, OSS, and ROS. region: the region where the service resides. If this option is not supported, use the asterisk ( `*` ) instead. account-id: the ID of the user account, such as 123456789012****. resource-relative-id: the specific description of a resource. The description varies based on service. For more information, see the documentation of each service.

| acs:oss:123456789012****:sample bucket/file1.txt _ |   | indicates |
|---|---|---|
| /file1.txt in Object Storage Service (OSS) and | 123456789012**** |   |

the user to which the resource belongs. Types of ROS resources that can be authorized

| Resource type | ARN format in the authorization policy |
|---|---|
| Stack | acs:ros:$regionid:$accountid:stack/$stackid |
|   | acs:ros:$regionid:$accountid:stack/* |
| Template | acs:ros:$regionid:$accountid:template/$templateid |
|   | acs:ros:$regionid:$accountid:template/* |
| StackGroup | acs:ros:$regionid:$accountid:stack group/* _ |

ROS API operations that can be authorized The following table lists ROS API operations that can be authorized and their corresponding ARN formats.

| Operation | ARN |
|---|---|
| CreateStack | acs:ros:$regionid:$accountid:stack/* |
| UpdateStack | acs:ros:$regionid:$accountid:stack/$stackid |
| DeleteStack | acs:ros:$regionid:$accountid:stack/$stackid |
| GetStack | acs:ros:$regionid:$accountid:stack/$stackid |
| ListStacks | acs:ros:$regionid:$accountid:stack/* |
| PreviewStack | acs:ros:$regionid:$accountid:stack/* |
| GetTemplateEstimat eCost | acs:ros:$regionid:$accountid:* |
| CancelUpdateStack | acs:ros:$regionid:$accountid:stack/$stackid |
| ContinueCreateStack | acs:ros:$regionid:$accountid:stack/$stackid |
| SetStackPolicy | acs:ros:$regionid:$accountid:stack/$stackid |
| GetStackPolicy | acs:ros:$regionid:$accountid:stack/$stackid |
| GetTemplate | acs:ros:$regionid:$accountid:stack/$stackid |
|   | acs:ros:$regionid:$accountid:template/$templateid |
| CreateChangeSet | When ChangeSetType is set to CREATE: acs:ros:$regionid:$accountid:stack/* |
|   | When ChangeSetType is set to UPDATE: acs:ros:$regionid:$accountid:stack/$stackid |
| GetChangeSet | acs:ros:$regionid:$accountid:stack/$stackid |
| ListChangeSets | acs:ros:$regionid:$accountid:stack/$stackid |
| ExecuteChangeSet | acs:ros:$regionid:$accountid:stack/$stackid |
| DeleteChangeSet | acs:ros:$regionid:$accountid:stack/$stackid |
| ListStackEvents | acs:ros:$regionid:$accountid:stack/$stackid |
| ListStackResources | acs:ros:$regionid:$accountid:stack/$stackid |
| GetStackResource | acs:ros:$regionid:$accountid:stack/$stackid |
| SignalResource | acs:ros:$regionid:$accountid:stack/$stackid |
| DetectStackDrift | acs:ros:$regionid:$accountid:stack/$stackid |
| DetectStackResource Drift | acs:ros:$regionid:$accountid:stack/$stackid |

| esource Orchestration S | ervice Developer Guide·API Referenc |
|---|---|

| Operation | ARN |
|---|---|
| GetStackDriftDetecti onStatus | acs:ros:$regionid:$accountid:stack/$stackid |
| ListStackResourceDrif ts | acs:ros:$regionid:$accountid:stack/$stackid |
| DetectStackGroupDrif t | acs:ros:$regionid:$accountid:stack group/* _ |
| UpdateStackTemplat eByResources | acs:ros:$regionid:$accountid:stack/$stackid |

### 1.6 Common error codes

This topic describes the common client and server error codes. Client error codes

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| UnknownError | The request processing has failed due to some unknown error. | 400 | The error message returned because an unknown error that is not caused by a server-side issue has occurred on the client. |
| MissingParameter | The input parameter {name} should be specified. | 400 | The error message returned because the input parameter is missing. name indicates the parameter name. |
|   | One of the input parameters {names} should be specified. | 400 | The error message returned because the input parameter is missing. You must specify one of the input parameters. names indicates the names of all the related parameters. |
|   | The input parameter {name} should be specified, {reason}. | 400 | The error message returned because the input parameter is missing. name indicates the parameter name, and reason indicates the specific reason. |
|   | The specified parameter {name} is invalid. | 400 | The error message returned because the specified parameter is invalid. name indicates the parameter name. |

| eveloper Guide·API Ref |   |   |   |
|---|---|---|---|
|   | erence Resource Orchestration Servic |   |   |
| InvalidParameter Error code | Error message | HTTP status code | Description |
|   | The specified parameter {name} is invalid, {reason}. | 400 | The error message returned because the specified parameter is invalid. name indicates the parameter name, and reason indicates the specific reason. |
| MultipleParameter | Only one of the input parameters {names} can be specified. | 400 | The error message returned because the number of specified parameters exceeds the limit. You can specify only one of the parameters. names indicates the names of all the related parameters. |
| InvalidIdempotenceP arameter | The specified parameters are different from before. | 400 | The error message returned because the idempotent token is the same, but the specified parameters are different from before. |
| LastTokenProcessin g | The last token request is processing. | 400 | The error message returned because the previous token request is being processed. Try again later. |
| Invalid | Data supplied was not valid: {reason}. | 400 | The error message returned because the value is invalid. reason indicates the specific reason. |
| InvalidValue | {reason}. | 400 | The error message returned because the value is invalid. reason indicates the specific reason. |
| RequestLimitExceed ed | Request limit exceeded: {reason}. | 400 | The error message returned because the request contains content that exceeds the limit. reason indicates the specific reason. You can change the part of content that exceeds the limit by adjusting the quota. |
| NotSupported | {feature} is not supported. | 400 | The error message returned because a specified feature is not supported. feature indicates the specific feature or operation. |

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| MismatchNextToken | {name} mismatches next token. | 400 | The error message returned because the specified parameter does not match the next token. name indicates the parameter name. |
| AssumeRoleFailure | Fail to assume role {name}: {reason} | 400 | The error message returned because ROS has failed to obtain a temporary identity to assume the specified RAM role. name indicates the RAM role name, and reason indicates the specific reason for the failure. |
| Forbidden | You are not authorized to complete this action. | 403 | The error message returned because you are not authorized to complete this action. |
|   | A required authorization for the specified action {api} is not supplied. Code: {code} RequestId: {request id} _ | 403 | The error message returned because you have not authorized ROS to call the operation. api indicates the name of the operation. code indicates the error code. request id indicates the ID of _ the request. |
| AccountTypeNotSup ported | Account type not supported. | 403 | The error message returned because the specified account type is not supported. |
| NotFound | {reason}. | 404 | The error message returned because the request contains content that does not exist. reason indicates the specific reason. |

Server error codes

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| InternalError | Server error. | 500 | The error message returned because an internal error has occurred. |

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| ServiceUnavailable | The request has failed due to a temporary failure of the server. | 503 | The error message returned because a server error has occurred. Try again later. If the problem persists, submit a ticket. |

### 1.7 Stack operations

#### 1.7.1 CreateStack

You can call this operation to create a stack. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateStack | The operation that you want to perform. Set the value to CreateStack. |
| Parameters.N.Par ameterKey | String | Yes | InstanceId | The key of parameter N. If the key and value of the parameter are not specified, the key and value in the template are used. Maximum value of N: 200. Not e Parameters is an optional parameter. If you need to specify Parameters, you must specify both Parameters.N.ParameterKe y and Parameters.N.ParameterVa lue. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Parameters.N.Par ameterValue | String | Yes | i-xxxxxx | The value of parameter N. Maximum value of N: 200. Not e Parameters is an optional parameter. If you need to specify Parameters, you must specify both Parameters.N.ParameterKe y and Parameters.N.ParameterVa lue. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackName | String | Yes | MyStack | The name of the stack. The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores ( ). It must start with a digit or letter. _ |
| DisableRollback | Boolean | No | false | Specifies whether to disable rollback on stack creation failure. Default value: false. Valid values: true: disables rollback on stack creation failure. false: enables rollback on stack creation failure. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TemplateBody | String | No | { "ROSTemplateFor matVersion": "2015-09-01" } | The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body is longer than required, we recommend that you add parameters to the HTTP POST request body to avoid request failures due to excessive length of URLs. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |
| StackPolicyURL | String | No | oss://ros-stack- policy/demo | The URL of the file that contains the stack policy. The URL must point to a policy located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/stack- policy/demo and oss://ros/stack- policy/demo?RegionId=cn-hangzhou. The policy can be up to 16,384 bytes in length and the URL can be up to 1,350 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Not e You must specify one of the StackPolicyBody and StackPolicyURL parameters, but you cannot specify both of them. |
| TimeoutInMinutes | Long | No | 10 | The timeout period that is specified for the stack creation request. Default value: 60. Unit: minutes. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| StackPolicyBody | String | No | {"Statement": [{"Action": "Update:*", "Resource": "*", "Effect": "Allow", "Principal": "*"}]} | The structure that contains the stack policy body. The stack policy body must be 1 to 16,384 bytes in length. Not e You must specify one of the StackPolicyBody and StackPolicyURL parameters, but you cannot specify both of them. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 42665544**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can be up to 64 characters in length and can contain letters, digits, hyphens (-), and underscores ( ). _ |
| TemplateURL | String | No | oss://ros- template/demo | The URL of the file that contains the template body. The URL must point to a template located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/template/demo and oss://ros/template/demo? RegionId=cn-hangzhou. The template must be 1 to 524,288 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| NotificationURLs. N | RepeatLi st | No | http://my- site.com/ros- event | The callback URL for receiving stack event N. Only HTTP POST is supported. Maximum value of N: 5. Each URL can be up to 1,024 bytes in length. ROS sends a notification to the specified URL when the stack state changes. If rollback is enabled on the stack, notifications are sent if the stack is in the CREATE ROLLBACK or ROLLBACK _ state, but are not sent when the stack is in the CREATE FAILED or _ UPDATE FAILED state. _ Not e ROS does not send notifications when the stack is in the IN PROGRESS state. _ Notifications are sent regardless of whether the Outputs parameter is specified. The following code is an example of a notification: { "Outputs": [ { "Description": "No description given", "OutputKey": "InstanceId", "OutputValue": "i-xxx" } ], "StackId": "80bd6b6c- e888-4573-ae3b-93d29113****", "StackName": "test- notification-url", "Status": "CREATE COMPLETE" _ } |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RamRoleName | String | No | test-role | The name of the RAM role. ROS assumes the specified RAM role to create the stack and call API operations by using the credentials of the role. All operations are performed under this role. If a RAM user is authorized to perform operations on the stack but does not have the permission to use the role, ROS still uses the role and grants the role the least privilege. If you do not specify this parameter, ROS uses the role previously associated with the stack. If no roles are available, ROS uses the temporary credentials generated from the credentials of your account. The RAM role name can be up to 64 characters in length. |
| DeletionProtectio n | String | No | Enabled | Specifies whether to enable deletion protection on the stack. Default value: Disabled. Valid values: Enabled: enables deletion protection on the stack. Disabled: disables deletion protection on the stack. You can release the stack by using the ROS console or by calling the DeleteStack operation. Not e The deletion protection property of a nested stack is the same as that of its root stack. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| CreateOption | String | No | KeepStackOnCrea tionComplete | Specifies whether to delete the stack after it is created. Default value: KeepStackOnCreationComplete. Valid values: KeepStackOnCreationComplete: retains the stack and all its resources after the stack is created. AbandonStackOnCreationComplete: deletes the stack but retains all its resources after the stack is created. This helps you ensure that the maximum number of stacks allowed to be created is not reached. If the stack fails to be created, the stack is retained. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| StackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | The ID of the request. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=CreateStack &RegionId=cn-hangzhou &StackName=MyStack &Parameters.1.ParameterKey=InstanceId &Parameters.1.ParameterValue=i-xxxxxx &TimeoutInMinutes=10 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateStackResponse>
          <StackId>4a6c9851-3b0f-4f5f-b4ca-a14bf691****</StackId>
          <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
</CreateStackResponse>
```

`JSON` format `{`

```json
    "StackId": "4a6c9851-3b0f-4f5f-b4ca-a14bf691****",
    "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F"
```

`}`

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| CircularDependency | Circular Dependency Found: {reason}. | 400 | The error message returned because the template contains a circular reference. reason indicates the specific reason. |
| InvalidSchema | {reason}. | 400 | The error message returned because the specified template format is incorrect. reason indicates the specific reason. |
| InvalidTemplateAttribut e | The Referenced Attribute ({resource} {name}) is incorrect. | 400 | The error message returned because the resource attribute referenced in the template is incorrect. resource indicates the resource name, and name indicates the attribute name. |
| InvalidTemplatePropert yType | The specified value type of ({resource} {section}) is incorrect. | 400 | The error message returned because the type of the specified resource section defined in the template is invalid. resource indicates the resource name, and section indicates the section name. |

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| InvalidTemplateReferen ce | The specified reference "{name}" (in {referencer}) is incorrect. | 400 | The error message returned because the template contains an invalid reference. name indicates the reference name, and referencer indicates the referencer name. |
| InvalidTemplateSection | The template section is invalid: {section}. | 400 | The error message returned because the template contains an invalid section. section indicates the section name. |
| InvalidTemplateVersion | The template version is invalid: {reason}. | 400 | The error message returned because the template version is incorrect. reason indicates the specific reason. |
| StackValidationFailed | {reason}. | 400 | The error message returned because the stack validation failed. reason indicates the specific reason. |
| UnknownUserParameter | The Parameter ({name}) was not defined in template. | 400 | The error message returned because the specified parameter is not defined in the template. name indicates the parameter key. |
| UserParameterMissing | The Parameter {name} was not provided. | 400 | The error message returned because no value is passed into the specified parameter defined in the template. name indicates the parameter key. |

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| ActionInProgress | Stack {name} already has an action ({action}) in progress. | 409 | The error message returned because the specified stack has a change operation in progress. name indicates the name or ID of the stack, and action indicates the change operation. |
| StackExists | The Stack ({name}) already exists. | 409 | The error message returned because a stack with the same name already exists. name indicates the stack name. |

#### 1.7.2 ContinueCreateStack

Creates a stack based on the template of the previous stack that fails to be created. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ContinueCreateSt ack | The operation that you want to perform. Set the value to ContinueCreateStack. |
| Parameters.N.Par ameterKey | String | Yes | Amount | The key of template parameter N to be overridden. If the key and value of the parameter are not specified, the key and value are set to those in the template of the stack that fails to be created. Maximum value of N: 200. Not e This parameter takes effect only when the Mode parameter is set to Recreate. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Parameters.N.Par ameterValue | String | Yes | 12 | The value of template parameter N to be overridden. Maximum value of N: 200. This parameter takes effect only when the Mode parameter is set to Recreate. Take note of the following limits on the template parameter to be overridden: This parameter cannot change values in the Conditions section of the template from true to false or from false to true. This parameter can be referenced only by resources that are recreated. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| RecreatingResour ces.N | RepeatLi st | No | WebServer | The resource N to be recreated upon creation failure. ROS recreates the resources you list in this parameter and all resources that depend on the resources. |
| RamRoleName | String | No | test-role | The name of the Resource Access Management (RAM) role. Resource Orchestration Service (ROS) assumes the specified RAM role to create the stack and call API operations by using the credentials of the role. All operations are performed under this role. If a RAM user is authorized to perform operations on the stack but does not have the permissions to use the role, ROS still uses the role and grants the role the least privilege. If you do not specify this parameter, ROS uses the role previously associated with the stack. If no roles are available, ROS uses the temporary credentials generated from the credentials of your account. The RAM role name can be up to 64 characters in length. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Mode | String | No | Recreate | The stack recreation mode. Default value: Recreate. Valid values: Recreate Only the following types of resources are recreated: Resources that fail to be created Resources specified in the RecreatingResources.N parameter Resources that depend on the resources specified in the RecreatingResources.N parameter Resources for which creation operations are not initiated The RecreatingResources.N, TemplateBody, TemplateURL, and Parameters parameters take effect only when the Mode parameter is set to Recreate. Ignore: ROS ignores and discards all resources that fail to be recreated and the resources for which creation operations are not initiated. Then, the stack creation operation is marked as successful. Content of the template is changed. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TemplateBody | String | No | { "ROSTemplateFor matVersion": "2015-09-01" } | The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body is longer than required, we recommend that you add parameters to the HTTP POST request body to avoid request failures due to excessive length of URLs. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. This parameter takes effect only when the Mode parameter is set to Recreate. Take note of the following limits on the template: Only the Description, Metadata, Resources, and Outputs sections in the template can be modified. No sections can be added to or removed from the outermost layer of the template. Take note of the following limits on the Resources section of the template: The resources not to be recreated cannot be deleted, and their template content cannot be modified. The resources to be recreated can be deleted, and their template content can be modified. New resources can be added. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TemplateURL | String | No | oss://ros- template/demo | The URL of the file that contains the template body. The URL must point to a template located in an HTTP or HTTPS web server or an Object Storage Service (OSS) bucket. Examples: oss://ros/template/demo and oss://ros/template/demo? RegionId=cn-hangzhou.The template can be up to 524,288 bytes in length. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. This parameter takes effect only when the Mode parameter is set to Recreate. For information about the limits on the template specified in this parameter, see the description of the TemplateBody parameter. |
| DryRun | Boolean | No | false | Specifies whether to check the validity of the request without actually making the request. Default value: false. Valid values: true: checks the validity of the request without actually making the request. false: makes the request to recreate the stack. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | The ID of the request. |
| StackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/?Action=ContinueCreateStack &RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ContinueCreateStackResponse>
       <RequestId type="string">B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
       <StackId type="string">0a7c379a-566f-4bc0-b3fb-a301df51****</StackId>
</ContinueCreateStackResponse>
```

`JSON` format `{`

```json
   "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F",
   "StackId": "0a7c379a-566f-4bc0-b3fb-a301df51****"
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | CircularDependency | Circular Dependency Found: {reason}. | The error message returned because the template contains a circular reference. reason indicates the specific reason. |
| 400 | InvalidSchema | {reason}. | The error message returned because the specified template format is invalid. reason indicates the specific reason. |
| 400 | InvalidTemplateAttribut e | The Referenced Attribute ({resource} {name}) is incorrect. | The error message returned because the resource attribute referenced in the template is invalid. resource indicates the resource name, and name indicates the attribute name. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidTemplatePropert yType | The specified value type of ({resource} {section}) is incorrect. | The error message returned because the type of the specified resource section defined in the template is invalid. resource indicates the resource name, and section indicates the section name. |
| 400 | InvalidTemplateReferen ce | The specified reference "{name}" (in {referencer}) is incorrect. | The error message returned because the template contains an invalid reference. name indicates the reference name, and referencer indicates the referencer name. |
| 400 | InvalidTemplateSection | The template section is invalid: {section}. | The error message returned because the template contains an invalid section. section indicates the section name. |
| 400 | InvalidTemplateVersion | The template version is invalid: {reason}. | The error message returned because the template version is invalid. reason indicates the specific reason. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | StackValidationFailed | {reason}. | The error message returned because the stack validation failed. reason indicates the specific reason. |
| 400 | UnknownUserParameter | The Parameter ({name}) was not defined in template. | The error message returned because the specified parameter is not defined in the template. name indicates the parameter key. |
| 400 | UserParameterMissing | The Parameter {name} was not provided. | The error message returned because no value is passed into the specified parameter defined in the template. name indicates the parameter key. |
| 400 | ContinueCreateStackVali dationFailed | {reason}. | The error message returned because the stack validation failed. reason indicates the specific reason. |
| 404 | ResourceNotFound | The Resource ({name}) could not be found in Stack {stack}. | The error message returned because the specified resource does not exist in the specified stack. name indicates the resource name, and stack indicates the stack name or ID. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the stack does not exist. name indicates the name or ID of the stack. |
| 409 | ActionInProgress | Stack {name} already has an action ({action}) in progress. | The error message returned because the specified stack has a change operation in progress. name indicates the name or ID of the stack, and action indicates the change operation. |

#### 1.7.3 UpdateStack

You can call this operation to update a stack. The values of Parameters and UsePreviousParameters in the request are related. If parameters defined in the template are not specified by Parameters, take note of the following items: When UsePreviousParameters is set to false, if the parameter has a default value in the template, the default value is used. If the parameter does not have a default value in the template, you must specify the parameter in the Parameters section. When UsePreviousParameters is set to true, if the parameter is specified when the stack is created, the specified value is used. If the parameter is not specified and it has a default value in the template, the default value is used. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateStack | The operation that you want to perform. Set the value to UpdateStack. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Parameters.N.Par ameterKey | String | Yes | Amount | The key of parameter N. If the key and value of the parameter are not specified, the key and value in the template are used. Maximum value of N: 200. Not e Parameters is an optional parameter. If you need to specify Parameters, you must specify both Parameters.N.ParameterKe y and Parameters.N.ParameterVa lue. |
| Parameters.N.Par ameterValue | String | Yes | 12 | The value of parameter N. Maximum value of N: 200. Not e Parameters is an optional parameter. If you need to specify Parameters, you must specify both Parameters.N.ParameterKe y and Parameters.N.ParameterVa lue. |
| RegionId | String | Yes | cn-beijing | The region ID of the stack. |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 42665544**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can be up to 64 characters in length and can contain letters, digits, hyphens (-), and underscores ( ). _ |
| StackPolicyDuring UpdateBody | String | No | {"Statement": [{"Effect": "Allow", "Action": "Update:*", "Principal": "*", "Resource": "*"}]} | The structure that contains the body of the temporary overriding stack policy. The stack policy body must be 1 to 16,384 bytes in length. To update protected resources, specify a temporary overriding stack policy during the update. If you do not specify a stack policy, the current policy that is associated with the stack is used. This parameter takes effect only when the ChangeSetType parameter is set to UPDATE. You can specify only one of the following parameters: StackPolicyBody StackPolicyURL StackPolicyDuringUpdateBody StackPolicyDuringUpdateURL |
| TimeoutInMinutes | Long | No | 10 | The timeout period that is specified for the stack update request. Default value: 60. Unit: minutes. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TemplateBody | String | No | {"ROSTemplateFo rmatVersion": "2015-09-01"} | The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body is longer than required, we recommend that you add parameters to the HTTP POST request body to avoid request failures due to excessive length of URLs. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |
| StackPolicyURL | String | No | oss://ros-stack- policy/demo | The URL of the file that contains the stack policy. The URL must point to a policy located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/stack- policy/demo and oss://ros/stack- policy/demo?RegionId=cn-hangzhou. The policy can be up to 16,384 bytes in length and the URL can be up to 1,350 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Not e You must specify one of the StackPolicyBody and StackPolicyURL parameters, but you cannot specify both of them. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| StackPolicyDuring UpdateURL | String | No | oss://ros-stack- policy/demo | The URL of the file that contains the temporary overriding stack policy. The URL must point to a policy located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/stack-policy/demo and oss://ros/stack-policy/demo? RegionId=cn-hangzhou. The policy can be up to 16,384 bytes in length and the URL can be up to 1,350 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Not e You must specify one of the StackPolicyBody and StackPolicyURL parameters, but you cannot specify both of them. To update protected resources, specify a temporary overriding stack policy during the update. If you do not specify a stack policy, the current policy that is associated with the stack is used. This parameter takes effect only when the ChangeSetType parameter is set to UPDATE. You can specify only one of the following parameters: StackPolicyBody StackPolicyURL StackPolicyDuringUpdateBody StackPolicyDuringUpdateURL |
| StackPolicyBody | String | No | {"Statement": [{"Action": "Update:*", "Resource": "*", "Effect": "Allow", "Principal": "*"}]} | The structure that contains the stack policy body. The stack policy body must be 1 to 16,384 bytes in length. Not e You must specify one of the StackPolicyBody and StackPolicyURL parameters, but you cannot specify both of them. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| UsePreviousPara meters | Boolean | No | true | Specifies whether to use the values that were passed last time for the parameters that you do not specify in the current request. Valid values: true false |
| DisableRollback | Boolean | No | false | This parameter cannot take effect when the stack is being updated. If the update fails, a rollback is performed regardless of the value of this parameter. |
| TemplateURL | String | No | oss://ros- template/demo | The URL of the file that contains the template body. The URL must point to a template located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/template/demo and oss://ros/template/demo? RegionId=cn-hangzhou. The template must be 1 to 524,288 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RamRoleName | String | No | test-role | The name of the RAM role. ROS assumes the specified RAM role to create the stack and call API operations by using the credentials of the role. All operations are performed under this role. If a RAM user is authorized to perform operations on the stack but does not have the permission to use the role, ROS still uses the role and grants the role the least privilege. If you do not specify this parameter, ROS uses the role previously associated with the stack. If no roles are available, ROS uses the temporary credentials generated from the credentials of your account. The RAM role name can be up to 64 characters in length. |
| ReplacementOpti on | String | No | Disabled | Specifies whether to enable replacement update after a resource attribute that does not support modification update is changed. Modification update keeps the physical ID of the resource unchanged. However, the resource is deleted and then recreated, and its physical ID is changed if replacement update is enabled. Default value: Disabled. Valid values: Enable: enables replacement update. Disabled: disables replacement update. Not e Modification update takes precedence over replacement update. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| StackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |

| R | esource Orchestra | tion Service |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | The ID of the request. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=UpdateStack &RegionId=cn-beijing &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &Parameters.1.ParameterKey=Amount &Parameters.1.ParameterValue=12 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UpdateStackResponse>
      <StackId>4a6c9851-3b0f-4f5f-b4ca-a14bf691****</StackId>
      <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
</UpdateStackResponse>
```

`JSON` format `{`

```json
    "StackId": "4a6c9851-3b0f-4f5f-b4ca-a14bf691****",
    "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F"
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | CircularDependency | Circular Dependency Found: {reason}. | The error message returned because the template contains a circular dependency. reason indicates the specific reason. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidSchema | {reason}. | The error message returned because the specified template format is incorrect. reason indicates the specific reason. |
| 400 | InvalidTemplateAttribut e | The Referenced Attribute ({resource} {name}) is incorrect. | The error message returned because the resource attribute referenced in the template is incorrect. resource indicates the resource name, and name indicates the attribute name. |
| 400 | InvalidTemplatePropert yType | The specified value type of ({resource} {section}) is incorrect. | The error message returned because the type of the specified resource section defined in the template is incorrect. resource indicates the resource name, and section indicates the section name. |
| 400 | InvalidTemplateReferen ce | The specified reference "{name}" (in {referencer}) is incorrect. | The error message returned because the template contains an invalid reference. name indicates the reference name, and referencer indicates the referencer name. |
| 400 | InvalidTemplateSection | The template section is invalid: {section}. | The error message returned because the template contains an invalid section. section indicates the section name. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidTemplateVersion | The template version is invalid: {reason}. | The error message returned because the template version is incorrect. reason indicates the specific reason. |
| 400 | StackPolicyValidationFai led | Action denied by stack policy: {reason}. | The error message returned because the stack policy validation failed. reason indicates the specific reason. |
| 400 | StackValidationFailed | {reason}. | The error message returned because the stack validation failed. reason indicates the specific reason. |
| 400 | UnknownUserParameter | The Parameter ({name}) was not defined in template. | The error message returned because the specified parameter is not defined in the template. name indicates the parameter key. |
| 400 | UserParameterMissing | The Parameter {name} was not provided. | The error message returned because no value is passed into the specified parameter defined in the template. name indicates the parameter key. |
| 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the specified stack does not exist. name indicates the name or ID of the stack. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 409 | ActionInProgress | Stack {name} already has an action ({action}) in progress. | The error message returned because the specified stack has a change operation in progress. name indicates the name or ID of the stack, and action indicates the change operation. |

#### 1.7.4 CancelUpdateStack

Cancels the update of a stack. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CancelUpdateSta ck | The operation that you want to perform. Set the value to CancelUpdateStack. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| CancelType | String | No | Safe | The method to cancel the update operation. Valid values: Quick: cancels the update of a stack as soon as possible. Safe: cancels the update of a stack as safely as possible. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | The ID of the request. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/?Action=CancelUpdateStack &RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CancelUpdateStackResponse>
         <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
         <StackId>4a6c9851-3b0f-4f5f-b4ca-a14bf691****</StackId>
</CancelUpdateStackResponse>
```

`JSON` format `{`

```json
   "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F",
   "StackId": "4a6c9851-3b0f-4f5f-b4ca-a14bf691****"
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the stack does not exist. name indicates the name or ID of the stack. |
| 409 | ActionInProgress | Stack {name} already has an action ({action}) in progress. | The error message returned because the specified stack has a change operation in progress. name indicates the name or ID of the stack, and action indicates the change operation. |

#### 1.7.5 GetStack

You can call this operation to query information about a stack. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetStack | The operation that you want to perform. Set the value to GetStack. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 42665544**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can be up to 64 characters in length and can contain letters, digits, hyphens (-), and underscores ( ). _ |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CreateTime | String | 2019-08- 01T04:07:39 | The time when the stack was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC. |
| Description | String | my stack description | The description of the stack. |
| DisableRollback | Boolean | false | Indicates whether rollback is disabled on stack creation failure. Default value: false. Valid values: true: The rollback on stack creation failure is disabled. false: The rollback on stack creation failure is enabled. |
| NotificationURL s | List | ["http://127.XX.XX. 1:8080/x", "http://127.0.XX.XX :8080/y"] | The callback URLs for receiving stack events. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Outputs | List | [{"Description": "Instance ID","OutputKey": "InstanceId","Output Value": "i-a****"}] | The output parameters of the stack. |
| Parameters | Array of Parameter |   | The list of input parameters of the stack. |
| ParameterKey | String | InstanceType | The key of the parameter. |
| ParameterValu e | String | ecs.cm4.6xlarge | The value of the parameter. |
| ParentStackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf692**** | The ID of the parent stack. |
| RegionId | String | cn-beijing | The region ID of the stack. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | String | CREATE COMPLETE _ | The state of the stack. Valid values: CREATE IN PROGRESS _ _ CREATE FAILED _ CREATE COMPLETE _ UPDATE IN PROGRESS _ _ UPDATE FAILED _ UPDATE COMPLETE _ DELETE IN PROGRESS _ _ DELETE FAILED _ DELETE COMPLETE _ CREATE ROLLBACK IN PROGRESS _ _ _ CREATE ROLLBACK FAILED _ _ CREATE ROLLBACK COMPLETE _ _ ROLLBACK IN PROGRESS _ _ ROLLBACK FAILED _ ROLLBACK COMPLETE _ CHECK IN PROGRESS _ _ CHECK FAILED _ CHECK COMPLETE _ REVIEW IN PROGRESS _ _ IMPORT CREATE IN PROGRESS _ _ _ IMPORT CREATE FAILED _ _ IMPORT CREATE COMPLETE _ _ IMPORT CREATE ROLLBACK IN PROGRESS _ _ _ _ IMPORT CREATE ROLLBACK FAILED _ _ _ IMPORT CREATE ROLLBACK COMPLETE _ _ _ IMPORT UPDATE IN PROGRESS _ _ _ IMPORT UPDATE FAILED _ _ IMPORT UPDATE COMPLETE _ _ IMPORT UPDATE ROLLBACK IN PROGRESS _ _ _ _ IMPORT UPDATE ROLLBACK FAILED _ _ _ IMPORT UPDATE ROLLBACK COMPLETE _ _ _ |
| StackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| StackName | String | MyStack | The name of the stack. The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores ( ). It must _ start with a digit or letter. |
| UpdateTime | String | 2019-08- 01T04:07:39 | The time when the stack was last updated. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC. |
| StatusReason | String | Stack successfully created | The reason why the stack is in its current state. |
| TemplateDescri ption | String | Some description | The description of the stack. |
| TimeoutInMinut es | Integer | 10 | The timeout period that is specified for the stack creation request. Unit: minutes. |
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | The ID of the request. |
| DeletionProtect ion | String | Enabled | Indicates whether deletion protection is enabled on the stack. Valid values: Enabled: Deletion protection is enabled on the stack. Disabled: Deletion protection is disabled on the stack. You can release the stack by using the ROS console or by calling the DeleteStack operation. Not e The deletion protection property of a nested stack is the same as that of its root stack. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DriftDetectionTi me | String | 2020-02- 27T07:47:47 | The time when the last successful drift detection operation was initiated. |
| RamRoleName | String | test-role | The name of the RAM role. ROS assumes the specified RAM role to create the stack and call API operations by using the credentials of the role. All operations are performed under this role. If a RAM user is authorized to perform operations on the stack but does not have the permission to use the role, ROS still uses the role and grants the role the least privilege. If you do not specify this parameter, ROS uses the role previously associated with the stack. If no roles are available, ROS uses the temporary credentials generated from the credentials of your account. The RAM role name can be up to 64 characters in length. |
| RootStackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf692**** | The ID of the root stack. This parameter is returned if the specified stack is a nested stack. |
| StackDriftStatu s | String | IN SYNC _ | The drift state of the stack in the last successful drift detection. Valid values: DRIFTED: The stack has drifted. NOT CHECKED: No drift detection has _ been successful on the stack group. IN SYNC: The stack is being synchronized. _ |
| StackType | String | ROS | The type of the stack. Valid values: ROS: The stack was created based on an ROS template. Terraform: The stack was created based on a Terraform template. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=GetStack &RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<GetStackResponse>
          <CreationTime>2019-08-01T04:07:39</CreationTime>
          <Description>No description</Description>
          <DisableRollback>false</DisableRollback>
          <NotificationURLs>http://127.0.XX.XX:8080/x</NotificationURLs>
          <NotificationURLs>http://127.0.XX.XX:8080/y</NotificationURLs>
          <Outputs>
                <Description>Instance ID</Description>
                <OutputKey>InstanceId</OutputKey>
                <OutputValue>i-a****</OutputValue>
          </Outputs>
          <Parameters>
                <ParameterKey>InstanceType</ParameterKey>
                <ParameterValue>ecs.cm4.6xlarge</ParameterValue>
          </Parameters>
          <RegionId>cn-hangzhou</RegionId>
          <StackId>4a6c9851-3b0f-4f5f-b4ca-a14bf691****</StackId>
          <StackName>MyStack</StackName>
          <Status>CREATE_COMPLETE</Status>
          <StatusReason>Stack successfully created</StatusReason>
          <TemplateDescription>Some description</TemplateDescription>
          <TimeoutInMinutes>10</TimeoutInMinutes>
          <UpdatedTime>2019-08-01T04:07:39</UpdatedTime>
          <ParentStackId>4a6c9851-3b0f-4f5f-b4ca-a14bf692****</ParentStackId>
          <DriftDetectionTime>2020-02-27T07:47:47</DriftDetectionTime>
          <StackDriftStatus>IN_SYNC</StackDriftStatus>
          <RamRoleName>test-role</RamRoleName>
          <DeletionProtection>Enabled</DeletionProtection>
          <RootStackId>4a6c9851-3b0f-4f5f-b4ca-a14bf692****</RootStackId>
          <StackType>ROS</StackType>
          <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
</GetStackResponse>
```

`JSON` format `{`

```json
    "CreationTime": "2019-08-01T04:07:39",
    "Description": "No description",
    "DisableRollback": false,
    "NotificationURLs": [
        "http://127.0.XX.XX:8080/x",
        "http://127.0.XX.XX:8080/y"
```

`],`

```json
    "Outputs": [
```

`{`

```json
            "Description": "Instance ID",
            "OutputKey": "InstanceId",
            "OutputValue": "i-a****"
```

`}` `],`

```json
    "Parameters": [
```

`{`

```json
            "ParameterKey": "InstanceType",
            "ParameterValue": "ecs.cm4.6xlarge"
```

`}` `],`

```json
    "RegionId": "cn-hangzhou",
    "StackId": "4a6c9851-3b0f-4f5f-b4ca-a14bf691****",
    "StackName": "MyStack",
    "Status": "CREATE_COMPLETE",
    "StatusReason": "Stack successfully created",
    "TemplateDescription": "Some description",
    "TimeoutInMinutes": 10,
    "UpdatedTime": "2019-08-01T04:07:39",
    "ParentStackId": "4a6c9851-3b0f-4f5f-b4ca-a14bf692****",
    "DriftDetectionTime": "2020-02-27T07:47:47",
    "StackDriftStatus": "IN_SYNC",
    "RamRoleName": "test-role",
    "DeletionProtection": "Enabled",
    "RootStackId": "4a6c9851-3b0f-4f5f-b4ca-a14bf692****",
    "StackType": "ROS",
    "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F"
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the specified stack does not exist. name indicates the name or ID of the stack. |

#### 1.7.6 DeleteStack

You can call this operation to delete a stack and all of its resources. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteStack | The operation that you want to perform. Set the value to DeleteStack. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| RetainAllResource s | Boolean | No | false | Specifies whether to retain the resources in the stack. |
| RetainResources. N | RepeatLi st | No | WebServer | The list of resources to retain. |
| RamRoleName | String | No | test-role | The name of the RAM role. ROS assumes the specified RAM role to create the stack and call API operations by using the credentials of the role. All operations are performed under this role. If a RAM user is authorized to perform operations on the stack but does not have the permission to use the role, ROS still uses the role and grants the role the least privilege. If you do not specify this parameter, ROS does not use the role previously associated with the stack. If you want to use a role, you must specify it in this parameter. If no roles are available, ROS uses the temporary credentials generated from the credentials of your account. The RAM role name can be up to 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | The ID of the request. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=DeleteStack &RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteStackResponse>
      <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
</DeleteStackResponse>
```

`JSON` format `{`

```json
  "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F"
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidOperation.Deletio nProtection | Fail to delete stack {ID}, as deletion protection is enabled. | The error message returned because deletion protection prevented the stack from being deleted. ID indicates the stack ID. |
| 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the specified stack does not exist. name indicates the name or ID of the stack. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 409 | ActionInProgress | Stack {name} already has an action ({action}) in progress. | The error message returned because the specified stack has a change operation in progress. name indicates the name or ID of the stack, and action indicates the change operation. |

#### 1.7.7 ListStacks

Queries the list of stacks. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListStacks | The operation that you want to perform. Set the value to ListStacks. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Status.N | RepeatLi st | No | CREATE COMPLET _ E | The status of stack N. Valid values: CREATE IN PROGRESS _ _ CREATE FAILED _ CREATE COMPLETE _ UPDATE IN PROGRESS _ _ UPDATE FAILED _ UPDATE COMPLETE _ DELETE IN PROGRESS _ _ DELETE FAILED _ DELETE COMPLETE _ CREATE ROLLBACK IN PROGRESS _ _ _ CREATE ROLLBACK FAILED _ _ CREATE ROLLBACK COMPLETE _ _ ROLLBACK IN PROGRESS _ _ ROLLBACK FAILED _ ROLLBACK COMPLETE _ CHECK IN PROGRESS _ _ CHECK FAILED _ CHECK COMPLETE _ REVIEW IN PROGRESS _ _ IMPORT CREATE IN PROGRESS _ _ _ IMPORT CREATE FAILED _ _ IMPORT CREATE COMPLETE _ _ IMPORT CREATE ROLLBACK IN PROGR _ _ _ _ ESS IMPORT CREATE ROLLBACK FAILED _ _ _ IMPORT CREATE ROLLBACK COMPLET _ _ _ E IMPORT UPDATE IN PROGRESS _ _ _ IMPORT UPDATE FAILED _ _ IMPORT UPDATE COMPLETE _ _ IMPORT UPDATE ROLLBACK IN PROG _ _ _ _ RESS IMPORT UPDATE ROLLBACK FAILED _ _ _ IMPORT UPDATE ROLLBACK COMPLET _ _ _ E Valid values of N: 1 to 5. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageSize | Long | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |
| ParentStackId | String | No | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the parent stack. |
| StackName.N | RepeatLi st | No | MyStack | The name of stack N. The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores ( ). It must start with a digit or letter. _ Fuzzy search with an asterisk (*) is supported. Valid values of N: 1 to 5. |
| PageNumber | Long | No | 1 | The number of the page to return. Pages start from page 1. Default value: 1. |
| ShowNestedStac k | Boolean | No | true | Specifies whether to display nested stacks. Default value: false. Valid values: true false Not e This parameter is set to true if the ParentStackId parameter is specified. |
| Tag.N.Key | String | No | usage | The key of tag N of the stack. Valid values of N: 1 to 20. |
| Tag.N.Value | String | No | test | The value of tag N of the stack. Valid values of N: 1 to 20. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| StackId | String | No | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. If detailed information about the stack is not required, you can use this parameter to replace the GetStack operation. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Stacks | Array of Stack |   | The list of stacks. |
| CreateTime | String | 2019-08- 01T04:07:39 | The time when the stack was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC. |
| DisableRollback | Boolean | false | Indicates whether rollback is disabled when the stack fails to be created. Default value: false. Valid values: true: Rollback is disabled when the stack fails to be created. false: Rollback is enabled when the stack fails to be created. |
| DriftDetectionTi me | String | 2020-02- 27T07:47:47 | The time when the latest successful drift detection operation was initiated. |
| ParentStackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf692**** | The ID of the parent stack. |
| RegionId | String | cn-hangzhou | The region ID of the stack. |
| StackDriftStatu s | String | IN SYNC _ | The drift status of the stack in the latest successful drift detection. Valid values: DRIFTED: The stack has drifted. NOT CHECKED: No drift detection has _ been performed on the stack. IN SYNC: The stack is being synchronized. _ |
| StackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |

| R | esource Orchestra | tion Service |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| StackName | String | MyStack | The name of the stack. |
| StackType | String | ROS | The type of the stack. Set the value to ROS, which indicates that the stack was created based on an ROS template. |
| Status | String | CREATE COMPLETE _ | The status of the stack. Valid values: CREATE IN PROGRESS _ _ CREATE FAILED _ CREATE COMPLETE _ UPDATE IN PROGRESS _ _ UPDATE FAILED _ UPDATE COMPLETE _ DELETE IN PROGRESS _ _ DELETE FAILED _ DELETE COMPLETE _ CREATE ROLLBACK IN PROGRESS _ _ _ CREATE ROLLBACK FAILED _ _ CREATE ROLLBACK COMPLETE _ _ ROLLBACK IN PROGRESS _ _ ROLLBACK FAILED _ ROLLBACK COMPLETE _ CHECK IN PROGRESS _ _ CHECK FAILED _ CHECK COMPLETE _ REVIEW IN PROGRESS _ _ IMPORT CREATE IN PROGRESS _ _ _ IMPORT CREATE FAILED _ _ IMPORT CREATE COMPLETE _ _ IMPORT CREATE ROLLBACK IN PROGRESS _ _ _ _ IMPORT CREATE ROLLBACK FAILED _ _ _ IMPORT CREATE ROLLBACK COMPLETE _ _ _ IMPORT UPDATE IN PROGRESS _ _ _ IMPORT UPDATE FAILED _ _ IMPORT UPDATE COMPLETE _ _ IMPORT UPDATE ROLLBACK IN PROGRESS _ _ _ _ IMPORT UPDATE ROLLBACK FAILED _ _ _ IMPORT UPDATE ROLLBACK COMPLETE _ _ _ |

| Parameter | Type | Example | Description |
|---|---|---|---|
| StatusReason | String | Stack successfully created | The reason why the stack is in its current state. |
| TimeoutInMinut es | Integer | 10 | The timeout period that is specified for the stack creation request. Unit: minutes. |
| UpdateTime | String | 2019-08- 01T04:07:39 | The time when the stack was last updated. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC. |
| PageSize | Integer | 10 | The number of entries returned per page. Maximum value: 50. Default value: 10. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| TotalCount | Integer | 1 | The total number of stacks. |
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | The ID of the request. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/?Action=ListStacks &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ListStacksResponse>
    <Stacks>
        <Stack>
            <StackId>4a6c9851-3b0f-4f5f-b4ca-a14bf691****</StackId>
            <ParentStackId>4a6c9851-3b0f-4f5f-b4ca-a14bf692****</ParentStackId>
            <StackName>StackName</StackName>
            <RegionId>cn-hangzhou</RegionId>
            <DisableRollback>false</DisableRollback>
            <CreateTime>2019-08-01T04:07:39</CreationTime>
            <Status>CREATE_COMPLETE</Status>
            <StatusReason>Stack successfully created</StatusReason>
            <TimeoutInMinutes>10</TimeoutInMinutes>
            <UpdatedTime>2019-08-01T04:07:39</UpdatedTime>
            <DriftDetectionTime>2020-02-27T07:47:47</DriftDetectionTime>
            <StackDriftStatus>IN_SYNC</StackDriftStatus>
            <StackType>ROS</StackType>
        </Stack>
    </Stacks>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <TotalCount>1</TotalCount>
    <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
</ListStacksResponse>
```

`JSON` format `{`

```json
    "Stacks": [
```

`{`

```json
            "StackId": "4a6c9851-3b0f-4f5f-b4ca-a14bf691****",
            "ParentStackId": "4a6c9851-3b0f-4f5f-b4ca-a14bf692****",
            "StackName": "MyStack",
            "RegionId": "cn-hangzhou",
            "DisableRollback": false,
            "CreateTime": "2019-08-01T04:07:39",
            "Status": "CREATE_COMPLETE",
            "StatusReason": "Stack successfully created",
            "TimeoutInMinutes": 10,
            "UpdatedTime": "2019-08-01T04:07:39",
            "DriftDetectionTime": "2020-02-27T07:47:47",
      "StackDriftStatus": "IN_SYNC",
            "StackType": "ROS"
```

`}` `],`

```json
    "PageNumber": 1,
    "PageSize": 10,
    "TotalCount": 1,
    "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F"
```

`}`

#### 1.7.8 PreviewStack

You can call this operation to preview the stack to be created by using a specified template. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | PreviewStack | The operation that you want to perform. Set the value to PreviewStack. |
| Parameters.N.Par ameterKey | String | Yes | InstanceType | The key of parameter N. If the key and value of the parameter are not specified, the key and value in the template are used. Maximum value of N: 200. Not e Parameters is an optional parameter. If you need to specify Parameters, you must specify both Parameters.N.ParameterKe y and Parameters.N.ParameterVa lue. |
| Parameters.N.Par ameterValue | String | Yes | ecs.cm4.6xlarge | The value of parameter N. Maximum value of N: 200. Not e Parameters is an optional parameter. If you need to specify Parameters, you must specify both Parameters.N.ParameterKe y and Parameters.N.ParameterVa lue. |
| RegionId | String | Yes | cn-beijing | The region ID of the stack. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| StackName | String | Yes | MyStack | The name of the stack. The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores ( ). It must start with a digit or letter. _ |
| DisableRollback | Boolean | No | false | Specifies whether to disable rollback on stack creation failure. Default value: false. Valid values: true: disables rollback on stack creation failure. false: enables rollback on stack creation failure. |
| TimeoutInMinutes | Long | No | 10 | The timeout period that is specified for the stack creation request. Unit: minutes. Default value: 60. |
| TemplateBody | String | No | {"ROSTemplateFo rmatVersion": "2015-09-01" } | The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body is longer than required, we recommend that you add parameters to the HTTP POST request body to avoid request failures due to excessive length of URLs. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| StackPolicyURL | String | No | oss://ros-stack- policy/demo | The URL of the file that contains the stack policy. The URL must point to a policy located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/stack- policy/demo and oss://ros/stack- policy/demo?RegionId=cn-hangzhou. The policy can be up to 16,384 bytes in length and the URL can be up to 1,350 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Not e You must specify one of the StackPolicyBody and StackPolicyURL parameters, but you cannot specify both of them. |
| StackPolicyBody | String | No | {"Statement": [{"Action": "Update:*", "Resource": "*", "Effect": "Allow", "Principal": "*"}]} | The structure that contains the stack policy body. The stack policy body must be 1 to 16,384 bytes in length. Not e You must specify one of the StackPolicyBody and StackPolicyURL parameters, but you cannot specify both of them. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 42665544**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can be up to 64 characters in length and can contain letters, digits, hyphens (-), and underscores ( ). _ |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TemplateURL | String | No | oss://ros- template/demo | The URL of the file that contains the template body. The URL must point to a template located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/template/demo and oss://ros/template/demo? RegionId=cn-hangzhou. The template must be 1 to 524,288 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | The ID of the request. |
| Stack | Struct |   | Details about the stack. |
| Description | String | One ECS instance. | The description of the stack. |
| DisableRollback | Boolean | false | Indicates whether rollback is disabled. |
| Parameters | Array of Parameter |   | The parameters of the stack. |
| ParameterKey | String | SystemDiskCategory | The key of the parameter. |
| ParameterValu e | String | cloud ssd _ | The value of the parameter. |
| RegionId | String | cn-beijing | The region ID of the stack. |
| Resources | Array of Resource |   | The list of resources in the stack. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Description | String | ECS instance. | The description of the resource. |
| LogicalResourc eId | String | WebServer | The logical resource ID. |
| Properties | Map | { "DiskMappings": [ { "Category": "cloud ssd", "Size": _ "20" } ], "SystemDisk Catego _ ry": "cloud ssd", _ "InstanceChargeTyp e": "PostPaid", "AutoRenew": "False", "WillReplace": true, "ImageId": "centos 7", _ "InstanceType": "ecs.g6.large", "AllocatePublicIP": true, "AutoRenewPeriod": 1, "IoOptimized": "optimized", "ZoneId": "cn- beijing-g", "VSwitchId": "", "SecurityGroupId": "", "Period": 1, "InternetChargeType ": "PayByTraffic", "SystemDiskCategor y": "cloud efficiency", _ "InternetMaxBandwi dthOut": 1, "VpcId": "", "InternetMaxBandwi dthIn": 200, "PeriodUnit": "Month" } | The properties of the resource. |
| RequiredBy | List | ["Resource1", "Resource2"] | The list of one or more resources that are dependent on the stack. |
| ResourceType | String | ALIYUN::ECS::Instan ce | The type of the resource. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Stack | Map | {} | Details about the nested stacks. The data structure of this parameter is the same as that of the entire responses. |
| StackName | String | MyStack | The name of the stack. |
| StackPolicyBod y | Map | { "Statement": [ { "Action": "Update:*", "Resource": "*", "Effect": "Allow", "Principal": "*" }, { "Action": "Update:*", "Resource": "LogicalResourceId/ apple1", "Effect": "Deny", "Principal": "*" } ] } | The stack policy. |
| TemplateDescri ption | String | One ECS instance. | The description of the template. |
| TimeoutInMinut es | Integer | 10 | The timeout period. Unit: minutes. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=PreviewStack &RegionId=cn-beijing &Parameters.1.ParameterValue=ecs.cm4.6xlarge &Parameters.1.ParameterKey=InstanceType &StackName=MyStack &TimeoutInMinutes=10 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<PreviewStackResponse>
          <Stack>
                <Description>No description</Description>
                <DisableRollback>true</DisableRollback>
                <Parameters>
                      <ParameterKey>UpdateVersion</ParameterKey>
                      <ParameterValue>1</ParameterValue>
```

`/`

```xml
                </Parameters>
                <RegionId>cn-beijing</RegionId>
                <Resources>
                      <Description></Description>
                      <LogicalResourceId>WaitConditionHandle</LogicalResourceId>
                      <Properties>
                            <Count>-1</Count>
                            <Mode>Full</Mode>
                            <UpdateVersion>1</UpdateVersion>
                      </Properties>
                      <ResourceType>ALIYUN::ROS::WaitConditionHandle</ResourceType>
                </Resources>
                <Resources>
                      <Description></Description>
                      <LogicalResourceId>nested</LogicalResourceId>
                      <Properties>
                            <Parameters></Parameters>
                            <TemplateURL>oss://nested-stack/test/demo</TemplateURL>
                            <TimeoutMins>16</TimeoutMins>
                      </Properties>
                      <ResourceType>ALIYUN::ROS::Stack</ResourceType>
                      <Stack>
                            <Description>No description</Description>
                            <DisableRollback>true</DisableRollback>
                            <Parameters>
                                  <ParameterKey>ALIYUN::AccountId</ParameterKey>
                                  <ParameterValue>1666666****</ParameterValue>
                            </Parameters>
                            <Parameters>
                                  <ParameterKey>ALIYUN::NoValue</ParameterKey>
                                  <ParameterValue>None</ParameterValue>
                            </Parameters>
                            <Parameters>
                                  <ParameterKey>ALIYUN::Region</ParameterKey>
                                  <ParameterValue>cn-beijing</ParameterValue>
                            </Parameters>
                            <Parameters>
                                  <ParameterKey>ALIYUN::StackId</ParameterKey>
                                  <ParameterValue>None</ParameterValue>
                            </Parameters>
                            <Parameters>
                                  <ParameterKey>ALIYUN::StackName</ParameterKey>
                                  <ParameterValue>test-preview-stack-complex-nested</Parame
terValue>
                            </Parameters>
                            <RegionId>cn-beijing</RegionId>
                            <Resources>
                                  <Description></Description>
                                  <LogicalResourceId>WaitConditionHandle</LogicalResourceId
```

`>`

```xml
                                  <Properties>
                                        <Count>-1</Count>
                                        <Mode>Full</Mode>
                                        <UpdateVersion>1</UpdateVersion>
</Properties>
```

```xml
                                  </Properties>
                                  <ResourceType>ALIYUN::ROS::WaitConditionHandle</ResourceT
ype>
                            </Resources>
                            <StackName>test-preview-stack-complex-nested</StackName>
                            <StackPolicyBody>
                                  <Statement>
                                        <Action>Update:*</Action>
                                        <Effect>Allow</Effect>
                                        <Principal>*</Principal>
                                        <Resource>*</Resource>
                                  </Statement>
                                  <Statement>
                                        <Action>Update:*</Action>
                                        <Effect>Deny</Effect>
                                        <Principal>*</Principal>
                                        <Resource>LogicalResourceId/apple1</Resource>
                                  </Statement>
                            </StackPolicyBody>
                            <TemplateDescription>No description</TemplateDescription>
                            <TimeoutInMinutes>12</TimeoutInMinutes>
                      </Stack>
                </Resources>
                <StackName>test-preview-stack-complex</StackName>
                <StackPolicyBody>
                      <Statement>
                            <Action>Update:*</Action>
                            <Effect>Allow</Effect>
                            <Principal>*</Principal>
                            <Resource>*</Resource>
                      </Statement>
                      <Statement>
                            <Action>Update:*</Action>
                            <Effect>Deny</Effect>
                            <Principal>*</Principal>
                            <Resource>LogicalResourceId/apple1</Resource>
                      </Statement>
                </StackPolicyBody>
                <TemplateDescription>No description</TemplateDescription>
                <TimeoutInMinutes>10</TimeoutInMinutes>
          </Stack>
          <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
</PreviewStackResponse>
```

`JSON` format `{`

```json
    "Stack": {
        "Description": "No description",
        "DisableRollback": true,
        "Parameters": [
```

`{`

```json
                "ParameterKey": "UpdateVersion",
                "ParameterValue": "1"
```

`}` `],`

```json
        "RegionId": "cn-beijing",
        "Resources": [
```

`{`

```json
                "Description": "",
                "LogicalResourceId": "WaitConditionHandle",
                "Properties": {
                    "Count": -1,
                    "Mode": "Full",
                    "UpdateVersion": 1
```

`},`

```json
                "RequiredBy": [],
                "ResourceType": "ALIYUN::ROS::WaitConditionHandle"
```

`},` `{`

```json
                "Description": "",
                "LogicalResourceId": "nested",
                "Properties": {
                    "Parameters": null,
                    "TemplateURL": "oss://nested-stack/test/demo",
                    "TimeoutMins": 16
```

`},`

```json
                "RequiredBy": [],
                "ResourceType": "ALIYUN::ROS::Stack",
                "Stack": {
                    "Description": "No description",
                    "DisableRollback": true,
                    "Parameters": [
```

`{`

```json
                            "ParameterKey": "ALIYUN::AccountId",
                            "ParameterValue": "1666666****"
```

`},` `{`

```json
                            "ParameterKey": "ALIYUN::NoValue",
                            "ParameterValue": "None"
```

`},` `{`

```json
                            "ParameterKey": "ALIYUN::Region",
                            "ParameterValue": "cn-beijing"
```

`},` `{`

```json
                            "ParameterKey": "ALIYUN::StackId",
                            "ParameterValue": "None"
```

`},` `{`

```json
                            "ParameterKey": "ALIYUN::StackName",
                            "ParameterValue": "test-preview-stack-complex-nested"
```

`}` `],`

```json
                    "RegionId": "cn-beijing",
                    "Resources": [
```

`{`

```json
                            "Description": "",
```

```json
                            "LogicalResourceId": "WaitConditionHandle",
                            "Properties": {
                                "Count": -1,
                                "Mode": "Full",
                                "UpdateVersion": 1
```

`},`

```json
                            "RequiredBy": [],
                            "ResourceType": "ALIYUN::ROS::WaitConditionHandle"
```

`}` `],`

```json
                    "StackName": "test-preview-stack-complex-nested",
                    "StackPolicyBody": {
                        "Statement": [
```

`{`

```json
                                "Action": "Update:*",
                                "Effect": "Allow",
                                "Principal": "*",
                                "Resource": "*"
```

`},` `{`

```json
                                "Action": "Update:*",
                                "Effect": "Deny",
                                "Principal": "*",
                                "Resource": "LogicalResourceId/apple1"
```

`}` `]` `},`

```json
                    "TemplateDescription": "No description",
                    "TimeoutInMinutes": 12
```

`}` `}` `],`

```json
        "StackName": "test-preview-stack-complex",
        "StackPolicyBody": {
            "Statement": [
```

`{`

```json
                    "Action": "Update:*",
                    "Effect": "Allow",
                    "Principal": "*",
                    "Resource": "*"
```

`},` `{`

```json
                    "Action": "Update:*",
                    "Effect": "Deny",
                    "Principal": "*",
                    "Resource": "LogicalResourceId/apple1"
```

`}` `]` `},`

```json
        "TemplateDescription": "No description",
        "TimeoutInMinutes": 10
```

`},`

```json
    "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F"
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | CircularDependency | Circular Dependency Found: {reason}. | The error message returned because the template contains a circular dependency. reason indicates the specific reason. |
| 400 | InvalidSchema | {reason}. | The error message returned because the specified template format is invalid. reason indicates the specific reason. |
| 400 | InvalidTemplateAttribut e | The Referenced Attribute ({resource} {name}) is incorrect. | The error message returned because the resource attribute referenced in the template is incorrect. resource indicates the resource name, and name indicates the attribute name. |
| 400 | InvalidTemplatePropert yType | The specified value type of ({resource} {section}) is incorrect. | The error message returned because the type of the specified resource section defined in the template is incorrect. resource indicates the resource name, and section indicates the section name. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidTemplateReferen ce | The specified reference "{name}" (in {referencer}) is incorrect. | The error message returned because the template contains an invalid reference. name indicates the reference name, and referencer indicates the referencer name. |
| 400 | InvalidTemplateSection | The template section is invalid: {section}. | The error message returned because the template contains an invalid property. section indicates the section name. |
| 400 | InvalidTemplateVersion | The template version is invalid: {reason}. | The error message returned because the template version is incorrect. reason indicates the specific reason. |
| 400 | StackValidationFailed | {reason}. | The error message returned because the stack validation failed. reason indicates the specific reason. |
| 400 | UnknownUserParameter | The Parameter ({name}) was not defined in template. | The error message returned because the specified parameter is not defined in the template. name indicates the parameter key. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | UserParameterMissing | The Parameter {name} was not provided. | The error message returned because no value is passed into the specified parameter defined in the template. name indicates the parameter key. |
| 409 | StackExists | The Stack ({name}) already exists. | The error message returned because a stack with the same name already exists. name indicates the stack name. |

#### 1.7.9 ListStackEvents

You can call this operation to query stacks and their resource events. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListStackEvents | The operation that you want to perform. Set the value to ListStackEvents. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Status.N | RepeatLi st | No | CREATE IN PROGR _ _ ESS | The state of resource N. Valid values: CREATE COMPLETE _ CREATE FAILED _ CREATE IN PROGRESS _ _ UPDATE IN PROGRESS _ _ UPDATE FAILED _ UPDATE COMPLETE _ UPDATE SKIPPED _ DELETE IN PROGRESS _ _ DELETE FAILED _ CHECK IN PROGRESS _ _ CHECK FAILED _ CHECK COMPLETE _ IMPORT IN PROGRESS _ _ IMPORT FAILED _ IMPORT COMPLETE _ |
| ResourceType.N | RepeatLi st | No | ALIYUN::ECS::Inst ance | The type of resource N. Maximum value of N: 200. |
| LogicalResourceId .N | RepeatLi st | No | WebServer | The logical ID of the resource as defined in the template. |
| PageNumber | Long | No | 1 | The number of the page to return. Pages start from page 1. Default value: 1. |
| PageSize | Long | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Events | Array of Event |   | The list of events. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| CreateTime | String | 2019-08- 01T04:07:39 | The time when the task was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC. |
| EventId | String | 0086612d-77cf- 4056-b0b5- ff8e94ad**** | The ID of the event. |
| LogicalResourc eId | String | WebServer | The logical ID of the resource as defined in the template. |
| PhysicalResourc eId | String | i- m5e3tfdbinchnexh** ** | The physical ID of the resource. |
| ResourceType | String | ALIYUN::ECS::Instan ce | The type of the resource. |
| StackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| StackName | String | StackName | The name of the stack. |
| Status | String | CREATE COMPLETE _ | The state of the resource. |
| StatusReason | String | state changed | The reason why the resource is in its current state. |
| PageNumber | Integer | 1 | The page number of the returned page. Pages start from page 1. Default value: 1. |
| PageSize | Integer | 10 | The number of entries returned per page. Maximum value: 50. Default value: 10. |
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | The ID of the request. |
| TotalCount | Integer | 20 | The total number of returned events. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=ListStackEvents &RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ListStackEventsResponse>
       <Events class="array">
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:56</CreationTime>
                     <EventId type="string">0086612d-77cf-4056-b0b5-ff8e94ad****</EventId>
                     <LogicalResourceId type="string">test-describe-events</LogicalResource
Id>
                     <PhysicalResourceId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****
</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::ROS::Stack</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackId>
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_COMPLETE</Status>
                     <StatusReason type="string">Stack successfully updated</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:55</CreationTime>
                     <EventId type="string">2b900d01-959b-49a8-8cfe-f7de87aa****</EventId>
                     <LogicalResourceId type="string">dummy</LogicalResourceId>
                     <PhysicalResourceId type="string">a</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::DEBUG::Dummy</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackId>
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_COMPLETE</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:55</CreationTime>
                     <EventId type="string">30f721d4-8124-4fd4-8afd-7b21471f****</EventId>
                     <LogicalResourceId type="string">dummy3</LogicalResourceId>
                     <PhysicalResourceId type="string">a</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::DEBUG::Dummy</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackId>
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">CREATE_COMPLETE</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:54</CreationTime>
                     <EventId type="string">b5ecc0ac-f855-4503-945c-82d398a2****</EventId>
                     <LogicalResourceId type="string">WaitConditionHandle</LogicalResourceI
```

`d>` `d>`

```
                     <ResourceType type="string">ALIYUN::ROS::WaitConditionHandle</Resource
Type>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackId>
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_COMPLETE</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:53</CreationTime>
                     <EventId type="string">a01e5730-7244-414e-b9ff-f97e3885****</EventId>
                     <LogicalResourceId type="string">dummy3</LogicalResourceId>
                     <ResourceType type="string">ALIYUN::DEBUG::Dummy</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackId>
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">CREATE_IN_PROGRESS</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:53</CreationTime>
                     <EventId type="string">262b2f54-7ae7-4cf6-9c8a-eb4d0801****</EventId>
                     <LogicalResourceId type="string">dummy</LogicalResourceId>
                     <PhysicalResourceId type="string">a</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::DEBUG::Dummy</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackId>
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_IN_PROGRESS</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:53</CreationTime>
                     <EventId type="string">163c3965-1617-4787-ba08-1eed0e3a****</EventId>
                     <LogicalResourceId type="string">nested</LogicalResourceId>
                     <PhysicalResourceId type="string">4ed7ab13-c912-4239-b064-8cea7caa****
</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::ROS::Stack</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackId>
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_COMPLETE</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:53</CreationTime>
                     <EventId type="string">71f7c25c-2ac7-4336-9934-85482111****</EventId>
                     <LogicalResourceId type="string">nested</LogicalResourceId>
                     <PhysicalResourceId type="string">4ed7ab13-c912-4239-b064-8cea7caa****
</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::ROS::Stack</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackId>
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_IN_PROGRESS</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
<CreationTimetype="string">2019-08-01T05:57:53</CreationTime>
```

```
                     <CreationTime type=string>20190801T05:57:53</CreationTime>
                     <EventId type="string">a5a0eb9e-7abe-44a1-a376-70955211****</EventId>
                     <LogicalResourceId type="string">WaitConditionHandle</LogicalResourceI
```

`d>`

```
                     <ResourceType type="string">ALIYUN::ROS::WaitConditionHandle</Resource
Type>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackId>
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_IN_PROGRESS</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:53</CreationTime>
                     <EventId type="string">250f5003-f59d-46f9-8471-65d0c630****</EventId>
                     <LogicalResourceId type="string">test-describe-events</LogicalResource
Id>
                     <PhysicalResourceId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****
</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::ROS::Stack</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackId>
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_IN_PROGRESS</Status>
                     <StatusReason type="string">Stack UPDATE started</StatusReason>
              </Event>
       </Events>
       <PageNumber type="number">1</PageNumber>
       <PageSize type="number">10</PageSize>
       <RequestId type="string">B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
       <TotalCount type="number">20</TotalCount>
</ListStackEventsResponse>
```

`JSON` format `{`

```json
   "Events": [
```

`{`

```json
           "CreationTime": "2019-08-01T05:57:56",
           "EventId": "0086612d-77cf-4056-b0b5-ff8e94ad****",
           "LogicalResourceId": "test-describe-events",
           "PhysicalResourceId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "ResourceType": "ALIYUN::ROS::Stack",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
           "Status": "UPDATE_COMPLETE",
           "StatusReason": "Stack successfully updated"
```

`},` `{`

```json
           "CreationTime": "2019-08-01T05:57:55",
           "EventId": "2b900d01-959b-49a8-8cfe-f7de87aa****",
           "LogicalResourceId": "dummy",
           "PhysicalResourceId": "a",
           "ResourceType": "ALIYUN::DEBUG::Dummy",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
```

```json
           "Status": "UPDATE_COMPLETE",
           "StatusReason": "state changed"
```

`},` `{`

```json
           "CreationTime": "2019-08-01T05:57:55",
           "EventId": "30f721d4-8124-4fd4-8afd-7b21471f****",
           "LogicalResourceId": "dummy3",
           "PhysicalResourceId": "a",
           "ResourceType": "ALIYUN::DEBUG::Dummy",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
           "Status": "CREATE_COMPLETE",
           "StatusReason": "state changed"
```

`},` `{`

```json
           "CreationTime": "2019-08-01T05:57:54",
           "EventId": "b5ecc0ac-f855-4503-945c-82d398a2****",
           "LogicalResourceId": "WaitConditionHandle",
           "ResourceType": "ALIYUN::ROS::WaitConditionHandle",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
           "Status": "UPDATE_COMPLETE",
           "StatusReason": "state changed"
```

`},` `{`

```json
           "CreationTime": "2019-08-01T05:57:53",
           "EventId": "a01e5730-7244-414e-b9ff-f97e3885****",
           "LogicalResourceId": "dummy3",
           "ResourceType": "ALIYUN::DEBUG::Dummy",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
           "Status": "CREATE_IN_PROGRESS",
           "StatusReason": "state changed"
```

`},` `{`

```json
           "CreationTime": "2019-08-01T05:57:53",
           "EventId": "262b2f54-7ae7-4cf6-9c8a-eb4d0801****",
           "LogicalResourceId": "dummy",
           "PhysicalResourceId": "a",
           "ResourceType": "ALIYUN::DEBUG::Dummy",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
           "Status": "UPDATE_IN_PROGRESS",
           "StatusReason": "state changed"
```

`},` `{`

```json
           "CreationTime": "2019-08-01T05:57:53",
           "EventId": "163c3965-1617-4787-ba08-1eed0e3a****",
           "LogicalResourceId": "nested",
           "PhysicalResourceId": "4ed7ab13-c912-4239-b064-8cea7caa****",
           "ResourceType": "ALIYUN::ROS::Stack",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
           "Status": "UPDATE_COMPLETE",
"Stt
```

`R` `"`

```
"tt
```

`h` `d"`

```json
           "StatusReason": "state changed"
```

`},` `{`

```json
           "CreationTime": "2019-08-01T05:57:53",
           "EventId": "71f7c25c-2ac7-4336-9934-85482111****",
           "LogicalResourceId": "nested",
           "PhysicalResourceId": "4ed7ab13-c912-4239-b064-8cea7caa****",
           "ResourceType": "ALIYUN::ROS::Stack",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
           "Status": "UPDATE_IN_PROGRESS",
           "StatusReason": "state changed"
```

`},` `{`

```json
           "CreationTime": "2019-08-01T05:57:53",
           "EventId": "a5a0eb9e-7abe-44a1-a376-70955211****",
           "LogicalResourceId": "WaitConditionHandle",
           "ResourceType": "ALIYUN::ROS::WaitConditionHandle",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
           "Status": "UPDATE_IN_PROGRESS",
           "StatusReason": "state changed"
```

`},` `{`

```json
           "CreationTime": "2019-08-01T05:57:53",
           "EventId": "250f5003-f59d-46f9-8471-65d0c630****",
           "LogicalResourceId": "test-describe-events",
           "PhysicalResourceId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "ResourceType": "ALIYUN::ROS::Stack",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
           "Status": "UPDATE_IN_PROGRESS",
           "StatusReason": "Stack UPDATE started"
```

`}` `],`

```json
   "PageNumber": 1,
   "PageSize": 10,
   "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F",
   "TotalCount": 20
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the specified stack does not exist. name indicates the name or ID of the stack. |

### 1.8 Resource operations

#### 1.8.1 GetResourceTypeTemplate

You can call this operation to query the template of a resource by resource type. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetResourceType Template | The operation that you want to perform. Set the value to GetResourceTypeTemplate. |
| ResourceType | String | Yes | ALIYUN::ECS::VP C | The type of the resource. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 87F54B2B-AEF0- 4C33-A72A- 3F8856A575E9 | The ID of the request. |
| TemplateBody | Map | {"ROSTemplateForm atVersion": "2015- 09-01"} | The structure that contains the template body. The template body must be 1 to 51,200 bytes in length. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=GetResourceTypeTemplate &ResourceType=ALIYUN::ECS::VPC &<Common request parameters>
```

Sample success responses `XML` format

```xml
<GetResourceTypeTemplateResponse>
       <RequestId type="string">87F54B2B-AEF0-4C33-A72A-3F8856A575E9</RequestId>
       <TemplateBody class="object">
              <Parameters class="object">
                     <CidrBlock class="object">
                            <Type type="string">String</Type>
                     </CidrBlock>
                     <Description class="object">
                            <Type type="string">String</Type>
                     </Description>
                     <ResourceGroupId class="object">
                            <Type type="string">String</Type>
                     </ResourceGroupId>
                     <VpcName class="object">
                            <Type type="string">String</Type>
                     </VpcName>
              </Parameters>
              <ROSTemplateFormatVersion type="string">2015-09-01</ROSTemplateFormatVersion>
              <Resources class="object">
                     <Vpc class="object">
                            <Properties class="object">
                                   <CidrBlock class="object">
                                          <Ref type="string">CidrBlock</Ref>
                                   </CidrBlock>
                                   <Description class="object">
                                          <Ref type="string">Description</Ref>
                                   </Description>
                                   <ResourceGroupId class="object">
                                          <Ref type="string">ResourceGroupId</Ref>
                                   </ResourceGroupId>
                                   <VpcName class="object">
                                          <Ref type="string">VpcName</Ref>
                                   </VpcName>
                            </Properties>
                            <Type type="string">ALIYUN::ECS::VPC</Type>
                     </Vpc>
              </Resources>
       </TemplateBody>
</GetResourceTypeTemplateResponse>
```

`JSON` format `{`

```json
  "RequestId": "87F54B2B-AEF0-4C33-A72A-3F8856A575E9",
  "TemplateBody": {
    "Parameters": {
      "CidrBlock": {
        "Type": "String"
```

`},`

```json
      "Description": {
        "Type": "String"
```

`},`

```json
      "ResourceGroupId": {
        "Type": "String"
```

`},`

```json
      "VpcName": {
        "Type": "String"
```

`}` `},`

```json
    "ROSTemplateFormatVersion": "2015-09-01",
    "Resources": {
      "Vpc": {
        "Properties": {
          "CidrBlock": {
            "Ref": "CidrBlock"
```

`},`

```json
          "Description": {
            "Ref": "Description"
```

`},`

```json
          "ResourceGroupId": {
            "Ref": "ResourceGroupId"
```

`},`

```json
          "VpcName": {
            "Ref": "VpcName"
```

`}` `},`

```json
        "Type": "ALIYUN::ECS::VPC"
```

`}` `}` `}` `}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | ResourceTypeNotFound | The Resource Type ({name}) could not be found. | The error message returned because the specified resource type does not exist. name indicates the name of the resource type. |

#### 1.8.2 ListStackResources

You can call this operation to query the resource list of a specific stack. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListStackResourc es | The operation that you want to perform. Set the value to ListStackResources. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | The ID of the request. |
| Resources | Array of Resource |   | The list of resources. |
| CreateTime | String | 2019-08- 01T06:01:23 | The time when the resource was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC. |
| DriftDetectionTi me | String | 2020-02- 27T07:47:47 | The time when the last successful drift detection operation was initiated. |
| LogicalResourc eId | String | dummy | The logical resource ID defined in the template. |
| PhysicalResourc eId | String | d04af923-e6b7- 4272-aeaa- 47ec9777**** | The physical ID of the resource. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ResourceDriftSt atus | String | IN SYNC _ | The drift state of the resource in the last successful drift detection. Valid values: DELETED: The actual configuration of the resource differs from its expected template configuration because the resource has been deleted. MODIFIED: The actual configuration of the resource differs from its expected template configuration. NOT CHECKED: ROS has not checked _ whether the actual configuration of the resource differs from its expected template configuration. IN SYNC: The actual configuration of the _ resource matches its expected template configuration. |
| ResourceType | String | ALIYUN::ROS::Stack | The type of the resource. |
| StackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| StackName | String | test-describe- resource | The name of the stack. The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores ( ). It must _ start with a digit or letter. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | String | UPDATE COMPLETE _ | The state of the resource. Valid values: CREATE COMPLETE _ CREATE FAILED _ CREATE IN PROGRESS _ _ UPDATE IN PROGRESS _ _ UPDATE FAILED _ UPDATE COMPLETE _ DELETE IN PROGRESS _ _ DELETE FAILED _ DELETE COMPLETE _ CHECK IN PROGRESS _ _ CHECK FAILED _ CHECK COMPLETE _ IMPORT IN PROGRESS _ _ IMPORT FAILED _ IMPORT COMPLETE _ |
| StatusReason | String | state changed | The reason why the resource is in its current state. |
| UpdateTime | String | 2019-08- 01T06:01:29 | The time when the resource was last updated. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=ListStackResources &RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ListStackResourcesResponse>
       <RequestId type="string">B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
       <Resources class="array">
              <Resource class="object">
                     <CreationTime type="string">2019-08-01T06:01:23</CreationTime>
                     <LogicalResourceId type="string">dummy</LogicalResourceId>
                     <PhysicalResourceId type="string">a</PhysicalResourceId>
<ResourceTypetype="string">ALIYUN::DEBUG::Dummy</ResourceType>
```

```xml
                     <ResourceType type=string>ALIYUN::DEBUG::Dummy</ResourceType>
                     <StackId type="string">efdf5c10-96a5-4fd7-ab89-68e7baa2****</StackId>
                     <StackName type="string">test-describe-resource</StackName>
                     <Status type="string">UPDATE_COMPLETE</Status>
                     <StatusReason type="string">state changed</StatusReason>
                     <UpdatedTime type="string">2019-08-01T06:01:29</UpdatedTime>
                     <DriftDetectionTime>2020-02-27T07:47:47</DriftDetectionTime>
                     <ResourceDriftStatus>IN_SYNC</ResourceDriftStatus>
              </Resource>
              <Resource class="object">
                     <CreationTime type="string">2019-08-01T06:01:28</CreationTime>
                     <LogicalResourceId type="string">dummy3</LogicalResourceId>
                     <PhysicalResourceId type="string">a</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::DEBUG::Dummy</ResourceType>
                     <StackId type="string">efdf5c10-96a5-4fd7-ab89-68e7baa2****</StackId>
                     <StackName type="string">test-describe-resource</StackName>
                     <Status type="string">CREATE_COMPLETE</Status>
                     <StatusReason type="string">state changed</StatusReason>
                     <UpdatedTime type="string">2019-08-01T06:01:29</UpdatedTime>
                     <DriftDetectionTime>2020-02-27T07:47:47</DriftDetectionTime>
                     <ResourceDriftStatus>IN_SYNC</ResourceDriftStatus>
              </Resource>
              <Resource class="object">
                     <CreationTime type="string">2019-08-01T06:01:23</CreationTime>
                     <LogicalResourceId type="string">WaitConditionHandle</LogicalResourceI
```

`d>`

```xml
                     <PhysicalResourceId type="string"></PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::ROS::WaitConditionHandle</Resource
Type>
                     <StackId type="string">efdf5c10-96a5-4fd7-ab89-68e7baa2****</StackId>
                     <StackName type="string">test-describe-resource</StackName>
                     <Status type="string">UPDATE_COMPLETE</Status>
                     <StatusReason type="string">state changed</StatusReason>
                     <UpdatedTime type="string">2019-08-01T06:01:29</UpdatedTime>
                     <DriftDetectionTime>2020-02-27T07:47:47</DriftDetectionTime>
                     <ResourceDriftStatus>IN_SYNC</ResourceDriftStatus>
              </Resource>
              <Resource class="object">
                     <CreationTime type="string">2019-08-01T06:01:23</CreationTime>
                     <LogicalResourceId type="string">nested</LogicalResourceId>
                     <PhysicalResourceId type="string">d04af923-e6b7-4272-aeaa-47ec9777****
</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::ROS::Stack</ResourceType>
                     <StackId type="string">efdf5c10-96a5-4fd7-ab89-68e7baa2****</StackId>
                     <StackName type="string">test-describe-resource</StackName>
                     <Status type="string">UPDATE_COMPLETE</Status>
                     <StatusReason type="string">state changed</StatusReason>
                     <UpdatedTime type="string">2019-08-01T06:01:28</UpdatedTime>
                     <DriftDetectionTime>2020-02-27T07:47:47</DriftDetectionTime>
                     <ResourceDriftStatus>IN_SYNC</ResourceDriftStatus>
              </Resource>
       </Resources>
</ListStackResourcesResponse>
```

`JSON` format `{`

```json
   "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F",
   "Resources": [
```

`{`

```json
           "CreationTime": "2019-08-01T06:01:23",
           "LogicalResourceId": "dummy",
           "PhysicalResourceId": "a",
           "ResourceType": "ALIYUN::DEBUG::Dummy",
           "StackId": "efdf5c10-96a5-4fd7-ab89-68e7baa2****",
           "StackName": "test-describe-resource",
           "Status": "UPDATE_COMPLETE",
           "StatusReason": "state changed",
           "UpdatedTime": "2019-08-01T06:01:29",
           "DriftDetectionTime": "2020-02-27T07:47:47",
        "ResourceDriftStatus": "IN_SYNC"
```

`},` `{`

```json
           "CreationTime": "2019-08-01T06:01:28",
           "LogicalResourceId": "dummy3",
           "PhysicalResourceId": "a",
           "ResourceType": "ALIYUN::DEBUG::Dummy",
           "StackId": "efdf5c10-96a5-4fd7-ab89-68e7baa2****",
           "StackName": "test-describe-resource",
           "Status": "CREATE_COMPLETE",
           "StatusReason": "state changed",
           "UpdatedTime": "2019-08-01T06:01:29",
           "DriftDetectionTime": "2020-02-27T07:47:47",
        "ResourceDriftStatus": "IN_SYNC"
```

`},` `{`

```json
           "CreationTime": "2019-08-01T06:01:23",
           "LogicalResourceId": "WaitConditionHandle",
           "PhysicalResourceId": "",
           "ResourceType": "ALIYUN::ROS::WaitConditionHandle",
           "StackId": "efdf5c10-96a5-4fd7-ab89-68e7baa2****",
           "StackName": "test-describe-resource",
           "Status": "UPDATE_COMPLETE",
           "StatusReason": "state changed",
           "UpdatedTime": "2019-08-01T06:01:29",
           "DriftDetectionTime": "2020-02-27T07:47:47",
        "ResourceDriftStatus": "IN_SYNC"
```

`},` `{`

```json
           "CreationTime": "2019-08-01T06:01:23",
           "LogicalResourceId": "nested",
           "PhysicalResourceId": "d04af923-e6b7-4272-aeaa-47ec9777****",
           "ResourceType": "ALIYUN::ROS::Stack",
           "StackId": "efdf5c10-96a5-4fd7-ab89-68e7baa2e0d5",
           "StackName": "test-describe-resource",
           "Status": "UPDATE_COMPLETE",
           "StatusReason": "state changed",
           "UpdatedTime": "2019-08-01T06:01:28",
```

```json
           "DriftDetectionTime": "2020-02-27T07:47:47",
        "ResourceDriftStatus": "IN_SYNC"
```

`}` `]` `}`

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| StackNotFound | The Stack ({name}) could not be found. | 404 | The error message returned because the specified stack does not exist. name indicates the name or ID of the stack. |

#### 1.8.3 GetStackResource

You can call this operation to query information about a resource in a specific stack. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetStackResourc e | The operation that you want to perform. Set the value to GetStackResource. |
| LogicalResourceId | String | Yes | WebServer | The logical ID of the resource as defined in the template. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 42665544**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can be up to 64 characters in length and can contain letters, digits, hyphens (-), and underscores ( ). _ |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ShowResourceAtt ributes | Boolean | No | true | Specifies whether to query resource attributes. Valid values: true false |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | String | CREATE COMPLETE _ | The state of the resource. Valid values: CREATE COMPLETE _ CREATE FAILED _ CREATE IN PROGRESS _ _ UPDATE IN PROGRESS _ _ UPDATE FAILED _ UPDATE COMPLETE _ DELETE IN PROGRESS _ _ DELETE FAILED _ CHECK IN PROGRESS _ _ CHECK FAILED _ CHECK COMPLETE _ IMPORT IN PROGRESS _ _ IMPORT FAILED _ IMPORT COMPLETE _ |
| Description | String | no description | The description of the resource. |
| LogicalResourc eId | String | WebServer | The logical ID of the resource as defined in the template. |
| StackId | String | efdf5c10-96a5- 4fd7-ab89- 68e7baa2**** | The ID of the stack. |
| StackName | String | test-describe- resource | The name of the stack. The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores ( ). It must _ start with a digit or letter. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| StatusReason | String | state changed | The reason why the resource is in its current state. |
| PhysicalResourc eId | String | d04af923-e6b7- 4272-aeaa- 47ec9777**** | The physical ID of the resource. |
| ResourceType | String | ALIYUN::ROS::WaitC onditionHandle | The type of the resource. |
| CreateTime | String | 2019-08- 01T06:01:23 | The time when the stack was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC. |
| Metadata | Map | {"key": "value"} | The metadata. |
| UpdateTime | String | 2019-08- 01T06:01:29 | The time when the stack was last updated. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ResourceAttrib utes | List | [ { "ResourceAttributeV alue":"curl -Uri \"http://100.100.XX .XX/waitcondition? stackname=test- describe- resource&stackid=ef df5c10-96a5-4fd7- ab89- 68e7baa2****&resou rce=WaitConditionH andle&expire=15646 8****&signature=991 d910a901a89db658 0d74233119960c004 ****\" -Method Post -Headers @{\"Content- Type\"=\"applicatio n/json\"; \"Accept\"=\"applic ation/json\"; \"x- acs-region- id\"=\"cn- beijing\"}", "ResourceAttributeK ey":"PowerShellCurl Cli" } ] | The list of resource attributes. |
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | The ID of the request. |
| DriftDetectionTi me | String | 2020-02- 27T07:47:47 | The time when the last successful drift detection operation was initiated. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ResourceDriftSt atus | String | IN SYNC _ | The drift state of the resource in the last successful drift detection. Valid values: DELETED: The actual configuration of the resource differs from its expected template configuration because the resource had been deleted. MODIFIED: The actual configuration of the resource differs from its expected template configuration. NOT CHECKED: ROS has not checked _ whether the actual configuration of the resource differs from its expected template configuration. IN SYNC: The actual configuration of the _ resource matches its expected template configuration. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=GetStackResource &RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &LogicalResourceId=WebServer &<Common request parameters>
```

Sample success responses `XML` format

```xml
<GetStackResourceResponse>
          <CreateTime>2019-08-01T06:01:23</CreateTime>
          <Description></Description>
          <LogicalResourceId>WaitConditionHandle</LogicalResourceId>
          <Metadata></Metadata>
          <PhysicalResourceId></PhysicalResourceId>
          <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
          <ResourceAttributes>
                <ResourceAttributeKey>CurlCli</ResourceAttributeKey>
                <ResourceAttributeValue>curl -i -X POST -H 'Content-Type: application/json'
-H 'Accept: application/json' -H 'x-acs-region-id: cn-beijing' http://100.100.XX.XX/waitcon dition?stackname=test-describe-resource\&amp;stackid=efdf5c10-96a5-4fd7-ab89-68e7baa2****\& amp;resource=WaitConditionHandle\&amp;expire=156468****\&amp;signature=991d910a901a89db6580 d74233119960c004****</ResourceAttributeValue>
          </ResourceAttributes>
          <ResourceAttributes>
                <ResourceAttributeKey>WindowsCurlCli</ResourceAttributeKey>
                <ResourceAttributeValue>curl -i -X POST -H "Content-Type: application/json"
-H "Accept: application/json" -H "x-acs-region-id: cn-beijing" "http://100.100.XX.XX/waitco ndition?stackname=test-describe-resource&amp;stackid=efdf5c10-96a5-4fd7-ab89-68e7baa2****&a mp;resource=WaitConditionHandle&amp;expire=156468****&amp;signature=991d910a901a89db6580d74 233119960c004****"</ResourceAttributeValue>
          </ResourceAttributes>
          <ResourceAttributes>
                <ResourceAttributeKey>PowerShellCurlCli</ResourceAttributeKey>
                <ResourceAttributeValue>curl -Uri "http://100.100.XX.XX/waitcondition?stack
name=test-describe-resource&amp;stackid=efdf5c10-96a5-4fd7-ab89-68e7baa2****&amp;resource=W aitConditionHandle&amp;expire=156468****&amp;signature=991d910a901a89db6580d74233119960c004
****" -Method Post -Headers @{"Content-Type"="application/json"; "Accept"="application/json
"; "x-acs-region-id"="cn-beijing"}</ResourceAttributeValue>
          </ResourceAttributes>
          <ResourceType>ALIYUN::ROS::WaitConditionHandle</ResourceType>
          <StackId>efdf5c10-96a5-4fd7-ab89-68e7baa2****</StackId>
          <StackName>test-describe-resource</StackName>
          <Status>UPDATE_COMPLETE</Status>
          <StatusReason>state changed</StatusReason>
          <UpdateTime>2019-08-01T06:01:29</UpdateTime>
          <DriftDetectionTime>2020-02-27T07:47:47</DriftDetectionTime>
          <ResourceDriftStatus>IN_SYNC</ResourceDriftStatus>
</GetStackResourceResponse>
```

`JSON` format `{`

```json
    "CreateTime": "2019-08-01T06:01:23",
    "Description": "",
    "LogicalResourceId": "WaitConditionHandle",
    "Metadata": {},
    "PhysicalResourceId": "",
    "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F",
    "ResourceAttributes": [
```

`{`

```json
            "ResourceAttributeKey": "CurlCli",
            "ResourceAttributeValue": "curl -i -X POST -H 'Content-Type: application/json'
-H 'Accept: application/json' -H 'x-acs-region-id: cn-beijing' http://100.100.XX.XX/waitcon dition?stackname=test-describe-resource\\&stackid=efdf5c10-96a5-4fd7-ab89-68e7baa2****\\&re source=WaitConditionHandle\\&expire=156468****\\&signature=991d910a901a89db6580d74233119960 c004****"
```

`},` `{`

```json
            "ResourceAttributeKey": "WindowsCurlCli",
            "ResourceAttributeValue": "curl -i -X POST -H \"Content-Type: application/json\
" -H \"Accept: application/json\" -H \"x-acs-region-id: cn-beijing\" \"http://100.100.XX.XX /waitcondition?stackname=test-describe-resource&stackid=efdf5c10-96a5-4fd7-ab89-68e7baa2*** *&resource=WaitConditionHandle&expire=156468****&signature=991d910a901a89db6580d74233119960 c004****\""
```

`},` `{`

```json
            "ResourceAttributeKey": "PowerShellCurlCli",
            "ResourceAttributeValue": "curl -Uri \"http://100.100.XX.XX/waitcondition?stack
name=test-describe-resource&stackid=efdf5c10-96a5-4fd7-ab89-68e7baa2****&resource=WaitCondi tionHandle&expire=156468****&signature=991d910a901a89db6580d74233119960c004****\" -Method P ost -Headers @{\"Content-Type\"=\"application/json\"; \"Accept\"=\"application/json\"; \"xacs-region-id\"=\"cn-beijing\"}"
```

`}` `],`

```json
    "ResourceType": "ALIYUN::ROS::WaitConditionHandle",
    "StackId": "efdf5c10-96a5-4fd7-ab89-68e7baa2****",
    "StackName": "test-describe-resource",
    "Status": "UPDATE_COMPLETE",
    "StatusReason": "state changed",
    "UpdateTime": "2019-08-01T06:01:29",
    "DriftDetectionTime": "2020-02-27T07:47:47",
    "ResourceDriftStatus": "IN_SYNC"
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | ResourceNotFound | The Resource ({name}) could not be found in Stack {stack}. | The error message returned because the specified resource does not exist in the stack. name indicates the resource name, and stack indicates the name or ID of the stack. |
| 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the specified stack does not exist. name indicates the name or ID of the stack. |

#### 1.8.4 GetResourceType

You can call this operation to query details about resource types. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetResourceType | The operation that you want to perform. Set the value to GetResourceType. |
| ResourceType | String | Yes | ALIYUN::ROS::Wa itConditionHandle | The type of the resource. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Attributes | Map | {"CurlCli": {},"PowerShellCurlCli ": {},"WindowsCurlCli": {}} | The attributes of the resource. |
| Properties | Map | {"Count": {},"Mode": {"Constraints": []}} | The properties of the resource. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | The ID of the request. |
| ResourceType | String | ALIYUN::ROS::WaitC onditionHandle | The type of the resource. |
| SupportDriftDe tection | Boolean | false | Indicates whether the resource supports drift detection. Valid values: true: The resource supports drift detection. false: The resource does not support drift detection. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=GetResourceType &ResourceType=ALIYUN::SLB::LoadBalancer &<Common request parameters>
```

Sample success responses `XML` format

```xml
<GetResourceTypeResponse>
       <Attributes class="object">
              <CurlCli class="object">
                     <Description type="string">Convenience attribute, provides curl CLI co
mmand prefix, which can be used for signalling handle completion or failure. You can signa l success by adding --data-binary '{"status": "SUCCESS"}' , or signal failure by adding --d ata-binary '{"status": "FAILURE"}'</Description>
              </CurlCli>
              <PowerShellCurlCli class="object">
                     <Description type="string">Convenience attribute, provides curl CLI co
mmand prefix for PowerShell, which can be used for signalling handle completion or failure. As this cmdlet was introduced in PowerShell 3.0, ensure the version of PowerShell satisfies the constraint. (Show the version via $PSVersionTable.PSVersion.) You can signal success by adding -Body '{"status": "SUCCESS"}' , or signal failure by adding -Body '{"status": "FAILU RE"}' </Description>
              </PowerShellCurlCli>
              <WindowsCurlCli class="object">
                     <Description type="string">Convenience attribute, provides curl CLI co
mmand prefix for Windows, which can be used for signalling handle completion or failure. As Windows does not support curl command, you need to install curl.exe and add it to PATH firs t. You can signal success by adding --data-binary "{\"status\": \"SUCCESS\"}" , or signal f ailure by adding --data-binary "{\"status\": \"FAILURE\"}" </Description>
              </WindowsCurlCli>
       </Attributes>
<Propertiesclass="object">
```

```
       <Properties class
object>
              <Count class="object">
                     <Default type="number">-1</Default>
                     <Description type="string">There are 3 preconditions that make Count t
aking effect: 1.Mode is set to Full. 2.Count &gt;= 0. 3.The id of signal is not specified. If so, it will be a self-increasing integer started fr om 1. For example, the id of the first signal is 1, the id of the second signal is 2, and s o on. If Count takes effect, signals with id &gt; Count will be deleted before update. The default value is -1, which means no effect. It is recommended to quote the same value with WaitCondition.Count. </Description>
                     <Immutable type="boolean">false</Immutable>
                     <Required type="boolean">false</Required>
                     <Type type="string">integer</Type>
                     <UpdateAllowed type="boolean">true</UpdateAllowed>
              </Count>
              <Mode class="object">
                     <Constraints class="array">
                            <e class="object">
                                   <AllowedValues class="array">
                                          <e type="string">Increment</e>
                                          <e type="string">Full</e>
                                   </AllowedValues>
                            </e>
                     </Constraints>
                     <Default type="string">Full</Default>
                     <Description type="string">If set to Increment, all old signals will b
e deleted before update. In this mode, WaitCondition.Count should reference an incremental value instead of a full value, such as ScalingGroupEnable.ScalingRuleArisExecuteResultNumbe rOfAddedInstances. If set to Full, no old signal will be deleted unless Count is set. In this mode, WaitCondit ion.Count should reference a full value, such as the same value with InstanceGroup.MaxAmoun t. It is recommended to use this mode with Count. Default to Full. </Description>
                     <Immutable type="boolean">false</Immutable>
                     <Required type="boolean">false</Required>
                     <Type type="string">string</Type>
                     <UpdateAllowed type="boolean">true</UpdateAllowed>
              </Mode>
       </Properties>
       <RequestId type="string">BA4C8BF3-482E-4B03-A1E3-C60DB7A95DE0</RequestId>
       <ResourceType type="string">ALIYUN::ROS::WaitConditionHandle</ResourceType>
       <SupportDriftDetection type="boolean">false</SupportDriftDetection>
</GetResourceTypeResponse>
```

`JSON` format `{`

```json
    "Attributes": {
        "CurlCli": {
            "Description": "Convenience attribute, provides curl CLI command prefix, which
can be used for signalling handle completion or failure. You can signal success by adding
```

```
--data-binary '{\"status\": \"SUCCESS\"}' , or signal failure by adding --data-binary '{\"s tatus\": \"FAILURE\"}'"
```

`},`

```json
        "PowerShellCurlCli": {
            "Description": "Convenience attribute, provides curl CLI command prefix for Pow
erShell, which can be used for signalling handle completion or failure. As this cmdlet was introduced in PowerShell 3.0, ensure the version of PowerShell satisfies the constraint. (S how the version via $PSVersionTable.PSVersion.) You can signal success by adding -Body '{\" status\": \"SUCCESS\"}' , or signal failure by adding -Body '{\"status\": \"FAILURE\"}' "
```

`},`

```json
        "WindowsCurlCli": {
            "Description": "Convenience attribute, provides curl CLI command prefix for Win
dows, which can be used for signalling handle completion or failure. As Windows does not su pport curl command, you need to install curl.exe and add it to PATH first. You can signal s uccess by adding --data-binary \"{\\\"status\\\": \\\"SUCCESS\\\"}\" , or signal failure by adding --data-binary \"{\\\"status\\\": \\\"FAILURE\\\"}\" "
```

`}` `},`

```json
    "Properties": {
        "Count": {
            "Default": -1,
            "Description": "There are 3 preconditions that make Count taking effect:\n1.Mod
e is set to Full.\n2.Count >= 0.\n3.The id of signal is not specified. If so, it will be a self-increasing integer started from 1. For example, the id of the first signal is 1, the i d of the second signal is 2, and so on.\n\nIf Count takes effect, signals with id > Count w ill be deleted before update.\nThe default value is -1, which means no effect.\nIt is recom mended to quote the same value with WaitCondition.Count.",
            "Immutable": false,
            "Required": false,
            "Type": "integer",
            "UpdateAllowed": true
```

`},`

```json
        "Mode": {
            "Constraints": [
```

`{`

```json
                    "AllowedValues": [
                        "Increment",
                        "Full"
```

`]` `}` `],`

```json
            "Default": "Full",
            "Description": "If set to Increment, all old signals will be deleted before upd
ate. In this mode, WaitCondition.Count should reference an incremental value instead of a f ull value, such as ScalingGroupEnable.ScalingRuleArisExecuteResultNumberOfAddedInstances.\n \nIf set to Full, no old signal will be deleted unless Count is set. In this mode, WaitCond ition.Count should reference a full value, such as the same value with InstanceGroup.MaxAmo unt. It is recommended to use this mode with Count.\n\nDefault to Full.",
            "Immutable": false,
            "Required": false,
            "Type": "string",
            "UpdateAllowed": true
```

`}` `},`

```
"ReqestId" "BA4C8BF3482E4B03A1E3C60DB7A95DE0"
```

```json
    "RequestId": "BA4C8BF3-482E-4B03-A1E3-C60DB7A95DE0",
    "ResourceType": "ALIYUN::ROS::WaitConditionHandle",
    "SupportDriftDetection": false
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | ResourceTypeNotFound | The Resource Type ({name}) could not be found. | The error message returned because the specified resource type does not exist. name indicates the name of the resource type. |

#### 1.8.5 ListResourceTypes

Queries the list of supported resource types. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListResourceType s | The operation that you want to perform. Set the value to ListResourceTypes. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | The ID of the request. |
| ResourceTypes | List | ["ALIYUN::ECS::Insta nce","ALIYUN::RDS:: Instance"] | The array of resource types. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/?Action=ListResourceTypes &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ListResorceTpesResponse>
```

|   | <ListResourceTypesResponse> <RequestId type="string">B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId> <ResourceTypes class="array"> <ResourceType type="string">ALIYUN::ACTIONTRAIL::Trail</ResourceType> <ResourceType type="string">ALIYUN::ACTIONTRAIL::TrailLogging</ResourceType> <ResourceType type="string">ALIYUN::ApiGateway::Api</ResourceType> <ResourceType type="string">ALIYUN::ApiGateway::App</ResourceType> <ResourceType type="string">ALIYUN::ApiGateway::Authorization</ResourceType> <ResourceType type="string">ALIYUN::ApiGateway::CustomDomain</ResourceType> <ResourceType type="string">ALIYUN::ApiGateway::Deployment</ResourceType> <ResourceType type="string">ALIYUN::ApiGateway::Group</ResourceType> <ResourceType type="string">ALIYUN::ApiGateway::Signature</ResourceType> <ResourceType type="string">ALIYUN::ApiGateway::SignatureBinding</ResourceTyp e> <ResourceType type="string">ALIYUN::ApiGateway::StageConfig</ResourceType> <ResourceType type="string">ALIYUN::ApiGateway::TrafficControl</ResourceType> <ResourceType type="string">ALIYUN::ApiGateway::TrafficControlBinding</Resour ceType> <ResourceType type="string">ALIYUN::ApiGateway::VpcAccessConfig</ResourceType > <ResourceType type="string">ALIYUN::BSS::WaitOrder</ResourceType> <ResourceType type="string">ALIYUN::CDN::Domain</ResourceType> <ResourceType type="string">ALIYUN::CDN::DomainConfig</ResourceType> <ResourceType type="string">ALIYUN::CEN::CenBandwidthLimit</ResourceType> <ResourceType type="string">ALIYUN::CEN::CenBandwidthPackage</ResourceType> <ResourceType type="string">ALIYUN::CEN::CenBandwidthPackageAssociation</Reso urceType> <ResourceType type="string">ALIYUN::CEN::CenInstance</ResourceType> <ResourceType type="string">ALIYUN::CEN::CenInstanceAttachment</ResourceType> <ResourceType type="string">ALIYUN::CEN::RouteEntry</ResourceType> <ResourceType type="string">ALIYUN::CS::App</ResourceType> <ResourceType type="string">ALIYUN::CS::Cluster</ResourceType> <ResourceType type="string">ALIYUN::DEBUG::Apple</ResourceType> <ResourceType type="string">ALIYUN::DEBUG::Dummy</ResourceType> <ResourceType type="string">ALIYUN::DEBUG::Failure</ResourceType> <ResourceType type="string">ALIYUN::DEBUG::Secret</ResourceType> <ResourceType type="string">ALIYUN::DEBUG::Update</ResourceType> <ResourceType type="string">ALIYUN::DNS::Domain</ResourceType> <ResourceType type="string">ALIYUN::DNS::DomainGroup</ResourceType> <ResourceType type="string">ALIYUN::DNS::DomainRecord</ResourceType> <ResourceType type="string">ALIYUN::ECS::AutoSnapshotPolicy</ResourceType> <ResourceType type="string">ALIYUN::ECS::BandwidthPackage</ResourceType> <ResourceType type="string">ALIYUN::ECS::Command</ResourceType> <ResourceType type="string">ALIYUN::ECS::CopyImage</ResourceType> <ResourceType type="string">ALIYUN::ECS::CustomImage</ResourceType> <ResourceType type="string">ALIYUN::ECS::DedicatedHost</ResourceType> <ResourceType type="string">ALIYUN::ECS::DeploymentSet</ResourceType> <ResourceType type="string">ALIYUN::ECS::Disk</ResourceType> <ResourceType type="string">ALIYUN::ECS::DiskAttachment</ResourceType> <ResourceType type="string">ALIYUN::ECS::ForwardEntry</ResourceType> <ResourceType type="string">ALIYUN::ECS::Instance</ResourceType> <ResourceType type="string">ALIYUN::ECS::InstanceClone</ResourceType> <ResourceType type="string">ALIYUN::ECS::InstanceGroup</ResourceType> <ResourceType type="string">ALIYUN::ECS::InstanceGroupClone</ResourceType> <ResourceType type="string">ALIYUN::ECS::Invocation</ResourceType> |   |
|---|---|---|

```
              <ResourceType type
string>ALIYUN::ECS::Invocation</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::JoinSecurityGroup</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::LaunchTemplate</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::NatGateway</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::NetworkInterface</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::NetworkInterfaceAttachment</Resource
Type>
              <ResourceType type="string">ALIYUN::ECS::NetworkInterfacePermission</Resource
Type>
              <ResourceType type="string">ALIYUN::ECS::PrepayInstance</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::PrepayInstanceGroupClone</ResourceTy
pe>
              <ResourceType type="string">ALIYUN::ECS::Route</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::SNatEntry</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::SSHKeyPair</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::SSHKeyPairAttachment</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::SecurityGroup</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::SecurityGroupClone</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::SecurityGroupEgress</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::SecurityGroupIngress</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::Snapshot</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::VPC</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::VSwitch</ResourceType>
              <ResourceType type="string">ALIYUN::ESS::AlarmTask</ResourceType>
              <ResourceType type="string">ALIYUN::ESS::AlarmTaskEnable</ResourceType>
              <ResourceType type="string">ALIYUN::ESS::LifecycleHook</ResourceType>
              <ResourceType type="string">ALIYUN::ESS::ScalingConfiguration</ResourceType>
              <ResourceType type="string">ALIYUN::ESS::ScalingGroup</ResourceType>
              <ResourceType type="string">ALIYUN::ESS::ScalingGroupEnable</ResourceType>
              <ResourceType type="string">ALIYUN::ESS::ScalingRule</ResourceType>
              <ResourceType type="string">ALIYUN::ESS::ScheduledTask</ResourceType>
              <ResourceType type="string">ALIYUN::FC::Function</ResourceType>
              <ResourceType type="string">ALIYUN::FC::FunctionInvoker</ResourceType>
              <ResourceType type="string">ALIYUN::FC::Service</ResourceType>
              <ResourceType type="string">ALIYUN::FC::Trigger</ResourceType>
              <ResourceType type="string">ALIYUN::KMS::Alias</ResourceType>
              <ResourceType type="string">ALIYUN::KMS::Key</ResourceType>
              <ResourceType type="string">ALIYUN::MEMCACHE::Instance</ResourceType>
              <ResourceType type="string">ALIYUN::MNS::Queue</ResourceType>
              <ResourceType type="string">ALIYUN::MNS::Subscription</ResourceType>
              <ResourceType type="string">ALIYUN::MNS::Topic</ResourceType>
              <ResourceType type="string">ALIYUN::MONGODB::Instance</ResourceType>
              <ResourceType type="string">ALIYUN::MONGODB::PrepayInstance</ResourceType>
              <ResourceType type="string">ALIYUN::MarketPlace::Image</ResourceType>
              <ResourceType type="string">ALIYUN::MarketPlace::Order</ResourceType>
              <ResourceType type="string">ALIYUN::NAS::AccessGroup</ResourceType>
              <ResourceType type="string">ALIYUN::NAS::AccessRule</ResourceType>
              <ResourceType type="string">ALIYUN::NAS::FileSystem</ResourceType>
              <ResourceType type="string">ALIYUN::NAS::MountTarget</ResourceType>
              <ResourceType type="string">ALIYUN::OSS::Bucket</ResourceType>
              <ResourceType type="string">ALIYUN::OTS::Instance</ResourceType>
              <ResourceType type="string">ALIYUN::OTS::VpcBinder</ResourceType>
              <ResourceType type="string">ALIYUN::PVTZ::Zone</ResourceType>
              <ResourceType type="string">ALIYUN::PVTZ::ZoneRecord</ResourceType>
              <ResourceType type="string">ALIYUN::PVTZ::ZoneVpcBinder</ResourceType>
```

`yp` `yp` `g` `p` `yp`

```
              <ResourceType type="string">ALIYUN::RAM::AccessKey</ResourceType>
              <ResourceType type="string">ALIYUN::RAM::AttachPolicyToRole</ResourceType>
              <ResourceType type="string">ALIYUN::RAM::Group</ResourceType>
              <ResourceType type="string">ALIYUN::RAM::ManagedPolicy</ResourceType>
              <ResourceType type="string">ALIYUN::RAM::Role</ResourceType>
              <ResourceType type="string">ALIYUN::RAM::User</ResourceType>
              <ResourceType type="string">ALIYUN::RAM::UserToGroupAddition</ResourceType>
              <ResourceType type="string">ALIYUN::RDS::Account</ResourceType>
              <ResourceType type="string">ALIYUN::RDS::AccountPrivilege</ResourceType>
              <ResourceType type="string">ALIYUN::RDS::DBInstance</ResourceType>
              <ResourceType type="string">ALIYUN::RDS::DBInstanceParameterGroup</ResourceTy
pe>
              <ResourceType type="string">ALIYUN::RDS::DBInstanceSecurityIps</ResourceType>
              <ResourceType type="string">ALIYUN::RDS::PrepayDBInstance</ResourceType>
              <ResourceType type="string">ALIYUN::REDIS::Instance</ResourceType>
              <ResourceType type="string">ALIYUN::REDIS::PrepayInstance</ResourceType>
              <ResourceType type="string">ALIYUN::ROS::Stack</ResourceType>
              <ResourceType type="string">ALIYUN::ROS::WaitCondition</ResourceType>
              <ResourceType type="string">ALIYUN::ROS::WaitConditionHandle</ResourceType>
              <ResourceType type="string">ALIYUN::SAG::ACL</ResourceType>
              <ResourceType type="string">ALIYUN::SAG::ACLAssociation</ResourceType>
              <ResourceType type="string">ALIYUN::SAG::ACLRule</ResourceType>
              <ResourceType type="string">ALIYUN::SAG::CloudConnectNetwork</ResourceType>
              <ResourceType type="string">ALIYUN::SAG::SmartAccessGatewayBinding</ResourceT
ype>
              <ResourceType type="string">ALIYUN::SLB::AccessControl</ResourceType>
              <ResourceType type="string">ALIYUN::SLB::BackendServerAttachment</ResourceTyp
```

`e>`

```
              <ResourceType type="string">ALIYUN::SLB::BackendServerToVServerGroupAddition<
/ResourceType>
              <ResourceType type="string">ALIYUN::SLB::Certificate</ResourceType>
              <ResourceType type="string">ALIYUN::SLB::DomainExtension</ResourceType>
              <ResourceType type="string">ALIYUN::SLB::Listener</ResourceType>
              <ResourceType type="string">ALIYUN::SLB::LoadBalancer</ResourceType>
              <ResourceType type="string">ALIYUN::SLB::LoadBalancerClone</ResourceType>
              <ResourceType type="string">ALIYUN::SLB::MasterSlaveServerGroup</ResourceType
```

`>`

```
              <ResourceType type="string">ALIYUN::SLB::Rule</ResourceType>
              <ResourceType type="string">ALIYUN::SLB::VServerGroup</ResourceType>
              <ResourceType type="string">ALIYUN::SLS::ApplyConfigToMachineGroup</ResourceT
ype>
              <ResourceType type="string">ALIYUN::SLS::MachineGroup</ResourceType>
              <ResourceType type="string">ALIYUN::UIS::Uis</ResourceType>
              <ResourceType type="string">ALIYUN::UIS::UisConnection</ResourceType>
              <ResourceType type="string">ALIYUN::UIS::UisNode</ResourceType>
              <ResourceType type="string">ALIYUN::VPC::EIP</ResourceType>
              <ResourceType type="string">ALIYUN::VPC::EIPAssociation</ResourceType>
              <ResourceType type="string">ALIYUN::VPC::PeeringRouterInterfaceBinding</Resou
rceType>
              <ResourceType type="string">ALIYUN::VPC::PeeringRouterInterfaceConnection</Re
sourceType>
              <ResourceType type="string">ALIYUN::VPC::RouterInterface</ResourceType>
              <ResourceType type="string">ALIYUN::VPC::SnatEntry</ResourceType>
       </ResourceTypes>
```

```
</ListResourceTypesResponse>
```

`JSON` format `{`

```json
   "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F",
   "ResourceTypes": [
       "ALIYUN::ACTIONTRAIL::Trail",
       "ALIYUN::ACTIONTRAIL::TrailLogging",
       "ALIYUN::ApiGateway::Api",
       "ALIYUN::ApiGateway::App",
       "ALIYUN::ApiGateway::Authorization",
       "ALIYUN::ApiGateway::CustomDomain",
       "ALIYUN::ApiGateway::Deployment",
       "ALIYUN::ApiGateway::Group",
       "ALIYUN::ApiGateway::Signature",
       "ALIYUN::ApiGateway::SignatureBinding",
       "ALIYUN::ApiGateway::StageConfig",
       "ALIYUN::ApiGateway::TrafficControl",
       "ALIYUN::ApiGateway::TrafficControlBinding",
       "ALIYUN::ApiGateway::VpcAccessConfig",
       "ALIYUN::BSS::WaitOrder",
       "ALIYUN::CDN::Domain",
       "ALIYUN::CDN::DomainConfig",
       "ALIYUN::CEN::CenBandwidthLimit",
       "ALIYUN::CEN::CenBandwidthPackage",
       "ALIYUN::CEN::CenBandwidthPackageAssociation",
       "ALIYUN::CEN::CenInstance",
       "ALIYUN::CEN::CenInstanceAttachment",
       "ALIYUN::CEN::RouteEntry",
       "ALIYUN::CS::App",
       "ALIYUN::CS::Cluster",
       "ALIYUN::DEBUG::Apple",
       "ALIYUN::DEBUG::Dummy",
       "ALIYUN::DEBUG::Failure",
       "ALIYUN::DEBUG::Secret",
       "ALIYUN::DEBUG::Update",
       "ALIYUN::DNS::Domain",
       "ALIYUN::DNS::DomainGroup",
       "ALIYUN::DNS::DomainRecord",
       "ALIYUN::ECS::AutoSnapshotPolicy",
       "ALIYUN::ECS::BandwidthPackage",
       "ALIYUN::ECS::Command",
       "ALIYUN::ECS::CopyImage",
       "ALIYUN::ECS::CustomImage",
       "ALIYUN::ECS::DedicatedHost",
       "ALIYUN::ECS::DeploymentSet",
       "ALIYUN::ECS::Disk",
       "ALIYUN::ECS::DiskAttachment",
       "ALIYUN::ECS::ForwardEntry",
       "ALIYUN::ECS::Instance",
       "ALIYUN::ECS::InstanceClone",
       "ALIYUN::ECS::InstanceGroup",
"ALIYUN::ECS::InstanceGroupClone",
```

```
       ALIYUN::ECS::InstanceGroupClone,
       "ALIYUN::ECS::Invocation",
       "ALIYUN::ECS::JoinSecurityGroup",
       "ALIYUN::ECS::LaunchTemplate",
       "ALIYUN::ECS::NatGateway",
       "ALIYUN::ECS::NetworkInterface",
       "ALIYUN::ECS::NetworkInterfaceAttachment",
       "ALIYUN::ECS::NetworkInterfacePermission",
       "ALIYUN::ECS::PrepayInstance",
       "ALIYUN::ECS::PrepayInstanceGroupClone",
       "ALIYUN::ECS::Route",
       "ALIYUN::ECS::SNatEntry",
       "ALIYUN::ECS::SSHKeyPair",
       "ALIYUN::ECS::SSHKeyPairAttachment",
       "ALIYUN::ECS::SecurityGroup",
       "ALIYUN::ECS::SecurityGroupClone",
       "ALIYUN::ECS::SecurityGroupEgress",
       "ALIYUN::ECS::SecurityGroupIngress",
       "ALIYUN::ECS::Snapshot",
       "ALIYUN::ECS::VPC",
       "ALIYUN::ECS::VSwitch",
       "ALIYUN::ESS::AlarmTask",
       "ALIYUN::ESS::AlarmTaskEnable",
       "ALIYUN::ESS::LifecycleHook",
       "ALIYUN::ESS::ScalingConfiguration",
       "ALIYUN::ESS::ScalingGroup",
       "ALIYUN::ESS::ScalingGroupEnable",
       "ALIYUN::ESS::ScalingRule",
       "ALIYUN::ESS::ScheduledTask",
       "ALIYUN::FC::Function",
       "ALIYUN::FC::FunctionInvoker",
       "ALIYUN::FC::Service",
       "ALIYUN::FC::Trigger",
       "ALIYUN::KMS::Alias",
       "ALIYUN::KMS::Key",
       "ALIYUN::MEMCACHE::Instance",
       "ALIYUN::MNS::Queue",
       "ALIYUN::MNS::Subscription",
       "ALIYUN::MNS::Topic",
       "ALIYUN::MONGODB::Instance",
       "ALIYUN::MONGODB::PrepayInstance",
       "ALIYUN::MarketPlace::Image",
       "ALIYUN::MarketPlace::Order",
       "ALIYUN::NAS::AccessGroup",
       "ALIYUN::NAS::AccessRule",
       "ALIYUN::NAS::FileSystem",
       "ALIYUN::NAS::MountTarget",
       "ALIYUN::OSS::Bucket",
       "ALIYUN::OTS::Instance",
       "ALIYUN::OTS::VpcBinder",
       "ALIYUN::PVTZ::Zone",
       "ALIYUN::PVTZ::ZoneRecord",
       "ALIYUN::PVTZ::ZoneVpcBinder",
       "ALIYUN::RAM::AccessKey",
       "ALIYUN::RAM::AttachPolicyToRole",
```

`y` `,`

```
       "ALIYUN::RAM::Group",
       "ALIYUN::RAM::ManagedPolicy",
       "ALIYUN::RAM::Role",
       "ALIYUN::RAM::User",
       "ALIYUN::RAM::UserToGroupAddition",
       "ALIYUN::RDS::Account",
       "ALIYUN::RDS::AccountPrivilege",
       "ALIYUN::RDS::DBInstance",
       "ALIYUN::RDS::DBInstanceParameterGroup",
       "ALIYUN::RDS::DBInstanceSecurityIps",
       "ALIYUN::RDS::PrepayDBInstance",
       "ALIYUN::REDIS::Instance",
       "ALIYUN::REDIS::PrepayInstance",
       "ALIYUN::ROS::Stack",
       "ALIYUN::ROS::WaitCondition",
       "ALIYUN::ROS::WaitConditionHandle",
       "ALIYUN::SAG::ACL",
       "ALIYUN::SAG::ACLAssociation",
       "ALIYUN::SAG::ACLRule",
       "ALIYUN::SAG::CloudConnectNetwork",
       "ALIYUN::SAG::SmartAccessGatewayBinding",
       "ALIYUN::SLB::AccessControl",
       "ALIYUN::SLB::BackendServerAttachment",
       "ALIYUN::SLB::BackendServerToVServerGroupAddition",
       "ALIYUN::SLB::Certificate",
       "ALIYUN::SLB::DomainExtension",
       "ALIYUN::SLB::Listener",
       "ALIYUN::SLB::LoadBalancer",
       "ALIYUN::SLB::LoadBalancerClone",
       "ALIYUN::SLB::MasterSlaveServerGroup",
       "ALIYUN::SLB::Rule",
       "ALIYUN::SLB::VServerGroup",
       "ALIYUN::SLS::ApplyConfigToMachineGroup",
       "ALIYUN::SLS::MachineGroup",
       "ALIYUN::UIS::Uis",
       "ALIYUN::UIS::UisConnection",
       "ALIYUN::UIS::UisNode",
       "ALIYUN::VPC::EIP",
       "ALIYUN::VPC::EIPAssociation",
       "ALIYUN::VPC::PeeringRouterInterfaceBinding",
       "ALIYUN::VPC::PeeringRouterInterfaceConnection",
       "ALIYUN::VPC::RouterInterface",
       "ALIYUN::VPC::SnatEntry"
```

`]` `}`

### 1.9 Template operations

#### 1.9.1 GetTemplateEstimateCost

You can call this operation to query estimated prices of resources to be created based on a template. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetTemplateEsti mateCost | The operation that you want to perform. Set the value to GetTemplateEstimateCost. |
| Parameters.N.Par ameterKey | String | Yes | InstanceId | The key of parameter N. If the key and value of the parameter are not specified, the key and value specified in the template are used. Maximum value of N: 200. Not e Parameters is an optional parameter. If you need to specify Parameters, you must specify both Parameters.N.ParameterKe y and Parameters.N.ParameterVa lue. |
| Parameters.N.Par ameterValue | String | Yes | i- m5e3tfdbinchnex h**** | The value of parameter N. Maximum value of N: 200. Not e Parameters is an optional parameter. If you need to specify Parameters, you must specify both Parameters.N.ParameterKe y and Parameters.N.ParameterVa lue. |
| RegionId | String | Yes | cn-beijing | The region ID of the stack. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TemplateURL | String | No | oss://ros- template/demo | The URL of the file that contains the template body. The URL must point to a template located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/template/demo and oss://ros/template/demo? RegionId=cn-hangzhou. The template can be up to 524,288 bytes in length, and the URL can be up to 1,024 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |
| TemplateBody | String | No | {"ROSTemplateFo rmatVersion": "2015-09-01"} | The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body is longer than required, we recommend that you add parameters to the HTTP POST request body to avoid request failures due to excessive length of URLs. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 42665544**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can be up to 64 characters in length and can contain letters, digits, hyphens (-), and underscores ( ). _ |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Resources | Map | The parameters in the Resources section | The details about resources. |
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | The ID of the request. |

The following table describes the parameters in the Resources section.

| Parameter | Type | Example | Description |
|---|---|---|---|
| Order |   |   | Details about the order. |
| Currency | String | CNY | The currency unit. |
| DiscountAmount | Long | 100 | The discount. |
| HandlingFeeAmount | Long | 0 | The service fee. |
| OptionalMixPromotions | Array | [] | The available mixed discounts. |
| OptionalPromotions | Array | [] | The available discounts. |
| OrderLines | String |   | The order information. |
| OriginalAmount | Long | 200 | The original price of the service. |
| RiCycleAmount | Long | 0 | The deducted amount of money. |
| RuleIds | Array | [100000****] | The list of one or more IDs of the discount rules. |
| TaxAmount | Long | 0 | The amount of tax. |

| esource Orchestration Serv | ice | Dev | eloper Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| TradeAmount | Long | 100 | The final price after the discount. |
| Rules |   |   | Details about the discount rules. |
| Name | String | Get 15% off a 1-year subscription | The name of the discount rule. |
| RuleDescId | Long | 100000**** | The ID of the discount rule. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=GetTemplateEstimateCost &RegionId=cn-beijing &Parameters.1.ParameterKey=InstanceId &Parameters.1.ParameterValue=i-m5e3tfdbinchnexh**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Resources>
    <NewEip>
        <Result>
            <Order>
                <Currency>CNY</Currency>
                <DiscountAmount>2.4</DiscountAmount>
                <HandlingFeeAmount>0</HandlingFeeAmount>
                <OrderLines/>
                <OriginalAmount>2.4</OriginalAmount>
                <RiCycleAmount>0</RiCycleAmount>
                <RuleIds>100000****</RuleIds>
                <TaxAmount>0</TaxAmount>
                <TradeAmount>0</TradeAmount>
            </Order>
            <Rules>
                <Rule>
                    <Name>Get 15% off a 1-year subscription</Name>
                    <RuleDescId>100000****</RuleDescId>
                </Rule>
            </Rules>
        </Result>
        <Success>true</Success>
        <Type>ALIYUN::VPC::EIP</Type>
    </NewEip>
</Resources> <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
```

`JSON` format `{`

```json
    "Resources": {
        "NewEip": {
            "Result": {
                "Order": {
                    "Currency": "CNY",
                    "DiscountAmount": 2.4,
                    "HandlingFeeAmount": 0,
                    "OptionalMixPromotions": [],
                    "OptionalPromotions": [],
                    "OrderLines": null,
                    "OriginalAmount": 2.4,
                    "RiCycleAmount": 0,
                    "RuleIds": [
                        100000****
```

`],`

```json
                    "TaxAmount": 0,
                    "TradeAmount": 0
```

`},`

```json
                "Rules": {
                    "Rule": [
```

`{`

```json
                            "Name": "Get 15% off a 1-year subscription",
                            "RuleDescId": 100000****
```

`}` `]` `}` `},`

```json
            "Success": true,
            "Type": "ALIYUN::VPC::EIP"
```

`}` `},`

```json
    "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F"
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | CircularDependency | Circular Dependency Found: {reason}. | The error message returned because the template contains a circular dependency. reason indicates the specific reason. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidSchema | {reason}. | The error message returned because the specified template format is invalid. reason indicates the specific reason. |
| 400 | InvalidTemplateAttribut e | The Referenced Attribute ({resource} {name}) is incorrect. | The error message returned because the resource attribute referenced in the template is invalid. resource indicates the resource name, and name indicates the attribute name. |
| 400 | InvalidTemplatePropert yType | The specified value type of ({resource} {section}) is incorrect. | The error message returned because the type of the specified resource section defined in the template is invalid. resource indicates the resource name, and section indicates the section name. |
| 400 | InvalidTemplateReferen ce | The specified reference "{name}" (in {referencer}) is incorrect. | The error message returned because the template contains an invalid reference. name indicates the reference name, and referencer indicates the referencer name. |
| 400 | InvalidTemplateSection | The template section is invalid: {section}. | The error message returned because the template contains an invalid property. section indicates the section name. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidTemplateVersion | The template version is invalid: {reason}. | The error message returned because the template version is invalid. reason indicates the specific reason. |
| 400 | StackValidationFailed | {reason}. | The error message returned because the stack validation failed. reason indicates the specific reason. |
| 400 | UnknownUserParameter | The Parameter ({name}) was not defined in template. | The error message returned because the specified parameter is not defined in the template. name indicates the parameter key. |
| 400 | UserParameterMissing | The Parameter {name} was not provided. | The error message returned because no value is passed into the specified parameter defined in the template. name indicates the parameter key. |

#### 1.9.2 ValidateTemplate

You can call this operation to validate the template that is used to create stacks. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ValidateTemplat e | The operation that you want to perform. Set the value to ValidateTemplate. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TemplateURL | String | No | oss://ros/templ ate/demo | The URL of the file that contains the template body. The URL must point to a template located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/template/demo and oss://ros/template/demo? RegionId=cn-hangzhou. The template can be up to 524,288 bytes in length, and the URL can be up to 1,024 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |
| RegionId | String | No | cn-hangzhou | The region ID of the stack template. |
| TemplateBody | String | No | {"ROSTemplateFo rmatVersion":"20 15-09-01"} | The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body is longer than required, we recommend that you add parameters to the HTTP POST request body to avoid request failures due to excessive length of URLs. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Description | String | No description | The description of the stack template. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Parameters | List | [{"Description": "", "Label": "param integer", _ "NoEcho": "false", "ParameterKey": "param integer", _ "Type": "Number"},{ "Description": "", "Label": "param float", _ "NoEcho": "false", "ParameterKey": "param float", _ "Type": "Number"}] | The input parameters of the stack template. The input parameters define the parameters that you must specify to create stacks based on the template. These parameters specify information about a stack, such as the username, password, and environment- related ECS instance type. |
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | The ID of the request. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=ValidateTemplate &TemplateURL=oss://ros/template/demo &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ValidateTemplateResponse>
       <Description type="string">No description</Description>
       <Parameters class="array">
              <Parameter class="object">
                     <Description type="string"></Description>
                     <Label type="string">param_integer</Label>
                     <NoEcho type="string">false</NoEcho>
                     <ParameterKey type="string">param_integer</ParameterKey>
                     <Type type="string">Number</Type>
              </Parameter>
              <Parameter class="object">
                     <Description type="string"></Description>
                     <Label type="string">param_float</Label>
                     <NoEcho type="string">false</NoEcho>
                     <ParameterKey type="string">param_float</ParameterKey>
                     <Type type="string">Number</Type>
              </Parameter>
              <Parameter class="object">
                     <Description type="string"></Description>
                     <Label type="string">param_bool</Label>
                     <NoEcho type="string">false</NoEcho>
<ParameterKe tpe"string">parambool</ParameterKe>
```

```
                     <ParameterKey type="string">param_bool</ParameterKey>
                     <Type type="string">Boolean</Type>
              </Parameter>
              <Parameter class="object">
                     <Description type="string"></Description>
                     <Label type="string">param_json_list</Label>
                     <NoEcho type="string">false</NoEcho>
                     <ParameterKey type="string">param_json_list</ParameterKey>
                     <Type type="string">Json</Type>
              </Parameter>
              <Parameter class="object">
                     <Default class="object">
                            <c class="array"></c>
                     </Default>
                     <Description type="string"></Description>
                     <Label type="string">param_has_default</Label>
                     <NoEcho type="string">false</NoEcho>
                     <ParameterKey type="string">param_has_default</ParameterKey>
                     <Type type="string">Json</Type>
              </Parameter>
              <Parameter class="object">
                     <Description type="string"></Description>
                     <Label type="string">UpdateVersion</Label>
                     <NoEcho type="string">false</NoEcho>
                     <ParameterKey type="string">UpdateVersion</ParameterKey>
                     <Type type="string">Number</Type>
              </Parameter>
              <Parameter class="object">
                     <Description type="string"></Description>
                     <Label type="string">param_str</Label>
                     <NoEcho type="string">false</NoEcho>
                     <ParameterKey type="string">param_str</ParameterKey>
                     <Type type="string">String</Type>
              </Parameter>
              <Parameter class="object">
                     <Description type="string"></Description>
                     <Label type="string">param_list</Label>
                     <NoEcho type="string">false</NoEcho>
                     <ParameterKey type="string">param_list</ParameterKey>
                     <Type type="string">CommaDelimitedList</Type>
              </Parameter>
              <Parameter class="object">
                     <Description type="string"></Description>
                     <Label type="string">param_json_dict</Label>
                     <NoEcho type="string">false</NoEcho>
                     <ParameterKey type="string">param_json_dict</ParameterKey>
                     <Type type="string">Json</Type>
              </Parameter>
       </Parameters>
       <RequestId type="string">B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
</ValidateTemplateResponse>
```

`JSON` format `{`

```json
   "Description": "No description",
   "Parameters": [
```

`{`

```json
           "Description": "",
           "Label": "param_integer",
           "NoEcho": "false",
           "ParameterKey": "param_integer",
           "Type": "Number"
```

`},` `{`

```json
           "Description": "",
           "Label": "param_float",
           "NoEcho": "false",
           "ParameterKey": "param_float",
           "Type": "Number"
```

`},` `{`

```json
           "Description": "",
           "Label": "param_bool",
           "NoEcho": "false",
           "ParameterKey": "param_bool",
           "Type": "Boolean"
```

`},` `{`

```json
           "Description": "",
           "Label": "param_json_list",
           "NoEcho": "false",
           "ParameterKey": "param_json_list",
           "Type": "Json"
```

`},` `{`

```json
           "Default": {
               "c": []
```

`},`

```json
           "Description": "",
           "Label": "param_has_default",
           "NoEcho": "false",
           "ParameterKey": "param_has_default",
           "Type": "Json"
```

`},` `{`

```json
           "Description": "",
           "Label": "UpdateVersion",
           "NoEcho": "false",
           "ParameterKey": "UpdateVersion",
           "Type": "Number"
```

`},` `{`

```json
           "Description": "",
           "Label": "param_str",
           "NoEcho": "false",
           "ParameterKey": "param_str",
           "Type": "String"
```

`},` `{`

```json
           "Description": "",
           "Label": "param_list",
           "NoEcho": "false",
           "ParameterKey": "param_list",
           "Type": "CommaDelimitedList"
```

`},` `{`

```json
           "Description": "",
           "Label": "param_json_dict",
           "NoEcho": "false",
           "ParameterKey": "param_json_dict",
           "Type": "Json"
```

`}` `],`

```json
   "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F"
```

`}`

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| InvalidTemplate | {reason}. | 400 | The error message returned because the specified template is invalid. reason indicates the specific reason. |

#### 1.9.3 GetTemplate

You can call this operation to query details about a template. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetTemplate | The operation that you want to perform. Set the value to GetTemplate. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackId | String | No | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| ChangeSetId | String | No | 1f6521a4-05af- 4975-afe9- bc4b45ad**** | The ID of the change set. |

| esource Orchestratio | n Service |   |   | Developer Guide·API Referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TemplateId | String | No | 5ecd1e10-b0e9- 4389-a565- e4c15efc**** | The ID of the template. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | The ID of the request. |
| TemplateBody | String | {\"ROSTemplateFor matVersion\": \"2015-09-01\"} | The structure that contains the template body. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=GetTemplate &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```json
<GetTemplateResponse>
        <TemplateBody>{"ROSTemplateFormatVersion": "2015-09-01", "Resources": {"dummy2": {"
Type": "ALIYUN::DEBUG::Dummy", "Properties": {"Map": {"Ref": "param_has_default"}, "List": {"Ref": "param_list"}}}, "dummy": {"Type": "ALIYUN::DEBUG::Dummy", "Properties": {"Map": {" Ref": "param_json_dict"}, "String": {"Ref": "param_str"}, "List": {"Ref": "param_json_list" }, "Number": {"Ref": "param_float"}, "Bool": {"Ref": "param_bool"}, "Integer": {"Ref": "par am_integer"}}}, "nested": {"Type": "ALIYUN::ROS::Stack", "Properties": {"TemplateURL": "oss ://nested-stack/simple/nested_demo", "TimeoutMins": 16}}, "WaitConditionHandle": {"Type": " ALIYUN::ROS::WaitConditionHandle", "Properties": {"UpdateVersion": {"Ref": "UpdateVersion"} }}}, "Parameters": {"param_integer": {"Type": "Number"}, "param_float": {"Type": "Number"}, "param_bool": {"Type": "Boolean"}, "param_json_list": {"Type": "Json"}, "param_has_default" : {"Default": "{\"c\": []}", "Type": "Json"}, "UpdateVersion": {"Type": "Number"}, "param_s tr": {"Type": "String"}, "param_list": {"Type": "CommaDelimitedList"}, "param_json_dict": { "Type": "Json"}}, "Outputs": {"param_integer": {"Value": {"Ref": "param_integer"}}, "param_ float": {"Value": {"Ref": "param_float"}}, "param_bool": {"Value": {"Ref": "param_bool"}}, "param_json_list": {"Value": {"Ref": "param_json_list"}}, "param_has_default": {"Value": {" Ref": "param_has_default"}}, "param_str": {"Value": {"Ref": "param_str"}}, "CurlCli": {"Val ue": {"Fn::GetAtt": ["WaitConditionHandle", "CurlCli"]}}, "param_list": {"Value": {"Ref": " param_list"}}, "param_json_dict": {"Value": {"Ref": "param_json_dict"}}}}</TemplateBody>
        <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
</GetTemplateResponse>
```

`JSON` format `{`

```json
   "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F",
   "TemplateBody": "{\"ROSTemplateFormatVersion\": \"2015-09-01\", \"Resources\": {\"dummy2
\": {\"Type\": \"ALIYUN::DEBUG::Dummy\", \"Properties\": {\"Map\": {\"Ref\": \"param_has_de fault\"}, \"List\": {\"Ref\": \"param_list\"}}}, \"dummy\": {\"Type\": \"ALIYUN::DEBUG::Dum my\", \"Properties\": {\"Map\": {\"Ref\": \"param_json_dict\"}, \"String\": {\"Ref\": \"par am_str\"}, \"List\": {\"Ref\": \"param_json_list\"}, \"Number\": {\"Ref\": \"param_float\"} , \"Bool\": {\"Ref\": \"param_bool\"}, \"Integer\": {\"Ref\": \"param_integer\"}}}, \"neste d\": {\"Type\": \"ALIYUN::ROS::Stack\", \"Properties\": {\"TemplateURL\": \"oss://nested-st ack/simple/nested_demo\", \"TimeoutMins\": 16}}, \"WaitConditionHandle\": {\"Type\": \"ALIY UN::ROS::WaitConditionHandle\", \"Properties\": {\"UpdateVersion\": {\"Ref\": \"UpdateVersi on\"}}}}, \"Parameters\": {\"param_integer\": {\"Type\": \"Number\"}, \"param_float\": {\"T ype\": \"Number\"}, \"param_bool\": {\"Type\": \"Boolean\"}, \"param_json_list\": {\"Type\" : \"Json\"}, \"param_has_default\": {\"Default\": \"{\\\"c\\\": []}\", \"Type\": \"Json\"}, \"UpdateVersion\": {\"Type\": \"Number\"}, \"param_str\": {\"Type\": \"String\"}, \"param_l ist\": {\"Type\": \"CommaDelimitedList\"}, \"param_json_dict\": {\"Type\": \"Json\"}}, \"Ou tputs\": {\"param_integer\": {\"Value\": {\"Ref\": \"param_integer\"}}, \"param_float\": {\ "Value\": {\"Ref\": \"param_float\"}}, \"param_bool\": {\"Value\": {\"Ref\": \"param_bool\" }}, \"param_json_list\": {\"Value\": {\"Ref\": \"param_json_list\"}}, \"param_has_default\" : {\"Value\": {\"Ref\": \"param_has_default\"}}, \"param_str\": {\"Value\": {\"Ref\": \"par am_str\"}}, \"CurlCli\": {\"Value\": {\"Fn::GetAtt\": [\"WaitConditionHandle\", \"CurlCli\" ]}}, \"param_list\": {\"Value\": {\"Ref\": \"param_list\"}}, \"param_json_dict\": {\"Value\ ": {\"Ref\": \"param_json_dict\"}}}}"
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the specified stack does not exist. name indicates the name or ID of the stack. |
| 404 | TemplateNotFound | The Tempalte ({ ID }) could not be found. | The error message returned because the specified template does not exist. ID indicates the template ID. |

#### 1.9.4 DeleteTemplate

You can call this operation to delete a stack and all of its resources. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteTemplate | The operation that you want to perform. Set the value to DeleteTemplate. |
| TemplateId | String | Yes | 5ecd1e10-b0e9- 4389-a565- e4c15efc**** | The ID of the stack. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 8C5D90E1-66B6- 496C-9371- 3807F8DA80A8 | The ID of the request. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=DeleteTemplate &TemplateId=5ecd1e10-b0e9-4389-a565-e4c15efc**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteTemplateResponse>
          <RequestId>8C5D90E1-66B6-496C-9371-3807F8DA80A8</RequestId>
</DeleteTemplateResponse>
```

`JSON` format `{`

```json
    "RequestId": "8C5D90E1-66B6-496C-9371-3807F8DA80A8"
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | TemplateNotFound | The Tempalte ({ ID }) could not be found. | The error message returned because the specified stack does not exist. |

#### 1.9.5 ListTemplates

You can call this operation to query the list of one or more templates. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListTemplates | The operation that you want to perform. Set the value to ListTemplates. |
| TemplateName | String | No | MyTemplate | The name of the template. The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores ( ). It must start with a digit or letter. _ |
| PageNumber | Long | No | 10 | The number of the page to return. Pages start from page 1. Default value: 1. |
| PageSize | Long | No | 1 | The number of entries to return on each page. Valid values: 1 to 50. Default value: 10. |
| Tag.N.Key | String | No | TestKey | The key of tag N. Valid values of N: 1 to 20. The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot contain http:// or https://. It cannot start with acs: or aliyun. |
| Tag.N.Value | String | No | TestValue | The value of tag N. Valid values of N: 1 to 20. The tag value can be an empty string. The tag value can be up to 128 characters in length and cannot contain http:// or https://. It cannot start with acs: or aliyun. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C3A8413B-1F16- 4DED-AC3E- 61A00718DE8A | The ID of the request. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| PageNumber | Integer | 1 | The page number of the returned page. Pages start from page 1. |
| TotalCount | Integer | 3 | The total number of templates. |
| Templates | Array of Template |   | Details about the templates. |
| CreateTime | String | 2019-10- 15T08:17:14.000000 | The time when the template was created. |
| Description | String | test-description | The description of the template. |
| TemplateId | String | 4d4f5aa2-3260- 4e47-863b- 763fbb12**** | The ID of the template. |
| TemplateName | String | test-list-templates | The name of the template. |
| UpdateTime | String | 2019-10- 15T08:17:14.000000 | The time when the template was created. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=ListTemplates &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ListTemplatesResponse>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <RequestId>C3A8413B-1F16-4DED-AC3E-61A00718DE8A</RequestId>
    <Templates>
       <CreateTime>2019-10-15T08:17:15.000000</CreateTime>
       <Description>test-description-update</Description>
       <TemplateId>c8b8bd07-c488-4302-ac15-b88ef073****</TemplateId>
       <TemplateName>test-template-name-update</TemplateName>
       <UpdateTime>2019-10-15T08:17:15.000000</UpdateTime>
    </Templates>
    <Templates>
       <CreateTime>2019-10-15T08:17:15.000000</CreateTime>
       <Description>test-description</Description>
       <TemplateId>4d4f5aa2-3260-4e47-863b-763fbb12****</TemplateId>
       <TemplateName>test-list-templates-2</TemplateName>
       <UpdateTime>2019-10-15T08:17:15.000000</UpdateTime>
    </Templates>
    <Templates>
       <CreateTime>2019-10-15T08:17:14.000000</CreateTime>
       <Description>test-description</Description>
       <TemplateId>1e808bb6-c2d1-4196-98a3-3b2cb2a4****</TemplateId>
       <TemplateName>test-list-templates-1</TemplateName>
       <UpdateTime>2019-10-15T08:17:14.000000</UpdateTime>
    </Templates>
    <TotalCount>3</TotalCount>
</ListTemplatesResponse>
```

`JSON` format `{`

```json
    "PageNumber": 1,
    "PageSize": 10,
    "RequestId": "C3A8413B-1F16-4DED-AC3E-61A00718DE8A",
    "Templates": [
```

`{`

```json
            "CreateTime": "2019-10-15T08:17:15.000000",
            "Description": "test-description-update",
            "TemplateId": "c8b8bd07-c488-4302-ac15-b88ef073****",
            "TemplateName": "test-template-name-update",
            "UpdateTime": "2019-10-15T08:17:15.000000"
```

`},` `{`

```json
            "CreateTime": "2019-10-15T08:17:15.000000",
            "Description": "test-description",
            "TemplateId": "4d4f5aa2-3260-4e47-863b-763fbb12****",
            "TemplateName": "test-list-templates-2",
            "UpdateTime": "2019-10-15T08:17:15.000000"
```

`},` `{`

```json
            "CreateTime": "2019-10-15T08:17:14.000000",
            "Description": "test-description",
            "TemplateId": "1e808bb6-c2d1-4196-98a3-3b2cb2a4****",
            "TemplateName": "test-list-templates-1",
            "UpdateTime": "2019-10-15T08:17:14.000000"
```

`}` `],`

```json
    "TotalCount": 3
```

`}`

#### 1.9.6 CreateTemplate

You can call this operation to create a template. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateTemplate | The operation that you want to perform. Set the value to CreateTemplate. |
| TemplateName | String | Yes | MyTemplate | The name of the template. The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores ( ). It must start with a digit or letter. _ |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TemplateURL | String | No | oss://ros/templ ate/demo | The URL of the file that contains the template body. The URL must point to a template located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/template/demo and oss://ros/template/demo? RegionId=cn-hangzhou. The template can be up to 524,288 bytes in length, and the URL can be up to 1,024 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Not e You can specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |
| Description | String | No | It is a demo. | The description of the template. The description can be up to 256 characters in length. |
| TemplateBody | String | No | {"ROSTemplateFo rmatVersion":"20 15-09-01"} | The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body is longer than required, we recommend that you add parameters to the HTTP POST request body to avoid request failures due to excessive length of URLs. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 8C5D90E1-66B6- 496C-9371- 3807F8DA80A8 | The ID of the request. |
| TemplateId | String | 5ecd1e10-b0e9- 4389-a565- e4c15efc**** | The ID of the template. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=CreateTemplate &TemplateName=MyTemplate &TemplateURL=oss://ros/template/demo &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateTemplateResponse>
          <RequestId>8C5D90E1-66B6-496C-9371-3807F8DA80A8</RequestId>
          <TemplateId>5ecd1e10-b0e9-4389-a565-e4c15efc****</TemplateId>
</CreateTemplateResponse>
```

`JSON` format `{`

```json
    "RequestId": "8C5D90E1-66B6-496C-9371-3807F8DA80A8",
    "TemplateId": "5ecd1e10-b0e9-4389-a565-e4c15efc****"
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidSchema | {reason}. | The error message returned because the specified template format is invalid. reason indicates the specific reason. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidTemplateAttribut e | The Referenced Attribute ({resource} {name}) is incorrect. | The error message returned because the resource attribute referenced in the template is incorrect. resource indicates the resource name, and name indicates the attribute name. |
| 400 | InvalidTemplatePropert yType | The specified value type of ({resource} {section}) is incorrect. | The error message returned because the type of the specified resource section defined in the template is incorrect. resource indicates the resource name, and section indicates the section name. |
| 400 | InvalidTemplateReferen ce | The specified reference "{name}" (in {referencer}) is incorrect. | The error message returned because the template contains an invalid reference. name indicates the reference name, and referencer indicates the referencer name. |
| 400 | InvalidTemplateSection | The template section is invalid: {section}. | The error message returned because the template contains an invalid property. section indicates the section name. |
| 400 | InvalidTemplateVersion | The template version is invalid: {reason}. | The error message returned because the template version is incorrect. reason indicates the specific reason. |

#### 1.9.7 UpdateTemplate

You can call this operation to update a template. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateTemplate | The operation that you want to perform. Set the value to UpdateTemplate. |
| TemplateId | String | Yes | 5ecd1e10-b0e9- 4389-a565- e4c15efc**** | The ID of the template. |
| TemplateURL | String | No | oss://ros/templ ate/demo | The URL of the file that contains the template body. The URL must point to a template located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/template/demo and oss://ros/template/demo? RegionId=cn-hangzhou. The template can be up to 524,288 bytes in length, and the URL can be up to 1,024 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |
| TemplateName | String | No | MyTemplate | The name of the template. The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores ( ). It must start with a digit or letter. _ |
| Description | String | No | It is a demo. | The description of the template. The description can be up to 256 characters in length. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TemplateBody | String | No | {"ROSTemplateFo rmatVersion":"20 15-09-01"} | The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body is longer than required, we recommend that you add parameters to the HTTP POST request body to avoid request failures due to excessive length of URLs. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 8C5D90E1-66B6- 496C-9371- 3807F8DA80A8 | The ID of the request. |
| TemplateId | String | 5ecd1e10-b0e9- 4389-a565- e4c15efc**** | The ID of the template. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=UpdateTemplate &TemplateId=5ecd1e10-b0e9-4389-a565-e4c15efc**** &TemplateURL=oss://ros/template/demo &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UpdateTemplateResponse>
          <RequestId>8C5D90E1-66B6-496C-9371-3807F8DA80A8</RequestId>
          <TemplateId>5ecd1e10-b0e9-4389-a565-e4c15efc****</TemplateId>
</UpdateTemplateResponse>
```

`JSON` format `{`

```json
    "RequestId": "8C5D90E1-66B6-496C-9371-3807F8DA80A8",
    "TemplateId": "5ecd1e10-b0e9-4389-a565-e4c15efc****"
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | TemplateNotFound | The Tempalte ({ ID }) could not be found. | The error message returned because the specified template does not exist. |
| 400 | InvalidSchema | {reason}. | The error message returned because the specified template format is invalid. reason indicates the specific reason. |
| 400 | InvalidTemplateAttribut e | The Referenced Attribute ({resource} {name}) is incorrect. | The error message returned because the resource attribute referenced in the template is invalid. resource indicates the resource name, and name indicates the attribute name. |
| 400 | InvalidTemplatePropert yType | The specified value type of ({resource} {section}) is incorrect. | The error message returned because the type of the specified resource section defined in the template is invalid. resource indicates the resource name, and section indicates the section name. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidTemplateReferen ce | The specified reference "{name}" (in {referencer}) is incorrect. | The error message returned because the template contains an invalid reference. name indicates the reference name, and referencer indicates the referencer name. |
| 400 | InvalidTemplateSection | The template section is invalid: {section}. | The error message returned because the template contains an invalid property. section indicates the section name. |
| 400 | InvalidTemplateVersion | The template version is invalid: {reason}. | The error message returned because the template version is invalid. reason indicates the specific reason. |

#### 1.9.8 GetTemplateSummary

You can call this operation to query information about a new or existing template. To specify the query object, you must specify one of the StackId, ChangeSetId, TemplateId, TemplateBody, and TemplateURL parameters. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetTemplateSum mary | The operation that you want to perform. Set the value to GetTemplateSummary. |
| StackId | String | No | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |

| esource Orchestratio | n Service |   |   | Developer Guide·API Referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TemplateBody | String | No | {"ROSTemplateFo rmatVersion":"20 15-09-01"} | The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body is longer than required, we recommend that you add parameters to the HTTP POST request body to avoid request failures due to excessive length of URLs. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |
| RegionId | String | No | cn-hangzhou | The region ID of the stack. |
| TemplateId | String | No | 5ecd1e10-b0e9- 4389-a565- e4c15efc**** | The ID of the template. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TemplateURL | String | No | oss://ros/templ ate/demo | The URL of the file that contains the template body. The URL must point to a template located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/template/demo and oss://ros/template/demo? RegionId=cn-hangzhou. The template can be up to 524,288 bytes in length, and the URL can be up to 1,024 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |
| ChangeSetId | String | No | 1f6521a4-05af- 4975-afe9- bc4b45ad**** | The ID of the change set. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Description | String | No description | The description of the stack template. |
| Metadata | Map | {"key": "value"} | The metadata that is specified in the template. |
| Parameters | List | [{"Description":"", "Label":"Name", "NoEcho":"false", "ParameterKey":"Na me", "Type":"String"}] | Details about the parameter declarations that describe the attributes of parameters. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | The ID of the request. |
| ResourceIdentif ierSummaries | Array of ResourceIdentif ierSummary |   | Details about the resource identifier summaries. A summary describes the resource into which you want to import other resources and the attributes that can be used to identify the resource. For example, VpcId is the identifier of the ALIYUN::ECS::VPC resource. |
| LogicalResourc eIds | List | ["Vpc"] | The logical IDs of all resources that are of the type that is specified by the ResourceType parameter. |
| ResourceIdentif iers | List | ["VpcId"] | The attributes of the resource. The attributes are used to identify the resource into which you want to import other resources. For example, VpcId is the identifier of the ALIYUN::ECS::VPC resource. |
| ResourceType | String | ALIYUN::ECS::VPC | The type of the resource. Not e You can import resources into the ALIYUN::ECS::VPC resource type. |
| ResourceTypes | List | ["ALIYUN::ECS::VPC" ] | All the resource types that are used in the template. |
| Version | String | 2015-09-01 | The version of the template. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=GetTemplateSummary &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &RegionId=cn-hangzhou &TemplateURL=oss://ros/template/demo &<Common request parameters>
```

Sample success responses `XML` format

```xml
<GetTemplateSummary>
          <Description>No description</Description>
          <Metadata></Metadata>
          <Parameters>
                <Description>Description of the vpc, [2, 256] characters. Do not fill or em
pty, the default is empty. </Description>
                <Label>Description</Label>
                <NoEcho>false</NoEcho>
                <ParameterKey>Description</ParameterKey>
                <Type>String</Type>
          </Parameters>
          <Parameters>
                <Description>Tags to attach to vpc. Max support 20 tags to add during creat
e vpc. Each tag with two properties Key and Value, and Key is required. </Description>
                <Label>Tags</Label>
                <MaxLength>20</MaxLength>
                <NoEcho>false</NoEcho>
                <ParameterKey>Tags</ParameterKey>
                <Type>Json</Type>
          </Parameters>
          <Parameters>
                <Description>IPv6 network cidr of the VPC. </Description>
                <Label>Ipv6CidrBlock</Label>
                <MinLength>1</MinLength>
                <NoEcho>false</NoEcho>
                <ParameterKey>Ipv6CidrBlock</ParameterKey>
                <Type>String</Type>
          </Parameters>
          <Parameters>
                <AllowedValues>True</AllowedValues>
                <AllowedValues>true</AllowedValues>
                <AllowedValues>False</AllowedValues>
                <AllowedValues>false</AllowedValues>
                <Default>false</Default>
                <Description>Whether to enable an IPv6 network cidr, the value is:False (de
fault): not turned on.True: On. </Description>
                <Label>EnableIpv6</Label>
                <NoEcho>false</NoEcho>
                <ParameterKey>EnableIpv6</ParameterKey>
                <Type>Boolean</Type>
          </Parameters>
          <Parameters>
                <Description>Resource group id. </Description>
                <Label>ResourceGroupId</Label>
                <NoEcho>false</NoEcho>
                <ParameterKey>ResourceGroupId</ParameterKey>
                <Type>String</Type>
          </Parameters>
          <Parameters>
                <Description>Display name of the vpc instance, [2, 128] English or Chinese
characters, must start with a letter or Chinese in size, can contain numbers, '' or '.', '
```

```
caactes, uststat
```

`t` `a`

```
ette
```

`o`

```
ese
```

`s`

```
e,ca cota ubes,
```

`_` `o` `.``,`

```xml
-'</Description>
                <Label>VpcName</Label>
                <NoEcho>false</NoEcho>
                <ParameterKey>VpcName</ParameterKey>
                <Type>String</Type>
          </Parameters>
          <Parameters>
                <Description>
                The IP address range of the VPC in the CIDR block form. You can use the fol
lowing IP address ranges and their subnets:
                10.0.0.0/8
                172.16.0.0/12 (Default)
                192.168.0.0/16</Description>
                <Label>CidrBlock</Label>
                <NoEcho>false</NoEcho>
                <ParameterKey>CidrBlock</ParameterKey>
                <Type>String</Type>
          </Parameters>
          <RequestId>FD70598C-3F4B-4E66-9A76-67F2E2D36938</RequestId>
          <ResourceIdentifierSummaries>
                <LogicalResourceIds>Vpc</LogicalResourceIds>
                <ResourceIdentifiers>VpcId</ResourceIdentifiers>
                <ResourceType>ALIYUN::ECS::VPC</ResourceType>
          </ResourceIdentifierSummaries>
          <ResourceTypes>ALIYUN::ECS::VPC</ResourceTypes>
          <Version>2015-09-01</Version>
</GetTemplateSummary>
```

`JSON` format `{`

```json
    "Description": "No description",
    "Metadata": {},
    "Parameters": [
```

`{`

```json
            "Description": "Description of the vpc, [2, 256] characters. Do not fill or emp
ty, the default is empty.",
            "Label": "Description",
            "NoEcho": "false",
            "ParameterKey": "Description",
            "Type": "String"
```

`},` `{`

```json
            "Description": "Tags to attach to vpc. Max support 20 tags to add during create
vpc. Each tag with two properties Key and Value, and Key is required.",
            "Label": "Tags",
            "MaxLength": 20,
            "NoEcho": "false",
            "ParameterKey": "Tags",
            "Type": "Json"
```

`},` `{`

```json
            "Description": "IPv6 network cidr of the VPC.",
"Lbl"
```

`"I`

```
6CidBl
```

`k"`

```json
            "Label": "Ipv6CidrBlock",
            "MinLength": 1,
            "NoEcho": "false",
            "ParameterKey": "Ipv6CidrBlock",
            "Type": "String"
```

`},` `{`

```json
            "AllowedValues": [
                "True",
                "true",
                "False",
                "false"
```

`],`

```json
            "Default": false,
            "Description": "Whether to enable an IPv6 network cidr, the value is:False (def
ault): not turned on.True: On.",
            "Label": "EnableIpv6",
            "NoEcho": "false",
            "ParameterKey": "EnableIpv6",
            "Type": "Boolean"
```

`},` `{`

```json
            "Description": "Resource group id.",
            "Label": "ResourceGroupId",
            "NoEcho": "false",
            "ParameterKey": "ResourceGroupId",
            "Type": "String"
```

`},` `{`

```json
            "Description": "Display name of the vpc instance, [2, 128] English or Chinese c
haracters, must start with a letter or Chinese in size, can contain numbers, '_' or '.', '- '",
            "Label": "VpcName",
            "NoEcho": "false",
            "ParameterKey": "VpcName",
            "Type": "String"
```

`},` `{`

```json
            "Description": "The IP address range of the VPC in the CIDR block form. You can
use the following IP address ranges and their subnets:\n10.0.0.0/8\n172.16.0.0/12 (Default) \n192.168.0.0/16",
            "Label": "CidrBlock",
            "NoEcho": "false",
            "ParameterKey": "CidrBlock",
            "Type": "String"
```

`}` `],`

```json
    "RequestId": "FD70598C-3F4B-4E66-9A76-67F2E2D36938",
    "ResourceIdentifierSummaries": [
```

`{`

```json
            "LogicalResourceIds": [
                "Vpc"
```

`],`

```json
            "ResourceIdentifiers": [
"VpcId"
```

```
                VpcId
```

`],`

```json
            "ResourceType": "ALIYUN::ECS::VPC"
```

`}` `],`

```json
    "ResourceTypes": [
        "ALIYUN::ECS::VPC"
```

`],`

```json
    "Version": "2015-09-01"
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | StackValidationFailed | {reason}. | The error message returned because the stack validation failed. reason indicates the specific reason. |
| 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the specified stack does not exist. name indicates the name or ID of the stack. |
| 404 | TemplateNotFound | The Tempalte ({ ID }) could not be found. | The error message returned because the specified template does not exist. ID indicates the template ID. |

### 1.10 Stack policy operations

#### 1.10.1 SetStackPolicy

You can call this operation to set a stack policy. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetStackPolicy | The operation that you want to perform. Set the value to SetStackPolicy. |

| Developer Guide·API | Reference |   |   | Resource Orchestration Servic |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| StackPolicyBody | String | No | {"Statement": [{"Effect":"Allow" ,"Action":"Updat e:*","Principal":"* ","Resource":"*"}]} | The structure that contains the stack policy body. The stack policy body must be 1 to 16,384 bytes in length. Not e You must specify one of the StackPolicyBody and StackPolicyURL parameters, but you cannot specify both of them. |
| StackPolicyURL | String | No | oss://ros/stack- policy/demo | The URL of the file that contains the stack policy. The URL must point to a policy located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/stack- policy/demo and oss://ros/stack- policy/demo?RegionId=cn-hangzhou. The policy can be up to 16,384 bytes in length and the URL can be up to 1,350 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Not e You must specify one of the StackPolicyBody and StackPolicyURL parameters, but you cannot specify both of them. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | The ID of the request. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=SetStackPolicy &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &StackPolicyURL=oss://ros/stack-policy/demo &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetStackPolicyResponse>
      <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
</SetStackPolicyResponse>
```

`JSON` format `{`

```json
   "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F"
```

`}`

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| StackValidationFailed | {reason}. | 400 | The error message returned because the stack validation failed. reason indicates the specific reason. |
| StackNotFound | The Stack ({name}) could not be found. | 404 | The error message returned because the specified stack does not exist. name indicates the name or ID of the stack. |

#### 1.10.2 GetStackPolicy

You can call this operation to query information about a stack policy. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetStackPolicy | The operation that you want to perform. Set the value to GetStackPolicy. |

| Developer Guide·API | Reference |   |   | Resource Orchestration Servic |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| StackPolicyBod y | Map | {"Statement": [{"Action": "Update:*", "Effect": "Allow","Principal": "*","Resource": "*"}]} | The structure that contains the stack policy body. The policy body must be 1 to 16,384 bytes in length. |
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | The ID of the request. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=GetStackPolicy &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<GetStackPolicyResponse>
    <StackPolicyBody>
        <Statement>
            <Statement>
                <Resource>*</Resource>
                <Principal>*</Principal>
                <Action>Update:*</Action>
                <Effect>Allow</Effect>
            </Statement>
            <Statement>
                <Resource>LogicalResourceId/WebServer</Resource>
                <Principal>*</Principal>
                <Action>Update:*</Action>
                <Effect>Deny</Effect>
            </Statement>
        </Statement>
    </StackPolicyBody>
    <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
</GetStackPolicyResponse>
```

`JSON` format `{`

```json
  "StackPolicyBody": {
    "Statement": [
```

`{`

```json
        "Action": "Update:*",
        "Effect": "Allow",
        "Principal": "*",
        "Resource": "*"
```

`},` `{`

```json
        "Action": "Update:*",
        "Effect": "Deny",
        "Principal": "*",
        "Resource": "LogicalResourceId/WebServer"
```

`}` `]` `},`

```json
  "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F"
```

`}`

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| StackNotFound | The Stack ({name}) could not be found. | 404 | The error message returned because the specified stack could not be found. name indicates the name or ID of the stack. |

### 1.11 Other operations

#### 1.11.1 DescribeRegions

You can call this operation to query available regions. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRegions | The operation that you want to perform. Set the value to DescribeRegions. |
| AcceptLanguage | String | No | zh-CN | The natural language that is used to filter responses. Default value: zh-CN. Valid values: zh-CN en-US ja |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Regions | Array of Region |   | Details about the regions. |
| LocalName | String | China (Hangzhou) | The name of the region in the local language. |
| RegionEndpoint | String | ros.aliyuncs.com | The endpoint of the region. |
| RegionId | String | cn-hangzhou | The ID of the region. |
| RequestId | String | 59F0F0A0-A637- 4292-9B91- 251EF5010913 | The ID of the request. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=DescribeRegions &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeRegionsResponse>
    <Regions>
        <Region>
            <RegionId>cn-qingdao</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>China (Qingdao)</LocalName>
        </Region>
        <Region>
            <RegionId>cn-beijing</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>China (Beijing)</LocalName>
        </Region>
        <Region>
            <RegionId>cn-zhangjiakou</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>China (Zhangjiakou)</LocalName>
        </Region>
        <Region>
            <RegionId>cn-huhehaote</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>China (Hohhot)</LocalName>
        </Region>
        <Region>
            <RegionId>cn-hangzhou</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>China (Hangzhou)</LocalName>
        </Region>
        <Region>
            <RegionId>cn-shanghai</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>China (Shanghai)</LocalName>
        </Region>
        <Region>
            <RegionId>cn-shenzhen</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>China (Shenzhen)</LocalName>
        </Region>
        <Region>
            <RegionId>cn-chengdu</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>China (Chengdu)</LocalName>
        </Region>
        <Region>
            <RegionId>ap-northeast-1</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>Japan (Tokyo)</LocalName>
        </Region>
        <Region>
            <RegionId>ap-southeast-1</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>Singapore (Singapore)</LocalName>
```

```
oca aeS gapoe(S gapoe)/oca
```

`a``e`

```xml
        </Region>
        <Region>
            <RegionId>ap-southeast-2</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>Australia (Sydney)</LocalName>
        </Region>
        <Region>
            <RegionId>ap-southeast-3</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>Malaysia (Kuala Lumpur)</LocalName>
        </Region>
        <Region>
            <RegionId>ap-southeast-5</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>Indonesia (Jakarta)</LocalName>
        </Region>
        <Region>
            <RegionId>ap-south-1</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>India (Mumbai)</LocalName>
        </Region>
        <Region>
            <RegionId>us-east-1</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>US (Virginia)</LocalName>
        </Region>
        <Region>
            <RegionId>us-west-1</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>US (Silicon Valley)</LocalName>
        </Region>
        <Region>
            <RegionId>eu-west-1</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>UK (London)</LocalName>
        </Region>
        <Region>
            <RegionId>me-east-1</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>UAE (Dubai)</LocalName>
        </Region>
        <Region>
            <RegionId>eu-central-1</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>Germany (Frankfurt)</LocalName>
        </Region>
    </Regions>
    <RequestId>59F0F0A0-A637-4292-9B91-251EF5010913</RequestId>
</DescribeRegionsResponse>
```

`JSON` format `{` `"R` `i` `"` `[`

```json
    "Regions": [
```

`{`

```json
            "LocalName": "China (Qingdao)"
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "cn-qingdao"
```

`},` `{`

```json
            "localName": "China (Beijing)",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "cn-beijing"
```

`},` `{`

```json
            "localName": "China (Zhangjiakou)",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "cn-zhangjiakou"
```

`},` `{`

```json
            "localName": "China (Hohhot)",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "cn-huhehaote"
```

`},` `{`

```json
            "localName": "China (Hangzhou)",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "cn-hangzhou"
```

`},` `{`

```json
            "localName": "China (Shanghai)",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "cn-shanghai"
```

`},` `{`

```json
            "localName": "China (Shenzhen)",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "cn-shenzhen"
```

`},` `{`

```json
            "LocalName": "China (Chengdu)"
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "cn-chengdu"
```

`},` `{`

```json
            "localName": "Japan (Tokyo)",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "ap-northeast-1"
```

`},` `{`

```json
            "localName": "Singapore (Singapore)",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "ap-southeast-1"
```

`},` `{`

```json
            "localName": "Australia (Sydney)",
            "RegionEndpoint": "ros.aliyuncs.com",
"RegionId":"ap-southeast-2"
```

```
            RegionId: ap-southeast-2
```

`},` `{`

```json
            "localName": "Malaysia (Kuala Lumpur)",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "ap-southeast-3"
```

`},` `{`

```json
            "localName": "Indonesia (Jakarta)",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "ap-southeast-5"
```

`},` `{`

```json
            "localName": "India (Mumbai)",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "ap-south-1"
```

`},` `{`

```json
            "localName": "US (Virginia)",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "us-east-1"
```

`},` `{`

```json
            "localName": "US (Silicon Valley)",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "us-west-1"
```

`},` `{`

```json
            "localName": "UK (London)",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "eu-west-1"
```

`},` `{`

```json
            "localName": "UAE (Dubai)",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "me-east-1"
```

`},` `{`

```json
            "LocalName": "Germany (Frankfurt)"
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "eu-central-1"
```

`}` `],`

```json
    "RequestId": "59F0F0A0-A637-4292-9B91-251EF5010913"
```

`}`

#### 1.11.2 SignalResource

You can call this operation to send signals. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SignalResource | The operation that you want to perform. Set the value to SignalResource. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| LogicalResourceId | String | Yes | WebServer | The logical ID of the resource as defined in the template. |
| Status | String | Yes | SUCCESS | The state of the signal. Failure signals can cause stack creation or update to fail. If all signals are warnings, the stack cannot be created or updated. Valid values: SUCCESS FAILURE WARNING |
| UniqueId | String | Yes | 27c7347b-352a- 4377-accf- 63d361c1**** | The unique ID of the signal. The ID must be 1 to 64 characters in length. If multiple signals are sent to a single resource, each signal must have a unique ID. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 42665544**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can be up to 64 characters in length and can contain letters, digits, hyphens (-) and underscores ( ). _ |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | The ID of the request. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=SignalResource &RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &LogicalResourceId=WebServer &Status=SUCCESS &UniqueId=27c7347b-352a-4377-accf-63d361c1**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SignalResourceResponse>
      <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
</SignalResourceResponse>
```

`JSON` format `{`

```json
   "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F"
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | ResourceNotAvailable | The Resource ({name}) is not available. | The error message returned because the specified resource is unavailable. name indicates the resource name. |
| 404 | ResourceNotFound | The Resource ({name}) could not be found in Stack {stack}. | The error message returned because the specified resource does not exist in the specified stack. name indicates the resource name, and stack indicates the stack name or ID. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the specified stack does not exist. The name parameter indicates the name or ID of the stack. |

#### 1.11.3 SetDeletionProtection

You can call this operation to configure deletion protection on a stack. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetDeletionProte ction | The operation that you want to perform. Set the value to SetDeletionProtection. |
| DeletionProtectio n | String | Yes | Enabled | Specifies whether to enable deletion protection on the stack. Default value: Disabled. Valid values: Enabled: enables deletion protection on the stack. Disabled: disables deletion protection on the stack. You can release the stack by using the ROS console or by calling the DeleteStack operation. Not e The deletion protection property of a nested stack is the same as that of its root stack. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. The deletion protection property of a nested stack is the same as that of its parent stack and cannot be changed. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | The ID of the request. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=SetDeletionProtection &DeletionProtection=Enabled &RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetDeletionProtectionResponse>
    <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
</SetDeletionProtectionResponse>
```

`JSON` format `{`

```json
    "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F"
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidOperation.SetDel etionProtection | Fail to set deletion protection for {type} {ID}, {reason}. | The error message returned because deletion protection failed to be enabled for a stack. type indicates the type of the object on which to perform the operation. ID indicates the ID of the object on which to perform the operation. reason indicates the specific reason. |
| 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the specified stack does not exist. name indicates the name or ID of the stack. |

#### 1.11.4 ListStackOperationRisks

You can call this operation to detect the resources that may face high risks caused by a stack deletion operation, and query the reason for each risk. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListStackOperatio nRisks | The operation that you want to perform. Set the value to ListStackOperationRisks. |
| OperationType | String | Yes | DeleteStack | The operation type to be detected. The DeleteStack value specifies to detect resources that may face high risks caused by a stack deletion operation. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |

| eveloper Guide·API | Reference |   |   | Resource Orchestration Servic |
|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 42665544**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can be up to 64 characters in length and can contain letters, digits, hyphens (-), and underscores ( ). _ |
| RamRoleName | String | No | test-role | The name of the RAM role. If you specify a RAM role, ROS creates stacks based on the permissions granted to the RAM role and uses the credentials of the RAM role to call API operations. If you do not specify a RAM role, ROS creates stacks based on the permissions of the current account. The RAM role name can be up to 64 characters in length. |
| RetainAllResource s | Boolean | No | false | Specifies whether to retain all resources in the stack. Default value: false. Valid values: true: The resources in the stack are retained. false: The resources in the stack are not retained. Not e This parameter is valid only when the OperationType parameter is set to DeleteStack. |
| RetainResources. N | RepeatLi st | No | WebServer | The list of resources to retain. Not e This parameter is valid only when the OperationType parameter is set to DeleteStack. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 72108E7A-E874- 4A5E-B22C- A61E94AD12CD | The ID of the request. |
| RiskResources | Array of Resource |   | The resources that face high risks caused by the stack deletion operation. |
| Code | String | NoPermission | The error code that is returned when the risk detection fails. This parameter is not returned when the risk detection succeeds. |
| LogicalResourc eId | String | MySG | The logical ID of the resource. It is the resource name defined in the template. |
| Message | String | You are not authorized to complete this action. | The error message that is returned when the risk detection fails. This parameter is not returned when the risk detection succeeds. |
| PhysicalResourc eId | String | sg- bp1dpioafqphedg9* *** | The physical ID of the resource. |
| Reason | String | There are some ECS instances (i- bp18el96s4wq635e* ***) depending on the security group. | The reason for the risk. |
| RequestId | String | DF4296CF-F45F- 4845-A72B- BE617601DB25 | The request ID that is returned when the risk detection fails. This parameter is not returned when the risk detection succeeds. |
| ResourceType | String | ALIYUN::ECS::Securi tyGroup | The type of the resource. |
| RiskType | String | Referenced | The type of the risk. Valid values: Referenced: The current resource is referenced by other resources. MaybeReferenced: The current resource may be referenced by other resources. AdditionalRiskCheckRequired: An additional risk detection is required for nested stacks. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=ListStackOperationRisks &OperationType=DeleteStack &RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ListStackOperationRisks>
    <RequestId>72108E7A-E874-4A5E-B22C-A61E94AD12CD</RequestId>
    <RiskResources>
       <LogicalResourceId>MySG</LogicalResourceId>
       <PhysicalResourceId>sg-bp1dpioafqphedg9****</PhysicalResourceId>
       <ResourceType>ALIYUN::ECS::SecurityGroup</ResourceType>
       <Reason>There are some ECS instances (i-bp18el96s4wq635e****) depending on the secur
ity group. </Reason>
       <RiskType>Referenced</RiskType>
    </RiskResources>
</ListStackOperationRisks>
```

`JSON` format `{`

```json
  "RequestId": "772108E7A-E874-4A5E-B22C-A61E94AD12CD",
  "RiskResources": [
```

`{`

```json
      "LogicalResourceId": "MySG",
      "PhysicalResourceId": "sg-bp1dpioafqphedg9****",
      "ResourceType": "ALIYUN::ECS::SecurityGroup",
      "Reason": "There are some ECS instances (i-bp18el96s4wq635e****) depending on the sec
urity group.",
      "RiskType": "Referenced"
```

`}` `]` `}` Apsara Stack SDKs

## 2 Use ASAPI to call Apsara Stack SDKs

SDKs

### 2.1 ASAPI Developer Guide

#### 2.1.1 ASAPI overview

This topic describes the architecture and features of the Apsara Stack API (ASAPI). The ASAPI is a unified ingress gateway for Apsara Stack services and a main component of the Apsara Uni-manager Management Console. The ASAPI provides a unified method for you to manage and make API calls. You can use Apsara Stack SDK to centrally make API calls to Apsara Stack services, including Elastic Compute Service (ECS) and Virtual Private Cloud (VPC). The ASAPI allows you to make API calls to manage and maintain Apsara Stack services. Make API calls to implement enterprise-grade management. For example, you can manage organizations, users, roles, resource sets, and logon policies. These operations are provided by the Apsara Stack SDKs Apsara Uni-manager Management Console. Make API calls to manage operations. For example, you can manage quotas, usage statistics, specifications, and password policies. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to manage resources. For example, you can create, delete, query, or modify cloud resources. These operations are provided by Apsara Stack services. If you call an API operation to create an ECS instance or a VPC, the API operation is provided by ECS or VPC. Make API calls to query monitoring metrics of Apsara Stack services. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to perform O&M. For example, you can manage monitoring and alerting, inventories, tasks, and physical servers. These operations are provided by the Apsara Uni-manager Operations Console. For more information, see the developer guide of the corresponding Apsara Stack service. For information about API operations used to manage organization users, see Apsara Uni-manager Management Console Developer Guide. For information about the API operation used to create an ECS instance, see ECS Developer Guide. Not e If the "Use Apsara Stack SDK to make API calls" section is included in the developer guide of an Apsara Stack service, the ASAPI is supported by the Apsara Stack service. In this case, you can make API calls based on the developer guide.

#### 2.1.2 Preparations

##### 2.1.2.1 Log on to the API Tool console

You can log on to the API Tool console from the Apsara Uni-manager Management Console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. Apsara Stack SDKs Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. In the top navigation bar, choose Product s > Ot hers > API T ool.

##### 2.1.2.2 View information about API operations

This topic describes how to view information about API operations. Before you use SDKs, obtain service names, API operation names, and API operation versions. Context The API operations on the API Directory page are only for reference. For information about how to call API operations, see developer guides of the corresponding cloud services. If the information on the API Directory page is inconsistent with that in the developer guide of the corresponding cloud service, the information in the developer guide prevails. Procedure
1. Go to the API Tool console. For more information, see Log on to the API Tool console.
2. In the left-side navigation pane, click API Direct ory.
3. On the API Direct ory page, select the desired service from the drop-down list, enter a keyword of
an API operation name in the search box, and then click the search icon.
4. Then, you can view the service name, API operation name, and API operation version.

##### 2.1.2.3 Generate an endpoint for the ASAPI

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

##### 2.1.2.4 Obtain Apsara Stack SDKs

The Apsara Stack API (ASAPI) is a unified portal provided by Apsara Stack. You can use the ASAPI to connect to all Apsara Stack services. Apsara Stack provides SDKs for API calls. For more information about how to obtain Apsara Stack SDKs, see Apsara Stack documentation.

##### 2.1.2.5 Obtain an AccessKey pair

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

##### 2.1.2.6 Query a region ID

When you use Apsara Stack SDK for Node.js to make API calls, specify a region ID. You can obtain a region ID in the Apsara Uni-manager Management Console. Procedure Apsara Stack SDKs
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and click User
Inf ormat ion.
3. In the Apsara St ack AccessKey Pair section, view the region ID.

#### 2.1.3 Common parameters

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

#### 2.1.4 SDK description

##### 2.1.4.1 Use Apsara Stack SDK for Java to call API operations

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

##### 2.1.4.2 Use Apsara Stack SDK for Python to call API operations

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

##### 2.1.4.3 Use Apsara Stack SDK for Node.js to call API operations

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

##### 2.1.4.4 SDK for POP

###### 2.1.4.4.1 SDK for Java

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

###### 2.1.4.4.2 SDK for Go

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

###### 2.1.4.4.3 SDK for Python

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

#### 2.1.5 HTTP requests

##### 2.1.5.1 Overview

This topic describes how to make API requests and is intended for users who use API URLs to initiate HTTP GET requests. If you are using an SDK to initiate requests, you can skip this topic. The request URL consists of different parameters and has a fixed syntax. The URL contains common request parameters, your signature, and operation-specific parameters. Sample request URLs are provided for each API operation. These URLs are not encoded to make them easy to read. Before you make a request, you must encode the request URL. After the authentication process is complete based on your signature, the results are returned to you. Response parameters are returned if the call is successful, whereas an error message is returned if the call fails. You can troubleshoot issues based on the error message.

##### 2.1.5.2 Request syntax

The Apsara Stack API (ASAPI) allows you to call API operations by sending HTTP GET requests based on URLs. Each URL must include request parameters. This topic describes the syntax of HTTP GET requests and provides the endpoint of the ASAPI. Sample request GetOrganizationList is used in the following unencoded URL request:

```
https://public.asapi.aliyuns.com/asapi/v3?Action=GetOrganizationList&Product=ascm&Version=2 019-05-10&Id=<Organization ID>&<Common parameters>
```

`https` : the protocol used to transmit the request. `public.asapi.aliyuns.com/asapi/v3` : the endpoint of the ASAPI. `Action=GetOrganizationList Product=ascm Version=2019-05-10` : the API operation to call. `Id` : the ID of the organization. `<Common parameters>` : the common parameters specified in the system. Apsara Stack SDKs Protocol The ASAPI supports only HTTPS. Endpoint For more information about how to obtain an endpoint, see Generate an endpoint for the ASAPI. To specify an API operation, use the `Action, Product, and Version` parameters. For example, set `Action` to GetOrganizationList, Product to ascm, and Version to 2019-05-10. You must also specify other operation-specific parameters and common parameters. For more information, see Common parameters.

##### 2.1.5.3 Request signatures

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

##### 2.1.5.4 Response

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
