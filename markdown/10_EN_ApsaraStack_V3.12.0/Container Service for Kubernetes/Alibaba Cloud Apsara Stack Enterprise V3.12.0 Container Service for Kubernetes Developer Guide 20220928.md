---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Container Service for Kubernetes Developer Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 33
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Container Service for Kubernetes Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E5%BC%B9%E6%80%A7%E8%AE%A1%E7%AE%97/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20Container%20Service%20for%20Kubernetes%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 Container Service for Kubernetes Developer Guide 20220928

## Table of Contents

- 1 Container Service API invocation
  - 1.1 Overview
  - 1.2 Common parameters
  - 1.3 Request syntax
  - 1.4 Response parameters
  - 1.5 Sign API requests
- 2 Cluster API list
  - 2.1 Download cluster certificates
  - 2.2 Create a Kubernetes cluster
  - 2.3 Add one or more existing ECS instances to a Kubernetes cluster
  - 2.4 Get kubeconfig files
  - 2.5 Query detailed information of a cluster
  - 2.6 Scale out Kubernetes clusters
  - 2.7 Delete clusters

API invocation

## 1 Container Service API invocation

invocation

### 1.1 Overview

To use the APIs provided by Container Service, you can send HTTP requests to the endpoint of Container Service APIs and include specific parameters in the requests. The system returns a response after processing the request.
2. Request structure

### 1.2 Common parameters

This topic lists the common request headers, common response headers, and common parameters that are required in Apsara Stack API (ASAPI) requests when you make Container Service for Kubernetes API requests. Common request headers Common request parameters must be included in all Container Service for Kubernetes API requests.

| Parameter | Description | Required |
|---|---|---|
| Authorization | The authentication information that is used to check the authenticity of a request. The string must follow the AccessKeyId:Signature format. | Yes |
| Content-Length | The length of the HTTP request content. This length is specified in RFC 2616. | Yes |
| Content-Type | The type of HTTP request content. This type must follow the format that is specified in RFC 2616. | Yes |
| Content-MD5 | The 128-bit MD5 hash value of the HTTP message body. The hash value is encoded in the Base64 format. We recommend that you set this parameter for all requests to prevent parameter tampering. | Yes |

API invocation

| Parameter | Description | Required |
|---|---|---|
| Date | The time when a request was created. The time must be in GMT. If the time between when the request was sent and when the request was received exceeds 15 minutes, the request is deemed invalid. | Yes |
| Host | The target host of the request, for example, diku.aliyuncs.com. | Yes |
| Accept | The type of response that is required by the client. Valid values: application/json and application/xml. | Yes |
| x-acs-version | The version number of the API. Set the value to 2015-12-15. | Yes |
| x-acs-region-id | The region where the Container Service for Kubernetes server is located. | Yes |
| x-acs-signature-nonce | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. | Yes |
| x-acs-signature-method | The encryption method of the signature string. Set the value to HMAC-SHA1. | Yes |

Examples

```
GET /clusters HTTP/1.1 Host: cs.aliyuncs.com Accept: application/json User-Agent: cs-sdk-python/0.0.1 (Darwin/15.2.0/x86_64;2.7.10) x-acs-signature-nonce: f63659d4-10ac-483b-99da-ea8fde61eae3 Authorization: acs <yourAccessKeyId>:<yourSignature> x-acs-signature-version: 1.0 Date: Wed, 16 Dec 2015 11:18:47 GMT x-acs-signature-method: HMAC-SHA1 Content-Type: application/json;charset=utf-8 X-Acs-Region-Id: cn-beijing Content-Length: 0
```

Common parameters required in ASAPI requests Additional common parameters are required when you make ASAPI requests. The following table lists these common parameters. API invocation

| Parameter | Description | Required |
|---|---|---|
| x-ascm-product-ak | The AccessKey pair that you can retrieve in the Apsara Stack Cloud Management (ASCM) console. | Yes |
| x-ascm-product-name | The name of the product that supports the API. Set the value to cs for Container Service. | Yes |
| x-ascm-product-version | The version number of the API. Set the value to 2015-12-15. | Yes |
| x-acs-regionid | The ID of the region where the target Container Service for Kubernetes cluster is deployed. | Yes |
| x-acs-organizationid | The ID of the organization to which the target Container Service for Kubernetes cluster belongs. | Yes |
| x-acs-resourceGroupId | The ID of the resource set of the target Container Service for Kubernetes cluster. | Yes |
| x-acs-roleid | The ID of the ASCM role that is authorized to make ASAPI requests. | Yes |

Common response headers Every response returns a unique RequestID regardless of whether the call is successful. Examples XML format

```
<? xml version="1.0" encoding="UTF-8"? > <!—Result Root Node--> <Interface Name+Response>
 | <!—Return Request Tag-->
 | <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
 | <!—Return Result Data-->
</Interface Name+Response>
```

JSON format

```json
    "RequestId": "4C467B38-3910-447D-87BC-AC049166F216"
    /* Return Result Data */
```

API invocation

### 1.3 Request syntax

This topic describes the syntax that you must follow when you make Container Service API requests. Endpoint The endpoints of the API operations are classified into the following types: Primary region: cs.${global:internet-domain} Secondary region: cs.${global:region}.${global:internet-domain} You must add the /roa prefix to the endpoint that you use to make an Apsara Stack API (ASAPI) request. For example, if the /clusters endpoint is used to create a cluster, you must include /roa/clust ers in your ASAPI request. Protocols HTTP and HTTPS are supported. We recommend that you send requests over HTTPS to enhance security. Request methods The following HTTP methods are supported: PUT, POST, GET, and DELETE. Request parameters Each request must contain common request parameters and parameters unique to specific operations. Request encoding All requests and responses are encoded in the UTF-8 format.

### 1.4 Response parameters

The response data is returned in a unified format. If status code `2xx` is returned, it indicates that the API call is successful. If status code `4xx` or `5xx` is returned, it indicates that the API call has failed. For successful API calls, response data is returned in XML or JSON format. You can pass a parameter to specify the format when you call the API. The default format is XML. The following example is formatted for readability. The actual result is not formatted with line feeds or indentation.

### 1.5 Sign API requests

This topic describes how to sign API requests to protect Container Service from unauthorized requests. Introduction Apsara Stack issues an AccessKey pair to each Apsara Stack tenant account. Each AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey ID is used to verify the identity of the user. The AccessKey secret is used to encrypt and verify the signature string. You must keep your AccessKey secret confidential. You can obtain and manage the AccessKey pair in the Apsara Stack Cloud Management (ASCM) console. API invocation Container Service verifies every request it receives. All requests to Container Service must contain signature information. Container Service implements symmetric encryption with an AccessKey pair to verify the identity of the request sender. Container Service only accepts requests that are validated by verification codes. Invalid requests are rejected and the HTTP status code 403 is returned. You can add the Authorization header to every HTTP request and include the signature in the header. You must add the signature to the Authorization header in the following format: `Authorization: acs`

```
[Access Key Id]:[Signature] .
```

The following sample code can be used to calculate the value of the `Signature` field:

```
Signature = base64(hmac-sha1(VERB + "\n"
            + ACCEPT + "\n"
            + Content-MD5 + "\n"
            + Content-Type + "\n"
            + Date + "\n"
            + CanonicalizedHeaders + "\n"
            + CanonicalizedResource))
```

`VERB` specifies the HTTP method, such as `PUT` . `ACCEPT` specifies the type of response that is required by the client. Valid values: application/json and application/xml.

| Content-MD5 |   | s |
|---|---|---|
| Content-Type |   |   |
| Date | specifies |   |

`Content-MD5` specifies the MD5 hash value of the request content. `Content-Type` specifies the type of request content. `Date` specifies the time when the request was sent. This parameter is required. The time must be in GMT. If the time between when the request was sent and when the request was received exceeds 15 minutes, the request is deemed invalid and the HTTP status code 400 is returned. For example, `Thu,` `17 Mar 2012 18:49:58 GMT` can be used. `CanonicalizedHeaders` specifies the header fields that are prefixed with `x-acs-` in the request. `CanonicalizedResource` specifies the Uniform Resource Identifier (URI) of the requested resource. For example, /clusters? name=my-clusters&resource=new can be used. The value of `CanonicalizedHeaders` including the header fields that are prefixed with `x-acs-` must meet the following requirements:
1. Convert the names of all HTTP request headers whose prefixes are `x-oss-` into lowercase
letters. For example, you must convert `X-ACS-Meta-Name: TaoBao` into `x-acs-meta-name: TaoBa` `o` . Header field names are case-insensitive. We recommend that you use lowercase letters.
2. If a header field value is too long, replace specific delimiters with spaces. The delimiters include \t
, \n , \r , and \f .
3. Sort HTTP headers in alphabetical order.
4. Delete any space between the header field names and values. For example, convert `x-acs-meta-n`

```
ame: TaoBao,Alipay into x-acs-meta-name:TaoBao,Alipay .
```

5. Join all header fields with the \n delimiter to form the value of CanonicalizedHeaders.
API invocation Not e `CanonicalizedResource` must follow this format: `CanonicalizedResource` specifies the URIs of the requested resources. You must sort sub-resources in alphabetical order

| & |   |
|---|---|
|   | ? |

and join them with the `&` delimiter to form a string. In the following example, the string that follows the question mark ( ? ) indicates the value of CanonicalizedResource.

```
http://cs.aliyuncs.com/clusters?name=my-clusters&resource=new
```

The value of `CanonicalizedResource` must be the following string:

```
/clusters? name=my-clusters&resource=new
```

Example The following example shows how to sign an API request. The `access_key_id` and `access_key_secret` fields respectively specify the AccessKey ID and AccessKey secret that are used in the example. We recommend that you use your own program to construct an API request. You can then calculate the signature that is used in the following example. Sample request:

```json
POST http://cs.aliyuncs.com/clusters?param1=value1&param2=value2 HTTP/1.1 Accept-Encoding: identity Content-Length: 210 Content-MD5: 6U4ALMkKSj0PYbeQSHqgmA== x-acs-version: 2015-12-15 Accept: application/json User-Agent: cs-sdk-python/0.0.1 (Darwin/15.2.0/x86_64;2.7.10) x-acs-signature-nonce: fbf6909a-93a5-45d3-8b1c-3e03a7916799 x-acs-signature-version: 1.0 Date: Wed, 16 Dec 2015 12:20:18 GMT x-acs-signature-method: HMAC-SHA1 Content-Type: application/json;charset=utf-8 X-Acs-Region-Id: cn-beijing Authorization: acs <yourAccessKeyId>:<yourSignature> {"password": "Just$****","instance_type": "ecs.m2.medium","name": "my-test-cluster-9708**** ","size": 1,"network_mode": "vpc","data_disk_category": "cloud","data_disk_size": 10,"ecs_i mage_id": "m-253l****l"}
```

Const ruct t he request Calculate the values of `Content-Length` and `Content-MD5` . `Content-Length` specifies the length of the content body. Not e The body cannot start with a space or line feed. API invocation

```json
body: {"password": "Just$****","instance_type": "ecs.m2.medium","name": "my-test-cluster-97 08****","size": 1,"network_mode": "vpc","data_disk_category": "cloud","data_disk_size": 10, "ecs_image_id": "m-253ll****"} Content-Length: 210
```

`Content-MD5` : Calculate the MD5 hash value by performing the following steps:

```json
body: {"password": "Just$****","instance_type": "ecs.m2.medium","name": "my-test-cluster-97 08****","size": 1,"network_mode": "vpc","data_disk_category": "cloud","data_disk_size": 10, "ecs_image_id": "m-253ll****"}
# Calculate the MD5 hash value of the body.
md5(body): e94e002cc90a4a3d0f61b790487aa098
# Convert the MD5 hash value into a byte array. Convert every two hexadecimal digits into o
ne byte.
# Example: e9 -> 11111111111111111111111111101001 -> -23
bytes(md5(body)): {[-23], [78], [0], [44], [-55], [10], [74], [61], [15], [97], [-73], [-11 2], [72], [122], [-96], [-104]}
# Convert the byte array into a string that is encoded in the Base64 format.
base64(bytes(md5(body))): 6U4ALMkKSj0PYbeQSHqgmA== Content-MD5: 6U4ALMkKSj0PYbeQSHqgmA==
```

Convert the value of `CanonicalizedHeaders` by performing the following steps:

```bash
# List all header field names prefixed with the string x-acs-.
x-acs-version: 2015-12-15 x-acs-signature-nonce: ca480402-7689-43ba-acc4-4d2013d9d8d4 x-acs-signature-version: 1.0 x-acs-signature-method: HMAC-SHA1 X-Acs-Region-Id: cn-beijing
# Convert the header field names into lowercase letters, delete the spaces at the start and
end of each line, and then sort the header field names in alphabetical order. Delete any sp ace between the header field names and values.
# Note: The last line cannot contain any line feed.
x-acs-region-id:cn-beijing x-acs-signature-method:HMAC-SHA1 x-acs-signature-nonce:fbf6909a-93a5-45d3-8b1c-3e03a7916799 x-acs-signature-version:1.0 x-acs-version:2015-12-15
```

Calculate the value of `CanonicalizedResource` . In this example, the length of the `CanonicalizedResource` field value is 27. Not e A line feed \n exists at the end of the first line.

```
/clusters? param1=value1&param2=value2
```

Calculate the value of `Signature` . API invocation Construct the value of `SignatureString` . In this example, the length of the signature string is 307. Except for the last line, each line has a line feed \n at the end.

```
POST application/json 6U4ALMkKSj0PYbeQSHqgmA== application/json;charset=utf-8 Wed, 16 Dec 2015 12:20:18 GMT x-acs-region-id:cn-beijing x-acs-signature-method:HMAC-SHA1 x-acs-signature-nonce:fbf6909a-93a5-45d3-8b1c-3e03a7916799 x-acs-signature-version:1.0 x-acs-version:2015-12-15 /clusters? param1=value1&param2=value2
```

Calculate the value of `Signature` .

```bash
# Use the AccessKey secret to encrypt the value of SignatureString. In this example, access
_key_secret specifies the AccessKey secret. hmac-sha1(SignatureString): fee03d405e421ebaf514adec881038c4b313584d
# Similar to Content-MD5 calculation, convert the encrypted string into a byte array.
# Convert the byte array into a string that is encoded in the Base64 format. The output is
the signature string. base64(bytes(hmac-sha1(SignatureString))): ZmVlMDNkNDA1ZTQyMWViYWY1MTRhZGVjODgxMDM4YzRiMzEz NTg0ZA== Signature: ZmVlMDNkNDA1ZTQyMWViYWY1MTRhZGVjODgxMDM4YzRiMzEzNTg0ZA==
```

The signature string is calculated. Add other header fields to your request and set the value of Signature to the calculated signature string. The following sample code shows the signed API request.

```json
POST http://cs.aliyuncs.com/clusters?param1=value1&param2=value2 HTTP/1.1 Accept-Encoding: identity Content-Length: 210 Content-MD5: 6U4ALMkKSj0PYbeQSHqgmA== x-acs-version: 2015-12-15 Accept: application/json User-Agent: cs-sdk-python/0.0.1 (Darwin/15.2.0/x86_64;2.7.10) x-acs-signature-nonce: fbf6909a-93a5-45d3-8b1c-3e03a7916799 x-acs-signature-version: 1.0 Date: Wed, 16 Dec 2015 12:20:18 GMT x-acs-signature-method: HMAC-SHA1 Content-Type: application/json;charset=utf-8 X-Acs-Region-Id: cn-beijing Authorization: acs <yourAccessKeyId>:<yourSignature> {"password": "Just$****","instance_type": "ecs.m2.medium","name": "my-test-cluster-9708**** ","size": 1,"network_mode": "vpc","data_disk_category": "cloud","data_disk_size": 10,"ecs_i mage_id": "m-253ll****"}
```

## 2 Cluster API list

### 2.1 Download cluster certificates

Download the certificate for the cluster where you are logged in. Request Request f ormat

```
GET /clusters/:clusterid/certs
```

Cust om request headers None. See Common request headers. Response Response f ormat

```
HTTP/1.1 200 OK
```

Cust om response headers None. See Common response headers. Response body

```json
    "config": "string"
```

Response body paramet ers

| Name | Type | Description |
|---|---|---|
| config | string | The kubeconfig file that contains information about the current user. |

Example Sample request

```
GET /clusters/C5b5e80b0b64a4bf6939d2d8fbbc5ded7/certs HTTP/1.1 <Common request header>
```

Sample response

```json
HTTP/1.1 200 OK <Common response header>
     "config": "xxxxxxxx"
```

### 2.2 Create a Kubernetes cluster

You can call this operation to create a Kubernetes cluster and add nodes to the cluster. Request Request f ormat

```
POST /clusters HTTP/1.1
```

Cust om request headers None. For more information, see Common request headers. Request body

```json
    "disable_rollback": "Specifies whether to disable rollback if the operation fails.",
    "name": "The name of the cluster that you want to create",
    "timeout_mins": "The timeout period for the system to create a cluster stack.",
    "cluster_type": "The type of the cluster. Set the value to Kubernetes.",
    "region_id": "The region where the cluster is deployed.",
    "vpcid": "VPC ID",
    "zoneid": "The zone of the cluster.",
    "vswitchid": "The ID of the VSwitch that is connected to the cluster.",
    "container_cidr": "The CIDR block of the pods.",
    "service_cidr": "The CIDR block of the services.",
    "ssh_flags": "Specifies whether to allow public access by using SSH.",
    "cloud_monitor_flags": "Specifies whether to install the Cloud Monitor agent.",
    "login_password": "The SSH logon password. You can select one between SSH authenticatio
n and key pair authentication.",
    "key_pair": "The name of the key pair. Select one between SSH authentication and key pa
ir authentication.",
    "master_instance_charge_type": "The billing method of the master nodes. Valid values: P
ostPaid and PrePaid.",
    "master_period_unit": "The unit of the subscription duration of the master node. Valid
values: Month and Year. This parameter takes effect only when master_instance_charge_type i s set to PrePaid.",
    "master_period": "The subscription duration of the master node. This parameter takes ef
fect only when master_instance_charge_type is set to PrePaid.",
    "master_auto_renew": "Specifies whether to enable auto renewal for the master nodes.",
    "master_auto_renew_period": "The renewal cycle of the master nodes.",
    "master_instance_type": "The instance types of the master nodes.",
    "master_system_disk_category": "The system disk type of the master nodes.",
    "master_system_disk_size": "The system disk size of the master nodes.",
    "master_data_disk": "Specifies whether to attach data disks to the master nodes.",
    "master_data_disk_category": "The data disk type of the master nodes.",
    "master_data_disk_size": "The data disk size of the master nodes.",
    "worker_instance_charge_type": "The billing method of the worker nodes. Valid values: P
rePaid and PostPaid.",
    "worker_period_unit": "The unit of the subscription duration of the worker nodes. Valid
values: Month and Year. This parameter takes effect only when worker_instance_charge_type i s set to PrePaid.",
    "worker_period": "The subscription duration of the worker nodes. This parameter takes e
ffect only when worker_instance_charge_type is set to PrePaid.",
    "worker_auto_renew": "Specifies whether to enable auto renewal for the worker nodes. Va
lid values: true and false.",
    "worker_auto_renew_period": "The renewal cycle of the worker nodes.",
    "worker_instance_type": "The instance types of the worker nodes.",
    "worker_system_disk_category": "The system disk type of the worker nodes.",
    "worker_system_disk_size": "The system disk size of the worker nodes.",
    "worker_data_disk": "Specifies whether to attach data disks to the worker nodes.",
    "worker_data_disk_category": "The data disk type of worker nodes.",
    "worker_data_disk_size": "The data disk size of the worker nodes.",
    "num_of_nodes": "The number of worker nodes",
    "snat_entry": "Specifies whether to configure Source Network Address Translation (SNAT)
rules.",
    "public_slb": "Specifies whether to enable Internet access to the API server."
```

Request body paramet ers

| Parameter | Type | Required | Description |
|---|---|---|---|
| disable rollback _ | bool | No | Specifies whether to disable rollback when the operation fails. Valid Values: true: Rollback is enabled. false: Rollback is disabled. Default value: true. If you choose to enable rollback when the operation fails, resources that are created during the operation are released. We recommend that you set the value to true. |
| name | string | Yes | The name of the cluster. The name can contain uppercase letters, lowercase letters, Chinese characters, digits, and hyphens (-). |
| timeout mins _ | int | No | The timeout period for the system to create a cluster stack. Unit: minutes. Default value: 60. |
| region id _ | string | Yes | The ID of the region where the cluster is deployed. |
| zoneid | string | Yes | The zone of the cluster. |
| vpcid | string | No | Optional. The ID of the VPC network where the cluster is deployed. If you do not set this parameter, the system automatically creates a VPC network that uses the CIDR block 192.168.0.0/16. Not e The vpcid and vswitchid parameters must be used together. |
| vswitchid | string | No | Optional. The ID of the VSwitch that is connected to the cluster. If you do not set this parameter, the system automatically creates a VSwitch that uses the CIDR block 192.168.0.0/16. |
| container cidr _ | string | No | The CIDR block of the pods. This CIDR block cannot overlap with that of the VPC network. If the VPC network is automatically created by the system, the container CIDR block is set to 172.16.0.0/16 by default. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| service cidr _ | string | No | The CIDR block of the services. This CIDR block cannot overlap with that of the VPC network or pods. If the VPC network is automatically created by the system, the service CIDR block is set to 172.19.0.0/20 by default. |
| master instance c _ _ harge type _ | string | Yes | The billing method of the master nodes. Valid values: PrePaid: the subscription billing method. Postpaid: the pay-as-you-go billing method. This is the default value. |
| master period uni _ _ t | string | No | The unit of the subscription duration of the master nodes. This parameter is required when master instance charge type is set to _ _ _ PrePaid. Valid values: Week: The subscription duration is measured in weeks. Month: The subscription duration is measured in months. |
| master period _ | int | No | The duration of the subscription. This parameter is required when master instance charge type is set to _ _ _ PrePaid. When PeriodUnit=Week , valid values include: 1, 2, 3, and 4. When PeriodUnit=Month , valid values include: 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 48, and 60. |
| master auto rene _ _ w | bool | No | Specifies whether to enable auto renewal for the master nodes. This parameter takes effect only when master instance charge type is set to _ _ _ PrePaid. Valid values: true: Auto renewal is enabled. false: Auto renewal is disabled. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| master auto rene _ _ w period _ | int | No | The renewal cycle of the master nodes. This parameter is required when master instance charge type is set to _ _ _ PrePaid and worker auto renew is set to _ _ true. When PeriodUnit=Week , valid values include: 1, 2, and 3. When PeriodUnit=Month , valid values include: 1, 2, 3, 6, and 12. |
| master instance t _ _ ype | string | Yes | The instance types of the master nodes. For more information, choose User Guide > Elastic Compute Service (ECS) > What is ECS? > Instances types and see the list of instance families . |
| master system di _ _ sk category _ | string | Yes | The system disk type of the master nodes. Valid values: cloud efficiency: ultra disk. _ cloud ssd: standard SSD. _ |
| master system di _ _ sk size _ | int | Yes | The system disk size of the master nodes. Unit: GiB. |
| master data disk _ _ | bool | No | Specifies whether to attach data disks to the master nodes. true: Data disks are attached to the master nodes. false: Data disks are not attached to the master nodes. |
| master data disk _ _ _ category | string | No | The data disk type of the master nodes. This parameter takes effect only when master data disk is set to true. Valid _ _ values: cloud: basic disk. cloud efficiency: ultra disk. _ cloud ssd: standard SSD. _ |
| master data disk _ _ _ size | int | No | The data disk size of the master nodes. This parameter takes effect only when master data disk is set to true. Unit: GiB. _ _ |

| Parameter | Type | Required | Description |
|---|---|---|---|
| worker instance c _ _ harge type _ | string | No | The billing method of worker nodes. Valid values: PrePaid: the subscription billing method. PostPaid: the pay-as-you-go billing method. This is the default value. |
| worker period uni _ _ t | string | No | The unit of the subscription duration of the worker nodes. This parameter is required when worker instance charge type is set to _ _ _ PrePaid. Valid values: Week: The subscription duration is measured in weeks. Month: The subscription duration is measured in months. |
| worker period _ | int | No | The duration of the subscription of the worker nodes. This parameter is required when worker instance charge type is _ _ _ set to PrePaid. When PeriodUnit=Week , valid values include: 1, 2, 3, and 4. When PeriodUnit=Month , valid values include: 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 48, and 60. |
| worker auto rene _ _ w | bool | No | Specifies whether to enable auto renewal for the worker nodes. Valid values: true: Auto renewal is enabled. false: Auto renewal is disabled. |
| worker auto rene _ _ w period _ | int | No | The renewal cycle of the worker nodes. This parameter is required when worker instance charge type is set to _ _ _ PrePaid and master auto renew is set to _ _ true. When PeriodUnit=Week , valid values include: 1, 2, and 3. When PeriodUnit=Month , valid values include: 1, 2, 3, 6, and 12. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| worker instance t _ _ ype | string | Yes | The instance types of the worker nodes. For more information, choose User Guide > Elastic Compute Service (ECS) > What is ECS? > Instances types and see the list of instance families . |
| worker system di _ _ sk category _ | string | Yes | The system disk type of the worker nodes. |
| worker system di _ _ sk size _ | int | Yes | The system disk size of the worker nodes. Unit: GiB. |
| worker data disk _ _ | string | No | Specifies whether to attach data disks to the worker nodes. true: Data disks are attached to the worker nodes. false: Data disks are not attached to the worker nodes. |
| worker data disk _ _ _ category | int | No | The data disk type of the worker nodes. This parameter takes effect only when worker data disk is set to true. Valid _ _ values: cloud: basic disk. cloud efficiency: ultra disk. _ cloud ssd: standard SSD. _ |
| worker data disk _ _ _ size | string | No | The data disk size of the worker nodes. This parameter takes effect only when worker data disk is set to true. Unit: GiB. _ _ |
| login password _ | string | Yes | The SSH logon password. The password must be 8 to 30 characters in length and contain three of the following character types: uppercase letters, lowercase letters, digits, and special characters. You can select one between SSH authentication and key pair authentication. |
| key pair _ | string | Yes | The name of the key pair. You can select one between SSH authentication and key pair authentication. |
| num of nodes _ _ | int | Yes | The number of worker nodes. Valid values: [0,300] |

| Parameter | Type | Required | Description |
|---|---|---|---|
| snat entry _ | bool | Yes | Specifies whether to configure SNAT rules. If the VPC is automatically created, set the value to true. If an existing VPC network is specified, set this parameter based on the following rules: If the VPC network can access the Internet, set the value to false. If the VPC network cannot access the Internet, set the value to true to configure SNAT rules. In this case, if the value is set to false, the SNAT rules cannot be configured and the VPC network cannot access the Internet. |
| ssh flags _ | bool | No | Specifies whether to enable SSH logon. true: SSH logon is enabled. false: SSH logon is disabled. |
| cloud monitor fla _ _ gs | bool | No | Specifies whether to install the Cloud Monitor agent. Valid Values: true: The Cloud Monitor agent is installed. false: The Cloud Monitor agent is not installed. |
| public slb _ | bool | No | Specifies whether to enable Internet access to the API server. Valid values: true: The API server is accessible over the Internet. false: The API server is not accessible over the Internet. It is accessible only over the internal network. |

Response Response f ormat

```
HTTP/1.1 202 Accepted
```

Cust om response headers None. For more information, see Common response headers. Response body

```json
    "cluster_id":"string",
    "request_id":"string",
    "task_id":"string"
```

Examples Sample request s

```json
POST /clusters HTTP/1.1 <Common request headers>
    "disable_rollback": true,
    "name": "my-test-Kubernetes-cluster",
    "timeout_mins": 60,
    "cluster_type": "Kubernetes",
    "region_id": "cn-beijing",
    "zoneid": "cn-beijing-f",
    "vpcid": "",
    "vswitchid": "",
    "num_of_nodes": 1,
    "container_cidr": "172.16.0.0/16",
    "service_cidr": "172.19.0.0/20",
    "cloud_monitor_flags": true,
    "master_instance_type": "ecs.sn1ne.large",
    "master_system_disk_category": "cloud_efficiency",
    "master_system_disk_size": 40,
    "worker_instance_type": "ecs.sn1ne.large",
    "worker_system_disk_category": "cloud_efficiency",
    "worker_system_disk_size": 40,
    "snat_entry": true,
    "ssh_flags": true,
    "login_password": "Hello1234"
```

Sample success responses

```json
HTTP/1.1 202 Accepted <Common response headers>
    "cluster_id": "cb95aa626a47740afbf6aa099b650d7ce",
    "request_id": "687C5BAA-D103-4993-884B-C35E4314A1E1",
    "task_id": "T-5a54309c80282e39ea00002f"
```

### 2.3 Add one or more existing ECS instances to a Kubernetes cluster

instances to a Kubernetes cluster You can call this operation to add one or more existing Elastic Compute Service (ECS) instances to a Kubernetes cluster. If the call is successful, a success response is returned. Not e When you add an ECS instance to the Kubernetes cluster, the system disk of the instance is replaced. We recommend that you back up data before you call this operation. Request Request f ormat

```
POST /clusters/{cluster_id}/attach HTTP/1.1
```

Request paramet ers

| Parameter | Type | Required | Description |
|---|---|---|---|
| cluster id _ | string | Yes | The ID of the cluster that you want to manage. |

Cust om request headers None. For more information, see Common request headers. Request body

```json
    "password": "The root password of the ECS instances.",
    "instances": "The ECS instances that you want to add to the cluster",
    "format_disk": "Specifies whether to format data disks.",
    "key_pair": "The key pair of the ECS instances."
```

Request body paramet ers

| Parameter | Type | Required | Description |
|---|---|---|---|
| password | String | Yes | The password for logging on to the ECS instances. The password must be 8 to 30 characters in length and contain three of the following character types: uppercase letters, lowercase letters, digits, and special characters. |
| instances | Array | Yes | The array of existing ECS instances. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| format disk _ | bool | No | Specifies whether to format data disks. |
| key pair _ | string | No | The name of the key pair. For Windows-based instances, ignore this parameter. Default value: empty. For Linux-based instances, the Passw ord parameter still takes effect if you set this parameter. For Linux-based instances, if you set this parameter, password authentication is disabled. |

Response Response f ormat

```
HTTP/1.1 202 OK
```

Cust om response headers None. For more information, see Common response headers. Response body

```json
    "list": [
            "code": "200",
            "instanceId": "i-2zee3oiwcyoz7kwdo8bt",
            "message": "successful"
```

`},`

```json
            "code": "200",
            "instanceId": "i-2ze0lgm3y6iylcbtcypf",
            "message": "successful"
```

`],`

```json
    "task_id": "T-5a544aff80282e39ea000039"
```

Examples Sample request s

```json
POST /clusters/Cccfd68c474454665ace07efce924f75f/attach HTTP/1.1 <Common request headers>
    "password": "Hello1234",
    "instances": [
        "i-xxxx",
        "i-yyyy"
```

`]` Sample success responses

```json
HTTP/1.1 202 Accepted <Common response headers>
    "list": [
            "code": "200",
            "instanceId": "i-xxxx",
            "message": "successful"
```

`},`

```json
            "code": "200",
            "instanceId": "i-yyyy",
            "message": "successful"
```

`],`

```json
    "task_id": "T-5a544aff80282e39ea000039"
```

### 2.4 Get kubeconfig files

Get the kubeconfig file that contains information about the current user. kubeconfig files are used to configure access to clusters. Request Request f ormat

```
GET /k8s/:clusterid/user_config
```

Cust om request headers None. See Common request headers. Response Response f ormat

```
HTTP/1.1 200 OK
```

Cust om response headers None. See Common response headers. Response body

```json
    "config": "string"
```

Response body paramet ers

| Name | Type | Description |
|---|---|---|
| config | string | The kubeconfig file that contains information about the current user. |

Example Sample request

```
GET /k8s/c5b5e80b0b64a4bf6939d2d8fbbc5ded7/user_config HTTP/1.1 <Common request header>
```

Sample response

```json
HTTP/1.1 200 OK <Common response header>
     "config": "xxxxxxxx"
```

### 2.5 Query detailed information of a cluster

cluster You can call this operation to query detailed information of a cluster by cluster ID. Request Request f ormat

```
GET /clusters/{cluster_id} HTTP/1.1
```

Request paramet ers

| Parameter | Type | Required | Description |
|---|---|---|---|
| cluster id _ | string | Yes | The ID of the cluster that you want to query. |

Cust om request headers None. For more information, see Common request headers. Request body None. Response Response f ormat

```
HTTP/1.1 200 OK
```

Cust om response headers None. For more information, see Common response headers. Response body

```json
    "agent_version": "string",
    "cluster_id": "string",
    "created": "datetime",
    "external_loadbalancer_id": "string",
    "master_url": "string",
    "name": "string",
    "network_mode": "string",
    "region_id": "string",
    "security_group_id": "string",
    "size": "numbers",
    "state": "string",
    "updated": "datetime",
    "vpc_id": "string",
    "vswitch_id": "string"
```

Response body paramet ers Cluster details

| Parameter | Type | Description |
|---|---|---|
| agent version _ | string | The version of the agent. |
| cluster id _ | String | The unique identifier of the cluster. |
| created | string | The time when the cluster was created. |
| external loadbalancer id _ _ | String | The ID of the Server Load Balancer (SLB) instance that is deployed in the cluster. |

| Parameter | Type | Description |
|---|---|---|
| master url _ | string | The address of the master nodes in the cluster. You can use this address to connect to the cluster. For more information, see the "Connect to a master node by using SSH" topic of Container Service for Kubernetes User Guide. |
| name | string | The cluster name that you specified when you created the cluster. The cluster name must be unique for each Apsara Stack tenant account. |
| network mode _ | String | The network type. vpc indicates the Virtual Private Cloud (VPC) network. |
| region id _ | String | The ID of the region where the cluster is located. |
| security group id _ _ | String | The ID of the security group. |
| size | String | The number of nodes in the cluster. |
| state | String | The state of the cluster. |
| updated | string | The last update time. |
| vpc id _ | string | The ID of the VPC. |
| vswitch id _ | string | The ID of the VSwitch. |

Examples Sample request s

```
GET /clusters/C5b5e80b0b64a4bf6939d2d8fbbc5ded7 HTTP/1.1 <Common request headers>
```

Sample success responses

```json
HTTP/1.1 200 Ok <Common response headers>
    "agent_version": "0.5-e56dab3",
    "cluster_id": "c978ca3eaacd3409a9437db07598f****",
    "created": "2015-12-11T03:52:40Z",
    "external_loadbalancer_id": "1518f2b7e4c-cn-beijing-btc-***",
    "master_url": "https://182.92. **.**:****",
    "name": "my-python-cluster-039d****",
    "network_mode": "vpc",
    "region_id": "cn-beijing",
    "security_group_id": "sg-25yqj***",
    "size": 5,
    "state": "running",
    "updated": "2015-12-15T15:01:58Z",
    "vpc_id": "",
    "vswitch_id": ""
```

### 2.6 Scale out Kubernetes clusters

You can call this operation to increase the number of worker nodes in a cluster. This operation is only applicable to resources created by Resource Orchestration Service (ROS). Request Request f ormat

```
PUT /clusters/{cluster_id} HTTP/1.1
```

Request paramet ers

| Parameter | Type | Required | Description |
|---|---|---|---|
| cluster id _ | string | Yes | The ID of the cluster that you want to manage. |

Cust om request headers None. For more information, see Common request headersCommon request headers. Request body

```json
    "disable_rollback": "Specifies whether to disable rollback if the operation fails.",
    "timeout_mins": "The timeout period for the system to create a cluster.",
    "worker_instance_type": "The instance types of the worker nodes.",
    "login_password": "The SSH login password of the worker nodes.",
    "num_of_nodes": "The number of worker nodes."
```

Request body paramet ers

| Parameter | Type | Required | Description |
|---|---|---|---|
| disable rollback _ | bool | Yes | Specifies whether to disable rollback when the operation fails. true: Rollback is disabled. false: Rollback is enabled. If you choose to enable rollback when the operation fails, resources that are created during the operation are released. We recommend that you set the value to true. |
| timeout mins _ | int | Yes | The timeout period for the system to create a cluster stack. Unit: minutes. Default value: 60. |
| worker instance type _ _ | string | Yes | The instance types of the worker nodes. For more information, choose User Guide > Elastic Compute Service (ECS) > What is ECS? > Instances types and see the list of instance families . |

| Parameter | Type | Required | Description |
|---|---|---|---|
| login password _ | string | Yes | The SSH logon password. The password must be 8 to 30 characters in length and contain letters, numbers, and special characters. The password must be the same as the password you specified when you created the cluster. Not e You can set only either login password or _ num of nodes. _ _ You must set the parameter that you set when you created the cluster. |
| num of nodes _ _ | int | Yes | The number of worker nodes. Valid values: [0,300] To expand the cluster, you must specify a value that is greater than the number of existing worker nodes. Not e You can set only either login password or _ num of nodes. _ _ You must set the parameter that you set when you created the cluster. |

Response Response f ormat

```
HTTP/1.1 202 Accepted
```

Cust om response headers None. For more information, see Common response headers. Response body

```json
    "cluster_id":"string",
    "request_id":"string",
    "task_id":"string"
```

Examples Sample request s

```json
PUT /clusters/Cccfd68c474454665ace07efce924f75f HTTP/1.1 <Common request headers>
    "disable_rollback": true,
    "timeout_mins": 60,
    "worker_instance_type": "ecs.sn1ne.large",
    "login_password": "Hello1234"
```

Sample success responses

```json
HTTP/1.1 202 Accepted <Common response headers>
    "cluster_id": "<yourClusterId>",
    "request_id": "687C5BAA-D103-4993-884B-C35E4314A1E1",
    "task_id": "T-5a54309c80282e39ea00002f"
```

### 2.7 Delete clusters

Delete clusters by cluster ID and release all nodes in the clusters. Request Request f ormat

```
DELETE /clusters/{cluster_id} HTTP/1.1
```

Request paramet ers

| Name | Type | Required | Description |
|---|---|---|---|
| cluster id _ | string | Yes | The ID of the cluster. |

Cust om request headers None. See Common request headers. Request body None. Response Response f ormat

```
HTTP/1.1 202 Accepted
```

Cust om response headers None. See Common response headers. Response body None. Example Sample request

```
DELETE /clusters/Cccfd68c474454665ace07efce924f75f HTTP/1.1 <Common request header>
```

Sample response

```
HTTP/1.1 202 Accepted <Common response header>
```
