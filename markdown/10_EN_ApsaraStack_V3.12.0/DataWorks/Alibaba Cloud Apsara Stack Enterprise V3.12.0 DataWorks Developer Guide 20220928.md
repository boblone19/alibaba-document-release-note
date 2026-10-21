---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 DataWorks Developer Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 174
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 DataWorks Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E5%A4%A7%E6%95%B0%E6%8D%AE/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20DataWorks%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 DataWorks Developer Guide 20220928

## Table of Contents

- 1 Overview
- 2 Terms
- 3 List of operations by function
- 4 Make API requests
  - 4.1 Java SDK
  - 4.2 HTTP API
    - 4.2.1 Endpoints
    - 4.2.2 Protocol
    - 4.2.3 Request method
    - 4.2.4 Encoding
    - 4.2.5 Signature method
    - 4.2.6 Response parameters
    - 4.2.7 API example
- 5 APIs for HTTP requests
  - 5.1 Create a node
  - 5.2 Update a node
  - 5.3 Update multiple nodes at a time
  - 5.4 Delete a node
  - 5.5 Query parent nodes
  - 5.6 Query child nodes
  - 5.7 Query the node code
  - 5.8 Query nodes
  - 5.9 Query a node by ID
  - 5.10 Obtain the total number of nodes
  - 5.11 Query node instances
  - 5.12 Query the operational logs of a node instance
  - 5.13 Query a node instance by ID
  - 5.14 Query the parent node instance by level
  - 5.15 Query the child node instances at a specified level
  - 5.16 Query the number of node instances in each status of an application
  - 5.17 Query the number of task instances in each status on a specified business date
  - 5.18 Query the number of node instances in each status for applications
  - 5.19 Rerun an instance
  - 5.20 Restore an instance
  - 5.21 Set the instance status to Success and trigger descendant instances
  - 5.22 Terminate a task
  - 5.23 Rerun a descendant instance
  - 5.24 Update the scheduling configurations of an instance
  - 5.25 Pause an instance
  - 5.26 Terminate multiple instances
  - 5.27 Rerun multiple instances
  - 5.28 Resume multiple tasks
  - 5.29 Pause multiple instances
  - 5.30 Set the status of multiple instances to Success
  - 5.31 Retrieve the total number of instances on the day
  - 5.32 Query business flow instances
  - 5.33 Retroactive execution
  - 5.34 Run a smoke test
  - 5.35 Execute an ad-hoc business flow
  - 5.36 Terminate a business flow
  - 5.37 Submit a resource package
  - 5.38 Query the submission status of a resource package
  - 5.39 Data structure
    - 5.39.1 NodeModifyDto
    - 5.39.2 TaskEntity
    - 5.39.3 DagEntity
    - 5.39.4 TaskStatus
    - 5.39.5 Dagstatus
    - 5.39.6 ProgramType
    - 5.39.7 CycleType
    - 5.39.8 DependencyType
- 6 Java SDK
  - 6.1 GetInstanceSummary
  - 6.2 AddResGroupGateWay
  - 6.3 CreateConnection
  - 6.4 CreateDag
  - 6.5 CreateDQCEntity
  - 6.6 CreateDQCFollower
  - 6.7 CreateDQCRule
  - 6.8 CreateManualDag
  - 6.9 CreateMetaSpiderJob
  - 6.10 CreateResGroup
  - 6.11 DeleteConnections
  - 6.12 DeleteDQCEntity
  - 6.13 DeleteDQCFollower
  - 6.14 DeleteDQCRule
  - 6.15 DeleteProjectResGroup
  - 6.16 DeleteResGroupGateWay
  - 6.17 GetDagDetail
  - 6.18 GetDataServiceApiDetail
  - 6.19 GetDataServiceAppDetail
  - 6.20 GetDefaultTenant
  - 6.21 GetDQCEntity
  - 6.22 GetDQCFollower
  - 6.23 GetDQCRule
  - 6.24 GetNodeDetail
  - 6.25 GetNodeUpdateStatus
  - 6.26 GetResGroupAk
  - 6.27 GetResGroupGatewayList
  - 6.28 GetResGroupList
  - 6.29 GetTableColumn
  - 6.30 GetTableList
  - 6.31 GetTaskLog
  - 6.32 GetUserInfo
  - 6.33 ListConnection
  - 6.34 ListDataServiceApps
  - 6.35 ListDataServiceAuthedApi
  - 6.36 ListPermission
  - 6.37 ListProjectModule
  - 6.38 ListProjectModules
  - 6.39 ListProject
  - 6.40 ListTenantModule
  - 6.41 ListUserPermission
  - 6.42 ModifyBusiness
  - 6.43 ModifyNode
  - 6.44 ModifySolution
  - 6.45 RerunTask
  - 6.46 ResumeTask
  - 6.47 SearchBusiness
  - 6.48 SearchManualDagNodeInstance
  - 6.49 SearchSolution
  - 6.50 SearchTasks
  - 6.51 TestConnectivity
  - 6.52 UpdateDQCFollower
  - 6.53 UpdateDQCRule
  - 6.54 UpdateResGroupGateWay
  - 6.55 CheckMetaTable
  - 6.56 GetMetaDB
  - 6.57 GetMetaTable
  - 6.58 GetMetaTableIntroWiki
  - 6.59 ListMetaColumnLineage
  - 6.60 ListMetaTableChangeLog
  - 6.61 ListMetaTableColumn
  - 6.62 ListMetaTableImpact
  - 6.63 ListMetaTableIntroWiki
  - 6.64 ListMetaTableLineage
  - 6.65 ListMetaTableOutput
  - 6.66 ListMetaTablePartition
  - 6.67 SearchMetaTables
  - 6.68 GetStorageAndCalcMetrics
  - 6.69 GetInstanceStatistic
  - 6.70 GetInstanceLog
  - 6.71 GetNodeCode
  - 6.72 QueryInstances
- 7 Obtain an AccessKey pair

## 1 Overview

DataWorks is a one-stop big data analytics and governance service released by Alibaba Cloud in 2009. It integrates all processes from data collection to data display and from data analytics to application running. It offers a wide range of features and services to help enterprises effectively build a data midend.

## 2 Terms

Workspace A workspace is the basic organizational object in DataWorks. It serves as the basic unit for you to manage tables, resources, user-defined functions (UDFs), nodes, and permissions. Node A node is a scheduling definition that is submitted and released on DataStudio or created by calling APIs. Business flow A business flow consists of a set of nodes with dependency between each other. Instance or task instance Before nodes can be run, they must be converted into task instances in the DataWorks scheduling system. by function

## 3 List of operations by function

Operations of the scheduling system Query the total number of nodes Query the parent node at a specified level Query the number of node instances in each status of an application Query the number of task instances in each status on a specified date Query the number of node instances in each status for applications Set the instance status to Success and trigger descendant instances Terminate a node Terminate multiple instances at a time Rerun multiple instances at a time Restore multiple nodes at a time Pause multiple instances at a time Query the total number of instances on the current day Query workflow instances Create a retroactive data generation task Run an ad-hoc workflow Terminate a workflow by function View the submission status of the resource package

## 4 Make API requests

DataWorks allows you to make API requests by using the Java SDK or the HTTP method. The Java SDK is newly released. You can use only the Java SDK to call API operations in the later versions of DataWorks. The HTTP method remains unchanged. No new API operations are added. In later versions, these API operations will be discontinued. We recommend that you use the Java SDK.

### 4.1 Java SDK

If you need to use a client to make an API request by using the Java SDK, you must specify the following parameters to initialize the client: popEndpoint, accessId, accessKey, popProduct, regionId, and popEndpointName. popEndpoint The endpoint for accessing the service. It consists of the prefix dataworks. followed by the domain name of Apsara Stack DataWorks. For example, if the DataStudio URL for Apsara Stack is http://ide.envxxx.yyyyy.com, the endpoint is dataworks. envxxx.yyyyy.com. If the actual endpoint does not follow the preceding rule, contact Alibaba Cloud technical support. accessId and accessKey The AccessKey ID and AccessKey secret of the Apsara Stack tenant account. popProduct The name of the service. Set the value to dataworks-private-cloud. regionId and popEndpointName regionId: the ID of the region where the service resides. Set the value to default. popEndpointName: the name of the endpoint. Set the value to default. Authorization You can use only an authorized Apsara Stack tenant account to make API requests by using the Java SDK. The whitelist mechanism is used for the access control of the DataWorks API. To authorize an Apsara Stack tenant account, add the account to the whitelist. If the account that you use to make API requests is not in the whitelist, the following error message appears.

```
com.aliyuncs.exceptions.ClientException: InvalidApi.NotFound : Specified api is not found, pleasecheck your url and method.
```

This error message indicates that the account is not authorized to call the specified API operation. To resolve this issue, perform the following operations: Contact the DataWorks technical support staff and provide them with the Apsara Stack tenant account to be authorized and the API operations to be called. After you receive an encrypted license generated by the DataWorks technical support staff based on the configuration in the runtime environment, use the license to authorize the account to make API requests.
1. Log on to Apsara Infrastructure Management Framework.
For more information, see Log on to Apsara Infrastructure Management Framework under Operat ions of basic plat f orms > Apsara Inf rast ruct ure Management Framework in Alibaba Cloud Apsara Stack Enterprise Operations Guide.
2. In the left-side navigation pane, click Monit oring.
3. In the top navigation bar, move the pointer over T asks and select Deployment Summary from
the drop-down menu.
4. On the Deployment Summary page, click Deployment Det ails. The Deployment Details page
appears.
5. Move the pointer over the base service, click Det ails, and then choose BasicClust er-A-
20190708-376d Machine List > base-baseBizApp > BaseBizMet aservice.
6. On the page that appears, find the target host and click T erminal in the Actions column to go to
the TerminalService page.
7. On the TerminalService page, click the Add icon, and run the docker ps | grep meta command
on the tab that appears to obtain the ID of the base-biz-metaservice container. For example, the following figure shows that the container ID is d6eb89507a17.
8. Log on to the container and run the docker exec -it d6eb89507a17 bash command. Then, you can
use the license for authorization. Run the following command to authorize the account to make API requests:

```bash
curl -X POST -d "license=4AA481CE03EAFA6529ECA131ED6E29AAD511B66A760C33786AD241BE1D90D7 007C4056FA26FD13318B92BCFB4B254E42" "http://127.0.0.1/dataos/v1/conf_dataos_api";
```

In this command, the license is provided by the DataWorks technical support staff. If `{"data":"ok"`

```
,"errCode":0,"errMsg":"success","requestId":"0a04142615555747936747847e031b"} appears
```

after you run the command, you can use the authorized account to make API requests. Sample code

```java
public void setup () throws IOException, ClientException {
   popEndpoint = "dataworks. envxxx.yyyyy.com";
   popEndpointName = "default";
   accessId = "accessId";
   accessKey = "accessKey";
   regionId = "default";
   popProduct = "dataworks-private-cloud";
   X509TrustAll.ignoreSSLCertificate();
   DefaultProfile.addEndpoint(popEndpointName, regionId, popProduct, popEndpoint);
   IClientProfile profile = DefaultProfile.getProfile(regionId, accessId, accessKey);
   IAcsClient client = new DefaultAcsClient(profile);
/** * Example: DemoApiRequest * @throws ServerException * @throws ClientException */ @Test public void test_DemoApi() throws ServerException, ClientException {
   DemoApiRequest request = new DemoApiRequest();
   request.setKeyword("abc");
   DemoApiResponse response = client.getAcsResponse(request);
   System.out.println(gson.toJson(response));
```

Specify the account for calling API operations that involve the scheduling system If you call an API operation that involves the scheduling system, you must specify the following three common request parameters: accountId, accountPwd, and clientName. The following procedure describes how to specify these three parameters:
1. You can ask a field engineer to log on to the database that hosts the base-biz-tsp service. The
name of the database is dwtsp.
2. The field engineer inserts a record into the cloudapi_account table to specify the accountId,
accountPwd, and clientName parameters. These three parameters uniquely identify the account that is used for calling the API operation.

### 4.2 HTTP API

> **Warning:** Alibaba Cloud has stopped maintaining the DataWorks HTTP API. To be compatible with earlier versions, the HTTP method can still be used, but will be discontinued in later versions. Change to use the Java SDK as soon as possible.

#### 4.2.1 Endpoints

The DataWorks API operations are categorized based on functions. Each type of API operations is accessed by using a specific domain name. For more information about the domain names, see the description about each type of API operations.

#### 4.2.2 Protocol

All APIs use the HTTP protocol in Apsara Stack.

#### 4.2.3 Request method

You can use the HTTP GET or POST request method to fulfill your intentions based on the description in the related API reference. If you use the GET method, an API operation returns the result based on the parameters in the query string. If you use the POST method, an API operation returns the result based on the parameters in the query string. The parameters in the request body are ignored.

#### 4.2.4 Encoding

UTF-8 encoding is used in all the DataWorks APIs.

#### 4.2.5 Signature method

Header (Required) base_id (Required) tenant_id Signature You must sign all API requests so that your identity can be verified. To sign an API request, follow these steps:
1. Add the following two parameters to the request URL: baseKey and timestamp.
2. Calculate a signature and add it to the HTTP header.
Sample GET request In this example, User B provides an HTTP GET API: /getapi. The name and age parameters are query parameters in the request URL. User A needs to use a URL that includes the following part to make the API request: /getapi?name=fengyeng&age=20 . After User A obtains a token from the token center with the authentication passed such as AppCode, the baseKey and timestamp parameters are added to the request URL as query parameters. You can specify the authentication method to allow others to access the API operation. Therefore, the new URL includes the following part: /getapi?name=fengyeng&age=20?baseKey=dsa134&timestamp=123456 `789` . A signature is then generated based on the token and query parameters in the new URL, and added to the request header by the requester as a field, for example, signature:dsafadfsa141fdsaf1. Sample POST request In this example, User B provides an HTTP POST API: /postapi. User A needs to use a URL that includes the following part to make the API request: /postapi. After User A obtains a token from the token center, the baseKey and timestamp parameters are added to the request URL as query parameters. Therefore, the new URL includes the following part: /postapi? baseKey=dsa134&timestamp=123456789. A signature is then generated based on the token and query parameters in the new URL, and added to the request header by the requester as a field, for example, signature:dsafadfsa141fdsaf1.

#### 4.2.6 Response parameters

```json
    "requestId": <STRING>, # The request ID, which is used to locate the log entries for tr
oubleshooting.
    "returnCode": "0", # A value of 0 indicates that the API operation is successful.
    "returnMessage": <STRING>, # The operation details.
    "successCode": "0",
    "count": <INTEGER>,
    "returnValue": <The returned result>
```

#### 4.2.7 API example

Sample code

```java
import org.apache.commons.lang3.StringUtils; import org.apache.http.HttpResponse; import org.apache.http.client.HttpClient; import org.apache.http.client.methods.HttpGet; import org.apache.http.client.methods.HttpUriRequest; import org.apache.http.impl.client.Ht tpClientBuilder; import java.io.BufferedReader; import java.io.IOException; import java.io.InputStreamReader ; import java.net.URLDecoder; import java.security.MessageDigest; import java.util.Arrays; public class SearchNodes { public static void main(String[] args) throws Exception { HttpClient httpClient = HttpClientBuilder.create().buil d(); String uri = "http://baseapi. ***.com/v1.0/node/prod?exe cuteMethod=SEARCH&searchText=nodeT est"; HttpUriRequest request = createHttpRequest( "base key", "base token", uri
```

);

```java
request.setHeader("tenant_id", "tenant ID"); request.setHeader("base_id", "Apsara Stack ten ant account ID"); HttpResponse response = httpClient.execute(request); BufferedReader bufferedReader = new Bu fferedReader(new InputStreamReader(response.getEntity().getContent())); StringBuilder stringBuilder = new St ringBuilder(); while(bufferedReader.ready()) { String line = bufferedReader.readLine(); if (line == null) { break; stringBuilder.append(line); System.out.println(stringBuilder.toString());
```

`y` `p` `g` `g`

```java
private static String byteArrayToHexString(byte[] byteArray) { final char[] HEX_DIGITS = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b','c', 'd', 'e', 'f'}; String result = null; int l = byteArray.length; char[] str = new char[l << 1]; int k = 0; for (int i = 0; i < l; i++) { byte byte0 = byteArray[i]; str[k++] = HEX_DIGITS[byte0 >>> 4 & 0xf]; str[k++] = HEX_DIGITS[byte0 & 0xf]; result = new String(str); return result; public static String tokenSign(String param, String salt) t hrows Exception { if (StringUtils.isEmpty(param) || StringUtils.isEmpty(salt)) {
  return null;
String query = URLDecoder.decode(param, "UTF-8"); String[] pStr = query.trim().split("&"); Arrays.sort(pStr); StringBuilder buf = new StringBuilder(); for (int i = 0; i < pStr.length; ++i) { buf.append(pStr[i]); buf.append("&"); String paramStr = buf.substring(0, buf.length() - 1); String sourceStr = salt + ":" + paramStr + ":" + salt; MessageDigest md = MessageDigest.getInstance("SHA-256"); byte[] byteArray = md.digest(sourceStr.getBytes("UTF-8")); return byteArrayToHexString(byteArray); protected static HttpUriRequest createHttpRequest(String baseKey, String baseToken, String uri) { StringBuilder buf; int index = uri.indexOf('?') ; if (index == -1) {
   index = uri.length();
   buf = new StringBuilder(uri.length() + baseKey.length() + 13);
   buf.append(uri).append('?') ;
} else {
   buf = new StringBuilder(uri.length() + baseKey.length() + 13);
   buf.append(uri).append('&');
   buf.append("baseKey=").append(baseKey);
   buf.append("&timestamp=").append(System.currentTimeMillis());
   HttpUriRequest request = new HttpGet(buf.toString()); String signature;
   try {
       signature = tokenSign(buf.substring(index + 1), baseToken);
   } catch (Exception ex) {
     throw new RuntimeException("error on sign for uri: " + uri, ex);
   request.addHeader("signature", signature);
   return request;
```

ests

## 5 APIs for HTTP requests

### 5.1 Create a node

URL: /v1.0/node/{projectEnv}/sync Method: POST Path parameters

| Parameter | Type | Description |
|---|---|---|
| projectEnv | String | The type of the environment. Valid values: DEV and PROD. The value DEV specifies the development environment. The value PROD specifies the production environment. |

Body

```json
    "executeMethod": CREATE_NODE_SYNC, # The type of the operation.
    # For more information about the parameters, see NodeModifyDto in Data structure.
    "nodeType": <INTEGER>, # The node type. Valid values: 0, 1, 2, and 3. The value 0 speci
fies a node that runs as scheduled. The value 1 specifies a one-off node. The value 2 speci fies a paused node. The value 3 specifies a dry-run node.
    "dependentType": <INTEGER>, # The dependency type of the node. Valid values: 0, 1, 2, a
nd 3. The value 0 specifies that the node can be run without waiting for the previous cycle of a specified node is completed. The value 1 specifies that the node is run only after the previous cycle of its child nodes is completed. The value 2 specifies that the node is run only after its previous cycle is completed. The value 3 specifies that the node is run only after the previous cycle of a custom node is completed.
    "nodeName": <STRING>, # The name of the node.
    "prgType": <INTEGER>, # The type of the node code.
    "priority": <INTEGER>, # The priority of the node.
    "owner": <STRING>, # The owner of the node.
    "appId": <LONG>, # The ID of the workspace to which the node belongs.
    "cycType": <INTEGER>, # The scheduling type.
    "codeSrc": <STRING>, # The node code.
    "nodeFrom": <STRING>, # The source of the node.
    "inputs": [{ # The input data of the node.
     "data": <STRING>, # The output data of the ancestor node.
    }],
    "outputs": [{ # The output data of the node.
      "data": <STRING>, # The output data of the current node.
    }],
"uniqueId": <STRING>, # The unique ID that you define for the request.
```

Response ests

```json
    "requestId": <STRING>, # The request ID. It is used to find the log entries for trouble
shooting.
    "returnCode": "0", # The execution status of the operation. The value 0 indicates that
the operation is successful.
    "returnMessage": <STRING>, # The returned execution details.
    "successCode": "0",
    "returnValue": <LONG>, # Node ID
```

### 5.2 Update a node

URL: /v1.0/node/{projectEnv}/sync Method: POST Path parameters

| Name | Type | Description |
|---|---|---|
| projectEnv | String | Valid values: DEV and PROD. |

Request body

```json
    "executeMethod": CREATE_NODE_SYNC, # The operation type.
    # For more information about the parameters, see NodeModifyDto in Data structure.
    "nodeType": <INTEGER>, # The node type. Valid values: 0, 1, 2, and 3. 0: a normal task.
1: an ad-hoc task. 2: a task of a paused node. 3: a task of a dry-run node.
    "dependentType": <INTEGER>, # The dependency type. Valid values: 0, 1, 2, and 3. 0:  Th
e node is executed only after the current cycle of another node is completed. 1: The node i s executed only after the previous cycle of the user-created node is completed. 2: The node is executed only after the previous cycle of the level-1 node is completed. 3: The node is executed only after its previous cycle is completed.
    "nodeName": <STRING>, # The name of the node.
    "prgType": <INTEGER>, # The type of the node script.
    "priority": <INTEGER>, # The priority.
    "owner": <STRING>, # The workspace owner.
    "appId": <LONG>, # The workspace ID.
    "cycType": <INTEGER>, # The scheduling type.
    "codeSrc": <STRING>, # The node code.
    "nodeFrom": <STRING>, # The source of the node.
    "inputs": [{ # The node inputs.
     "data": <STRING>， # The output of the ancestor nodes.
    }],
    "outputs": [{ # The node outputs.
      "data": <STRING>, # The output of the node.
    }],
"uniqueId": <STRING>, # The unique ID that you define for the request.
```

Response ests

```json
    "requestId": <STRING>, # The request ID, used to search for logs diagnose the issues.
    "returnCode": "0", # 0 indicates that the operation is called.
    "returnMessage": <STRING>, # The operatiaon details.
    "successCode": "0",
    "returnValue": true
```

### 5.3 Update multiple nodes at a time

URL: /v1.0/node/{projectEnv} Method: POST Path parameters

| Parameter | Type | Description |
|---|---|---|
| projectEnv | String | The type of the environment. Valid values: DEV and PROD. The value DEV specifies the development environment. The value PROD specifies the production environment. |

Body `[`

```json
        "executeMethod": "CREATE_NODE", # The operation that you want to perform. Valid val
ues: CREATE_NODE, UPDATE_NODE, and DELETE_NODE.
        "nodeId": <LONG>, # The ID of the node in the scheduling system. This parameter mus
t be specified when you call this operation to update a node.
        "uniqueId": <LONG>, # Required. The unique ID of the request. It is transferred fro
m the client and used only by the client to compare execution results.
        "nodeName": <STRING>, # Required. The name of the node.
        "nodeType": <INTEGER>, # Required. The node type. Valid values: 0, 1, 2, and 3. The
value 0 specifies a node that runs as scheduled. The value 1 specifies a one-off node. The value 2 specifies a paused node. The value 3 specifies a dry-run node.
        "prgType": <INTEGER>, # Required. The type of the node code, for example, odps_shel
l and odps_sql.
        "description": <STRING>, # Optional. The description of the node.
        "paraValue": <STRING>, # Optional. The key-value pairs of a node.
        "priority": <INTEGER>, # Optional. The priority of the node. Default value: 0.
        "cronExpress": <STRING>, # Required. The CRON expression.
        "cloudUUID": <LONG>, # The node ID that is stored in the code library. This paramet
er is required when you call this operation to update a node and is optional when you call this operation to create a node.
        "fileId": <LONG>, # Optional. The ID of the node code file.
        "fileVersion": <LONG>, # Optional. The version number of the node code file.
        "owner": <STRING>, # Required. The owner of the node. The value must be a standard
employee ID. "resGroupId":<LONG>,#Required TheIDoftheresourcegrouptowhichthenodebe
```

ests

```json
        resGroupId: <LONG>, # Required. The ID of the resource group to which the node be
longs.
        "appId": <LONG>, # Required. The ID of the workspace to which the node belongs.
        "baseLineId": <LONG>, # The ID of the baseline to which the node belongs.
        "createUser": <STRING>, # Required. The user who created the node.
        "modifyUser": <STRING>, # Required. The user who modified the node last time.
        "multiInstCheckType": <INTEGER>, # Optional. The identifier of the operation that c
hecks whether multiple instances exist.
        "cycType": <INTEGER>, # Required. The cycle type. Valid values: 0, 1, and 2. The va
lue 0 specifies that the cycle is equal to or longer than one day. The value 1 specifies th at the cycle is shorter than one day. The value 2 specifies that the cycle is shorter than one day and node instances are executed in order of the node instance IDs, such as 1, 2, 3.
```

`..`

```json
        "dependentType": <INTEGER>, # Required. The dependency type of the node. Valid valu
es: 0, 1, 2, and 3. The value 0 specifies that the node can be run without waiting for the previous cycle of a specified node is completed. The value 1 specifies that the node is run only after the previous cycle of its child nodes is completed. The value 2 specifies that t he node is run only after its previous cycle is completed. The value 3 specifies that the n ode is run only after the previous cycle of a custom node is completed.
        "dependentNodeIds": [<LONG>, ...], # The ID of nodes on which the current node depe
nds. By default, this parameter is set to the IDs of child nodes of the current node.
        "multiInstKillType": <INTEGER>, # Optional. The type of instances to be terminated.
Valid values: 0, 1, and 2. The value 0 specifies to terminate no node instances. The value 1 specifies to terminate non-routine node instances. The value 2 specifies to terminate rou tine node instances.
        "refreshToTask": <BOOLEAN>, # Optional. Specifies whether the configuration takes e
ffect on the current node instance.
        "updateNodeOnly": <BOOLEAN>, # Specifies whether to refresh the metadata of ancesto
r and descendant nodes. Default value: false.
        "codeSrc": <STRING>, # The node code. This parameter must be specified when the val
ue of updateNodeOnly is set to false.
        "envType": <INTEGER> , # Optional. The type of the runtime environment.
        "nodeFrom": <STRING>, # Optional. The source of the node, that is, the system from
which the node is deployed.
        "inputs": [
                "data": <STRING>, # Required. The input data of the node.
```

`},`

```json
            ...
        ], # Required. The input data of the node.
        "outputs": [
                "data": <STRING>, # Required. The output data of the node.
            , ...
        ], # Required. The output data of the node.
        "relatedFlowId": <LONG>, # Optional. The ID of the sub-flow to which the node belon
gs.
        "startEffectDate": <STRING>, # Optional. The start date of the time period during w
hich scheduling is permitted.
        "endEffectDate": <STRING>, # Optional. The end date of the time period during which
scheduling is permitted.
        "rerunAble": <BOOLEAN>, # Required. Specifies whether the node can be rerun.
        "userExtension": <STRING>, # Optional. The extended properties of the node.
```

ests `,` `p` `p` `p`

```json
        "childNodeId": <LONG>, # Optional. The ID of the child node. It is used when you ad
d or delete a node dependency.
        "parentNodeId": <LONG>, # Optional. The ID of the parent node.
        "createInstanceUrl": <STRING>, # Optional. The URL used to create a node instance.
        "dqcType": <INTEGER>, # Optional. The type of the Data Quality check.
        "dqcDescription": <STRING>, # Optional. The description of the Data Quality check.
        "taskRerunTime": <INTEGER>, # Optional. The time when the node reruns.
        "taskRerunInterval": <LONG>, # Optional. The interval at which the node reruns.
        "manualTrigger": <INTEGER>, # Optional. Specifies whether the node needs to be manu
ally triggered.
        "sycRefreshTask": <BOOLEAN>, # Optional. Specifies whether the node instances are u
pdated when the node is updated.
        "flowId": <LONG> # Required. The ID of the flow to which the node belongs.
```

`},`

```
    ...
```

`]` Response

```json
    "requestId": <STRING>, # The request ID. It is used to find the log entries for trouble
shooting.
    "returnCode": "0", # The execution status of the operation. The value 0 indicates that
the operation is successful.
    "returnMessage": <STRING>, # The returned execution details.
    "successCode": "0",
    "returnValue": <STRING> # requestId
```

### 5.4 Delete a node

URL: /v1.0/node/{projectEnv}/sync Method: POST Path parameters

| Name | Type | Description |
|---|---|---|
| projectEnv | String | Valid values: DEV and PROD. |

Request body

```json
    "executeMethod": DELETE_NODE_SYNC, # The operation type.
    "nodeId": <LONG>, # The node ID.
```

Response ests

```json
    "requestId": <STRING>, # The request ID, used to search for logs to diagnose the issues
```

`.`

```json
    "returnCode": "0", # 0 indicates that the operation is called.
    "returnMessage": <STRING>, # The operation details.
    "successCode": "0",
    "returnValue": {
        "Node ID": "success",
```

…

### 5.5 Query parent nodes

Description: You can call this operation to query the parent nodes of the specified node. URL: /v1.0/node/{projectEnv} Method: GET Path parameters

| Name | Type | Description |
|---|---|---|
| projectEnv | String | Valid values: DEV and PROD. |

URL query string parameters

| Name | Type | Description |
|---|---|---|
| executeMethod | String | (Required) The operation that you want to perform. Set the value to SEARCH NODE PARENTS BY DEPTH. _ _ _ _ |
| nodeId | Long | (Required) The ID of the node. |
| depth | Integer | (Required) The number of levels to be traversed. |
| nodeIds | String | (Optional) The node IDs, separated by commas (,). |
| cloudUUID | Long | (Optional) The node ID that is stored in the code library. |

Response

```json
    "requestId": <STRING>, # The request ID, used to search for logs to diagnose the issues
```

`.`

```json
    "returnCode": "0", # 0 indicates that the operation is called.
    "returnMessage": <STRING>, # The operation details.
    "successCode": "0",
    "count": <INTEGER>,
    "returnValue": [<NodeEntity>, ...]
```

ests

### 5.6 Query child nodes

Description: You can call this operation to retrieve child nodes of a specified node by level. URL: /v1.0/node/{projectEnv} Method: GET Path parameters

| Name | Type | Description |
|---|---|---|
| projectEnv | String | Valid values: DEV and PROD. |

URL query string parameters

| Name | Type | Description |
|---|---|---|
| executeMethod | String | (Required) The operation that you want to perform. Set the value to SEARCH NODE PARENTS BY DEPT _ _ _ _ H. |
| nodeId | Long | (Required) The node ID. |
| depth | Integer | (Required) The number of levels to be traversed. |
| nodeIds | String | (Optional) The node IDs, separated by commas (,). |
| cloudUUID | Long | (Optional) The node ID that is stored in the code library. |

Response

```json
    "requestId": <STRING>, # The request ID, used to search for logs to diagnose the issues
```

`.`

```json
    "returnCode": "0", # 0 indicates that the operation is called.
    "returnMessage": <STRING>, # The operation details.
    "successCode": "0",
    "count": <INTEGER>,
    "returnValue": [<NodeEntity>, ...]
```

### 5.7 Query the node code

URL: /v1.0/node/{projectEnv} Method: GET ests Path parameters

| Parameter | Type | Description |
|---|---|---|
| projectEnv | String | The type of the environment. Valid values: DEV and PROD. The value DEV specifies the development environment. The value PROD specifies the production environment. |

Query parameters in the request URL

| Parameter | Type | Description |
|---|---|---|
| executeMethod | String | The operation that you want to perform. Set the value to SEARCH NODE CODE. _ _ |
| cloudUUID | Long | The node ID that is stored in the code library. |
| version | Long | The version of the node code. |

Response

```json
    "requestId": <STRING>, # The request ID. It is used to find the log entries for trouble
shooting.
    "returnCode": "0", # The execution status of the operation. The value 0 indicates that
the operation is successful.
    "returnMessage": <STRING>, # The returned execution details.
    "successCode": "0",
    "count": <INTEGER>,
    "returnValue": <STRING> # The node code.
```

### 5.8 Query nodes

URL: /v1.0/node/{projectEnv} Method: GET Path parameters

| Parameter | Type | Description |
|---|---|---|

ests

| Parameter | Type | Description |
|---|---|---|
| projectEnv | String | The type of the environment. Valid values: DEV and PROD. The value DEV specifies the development environment. The value PROD specifies the production environment. |

Query parameters in the request URL

| Parameter | Type | Description |
|---|---|---|
| executeMetho d | String | The operation that you want to perform. Set the value to SEARCH. |
| nodeName | String | Optional. The name of the node. |
| cloudUUID | Long | Optional. The node ID that is stored in the code library. |
| nodeId | Long | Optional. The ID of the node to query. |
| version | Long | Optional. The version of the node code. |
| inputs | String | Optional. The input data of the node. Separate multiple records with commas (,). |
| outputs | String | Optional. The output data of the node. Separate multiple records with commas (,). |
| fileId | Long | Optional. The ID of the code file. |
| nodeIds | String | Optional. The IDs of nodes to query. Separate multiple IDs with commas (,). |
| searchText | String | Optional. The characters to be entered on the front end used for searches, including the node ID and node name. The suffix fuzzy search is supported. |
| prgType | String | Optional. The type of the node code. |
| prgTypes | Integer | Optional. The types of the node code. Separate multiple types with commas (,). |
| appId | Long | Optional. The ID of the workspace to which the nodes belong. If you do not specify this parameter, all the applications under the current account are searched. |
| owner | String | Optional. The owner of the node. |
| createUser | String | Optional. The user who created the node. |
| modifyUser | String | Optional. The user who modified the node. |

| D e | eveloper Guide·A sts | PIs for HTTP requ | DataWork | s |
|---|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| createTime | String | Optional. The time when the node was created, in the format of yyyy- MM-dd HH:mm:ss. |
| modifyTime | String | Optional. The time when the node was modified, in the format of yyyy- MM-dd HH:mm:ss. |
| baseLineId | Long | Optional. The ID of the baseline. |
| deployDate | String | Optional. The time when the node was deployed. |
| orderBy | String | Optional. Specifies the way in which the nodes are ordered. |
| isDetail | Boolean | Optional. Specifies whether to query the node details. |
| depth | Integer | Optional. The number of levels to be traversed. |
| flowId | Long | The ID of the flow to which the node belongs. |
| nodeType | Integer | The type of the node. Valid values: 0, 1, 2, and 3. 0: the nodes that run as scheduled. 1: a node that must be manually triggered and cannot be scheduled. 2: a paused node. Paused nodes are initiated as scheduled but the system immediately returns a failure indication without executing the nodes. 3: a dry-run node. Dry-run nodes are initiated as scheduled but the system immediately returns a success indication without executing the nodes. This parameter is optional. |
| tenantId | Long | Optional. The ID of the tenant. |
| bizDate | String | Optional. The date-based timestamp of the node, in the format of yyyy-MM-dd. |
| prgName | String | Optional. The name of the node code file. |
| isOnline | Integer | Optional. The online status of the node. Valid values: 0 and 1. 0: online. 1: offline. |
| modifyStartTi me | String | Optional. The start of the time period during which the node was modified. |
| modifyEndTim e | String | Optional. The end of the time period during which the node was modified. |
| deployStarting Date | String | Optional. The start of the time period during which the node was deployed. |
| deployDeadlin eDate | String | Optional. The end of the time period during which the node was deployed. |

| ataWorks |   | Developer Guide·APIs for HTTP req est |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| nodeForm | String | The source of the node. |
| rerunAble | Boolean | Optional. Specifies whether to query nodes that can be or cannot be rerun. |
| bizId | Long | Optional. The workflow ID. |
| solId | Long | Optional. The solution ID. |
| filePaths | String | Optional. The paths to the node code files. |
| isSmoke | Boolean | Optional. Specifies whether to query nodes for which the smoke test is or is not run. |
| resGroupId | Long | Optional. The ID of the resource group. |
| isDeploy | Boolean | Optional. Specifies whether to query nodes that are deployed or are not deployed. |
| deployType | Integer | Optional. The type of the node after deployment. Valid values: 0, 1, 2, and 3. The value 0 specifies no type limit. The value 1 specifies a new node. The value 2 specifies a modified node. The value 3 specifies a deleted node. |
| pageStart | Integer | None. |
| pageSize | Integer | None. |

Response

```json
    "requestId": <STRING>, # The request ID. It is used to find the log entries for trouble
shooting.
    "returnCode": "0", # The execution status of the operation. The value 0 indicates that
the operation is successful.
    "returnMessage": <STRING>, # The returned execution details.
    "successCode": "0",
    "count": <INTEGER>,
    "returnValue": [
        <NodeEntity>,
        ...
```

`]`

### 5.9 Query a node by ID

URL: /v1.0/node/{projectEnv} Method: GET Path parameters ests

| Name | Type | Description |
|---|---|---|
| projectEnv | String | Valid values: DEV and PROD. |

URL query string parameters

| Name | Type | Description |
|---|---|---|
| executeMethod | String | SEARCH NODE BY ID _ _ _ |
| nodeId | Long | None. |
| isDetail | Boolean | Indicates whether to query the details about the node. |

Response

```json
    "requestId": <STRING>, # The request ID, used to search for logs to diagnose the issues
```

`.`

```json
    "returnCode": "0", #  0 indicates that the operation is called.
    "returnMessage": <STRING>, # The operation details.
    "successCode": "0",
    "count": <INTEGER>,
    "returnValue": <NodeEntity>
```

### 5.10 Obtain the total number of nodes

nodes URL: /v1.0/node/{projectEnv} Method: GET Headers: application/json; charset=UTF-8 Path parameters

| Name | Type | Description |
|---|---|---|
| projectEnv | String | Valid values: DEV and PROD. |

URL query string parameters

| Name | Type | Description |
|---|---|---|
| executeMethod | String | The operation that you want to perform. Set the value to SEARCH NODE COUNT. _ _ |

ests Response

```json
    "returnCode": "0",
    "returnErrorSolution": "",
    "returnMessage": "",
    "requestId": null,
    "returnValue": 283232, # The total number of nodes.
    "success": true
```

### 5.11 Query node instances

URL: /v1.0/task/{projectEnv} Headers: application/json; charset=UTF-8 Method: GET Path parameters

| Parameter | Type | Description |
|---|---|---|
| projectEnv | String | The type of the environment. Valid values: DEV and PROD. The value DEV specifies the development environment. The value PROD specifies the production environment. |

Query parameters in the request URL

| Parameter | Type | Description |
|---|---|---|
| executeMethod | String | The operation that you want to perform. Set the value to SEARCH. |
| appId | Long | The ID of the workspace to which the node instance belongs. |
| appIds | String | The IDs of workspaces to which the node instances belong. Separate multiple application IDs with commas (,). |
| taskId | Long | The ID of the node instance to query. |
| nodeId | Long | The ID of the node to which the node instance belongs. |
| inGroupId | Long | The ID of the cycle to which the node instance belongs. |
| nodeIds | String | The IDs of nodes to which the node instances belong. Separate multiple node IDs with commas (,). |
| dagId | Long | The ID of the workflow instance to which the node instance belongs. |

| eveloper Guide·APIs f | or HTTP requ |   |
|---|---|---|

ests

| Parameter | Type | Description |
|---|---|---|
| taskType | Integer | The type of the node instance. Valid values: 0, 1, 2, and 3. 0: routine. 1: manually triggered. 2: paused. 3: dry-run. |
| taskTypes | String | The types of the node instances. Separate multiple types with commas (,). |
| taskStatuses | String | The statuses of the node instances. Separate multiple statuses with commas (,). |
| dagType | Integer | The type of the workflow instance to which the node instance belongs. Valid values: 1, 2, 3, and 4. 1: the routine workflow instance that is run as scheduled. 2: the workflow instance for smoke test. 3: the workflow instance for generating retroactive data. 4: the manually triggered workflow instance. |
| prgType | Integer | The type of the node code. |
| status | Integer | The status of the node. |
| owner | String | The owner of the node or the node instance. |
| bizdate | String | The date-based timestamp. |
| odpsInstanceId | String | The ID of the ODPS node instance. |
| bizBeginHour | String | The start of the time period when the workflow runs. |
| bizEndHour | String | The end of the time period when the workflow runs. |
| beginBizDate | String | The start date of the period when the workflow runs. |
| endBizDate | String | The end date of the period when the workflow runs. |
| searchText | String | The characters entered on the front end used for searches, including the node ID and node name. |
| baseLineId | Long | The ID of the baseline to which the node instance belongs. |
| createTime | String | The time when the node instance was created. |
| isDetail | Boolean | Optional. Specifies whether to query the details of the node instance. |
| opSeq | Long | The sequence number of the operation. |
| depth | Integer | Optional. The number of levels to be traversed. |

| ataWorks |   | Developer Guide·APIs for HTTP req est |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| historyId | Long | The ID of the node instance log. |
| costTime | Integer | The time elapsed for running the node instance. Unit: seconds. |
| startRunTimeFrom | String | The start of a time period during which the node instance starts running. |
| startRunTimeTo | String | The end of a time period during which the node instance starts running. |
| finishRunTimeFro m | String | The start of a time period during which the node instance stops running. |
| finishRunTimeTo | String | The end of a time period during which node instance stops running. |
| createTimeFrom | String | The start of a time period during which the node instance was created. |
| createTimeTo | String | The end of a time period during which the node instance was created. |
| prgTypes | String | The types of the node code. Separate multiple types with commas (,). |
| taskIds | String | The IDs of the node instances to query. |
| rerunAble | Boolean | Optional. Specifies whether to query node instances that can be or cannot be rerun. |
| dagName | String | The name of the workflow instance. |
| orderBy | String | Optional. Specifies the way in which the node instances are ordered. |
| bizId | Long | The ID of the workflow. |
| solId | Long | The ID of the solution. |
| gmtdate | String | The date when the node instance was generated. |
| createUser | String | The user who created the node instance. |
| modifyUser | String | The user who modified the node instance last time. |
| modifyTime | String | The time when the node instance was last modified. |
| deployDate | String | The date when the node instance was deployed. |
| pageStart | Integer | The start number of the returned page. |
| pageSize | Integer | The number of entries returned per page. |

Response ests

```json
    "requestId": <STRING>, # The request ID. It is used to find the log entries for trouble
shooting.
    "returnCode": "0", # The execution status of the operation. The value 0 indicates that
the operation is successful.
    "returnMessage": <STRING>, # The returned execution details.
    "successCode": "0",
    "count": <INTEGER>,
    "returnValue": [
        <TaskEntity>,
        ...
```

`]`

### 5.12 Query the operational logs of a node instance

node instance URL: /v1.0/task/{projectEnv} Headers: application/json; charset=UTF-8 Method: GET Path parameters

| Parameter | Type | Description |
|---|---|---|
| projectEnv | String | The type of the environment. Valid values: DEV and PROD. The value DEV specifies the development environment. The value PROD specifies the production environment. |

Query parameters in the request URL

| Parameter | Type | Description |
|---|---|---|
| executeMethod | String | The operation that you want to perform. Set the value to SEARCH TASK RUNLOG. _ _ |
| taskId | Long | The ID of the node instance. Specify either taskId or historyId. |
| historyId | Long | The ID of the node instance log. Specify either taskId or historyId. |

Response ests

```json
    "requestId": <STRING>, # The request ID. It is used to find the log entries for trouble
shooting.
    "returnCode": "0", # The execution status of the operation. The value 0 indicates that
the operation is successful.
    "returnMessage": <STRING>, # The returned execution details.
    "successCode": "0",
    "returnValue": <STRING>
```

### 5.13 Query a node instance by ID

URL: /v1.0/task/{projectEnv} Headers: application/json; charset=UTF-8 Method: GET Path parameters

| Parameter | Type | Description |
|---|---|---|
| projectEnv | String | The type of the environment. Valid values: DEV and PROD. The value DEV specifies the development environment. The value PROD specifies the production environment. |

Query parameters in the request URL

| Parameter | Type | Description |
|---|---|---|
| executeMetho d | String | The operation that you want to perform. Set the value to SEARCH TASK BY ID. _ _ _ |
| taskId | Long | The ID of the node instance to query. |
| isDetail | Boolean | Specifies whether to obtain the application details. |

Response

```json
    "requestId": <STRING>, # The request ID. It is used to find the log entries for trouble
shooting.
    "returnCode": "0", # The execution status of the operation. The value 0 indicates that
the operation is successful.
    "returnMessage": <STRING>, # The returned execution details.
    "successCode": "0",
    "returnValue": <TaskEntity>
```

ests

### 5.14 Query the parent node instance by level

by level URL: /v1.0/task/{projectEnv} Headers: application/json; charset=UTF-8 Method: GET Path parameters

| Name | Type | Description |
|---|---|---|
| projectEnv | String | Valid values: DEV and PROD. |

URL query string parameters

| Name | Type | Description |
|---|---|---|
| executeMetho d | String | The operation that you want to perform. Set the value to SEARCH TASK PARENTS BY DEPTH. _ _ _ _ |
| taskId | Long | The ID of the business flow instance that contains the task instance. |
| depth | Integer | The level of the node. |

Response

```json
    "requestId": <STRING>, # The request ID, used to search for logs to diagnose the issues
```

`.`

```json
    "returnCode": "0", # 0 indicates that the operation is called.
    "returnMessage": <STRING>, # The operation details.
    "successCode": "0",
    "count": <INTEGER>,
    "returnValue": [
        <TaskEntity>,
        ...
```

`]`

### 5.15 Query the child node instances at a specified level

at a specified level URL: /v1.0/task/{projectEnv} Headers: application/json; charset=UTF-8 Method: GET ests Path parameters

| Parameter | Type | Description |
|---|---|---|
| projectEnv | String | The type of the environment. Valid values: DEV and PROD. The value DEV specifies the development environment. The value PROD specifies the production environment. |

Query parameters in the request URL

| Parameter | Type | Description |
|---|---|---|
| executeMetho d | String | The operation that you want to perform. Set the value to SEARCH TASK CHILDREN BY DEPTH. _ _ _ _ |
| taskId | Long | The ID of the node instance. |
| depth | Integer | The level where the node instance resides. |

Response

```json
    "requestId": <STRING>, # The request ID. It is used to find the log entries for trouble
shooting.
    "returnCode": "0", # The execution status of the operation. The value 0 indicates that
the operation is successful.
    "returnMessage": <STRING>, # The returned execution details.
    "successCode": "0",
    "count": <INTEGER>,
    "returnValue": [
        <TaskEntity>,
        ...
```

`]`

### 5.16 Query the number of node instances in each status of an application

instances in each status of an application URL: /v1.0/task/{projectEnv} Headers: application/json; charset=UTF-8 Method: GET Path parameters ests

| Parameter | Type | Description |
|---|---|---|
| projectEnv | String | The type of the environment. Valid values: DEV and PROD. The value DEV specifies the development environment. The value PROD specifies the production environment. |

Query parameters in the request URL

| Parameter | Type | Description |
|---|---|---|
| executeMethod | String | The operation that you want to perform. Set the value to SEARCH TASK STATISTICS. _ _ |
| appId | Long | - |
| bizdate | String | - |

Response

```json
    "requestId": <STRING>, # The request ID. It is used to find the log entries for trouble
shooting.
    "returnCode": "0", # The execution status of the operation. The value 0 indicates that
the operation is successful.
    "returnMessage": <STRING>, # The returned execution details.
    "successCode": "0",
    "count": <INTEGER>,
    "returnValue": {
         "dagType": <INTEGER>,
         "appId": <LONG>,
         "bizdate": <STRING>, # The date-based timestamp.
         "noRun": <INTEGER>,
         "running": <INTEGER>,
         "waittingResource": <INTEGER>,
         "failure": <INTEGER>,
         "success": <INTEGER>,
        "waittingTime": <INTEGER>
```

### 5.17 Query the number of task instances in each status on a specified business date

instances in each status on a specified business date URL: /v1.0/task/{projectEnv} ests Headers: application/json; charset=UTF-8 Method: GET Path parameters

| Name | Type | Description |
|---|---|---|
| projectEnv | String | Valid values: DEV and PROD. |

URL query string parameters

| Name | Type | Description |
|---|---|---|
| executeMethod | String | The operation that you want to perform. Set the value to SEARCH TASK STATISTICS BY OW _ _ _ _ NER. |
| bizdate | String | None. |

Response

```json
   "requestId": <STRING>, # The request ID, used to search for logs to diagnose the issues.
    "returnCode": "0", # 0 indicates that the operation is called.
    "returnMessage": <STRING>, # The operation details.
    "successCode": "0",
    "count": <INTEGER>,
    "returnValue": {
         "dagType": <INTEGER>,
         "appId": <LONG>,
         "bizdate": <STRING>, # The business date.
         "noRun": <INTEGER>,
         "running": <INTEGER>,
         "waittingResource": <INTEGER>,
         "failure": <INTEGER>,
         "success": <INTEGER>,
        "waittingTime": <INTEGER>
```

### 5.18 Query the number of node instances in each status for applications

instances in each status for applications URL: /v1.0/task/{projectEnv} Headers: application/json; charset=UTF-8 ests Method: GET Path parameters

| Parameter | Type | Description |
|---|---|---|
| projectEnv | String | The type of the environment. Valid values: DEV and PROD. The value DEV specifies the development environment. The value PROD specifies the production environment. |

Query parameters in the request URL

| Parameter | Type | Description |
|---|---|---|
| executeMethod | String | The operation that you want to perform. Set the value to SEARCH TASK SUCCESSINFO. _ _ |
| bizdate | String | The date-based timestamp. |
| costTime | Integer | The time elapsed for running the node instance. Unit: seconds. |
| startRunTimeFrom | String | The start of a time period during which the node instance starts running. |
| startRunTimeTo | String | The end of a time period during which the node instance starts running. |
| finishRunTimeFrom | String | The start of a time period during which the node instance stops running. |
| finishRunTimeTo | String | The end of a time period during which the node instance stops running. |
| createTimeFrom | String | The start of a time period during which the node instance was created. |
| createTimeTo | String | The end of a time period during which the node instance was created. |
| appId | Long | The ID of workspace to which the node instance belongs. |

|   |   | Developer Guide·APIs for HTTP req |
|---|---|---|

ests

| Parameter | Type | Description |
|---|---|---|
| searchText | String | The characters entered on the front end used for searches, including the node ID and node name. The suffix fuzzy search is supported. |
| nodeId | Long | The ID of the node to which the node instance belongs. |
| nodeIds | String | The IDs of nodes to which the node instances belong. |
| taskIds | String | The IDs of the node instances to query. |
| taskStatuses | String | The statuses of the node instances to query. |
| taskTypes | String | The types of the node instances to query. |
| prgTypes | String | The time when the node instance was created. |
| createTime | String |   |
| modifyTime | String | The time when the node instance was last modified. |
| deployDate | String | The date when the node instance was deployed. |
| gmtdate | String | The date when the node instance was generated. |
| bizBeginHour | String | The start of the time period when the workflow runs. |
| bizEndHour | String | The end of the time period when the workflow runs. |
| bizBeginDate | String | The start date of the period when the workflow runs. |
| bizEndDate | String | The end date of the period when the workflow runs. |

Response ests

```json
   "requestId": <STRING>, # The request ID. It is used to find the log entries for troubles
hooting.
    "returnCode": "0", # The execution status of the operation. The value 0 indicates that
the operation is successful.
    "returnMessage": <STRING>, # The returned execution details.
    "successCode": "0",
    "returnValue": {
        "totalCount": <INTEGER>,
        "notRunCount": <INTEGER>,
        "waitTimeCount": <INTEGER>,
        "waitResCount": <INTEGER>,
        "runningCount": <INTEGER>,
        "failureCount": <INTEGER>,
        "successCount": <INTEGER>
```

### 5.19 Rerun an instance

URL: /v1.0/task/{projectEnv} Headers: application/json; charset=UTF-8 Method: POST Path parameters

| Name | Type | Description |
|---|---|---|
| projectEnv | String | Valid values: DEV and PROD. |

Request body

```json
    "executeMethod": "RERUN_TASK",
    "taskId": <LONG>
```

Response

```json
    "requestId": <STRING>, # The request ID, used to search for logs to diagnose the issues
```

`.`

```json
    "returnCode": "0", # 0 indicates that the operation is called.
    "returnMessage": <STRING>, # The operation details.
    "successCode": "0",
    "returnValue": true
```

ests

### 5.20 Restore an instance

URL: /v1.0/task/{projectEnv} Headers: application/json; charset=UTF-8 Method: POST Path parameters

| Name | Type | Description |
|---|---|---|
| projectEnv | String | Valid values: DEV and PROD. |

Request body

```json
    "executeMethod": "RESUM_TASK",
    "taskId": <LONG>
```

Response

```json
    "requestId": <STRING>, # The request ID, used to search for logs to diagnose the issues
```

`.`

```json
    "returnCode": "0", # The value 0 indicates that the operation is called.
    "returnMessage": <STRING>, # The operation details.
    "successCode": "0",
    "returnValue": true
```

### 5.21 Set the instance status to Success and trigger descendant instances

Success and trigger descendant instances URL: /v1.0/task/{projectEnv} Headers: application/json; charset=UTF-8 Method: POST Path parameters

| Name | Type | Description |
|---|---|---|
| projectEnv | String | Valid values: DEV and PROD. |

Request body ests

```json
    "executeMethod": "SETSUCCESS_TASK",
    "taskId": <LONG>
```

Response

```json
    "requestId": <STRING>, # The request ID, used to search for logs to diagnose the issues
```

`.`

```json
    "returnCode": "0", # 0 indicates that the operation is called.
    "returnMessage": <STRING>, # The operation details.
    "successCode": "0",
    "returnValue": true
```

### 5.22 Terminate a task

URL: /v1.0/task/{projectEnv} Headers: application/json; charset=UTF-8 Method: POST Path parameters

| Name | Type | Description |
|---|---|---|
| projectEnv | String | Valid values: DEV and PROD. |

Request body

```json
    "executeMethod": "KILL_TASK",
    "taskId": <LONG>
```

Response

```json
    "requestId": <STRING>, # The request ID, used to search for logs to diagnose the issues
```

`.`

```json
    "returnCode": "0", # 0 indicates that the operation is called.
    "returnMessage": <STRING>, # The operation details.
    "successCode": "0",
    "returnValue": true
```

### 5.23 Rerun a descendant instance

ests URL: /v1.0/task/{projectEnv} Headers: application/json; charset=UTF-8 Method: POST Path parameters

| Name | Type | Description |
|---|---|---|
| projectEnv | String | Valid values: DEV and PROD. |

Request body

```json
    "executeMethod": "FIXDATA",
    "taskId": <LONG>,
    "includeTaskIds": [<LONG>, ...]
```

Response

```json
     "requestId": <STRING>, # The request ID, used to search for logs to diagnose the issue
```

`s.`

```json
    "returnCode": "0", # 0 indicates that the operation is called.
    "returnMessage": <STRING>, # The operation details.
    "successCode": "0",
    "returnValue": true
```

### 5.24 Update the scheduling configurations of an instance

configurations of an instance URL: /v1.0/task/{projectEnv} Headers: application/json; charset=UTF-8 Method: POST Path parameters

| Name | Type | Description |
|---|---|---|
| projectEnv | String | Valid values: DEV and PROD. |

Request body ests

```json
    "Executemethod": "maid ",
    "taskId": <LONG>
```

Response

```json
    "requestId": <STRING>, # The request ID, used to search for logs to diagnose the issues
```

`.`

```json
    "returnCode": "0", # 0 indicates that the operation is called.
    "returnMessage": <STRING>, # The operation details.
    "successCode": "0",
    "returnValue": true
```

### 5.25 Pause an instance

URL: /v1.0/task/{projectEnv} Headers: application/json; charset=UTF-8 Method: POST Path parameters

| Name | Type | Description |
|---|---|---|
| projectEnv | String | Valid values: DEV and PROD. |

Request body

```json
    "executeMethod": "STOP_TASK",
    "taskId": <LONG>
```

Response

```json
    "requestId": <STRING>, # The request ID, used to search for logs to diagnose the issues
```

`.`

```json
    "returnCode": "0", # 0 indicates that the operation is called.
    "returnMessage": <STRING>, # The operation details.
    "successCode": "0",
    "returnValue": true
```

### 5.26 Terminate multiple instances

ests URL: /v1.0/task/{projectEnv} Headers: application/json; charset=UTF-8 Method: POST Path parameters

| Name | Type | Description |
|---|---|---|
| projectEnv | String | Valid values: DEV and PROD. |

Request body

```json
     "executeMethod": "BATCH_KILL_TASK",
     "includeTaskIds": [<LONG>, ...]
```

Response

```json
    "requestId": <STRING>, # The request ID, used to search for logs to diagnose the issues
```

`.`

```json
    "returnCode": "0", # 0 indicates that the operation is called.
    "returnMessage": <STRING>, # The operation details.
    "successCode": "0",
    "returnValue": true
```

### 5.27 Rerun multiple instances

URL: /v1.0/task/{projectEnv} Headers: application/json; charset=UTF-8 Method: POST Path parameters

| Name | Type | Description |
|---|---|---|
| projectEnv | String | Valid values: DEV and PROD. |

Request body

```json
     "executeMethod": "BATCH_RESUM_TASK",
     "includeTaskIds": [<LONG>, ...]
```

Response ests

```json
    "requestId": <STRING>, # The request ID, used to search for logs to diagnose the issues
```

`.`

```json
    "returnCode": "0", # 0 indicates that the operation is called.
    "returnMessage": <STRING>, # The operation details.
    "successCode": "0",
    "returnValue": true
```

### 5.28 Resume multiple tasks

URL: /v1.0/task/{projectEnv} Headers: application/json; charset=UTF-8 Method: POST Path parameters

| Name | Type | Description |
|---|---|---|
| projectEnv | String | Valid values: DEV and PROD. |

Request body

```json
      "executeMethod": "BATCH_RESUM_TASK",
      "includeTaskIds": [<LONG>, ...]
```

Response

```json
    "requestId": <STRING>, # The request ID, used to search for logs to diagnose the issues
```

`.`

```json
    "returnCode": "0", # 0 indicates that the operation is called.
    "returnMessage": <STRING>, # The operation details.
    "successCode": "0",
    "returnValue": true
```

### 5.29 Pause multiple instances

URL: /v1.0/task/{projectEnv} Headers: application/json; charset=UTF-8 Method: POST Path parameters ests

| Name | Type | Description |
|---|---|---|
| projectEnv | String | Valid values: DEV and PROD. |

Request body

```json
      "executeMethod": "BATCH_STOP_TASK",
      "includeTaskIds": [<LONG>, ...]
```

Response

```json
    "requestId": <STRING>, # The request ID, used to search for logs to diagnose the issues
```

`.`

```json
    "returnCode": "0", # 0 indicates that the operation is called.
    "returnMessage": <STRING>, # The operation details.
    "successCode": "0",
    "returnValue": true
```

### 5.30 Set the status of multiple instances to Success

instances to Success URL: /v1.0/task/{projectEnv} Headers: application/json; charset=UTF-8 Method: POST Path parameters

| Name | Type | Description |
|---|---|---|
| projectEnv | String | Valid values: DEV and PROD. |

Request body

```json
     "executeMethod": "BATCH_SETSUCCESS_TASK",
     "includeTaskIds": [<LONG>, ...]
```

Response ests

```json
    "requestId": <STRING>, # The request ID, used to search for logs to diagnose the issues
```

`.`

```json
    "returnCode": "0", # 0 indicates that the operation is called.
    "returnMessage": <STRING>, # The operation details.
    "successCode": "0",
    "returnValue": true
```

### 5.31 Retrieve the total number of instances on the day

instances on the day URL: /v1.0/task/{projectEnv} Headers: application/json; charset=UTF-8 Method: GET Path parameters

| Name | Type | Description |
|---|---|---|
| projectEnv | String | Valid values: DEV and PROD. |

URL query string parameters

| Name | Type | Description |
|---|---|---|
| executeMetho d | String | SEARCH TASK STATISTICS BY DATE _ _ _ _ |
| dagType | Integer | (Optional) Default value: 1. |
| bizdate | String | (Optional) The day before the current day, in the format of yyyy-MM- dd. |

Response

```json
    "returnCode": "0",
    "returnErrorSolution": "",
    "returnMessage": "",
    "requestId": null,
    "Redding value": 283232, # The number of instances.
    "success": true
```

### 5.32 Query business flow instances

URL: /v1.0/dag/{projectEnv} ests Method: GET Path parameters

| Name | Type | Description |
|---|---|---|
| projectEnv | String | Valid values: DEV and PROD. |

URL query string parameters

| Name | Type | Description |
|---|---|---|
| executeMetho d | String | The operation that you want to perform. Set the value to SEARCH DAG BY ID. _ _ _ |
| dagId | Long | The ID of the business flow instance that contains the task instance. |

Response

```json
    "requestId": <STRING>, # The request ID, used to search for logs to diagnose the issues
```

`.`

```json
    "returnCode": "0", # 0 indicates that the operation is called.
    "returnMessage": <STRING>, # The operation details.
    "successCode": "0",
    "count": <INTEGER>,
    "returnValue": [<DagEntity>, ...]
```

### 5.33 Retroactive execution

URL: /v1.0/dag/{projectEnv} Method: POST Path parameters

| Name | Type | Description |
|---|---|---|
| projectEnv | String | Valid values: DEV and PROD. |

Request body ests

```json
        "executeMethod": "CREATE_DAG",
        "name": <STRING>, # The name of the retroactive workflow.
 "type": 3, # The business flow type. 3: retroactive execution.
 "rootNodeId": <LONG>, # The root node ID from which the retroactive execution starts. If d
ata of only one node is retroacted, set the value to the ID of the node.
 "includeNodeIds": [<LONG>, ...], # The IDs of the nodes to be retroacted. If data of only
one node is retroacted, set the value to the ID of the node.
 "excludeNodeIds": [<LONG>, ...], # The IDs of nodes that are excluded from the retroactive
execution.
 "startBizDate": <STRING>, # The start date-based timestamp of data involved in the retroac
tive task, in the format of yyyy-MM-dd hh:mm:ss.
 "endBizDate": <STRING>, # The end date-based timestamp of data involved in the retroactive
task, in the format of yyyy-MM-dd hh:mm:ss.
 "bizBeginTime": <STRING>, # The start time of the hourly task. For example, 13:04:04.
 "bizEndTime": <STRING>, # The end time of the hourly task. For example, 14:04:04.
 "isParallel": <BOOLEAN>, # Indicates whether the DAGs of retroactive execution can run con
currently.
 "nodeParas": {<LONG>: <STRING>, ...}, # (Optional) The user-defined parameter for updating
a node. The key is node ID. The value is the ID of the node.
        "dagPara": <STRING>, # (Optional) The parameter for configuring a DAG, which applie
s to all instances in the DAG.
```

Response

```json
    "requestId": <STRING>, # The request ID, used to search for logs to diagnose the issues
```

`.`

```json
    "returnCode": "0", # 0 indicates that the operation is called.
    "returnMessage": <STRING>, # The operation details.
    "successCode": "0",
    "returnValue": <LONG>, # The DAG ID.
```

### 5.34 Run a smoke test

URL: /v1.0/dag/{projectEnv} Method: POST Path parameters

| Parameter | Type | Description |
|---|---|---|
| projectEnv | String | The type of the environment. Valid values: DEV and PROD. The value DEV specifies the development environment. The value PROD specifies the production environment. |

ests Body

```json
        "executeMethod": "CREATE_DAG",
        "name": <STRING>, # The custom name of the workflow.
 "type": 2, # The type of the workflow instance. The value 2 specifies a smoke test.
 "bizdate": <STRING>, # The date-based timestamp, in the format of yyyy-MM-dd hh:mm:ss.
 "rootNodeId": <LONG>, # The ID of the root node.
 "rootNodeAppId": <LONG>, # The ID of the workspace to which the root node belongs.
 "includeNodeIds": [], # The IDs of the whitelisted nodes. Leave this parameter blank.
 "excludeNodeIds": [], # The IDs of the blacklisted nodes. Leave this parameter blank.
 "bizBeginTime": <STRING>, # The start time of the hourly node, for example, 13:04:04.
 "bizEndTime": <STRING>, # The end time of the hourly node, for example, 14:04:04.
 "isParallel": false, # Specifies whether the node instance for running the smoke test can
be run concurrently.
 "nodeParas": {<LONG>: <STRING>, ...}, # Optional. The custom key-value pairs for updating
a node. Set the keys to node ID and the values to the scheduling parameters of the node.
    "dagPara": <STRING>, # Optional. The key-value pair used to generate retroactive data f
or a workflow instance. It applies to all node instances that belong to the workflow instan ce.
```

Response

```json
    "requestId": <STRING>, # The request ID. It is used to find the log entries for trouble
shooting.
    "returnCode": "0", # The execution status of the operation. The value 0 indicates that
the operation is successful.
    "returnMessage": <STRING>, # The returned execution details.
    "successCode": "0",
    "returnValue": <LONG>, # dag id
```

### 5.35 Execute an ad-hoc business flow

URL: /v1.0/dag/{projectEnv} Method: POST Path parameters

| Name | Type | Description |
|---|---|---|
| projectEnv | String | Valid values: DEV and PROD. |

Request body ests

```json
        "executeMethod": "CREATE_BUS_PROC_DAG",
        "name": <STRING>, # The name of the ad-hoc business flow instance.
 "type": 5, # Set the type of the ad-hoc business flow instance to 5.
        "flowId": <LONG>, # The ID of the ad-hoc business flow.
 bizdate": <STRING>,  # The date-based timestamp of data, in the format of yyyy-MM-dd hh:mm
:ss.
 "rootNodeAppId": <LONG>,  # The ID of the application.
 "includeNodeIds": [],
 "excludeNodeIds": [],
 "isParallel": false,
 "nodeParas": {<LONG>: <STRING>, ...}, # (Optional) The user-defined parameter for updating
a node. The key is node ID. The value is the ID of the node.
        "dagPara": <STRING>, # (Optional) The parameter for configuring a DAG, which applie
s to all instances in the DAG.
```

Response

```json
    "requestId": <STRING>, # The request ID, used to search for logs to diagnose the issues
```

`.`

```json
    "returnCode": "0", # 0 indicates that the operation is called.
    "returnMessage": <STRING>, # The operation details.
    "successCode": "0",
    "count": <INTEGER>,
    "returnValue": <LONG>, # The DAG ID.
```

### 5.36 Terminate a business flow

URL: /v1.0/dag/{projectEnv} Method: POST Path parameters

| Name | Type | Description |
|---|---|---|
| projectEnv | String | Valid values: DEV and PROD. |

Request body

```json
        "executeMethod": "CREATE_DAG",
       "Dagids": [<long>,...], # The ID of the DAGs to be terminated.
```

Response ests

```json
    "requestId": <STRING>, # The request ID, used to search for logs to diagnose the issues
```

`.`

```json
    "returnCode": "0", # 0 indicates that the operation is called.
    "returnMessage": <STRING>, # The operation details.
    "successCode": "0",
    "Charlevalue": <Boolean>
```

### 5.37 Submit a resource package

Description: You can call this operation to submit a resource package that contains flow and node definitions and resources. After the operation is called, RequestID is returned. URL: /submission/project/{projectIdentifier} Method: POST Headers: Content-type: multipart/form-data Data type: zipped files Response

```json
    "requestId": <STRING>, # The request ID, used to search for logs to diagnose the issues
```

`.`

```json
    "returnCode": "0", # 0 indicates that the operation is called.
    "returnMessage": <STRING>, # The operation details.
    "successCode": "0",
    "returnValue": true
```

### 5.38 Query the submission status of a resource package

resource package URL: /submission/project/{projectIdentifier}/{requestId} Path parameters

| Name | Type | Description |
|---|---|---|
| requestId | String | None. |

Response ests

```json
    "requestId": <STRING>, # The request ID, used to search for logs to diagnose the issues
```

`.`

```json
    "returnCode": "0", # 0 indicates that the operation is called.
    "returnMessage": <STRING>, # The operation details.
    "successCode": "0",
    "returnValue": {
        "createTime": <STRING>, # The time at which the submitted request is accepted by th
e system.
        "name": <STRING>, # The generated name in the [the caller system name-backToCheckId
-createTime] format.
        "status": <STRING>, # The status. Values: success, fail, and running.
        "message": <STRING>
```

### 5.39 Data structure

#### 5.39.1 NodeModifyDto

```json
        "nodeId": <LONG>, # The ID of the node in the scheduling system. This parameter mus
t be specified when you call this operation to update a node.
        "uniqueId": <LONG>, # Required. The unique ID of the request. It is transferred fro
m the client and used only by the client to compare execution results.
        "nodeName": <STRING>, # Required. The name of the node.
        "nodeType": <INTEGER>, # Required. The node type. Valid values: 0, 1, 2, and 3. The
value 0 specifies a node that runs as scheduled. The value 1 specifies a one-off node. The value 2 specifies a paused node. The value 3 specifies a dry-run node.
        "prgType": <INTEGER>, # Required. The type of the node code, for example, odps_shel
l and odps_sql.
        "description": <STRING>, # Optional. The description of the node.
        "paraValue": <STRING>, # Optional. The key-value pairs of a node.
        "priority": <INTEGER>, # Optional. The priority of the node. Default value: 0.
        "cronExpress": <STRING>, # Required. The CRON expression.
        "cloudUUID": <LONG>, # The node ID that is stored in the code library. This paramet
er is required when you call this operation to update a node and is optional when you call this operation to create a node.
        "fileId": <LONG>, # Optional. The ID of the code file.
        "fileVersion": <LONG>, # Optional. The version number of the code file.
        "owner": <STRING>, # Required. The owner of the node.
        "resGroupId": <LONG>, # Required. The ID of the resource group to which the node be
longs.
        "appId": <LONG>, # Required. The ID of the workspace to which the node belongs.
        "baseLineId": <LONG>, # The ID of the baseline to which the node belongs.
        "createUser": <STRING>, # Required. The user who created the node.
        "modifyUser": <STRING>, # Required. The user who modified the node last time.
        "cycType": <INTEGER>, # Required. The cycle type. Valid values: 0, 1, and 2. The va
lue 0 specifies that the cycle is equal to or longer than one day. The value 1 specifies th at the cycle is shorter than one day. The value 2 specifies that the cycle is shorter than one day and node instances are executed in order of the node instance IDs, such as 1, 2, 3.
```

ests `..`

```json
        "dependentType": <INTEGER>, # Required. The dependency type of the node. Valid valu
es: 0, 1, 2, and 3. The value 0 specifies that the node can be run without waiting for the previous cycle of a specified node is completed. The value 1 specifies that the node is run only after the previous cycle of a custom node is completed. The value 2 specifies that the node is run only after the previous cycle of its child nodes is completed. The value 3 spec ifies that the node is run only after its previous cycle is completed.
        "dependentNodeIds": [<LONG>, ...], # The IDs of the custom cross-version dependent
nodes. This parameter must be specified when the value of dependentType is set to 3. Separa te multiple IDs with commas (,).
        "multiInstKillType": <INTEGER>, # Optional. The type of instances to be terminated.
Valid values: 0, 1, and 2. The value 0 specifies to terminate no node instances. The value 1 specifies to terminate non-routine node instances. The value 2 specifies to terminate rou tine node instances.
        "refreshToTask": <BOOLEAN>, # Optional. Specifies whether the configuration takes e
ffect on the current node instance.
        "updateNodeOnly": <BOOLEAN>, # Specifies whether to refresh the metadata of ancesto
r and descendant nodes. Default value: false.
        "codeSrc": <STRING>, # The node code. This parameter must be specified when the val
ue of updateNodeOnly is set to false.
        "envType": <INTEGER> , # Optional. The type of the runtime environment.
        "nodeFrom": <STRING>, # Optional. The source of the node, that is, the system from
which the node is deployed.
        "inputs": [
                "data": <STRING>, # Required. The input data of the node.
```

`},`

```json
            ...
        ], # Required. The input data of the node.
        "outputs": [
                "data": <STRING>, # Required. The output data of the node.
            , ...
        ], # Required. The output data of the node.
        "relatedFlowId": <LONG>, # Optional. The ID of the sub-flow to which the node belon
gs.
        "startEffectDate": <STRING>, # Optional. The start date of the time period during w
hich scheduling is permitted.
        "endEffectDate": <STRING>, # Optional. The end date of the time period during which
scheduling is permitted.
        "rerunAble": <BOOLEAN>, # Required. Specifies whether the node can be rerun.
        "userExtension": <STRING>, # Optional. The extended properties of the node.
        "childNodeId": <LONG>, # Optional. The ID of the child node. It is used when you ad
d or delete a node dependency.
        "parentNodeId": <LONG>, # Optional. The ID of the parent node.
        "createInstanceUrl": <STRING>, # Optional. The URL used to create a node instance.
        "dqcType": <INTEGER>, # Optional. The type of the Data Quality check.
        "dqcDescription": <STRING>, # Optional. The description of the Data Quality check.
        "taskRerunTime": <INTEGER>, # Optional. The time when the node reruns.
        "taskRerunInterval": <LONG>, # Optional. The interval at which the node reruns.
```

`"`

```
lTi
```

`"`

```
INTEGER
#Oti
```

`l` `S`

```
ifi hth
```

`th` `d` `d` `t` `b` ests

```json
        "manualTrigger": <INTEGER>, # Optional. Specifies whether the node needs to be manu
ally triggered.
        "sycRefreshTask": <BOOLEAN>, # Optional. Specifies whether the node is a synchronou
s reloading node.
        "flowId": <LONG> # Required. The ID of the flow to which the node belongs.
```

#### 5.39.2 TaskEntity

```java
private Long id; // The node ID recorded in the database. It increments automatically. private Long taskId; // The ID of the node instance. private Long nodeId; // The ID of the node to which the node instance belongs. private Long dagId; // The ID of the workflow instance to which the node instance belongs. private Integer inGroupId; // The sequence number of the cycle on the current day of the ho urly node. private Integer taskType; // The type of the node. Valid values: 0, 1, 2, and 3. The value 0 specifies a node that runs as scheduled. The value 1 specifies a one-off node. The value 2 specifies a paused node. The value 3 specifies a dry-run node. private Integer dagType; // The type of the workflow instance to which the node instances b elong. Valid values: 1, 2, 3, and 4. The value 1 specifies the routine workflow instance th at is run as scheduled. The value 2 specifies the workflow instance for smoke test. The val ue 3 specifies the workflow instance for generating retroactive data. The value 4 specifies the manually triggered workflow instance. @JsonSerialize(using = DateSerializer.class, include = Inclusion.NON_NULL) @JsonDeserialize(using = DateDeserializer.class) private Date dueTime; // The time when the node is scheduled to run. private Integer status; // The status of the node. private Long opSeq; // The sequence number of the operation. private Integer opCode; // The operation command. private String owner; // The owner of the node instance. @JsonSerialize(using = DateSerializer.class, include = Inclusion.NON_NULL) @JsonDeserialize(using = DateDeserializer.class) private Date bizdate; // The date-based timestamp. @JsonSerialize(using = DateSerializer.class, include = Inclusion.NON_NULL) @JsonDeserialize(using = DateDeserializer.class) private Date gmtdate; // The date when the node instance was generated. private String gateway; // The gateway server on which the node runs. private String gwProcessId; // The ID of the gateway process in which the node runs. private String gwLogFile; // The log file of the gateway on which the node runs. @JsonSerialize(using = DateSerializer.class, include = Inclusion.NON_NULL) @JsonDeserialize(using = DateDeserializer.class) private Date alisaReturnTime; // The date when the alisa service is rerun. private String prgName; // The name of the node code file. private Integer prgType; // The type of the node code, for example, odps_sql. private Integer priority; // The priority of the node. private Integer weight; // The weight of the node. private String execName; // The name of the node code file. private Long fileId; // The ID of the node code file. private Integer fileVersion; // The version number of the node code file. private String odpsProjectName; // The name of the MaxCompute project. private String paraValue; // The key-value pairs of a node. private String gwLogLocalFile; // The local log file of the gateway on which the node runs. private String resGroupIdentifier; // The identifier of the resource group.
```

ests

```java
private Long resGroupId; // The ID of the resource group to which the node instance belongs
```

`.`

```java
private Long baseLineId; // The ID of the baseline to which the node instance belongs. private Long appId; // The ID of the workspace to which the node instance belongs. private String appName; // The name of the application to which the node instance belongs. @JsonSerialize(using = DateSerializer.class, include = Inclusion.NON_NULL) @JsonDeserialize(using = DateDeserializer.class) private Date beginWaitTimeTime; // The time elapsed until the node status is changed to Pen ding (Schedule). @JsonSerialize(using = DateSerializer.class, include = Inclusion.NON_NULL) @JsonDeserialize(using = DateDeserializer.class) private Date beginWaitResTime; // The time elapsed until the node status is changed to Pend ing (Resources). @JsonSerialize(using = DateSerializer.class, include = Inclusion.NON_NULL) @JsonDeserialize(using = DateDeserializer.class) private Date beginRunningTime; // The time elapsed until the node status is changed to Runn ing. @JsonSerialize(using = DateSerializer.class, include = Inclusion.NON_NULL) @JsonDeserialize(using = DateDeserializer.class) private Date finishTime; // The end of the time period when the node instance runs. @JsonSerialize(using = DateSerializer.class, include = Inclusion.NON_NULL) @JsonDeserialize(using = DateDeserializer.class) private Date createTime; // The time when the node instance was created. private String createUser; // The user who created the node instance. @JsonSerialize(using = DateSerializer.class, include = Inclusion.NON_NULL) @JsonDeserialize(using = DateDeserializer.class) private Date modifyTime; // The time when the node instance was modified last time. private String modifyUser; // The user who modified the node instance last time. private Integer multiInstCheckType; // The identifier of the operation that checks whether multiple instances exist. private Integer multiKillType; // The identifier of the operation that terminates multiple instances. private Integer cycType; // The cycle type. @JsonSerialize(using = DateSerializer.class, include = Inclusion.NON_NULL) @JsonDeserialize(using = DateDeserializer.class) private Date cycTime; // The period that the cycle lasts. private Integer roleType; // The role of the node, for example, a leaf node or a non-leaf n ode. private Integer dependentType; // The dependency type of the node. @JsonSerialize(using = DateSerializer.class, include = Inclusion.NON_NULL) @JsonDeserialize(using = DateDeserializer.class) private Date deployDate; // The date when the node instance was deployed. private String nodeName; // The name of the node. private Integer rerunTimes; // The number of times the node is rerun. @JsonSerialize(using = DateSerializer.class, include = Inclusion.NON_NULL) @JsonDeserialize(using = DateDeserializer.class) private Date nodeModifyTime; // The time when the node was modified last time. @JsonSerialize(using = DateSerializer.class, include = Inclusion.NON_NULL) @JsonDeserialize(using = DateDeserializer.class) private Date refreshTime; @JsonSerialize(using = DateSerializer.class, include = Inclusion.NON_NULL) @JsonDeserialize(using = DateDeserializer.class) private Date delayExecTime; private Boolean rerunAble;
```

`i` `t`

```
Lit<T kRlti Dt>
```

`tT`

```
kRlti //Th
```

`t`

```
lti fth
```

`d` `i` `t` ests

```java
private List<TaskRelationDto> parentTaskRelations; // The parent relations of the node inst ance. private List<TaskRelationDto> childTaskRelations; // The child relations of the node instan ce. private Integer isRunOver;// Indicates whether the node instance has been run. private Long bizId; private List<MetaTable> parentOutputTabMetas; // The metadata of the table on which the nod e instance depends. private List<MetaTable> outputTabMetas; // The metadata of the output table of the node ins tance.
```

#### 5.39.3 DagEntity

```java
private String name; // The name of the workflow instance.
 private Integer type; // The type of the workflow instance.
 @JsonSerialize(using = DateSerializer.class, include = Inclusion.NON_NULL)
        @JsonDeserialize(using = DateDeserializer.class)
 private Date bizdate; // The date-based timestamp. This parameter must be specified for a
one-off node.
 private Long rootNodeId; // The ID of the root node.
 private List<Long> includeNodeIds = new ArrayList<Long>(); // The IDs of the whitelisted n
odes.
 private List<Long> excludeNodeIds = new ArrayList<Long>(); // The IDs of the blacklisted n
odes.
 @JsonSerialize(using = DateSerializer.class, include = Inclusion.NON_NULL)
        @JsonDeserialize(using = DateDeserializer.class)
 private Date startBizDate; // The start of the time period when the retroactive data gener
ation task runs.
 @JsonSerialize(using = DateSerializer.class, include = Inclusion.NON_NULL)
        @JsonDeserialize(using = DateDeserializer.class)
 private Date endBizDate; // The end of the time period when the retroactive data generatio
n task runs.
 private String bizBeginTime; // The start time of the hourly node, for example, 13:04:04.
 private String bizEndTime; // The end time of the hourly node, for example, 14:04:04.
 private Boolean isParallel; // Specifies whether the workflow instance to which the retroa
ctive data generation task belongs can be run concurrently.
 // ////////////////////////////////The preceding parameters are required for creating an a
d-hoc workflow.//////////////////////////////////////////
 private Long dagId; // The ID of the workflow instance.
 private Integer status; // The status of the workflow instance.
 @JsonSerialize(using = DateSerializer.class, include = Inclusion.NON_NULL)
        @JsonDeserialize(using = DateDeserializer.class)
 private Date gmtdate; // The date when the workflow instance was generated.
 @JsonSerialize(using = DateSerializer.class, include = Inclusion.NON_NULL)
        @JsonDeserialize(using = DateDeserializer.class)
 private Date startDate; // The date when the workflow instance starts.
 @JsonSerialize(using = DateSerializer.class, include = Inclusion.NON_NULL)
        @JsonDeserialize(using = DateDeserializer.class)
 private Date startTime; // The start of the time period when the workflow instance runs.
 @JsonSerialize(using = DateSerializer.class, include = Inclusion.NON_NULL)
        @JsonDeserialize(using = DateDeserializer.class)
 private Date finishTime; // The end of the time period when the workflow instance runs.
 private String rootTaskIds; // The IDs of instances that belong to the root node.
```

ests

```java
 private Long appId; // The ID of the workspace to which the workflow instance belongs.
 private Long parentDagId; // The ID of the parent workflow instance.
 private Long childDagId; // The ID of the child workflow instance.
 @JsonSerialize(using = DateSerializer.class, include = Inclusion.NON_NULL)
        @JsonDeserialize(using = DateDeserializer.class)
 private Date createTime; // The time when the workflow instance was created.
 private String createUser; // The user who created the workflow instance.
 @JsonSerialize(using = DateSerializer.class, include = Inclusion.NON_NULL)
        @JsonDeserialize(using = DateDeserializer.class)
 private Date modifyTime; // The time when the workflow instance was modified last time.
 private String modifyUser; // The user who modified the workflow instance last time.
 private Integer createStatus; // The status of the creation. Valid values: 1, 2, 3, and 4.
1: The instance is being initiated. 2: The instance is being created. 3: The instance is cr eated. 4: The instance failed to be created.
 private Long opSeq;
 private Integer dagNum;
 private Boolean isDependDaily = false; // Specifies whether the workflow instance depends
on an instance in the development environment.
```

#### 5.39.4 TaskStatus

Not_run (1, "The task is not running "), Wait_time (2, "The task is pending execution."), Wait_resource (3, "The task is waiting for resources."), RUNNING(4, "The task is running."), FAILURE(5, "An error occurred while the task is executed."), SUCCESS(6, "The task execution is completed.");

#### 5.39.5 Dagstatus

Created (1, "The DAG has been created."), RUNNING(4, "The DAG is running."), FAILURE(5, "An error occurred while the DAG is executed."), SUCCESS(6, "The DAG is executed.");

#### 5.39.6 ProgramType

IDE_SHELL(6), ODPS_SQL(10), ODPS_MR(11), POL_SYNC(23) Synchronization task

#### 5.39.7 CycleType

DAY(0), // Indicates cycles that are no shorter than one day. NOT_DAY(1), // Indicates cycles that are shorter than one day. NOT_DAY_SEQ(2); // The sequence number of each cycle that is shorter than one day. The cycles are arranged in an ordered array. ests

#### 5.39.8 DependencyType

NONE(0), // The node can be run without waiting for the previous cycle of a specified node is completed. USER_DEFINE(1), // The node is run only after the previous cycle of a custom node is completed. CHILD(2), // The node is run only after the previous cycle of its child nodes is completed. SELF(3); // The node is run only after its previous cycle is completed.

## 6 Java SDK

### 6.1 GetInstanceSummary

You can call this operation to query the information about instances of readers or writers based on the specified Apsara Stack tenant account ID.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to GetInstanceSummary. |
| Aliuid | String | Yes | The ID of the Apsara Stack tenant account ID. |
| EndTime | String | Yes | The end time of time range where this operation is performed. Specify the time in the yyyy-mm-dd format. |
| StartTime | String | Yes | The start time of time range where this operation is performed. Specify the time in the yyyy-mm-dd format. |
| Type | String | Yes | Specifies whether to return the instance information about readers or writers. A value of 1 indicates that the result is the information about instances of readers. A value of 2 indicates that the result is the information about instances of writers. |

| Parameter | Type | Description |
|---|---|---|
| Data | Long | The information about instances. |
| ErrCode | Long | The error code. |

| Developer Guide·Java SDK |   | DataWork |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| ErrMsg | String | The error message. |
| RequestId | String | The ID of the request. |

Sample request

```
http(s)://[Endpoint]/? Action=GetInstanceSummary &Aliuid=178*****2537 &EndTime=2019-02-21 &StartTime=2019-02-21 &Type=1 &<Common request parameters>
```

Sample response

```json
"Data": [ "InstanceCnt": 17, "AliyunKp": "1782****62537", "PluginName": "mysql", "TotalRecords": 4255624, "TotalBytes": 266409932
```

`],`

```json
"ErrMsg": "success", "RequestId": "e19f8502-76d2-4cb1-ab54-b93013cfad17", "ErrCode": 0
```

### 6.2 AddResGroupGateWay

You can call this operation to add a gateway to a resource group.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to AddResGroupGateWay. |
| BaseId | String | Yes | The ID of the Apsara Stack account. |
| Identifier | String | Yes | The identifier of the resource group. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| Memory | Integer | Yes | The memory size of the resource group. |
| NodeAddress | String | Yes | The IP address of the node that runs the gateway. |
| NodeName | String | Yes | The name of the node that runs the gateway. |
| ProjectId | Long | Yes | The ID of the DataWorks workspace. |
| TenantId | Long | Yes | The ID of the tenant. |
| VCpu | Integer | Yes | The number of cores in the vCPU of the gateway. |

| Parameter | Type | Description |
|---|---|---|
| Data | Boolean | The returned data. Indicates whether the operation is successful. |
| ErrCode | Long | The error code. |
| ErrMsg | String | The error message. |
| RequestId | String | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/? Action=AddResGroupGateWay &BaseId=1486***73474 &Identifier=3907f9a58******6b2506 &Memory=3 &NodeAddress=12.12.12.12 &NodeName=hostname &ProjectId=75059 &TenantId=2678***8690 &VCpu=8 &<Common request parameters>
```

Sample success responses

```json
    "requestId": "0bc1748b*****493e5f15",
    "data": true,
    "errMsg": "success",
    "errCode": 0
```

### 6.3 CreateConnection

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateConnection. |
| Connection | String | Yes | The connection string of the data source. |
| Name | String | Yes | The name of the data source. |
| ProjectId | Long | Yes | The ID of the DataWorks workspace. |
| Type | String | Yes | The type of the data source. |
| EnvType | Integer | No | The type of the environment. Valid values: 0 and 1. The value 0 specifies the development environment. The value 1 specifies the production environment. |
| TenantId | Long | No | The ID of the tenant. |
| Shared | Boolean | No | Specifies whether the data source is shared or not. |
| Description | String | No | The description of the data source. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| SubType | String | No | The subtype of the data source. Currently, only MySQL is supported. |

| Parameter | Type | Description |
|---|---|---|
| Data | Long | The returned data. If the operation is successful, it returns the ID of the connected data source. If the operation fails, it returns null. |
| ErrCode | Long | The error code. |
| ErrMsg | String | The error message. |
| RequestId | String | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/? Action=CreateConnection &<Common request parameters>
```

### 6.4 CreateDag

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateDag. |
| AccountId | String | Yes | The ID of the account that is assigned by the scheduling system to call this operation. |
| AccountPwd | String | Yes | The password of the account that is assigned by the scheduling system to call this operation. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| ClientName | String | Yes | The name of the client that is assigned by the scheduling system to call this operation. |
| BaseId | String | Yes | The ID of the Apsara Stack account that you use to call this operation. |
| DagModifyDto | String | Yes | { "executeMethod": "CREATE DAG", _ "name": "test create dag" _ _ , "type": 3, "includeNodeIds": [3231], "excludeNodeIds": [], "rootNodeId": 3231, "startBizDate": "2018-07-08 00:00:00", "endBizDate": "2018-07-09 00:00:00", "isParallel": false } |

| Parameter | Type | Required | Description |
|---|---|---|---|
| ProjectEnv | String | Yes | The type of the environment. Valid values: DEV and PROD. The value DEV specifies the development environment. The value PROD specifies the production environment. |
| TenantId | Long | Yes | The ID of the tenant. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. If an error occurs, send the request ID to the developers of the scheduling system for troubleshooting. |
| ReturnCode | String | The return code. The value 0 indicates that the operation is successful. |
| ReturnErrorSolution | String | The solution to resolve the issue. |
| ReturnMessage | String | The error message. |
| ReturnValue | Long | The value of the DagID parameter. |

Sample success responses

```json
    "returnCode":"0",
    "returnErrorSolution":"",
    "returnMessage":"",
    "requestId":"740ded9e-f6f5-4fde-a419-9b54***e8",
    "returnValue":300000119,
    "success":true
```

### 6.5 CreateDQCEntity

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateDQCEntity. |
| EnvType | String | Yes | The type of the computing engine. |
| MatchExpression | String | Yes | The name of the partition filter expression. |
| ProjectName | String | Yes | The name of the MaxCompute project. |
| TableName | String | Yes | The name of the table. |

| Parameter | Type | Description |
|---|---|---|
| ReturnCode | String | The return code. The value 0 indicates that the operation is successful. Other values indicate that the operation failed. |
| ReturnValue | Integer | The ID of the partition filter expression that has been created. |

Sample requests

```
/? Action=CreateDQCEntity &EntityLevel=0 &EnvType=odps &MatchExpression=ds=${yyyymmdd-1} &ProjectName=autotest &TableName=test_dqc_decimal_1119_2 &<Common request parameters>
```

Sample success responses

```json
"ReturnCode": "0", "ReturnValue": 4003923
```

### 6.6 CreateDQCFollower

You can call this operation to subscribe to messages from Data Quality. The messages are generated for the partitions that are specified by the partition filter expression. The methods of receiving messages include the emails, Short Message Service (SMS), and DingTalk. Not e To receive messages by using DingTalk, specify a DingTalk group that receives the messages on the Robot Management page and add a chatbot. After you add the chatbot, a webhook URL for the chatbot is automatically generated. You can then enable Data Quality to send HTTP POST requests to this URL to send messages to the specified DingTalk group.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateDQCFollower. |
| ProjectName | String | No | The name of the MaxCompute project. |
| Follower | String | No | The object of receiving the subscribed messages. If you want to receive the messages by using emails or the SMS, specify your employee ID. If you want to receive the messages by using DingTalk, specify the webhook URL. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| AlarmMode | Integer | No | The method of receiving alerts and notifications. The value 1 specifies that you receive alerts and notifications by using emails. The value 2 specifies that you receive alerts and notifications by using emails and the SMS. The value 3 specifies that you receive alerts and notifications from the specified DingTalk group by using the webhook URL. The value 4 specifies that you receive alerts and notifications from the specified DingTalk group and mention all members in the group. |
| EntityId | Long | No | The ID of the partition filter expression. |

| Parameter | Type | Description |
|---|---|---|
| ReturnCode | String | The return code. |
| ReturnValue | Integer | The ID of the subscription. |

Sample requests

```
/? Action=CreateDQCFollower &AlarmMode=2 &EntityId=4003922 &Follower=50624 &ProjectName=autotest &<Common request parameters>
```

Sample success responses

```json
"ReturnValue": 1726, "ReturnCode": "0"
```

### 6.7 CreateDQCRule

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to CreateDQCRule. |
| EntityId | Integer | Yes | The ID of the partition expression. |
| ProjectName | String | Yes | The name of the MaxCompute project. |
| Rules | String | Yes | The rules to be created. |

| Parameter | Type | Description |
|---|---|---|
| ReturnCode | String | The return code. |
| ReturnValue | Boolean | Indicates whether the specified rules have been created. |

Sample request

```json
/? EntityId=4003922 &ProjectName=autotest &Rules={ "addTemplateRules":[{ "property":"table_count", "propertyType":"table", "blockType":"0", "templateId":"7", "trend":"abs", "warningThreshold":10, "critical Threshold":50, "ruleType":"0" }], "addSelfserviceRules":[{ "property":"table_count", "propertyType":"table", "blockType":"0", "methodName":"count/table_count", "w hereCondition":"id>100", "checker":"9", "trend":"abs", "operator":">", "expectValue":0, "comment":"This is a rule.", "ruleType":"1", "warningThreshold":null, "criticalThreshold":null}], "envType":"o dps", "projectName":"autotest", "entityId":4003922} &<Common request parameters>
```

Sample response

```json
"ReturnValue": true, "ReturnCode": "0"
```

### 6.8 CreateManualDag

You can call this API operation in OpenAPI Explorer for debugging. OpenAPI Explorer allows you to call API operations through its web interface. It automatically generates SDK code examples based on the specified request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|

| Parameter |   | Type |   | Required |   |   |   | Description |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Action |   | String |   | Yes |   |   |   | The operation that you want to perform. Set this parameter to CreateManualDag. |   |   |   |
| Bizdate |   | String |   | Yes |   |   |   | The data timestamp. Specify the date-based timestamp of data to be processed, such as 2019-04-03 00:00:00. |   |   |   |
| FlowName |   | String |   | Yes |   |   |   | The name of the manually triggered workflow. |   |   |   |
| ProjectName |   | String |   | Yes |   |   |   | The name of the DataWorks workspace. |   |   |   |
| DagPara |   | String |   | No |   |   |   | The workflow parameters in the format of { "key1": |   |   |   |
|   |   |   |   |   |   |   |   |   | { "key1": |   |   |
|   |   |   |   |   |   |   |   | "val1", "key2": |   |   |   |
|   |   |   |   |   |   |   |   | "val2" } |   |   |   |
| NodePara |   | String |   | No |   |   |   | The node parameters in the format of Map<Long, String>. Long indicates the node ID, and String indicates a string of key-value pairs, such as { |   |   |   |
|   |   |   |   |   |   |   |   |   |   | { |   |
|   |   |   |   |   |   |   |   | "1232234255": |   |   |   |
|   |   |   |   |   |   |   |   | "key1=val1 |   |   |   |
|   |   |   |   |   |   |   |   | key2=val2", |   |   |   |
|   |   |   |   |   |   |   |   | "321231412": |   |   |   |
|   |   |   |   |   |   |   |   | "key1=val1 |   |   |   |
|   |   |   |   |   |   |   |   | key2=val2" } |   |   |   |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| ReturnCode | String | The return code. |
| ReturnErrorSolution | String | The solution to resolve the issue. |
| ReturnMessage | String | The error message. |

| Parameter | Type | Description |
|---|---|---|
| ReturnValue | Long | The value of the dagId parameter. |

Sample response

```json
"RequestId": "****", "ReturnCode": 0, "ReturnMessage": "", "ReturnErrorSolution": "", "ReturnValue": 123142124124
```

### 6.9 CreateMetaSpiderJob

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateMetaSpiderJob. |
| BaseId | String | Yes | The ID of the Apsara Stack account. |
| DatasourceId | Long | Yes | The ID of the data source. |
| ProjectId | Long | Yes | The ID of the DataWorks workspace. |
| SpiderConfig | String | Yes | The configuration information about the job to create. |
| TenantId | Long | Yes | The ID of the tenant. |
| SpiderCron | String | No | The CRON expression of the job to create. |

| Parameter | Type |
|---|---|
| Data | Boolean |
| ErrCode | Long |

| ataWorks | Developer Guide·Java SD |
|---|---|
| Parameter | Type |
| ErrMsg | String |
| RequestId | String |

Sample requests

```
http(s)://[Endpoint]/? Action=CreateMetaSpiderJob &<Common request parameters>
```

### 6.10 CreateResGroup

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateResGroup. |
| BaseId | String | Yes | The ID of the Apsara Stack account. |
| Name | String | Yes | The name of the resource group to create. |
| ProjectId | Long | Yes | The ID of the DataWorks workspace. |
| ProjectIds | JSON | Yes | The IDs of the DataWorks workspaces. |
| TenantId | Long | Yes | The ID of the tenant. |

| Parameter | Type | Description |
|---|---|---|
| Data | Object | The returned data. |
| ErrCode | Long | The error code. |
| ErrMsg | String | The error message. |
| RequestId | String | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/? Action=CreateResGroup &BaseId=1486821399873474 &Name=test20190509 &ProjectId=75059 &ProjectIds=["75059"] &TenantId=267883377178690 &<Common request parameters>
```

Sample success responses

```json
"requestId": "0a98***e0b1b", "data": { "id": 334603176233473, "identifier": "e86f****64dde44", "name": "test1234", "nick": null, "type": "DI", "mode": "ISOLATE", "tenantId": 267883377178690, "enableKp": false, "cluster": "e86f1****64dde44", "quota": null, "isDefault": false, "sequence": null, "action": "create", "specs": { "resourceGroupTag": "1"
```

`},`

```json
"errMsg": "success", "errCode": 0
```

### 6.11 DeleteConnections

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteConnections. |
| ConnectionIds | String | Yes | The IDs of the data sources to delete. |

| Parameter | Type | Description |
|---|---|---|
| Data | Boolean | Indicates whether the specified data resources have been deleted. |
| ErrCode | Long | The error code. |
| ErrMsg | String | The error message. |
| RequestId | String | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/? Action=DeleteConnections &<Common request parameters>
```

### 6.12 DeleteDQCEntity

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteDQCEntity. |
| EntityId | Long | Yes | The ID of the partition filter expression. |
| EnvType | String | Yes | The type of the computing engine. Supported computing engines are MaxCompute, Hive, and Realtime Compute. |
| ProjectName | String | Yes | The name of the MaxCompute project. |

| Parameter | Type | Description |
|---|---|---|
| ReturnCode | String | The return code. |
| ReturnValue | Boolean | Indicates whether the operation is successful. |

Sample requests

```
/? Action=DeleteDQCEntity &EntityId=4003922 &EnvType=odps &ProjectName=autotest &<Common request parameters>
```

Sample success responses

```json
"ReturnValue": true, "ReturnCode": "0"
```

### 6.13 DeleteDQCFollower

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DeleteDQCFollower. |
| ProjectName | Long | No | The name of the MaxCompute project. |
| Id | Long | No | The ID of the subscription. |

| Parameter | Type | Description |
|---|---|---|
| ReturnCode | String | The return code. |
| ReturnValue | Boolean | Indicates whether the operation is successful. |

Sample request

```
/? Action=DeleteDQCFollower &Id=1724 &ProjectName=autotest &<Common request parameters>
```

Sample response

```json
"ReturnValue": true, "ReturnCode": "0"
```

### 6.14 DeleteDQCRule

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteDQCRule. |
| ProjectName | String | No | The name of the MaxCompute project. |
| Id | Long | No | The ID of the Data Quality check (DQC) rule to delete. |

| Parameter | Type | Description |
|---|---|---|
| ReturnCode | String | The return code. |
| ReturnValue | Boolean | Indicates whether the specified rule has been deleted. |

Sample requests

```
/? Action=DeleteDQCRule &Id=279580661 &ProjectName=autotest &<Common request parameters>
```

Sample success responses

```json
"ReturnCode": "0", "ReturnValue": true
```

### 6.15 DeleteProjectResGroup

Requestparameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteProjectResGroup. |
| BaseId | String | Yes | The ID of the Apsara Stack account. |
| Identifier | String | Yes | The identifier of the resource group. |
| ProjectId | Long | Yes | The ID of the DataWorks workspace. |
| ResGroupId | Long | Yes | The ID of the resource group. |
| TenantId | Long | Yes | The ID of the tenant. |

| Parameter | Type | Description |
|---|---|---|
| Data | Boolean | Indicates whether the specified resource group has been deleted. Valid values: true and false. The value true indicates that the resource group has been deleted. The value false indicates that the resource group failed to be deleted. |
| ErrCode | Long | The error code. |
| ErrMsg | String | The error message. |
| RequestId | String | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/? Action=DeleteProjectResGroup &BaseId=1486821399873474 &Identifier=e86f1a3ba2ca451eab8851ed564dde44 &ProjectId=75059 &ResGroupId=334603176233473 &TenantId=267883377178690 &<Common request parameters>
```

Sample success responses

```json
"requestId": "0bc1746d15574010397142703e6afb", "data": true, "errMsg": "success", "errCode": 0
```

### 6.16 DeleteResGroupGateWay

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteResGroupGateWa y. |
| BaseId | String | Yes | The ID of the Apsara Stack account. |
| Identifier | String | Yes | The identifier of the resource group. |
| NodeName | String | Yes | The name of the gateway. |
| ProjectId | Long | Yes | The ID of the DataWorks workspace. |
| TenantId | Long | Yes | The ID of the tenant. |

| Parameter | Type | Description |
|---|---|---|
| Data | Boolean | Indicates whether the specified gateway has been deleted. |
| ErrCode | Long | The error code. |
| ErrMsg | String | The error message. |
| RequestId | String | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/? Action=DeleteResGroupGateWay &BaseId=1486821399873474 &Identifier=3907f9a5832942f9b63b0908476b2506 &NodeName=hostname &ProjectId=75059 &TenantId=267883377178690 &<Common request parameters>
```

Sample success responses

```json
"requestId": "0bc1748b15574028120678613e5f16", "data": true, "errMsg": "success", "errCode": 0
```

### 6.17 GetDagDetail

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GetDagDetail. |
| AccountId | String | Yes | The ID of the account that is assigned by the scheduling system to call this operation. |
| AccountPwd | String | Yes | The password of the account that is assigned by the scheduling system to call this operation. |
| ClientName | String | Yes | The name of the client that is assigned by the scheduling system to call this operation. |
| BaseId | String | Yes | The ID of the Apsara Stack account that you use to call this operation. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| ProjectEnv | String | Yes | The type of the environment. Valid values: DEV and PROD. The value DEV specifies the development environment. The value PROD specifies the production environment. |
| TenantId | Long | Yes | The ID of the tenant. |
| DagId | Long | No | The ID of the workflow instance. |

| Parameter | Type | Description |
|---|---|---|
| Count | Integer | The number of the returned workflow instances. |
| RequestId | String | The ID of the request. |
| ReturnCode | String | The return code. |
| ReturnMessage | String | The error message. |
| ReturnErrorSolution | String | The solution to resolve the issue. |
| ReturnValue | Long | The returned data. |

Sample success responses

```json
"returnCode": "0", "returnErrorSolution": "", "returnMessage": "", "requestId": "14***4-e059-4bf4-a2c1-***323f", "returnValue": [ "name": "Retroactive Instance Test 15", "type": 3, "rootNodeId": 1, "status": 6, "flowId": 1
```

`],`

```json
"success": true
```

### 6.18 GetDataServiceApiDetail

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GetDataServiceApiDetail . |
| ApiId | Long | Yes | The ID of the API to query. |
| Verbose | Long | No | Specifies whether to return the details of the API. |

| Parameter | Type | Description |
|---|---|---|
| Data | Boolean | The details of the DataService API. |
| ErrCode | Integer | The error code. |
| ErrMsg | String | The error message. |
| RequestId | String | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/? Action=GetDataServiceApiDetail &<Common request parameters>
```

### 6.19 GetDataServiceAppDetail

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GetDataServiceAppDetai l. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| BaseId | String | Yes | The ID of the Apsara Stack account. |
| ProjectId | Long | Yes | The ID of the DataWorks workspace. |

| Parameter | Type | Description |
|---|---|---|
| Data | Boolean | The details of the DataService application. |
| ErrCode | Integer | The error code. |
| ErrMsg | String | The error message. |
| RequestId | String | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/? Action=GetDataServiceAppDetail &<Common request parameters>
```

### 6.20 GetDefaultTenant

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GetDefaultTenant. |

| Parameter | Type | Description |
|---|---|---|
| ErrCode | Integer | The error code. |
| ErrMsg | String | The error message. |
| RequestId | String | The ID of the request. |
| Tenant | String | The information about the tenant. |

| Developer Guide·Java SDK |   | DataWork |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| TenantCode | String | The code of the tenant. |
| TenantOwnerBaseId | String | The ID of the Apsara Stack account of the tenant owner. |

Sample requests

```
http(s)://[Endpoint]/? Action=GetDefaultTenant &<Common request parameters>
```

### 6.21 GetDQCEntity

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GetDQCEntity. |
| ProjectName | String | No | The name of the DataWorks workspace. |
| TableName | String | No | The name of the table. |
| EnvType | String | No | The type of the computing engine. Supported computing engines are MaxCompute, Hive, and Realtime Compute. |
| MatchExpression | String | No | The partition filter expression. If you do not specify this parameter, the operation returns all the partition filter expressions of the specified table. |

| Parameter | Type | Description |
|---|---|---|
| ReturnCode | String | The return code. |

| Parameter | Type | Description |
|---|---|---|
| ReturnValue | String | The partition filter expressions that were queried. |

Sample requests

```
http(s)://[Endpoint]/? Action=GetDQCEntity &EnvType=odps &MatchExpression=dt=${yyyymmdd-1} &ProjectName=autotest &TableName=test_dqc_decimal_1119_2 &<Common request parameters>
```

Sample success responses

```json
"ReturnValue": { "Entity": [ "EntityLevel": 0, "ProjectName": "autotest", "MatchExpression": "dt=${yyyymmdd-3}", "Followers": "050624", "OnDuty": "050624", "Sql": 0, "GmtCreate": "2018-11-26 15:06:32", "EnvType": "odps", "Task": 0, "HasRelativeNode": false, "Id": 4003918, "TableName": "test_dqc_decimal_1119_2", "GmtModify": "2018-11-26 15:06:32"
```

`},`

```json
"EntityLevel": 0, "ProjectName": "autotest", "MatchExpression": "dt=${yyyymmdd-1}", "Followers": "050624", "OnDuty": "050624", "Sql": 0, "GmtCreate": "2018-11-26 22:31:13", "EnvType": "odps", "Task": 0, "HasRelativeNode": false, "Id": 4003922, "TableName": "test_dqc_decimal_1119_2", "GmtModify": "2018-11-26 22:31:13"
```

`},`

```json
"EntityLevel": 0, "ProjectName": "autotest", "MatchExpression": "dt=${yyyymmdd-2}", "Followers": "050624", "OnDuty": "050624", "Sql": 0, "GmtCreate": "2018-11-26 23:18:34", "EnvType": "odps", "Task": 0, "HasRelativeNode": false, "Id": 4003923, "TableName": "test_dqc_decimal_1119_2", "GmtModify": "2018-11-26 23:18:34"
```

`]` `},`

```json
"ReturnCode": "0"
```

### 6.22 GetDQCFollower

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GetDQCFollower. |
| ProjectName | String | No | The name of the DataWorks workspace. |
| EntityId | Long | No | The ID of the partition filter expression. |

| Parameter | Type | Description |
|---|---|---|
| ReturnCode | String | The return code. |
| ReturnValue | String | The objects and applications that subscribe to the messages from Data Quality. |

Sample requests

```
http(s)://[Endpoint]/? Action=GetDQCFollower &EntityId=4003922 &ProjectName=odps &<Common request parameters>
```

Sample success responses

```json
"ReturnCode": "0", "ReturnValue": { "Follower": [ "ProjectName": "autotest", "AlarmMode": 1, "Follower": "050624", "Id": 1726, "TableName": "test_dqc_decimal_1119_2", "EntityId": "4003922"
```

`]`

### 6.23 GetDQCRule

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GetDQCRule. |
| ProjectName | String | No | The name of the DataWorks workspace. |
| EntityId | Long | No | The ID of the partition filter expression. |

| Parameter | Type | Description |
|---|---|---|
| ReturnCode | String | The return code. |
| ReturnValue | List | The details of the rules. |

Sample requests

```
http(s)://[Endpoint]/? Action=GetDQCRule &EntityId=4003922 &ProjectName=autotest &<Common request parameters>
```

Sample success responses

```json
"ReturnValue": { "TemplateRules": { "TemplateRule": [ "TemplateName": "SQL task table rows, 1,7, 30 days fluctuation test", "ProjectName": "autotest", "MatchExpression": "dt=${yyyymmdd-1}", "WarningThreshold": "40", "RuleCheckerRelationId": 1008005, "RuleType": 0, "MethodId": 8, "CriticalThreshold": "80", "FixCheck": false, "OnDuty": "050624", "Property": "table_count", "TemplateId": 7,
```

```json
"PropertyKey": "table_count", "MethodName": "table_count", "HistoryWarningThreshold": "history max:40%,history min:10%", "BlockType": 1, "CheckerId": 7, "TableName": "test_dqc_decimal_1119_2", "Id": 279580663, "EntityId": 4003922, "HistoryCriticalThreshold": "history max:80%,history min:50%", "Trend": "abs"
```

`},`

```json
"TemplateName": "SQL task table rows, 1,7, 30 days fluctuation test", "ProjectName": "autotest", "MatchExpression": "dt=${yyyymmdd-1}", "WarningThreshold": "10", "RuleCheckerRelationId": 1008007, "RuleType": 0, "MethodId": 8, "CriticalThreshold": "50", "FixCheck": false, "OnDuty": "050624", "Property": "table_count", "TemplateId": 7, "PropertyKey": "table_count", "MethodName": "table_count", "HistoryWarningThreshold": "history max:10%,history min:10%", "BlockType": 0, "CheckerId": 7, "TableName": "test_dqc_decimal_1119_2", "Id": 279580665, "EntityId": 4003922, "HistoryCriticalThreshold": "history max:50%,history min:50%", "Trend": "abs"
```

`},`

```json
"TemplateName": "SQL task table rows, 1,7, 30 days fluctuation test", "ProjectName": "autotest", "MatchExpression": "dt=${yyyymmdd-1}", "WarningThreshold": "10", "RuleCheckerRelationId": 1008009, "RuleType": 0, "MethodId": 8, "CriticalThreshold": "50", "FixCheck": false, "OnDuty": "050624", "Property": "table_count", "TemplateId": 7, "PropertyKey": "table_count", "MethodName": "table_count", "HistoryWarningThreshold": "history max:10%,history min:10%", "BlockType": 0, "CheckerId": 7, "TableName": "test_dqc_decimal_1119_2", "Id":279580667
```

```json
"Id": 279580667, "EntityId": 4003922, "HistoryCriticalThreshold": "history max:50%,history min:50%", "Trend": "abs"
```

`]` `},`

```json
"SelfserviceRules": { "SelfserviceRule": [ "ProjectName": "autotest", "MatchExpression": "dt=${yyyymmdd-1}", "Checker": 9, "RuleCheckerRelationId": 1008004, "WhereCondition": "id>100", "RuleType": 1, "MethodId": 21, "FixCheck": true, "CheckerName": "compared with a fixed value", "OnDuty": "050624", "Property": "table_count", "PropertyKey": "table_count", "MethodName": "count/table_count", "BlockType": 0, "TableName": "test_dqc_decimal_1119_2", "Id": 279580662, "CheckerId": 6, "EntityId": 4003922, "Trend": "abs"
```

`},`

```json
"ProjectName": "autotest", "MatchExpression": "dt=${yyyymmdd-1}", "Checker": 9, "RuleCheckerRelationId": 1008006, "WhereCondition": "id>100", "RuleType": 1, "MethodId": 21, "FixCheck": true, "CheckerName": "compared with a fixed value", "OnDuty": "050624", "Property": "table_count", "PropertyKey": "table_count", "MethodName": "count/table_count", "BlockType": 0, "TableName": "test_dqc_decimal_1119_2", "Id": 279580664, "CheckerId": 6, "EntityId": 4003922, "Trend": "abs"
```

`},`

```json
"ProjectName": "autotest", "MatchExpression": "dt=${yyyymmdd-1}", "Checker":9,
```

```json
Checker: 9, "RuleCheckerRelationId": 1008008, "WhereCondition": "id>100", "RuleType": 1, "MethodId": 21, "FixCheck": true, "CheckerName": "compared with a fixed value", "OnDuty": "050624", "Property": "table_count", "PropertyKey": "table_count", "MethodName": "count/table_count", "BlockType": 0, "TableName": "test_dqc_decimal_1119_2", "Id": 279580666, "CheckerId": 6, "EntityId": 4003922, "Trend": "abs"
```

`},`

```json
"ProjectName": "autotest", "MatchExpression": "dt=${yyyymmdd-1}", "Checker": 9, "RuleCheckerRelationId": 1008010, "WhereCondition": "id>100", "RuleType": 1, "MethodId": 21, "FixCheck": true, "CheckerName": "compared with a fixed value", "OnDuty": "050624", "Property": "table_count", "PropertyKey": "table_count", "MethodName": "count/table_count", "BlockType": 0, "TableName": "test_dqc_decimal_1119_2", "Id": 279580668, "CheckerId": 6, "EntityId": 4003922, "Trend": "abs"
```

`]` `},`

```json
"ReturnCode": "0"
```

### 6.24 GetNodeDetail

| Parameter | Type | Required | Description |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GetNodeDetail. |
| AccountId | String | Yes | The ID of the account that is assigned by the scheduling system to call this operation. |
| AccountPwd | String | Yes | The password of the account that is assigned by the scheduling system to call this operation. |
| BaseId | String | Yes | The ID of the Apsara Stack account that you use to call this operation. |
| ClientName | String | Yes | The name of the client that is assigned by the scheduling system to call this operation. |
| NodeId | Long | Yes | The ID of the node to query. |
| ProjectEnv | String | Yes | The type of the environment. Valid values: DEV and PROD. The value DEV specifies the development environment. The value PROD specifies the production environment. |
| TenantId | Long | Yes | The ID of the tenant. |
| IsDetail | Boolean | No | Specifies whether to return the detailed information about this node. Valid values: true and false. |

| Parameter | Type | Description |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. If an error occurs, send the request ID to the developers of the scheduling system for troubleshooting. |
| ReturnCode | String | The return code. The value 0 indicates that the operation is successful. |
| ReturnErrorSolution | String | The solution to resolve the issue. |
| ReturnMessage | String | The error message. |
| ReturnValue | String | None |

Sample requests

```
http(s)://[Endpoint]/? Action=GetNodeDetail &EntityId=4003922 &ProjectName=autotest &<Common request parameters>
```

Sample success responses

```json
"ReturnValue": { "TemplateRules": { "TemplateRule": [ "TemplateName": "SQL task table rows, 1,7, 30 days fluctuation test", "ProjectName": "autotest", "MatchExpression": "dt=${yyyymmdd-1}", "WarningThreshold": "40", "RuleCheckerRelationId": 1008005, "RuleType": 0, "MethodId": 8, "CriticalThreshold": "80", "FixCheck": false, "OnDuty": "050624", "Property": "table_count", "TemplateId": 7, "PropertyKey": "table_count", "MethodName": "table_count", "HistoryWarningThreshold": "history max:40%,history min:10%", "BlockType": 1, "CheckerId": 7, "TableName": "test_dqc_decimal_1119_2", "Id": 279580663, "EntityId": 4003922, "HistoryCriticalThreshold": "history max:80%,history min:50%", "Trend": "abs"
```

`},`

```json
"TemplateName": "SQL task table rows, 1,7, 30 days fluctuation test", "ProjectName": "autotest", "MatchExpression": "dt=${yyyymmdd-1}", "WarningThreshold": "10", "RuleCheckerRelationId": 1008007, "RuleType": 0, "MethodId": 8, "CriticalThreshold": "50", "FixCheck": false, "OnDuty": "050624", "Property": "table_count", "TemplateId": 7, "PropertyKey": "table_count", "MethodName": "table_count", "HistoryWarningThreshold": "history max:10%,history min:10%", "BlockType": 0, "CheckerId": 7, "TableName": "test_dqc_decimal_1119_2", "Id": 279580665, "EntityId": 4003922, "HistoryCriticalThreshold": "history max:50%,history min:50%", "Trend": "abs"
```

`},`

```json
"TemplateName": "SQL task table rows, 1,7, 30 days fluctuation test", "ProjectName": "autotest", "MatchExpression": "dt=${yyyymmdd-1}", "WarningThreshold": "10", "RuleCheckerRelationId": 1008009, "RuleType": 0, "MethodId": 8, "CriticalThreshold": "50", "FixCheck": false, "OnDuty": "050624", "Property": "table_count", "TemplateId": 7, "PropertyKey": "table_count", "MethodName": "table_count", "HistoryWarningThreshold": "history max:10%,history min:10%", "BlockType": 0, "CheckerId": 7, "TableName": "test_dqc_decimal_1119_2", "Id": 279580667, "EntityId": 4003922, "HistoryCriticalThreshold": "history max:50%,history min:50%", "Trend": "abs"
```

`]` `},`

```json
"SelfserviceRules": { "SelfserviceRule": [
```

```json
"ProjectName": "autotest", "MatchExpression": "dt=${yyyymmdd-1}", "Checker": 9, "RuleCheckerRelationId": 1008004, "WhereCondition": "id>100", "RuleType": 1, "MethodId": 21, "FixCheck": true, "CheckerName": "compared with a fixed value", "OnDuty": "050624", "Property": "table_count", "PropertyKey": "table_count", "MethodName": "count/table_count", "BlockType": 0, "TableName": "test_dqc_decimal_1119_2", "Id": 279580662, "CheckerId": 6, "EntityId": 4003922, "Trend": "abs"
```

`},`

```json
"ProjectName": "autotest", "MatchExpression": "dt=${yyyymmdd-1}", "Checker": 9, "RuleCheckerRelationId": 1008006, "WhereCondition": "id>100", "RuleType": 1, "MethodId": 21, "FixCheck": true, "CheckerName": "compared with a fixed value", "OnDuty": "050624", "Property": "table_count", "PropertyKey": "table_count", "MethodName": "count/table_count", "BlockType": 0, "TableName": "test_dqc_decimal_1119_2", "Id": 279580664, "CheckerId": 6, "EntityId": 4003922, "Trend": "abs"
```

`},`

```json
"ProjectName": "autotest", "MatchExpression": "dt=${yyyymmdd-1}", "Checker": 9, "RuleCheckerRelationId": 1008008, "WhereCondition": "id>100", "RuleType": 1, "MethodId": 21, "FixCheck": true, "CheckerName": "compared with a fixed value", "OnDuty": "050624", "Property": "table_count", "PropertyKey": "table_count",
```

`/`

```json
"MethodName": "count/table_count", "BlockType": 0, "TableName": "test_dqc_decimal_1119_2", "Id": 279580666, "CheckerId": 6, "EntityId": 4003922, "Trend": "abs"
```

`},`

```json
"ProjectName": "autotest", "MatchExpression": "dt=${yyyymmdd-1}", "Checker": 9, "RuleCheckerRelationId": 1008010, "WhereCondition": "id>100", "RuleType": 1, "MethodId": 21, "FixCheck": true, "CheckerName": "compared with a fixed value", "OnDuty": "050624", "Property": "table_count", "PropertyKey": "table_count", "MethodName": "count/table_count", "BlockType": 0, "TableName": "test_dqc_decimal_1119_2", "Id": 279580668, "CheckerId": 6, "EntityId": 4003922, "Trend": "abs"
```

`]` `},`

```json
"ReturnCode": "0"
```

### 6.25 GetNodeUpdateStatus

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GetNodeUpdateStatus. |
| AccountId | String | No | The ID of the account that is assigned by the scheduling system to call this operation. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| AccountPwd | String | No | The password of the account that is assigned by the scheduling system to call this operation. |
| ClientName | String | No | The name of the client that is assigned by the scheduling system to call this operation. |
| BaseId | String | No | The ID of the Apsara Stack account that you use to call this operation. |
| RequestId | String | No | The ID of the request. You can use this ID to call the ModifyNode operation to modify a node. The ModifyNode operation then returns this ID as the value of the ReturnValue response parameter. |
| TenantId | LONG | No | The ID of the tenant. |
| IsDetail | Boolean | No | Specifies whether to return the detailed information about the node update. Valid values: true and false. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. If an error occurs, send the request ID to the developers of the scheduling system for troubleshooting. |
| ReturnCode | String | The return code. The value 0 indicates that the operation is successful. |
| ReturnErrorSolution | String | The solution to resolve the issue. |
| ReturnMessage | String | The error message. |

| Parameter | Type | Description |
|---|---|---|
| ReturnValue | String | The value of the RequestId parameter. |

Sample success responses

```json
"returnCode": "0", "returnErrorSolution": "", "returnMessage": "", "requestId": "0bbaa24515574698398786934e12b8", "returnValue": { "requestId": "0a64886b-1d63-4e5c-ad3e-d4eda4c2381c", "createTime": 1555065345000, "name": "ide-base", "status": "SUCCESS", "isDetail": true, "flowId": 28620441, "executeDetails": [ "uniqueId": "9745681_2", "cloudUUID": 111164284, "executeStatus": "SUCCESS", "executeMsg": "success", "dagId": null
```

`},`

```json
"uniqueId": "9745682_5", "cloudUUID": 111001035, "executeStatus": "SUCCESS", "executeMsg": "success", "dagId": null
```

`},`

```json
"uniqueId": "9745683_9", "cloudUUID": 111087244, "executeStatus": "SUCCESS", "executeMsg": "success", "dagId": null
```

`},`

```json
"uniqueId": "9745680_12", "cloudUUID": 111087242, "executeStatus": "SUCCESS", "executeMsg": "success", "dagId": null
```

`},`

```json
"uniqueId": "9745680_12", "cloudUUID": 111087242, "executeStatus": "INIT", "executeMsg": null, "dagId": null
```

`]` `},`

```json
"success": true
```

### 6.26 GetResGroupAk

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to GetResGroupAk. |
| BaseId | String | Yes | The ID of the Apsara Stack tenant account. |
| Identifier | String | Yes | The identifier of the resource group. |
| ProjectId | Long | Yes | The ID of the DataWorks workspace. |
| TenantId | Long | Yes | The ID of the tenant. |

| Parameter | Type | Description |
|---|---|---|
| ErrCode | Long | The error code. |
| ErrMsg | String | The error message. |
| RequestId | String | The ID of the request. |

Sample request

```
http(s)://[Endpoint]/? Action=GetResGroupAk &BaseId=148****873474 &Identifier=3907f9****6b2506 &ProjectId=75059 &TenantId=2678***78690 &<Common request parameters>
```

Sample response

```json
"requestId": "0a98a368***97e56fd", "data": { "username": "zz_3907f9***08476b2506", "password": "vcn9******", "rank": 4, "ossBackUp": false, "callback": false, "callbackUrl": ""
```

`},`

```json
"errMsg": "success", "errCode": 0
```

### 6.27 GetResGroupGatewayList

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to GetResGroupGatewayLis t. |
| BaseId | String | Yes | The ID of the Apsara Stack account. |
| Identifier | String | Yes | The identifier of the resource group. |
| ProjectId | Long | Yes | The ID of the DataWorks workspace. |
| TenantId | Long | Yes | The ID of the tenant. |

| Parameter | Type | Description |
|---|---|---|
| Data | List | The returned data. |
| ErrCode | Long | The error code. |
| ErrMsg | String | The error message. |
| RequestId | String | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/? Action=GetResGroupGatewayList &BaseId=1486****73474 &Identifier=3907f9a5******76b2506 &ProjectId=75059 &TenantId=2678****78690 &<Common request parameters>
```

Sample success responses

```json
"requestId": "0a98a35415574015996432719e2c97", "data": [{
    "clusterName": "3907f9a5832942f9b63b0908476b2506",
    "nodeName": "1.2.3.50",
    "nodeAddress": "1.2.3.50",
    "maxSlot": 32,
    "useSlot": 0,
    "state": 1,
    "live": false,
    "startMon": false,
    "regionId": 1,
    "nodeProperties": "{\"memory\":8,\"vCpu\":4}",
    "vCpu": 4,
    "memory": 8,
    "useDmu": 0
    }],
    "errMsg": "success",
    "errCode": 0
```

### 6.28 GetResGroupList

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GetResGroupList. |
| AlisaDetail | Boolean | Yes | Indicates whether to return the node details. |
| BaseId | String | Yes | The ID of the Apsara Stack account. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| Level | String | Yes | The level of the resource group. Valid values: project and tenant. The value project indicates that the resource group belongs to a project. The value tenant indicates that the resource group belongs to a tenant. |
| ProjectId | Long | Yes | The ID of the DataWorks workspace. |
| ResourceGroupType | String | Yes | The type of the resource group. |
| TenantId | Long | Yes | The ID of the tenant. |

| Parameter | Type | Description |
|---|---|---|
| Data | List | The returned data. |
| ErrCode | Long | The error code. |
| ErrMsg | String | The error message. |
| RequestId | String | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/? Action=GetResGroupList &AlisaDetail=true &BaseId=14*****3474 &Level=project &ProjectId=75059 &ResourceGroupType=di &TenantId=2678*****690 &<Common request parameters>
```

Sample success responses

```json
"requestId": "0a98a3****52214e2c97", "data": [{ "id": 29810****9522, "identifier": "group_267****178690", "name": "default resource group",
```

`g` `p``,`

```json
"nick": null, "isDefault": true, "networkType": null, "nodes": null, "maxSlot": null, "useSlot": null, "useDmu": null, "maxDmu": null, "projects": null, "resourceGroupType": null, "diResourceGroupType": 0, "buyType": "pay-as-you-go"
```

`},`

```json
"id": 200000003001, "identifier": "3907f9a58***08476b2506", "name": "y1y1y1", "nick": null, "isDefault": false, "networkType": 1, "nodes": [{ "clusterName": "3907f9a583****8476b2506", "nodeName": "1.2.3.50", "nodeAddress": "1.2.3.50", "maxSlot": 32, "useSlot": 0, "state": 1, "live": false, "startMon": false, "regionId": 1, "nodeProperties": "{\"memory\":8,\"vCpu\":4}", "vCpu": 4, "memory": 8, "useDmu": 0 }], "maxSlot": 32, "useSlot": 0, "useDmu": 0, "maxDmu": 16, "projects": null, "resourceGroupType": null, "diResourceGroupType": 1, "buyType": "pay-as-you-go"
```

`},`

```json
"id": 33224***49920, "identifier": "c43d****cb7fef18c137", "name": "cfr", "nick": null, "isDefault": false, "networkType": 1, "nodes": [{ "clusterName": "c43da72697****c137", "nodeName": "deide",
```

```json
"nodeAddress": "10.0.0.22", "maxSlot": 8, "useSlot": 0, "state": 1, "live": false, "startMon": false, "regionId": 1, "nodeProperties": "{\"memory\":4,\"vCpu\":2}", "vCpu": 2, "memory": 4, "useDmu": 0 }], "maxSlot": 8, "useSlot": 0, "useDmu": 0, "maxDmu": 4, "projects": null, "resourceGroupType": null, "diResourceGroupType": 1, "buyType": "pay-as-you-go"
```

`},`

```json
"id": 329080157014786, "identifier": "bd49c8014fb64f53835793e94932a9ac", "name": "hello", "nick": null, "isDefault": false, "networkType": 1, "nodes": [{ "clusterName": "bd49c801******e94932a9ac", "nodeName": "djed***qduew", "nodeAddress": "0.1.0.0", "maxSlot": 24, "useSlot": 0, "state": 1, "live": false, "startMon": false, "regionId": 1, "nodeProperties": "{\"memory\":8,\"vCpu\":8}", "vCpu": 8, "memory": 8, "useDmu": 0 }], "maxSlot": 24, "useSlot": 0, "useDmu": 0, "maxDmu": 12, "projects": null, "resourceGroupType": null, "diResourceGroupType": 1, "buyType": "pay-as-you-go" }], "errMsg": "success", "errCode": 0
```

### 6.29 GetTableColumn

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GetTableColumn. |
| BaseId | String | Yes | The ID of the Apsara Stack account. |
| DatasourceName | String | Yes | The name of the data source. |
| DatasourceType | String | Yes | The type of the data source. |
| ProjectId | Long | Yes | The ID of the DataWorks workspace. |
| SubType | String | Yes | The subtype of the data source. Currently, only MySQL is supported. |
| Table | String | Yes | The name of the table in the data source. |
| TenantId | Long | Yes | The ID of the tenant. |
| Id | String | No | The ID of the data source. |

| Parameter | Type | Description |
|---|---|---|
| Data | - | The fields of the specified table in the data source. |
| ErrCode | Long | The error code. |
| ErrMsg | String | The error message. |
| RequestId | String | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/? Action=GetTableColumn &BaseId=148682***73474 &DatasourceName=odps_first &DatasourceType=odps &ProjectId=75059 &SubType=public &Table=t &TenantId=2678***78690 &<Common request parameters>
```

Sample success responses

```json
"requestId": "0bc1748b15574030794246845e5f16", "data": { "splitPk": [], "columns": [{ "name": "id", "type": "STRING" }], "partitionColumns": [], "extraInfo": {}
```

`},`

```json
"errMsg": "success", "errCode": 0
```

### 6.30 GetTableList

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to GetTableList. |
| BaseId | String | Yes | The ID of the Apsara Stack tenant account. |
| DatasourceName | String | Yes | The name of the data store. |
| DatasourceType | String | Yes | The type of the data store. |
| ProjectId | Long | Yes | The ID of the DataWorks workspace. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| SubType | String | Yes | The subtype of the data store. |
| Table | String | Yes | The name of the table in the data store. |
| TenantId | Long | Yes | The ID of the tenant. |
| Id | Long | No | The ID of the data store. |
| PageSize | Long | No | The number of entries to return on each page. |

| Parameter | Type | Description |
|---|---|---|
| Data | - | The returned data. |
| ErrCode | Long | The error code. |
| ErrMsg | String | The error message. |
| RequestId | String | The ID of the request. |

Sample request

```
http(s)://[Endpoint]/? Action=GetTableList &BaseId=1486821399873474 &DatasourceName=odps_first &DatasourceType=odps &ProjectId=75059 &SubType=public &Table=t &TenantId=267883377178690 &<Common request parameters>
```

Sample response

```json
"requestId": "0bc17****2e5f16", "data": { "tables": ["c", "t", "t1", "t2", "wowo", "zzyx", "oss_test", "oss_tes00t", "test_input"]
```

`},`

```json
"errMsg": "success", "errCode": 0
```

### 6.31 GetTaskLog

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to GetTaskLog. |
| AccountId | String | Yes | The ID of the account that is assigned by the scheduling system to call this operation. |
| AccountPwd | String | Yes | The password of the account that is assigned by the scheduling system to call this operation. |
| BaseId | String | Yes | The ID of the Apsara Stack account that you use to call this operation. |
| ClientName | String | Yes | The name of the client that is assigned by the scheduling system to call this operation. |
| ProjectEnv | String | Yes | The type of the environment. Valid values: PROD and DEV. The value PROD specifies to return the information about the node instances in the production environment that meet the search conditions. The value DEV specifies to return the information about the node instances in the development environment that meet the search conditions. |
| TenantId | Long | Yes | The ID of the tenant. Set the value to 1. |
| TaskId | Long | No | The ID of the node instance. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. If an error occurs, send the request ID to the developers of the scheduling system for troubleshooting. |
| ReturnCode | String | The return code. The value 0 indicates that the operation is successful. |
| ReturnErrorSolution | String | None |
| ReturnMessage | String | The error message. |
| ReturnValue | String | The logs that were returned. |

Sample requests

```
http(s)://[Endpoint]/? Action=GetTaskLog &AccountId=C00000 &AccountPwd=account_pwd &BaseId=0I0001 &ClientName=aone_app_name &ProjectEnv=DEV &TenantId=1 &TaskId=20000000 &<Common request parameters>
```

Sample success responses

```json
"ReturnValue": "I'm alog", "ReturnCode": "0", "RequestId": "023dbca2-3****f23fa26", "ReturnErrorSolution": "", "ReturnMessage": ""
```

### 6.32 GetUserInfo

| Parameter | Type | Required | Description |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | STRING | Yes | The operation that you want to perform. Set the value to GetUserInfo. |

| Parameter | Type | Description |
|---|---|---|
| ErrCode | INTEGER | The returned error code. |
| ErrMsg | STRING | The returned message. |
| RequestId | STRING | The ID of the request. |
| User | N/A | The information about the user that was queried. |

### 6.33 ListConnection

You can call this operation to query data sources.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ProjectId | Long | Yes | 12345 | The ID of the data source. |
| Name | String | No | "myds" | The name of the data source. This parameter must be specified when you want to query the AccessKey of a computing engine. By default, do not set this parameter. |
| Keyword | Boolean | No | "mydatasource" | Specifies whether to hide the specified sensitive fields. Default value: false. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Status | Integer | No | 0 | The status of the data source. Valid values: 0, 1, and 2. 0: The data source is deleted. 1: The data source is normal. 2: The data source is disabled. |
| BindEngineId | Long | No | 12345 | The ID of the compute engine that is bound with the data source. |
| EnvType | Integer | No | 1 | The type of the environment. Valid values: 0 and 1. 0: the development environment. 1: the production environment. |
| BaseId | String | No | "034302" | The ID of the Apsara Stack account. This parameter must be specified when you want to query the AccessKey of a computing engine. By default, do not set this parameter. |
| Verbose | Boolean | No | true | Specifies whether to return the details about the connection string of the data source. Default value: false. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageNum | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Default value: 10. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | c9afd89b-7aef-47c9- 9902-e0500d843268 | The ID of the request. If an error occurs, send the request ID to the developers of the scheduling system for troubleshooting. The request ID must be globally unique. |
| errCode | Long | 0 | The error code. The value 0 indicates that the operation is successful. A value greater than 0 indicates the error code of the error that occurred. |
| errMsg | String | success | The error message. If the value of the errCode parameter is 0, the value of the errMsg parameter is a null string or success. |
| data | PagingResult<Connectio n> | N/A | The returned data. |
| TotalNum | Integer | N/A | The total number of entries that were returned. |
| PageNum | Integer | N/A | The page number of the returned page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageSize | Integer | N/A | The number of entries returned per page. |
| Connections | List<Connection> | N/A | The list of data sources that were returned. |
| Id | Long | 12345 | The ID of the data source. |
| TenantId | Long | 12345 | The ID of the tenant. |
| ProjectId | Long | 12345 | The ID of the DataWorks workspace. |
| Name | String | "testDataSource" | The name of the data source. |
| Type | String | "mysql" | The type of the connection string. |
| SubType | String | "" | The subtype of the connection string. |
| EnvType | Integer | 0 | The type of the environment. Valid values: 0 and 1. The value 0 indicates the development environment. The value 1 indicates the production environment. |
| Connection | String | {"username":"u1","pass word":"p1"} | The connection string of the data source. |
| Sequence | Integer | 300 | The sequence number of the data source. |
| Status | Integer | 0 | The status of the data source. Valid values: 0, 1, and 2. 0: The data source is deleted. 1: The data source is normal. 2: The data source is disabled. |
| Description | String | "this is a testdatasource" | The description of the data source. |

|   | DataWorks |   |   | Developer Guide·Java SD | K |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Shared | Boolean | true | Indicates whether the data source is shared among users of the tenant. |
| GmtCreate | Date | 2018-11-11 00:00:00 | The time when the data source was created. |
| GmtModified | Date | 2018-11-11 00:00:00 | The time when the data source was last modified. |
| Operator | String | "032214" | The user who modified the data source last time. |
| ConnectTime | Date | 2018-11-11 00:00:00 | The time when the data source was last connected. |
| ConnectStatus | Integer | 0 | The connection status of the data source. Valid values: 0, 1, and 2. 0: The connectivity test has not been run. 1: The data source is successfully connected. 2: The data source failed the connectivity test. |

Sample requests

```
/? ProjectId=12345 &Keyword="mydatasource" &<Common request parameters>
```

Sample success responses JSON format

```json
  "data":{
    "TotalNum":35,
    "PageNum":1,
    "PageSize":10,
    "Connections":[
        "Id":12345,
        "TenantId":12345,
        "ProjectId":12345,
        "Name":"testDataSource",
        "Type":"mysql",
        "SubType":"",
        "EnvType":0,
        "Connection":"{\"username\":\"u1\",\"password\":\"p1\"}",
        "Sequence":300,
        "Status":0,
        "Description":"this is a test datasource",
        "Shared":0,
        "GmtCreate":"2018-11-11 00:00:00",
        "GmtModified":"2018-11-11 00:00:00",
        "Operator":"032214",
        "ConnectTime":"2018-11-11 00:00:00",
        "ConnectStatus":0
      },...
```

`]` `},`

```json
  "errCode":0,
  "errMsg":"success",
  "requestId":"c9afd89b-7aef-47c9-9902-e0500d843268"
```

Sample error responses JSON format

```json
  "data":null,
  "errCode":1101002001,
  "errMsg":"invalid parameter",
  "requestId":"c9afd89b-7aef-47c9-9902-e0500d843268"
```

### 6.34 ListDataServiceApps

| Parameter | Type | Required | Description |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ListDataServiceApps. |
| BaseId | String | No | The ID of the Apsara Stack account. |
| AppName | String | No | The name of the application to query. |
| PageSize | Integer | No | The number of entries to return on each page. |
| PageNum | Integer | No | The number of the page to return. |

| Parameter | Type | Description |
|---|---|---|
| Data | N/A | The returned data. |
| ErrCode | Integer | The error code. |
| ErrMsg | String | The error message. |
| RequestId | String | The ID of the request. |

### 6.35 ListDataServiceAuthedApi

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ListDataServiceAuthedA pi. |
| BaseId | String | Yes | The ID of the Apsara Stack account. |
| ProjectId | Long | Yes | The ID of the DataWorks workspace. |
| ApiStatus | String | No | The status of the operation to query. |

| eveloper Guide·Java SDK |   |   | DataWork |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| PageNum | Integer | No | The number of the page to return. |
| PageSize | Integer | No | The number of entries to return on each page. |
| Verbose | Boolean | No | Indicates whether to return the details of the operation. |

| Parameter | Type | Description |
|---|---|---|
| Data | N/A | The returned data. |
| ErrCode | Integer | The error code. |
| ErrMsg | String | The error message. |
| RequestId | String | The ID of the request. |

### 6.36 ListPermission

You can call this operation to query permissions.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ListPermission. |
| baseId | String | No | The ID of the Apsara Stack account. |
| tenantId | Long | No | The ID of the tenant. |
| projectId | Long | No | The ID of the DataWorks workspace. |
| modules | String | No | The modules of the DataWorks workspace. |

| Parameter | Type | Description |
|---|---|---|
| Data | N/A | The returned data. |
| errCode | Integer | The error code. The value 0 indicates that the operation is successful. A value greater than 0 indicates the error code of the error that occurred. |
| requestId | String | The ID of the request. If an error occurs, send the request ID to the developers of the scheduling system for troubleshooting. The request ID must be globally unique. |

Sample requests

```
/? Action=ListPermission &baseId= &modules= &projectId= &tenantId= &<Common request parameters>
```

### 6.37 ListProjectModule

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ListProjectModule. |
| ProjectId | Long | No | The ID of the DataWorks workspace. |

| Parameter | Type | Description |
|---|---|---|
| ErrCode | Integer | The error code. |
| ErrMsg | String | The error message. |

| Developer Guide·Java SDK |   | DataWork |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| Modules | N/A | The modules of the DataWorks workspace. |
| RequestId | String | The ID of the request. |

### 6.38 ListProjectModules

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ListProjectModules. |
| ProjectId | Long | No | The ID of the DataWorks workspace. |

| Parameter | Type | Description |
|---|---|---|
| ErrCode | Integer | The error code. |
| ErrMsg | String | The error message. |
| Modules | N/A | The modules of the DataWorks workspace. |
| RequestId | String | The ID of the request. |

### 6.39 ListProject

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ListProject. |

| Parameter | Type | Description |
|---|---|---|
| ErrCode | Long | The error code. |

| ataWorks |   | Developer Guide·Java SD |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| ErrMsg | String | The error message. |
| ProjectList | N/A | The DataWorks workspaces that were queried. |
| RequestId | String | The ID of the request. |

### 6.40 ListTenantModule

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ListTenantModule. |
| TenantId | Long | No | The ID of the tenant. |

| Parameter | Type | Description |
|---|---|---|
| ErrCode | Integer | The error code. |
| ErrMsg | String | The error message. |
| Modules | N/A | The modules of the tenant. |
| RequestId | String | The ID of the request. |

### 6.41 ListUserPermission

You can call this operation to query permissions of a user.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ListUserPermission. |
| BaseId | String | No | The ID of the Apsara Stack account. |
| TenantId | Long | No | The ID of the tenant. |

| eveloper Guide·Java SDK |   |   | DataWork |
|---|---|---|---|
| Parameter | Type | Required | Description |
| ProjectId | Long | No | The ID of the DataWorks workspace. |
| Modules | String | No | The modules of the DataWorks workspace. |

| Parameter | Type | Description |
|---|---|---|
| Data | N/A | The returned data. |
| ErrCode | Integer | The error code. The value 0 indicates that the operation is successful. A value greater than 0 indicates the error code of the error that occurred. |
| ErrMsg | String | The error message. If the value of the errCode parameter is 0, the value of the errMsg parameter is a null string or success. |
| RequestId | String | The ID of the request. If an error occurs, send the request ID to the developers of the scheduling system for troubleshooting. The request ID must be globally unique. |

### 6.42 ModifyBusiness

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyBusiness. |
| AccountId | String | No | The ID of the account that is assigned by the scheduling system to call this operation. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| AccountPwd | String | No | The password of the account that is assigned by the scheduling system to call this operation. |
| BaseId | String | No | The ID of the Apsara Stack account that you use to call this operation. |
| BusinessModifyDto | String | No | { "executeMethod": "UPDATE BUSINESS" _ , "bizId": 100000003, "bizKey": "biz key 01", _ _ "bizName": "biz name 01 xxxx _ _ _ ", "solId": 100000002, "appId": 78918, "tenantId": 2797***8706 } |
| ClientName | String | No | The name of the client that is assigned by the scheduling system to call this operation. |
| TenantId | Long | No | The ID of the tenant. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. If an error occurs, send the request ID to the developers of the scheduling system for troubleshooting. |
| ReturnCode | String | The return code. The value 0 indicates that the operation is successful. |
| ReturnErrorSolution | String | None |
| ReturnMessage | String | The error message. |
| ReturnValue | String | The information about the workflow that was modified. |

### 6.43 ModifyNode

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyNode. |
| AccountId | String | No | The ID of the account that is assigned by the scheduling system to call this operation. |
| AccountPwd | String | No | The password of the account that is assigned by the scheduling system to call this operation. |
| ClientName | String | No | The name of the client that is assigned by the scheduling system to call this operation. |

| DataWorks |   |   | Developer Guide·Java SD |   |   |
|---|---|---|---|---|---|
| Parameter | Type | Required |   | De[s c{ription "executeMethod": |   |
| ModifyDtoList | String | No | "CREATE NODE", _ "nodeType": 0, "cronExpress": "0 0 0 * * ?", "owner": " {{user id}}", _ "createUser": "{{user id}}", _ "modifyUser": " {{user id}}", _ "dependentType": 0, "nodeName": "locale test node _ _ 118", "prgType": 99, "priority": 0, "appId": 14255, "cycType": 1, "codeSrc": "", "nodeFrom": "postman", "inputs": [ { "data": "test dev prod de _ _ _ pend single root" _ _ } ], "outputs": [ "data": "locale test node _ _ 118out" } ], "uniqueId": "locale test node _ _ 6" } ] | "CREATE NODE", _ "nodeType": 0, "cronExpress": "0 0 0 * * ?", "owner": " {{user id}}", _ "createUser": "{{user id}}", _ "modifyUser": " {{user id}}", _ "dependentType": 0, "nodeName": "locale test node _ _ 118", "prgType": 99, "priority": 0, "appId": 14255, "cycType": 1, "codeSrc": "", "nodeFrom": "postman", "inputs": [ { "data": "test dev prod de _ _ _ pend single root" _ _ } ], "outputs": [ "data": "locale test node _ _ 118out" } ], "uniqueId": "locale test node _ _ 6" } ] |   |

| Parameter | Type | Required | Description |
|---|---|---|---|
| ProjectEnv | String | No | The type of the environment. Valid values: DEV and PROD. The value DEV specifies the development environment. The value PROD specifies the production environment. |
| BaseId | String | No | The ID of the Apsara Stack account that you use to call this operation. |
| TenantId | Long | No | The ID of the tenant. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. If an error occurs, send the request ID to the developers of the scheduling system for troubleshooting. |
| ReturnCode | String | The return code. The value 0 indicates that the operation is successful. |
| ReturnErrorSolution | String | The solution to resolve the issue. |
| ReturnMessage | String | The error message. |
| ReturnValue | String | The value of the RequestId parameter. The request ID is returned after you send an asynchronous request. You can use this ID to call the GetNodeUpdateStatus operation to query the node status. |

Sample success responses

```json
"returnCode": "0", "returnErrorSolution": "", "returnMessage": "", "requestId": "82e4c****a39fbda", "returnValue": "82e4c04****f5a39fbda", "success": true
```

### 6.44 ModifySolution

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifySolution. |
| AccountId | String | No | The ID of the account that is assigned by the scheduling system to call this operation. |
| AccountPwd | String | No | The password of the account that is assigned by the scheduling system to call this operation. |
| BaseId | String | No | The ID of the Apsara Stack account that you use to call this operation. |
| ClientName | String | No | The name of the client that is assigned by the scheduling system to call this operation. |
| TenantId | Long | No | The ID of the tenant. |
| SolutionModifyDto | String | No | The information about the solution in the JSON format. |

| Parameter | Type | Description |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. If an error occurs, send the request ID to the developers of the scheduling system for troubleshooting. |
| ReturnCode | String | The return code. The value 0 indicates that the operation is successful. |
| ReturnErrorSolution | String | The solution to resolve the issue. |
| ReturnMessage | String | The error message. |
| ReturnValue | String | None |

Example of the SolutionModifyDto parameter

```json
"executeMethod": "UPDATE_SOLUTION", "solId": 100000001, "solName": "sol_name_01_xxxx", "appId": 78918, "tenantId": 279717776488706
```

Sample success responses

```json
"returnCode": "0", "returnErrorSolution": "", "returnMessage": "", "requestId": "53ca5f***11bab4d0975", "returnValue": { "solId": 100000001, "solName": "sol_name_01_xxxx", "appId": 78918, "tenantId": 279717776488706
```

`},`

```json
"success": true
```

### 6.45 RerunTask

| Parameter | Type | Required | Description |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to RerunTask. |
| AccountId | String | Yes | The ID of the account that is assigned by the scheduling system to call this operation. |
| AccountPwd | String | Yes | The password of the account that is assigned by the scheduling system to call this operation. |
| BaseId | String | Yes | The ID of the Apsara Stack account that you use to call this operation. |
| ClientName | String | Yes | The name of the client that is assigned by the scheduling system to call this operation. |
| ProjectEnv | String | Yes | The type of the environment. |
| TaskId | Long | Yes | None |
| TenantId | Long | Yes | The ID of the tenant. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| ReturnCode | String | The error code. |
| ReturnErrorSolution | String | The solution to resolve the issue. |
| ReturnMessage | String | The error message. |
| ReturnValue | Boolean | Indicates whether the node is successfully rerun. |

Sample success responses

```json
"RequestID": "", "RetrunCode": 12344, "ReturnErrorSolution": "****", "ReturnMessage": "****", "ReturnValue": true
```

### 6.46 ResumeTask

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ResumeTask. |
| AccountId | String | No | The ID of the account that is assigned by the scheduling system to call this operation. |
| AccountPwd | String | No | The password of the account that is assigned by the scheduling system to call this operation. |
| BaseId | String | No | The ID of the Apsara Stack account that you use to call this operation. |
| ClientName | String | No | The name of the client that is assigned by the scheduling system to call this operation. |
| ProjectEnv | String | No | The type of the environment. Valid values: DEV and PROD. |
| TaskId | Long | No | The ID of the node to resume. |
| TenantId | Long | No | The ID of the tenant. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. If an error occurs, send the request ID to the developers of the scheduling system for troubleshooting. |
| ReturnCode | String | The error code. |
| ReturnErrorSolution | String | The solution to resolve the issue. |
| ReturnMessage | String | The error message. |

Sample success responses

```json
"RequestId": "1212adf***s-adfsdsf", "ReturnCode": 0, "ReturnMessage": "", "ReturnErrorSolution": "", "ReturnValue": true
```

### 6.47 SearchBusiness

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to SearchBusiness. |
| AccountId | String | No | The ID of the account that is assigned by the scheduling system to call this operation. |
| AccountPwd | String | No | The password of the account that is assigned by the scheduling system to call this operation. |
| BaseId | String | No | The ID of the Apsara Stack account that you use to call this operation. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| BizId | Long | No | Optional. The ID of the workflow. |
| ClientName | String | No | The name of the client that is assigned by the scheduling system to call this operation. |
| BizName | String | No | The name of the workflow. |
| BizKey | String | No | Optional. The key of the workflow. |
| TenantId | Long | No | The ID of the tenant. |
| AppId | Long | No | The ID of the DataWorks workspace. |
| AppIds | String | No | Optional. The IDs of the DataWorks workspaces. Separate multiple IDs with commas (,). |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. If an error occurs, send the request ID to the developers of the scheduling system for troubleshooting. |
| ReturnCode | String | The return code. The value 0 indicates that the operation is successful. |
| ReturnErrorSolution | String | The solution to resolve the issue. |
| ReturnMessage | String | The error message. |
| ReturnValue | - | None |

Sample success responses

```json
"returnCode": "0", "returnErrorSolution": "", "returnMessage": "", "requestId": "d4605f***145312", "returnValue": [ "bizId": 10010759, "bizName": "Control Node 0", "bizKey": "10010759", "appId": 12344, "tenantId": 121**212
```

`],`

```json
"success": true
```

### 6.48 SearchManualDagNodeInstance

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to SearchManualDagNodeI nstance. |
| ProjectName | String | No | The name of the DataWorks workspace. |
| DagId | Long | No | The ID of the instance for a manually triggered workflow. You can obtain this ID by calling the CreateManualDag operation. |

| Parameter | Type | Description |
|---|---|---|
| Data | String | The instances of the manually triggered workflow. |
| ErrCode | String | The error code. |
| ErrMsg | String | The error message. |
| RequestId | String | The ID of the request. |

| eveloper Guide·Java SDK |   | DataWork |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| Success | Boolean | Indicates whether the operation is successful. |

### 6.49 SearchSolution

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to SearchSolution. |
| AccountId | String | No | The ID of the account that is assigned by the scheduling system to make the API request. |
| AccountPwd | String | No | The password of the account that is assigned by the scheduling system to make the API request. |
| BaseId | String | No | The ID of the Apsara Stack tenant account that you use to call this operation. |
| ClientName | String | No | The name of the client that is assigned by the scheduling system to make the API request. |
| SolId | Long | No | (Optional) The ID of the solution. |
| SolName | String | No | The name of the solution. |
| TenantId | Long | No | The ID of the tenant. |
| AppId | Long | No | The ID of the DataWorks workspace. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. If an error occurs, you can send the request ID to the developers of the scheduling system for troubleshooting. |
| ReturnCode | String | The error code. |
| ReturnErrorSolution | String | The solution to resolve the issue. |
| ReturnMessage | String | The error message. |

Sample response

```json
"returnCode": "0", "returnErrorSolution": "", "returnMessage": "", "requestId": "1381****b98d87c", "returnValue": [ "solId": 100000007, "solName": "Solution Test 222", "appId": 33646, "tenantId": 27***9020672
```

`],`

```json
"success": true
```

### 6.50 SearchTasks

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to SearchTasks. |
| AccountId | String | Yes | The ID of the account that is assigned by the scheduling system to call this operation. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| AccountPwd | String | Yes | The password of the account that is assigned by the scheduling system to call this operation. |
| BaseId | String | Yes | The ID of the Apsara Stack account that you use to call this operation. |
| ClientName | String | Yes | The name of the client that is assigned by the scheduling system to call this operation. |
| ProjectEnv | String | Yes | The type of the environment. Valid values: PROD and DEV. The value PROD specifies to return the information about the node instances in the production environment that meet the search conditions. The value DEV specifies to return the information about the node instances in the development environment that meet the search conditions. |
| NodeId | Long | No | The ID of the node. You can view the ID on the node configuration page in the DataWorks console. |
| TenantId | Long | Yes | The ID of the tenant. Set the value to 1. |
| DagId | Long | No | The ID of the workflow instance to which the node instances belong. When you call the CreateDag operation to create a workflow instance, the ID of the workflow instance is returned. You can use this ID to query the workflow instance. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| Bizdate | String | No | The date-based timestamp. The value is in the format of yyyy- mm-dd 00:00:00. You can use this data timestamp to filter the node instances. |

| Parameter | Type | Description |
|---|---|---|
| Count | Integer | The number of the node instances that meet the search conditions. |
| RequestId | String | The ID of the request. If an error occurs, send the request ID to the developers of the scheduling system for troubleshooting. |
| ReturnCode | String | The return code. The value 0 indicates that the operation is successful. |
| ReturnErrorSolution | String | The solution to resolve the issue. |
| ReturnMessage | String | The error message. |
| ReturnValue |   | None |

Sample requests

```
http(s)://[Endpoint]/? Action=SearchTasks &AccountId=C00000 &AccountPwd=account-pwd &BaseId=0I0001 &ClientName=aone_app_name &ProjectEnv=PROD &TenantId=1 &Bizdate=2018-11-17 00:00:00 &DagId=10000000 &NodeId=1000001 &<Common request parameters>
```

Sample success responses

```json
"Count": 3236869, "ReturnValue": [ "DqcInstance": "", "BeginWaitResTime": "", "ResGroupId": 30004716, "AppId": 14255, "TaskId": 9993181585, "PrgName": "", "Gmtdate": "2018-11-17 00:00:00", "NodeId": 20636213, "DqcDescription": "", "BeginRunningTime": "", "AlisaReturnTime": "", "FinishTime": "", "GwLogLocalFile": "", "DagId": 300041822, "ParaValue": "", "DueTime": "2018-11-17 00:06:00", "BaseLineId": 332, "NodeName": "trewtes", "CycType": 0, "DagType": 2, "InGroupId": 1, "Priority": 1, "RerunAble": true, "Status": 1, "ResGroupIdentifier": "group_30004716", "GwProcessId": "", "PrgType": 10, "Bizdate": "2018-11-16 00:00:00", "ExecName": "/opt/taobao/tbdpapp/odpswrapper/odpswrapper.py", "BeginWaitTimeTime": "", "Gateway": "", "GwLogFile": "", "TaskType": 0
```

`]`

### 6.51 TestConnectivity

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to TestConnectivity. |

| ataWorks |   |   | Developer Guide·Java SD |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| BaseId | String | Yes | The ID of the Apsara Stack account. |
| Connection | String | Yes | The connection string of the data source. |
| Name | String | Yes | The name of the data source. |
| ProjectId | Long | Yes | The ID of the DataWorks workspace. |
| SubType | String | Yes | The subtype of the data source. Currently, only MySQL is supported. |
| TenantId | Long | Yes | The ID of the tenant. Set the value to 1. |
| Type | String | Yes | The type of the data source. |
| Id | Long | No | The ID of the data source. |
| UseUserDefinedSecret | Boolean | No | Specifies whether to use the saved password for logging on to the data source. |

| Parameter | Type | Description |
|---|---|---|
| Data | Boolean | Indicates whether the data source is successfully connected. |
| ErrCode | Long | The error code. |
| ErrMsg | String | The error message. |
| RequestId | String | The ID of the request. |

Sample requests

```json
http(s)://[Endpoint]/? Action=TestConnectivity &BaseId=1486*****474 &Connection={"jdbcUrl":"jdbc:mysql://12.11.12.1:3306/data", "username":"root ", "password":"***", "tag":"public"} &Name="test" &ProjectId=75059 &SubType=public &TenantId=26788***178690 &Type=mysql &<Common request parameters>
```

Sample success responses

```json
"requestId": "0a98***7e2c95", "data": null, "errMsg": "Test for the data source connectivity failed:error message: Communications link failure\n\nThe last packet sent successfully to the server was 0 milliseconds ago. The driv er has not received any packets from the server. error with code: PROJECT_DATASOURCE_CONN_E RROR", "errCode": 610008
```

### 6.52 UpdateDQCFollower

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to UpdateDQCFollower. |
| ProjectName | String | No | The name of the DataWorks workspace. |
| Id | Long | No | The ID of the subscription. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| Follower | String | No | The object of receiving the subscribed messages. If you want to receive the messages by using emails or the SMS, specify your employee ID. If you want to receive the messages by using DingTalk, specify the webhook URL. |
| AlarmMode | Integer | No | The method of receiving alerts and notifications. A value of 1 indicates that you receive alerts and notifications by using emails. A value of 2 indicates that you receive alerts and notifications by using emails and the SMS. A value of 3 indicates that you receive alerts and notifications from the specified DingTalk group by using the webhook URL. A value of 4 indicates that you receive alerts and notifications from the specified DingTalk group and mention all members in the group. |

| Parameter | Type | Description |
|---|---|---|
| ReturnCode | String | The return code. |
| ReturnValue | Boolean | Indicates whether the subscription information has been changed. |

Sample request

```
http(s)://[Endpoint]/? Id=279580663 &ProjectName=autotest &BlockType=1 &Checker=9 &Comment=Test &CriticalThreshold=40 &EntityId=4003922 &ExpectValue=0 &MethodName=count/table_count &Operator=50624 &Property=table_count &PropertyType=table &RuleType=0 &TemplateId=7 &Trend=abs &WarningThreshold=20 &WhereCondition=60 &<Common request parameters>
```

Sample response

```json
"ReturnValue": true, "ReturnCode": "0"
```

### 6.53 UpdateDQCRule

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to UpdateDQCRule. |
| ProjectName | String | Yes | The name of the DataWorks workspace. |
| Id | Long | Yes | The ID of the Data Quality check (DQC) rule to change. |
| BlockType | Integer | No | The type of the DQC rule. Valid values: 0 and 1. The value 0 specifies a soft rule. The value 1 specifies a hard rule. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| EntityId | Long | No | The ID of the partition filter expression. |
| Comment | String | No | The description of the DQC rule. |
| Checker | Integer | No | The ID of the checker. |
| ExpectValue | String | No | The expected value of the checker. |
| Trend | String | No | The trend of the expected value. |
| MethodName | String | No | The sampling method, such as max, table count- _ count distinct, and _ user defined. _ |
| Operator | String | No | The user who is to change the DQC rule. |
| Property | String | No | The field of the DQC rule to change. |
| PropertyType | String | No | The type of the field. |
| RuleType | Integer | No | The type of the DQC rule. Valid values: 0 and 1. The value 0 specifies that the rule is defined by the system. The value 1 specifies that the rule is defined by users. |
| WhereCondition | String | No | The filtering condition. Write a SQL statement to specify the filtering condition. |
| CriticalThreshold | String | No | The error threshold. |
| WarningThreshold | String | No | The warning threshold. |
| TemplateId | Integer | No | The ID of the template to use for changing the DQC rule. |

Checkers Methods

| Parameter | Type | Description |
|---|---|---|
| ReturnCode | String | The return code. |
| ReturnValue | Boolean | Indicates whether the DQC rule has been changed. |

Sample requests

```
http(s)://[Endpoint]/? Action=UpdateDQCFollower &AlarmMode=1 &Follower=50624 &Id=1724 &ProjectName=autotest &<Common request parameters>
```

Sample success responses

```json
"ReturnValue": true, "ReturnCode": "0"
```

### 6.54 UpdateResGroupGateWay

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to UpdateResGroupGateW ay. |
| BaseId | String | Yes | The ID of the Apsara Stack account. |
| Identifier | String | Yes | The identifier of the resource group. |
| Memory | Integer | Yes | The memory size of the gateway. |

| DataWorks |   |   | Developer Guide·Java SD |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| NodeName | String | Yes | The name of the node that runs the gateway. |
| ProjectId | Long | Yes | The ID of the DataWorks workspace. |
| TenantId | Long | Yes | The ID of the tenant. |
| VCpu | Integer | Yes | The number of cores in the vCPU of the gateway. |

| Parameter | Type | Description |
|---|---|---|
| Data | Boolean | Indicates whether the gateway configuration has been changed. |
| ErrCode | Long | The error code. |
| ErrMsg | String | The error message. |
| RequestId | String | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/? Action=UpdateResGroupGateWay &BaseId=1486821399873474 &Identifier=3907f9a58***8476b2506 &Memory=4 &NodeName=hostname &ProjectId=75059 &TenantId=26788a***90 &VCpu=9
 &<Common request parameters>
```

Sample success responses

```json
"requestId": "0bc174***5f15", "data": true, "errMsg": "success", "errCode": 0
```

### 6.55 CheckMetaTable

Checks whether a table exists.

| Parameter | Type | Required | Description |
|---|---|---|---|
| TableGuid | STRING | No | The GUID of the table. |

| Parameter | Type | Description |
|---|---|---|
| Data | Boolean | Indicates whether the table exists. |

Sample code

```java
private String product = "dataworks-private-cloud"; private String version = "2019-01-17"; private String appGuid = "odps.dw_meta"; private String tableGuid = "odps.dw_meta.dwd_d_odps_table"; private String columnName = "table_comment"; CommonRequest cr = new CommonRequest(); cr.setProduct(product); cr.setVersion(version); cr.setMethod(MethodType.GET); cr.setAction("CheckMetaTable"); cr.putQueryParameter("TableGuid", tableGuid); CommonResponse cresp = client.getCommonResponse(cr); assertNotNull(cresp); assertNotNull(cresp.getData());
```

### 6.56 GetMetaDB

Queries the information about a MaxCompute project.

| Parameter | Type | Required | Description |
|---|---|---|---|
| DbGuid | STRING | No | The GUID of the MaxCompute project. |

| Parameter | Type | Description |
|---|---|---|
| AppGuid | STRING | The GUID of the MaxCompute project. |

| DataWorks |   | Developer Guide·Java SD |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| ProjectName | STRING | The name of the MaxCompute project. |
| ProjectNameCn | STRING | The description of the MaxCompute project. |
| OwnerId | STRING | The Apsara Stack tenant account of the MaxCompute project owner. |
| OwnerName | STRING | The name of the MaxCompute project owner. |
| CreateTime | STRING | The time when the MaxCompute project was created. |
| ModifyTime | STRING | The time when the MaxCompute project was modified. |

Sample code

```java
private String product = "dataworks-private-cloud"; private String version = "2019-01-17"; private String appGuid = "odps.dw_meta"; private String tableGuid = "odps.dw_meta.dwd_d_odps_table"; private String columnName = "table_comment"; CommonRequest cr = new CommonRequest(); cr.setProduct(product); cr.setVersion(version); cr.setMethod(MethodType.GET); cr.setAction("GetMetaDB"); cr.putQueryParameter("DbGuid", appGuid); CommonResponse cresp = client.getCommonResponse(cr); assertNotNull(cresp); assertNotNull(cresp.getData());
```

### 6.57 GetMetaTable

Queries the detailed information about a table.

| Parameter | Type | Required | Description |
|---|---|---|---|
| TableGuid | STRING | No | The GUID of the table. |

| Parameter | Type | Description |
|---|---|---|
| AppGuid | STRING | The GUID of the MaxCompute project where the table resides. |
| SrcType | INTEGER | The source of the table. A value of 0 indicates MaxCompute. |
| LastDdlTime | STRING | The time when the table was last updated. |
| TableGuid | STRING | The GUID of the table. |
| OwnerId | STRING | The Apsara Stack tenant account of the table owner. |
| HeatDegree | INTEGER | The popularity of the table. |
| Labels | STRING | The tags of the table. Multiple tags are separated with commas (,). |
| TableDesc | STRING | The description of the table. |
| HasPart | INTEGER | Indicates whether the table is a partitioned table. A value of 1 indicates that the table is a partitioned table. |
| IsVisible | INTEGER | Indicates whether the table is visible. A value of 1 indicates that the table is visible. |
| LifeCycle | INTEGER | The lifecycle of the table. |
| DataSize | LONG | The storage space occupied by the table. |
| TableName | STRING | The name of the table. |
| CreateTime | STRING | The time when the table was created. |
| LastModifyTime | STRING | The time when the table was last modified. |

Sample code

```java
private String product = "dataworks-private-cloud"; private String version = "2019-01-17"; private String appGuid = "odps.dw_meta"; private String tableGuid = "odps.dw_meta.dwd_d_odps_table"; private String columnName = "table_comment"; CommonRequest cr = new CommonRequest(); cr.setProduct(product); cr.setVersion(version); cr.setMethod(MethodType.GET); cr.setAction("GetMetaTable"); cr.putQueryParameter("TableGuid", tableGuid); CommonResponse cresp = client.getCommonResponse(cr); assertNotNull(cresp); assertNotNull(cresp.getData());
```

### 6.58 GetMetaTableIntroWiki

Queries the instructions of the specified version on how to use a table.

| Parameter | Type | Required | Description |
|---|---|---|---|
| TableGuid | STRING | Yes | The GUID of the table. |
| WikiVersion | LONG | No | The version number of Wiki. |

| Parameter | Type | Description |
|---|---|---|
| GmtCreate | STRING | The time when the table was created. |
| GmtModified | STRING | The time when the table was modified. |
| CreatorName | STRING | The name of the table creator. |
| CreatorBaseId | STRING | The base ID of the table creator. |
| Content | STRING | The description of the table. |

Sample code

```java
private String product = "dataworks-private-cloud"; private String version = "2019-01-17"; private String appGuid = "odps.dw_meta"; private String tableGuid = "odps.dw_meta.dwd_d_odps_table"; private String columnName = "table_comment"; CommonRequest cr = new CommonRequest(); cr.setProduct(product); cr.setVersion(version); cr.setMethod(MethodType.GET); cr.setAction("GetMetaTableIntroWiki"); cr.putQueryParameter("TableGuid", tableGuid); cr.putQueryParameter("WikiVersion", 2); CommonResponse cresp = client.getCommonResponse(cr); assertNotNull(cresp); assertNotNull(cresp.getData());
```

### 6.59 ListMetaColumnLineage

Queries the lineage of a field.

| Parameter | Type | Required | Description |
|---|---|---|---|
| TableGuid | STRING | Yes | The GUID of the table. |
| ColumnName | STRING | Yes | The name of the field in the table. |
| Direction | STRING | Yes | Specifies whether to query the ancestor or descendant lineage of the field. A value of UP specifies that ancestor fields are to be queried, and a value of DOWN specifies that descendant fields are to be queried. |

| Parameter | Type | Description |
|---|---|---|
| TableName | STRING | The name of the ancestor or descendant table. |
| ColumnName | STRING | The name of the ancestor or descendant field. |
| ColumnGuid | STRING | The GUID of the ancestor or descendant field. |

Sample code

```java
private String product = "dataworks-private-cloud"; private String version = "2019-01-17"; private String appGuid = "odps.dw_meta"; private String tableGuid = "odps.dw_meta.dwd_d_odps_table"; private String columnName = "table_comment"; CommonRequest cr = new CommonRequest(); cr.setProduct(product); cr.setVersion(version); cr.setMethod(MethodType.GET); cr.setAction("ListMetaColumnLineage"); cr.putQueryParameter("TableGuid", tableGuid); cr.putQueryParameter("Direction", "DOWN"); cr.putQueryParameter("ColumnName", columnName); CommonResponse cresp = client.getCommonResponse(cr); assertNotNull(cresp); assertNotNull(cresp.getData());
```

### 6.60 ListMetaTableChangeLog

Queries the change logs of a table.

| Parameter | Type | Required | Description |
|---|---|---|---|
| TableGuid | STRING | Yes | The GUID of the table. |
| StartDate | STRING | No | The beginning of the time range to query, in the yyyy-MM-dd format. |
| EndDate | STRING | No | The end of the time range to query, in the yyyy-MM-dd format. |
| ChangeType | STRING | No | The change type. Valid values: CREATETABLE, _ ALTERTABLE, _ DROPTABLE, _ ADDPARTITION, and _ DROPPARTITION. _ |
| ObjectType | STRING | No | The entity on which the change was made. Valid values: TABLE and PARTITION. |
| PageNum | INTEGER | No | The number of the page to return. |

| Developer Guide·Java SDK |   |   | DataWork |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| PageSize | INTEGER | No | The number of entries to return on each page. |

| Parameter | Type | Description |
|---|---|---|
| GmtCreate | STRING | The time when the table was created. |
| GmtModified | STRING | The time when the table was modified. |
| Guid | STRING | The name of the table creator. |
| ChangeType | STRING | The change type. |
| ObjectType | STRING | The entity on which the change was made. |
| Operator | STRING | The name of the operator. |
| ChangeContent | STRING | The change description. |

Sample code

```java
private String product = "dataworks-private-cloud"; private String version = "2019-01-17"; private String appGuid = "odps.dw_meta"; private String tableGuid = "odps.dw_meta.dwd_d_odps_table"; private String columnName = "table_comment"; CommonRequest cr = new CommonRequest(); cr.setProduct(product); cr.setVersion(version); cr.setMethod(MethodType.GET); cr.setAction("ListMetaTableChangeLog"); cr.putQueryParameter("TableGuid", tableGuid); cr.putQueryParameter("StartDate", "2020-03-22"); cr.putQueryParameter("EndDate", "2020-03-26"); cr.putQueryParameter("ChangeType", "ADD_PARTITION"); cr.putQueryParameter("ObjectType", "PARTITION"); cr.putQueryParameter("PageNum", String.valueOf(1)); cr.putQueryParameter("PageSize", String.valueOf(3)); CommonResponse cresp = client.getCommonResponse(cr); assertNotNull(cresp); assertNotNull(cresp.getData());
```

### 6.61 ListMetaTableColumn

Queries the information about fields in a table.

| Parameter | Type | Required | Description |
|---|---|---|---|
| TableGuid | String | Yes | The GUID of the table. |

| Parameter | Type | Description |
|---|---|---|
| TableGuid | STRING | The GUID of the table. |
| TableName | STRING | The name of the table. |
| ColumnGuid | STRING | The GUID of the field. |
| ColumnName | STRING | The name of the field. |
| ColumnType | STRING | The type of the field. |
| SeqNumber | INTEGER | The sequence number of the field. |
| IsPartitionCol | INTEGER | Indicates whether the field is a partition field. A value of 1 indicates that the field is a partition field. |
| IsPrimaryKey | INTEGER | Indicates whether the field is a primary key. A value of 1 indicates that the field is a primary key. |
| IsNullable | INTEGER | Indicates whether the field can be null. |
| Comment | STRING | The description of the field. |

Sample code

```java
private String product = "dataworks-private-cloud"; private String version = "2019-01-17"; private String appGuid = "odps.dw_meta"; private String tableGuid = "odps.dw_meta.dwd_d_odps_table"; private String columnName = "table_comment"; CommonRequest cr = new CommonRequest(); cr.setProduct(product); cr.setVersion(version); cr.setMethod(MethodType.GET); cr.setAction("ListMetaTableColumn"); cr.putQueryParameter("TableGuid", tableGuid); CommonResponse cresp = client.getCommonResponse(cr); assertNotNull(cresp); assertNotNull(cresp.getData());
```

### 6.62 ListMetaTableImpact

Queries the impact analysis result of a table.

| Parameter | Type | Required | Description |
|---|---|---|---|
| TableGuid | STRING | Yes | The GUID of the table. |
| ColumnName | STRING | No | The name of the field. |
| Direction | STRING | Yes | Specifies whether to query the impacts on ancestor or descendant tables. Valid values: OUT and PUT. |

| Parameter | Type | Description |
|---|---|---|
| TableGuid | STRING | The GUID of the table. |

Sample code

```java
private String product = "dataworks-private-cloud"; private String version = "2019-01-17"; private String appGuid = "odps.dw_meta"; private String tableGuid = "odps.dw_meta.dwd_d_odps_table"; private String columnName = "table_comment"; CommonRequest cr = new CommonRequest(); cr.setProduct(product); cr.setVersion(version); cr.setMethod(MethodType.GET); cr.setAction("ListMetaTableColumn"); cr.putQueryParameter("TableGuid", tableGuid); cr.putQueryParameter("Direction", "OUTPUT"); cr.putQueryParameter("ColumnName", columnName); CommonResponse cresp = client.getCommonResponse(cr); assertNotNull(cresp); assertNotNull(cresp.getData());
```

### 6.63 ListMetaTableIntroWiki

Queries the instructions on how to use a table.

| Parameter | Type | Required | Description |
|---|---|---|---|
| TableGuid | STRING | Yes | The GUID of the table. |

| Parameter | Type | Description |
|---|---|---|
| TableGuid | STRING | The GUID of the table. |
| GmtCreate | STRING | The time when the table was created. |
| GmtModified | STRING | The time when the table was modified. |
| Creator | STRING | The base ID of the table creator. |
| CreatorName | STRING | The name of the table creator. |
| CreatorBaseId | STRING | The base ID of the table creator. |
| Version | LONG | The version number of Wiki. |

Sample code

```java
private String product = "dataworks-private-cloud"; private String version = "2019-01-17"; private String appGuid = "odps.dw_meta"; private String tableGuid = "odps.dw_meta.dwd_d_odps_table"; private String columnName = "table_comment"; CommonRequest cr = new CommonRequest(); cr.setProduct(product); cr.setVersion(version); cr.setMethod(MethodType.GET); cr.setAction("ListMetaTableIntroWiki"); cr.putQueryParameter("TableGuid", tableGuid); CommonResponse cresp = client.getCommonResponse(cr); assertNotNull(cresp); assertNotNull(cresp.getData());
```

### 6.64 ListMetaTableLineage

Queries the lineage of a table.

| Parameter | Type | Required | Description |
|---|---|---|---|
| TableGuid | STRING | Yes | The GUID of the table. |
| Direction | STRING | Yes | Specifies whether to query the ancestor or descendant lineage of the table. Valid values: UP, DOWN, and ALL. |
| PageNum | INTEGER | No | The number of the page to return. |
| PageSize | INTEGER | No | The number of entries to return on each page. |

| Parameter | Type | Description |
|---|---|---|
| DstTableGuid | STRING | The GUID of the destination table. |
| SrcTableGuid | STRING | The GUID of the source table. |

Sample code

```java
private String product = "dataworks-private-cloud"; private String version = "2019-01-17"; private String appGuid = "odps.dw_meta"; private String tableGuid = "odps.dw_meta.dwd_d_odps_table"; private String columnName = "table_comment"; CommonRequest cr = new CommonRequest(); cr.setProduct(product); cr.setVersion(version); cr.setMethod(MethodType.GET); cr.setAction("ListMetaTableLineage"); cr.putQueryParameter("TableGuid", tableGuid); cr.putQueryParameter("Direction", "ALL"); cr.putQueryParameter("PageNum", String.valueOf(1)); cr.putQueryParameter("PageSize", String.valueOf(3)); CommonResponse cresp = client.getCommonResponse(cr); assertNotNull(cresp); assertNotNull(cresp.getData());
```

### 6.65 ListMetaTableOutput

Queries the information about the node instances that generate data for a table.

| Parameter | Type | Required | Description |
|---|---|---|---|
| TableGuid | STRING | Yes | The GUID of the table. |
| StartDate | STRING | No | The beginning of the time range to query, in the yyyy-MM-dd format. |
| EndDate | STRING | No | The end of the time range to query, in the yyyy-MM-dd format. |
| PageNum | INTEGER | No | The number of the page to return. |
| PageSize | INTEGER | No | The number of entries to return on each page. |

| Parameter | Type | Description |
|---|---|---|
| TableGuid | STRING | The GUID of the table. |
| ProjectId | LONG | The ID of the DataWorks workspace to which the node belongs. |

|   | Developer Guide·Java SDK |   | DataWork | s |
|---|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| TaskId | STRING | The ID of the node. |
| TaskInstId | LONG | The ID of the node instance. |
| StartTime | STRING | The time when the node instance was started. |
| EndTime | STRING | The time when the node instance was ended. |
| ExecuteTime | STRING | The time taken to run the node instance. |
| WaitTime | STRING | The period during which the node instance was waiting to be run. |

Sample code

```java
private String product = "dataworks-private-cloud"; private String version = "2019-01-17"; private String appGuid = "odps.dw_meta"; private String tableGuid = "odps.dw_meta.dwd_d_odps_table"; private String columnName = "table_comment"; CommonRequest cr = new CommonRequest(); cr.setProduct(product); cr.setVersion(version); cr.setMethod(MethodType.GET); cr.setAction("ListMetaTableOutput"); cr.putQueryParameter("TableGuid", tableGuid); cr.putQueryParameter("StartDate", "2020-03-22"); cr.putQueryParameter("EndDate", "2020-03-26"); cr.putQueryParameter("PageNum", String.valueOf(2)); cr.putQueryParameter("PageSize", String.valueOf(2)); CommonResponse cresp = client.getCommonResponse(cr); assertNotNull(cresp); assertNotNull(cresp.getData());
```

### 6.66 ListMetaTablePartition

Queries the partition information of a table.

| Parameter | Type | Required | Description |
|---|---|---|---|
| TableGuid | STRING | Yes | The GUID of the table. |
| PageNum | INTEGER | No | The number of the page to return. |

| D | ataWorks |   |   | Developer Guide·Java SD | K |
|---|---|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| PageSize | INTEGER | No | The number of entries to return on each page. |

| Parameter | Type | Description |
|---|---|---|
| AppGuid | STRING | The GUID of the MaxCompute project. |
| TableGuid | STRING | The GUID of the table. |
| TableName | STRING | The name of the table. |
| PartitionGuid | STRING | The GUID of the partition. |
| PartitionName | STRING | The name of the partition. |
| CreateTime | STRING | The time when the partition was created. |
| ModifyTime | STRING | The time when the partition was modified. |
| DataSize | LONG | The storage space occupied by the partition. |
| Records | LONG | The number of records in the partition. |

Sample code

```java
private String product = "dataworks-private-cloud"; private String version = "2019-01-17"; private String appGuid = "odps.dw_meta"; private String tableGuid = "odps.dw_meta.dwd_d_odps_table"; private String columnName = "table_comment"; CommonRequest cr = new CommonRequest(); cr.setProduct(product); cr.setVersion(version); cr.setMethod(MethodType.GET); cr.setAction("ListMetaTablePartition"); cr.putQueryParameter("TableGuid", tableGuid); cr.putQueryParameter("PageNum", String.valueOf(2)); cr.putQueryParameter("PageSize", String.valueOf(2)); CommonResponse cresp = client.getCommonResponse(cr); assertNotNull(cresp); assertNotNull(cresp.getData());
```

### 6.67 SearchMetaTables

Queries MaxCompute tables.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Keyword | STRING | Yes | The keyword used to query MaxCompute tables. |
| PageNum | INTEGER | No | The number of the page to return. |
| PageSize | INTEGER | No | The number of entries to return on each page. |

| Parameter | Type | Description |
|---|---|---|
| AppGuid | STRING | The GUID of the MaxCompute project. |
| TableGuid | STRING | The GUID of the table. |
| TableName | STRING | The name of the table. |
| CreateTime | STRING | The time when the table was created. |
| LastDdlTime | STRING | The time when the table schema was last changed. |
| LastModifyTime | STRING | The time when the table was last updated. |
| OwnerId | STRING | The base ID of the table owner. |

Sample code

```java
private String product = "dataworks-private-cloud"; private String version = "2019-01-17"; private String appGuid = "odps.dw_meta"; private String tableGuid = "odps.dw_meta.dwd_d_odps_table"; private String columnName = "table_comment"; CommonRequest cr = new CommonRequest(); cr.setProduct(product); cr.setVersion(version); cr.setMethod(MethodType.GET); cr.setAction("SearchMetaTables"); cr.putQueryParameter("Keyword", tableGuid); cr.putQueryParameter("PageNum", String.valueOf(1)); cr.putQueryParameter("PageSize", String.valueOf(2)); CommonResponse cresp = client.getCommonResponse(cr); assertNotNull(cresp); assertNotNull(cresp.getData());
```

### 6.68 GetStorageAndCalcMetrics

Queries the storage and computing data of a specific project or the current Apsara Stack tenant account.

| Parameter | Type | Required | Description |
|---|---|---|---|
| AppGuids | STRING | No | The GUIDs of the MaxCompute projects. The GUIDs are separated with commas (,). |
| DateString | STRING | No | The query date. The default value is the data timestamp. |
| PageSize | INTEGER | No | The number of entries to return on each page. |

| Parameter | Type | Description |
|---|---|---|
| TotalStorage | LONG | The name of the table. |
| TotalCpuCost | LONG | The GUID of the table. |

Sample code

```java
private String product = "dataworks-private-cloud"; private String version = "2019-01-17"; private String appGuid = "odps.dw_meta"; private String tableGuid = "odps.dw_meta.dwd_d_odps_table"; private String columnName = "table_comment"; CommonRequest cr = new CommonRequest(); cr.setProduct(product); cr.setVersion(version); cr.setMethod(MethodType.GET); cr.setAction("GetStorageAndCalcMetrics"); cr.putQueryParameter("AppGuids", appGuid); cr.putQueryParameter("DateString", '2020-01-01'); CommonResponse cresp = client.getCommonResponse(cr); assertNotNull(cresp); assertNotNull(cresp.getData());
```

### 6.69 GetInstanceStatistic

Queries instance statistics.

| Parameter | Required | Type | Description |
|---|---|---|---|
| Bizdate | No | STRING | The data timestamp, in the yyyy-MM-dd format. |
| AppId | No | LONG | The ID of the workspace. |

Sample response

```json
  "ReturnErrorSolution": "",
  "ReturnCode": "0",
  "RequestId": "83190FF7-8EAF-44DB-9170-AC0AXXXX",
  "ReturnMessage": "",
  "ReturnValue": {
    "TotalCount": 15,
    "RunningCount": 0,
    "FailureCount": 0,
    "NotRunCount": 15,
    "SuccessCount": 0,
    "WaitTimeCount": 0,
    "WaitResourceCount": 0
```

`},`

```json
  "Success": true
```

Sample code

```java
@Test public void testGetInstanceStatistic() throws ClientException {
    CommonRpcRequest commonRpcRequest = new CommonRpcRequest(popProduct, popVersion, "GetIn
stanceStatistic");
    commonRpcRequest.setMethod(MethodType.POST);
    String projectId = getTestProperties("projectId");
    String bizdate = getTestProperties("bizdate");
    commonRpcRequest.putQueryParameter("AppId", projectId);
    commonRpcRequest.putQueryParameter("Bizdate", bizdate);
    HttpResponse response = client.doAction(commonRpcRequest);
    System.out.println(GsonUtils.gson.toJson(response.getHttpContentString()));
```

### 6.70 GetInstanceLog

Queries the operational logs of a node instance.

| Parameter | Required | Type | Description |
|---|---|---|---|
| InstanceId | No | LONG | The ID of the instance. |
| ProjectEnv | Yes | STRING | The environment of the node instance. Valid values: PROD and DEV. |

Sample response

```json
  "ReturnErrorSolution": "",
  "ReturnCode": "0",
  "RequestId": "CEC994D9-45BD-4531-B2CE-6XXXX",
  "ReturnMessage": "",
  "ReturnValue": "No operational logs are generated.",
  "Success": true
```

Sample code

```java
@Test
    public void testGetInstanceLog() throws ClientException {
        CommonRpcRequest commonRpcRequest = new CommonRpcRequest(popProduct, popVersion, "G
etInstanceLog");
        commonRpcRequest.setMethod(MethodType.POST);
        Long instanceId = Long.valueOf(getTestProperties("instanceId"));
        String projectEnv = getTestProperties("projectEnv");
        commonRpcRequest.putQueryParameter("InstanceId", instanceId);
        commonRpcRequest.putQueryParameter("ProjectEnv", projectEnv);
        HttpResponse response = client.doAction(commonRpcRequest);
        System.out.println(GsonUtils.gson.toJson(response.getHttpContentString()));
```

### 6.71 GetNodeCode

Queries the code of a node.

| Parameter | Required | Type | Description |
|---|---|---|---|
| NodeId | Yes | LONG | The ID of the node. |
| ProjectEnv | Yes | STRING | The environment of the node. Valid values: PROD and DEV. Default value: PROD. |

Sample response

```json
  "ReturnErrorSolution": "",
  "ReturnCode": "0",
  "RequestId": "30DB3056-F6F1-4A05-88EE-5XXXX",
  "ReturnMessage": "",
  "ReturnValue": "echo 'hello'"
```

Sample code

```java
    @Test
    public void testGetNodeCode() throws ClientException {
        CommonRpcRequest commonRpcRequest = new CommonRpcRequest(popProduct, popVersion, "G
etNodeCode");
        commonRpcRequest.setMethod(MethodType.POST);
        Long nodeId = Long.valueOf(getTestProperties("nodeId"));
        String projectEnv = getTestProperties("projectEnv");
        commonRpcRequest.putQueryParameter("NodeId", nodeId);
        commonRpcRequest.putQueryParameter("ProjectEnv", projectEnv);
        HttpResponse response = client.doAction(commonRpcRequest);
        System.out.println(GsonUtils.gson.toJson(response.getHttpContentString()));
```

### 6.72 QueryInstances

Queries instances.

| Parameter | Required | Type | Description |
|---|---|---|---|
| Bizdate | No | STRING | The data timestamp, in the yyyy-MM-dd format. |
| ProjectId | No | LONG | The ID of the workspace. |
| NodeId | Yes | LONG | The ID of the node. |
| NodeName | Yes | STRING | The name of the node. |
| TaskStatus | Yes | STRING | The status of the node. Valid values: NOT RUN, _ WAIT TIME, _ WAIT RESOURCE, _ RUNNING, CHECKING, CHECKING CONDITION, _ FAILURE, and SUCCESS. |
| ProjectEnv | Yes | STRING | The environment of the node. Valid values: PROD and DEV. |

Sample response

```json
  "ReturnErrorSolution": "",
  "ReturnCode": "0",
  "RequestId": "7AFA7207-2F44-4ECC-AE77-XXXX",
  "ReturnMessage": "",
  "ReturnValue": [
      "Status": "SUCCESS",
      "ModifyTime": 15881766XXXX,
      "InstanceId": 70652XXXX,
      "DagType": "DAILY",
      "NodeName": "Delay node",
      "CreateTime": 1588088309461,
      "CycTime": 1588176600000,
      "BeginWaitTimeTime": 1588176XXXX,
      "DagId": 700126518687,
      "Bizdate": 1588089600000,
      "BeginRunningTime": 1588176671359,
      "FinishTime": 1588176680949,
      "NodeId": 700001891566,
      "BeginWaitResTime": 1588176601707
```

`},`

```json
      "Status": "SUCCESS",
      "ModifyTime": 1588090445868,
      "InstanceId": 706518829092,
      "DagType": "DAILY",
      "NodeName": "Delay node",
      "CreateTime": 1588001922168,
      "CycTime": 1588090200000,
      "BeginWaitTimeTime": 1588089826198,
      "DagId": 700126318686,
      "Bizdate": 1588003200000,
      "BeginRunningTime": 1588090305062,
      "FinishTime": 1588090445868,
      "NodeId": 700001891566,
      "BeginWaitResTime": 1588090203188
```

`]` Sample code

```java
    @Test
    public void testQueryInstances() throws ClientException {
        CommonRpcRequest commonRpcRequest = new CommonRpcRequest(popProduct, popVersion, "Q
ueryInstances");
        commonRpcRequest.setMethod(MethodType.POST);
        String projectId = getTestProperties("projectId");
        String projectEnv = getTestProperties("projectEnv");
        String bizdate = getTestProperties("bizdate");
        String pageNumber = getTestProperties("pageNumber");
        String nodeId = getTestProperties("nodeId");
        String nodeName = getTestProperties("nodeName");
        String taskStatus = getTestProperties("taskStatus");
        commonRpcRequest.putQueryParameter("Bizdate", bizdate);
        commonRpcRequest.putQueryParameter("ProjectId", projectId);
        commonRpcRequest.putQueryParameter("NodeId", nodeId);
        commonRpcRequest.putQueryParameter("PageNumber", pageNumber);
        commonRpcRequest.putQueryParameter("NodeName", nodeName);
        commonRpcRequest.putQueryParameter("ProjectEnv", projectEnv);
        commonRpcRequest.putQueryParameter("TaskStatus", taskStatus);
        HttpResponse response = client.doAction(commonRpcRequest);
        System.out.println(GsonUtils.gson.toJson(response.getHttpContentString()));
```

ey pair

## 7 Obtain an AccessKey pair

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
