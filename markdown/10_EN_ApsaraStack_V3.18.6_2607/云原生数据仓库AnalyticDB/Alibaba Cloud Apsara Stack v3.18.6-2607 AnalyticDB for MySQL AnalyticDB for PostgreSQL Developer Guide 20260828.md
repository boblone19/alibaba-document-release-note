---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 AnalyticDB for MySQL AnalyticDB for PostgreSQL Developer Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 90
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 AnalyticDB for MySQL AnalyticDB for PostgreSQL Developer Guide 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E5%8E%9F%E7%94%9F%E6%95%B0%E6%8D%AE%E4%BB%93%E5%BA%93AnalyticDB/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20AnalyticDB%20for%20MySQL%20AnalyticDB%20for%20PostgreSQL%20Developer%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 AnalyticDB for MySQL AnalyticDB for PostgreSQL Developer Guide 20260828

## Getting started

### Usage notes on development

**documentation**

This topic describes how to view the desired product development documentation when you use Apsara Stack API (ASAPI).

**Procedure**

You can follow the procedure described in the following figure to view the desired development documentation.

**Prerequisites**

The Apsara Stack version is obtained from an O&M personnel or operations administrator.

**Procedure**

You can go to the Apsara Stack documentation center and view the desired product documentation.
1. Go to the Apsara Stack Documentation Centerpage by using a browser.
2. Click the **Enterprise**, **Agility**, or **All-in-one** tab based on the Apsara Stack version that you
use.
3. Select an Apsara Stack version from the drop-down list.
4. In the left-side navigation pane, select the name of the product that you want to view.
5. In the upper-right corner of the product documentation section, click **View Details** or
**Download PDF**.

### Process of API calls

Apsara Stack allows you to call API operations by using the Portable OpenAPI Proxy (POP) gateway or the Apsara Stack API (ASAPI) gateway. To ensure that Apsara Stack provides the same experience as the public cloud, API operations in Apsara Stack are called by using the POP gateway by default starting from Apsara Stack Enterprise V3.16.0. This topic describes how to call API operations in Apsara Stack by using the POP gateway.

**Note**

You can continue to use the ASAPI gateway to call API operations in Apsara Stack that is earlier than V3.16.0. For more information, see Process of API calls by using the ASAPI gateway, Generate an endpoint for ASAPI, and Obtain Apsara Stack SDKs.

**Procedure**

1. Obtain AccessKey credentials.
Obtain the AccessKey credentials that are required for calling an API operation. For more information, see Obtain an AccessKey pair or Obtain an STS AccessKey 3-tuple.

**Note**

We recommend that you use an AccessKey pair or an STS AccessKey 3-tuple of a personal account to call the API operations of the Apsara Uni-manager Management Console and cloud services.
2. Obtain the region ID.
For more information, see Obtain common header parameters.
3. Obtain the organization ID and resource set ID.
You can call the GetOrganizationList operation to obtain the organization ID. For more information, see GetOrganizationList in Apsara Uni-manager Management Console Develop er Guide. You can call the ListResourceGroup operation to obtain the resource set ID. For more information, see ListResourceGroup in Apsara Uni-manager Management Console Develope r Guide.

**Note**

When you call an API operation, set the `<x-acs-organizationid>` parameter to the organization ID that you obtained, and set the `<x-acs-resourcegroupid>` parameter to the resource set ID that you obtained. This way, you can query resources in the specified organization and resource set. If you do not set the `<x-acs-organizationid>` parameter, the ID of the organization to which the current user belongs is used by default. If you do not set the `<x-acs-resourcegroupid>` parameter, this parameter is left empty by default. If you specify a resource set, you must also specify an organization ID.
4. View the developer guide of the cloud service that you want to use to learn how to make
the API call. View the developer guide of the cloud service that you want to use. This way, you can learn the features of API operations and how to call the API operations. For more information, see Usage notes on development documentation.
5. Obtain the endpoint of the cloud service.
6. Obtain an SDK of the cloud service and call an API operation.

## Preparations

### Log on to the API Tool console

You can log on to the API Tool console from the Apsara Uni-manager Management Console.

**Prerequisites**

Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment personnel. A browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press Enter.
2. Enter your username and password.
Obtain the username and password that are used to log on to the Apsara Uni-manager Management Console from the operations administrator.

**Note**

When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, which include ! @ # $ %
3. Click **Log On**.
4. If your account has multi-factor authentication (MFA) enabled, perform corresponding
operations in the following scenarios: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device. Enter a six-digit MFA verification code and click **Authenticate**.

**Note**

For more information, see the **Bind a virtual MFA device to enable MFA** topic in
**Apsara Uni-manager Management Console User Guide** .
5. In the top navigation bar, choose **Products > Others > API Tool**.

### Obtain the information and

**the endpoint of an API operation**

To call an API operation of a cloud service, you must obtain the information about the operation, including the service code, operation name, and API version.

**Background information**

The API information on the debugging page of the Apsara Uni-manager Management Console is for reference only. For more information about how to call API operations, see the developer guides of cloud services. If the information on the debugging page is different from that in the developer guide of a cloud service, the information in the developer guide prevails.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Application Services** > **OpenAPI**
**Explorer**.
3. On the **OpenAPI Explorer** page, choose **API Integration** > **API Debugging** in the top
navigation bar.
4. In the left-side navigation pane, select the cloud service that you want to manage.
5. Select an API version from the **Version** drop-down list.
6. In the API operation list, you can view all API operations of the current version.
7. Click the operation that you want to call. Obtain the endpoint from the Endpoint parameter
on the Parameter tab.

### Obtain an AccessKey pair

AccessKey credentials are assigned by Resource Access Management (RAM) or Security Token Service (STS). You need to provide only a single type of AccessKey credentials for authentication when you call API operations. This topic describes how to obtain an AccessKey pair that is assigned by RAM.

**Background information**

An AccessKey pair is used to verify the identity of a request sender. An AccessKey pair consists of an AccessKey ID and an AccessKey secret that are used to implement symmetric encryption. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. You can use RAM or STS to assign an AccessKey pair for authentication. An AccessKey pair that is assigned by RAM to a third party consists of an AccessKey ID and an AccessKey secret. An AccessKey 3-tuple that is assigned by STS to a third party consists of an AccessKey ID, an AccessKey secret, and a security token. For more information, see Obtain an STS AccessKey 3-tuple. The Apsara Uni-manager Management Console provides AccessKey pairs to personal accounts or organizations. Only the administrators of level-1 organizations and operations administrators can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the operations provided by the Apsara Unimanager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the header parameters that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions may occur.

**Warning**

The AccessKey pair of a personal account is managed by the permission system of the Apsara Uni-manager Management Console. If you need to obtain the AccessKey pair of an organization, make sure that your operation is allowed by an administrator. This ensures security.

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. Example: cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For more information about how to obtain organization IDs, see GetOrganizationList in Apsara Uni- manager Management Console Developer Guide. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For more information about how to obtain resource set IDs, see ListResourceGroup in Apsara Uni- manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance that you want to manage. If you want to obtain the ID of an Elastic Compute Service (ECS) instance, you can obtain the ID from the ECS instance list. |

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, click the profile picture and then select **User**
**Information**.
3. In the **AccessKey Pair** section, view the AccessKey pair of the personal account.

**Note**

An AccessKey pair consists of an AccessKey ID and an AccessKey secret. These credentials provide full permissions on cloud resources within your account. You must keep the AccessKey pair confidential.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you
want to obtain.
5. Click **Management AccessKey** on the right side of the page.
6. In the dialog box that appears, view the AccessKey pair of the organization.

### Obtain an STS AccessKey 3-

**tuple**

This topic describes how to use Security Token Service (STS) to call API operations in Apsara Stack.

**Background information**

STS allows you to manage temporary credentials to your Apsara Stack resources. You can use STS to call API operations in Apsara Stack. An STS AccessKey 3-tuple consists of an AccessKey ID, an AccessKey secret, and a security token. When you use STS to call API operations, you must specify an STS AccessKey 3-tuple. For more information about STS, see What is STS?

**Procedure**

1. Obtain the `RAM role` .
i. Log on to the Apsara Uni-manager Management Console. ii. Click the profile picture in the upper-right corner of the page and select **User**
**Information**.
iii. Click **View Current Role Policy**. In the **View Policies of Current Role** dialog box, view your `RAM role` .
2. Obtain the STS AccessKey 3-tuple.

**Note**

In the following sample code, replace the parameters with the actual values. Delete the angle brackets (<>) in the final code. Parameters: <yourRegionID>: Replace the parameter with the region ID. <yourAccessKeyID>: Replace the parameter with your AccessKey ID. <yourAccessKeySecret>: Replace the parameter with your AccessKey secret. <yourRoleSessionName>: Replace the parameter with the name of the current session. <yourRoleArn>: Replace the parameter with the Alibaba Cloud Resource Name (ARN) of your RAM role. "sts.aliyuns.com": Replace the parameter with the endpoint of STS.

```java
public static void main(String[] args) {
    // Create and initialize a DefaultAcsClient instance.
    // Specify the region ID, AccessKey ID, and AccessKey secret.
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "
<yourAccessKeyID>", "<yourAccessKeySecret>");
    HttpClientConfig clientConfig = HttpClientConfig.getDefault();
    clientConfig.setIgnoreSSLCerts(true);
    clientConfig.setProtocolType(ProtocolType.HTTPS);
    profile.setHttpClientConfig(clientConfig);
    IAcsClient client = new DefaultAcsClient(profile);
    String assumeRole = callAssumeRole(client);
    if (StringUtils.isEmpty(assumeRole)) return;
    JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
    JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
    // Obtain the STS AccessKey 3-tuple.
    String stsAK = credentials.getString("AccessKeyId");
    String stsSK = credentials.getString("AccessKeySecret");
    String stsToken = credentials.getString("SecurityToken");
private static String callAssumeRole(IAcsClient client) {
    CommonRequest request = new CommonRequest();
    // Replace "sts.aliyuns.com" with the endpoint of STS. Format: sts-
vpc.${global:region}.${global:internet-domain}.
    request.setSysDomain("sts.aliyuns.com");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
    // Replace "<yourRoleSessionName>" with the name of the current session.
    request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
    // Replace "<yourRoleArn>" with the actual ARN that you obtain in the preceding s
tep for the RAM role.
    request.putQueryParameter("RoleArn", "<yourRoleArn>");
    try {
        CommonResponse response = client.getCommonResponse(request);
        return response.getData();
    } catch (ServerException e) {
        System.out.println(e.getErrCode());
        System.out.println(e.getErrMsg());
    } catch (ClientException e) {
        System.out.println(e.getErrCode());
        System.out.println(e.getErrMsg());
    return null;
```

3. Use the AccessKey 3-tuple assigned by STS to call an operation of a service. The following
sample code provides an example on how to use the AccessKey 3-tuple assigned by STS to call the `DescribeZones` operation of Elastic Compute Service (ECS):

**Note**

In the following sample code, replace the parameters with the actual values. Delete the angle brackets (<>) in the final code. Parameters: <yourRegionID>: Replace the parameter with the region ID. <yourStsAccesskeyID>: Replace the parameter with your STS AccessKey ID. <yourStsAccessKeySecret>: Replace the parameter with your AccessKey secret. <yourStsToken>. Replace the parameter with your security token. <yourResourceGroupID>: Replace the parameter with the resource set ID. <yourOrganizationID>: Replace the parameter with the organization ID.

```java
public static void main(String[] args) {
    // Replace "<yourRegionID>" with the region ID.
    // Replace "<yourStsAccessKeyID>" and "<yourStsAccessKeySecret>" with the AccessK
ey ID and AccessKey secret of the 3-tuple obtained in the previous step.
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "
<yourStsAccesskey>", "<yourStsAccessSecret>");
    HttpClientConfig clientConfig = HttpClientConfig.getDefault();
    clientConfig.setIgnoreSSLCerts(true);
    clientConfig.setProtocolType(ProtocolType.HTTPS);
    profile.setHttpClientConfig(clientConfig);
    IAcsClient client = new DefaultAcsClient(profile);
    CommonRequest request = new CommonRequest();
    request.setSysDomain("ecs.aliyuns.com");
    request.setSysProduct("ECS");
    request.setSysAction("DescribeZones");
    request.setSysVersion("2014-05-26");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
    // Replace "<yourRegionID>" with the region ID.
    request.putHeadParameter("x-acs-regionid", "<yourRegionID>");
    // Replace "<yourStsToken>" with the security token of the 3-tuple obtained in th
e previous step.
    request.putQueryParameter("SecurityToken", "<yourStsToken>");
    // Optional. Replace the parameter with the resource set ID.
    // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
    // Required. Replace the parameter with the organization ID.
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

### Obtain common header

**parameters**

When you call API operations, you must provide multiple header parameters. This topic describes how to obtain common header parameters and explains specific response parameters after you call API operations.

**Obtain a region ID**

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources**>**Regions**.
4. Click the name of the organization whose region ID you want to view.
5. View the region ID in the **Regions** on the right.

**Obtain an organization ID**

You can call an API operation to obtain the organization ID. For more information, see the GetOrganizationList section in Apsara Uni-manager Management Console Developer Guide.

**Obtain a resource set ID**

You can call an API operation to obtain the resource set ID. For more information, see the ListResourceGroup section in Apsara Uni-Manager Management Console Developer Guide.

**Obtain an instance ID**

Each cloud service must modify the service name and the procedure for obtaining the instance ID. You can obtain the instance ID from the instance list of a cloud service in the Apsara Unimanager Management Console. The following procedure uses Elastic Compute Service (ECS) as an example:
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products**>**Elastic Computing**>**Elastic Compute**
**Service**.
3. In the left-side navigation pane, click **Instances**.
4. View the **Instance ID** in the instance list.

**Response parameters**

After you call an API operation that is used to query cloud service resource instances, the system returns the following parameters by default.

| Parameter | Description |
|---|---|
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The ID of the resource set. |

| DepartmentName | The name of the organization. |
|---|---|
| Department | The ID of the organization. |

## API reference

### Request structure

To call an API operation, you must send an HTTP GET request to the API endpoint. You must add the request parameters that correspond to the API operation. The processing results are returned in the response.

**Endpoints**

The endpoint of the AnalyticDB for PostgreSQL API is gpdb.aliyuncs.com. For more information about how to obtain the endpoint, see Obtain the endpoint of AnalyticDB for PostgreSQL.

**Protocols**

You can call API operations by sending HTTP or HTTPS requests. To enhance security, we recommend that you send HTTPS requests. Specific password-related API operations support only HTTPS.

**Methods**

You can send requests by using the HTTP GET method. This method requires that you specify request parameters in the request URL.

**Request parameters**

When you make an API request, you must set the Action parameter to the operation (such as CreateDBInstance) that you want to perform. You must also specify common request parameters and operation-specific request parameters.

**Encoding**

Requests and responses are both encoded in UTF-8.

### Common parameters

This topic describes the AnalyticDB for PostgreSQL common parameters.

**Common request parameters**

Common request parameters are parameters that every operation requires. Table 1. Common request parameters

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| Format | String | No | The response format. Valid values: JSON and XML. Default value: XML |
| Version | String | Yes | The version of the API. Specify the version in the YYYY-MM-DD format. Set the value to 2016-05-03. |

| AccessKeyId | String | Yes | The AccessKey ID provided by Alibaba Cloud for you to access services. |
|---|---|---|---|
| Signature | String | Yes | The signature string. For more information about how to calculate the signature, see Signature mechanism. |
| SignatureMethod | String | Yes | The signature algorithm. Set the value to HMAC- SHA1. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in UTC. Format: YYYY-MM-DDThh:mm:ssZ Example: 2019-08-15T12:00:00Z specifies 20:00:00 on August 15, 2019 in China Standard Time. |
| SignatureVersion | String | Yes | The version of the signature algorithm. Set the value to 1.0. |
| SignatureNonce | String | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |

```
https://gpdb.aliyuncs.com/ ?Format=xml &Version=2016-05-03 &Signature=Pcxxxxxxxxxxxxxxxxxxxxxx &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2019-06-01T12:00:00Z
```

**Common response parameters**

The system returns a unique RequestId for every API call, regardless of whether the call succeeds or fails. Example:

```xml
<?xml version="1.0" encoding="utf-8"?> <!—Root node of the response--> <OperationName+Response>
 <!—Request ID tag-->
 <RequestId>4C467B38-3910-447D-87BC-AC**********</RequestId>
 <!—Response data-->
</OperationName+Response>
```

### Responses

API responses use the HTTP response format where a 2xx status code indicates a successful call and a 4xx or 5xx status code indicates a failed call. Responses can be returned in either the JSON or XML format. You can specify the response format in the request. The default response format is XML. The response examples in this topic are formatted with line breaks or indents for a clear view. Actual response data is not formatted in the same manner as these examples.

**Sample success responses**

XML format The XML response includes a message that indicates whether the request is successful and the specific service data. Example:

```xml
<? xml version="1.0" encoding="utf-8"? > <!-The root node of the result--> <API name+Response>
    <!-The returned request tag-->
 <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
    <!-The response data-->
</API name+Response>
```

JSON format `{`

```json
    "RequestId": "4C467B38-3910-447D-87BC-AC049166F216",
    /* The response data */
```

**Sample error responses**

No result is returned after the API call fails. You can locate the cause of the error by referring to the error codes in Appendix. When a request fails, an HTTP response containing an HTTP status code (4xx or 5xx) is returned. The returned message body contains the specific error code and error message. The message body also contains a globally unique RequestId and the HostId of the site you request to access. If you are unable to find the error cause, you can contact Alibaba Cloud customer service and provide the HostId and RequestId to help solve the problem as quickly as possible. XML format

```xml
<? xml version="1.0" encoding="UTF-8"? > <Error>
   <RequestId>8906582E-6722-409A-A6C4-0E7863B733A5</RequestId>
   <HostId>gpdb.example.com</HostId>
   <Code>UnsupportedOperation</Code>
   <Message>The specified action is not supported. </Message>
</Error>
```

JSON format `{`

```json
    "RequestId": "7463B73D-35CC-4D19-A010-6B8D65D242EF",
    "HostId": "gpdb.example.com",
    "Code": "UnsupportedOperation",
    "Message": "The specified action is not supported."
```

### Signature mechanism

AnalyticDB for PostgreSQLThe service authenticates every request. Therefore, whether you submit a request over HTTP or HTTPS, you must include a signature in the request. The system verifies the identity of the sender by using symmetric encryption with an AccessKey ID and an AccessKey Secret. Alibaba Cloud issues the AccessKey ID and AccessKey Secret to users (you can apply for and manage them on the Alibaba Cloud official website). The AccessKey ID identifies the user. The AccessKey Secret encrypts the signature string and serves as the key for the server to verify the signature string. You must keep the AccessKey Secret strictly confidential. Only you and Alibaba Cloud know it.AnalyticDB for PostgreSQL For more information about how to obtain an AccessKey, see Obtain an AccessKey pair. When you access the service, sign your request by performing the following steps:
1. Use the request parameters to construct a canonicalized query string.
i. Sort all request parameters (including common request parameters described in the documentation and custom parameters specific to the requested API operation, but excluding the Signature parameter itself mentioned in common request parameters) in lexicographic order by parameter name.

**Note**

If you use the GET method to submit the request, these parameters constitute the parameter part of the request URI (the part after ? connected by &). ii. Encode the name and value of each request parameter. Use the UTF-8 character set for URL encoding. The URL encoding rules are as follows: Do not encode uppercase letters (A-Z), lowercase letters (a-z), digits (0-9), hyphens (-), underscores (_), periods (.), or tildes (~). Encode other characters in the %XY format, where XY is the hexadecimal representation of the ASCII code of the character. For example, encode the double quotation mark (") as %22. Encode extended UTF-8 characters in the %XY%ZA… format. Note that you must encode the space character as %20, not as a plus sign (+).

**Note**

Libraries that support URL encoding (such as java.net.URLEncoder in Java) typically follow the rules of the application/x-www-form-urlencoded MIME type. To comply with the preceding encoding rules, you can directly use such libraries for encoding and then replace the plus sign (+) with %20, the asterisk (*) with %2A, and %7E with the tilde (~) in the encoded string. iii. Connect the encoded parameter name and value with an equal sign (=). iv. Concatenate the strings connected by equal signs in lexicographic order by parameter name, using ampersands (&) as separators. This produces the canonicalized query string.
2. Use the canonicalized string constructed in the previous step to construct a string for
calculating the signature by following this rule:

```
StringToSign= HTTPMethod + “&" + percentEncode(“/") + "&" + percentEncode(CanonicalizedQueryString)
```

HTTPMethod is the HTTP method used to submit the request, such as GET. percentEncode("/") is the value obtained by encoding the forward slash (/) according to the URL encoding rules described in Step 1.b, which is %2F. percentEncode(CanonicalizedQueryString) is the string obtained by encoding the canonicalized query string constructed in Step 1 according to the URL encoding rules described in Step 1.b.
3. Calculate the HMAC value of the signature by using the string constructed for signature
calculation, as defined in RFC2104.

**Note**

When you calculate the signature, use the AccessKey Secret held by the user appended with an ampersand (&) (ASCII: 38) as the key, and use the SHA-1 hash algorithm.
4. Encode the HMAC value into a string by using Base64 encoding. This produces the
signature value.
5. Add the obtained signature value as the Signature parameter to the request parameters.
This completes the request signing process.

**Note**

When you submit the signature value as the final request parameter value to the GPDB server, encode it according to the rules specified in RFC3986, just like other parameters. For example, before signing, the request URL for DescribeDBInstances is:

```
http://gpdb.example.com/?Timestamp=2013-06-01T10:33:56Z&Format=XML&Acce ssKeyId=testid&Action=DescribeDBInstances&SignatureMethod=HMAC-SHA1&Regi onId=reg ion1&SignatureNonce=NwDAxvLU6tFE0DVb&Version=2014-08-15&Signatur eVersion=1.0
```

The StringToSign is:

```
GET&%2F&AccessKeyId%3Dtestid%26Action%DescribeDBInstances%26Format%3DXML %26RegionId%3Dregion1%26SignatureMethod%3DHMAC-SHA1%26SignatureNonce%3DN wDAxvLU6tFE0DVb%26SignatureVersion%3D1.0%26Timestamp%3D2013-06-01T10%253 A33%253A56Z%26Version%3D2014-08-15
```

Assume that the AccessKey ID is testid and the AccessKey Secret is testsecret. The key used to calculate the HMAC value is testsecret&. The calculated signature value is: GfQRtWbwdE8sp7q9lBgZyutVht8= The signed request URL is (note the added Signature parameter):

```
http://gpdb.example.com/?Timestamp=2012-12-26T10%3A33%3A56Z&Format=XML& AccessKeyId=testid&Action=DescribeDBInstances&SignatureMethod=HMAC-SHA1& RegionId=region1&SignatureNonce=NwDAxvLU6tFE0DVb&Version=2012-09-13&Sign atureVersion=1.0&Signature= Gfxxxxxxxxxxxxxxxxxxxx
```

### RAM authorization

#### Authorize resources by using RAM

All instances you create by using your Alibaba Cloud Account are resources owned by that account. By default, the account has full operation permissions on its own resources. You can use Alibaba Cloud Resource Access Management (RAM) to grant RAM users access and management permissions to resources under your Alibaba Cloud Account.

**Note**

Skip this section if you do not need to use RAM.

#### Resources that can be authorized in

**RAM**

Only one type of AnalyticDB for PostgreSQL resource can be authorized in RAM: DBInstance. The following table lists the descriptions of resources when you use RAM to authorize access permissions to these resources. Table 1. Resource description

| Resource | Resource description in the authorization policy |
|---|---|
| DBInstance | acs:gpdb:$regionid: $accountid:dbinstance/$dbinstanceid acs:gpdb:$regionid:$accountid:dbinstance/* acs:gpdb:* : *:dbinstance/* |

**Note**

$regionid: the ID of a region. Use an asterisk (*) to indicate the ID of any region. $dbinstanceid: the ID of a DBInstance. Use an asterisk (*) to indicate the ID of any instance. $accoutid: the userid of the resource owner. Use an asterisk (*) to indicate the ID of any account.

#### Operations that can be authorized in

**RAM**

You can use Resource Access Management (RAM) to authorize access permissions on AnalyticDB for PostgreSQL resources. All operations except the DescribeRegions operation can be authorized.

#### Authentication rules of API operations

When you call API operations to access AnalyticDB for PostgreSQL resources as a Resource Access Management (RAM) user, AnalyticDB for PostgreSQL checks with RAM whether the RAM user is granted the required permissions. The permissions to be checked are determined by the resources that are used by each API operation. For more information about authentication rules of each API operation, see Authentication rules of API operations. Table 1. Authentication rules of API operations

| Operation | Authorization rule |
|---|---|
| CreateDBInstance | acs:gpdb:$regionid: dbinstance /$* |
| DeleteDBInstance | acs:gpdb:$regionid: $accountid:dbinstance/$dbinstanceid |
| DescribeDBInstanceAttribute | acs:gpdb:$regionid: $accountid:dbinstance/$dbinstanceid |
| DescribeDBInstances | acs:gpdb:$regionid: $accountid:dbinstance/$dbinstanceid |
| DescribeRegions | acs:gpdb:$regionid: $accountid:dbinstance/$dbinstanceid |
| DescribeResourceUsage | acs:gpdb:$regionid: $accountid:dbinstance/$dbinstanceid |
| ModifyDBInstanceConnectionMode | acs:gpdb:$regionid: $accountid:dbinstance/$dbinstanceid |

| ModifyDBInstanceDescription | acs:gpdb:$regionid: $accountid:dbinstance/$dbinstanceid |
|---|---|
| ModifyDBInstanceMaintainTime | acs:gpdb:$regionid: $accountid:dbinstance/$dbinstanceid |
| RestartDBInstance | acs:gpdb:$regionid: $accountid:dbinstance/$dbinstanceid |
| DeleteDatabase | acs:gpdb:$regionid: $accountid:dbinstance/$dbinstanceid |
| DescribeAccounts | acs:gpdb:$regionid: $accountid:dbinstance/$dbinstanceid |
| ModifyAccountDescription | acs:gpdb:$regionid: $accountid:dbinstance/$dbinstanceid |
| CreateAccount | acs:gpdb:$regionid: dbinstance /$* |
| ResetAccountPassword | acs:gpdb:$regionid: $accountid:dbinstance/$dbinstanceid |
| DescribeDBInstanceIPArrayList | acs:gpdb:$regionid: $accountid:dbinstance/$dbinstanceid |
| DescribeDBClusterIPArrayList | acs:gpdb:$regionid: $accountid:dbinstance/$dbinstanceid |
| ModifySecurityIps | acs:gpdb:$regionid: $accountid:dbinstance/$dbinstanceid |
| DescribeSlowLogRecords | acs:gpdb:$regionid: $accountid:dbinstance/$dbinstanceid |
| DescribeSQLCollectorPolicy | acs:gpdb:$regionid: $accountid:dbinstance/$dbinstanceid |
| DescribeSQLLogFiles | acs:gpdb:$regionid: $accountid:dbinstance/$dbinstanceid |
| DescribeSQLLogRecords | acs:gpdb:$regionid: $accountid:dbinstance/$dbinstanceid |
| ModifySQLCollectorPolicy | acs:gpdb:$regionid: $accountid:dbinstance/$dbinstanceid |
| DescribeDBInstancePerformance | acs:gpdb:$regionid: $accountid:dbinstance/$dbinstanceid |
| AllocateInstancePublicConnection | acs:gpdb:$regionid: $accountid:dbinstance/$dbinstanceid |
| DescribeDBInstanceNetInfo | acs:gpdb:$regionid: $accountid:dbinstance/$dbinstanceid |
| ReleaseClusterPublicConnection | acs:gpdb:$regionid: $accountid:dbinstance/$dbinstanceid |
| ModifyDBInstanceConnectionString | acs:gpdb:$regionid: $accountid:dbinstance/$dbinstanceid |

| nalyticDB for MySQL | AnalyticDB for PostgreSQL Deve oper Guide·API referenc |
|---|---|

| ModifyDBInstanceNetworkType | acs:gpdb:$regionid: $accountid:dbinstance/$dbinstanceid |
|---|---|
| ReleaseInstancePublicConnection | acs:gpdb:$regionid: $accountid:dbinstance/$dbinstanceid |

### Instance management

#### CreateDBInstance

Call CreateDBInstance to create an AnalyticDB for PostgreSQL instance. Request parameters

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateDBInstanc e | The action that you want to perform. Set the value to CreateDBInstance. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region. For more information about available regions, see the DescribeRegions operation. |
| ZoneId | String | Yes | cn-hangzhou-i | The ID of the zone. For more information about zones, see the DescribeRegions operation. |
| EngineVersion | String | Yes | 6.0 | The version of the engine. Valid values: 6.0: the standard edition instance of version 6.0 6.0x: the vector edition instance of version 6.0 |
| Engine | String | Yes | gpdb | The engine. Set the value to gpdb. |

| DBInstanceClass | String | No | gpdb.group.segs dx1 | The instance type. For more information, see Instance types. Important You must specify this parameter if DBInstanceMode is set to Classic. |
|---|---|---|---|---|
| SegStorageType | String | No | local ssd _ | The disk storage type. The value local ssd is supported. _ |
| DBInstanceGrou pCount | String | No | 2 | The number of virtual warehouses for AnalyticDB for PostgreSQL. Important You must specify this parameter if DBInstanceMode is set to Classic. |
| InstanceSpec | String | No | 8C64G | The specification of compute nodes. Important You must specify this parameter if DBInstanceMode is set to StorageReserver. To create a vector edition instance, you must select a compute node specification higher than 8C64G. |
| SegNodeNum | String | No | 2 | The number of compute nodes. Valid values: 2 to 512. The step size is 2. Important You must specify this parameter if DBInstanceMode is set to StorageReserver. |
| MasterNodeNum | String | No | 1 | The number of master nodes. The value is fixed to 1. |

| DBInstanceMode | String | No | StorageReserver | The resource type of the instance. Valid values: Classic: storage-compute integrated mode StorageReserver: reserved storage mode |
|---|---|---|---|---|
| StorageType | String | No | local ssd _ | The storage type. The only valid value is local ssd. _ Important You must specify this parameter if DBInstanceMode is set to StorageReserver. |
| DBInstanceDesc ription | String | No | gp- bp12ga6v69h86 **** | The description of the AnalyticDB for PostgreSQL instance. The description can be up to 256 characters in length. |
| SecurityIPList | String | Yes | 127.0.0.1 | The IP allowlist. The default value is 127.0.0.1 . |
| PayType | String | No | Postpaid | The billing method. Valid values: Postpaid: pay-as-you-go Prepaid: subscription Set this parameter to Postpaid. |
| Period | String | No | Month | The unit of the subscription duration. Valid values: Month: month Year: year Note You must specify this parameter if PayType is set to Prepaid. |

| UsedTime | String | No | 1 | The subscription duration. Valid values: If Period is set to Month, valid values are 1 to 9. If Period is set to Year, valid values are 1 to 3. Note You must specify this parameter if PayType is set to Prepaid. |
|---|---|---|---|---|
| ClientToken | String | Yes | 0c593ea1-3bea- 11e9-b96b- 88e9fe637760 | The idempotent check. |
| InstanceNetwork Type | String | No | VPC | The network type of the instance. Valid values: VPC: virtual private cloud Classic: classic network. This is the default value. |
| VPCId | String | No | vpc- bp19ame5m1r3 oejns**** | If InstanceNetworkType is set to VPC, you must specify VPCId. The region of VPCId must be the same as that specified by RegionId. |
| VSwitchId | String | No | vsw- bp1cpq8mr64pa ltkb**** | If InstanceNetworkType is set to VPC, you must specify VSwitchId. The zone of VSwitchId must be the same as that specified by ZoneId. |
| CpuType | String | No | Intel | The chip architecture. Note Call the DescribeCpuTypes operation to query the chip architecture. |

| SrcDbInstanceN ame | String | No | gp- bp12g4sd89h86 **** | The ID of the source instance for cloning. You must configure this parameter together with BackupSetId to restore a backup set from the source instance to a new instance. Note Call the DescribeDBInstances operation to view the instance IDs of AnalyticDB for PostgreSQL. |
|---|---|---|---|---|
| BackupSetId | String | No | 1111111111 | The ID of the backup set. You must configure this parameter together with SrcDbInstanceName. Note Call DescribeDataBackups to view the IDs of all backup sets under the destination instance. |
| BackupVSwitchI d | String | No | vsw- bp4si98m0skpal tkb**** | The vSwitch ID of the standby zone. Use this parameter to create a multi- zone disaster recovery instance. |
| BackupZoneId | String | No | cn-hangzhou-h | The ID of the standby zone. Use this parameter to create a multi-zone instance. Note Call the DescribeRegions operation to view available zones. |

You do not need to configure other parameters, including PrivateIpAddress, ServerlessResource, IdleTime, ServerlessMode, MasterInstanceSpec, and CreateSampleData. These parameters do not take effect in Apsara Stack.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| eagleEyeTrace Id | String | 0a3214031709881 2558046******* | The EagleEye ID. |
| DBInstanceId | String | gp- ty9wj0p3qy68***** | The ID of the instance. |

| asapiSuccess | Boolean | true | Indicates whether the ASAPI request succeeded. |
|---|---|---|---|
| asapiRequestI d | String | 3995B9A6-B3A9- 4BB7-AC2D- 3C54EA5FA854 | The ID of the ASAPI request. |
| RequestId | String | 3995B9A6-B3A9- 4BB7-AC2D- 3C54EA5FA854 | The ID of the request. |

**Examples**

Sample requests

```
https://gpdb.aliyuncs.com/?Action=CreateDBInstance &ClientToken=0c593ea1-3bea-11e9-b96b-88e9fe637760 &Engine=gpdb &EngineVersion=6.0 &RegionId=cn-hangzhou &SecurityIPList=127.0.0.1 &ZoneId=cn-hangzhou-i &DBInstanceMode=StorageReserver &SegNodeNum=2 &InstanceSpec=8C64G &SegStorageType=local_ssd &StorageType=local_ssd &PayType=Postpaid &VPCId=vpc-ty9c32muyvatf4b9***** &VSwitchId=vsw-ty94i9cgkocyhjpo***** &InstanceNetworkType=VPC &CpuType=Kunpeng &<Common Request Parameter>
```

Sample success responses `XML` format

```xml
<CreateDBInstanceResponse>
          <eagleEyeTraceId>0a32140317098812558046*******</eagleEyeTraceId>
          <asapiSuccess>true</asapiSuccess>
          <asapiRequestId>3995B9A6-B3A9-4BB7-AC2D-3C54EA5FA854</asapiRequestId>
          <RequestId>3995B9A6-B3A9-4BB7-AC2D-3C54EA5FA854</RequestId>
          <DBInstanceId>gp-ty9wj0p3qy68*****</DBInstanceId>
</CreateDBInstanceResponse>
```

`JSON` format `{`

```json
  "eagleEyeTraceId":"0a32140317098812558046*******"
  "asapiSuccess":true
  "asapiRequestId":"3995B9A6-B3A9-4BB7-AC2D-3C54EA5FA854"
  "RequestId":"3995B9A6-B3A9-4BB7-AC2D-3C54EA5FA854"
  "DBInstanceId":"gp-ty9wj0p3qy68*****"
```

#### DescribeResourceUsage

You can call this operation to query the disk space that is used by an instance.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeResourc eUsage | The operation that you want to perform. Set the value to DescribeResourceUsage. |
| DBInstanceId | String | Yes | gp-xxxxxxxxxxx | The ID of the instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupSize | Long | 26624 | The disk space that is used to store backup files. Unit: bytes. -1 indicates no space is used. |
| DBInstanceId | String | gp-xxxxxxxx | The ID of the instance. |
| DataSize | Long | 83886080 | The disk space that is used to store data files. Unit: bytes. -1 indicates that no space is used. |
| DiskUsed | Long | 285212672 | The total space occupied by data and log files. Unit: bytes. -1 indicates that no space is used. |
| Engine | String | gpdb | The engine of the database. |
| LogSize | Long | 201326592 | The disk space that is used to store log files. Unit: bytes. -1 indicates that no space is used. |

| RequestId | String | 860FBA9E-BFFD- 493E-91A1- 2349B9D74AE7 | The ID of the request. |
|---|---|---|---|

**Examples**

Sample requests

```
https://gpdb.aliyuncs.com/?Action=DescribeResourceUsage &DBInstanceId=gp-xxxxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeResourceUsageResponse>
          <DBInstanceId>gp-xxxxxxx</DBInstanceId>
          <RequestId>860FBA9E-BFFD-493E-91A1-2349B9D74AE7</RequestId>
          <LogSize>201326592</LogSize>
          <DataSize>83886080</DataSize>
          <BackupSize>26624</BackupSize>
          <Engine>gpdb</Engine>
          <DiskUsed>285212672</DiskUsed>
</DescribeResourceUsageResponse>
```

`JSON` format `{`

```json
    "DBInstanceId":"gp-xxxxxxx",
    "RequestId":"860FBA9E-BFFD-493E-91A1-2349B9D74AE7",
    "LogSize":201326592,
    "DataSize":83886080,
    "BackupSize":26624,
    "Engine":"gpdb",
    "DiskUsed":285212672
```

#### ModifyDBInstanceMaintainTime

You can call this operation to modify the maintenance window of an instance. Typically, the maintenance window is set to the off-peak hours to minimize the impact on services. Alibaba Cloud performs instance maintenance at the maintenance window that you specify.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | ModifyDBInstanc eMaintainTime | The operation that you want to perform. Set the value to ModifyDBInstanceMaintainTime. |
|---|---|---|---|---|
| DBInstanceId | String | Yes | gp-xxxxxxxx | The ID of the instance. |
| EndTime | String | Yes | 03:00Z | The end time of the maintenance window. Example: 03:00Z. The end time must be later than the start time. |
| StartTime | String | Yes | 02:00Z | The start time of the maintenance window. Example: 02:00Z. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CA9A34C8-AC95- 413B-AC6A- CEBF67429CCA | The ID of the request. |

**Examples**

Sample requests

```
https://gpdb.aliyuncs.com/?Action=ModifyDBInstanceMaintainTime &DBInstanceId=gp-xxxxxxxx &EndTime=03:00Z &StartTime=02:00Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceMaintainTimeResponse>
           <RequestId>CA9A34C8-AC95-413B-AC6A-CEBF67429CCA</RequestId>
</ModifyDBInstanceMaintainTimeResponse>
```

`JSON` format `{`

```json
   "RequestId": "CA9A34C8-AC95-413B-AC6A-CEBF67429CCA"
```

#### RestartDBInstance

You can call this operation to restart an instance.

**Requestparameters**

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| DBInstanceId | String | Yes | gp-xxxxxxxxx | The ID of the instance. |
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe637760 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | A7356493-7141- 4393-8951- CDA8AB5D67EC | The ID of the request. |

**Examples**

Sample requests

```
https://gpdb.aliyuncs.com/?Action=RestartDBInstance &DBInstanceId=gp-xxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RestartDBInstance>
           <RequestId>A7356493-7141-4393-8951-CDA8AB5D67EC</RequestId>
</RestartDBInstance>
```

`JSON` format `{`

```json
  "RequestId":"A7356493-7141-4393-8951-CDA8AB5D67EC"
```

#### AddBuDBInstanceRelation

You call this operation to associate the BusinessUnit parameter to an instance.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | AddBuDBInstanc eRelation | The operation that you want to perform. Set the value to AddBuDBInstanceRelation. |
|---|---|---|---|---|
| BusinessUnit | String | Yes | BusinessUnit | The description of the business unit. |
| DBInstanceId | String | Yes | gp-xxxxxxx | The ID of the instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| BusinessUnit | String | BusinessUnit | The description of the business unit. |
| DBInstanceNa me | String | gp-xxxxxx | The ID of the instance. |
| RequestId | String | B4CAF581-2AC7- 41AD-8940- D56DF7AADF5B | The ID of the request. |

**Examples**

Sample requests

```
http(s)://gpdb.aliyuncs.com/? Action=AddBuDBInstanceRelation &DBInstanceId=gp-xxxxxx &BusinessUnit=BusinessUnit
```

Sample success responses `XML` format

```xml
<AddBuDBInstanceRelationResponse>
      <RequestId>D4D4BE8A-DD46-440A-BFCD-EE31DA81C9DD</RequestId>
      <BusinessUnit>BusinessUnit</BusinessUnit>
      <DBInstanceName>gp-xxxxxx</DBInstanceName>
</AddBuDBInstanceRelationResponse>
```

`JSON` format `{`

```json
  "RequestId":"D4D4BE8A-DD46-440A-BFCD-EE31DA81C9DD",
  "BusinessUnit": "BusinessUnit",
  "DBInstanceName": "gp-xxxxxx"
```

### Database management

### Account management

#### CreateAccount

You can call this operation to create an account for a database.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateAccount | The operation that you want to perform. Set the value to CreateAccount. |
| AccountName | String | Yes | testacc02 | The name of the account. |
| AccountPasswor d | String | Yes | pw1234 | The password for the account. |
| DBInstanceId | String | Yes | gp-xxxxxxxx | The ID of the instance. |
| DatabaseName | String | No | test01 | The name of the database. |
| AccountDescripti on | String | No | testacc02 | The description of the account. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D4D4BE8A-DD46- 440A-BFCD- EE31DA81C9DD | The ID of the request. |

**Examples**

Sample requests

```
https://gpdb.aliyuncs.com/?Action=CreateAccount &AccountName=testacc02 &AccountPassword=pw1234 &DBInstanceId=gp-xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateAccountResponse>
           <RequestId>D4D4BE8A-DD46-440A-BFCD-EE31DA81C9DD</RequestId>
</CreateAccountResponse>
```

`JSON` format `{`

```json
  "RequestId":"D4D4BE8A-DD46-440A-BFCD-EE31DA81C9DD"
```

#### ResetAccountPassword

You can call this operation to reset the password for your account in an instance. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance is not locked.

**Request parameters**

| Parameter | Type | Requir ed |   | Example | Description |   |   |
|---|---|---|---|---|---|---|---|
| AccountName | String | Yes |   | testaccount 1 _ | The name of the account. |   |   |
| AccountPasswor d | String | Yes |   | Testaccount 1 _ | The new password for the account. The password must be 8 to 32 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include ! @ # $ % ^ & * ( ) + _ - = |   |   |
|   |   |   |   |   |   | ! @ # $ % ^ & * ( ) + _ |   |
|   |   |   |   |   | - = |   |   |
| DBInstanceId | String | Yes |   | gp-xxxxxxxxx | The ID of the instance. |   |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 187C80FC-75C4- 477C-BBF2- A368A36D041C | The ID of the request. |

**Examples**

Sample requests

```
https://gpdb.aliyuncs.com/?Action=ResetAccountPassword &AccountName=testaccount_1 &AccountPassword=Testaccount_1 &DBInstanceId=gp-xxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ResetAccountPasswordResponse>
           <RequestId>187C80FC-75C4-477C-BBF2-A368A36D041C</RequestId>
</ResetAccountPasswordResponse>
```

`JSON` format `{`

```json
    "RequestId":"187C80FC-75C4-477C-BBF2-A368A36D041C"
```

#### DescribeAccounts

You can call this operation to query the information of a database account.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAccount s | The operation that you want to perform. Set the value to DescribeAccounts. |
| DBInstanceId | String | Yes | gp-xxxxxxxxx | The ID of the instance. |
| AccountName | String | No | onlyreadacc | The name of the account. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Accounts | Array of DBInstanceAcc ount | None | The information of the account, which is an array of DBInstanceAccount data. |
| DBInstanceAcc ount | None | None | None |

| AccountDescri ption | String | testacc01 | The description of the account. |
|---|---|---|---|
| AccountName | String | testacc01 | The name of the account. |
| AccountStatus | String | 1 | The status of the account. Valid values: 0: The account is being created. 1: The account is in use. 3: The account is being deleted. |
| DBInstanceId | String | gp-xxxxxxxx | The ID of the instance. |
| RequestId | String | 7565770E-7C45- 462D-BA4A- 8A5396F2CAD1 | The ID of the request. |

**Examples**

Sample requests

```
https://gpdb.aliyuncs.com/?Action=DescribeAccounts &DBInstanceId=gp-xxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeAccountsResponse>
           <RequestId>7565770E-7C45-462D-BA4A-8A5396F2CAD1</RequestId>
             <Accounts>
                   <DBInstanceAccount>
                        <AccountName>testaccount_1</AccountName>
                        <DBInstanceId>gp-xxxxxxx</DBInstanceId>
                        <AccountStatus>1</AccountStatus>
                        <AccountDescription></AccountDescription>
                   </DBInstanceAccount>
             </Accounts>
</DescribeAccountsResponse>
```

`JSON` format `{`

```json
    "Accounts": {
      "DBInstanceAccount": [
```

`{`

```json
          "AccountDescription": "",
          "DBInstanceId": "gp-xxxxxxx",
          "AccountStatus": "1",
          "AccountName": "testaccount_1"
```

`]` `},`

```json
    "RequestId": "7565770E-7C45-462D-BA4A-8A5396F2CAD1"
```

#### ModifyAccountDescription

You can call this operation to modify the description of a database account in an instance.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| AccountDescripti on | String | Yes | testAccoutdescri be | The new description of the database account. The description must meet the following requirements: The description must start with a letter. The description cannot start with http:// or https:// . The description can contain letters, underscores ( ), hyphens _ (-), and digits. The description must be 2 to 256 characters in length. |
| AccountName | String | Yes | testAccout | The name of the account. The account name must be unique and meet the following requirements: The name must start with a letter. The name can contain lowercase letters, digits, and underscores ( ). _ The name can be up to 16 characters in length. The name cannot contain reserved keywords. |
| DBInstanceId | String | Yes | gp-xxxxxxxxx | The ID of the instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 99BBBD5E-B5D8- 4FC8-B8BF- FB1A0A38BBA2 | The ID of the request. |

**Examples**

Sample requests

```
https://gpdb.aliyuncs.com/?Action=ModifyAccountDescription &AccountDescription=testAccoutdescribe &AccountName=testAccout &DBInstanceId=gp-xxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyAccountDescriptionResponse>
           <RequestId>99BBBD5E-B5D8-4FC8-B8BF-FB1A0A38BBA2</RequestId>
</ModifyAccountDescriptionResponse>
```

`JSON` format `{`

```json
    "RequestId": "99BBBD5E-B5D8-4FC8-B8BF-FB1A0A38BBA2"
```

### Security management

#### DescribeDBInstanceIPArrayList

You can call this operation to query the list of one or more IP addresses that are allowed to access an instance.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| DBInstanceId | String | Yes | gp-xxxxxxxxxxx | The ID of the instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Items | Array of DBInstanceIPA rray | None | The information of IP addresses that are allowed to access the instance, which is an array of DBInstanceIPArray data. |
|---|---|---|---|
| DBInstanceIPA rray | None | None | None |
| DBInstanceIPA rrayAttribute | String | hidden | This parameter is empty by default. You can use this parameter to specify an attribute for a whitelist. A whitelist with the hidden attribute does not appear in the console. |
| DBInstanceIPA rrayName | String | default | The name of the whitelist. |
| SecurityIPList | String | 127.0.0.1 | The IP addresses listed in the whitelist. You can add up to 1,000 IP addresses to the whitelist. Separate multiple IP addresses with commas (,). The IP addresses must use one of the following formats: 0.0.0.0/0 10.23.12.24. This is an IP address. Classless Inter-Domain Routing (CIDR) blocks, such as 10.23.12.24/24, where /24 indicates the prefix of the CIDR block is 24 bits in length. You can replace 24 with a value in the range of 1 to 32 . |
| RequestId | String | CB7AA0BF-BE41- 480E-A3DC- C97BF85A391B | The ID of the request. |

**Examples**

Sample requests

```
https://gpdb.aliyuncs.com/?Action=DescribeDBInstanceIPArrayList &DBInstanceId=gp-xxxxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeDBInstanceIPArrayListResponse>
  <Items>
        <DBInstanceIPArray>
              <DBInstanceIPArrayName>default</DBInstanceIPArrayName>
              <DBInstanceIPArrayAttribute>hidden</DBInstanceIPArrayAttribute>
              <securityIPList>127.0.0.1</securityIPList>
        </DBInstanceIPArray>
  </Items>
  <RequestId>CB7AA0BF-BE41-480E-A3DC-C97BF85A391B</RequestId>
</DescribeDBInstanceIPArrayListResponse>
```

`JSON` format `{`

```json
    "Items":{
        "DBInstanceIPArray":[
```

`{`

```json
              "DBInstanceIPArrayName":"default",
              "DBInstanceIPArrayAttribute":"hidden",
              "securityIPList":"127.0.0.1"
```

`]` `},`

```json
    "RequestId":"CB7AA0BF-BE41-480E-A3DC-C97BF85A391B"
```

#### ModifySecurityIps

You can call this operation to modify the IP addresses that are allowed to access an instance. Before you call this operation, make sure that the following requirements are met: The instance is in the Running state. The instance is not locked.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySecurityIp s | The operation that you want to perform. Set the value to ModifySecurityIps. |
| DBInstanceId | String | Yes | gp-xxxxxxxxx | The ID of the instance. |

| SecurityIPList | String | Yes | 127.0.0.1 | The IP addresses listed in the whitelist. You can add up to 1,000 IP addresses to the whitelist. Separate multiple IP addresses with commas (,). The IP addresses must use one of the following formats: 0.0.0.0/0 10.23.12.24. This is an IP address. Classless Inter-Domain Routing (CIDR) blocks, such as 10.23.12.24/24, where /24 indicates the prefix of the CIDR block is 24 bits in length. You can replace 24 with a value in the range of 1 to 32 . |
|---|---|---|---|---|
| DBInstanceIPArr ayName | String | No | Default | The name of the whitelist. If you do not enter a name, IP addresses are added to the default whitelist. Note You can create up to 50 whitelists for an instance. |
| DBInstanceIPArr ayAttribute | String | No | hidden | The attribute of the IP address whitelist. By default, this parameter is empty. You can use this parameter to distinguish whitelists that have different attributes. The console does not display whitelists that have the hidden attribute. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 871C698F-B43D- 4D1D-ACD6- DF56B0F89978 | The ID of the request. |

**Examples**

Sample requests

```
https://gpdb.aliyuncs.com/?Action=ModifySecurityIps &DBInstanceId=gp-xxxxxxxxx &SecurityIPList=127.0.0.1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifySecurityIpsResponse>
           <RequestId>871C698F-B43D-4D1D-ACD6-DF56B0F89978</RequestId>
</ModifySecurityIpsResponse>
```

`JSON` format `{`

```json
  "RequestId":"871C698F-B43D-4D1D-ACD6-DF56B0F89978"
```

### Log management

#### DescribeSQLCollectorPolicy

You can call this operation to query whether the SQL collection feature is enabled for an instance.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSQLColl ectorPolicy | The operation that you want to perform. Set the value to DescribeSQLCollectorPolicy. |
| DBInstanceId | String | Yes | gp-xxxxxxxxx | The ID of the instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | ABB39CC3-4488- 4857-905D- 2E4A051D0521 | The ID of the request. |
| SQLCollectorSt atus | String | Enable | The status of SQL collection. Enable: SQL collection is enabled. Disabled: SQL collection is disabled. |

**Examples**

Sample requests

```
https://gpdb.aliyuncs.com/?Action=DescribeSQLCollectorPolicy &DBInstanceId=gp-xxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeSQLCollectorPolicyResponse>
   <RequestId>ABB39CC3-4488-4857-905D-2E4A051D0521</RequestId>
   <SQLCollectorStatus>Enable</SQLCollectorStatus>
</DescribeSQLCollectorPolicyResponse>
```

`JSON` format `{`

```json
    "RequestId":"ABB39CC3-4488-4857-905D-2E4A051D0521",
    "SQLCollectorStatus":"Enable"
```

#### DescribeSlowLogRecords

Queries slow SQL query details of a database in an instance within a specific time range.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |   |   |
|---|---|---|---|---|---|---|
| Action | String | Yes | DescribeSlowLo gRecords | The operation that you want to perform. Set the value to DescribeSlowLogRecords. |   |   |
| DBInstanceId | String | Yes | gp-xxxxxxx | The ID of the instance. |   |   |
| EndTime | String | Yes | 2018-07- 19T09:00:08Z | The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. Example: 2011-06- 11T15:00Z. |   |   |
|   |   |   |   |   | yyyy-MM- |   |
| StartTime | String | Yes | 2018-07- 09T09:00:08Z | The beginning of the time range to query. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Example: 2011-06-11T15:00Z. |   |   |
| SQLId | Long | No | 143242632 | The ID of the slow SQL query. |   |   |

| :08Z | ddTHH:mm:ssZ |
|---|---|

| DBName | String | No | test | The name of the database. |
|---|---|---|---|---|
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Engine | String | gpdb | The database engine of the instance. |
| Items | Array of SQLSlowRecor d |   | Details of the slow queries. |
| SQLSlowRecor d |   |   |   |
| DBName | String | test | The name of the database. |
| ExecutionStart Time | String | 2018-07- 09T09:00:08Z | The beginning of the time range within which the query is executed. The time follows the ISO 8601 standard in the YYYY- MM-DDTHH:mm:ssZ format. The time is displayed in UTC. Example: 2011-06- 11T15:00:08Z. |
| HostAddress | String | 127.0.0.1 | The IP address of the host that is used to connect to the database. |
| LockTimes | Long | 12 | The lock duration of the query. Unit: seconds. |
| ParseRowCoun ts | Long | 125 | The number of parsed rows. |
| QueryTimes | Long | 123 | The execution duration of the query. Unit: seconds. |

| ReturnRowCou nts | Long | 1 | The number of entries returned. |
|---|---|---|---|
| SQLText | String | update test.zxb set id=0 limit 1 | The SQL query statement. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCo unt | Integer | 1 | The number of slow SQL queries on the current page. |
| RequestId | String | 542BB8D6-4268- 45CC-A557- B03EFD7AB30A | The ID of the request. |
| TotalRecordCo unt | Integer | 1 | The total number of entries returned. |

**Examples**

Sample requests

```
https://gpdb.aliyuncs.com/?Action=DescribeSlowLogRecords &DBInstanceId=gp-xxxxxxx &EndTime=2018-07-19T09:00:08Z &StartTime=2018-07-09T09:00:08Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeSlowLogRecordsResponse>
      <RequestId>542BB8D6-4268-45CC-A557-B03EFD7AB30A</RequestId>
      <Engine>gpdb</Engine>
      <PageNumber>1</PageNumber>
      <PageRecordCount>1</PageRecordCount>
      <TotalRecordCount>1</TotalRecordCount>
      <Items>
            <SQLSlowRecord>
                  <HostAddress>127.0.0.1</HostAddress>
                  <DBName>test</DBName>
                  <SQLText> update test.zxb set id=0 limit 1</SQLText>
                  <QueryTimes>123</QueryTimes>
                  <LockTimes>12</LockTimes>
                  <ParseRowCounts>125</ParseRowCounts>
                  <ReturnRowCounts>1</ReturnRowCounts>
                  <ExecutionStartTime>2018-07-09T09:00:08Z</ExecutionStartTime>
            </SQLSlowRecord>
      </Items>
</DescribeSlowLogRecordsResponse>
```

`JSON` format `{`

```json
    "RequestId":"542BB8D6-4268-45CC-A557-B03EFD7AB30A",
    "Engine":"gpdb",
    "PageNumber":1,
    "PageRecordCount":1,
    "TotalRecordCount":1,
    "Items":{
        "SQLSlowRecord":[
```

`{`

```json
                "HostAddress":"127.0.0.1",
                "DBName":"test",
                "SQLText":" update test.zxb set id=0 limit 1",
                "QueryTimes":"123",
                "LockTimes":"12",
                "ParseRowCounts":"125",
                "ReturnRowCounts":"1",
                "ExecutionStartTime":"2018-07-09T09:00:08Z"
```

`]`

#### DescribeSQLLogFiles

You can call this operation to query the list of SQL audit log files.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSQLLog Files | The operation that you want to perform. Set the value to DescribeSQLLogFiles. |
| DBInstanceId | String | Yes | gp-xxxxxxxxxx | The ID of the instance. |
| FileName | String | No | log20200202 | The name of the file. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30 |
| PageNumber | Integer | No | 1 | The number of the page to return. Valid values: any non-zero positive integer. Default value: 1. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | Array of LogFile | None | The information of the log file, which is an array of LogFile data. |
| LogFile | None | None | None |
| FileID | String | 1023423423 | The ID of the file. |
| LogDownloadU RL | String | xxxxxx | The URL that is used to download the file. If the URL is unavailable, an empty string is returned. |
| LogEndTime | String | 2019-02- 24T14:10Z | The end of the time range within which data is recorded in the file. |
| LogSize | String | 100210 | The size of the file. Unit: bytes. |
| LogStartTime | String | 2019-02- 24T12:10Z | The beginning of the time range within which data is recorded in the file. |
| LogStatus | String | Success | The status of the file. Valid values: NoStart Generating Success Failed |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCo unt | Integer | 1 | The number of entries on the current page. |
| RequestId | String | 66E164C1-D7F2- 4D85-849D- E2883FCFFBA5 | The ID of the request. |
| TotalRecordCo unt | Integer | 1 | The total number of entries. |

**Examples**

Sample requests

```
https://gpdb.aliyuncs.com/?Action=DescribeSQLLogFiles &DBInstanceId=gp-xxxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeSQLLogFilesResponse>
  <Items>
        <LogFile>
              <FileID>1023423423</FileID>
              <LogDownloadURL>xxxxxxx</LogDownloadURL>
              <LogEndTime>2019-02-24T14:10Z</LogEndTime>
              <LogSize>100210</LogSize>
              <LogStartTime>2019-02-24T12:10Z</LogStartTime>
              <LogStatus>Success</LogStatus>
        </LogFile>
  </Items>
  <PageNumber>1</PageNumber>
  <TotalRecordCount>1</TotalRecordCount>
  <RequestId>66E164C1-D7F2-4D85-849D-E2883FCFFBA5</RequestId>
  <PageRecordCount>1</PageRecordCount>
</DescribeSQLLogFilesResponse>
```

`JSON` format `{`

```json
    "Items": {
        "LogFile": [
```

`{`

```json
                "FileID": "1023423423",
                "LogDownloadURL": "xxxxxxx",
                "LogEndTime": "2019-02-24T14:10Z",
                "LogSize":"100210",
                "LogStartTime": "2019-02-24T12:10Z",
                "LogStatus": "Success"
```

`]` `},`

```json
    "PageNumber": 1,
    "TotalRecordCount": 1,
    "RequestId": "66E164C1-D7F2-4D85-849D-E2883FCFFBA5",
    "PageRecordCount": 1
```

#### ModifySQLCollectorPolicy

You can call this operation to enable or disable the SQL collection feature for an instance.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | ModifySQLCollec torPolicy | The operation that you want to perform. Set the value to ModifySQLCollectorPolicy. |
|---|---|---|---|---|
| DBInstanceId | String | Yes | gp-xxxxxxxx | The ID of the instance. |
| SQLCollectorStat us | String | Yes | Enable | Specifies whether to enable or disable SQL collection. Enable: enables SQL collection. Disabled: disables SQL collection. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4FA1F1D1-50A6- 4F60-9A78- 5752F2076A53 | The ID of the request. |

**Examples**

Sample requests

```
https://gpdb.aliyuncs.com/?Action=ModifySQLCollectorPolicy &DBInstanceId=gp-xxxxxxxx &SQLCollectorStatus=Enable &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifySQLCollectorPolicyResponse>
           <RequestId>4FA1F1D1-50A6-4F60-9A78-5752F2076A53</RequestId>
</ModifySQLCollectorPolicyResponse>
```

`JSON` format `{`

```json
  "RequestId":"4FA1F1D1-50A6-4F60-9A78-5752F2076A53"
```

#### DescribeSQLLogRecords

You can call this operation to query the SQL audit logs generated for an instance.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | DescribeSQLLog Records | The operation that you want to perform. Set the value to DescribeSQLLogRecords. |
|---|---|---|---|---|
| DBInstanceId | String | Yes | gp-xxxxxxxxxx | The ID of the instance. |
| EndTime | String | Yes | 2018-07- 09T08:50:20Z | The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. The end time must be later than the start time. |
| StartTime | String | Yes | 2018-07- 09T04:50:20Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |
| QueryKeywords | String | No | keywords1 | The keywords that are used for queries. Separate multiple keywords with spaces. The maximum number of keywords is 10. |
| Database | String | No | testdb | The name of the database to be queried. By default, all databases are queried. |
| User | String | No | testacc | The username of the database. By default, all users are selected. |
| Form | String | No | Stream | Specifies whether to generate SQL audit log files or return SQL audit log records. Default value: Stream. Valid values: File: generates audit log files. If you set this parameter to File, only common response parameters are returned. Therefore, you need to call the DescribeSQLLogFiles operation to obtain the download URL of audit log files. Stream: generates data streams. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. Valid values: any non-zero positive integer. Default value: 1. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | Array of SQLRecord | None | The information of SQL queries, which is an array of SQLRecord data. |
| SQLRecord | None | None | None |
| AccountName | String | testacc | The account name. |
| DBName | String | testdb | The name of the database. |
| ExecuteTime | String | 2018-07- 09T08:50:20Z | The time when the statement is executed. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. Example: 2011-05-30 T12:11:20Z. |
| HostAddress | String | 127.0.0.1 | The IP address of the client. |
| ReturnRowCou nts | Long | 122 | The number of returned entries. |
| SQLText | String | update test.zxb set id=0 limit 1 | The SQL statement that is recorded in the log. |
| ThreadID | String | 723 | The ID of the thread. |
| TotalExecution Times | Long | 130 | The execution duration of the SQL statement. Unit: microseconds. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCo unt | Integer | 1 | The number of SQL audit log records on the current page. |
| RequestId | String | 9B24F29F-BA7F- 47A3-838E- C6A993888388 | The ID of the request. |
| TotalRecordCo unt | Integer | 1 | The total number of entries. |

**Examples**

Sample requests

```
https://gpdb.aliyuncs.com/?Action=DescribeSQLLogRecords &DBInstanceId=gp-xxxxxxx &StartTime=2018-07-09T04:50:20Z &EndTime=2018-07-09T08:50:20Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeSQLLogRecords>
  <Items>
        <SQLRecord>
              <AccountName>testacc</AccountName>
              <DBName>testdb</DBName>
              <ExecuteTime>2018-07-09T08:50:20Z</ExecuteTime>
              <HostAddress>127.0.0.1</HostAddress>
              <ReturnRowCounts>122</ReturnRowCounts>
              <SQLText>update test.zxb set id=0 limit 1</SQLText>
              <ThreadID>723</ThreadID>
              <TotalExecutionTimes>130</TotalExecutionTimes>
        </SQLRecord>
  </Items>
  <TotalRecordCount>1</TotalRecordCount>
  <PageNumber>1</PageNumber>
  <RequestId>9B24F29F-BA7F-47A3-838E-C6A993888388</RequestId>
  <PageRecordCount>1</PageRecordCount>
</DescribeSQLLogRecords>
```

`JSON` format `{`

```json
    "Items": {
        "SQLRecord": [
```

`{`

```json
                "AccountName": "testacc",
                "DBName": "testdb",
                "ExecuteTime": "2018-07-09T08:50:20Z",
                "HostAddress": "127.0.0.1",
                "ReturnRowCounts": "122",
                "SQLText": "update test.zxb set id=0 limit 1",
                "ThreadID": "723",
                "TotalExecutionTimes": "130"
```

`]` `},`

```json
    "TotalRecordCount": 1,
    "PageNumber": 1,
    "RequestId": "9B24F29F-BA7F-47A3-838E-C6A993888388",
    "PageRecordCount": 1
```

### Network management

#### AllocateInstancePublicConnection

You can call this operation to specify a public endpoint of the instance.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | No | AllocateInstance PublicConnectio n | The operation that you want to perform. Set the value to AllocateInstancePublicConnection. |
| ConnectionStrin gPrefix | String | Yes | gp-xxxxxxxx | The endpoint of the instance. |
| DBInstanceId | String | Yes | gp-xxxxxxxx | The ID of the instance. |
| Port | String | Yes | 3432 | The port associated with the endpoint. Valid values: 3200 to 3999. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | ADD6EA90-EECB- 4C12-9F26- 0B6DB58710EF | The ID of the request. |

**Examples**

Sample requests

```
http(s)://gpdb.aliyuncs.com/? Action=AllocateInstancePublicConnection &ConnectionStringPrefix=gp-xxxxxxxx &DBInstanceId=gp-xxxxxxxx &Port=3432 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>ADD6EA90-EECB-4C12-9F26-0B6DB58710EF</RequestId>
```

`JSON` format `{`

```json
    "RequestId": "ADD6EA90-EECB-4C12-9F26-0B6DB58710EF"
```

#### DescribeDBInstanceNetInfo

You can call this operation to query the connection information of an instance.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| DBInstanceId | String | Yes | gp-xxxxxxxxxx | The ID of the instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceNet Infos | Array of DBInstanceNet Info | None | The connection information of the instance. |
| DBInstanceNet Info | None | None | None |
| ConnectionStri ng | String | gp- xxxxxxx.gpdb.rds.a liyuncs.com | The URL of the database. |
| IPAddress | String | 127.0.0.1 | The IP address of the instance. |
| IPType | String | Inner | The type of IP address. Valid values for instances in the classic network: Inner and Public Valid values for instances in a VPC: Private and Public |
| Port | String | 3432 | The port information. |
| VPCId | String | vpc-xxxxxxx | The ID of the VPC. |
| VSwitchId | String | vsw-xxxxxxxx | The ID of the vSwitch. Multiple IDs are separated by commas (,). |

| InstanceNetwo rkType | String | Classic | The network type of the instance. Valid values: Classic VPC |
|---|---|---|---|
| RequestId | String | 7565770E-7C45- 462D-BA4A- 8A5396F2CAD1 | The ID of the request. |

**Examples**

Sample requests

```
https://gpdb.aliyuncs.com/?Action=DescribeDBInstanceNetInfo &DBInstanceId=gp-xxxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeDBInstanceNetInfoResponse>
  <instanceNetworkType>Classic</instanceNetworkType>
  <DBInstanceNetInfos>
        <DBInstanceNetInfo>
              <DBInstanceNetType>1</DBInstanceNetType>
              <connectionString>gp-xxxxxxx.gpdb.rds.aliyuncs.com</connectionString>
              <ipAddress>127.0.0.1</ipAddress>
              <port>3432</port>
              <VPCId>vpc-xxxxxxxxx</VPCId>
              <VSwitchId>vsw-xxxxxxx</VSwitchId>
        </DBInstanceNetInfo>
  </DBInstanceNetInfos>
  <RequestId>7565770E-7C45-462D-BA4A-8A5396F2CAD1</RequestId>
</DescribeDBInstanceNetInfoResponse>
```

`JSON` format `{`

```json
    "instanceNetworkType": "Classic",
    "DBInstanceNetInfos": {
        "DBInstanceNetInfo": [
```

`{`

```json
                "DBInstanceNetType": "1",
                "connectionString": "gp-xxxxxxx.gpdb.rds.aliyuncs.com",
                "ipAddress": "127.0.0.1",
                "port": "3432",
                "VPCId": "vpc-xxxxxxxxx",
                "VSwitchId": "vsw-xxxxxxx"
```

`]` `},`

```json
    "RequestId": "7565770E-7C45-462D-BA4A-8A5396F2CAD1"
```

#### ModifyDBInstanceConnectionString

You can call this operation to modify the internal or public endpoint of an instance.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstanc eConnectionStri ng | The operation that you want to perform. Set this parameter to ModifyDBInstanceConnectionString. |
| ConnectionStrin gPrefix | String | Yes | gp-xxxxxxxx | The endpoint to be used by the instance. |
| CurrentConnecti onString | String | Yes | gp- xxxxxxx.gpdb.rd s.aliyuncs.com | The endpoint used by the instance. |
| DBInstanceId | String | Yes | gp-xxxxxxx | The ID of the instance. |
| Port | String | Yes | 3432 | The port to be used by the instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 29B0BF34-D069- 4495-92C7- FA6D94528A9E | The ID of the request. |

**Examples**

Sample requests

```
https://gpdb.aliyuncs.com/?Action=ModifyDBInstanceConnectionString &ConnectionStringPrefix=gp-xxxxxxxx &CurrentConnectionString=gp-xxxxxxx.gpdb.rds.aliyuncs.com &DBInstanceId=gp-xxxxxxx &Port=3432 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceConnectionStringResponse>
           <RequestId>29B0BF34-D069-4495-92C7-FA6D94528A9E</RequestId>
</ModifyDBInstanceConnectionStringResponse>
```

`JSON` format `{`

```json
 "RequestId": "29B0BF34-D069-4495-92C7-FA6D94528A9E"
```

#### ModifyDBInstanceNetworkType

You can call this operation to switch the network type of an instance between VPC and classic network.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| DBInstanceId | String | Yes | gp-xxxxxxxx | The ID of the instance. |
| InstanceNetwork Type | String | Yes | VPC | The network type of the instance. Valid values: VPC Classic |
| VPCId | String | No | vpc-xxxxxxxx | The ID of the VPC. |
| VSwitchId | String | No | vsw-xxxxxxxx | The ID of the vSwitch. This parameter is required when the VPCId parameter is specified. |

| PrivateIpAddress | String | No | 192.168.0.10 | The private IP address of the instance. You can specify an IP address of the VPC to which the vSwitch belongs. If no IP address is specified, the system assigns an IP address based on the VPC ID and vSwitch ID. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 2d0c35a9-f5da- 44ba-852d- 741e27b7eb0b | The ID of the request. |

**Examples**

Sample requests

```
https://gpdb.aliyuncs.com/?Action=ModifyDBInstanceNetworkType &DBInstanceId=gp-xxxxxxxx &InstanceNetworkType=VPC &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceNetworkTypeResponse>
           <RequestId>2d0c35a9-f5da-44ba-852d-741e27b7eb0b</RequestId>
</ModifyDBInstanceNetworkTypeResponse>
```

`JSON` format `{`

```json
  "RequestId":"2d0c35a9-f5da-44ba-852d-741e27b7eb0b"
```

#### ReleaseInstancePublicConnection

You can call this operation to release the public endpoint of an instance.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| CurrentConnecti onString | String | Yes | gp- xxxxxxx.gpdb.rd s.aliyuncs.com | The public endpoint of the instance. |

| DBInstanceId | String | Yes | gp-xxxxxxxx | The ID of the instance. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9CEF7037-4158- 4A65-BEC7- 2A1541F6FE74 | The ID of the request. |

**Examples**

Sample requests

```
https://gpdb.aliyuncs.com/?Action=ReleaseInstancePublicConnection &CurrentConnectionString=gp-xxxxxxx.gpdb.rds.aliyuncs.com &DBInstanceId=gp-xxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ReleaseInstancePublicConnectionResponse>
           <RequestId>9CEF7037-4158-4A65-BEC7-2A1541F6FE74</RequestId>
</ReleaseInstancePublicConnectionResponse>
```

`JSON` format `{`

```json
   "RequestId": "9CEF7037-4158-4A65-BEC7-2A1541F6FE74"
```

#### SwitchDBInstanceNetType

You can call this operation to switch between internal and public endpoints.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SwitchDBInstanc eNetType | The operation that you want to perform. Set the value to SwitchDBInstanceNetType. |

| ConnectionStrin gPrefix | String | Yes | test1234 | The prefix of the custom endpoint. The prefix can be up to 30 characters in length and can contain letters, digits, and hyphens (-). It must start with a letter. |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| Port | String | Yes | 3306 | The port associated with the endpoint. Valid values: 3001 to 3999. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | FA67B751-2A2D- 470C-850B- D6B93699D35C | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=SwitchDBInstanceNetType &ConnectionStringPrefix=test1234 &DBInstanceId=rm-uf6wjk5xxxxxxx &Port=3306 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>FA67B751-2A2D-470C-850B-D6B93699D35C</RequestId>
```

`JSON` format

```json
{"RequestId":"FA67B751-2A2D-470C-850B-D6B93699D35C"}
```

### Tag management

#### TagResources

Add tags to specific instances.

**Request parameters**

| > Document Versio | n: 20260828 |   |   | 6 |
|---|---|---|---|---|

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The region ID of the instances. |
| ResourceId.N | RepeatL ist | Yes | dbaudit-cn- 78v1gcxxxxx | The ID of instance N. Valid values of N: 1 to 20. |
| ResourceType | String | Yes | INSTANCE | The type of the resource. Set the value to INSTANCE. INSTANCE indicates reserved storage mode instance. |
| Tag.N.Key | String | No | test | The key of tag N. Valid values of N: 1 to 20. The tag key cannot be an empty string. It can be up to 128 characters in length. Tag keys cannot contain http:// or https:// and cannot start with acs: or aliyun. |
| Tag.N.Value | String | No | testapi | The value of tag N. Valid values of N: 1 to 20. The tag value can be an empty string. It can be up to 128 characters in length. Tag values cannot contain http:// or https:// and cannot start with acs: or aliyun. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 23DD5EDB-EAC7- 44A5-A68E- 798BB085D27F | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=TagResources &RegionId=cn-hangzhou &ResourceId.1=dbaudit-cn-78v1gcxxxxx &ResourceType=INSTANCE &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>23DD5EDB-EAC7-44A5-A68E-798BB085D27F</RequestId>
```

`JSON` format

```json
{"RequestId":"23DD5EDB-EAC7-44A5-A68E-798BB085D27F"}
```

#### ListTagResources

You can call this operation to query tags that are bound to one or more instances.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. |
| ResourceType | String | Yes | instance | The type of the resource. Valid values: instance : reserved storage mode ALIYUN::GPDB::INSTANCE : elastic storage mode |
| ResourceId.N | RepeatL ist | No | gp-xxxxxxxxxx | The ID of the instance. |
| Tag.N.Key | String | No | TestKey | The key of tag N. The tag key can contain 1 to 128 characters in length. Valid values of N: 1 to 20. You can use Tag.N to query instances that have specific tags bound. Tag.N consists of Tag.N.Key and Tag.N.Value. If you specify only Tag.N.Key , the instances that contain all the specified tag keys are returned. If you specify only Tag.N.Value , InvalidParameter.TagValue is returned. If you specify multiple tag key- value pairs at a time, the instances that contain all the specified tag keys are returned. |

| Tag.N.Value | String | No | TestValue | The value of tag N. The tag value can contain 1 to 128 characters in length. Valid values of N: 1 to 20. |
|---|---|---|---|---|
| NextToken | String | No | caeba0bbb2be0 3f84eb48b699f0 a4883 | The token used to perform the next query. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| NextToken | String | caeba0bbb2be03f8 4eb48b699f0a488 3 | The token that was returned for the next query. |
| RequestId | String | 5414A4E5-4C36- 4461-95FC- 23757A20B5F8 | The ID of the request. |
| TagResources | Array of TagResource | None | The information of instances and tags, including the instance IDs,resource types, and tag key-value pairs, which is an array of TagResource data. |
| TagResource | None | None | None |
| ResourceId | String | gp-xxxxxxxxxx | The ID of the instance. |
| ResourceType | String | instance | The type of the resource. |
| TagKey | String | TestKey | The tag key of the instance. |
| TagValue | String | TestValue | The tag value of the instance. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=ListTagResources &RegionId=cn-hangzhou &ResourceType=instance &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>5414A4E5-4C36-4461-95FC-23757A20B5F8</RequestId> <NextToken>caeba0bbb2be03f84eb48b699f0a4883</NextToken> <TagResources>
    <TagResource>
        <ResourceId>gp-xxxxxxxxxx</ResourceId>
        <TagKey>TestKey</TagKey>
        <ResourceType>instance</ResourceType>
        <TagValue>TestValue</TagValue>
    </TagResource>
</TagResources>
```

`JSON` format `{`

```json
    "RequestId": "5414A4E5-4C36-4461-95FC-23757A20B5F8",
    "NextToken": "caeba0bbb2be03f84eb48b699f0a4883",
    "TagResources": {
        "TagResource": {
            "ResourceId": "gp-xxxxxxxxxx",
            "TagKey": "TestKey",
            "ResourceType": "instance",
            "TagValue": "TestValue"
```

#### UntagResources

Removes tags from specific instances.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The region ID of the instances. |
| ResourceId.N | RepeatL ist | Yes | dbaudit-cn-test | The ID of instance N. Valid values of N: 1 to 20. |
| ResourceType | String | Yes | INSTANCE | The type of the resource. Set the value to INSTANCE. INSTANCE indicates reserved storage mode instance. |
| TagKey.N | RepeatL ist | No | 456 | The key of tag N. Valid values of N: 1 to 20. |

| All | Boolean | No | false | Specifies whether to remove all tags from the instances. When the TagKey.N parameter is specified, set the All parameter to false to remove the specified tags from the instances. When the TagKey.N parameter is not specified, set the All parameter to true to remove all tags from the instances. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 8EC13467-A84C- 401F-A4A0- AF893066FBA1 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UntagResources &RegionId=cn-hangzhou &ResourceId.1=dbaudit-cn-test &ResourceType=INSTANCE &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>8EC13467-A84C-401F-A4A0-AF893066FBA1</RequestId>
```

`JSON` format

```json
{"RequestId":"8EC13467-A84C-401F-A4A0-AF893066FBA1"}
```

#### DescribeTags

You can call this operation to query the tags of an instance.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. |
| ResourceType | String | Yes | instance | The type of the resource. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | The ID of the request. |
| Tags | Array of Tag |   | The information of the tag, which is an array of tag key and tag value. |
| TagKey | String | user | The tag key of the instance. |
| TagValue | String | admin | The tag value of the instance. |

**Examples**

Sample requests

```
http(s)://gpdb.aliyuncs.com/? Action=DescribeTags &RegionId=cn-hangzhou &ResourceType=instance
```

Sample success responses `XML` format

```xml
<RequestId>65BDA532-28AF-4122-AA39-B382721EEE64</RequestId> <Tags>
    <TagKey>test</TagKey>
    <TagValue>admin</TagValue>
</Tags>
```

`JSON` format `{`

```json
    "RequestId": "65BDA532-28AF-4122-AA39-B382721EEE64",
    "Tags": [
```

`{`

```json
            "TagKey": "test",
            "TagValue": "admin"
```

`]`

### Appendix

#### Error codes

##### Client error codes

**Common errors**

| Error code | Description | HTTP status code |
|---|---|---|
| MissingParameter | The input parameter "parameter name" that is mandatory for processing this request is not supplied. | 400 |
| InvalidParameter | The specified parameter "Action or Version" is not valid. | 400 |
| InvalidAccessKeyId.No tFound | The Access Key ID provided does not exist in our records. | 404 |
| IncompleteSignature | The request signature does not conform to Aliyun standards. | 400 |
| IllegalTimestamp | The input parameter "Timestamp" that is mandatory for processing this request is not supplied. | 400 |
| InvalidOwnerId | The specified OwnerId is not valid. | 400 |
| InvalidOwnerAccount | The specified OwnerAccount is not valid. | 400 |
| InvalidOwner | OwnerId and OwnerAccount can't be used at one API access. | 400 |
| Throttling | Request was denied due to request throttling. | 400 |
| InvalidAction | The specified action is not valid. | 403 |
| ActionUnauthorized | The specified action is not available for you | 403 |
| UnsupportedHTTPMeth od | This http method not supported. | 403 |
| UnsupportedParamete r | The parameter "<parameter name>" is not supported. | 400 |
| Forbidden.InstanceNot Found | The specified DB instance does not exist. | 404 |
| Forbidden.RAM | The user is not authorized to operate the specified resource, or this operation does not support RAM. | 403 |
| Forbedden.NotSupport RAM | This action does not support accessed by RAM mode. | 403 |
| Forbidden.RiskControl | This operation is forbidden by Aliyun Risk Control system. | 403 |
| InsufficientBalance | Your account does not have enough balance. | 400 |
| Forbidden.Authenticati on | This operation is forbidden by Aliyun Realname Authentication system. | 403 |

| Invalid<parameter name>.ValueNotSupp orted | The specified parameter "parameter name" is not valid. | 400 |
|---|---|---|
| Invalid<parameter name>.Malformed | The specified parameter "parameter name n" is not valid. | 400 |
| InvalidParameter | The specified parameter "parameter name n" is not valid. | 400 |

**Specific errors**

| Error code | Description | HTTP status code |
|---|---|---|
| InvalidRegionId.NotFou nd | The DBInstanceId provided does not exist in our records. | 404 |
| InvalidSecurityIPList.D uplicate | The Security IP address is not in the available range or occupied. | 400 |
| InvalidSecurityIPListLe ngth.Malformed | The security IP address is beyond the available range or is already used. | 400 |
| InvalidEngineVersionIn Region.NotAvailable | The EngineVersion in the Region is not available. | 403 |
| InvaildEngineInRegion. NotAvailable | The Engine in the Region is not available. | 403 |
| InvaildDBInstanceClas sInRegion.NotAvailable | The DBInstanceClass in the Region is not available. | 403 |
| OperationDenied | The resource is out of usage. | 403 |
| RegionUnauthorized | There is no authority to create instance in the specified region. | 403 |
| QuotaExceeded.Create Instance | The quota of create instance exceeds. | 403 |
| InvalidDBInstanceId.N otFound | The specified DBInstanceId does not exist. | 404 |
| MissingParameter | The input parameters "DBInstanceClass" and "DBInstanceStorage" all blank or no change. | 400 |
| OperationDenied.DBIn stanceType | The operation is not permitted due to type of instance. | 400 |
| OperationDenied.DBIn stanceStorageReduce | The operation is not permitted due to reduce storage. | 403 |
| OperationDenied.DBIn stanceStatus | The operation is not permitted due to instance status. | 403 |
| DependencyViolation | The operation is not permitted due to instance mount read only or guard instance. | 403 |
| InvalidConnectionStrin gPrefix.Duplicate | The connection string is not in the available range or occupied. | 400 |

| QuotaExceeded.Switch Time | The quota of switch time exceed. | 400 |
|---|---|---|
| OperationDenied.Lock Mode | The operation is not permitted due to lock of instance. | 403 |
| InvalidSecurityIps.Dupl icate | The quota of security ip exceeds. | 400 |
| OperationDenied.Curre ntEngineVersion | The operation is not permitted due to specified current version. | 400 |
| OperationDenied.Read OnlyDBInstanceLower | The operation is not permitted due to higher read only instance version . | 403 |
| OperationDenied.Guar dDBInstanceLower | The operation is not permitted due to higher guard instance version . | 403 |
| OperationDenied.Mast erDBInstanceState | The status of the specified master instance does not support this operation. | 403 |
| QuotaExceeded.DBNa me | The quota of db exceeds. | 400 |
| InvalidDBName.Duplic ate | The specified DB name is invalid or already exists. | 400 |
| InvalidParameter.Keyw ord | The specified DBName is a reserved keyword. | 400 |
| OperationDenied.DBSt atus | The status of the database does not support this operation. | 403 |
| OperationDenied.DBIn stanceEngine | The operation is not permitted due to engine of instance. | 403 |
| FTPServiceUnavailable | The service is unavailable now; wait several minutes and try again. | 403 |
| QuotaExceeded.Uploa d | The quota of file exceeds. | 403 |
| InvalidFileName.NotCo mpleted | The specified "FileName" is not completed . | 404 |
| InvalidFileName.NotAv ailable | The specified "FileName" is not Available . | 404 |
| QuotaExceeded.FileSiz e | The quota of file size exceeds. | 403 |
| QuotaExceeded.DBInst anceStorage | The quota of instance storage exceeds. | 403 |
| InvalidDBInfo.Malform ed | The specified parameter "DBInfo" is not valid or db not exist. | 400 |
| OperationDenied.Regi on | The operation is not permitted due to different region. | 403 |

| OperationDenied.Engi ne | The operation is not permitted due to different engine. | 403 |
|---|---|---|
| OperationDenied.DBIn stanceId | The operation is not permitted due to DBInstanceId and SourceDBInstanceId is same. | 403 |
| InvalidTaskId.NotFoun d | The ImportId provided does not exist in our records. | 400 |
| OperationDenied.Incor rectTaskStatus | The operation is not permitted due to status of import. | 403 |
| InvalidAccountName.k eyword | The specified AccountName is a reserved keyword. | 400 |
| InvalidAccountName.D uplicate | The specified AccountName already exists. | 400 |
| QuotaExceeded.Accou ntName | The quota of account exceeds. | 403 |
| OperationDenied.Acco untStatus | The status of the account does not support this operation. | 403 |
| InvalidDBName.NotFo und | The specified database does not exist. | 404 |
| OperationDenied.Acco untType | The operation is not permitted due to type of account. | 403 |
| OperationDenied.Back upJobExists | You cannot perform this operation; a backup job exists. | 403 |
| OperationDenied.NoDa tabase | The operation is not permitted due to no database. | 403 |
| InvalidStartTimeAndEn dTime.Malformed | The EndTime must be later than or equal to the StartTime. | 400 |
| OperationDenied.Back upJobExists | You cannot perform this operation; a backup job exists. | 403 |
| InvalidBackupId.NotFo und | The BackupId provided does not exist in our records. | 404 |
| OperationDenied.NotF oundBackup | The operation is not permitted due to no backup. | 403 |
| OperationDenied.Back upStatus | The operation is not permitted due to type of backup. | 403 |
| OperationDenied.Back upMethod | The operation is not permitted method of backup. | 403 |
| OperationDenied.Tem pDBInstanceExists | You cannot perform this operation; a temp instance exists. | 403 |
| Forbidden.Authenticati on | The operation is forbidden by Aliyun Realname Authentication System. | 403 |

| IncorrectDBInstanceCo nnType | Current DB instance conn type does not support this operation. | 404 |
|---|---|---|
| IncorrecttVpcId.Mismat ch | The specified parameter "VpcId" is not valid. | 400 |
| IntranetNetTypeNotExi sts | Current DB instance net type does not support this operation. | 404 |
| InvalidDBInstanceNam e.NotFound | The DBInstanceId provided does not exist in our records. | 403 |
| InvalidConnectionMod e.ValueNotSupported | The specified parameter "ConnectionMode" is not valid. | 400 |
| InvalidConnectionStrin g.Duplicate Specified | connection string already exists in the Aliyun RDS. | 403 |
| InvalidConnectionStrin g.Duplicate Specified | connection string or port want to be modified is the same with current net type. | 400 |
| InvalidConnectionStrin gPrefix.Duplicated | The specified connection string already exists. | 403 |
| InvalidCurrentConnecti onString.NotFound | Specified current connection string doesn't exist. | 400 |
| InvalidDBInstanceId.N otFound | The specified DBInstanceId does not exist. | 400 |
| InvalidDBInstanceId.Q uotaExceeded | The quota of instance id exceeds. | 400 |
| InvalidDBInstanceNetT ype.NotFound | The Specified DB instance net type is not found. | 404 |
| InvalidDBinstanceNetT ype.ValueNotSupport | The specified parameter "DBinstanceNetType" is not valid. | 400 |
| InvalidDBInstanceType .ValueNotSupport | The specified parameter "DBInstanceType" is not valid. | 400 |
| InvalidEngineVersion. Malformed | The specified parameter "EngineVersion" is not valid. | 400 |
| InvalidInstanceNetwor kType.ValueNotSuppor ted | The specified parameter "InstanceNetworkType" is not valid. | 400 |
| InvalidParameter | The specified parameter "dbInstanceId" is not valid. | 400 |
| InvalidPort.Malformed | Specified port is not valid. | 400 |
| InvalidPrivateIpAddres s.Duplicated | Specified private IP address is duplicated. | 400 |
| InvalidPrivateIpAddres s.Mismatch | Specified private IP address is not in the CIDR block of virtual switch. | 400 |

| InvalidVPCId.NotFound | The specified connection string or port does not match the current network type. | 400 |
|---|---|---|
| InvalidVSwitchId.Mism atch | Specified instance and virtual switch are not in the same zone. | 400 |
| InvalidVSwitchId.NotFo und | Specified virtual switch is not found in specified VPC. | 400 |
| NetTypeExists | Specified net type already existed. | 400 |
| NetTypeExists | Specified public net type already existed. | 403 |
| OperationDenied.DBIn stanceNetType | The network type of the specified instance does not support this operation. | 403 |
| OperationDenied.DBIn stanceStatus | The specified connection string or port does not match the current network type. | 403 |
| OperationDenied.DBIn stanceType | The operation is not permitted due to type of instance. | 403 |
| OperationDenied.Lock Mode | The instance is locked. | 403 |
| OperationDenied.Switc h | Specified instance cannot be switched. | 400 |
| OperationDenied.Switc h | Specified instance cannot be switched to VPC. | 403 |
| OperationDenied.Switc hToVPC | Specified instance cannot be switched to VPC. | 403 |
| OperationDenied | The requested resource is sold out in the specified zone; try other types of resources or other regions and zones. | 403 |
| OperationDenied | The vpc cloudinstanceIp is use, please check params. | 406 |
| OperationDenied | The vpc service is error, please check params. | 400 |
| PARAMETER ERROR _ | The vpc request parameter may not be null. | 406 |
| PARAMETER MUST NO _ _ T NULL _ | The parameter must not be null. | 406 |
| PublicConnectionExists | PublicConnection exists. | 403 |
| bpcIzNoNotEqualsRds MultIzNo | Specified vpc IzNo not equal rds IzNo. | 400 |
| IncorrectDBInstanceSt ate | CurrentDB instance state does not support this operation. | 403 |
| IncorrectDBInstanceTy pe | CurrentDB instance type does not support this operation. | 400 |

| IncorrectDBInstanceLo ckMode | CurrentDB instance lock mode does not support this operation. | 400 |
|---|---|---|
| ParamNotSupportedFo rCurrentVersion | Parameteris not supported for current version. | 400 |
| InvalideStatus.Format | MigrateTask Status is not valid. | 400 |
| EngineVersionNotSupp orted | EngineVersion specified cannot be replicate with the source DB Instance. | 400 |
| EngineNotSupported | Engine specified cannot be supported the operation.. | 400 |
| ConnectionModeNotSu pported | ConnectionMode specified cannot be replicate with the source DB Instance. | 400 |
| InvalidConfigurationVa lue.Malformed | Specified ConfigurationValue is not valid. | 403 |
| InvalidConfigurationVa lueStatus.Malformed | Specified ProxyConfigurationValue (status) is not valid.. | 403 |
| InvalidConfigurationVa lueOrther.Malformed | Specified ProxyConfigurationValue (check interval seconds or _ _ max failed login attempts or blocking seconds ) _ _ _ _ is not valid. | 403 |
| ProxyConnectionPersis tExists | Specified same ProxyConnectionPersist already exists. | 400 |
| ProxyConnectionPersis t.NotFound | Specified same ProxyConnectionPersist already exists. | 400 |
| ProxyConnectionPersis t.NotFound | Specified ProxyConnectionPersist is not found. | 400 |
| ProxyConnectionPersis tParametersInvalid | ProxyConnectionPersist parameter out of range | 400 |
| InvalidConfigValue | ProxyConnectionPersist parameter config table not exits or data error. | 400 |
| InvalidDBInstance.Not Found | Specified instance does not exist or not support. | 400 |
| ProxyConnectionPersis t.NotFound | Specified ProxyConnectionPersist is not found. | 400 |
| ProxyConnectionPersis tParametersInvalid | ProxyConnectionPersist parameter out of range. | 400 |
| InvalidConfigValue | parameter config table not exits or data error. | 400 |

##### Server error codes

| Error code | Error message | HTTP status code |
|---|---|---|

| ServiceUnavailable | The request has failed due to a temporary failure of the server. | 503 |
|---|---|---|
| InternalError | The request processing has failed due to some unknown error, exception or failure. The request processing | 500 |

#### Instance types

Table 1. Instance types

| Instance type | vCPU | Memory (MB) | Storage space (GB) | Storage space (Mbit/s) | Disk type |
|---|---|---|---|---|---|
| gpdb.group.segsdx 1 | 1 | 8,192 | 80 | 150 | SSD |
| gpdb.group.segsdx 2 | 2 | 16,384 | 160 | 300 | SSD |
| gpdb.group.segsdx 16 | 16 | 131,072 | 1,280 | 2,400 | SSD |

#### Performance parameters table

| Parameter name | Metric | Unit | Description |
|---|---|---|---|
| adbpg segment cnt _ _ | Compute node count | None | The total number of Segment nodes in the instance, collected every hour. |
| adbpg instance dis _ _ k used mb _ _ | Total storage usage of the instance | MB | The sum of storage space actually used by all Segment nodes. |
| adbpg instance dis _ _ k usage percent _ _ | Total storage utilization of the instance | % | The storage usage of all Segment nodes divided by the reserved storage space of all Segment nodes in the instance. |
| node master conne _ _ ction count _ | Coordinator node connection count | None | The number of connections to the Master node. |
| node segment con _ _ nection count _ | Compute node connection count | None | The number of connections to the Segment node. |
| node segment wor _ _ kfile used mb _ _ | Size of temporary disk-spilled files | MB | The size of files temporarily written to disk when computations on the Segment node exceed available memory. |

| node cpu used per _ _ _ cent | CPU utilization | % | The CPU utilization of the Master node or Segment node. |
|---|---|---|---|
| node mem used p _ _ _ ercent | Memory utilization | % | The memory utilization of the Master node or Segment node. |
| node disk iops per _ _ _ cent | I/O utilization | % | The I/O utilization of the Master node or Segment node. |
| node disk used mb _ _ _ | Storage usage | MB | The storage usage of each Segment node. |
| node disk usage p _ _ _ ercent | Storage utilization | % | The storage usage of each Segment node divided by its preset space. |
| adbpg rsq cost _ _ | Query cost for resource queue | None | Represents the total estimated cost of all queries allowed to run under the current queue. A value of -1 for rsqCostLimit indicates no limit. rsqCostValue represents the cumulative cost of all currently running queries. |
| adbpg rsq count _ _ | Query concurrency for resource queue | None | Represents the number of concurrent queries allowed to run under the current queue. If the concurrency limit is reached, subsequent queries must wait in line. rsqCountLimit is the concurrency limit. A value of -1 means no limit. rsqCountValue represents the number of concurrently running queries. |
| adbpg rsq memory _ _ | Memory usage for resource queue queries | Byte | Represents the total memory used by all queries allowed to run under the current queue. rsqMemoryLimit is the total memory limit. A value of -1 means no limit. rsqMemoryValue represents the memory used by running queries. |
| adbpg rsq waiters _ _ | Number of waiting queries in resource queue | None | rsqwaiters represents the number of queries belonging to the current queue that are waiting due to insufficient resources and cannot acquire a slot in the resource queue. When the number of running queries reaches the concurrency limit, new queries entering the queue may be unable to obtain a resource group operation and must wait until resources become available to support new queries. These queries appear in the waiting state in the pg stat activity view. _ _ |

| adbpg rsq holders _ _ | Number of running queries in resource queue | None | rsqholders represents the number of statements belonging to the current queue that have acquired a resource queue slot and can begin execution. This metric shows the number of queries that have obtained a slot in the queue, but it does not necessarily mean these queries are in an active state. During execution, these queries may continue to wait for other system resources (such as row locks), and during this time, the resource queue slots they occupy will not be released. Note In most cases, the value of rsqcountvalue equals rsqholders. In rare cases, rsqholders may be greater than rsqcountvalue, which can occur if a system anomaly causes a query to finish execution without releasing its resource queue lock. If a significant discrepancy between rsqholders and rsqcountvalue persists for a long time, contact an engineer for troubleshooting. |
|---|---|---|---|
| adbpg db qps _ _ | Instance QPS | None | The QPS metric indicates the total number of read queries processed per second by the database instance. Query statements include SELECT, SELECT INTO, SELECT FOR UPDATE, and FETCH statements. |
| adbpg db tps _ _ | Instance TPS | None | The TPS metric indicates the total number of write operations processed per second by the database instance. Write operations include INSERT, UPDATE, DELETE, and INSERT INTO SELECT statements. |

Table 1. Performance parameters table

#### Instance states

Table 1. Instance states

| State | Description |
|---|---|
| Creating | The instance is being created. |
| Running | The instance is running. |
| Deleting | The instance is being deleted. |
| Rebooting | The instance is being restarted. |
| DBInstanceClassChanging | The instance specifications are being changed. |

| Transfering | The instance is being migrated. |
|---|---|
| EngineVersionUpgrading | The engine version is being upgraded. |
| TransferingToOtherInstance | The data is being migrated to other AnalyticDB for PostgreSQL instances. |
| GuardDBInstanceCreating | The disaster recovery instance is being created. |
| Restoring | The instance is being restored from a backup. |
| Importing | Data is being imported into the instance. |
| ImportingFromOtherInstance | Data is being imported into the instance from another AnalyticDB for PostgreSQL instance. |
| DBInstanceNetTypeChanging | The network type is being changed. |
| GuardSwitching | The instance is undergoing a failover. |

#### Terms

Table 1. Terms

| Term | Full name | Description |
|---|---|---|
| DBInstance | database instance | A database service process that takes up physical memory independently. You can configure different memory size and disk space. The memory size determines the performance of the instance, such as the IOPS and connections. |
| DBInstanceId | database instance ID | A globally unique name that identifies an instance. |
| Group | compute node | A compute node is the minimum computing and resource storage unit of an AnalyticDB for PostgreSQL database that you can purchase. |
| DBInstanceClas s | compute node type | The types are as follows: gpdb.group.segsdx1: 1 vCPU, 8 GB of memory, and 80 GB of SSD storage space. gpdb.group.segsdx2: 2 vCPUs, 16 GB of memory, and 160 GB of SSD storage space. gpdb.group.segsdx16: 16 vCPUs, 128 GB of memory, and 1.28 TB of SSD storage space. Each compute node consists of a primary node and a secondary node that have identical specifications. |

| DBInstanceGrou pCount | node count | The number of compute nodes in the AnalyticDB for PostgreSQL instance that you have purchased. For example: If the value of DBInstanceClass is gpdb.group.segsdx2, the instance has two compute nodes. Total available resources: 4 vCPUs, 32 GB of memory, and 320 GB of SSD storage space. For resource and performance reasons, the valid value of DBInstanceGroupCount strictly corresponds to DBInstanceClass: gpdb.group.segsdx1: 2 gpdb.group.segsdx2: 2, 4, and 8 gpdb.group.segsdx16: 2 and 4 |
|---|---|---|
| DB Account | database account | An account identifies the access permissions on a database. A database can be created with multiple accounts, and an account can be associated with multiple databases. |
| AccountName | database account name | The name of a database account identifies the account. The name must be unique among all the database accounts that are in the same instance. |
| Region | region | The region indicates the data center in the specified region. |

## Appendixes

### STS overview

#### What is STS?

Apsara Stack Security Token Service (STS) allows you to manage temporary credentials to your Apsara Stack resources. Resource Access Management (RAM) provides RAM users and roles. A RAM role does not have permanent identity credentials. A RAM role can be assumed for Apsara Stack resource access only by using an STS token. When an STS token is issued, you can specify a validity period and access permissions for the STS token.

**Use an STS token to assume a RAM role**

An authorized RAM user can use an AccessKey pair to call the AssumeRole operation. This way, the RAM user can obtain an STS token of a RAM role and use the STS token to access Apsara Stack resources.

**Benefits**

STS tokens reduce the risks of AccessKey pair leaks. An AccessKey pair is a long-term credential for a RAM user. STS tokens are temporary credentials. You can specify a validity period for an STS token. The token automatically becomes invalid when it expires. You do not need to rotate STS tokens on a regular basis. You can attach custom policies to STS tokens for flexible and fine-grained authorization.

#### AssumeRole

Obtains a Security Token Service (STS) token to assume a RAM role. In this operation, an Alibaba Cloud account is used as the trusted entity of the Resource Access Management (RAM) role.

**Request parameters**

| Parameter | Type | Requ ired | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AssumeRole | The operation that you want to perform. Set the value to AssumeRole. |
| RoleArn | String | Yes | acs:ram::123456 789012****:role/ adminrole | The Alibaba Cloud Resource Name (ARN) of the RAM role. The trusted entity of the RAM role is an Alibaba Cloud account. |

| Parameter | Type | Requ ired | Example | Description |
|---|---|---|---|---|
| RoleSessionNa me | String | Yes | alice | The custom name of the role session. You can specify the value of this parameter based on your business requirements. In most cases, this parameter is set to the identity of the user who calls the operation, such as the username. In ActionTrail logs, you can distinguish the users who assume the same RAM role to perform operations based on the value of the RoleSessionName parameter. This way, you can perform user-specific auditing. The value must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores ( ). _ |
| Policy | String | No | {"Statement": [{"Action": ["*"],"Effect": "Allow","Resourc e": ["*"]}],"Version":" 1"} | The policy that specifies the permissions of the returned STS token. You can use this parameter to grant the STS token fewer permissions than the permissions granted to the RAM role. The value of the parameter must be 1 to 1,024 characters in length. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6894B13B-6D71- 4EF5-88FA- F32781734A7F | The ID of the request. |
| Credentials | None | None | The access credentials. |
| AccessKeyId | String | STS.L4aBSCSJVMuK g5U1**** | The AccessKey ID. |
| AccessKeySecret | String | ****************************************** | The AccessKey secret. |
| SecurityToken | String | ******** | The STS token. |

| nalyticDB for Postgre | SQL Devel |   |   |
|---|---|---|---|

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

**Call an API operation to obtain the STS AccessKey triplet.**

In the following sample code, the `Sts::AssumeRole::2015-04-01` operation is used to obtain the triplet.

```java
package com.aliyuns.test; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; import org.apache.commons.lang3.StringUtils; public class STSAccessKeyDemo {
    public static void main(String[] args) {
//CreateandinitialieaDefaltAcsClientinstance
```

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
        // Replace "sts.aliyuns.com" with the actual endpoint of the STS token. In most
cases, the STS token is in the following format: stsvpc.${global:region}.${global:internet-domain}.
        request.setSysDomain("sts.aliyuns.com");
        request.setSysProduct("Sts");
        request.setSysAction("AssumeRole");
        request.setSysVersion("2015-04-01");
        request.setSysMethod(MethodType.POST);
        request.setHttpContentType(FormatType.FORM);
        // Replace "<yourRoleSessionName>" with the alias that you specify in this API
operation for the role session. It is a business parameter.
        request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
        // Replace "<yourRoleArn>" with the actual ARN that you obtain in the preceding
step for the RAM role.
        request.putQueryParameter("RoleArn", "<yourRoleArn>");
        try {
            CommonResponse response = client.getCommonResponse(request);
            String assumeRole = response.getData();
            if (StringUtils.isEmpty(assumeRole)) return;
            JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
            JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
            // Obtain the STS triplet.
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

**Call examples**

In the following sample code, the `DescribeZones` operation in Elastic Compute Service (ECS) is used.

```java
package com.aliyuns.test; import com.aliyuncs.CommonRequest; importcomaliyuncsCommonResponse;
```

```java
import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class DescribeZonesDemo {
    public static void main(String[] args) {
        // Replace "<yourRegionID>" with the actual region ID.
        // Replace "<yourStsAccesskey>" and "<yourStsAccessKeySecret>" with the
AccessKey ID and secret in the STS triplet that you obtain in the preceding step.
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
        // Replace "<yourStsToken>" with the STS token in the STS triplet that you obta
in in the preceding step.
        request.putQueryParameter("SecurityToken", "<yourStsToken>");
        // Specify the resource set ID. It is optional.
        // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
        // Specify the organization ID. It is required.
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

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | The parameter RoleArn is wrongly formed. | The error message returned because the ARN format of the RAM role is invalid. |
| 400 | InvalidParameter.Role Arn | The parameter RoleArn is wrongly formed. | The error message returned because the ARN format of the RAM role is invalid. |
| 400 | InvalidParameter.Role SessionName | The parameter RoleSessionName is wrongly formed. | The error message returned because the format of the RoleSessionName parameter is invalid. The value must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores ( ). _ |
| 400 | InvalidParameter.Dura tionSeconds | The Min/Max value of DurationSeconds is 15min/1hr. | The error message returned because the value of the DurationSeconds parameter is invalid. The value must be greater than or equal to 900 and less than or equal to the MaxSessionDuration value. |
| 400 | InvalidParameter.Polic yGrammar | The parameter Policy has not passed grammar check. | The error message returned because the syntax of the specified policy is invalid. |
| 400 | InvalidParameter.Polic ySize | The size of Policy must be smaller than 1024 bytes. | The error message returned because the length of the specified policy string exceeds the upper limit. The policy string can be up to 1,024 characters in length. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 403 | NoPermission | You are not authorized to do this action. You should be authorized by RAM. | The error message returned because the STS token does not have the required permissions. |
| 404 | EntityNotExist.Role | The specified Role not exists. | The error message returned because the specified RAM role does not exist. |
| 500 | InternalError | STS Server Internal Error happened. | The error message returned because an internal server error has occurred. |
