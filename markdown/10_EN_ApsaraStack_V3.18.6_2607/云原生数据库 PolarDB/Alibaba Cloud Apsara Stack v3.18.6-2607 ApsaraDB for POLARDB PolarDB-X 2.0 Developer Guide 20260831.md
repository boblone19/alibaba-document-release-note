---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 ApsaraDB for POLARDB PolarDB-X 2.0 Developer Guide 20260831"
product_version: "V3.18.6_2607"
doc_version: "20260831"
pdf_pages: 179
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 ApsaraDB for POLARDB PolarDB-X 2.0 Developer Guide 20260831.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E5%8E%9F%E7%94%9F%E6%95%B0%E6%8D%AE%E5%BA%93%20PolarDB/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20ApsaraDB%20for%20POLARDB%20PolarDB-X%202.0%20Developer%20Guide%2020260831.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 ApsaraDB for POLARDB PolarDB-X 2.0 Developer Guide 20260831

se the SDK for Java

## Use the SDK for Java

### Use the SDK

#### Configure connection requests

This topic describes how to configure a connection request by using the HttpClientConfig object. You can use the following code to configure the HttpClientConfig object. We recommend that you select and configure the following parameters based on your business requirements.

**Note**

Replace the variables in the following sample code with actual values. Do not retain the angle brackets (<>) in the final code. The following section describes the variables: <readTimeout>: Specify a read timeout period based on your business requirements. Unit: milliseconds. <connectionTimeout>: Specify a connection timeout period based on your business requirements. Unit: milliseconds. <maxRequestsPerHost>: Specify the maximum number of requests that are supported by each server based on your business requirements. The supported data type is INTEGER. <maxRequests>: Specify a maximum number of requests based on your business requirements. The supported data type is INTEGER. <http://192.168.XX.XX:33XX>: Replace this variable with the IP address and port of the proxy that you use. se the SDK for Java

```
// Obtain the HttpClientConfig object. HttpClientConfig clientConfig = HttpClientConfig.getDefault(); // Specify whether to ignore certificates. clientConfig.setIgnoreSSLCerts(true); // (Optional) Specify a read timeout period. Unit: milliseconds. clientConfig.setReadTimeoutMillis(<readTimeout>); // (Optional) Specify a connection timeout period. Unit: milliseconds. clientConfig.setConnectionTimeoutMillis(<connectionTimeout>); // (Optional) Specify the maximum number of requests that are supported by each server. The supported data type is INTEGER. clientConfig.setMaxRequestsPerHost(<maxRequestsPerHost>); // (Optional) Specify a maximum number of requests. The supported data type is INTEGER. clientConfig.setMaxRequests(<maxRequests>); // (Optional) Specify a protocol type. clientConfig.setProtocolType(ProtocolType.HTTP); /** (Optional) Specify whether to configure a proxy based on your business requirements. Sample code: clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
```

`or`

```
clientConfig.setHttpsProxy("<https://192.168.XX.XX:33XX>"); Replace https://192.168.XX.XX:33XX with the actual IP address and port of the proxy tha t you use.
```

`*/`

```
profile.setHttpClientConfig(clientConfig);
```

#### Error handling

If an error occurs on the server or in the SDK when you use Apsara Stack SDK for Java, an error response is returned. The error response contains an error code and an error message. In most cases, you do not need to handle the errors returned by the SDK for Java. You need to only handle the errors returned by the server based on error messages. `ServerException` indicates a server error. `ClientException` indicates an SDK error. The following error indicates that the AccessKey ID is invalid. You must specify a valid AccessKey ID.

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

If you want to handle the SDK errors returned by Apsara Stack SDK for Java, refer to the following example to write your code: se the SDK for Java

```java
try {
    FooResponse response = client.getAcsResponse(request);
    // Handle the response.
}catch (ServerException e){
    // Add your own error handling logic here.
    // For example, print the specific error information.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
    // If you encounter a difficult issue, submit a ticket and provide the RequestId.
    System.out.println("ResponseId=" + e.getRequestId());
}catch (ClientException e){
    // Add your own error handling logic here.
    // For example, print the specific error information.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
```

`}` se the SDK for Python

## Use the SDK for Python

### Use the SDK

#### Configure HTTPS requests

Apsara Stack SDK for Python allows you to initiate API requests over HTTP and HTTPS. You can specify the HTTP or HTTPS protocol for a specific request, or set a global default protocol.

**Note**

The default protocol (HTTP or HTTPS) of a service takes precedence over the global default protocol.

**Add OpenSSL support**

OpenSSL support in Python is required for sending HTTPS requests by using the SDK for Python. To use Apsara Stack SDK for Python to send HTTPS requests, you must add OpenSSL support in Python. OpenSSL supports TLS 1.2 and later. Run the `python -c "import ssl"` command to check whether your Python environment supports OpenSSL. If the following error message is not displayed, OpenSSL is supported: ImportError: No module named ssl If OpenSSL is not installed in your Python environment, run the following command to install OpenSSL:

```
pip install pyopenssl
```

.

**Set the protocol to HTTP or HTTPS for a request**

The following sample code shows how to configure HTTPS as the protocol for a request:

```bash
request = DescribeInstancesRequest() request.set_protocol_type("https")
# Set the value to https or http.
```

**Set a global default protocol**

The following sample code shows how to specify a global default protocol:

```java
import aliyunsdkcore.request aliyunsdkcore.request.set_default_protocol_type("https")
# Create a request and call client.do_action_with_exception() to send the request.
```

#### Handle errors

If the server or SDK encounters an error when you use the SDK for Python, the SDK returns an error response. The error response contains an error code and an error message. se the SDK for Python Among the errors returned by the SDK for Python, you do not need to handle the SDK errors, but must solve the server errors. `ServerException` indicates a server error. `ClientException` indicates an SDK error. For example, if the following error occurs, you can modify the AccessKey ID based on the error message:

```
aliyunsdkcore.acs\_exception.exceptions.ServerException: HTTP Status: 404 Error:InvalidAccessKeyId.NotFound Specified access key is not found.
```

If you want to handle the SDK errors returned by the SDK, refer to the following example to write your code:

```bash
try:
    response = client.do_action_with_exception(request)
except ServerException as e:
    # You can add your error handling logic here.
    # For example, display the error message.
    print e.get_http_status()
    print e.get_error_code()
    print e.get_error_msg()
```

se the SDK for Go

## Use the SDK for Go

### Use the SDK

#### Install the core package of Apsara

**Stack SDK for Go**

This topic describes how to install the core package of Apsara Stack SDK for Go. Apsara Stack SDK for Go supports Go 1.10.x and later. You can run the following command to install the core package:

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

## API Reference

### Request structure

PolarDB-X exposes a Query API that accepts HTTP GET requests with URL-encoded parameters. This reference covers the regional endpoints, supported protocols, request URL format, parameter types, and encoding requirements.

**Endpoint**

To query the endpoint:
1. In the Apsara Uni-manager Management Console, choose **Products > Development**
**Tools > OpenAPI Explorer**.
2. In the top menu, click **API Integration** and click **API Debugging**. Search for polardbx in
the product list on the right.
3. In the displayed API list, click any API to view its endpoint.

**Protocols**

PolarDB-X supports both HTTP and HTTPS. Use HTTPS to keep data secure in transit.

**Request syntax**

All PolarDB-X API calls use HTTP GET. Construct the request URL as follows:

```
http://Endpoint/?Action=xx&Parameters
```

**Note**

**Endpoint**: the regional endpoint for the PolarDB-X API. For more information, see
Endpoint.
**Action**: the name of the API operation to call, such as DescribeTables, which can
be called to query data tables of a created distributed relational database.
**Version**: the API version. Always set it to 2020-02-02.
**Parameters**: operation-specific parameters, separated by ampersand (&).
Request parameters consist of common request parameters and operation-specific parameters. Common parameters include the API version and authentication information. For more information, see Common parameters.

**Request parameters**

Each request must specify the operation to perform by using the Action parameter (such as CreateDatabase). Each operation requires common request parameters and operationspecific request parameters.

**Character encoding**

The system encodes all requests and responses in UTF-8.

### Common parameters

This topic describes the common parameters that can be used to call each API operation in PolarDB-X. Common parameters include request parameters and response parameters.

**Common request parameters**

| Parameter | Type | Requi red | Description |
|---|---|---|---|
| Format | Strin g | No | The format in which to return the response. Valid values: JSON and XML. Default value: JSON. |
| Version | Strin g | Yes | The version number of the API. Specify the version number in the YYYY-MM-DD format. Set the value to 2020-02-02. |
| AccessKeyId | Strin g | Yes | The AccessKey ID that is used to connect to PolarDB-X. |
| Signature | Strin g | Yes | The signature string of the current request. |
| SignatureMe thod | Strin g | Yes | The encryption method of the signature string. Set the value to HMAC-SHA1. |
| Timestamp | Strin g | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. For example, if you want to specify 20:00:00 (UTC+8) on January 10, 2013 as the value of the timestamp, set the value to 2013- 01-10T12:00:00Z. |
| SignatureVer sion | Strin g | Yes | The version of the signature encryption algorithm. Set the value to 1.0. |
| SignatureNo nce | Strin g | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |
| ResourceOw nerAccount | Strin g | No | The name of the account that owns the resource that you want to access. You can use this account to log on to PolarDB-X to call API operations. |

**Common response parameters**

API responses use the HTTP response format. Responses can be returned in the JSON or XML format. You can specify the response format in the request. The default response format is XML. Each response returns a unique **RequestId** regardless of whether the call is successful. A `2xx` status code indicates a successful call. A `4xx` or `5xx` status code indicates a failed call. Sample responses: XML format

```xml
<?xml version="1.0" encoding="utf-8"?>
    <!--Result Root Node-->
    <Interface Name+Response>
        <!--Return Request Tag-->
        <RequestId>4C467B38-3910-447D-87BC-AC0491******</RequestId>
        <!--Return Result Data-->
    </Interface Name+Response>
```

JSON format `{`

```json
    "RequestId":"4C467B38-3910-447D-87BC-AC0491******",
    /*Return Result Data*/
```

`}`

### Performance parameters

This topic describes the parameters that are used to monitor the performance of compute nodes, data nodes, Global Meta Service (GMS) nodes, and change data capture (CDC) nodes in PolarDB-X instances.

**Parameters related to compute nodes**

| API parameter | Description |
|---|---|
| Cpu Usage _ | The CPU utilization as a percentage value. |
| Mem Usage _ | The usage of heap memory of a Java Virtual Machine (JVM) as a percentage value. The value of this parameter is calculated based on the following formula: Usage of JVM heap memory = Amount of the used JVM heap memory/Total amount of JVM heap memory × 100%. |
| Logic RT _ | The average response time of requests that are sent by users. Unit: microseconds. The value of this parameter is calculated based on the following formula: Response time of a request = Point in time at which the result of the request is returned - Point in time at which the request is received. |
| Physical RT _ | The average response time of requests that are sent from compute nodes to data nodes. Unit: microseconds. The value of this parameter is calculated based on the following formula: Response time of a request = Point in time at which the compute node receives the result from the data node - Point in time at which the compute node sends the request to the data node. |
| Logic QPS _ | The average number of user requests that are processed per second. |

| Logic TPS _ | The average number of transactions that are processed per second. |
|---|---|
| Physical QPS _ | The average number of requests that are sent to data nodes per second. |
| Network Usage _ | The network throughput, which indicates the sum of the inbound traffic and the outbound traffic per second. Unit: byte/s. |
| Connections | The number of connections. The following data can be returned: active connection: the total number of _ connections. connection count: the number of connections _ that are created per second. |
| Thread Detail _ | The number of active connections. |
| JVM CollectorTime _ | The average period of time that is required to perform garbage collection (GC) per second. The unit of the value is nanoseconds. The following data can be returned: The average period of time that is required to perform GC in the young generation space per second. The average period of time that is required to perform full GC per second. |
| Slow RequestCount _ | The following data can be returned: The average number of slow SQL requests that are sent by users per second. The average number of slow SQL requests that are sent to data nodes per second. |

**Parameters related to data nodes or GMS nodes**

| API parameter | Description |
|---|---|
| MySQL NetworkTraffic _ | The following data can be returned: The average amount of inbound traffic to the PolarDB-X instance per second. Unit: KB. The average amount of outbound traffic from the PolarDB-X instance per second. Unit: KB. |
| MySQL QPSTPS _ | The following data can be returned: The average number of SQL statements that are executed per second. The average number of transactions that are processed per second. |
| MySQL Sessions _ | The following data can be returned: The number of active connections. The total number of connections. |

| MySQL InnoDBBufferRatio _ | The following data can be returned: The read hit ratio of the InnoDB buffer pool. The usage of the InnoDB buffer pool. The dirty ratio of the InnoDB buffer pool. |
|---|---|
| MySQL InnoDBDataReadWriten _ | The following data can be returned: The average volume of data that InnoDB reads per second. Unit: KB. The average volume of data that InnoDB writes per second. Unit: KB. |
| MySQL InnoDBLogRequests _ | The following data can be returned: The average number of read operations that are performed on an InnoDB buffer pool per second. The average number of write operations that are performed on an InnoDB buffer pool per second. |
| MySQL InnoDBLogWrites _ | The following data can be returned: The average number of log write requests that are processed per second. The average number of physical writes that are performed on log files per second. The average number of operations that are performed by using the fsync() function to write data to log files per second. |
| MySQL TempDiskTableCreates _ | The number of temporary tables that are automatically created on the hard disk during statement execution. |
| MySQL COMDML _ | The following data can be returned: The average number of times for which the DELETE statements are executed per second. The average number of times for which the INSERT statements are executed per second. The average number of times for which the INSERT SELECT statements are executed per _ second. The average number of times for which the REPLACE statements are executed per second. The average number of times for which the REPLACE SELECT statements are executed per _ second. The average number of times for which the SELECT statements are executed per second. The average number of times for which the UPDATE statements are executed per second. |

| MySQL RowDML _ | The following data can be returned: The average number of rows that are read from an InnoDB table per second. The average number of rows that are updated in an InnoDB table per second. The average number of rows that are deleted from an InnoDB table per second. The average number of rows that are inserted into an InnoDB table per second. The average number of physical writes that are performed on log files per second. |
|---|---|
| MySQL MemCpuUsage _ | The following data can be returned: The CPU utilization of the PolarDB-X instance. The memory usage of the PolarDB-X instance. |
| MySQL IOPS _ | The IOPS of the PolarDB-X instance. |
| MySQL DetailedSpaceUsage _ | The following data can be returned: The used storage of the PolarDB-X instance. The data storage. The log storage. The temporary storage. The system storage. |
| slavestat | The replication delay between the primary instance and the read-only instances. |
| MySQL ThreadStatus _ | The following data can be returned: the number of active threads and the number of connected threads. |
| MySQL ReplicationDelay _ | The replication delay between the primary instance and the secondary instance. Unit: seconds. |
| MySQL ReplicationThread _ | The following data can be returned: the states of I/O threads and SQL threads based on which data can be replicated. The value 1 indicates that the related threads are normal. The value 0 indicates that the related threads are lost. |
| IOPSUsage | The IOPS usage as a percentage value. |
| MySQL Slow Queries _ _ | The average number of slow SQL requests that are processed per second. |

**Parameters related to CDC nodes**

| API parameter | Description |
|---|---|
| Cdc DumperDelay _ | The latency that occurs when binary log events are being processed. Unit: milliseconds. |
| Cdc DumperThroughput _ | The data size of binary log events that are processed per second. Unit: byte/s. |

| Cdc CpuUsage _ | The CPU utilization as a percentage value. |
|---|---|
| Cdc DumperHeapUsage _ | The usage of JVM heap memory as a percentage value. The value of this parameter is calculated based on the following formula: Usage of JVM heap memory = Amount of the used JVM heap memory/Total amount of JVM heap memory × 100%. |
| Cdc DumperOps _ | The information about binary log events that are processed. The following data can be returned: dumper total eps: the average number of _ _ binary log events that are processed per second. dumper dml eps: the average number of _ _ binary log events during which DML statements are executed per second. dumper tps: the average number of _ transactions that are processed per second. |

### Instance states

| State | Description |
|---|---|
| Creating | The instance is being created. |
| Running | The instance is running. |
| Deleting | The instance is being deleted. |
| Rebooting | The instance is restarting. |
| DBInstanceClassChanging | The instance is being upgraded or downgraded. |
| TRANSING | The instance is being migrated. |
| EngineVersionUpgrading | The version of the database engine that the instance runs is being upgraded. |
| TransingToOthers | The data of the PolarDB-X instance is being migrated to an ApsaraDB RDS for MySQL instance. |
| GuardDBInstanceCreating | A disaster recovery instance is being created for the instance. |
| Restoring | The instance is being restored from a backup. |
| Importing | Data is being imported to the instance. |
| ImportingFromOthers | Data is being imported to the PolarDB-X instance from an ApsaraDB RDS for MySQL instance. |
| DBInstanceNetTypeChanging | The network type of the instance is being changed. |

| GuardSwitching | A failover operation is being performed for an instance in a disaster recovery scenario. |
|---|---|
| INS CLONING _ | The instance is being cloned. |
| Released | The instance is released. |

### Instance management

#### CreateDBInstance

Call the CreateDBInstance operation to create a PolarDB-X instance.

**Request headers**

This operation uses common request headers only. For more information, see Common request parameters.

**Request parameters**

| Paramete r | Typ e | Posi stio n | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Quer y | Yes | cn-hangzhou | The region where the instance resides. |
| Action | Strin g | Syst em | No | CreateDBInstance | The action that you want to perform. Set the value to CreateDBInstance. |
| PayType | Strin g | Quer y | No | PREPAY | The billing method of the instance. Valid values: PREPAY: subscription POSTPAY: pay-as-you- go |
| DBNodeCo unt | Integ er | Quer y | No | 2 | The number of instance nodes. The minimum value is 2. |
| DBNodeCl ass | Strin g | Quer y | No | polarx.x4.2xlarge.2d | The node specification, for example, polarx.x4.2xlarge.2e, which indicates 16 CPU cores and 64 GB memory. |
| CNNodeCo unt | Integ er | Quer y | No | 2 | The number of compute nodes. |

| CNNodeCl ass | Strin g | Quer y | No | polarx.x4.medium.2e | The compute node specification. |
|---|---|---|---|---|---|
| DNNodeCo unt | Integ er | Quer y | No | 2 | The number of storage nodes. |
| DNNodeCl ass | Strin g | Quer y | No | mysql.n4.medium.25 | The storage node specification. |
| ZoneId | Strin g | Quer y | Yes | cn-hangzhou-a | The zone of the instance. |
| ClientToke n | Strin g | Quer y | No | xxxxxx-xxx | A client-generated token that is used to ensure the idempotence of the request. Make sure that the token is unique for each request. |
| NetworkTy pe | Strin g | Quer y | No | vpc | The network type. vpc: virtual private cloud (VPC) classic: lassic network |
| VPCId | Strin g | Quer y | No | vpc-***** | The ID of the VPC. |
| VSwitchId | Strin g | Quer y | No | vsw-********* | The ID of the vSwitch. |
| UsedTime | Integ er | Quer y | No | 1 | For a subscription, specify the duration in months or years. |
| Period | Strin g | Quer y | No | Month | The unit of a billing cycle. For subscription instances, you can select Year or Month. For pay- as-you-go instances, Hour is selected by default. |
| ResourceG roupId | Strin g | Quer y | No | null | The resource group ID. This parameter can be empty. |

| AutoRene w | Bool ean | Quer y | No | true | Specifies whether to enable auto-renewal. Default value: true. true: Enable auto- renewal. false: Disable auto- renewal. |
|---|---|---|---|---|---|
| EngineVer sion | Strin g | Quer y | No | 5.7 | The MySQL engine version. Valid values: 5.7 and 8.0. Default value: 5.7. |
| IsReadDBI nstance | Bool ean | Quer y | No | false | Specifies whether the instance is a read-only instance. true: The instance is a read-only instance. false: The instance is not a read-only instance. |
| PrimaryDB InstanceN ame | Strin g | Quer y | No | pxc-********* | If the instance is a read- only instance, you must specify the primary instance. |
| TopologyT ype | Strin g | Quer y | No | 3azones | The topology type. Valid values: 3azones: three-zone deployment 1azone: single-zone deployment |
| PrimaryZo ne | Strin g | Quer y | No | cn-shenzhen-e | The primary zone. |
| Secondary Zone | Strin g | Quer y | No | cn-shenzhen-a | The secondary zone. |
| TertiaryZo ne | Strin g | Quer y | No | cn-shenzhen-e | The tertiary zone. |
| Series | Strin g | Quer y | No | enterprise | enterprise: Enterprise Edition standard: Standard Edition |

| IsColumna rReadDBIn stance | Bool ean | Quer y | No | true | Specifies whether the instance to create is a column-store read-only instance. |
|---|---|---|---|---|---|
| IPVersion | Strin g | Quer y | No | IPv4 | The IP version. This parameter is optional. Default value: IPv4. Valid values: IPv4 IPv4v6 |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9B2F3840-5C98- 475C-B269- 2D5C3A31797C | The request ID. |
| DBInstanceNa me | String | pxc-********* | The name of the created instance. |
| OrderId | String | 12345 | The order ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateDBInstance &RegionId=cn-hangzhou &ZoneId=cn-hangzhou-a &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"9B2F3840-5C98-475C-B269-2D5C3A31797C",
 "OrderId":"12345",
 "DBInstanceName":"pxc-*********"
```

`}` `XML` format

```xml
<RequestId>9B2F3840-5C98-475C-B269-2D5C3A31797C</RequestId> <OrderId>12345</OrderId> <DBInstanceName>pxc-*********</DBInstanceName>
```

#### DeleteDBInstance

Deletes a PolarDB-X instance.

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates sample code for different SDKs.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteDBInstanc e | The operation to perform. Set the value to DeleteDBInstan ce. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. |
| DBInstanceName | String | Yes | pxc-******** | The name of the instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9B2F3840-5C98-475C- B269-2D5C3A31797C | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteDBInstance &RegionId=cn-hangzhou &DBInstanceName=pxc-******** &<Common request parameters>
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <DeleteDBInstanceResponse>
    <RequestId>9B2F3840-5C98-475C-B269-2D5C3A31797C</RequestId>
</DeleteDBInstanceResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "RequestId" : "9B2F3840-5C98-475C-B269-2D5C3A31797C"
```

`}`

#### DescribeDBInstanceAttribute

Call the DescribeDBInstanceAttribute API to query the attributes of an instance.

**Debug**

You can run this API directly in OpenAPI Explorer without the need to calculate the signature. After a successful run, OpenAPI Explorer automatically generates SDK code examples.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInsta nceAttribute | The required parameter. Set the value to DescribeDBInstanceAttribute. |
| RegionId | String | Yes | cn-hangzhou | The region where the instance resides. |
| DBInstanceNam e | String | Yes | pxc-******** | The name of the instance. |
| ResourceGroupI d | String | No | rg- aekzaxhezhs5** * | The ID of the resource group. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9B2F3840-5C98- 475C-B269- 2D5C3A31797C | The ID of the request. |
| DBInstance | Object |   | The information about the database instance. |

| Type | String | ReadWrite | The instance type. Valid values: ReadWrite: primary instance ReadOnly: read-only instance |
|---|---|---|---|
| Status | String | Running | The status of the instance. For more information, see Instance state table. |
| RightsSeparati onStatus | String | disabled | The status of the three-role mode. Valid values: disabled: The three-role mode is not enabled. enabled: The three-role mode is enabled. processing: The system is processing the request. unknown: The status is unknown. This may occur because the instance is unreachable. |
| DBNodeCount | Integer | 2 | The number of nodes in the instance. |
| Expired | String | false | Indicates whether the instance has expired. Valid values: true: The instance has expired. false: The instance is running normally. |
| CreateTime | String | 2021-08- 31T08:56:25.000+ 0000 | The time when the instance was created. |
| PayType | String | Postpaid | The billing method of the instance. Valid values: Postpaid: pay-as-you-go Prepaid: subscription billing |
| Port | String | 3306 | The intranet connection port. |

| LockMode | String | Unlock | The lock mode of the instance. Valid values: Unlock: The instance is not locked. ManualLock: The instance is manually locked. LockByExpiration: The instance is automatically locked due to expiration. LockByRestoration: The instance is automatically locked before a rollback. LockByDiskQuota: The instance is automatically locked because the storage is full. LockReadInstanceByDiskQuota: The read-only instance is automatically locked because the storage is full. |
|---|---|---|---|
| Description | String | test instance | The description of the instance. |
| ConnectionStri ng | String | pxc- sprpx766******.pol arx.singapore.rds.a liyuncs.com | The intranet connection information. |
| StorageUsed | Long | 1704250**** | The used storage capacity. |
| ExpireDate | String | 2022-08- 31T16:00:00.000+ 0000 | The expiration time. The format is yyyy- MM-ddTHH:mm:ss.sss+0000 (UTC time). |
| CommodityCo de | String | drds polarxpost pu _ _ blic cn _ | The commodity type of the instance. The value is fixed as drds polarxpost public cn. _ _ _ |
| MaintainStartT ime | String | 06:00 | The start time of the maintenance window for the instance. This value is in UTC time. Add 8 hours to obtain the maintenance window displayed in the console. |
| DBInstanceTy pe | String | ReadWrite | The instance type. Valid values: ReadWrite: primary instance ReadOnly: read-only instance |
| DBNodeClass | String | polarx.x4.large.2e | The specification of the instance node. |

| LatestMinorVe rsion | String | polarx- kernel 5.4.11- _ 16301083 xcluster _ -20210805 | The latest kernel version that the current instance supports. |
|---|---|---|---|
| MaintainEndTi me | String | 06:00 | The end time of the maintenance window for the instance. This value is in UTC time. Add 8 hours to obtain the maintenance window displayed in the console. |
| DBType | String | polarx | The database engine. The value is fixed as polarx. |
| RightsSeparati onEnabled | Boolean | false | The status of the three-role mode. Valid values: false: The three-role mode is not enabled. true: The three-role mode is enabled. |
| VPCId | String | vpc-xxxxx | The ID of the VPC. |
| MinorVersion | String | polarx- kernel 5.4.11- _ 16301083 xcluster _ -20210805 | The current kernel version. |
| RegionId | String | cn-hangzhou | The region where the instance resides. |
| Network | String | VPC | The network type of the instance. Valid values: Classic: classic network VPC: VPC |
| DBVersion | String | 5.5 | The database version. |
| VSwitchId | String | vsw-xxxxxx | The vSwitch ID. |
| ZoneId | String | cn-hangzhou-a | The availability zone where the instance resides. |
| Engine | String | MySQL | The database engine. The value is fixed as MySQL. |
| KindCode | Integer | 18 | The engine version of the instance. This is an internal parameter. |

| Id | String | rm- uf6wjk5xxxxxxxxxx | The ID of the primary instance. If this parameter is not returned, the instance is a primary instance. |
|---|---|---|---|
| DBNodes | Array of DBNode |   | The information of the database nodes. |
| ComputeNodeI d | String | pxc-i-xxxxxx | The name of the compute node. |
| NodeClass | String | polarx.x4.large.2e | The specification of the node. |
| DataNodeId | String | pxc-xdb-xxxxxx | The name of the storage node. |
| ZoneId | String | cn-hangzhou-a | The name of the availability zone where the node resides. |
| Id | String | pxi-xxxxxx | The ID of the logical node. |
| RegionId | String | cn-hangzhou | The ID of the region where the node resides. |
| ConnAddrs | Array of ConnAddr |   | The endpoint information. |
| Type | String | VPC | The connection type. VPC indicates an intranet connection, and PUBLIC indicates an Internet connection. |
| VSwitchId | String | vsw-xxxxxx | The vSwitch ID. |
| Port | Long | 3306 | The connection port number. |
| VPCId | String | vpc-xxxxxx | The ID of the VPC. |
| ConnectionStri ng | String | polardbx- xxx.aliyuncs.com | The endpoint. |
| ReadDBInstan ces | Array of String | pxr-xxxxxx | The names of the read-only instances. |

| ResourceGrou pId | String | rg-xxxx | The ID of the resource group. |
|---|---|---|---|
| TagSet | Array of TagSet |   | The tag set. |
| Key | String | key2 | The name of the tag. |
| Value | String | value2 | The value of the tag. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeDBInstanceAttribute &RegionId=cn-hangzhou &DBInstanceName=pxc-******** &Common request parameters
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <DescribeDBInstanceAttributeResponse>
    <RequestId>9B2F3840-5C98-475C-B269-2D5C3A31797C</RequestId>
    <DBInstance>
        <Type>ReadWrite</Type>
        <Status>Running</Status>
        <RightsSeparationStatus>disabled</RightsSeparationStatus>
        <DBNodeCount>2</DBNodeCount>
        <Expired>false</Expired>
        <CreateTime>2021-08-31T08:56:25.000+0000</CreateTime>
        <PayType>Postpaid</PayType>
        <Port>3306</Port>
        <LockMode>Unlock</LockMode>
        <Description>test instance</Description>
        <ConnectionString>pxc-
sprpx766******.polarx.singapore.rds.aliyuncs.com</ConnectionString>
        <StorageUsed>1704250****</StorageUsed>
        <ExpireDate>2022-08-31T16:00:00.000+0000</ExpireDate>
        <CommodityCode>drds_polarxpost_public_cn</CommodityCode>
        <MaintainStartTime>06:00</MaintainStartTime>
        <DBInstanceType>ReadWrite</DBInstanceType>
        <DBNodeClass>polarx.x4.large.2e</DBNodeClass>
        <LatestMinorVersion>polarx-kernel_5.4.11-16301083_xcluster-
20210805</LatestMinorVersion>
        <MaintainEndTime>06:00</MaintainEndTime>
        <DBType>polarx</DBType>
<RightsSeparationEnabled>false</RightsSeparationEnabled>
```

```xml
        <RightsSeparationEnabled>false</RightsSeparationEnabled>
        <VPCId>vpc-xxxxx</VPCId>
        <MinorVersion>polarx-kernel_5.4.11-16301083_xcluster-20210805</MinorVersion>
        <RegionId>cn-hangzhou</RegionId>
        <Network>VPC</Network>
        <DBVersion>5.5</DBVersion>
        <VSwitchId>vsw-xxxxxx</VSwitchId>
        <ZoneId>cn-hangzhou-a</ZoneId>
        <Engine>MySQL</Engine>
        <KindCode>18</KindCode>
        <Id>rm-uf6wjk5xxxxxxxxxx</Id>
        <DBNodes>
            <ComputeNodeId>pxc-i-xxxxxx</ComputeNodeId>
            <NodeClass>polarx.x4.large.2e</NodeClass>
            <DataNodeId>pxc-xdb-xxxxxx</DataNodeId>
            <ZoneId>cn-hangzhou-a</ZoneId>
            <Id>pxi-xxxxxx</Id>
            <RegionId>cn-hangzhou</RegionId>
        </DBNodes>
        <ConnAddrs>
            <Type>VPC</Type>
            <VSwitchId>vsw-xxxxxx</VSwitchId>
            <Port>3306</Port>
            <VPCId>vpc-xxxxxx</VPCId>
            <ConnectionString>polardbx-xxx.aliyuncs.com</ConnectionString>
        </ConnAddrs>
        <ReadDBInstances>pxr-xxxxxx</ReadDBInstances>
    </DBInstance>
</DescribeDBInstanceAttributeResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "RequestId" : "9B2F3840-5C98-475C-B269-2D5C3A31797C",
  "DBInstance" : {
    "Type" : "ReadWrite",
    "Status" : "Running",
    "RightsSeparationStatus" : "disabled",
    "DBNodeCount" : 2,
    "Expired" : "false",
    "CreateTime" : "2021-08-31T08:56:25.000+0000",
    "PayType" : "Postpaid",
    "Port" : "3306",
    "LockMode" : "Unlock",
    "Description" : "test instance",
    "ConnectionString" : "pxc-sprpx766vo62nh.polarx.singapore.rds.aliyuncs.com",
    "StorageUsed" : 1704250****,
    "ExpireDate" : "2022-08-31T16:00:00.000+0000",
    "CommodityCode" : "drds_polarxpost_public_cn",
    "MaintainStartTime" : "06:00",
    "DBInstanceType" : "ReadWrite",
```

```json
    "DBNodeClass" : "polarx.x4.large.2e",
    "LatestMinorVersion" : "polarx-kernel_5.4.11-16301083_xcluster-20210805",
    "MaintainEndTime" : "06:00",
    "DBType" : "polarx",
    "RightsSeparationEnabled" : false,
    "VPCId" : "vpc-xxxxx",
    "MinorVersion" : "polarx-kernel_5.4.11-16301083_xcluster-20210805",
    "RegionId" : "cn-hangzhou",
    "Network" : "VPC",
    "DBVersion" : "5.5",
    "VSwitchId" : "vsw-xxxxxx",
    "ZoneId" : "cn-hangzhou-a",
    "Engine" : "MySQL",
    "KindCode" : 18,
    "Id" : "rm-uf6wjk5xxxxxxxxxx",
    "DBNodes" : [ {
      "ComputeNodeId" : "pxc-i-xxxxxx",
      "NodeClass" : "polarx.x4.large.2e",
      "DataNodeId" : "pxc-xdb-xxxxxx",
      "ZoneId" : "cn-hangzhou-a",
      "Id" : "pxi-xxxxxx",
      "RegionId" : "cn-hangzhou"
    } ],
    "ConnAddrs" : [ {
      "Type" : "VPC",
      "VSwitchId" : "vsw-xxxxxx",
      "Port" : 3306,
      "VPCId" : "vpc-xxxxxx",
      "ConnectionString" : "polardbx-xxx.aliyuncs.com"
    } ],
    "ReadDBInstances" : [ "pxr-xxxxxx" ]
```

`}` `}`
```html ``````html ``````html ```

#### DescribeDBInstances

Call the DescribeDBInstances operation to list database instances.

**Debugging**

You can run this operation directly in OpenAPI Explorer without calculating the signature. After a successful run, OpenAPI Explorer automatically generates SDK code examples.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInsta nces | The system-defined parameter. Set the value to DescribeDBInstances. |

| RegionId | String | Yes | cn-hangzhou | The ID of the region where the instance resides. |
|---|---|---|---|---|
| PageNumber | Integer | No | 1 | The page number. Pages start from page 1. |
| PageSize | Integer | No | 20 | The number of entries per page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C458B1E8-1683- 3645-B154- 6BA32080EEA | The request ID. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 30 | The number of entries per page. |
| TotalNumber | Integer | 30 | The total number of entries. |
| DBInstances | Array of DBInstance |   | The queried instances. |
| Type | String | ReadWrite | The instance type. Valid values: ReadWrite: primary instance ReadOnly: read-only instance |
| Status | String | Running | The instance status. |
| CommodityCo de | String | drds polarxpre pu _ _ blic cn _ | The commodity code. |
| ExpireTime | String | 2021-12- 01T16:00:00.000+ 0000 | The expiration time. |
| Expired | Boolean | false | Indicates whether the instance has expired. |

| CreateTime | String | 2021-11- 01T03:49:50.000+ 0000 | The creation time. |
|---|---|---|---|
| PayType | String | Prepaid | The billing method of the instance. Valid values: Postpaid: pay-as-you-go Prepaid: subscription |
| LockReason | String | Overdue payment | The reason for locking. |
| DBType | String | polarx | The database engine. |
| LockMode | String | Unlock | Indicates whether the instance is locked. |
| VPCId | String | VPCID | The Virtual Private Cloud (VPC) ID. |
| MinorVersion | String | polarx- kernel 5.4.12- _ 16349923 xcluster _ -20210926 | The current kernel version. |
| RegionId | String | cn-hangzhou | The region ID. |
| Network | String | VPC | The network type. |
| DBVersion | String | 5.7 | The database version. |
| Description | String | Test | The database description. |
| NodeClass | String | polarx.x4.large.2e | The node type. |
| StorageUsed | Long | 40658534400 | The storage space that is used. |
| NodeCount | Integer | 5 | The number of nodes. |
| ZoneId | String | cn-hangzhou-g | The zone ID. |
| Engine | String | polarx | The engine model. |

| Id | String | pxc-hzr2yeov****** | The instance ID. |
|---|---|---|---|
| Nodes | Array of PolarDBXNode |   | The list of nodes. |
| ZoneId | String | cn-hangzhou-g | The zone ID. |
| Id | String | pxi- zd89wrzqhbfwyuo | The node ID. |
| ClassCode | String | polarx.x4.large.2e | The node type. |
| RegionId | String | cn-hangzhou-g- aliyun | The region ID. |
| ReadDBInstan ces | Array of String | pxr-hzr2yeo****** | The name of the read-only instance. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeDBInstances &RegionId=cn-hangzhou &PageNumber=1 &PageSize=20 &Common request parameters
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <DescribeDBInstancesResponse>
    <RequestId>C458B1E8-1683-3645-B154-6BA32080EEA</RequestId>
    <PageNumber>1</PageNumber>
    <PageSize>30</PageSize>
    <TotalNumber>30</TotalNumber>
    <DBInstances>
        <Type>ReadWrite</Type>
        <Status>Running</Status>
        <CommodityCode>drds_polarxpre_public_cn</CommodityCode>
        <ExpireTime>2021-12-01T16:00:00.000+0000</ExpireTime>
        <Expired>false</Expired>
        <CreateTime>2021-11-01T03:49:50.000+0000</CreateTime>
        <PayType>Prepaid</PayType>
        <LockReason>Overdue payment</LockReason>
        <DBType>polarx</DBType>
        <LockMode>Unlock</LockMode>
        <VPCId>VPCID</VPCId>
        <MinorVersion>polarx-kernel_5.4.12-16349923_xcluster-20210926</MinorVersion>
        <RegionId>cn-hangzhou</RegionId>
        <Network>VPC</Network>
        <DBVersion>5.7</DBVersion>
        <Description>Test</Description>
        <NodeClass>polarx.x4.large.2e</NodeClass>
        <StorageUsed>40658534400</StorageUsed>
        <NodeCount>5</NodeCount>
        <ZoneId>cn-hangzhou-g</ZoneId>
        <Engine>polarx</Engine>
        <Id>pxc-hzr2yeov******</Id>
        <Nodes>
            <ZoneId>cn-hangzhou-g</ZoneId>
            <Id>pxi-zd89wrzqhbfwyuo</Id>
            <ClassCode>polarx.x4.large.2e</ClassCode>
            <RegionId>cn-hangzhou-g-aliyun</RegionId>
        </Nodes>
        <ReadDBInstances>pxr-hzr2yeo******</ReadDBInstances>
    </DBInstances>
</DescribeDBInstancesResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "RequestId" : "C458B1E8-1683-3645-B154-6BA32080EEA",
  "PageNumber" : 1,
  "PageSize" : 30,
  "TotalNumber" : 30,
  "DBInstances" : [ {
    "Type" : "ReadWrite",
    "Status" : "Running",
    "CommodityCode" : "drds_polarxpre_public_cn",
    "ExpireTime" : "2021-12-01T16:00:00.000+0000",
    "Expired" : false,
    "CreateTime" : "2021-11-01T03:49:50.000+0000",
    "PayType" : "Prepaid",
    "LockReason" : "Overdue payment",
    "DBType" : "polarx",
    "LockMode" : "Unlock",
    "VPCId" : "VPCID",
    "MinorVersion" : "polarx-kernel_5.4.12-16349923_xcluster-20210926",
    "RegionId" : "cn-hangzhou",
    "Network" : "VPC",
    "DBVersion" : "5.7",
    "Description" : "Test",
    "NodeClass" : "polarx.x4.large.2e",
    "StorageUsed" : 40658534400,
    "NodeCount" : 5,
    "ZoneId" : "cn-hangzhou-g",
    "Engine" : "polarx",
    "Id" : "pxc-hzr2yeov9jmg3z",
    "Nodes" : [ {
      "ZoneId" : "cn-hangzhou-g",
      "Id" : "pxi-zd89wrzqh******",
      "ClassCode" : "polarx.x4.large.2e",
      "RegionId" : "cn-hangzhou-g-aliyun"
    } ],
    "ReadDBInstances" : [ "pxr-hzr2yeov******" ]
  } ]
```

`}`

#### DescribeScaleOutMigrateTaskList

Queries the progress of a scale-out task.

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | No | DescribeScaleOut MigrateTaskList | The operation that you want to perform. Set the value to DescribeScaleO utMigrateTaskL ist. |
| DBInstanceName | String | Yes | pxc-******** | The ID of the instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Progress | Integer | 32 | The progress of the scale-out task. |
| RequestId | String | C458B1E8-1683-3645- B154-6BA32080EEA | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeScaleOutMigrateTaskList &ResourceOwnerId=111 &DBInstanceName=pxc-******** &<Common request parameters>
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <DescribeScaleOutMigrateTaskListResponse>
    <Progress>32</Progress>
    <RequestId>C458B1E8-1683-3645-B154-6BA32080EEA</RequestId>
</DescribeScaleOutMigrateTaskListResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "Progress" : 32,
  "RequestId" : "C458B1E8-1683-3645-B154-6BA32080EEA"
```

`}`

#### DescribeTasks

Queries the tasks performed on a PolarDB-X instance within a specified time range.

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | No | DescribeTasks | The operation to perform. Set the value to DescribeTasks. |
| DBInstanceId | String | Yes | pxc-hzjasd**** | The name of the instance. |
| StartTime | String | Yes | 2021-11-01 | The beginning of the time range to query. |
| EndTime | String | Yes | 2021-11-04 | The end of the time range to query. |
| PageSize | Integer | No | 20 | The number of entries per page. Valid values: 5 to 1000. |
| PageNumber | Integer | No | 30 | The page number. |
| RegionId | String | Yes | cn-hangzhou | The region where the PolarDB-X instance resides. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D6045D78-C119- 5A17-9DEA- 0F810394E008 | The request ID. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCount | Integer | 30 | The number of entries returned on the current page. |
| TotalRecordCount | Integer | 2 | The total number of entries returned. |

| Items | Array of TaskProgressInfo |   | The list of tasks. |
|---|---|---|---|
| Status | String | RUNNING | The status of the task. Valid values: RUNNING: The task is running. FAILED: The task failed. |
| FinishTime | String | 2021-10- 20T20:00:00Z | The time when the task ended. The time follows the ISO 8601 standard in the yyyy- MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| Progress | String | 80 | The progress of the task, as a percentage. |
| BeginTime | String | 2021-10- 20T19:40:00Z | The time when the task started. The time follows the ISO 8601 standard in the yyyy- MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| TaskErrorCode | String | 400 | The error code. This parameter is returned only for failed tasks. |
| DBName | String | DBName | The name of the database associated with the task. In most cases, an empty string is returned. |
| ProgressInfo | String | ProgressInfo | The details of the task progress. In most cases, an empty string is returned. |
| ScaleOutToken | String | FEA5DC20-6D8A- 5979-97AA- FC57546ADC20 | The token that uniquely identifies the task in the backend. This parameter is returned only for scale-out tasks. |
| TaskId | String | 20089398 | The ID of the task. |
| TaskErrorMessage | String | xxxxxxxx | The error message. This parameter is returned only for failed tasks. |
| TaskAction | String | multi scale out _ _ | The unique identifier of the task type in the backend. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeTasks &DBInstanceId=pxc-hzjasd**** &StartTime=2021-11-01 &EndTime=2021-11-04 &PageSize=20 &PageNumber=30 &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <DescribeTasksResponse>
    <RequestId>D6045D78-C119-5A17-9DEA-0F810394E008</RequestId>
    <PageNumber>1</PageNumber>
    <PageRecordCount>30</PageRecordCount>
    <TotalRecordCount>2</TotalRecordCount>
    <Items>
        <Status>RUNNING</Status>
        <FinishTime>2021-10-20T20:00:00Z</FinishTime>
        <Progress>80</Progress>
        <BeginTime>2021-10-20T19:40:00Z</BeginTime>
        <TaskErrorCode>400</TaskErrorCode>
        <DBName>DBName</DBName>
        <ProgressInfo>ProgressInfo</ProgressInfo>
        <ScaleOutToken>FEA5DC20-6D8A-5979-97AA-FC57546ADC20</ScaleOutToken>
        <TaskId>20089398</TaskId>
        <TaskErrorMessage>xxxxxxxx</TaskErrorMessage>
        <TaskAction>multi_scale_out</TaskAction>
    </Items>
</DescribeTasksResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "RequestId" : "D6045D78-C119-5A17-9DEA-0F810394E008",
  "PageNumber" : 1,
  "PageRecordCount" : 30,
  "TotalRecordCount" : 2,
  "Items" : [ {
    "Status" : "RUNNING",
    "FinishTime" : "2021-10-20T20:00:00Z",
    "Progress" : "80",
    "BeginTime" : "2021-10-20T19:40:00Z",
    "TaskErrorCode" : "400",
    "DBName" : "DBName",
    "ProgressInfo" : "ProgressInfo",
    "ScaleOutToken" : "FEA5DC20-6D8A-5979-97AA-FC57546ADC20",
    "TaskId" : "20089398",
    "TaskErrorMessage" : "xxxxxxxx",
    "TaskAction" : "multi_scale_out"
  } ]
```

`}`

#### ModifyDBInstanceClass

Changes the instance type of a PolarDB-X instance.

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstanc eClass | The operation that you want to perform. Set the value to ModifyDBInstanceClass. |
| RegionId | String | Yes | cn-hangzhou | The ID of region in which the instance you want to change is located. |
| DBInstanceNam e | String | Yes | pxc-hzjasd**** | The ID of the instance whose type you want to change. |

| TargetDBInstanc eClass | String | Yes | polarx.x4.xlarge. 2e | The new instance type of the instance. Valid values: polarx.x4.medium.2e: Instances of this type have 2 CPU cores and 8 GB of memory. polarx.x4.large.2e: Instances of this type have 4 CPU cores and 16 GB of memory. polarx.x8.large.2e: Instances of this type have 4 CPU cores and 32 GB of memory. polarx.x4.xlarge.2e: Instances of this type have 8 CPU cores and 32 GB of memory. polarx.x8.xlarge.2e: Instances of this type have 8 CPU cores and 64 GB of memory. polarx.x4.2xlarge.2e: Instances of this type have 16 CPU cores and 64 GB of memory. polarx.x8.2xlarge.2e: Instances of this type have 16 CPU cores and 128 GB of memory. polarx.x4.4xlarge.2e: Instances of this type have 32 CPU cores and 128 GB of memory. polarx.x8.4xlarge.2e: Instances of this type have 32 CPU cores and 256 GB of memory. polarx.st.8xlarge.2e: Instances of this type have 60 CPU cores and 470 GB of memory. polarx.st.12xlarge.2e: Instances of this type have 90 CPU cores and 720 GB of memory. |
|---|---|---|---|---|
| ClientToken | String | No | FEA5DC20- 6D8A-5979- 97AA- FC57546ADC20 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| OrderId | String | 20211103105558 | The ID of the order. An order is created each time you upgrade or downgrade the specifications of your instance or change the instance type of your instance. |
| RequestId | String | FEA5DC20-6D8A- 5979-97AA- FC57546ADC20 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyDBInstanceClass &RegionId=cn-hangzhou &DBInstanceName=pxc-hzjasd**** &TargetDBInstanceClass=polarx.x4.xlarge.2e &ClientToken=FEA5DC20-6D8A-5979-97AA-FC57546ADC20 &Common request parameters
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <ModifyDBInstanceClassResponse>
    <OrderId>20211103105558</OrderId>
    <RequestId>FEA5DC20-6D8A-5979-97AA-FC57546ADC20</RequestId>
</ModifyDBInstanceClassResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "OrderId" : "20211103105558",
  "RequestId" : "FEA5DC20-6D8A-5979-97AA-FC57546ADC20"
```

`}`

#### ModifyDBInstanceConfig

Modifies the configuration items of a PolarDB-X instance.

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstanc eConfig | The operation that you want to perform. Set the value to ModifyDBInstanceConfig. |

| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. |
|---|---|---|---|---|
| DBInstanceNam e | String | Yes | pxc-hzjasd**** | The ID of the instance. |
| ConfigName | String | Yes | ENABLE CONSIS _ TENT REPLICA R _ _ EAD | The configuration item. If you set this parameter to ENABLE CONSISTENT REPLICA READ _ _ _ , this operation enables or disables consistent reads among read-only instances in hybrid transaction/analytical processing (HTAP) scenarios for the specified PolarDB-X instance. |
| ConfigValue | String | Yes | true | If ConfigName is set to ENABLE CONSISTENT REPLICA READ _ _ _ , the valid values of the ConfigValue parameter are true and false. |
| ResourceGroupI d | String | No | rg- acfmx2qz2eh2** * | The ID of the resource group. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | FEA5DC20-6D8A- 5979-97AA- FC57546ADC20 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyDBInstanceConfig &RegionId=cn-hangzhou &DBInstanceName=pxc-hzjasd**** &ConfigName=ENABLE_CONSISTENT_REPLICA_READ &ConfigValue=true &ResourceGroupId=rg-acfmx2qz2eh2*** &<Common request parameters>
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <ModifyDBInstanceConfigResponse>
    <RequestId>FEA5DC20-6D8A-5979-97AA-FC57546ADC20</RequestId>
</ModifyDBInstanceConfigResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "RequestId" : "FEA5DC20-6D8A-5979-97AA-FC57546ADC20"
```

`}`

#### 4.5.9. \ ModifyDBInstanceDescription

Modifies the description of a PolarDB for Xscale (PolarDB-X) instance.

**Debugging**

OpenAPI Explorer automatically calculates signature values and generates sample code for different SDKs. Try it in OpenAPI Explorer.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstanc eDescription | The operation to perform. Set the value to ModifyDBInstan ceDescription. |
| RegionId | String | Yes | cn-hangzhou | The region where the instance resides. |
| DBInstanceName | String | Yes | pxc-hzjasd**** | The instance ID. |
| DBInstanceDescri ption | String | Yes | test | The new description of the instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | FEA5DC20-6D8A- 5979-97AA- FC57546ADC20 | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyDBInstanceDescription &RegionId=cn-hangzhou &DBInstanceName=pxc-hzjasd**** &DBInstanceDescription=test &<Common request parameters>
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <ModifyDBInstanceDescriptionResponse>
    <RequestId>FEA5DC20-6D8A-5979-97AA-FC57546ADC20</RequestId>
</ModifyDBInstanceDescriptionResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "RequestId" : "FEA5DC20-6D8A-5979-97AA-FC57546ADC20"
```

`}`

#### ReleaseInstancePublicConnection

Call the ReleaseInstancePublicConnection operation to release the public endpoint of a PolarDB-X instance.

**Debugging**

You can use OpenAPI Explorer to call this operation without calculating a signature. After you run the operation successfully, OpenAPI Explorer automatically generates SDK code samples.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ReleaseInstance PublicConnectio n | The operation that you want to perform. Set the value to ReleaseInstancePublicConnection . |
| DBInstanceNam e | String | Yes | pxc-hzjasd**** | The instance name. |
| CurrentConnecti onString | String | Yes | pxc- hzja******.polar x.rds.aliyuncs.co m | The connection string of the public endpoint. |
| RegionId | String | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | FEA5DC20-6D8A- 5979-97AA- FC57546ADC20 | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ReleaseInstancePublicConnection &ResourceOwnerId=100899 &DBInstanceName=pxc-hzjasd**** &CurrentConnectionString=pxc-hzja******.polarx.rds.aliyuncs.com &RegionId=cn-hangzhou &Common request parameters
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <ReleaseInstancePublicConnectionResponse>
    <RequestId>FEA5DC20-6D8A-5979-97AA-FC57546ADC20</RequestId>
</ReleaseInstancePublicConnectionResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "RequestId" : "FEA5DC20-6D8A-5979-97AA-FC57546ADC20"
```

`}`

#### RestartDBInstance

Restarts a PolarDB-X instance.

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | RestartDBInstanc e | The operation that you want to perform. Set the value to RestartDBInsta nce. |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. |
| DBInstanceName | String | Yes | pxc-hzjasd**** | The name of the DB instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | FEA5DC20-6D8A- 5979-97AA- FC57546ADC20 | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=RestartDBInstance &RegionId=cn-hangzhou &DBInstanceName=pxc-hzjasd**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <RestartDBInstanceResponse>
    <RequestId>FEA5DC20-6D8A-5979-97AA-FC57546ADC20</RequestId>
</RestartDBInstanceResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "RequestId" : "FEA5DC20-6D8A-5979-97AA-FC57546ADC20"
```

`}`

#### UpgradeDBInstanceKernelVersion

Updates the kernel version of a PolarDB-X instance.

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpgradeDBInsta nceKernelVersio n | The operation that you want to perform. Set the value to UpgradeDBInstanceKernelVersio n. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. |
| DBInstanceNam e | String | Yes | pxc-hzjasd**** | The name of the instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceNa me | String | pxc-hzjasd**** | The name of the instance. |
| TargetMinorVe rsion | String | polarx- kernel 5.4.7- _ 16001481 xcluster _ -20200910 | The kernel version after the update. |
| RequestId | String | FEA5DC20-6D8A- 5979-97AA- FC57546ADC20 | The ID of the request. |
| TaskId | String | 422922413 | The ID of the backend task. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpgradeDBInstanceKernelVersion &RegionId=cn-hangzhou &DBInstanceName=pxc-hzjasd**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <UpgradeDBInstanceKernelVersionResponse>
    <DBInstanceName>pxc-hzjasd****</DBInstanceName>
    <TargetMinorVersion>polarx-kernel_5.4.7-16001481_xcluster-
20200910</TargetMinorVersion>
    <RequestId>FEA5DC20-6D8A-5979-97AA-FC57546ADC20</RequestId>
    <TaskId>422922413</TaskId>
</UpgradeDBInstanceKernelVersionResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "DBInstanceName" : "pxc-hzjasd****",
  "TargetMinorVersion" : "polarx-kernel_5.4.7-16001481_xcluster-20200910",
  "RequestId" : "FEA5DC20-6D8A-5979-97AA-FC57546ADC20",
  "TaskId" : "422922413"
```

`}`

#### UpdatePolarDBXInstanceNode

Call the UpdatePolarDBXInstanceNode operation to change the number of nodes in an instance. This operation supports scale out and scale in. The request generates a transaction order.

**Debugging**

You can use OpenAPI Explorer to run this operation directly without calculating signatures. After successful execution, OpenAPI Explorer automatically generates SDK code samples.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdatePolarDBX InstanceNode | The operation that you want to perform. Set the value to UpdatePolarDBXInstanceNode. |
| RegionId | String | Yes | cn-hanzhou | The region ID. |
| DBInstanceNam e | String | Yes | pxc-hzja****** | The instance name ID. |

| DbInstanceNode Count | String | Yes | 3 | The target number of nodes for the instance. Valid values: 0 to 99. |
|---|---|---|---|---|
| ClientToken | String | Yes | FEA5DC20- 6D8A-5979- 97AA- FC57546ADC20 | The client token, which is a random string. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| OrderId | String | 20211103105558 | The order ID generated when changing the number of nodes in the instance. |
| RequestId | String | FEA5DC20-6D8A- 5979-97AA- FC57546ADC20 | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdatePolarDBXInstanceNode &RegionId=cn-hanzhou &DBInstanceName=pxc-hzja****** &DbInstanceNodeCount=3 &ClientToken=FEA5DC20-6D8A-5979-97AA-FC57546ADC20 &Common request parameters
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <UpdatePolarDBXInstanceNodeResponse>
    <OrderId>20211103105558</OrderId>
    <RequestId>FEA5DC20-6D8A-5979-97AA-FC57546ADC20</RequestId>
</UpdatePolarDBXInstanceNodeResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "OrderId" : "20211103105558",
  "RequestId" : "FEA5DC20-6D8A-5979-97AA-FC57546ADC20"
```

`}`

#### DescribeBinaryLogList

Queries the binary log files of a PolarDB-X instance. By default, binary log files are saved for 15 days. Each binary log file that is returned by this operation contains the log entries that are generated over the time range that is specified by the StartTime and EndTime parameters. If the value of the DownloadLink response parameter is a URL instead of NULL, you can download the binary log file from this URL. This URL is valid within two days after it is generated. Download the binary log file before the URL expires.

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBinaryL ogList | The operation that you want to perform. Set the value to DescribeBinaryLogList. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Default value: 30. |
| DBInstanceNam e | String | Yes | pxc- hzfd13214****** | The name of the instance. |
| StartTime | String | Yes | 2021-09-09 10:27:46 | The beginning of the time range to query. |
| EndTime | String | Yes | 2021-11-09 10:27:46 | The end of the time range to query. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 2DFF784E-DC31- 5BBC-9B25- 9261CD9E0AA9 | The ID of the request. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 30 | The number of entries returned on the current page. |
| TotalNumber | Integer | 100 | The total number of the returned binary log files. |
| LogList | Array of LogList |   | The details about the returned binary log files. |
| EndTime | String | 2021-11-09 10:27:46 | The end of the time range in which log entries were generated in the binary log file. |
| ModifiedTime | String | 2021-11-09 10:27:46 | The last time when the binary log file was updated. |
| UploadHost | String | 10.110.88.9 | The IP address of the host to which the binary log file is backed up. |
| UploadStatus | Integer | 2 | The backup state of the binary log file. Valid values: 0: The binary log file is not backed up. 1: The binary log file is being backed up. 2: The binary log file is backed up. |
| DownloadLink | String | http://polarx-cdc- binlog-cn- hangzhou.oss-cn- hangzhou.aliyuncs. com/polardbx cdc/ _ pxc- hzfd1321******/bin log.000001? Expires=16364695 02&OSSAccessKeyI d=LT13fds12dsaf** **&Signature=fdp m%bdsfadsa%2F% bdsafd****** | The download URL of the binary log file. This URL is valid within two days after it is generated. |

| BeginTime | String | 2021-09-09 10:27:46 | The beginning of the time range in which log entries were generated in the binary log file. |
|---|---|---|---|
| LogSize | Long | 536870912 | The size of the binary log file. Unit: bytes. |
| FileName | String | binlog.000001 | The name of the binary log file. |
| CreatedTime | String | 2021-09-09 10:27:46 | The time when the binary log file was created. |
| PurgeStatus | Integer | 0 | Indicates whether the binary log file is deleted. Valid values: 0: The binary log file is not deleted. 1: The binary log file is deleted. |
| Id | Long | 100 | The unique ID of the returned entry. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeBinaryLogList &RegionId=cn-hangzhou &PageNumber=1 &PageSize=30 &DBInstanceName=pxc-hzfd13214****** &StartTime=2021-09-09 10:27:46 &EndTime=2021-11-09 10:27:46 &<Common request parameters>
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <DescribeBinaryLogListResponse>
    <RequestId>2DFF784E-DC31-5BBC-9B25-9261CD9E0AA9</RequestId>
    <PageNumber>1</PageNumber>
    <PageSize>30</PageSize>
    <TotalNumber>100</TotalNumber>
    <LogList>
        <EndTime>2021-11-09 10:27:46</EndTime>
        <ModifiedTime>2021-11-09 10:27:46</ModifiedTime>
        <UploadHost>10.110.88.9</UploadHost>
        <UploadStatus>2</UploadStatus>
        <DownloadLink>http://polarx-cdc-binlog-cn-hangzhou.oss-cn-
hangzhou.aliyuncs.com/polardbx_cdc/pxc-hzfd13214******/binlog.000001? Expires=1636469502&amp;OSSAccessKeyId=LT13fds12dsaf****&amp;Signature=fdpm%bdsfadsa%2F%bd
*****</DownloadLink>
        <BeginTime>2021-09-09 10:27:46</BeginTime>
        <LogSize>536870912</LogSize>
        <FileName>binlog.000001</FileName>
        <CreatedTime>2021-09-09 10:27:46</CreatedTime>
        <PurgeStatus>0</PurgeStatus>
        <Id>100</Id>
    </LogList>
</DescribeBinaryLogListResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "RequestId" : "2DFF784E-DC31-5BBC-9B25-9261CD9E0AA9",
  "PageNumber" : 1,
  "PageSize" : 30,
  "TotalNumber" : 100,
  "LogList" : [ {
    "EndTime" : "2021-11-09 10:27:46",
    "ModifiedTime" : "2021-11-09 10:27:46",
    "UploadHost" : "10.110.88.9",
    "UploadStatus" : 2,
    "DownloadLink" : "http://polarx-cdc-binlog-cn-hangzhou.oss-cn-
hangzhou.aliyuncs.com/polardbx_cdc/pxc-hzfd13214******/binlog.000001? Expires=1636469502&OSSAccessKeyId=LT13fds12dsaf****&Signature=fdpm%bdsfadsa%2F%bdsaf*****
```

`,`

```json
    "BeginTime" : "2021-09-09 10:27:46",
    "LogSize" : 536870912,
    "FileName" : "binlog.000001",
    "CreatedTime" : "2021-09-09 10:27:46",
    "PurgeStatus" : 0,
    "Id" : 100
  } ]
```

`}`

**Error codes**

| HttpCod e | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidPageSize.Ma lformed | The specified parameter PageSize is not valid. | The error message returned because the specified PageSize parameter is invalid. |

For a list of error codes, visit the API Error Center.

#### ModifyDBInstanceVip

Modify the virtual IP address (VIP) of a PolarDB-X instance.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| RegionId | Strin g | Quer y | Yes | cn-hangzhou | The ID of the region where the instance resides. |
|---|---|---|---|---|---|
| DBInstanc eName | Strin g | Quer y | Yes | pxc-xxxxx | The name of the PolarDB- X instance whose VIP you want to modify. |
| SwitchTim e | Strin g | Quer y | No | 2026-04-10T00:00:00Z | The scheduled switchover time, in ISO 8601 format. |
| SwitchMod e | Strin g | Quer y | No | Immediate | The switchover mode. Valid values: Immediate: Perform the switchover immediately. MaintainTime: Perform the switchover during the maintenance window. |
| VpcId | Strin g | Quer y | No | vpc-xxxxx | The ID of the VPC where the instance resides. |
| VSwitchId | Strin g | Quer y | No | vsw-xxxxx | The ID of the destination vSwitch. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | Success | The message returned by the operation. |
| RequestId | String | 0A5C7D6B-XXXX- XXXX-XXXX- XXXXXXXXXXXX | The unique identifier of the request. |
| Success | Boolean | true | Indicates whether the operation succeeded. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyDBInstanceVip &RegionId=cn-hangzhou &DBInstanceName=pxc-xxxxx &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "Message":"Success",
 "RequestId":"0A5C7D6B-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
 "Success":true
```

`}` `XML` format

```xml
<Message>Success</Message> <RequestId>0A5C7D6B-XXXX-XXXX-XXXX-XXXXXXXXXXXX</RequestId> <Success>true</Success>
```

#### CreateTransformOperation

Call the CreateTransformOperation operation to handle transformation tasks for a PolarDB-X instance.

**Request headers**

This operation uses common request headers. No special request headers apply. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Quer y | Yes | cn-hangzhou | The ID of the region where the resource resides. |
| DBInstanc eName | Strin g | Quer y | Yes | px-instance-001 | The name of the database instance. |
| Operation | Strin g | Quer y | Yes | precheck | The type of operation, such as starting or stopping a transformation task. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | ABCDE-12345- FGHIJ | The unique identifier of the request. |
| Success | Boolean | true | Indicates whether the operation was successful. |
| Message | String | Operation successful. | The message returned. |
| Data | Struct | - | The data object returned. |
| -TaskId | String | task-12345 | The unique identifier of the task. |
| -ResultCode | String | 200 | The result code that indicates the status of the operation. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateTransformOperation &RegionId=cn-hangzhou &DBInstanceName=px-instance-001 &Operation=StartTransform &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"ABCDE-12345-FGHIJ",
 "Message":"Operation successful.",
 "Data":{
  "TaskId":"task-12345",
  "ResultCode":"200"
```

`},`

```json
 "Success":true
```

`}` `XML` format

```xml
<RequestId>ABCDE-12345-FGHIJ</RequestId> <Message>Operation successful.</Message> <Data>
  <TaskId>task-12345</TaskId>
  <ResultCode>200</ResultCode>
</Data> <Success>true</Success>
```

#### DescribeTransformStatus

Query the transformation status. This API retrieves the transformation status of a PolarDB-X instance. Ensure that you provide all required request parameters when you call this API.

**Request headers**

This API uses common request headers only. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Quer y | Yes | cn-hangzhou | The ID of the region. This parameter is required. |
| DBInstanc eName | Strin g | Quer y | Yes | my-db-instance | The name of the database instance. This parameter is required. |
| QueryRepo rt | Strin g | Quer y | No | true | Specifies whether to return report information. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE**** | The unique identifier of the request. |
| Success | Boolean | true | Indicates whether the operation was successful. |
| Message | String | success | The message that describes the result of the operation. |

| Data | Struct | - | The data object that contains detailed status information. |
|---|---|---|---|
| -Operations | List | - | The list of operations currently in progress. |
| - EnterpriseInsN ame | String | ent-ins-xxx | The name of the enterprise edition instance. |
| - StandardInsNa me | String | std-ins-xxx | The name of the standard edition instance. |
| -Phase | String | SWITCHING | The current phase of the transformation. |
| -Processing | Boolean | false | Indicates whether the system is processing the request. |
| -CanSwitch | Boolean | true | Indicates whether you can perform a switchover. If the value is true, you can perform the switchover operation. |
| - CanUndoSwitc h | Boolean | false | Indicates whether you can undo the switchover. If the value is true, you can perform the failback operation. |
| -CanCancel | Boolean | false | Indicates whether the operation can be canceled. |
| -CanFinish | Boolean | true | Indicates whether the operation can be completed. |
| -CanUpgrade | Boolean | false | Indicates whether the upgrade can be performed. |
| -ReportTime | Long | 1678888888000 | The timestamp when the report was generated. |

| - ReportSumma ry | Map | - | The summary information of the report. The key-value pairs correspond to inspection items as follows: If the value is an empty array [], the item passed the inspection. If the value is not empty and contains specific error information, the item failed the inspection. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeTransformStatus &RegionId= &DBInstanceName= &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"473469C7-AA6F-4DC5-B3DB-A3DC0DE****",
 "Message":"success\t",
 "Data":{
  "ReportTime":1678888888000,
  "Phase":"SWITCHING",
  "CanFinish":true,
  "CanUpgrade":false,
  "StandardInsName":"std-ins-xxx",
  "ReportSummary":"",
  "CanUndoSwitch":false,
  "Operations":"",
  "EnterpriseInsName":"ent-ins-xxx",
  "CanSwitch":true,
  "CanCancel":false,
  "Processing":false
```

`},`

```json
 "Success":true
```

`}` `XML` format

```xml
<RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE****</RequestId> <Message>success </Message> <Data>
  <ReportTime>1678888888000</ReportTime>
  <Phase>SWITCHING</Phase>
  <CanFinish>true</CanFinish>
  <CanUpgrade>false</CanUpgrade>
  <StandardInsName>std-ins-xxx</StandardInsName>
  <ReportSummary  />
  <CanUndoSwitch>false</CanUndoSwitch>
  <Operations  />
  <EnterpriseInsName>ent-ins-xxx</EnterpriseInsName>
  <CanSwitch>true</CanSwitch>
  <CanCancel>false</CanCancel>
  <Processing>false</Processing>
</Data> <Success>true</Success>
```

#### ModifyDBInstanceSeries

Call the ModifyDBInstanceSeries operation to upgrade a PolarDB-X Standard Edition instance to an Enterprise Edition instance.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Quer y | Yes | cn-hangzhou | The ID of the region where the instance resides. |
| DBInstanc eName | Strin g | Quer y | Yes | pxc-xxxxxxxx | The name of the PolarDB- X instance that you want to upgrade. |
| DNNodeCl ass | Strin g | Quer y | No | pxc.d2.large | The specification of DN nodes. |
| Storage | Strin g | Quer y | No | 100 | The storage capacity. Unit: GB. |
| ClientToke n | Strin g | Quer y | No | 123e4567-e89b-12d3- a456-426614174000 | The token that ensures the idempotence of the request. |

| CNNodeCo unt | Integ er | Quer y | No | 2 | The number of CN nodes. |
|---|---|---|---|---|---|
| DNNodeCo unt | Integ er | Quer y | No | 1 | The number of DN nodes. Set the value to 1. |
| Series | Strin g | Quer y | No | Enterprise | The series of the instance. Set the value to Enterprise. |
| CNNodeCl ass | Strin g | Quer y | No | pxc.c2.medium | The specification of CN nodes. For more information, see Specifications in the product documentation. |

You must provide all parameters marked as required. Otherwise, the request may fail.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0000-ABCD-EFGH- IJKL | The unique identifier of the request. You can use this ID to troubleshoot and locate issues. |
| OrderId | String | 202002021234567 89 | The ID of the order. The system returns this parameter only when a billing change occurs. You can use this ID to query related operation records. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyDBInstanceSeries &RegionId=cn-hangzhou &DBInstanceName=pxc-xxxxxxxx &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"0000-ABCD-EFGH-IJKL",
 "OrderId":"20200202123456789"
```

`}` `XML` format

```xml
<RequestId>0000-ABCD-1234-EFGH</RequestId> <OrderId>2020101010101010</OrderId>
```

#### DescribeDBInstanceTopology

Call the DescribeDBInstanceTopology operation to retrieve the topology of a PolarDB-X instance.

**Request headers**

This operation uses common request headers and does not have specific request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Quer y | Yes | pxc-unro6hys9vpdtf | The ID of the region to which the instance belongs. |
| DBInstanc eName | Strin g | Quer y | Yes | cn-wulan-env212-d01 | The instance ID. |
| StartTime | Strin g | Quer y | No | 2021-10-21T10:30:45Z 04:00:00 | The beginning of the time range to query the historical topology of the instance. Specify the time in the yyyy-MM-dd HH:mm:ss format. |
| EndTime | Strin g | Quer y | No | 2021-10-22T10:30:45Z 04:00:00 | The end of the time range to query the historical topology of the instance. Specify the time in the yyyy-MM-dd HH:mm:ss format. |
| MinuteSim ple | Bool ean | Quer y | No | true | Specifies whether to query the historical topology. |

**Response data**

| RequestId | String | A1449163-F718- 4EF0-B993- FA447DB18FD0 | The request ID. |
|---|---|---|---|
| Data | Struct | - | The data structure. |

| - LogicInstanceT opology | Struct | - | The instance topology. |
|---|---|---|---|
| --Items | Array | - | The structure. |
| --- ConnectionIp | Array | - | The connection IP addresses. |
| ---- ConnectionStri ng | String | 10.212.2.49 | The endpoint. |
| ----Port | String | 3000 | The port number. |
| ---- DBInstanceNet Type | Integer | 1 | The network type of the instance. |
| --- AzoneRoleList | Array | - | The list of zone roles. |
| ----Azone | String | cn-wulan-env212- amtest212001-a | The zone. |
| ----Role | String | master | The role. |
| --- EngineVersion | String | 2.0 | The engine version. |
| --- MaintainEndTi me | String | 06:00:00 | The maintenance end time. |
| ---LockMode | Integer | 0 | The lock mode. |
| --- DBInstanceNa me | String | pxc-i-rx2vwf68cu | The database instance name. |
| --- PhyInstanceNa me | String | pxc- unro6hys9vpdtfkto p-cn | The physical instance name. |

| --- DBInstanceSta tusDescription | String | ACTIVATION | The description of the database instance status. |
|---|---|---|---|
| --- DBInstanceId | String | 617 | The database instance ID. |
| ---LockReason | String | null | The reason for locking. |
| --- DBInstanceSta tus | Integer | 1 | The database instance status. |
| --- DBInstanceCre ateTime | String | 2023-12- 06T07:47:10Z | The creation time of the database instance. |
| --- MaintainStartT ime | String | 02:00:00 | The maintenance start time. |
| --- CharacterType | String | polarx cn _ | The node type. |
| ---Engine | String | polarx cn _ | The engine. |
| --- DBInstanceCo nnType | Integer | 1 | The network type of the node. |
| --- DBInstanceDe scription | String | pxc- sprcym7g7wj7k | The instance description. |
| ---MaxIops | Integer | 4000 | The maximum IOPS. |
| ---DiskSize | Long | 51200 | The disk size. |
| --- MaxConnectio ns | Integer | 2000 | The maximum number of connections. |
| ---Region | String | cn-wulan-env212- d01;cn-wulan- env212-d01;cn- wulan-env212-d01 | The region. |

| ---Azone | String | cn-wulan-env212- amtest212001-a | The zone. |
|---|---|---|---|
| ---Role | String | polarx storage _ | The role. |
| ---Activated | Boolean | true | Indicates whether it is activated. |
| ---Status | String | In use | The status. |
| ---NodeClass | String | polarx.n4.medium. 2e.cdc | The node specification. |
| --HistoryItems | Array | - | The structure. |
| --- ConnectionIp | Array | - | The connection IP addresses. |
| ---- ConnectionStri ng | String | 10.212.2.49 | The endpoint. |
| ----Port | String | 3000 | The port number. |
| ---- DBInstanceNet Type | Integer | 1 | The network type of the instance. |
| --- AzoneRoleList | Array | - | The list of zone roles. |
| ----Azone | String | cn-wulan-env212- amtest212001-a | The zone. |
| ----Role | String | master | The role. |
| --- EngineVersion | String | 2.0 | The engine version. |
| --- MaintainEndTi me | String | 06:00:00 | The maintenance end time. |
| ---LockMode | Integer | 0 | The lock mode. |

| --- DBInstanceNa me | String | pxc-i-rx2vwf68cu | The database instance name. |
|---|---|---|---|
| --- PhyInstanceNa me | String | pxc- unro6hys9vpdtfkto p-cn | The physical instance name. |
| --- DBInstanceSta tusDescription | String | ACTIVATION | The description of the database instance status. |
| --- DBInstanceId | String | 617 | The database instance ID. |
| ---LockReason | String | null | The reason for locking. |
| --- DBInstanceSta tus | Integer | 1 | The database instance status. |
| --- DBInstanceCre ateTime | String | 2023-12- 06T07:47:10Z | The creation time of the database instance. |
| --- MaintainStartT ime | String | 02:00:00 | The maintenance start time. |
| --- CharacterType | String | polarx cn _ | The node type. |
| ---Engine | String | polarx cn _ | The engine. |
| --- DBInstanceCo nnType | Integer | 1 | The network type of the node. |
| --- DBInstanceDe scription | String | pxc- sprcym7g7wj7k | The instance description. |
| ---MaxIops | Integer | 4000 | The maximum IOPS. |
| ---DiskSize | Long | 51200 | The disk size. |

| --- MaxConnectio ns | Integer | 2000 | The maximum number of connections. |
|---|---|---|---|
| ---Region | String | cn-wulan-env212- d01;cn-wulan- env212-d01;cn- wulan-env212-d01 | The region. |
| ---Azone | String | cn-wulan-env212- amtest212001-a | The zone. |
| ---Role | String | polarx storage _ | The role. |
| ---Activated | Boolean | true | Indicates whether it is activated. |
| ---Status | String | In use | The status. |
| ---NodeClass | String | polarx.n4.medium. 2e.cdc | The node specification. |
| -- DBInstanceCo nnType | String | 1 | The network type of the node. |
| -- DBInstanceDe scription | String | pxc- sprcym7g7wj7k | The database instance description. |
| -- DBInstanceSto rage | Integer | 1 | The database instance storage. |
| -- EngineVersion | String | 5.7 | The engine version. |
| -- DBInstanceSta tus | Integer | 1 | The database instance status. |
| --LockMode | Integer | 0 | The lock mode. |
| -- DBInstanceCo nnType | String | 1 | The network type of the node. |

| -- MaintainStartT ime | String | 02:00:00 | The maintenance start time. |
|---|---|---|---|
| -- MaintainEndTi me | String | 06:00:00 | The maintenance end time. |
| --DBInstanceId | String | 624 | The database instance ID. |
| -- DBInstanceCre ateTime | String | 2023-12- 06T07:47:10Z | The creation time of the database instance. |
| -- DBInstanceSta tusDescription | String | ACTIVATION | The description of the database instance status. |
| --LockReason | String | null | The reason for locking. |
| --Engine | String | mysql | The engine. |
| -- DBInstanceNa me | String | pxc-i-rx2vwf68cu | The instance name. |

**Examples**

Sample request

```
http(s)://[Endpoint]/?Action=DescribeDBInstanceTopology &RegionId=pxc-unro6hys9vpdtf &DBInstanceName=cn-wulan-env212-d01 &Common request parameters
```

Sample success response `JSON` format `{`

```json
 "RequestId":"A1449163-F718-4EF0-B993-FA447DB18FD0",
 "Data":{
  "LogicInstanceTopology":{
   "EngineVersion":"5.7",
   "DBInstanceStatus":1,
   "HistoryItems":[
```

`{`

```json
     "CharacterType":"polarx_cn",
     "DBInstanceConnType":1,
```

```json
     "MaxIops":4000,
     "Activated":true,
     "NodeClass":"polarx.n4.medium.2e.cdc",
     "ConnectionIp":[
```

`{`

```json
       "DBInstanceNetType":1,
       "Port":"3000",
       "ConnectionString":"10.212.2.49"
```

`}` `],`

```json
     "MaintainEndTime":"06:00:00",
     "DBInstanceId":"617",
     "DBInstanceStatusDescription":"ACTIVATION",
     "DiskSize":51200,
     "DBInstanceCreateTime":"2023-12-06T07:47:10Z",
     "LockReason":"null",
     "AzoneRoleList":[
```

`{`

```json
       "Azone":"cn-wulan-env212-amtest212001-a",
       "Role":"primary"
```

`}` `],`

```json
     "MaintainStartTime":"02:00:00",
     "Engine":"polarx_cn",
     "DBInstanceDescription":"pxc-sprcym7g7wj7k",
     "DBInstanceName":"pxc-i-rx2vwf68cu",
     "Azone":"cn-wulan-env212-amtest212001-a",
     "Status":"In use",
     "EngineVersion":"2.0",
     "DBInstanceStatus":1,
     "MaxConnections":2000,
     "PhyInstanceName":"pxc-unro6hys9vpdtfktop-cn",
     "LockMode":0,
     "Role":"polarx_storage",
     "Region":"cn-wulan-env212-d01;cn-wulan-env212-d01;cn-wulan-env212-d01"
```

`}` `],`

```json
   "LockMode":0,
   "DBInstanceConnType":"1",
   "Series":"",
   "MaintainEndTime":"06:00:00",
   "DBInstanceId":"624",
   "DBInstanceStorage":1,
   "DBInstanceStatusDescription":"ACTIVATION",
   "DBInstanceCreateTime":"2023-12-06T07:47:10Z",
   "LockReason":"",
   "Items":[
```

`{`

```json
     "CharacterType":"polarx_cn",
     "DBInstanceConnType":1,
     "MaxIops":4000,
     "Activated":true,
     "NodeClass":"polarx.n4.medium.2e.cdc",
     "ConnectionIp":[
```

`{` `{`

```json
       "DBInstanceNetType":1,
       "Port":"3000",
       "ConnectionString":"10.212.2.49"
```

`}` `],`

```json
     "MaintainEndTime":"06:00:00",
     "DBInstanceId":"617",
     "Version":"",
     "DBInstanceStatusDescription":"ACTIVATION",
     "DiskSize":51200,
     "DBInstanceCreateTime":"2023-12-06T07:47:10Z",
     "LockReason":"null",
     "AzoneRoleList":[
```

`{`

```json
       "Azone":"cn-wulan-env212-amtest212001-a",
       "Role":"primary",
       "ReplicaId":""
```

`}` `],`

```json
     "MaintainStartTime":"02:00:00",
     "Engine":"polarx_cn",
     "DBInstanceDescription":"pxc-sprcym7g7wj7k",
     "DBInstanceName":"pxc-i-rx2vwf68cu",
     "Azone":"cn-wulan-env212-amtest212001-a",
     "Status":"In use",
     "EngineVersion":"2.0",
     "DBInstanceStatus":1,
     "MaxConnections":2000,
     "PhyInstanceName":"pxc-unro6hys9vpdtfktop-cn",
     "LockMode":0,
     "Role":"polarx_storage",
     "Region":"cn-wulan-env212-d01;cn-wulan-env212-d01;cn-wulan-env212-d01"
```

`}` `],`

```json
   "DBInstanceDescription":"pxc-sprcym7g7wj7k",
   "MaintainStartTime":"02:00:00",
   "Engine":"mysql",
   "DBInstanceName":"pxc-i-rx2vwf68cu"
```

`}` `}` `}` `XML` format

```xml
<RequestId>A1449163-F718-4EF0-B993-FA447DB18FD0</RequestId> <Data>
 <LogicInstanceTopology>
  <EngineVersion>5.7</EngineVersion>
  <DBInstanceStatus>1</DBInstanceStatus>
  <HistoryItems>
   <CharacterType>polarx_cn</CharacterType>
   <DBInstanceConnType>1</DBInstanceConnType>
   <MaxIops>4000</MaxIops>
```

```xml
   <Activated>true</Activated>
   <NodeClass>polarx.n4.medium.2e.cdc</NodeClass>
   <ConnectionIp>
    <DBInstanceNetType>1</DBInstanceNetType>
    <Port>3000</Port>
    <ConnectionString>10.212.2.49</ConnectionString>
   </ConnectionIp>
   <MaintainEndTime>06:00:00</MaintainEndTime>
   <DBInstanceId>617</DBInstanceId>
   <DBInstanceStatusDescription>ACTIVATION</DBInstanceStatusDescription>
   <DiskSize>51200</DiskSize>
   <DBInstanceCreateTime>2023-12-06T07:47:10Z</DBInstanceCreateTime>
   <LockReason>null</LockReason>
   <AzoneRoleList>
    <Azone>cn-wulan-env212-amtest212001-a</Azone>
    <Role>primary</Role>
   </AzoneRoleList>
   <MaintainStartTime>02:00:00</MaintainStartTime>
   <Engine>polarx_cn</Engine>
   <DBInstanceDescription>pxc-sprcym7g7wj7k</DBInstanceDescription>
   <DBInstanceName>pxc-i-rx2vwf68cu</DBInstanceName>
   <Azone>cn-wulan-env212-amtest212001-a</Azone>
   <Status>In use</Status>
   <EngineVersion>2.0</EngineVersion>
   <DBInstanceStatus>1</DBInstanceStatus>
   <MaxConnections>2000</MaxConnections>
   <PhyInstanceName>pxc-unro6hys9vpdtfktop-cn</PhyInstanceName>
   <LockMode>0</LockMode>
   <Role>polarx_storage</Role>
   <Region>cn-wulan-env212-d01;cn-wulan-env212-d01;cn-wulan-env212-d01</Region>
  </HistoryItems>
  <LockMode>0</LockMode>
  <DBInstanceConnType>1</DBInstanceConnType>
  <Series  />
  <MaintainEndTime>06:00:00</MaintainEndTime>
  <DBInstanceId>624</DBInstanceId>
  <DBInstanceStorage>1</DBInstanceStorage>
  <DBInstanceStatusDescription>ACTIVATION</DBInstanceStatusDescription>
  <DBInstanceCreateTime>2023-12-06T07:47:10Z</DBInstanceCreateTime>
  <LockReason  />
  <Items>
   <CharacterType>polarx_cn</CharacterType>
   <DBInstanceConnType>1</DBInstanceConnType>
   <MaxIops>4000</MaxIops>
   <Activated>true</Activated>
   <NodeClass>polarx.n4.medium.2e.cdc</NodeClass>
   <ConnectionIp>
    <DBInstanceNetType>1</DBInstanceNetType>
    <Port>3000</Port>
    <ConnectionString>10.212.2.49</ConnectionString>
   </ConnectionIp>
   <MaintainEndTime>06:00:00</MaintainEndTime>
   <DBInstanceId>617</DBInstanceId>
   <Version  />
<DBI
```

`t`

```
Stt
```

`D`

```
iti >ACTIVATION</DBI
```

`t`

```
Stt
```

`D`

```
iti
```

`>`

```xml
   <DBInstanceStatusDescription>ACTIVATION</DBInstanceStatusDescription>
   <DiskSize>51200</DiskSize>
   <DBInstanceCreateTime>2023-12-06T07:47:10Z</DBInstanceCreateTime>
   <LockReason>null</LockReason>
   <AzoneRoleList>
    <Azone>cn-wulan-env212-amtest212001-a</Azone>
    <Role>primary</Role>
    <ReplicaId  />
   </AzoneRoleList>
   <MaintainStartTime>02:00:00</MaintainStartTime>
   <Engine>polarx_cn</Engine>
   <DBInstanceDescription>pxc-sprcym7g7wj7k</DBInstanceDescription>
   <DBInstanceName>pxc-i-rx2vwf68cu</DBInstanceName>
   <Azone>cn-wulan-env212-amtest212001-a</Azone>
   <Status>In use</Status>
   <EngineVersion>2.0</EngineVersion>
   <DBInstanceStatus>1</DBInstanceStatus>
   <MaxConnections>2000</MaxConnections>
   <PhyInstanceName>pxc-unro6hys9vpdtfktop-cn</PhyInstanceName>
   <LockMode>0</LockMode>
   <Role>polarx_storage</Role>
   <Region>cn-wulan-env212-d01;cn-wulan-env212-d01;cn-wulan-env212-d01</Region>
  </Items>
  <DBInstanceDescription>pxc-sprcym7g7wj7k</DBInstanceDescription>
  <MaintainStartTime>02:00:00</MaintainStartTime>
  <Engine>mysql</Engine>
  <DBInstanceName>pxc-i-rx2vwf68cu</DBInstanceName>
 </LogicInstanceTopology>
</Data>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 |   | InvalidDBInstance.NotFound | The specified database instance does not exist. |

#### RestoreDBInstance

Call the RestoreDBInstance operation to restore an instance.

**Request headers**

This operation uses common request headers and does not have special request headers. For more information, see Common request parameters.

**Request parameters**

| 7 |   |   |   | > D | ocument Version: 2026083 |
|---|---|---|---|---|---|

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Quer y | No | cn-wulan-env213-d01 | The region ID. |
| Action | Strin g | Syst em | No | RestoreDBInstance | The operation that you want to perform. Set the value to RestoreDBInstance. |
| PayType | Strin g | Quer y | No | POSTPAY | The payment type. |
| DBNodeCo unt | Integ er | Quer y | No | 2 | The number of nodes. The value must be greater than or equal to 2. |
| DBNodeCl ass | Strin g | Quer y | No | polarx.x4.large.2e | The node specification. |
| ZoneId | Strin g | Quer y | No | cn-wulan-env213- amtest213001-a | The zone ID. |
| ClientToke n | Strin g | Quer y | No | c1dd299c-10c6-11ea- bbbb-************ | The client token that guarantees the idempotence of the request and prevents duplicate submissions. Generate this parameter on the client side. Ensure that its value is unique across different requests, contains no more than 64 ASCII characters, and includes no non-ASCII characters. |
| NetworkTy pe | Strin g | Quer y | No | vpc | The network type. |
| VPCId | Strin g | Quer y | No | vpc- 6ke45qy560ugfrf36**** | The Virtual Private Cloud (VPC) ID. |
| VSwitchId | Strin g | Quer y | No | vsw- 6kekhga14ftf3kmq1**** | The vSwitch ID. |

| ResourceG roupId | Strin g | Quer y | No | aa | The resource group ID. |
|---|---|---|---|---|---|
| EngineVer sion | Strin g | Quer y | No | 5.7 | The engine version. |
| OriginalDB InstanceN ame | Strin g | Quer y | Yes | pxc-unrwuyttjx**** | The name of the source instance. |
| RecoveryT ypeCode | Strin g | Quer y | No | AnyTime | The recovery type code. |
| RestoreTi me | Strin g | Quer y | No | 2022-08-24T00:53:20Z | The point in time to which you want to restore data. Specify the time in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. |
| BackupSet Id | Strin g | Quer y | No | 11 | The ID of the backup set. |
| Storage | Strin g | Quer y | No | 5 | The storage capacity. Unit: GB. |
| IPVersion | Strin g | Quer y | No | IPv4 | The IP version. This parameter is optional. Default value: IPv4. Valid values: IPv4 IPv4v6 |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | BFC01449-C5D2- 4457-8909- 8285B9E1710 | The request ID. |
| DBInstanceNa me | String | pxc-unrwuyttjx**** | The instance ID. |

| OrderId | String | 11 | The order ID. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=RestoreDBInstance &OriginalDBInstanceName=pxc-unrwuyttjx**** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"BFC01449-C5D2-4457-8909-8285B9E1710",
 "OrderId":"11",
 "DBInstanceName":"pxc-unrwuyttjx****"
```

`}` `XML` format

```xml
<RequestId>BFC01449-C5D2-4457-8909-8285B9E1710</RequestId> <OrderId>11</OrderId> <DBInstanceName>pxc-unrwuyttjx****</DBInstanceName>
```

### Database management

#### CreateDB

Creates a PolarDB-X database.

**Debugging**

Alibaba Cloud provides OpenAPI Explorer to simplify API usage. OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateDB | The operation that you want to perform. Set the value to CreateDB. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where your PolarDB-X instance is deployed. |

| DBInstanceNam e | String | Yes | pxc- ************** | The name of the PolarDB-X instance. |
|---|---|---|---|---|
| AccountName | String | Yes | testaccount | The username of the account that is used to access the database. |
| Charset | String | Yes | utf8mb4 | The character set that the database supports. For example, you can set the value to utf8mb4. |
| DbName | String | Yes | testdb | The name of the database. |
| AccountPrivilege | String | Yes | ReadWrite | The permissions on the database. Specify the type of permissions that you want to grant to the account that is specified by the AccountName parameter. Valid values: ReadWrite ReadOnly DMLOnly DDLOnly |
| DbDescription | String | No | db for test | The description of the database. |
| SecurityAccount Name | String | No | securityAccount | The username of the data security administrator (DSA) account. Note If the three-role mode is enabled for the PolarDB-X instance to which the database belongs, you must specify this parameter. |
| SecurityAccount Password | String | No | securityPasswor d | The password of the DSA account. Note If the three-role mode is enabled for the PolarDB-X instance to which the database belongs, you must specify this parameter. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | ***** | The message that is returned. If the request is successful, "success" is returned. If the request fails, an error code is returned. |

| RequestId | String | 9B2F3840-5C98- 475C-B269- 2D5C3A31797C | The ID of the request. |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateDB &RegionId=cn-hangzhou &DBInstanceName=pxc-************** &AccountName=testaccount &Charset=utf8mb4 &DbName=testdb &AccountPrivilege=ReadWrite &DbDescription=db for test &SecurityAccountName=securityAccount &SecurityAccountPassword=securityPassword &<Common request parameters>
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <CreateDBResponse>
    <Message>*****</Message>
    <RequestId>9B2F3840-5C98-475C-B269-2D5C3A31797C</RequestId>
    <Success>true</Success>
</CreateDBResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "Message" : "*****",
  "RequestId" : "9B2F3840-5C98-475C-B269-2D5C3A31797C",
  "Success" : true
```

`}`

#### 4.6.2. \ DescribeTableDetail

Queries the schema of a table in a PolarDB-X instance.

**Debugging**

OpenAPI Explorer automatically calculates the request signature. Call this operation in OpenAPI Explorer to simplify API usage and generate SDK sample code.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeTableDe tail | The operation to perform. Set the value to DescribeTableD etail. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the PolarDB-X instance is deployed. |
| DBInstanceName | String | Yes | pxc- sprcym7g7w**** | The name of the PolarDB-X instance. |
| DbName | String | Yes | sbtest | The name of the database to which the table belongs. |
| TableName | String | Yes | k 4 _ | The name of the table. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | success | The response message. Returns success if the request succeeds, or an error code if the request fails. |
| RequestId | String | FE5D94E3-3C93-3594- 95D9-AAED2A980915 | The request ID. |
| Success | Boolean | true | Indicates whether the request succeeded. |
| Data | Object |   | The returned data. |
| Fields | Array of Field |   | The fields in the table. |
| Key | String | k 1 _ | The field name of the column. |
| DataType | String | multi | The data type of the column. |
| Column | String | k | The alias of the column. |

| Extra | String | * | A hidden parameter. |
|---|---|---|---|

**Examples**

Sample request

```
http(s)://[Endpoint]/?Action=DescribeTableDetail &RegionId=cn-hangzhou &DBInstanceName=pxc-sprcym7g7w**** &DbName=sbtest &TableName=k_4 &<Common request parameters>
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <DescribeTableDetailResponse>
    <Message>success</Message>
    <RequestId>FE5D94E3-3C93-3594-95D9-AAED2A980915</RequestId>
    <Success>true</Success>
    <Data>
        <Fields>
            <Key>k_1</Key>
            <DataType>multi</DataType>
            <Column>k</Column>
            <Extra>*</Extra>
        </Fields>
    </Data>
</DescribeTableDetailResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "Message" : "success",
  "RequestId" : "FE5D94E3-3C93-3594-95D9-AAED2A980915",
  "Success" : true,
  "Data" : {
    "Fields" : [ {
      "Key" : "k_1",
      "DataType" : "multi",
      "Column" : "k",
      "Extra" : "*"
    } ]
```

`}` `}`

#### DeleteDB

Deletes a database from a PolarDB-X instance.

**Debugging**

Use OpenAPI Explorer to call this operation. OpenAPI Explorer calculates the signature for you and generates sample code for the supported SDKs.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteDB | The operation to perform. Set the value to DeleteDB. |
| RegionId | String | Yes | cn-hangzhou | The region where the PolarDB-X instance resides. |
| DBInstanceName | String | Yes | pxc-******** | The name of the PolarDB-X instance. |
| DbName | String | Yes | testdb | The name of the database to delete. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | ***** | The returned message. If the request succeeds, success is returned. If the request fails, an error code is returned. |
| RequestId | String | 9B2F3840-5C98-475C- B269-2D5C3A31797C | The request ID. |
| Success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteDB &RegionId=cn-hangzhou &DBInstanceName=pxc-******** &DbName=testdb &<Common request parameters>
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <DeleteDBResponse>
    <Message>*****</Message>
    <RequestId>9B2F3840-5C98-475C-B269-2D5C3A31797C</RequestId>
    <Success>true</Success>
</DeleteDBResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "Message" : "*****",
  "RequestId" : "9B2F3840-5C98-475C-B269-2D5C3A31797C",
  "Success" : true
```

`}`

#### DescribeCharacterSet

Queries the character sets supported by databases in a PolarDB-X instance.

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, call this operation in OpenAPI Explorer, which generates sample code for different SDKs.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCharact erSet | The operation to perform. Set the value to DescribeCharac terSet. |
| DBInstanceName | String | Yes | pxc-********* | The name of the PolarDB-X instance. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the PolarDB-X instance resides. |

**Response elements**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Message | String | success | The result of the request. Returns success if the request is successful, or an error code if the request fails. |
|---|---|---|---|
| RequestId | String | 709C1E40-092D- 4A3D-9958- 6D7438****** | The request ID. |
| Success | Boolean | true | Specifies whether the request is successful. |
| Data | Object |   | The returned data. |
| Engine | String | polarx | The storage class of databases in the PolarDB-X instance. The value is polarx . |
| CharacterSet | Array of String | utf8 | The character sets supported by databases in the PolarDB-X instance. |

**Examples**

Sample request

```
http(s)://[Endpoint]/?Action=DescribeCharacterSet &DBInstanceName=pxc-********* &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <DescribeCharacterSetResponse>
    <Message>success</Message>
    <RequestId>709C1E40-092D-4A3D-9958-6D7438******</RequestId>
    <Success>true</Success>
    <Data>
        <Engine>polarx</Engine>
        <CharacterSet>utf8</CharacterSet>
    </Data>
</DescribeCharacterSetResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "Message" : "success",
  "RequestId" : "709C1E40-092D-4A3D-9958-6D7438******",
  "Success" : true,
  "Data" : {
    "Engine" : "polarx",
    "CharacterSet" : [ "utf8" ]
```

`}` `}`

#### DescribeDistributeTableList

Queries the details of tables in a PolarDB-X database.

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates sample code for different SDKs.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDistribut eTableList | The operation that you want to perform. Set the value to DescribeDistrib uteTableList. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where your PolarDB-X instance is deployed. |
| DBInstanceName | String | Yes | pxc-******** | The name of the PolarDB-X instance. |
| DbName | String | Yes | sbtest1 | The name of the database. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Message | String | Success | The response message. If the request is successful, Success is returned. If the request fails, an error code is returned. |
|---|---|---|---|
| RequestId | String | C458B1E8-1683-3645- B154-6BA32080EEA | The request ID. |
| Success | Boolean | true | Indicates whether the request is successful. |
| Data | Object |   | The returned data. |
| Tables | Array of Table |   | The list of tables. |
| TableName | String | sbtest1 | The name of the table. |
| TableType | String | multi | The type of the table. |
| TbKey | String | "" | The primary key of the table. |
| DbKey | String | id | The primary key of the database. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeDistributeTableList &RegionId=cn-hangzhou &DBInstanceName=pxc-******** &DbName=sbtest1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <DescribeDistributeTableListResponse>
    <Message>Success</Message>
    <RequestId>C458B1E8-1683-3645-B154-6BA32080EEA</RequestId>
    <Success>true</Success>
    <Data>
        <Tables>
            <TableName>sbtest1</TableName>
            <TableType>multi</TableType>
            <TbKey>""</TbKey>
            <DbKey>id</DbKey>
        </Tables>
    </Data>
</DescribeDistributeTableListResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "Message" : "Success",
  "RequestId" : "C458B1E8-1683-3645-B154-6BA32080EEA",
  "Success" : true,
  "Data" : {
    "Tables" : [ {
      "TableName" : "sbtest1",
      "TableType" : "multi",
      "TbKey" : """",
      "DbKey" : "id"
    } ]
```

`}` `}`

#### ModifyDatabaseDescription

Modifies the description of a PolarDB-X database.

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | ModifyDatabaseD escription | The operation to perform. Set the value to ModifyDatabas eDescription. |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the PolarDB-X instance resides. |
| DBInstanceName | String | Yes | pxc-hzjasd**** | The name of the PolarDB-X instance. |
| DbName | String | Yes | testDB | The name of the database. |
| DbDescription | String | Yes | DatabaseForTest | The new description of the database. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | success | The returned message. Returns success if the request succeeds, or an error code if the request fails. |
| RequestId | String | FEA5DC20-6D8A- 5979-97AA- FC57546ADC20 | The request ID. |
| Success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyDatabaseDescription &RegionId=cn-hangzhou &DBInstanceName=pxc-hzjasd**** &DbName=testDB &DbDescription=DatabaseForTest &<Common request parameters>
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <ModifyDatabaseDescriptionResponse>
    <Message>success</Message>
    <RequestId>FEA5DC20-6D8A-5979-97AA-FC57546ADC20</RequestId>
    <Success>true</Success>
</ModifyDatabaseDescriptionResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "Message" : "success",
  "RequestId" : "FEA5DC20-6D8A-5979-97AA-FC57546ADC20",
  "Success" : true
```

`}`

#### DescribeDbList

Queries the databases in a PolarDB-X instance, including each database's character set and the accounts authorized to access it.

**Debugging**

Alibaba Cloud provides OpenAPI Explorer to simplify API usage. OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDbList | The operation that you want to perform. Set the value to DescribeDbList. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the PolarDB-X instance resides. |
| DBInstanceName | String | Yes | pxc-******** | The name of the PolarDB-X instance. |
| DBName | String | No | db name _ | The name of the database to query. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C458B1E8-1683-3645- B154-6BA32080EEA | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. |
| Message | String | Success | The response message. Returns success if the request succeeded, or an error code if it failed. |
| Data | Array of DB |   | The list of databases. |
| └ DBName | String | test | The name of the database. |
| └ DBDescription | String | test | The description of the database. |
| └ DBInstanceName | String | pxc-******** | The name of the PolarDB-X instance in which the database is deployed. |
| └ CharacterSetName | String | utf8mb4 | The character set of the database. |
| └ Accounts | Array of Account |   | The accounts authorized to access the database. |
| └ AccountName | String | root4test | The username of the account. |
| └ AccountPrivilege | String | ReadWrite | The permissions granted to the account. |

**Examples**

Sample request

```
http(s)://[Endpoint]/?Action=DescribeDbList &RegionId=cn-hangzhou &DBInstanceName=pxc-******** &DBName=db_name &<Common request parameters>
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <DescribeDbListResponse>
    <Message>Success</Message>
    <RequestId>C458B1E8-1683-3645-B154-6BA32080EEA</RequestId>
    <Success>true</Success>
    <Data>
        <DBName>test</DBName>
        <DBDescription>test</DBDescription>
        <DBInstanceName>pxc-********</DBInstanceName>
        <CharacterSetName>utf8mb4</CharacterSetName>
        <Accounts>
            <AccountPrivilege>ReadWrite</AccountPrivilege>
            <AccountName>root4test</AccountName>
        </Accounts>
    </Data>
</DescribeDbListResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "Message" : "Success",
  "RequestId" : "C458B1E8-1683-3645-B154-6BA32080EEA",
  "Success" : true,
  "Data" : [ {
    "DBName" : "test",
    "DBDescription" : "test",
    "DBInstanceName" : "pxc-********",
    "CharacterSetName" : "utf8mb4",
    "Accounts" : [ {
      "AccountPrivilege" : "ReadWrite",
      "AccountName" : "root4test"
    } ]
  } ]
```

`}`

### Regions

#### DescribeRegions

Call the DescribeRegions operation to get the region list.

**Debugging**

You can use OpenAPI Explorer to run this operation. OpenAPI Explorer automatically calculates the signature and generates SDK code samples after a successful run.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRegions | The operation that you want to perform. Set the value to DescribeRegions. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The error code. |
| Message | String | success | The error message. |
| RequestId | String | C458B1E8-1683- 3645-B154- 6BA32080EEA | The request ID. |
| Success | Boolean | true | Indicates whether the request succeeded. |
| ErrorCode | Integer | 200 | The error code. |
| Regions | Array of Region |   | The list of regions. |
| Region |   |   |   |
| SupportPolarx 10 | Boolean | true | Indicates whether PolarDB-X 1.0 is supported. |
| SupportPolarx 20 | Boolean | true | Indicates whether PolarDB-X 2.0 is supported. |
| RegionId | String | ch-hangzhou | The region ID. |
| Zones | Array of Zone |   | The list of zones. |
| Zone |   |   |   |
| ZoneId | String | cn-hangzhou-a | The zone. |

| VpcEnabled | Boolean | true | Indicates whether Virtual Private Cloud (VPC) is supported. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeRegions &Common request parameters
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <DescribeRegionsResponse>
    <Code>200</Code>
    <Message>success</Message>
    <RequestId>C458B1E8-1683-3645-B154-6BA32080EEA</RequestId>
    <Success>true</Success>
    <ErrorCode>200</ErrorCode>
    <Regions>
        <SupportPolarx10>true</SupportPolarx10>
        <SupportPolarx20>true</SupportPolarx20>
        <RegionId>ch-hangzhou</RegionId>
        <Zones>
            <ZoneId>cn-hangzhou-a</ZoneId>
            <VpcEnabled>true</VpcEnabled>
        </Zones>
    </Regions>
</DescribeRegionsResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "Code" : 200,
  "Message" : "success",
  "RequestId" : "C458B1E8-1683-3645-B154-6BA32080EEA",
  "Success" : true,
  "ErrorCode" : 200,
  "Regions" : [ {
    "SupportPolarx10" : true,
    "SupportPolarx20" : true,
    "RegionId" : "ch-hangzhou",
    "Zones" : [ {
      "ZoneId" : "cn-hangzhou-a",
      "VpcEnabled" : true
    } ]
  } ]
```

`}`

### Account management

#### CreateAccount

Call the CreateAccount operation to create an account.

**Debugging**

You can use OpenAPI Explorer to run this operation without manually calculating the signature. After you successfully run the operation, OpenAPI Explorer automatically generates sample SDK code.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateAccount | The operation that you want to perform. Set the value to CreateAccount. |
| RegionId | String | Yes | cn-hangzhou | The region where the instance resides. |
| DBInstanceNam e | String | Yes | pxc- ************** | The name of the instance. |
| AccountName | String | Yes | testAccount | The username of the account to be created. |

| AccountPasswor d | String | Yes | Test@1111 | The password of the account to be created. |
|---|---|---|---|---|
| DBName | String | No | testdb | The name of the database that the account can access. |
| AccountPrivilege | String | No | ReadWrite | The permissions granted to the new account on a specific database. Valid values: ReadWrite ReadOnly DMLOnly DDLOnly |
| AccountDescripti on | String | No | test | The description of the account. |
| SecurityAccount Name | String | No | securityAccount | The username of the data security administrator (DSA) account. Note This parameter is required if the three-role mode is enabled. Otherwise, it is optional. |
| SecurityAccount Password | String | No | securityPasswor d | The password of the DSA account. Note This parameter is required if the three-role mode is enabled. Otherwise, it is optional. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | **** | The error message returned if the request fails. If the request succeeds, this parameter is empty. |
| RequestId | String | 9B2F3840-5C98- 475C-B269- 2D5C3A31797C | The ID of the request. |

| Success | Boolean | true | Indicates whether the request was successful. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateAccount &RegionId=cn-hangzhou &DBInstanceName=pxc-************** &AccountName=testAccount &AccountPassword=Test@1111 &DBName=testdb &AccountPrivilege=ReadWrite &AccountDescription=test &SecurityAccountName=securityAccount &SecurityAccountPassword=securityPassword &Common request parameters
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <CreateAccountResponse>
    <Message>****</Message>
    <RequestId>9B2F3840-5C98-475C-B269-2D5C3A31797C</RequestId>
    <Success>true</Success>
</CreateAccountResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "Message" : "****",
  "RequestId" : "9B2F3840-5C98-475C-B269-2D5C3A31797C",
  "Success" : true
```

`}`

#### ModifyAccountPrivilege

Call the ModifyAccountPrivilege operation to modify account permissions.

**Debugging**

You can use OpenAPI Explorer to call this operation without calculating signatures. After you run the operation successfully, OpenAPI Explorer automatically generates SDK code examples.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyAccountPr ivilege | The operation that you want to perform. Set the value to ModifyAccountPrivilege. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. |
| DBInstanceNam e | String | Yes | pxc- htri0ori****** | The ID of the instance. |
| AccountName | String | Yes | account sec _ | The username of the account. |
| DbName | String | Yes | sbtest | The name of the database. |
| AccountPrivilege | String | Yes | ReadWrite | The permission of the account. Valid values: ReadWrite ReadOnly DMLOnly DDLOnly |
| SecurityAccount Name | String | No | account audit _ | The username of the data security administrator (DSA) account. |
| SecurityAccount Password | String | No | ***** | The password of the DSA account. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | success | The message that is returned. If the request is successful, "success" is returned. If the request fails, an error code is returned. |

| RequestId | String | 73559800-3c8c- 11ec-bd40- 99cfcff3fe1e | The unique request ID. |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyAccountPrivilege &RegionId=cn-hangzhou &DBInstanceName=pxc-htri0ori****** &AccountName=account_sec &DbName=sbtest &AccountPrivilege=ReadWrite &SecurityAccountName=account_audit &SecurityAccountPassword=***** &Common request parameters
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <ModifyAccountPrivilegeResponse>
    <Message>success</Message>
    <RequestId>73559800-3c8c-11ec-bd40-99cfcff3fe1e</RequestId>
    <Success>true</Success>
</ModifyAccountPrivilegeResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "Message" : "success",
  "RequestId" : "73559800-3c8c-11ec-bd40-99cfcff3fe1e",
  "Success" : true
```

`}`

#### EnableRightsSeparation

Call the EnableRightsSeparation operation to enable the three-role mode for a PolarDB-X instance.

**Debugging**

You can use OpenAPI Explorer to run this operation. OpenAPI Explorer automatically calculates the signature and generates SDK code samples after the operation succeeds.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | EnableRightsSep aration | The operation that you want to perform. Set the value to EnableRightsSeparation. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. |
| DBInstanceNam e | String | Yes | pxc- htri0ori****** | The name of the instance. |
| SecurityAccount Name | String | Yes | account sec _ | The username of the data security administrator (DSA) account. |
| SecurityAccount Password | String | Yes | ***** | The password of the DSA account. |
| SecurityAccount Description | String | No | test123 | The description of the DSA account. |
| AuditAccountNa me | String | Yes | account audit _ | The username of the data audit administrator (DAA) account. |
| AuditAccountPas sword | String | Yes | ****** | The password of the DAA account. |
| AuditAccountDe scription | String | No | test123 | The description of the DAA account. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | success | If the request succeeds, the system returns "success". If the request fails, the system returns an error code. |
| RequestId | String | 73559800-3c8c- 11ec-bd40- 99cfcff3fe1e | The unique ID of the request. |

| Success | Boolean | true | Indicates whether the request was successful. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=EnableRightsSeparation &RegionId=cn-hangzhou &DBInstanceName=pxc-htri0ori****** &SecurityAccountName=account_sec &SecurityAccountPassword=***** &SecurityAccountDescription=test123 &AuditAccountName=account_audit &AuditAccountPassword=****** &AuditAccountDescription=test123 &Common request parameters
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <EnableRightsSeparationResponse>
    <Message>success</Message>
    <RequestId>73559800-3c8c-11ec-bd40-99cfcff3fe1e</RequestId>
    <Success>true</Success>
</EnableRightsSeparationResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "Message" : "success",
  "RequestId" : "73559800-3c8c-11ec-bd40-99cfcff3fe1e",
  "Success" : true
```

`}`

#### ResetAccountPassword

Call the ResetAccountPassword operation to reset the password for a database account.

**Debugging**

You can use OpenAPI Explorer to call this operation without calculating a signature. After you run the operation successfully, OpenAPI Explorer automatically generates SDK code examples.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ResetAccountPa ssword | The operation that you want to perform. Set the value to ResetAccountPassword. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. |
| DBInstanceNam e | String | Yes | pxc- htri0ori****** | The name of the instance. |
| AccountName | String | Yes | account | The name of the account. |
| AccountPasswor d | String | Yes | ***** | The password of the account. |
| SecurityAccount Name | String | No | account sec _ | The name of the security administrator account. |
| SecurityAccount Password | String | No | ***** | The password of the security administrator account. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | success | The response message. If the request is successful, "success" is returned. If the request fails, an error code is returned. |
| RequestId | String | 73559800-3c8c- 11ec-bd40- 99cfcff3fe1e | The unique request ID. |
| Success | Boolean | true | Indicates whether the request was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ResetAccountPassword &RegionId=cn-hangzhou &DBInstanceName=pxc-htri0ori****** &AccountName=account &AccountPassword=***** &SecurityAccountName=account_sec &SecurityAccountPassword=***** &Common request parameters
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <ResetAccountPasswordResponse>
    <Message>success</Message>
    <RequestId>73559800-3c8c-11ec-bd40-99cfcff3fe1e</RequestId>
    <Success>true</Success>
</ResetAccountPasswordResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "Message" : "success",
  "RequestId" : "73559800-3c8c-11ec-bd40-99cfcff3fe1e",
  "Success" : true
```

`}`

#### CreateSuperAccount

Creates a privileged account for a PolarDB-X instance. Each instance supports only one privileged account.

**Debugging**

OpenAPI Explorer automatically calculates the signature value and generates SDK sample code. Use it to simplify API calls and reduce manual effort.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateSuperAcco unt | The operation to perform. Set the value to CreateSuperAcc ount. |

| RegionId | String | Yes | cn-hangzhou | The region where the PolarDB-X instance resides. |
|---|---|---|---|---|
| DBInstanceName | String | Yes | pxc-************ | The name of the PolarDB-X instance. |
| AccountName | String | Yes | dba | The username of the privileged account. |
| AccountPassword | String | Yes | testdbapassword | The password of the privileged account. |
| AccountDescripti on | String | No | testdbadescriptio n | The description of the privileged account. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9B2F3840-5C98-475C- B269-2D5C3A31797C | The request ID. |
| Success | Boolean | true | Indicates whether the request is successful. |
| Message | String | ***** | The returned message. Returns success if the request succeeds, or an error code if it fails. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateSuperAccount &RegionId=cn-hangzhou &DBInstanceName=pxc-************ &AccountName=dba &AccountPassword=testdbapassword &AccountDescription=testdbadescription &<Common request parameters>
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <CreateSuperAccountResponse>
    <Message>*****</Message>
    <RequestId>9B2F3840-5C98-475C-B269-2D5C3A31797C</RequestId>
    <Success>true</Success>
</CreateSuperAccountResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "Message" : "*****",
  "RequestId" : "9B2F3840-5C98-475C-B269-2D5C3A31797C",
  "Success" : true
```

`}`

#### DeleteAccount

Deletes a database account from a PolarDB-X instance.

**Debugging**

You can call this operation in OpenAPI Explorer, which automatically calculates the required signature and generates sample code for different SDKs.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteAccount | The operation to perform. Set the value to DeleteAccount. |
| DBInstanceName | String | Yes | pxc-********* | The name of the PolarDB-X instance. |
| AccountName | String | Yes | testaccount | The username of the account to delete. |
| RegionId | String | Yes | cn-hangzhou | The region where the PolarDB-X instance resides. |

| SecurityAccount Name | String | No | securityAccount | The username of the data security administrator (DSA) account. Important Required if three-role mode is enabled for the instance. |
|---|---|---|---|---|
| SecurityAccountP assword | String | No | securityPassword | The password of the DSA account. Important Required if three-role mode is enabled for the instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | **** | The returned message. Returns success if the request succeeds, or an error code if it fails. |
| RequestId | String | 9B2F3840-5C98-475C- B269-2D5C3A31797C | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. |

**Examples**

Sample request

```
http(s)://[Endpoint]/?Action=DeleteAccount &DBInstanceName=pxc-********* &AccountName=testaccount &RegionId=cn-hangzhou &SecurityAccountName=securityAccount &SecurityAccountPassword=securityPassword &<Common request parameters>
```

Sample success responses XML format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <DeleteAccountResponse>
    <Message>****</Message>
    <RequestId>9B2F3840-5C98-475C-B269-2D5C3A31797C</RequestId>
    <Success>true</Success>
</DeleteAccountResponse>
```

JSON format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "Message" : "****",
  "RequestId" : "9B2F3840-5C98-475C-B269-2D5C3A31797C",
  "Success" : true
```

`}`

#### DescribeAccountList

Queries the accounts in a PolarDB-X instance. Filter by account name or account type, or retrieve all accounts at once.

**Debugging**

Alibaba Cloud provides OpenAPI Explorer to simplify API usage. OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAccount List | The operation to perform. Set the value to DescribeAccoun tList. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the PolarDB-X instance resides. |
| DBInstanceName | String | Yes | pxc-******** | The name of the PolarDB-X instance. |

| AccountName | String | No | testaccount | The username of the account to query. Specify this parameter to query a specific account. |
|---|---|---|---|---|
| AccountType | String | No | 0 | The type of accounts to query. If not specified, all accounts in the instance are returned. Valid values depend on whether the three-role mode is enabled:<br>- Three-role mode disabled: 0 (standard accounts), 1 (privileged account)<br>- Three-role mode enabled: 0 (standard accounts), 2 (database administrator (DBA) account), 3 (data security administrator (DSA) account), 4 (data audit administrator (DAA) account) |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9B2F3840-5C98-475C- B269-2D5C3A31797C | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. |
| Message | String | success | The response message. Returns success if the request succeeded, or an error code if it failed. |
| Data | Array of Account |   | The account details returned. |

| GmtCreated | String | 2012-06-08T15:00Z | The time when the account was created. |
|---|---|---|---|
| DBInstanceName | String | pxc-********* | The name of the PolarDB-X instance. |
| AccountDescription | String | testaccount desc | The description of the account. |
| DBName | String | testdb | The PolarDB-X database that the account can access. |
| AccountPrivilege | String | ReadWrite | The permissions granted to the account. |
| AccountType | String | 0 | The type of the account. Valid values depend on whether the three-role mode is enabled:<br>- Three- role mode disabled: 0 (standard accounts), 1 (privileged account) <br>- Three-role mode enabled: 0 (standard accounts), 2 (database administrator (DBA) account), 3 (data security administrator (DSA) account), 4 (data audit administrator (DAA) account) |
| AccountName | String | testAccount | The username of the account. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeAccountList &RegionId=cn-hangzhou &DBInstanceName=pxc-******** &AccountName=testaccount &AccountType=0 &<Common request parameters>
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <DescribeAccountListResponse>
    <Message>success</Message>
    <RequestId>9B2F3840-5C98-475C-B269-2D5C3A31797C</RequestId>
    <Success>true</Success>
    <Data>
        <GmtCreated>2012-06-08T15:00Z</GmtCreated>
        <DBInstanceName>pxc-*********</DBInstanceName>
        <AccountDescription>testaccount desc</AccountDescription>
        <DBName>testdb</DBName>
        <AccountPrivilege>ReadWrite</AccountPrivilege>
        <AccountType>0</AccountType>
        <AccountName>testAccount</AccountName>
    </Data>
</DescribeAccountListResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "Message" : "success",
  "RequestId" : "9B2F3840-5C98-475C-B269-2D5C3A31797C",
  "Success" : true,
  "Data" : [ {
    "GmtCreated" : "2012-06-08T15:00Z",
    "DBInstanceName" : "pxc-*********",
    "AccountDescription" : "testaccount desc",
    "DBName" : "testdb",
    "AccountPrivilege" : "ReadWrite",
    "AccountType" : "0",
    "AccountName" : "testAccount"
  } ]
```

`}`

#### ModifyAccountDescription

Modifies the description of a database account in a PolarDB-X instance.

**Debugging**

OpenAPI Explorer simplifies API usage by automatically calculating request signatures and generating SDK sample code. Try this operation in OpenAPI Explorer.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | ModifyAccountDe scription | The operation to perform. Set the value to ModifyAccount Description. |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The region where the PolarDB-X instance resides. |
| DBInstanceName | String | Yes | pxc-hzjasd**** | The name of the PolarDB-X instance. |
| AccountName | String | Yes | account | The username of the account to modify. |
| AccountDescripti on | String | No | AccountForTest | The new description for the account. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | msg | The response message. Returns success if the request succeeds, or an error code if it fails. |
| RequestId | String | FEA5DC20-6D8A- 5979-97AA- FC57546ADC20 | The request ID. |
| Success | Boolean | true | Indicates whether the request succeeded. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyAccountDescription &RegionId=cn-hangzhou &DBInstanceName=pxc-hzjasd**** &AccountName=account &AccountDescription=AccountForTest &<Common request parameters>
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <ModifyAccountDescriptionResponse>
    <Message>msg</Message>
    <RequestId>FEA5DC20-6D8A-5979-97AA-FC57546ADC20</RequestId>
    <Success>true</Success>
</ModifyAccountDescriptionResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "Message" : "msg",
  "RequestId" : "FEA5DC20-6D8A-5979-97AA-FC57546ADC20",
  "Success" : true
```

`}`

### Data security

#### AllocateInstancePublicConnection

Creates a public endpoint for a PolarDB-X instance.

**Debugging**

OpenAPI Explorer automatically calculates the signature value. Call this operation in OpenAPI Explorer to generate sample code for different SDKs.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | No | AllocateInstanceP ublicConnection | The operation that you want to perform. Set the value to AllocateInstanc ePublicConnect ion. |
| DBInstanceName | String | Yes | pxc- \*\*\*\*\*\*\*\*\*\*\ *\*\*\* | The name of the instance. |
| ConnectionString Prefix | String | Yes | pxc- \*\*\*\*\*\*\*\*\*\*\ *\*\*\* | The prefix of the public endpoint. |

| Port | String | Yes | 3306 | The port number of the public endpoint. |
|---|---|---|---|---|
| RegionId | String | No | cn-hangzhou | The region where the PolarDB-X instance resides. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9B2F3840-5C98-475C- B269-2D5C3A31797C | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AllocateInstancePublicConnection &DBInstanceName=pxc-************** &ConnectionStringPrefix=pxc-************** &Port=3306 &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <AllocateInstancePublicConnectionResponse>
    <RequestId>9B2F3840-5C98-475C-B269-2D5C3A31797C</RequestId>
</AllocateInstancePublicConnectionResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "RequestId" : "9B2F3840-5C98-475C-B269-2D5C3A31797C"
```

`}`

#### CheckCloudResourceAuthorized

Call the CheckCloudResourceAuthorized operation to check whether your Alibaba Cloud account is authorized to use Key Management Service (KMS) for a PolarDB-X instance.

**Debugging**

You can use OpenAPI Explorer to call this operation. OpenAPI Explorer automatically calculates the signature and generates SDK code samples after the call succeeds.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CheckCloudReso urceAuthorized | The operation that you want to perform. Set the value to CheckCloudResourceAuthorized. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the instance resides. |
| DBInstanceNam e | String | Yes | pxc-******** | The instance ID. |
| RoleArn | String | No | acs:ram::12345 6789012****:rol e/AliyunRdsInsta nceEncryptionD efaultRole | The Alibaba Cloud Resource Name (ARN) of the RAM role that you want to assign to your account. Specify the ARN in the format of acs:ram::$accountID:role/$roleName. After the RAM role is assigned, you can use KMS for your PolarDB-X instance. $accountID: the ID of the Alibaba Cloud account. To view the account ID, you can log on to the Alibaba Cloud Management Console, move the pointer over your profile picture in the upper- right corner of the page, and then click Security Settings. $roleName: the name of the RAM role. Set the value to AliyunRdsInstanceEncryptionDefau ltRole. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | A501A191-BD70- 5E50-98A9- C2A486A82**** | The request ID. |

| Data | Object |   | The response body. |
|---|---|---|---|
| AuthorizationS tate | String | 0 | The authorization state of your account. Valid values: 0: Your account is not authorized to use KMS. 1: Your account is authorized to use KMS. 2: KMS is not activated for your account. |
| RoleArn | String | acs:ram::12345678 9012****:role/Aliyu nRdsInstanceEncry ptionDefaultRole | The ARN of the RAM role that is assigned to your account. The ARN is in the format of acs:ram::$accountID:role/$roleName. After the RAM role is assigned, you can use KMS for your PolarDB-X instance. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CheckCloudResourceAuthorized &RegionId=cn-hangzhou &DBInstanceName=pxc-******** &RoleArn=acs:ram::123456789012****:role/AliyunRdsInstanceEncryptionDefaultRole &Common request parameters
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <CheckCloudResourceAuthorizedResponse>
    <RequestId>A501A191-BD70-5E50-98A9-C2A486A82****</RequestId>
    <Data>
        <AuthorizationState>0</AuthorizationState>
<RoleArn>acs:ram::123456789012****:role/AliyunRdsInstanceEncryptionDefaultRole</RoleArn>
    </Data>
</CheckCloudResourceAuthorizedResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "RequestId" : "A501A191-BD70-5E50-98A9-C2A486A82****",
  "Data" : {
    "AuthorizationState" : "0",
    "RoleArn" : "acs:ram::123456789012****:role/AliyunRdsInstanceEncryptionDefaultRole"
```

`}` `}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 403 | IncorrectEngineVer sion | The current engine version does not support the operation. | The current engine version does not support the operation. |

For a list of error codes, visit the API Error Center.

#### DescribeDBInstanceTDE

Call the DescribeDBInstanceTDE operation to query whether Transparent Data Encryption (TDE) is enabled for an instance.

**Debugging**

You can use OpenAPI Explorer to run this operation without calculating a signature. After you run the operation successfully, OpenAPI Explorer automatically generates SDK code examples.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInsta nceTDE | The operation that you want to perform. Set the value to DescribeDBInstanceTDE. |
| DBInstanceNam e | String | No | pxc-******** | The instance name. |
| RegionId | String | No | cn-hangzhou | The region ID of the instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C458B1E8-1683- 3645-B154- 6BA32080EEA | The request ID. |
| Data | Object |   | The data structure. |
| TDEStatus | String | 0 | Indicates whether TDE is enabled: 0: disabled 1: enabled |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeDBInstanceTDE &DBInstanceName=pxc-******** &RegionId=cn-hangzhou &Common request parameters
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <DescribeDBInstanceTDEResponse>
    <RequestId>C458B1E8-1683-3645-B154-6BA32080EEA</RequestId>
    <Data>
        <TDEStatus>0</TDEStatus>
    </Data>
</DescribeDBInstanceTDEResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "RequestId" : "C458B1E8-1683-3645-B154-6BA32080EEA",
  "Data" : {
    "TDEStatus" : "0"
```

`}` `}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 403 | IncorrectEngineVer sion | The current engine version does not support the operation. | The current engine version does not support the operation. |

For a list of error codes, visit the API Error Center.

#### 4.9.4. \ DescribeUserEncryptionKeyList

Queries the keys that are used by Transparent Data Encryption (TDE) for a PolarDB-X instance.

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeUserEncr yptionKeyList | The operation that you want to perform. Set the value to DescribeUserEn cryptionKeyList . |
| DBInstanceName | String | No | pxc-hzjasdyu**** | The ID of the PolarDB-X instance. |
| RegionId | String | No | cn-hangzhou | The region ID of the PolarDB-X instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | FEA5DC20-6D8A- 5979-97AA- FC57546ADC20 | The request ID. |
| Data | Object |   | The returned data. |
| KeyIds | Array of String | RkVBNURDMjAtNkQ4Q S01OTc5LTk3QUEtRkM 1NzU0Nk****** | The keys that are used by TDE to encrypt data. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeUserEncryptionKeyList &DBInstanceName=pxc-hzjasdyu**** &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <DescribeUserEncryptionKeyListResponse>
    <RequestId>FEA5DC20-6D8A-5979-97AA-FC57546ADC20</RequestId>
    <Data>
        <KeyIds>RkVBNURDMjAtNkQ4QS01OTc5LTk3QUEtRkM1NzU0Nk******</KeyIds>
    </Data>
</DescribeUserEncryptionKeyListResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "RequestId" : "FEA5DC20-6D8A-5979-97AA-FC57546ADC20",
  "Data" : {
    "KeyIds" : [ "RkVBNURDMjAtNkQ4QS01OTc5LTk3QUEtRkM1NzU0Nk******" ]
```

`}` `}`

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | IncorrectEngineVersio n | The current engine version does not support the operation. | The engine version of the specified PolarDB- X instance does not support this operation. |

For a list of error codes, visit the API Error Center.

#### DescribeSecurityIps

Call the DescribeSecurityIps operation to query the IP address whitelist of a PolarDB-X instance.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | Syst em | Yes | DescribeSecurityIps | The operation that you want to perform. Set the value to DescribeSecurityIps. |
| app ip _ | Strin g | Syst em | Yes | 192.168.1.xxx | The IP address of the client application that initiates the API request. The system uses this parameter for security audit and source verification. |
| ak mfa pr _ _ esent | Strin g | Syst em | Yes | true | Indicates whether the AccessKey in use has been bound to Multi- Factor Authentication (MFA). The system uses this parameter to verify security policies for high- risk operations. |
| RegionId | Strin g | Quer y | Yes | cn-hangzhou | The ID of the region where the instance resides. |
| DBInstanc eName | Strin g | Quer y | Yes | pxc-hzjasd**** | The name of the instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 14036EBE-CF2E- 44DB-ACE9- AC6157D3A6FC | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |
| Message | String | success | Additional information returned by the API. The system returns "success" for a successful request and returns the corresponding error code for a failed request. |
| Data | Struct | - | The returned data. |

| -GroupItems | Array | - | The details about the IP address whitelists. |
|---|---|---|---|
| --GroupName | String | defaultGroup | The name of the IP address whitelist. |
| --SecurityIPList | String | 127.0.x.x,172.168. x.x | The IP addresses and CIDR blocks that are specified in the IP address whitelist. |
| -- SecurityIPType | String | IPv4 | The type of the security group. Valid values: IPv4 IPv6 |
| --CreateTime | String | 2021-08- 31T08:56:25.000+ 0000 | The creation time. |
| - DBInstanceNa me | String | pxc-hzjasd**** | The name of the instance. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSecurityIps &RegionId=cn-hangzhou &DBInstanceName=pxc-hzjasd**** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"14036EBE-CF2E-44DB-ACE9-AC6157D3A6FC",
 "Message":"success",
 "Data":{
  "GroupItems":[
```

`{`

```json
    "GroupName":"defaultGroup",
    "SecurityIPType":"IPv4",
    "SecurityIPList":"127.0.0.1,172.168.0.0",
    "CreateTime":"2021-08-31T08:56:25.000+0000"
```

`}` `],`

```json
  "DBInstanceName":"pxc-hzjasd****"
```

`},`

```json
 "Success":true
```

`}` `XML` format

```xml
<RequestId>14036EBE-CF2E-44DB-ACE9-AC6157D3A6FC</RequestId> <Message>success</Message> <Data>
 <GroupItems>
  <GroupName>defaultGroup</GroupName>
  <SecurityIPType>IPv4</SecurityIPType>
  <SecurityIPList>127.0.0.1,172.168.0.0</SecurityIPList>
  <CreateTime>2021-08-31T08:56:25.000+0000</CreateTime>
 </GroupItems>
 <DBInstanceName>pxc-hzjasd****</DBInstanceName>
</Data> <Success>true</Success>
```

#### ModifySecurityIps

Call the ModifySecurityIps operation to modify the IP address whitelist for an instance.

**Request headers**

This operation uses common request headers. No special request headers exist. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | Syst em | Yes | ModifySecurityIps | The operation that you want to perform. Set the value to ModifySecurityIps. |
| app ip _ | Strin g | Syst em | Yes | 192.168.1.105 | The IP address of the client application that initiates the API request. The system uses this IP address for security audit and source verification. |
| ak mfa pr _ _ esent | Strin g | Syst em | Yes | true | Indicates whether the AccessKey in use has been bound to Multi- Factor Authentication (MFA). The system uses this parameter to verify security policies for high- risk operations. |
| RegionId | Strin g | Quer y | Yes | cn-hangzhou | The ID of the region where the instance resides. |

| DBInstanc eName | Strin g | Quer y | Yes | pxc-hzjasd**** | The ID of the instance. |
|---|---|---|---|---|---|
| GroupNam e | Strin g | Quer y | No | default | The name of the IP whitelist group for the instance. |
| SecurityIPL ist | Strin g | Quer y | Yes | 127.0.0.1,192.168.0.0 | The list of IP addresses in the whitelist group. Separate multiple IP addresses with commas (,). |
| ModifyMod e | Strin g | Quer y | No | 1 | The modification mode of the IP whitelist. Valid values: 0: The system overwrites the original IP whitelist group. 1: The system creates an IP whitelist group. 2: The system deletes the original IP whitelist group. |
| SecurityIP Type | Strin g | Quer y | No | IPv4 | The type of IP address. This parameter is optional. Default value: IPv4. Valid values: IPv4 IPv6 |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | FEA5DC20-6D8A- 5979-97AA- FC57546ADC20 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |
| Message | String | success | The message returned for the request. If the request succeeded, "success" appears. If the request failed, an error code appears. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifySecurityIps &Action=ModifySecurityIps &app_ip= &ak_mfa_present= &RegionId=cn-hangzhou &DBInstanceName=pxc-hzjasd**** &SecurityIPList=127.0.0.1,192.168.0.0 &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"FEA5DC20-6D8A-5979-97AA-FC57546ADC20",
 "Message":"success",
 "Success":true
```

`}` `XML` format

```xml
<RequestId>FEA5DC20-6D8A-5979-97AA-FC57546ADC20</RequestId> <Message>success</Message> <Success>true</Success>
```

#### UpdateDBInstanceTDE

Call the UpdateDBInstanceTDE operation to enable Transparent Data Encryption (TDE) for an instance.

**Debugging**

You can use OpenAPI Explorer to run this operation. OpenAPI Explorer automatically calculates the signature and generates SDK code samples after the operation succeeds.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateDBInstan ceTDE | The operation that you want to perform. Set the value to UpdateDBInstanceTDE. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. |

| DBInstanceNam e | String | Yes | pxc-hzjasd**** | The ID of the instance. |
|---|---|---|---|---|
| TDEStatus | Integer | Yes | 1 | Specifies whether to enable TDE. The value is fixed at 1. |
| EncryptionKey | String | No | RkVBNURDMjAt NkQ4QS01OTc5 LTk3QUEtRkM1N zU0Nk****** | The ID of the custom key. If you do not specify this parameter, the system automatically generates a key. |
| RoleArn | String | No | acs:ram::14069 26****:role/aliyu nrdsinstanceenc ryptiondefaultrol e | The Alibaba Cloud Resource Name (ARN) of the Resource Access Management (RAM) role that you want to assign to your account. For more information, see the RAM role overview. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | FEA5DC20-6D8A- 5979-97AA- FC57546ADC20 | The ID of the request. |
| Data | Object |   | The returned information. |
| TaskId | String | 42292**** | The ID of the backend task. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateDBInstanceTDE &RegionId=cn-hangzhou &DBInstanceName=pxc-hzjasd**** &TDEStatus=1 &EncryptionKey=RkVBNURDMjAtNkQ4QS01OTc5LTk3QUEtRkM1NzU0Nk****** &RoleArn=acs:ram::1406926****:role/aliyunrdsinstanceencryptiondefaultrole &Common request parameters
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <UpdateDBInstanceTDEResponse>
    <RequestId>FEA5DC20-6D8A-5979-97AA-FC57546ADC20</RequestId>
    <Data>
        <TaskId>42292****</TaskId>
    </Data>
</UpdateDBInstanceTDEResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "RequestId" : "FEA5DC20-6D8A-5979-97AA-FC57546ADC20",
  "Data" : {
    "TaskId" : "42292****"
```

`}` `}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 403 | IncorrectEngineVer sion | The current engine version does not support the operation. | The current engine version does not support the operation. |

For a list of error codes, visit the API Error Center.

#### DescribeSQLLogRecords

Queries the SQL log records of a PolarDB-X instance.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSQLLog Records | The operation that you want to perform. Set the value to DescribeSQLLogRecords. |
| DBInstanceNam e | String | Yes | pxc- unrwuyttjx**** | The name of the instance. |

| DBName | String | Yes | aaa | The name of the database. |
|---|---|---|---|---|
| DBUser | String | Yes | testuser | The username of the database. |
| EndTime | String | Yes | 2022-08- 24T07:09:00Z | The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. The end time must be later than the start time. |
| ExtraField | Boolean | Yes | true | Specifies whether to include additional fields in the response. The additional fields are database engine- specific fields. Valid values: TRUE FALSE |
| ExtraFieldSearch | String | Yes | execute target _ _ schema=dbna _ me, execute so _ _ urce user=user _ name,trace id=t _ ransactionId, ex _ ecute logic id= _ _ nodeI | Additional fields used to filter the SQL log records. You must specify the additional fields as pairs of keys and values. Multiple key-value pairs can be specified in a format such as "dbname=test,dbuser=testuser". |
| InstanceEngine | String | Yes | polarx | The database engine type of the instance. Set the value to polarx. |
| InstanceName | String | Yes | pxc- unrwuyttjx**** | The name of the instance. |
| KeyWords | String | Yes | aaa | The keywords used to filter the SQL log records. |
| keyWordsAllMat ch | Boolean | Yes | false | Specifies whether all keywords must match for records to be included in the search result. Valid values: true and false. |
| PageCount | Integer | Yes | 1 | The page number. |
| PageSize | Integer | Yes | 10 | The number of entries per page. |
| RegionId | String | Yes | cn-wulan- env213-d01 | The region ID of the instance. |

| ReverseOrderQu ery | String | Yes | false | Specifies whether to return the SQL log records in reverse order. Valid values for the redline component: true (default): returns the SQL log records in reverse order. false: does not return the SQL log records in reverse order. |
|---|---|---|---|---|
| SQLSourceIP | String | Yes | 192.100.XX.XX | The IP address from which the SQL statement is executed. |
| SQLTemplateID | String | Yes | 11 | The ID of the SQL template. |
| SQLType | String | Yes | Insert,Update,D elete | The type of the SQL statement. Valid values: INSERT, UPDATE, and DELETE. Separate multiple types with commas (,). |
| StartTime | String | Yes | 2022-08- 24T06:59:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Struct |   | The information about the SQL log records of the instance. |
| PageNumber | Integer | 1 | The page number. |
| PageRecordCo unt | Integer | 5 | The number of SQL audit log entries on the current page. |
| RequestId | String | 02895B72-1178- 5799-991E- 663FB4EEDD84 | The ID of the request. |
| SQLRecordIte ms | Array of SQLRecordIte m |   | The information about individual SQL log records. |
| AccountName | String | huijnb | The name of the account. |

| DBName | String | rtyui | The name of the database. |
|---|---|---|---|
| DBNodeRole | String | master | The role of the database node on which the SQL statement was executed. Valid values: master: the primary node slave: a read-only node |
| ExecuteProces sID | String | 101 | The ID of the process or thread that executed the SQL statement. This parameter is reserved. |
| ExecuteTime | String | 2022-08- 24T08:21:22.660+ 00:00 | The time when the SQL statement was executed. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| ExtraFieldItem s |   | { "Tddlversion":"5.4. 14-16563827", "Sct":"0", "Smem":"0", "executestarttime" :"2022-08- 24T08:21:22.660+ 00:00", "Frows":"0", "Scnt":"0", "executesourceuse r":"drds", "tag:packid":"2e0c 13c56e251d03- 92482", "Ts":"1661329272 656", "sqlrendered":"sele ct sleep(10)", "Tmem":"0", "sqltotalcosttime":- 1, "sqlselectrows":- 1, "Lmem":"0", "sqlscanrows":1, "Mem":"0", "executetargetsch ema":"drds", "Ltc":"3983013", "schemaType":"pol arx", "uid":"1012354764 658849", "Ptc":"0", "Txid":"14ce2d05d | Other information. Example: { "Tddl version":"5.4.14-16563827", _ "Sct":"0", "Smem":"0", " execute start time":"2022-08- _ _ _ 24T08:21:22.660+00:00", "Frows":"0", "Scnt":"0", " execute source user":"drds", _ _ _ " tag : pack id ":"2e0c13c56e251d03 __ ____ _ __ -92482", "Ts":"1661329272656", " sql rendered":"select sleep(10)", _ _ "Tmem":"0", " sql total cost time":-1, _ _ _ _ " sql select rows":-1, _ _ _ "Lmem":"0", " sql scan rows":1, _ _ _ "Mem":"0", " execute target schema":"drds", _ _ _ "Ltc":"3983013", " schemaType":"polarx", _ " uid":"1012354764658849", _ "Ptc":"0", "Tx id":"14ce2d05de409000", _ " sql template params":"", _ _ _ " sql update rows":-1, _ _ _ |

|   | String | e409000", "sqltemplateparam s":"", "sqlupdaterows":- 1, "Mr":"0", "Mpct":"-1.0", "threadid":-1, "Arows":"0", "Prstc":"0", "Bid":"- 1", "executelogicid":"p xc-i-cfwboi1k6o", "Mbt":"0", "":"TDDL", "topic":"pxc- unrwuyttjxwhfk", "Traceid":"14ce2d0 5de409000", "Pctc":"0", "Pid":"- 1", "Letc":"922668", "Tid":"36f3bf88", "Type":"000", "executesourcepor t":55738, "Lio":"0", "Pstc":"0", "Lnet":"0.0", | "Mr":"0", "Mpct":"-1.0", " thread id":-1, _ _ "Arows":"0", "Prstc":"0", "Bid":"-1", " execute logic id":"pxc-i-cfwboi1k6o", _ _ _ "Mbt":"0", " ":"TDDL", _ " topic ":"pxc-unrwuyttjxwhfk", __ __ "Trace id":"14ce2d05de409000", _ "Pctc":"0", "Pid":"-1", "Letc":"922668", "Tid":"36f3bf88", "Type":"000", " execute source port":55738, _ _ _ |
|---|---|---|---|
|   |   | "Lotc":"3060345", "sqlcosttime":"100 04070", "Logversion":"V3", "Lcpu":"0", "executesource ip" _ :"10.213.1.1", "Wt":"TP" } | "Lio":"0", "Pstc":"0", "Lnet":"0.0", "Lotc":"3060345", " sql cost time":"10004070", _ _ _ "Log version":"V3", _ "Lcpu":"0", " execute source ip":"10.213.1.1", _ _ _ "Wt":"TP" } |
| ReturnRows | Long | 1 | The number of rows returned. |
| SQLTemplateI D | String | 11 | The ID of the SQL template. |
| SQLText | String | select * from a1; | The content of the SQL statement. |
| SQLType | String | select | The type of the SQL statement. |
| ScanRows | Long | 1 | The number of rows scanned by the SQL query. |
| SourceIP | String | 10.213.1.1 | The IP address from which the SQL statement was executed. |

| SourcePort | Integer | 55738 | The port from which the SQL statement was executed. |
|---|---|---|---|
| TotalExecution Times | Long | 1000 | The total execution time of the SQL statement. Unit: microseconds. |
| UpdateRows | Long | 1 | The number of rows updated by the SQL query. |
| TotalRecordCo unt | Integer | 100 | The total number of SQL log records. |
| RequestId | String | 02895B72-1178- 5799-991E- 663FB4EEDD84 | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSQLLogRecords &DBInstanceName=pxc-unrwuyttjx**** &DBName=aaa &DBUser=testuser &EndTime=2022-08-24T07:09:00Z &ExtraField=true &ExtraFieldSearch=_execute_target_schema=dbname,_execute_source_user=username,trace_id=tr sactionId,_execute_logic_id=nodeI &InstanceEngine=polarx &InstanceName=pxc-unrwuyttjx**** &KeyWords=aaa &keyWordsAllMatch=false &PageCount=1 &PageSize=10 &RegionId=cn-wulan-env213-d01 &ReverseOrderQuery=false &SQLSourceIP=192.100.XX.XX &SQLTemplateID=11 &SQLType=Insert,Update,Delete &StartTime=2022-08-24T06:59:00Z &<Common request parameters>
```

Sample success responses `XML` format

```json
<RequestId>02895B72-1178-5799-991E-663FB4EEDD84</RequestId> <Data>
    <TotalRecordCount>100</TotalRecordCount>
    <PageRecordCount>5</PageRecordCount>
    <RequestId>02895B72-1178-5799-991E-663FB4EEDD84</RequestId>
    <PageNumber>1</PageNumber>
    <SQLRecordItems>
        <SQLTemplateID>11</SQLTemplateID>
        <ExecuteTime>2022-08-24T08:21:22.660+00:00</ExecuteTime>
        <ExecuteProcessID>101</ExecuteProcessID>
        <DBNodeRole>master</DBNodeRole>
        <TotalExecutionTimes>1000</TotalExecutionTimes>
        <ExtraFieldItems>{ "Tddlversion":"5.4.14-16563827", "Sct":"0", "Smem":"0",
"executestarttime":"2022-08-24T08:21:22.660+00:00", "Frows":"0", "Scnt":"0", "executeso urceuser":"drds", "tag:packid":"2e0c13c56e251d03-92482", "Ts":"1661329272656", "sqlrend ered":"select sleep(10)", "Tmem":"0", "sqltotalcosttime":-1, "sqlselectrows":-1, "Lmem" :"0", "sqlscanrows":1, "Mem":"0", "executetargetschema":"drds", "Ltc":"3983013", "schem aType":"polarx", "uid":"1012354764658849", "Ptc":"0", "Txid":"14ce2d05de409000", "sqlte mplateparams":"", "sqlupdaterows":-1, "Mr":"0", "Mpct":"-1.0", "threadid":-1, "Arows":" 0", "Prstc":"0", "Bid":"-1", "executelogicid":"pxc-i-cfwboi1k6o", "Mbt":"0", "":"TDDL", "topic":"pxc-unrwuyttjxwhfk", "Traceid":"14ce2d05de409000", "Pctc":"0", "Pid":"-1", "Le tc":"922668", "Tid":"36f3bf88", "Type":"000", "executesourceport":55738, "Lio":"0", "Ps tc":"0", "Lnet":"0.0", "Lotc":"3060345", "sqlcosttime":"10004070", "Logversion":"V3", " Lcpu":"0", "executesource_ip":"10.213.1.1", "Wt":"TP" }</ExtraFieldItems>
        <SourcePort>55738</SourcePort>
        <ReturnRows>1</ReturnRows>
        <UpdateRows>1</UpdateRows>
        <SQLText>select * from a1;</SQLText>
        <ScanRows>1</ScanRows>
        <SourceIP>10.213.1.1</SourceIP>
        <DBName>rtyui</DBName>
        <SQLType>select</SQLType>
        <AccountName>huijnb</AccountName>
    </SQLRecordItems>
</Data>
```

`JSON` format

```json
{"RequestId":"02895B72-1178-5799-991E-663FB4EEDD84","Data": {"TotalRecordCount":"100","PageRecordCount":"5","RequestId":"02895B72-1178-5799-991E-66 3FB4EEDD84","PageNumber":"1","SQLRecordItems": [{"SQLTemplateID":"11","ExecuteTime":"2022-08- 24T08:21:22.660+00:00","ExecuteProcessID":"101","DBNodeRole":"master","TotalExecutionTime :"1000","ExtraFieldItems":"{ \"Tddlversion\":\"5.4.14-16563827\", \"Sct\":\"0\", \"Smem \":\"0\", \"executestarttime\":\"2022-08-24T08:21:22.660+00:00\", \"Frows\":\"0\", \"Sc nt\":\"0\", \"executesourceuser\":\"drds\", \"tag:packid\":\"2e0c13c56e251d03-92482\", \"Ts\":\"1661329272656\", \"sqlrendered\":\"select sleep(10)\", \"Tmem\":\"0\", \"sqlto talcosttime\":-1, \"sqlselectrows\":-1, \"Lmem\":\"0\", \"sqlscanrows\":1, \"Mem\":\"0\", \"executetargetschema\":\"drds\", \"Ltc\":\"3983013\", \"schemaType\":\"polarx\", \"uid\":\"1012354764658849\", \"Ptc\":\"0\", \"Txid\":\"14ce2d05de409000\", \"sqltemplateparams\":\"\", \"sqlupdaterows\":-1, \"Mr\" :\"0\", \"Mpct\":\"-1.0\", \"threadid\":-1, \"Arows\":\"0\", \"Prstc\":\"0\", \"Bid\":\ "-1\", \"executelogicid\":\"pxc-i-cfwboi1k6o\", \"Mbt\":\"0\", \"\":\"TDDL\", \"topic\" :\"pxc-unrwuyttjxwhfk\", \"Traceid\":\"14ce2d05de409000\", \"Pctc\":\"0\", \"Pid\":\"-1 \", \"Letc\":\"922668\", \"Tid\":\"36f3bf88\", \"Type\":\"000\", \"executesourceport\":55738, \"Lio\":\"0\", \"Pstc\":\"0\", \"Lnet\":\"0.0\", \"Lotc\": \"3060345\", \"sqlcosttime\":\"10004070\", \"Logversion\":\"V3\", \"Lcpu\":\"0\", \"exe cutesource_ip\":\"10.213.1.1\", \"Wt\":\"TP\" }","SourcePort":"55738","ReturnRows":"1","UpdateRows":"1","SQLText":"select * from a1;" ,"ScanRows":"1","SourceIP":"10.213.1.1","DBName":"rtyui","SQLType":"select","AccountName" huijnb"}]}}
```

### Backup management

#### CreateBackup

Creates a backup for a PolarDB-X instance and returns the backup set ID.

**Try it now**

Use OpenAPI Explorer to call this operation directly from your browser. OpenAPI Explorer calculates request signatures automatically and generates SDK sample code.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateBackup | The operation to perform. Set the value to CreateBackup. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the PolarDB-X instance resides. |
| DBInstanceName | String | Yes | pxc- \*\*\*\*\*\*\*\*\*\*\ *\*\*\* | The name of the PolarDB-X instance. |

| BackupType | String | No | 0 | The backup type. Valid values: 0 (fast backup). |
|---|---|---|---|---|

**Response elements**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | \*\*\*\*\* | The response message. Returns success if the request succeeds, or an error code if it fails. |
| RequestId | String | 9B2F3840-5C98-475C- B269-2D5C3A31797C | The request ID. |
| Success | Boolean | true | Indicates whether the request succeeded. |
| Data | Array of Account |   |   |
| BackupSetId | Long | 627833 | The ID of the backup set. |

**Examples**

Sample request

```
http(s)://[Endpoint]/?Action=CreateBackup &RegionId=cn-hangzhou &DBInstanceName=pxc-************** &BackupType=0 &<Common request parameters>
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <CreateBackupResponse>
    <Message>*****</Message>
    <RequestId>9B2F3840-5C98-475C-B269-2D5C3A31797C</RequestId>
    <Success>true</Success>
    <Data>
        <BackupSetId>627833</BackupSetId>
    </Data>
</CreateBackupResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "Message" : "*****",
  "RequestId" : "9B2F3840-5C98-475C-B269-2D5C3A31797C",
  "Success" : true,
  "Data" : [ {
    "BackupSetId" : 627833
  } ]
```

`}`

#### DescribeBackupPolicy

Queries the backup policy of a PolarDB-X instance.

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackup Policy | The operation that you want to perform. Set the value to DescribeBackupPolicy. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. |
| DBInstanceNam e | String | Yes | pxc-******** | The name of the instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | success | The message that is returned. If the request is successful, "success" is returned. If the request fails, an error code is returned. |
| RequestId | String | B87E2AB3-B7C9- 4394-9160- 7F639F732031 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request is successful. |

| Data | Array of Account |   | The returned data. |
|---|---|---|---|
| LogLocalReten tionSpace | Integer | 30 | The maximum percentage of storage space that can be consumed by binary log (binlog) files. |
| DBInstanceNa me | String | pxc-xxxxxx | The ID of the instance that was queried. |
| BackupWay | String | P | The backup method. Valid values: L: logical backup P: physical backup |
| BackupPeriod | String | 1001000 | The days on which the system backs up data in a week. The value must be a string of seven digits to specify that backup is performed on at least two days in each week. Each digit specifies whether the system performs backup for the instance on a day of the week. The digit 0 specifies that backup is not performed on the day and the digit 1 specifies that the system performs backup for the instance on the day. The first digit from the left side specifies whether the system performs backup for the instance on Monday. The second digit from the left side specifies whether the system performs backup for the instance on Tuesday. The third digit from the left side specifies whether the system performs backup for the instance on Wednesday. The fourth digit from the left side specifies whether the system performs backup for the instance on Thursday. The fifth digit from the left side specifies whether the system performs backup for the instance on Friday. The sixth digit from the left side specifies whether the system performs backup for the instance on Saturday. The seventh digit from the left side specifies whether the system performs backup for the instance on Sunday. |

| ForceCleanOn HighSpaceUsa ge | Integer | 1 | Indicates whether the system automatically deletes binlog files when the space usage of the instance exceeds 80% or the remaining space of the instance is less than 50 GB. Valid values: 0: The system does not automatically delete binlog files when the space usage of the instance exceeds 80% or the remaining space of the instance is less than 50 GB. 1: The system automatically deletes binlog files when the space usage of the instance exceeds 80% or the remaining space of the instance is less than 50 GB. |
|---|---|---|---|
| BackupType | String | 0 | The type of the backup. Valid values: 0: fast backup 1: consistent backup |
| LocalLogReten tion | Integer | 30 | The number of hours for which log backup files can be retained in the PolarDB-X instance. |
| RemoveLogRe tention | Integer | 7 | The number of days for which log backup files can be retained in the backup storage space that is provided by Alibaba Cloud. Valid values: 7 to 730. Default value: 7. |
| BackupPlanBe gin | String | 03:00Z | The point in time that the system starts to back up data. |
| BackupSetRet ention | Integer | 7 | The number of days for which the backup set is retained. |
| IsEnabled | Integer | 1 | Indicates whether the log backup feature is enabled. Valid values: 1: The log backup feature is enabled. 0: The log backup feature is disabled. |
| ColdDataBack upInterval | Integer | 30 | The number of days between backups for cold data. Valid values: 1 to 59. |
| ColdDataBack upRetention | Integer | 30 | The number of days for which backup files for cold data are retained. Valid values: 30 to 730. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeBackupPolicy &RegionId=cn-hangzhou &DBInstanceName=pxc-******** &Common request parameters
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <DescribeBackupPolicyResponse>
    <Message>success</Message>
    <RequestId>B87E2AB3-B7C9-4394-9160-7F639F732031</RequestId>
    <Success>true</Success>
    <Data>
        <LogLocalRetentionSpace>30</LogLocalRetentionSpace>
        <DBInstanceName>pxc-xxxxxx</DBInstanceName>
        <BackupWay>P</BackupWay>
        <BackupPeriod>1001000</BackupPeriod>
        <ForceCleanOnHighSpaceUsage>1</ForceCleanOnHighSpaceUsage>
        <BackupType>0</BackupType>
        <LocalLogRetention>30</LocalLogRetention>
        <RemoveLogRetention>7</RemoveLogRetention>
        <BackupPlanBegin>03:00Z</BackupPlanBegin>
        <BackupSetRetention>7</BackupSetRetention>
        <IsEnabled>1</IsEnabled>
        <ColdDataBackupInterval>30</ColdDataBackupInterval>
        <ColdDataBackupRetention>30</ColdDataBackupRetention>
    </Data>
</DescribeBackupPolicyResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "Message" : "success",
  "RequestId" : "B87E2AB3-B7C9-4394-9160-7F639F732031",
  "Success" : true,
  "Data" : [ {
    "LogLocalRetentionSpace" : 30,
    "DBInstanceName" : "pxc-xxxxxx",
    "BackupWay" : "P",
    "BackupPeriod" : "1001000",
    "ForceCleanOnHighSpaceUsage" : 1,
    "BackupType" : "0",
    "LocalLogRetention" : 30,
    "RemoveLogRetention" : 7,
    "BackupPlanBegin" : "03:00Z",
    "BackupSetRetention" : 7,
    "IsEnabled" : 1,
    "ColdDataBackupInterval" : 30,
    "ColdDataBackupRetention" : 30
  } ]
```

`}`

#### DescribeBackupSetList

Queries backup sets of a PolarDB-X instance.

**Debugging**

Alibaba Cloud provides OpenAPI Explorer to simplify API usage. OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackup SetList | The operation that you want to perform. Set the value to DescribeBackupSetList. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the PolarDB-X instance is deployed. |
| DBInstanceNam e | String | Yes | pxc-xxxxxx | The name of the PolarDB-X instance. |
| StartTime | Long | No | 1635707845000 | The start time of the backup. Unit: millisecond. |

| EndTime | Long | No | 1635707845000 | The end time of the backup. Unit: millisecond. |
|---|---|---|---|---|
| PageSize | Integer | No | 30 | The number of entries to return on each page. |
| PageNumber | Integer | No | 1 | The number of the page to return. Pages start from page 1. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | success | The message that is returned. If the request is successful, "success" is returned. If the request fails, an error code is returned. |
| RequestId | String | 1A6D328C-84B8- 40DC-BF49- 6C73984D7494 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request is successful. |
| Data | Array of BackupSet |   | The data that is returned. |
| EndTime | Long | 1635706960956 | The end time of the backup. |
| Status | Integer | 1 | The status of the backup set. 0: The system is backing up the data. 1: The backup is successful. 2: The backup failed. |
| BackupSetSize | Long | 88803195 | The size of the backup set. Unit: byte. |
| BackupSetId | Long | 111 | The ID of the backup set. |
| BackupType | Integer | 1 | The type of the backup. 0: fast backup 1: consistent backup |
| BeginTime | Long | 1635706960956 | The start time of the backup. |

| BackupModel | Integer | 0 | The backup method. 0: automatic backup 1: manual backup |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeBackupSetList &RegionId=cn-hangzhou &DBInstanceName=pxc-xxxxxx &StartTime=1635707845000 &EndTime=1635707845000 &PageSize=30 &PageNumber=1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <DescribeBackupSetListResponse>
    <Message>success</Message>
    <RequestId>1A6D328C-84B8-40DC-BF49-6C73984D7494</RequestId>
    <Success>true</Success>
    <Data>
        <EndTime>1635706960956</EndTime>
        <Status>1</Status>
        <BackupSetSize>88803195</BackupSetSize>
        <BackupSetId>111</BackupSetId>
        <BackupType>1</BackupType>
        <BeginTime>1635706960956</BeginTime>
        <BackupModel>0</BackupModel>
    </Data>
</DescribeBackupSetListResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "Message" : "success",
  "RequestId" : "1A6D328C-84B8-40DC-BF49-6C73984D7494",
  "Success" : true,
  "Data" : [ {
    "EndTime" : 1635706960956,
    "Status" : 1,
    "BackupSetSize" : 88803195,
    "BackupSetId" : 111,
    "BackupType" : 1,
    "BeginTime" : 1635706960956,
    "BackupModel" : 0
  } ]
```

`}`

#### UpdateBackupPolicy

Call the UpdateBackupPolicy operation to modify the backup policy for an instance.

**Debugging**

You can use OpenAPI Explorer to run this operation without calculating the signature. After you run the operation successfully, OpenAPI Explorer automatically generates SDK code samples.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateBackupP olicy | The operation that you want to perform. Set the value to UpdateBackupPolicy. |
| RegionId | String | Yes | cn-hangzhou | The region ID. |
| DBInstanceNam e | String | Yes | pxc-hzja****** | The instance name ID. |

| BackupPeriod | String | No | 1001000 | The days of the week on which the system performs backups. The value must be a 7-digit string, with at least two days selected. Each digit represents a day of the week, where 0 means no backup and 1 means backup enabled: The first digit: Monday The second digit: Tuesday The third digit: Wednesday The fourth digit: Thursday The fifth digit: Friday The sixth digit: Saturday The seventh digit: Sunday |
|---|---|---|---|---|
| BackupPlanBegi n | String | No | 03:00Z | The point in time when the system starts to back up data on the specified days of the week. The time is in UTC. |
| BackupSetReten tion | Integer | No | 30 | The retention period of the backup set. Unit: day. |
| BackupType | String | No | 0 | The backup type. Only 0 is supported, which indicates fast backup. |
| BackupWay | String | No | P | The backup method. Valid values: P: physical backup L: logical backup |
| ForceCleanOnHi ghSpaceUsage | Integer | No | 1 | Specifies whether to forcibly purges binlogs when the total space usage of the instance exceeds 80% or the remaining space is less than 50 GB. If enabled, the system purges binlogs starting from the earliest one until the total space usage drops below 80% and the remaining space exceeds 50 GB. Valid values: 1: yes 0: no |
| IsEnabled | Integer | No | 1 | Specifies whether to enable backup. The value is fixed to 1. |

| LocalLogRetenti on | Integer | No | 7 | The local retention period (hours) of log backups. Valid values: 0 to 168. A value of 0 indicates that logs are not retained. Default value: 7. |
|---|---|---|---|---|
| RemoveLogRete ntion | Integer | No | 7 | The remote retention period (days) of log backups. Valid values: 7 to 730. Default value: 7. |
| LogLocalRetenti onSpace | Integer | No | 30 | The maximum local space usage for logs. Valid values: 0 to 50. This is a cyclic space, that is, when binlog files occupy the specified percentage of storage space, the system purges the oldest binlogs until the storage usage falls below the specified threshold. Default value: 30. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | success | The returned message. The system returns success for a successful request and an error code for a failed request. |
| RequestId | String | FEA5DC20-6D8A- 5979-97AA- FC57546ADC20 | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. |
| Data | Array of Account |   | The details of the backup policy. |
| LogLocalReten tionSpace | Integer | 30 | The maximum local space usage for logs. Valid values: 0 to 50. This is a cyclic space. Default value: 30. |
| DBInstanceNa me | String | pxc-hzja****** | The instance name ID. |
| BackupWay | String | P | The backup method. Valid values: P: physical backup L: logical backup |

| BackupPeriod | String | 1001000 | The backup cycle. |
|---|---|---|---|
| ForceCleanOn HighSpaceUsa ge | Integer | 1 | Specifies whether to forcibly purge binlogs. |
| BackupType | String | 0 | The backup type. A value of 0 indicates fast backup. |
| LocalLogReten tion | Integer | 7 | The local retention period (hours) of log backups. Valid values: 0 to 168. A value of 0 indicates that logs are not retained. Default value: 7. |
| RemoveLogRe tention | Integer | 7 | The remote retention period (days) of log backups. Valid values: 7 to 730. Default value: 7. |
| BackupPlanBe gin | String | 03:00Z | The point in time when the system starts to back up data on the specified days of the week. The time is displayed in UTC. |
| BackupSetRet ention | Integer | 30 | The retention period of the backup set. Unit: day. |
| IsEnabled | Integer | 1 | Specifies whether to enable backup. The value is fixed to 1. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateBackupPolicy &RegionId=cn-hangzhou &DBInstanceName=pxc-hzja****** &BackupPeriod=1001000 &BackupPlanBegin=03:00Z &BackupSetRetention=30 &BackupType=0 &BackupWay=P &ForceCleanOnHighSpaceUsage=1 &IsEnabled=1 &LocalLogRetention=7 &RemoveLogRetention=7 &LogLocalRetentionSpace=30 &Common request parameters
```

Sample success responses `XML` format

|   | HTTP/1.1 200 OK Content-Type:application/xml <UpdateBackupPolicyResponse> <Message>success</Message> <RequestId>FEA5DC20-6D8A-5979-97AA-FC57546ADC20</RequestId> <Success>true</Success> <Data> <LogLocalRetentionSpace>30</LogLocalRetentionSpace> <DBInstanceName>pxc-hzja******</DBInstanceName> <BackupWay>P</BackupWay> <BackupPeriod>1001000</BackupPeriod> <ForceCleanOnHighSpaceUsage>1</ForceCleanOnHighSpaceUsage> <BackupType>0</BackupType> <LocalLogRetention>7</LocalLogRetention> <RemoveLogRetention>7</RemoveLogRetention> <BackupPlanBegin>03:00Z</BackupPlanBegin> <BackupSetRetention>30</BackupSetRetention> <IsEnabled>1</IsEnabled> </Data> </UpdateBackupPolicyResponse> |   |
|---|---|---|

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "Message" : "success",
  "RequestId" : "FEA5DC20-6D8A-5979-97AA-FC57546ADC20",
  "Success" : true,
  "Data" : [ {
    "LogLocalRetentionSpace" : 30,
    "DBInstanceName" : "pxc-hzja******",
    "BackupWay" : "P",
    "BackupPeriod" : "1001000",
    "ForceCleanOnHighSpaceUsage" : 1,
    "BackupType" : "0",
    "LocalLogRetention" : 7,
    "RemoveLogRetention" : 7,
    "BackupPlanBegin" : "03:00Z",
    "BackupSetRetention" : 30,
    "IsEnabled" : 1
  } ]
```

`}`

### Parameter management

#### 4.11.1. \ DescribeParameters

Queries the parameter settings of a PolarDB-X instance, including both the configured and actively running values for compute and storage nodes.

**Debugging**

OpenAPI Explorer automatically calculates the signature value. Call this operation in OpenAPI Explorer to generate sample code for different SDKs.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeParamet ers | The operation to perform. Set the value to DescribeParam eters. |
| RegionId | String | Yes | cn-hangzhou | The region of the instance. |
| DBInstanceId | String | Yes | pxc-\*\*\*\*\*\*\*\* | The ID of the instance. |
| ParamLevel | String | No | compute | The node type whose parameters to query. Valid values: compute: data nodes storage: storage nodes |

**Response elements**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6BA32080EEA | The request ID. |
| Data | Object | — | The parameter details. |
| Data.EngineVersion | String | 2.0 | The engine version. Default value: 2.0. |
| Data.Engine | String | polarx | The engine type. Default value: polarx. |
| Data.ConfigParameter s | Array of DBInstanceParameter | — | The parameter values as saved in the configuration. |
| Data.ConfigParameter s[].ParameterName | String | CONN POOL XPROTO _ _ _ STORAGE DB PORT _ _ | The parameter name. |
| Data.ConfigParameter s[].ParameterValue | String | -1 | The parameter value. |

| Data.ConfigParameter s[].ParameterDescripti on | String | Specifies whether to turn on the proprietary protocol for storage nodes.(-1: turn off; 0: turn on) | The parameter description. |
|---|---|---|---|
| Data.RunningParamet ers | Array of DBInstanceParameter | — | The parameter values currently in effect on the instance. |
| Data.RunningParamet ers[].ParameterName | String | CONN POOL XPROTO _ _ _ STORAGE DB PORT _ _ | The parameter name. |
| Data.RunningParamet ers[].ParameterValue | String | -1 | The parameter value. |
| Data.RunningParamet ers[].ParameterDescri ption | String | Specifies whether to turn on the proprietary protocol for storage nodes.(-1: turn off; 0: turn on) | The parameter description. |

**Examples**

**Sample request**

```
http(s)://[Endpoint]/?Action=DescribeParameters &RegionId=cn-hangzhou &DBInstanceId=pxc-******** &ParamLevel=compute &<Common request parameters>
```

**Sample success response**

`XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <DescribeParametersResponse>
    <RequestId>6BA32080EEA</RequestId>
    <Data>
        <EngineVersion>2.0</EngineVersion>
        <Engine>polarx</Engine>
        <ConfigParameters>
            <ParameterDescription>Specifies whether to turn on the proprietary protocol
for storage nodes.(-1: turn off; 0: turn on)</ParameterDescription>
            <ParameterName>CONN_POOL_XPROTO_STORAGE_DB_PORT</ParameterName>
            <ParameterValue>-1</ParameterValue>
        </ConfigParameters>
        <RunningParameters>
            <ParameterDescription>Specifies whether to turn on the proprietary protocol
for storage nodes.(-1: turn off; 0: turn on)</ParameterDescription>
            <ParameterName>CONN_POOL_XPROTO_STORAGE_DB_PORT</ParameterName>
            <ParameterValue>-1</ParameterValue>
        </RunningParameters>
    </Data>
</DescribeParametersResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "RequestId" : "6BA32080EEA",
  "Data" : {
    "EngineVersion" : "2.0",
    "Engine" : "polarx",
    "ConfigParameters" : [ {
      "ParameterDescription" : "Specifies whether to turn on the proprietary protocol f
or storage nodes.(-1: turn off; 0: turn on)",
      "ParameterName" : "CONN_POOL_XPROTO_STORAGE_DB_PORT",
      "ParameterValue" : "-1"
    } ],
    "RunningParameters" : [ {
      "ParameterDescription" : "Specifies whether to turn on the proprietary protocol f
or storage nodes.(-1: turn off; 0: turn on)",
      "ParameterName" : "CONN_POOL_XPROTO_STORAGE_DB_PORT",
      "ParameterValue" : "-1"
    } ]
```

`}` `}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|

| 404 | InvalidDBInstance.Not Found | The specified DB instance does not exist. | The specified instance does not exist. |
|---|---|---|---|

For a list of error codes, visit the API Error Center.

#### ModifyParameter

Call the ModifyParameter operation to modify instance parameters for both the compute layer and the storage layer.

**Debugging**

You can use OpenAPI Explorer to run this operation directly, eliminating the need to calculate signatures. After successful execution, OpenAPI Explorer automatically generates SDK code samples.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyParamete r | The operation that you want to perform. Set the value to ModifyParameter. |
| RegionId | String | Yes | cn-hangzhou | The region ID. |
| DBInstanceId | String | Yes | pxc-hzjasd**** | The instance ID. |
| ParamLevel | String | No | compute | The parameter type: compute: The parameter is used to describe data nodes. storage: The parameter is used to describe storage nodes. |
| Parameters | String | Yes | {"CONN POOL B _ _ LOCK TIMEOUT" _ :"6000"} | The parameter must be a string in JSON format. MapKey indicates the parameter name, and MapValue indicates the parameter value. |
| ClientToken | String | No | FEA5DC20- 6D8A-5979- 97AA- FC57546ADC20 | The client token that identifies the request. Specify any unique string. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | FEA5DC20-6D8A- 5979-97AA- FC57546ADC20 | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyParameter &RegionId=cn-hangzhou &DBInstanceId=pxc-hzjasd**** &ParamLevel=compute &Parameters={"CONN_POOL_BLOCK_TIMEOUT":"6000"} &ClientToken=FEA5DC20-6D8A-5979-97AA-FC57546ADC20 &Common request parameters
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <ModifyParameterResponse>
    <RequestId>FEA5DC20-6D8A-5979-97AA-FC57546ADC20</RequestId>
</ModifyParameterResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "RequestId" : "FEA5DC20-6D8A-5979-97AA-FC57546ADC20"
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidDBInstance. NotFound | The specified DB instance does not exist. | The database instance does not exist. |

For a list of error codes, visit the API Error Center.

### SSL encryption

#### DescribeDBInstanceSSL

Call the DescribeDBInstanceSSL operation to view SSL information.

**Debugging**

You can use OpenAPI Explorer to run this operation. OpenAPI Explorer automatically calculates the signature and generates SDK code examples after the operation succeeds.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInsta nceSSL | The operation that you want to perform. Set the value to DescribeDBInstanceSSL. |
| DBInstanceNam e | String | No | pxc-********* | The instance ID. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C458B1E8-1683- 3645-B154- 6BA32080EEA | The request ID. |
| Data | Object |   | The data structure. |
| SSLEnabled | Boolean | false | Indicates whether SSL is enabled for the instance: true: SSL is enabled. false: SSL is disabled. |
| SSLExpiredTim e | String | 2022-11- 04T09:39:07Z | The time when the certificate expires. |

| CertCommonN ame | String | pxc- sddddddcym7g7w* ***.polarx.singapor e.rds.aliyuncs.com | The domain name bound to the certificate. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeDBInstanceSSL &DBInstanceName=pxc-********* &RegionId=cn-hangzhou &Common request parameters
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <DescribeDBInstanceSSLResponse>
    <RequestId>C458B1E8-1683-3645-B154-6BA32080EEA</RequestId>
    <Data>
        <SSLEnabled>false</SSLEnabled>
        <SSLExpiredTime>2022-11-04T09:39:07Z</SSLExpiredTime>
        <CertCommonName>pxc-
sddddddcym7g7w****.polarx.singapore.rds.aliyuncs.com</CertCommonName>
    </Data>
</DescribeDBInstanceSSLResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "RequestId" : "C458B1E8-1683-3645-B154-6BA32080EEA",
  "Data" : {
    "SSLEnabled" : false,
    "SSLExpiredTime" : "2022-11-04T09:39:07Z",
    "CertCommonName" : "pxc-sddddddcym7g7w****.polarx.singapore.rds.aliyuncs.com"
```

`}` `}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|

| 400 | IdempotentParame terMismatch | The request uses the same client token as a previous, but non-identical request. Do not reuse a client token with different requests, unless the requests are identical. | The request uses the same client token as a previous, but non-identical request. Do not reuse a client token with different requests, unless the requests are identical. |
|---|---|---|---|
| 400 | InvalidAction | The specified Action is invalid. | The specified Action is invalid. |
| 404 | InvalidDBInstance. NotFound | The specified DB instance does not exist. | The database instance does not exist. |
| 500 | InternalError | An error occurred while processing your request. | The operation is temporarily unavailable. |

For a list of error codes, visit the API Error Center.

#### UpdateDBInstanceSSL

Call the UpdateDBInstanceSSL operation to update the SSL configuration of an instance.

**Debugging**

You can use OpenAPI Explorer to run this operation. OpenAPI Explorer automatically calculates the signature and generates SDK code samples after the operation succeeds.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateDBInstan ceSSL | The operation that you want to perform. Set the value to UpdateDBInstanceSSL. |
| EnableSSL | Boolean | Yes | true | Specifies whether to enable SSL. A value of true indicates that SSL is enabled. A value of false indicates that SSL is disabled. |
| CertCommonNa me | String | No | pxc- hzrqjarxdo****.p olarx.rds.aliyunc s.com | The domain name bound to the certificate. |
| DBInstanceNam e | String | Yes | pxc-hzjasd**** | The instance name. |
| RegionId | String | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | FEA5DC20-6D8A- 5979-97AA- FC57546ADC20 | The request ID. |
| Data | Object |   | The response data. |
| TaskId | Long | 2209883 | The backend task ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateDBInstanceSSL &EnableSSL=true &CertCommonName=pxc-hzrqjarxdo****.polarx.rds.aliyuncs.com &DBInstanceName=pxc-hzjasd**** &RegionId=cn-hangzhou &Common request parameters
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <UpdateDBInstanceSSLResponse>
    <RequestId>FEA5DC20-6D8A-5979-97AA-FC57546ADC20</RequestId>
    <Data>
        <TaskId>2209883</TaskId>
    </Data>
</UpdateDBInstanceSSLResponse>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "RequestId" : "FEA5DC20-6D8A-5979-97AA-FC57546ADC20",
  "Data" : {
    "TaskId" : 2209883
```

`}` `}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidDBInstance. NotFound | The specified DB instance does not exist. | The database instance does not exist. |

For a list of error codes, visit the API Error Center.

### Monitoring

#### DescribeInstanceDbPerformance

Queries the detailed information about database monitoring.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeInstanc eDbPerformance | The operation that you want to perform. Set the value to DescribeInstanceDbPerformance. |
| DbInstanceNam e | String | Yes | pxc- **************** | The ID of the instance |
| DbName | String | Yes | db2 | The name of the database. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. |
| Keys | String | No | qps,active,runni ng count _ | The metrics that you want to query. Valid values: lqps: queries per second (QPS) active: the number of connections running count: the number of _ active threads Note You can specify multiple metrics at the same time. Separate multiple metrics with commas (,). |
| StartTime | String | No | 2020-08-19 11:02:50 | The beginning of the time range to query. Specify the time in the time zone of the queried database in the yyyy-mm-dd hh:mm:ss format. |

| EndTime | String | No | 2020-08-19 11:03:50 | The end of the time range to query. Specify the time in the time zone of the queried database in the yyyy- mm-dd hh:mm:ss format. Note The end of the time range must be later than the beginning of the time range. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Struct |   | The monitoring data. |
| PerformanceIt ems | Array of PerformanceIt em |   | The list of metrics. |
| Measurement | String | lqps,active,running count _ | The monitoring metrics. Valid values: lqps: queries per second (QPS). active: the number of connections. running count: the number of active _ threads. |
| MetricName | String | lqps | The details of a single monitoring metric, such as lqps. |
| Points | Array of Point |   | The monitoring data of the metric. Note If no monitoring data is collected within the query time range, the value of this parameter is empty. |
| Timestamp | Long | 1597179542 | The point in time at which the monitoring data is collected within the query time range. The value is a UNIX timestamp. Unit: seconds. |
| Value | String | 1 | The value of the metric. |
| Message | String | **** | The returned message. |
| RequestId | String | 5C07B700-A7CC- 4F81-8861- 86F840G7YH6U | The request ID. |

| Success | Boolean | true | Indicates whether the request is successful. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeInstanceDbPerformance &DbInstanceName=pxc-**************** &DbName=db2 &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Message>****</Message> <RequestId>5C07B700-A7CC-4F81-8861-86F840G7YH6U</RequestId> <Data>
    <PerformanceItems>
        <Measurement>lqps,active,running_count</Measurement>
        <MetricName>lqps</MetricName>
        <Points>
            <Value>1</Value>
            <Timestamp>1597179542</Timestamp>
        </Points>
    </PerformanceItems>
</Data> <Success>true</Success>
```

`JSON` format

```json
{"Message":"****","RequestId":"5C07B700-A7CC-4F81-8861-86F840G7YH6U","Data":{"Performan ceItems":[{"Measurement":"lqps,active,running_count","MetricName":"lqps","Points":[{"Va lue":"1","Timestamp":"1597179542"}]}]},"Success":"true"}
```

#### DescribeInstanceStoragePerformance

Queries the monitoring information of a storage node.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeInstanc eStoragePerfor mance | The operation that you want to perform. Set the value to DescribeInstanceStoragePerformanc e. |

| DbInstanceNam e | String | Yes | pxc- hzr2ak5ll5**** | The name of the instance. |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. |
| StorageInstanceI d | String | No | pxc-xdb-s- pxchzr2ak5ll529 yz**** | The ID of the storage node. |
| Keys | String | No | MySQL MemCpu _ Usage,MySQL N _ etworkTraffic | The metrics that you want to view. |
| StartTime | String | No | 2020-08-12 05:16:35 | The beginning of the time range to query. Specify the time in the time zone of the queried instance in the yyyy-mm-dd hh:mm:ss format. |
| EndTime | String | No | 2020-08-12 11:16:35 | The end of the time range to query. Specify the time in the time zone of the queried instance in the yyyy- mm-dd hh:mm:ss format. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Struct |   | The monitoring data. |
| PerformanceIt ems | Array of PerformanceIt em |   | The list of metrics. |
| Measurement | String | com insert _ | The metric. |
| MetricName | String | com insert _ | The details of a single monitoring metric, such as com insert. _ |
| Points | Array of Point |   | The monitoring data of the metric. |
| Timestamp | Long | 1597180560000 | The point in time at which the monitoring data is collected within the query time range. The value is a UNIX timestamp. Unit: seconds. |
| Value | String | 0.1 | The value of the metric. |
| Message | String | **** | The returned message. |

| RequestId | String | 39518C53-F3C3- 424B-8108- 27CCF9DR54TH | The request ID. |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request is successful. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeInstanceStoragePerformance &DbInstanceName= pxc-hzr2ak5ll5**** &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Message>****</Message> <RequestId>39518C53-F3C3-424B-8108-27CCF9DR54TH</RequestId> <Data>
    <PerformanceItems>
        <Measurement>com_insert</Measurement>
        <MetricName>com_insert</MetricName>
        <Points>
            <Value>0.1</Value>
            <Timestamp>1597180560000</Timestamp>
        </Points>
    </PerformanceItems>
</Data> <Success>true</Success>
```

`JSON` format

```json
{"Message":"****","RequestId":"39518C53-F3C3-424B-8108-27CCF9DR54TH","Data":{"Performan ceItems":[{"Measurement":"com_insert","MetricName":"com_insert","Points": [{"Value":"0.1","Timestamp":"1597180560000"}]}]},"Success":"true"}
```

#### DescribeInstancePerformance

Queries the monitoring information of an instance.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | DescribeInstanc ePerformance | The operation that you want to perform. Set the value to DescribeInstancePerformance. |
|---|---|---|---|---|
| DbInstanceNam e | String | Yes | pxc- hzr2ak5ll5**** | The ID of the instance |
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. |
| NodeId | String | No | pxc-i- xbmb73**** | The ID of the node on the instance. |
| Keys | String | No | cpu,old | The metrics that you want to query. Valid values: lqps: logical queries per second (QPS) lrt: logical response time (RT) con: the number of front-end connections active: the number of active threads netin: inbound traffic netout: outbound traffic cpu: CPU utilization old: memory utilization |
| StartTime | String | No | 2020-08-12 04:59:02 | The beginning of the time range to query. Specify the time in the time zone of the queried instance in the yyyy-mm-dd hh:mm:ss format. |
| EndTime | String | No | 2020-08-12 10:59:02 | The end of the time range to query. Specify the time in the time zone of the queried instance in the yyyy- mm-dd hh:mm:ss format. Note The end of the time range must be later than the beginning of the time range. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Struct |   | The monitoring data. |
| PerformanceIt ems | Array of PerformanceIt em |   | Metrics and monitoring data. |

| Measurement | String | cpu,old | The list of metrics. Valid values: lqps: logical queries per second (QPS) lrt: logical response time (RT) con: the number of front-end connections active: the number of active threads netin: inbound traffic netout: outbound traffic cpu: CPU utilization old: memory utilization |
|---|---|---|---|
| MetricName | String | cpu | The details of a single monitoring metric. |
| Points | Array of Point |   | The monitoring data of the metric. |
| Timestamp | Long | 1597201474 | The point in time at which the monitoring data is collected within the query time range. The value is a UNIX timestamp. Unit: seconds. |
| Value | String | 1 | The value of the metric. |
| Message | String | **** | The returned message. |
| RequestId | String | 88DC5709-8BEC- 4D17-A6D5- 4DACA9DF45TP | The request ID. |
| Success | Boolean | true | Indicates whether the request is successful. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeInstancePerformance &DbInstanceName=pxc-hzr2ak5ll5**** &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Message>****</Message> <RequestId>88DC5709-8BEC-4D17-A6D5-4DACA9DF45TP</RequestId> <Data>
    <PerformanceItems>
        <Measurement>cpu,old</Measurement>
        <MetricName>cpu</MetricName>
        <Points>
            <Value>1</Value>
            <Timestamp>1597201474</Timestamp>
        </Points>
    </PerformanceItems>
</Data> <Success>true</Success>
```

`JSON` format

```json
{"Message":"****","RequestId":"88DC5709-8BEC-4D17-A6D5-4DACA9DF45TP","Data":{"Performan ceItems":[{"Measurement":"cpu,old","MetricName":"cpu","Points": [{"Value":"1","Timestamp":"1597201474"}]}]},"Success":"true"}
```

#### DescribeMetricsPerf

Queries the monitoring information of computing resources, storage resources, and log resources.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMetrics Perf | The operation that you want to perform. Set the value to DescribeMetricsPerf. |
| DBInstanceNam e | String | Yes | pxc- unrwuyttjx**** | The name of the instance. |
| EndTime | String | Yes | 2022-08- 22T08:00:57Z | The end of the time range to query. Specify the time in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |
| InstanceName | String | Yes | pxc- unrwuyttjx**** | The name of the instance. |
| IsMultipleIns | Boolean | No | false | Indicates whether multiple instances are monitored. Valid values: true and false. |

| MetricsGroupKe y | String | No | Connections | The group of performance metrics that you want to query. You can specify only one group. |
|---|---|---|---|---|
| MetricsKeys | String | No | avg(node slow r _ _ equest count),a _ vg(node physica _ l slow request c _ _ _ ount),avg(node _ network in byte _ _ s),avg(node net _ work out bytes), _ _ avg(jvmstats yg _ c collector time _ _ ),avg(jvmstats f _ gc collector tim _ _ e) | The performance metrics that you want to query. Separate multiple metrics with commas (,). |
| MetricsMeasure ment | String | Yes | polarx | The name of the monitored service. |
| RegionId | String | Yes | cn-wulan- env213-d01 | The region ID of the instance. |
| StartTime | String | Yes | 2022-08- 22T02:00:57Z | The beginning of the time range to query. Specify the time in the yyyy- MM-ddTHH:mmZ format. The time must be in UTC. |
| HostId | String | No | 10000 | The ID of the host. You must specify this parameter or the InstanceName parameter. |
| DbRole | String | No | 0 | The role of the node. Valid values: 0: master 1: slave 18: standby |
| InsLogicId | String | No | pxc-c-xxxxxxx | The names of physical nodes. Separate multiple names with commas (,). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Struct |   | The data returned. |
| Code | String | 200 | The returned status code. |
| EndTime | String | 2022-08- 24T06:57:37Z | The end of the query time range. |

| HostId | String | 1000 | The ID of the server. |
|---|---|---|---|
| HostMetricIte ms | Array of HostMetricIte m |   | The performance metrics of the server. |
| InsId | String | pxc- hzrqdp9iwn**** | The ID of the instance |
| InsLogicId | String | pxc-c-xxxxxxx | The logical ID of the instance. |
| InsName | String | pxc- hzr1m03gei**** | The name of the instance. |
| MetricsGroupK ey | String | Connections | The group of performance metrics that you query. |
| MetricsKey | String | avg(node slow req _ _ uest count),avg(no _ de physical slow r _ _ _ equest count),avg( _ node network in b _ _ _ ytes),avg(node net _ work out bytes),av _ _ g(jvmstats ygc coll _ _ ector time),avg(jv _ mstats fgc collect _ _ or time) _ | The performance metric that you query. Multiple values are separated with commas (,). |
| MetricsValues | Array of MetricValue |   | The performance metrics that are returned. |
| MetricsData | String | 24 | The value of the metric. |
| MetricsTimest amp | String | 1568620311000 | The timestamp of the metric. |
| HttpStatusCod e | Integer | 200 | The status code of the request. A value of 200 indicates that the request is successful. |
| InstanceEngin e | String | polarx | The type of the instance. |
| InstanceID | String | pxc-unrwuyttjx**** | The ID of the instance |
| InstanceNode Role | String | master | The role of the node. Valid values: master and slave. |

| Message | String | success | The returned message. |
|---|---|---|---|
| StartTime | String | 2022-08- 24T05:57:37Z | The beginning of the query time range. The time is in the yyyy-MM-ddTHH:mmZ format. The time is in UTC. |
| Success | Boolean | true | Indicates whether the request is successful. |
| UserID | String | 26842 | The user ID. |
| RequestId | String | BFC01449-C5D2- 4457-8909- 8285B9E1710 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMetricsPerf &DBInstanceName=pxc-unrwuyttjx**** &EndTime=2022-08-22T08:00:57Z &InstanceName=pxc-unrwuyttjx**** &IsMultipleIns=false &MetricsGroupKey=Connections &MetricsKeys=avg(node_slow_request_count),avg(node_physical_slow_request_count),avg(node_ twork_in_bytes),avg(node_network_out_bytes),avg(jvmstats_ygc_collector_time),avg(jvmstats gc_collector_time) &MetricsMeasurement=polarx &RegionId=cn-wulan-env213-d01 &StartTime=2022-08-22T02:00:57Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>BFC01449-C5D2-4457-8909-8285B9E1710</RequestId> <Data>
    <EndTime>2022-08-24T06:57:37Z</EndTime>
    <Message>success</Message>
    <InstanceID>pxc-unrwuyttjx****</InstanceID>
    <UserID>26842</UserID>
    <InstanceNodeRole>master</InstanceNodeRole>
    <StartTime>2022-08-24T05:57:37Z</StartTime>
    <HttpStatusCode>200</HttpStatusCode>
    <InstanceEngine>polarx</InstanceEngine>
    <HostId>1000</HostId>
    <Code>200</Code>
    <Success>true</Success>
    <HostMetricItems>
        <InsId> pxc-hzrqdp9iwn****</InsId>
<MetricsKey>avg(node_slow_request_count),avg(node_physical_slow_request_count),avg(node_n work_in_bytes),avg(node_network_out_bytes),avg(jvmstats_ygc_collector_time),avg(jvmstats_ c_collector_time)</MetricsKey>
        <MetricsGroupKey>Connections</MetricsGroupKey>
        <InsLogicId>pxc-c-xxxxxxx</InsLogicId>
        <InsName>pxc-hzr1m03gei****</InsName>
        <MetricsValues>
            <MetricsData>24</MetricsData>
            <MetricsTimestamp>1568620311000</MetricsTimestamp>
        </MetricsValues>
    </HostMetricItems>
</Data>
```

`JSON` format

```json
{"RequestId":"BFC01449-C5D2-4457-8909-8285B9E1710","Data":{"EndTime":"2022-08-24T06:57: 37Z","Message":"success","InstanceID":"pxcunrwuyttjx****","UserID":"26842","InstanceNodeRole":"master","StartTime":"2022-08-24T05 :57:37Z","HttpStatusCode":"200","InstanceEngine":"polarx","HostId":"1000","Code":"200","S cess":"true","HostMetricItems":[{"InsId":" pxchzrqdp9iwn****","MetricsKey":"avg(node_slow_request_count),avg(node_physical_slow_request ount),avg(node_network_in_bytes),avg(node_network_out_bytes),avg(jvmstats_ygc_collector_t e),avg(jvmstats_fgc_collector_time)","MetricsGroupKey":"Connections","InsLogicId":"pxcc-xxxxxxx","InsName":"pxc-hzr1m03gei****","MetricsValues": [{"MetricsData":"24","MetricsTimestamp":"1568620311000"}]}]}}
```

### DAS

#### GetSlowRequestRecords

Queries slow request records.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | GetSlowRequestRecords | The operation that you want to perform. Set the value to GetSlowRequestRecords . |
| InstanceId | Strin g | Query | No | pxc-unrs3lrchgzfid | The instance ID. |
| NodeId | Strin g | Query | No | pxc-unrs3lrchgzfiddawj- cn#pxc-i-qaibfzqlqo | The node ID. |
| DbName | Strin g | Query | No | testDB | The name of the database. |
| Start | Strin g | Query | No | 1749431640000 | The beginning of the time range to query. |
| End | Strin g | Query | No | 1749435240000 | The end of the time range to query. |
| PageNo | Strin g | Query | No | 1 | The page number. |
| PageSize | Strin g | Query | No | 30 | The number of entries per page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | Successful | The returned message. If the request was successful, Successful is returned. If the request failed, an error message that contains information such as an error code is returned. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B6D17591-B48B- 4D31-9CD6- 9B9796B2**** | The request ID. |
| Synchro | String | true | The reserved parameter. |
| Data | String | { "total":1, "pageNo":1, "pageSize":30, "list":[ { "schema":"***", "rows examined":- _ 1, "sql id":" 1676873 _ _ 441%7C46", "max rows examin _ _ ed":-1, "count":1, "max query time": _ _ 1.494, "sql":"****", "lock time":0.0, _ "rows sent":0, _ "database":"***", "host":"10.***", "max lock time":0. _ _ 0, "user":"***", "max rows sent":0 _ _ , "query time":1.494 _ , "timestamp":1752 227282000 } ] } | "schema": the name of the database. "rows examined": the total number of _ scanned rows. "sql id": the SQL ID of the instance. _ "max rows examined": the maximum _ _ number of scanned rows. "count": the total number of executions. "max query time": the maximum SQL _ _ response time, in seconds. "sql": the SQL statement. "lock time": the lock wait time. _ "rows sent": the total number of _ returned rows. "database": the name of the database. "host": the IP address of the client. "max lock time": the longest lock wait _ _ time. "user": the username. "max rows sent": the maximum _ _ number of returned rows. "query time": the time used to execute _ the SQL statement, in seconds. "timestamp": the execution time. |
| Code | String | 200 | The HTTP status code. |
| Success | String | true | Indicates whether the request was successful. Valid values: true false |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetSlowRequestRecords &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "Message":"Successful",
 "RequestId":"B6D17591-B48B-4D31-9CD6-9B9796B2****",
 "Synchro":"true",
 "Data":"{\t\t\"total\":1,\t\t\"pageNo\":1,\t\t\"pageSize\":30,\t\t\"list\":[\t\t\t{\t\
t\t\t\"schema\":\"***\",\t\t\t\t\"rows_examined\":- 1,\t\t\t\t\"sql_id\":\"_1676873441%7C46\",\t\t\t\t\"max_rows_examined\":- 1,\t\t\t\t\"count\":1,\t\t\t\t\"max_query_time\":1.494,\t\t\t\t\"sql\":\"****\",\t\t\t\t\ ock_time\":0.0,\t\t\t\t\"rows_sent\":0,\t\t\t\t\"database\":\"***\",\t\t\t\t\"host\":\"10
**\",\t\t\t\t\"max_lock_time\":0.0,\t\t\t\t\"user\":\"***\",\t\t\t\t\"max_rows_sent\":0,\
t\t\t\"query_time\":1.494,\t\t\t\t\"timestamp\":1752227282000\t\t\t}\t]}",
 "Code":"200",
 "Success":"true"
```

`}` `XML` format

```xml
<Message>Successful</Message> <RequestId>B6D17591-B48B-4D31-9CD6-9B9796B2****</RequestId> <Synchro>true</Synchro> <Data>{
  &quot;total&quot;:1,
  &quot;pageNo&quot;:1,
  &quot;pageSize&quot;:30,
  &quot;list&quot;:[
```

`{`

```
    &quot;schema&quot;:&quot;***&quot;,
    &quot;rows_examined&quot;:-1,
    &quot;sql_id&quot;:&quot;_1676873441%7C46&quot;,
    &quot;max_rows_examined&quot;:-1,
    &quot;count&quot;:1,
    &quot;max_query_time&quot;:1.494,
    &quot;sql&quot;:&quot;****&quot;,
    &quot;lock_time&quot;:0.0,
    &quot;rows_sent&quot;:0,
    &quot;database&quot;:&quot;***&quot;,
    &quot;host&quot;:&quot;10.***&quot;,
    &quot;max_lock_time&quot;:0.0,
    &quot;user&quot;:&quot;***&quot;,
    &quot;max_rows_sent&quot;:0,
    &quot;query_time&quot;:1.494,
    &quot;timestamp&quot;:1752227282000
```

`}` `]`

```xml
}</Data>
 <Code>200</Code>
 <Success>true</Success>
```

ppendixes

## Appendixes

### STS overview

#### What is STS?

Security Token Service (STS) allows you to manage temporary credentials to your Apsara Stack resources. Resource Access Management (RAM) provides RAM users and RAM roles. A RAM role does not have permanent identity credentials. A RAM role can be assumed to access Apsara Stack resources by using an issued STS token. When the STS token is issued, you can specify a validity period and access permissions for the STS token.

**Use a RAM user to obtain an STS token**

An authorized RAM user can use an AccessKey pair to call the AssumeRole operation. This way, the RAM user can obtain an STS token of a RAM role and can use the STS token to access Apsara Stack resources.

**Benefits**

STS tokens help reduce the risks of AccessKey pair leaks. An AccessKey pair is a long-term credential for a RAM user. STS tokens are temporary credentials. You can specify the validity period for STS tokens. After STS tokens expire, they become invalid. Therefore, you do not need to rotate the STS tokens on a regular basis. You can attach custom policies to STS tokens for flexible and fine-grained authorization.

#### AssumeRole

Obtains a Security Token Service (STS) token that is used by a RAM user to assume a RAM role. In this example, an Apsara Stack tenant account is used as the trusted entity of the RAM role.

**Request parameters**

| Parameter | Type | Requ ired | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AssumeRole | The operation that you want to perform. Set the value to AssumeRole. |
| RoleArn | String | Yes | acs:ram::123456 789012****:role/ adminrole | The Apsara Stack Resource Name (ARN) of the RAM role. The trusted entity of the RAM role is an Apsara Stack tenant account. |

ppendixes

| Parameter | Type | Requ ired | Example | Description |
|---|---|---|---|---|
| RoleSessionNa me | String | Yes | alice | The name of the role session. Set this parameter based on your business requirements. In most cases, you can set this parameter to the identity of the user who calls the operation. For example, specify a username. In ActionTrail logs, you can distinguish the users who assume the same RAM role to perform operations based on the value of the RoleSessionName parameter. This way, you can perform user-specific auditing. The name must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores ( ). _ |
| Policy | String | No | {"Statement": [{"Action": ["*"],"Effect": "Allow","Resourc e": ["*"]}],"Version":" 1"} | The policy that specifies the permissions of the STS token. You can use this parameter to grant the STS token fewer permissions than the permissions granted to the RAM role. The policy must be 1 to 1,024 characters in length. |

**Responses**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6894B13B-6D71- 4EF5-88FA- F32781734A7F | The ID of the request. |
| Credentials | None | None | The access credentials. |
| AccessKeyId | String | STS.L4aBSCSJVMuK g5U1**** | The AccessKey ID. |
| AccessKeySecret | String | ****************************************** | The AccessKey secret. |
| SecurityToken | String | ******** | The security token. |

ppendixes

| Parameter | Type | Example | Description |
|---|---|---|---|
| Expiration | String | 2015-04- 09T11:52:19Z | The time when the STS token expires. |
| AssumedRoleUser | None | None | The temporary identity that you use to assume the RAM role. |
| Arn | String | acs:ram::12345678 9012****:role/admi nrole/alice | The ARN of the temporary identity that you use to assume the RAM role. |
| AssumedRoleId | String | 34458433936495** **:alice | The ID of the temporary identity that you use to assume the RAM role. |

**Examples**

**Add Project Object Model (POM) dependencies**

The Alibaba Cloud core library is required. Perform the following steps to add the Alibaba Cloud core library to POM:

```xml
    <dependency>
      <groupId>com.aliyun</groupId>
      <artifactId>aliyun-java-sdk-core</artifactId>
      <version>[4.4.9,5.0.0)</version>
    </dependency>
```

**Call an API operation to obtain the STS AccessKey 3-tuple.**

In the following sample code, the `Sts::AssumeRole::2015-04-01` operation is used to obtain the 3-tuple.

```java
package com.aliyuns.test; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; import org.apache.commons.lang3.StringUtils; public class STSAccessKeyDemo {
    public static void main(String[] args) {
//CreateandinitialieaDefaltAcsClientinstance
```

ppendixes

```java
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "
<yourAccessKeyID>", "<yourAccessKeySecret>");
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);
        clientConfig.setProtocolType(ProtocolType.HTTPS);
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        CommonRequest request = new CommonRequest();
        // Replace "sts.aliyuns.com" with the actual endpoint of STS. In most cases, th
e endpoint is in the following format: sts-vpc.${global:region}.${global:internet-domai n}.
        request.setSysDomain("sts.aliyuns.com");
        request.setSysProduct("Sts");
        request.setSysAction("AssumeRole");
        request.setSysVersion("2015-04-01");
        request.setSysMethod(MethodType.POST);
        request.setHttpContentType(FormatType.FORM);
        // Replace "<yourRoleSessionName>" with the alias that you specify for the curr
ent role session.
        request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
        // Replace "<yourRoleArn>" with the actual ARN that you obtained for the RAM ro
le in the preceding step.
        request.putQueryParameter("RoleArn", "<yourRoleArn>");
        try {
            CommonResponse response = client.getCommonResponse(request);
            String assumeRole = response.getData();
            if (StringUtils.isEmpty(assumeRole)) return;
            JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
            JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
            // Obtain the STS AccessKey 3-tuple.
            String stsAK = credentials.getString("AccessKeyId");
            String stsSK = credentials.getString("AccessKeySecret");
            String stsToken = credentials.getString("SecurityToken");
            System.out.println("stsAk: " + stsAK +"\nstsSk: " + stsSK + "\nstsToken: "
+ stsToken);
        } catch (ServerException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
        } catch (ClientException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
```

`}` `}` `}`

**Call examples**

In the following sample code, the `DescribeZones` operation in Elastic Compute Service (ECS) is used.

```java
package com.aliyuns.test; import com.aliyuncs.CommonRequest; importcomaliyuncsCommonResponse;
```

ppendixes

```java
import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class DescribeZonesDemo {
    public static void main(String[] args) {
        // Replace "<yourRegionID>" with the actual region ID.
        // Replace "<yourStsAccesskey>" and "<yourStsAccessKeySecret>" with the
AccessKey ID and secret in the 3-tuple that you obtained in the preceding step.
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "
<yourStsAccessKey>", "<yourStsAccessKeySecret>");
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);
        clientConfig.setProtocolType(ProtocolType.HTTPS);
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        CommonRequest request = new CommonRequest();
        request.setSysDomain("ecs.aliyuns.com");
        request.setSysProduct("Ecs");
        request.setSysAction("DescribeZones");
        request.setSysVersion("2014-05-26");
        request.setSysMethod(MethodType.POST);
        request.setHttpContentType(FormatType.FORM);
        //Replace "<yourRegionID>" with the actual region ID.
        request.putHeadParameter("x-acs-regionid", "<yourRegionID>");
        // Replace "<yourStsToken>" with the STS token in the 3-tuple that you obtained
in the preceding step.
        request.putQueryParameter("SecurityToken", "<yourStsToken>");
        // Optional. Specify the resource set ID.
        // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
        // Required. Specify the organization ID.
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

`}` `}` `}`

**Error codes**

ppendixes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | The parameter RoleArn is wrongly formed. | The error message returned because the ARN format of the RAM role is invalid. |
| 400 | InvalidParameter.Role Arn | The parameter RoleArn is wrongly formed. | The error message returned because the ARN format of the RAM role is invalid. |
| 400 | InvalidParameter.Role SessionName | The parameter RoleSessionName is wrongly formed. | The error message returned because the value of the RoleSessionName parameter is in an invalid format. The value must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores ( ). _ |
| 400 | InvalidParameter.Dura tionSeconds | The Min/Max value of DurationSeconds is 15min/1hr. | The error message returned because the value of the DurationSeconds parameter is invalid. The minimum value is 900, and the maximum value is equal to the value of the MaxSessionDuration parameter. |
| 400 | InvalidParameter.Polic yGrammar | The parameter Policy has not passed grammar check. | The error message returned because the syntax of the policy is invalid. |
| 400 | InvalidParameter.Polic ySize | The size of Policy must be smaller than 1024 bytes. | The error message returned because the length of the specified policy string exceeds the upper limit. The policy string can be up to 1,024 characters in length. |

ppendixes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | NoPermission | You are not authorized to do this action. You should be authorized by RAM. | The error message returned because the STS token does not have the required permissions. |
| 404 | EntityNotExist.Role | The specified Role not exists. | The error message returned because the specified RAM role does not exist. |
| 500 | InternalError | STS Server Internal Error happened. | The error message returned because an internal server error occurred. |
