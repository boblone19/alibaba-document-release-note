---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 OpenTrek OpenTrek Dev Developer Guide 20260901"
product_version: "V3.18.6_2607"
doc_version: "20260901"
pdf_pages: 279
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 OpenTrek OpenTrek Dev Developer Guide 20260901.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/OpenTrek/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20OpenTrek%20OpenTrek%20Dev%20Developer%20Guide%2020260901.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 OpenTrek OpenTrek Dev Developer Guide 20260901

## Platform Function Class

Interface services related to the platform control area

### Use the SDK

#### Use POP gateway to call Apsara Stack API

**operations**

**1.1.1.1. Overview**

Apsara Stack is the same as the public cloud, you can use the POP gateway to make API calls. This topic describes the overview.

**Background information**

You can use the POP gateway to call Apsara Stack API operations to add, delete, modify, and query resources at the control layer, such as instances, topics, and groups. The platform has an SDK that supports the Java language. You can directly call Apsara Stack APIs by downloading the SDK in the platform. The sample code of the SDK API in the documentation is for reference only. For more information about the complete steps and parameters of each API, see Developer Portal SDK examples and OpenAPI documentation.

**Environmental requirements**

Supports JDK8 to JDK19 Platform support: Linux, Mac, Windows

**Language**

Currently, only the Java language is supported.

**Publishing History**

**SDK version**

| Version number | Release Time | Update Content |
|---|---|---|
| 3.16.2-0 | 2024.09 | The SDK for external APIs of Apsara Stack 3.16.2 is newly released. |

**Operations**

The list of APIs supported by the current Apsara Stack Enterprise SDK.

| API Name | Version |
|---|---|
| BindSystemTags | 3.16.2-0 |
| CheckFortestConsumerId | 3.16.2-0 |
| CheckFortestInstance | 3.16.2-0 |
| CheckFortestRamAction | 3.16.2-0 |

| CheckFortestTopic | 3.16.2-0 |
|---|---|
| CreateCloudInfo | 3.16.2-0 |
| CreateCloudRouterTask | 3.16.2-0 |
| CreateDeploymentMqConnector | 3.16.2-0 |
| CreateEmpower | 3.16.2-0 |
| CreateEmpowerBySub | 3.16.2-0 |
| CreateGroup | 3.16.2-0 |
| CreateGroupEmpowerBySub | 3.16.2-0 |
| CreateInstance | 3.16.2-0 |
| CreateTopic | 3.16.2-0 |
| CreateUnitResetTask | 3.16.2-0 |
| CreateVpcTunnelInstanceSingleTunnel | 3.16.2-0 |
| DeleteCloudInfo | 3.16.2-0 |
| DeleteCloudRouterTask | 3.16.2-0 |
| DeleteDeploymentMqConnector | 3.16.2-0 |
| DeleteEmpower | 3.16.2-0 |
| DeleteGroup | 3.16.2-0 |
| DeleteGroupEmpower | 3.16.2-0 |
| DeleteInstance | 3.16.2-0 |
| DeleteTopic | 3.16.2-0 |
| DeleteTraceQueryTask | 3.16.2-0 |
| DeleteVpcTunnelInstanceSingleTunnel | 3.16.2-0 |

| DeployDeploymentMqConnector | 3.16.2-0 |
|---|---|
| DownloadMessage | 3.16.2-0 |
| DownloadMessageAllInDLQ | 3.16.2-0 |
| DownloadMessageBodyInDLQ | 3.16.2-0 |
| PageQueryCloudRouterTask | 3.16.2-0 |
| PageQueryGroupList | 3.16.2-0 |
| PageQueryTopicList | 3.16.2-0 |
| PageQueryTraceListByUserId | 3.16.2-0 |
| PauseMqConnector | 3.16.2-0 |
| PushMessage | 3.16.2-0 |
| QueryAllConsumerAccumulation | 3.16.2-0 |
| QueryCloudInfo | 3.16.2-0 |
| QueryCloudRouterItems | 3.16.2-0 |
| QueryCloudRouterTask | 3.16.2-0 |
| QueryCloudRouterTaskStats | 3.16.2-0 |
| QueryClusterCapacity | 3.16.2-0 |
| QueryClusterList | 3.16.2-0 |
| QueryCommonGenRedirectUrl | 3.16.2-0 |
| QueryCommonRegionData | 3.16.2-0 |
| QueryConsumerAccumulate | 3.16.2-0 |
| QueryConsumerConnection | 3.16.2-0 |
| QueryConsumerJstackInfo | 3.16.2-0 |

| QueryConsumerProgress | 3.16.2-0 |
|---|---|
| QueryConsumerStatus | 3.16.2-0 |
| QueryConsumerTimespan | 3.16.2-0 |
| QueryEmpowerList | 3.16.2-0 |
| QueryGroupEmpowerList | 3.16.2-0 |
| QueryGroupIdList | 3.16.2-0 |
| QueryGroupList | 3.16.2-0 |
| QueryGroupSubDetail | 3.16.2-0 |
| QueryInstanceBaseInfo | 3.16.2-0 |
| QueryInstanceList | 3.16.2-0 |
| QueryInstanceStatistics | 3.16.2-0 |
| QueryMessageById | 3.16.2-0 |
| QueryMessageByIdInDLQ | 3.16.2-0 |
| QueryMessageByKey | 3.16.2-0 |
| QueryMessageByPagedDLQ | 3.16.2-0 |
| QueryMessageByPagedTopic | 3.16.2-0 |
| QueryMetaData | 3.16.2-0 |
| QueryMqConnectorDeploymentList | 3.16.2-0 |
| QueryMqConnectorInfoList | 3.16.2-0 |
| QueryMqConnectorMetricsDetailList | 3.16.2-0 |
| QueryMqConnectorSysResourceName | 3.16.2-0 |
| QueryPubTraceByQueryId | 3.16.2-0 |

| QueryRegionConsoleUrlList | 3.16.2-0 |
|---|---|
| QueryRegionList | 3.16.2-0 |
| QueryRouterInstanceList | 3.16.2-0 |
| QueryRouterTopicList | 3.16.2-0 |
| QuerySubscriptionList | 3.16.2-0 |
| QuerySystemTagList | 3.16.2-0 |
| QueryTopic | 3.16.2-0 |
| QueryTopicList | 3.16.2-0 |
| QueryTopicListByGroupId | 3.16.2-0 |
| QueryTopicNameList | 3.16.2-0 |
| QueryTopicStatus | 3.16.2-0 |
| QueryTopicSubDetail | 3.16.2-0 |
| QueryTraceByMsgId | 3.16.2-0 |
| QueryTraceByMsgKey | 3.16.2-0 |
| QueryTraceByMsgTopic | 3.16.2-0 |
| QueryTraceMapByQueryId | 3.16.2-0 |
| QueryTrendFlowLimit | 3.16.2-0 |
| QueryTrendGroupOutputTps | 3.16.2-0 |
| QueryTrendTopicInputTps | 3.16.2-0 |
| QueryUnitLatestConsumerTime | 3.16.2-0 |
| QueryUnitResetTask | 3.16.2-0 |
| QueryVpcTunnelInstanceSingleTunnelList | 3.16.2-0 |

| QueryVpcTunnelTunnelSwitch | 3.16.2-0 |
|---|---|
| ResendMessageByIdInDLQ | 3.16.2-0 |
| ResetConsumerOffset | 3.16.2-0 |
| ResumeMqConnector | 3.16.2-0 |
| SearchRouterTask | 3.16.2-0 |
| SearchSubscription | 3.16.2-0 |
| SendMessage | 3.16.2-0 |
| StartCloudRouterTask | 3.16.2-0 |
| StopCloudRouterTask | 3.16.2-0 |
| TraceMessage | 3.16.2-0 |
| UnbindSystemTags | 3.16.2-0 |
| UpdateCloudInfo | 3.16.2-0 |
| UpdateCloudRouterTask | 3.16.2-0 |
| UpdateConsumerReadableByTopicAndGroup | 3.16.2-0 |
| UpdateGroupConsumer | 3.16.2-0 |
| UpdateGroupInfo | 3.16.2-0 |
| UpdateInstance | 3.16.2-0 |
| UpdateMqConnectorDeployment | 3.16.2-0 |
| UpdateTopic | 3.16.2-0 |
| UpdateTopicInfo | 3.16.2-0 |

**1.1.1.2. Call Preposition**

Apsara Stack is the same as the public cloud, you can use the POP gateway to make API calls. This topic describes the preparations that you must make before you call this operation.

**Background information**

**g**

To keep Apsara Stack in the same way as the public cloud and enable you to have a more convenient and consistent experience, we recommend that you use the POP gateway to call Apsara Stack APIs.

**Obtain the endpoint of a cloud service**

**Access the developer portal**

1. Log on to the Apsara Uni-manager Operations console.
2. In the top navigation bar, choose **Products** > **Development Tools** > **APIs and Tools** > **Developer**
**Portal**.
3. On the **Developer Portal** page, choose **API Integration** > **API Debugging**.
4. In the left-side navigation pane, select the target cloud service.
5. Select an API version from the **Version** drop-down list.
6. In the API list below, you can view all APIs of the current version.
7. Select the operation that you want to view and obtain the POP endpoint of the cloud service.

**Obtain a value from the basic O&M platform of the**

When you call Apsara Stack APIs by using the POP gateway, you must use the endpoints of the business domains of cloud services. You can obtain it from Alibaba Cloud on-site O&M engineers. You can also obtain the endpoint by yourself. This topic describes how to obtain the endpoint of a cloud service domain.
1. Log on to the Apsara Uni-manager Operations console.
2. In the top navigation bar, choose **Platform O&M** > **Basic O&M Platform** > **O&M Tools**.
3. In the left-side navigation pane, choose **O&M Tools** > **Service Registration Variable Dashboard**.
4. On the **Registration Variable Dashboard** page, click **Advanced Filter**.
5. Enter a `ons_bizapi_endpoint` in the Service Registration field and click **Search**.
icon.
6. In the **Service Registration** column for the `mq-console` service, click the
7. Click the text information in the `mq-console` Service **Service Registration** column. In the **Register**
**Variable** dialog box, view the ons_bizapi_endpoint value, which is the `Endpoint` value.

**Obtain common parameters**

The parameters used to call Apsara Stack API operations by using POP Gateway, such as the organization ID, resource set ID, regionID, and instance ID. For more information about how to obtain the parameters, see Obtain common header parameters.

**1.1.1.3. Java Edition**

This topic describes how to use the advanced SDK to call API operations by using the POP gateway.

**Installation Instructions**

**Obtain the SDK package from the developer portal**

1. Log on to the Apsara Uni-manager Operations console.
2. In the top navigation bar, choose **Products** > **Development Tools** > **APIs and Tools** > **Developer**
**Portal**.
3. On the **Developer Portal** page, choose **API Integration** > **SDK Examples**.
4. Click the
button, choose **Middleware** > **MQ**, and set **Version** to **2018-02-05**.
5. Select **Advanced Edition** from the **SDK Type** drop-down list and select Java.
6. The following section shows the sample code. Click **Download Complete Project** to obtain the sample
project and SDK package.

**Import SDK packages**

1. Use one of the following methods to create a Maven project:
Method 1: Add a Maven project to IDEA. Method 2: Convert an existing project to a Maven project. i. Right-click the project you want to convert and select **Add Framework Support...**. ii. Select the **Maven** and click **OK****。**
2. Create a lib directory in the project root directory. Obtain the SDK package from the developer portal and
add it to the lib directory, as shown in the following figure.
3. Add Java SDK dependencies to the pom.xml file in the project directory.

```xml
<dependencies>
    <dependency>
        <groupId>com.aliyun.apsarastack</groupId>
        <artifactId>aliyun-java-sdk-ons</artifactId>
        <version>3.18.3-0</version>
        <scope>system</scope>
        <systemPath>${project.basedir}/lib/aliyun-java-sdk-ons-3.18.3-0.jar</systemPath>
    </dependency>
</dependencies>
```

4. View the Maven section on the right of IDEA.
As shown in the following figure, the dependency has been successfully imported.

**Code example**

The example shows how to call the `QueryInstanceList` API to `query the MQ instance list` .

```java
import com.aliyun.ons_inner20180205.Client; import com.aliyun.ons_inner20180205.models.QueryInstanceListRequest; import com.aliyun.ons_inner20180205.models.QueryInstanceListResponse; import com.aliyun.tea.TeaException; import com.aliyun.teaopenapi.models.Config; import com.aliyun.teautil.models.ExtendsParameters; importcom.aliyun.teautil.models.RuntimeOptions;
```

```java
potco.a yu.teaut .odes.ut eOptos; import java.util.HashMap; import java.util.Map; public class sample {
    public static void main(String[] args) throws Exception {
        // 1. Initialize the configuration object com.aliyun.teaopenapi.models.Config.
        Config config = new Config()
                // Specify the region ID.
                .setRegionId("<your-regionId>")
                // The AccessKey ID.
                .setAccessKeyId("<AccessKey ID>")
                // Your AccessKey secret.
                .setAccessKeySecret("<AccessKey Secret>")
                // You can use the Config parameter to set the proxy for requests during client
initialization. Replace the following example based on your business requirements.
                .setHttpProxy("http://127.0.0.1:9898");
        // The domain name that you want to access. For more information, see the API debugging page i
n Developer Portal.
        config.endpoint = "<your Endpoint>";
        // 2. Instantiate a client and generate an object client from the
com.aliyun.ons_inner20180205.Client class. The subsequent request and response are obtained from the com.aliyun.ons_inner20180205.models.
        Client client = new Client(config);
        // 3. run time parameter settings.
        RuntimeOptions runtime = new RuntimeOptions();
        Map<String, String> headers = new HashMap<>();
        // The ID of the organization.
        headers.put("x-acs-organizationid", "<your-organizationId>");
        // The ID of the resource group.
        headers.put("x-acs-resourcegroupid", "<your-resourcegroupId>");
        // The role ID.
        headers.put("x-acs-roleId", "<your-roleId>");
        runtime.setExtendsParameters(new ExtendsParameters().setHeaders(headers));
        // You can use the RuntimeOptions run time parameter to configure the proxy for the current re
quest. The priority of the proxy configuration is RuntimeOption> Client. Select a proxy type based on your business requirements.
        runtime.setHttpProxy("http://127.0.0.1:9898");
        runtime.ignoreSSL = true;
        runtime.setConnectTimeout(3000);
        runtime.setReadTimeout(30000);
        // 4. Set the request parameters of the request class and set the required information for the
properties of the class. For information that must be provided in the API, see the specific API docume ntation.
        QueryInstanceListRequest request = new QueryInstanceListRequest();
        // The value of this parameter is assumed. Enter the value based on your business
requirements.
        request.setNeedResourceInfo(true);
        // The value of this parameter is assumed. Enter the value based on your business needs.
        request.setOnsSessionId("your_value");
        // The value of this parameter is assumed. Enter the value based on your business needs.
        request.setOnsRegionId("your_value");
        // The value of this parameter is assumed. Enter the value based on your business needs.
        request.setPreventCache(System.currentTimeMillis());
        try{
            // 5. Obtain the response from the client object.
            QueryInstanceListResponse response = client.queryInstanceListWithOptions(request,
runtime);
            // 6. Call the corresponding property in the response to obtain the returned parameter
```

`//` `p` `g``p` `p` `y` `p` `p`

```java
value. Assume that you need to obtain the requestId :
            String requestId = response.body.getRequestId();
            // The returned result is an example only. Replace the returned result based on your
actual business situation.
            System.out.println(com.aliyun.teautil.Common.toJSONString(response));
        } catch (TeaException error) {
            // Use catch() to handle errors.
            // Only for print display here, please handle exceptions with caution, do not directly
ignore exceptions in the project.
            System.out.println(error.message);
        } catch (Exception _error) {
            // Use catch() to handle errors.
            TeaException error = new TeaException(_error.getMessage(), _error);
            // Only for print display here, please handle exceptions with caution, do not directly
ignore exceptions in the project.
            System.out.println(error.getMessage());
```

**Step introduction**

1. Initializes the configuration object com.aliyun.teaopenapi.models.Config. The Config object stores the
configurations such as the AccessKey ID, AccessKeySecret, and endpoint. For more information about how to obtain the configurations, see Obtain an AccessKey and Obtain API information and endpoints.

```
Config config = new Config() // Your AccessKey ID .setAccessKeyId(System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID")) // Your AccessKey secret. .setAccessKeySecret(System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET")); // The domain name that is accessed. config.endpoint = "************";
```

2. Instantiate a client and generate object client from com.aliyun.ons_inner20180205.Client class. The
subsequent request response is obtained from the com.aliyun.ons_inner20180205.models.

```
Client client = new Client(config);
```

3. Create a request for the corresponding API. The naming rule for a class is the API method name plus
Request. For example:

```
QueryInstanceListRequest request = new QueryInstanceListRequest();
```

4. Set parameters of the request class. Use the properties of the request class to set the necessary
information, that is, the information that must be provided in the API.

```
request.SourceRegionId = "your_value"; // The value of this parameter is assumed. request.RegionId = "your_value"; // The value of this parameter is assumed.
```

5. Use the client object to obtain the response of the corresponding request.

```java
QueryInstanceListResponse response = client.queryInstanceListWithOptions(request, runtime); System.out.println(new Gson().toJson(response.Body));
```

6. Call the corresponding property in the response to obtain the returned parameter value. Assume that you
need to obtain the requestId. Example:

```
String requestId = response.Body.requestId;
```

7. Use catch() to handle errors.

```
catch (Exception e) {
    e.printStackTrace();
```

#### Before you begin

**1.1.2.1. Obtain API information and the endpoint of an API**

**operation**

To call an API operation of a cloud service, you must familiarize yourself with the information about the operation, including the service code, operation name, and API version.

**Background information**

The API information on the debugging page in the Apsara Uni-manager Management Console is for reference only. For information about how to call API operations, see the developer guides of cloud services. If the information on the debugging page is different from that in the developer guide of a cloud service, the information in the developer guide shall prevail.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Development Tools** > **APIs and Tools** > **Developer**
**Portal**.
3. On the **Developer Portal** page, choose **API Integration** > **API Debugging**.
4. In the left-side navigation pane, select the target cloud service.
5. Select an API version from the **Version** drop-down list.
6. In the API list below, you can view all APIs of the current version.
7. Select the operation that you want to view and obtain the POP endpoint of the cloud service.

**1.1.2.2. Obtain AccessKey credentials**

Access credentials are assigned by Resource Access Management (RAM) or Security Token Service (STS). You can use either type of access credential for authentication when you make an API request. This topic describes how to obtain access credentials that are assigned by RAM.

**Background information**

An AccessKey pair is used to verify the identity of a request sender based on symmetric encryption. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. AccessKey credentials can be assigned by RAM or STS: Use RAM to assign an AccessKey ID and an AccessKey secret to a third party. Use STS to assign an AccessKey ID, an AccessKey secret, and a security token to a third party. For more information, see Obtain an access credential assigned by STS. The Apsara Uni-manager Management Console provides AccessKey pairs to personal accounts and organizations. Only the administrators of level-1 organizations and operations administrators can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the API operations of the Apsara Uni-manager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the header parameters that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions may occur.

**Warning**

The AccessKey pair of a personal account is managed by the permission system of the Apsara Unimanager Management Console and has limited permissions. The AccessKey pair of an organization has greater permissions. If you want to use such an AccessKey pair, make sure that your operation is allowed by an administrator to ensure security.

| Header | Description |
|---|---|
| x-acs-regionid | The region ID. Example: cn-hangzhou-*. |
| x-acs-organizationid | The organization ID in the Apsara Uni-manager Management Console. For more information about how to obtain an organization ID, see GetOrganizationList in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-resourcegroupid | The resource set ID in the Apsara Uni-manager Management Console. For more information about how to obtain a resource set ID, see ListResourceGroup in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance that you want to manage. For example, you can use the ID of an Elastic Compute Service (ECS) instance obtained from the ECS instance list. |

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log in to the Apsara Uni-manager Management Console.
2. Click the profile picture in the upper-right corner of the page and click **User Information**.
3. In the **AccessKey Pair** section, view the AccessKey pair of the personal account.

**Note**

An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey pair provides full permissions on cloud resources within your account. You must keep the AccessKey pair confidential.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you want to obtain.
5. On the right side of the page, click **Manage AccessKey Pairs**.
6. In the dialog box that appears, view the AccessKey pair of the organization.

**1.1.2.3. Obtain the values of common request headers**

You must provide multiple header parameters when you call API operations in Apsara Stack. This topic describes how to obtain the values of common header parameters. This topic also explains the response parameters that are returned after you call API operations.

**Obtain a region ID**

1. Log in to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources** > **Regions**.
4. On the Regions page, find the organization that you want to view and click its name in the organization
tree.
5. In the **Regions** list, obtain the region ID from the **Region Name** column.

**Obtain an organization ID**

You must call a specific API operation to obtain the organization ID. You can obtain the organization ID by using the online debugging feature in the Apsara Uni-manager Management Console.
1. Log in to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, choose **Products** > **Development Tools** > **API & SDK** > **OpenAPI Explorer**.
3. In the top navigation bar of the **OpenAPI Explorer** page, choose **API Integration** > **API Debugging**.
4. Move the pointer over the
icon and choose **Platform** > **Apsara Uni-manager**. Select **2019-05-10** from the **Version** drop-down list.
5. Search for the `GetOrganizationList` operation and debug the operation online. Set the name parameter
to the name of the organization that you want to query and click Initiate Call. Obtain the organization ID from the **id** parameter on the **Call Result** tab. For more information about this operation, see the GetOrga nizationList section of Apsara Uni-manager Operations Console Developer Guide.

**Obtain a resource set ID**

You must call a specific API operation to obtain the resource set ID. You can obtain the resource set ID by using the online debugging feature in the Apsara Uni-manager Management Console.
1. Log in to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, choose **Products** > **Development Tools** > **API & SDK** > **OpenAPI Explorer**.
3. In the top navigation bar of the **OpenAPI Explorer** page, choose **API Integration** > **API Debugging**.
4. Move the pointer over the
icon and choose **Platform** > **Apsara Uni-manager**. Select **2019-05-10** from the **Version** drop-down list.
5. Search for the `ListResourceGroup` operation and debug the operation online. Obtain the resource set ID
from the **id** parameter on the **Call Result** tab. For more information about this operation, see the ListReso urceGroup section of Apsara Uni-manager Operations Console Developer Guide.

**Obtain an instance ID**

You can obtain the ID of an instance in the cloud service console of the Apsara Uni-manager Management Console. For example, to obtain the ID of an API gateway, perform the following steps:
1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Middleware** > **MSMQ** > **MSMQ RocketMQ Edition**.
3. In the left-side navigation pane, click **Instances**.
4. View the **Instance ID** in the instance list.

**Response parameters**

If you call the API operation of a list instance, the following value is added by default.

| Parameter | Description |
|---|---|
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The resource set ID. |
| DepartmentName | The name of the organization. |
| Department | The organization ID. |

**1.1.2.4. Obtain an STS AccessKey pair**

This topic describes how to use Security Token Service (STS) to call Apsara Stack API operations.

**Background information**

STS allows you to manage temporary access credentials for your Apsara Stack resources. You can use STS to call API operations.

**Procedure**

1. Obtain the Apsara Stack Resource Name (ARN) of your Resource Access Management (RAM) role.
i. Log in to the Apsara Uni-manager Management Console. ii. In the upper-right corner of the homepage, click the profile picture, and then click **User Information**. iii. On the page that appears, click **View Current Role Policy**.

| RAM role . |   |
|---|---|
| secret ( | stsSK |

In the **View Policies of Current Role** dialog box, view the ARN of your `RAM role` .
2. Use the following code to obtain an AccessKey ID ( `stsAK` ), an AccessKey secret ( `stsSK` ), and an STS
token ( `stsToken` ) by assuming the `RAM role` .

```
public static void main(String[] args) {
     ASClient asClient = new ASClient();
     // Specify the description of the call source.
        asClient.setSdkSource("test");
     // Specify the ARN.
        String assumeRole = AssumeRole(asClient, "<RAM Role>");
        JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
        JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
        // Obtain the access credentials assigned by STS.
        String stsAK = credentials.getString("AccessKeyId");
        String stsSK = credentials.getString("AccessKeySecret");
        String stsToken = credentials.getString("SecurityToken");
public static String AssumeRole(ASClient asClient, String roleArn) {
        Map<String, String> headers = new HashMap<>();
        Map<String, Object> reqParams = new HashMap<>();
        reqParams.put("action", "AssumeRole");
        reqParams.put("Product", "Sts");
        reqParams.put("Version", "2015-04-01");
        reqParams.put("regionId", regionId);
     // The AccessKey ID of the current user.
        reqParams.put("AccessKeyId", <The AccessKey ID of the current user>);
     // The AccessKey secret of the current user.
        reqParams.put("AccessKeySecret", <The AccessKey secret of the current user>);
        reqParams.put("roleSessionName", "StsUser");
        reqParams.put("roleArn", roleArn);
        return asClient.doRequest(endpoint, headers, reqParams);
```

3. You can use STS to call the APIs of cloud products. Example:

```java
import com.aliyun.credentials.Client; import com.aliyun.credentials.models.Config; // The following example shows how to use an STS token to initialize a credential client (the proced ure for obtaining an STS token is not included). public class DemoStsTest {
    public static void main(String[] args) {
        Config credentialConfig = new Config();
        credentialConfig.setType("sts");
        // Replace it with the AccessKeyI in the STS triplet obtained in the previous step.
        credentialConfig.setAccessKeyId("your_AccessKeyId");
        // Replace it with the AccessKeySecret in the STS triplet obtained in the previous step.
        credentialConfig.setAccessKeySecret("your__AccessKeySecret");
        // Replace it with the SecurityToken in the STS triplet obtained in the previous step.
        credentialConfig.setSecurityToken("your__SecurityToken");
        Client credentialClient = new Client(credentialConfig);
        // Continue to call the API. For more information, see the API documentation.
```

### References

#### Agent

**1.2.1.1. Agent**

**1.2.1.1.1. PostAgentOpenapiAgentVersionPagequery**

Query the version list of intelligences

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| current | Integer | Body | Yes | 1 | The current number of pages. This parameter is required. |

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| pageSize | Integer | Body | Yes | 10 | The number of pieces per page. This parameter is required. |
| agentCode | String | Body | Yes | 905a3aaa-5797-47fb-ac71- b8dcd88b9ac0 | The agent encoding. This parameter is required. |
| versionNam e | String | Body | Yes | 1.0 | Fuzzy search for the version name. This parameter is required. |

**Response parameters**

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |
| data | Object | Return data | {} |
| total | Integer | The total number of intelligent body versions queried. | 1 |
| list | List | The list of intelligent body versions queried. |   |
| agentCode | String | agent unique encoding | a9c81580-8e93-42e1- b331-5cc6506c0093 |
| agentName | String | Agent Name | DB with table recall |
| agentDefinition | String | agent description | DB with table recall |
| versionName | String | Version Name | knowledge base check |
| agentVersion | String | Version encoding | 1757388497303 |
| agentStatus | String | The status of the version. DEV=In Design, ONLINE=Online, OFFLINE=Offline | DEV |
| gmtCreate | String | Creation time | 2025-08- 29T11:43:54.722+00:00 |
| gmtModified | String | Modification time | 2025-08- 29T11:43:54.722+00:00 |
| pageSize | Integer | Size per page | 60 |
| current | Integer | Current Page | 1 |
| errorCode | String | The error code. | true |
| errorMsg | String | The error message. | true |

```
 JSON format
```

```json
  "errorMessages": [],
  "success": true,
  "data": {
    "extInfos": {},
    "total": 1,
    "list": [
        "id": 759,
        "gmtCreate": "2025-11-11T12:19:54.315+00:00",
        "gmtModified": "2025-11-11T12:19:54.315+00:00",
        "tenant": "fmthktsjdb",
        "agentCode": "9456fd9d-1a55-43b0-b383-f1331e81e69d",
        "agentName": "testAgent",
        "agentVersion": "1762863594309",
        "versionName": "Version 1",
        "agentDefinition": "testUpdate",
        "developer": {
          "id": null,
          "gmtCreate": null,
          "gmtModified": null,
          "tenant": null,
          "uniqueCode": "7b7d340c8ec04c9db0c8c072e3d5e690",
          "source": null,
          "outerId": null,
          "name": "Daily administrator"
```

`},`

```json
        "pd": {
          "id": null,
          "gmtCreate": null,
          "gmtModified": null,
          "tenant": null,
          "uniqueCode": "7b7d340c8ec04c9db0c8c072e3d5e690",
          "source": null,
          "outerId": null,
          "name": "Daily administrator"
```

`},`

```json
        "agentStatus": "DEV",
        "engineConfig": {
          "engineName": "processAgentEngine",
          "considerServiceName": "DefaultConsiderService",
          "protocolParserName": null,
          "supportTaskBuilderName": null,
          "maxCountsOfConsider": null,
          "maxResponseWaitMs": null,
          "enginePolicy": "ReAct",
          "flowType": null
```

`},`

```json
        "modelConfig": null,
        "scriptConfig": {
          "engineName": null,
          "script": null
```

`},`

```json
        "availableToolsConfig": null,
        "createType": null,
        "method": null,
        "configMethod": null,
        "icon": null,
        "jumpUrl": null,
        "flowType": "workflow",
        "templateType": null,
        "canDeployTemplate": false
```

`],`

```json
    "pageSize": 10,
    "current": 1,
    "totalPages": 1
```

`},`

```json
  "errorCode": null,
  "errorMsg": null,
  "extraData": null,
  "traceId": null,
  "env": null,
  "other": null,
  "firstErrorMessage": null,
  "failure": false
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.1.1.2. PostAgentOpenapiMemoryLongtermPartitionAdd**

Write memory partition contents

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| partitionCod e | String | Body | Yes | 1111 | Partition encoding. This parameter is required. |
| storageKey | String | Body | Yes | key | Key-value pair-KEY. This parameter is required. |
| storageValu e | String | Body | Yes | value | Key-value pair-VALUE. This parameter is required. |
| storageCont ent | String | Body | Yes | example | The text. This parameter is required. |
| memoryUser Id | String | Body | Yes | 1234 | Memory user ID. This parameter is required. |
| status | Integer | Body | Yes | 0 | Status 0: Normal 1: Deleted 2: Disabled. This parameter is required. |

**Response parameters**

| Field | Data types | Description | Examples |
|---|---|---|---|
| success | Boolean | Success | true |
| data | Object | Return data | {} |
| memoryCode | String | Memory Encoding | a9c81580-8e93-42e1- b331-5cc6506c0093 |
| errorCode | String | The error code. | true |
| errorMsg | String | The error message. | true |

```
 JSON format
```

```json
  "errorMessages": [],
  "success": false,
  "data": null,
  "errorCode": "-1",
  "errorMsg": "The memory partition does not exist",
  "extraData": null,
  "traceId": null,
  "env": null,
  "other": null,
  "firstErrorMessage": null,
  "failure": false
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.1.1.3. PostAgentOpenapiAgentCreate**

Create intelligences

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| agentName | String | Body | Yes | DB with table recall | The name of the agent. This parameter is required. |
| agentDesc | String | Body | Yes | DB with table recall | The description of the agent. This parameter is required. |

**Response parameters**

| Field | Data types | Description |
|---|---|---|
| success | Boolean | Success |
| data | Object | Return data |
| agentCode | String | agent unique encoding |
| agentName | String | Agent Name |
| agentDesc | String | agent description |
| workspaceCode | String | Workspace encoding |
| gmtCreate | String | The creation time. |
| gmtModified | String | The modification time. |
| errorCode | String | The error code. |
| errorMsg | String | Error description |

`JSON` format

```json
  "errorMessages": [],
  "success": true,
  "data": {
    "id": 189,
    "gmtCreate": "2025-11-11T12:00:00.308+00:00",
    "gmtModified": "2025-11-11T12:00:00.308+00:00",
    "tenant": "fmthktsjdb",
    "agentCode": "9456fd9d-1a55-43b0-b383-f1331e81e69d",
    "agentName": "testAgent",
    "agentDesc": "test",
    "icon": null,
    "label": null,
    "developer": {
      "id": null,
      "gmtCreate": null,
      "gmtModified": null,
      "tenant": null,
      "uniqueCode": "7b7d340c8ec04c9db0c8c072e3d5e690",
      "source": null,
      "outerId": null,
      "name": "daily_root"
```

`},`

```json
    "pd": {
      "id": null,
      "gmtCreate": null,
      "gmtModified": null,
      "tenant": null,
      "uniqueCode": "7b7d340c8ec04c9db0c8c072e3d5e690",
      "source": null,
      "outerId": null,
      "name": "daily_root"
```

`},`

```json
    "outputVersions": null,
    "workspaceCode": "fmthktsjdb",
    "agentApiLimitConfig": null
```

`},`

```json
  "errorCode": null,
  "errorMsg": null,
  "extraData": null,
  "traceId": null,
  "env": null,
  "other": null,
  "firstErrorMessage": null,
  "failure": false
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |

| l | OpenTrek Dev Developer Guide·P atform Function Class |   | OpenTre | k |
|---|---|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.1.1.4. PostAgentOpenapiAgentVersionCreate**

Create an agent version

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| agentCode | String | Body | Yes | 905a3aaa-5797-47fb-ac71- b8dcd88b9ac0 | The agent encoding. This parameter is required. |

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| versionNam e | String | Body | Yes | Version 1 | The description of the version. This parameter is required. |
| flowType | String | Body | Yes | workflow | The creation mode. workflow=workflow. default=template-based. This parameter is required. |
| templateCod e | String | Body | Yes | 3b7628cc51544996908b6ea 55ae07bc1 | The encoding of the template. This is required when the creation mode is template-based. |

**Response parameters**

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |
| data | Object | Return data | {} |
| agentCode | String | agent unique encoding | a9c81580-8e93-42e1- b331-5cc6506c0093 |
| agentName | String | Agent Name | DB with table recall |
| agentVersion | String | Agent version | 1759062292925 |
| versionName | String | Version Description | Version 1 |
| agentDesc | String | agent description | DB with table recall |
| workspaceCode | String | Workspace encoding | baseline |
| gmtCreate | String | Creation time | 2025-08- 29T11:43:54.722+00:00 |
| gmtModified | String | Modification time | 2025-08- 29T11:43:54.722+00:00 |
| errorCode | String | Error code | true |
| errorMsg | String | The error message. | true |

```
 JSON format
```

```json
  "errorMessages": [],
  "success": true,
  "data": true,
  "errorCode": null,
  "errorMsg": null,
  "extraData": null,
  "traceId": null,
  "env": null,
  "other": null,
  "firstErrorMessage": null,
  "failure": false
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.1.1.5. PostAgentOpenapiAgentDelete**

Delete intelligences

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| agentCode | String | Body | Yes | a9c81580-8e93-42e1-b331- 5cc6506c0093 | The only encoding of the agent. This parameter is required. |

**Response parameters**

| Field | Data types | Description | Examples |
|---|---|---|---|
| success | Boolean | Success | true |
| errorCode | String | The error code. | true |
| errorMsg | String | The error message. | true |

```json
 JSON format
  "errorMessages": [],
  "success": true,
  "data": true,
  "errorCode": null,
  "errorMsg": null,
  "extraData": null,
  "traceId": null,
  "env": null,
  "other": null,
  "firstErrorMessage": null,
  "failure": false
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |

| OpenTrek Dev Developer Guide·P atform Function Class |   | OpenTre |
|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.1.1.6. PostAgentOpenapiAgentUpdate**

Edit Intelligences

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| agentCode | String | Body | Yes | a9c81580-8e93-42e1-b331- 5cc6506c0093 | The only encoding of the agent. This parameter is required. |
| agentName | String | Body | Yes | DB with table recall | The name of the agent. This parameter is required. |
| agentDesc | String | Body | Yes | DB with table recall | The description of the agent. This parameter is required. |

**Response parameters**

| Field | Data types | Description | Examples |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |
| data | Boolean | Indicates whether the request was successful. | true |
| errorCode | String | The error code. | true |
| errorMsg | String | The error message. | true |

```json
 JSON format
  "errorMessages": [],
  "success": true,
  "data": true,
  "errorCode": null,
  "errorMsg": null,
  "extraData": null,
  "traceId": null,
  "env": null,
  "other": null,
  "firstErrorMessage": null,
  "failure": false
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |

| OpenTrek Dev Developer Guide·P |   |   |
|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.1.1.7. PostAgentOpenapiAgentVersionUpdate**

Edit agent version

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| agentCode | String | Body | Yes | a9c81580-8e93-42e1-b331- 5cc6506c0093 | The only encoding of the agent. This parameter is required. |

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| agentVersio n | String | Body | Yes | 1759062292925 | The version of the agent. This parameter is required. |
| versionNam e | String | Body | Yes | Version 1 | The name of the version. This parameter is required. |

**Response parameters**

| Field | Data types | Description | Examples |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |
| data | Boolean | Indicates whether the request was successful. | true |
| errorCode | String | The error code. | true |
| errorMsg | String | The error message. | true |

```json
 JSON format
  "errorMessages": [],
  "success": true,
  "data": true,
  "errorCode": null,
  "errorMsg": null,
  "extraData": null,
  "traceId": null,
  "env": null,
  "other": null,
  "firstErrorMessage": null,
  "failure": false
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |

| atform Function Class |   |   |
|---|---|---|
| HTTP status return code | Error description | Error interpretation |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.1.1.8. PostAgentOpenapiAgentVersionDelete**

Delete an agent version

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| agentCode | String | Body | Yes | a9c81580-8e93-42e1-b331- 5cc6506c0093 | The only encoding of the agent. This parameter is required. |
| agentVersio n | String | Body | Yes | 1759062292925 | The version of the agent. This parameter is required. |

**Response parameters**

| Field | Data types | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |
| errorCode | String | The error code. | true |
| errorMsg | String | The error message. | true |

```json
 JSON format
  "errorMessages": [],
  "success": true,
  "data": true,
  "errorCode": null,
  "errorMsg": null,
  "extraData": null,
  "traceId": null,
  "env": null,
  "other": null,
  "firstErrorMessage": null,
  "failure": false
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |

| OpenTrek Dev Developer Guide·P |   | OpenTre |
|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.1.1.9. PostAgentOpenapiAgentPagequery**

Query the intelligences list

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| current | Integer | Body | Yes | 1 | The current number of pages. This parameter is required. |
| pageSize | Integer | Body | Yes | 10 | The number of pieces per page. This parameter is required. |
| agentName | String | Body | Yes | agent | Intelligent body name fuzzy search, this parameter is required. |

**Response parameters**

| Field | Data types | Description | Examples |
|---|---|---|---|
| success | Boolean | Success | true |
| data | Object | Return data | {} |
| total | Integer | Total number of intelligences queried | 1 |

| Field | Data types | Description | Examples |
|---|---|---|---|
| list | List | The list of intelligences queried. |   |
| agentCode | String | agent unique encoding | a9c81580-8e93-42e1- b331-5cc6506c0093 |
| agentName | String | Agent Name | DB with table recall |
| agentDesc | String | agent description | DB with table recall |
| workspaceCode | String | Workspace encoding | baseline |
| gmtCreate | String | Creation time | 2025-08- 29T11:43:54.722+00:00 |
| gmtModified | String | Modification time | 2025-08- 29T11:43:54.722+00:00 |
| pageSize | Integer | Size per page | 60 |
| current | Integer | Current Page | 1 |
| errorCode | String | The error code. | true |
| errorMsg | String | The error message. | true |

```
 JSON format
```

```json
  "errorMessages": [],
  "success": true,
  "data": {
    "extInfos": {},
    "total": 1,
    "list": [
        "id": 188,
        "gmtCreate": "2025-10-23T01:46:02.907+00:00",
        "gmtModified": "2025-10-23T01:46:02.907+00:00",
        "tenant": "fmthktsjdb",
        "agentCode": "52a38b92-88da-48cf-8317-2d22d71beb5c",
        "agentName": "chengmutest",
        "agentDesc": "111",
        "icon": "AGENT_ICON_6",
        "label": null,
        "developer": {
          "id": null,
          "gmtCreate": null,
          "gmtModified": null,
          "tenant": null,
          "uniqueCode": "33ad2daf266d454a9cd1a9469a75c53d",
          "source": null,
          "outerId": null,
          "name": "test"
```

`},`

```json
        "pd": {
          "id": null,
          "gmtCreate": null,
          "gmtModified": null,
          "tenant": null,
          "uniqueCode": "33ad2daf266d454a9cd1a9469a75c53d",
          "source": null,
          "outerId": null,
          "name": "test"
```

`},`

```json
        "outputVersions": null,
        "workspaceCode": "fmthktsjdb",
        "agentApiLimitConfig": null
```

`],`

```json
    "pageSize": 10,
    "current": 1,
    "totalPages": 1
```

`},`

```json
  "errorCode": null,
  "errorMsg": null,
  "extraData": null,
  "traceId": null,
  "env": null,
  "other": null,
  "firstErrorMessage": null,
  "failure": false
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.1.2. tools-for-agents**

**1.2.1.2.1. PostAgentOpenapiToolUpdate**

Editing tools

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| name | String | Body | No | Test tool | Tool |
| desc | String | Body | No | Test tool | The tool description. |
| serviceConfi g | Json | Body | No | {} | Tool configuration |
| toolType | String | Body | No | api | The type of the tool. |

**Response parameters**

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |
| data | Object | Return data | {} |
| code | String | Tool coding | a9c81580-8e93-42e1- b331-5cc6506c0093 |
| name | String | Tool name | Test tool |
| desc | String | Tool Description | Test tool |
| version | String | Tool Version | 1759118429269 |
| serviceConfig | Object | Tool configuration | {} |
| workspaceCode | String | Workspace encoding | baseline |
| gmtCreate | String | Creation time | 2025-08- 29T11:43:54.722+00:00 |
| gmtModified | String | Modification time | 2025-08- 29T11:43:54.722+00:00 |
| errorCode | String | Error code | true |
| errorMsg | String | The error message. | true |

```
 JSON format
```

```json
  "errorMessages": [],
  "success": true,
  "data": null,
  "errorCode": null,
  "errorMsg": null,
  "extraData": null,
  "traceId": null,
  "env": null,
  "other": null,
  "firstErrorMessage": null,
  "failure": false
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.1.2.2. PostAgentOpenapiToolPagequery**

Query tool list

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| current | Integer | Body | Yes | 1 | The current number of pages. This parameter is required. |
| pageSize | Integer | Body | Yes | 10 | The number of pieces per page. This parameter is required. |
| toolCategory | String | Body | Yes | my | Category, my=My tool, platform=Platform tool. This parameter is required. |
| toolType | String | Body | Yes | my | The type of the tool. This parameter is required. The value of this parameter is API. The value of this parameter is MY MCP=mcp. _ The value of this parameter is knowledge base. |

**Response parameters**

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |
| data | Object | Return data | {} |
| total | Integer | Total number of intelligences queried | 1 |
| list | List | The list of intelligences queried. |   |

| 48 |   | > Doc | ument Version: 20260901 |
|---|---|---|---|

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| code | String | Tool coding | 10110baseline |
| name | String | Tool name | doc-parse |
| desc | String | Tool Description | Built-in document parsing tools |
| workspaceCode | String | Workspace encoding | baseline |
| gmtCreate | String | Creation time | 2025-08- 29T11:43:54.722+00:00 |
| gmtModified | String | Modification time | 2025-08- 29T11:43:54.722+00:00 |
| toolType | String | Tool Type | MCP |
| toolSubType | String | Tool Subtype | doc-parse |
| serviceConfig | Object | Tool configuration |   |
| pageSize | Integer | The number of entries returned per page. | 60 |
| current | Integer | Current Page | 1 |
| errorCode | String | The error code. | true |
| errorMsg | String | The error message. | true |

`JSON` format

```json
  "errorMessages": [],
  "success": true,
  "data": {
    "marketCode": "system",
    "marketName": "Custom templates",
    "itemCode": "3b7628cc51544996808b6ea55ae07bc1",
    "itemName": "AutoBot dialog assistant",
    "itemLabels": [
      "System Built-in"
```

`],`

```json
    "itemType": "agentTemplate",
    "targetCode": "851d5b0b-8393-497c-b909-1d3209efee74",
    "targetName": "v1.0",
    "targetVersion": "1731573095677",
    "status": "online",
    "statusDesc": "The service has been installed.",
    "operatorId": null,
    "operatorName": null,
    "showDetail": {
      "skills": [
        "Support access to users' existing business APIs",
        "Supports the OneRag plug-in to link user business data",
        "Support for accessing other agent instances"
```

`],`

```json
      "usage": {
        "attachment": {},
        "configDesc": "None",
        "limitDesc": "None"
```

`},`

```json
      "description": "Comprehensive Q&A capabilities",
      "interfaceInfo": {
        "inputParams": [
            "example": "bd962db7-b1c8-4466-a2cc-41b9b67cd94b return value of the session creation inter
face uniqueCode",
            "label": "sessionId",
            "name": "sessionId",
            "necessary": true,
            "type": "STRING"
```

`},`

```json
            "example": "true",
            "label": "Whether to stream",
            "name": "stream",
            "necessary": true,
            "type": "BOOL"
```

`},`

```json
            "example": "true By default, new content is output each time, excluding the text that is ou
tput in the preceding sequence",
            "label": "When stream=true, controls whether new text is not added",
            "name": "delta",
            "necessary": true,
            "type": "BOOL"
```

`},`

```json
            "example": "false does not return trace records by default",
            "label": "When trace=true, controls whether trace records are returned",
            "name": "trace",
            "necessary": false,
            "type": "BOOL"
```

`},`

```json
            "children": [
                "example": "Book me a flight from Shanghai to Zurich tomorrow",
                "label": "Conversation input",
                "name": "text",
                "necessary": true,
                "type": "STRING"
```

`},`

```json
                "example": "{}",
                "label": "Extended information",
                "name": "metadata",
                "necessary": false,
                "type": "OBJECT"
```

`},`

```json
                "children": [
                    "example": "{}",
                    "label": "Attachment address",
                    "name": "url",
                    "necessary": true,
                    "type": "STRING"
```

`},`

```json
                    "example": "{}",
                    "label": "Attachment name",
                    "name": "name",
                    "necessary": false,
```

```json
                    "type": "STRING"
```

`],`

```json
                "example": "[]",
                "label": "Attachment information",
                "name": "attachments",
                "necessary": false,
                "type": "LIST<Object>"
```

`],`

```json
            "example": "{\"text\":\" Book me a ticket from Shanghai to Zurich tomorrow \",
\"metadata\":{}, \"attachments\":[{\"url\":\"\", \"name\":\"\"}]}",
            "label": "Request message body",
            "name": "message",
            "necessary": true,
            "type": "OBJECT"
```

`],`

```json
        "interfaceDesc": "None",
        "outputParams": [
            "example": "message.de lta output text block think.de lta thought process block error error
message",
            "label": "Data type",
            "name": "object",
            "necessary": true,
            "type": "STRING"
```

`},`

```json
            "example": "assistant",
            "label": "Role",
            "name": "role",
            "necessary": true,
            "type": "STRING"
```

`},`

```json
            "example": "object=message.delta scenario: {\"type\": \"text\",\"text\":{\"value\": \" Incr
emental response content \"}} Scenario object=thought.delta: {\"type\": \"text\",\"data\": \" Think co ntent increment \"} object=error scenario {\"errorMsg\": \" Error message content \"} ",
            "label": "Data content",
            "name": "content",
            "necessary": true,
            "type": "OBJECT"
```

`},`

```json
            "example": "{\"key\":\"value\"}",
            "label": "Extended field",
            "name": "metadata",
            "necessary": false,
            "type": "OBJECT"
```

`},`

```json
            "example": "false|true",
            "label": "Specifies whether to end the output of marker text in streaming
(object=message.delta) scenarios",
            "name": "end",
            "necessary": true,
            "type": "BOOL"
```

`},`

```json
            "example": "-",
            "label": "Current session ID",
            "name": "sessionId",
```

```json
            "necessary": true,
            "type": "STRING"
```

`},`

```json
            "example": "-",
            "label": "The ID of the currently running request",
            "name": "requestId",
            "necessary": true,
            "type": "STRING"
```

`},`

```json
            "example": "true",
            "label": "Non-streaming-Whether the service is successful",
            "name": "success",
            "necessary": true,
            "type": "BOOL"
```

`},`

```json
            "children": [
                "children": [
                    "example": "assistant",
                    "label": "Role",
                    "name": "role",
                    "necessary": true,
                    "type": "STRING"
```

`},`

```json
                    "example": "{\"key\":\"value\"}",
                    "label": "Extended field",
                    "name": "metadata",
                    "necessary": false,
                    "type": "OBJECT"
```

`},`

```json
                    "children": [
                        "example": "text|image",
                        "label": "Output content type",
                        "name": "type",
                        "necessary": true,
                        "type": "STRING"
```

`},`

```json
                        "children": [
                            "example": "Hello! Is there anything I can help you with?",
                            "label": "Output text",
                            "name": "value",
                            "necessary": true,
                            "type": "STRING"
```

`],`

```json
                        "example": "{}",
                        "label": "type=text output structure",
                        "name": "text",
                        "necessary": true,
                        "type": "OBJECT"
```

`},`

```json
                        "children": [
```

```json
                            "example": "",
                            "label": "The address of the output image",
                            "name": "url",
                            "necessary": true,
                            "type": "STRING"
```

`],`

```json
                        "example": "{}",
                        "label": "type=output structure of the image scenario",
                        "name": "image",
                        "necessary": true,
                        "type": "OBJECT"
```

`],`

```json
                    "example": "",
                    "label": "Output content",
                    "name": "content",
                    "necessary": true,
                    "type": "LIST<Object>"
```

`],`

```json
                "example": "{}",
                "label": "Non-streaming-output text response",
                "name": "message",
                "necessary": false,
                "type": "OBJECT"
```

`},`

```json
                "children": [
                    "example": "assistant",
                    "label": "Role",
                    "name": "role",
                    "necessary": true,
                    "type": "STRING"
```

`},`

```json
                    "children": [
                        "example": "",
                        "label": "Output text",
                        "name": "data",
                        "necessary": true,
                        "type": "STRING"
```

`},`

```json
                        "example": "text",
                        "label": "The output content type. Currently, it is the constant text",
                        "name": "type",
                        "necessary": true,
                        "type": "STRING"
```

`],`

```json
                    "example": "",
                    "label": "Output content",
                    "name": "content",
                    "necessary": true,
                    "type": "OBJECT"
```

`],`

```json
                "example": "{}",
                "label": "Non-streaming-output thought response",
                "name": "thoughts",
```

```json
                "necessary": false,
                "type": "OBJECT"
```

`],`

```json
            "example": "{}",
            "label": "Non-streaming-business response",
            "name": "data",
            "necessary": false,
            "type": "OBJECT"
```

`},`

```json
            "example": "true",
            "label": "Non-streaming-business error code",
            "name": "errorCode",
            "necessary": false,
            "type": "BOOL"
```

`},`

```json
            "example": "true",
            "label": "Non-streaming-business error description",
            "name": "errorMsg",
            "necessary": false,
            "type": "BOOL"
```

`]` `},`

```json
      "type": "platform"
```

`},`

```json
    "config": null,
    "feature": {
      "templateType": "AutoBot"
```

`},`

```json
    "operateControl": null
```

`},`

```json
  "errorCode": null,
  "errorMsg": null,
  "extraData": null,
  "traceId": null,
  "env": null,
  "other": null,
  "firstErrorMessage": null,
  "failure": false
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |

|   | OpenTrek |   | OpenTrek Dev Developer Guide· latform Function Clas | P s |
|---|---|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.1.2.3. PostAgentOpenapiToolCreate**

Create a tool

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| name | String | Body | Yes | Test tools | The name of the tool. This parameter is required. |
| desc | String | Body | Yes | Test tool | The description of the tool. This parameter is required. |
| serviceConfi g | Json | Body | Yes | {} | The tool configuration. This parameter is required. |

| OpenTrek Dev atform Functi | Develop on Class | er Guide·P |   |   | OpenTre |
|---|---|---|---|---|---|

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| toolType | String | Body | Yes | api | The type of the tool. This parameter is required. |

**Response parameters**

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |
| data | Object | Return data | {} |
| code | String | Tool coding | a9c81580-8e93-42e1- b331-5cc6506c0093 |
| name | String | Tool name | Test tool |
| desc | String | Tool Description | Test tool |
| version | String | Tool Version | 1759118429269 |
| serviceConfig | Object | Tool configuration | {} |
| workspaceCode | String | Workspace encoding | baseline |
| gmtCreate | String | Creation time | 2025-08- 29T11:43:54.722+00:00 |
| gmtModified | String | Modification time | 2025-08- 29T11:43:54.722+00:00 |
| errorCode | String | Error code | true |
| errorMsg | String | Error description | true |

`JSON` format

```json
  "errorMessages": [],
  "success": true,
  "data": {
    "id": 143,
    "gmtCreate": "2025-11-11T13:24:14.501+00:00",
    "gmtModified": "2025-11-11T13:24:14.501+00:00",
    "tenant": "fmthktsjdb",
    "code": "3e8f4bea-298d-40c7-9c41-7adfd4e37940",
    "workspaceCode": "fmthktsjdb",
    "name": "jieyan",
    "version": "1762867454501",
    "desc": "jieyan",
    "toolType": "api",
    "toolSubType": null,
    "owner": {
      "id": null,
      "gmtCreate": null,
      "gmtModified": null,
      "tenant": null,
      "uniqueCode": "7b7d340c8ec04c9db0c8c072e3d5e690",
      "source": null,
      "outerId": null,
      "name": "daily_root"
```

`},`

```json
    "serviceConfig": {
      "executorName": null,
      "result2PromptName": null,
      "serviceInvocationConfig": null,
      "toolCommonConfig": null,
      "llmConfig": null,
      "toolApiConfig": null,
      "toolScriptConfig": null,
      "searchChunkConfig": null,
      "toolUseDetail": null,
      "mcpConfig": null
```

`},`

```json
    "shareWorkspaces": null,
    "allFlag": null
```

`},`

```json
  "errorCode": null,
  "errorMsg": null,
  "extraData": null,
  "traceId": null,
  "env": null,
  "other": null,
  "firstErrorMessage": null,
  "failure": false
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |

| OpenTrek Dev Developer Guide·P atform Function Class |   | OpenTre |
|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.1.2.4. PostAgentOpenapiToolGetone**

Query tool details

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| uniqueCode | String | Body | Yes | a9c81580-8e93-42e1-b331- 5cc6506c0093 | The encoding of the tool. This parameter is required. |

| OpenTrek |   |   |   | OpenT | rek Dev Developer Guide· latform Function Clas |
|---|---|---|---|---|---|

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| version | String | Body | Yes | 1759118429269 | The version of the tool. This parameter is required. |

**Response parameters**

| Field | Data types | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |
| data | Object | Response parameters | {} |
| code | String | Tool coding | a9c81580-8e93-42e1- b331-5cc6506c0093 |
| name | String | Tool name | Test tool |
| desc | String | Tool Description | Test tool |
| version | String | Tool Version | 1759118429269 |
| serviceConfig | Object | Tool configuration | {} |
| workspaceCode | String | Workspace encoding | baseline |
| gmtCreate | String | Creation time | 2025-08- 29T11:43:54.722+00:00 |
| gmtModified | String | Modification time | 2025-08- 29T11:43:54.722+00:00 |
| errorCode | String | Error code | true |
| errorMsg | String | Error description | true |

`JSON` format

```json
  "errorMessages": [],
  "success": true,
  "data": {
    "id": 141,
    "gmtCreate": "2025-09-18T02:35:40.599+00:00",
    "gmtModified": "2025-09-18T02:35:40.599+00:00",
    "tenant": "fmthktsjdb",
    "code": "3c31d315-43a1-47f7-81ab-12b0d75fd2ab",
    "workspaceCode": "fmthktsjdb",
    "name": "fangyu test-Baidu",
    "version": "1757382560369",
    "desc": "fangyu test",
    "toolType": "api",
    "toolSubType": null,
    "owner": {
      "id": null,
      "gmtCreate": null,
      "gmtModified": null,
      "tenant": null,
      "uniqueCode": "33ad2daf266d454a9cd1a9469a75c53d",
      "source": null,
      "outerId": null,
```

```json
      "name": "test"
```

`},`

```json
    "serviceConfig": {
      "executorName": "openPlatformSpiToolExecutor",
      "result2PromptName": null,
      "serviceInvocationConfig": null,
      "toolCommonConfig": null,
      "llmConfig": null,
      "toolApiConfig": {
        "apiUrl": "http://www.baidu.com",
        "toolTags": null,
        "apiProtocol": "get",
        "platformTool": null,
        "limitQps": 50,
        "apiHeaderList": [
            "fieldCode": "Content-Type",
            "fieldType": "CONSTANT",
            "fieldValue": "application/json",
            "fieldDesc": "",
            "flowEditable": false,
            "encrypt": false
```

`],`

```json
        "requestToolApiFieldList": [
            "fieldCode": "a",
            "fieldType": "STRING",
            "parentFieldCode": null,
            "required": false,
            "leaf": null,
            "flowEditable": true,
            "fieldDemo": null,
            "fieldDesc": "",
            "extend": null,
            "refType": null,
            "refValue": "",
            "propertyValue": null,
            "children": null
```

`],`

```json
        "responseToolApiFieldList": [
            "fieldCode": "b",
            "fieldType": "STRING",
            "parentFieldCode": null,
            "required": false,
            "leaf": null,
            "flowEditable": true,
            "fieldDemo": null,
            "fieldDesc": "",
            "extend": null,
            "refType": null,
            "refValue": "",
            "propertyValue": null,
            "children": null
```

`],`

```json
        "asyncExecutorFlag": false,
        "mockResponse": null,
        "preHandle": null,
        "reasoningModel": null,
        "promptTemplate": null,
```

```json
        "preHandlerScript": null,
        "httpMethod": "GET",
        "responseParserName": null,
        "returnByStream": false,
        "toolApiMetaConfigDTO": null,
        "browserExecution": null
```

`},`

```json
      "toolScriptConfig": null,
      "searchChunkConfig": null,
      "toolUseDetail": null,
      "mcpConfig": null
```

`},`

```json
    "shareWorkspaces": null,
    "allFlag": null
```

`},`

```json
  "errorCode": null,
  "errorMsg": null,
  "extraData": null,
  "traceId": null,
  "env": null,
  "other": null,
  "firstErrorMessage": null,
  "failure": false
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |

| l | OpenTrek Dev Developer Guide·P atform Function Class |   | OpenTre | k |
|---|---|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.1.2.5. PostAgentOpenapiToolDelete**

Delete a tool

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| uniqueCode | String | Body | Yes | a9c81580-8e93-42e1-b331- 5cc6506c0093 | The encoding of the tool. This parameter is required. |
| version | String | Body | Yes | 1759118429269 | The version of the tool. This parameter is required. |

**Response parameters**

| Field | Data types | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |
| errorCode | String | The error code. | true |
| errorMsg | String | The error message. | true |

```
 JSON format
```

```json
  "errorMessages": [],
  "success": true,
  "data": null,
  "errorCode": null,
  "errorMsg": null,
  "extraData": null,
  "traceId": null,
  "env": null,
  "other": null,
  "firstErrorMessage": null,
  "failure": false
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.1.3. Intelligence body template**

**1.2.1.3.1. PostAgentOpenapiTemplateGetone**

Querying the Details of an Intelligence Template

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| itemCode | String | Body | Yes | 3b7628cc51544996908b6ea 55ae07bc1 | The encoding of the template. This parameter is required. |

**Response parameters**

| Field | Data types | Description | Examples |
|---|---|---|---|
| success | Boolean | Success | true |
| data | Object | Return data | {} |
| itemCode | String | Template encoding | 3b7628cc51544996908b6e a55ae07bc1 |
| itemName | String | Template Name | Conversation Assistant |
| agentDesc | String | agent description | DB with table recall |
| marketCode | String | Template type, system=platform templates, common=custom templates | system |
| showDetail | Object | Template details |   |
| errorCode | String | The error code. | true |
| errorMsg | String | The error message. | true |

`JSON` format

```json
  "success": true,
  "errorCode": null,
  "errorMsg": null,
  "data": {
    "marketCode": "system",
    "marketName": "Custom templates",
"itemCode":"3b7628cc51544996808b6ea55ae07bc1",
```

```json
    itemCode: 3b7628cc51544996808b6ea55ae07bc1,
    "itemName": "AutoBot dialog assistant",
    "itemLabels": ["Built-in"],
    "itemType": "agentTemplate",
    "targetCode": "851d5b0b-8393-497c-b909-1d3209efee74",
    "targetName": "v1.0",
    "targetVersion": "1731573095677",
    "status": "online",
    "statusDesc": "The service has been installed.",
    "showDetail": {
      "type": "platform",
      "description": "Comprehensive Q&A capabilities",
      "skills": [
        "Support access to users' existing business APIs",
        "Supports the OneRag plug-in to link user business data",
        "Support for accessing other agent instances"
```

`],`

```json
      "usage": {
        "configDesc": "None",
        "limitDesc": "None"
```

`},`

```json
      "interfaceInfo": {
        "interfaceDesc": "None",
        "inputParams": [
            "name": "sessionId",
            "label": "sessionId",
            "type": "STRING",
            "necessary": true,
            "example": "bd962db7-b1c8-4466-a2cc-41b9b67cd94b"
```

`},`

```json
            "name": "stream",
            "label": "Whether to stream",
            "type": "BOOL",
            "necessary": true,
            "example": "true"
```

`},`

```json
            "name": "message",
            "label": "Request message body",
            "type": "OBJECT",
            "necessary": true,
            "example": "{\"text\":\" Book me a ticket from Shanghai to Zurich tomorrow \"}",
            "children": [
                "name": "text",
                "label": "Conversation input",
                "type": "STRING",
                "necessary": true
```

`]` `],`

```json
        "outputParams": [
            "name": "object",
            "label": "Data type",
            "type": "STRING",
            "necessary": true,
            "example": "message.delta"
```

`},`

```json
"name":"role",
```

```json
            name: role,
            "label": "Role",
            "type": "STRING",
            "necessary": true,
            "example": "assistant"
```

`},`

```json
            "name": "sessionId",
            "label": "Current session ID",
            "type": "STRING",
            "necessary": true
```

`]` `},`

```json
    "config": null,
    "feature": {
      "templateType": "AutoBot"
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |

| OpenTrek |   | OpenTrek Dev Developer Guide· |
|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.1.3.2. PostAgentOpenapiTemplatePagequery**

Query the list of intelligence templates

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| current | Integer | Body | Yes | 1 | The current number of pages. This parameter is required. |
| pageSize | Integer | Body | Yes | 10 | The number of pieces per page. This parameter is required. |
| name | String | Body | Yes | Conversation Assistant | Fuzzy search for the template name. This parameter is required. |

**Response parameters**

| Field | Data types | Description | Examples |
|---|---|---|---|
| success | Boolean | Success | true |
| data | Object | Return data | {} |
| total | Integer | Total number of templates queried | 1 |
| list | List | The list of queried templates. |   |

| > Document Version: 202 | 60901 |   | 67 |
|---|---|---|---|

| Field | Data types | Description | Examples |
|---|---|---|---|
| itemCode | String | Template encoding | 3b7628cc51544996908b6e a55ae07bc1 |
| itemName | String | Template Name | Conversation Assistant |
| agentDesc | String | agent description | DB with table recall |
| marketCode | String | Template type, system=platform templates, common=custom templates | system |
| showDetail | Object | Template details |   |
| pageSize | Integer | The number of entries returned per page. | 60 |
| current | Integer | Current Page | 1 |
| errorCode | String | The error code. | true |
| errorMsg | String | The error message. | true |

```
 JSON format
```

```json
  "success": true,
  "errorCode": null,
  "errorMsg": null,
  "data": {
    "total": 1,
    "current": 1,
    "pageSize": 10,
    "totalPages": 1,
    "list": [
        "marketCode": "common",
        "marketName": "Custom templates",
        "itemCode": "79d39852ceb148b9a0afe674a2e6d38d",
        "itemName": "whatsapp",
        "itemLabels": ["whatsapp"],
        "itemType": "agentTemplate",
        "targetCode": "22bb7850-78b2-4ce7-b29d-682460f6a6ed",
        "targetName": "Tool",
        "targetVersion": "1740037093657",
        "status": "online",
        "statusDesc": "The service has been installed.",
        "showDetail": {
          "icon": "AGENT_ICON_6",
          "description": "whatsapp",
          "type": "custom",
          "usage": {
            "configDesc": "whatsapp",
            "limitDesc": "whatsapp"
```

`},`

```json
          "interfaceInfo": {
            "interfaceDesc": "whatsapp",
            "inputParams": [
                "name": "sessionId",
                "label": "sessionId",
                "type": "STRING",
                "necessary": true,
                "example": "bd962db7-b1c8-4466-a2cc-41b9b67cd94b"
```

`],`

```json
            "outputParams": [
                "name": "object",
                "label": "Data type",
                "type": "STRING",
                "necessary": true,
                "example": "message.delta"
```

`]` `},`

```json
        "config": {
          "agentCode": "22bb7850-78b2-4ce7-b29d-682460f6a6ed",
          "agentName": "lxj agent view",
          "versionName": "Tool",
          "versionCode": "1740037093657"
```

`]`

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.1.4. Prompt Template**

**1.2.1.4.1. PostAgentOpenapiPromptSave**

Create /update prompt word templates

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |

| OpenTrek |   |   |   | OpenT | rek Dev Developer Guide· latform Function Clas |
|---|---|---|---|---|---|

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| id | Integer | Body | Yes | 12 | Unique identifier of the prompt template (required for update scenarios) |
| name | String | Body | Yes | Test | The name of the prompt template. This parameter is required. |
| labels | Repeat List | Body | Yes | ["Workplace Efficiency"] | The category label. This parameter is required. |
| frame | String | Body | Yes | Custom | The type of the prompt frame. This parameter is required. Valor: Custom \| CRISPE \| Few-shot |
| promptTemp | String | Body | Yes | Test content | The summary of the prompt word. This parameter is required. |
| prompt | String | Body | Yes | {"prompt":"Convert this md content to txt format and output only the txt format content '''markdown {{mdContent}} '''"} | The content of the prompt template, in the structured JSON format. This parameter is required. |

**Response parameters**

| Field | Data types | Description | Examples |
|---|---|---|---|
| success | Boolean | Success | true |
| errorCode | String | The error code. | true |
| errorMsg | String | The error message. | true |

```json
 JSON format
    "success": true,
    "errorCode": null,
    "errorMsg": null
```

**Additional information**

| HTTP status return code | The error message. | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.1.4.2. PostAgentOpenapiPromptDeploy**

Publish prompt word templates

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| id | Integer | Body | Yes | 1234 | The unique identifier of the prompt template. This parameter is required. |

**Response parameters**

| Field | Data types | Description | Examples |
|---|---|---|---|
| success | Boolean | Success | true |
| errorCode | String | The error code. | true |
| errorMsg | String | The error message. | true |

```json
 JSON format
    "success": true,
    "errorCode": null,
    "errorMsg": null
```

**Additional information**

| HTTP status return code | The error message. | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |

| l | OpenTrek Dev Developer Guide·P atform Function Class |   | OpenTre | k |
|---|---|---|---|---|

| HTTP status return code | The error message. | Error interpretation |
|---|---|---|
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.1.4.3. PostAgentOpenapiPromptQueryprompttypes**

Query prompt word classification

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| current | Integer | Body | Yes | 1 | The current number of pages. This parameter is required. |
| pageSize | Integer | Body | Yes | 10 | The number of pieces per page. This parameter is required. |

**Response parameters**

| Field | Data types | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |
| data | Object | Response parameters | {} |
| total | Integer | The total number of types of prompt words queried. | 1 |

| Field | Data types | Description | Sample value |
|---|---|---|---|
| list | List | The list of types of prompt words queried. |   |
| code | String | Unique code for prompt word classification | ZCXL |
| name | String | Prompt word classification name | Workplace efficiency |
| pageSize | Integer | Size per page | 60 |
| current | Integer | Current Page | 1 |
| errorCode | String | The error code. | true |
| errorMsg | String | The error message. | true |

```json
 JSON format
    "success": true,
    "data": {
        "total": 1,
        "list": [
                "id": null,
                "gmtCreate": "2025-06-17T07:20:49.621+00:00",
                "gmtModified": "2025-06-17T07:20:49.621+00:00",
                "code": "ZCXL",
                "name": "Workplace efficiency",
                "marketType": "promptTemplate",
                "desc": null,
                "owner": {
                    "userId": "503",
                    "userName": "test"
```

`},`

```json
                "modifiyUser": null,
                "recommendItems": null,
                "feature": null,
                "managers": null
```

`],`

```json
        "pageSize": 10,
        "current": 1,
        "totalPages": 1
```

`},`

```json
    "errorCode": null,
    "errorMsg": null
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.1.4.4. PostAgentOpenapiPromptDelete**

Delete a prompt word template

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| id | Integer | Body | Yes | 1234 | The unique identifier of the prompt template. This parameter is required. |

**Response parameters**

| Field | Data types | Description | Examples |
|---|---|---|---|
| success | Boolean | Success | true |
| errorCode | String | The error code. | true |
| errorMsg | String | The error message. | true |

```json
 JSON format
    "success": true,
    "errorCode": null,
    "errorMsg": null
```

**Additional information**

| HTTP status return code | The error message. | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |

| l | OpenTrek Dev Developer Guide·P atform Function Class |   | OpenTre | k |
|---|---|---|---|---|

| HTTP status return code | The error message. | Error interpretation |
|---|---|---|
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.1.4.5. PostAgentOpenapiPromptPagequery**

Query the list of prompt word templates

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| current | Integer | Body | Yes | 1 | The current number of pages. This parameter is required. |
| pageSize | Integer | Body | Yes | 10 | The number of pieces per page. This parameter is required. |
| type | String | Body | Yes | custom | The type of the prompt word template. This parameter is required. custom: my prompt word. platform: platform prompt word. |
| name | String | Body | Yes | Test name | The name of the prompt word. Fuzzy search is required. |

**Response parameters**

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |

| 78 |   | > Doc | ument Version: 20260901 |
|---|---|---|---|

| OpenTrek |   | OpenTr | ek Dev Developer Guide· latform Function Clas |
|---|---|---|---|

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| data | Object | Return data | {} |
| total | Integer | Total number of prompt word templates queried | 1 |
| list | List | The list of prompt word templates that are queried. |   |
| id | Integer | Unique encoding of prompt word templates | 57 |
| name | String | Prompt Word Template Name | md format to txt |
| type | Integer | The type of the prompt word template. custom: my prompt word. system: platform prompt word. | custom: my prompt word, system: platform prompt word |
| labels | String | Category label | ["Workplace Efficiency"] |
| projectCode | String | Workspace encoding | baseline |
| frame | String | Cue frame type, Custom \| CRISPE \| Few-shot | Custom |
| prompt | String | The content of the hint template in the structured JSON format. | {"prompt":"Convert this md content to txt format and only output the txt format content 'markdown {{mdContent}} '''"} |
| pageSize | Integer | Size per page | 60 |
| current | Integer | Current Page | 1 |
| errorCode | String | The error code. | true |
| errorMsg | String | The error message. | true |

```
 JSON format
```

```json
  "errorMessages": [],
  "success": true,
  "data": {
    "extInfos": {},
    "total": 1,
    "list": [
        "id": 5,
        "projectCode": "fmthktsjdb",
        "name": "Shenyang Custom",
        "frame": "Custom",
        "prompt": "{\"prompt\":\" You are a {{discipline}} professor who answers user questions based
on your expertise. \"}",
        "promptTemp": "You are a {{discipline}} professor who answers user questions based on your
expertise. ",
        "debugModel": "rsv-ik4zut8s",
        "debugModelVersion": "OPENTREK_MODEL_DEFAULT_VERSION",
        "debugArgs": "{\" Subject \":\" Computer \"}",
        "debugStatus": "success",
        "debugResult": "Of course, I will do my best to help you with computer science questions. What
are you interested in? Examples include programming languages, data structures, algorithms, operating systems, networks, and databases. ",
        "creatorId": null,
        "creator": null,
        "modified": null,
        "lastModified": null,
        "gmtCreate": "2025-07-21T07:00:33.013+00:00",
        "gmtModified": "2025-09-05T02:24:45.976+00:00",
        "isDel": false,
        "type": "custom",
        "labels": [
          "Marketing Copy",
          "Workplace Efficiency"
```

`],`

```json
        "operateControl": null
```

`],`

```json
    "pageSize": 10,
    "current": 1,
    "totalPages": 1
```

`},`

```json
  "errorCode": null,
  "errorMsg": null,
  "extraData": null,
  "traceId": null,
  "env": null,
  "other": null,
  "firstErrorMessage": null,
  "failure": false
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |

| OpenTrek |   | OpenTrek Dev Developer Guide· |
|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

#### Knowledge Base Management

**1.2.2.1. PostKortexApiKbDocFileDelete**

Document knowledge base Delete Document

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| kbCode | String | Body | Yes | kk062kg1t4hd | knowledge base unique encoding. This parameter is required. |
| fileCode | String | Body | No | 3fedc04432424c9886b1bbb6 9666b7ed | Document code (used for single deletion, select one of fileCodes and fileCodes) |
| fileCodes | Repeat List | Body | No | ["3fedc04432424c9886b1bb b69666b7ed", "394e8fa103844b3c96d6810 ae5bc6bed"] | Document code list (used for batch deletion, select one of fileCode and fileCode) |

**Response parameters**

| Field | Data types | Description | Examples |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |
| data | object | Return Data | {} |
| affected | Integer | Number of affected | 1 |
| errorCode | String | The error code. | true |
| errorMsg | String | The error message. | true |

```json
 JSON format
    "success": true,
    "data": {
        "affected": 1
```

`},`

```json
    "errorCode": null,
    "errorMsg": null
```

**Additional information**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |

| OpenTrek |   | OpenTrek Dev Developer Guide· latform Function Clas |
|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.2.2. PostKortexApiKbUpdateMateData**

Update the metadata of a knowledge base.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request header parameters**

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| x-sfm-authorization | String | No | The APP KEY. _ | Bearer YOUR APP KEY _ _ |
| x-sfm- workspacecode | String | Yes | The target workspace. | workspace code _ |
| Content-Type | String | Yes | The Content-Type. | application/json |

**Request body parameters**

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| code | String | Yes | The unique code of the knowledge base. | z7pn9wbtkpy0 |
| name | String | No | The name of the knowledge base. | Test |

| description | String | No | The description of the knowledge base. | Test knowledge base |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|
| success | Boolean | Indicates whether the operation succeeded. | true |
| data | object | The returned data. | {} |
| updates | Integer | Indicates whether the update succeeded. | 1 |
| errorCode | String | The error code. | true |
| errorMsg | String | The error description. | true |

`JSON` format

```json
    "success": true,
    "data":{
  "stats":{
   "metaAffects":{
    "updates":1
```

`},`

```json
    "errorCode": null,
    "errorMsg": null
```

**Document supplementary notes**

| HTTP status code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | A required parameter for the gateway is missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed. The APP KEY is _ invalid. |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. The APP KEY _ has expired. |

| 401 | GATEWAY ROLE NOT MATCH! | Authentication failed. The role associated with the current APP KEY _ user does not match. |
|---|---|---|
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role associated with the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | The service invocation path is invalid. |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service invocation path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggered throttling. Try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggered throttling. Try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | A required business parameter is missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The workspace code passed does not match the workspace code associated with the APP KEY user. _ |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. The authentication method is not supported. |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed. The user role does not match. |

**1.2.2.3. PostKortexApiKbDataConsumebulk**

Writes data to the knowledge base based on the knowledge base data model definition. You can add, delete, and modify data.

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |

| OpenTrek Dev | Develop | er Guide·P |   |   | OpenTre |
|---|---|---|---|---|---|

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| kbCode | String | Body | Yes | cozhklqn3omz | knowledge base unique encoding. This parameter is required. |
| kbSubmodel Code | String | Body | Yes | 1234 | The unique encoding of the knowledge base content structure, which can be obtained by knowledge base details. This parameter is required. |
| datasourceN odeId | String | Body | Yes | source builtin smod _ _ | Data processing source knowledge base documents are transferred by the scene of the DKE processing chunk source builtin dke; other _ _ scene transfer source builtin smod; delete _ _ scene transfer kb submodel. _ This parameter is required. |
| forceReplace | Boolea n | Body | Yes | false | Forcibly replace semantics. This parameter is required. |
| data | Repeat List | Body | Yes | [] | The data set to be changed. This parameter is required. |
| -key | Repeat List | Body | No | [] | The ID of the data key. This parameter is required. |
| -operation | String | Body | No | Insert\|Delete\|Update | operation. Note that the operation must be the same in a message. This parameter is required. |

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| -after | Json | Body | No | {} | The specific data content varies according to the structure of different assemblies in the knowledge base. When Insert \| Update needs to transfer data to the after node, note that Update does not support incremental updates, and full data model field definitions need to be transferred for each update. When Delete is not required, but to ensure that the key node has a value, this parameter is required. |

**Response parameters**

| Field | Data types | Description | Examples |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |
| data | object | Return Data | {} |
| errorCode | String | The error code. | true |
| errorMsg | String | The error message. | true |

```json
 JSON format
    "success": true,
    "data": null,
    "errorCode": null,
    "errorMsg": null
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |

| OpenTrek Dev Developer Guide·P |   |   |
|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.2.4. GetKortexApiStatisticsTrend**

Obtain the time series data required for a trend chart

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| startTime | String | Query | No. | 2025-08-30 | The start time of the filter. Format: YYYY-MM-DD. |
| endTime | String | Query | No | 2025-01-26 | The end time of the filter. Format: YYYY-MM-DD. The default is the last seven days |

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| dataType | String | Query | No | 201 | Currently, only document knowledge base is supported. |
| timeRange | String | Query | No | last 7 days _ _ | The preset time range. Valid values: last 7 days, _ _ last 30 days, last 90 days, _ _ _ _ and last 180 days. StartTime _ _ and endTime are ignored when this parameter is provided |

**Response parameters**

| Field | Data types | Description | Examples |
|---|---|---|---|
| errorCode | Integer | Error code | 200 |
| errorMsg | String | Error message | success |
| success | Boolean | Indicates whether the request was successful. | true |
| data | Object | Trend data | {"dimensions": [{...},{...}], "source": [[...], ...]} |
| dimensions | List | Fixed structure returns: a list of names of dimensions and metrics that define the meaning of each column in the source array. | [{"key":"date","label":"time "}, {"key":"fileCount","label":"t otal number of files"}, {"key":"fileSize","label":"fil e size"}, {"key":"tokenCount","label ":"total number of tokens"}] |
| source | List | The data matrix. Each row represents a point in time. The values in each column correspond to the names in the dimensions array. | [["2025-08-30", 18000, 1572864, 23943], ["2025- 01-21", 22000, 2097152, 134667]] |

`JSON` format

```json
  "success": true,
  "data": {
    "dimensions": [
        "key": "date",
        "label": "Time"
```

`},`

```json
        "key": "fileCount",
        "label": "Total number of files"
```

`},`

```json
        "key": "fileSize",
        "label": "File size"
```

`},`

```json
        "key": "tokenCount",
        "label": "total number of tokens"
```

`],`

```json
    "source": [
```

`[`

```
        "2025-08-29",
```

`1,`

```
        3532962,
        121036
```

`],` `[`

```
        "2025-08-30",
```

`1,`

```
        3532962,
        121036
```

`],` `[`

```
        "2025-08-31",
```

`1,`

```
        3532962,
        121036
```

`],` `[`

```
        "2025-09-01",
```

`1,`

```
        3532962,
        121036
```

`]` `]` `},`

```json
  "errorCode": null,
  "errorMsg": null
```

**Additional information**

| HTTP status return code | The error message. | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |

| OpenTrek |   | OpenTrek Dev Developer Guide· |
|---|---|---|

| HTTP status return code | The error message. | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.2.5. PostKortexApiKbDelete**

Delete knowledge base

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| code | String | Body | Yes | rkiviej5rkm2 | knowledge base unique encoding. This parameter is required. |

**Response parameters**

| Field | Data types | Description | Examples |
|---|---|---|---|
| success | Boolean | Success | true |
| data | object | Return data | {} |
| kb | Object | (Custom old) knowledge base dimension statistics |   |
| deletes | Integer | Number of Deletions | 1 |
| kbSubmodel | Object | (Custom old) knowledge base data model dimension statistics |   |
| deletes | Integer | Number of Deletions | 1 |
| kbSubmodelField | Object | (Custom Old) knowledge base Data Model Field Dimension Statistics |   |
| deletes | Integer | Number of Deletions | 1 |
| kbIndex | Object | (Custom old) knowledge base index dimension statistics |   |
| deletes | Integer | Number of Deletions | 1 |
| kbIndexField | Object | (Custom old) knowledge base index field dimension statistics |   |
| deletes | Integer | Number of Deletions | 1 |
| monoDeletes | Object | (Document knowledge base | Graphic knowledge base) delete operation statistics object |
| kb | Object | Knowledge base |   |
| deletes | Integer | Number of Deletions | 1 |
| kbSubmodel | Object | knowledge base data model |   |
| deletes | Integer | Number of Deletions | 1 |
| kbSubmodelField | Object | knowledge base Data Model Fields |   |
| deletes | Integer | Number of Deletions | 1 |
| kbIndex | Object | knowledge base index |   |
| deletes | Integer | Number of Deletions | 1 |
| kbIndexField | Object | knowledge base index fields |   |

| OpenTrek |   | OpenTr | ek Dev Developer Guide· latform Function Clas |
|---|---|---|---|

| Field | Data types | Description | Examples |
|---|---|---|---|
| deletes | Integer | Number of Deletions | 1 |
| kbdocFileDeletes | Integer | (Document knowledge base) Total number of files deleted | 0 |
| kbVisualFileDeletes | Integer | (Graphic knowledge base) Total number of pictures deleted | 0 |
| errorCode | String | Error code | true |
| errorMsg | String | The error message. | true |

```json
 JSON format
    "success": true,
    "data": {
        "monoDeletes": {
            "kbIndex": {
                "deletes": 2
```

`},`

```json
            "kb": {
                "deletes": 1
```

`},`

```json
            "kbSubmodelField": {
                "deletes": 9
```

`},`

```json
            "kbSubmodel": {
                "deletes": 1
```

`},`

```json
            "kbIndexField": {
                "deletes": 6
```

`},`

```json
        "kbdocFileDeletes": 0
```

`},`

```json
    "errorCode": null,
    "errorMsg": null
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |

| OpenTrek Dev Developer Guide·P atform Function Class |   | OpenTre |
|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.2.6. PostKortexApiKbMonoDetail**

Get knowledge base data model definitions and other details

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| code | String | Body | Yes | rkiviej5rkm2 | knowledge base unique encoding. This parameter is required. |

**Response parameters**

| Field | Data types | Description | Examples |
|---|---|---|---|
| success | Boolean | Success | true |

| 94 |   | > Doc | ument Version: 20260901 |
|---|---|---|---|

| OpenTrek |   |   | latform Function Clas |
|---|---|---|---|

| Field | Data types | Description | Examples |
|---|---|---|---|
| data | object | Return data | {} |
| code | String | knowledge base unique encoding | tzf5wnyvkfdg |
| name | String | knowledge base name | Central verification |
| description | String | knowledge base Description | Annual Report Document |
| kbType | Integer | knowledge base Type | 100,"Custom knowledge base", 201,"Document knowledge base", 202,"BI knowledge base", 203,"Graphic knowledge base" |
| kbProperties | Object | knowledge base extended attributes, see the explanation of the field with the same name related to the knowledge base creation interface. |   |
| kbSubmodels | List | For more information about the knowledge base data model, see the definition of fields with the same name related to the knowledge base creation interface. |   |
| kbSubmodelName | String | Custom Standard knowledge base Name |   |
| kbSubmodelCode | String | Custom standard knowledge base data model unique encoding |   |
| kbSubmodelFields | List | Attribute information included in custom standard knowledge base |   |
| fieldName | String | Field name, database field naming syntax, hump scene with underscore | matter name _ |
| fieldComment | String | Field Interpretation | Name of matter |
| fieldType | String | Field type varchar \| varchar 64 \| varchar 256 \| _ _ varchar 1024 \| integer _ | varchar 1024 _ |
| fieldIndexExt | String | Description of index- related extensions | filter |
| kbSubmodelCode | String | Attribution Data Model Encoding |   |
| kbCode | String | Ownership knowledge base Code |   |

| OpenTrek Dev Developer | Guide·P |   |   |
|---|---|---|---|
| atform Function Class |   |   | OpenTre |
| Field | Data types | Description | Examples |
| kbIndexes | List | Index information included in custom standard knowledge base |   |
| kbIndexCode | String | Unique encoding for index storage |   |
| kbSubmodelCode | String | Attribution Data Model Encoding |   |
| kbCode | String | Ownership knowledge base Code |   |
| kbIndexEngineType | String | index type builtin vector: _ vector index engine; builtin es: full-text index _ engine | builtin vector _ |
| kbIndexName | String | Index Definition Name | Matched Name Match |
| kbIndexFields | List | Index field definition |   |
| fieldName | String | Field name, database field naming syntax, hump scene with underscore | matter name _ |
| fieldIndexType | String | field index type resource for recall; retrieve for retrieval | resource |
| kbIndexProperties | Object | Text Vectorization Model Data Encapsulation |   |
| model | Object | The text vectorization model configuration. The structure is the same as that of the preceding textModel. You must select modelType=EMBEDDING. |   |
| indexType | String | Index type vector \| es | vector |
| refRes | String | knowledge base Reference Resources |   |
| disableFlag | Integer | Whether to enable | 1 |
| createTime | String | Creation time | 2025-07- 16T15:00:24.192928 |
| createUser | String | knowledge base Creator | dke |

`JSON` format

```json
    "success": true,
    "data": {
        "code": "z7pn9wbtkpy0",
        "name": "Custom knowledge base",
        "description": "Test custom knowledge base creation",
        "kbType": 100,
        "kbProperties": null,
        "kbSubmodels": [
                "kbSubmodelCode": "z7pn9wbtkpy0x6l8",
                "kbSubmodelName": "Standard knowledge base",
                "kbSubmodelFields": [
                        "kbCode": "z7pn9wbtkpy0",
                        "kbSubmodelCode": "z7pn9wbtkpy0x6l8",
                        "fieldName": "matter_code",
                        "fieldType": "varchar_256",
                        "fieldComment": "Event code",
                        "fieldDefaultValue": null,
                        "fieldIndexExt": null
```

`},`

```json
                        "kbCode": "z7pn9wbtkpy0",
                        "kbSubmodelCode": "z7pn9wbtkpy0x6l8",
                        "fieldName": "matter_name",
                        "fieldType": "varchar_256",
                        "fieldComment": "Event name",
                        "fieldDefaultValue": null,
                        "fieldIndexExt": null
```

`],`

```json
                "kbIndexes": [
                        "kbCode": "z7pn9wbtkpy0",
                        "kbSubmodelCode": "z7pn9wbtkpy0x6l8",
                        "kbIndexCode": "z7pn9wbtkpy0w83n",
                        "kbIndexName": "Matched name matching",
                        "kbIndexEngineType": "builtin_vector",
                        "kbIndexProperties": {
                            "indexType": "vector",
                            "dimensionSize": 1536,
                            "model": {
                                "abilities": [
```

`],`

```json
                                "modelName": "New word embedding",
                                "path": "/api/batch_predict_embeddings",
                                "modelSource": "system",
                                "modelExtParams": [
```

`],`

```json
                                "customModelMappings": [
```

`],`

```json
                                "modelCode": "rsv-e9modnqp",
                                "invokeUrl": "http://ai-gateway-svc:8090/v1/router/call/rsv-e9modnqp",
                                "modelConfigMode": "normal",
                                "modelType": "EMBEDDING",
                                "source": "system"
```

`},`

```json
                        "kbIndexFields": [
                                "fieldName": "matter_code",
                                "fieldIndexType": "resource"
```

`},`

```json
                                "fieldName": "matter_name",
                                "fieldIndexType": "retrieve"
```

`]` `]` `],`

```json
        "refRes": null,
        "disableFlag": 0,
        "createTime": "2025-07-22T22:59:48.073965",
        "updateTime": "2025-07-22T22:59:48.073969",
        "createUser": "gaochai"
```

`},`

```json
    "errorCode": null,
    "errorMsg": null
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |

|   | OpenTrek |   | OpenTrek Dev Developer Guide· latform Function Clas | P s |
|---|---|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.2.7. PostKortexApiKbCreate**

Create knowledge base

**Request header**

This interface uses common request headers without special request headers. See the public request parameters documentation.

**Parameters**

| Field | Data types | Required | Description | Sample value |
|---|---|---|---|---|
| name | String | Yes | Name | Test Engineer |
| description | String | Yes | knowledge base Description | Test |
| kbType | Integer | Yes | knowledge base Type | 100,"Custom knowledge base", 201,"Document knowledge base", 202,"Q knowledge base", 203,"Graphic knowledge base" |
| kbProperties | Object | Yes | These 6 attributes of any knowledge class type, must have a value of type, and no knowledge base type is specified) |   |
| processStrategy | Object | Yes | Document knowledge base (attribute non-group can be seen) |   |
| chunkStrategyMetho d | String | Yes | Segmentation policy, which is passed by default | default |
| processStrategyMeth od | String | Yes | Parsing strategy (simple basic parsing only extracts text from documents), deep parsing increases parsing capabilities such as pictures, tables, and formulas) | deep |
| processDeepConfigs | List | Yes | Parsing strategy (simple basic parsing only extracts text from documents), deep parsing increases parsing capabilities such as pictures, tables, and formulas) |   |

| Field | Data types | Required | Description | Sample value |
|---|---|---|---|---|
| key | String | Yes | In-depth parsing enables image OCR, table parse table _ parsing, equation parse _ formula parsing, and if figure enhance _ _ image enhancement. |   |
| enable | String | Yes | Whether to enable | true |
| textModel | Object | Yes | Document knowledge base (text vectorization model)-Model service parameters can be described through the platform procedures, general knowledge base details interface for knowledge, according to the school-level service characteristics, after the organization needs to be used in the form of a table, search into the number of the necessary space, and once the confirmation step may affect the generation, can not be changed. |   |
| modelType | String | Yes | The type of the model. This value is the type of the model trained by "EMBEDDING". |   |
| invokeUrl | String | Yes | The service address of the model call. |   |
| path | String | Yes | Request URL for model invocation |   |
| modelConfigMode | String | Yes | The type of the model configuration. You can set this field to normal. | normal |
| modelSource | String | Yes | The source of the model. You can set the value to system. | system |
| modelCode | String | Yes | Model encoding |   |
| modelName | String | Yes | Model name |   |
| visualProcess | Boolean | Yes | Graphic knowledge base (whether intelligent parsing is enabled) |   |

| Field | Data types | Required | Description | Sample value |
|---|---|---|---|---|
| visualProcessModel | Object | Yes | Graphic knowledge base (including 5 grid models). TextModel must be sent to the model, and the model configuration with modelType=vlm must be filled in. Model service parameters can be described in the platform procedures, and the general knowledge base details interface can be used for detailed knowledge. According to the school-level service characteristics, after organization, they need to be used in the form of tables and searched for the necessary space. |   |
| visualDescPrompt | String | Yes | Graphic knowledge base (contains 5 items of Prompt, which can also be referred to and described) | Please describe the diagram in short language, without bringing in emotions and plurals. |
| visualIndexModel | Object | Yes | Graphic knowledge base (including 5 lattice models). TextModel is sent to the model, and the model configuration of the modelType=IM EMB _ EDDING must be filled in. Model service parameters can be detailed through the platform procedure description and the general knowledge base details interface. According to the school-level service characteristics, they need to be used in the form of a table after organization, and the necessary space is searched for the number, and once the confirmation step may affect the generation, they cannot be changed. |   |
| indexKTrigger | String | Yes | Graphic knowledge base (image trigger, default pass upload) | upload |

| Field | Data types | Required | Description | Sample value |
|---|---|---|---|---|
| kbSubmodels | List | Yes | Custom text knowledge base must include model definition |   |
| kbSubmodelName | Boolean | Yes | Custom Standard Knowledge Class Name |   |
| kbSubmodelFields | List | Yes | Custom Text Standard Knowledge Class Custom Attribute Item Information |   |
| fieldName | String | Yes | Field name, all database fields contain this, configuration is connected to Qian occupy the lease | matter name _ |
| fieldComment | String | Yes | Field Interpretation | Name of matter |
| fieldType | String | Yes | Field type varchar(varchar 64 _ | varchar 256 _ |
| kbIndexes | List | Yes | Self-defined standard knowledge class self-defined index item information. |   |
| kbIndexEngineType | String | Yes | index type builtin vector image _ index engine, builtin es final text _ index engine | builtin vector _ |
| kbIndexName | String | Yes | Index finitive name | Category |
| kbIndexFields | List | Yes | Index field definition |   |

| Field | Data types | Required | Description | Sample value |
|---|---|---|---|---|
| fieldName | String | Yes | Field name, all database fields contain this, configuration is connected to Qian occupy the lease | matter name _ |
| fieldComment | String | Yes | Field Interpretation | Name of matter |
| fieldType | String | Yes | Field type varchar(varchar 64 _ | varchar 256 _ |
| fieldIndexType | String | Yes | The field index type resource is used for recall and retrieval is used for retrieval. | resource |
| kbIndexProperties | Object | Yes | Text vectorization model link key |   |
| model | Object | Yes | The text vectorization model configuration and structure are the same as the preceding textModel. You must set this parameter to modelType to EMBEDDING. |   |

**Response parameters**

| Field | Data types | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |
| data | object | Return Data | {} |
| stats | Object | Creation details |   |
| kbCode | String | knowledge base unique encoding | y4fu5k9w5yI2 |
| errorCode | String | Error code | true |
| errorMsg | String | The error message. | true |

```json
 JSON format
    "success": true,
    "data": {
        "stats": {
            "metaAffects": {
                "kbIndex": {
                    "deletes": 0,
                    "inserts": 1
```

`},`

```json
                "kb": {
                    "inserts": 1
```

`},`

```json
                "kbSubmodelField": {
                    "deletes": 0,
```

`,`

```json
                    "inserts": 2
```

`},`

```json
                "kbSubmodel": {
                    "deletes": 0,
                    "inserts": 1
```

`},`

```json
                "kbIndexField": {
                    "deletes": 0,
                    "inserts": 2
```

`},`

```json
            "ddlStats_smod": {
                "deletes": {
```

`},`

```json
                "fieldInserts": {
```

`},`

```json
                "inserts": {
                    "z7pn9wbtkpy0x6l8": {
                        "kbSubmodelEntity": {
                            "id": 458,
                            "kbCode": "z7pn9wbtkpy0",
                            "kbSubmodelCode": "z7pn9wbtkpy0x6l8",
                            "kbSubmodelName": "Standard knowledge base",
                            "projectCode": "17ac7ce4-23ad-413b-95f4-55732b15a4b7",
                            "createTime": "2025-07-22T22:59:48.086900569",
                            "createUser": "gaochai",
                            "updateTime": "2025-07-22T22:59:48.086903719",
                            "updateUser": "gaochai"
```

`},`

```json
                        "kbSubmodelFieldEntities": [
                                "id": 3041,
                                "kbCode": "z7pn9wbtkpy0",
                                "kbSubmodelCode": "z7pn9wbtkpy0x6l8",
                                "fieldName": "matter_code",
                                "fieldType": "varchar_256",
                                "fieldComment": "Event code",
                                "fieldDefaultValue": null,
                                "fieldIndexExt": null,
                                "projectCode": "17ac7ce4-23ad-413b-95f4-55732b15a4b7",
                                "createTime": "2025-07-22T22:59:48.099405932",
                                "createUser": "gaochai",
                                "updateTime": "2025-07-22T22:59:48.099409152",
                                "updateUser": "gaochai"
```

`},`

```json
                                "id": 3042,
                                "kbCode": "z7pn9wbtkpy0",
                                "kbSubmodelCode": "z7pn9wbtkpy0x6l8",
                                "fieldName": "matter_name",
                                "fieldType": "varchar_256",
                                "fieldComment": "Event name",
                                "fieldDefaultValue": null,
                                "fieldIndexExt": null,
                                "projectCode": "17ac7ce4-23ad-413b-95f4-55732b15a4b7",
                                "createTime": "2025-07-22T22:59:48.099419083",
                                "createUser": "gaochai",
                                "updateTime": "2025-07-22T22:59:48.099420433",
                                "updateUser": "gaochai"
```

`]` `},`

```json
            "ddlStats_kbidx": {
                "deletes": {
```

`},`

```json
                "fieldInserts": {
```

`},`

```json
                "inserts": {
                    "z7pn9wbtkpy0w83n": {
                        "kbIndexEntity": {
                            "id": 721,
                            "kbCode": "z7pn9wbtkpy0",
                            "kbSubmodelCode": "z7pn9wbtkpy0x6l8",
                            "kbIndexCode": "z7pn9wbtkpy0w83n",
                            "kbIndexName": "Matched name matching",
                            "kbIndexEngineType": "builtin_vector",
                            "kbIndexProperties": "
{\"indexType\":\"vector\",\"dimensionSize\":1536,\"model\":\" modelConfigMode\":\"normal\",\"modelCode\":\"rsv-e9modnqp\",\"modelName\":\" New word embedding \",\"a bilities\":[]," modelExtParams ":[]," modelType ": " EMBEDDING "," modelSource ": " system "," source ": " system "," customModelMappings ":[]," invokeUrl ": " http://ai-gateway-svc:8090/v1/router/call ", rsv-e9modnqp\"path\":\"/api/batch_predict_embeddings\"}}",
                            "projectCode": "17ac7ce4-23ad-413b-95f4-55732b15a4b7",
                            "createTime": "2025-07-22T22:59:48.11207465",
                            "createUser": "gaochai",
                            "updateTime": "2025-07-22T22:59:48.11207763",
                            "updateUser": "gaochai"
```

`},`

```json
                        "kbIndexFieldEntities": [
                                "id": 2305,
                                "kbCode": "z7pn9wbtkpy0",
                                "kbSubmodelCode": "z7pn9wbtkpy0x6l8",
                                "kbIndexCode": "z7pn9wbtkpy0w83n",
                                "fieldName": "matter_code",
                                "fieldType": null,
                                "fieldIndexType": "resource",
                                "fieldIndexDefinition": "
{\"indexType\":\"vector\",\"dimensionSize\":1536,\"model\":\" modelConfigMode\":\"normal\",\"modelCode\":\"rsv-e9modnqp\",\"modelName\":\" New word embedding \",\"a bilities\":[]," modelExtParams ":[]," modelType ": " EMBEDDING "," modelSource ": " system "," source ": " system "," customModelMappings ":[]," invokeUrl ": " http://ai-gateway-svc:8090/v1/router/call ", rsv-e9modnqp\"path\":\"/api/batch_predict_embeddings\"}}",
                                "projectCode": "17ac7ce4-23ad-413b-95f4-55732b15a4b7",
                                "createTime": "2025-07-22T22:59:48.124616445",
                                "createUser": "gaochai",
                                "updateTime": "2025-07-22T22:59:48.124620155",
                                "updateUser": "gaochai"
```

`},`

```json
                                "id": 2306,
                                "kbCode": "z7pn9wbtkpy0",
                                "kbSubmodelCode": "z7pn9wbtkpy0x6l8",
                                "kbIndexCode": "z7pn9wbtkpy0w83n",
                                "fieldName": "matter_name",
                                "fieldType": null,
                                "fieldIndexType": "retrieve",
                                "fieldIndexDefinition": "
{\"indexType\":\"vector\",\"dimensionSize\":1536,\"vectorFieldName\":\"sys_emb_matter_name\",\"model\": {\"modelConfigMode\":\"normal\",\"modelCode\":\"rsv-e9modnqp\",\"modelName\":\" New word embedding \",
```

```json
" abilities ":[]," modelExtParams ":[]," modelType ": " EMBEDDING "," modelSource ": " system "," sour ce ": " system "," customModelMappings ":[]," invokeUrl ": //: " http: ai-gateway-svc 8090/v1/router/call/rsv-e9modnqp\",\"path\":\"/api/batch_predict_embeddings\"}}",
                                "projectCode": "17ac7ce4-23ad-413b-95f4-55732b15a4b7",
                                "createTime": "2025-07-22T22:59:48.124630415",
                                "createUser": "gaochai",
                                "updateTime": "2025-07-22T22:59:48.124631745",
                                "updateUser": "gaochai"
```

`]` `},`

```json
        "kbCode": "z7pn9wbtkpy0"
```

`},`

```json
    "errorCode": null,
    "errorMsg": null
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.2.8. PostKortexApiKbFileDataSync**

For document knowledge base and graphic knowledge base, knowledge base source files can be written through this interface.

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| kbCode | String | Body | Yes | cozhklqn3omz | knowledge base unique encoding. This parameter is required. |
| kbType | Integer | Body | Yes | 201 | The knowledge base type. This parameter is required. |
| referer | String | Body | No | https://example.com | Application source verification can be passed in scenarios where the file address has anti-letether. |
| fileInfo | Repeat List | Body | Yes | [] | Bulk data delivery. This parameter is required. |
| - fileOriginalU rl | String | Body | No | https://****/tmp/pic/8f1af9cb aa9d9aee17a0c0bd944ef662 .jpeg | The full path URL of the original file. The platform supports the whitelist restriction capability. If you access the restricted address, the response "The current file address has been rejected" is returned. This parameter is required. |
| - fileOriginalN ame | String | Body | No | Landscape. jpeg | The name of the file. By default, the text after the last / |

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| - fileOuterCod e | String | Body | No | 111111111 | The external unique identifier of the file, which is recommended to be passed. It is used to return the internal fileCode mapping and preprocessing exception information. |
| - fileOriginalC ontent | String | Body | No | Scenery | File Description (available in graphic knowledge base scenarios) |

**Response parameters**

| Field | Data types | Description | Examples |
|---|---|---|---|
| success | Boolean | Success | true |
| data | object | Return data | {} |
| insert | Integer | Asynchronous quantity to be transferred | 0 |
| update | Integer | Updated quantity | 0 |
| insertMap | JSONObject | File encoding mapping, key: fileOuterCode, value: fileCode | {} |
| errorCode | String | The error code. | true |
| errorMsg | String | The error message. | true |

```json
 JSON format
    "success": true,
    "data": {
        "insert": 1
```

`},`

```json
    "errorCode": null,
    "errorMsg": null,
    "traceId": null,
    "env": null,
    "ext": null
```

**Additional information**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |

|   | OpenTrek |   | OpenTrek Dev Developer Guide· latform Function Clas | P s |
|---|---|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.2.9. PostKortexApiKbEnable**

Enable knowledge base

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| code | String | Body | Yes | rkiviej5rkm2 | knowledge base unique encoding. This parameter is required. |

**Response parameters**

| Field | Data types | Description | Examples |
|---|---|---|---|
| success | Boolean | Success | true |
| data | object | Return Data | {} |
| kbEnable | Integer | Is enabled successfully | 0 |
| errorCode | String | The error code. | true |
| errorMsg | String | The error message. | true |

```json
 JSON format
    "success": true,
    "data": {
        "kbEnable": 1
```

`},`

```json
    "errorCode": null,
    "errorMsg": null
```

**Additional information**

| HTTP status return code | The error message. | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |

| OpenTrek |   | OpenTrek Dev Developer Guide· latform Function Clas |
|---|---|---|

| HTTP status return code | The error message. | Error interpretation |
|---|---|---|
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.2.10. PostKortexApiKbList**

Query the knowledge base list

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| pageIndex | Integer | Body | Yes | 1 | The current request page. This parameter is required. |
| pageSize | Integer | Body | Yes | 10 | The number of requests per page. This parameter is required. |
| kbCode | String | Body | No | qdqsajkhjn6x | knowledge base unique encoding |
| kbName | String | Body | No | Test graphic knowledge base | knowledge base name |
| kbType | Integer | Body | No | 100 | knowledge base Type |

**Response parameters**

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |
| data | object | Return Data | {} |
| total | Integer | Total number of knowledge base queried | 1 |
| list | List | List of knowledge base queried |   |
| code | String | knowledge base unique encoding | qdqsajkhjn6x |
| name | String | knowledge base name | Gao Chai Test Graphic knowledge base |
| kbType | Integer | knowledge base Type | 100,"Custom knowledge base", 201,"Document knowledge base", 202,"Q knowledge base", 203,"Graphic knowledge base" |
| description | String | knowledge base Description | High Firewood Test |
| projectCode | String | Workspace encoding | baseline |
| createTime | String | Creation time | 2025-07- 04T21:28:45.03314 |
| createUser | String | The creator. | gaochai |
| pageSize | Integer | The number of entries returned per page. | 60 |
| current | Integer | Current Page | 1 |
| errorCode | String | The error code. | true |
| errorMsg | String | The error message. | true |

`JSON` format

```json
    "success": true,
    "data": {
        "total": 1,
        "list": [
                "id": 363,
                "code": "z7pn9wbtkpy0",
                "name": "Custom knowledge base",
                "kbType": 100,
                "description": "Test custom knowledge base creation",
                "sysProperties": null,
                "kbProperties": null,
                "refRes": null,
                "state": null,
                "deleteFlag": null,
                "disableFlag": 0,
                "projectCode": "17ac7ce4-23ad-413b-95f4-55732b15a4b7",
                "createTime": "2025-07-22T22:59:48.073965",
                "createUser": "test",
                "updateTime": "2025-07-22T22:59:48.073969",
                "updateUser": "gaochai"
```

`],`

```json
        "pageSize": 60,
        "current": 1
```

`},`

```json
    "errorCode": null,
    "errorMsg": null
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |

| l | OpenTrek Dev Developer Guide·P atform Function Class |   | OpenTre | k |
|---|---|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.2.11. GetKortexApiStatisticsDetails**

Obtains a detailed data list.

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| pageNumber | Integer | Query | Yes | 1 | The current page number. This parameter is required. |
| pageSize | Integer | Query | Yes | 10 | The number of entries to display on each page. This parameter is required. |
| dataType | String | Query | No | 1 | Currently, only document knowledge base is supported. |
| startTime | String | Query | No | 2025-01-20 | The point in time at which the statistics were collected. Format: YYYY-MM-DD. This scenario is consistent with the endTime |

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| endTime | String | Query | No | 2025-01-26 | The point in time at which the statistics were collected. Format: YYYY-MM-DD. This scenario is consistent with startTime. If the end time is not specified, the default time is today. |

**Response parameters**

| Field | Data types | Description | Sample value |
|---|---|---|---|
| errorCode | Integer | Error code | 200 |
| errorMsg | String | Error message | success |
| success | Boolean | Indicates whether the request was successful. | true |
| data | Object | Paging Data Object | 0 |
| pageNumber | Integer | The page number of the returned page. | 1 |
| pageSize | Integer | Number of entries displayed per page | 10 |
| totalCount | Integer | The total number of entries returned. | 35 |
| columns | List | Column definition metadata | [{"label": "data type", "value": "dataType"}] |
| label | String | Display name of the column | Data types |
| value | String | Field Key of the column | dataType |
| list | List | Data list of the current page | [{...}] |
| kbName | String | knowledge base name | sea impact test data set |
| fileCount | Integer | Number of original files | 15 |
| fileSize | Integer | Original File Size (Bytes) | 214748364800 |
| tokenCount | Integer | Total number of tokens | 100000 |

`JSON` format

```json
  "success": true,
  "data": {
    "columns": [
        "label": "knowledge base name",
        "value": "kbName"
```

`},`

```json
        "label": "Number of original files",
        "value": "fileCount"
```

`},`

```json
        "label": "Original file size",
        "value": "fileSize"
```

`},`

```json
        "label": "Total number of tokens",
        "value": "tokenCount"
```

`],`

```json
    "pageNumber": 1,
    "pageSize": 10,
    "totalCount": 1,
    "list": [
        "projectCode": "05bb2bad-689b-4518-9a50-53953c65d59a",
        "date": null,
        "fileCount": 1,
        "fileSize": 3532962,
        "fileOtherSizes": null,
        "tokenCount": 121036,
        "kbName": "Gao Chai verification",
        "kbCode": "v8ocqajdnb16"
```

`]` `},`

```json
  "errorCode": null,
  "errorMsg": null
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |

|   |   | latform Function Clas |
|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.2.12. GetKortexApiStatisticsKpi**

Obtain data for three core metrics

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| dataType | String | Query | No. | 201 | Data types |
| startTime | String | Query | No | 2025-01-20 | The point in time at which the statistics were collected. Format: YYYY-MM-DD. This scenario is consistent with the endTime |

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| endTime | String | Query | No | 2025-01-26 | The point in time at which the statistics were collected. Format: YYYY-MM-DD. This scenario is consistent with startTime. If the end time is not specified, the default time is today. |

**Response parameters**

| Field | Data types | Description | Examples |
|---|---|---|---|
| errorCode | Integer | Error code | 0 |
| errorMsg | String | Error message | success |
| success | Boolean | Success | true |
| data | List | Core indicator data list | [{"key": "fileCount", "label": "Total number of files", "value": 1262}, ...] |
| key | String | Metric Key | fileCount\|fileSize\|tokenCou nt |
| label | String | Metric | Total number of original files |
| value | Integer | The metric values. | 1262 |

```
 JSON format
```

```json
  "success": true,
  "data": [
      "key": "fileCount",
      "label": "Total number of files",
      "value": 1
```

`},`

```json
      "key": "fileSize",
      "label": "File size",
      "value": 3532962
```

`},`

```json
      "key": "tokenCount",
      "label": "Total number of tokens (only for document types)",
      "value": "121036"
```

`],`

```json
  "errorCode": null,
  "errorMsg": null
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |

| OpenTrek Dev Developer Guide·P |   |   |
|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.2.13. PostKortexApiKbDocChunkList**

Document knowledge base chunk detail list query

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| pageIndex | Integer | Body | Yes | 1 | The current page number. This parameter is required. |
| pageSize | Integer | Body | Yes | 10 | The size of each page. This parameter is required. |
| kbCode | String | Body | Yes | h8qp21tb85pf | knowledge base unique encoding. This parameter is required. |
| keyword | String | Body | Yes | 1 | Keyword query. This parameter is required. |
| code | String | Body | Yes | 1 | The unique encoding of the segment. This parameter is required. |
| fileCode | String | Body | Yes | 1c1363763d8a44e1a4bf27b5 16f269c9 | The file encoding. This parameter is required. |

**Response parameters**

| Field | Data types | Description | Examples |
|---|---|---|---|
| success | Boolean | Success | true |

| 120 |   | > Doc | ument Version: 20260901 |
|---|---|---|---|

|   | OpenTrek |   | OpenTr | ek Dev Developer Guide· latform Function Clas | P s |
|---|---|---|---|---|---|

| Field | Data types | Description | Examples |
|---|---|---|---|
| data | object | Return Data | {} |
| total | Integer | The total number of queried lists. | 39 |
| list | List | The list of queried |   |
| file code _ | String | File code | 139ace527fad49d1b60642 d927cf0734 |
| file name _ | String | Document Name | HSBC Hong Kong User's Guide 2022.5 (1).pdf |
| file path _ | String | Document Path | apsara/kortex/kb/doc/file/fr flNcOUgYp21rtbw3vsaXob OlFspojA /HSBC Hong Kong User Guide 2022.5 (1).pdf |
| create user _ | String | Creator | gaochai |
| sys data id _ _ | String | unique data id | 180eeed6-58a1-43da- 980a-21d50e65615e |
| sys create time _ _ | String | Creation time | 2025-07- 11T20:08:40.140449 |
| chunk upload type _ _ | Integer | Upload Type | 1 |
| chunk content _ | String | chunk content-text prompt sent to LLM after recall |   |
| chunk representation _ | String | chunk content-text for vectorization, used in the retrieve phase |   |
| show content _ | String | chunk content-text form with bbox and objects placeholders |   |
| chunk bboxes _ | List | bbox coordinate information |   |
| text bbox _ | List | Coordinates | [ 0.3115, 0.0683, 0.0285, 0.372 ] |
| text type _ | String | Text type | docTitle |
| text content _ | String | Text content | HSBC Hong Kong Account Usage Guide |
| page | Integer | Number of pages | 1 |

| OpenTrek Dev Developer | Guide·P |   | OpenTre |
|---|---|---|---|

| Field | Data types | Description | Examples |
|---|---|---|---|
| objects | List | Object information-tables, pictures, etc. |   |
| start page _ | Integer | The serial number of the chunk. | 1 |
| chunk sort number _ _ | Integer | Page number | 0 |
| title | String | The title of the auxiliary media asset. |   |
| chapter title _ | String | Chapter Title |   |
| pageSize | Integer | The number of entries returned per page. | 60 |
| current | Integer | Current Page | 1 |
| errorCode | String | The error code. | true |
| errorMsg | String | The error message. | true |

`JSON` format

```json
    "success": true,
    "data": {
        "total": 1,
        "list": [
                "file_code": "7a3f64a3f22a4f12b2fe2557d3139595",
                "file_name": "I was on the verge of collapse"_full.pdf",
                "file_path": "kortex/kb/doc/file/kk062kg1t4hd/7 a3f64a3f22a4f12b2fe2557d3139595 /" I wa
s on the verge of crash "_full.pdf",
                "create_user": "gaochai",
                "sys_data_id": "88b3affd-5b56-4819-9ebd-a12e8ce46db1",
                "sys_create_time": "2025-07-22T23:51:58.250412",
                "chunk_upload_type": 1,
                "chunk_content": "I was on the verge of; collapse; Liu Chuanzhi; Xu Xiaoping; Wang Qian
g; Highly recommended; CITIC Publishing Group I was on the verge of collapse -Yu Minhong Telling the R oad of New Oriental's Entrepreneurship and Development Yu Minhong's CITIC Publishing Group",
                "chunk_representation": "I have walked on the verge of collapse; Liu Chuanzhi; Xu Xiaop
ing; Wang Qiang; Dingli recommended; CITIC Publishing Group I have walked on the verge of collapse -Yu Minhong personally narrate the path of entrepreneurship and development of New Oriental written by Yu Minhong CITIC Publishing Group",
                "show_content": "{object_1_figure_0} I was on the verge of collapse -- Yu Minhong's des
cription of the entrepreneurial development of New Oriental CITIC Publishing Group by Yu Minhong",
                "chunk_bboxs": [
                        "text_bbox": [
                            0.2206,
                            0.2898,
                            0.0909,
                            0.5547
```

`],`

```json
                        "text_type": "docTitle",
                        "text_content": "I was on the brink of collapse-Yu Minhong on the of New Orient
al's entrepreneurial development",
                        "page": 2
```

`},`

```json
                        "text_bbox": [
                            0.2819,
                            0.2923,
                            0.0372,
                            0.4387
```

`],`

```json
                        "text_type": "line",
                        "text_content": "I was on the verge of a crash",
                        "page": 2
```

`},`

```json
                        "text_bbox": [
                            0.2247,
                            0.3542,
                            0.0259,
                            0.549
```

`],`

```json
                        "text_type": "line",
                        "text_content": "-- Yu Minhong's road to entrepreneurship and development of Ne
w Oriental",
                        "page": 2
```

`},`

```json
                        "text_bbox": [
                            0.4567,
                            0.404,
                            0.0158,
                            0.0858
```

`],`

```json
                        "text_type": "paraText",
                        "text_content": "By Yu Minhong",
                        "page": 2
```

`},`

```json
                        "text_bbox": [
                            0.4592,
                            0.4059,
                            0.0139,
                            0.0817
```

`],`

```json
                        "text_type": "line",
                        "text_content": "By Yu Minhong",
                        "page": 2
```

`},`

```json
                        "text_bbox": [
                            0.442,
                            0.5114,
                            0.0177,
                            0.1152
```

`],`

```json
                        "text_type": "paraText",
                        "text_content": "CITIC Publishing Group ",
                        "page": 2
```

`},`

```json
                        "text_bbox": [
```

```
                            0.4453,
                            0.5133,
                            0.0152,
                            0.1095
```

`],`

```json
                        "text_type": "line",
                        "text_content": "CITIC Publishing Group",
                        "page": 2
```

`],`

```json
                "objects": [
                        "object_id": "object_1_figure_0",
                        "object_type": "figure",
                        "object_sub_type": "other",
                        "object_content": "I walked on; Collapsing; On the edge; Liu Chuanzhi; Xu Xiaop
ing; Wang Qiang; Highly recommended; CITIC Publishing Group",
                        "object_caption": "",
                        "object_bbox": "[0.0335,0.0019,0.9924,0.9346]",
                        "object_representation": "",
                        "object_path":
"kortex/kb/doc/file/7a3f64a3f22a4f12b2fe2557d3139595/output/chunk/objects/0_0_figure.jpg",
                        "page": 1
```

`],`

```json
                "start_page": 1,
                "chunk_sort_number": 0,
                "title": null,
                "chapter_title": null
```

`],`

```json
        "pageSize": 10,
        "current": 1
```

`},`

```json
    "errorCode": null,
    "errorMsg": null
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |

|   |   | OpenTrek Dev Developer Guide· |
|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.2.14. PostKortexApiKbDocFileReprocess**

Document knowledge base re-parsing

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| kbCode | String | Body | Yes | kk062kg1t4hd | knowledge base unique encoding. This parameter is required. |
| fileCode | String | Body | No | 3fedc04432424c9886b1bbb6 9666b7ed | File encoding |

**Response parameters**

| Field | Data types | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |

| OpenTrek Dev Developer atform Function Class | Guide·P |   | OpenTre |
|---|---|---|---|

| Field | Data types | Description | Sample value |
|---|---|---|---|
| data | object | Return Data | {} |
| updated | Integer | Number of affected | 1 |
| errorCode | String | The error code. | true |
| errorMsg | String | The error message. | true |

```json
 JSON format
    "success": true,
    "data": {
        "updated": 1
```

`},`

```json
    "errorCode": null,
    "errorMsg": null
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |

| OpenTrek |   | OpenTrek Dev Developer Guide· latform Function Clas |
|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.2.15. PostKortexApiKbDocChunkEdit**

Document knowledge base chunk content correction

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| kbCode | String | Body | Yes | cozhklqn3omz | knowledge base unique encoding. This parameter is required. |
| data | Json | Body | Yes | {} | The dataset to be changed. This parameter is required. |
| - chunk conte _ nt | String | Body | No | User purchased a laptop | The content of the chunk. This parameter is required. |
| -sys data id _ _ | String | Body | No | 1234 | The unique ID of the data. The document knowledge base scenario is a segmented code. This parameter is required. |

**Response parameters**

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |
| data | object | Return Data | {} |
| errorCode | String | The error code. | true |
| errorMsg | String | The error message. | true |

```json
 JSON format
    "success": true,
    "data": null,
    "errorCode": null,
    "errorMsg": null
```

**Additional information**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.2.16. PostKortexApiKbSubmodelDataList**

knowledge base data query, such as business data entered by a data model defined in a custom knowledge base scenario

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| kbSubmodel Code | String | Body | Yes | tttbnz21diense89 | knowledge base the data model code. For more information, see knowledge base details. This parameter is required. |
| kbCode | String | Body | Yes | sadfak2s | knowledge base encoding. This parameter is required. |
| current | Integer | Body | Yes | 1 | The number of pages to be paged. This parameter is required. |
| pageSize | Integer | Body | Yes | 10 | The number of pieces per page. This parameter is required. |

**Response parameters**

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |
| data | object | Return data | {} |
| total | Integer | Total number of knowledge base queried | 1 |
| list | List | List of knowledge base queried |   |
| sys data id _ _ | String | Unique data ID; | true |
| sys create time _ _ | String | The creation time. | true |
| sys source ids _ _ | String | Additional data information | true |

| OpenTrek Dev Developer | Guide·P |   | OpenTre |
|---|---|---|---|
| atform Function Class |   |   |   |
| Property | Data structure | Description | Sample value |
| **** | String | Custom data fields; for example, I created a custom knowledge base that defines a 'standard knowledge base, 'which contains two fields, matter code,matter name; _ _ | The value of the custom data field. |
| pageSize | Integer | Size per page | 60 |
| current | Integer | Current Page | 1 |
| errorCode | String | The error code. | true |
| errorMsg | String | The error message. | true |

`JSON` format

```json
    "total": 3,
    "list": [
            "matter_name": "Manhole cover defect 1",
            "sys_source_ids": "{\"kb_submodel\": \"true\", \"kb_submodel.sys_data_id\": \"b724ba0f-
a836-4f5e-88d8-c90dda96e3e6\"}",
            "sys_data_id": "b724ba0f-a836-4f5e-88d8-c90dda96e3e6",
            "matter_code": "CODE0003",
            "sys_create_time": "2025-07-22T15:44:14.592+00:00"
```

`},`

```json
            "matter_name": "Noise nuisance",
            "sys_source_ids": "{\"kb_submodel\": \"true\", \"kb_submodel.sys_data_id\": \"d42ba34b-
553c-4d7f-adc6-ef81ce65255f\"}",
            "sys_data_id": "d42ba34b-553c-4d7f-adc6-ef81ce65255f",
            "matter_code": "CODE0003",
            "sys_create_time": "2025-07-22T15:43:05.304+00:00"
```

`},`

```json
            "matter_name": "Privately built",
            "sys_source_ids": "{\"kb_submodel\": \"true\", \"source_builtin_smod\": \"true\",
\"kb_submodel.sys_data_id\": \"d3a2163b-68de-400f-a2b3-dd312247207d\", \"source_builtin_smod.sys_id\": \"1\"}",
            "sys_data_id": "d3a2163b-68de-400f-a2b3-dd312247207d",
            "matter_code": "CODE0002",
            "sys_create_time": "2025-07-22T15:17:58.050+00:00"
```

`],`

```json
    "pageSize": 10,
    "current": 1
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |

|   | OpenTrek |   | OpenTrek Dev Developer Guide· latform Function Clas | P s |
|---|---|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.2.17. PostKortexApiKbDocFileList**

Document knowledge base File List Query

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| current | Integer | Body | Yes | 1 | The current page number. This parameter is required. |
| pageSize | Integer | Body | Yes | 10 | The size of each page. This parameter is required. |
| kbCode | String | Body | Yes | h8qp21tb85pf | knowledge base unique encoding. This parameter is required. |
| fileCode | String | Body | No | 1866347c49824f62ab061576 b8891806 | File Code |

**Response parameters**

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |
| data | object | Return data | {} |
| total | Integer | Total number of documents queried | 1 |
| list | List | List of documents queried |   |
| kbCode | String | knowledge base code | h8qp21tb85pf |
| fileCode | String | Document code | 1866347c49824f62ab0615 76b8891806 |
| fileOriginalName | String | Original name of document | [Information Attachment] 101330100230176- Vulnerability Authentication.docx |
| filePath | String | Document Path | apsara/kortex/kb/doc/file/a opf27k2rZieth5u7ce8fhTN2 p6j1DRn /[Intelligence Attachment] 101330100230176- Vulnerabily.docx |
| fileType | String | Document Type | docx |
| fileSize | String | Document Size |   |
| fileChecksum | String | fileChecksum |   |
| ownerId | String | owner id | 48381f1dbff84ad89060517 7585ea7ff |

| 132 |   | > Doc | ument Version: 20260901 |
|---|---|---|---|

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| fileOutputChunkPath | String | Path of the chunk parsed from the document | kortex/kb/doc/file/1866347 c49824f62ab061576b8891 806/output/chunk/chunk.js onl |
| state | Integer | Status 103 to be transferred; 102 transfer failed; 0 to be scheduled \| transfer succeeded; 100 in progress; 200 succeeded; 500 failed | 200 |
| uploadType | Integer | Upload Type 1 -Manual Upload, 2 - API Upload | API |
| refRes | String | Associated Resources |   |
| metadata | String | Metadata |   |
| projectCode | String | Workspace encoding | baseline |
| createTime | String | Creation time | 2025-07- 09T19:28:46.289265 |
| createUser | String | Creator | dke |
| pageSize | Integer | The number of entries returned per page. | 60 |
| current | Integer | Current Page | 1 |
| errorCode | String | The error code. | true |
| errorMsg | String | The error message. | true |

```
 JSON format
```

```json
    "success": true,
    "data": {
        "total": 1,
        "list": [
                "kbCode": "kk062kg1t4hd",
                "fileCode": "7a3f64a3f22a4f12b2fe2557d3139595",
                "fileOriginalUrl": "https://ibp-deliver.oss-cn-
hangzhou.aliyuncs.com/%E3%80%8A%E6%88%91%E6%9B%BE%E8%B5%B0%E5%9C%A8%E5%B4%A9%E6%BA%83%E7%9A%84%E8%BE%B9% BC%98%E3%80%8B_full.pdf",
                "fileOriginalName": "I was on the verge of collapse"_full.pdf",
                "filePath": "kortex/kb/doc/file/kk062kg1t4hd/7 a3f64a3f22a4f12b2fe2557d3139595 /" I was
on the verge of crash "_full.pdf",
                "fileType": "pdf",
                "fileSize": null,
                "fileChecksum": null,
                "ownerId": "2b6b6d96279a4c7eaf3357dca86a4844",
                "fileOriginalOutputChunkUrl": null,
                "fileOutputChunkPath": null,
                "state": 100,
                "uploadType": 2,
                "refRes": null,
                "metadata": null,
                "projectCode": "17ac7ce4-23ad-413b-95f4-55732b15a4b7",
                "createTime": "2025-07-22T23:49:44.740747",
                "createUser": "gaochai",
                "updateTime": "2025-07-22T23:49:51.550727",
                "updateUser": null,
                "createUserId": "2b6b6d96279a4c7eaf3357dca86a4844",
                "updateUserId": "2b6b6d96279a4c7eaf3357dca86a4844"
```

`],`

```json
        "pageSize": 10,
        "current": 1
```

`},`

```json
    "errorCode": null,
    "errorMsg": null
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |

| OpenTrek |   | latform Function Clas |
|---|---|---|
| HTTP status return code | Error description | Error interpretation |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.2.18. PostKortexApiKbDisable**

Deactivate knowledge base

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| code | String | Body | Yes | rkiviej5rkm2 | knowledge base unique encoding. This parameter is required. |

**Response parameters**

| Field | Data types | Description | Examples |
|---|---|---|---|
| success | Boolean | Success | true |
| data | object | Return Data | {} |
| kbDisable | Integer | Successful deactivation | 1 |

| OpenTrek Dev Developer atform Function Class | Guide·P |   | OpenTre |
|---|---|---|---|

| Field | Data types | Description | Examples |
|---|---|---|---|
| errorCode | String | The error code. | true |
| errorMsg | String | The error message. | true |

```json
 JSON format
    "success": true,
    "data": {
        "kbDisable": 1
```

`},`

```json
    "errorCode": null,
    "errorMsg": null
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

#### Data Center

Data center-related APIs

**1.2.3.1. Data Management**

**1.2.3.1.1. GetDataEngineApiV2Datasets**

Obtain a list of datasets

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| keyword | String | Query | No. | mmlu | The search keyword. |
| tags | String | Query | No. | 1,2,3 | Dataset tag KeyID |
| pageNumber | Integer | Query | No. | 1 | Page number of the list |
| pageSize | Integer | Query | No. | 10 | The number of entries to return on each page. |
| order | String | Query | No. | DESC | The sort method. Valid values: |
| orderBy | String | Query | No. | createdAt | The field used for sorting. |
| brief | Boolea n | Query | No. | false | Data Set Brief |
| ownerId | String | Query | No. | 123456 | The user ID. |

**Response parameters**

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |

| > Document Version: 202 | 60901 |   | 137 |
|---|---|---|---|

| OpenTrek Dev Developer atform Function Class | Guide·P |   | OpenTre |
|---|---|---|---|

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| data | Object | Response parameters |   |
| datasets | List | The dataset list. |   |
| id | Integer | The ID of the dataset. | 128 |
| code | String | Dataset Code | mmlu no train _ _ |
| name | String | The name of the training dataset. | dataset001 |
| description | String | Dataset description |   |
| parquetFileSize | Integer | The size of the training dataset. | 118019 |
| rowCount | Integer | Number of rows | 36 |
| downloadCount | Integer | The number of times the shared files were downloaded. | 9 |
| tags | List | The tags. |   |
| id | Integer | The tag ID. | 7 |
| name | String | The name of the tag. | Multi-label classification |
| value | String | The tag value. |   |
| ownerId | String | Dataset owner ID | 1631044****3440 |
| ownerName | String | Dataset owner username | admin |
| tenantCode | String | Tenant Code | sfmboost |
| workspaceCode | String | Workgroup Code | default workspace _ |
| createdAt | String | Creation time | 2021-01-30T12:51:33.028Z |
| updatedAt | String | Update time | 2021-01-30T12:51:33.028Z |
| pageSize | Integer | Number of rows per page | 20 |
| totalCount | Integer | Total Quantity | 79 |
| pageNumber | Integer | The page number of the returned page. | 1 |

```json
 JSON format
  "datasets": [
      "id": 128,
      "code": "mmlu_no_train",
      "name": "dataset001",
      "description": "",
      "parquetFilesSize": 118019,
      "rowCount": 36,
      "downloadCount": 9,
      "tags": [
          "id": 7,
          "name": "Multi-label classification",
          "value": ""
```

`},`

```json
          "id": 202,
          "name": "French",
          "value": "French label value"
```

`],`

```json
      "ownerId": "1631044****3440",
      "ownerName": "admin",
      "tenantCode": "sfmboost",
      "workspaceCode": "default_workspace",
      "createdAt": "2021-01-30T12:51:33.028Z",
      "updatedAt": "2021-01-30T12:51:33.028Z"
```

`],`

```json
  "pageSize": 20,
  "totalCount": 79,
  "pageNumber": 1
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |

| l | OpenTrek Dev Developer Guide·P atform Function Class |   | OpenTre | k |
|---|---|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.1.2. PostDataEngineApiV2Datasets**

Create a dataset

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| code | String | Body | Yes | mmlu no train _ _ | The code of the dataset. This parameter is required. |
| name | String | Body | No | Dataset | Dataset Name |
| subset | String | Body | No | default | Subset Name |
| split | String | Body | No | train | Slice Name |
| description | String | Body | No | Test data | Dataset description |
| tags | Repeat List | Body | No | [{"id":1234, "value":"1w- 10w"}] | The tags. |

|   | OpenTrek |   |   |   | OpenT | rek Dev Developer Guide· latform Function Clas | P s |
|---|---|---|---|---|---|---|---|

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| -id | Integer | Body | No | 1234 | The tag ID. |
| -value | String | Body | No | 1w-10w | The tag value. |

**Response parameters**

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| success | Boolean | Success | true |
| data | Object | Return data | { "id": 99, "code": "mmlu no train" } _ _ |
| id | Integer | Dataset ID | 99 |
| code | String | Dataset code | mmlu no train _ _ |

```json
 JSON format
  "success": true,
  "data": {
    "id": 99,
    "code": "mmlu_no_train"
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |

| OpenTrek Dev Developer Guide·P |   | OpenTre |
|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.1.3. PutDataEngineApiV2Datasets**

Update a dataset

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| code | String | Body | Yes | mmlu no train _ _ | The code of the dataset. This parameter is required. |
| name | String | Body | No | Zhang San test data set | Dataset Name |
| description | String | Body | No | testDescription | Dataset description |
| tags | Repeat List | Body | No | [{"id":123, "value":"1w- 10w"}] | Tag list |
| -id | Integer | Body | No | 123 | The tag ID. |
| -value | String | Body | No | 1w-10w | The tag value. |

**Response parameters**

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |
| data | Boolean | Response parameters | true |

```json
 JSON format
  "success": true,
  "data": true
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.1.4. DeleteDataEngineApiV2DatasetsCode**

Delete a dataset

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| code | String | Path | Yes | mmlu no train _ _ | The code of the dataset. This parameter is required. |

**Response parameters**

| Field | Data types | Description | Examples |
|---|---|---|---|
| success | Boolean | Success | true |
| data | Boolean | Response parameters | true |

```json
 JSON format
  "success": true,
  "data": true
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |

| OpenTrek |   | OpenTrek Dev Developer Guide· |
|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.1.5. GetDataEngineApiV2DatasetsCode**

Obtain the details of a dataset.

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| code | String | Path | Yes | mmlu no train _ _ | Dataset Code |

**Response parameters**

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |
| data | Object | Response parameters |   |

| > Document Version: 202 | 60901 |   | 145 |
|---|---|---|---|

| OpenTrek Dev Developer atform Function Class | Guide·P |   | OpenTre |
|---|---|---|---|

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| code | String | Dataset Code | mmlu no train _ _ |
| name | String | The name of the training dataset. | Sword 3 test data set |
| description | String | Dataset description |   |
| originalFileSize | Integer | The size of the original resource file. Unit: bytes. | 118019 |
| parquetFileSize | Integer | The size of the dataset. Unit: bytes. | 118019 |
| rowCount | Integer | Number of rows | 36 |
| downloadCount | Integer | The number of times the shared files were downloaded. | 9 |
| tags | List | The tags. |   |
| id | Integer | The tag ID. | 123 |
| name | String | The name of the tag. | size scale _ |
| value | String | The tag value. | lw-10w |
| subsets | List | Subset List |   |
| code | String | Subset Code | default |
| name | String | Subset Name | default |
| parquetFileSize | Integer | The size of the subset data. Unit: bytes. | 0 |
| rowCount | Integer | Number of rows of subset data | 19 |
| features | List | The columns. |   |
| columnName | String | The name of the field. | idx __ |

| 146 |   | > Doc | ument Version: 20260901 |
|---|---|---|---|

| OpenTrek |   | OpenTr | ek Dev Developer Guide· latform Function Clas |
|---|---|---|---|

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| columnType | String | Field Type | string |
| columnPhysicalType | String | Field Physical Type | varchar |
| columnComment | String | Field description | Unique data item identifier |
| splits | List | Slice list |   |
| code | String | Slice Code | train |
| subset | String | Subset | default |
| name | String | Slice Name | train |
| parquetFileSize | Integer | The size of the slice data. Unit: bytes. | 0 |
| rowCount | Integer | Number of rows of sliced data | 19 |
| dataFiles | List | Data file list | ["cat.jpg", "dog.jpg", "cet.jpg"] |
| producer | String | Data sources: KN DATASET, _ KN PROCESS, KN LABEL, _ _ and UNKNOWN | KN DATASET _ |
| ownerId | String | Dataset owner ID | 1631044****3440 |
| ownerName | String | Dataset owner username | admin |
| tenantCode | String | Tenant Code | sfmboost |
| workspaceCode | String | Workgroup Code | default workspace _ |
| createdAt | String | Creation time | 2021-01-30T12:51:33.028Z |
| updatedAt | String | Update time | 2021-01-30T12:51:33.028Z |
| repoPath | String | Dataset Warehouse Address | sfm/dataset/baseline/mmlu no train/main _ _ |
| parquetPath | String | Dataset parquet address | sfm/dataset/baseline/mmlu no train/parquet _ _ |
| summaryModified | String | The time when the dataset summary was last modified. | 2021-01-30T12:51:33.028Z |

`JSON` format

```json
  "code": "mmlu_no_train",
  "name": "Zhang San test dataset",
  "description": "",
  "parquetFilesSize": 118019,
  "rowCount": 36,
  "downloadCount": 9,
  "tags": [
      "id": 123,
      "name": "size_scale",
      "value": "1w-10w"
```

`],`

```json
  "subsets": [
      "code": "default",
      "name": "default",
      "parquetFilesSize": 0,
      "rowCount": 19,
      "features": [
          "columnName": "__idx",
          "columnType": "string",
          "columnPhysicalType": "varchar",
          "columnComment": ""
```

`},`

```json
          "columnName": "__content",
          "columnType": "string",
          "columnPhysicalType": "varchar",
          "columnComment": ""
```

`],`

```json
      "splits": [
          "code": "train",
          "subset": "default",
          "name": "train",
          "parquetFilesSize": 0,
          "rowCount": 19
```

`]` `],`

```json
  "ownerId": "1631044****3440",
  "ownerName": "admin",
  "tenantCode": "sfmboost",
  "workspaceCode": "default_workspace",
  "createdAt": "2021-01-30T12:51:33.028Z",
  "updatedAt": "2021-01-30T12:51:33.028Z",
  "repoPath": "sfm/dataset/baseline/mmlu_no_train/main",
  "parquetPath": "sfm/dataset/baseline/mmlu_no_train/parquet"
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |

|   | OpenTrek |   | OpenTrek Dev Developer Guide· latform Function Clas | P s |
|---|---|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.1.6. PostDataEngineApiV2DatasetsCodeFiles**

Notify Dataset File Add

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| code | String | Path | Yes | mmlu no train _ _ | Dataset Code |
| filePaths | Repeat List | Body | Yes | ["pdfs/1902.10909v1.pdf","R ay -Distributed Computing Framework Architecture Design Details v2.pdf","pdfs/2406.02543v1. pdf"] | The list of file paths. This parameter is required. |
| relative | Boolea n | Body | Yes | true | Whether the path is a relative path. This parameter is required. |

**Response parameters**

| Field | Data types | Description | Examples |
|---|---|---|---|
| success | Boolean | Success | true |
| data | Object | Return data |   |
| id | String | Task ID | 510FF634FCE407EEA1763 854519FD3CE |
| completed | Boolean | Whether to complete | true |
| createTime | String | Creation time | 2024-10-08T11:53:23.000Z |
| status | String | Task status: Success, Fail, Cancel | Success |
| response | Object | Task response data | {} |
| error | String | Error message |   |
| progress | Integer | Execution progress | 100 |

`JSON` format

```json
  "success": true,
  "data": {
    "id": "510FF634FCE407EEA1763854519FD3CE",
    "completed": true,
    "createTime": "2024-10-08T11:53:23.000Z",
    "status": "Success",
    "response": {},
    "error": "",
    "progress": 100
```

**Additional information**

| HTTP status return code | The error message. | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |

|   | OpenTrek |   | OpenTrek Dev Developer Guide· latform Function Clas | P s |
|---|---|---|---|---|

| HTTP status return code | The error message. | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.1.7. DeleteDataEngineApiV2DatasetsCodeFiles**

Notify Dataset File Deletion

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| code | String | Path | Yes | mmlu no train _ _ | Dataset Code |
| filePaths | Repeat List | Body | Yes | ["pdfs/1902.10909v1.pdf", "Ray -Distributed Computing Framework Architecture Design Details v2.pdf", "pdfs/2406.02543v1.pdf"] | An array of relative file paths. This parameter is required. |
| relative | Boolea n | Body | Yes | true | Whether the path is a relative path. This parameter is required. |

**Response parameters**

| Field | Data types | Description | Examples |
|---|---|---|---|
| success | Boolean | Success | true |
| data | Object | Return data |   |
| id | String | Task ID | 510FF634FCE407EEA1763 854519FD3CE |
| completed | Boolean | Whether the execution is complete | true |
| createTime | String | Task creation time | 2024-10-08T11:53:23.000Z |
| status | String | Task Status | Success |
| response | Object | Resource information generated by the task | {} |
| error | String | Error message |   |
| progress | Integer | Execution progress | 100 |

`JSON` format

```json
  "success": true,
  "data": {
    "id": "510FF634FCE407EEA1763854519FD3CE",
    "completed": true,
    "createTime": "2024-10-08T11:53:23.000Z",
    "status": "Success",
    "response": {},
    "error": "",
    "progress": 100
```

**Additional information**

| HTTP status return code | The error message. | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |

|   | OpenTrek |   | OpenTrek Dev Developer Guide· latform Function Clas | P s |
|---|---|---|---|---|

| HTTP status return code | The error message. | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.1.8. GetDataEngineApiV2DatasetsCodeFiles**

Query the list of dataset files by page

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| code | String | Path | Yes | COCO 2017 _ | Dataset Code |
| filePath | String | Body | No | val | File path |
| relative | Boolea n | Body | No | true | Whether it is a relative path |
| pageNumber | Integer | Body | No | 1 | Page number |
| pageSize | Integer | Body | No | 10 | The number of entries returned per page. |

**Response parameters**

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| success | Boolean | Success | true |
| data | Object | Return data |   |
| datasetFileInfos | List | File information list |   |
| name | String | File name | 000000000139.jpg |
| filepath | String | File Path | sfm/dataset/baseline/opent rek/COCO 2017/main/val/0 _ 00000000139.jpg |
| suffix | String | File Name Extensions | jpg |
| size | Integer | The size of the file. | 161811 |
| lastModified | Integer | Last Modified Timestamp | 1737106513 |
| pageSize | Integer | The number of entries per page. | 10 |
| totalCount | Integer | The total number of records. | 5000 |
| pageNumber | Integer | Current Page Number | 1 |

`JSON` format

```json
  "success": true,
  "data": {
    "datasetFileInfos": [
        "name": "000000000139.jpg",
        "filepath": "sfm/dataset/baseline/opentrek/COCO_2017/main/val/000000000139.jpg",
        "suffix": "jpg",
        "size": 161811,
        "lastModified": 1737106513
```

`},`

```json
        "name": "000000000285.jpg",
        "filepath": "sfm/dataset/baseline/opentrek/COCO_2017/main/val/000000000285.jpg",
        "suffix": "jpg",
        "size": 335861,
        "lastModified": 1737106513
```

`],`

```json
    "pageSize": 10,
    "totalCount": 5000,
    "pageNumber": 1
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |

| OpenTrek Dev Developer Guide·P atform Function Class |   | OpenTre |
|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.1.9. PostDataEngineApiV2DatasetsCodeSubsets**

New Data Subset

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The target workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| code | String | Path | Yes | mmlu no train _ _ | Dataset Code |
| subset | String | Body | Yes | default | The data subset code. This parameter is required. |
| dataFiles | Repeat List | Body | Yes | ["pdfs/1902.10909v1.pdf"] | The list of associated data files. This parameter is required. |
| autoUpdate | Boolea n | Body | Yes | false | Whether to automatically update the view. This parameter is required. |

**Response parameters**

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |
| data | Object | Response parameters |   |
| id | Integer | Subset ID | 278 |
| code | String | Subset Code | new yaml test _ _ |
| createdAt | String | Creation time | 2025-03-06T11:41:33.271Z |

| 156 |   | > Doc | ument Version: 20260901 |
|---|---|---|---|

|   |   | OpenTr | ek Dev Developer Guide· |
|---|---|---|---|
| OpenTrek |   |   | latform Function Clas |

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| updatedAt | String | Update time | 2025-03-06T11:41:33.271Z |
| workspaceCode | String | Workgroup Code | opentrek |
| tenantCode | String | Tenant Code | baseline |
| name | String | Subset Name | Subset configuration test |
| description | String | Subset Description | Subset configuration test |
| originalFileSize | Integer | Original file size | 0 |
| parquetFileSize | Integer | Data View Size | 0 |
| rowCount | Integer | Number of rows | 0 |
| downloadCount | Integer | The number of times the shared files were downloaded. | 0 |
| ownerId | String | Owner ID | 20240813 |
| ownerName | String | The name of the owner. | admin |
| tags | List | The tags. | [] |

`JSON` format

```json
  "success": true,
  "data": {
    "id": 278,
    "code": "new_yaml_test",
    "createdAt": "2025-03-06T11:41:33.271Z",
    "updatedAt": "2025-03-06T11:41:33.271Z",
    "workspaceCode": "opentrek",
    "tenantCode": "baseline",
    "name": "Subset configuration test",
    "description": "Subset configuration test",
    "originalFilesSize": 0,
    "parquetFilesSize": 0,
    "rowCount": 0,
    "downloadCount": 0,
    "ownerId": "20240813",
    "ownerName": "admin",
    "tags": []
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.1.10. PutDataEngineApiV2DatasetsCodeSubsets**

Update a subset of data

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| code | String | Path | Yes | mmlu no train _ _ | Dataset Code |
| subset | String | Body | Yes | default | The data subset code. This parameter is required. |
| dataFiles | Repeat List | Body | Yes | ["pdfs/*.pdf"] | The list of associated data files. This parameter is required. |
| autoUpdate | Boolea n | Body | Yes | true | Whether to automatically update the view. This parameter is required. |

**Response parameters**

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |
| data | Object | Response parameters |   |
| id | Integer | The ID of the dataset. | 278 |
| code | String | Dataset Code | new yaml test _ _ |
| createdAt | String | Creation time | 2025-03-06T11:41:33.271Z |
| updatedAt | String | Update time | 2025-03-06T11:41:33.271Z |
| workspaceCode | String | Workgroup Code | opentrek |
| tenantCode | String | Tenant Code | baseline |
| name | String | Dataset Name | Subset configuration test |
| description | String | Dataset description | Subset configuration test |
| originalFileSize | Integer | Original resource file size | 0 |
| parquetFileSize | Integer | Data Set Size | 0 |
| rowCount | Integer | Number of rows | 0 |
| downloadCount | Integer | The number of times the shared files were downloaded. | 0 |
| ownerId | String | Owner ID | 20240813 |
| ownerName | String | Owner user name | admin |
| tags | List | The tags. | [] |

`JSON` format

```json
  "success": true,
  "data": {
    "id": 278,
    "code": "new_yaml_test",
    "createdAt": "2025-03-06T11:41:33.271Z",
    "updatedAt": "2025-03-06T11:41:33.271Z",
    "workspaceCode": "opentrek",
    "tenantCode": "baseline",
    "name": "Subset configuration test",
    "description": "Subset configuration test",
    "originalFilesSize": 0,
    "parquetFilesSize": 0,
    "rowCount": 0,
    "downloadCount": 0,
    "ownerId": "20240813",
    "ownerName": "admin",
    "tags": []
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |

|   | OpenTrek |   | OpenTrek Dev Developer Guide· latform Function Clas | P s |
|---|---|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.1.11.**

**DeleteDataEngineApiV2DatasetsCodeSubsetsSubsetcode**

Delete a subset of a dataset

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| code | String | Path | Yes | mmlu no train _ _ | Dataset Code |
| subsetCode | String | Path | Yes | mmlu no train _ _ | Data Subset Code |

**Response parameters**

| Field | Data types | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |
| data | Boolean | Response parameters | true |

```json
 JSON format
  "success": true,
  "data": true
```

**Additional information**

| HTTP status return code | The error message. | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.1.12. GetDataEngineApiV2DatasetsCodeSubsets**

Dataset subset list

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| code | String | Path | Yes | mmlu no train _ _ | Dataset Code |
| built | Boolea n | Query | No | true | Whether to get only the subset that has been built |
| subsets | Repeat List | Query | No. | ["default"] | Subset List |

**Response parameters**

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |
| data | Object | Response parameters |   |
| subsets | List | Subset List |   |
| code | String | Subset Code | image subset _ |
| name | String | Subset Name | image subset _ |
| parquetFileSize | Integer | The size of the subset data. Unit: bytes. | 275025 |
| rowCount | Integer | Number of rows of subset data | 5000 |
| features | List | The columns. |   |
| columnName | String | The name of the field. | idx __ |
| columnType | String | Field Type | string |
| columnPhysicalType | String | Field Physical Type | varchar |
| columnComment | String | Field description |   |

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| splits | List | Slice list |   |
| code | String | Slice Code | train |
| subset | String | Subset | image subset _ |
| name | String | Slice Name | train |
| parquetFileSize | Integer | The size of the slice data. Unit: bytes. | 275025 |
| rowCount | Integer | Number of rows of sliced data | 5000 |
| sourceFiles | List | Source file list | ["sfm/dataset/baseline/ope ntrek/COCO 2017/main/**/ _ *.jpg"] |
| lastModified | Integer | The time when the A/B test group was last updated. | 1737107658 |
| pageSize | Integer | The number of entries per page. | 2 |
| totalCount | Integer | The total number of records. | 2 |
| pageNumber | Integer | The page number of the returned page. | 1 |

```json
 JSON format
  "success": true,
  "data": {
    "subsets": [
        "code": "image_subset",
        "name": "image_subset",
        "parquetFilesSize": 275025,
        "rowCount": 5000,
        "features": [
            "columnName": "__idx",
            "columnType": "string",
            "columnPhysicalType": "varchar",
            "columnComment": ""
```

`},`

```json
            "columnName": "image",
            "columnType": "Image",
            "columnPhysicalType": "struct(bytes blob, path varchar)",
            "columnComment": ""
```

`],` `"` `li` `"` `[`

```json
        "splits": [
            "code": "train",
            "subset": "image_subset",
            "name": "train",
            "parquetFilesSize": 275025,
            "rowCount": 5000,
            "sourceFiles": [
              "sfm/dataset/baseline/opentrek/COCO_2017/main/**/*.jpg"
```

`]` `],`

```json
        "lastModified": 1737107658
```

`},`

```json
        "code": "image_subset_annotation_dd52841...9d1e7925c5",
        "name": "image_subset_annotation_dd52841...9d1e7925c5",
        "parquetFilesSize": 8898,
        "rowCount": 14,
        "features": [
            "columnName": "image",
            "columnType": "Image",
            "columnPhysicalType": "struct(bytes blob, path varchar)",
            "columnComment": ""
```

`},`

```json
            "columnName": "label",
            "columnType": "string",
            "columnPhysicalType": "varchar",
            "columnComment": ""
```

`],`

```json
        "splits": [
            "code": "train",
            "subset": "image_subset_annotation_dd52841...9d1e7925c5",
            "name": "train",
            "parquetFilesSize": 8898,
            "rowCount": 14,
            "sourceFiles": [
"sfm/dataset/baseline/opentrek/COCO_2017/parquet/image_subset_annotation_dd528417ad82405f835e969d1e7925c rain/0000.parquet"
```

`]` `],`

```json
        "lastModified": 1737107659
```

`],`

```json
    "pageSize": 2,
    "totalCount": 2,
    "pageNumber": 1
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |

| OpenTrek Dev Developer Guide·P atform Function Class |   | OpenTre |
|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.1.13.**

**GetDataEngineApiV2DatasetsCodeSubsetsSearch**

Search for a subset of a dataset

**Request header**

This interface uses common request headers without special request headers. See the public request parameters documentation.

**Parameters**

| Paramete r Name | Type | Locatio n | Required | Example | Limit |
|---|---|---|---|---|---|
| code | String | Path | Yes | mmlu no train _ _ | Dataset Code |

**Response parameters**

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| code | String | Subset Code | image subset _ |

| 166 |   | > Doc | ument Version: 20260901 |
|---|---|---|---|

|   |   |   | latform Function Clas |
|---|---|---|---|

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| name | String | Subset Name | image subset _ |
| parquetFilesSize | Integer | The size of the subset data. Unit: bytes. | 275025 |
| rowCount | Integer | Number of rows of subset data | 5000 |
| features | List | The columns. |   |
| columnName | String | The name of the field. | idx __ |
| columnType | String | Field data type | string |
| columnPhysicalType | String | Field Physical Type | varchar |
| columnComment | String | Field Description |   |
| splits | List | Slice list |   |
| code | String | Slice Code | train |
| subset | String | Subset | image subset _ |
| name | String | Slice Name | train |
| parquetFilesSize | Integer | The size of the slice data. Unit: bytes. | 275025 |
| rowCount | Integer | Number of rows of sliced data | 5000 |
| sourceFiles | List | Source file list | ["sfm/dataset/baseline/ope ntrek/COCO 2017/main/**/ _ * .jpg"] |
| lastModified | Integer | Last modification time | 1737107658 |

`JSON` format

```json
        "code": "image_subset",
        "name": "image_subset",
        "parquetFilesSize": 275025,
        "rowCount": 5000,
        "features": [
            "columnName": "__idx",
            "columnType": "string",
            "columnPhysicalType": "varchar",
            "columnComment": ""
```

`},`

```json
            "columnName": "image",
            "columnType": "Image",
            "columnPhysicalType": "struct(bytes blob, path varchar)",
            "columnComment": ""
```

`],`

```json
        "splits": [
            "code": "train",
            "subset": "image_subset",
            "name": "train",
            "parquetFilesSize": 275025,
            "rowCount": 5000,
            "sourceFiles": [
              "sfm/dataset/baseline/opentrek/COCO_2017/main/**/*.jpg"
```

`]` `],`

```json
        "lastModified": 1737107658
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |

|   | OpenTrek |   | OpenTrek Dev Developer Guide· latform Function Clas | P s |
|---|---|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.1.14. GetDataEngineApiV2DatasetsCodeViewer**

Obtain dataset preview data

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| code | String | Path | Yes | mmlu no train _ _ | Dataset Code |
| subset | String | Query | No. | default | Subset Code |
| split | String | Query | No. | train | Slice Code |
| pageNumber | Integer | Query | No. | 1 | Page number of the list |
| pageSize | Integer | Query | No. | 10 | The number of entries returned per page. |

**Response parameters**

| Property | Data structure | Description | Sample value |
|---|---|---|---|

| > Document Version: 202 | 60901 |   | 169 |
|---|---|---|---|

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |
| data | Object | Response parameters |   |
| schema | List | The information about the column. |   |
| columnName | String | Field Name | pdf url _ |
| columnType | String | Field Type | string |
| columnPhysicalType | String | Field Physical Type | varchar |
| data | List | Data content | [["oss://xxx/tenant/dataset/ xxx/tmp/xxx.pdf", {"path": "tmp/xxx.pdf", "bytes": null}, 19849], ...] |
| status | String | View construction status: BUILDING, BUILD FAILED, _ BUILT | BUILD FAILED _ |
| message | String | Error message | ... |
| pageSize | Integer | The number of entries to return on each page. | 100 |
| totalCount | Integer | Total Rows | 12389 |
| pageNumber | Integer | The page number of the returned page. | 1 |

```
 JSON format
```

```json
  "success": true,
  "data": {
    "schema": [
        "columnName": "pdf_url",
        "columnType": "string",
        "columnPhysicalType": "varchar"
```

`},`

```json
        "columnName": "file",
        "columnType": "Doc",
        "columnPhysicalType": "struct(bytes blob, path varchar)"
```

`},`

```json
        "columnName": "size",
        "columnType": "int64",
        "columnPhysicalType": "int64"
```

`],`

```json
    "data": [
```

`[`

```json
        "oss://xxx/tenant/dataset/xxx/tmp/xxx.pdf",
          "path": "tmp/xxx.pdf",
          "bytes": null
```

`},`

```
        19849
```

`]` `],`

```json
    "status": "BUILD_FAILED",
    "message": "...",
    "pageSize": 100,
    "totalCount": 12389,
    "pageNumber": 1
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |

| OpenTrek Dev Developer Guide·P |   | OpenTre |
|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.1.15. GetDataEngineApiV2FilesImagePresignedUrl**

Obtain the image URL

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| datasetCode | String | Query | Yes | mmlu | Dataset Code |
| filePath | String | Query | Yes | train /turtle tan. jpeg | File relative path |
| width | Integer | Query | No. | 100 | Specify image width |
| height | Integer | Query | No. | 100 | Specify image height |

**Response parameters**

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |
| data | Object | Return data |   |
| url | String | Image URL | https://oss-cn- hangzhou.aliyuncs.com/.../ %E4%B9%8C%E9%BE%9F %E9%BE%9F%E6%BD%AD .jpeg?Signature=xxx |
| expiration | Integer | Validity Period (Seconds) | 3600 |
| expireTime | String | Expiration time | 2024-10-08T11:53:23.000Z |

`JSON` format

```json
  "success": true,
  "data": {
    "url": "https://oss-cn-hangzhou.aliyuncs.com/../%E4%B9%8C%E9%BE%9F%E6%BD%AD.jpeg?Signature=xxx",
    "expiration": 3600,
    "expireTime": "2024-10-08T11:53:23.000Z"
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |

| OpenTrek Dev Developer Guide·P atform Function Class |   | OpenTre |
|---|---|---|
| HTTP status return code | Error description | Error interpretation |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.1.16. GetDataEngineApiV2FilesPresignedUrl**

Obtain the file download address

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| datasetCode | String | Query | Yes | mmlu | Dataset Code |
| filePath | String | Query | Yes | pdfs/1902.10909v1.pdf | File relative path |
| useShortUrl | Boolea n | Query | No | false | Whether to return short address Default value: false |

**Response parameters**

| Field | Data types | Description | Examples |
|---|---|---|---|
| success | Boolean | Success | true |
| data | Object | Return data |   |
| url | String | Pre-signed download address | https://oss-cn- hangzhou.aliyuncs.com/.../ 1902.10909v1.pdf? Signature=xxx |
| expiration | Integer | Validity Period (Seconds) | 3600 |
| expireTime | String | Expiration time | 2024-10-08T11:53:23.000Z |

`JSON` format

```json
  "success": true,
  "data": {
    "url": "https://oss-cn-hangzhou.aliyuncs.com/../1902.10909v1.pdf?Signature=xxx",
    "expiration": 3600,
    "expireTime": "2024-10-08T11:53:23.000Z"
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.1.17. DeleteDataEngineApiV2Files**

Delete files in a dataset at a time

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| datasetCode | String | Query | Yes | mmlu | Dataset Code |
| filePaths | Repeat List | Query | Yes | ["train /turtle tan. jpeg"] | File path list |
| relative | Boolea n | Query | No | true | Whether to use a relative path |

**Response parameters**

| Field | Data types | Description | Examples |
|---|---|---|---|
| success | Boolean | Success | true |
| data | Object | Return data | { "cnt": 1, "deletedFiles": ["train /Wuguitan. jpeg"] } |
| cnt | Integer | Number of deleted files | 1 |
| deletedFiles | List | Deleted File List | ["train /Wuguitan. jpeg"] |

`JSON` format

```json
  "success": true,
  "data": {
    "cnt": 1,
    "deletedFiles": ["train /turtle tan. jpeg"]
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |

| OpenTrek |   | OpenTrek Dev Developer Guide· |
|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.1.18. GetDataEngineApiV2FilesUploadCredential**

Obtain the file upload authorization credential

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| datasetCode | String | Query | Yes | mmlu | Dataset Code |

**Response parameters**

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |
| data | Object | Response parameters |   |
| type | String | The storage type. | oss |
| endpoint | String | Access Endpoint | https://oss-cn- hangzhou.aliyuncs.com |
| internalEndpoint | String | Internal access address | xxx |
| externalEndpoint | String | External access address | xxx |
| bucket | String | Bucket name | kn-tenant-xxx |
| region | String | Area | xxx |
| accessKeyId | String | Access key ID | xxx |
| accessKeySecret | String | accessKey pair | xxx |
| stsToken | String | STS Token | xxx |
| expiration | Integer | Validity Period (Seconds) | 3600 |
| expireTime | String | Expiration time | 2024-10-08T11:53:23.000Z |

`JSON` format

```json
  "success": true,
  "data": {
    "type": "oss",
    "endpoint": "https://oss-cn-hangzhou.aliyuncs.com",
  "internalEndpoint": "xxx",
    "externalEndpoint": "xxx",
   "bucket": "kn-tenant-xxx",
    "region": "xxx",
    "accessKeyId": "xxx",
    "accessKeySecret": "xxx",
    "stsToken": "xxx",
    "expiration": 3600,
    "expireTime": "2024-10-08T11:53:23.000Z"
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |

| OpenTrek |   | latform Function Clas |
|---|---|---|
| HTTP status return code | Error description | Error interpretation |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.1.19. GetDataEngineApiV2FilesDownloadCredential**

Obtain the file download authorization credential

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| datasetCode | String | Query | Yes | mmlu | Dataset Code |

**Response parameters**

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |
| data | Object | Response parameters |   |
| type | String | The storage type. | oss |
| endpoint | String | Access Endpoint | https://oss-cn- hangzhou.aliyuncs.com |
| internalEndpoint | String | Internal access address | xxx |
| externalEndpoint | String | External access address | xxx |
| bucket | String | Bucket name | kn-tenant-xxx |
| region | String | Area | xxx |
| accessKeyId | String | Access key ID | xxx |
| accessKeySecret | String | accessKey pair | xxx |
| stsToken | String | Security Token | xxx |
| expiration | Integer | Validity Period (Seconds) | 3600 |
| expireTime | String | Expiration time | 2024-10-08T11:53:23.000Z |

`JSON` format

```json
  "success": true,
  "data": {
    "type": "oss",
    "endpoint": "https://oss-cn-hangzhou.aliyuncs.com",
  "internalEndpoint": "xxx",
    "externalEndpoint": "xxx",
    "bucket": "kn-tenant-xxx",
    "region": "xxx",
    "accessKeyId": "xxx",
    "accessKeySecret": "xxx",
    "stsToken": "xxx",
    "expiration": 3600,
    "expireTime": "2024-10-08T11:53:23.000Z"
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.2. Data Processing**

**1.2.3.2.1. GetDataEngineApiV2ProcessTasksTaskid**

Obtains the details of a processing task.

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| taskId | Integer | Path | Yes | 123 | The task ID. |

**Response parameters**

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| id | Integer | The task ID. | 123 |
| name | String | Task Name | Customize Mengniu text cleaning tasks |
| description | String | Task Description | Clean clean Mengniu task |
| editState | String | Task editing status | draft |
| type | String | Task Type | pipeline |
| dkeJobId | Integer | DKE job ID | 231 |
| tplId | Integer | Template ID | 12 |
| tplName | String | The template name. | Data Cleansing |
| tplCode | String | Message Template Code | text clean _ |
| tplVersion | String | Template Version | v1.0.0 |
| operatorIds | List | Use the operator ID list | [12, 13, 14] |
| operators | List | Operator Details | [] |
| config | Object | Task Configuration | {} |
| creatorId | String | Creator ID | 1631044****3440 |
| creatorName | String | Creator user name | admin |

| 182 |   | > Doc | ument Version: 20260901 |
|---|---|---|---|

| OpenTrek |   | OpenTr | ek Dev Developer Guide· latform Function Clas |
|---|---|---|---|

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| tenantCode | String | Tenant Code | sfmboost |
| workspaceCode | String | Workgroup Code | default workspace _ |
| createdAt | String | Creation time | 2021-01-30T12:51:33.028Z |
| updatedAt | String | Update time | 2021-01-30T12:51:33.028Z |

`JSON` format

```json
  "id": 123,
  "name": "Custom Mengniu text cleansing task",
  "description": "Clean Mengniu",
  "editState": "draft",
  "type": "pipeline",
  "dkeJobId": 231,
  "tplId": 12,
  "tplName": "Data cleansing",
  "tplCode": "text_clean",
  "tplVersion": "v1.0.0",
  "operatorIds": [12, 13, 14],
  "operators": [],
  "config": {},
  "creatorId": "1631044****3440",
  "creatorName": "admin",
  "tenantCode": "sfmboost",
  "workspaceCode": "default_workspace",
  "createdAt": "2021-01-30T12:51:33.028Z",
  "updatedAt": "2021-01-30T12:51:33.028Z"
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |

| OpenTrek Dev Developer Guide·P |   |   |
|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.2.2. GetDataEngineApiV2ProcessTemplates**

Obtains the list of processing templates.

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| keyword | String | Query | No. | Data Cleansing | The search keyword. |
| type | String | Query | No. | pipeline | The template type. |
| pageNumber | Integer | Query | No. | 1 | Page number of the list |
| pageSize | Integer | Query | No. | 10 | The number of entries to return on each page. |

**Response parameters**

| Field | Data types | Description | Examples |
|---|---|---|---|

| Field | Data types | Description | Examples |
|---|---|---|---|
| templates | List | List of templates | [{"id": 128, "code": "text clean", "name": "data _ cleansing", "description": "data cleansing", "type": "pipeline", "icon": "", "tags": ["text", "LLM"], "version": "v1.0.0", "ownerId": "1631044****3440", "ownerName": "admin", "tenantCode": "sfmboost", "workspaceCode": "default workspace", _ "createdAt": "2021-01- 30T12:51:33.028Z", "updatedAt": "2021-01- 30T12:51:33.028Z"}] |
| id | Integer | Template ID | 128 |
| code | String | Message Template Code | text clean _ |
| name | String | The template name. | Data Cleansing |
| description | String | Template Description | Clean data |
| type | String | Template type | pipeline |
| icon | String | Template icon |   |
| tags | List | Template Tags | ["text", "LLM"] |
| version | String | Template Version | v1.0.0 |
| ownerId | String | The ID of the template owner. | 1631044****3440 |
| ownerName | String | Template owner username | admin |
| tenantCode | String | Tenant Code | sfmboost |
| workspaceCode | String | Workgroup Code | default workspace _ |
| createdAt | String | Creation time | 2021-01-30T12:51:33.028Z |
| updatedAt | String | Update time | 2021-01-30T12:51:33.028Z |
| pageSize | Integer | Number of rows per page | 20 |
| totalCount | Integer | Total Quantity | 79 |
| pageNumber | Integer | The page number of the returned page. | 1 |

```
 JSON format
```

```json
  "templates": [
      "id": 128,
      "code": "text_clean",
      "name": "Data cleansing",
      "description": "Clean data",
      "type": "pipeline",
      "icon": "",
      "tags": ["text", "LLM"],
      "version": "v1.0.0",
      "ownerId": "1631044****3440",
      "ownerName": "admin",
      "tenantCode": "sfmboost",
      "workspaceCode": "default_workspace",
      "createdAt": "2021-01-30T12:51:33.028Z",
      "updatedAt": "2021-01-30T12:51:33.028Z"
```

`],`

```json
  "pageSize": 20,
  "totalCount": 79,
  "pageNumber": 1
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |

| OpenTrek |   | OpenTrek Dev Developer Guide· latform Function Clas |
|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.2.3. PostDataEngineApiV2ProcessTasks**

Create a processing task

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| name | String | Body | Yes | Custom cleaning tasks | The name of the task. This parameter is required. |
| description | String | Body | No | Custom cleaning tasks | Task Description |
| type | String | Body | Yes | pipeline | The type of the task. This parameter is required. |
| tplId | Integer | Body | Yes | 12 | The ID of the template. This parameter is required. |
| tplName | String | Body | Yes | Data cleansing | The name of the template. This parameter is required. |
| tplCode | String | Body | Yes | text clean _ | The code of the template. This parameter is required. |
| tplVersion | String | Body | Yes | v1.0.0 | The version of the template. This parameter is required. |
| config | Json | Body | Yes | {} | The task configuration. This parameter is required. |

| OpenTrek Dev | Develop | er Guide·P |   |   |   |
|---|---|---|---|---|---|

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| - datasetImpo rt | String | Body | No | sfm://dataset code/subset _ | The input dataset. This parameter is required. |
| - datasetExpo rt | String | Body | No | sfm://dataset code/subset _ | The output dataset. This parameter is required. |
| -np | Integer | Body | No | 1 | Calculate the parallelism |
| -process | Repeat List | Body | No | [{"word parser offline mapp _ _ _ er": {"image ocr": false, _ "save file": false, _ "deep parse": true, _ "table parse": false, _ "equation parse": false, _ "image filter size": [3,3]}}, _ _ {"parser format offline map _ _ _ per": {"persistent": true, "input feature key": _ _ "word parser", _ "input feature type": _ _ "word parser"}}] _ | pipeline configuration, operator execution list |

**Response parameters**

| Field | Data types | Description | Sample value |
|---|---|---|---|
| id | Integer | The task ID. | 123 |

```json
 JSON format
  "id": 123
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |

| OpenTrek |   | OpenTrek Dev Developer Guide· latform Function Clas |
|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.2.4. DeleteDataEngineApiV2ProcessTasksTaskid**

Delete a processing task

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| taskId | Integer | Path | Yes | 123 | The task ID. |

**Response parameters**

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |

`JSON` format

```json
{"success": true}
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.2.5. GetDataEngineApiV2ProcessTasks**

Obtains the list of processing tasks.

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| keyword | String | Query | No. | mmlu | The search keyword. |
| editState | String | Query | No. | draft | Task editing status |
| type | String | Query | No. | pipeline | Task Type |
| pageNumber | Integer | Query | No. | 1 | Page number of the list |
| pageSize | Integer | Query | No. | 10 | The number of entries to return on each page. |
| order | String | Query | No. | DESC | The sort method. Valid values: |
| orderBy | String | Query | No. | createdAt | The field used for sorting. |

**Response parameters**

| Property | Data structure | Description | Examples |
|---|---|---|---|
| tasks | List | Task List | [{"id": 123, "name": "custom cleansing task", "description": "custom cleansing task", "editState": "draft", "type": "pipeline", "dkeJobId": 231, "tplId": 12, "tplName": "data cleansing", "tplCode v1.", " text clean "" _ creatorId": "1631044****3440", "creatorName": "admin", "tenantCode": "sfmboost", "workspaceCode": "default workspace", _ "createdAt": "2021-01- 30T12:51:33.028Z", "updatedAt": "2021-01- 30T12:51 "}: 2851 |
| id | Integer | Task ID | 123 |
| name | String | Task name | Custom cleaning tasks |
| description | String | Task Description | Custom cleaning tasks |
| editState | String | Task editing status | draft |
| type | String | Task Type | pipeline |
| dkeJobId | Integer | DKE job ID | 231 |
| tplId | Integer | Template ID | 12 |
| tplName | String | The template name. | Data Cleansing |
| tplCode | String | Template Code | text clean _ |

| > Document Version: 202 | 60901 |   | 191 |
|---|---|---|---|

| OpenTrek Dev Developer | Guide·P |   |   |
|---|---|---|---|
| atform Function Class |   |   | OpenTre |

| Property | Data structure | Description | Examples |
|---|---|---|---|
| tplVersion | String | template version | v1.0.0 |
| creatorId | String | The ID of the user who assigned the role. | 1631044****3440 |
| creatorName | String | Creator user name | admin |
| tenantCode | String | Tenant Code | sfmboost |
| workspaceCode | String | Workgroup Code | default workspace _ |
| createdAt | String | Creation time | 2021-01-30T12:51:33.028Z |
| updatedAt | String | Update time | 2021-01-30T12:51:33.028Z |
| pageSize | Integer | The number of entries to return on each page. | 20 |
| totalCount | Integer | The total number of entries returned. | 79 |
| pageNumber | Integer | Current Page Number | 1 |

`JSON` format

```json
  "tasks": [
      "id": 123,
      "name": "Custom cleansing task",
      "description": "Custom cleansing task",
      "editState": "draft",
      "type": "pipeline",
      "dkeJobId": 231,
      "tplId": 12,
      "tplName": "Data cleansing",
      "tplCode": "text_clean",
      "tplVersion": "v1.0.0",
      "creatorId": "1631044****3440",
      "creatorName": "admin",
      "tenantCode": "sfmboost",
      "workspaceCode": "default_workspace",
      "createdAt": "2021-01-30T12:51:33.028Z",
      "updatedAt": "2021-01-30T12:51:33.028Z"
```

`],`

```json
  "pageSize": 20,
  "totalCount": 79,
  "pageNumber": 1
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |

| OpenTrek |   | OpenTrek Dev Developer Guide· latform Function Clas |
|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.2.6. GetDataEngineApiV2Operators**

Obtains the operator list.

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| keyword | String | Query | No. | text | The search keyword. |
| type | String | Query | No. | Mapper | Operator |

**Response parameters**

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| operators | List | Operator list |   |
| id | Integer | Operator ID | 1203 |
| name | String | Operator Name | Text Enhancement |
| code | String | Operator Code | opentrek text enhanceme _ _ nt mapper _ |
| description | String | Operator Description | Used to enhance text |
| type | String | Operator | Mapper |
| modalities | List | Supported data types | ["text"] |
| devices | List | Supported device types | ["CPU", "GPU"] |
| tags | List | Label | ["LLM"] |
| updateFeatures | List | Operator change field | [{"columnName": "problem", "columnType": "string", "columnPhysicalType": "varchar", "columnComment": "User Question"}, {"columnName": "param:solution", "columnType": "string", "columnPhysicalType": "varchar", "columnComment"] Answer "}: |
| columnName | String | Field Name | problem |
| columnType | String | Field Type | String |
| columnPhysicalType | String | Field Physical Type | varchar |
| columnComment | String | Field description | Enter a question. |

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| params | List | The parameters. | [{"type": "literal", "required": true, "key": "model", "defaultValue": "qwen-max", "desc": "Model to use for data generation.", "options": ["qwen-max", "qwen-vl"]}] |
| type | String | Parameter type | literal |
| required | Boolean | Required | true |
| key | String | Parameter Key | model |
| defaultValue | String | The default value of the property. | qwen-max |
| desc | String | The parameter description. | Model to use for data generation. |
| options | List | Optional value | ["qwen-max", "qwen-vl"] |
| components | List | Front-end component configuration | [{"type": "Select", "required": true, "label": "model name", "key": "model", "desc": "simple description of the current form item", "defaultValue": "qwen-max", "options": [{"label": "general questions", "value": "qwen- max", ...}]}] |
| type | String | Component types | Select |
| required | Boolean | Required | true |
| label | String | Component label | Model name |
| key | String | Parameter Key | model |
| desc | String | Component description | A brief description of the current form item |
| defaultValue | String | Default Value | qwen-max |
| options | List | List of options | [{"label": "thousands of questions of general meaning", "value": "qwen- max", "desc": "thousands of questions of general meaning is a large model specially responding to human instructions..."}] |
| label | String | Option Label | Qwen |
| value | String | Option | qwen-max |
| desc | String | Description | Tongyi Thousand Questions is a large model that specifically responds to human instructions, and is a flexible and versatile player... |

| > Document Version: 202 | 60901 |   | 195 |
|---|---|---|---|

| OpenTrek Dev Developer atform Function Class | Guide·P |   | OpenTre |
|---|---|---|---|

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| extra | Object | Extended configuration | {"min": 0, "max": 10, "step": 1, "mode": "multiple"} |
| min | Integer | Minimum | 0 |
| max | Integer | Maximum | 10 |
| step | Integer | Step size for purchase (GB) | 1 |
| mode | String | mode | multiple |
| pageSize | Integer | The number of entries to return on each page. | 20 |
| totalCount | Integer | The total number of entries returned. | 79 |
| pageNumber | Integer | The page number of the returned page. | 1 |

`JSON` format

```json
  "operators": [
      "id": 1203,
      "name": "Text enhancement",
      "code": "opentrek_text_enhancement_mapper",
      "description": "Used to enhance text",
      "type": "Mapper",
      "modalities": ["text"],
      "devices": ["CPU", "GPU"],
      "tags": ["LLM"],
      "updateFeatures": [
          "columnName": "problem",
          "columnType": "string",
          "columnPhysicalType": "varchar",
          "columnComment": "User question"
```

`},`

```json
          "columnName": "param:solution",
          "columnType": "string",
          "columnPhysicalType": "varchar",
          "columnComment": "LLM answer"
```

`],`

```json
      "params": [
          "type": "literal",
          "required": true,
          "key": "model",
          "defaultValue": "qwen-max",
          "desc": "Model to use for data generation.",
          "options": ["qwen-max", "qwen-vl"]
```

`],`

```json
      "components": [
          "type": "Select",
```

```json
          "required": true,
          "label": "Model name",
          "key": "model",
          "desc": "A brief description of the current form item",
          "defaultValue": "qwen-max",
          "options": [
              "label": "Tongyi Qiwen",
              "value": "qwen-max",
              "desc": "Tongyi Qianwen is a large model that specially responds to human instructions. I
t is a flexible and versatile player who can write emails, weekly newspapers, outlines, poems, novels, plays, coding, tabulation and even role-playing. "
```

`},`

```json
              "label": "VL",
              "value": "qwen-vl",
              "desc": "qwen-vl VL is a large-scale visual language model developed by Alibaba Cloud. It
can use images, text, and check boxes as input and use text and check boxes as output. It supports Chi nese multi-modal dialogues and multi-image dialogues. "
```

`],`

```json
          "extra": {
            "min": 0,
            "max": 10,
            "step": 1,
            "mode": "multiple"
```

`]` `],`

```json
  "pageSize": 20,
  "totalCount": 79,
  "pageNumber": 1
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |

| OpenTrek Dev Developer Guide·P |   | OpenTre |
|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.2.7.**

**GetDataEngineApiV2ProcessTasksTaskidInstances**

Obtain the information of a task running instance.

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| taskId | Integer | Path | Yes | 100 | The task ID. |
| runId | Integer | Query | Yes | 1001 | Task Run ID |

**Response parameters**

| Property | Data structure | Description | Examples |
|---|---|---|---|

| Property | Data structure | Description | Examples |
|---|---|---|---|
| data | List | Returned data list | [{"id":667,"tenantCode":"b aseline","flowId":555,"taskI d":556,"taskCode":"job 25 _ 204e0c233c11f0aac656db 6f3d4393","taskName":" [To be verified] text-data parsing-CHUNK splitting"...}] |
| id | Integer | Instance ID | 667 |
| tenantCode | String | Tenant Code | baseline |
| flowId | Integer | Process ID | 555 |
| taskId | Integer | Task ID | 556 |
| taskCode | String | Task Code | job 25204e0c233c11f0aac _ 656db6f3d4393 |
| taskName | String | Task Name | [To be verified] text-data parsing-CHUNK splitting |
| instanceCode | String | Instance Code | 556.250427.15:50.W6hwd Gl7j.250427 |
| instanceType | Integer | Instance type | 2 |
| duration | String | Execution duration | 3s |
| taskVersion | String | Task Version | 1745740172030 |
| execType | String | Execution Type | KN PROC _ |
| parents | Object | Parent instance | null |
| children | Object | Secondary Instance | null |
| status | Integer | Instance status (1: pending execution, 2: executing, 3: successful, 4: failed, 5: timeout, 6: queuing, 7: exception) | 4 |
| substatus | Integer | Sub-state | -1 |
| retry | Integer | Number of retries | 0 |
| revision | Integer | The revision version. | 0 |
| bizdate | String | Data Timestamp | 2025-04-26 15:50:00 |
| plandate | String | Planned Date | 2025-04-27 15:50:00 |
| execdate | String | Execution Date | null |
| gmtCreate | String | The creation time. | 2025-04-27 15:50:42 |
| gmtStart | String | Start Time | 2025-04-27 15:50:43 |
| gmtEnd | String | End Time | 2025-04-27 15:50:46 |
| gmtHeartbeat | String | The heartbeat time of the ECU. | 2025-04-27 15:50:48 |
| createdBy | String | The creator. | qingfu.zmq |

| > Document Version: 202 | 60901 |   | 199 |
|---|---|---|---|

| OpenTrek Dev Developer | Guide·P |   | OpenTre |
|---|---|---|---|
| atform Function Class |   |   |   |

| Property | Data structure | Description | Examples |
|---|---|---|---|
| rerun | Boolean | Rerun | false |
| retryStrategy | Object | Retry Policy | null |
| priority | Integer | Priority | 10 |
| importDataset | Object | Import a dataset | null |
| exportDataset | Object | Export a dataset | null |
| pageSize | Integer | The number of entries on this page. | 20 |
| totalCount | Integer | The total number of records. | 79 |
| pageNumber | Integer | The page number of the returned page. | 1 |

```json
 JSON format
  "success": true,
  "data": [
      "id": 667,
      "tenantCode": "baseline",
      "flowId": 555,
      "taskId": 556,
      "taskCode": "job_25204e0c233c11f0aac656db6f3d4393",
      "taskName": "[To be verified] text-data parsing-CHUNK splitting",
      "instanceCode": "556.250427.15:50.W6hwdGl7j.250427",
      "instanceType": 2,
      "duration": "3s",
      "taskVersion": "1745740172030",
      "execType": "KN_PROC",
      "parents": null,
      "children": null,
      "status": 4,
      "substatus": -1,
      "retry": 0,
      "revision": 0,
      "bizdate": "2025-04-26 15:50:00",
      "plandate": "2025-04-27 15:50:00",
      "execdate": null,
      "gmtCreate": "2025-04-27 15:50:42",
      "gmtStart": "2025-04-27 15:50:43",
      "gmtEnd": "2025-04-27 15:50:46",
      "gmtHeartbeat": "2025-04-27 15:50:48",
      "createdBy": "qingfu.zmq",
      "rerun": false,
      "retryStrategy": null,
      "priority": 10,
      "importDataset": null,
      "exportDataset": null
```

`]`

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.2.8. PostDataEngineApiV2ProcessTasksTaskidRun**

Run processing tasks

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| xlmGroupCo de | String | Body | Yes | xxxx | The code of the resource pool. This parameter is required. |
| specs | Json | Body | Yes | {"name": "CPU", "data": {"vCPU": 1, "Mem": "1GB"}} | The specification configuration. This parameter is required. |
| -vCPU | Integer | Body | No | 1 | The number of vCPUs. This parameter is required. |
| -Mem | String | Body | No | 1GB | The memory size. This parameter is required. |
| -np | Integer | Body | No | 1 | The degree of parallelism. This parameter is required. |
| -GPU | Json | Body | No | {"NVIDIA-A100-SXM80GB": 1} | The GPU specification. This parameter is required. |

**Response parameters**

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |
| data | Object | Response parameters |   |
| id | Integer | Task Run ID | 2357 |

```json
 JSON format
  "success": true,
  "data": {"id": 2357}
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |

|   |   | OpenTrek Dev Developer Guide· |
|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.2.9. PostDataEngineApiV2ProcessTasksTaskidPublish**

Publish a task

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| taskId | Integer | Path | Yes | 123 | The task ID. |

**Response parameters**

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |

`JSON` format

```json
{"success": true}
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.2.10.**

**PostDataEngineApiV2ProcessTasksTaskidUnpublish**

To undownload a task

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| taskId | Integer | Path | Yes | 123 | The task ID. |

**Response parameters**

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |

`JSON` format

```json
{"success": true}
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |

| OpenTrek Dev Developer Guide·P atform Function Class |   | OpenTre |
|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.2.11. GetDataEngineApiV2ProcessTemplatesCode**

Obtain the details of a processing template.

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| code | String | Path | Yes | mmlu no train _ _ | Message Template Code |

**Response parameters**

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| id | Integer | Template ID | 128 |
| code | String | Message Template Code | text clean _ |
| name | String | The template name. | Data Cleansing |
| description | String | Template Description | Data Cleansing |
| type | String | The template type. | pipeline |
| icon | String | Template icon |   |
| tags | List | Template Tags | ["text", "LLM"] |

| 206 |   | > Doc | ument Version: 20260901 |
|---|---|---|---|

|   |   | OpenTr | ek Dev Developer Guide· |
|---|---|---|---|
| OpenTrek |   |   | latform Function Clas |

| Property | Data structure | Description | Sample value |
|---|---|---|---|
| version | String | Template Version | v1.0.0 |
| operators | List | Operator list | [{}] |
| config | Object | Template configuration | {} |
| ownerId | String | The ID of the template owner. | 1631044****3440 |
| ownerName | String | Template owner username | admin |
| tenantCode | String | Tenant Code | sfmboost |
| workspaceCode | String | Workgroup Code | default workspace _ |
| createdAt | String | Creation time | 2021-01-30T12:51:33.028Z |
| updatedAt | String | Update time | 2021-01-30T12:51:33.028Z |

`JSON` format

```json
  "id": 128,
  "code": "text_clean",
  "name": "Data cleansing",
  "description": "Data cleansing",
  "type": "pipeline",
  "icon": "",
  "tags": ["text", "LLM"],
  "version": "v1.0.0",
  "operators": [{}],
  "config": {},
  "ownerId": "1631044****3440",
  "ownerName": "admin",
  "tenantCode": "sfmboost",
  "workspaceCode": "default_workspace",
  "createdAt": "2021-01-30T12:51:33.028Z",
  "updatedAt": "2021-01-30T12:51:33.028Z"
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |

| OpenTrek Dev Developer Guide·P |   | OpenTre |
|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.2.12. PutDataEngineApiV2ProcessTasks**

Updating a machining task

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| id | Integer | Body | Yes | 123 | The ID of the task. This parameter is required. |

| OpenTrek |   |   |   | OpenT | rek Dev Developer Guide· latform Function Clas |
|---|---|---|---|---|---|

| Paramete r Name | Type | Positio n | Required | Example | Limit |
|---|---|---|---|---|---|
| name | String | Body | Yes | Custom cleaning tasks | The name of the task. This parameter is required. |
| description | String | Body | No | Custom cleaning tasks | Task Description |
| type | String | Body | Yes | pipeline | The type of the task. This parameter is required. |
| tplId | Integer | Body | Yes | 12 | The ID of the template. This parameter is required. |
| tplName | String | Body | Yes | Data cleansing | The name of the template. This parameter is required. |
| tplCode | String | Body | Yes | text clean _ | The code of the template. This parameter is required. |
| tplVersion | String | Body | Yes | v1.0.0 | The version of the template. This parameter is required. |
| config | Json | Body | Yes | {} | The task configuration. This parameter is required. |
| - datasetImpo rt | String | Body | No | sfm://dataset code/subset _ | The input dataset. This parameter is required. |
| - datasetExpo rt | String | Body | No | sfm://dataset code/subset _ | The output dataset. This parameter is required. |
| -np | Integer | Body | No | 1 | Calculate the parallelism |
| -process | Repeat List | Body | No | [{"word parser offline mapp _ _ _ er": {"image ocr": false, _ "save file": false, _ "deep parse": true, _ "table parse": false, _ "equation parse": false, _ "image filter size": [3,3]}}, _ _ {"parser format offline map _ _ _ per": {"persistent": true, "input feature key": _ _ "word parser", _ "input feature type": _ _ "word parser"}}] _ | pipeline configuration, operator execution list |

**Response parameters**

| Field | Data types | Description | Examples |
|---|---|---|---|
| success | Boolean | Indicates whether the request was successful. | true |

`JSON` format

```
{success: true}
```

**Additional information**

| HTTP status return code | The error message. | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

**1.2.3.2.13.**

**GetDataEngineApiV2ProcessTasksInstancesInstancecodeLog**

Obtain task instance logs

**Request header**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- authorizatio n | String | Header | No | Bearer YOUR APP KEY _ _ | APP KEY _ |

|   |   |   |   | OpenT | rek Dev Developer Guide· |
|---|---|---|---|---|---|

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| x-sfm- workspaceco de | String | Header | Yes | your workspace code _ _ | The destination workspace. This parameter is required. |
| Content- Type | String | Header | Yes | application/json | Content-Type. This parameter is required. |

**Parameters**

| Paramete r Name | Type | Locatio n | Required | Examples | Description |
|---|---|---|---|---|---|
| instanceCod e | String | Path | Yes | 1460.250701.17:34.JMR7CCD 57.250701 | Task instance code |

**Response parameters**

| Field | Data types | Description | Examples |
|---|---|---|---|
| log | String | Task instance logs | 2025-07-01 17:59:52.301073 +0800 CST -------------------------------- -- 2025-07-01 18:05:30.643637 +0800 CST |

`JSON` format

```json
{"log": "2025-07-01 17:59:52.301073 +0800 CST------------2025-07-01 18:05:30.643637 +0800 CST"}
```

**Documentation Supplement**

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required parameters of the gateway are missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed, invalid APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | Authentication failed. APP KEY has _ expired. |
| 401 | GATEWAY ROLE NOT MATCH! | The authentication failed because the role corresponding to the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role corresponding to the current APP KEY _ user has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service call path |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service call path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggers throttling. Please try again later. |

| OpenTrek Dev Developer Guide·P |   |   |
|---|---|---|

| HTTP status return code | Error description | Error interpretation |
|---|---|---|
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggers throttling. Please try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | The required parameters for the business are missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace encoding does not match the workspace encoding associated with the APP KEY home _ user |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. Unsupported authentication method |
| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | Authentication failed, user role does not match |

Application integration APIs

## Application integration APIs

These APIs provide services for platform tenants.

### User guide

#### Obtain an API key

Open APIs use API keys for authentication. This mechanism controls access to the API. Before making an API call, you must provide a valid key to verify your identity and gain access to the API. This topic describes how to obtain an API key for the Application Center API.

**Important**

You can obtain API keys for the Application Center API directly from the large language model (LLM) platform. To obtain API keys for the Knowledge Center API, contact the administrator of the corresponding module.

**Procedure**

1. Log in to OpenTrek Agent Dev.
2. In the left-side navigation pane, select **Integration & Open Platform > APP_KEY**.
3.
4. Fill in the required information.
5.
6. On the **Obtain the key** page, click
to copy the key, and then click **OK** to close the window. The system displays the generated API key name in the key list.

**Important**

Store this key in a secure and accessible place. For security reasons, the system displays the key only once. After closing this window, you cannot view it again. Copy and save it timely. If you lose this key, you must repeat the preceding steps to generate a new key.
7. On the **API-Keys** page, click **OK**.

### API documentation

#### Agent

**2.2.1.1. Create a session**

**API overview**

This API creates a new agent session. To test the API call, view the request example and click the debug button next to the cURL command example.

**Prerequisites**

Go to Homepage > Profile Picture > APP_KEY to create an APP_KEY. Then, go to the agent page to complete the agent configuration. Obtain the agent code and version code, or configure an output version.

**API endpoint**

Application integration APIs POST http://ibp-studio-daily.aegmp.com/gateway/agent/api/createSession

**Request parameters**

Header parameters

| Field | Data type | Required | Description | Example |
|---|---|---|---|---|
| Authorization | String | Yes | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | Yes | Content-Type | application/json |

Body parameters

| Field | Data type | Required | Description | Example |
|---|---|---|---|---|
| agentCode | string | Yes | Agent code | e36a0ab1-b673- 49d0-9534- 1480a147c691 |
| agentVersion | string | No | Agent version | 1706863858334 |

**Response parameters**

| Field | Data type | Description | Example |
|---|---|---|---|
| success | boolean | Indicates whether the request was successful. | true |
| data | object | The returned data. | {"uniqueCode":"4bcaa882- 9c54-4b78-9057- 54db58591b5b"} |

**Request example**

```json
curl -X 'POST' http://ibp-studio-daily.aegmp.com/gateway/agent/api/createSession \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -d '{
    "agentCode": "",
    "agentVersion": ""
```

`}'`

**Response example**

```json
 "success": true,
 "data": {
  "uniqueCode": "4bcaa882-9c54-4b78-9057-54db58591b5b"
```

`},`

```json
 "errorCode": null,
 "errorMsg": null
```

**Status codes**

Gateway error status codes Application integration APIs

| HTTP status code | Error description | Fault description |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | A required gateway parameter is missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed. The APP KEY is _ invalid. |
| 401 | GATEWAY APP KEY ALREADY EXPIRE _ D! | Authentication failed. The APP KEY _ has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | The service invocation path is invalid. |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The service invocation path is not registered. |
| 429 | GATEWAY LIMIT ! | The service has triggered rate limiting. Try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSI NG! | A required service parameter is missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The provided workspace code does not match the workspace code associated with the user's APP KEY. _ |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. The authentication method is not supported. |
| 401 | GATEWAY AUTH USER NOT MATCH W _ RONG! | Authentication failed. The user information does not match. |
| 401 | GATEWAY AUTH USER ROLE WRONG _ _ ! | Authentication failed. The user role does not match. |
| 404 | GATEWAY ROUTE URL NOT FOUND! | The target service endpoint is invalid. |
| 401 | GATEWAY LIMIT ! | The maximum number of service connections has been reached. Try again later. |
| 500 | TARGET SERVICE ERROR CONNECTI _ _ _ ON REFUSE EXCEPTION _ _ | The target service refused the connection. |
| 500 | TARGET SERVICE ERROR NO RESPO _ _ _ _ NSE EXCEPTION _ | The target service did not respond. |

**2.2.1.2. Invoke an agent**

**API overview**

Application integration APIs This API lets you ask questions to an agent within an existing session. You can view the request example and click the test button next to the cURL command example to verify the API call.

**Prerequisites**

Go to the menu and choose Homepage > Profile Picture > APP_KEY to create an APP_KEY. Then, call the 'Create session' API to obtain the `uniqueCode` return value.

**Endpoint**

POST http://ibp-studio-daily.aegmp.com/gateway/agent/api/run

**Request parameters**

Header parameters

| Field | Data type | Required | Description | Example |
|---|---|---|---|---|
| Authorization | String | Yes | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | Yes | Content-Type | application/json |

Body parameters

| Field | Data type | Required | Description | Example |
|---|---|---|---|---|
| sessionId | String | Yes | sessionId | bd962db7-b1c8- 4466-a2cc- 41b9b67cd94b. The `uniqueCode` returned by the 'Create session' API. |
| stream | Boolean | Yes | Specifies whether to use streaming output. | true |
| delta | Boolean | Yes | Specifies whether to disable appending new text when stream is set to true. | Default: true. If true, each output contains only new content, not previously sent text. |
| trace | Boolean | No | If true, returns trace records. | Default: false. Trace records are not returned. |
| message | object | Yes | The request message body. | {"text":"Book a flight ticket for me from Shanghai to Zurich for tomorrow.","metadat a":{}, "attachments": [{"url":"","name":""} ]} |

Application integration APIs

| text | string | Yes | The conversation input. | Book a flight ticket for me from Shanghai to Zurich for tomorrow. |
|---|---|---|---|---|
| metadata | Map | No | Extended information. | {} |
| attachments | List<Object> | No | Attachment information. | [] |
| url | string | Yes | The URL of the attachment. | {} |
| name | string | No | The name of the attachment. | {} |

**Response parameters**

| Field | Data type | Description | Example |
|---|---|---|---|
| object | string | The data type. | message.delta: An output text block. thought.delta: A thought process block. error: An error message. |
| role | string | The role. | assistant |
| content | object | The data content. | If `object` is `message.delta`: {"type":"text","text": {"value":"Incremental agent response"}} If `object` is `thought.delta`: {"type":"text","data":"Incre mental thought process"} If `object` is `error`: {"errorMsg": "Error message content"} |
| metadata | object | Extended fields. | {"key":"value"} |
| end | Boolean | In a streaming scenario where `object` is `message.delta`, this marks whether the text output is complete. | false\|true |
| sessionId | string | The current session ID. | - |
| requestId | string | The ID of the current request. | - |

Application integration APIs

| id | object | The unique business ID for the streaming message. | The unique ID for the thought content or the final answer. Multiple thought content blocks can be output before the Q&A session ends. In multi-stream scenarios, you can use custom ID prefixes to differentiate the streams for rendering. |
|---|---|---|---|
| success | Boolean | Non-streaming: Indicates whether the business operation was successful. | true |
| data | object | Non-streaming: The business response. | {} |
| message | object | Non-streaming: The text output response. | {} |
| role | string | The role. | assistant |
| metadata | object | Extended fields. | {"key":"value"} |
| content | List<Object> | The output content. | Contains `type` and `content`. |
| type | String | The type of the output content. | text\|image |
| text | JSONObject | The output structure for the scenario where `type` is `text`. | {} |
| value | String | The output text. | Hello! How can I help you? |
| image | JSONObject | The output structure for the scenario where `type` is `image`. | {} |
| url | String | The URL of the output image. |   |
| thoughts | object | Non-streaming: The thought process response. | {} |
| role | string | The role. | assistant |
| content | object | The output content. |   |
| data | String | The output text. |   |

Application integration APIs

| type | String | The type of the output content. Currently, this is the constant `text`. | text |
|---|---|---|---|
| errorCode | Boolean | Non-streaming: The business error code. | true |
| errorMsg | Boolean | Non-streaming: The business error description. | true |

**Request example**

```json
curl -X 'POST' http://ibp-studio-daily.aegmp.com/gateway/agent/api/run \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -d '{
    "stream":true,
    "delta":true,
    "sessionId": "7af650e7-ed57-498d-8081-fe1dea5361fa",
    "message":{
        "text":"Book a flight ticket for me from Shanghai to Zurich for tomorrow.",
        "metadata":{},
        "attachments":[]
```

`}'`

**Response examples**

**Streaming output**

Application integration APIs

```json
data: {"object": "message.delta","end":false,"role": "assistant","sessionId":"de454297-c547-440f-ae55- 057a83a2d121","content": [{"type":"text","text": {"value": "Incremental agent response"}}],"metadata": {"key": "value"}} data: {"object": "thought.delta","role": "assistant","sessionId":"de454297-c547-440f-ae55- 057a83a2d121","content": {"type":"text","data":"Incremental thought process"}} data: {"object": "error","role": "assistant","sessionId":"de454297-c547-440f-ae55- 057a83a2d121","content": {"errorMsg": "Error message content"}} data:{"content": {"data":"Hello","type":"text"},"id":"323ef0f2f57e445fbec343f62441c608","object":"thought.delta"} data:{"content": {"data":"!","type":"text"},"id":"323ef0f2f57e445fbec343f62441c608","object":"thought.delta"} data:{"content":{"data":"May I ask ","type":"text"},"id":"323ef0f2f57e445fbec343f62441c608","object":"thought.delta"} data:{"content":{"data":"how I can help you?","type":"text"},"id":"323ef0f2f57e445fbec343f62441c608","object":"thought.delta"} data:{"content": {"data":"","type":"text"},"id":"323ef0f2f57e445fbec343f62441c608","object":"thought.delta"} data:{"content":[{"text":{"value":"Hello"},"type":"text"}],"end":false,"gmtCreate":"2024-09-19 11:52:5 6.012","id":"9b0a21677f4a4512935c0e96977f292b","metadata":{},"requestId":"6d511a54-d95f-419c-9d34-02e8 6ea050e4","role":"assistant","sessionId":"7af650e7-ed57-498d-8081-fe1dea5361fa","useage": {"uiTaskId":"23ce3bf3-5248-4293-8326-bdb7f452a092"},"object":"message.delta"} data:{"content":[{"text":{"value":"!"},"type":"text"}],"end":false,"gmtCreate":"2024-09-19 11:52:56.012","id":"9b0a21677f4a4512935c0e96977f292b","metadata":{},"requestId":"6d511a54-d95f-419c-9d 34-02e86ea050e4","role":"assistant","sessionId":"7af650e7-ed57-498d-8081-fe1dea5361fa","useage":{"uiTa skId":"23ce3bf3-5248-4293-8326-bdb7f452a092"},"object":"message.delta"} data:{"content":[{"text":{"value":"May I ask "},"type":"text"}],"end":false,"gmtCreate":"2024-09-19 11 :52:56.012","id":"9b0a21677f4a4512935c0e96977f292b","metadata":{},"requestId":"6d511a54-d95f-419c-9d34 -02e86ea050e4","role":"assistant","sessionId":"7af650e7-ed57-498d-8081-fe1dea5361fa","useage": {"uiTaskId":"23ce3bf3-5248-4293-8326-bdb7f452a092"},"object":"message.delta"} data:{"content":[{"text":{"value":"how I can help you?"},"type":"text"}],"end":false,"gmtCreate":"2024-09-19 11:52:56.012","id":"9b0a21677f4a4512935c0e96977f292b","metadata":{},"requestId":"6d511a54-d95f-419c-9d 34-02e86ea050e4","role":"assistant","sessionId":"7af650e7-ed57-498d-8081-fe1dea5361fa","useage":{"uiTa skId":"23ce3bf3-5248-4293-8326-bdb7f452a092"},"object":"message.delta"} data:{"content":[{"text":{"value":""},"type":"text"}],"end":true,"gmtCreate":"2024-09-19 11:52:56.012","id":"9b0a21677f4a4512935c0e96977f292b","metadata":{},"requestId":"6d511a54-d95f-419c-9d 34-02e86ea050e4","role":"assistant","sessionId":"7af650e7-ed57-498d-8081-fe1dea5361fa","useage":{"uiTa skId":"23ce3bf3-5248-4293-8326-bdb7f452a092"},"object":"message.delta"}
```

**Sample response**

**Non-streaming output**

Application integration APIs

```json
 "success": true,
 "data": {
  "message": {
   "role": "assistant",
   "content": [{
    "type": "text",
    "text": {
     "value": "Hello! How can I help you?"
   },{
    "type": "image",
    "image": {
     "url": ""
   }],
   "metadata": null
```

`},`

```json
  "thoughts": [{
    "role": "assistant",
    "content": {
     "type": "text",
     "data": ""
```

`],`

```json
  "error": null
```

`},`

```json
 "errorCode": null,
 "errorMsg": null
```

**Status codes**

Gateway exception status codes

| HTTP status code | Error description | Error meaning |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | A required gateway parameter is missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed. The APP KEY is _ invalid. |
| 401 | GATEWAY APP KEY ALREADY EXPIRE _ D! | Authentication failed. The APP KEY _ has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | The service invocation path is invalid. |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The service invocation path is not registered. |
| 429 | GATEWAY LIMIT ! | The service has triggered rate limiting. Try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSI NG! | A required business parameter is missing. |

Application integration APIs

| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The provided workspace code does not match the workspace code associated with the APP KEY owner. _ |
|---|---|---|
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. The authentication method is not supported. |
| 401 | GATEWAY AUTH USER NOT MATCH W _ RONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE WRONG _ _ ! | Authentication failed. The user role does not match. |
| 404 | GATEWAY ROUTE URL NOT FOUND! | The target service endpoint is invalid. |
| 401 | GATEWAY LIMIT ! | The maximum number of service connections has been reached. Try again later. |
| 500 | TARGET SERVICE ERROR CONNECTI _ _ _ ON REFUSE EXCEPTION _ _ | The target service denied the connection. |
| 500 | TARGET SERVICE ERROR NO RESPO _ _ _ _ NSE EXCEPTION _ | The target service did not respond. |

**2.2.1.3. Stop a session**

**API overview**

You can call this API to stop a session. To test the API call, review the request example and click the debug button next to the cURL command example.

**Prerequisites (View APP_KEY)**

Go to Homepage > Profile Picture > APP_KEY to create an APP_KEY. Then, call the 'Create a session' API to obtain the `uniqueCode` return value.

**API endpoint**

POST http://ibp-studio-daily.aegmp.com/gateway/agent/api/clearSession

**Request parameters**

Header parameters

| Field | Data type | Required | Description | Example |
|---|---|---|---|---|
| Authorization | String | Yes | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | Yes | Content-Type | application/json |

Body parameters

| Field | Data type | Required | Description | Example |
|---|---|---|---|---|

Application integration APIs

| sessionId | string | Yes | Session ID | de454297-c547- 440f-ae55- 057a83a2d121 The `uniqueCode` that is returned when you call the 'Create a session' API. |
|---|---|---|---|---|

**Response parameters**

| Field | Data type | Description | Example |
|---|---|---|---|
| success | boolean | Indicates whether the call was successful. | true |

**Request example**

```json
curl -X 'POST' http://ibp-studio-daily.aegmp.com/gateway/agent/api/clearSession \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -d '{
    "sessionId": "de454297-c547-440f-ae55-057a83a2d121"
```

`}'`

**Response example**

```json
  "success": true
```

**Status codes**

Gateway error status codes

| HTTP status code | Error description | Fault description |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | A required gateway parameter is missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed. The APP KEY is _ invalid. |
| 401 | GATEWAY APP KEY ALREADY EXPIRE _ D! | Authentication failed. The APP KEY _ has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | The service invocation path is invalid. |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The service invocation path is not registered. |
| 429 | GATEWAY LIMIT ! | The service has triggered rate limiting. Try again later. |

Application integration APIs

| 403 | GATEWAY HEADER PARAMETER MISSI NG! | A required business parameter is missing. |
|---|---|---|
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The provided workspace encoding does not match the workspace encoding associated with the APP KEY owner. _ |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. The authentication method is not supported. |
| 401 | GATEWAY AUTH USER NOT MATCH W _ RONG! | Authentication failed. The Access Key (AK) user information does not match. |
| 401 | GATEWAY AUTH USER ROLE WRONG _ _ ! | Authentication failed. The user role does not match. |
| 404 | GATEWAY ROUTE URL NOT FOUND! | The destination service endpoint is invalid. |
| 401 | GATEWAY LIMIT ! | The maximum number of service connections has been reached. Try again later. |
| 500 | TARGET SERVICE ERROR CONNECTI _ _ _ ON REFUSE EXCEPTION _ _ | The destination service rejected the connection. |
| 500 | TARGET SERVICE ERROR NO RESPO _ _ _ _ NSE EXCEPTION _ | The destination service did not respond. |

**2.2.1.4. Delete a session**

**API overview**

This API permanently deletes a session and its related procedure data.

**Prerequisites**

An APP_KEY is required. To create an APP_KEY, navigate to Homepage > Profile Picture > APP_KEY.

**API endpoint**

POST http://ibp-studio-daily.aegmp.com/gateway/agent/api/deleteSession

**Request parameters**

Header parameters

| Field | Data type | Required | Description | Example |
|---|---|---|---|---|
| Authorization | String | Yes | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | Yes | Content-Type | application/json |

Body parameters Application integration APIs

| Field | Data type | Required | Description | Example |
|---|---|---|---|---|
| sessionId | string | Yes | The session ID. | de454297-c547- 440f-ae55- 057a83a2d121. This is the `uniqueCode` value returned from the Create a session API call. |

**Response parameters**

| Field | Data type | Description | Example |
|---|---|---|---|
| success | boolean | Indicates whether the service call was successful. | true |
| data | boolean | Indicates whether the business operation was successful. | true |

**Request example**

```bash
curl -X 'POST' http://ibp-studio-daily.aegmp.com/gateway/agent/api/deleteSession \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -d '{ "sessionId": "de454297-c547-440f-ae55-057a83a2d121"
```

`}'`

**Response example**

```json
  "success": true ,"data": true
```

**Status code descriptions**

Gateway error status codes

| HTTP status code | Error description | Fault definition |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | A required gateway parameter is missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed. The APP KEY is _ invalid. |
| 401 | GATEWAY APP KEY ALREADY EXPIRE _ D! | Authentication failed. The APP KEY _ has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | The service invocation path is invalid. |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The service invocation path is not registered. |

Application integration APIs

| 429 | GATEWAY LIMIT ! | The service has triggered rate limiting. Try again later. |
|---|---|---|
| 403 | GATEWAY HEADER PARAMETER MISSI NG! | The request is missing a required service parameter. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The specified workspace does not match the workspace that is associated with the APP KEY. _ |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. The authentication method is not supported. |
| 401 | GATEWAY AUTH USER NOT MATCH W _ RONG! | Authentication failed. The user information for authentication does not match. |
| 401 | GATEWAY AUTH USER ROLE WRONG _ _ ! | Authentication failed. The user role does not match. |
| 404 | GATEWAY ROUTE URL NOT FOUND! | The target service endpoint is invalid. |
| 401 | GATEWAY LIMIT ! | The maximum number of service connections has been reached. Try again later. |
| 500 | TARGET SERVICE ERROR CONNECTI _ _ _ ON REFUSE EXCEPTION _ _ | The target service refused the connection. |
| 500 | TARGET SERVICE ERROR NO RESPO _ _ _ _ NSE EXCEPTION _ | The target service did not respond. |

**2.2.1.5. Asynchronous tool callback**

**Overview**

Call this API to register an asynchronous API tool in the Toolbox. When the agent invokes your registered tool, it sends a unique task ID in the idx-agent-task-id header. After your task is complete, use this asynchronous callback API to finalize the tool invocation.

**Prerequisites**

Go to Homepage > Profile Picture > APP_KEY to create an APP_KEY. Then, call the 'Create session' API to obtain the uniqueCode return value.

**API endpoint**

POST http://ibp-studio-daily.aegmp.com/gateway/agent/api/taskFinishNotice

**Request parameters**

Header parameters

| Field | Data type | Required | Description | Example |
|---|---|---|---|---|
| Authorization | String | Yes | APP KEY _ | Bearer YOUR APP KEY _ _ |

Application integration APIs

| Content-Type | String | Yes | Content-Type | application/json |
|---|---|---|---|---|

Body parameters

| Field | Data type | Required | Description | Example |
|---|---|---|---|---|
| success | boolean | Yes | Indicates whether the task was successful. | true |
| taskId | string | Yes | Task ID | The value of the idx- agent-task-id header for the tool call is de454297-c547- 440f-ae55- 057a83a2d121. |
| data | string | Yes | The task result. | The value must be a JSON-formatted string. For example: {"result":"Asynchron ous API call successful"}. |
| errorCode | string | No | The error code. | The error code. |
| errorMsg | string | No | The error message. | The error message. |

**Response parameters**

| Field | Data type | Description | Example |
|---|---|---|---|
| success | boolean | The operation is successful. | true |

**Request example**

```json
curl -X 'POST' http://ibp-studio-daily.aegmp.com/gateway/agent/api/taskFinishNotice \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -d '{
    "taskId": "de454297-c547-440f-ae55-057a83a2d121"
  ,"success": true
  ,"data": "{\"result\":\"Asynchronous API call successful.\"}"
```

`}'`

**Response example**

```json
  "success": true
```

**Status codes**

Gateway error status codes Application integration APIs

| HTTP status code | Error description | Fault description |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | The required gateway parameter is missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed. The APP KEY is _ invalid. |
| 401 | GATEWAY APP KEY ALREADY EXPIRE _ D! | Authentication failed. The APP KEY _ has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | Invalid service invocation path. |
| 403 | GATEWAY APP PATH NOT REGISTERE _ D! | The current service invocation path is not registered. |
| 429 | GATEWAY LIMIT ! | The service has triggered rate limiting. Try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSI NG! | A required business parameter is missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The provided workspace code does not match the workspace code associated with the APP KEY owner. _ |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. The authentication method is not supported. |
| 401 | GATEWAY AUTH USER MISMATCH! _ | Authentication failed. The AccessKey user information does not match. |
| 401 | GATEWAY AUTH USER ROLE WRONG _ _ ! | Authentication failed. The user role does not match. |
| 404 | GATEWAY ROUTE URL NOT FOUND! | Invalid target service endpoint. |
| 401 | GATEWAY CONNECTION LIMIT REACH ED! | The maximum number of service connections has been reached. Try again later. |
| 500 | TARGET SERVICE ERROR CONNECTI _ _ _ ON REFUSE EXCEPTION _ _ | The target service rejected the connection. |
| 500 | TARGET SERVICE ERROR NO RESPO _ _ _ _ NSE EXCEPTION _ | The target service did not respond. |

**2.2.1.6. Call Result Feedback**

**Overview**

Application integration APIs You can provide feedback on the result of a one-time agent execution or on a specific task within the execution.

**Prerequisites**

After you invoke an agent, you can provide feedback, such as a like or dislike, on the result.

**Endpoint**

POST http://ibp-studio-daily.aegmp.com/gateway/agent/api/feedback

**Request parameters**

Header parameters

| Field | Data type | Required | Description | Example |
|---|---|---|---|---|
| Authorization | String | Yes | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | Yes | Content-Type | application/json |

Body parameters

| Field | Data type | Required | Description | Example |
|---|---|---|---|---|
| sessionId | string | Yes | The session ID. |   |
| requestId | string | Yes | The request ID. |   |
| taskId | string | Yes | The task ID. |   |
| uniqueCode | string | No | The unique ID. Pass this parameter to update feedback information. |   |
| subject | string | Yes | The feedback object. | REQUEST: Provide feedback on the output of a one-time run. TASK: Provide feedback on a specific task in the run. |
| provider | object | Yes | The provider of the feedback. |   |
| source | string | Yes | The source of the feedback provider. | USER: The user. AUTO EVALUATION: _ The evaluation center. |
| extendInfo | object | No | Extended information about the feedback provider. |   |

Application integration APIs

| vote | string | Yes | The feedback result. | LIKE: Like. DISLIKE: Dislike. NEUTRAL: Neutral. |
|---|---|---|---|---|
| extCommentsInfo | object | No | Extended information about the feedback result. |   |

**Response parameters**

| Field | Data type | Description | Example |
|---|---|---|---|
| success | boolean | Indicates whether the request was successful. |   |
| data | object | The feedback information. |   |
| sessionId | string | The session ID. |   |
| requestId | string | The request ID. |   |
| taskId | string | The task ID. |   |
| uniqueCode | string | The unique ID. |   |
| subject | string | The feedback object. | REQUEST: Provide feedback on the output of a one-time run. TASK: Provide feedback on a specific task in the run. |
| provider | object | The provider of the feedback. |   |
| source | string | The source of the feedback provider. | USER: The user. AUTO EVALUATION: The _ evaluation center. |
| extendInfo | object | Extended information about the feedback provider. |   |
| vote | string | The feedback result. | LIKE: Like. DISLIKE: Dislike. NEUTRAL: Neutral. |
| extCommentsInfo | object | Extended information about the feedback result. |   |
| errorCode | string | The error code. |   |
| errorMsg | string | Error code |   |

Application integration APIs

**Request example**

```json
curl --location --request POST 'http://ibp-studio-daily.aegmp.com/gateway/agent/api/feedback' \ --header 'Authorization: Bearer YOUR_APP_KEY' \ --header 'Content-Type: application/json' \ -d '{
    "sessionId": "87302f04-7617-41e4-b4c9-9028c3341dcg",
    "requestId": "e359512f-ba3a-46a7-b412-882d7e9f8b32",
    "taskId": "61e60082-690c-4548-a7ef-28d1ff6bb0f9",
    "subject": "TASK",
    "provider": {
        "source": "USER",
        "extendInfo": {}
```

`},`

```json
    "vote": "LIKE",
    "extCommentsInfo": {
        "comment": "123"
```

`}'`

**Response example**

```json
  "errorMessages": [],
  "success": true,
  "data": {
    "tenant": null,
    "sessionId": "87302f04-7617-41e4-b4c9-9028c3341dcg",
    "requestId": "e359512f-ba3a-46a7-b412-882d7e9f8b32",
    "taskId": "61e60082-690c-4548-a7ef-28d1ff6bb0f9",
    "subject": "TASK",
    "uniqueCode": "b8f5ea27-50f7-4147-88d1-9d02ccbf0061",
    "provider": {
      "source": "USER",
      "extendInfo": {}
```

`},`

```json
    "vote": "LIKE",
    "extCommentsInfo": {
      "comment": "123"
```

`},`

```json
  "errorCode": null,
  "errorMsg": null
```

**Status codes**

Gateway exception status codes

| HTTP status code | Error description | Fault description |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | A required gateway parameter is missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed. The APP KEY is _ invalid. |
| 401 | GATEWAY APP KEY ALREADY EXPIRE _ D! | Authentication failed. The APP KEY _ has expired. |

Application integration APIs

| 403 | GATEWAY APP PATH NOT FOUND! _ | The service invocation path is invalid. |
|---|---|---|
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service invocation path is not registered. |
| 429 | GATEWAY LIMIT! | The service has triggered rate limiting. Try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSI NG! | A required business parameter is missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The passed workspace code does not match the workspace code associated with the user of the APP KEY. _ |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. The authentication method is not supported. |
| 401 | GATEWAY AUTH USER NOT MATCH W _ RONG! | Authentication failed. The AccessKey (AK) user information does not match. |
| 401 | GATEWAY AUTH USER ROLE WRONG _ _ ! | Authentication failed. The user role does not match. |
| 404 | GATEWAY ROUTE URL NOT FOUND! | The destination service endpoint is invalid. |
| 401 | GATEWAY LIMIT! | The maximum number of service connections has been reached. Try again later. |
| 500 | TARGET SERVICE ERROR CONNECTI _ _ _ ON REFUSE EXCEPTION _ _ | The destination service rejected the connection. |
| 500 | TARGET SERVICE ERROR NO RESPO _ _ _ _ NSE EXCEPTION _ | The destination service did not respond. |

#### Knowledge base retrieval

**2.2.2.1. Knowledge base retrieval**

The system provides general retrieval capabilities for knowledge bases, including document, custom, and image-text knowledge bases.

**Prerequisites**

Users can implement general retrieval capabilities for specific fields by using the `kbSubmodels.kbIndexes` field of the knowledge base. To verify the effect of calling the business API, view the request example and click the debugging button to the right of the curl command example.

**Endpoint**

```
 POST http://ibp-studio-daily.aegmp.com/gateway/kortex/api/kb/mono/retrieve
```

Application integration APIs

**Request parameters**

**Header parameters**

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| Authorizatio n | String | Yes | The APP KEY. _ | Bearer YOUR APP KEY _ _ |
| Content- Type | String | Yes | The Content- Type. | application/json |
| x-sfm- workspaceco de | String | Yes | The target workspace. | your workspace code _ _ |

**Body parameters**

| Parameter | Type | Required | Descriptio n | Example |
|---|---|---|---|---|
| kbIndexCode | String | Yes | The code of the knowledge base index. See kbSubmodel s[0].kbIndex es[0].kbInde xCode in the knowledge base details response. | tttbnz21diense89. |
| kbIndexRetrieve FieldName | String | Yes | The retrieval field. | chunk representation, as shown in the _ kbSubmodels section of the knowledge base details response; for document knowledge bases, always pass chunk representation; _ for image-text knowledge bases, pass either image path or text; _ for custom knowledge bases, see the Retrieve-type fields in kbSubmodels[0].kbIndexes within the knowledge base details response body. |
| query | String | Yes | The query content. | A string. |
| filters | JSONObject | No | The query content. | Extended filters. For example, for a documentt knowledge base, you can retrieve specific documents, such as {"file code": "aaa"}. _ |
| score | Double | Yes | The minimum score. | 0.01 |

Application integration APIs

| limit | Integer | Yes | The number of returned entries. | 10 |
|---|---|---|---|---|
| advancedRules | Object | No | The advanced rule configuratio n, which supports complex filtering conditions combined with AND/OR logic. | {"operator":"AND","conditions": [{"type":"simple","simpleRule": {"fileName":"plan code","ruleTypeEnum":"EQ","file _ Value":"YCJ2024100"}}, {"type":"nested","advancedRules": {"operator":"AND","conditions": [{"type":"simple","simpleRule": {"fileName":"plan name","ruleTypeEnum":"LIKE","fi _ leValue":"Jiangnan District"}}, {"type":"simple","simpleRule": {"fileName":"area name","ruleTypeEnum":"IN","file _ ValueList":["Jiangbei District","Jiangnan District"]}}]}}]} |
| - operator | String | Yes | The logical operator. Valid values: AND, OR. | AND |
| - conditions | Array | Yes | The list of conditions. Each condition can be a simple condition (type=simpl e) or a nested condition (type=neste d). | [{"type":"simple",...},{"type":"nested",...}] |
| -- type | String | Yes | The condition type. Valid values: simple (simple condition), nested (nested condition). | simple |
| -- simpleRule | Object | No | The definition of a simple rule. This parameter is required when type=simple . | {"fileName":"plan code","ruleTypeEnum":"EQ","file _ Value":"YWC34520000"} |
| --- fileName | String | Yes | The name of the field to match. | plan code _ |

Application integration APIs

| --- ruleTypeEnum | String | Yes | The rule type. Valid values: EQ (equals), IN (includes), IS NOT NUL _ _ L (not null), LIKE (fuzzy match). | EQ |
|---|---|---|---|---|
| ---fileValue | Object | No | A single matching value. Use this parameter when ruleTypeEnu m is EQ or LIKE. | YCJ2024520000 |
| ---fileValueList | Array | No | The list of multiple matching values. Use this parameter when ruleTypeEnu m is IN. | ["Jiangnan District",Jiangbei District"] |
| -- advancedRules | Object | No | The nested advanced search rule. This parameter is required when type=neste d. It supports recursive nesting. | {"operator":"AND","conditions": [{"type":"simple",...},{"type":"simple",...}]} |
| ---operator | String | Yes | The nested logical operator. Valid values: AND, OR. | AND |
| ---conditions | Array | Yes | The list of nested conditions. | [...] |

**Request example**

Application integration APIs

```json
curl -X 'POST' http://ibp-studio-daily.aegmp.com/gateway/kortex/api/kb/mono/retrieve \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -H 'x-sfm-workspacecode: baseline' \ -d '{
    "kbIndexCode":"qdqsajkhjn6xpn7z",
     "kbIndexRetrieveFieldName":"text",
     "query":"strawberry",
      "score":0.01,
     "limit":10
```

`}'`

**Response parameters**

| Field | Type | Description | Example |
|---|---|---|---|
| success | Boolean | Indicates whether the operation succeeded. | true |
| data | List<Object> | The returned data, structured according to the predefined kbSubmodels schema. | [] |
| -score | String | The score. | true |
| -sys source ids _ _ | String | Additional data information. | true |
| -sys data id _ _ | String | The unique ID of the data. | true |
| -sys create time _ _ | String | The creation time. | true |
| -**** | String | Dynamic custom recall fields. For example, for image-text knowledge bases: file code, _ image path, text; for _ document knowledge bases: file code, _ chunk bboxs, _ show content, _ chunk upload type, _ _ chunk content, _ chunk sort number, _ _ start page. _ |   |
| metrics | Object | Performance metrics. | {} |
| -kbCode | String | The code of the knowledge base. | xxx |
| -totalTime | Long | The total retrieval time in milliseconds. | 150 |

Application integration APIs

| -chunksCount | Integer | The number of chunks returned. | 10 |
|---|---|---|---|
| -retrievalDetails | List<Object> | Detailed retrieval metrics. | [{"kbIndexCode":"yyy","en gineType":"builtin vector", _ "embeddingTime":50,"vect orRecallTime":80,"retrieve dChunksCount":10}] |
| --kbIndexCode | String | The code of the index. | ozqn95a5936ycwkl |
| --engineType | String | The type of the engine. | builtin vector _ |
| --embeddingTime | Long | The vector embedding time in milliseconds. | 50 |
| --vectorRecallTime | Long | The vector recall time in milliseconds. | 80 |
| --textQueryTime | Long | The full-text query time in milliseconds. | 60 |
| --retrievedChunksCount | Integer | The number of chunks actually recalled by the engine. | 10 |
| errorCode | String | The error code. | true |
| errorMsg | String | The error description. | true |

**Response example**

```json
{"success":true,"data": [{"score":0.529308557510376,"file_code":"adaf2a92995b4e439f68ebe3222de9a1","sys_source_ids":" {\"kb_submodel\": \"true\", \"kb_submodel.sys_data_id\": \"82aab26d-b1ff-40da-a3fcbbadb5b3b439\"}","image_path":"apsara/kortex/kb/visual/file/wjtir7knghhr/SglptjTkqA35r12MoUOVxE91rWSEonT f1af9cbaa9d9aee17a0c0bd944ef662.jpeg","sys_data_id":"82aab26d-b1ff-40da-a3fcbbadb5b3b439","text":"This is a close-up photo of a strawberry with water droplets on its surface and green leaves in the background.","sys_create_time":"2025-07- 04T13:28:58.122+00:00"}],"errorCode":null,"errorMsg":null}
```

**Status codes**

Descriptions of gateway exception status codes.

| HTTP status code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | A required parameter for the gateway is missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed. The APP KEY is invalid. _ |
| 401 | GATEWAY APP KEY ALREADY EXPIRED! _ | Authentication failed. The APP KEY has expired. _ |

Application integration APIs

| 401 | GATEWAY ROLE NOT MATCH! | Authentication failed. The role associated with the current APP KEY user does not match. _ |
|---|---|---|
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role associated with the current APP KEY user has expired. _ |
| 403 | GATEWAY APP PATH NOT FOUND! _ | The service invocation path is invalid. |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service invocation path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggered rate limiting. Try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggered rate limiting. Try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | A required business parameter is missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATC H! | The workspace code passed does not match the workspace code associated with the APP KEY _ user. |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. The authentication method is not supported. |
| 401 | GATEWAY AUTH USER NOT MATCH WRONG! _ | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE WRONG! _ _ | Authentication failed. The user role does not match. |
| 404 | GATEWAY ROUTE URL NOT FOUND! | The target service address is invalid. |
| 401 | GATEWAY LIMIT ! | The service connection limit has been reached. Try again later. |
| 500 | TARGET SERVICE ERROR CONNECTION REF _ _ _ _ USE EXCEPTION _ | The target service refused the connection. |
| 500 | TARGET SERVICE ERROR NO RESPONSE EX _ _ _ _ _ CEPTION | The target service did not respond. |

**2.2.2.2. Batch retrieval for knowledge bases**

Retrieve from multiple knowledge bases simultaneously. You can configure different retrieval parameters for each knowledge base. The system supports a maximum of 10 knowledge bases in a single batch retrieval.

**Prerequisites**

The batch retrieval API retrieves data from multiple knowledge bases simultaneously, and returns independent results and performance metrics for each knowledge base. This API applies to scenarios requiring data retrieval from multiple knowledge bases at the same time.

**Endpoint**

Application integration APIs

```
 POST http://ibp-studio-daily.aegmp.com/sfm-agent-studio/sfm-api-
gateway/gateway/kortex/api/kb/mono/combination/retrieve
```

**Request parameters**

**Header parameters**

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| Authorization | String | Yes | The APP KEY. _ | Bearer YOUR APP KEY _ _ |
| x-sfm- workspacecode | String | Yes | The target workspace. | your workspace cod _ _ e |
| Content-Type | String | Yes | The Content-Type. | application/json |

Body parameters

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| combinationParams | List<object> | Yes | The list of retrieval parameters. | [{"kbIndexCode":"xx x","kbIndexRetrieveF ieldName":"name"," query":"test","score" :0.01,"limit":10}] |
| -kbIndexCode | String | Yes | The code of the knowledge base index. | tttbnz21dien |
| - kbIndexRetrieveField Name | String | Yes | The retrieval field. | name |
| -query | String | Yes | The query content. | test query |
| -score | Double | Yes | The minimum score. | 0.01 |
| -limit | Integer | Yes | The number of returned entries. | 10 |
| -filters | Object | No | The query content. | Extended filter items. For example, for an image-text knowledge base, you can retrieve specific documents. Example: {"file code": _ ["8a58578fce264cd3 a648162ea94d2686" ]} |

Application integration APIs

| -mapBatchKey | String | No | The result mapping key for batch retrieval, used to distinguish results from different requests. | kb1 |
|---|---|---|---|---|
| -advancedRules | Object | No | The advanced rule configuration, which supports complex filtering conditions combined with AND/OR logic. | {"operator":"AND","c onditions": [{"type":"simple","si mpleRule": {"fileName":"plan co _ de","ruleTypeEnum": "EQ","fileValue":"YCJ 2024100"}}, {"type":"nested","ad vancedRules": {"operator":"AND","c onditions": [{"type":"simple","si mpleRule": {"fileName":"plan n _ ame","ruleTypeEnu m":"LIKE","fileValue" :"Jiangnan District"}}, {"type":"simple","si mpleRule": {"fileName":"area n _ ame","ruleTypeEnu m":"IN","fileValueList ":["Jiangbei District","Jiangnan District"]}}]}}]} |
| --operator | String | Yes | The logical operator. Valid values: AND, OR. | AND |
| --conditions | Array | Yes | The list of conditions. Each condition can be a simple condition (type=simple) or a nested condition (type=nested). | [{"type":"simple",...} , {"type":"nested",...}] |
| ---type | String | Yes | The condition type. Valid values: simple (simple condition), nested (nested condition). | simple |
| ---simpleRule | Object | No | The definition of a simple rule. This parameter is required when type=simple. | {"fileName":"plan co _ de","ruleTypeEnum": "EQ","fileValue":"YW C34520000"} |
| ----fileName | String | Yes | The name of the field to match. | plan code _ |

Application integration APIs

| ----ruleTypeEnum | String | Yes | The rule type. Valid values: EQ (equals), IN (contains), IS NOT NULL (not _ _ null), LIKE (fuzzy match). | EQ |
|---|---|---|---|---|
| ----fileValue | Object | No | A single matching value. Use this parameter when ruleTypeEnum is EQ or LIKE. | YCJ2024520000 |
| ----fileValueList | Array | No | The list of multiple matching values. Use this parameter when ruleTypeEnum is IN. | [\"Jiangnan District\",\"Jiangbei District\"] |
| ---advancedRules | Object | No | The nested advanced retrieval rule. This parameter is required when type=nested. It supports recursive nesting. | {\"operator\":\"AND\" ,\"conditions\": [{\"type\":\"simple\",. ..}, {\"type\":\"simple\",.. .}]} |
| ----operator | String | Yes | The nested logical operator. Valid values: AND, OR. | AND |
| ----conditions | Array | Yes | The list of nested conditions. | [...] |

**Request example**

Example of batch retrieval from knowledge bases Application integration APIs

```json
curl -X 'POST' http://ibp-studio-daily.aegmp.com/sfm-agent-studio/sfm-apigateway/gateway/kortex/api/kb/mono/combination/retrieve \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -H 'x-sfm-workspacecode: baseline' \ -d '{
    "combinationParams":[
            "kbCode":"kbcode1",
            "kbIndexRetrieveFieldName":"name",
            "query":"Test query 1",
            "score":0.01,
            "limit":5,
            "mapBatchKey":"kb1",
            "kbIndexEngineType":"builtin_vector"
```

`},`

```json
            "kbCode":"kbcode2",
            "kbIndexRetrieveFieldName":"text",
            "query":"Test query 2",
            "score":0.01,
            "limit":5,
            "mapBatchKey":"kb2",
            "kbIndexEngineType":"builtin_es"
```

`]` `}'`

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|
| success | Boolean | Indicates whether the operation succeeded. | true |
| data | List<Object> | The list of batch retrieval results. | [] |
| -mapBatchKey | String | The result mapping key, which corresponds to mapBatchKey in the request. | kb1 |
| -kbCode | String | The code of the knowledge base. | xxx |
| -kbIndexEngineType | String | The type of the index engine. | builtin vector _ |
| -kbIndexCode | String | The code of the index. | yyy |
| -result | List<Map<String,Object>> | The list of retrieval results. | [{"score":0.85,"file code":" _ xxx"}] |
| metrics | Object | The performance metrics. | {} |

Application integration APIs

| -kbCode | String | The code of the knowledge base. | xxx |
|---|---|---|---|
| -totalTime | Long | The total retrieval time in milliseconds. | 150 |
| -chunksCount | Integer | The number of chunks returned. | 10 |
| -retrievalDetails | List<Object> | The detailed retrieval metrics. | [] |
| --kbIndexCode | String | The code of the index. | ozqn95a5936ycwkl |
| --engineType | String | The type of the engine. | builtin vector _ |
| --embeddingTime | Long | The vector embedding time in milliseconds. | 50 |
| --vectorRecallTime | Long | The vector recall time in milliseconds. | 80 |
| --textQueryTime | Long | The full-text query in milliseconds. | 60 |
| --retrievedChunksCount | Integer | The number of chunks actually recalled by this engine. | 10 |
| errorCode | String | The error code. | 401 |
| errorMsg | String | The error description. | Request error |

**Response example**

```json
{"success":true,"data": [{"mapBatchKey":"kb1","kbCode":"o4jgjrg0997v","kbIndexEngineType":"builtin_vector","kbIndexCode":"o4jgjr 97vr4rd","result":[{"score":1,"sys_source_ids":"{\'kb_submodel\': \'true\', \'source_builtin_smod\': \ 'true\', \'kb_submodel.sys_data_id\': \'a8c07518-0f8f-4ff4-b5f4-a91781241cac\'}","name":"Xiao Ming","sys_data_id":"a8c07518-0f8f-4ff4-b5f4a91781241cac","describe":"Student","age":12,"sys_create_time":"2026-03-13T07:16:57.661+00:00"},{"score ":0.4903782308101654,"sys_source_ids":"{\'kb_submodel\': \'true\', \'source_builtin_smod\': \'true\', \'kb_submodel.sys_data_id\': \'5a8d1e92-ec8f-4316-aa8b-7be48379733e\'}","name":"Xiao Gang","sys_data_id":"5a8d1e92-ec8f-4316-aa8b- 7be48379733e","describe":"Worker","age":25,"sys_create_time":"2026-03- 13T07:17:12.418+00:00"}],"metrics": {"kbCode":"o4jgjrg0997v","totalTime":412,"chunksCount":2,"retrievalDetails": [{"kbIndexCode":"o4jgjrg0997vr4rd","engineType":"builtin_vector","embeddingTime":279,"vectorRecallTime": "textQueryTime":null,"retrievedChunksCount":2}]}}],"errorCode":null,"errorMsg":null,"traceId":null,"env" ll,"ext":null}
```

**Status codes**

Application integration APIs

| HTTP status code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | A required parameter for the gateway is missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed. The APP KEY is invalid. _ |
| 401 | GATEWAY APP KEY ALREADY EXPIRED! _ | Authentication failed. The APP KEY has expired. _ |
| 401 | GATEWAY ROLE NOT MATCH! | Authentication failed. The role associated with the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role associated with the current APP KEY user has expired. _ |
| 403 | GATEWAY APP PATH NOT FOUND! _ | The service invocation path is invalid. |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service invocation path is not registered. |
| 429 | GATEWAY LIMIT ! | The service triggered rate limiting. Try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service triggered rate limiting. Try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | A required business parameter is missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATC H! | The workspace code passed does not match the workspace code associated with the APP KEY user. _ |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. The authentication method is not supported. |
| 401 | GATEWAY AUTH USER NOT MATCH WRONG! _ | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE WRONG! _ _ | Authentication failed. The user role does not match. |
| 404 | GATEWAY ROUTE URL NOT FOUND! | The target service address is invalid. |
| 401 | GATEWAY LIMIT ! | The service connection limit has been reached. Try again later. |
| 500 | TARGET SERVICE ERROR CONNECTION REFU _ _ _ _ SE EXCEPTION _ | The target service refused the connection. |
| 500 | TARGET SERVICE ERROR NO RESPONSE EXC _ _ _ _ _ EPTION | The target service did not respond. |

Application integration APIs

**2.2.2.3. Document knowledge base retrieval**

The system retrieves content based on the encoding of the document knowledge base.

**Prerequisites**

You can verify the effect of calling the business API by viewing the request example and clicking the debugging button to the right of the curl command example.

**Endpoint**

| POST http://ibp-studio-daily.aegmp.com/sfm-agent-studio/sfm-api- |   |
|---|---|

**Request parameters**

**Header parameters**

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| Authorization | String | Yes | The APP KEY. _ | Bearer YOUR APP KEY _ _ |
| x-sfm- workspacecode | String | Yes | The target workspace. | your workspace cod _ _ e |
| Content-Type | String | Yes | The Content-Type. | application/json |

**Body parameters**

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| kbCode | String | Yes | The code of the knowledge base. | tttbnz21dien |
| kbIndexEngineType | String | No | The type of index engine. Valid values: builtin vector (vector _ index engine), builtin es (full-text _ index engine). | builtin vector _ |
| query | String | Yes | The query content. | A string |
| score | Double | Yes | The minimum score. | 0.01 |
| limit | Integer | Yes | The number of returned entries. | 10 |

Application integration APIs

| filters | Object | No | The filter conditions. | Extended filter items, {"fileCodes": ["d110d4f793e347b db8aaf840b3e3d27a ","8a58578fce264cd 3a648162ea94d268 6"]} |
|---|---|---|---|---|
| chunkConfig | Object | No | The chunk extension configuration. | {"chunkBefore": 2, "chunkAfter": 2, "withNeighborChunk s": true} |
| -chunkBefore | Integer | No | The number of adjacent chunks before the current chunk to return. The maximum value is 5. | 2 |
| -chunkAfter | Integer | No | The number of adjacent chunks after the current chunk to return. The maximum value is 5. | 2 |
| -withNeighborChunks | Boolean | No | Specifies whether to return the list of adjacent chunk content. | true |
| fusionType | String | No | The fusion retrieval type. Valid values: lws (linear weighted scoring), rrf (reciprocal rank fusion). If this parameter is empty, fusion retrieval is not used. | lws |
| fusionConfig | Object | No | The fusion retrieval configuration. You must set this parameter only if fusionType is not empty. | {"textScore": 0.5, "vectorScore": 0.5, "topKText": 20, "topKVec": 20, "topN": 10, "keywordWeight": 0.5, "rankDiscount": 60} |
| -topKText | Integer | No | The number of entries returned by full-text retrieval. By default, the system uses the value of "limit". | 20 |

Application integration APIs

| -topKVec | Integer | No | The number of entries returned by vector retrieval. By default, the system uses the value of "limit". | 20 |
|---|---|---|---|---|
| -topN | Integer | No | The number of entries to return after fusion retrieval. By default, the system uses the value of "limit". | 10 |
| -textScore | Double | No | The score threshold for full-text retrieval, used in fusion retrieval. Default value: 0.5. | 0.5 |
| -vectorScore | Double | No | The score threshold for vector retrieval, used in fusion retrieval. Default value: 0.5. | 0.5 |
| -keywordWeight | Float | No | The keyword weight (used in LWS). A higher value gives more preference to full-text retrieval using BM25. Default value: 0.5. | 0.5 |
| -rankDiscount | Integer | No | The rank decay coefficient for RRF. A higher value places less emphasis on top rankings. Default value: 60. | 60 |
| needFileInfo | Boolean | No | Specifies whether to return file information. | true |

**Request example**

```json
curl -X 'POST' http://ibp-studio-daily.aegmp.com/sfm-agent-studio/sfm-apigateway/gateway/kortex/api/kb/doc/retrieve \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -H 'x-sfm-workspacecode: baseline' \ -d '{
    "kbCode":"qdqsajkhjn6x",
     "query":"strawberry",
      "score":0.01,
     "limit":10
```

`}'`

**Response parameters**

Application integration APIs

| Field | Type | Description | Example |
|---|---|---|---|
| success | Boolean | Indicates whether the operation succeeded. | true |
| data | List<Object> | The returned data, structured according to the predefined kbSubmodels schema. | [] |
| -score | String | The relevance score of the retrieval result. The meaning varies by retrieval type. For single-engine retrieval, the original engine semantics apply. For hybrid retrieval, scores are normalized for unified evaluation. 1) Single- engine retrieval: retains original engine semantics— vector retrieval uses cosine similarity (0–1), full-text retrieval uses BM25 relevance score. 2) LWS fusion: linear weighted fusion score, normalized. 3) RRF fusion: reciprocal rank fusion score based on ranking. | 0.5 |
| -sys data id _ _ | String | The unique ID of the data. | 59cc2523-8445-4f3a-91f7- 5e311f5530b2 |
| -file name _ | String | The file name, returned only when needFileInfo is true. | document.pdf |
| -file url _ | String | The file URL, returned only when needFileInfo is true. It contains temporary STS authentication information. | https://example.com/files/d ocument.pdf |
| -file type _ | String | The file type, returned only when needFileInfo is true. | pdf |
| -sys create time _ _ | String | The time when the data was created. | 2023-04-01T12:34:56Z |
| -file code _ | String | The file code, returned only when needFileInfo is true. | 123456 |
| -chunk upload type _ _ | Integer | The upload type. | 1 |
| -chunk content _ | String | The chunk content—the text sent to the LLM as a prompt after recall. |   |

Application integration APIs

| -show content _ | String | The chunk content—in text form with placeholders for bounding boxes and objects. |   |
|---|---|---|---|
| -chunk bboxs _ | List<Object> | The bounding box coordinate information. |   |
| -start page _ | Integer | The sequence number of the chunk. | 1 |
| -chunk sort number _ _ | Integer | The page number. | 0 |
| -beforeChunks | List<KbdocChunkNeighbor > | The list of N preceding adjacent chunks. The system returns this field only when chunkBefore is greater than 0. | [{"sysDataId":"xxx","fileCo de":"yyy","chunkContent":" content"}] |
| -afterChunks | List<KbdocChunkNeighbor > | The list of N following adjacent chunks, returned only when chunkAfter is greater than 0. | [{"sysDataId":"xxx","fileCo de":"yyy","chunkContent":" content"}] |
| -neighborChunkContents | List<String> | The list of adjacent chunk content, returned only when withNeighborChunks is true. | ["previous chunk content","retrieved chunk content","next chunk content"] |
| ext | Object | The extended field. | {} |
| -metrics | Object | The performance metrics. | {} |
| --kbCode | String | The code of the knowledge base. | ozqn95a5936y |
| --totalTime | Long | The total retrieval time in milliseconds. | 150 |
| --chunksCount | Integer | The number of chunks returned. | 10 |
| --fusionType | String | The type of fusion method. | lws |
| --rrfTime | Long | The RRF fusion time in milliseconds (present only during RRF fusion). | 20 |
| --lwsTime | Long | The LWS fusion time in milliseconds (present only during LWS fusion). | 15 |

Application integration APIs

| --fillTime | Long | The time taken to fill additional information, in milliseconds. | 30 |
|---|---|---|---|
| --retrievalDetails | List<Object> | The detailed retrieval metrics. | [{"kbIndexCode":"ozqn95a 5936ycwkl","engineType":" builtin vector","embedding _ Time":50,"vectorRecallTim e":80,"retrievedChunksCou nt":10}] |
| ---kbIndexCode | String | The code of the index. | ozqn95a5936ycwkl |
| ---engineType | String | The type of the engine. | builtin vector _ |
| ---embeddingTime | Long | The vector embedding time in milliseconds. | 50 |
| ---vectorRecallTime | Long | The vector recall time in milliseconds. | 80 |
| ---textQueryTime | Long | The full-text query time in milliseconds. | 60 |
| ---retrievedChunksCount | Integer | The number of chunks actually recalled by this engine. | 10 |
| errorCode | String | The error code. | 401 |
| errorMsg | String | The error description. | Error |

**Response example**

```json
{"success":true,"data":[{"sys_data_id":"eda55b8d-93e6-40b7-a6de- 19b49f97b6fd","file_code":"e8f574d28a854f31aa52fda0d18f713e","chunk_content":"xxxxxxxxxxxxx","score":0.5 9527},{"sys_data_id":"aafd75f6-e8cd-4f64-994f- 59cb51a3fe5b","file_code":"e8f574d28a854f31aa52fda0d18f713e","chunk_content":"xxxxxxxxxxxx","score":0.53 395},{"sys_data_id":"2c162691-245b-4a9a-9b22ccf401de84b0","file_code":"e8f574d28a854f31aa52fda0d18f713e","chunk_content":"xxxxxxxxxxx","score":0.503 36}],"errorCode":null,"errorMsg":null,"traceId":null,"env":null,"ext":{"metrics":" {'kbCode':'q82ni07qxpcg','chunksCount':3,'fillTime':0,'retrievalDetails': [{'embeddingTime':144,'engineType':'builtin_vector','kbIndexCode':'q82ni07qxpcgb765','retrievedChunksCou :3,'vectorRecallTime':49}],'totalTime':213}"}}
```

**Status codes**

| HTTP status code | Error description | Error interpretation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | A required parameter for the gateway is missing. |

Application integration APIs

| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed. The APP KEY is invalid. _ |
|---|---|---|
| 401 | GATEWAY APP KEY ALREADY EXPIRED! _ | Authentication failed. The APP KEY has expired. _ |
| 401 | GATEWAY ROLE NOT MATCH! | Authentication failed. The role associated with the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role associated with the current APP KEY user has expired. _ |
| 403 | GATEWAY APP PATH NOT FOUND! _ | The service invocation path is invalid. |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service invocation path is not registered. |
| 429 | GATEWAY LIMIT ! | The service has triggered rate limiting. Try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service has triggered rate limiting. Try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | A required business parameter is missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MAT CH! | The workspace code passed does not match the workspace code associated with the APP KEY user. _ |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. The authentication method is not supported. |
| 401 | GATEWAY AUTH USER NOT MATCH WRONG! _ | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE WRONG! _ _ | Authentication failed. The user role does not match. |
| 404 | GATEWAY ROUTE URL NOT FOUND! | The target service address is invalid. |
| 401 | GATEWAY LIMIT ! | The service connection limit has been reached. Try again later. |
| 500 | TARGET SERVICE ERROR CONNECTION REF _ _ _ _ USE EXCEPTION _ | The target service refused the connection. |
| 500 | TARGET SERVICE ERROR NO RESPONSE EX _ _ _ _ _ CEPTION | The target service did not respond. |

**2.2.2.4. Batch retrieval for document knowledge bases**

Retrieve from multiple document knowledge bases at the same time. You can configure different retrieval parameters for each knowledge base. The system supports a maximum of 10 knowledge bases in a single batch retrieval.

**Prerequisites**

Application integration APIs The batch retrieval API supports simultaneous retrieval from multiple document knowledge bases, and returns independent results for each knowledge base. This API applies to scenarios requiring data retrieval from multiple document knowledge bases at the same time.

**Endpoint**

| POST http://ibp-studio-daily.aegmp.com/sfm-agent-studio/sfm-api- |   |
|---|---|

**Request parameters**

**Header parameters**

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| Authorization | String | Yes | The APP KEY. _ | Bearer YOUR APP KEY _ _ |
| x-sfm- workspacecode | String | Yes | The target workspace. | your workspace cod _ _ e |
| Content-Type | String | Yes | The Content-Type. | application/json |

**Body parameters**

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| combinationParams | List<Object> | Yes | The list of retrieval parameters. | [{"kbCode":"xxx","qu ery":"test","score":0. 01,"limit":10}] |
| -kbCode | String | Yes | The code of the knowledge base. | tttbnz21dien |
| -query | String | Yes | The query content. | Test query |
| -score | Double | Yes | The minimum score. | 0.01 |
| -limit | Integer | Yes | The number of returned entries. | 10 |
| -mapBatchKey | String | No | The result mapping key for batch retrieval, used to distinguish results from different requests. | kb1 |
| -kbIndexEngineType | String | No | The type of the index engine. Valid values: builtin vector (vector _ index engine), builtin es (full-text _ index engine). | builtin vector _ |

Application integration APIs

| -filters | Object | No | The filter conditions. | Extended filter items, {"fileCodes": ["d110d4f793e347b db8aaf840b3e3d27a ","8a58578fce264cd 3a648162ea94d268 6"]} |
|---|---|---|---|---|
| -chunkConfig | Object | No | The chunk extension configuration. | {"chunkBefore": 2, "chunkAfter": 2, "withNeighborChunk s": true} |
| --chunkBefore | Integer | No | The number of adjacent chunks before the current chunk to return. The maximum value is 5. | 2 |
| --chunkAfter | Integer | No | The number of adjacent chunks after the current chunk to return. The maximum value is 5. | 2 |
| -- withNeighborChunks | Boolean | No | Specifies whether to return the list of adjacent chunk content. | true |
| -fusionType | String | No | The fusion retrieval type. Valid values: lws (linear weighted scoring), rrf (reciprocal rank fusion). If this parameter is empty, fusion retrieval is not used. | lws |
| -fusionConfig | Object | No | The fusion retrieval configuration. Set this parameter only when fusionType is not empty. | {"textScore": 0.5, "vectorScore": 0.5, "topKText": 20, "topKVec": 20, "topN": 10, "keywordWeight": 0.5, "rankDiscount": 60} |
| --topKText | Integer | No | The number of entries returned by full-text retrieval. By default, the system uses the value of "limit". | 20 |

Application integration APIs

| --topKVec | Integer | No | The number of entries returned by vector retrieval. By default, the system uses the value of "limit". | 20 |
|---|---|---|---|---|
| --topN | Integer | No | The number of entries returned after fusion retrieval. By default, the system uses the value of "limit". | 10 |
| --textScore | Double | No | The score threshold for full-text retrieval, used during fusion retrieval. Default value: 0.5. | 0.5 |
| --vectorScore | Double | No | The score threshold for vector retrieval, used during fusion retrieval. The default value is 0.5. | 0.5 |
| --keywordWeight | Float | No | The keyword weight (used in LWS fusion). A higher value gives more preference to full-text retrieval using BM25. Default value: 0.5. | 0.5 |
| --rankDiscount | Integer | No | The rank decay coefficient for RRF fusion. A higher value places less emphasis on top rankings. Default value: 60. | 60 |
| -needFileInfo | Boolean | No | Specifies whether to return file information. | true |

**Request example**

Application integration APIs

```json
curl -X 'POST' http://ibp-studio-daily.aegmp.com/sfm-agent-studio/sfm-apigateway/gateway/kortex/api/kb/doc/combination/retrieve \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -H 'x-sfm-workspacecode: baseline' \ -d '{
    "combinationParams":[
            "kbCode":"kbcode1",
            "query":"Test query 1",
            "score":0.01,
            "limit":5,
            "mapBatchKey":"kb1"
```

`},`

```json
            "kbCode":"kbcode2",
            "query":"Test query 2",
            "score":0.01,
            "limit":5,
            "mapBatchKey":"kb2",
            "fusionType":"lws",
            "topKText":20,
            "topKVec":20,
            "topN":5
```

`]` `}'`

**Response parameters**

| Field | Type | Description | Example |
|---|---|---|---|
| success | Boolean | Indicates whether the operation succeeded. | true |
| data | List<Object> | The list of batch retrieval results. | [] |
| -mapBatchKey | String | The result mapping key, which corresponds to mapBatchKey in the request. | kb1 |
| -kbCode | String | The code of the knowledge base. | xxx |
| -result | List<KbdocRetrieveItem> | The list of retrieval results. | [{"sys data id":"xxx","file _ _ _ code":"yyy","chunk conten _ t":"content","score":0.85}] |

Application integration APIs

| --score | String | For single-engine retrieval, the original engine semantics apply. For hybrid retrieval, scores are normalized for unified evaluation. 1) Single- engine retrieval: retains original engine semantics— vector retrieval uses cosine similarity (0–1), full-text retrieval uses BM25 relevance score. 2) LWS fusion: linear weighted fusion score, normalized. 3) RRF fusion: reciprocal rank fusion score based on ranking. | 0.5 |
|---|---|---|---|
| --sys data id _ _ | String | The unique ID of the data. | 59cc2523-8445-4f3a-91f7- 5e311f5530b2 |
| --file name _ | String | The file name, returned only when needFileInfo is true. | document.pdf |
| --file url _ | String | The file URL, returned only when needFileInfo is true. It includes temporary STS authentication information. | https://example.com/files/d ocument.pdf |
| --file type _ | String | The file type, returned only when needFileInfo is true. | pdf |
| --sys create time _ _ | String | The time when the data was created. | 2023-04-01T12:34:56Z |
| --file code _ | String | The file code, returned only when needFileInfo is true. | 123456 |
| --chunk upload type _ _ | Integer | The upload type. | 1 |
| --chunk content _ | String | The chunk content—the text sent to the LLM as a prompt after recall. |   |
| --show content _ | String | The chunk content—in text form with placeholders for bounding boxes and objects. |   |
| --chunk bboxs _ | List<Object> | The bounding box coordinate information. |   |

Application integration APIs

| ---text bbox _ | List<Double> | The coordinates. | [ 0.3115, 0.0683, 0.0285, 0.372 ] |
|---|---|---|---|
| ---text type _ | String | The type of the text. | docTitle |
| ---text content _ | String | The content of the text. | Guide to HSBC Hong Kong accounts |
| ---page | Integer | The page number. | 1 |
| --start page _ | Integer | The sequence number of the chunk. | 1 |
| --chunk sort number _ _ | Integer | The page number. | 0 |
| --beforeChunks | List<KbdocChunkNeighbor > | The list of N preceding adjacent chunks, returned only when chunkBefore is greater than 0. | [{"sysDataId":"xxx","fileCo de":"yyy","chunkContent":" content"}] |
| --afterChunks | List<KbdocChunkNeighbor > | The list of N following adjacent chunks, returned only when chunkAfter is greater than 0. | [{"sysDataId":"xxx","fileCo de":"yyy","chunkContent":" content"}] |
| --neighborChunkContents | List<String> | The list of adjacent chunk content, returned only when withNeighborChunks is true. | ["previous chunk content","retrieved chunk content","next chunk content"] |
| -metrics | Object | The performance metrics. | {} |
| --kbCode | String | The code of the knowledge base. | xxx |
| --totalTime | Long | The total retrieval time in milliseconds. | 150 |
| --chunksCount | Integer | The number of returned chunks. | 10 |
| --fusionType | String | The type of fusion method. | lws |
| --rrfTime | Long | The RRF fusion time in milliseconds (present only during RRF fusion). | 20 |

Application integration APIs

| --lwsTime | Long | The LWS fusion time in milliseconds (present only during LWS fusion). | 15 |
|---|---|---|---|
| --fillTime | Long | The time taken to fill additional information, in milliseconds. | 30 |
| --retrievalDetails | List<Object> | The detailed retrieval metrics. | [] |
| ---kbIndexCode | String | The code of the index. | ozqn95a5936ycwkl |
| ---engineType | String | The type of the engine. | builtin vector _ |
| ---embeddingTime | Long | The vector embedding time in milliseconds. | 50 |
| ---vectorRecallTime | Long | The vector recall time in milliseconds. | 80 |
| ---textQueryTime | Long | The full-text query time in milliseconds. | 60 |
| ---retrievedChunksCount | Integer | The number of chunks actually recalled by the engine. | 10 |
| -success | Boolean | Indicates whether the retrieval succeeded. | true |
| -errorMessage | String | The error message, returned only when retrieval fails. | The knowledge base does not exist. |
| errorCode | String | The error code. | 401 |
| errorMsg | String | The error description. | Error. |

**Response example**

Application integration APIs

```json
{"success":true,"data":[{"mapBatchKey":"ozqn95a5936y","kbCode":"ozqn95a5936y","result": [{"sys_data_id":"59cc2523-8445-4f3a-91f7- 5e311f5530b2","file_code":"89549201e6e24b0f83a328863701b593","chunk_content":"xxxxxxxxxxxx","score":0.5} {"sys_data_id":"ab4a788d-889e-4916-bc53d09ae943c12d","file_code":"89549201e6e24b0f83a328863701b593","chunk_content":"xxxxxxxxxxxx","score":0.5} {"sys_data_id":"fe422a14-cecf-4fe8-a8ec- 1ae9c8760a21","file_code":"89549201e6e24b0f83a328863701b593","chunk_content":"xxxxxxxxxxxx","score":0}], trics": {"kbCode":"ozqn95a5936y","totalTime":220,"chunksCount":3,"fusionType":"LWS","rrfTime":null,"lwsTime":0," lTime":0,"retrievalDetails": [{"kbIndexCode":"ozqn95a5936ysvdl","engineType":"builtin_es","embeddingTime":null,"vectorRecallTime":nul textQueryTime":21,"retrievedChunksCount":1}, {"kbIndexCode":"ozqn95a5936ycwkl","engineType":"builtin_vector","embeddingTime":153,"vectorRecallTime":3 textQueryTime":null,"retrievedChunksCount":2}]},"success":true,"errorMessage":null}],"errorCode":null,"e rMsg":null,"traceId":null,"env":null,"ext":null}
```

**Status codes**

| HTTP status code | Error description | Error explanation |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | A required parameter for the gateway is missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed. The APP KEY is invalid. _ |
| 401 | GATEWAY APP KEY ALREADY EXPIRED! _ | Authentication failed. The APP KEY has expired. _ |
| 401 | GATEWAY ROLE NOT MATCH! | Authentication failed. The role associated with the current APP KEY user does not match. _ |
| 401 | GATEWAY ROLE HAS EXPIRED! | Authentication failed. The role associated with the current APP KEY user has expired. _ |
| 403 | GATEWAY APP PATH NOT FOUND! _ | The service invocation path is invalid. |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service invocation path is not registered. |
| 429 | GATEWAY LIMIT ! | The service has triggered rate limiting. Try again later. |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | The service has triggered rate limiting. Try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSING! | A required business parameter is missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The workspace code passed does not match the workspace code associated with the APP KEY user. _ |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. The authentication method is not supported. |

Application integration APIs

| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | Authentication failed. The AK user information does not match. |
|---|---|---|
| 401 | GATEWAY AUTH USER ROLE WRONG! _ _ | Authentication failed. The user role does not match. |
| 404 | GATEWAY ROUTE URL NOT FOUND! | The target service address is invalid. |
| 401 | GATEWAY LIMIT ! | The service connection limit has been reached. Try again later. |
| 500 | TARGET SERVICE ERROR CONNECTION _ _ _ _ REFUSE EXCEPTION _ | The target service refused the connection. |
| 500 | TARGET SERVICE ERROR NO RESPONSE _ _ _ _ EXCEPTION _ | The target service did not respond. |

**2.2.2.5. Data table knowledge base retrieval service**

**Overview**

This service searches for vectors or text in an indexed data table within a knowledge base. You can view the request example and click the Test button next to the cURL command to test the service invocation.

**Prerequisites (View APP_KEY)**

Go to Homepage > Profile Picture > APP_KEY to create an APP_KEY. Then, go to Homepage > Profile Picture > Workspace Management to obtain the code of the target workspace. If you cannot see the Workspace Management menu, contact the tenant administrator or the administrator of the target workspace.

**API endpoint**

POST http://ibp-studio-daily.aegmp.com/gateway/dext/api/retrieve/v1/search

**Request parameters**

Header parameters

| Field | Data type | Required | Description | Example |
|---|---|---|---|---|
| Authorization | String | Yes | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | Yes | Content-Type | application/json |
| x-sfm- workspacecode | String | Yes | The target workspace. | your workspace cod _ _ e |

Body parameters

| Field | Data type | Required | Description | Example |
|---|---|---|---|---|
| dataPortfolioCode | String | Yes | The code of the knowledge base. | 82168c22b87d494cb 9b5e813e215ae9b |

Application integration APIs

| domainName | String | Yes | The domain name in the knowledge base. Valid values: table (table and column information), value, knowledge, biSample (sample library/ICL), and dimension. | table |
|---|---|---|---|---|
| query | String | Yes | The text content of the query. | West Lake District |
| returnNum | Integer | Yes | The number of results to return. The maximum value is 100. | 10 |
| score | Double | Yes | The score threshold for filtering results. |   |
| storeEngine | String | Yes | The index type. Valid values: vector and text. | vector |
|   |   |   |   | domain: knowledge, storeEngine: vector { "domainFilters":{ "scopeOfAllTables":f alse, "category":"Glossary Explanation", "tableCodes": ["e5e66de1d72a48b ab699a599dcf78040 "], "columnCodes": ["e5e66de1d72a48b ab699a599dcf78040 "] } } domainFilters parameter descriptions: scopeOfAllTables: false specifies that the search is not across the entire knowledge base. true specifies that the search is across the entire knowledge base. category: The knowledge group. tableCodes: The table codes. These are obtained from the knowledge base table API and represent the tables related to this piece of knowledge. columnCodes: The |

Application integration APIs

| domainFilters | JSONObject | No | The filter parameters supported for a specific domain. The supported search scope varies by domain. For more information about the supported scopes, see the examples. | field codes. These are obtained from the knowledge base field API and represent the fields related to this piece of knowledge. domain: value, storeEngine: text { "domainFilters":{ "tableCodes": ["66024e2bf01541d a93e3bd04cdf946a5 "], "columnCodes": ["758f112ee7a84f46 84dd5a893ddf1430" ] } } domainFilters parameter descriptions: tableCodes: The |
|---|---|---|---|---|
|   |   |   |   | table codes. These are obtained from the knowledge base table API and represent the tables where this value is located. columnCodes: The field codes. These are obtained from the knowledge base field API and represent the fields where this value is located. domain: dimension, storeEngine: text { "domainFilters":{ "dimDsCodes": ["3c2e30a6873b471 7890e0adf3c70781c "] } } domainFilters parameter descriptions: dimDsCodes: The dimension table codes. These are obtained from the `refDims` response parameter of the field API. |

**Response parameters**

| Field | Data type | Description | Example |
|---|---|---|---|
| success | boolean | Indicates whether the API call was successful. | true |
| data | Object | The data node. |   |

Application integration APIs

| items | JSONArray | The list of data returned by the retrieval. | true |
|---|---|---|---|
| score | Double | A floating-point number that indicates the sorting score. A larger value indicates a higher similarity. | 0.334 |
| content | String | The retrieved text content. | Workshop 2 of XX Factory |
|   |   |   | table (table and column information) { "resources": { "schema": { "tables": [ { "table": { "columns": [ { "columnComment": "Team Name", "columnCode": "083b4109b21a4c58b555e 6885a320667", "columnName": "team name" _ } ], "tableCode": "2dda169434a342f6b6233 940e69c883a", "tableName": "llm dev inventory" _ _ } } ] } } } Parameter descriptions: tableCode: The table code. tableName: The original table name. columnCode: The field code. columnName: The original field name. columnComment: The field comment. The system prioritizes manually modified comments from the UI. Otherwise, it uses the corresponding comment from the source database. value { "resources": { "value": { "columnCode": "eb19cfa9308b467c8fda8b c3ef84380c", "value": { "value": "John Doe" }, "tableName": "llm dev input inventory", _ _ _ "columnName": "alias" } |

Application integration APIs

| resources | JSONObject | The structured data where the retrieved text content is located. The structure varies for different domains. See the examples. | } } Parameter descriptions: columnCode: The field code. value: The actual value in the source database. tableName: The original table name. columnName: The original field name. knowledge { "resources": { "knowledge": { "code": "ec231f17cfbc40e08afef23 c066c2d37", "name": "John Doe's Team", "refRes": { "schema": { "columnCodes": [], "tables": [], "allTables": true, "tableCodes": [] } }, "content": "R&D group, supervised by John Doe" } } } Parameter descriptions: code: The system code for this piece of knowledge. name: The name of the knowledge. content: The content of the knowledge. refRes: The resources attached to this piece of knowledge. For more |
|---|---|---|---|
|   |   |   | information, see the description of the `refRes` node in the Expert Knowledge section of the "Query knowledge base resources" topic. biSample (sample library/ICL) { "resources": { "biSample": { "code": "9fa48139fc6043889856a0 6332e64e01", "query": "What was the overall manpower status last week?", "sql": "select project name _ , sum(actual input) from _ llm dev inventory where _ _ week start >= _ DATE SUB(CURRENT DATE _ _ , INTERVAL 7 day) group by project name" _ } } } Parameter descriptions: code: The system code for this sample. query: The query in the sample library, such as 'Find the highest score'. sql: The SQL statement in |

Application integration APIs

|   |   |   | the sample library, such as 'select max(score) from exam;'. dimension { "resources": { "dimension": { "dimDsCode": "9fa48139fc6043889856a0 6332e64e01", "key": "1", "value": "Male" } } } Parameter descriptions: dimDsCode: The code corresponding to the dimension table in the knowledge base. key: The corresponding dimension key, such as '1'. value: The corresponding dimension value, such as 'Male'. |
|---|---|---|---|

**Request example**

```json
curl -X 'POST' http://ibp-studio-daily.aegmp.com/gateway/dext/api/retrieve/v1/search \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'x-sfm-workspacecode: test' \ -H 'Content-Type: application/json' \ -d '{
    "dataPortfolioCode":"543eec8256cf40418d18c009ad9b319b",
    "domainName":"dimension",
    "query":"Company",
    "returnNum":10,
    "score":0.52,
    "domainFilters":{
        "dimDsCodes":["3c2e30a6873b4717890e0adf3c70781c"]
```

`},`

```json
    "storeEngine":"text"
```

`}'`

**Response example**

Application integration APIs

```json
    "success": true,
    "data": [
            "score": 1.0809742,
            "indexCode": "94bff03a24df40138044a5da0e601cff",
            "dataPortfolioCode": "543eec8256cf40418d18c009ad9b319b",
            "domainName": "dimension",
            "content": "China Resources Land Limited",
            "contentIndex": 0,
            "sysTag": null,
            "resources": {
                "dimension": {
                    "dimDsName": "3c2e30a6873b4717890e0adf3c70781c",
                    "dimDsCode": "3c2e30a6873b4717890e0adf3c70781c",
                    "value": "China Resources Land Limited",
                    "key": "China Resources Land Limited"
```

`},`

```json
            "tag": null,
            "version": null
```

`},`

```json
            "score": 1.0809742,
            "indexCode": "e4d32d35aca84ee18d940a5d411b5453",
            "dataPortfolioCode": "543eec8256cf40418d18c009ad9b319b",
            "domainName": "dimension",
            "content": "Country Garden Holdings Company Limited",
            "contentIndex": 0,
            "sysTag": null,
            "resources": {
                "dimension": {
                    "dimDsName": "3c2e30a6873b4717890e0adf3c70781c",
                    "dimDsCode": "3c2e30a6873b4717890e0adf3c70781c",
                    "value": "Country Garden Holdings Company Limited",
                    "key": "Country Garden Holdings Company Limited"
```

`},`

```json
            "tag": null,
            "version": null
```

`],`

```json
    "errorCode": null,
    "errorMsg": null,
    "traceId": null,
    "env": null,
    "ext": null
```

**Status code descriptions**

Gateway exception status codes

| HTTP status code | Error message | Fault description |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | A required gateway parameter is missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed. The APP KEY is _ invalid. |

Application integration APIs

| 401 | GATEWAY APP KEY ALREADY EXPIRE _ D! | Authentication failed. The APP KEY _ has expired. |
|---|---|---|
| 403 | GATEWAY APP PATH NOT FOUND! _ | The service invocation path is invalid. |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service invocation path is not registered. |
| 429 | GATEWAY LIMIT ! | The service has triggered rate limiting. Try again later. |
| 403 | The gateway header parameter is missing. | A required business parameter is missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The provided workspace code does not match the workspace code associated with the user who owns the APP KEY. _ |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. The authentication method is not supported. |
| 401 | GATEWAY AUTH USER NOT MATCH W _ RONG! | Authentication failed. The AK user information does not match. |
| 401 | GATEWAY AUTH USER ROLE WRONG _ _ ! | Authentication failed. The user role does not match. |
| 404 | GATEWAY ROUTE URL NOT FOUND! | The target service endpoint is invalid. |
| 401 | GATEWAY LIMIT ! | The maximum number of service connections has been reached. Try again later. |
| 500 | TARGET SERVICE ERROR CONNECTI _ _ _ ON REFUSE EXCEPTION _ _ | The target service denied the connection. |
| 500 | TARGET SERVICE ERROR NO RESPO _ _ _ _ NSE EXCEPTION _ | The target service did not respond. |

**2.2.2.6. Query resources in a data table knowledge base -**

**Tables**

**API overview**

Use this API to query the details of tables attached to a specified knowledge base. You can review the request example and click the test button to the right of the curl command example to test the API call.

**Prerequisites**

Go to Homepage > Profile Picture > APP_KEY to create an APP_KEY. Then, go to Homepage > Profile Picture > Workspace Management to obtain the code of the target workspace. If the Workspace Management menu is not visible, contact the tenant administrator or the administrator of the target workspace. Application integration APIs

**API endpoint**

POST http://ibp-studio-daily.aegmp.com/gateway/dext/api/dp/refRes/schema/listTablesWithRelatedInfo

**Request parameters**

Header parameters

| Field | Data type | Required | Description | Example |
|---|---|---|---|---|
| Authorization | String | Yes | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | Yes | Content-Type | application/json |
| x-sfm- workspacecode | String | Yes | The target workspace. | your workspace cod _ _ e |

Body parameters

| Field | Data type | Required | Description | Example |
|---|---|---|---|---|
| dpCode | String | Yes | The code of the knowledge base. | 82168c22b87d494cb 9b5e813e215ae9b |
| current | Integer | Yes | The current page number. | 1 |
| pageSize | Integer | Yes | The number of entries per page. The value cannot exceed 1000. | 10 |

**Response parameters**

| Field | Data type | Description | Example |
|---|---|---|---|
| success | boolean | Indicates whether the API call was successful. | true |
| data | JSONObject | The data node. |   |
| total | Integer | The total number of entries. | 100 |
| list | JSONArray | The list of data returned by the query. | true |
| dpCode | String | The ID of the knowledge base. | 2688caccbe93fdd26b6619 5ebf7c1f2d |
| tableCode | String | The code of the table. This code is globally unique in the database. | ca2cbfb7928d59547a3a28 a044467b15 |

Application integration APIs

| tableName | String | The original table name. | tbl student _ |
|---|---|---|---|
| tableCommentExt | String | The comment for the table. The system gives priority to comments that are manually modified on the page. Otherwise, the system uses the corresponding comment from the source database. | Student table |

**Request example**

```json
curl -X 'POST' http://ibp-studiodaily.aegmp.com/gateway/dext/api/dp/refRes/schema/listTablesWithRelatedInfo \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'x-sfm-workspacecode: test' \ -H 'Content-Type: application/json' \ -d '{
    "dpCode": "543eec8256cf40418d18c009ad9b319b",
    "pageSize": 1000,
    "current": 1
```

`}'`

**Response example**

```json
    "success": true,
    "data": {
        "total": 2,
        "list": [
                "dpCode": "543eec8256cf40418d18c009ad9b319b",
                "tableCode": "66024e2bf01541da93e3bd04cdf946a5",
                "tableName": "dwd_mat_voucher",
                "tableCommentExt": "Material voucher"
```

`},`

```json
                "dpCode": "543eec8256cf40418d18c009ad9b319b",
                "tableCode": "b3856941fbe0462b9b9e3dcb95d79886",
                "tableName": "zfsc_spzz_xs_qg_y",
                "tableCommentExt": "Housing market_Commercial residential sales_Monthly, source: Nation
al Bureau of Statistics"
```

`],`

```json
        "pageSize": 1000,
        "current": 1
```

`},`

```json
    "errorCode": null,
    "errorMsg": null,
    "traceId": null,
    "env": null,
    "ext": null
```

**Status codes**

Gateway error status codes

| HTTP status code | Error description | Fault description |
|---|---|---|

Application integration APIs

| 401 | GATEWAY APP KEY MISSING! _ | A required gateway parameter is missing. |
|---|---|---|
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed. The APP KEY is _ invalid. |
| 401 | GATEWAY APP KEY ALREADY EXPIRE _ D! | Authentication failed. The APP KEY _ has expired. |
| 403 | GATEWAY APP PATH NOT FOUND! _ | The service invocation path is invalid. |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service invocation path is not registered. |
| 429 | GATEWAY LIMIT ! | The service has triggered rate limiting. Try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSI NG! | A required business parameter is missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The provided workspace code does not match the workspace code associated with the user who owns the APP KEY. _ |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. The authentication method is not supported. |
| 401 | GATEWAY AUTH USER NOT MATCH W _ RONG! | Authentication failed. The user information does not match. |
| 401 | GATEWAY AUTH USER ROLE WRONG _ _ ! | Authentication failed. The user role does not match. |
| 404 | GATEWAY ROUTE URL NOT FOUND! | The target service endpoint is invalid. |
| 401 | GATEWAY LIMIT ! | The maximum number of service connections has been reached. Try again later. |
| 500 | TARGET SERVICE ERROR CONNECTI _ _ _ ON REFUSE EXCEPTION _ _ | The target service refused the connection. |
| 500 | TARGET SERVICE ERROR NO RESPO _ _ _ _ NSE EXCEPTION _ | The target service did not respond. |

**2.2.2.7. Query data table knowledge base resources - Fields**

**API overview**

Use this API to query the details of fields in a specified table of a knowledge base. To test the API call, you can view the request example and click the Test button next to the cURL command example. Application integration APIs

**Prerequisites**

Go to Homepage > Profile Picture > APP_KEY and create an APP_KEY. Then, go to Homepage > Profile Picture
> Workspace Management to obtain the code for the target workspace. If the Workspace Management menu
is not visible, contact the tenant administrator or the administrator of the target workspace.

**Request URL**

POST http://ibp-studio-daily.aegmp.com/gateway/dext/api/dp/refRes/schema/listColumnsWithRelatedInfo

**Request parameters**

Header parameters

| Field | Data type | Required | Description | Example |
|---|---|---|---|---|
| Authorization | String | Yes | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | Yes | Content-Type | application/json |
| x-sfm- workspacecode | String | Yes | The target workspace. | your workspace cod _ _ e |

Body parameters

| Field | Data type | Required | Description | Example |
|---|---|---|---|---|
| dpCode | String | Yes | The code of the knowledge base. | 82168c22b87d494cb 9b5e813e215ae9b |
| tableCode | String | Yes | The code of the table. | 6174366442861c02 3cba74c26321cd8a |
| current | Integer | Yes | The current page number. | 1 |
| pageSize | Integer | Yes | The number of entries per page. The value cannot exceed 1000. | 10 |

**Response parameters**

| Field | Data type | Description | Example |
|---|---|---|---|
| success | boolean | Indicates whether the API call was successful. | true |
| data | JSONObject | The data node. |   |
| total | Integer | The total number of entries. | 100 |
| list | JSONArray | The list of data returned by the retrieval. | true |

Application integration APIs

| dpCode | String | The ID of the knowledge base. | 2688caccbe93fdd26b6619 5ebf7c1f2d |
|---|---|---|---|
| tableCode | String | The code of the table. | ca2cbfb7928d59547a3a28 a044467b15 |
| columnCode | String | The code of the field. | ca2cbfb7928d59547a3a28 a044467b15 |
| columnName | String | The original name of the field. | col student name _ _ |
| columnCommentExt | String | The comment for the field. The system prioritizes manually modified comments from the page. If no manual comment exists, it uses the corresponding comment from the source database. | Student Name |
| tags | JSONObject | The extension configuration maintained in the knowledge base, in key:value format. | {"Recall with table":"Yes"} |
| refDims.dims[*] | JSONArray | The associated dimensions. This is a deep JSONPath expression. |   |
| code | String | The code of the dimension table. |   |
| name | String | The name of the dimension table. |   |
| refDimType | Integer | Related Dimensions |   |

**Request example**

```json
curl -X 'POST' http://ibp-studiodaily.aegmp.com/gateway/dext/api/dp/refRes/schema/listColumnsWithRelatedInfo \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'x-sfm-workspacecode: test' \ -H 'Content-Type: application/json' \ -d '{
    "dpCode":"094107a115f64f5c8770aa1c3a0d0c3c",
    "tableCode":"08dc4cbfef7c477e8ab9f50417678fd4"
```

`}'`

**Response example**

Application integration APIs

```json
    "success": true,
    "data": {
        "total": 20,
        "list": [
                "dpCode": "094107a115f64f5c8770aa1c3a0d0c3c",
                "tableCode": "08dc4cbfef7c477e8ab9f50417678fd4",
                "columnCode": "e5e66de1d72a48bab699a599dcf78040",
                "columnName": "student_name",
                "columnCommentExt": "Student Name",
                "tags": {
                    "Recall with table": "Yes"
```

`},`

```json
                "includeValue": 0,
                "refDims": {
                    "dims": [
                            "code": "0d57e22c692a4c83a4de24fb1bb064b9",
                            "name": "Student List Table",
                            "refDimType": 1
```

`]` `},`

```json
                "dpCode": "094107a115f64f5c8770aa1c3a0d0c3c",
                "tableCode": "08dc4cbfef7c477e8ab9f50417678fd4",
                "columnCode": "e911596b0c8648378b41c22fcdabe7e8",
                "columnName": "score",
                "columnCommentExt": "Exam Score",
                "tags": null,
                "includeValue": 0,
                "refDims": null
```

`],`

```json
        "pageSize": 10,
        "current": 1
```

`},`

```json
    "errorCode": null,
    "errorMsg": null,
    "traceId": null,
    "env": null,
    "ext": null
```

**Status Code Descriptions**

Gateway error status codes

| HTTP status code | Error description | Meaning |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | A required gateway parameter is missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed. The APP KEY is _ invalid. |

Application integration APIs

| 401 | GATEWAY APP KEY ALREADY EXPIRE _ D! | Authentication failed. The APP KEY _ has expired. |
|---|---|---|
| 403 | GATEWAY APP PATH NOT FOUND! _ | The service invocation path is invalid. |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service invocation path is not registered. |
| 429 | GATEWAY LIMIT ! | The service has triggered rate limiting. Try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSI NG! | A required business parameter is missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The provided workspace code does not match the workspace code associated with the APP KEY owner. _ |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. The authentication method is not supported. |
| 401 | GATEWAY AUTH USER NOT MATCH W _ RONG! | Authentication failed. The AccessKey user information does not match. |
| 401 | GATEWAY AUTH USER ROLE WRONG _ _ ! | Authentication failed. The user role does not match. |
| 404 | GATEWAY ROUTE URL NOT FOUND! | The target service endpoint is invalid. |
| 401 | GATEWAY LIMIT ! | The maximum number of service connections has been reached. Try again later. |
| 500 | TARGET SERVICE ERROR CONNECTI _ _ _ ON REFUSE EXCEPTION _ _ | The target service denied the connection. |
| 500 | TARGET SERVICE ERROR NO RESPO _ _ _ _ NSE EXCEPTION _ | The target service did not respond. |

**2.2.2.8. Query expert knowledge resources in a data table**

**knowledge base**

**API overview**

You can use this API to query expert knowledge resources attached to a specified knowledge base. You can view the request example and click the test button next to the cURL command example to test the API call.

**Prerequisites (View APP_KEY)**

First, go to Homepage > Profile Picture > APP_KEY to create an APP_KEY. Then, go to Homepage > Profile Picture > Workspace Management to obtain the target workspace code. If the Workspace Management menu is not visible, contact the tenant administrator or the target workspace administrator. Application integration APIs

**API endpoint**

POST http://ibp-studio-daily.aegmp.com/gateway/dext/api/dp/refRes/flexExt/list

**Request parameters**

Header parameters

| Field | Data type | Required | Description | Example |
|---|---|---|---|---|
| Authorization | String | Yes | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | Yes | Content-Type | application/json |
| x-sfm- workspacecode | String | Yes | Target workspace | your workspace cod _ _ e |

Body parameters

| Field | Data type | Required | Description | Example |
|---|---|---|---|---|
| dpCode | String | Yes | Knowledge base code | 82168c22b87d494cb 9b5e813e215ae9b |
| current | Integer | Yes | Current page number | 1 |
| pageSize | Integer | Yes | Page size. Cannot exceed 1000. | 10 |
| scopeOfAllTables | Boolean | No | Specifies whether to filter for the entire knowledge base. `null`: No limit. `true`: Filters at the entire knowledge base level. `false`: Filters at a level other than the entire knowledge base. | true |
| tableCodes | String[] | No | Filter item. The `tableCodes` that contain table-level and column-level knowledge. |   |
| columnCodes | String[] | No | Filter item. The `columnCodes` that contain column-level knowledge. |   |
| categories | String[] | No | Filter item. The knowledge group. |   |

**Response parameters**

Application integration APIs

| Field | Data type | Description | Example |
|---|---|---|---|
| success | boolean | Indicates whether the API call was successful. | true |
| data | JSONObject | Data node. |   |
| total | Integer | Total number of entries. | 100 |
| list | JSONArray | A list of data returned from the query. | true |
| code | String | Knowledge code. | 2688caccbe93fdd26b6619 5ebf7c1f2d |
| name | String | Knowledge name. | Academy |
| content | String | Knowledge content. | This Campus refers to the campus to which the user belongs. |
| refRes | JSONObject | The resource attached to this knowledge item. |   |
| schema | JSONObject | Attached resource: Table. |   |
| allTables | Boolean | Indicates if the scope is the entire knowledge base. A value of `true` means the scope is the entire knowledge base. |   |
| tableCodes | String[] | The `tableCodes` that contain all table-level and column-level knowledge within `tables`. |   |
| columnCodes | String[] | The `columnCodes` that contain all column-level knowledge within `tables`. |   |
| tables | JSONObject | The scope of attached table-level and column- level knowledge. This is consistent with `resources.schema.tables` when `domain=table`. |   |

**Example request**

Application integration APIs

```json
curl -X 'POST' http://ibp-studio-daily.aegmp.com/gateway/dext/api/dp/refRes/flexExt/list \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'x-sfm-workspacecode: test' \ -H 'Content-Type: application/json' \ -d '{
    "current":1,
    "pageSize":10,
    "dpCode":"094107a115f64f5c8770aa1c3a0d0c3c",
    "scopeOfAllTables":true,
    "tableCodes":["08dc4cbfef7c477e8ab9f50417678fd4"],
    "columnCodes":["e5e66de1d72a48bab699a599dcf78040"],
    "categories":["Calculation Method"]
```

`}'`

**Example response**

Application integration APIs

```json
    "success": true,
    "data": {
        "total": 1,
        "list": [
                "code": "263a188399a24bb282c7325b40d4a231",
                "name": "This Campus",
                "content": "This Campus refers to the campus to which the user belongs.",
                "datasourceCode": "5ca9ab2356b8419094983535587e5d03",
                "tags": null,
                "refRes": {
                    "schema": {
                        "allTables": false,
                        "tables": [
                                "tableCode": "08dc4cbfef7c477e8ab9f50417678fd4",
                                "tableName": "Campus Dictionary Table",
                                "allColumns": false,
                                "columns": [
                                        "columnCode": "e5e66de1d72a48bab699a599dcf78040",
                                        "columnName": "Campus Name"
```

`]` `],`

```json
                        "tableCodes": [
                            "08dc4cbfef7c477e8ab9f50417678fd4"
```

`],`

```json
                        "columnCodes": [
                            "e5e66de1d72a48bab699a599dcf78040"
```

`]` `],`

```json
        "pageSize": 10,
        "current": 1
```

`},`

```json
    "errorCode": null,
    "errorMsg": null,
    "traceId": null,
    "env": null,
    "ext": null
```

**Status code descriptions**

Status codes for gateway exceptions

| HTTP status code | Error description | Fault description |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | A required gateway parameter is missing. |
| 401 | GATEWAY APP KEY WRONG! _ | Authentication failed. The APP KEY is _ invalid. |

Application integration APIs

| 401 | GATEWAY APP KEY ALREADY EXPIRE _ D! | Authentication failed. The APP KEY is _ expired. |
|---|---|---|
| 403 | GATEWAY APP PATH NOT FOUND! _ | The service invocation path is invalid. |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | The current service invocation path is not registered. |
| 429 | GATEWAY LIMIT ! | The service has triggered rate limiting. Try again later. |
| 403 | GATEWAY HEADER PARAMETER MISSI NG! | A required business parameter is missing. |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | The provided workspace code does not match the workspace associated with the APP KEY. _ |
| 401 | GATEWAY AUTH TYPE WRONG! _ | Authentication failed. The authentication method is not supported. |
| 401 | GATEWAY AUTH USER NOT MATCH W _ RONG! | Authentication failed. The user information for the AK does not match. |
| 401 | GATEWAY AUTH USER ROLE WRONG _ _ ! | Authentication failed. The user role does not match. |
| 404 | GATEWAY ROUTE URL NOT FOUND! | The target service endpoint is invalid. |
| 401 | GATEWAY LIMIT ! | The maximum number of service connections has been reached. Try again later. |
| 500 | TARGET SERVICE ERROR CONNECTI _ _ _ ON REFUSE EXCEPTION _ _ | The target service refused the connection. |
| 500 | TARGET SERVICE ERROR NO RESPO _ _ _ _ NSE EXCEPTION _ | The target service is not responding. |
