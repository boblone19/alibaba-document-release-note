---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Prometheus Service Developer Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 24
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 Prometheus Service Developer Guide 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E5%8F%AF%E8%A7%82%E6%B5%8B%E7%9B%91%E6%8E%A7%20Prometheus%20%E7%89%88/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Prometheus%20Service%20Developer%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Prometheus Service Developer Guide 20260828

## Download SDKs

Prometheus Monitoring provides SDKs for Java, TypeScript, Go, PHP, Python, and C#. This topic describes the methods to download them.

| Download SDK | Download method |
|---|---|
| Download the Java SDK | Add the following Maven dependency to the pom.xml file to download the Java SDK: <dependency> <groupId>com.aliyun</groupId> <artifactId>arms20190808</artifactId> <version>1.0.0</version> </dependency> |
| Download the TypeScript SDK | Run the following command to download the TypeScript SDK: npm install @alicloud/arms20190808@1.0.0 |
| Download the Go SDK | Run the following command to download the Go SDK: go get github.com/alibabacloud-go/arms-20190808 |
| Download the PHP SDK | Run the following command to download the PHP SDK: composer require alibabacloud/arms-20190808 1.0.0 |
| Download the Python SDK | Run the following command to download the Python SDK: pip install alibabacloud arms20190808==1.0.0 _ |
| Download the C# SDK | Run the following command to download the C# SDK: dotnet add package AlibabaCloud.SDK.ARMS20190808 -- version 1.0.0 |

les

## Request examples

This topic provides examples of how to call the ListDashboards API operation to access Prometheus Monitoring. The examples demonstrate how to send HTTP POST requests to retrieve data using different programming languages, such as Java and Python.

**Java request example**

```java
package com.aliyun.sample; import com.aliyun.tea.*; import com.aliyun.arms20190808.*; import com.aliyun.arms20190808.models.*; import com.aliyun.teaopenapi.*; import com.aliyun.teaopenapi.models.*; public class Sample {
 /**
 * Use the AccessKey ID and AccessKey secret to initialize the client.
```

`*`

```
 * @param accessKeyId
 * @param accessKeySecret
 * @return Client
 * @throws Exception
```

`*/`

```java
 public static com.aliyun.arms20190808.Client createClient(String accessKeyId, String
accessKeySecret) throws Exception {
 Config config = new Config().setAccessKeyId(accessKeyId)
                    .setAccessKeySecret(accessKeySecret)
                    .setRegionId(“${regionId}”); // The region ID where the Prometheus p
roduct is located.
 config.endpoint = "${proxy_prometheus_api_domain}"; // The POP domain name of the Prom
etheus product.
 return new com.aliyun.arms20190808.Client(config);
 public static void main(String[] args_) throws Exception {
 com.aliyun.arms20190808.Client client =createClient("accessKeyId", "accessKeySecret");
 ListDashboardsRequestl istDashboardsRequest = new ListDashboardsRequest();
 listDashboardsRequest.setClusterId("clusterId");
 listDashboardsRequest.setRegionId("regionIdValue");
 ListDashboardsResponse response =client.listDashboards(listDashboardsRequest);
 System.out.println(response.body);
```

**TypeScript request example**

les

```java
import ARMS20190808, * as $ARMS20190808 from '@alicloud/arms20190808'; // For information about module dependencies, download the module dependency file for t he project or check the SDK dependency information in the upper-right corner. import OpenApi, * as $OpenApi from '@alicloud/openapi-client'; import * as $tea from '@alicloud/tea-typescript'; export default class Client {
 /**
 * Use the AccessKey ID and AccessKey secret to initialize the client.
 * @param accessKeyId
 * @param accessKeySecret
 * @return Client
 * @throws Exception
```

`*/`

```
 static createClient(accessKeyId: string, accessKeySecret: string): ARMS20190808 {
 let config = new $OpenApi.Config({
 accessKeyId: accessKeyId,
 accessKeySecret: accessKeySecret,
 regionId: “${regionId}”, // The region ID where the Prometheus product is located.
 });
 // The domain name to access.
 config.endpoint = "${proxy_prometheus_api_domain}"; // The POP domain name of the Prom
etheus product.
 return new ARMS20190808(config);
 static async main(args: string[]): Promise<void> {
 let client = Client.createClient("accessKeyId", "accessKeySecret");
       let listDashboardsRequest = new $ARMS20190808.ListDashboardsRequest({ });
       ... // Set business parameters.
 await client.listDashboards(listDashboardsRequest);
Client.main(process.argv.slice(2));
```

**Go request example**

les

```java
package main import (
 "os"
 arms20190808"github.com/alibabacloud-go/arms-20190808/client"
 openapi"github.com/alibabacloud-go/darabonba-openapi/client"
 "github.com/alibabacloud-go/tea/tea"
```

`)`

```
/**
* Use the AccessKey ID and AccessKey secret to initialize the client.
* @param accessKeyId
* @param accessKeySecret
* @return Client
* @throws Exception
```

`*/`

```
func CreateClient (accessKeyId *string, accessKeySecret *string) (_result *arms20190808 .Client, _err error) {
 config := &openapi.Config{
 AccessKeyId: accessKeyId,
       AccessKeySecret: accessKeySecret,
       RegionId:“${regionId}”, // The region ID where the Prometheus product is
located.
 // The domain name to access.
 config.Endpoint = tea.String("${proxy_prometheus_api_domain}") // The POP domain name
of the Prometheus product.
 _result = &arms20190808.Client{}
 _result, _err = arms20190808.NewClient(config)
 return _result, _err
func _main (args []*string) (_err error) {
 client, _err := CreateClient(tea.String("accessKeyId"), tea.String("accessKeySecret"))
 if _err != nil {
 return _err
 listDashboardsRequest := &arms20190808.ListDashboardsRequest{}
 ... // Set business parameters.
 _, _err = client.ListDashboards(listDashboardsRequest)
 if _err != nil {
 return _err
 return _err
func main() {
 err := _main(tea.StringSlice(os.Args[1:]))
 if err != nil {
 panic(err)
```

les

**PHP request example**

```
<?php namespace AlibabaCloud\SDK\Sample; use AlibabaCloud\SDK\ARMS\V20190808\ARMS; use Darabonba\OpenApi\Models\Config; use AlibabaCloud\SDK\ARMS\V20190808\Models\ListDashboardsRequest; class Sample {
 /**
 * Use the AccessKey ID and AccessKey secret to initialize the client.
 * @param string $accessKeyId
 * @param string $accessKeySecret
 * @return ARMS Client
```

`*/`

```
 public static function createClient($accessKeyId, $accessKeySecret){
 $config = new Config([
 "accessKeyId" => $accessKeyId,
 "accessKeySecret" => $accessKeySecret
         "regionId" => “${regionId}” // The region ID where the Prometheus product is
located.
    ]);
   // The domain name to access.
   $config->endpoint = "${proxy_prometheus_api_domain}"; // The POP domain name of the
Prometheus product.
   return new ARMS($config);
 /**
 * @param string[] $args
 * @return void
```

`*/`

```
 public static function main($args){
 $client = self::createClient("accessKeyId", "accessKeySecret");
 $listDashboardsRequest = new ListDashboardsRequest([]);
 ... // Set business parameters.
               $client->listDashboards($listDashboardsRequest);
$path = __DIR__ . \DIRECTORY_SEPARATOR . '..' . \DIRECTORY_SEPARATOR . 'vendor' . \DIRE CTORY_SEPARATOR . 'autoload.php'; if (file_exists($path)) {
 require_once $path;
Sample::main(array_slice($argv, 1));
```

**Python request example**

```java
# -*- coding: utf-8
-*import sys fromtypingimportList
```

| l | Developer Guide·Request examp Prometheus Servic es | e |
|---|---|---|
| from typing import List from alibabacloud arms20190808.client import Client as ARMS20190808Client _ from alibabacloud tea openapi import models as open api models _ _ _ _ from alibabacloud arms20190808 import models as arms20190808 models _ _ class Sample: def init (self): __ __ pass @staticmethod def create client( _ access key id: str, _ _ access key secret: str, _ _ region id: str, _ ) -> ARMS20190808Client: """ Use the AccessKey ID and AccessKey secret to initialize the client. @param access key id: _ _ @param access key secret: _ _ @return: Client @throws Exception """ config = open api models.Config( _ _ # Your AccessKey ID. access key id=access key id, _ _ _ _ # Your AccessKey secret. access key secret=access key secret _ _ _ _ region id=“${regionId}” // The region ID where the Prometheus pro _ duct is located. ) # The domain name to access. config.endpoint = "${proxy prometheus api domain}" # The POP domain name of the Promet _ _ _ heus product. return ARMS20190808Client(config) @staticmethod def main( args: List[str], ) -> None: client = Sample.create client('accessKeyId', 'accessKeySecret') _ list dashboards request = arms20190808 models.ListDashboardsRequest() _ _ _ ... # Set business parameters. client.list dashboards(list dashboards request) _ _ _ @staticmethod async def main async( _ args: List[str], ) -> None: client = Sample.create client('accessKeyId', 'accessKeySecret') _ list dashboards request = arms20190808 models.ListDashboardsRequest() _ _ _ ... # Set business parameters. await client.list dashboards async(list dashboards request) _ _ _ _ if name == ' main ': __ __ __ __ Sample.main(sys.argv[1:]) | from typing import List from alibabacloud arms20190808.client import Client as ARMS20190808Client _ from alibabacloud tea openapi import models as open api models _ _ _ _ from alibabacloud arms20190808 import models as arms20190808 models _ _ class Sample: def init (self): __ __ pass @staticmethod def create client( _ access key id: str, _ _ access key secret: str, _ _ region id: str, _ ) -> ARMS20190808Client: """ Use the AccessKey ID and AccessKey secret to initialize the client. @param access key id: _ _ @param access key secret: _ _ @return: Client @throws Exception """ config = open api models.Config( _ _ # Your AccessKey ID. access key id=access key id, _ _ _ _ # Your AccessKey secret. access key secret=access key secret _ _ _ _ region id=“${regionId}” // The region ID where the Prometheus pro _ duct is located. ) # The domain name to access. config.endpoint = "${proxy prometheus api domain}" # The POP domain name of the Promet _ _ _ heus product. return ARMS20190808Client(config) @staticmethod def main( args: List[str], ) -> None: client = Sample.create client('accessKeyId', 'accessKeySecret') _ list dashboards request = arms20190808 models.ListDashboardsRequest() _ _ _ ... # Set business parameters. client.list dashboards(list dashboards request) _ _ _ @staticmethod async def main async( _ args: List[str], ) -> None: client = Sample.create client('accessKeyId', 'accessKeySecret') _ list dashboards request = arms20190808 models.ListDashboardsRequest() _ _ _ ... # Set business parameters. await client.list dashboards async(list dashboards request) _ _ _ _ if name == ' main ': __ __ __ __ Sample.main(sys.argv[1:]) |   |

les `p` `(``y` `g``[` `])`

**C# request example**

```
using System; using System.Collections; using System.Collections.Generic; using System.IO; using System.Threading.Tasks; using Tea; using Tea.Utils; namespace AlibabaCloud.SDK.Sample
```

`{`

```java
 public class Sample
```

`{`

```
 /**
 * Use the AccessKey ID and AccessKey secret to initialize the client.
 * @param accessKeyId
 * @param accessKeySecret
 * @return Client
 * @throws Exception
```

`*/`

```
 public static AlibabaCloud.SDK.ARMS20190808.Client CreateClient(string accessKeyId, st
ring accessKeySecret)
```

`{`

```
 AlibabaCloud.OpenApiClient.Models.Config config = new
AlibabaCloud.OpenApiClient.Models.Config
```

`{`

```
 AccessKeyId = accessKeyId,
 AccessKeySecret = accessKeySecret,
                               regionId = “${regionId}”, // The region ID where the Prom
etheus product is located.
```

};

```
 // The domain name to access.
 config.Endpoint = "${proxy_prometheus_api_domain}"; // The POP domain name of the Prom
etheus product.
 return new AlibabaCloud.SDK.ARMS20190808.Client(config);
 public static void Main(string[] args)
```

`{`

```
 AlibabaCloud.SDK.ARMS20190808.Client client = CreateClient("accessKeyId",
"accessKeySecret");
 AlibabaCloud.SDK.ARMS20190808.Models.ListDashboardsRequest listDashboardsRequest = new
AlibabaCloud.SDK.ARMS20190808.Models.ListDashboardsRequest();
 ... // Set business parameters.
 client.ListDashboards(listDashboardsRequest);
```

meters

## Obtain API parameters

This topic describes how to obtain the parameters required to access the Prometheus monitoring developer API. These parameters allow you to quickly access the Platform Open Protocol (POP) API for Prometheus monitoring.

**Obtain the POP domain name for Prometheus monitoring**

As shown in the following figure, the value of `"proxy_prometheus_api_domain":` is the POP domain name for Prometheus monitoring. Contact technical support to obtain this domain name.

**Obtain the RegionId**

Contact technical support to obtain the RegionId for the current environment.

**Obtain the AccessKey pair**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the interface, click the profile picture, and then click **Personal**
**Information**.
3. In the Alibaba Cloud **AccessKey** section, find the AccessKey information for your account.

## API reference

### ListDashboards

Call the ListDashboards operation to retrieve a list of Grafana dashboards for a cluster.

**Request parameters**

| Name | Type | Requir ed | Example | Description |   |   |
|---|---|---|---|---|---|---|
| Action | String | Yes | ListDashboards | A required parameter. Set the value to ListDashboards. |   |   |
| ClusterId | String | Yes | cc7a37ee31aea 4ed1a059eff803 4b**** | The ID of the Container Service for Kubernetes (ACK) cluster. |   |   |
| RegionId | String | Yes | cn-hangzhou | The region ID. |   |   |
| ClusterType | String | No | Node | The cluster type. Use this parameter to query the dashboard list for a virtual cluster. |   |   |
| Title | String | No | ApiServer | The title of the dashboard. The dashboard title may change. Use the DashboardName parameter for queries. |   |   |
| Product | String | No | xxxx | The code of the cloud product. |   |   |
| RecreateSwitch | Boolean | No | false | A switch that controls the creation or query of virtual clusters. It ensures compatibility with historical data. |   |   |
| DashboardName | String | No | k8s-node- overview | The unique names of the dashboards. You can query dashboards by specifying their names. Unlike the Title parameter, the Title can change, but the name does not. You can also specify multiple names separated by commas (,). For example: k8s-event,k8s- overview . A dashboard can have multiple versions under the same name. To specify a version, append the version information to the name, for example: k8s-event:v1,k8s- overview:latest . |   |   |
|   |   |   |   |   | k8s-event:v1,k8s- |   |
|   |   |   |   | overview:latest |   |   |

|   |   | k8s-event,k8s- |
|---|---|---|
|   | overview |   |

**Response parameters**

| Name | Type | Example | Description |
|---|---|---|---|
| DashboardVos | Array of DashboardVos |   | The information about the Grafana dashboards. |
| DashboardTyp e | String | Node | The dashboard type. This parameter has the same function as Exporter, but its meaning is more specific. |
| Exporter | String | Nginx | The type of the exporter source. Valid values include the following: Prometheus Node GPU Redis MySQL Kafka Nginx (v2) Nginx ZooKeeper MongoDB RabbitMQ PostgreSQL Kubernetes Client Library Elasticsearch RocketMQ |
| HttpUrl | String | http://g.console.ali yun.com/d/113197 1649496228-*****- 59/ApiServer? orgId=3**&refresh =60s | The URL of the dashboard. |
| HttpsUrl | String | http://g.console.ali yun.com/d/113197 1649496228-*****- 59/ApiServer? orgId=3**&refresh =60s | The URL of the dashboard. |

| Id | String | 1100** | The ID of the Grafana dashboard. This ID is unique only when the Grafana dashboard is installed. |
|---|---|---|---|
| IsArmsExporte r | Boolean | false | Indicates whether the exporter is provided by ARMS: true: The exporter is provided by ARMS. false: The exporter is not provided by ARMS. |
| Kind | String | BASIC | The type of the dashboard. Valid values: BASIC, THIRD, LIMIT, and CUSTOM. |
| Name | String | k8s-node-overview | The name of the dashboard. Unlike the Title, the name does not change. |
| NeedUpdate | Boolean | false | Indicates whether a new version of the dashboard is available for upgrade. |
| Tags | List | ["arms- k8s","ccc8ce1fe0c 9543629e39ee657 e34****"] | The tags of the Grafana dashboard. |
| Time | String | 1590136924 | The UNIX timestamp for when the Grafana dashboard was created. |
| Title | String | ApiServer | The title of the Grafana dashboard. |
| Type | String | dash-db | The type of the Grafana dashboard. Valid values: dash-db: dashboard dash-folder: folder (can contain dashboards) |
| Uid | String | 113197164949622 8-*****-59 | The unique identifier of the dashboard when multiple Grafana dashboards are installed. This is the unique business ID displayed on the page. |
| Url | String | http://g.console.ali yun.com/d/113197 1649496228-*****- 59/ApiServer? orgId=3**&refresh =60s | The complete URL of the Grafana dashboard. |

| Version | String | v2 | The version of the dashboard. This parameter and the name form a unique key to identify a dashboard. |
|---|---|---|---|
| RequestId | String | 2A0CEDF1-06FE- 44AC-8E21- 21A5BE65**** | The request ID. |

**Examples**

Sample request

```
http(s)://[Endpoint]/?Action=ListDashboards &ClusterId=cc7a37ee31aea4ed1a059eff8034b**** &RegionId=cn-hangzhou &<Common request parameters>
```

Sample responses `XML` format

```xml
<DashboardVos>
    <Title>ApiServer</Title>
    <Time>1590136924</Time>
    <Exporter>Nginx</Exporter>
    <HttpUrl>http://g.console.aliyun.com/d/1131971649496228-*****-59/ApiServer?
orgId=3**&amp;refresh=60s</HttpUrl>
    <Url>http://g.console.aliyun.com/d/1131971649496228-*****-59/ApiServer?
orgId=3**&amp;refresh=60s</Url>
    <Name>k8s-node-overview</Name>
    <Uid>1131971649496228-*****-59</Uid>
    <Type>dash-db</Type>
    <NeedUpdate>false</NeedUpdate>
    <Version>v2</Version>
    <Kind>BASIC</Kind>
    <Id>1100**</Id>
    <DashboardType>Node</DashboardType>
    <HttpsUrl>http://g.console.aliyun.com/d/1131971649496228-*****-59/ApiServer?orgId=3
**&amp;refresh=60s</HttpsUrl>
    <IsArmsExporter>false</IsArmsExporter>
    <Tags>["arms-k8s","ccc8ce1fe0c9543629e39ee657e34****"]</Tags>
</DashboardVos> <RequestId>2A0CEDF1-06FE-44AC-8E21-21A5BE65****</RequestId>
```

`JSON` format `{`

```json
    "DashboardVos": {
        "Title": "ApiServer",
        "Time": 1590136924,
        "Exporter": "Nginx",
        "HttpUrl": "http://g.console.aliyun.com/d/1131971649496228-*****-59/ApiServer?o
rgId=3**&amp;refresh=60s",
        "Url": "http://g.console.aliyun.com/d/1131971649496228-*****-59/ApiServer?
orgId=3**&amp;refresh=60s",
        "Name": "k8s-node-overview",
        "Uid": "1131971649496228-*****-59",
        "Type": "dash-db",
        "NeedUpdate": false,
        "Version": "v2",
        "Kind": "BASIC",
        "Id": "1100**",
        "DashboardType": "Node",
        "HttpsUrl": "http://g.console.aliyun.com/d/1131971649496228-*****-59/ApiServer?
orgId=3**&amp;refresh=60s",
        "IsArmsExporter": false,
        "Tags": "[\"arms-k8s\",\"ccc8ce1fe0c9543629e39ee657e34****\"]"
```

`},`

```json
    "RequestId": "2A0CEDF1-06FE-44AC-8E21-21A5BE65****"
```

### SearchAlertContact

You can call the SearchAlertContact operation to query alert contacts.

**Request parameters**

| Name | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SearchAlertCont act | A required parameter. Set the value to SearchAlertContact. |
| RegionId | String | Yes | cn-hangzhou | The region ID. |
| ContactName | String | No | John Doe | The name of the alert contact. |
| Phone | String | No | 1381111**** | The phone number of the alert contact. |
| Email | String | No | someone@exam ple.com | The email address of the contact. |

| CurrentPage | String | No | 1 | The number of the page to return. |
|---|---|---|---|---|
| PageSize | String | No | 20 | The number of items to return on each page. |
| ContactIds | String | No | [12345] | The ID of the alert contact. |

**Response parameters**

| Name | Type | Example | Description |
|---|---|---|---|
| PageBean | Struct |   | The returned struct. |
| Contacts | Array of Contact |   | A list of contact objects. |
| ContactId | Long | 123 | The contact ID. |
| ContactName | String | John Doe | The contact name. |
| CreateTime | Long | 1572349025000 | The creation timestamp. |
| DingRobot | String | https://oapi.dingtal k.com/robot/send? access token=91f2 _ f6**** | The Webhook URL of the DingTalk robot. |
| Email | String | someone@exampl e.com | The email address of the contact. |
| Phone | String | 1381111**** | The phone number of the contact. |
| SystemNoc | Boolean | false | Indicates whether the contact receives system notifications: true: The contact receives system notifications. false: The contact does not receive system notifications. |
| UpdateTime | Long | 1580258717000 | The update timestamp. |

| UserId | String | 113197164949**** | The user ID. |
|---|---|---|---|
| Webhook | String | {\"body\":\"{ \\\"msg type\\\": _ \\\"text\\\", \\\"content\\\": { \\\"text\\\": \\\"$content\\\" } }\",\"header\": {\"Arms-Content- Type\":\"json\"},\" method\":\"post\",\ "params\": {},\"url\":\"https://* **",\"userId\":\"113 1971649***\"}", | The webhook information. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of items returned per page. |
| TotalCount | Integer | 23 | The total number of items returned. |
| RequestId | String | 21E85B16-75A6- 429A-9F65- 8AAC9A54**** | The request ID. |

**Examples**

Request example

```
http(s)://[Endpoint]/?Action=SearchAlertContact &RegionId=cn-hangzhou &<Common request parameters>
```

Response example `XML` format

```xml
<PageBean>
    <TotalCount>23</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <Contacts>
        <Email>someone@example.com</Email>
        <UserId>113197164949****</UserId>
        <Phone>1381111****</Phone>
        <CreateTime>1572349025000</CreateTime>
        <UpdateTime>1580258717000</UpdateTime>
        <Webhook>{\"body\":\"{ \\\"msg_type\\\": \\\"text\\\", \\\"content\\\": {
\\\"text\\\": \\\"$content\\\" } }\",\"header\":{\"Arms-Content- Type\":\"json\"},\"method\":\"post\",\"params\": {},\"url\":\"https://***",\"userId\":\"1131971649***\"}",</Webhook>
        <ContactId>123</ContactId>
        <DingRobot>https://oapi.dingtalk.com/robot/send?access_token=91f2f6****
</DingRobot>
        <SystemNoc>false</SystemNoc>
        <ContactName>John Doe</ContactName>
    </Contacts>
</PageBean> <RequestId>21E85B16-75A6-429A-9F65-8AAC9A54****</RequestId>
```

`JSON` format `{`

```json
    "PageBean": {
        "TotalCount": 23,
        "PageSize": 10,
        "PageNumber": 1,
        "Contacts": {
            "Email": "someone@example.com",
            "UserId": "113197164949****",
            "Phone": "1381111****",
            "CreateTime": 1572349025000,
            "UpdateTime": 1580258717000,
            "Webhook": "{\\\"body\\\":\\\"{ \\\\\\\"msg_type\\\\\\\": \\\\\\\"text\\\\\\
\", \\\\\\\"content\\\\\\\": { \\\\\\\"text\\\\\\\": \\\\\\\"$content\\\\\\\" } }\\\",\ \\"header\\\":{\\\"Arms-Content- Type\\\":\\\"json\\\"},\\\"method\\\":\\\"post\\\",\\\"params\\\": {},\\\"url\\\":\\\"https://***\",\\\"userId\\\":\\\"1131971649***\\\"}\",",
            "ContactId": 123,
            "DingRobot": "https://oapi.dingtalk.com/robot/send?
access_token=91f2f6****",
            "SystemNoc": false,
            "ContactName": "John Doe"
```

`},`

```json
    "RequestId": "21E85B16-75A6-429A-9F65-8AAC9A54****"
```

### SearchAlertContactGroup

You can call the SearchAlertContactGroup operation to query alert contact groups.

**Request parameters**

| Name | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SearchAlertCont actGroup | The required parameter. Set the value to SearchAlertContactGroup. |
| RegionId | String | Yes | cn-hangzhou | The region ID. |
| ContactGroupNa me | String | No | TestGroup | The name of the alert contact group. |
| ContactName | String | No | John Doe | The name of the alert contact. |
| ContactId | Long | No | 123 | The ID of the alert contact. Call the SearchAlertContact operation to obtain the contact ID. |
| ContactGroupIds | String | No | 746 | The ID of the alert contact group. You can specify multiple IDs. Separate them with commas (,). |
| IsDetail | Boolean | No | true | Specifies whether to return all contacts in the contact group. By default, the contacts are not returned. |

**Response parameters**

| Name | Type | Example | Description |
|---|---|---|---|
| ContactGroups | Array of ContactGroup |   | The information about the alert contact groups. |
| ContactGroupI d | Long | 746 | The ID of the alert contact group. |
| ContactGroup Name | String | TestGroup | The name of the alert contact group. |

| Contacts | Array of Contact |   | A list of contact objects. |
|---|---|---|---|
| ContactId | Long | 123 | The ID of the contact. |
| ContactName | String | John Doe | The name of the contact. |
| CreateTime | Long | 1572349025000 | The UNIX timestamp for the creation time. |
| DingRobot | String | https://oapi.dingtal k.com/robot/send? access token=91f2 _ f6**** | The webhook URL of the DingTalk robot. |
| Email | String | someone@exampl e.com | The email address of the contact. |
| Phone | String | 1381111**** | The phone number of the contact. |
| SystemNoc | Boolean | false | Specifies whether the contact receives system notifications. true: Receives system notifications. false: Does not receive system notifications. |
| UpdateTime | Long | 1580258717000 | The UNIX timestamp for the update time. |
| UserId | String | 113197164949**** | The user ID. |
| CreateTime | Long | 1529668855000 | The UNIX timestamp for the creation time. |
| UpdateTime | Long | 1529668855000 | The UNIX timestamp for the update time. |
| UserId | String | 113197164949**** | The user ID. |
| RequestId | String | 4D6C358A-A58B- 4F4B-94CE- F5AAF023**** | The request ID. |

**Examples**

Request example

```
http(s)://[Endpoint]/?Action=SearchAlertContactGroup &RegionId=cn-hangzhou &<Common request parameters>
```

Response example `XML` format

```xml
<ContactGroups>
    <ContactGroupId>746</ContactGroupId>
    <ContactGroupName>TestGroup</ContactGroupName>
    <UserId>113197164949****</UserId>
    <CreateTime>1529668855000</CreateTime>
    <UpdateTime>1529668855000</UpdateTime>
    <Contacts>
        <Email>someone@example.com</Email>
        <UserId>113197164949****</UserId>
        <Phone>1381111****</Phone>
        <CreateTime>1572349025000</CreateTime>
        <UpdateTime>1580258717000</UpdateTime>
        <ContactId>123</ContactId>
        <DingRobot>https://oapi.dingtalk.com/robot/send?access_token=91f2f6****
</DingRobot>
        <SystemNoc>false</SystemNoc>
        <ContactName>John Doe</ContactName>
    </Contacts>
</ContactGroups> <RequestId>4D6C358A-A58B-4F4B-94CE-F5AAF023****</RequestId>
```

`JSON` format `{`

```json
    "ContactGroups": {
        "ContactGroupId": 746,
        "ContactGroupName": "TestGroup",
        "UserId": "113197164949****",
        "CreateTime": 1529668855000,
        "UpdateTime": 1529668855000,
        "Contacts": {
            "Email": "someone@example.com",
            "UserId": "113197164949****",
            "Phone": "1381111****",
            "CreateTime": 1572349025000,
            "UpdateTime": 1580258717000,
            "ContactId": 123,
            "DingRobot": "https://oapi.dingtalk.com/robot/send?
access_token=91f2f6****",
            "SystemNoc": false,
            "ContactName": "John Doe"
```

`},`

```json
    "RequestId": "4D6C358A-A58B-4F4B-94CE-F5AAF023****"
```
