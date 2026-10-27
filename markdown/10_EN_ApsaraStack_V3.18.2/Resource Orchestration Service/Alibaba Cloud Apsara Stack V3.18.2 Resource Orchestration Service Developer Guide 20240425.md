---
title: "Alibaba Cloud Apsara Stack V3.18.2 Resource Orchestration Service Developer Guide 20240425"
product_version: "V3.18.2"
doc_version: "20240425"
pdf_pages: 68
source_pdf: "Alibaba Cloud Apsara Stack V3.18.2 Resource Orchestration Service Developer Guide 20240425.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.2%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E8%B5%84%E6%BA%90%E7%BC%96%E6%8E%92/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.2%20Resource%20Orchestration%20Service%20Developer%20Guide%2020240425.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.2 Resource Orchestration Service Developer Guide 20240425

## Table of Contents

- 1 API reference
  - 1.1 文档标题缺失，请补全后重新导出
    - 1.1.1 Overview
    - 1.1.2 List of operations by function
    - 1.1.3 Make API requests
      - 1.1.3.1 Overview
      - 1.1.3.2 Request structure
      - 1.1.3.3 Common parameters
      - 1.1.3.4 Responses
      - 1.1.3.5 Request signatures
      - 1.1.3.6 Status code
    - 1.1.4 Stack operations
      - 1.1.4.1 Create a stack
      - 1.1.4.2 Delete a stack
      - 1.1.4.3 Discard a stack
      - 1.1.4.4 Query stacks
      - 1.1.4.5 Query the information about a stack
      - 1.1.4.6 Preview a stack
      - 1.1.4.7 Update a stack
    - 1.1.5 Resource operations
      - 1.1.5.1 Query a list of resources
      - 1.1.5.2 Query the information about a resource
      - 1.1.5.3 Query resource types
      - 1.1.5.4 Query the information about a resource type
      - 1.1.5.5 Query the information about a resource type-specific template
    - 1.1.6 Template operations
      - 1.1.6.1 Validate the information about a template
      - 1.1.6.2 Query the information about a template
    - 1.1.7 Other operations
      - 1.1.7.1 Query events
- 2 Use Apsara Stack SDK by ASAPI
  - 2.1 Overview
  - 2.2 Log on to the API Tool console
  - 2.3 View the information about API operations
  - 2.4 Obtain the endpoint of ASAPI
  - 2.5 Obtain the core package for ASAPI
  - 2.6 Obtain an AccessKey pair
  - 2.7 Query the region ID
  - 2.8 SDK for Java
  - 2.9 SDK for Node.js
  - 2.10 Use POP SDK to call ASAPI (optional)

## 1 API reference

### 1.1 文档标题缺失，请补全后重新导出

#### 1.1.1 Overview

Resource Orchestration Service (ROS) enables you to create templates and define the cloud resources (such as ECS or ApsarDB for RDS instances) that are required for your business in the templates. Then, ROS automatically creates and configures resources based on the templates. ROS has the following benefits.

**Simplify resource management**

If you want to create a scalable web application that contains backend databases or to create a cluster that consists of dozens of ECS instances, you need to deploy multiple resources such as ECS, ApsaraDB for RDS, VPC, ESS, and SLB. Typically, you must deploy each resource individually and manually orchestrate the resources to satisfy your needs. These tasks are time-consuming and add complexity to the operations required to get your application up and running. ROS allows you to create a web application or cluster by creating or modifying a resource orchestration template, without the need to worry about the complex configuration. For example, the template lists the attributes (such as type, configuration, and quantity) and dependencies of the required resources. Then ROS parses this template, creates the resources based on their dependencies and parameters, and automatically orchestrates the resources to satisfy your needs. This ensures that all resources created by using the template run properly. Furthermore, you can delete all resources that are created by the same template at the click of a button.

**Quickly replicate a collection of resources**

If you have created a web application or cluster by using ROS, you can reuse the template to replicate the entire collection of resources. The template records the attributes and dependencies of each resource. You do not need to configure the resources again during resource replication.

#### 1.1.2 List of operations by function

The following tables list API operations available for use in Resource Orchestration Service (ROS), such as stack, resource, and template operations. Table 1. Stack operations

| URI | Method | Description |
|---|---|---|
| /stacks | POST | Creates a stack. |
| /stacks | GET | Queries the list of stacks. |
| /stacks/{StackName}/{StackId} | GET | Queries information about a stack. |
| /stacks/{StackName}/{StackId} | PUT | Updates a stack. |
| /stacks/{StackName}/{StackId} | DELETE | Deletes a stack. |

| /stacks/{StackName}/{StackId}/abandon | DELETE | Discards a stack. |
|---|---|---|
| /stacks/preview | POST | Previews a stack. |

Table 2. Resource operations

| URI | Method | Description |
|---|---|---|
| /stacks/{StackName}/{StackId}/resources | GET | Queries the list of stacks. |
| /stacks/{StackName}/{StackId}/resources/{ResourceNa me} | GET | Queries information about a stack. |
| /resource types _ | GET | Queries the list of resource types. |
| /resource types/{TypeName} _ | GET | Queries information about resource types. |
| /resource types/{TypeName}/template _ | GET | Queries information about resource type-specific templates. |

Table 3. Template operations

| URI | Method | Description |
|---|---|---|
| /stacks/{StackName}/{StackId}/template | GET | Queries information about a template. |
| /validate | POST | Validates information about a template. |

Table 4. Other operations

| URI | Method | Description |
|---|---|---|
| /stacks/{StackName}/{StackId}/events | GET | Queries the event list. |
| /regions | GET | Queries the region list. |

#### 1.1.3 Make API requests

##### 1.1.3.1 Overview

To send an API request, you must send an HTTP or HTTPS request to the service endpoint. You must add the request parameters that correspond to the API operation being called. After you call the API, the system returns a response.

##### 1.1.3.2 Request structure

This topic describes the request structure of the request method.

**Endpoints**

The endpoint of the ROS API is `ros.example.com` .

**Protocols**

Requests over HTTP or HTTPS are supported. We recommend that you use HTTPS for enhanced security.

**Methods**

Read-only access (ROA) is supported over HTTP or HTTPS.

**Encoding**

All requests and responses are encoded in UTF-8.

##### 1.1.3.3 Common parameters

This topic describes the common request and response parameters.

**Common request parameters**

Common request parameters must be included in all API requests. Examples

```
POST http://ros.example.com/stacks HTTP/1.1 x-acs-signature-method: HMAC-SHA1 Authorization: acs <AccessKeyId>:<signature> Date: Fri, 11 Sep 2015 05:28:47 GMT Content-MD5: 4eCVDLNDI0GRJMiZ6mLm**** x-acs-signature-version: 1.0 Accept: application/octet-stream Content-Type: application/json;charset=utf-8 x-acs-version: 2015-09-01 Cache-Control: no-cache Pragma: no-cache x-acs-region-id:cn-beijing Host: ros.example.com Connection: keep-alive Content-Length: 502
```

**Common response parameters**

Every response returns a unique X-Acs-Request-Id in the header regardless of whether the call is successful. If the response shows an error, provide the X-Acs-Request-Id to the technical support engineers for troubleshooting. Examples

```
HTTP/1.1 201 Created Date: Fri, 11 Sep 2015 05:28:48 GMT Content-Type: application/json Content-Length: 155 Connection: close Access-Control-Allow-Origin: * Access-Control-Allow-Methods: POST, GET, OPTIONS Access-Control-Allow-Headers: X-Requested-With, X-Sequence, _aop_secret, _aop_signature Access-Control-Max-Age: 172800 X-Acs-Request-Id: 14E***E2-B**8-4**4-B**E-52*******66C Server: Jetty(7.2.2.v20101205) /* Return Result Data */
```

##### 1.1.3.4 Responses

This topic describes the responses returned after API operations are called. API responses use the HTTP response format: A 2xx status code indicates a successful call. A 4xx or 5xx status code indicates a failed call. Responses can be returned in either the JSON or XML format. The default response format is XML. An external system can configure parameters in a request to specify the format of the response data.

> **Note:** The sample responses in this topic are formatted for better readability. The actual responses are not formatted with line breaks or indentation.

**Sample success responses**

```
HTTP/1.1 201 Created Date: Fri, 11 Sep 2015 05:28:48 GMT Content-Type: application/json Content-Length: 155 Connection: close Access-Control-Allow-Origin: * Access-Control-Allow-Methods: POST, GET, OPTIONS Access-Control-Allow-Headers: X-Requested-With, X-Sequence, _aop_secret, _aop_signature Access-Control-Max-Age: 172800 X-Acs-Request-Id: 14******2-B**8-4**4-B**E-5*********6C Server: Jetty(7.2.2.v20101205)
```

`{`

```json
    "Id":"b****c3c-4**4-4**7-a**5-c3******8316",
    "Name":"myStack"
```

`}`

**Sample error responses**

```
HTTP/1.1 409 Conflict Content-Type: application/json; charset=UTF-8 Content-Length: 79 Date: Fri, 13 Nov 2015 08:06:46 GMT
```

`{`

```json
    "Message" : "The Stack (test_link_044) already exists.",
    "Code" : "StackExists"
```

`}`

**Common errors**

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| MissingParamete r | The input parameter "Action" that is mandatory for processing this request is not supplied. | 400 | The error message returned because the Action parameter is missing. |

##### 1.1.3.5 Request signatures

This topic describes the request signatures. A resource-oriented architecture (ROA) style signature consists of two parts: common request header and CanonicalizedResource. The message body is not included in the signature. The common request header contains HTTP header parameters and Alibaba Cloud protocol header parameters.

**Common request headers**

| Header | Description |
|---|---|
| Authorization | The authentication information that is used to check the request validity, in the acs AccessKeyId:signature format. |
| Content-Length | The HTTP request content length defined in RFC 2616. |
| Content-Type | The HTTP request content type defined in RFC 2616. |
| Content-MD5 | The Base64-encoded 128-bit MD5 hash value of the HTTP message body. We recommend that you specify this parameter for all requests to prevent request tampering. |
| Date | The date and time of the request in GMT format. Example: Wed, 26 Aug. 2015 17:01:00 GMT. |
| Accept | The response type required by the client, which can be application/json or application/xml. |
| Host | The target host of the request. Example: ros.example.com. |

| x-acs-signature- nonce | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |
|---|---|
| x-acs-signature- method | The encryption method of the signature string. Set the value to HMAC-SHA1. |
| x-acs-signature- version | The version of the signature encryption algorithm. Set the value to 1.0. |

**Signature calculation method**

ROA-style API requests are signed using the standard Authorization header. The request syntax is as follows:

```
Authorization: acs AccessKeyId:Signature
```

**Signature calculation for common request headers**

HTTP headers The signature calculation must contain the values of the following parameters (without keys): Accept, Content-MD5, Content-Type, and Date.

> **Note:** Content-Length is not included in the signature. Parameters must be sorted in order. If a parameter has no value, replace it with "\n".

Alibaba Cloud protocol headers (CanonicalizedHeaders) CanonicalizedHeaders are non-standard HTTP headers of Alibaba Cloud. They are parameters prefixed with "x-acs-" in a request. You can use the following method to construct CanonicalizedHeaders: i. Convert the names of all HTTP request headers prefixed with x-acs- into lowercase letters. For example, "X-acs-OSS-Meta-Name: TaoBao" is converted into "x-acs-oss-metaname: TaoBao". The name of the request header is not case-sensitive based on the specifications of Alibaba Cloud. However, we recommend that you use lowercase letters for such names. ii. If the value section of a common request header is too long, replace the \t, \n, \r, and \f separators with spaces. iii. Sort all HTTP request headers that are obtained from the preceding step in alphabetical order. iv. Delete any spaces on either side of a separator between each request header and content. For example: "x-acs-oss-meta-name: TaoBao,Alipay" is converted into "x-acsoss-meta-name:TaoBao,Alipay". v. Separate all headers and content with the "\n" separator to form the final CanonicalizedHeaders. How to include CanonicalizedResource and queryString in the signature CanonicalizedResource represents the specification description of the resource to be accessed. Sort sub-resources along with query in alphabetical order and separate them with ampersands (&) as the separator to generate a sub-resource string. The string consists of all parameters after the question mark (?). Example:

```
http://ros.example.com/stacks?na**=test_a**rt&status=COMPLETE
```

The sorting result is:

```
name=test_alert+"\n"+ status=COMPLETE
```

**Signature encapsulation**

```
Authorization = acs AccessKeyId + ":" + Signature Signature = Base64( HMAC-SHA1( AccessSecret, UTF-8-Encoding-Of( StringToSign) ) ) StringToSign =
```

HTTP headers

```
HTTP-Verb + "\n" +
    Accept + "\n" +
    Content-MD5 + "\n" +
    Content-Type + "\n" +
    Date + "\n" +
```

Alibaba Cloud protocol headers (CanonicalizedHeaders)

```
CanonicalizedHeaders +
```

How to include CanonicalizedResource and queryString in the signature

```
CanonicalizedResource
```

##### 1.1.3.6 Status code

This topic describes the HTTP status codes that are returned when API operations are called.

| HTTP status code | Description |
|---|---|
| 2XX | A 2xx status code indicates a successful call. |
| 4XX | A 4xx status code indicates a service error. |
| 5XX | A 5xx status code indicates a system error. |

#### 1.1.4 Stack operations

##### 1.1.4.1 Create a stack

You can call this operation to create a stack.

**Precautions**

A stack is created based on your specified template and its parameters. The template content that you submit must be included in the HTTP message body. You must specify the stack name. After the stack is created, the system returns a unique stack ID that is used in subsequent operations. Stacks are distinguished by their user ID. Therefore, each stack created with the same user ID in the same region must have a unique name. The stack name cannot be changed after the stack is created. The stack cannot be moved to another account. The region where the stack is created must be specified in the x-acs-region-id header. The stack and resources in it must reside within the same region.

**Request parameters**

| Parameter | Positi on | Type | Requir ed | Description |
|---|---|---|---|---|
| x-acs-region- id | heade r | String | Yes | The region ID of the stack to be created. |
| Name | body | String | Yes | The name of the stack. It must comply with the ^[a- zA-Z][a-zA-Z0-9 .-]*$ regular expression and can _ contain up to 255 characters in length. |
| Template | body | JSON | Yes | The template of the stack, in the JSON format. The maximum size of the template is 512 KB. The value of this parameter is adjustable. |
| Parameters | body | JSON | Yes | The parameters required to create the stack. The key of each parameter in the Parameters segment must be defined in the template. |
| DisableRollb ack | body | Boole an | No | Specifies whether rollback on stack creation failure is disabled. Valid values: True: disables rollback on stack creation failure. False: enables rollback on stack creation failure. |
| TimeoutMins | body | Integ er | Yes | The timeout period that is specified for the stack creation request. Unit: minutes. Default value: 60. |

|   | zA-Z][a-zA-Z0-9 .-]*$ _ |
|---|---|

**Response parameters**

| Parameter | Type | Description |
|---|---|---|
| Id | String | The unique ID of the stack. |
| Name | String | The name of the stack. |

**Error codes**

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| InternalError | Server error | 500 | The error message returned because an internal server error has occurred. |

| NotSupported | %(feature)s is not supported | 404 | The error message returned because the specified parameter is not supported. |
|---|---|---|---|
| InvalidTemplateVersi on | Template version was not provided. | 400 | The error message returned because the specified template version number does not exist. |
| InvalidTemplateVersi on | Ambiguous versions (%s). | 400 | The error message returned because the specified template version number does not exist. |
| InvalidTemplateSecti on | The Parameter (%(key)s) has no attributes. | 400 | The error message returned because the specified template attributes are invalid. |
| StackValidationFaile d | Each Resource must contain a Type key. | 400 | The error message returned because the specified resource does not contain the Type attribute. |
| StackValidationFaile d | Resources must contain Resource.Found a [%s] instead. | 400 | The error message returned because Resources does not contain any resources. |
| StackValidationFaile d | Invalid deletion policy "%s". | 400 | The error message returned because the specified deletion policy does not exist. |
| StackValidationFaile d | "%s" deletion policy not supported. | 400 | The error message returned because the specified deletion policy does not exist. |
| StackValidationFaile d | Unknown Property %s. | 400 | The error message returned because the specified property is unknown. |
| InvalidSchemaError | Property %(prop)s: % (ua)s and %(im)s cannot both be True. | 400 | The error message returned because the specified template format is invalid. |

**Examples**

Sample requests

```
POST http://ros.example.com/stacks HTTP/1.1 x-acs-signature-method: HMAC-SHA1 Authorization: acs <AccessKeyId>:<signature> Date: Fri, 11 Sep 2015 05:28:47 GMT Content-MD5: 4eCVDLNDI0GRJMiZ6mLmgw== x-acs-signature-version: 1.0 Accept: application/octet-stream Content-Type: application/json;charset=utf-8 x-acs-version: 2015-09-01 Cache-Control: no-cache Pragma: no-cache x-acs-region-id:cn-beijing Host: ros.example.com Connection: keep-alive Content-Length: 502
```

`{`

```json
  "Name": "<stack name>",
  "Parameters":
```

`{`

```json
    "key": "value"
```

`},`

```json
  "Template":<template text>,
  "DisableRollback": true,
  "TimeoutMins": 15
```

`}` Sample responses

```
HTTP/1.1 201 Created Date: Fri, 11 Sep 2015 05:28:48 GMT Content-Type: application/json Content-Length: 155 Connection: close Access-Control-Allow-Origin: * Access-Control-Allow-Methods: POST, GET, OPTIONS Access-Control-Allow-Headers: X-Requested-With, X-Sequence, _aop_secret, _aop_signature Access-Control-Max-Age: 172800 X-Acs-Request-Id: 14*****2-B**8-4**4-B**E-5********66C Server: Jetty(7.2.2.v20101205)
```

`{`

```json
    "Id":"b4****3c-4**4-4**7-a**5-c3********16",
    "Name":"m***ack"
```

`}`

##### 1.1.4.2 Delete a stack

You can call this operation to delete a stack and all the resources in the stack.

**Request parameters**

| Parame ter | Locat ion | Type | Require d | Description |
|---|---|---|---|---|
| x-acs- region-id | heade r | String | Yes | The region ID of the stack. |
| StackNa me | URI | String | Yes | The stack name. The name must comply with the ^[a- zA-Z][a-zA-Z0-9 .-]*$ regular expression. _ |
| StackId | URI | String | Yes | The stack ID. |

|   | zA-Z][a-zA-Z0-9 .-]*$ _ |
|---|---|

**Response parameters**

None.

**Error codes**

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| InternalError | Server error | 500 | An unknown server error occurred. |
| StackNotFound | The Stack %(stack name)s could not _ be found. | 404 | The stack does not exist. |
| ActionInProgress | Stack %(stack name)s already has _ an action (%(action)s) in progress. | 409 | The stack has an action in progress. Try again later. |
| StopActionFailed | Failed to stop stack (% (stack name)s) on other engine (% _ (engine id)s) _ | 404 | Failed to delete the stack because a process is running on the stack and cannot be stopped. |

**Examples**

Sample requests

```
DELETE http://ros.example.com/stacks/myStack/28087440-3701-40ef-bbe8-6e80787d307f HTTP/
```

### 1.1 文档标题缺失，请补全后重新导出

```
x-acs-signature-method: HMAC-SHA1 Authorization: acs ACSTQDkNtSMrZtwL:3TCZAbfoSw8bpVeg/X5Uag1KgM8= Date: Fri, 11 Sep 2015 05:30:02 GMT x-acs-signature-version: 1.0 x-sdk-client: Java/2.0.0 Accept: application/octet-stream x-acs-version: 2015-09-01 Cache-Control: no-cache Pragma: no-cache User-Agent: Java/1.6.0_27 Host: ros.example.com Connection: keep-alive x-acs-region-id:cn-beijing
```

Sample responses

```
HTTP/1.1 204 No Content Date: Fri, 11 Sep 2015 05:29:18 GMT Content-Type: application/json; charset=UTF-8 Content-Length: 521 Connection: close Access-Control-Allow-Origin: * Access-Control-Allow-Methods: POST, GET, OPTIONS Access-Control-Allow-Headers: X-Requested-With, X-Sequence, _aop_secret, _aop_signature Access-Control-Max-Age: 172800 X-Acs-Request-Id: 8*****A8-2**0-4**E-9**4-4********342 Server: Jetty(7.2.2.v20101205)
```

##### 1.1.4.3 Discard a stack

You can call this operation to discard a stack but retain all resources in the stack.

**Request parameters**

| Paramet er | Locati on | Type | Require d | Description |
|---|---|---|---|---|
| x-acs- region-id | header | String | Yes | The region ID of the stack. |
| StackNam e | URI | String | Yes | The stack name. The name can be up to 255 characters in length, and must comply with the ^[a- zA-Z][a-zA-Z0-9 .-]*$ regular expression. _ |
| StackId | URI | String | Yes | The stack ID. |

|   | zA-Z][a-zA-Z0-9 .-]*$ _ |
|---|---|

**Response parameters**

| Parameter | Type | Description |
|---|---|---|
| Id | String | The stack ID. |
| Name | String | The stack name. |
| Action | String | The operation that was performed. |
| Status | String | The state. |
| Template | Json | The template. |
| Resources | Json | The resources. |
| Environment | Json | The environment. |

**Error codes**

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| InternalError | Server error | 500 | An unknown server error occurred. |
| StackNotFound | The Stack (% (stack name)s) could _ not be found. | 404 | The specified stack does not exist. |

**Examples**

Sample requests

```
DELETE http://ros.example.com/stacks/myStack/28087440-3701-40ef-bbe8- 6e80787d307f/abandon HTTP/1.1 x-acs-signature-method: HMAC-SHA1 Authorization: acs ACSTQDkNtSMrZtwL:3TCZAbfoSw8bpVeg/X5Uag1KgM8= Date: Fri, 11 Sep 2015 05:30:02 GMT x-acs-signature-version: 1.0 x-sdk-client: Java/2.0.0 Accept: application/octet-stream x-acs-version: 2015-09-01 Cache-Control: no-cache Pragma: no-cache User-Agent: Java/1.6.0_27 Host: ros.example.com Connection: keep-alive x-acs-region-id:cn-beijing
```

Sample responses

```
HTTP/1.1 200 OK Date: Fri, 11 Sep 2015 05:29:18 GMT Content-Type: application/json; charset=UTF-8 Content-Length: 521 Connection: close Access-Control-Allow-Origin: * Access-Control-Allow-Methods: POST, GET, OPTIONS Access-Control-Allow-Headers: X-Requested-With, X-Sequence, _aop_secret, _aop_signature Access-Control-Max-Age: 172800 X-Acs-Request-Id: 8****0A8-2**0-4**E-9**4-4********342 Server: Jetty(7.2.2.v20101205)
```

`{`

```json
    "Status" : "COMPLETE",
    "Name" : "test",
    "Environment" : {
        "parameter_defaults" : {},
        "parameters" : {},
        "resource_registry" : {
            "resources" : {}
```

`}` `},`

```json
    "Template" : {
        "Outputs" : {
            "secret1_v" : {
                "Description" : "secret1",
                "Value" : {
                    "get_attr" : ["secret1", "value"]
```

`}` `}` `},`

```json
        "Resources" : {
            "secret1" : {
"Type":"ALIYUN::RandomString"
```

```
                Type : ALIYUN::RandomString
```

`},`

```json
            "securet3" : {
                "Type" : "ALIYUN::RandomString",
                "Properties" : {
                    "length" : 100,
                    "sequence" : "octdigits"
```

`}` `},`

```json
            "securet2" : {
                "Type" : "ALIYUN::RandomString",
                "Properties" : {
                    "length" : 10
```

`}` `}` `},`

```json
        "ROSTemplateFormatVersion" : "2015-09-01"
```

`},`

```json
    "Action" : "CREATE",
    "Id" : "698ac08a-239d-4f2c-9609-af********31",
    "Resources" : {
        "secret1" : {
            "status" : "COMPLETE",
            "name" : "secret1",
            "resource_data" : {
                "value" : "ccsE2UZXxWX4oqu0lUpFqaZFulSc70jx"
```

`},`

```json
            "resource_id" : "test-secret1-x7********fw",
            "action" : "CREATE",
            "type" : "ALIYUN::RandomString",
            "metadata" : {}
```

`},`

```json
        "securet3" : {
            "status" : "COMPLETE",
            "name" : "securet3",
            "resource_data" : {
                "value" : "asfdasdf"
```

`},`

```json
            "resource_id" : "test-securet3-h********erg",
            "action" : "CREATE",
            "type" : "ALIYUN::RandomString",
            "metadata" : {}
```

`},`

```json
        "securet2" : {
            "status" : "COMPLETE",
            "name" : "securet2",
            "resource_data" : {
                "value" : "qGOkT6QX61"
```

`},`

```json
            "resource_id" : "test-securet2-x********dw6",
            "action" : "CREATE",
            "type" : "ALIYUN::RandomString",
            "metadata" : {}
```

```
etadata :{}
```

`}`

##### 1.1.4.4 Query stacks

You can call this operation to query stacks.

**Request parameters**

| Parameter | Locati on | Type | Requi red | Description |
|---|---|---|---|---|
| x-acs-region-id | header | String | Yes | The ID of the region where you want to query stacks. |
| StackId | Query | String | No | The stack ID. |
| Name | Query | String | No | The stack name. The name can be up to 255 characters in length, and must comply with the ^[a-zA-Z][a-zA-Z0-9 .-]*$ _ regular expression. |
| Status | Query | String | No | The state of the stack. You can use this parameter to filter stacks. Valid values: CREATE COMPLETE _ CREATE FAILED _ CREATE IN PROGRESS _ _ DELETE FAILED _ DELETE IN PROGRESS _ _ ROLLBACK COMPLETE _ ROLLBACK FAILED _ ROLLBACK IN PROGRESS _ _ |
| PageNumber | Query | Integer | No | The number of the page to return. Pages start from page 1. Default value: 1. |
| PageSize | Query | Integer | No | The number of entries to return on each page. Maximum value: 100. Default value: 10. |

**Response parameters**

| Parameter | Type | Description |
|---|---|---|
| TotalCount | Integer | The total number of stacks. |
| PageNumber | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| Stacks | List | The stacks. The Stack table in the following section describes the specific fields. |

Table 1: Stack

| Field | Type | Description |
|---|---|---|
| Region | String | The region ID of the stack. |
| Id | String | The stack ID. |
| Name | String | The stack name. |
| Updated | String | The time when the stack was updated. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC. |
| Created | String | The time when the stack was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC. |
| StatusReason | String | The reason why the stack is in its current state. |
| Status | String | The state of the stack. Valid values: CREATE COMPLETE _ CREATE FAILED _ CREATE IN PROGRESS _ _ DELETE FAILED _ DELETE IN PROGRESS _ _ ROLLBACK COMPLETE _ ROLLBACK FAILED _ ROLLBACK IN PROGRESS _ _ |

| g | 8601 |
|---|---|

| Description | String | The description of the stack. |
|---|---|---|
| DisableRollback | Boolea n | Indicates whether rollback is disabled when the stack fails to be created. Valid values: true false |
| TimeoutMins | Integer | The timeout period that is allowed to create the stack. Unit: minutes. |

**Error codes**

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| InternalError | Server error | 500 | An internal error occurred on the server. |
| StackNotFound | The Stack (% (stack name)s) could _ not be found. | 404 | The specified stack does not exist. |

**Examples**

Sample requests

```
GET http://ros.example.com/stacks HTTP/1.1 x-acs-signature-method: HMAC-SHA1 Authorization: acs ACSTQDkNtSMrZtwL:E9tMDBiLOywWyO1NJubGXV2Dq08= Date: Fri, 11 Sep 2015 05:28:05 GMT x-acs-signature-version: 1.0 x-sdk-client: Java/2.0.0 Accept: application/octet-stream x-acs-version: 2015-09-01 Cache-Control: no-cache Pragma: no-cache Host: ros.example.com Connection: keep-alive x-acs-region-id:cn-beijing
```

Sample responses

```
HTTP/1.1 200 OK Date: Fri, 11 Sep 2015 05:28:06 GMT Content-Type: application/json; charset=UTF-8 Content-Length: 945 Connection: close Access-Control-Allow-Origin: * Access-Control-Allow-Methods: POST, GET, OPTIONS Access-Control-Allow-Headers: X-Requested-With, X-Sequence, _aop_secret, _aop_signature Access-Control-Max-Age: 172800 X-Acs-Request-Id: 1******F-0**4-4**B-9**4-E********964
```

`{`

```json
  "TotalCount" : 5,
  "PageNumber" : 1,
  "Stacks" : [{
      "Status" : "CREATE_COMPLETE",
      "Updated" : null,
      "Description" : "No description",
      "Created" : "2015-10-23T07:54:29",
      "Region" : "cn-beijing",
      "StatusReason" : "Stack CREATE completed successfully",
      "DisableRollback" : true,
      "TimeoutMins" : 15,
      "Id" : "2669808f-c5e1-4777-85b9-5a2a3971*****",
      "Name" : "hope_test_chinese"
    }, {
      "Status" : "CREATE_COMPLETE",
      "Updated" : null,
      "Description" : "No description",
      "Created" : "2015-10-23T05:17:59",
      "Region" : "cn-beijing",
      "StatusReason" : "Stack CREATE completed successfully",
      "DisableRollback" : true,
      "TimeoutMins" : 15,
      "Id" : "4******d-c**c-4**e-b**b-d********8f45",
      "Name" : "hope_test_Scalin****up"
```

`}` `],`

```json
  "PageSize" : 2
```

`}`

##### 1.1.4.5 Query the information about a stack

You can call this operation to query the information about a stack.

**Request parameters**

| Parameter | Locati on | Type | Requi red | Description |
|---|---|---|---|---|

| x-acs-region-id | header | String | Yes | The region ID of the stack. |
|---|---|---|---|---|
| StackName | URI | String | Yes | The stack name. The name can be up to 255 characters in length, and must comply with the ^[a-zA-Z][a-zA-Z0-9 .-]*$ _ regular expression. |
| StackId | URI | String | Yes | The stack ID. |

**Response parameters**

| Parameter | Type | Description |
|---|---|---|
| Parameters | JSON | The collection of stack parameters. The value is in the JSON format. |
| Id | String | The stack ID. |
| Region | String | The region ID of the stack. |
| Name | String | The stack name. |
| Updated | String | The time when the stack was updated. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC. |
| Created | String | The time when the stack was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC. |
| TemplateDescrip tion | String | The description of the stack. |
| StatusReason | String | The reason why the stack is in its current state. |

| Status | String | The state of the stack. Valid values: CREATE COMPLETE _ CREATE FAILED _ CREATE IN PROGRESS _ _ DELETE FAILED _ DELETE IN PROGRESS _ _ ROLLBACK COMPLETE _ ROLLBACK FAILED _ ROLLBACK IN PROGRESS _ _ |
|---|---|---|
| Outputs | List | The outputs. |
| DisableRollback | Boolean | Indicates whether rollback is disabled when the stack fails to be created. Valid values: true false |
| TimeoutMins | Integer | The timeout period that is allowed to create the stack. Unit: minutes. Default value: 60. |

**Error codes**

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| InternalError | Server error | 500 | An unknown server error occurred. |
| StackNotFound | The Stack (%(stack name)s) _ could not be found. | 404 | The stack does not exist. |
| InvalidParameter | The specified parameter % (parameter)s is not valid. | 400 | The parameter is invalid. |

**Examples**

Sample requests

```
GET http://ros.example.com/stacks/myStack/378826b1-a71b-4c14-aa91-9b36351fbea9 HTTP/1.1 x-acs-signature-method: HMAC-SHA1 Authorization: acs ACSTQDkNtSMrZtwL:QnReVdih0pYK5MpRJwjIhCYsssY= Date: Fri, 11 Sep 2015 05:29:18 GMT x-acs-signature-version: 1.0 x-sdk-client: Java/2.0.0 Accept: application/octet-stream x-acs-version: 2015-09-01 Cache-Control: no-cache Pragma: no-cache User-Agent: Java/1.6.0_27 Host: ros.example.com Connection: keep-alive x-acs-region-id:cn-beijing
```

Sample responses

```
HTTP/1.1 200 OK Date: Fri, 11 Sep 2015 05:29:18 GMT Content-Type: application/json; charset=UTF-8 Content-Length: 521 Connection: close Access-Control-Allow-Origin: * Access-Control-Allow-Methods: POST, GET, OPTIONS Access-Control-Allow-Headers: X-Requested-With, X-Sequence, _aop_secret, _aop_signature Access-Control-Max-Age: 172800 X-Acs-Request-Id: 8******8-2**0-4**E-9**4-4********342 Server: Jetty(7.2.2.v20101205)
```

`{`

```json
    "Id" : "378826b1-a71b-4c14-aa91-9b36351f****",
    "Updated" : null,
    "DisableRollback" : true,
    "TimeoutMins" : 15,
    "TemplateDescription" : "No description",
    "StatusReason" : "Stack CREATE completed successfully",
    "Created" : "2015-09-11T07:38:03Z",
    "Region" : "cn-beijing",
    "Status" : "CREATE_COMPLETE",
    "Name" : "myStack",
    "Outputs" :
```

`[{`

```json
            "output_key" : "secr***_v",
            "description" : "secret1",
            "output_value" : {
                "get_attr" :
```

`[`

```
                    "secret1",
                    "value"
```

`]` `}` `}` `],`

```json
    "Parameters" : {
        "ALIYUN::StackId" : "3********1-a**b-4**4-a**1-9********ea9",
        "ALIYUN::StackName" : "m****ck"
```

`}` `}`

##### 1.1.4.6 Preview a stack

You can call this operation to preview the information about a stack that you want to create by using a template.

**Request parameters**

| Para mete r | Locat ion | Type | Requir ed | Description |
|---|---|---|---|---|
| x-acs- regio n-id | heade r | String | Yes | The region ID of the stack. |
| Name | body | String | Yes | The stack name. The name can be up to 255 characters in length, and must comply with the ^[a-zA-Z][a-zA-Z0-9 .-]*$ _ regular expression. |
| Templ ate | body | JSON | Yes | The template in the JSON format. The template can be up to 512 KB in length. The value of this parameter is adjustable. |

**Response parameters**

| Parameter | Type | Description |
|---|---|---|
| Description | String | The description of the stack. |
| Updated | String | The update time. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC. |
| Parameters | JSON | The collection of stack parameters. The value is in the JSON format. |
| Created | String | The creation time. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC. |
| Region | String | The region ID of the stack. |
| TemplateDescripti on | String | The description of the template. |
| Webhook | String | The custom callback function. |
| Id | String | The stack ID. |
| Resources | JSON | The collection of resources in the stack. The value is in the JSON format. |
| Name | String | The stack name. |

**Error codes**

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| InternalError | Server error | 500 | An unknown server error occurred. |
| NotSupported | %(feature)s is not supported | 404 | The parameter is not supported. |
| InvalidTemplateVers ion | Template version was not provided. | 400 | The template version number is invalid. |
| InvalidTemplateVers ion | Ambiguous versions (%s). | 400 | The template version number is invalid. |
| InvalidTemplateSect ion | The Parameter (%(key)s) has no attributes. | 400 | The template attributes are invalid. |
| StackValidationFaile d | Each Resource must contain a Type key. | 400 | The resource does not contain the Type property. |
| StackValidationFaile d | Resources must contain Resource. Found a [%s] instead. | 400 | The Resources section does not contain resources. |
| StackValidationFaile d | Invalid deletion policy "%s". | 400 | The deletion policy is invalid. |
| StackValidationFaile d | "%s" deletion policy not supported. | 400 | The deletion policy is invalid. |
| StackValidationFaile d | Unknown Property %s. | 400 | The property is unknown. |
| InvalidSchemaError | Property %(prop)s: %(ua)s and % (im)s cannot both be True. | 400 | The template format is invalid. |

**Examples**

Sample requests

```
POST http://ros.example.com/stacks/preview HTTP/1.1 x-acs-signature-method: HMAC-SHA1 Authorization: acs <AccessKeyId>:<signature> Date: Fri, 11 Sep 2015 05:28:47 GMT Content-MD5: 4eCVDLNDI0GRJMiZ6mLmgw== x-acs-signature-version: 1.0 Accept: application/octet-stream Content-Type: application/json;charset=utf-8 x-acs-version: 2015-09-01 Cache-Control: no-cache Pragma: no-cache x-acs-region-id:cn-beijing Host: ros.example.com Connection: keep-alive Content-Length: 502
```

`{`

```json
  "Name": "<stack name>",
  "Parameters":
```

`{`

```json
    "key": "value"
```

`},`

```json
  "Template":<template text>,
  "DisableRollback": true,
  "TimeoutMins": 15
```

`}` Sample responses

```
HTTP/1.1 201 Created Date: Fri, 11 Sep 2015 05:28:48 GMT Content-Type: application/json Content-Length: 155 Connection: close Access-Control-Allow-Origin: * Access-Control-Allow-Methods: POST, GET, OPTIONS Access-Control-Allow-Headers: X-Requested-With, X-Sequence, _aop_secret, _aop_signature Access-Control-Max-Age: 172800 X-Acs-Request-Id: 1*****E2-B**8-4**4-B**E-5********66C Server: Jetty(7.2.2.v20101205)
```

`{`

```json
    "Updated":null,
    "Description":"No description",
    "Parameters":{
        "ALIYUN::StackId":"None",
        "ALIYUN::StackName":"update_test_0040",
        "ALIYUN::Region":"cn-beijing"
```

`},`

```json
    "Created":"2017-01-17T07:01:10.437639",
    "Region":"cn-beijing",
    "TemplateDescription":"No description",
    "Webhook":null,
    "Id":"None",
```

```json
    "DisableRollback":false,
    "TimeoutMins":120,
    "Resources":[
```

`{`

```json
            "UpdatedTime":null,
            "StackIdentity":{
                "StackName":"update_test_0040",
                "StackId":"None",
                "Region":"cn-beijing",
                "Tenant":"1754580903499898",
                "Path":""
```

`},`

```json
            "ResourceStatus":"COMPLETE",
            "Description":"",
            "ResourceData":null,
            "ResourceStatusReason":"",
            "ResourceAction":"INIT",
            "PhysicalResourceId":"",
            "DeletedTime":null,
            "StackName":"update_test_0040",
            "ResourceType":"ALIYUN::ECS::InstanceGroupClone",
            "RequiredBy":[
```

`],`

```json
            "Attributes":{
                "OrderId":null,
                "InnerIps":null,
                "PrivateIps":null,
                "ZoneIds":null,
                "PublicIps":null,
                "InstanceIds":null
```

`},`

```json
            "CreatedTime":null,
            "ResourceName":"WebServer",
            "ResourceIdentity":{
                "StackName":"update_test_0040",
                "StackId":"None",
                "Region":"cn-beijing",
                "Tenant":"1754580903499898",
                "Path":"/resources/WebServer"
```

`},`

```json
            "Properties":{
                "AutoReleaseTime":null,
                "DiskMappings":null,
                "LoadBalancerIdToAttach":null,
                "Description":null,
                "BackendServerWeight":100,
                "Tags":null,
                "MinAmount":1,
                "SecurityGroupId":null,
                "ZoneId":null,
                "InternetMaxBandwidthOut":null,
                "ImageId":null,
                "SourceInstanceId":"i-2********m597****jhr",
                "Password":"Test1234",
```

`"` `"` `ll`

```json
                "InstanceName":null,
                "MaxAmount":1
```

`},`

```json
            "Metadata":{
```

`}` `}` `],`

```json
    "Name":"upda**_test_0040"
```

`}`

##### 1.1.4.7 Update a stack

You can call this operation to update a stack by specifying the name, ID, new template, and parameters of the stack.

**Precautions**

The template content that you submit must be included in the HTTP message body. The system identifies the stack to be updated based on the name and ID of the stack. After comparing the original template with the new one, the system updates resources included in both templates based on the comparison results. If the new template has a new resource that does not exist in the original template, the system adds the new resource to the stack. If a resource that exists in the original template has been removed in the new template, the system removes the resource from the stack. If the resource attribute of the original template is modified in the new template, the resource attribute is updated. The system only updates the resource attributes that can be updated. Otherwise, an error is returned. The stack name cannot be updated. If rollback on stack update failure is enabled, the stack is restored to its original status after the stack fails to be updated. The region where the stack is created must be specified in the x-acs-region-id format.

**Request parameters**

| Parameter | Pos itio n | Type | Requir ed | Description |
|---|---|---|---|---|
| x-acs-region- id | hea der | String | Yes | The region where the stack resides. |
| StackName | URI | String | Yes | The name of the stack. It must comply with the ^[a-zA- Z][a-zA-Z0-9 .-]*$ regular expression and can contain _ up to 255 characters in length. |
| StackId | URI | String | Yes | The ID of the stack. |
| Template | bod y | JSON | Yes | The template of the stack, in the JSON format. The maximum size of the template is 512 KB. The value of this parameter is adjustable. |

| Parameters | bod y | JSON | Yes | The parameters required to update the stack. The keys are defined in the template. |
|---|---|---|---|---|
| DisableRollba ck | bod y | Boole an | No | Specifies whether rollback on stack update failure is disabled. Valid values: True: disables rollback on stack update failure. False: enables rollback on stack update failure. |
| TimeoutMins | bod y | Intege r | Yes | The timeout period that is specified for the stack update request. Unit: minutes. Default value: 60. |

**Response parameters**

| Parameter | Type | Description |
|---|---|---|
| Id | String | The ID of the stack. |
| Name | String | The name of the stack. |

**Error codes**

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| InternalError | Server error | 500 | The error message returned because an internal server error has occurred. |
| NotSupported | %(feature)s is not supported | 404 | The error message returned because the specified parameter is not supported. |
| InvalidTemplateVers ion | Template version was not provided. | 400 | The error message returned because the specified template version number is invalid. |
| InvalidTemplateVers ion | Ambiguous versions (%s). | 400 | The error message returned because the specified template version number is invalid. |
| InvalidTemplateSect ion | The Parameter (%(key)s) has no attributes. | 400 | The error message returned because the specified template attributes do not exist. |
| StackValidationFaile d | Each Resource must contain a Type key. | 400 | The error message returned because the specified resource does not contain the Type attribute. |

| StackValidationFaile d | Resources must contain Resource. Found a [%s] instead. | 400 | The error message returned because Resources does not contain any resources. |
|---|---|---|---|
| StackValidationFaile d | Invalid deletion policy "%s". | 400 | The error message returned because the deletion policy is invalid. |
| StackValidationFaile d | "%s" deletion policy not supported. | 400 | The error message returned because the deletion policy is invalid. |
| StackValidationFaile d | Unknown Property %s. | 400 | The error message returned because the specified property is unknown. |
| InvalidSchemaError | Property %(prop)s: %(ua)s and % (im)s cannot both be True. | 400 | The error message returned because the specified template format is invalid. |

**Examples**

Sample requests

```
PUT http://ros.example.com/stacks/myStack/28087440-3701-40ef-bbe8-6e80787d307f HTTP/1.1 x-acs-signature-method: HMAC-SHA1 Authorization: acs <AccessKeyId>:<signature> Date: Fri, 11 Sep 2015 05:28:47 GMT Content-MD5: 4eCVDLNDI0GRJMiZ6mLmgw== x-acs-signature-version: 1.0 Accept: application/octet-stream Content-Type: application/json;charset=utf-8 x-acs-version: 2015-09-01 Cache-Control: no-cache Pragma: no-cache x-acs-region-id:cn-beijing Host: ros.example.com Connection: keep-alive Content-Length: 502
```

`{`

```json
  "Parameters":
```

`{`

```json
    "key": "value"
```

`},`

```json
  "Template":<template text>,
  "DisableRollback": true,
  "TimeoutMins": 15
```

`}` Sample responses

```
HTTP/1.1 200 OK Date: Wed, 04 Jan 2017 08:13:24 GMT Content-Type: application/json Content-Length: 155 Connection: close Access-Control-Allow-Origin: * Access-Control-Allow-Methods: POST, GET, OPTIONS Access-Control-Allow-Headers: X-Requested-With, X-Sequence, _aop_secret, _aop_signature Access-Control-Max-Age: 172800 X-Acs-Request-Id: 1******2-B**8-4**4-B**E-5********66C Server: Jetty(7.2.2.v20101205)
```

`{`

```json
    "Id":"b******c-4**4-4**7-a**5-c********316",
    "Name":"myStack"
```

`}`

#### 1.1.5 Resource operations

##### 1.1.5.1 Query a list of resources

You can call this operation to query the list of resources in a stack.

**Request parameters**

| Parameter | Locati on | Type | Requi red | Description |
|---|---|---|---|---|
| x-acs-region-id | header | String | Yes | The region ID of the stack. |
| StackName | URI | String | No | The stack name. The name can be up to 255 characters in length, and must comply with the ^[a-zA-Z][a-zA-Z0-9 .-]*$ _ regular expression. |
| StackId | URI | String | No | The stack ID. |

**Response parameters**

The system returns the list of resources.

| Parameter | Type | Description |
|---|---|---|
| Name | String | The resource name. |
| Id | String | The resource ID. |

| Type | String | The resource type. |
|---|---|---|
| Status | String | The state of the resource. Valid values: CREATE COMPLETE _ CREATE FAILED _ CREATE IN PROGRESS _ _ DELETE FAILED _ DELETE IN PROGRESS _ _ ROLLBACK COMPLETE _ ROLLBACK FAILED _ ROLLBACK IN PROGRESS _ _ |
| StatusReaso n | String | The reason why the resource is in its current state. |
| Updated | String | The time when the resource was updated. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC. |
| PhysicalId | String | The physical ID of the resource. |

**Error codes**

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| InternalError | Server error | 500 | An unknown server error occurred. |
| StackNotFound | The Stack (%(stack name)s) could not _ be found. | 404 | The stack does not exist. |

**Examples**

Sample requests

```
GET http://ros.example.com/stacks/myStack/28087440-3701-40ef-bbe8- 6e80787d307f/resources HTTP/1.1 x-acs-signature-method: HMAC-SHA1 Authorization: acs ACSTQDkNtSMrZtwL:8xKxVMy4xi2zgXUNLERRiZbg**** Date: Fri, 11 Sep 2015 05:30:11 GMT x-acs-signature-version: 1.0 x-sdk-client: Java/2.0.0 Accept: application/octet-stream x-acs-version: 2015-09-01 Cache-Control: no-cache Pragma: no-cache User-Agent: Java/1.6.0_27 Host: ros.example.com Connection: keep-alive x-acs-region-id:cn-beijing
```

Sample responses

```
HTTP/1.1 200 OK Date: Fri, 11 Sep 2015 05:30:12 GMT Content-Type: application/json; charset=UTF-8 Content-Length: 1694 Connection: close Vary: Accept-Encoding Access-Control-Allow-Origin: * Access-Control-Allow-Methods: POST, GET, OPTIONS Access-Control-Allow-Headers: X-Requested-With, X-Sequence, _aop_secret, _aop_signature Access-Control-Max-Age: 172800 X-Acs-Request-Id: A******2-C**7-4**0-9**2-D********385 Server: Jetty(7.2.2.v20101205)
```

`[` `{`

```json
    "Status":"CREATE_COMPLETE",
    "Updated":"2015-09-11T07:38:03Z",
    "PhysicalId":"myStack-secret1-mfhzo5m*****",
    "Id":"sec***1",
    "Type":"ALIYUN::RandomString",
    "StatusReason":"state changed",
    "Name":"secret1"
```

`}` `]`

##### 1.1.5.2 Query the information about a resource

You can call this operation to query the information about a resource.

**Request parameters**

| Parameter | Loca tion | Type | Require d | Description |
|---|---|---|---|---|

| x-acs-region- id | head er | Strin g | Yes | The region ID of the stack that you want to query. |
|---|---|---|---|---|
| StackName | URI | Strin g | Yes | The stack name. The name can be up to 255 characters in length, and must comply with the ^[a-zA-Z][a-zA-Z0-9 .-]*$ regular _ expression. |
| StackId | URI | Strin g | Yes | The stack ID. |
| ResourceNam e | URI | Strin g | Yes | The resource name. |

**Response parameters**

| Parameter | Type | Description |
|---|---|---|
| Name | String | The resource name. |
| Id | String | The resource ID. |
| Type | String | The resource type. |
| Status | String | The state of the resource. Valid values: CREATE COMPLETE _ CREATE FAILED _ CREATE IN PROGRESS _ _ DELETE FAILED _ DELETE IN PROGRESS _ _ ROLLBACK COMPLETE _ ROLLBACK FAILED _ ROLLBACK IN PROGRESS _ _ |
| StatusReaso n | String | The reason why the resource is in its current state. |
| Updated | String | The time when the resource was updated. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC. |
| PhysicalId | String | The physical ID of the resource. |

**Error codes**

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| InternalError | Server error | 500 | An unknown server error occurred. |
| StackNotFound | The Stack (%(stack name)s) could not be _ found. | 404 | The stack does not exist. |
| ResourceNotFo und | The Resource (%(resource name)s) could _ not be found in Stack %(stack name)s. _ | 404 | The resource does not exist. |

**Examples**

Sample requests

```
GET http://ros.example.com/stacks/myStack/28087440-3701-40ef-bbe8- 6e80787d307f/resources/secret1 HTTP/1.1 x-acs-signature-method: HMAC-SHA1 Authorization: acs ACSTQDkNtSMrZtwL:niea/6wW/HHwwiafneHX+oM3**** Date: Fri, 11 Sep 2015 05:30:54 GMT x-acs-signature-version: 1.0 x-sdk-client: Java/2.0.0 Accept: application/octet-stream x-acs-version: 2015-09-01 Cache-Control: no-cache Pragma: no-cache User-Agent: Java/1.6.0_27 Host: ros.example.com Connection: keep-alive x-acs-region-id:cn-beijing
```

Sample responses

```
HTTP/1.1 200 OK Date: Fri, 11 Sep 2015 05:30:12 GMT Content-Type: application/json; charset=UTF-8 Content-Length: 1694 Connection: close Vary: Accept-Encoding Access-Control-Allow-Origin: * Access-Control-Allow-Methods: POST, GET, OPTIONS Access-Control-Allow-Headers: X-Requested-With, X-Sequence, _aop_secret, _aop_signature Access-Control-Max-Age: 172800 X-Acs-Request-Id: A******2-C**7-4**0-9**2-D********385 Server: Jetty(7.2.2.v20101205)
```

`{`

```json
    "Status":"CREATE_COMPLETE",
    "Updated":"2015-09-11T07:38:03Z",
    "PhysicalId":"myStack-secret1-mfhzo5m*****",
    "Id":"sec***1",
    "Type":"ALIYUN::RandomString",
    "StatusReason":"state changed",
    "Name":"secret1"
```

`}`

##### 1.1.5.3 Query resource types

You can call this operation to query supported resource types.

**Request parameters**

| Paramete r | Locati on | Typ e | Requir ed | Description |
|---|---|---|---|---|
| x-acs- region-id | heade r | Stri ng | Yes | The region ID of the stack. |
| SupportSta tus | Query | Stri ng | No | The supported state. You can use this parameter to filter resource types. Valid values: UNKNOWN SUPPORTED DEPRECATED UNSUPPORTED HIDDEN |

**Response parameters**

| Parameter | Type | Description |
|---|---|---|

| ResourceTypes | List | The resource types. |
|---|---|---|

**Error codes**

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| InternalError | Server error | 500 | An unknown server error occurred. |

**Examples**

Sample requests

```
GET http://ros.example.com/resource_types HTTP/1.1 x-acs-signature-method: HMAC-SHA1 Authorization: acs ACSTQDkNtSMrZtwL:niea/6wW/HHwwiafneHX+oM3**** Date: Fri, 11 Sep 2015 05:30:54 GMT x-acs-signature-version: 1.0 x-sdk-client: Java/2.0.0 Accept: application/octet-stream x-acs-version: 2015-09-01 Cache-Control: no-cache Pragma: no-cache User-Agent: Java/1.6.0_27 Host: ros.example.com Connection: keep-alive x-acs-region-id:cn-beijing
```

Sample responses

```
HTTP/1.1 200 OK Date: Fri, 11 Sep 2015 05:30:12 GMT Content-Type: application/json; charset=UTF-8 Content-Length: 1694 Connection: close Vary: Accept-Encoding Access-Control-Allow-Origin: * Access-Control-Allow-Methods: POST, GET, OPTIONS Access-Control-Allow-Headers: X-Requested-With, X-Sequence, _aop_secret, _aop_signature Access-Control-Max-Age: 172800 X-Acs-Request-Id: A******2-C**7-4**0-9**2-D********385 Server: Jetty(7.2.2.v20101205)
```

`{`

```json
  "ResourceTypes" : [
    "ALIYUN::SLB::Listener",
    "ALIYUN::ESS::ScalingConfiguration",
    "ALIYUN::ECS::VSwitch",
    "ALIYUN::KVSTORE::Instance",
    "ALIYUN::ECS::Route",
    "ALIYUN::SLB::LoadBalancer",
    "ALIYUN::ECS::DiskAttachment",
    "ALIYUN::ECS::SecurityGroupIngress",
    "ALIYUN::RDS::DBInstance",
    "ALIYUN::ECS::SecurityGroupEgress"
```

`]` `}`

##### 1.1.5.4 Query the information about a resource type

**type**

You can call this operation to query the information about a resource type.

**Request parameters**

| Parameter | Locatio n | Type | Required | Description |
|---|---|---|---|---|
| x-acs-region-id | header | String | Yes | The region ID of the stack that you want to query. |
| TypeName | URI | String | Yes | The name of the resource type. |

**Response parameters**

| Parameter | Type | Description |
|---|---|---|
| ResourceType | String | The resource type. |
| Attributes | Json | The resource attributes. |
| SupportStatus | Json | The state of the resource type. Valid values: UNKNOWN SUPPORTED DEPRECATED UNSUPPORTED HIDDEN |
| Properties | Json | The resource properties. |

**Error codes**

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| InternalError | Server error | 500 | An unknown server error occurred. |
| ResourceTypeNotFo und | The Resource Type (% (type name)s) could not be _ found. | 404 | The resource type is not found. |

**Examples**

Sample requests

```
GET http://ros.example.com/resource_types/ALIYUN::SLB::LoadBalancer HTTP/1.1 x-acs-signature-method: HMAC-SHA1 Authorization: acs ACSTQDkNtSMrZtwL:niea/6wW/HHwwiafneHX+oM3**** Date: Fri, 11 Sep 2015 05:30:54 GMT x-acs-signature-version: 1.0 x-sdk-client: Java/2.0.0 Accept: application/octet-stream x-acs-version: 2015-09-01 Cache-Control: no-cache Pragma: no-cache User-Agent: Java/1.6.0_27 Host: ros.example.com Connection: keep-alive x-acs-region-id:cn-beijing
```

Sample responses

```
HTTP/1.1 200 OK Date: Fri, 11 Sep 2015 05:30:12 GMT Content-Type: application/json; charset=UTF-8 Content-Length: 1694 Connection: close Vary: Accept-Encoding Access-Control-Allow-Origin: * Access-Control-Allow-Methods: POST, GET, OPTIONS Access-Control-Allow-Headers: X-Requested-With, X-Sequence, _aop_secret, _aop_signature Access-Control-Max-Age: 172800 X-Acs-Request-Id: A******2-C**7-4**0-9**2-D********385 Server: Jetty(7.2.2.v20101205)
```

`{`

```json
  "Attributes" : {
    "LoadBalancerId" : {
      "description" : "The id of load balance generated"
```

`}` `},`

```json
  "SupportStatus" : {
    "status" : "SUPPORTED",
    "message" : null,
    "version" : null
```

`},`

```json
  "ResourceType" : "ALIYUN::SLB::LoadBalancer",
  "Properties" : {
    "InternetChargeType" : {
      "update_allowed" : false,
      "immutable" : false,
      "constraints" : [
```

`{`

```json
          "allowed_values" : [
            "paybybandwidth",
            "paybytraffic"
```

`]` `],`

```json
"description":"Thechargingtypeofnetworkbilling"
```

```json
      description : The charging type of network billing.,
      "required" : false,
      "type" : "string"
```

`},`

```json
    "AddressType" : {
      "update_allowed" : false,
      "immutable" : false,
      "constraints" : [
```

`{`

```json
          "allowed_values" : [
            "internet",
            "intranet"
```

`]` `}` `],`

```json
      "description" : "The type of address.",
      "required" : false,
      "type" : "string"
```

`},`

```json
    "Bandwidth" : {
      "update_allowed" : false,
      "immutable" : false,
      "constraints" : [
```

`{`

```json
          "range" : {
            "max" : 1000,
            "min" : 1
```

`}` `}` `],`

```json
      "description" : "The bandwidth in Mbps of network.",
      "required" : false,
      "type" : "integer"
```

`},`

```json
    "VpcId" : {
      "update_allowed" : false,
      "immutable" : false,
      "type" : "string",
      "required" : false,
      "description" : "The id of virtual private cloud."
```

`},`

```json
    "VSwitchId" : {
      "update_allowed" : false,
      "immutable" : false,
      "type" : "string",
      "required" : false,
      "description" : "The id of software-based network switch."
```

`},`

```json
    "LoadBalancerName" : {
      "update_allowed" : false,
      "immutable" : false,
      "type" : "string",
      "required" : false,
      "description" : "The display name of load balance."
```

##### 1.1.5.5 Query the information about a resource type-specific template

**type-specific template**

You can call this operation to query the information about a template specific to a resource type.

**Request parameters**

| Parameter | Locatio n | Type | Required | Description |
|---|---|---|---|---|
| x-acs-region-id | header | String | Yes | The region ID of the stack that you want to create. |
| TypeName | URI | String | Yes | The name of the resource type. |

**Response parameters**

| Parameter | Type | Description |
|---|---|---|
| ROSTemplateFormatVersion | String | The version number of the template. |
| Parameters | Json | The parameters in the Parameters section of the template. The Parameters section defines the parameters that you must specify to create a stack based on the template. Each time you create a stack, you can use the parameters to specify custom information, such as the username, password, and environment-related Elastic Compute Service (ECS) instance type. |
| Outputs | Json | The outputs in the Outputs section of the template. The Outputs section defines the information that you want to obtain after the stack is created. |
| Resources | Json | The resources in the Resources section of the template. The Resources section provides the definitions of cloud resources that Resource Orchestration Service (ROS) deploys by using the template. Each resource is defined in a separate resource block. |

**Error codes**

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| InternalError | Server error | 500 | An unknown server error occurred. |
| ResourceTypeNotFo und | The Resource Type (% (type name)s) could not be found. _ | 404 | The resource type in not found. |

**Examples**

Sample requests

```
GET http://ros.example.com/resource_types/ALIYUN::SLB::LoadBalancer/template HTTP/1.1 x-acs-signature-method: HMAC-SHA1 Authorization: acs ACSTQDkNtSMrZtwL:niea/6wW/HHwwiafneHX+oM3**** Date: Fri, 11 Sep 2015 05:30:54 GMT x-acs-signature-version: 1.0 x-sdk-client: Java/2.0.0 Accept: application/octet-stream x-acs-version: 2015-09-01 Cache-Control: no-cache Pragma: no-cache User-Agent: Java/1.6.0_27 Host: ros.example.com Connection: keep-alive x-acs-region-id:cn-beijing
```

Sample responses

```
HTTP/1.1 200 OK Date: Fri, 11 Sep 2015 05:30:12 GMT Content-Type: application/json; charset=UTF-8 Content-Length: 1694 Connection: close Vary: Accept-Encoding Access-Control-Allow-Origin: * Access-Control-Allow-Methods: POST, GET, OPTIONS Access-Control-Allow-Headers: X-Requested-With, X-Sequence, _aop_secret, _aop_signature Access-Control-Max-Age: 172800 X-Acs-Request-Id: A******2-C**7-4**0-9**2-D********385 Server: Jetty(7.2.2.v20101205)
```

`{`

```json
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Parameters" : {
    "InternetChargeType" : {
      "AllowedValues" : [
        "paybybandwidth",
        "paybytraffic"
```

`],`

```json
      "Type" : "String",
      "Description" : "The charging type of network billing."
```

`},`

```json
    "AddressType" : {
      "AllowedValues" : [
        "internet",
        "intranet"
```

`],`

```json
      "Type" : "String",
      "Description" : "The type of address."
```

`},`

```json
    "Bandwidth" : {
      "Description" : "The bandwidth in Mbps of network.",
      "Type" : "Number",
      "MinValue" : 1,
      "MaxValue" : 1000
```

`},`

```json
    "VpcId" : {
      "Type" : "String",
      "Description" : "The id of virtual private cloud."
```

`},`

```json
    "VSwitchId" : {
      "Type" : "String",
      "Description" : "The id of software-based network switch."
```

`},`

```json
    "LoadBalancerName" : {
      "Type" : "String",
      "Description" : "The display name of load balance."
```

`}` `},`

```json
  "Outputs" : {
    "LoadBalancerId" : {
      "Value" : "{\"Fn::GetAtt\": [\"LoadBalance\", \"LoadBalancerId\"]}",
      "Description" : "The id of load balance generated"
```

`}` `},`

```json
  "Resources" : {
    "LoadBalance" : {
      "Type" : "ALIYUN::SLB::LoadBalancer",
      "Properties" : {
        "InternetChargeType" : {
          "Ref" : "InternetChargeType"
```

`},`

```json
        "AddressType" : {
          "Ref" : "AddressType"
```

`},`

```json
        "Bandwidth" : {
          "Ref" : "Bandwidth"
```

`},`

```json
        "VpcId" : {
          "Ref" : "VpcId"
```

`},`

```json
        "VSwitchId" : {
          "Ref" : "VSwitchId"
```

`},`

```json
        "LoadBalancerName" : {
          "Ref" : "LoadBalancerName"
```

`}` `}` `}` `}`

#### 1.1.6 Template operations

##### 1.1.6.1 Validate the information about a template

You can call this operation to validate the information about a stack template.

**Request parameters**

| Parameter | Location | Type | Required | Description |
|---|---|---|---|---|
| x-acs-region-id | header | Strin g | Yes | The region ID of the stack. |
| Template | Body | Json | Yes | The template that you want to validate. |

**Response parameters**

| Parameter | Type | Description |
|---|---|---|
| Parameters | Json | The parameters in the Parameters section of the template. The Parameters section defines the parameters that you must specify to create a stack based on the template. Each time you create a stack, you can use the parameters to specify custom information, such as the username, password, and environment-related Elastic Compute Service (ECS) instance type. |
| Description | Json | The description of the template. |

**Error codes**

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| InternalError | Server error | 500 | An unknown server error occurred. |

| InvalidTemplateVersion | Template version was not provided. | 400 | The template version is invalid. |
|---|---|---|---|
| InvalidTemplateVersion | Ambiguous versions (%s). | 400 | The template version is invalid. |
| InvalidTemplateSection | The Parameter (%(key)s) has no attributes. | 400 | The template attributes are invalid. |
| StackValidationFailed | Each Resource must contain a Type key. | 400 | The resource does not contain the Type property. |
| StackValidationFailed | Invalid deletion policy "%s". | 400 | The deletion policy is invalid. |
| StackValidationFailed | "%s" deletion policy not supported. | 400 | The deletion policy is invalid. |
| StackValidationFailed | Unknown Property %s. | 400 | The property is unknown. |
| InvalidSchemaError | Property %(prop)s: % (ua)s and %(im)s cannot both be True. | 400 | The template format is invalid. |

**Examples**

Sample requests

```
GET http://ros.example.com/validate HTTP/1.1 x-acs-signature-method: HMAC-SHA1 Authorization: acs ACSTQDkNtSMrZtwL:niea/6wW/HHwwiafneHX+oM3ALU= Date: Fri, 11 Sep 2015 05:30:54 GMT x-acs-signature-version: 1.0 x-sdk-client: Java/2.0.0 Accept: application/octet-stream x-acs-version: 2015-09-01 Cache-Control: no-cache Pragma: no-cache User-Agent: Java/1.6.0_27 Host: ros.example.com Connection: keep-alive x-acs-region-id:cn-beijing
```

`{`

```json
  "Template" : {
    "ROSTemplateFormatVersion" : "2015-09-01"
```

`}` `}` Sample responses

```
HTTP/1.1 200 OK Date: Fri, 11 Sep 2015 05:30:12 GMT Content-Type: application/json; charset=UTF-8 Content-Length: 1694 Connection: close Vary: Accept-Encoding Access-Control-Allow-Origin: * Access-Control-Allow-Methods: POST, GET, OPTIONS Access-Control-Allow-Headers: X-Requested-With, X-Sequence, _aop_secret, _aop_signature Access-Control-Max-Age: 172800 X-Acs-Request-Id: A******2-C**7-4**0-9**2-D********385 Server: Jetty(7.2.2.v20101205)
```

`{`

```json
  "Parameters" : {
```

`},`

```json
  "Description" : "No description"
```

`}`

##### 1.1.6.2 Query the information about a template

You can call this operation to query the information about a template when you use the template create a stack.

**Request parameters**

| Parameter | Locatio n | Type | Required | Description |
|---|---|---|---|---|

| x-acs-region-id | header | String | Yes | The region ID of the stack. |
|---|---|---|---|---|
| StackName | URI | String | Yes | The stack name. |
| StackId | URI | String | Yes | The stack ID. |

**Response parameters**

| Parameter | Type | Description |
|---|---|---|
| ROSTemplateFormatVersi on | String | The version number of the template. |
| Parametersd | Json | The parameters in the Parameters section of the template. The Parameters section defines the parameters that you must specify to create a stack based on the template. Each time you create a stack, you can use the parameters to specify custom information, such as the username, password, and environment-related Elastic Compute Service (ECS) instance type. Note If this parameter is specified when you create a stack, the value of this parameter is returned. |
| Outputs | Json | The outputs in the Outputs section of the template. The Outputs section defines the information that you want to obtain after the stack is created. Note If this parameter is specified when you create a stack, the value of this parameter is returned. |
| Resources | Json | The resources in the Resources section of the template. The Resources section provides the definitions of cloud resources that Resource Orchestration Service (ROS) deploys by using the template. Each resource is defined in a separate resource block. |

| Description | Json | The description of the template. You can use this parameter to provide useful information about the template. Note If this parameter is specified when you create a stack, the value of this parameter is returned. |
|---|---|---|

**Error codes**

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| InternalError | Server error | 500 | An unknown server error occurred. |
| StackNotFound | The Stack (% (stack name)s) could _ not be found. | 404 | The specified stack does not exist. |

**Examples**

Sample requests

```
GET http://ros.example.com/ stacks/myStack/378826b1-a71b-4c14-aa91- 9b36351f****/template HTTP/1.1 x-acs-signature-method: HMAC-SHA1 Authorization: acs ACSTQDkNtSMrZtwL:fWkOnYo6QzK3KvMANKE0VFeBos4= Date: Fri, 11 Sep 2015 05:31:53 GMT x-acs-signature-version: 1.0 x-sdk-client: Java/2.0.0 Accept: application/octet-stream x-acs-version: 2015-09-01 Cache-Control: no-cache Pragma: no-cache User-Agent: Java/1.6.0_27 Host: ros.example.com Connection: keep-alive x-acs-region-id:cn-beijing
```

Sample responses

```
HTTP/1.1 200 OK Date: Fri, 11 Sep 2015 05:30:12 GMT Content-Type: application/json; charset=UTF-8 Content-Length: 1694 Connection: close Vary: Accept-Encoding Access-Control-Allow-Origin: * Access-Control-Allow-Methods: POST, GET, OPTIONS Access-Control-Allow-Headers: X-Requested-With, X-Sequence, _aop_secret, _aop_signature Access-Control-Max-Age: 172800 X-Acs-Request-Id: A******2-C**7-4**0-9**2-D********385 Server: Jetty(7.2.2.v20101205)
```

`{`

```json
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Resources" : {
    "str2" : {
      "Type" : "ALIYUN::RandomString"
```

`},`

```json
    "str1" : {
      "Type" : "ALIYUN::RandomString",
      "DependsOn" : "str2"
```

`}` `},`

```json
  "Description" : "Simple template to deploy a single compute instance"
```

`}`

#### 1.1.7 Other operations

##### 1.1.7.1 Query events

You can call this operation to query a stack and its resource events.

**Request parameters**

| Parameter | Locat ion | Type | Requir ed | Description |
|---|---|---|---|---|
| x-acs- region-id | head er | String | Yes | The ID of the region where you want to query the stack. |
| StackName | URI | String | Yes | The stack name. The name can be up to 255 characters in length, and must comply with the ^[a-zA-Z][a-zA-Z0-9 .-]*$ regular expression. _ |
| StackId | URI | String | Yes | The stack ID. |

| ResourceSta tus | Query | String | Yes | The state of the resource. Valid values: COMPLETE FAILED IN PROGRESS _ |
|---|---|---|---|---|
| ResourceNa me | Query | String | Yes | The resource name. |
| ResourceTy pe | Query | String | Yes | The resource type. |
| PageNumbe r | Query | Integer | Yes | The number of the page to return. Pages start from page 1. Default value: 1. |
| PageSize | Query | Integer | Yes | The number of entries to return on each page. Maximum value: 100. Default value: 10. |

**Response parameters**

| Parameter | Type | Description |
|---|---|---|
| TotalCount | Integer | The total number of events. |
| PageNumber | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| Events | List | The events. The Event table in the following section describes the specific fields. |

Table 1: Event

| Field | Type | Description |
|---|---|---|
| ResourceStatus | String | The state of the resource. |
| ResourceName | String | The resource name. |
| StatusReason | String | The reason why the resource is in its current state. |
| Id | String | The event ID. |

| ResourceId | String | The resource ID. |
|---|---|---|
| ResourceType | String | The resource type. |
| ResourcePhysicalId | String | The physical ID of the resource. |
| Time | String | The time when the event was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC. |

**Error codes**

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| InternalError | Server error | 500 | An internal error occurred on the server. |
| StackNotFou nd | The Stack (%(stack name)s) could not be _ found. | 404 | The stack does not exist. |

**Examples**

Sample requests

```
GET http://ros.example.com/ stacks/myStack/378826b1-a71b-4c14-aa91-9b36351f****/events HTTP/1.1 x-acs-signature-method: HMAC-SHA1 Authorization: acs ACSTQDkNtSMrZtwL:fWkOnYo6QzK3KvMANKE0VFeBos4= Date: Fri, 11 Sep 2015 05:31:53 GMT x-acs-signature-version: 1.0 x-sdk-client: Java/2.0.0 Accept: application/octet-stream x-acs-version: 2015-09-01 Cache-Control: no-cache Pragma: no-cache User-Agent: Java/1.6.0_27 Host: ros.example.com Connection: keep-alive x-acs-region-id:cn-beijing
```

Sample responses

```
HTTP/1.1 200 OK Date: Fri, 11 Sep 2015 05:31:53 GMT Content-Type: application/json; charset=UTF-8 Content-Length: 10197 Connection: close Vary: Accept-Encoding Access-Control-Allow-Origin: * Access-Control-Allow-Methods: POST, GET, OPTIONS Access-Control-Allow-Headers: X-Requested-With, X-Sequence, _aop_secret, _aop_signature Access-Control-Max-Age: 172800 X-Acs-Request-Id: 1******8-A**A-4***-8**F-C********876 Server: Jetty(7.2.2.v20101205)
```

`{`

```json
  "TotalCount" : 4,
  "PageNumber" : 1,
  "Events" : [{
      "Status" : "CREATE_IN_PROGRESS",
      "ResourceType" : "ALIYUN::ECS::Disk",
      "ResourceId" : "DataDisk",
      "StatusReason" : "state changed",
      "Time" : "2015-10-23T07:54:31",
      "ResourceName" : "DataDisk",
      "Id" : "2******9-4**4-4**7-b**c-a********879",
      "ResourcePhysicalId" : null
    }, {
      "Status" : "CREATE_IN_PROGRESS",
      "ResourceType" : "ALIYUN::ROS::Stack",
      "ResourceId" : "hope_test_chinese",
      "StatusReason" : "Stack CREATE started",
      "Time" : "2015-10-23T07:54:30",
      "ResourceName" : "hope_test_chinese",
      "Id" : "e******b-3**f-4**6-9**8-a********6c3",
      "ResourcePhysicalId" : "2******f-c**1-4**7-8**9-5********cc4"
```

`}` `],`

```json
  "PageSize" : 2
```

`}` ck SDK by ASAPI

## 2 Use Apsara Stack SDK by ASAPI

**ASAPI**

### 2.1 Overview

This topic describes the architecture and features of Apsara Stack API (ASAPI). ASAPI is a platform that integrates all features and is the only portal to connect to Apsara Stack. ASAPI can categorize operations and audit and manage their calls. It can also assemble and customize existing operations and adapt to your operations. Each cloud service can call ASAPI for required data and features, avoiding inconsistent operations caused by different call methods and separate encapsulation. This can ensure the operation program integrity and improve development efficiency and code portability. ASAPI allows you to manage and call operations in a unified manner and customize development. ASAPI supports access of most cloud services deployed in Apsara Stack and passthrough or encapsulation of different backend APIs. This way, operations can be called with the same method. ASAPI allows you to use SDKs and API Portal to call APIs registered in ASAPI, customize SDKs, and manage versions of Apsara Stack, services, and APIs. ck SDK by ASAPI

### 2.2 Log on to the API Tool console

You can log on to the API Tool console through the Apsara Stack Cloud Management (ASCM) console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.
2. Enter your username and password.
Obtain the username and password from an operations administrator.

> **Note:** The first time you log on to the Apsara Uni-manager Management Console, you must change the password of your account. The password must be 8 to 20 characters in length and contain at least two of the following character types:
> Uppercase or lowercase letters
> Digits
> Special characters such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%).

3. Click **Log On**.
4. In the top navigation bar, choose **Products > Others > API Tool**.

### 2.3 View the information about API operations

**API operations**

You must obtain a service name, API operation name, and API version. All the information is required when you use SDKs.

**Procedure**

1. Log on to the API Tool console.
2. In the left-side navigation pane, click **API fold**.
3. On the **API Directory** page, select the target service from the drop-down list, enter the API
operation name in the search box, and then click the search icon. ck SDK by ASAPI
4. View and remember the service name, API operation name, and API version.

### 2.4 Obtain the endpoint of ASAPI

You can obtain the endpoint of Apsara Stack API (ASAPI) in the Apsara Stack Operations (ASO) console.
1. In the address bar, enter the URL region-id.aso.intranet-domain-id.com and press the Enter
key.

> **Note:** You can select a language from the drop-down list in the upper-right corner of the page.

2. Enter your username and password.

> **Note:** Obtain the username and password for logging on to the ASO console from the deployment personnel or an administrator.

When you log on to the ASO console for the first time, you must change the password of your username as prompted. To enhance security, a password must meet the following requirements: It must contain uppercase and lowercase letters. It must contain digits. It must contain special characters such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%). It must be 10 to 20 characters in length. ck SDK by ASAPI
3. Click **Log On** to go to the **ASO** console.
4. In the left-side navigation pane, choose **Products > Product List**. On the Product List
page, click **Apsara Infrastructure Management Framework**.
5. In the left-side navigation pane of the Apsara Infrastructure Management Framework
console, click **Reports**.
6. On the **All Reports** page, search for **Registration Vars of Services**. Click **Registration**
**Vars of Services**.
7. On the **Registration Vars of Services** page, click the
icon next to **Service**. In the dialog box that appears, search for **asapi**.
8. Right-click the **Service Registration** column corresponding to asapi and select **Show**
**More**.
9. In the **Details** dialog box, view the value of **asapi.gateway.endpoint**. The value is the
logon URL of the Apsara ASAPI Management platform. ck SDK by ASAPI

### 2.5 Obtain the core package for ASAPI

**ASAPI**

Apsara Stack uses Apsara Stack API (ASAPI) as a unified portal for all Apsara Stack products that are connected to ASAPI. ASAPI also provides SDKs to call product APIs. For more information about how to obtain the core package for ASAPI, see Apsara Stack documentation.

### 2.6 Obtain an AccessKey pair

An AccessKey pair is composed of an AccessKey ID and an AccessKey secret. The AccessKey pair is used to implement symmetric encryption to verify the identity of the requester. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. This topic describes how to obtain an AccessKey pair.

**Prerequisites**

Only operation administrators and level-1 organization administrators can obtain the AccessKey pair of an organization.

**Obtain the AccessKey of an organization**

To obtain the AccessKey pair of an organization, perform the following operations:
1. Log on to the ASCM console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane of the **Enterprise** page, click **Organizations**.
4. In the Organizations navigation tree, click the
icon on the right of the organization to be added.
5. Select **AccessKey**.
6. In the AccessKey message, view the AccessKey pair of the organization.
ck SDK by ASAPI

> **Note:** An AccessKey pair is automatically allocated to a level-1 organization. Subordinate organizations use the same AccessKey pair as their level-1 organization.

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following operations:
1. Log on to the ASCM console as an administrator.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and
click **User Information**.
3. In the **Apsara Stack AccessKey Pair** section of the User Information page, view your
AccessKey pair.

> **Note:** The AccessKey pair consists of an AccessKey ID and an AccessKey secret. These credentials provide you full permissions on Apsara Stack resources. You must keep the AccessKey pair confidential.

### 2.7 Query the region ID

You must specify the region ID when you call Apsara Stack SDK for Node.js. You must query the region ID in the Apsara Stack Cloud Management (ASCM) console.
1. Log on to the ASCM console as an administrator.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and
click **User Information**.
3. In the **Apsara Stack AccessKey Pair** section, you can view the region ID.

### 2.8 SDK for Java

This topic describes how to obtain and use Apsara Stack SDK for Java.

**Prerequisites**

You must have an Apsara Stack tenant account and an AccessKey pair (AccessKey ID and AccessKey secret) to use Apsara Stack SDK for Java. You can obtain an AccessKey pair in the Apsara Stack Cloud Management (ASCM) console. For more information, see Obtain an AccessKey pair. The endpoint of ASAPI is obtained. For more information about how to obtain the service endpoint, see Obtain the endpoint of ASAPI. Apsara Stack SDK for Java supports JDK 1.6 and later. ck SDK by ASAPI

**Add dependencies**

Add dependencies to pom.xml:

```xml
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>asapi</artifactId>
    <version>0.0.3-RELEASE</version>
</dependency>
```

**Usage**

You can call API operations on Asapi by using GET and POST requests. GET requests

```
 ASClient client = new ASClient();
// Form 1 String result = client.doGet(endpoint, parameters); // Form 2 String result = client.doRequest(endpoint, parameters);
```

POST requests

```java
public void callAsapiServerThroughAscm(){
    Map<String, String> parameters = new HashMap<String, String>();
    parameters.put("Product", "Ros");
    parameters.put("Action", "DescribeStacks");
    parameters.put("Version", "2015-09-01");
    parameters.put("RegionId", "cn-qingdao-env25-d01");
    parameters.put("AccessKeyId", "OYZWcdjcbmz0****");
    parameters.put("AccessKeySecret", "******************************");
    parameters.put("PageNumber", "1");
    parameters.put("PageSize", "10");
    ASClient client = new ASClient("local");
    String result = client.doRequest(endpoint, parameters);
    System.out.println(result);
```

`}`

**Header parameters**

| Parameter | Description |
|---|---|
| x-acs-regionid | The region ID. For more information about how to obtain the region ID, see Query the region ID. |
| x-acs-organizationid | The ID of the organization in the ASCM console. |
| x-acs-resourcegroupid | The ID of the resource set in the ASCM console. |
| x-acs-instanceid | The ID of the instance for which you want to change settings. |

ck SDK by ASAPI

### 2.9 SDK for Node.js

This topic describes how to obtain and use Apsara Stack SDK for Node.js.

**Prerequisites**

You must have an Apsara Stack tenant account and an AccessKey pair (AccessKey ID and AccessKey secret) to use Apsara Stack SDK for Node.js. You can obtain and view your AccessKey pair in the ASCM console. For more information, see Obtain an AccessKey pair. The endpoint of ASAPI is obtained. For more information about how to obtain the service endpoint, see Obtain the endpoint of ASAPI. The region ID is obtained. For more information about how to obtain the region ID, see Query the region ID.

**Add dependencies**

1. Install Apsara Stack SDK for Node.js.

```
 tnpm install --save @ali/asapi-nodejs-sdk
```

2. If mocha.opts depends on eggjs, you must configure mocha.opts.

```
--recursive --colors --timeout 60000 --reporter mochawesome --require co-mocha --require egg-ts-helper/register --require espower-typescript/guess -- require intelli-espower-loader
```

**Usage**

The following example shows how to use Apsara Stack SDK for Node.js:
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
3. Initiate the request and handle its response or exception.
ck SDK by ASAPI

```java
// Import the core package. import * as ASAPIClient from '@ali/asapi-nodejs-sdk'; // Configure parameters about environments. const cnofig = {
    API_GATEWAY: 'http://${ASAPI_ENDPOINT}/asapi/v3',
    regionId: 'cn-hangzhou',
    accessKeyId: 'xxxxxxxxxxxxxxxxxx',
    accessKeySecret: 'xxxxxxxxxxxxxxxxxx'
```

};

```
// Specify the HttpCLient parameter to initiate a specified call. If HttpCLient is se t to null, the built-in client is used by default. const custom_http_client = null; // Initiate the ASAPI client. const AsapiClient = new ASAPIClient(cnofig, custom_http_client); // Set request parameters. const params = {
    // Required parameters: specify the name and version of the product for which you
want to initiate the call.
    Product: 'ascm',
    Version: '2019-05-10',
    // Required parameters: specify the specific function.
    Action: 'CreateUser',
    // Optional business parameter: request parameters that correspond to the functio
```

`n.`

```
    Username: 'testCreateUser',
    Passwd: 'Alibaba%1688',
    Age: 22,
    IsMale: false,
    idList: ["34", "26", "22"]
```

};

```
// Initiate a call and obtain the response. const result = await AsapiClient.doRequest(params, {method: 'POST'}); // Display the response. console.log(result);
```

### 2.10 Use POP SDK to call ASAPI (optional)

**(optional)**

If an application used POP SDK to call cloud products, you must switch the gateway to Asapi by performing the following steps.

**Procedure**

1. Switch the gateway to Asapi and add common parameters to the request header.
2. Add the **Product Name** field to the request header.
ck SDK by ASAPI

> **Note:** Different products use different endpoints in POP SDK. However, Asapi provides only one domain name. You cannot identify the product to which an API operation belongs based on the API operation name and the version number. For example, both ECS and KVStore for Redis provide the DescribeInstances API operation of the 2015-01-01 version.

**Sample code**

The following code provides an example on how to use POP SDK to call ROS API operations.

```
public void DescribeMetricLastTest(){
    // Set a proxy by specifying the Cloud parameter. If you do not need to set a proxy
, delete the code related to Cloud.
    Cloud cloud = new Cloud();
    cloud.setConfig("proxy_host", "100.67.XX.XX");
    cloud.setConfig("proxy_port", "XXXX");
    ASClient asClient = new ASClient(cloud);
    HashMap<String, String> params = new HashMap<>(8);
    params.put("RegionId", "cn-hangzhou");
    params.put("AccessKeyId", "OYZWcdjcbmz0****");
    params.put("AccessKeySecret", "******************************");
    params.put("Namespace", "acs_ecs_dashboard");
    params.put("MetricName", "memory_totalspace");
    params.put("Action", "DescribeMetricLast");
    params.put("Version", "2019-01-01");
    params.put("Product", "Cms");
    String strResult = asClient.doPost("{asApi endpoint}", params);
    logger.info(strResult);
```

`}`
