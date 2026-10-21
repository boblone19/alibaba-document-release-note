---
title: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Log Service Developer Guide 20220928"
product_version: "V3.14.0"
doc_version: "20220928"
pdf_pages: 217
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Log Service Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.14.0/%E5%BA%94%E7%94%A8%E6%9C%8D%E5%8A%A1/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.14.0%20Log%20Service%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.14.0 Log Service Developer Guide 20220928

## Table of Contents

- 1 API Reference
  - 1.1 Overview
  - 1.2 Common request headers
  - 1.3 Common response headers
  - 1.4 Request signatures
  - 1.5 Common error codes
  - 1.6 Project API
    - 1.6.1 CreateProject
    - 1.6.2 DeleteProject
    - 1.6.3 UpdateProject
    - 1.6.4 GetProject
    - 1.6.5 ListProject
    - 1.6.6 GetProjectLogs
  - 1.7 Logstore operations
    - 1.7.1 CreateLogstore
    - 1.7.2 DeleteLogstore
    - 1.7.3 UpdateLogstore
    - 1.7.4 GetLogstore
    - 1.7.5 ListLogstore
    - 1.7.6 ListShards
    - 1.7.7 SplitShard
    - 1.7.8 MergeShards
    - 1.7.9 GetCursor
    - 1.7.10 GetCursorTime
    - 1.7.11 PullLogs
    - 1.7.12 PostLog
    - 1.7.13 GetLogs
    - 1.7.14 GetHistograms
    - 1.7.15 UpdateIndex
    - 1.7.16 CreateIndex
    - 1.7.17 DeleteIndex
    - 1.7.18 GetIndex
    - 1.7.19 PutWebtracking
  - 1.8 Logtail machine group operations
    - 1.8.1 CreateMachineGroup
    - 1.8.2 DeleteMachineGroup
    - 1.8.3 UpdateMachineGroup
    - 1.8.4 ListMachineGroup
    - 1.8.5 GetMachineGroup
    - 1.8.6 ApplyConfigToMachineGroup
    - 1.8.7 RemoveConfigFromMachineGroup
    - 1.8.8 ListMachines
    - 1.8.9 GetAppliedConfigs
  - 1.9 Logtail configuration operations
    - 1.9.1 CreateConfig
    - 1.9.2 ListConfig
    - 1.9.3 GetAppliedMachineGroups
    - 1.9.4 GetConfig
    - 1.9.5 DeleteConfig
    - 1.9.6 UpdateConfig
  - 1.10 Consumer group operations
    - 1.10.1 CreateConsumerGroup
    - 1.10.2 DeleteConsumerGroup
    - 1.10.3 GetCheckPoint
    - 1.10.4 HeartBeat
    - 1.10.5 ListConsumerGroup
    - 1.10.6 UpdateCheckPoint
    - 1.10.7 UpdateConsumerGroup
  - 1.11 RAM or STS
    - 1.11.1 Overview
    - 1.11.2 Resource list
    - 1.11.3 Action list
    - 1.11.4 Authentication rules
  - 1.12 Description of common resources
    - 1.12.1 Encrypt data
    - 1.12.2 Data model
    - 1.12.3 Data encoding
    - 1.12.4 Logstores
    - 1.12.5 Shards
    - 1.12.6 Logtail configurations
    - 1.12.7 Logtail machine group
- 2 SDK Reference
  - 2.1 Introduction
    - 2.1.1 Overview
    - 2.1.2 Basic configurations
    - 2.1.3 Error handling
    - 2.1.4 API specifications
  - 2.2 Java SDK
  - 2.3. .NET SDK
  - 2.4. .NET Core SDK
  - 2.5 PHP SDK
  - 2.6 Python SDK
  - 2.7 SDK for Android
  - 2.8 SDK for C
  - 2.9 SDK for Go
  - 2.10 iOS SDK
  - 2.11 SDK for C ++
  - 2.12 Node.js SDK
- 3 ASAPI Reference
  - 3.1 Overview
  - 3.2 Preparations
    - 3.2.1 Log on to the API Tool console
    - 3.2.2 View the information of API operations
    - 3.2.3 Generate an endpoint for the ASAPI
    - 3.2.4 Obtain Apsara Stack SDKs
    - 3.2.5 Obtain an AccessKey pair
    - 3.2.6 Query a region ID
  - 3.3 Common request parameters
  - 3.4 SDK Reference
    - 3.4.1 Apsara Stack SDK for Java
  - 3.5 HTTP Requests
    - 3.5.1 Overview
    - 3.5.2 Request syntax
    - 3.5.3 Request signatures
    - 3.5.4 Response
- 4 Obtain an AccessKey pair
- 5 Obtain an endpoint

## 1 API Reference

### 1.1 Overview

Log Service allows you to collect and manage logs by using the Apsara Uni-manager Management Console. In addition, Log Service allows you to use the Log Service API to collect logs, query logs, and manage your projects and Logstores.

| Object | Operation |
|---|---|
| Log | Basic terms such as log and log group |
| Project | ListProject, CreateProject, DeleteProject, GetProject, and UpdateProject |
|   | GetProjectLogs (Queries all logs in a project) |
| Config | ListConfig, CreateConfig, DeleteConfig, GetConfig, and UpdateConfig |
|   | GetAppliedMachineGroups (Queries the machine groups to which a Logtail configuration file is applied) |
| MachineGroup | ListMachineGroup, CreateMachineGroup, DeleteMachineGroup, GetMachineGroup, and UpdateMachineGroup |
|   | ApplyConfigToMachineGroup and RemoveConfigFromMachineGroup (Deletes a Logtail configuration file) |
|   | GetAppliedConfigs (Queries the applied Logtail configuration files) |
| Logstore | ListLogstore, CreateLogstore, DeleteLogstore, GetLogstore, and UpdateLogstore |
|   | GetLogs (Queries logs) and GetHistograms (Queries the distribution of logs) |
| Index | GetIndex, CreateIndex, DeleteIndex, and UpdateIndex |
| Shard | ListShards, SplitShard, and MergeShards |
|   | PostLog (Writes logs) |
|   | GetCursor (Locates logs) |
|   | PullLogs (Consumes logs) |
|   | CreateConsumerGroup, DeleteConsumerGroup, ListConsumerGroup, and UpdateConsumerGroup |
| Document Version: 20220928 |   |

| Developer Guide·API Reference | Log Servic |
|---|---|
| COobnjescutmer group | Operation |
|   | HeartBeat (Sends heartbeat packets), GetCheckPoint, and UpdateCheckPoint |

You can call the API to perform the following operations: Collect logs based on Logtail configurations and Logtail machine group. Create Logstores and write logs to or read logs from the Logstores.

> Not e
> The Log Service API is a RESTful API based on the HTTP protocol.
> Security verification is required for all API requests. For information about the API request signature method and process, see Request signatures.

### 1.2 Common request headers

The Log Service API is a RESTful API based on the HTTP protocol. The Log Service API supports a set of common request headers that can be used in all API requests. Each Log Service API request must provide a common request header. The following table describes the fields of the common request headers.

| Header field | Type | Description |
|---|---|---|
| Accept | Strin g | The type of the response that the client expects Log Service to return. Two response types are supported: application/json and application/x-protobuf. This field is optional and valid for only GET requests. The specific value is subject to the definition of each API. |
| Accept- Encoding | Strin g | The compression algorithm that the client expects Log Service to return. LZ4 and DEFLATE are supported. The value can also be an empty string, indicating that no compression is performed. This field is optional and valid only for GET requests. The specific value is subject to the definition of each API. |
| Authorizatio n | Strin g | The signature content. For more information, see Request signatures. |
| Content- Length | Num eric valu e | The length of the HTTP request body defined in RFC 2616. If the request does not have a body, this field is not required. |
| Content- MD5 | Strin g | The uppercase string that is generated after the request body is calculated based on the MD5 algorithm. If the request does not have a body, this field is not required. |
| Content- Type | Strin g | The type of the HTTP request body defined in RFC 2616. Log Service API requests support only two types: application and x-protobuf. If the request does not have a body, this field is not required. The specific value is subject to the definition of each API. |

| og Service |   | Developer Guide·API Referenc |
|---|---|---|

| Header field | Type | Description |
|---|---|---|
| Date | Strin g | The time when the request is sent. Only the RFC 822 format is supported. The GMT standard time is used. The formatted string is %a, %d %b %Y %H:%M:%S GMT, for example, Mon, 3 Jan 2010 08:33:47 GMT. |
| Host | Strin g | The complete hostname of the HTTP request. The value does not include protocol headers such as http:// . Example: big-game.regionid.example.com . |
| x-log- apiversion | Strin g | The API version. The current version is 0.6.0. |
| x-log- bodyrawsize | Num eric valu e | The initial size of the request body. If the request does not have a body, the value is 0. If the request body is compressed, the value is the size of the initial data before the compression. Valid values: 0 to 3 × 1024 × 1024. This field is optional and only required when the request body is compressed. |
| x-log- compressty pe | Strin g | The compression type of the API request body. LZ4 and DEFLATE that are defined in RFC 1951 are supported. If you want to use the ZLIB compression type, see RFC 1950. If the request body is not compressed, this field is not required. |
| x-log-date | Strin g | The time when the request is sent. The time format is the same as that of the Date field. This field is optional. If a request contains this field, the value of this field replaces the value of the Date field for the request verification performed by Log Service. The Date field must be provided regardless of whether a request has an x- log-date field. |
| x-log- signatureme thod | Strin g | The signature calculation method. Set the value to hmac-sha1 . |

> Not e
> The maximum difference between the time represented by the Date field of a request and the time when Log Service receives the request is 15 minutes. If the difference exceeds 15 minutes, Log Service rejects the request. If an x-log-date field is specified in the request, the time difference is calculated based on the value of the x-log-date field.
> If the compression algorithm is specified in x-log-compresstype of a request, the raw data must be compressed and then placed into the HTTP request body. The values of Content- Length and Content-MD5 fields are calculated based on the compressed HTTP body.
> The value of the Date field cannot be specified for the HTTP requests sent by some platforms. As a result, no correct value of the Date field is available to calculate the request signature. In this case, you must specify an x-log-date field and use the value of this field to calculate the request signature. After Log Service receives an API request, it checks whether the request contains an x-log-date field. If yes, Log Service uses the value of the x-log-date field for signature verification. If no, Log Service uses the value of the standard HTTP field Date for signature verification.

### 1.3 Common response headers

The Log Service API is a RESTful API based on the HTTP protocol. Each Log Service API response provides a common response header. The following table describes the fields in the common response headers.

| Header field | Typ e | Description |
|---|---|---|
| Content- Length | Nu meri c valu e | The length of the HTTP response defined in RFC 2616. |
| Content- MD5 | Strin g | The MD5 value of the HTTP response defined in RFC 2616. This value is an uppercase string after the request body is calculated based on the MD5 algorithm. |
| Content- Type | Strin g | The type of the HTTP response defined in RFC 2616. Log Service supports two response types: application/json and application/x-protobuf. |
| Date | Strin g | The time when the request is returned. Only the RFC 822 format is supported. The GMT standard time is used. The formatted string is %a, %d %b %Y %H:%M:%S GMT, for example, Mon, 3 Jan 2010 08:33:47 GMT. |
| x-log- requestid | Strin g | The unique ID that marks the request. The ID is generated by Log Service. This response header field is irrelevant to applications. It is used to troubleshoot problems. To troubleshoot failed API requests, you can provide this ID to the technical support team of Log Service. |

### 1.4 Request signatures

Each HTTP request of a Log Service API operation must pass security verification to ensure log data security. The security verification is performed by using the symmetric encryption algorithm. You can use an AccessKey pair for security verification. The security verification process of an API request is as follows:
1. The requester generates a signature string based on the API request content, including the HTTP
header and body.
2. The requester uses an AccessKey pair that consists of an AccessKey ID and AccessKey secret to sign
the signature string. A digital signature is generated for this API request.
3. The requester sends both the API request content and digital signature to Log Service.
4. Log Service receives the request, and then repeats steps 1 and 2.

> Not e Log Service retrieves the AccessKey pair from the backend to calculate the signature string and generate the expected digital signature for this request.

5. The server compares the expected digital signature with the digital signature sent from the
requester. If both signatures are the same, the request passes the security verification. Otherwise, the request is rejected. The following figure shows the security verification process. Security verification process The security verification process can also be used for the following purposes: Identify the user that sends the API request. A user must specify the AccessKey pair that is used to generate the digital signature before the user sends the API request. Then, Log Service can use the AccessKey pair to identify the user and implement access control. Check whether the API request is intercepted and tampered with during transmission. Log Service recalculates the signature string based on the received API request. If the API request is intercepted and tampered with during transmission, the API request cannot pass the security verification. Sign an API request To pass the security verification for an API request, you must sign the API request on the requester to generate a digital signature. You must also use the Authorization field to transmit the digital signature of the API request over the network. The format of the Authorization field is as follows:

```
Authorization:LOG <AccessKeyId>:<Signature>
```

In the preceding format, the value of the Authorization field contains the AccessKey ID. The AccessKey secret is used to construct the signature. To construct the signature, follow these steps:
1. Prepare an AccessKey pair.
To generate a digital signature for an API request, you must use an AccessKey pair. The AccessKey pair consists of an AccessKey ID and an AccessKey secret.
2. Generate a signature string for the API request.
The signature string of a Log Service API operation is generated based on the method, header, and body of the HTTP request. The signature string is generated by using the following formula:

```
SignString = VERB + "\n"
             + CONTENT-MD5 + "\n"
             + CONTENT-TYPE + "\n"
             + DATE + "\n"
             + CanonicalizedLOGHeaders + "\n"
             + CanonicalizedResource
```

In the preceding formula, \n indicates the newline escape character and the plus sign ( `+` ) indicates the string concatenation operator. The following table describes the other elements. Signature string elements

| Element | Description | Example |
|---|---|---|
| VERB | The method name of the HTTP request. | PUT, GET, and POST |
| CONTENT-MD5 | The MD5 value of the HTTP request body, which must be an uppercase string. | 875264590688CA6171F6228AF5BBB3D2 |
| CONTENT-TYPE | The type of the HTTP request body. | application/x-protobuf |
| DATE | The standard timestamp field of the HTTP request. This field complies with the RFC 1123 time format and uses the GMT standard time. | Mon, 3 Jan 2010 08:33:47 GMT |
| CanonicalizedLOGHe aders | The string constructed by the custom fields in the HTTP request. The custom fields are prefixed with x-log and x-acs . | x-log-apiversion:0.6.0\nx-log- bodyrawsize:50\nx-log- signaturemethod:hmac-sha1 |
| CanonicalizedResour ce | The string constructed by using the HTTP request resources. | /logstores/app log _ |

If an HTTP request does not have a body, the CONTENT-MD5 and CONTENT-TYPE fields are empty strings. In this case, the signature string is generated by using the following formula:

```
SignString = VERB + "\n"
             + "\n"
             + "\n"
             + DATE + "\n"
             + CanonicalizedLOGHeaders + "\n"
             + CanonicalizedResource
```

The `x-log-date` custom request field is used in Log Service API operations. For more information, see Common request headers. If you specify this field in a request, the field value replaces the value of the HTTP standard request field Date during signature generation. The CanonicalizedLOGHeaders string is constructed as follows: i. Convert the names of all HTTP request fields prefixed with `x-log` and `x-acs` into lowercase letters. ii. Sort all Log Service custom request fields obtained in the previous step in lexicographical order. iii. Delete all spaces on either side of a delimiter between the request header and content. iv. Separate all headers and contents with the \n delimiter to obtain the CanonicalizedLOGHeader string. The CanonicalizedResource string is constructed as follows: i. Set the CanonicalizedResource string to an empty string (""). ii. Enter the Log Service resources that you want to access, for example, /logstores/logstorenam e. If `logstorename` does not exist, this string is left blank. iii. If the request contains a query string ( `QUERY_STRING` ), add a question mark ( ? ) and the query string at the end of the CanonicalizedResource string.

| QUERY STRING _ | is th |
|---|---|
| URL. Equal signs ( | = |

In the request, `QUERY_STRING` is the lexicographically sorted string of the request parameters included in the URL. Equal signs ( `=` ) are used between the names and values of parameters to form a string. The name-value pairs are then sorted in lexicographical order and connected with ampersands ( `&` ) to form a string. The formula is described as follows:

```
QUERY_STRING = "KEY1=VALUE1" + "&" + "KEY2=VALUE2"
```

3. Generate a digital signature for the request.
Log Service API operations support only the `hmac-sha1` digital signature algorithm, which is also the default signature algorithm. The signature formula is as follows:

```
Signature = base64(hmac-sha1(UTF8-Encoding-Of(SignString), AccessKeySecret))
```

The HMAC-SHA1 method defined in RFC 2104 is used as the signature method. The AccessKey secret used in the preceding formula must match the AccessKey ID in the final Authorization field. Otherwise, the request cannot be verified by Log Service. After the digital signature is generated, use the signature to construct a complete security verification header for the API request. Then, enter the security verification header in the HTTP request and send the request. Examples The following two examples demonstrate how to sign an API request. In the examples, the AccessKey pair you use to sign the API request is as follows:

```
AccessKeyId = "<yourAccessKeyId>" AccessKeySecret = "<yourAccessKeySecret>"
```

Example 1: you want to send the following GET request to list all Logstores in the ali-test-project project:

```
GET /logstores HTTP 1.1 Mon, 09 Nov 2015 06:11:16 GMT Host: ali-test-project.regionid.example.com x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1
```

The following signature string is generated for the API request:

```
GET\n\n\nMon, 09 Nov 2015 06:11:16 GMT\nx-log-apiversion:0.6.0\nx-log-signaturemethod:hma c-sha1\n/logstores? logstoreName=&offset=0&size=1000
```

The CONTENT-TYPE and CONTENT-MD5 fields are empty because the GET request does not have an HTTP body. If the AccessKey secret is used to generate a signature, the signature is as follows:

```
jEYOTCJs2e88o+y5F4/S5IsnBJQ=
```

The digitally signed HTTP request is as follows:

```
GET /logstores HTTP 1.1 Mon, 09 Nov 2015 06:11:16 GMT Host: ali-test-project.regionid.example.com x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1 Authorization: LOG <yourAccessKeyId>:<yourSignature>
```

Example 2: You want to write the following log to the Logstore named test-logstore in the ali-testproject project:

```json
topic="" time=1447048976 source="10.10.10.1" "TestKey": "TestContent"
```

The following HTTP request must be constructed based on the Log Service API definition:

```
POST /logstores/test-logstore HTTP/1.1 Date: Mon, 09 Nov 2015 06:03:03 GMT Host: test-project.regionid.example.com x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1 Content-MD5: 1DD45FA4A70A9300CC9FE7305AF2C494 Content-Length: 52 x-log-apiversion:0.6.0 x-log-bodyrawsize:50 x-log-compresstype:lz4 x-log-signaturemethod:hmac-sha1 <The log is serialized to byte streams in the ProtoBuffer format.>
```

In this HTTP request, the log is first serialized to byte streams in the ProtoBuffer format and then used as the request body. For more information, see Data encoding. The value of the Content-Type header field value in this request is application/x-protobuf. The value of the Content-MD5 header field is the MD5 value that corresponds to the request body. The signature string of this request is as follows:

```
POST\n1DD45FA4A70A9300CC9FE7305AF2C494\napplication/x-protobuf\nMon, 09 Nov 2015 06:03:03 GMT\nx-log-apiversion:0.6.0\nx-log-bodyrawsize:50\nx-log-compresstype:lz4\nx-log-signatur emethod:hmac-sha1\n/logstores/test-logstore
```

If the AccessKey secret is used to generate a signature, the signature is as follows:

```
XWLGYHGg2F2hcfxWxMLiNkGki6g=
```

The digitally signed HTTP request is as follows:

```
POST /logstores/test-logstore HTTP/1.1 Date: Mon, 09 Nov 2015 06:03:03 GMT Host: test-project.regionid.example.com x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1 Content-MD5: 1DD45FA4A70A9300CC9FE7305AF2C494 Content-Length: 52 x-log-apiversion:0.6.0 x-log-bodyrawsize:50 x-log-compresstype:lz4 x-log-signaturemethod:hmac-sha1 Authorization: LOG <yourAccessKeyId>:<yourSignature> <The log is serialized to byte streams in the ProtoBuffer format.>
```

### 1.5 Common error codes

When an API request error occurs, Log Service returns an error message, including the HTTP status code and the specific error details in the response body. The error details in the response body are formatted as follows:

```json
"errorCode" : <ErrorCode>, "errorMessage" : <ErrorMessage>
```

Some of the error messages that may be returned by Log Service apply to most APIs and are defined as common error codes. The other error messages apply only to some APIs and are defined as special error codes. The unique error codes of an API are described in the relevant API reference. Common error codes

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 411 | MissingContentLeng th | Content-Length does not exist in http header when it is necessary. | The error message returned because the required Content- Length field does not exist in the request header. |
| 415 | InvalidContentType | Content-Type {type} is unsupported. | The error message returned because the specified Content- Type is not supported. |
| 400 | MissingContentType | Content-Type does not exist in http header when body is not empty. | The error message returned because the Content-Type header field is not specified when the HTTP request body is not empty. |
| 400 | MissingBodyRawSize | x-log-bodyrawsize does not exist in header when it is necessary. | The error message returned because the required x-log- bodyrawsize field does not exist in the request header in the compression scenario. |

| eveloper Guide· | API Reference |   | Log Servic |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidBodyRawSize | x-log-bodyrawsize is invalid. | The error message returned because the x-log-bodyrawsize value is invalid. |
| 400 | InvalidCompressTyp e | x-log-compresstype {type} is unsupported. | The error message returned because the compression type specified in the x-log- compresstype parameter is not supported. |
| 400 | MissingHost | Host does not exist in http header. | The error message returned because the Host field does not exist in the HTTP request header. |
| 400 | MissingDate | Date does not exist in http header. | The error message returned because the Data field does not exist in the HTTP request header. |
| 400 | InvalidDateFormat | Date {date} must follow RFC822. | The error message returned because the value of the Date field in the request header does not comply with the RFC 822 standard. |
| 400 | MissingAPIVersion | x-log-apiversion does not exist in http header. | The error message returned because the x-log-apiversion field does not exist in the HTTP request header. |
| 400 | InvalidAPIVersion | x-log-apiversion {version} is unsupported. | The error message returned because the value of the x-log- apiversion field in the HTTP request header is not supported. |
| 400 | MissAccessKeyId | x-log-accesskeyid does not exist in header. | The error message returned because no AccessKey ID exists in the Authorization header field. |
| 401 | Unauthorized | The AccessKeyId is unauthorized. | The error message returned because the specified AccessKey ID is unauthorized. |
| 400 | MissingSignatureMet hod | x-log-signaturemethod does not exist in http header. | The error message returned because the x-log- signaturemethod field does not exist in the HTTP request header. |
| 400 | InvalidSignatureMeth od | signature method {method} is unsupported. | The error message returned because the signature method specified in the x-log- signaturemethod header field is not supported. |

| og Service |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | RequestTimeTooSke wed | Request time exceeds server time more than 15 minutes. | The error message returned because the request sending time is more than 15 minutes before or after the current server time. |
| 404 | ProjectNotExist | Project {name} does not exist. | The error message returned because the specified project does not exist. |
| 401 | SignatureNotMatch | Signature {signature} is not matched. | The error message returned because the digital signature of the request does not match the signature computed in Log Service. |
| 403 | WriteQuotaExceed | Write quota is exceeded. | The error message returned because the log write quota is exceeded. |
| 403 | ReadQuotaExceed | Read quota is exceeded. | The error message returned because the log read quota is exceeded. |
| 500 | InternalServerError | Internal server error message. | The error message returned because an internal server error occurred. |
| 503 | ServerBusy | The server is busy, please try again later. | The error message returned because the server is busy. Try again later. |

The {…} in the error message indicates the specific error information. For example, {name} in the ProjectNotExist error message is replaced by a specific project name.

### 1.6 Project API

#### 1.6.1 CreateProject

Creates a project. Request syntax

```json
POST / HTTP/1.1 Authorization: <AuthorizationString> x-log-bodyrawsize: 0 User-Agent: <UserAgent> x-log-apiversion: 0.6.0 Host: <Project Endpoint> x-log-signaturemethod: hmac-sha1 Date: <GMT Date> Content-Type: application/json Content-MD5: <Content-MD5> Content-Length: <ContentLength> Connection: Keep-Alive
  "projectName": <ProjectName>,
  "description": <Description>
```

Request elements Request headers The CreateProject API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| projectName | String | Yes | The name of the project. |
| description | String | Yes | The description of the project. |

Response elements Response headers The CreateProject API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters The HTTP status code 200 is returned. Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 400 | ProjectAlreadyExist | Project {project} already exist |
| 400 | ParameterInvalid | The body is not valid json string |

| og Service |   | Developer Guide·API Referenc |
|---|---|---|

| HTTP status code | Error code | Error message |
|---|---|---|
| 500 | InternalServerError | Specified Server Error Message |

Examples Sample requests

```json
POST / HTTP/1.1 Authorization: LOG <yourAccessKeyId>:<yourSignature> x-log-bodyrawsize: 0 User-Agent: sls-java-sdk-v-0.6.1 x-log-apiversion: 0.6.0 Host: my-project-test.cn-shanghai.log.aliyuncs.com x-log-signaturemethod: hmac-sha1 Date: Sun, 27 May 2018 07:43:26 GMT Content-Type: application/json Content-MD5: A7967D81EFF5E3CD447FB6D8DF294E20 Content-Length: 80 Connection: Keep-Alive
  "projectName": "my-project-test",
  "description": "Description of my-project-test"
```

Sample responses

```
HTTP/1.1 200 Server: nginx Content-Length: 0 Connection: close Access-Control-Allow-Origin: * Date: Sun, 27 May 2018 07:43:27 GMT x-log-requestid: 5B0A619F205DC3F30EDA9322
```

#### 1.6.2 DeleteProject

Deletes a project. Request syntax

```
DELETE / HTTP/1.1 Authorization: <AuthorizationString> x-log-bodyrawsize: 0 User-Agent: <UserAgent> x-log-apiversion: 0.6.0 Host: <Project Endpoint> x-log-signaturemethod: hmac-sha1 Date: <GMT Date> Content-Type: application/x-protobuf Connection: Keep-Alive
```

Request elements Request headers The DeleteProject API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| projectName | String | Yes | The name of the project. The name is a part of the Host parameter in the header. |

Response elements Response headers The DeleteProject API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters The HTTP status code 200 is returned. Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 404 | ProjectNotExist | The project does not exist: {project} |
| 500 | InternalServerError | Specified Server Error Message |

Examples Sample requests

```
DELETE / HTTP/1.1 Authorization: LOG <yourAccessKeyId>:<yourSignature> x-log-bodyrawsize: 0 User-Agent: sls-java-sdk-v-0.6.1 x-log-apiversion: 0.6.0 Host: my-project-test.cn-shanghai.log.aliyuncs.com x-log-signaturemethod: hmac-sha1 Date: Sun, 27 May 2018 08:25:04 GMT Content-Type: application/x-protobuf Connection: Keep-Alive
```

Sample responses

```
HTTP/1.1 200 Server: nginx Content-Length: 0 Connection: close Access-Control-Allow-Origin: * Date: Sun, 27 May 2018 08:25:04 GMT x-log-requestid: 5B0A6B60BB6EE39764D458B5
```

#### 1.6.3 UpdateProject

Modifies a project. Request syntax

```
PUT / HTTP/1.1 Authorization: <AuthorizationString> x-log-bodyrawsize: 0 User-Agent: <UserAgent> x-log-apiversion: 0.6.0 Host: <Project Endpoint> x-log-signaturemethod: hmac-sha1 Date: <GMT Date> Content-Type: application/json Content-MD5: <Content-MD5> Content-Length: <ContentLength> Connection: Keep-Alive
```

Request elements Request headers The UpdateProject API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| projectName | String | Yes | The name of the project. The name is a part of the Host parameter in the header. |
| description | String | Yes | The description of the project. The value is an empty string by default. |

Response elements Response headers The UpdateProject API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters The HTTP status code 200 is returned. Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 404 | ProjectNotExist | The project does not exist: <Project> |
| 400 | ParameterInvalid | The body is not valid json string |
| 500 | InternalServerError | Specified Server Error Message |

Examples Sample requests

```json
PUT / HTTP/1.1 Authorization: LOG <yourAccessKeyId>:<yourSignature> x-log-bodyrawsize: 0 User-Agent: sls-java-sdk-v-0.6.1 x-log-apiversion: 0.6.0 Host: my-project-test.cn-shanghai.log.aliyuncs.com x-log-signaturemethod: hmac-sha1 Date: Sun, 27 May 2018 07:43:26 GMT Content-Type: application/json Content-MD5: A7967D81EFF5E3CD447FB6D8DF294E20 Content-Length: 40 Connection: Keep-Alive
  "description": "Description of my-project-test"
```

Sample responses

```
HTTP/1.1 200 Server: nginx Content-Length: 0 Connection: close Access-Control-Allow-Origin: * Date: Sun, 27 May 2018 07:43:27 GMT x-log-requestid: 5B0A619F205DC3F30EDA9322
```

#### 1.6.4 GetProject

Queries a project based on the project name. Request syntax

```
GET / HTTP/1.1 Authorization: <AuthorizationString> x-log-bodyrawsize: 0 User-Agent: <UserAgent> x-log-apiversion: 0.6.0 Host: <Project Endpoint> x-log-signaturemethod: hmac-sha1 Date: <GMT Date> Content-Type: application/x-protobuf Connection: Keep-Alive
```

Request elements Request headers The GetProject API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| projectName | String | Yes | The name of the project. The name is a part of the Host parameter in the header. |

Response elements Response headers The GetProject API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters After the request succeeds, the response body contains the details of the project. The following table describes the response parameters.

| Parameter | Type | Description |
|---|---|---|
| createTime | String | The time when the project was created. |
| description | String | The description of the project. |
| lastModifyTime | String | The time when the project was last modified. |
| owner | String | The ID of the account that was used to create the project. |
| projectName | String | The name of the project. |

| veloper Guide·API Reference |   | Log Servic |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| status | String | The status of the project. |
| region | String | The region to which the project belongs. |

Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 404 | ProjectNotExist | The project does not exist: {project} |
| 500 | InternalServerError | Specified Server Error Message |

Examples Sample requests

```
GET / HTTP/1.1 Authorization: LOG <yourAccessKeyId>:<yourSignature> x-log-bodyrawsize: 0 User-Agent: sls-java-sdk-v-0.6.1 x-log-apiversion: 0.6.0 Host: my-project-test.cn-shanghai.log.aliyuncs.com x-log-signaturemethod: hmac-sha1 Date: Sun, 27 May 2018 08:25:04 GMT Content-Type: application/x-protobuf Connection: Keep-Alive
```

Sample responses

```
HTTP/1.1 200 Server: nginx Content-Length: 0 Connection: close Access-Control-Allow-Origin: * Date: Sun, 27 May 2018 08:25:04 GMT x-log-requestid: 5B0A6B60BB6EE39764D458B5
```

#### 1.6.5 ListProject

Lists all projects. Request syntax

```
GET /? offset={offset}&size={size} HTTP/1.1 Authorization: <AuthorizationString> x-log-bodyrawsize: 0 User-Agent: <UserAgent> x-log-apiversion: 0.6.0 Host: <Endpoint> x-log-signaturemethod: hmac-sha1 Date: <GMT Date> Content-Type: application/x-protobuf Connection: Keep-Alive
```

Request elements Request headers The ListProject API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| offset | Integer | No | The start position of the records to return. Default value: 0. |
| size | Integer | No | The maximum number of entries to return on each page. Default and maximum value: 500. |

Response elements Response headers The ListProject API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters After the request succeeds, the response body contains the project list. The following table describes the response parameters.

| Parameter | Type | Description |
|---|---|---|
| count | Integer | The number of returned projects on each page. |
| total | Integer | The total number of ruturned projects. |
| projects | Array | The list of projects. |

The following table describes the elements of the projects parameter.

| Element | Type | Description |
|---|---|---|
| createTime | String | The time when the project was created. |
| description | String | The description of the project. |
| lastModifyTime | String | The time when the project was last modified. |
| owner | String | The ID of the account that was used to create the project. |
| projectName | String | The name of the project. |
| status | String | The status of the project. |
| region | String | The region to which the project belongs. |

Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 500 | InternalServerError | Specified Server Error Message |

Examples Sample requests

```
GET /? offset=0&size=2&projectName= HTTP/1.1 Authorization: LOG <yourAccessKeyId>:<yourSignature> x-log-bodyrawsize: 0 User-Agent: sls-java-sdk-v-0.6.1 x-log-apiversion: 0.6.0 Host: cn-shanghai.log.aliyuncs.com x-log-signaturemethod: hmac-sha1 Date: Sun, 27 May 2018 09:03:33 GMT Content-Type: application/x-protobuf Connection: Keep-Alive
```

Sample responses

```json
HTTP/1.1 200 Server: nginx Content-Type: application/json Content-Length: 345 Connection: close Access-Control-Allow-Origin: * Date: Sun, 27 May 2018 09:03:33 GMT x-log-requestid: 5B0A7465AAEA20CA70DE3064
  "count": 2,
  "total": 11,
  "projects": [
      "projectName": "project1",
      "status": "Normal",
      "owner": "",
      "description": "",
      "region": "cn-shanghai",
      "createTime": "1524222931",
      "lastModifyTime": "1524539357"
```

`},`

```json
      "projectName": "project123456",
      "status": "Normal",
      "owner": "",
      "description": "",
      "region": "cn-shanghai",
      "createTime": "1471963876",
      "lastModifyTime": "1524539357"
```

`]`

#### 1.6.6 GetProjectLogs

Queries logs in a project by using an SQL statement. Request syntax The request syntax of the GetProjectLogs API operation is as follows:

```
GET /logs query=SELECT avg(latency) as avg_latency FROM where __date__ >'2017-09-01 00:00: 00' and __date__ < '2017-09-02 00:00:00' Authorization: <AuthorizationString> Date: Wed, 3 Sept. 2014 08:33:46 GMT Host: big-game.cn-hangzhou.log.aliyuncs.com x-log-bodyrawsize: 0 x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1
```

Request elements Request headers The GetProjectLogs API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| query | String | Yes | The SQL statement that is used for the query. |

Response elements Response headers For information about common response headers of Log Service API operations, see Common response headers. The following table describes the special response parameters of the GetProjectLogs API operation.

| Parameter | Type | Description |
|---|---|---|
| x-log-progress | String | The status of the query results. Valid values: Incomplete and Complete. |
| x-log-count | Integer | The total number of logs in the current query results. |
| x-log-processed-rows | Integer | The number of rows processed in the query. |
| x-log-elapsed- millisecond | Integer | The number of milliseconds consumed by the query. |

Response parameters The response body of the GetProjectLogs API operation is an array. Each element in the array is a log. The following table describes the response parameters.

| Parameter | Type | Description |
|---|---|---|
| time __ __ | Integer | The log timestamp. This parameter indicates the number of seconds that have elapsed since the Unix epoch 00:00:00 UTC on January 1, 1970. |
| source __ __ | String | The log source, which is specified when logs are written. |
| [content] | Key-Value pair | The original content of logs. |

Additional considerations The query statement that is used in this API operation is a standard SQL statement. You must specify a project in the domain name of the request. You must specify a Logstore in the FROM condition of the query statement. A Logstore can be regarded as a SQL table. You must specify a time range in the SQL statement by using the __date__ parameter (timestamp) or __time__ parameter (Unix timestamp). If the number of logs in the Logstore significantly changes, Log Service cannot predict how many times this API operation needs to be called to obtain the complete results. In this case, you must check the value of the x-log-progress parameter in the returned results of each request. Based on the value, you can determine whether to repeatedly call this API operation to obtain the complete results.

> Not e The same number of query compute units (CUs) is consumed each time you call this API operation.

Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | ParameterInvalid | parameter is invalid | The error message returned because the specified request parameter is invalid. |

Example In this example, the logs with the groupA topic are queried in a Logstore named app_log. The Logstore belongs to a project named big-game in the China (Hangzhou) region. The time range is from 2014-09- 01 00:00:00 to 2014-09-01 22:00:00 and the keyword is "error". The query starts from the beginning of the time range. A maximum of 20 logs can be returned. Sample requests

```
GET /logs/? query=SELECT * FROM <logStoreName> where __line__ = 'abc' and __date__ >'2017 -09-01 00:00:00' and __date__ < '2017-09-02 00:00:00'&line=20&offset=0 HTTP/1.1 Authorization: <AuthorizationString> Date: Wed, 3 Sept. 2014 08:33:46 GMT Host: big-game.cn-hangzhou.log.aliyuncs.com x-log-bodyrawsize: 0 x-log-apiversion: 0.4.0 x-log-signaturemethod: hmac-sha1
```

Sample responses

```json
HTTP/1.1 200 OK Content-MD5: 36F9F7F0339BEAF571581AF1B0AAAFB5 Content-Type: application/json Content-Length: 269 Date: Wed, 3 Sept. 2014 08:33:47 GMT x-log-requestid: efag01234-12341-15432f x-log-progress : Complete x-log-count : 10000 x-log-processed-rows: 10000 x-log-elapsed-millisecond:5
    "progress": "Complete",
    "count": 2,
    "logs": [
            "__time__": 1409529660,
            "__source__": "10.237.0.17",
            "Key1": "error",
            "Key2": "Value2"
```

`},`

```json
            "__time__": 1409529680,
            "__source__": "10.237.0.18",
            "Key3": "error",
            "Key4": "Value4"
```

`]` In the sample response, the x-log-progress value is Complete. This indicates that the log query is completed and the returned results are complete. In this query, two logs that meet the query conditions are found. If the x-log-progress value is Incomplete, you must repeat the request to obtain the complete results.

### 1.7 Logstore operations

#### 1.7.1 CreateLogstore

Creates a Logstore. Request syntax The request syntax of the CreateLogstore API operation is as follows:

```json
POST /logstores HTTP/1.1 Authorization: <AuthorizationString> Date: <GMT Date> Host: <Project Endpoint> x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1
    "logstoreName" : <logStoreName>,
    "ttl": <ttl>,
    "shardCount": <shardCount>,
    "autoSplit": <autoSplit>,
    "maxSplitShard": <maxSplitShard>
```

Request elements Request headers The CreateLogstore API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| logstoreName | String | Yes | The name of the Logstore. The name must be unique in a project. |
| ttl | Integer | Yes | The time to live (TTL) of log data. Unit: days. Valid values: 1 to 3600. |
| shardCount | Integer | Yes | The number of shards. Valid values: 1 to 100. |
| enable tracking _ | Boolean | No | Specifies whether to enable the WebTracking feature. Default value: false. |
| autoSplit | Boolean | No | Specifies whether to enable automatic sharding. Default value: false. |
| maxSplitShard | Integer | No | The maximum number of shards for automatic sharding. Valid values: 1 to 64. Default value: 64. This parameter must be specified if the autoSplit parameter is set to true. |

Response elements Response headers The CreateLogstore API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common request headers. Response parameters The HTTP status code 200 is returned. Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 400 | LogstoreAlreadyExist | logstore {logstoreName} already exists |
| 500 | InternalServerError | Specified Server Error Message |
| 400 | LogstoreInfoInvalid | logstore info is invalid |
| 400 | ProjectQuotaExceed | Project Quota Exceed |

Examples Sample requests

```json
POST /logstores HTTP/1.1 Header : x-log-apiversion=0.6.0, Authorization=LOG <yourAccessKeyId>:<yourSignature>, Host=ali-test-project.cn-hangzhou-devcommon-intranet.sls.aliyuncs.com, Date=Wed, 11 Nov 2015 07:35:00 GMT, Content-Length=55, x-log-signaturemethod=hmac-sha1, Content-MD5=7EF43D0B8F4A807B95E775048C911C72, User-Agent=sls-java-sdk-v-0.6.0, Content-Type=application/json Body :
    "logstoreName": "test-logstore",
    "ttl": 1,
    "shardCount": 2,
    "autoSplit": true,
    "maxSplitShard": 64
```

Sample responses

```
HTTP/1.1 200 OK Header: Date=Wed, 11 Nov 2015 07:35:00 GMT, Content-Length=0, x-log-requestid=5642EFA499248C827B012B39, Connection=close, Server=nginx/1.6.1
```

#### 1.7.2 DeleteLogstore

Deletes a Logstore, including all shards and indexes of the Logstore. Request syntax

```
DELETE /logstores/{logstoreName} HTTP/1.1 Authorization: <AuthorizationString> Date: <GMT Date> Host: <Project Endpoint> x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1
```

Request parameters Request headers The DeleteLogstore API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| logstoreName | String | Yes | The name of the Logstore. The name must be unique in a project. |

Response parameters Response headers The DeleteLogstore API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters The HTTP status code 200 is returned. Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 404 | LogStoreNotExist | logstore {logstoreName} does not exist |
| 500 | InternalServerError | Specified Server Error Message |

Examples Sample requests

```
DELETE /logstores/test_logstore HTTP/1.1 Header : x-log-apiversion=0.6.0, Authorization=LOG <yourAccessKeyId>:<yourSignature>, Host=ali-test-project.cn-hangzhou-devcommon-intranet.sls.aliyuncs.com, Date=Wed, 11 Nov 2015 08:09:38 GMT, Content-Length=0, x-log-signaturemethod=hmac-sha1, User-Agent=sls-java-sdk-v-0.6.0, Content-Type=application/json
```

Sample responses

```
HTTP/1.1 200 OK Header: Date=Wed, 11 Nov 2015 08:09:39 GMT, Content-Length=0, x-log-requestid=5642F7C399248C817B013A07, Connection=close, Server=nginx/1.6.1
```

#### 1.7.3 UpdateLogstore

Updates the attributes of a Logstore. Only the time to live (TTL) and shard attributes can be updated. Request syntax

```json
PUT /logstores/{logstoreName} HTTP/1.1 Authorization: <AuthorizationString> Date: <GMT Date> Host: <Project Endpoint> x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1
    "logstoreName": <logstoreName>,
    "ttl": <ttl>,
    "shardCount": <shardCount>,
    "autoSplit": <autoSplit>,
    "maxSplitShard": <maxSplitShard>
```

Request elements Request headers The UpdateLogstore API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| logstoreName | String | Yes | The name of the Logstore. The name must be unique in a project. |
| ttl | Integer | Yes | The time to live (TTL) of log data. Unit: days. Valid values: 1 to 3600. |
| shardCount | Integer | Yes | The number of shards. After the attributes of a Logstore are updated, the number of shards is unchanged. You can only call the SplitShard or MergeShards operation to change the number of shards. |
| enable tracking _ | Boolean | No | Specifies whether to enable the WebTracking feature. |
| autoSplit | Boolean | No | Specifies whether to enable automatic sharding. |
| maxSplitShard | Integer | No | The maximum number of shards for automatic sharding. Valid values: 1 to 64. This parameter must be specified if the autoSplit parameter is set to true. |

Response elements Response headers The UpdateLogstore API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters The HTTP status code 200 is returned. Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 404 | ProjectNotExist | Project {ProjectName} does not exist |
| 404 | LogStoreNotExist | logstore {logstoreName} does not exist |
| 400 | LogStoreAlreadyExist | logstore {logstoreName} already exists |
| 500 | InternalServerError | Specified Server Error Message |
| 400 | ParameterInvalid | invalid shard count,you can only modify shardCount by split& merge shard |

Additional considerations You can modify the number of shards be only calling the SplitShard or MergeShards API operation. Examples Sample requests

```json
PUT /logstores/test-logstore HTTP/1.1 Header: x-log-apiversion=0.6.0, Authorization=LOG <yourAccessKeyId>:<yourSignature>, Host=ali-test-project.cn-hangzhou-devcommon-intranet.sls.aliyuncs.com, Date=Wed, 11 Nov 2015 08:28:19 GMT, Content-Length=55, x-log-signaturemethod=hmac-sha1, Content-MD5=757C60FC41CC7D3F60B88E0D916D051E, User-Agent=sls-java-sdk-v-0.6.0, Content-Type=application/json Body :
    "logstoreName": "test-logstore",
    "ttl": 1,
    "shardCount": 2,
    "autoSplit": true,
    "maxSplitShard": 64
```

Sample responses

```
HTTP/1.1 200 OK Header: Date=Wed, 11 Nov 2015 08:28:20 GMT, Content-Length=0, x-log-requestid=5642FC2399248C8F7B0145FD, Connection=close, Server=nginx/1.6.1
```

#### 1.7.4 GetLogstore

Queries the attributes of a Logstore. Request syntax

```
GET /logstores/{logstoreName} HTTP/1.1 Authorization: <AuthorizationString> Date: <GMT Date> Host: <Project Endpoint> x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1
```

Request elements Request headers The GetLogstore API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| logstoreName | String | Yes | The name of the Logstore. The name must be unique in a project. |

Response elements Response headers The GetLogstore API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters The HTTP status code 200 is returned.

```json
    "logstoreName" : <logstoreName>,
    "ttl": <ttl>,
    "shardCount": <shardCount>,
    "createTime": <createTime>,
    "lastModifyTime": <lastModifyTime>
```

Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 404 | ProjectNotExist | Project {ProjectName} does not exist |
| 404 | LogstoreNotExist | logstore {logstoreName} does not exist |
| 500 | InternalServerError | Specified Server Error Message |

Examples Sample requests

```
GET /logstores/test-logstore HTTP/1.1 Header : x-log-apiversion=0.6.0, Authorization=LOG <yourAccessKeyId>:<yourSignature>, Host=ali-test-project.cn-hangzhou-devcommon-intranet.sls.aliyuncs.com, Date=Wed, 11 Nov 2015 07:53:29 GMT, Content-Length=0, x-log-signaturemethod=hmac-sha1, User-Agent=sls-java-sdk-v-0.6.0, Content-Type=application/json
```

Sample responses

```json
HTTP/1.1 200 OK Header : Date=Wed, 11 Nov 2015 07:53:30 GMT, Content-Length=107, x-log-requestid=5642F3FA99248C817B01352D, Connection=close, Content-Type=application/json, Server=nginx/1.6.1 Body :
    "logstoreName": test-logstore,
    "ttl": 1,
    "shardCount": 2,
    "createTime": 1447833064,
    "lastModifyTime": 1447833064
```

#### 1.7.5 ListLogstore

Lists all Logstores in a specified project. Request syntax

```
GET /logstores HTTP/1.1 Authorization: <AuthorizationString> Date: <GMT Date> Host: <Project Endpoint> x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1
```

Request elements Request headers The ListLogstore API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| offset | Integer | No | The start position of the records to return. Default value: 0. |
| size | Integer | No | The maximum number of entries to return on each page. Default and maximum value: 500. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| logstoreName | String | Yes | The Logstore name that is used as a filtering condition. Fuzzy match is used. |

Response elements Response headers The ListLogstore API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters After a ListLogstore request succeeds, the response body contains a list of all Logstores in the specified project. The following table describes the response parameters.

| Parameter | Type | Description |
|---|---|---|
| count | Integer | The number of returned Logstores. |
| total | Integer | The total number of Logstores. |
| logstores | String array | The name list of returned Logstores. |

Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 404 | ProjectNotExist | Project {ProjectName} does not exist |
| 500 | InternalServerError | Specified Server Error Message |
| 400 | ParameterInvalid | Invalid parameter size, (0.6.0] |
| 400 | InvalidLogStoreQuery | logstore Query is invalid |

Examples Sample requests

```
GET /logstores HTTP/1.1 Header: x-log-apiversion=0.6.0, Authorization=LOG <yourAccessKeyId>:<yourSignature>, Host=ali-test-project.cn-hangzhou-devcommon-intranet.sls.aliyuncs.com, Date=Wed, 11 Nov 2015 08:09:39 GMT, Content-Length=0, x-log-signaturemethod=hmac-sha1, User-Agent=sls-java-sdk-v-0.6.0, Content-Type=application/json
```

Sample responses

```json
HTTP/1.1 200 OK Header: Date=Wed, 11 Nov 2015 08:09:39 GMT, Content-Length=52, x-log-requestid=5642F7C399248C8D7B01342F, Connection=close, Content-Type=application/json, Server=nginx/1.6.1 Body: "count":1, "logstores":["test-logstore"], "total":1
```

#### 1.7.6 ListShards

Lists all available shards in a Logstore. Request syntax

```
GET /logstores/<logstorename>/shards HTTP/1.1 Authorization: <AuthorizationString> Date: <GMT Date> Host: <Project Endpoint> x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1
```

Request elements Request headers The ListShards API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| logstoreName | String | Yes | The name of the Logstore. |

Response elements Response headers The ListShards API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response elements The response is an array that consists of shards. `[`

```json
        "shardID": 0,
        "status": "readwrite",
        "inclusiveBeginKey": "00000000000000000000000000000000",
        "exclusiveEndKey": "8000000000000000000000000000000",
        "createTime": 1453949705
```

`},`

```
        ...
```

`},`

```
        ...
```

`]` Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 404 | LogStoreNotExist | logstore {logstoreName} does not exist |
| 500 | InternalServerError | Specified Server Error Message |
| 400 | LogStoreWithoutShard | logstore has no shard |

> Not e The {logstoreName} variable in the preceding error message is replaced with a specific Logstore name.

Examples Sample requests

```json
GET /logstores/sls-test-logstore/shards Header :
    "Content-Length": 0,
    "x-log-signaturemethod": "hmac-sha1",
    "x-log-bodyrawsize": 0,
    "User-Agent": "log-python-sdk-v-0.6.0",
    "Host": "ali-test-project.cn-hangzhou-devcommon-intranet.sls.aliyuncs.com",
    "Date": "Thu, 12 Nov 2015 03:40:31 GMT",
    "x-log-apiversion": "0.6.0",
    "Authorization": "LOG <yourAccessKeyId>:<yourSignature>"
```

Sample responses

```json
Header:
    "content-length": "57",
    "server": "nginx/1.6.1",
    "connection": "close",
    "date": "Thu, 12 Nov 2015 03:40:31 GMT",
    "content-type": "application/json",
    "x-log-requestid": "56440A2F99248C050600C74C"
Body :
```

`[`

```json
        "shardID": 1,
        "status": "readwrite",
        "inclusiveBeginKey": "00000000000000000000000000000000",
        "exclusiveEndKey": "8000000000000000000000000000000",
        "createTime": 1453949705
```

`},`

```json
        "shardID": 2,
        "status": "readwrite",
        "inclusiveBeginKey": "80000000000000000000000000000000",
        "exclusiveEndKey": "ffffffffffffffffffffffffffffffff",
        "createTime": 1453949705
```

`},`

```json
        "shardID": 0,
        "status": "readonly",
        "inclusiveBeginKey": "00000000000000000000000000000000",
        "exclusiveEndKey": "ffffffffffffffffffffffffffffffff",
        "createTime": 1453949705
```

`]`

#### 1.7.7 SplitShard

Splits a specified shard in the read/write state. Request syntax

```
POST /logstores/<logstorename>/shards/<shardid>? action=split&key=<splitkey> HTTP/1.1 Authorization: <AuthorizationString> Date: <GMT Date> Host: <Project Endpoint> x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1
```

Request elements Request headers The SplitShard API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| logstoreName | String | Yes | The name of the Logstore. |
| shardid | Integer | Yes | The ID of the shard. |
| splitkey | String | Yes | The location where the shard is split. |

Response elements Response headers Content-Type: application/json The SplitShard API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters The response is an array that consists of three shards. The first shard is the original shard. The second and third shards are the new shards that are created by splitting the original shard. `[`

```json
        "shardID": 33,
        "status": "readonly",
        "inclusiveBeginKey": "ee000000000000000000000000000000",
        "exclusiveEndKey": "ffffffffffffffffffffffffffffffff",
        "createTime": 1453949705
```

`},`

```json
        "shardID": 163,
        "status": "readwrite",
        "inclusiveBeginKey": "ee000000000000000000000000000000",
        "exclusiveEndKey": "ef000000000000000000000000000000",
        "createTime": 1453949705
```

`},`

```json
        "shardID": 164,
        "status": "readwrite",
        "inclusiveBeginKey": "ef000000000000000000000000000000",
        "exclusiveEndKey": "ffffffffffffffffffffffffffffffff",
        "createTime": 1453949705
```

`]` Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 404 | LogStoreNotExist | logstore {logstoreName} does not exist |
| 400 | ParameterInvalid | invalid shard id |
| 400 | ParameterInvalid | invalid mid hash |
| 500 | InternalServerError | Specified Server Error Message |
| 400 | LogStoreWithoutShard | logstore has no shard |

> Not e The {logstoreName} variable in the preceding error message is replaced with a specific Logstore name.

Examples Sample requests

```json
POST /logstores/logstorename/shards/33? action=split&key=ef000000000000000000000000000000 Header :
    "Content-Length": 0,
    "x-log-signaturemethod": "hmac-sha1",
    "x-log-bodyrawsize": 0,
    "User-Agent": "log-python-sdk-v-0.6.0",
    "Host": "ali-test-project.cn-hangzhou.sls.aliyuncs.com",
    "Date": "Thu, 12 Nov 2015 03:40:31 GMT",
    "x-log-apiversion": "0.6.0",
    "Authorization": "LOG <yourAccessKeyId>:<yourSignature>"
```

Sample responses

```json
Header:
    "content-length": "57",
    "server": "nginx/1.6.1",
    "connection": "close",
    "date": "Thu, 12 Nov 2015 03:40:31 GMT",
    "content-type": "application/json",
    "x-log-requestid": "56440A2F99248C050600C74C"
Body :
```

`[`

```json
        "shardID": 33,
        "status": "readonly",
        "inclusiveBeginKey": "ee000000000000000000000000000000",
        "exclusiveEndKey": "ffffffffffffffffffffffffffffffff",
        "createTime": 1453949705
```

`},`

```json
        "shardID": 163,
        "status": "readwrite",
        "inclusiveBeginKey": "ee000000000000000000000000000000",
        "exclusiveEndKey": "ef000000000000000000000000000000",
        "createTime": 1453949705
```

`},`

```json
        "shardID": 164,
        "status": "readwrite",
        "inclusiveBeginKey": "ef000000000000000000000000000000",
        "exclusiveEndKey": "ffffffffffffffffffffffffffffffff",
        "createTime": 1453949705
```

`]`

#### 1.7.8 MergeShards

Merges two adjacent shards that are in the read/write state. If you specify the ID of a shard in the request, Log Service automatically finds the adjacent shard. Request syntax

```
POST /logstores/<logstorename>/shards/<shardid>? action=merge HTTP/1.1 Authorization: <AuthorizationString> Date: <GMT Date> Host: <Project Endpoint> x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1
```

Request elements Request headers The MergeShards API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| logstoreName | String | Yes | The name of the Logstore. |
| shardid | Integer | Yes | The ID of the shard. |

Response elements Response headers Content-Type: application/json The MergeShards API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters An array that consists of three shards is returned. The first shard is the merged shard. The other two shards are the original shards. `[`

```json
        'shardID': 167,
        'status': 'readwrite',
        'inclusiveBeginKey': 'e0000000000000000000000000000000',
        'createTime': 1453953105,
        'exclusiveEndKey': 'ffffffffffffffffffffffffffffffff'
```

`},`

```json
        'shardID': 30,
        'status': 'readonly',
        'inclusiveBeginKey': 'e0000000000000000000000000000000',
        'createTime': 0,
        'exclusiveEndKey':
        'e7000000000000000000000000000000'
```

`},`

```json
        'shardID': 166,
        'status': 'readonly',
        'inclusiveBeginKey': 'e7000000000000000000000000000000',
        'createTime': 1453953073,
        'exclusiveEndKey': 'ffffffffffffffffffffffffffffffff'
```

`]` Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 404 | LogStoreNotExist | logstore {logstoreName} does not exist |
| 400 | ParameterInvalid | invalid shard id |
| 400 | ParameterInvalid | can not merge the last shard |
| 500 | InternalServerError | Specified Server Error Message |
| 400 | LogStoreWithoutShard | logstore has no shard |

> Not e The {Name} variable in the preceding error message is replaced with a specific Logstore name.

Examples Sample requests

```json
POST /logstores/logstorename/shards/30? action=merge Header :
    "Content-Length": 0,
    "x-log-signaturemethod": "hmac-sha1",
    "x-log-bodyrawsize": 0,
    "User-Agent": "log-python-sdk-v-0.6.0",
    "Host": "ali-test-project.cn-hangzhou.sls.aliyuncs.com",
    "Date": "Thu, 12 Nov 2015 03:40:31 GMT",
    "x-log-apiversion": "0.6.0",
    "Authorization": "LOG <yourAccessKeyId>:<yourSignature>"
```

Sample responses

```json
Header:
    "content-length": "57",
    "server": "nginx/1.6.1",
    "connection": "close",
    "date": "Thu, 12 Nov 2015 03:40:31 GMT",
    "content-type": "application/json",
    "x-log-requestid": "56440A2F99248C050600C74C"
Body :
```

`[`

```json
        'shardID': 167,
        'status': 'readwrite',
        'inclusiveBeginKey': 'e0000000000000000000000000000000',
        'createTime': 1453953105,
        'exclusiveEndKey': 'ffffffffffffffffffffffffffffffff'
```

`},`

```json
        'shardID': 30,
        'status': 'readonly',
        'inclusiveBeginKey': 'e0000000000000000000000000000000',
        'createTime': 0,
        'exclusiveEndKey':
        'e7000000000000000000000000000000'
```

`},`

```json
        'shardID': 166,
        'status': 'readonly',
        'inclusiveBeginKey': 'e7000000000000000000000000000000',
        'createTime': 1453953073,
        'exclusiveEndKey': 'ffffffffffffffffffffffffffffffff'
```

`]`

#### 1.7.9 GetCursor

Queries a cursor based on a point in time. You can use a cursor to obtain the location of a specific log. The following figure shows the relationships among a cursor, project, Logstore, and shard. Each project has multiple Logstores. Each Logstore has multiple shards. You can use a cursor to obtain the location of a specific log. Request syntax The request syntax of the GetCursor API operation is as follows:

```
GET /logstores/ay42/shards/2? type=cursor&from=1402341900 HTTP/1.1 Authorization: <AuthorizationString> Date: <GMT Date> Host: <Project Endpoint> x-log-apiversion: 0.6.0
```

Request elements Request headers The GetCursor API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| shard | String | Yes | The name of the shard. |
| type | String | Yes | This parameter must be set to cursor. |
| from | String | Yes | The time that is used to query a cursor. Set the value to a Unix timestamp or a string such as begin or end . |

You can use the from parameter to locate the logs within the lifecycle of a shard in a Logstore. If the lifecycle of the Logstore is `[begin_time, end_time)` and the from parameter is set to from_time, the response is returned as follows: from_time ≤ begin_time or from_time = "begin" : A cursor is returned. The cursor corresponds to the log whose timestamp is begin_time. from_time ≥ end_time or from_time = "end" : A cursor is returned. The cursor corresponds to the next log to be written at the current time (No data exists in the current cursor location). `from_time > begin_time and from_time < end_time` : A cursor is returned. The cursor corresponds to the first packet that Log Service receives later than or at from_time.

> Not e The lifecycle of a Logstore is specified by the ttl parameter of the Logstore. For example, the current time is 2018-11-11 09:00:00 and the ttl parameter is set to 5. The time interval of consumable data in each shard is `[2018-11-05 09:00:00, 2018-11-11 09:00:00)` .
> The server time is used.

Response elements Response headers The GetCursor API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters

```json
    "cursor": "MTQ0NzI5OTYwNjg5NjYzMjM1Ng=="
```

Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 404 | LogStoreNotExist | Logstore {Name} does not exist |
| 400 | ParameterInvalid | Parameter From is not valid |
| 400 | ShardNotExist | Shard {ShardID} does not exist |
| 500 | InternalServerError | Specified Server Error Message |
| 400 | LogStoreWithoutShard | the logstore has no shard |

Examples Sample requests

```json
GET /logstores/sls-test-logstore/shards/0? type=cursor&from=begin Header:
    "Content-Length": 0,
    "x-log-signaturemethod": "hmac-sha1",
    "x-log-bodyrawsize": 0,
    "User-Agent": "log-python-sdk-v-0.6.0",
    "Host": "ali-test-project.cn-hangzhou-devcommon-intranet.sls.aliyuncs.com",
    "Date": "Thu, 12 Nov 2015 03:56:57 GMT",
    "x-log-apiversion": "0.6.0",
    "Content-Type": "application/json",
    "Authorization": "LOG <yourAccessKeyId>:<yourSignature>"
```

Sample responses

```json
Header:
    "content-length": "41",
    "server": "nginx/1.6.1",
    "connection": "close",
    "date": "Thu, 12 Nov 2015 03:56:57 GMT",
    "content-type": "application/json",
    "x-log-requestid": "56440E0999248C070600C6AA"
Body:
    "cursor": "MTQ0NzI5OTYwNjg5NjYzMjM1Ng=="
```

#### 1.7.10 GetCursorTime

Queries the server time based on the cursor. Request syntax

```
GET /logstores/{logstoreName}/shards/{shard}? cursor={cursor}&type=cursor_time HTTP/1.1 Authorization: <AuthorizationString> Date: <GMT Date> Host: <Project Endpoint> x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1
```

Request elements Request headers The GetCursorTime API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| logstoreName | String | Yes | The name of the Logstore. |
| shard | Integer | Yes | The ID of the shard. |
| cursor | String | Yes | The cursor that is used to obtain the corresponding timestamp. |
| type | String | Yes | Set the value to cursor time. _ |

Response elements Response headers The GetCursorTime API does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters

```json
   "cursor_time": 1554260243
```

Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 404 | LogStoreNotExist | Logstore {Name} does not exist |
| 400 | ParameterInvalid | Parameter From is not valid |
| 400 | ShardNotExist | Shard {ShardID} does not exist |
| 500 | InternalServerError | Specified Server Error Message |
| 400 | LogStoreWithoutShard | the logstore has no shard |

Examples Sample requests

```
GET /logstores/internal-operation_log/shards/0? cursor=MTU0NzQ3MDY4MjM3NjUxMzQ0Ng%3D%3D&t ype=cursor_time HTTP/1.1 Authorization: LOG <yourAccessKeyId>:<yourSignature> x-log-bodyrawsize: 0 User-Agent: sls-java-sdk-v-0.6.1 x-log-apiversion: 0.6.0 Host: my-project.cn-hangzhou.sls.aliyuncs.com x-log-signaturemethod: hmac-sha1 Date: Wed, 03 Apr 2019 02:57:23 GMT Content-Type: application/x-protobuf Connection: Keep-Alive
```

Sample responses

```json
HTTP/1.1 200 Server: nginx Content-Type: application/json Content-Length: 26 Connection: close Access-Control-Allow-Origin: * Date: Wed, 03 Apr 2019 02:57:23 GMT x-log-requestid: 5CA42113D2F00378A74B9051
  "cursor_time": 1554260243
```

#### 1.7.11 PullLogs

Pulls logs from a Logstore. You must specify a shard when you call this API operation. Only Protocol Buffer log data can be pulled from a Logstore. For more information, see Protocol Buffer format. In scenarios that involve the Storm architecture, election and collaborative consumption can be performed through LoghubClientLib. Request syntax

```
GET /logstores/ay42/shards/0? type=logs&cursor=MTQ0NzMyOTQwMTEwMjEzMDkwNA==&count=100 HTTP/
```

### 1.1 Overview

```
Accept: application/x-protobuf Accept-Encoding: lz4 Authorization: <AuthorizationString> Date: <GMT Date> Host: <Project Endpoint> x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1
```

Request parameters Request header fields Accept: application/x-protobuf Accept-Encoding: lz4, deflate, or “” For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| type | String | Yes | Set the value to logs. |
| cursor | String | Yes | The cursor that identifies where data reading starts. This indicates the start point. |
| count | Integer | Yes | The number of returned log groups. Valid values: 1 to 1000. |

Response parameters Response header fields x-log-cursor: The next cursor of the currently read data. x-log-count: The number of currently returned logs. For information about common response headers of Log Service API operations, see Common response headers. Response elements Serialized data is returned in the Protocol Buffer format. The data may be compressed. Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 404 | LogStoreNotExist | Logstore {Name} does not exist |
| 400 | ParameterInvalid | Parameter Cursor is not valid |
| 400 | ParameterInvalid | ParameterCount should be in [0- 1000] |
| 400 | ShardNotExist | Shard {ShardID} does not exist |
| 400 | InvalidCursor | this cursor is invalid |
| 500 | InternalServerError | Specified Server Error Message |

Examples Sample requests

```json
Read data from shard 0. GET /logstores/sls-test-logstore/shards/0? cursor=MTQ0NzMyOTQwMTEwMjEzMDkwNA==&count=1000 &type=log Header:
    "Authorization"="LOG <yourAccessKeyId>:<yourSignature>",
    "x-log-bodyrawsize"=0,
    "User-Agent" : "sls-java-sdk-v-0.6.0",
    "x-log-apiversion" : "0.6.0",
    "Host" : "ali-test-project.cn-hangzhou-failover-intranet.sls.aliyuncs.com",
    "x-log-signaturemethod" : "hmac-sha1",
    "Accept-Encoding" : "lz4",
    "Content-Length": 0,
    "Date" : "Thu, 12 Nov 2015 12:03:17 GMT",
    "Content-Type" : "application/x-protobuf",
    "accept" : "application/x-protobuf"
```

Sample responses

```json
Header:
    "x-log-count" : "1000",
    "x-log-requestid" : "56447FB20351626D7C000874",
    "Server" : "nginx/1.6.1",
    "x-log-bodyrawsize" : "34121",
    "Connection" : "close",
    "Content-Length" : "4231",
    "x-log-cursor" : "MTQ0NzMyOTQwMTEwMjEzMDkwNA==",
    "Date" : "Thu, 12 Nov 2015 12:01:54 GMT",
    "x-log-compresstype" : "lz4",
    "Content-Type" : "application/x-protobuf"
Body: The <log group list in the Protocol Buffer format> after the compression.
```

Page flip To flip the page (get the next token) without returning data, you can send HTTP HEAD requests.

#### 1.7.12 PostLog

Writes log data to a Logstore. Only Protocol Buffer log data can be written to a Logstore. For more information, see Protocol Buffer format.

> Not e Log data is written in the form of log groups.

Log data can be written to a Logstore in either of the following modes: LoadBalance: In this mode, Log Service automatically writes logs to all writable shards in a Logstore. This mode provides high availability (SLA: 99.95%) in data writes. It applies to scenarios where data writes and reads are irrelevant to shards, for example, where ordering is not considered. KeyHash: The key field is added to the URL parameter. This determines which shard to store the log data. This field is optional. If you do not specify this field, Log Service automatically writes log data in the LoadBalance mode. For example, Log Service can hash an instance as a producer to a fixed shard based on the name of the instance. This ensures that data is written and consumed by using a strict order in the shard. The key is included only in the MD5 value range of a shard at a time even when the shard is merged or split. For more information, see Shards. Protocol Buffer log data The following table describes the fields of Protocol Buffer log data. For more information, see Data model and Data encoding. Log

| Field | Type | Required | Description |
|---|---|---|---|
| Time | Integer | Yes | The time when the log was generated. |
| Contents | List | Yes, this field must contain at least one element. | The list of log fields. For information about the field elements, see the Content field table. |

Content

| Field | Type | Required | Description |
|---|---|---|---|
| Key | String | Yes | The name of the custom key. |
| Value | String | Yes | The value of the custom key. |

LogTag

| Field | Type | Required | Description |
|---|---|---|---|
| Key | String | Yes | The name of the custom key. |
| Value | String | Yes | The value of the custom key. |

LogGroup

| Field | Type | Required | Description |
|---|---|---|---|
| Logs | List | Yes | A list of logs. For information about the field elements, see the Log field table. |

| Field | Type | Required | Description |
|---|---|---|---|
| Topic | String | Yes | A user-defined field in a log. This field identifies a group of logs. |
| Source | String | Yes | The source of the log, for example, the IP address of the machine where the log is generated. |
| LogTags | List | Yes | The list of log tags. For information about the field elements, see the LogTags field table. |

Request syntax LoadBalance mode

```
POST /logstores/<logstorename>/shards/lb HTTP/1.1 Authorization: <AuthorizationString> Content-Type: application/x-protobuf Content-Length: <Content Length> Content-MD5: <Content MD5> Date: <GMT Date> Host: <Project Endpoint> x-log-apiversion: 0.6.0 x-log-bodyrawsize: <BodyRawSize> x-log-compresstype: lz4 x-log-signaturemethod: hmac-sha1 <Compressed log data in the Protocol Buffer format>
```

KeyHash mode

```
POST /logstores/<logstorename>/shards/route? key=14d2f850ad6ea48e46e4547edbbb27e0 Authorization: <AuthorizationString> Content-Type: application/x-protobuf Content-Length: <Content Length> Content-MD5: <Content MD5> Date: <GMT Date> Host: <Project Endpoint> x-log-apiversion: 0.6.0 x-log-bodyrawsize: <BodyRawSize> x-log-compresstype: lz4 x-log-signaturemethod: hmac-sha1 <Compressed log data in the Protocol Buffer format>
```

Request elements Request headers For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| logstorename | String | Yes | The name of the Logstore to which logs are written. |

Response elements Response headers The PutLogs API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters No response element is returned after the request succeeds. Additional considerations You can call the PutLogs API operation to write a maximum of 3 MB log group data or 4,096 logs each time. The size of values in each log cannot be greater than 1 MB. If these limits are exceeded, the request will fail and no log data will be written. Log Service checks the format of log data written by the PutLogs API operation. If a log does not meet the format requirements, the request will fail and no log data will be written. Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | PostBodyInvalid | Protobuffer content cannot be parsed. | The error message returned because the logs in the Protocol Buffer format cannot be parsed. |
| 400 | InvalidTimestamp | Invalid timestamps are in logs. | The error message returned because the logs contain invalid timestamps. |
| 400 | InvalidEncoding | Non-UTF8 characters are in logs. | The error message returned because the logs contain non-UTF-8 characters. |
| 400 | InvalidKey | Invalid keys are in logs. | The error message returned because the logs contain invalid keys. |

| Developer Guide·API Refere | nce |   | Log Servic |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | PostBodyTooLarge | Logs must be less than or equal to 3 MB and 4096 entries. | The error message returned because the size of logs is greater than 3 MB or the number of logs exceeds 4,096. |
| 400 | PostBodyUncompressErr or | Failed to decompress logs. | The error message returned because the logs fail to be decompressed. |
| 499 | PostBodyInvalid | The post data time is out of range | The error message returned because the log timestamp is not within the valid range: [-7 × 24 hours, + 15 minutes]. |
| 404 | LogStoreNotExist | logstore {Name} does not exist. | The error message returned because the specified Logstore does not exist. |

> Not e The {Name} variable in the preceding error message is replaced with a specific Logstore name.

Examples Sample requests

```json
POST /logstores/sls-test-logstore
    "Content-Length": 118,
    "Content-Type":"application/x-protobuf",
    "x-log-bodyrawsize":1356,
    "Host": "ali-test-project.cn-hangzhou-devcommon-intranet.sls.aliyuncs.com",
    "Content-MD5":"6554BD042149C844761C2C094A8FECCE",
    "Date":"Thu, 12 Nov 2015 06:54:26 GMT",
    "x-log-apiversion": "0.6.0",
    "x-log-compresstype":"lz4"
    "x-log-signaturemethod": "hmac-sha1",
    "Authorization":"LOG <yourAccessKeyId>:<yourSignature>"
<Binary data obtained after logs in the Protocol Buffer format are compressed with the LZ 4 algorithm>
```

Sample responses

```json
Header
    "date": "Thu, 12 Nov 2015 06:53:03 GMT",
    "connection": "close",
    "x-log-requestid": "5644160399248C060600D216",
    "content-length": "0",
    "server": "nginx/1.6.1"
```

#### 1.7.13 GetLogs

Queries logs in a Logstore of a specified project, or queries the logs that meet the specified conditions. After a log is written to a Logstore, you can call the GetHistograms and GetLogs API operations to query the log. However, the query has a latency, which varies with the type of the log. Based on the log timestamp, Log Service classifies logs into the following two types: Real-time data: For this type, the difference between the time in a log and the current time on the server is (-180 seconds, 900 seconds]. For example, if the log time is UTC 2014-09-25 12:03:00 and the server receives the log at UTC 2014-09-25 12:05:00, the log is regarded as real-time data. Historical data: For this type, the difference between the time in a log and the current time on the server is [-7 × 86,400 seconds, -180 seconds). For example, if the log time is UTC 2014-09-25 12:00:00 and the server receives the log at UTC 2014-09-25 12:05:00, the log is regarded as historical data. Real-time data can be queried with a maximum latency of three seconds after being written to a Logstore. In most cases, 99.9% of real-time data can be queried in one second. Request syntax The request syntax of the GetLogs API operation is as follows:

```
GET /logstores/<logstorename>? type=log&topic=<logtopic>&from=<starttime>&to=<endtime>&quer y=<querystring>&line=<linenum>&offset=<startindex>&reverse=<ture|false> HTTP/1.1 Authorization: <AuthorizationString> Date: <GMT Date> Host: <Project Endpoint> x-log-bodyrawsize: 0 x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1
```

Request elements Request headers The GetLogs API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| logstorename | String | Yes | The name of the Logstore whose logs you want to query. |

| veloper Guide·API Ref | erence |   | Log Servic |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| type | String | Yes | The type of data in the Logstore. The value of this parameter must be log. |
| from | Integer | Yes | The start time of the time range during which the logs to be queried are generated. This parameter indicates the number of seconds that have elapsed since the Unix epoch 00:00:00 UTC on January 1, 1970. |
| to | Integer | Yes | The end time of the time range during which the logs to be queried are generated. This parameter indicates the number of seconds that have elapsed since the Unix epoch 00:00:00 UTC on January 1, 1970. |
| topic | String | No | The topic of the logs to be queried. |
| query | String | No | The query statement. see User Guide. The path is Query and analysis > Query synt ax and f unct ions > Query synt ax. |
| line | Integer | No | The maximum number of logs to return for the request. Value range: 0 to 100. Default value: 100. |
| offset | Integer | No | The start point of the returned log for the request. Valid values: 0 and positive integers. Default value: 0. |
| reverse | Boolean | No | Specifies whether to return logs in reverse order based on the log timestamp, accurate to seconds. If the value is true, logs are returned in reverse order. If the value is false, logs are returned in regular order. Default value: false. |

Response elements Response headers The GetLogs API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. The response header contains a special element that indicates whether the returned results of the request are complete. The following table describes the response parameters.

| Parameter | Type | Description |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| x-log-progress | String | The status of the query results. Valid values: Incomplete and Complete. |
| x-log-count | Integer | The total number of logs in the current query results. |

Response parameters After a GetLogs request succeeds, the response body contains log data hits in the query. If a large number of logs (measured in TBs) are queried, the response of the GetLogs operation may be incomplete. The response body of the GetLogs operation is an array. Each element in the array is a log. The following table describes the elements in the array.

| Element | Type | Description |
|---|---|---|
| time __ __ | Integer | The log timestamp. This parameter indicates the number of seconds that have elapsed since the Unix epoch 00:00:00 UTC on January 1, 1970. |
| Source __ __ | String | The log source, which is specified when logs are written. |
| [content] | Key-value pair | The original content of logs. |

Additional considerations The time range defined by the from and to request parameters is left closed and right open. This means that the time range includes the start time, but does not include the end time. If the from and to parameters for a time range have the same value, the time range is invalid and the function will return an error. If the number of logs in the Logstore significantly changes, Log Service cannot predict how many times this API operation needs to be called to obtain the complete results. In this case, you must check the value of the x-log-progress parameter in the returned results of each request. Based on the value, you can decide whether to repeatedly call this API operation to obtain the complete results.

> Not e The same number of query compute units (CUs) is consumed each time you call this API operation.

Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | LogStoreNotExist | logstore {Name} does not exist | The error message returned because the specified Logstore does not exist. |

| Developer Guide·API Refere | nce |   | Log Servic |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidTimeRange | request time range is invalid | The error message returned because the specified time interval of the request is invalid. |
| 400 | InvalidQueryString | query string is invalid | The error message returned because the specified query string of the request is invalid. |
| 400 | InvalidOffset | offset is invalid | The error message returned because the specified offset parameter of the request is invalid. |
| 400 | InvalidLine | line is invalid | The error message returned because the specified line parameter of the request is invalid. |
| 400 | InvalidReverse | Reverse value is invalid | The error message returned because the specified reverse parameter is invalid. |
| 400 | IndexConfigNotExist | logstore without index config | The error message returned because the index feature has not been enabled for the Logstore. |

> Not e The {name} variable in the preceding error message is replaced with a specific Logstore name.

Example In this example, the logs with the groupA topic are queried in a Logstore named app_log. The Logstore belongs to a project named big-game in the China (Hangzhou) region. The time range is from 2014-09- 01 00:00:00 to 2014-09-01 22:00:00 and the keyword is "error". The query starts from the beginning of the time range. A maximum of 20 logs can be returned. Sample requests

```
GET /logstores/app_log？ type=log&topic=groupA&from=1409529600&to=1409608800&query=error& line=20&offset=0 HTTP/1.1 Authorization: <AuthorizationString> Date: Wed, 3 Sept. 2014 08:33:46 GMT Host: big-game.cn-hangzhou.log.aliyuncs.com x-log-bodyrawsize: 0 x-log-apiversion: 0.4.0 x-log-signaturemethod: hmac-sha1
```

Sample responses

```json
HTTP/1.1 200 OK Content-MD5: 36F9F7F0339BEAF571581AF1B0AAAFB5 Content-Type: application/json Content-Length: 269 Date: Wed, 3 Sept. 2014 08:33:47 GMT x-log-requestid: efag01234-12341-15432f x-log-progress : Complete x-log-count : 10000 x-log-processed-rows: 10000 x-log-elapsed-millisecond:5
    "progress": "Complete",
    "count": 2,
    "logs": [
            "__time__": 1409529660,
            "__source__": "10.237.0.17",
            "Key1": "error",
            "Key2": "Value2"
```

`},`

```json
            "__time__": 1409529680,
            "__source__": "10.237.0.18",
            "Key3": "error",
            "Key4": "Value4"
```

`]` In the sample response, the x-log-progress value is Complete. This indicates that the log query is completed and the returned results are complete. Two logs meet the specified query conditions and are displayed as the value of the logs parameter. If the x-log-progress value is Incomplete, you must repeat the request to obtain the complete results.

#### 1.7.14 GetHistograms

Queries the distribution of logs in a Logstore within a specified project, or queries the distribution of logs that meet the specified conditions. After a log is written to a Logstore, you can call the GetHistograms and GetLogs API operations to query the log. However, the query has a latency, which varies with the type of the log. Based on the log timestamp, Log Service classifies logs into the following two types: Real-time data: For this type, the difference between the time in a log and the current time on the server is within the interval (-180 seconds, 900 seconds]. For example, if the log time is UTC 2014-09- 25 12:03:00 and the server receives the log at UTC 2014-09-25 12:05:00, the log is regarded as realtime data. The latency for real-time data is three seconds, from the time when the data is written to the Logstore to the time when the data can be queried. Historical data: For this type, the difference between the time in a log and the current time on the server is [-7 × 86,400 seconds, -180 seconds). For example, if the log time is UTC 2014-09-25 12:00:00 and the server receives the log at UTC 2014-09-25 12:05:00, the log is regarded as historical data. Request syntax The request syntax of the GetHistograms API operation is as follows:

```
GET /logstores/<logstorename>? type=histogram&topic=<logtopic>&from=<starttime>&to=<endtime >&query=<querystring> HTTP/1.1 Authorization: <AuthorizationString> Date: <GMT Date> Host: <Project Endpoint> x-log-bodyrawsize: 0 x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1
```

Request elements Request headers The GetHistograms API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| logstorename | String | Yes | The name of the Logstore whose logs you want to query. |
| type | String | Yes | The type of data in the Logstore. The value of this parameter must be histogram. |
| from | Integer | Yes | The start time of the time range during which the logs to be queried are generated. This parameter indicates the number of seconds that have elapsed since the Unix epoch 00:00:00 UTC on January 1, 1970. |
| to | Integer | Yes | The end time of the time range during which the logs to be queried are generated. This parameter indicates the number of seconds that have elapsed since the Unix epoch 00:00:00 UTC on January 1, 1970. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| topic | String | No | The topic of the logs to be queried. |
| query | String | No | The query statement. For more information about the query syntax, see User Guide. The path is Query and analysis > Query synt ax and f unct ions > Query synt ax. |

Response elements Response headers The GetHistograms API does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters After a GetHistograms request succeeds, the response body contains the distribution of the log hits returned by the query along the timeline. The response results evenly divide the time range into several subintervals and returns the number of log hits for each subinterval. The following table describes the response parameters.

| Parameter | Type | Description |
|---|---|---|
| progress | String | The status of the query results. Valid values: Incomplete and Complete. |
| count | Integer | The total number of logs in the current query results. |
| histograms | Array | The distribution of the current query results in the subintervals. For information about the parameters of each element in the histograms array, see the following table. |

This table describes the elements in the histograms parameter.

| Element | Type | Description |
|---|---|---|
| from | Integer | The start time of the subinterval. This parameter indicates the number of seconds that have elapsed since the Unix epoch 00:00:00 UTC on January 1, 1970. |
| to | Integer | The end time of the subinterval. This parameter indicates the number of seconds that have elapsed since the Unix epoch 00:00:00 UTC on January 1, 1970. |
| count | Integer | The number of logs that meet the query conditions for this subinterval in the current query results. |

| veloper Guide·API Referenc | e | Log Servic |
|---|---|---|

| Element | Type | Description |
|---|---|---|
| progress | String | Indicates whether the current query results in the subinterval are complete. Valid values: Incomplete and Complete. |

Additional considerations The preceding time ranges or subintervals are left closed and right open. This means that each time range or subinterval includes the start time, but does not include the end time. If the from and to parameters for a time range have the same value, the time range is invalid and the function will return an error. The time range is consistently divided into subintervals in the response. If the time range is unchanged, the subintervals divided in the response is also unchanged. If the number of logs in the Logstore significantly changes, Log Service cannot predict how many times this API operation needs to be called to obtain the complete results. In this case, you must check the value of the progress parameter in the returned results of each request. Based on the value, you can decide whether to repeatedly call this API operation to obtain the complete results.

> Not e The same number of query compute units (CUs) is consumed each time you call this API operation.

Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | LogStoreNotExist | logstore {Name} does not exist | The error message returned because the specified Logstore does not exist. |
| 400 | InvalidTimeRange | request time range is invalid | The error message returned because the specified time interval of the request is invalid. |
| 400 | InvalidQueryString | query string is invalid | The message returned when the query string of the request is invalid. |

> Not e The {name} variable in the preceding error message is replaced with a specific Logstore name.

Example In this example, the distribution of logs with the groupA topic is queried in a Logstore named app_log. The Logstore belongs to a project named big-game in the China (Hangzhou) region. The time range is from 2014-09-01 00:00:00 to 2014-09-01 22:00:00 and the keyword is "error". Sample requests

```
GET /logstores/app_log? type=histogram&topic=groupA&from=1409529600&to=1409608800&query=e rror HTTP/1.1 Authorization: LOG <yourAccessKeyId>:<yourSignature> Date: Wed, 3 Sept. 2014 08:33:46 GMT Host: big-game.cn-hangzhou.log.aliyuncs.com x-log-bodyrawsize: 0 x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1
```

Sample responses

```
HTTP/1.1 200 OK Content-Type: application/json Content-MD5: E6AD9C21204868C2DE84EE3808AAA8C8 Content-Type: application/json Date: Wed, 3 Sept. 2014 08:33:47 GMT Content-Length: 232 x-log-requestid: efag01234-12341-15432f
```

`[`

```json
            "from": 1409529600,
            "to": 1409569200,
            "count": 2,
            "progress": "Complete"
```

`},`

```json
            "from": 1409569200,
            "to": 1409608800,
            "count": 1,
            "progress": "Incomplete"
```

`]` In this sample response, the server divides the entire histogram into two equal time ranges: [2014-09-01 00:00:00, 2014-09-01 11:00:00) and [2014-09-01 11:00:00, 2014-09-01 22:00:00). The first query returns incomplete data because the amount of data exceeds the limit. The sample response indicates three hits. The results for the time range [2014-09-01 00:00:00 2014-09-01 11:00:00) are complete, including two hits. The results for the other time range are incomplete, including one hit. To obtain the complete results, you must repeatedly call the preceding sample request until the progress value in the response changes to Complete. The sample response is as follows:

```
HTTP/1.1 200 OK Content-Type: application/json Content-MD5: E6AD9C21204868C2DE84EE3808AAA8C8 Content-Type: application/json Date: Wed, 3 Sept. 2014 08:33:48 GMT Content-Length: 232 x-log-requestid: afag01322-1e241-25432e
```

`[`

```json
            "from": 1409529600,
            "to": 1409569200,
            "count": 2,
            "progress": "Complete"
```

`},`

```json
            "from": 1409569200,
            "to": 1409608800,
            "count": 2,
            "progress": "complete"
```

`]`

#### 1.7.15 UpdateIndex

Updates the indexes of a Logstore. Request syntax

```json
PUT /logstores/<logstoreName>/index HTTP/1.1 Authorization: <AuthorizationString> x-log-bodyrawsize: 0 User-Agent: <UserAgent> x-log-apiversion: 0.6.0 Host: <Project Endpoint> x-log-signaturemethod: hmac-sha1 Date: <GMT Date> Content-Type: application/json Content-MD5: <Content-MD5> Content-Length: <ContentLength>
  "line": <full text index>,
  "keys": <key-value index>,
  "ttl": <ttl>
```

Request elements Request headers The UpdateIndex API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| logstoreName | String | Yes | The name of the Logstore. |
| TTL | Integer | No | The time to live (TTL) of the indexes. Valid values: 7, 30, and 90. Default value: 0. |
| keys | Object | No | The key-value index, where the key refers to the field name and the value refers to the field value. |
| line | Object | No | The full-text index. |

You must specify the keys parameter or the line parameter, or both. The following table describes the full-text index attributes.

| Attribute | Type | Required | Description |
|---|---|---|---|
| token | Array | Yes | The list of delimiters. |
| caseSensitive | Boolean | No | Specifies whether the fields are case- sensitive. |
| chn | Boolean | No | Specifies whether the fields contain Chinese characters. |
| include keys _ | Array | No | The list of included fields. This parameter and the exclude keys _ parameter cannot be specified at the same time. |
| exclude keys _ | Array | No | The list of the excluded fields. This parameter and the include keys parameter _ cannot be specified at the same time. |

The following table describes the key-value index attributes.

| Attribute | Type | Required | Description |
|---|---|---|---|
| type | String | Yes | The type of the fields. |

| veloper Guide·API Referenc | e |   | Log Servic |
|---|---|---|---|

| Attribute | Type | Required | Description |
|---|---|---|---|
| alias | String | No | The alias of the field. |
| chn | Boolean | No | Specifies whether the fields contain Chinese characters. This parameter takes effect only when the type parameter is set to text. |
| token | Array | Required only when the type parameter is set to text | The list of delimiters. This parameter takes effect only when the type parameter is set to text. |
| caseSensitive | Boolean | No | Specifies whether the fields are case- sensitive. This parameter takes effect only when the type parameter is set to text. |
| doc value _ | Boolean | No | Specifies whether to enable analytics for the field. |

Response elements Response headers The UpdateIndex API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters The HTTP status code 200 is returned. Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 400 | ParameterInvalid | log store index is not created |
| 400 | ParameterInvalid | key config must has type |
| 400 | IndexInfoInvalid | required field token is lacking or of error format |
| 400 | IndexInfoInvalid | required fields line/keys are lacking or of error format |

| og Service |   | Developer Guide·API Referenc |
|---|---|---|

| HTTP status code | Error code | Error message |
|---|---|---|
| 404 | ProjectNotExist | The Project does not exist : {Project} |
| 404 | LogStoreNotExist | logstore {logstoreName} does not exist |
| 500 | InternalServerError | Specified Server Error Message |

Examples Sample requests

```json
PUT /logstores/logstore-4/index HTTP/1.1 Header: Authorization: LOG <yourAccessKeyId>:<yourSignature> x-log-bodyrawsize: 0 User-Agent: sls-java-sdk-v-0.6.1 x-log-apiversion: 0.6.0 Host: my-project.cn-shanghai.log.aliyuncs.com x-log-signaturemethod: hmac-sha1 Date: Mon, 07 May 2018 09:47:20 GMT Content-Type: application/json Content-MD5: 1860B805A6AA5288B97B32CF3B519112 Content-Length: 316 Connection: Keep-Alive Body:
  "line": {
    "token": [
      ",",
      " ",
      "'",
      "\"",
      ";",
      "=",
      "(",
      ")",
      "[",
      "]",
      "{",
      "}",
      "?",
      "@",
      "&",
      "<",
      ">",
      "/",
      ":",
      "\n",
      "\t",
      "\r"
```

`]` `},`

```json
  "keys": {
    "agent": {
      "doc_value": true,
      "caseSensitive": true,
      "alias": "agent_alias",
      "type": "text",
      "token": [
        ",",
        " ",
        "'",
        "\"",
        ";",
        "=",
        "(",
        ")",
        "[",
        "]",
        "{",
        "}",
        "?",
        "@",
        "&",
        "<",
        ">",
        "/",
        ":",
        "\n",
        "\t",
        "\r"
```

`]` `},`

```json
  "ttl": 90
```

Sample responses

```
HTTP/1.1 200 Server: nginx/1.12.1 Content-Length: 0 Connection: close Access-Control-Allow-Origin: * Date: Mon, 07 May 2018 09:47:21 GMT x-log-requestid: 5AF020A98CBAA2EF52AB66C9
```

#### 1.7.16 CreateIndex

Creates indexes for a specified Logstore. Request syntax

```json
POST /logstores/<logstoreName>/index HTTP/1.1 Authorization: <AuthorizationString> x-log-bodyrawsize: <x-log-bodyrawsize> User-Agent: <User-Agent> x-log-apiversion: <APIVersion> Host: <Project Endpoint> x-log-signaturemethod: hmac-sha1 Date: <GMT Date> Content-Type: application/json Content-MD5: <Content-MD5> Content-Length: <Content-Length>
  "line": <full text index>,
  "keys": <key-value index>
```

Request elements Request headers The CreateIndex API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers.

| Parameter | Type | Required | Description |
|---|---|---|---|
| logstoreName | String | Yes | The name of the Logstore. |
| keys | Object | No | The key-value index, where the key refers to the field name and the value refers to the field value. |
| line | Object | No | The full-text index. |

You must specify the keys parameter or the line parameter, or both. The following table describes the full-text index attributes.

| Attribute | Type | Required | Description |
|---|---|---|---|
| caseSensitive | Boolean | No | Specifies whether the fields are case- sensitive. |
| chn | Boolean | No | Specifies whether the fields contain Chinese characters. |
| token | Array | Yes | The list of delimiters. |

| Attribute | Type | Required | Description |
|---|---|---|---|
| include keys _ | Array | No | The list of included fields. This parameter and the exclude keys _ parameter cannot be specified at the same time. |
| exclude keys _ | Array | No | The list of excluded fields. This parameter and the include keys _ parameter cannot be specified at the same time. |

The following table describes the key-value index attributes.

| Attribute | Type | Required | Description |
|---|---|---|---|
| type | String | Yes | The type of the field. |
| alias | String | No | The alias of the field. |
| chn | Boolean | No | Specifies whether the fields contain Chinese characters. This parameter takes effect only when the type parameter is set to text. |
| token | Array | Required only when the type parameter is set to text | The list of delimiters. This parameter takes effect only when the type parameter is set to text. |
| caseSensitive | Boolean | No | Specifies whether the fields are case- sensitive. This parameter takes effect only when the type parameter is set to text. |
| doc value _ | Boolean | No | Specifies whether to enable analytics for the field. |

Response elements Response headers The CreateIndex API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters The HTTP status code 200 is returned. Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 400 | IndexInfoInvalid | required field token is lacking or of error format |
| 400 | IndexAlreadyExist | log store index is already created |
| 404 | ProjectNotExist | The Project does not exist : {Project} |
| 404 | LogStoreNotExist | logstore {logstoreName} does not exist |
| 500 | InternalServerError | Specified Server Error Message |

> Not e The {Project} and {logstoreName} variables in the preceding error messages are replaced with a specific project name and Logstore name.

Examples Sample requests

```json
POST /logstores/my-logstore/index HTTP/1.1 Authorization: LOG <yourAccessKeyId>:<yourSignature> x-log-bodyrawsize: 0 User-Agent: sls-java-sdk-v-0.6.1 x-log-apiversion: 0.6.0 Host: my-project.cn-shanghai.log.aliyuncs.com x-log-signaturemethod: hmac-sha1 Date: Mon, 07 May 2018 09:43:16 GMT Content-Type: application/json Content-MD5: 22876515FC311F857AD6C7902F6A0148 Content-Length: 316 Connection: Keep-Alive
  "line": {
    "token": [
      ",",
      " ",
      "'",
      "\"",
      ";",
      "=",
"("
```

`(``,`

```
      ")",
      "[",
      "]",
      "{",
      "}",
      "?",
      "@",
      "&",
      "<",
      ">",
      "/",
      ":",
      "\n",
      "\t",
      "\r"
```

`]` `},`

```json
  "keys": {
    "agent": {
      "doc_value": true,
      "caseSensitive": true,
      "alias": "agent_alias",
      "type": "text",
      "token": [
        ",",
        " ",
        "'",
        "\"",
        ";",
        "=",
        "(",
        ")",
        "[",
        "]",
        "{",
        "}",
        "?",
        "@",
        "&",
        "<",
        ">",
        "/",
        ":",
        "\n",
        "\t",
        "\r"
```

`]`

#### 1.7.17 DeleteIndex

Deletes the indexes of a Logstore. Request syntax

```
DELETE /logstores/<logstoreName>/index HTTP/1.1 Authorization: <AuthorizationString> x-log-bodyrawsize: 0 User-Agent: <UserAgent> x-log-apiversion: 0.6.0 Host: <Project Endpoint> x-log-signaturemethod: hmac-sha1 Date: <GMT Date> Content-Type: application/x-protobuf Connection: Keep-Alive
```

Request parameters Request headers The DeleteIndex API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| logstoreName | String | Yes | The name of the Logstore. |

Response elements Response headers The DeleteIndex API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters The HTTP status code 200 is returned. Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 400 | ParameterInvalid | log store index not created |
| 404 | ProjectNotExist | The Project does not exist : {Project} |
| 404 | LogStoreNotExist | logstore {logstoreName} does not exist |

| Developer Guide·API Reference |   | Log Servic |
|---|---|---|

| HTTP status code | Error code | Error message |
|---|---|---|
| 500 | InternalServerError | Specified Server Error Message |

Examples Sample requests

```
DELETE /logstores/my-logstore/index HTTP/1.1 Authorization: LOG <yourAccessKeyId>:<yourSignature> x-log-bodyrawsize: 0 User-Agent: sls-java-sdk-v-0.6.1 x-log-apiversion: 0.6.0 Host: my-project.cn-shanghai.log.aliyuncs.com x-log-signaturemethod: hmac-sha1 Date: Sun, 06 May 2018 13:22:57 GMT Content-Type: application/x-protobuf Connection: Keep-Alive
```

Sample responses

```
HTTP/1.1 200 Server: nginx/1.12.1 Content-Length: 0 Connection: close Access-Control-Allow-Origin: * Date: Sun, 06 May 2018 13:22:57 GMT x-log-requestid: 5AEF01B1A458E41C2F8326A8
```

#### 1.7.18 GetIndex

Queries the indexes of a Logstore. Request syntax The request syntax of the GetIndex API operation is as follows:

```
GET /logstores/<logstoreName>/index HTTP/1.1 Authorization: <AuthorizationString> x-log-bodyrawsize: 0 User-Agent: <UserAgent> x-log-apiversion: 0.6.0 Host: <Project Endpoint> x-log-signaturemethod: hmac-sha1 Date: <GMT Date> Content-Type: application/x-protobuf Connection: Keep-Alive
```

Request elements Request headers The GetIndex API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common response headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| logstoreName | String | Yes | The name of the Logstore. |

Response elements Response headers The GetIndex API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters When the GetIndex API operation succeeds, the response body contains the indexes of the specified project and Logstore. The following table describes the response body parameters.

| Parameter | Type | Description |
|---|---|---|
| index mode _ | String | The type of the indexes. |
| keys | Dictionary | The key-value index, where the key refers to the field name and the value refers to the field value. |
| line | object | The full-text index. |
| storage | String | The storage type. The default value is pg, which refers to PostgreSQL. |
| ttl | Integer | The time to live (TTL) of the index file. Valid values: 7, 30, and 90. Unit: days. |
| lastModifyTime | Integer | The time when the indexes were last modified. The value is a Unix timestamp. |

Full-text index attributes

| Parameter | Type | Description |
|---|---|---|
| caseSensitive | Boolean | Indicates whether the indexes are case sensitive. |
| chn | Boolean | Indicates whether the fields contain Chinese characters. |
| token | Array | The list of delimiters. |
| include keys _ | Array | The list of included fields. |
| exclude keys _ | Array | The list of excluded fields. |

Key-value index attributes

| Parameter | Type | Description |
|---|---|---|
| type | String | Indicates the type of the field. |
| alias | String | The alias of the field. |
| chn | Boolean | Indicates whether the fields contain Chinese characters. This parameter takes effect only when the type parameter is set to text. |
| token | Array | The list of delimiters. This parameter takes effect only when the type parameter is set to text. |
| caseSensitive | Boolean | Indicates whether the fields are case-sensitive. This parameter takes effect only when the type parameter is set to text. |
| doc value _ | Boolean | Indicates whether to enable analytics for the index. |

Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message | Description&nbsp; |
|---|---|---|---|
| 400 | IndexConfigNotExist | index config doesn’t exist | The error message returned because the specified index does not exist. |

| HTTP status code | Error code | Error message | Description&nbsp; |
|---|---|---|---|
| 404 | ProjectNotExist | The Project does not exist : {Project} | The error message returned because the specified project does not exist. |
| 404 | LogStoreNotExist | logstore {logstoreName} does not exist | The error message returned because the specified Logstore does not exist. |
| 500 | InternalServerError | Specified Server Error Message | The error message returned because an error occurs on the specified server. |

Examples Sample requests

```
GET /logstores/logstore-4/index HTTP/1.1 Authorization: LOG <yourAccessKeyId>:<yourSignature> x-log-bodyrawsize: 0 User-Agent: sls-java-sdk-v-0.6.1 x-log-apiversion: 0.6.0 Host: my-project.cn-shanghai.log.aliyuncs.com x-log-signaturemethod: hmac-sha1 Date: Sun, 06 May 2018 13:08:42 GMT Content-Type: application/x-protobuf Connection: Keep-Alive
```

Sample responses

```json
HTTP/1.1 200 Server: nginx/1.12.1 Content-Type: application/json Content-Length: 712 Connection: close Access-Control-Allow-Origin: * Date: Sun, 06 May 2018 13:08:42 GMT x-log-requestid: 5AEEFE5A8B8AEB5E6C82B395
  "index_mode": "v2",
  "keys": {
    "agent": {
      "alias": "",
      "caseSensitive": false,
      "chn": false,
      "doc_value": true,
      "token": [
        ",",
        " ",
        "'",
        "\"",
```

`,`

```
        ";",
        "=",
        "(",
        ")",
        "[",
        "]",
        "{",
        "}",
        "?",
        "@",
        "&",
        "<",
        ">",
        "/",
        ":",
        "\n",
        "\t",
        "\r"
```

`],`

```json
      "type": "text"
```

`},`

```json
    "bytes": {
      "alias": "",
      "doc_value": true,
      "type": "long"
```

`},`

```json
    "remote_ip": {
      "alias": "",
      "caseSensitive": false,
      "chn": false,
      "doc_value": true,
      "token": [
        ",",
        " ",
        "'",
        "\"",
        ";",
        "=",
        "(",
        ")",
        "[",
        "]",
        "{",
        "}",
        "?",
        "@",
        "&",
        "<",
        ">",
        "/",
        ":",
        "\n",
        "\t",
        "\r"
```

`],`

```json
      "type": "text"
```

`},`

```json
    "response": {
      "alias": "",
      "doc_value": true,
      "type": "long"
```

`},`

```json
  "line": {
    "caseSensitive": false,
    "chn": false,
    "token": [
      ",",
      " ",
      "'",
      "\"",
      ";",
      "=",
      "(",
      ")",
      "[",
      "]",
      "{",
      "}",
      "?",
      "@",
      "&",
      "<",
      ">",
      "/",
      ":",
      "\n",
      "\t",
      "\r"
```

`]` `},`

```json
  "storage": "pg",
  "ttl": 30,
  "lastModifyTime": 1524155379
```

#### 1.7.19 PutWebtracking

Merges multiple logs into one log during a single collection request. In the WebTracking mode, only one log can be written to each request. This API operation applies to scenarios where you need to collect a large amount of logs. Before you can call the PutWebtracking API operation, you must turn on the WebTracking switch for the corresponding Logstore. We recommend that you call this API operation to collect logs from web pages or clients. Request syntax

```json
POST {project}.{endpoint}/logstores/{logstoreName}/track HTTP/1.1 x-log-apiversion: 0.6.0 x-log-bodyrawsize: 1234 x-log-compresstype: gzip
  "__topic__": "topic",
  "__source__": "source",
  "__logs__": [
      "key1": "value1",
      "key2": "value2"
```

`},`

```json
      "key1": "value1",
      "key2": "value2"
```

`],`

```json
  "__tags__": {
    "tag1": "value1",
    "tag2": "value2"
```

Request elements Request headers Only the following three fields are required in the request header: x-log-apiversion: 0.6.0 x-log-bodyrawsize: 1234 x-log-compresstype: gzip The first two fields are required, and the third one is optional. For more information, see Common request headers. Request parameters URL parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| logstoreName | String | Yes | The name of the Logstore. |
| endpoint | String | Yes | The endpoint of Log Service. For more information, see Obtain an endpoint. |
| project | String | Yes | The name of the project. |

Request body parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| topic __ __ | String | No | The topic of the log. |
| source __ __ | String | No | The source of the log. |
| logs __ __ | list | Yes | The content of the log. Each element is a JSON object that indicates a log. Not e The time in a log collected by using the WebTracking feature is the time when the log arrives at Log Service. You do not need to specify the time field for __ __ each log. If this field is specified, it is overwritten by the time when the log arrives at Log Service. |
| tags __ __ | object | No | The tag of the log. |

Response elements Response headers The PutWebtracking API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters No response parameter is returned after the request succeeds. Examples Sample requests

```json
POST my-project.cn-hangzhou.log.aliyuncs.com/logstores/logstore-test/track HTTP/1.1 x-log-apiversion: 0.6.0 x-log-bodyrawsize: 1234 x-log-compresstype: gzip
  "__topic__": "topic",
  "__source__": "source",
  "__logs__": [
      "foo": "bar",
      "foo1": "bar1"
```

`},`

```json
      "bar": "foo",
      "bar1": "foo1"
```

`],`

```json
  "__tags__": {
    "tag1": "value1",
    "tag2": "value2"
```

Sample responses

```
HTTP/1.1 200 OK Header: Date=Wed, 20 May 2019 07:35:00 GMT, Content-Length=0, x-log-requestid=5642EFA499248C827B012B39, Connection=close, Server=nginx/1.6.1
```

### 1.8 Logtail machine group operations

#### 1.8.1 CreateMachineGroup

Creates a machine group to which the Logtail configuration is distributed and applied. Request syntax

```json
POST /machinegroups HTTP/1.1 Authorization: <AuthorizationString> Content-Type:application/json Content-Length:<Content Length> Content-MD5<:<Content MD5> Date: <GMT Date> Host: <Project Endpoint> x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1
    "groupName" : "testgroup",
    "groupType" : "",
    "groupAttribute" : {
        "externalName" : "testgroup",
        "groupTopic": "testgrouptopic"
```

`},`

```json
    "machineIdentifyType" : "ip",
    "machineList" : [
        "test-ip1",
        "test-ip2"
```

`]` Request elements Request headers The CreateMachineGroup API does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters Request body parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| groupName | String | Yes | The name of the machine group. The name must be unique in a project. |
| groupType | String | No | The type of the machine group. Default value: null. |
| machineIdentifyType | String | Yes | The type of the machine identifier. Valid values: ip and userdefined-id. |
| groupAttribute | object | Yes | The attribute of the machine group. Default value: null. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| machineList | Array | Yes | The specific machine identifier, which can be an IP address or user- defined identifier. |

The following table describes the attributes that are specified by the groupAttribute parameter.

| Attribute | Type | Required | Description |
|---|---|---|---|
| groupTopic | String | No | The topic of the machine group. Default value: null. |
| externalName | String | No | The external identifier on which the machine group depends. Default value: null. |

Response elements Response headers The CreateMachineGroup API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters The HTTP status code 200 is returned. Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 400 | MachineGroupAlreadyExist | group {GroupName} already exists |
| 400 | InvalidParameter | invalid group resource json |
| 500 | InternalServerError | Internal server error |

Examples Sample requests

```json
POST /machinegroups HTTP/1.1 Header :
    "x-log-apiversion": "0.6.0",
    "Authorization": "LOG <yourAccessKeyId>:<yourSignature>",
    "Host": "ali-test-project.cn-hangzhou-devcommon-intranet.sls.aliyuncs.com",
    "Date": "Tue, 10 Nov 2015 17:57:33 GMT",
    "Content-Length": "187",
    "x-log-signaturemethod": "hmac-sha1",
    "Content-MD5": "82033D507DEAAD72067BB58DFDCB590D",
    "User-Agent": "sls-java-sdk-v-0.6.0",
    "Content-Type": "application/json",
    "x-log-bodyrawsize": "0"
Body :
    "groupName": "test-machine-group",
    "groupType": "",
    "machineIdentifyType": "ip",
    "groupAttribute":     {
        "groupTopic": "testtopic",
        "externalName": "testgroup"
```

`},`

```json
    "machineList":     [
        "127.0.0.1",
        "127.0.0.2"
```

`]` Sample responses

```json
HTTP/1.1 200 OK Header :
    "Date": "Tue, 10 Nov 2015 17:57:33 GMT",
    "Content-Length": "0",
    "x-log-requestid": "5642300D99248CB76D005D36",
    "Connection": "close",
    "Server": "nginx/1.6.1"
```

#### 1.8.2 DeleteMachineGroup

Deletes a machine group. After you delete a machine group, the Logtail configuration applied to the machine group is also deleted. Request syntax

```
DELETE /machinegroups/{groupName} HTTP/1.1 Authorization: <AuthorizationString> Date: <GMT Date> Host: <Project Endpoint> x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1
```

Request elements Request headers The DeleteMachineGroup API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| groupName | String | Yes | The name of the machine group. |

Response elements Response headers The DeleteMachineGroup API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters The HTTP status code 200 is returned. Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 404 | GroupNotExist | group {GroupName} does not exist |
| 500 | InternalServerError | internal server error |

Examples Sample requests

```json
DELETE /machinegroups/test-machine-group-4 HTTP/1.1 Header :
    "x-log-apiversion": "0.6.0",
    "Authorization": "LOG <yourAccessKeyId>:<yourSignature>",
    "Host": "ali-test-project.cn-hangzhou-devcommon-intranet.sls.aliyuncs.com",
    "Date": "Tue, 10 Nov 2015 19:13:28 GMT",
    "Content-Length": "0",
    "x-log-signaturemethod": "hmac-sha1",
    "User-Agent": "sls-java-sdk-v-0.6.0",
    "Content-Type": "application/x-protobuf",
    "x-log-bodyrawsize": "0"
```

Sample responses

```json
HTTP/1.1 200 OK Header :
    "Date": "Tue, 10 Nov 2015 19:13:28 GMT",
    "Content-Length": "0",
    "x-log-requestid": "564241D899248C827B000CFE",
    "Connection": "close",
    "Server": "nginx/1.6.1"
```

#### 1.8.3 UpdateMachineGroup

Updates the information of a machine group. If the Logtail configurations are applied to a machine group, the configurations are automatically applied to or removed from a machine when the machine is added to or removed from the machine group. Request syntax

```json
PUT /machinegroups/{groupName} HTTP/1.1 Authorization: <AuthorizationString> Content-Type:application/json Content-Length:<Content Length> Content-MD5<:<Content MD5> Date: <GMT Date> Host: <Project Endpoint> x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1
    "groupName": "test-machine-group",
    "groupType" : "",
    "groupAttribute" : {
        "externalName" : "testgroup",
        "groupTopic": "testgrouptopic"
```

`},`

```json
    "machineIdentifyType" : "ip",
    "machineList" : [
        "test-ip1",
        "test-ip2"
```

`]` Request elements Request headers The UpdateMachineGroup API does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters URL parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| groupName | String | Yes | The name of the machine group. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| groupName | String | Yes | The name of the machine group. The name must be unique in a project. |
| groupType | String | No | The type of the machine group. Default value: null. |
| machineIdentifyType | String | Yes | The type of the machine identifier. Valid values: ip and userdefined-id. |
| groupAttribute | Object | Yes | The attribute of the machine group. Default value: null. |
| machineList | Array | Yes | The list of machine identifiers, which can be IP addresses or user-defined identifiers. |

The groupAttribute parameter consists of the following parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| groupTopic | String | No | The topic of the machine group. Default value: null. |
| externalName | String | No | The identifier of the external management system on which the machine group depends. Default value: null. |

Response elements Response headers The UpdateMachineGroup API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters The HTTP status code 200 is returned. Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 404 | GroupNotExist | group {GroupName} does not exist |
| 400 | InvalidParameter | invalid group resource json |
| 500 | InternalServerError | internal server error |

Examples Sample requests

```json
PUT /machinegroups/test-machine-group HTTP/1.1 Header :
    "x-log-apiversion": "0.6.0",
    "Authorization": "LOG <yourAccessKeyId>:<yourSignature>",
    "Host": "ali-test-project.cn-hangzhou-devcommon-intranet.sls.aliyuncs.com",
    "Date": "Tue, 10 Nov 2015 18:41:43 GMT",
    "Content-Length": "194",
    "x-log-signaturemethod": "hmac-sha1",
    "Content-MD5": "2CEBAEBE53C078891527CB70A855BAF4",
    "User-Agent": "sls-java-sdk-v-0.6.0",
    "Content-Type": "application/json",
    "x-log-bodyrawsize": "0"
Body :
    "groupName": "test-machine-group",
    "groupType": "",
    "machineIdentifyType": "userdefined",
    "groupAttribute":     {
        "groupTopic": "testtopic2",
        "externalName": "testgroup2"
```

`},`

```json
    "machineList":     [
        "uu_id_1",
        "uu_id_2"
```

`]` Sample responses

```json
HTTP/1.1 200 OK Header :
    "Date": "Tue, 10 Nov 2015 18:41:43 GMT",
    "Content-Length": "0",
    "x-log-requestid": "56423A6799248CA57B00035C",
    "Connection": "close",
    "Server": "nginx/1.6.1"
```

#### 1.8.4 ListMachineGroup

Lists machine groups. Request syntax

```
GET /machinegroups? offset=1&size=100 HTTP/1.1 Authorization: <AuthorizationString> Date: <GMT Date> Host: <Project Endpoint> x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1
```

Request elements Request headers The ListMachineGroup API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| offset | Integer | No | The start position of the records to return. Default value: 0. |
| size | Integer | No | The maximum number of entries to return on each page. Default and maximum value: 500. |
| groupName | String | No | The group machine name that is used as a filtering condition. Fuzzy match is supported. |

Response elements Response headers The ListMachineGroup API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters After the request succeeds, the response body contains a list of all machine groups in the specified project. The following table describes the response parameters.

| Parameter | Type | Description |
|---|---|---|
| count | Integer | The number of returned machine groups on each page. |
| total | Integer | The total number of returned machine groups. |
| machinegroups | JSON array | The list of returned machine groups. |

```json
    "machinegroups":     [
        "test-machine-group",
        "test-machine-group-2"
```

`],`

```json
    "count": 2,
    "total": 2
```

Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 500 | InternalServerError | internal server error |

Examples Sample requests

```json
GET /machinegroups? groupName=test-machine-group&offset=0&size=3 HTTP/1.1 Header :
    "x-log-apiversion": "0.6.0",
    "Authorization": "LOG <yourAccessKeyId>:<yourSignature>",
    "Host": "ali-test-project.cn-hangzhou-devcommon-intranet.sls.aliyuncs.com",
    "Date": "Tue, 10 Nov 2015 18:34:44 GMT",
    "Content-Length": "0",
    "x-log-signaturemethod": "hmac-sha1",
    "User-Agent": "sls-java-sdk-v-0.6.0",
    "Content-Type": "application/x-protobuf",
    "x-log-bodyrawsize": "0"
```

Sample responses

```json
HTTP/1.1 200 OK Header :
    "Date": "Tue, 10 Nov 2015 18:34:44 GMT",
    "Content-Length": "83",
    "x-log-requestid": "564238C499248C8F7B0001DE",
    "Connection": "close",
    "Content-Type": "application/json",
    "Server": "nginx/1.6.1"
Body :
    "machinegroups":     [
        "test-machine-group",
        "test-machine-group-2"
```

`],`

```json
    "count": 2,
    "total": 2
```

#### 1.8.5 GetMachineGroup

Queries the details of a machine group. Request syntax

```
GET /machinegroups/{groupName} HTTP/1.1 Authorization: <AuthorizationString> Date: <GMT Date> Host: <Project Endpoint> x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1
```

Request elements Request headers The GetMachineGroup API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| groupName | String | Yes | The name of the machine group. |

Response elements Response headers The GetMachineGroup API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters

| Parameter | Type | Description |
|---|---|---|
| groupName | String | The name of the machine group. The name must be unique in a project. |
| groupType | String | The type of the machine group. Valid values: null and Armory. Default value: null. |
| machineIdentifyType | String | The type of the machine identifier. Valid values: ip and userdefined-id. |
| groupAttribute | JSON object | The attribute of the machine group. Default value: null. |
| machineList | JSON array | The list of machine identifiers, which can be IP addresses or user-defined identifiers. |
| createTime | Integer | The time when the machine group was created. |
| lastModifyTime | Integer | The time when the machine group was last updated. |

The groupAttribute parameter consists of the following parameters.

| Name | Type | Required | Description |
|---|---|---|---|
| groupTopic | String | No | The topic of the machine group. |
| externalName | String | No | The identifier of the external management system (Armory) on which the machine group depends. |

```json
    "groupName": "test-machine-group",
    "groupType": "",
    "groupAttribute":     {
        "externalName": "testgroup",
        "groupTopic": "testtopic"
```

`},`

```json
    "machineIdentifyType": "ip",
    "machineList":     [
        "127.0.0.1",
        "127.0.0.2"
```

`],`

```json
    "createTime": 1447178253,
    "lastModifyTime": 1447178253
```

Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 404 | MachineGroupNotExist | group {GroupName} does not exist |
| 500 | InternalServerError | internal server error |

Examples Sample requests

```json
GET /machinegroups/test-machine-group HTTP/1.1 Header :
    "x-log-apiversion": "0.6.0",
    "Authorization": "LOG <yourAccessKeyId>:<yourSignature>",
    "Host": "ali-test-project.cn-hangzhou-devcommon-intranet.sls.aliyuncs.com",
    "Date": "Tue, 10 Nov 2015 18:15:24 GMT",
    "Content-Length": "0",
    "x-log-signaturemethod": "hmac-sha1",
    "User-Agent": "sls-java-sdk-v-0.6.0",
    "Content-Type": "application/x-protobuf",
    "x-log-bodyrawsize": "0"
```

Sample responses

```json
HTTP/1.1 200 OK Header :
    "Date": "Tue, 10 Nov 2015 18:15:23 GMT",
    "Content-Length": "239",
    "x-log-requestid": "5642343B99248CB36D0060B8",
    "Connection": "close",
    "Content-Type": "application/json",
    "Server": "nginx/1.6.1"
Body :
    "groupName": "test-machine-group",
    "groupType": "",
    "groupAttribute":     {
        "externalName": "testgroup",
        "groupTopic": "testtopic"
```

`},`

```json
    "machineIdentifyType": "ip",
    "machineList":     [
        "127.0.0.1",
        "127.0.0.2"
```

`],`

```json
    "createTime": 1447178253,
    "lastModifyTime": 1447178253
```

#### 1.8.6 ApplyConfigToMachineGroup

Applies a Logtail configuration to a machine group. Request syntax

```
GET /machinegroups/{groupName} HTTP/1.1 Authorization: <AuthorizationString> Date: <GMT Date> Host: <Project Endpoint> x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1
```

Request elements Request headers The ApplyConfigToMachineGroup API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| GroupName | String | Yes | The name of the machine group. |
| ConfigName | String | Yes | The name of the Logtail configuration. |

Response elements Response headers The ApplyConfigToMachineGroup API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters The HTTP status code 200 is returned. Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 404 | GroupNotExist | group {GroupName} does not exist |
| 404 | ConfigNotExist | config {ConfigName} does not exist |
| 500 | InternalServerError | internal server error |

Examples Sample requests

```json
PUT /machinegroups/sample-group/configs/logtail-config-sample Header :
    "Content-Length": 0,
    "x-log-signaturemethod": "hmac-sha1",
    "x-log-bodyrawsize": 0,
    "User-Agent": "log-python-sdk-v-0.6.0",
    "Host": "ali-test-project.cn-hangzhou-devcommon-intranet.sls.aliyuncs.com",
    "Date": "Mon, 09 Nov 2015 09:44:43 GMT",
    "x-log-apiversion": "0.6.0",
    "Authorization": "LOG <yourAccessKeyId>:<yourSignature>"
```

Sample responses

```json
    "date": "Mon, 09 Nov 2015 09:44:43 GMT",
    "connection": "close",
    "x-log-requestid": "56406B0B99248CAA230BA094",
    "content-length": "0",
    "server": "nginx/1.6.1"
```

#### 1.8.7 RemoveConfigFromMachineGroup

Deletes a Logtail configuration from a machine group. Request syntax

```
GET /machinegroups/{groupName} HTTP/1.1 Authorization: <AuthorizationString> Date: <GMT Date> Host: <Project Endpoint> x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1
```

Request elements Request headers The RemoveConfigFromMachineGroup API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| GroupName | String | Yes | The name of the machine group. |
| ConfigName | String | Yes | The name of the Logtail configuration. |

Response elements Response headers The RemoveConfigFromMachineGroup API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters The HTTP status code 200 is returned. Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 404 | GroupNotExist | group {GroupName} does not exist |
| 404 | ConfigNotExist | config {ConfigName} does not exist |
| 500 | InternalServerError | internal server error |

Examples Sample requests

```json
DELETE /machinegroups/sample-group/configs/logtail-config-sample
    "Content-Length": 0,
    "x-log-signaturemethod": "hmac-sha1",
    "x-log-bodyrawsize": 0,
    "User-Agent": "log-python-sdk-v-0.6.0",
    "Host": "ali-test-project.cn-hangzhou-devcommon-intranet.sls.aliyuncs.com",
    "Date": "Mon, 09 Nov 2015 09:48:48 GMT",
    "x-log-apiversion": "0.6.0",
    "Authorization": "LOG <yourAccessKeyId>:<yourSignature>"
```

Sample responses

```json
    "date": "Mon, 09 Nov 2015 09:48:48 GMT",
    "connection": "close",
    "x-log-requestid": "56406C0099248CAA230BE135",
    "content-length": "0",
    "server": "nginx/1.6.1"
```

#### 1.8.8 ListMachines

Lists your machines in a machine group that is connected with Log Service. Request syntax

```
GET /machinegroups/{groupName}/machines HTTP/1.1 Authorization: <AuthorizationString> Date: <GMT Date> Host: <Project Endpoint> x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1
```

Request elements Request headers The ListMachines API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| groupName | String | Yes | The name of the machine group. |
| offset | Integer | No | The start position of the returned records. Default value: 0. |
| size | Integer | No | The maximum number of entries to return on each page. Default and maximum value: 500. |

Response elements Response headers The ListMachines API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters

| Parameter | Type | Description |
|---|---|---|
| count | Integer | The number of returned machines on each page. |
| total | Integer | The total number of machines. |
| machines | JSON array | The list of returned machines. |

The machines parameter consists of the following attributes.

| Attribute | Type | Description |
|---|---|---|
| ip | String | The IP address of the machine. |
| machine-uniqueid | String | The universally unique identifier (UUID) of the machine. |
| userdefined-id | String | The user-defined identifier of the machine. |

Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 404 | GroupNotExist | group {GroupName} does not exist |
| 500 | InternalServerError | internal server error |

Additional considerations The API operation lists only the machines that are normally connected with Log Service. Examples Sample requests

```json
GET /machinegroups/test-machine-group-5/machines? offset=0&size=3 HTTP/1.1 Header :
    "x-log-apiversion": "0.6.0",
    "Authorization": "LOG <yourAccessKeyId>:<yourSignature>",
    "Host": "ali-test-project.cn-hangzhou-devcommon-intranet.sls.aliyuncs.com",
    "Date": "Tue, 10 Nov 2015 19:04:57 GMT",
    "Content-Length": "0",
    "x-log-signaturemethod": "hmac-sha1",
    "User-Agent": "sls-java-sdk-v-0.6.0",
    "Content-Type": "application/x-protobuf",
    "x-log-bodyrawsize": "0"
```

Sample responses

```json
HTTP/1.1 200 OK Header :
    "Date": "Tue, 10 Nov 2015 19:04:58 GMT",
    "Content-Length": "324",
    "x-log-requestid": "56423FD999248C827B000A57",
    "Connection": "close",
    "Content-Type": "application/json",
    "Server": "nginx/1.6.1"
Body :
    "machines":     [
            "ip": "10.101.166.116",
            "machine-uniqueid": "",
            "userdefined-id": "",
            "lastHeartbeatTime": 1447182247
```

`},`

```json
            "ip": "10.101.165.193",
            "machine-uniqueid": "",
            "userdefined-id": "",
            "lastHeartbeatTime": 1447182246
```

`},`

```json
            "ip": "10.101.166.91",
            "machine-uniqueid": "",
            "userdefined-id": "",
            "lastHeartbeatTime": 1447182248
```

`],`

```json
    "count": 3,
    "total": 8
```

#### 1.8.9 GetAppliedConfigs

Queries the Logtail configurations that are applied to a machine group. Request syntax

```
GET /machinegroups/{groupName}/configs HTTP/1.1 Authorization: <AuthorizationString> Date: <GMT Date> Host: <Project Endpoint> x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1
```

Request elements Request headers The GetAppliedConfigs API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| groupName | String | Yes | The name of the machine group. |

Response elements Response headers The GetAppliedConfigs API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters After a GetAppliedConfigs request succeeds, the response body contains a list of all machines in the specified machine group. The following table describes the response parameters.

| Parameter | Type | Description |
|---|---|---|
| count | Integer | The number of returned configurations on each page. |
| configs | String array | The list of returned configurations. |

Error codes In addition to the Common error codes of Log Service API operations, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 404 | GroupNotExist | group {GroupName} does not exist |
| 500 | InternalServerError | internal server error |

Examples Sample requests

```json
GET /machinegroups/test-machine-group/configs HTTP/1.1 Header :
    "x-log-apiversion": "0.6.0",
    "Authorization": "LOG <yourAccessKeyId>:<yourSignature>",
    "Host": "ali-test-project.cn-hangzhou-devcommon-intranet.sls.aliyuncs.com",
    "Date": "Tue, 10 Nov 2015 19:45:48 GMT",
    "Content-Length": "0",
    "x-log-signaturemethod": "hmac-sha1",
    "User-Agent": "sls-java-sdk-v-0.6.0",
    "Content-Type": "application/x-protobuf",
    "x-log-bodyrawsize": "0"
```

Sample responses

```json
HTTP/1.1 200 OK Header :
    "Date": "Tue, 10 Nov 2015 19:45:48 GMT",
    "Content-Length": "53",
    "x-log-requestid": "5642496C99248C8C7B00173F",
    "Connection": "close",
    "Content-Type": "application/json",
    "Server": "nginx/1.6.1"
Body :
    "configs":     [
        "two",
        "three",
        "test_logstore"
```

`],`

```json
    "count": 3
```

### 1.9 Logtail configuration operations

#### 1.9.1 CreateConfig

Creates a Logtail configuration. Request syntax

```json
POST /configs HTTP/1.1 Authorization: <AuthorizationString> Content-Type:application/json Content-Length:<Content Length> Content-MD5<:<Content MD5> Date: <GMT Date> Host: <Project Endpoint> x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1
    "configName": "testcategory1",
    "inputType": "file",
    "inputDetail": {
        "logType": "common_reg_log",
        "logPath": "/var/log/httpd/",
        "filePattern": "access*.log",
        "localStorage": true,
        "timeFormat": "%Y/%m/%d %H:%M:%S",
        "logBeginRegex": ".*",
        "regex": "(\w+)(\s+)",
        "key" :["key1", "key2"],
        "filterKey":["key1"],
        "filterRegex":["regex1"],
        "fileEncoding":"utf8",
        "topicFormat": "none"
```

`},`

```json
    "outputType": "LogService",
    "outputDetail":
        "logstoreName": "perfcounter"
```

Request elements Request headers The CreateConfig API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters For information about the request parameters and Logtail configuration examples, see Logtail configurations. Response elements Response headers The CreateConfig API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response elements The HTTP status code 200 is returned. Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 400 | ConfigAlreadyExist | config {Configname} already exists |
| 400 | InvalidParameter | invalid config resource json |
| 500 | InternalServerError | internal server error |

The configuration fails to be created if an error occurs, for example, the configuration already exists, the format is incorrect, the required parameters are missing, or the quota is exceeded. Examples Sample requests

```json
POST /configs HTTP/1.1 Header :
    'Content-Length': 737,
    'Host': 'ali-test-project.cn-hangzhou-devcommon-intranet.sls.aliyuncs.com',
    'x-log-bodyrawsize': 737,
    'Content-MD5': 'FBA01ECF7255BE143379BC70C56BBF68',
    'x-log-signaturemethod': 'hmac-sha1',
    'Date': 'Mon, 09 Nov 2015 07:45:30 GMT',
    'x-log-apiversion': '0.6.0',
    'User-Agent': 'log-python-sdk-v-0.6.0',
    'Content-Type': 'application/json',
    'Authorization': 'LOG <yourAccessKeyId>:<yourSignature>'
Body:
    "configName": "sample-logtail-config",
    "inputType": "file",
    "inputDetail": {
        "logType": "common_reg_log",
        "logPath": "/var/log/httpd/",
        "filePattern": "access*.log",
        "localStorage": true,
        "timeFormat": "%d/%b/%Y:%H:%M:%S",
        "logBeginRegex": "\\d+\\.\\d+\\.\\d+\\.\\d+ - .*",
        "regex": "([\\d\\.] +) \\S+ \\S+ \\[(\\S+) \\S+\\] \"(\\w+) ([^\"]*)\" ([\\d\\.]+
) (\\d+) (\\d+) (\\d+|-) \"([^\"]*)\" \"([^\"]*)\".*",
        "key": ["ip", "time", "method", "url", "request_time", "request_length", "status"
, "length", "ref_url", "browser"],
        "filterKey": [],
        "filterRegex": [],
        "topicFormat": "none",
        "fileEncoding": "utf8"
```

`},`

```json
    "outputType": "LogService",
    "outputDetail":
        "logstoreName": "sls-test-logstore"
```

Sample responses

```json
HTTP/1.1 200 OK Header
    'date': 'Mon, 09 Nov 2015 07:45:30 GMT',
    'connection': 'close',
    'x-log-requestid': '56404F1A99248CA26C002180',
    'content-length': '0',
    'server': 'nginx/1.6.1'
```

#### 1.9.2 ListConfig

Lists all configurations of a project. You can set the relevant parameters in the syntax to list the configurations on multiple pages. Request syntax

```
GET /configs? offset=0&size=100 HTTP/1.1 Authorization: <AuthorizationString> Date: <GMT Date> Host: <Project Endpoint> x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1
```

Request elements Request headers The ListConfig API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| offset | Integer | No | The start position of entries to return. Default value: 0. |
| size | Integer | No | The maximum number of entries to return on each page. Default value: 500. |

Response elements Response headers The ListConfig API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters The response body of the ListConfig API operation contains a list of all configurations in the project. The following table describes the response parameters.

| Parameter | Type | Description |
|---|---|---|
| count | Integer | The number of returned configurations on each page. |
| total | Integer | The total number of returned configurations. |

| Parameter | Type | Description |
|---|---|---|
| configs | String array | The list of returned configurations. |

Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 404 | ConfigNotExist | config {Configname} does not exist |
| 500 | InternalServerError | internal server error |

Examples Sample requests

```json
GET /configs? offset=0&size=10 HTTP/1.1 Header :
    "Content-Length": 0,
    "x-log-signaturemethod": "hmac-sha1",
    "x-log-bodyrawsize": 0,
    "User-Agent": "log-python-sdk-v-0.6.0",
    "Host": "ali-test-project.cn-hangzhou-devcommon-intranet.sls.aliyuncs.com",
    "Date": "Mon, 09 Nov 2015 09:19:13 GMT",
    "x-log-apiversion": "0.6.0",
    "Authorization": "LOG <yourAccessKeyId>:<yourSignature>"
```

Sample responses

```json
Header :
    "content-length": "103",
    "server": "nginx/1.6.1",
    "connection": "close",
    "date": "Mon, 09 Nov 2015 09:19:13 GMT",
    "content-type": "application/json",
    "x-log-requestid": "5640651199248CAA2300C2BA"
Body:
    "count": 3,
    "configs":
```

`[`

```
        "logtail-config-sample",
        "logtail-config-sample-2",
        "logtail-config-sample-3"
```

`],`

```json
    "total": 3
```

#### 1.9.3 GetAppliedMachineGroups

Lists the machines that apply a Logtail configuration. Request syntax

```
GET /configs/{configName}/machinegroups HTTP/1.1 Authorization: <AuthorizationString> Date: <GMT Date> Host: <Project Endpoint> x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1
```

Request elements Request headers The GetAppliedMachineGroups API operation does not have special request headers. For information about common request headers of Log Service API operations, see Logtail configurations. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| ConfigName | String | Yes | The name of the Logtail configuration. |

Response elements Response headers The GetAppliedMachineGroups API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters After the request succeeds, the response body contains a list of all machines in the specified machine group. The following table describes the response parameters.

| Parameter | Type | Description |
|---|---|---|
| count | Integer | The number of returned machine groups. |
| machinegroups | String array | The list of returned machine groups. |

Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 404 | GroupNotExist | group {GroupName} does not exist |
| 500 | InternalServerError | internal server error |

Examples Sample requests

```json
GET /configs/logtail-config-sample/machinegroups Header:
    "Content-Length": 0,
    "x-log-signaturemethod": "hmac-sha1",
    "x-log-bodyrawsize": 0,
    "User-Agent": "log-python-sdk-v-0.6.0",
    "Host": "ali-test-project.cn-hangzhou-devcommon-intranet.sls.aliyuncs.com",
    "Date": "Mon, 09 Nov 2015 09:51:38 GMT",
    "x-log-apiversion": "0.6.0",
    "Authorization": "LOG <yourAccessKeyId>:<yourSignature>"
```

Sample responses

```json
Header :
    "content-length": "44",
    "server": "nginx/1.6.1",
    "connection": "close",
    "date": "Mon, 09 Nov 2015 09:51:38 GMT",
    "content-type": "application/json",
    "x-log-requestid": "56406CAA99248CAA230BE828"
Body:
    "count": 1,
    "machinegroups":
```

`[`

```
        "sample-group"
```

`]`

#### 1.9.4 GetConfig

Queries the details of a Logtail configuration. Request syntax

```
GET /configs/<configName> HTTP/1.1 Authorization: <AuthorizationString> Date: <GMT Date> Host: <Project Endpoint> x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1
```

Request elements Request headers The GetConfig API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| ConfigName | String | Yes | The name of the Logtail configuration. |

Response elements Response headers The GetConfig API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common request headers. Response parameters For information about the response parameters and Logtail configuration examples, see Logtail configurations. Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 404 | ConfigNotExist | Config {Configname} does not exist |
| 500 | InternalServerError | Specified Server Error Message |

Examples Sample requests

```json
GET /configs/logtail-config-sample Header :
    "Content-Length": 0,
    "x-log-signaturemethod": "hmac-sha1",
    "x-log-bodyrawsize": 0,
    "User-Agent": "log-python-sdk-v-0.6.0",
    "Host": "ali-test-project.cn-hangzhou-devcommon-intranet.sls.aliyuncs.com",
    "Date": "Mon, 09 Nov 2015 08:29:15 GMT",
    "x-log-apiversion": "0.6.0",
    "Authorization": "LOG <yourAccessKeyId>:<yourSignature>"
```

Sample responses

```json
Header :
    "content-length": "730",
    "server": "nginx/1.6.1",
    "connection": "close",
    "date": "Mon, 09 Nov 2015 08:29:15 GMT",
    "content-type": "application/json",
    "x-log-requestid": "5640595B99248CAA23004A59"
Body :
    "configName": "logtail-config-sample",
    "outputDetail": {
        "endpoint": "http://cn-hangzhou-devcommon-intranet.sls.aliyuncs.com",
        "logstoreName": "sls-test-logstore"
```

`},`

```json
    "outputType": "LogService",
    "inputType": "file",
    "inputDetail": {
        "regex": "([\\d\\.] +) \\S+ \\S+ \\[(\\S+) \\S+\\] \"(\\w+) ([^\"]*)\" ([\\d\\.]+
) (\\d+) (\\d+) (\\d+|-) \"([^\"]*)\" \"([^\"]*)\".*",
        "filterKey": [],
        "logPath": "/var/log/httpd/",
        "logBeginRegex": "\\d+\\.\\d+\\.\\d+\\.\\d+ - .*",
        "logType": "common_reg_log",
        "topicFormat": "none",
        "localStorage": true,
        "key": [
            "ip",
            "time",
            "method",
            "url",
            "request_time",
            "request_length",
            "status",
            "length",
            "ref_url",
            "browser"
```

`],`

```json
        "filePattern": "access*.log",
        "timeFormat": "%d/%b/%Y:%H:%M:%S",
        "filterRegex": []
```

`},`

```json
    "createTime": 1447040456,
    "lastModifyTime": 1447050456
```

#### 1.9.5 DeleteConfig

Deletes a Logtail configuration. When you call this API operation, the Logtail configuration is deleted even if it is applied to the Machine Group. Request syntax

```
DELETE /configs/<configName> HTTP/1.1 Authorization: <AuthorizationString> Date: <GMT Date> Host: <Project Endpoint> x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1
```

Request elements Request headers The DeleteConfig API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| ConfigName | String | Yes | The name of the logtail configuration. |

Response elements Response headers The DeleteConfig API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters The HTTP status code 200 is returned. Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 404 | ConfigNotExist | config {Configname} does not exist |
| 400 | InvalidParameter | invalid config resource json |
| 500 | InternalServerError | internal server error |

Examples Sample requests

```json
DELETE /configs/logtail-config-sample Header :
    "Content-Length": 0,
    "x-log-signaturemethod": "hmac-sha1",
    "x-log-bodyrawsize": 0,
    "User-Agent": "log-python-sdk-v-0.6.0",
    "Host": "ali-test-project.cn-hangzhou-devcommon-intranet.sls.aliyuncs.com",
    "Date": "Mon, 09 Nov 2015 09:28:21 GMT",
    "x-log-apiversion": "0.6.0",
    "Authorization": "LOG <yourAccessKeyId>:<yourSignature>"
```

Sample responses

```json
Header :
    "date": "Mon, 09 Nov 2015 09:28:21 GMT",
    "connection": "close",
    "x-log-requestid": "5640673599248CAA230836C6",
    "content-length": "0",
    "server": "nginx/1.6.1"
```

#### 1.9.6 UpdateConfig

Updates Logtail configurations. If the Logtail configurations are applied to a machine group, the configurations of the machine group are also updated. Request syntax

```json
PUT /configs/<configName> HTTP/1.1 Authorization: <AuthorizationString> Content-Type:application/json Content-Length:<Content Length> Content-MD5<:<Content MD5> Date: <GMT Date> Host: <Project Endpoint> x-log-apiversion: 0.6.0 x-log-signaturemethod: hmac-sha1
    "configName": "testcategory1",
    "inputType": "file",
    "inputDetail": {
        "logType": "common_reg_log",
        "logPath": "/var/log/httpd/",
        "filePattern": "access.log",
        "localStorage": true,
        "timeFormat": "%Y/%m/%d %H:%M:%S",
        "logBeginRegex": ".*",
        "regex": "(\w+)(\s+)",
        "key" :["key1", "key2"],
        "filterKey":["key1"],
        "filterRegex":["regex1"],
        "topicFormat": "none"
```

`},`

```json
    "outputType": "LogService",
    "outputDetail":
        "logstoreName": "perfcounter"
```

Request elements Request headers The UpdateConfig API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters For information about the request parameters and Logtail configuration examples, see Logtail configurations. Response elements Response headers The UpdateConfig API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters After the request succeeds, the HTTP status code 200 is returned. Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 404 | ConfigNotExist | config {Configname} does not exist |
| 400 | InvalidParameter | invalid config resource json |
| 400 | BadRequest | config resource configname does not match with request |
| 500 | InternalServerError | internal server error |

The configuration fails to be created if an error occurs, for example, the format is incorrect, the required parameters are missing, or the quota is exceeded. Examples Sample requests

```json
PUT /configs/logtail-config-sample Header :
    "Content-Length": 737,
    "Host": "ali-test-project.cn-hangzhou-devcommon-intranet.sls.aliyuncs.com",
    "x-log-bodyrawsize": 737,
    "Content-MD5": "431263EB105D584A5555762A81E869C0",
    "x-log-signaturemethod": "hmac-sha1",
    "Date": "Mon, 09 Nov 2015 09:14:32 GMT",
    "x-log-apiversion": "0.6.0",
    "User-Agent": "log-python-sdk-v-0.6.0",
    "Content-Type": "application/json",
    "Authorization": "LOG <yourAccessKeyId>:<yourSignature>"
Body :
    "outputDetail": {
        "logstoreName": "sls-test-logstore"
```

`},`

```json
    "inputType": "file",
    "inputDetail": {
        "regex": "([\\d\\.] +) \\S+ \\S+ \\[(\\S+) \\S+\\] \"(\\w+) ([^\"]*)\" ([\\d\\.]+
) (\\d+) (\\d+) (\\d+|-) \"([^\"]*)\" \"([^\"]*)\".*",
        "filterKey": [],
        "logPath": "/var/log/nginx/",
        "logBeginRegex": "\\d+\\.\\d+\\.\\d+\\.\\d+ - .*",
        "logType": "common_reg_log",
        "topicFormat": "none",
        "localStorage": true,
        "key": [
            "ip",
            "time",
            "method",
            "url",
            "request_time",
            "request_length",
            "status",
            "length",
            "ref_url",
            "browser"
```

`],`

```json
        "filePattern": "access*.log",
        "timeFormat": "%d/%b/%Y:%H:%M:%S",
        "filterRegex": []
```

`},`

```json
    "outputType": "LogService",
    "configName": "logtail-config-sample"
```

Sample responses

```json
    "date": "Mon, 09 Nov 2015 09:14:32 GMT",
    "connection": "close",
    "x-log-requestid": "564063F899248CAA2300B778",
    "content-length": "0",
    "server": "nginx/1.6.1"
```

### 1.10 Consumer group operations

#### 1.10.1 CreateConsumerGroup

Creates a consumer group in a Logstore. Request syntax

```json
POST /logstores/<logstoreName>/consumergroups HTTP/1.1 Authorization: <AuthorizationString> x-log-bodyrawsize: 0 User-Agent: <UserAgent> x-log-apiversion: 0.6.0 Host: <Project Endpoint> x-log-signaturemethod: hmac-sha1 Date: <GMT Date> Content-Type: application/json Content-MD5: F58544E4D022CC28A93D0B7CC208A5AA Content-Length: <ContentLength>
  "consumerGroup": <consumerGroup>,
  "timeout": <timeout>,
  "order": <order>
```

Request elements Request headers The CreateConsumerGroup API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| logstoreName | String | Yes | The name of the Logstore. |
| consumerGroup | String | Yes | The name of the consumer group. The name must be unique in a project. |
| timeout | Integer | Yes | The timeout period. If Log Service does not receive a heartbeat message from a consumer within the timeout period, the consumer is deleted. |

| Service |   |   | Developer Guide·API Referenc |
|---|---|---|---|
| Parameter | Type | Required | Description |
| order | Boolean | Yes | Specifies whether to consume data in sequence from a single shard. Valid values: true: The data in a single shard is consumed in sequence. The data in the original shard is first consumed after the shard is split. Then, the data in the new shards is consumed at the same time. false: The data in a single shard is randomly consumed. |

Response elements Response headers The CreateConsumerGroup API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters The HTTP status code 200 is returned. Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 400 | ConsumerGroupAlreadyExist | consumer group already exist |
| 400 | JsonInfoInvalid | consumerGroup or timeout is of error format |
| 404 | ProjectNotExist | The Project does not exist : {Project} |
| 404 | LogStoreNotExist | logstore {logstoreName} does not exist |
| 500 | InternalServerError | Specified Server Error Message |

Examples Sample requests

```json
POST /logstores/my-logstore/consumergroups HTTP/1.1 Header: Authorization: LOG <yourAccessKeyId>:<yourSignature> x-log-bodyrawsize: 0 User-Agent: sls-java-sdk-v-0.6.1 x-log-apiversion: 0.6.0 Host: my-project.cn-shanghai.log.aliyuncs.com x-log-signaturemethod: hmac-sha1 Date: Fri, 04 May 2018 08:02:22 GMT Content-Type: application/json Content-MD5: F58544E4D022CC28A93D0B7CC208A5AA Content-Length: 65 Connection: Keep-Alive Body:
  "consumerGroup": "consumer-group-1",
  "timeout": 300,
  "order": true
```

Sample responses

```
HTTP/1.1 200 Server: nginx/1.12.1 Content-Length: 0 Connection: close Access-Control-Allow-Origin: * Date: Fri, 04 May 2018 08:15:11 GMT x-log-requestid: 5AEC168FA796F4195BF404CB
```

#### 1.10.2 DeleteConsumerGroup

Deletes a consumer group. Request syntax

```
DELETE /logstores/<logstoreName>/consumergroups/<consumerGroupName> HTTP/1.1 Authorization: <AuthorizationString> x-log-bodyrawsize: 0 User-Agent: <UserAgent> x-log-apiversion: 0.6.0 Host: <Project Endpoint> x-log-signaturemethod: hmac-sha1 Date: <GMT Date> Content-Type: application/x-protobuf Content-MD5: F58544E4D022CC28A93D0B7CC208A5AA
```

Request elements Request headers The DeleteConsumerGroup API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| logstoreName | String | Yes | The name of the Logstore to which the consumer group belongs. |
| consumerGroup | String | Yes | The consumer group to be deleted. |

Response elements Response headers The DeleteConsumerGroup API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters The HTTP status code 200 is returned. Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 404 | ProjectNotExist | The Project does not exist : {Project} |
| 404 | LogStoreNotExist | logstore {logstoreName} does not exist |
| 500 | InternalServerError | Specified Server Error Message |

Additional considerations If you attempt to delete a consumer group that does not exist, the system will return a success message. Examples Sample requests

```
DELETE /logstores/logstore-test/consumergroups/consumer-group-1 HTTP/1.1 Header: Authorization: LOG <yourAccessKeyId>:<yourSignature> x-log-bodyrawsize: 0 User-Agent: sls-java-sdk-v-0.6.1 x-log-apiversion: 0.6.0 Host: my-project.cn-shanghai.log.aliyuncs.com x-log-signaturemethod: hmac-sha1 Date: Fri, 04 May 2018 08:02:22 GMT Content-Type: application/json Content-MD5: F58544E4D022CC28A93D0B7CC208A5AA Content-Length: 65 Connection: Keep-Alive
```

Sample responses

```
HTTP/1.1 200 Server: nginx/1.12.1 Content-Length: 0 Connection: close Access-Control-Allow-Origin: * Date: Fri, 04 May 2018 08:15:11 GMT x-log-requestid: 5AEC168FA796F4195BF404CB
```

#### 1.10.3 GetCheckPoint

Queries the checkpoints of one or all shards from which data is consumed by a consumer group. Request syntax

```
GET /logstores/<logstoreName>/consumergroups/<consumerGroup>? shard=<shardId> HTTP/1.1 Authorization: <AuthorizationString> x-log-bodyrawsize: 0 User-Agent: <UserAgent> x-log-apiversion: 0.6.0 Host: <Project Endpoint> x-log-signaturemethod: hmac-sha1 Date: <GMT Date> Content-Type: application/json Connection: Keep-Alive
```

Request elements Request headers The GetCheckPoint API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| logstoreName | String | Yes | The name of the Logstore to which the consumer group belongs. |
| consumerGroup | String | Yes | The name of the consumer group. |
| shardId | Integer | No | The ID of the shard. If the specified shard does not exist, an empty list is returned. If the shard ID is not specified, the checkpoints of all shards are returned. |

Response elements Response headers The GetCheckPoint API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters After the request succeeds, the response body contains the checkpoint of the shard from which data is consumed by the specified consumer group. The following table describes the response parameters.

| Parameter | Type | Description |
|---|---|---|
| shard | Integer | The ID of the shard. |
| checkpoint | String | The value of the checkpoint. |
| updateTime | Integer | The time when the checkpoint was last updated. |
| consumer | String | The consumer that consumes data from the shard. |

Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 404 | ProjectNotExist | The Project does not exist : {Project} |
| 404 | LogStoreNotExist | logstore {logstoreName} does not exist |
| 404 | ConsumerGroupNotExist | consumer group not exist |
| 500 | InternalServerError | Specified Server Error Message |

Examples Sample requests

```
GET /logstores/my-logstore/consumergroups/consumer_group_test? shard=0 Authorization: LOG <yourAccessKeyId>:<yourSignature> x-log-bodyrawsize: 0 User-Agent: sls-java-sdk-v-0.6.1 x-log-apiversion: 0.6.0 Host: my-project.cn-shanghai.log.aliyuncs.com x-log-signaturemethod: hmac-sha1 Date: Fri, 04 May 2018 09:26:53 GMT Content-Type: application/x-protobuf Connection: Keep-Alive
```

Sample responses

```
HTTP/1.1 200 Server: nginx/1.12.1 Content-Type: application/json Content-Length: 111 Connection: close Access-Control-Allow-Origin: * Date: Fri, 04 May 2018 09:26:53 GMT x-log-requestid: 5AEC275D1FFC036AB254B20C
```

`[`

```json
    "shard": 0,
    "checkpoint": "MTUyNDE1NTM3OTM3MzkwODQ5Ng==",
    "updateTime": 1524224984800922,
    "consumer": "consumer_1"
```

`]`

#### 1.10.4 HeartBeat

Sends a heartbeat packet to Log Service for a consumer. Request syntax

```
POST /logstores/<logstoreName>/consumergroups/<consumerGroup>? type=heartbeat&consumer=<con sumer> HTTP/1.1 Authorization: <AuthorizationString> x-log-bodyrawsize: 0 User-Agent: <UserAgent> x-log-apiversion: 0.6.0 Host: <Project Endpoint> x-log-signaturemethod: hmac-sha1 Date: <GMT Date> Content-Type: application/json Content-MD5: F58544E4D022CC28A93D0B7CC208A5AA Content-Length: <ContentLength> <shard ID list>
```

Request elements Request headers The HeartBeat API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| logstoreName | String | Yes | The name of the Logstore. The name must be unique in a project. |
| consumerGroup | String | Yes | The name of the consumer group. The name must be unique in a project. |
| consumer | String | Yes | The consumer. |
| {Shard ID List} | Array | Yes | The ID list of shards from which data is consumed. |

Response elements Response headers The HeartBeat API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters After the request succeeds, the HTTP status code 200 is returned. An ID list is also returned, containing all shards from which data are consumed by the consumer. Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 400 | NotExistConsumerWithBody | non-exist consumer with non- empty body of heartbeat message |
| 404 | ProjectNotExist | The Project does not exist : {Project} |
| 404 | LogStoreNotExist | logstore {logstoreName} does not exist |
| 404 | ConsumerGroupNotExist | consumer group not exist |
| 500 | InternalServerError | Specified Server Error Message |

Additional considerations The heartbeat packet can be sent only when the connection between the consumer and Log Service is established. Examples Sample requests

```
POST /logstores/my-logstore/consumergroups/consumer_group_test? type=heartbeat&consumer=c onsumer_1 HTTP/1.1 Authorization: LOG <yourAccessKeyId>:<yourSignature> x-log-bodyrawsize: 0 User-Agent: sls-java-sdk-v-0.6.1 x-log-apiversion: 0.6.0 Host: my-project.cn-shanghai.log.aliyuncs.com x-log-signaturemethod: hmac-sha1 Date: Sun, 06 May 2018 09:44:10 GMT Content-Type: application/json Content-MD5: 8D5162CA104FA7E79FE80FD92BB657FB Content-Length: 3 Connection: Keep-Alive [0]
```

Sample responses

```
HTTP/1.1 200 Server: nginx/1.12.1 Content-Type: application/json Content-Length: 5 Connection: close Access-Control-Allow-Origin: * Date: Sun, 06 May 2018 09:44:11 GMT x-log-requestid: 5AEECE6B1FFC0366B2553FB5 [0,1]
```

#### 1.10.5 ListConsumerGroup

Lists all consumer groups of a Logstore. Request syntax

```
GET /logstores/<logstoreName>/consumergroups HTTP/1.1 Authorization: <AuthorizationString> x-log-bodyrawsize: 0 User-Agent: <UserAgent> x-log-apiversion: 0.6.0 Host: <Project Endpoint> x-log-signaturemethod: hmac-sha1 Date: <GMT Date> Content-Type: application/x-protobuf Connection: Keep-Alive
```

Request elements Request headers The ListConsumerGroup API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| logstoreName | String | Yes | The name of the Logstore. |

Response elements Response headers The ListConsumerGroup API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters After the ListConsumerGroup request succeeds, the response body contains a list of all consumer groups that read log data from the specified Logstore. The following table describes the response parameters.

| Parameter | Type | Description |
|---|---|---|
| consumerGroup | String | The name of the consumer group. |
| timeout | Integer | The timeout period. If the specified Logstore does not receive a heartbeat packet from the consumer group during the timeout period, the consumer group is deleted. |
| order | Boolean | Indicates whether log data was consumed in sequence. |

Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 404 | ProjectNotExist | The Project does not exist : {Project} |
| 404 | LogStoreNotExist | logstore {logstoreName} does not exist |
| 500 | InternalServerError | Specified Server Error Message |

Examples Sample requests

```
GET /logstores/my-logstore/consumergroups HTTP/1.1 Authorization: LOG <yourAccessKeyId>:<yourSignature> x-log-bodyrawsize: 0 User-Agent: sls-java-sdk-v-0.6.1 x-log-apiversion: 0.6.0 Host: my-project.cn-shanghai.log.aliyuncs.com x-log-signaturemethod: hmac-sha1 Date: Fri, 04 May 2018 08:47:30 GMT Content-Type: application/x-protobuf Connection: Keep-Alive
```

Sample responses

```
HTTP/1.1 200 Server: nginx/1.12.1 Content-Type: application/json Connection: close Access-Control-Allow-Origin: * Date: Fri, 04 May 2018 08:47:31 GMT x-log-requestid: 5AEC1E23048191954B42EAB9
```

`[`

```json
    "name": "test-consumer-group",
    "timeout": 30,
    "order": true
```

`]`

#### 1.10.6 UpdateCheckPoint

Updates the checkpoint of a shard in a Logstore of a project for a consumer group. Request syntax

```json
POST /logstores/<logstoreName>/consumergroups/<consumerGroupName>? forceSuccess=<forceSucce ss>&type=checkpoint&consumer=<consumer> HTTP/1.1 Authorization: <AuthorizationString> x-log-bodyrawsize: 0 User-Agent: <UserAgent> x-log-apiversion: 0.6.0 Host: <Project Endpoint> x-log-signaturemethod: hmac-sha1 Date: <GMT Date> Content-Type: application/json Content-Length: <ContentLength> Connection: Keep-Alive
  "shard": <shardID>,
  "checkpoint": <checkpoint>
```

Request elements Request headers The UpdateCheckPoint API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| logstoreName | String | Yes | The name of the Logstore to which the consumer group belongs. |
| consumerGroup | String | Yes | The name of the consumer group. |
| forceSuccess | Boolean | No | Specifies whether to forcibly update the consumer group. |
| consumer | String | No | The consumer. |
| shard | Integer | Yes | The ID of the shard. |
| checkpoint | String | Yes | The value of the checkpoint. |

Response elements Response headers The UpdateCheckPoint API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters The HTTP status code 200 is returned. Error codes In addition to Common error codes, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 400 | InvalidShardCheckPoint | shard checkpoint not encoded by base64 |
| 404 | ProjectNotExist | The Project does not exist : {Project} |
| 404 | LogStoreNotExist | logstore {logstoreName} does not exist |
| 404 | ConsumerGroupNotExist | consumer group not exist |

| eveloper Guide·API Reference |   | Log Servic |
|---|---|---|

| HTTP status code | Error code | Error message |
|---|---|---|
| 404 | ShardNotExist | shard not exist |
| 500 | InternalServerError | Specified Server Error Message |

Additional considerations If the consumer is not specified, the checkpoint can be updated only when the forceSuccess parameter is set to true. Examples Sample requests

```json
POST /logstores/logstore-4/consumergroups/consumer_group_test? forceSuccess=false&type=ch eckpoint&consumer=consumer_1 HTTP/1.1 Authorization: LOG <yourAccessKeyId>:<yourSignature> x-log-bodyrawsize: 0 User-Agent: sls-java-sdk-v-0.6.1 x-log-apiversion: 0.6.0 Host: my-project.cn-shanghai.log.aliyuncs.com x-log-signaturemethod: hmac-sha1 Date: Sun, 06 May 2018 09:14:53 GMT Content-Type: application/json Content-MD5: 59457BAFB3F85A5117BDE243947583B0 Content-Length: 55 Connection: Keep-Alive
  "shard": 0,
  "checkpoint": "MTUyNDE1NTM3OTM3MzkwODQ5Ng=="
```

Sample responses

```
HTTP/1.1 200 Server: nginx/1.12.1 Content-Length: 0 Connection: close Access-Control-Allow-Origin: * Date: Sun, 06 May 2018 09:14:54 GMT x-log-requestid: 5AEEC78E1FFC0366B24F1C63
```

#### 1.10.7 UpdateConsumerGroup

Updates the attributes of a consumer group. Request syntax

```json
PUT /logstores/<logstoreName>/consumergroups/<consumerGroupName> HTTP/1.1 Authorization: <AuthorizationString> x-log-bodyrawsize: 0 User-Agent: <UserAgent> x-log-apiversion: 0.6.0 Host: <Project Endpoint> x-log-signaturemethod: hmac-sha1 Date: <GMT Date> Content-Type: application/json Content-MD5: F58544E4D022CC28A93D0B7CC208A5AA Content-Length: <ContentLength>
  "timeout": <timeout>,
  "order": <order>
```

Request elements Request headers The UpdateConsumerGroup API operation does not have special request headers. For information about common request headers of Log Service API operations, see Common request headers. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| logstoreName | String | Yes | The name of the Logstore to which the consumer group belongs. |
| consumerGroup | String | Yes | The name of the consumer group. |
| timeout | Integer | No | The timeout period. If Log Service does not receive a heartbeat packet during the timeout period, the consumer group is deleted. |
| order | Boolean | No | Specifies whether to consume data in sequence from a single shard. Valid values: true: The data in a single shard is consumed in sequence. The data in the original shard is first consumed after the shard is split. Then, the data in the new shards is consumed at the same time. false: The data in a single shard is randomly consumed. |

> Not e You must specify the `timeout` or `order` parameter, or specify both parameters.

Response elements Response headers The UpdateConsumerGroup API operation does not have special response headers. For information about common response headers of Log Service API operations, see Common response headers. Response parameters The HTTP status code 200 is returned. Error codes In addition to Common response headers, the API operation may also return the following special error codes.

| HTTP status code | Error code | Error message |
|---|---|---|
| 400 | JsonInfoInvalid | timeout is of error value type |
| 404 | ProjectNotExist | The Project does not exist : {Project} |
| 404 | ConsumerGroupNotExist | consumer group not exist |
| 404 | LogStoreNotExist | logstore {logstoreName} does not exist |
| 500 | InternalServerError | Specified Server Error Message |

Examples Sample requests

```json
PUT /logstores/logstore-test/consumergroups/consumer-group-1 HTTP/1.1 Header: Authorization: LOG <yourAccessKeyId>:<yourSignature> x-log-bodyrawsize: 0 User-Agent: sls-java-sdk-v-0.6.1 x-log-apiversion: 0.6.0 Host: my-project.cn-shanghai.log.aliyuncs.com x-log-signaturemethod: hmac-sha1 Date: Fri, 04 May 2018 08:02:22 GMT Content-Type: application/json Content-MD5: F58544E4D022CC28A93D0B7CC208A5AA Content-Length: 65 Connection: Keep-Alive Body:
  "order": false,
  "timeout": 100
```

Sample responses

```
HTTP/1.1 200 Server: nginx/1.12.1 Content-Length: 0 Connection: close Access-Control-Allow-Origin: * Date: Fri, 04 May 2018 08:15:11 GMT x-log-requestid: 5AEC168FA796F4195BF404CB
```

### 1.11 RAM or STS

#### 1.11.1 Overview

Use RAM to authorize a RAM user to access Log Service resources of an Alibaba Cloud account You can create projects, Logstores, Logtail configurations, and machine group in Log Service. You have full permissions on these resources. You can call all relevant API operations to use the resources. However, if you use your Alibaba Cloud account to create a RAM user, the RAM user is unauthorized to use your resources in Log Service. To allow the RAM user to use your resources, you must grant relevant permissions on the resources to the RAM user. You can use RAM policies to grant a RAM user the following permissions on Log Service resources: Upload data to a specified Logstore If you grant this permission to a RAM user, the RAM user can upload data to the specified Logstore by using the relevant API or SDK. The policy is as follows:

```json
    "Version": "1",
    "Statement": [
        "Action": [
          "log:Post*",
          "log:BatchPost*"
```

`],`

```json
        "Resource": ["acs:log:*:*:project/<The name of the specified proejct>/logstore/<T
he name of the specified Logstore>"],
        "Effect": "Allow"
```

`]` Query data of a specified Logstore in the console If you grant this permission to a RAM user, the RAM user can query logs, pull logs, and view the Logstore list after logging on to the Log Service console. The policy is as follows:

```json
    "Version": "1",
    "Statement": [
        "Action": ["log:List*"],
        "Resource": ["acs:log:*:*:project/<The name of the specified proejct>/*"],
        "Effect": "Allow"
```

`},`

```json
        "Action": ["log:Get*"],
        "Resource": ["acs:log:*:*:project/<The name of the proejct>/logstore/<The name of
the Logstore>"],
        "Effect": "Allow"
```

`]` You can skip this topic if you do not need to grant access to your Log Service resources across accounts. Skipping this topic does not affect your understanding and use of the other topics in the document. Related topics:

#### 1.11.2 Resource list

This topic describes the resources whose permissions you can grant to a RAM user. You can use an Alibaba Cloud account to grant a RAM user specific permissions on Log Service resources. The following table lists the resources and relevant expressions.

| Resource | Expression in policies |
|---|---|
| Project and Logstore | acs:log:${regionName}:${projectOwnerAliUid}:project/${projectName}/l ogstore/${logstoreName} |
| Project, Logstore, and LogShipper | acs:log:${regionName}:${projectOwnerAliUid}:project/${projectName}/l ogstore/${logstoreName}/shipper/${shipperName} |
|   | acs:log:${regionName}:${projectOwnerAliUid}:project/${projectName}/l ogstore/* |
| Project and Logtail | acs:log:${regionName}:${projectOwnerAliUid}:project/${projectName}/l ogtailconfig/${logtailconfig} |
|   | acs:log:${regionName}:${projectOwnerAliUid}:project/${projectName}/l ogtailconfig/* |
|   | acs:log:${regionName}:${projectOwnerAliUid}:project/${projectName}/ machinegroup/${machineGroupName} |
| 43 | > Document Version: 2022092 |

| og Service | Developer Guide·API Referenc |
|---|---|
| Project and machine group Resource | Expression in policies |
|   | acs:log:${regionName}:${projectOwnerAliUid}:project/${projectName}/ machinegroup/* |
| Project and consumer group | acs:log:${regionName}:${projectOwnerAliUid}:project/${projectName}/l ogstore/${logstoreName}/consumergroup/${consumerGroupName} |
|   | acs:log:${regionName}:${projectOwnerAliUid}:project/${projectName}/l ogstore/${logstoreName}/consumergroup/* |
| Project and saved search | acs:log:${regionName}:${projectOwnerAliUid}:project/${projectName}/s avedsearch/${savedSearchName} |
|   | acs:log:${regionName}:${projectOwnerAliUid}:project/${projectName}/s avedsearch/* |
| Project and dashboard | acs:log:${regionName}:${projectOwnerAliUid}:project/${projectName}/d ashboard/${dashboardName} |
|   | acs:log:${regionName}:${projectOwnerAliUid}:project/${projectName}/d ashboard/* |
| Project and alert | acs:log:${regionName}:${projectOwnerAliUid}:project/${projectName}/a lert/${alarmName} |
|   | acs:log:${regionName}:${projectOwnerAliUid}:project/${projectName}/a lert/* |
| All types of resources | acs:log:${regionName}:${projectOwnerAliUid}:* |
|   | acs:log:*:${projectOwnerAliUid}:* |

> Not e The resources in Log Service have hierarchical relationships. Projects are root resources. Logstores, Logtail, and machine groups are parallel sub-resources of projects. LogShipper and consumer groups are sub-resources of Logstores.

The following table describes the parameters that are used in policies.

| Parameter | Description |
|---|---|
| ${regionName} | The name of a region. |
| ${projectOwnerAliUid} | The ID of an Alibaba Cloud account. |
| ${projectName} | The name of a project. |
| ${logstoreName} | The name of a Logstore. |
| ${logtailconfig} | The name of a Logtail configuration. |
| ${machineGroupName} | The name of a machine group. |

| D | eveloper Guide·API Reference | Log Servic | e |
|---|---|---|---|

| Parameter | Description |
|---|---|
| ${shipperName} | The name of a LogShipper rule. |
| ${consumerGroupName} | The name of a consumer group. |
| ${savedSearchName} | The name of a saved search. |
| ${dashboardName} | The name of a dashboard. |
| ${alarmName} | The name of an alert rule. |

#### 1.11.3 Action list

This topic describes the actions that a RAM user can perform on Log Service resources after you grant the relevant permissions to the RAM user in the RAM console. Actions In the RAM console, you can authorize a RAM user to perform the following actions on Log Service resources.

| Action | Description |
|---|---|
| CreateProject | Creates a project. |
| GetLogs | Queries logs in a Logstore of a project. |
| GetHistograms | Queries the distribution of logs in a Logstore of a project. |
| GetLogstore | Queries the attributes of a Logstore. |
| ListLogstore | Lists all Logstores in a project. |
| CreateLogstore | Creates a Logstore in a project. |
| DeleteLogstore | Deletes a Logstore, including all shards and indexes in the Logstore. |
| UpdateLogstore | Updates the attributes of a Logstore. |
| GetCursorOrData (GetCursor and PullLogs) | Queries a cursor based on a point in time. It can also be used to query logs based on a cursor and quantity. |
| ListShards | Lists all available shards in a Logstore. |
| PostLog | Writes log data to a Logstore. |
| CreateConfig | Creates a Logtail configuration in a project. |
| UpdateConfig | Updates a Logtail configuration. |

| og Service | Developer Guide·API Referenc |
|---|---|
| Action | Description |
| DeleteConfig | Deletes a Logtail configuration. |
| GetConfig | Queries the details of a Logtail configuration. |
| UpdateConfig | Lists all Logtail configurations in a project. You can set the relevant parameters to show the configurations on multiple pages. |
| CreateMachineGroup | Creates a machine group to specify the servers from which logs are collected. |
| UpdateMachineGroup | Updates the information of a machine group. |
| DeleteMachineGroup | Deletes a machine group. |
| GetMachineGroup | Queries the details of a machine group. |
| ListMachineGroup | Lists machine groups. |
| ListMachines | Lists your machines in a machine group that is connected with Log Service. |
| ApplyConfigToMachineGroup | Applies a Logtail configuration to a machine group. |
| RemoveConfigFromMachineGroup | Deletes a Logtail configuration from a machine group. |
| GetAppliedConfigs | Queries the name of Logtail configuration applied to a machine group. |
| CreateConsumerGroup | Creates a consumer group in a Logstore. |
| UpdateConsumerGroup | Modifies the attributes of a consumer group. |
| DeleteConsumerGroup | Deletes a consumer group. |
| ListConsumerGroup | Lists all consumer groups of a Logstore. |
| UpdateCheckPoint | Updates the checkpoint of a shard for a consumer group. |
| HeartBeat | Sends a heartbeat packet to Log Service for a consumer. |
| GetCheckPoint | Queries the checkpoints of one or all shards from which data is consumed by a consumer group. |
| CreateIndex | Creates one or more indexes for a Logstore. |
| DeleteIndex | Deletes one or more indexes from a Logstore. |
| GetIndex | Queries one or more indexes of a Logstore. |

| D | eveloper Guide·API Reference | Log Servic | e |
|---|---|---|---|

| Action | Description |
|---|---|
| UpdateIndex | Updates one or more indexes of a Logstore. |
| log:CreateSavedSearch | Creates a saved search. |
| log:UpdateSavedSearch | Updates a saved search. |
| log:GetSavedSearch | Queries a saved search. |
| log:DeleteSavedSearch | Deletes a saved search. |
| log:ListSavedSearch | Queries the saved search list. |
| log:CreateDashboard | Creates a dashboard. |
| log:UpdateDashboard | Updates a dashboard. |
| log:GetDashboard | Queries a dashboard. |
| log:DeleteDashboard | Deletes a dashboard. |
| log:ListDashboard | Queries the dashboard list. |
| log:CreateJob | Creates a job, for example, an alert or subscription. |
| log:UpdateJob | Updates a job. |
| log:CreateApp | Grants a RAM user the permission to create an application, for example, Cost Manager or Log Audit Service. |
| log:UpdateApp | Grants a RAM user the permission to update an application, for example, Cost Manager or Log Audit Service. |
| log:GetApp | Grants a RAM user the permission to view an application, for example, Cost Manager or Log Audit Service. |
| log:DeleteApp | Grants a RAM user the permission to delete an application, for example, Cost Manager or Log Audit Service. |

#### 1.11.4 Authentication rules

When a RAM user calls Log Service API operations to access the resources of an Alibaba Cloud account, Log Service authenticate the RAM user. This ensures that the resource owner has granted the RAM user the relevant permissions on the resources. This topic describes the authentication rules that apply when a RAM user calls Log Service APIs to access the resources of an Alibaba Cloud account. Logstore authentication rules Each Log Service API operation determines which permissions to check based on the relevant resources and the API syntax. The following table describes the Logstore authentication rules for the relevant API operations.

| Operation |   | Resource |   |
|---|---|---|---|
| log:GetLogStore |   | acs:log:${regionName}:${projectOwnerAliUid}:projec t/${projectName}/logstore/${logstoreName} |   |
| log:ListLogStores |   | acs:log:${regionName}:${projectOwnerAliUid}:projec t/${projectName}/logstore/* |   |
| log:CreateLogStore |   | acs:log:${regionName}:${projectOwnerAliUid}:projec t/${projectName}/logstore/* |   |
| log:DeleteLogStore |   | acs:log:${regionName}:${projectOwnerAliUid}:pr oject/${projectName}/logstore/${logstoreName} |   |
|   |   |   | acs:log:${regionName}:${projectOwnerAliUid}:pr |
|   | DeleteLogStore | oject/${projectName}/logstore/${logstoreName} |   |
| log:UpdateLogStore |   | acs:log:${regionName}:${projectOwnerAliUid}:pr oject/${projectName}/logstore/${logstoreName} |   |
|   |   |   | acs:log:${regionName}:${projectOwnerAliUid}:pr |
|   | UpdateLogStore | oject/${projectName}/logstore/${logstoreName} |   |

LogHub authentication rules The following table describes the LogHub authentication rules of the relevant data write and consumption API operations. The GetCursor and GetLogs API operations are included in the log:GetCursorOrData API operation.

| Operation |   | Resource |   |
|---|---|---|---|
| log:GetCursorOrData |   | acs:log:${regionName}:${projectOwnerAliUid}:projec t/${projectName}/logstore/${logstoreName} |   |
| log:ListShards |   | acs:log:${regionName}:${projectOwnerAliUid}:pr oject/${projectName}/logstore/${logstoreName} |   |
|   |   |   | acs:log:${regionName}:${projectOwnerAliUid}:pr |
|   | ListShards | oject/${projectName}/logstore/${logstoreName} |   |
| log:PostLogStoreLogs |   | acs:log:${regionName}:${projectOwnerAliUid}:pr oject/${projectName}/logstore/${logstoreName} |   |
|   |   |   | acs:log:${regionName}:${projectOwnerAliUid}:pr |
|   | PostLogStoreLogs | oject/${projectName}/logstore/${logstoreName} |   |

Configuration authentication rules

| Operation |   | Resource |   |   |
|---|---|---|---|---|
| log:CreateConfig |   | acs:log:${regionName}:${projectOwnerAliUid}:pr oject/${projectName}/logtailconfig/* |   |   |
| log:UpdateConfig |   | acs:log:${regionName}:${projectOwnerAliUid}:pr |   |   |
|   |   |   | acs:log:${regionName}:${projectOwnerAliUid}:pr |   |
|   | UpdateConfig | oject/${projectName}/logtailconfig/${logtailCon |   |   |
|   |   | figName} |   |   |

|   |   | acs:log:${regionName}:${projectOwnerAliUid}:pr |
|---|---|---|
| CreateConfig | oject/${projectName}/logtailconfig/* |   |

| eveloper Guide·API Reference | Log Servic |
|---|---|

| Operation |   | Resource |   |   |
|---|---|---|---|---|
| log:DeleteConfig |   | acs:log:${regionName}:${projectOwnerAliUid}:pr |   |   |
|   |   |   | acs:log:${regionName}:${projectOwnerAliUid}:pr |   |
|   | DeleteConfig | oject/${projectName}/logtailconfig/${logtailCon |   |   |
|   |   | figName} |   |   |
| log:GetConfig |   | acs:log:${regionName}:${projectOwnerAliUid}:pr |   |   |
|   |   |   | acs:log:${regionName}:${projectOwnerAliUid}:pr |   |
|   | GetConfig | oject/${projectName}/logtailconfig/${logtailCon |   |   |
|   |   | figName} |   |   |
| log:ListConfig |   | acs:log:${regionName}:${projectOwnerAliUid}:pr oject/${projectName}/logtailconfig/* |   |   |

|   |   | acs:log:${regionName}:${projectOwnerAliUid}:pr |
|---|---|---|
| ListConfig | oject/${projectName}/logtailconfig/* |   |

Machine group authentication rules

| Operation |   | Resource |   |   |
|---|---|---|---|---|
| log:CreateMachineGroup |   | acs:log:${regionName}:${projectOwnerAliUid}:pr oject/${projectName}/machinegroup/* |   |   |
| log:UpdateMachineGroup |   | acs:log:${regionName}:${projectOwnerAliUid}:pr |   |   |
|   |   |   | acs:log:${regionName}:${projectOwnerAliUid}:pr |   |
|   | UpdateMachineGroup | oject/${projectName}/machinegroup/${machineGro |   |   |
|   |   | upName} |   |   |
| log:DeleteMachineGroup |   | acs:log:${regionName}:${projectOwnerAliUid}:projec t/${projectName}/machinegroup/${machineGroupNa me} |   |   |
| log:GetMachineGroup |   | acs:log:${regionName}:${projectOwnerAliUid}:pr |   |   |
|   |   |   | acs:log:${regionName}:${projectOwnerAliUid}:pr |   |
|   | GetMachineGroup | oject/${projectName}/machinegroup/${machineGro |   |   |
|   |   | upName} |   |   |
| log:ListMachineGroup |   | acs:log:${regionName}:${projectOwnerAliUid}:pr oject/${projectName}/machinegroup/* |   |   |
| log:ListMachines |   | acs:log:${regionName}:${projectOwnerAliUid}:projec t/${projectName}/machinegroup/${machineGroupNa me} |   |   |

|   |   | acs:log:${regionName}:${projectOwnerAliUid}:pr |
|---|---|---|
| CreateMachineGroup | oject/${projectName}/machinegroup/* |   |

|   |   | acs:log:${regionName}:${projectOwnerAliUid}:pr |
|---|---|---|
| ListMachineGroup | oject/${projectName}/machinegroup/* |   |

Interactive API operations for configurations and machine groups

| Operation |   | Resource |   |   |
|---|---|---|---|---|
|   |   | acs:log:${regionName}:${projectOwnerAliUid}:pr |   |   |
|   |   |   | acs:log:${regionName}:${projectOwnerAliUid}:pr |   |
|   |   | oject/${projectName}/logtailconfig/${logtailCon |   |   |
|   |   | figName} |   |   |
| log:ApplyConfigToGroup |   | acs:log:${regionName}:${projectOwnerAliUid}:proj |   |   |
|   |   | ect/${projectName}/machinegroup/${machineGro |   |   |
|   |   | upName} |   |   |

| Operation |   | Resource |   |   |
|---|---|---|---|---|
|   |   | acs:log:${regionName}:${projectOwnerAliUid}:pr |   |   |
|   |   |   | acs:log:${regionName}:${projectOwnerAliUid}:pr |   |
|   |   | oject/${projectName}/logtailconfig/${logtailCon |   |   |
|   |   | figName} |   |   |
| log:RemoveConfigFromGroup |   | acs:log:${regionName}:${projectOwnerAliUid}:proj |   |   |
|   |   | ect/${projectName}/machinegroup/${machineGroup |   |   |
|   |   | Name} |   |   |
| log:GetAppliedMachineGroups |   | acs:log:${regionName}:${projectOwnerAliUid}:pr |   |   |
|   |   |   | acs:log:${regionName}:${projectOwnerAliUid}:pr |   |
|   | GetAppliedMachineGroups | oject/${projectName}/logtailconfig/${logtailCon |   |   |
|   |   | figName} |   |   |
| log:GetAppliedConfigs |   | acs:log:${regionName}:${projectOwnerAliUid}:pr |   |   |
|   |   |   | acs:log:${regionName}:${projectOwnerAliUid}:pr |   |
|   | GetAppliedConfigs | oject/${projectName}/machinegroup/${machineGro |   |   |
|   |   | upName} |   |   |

### 1.12 Description of common resources

resources

#### 1.12.1 Encrypt data

Log Service allows you to use Key Management Service (KMS) to encrypt data for secure storage. This topic describes the data encryption mechanism of Log Service and how to encrypt data by using KMS. Data encryption mechanism Log Service encrypts data by using KMS. The data encryption mechanism has the following characteristics: Log Service supports the Advanced Encryption Standard (AES) encryption algorithm.和国密算法SM4 You can create and manage a customer master key (CMK) in the KMS console to ensure the security of the CMK. Log Service supports the following encryption types: Service key-based encryption: Log service generates an independent service key for each Logstore. The service key never expires. Bring Your Own Key (BYOK) encryption: You can create a CMK in the KMS console and grant the relevant permissions to Log Service. When Log Service calls a KMS API operation, this CMK is used to create a key for data encryption. If the CMK is deleted or disabled, the BYOK key becomes invalid.

> Not ice
> You can configure data encryption for a Logstore only when you call the CreateProject operation to create the Logstore. The algorithm or type of data encryption cannot be changed after the Logstore is created.
> If the CMK created in the KMS console becomes invalid, all read and write requests on the Logstore fail.
> The CMK generated by the service key of Log Service does not rotate.

Service key-based encryption When you call the CreateProject operation to create a Logstore, add the encrypt_conf node to encrypt data by using the following sample code:

```json
encrypt_conf = {
    "enable" : True, # If you set the value to True, data encryption is enabled.
    "encrypt_type": "aes_gcm", # The encryption algorithm. You can set the value tosm4_gcm
或aes_gcm.
```

Bring Your Own Key (BYOK) encryption
1. In the KMS console, create a BYOK.
For more information, see the Key Management Service (KMS) > Creat e a CMK topic in User Gui de.
2. Create a level -1 organization.
i. Log on to the Apsara Uni-manager Management Console. For more information, see the User Guide > Log on t o t he Apsara Uni-manager Management Console topic. ii. Creates an organization. For more information, see the User Guide > Ent erprise > Organizat ions > Creat e an organizat ion topic in User Guide.
3. Create a RAM role for a level -1 organization.
i. In the top navigation bar of the Apsara Uni-manager Management Console, click Conf igurat ions. ii. On the RAM Service Linked Role tab, click Creat e RAM Role. iii. In the Organizat ion Name drop-down list, select the created organization. In the Service Name drop-down list, select Log Service, and click OK. iv. On the RAM Service Linked Role page, find the AliyunLogAccessingKMSRole service role, and click Det ails to obtain the ARN of the RAM role.
4. When you call the CreateProject operation to create a Logstore, add the encrypt_conf node to
encrypt data by using the following sample code:

```json
encrypt_conf = {
    "enable" : True, # If you set the value to True, data encryption is enabled.
    "encrypt_type": "aes_gcm", # The encryption algorithm. You can set the value tosm4_
gcm或aes_gcm.
    "user_cmk_info":
            "cmk_key_id": "", # The ID of the CMK that you created in Step 1.
            "arn": "", # The ARN of the RAM role that is obtained in Step 3.
            "region_id" : ""# The ID of the region where the CMK resides.
```

#### 1.12.2 Data model

This topic describes the data model of Log Service. Project A project is a basic management unit in Log Service and is used to isolate and control resources. You can use a project to manage all logs and log sources of an application. Logstore A Logstore is a unit that collects, stores, and consumes logs in Log Service. Each Logstore belongs to a single project. Each project can have multiple Logstores. You can create multiple Logstores for a project based on your business requirements. We recommend that you create an independent Logstore for each type of logs in an application. For example, you have a game application named big-game. The server stores three types of logs: operation_log, application_log, and access_log. You can create a project named big-game and then create three Logstores in the project to collect, store, and query the three types of logs. Log A log is the minimum data unit that is processed in Log Service. Log Service uses a semi-structured data model to define a log. The data model is as follows: Topic: a user-defined field that marks multiple logs. For example, access logs can be marked based on the sites. This field is an empty string by default. An empty string is also a valid topic. Time: a reserved field in a log, used to indicate the time when the log is generated. This value is a Unix timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. Content: a field that records the content of a log. The content consists of one or more content items. Each content item is a key-value pair. Source: a field that indicates the source of a log, for example, the IP address of the machine where the log is generated. This field is empty by default. The following table describes the requirements for the values of these fields. Log fields

| Field | Requirement |
|---|---|
| time | An integer in the Unix timestamp format. Unit: seconds. |
| topic | A UTF-8 encoded string of up to 128 characters. |
| source | A UTF-8 encoded string of up to 128 characters. |
| content | One or more key-value pairs. A key is a UTF-8 encoded string of up to 128 characters. It can contain only letters, underscores ( ), and digits. It cannot start with a digit. A value _ is a UTF-8 encoded string of up to 1,048,576 (1024 × 1024) bytes. |

|   |   | time __ __ |
|---|---|---|
| extract others _ _ _ |   |   |

> Not e The key in the content field cannot be any of the following keywords: `__time__` ,

```
 __source__ ,  __topic__ ,  __partition_time__ , and  _extract_others_   .
```

Topic Logs in a Logstore can be grouped by topics. Topics can be specified when you write logs to a Logstore. For example, you can use your user ID as the topic of a log when you write the log to a Logstore. If you do not need to group logs in a Logstore, you can specify the same topic for all logs.

> Not e An empty string is a valid topic. The topic of a log is an empty string by default.

Logs are used in various formats in actual scenarios. The following example shows how to map a raw NGINX access log to the log data model of Log Service. In this example, the IP address of your NGINX server is 10.10.10.1. A raw log on this server is as follows:

```
10.1.1.1 - - [01/Mar/2012:16:12:07 +0800] "GET /Send? AccessKeyId=<yourAccessKeyId> HTTP/1. 1" 200 5 "-" "Mozilla/5.0 (X11; Linux i686 on x86_64; rv:10.0.2) Gecko/20100101 Firefox/10. 0.2"
```

The following table describes how to map the raw log to the log data model of Log Service. Log data model of Log Service

| Field | Field value | Description |
|---|---|---|
| topic | “” | The default value (empty string) is used. |
| time | 1330589527 | The time when the log was generated. The time is converted from the timestamp of the raw log. Unit: seconds. |
| source | “10.10.10.1” | The IP address of the server is used as the log source. |
| content | Key-value pair | The content of the log. |

You can decide how to extract the raw log content and combine the extracted content into key-value pairs. The following table describes custom key-value pairs. Custom key-value pairs

| Key | Value |
|---|---|
| ip | “10.1.1.1” |
| method | “GET” |
| status | “200” |
| length | “5” |
| ref url _ | “-“ |
| browser | “Mozilla/5.0 (X11; Linux i686 on x86 64; rv:10.0.2) Gecko/20100101 Firef _ |

LogGroup A group of logs. Logs A collection of multiple logs. LogGroupList A collection of log groups that are used to return results. Encoding method The following table describes the content encoding method that is supported by Log Service. The RESTful API layer is indicated by Content-Type. Supported encoding method

| Encoding method | Content-Type | Description |
|---|---|---|
| ProtoBuf | The data model is encoded by Protocol Buffer. | application/x-protobuf |

The following sample code shows how to use Protocol Buffer to define the objects in the data model:

```
message Log
    required uint32 Time = 1;// Unix time format
    message Content
        required string Key = 1;
        required string Value = 2;
    repeated Content Contents= 2;
message LogGroup
    repeated Log Logs= 1;
    optional string Reserved = 2; // Reserved fields
    optional string Topic = 3;
    optional string Source = 4;
message LogGroupList
    repeated LogGroup logGroupList = 1;
```

> Not e When you use the Protocol Buffer format, key-value pairs must be unique. Otherwise, an undefined behavior occurs.

#### 1.12.3 Data encoding

Log Service uses Protocol Buffer as the standard log format. You can write logs to Log Service in the Protocol Buffer format. Protocol Buffer is used as a format to interchange structured data. Before you write logs to Log Service by calling relevant API operations, you must serialize raw log data to Protocol Buffer data streams as follows:

```
message Log
    required uint32 time = 1; // UNIX Time Format
    message Content
        required string key = 1;
        required string value = 2;
    repeated Content contents= 2;
message LogGroup
    repeated Log logs= 1;
    optional string reserved =2; // An internal field. You do not need to specify this fiel
```

`d.`

```
    optional string topic = 3;
    optional string source = 4;
message LogGroupList
    repeated LogGroup logGroupList = 1;
```

> Not e
> When you use the Protocol Buffer format, key-value pairs must be unique. Otherwise, an undefined behavior occurs.
> For more information about the Protocol Buffer format, visit GitHub.
> For more information about the API operations that write logs to Log Service, see PostLog.

#### 1.12.4 Logstores

A Logstore is a data storage unit. You can create up to 10 Logstores for each project by default. The name of a Logstore must be unique in the project to which the Logstore belongs. A Logstore is the portal for all log data. You can read data from or write data to the Logstore. The naming rules for Logstores are as follows: The name can only contain lowercase letters, digits, hyphens (-), and underscores (_). The name must start and end with a lowercase letter or a digit. The name must be 2 to 63 characters in length. Example

```json
    “logstoreName" : "access_log",
    "ttl": 1,
    "shardCount": 2,
    "createTime":1439538649,
    "lastModifyTime":1439538649
```

The following table describes the Logstore parameters. Logstore parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| logstoreName | String | Yes | The name of the Logstore. The name must be unique in the project to which the Logstore belongs. |
| ttl | Integer | Yes | The time to live (TTL) of log data. Unit: days. Minimum value: 1. |
| shardCount | Integer | Yes | The number of shards in the Logstore. |
| createTime | Integer | No | The time when the Logstore was created in Log Service. This parameter is displayed only in the output result. |
| lastModifyTime | Integer | No | The time when the Logstore is updated in Log Service. This parameter is displayed only in the output result. |

#### 1.12.5 Shards

A shard is a basic read/write unit in each Logstore. You can specify the number of shards in each Logstore. To read data from a shard, you must specify the shard. To write data to a shard, you do not need to specify the shard. Instead, you can use the load balancing mode. In this mode, data is written to multiple shards based on automatic balancing. This ensures high availability of the write operation. The following table describes the parameters of a shard. Shard parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| shardID | Integer | Yes | The unique ID of a shard in the Logstore. The shard ID is automatically generated by the system. |

#### 1.12.6 Logtail configurations

You can create up to 100 Logtail configurations for a project. The name of a Logtail configuration must be unique in a project. You can use a Logtail configuration to specify the location, method, and parameters for log collection. The naming rules for Logtail configurations are as follows: The name can only contain lowercase letters, digits, hyphens (-), and underscores (_). The name must start and end with a lowercase letter or a digit. The name must be 2 to 128 characters in length. Example

```json
    "configName": "testcategory1",
    "inputType": "file",
    "inputDetail": {
        "logType": "common_reg_log",
        "logPath": "/var/log/httpd/",
        "filePattern": "access.log",
        "localStorage": true,
        "timeFormat": "%Y/%m/%d %H:%M:%S",
        "logBeginRegex": ".*",
        "regex": "(\w+)(\s+)",
        "key" :[“key1", “key2"],
        "filterKey":["key1"],
        "filterRegex":[“regex1"],
        "topicFormat": “none"
```

`},`

```json
    "outputType": "sls",
    "outputDetail":
        "logstoreName": "perfcounter"
```

`},`

```json
    "createTime": 1400123456,
    "lastModifyTime": 1400123456
```

The following table describes the configuration parameters. Configuration parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| configName | String | Yes | The name of the Logtail configuration. The name must be unique in a project. |
| inputType | String | Yes | The input type. Default value: file. |
| inputDetail | json | Yes | See the following table. |
| outputType | String | Yes | The output type. Only LogService is supported. |
| outputDetail | String | Yes | See the following table. |
| createTime | Integer | No | The time when the Logtail configuration was created. |

| D | eveloper Guide·API Ref | erence |   | Log Servic | e |
|---|---|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| lastModifyTime | Integer | No | The time when the Logtail configuration was last updated on Log Service. |

The following table describes the elements of the inputDetail parameter. inputDetail elements

| Element | Type | Required | Description |   |   |
|---|---|---|---|---|---|
| logType | String | Yes | The log type. Valid value: common reg log. _ _ |   |   |
| logPath | String | Yes | The parent directory where the log resides, for example, /var/logs/ . |   |   |
| filePattern | String | Yes | The pattern of the log file, for example, access*.log . |   |   |
| localStorage | Boolean | Yes | Specifies whether to enable the local cache. Logs up to 1 GB can be locally cached when the link to Log Service is disconnected. |   |   |
| timeFormat | String | Yes | The format of the log time, for example, %Y/%m/%d %H:%M:%S . |   |   |
|   |   |   |   | %Y/%m/%d |   |
| logBeginRegex | String | Yes | The regular expression that specifies the pattern of the first line of a log. This parameter is applicable to multiline logs. |   |   |
| regex | String | Yes | The regular expression that is used to extract logs. |   |   |
| key | Array | Yes | The key that is generated after logs are extracted. |   |   |
| filterKey | Array | Yes | The key that is used to filter logs. A log meets the requirements only when the key value matches the regular expression specified in the corresponding filterRegex column. |   |   |

|   | %H:%M:%S |
|---|---|

| Element | Type | Required | Description |
|---|---|---|---|
| filterRegex | Array | Yes | The regular expression that is specified for each filterKey. The length of filterRegex must be the same as that of filterKey. |
| topicFormat | String | No | Specifies part of the log file path as the topic, for example, /var/log/(. *).log . The default value is none, indicating that the topic is null. |
| preserve | Boolean | No | Valid values: true and false. The value true indicates that the directory monitoring never times out. The value false indicates that the timeout period for directory monitoring is 30 minutes. Default value: true. |
| preserveDepth | Integer | No | Specifies the depth of the monitored directories if the preserve parameter is set to false. Maximum value: 3. |

The following table describes the elements of the outputDetail parameter. outputDetail elements

| Element | Type | Required | Description |
|---|---|---|---|
| logstoreName | String | Yes | The name of the Logstore. |

#### 1.12.7 Logtail machine group

After a machine with Logtail is started, the machine is automatically associated with the user specified in the Logtail configurations. The machine can be identified by using the following three methods: IP address: the IP address corresponding to the hostname. This is the simplest method, but the IP address may be duplicated in environments such as Virtual Private Cloud (VPC). Universally unique identifier (UUID): the UUID of the desktop management interface (DMI) device. For more information, visit RFC 4122. User-defined ID: the user-defined machine identifier in the Logtail directory. The attributes of each machine are as follows:

```json
    "ip" : "testip1",
    "machine-uniqueid" : "testuuid1",
    "userdefined-id" : "testuserdefinedid1",
    "lastHeartbeatTime”:1397781420
```

The following table describes the machine attribute parameters. Parameters

| Parameter | Type | Description |
|---|---|---|
| ip | String | The IP address corresponding to the machine hostname. |
| machine-uniqueid | String | The unique primary key marked by the machine. The primary key is uploaded by Logtail. |
| userdefined-id | String | The user-defined machine identifier that is uploaded by Logtail. |
| lastHeartbeatTime(output-only) | Integer | The last heartbeat time of the machine. The value is a Unix timestamp representing the number of seconds that have elapsed since the epoch time. |

machinegroup The machinegroup parameter indicates the machine group that belongs to the current user in the project. The machine group can be identified by an IP address or user-defined ID. IP addresses are more easily identified than user-defined IDs. However, user-defined IDs can identify machine groups in VPC even when repeated IP addresses exist. You can select either of the two machine identification methods based on your business requirements. The naming rules of machine groups are as follows: The name can contain only lowercase letters, digits, hyphens (-), and underscores (_). The name must start and end with a lowercase letter or digit. The name must be 2 to 128 characters in length. Example

```json
    "groupName" : "testgroup",
    "groupType" : "",
    "groupAttribute" : {
        "externalName" : "testgroup",
        “groupTopic”: “testgrouptopic”
```

`},`

```json
    “machineIdentifyType”: "ip",
    "machineList" : [
        "ip1",
        "ip2"
        ...
```

`],`

```json
    “createTime”: 1431705075,
    "lastModifyTime" : 1431705075
```

The following table lists the parameters of a machine group. Machine group parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| groupName | String | Yes | The name of the machine group. The name must be unique in a project. |
| groupType | String | No | The type of the machine group. Default value: null. |
| machineIdentifyType | String | Yes | The machine identification type. Valid values: ip or userdefined-id. |
| groupAttribute | object | Yes | The attribute of the machine group. Default value: null. |
| machineList | Array | Yes | The list of machine identifiers. Valid values: IP addresses or user-defined identifiers. |
| createTime(output- only) | Integer | No | The time when the machine group was created. |
| lastModifyTime(outp ut-only) | Integer | No | The time when the machine group was last updated on Log Service. |

The following table describes the parameters of groupAttribute. groupAttribute parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| groupTopic | String | No | The topic of the machine group. Default value: null. |
| externalName | String | No | The external management identifier on which the machine group depends. Default value: null. |

## 2 SDK Reference

### 2.1 Introduction

#### 2.1.1 Overview

Log Service provide software development kits (SDKs) for multiple languages, such as Java, .NET, Python, PHP, and C. You can select an SDK based on your business requirements. Log Service SDKs are implemented based on Log Service APIs. Log Service SDKs provide the same capabilities as Log Service APIs. For more information about Log Service APIs, see API Reference. Before you can use a Log Service SDK, you must have an active Alibaba Cloud AccessKey pair (AccessKey ID and AccessKey secret). In addition, you must specify the endpoint of Log Service in the SDK. For more information, see Basic configurations. Log Service SDKs can be regarded as Log Service APIs that are encapsulated in different languages to provide the following features: Uniform encapsulation. Log Service APIs are uniformly encapsulated. You do not need to create API requests and parse API responses. For more information, see API specifications. The APIs in different languages are similar. This simplifies the switchover between different languages. Automatic digital signatures. You do not need to specify the digital signature logic of Log Service APIs. This simplifies the use of Log Service APIs. Protocol Buffer-formatted encapsulation. The logs collected by Log Service are encapsulated in the Protocol Buffer format. You do not need to specify the format. Automatic compression. Logs are compressed by using the method defined in Log Service APIs. You do not need to manually compress logs. SDKs in some languages allow you to specify whether to write logs in the compression mode. The compression mode is used by default. Centralized error handling methods. You can use SDKs to handle errors based on the relevant language. For more information, see Error handling. Synchronous requests. SDKs in all languages support only synchronous requests. The following table describes the download address and user guide of Log Service SDKs in different languages.

| SDK language | Documentation | Source code |
|---|---|---|
| Java | SDK for Java and Log Service SDK for Java 0.6.0 API | GitHub |
| .NET | SDK for .NET and Aliyun.Api.SLS Namespace | GitHub |
| PHP | SDK for PHP and SLS PHP SDK _ _ | GitHub |
| Node.js | SDK for Node.js | GitHub |
| Python | SDK for Python and Python documentation | GitHub |
| C | SDK for C | GitHub |

| Developer Guide·SDK Re | ference | Log Servic |
|---|---|---|

| SDK language | Documentation | Source code |
|---|---|---|
| GO | SDK for Go | GitHub |
| iOS | SDK for iOS | GitHub |
| Android | SDK for Android | GitHub |
| C++ | SDK for C ++ | GitHub |

#### 2.1.2 Basic configurations

Before you can use SDKs to interact with Log Service, you must configure the basic settings. This topic describes the basic SDK configurations. Basic configurations: Endpoint: You must specify the endpoint that is used by the client to access Log Service. AccessKey pair (AccessKey ID and AccessKey secret): You must specify the AccessKey pair that is used by the client to access Log Service. The following sections describe how to use endpoints and AccessKey pairs. Endpoint Before you use an SDK, you must determine the access method and endpoint.
1. When you select an endpoint for a client instance, make sure that the region of your project is the
same as the region of your endpoint. Otherwise, you cannot use the SDK to access your project.
2. All API endpoints support only the HTTP protocol.
AccessKey pairs All interaction requests that are sent to Log Service must be authenticated. An AccessKey pair that consists of an AccessKey ID and AccessKey secret is the critical factor for the authentication. When you create a client instance, you must specify an AccessKey ID and AccessKey secret. You must obtain an AccessKey pair in the Apsara Uni-manager Management Console.

> Not e
> An Apsara Stack tenant account can have multiple AccessKey pairs. You must specify the AccessKey ID and AccessKey secret of the same AccessKey pair when you create a client instance. Otherwise, authentication fails.
> The specified AccessKey must be in the Enabled state. Otherwise, the requests are denied by Log Service. To view the status of the AccessKey pair, you can log on to the Apsara Uni- manager Management Console.

Examples Assume that you want to access a project and you have an AccessKey pair that is in the Enabled state. The following AccessKey pair is used:

```
AccessKeyId = "<yourAccessKeyId>" AccessKeySecret = "<yourAccessKeySecret>"
```

You can use the following snippets to create a client instance based on the language: Java

```
String endpoint = "regionid.example.com"; // Specify the endpoint based on your region an d access method. String accessKeyId = "<youraccessKeyId>"; // Specify your AccessKey ID. String accessKeySecret = "<youraccessKeySecret>"; // Specify your AccessKey secret. Client client = new Client(endpoint, accessKeyId, acccessKeySecret); //use client to operate log service project......
```

.NET(C#)

```
String endpoint = "regionid.example.com"; // Specify the endpoint based on your region an d access method. String accessKeyId = "<youraccessKeyId>"; // Specify your AccessKey ID. String accessKeySecret = "<youraccessKeySecret>"; // Specify your AccessKey secret. SLSClient client = new SLSClient(endpoint, accessKeyId, accessKeySecret); //use client to operate sls project......
```

PHP

```
$endpoint = 'regionid.example.com'; // The endpoint of the China (Hangzhou) region is use d as an example. Replace it with the actual endpoint based on your region and access meth od. $accessKeyId = '<youraccessKeyId>'; // Specify your AccessKey ID. $accessKey = '<youraccessKey>'; // Specify your AccessKey secret. $client = new Aliyun_Sls_Client($endpoint, $accessKeyId, $accessKey); //use client to operate sls project......
```

Python

```bash
# // Specify the endpoint based on your region and access method.
endpoint = 'regionid.example.com'
# Specify your AccessKey ID.
accessKeyId = '<youraccessKeyId>'
# Specify your AccessKey secret.
accessKey = '<youraccessKey>' client = LogClient(endpoint, accessKeyId, accessKey)
#use client to operate log project......
```

#### 2.1.3 Error handling

SDK errors are divided into the following types: Errors returned by Log Service. Errors of this type are handled by SDKs. For more information about this error type, see the common error codes of the Log Service API operations. Network errors that occur when you send requests to the server by using SDKs. This type of errors include network disconnection and server response timeout. Errors that are generated by SDKs and related to platforms or languages, for example, memory overflows. All SDKs provided by Alibaba Cloud handle errors by throwing exceptions based on the following principles: The first and second types of errors are encapsulated as the LogException class and sent to users by SDKs. The third type of errors are not handled by SDKs, but are sent to users as the platform-specific and language-specific NativeException class. LogException The LogException class is defined by SDKs to handle the logical errors of Log Service. This class inherits the base class for all exceptions from each language, and provides the following exception information: Error code: indicates the error type. For an error returned by Log Service when you use an SDK, the error code is the same as that returned by the relevant API operation. The error code of SDK network request errors is RequestError. For more information, see API Reference. Error message: indicates the message that is returned together with an error. For an error returned by Log Service when you use an SDK, the error message is the same as that returned by the relevant API operation. The error message of network errors is "request is failed". For more information, see the relevant API reference. Request ID: indicates the ID of the request for which the current error is returned. The request ID is generated by Log Service. This ID is returned only when an error message is returned by Log Service. Otherwise, an empty string is returned. If you receives a request error, you can provide the relevant request ID to the Log Service team for troubleshooting. Request failures and retries When you use an SDK to access Log Service, the access request may fail due to temporary network disconnection, transmission delay, and slow server response. These errors are sent as exceptions. Log Service does not implement retry logic. When you use the SDK, you must customize the handling logic, for example, retry the request or report an error. Examples For example, you want to access a project named big-game and retry the access request for a specified number of times in the case of network exceptions. You can use the following snippets based on the language: Java

```
// Other code... String accessId = "<youraccessId>"; // Specify your AccessKey ID. String accessKey = "<youraccessKey>"; // Specify your AccessKey secret. String project = "big-game"; String endpoint = "regionid.example.com"; int max_retries = 3;
```

`/*`

```
 * Create a client.
```

`*/`

```java
Client client = new Client(accessId, accessKey, endpoint); ListLogStoresRequest lsRequest = new ListLogStoresRequest(project); for (int i = 0; i < max_retries; i++)
    try
        ListLogStoresResponse res = client.ListLogStores(lsRequest)
        // Process the returned data...
        break;
    catch(LogException ex)
        if (e.GetErrorCode() == "RequestError")
            if ( i == max_retries - 1)
                System.out.println("request is still failed after all retries.");
                break;
            else
                System.out.println("request error happens, retry it!") ;
        else
            System.out.println("error code :" + e.GetErrorCode());
            System.out.println("error message :" + e.GetErrorMessage());
            System.out.println("error requestId :" + e.GetRequestId());
            break;
    catch(...)
        System.out.println("unrecoverable exception when listing logstores.");
        break;
// Other code...
```

.NET(C#):

```
// Other code... String accessId = "<youraccessId>"; // Specify your AccessKey ID. String accessKey = "<youraccessKey>"; // Specify your AccessKey secret. String project = "big-game"; String endpoint = "regionid.example.com"; int max_retries = 3; // Create a client. SLSClient client = new SLSClient(endpoint, accessId, accessKey); ListLogstoresRequest request = new ListLogstoresRequest(); request.Project = project; for (int i = 0; i < max_retries; i++)
    try
        ListLogstoresResponse response = client.ListLogstores(request);
        // Process the returned data...
        break;
    catch(LogException ex)
        if (e.errorCode == "SLSRequestError")
            if ( i == max_retries - 1)
                Console.Writeline(“request is still failed after all retries.”);
                break;
            else
                Console.Writeline("request error happens, retry it!") ;
        else
            Console.Writeline("error code :" + e.errorCode;
            Console.Writeline("error message :" + e.Message;
            Console.Writeline("error requestId :" + e.RequestId;
            break;
    catch(...)
        Console.Writeline("unrecoverable exception when listing logstores.");
        break;
// Other code...
```

PHP

```
<? php // Other code... $endpoint = 'regionid.example.com'; $accessId = '<youraccessId>'; // Specify your AccessKey ID. $accessKey = '<youraccessKey>'; // Specify your AccessKey secret. $maxRetries = 3; // Create a Log Service client. $client = new Aliyun_Sls_Client($endpoint, $accessId, $accessKey); $project = 'big-game'; $request = new Aliyun_Sls_Models_ListLogstoresRequest($project); for($i = 0; $i < $maxRetries; ++$i)
    try
        $response = $client->ListLogstores($request);
        // Process the returned data...
        break;
    catch (Aliyun_Sls_Exception $e)
        if ($e->getErrorCode()=='RequestError')
            if ($i+1 == $maxRetries)
                echo "error code :" . $e->getErrorCode() . PHP_EOL;
                echo "error message :" . $e->getErrorMessage() . PHP_EOL;
                break;
            echo 'request error happens, retry it!' . PHP_EOL;
        else
            echo "error code :" . $e->getErrorCode() . PHP_EOL;
            echo "error message :" . $e->getErrorMessage() . PHP_EOL;
            echo "error requestId :" . $e->getRequestId() . PHP_EOL;
            break;
    catch (Exception $ex)
        echo 'unrecoverable exception when listing logstores.' . PHP_EOL;
        var_dump($ex);
        break;
// Other code...
```

Python

```bash
// Other code... endpoint = 'regionid.example.com' accessId = '<youraccessId>' # Specify your AccessKey ID. accessKey = '<youraccessKey>' # Specify your AccessKey secret. maxRetries = 3
# Create a client.
client = Client(endpoint, accessId, accessKey) project = 'big-game' lsRequest = ListLogstoresRequest(project) for i in xrange(maxRetries):
    try:
        res = client.ListLogstores(lsRequest)
        # Process the returned data...
        break
    except LogException as e:
        if e.getErrorCode() == "RequestError":
            if i+1 == maxRetries:
                print "error code :" + e.getErrorCode()
                print "error message :" + e.getErrorMessage()
                break
            else:
                print "request error happens, retry it!"
        else:
            print "error code :" + e.getErrorCode()
            print "error message :" + e.getErrorMessage()
            print "error requestId :" + e.getRequestId()
            break
    except Exception as e:
        print 'unrecoverable exception when listing logstores.'
        break
// Other code...
```

#### 2.1.4 API specifications

SDKs in different languages are implemented in different methods. However, all relevant API operations comply with the request-response principle. These API operations are called by using the following procedure:
1. Create a request instance by using request parameters.
2. Call the corresponding API operation in the SDK and pass the API information to the request
instance.
3. Encapsulate the results returned by the SDK interface into a response instance and then return the
response instance to the user. The following snippets show how to obtain the names of all Logstores in a project based on the preceding steps. Java

```
// Other code... String accessId = "<youraccessId>"; // Specify your AccessKey ID. String accessKey = "<youraccessKey>"; // Specify your AccessKey secret. String project = "your_project"; // Specify your project name. String endpoint = "region_endpoint";// The China (Hangzhou) region is used as an example. S pecify the endpoint based on your region and access method. // Create a client instance. Client client = new Client(endpoint, accessId, accessKey); // Specify the project request parameter to initialize the ListLogstores request class. ListLogStoresRequest lsRequest = new ListLogStoresRequest(project); // Use the request instance to call the ListLogstores API operation. The returned parameter is the corresponding response instance. ListLogStoresResponse res = client.ListLogStores(lsRequest); // Access the response instance to retrieve the request results. ArrayList<String> names = res.GetLogStores(); // Other code...
```

.NET(C#)

```
// Other code... String accessId = "<youraccessId>"; // Specify your AccessKey ID. String accessKey = "<youraccessKey>"; // Specify your AccessKey secret. String project = "your_project"; // Specify your project name. String endpoint = "region_endpoint";// The China (Hangzhou) region is used as an example. S pecify the endpoint based on your region and access method. // Create a client instance. SLSClient client = new SLSClient(endpoint, accessId, accessKey); // Specify the project request parameter to initialize the ListLogstores request class. ListLogStoresRequest lsRequest = new ListLogStoresRequest(); lsRequest.Project = project; // Use the request instance to call the ListLogstores API operation. The returned parameter is the corresponding response instance. ListLogStoresResponse res = client.ListLogStores(lsRequest); // Access the response instance to retrieve the request results. List<String> names = res.Logstores; // Other code...
```

PHP

```
// Other code... $accessId = "<youraccessId>"; // Specify your AccessKey ID. $accessKey = "<youraccessKey>"; // Specify your AccessKey secret. $project = "your_project"; // Specify your project name. $endpoint = "region_endpoint";// The China (Hangzhou) region is used as an example. Specify the endpoint based on your region and access method. //Create a Log Service client instance. $client = new Aliyun_Sls_Client($endpoint, $accessId, $accessKey); // Specify the project request parameter to initialize the ListLogstores request class. $request = new Aliyun_Sls_Models_ListLogstoresRequest($project); // Use the request instance to call the ListLogstores API operation. The returned parameter is the corresponding response instance. $response = $client->listLogstores($request); // Access the response instance to retrieve the request results. $names = $response->getLogstores(); // Other code...
```

Python

```bash
// Other code... accessId = '<youraccessId>'; // Specify your AccessKey ID. accessKey = '<youraccessKey>'; // Specify your AccessKey secret. project = 'your_project'; // Specify your project name. endpoint = 'region_endpoint';// The China (Hangzhou) region is used as an example. Specify the endpoint based on your region and access method.
# Create a client instance.
client = LogClient(endpoint, accessId, accessKey)
# Specify the project request parameter to initialize the ListLogstores request class.
lsRequest = ListLogstoresRequest(project)
# Use the request instance to call the ListLogstores API operation. The returned parameter
is the corresponding response instance. res = client.list_logstores(lsRequest)
# Access the response instance to retrieve the request results.
names = res.get_logstores(); // Other code...
```

The Log Service SDKs implement multiple API operations such as ListLogStores, and define the corresponding request and response classes. The Log Service SDKs of different languages also provide secondary APIs encapsulated with these basic request-response APIs. You do not need to create request instances or parse the content of the response. For more information about the secondary interfaces, see the API reference of each SDK.

### 2.2 Java SDK

Log Service SDK for Java allows Java developers to perform operations in Log Service by using Java programs. You can use Maven dependencies to add the SDK. You can also download the SDK package to an on-premises server. Download URL Log Service SDK for Java supports J2SE V6.0 and later. Click here to download the latest SDK. Step 1: Create an Apsara Stack tenant account To access Log Service, you must create an account in the Apsara Uni-manager Management Console. Step 2: Obtain an Apsara Stack AccessKey pair To use Log Service SDK for Java, you must obtain an AccessKey pair. Log on to the Apsara Uni-manager Management Console. Select an AccessKey pair for the SDK. The AccessKey pair will be used in the following steps and must be kept confidential. For information about how to use an AccessKey pair in Log Service SDK for Java, see Basic configurations. Step 3: Create a project and a Logstore in the Log Service console Use Log Service SDK for Java to create a project and a Logstore.

> Not e
> The account that you use to create the project and the Logstore must be the same as the account that you used to obtain the AccessKey pair.
> The project name must be unique in Log Service. The Logstore name must be unique in the project.
> After you create the project, you cannot modify its region or migrate the project across regions.

Step 4: Install a Java development environment Log Service SDK for Java supports Java development environment J2SE V6.0 and later. You can visit the Java official website to download and install the Java development environment. Step 5: Install Log Service SDK for Java After you install the Java development environment, you must install Log Service SDK for Java. To install Log Service SDK for Java, use one of the following methods: Download the latest SDK for Java package from Apache Maven. Add the following configurations to your Maven project:

```xml
<dependency>
         <groupId>com.google.protobuf</groupId>
         <artifactId>protobuf-java</artifactId>
         <version>2.5.0</version>
</dependency> <dependency> <groupId>com.aliyun.openservices</groupId> <artifactId>aliyun-log</artifactId> <version>0.6.7</version> <exclusions>
        <exclusion>
            <groupId>com.google.protobuf</groupId>
            <artifactId>protobuf-java</artifactId>
       </exclusion>
</exclusions> </dependency>
```

Download Log Service SDK for Java package, and then reference the local package in your Java project.
1. Download Log Service SDK for Java package. Log Service SDK for Java is periodically updated. You
can use Maven to obtain the latest version.
2. Decompress the downloaded package to a specified directory. Log Service SDK for Java does not
require installation.
3. Add all JAR packages (including third-party dependent packages) in the SDK package to your Java
project. For more information, see the relevant documents about integrated development environment (IDE). Step 6: Start a new Java project The following sample code shows how to use Log Service SDK for Java. To interact with Log Service and obtain the relevant output, run the following sample code in a text editor or Java IDE:

```java
package sdksample; import java.util.ArrayList; import java.util.List; import java.util.Vector; import java.util.Date; import com.aliyun.openservices.log.Client; import com.aliyun.openservices.log.common.*; import com.aliyun.openservices.log.exception.*; import com.aliyun.openservices.log.request.*; import com.aliyun.openservices.log.response.*; import com.aliyun.openservices.log.common.LogGroupData; import com.aliyun.openservices.log.common.LogItem; import com.aliyun.openservices.log.common.Logs.Log; import com.aliyun.openservices.log.common.Logs.Log.Content; import com.aliyun.openservices.log.common.Logs.LogGroup; import com.aliyun.openservices.log.common.Consts.CursorMode; public class sdksample {
    public static void main(String args[]) throws LogException, InterruptedException {
        String endpoint = "<log_service_endpoint>"; // Select the endpoint that matches the
region of the project created in the preceding steps.
        // Endpoint
        String accessKeyId = "<youraccessKeyId>"; // Use your AccessKey ID.
        String accessKeySecret = "<youraccessKeySecret>"; // Use your AccessKey secret.
        // AccessKeySecret
        String project = "<project_name>"; // The name of the project created in the preced
ing steps.
        String logstore = "<logstore_name>"; // The name of the Logstore created in the pre
ceding steps.
        // Create a client instance.
        Client client = new Client(endpoint, accessKeyId, accessKeySecret);
        // List all Logstores in the current project.
        int offset = 0;
        int size = 100;
        String logStoreSubName = "";
        ListLogStoresRequest req1 = new ListLogStoresRequest(project, offset, size, logStor
eSubName);
        ArrayList<String> logStores = client.ListLogStores(req1).GetLogStores();
        System.out.println("ListLogs:" + logStores.toString() + "\n");
        // Write logs.
```

```
        String topic = "";
        String source = "";
        // Send 10 packets. Each packet contains 10 log entries.
        for (int i = 0; i < 10; i++) {
            Vector<LogItem> logGroup = new Vector<LogItem>();
            for (int j = 0; j < 10; j++) {
                LogItem logItem = new LogItem((int) (new Date().getTime() / 1000));
                logItem.PushBack("index"+String.valueOf(j), String.valueOf(i * 10 + j));
                logGroup.add(logItem);
            PutLogsRequest req2 = new PutLogsRequest(project, logstore, topic, source, logG
roup);
            client.PutLogs(req2);
```

`/*`

```
             * You can specify a shard to which data is sent.
             * After you set a hash key, data is written to the shard whose MD5 value range
includes the hash key. For more information, see the API operation PutLogsResponse.
             * PutLogs( String project, String logStore, String topic,
             * List<LogItem> logItems, String source, String shardHash //
             * Write data to the shard based on the hash key, which can be MD5(ip) or MD5(i
d).
```

`*/`

```java
        // Read the data that was written to shard 0 in the last minute.
        int shard_id = 0;
        long curTimeInSec = System.currentTimeMillis() / 1000;
        GetCursorResponse cursorRes = client.GetCursor(project, logstore, shard_id, curTime
InSec - 60);
        String beginCursor = cursorRes.GetCursor();
        cursorRes = client.GetCursor(project, logstore, shard_id, CursorMode.END);
        String endCursor = cursorRes.GetCursor();
        String curCursor = beginCursor;
        while (curCursor.equals(endCursor) == false) {
            int loggroup_count = 2; // Read two log groups at a time.
            BatchGetLogResponse logDataRes = client.BatchGetLog(project, logstore, shard_id
, loggroup_count, curCursor,
                    endCursor);
            // Read the log group list.
            List<LogGroupData> logGroups = logDataRes.GetLogGroups();
            for(LogGroupData logGroup: logGroups){
                FastLogGroup flg = logGroup.GetFastLogGroup();
                System.out.println(String.format("\tcategory\t:\t%s\n\tsource\t:\t%s\n\ttop
ic\t:\t%s\n\tmachineUUID\t:\t%s",
                        flg.getCategory(), flg.getSource(), flg.getTopic(), flg.getMachineU
UID()));
                System.out.println("Tags");
                for (int tagIdx = 0; tagIdx < flg.getLogTagsCount(); ++tagIdx) {
                    FastLogTag logtag = flg.getLogTags(tagIdx);
                    System.out.println(String.format("\t%s\t:\t%s", logtag.getKey(), logtag
.getValue()));
                for (int lIdx = 0; lIdx < flg.getLogsCount(); ++lIdx) {
                    FastLog log = flg.getLogs(lIdx);
                    System.out.println("--------\nLog: " + lIdx + ", time: " + log.getTime(
```

```java
) + ", GetContentCount: " + log.getContentsCount());
                    for (int cIdx = 0; cIdx < log.getContentsCount(); ++cIdx) {
                        FastLogContent content = log.getContents(cIdx);
                        System.out.println(content.getKey() + "\t:\t" + content.getValue())
```

;

```java
            String next_cursor = logDataRes.GetNextCursor();
            System.out.println("The Next cursor:" + next_cursor);
            curCursor = next_cursor;
        // Note: You can call the following API operation only after you enable the indexin
g feature.
        // Before you query logs, wait for 1 minute.
        try {
            Thread.sleep(60 * 1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        // Query the distribution of logs.
        String query = "<Specify the query keyword. To query all contents, use an empty str
ing.>";
        int from = (int) (new Date().getTime() / 1000 - 300);
        int to = (int) (new Date().getTime() / 1000);
        GetHistogramsResponse res3 = null;
        while (true) {
            GetHistogramsRequest req3 = new GetHistogramsRequest(project, logstore, topic,
query, from, to);
            res3 = client.GetHistograms(req3);
            if (res3 ! = null && res3.IsCompleted()) // IsCompleted()
            // If "true" is returned, the query result is accurate.
            // If "false" is returned, the query is repeated.
                break;
            Thread.sleep(200);
        System.out.println("Total count of logs is " + res3.GetTotalCount());
        for (Histogram ht : res3.GetHistograms()) {
            System.out.printf("from %d, to %d, count %d.\n", ht.GetFrom(), ht.GetTo(), ht.G
etCount());
        // Query log data.
        long total_log_lines = res3.GetTotalCount();
        int log_offset = 0;
        int log_line = 10;
        while (log_offset <= total_log_lines) {
            GetLogsResponse res4 = null;
            // For each log offset, 10 lines are read at a time. If a read operation fails,
a maximum of three retries are allowed.
            for (int retry_time = 0; retry_time < 3; retry_time++) {
                GetLogsRequest req4 = new GetLogsRequest(project, logstore, from, to, topic
, query, log_offset, logline false);
```

```java
                        log_line, false);
                res4 = client.GetLogs(req4);
                if (res4 ! = null && res4.IsCompleted()) {
                    break;
                Thread.sleep(200);
            System.out.println("Read log count:" + String.valueOf(res4.GetCount()));
            log_offset += log_line;
        // Enable the analytics feature. You can use SQL statements only after you enable t
he analytics feature. You can log on to the Log Service console or use the SDK to enable th e analytics feature.
        IndexKeys indexKeys = new IndexKeys();
        ArrayList<String> tokens = new ArrayList<String>();
        tokens.add(",");
        tokens.add(".");
        tokens.add("#");
        IndexKey keyContent = new IndexKey(tokens,false,"text");
        indexKeys.AddKey("index0",keyContent);
        keyContent = new IndexKey(new ArrayList<String>(),false,"long");
        indexKeys.AddKey("index1",keyContent);
        keyContent = new IndexKey(new ArrayList<String>(),false,"double");
        indexKeys.AddKey("index2",keyContent);
        IndexLine indexLine = new IndexLine(new ArrayList<String>(),false);
        Index index = new Index(7,indexKeys,indexLine);
        CreateIndexRequest createIndexRequest = new CreateIndexRequest(project,logstore,ind
ex);
        client.CreateIndex(createIndexRequest);
        // Use the analytics feature.
        GetLogsRequest req4 = new GetLogsRequest(project, logstore, from, to, "", " index0:
value | select avg(index1) as v1,sum(index2) as v2, index0 group by index0");
        GetLogsResponse res4 = client.GetLogs(req4);
        if(res4 ! = null && res4.IsCompleted()){
            for (QueriedLog log : res4.GetLogs()){
                LogItem item = log.GetLogItem();
                for(LogContent content : item.GetLogContents()){
                    System.out.print(content.GetKey()+":"+content.GetValue());
                System.out.println();
```

Usage notes To improve the I/O efficiency of your system, we recommend that you do not use SDKs to write data to Log Service. For information about the recommended data writing methods, see the "Producer Library" section in User Guide. Producer Library To call API operations for data consumption in Log Service, we recommend that you do not use SDKs. Log Service provides an advanced consumer library. The consumer library consumes data in a manner that is transparent to the user, and provides advanced features such as load balancing and sequential consumption. For more information, see Consumer Library in User Guide. Consumer Library

### 2.3. .NET SDK

Log Service provides developers with Log Service SDK for .NET to simplify the use of Log Service. Download URL Log Service SDK for .NET allows developers on Windows to use Log Service on the .NET platform. Log Service SDK for .NET supports .NET Framework 3.5, .NET Framework 4.0, and .NET Framework 4.5. Even though different SDK files are used for different .NET Framework versions, the APIs and features of these versions are the same. The download URL of Log Service SDK for .NET is GitHub. Step 1: Create an Apsara Stack tenant account To access Log Service, you must create an account in the Apsara Uni-manager Management Console. Step 2: Obtain an AccessKey pair To use Log Service SDK for .NET, you must obtain an AccessKey pair. Log on to the Apsara Uni-manager Management Console and select an AccessKey pair for the SDK. The AccessKey pair will be used in the following steps and must be kept confidential. For information about how to use an AccessKey pair in Log Service SDK for .NET, see Basic configurations. Step 3: Create a project and a Logstore in the Log Service console Use Log Service SDK for .NET to create a project and a Logstore.

> Not e

The account that you use to create the project and the Logstore must be the same as the account that you used to obtain the AccessKey pair. The project name must be unique in Log Service. The Logstore name must be unique in the project. After you create the project, you cannot modify its region or migrate the project across regions. Step 4: Install a .NET development environment Log Service SDK for .NET supports the .NET Framework 3.5, .NET Framework 4.0, and .NET Framework 4.5 development environments. We recommend that you install one of the following .NET development environments: Microsoft .NET Framework 3.5, Microsoft .NET Framework 4.0, or Microsoft .NET Framework 4.5 (based on your environment) Visual Studio 2010 or later Step 5: Download and install Log Service SDK for .NET After you build a .NET development environment, you must install Log Service SDK for .NET. To install Log Service SDK for .NET, perform the following steps:
1. Download Log Service SDK for .NET.
Download Log Service SDK for .NET from GitHub. Click here to download the latest Log Service SDK for .NET package.
2. Decompress the downloaded package to a specified directory. Log Service SDK for .NET does not
require installation. The following step describes how to use the SDK in your Visual Studio project. Step 6: Create a Log Service .NET project After you install the .NET development environment and Log Service SDK for .NET, you can create a Log Service .NET project. For more information, see the LOG SDK Sample project in the SLS SDK 40 solution at GitHub.

### 2.4. .NET Core SDK

Context Log Service SDK for .NET Core allows developers to use Log Service by using the .NET Core framework. The download URL of Log Service SDK for .NET Core is GitHub. Procedure
1. Create an Apsara Stack tenant account.
To access Log Service, you must create an account in the Apsara Uni-manager Management Console.
2. Obtain an Apsara Stack AccessKey pair.
To use Log Service SDK for .NET Core, you must obtain an Apsara Stack AccessKey pair. Log on to the Apsara Uni-manager Management Console and select an AccessKey pair for the SDK. The AccessKey pair will be used in the following steps and must be kept confidential. For information about how to use the AccessKey pair in Log Service SDK for .NET Core, see Basic configurations.
3. Create a project and a Logstore.
Before you can use the SDK, you must create a project and a Logstore in the Log Service console. i. Log on to the Log Service console. ii. In the Projects section, click Creat e Project . iii. Enter a Project Name, select a Region, and then click OK. iv. In the Project s section, click the name of the project. On the page that appears, click the plus sign (+) in the left-side navigation pane. You can also click Creat e to create a Logstore as prompted after you create a project. v. In the dialog box that appears, set the required parameters, and then click OK. You must specify the Logstore name, data retention period, and number of shards. Set the number of shards based on your business requirements. In this example, four shards are created.

> Not e
> The account that you use to create the project and the Logstore must be the same as the account that you used to obtain the AccessKey pair.
> The project name must be unique in Log Service. The Logstore name must be unique in the project.
> After you create the project, you cannot modify its region or migrate the project across regions.

4. Install the .NET Core development environment.
Log Service SDK for .NET Core supports the following versions: .NET Core 2.0 .NET Framework (with .NET Core 1.x SDK) 4.6.2 .NET Framework (with .NET Core 2.0 SDK) 4.6.1 For more information about all supported versions, visit GitHub.
5. Download and install Log Service SDK for .NET Core.
After you build the .NET Core development environment, you must install Log Service SDK for .NET Core. i. Download Log Service SDK for .NET Core. Click here to download Log Service SDK for .NET Core from GitHub. ii. Decompress the downloaded package to a specified directory. Log Service SDK for .NET Core does not require installation. You can use Log Service SDK for .NET Core for your Visual Studio project.
6. Create a Log Service .NET Core project.
After you install the .NET Core development environment and Log Service SDK for .NET Core, you can create a .NET Core project. For more information, visit GitHub Wiki.

### 2.5 PHP SDK

Log Service provides developers with Log Service SDK for PHP to simplify the use of Log Service. Download URL You can download Log Service SDK for PHP from GitHub: Step 1: Create an Apsara Stack tenant account To access Log Service, you must create an account in the Apsara Uni-manager Management Console. Step 2: Obtain an Apsara Stack AccessKey pair To use Log Service SDK for PHP, you must obtain an AccessKey pair. Log on to the Apsara Uni-manager Management Console. Select an AccessKey pair for the SDK. The AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey pair will be used in the following steps and must be kept confidential. For information about how to use an AccessKey pair in Log Service SDK for PHP, see Basic configurations. Step 3: Create a project and a Logstore in the Log Service console Use Log Service SDK for PHP to create a project and a Logstore.

> Not e

The account that you use to create the project and the Logstore must be the same as the account that you used to obtain the AccessKey pair. The project name must be unique in Log Service. The Logstore name must be unique in the project. After you create the project, you cannot modify its region or migrate the project across regions. Step 4: Install a PHP development environment Log Service SDK for PHP supports PHP V5.2.1 and later. You can install a supported PHP on an onpremises server and build a PHP development environment. Step 5: Download and install Log Service SDK for PHP After you build a PHP development environment, you must install Log Service SDK for PHP. To install Log Service SDK for PHP, perform the following steps:
1. Download the latest SDK for PHP package from GitHub.
2. Decompress the downloaded package to a specified directory. Log Service SDK for PHP does not
require installation. Log Service SDK for PHP includes the SDK code, third-party dependent packages, and an autoloader to simplify the use of the SDK. The following step describes how to use the SDK in your PHP project. Step 6: Create a PHP project To interact with Log Service and obtain the output, you can run the following sample code in a text editor or the PHP integrated development environment (IDE):

```bash
<? php /* Use the autoloader to load all required PHP modules. Specify the path of the file that c ontains the autoloader. */ require_once realpath(dirname(__FILE__) . '/.. /Log_Autoload.php'); $endpoint = 'regionid.example.com'; // The endpoint of the China (Hangzhou) region is used as an example. Replace it with the actual endpoint based on your region and access method. $accessKeyId = '<youraccessKeyId>'; // Specify your AccessKey ID. $accessKey = '<youraccessKey>'; // Specify your AccessKey secret. $project = 'your_project'; // The name of the project created in the preceding steps. $logstore = 'your_logstore'; // The name of the Logstore created in the preceding steps. $client = new Aliyun_Log_Client($endpoint, $accessKeyId, $accessKey);
# List all Logstores in the current project.
$req1 = new Aliyun_Log_Models_ListLogstoresRequest($project); $res1 = $client->listLogstores($req1); var_dump($res1);
# Create a Logstore.
$req2 = new Aliyun_Log_Models_CreateLogstoreRequest($project,$logstore,3,2); $res2 = $client -> createLogstore($req2);
# Wait until the Logstore takes effect.
```

`l`

```
(60)
```

```python
sleep(60);
# Write logs.
$topic = ""; $source = ""; $logitems = array(); for ($i = 0; $i < 5; $i++)
    $contents = array('index1'=> strval($i));
    $logItem = new Aliyun_Log_Models_LogItem();
    $logItem->setTime(time());
    $logItem->setContents($contents);
    array_push($logitems, $logItem);
$req2 = new Aliyun_Log_Models_PutLogsRequest($project, $logstore, $topic, $source, $logitem s); $res2 = $client->putLogs($req2); var_dump($res2);
# Pull the data.
# List the shard IDs in the Logstore.
$listShardRequest = new Aliyun_Log_Models_ListShardsRequest($project,$logstore); $listShardResponse = $client -> listShards($listShardRequest); foreach($listShardResponse-> getShardIds() as $shardId)
    # Obtain the cursor that corresponds to each shard ID.
    $getCursorRequest = new Aliyun_Log_Models_GetCursorRequest($project,$logstore,$shardId,
null, time() - 60);
    $response = $client -> getCursor($getCursorRequest);
    $cursor = $response-> getCursor();
    $count = 100;
    while(true)
        # Start to read data from a cursor.
        $batchGetDataRequest = new Aliyun_Log_Models_BatchGetLogsRequest($project,$logstore
,$shardId,$count,$cursor);
        var_dump($batchGetDataRequest);
        $response = $client -> batchGetLogs($batchGetDataRequest);
        if($cursor == $response -> getNextCursor())
            break;
        $logGroupList = $response -> getLogGroupList();
        foreach($logGroupList as $logGroup)
            print ($logGroup->getCategory());
            foreach($logGroup -> getLogsArray() as $log)
                foreach($log -> getContentsArray() as $content)
                    print($content-> getKey().":".$content->getValue()."\t");
                print("\n");
        $cursor = $response -> getNextCursor();
```

```bash
# Before you query logs, wait for 1 minute.
sleep(60);
# Query the distribution of logs. Before you query logs, you must ensure that indexes are c
reated. Log Service SDK for PHP does not provide the API operation that you can call to cre ate indexes. You must create indexes in the Log Service console. $topic = ""; $query=''; $from = time()-3600; $to = time(); $res3 = NULL; while (is_null($res3) || (! $res3->isCompleted()))
    $req3 = new Aliyun_Log_Models_GetHistogramsRequest($project, $logstore, $from, $to, $to
pic, $query);
    $res3 = $client->getHistograms($req3);
var_dump($res3);
# Query log data.
$res4 = NULL; while (is_null($res4) || (! $res4->isCompleted()))
    $req4 = new Aliyun_Log_Models_GetLogsRequest($project, $logstore, $from, $to, $topic, $
query, 5, 0, False);
    $res4 = $client->getLogs($req4);
var_dump($res4);
```

### 2.6 Python SDK

Log Service provides developers with Log Service SDK for Python to simplify the use of Log Service. Download URLs You can click here to download Log Service SDK for Python. You can also download Log Service SDK for Python from GitHub: https://github.com/aliyun/aliyun-log-python-sdk Step 1: Create an Apsara Stack tenant account To access Log Service, you must create an account in the Apsara Uni-manager Management Console. Step 2: Obtain an Apsara Stack AccessKey pair To use Log Service SDK for Python, you must obtain an AccessKey pair. Log on to the Apsara Uni-manager Management Console. Select an AccessKey pair for the SDK. The AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey pair will be used in the following steps and must be kept confidential. For information about how to use an AccessKey pair in Log Service SDK for Python, see Basic configurations. Step 3: Create a project and a Logstore in the Log Service console Before you can use the SDK, you must create a project and a Logstore in the Log Service console.
1. Log on to the Log Service console.
2. In the Projects section, click Creat e Project .
3. Set the Project Name and the Region parameters, and then click OK.
4. In the Project s section, click the name of the project. On the page that appears, click the plus sign
(+) in the left-side navigation pane. You can also click Creat e to create a Logstore as prompted after you create a project.
5. In the dialog box that appears, set the required parameters, and then click OK.
You must specify the Logstore name, data retention period, and number of shards. Set the number of shards based on your business requirements. In this example, four shards are created.

> Not e
> The account that you use to create the project and the Logstore must be the same as the account that you used to obtain the AccessKey pair.
> The project name must be unique in Log Service. The Logstore name must be unique in the project.
> After you create the project, you cannot modify its region or migrate the project across regions.

Step 4: Install the Python development environment Log Service SDK for Python is a pure Python library that supports all operating systems on which Python runs, such as Linux, Mac OS X, and Windows. To install the Python development environment, perform the following steps:
1. Download and install the latest Python installation package.

> Not e
> Log Service SDK for Python supports Python 2.6, 2.7, 3.3, 3.4, 3.5, and 3.6. You can run the `python -V` command to check the current version of Python.
> Python no longer supports Python 2.6 or Python 3.3. We recommend that you use Python 2.7, Python 3.4, or a later version.

2. Download and install the Python package management tool pip.
After you install pip, run the `pip -V` command to check whether the installation is successful and view the pip version. Step 5: Install Log Service SDK for Python Run the following command as an administrator in Shell to install Log Service SDK for Python.

```
pip install -U aliyun-log-python-sdk
```

Step 6: Start a Python program The following sample code shows how to use Log Service SDK for Python. To interact with Log Service and obtain the relevant output, run the following sample code in a text editor or Python IDE: For more information, visit GitHub.

```java
# encoding: utf-8
import time from aliyun.log.logitem import LogItem from aliyun.log.logclient import LogClient from aliyun.log.getlogsrequest import GetLogsRequest from aliyun.log.putlogsrequest import PutLogsRequest from aliyun.log.listlogstoresrequest import ListLogstoresRequest from aliyun.log.gethistogramsrequest import GetHistogramsRequest def main():
    endpoint = '' # Select the endpoint that matches the region of the project created in t
he preceding steps.
    accessKeyId = '' # Use your AccessKey ID.
    accessKey = '' # Use your AccessKey secret.
    project = '' # The name of the project created in the preceding steps.
    logstore = '' # The name of the Logstore created in the preceding steps.
    # Note: Configure four shards for the created Logstore.
    # Create a client instance.
    client = LogClient(endpoint, accessKeyId, accessKey)
    # List all Logstores.
    req1 = ListLogstoresRequest(project)
    res1 = client.list_logstores(req1)
    res1.log_print()
    topic = ""
    source = ""
    # Send 10 packets. Each packet contains 10 log entries.
    for i in range(10):
        logitemList = []  # LogItem list
        for j in range(10):
            contents = [('index', str(i * 10 + j))]
            logItem = LogItem()
            logItem.set_time(int(time.time()))
            logItem.set_contents(contents)
            logitemList.append(logItem)
        req2 = PutLogsRequest(project, logstore, topic, source, logitemList)
        res2 = client.put_logs(req2)
        res2.log_print()
    # List all shards and read the data written within the last minute.
    listShardRes = client.list_shards(project, logstore)
    for shard in listShardRes.get_shards_info():
        shard_id = shard["shardID"]
        start_time = int(time.time() - 60)
        end_time = start_time + 60
        res = client.get_cursor(project, logstore, shard_id, start_time)
        res.log_print()
        start_cursor = res.get_cursor()
        res = client.get_cursor(project, logstore, shard_id, end_time)
        end_cursor = res.get_cursor()
        while True:
            loggroup_count = 100  # Read 100 packets each time.
            res = client.pulllogs(project, logstore, shardid, startcursor, loggroupcoun
```

`p` `_`

```
g(p
```

`j` `,` `g` `,` `_` `,` `_` `,` `gg` `p_`

```bash
t, end_cursor)
            res.log_print()
            next_cursor = res.get_next_cursor()
            if next_cursor == start_cursor:
                break
            start_cursor = next_cursor
    # Note: You can call the following API operation to query data only after you enable th
e indexing feature.
    time.sleep(60)
    topic = ""
    query = "index"
    From = int(time.time()) - 600
    To = int(time.time())
    res3 = None
    # Query the number of log entries generated within the last 10 minutes based on the que
ry conditions. Retry the query if not all execution results are correct.
    while (res3 is None) or (not res3.is_completed()):
        req3 = GetHistogramsRequest(project, logstore, From, To, topic, query)
        res3 = client.get_histograms(req3)
    res3.log_print()
    # Obtain the number of log entries that match the query conditions.
    total_log_count = res3.get_total_count()
    log_line = 10
    # Read 10 log entries each time until all log data is queried. Retry the query three ti
mes if not all query results are correct during each query.
    for offset in range(0, total_log_count, log_line):
        res4 = None
        for retry_time in range(0, 3):
            req4 = GetLogsRequest(project, logstore, From, To, topic, query, log_line, offs
et, False)
            res4 = client.get_logs(req4)
            if res4 is not None and res4.is_completed():
                break
            time.sleep(1)
        if res4 is not None:
            res4.log_print()
    listShardRes = client.list_shards(project, logstore)
    shard = listShardRes.get_shards_info()[0]
    # Split a shard.
    if shard["status"] == "readwrite":
        shard_id = shard["shardID"]
        inclusiveBeginKey = shard["inclusiveBeginKey"]
        midKey = inclusiveBeginKey[:-1] + str((int(inclusiveBeginKey[-1:])) + 1)
        client.split_shard(project, logstore, shard_id, midKey)
    # Merge shards.
    shard = listShardRes.get_shards_info()[1]
    if shard["status"] == "readwrite":
        shard_id = shard["shardID"]
        client.merge_shard(project, logstore, shard_id)
    # Delete a shard.
    shard = listShardRes.get_shards_info()[-1]
    if shard["status"] == "readonly":
        shard_id = shard["shardID"]
        client.delete_shard(project, logstore, shard_id)
```

```bash
 # Create an external data source. def sample_external_store(client,project): res = client.
create_external_store(project,ExternalStoreConfig("rds_store","cn-qingdao","rds-vpc","vpc-m 5eq4irc1pucpk85frr5j","i-m5eeo2whsnfg4kzq54ah","47.104.78.128","3306","root","sfdsfldsfksfl sdfs","meta","join_meta")); res.log_print() res = client.update_external_store(project,Exte rnalStoreConfig("rds_store","cn-qingdao","rds-vpc","vpc-m5eq4irc1pucpk85frr5j","i-m5eeo2whs nfg4kzq54ah","47.104.78.128","3306","root","sfdsfldsfksflsdfs","meta","join_meta")); res.lo g_print() res = client.get_external_store(project,"rds_store"); res.log_print() res = clien t.list_external_store(project,""); res.log_print(); res = client.delete_external_store(proj ect,"rds_store") res.log_print(); # Use Log Service SDK for Python to query data. req4 = Ge tLogsRequest(project, logstore, From, To, topic, "* | select count(1)", 10,0, False) res4 = client.get_logs(req4) # Use Log Service SDK for Python to query data in ApsaraDB RDS for My SQL through the JOIN syntax. req4 = GetLogsRequest(project, logstore, From, To, topic, "* | select count(1) from "+logstore +" l join rds_store r on l.ikey =r.ekey", 10,0, False) res4 = client.get_logs(req4) # Use Log Service SDK for Python to write the query result to RDS. req4 = GetLogsRequest(project, logstore, From, To, topic, "* | insert into rds_store select count(1) ", 10,0, False) res4 = client.get_logs(req4) if __name__ == '__main__':
    main()
```

### 2.7 SDK for Android

The Log Service SDK for Android is used to collect user data from Android platforms and write the data to Log Service. Download URL at GitHub https://github.com/aliyun/aliyun-log-android-sdk

### 2.8 SDK for C

The Log Service SDK for C is used to access logs in Log Service from multiple platforms, such as the MIPS and OpenWrt systems. The SDK for C uses libcurl as a network library. The apr/apr-util library resolves issues about memory management and cross-platform operations. You can use the SDK for C after you compile a small part of the source code. In addition, the C Producer Library and C Producer Lite Library provide you with a one-stop log collection solution across different platforms. This solution features simple deployment, high performance, and low resource consumption. For more information, visit the following GitHub URLs: C Producer Library (recommended for servers) C Producer Lite Library (recommended for IoT and smart devices)

### 2.9 SDK for Go

Log Service provides developers with the SDK for Go to simplify the use of Log Service. The Log Service SDK for Go allows developers to perform the following operations: Write and consume data in batches. Use keywords to query indexes. Manage Logtail configurations and machine groups. You can download the SDK for Go from the following GitHub URL: https://github.com/aliyun/aliyunlog-go-sdk. For information about the usage instructions and sample code, see README.

### 2.10 iOS SDK

Log Service SDK for iOS is implemented based on Log Service APIs. The SDK allows you to write logs to Log Service. You can download Log Service SDK for iOS from GitHub based on your programming language. Swift: https://github.com/aliyun/aliyun-log-ios-sdk. Object-C: https://github.com/lujiajing1126/AliyunLogObjc. AliyunLogObjc is a third-party tested SDK. You can raise issues to the author and receive a quick response. Swift-based sample code of Log Service SDK for iOS `/*`

```
    Use an endpoint, AccessKey ID, and AccessKey secret to create a Log Service client.
    @endPoint: The endpoint. For more information, visit https://help.aliyun.com/document_d
etail/29008.html.
```

`*/`

```python
let myClient = try! LOGClient(endPoint: "",
                              accessKeyID: "",
                              accessKeySecret: "",
                              projectName:"")
/* Create a log group. */ let logGroup = try! LogGroup(topic: "mTopic",source: "mSource")
   /* Write a log entry to the log group. */
    let log1 = Log()
          try! log1.PutContent("K11", value: "V11")
         try! log1.PutContent("K12", value: "V12")
         try! log1.PutContent("K13", value: "V13")
    logGroup.PutLog(log1)
   /* Write a log entry to the log group. */
    let log2 = Log()
          try! log2.PutContent("K21", value: "V21")
         try! log2.PutContent("K22", value: "V22")
         try! log2.PutContent("K23", value: "V23")
    logGroup.PutLog(log2)
 /* Send the log entry. */
 myClient.PostLog(logGroup,logStoreName: ""){ response, error in
        // handle response however you want
        if error?.domain == NSURLErrorDomain && error?.code == NSURLErrorTimedOut {
            print("timed out") // note, `response` is likely `nil` if it timed out
```

Objective-C For information about how to use Log Service SDK for iOS based on Objective-C, visit Objective-C at GitHub.

### 2.11 SDK for C ++

The Log Service SDK for C ++ allows you call Log Service API operations in C++ programs. This SDK applies only to Linux platforms. The Log Service SDK for C ++ supports all Log Service APIs and provides multiple features, such as resource creation and data read/write. You can download the SDK for C ++ from the following GitHub URL: https://github.com/aliyun/aliyunlog-cpp-sdk.

### 2.12 Node.js SDK

Log Service SDK for Node.js allows developers to use Log Service by using Node.js programs. This topic describes how to use Log Service SDK for Node.js to write log data to Log Service. Procedure
1. Create an Apsara Stack tenant account.
2. Obtain an Apsara Stack AccessKey pair.
The AccessKey pair will be used in the following steps and must be kept confidential. For information about how to use the AccessKey pair in Log Service SDK for Node.js, see Basic configurations.
3. Create a project.
i. Use the Node.js web framework Express to create a project. For more information, see installing. ii. Install morgan. iii. Create an app.js file in the project. The app.js file contains the following code:

```
var express = require('express') var morgan = require('morgan') var app = express() const logger = morgan(function (tokens, req, res) {
  return [
    tokens.method(req, res),
    tokens.url(req, res),
    tokens.status(req, res),
    tokens.res(req, res, 'content-length'), '-',
    tokens['response-time'](req, res), 'ms'
  ].join(' ')
```

`})`

```
app.use(logger) app.get('/', (req, res) => res.send('Hello World!')) app.listen(3000, () => console.log('Example app listening on port 3000!'))
```

iv. Run the node app.js command to start the project. Visit `http://localhost:3000` . Then, access logs are generated.
4. Write logs to Log Service.
i. Install aliyun-sdk. Click here to download aliyun-sdk. Run the npm inst all aliyun-sdk command to install aliyunsdk. ii. Create a project and a Logstore in the Log Service console. iii. Call Log Service SDK for Node.js in the project. The following sample code is used:

```
var express = require('express') var morgan = require('morgan') var ALY = require('aliyun-sdk') // Call aliyun-sdk. var app = express() const logger = morgan(function (tokens, req, res) {
  // Obtain log data.
  const log = [
    tokens.method(req, res),
    tokens.url(req, res),
    tokens.status(req, res),
    tokens.res(req, res, 'content-length'), '-',
    tokens['response-time'](req, res), 'ms'
```

`]`

```json
  var sls = new ALY.SLS({
    "accessKeyId": "LTA******G9", // The AccessKey ID that is obtained in Step 2
    "secretAccessKey": "MMfX******lo1", // The AccessKey secret that is obtained in
Step 2
    endpoint: 'http://cn-hangzhou.sls.aliyuncs.com',
    apiVersion: '2015-06-01'
```

`})`

```
  var logGroup = {
    logs: [
        time:  Math.floor(new Date().getTime()/1000), // Unit: seconds
        contents: [ // Key-value pairs
            key: 'method',
            value: log[0]
```

`},`

```
            key: 'url',
            value: log[1]
```

`},`

```
            key: 'status',
            value: log[2]
```

`},`

```
            key: 'time',
            value: log[5]
```

`]`

```
    }],
    topic: 'topicName', //optional
    source: '127.0.0.1' //optional
```

};

```
  var opt = {
    projectName: 'wangdan-test',
    logStoreName: 'test',
    logGroup
  sls.putLogs(opt,function(error, data) {
    console.log(error, data)
```

`})`

```
  return [
    tokens.method(req, res),
    tokens.url(req, res),
    tokens.status(req, res),
    tokens.res(req, res, 'content-length'), '-',
    tokens['response-time'](req, res), 'ms'
  ].join(' ')
```

`})`

```
app.use(logger) app.get('/', (req, res) => res.send('Hello World!')) app.listen(3000, () => console.log('Example app listening on port 3000!'))
```

5. View collected log data.
In the Log Service console, find the Logstore in the project. Click the Logstore name, enter a query statement in the search box on the Search & Analysis page, and then click Search & Analyze to view log data. The following figure indicates that most page views (PVs) occurred between 18:30 and 19:00 on September 12 during the specified time range. You can record and display the PV statistics as a chart on your dashboard.

## 3 ASAPI Reference

### 3.1 Overview

This topic describes the architecture and features of Apsara Stack API (ASAPI). ASAPI is a platform that integrates all features and is the only portal to connect to Apsara Stack. ASAPI can categorize, audit, and manage API operations. ASAPI can also assemble and customize existing API operations and adapt to your API operations. Each cloud service can call ASAPI for required data and features to avoid inconsistent operations that may be caused by different request methods and separate encapsulation. This ensures the integrity of API operations, increases the development efficiency of API operations, and improves the portability of code.

> Not e Only the CreateProject, DeleteProject, UpdateProject, GetProject, and ListProject API operations in Log Service are available in ASAPI. You can use ASAPI to call these API operations.

ASAPI allows you to manage and call API operations in a centralized manner and customize development for API operations. ASAPI supports access to most cloud services deployed in Apsara Stack and supports pass-through or encapsulation of different backend APIs. This way, operations can be called by using the same method. ASAPI allows you to use SDKs and API portals to call API operations registered on ASAPI, customize SDKs, and manage versions of Apsara Stack, services, and APIs.

### 3.2 Preparations

#### 3.2.1 Log on to the API Tool console

You can log on to the API Tool console from the Apsara Uni-manager Management Console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator.

> Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types:
> Uppercase or lowercase letters
> Digits
> Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)

3. Click Log On.
4. In the top navigation bar, choose Product s > Ot hers > API T ool.

#### 3.2.2 View the information of API operations

This topic describes how to view information of API operations. The following information is required when you use an SDK: service name, API operation name, and API operation version. Procedure
1. Log on to the API Tool console.
2. In the left-side navigation pane, click API Direct ory.
3. On the API Direct ory page, select the required service from the drop-down list in the upper-left
corner. Then, enter a keyword of an API operation name in the search box and click the Search icon.
4. Then, you can view the service name, API operation name, and API version number.

#### 3.2.3 Generate an endpoint for the ASAPI

This topic describes three methods used to generate an endpoint for the Apsara Stack API (ASAPI). Method 1: Use Registration Vars of Services to generate an endpoint
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
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click O&M. iii. In the left-side navigation pane, choose Product Management > Product s. iv. In the Apsara Stack O&M section, click Apsara Inf rast ruct ure Management Framework.
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

> Not e

1. Replace <region> with your actual region ID. For information about how to query a region ID,
see Query a region ID.
2. Replace <internet-domain> with the root domain of your Apsara Stack service. To obtain the
root domain, contact Apsara Stack O&M personnel. Take note of this point: Use the internetdomain parameter instead of the intranet-domain parameter. If the region value is `cn-****-****-d01` and the int ernet -domain value is `inter.****.****.com` , the following endpoint can be generated:

```
https://public.asapi.cn-****-****-d01.inter.****.****.com/asapi/v3
```

#### 3.2.4 Obtain Apsara Stack SDKs

The Apsara Stack API (ASAPI) is a unified portal provided by Apsara Stack. You can use the ASAPI to connect to all Apsara Stack services. Apsara Stack provides SDKs for API calls. For more information about how to obtain Apsara Stack SDKs, see Apsara Stack documentation.

#### 3.2.5 Obtain an AccessKey pair

An AccessKey pair that consists of an AccessKey ID and an AccessKey secret is used to implement symmetric encryption. This helps you verify the identity of a requester. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. This topic describes how to obtain an AccessKey pair. Prerequisites An account of the operations administrator or the level-1 organization administrator is obtained. Only an operations administrator or a level-1 organization administrator can obtain an AccessKey pair. Context If you need to make API calls to the Apsara Uni-manager Management Console or other Apsara Stack services, we recommend that you use the AccessKey pair of a personal account. If you use the AccessKey pair of a personal account, configure the request headers that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions can occur.

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region, for example, cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For information about how to obtain an organization ID, see the "GetOrganizationList" section in Apsara Uni-manager Management Console Developer Guide. |

| Parameter | Description |
|---|---|
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For information about how to obtain a resource set ID, see the "ListResourceGroup" section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance to which you make API calls. If you need to make API calls to an Elastic Compute Service (ECS) instance, obtain the ID of the ECS instance on the Instances page. |

> **Warning:** The AccessKey pair of a personal account is managed and controlled by the permission system of the Apsara Uni-manage Management Console. If you need to obtain the AccessKey pair of an account that has permissions on an organization, make sure that your operation is allowed by an administrator. This ensures security. The account that has permissions on an organization is a privileged account.

Obtain the AccessKey pair of a personal account To obtain the AccessKey pair of a personal account, perform the following operations:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and click User
Inf ormat ion.
3. In the Apsara St ack AccessKey Pair section, obtain the AccessKey pair.

> Not e The AccessKey pair that consists of an AccessKey ID and an AccessKey secret is the credential for you to have full permissions on Apsara Stack resources. Keep your AccessKey pair confidential.

Obtain the AccessKey pair of an account that has permissions on an organization To obtain the AccessKey pair of an account that has permissions on an organization, perform the following operations:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane of the Ent erprise page, click Organizat ions.
4. In the Organizations navigation tree, click the name of the organization that you want to manage.
5. On the right side of the page, click Obt ain AccessKey Pair.
6. In the message that appears, obtain the AccessKey pair of the account that has permissions on the
organization.

> Not e The system automatically allocates an AccessKey pair to the account that has permissions on the level-1 organization. The same AccessKey pair is used by the accounts that have permissions on the subordinate organizations.

#### 3.2.6 Query a region ID

When you use Apsara Stack SDK for Node.js to make API calls, specify a region ID. You can obtain a region ID in the Apsara Uni-manager Management Console. Procedure
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and click User
Inf ormat ion.
3. In the Apsara St ack AccessKey Pair section, view the region ID.

### 3.3 Common request parameters

Common request parameters must be included in all API requests. Common request parameters The following common request parameters are used to call the ASAPI service.

| Paramet er | T ype | Required | Descript ion |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. For more information, see View the information about API operations. |
| Product | String | Yes | The name of the service. |
| Version | String | Yes | The API version of the service. For more information, see View the information about API operations. |

| Paramet er | T ype | Required | Descript ion |
|---|---|---|---|
| RegionId | String | Yes | The ID of the region. For more information, see Query the region ID. |
| AccessKeyId | String | Yes | The AccessKey ID used to connect to the service. For more information, see Obtain an AccessKey pair. |
| Signature | String | Yes | The signature string of the request. For more information, see Request signatures. |
| SignatureMethod | String | Yes | The encryption method of the signature string. Set the value to HMAC- SHA1 or HMAC-SHA256. |
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Set the value to 1.0 or 2.0. |
| SignatureNonce | String | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the yyyy- MM-ddTHH:mm:ssZ format. The time must be in UTC. Example: 2018-01-01T12:00:00Z. |

| Paramet er | T ype | Required | Descript ion |
|---|---|---|---|
| Format | String | Yes | The format in which to return the response. Set the value to JSON. |

> Not e

```
The Signature , SignatureMethod , SignatureVersion , SignatureNonce , Timestamp ,
```

> and `Format` parameters are encapsulated into the SDK.

### 3.4 SDK Reference

#### 3.4.1 Apsara Stack SDK for Java

This topic describes how to obtain and use Apsara Stack SDK for Java. Prerequisites An authorized account and an AccessKey pair are obtained. The AccessKey pair consists of an AccessKey ID and an AccessKey secret. For more information about how to obtain and view your AccessKey pair in the Apsara Uni-manager Management Console, see Obtain an AccessKey pair. The endpoint of ASAPI is obtained. For more information, see Obtain the endpoint of ASAPI. Apsara Stack SDK for Java supports JDK V1.8 and later. Add dependencies Add dependencies to the pom.xml file:

```xml
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>asapi</artifactId>
    <version>0.0.8.1-RELEASE</version>
</dependency>
```

Use Apsara Stack SDK for Java

```
// Set the request parameters. try {
  Map<String, String> requestParams = new HashMap<String, String>();
  // Set the parameters for Log Service.
  requestParams.put("Product", "SLS"); // The service name must be the same as that displ
ayed in the corresponding API directory.
  requestParams.put("Action", "ListProject"); // The name of the API operation. The name
```

```java
is case-sensitive and must be the same as that in the API directory.
  requestParams.put("Version", "2020-03-31"); // The version number of the API.
  requestParams.put("offset", "0");
  requestParams.put("size", "10");
  // Set the authorization parameters.
  requestParams.put("AccessKeyId", ""); // The AccessKey ID of the authorized account.
  requestParams.put("AccessKeySecret", ""); // The AccessKey secret of the authorized acc
ount.
  requestParams.put("RegionId", ""); // The region ID.
  // Create a client to initiate requests.
  ASClient client = new ASClient();
  // Set the parameters in the request header.
  client.addHeader("x-acs-regionId", "");
  client.addHeader("x-acs-resourcegroupid", "");
  client.addHeader("x-acs-organizationid", "");
  // Initiate the request and obtain the response.
  String result = client.doRequest("your_endpoint", requestParams);
  JSONObject jsonObject = JSONObject.parseObject(result);
  Map<String, Object> mapData = new HashMap<String, Object>();
  if ("true".equals(jsonObject.getString("success"))) {
    String projects = jsonObject.getString("projects");
    List<String> array = JSONArray.parseArray(projects, String.class);
    List<Object> data = new ArrayList<Object>();
    for (String projectStr : array) {
      JSONObject object = JSONObject.parseObject(projectStr);
      Set<String> keySet = object.keySet();
      Map<String, String> map = new HashMap<String, String>(keySet.size());
      for (String key : keySet) {
        if ("description".equals(key)) {
          String description = object.getString(key);
          map.put("projectDesc", description == null ? "" : description);
      } else if ("region".equals(key)) {
        map.put("clusterRegion", object.getString(key));
      } else {
        map.put(key, object.getString(key));
    data.add(map);
    mapData.put(SLSBaseConst.E_PROJECTS, data);
    mapData.put(SLSBaseConst.E_TOTAL, jsonObject.getInteger("total"));
    mapData.put(SLSBaseConst.E_COUNT, jsonObject.getInteger("count"));
    System.out.println(mapData);
   } else {
     throw new RuntimeException("list failed");
  } catch (Exception e) {
    e.printStackTrace();
```

CreateProejct

```java
try {
  Map<String, String> requestParams = new HashMap<String, String>();
  // Set the parameters for Log Service.
  requestParams.put("action", "CreateProject"); // The name of the API operation. The nam
e is case-sensitive and must be the same as that in the API directory.
  requestParams.put("product", "SLS"); // The service name must be the same as that displ
ayed in the corresponding API directory.
  requestParams.put("version", "2020-03-31"); // The version number of the API.
  requestParams.put("projectName", ""); // The name of the project.
  requestParams.put("description", ""); // The description of the project.
  requestParams.put("RegionId", ""); // The region ID.
  requestParams.put("AccessKeyId", ""); // The AccessKey ID of the authorized account.
  requestParams.put("AccessKeySecret", ""); // The AccessKey secret of the authorized acc
ount.
  requestParams.put("Department", "");
  requestParams.put("ResourceGroup", "");
  // Create a client to initiate requests.
  ASClient client = new ASClient();
  // Set the parameters in the request header.
  client.addHeader("x-acs-regionId", "");
  client.addHeader("x-acs-resourcegroupid", "");
  client.addHeader("x-acs-organizationid", "");
  String result = client.doRequest("your_endpoint", requestParams);
  System.out.println(result);
} catch (Exception e) {
  e.printStackTrace();
```

```java
try {
  Map<String, String> requestParams = new HashMap<String, String>();
  // Set the parameters for Log Service.
  requestParams.put("action", "GetProject"); // The service name must be the same as that
displayed in the corresponding API directory.
  requestParams.put("product", "SLS"); // The name of the API operation. The name is case
-sensitive and must be the same as that in the API directory.
  requestParams.put("version", "2020-03-31"); // The version number of the API.
  requestParams.put("projectName", ""); // The name of the project.
  requestParams.put("RegionId", ""); // The AccessKey ID of the authorized account.
  requestParams.put("AccessKeyId", ""); // The AccessKey ID of the authorized account.
  requestParams.put("AccessKeySecret", ""); // The AccessKey secret of the authorized acc
ount.
  // Create a client to initiate requests.
  ASClient client = new ASClient();
  // Set the parameters in the request header.
  client.addHeader("x-acs-regionId", "");
  client.addHeader("x-acs-resourcegroupid", "");
  client.addHeader("x-acs-organizationid", "");
  client.addHeader("x-acs-instanceId", "");
    String result = client.doRequest("your_endpoint", requestParams);
    JSONObject object = JSONObject.parseObject(result);
    if (object.getString("projectName") == null) {
      throw new RuntimeException(result);
    } else {
      Set<String> keySet = object.keySet();
      Map<String, String> map = new HashMap<String, String>(keySet.size());
      for (String key : keySet) {
        if ("description".equals(key)) {
          String description = object.getString(key);
          map.put("projectDesc", description == null ? "" : description);
        } else if ("region".equals(key)) {
         map.put("clusterRegion", object.getString(key));
        } else {
        map.put(key, object.getString(key));
      System.out.println(map);
  } catch (Exception e) {
    e.printStackTrace();
```

```java
try {
  Map<String, String> requestParams = new HashMap<String, String>();
  // Set the parameters for Log Service.
  requestParams.put("action", "UpdateProject"); // The name of the API operation. The nam
e is case-sensitive and must be the same as that in the API directory.
  requestParams.put("product", "SLS"); // The service name must be the same as that displ
ayed in the corresponding API directory.
  requestParams.put("version", "2020-03-31"); // The version number of the API.
  requestParams.put("projectName", "");// The name of the project to be updated.
  requestParams.put("description", ""); // The description of the project.
  requestParams.put("RegionId", ""); // The region ID.
  requestParams.put("AccessKeyId", ""); // The AccessKey ID of the authorized account.
  requestParams.put("AccessKeySecret", ""); // The AccessKey secret of the authorized acc
ount.
  requestParams.put("Department", "");
  requestParams.put("ResourceGroup", "");
  // Create a client to initiate requests.
  ASClient client = new ASClient();
  // Set the parameters in the request header.
  client.addHeader("x-acs-regionId", "");
  client.addHeader("x-acs-resourcegroupid", "");
  client.addHeader("x-acs-organizationid", "");
  String result = client.doRequest("your_endpoint", requestParams);
    System.out.println(result);
  } catch (Exception e) {
    e.printStackTrace();
```

```java
try {
  Map<String, String> requestParams = new HashMap<String, String>();
  // Set the parameters for Log Service.
  requestParams.put("action", "DeleteProject"); // The name of the API operation. The nam
e is case-sensitive and must be the same as that in the API directory.
  requestParams.put("product", "SLS"); // The service name must be the same as that displ
ayed in the corresponding API directory.
  requestParams.put("version", "2020-03-31"); // The version number of the API.
  requestParams.put("projectName", ""); // The name of the project to be deleted.
  requestParams.put("RegionId", ""); // The region ID.
  requestParams.put("AccessKeyId", ""); // The AccessKey ID of the authorized account.
  requestParams.put("AccessKeySecret", ""); // The AccessKey secret of the authorized acc
ount.
  // Create a client to initiate requests.
  ASClient client = new ASClient();
  // Set the parameters in the request header.
  client.addHeader("x-acs-regionId", "");
  client.addHeader("x-acs-resourcegroupid", "");
  client.addHeader("x-acs-organizationid", "");
  client.addHeader("x-acs-instanceId", "");
    String result =client.doRequest("<your_endpoint>", requestParams);
    System.out.println(result);
  } catch (Exception e) {
    e.printStackTrace();
```

The following table describes the parameters in the request header.

| Parameter | Description |
|---|---|
| x-acs-regionid | The region ID. For more information about how to obtain the region ID, see Query the region ID. |
| x-acs-resourcegroupid | The ID of the organization in the Apsara Uni- manager Management Console. |
| x-acs-organizationid | The ID of the resource set in the Apsara Uni- manager Management Console. |
| x-acs-instanceid | The ID of the instance that you want to manage. |

### 3.5 HTTP Requests

#### 3.5.1 Overview

This topic describes how to make API requests and is intended for users who use API URLs to initiate HTTP GET requests. If you are using an SDK to initiate requests, you can skip this topic. The request URL consists of different parameters and has a fixed syntax. The URL contains common request parameters, your signature, and operation-specific parameters. Sample request URLs are provided for each API operation. These URLs are not encoded to make them easy to read. Before you make a request, you must encode the request URL. After the authentication process is complete based on your signature, the results are returned to you. Response parameters are returned if the call is successful, whereas an error message is returned if the call fails. You can troubleshoot issues based on the error message.

#### 3.5.2 Request syntax

The Apsara Stack API (ASAPI) allows you to call API operations by sending HTTP GET requests based on URLs. Each URL must include request parameters. This topic describes the syntax of HTTP GET requests and provides the endpoint of the ASAPI. Sample request GetOrganizationList is used in the following unencoded URL request:

```
https://public.asapi.aliyuns.com/asapi/v3?Action=GetOrganizationList&Product=ascm&Version=2 019-05-10&Id=<Organization ID>&<Common parameters>
```

`https` : the protocol used to transmit the request. `public.asapi.aliyuns.com/asapi/v3` : the endpoint of the ASAPI. `Action=GetOrganizationList Product=ascm Version=2019-05-10` : the API operation to call. `Id` : the ID of the organization. `<Common parameters>` : the common parameters specified in the system. Protocol The ASAPI supports only HTTPS. Endpoint For more information about how to obtain an endpoint, see Generate an endpoint for the ASAPI. To specify an API operation, use the `Action, Product, and Version` parameters. For example, set `Action` to GetOrganizationList, Product to ascm, and Version to 2019-05-10. You must also specify other operation-specific parameters and common parameters. For more information, see Common parameters.

#### 3.5.3 Request signatures

This topic describes how to sign HTTP API requests. ASAPI uses the request signature to verify the identity of the request sender. ASAPI implements symmetric encryption by using an AccessKey pair to verify the identity of the request sender.

> Not e
> An AccessKey pair consists of an AccessKey ID and an AccessKey secret, which are issued to each user or organization in the Apsara Uni-manager Management Console.
> The AccessKey ID is used to verify identities of users, and the AccessKey secret is used to encrypt and verify signature strings. You must keep your AccessKey secret confidential.
> ASAPI provides SDKs for Node.js, Python, and Java to facilitate complex signature calculation. For more information, see Obtain the core package for ASAPI.

Step 1: Create a canonicalized query string
1. Arrange the request parameters in alphabetical order, including all common and operation-specific
parameters except the `Signature` parameter.

> Not e
> If you use the GET method to send a request,these parameters are connected by ampersands (&) and included in the request URL. The first request parameter follows a question mark (?).

2. Encode the request parameters and their values in UTF-8 based on RFC 3986. The following rules
apply in the encoding process: Letters, digits, and special characters such as hyphens ( `-` ), underscores ( `_` ), and periods ( `.` ) do not need to be encoded. Other characters must be percent encoded in the %XY format. `XY` represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks ( `"` ) are encoded as %22 . Extended UTF-8 characters are encoded in the %XY%ZA… format. Spaces must be encoded as %20 . Do not encode spaces as plus signs ( `+` ). This encoding method is similar to but different from the `application/x-www-form-urlencoded` MIME encoding algorithm. If you use `java.net.URLEncoder` from the Java standard library, use `percentEncode` to encode request parameters and their values. In the encoded query string, replace the plus signs ( `+` ) with %20 , asterisks ( `*` ) with %2A , and %7E with tildes ( ~ ). This way, you can obtain an encoded string that matches the preceding encoding rules.

```java
private static final String ENCODING = "UTF-8"; private static String percentEncode(String value) throws UnsupportedEncodingException
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

> Not e
> When you calculate the signature, the key value specified by RFC 2104 is your
> `AccessKey secret` plus an ampersand (&), which has an ASCII value of 38. For more

information, see Obtain an AccessKey pair.
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

You can use browsers or tools such as cURL and Wget to initiate an HTTP request for calling the `DescribeRegions` operation to query the Alibaba Cloud region list. Example 2: Use t he st andard library of t he programming language `GetOrganizationList` is used in this example to query regions. For example, `AccessKeyID` is set to testid, `AccessKeySecret` is set to testsecret, and all request parameters are stored in a Java `Map<String, String>` object.
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

5. Use browsers or tools such as cURL and Wget to initiate an HTTP request.

#### 3.5.4 Response

Responses are returned only in the JSON format. If a return code is greater than or equal to 200 and less than 300, a success response is returned. Otherwise, an error response is returned. Sample success response If a request is successful, the request ID and operation-specific parameter values are returned. For more information, see the developer guide of the corresponding Apsara Stack service.

```json
    "eagleEyeTraceId": "xxx-xxx-xxx-xxx", // The trace ID provided by EagleEye.
    "asapiSuccess": true,
    "RequestId": "xxxxxxxxxx",
    "Regions": { // The regions returned after you call the DescribeRegions operation.
        "Region": [
                "RegionId": "",
                "RegionEndpoint": "",
                "LocalName": ""
```

`]` Sample error response If a request fails, the following information is returned. For more information, see the developer guide of the corresponding Apsara Stack service.

```json
    "code": "asapi.server.api.notfound",// The error code.
    "eagleEyeTraceId": "xxx-xxx-xxx-xxx", // The trace ID provided by EagleEye.
    "asapiSuccess": false, // Indicates whether the request is successful.
    "hostId": "xxxx", // The ID of the host.
    "message": "Failed to ....", // The message returned.
    "asapiErrorMessage": "Failed to ....", // The error message provided by the ASAPI.
    "asapiErrorCode": "asapi.server.api.notfound" // The error code provided by the ASAPI.
```

ey pair

## 4 Obtain an AccessKey pair

An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey pair is used to implement symmetric encryption to verify the identity of the requester. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. This topic describes how to obtain the AccessKey pair of an organization. Prerequisites Only the operation administrators or level-1 organization administrators can obtain the AccessKey pair of an organization. Context We recommend that you use the AccessKey pair of a personal account to call Apsara Uni-manager and cloud service APIs. When you use the AccessKey pair of a personal account, you must configure header parameters in the following table for access control.

| Parameter | Description |
|---|---|
| x-acs-regionid | The region ID, such as cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager console. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager console. |
| x-acs-instanceid | The ID of the instance on which you want to perform operations. |

> **Warning:** The AccessKey pairs of personal accounts are managed by the Apsara Uni-manager permission system. AccessKey pairs of organization accounts have higher permissions. For security purposes, organization operations must be approved by administrators.

Obtain the AccessKey pair of a personal account To obtain the AccessKey pair of a personal account, perform the following operations:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and click User
Inf ormat ion.
3. In the Apsara St ack AccessKey Pair section, view your AccessKey pair.
ey pair

> Not e The AccessKey pair consists of an AccessKey ID and an AccessKey secret. AccessKey pairs allow you to access Apsara Stack resources with full permissions for your account. You must keep your AccessKey pair confidential.

Obtain the AccessKey pair of an organization To obtain the AccessKey pair of an organization, perform the following operations:
1. In the address bar, enter the URL of the Apsara Uni-manager Management Console. Press the Enter
key.
2. Enter your username and password.
Obtain the username and password that you can use to log on to the console from the operations administrator.

> Not e When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. Your password must meet complexity requirements. The password must be 8 to 20 characters in length and must contain at least two of the following character types:
> Uppercase or lowercase letters
> Digits
> Special characters, which include ! @ # $ %

3. Click Login.
4. In the top navigation bar, click Ent erprise.
5. In the left-side navigation pane of the Ent erprise page, click Organizat ions.
6. In the organization navigation tree, click an organization name.
7. In the Current Organization section, click Obt ain an accesskey.
8. In the AccessKey message, view the AccessKey pair of the organization.

> Not e An AccessKey pair is automatically allocated to each level-1 organization. Subordinate organizations use the same AccessKey pair of their level-1 organization.

t

## 5 Obtain an endpoint

You can obtain an endpoint of a service in the Apsara Uni-manager Operations Console. Procedure
1. Log on to the Apsara Uni-manager Operations Console.
For more information, see Log on to the API Tool console.
2. In the left-side navigation pane, choose Product s > Product List > Apsara St ack O&M.
3. Click Apsara Inf rast ruct ure Management Framework to go to the Apsara Infrastructure
Management Framework console.
4. In the left-side navigation pane, click Report s to open the All Report s page.
5. In the Report column, click Regist rat ion Vars of Services.
6. In the dialog box that appears, click the
icon in the column, enter sls in the search box, and then click Apply Filt er.
7. Right-click the service in the Service Regist rat ion column of sls-backend-server, and then click
Show More.
8. In the Det ails dialog box, view the endpoint of Log Service.
