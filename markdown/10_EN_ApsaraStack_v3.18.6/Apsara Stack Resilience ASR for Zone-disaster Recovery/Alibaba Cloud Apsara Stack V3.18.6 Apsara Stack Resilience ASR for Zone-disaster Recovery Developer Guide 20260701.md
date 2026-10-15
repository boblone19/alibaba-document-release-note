---
title: "Apsara Stack Resilience ASR for Zone-disaster Recovery Developer Guide 20260701"
product_version: "V3.18.6"
pdf_pages: 118
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 Apsara Stack Resilience ASR for Zone-disaster Recovery Developer Guide 20260701.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E5%90%8C%E5%9F%8E%E5%AE%B9%E7%81%BEASR/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Apsara%20Stack%20Resilience%20ASR%20for%20Zone-disaster%20Recovery%20Developer%20Guide%2020260701.pdf"
converter: line-classifier (PyMuPDF)
---

# Apsara Stack Resilience ASR for Zone-disaster Recovery Developer Guide 20260701

Apsara Stack Resilience ASR for Zone-disaster Recovery

## API call flow

Apsara Stack lets you call APIs of the Zone-Disaster Recovery Management Platform (ASR) through the POP Gateway.

**Flowchart**

The following figure shows the API call flow for ASR.

**Steps**

1. Obtain API information.
For more information, see API Reference.
2. Obtain the AccessKey ID and AccessKey secret. For more information, see Obtain an
AccessKey.
3. Obtain the Endpoint and Region ID for ASR. For more information, see Obtain API
information and its endpoint.
4. Obtain the SDK package and SDK core library for ASR. For more information, see Calling
Apsara Stack APIs using POP Gateway.
5. Call an API operation for ASR.
ASR for Zone-disaster Recovery Apsara Stack Resilience

## Preparations

### Obtain an AccessKey

This topic describes how to obtain an AccessKey ID and an AccessKey secret.

**Background information**

An AccessKey authenticates the identity of a request sender. It uses symmetric encryption and consists of an AccessKey ID and an AccessKey secret. The AccessKey ID identifies the user, and the AccessKey secret is a string used to create an encrypted signature. The Apsara Uni-manager Management Console provides personal AccessKeys and organization AccessKeys. Personal account AccessKeys are used to call APIs.

**Note**

Only operations administrators and primary organization administrators can obtain organization AccessKeys.

**Before you obtain a personal account AccessKey, ensure**

**that the logged-on user has the organization backup**

**administrator role. Otherwise, API calls may fail.**

**Obtain a personal account AccessKey**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the page, click the profile picture of the current user, and then
click**Personal Information**.
3. In the**AccessKey**section, you can view the AccessKey information for the personal
account.

**Important**

The AccessKey ID and AccessKey secret are the keys to access your cloud resources. They grant full permissions to your account. You must keep them secure.

**Obtain an organization AccessKey**

**Warning**

Personal account AccessKeys are restricted by the permission system of the Apsara Unimanager Management Console. In contrast, organization AccessKeys have higher permissions. Therefore, an administrator must confirm that the operation is secure.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
Apsara Stack Resilience ASR for Zone-disaster Recovery
2. In the top menu bar, click**Enterprise**.
3. In the navigation pane on the left, choose**Resource Management**>**Organization**
**Management**.
4. In the organization chart, click the name of the target primary organization.
5. Click**Manage AccessKey**.
6. In the dialog box that appears, you can view the organization AccessKey information.

### Obtain API information and its

**endpoint**

Before you begin, you need the following information for the API operation: the product name (code), the API operation name, and the API version.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top menu bar, choose **Platform O&M > Apsara Infrastructure Management >**
**Resource Management**.
3. In the navigation pane on the left, choose **Resource Management > Product Cluster**
**O&M**.
4. In the search box, enter bcmc.
5. Click **Cluster Details**. On the details page, select the **Desired State Configuration** tab.
6. Select kv.conf. Click **Show Content** to view and save the region value.
ASR for Zone-disaster Recovery Apsara Stack Resilience
7. Select the **Service List** tab. Click the bcmc service name to open its details page.
8. Obtain the value of asr.pop.open.endpoint and save it.

### Calling private cloud APIs

**through a POP gateway**

This topic describes how to call private cloud APIs through a Product Open Platform (POP) gateway.

#### Python version

**Prerequisites**

Install the SDK core library and package dependencies using pip.

**Installation code**

After you download the SDK package from the developer portal, run the following command to install it:

```
pip install apsarastack_asr20250916.tar.gz
```

**Installation instructions**

**Obtain the SDK from the developer portal**

1. Log on to the ASCM developer portal and click SDK Sample.
Apsara Stack Resilience ASR for Zone-disaster Recovery
2. From the SDK Type drop-down list, select Premium Edition. Then, select Java as the
language.
3. The sample code is displayed. Click Download Full Project to download the sample project
and the SDK package.

**Import the SDK package**

1. Create a Maven project in one of the following ways.
ASR for Zone-disaster Recovery Apsara Stack Resilience Method 1: Add a Maven project in IDEA. Method 2: Convert an existing project to a Maven project. Right-click the project that you want to convert and select **Add Framework Support**... Select Maven and click OK.
2. In the project's root directory, create a `lib` folder and place the Java SDK package in it, as
shown in the following figure.
3. In the pom.xml file in the project directory, add the dependency for the Java SDK. For the
required code, see the Installation code section.
4. Verify in the Maven pane on the right side of IDEA that the dependency is successfully
imported, as shown in the figure.

**Code sample**

Use the following sample code to call an API. Ensure that the code runs successfully and does not expose private information.

```java
# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import os import sys fromtypingimportList
```

Apsara Stack Resilience ASR for Zone-disaster Recovery

```python
from typing import List from alibabacloud_tea_openapi import models as open_api_models from alibabacloud_tea_util import models as util_models from alibabacloud_darabonba_env.client import Client as EnvClient from alibabacloud_tea_console.client import Client as ConsoleClient from alibabacloud_tea_util.client import Client as UtilClient from apsarastack_asr20250916.client import Client as SddpClient from apsarastack_asr20250916 import models as sddp_models class Sample:
    def __init__(self):
        pass
    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
        region_id: str,
    ) -> SddpClient:
        """
        Initializes a client using an AccessKey ID and an AccessKey secret.
        """
        config = open_api_models.Config()
        # The endpoint.
        config.endpoint = '<yourEndpoint>'
        # Your AccessKey ID.
        config.access_key_id = access_key_id
        # Your AccessKey secret.
        config.access_key_secret = access_key_secret
        # Your zone ID.
        config.region_id = region_id
        return SddpClient(config)
    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        # Special header parameters. Set the organization ID and resource group ID for
resource isolation. Modify these values as needed.
        # When you call an Apsara Stack API, you generally need to provide multiple com
mon header parameters, including x-acs-regionid, x-acs-organizationid, and x-acs-resour cegroupid.
        # For extra parameters, use the method with the WithOptions suffix, such as des
cribeImagesWithOptions(describeImagesRequest, runtime).
        headers = {
            'x-acs-organizationid': '<yourOrganizationId>',
            'x-acs-resourcegroupid': '<yourResourceGroupId>',
            'x-acs-regionId': '<yourRegionId>',
        }
        extends_params = util_models.ExtendsParameters(
            headers=headers
```

ASR for Zone-disaster Recovery Apsara Stack Resilience )

```bash
        # Create and configure runtimeOptions.
        runtime_options = util_models.RuntimeOptions(
            extends_parameters=extends_params
```

)

```bash
        # To ensure secure communication in a production environment, we recommend that
you keep SSL verification enabled. If you must skip SSL certificate verification in a t est environment, you can set the ignoreSSL runtime parameter.
        # Skip SSL certificate verification.
        runtime_options.ignore_ssl = True
        client = Sample.create_client('<yourAccessKeyId>', '<yourAccessKeySECRET>', '<y
ourRegionId>')
        request = sddp_models.ListProtectionGroupRequest()
        request.page_number = 1 # This is a placeholder value. Set the parameter as req
uired.
        request.page_size = 10 # This is a placeholder value. Set the parameter as requ
ired.
        request.protection_name = "bcmctest" # This is a placeholder value. Set the par
ameter as required.
        response = client.list_protection_group_with_options(request, headers,
runtime_options)
        detail = response.body
        ConsoleClient.log(UtilClient.to_jsonstring(detail))
if __name__ == '__main__':
    Sample().main(sys.argv[1:])
```

**Step-by-step example**

1. Initialize the Config object. This object stores configurations such as the AccessKey ID,
AccessKey secret, and endpoint. You can find the endpoint in the ASCM developer portal. Apsara Stack Resilience ASR for Zone-disaster Recovery

```python
@staticmethod def create_client(
        access_key_id: str,
        access_key_secret: str,
        region_id: str,
    ) -> SddpClient:
        """
        Use your AccessKey ID and AccessKey secret to create a client.
        """
        config = open_api_models.Config()
        # endpoint
        config.endpoint = '<yourEndpoint>'
        # Your AccessKey ID
        config.access_key_id = access_key_id
        # Your AccessKey secret
        config.access_key_secret = access_key_secret
        # Your region ID
        config.region_id = region_id
        return SddpClient(config)
```

2. Instantiate the client object.

```
client = Sample.create_client('<yourAccessKeyId>', '<yourAccessKeySECRET>', '<yourRegionId>') request.page_number = 1 // This is a sample value. Replace it with the actual value. request.page_size = 10 // This is a sample value. Replace it with the actual value. request.protection_name = "bcmctest" // This is a sample value. Replace it with the act ual value.
```

3. Create a request for the corresponding API. The request class is named by appending
Request to the API operation name. For example, the request class for the ListProtectionGroup API operation is ListProtectionGroupRequest.

```
request = sddp_models.ListProtectionGroupRequest()
```

4. Set the headers and runtime parameters for the method call.
ASR for Zone-disaster Recovery Apsara Stack Resilience

```
headers = {
            'x-acs-organizationid': '<yourOrganizationId>',
            'x-acs-resourcegroupid': '<yourResourceGroupId>',
            'x-acs-regionId': '<yourRegionId>',
        }
extends_params = util_models.ExtendsParameters(
            headers=headers
```

)

```bash
# Create and configure runtimeOptions
 runtime_options = util_models.RuntimeOptions(
            extends_parameters=extends_params
```

)

```bash
 # To ensure secure communication in a production environment, we recommend that you ke
ep SSL verification enabled. If you must skip certificate verification in a test enviro nment, you can do so using the ignoreSSL runtime parameter.
# Ignore SSL certificate verification.
runtime_options.ignore_ssl = True
```

5. Retrieve the response for the request from the client object.

```
response = client.list_protection_group_with_options(request, headers, runtime_options) detail = response.body ConsoleClient.log(UtilClient.to_jsonstring(detail))
```

7. Use try...except to handle exceptions.

```bash
except Exception as e:
    # Handle the exception
   logging.error(e)
```

#### Java version

**Prerequisites**

This SDK supports Java Development Kit (JDK) versions 8 to 19 on Linux, Mac, and Windows platforms.

**Installation instruction code**

After you obtain the software development kit (SDK) package from the developer portal, you can use the following Maven dependency to manage the package:

```xml
<dependency>
       <groupId>com.aliyun.apsarastack</groupId>
       <artifactId>asr20250916</artifactId>
       <version>3.18.6-SP003-SNAPSHOT</version>
</dependency>
```

**Installation instructions**

**Obtain the SDK from the developer portal**

Apsara Stack Resilience ASR for Zone-disaster Recovery
1. Log on to the ASCM developer portal and click SDK Sample.
2. From the SDK Type drop-down list, select Premium Edition, and then select Java.
3. The sample code is displayed. Click Download Full Project to obtain the sample project and
the SDK package.

**Import the SDK package**

1. Create a Maven project in one of the following ways:
ASR for Zone-disaster Recovery Apsara Stack Resilience Method 1: Add a Maven project in IntelliJ IDEA. Method 2: Convert an existing project to a Maven project. Right-click the project that you want to convert and select **Add Framework Support...**. Select Maven and click OK.
2. In the project's root directory, create a `lib` folder and add the Java SDK package to it, as
shown in the following figure.
3. Add the Java SDK dependency to the `pom.xml` file in the project directory. For the
required code, see the Maven dependency section.
4. In the Maven pane on the right side of IntelliJ IDEA, verify that the dependency is
successfully imported, as shown in the figure.

**Code sample**

Use the following sample code to call an API. Ensure that your code runs correctly and protects sensitive information.

```java
import com.aliyun.apsarastack.asr20250916.Client; import com.aliyun.apsarastack.asr20250916.models.*; import com.aliyun.teautil.models.ExtendsParameters; import com.aliyun.teautil.models.RuntimeOptions; importcomgooglegsonGson;
```

Apsara Stack Resilience ASR for Zone-disaster Recovery

```java
import com.google.gson.Gson; import java.util.HashMap; import java.util.Map; public class Sample {
    public static Client createClient() throws Exception {
        // The AccessKey ID and AccessKey secret of the organization or ASCM user.
        com.aliyun.teaopenapi.models.Config config = new
com.aliyun.teaopenapi.models.Config()
                // Required
                .setAccessKeyId("<yourAccessKeyID>")
                // Required
                .setAccessKeySecret("<yourAccessKeySecret>");
        // The public domain name of the POP API for the product.
        config.endpoint = "<yourEndpoint>";
        return new Client(config);
    }
    public static void main(String[] args_) throws Exception {
        testSwitchInstance();
    }
    public static void testSwitchInstance() throws Exception {
        Client client = createClient();
        SwitchInstanceRequest switchInstanceRequest = new SwitchInstanceRequest();
        RuntimeOptions runtime = new RuntimeOptions();
        Map<String, String> headers = new HashMap<String, String>();
        // The organization ID and resource group ID. Obtain this information from ASCM
for the current account.
        headers.put("x-acs-organizationid", "<yourOrganizatioId>");
        headers.put("x-acs-resourcegroupid", "<yourResourceGroupID>");
        headers.put("x-acs-regionId", "<yourRegionID>");
        runtime.ignoreSSL = true;
        runtime.setExtendsParameters(new ExtendsParameters().setHeaders(headers));
        switchInstanceRequest.setProcessId(97);  // This is a sample value. Replace it
with the actual value.
        switchInstanceRequest.setProcessAction("SWITCH");  // This is a sample value. R
eplace it with the actual value.
        switchInstanceRequest.setInstanceIds("oss-instance1");  // This is a sample val
ue. Replace it with the actual value.
        try {
client.switchInstanceWithOptions(switchInstanceRequest, headers, runtime);
            System.out.println(new Gson().toJson(response.body));
        } catch (Exception error) {
            // Error message
            System.out.println(error.getMessage());
        }
    }
}
```

ASR for Zone-disaster Recovery Apsara Stack Resilience

**Sample steps**

1. Initialize the `com.aliyun.teaopenapi.models.Config` configuration object. This object stores
configurations such as the AccessKey ID, AccessKey secret, and Endpoint. You can find the Endpoint in the ASCM developer portal.

```
// The AccessKey ID and AccessKey secret of the organization or ASCM user. com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config()
     // Required
    .setAccessKeyId("<yourAccessKeyID>")
     // Required
    .setAccessKeySecret("<yourAccessKeySecret>");
// The public domain name of the POP API for the product. config.endpoint = "<yourEndpoint>";
```

2. Instantiate a client. Create a `client` object from the
`com.aliyun.apsarastack.asr20250916.Client` class. Request and response objects are available in the `com.aliyun.apsarastack.asr20250916.models` package.

```
Client client = new Client(config);
```

3. Create a request for the API. The request class follows the naming convention of `API
method name` + `Request`. For example, the request class for the `SwitchInstance` API is `SwitchInstanceRequest`.

```
SwitchInstanceRequest switchInstanceRequest = new SwitchInstanceRequest();
```

4. Set the parameters and headers for the API call.

```
RuntimeOptions runtime = new RuntimeOptions(); Map<String, String> headers = new HashMap<String, String>(); // The organization ID and resource group ID. Obtain this information from ASCM for the current account. headers.put("x-acs-organizationid", "<yourOrganizatioId>"); headers.put("x-acs-resourcegroupid", "<yourResourceGroupID>"); headers.put("x-acs-regionId", "<yourRegionID>"); runtime.ignoreSSL = true; runtime.setExtendsParameters(new ExtendsParameters().setHeaders(headers)); switchInstanceRequest.setProcessId(97); // This is a sample value. Replace it with the actual value. switchInstanceRequest.setProcessAction("SWITCH"); // This is a sample value. Replace i t with the actual value. switchInstanceRequest.setInstanceIds("oss-instance1"); // This is a sample value. Repl ace it with the actual value.
```

5. Use the `client` object to retrieve the response for the request.

```java
client.switchInstanceWithOptions(switchInstanceRequest, headers, runtime); System.out.println(new Gson().toJson(response.body));
```

6. Use a `catch` block to handle errors.

| Language | Version number | Release date | Updates |
|---|---|---|---|
| Java | 3.18.6-SP003 | 2025-09 | Drill APIs for ASR protection groups |
| Python | 3.18.6-SP003 | 2025-09 | Drill APIs for ASR protection groups |

| API name | Version |
|---|---|
| ASR.CheckProductInstance.2025-09-16 | v3.18.6 |
| ASR.CloseProcess.2025-09-16 | v3.18.6 |
| ASR.CreateDisasterRecoveryProcess.2025-09-16 | v3.18.6 |
| ASR.CreateDrillProcess.2025-09-16 | v3.18.6 |
| ASR.CreateHdrReverse.2025-09-16 | v3.18.6 |
| ASR.CreateNextProcess.2025-09-16 | v3.18.6 |
| ASR.ExecuteProcess.2025-09-16 | v3.18.6 |
| ASR.GetDrillPlan.2025-09-16 | v3.18.6 |

Apsara Stack Resilience ASR for Zone-disaster Recovery

```bash
except Exception as e:
    # Handle the exception
    logging.error(e)
```

#### SDK overview

The API sample code in this document is provided for reference only. For complete instructions and parameter descriptions, see the SDK examples and the OpenAPI documentation on the Developer Portal.

**SDK versions**

**API list**

The current SDK supports the following APIs.

| ASR.GetInstanceStatus.2025-09-16 | v3.18.6 |
|---|---|
| ASR.GetPrevProcess.2025-09-16 | v3.18.6 |
| ASR.GetProcessCheck.2025-09-16 | v3.18.6 |
| ASR.GetProcessDetail.2025-09-16 | v3.18.6 |
| ASR.GetProcessEntry.2025-09-16 | v3.18.6 |
| ASR.GetProcessTrace.2025-09-16 | v3.18.6 |
| ASR.GetProtectionGroup.2025-09-16 | v3.18.6 |
| ASR.GetZoneInfo.2025-09-16 | v3.18.6 |
| ASR.ListDrillPlan.2025-09-16 | v3.18.6 |
| ASR.ListDrillProcesses.2025-09-16 | v3.18.6 |
| ASR.ListProcesses.2025-09-16 | v3.18.6 |
| ASR.ListProtectionGroup.2025-09-16 | v3.18.6 |
| ASR.ListProtectionGroupStatistics.2025-09-16 | v3.18.6 |
| ASR.ListProtectionGroupStatus.2025-09-16 | v3.18.6 |
| ASR.SetProcessSwitchStep.2025-09-16 | v3.18.6 |
| ASR.SwitchInstance.2025-09-16 | v3.18.6 |

ASR for Zone-disaster Recovery Apsara Stack Resilience

**Availability**

Some APIs from previous versions are now deprecated or obsolete. This topic describes these deprecated and obsolete APIs. Deprecated APIs are marked as such in your Integrated Development Environment (IDE). The API reference still describes how to call them. Deprecated APIs are typically not supported in future Apsara Stack versions. Apsara Stack Resilience ASR for Zone-disaster Recovery Most obsolete APIs do not have an alternative and are not described in the API reference. However, a few obsolete APIs have alternatives with similar features. IDEA marks deprecated APIs to help developers identify them. Do not use these APIs for new projects.

| Status code | Error code | Error message | Error scenarios |
|---|---|---|---|
| 404 | InvalidProduct.NotFou nd | Cannot find product according to your specified domain. | The Domain parameter is incorrect. The product cannot be found using the specified domain. |
| 404 | InvalidApi.NotFound | The specified API operation is not found. Please check your URL and method. | The API operation does not exist, or it is a private API operation and the current user is not on the authorization list. |
| 400 | InvalidProtocol.NeedSs l | Your request is denied due to a lack of SSL protection. | The API operation must use the HTTPS protocol. |
| 400 | Missing{ParameterNa me} | {ParameterName} is mandatory for this action. | A required parameter is missing. {ParameterName} is replaced with the specific parameter name. |
| 404 | InvalidAccessKeyId.No tFound | Specified access key is not found. | The specified AccessKey ID cannot be found. |
| 400 | InvalidAccessKeyId.Ina ctive | Specified access key is disabled. | The specified AccessKey ID is disabled. |
| 400 | InvalidTimeStamp.For mat | Specified time stamp or date value is not well formatted. | The timestamp format is incorrect. Use the Date or Timestamp format. |
| 400 | InvalidTimeStamp.Expi red | Specified time stamp or date value is expired. | The timestamp is expired. Make sure the device time is synchronized with the server time. The allowed time drift is 15 minutes. |

Apsara Stack Resilience ASR for Zone-disaster Recovery

## Error code information

This topic describes the common error codes and error messages that occur when you call API operations. When you call ASR API operations, you might encounter two types of errors: software development kit (SDK) call exceptions and backend service execution exceptions. If a request to a POP API operation fails, the system returns an error message. This type of error is usually caused by an improper API call. You can adjust the request parameters based on the error message. The following table describes common POP SDK exceptions.

| 413 | PayloadTooLarge | The request payload is too large, the limitation is xxx bytes. | The request body is too large and exceeds the limit of xxx bytes. Reduce the request data size and retry. |
|---|---|---|---|

| Success | Error code | Error message | Error message |
|---|---|---|---|
| false | authenticationFailed | authenticationFailed | Request authentication failed. Check the credentials or permission configuration. |
| false | internalError | Internal Error | An internal error occurred in the ASR service. Retry later or contact technical support. |
| false | instanceCheckError | Product instance check error | An error occurred during the product instance check. Confirm that the instance status is Normal. |
| false | protectionGroupListError | ProtectionGroup list query error! | Failed to get the protection group list. Check the service status. |
| false | protectionGroupStatisticsErro r | ProtectionGroup statistics error! | Failed to get the protection group overview. |
| false | protectionGroupStatusError | Protection group status check error! | An error occurred during the protection group status check. |
| false | protectionGroupDetailError | ProtectionGroup detail query error! | An error occurred while viewing the protection group details. |

Apsara Stack Resilience ASR for Zone-disaster Recovery For backend service exceptions, the API operation still returns a response, but the Success field is false. The response also contains a specific error code and error message. Contact the zone-disaster recovery development team with this error information to locate and resolve the issue.

| false | recoveryProcessQueryError | Recovery process detail query error! | An error occurred during the recovery flow information query. |
|---|---|---|---|
| false | recoveryProcessTraceError | recovery process trace query error! | An error occurred during the switchover log query. |
| false | createNextRecoveryProcessE rror | Create next recovery process error! | Failed to create the next recovery step. Check the current flow status. |
| false | executeRecoveryProcessErro r | Execute recovery process error! | Failed to execute the recovery step. Confirm that the operation conditions are met. |
| false | skipRecoveryProcessError | Skip recovery process step error! | Failed to skip the recovery step. Confirm that this step can be skipped. |
| false | recoveryProcessCloseError | Recovery process close error! | Failed to close the recovery flow. Confirm that the flow is not in an executing state. |
| false | switchInstanceError | switch instance error! | An error occurred during the instance switchover operation. Check the status of the target instance. |
| false | createHdrReverseError | Create hdr reverse error! | The reverse switchover of the HDR protection group failed. Check the synchronization status. |

Apsara Stack Resilience ASR for Zone-disaster Recovery

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageNum ber | Integ er | Body | No | 1 | The page number. |
| PageSize | Integ er | Body | No | 10 | The number of entries per page. |
| Protection Name | Strin g | Body | No | test | The name of the protection group. |
| CheckStat us | Strin g | Body | No | NORMAL | The check status. |
| Protection GroupId | Integ er | Body | No | 10 | The ID of the protection group. |

| Parameter | Type | Example | Description |
|---|---|---|---|

Apsara Stack Resilience ASR for Zone-disaster Recovery

## API reference

This is the API reference content.

### Protection group

#### ListProtectionGroup

This operation lists protection groups. The response contains creation information, instance information, and the current status of each group. Description You can query all protection groups, or filter the results by specifying parameters such as PageNumber.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array | {} | The returned data. |
| - ProtectionGrou pId | Integer | 10 | The ID of the protection group. |
| - ProtectionNam e | String | test | The name of the protection group. |
| -Description | String | test | The description. |
| -CheckStatus | String | NORMAL | The check status. |
| -GmtCreate | Long | 1756107183000 | The time when the group was created. |
| -GmtModified | Long | 1756107183000 | The time when the group was last modified. |
| -CreateUid | String | 999999999 | Creating an account ID |
| -AccountId | String | 999999999 | The Alibaba Cloud account. |
| -Instances | String | rm-xxx | The name of the instance. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. The operation succeeded. failed: false |
| Code | String | 200 | The status code. A value of 200 indicates that the call is successful. |
| Message | String | success | The returned message. |
| ErrorMessage | String | "" | The error message. |
| ErrorCode | String | 500 | The error code. |

ASR for Zone-disaster Recovery Apsara Stack Resilience

| psara Stack Resil | ience |  | ASR for Zone-disaster Recovery |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Path | String | /xxx/ | The URI of the request. |
| Cost | Long | 20 | The time consumed by the API call. Unit: milliseconds (ms). |
| TotalCount | Integer | 100 | The total number of entries in the list. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |

**Examples**

Sample request

```
{ }
```

Sample response `JSON` format ASR for Zone-disaster Recovery Apsara Stack Resilience

```json
{
 "Path":"/xxx/",
 "TotalCount":100,
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "PageSize":10,
 "PageNumber":1,
 "Data":[
  {
   "Instances":"rm-xxx",
   "GmtCreate":1756107183000,
   "Description":"test",
   "AccountId":"999999999",
   "ProtectionGroupId":10,
   "ProtectionName":"test",
   "CheckStatus":"NORMAL",
   "GmtModified":1756107183000,
   "CreateUid":"999999999"
  }
```

`],`

```json
 "ErrorCode":"500",
 "ErrorMessage":"\"\"",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` format

```xml
<Path>/xxx/</Path> <TotalCount>100</TotalCount> <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <Instances>rm-xxx</Instances>
 <GmtCreate>1756107183000</GmtCreate>
 <Description>test</Description>
 <AccountId>999999999</AccountId>
 <ProtectionName>test</ProtectionName>
 <CheckStatus>NORMAL</CheckStatus>
 <GmtModified>1756107183000</GmtModified>
 <CreateUid>999999999</CreateUid>
</Data> <ErrorCode>500</ErrorCode> <ErrorMessage>&quot;&quot;</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Protection GroupIds | Strin g | Body | Yes | 12 | The ID of the protection group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. true: The request was successful. Failed: false. |
| Code | String | 200 | The status code. A value of 200 indicates that the call was successful. |
| Message | String | success | The returned message. |
| ErrorMessage | String | "" | The error message. |
| ErrorCode | String | 500 | The error code. |

Apsara Stack Resilience ASR for Zone-disaster Recovery

#### ListProtectionGroupStatistics

This operation queries overview information for a protection group, including the number of switches, involved products, instances, and the time of the last drill. Description

**Prerequisites**

You can call this operation to query overview information for a protection group, including the number of switches, involved products, instances, and the time of the last drill. You must specify a protection group ID. To obtain the ID, call the ListProtectionGroup operation.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see the documentation about common request parameters.

**Request syntax**

```
POST /api/pop/v1/listProtectionGroupStatistics HTTP/1.1
```

**Request parameters**

**Response parameters**

| SR for Zone-disa Developer Guide·A | ster Recovery PI reference |  | Apsara Stack Resilienc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Path | String | /xxx/ | The URI of the request. |
| Cost | Long | 20 | The time taken to complete the request. Unit: milliseconds (ms). |
| Data | Struct | {} | The returned data. |
| -Instances | Array | [] | The details of the instances. |
| --Product | String | RDS | The cloud product. |
| --NormalCount | Integer | 10 | The number of normal instances for the product. |
| -- AbnormalCoun t | Integer | 10 | The number of abnormal instances for the product. |
| -DrillPlanCount | Integer | 10 | The number of drill plans. |
| -DrillCount | Integer | 10 | The number of drills. |
| -DrillSuccess | Integer | 10 | The number of successful drills. |
| -DrillFailure | Integer | 10 | The number of failed drills. |
| - CrashPlanCou nt | Integer | 10 | The number of contingency plans. |
| -CrashCount | Integer | 10 | The number of contingencies. |
| -CrashSuccess | Integer | 10 | The number of successful contingencies. |
| -CrashFailure | Integer | 10 | The number of failed contingencies. |
| - SwitchCheckC ount | Integer | 10 | The number of switchover checks. |
| - RecoveryChec kCount | Integer | 10 | The number of recovery checks. |

| A | psara Stack Resil | ience |  | ASR for Zone-disaster Recovery Developer Guide·API referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| - SwitchBackCh eckCount | Integer | 10 | The number of failback checks. |
| -SwitchCount | Integer | 10 | The number of switchovers. |
| - SwitchBackCo unt | Integer | 10 | The number of failbacks. |
| - NonProcessCo unt | Integer | 10 | The number of items without an associated process. |

**Examples**

Request example

```
POST /api/pop/v1/listProtectionGroupStatistics HTTP/1.1 { }
```

Sample success response `JSON` format ASR for Zone-disaster Recovery Apsara Stack Resilience

```json
{
 "Path":"/xxx/",
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "Data":{
  "SwitchCheckCount":10,
  "CrashPlanCount":10,
  "SwitchBackCheckCount":10,
  "CrashCount":10,
  "Instances":[
   {
    "NormalCount":10,
    "Product":"RDS",
    "AbnormalCount":10
   }
```

`],`

```json
  "DrillPlanCount":10,
  "NonProcessCount":10,
  "SwitchBackCount":10,
  "DrillCount":10,
  "CrashSuccess":10,
  "SwitchCount":10,
  "CrashFailure":10,
  "DrillFailure":10,
  "RecoveryCheckCount":10,
  "DrillSuccess":10
 },
 "ErrorCode":"500",
 "ErrorMessage":"\"\"",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` format Apsara Stack Resilience ASR for Zone-disaster Recovery

```xml
<Path>/xxx/</Path> <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data>
 <SwitchCheckCount>10</SwitchCheckCount>
 <CrashPlanCount>10</CrashPlanCount>
 <SwitchBackCheckCount>10</SwitchBackCheckCount>
 <CrashCount>10</CrashCount>
 <Instances>
  <NormalCount>10</NormalCount>
  <Product>RDS</Product>
  <AbnormalCount>10</AbnormalCount>
 </Instances>
 <DrillPlanCount>10</DrillPlanCount>
 <NonProcessCount>10</NonProcessCount>
 <SwitchBackCount>10</SwitchBackCount>
 <DrillCount>10</DrillCount>
 <CrashSuccess>10</CrashSuccess>
 <SwitchCount>10</SwitchCount>
 <CrashFailure>10</CrashFailure>
 <DrillFailure>10</DrillFailure>
 <RecoveryCheckCount>10</RecoveryCheckCount>
 <DrillSuccess>10</DrillSuccess>
</Data> <ErrorCode>500</ErrorCode> <ErrorMessage>&quot;&quot;</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### ListProtectionGroupStatus

This operation lists the status of protection groups to check whether they are in a normal state. Description

**Usage notes**

The CanEdit field in the response is for frontend use only. Ignore this field when you make API calls.

**Request headers**

This operation uses common request headers. No special request headers are used. For more information, see Common request parameters.

**Request syntax**

```
POST /api/pop/v1/listProtectionGroupStatus HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Protection GroupIds | Strin g | Body | Yes | 10 | The ID of the protection group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array | {} | The returned data. |
| - ProtectionGrou pId | Integer | 10 | The ID of the protection group. |
| -Status | String | Normal | The status of the protection group. |
| -CanEdit | Boolean | true | Editable |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The return status. true: The request was successful. The operation did not fail. |
| Code | String | 200 | The status code. A value of 200 indicates that the call was successful. |
| Message | String | success | The returned message. |
| ErrorMessage | String | "" | The error message. |
| ErrorCode | String | 500 | The error code. |
| Path | String | /xxx/ | The URI of the request. |
| Cost | Long | 20 | The time consumed by the API call. Unit: milliseconds (ms). |

ASR for Zone-disaster Recovery Apsara Stack Resilience

**Response parameters**

**Examples**

Request example Apsara Stack Resilience ASR for Zone-disaster Recovery

```
POST /api/pop/v1/listProtectionGroupStatus HTTP/1.1 { }
```

Example of a successful response `JSON` format

```json
{
 "Path":"/xxx/",
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "Data":[
  {
   "Status":"Normal",
   "ProtectionGroupId":10,
   "CanEdit":true
  }
```

`],`

```json
 "ErrorCode":"500",
 "ErrorMessage":"\"\"",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` format

```xml
<Path>/xxx/</Path> <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data>
 <Status>Normal</Status>
 <CanEdit>true</CanEdit>
</Data> <ErrorCode>500</ErrorCode> <ErrorMessage>&quot;&quot;</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### GetProtectionGroup

Retrieves the details of a protection group, including the products and instances that the group contains. Description

**Before you begin**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Protection GroupId | Integ er | Body | Yes | 10 | The ID of the protection group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8 | The request ID. |
| Success | Boolean | true | The returned status. true: The request was successful. Failed: false |
| Code | String | 200 | The return code of the request. A value of 200 indicates that the request was successful. |
| Message | String | success | Additional information. |
| ErrorMessage | String | "" | The error message. |
| ErrorCode | String | 500 | The error code. |
| Path | String | /xxx/xx | The URI of the request. |
| Cost | Long | 30 | The time consumed by the API call. Unit: milliseconds (ms). |

ASR for Zone-disaster Recovery Apsara Stack Resilience This operation requires the ProtectionGroupId parameter. Call the ListProtectionGroup operation to retrieve a list of all protection groups. Then, find the ProtectionGroupId that corresponds to the name of your protection group.

**Request headers**

This operation uses common request headers and has no special request headers. For more information about common request parameters, see the corresponding document.

**Request syntax**

**Request parameters**

**Response parameters**

| psara Stack Resil | ience |  | ASR for Zone-disaster Recovery Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Struct | {} | The returned data. |
| -Instances | Array | [] | The list of instances. |
| --ZoneInfo | String | cn-wulan-env10- amtest10000-a | The zone information. |
| --InstanceId | String | "rm-xx" | The instance ID. |
| --InstanceAlias | String | "rm-xx" | The alias of the instance. |
| --Product | String | RDS | The code of the cloud product. |
| -- MasterLocatio n | String | cn-wulan-env10- amtest10000-a | The location of the primary node. |
| --CheckStatus | String | NORMAL | The status of the instance. |
| --CheckTime | Long | 1635143903000 | The timestamp of the last check. |
| --Result | String | success | The returned result. |
| --Info | String | "" | The returned information. |
| -Id | Integer | 10 | The ID of the protection group. |
| - ProtectionNam e | String | test | The name of the protection group. |
| -Description | String | test | The description. |
| -CheckStatus | String | NORMAL | The check status. |
| -GmtCreate | Long | 1756107183000 | The time when the group was created. |
| -GmtModified | Long | 1756107183000 | The time when the group was last modified. |
| -AccountId | String | 999999999 | The ID of the Alibaba Cloud account. |

| SR for Zone-disa Developer Guide·A | ster Recovery PI reference |  | Apsara Stack Resilienc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -CreateUid | String | 999999999 | The UID of the user who created the group. |
| -CanEdit | Boolean | true | Editable |

**Examples**

Request example

```
{ }
```

Response example `JSON` format Apsara Stack Resilience ASR for Zone-disaster Recovery

```json
{
 "Path":"/xxx/xx",
 "RequestId":"F0A8A039-930D-5EC1-97C8",
 "Message":"success",
 "Data":{
  "GmtCreate":1756107183000,
  "Description":"test",
  "AccountId":"999999999",
  "Instances":[
   {
    "MasterLocation":"cn-wulan-env10-amtest10000-a",
    "CheckTime":1635143903000,
    "InstanceId":"\"rm-xx\"",
    "InstanceAlias":"\"rm-xx\"",
    "CheckStatus":"NORMAL",
    "Product":"RDS",
    "Info":"",
    "ZoneInfo":"cn-wulan-env10-amtest10000-a",
    "Result":"success"
   }
```

`],`

```json
  "ProtectionName":"test",
  "CheckStatus":"NORMAL",
  "GmtModified":1756107183000,
  "CreateUid":"999999999",
  "Id":10,
  "CanEdit":true
 },
 "ErrorCode":"500",
 "ErrorMessage":"\"\"",
 "Code":"200",
 "Cost":30,
 "Success":true
}
```

`XML` format ASR for Zone-disaster Recovery Apsara Stack Resilience

```xml
<Path>/xxx/xx</Path> <RequestId>F0A8A039-930D-5EC1-97C8</RequestId> <Message>success</Message> <Data>
 <GmtCreate>1756107183000</GmtCreate>
 <Description>test</Description>
 <AccountId>999999999</AccountId>
 <Instances>
  <MasterLocation>cn-wulan-env10-amtest10000-a</MasterLocation>
  <CheckTime>1635143903000</CheckTime>
  <InstanceId>&quot;rm-xx&quot;</InstanceId>
  <InstanceAlias>&quot;rm-xx&quot;</InstanceAlias>
  <CheckStatus>NORMAL</CheckStatus>
  <Product>RDS</Product>
  <Info></Info>
  <ZoneInfo>cn-wulan-env10-amtest10000-a</ZoneInfo>
  <Result>success</Result>
 </Instances>
 <ProtectionName>test</ProtectionName>
 <CheckStatus>NORMAL</CheckStatus>
 <GmtModified>1756107183000</GmtModified>
 <CreateUid>999999999</CreateUid>
 <Id>10</Id>
 <CanEdit>true</CanEdit>
</Data> <ErrorCode>500</ErrorCode> <ErrorMessage>&quot;&quot;</ErrorMessage> <Code>200</Code> <Cost>30</Cost> <Success>true</Success>
```

#### CheckProductInstance

You can call this operation to check the status of a product instance and determine whether it supports a disaster recovery switchover. API description Before you call this operation, you must confirm which organization owns the instance to prevent unauthorized access. Alibaba Cloud Site Recovery (ASR) does not verify instance ownership.

**Request headers**

This operation has no special request headers. For more information about common request headers, see Common request parameters.

**Request syntax**

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| CloudProd uct | Strin g | Body | Yes | RDS | The cloud product. |
| InstanceId s | Strin g | Body | Yes | rm-2ze8g2am97624 | The instance ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8 | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. failed: false |
| Code | String | 200 | The status code. A value of 200 indicates that the call was successful. |
| Message | String | success | The returned message. |
| ErrorMessage | String | "" | The error message. |
| ErrorCode | String | 500 | The error code. |
| Path | String | /xxx/xxx | The URI of the request. |
| Cost | Long | 20 | The time consumed by the API call. Unit: milliseconds (ms). |
| Data | Struct | {} | The returned data. |
| -Instances | Array | [] | The list of instances. |
| --InstanceId | String | rm- 2ze8g2am97624 | The instance ID. |
| --Available | Boolean | true | Indicates whether the instance is available. |
| --Message | String | message | The returned message. |

Apsara Stack Resilience ASR for Zone-disaster Recovery

**Response parameters**

| ASR for Zone-disa Developer Guide·A | ster Recovery PI reference |  | Apsara Stack Resilienc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -CloudProduct | String | RDS | The cloud product. |

**Examples**

Request example

```json
{ "CloudProduct":"RDS", "InstanceIds":"rm-2ze8g2am97624" }
```

Successful response example `JSON` format

```json
{
 "Path":"/xxx/xxx",
 "RequestId":"F0A8A039-930D-5EC1-97C8",
 "Message":"success",
 "Data":{
  "Instances":[
   {
    "Message":"message",
    "InstanceId":"rm-2ze8g2am97624",
    "Available":true
   }
```

`],`

```json
  "CloudProduct":"RDS"
 },
 "ErrorCode":"500",
 "ErrorMessage":"\"\"",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` format

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| Success | Boolean | true | The return status. true: The request was successful. false: The request failed. |
| Code | String | 200 | The status code. A value of 200 indicates that the call was successful. |

Apsara Stack Resilience ASR for Zone-disaster Recovery

```xml
<Path>/xxx/xxx</Path> <RequestId>F0A8A039-930D-5EC1-97C8</RequestId> <Message>success</Message> <Data>
 <Instances>
  <Message>message</Message>
  <InstanceId>rm-2ze8g2am97624</InstanceId>
  <Available>true</Available>
 </Instances>
 <CloudProduct>RDS</CloudProduct>
</Data> <ErrorCode>500</ErrorCode> <ErrorMessage>&quot;&quot;</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### GetZoneInfo

Retrieves information about the zones that are available when you create a recovery plan. Description You can also call this operation to retrieve information about the zones that are available when you create a protection group.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

**Response data**

| SR for Zone-disa | ster Recovery |  |  |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | success | The message returned. |
| ErrorMessage | String | "" | The error message. |
| ErrorCode | String | 500 | The error code. |
| Path | String | /xxx/ | The URI of the request. |
| Cost | Long | 20 | The time taken to process the request, in milliseconds (ms). |
| Data | Struct | {} | The data returned. |
| -ZoneInfo | String | cn-wulan-env10- amtest10000-a | The information about the zone. |

**Examples**

Request example Successful response example `JSON` format

```json
{
 "Path":"/xxx/",
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "Data":{
  "ZoneInfo":"cn-wulan-env10-amtest10000-a"
 },
 "ErrorCode":"500",
 "ErrorMessage":"\"\"",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` format

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ProcessId | Integ er | Body | No | 1 | The ID of the process. |
| PlanName | Strin g | Body | No | test | The name of the plan. |
| Execution Mode | Strin g | Body | No | MANUAL | The execution mode. |
| ProcessSt atus | Strin g | Body | No | EXECUTING | The status of the process. |

Apsara Stack Resilience ASR for Zone-disaster Recovery

```xml
<Path>/xxx/</Path> <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data>
 <ZoneInfo>cn-wulan-env10-amtest10000-a</ZoneInfo>
</Data> <ErrorCode>500</ErrorCode> <ErrorMessage>&quot;&quot;</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

### Drill plans

#### ListProcesses

You can call this operation to list the steps in a recovery drill process and view details such as the process type, execution mode, and current status. API description This operation is used only for resource processing in upgrade scenarios. Customers must call the ListDrillProcesses operation instead. You can call this operation to query all processes or a specific process. To query all processes, do not specify any parameters. To query a specific process, specify the ProcessId parameter.

**Request headers**

This operation uses only common request headers. For more information, see Common parameters.

**Request syntax**

**Request parameters**

| SR for Zone- Developer Gui | disaster R de·API re | ecovery ference |  |  | Apsara Stack Resilienc |
|---|---|---|---|---|---|

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageNum ber | Integ er | Body | No | 1 | The page number. |
| PageSize | Integ er | Body | No | 100 | The number of entries per page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array | {} | The returned data. |
| -PgId | Integer | 10 | The ID of the protection group. |
| -PlanId | Integer | 16 | The ID of the recovery drill plan. |
| -PlanName | String | test | The name of the plan. |
| -Zone | String | cn-wulan-env10- amtest10000-a | The zone. |
| -ProcessId | Integer | 5 | The ID of the process. |
| -ProcessType | String | DRILL RECOVERY _ | The type of the process. |
| - ProtectionNam e | String | test | The name of the protection group. |
| - ExecutionMod e | String | MANUAL | The execution mode. |
| -ProcessStatus | String | EXECUTING | The status of the process. |
| -AccountId | String | 999999999 | The ID of the Alibaba Cloud account. |
| -CreateUid | String | 999999999 | Create a user ID (UID) |
| -StartTime | Long | 1756112392000 | The time when the process started. |
| -EndTime | Long | 1756112392000 | The time when the process ended. |

**Response parameters**

| A | psara Stack Resil | ience |  | ASR for Zone-disaster Recovery Developer Guide·API referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -OrderId | Integer | 9 | The sort order field. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. true: The request was successful. The operation has not failed. |
| Code | String | 200 | The HTTP status code. A value of `200` indicates that the request was successful. |
| Message | String | success | The message returned. |
| ErrorMessage | String | "" | The error message. |
| ErrorCode | String | 500 | The error code. |
| Path | String | /xxx/ | The URI of the request. |
| Cost | Long | 20 | The time consumed by the request, in milliseconds (ms). |
| TotalCount | Integer | 100 | The total number of entries. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |

**Examples**

Sample request

```
{ }
```

Sample response `JSON` format ASR for Zone-disaster Recovery Apsara Stack Resilience

```json
{
 "Path":"/xxx/",
 "TotalCount":100,
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "PageSize":10,
 "PageNumber":1,
 "Data":[
  {
   "AccountId":"999999999",
   "EndTime":1756112392000,
   "ProcessStatus":"EXECUTING",
   "Zone":"cn-wulan-env10-amtest10000-a",
   "PlanId":16,
   "CreateUid":"999999999",
   "StartTime":1756112392000,
   "ExecutionMode":"MANUAL",
   "PlanName":"test",
   "OrderId":9,
   "ProcessType":"DRILL_RECOVERY",
   "PgId":10,
   "ProtectionName":"test",
   "ProcessId":5
  }
```

`],`

```json
 "ErrorCode":"500",
 "ErrorMessage":"\"\"",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` format Apsara Stack Resilience ASR for Zone-disaster Recovery

```xml
<Path>/xxx/</Path> <TotalCount>100</TotalCount> <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <AccountId>999999999</AccountId>
 <EndTime>1756112392000</EndTime>
 <ProcessStatus>EXECUTING</ProcessStatus>
 <Zone>cn-wulan-env10-amtest10000-a</Zone>
 <PlanId>16</PlanId>
 <CreateUid>999999999</CreateUid>
 <StartTime>1756112392000</StartTime>
 <ExecutionMode>MANUAL</ExecutionMode>
 <PlanName>test</PlanName>
 <OrderId>9</OrderId>
 <ProcessType>DRILL_RECOVERY</ProcessType>
 <PgId>10</PgId>
 <ProtectionName>test</ProtectionName>
 <ProcessId>5</ProcessId>
</Data> <ErrorCode>500</ErrorCode> <ErrorMessage>&quot;&quot;</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### ListDrillProcesses

This operation lists drill processes. The information returned includes the process type, execution mode, and current status. API details You can call this operation to query information about drill processes. To query all processes, do not specify any request parameters. To query a specific process, specify the ProcessId parameter.

**Request headers**

This operation uses only common request headers. For more information, see the documentation about common request parameters.

**Request syntax**

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ProcessId | Integ er | Body | No | 1 | The process ID. |
| PlanName | Strin g | Body | No | test | The plan name. |
| Execution Mode | Strin g | Body | No | MANUAL | The execution mode. |
| ProcessSt atus | Strin g | Body | No | EXECUTING | The process status. |
| PageNum ber | Integ er | Body | No | 1 | The page number. |
| PageSize | Integ er | Body | No | 10 | The number of entries per page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array | {} | The returned data. |
| -PgId | Integer | 1 | The ID of the protection group. |
| -PlanId | Integer | 1 | The ID of the drill plan. |
| -PlanName | String | test | The name of the plan. |
| -Zone | String | cn-wulan-env10- amtest10000-a | The zone. |
| -ProcessId | Integer | 5 | The process ID. |
| -ProcessType | String | DRILL RECOVERY _ | The process type. |
| - ProtectionNam e | String | test | The name of the protection group. |
| - ExecutionMod e | String | MANUAL | The execution mode. |
| -ProcessStatus | String | EXECUTING | The process status. |

ASR for Zone-disaster Recovery Apsara Stack Resilience

**Response parameters**

| A | psara Stack Resil | ience |  | ASR for Zone-disaster Recovery Developer Guide·API referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -AccountId | String | 999999999 | The ID of the Alibaba Cloud account. |
| -CreateUid | String | 999999999 | Creating a UID |
| -StartTime | Long | 1756112392000 | The start time. |
| -EndTime | Long | 1756112392000 | The end time. |
| -OrderId | Integer | 9 | The sorting field. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The return status. true: The request was successful. Failed: false |
| Code | String | 200 | The status code. A value of 200 indicates that the call was successful. |
| Message | String | success | The returned message. |
| ErrorMessage | String | "" | The error message. |
| ErrorCode | String | 500 | The error code. |
| Path | String | /xxx/ | The URI of the request. |
| Cost | Long | 1000 | The time consumed by the operation. Unit: milliseconds (ms). |
| TotalCount | Integer | 100 | The total number of entries. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |

**Examples**

ASR for Zone-disaster Recovery Apsara Stack Resilience Request example

```
{ }
```

Sample response `JSON` format

```json
{
 "Path":"/xxx/",
 "TotalCount":100,
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "PageSize":10,
 "PageNumber":1,
 "Data":[
  {
   "AccountId":"999999999",
   "EndTime":1756112392000,
   "ProcessStatus":"EXECUTING",
   "Zone":"cn-wulan-env10-amtest10000-a",
   "PlanId":1,
   "CreateUid":"999999999",
   "StartTime":1756112392000,
   "ExecutionMode":"MANUAL",
   "PlanName":"test",
   "OrderId":9,
   "ProcessType":"DRILL_RECOVERY",
   "PgId":1,
   "ProtectionName":"test",
   "ProcessId":5
  }
```

`],`

```json
 "ErrorCode":"500",
 "ErrorMessage":"\"\"",
 "Code":"200",
 "Cost":1000,
 "Success":true
}
```

`XML` format

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Zone-disaster Recovery

```xml
<Path>/xxx/</Path> <TotalCount>100</TotalCount> <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <AccountId>999999999</AccountId>
 <EndTime>1756112392000</EndTime>
 <ProcessStatus>EXECUTING</ProcessStatus>
 <Zone>cn-wulan-env10-amtest10000-a</Zone>
 <PlanId>1</PlanId>
 <CreateUid>999999999</CreateUid>
 <StartTime>1756112392000</StartTime>
 <ExecutionMode>MANUAL</ExecutionMode>
 <PlanName>test</PlanName>
 <OrderId>9</OrderId>
 <ProcessType>DRILL_RECOVERY</ProcessType>
 <PgId>1</PgId>
 <ProtectionName>test</ProtectionName>
 <ProcessId>5</ProcessId>
</Data> <ErrorCode>500</ErrorCode> <ErrorMessage>&quot;&quot;</ErrorMessage> <Code>200</Code> <Cost>1000</Cost> <Success>true</Success>
```

#### CloseProcess

Call this operation to shut down a flow. You can shut down a flow after a recovery drill for a protection group is complete or shut it down early if an exception occurs. Description

**Prerequisites**

Obtain the ProcessId of the flow before you call this operation.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see the common request parameters document.

**Request syntax**

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ProcessId | Integ er | Body | Yes | 10 | The ID of the flow. |
| IsForce | Boole an | Body | Yes | false | Specifies whether to forcibly shut down the flow. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | String | 200 | The status code. A value of 200 indicates that the call was successful. |
| Message | String | success | The returned message. |
| ErrorMessage | String | "" | The error message. |
| ErrorCode | String | 500 | The error code. |
| Path | String | /xxx/ | The URI of the request. |
| Cost | Long | 20 | The time consumed by the API call. Unit: milliseconds (ms). |
| Data | Struct | {} | The returned data. |
| -ProcessId | String | 10 | The ID of the flow. |
| -ProcessAction | String | SWITCH | The drill action. |
| -PlanId | Integer | 10 | The ID of the plan. |

ASR for Zone-disaster Recovery Apsara Stack Resilience

**Response parameters**

|  |  |  | ASR for Zone-disaster Recovery |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -ProcessType | String | SWITCH | The type of the flow. |

**Examples**

Sample request

```json
{ "ProcessId":"10", "IsForce":"false" }
```

Sample successful response `JSON` format

```json
{
 "Path":"/xxx/",
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "Data":{
  "ProcessAction":"SWITCH",
  "ProcessType":"SWITCH",
  "PlanId":10,
  "ProcessId":"10"
 },
 "ErrorCode":"500",
 "ErrorMessage":"\"\"",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` format

```xml
<Path>/xxx/</Path> <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data>
 <ProcessAction>SWITCH</ProcessAction>
 <ProcessType>SWITCH</ProcessType>
 <PlanId>10</PlanId>
 <ProcessId>10</ProcessId>
</Data> <ErrorCode>500</ErrorCode> <ErrorMessage>&quot;&quot;</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PlanId | Integ er | Body | Yes | 10 | The ID of the plan. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| Success | Boolean | true | The status of the response. true: The request was successful. The operation has not failed. |
| Code | String | 200 | The status code. A value of 200 indicates that the call was successful. |
| Message | String | success | The returned message. |
| ErrorMessage | String | "" | The error message. |
| ErrorCode | String | 500 | The error code. |
| Path | String | /xxx/ | The URI of the request. |

ASR for Zone-disaster Recovery Apsara Stack Resilience

#### CreateDrillProcess

This operation creates a drill process for a drill plan. After the process starts, you can perform a switchover of the protection group. Description

**Prerequisites**

Before you call this operation, obtain the PlanId of the drill plan.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

**Request parameters**

**Response parameters**

| A | psara Stack Resil | ience |  | ASR for Zone-disaster Recovery Developer Guide·API referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Cost | Long | 20 | The time consumed by the API call. Unit: milliseconds (ms). |
| Data | Struct | {} | The returned data. |
| -ProcessId | String | 10 | The process ID. |
| -ProcessAction | String | SWITCH CHECK _ | The process action. |
| -PlanId | Integer | 4 | The plan ID. |
| -ProcessType | String | DRILL RECOVERY _ | The process type. |

**Examples**

Request example

```json
{ "PlanId":"10" }
```

Response example `JSON` format

```json
{
 "Path":"/xxx/",
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "Data":{
  "ProcessAction":"SWITCH_CHECK",
  "ProcessType":"DRILL_RECOVERY",
  "PlanId":4,
  "ProcessId":"10"
 },
 "ErrorCode":"500",
 "ErrorMessage":"\"\"",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ProcessId | Integ er | Body | Yes | 10 | The flow ID. |
| TraceId | Strin g | Body | Yes | 1760325130967#rm- jp7lct7rd5l61b7t0#1#61 5E81E0-82CA-40C3- 8AC0-F002591EFC1C | The execution record ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|

ASR for Zone-disaster Recovery Apsara Stack Resilience

```xml
<Path>/xxx/</Path> <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data>
 <ProcessAction>SWITCH_CHECK</ProcessAction>
 <ProcessType>DRILL_RECOVERY</ProcessType>
 <PlanId>4</PlanId>
 <ProcessId>10</ProcessId>
</Data> <ErrorCode>500</ErrorCode> <ErrorMessage>&quot;&quot;</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### GetProcessTrace

You can call this operation to retrieve flow logs. It is primarily used to obtain the switchover logs for a protection group. Description You can call this operation to retrieve flow logs. Before you call this operation, you must obtain the ProcessId of the protection group switchover and the TraceId that is returned by the switchover operation.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see the Common request parameters document.

**Request syntax**

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array | {} | The returned data. |
| -TraceId | String | 9A506E30-DA33- 43D6-AACC- C3F85435D890 | The execution record ID. |
| -Product | String | RDS | The cloud product. |
| -ActionType | String | SWITCH | The action type. |
| -StepName | String | dr service check | The step name. |
| -StepMsg | String | dr service status is good | The step information. |
| -GmtCreated | Long | 1760325133000 | The time when the record was created. |
| -GmtModified | Long | 1760325133000 | The time when the record was last modified. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. Failed: false. |
| Code | String | 200 | The status code. A value of 200 indicates that the call was successful. |
| Message | String | success | The returned message. |
| ErrorMessage | String | "" | The error message. |
| ErrorCode | String | 500 | The error code. |
| Path | String | /xxx/ | The URI of the request. |
| Cost | Long | 20 | The time consumed by the operation. Unit: milliseconds (ms). |

Apsara Stack Resilience ASR for Zone-disaster Recovery ASR for Zone-disaster Recovery Apsara Stack Resilience

**Examples**

Sample request

```json
{ "ProcessId":"10", "TraceId":"1760325130967#rm-jp7lct7rd5l61b7t0#1#615E81E0-82CA-40C3-8AC0-F002591EFC1C" }
```

Sample successful response `JSON` format

```json
{
 "Path":"/xxx/",
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "Data":[
  {
   "ActionType":"SWITCH",
   "GmtModified":1760325133000,
   "TraceId":"9A506E30-DA33-43D6-AACC-C3F85435D890",
   "Product":"RDS",
   "StepName":"dr service check",
   "GmtCreated":1760325133000,
   "StepMsg":"dr service status is good"
  }
```

`],`

```json
 "ErrorCode":"500",
 "ErrorMessage":"\"\"",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` format

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ProcessId | Integ er | Body | Yes | 10 | The ID of the flow. |
| ProcessAc tion | Strin g | Body | Yes | SWITCH | The action of the flow. |
| Step | Integ er | Body | Yes | 1 | The step number. |

Apsara Stack Resilience ASR for Zone-disaster Recovery

```xml
<Path>/xxx/</Path> <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data>
 <ActionType>SWITCH</ActionType>
 <GmtModified>1760325133000</GmtModified>
 <TraceId>9A506E30-DA33-43D6-AACC-C3F85435D890</TraceId>
 <Product>RDS</Product>
 <StepName>dr service check</StepName>
 <GmtCreated>1760325133000</GmtCreated>
 <StepMsg>dr service status is good</StepMsg>
</Data> <ErrorCode>500</ErrorCode> <ErrorMessage>&quot;&quot;</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### ExecuteProcess

Call this API to start a switchover flow that executes the steps for switchovers and failbacks within a protection group. API description Before you call this API, obtain the values for the ProcessId and ProcessAction parameters.

**Request headers**

This API uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request syntax**

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| Success | Boolean | true | Indicates whether the call was successful. true: The call was successful. Failed: false |
| Code | String | 200 | The status code. A value of 200 indicates that the call is successful. |
| Message | String | success | The returned message. |
| ErrorMessage | String | "" | The error message. |
| ErrorCode | String | 500 | The error code. |
| Path | String | /xxx/ | The URI of the request. |
| Cost | Long | 20 | The time it takes to call the API. Unit: milliseconds (ms). |

ASR for Zone-disaster Recovery Apsara Stack Resilience

**Examples**

Request example

```json
{ "ProcessId":"10", "ProcessAction":"SWITCH", "Step":"1" }
```

Response example `JSON` format

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ProcessId | Integ er | Body | Yes | 10 | The ID of the flow. |
| ProcessAc tion | Strin g | Body | Yes | SWITCH | The action type of the flow. |

Apsara Stack Resilience ASR for Zone-disaster Recovery

```json
{
 "Path":"/xxx/",
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "ErrorCode":"500",
 "ErrorMessage":"\"\"",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` format

```xml
<Path>/xxx/</Path> <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <ErrorCode>500</ErrorCode> <ErrorMessage>&quot;&quot;</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### CreateNextProcess

You can call this operation to move a drill flow to the next step.

**Prerequisites**

Before you call this operation, you must obtain the ProcessId and ProcessAction.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common parameters.

**Request syntax**

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| IsForce | Boole an | Body | Yes | true | Specifies whether to force the operation. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | String | 200 | The status code. A value of 200 indicates that the call was successful. |
| Message | String | success | The returned message. |
| ErrorMessage | String | "" | The error message. |
| ErrorCode | String | 500 | The error code. |
| Path | String | /xxx/ | The URI of the request. |
| Cost | Long | 20 | The time consumed by the API call. Unit: milliseconds (ms). |
| Data | Struct | {} | The returned data. |
| -ProcessId | String | 10 | The ID of the flow. |
| -ProcessAction | String | SWITCH | The action type of the flow. |
| - ProtectionGrou pId | Integer | 6 | The ID of the protection group. |

ASR for Zone-disaster Recovery Apsara Stack Resilience

**Response parameters**

**Examples**

Sample request Apsara Stack Resilience ASR for Zone-disaster Recovery

```json
{ "ProcessId":"10", "ProcessAction":"SWITCH", "IsForce":"true" }
```

Sample response `JSON` format

```json
{
 "Path":"/xxx/",
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "Data":{
  "ProcessAction":"SWITCH",
  "ProtectionGroupId":6,
  "ProcessId":"10"
 },
 "ErrorCode":"500",
 "ErrorMessage":"\"\"",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` format

```xml
<Path>/xxx/</Path> <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data>
 <ProcessAction>SWITCH</ProcessAction>
 <ProcessId>10</ProcessId>
</Data> <ErrorCode>500</ErrorCode> <ErrorMessage>&quot;&quot;</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### GetInstanceStatus

You can call this operation to retrieve the status of an instance in a protection group. The status includes information such as the location of the primary node and the Recovery Point Objective (RPO). API description

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ProcessId | Integ er | Body | Yes | 10 | The ID of the flow. |
| ProcessAc tion | Strin g | Body | Yes | SWITCH | The type of the flow. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. true: The request was successful. failed: false |
| Code | String | 200 | The status code. A value of 200 indicates that the call was successful. |
| Message | String | success | The returned message. |
| ErrorMessage | String | "" | The error message. |
| ErrorCode | String | 500 | The error code. |
| Path | String | /xxx/ | The URI of the request. |
| Cost | Long | 20 | The time consumed by the API call, in milliseconds (ms). |

ASR for Zone-disaster Recovery Apsara Stack Resilience Before you call this operation, you must obtain the ProcessId of the drill flow.

**Request headers**

This operation uses only common request headers. No special request headers are required. For more information, see Common Request Parameters.

**Request syntax**

**Request parameters**

**Response parameters**

| psara Stack Resil | ience |  | ASR for Zone-disaster Recovery |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Struct | {} | The returned data. |
| - PrevActionStat us | String | [] | The status of the preceding action. |
| - InstanceAction s | Array | [] | A list of instance statuses. |
| --Id | Integer | 1 | The ID of the instance status. |
| --ActionId | Integer | 10 | The action ID. |
| -- ProcessAction | String | RECOVERY CHECK _ | The flow action. |
| --SourceIdc | String | amtest21 | The source data center. |
| --DestIdc | String | amtest22 | The destination data center. |
| --Step | Integer | 1 | The step number. |
| --InstanceId | String | rm- bp1162kryivb8**** | The instance ID. |
| --InstanceAlias | String | test | The alias of the instance. |
| --Info | String | "" | The message. |
| --Product | String | RDS | The cloud product. |
| --StartTime | Long | 1759211487000 | The start time. |
| --EndTime | Long | 1759211487000 | The end time. |
| --ActionStatus | String | INIT | The action status. |
| --Result | String | "" | The returned result. |
| -- ConsumeTime | String | 120 | The time consumed. |

| SR for Zone-disa Developer Guide·A | ster Recovery PI reference |  | Apsara Stack Resilienc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| --TraceId | String | 9A506E30-DA33- 43D6-AACC- C3F85435D890 | The ID of the request record. |
| -- MasterLocatio n | String | cn-wulan-env10- amtest10000-a | The location of the primary node. |
| --SyncDelay | String | { "value": "0", "status": true } | The latency. |
| --SyncStatus | String | { "value": "CheckInfo.Increas eReplica", "status": true } | The latency status. |
| --FailoverType | Struct | {} | The switchover type. |
| ---value | String | AUTOMATIC | Content. |
| ---info | String | AutomaticFailover | The information. |
| -ProcessStatus | String | FINISH | The status of the flow. |
| -ActionStatus | String | INIT | The action status. |
| -StartTime | Long | 1759211487000 | The start time. |
| -EndTime | Long | 1759211487000 | The end time. |
| -ConsumeTime | String | 120 | The execution time. |
| -CurrentStep | Integer | 1 | The current step. |

**Examples**

Sample request

```json
{ "ProcessId":"10", "ProcessAction":"SWITCH" }
```

Sample response `JSON` format Apsara Stack Resilience ASR for Zone-disaster Recovery

```json
{
 "Path":"/xxx/",
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "Data":{
  "InstanceActions":[
   {
    "ProcessAction":"RECOVERY_CHECK",
    "SyncDelay":"{<br/>            \"value\": \"0\",<br/>            \"status\":
true<br/> }",
    "EndTime":1759211487000,
    "InstanceId":"rm-bp1162kryivb8****",
    "StartTime":1759211487000,
    "SyncStatus":"{<br/>            \"value\": \"CheckInfo.IncreaseReplica\",<br/>
\"status\": true<br/> }",
    "Product":"RDS",
    "Step":1,
    "FailoverType":[
     {
      "value":"AUTOMATIC",
      "info":"AutomaticFailover"
     }
```

`],`

```json
    "Info":"",
    "DestIdc":"amtest22",
    "ActionStatus":"INIT",
    "Result":"",
    "MasterLocation":"cn-wulan-env10-amtest10000-a",
    "ActionId":10,
    "InstanceAlias":"test",
    "TraceId":"9A506E30-DA33-43D6-AACC-C3F85435D890",
    "Id":1,
    "SourceIdc":"amtest21",
    "ConsumeTime":"120"
   }
```

`],`

```json
  "EndTime":1759211487000,
  "ProcessStatus":"FINISH",
  "StartTime":1759211487000,
  "CurrentStep":1,
  "ConsumeTime":"120",
  "PrevActionStatus":"[]",
  "ActionStatus":"INIT"
 },
 "ErrorCode":"500",
 "ErrorMessage":"",
 "Code":"200",
 "Cost":20,
 "Success":true
}<br/><br/><br/><br/><br/><br/>
```

`XML` format ASR for Zone-disaster Recovery Apsara Stack Resilience

```xml
<Path>/xxx/</Path> <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data>
 <InstanceActions>
  <ProcessAction>RECOVERY_CHECK</ProcessAction>
  <SyncDelay>{
            &quot;value&quot;: &quot;0&quot;,
            &quot;status&quot;: true
          }</SyncDelay>
   <EndTime>1759211487000</EndTime>
   <InstanceId>rm-bp1162kryivb8****</InstanceId>
   <StartTime>1759211487000</StartTime>
   <SyncStatus>{
            &quot;value&quot;: &quot;CheckInfo.IncreaseReplica&quot;,
            &quot;status&quot;: true
          }</SyncStatus>
    <Product>RDS</Product>
    <Step>1</Step>
    <FailoverType>
     <value>AUTOMATIC</value>
     <info>AutomaticFailover</info>
    </FailoverType>
    <Info>""</Info>
    <DestIdc>amtest22</DestIdc>
    <ActionStatus>INIT</ActionStatus>
    <Result>""</Result>
    <MasterLocation>cn-wulan-env10-amtest10000-a</MasterLocation>
    <ActionId>10</ActionId>
    <InstanceAlias>test</InstanceAlias>
    <TraceId>9A506E30-DA33-43D6-AACC-C3F85435D890</TraceId>
    <Id>1</Id>
    <SourceIdc>amtest21</SourceIdc>
    <ConsumeTime>120</ConsumeTime>
   </InstanceActions>
   <EndTime>1759211487000</EndTime>
   <ProcessStatus>FINISH</ProcessStatus>
   <StartTime>1759211487000</StartTime>
   <CurrentStep>1</CurrentStep>
   <ConsumeTime>120</ConsumeTime>
   <PrevActionStatus>[]</PrevActionStatus>
   <ActionStatus>INIT</ActionStatus>
  </Data>
  <ErrorCode>500</ErrorCode>
  <ErrorMessage>""</ErrorMessage>
  <Code>200</Code>
  <Cost>20</Cost>
  <Success>true</Success>
```

#### GetProcessEntry

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| PlanId | Integ er | Body | Yes | 10 | The ID of the drill plan. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. The operation was successful. Failure: No. |
| Code | String | 200 | The response code. |
| Message | String | success | The response message. |
| ErrorMessage | String | "" | The error message. |
| ErrorCode | String | 500 | The error code. |
| Path | String | /xxx/ | The URI of the request. |
| Cost | Long | 20 | The time it took to process the request. Unit: milliseconds (ms). |

Apsara Stack Resilience ASR for Zone-disaster Recovery This operation retrieves information about the steps in a drill process, including the instance status, action status, and process steps. API description

**Prerequisites**

Before you call this operation, call the ListDrillPlan operation to obtain the PlanId of the drill plan.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

**Request parameters**

**Response parameters**

| SR for Zone-disa Developer Guide·A | ster Recovery PI reference |  | Apsara Stack Resilienc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Struct | {} | The returned data. |
| - PrevActionStat us | String | [] | The status of the previous action. |
| - InstanceAction s | Array | [] | A list of instance information. |
| --Id | Integer | 1 | The ID of the instance status. |
| --ActionId | Integer | 10 | The action ID. |
| -- ProcessAction | String | SWITCH | The action of the process. |
| --SourceIdc | String | amtest21 | The source data center. |
| --DestIdc | String | amtest22 | The destination data center. |
| --Step | Integer | 2 | The ordinal number of the step. |
| --InstanceId | String | rm-2ze8g2am9762 | The instance ID. |
| --InstanceAlias | String | test | The alias of the instance. |
| --Product | String | RDS | The cloud product. |
| --StartTime | Long | 1759211487000 | The start time. |
| --EndTime | Long | 1759211487000 | The end time. |
| --ActionStatus | String | INIT | The action status. |
| --Result | String | "" | The returned result. |
| -- ConsumeTime | String | 120 | The time consumed. |
| --TraceId | String | 9A506E30-DA33- 43D6-AACC- C3F85435D890 | The ID of the request record. |

| psara Stack Resil | ience |  | ASR for Zone-disaster Recovery Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -- MasterLocatio n | String | cn-wulan-env10- amtest10000-a | The location of the primary node. |
| --SyncDelay | String | { "value": "0", "status": true } | The latency. |
| --SyncStatus | String | { "value": "CheckInfo.Increas eReplica", "status": true } | The latency status. |
| -ProcessId | String | 1 | The process ID. |
| -ProcessType | String | DRILL RECOVERY _ | The process type. |
| -ProcessAction | String | RECOVERY CHECK _ | The action of the process. |
| - ExecutionMod e | String | MANUAL | The execution mode. |
| -ActionStatus | String | NORMAL | The action status. |
| -ActionUser | String | 999999999 | The user who executes the action. |
| -StartTime | Long | 1759211487000 | The start time. |
| -EndTime | Long | 1759211487000 | The end time. |
| - SwitchDirectio n | String | amtest21- >amtest22 | The switchover direction. |
| -Zone | String | cn-wulan-env128- amtest217002-b | The zone for the drill. |
| -ConsumeTime | String | 120 | The execution time. |
| -ShowAction | String | RECOVERY CHECK _ | The process status displayed on the page. |
| -ProcessStatus | String | FINISH | The process status. |
| -CurrentStep | String | 1 | The current step. |

| SR for Zone-disa | ster Recovery |  | Apsara Stack Resilienc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| - ProtectionGrou pId | Integer | 16 | The protection group ID. |
| -PlanId | Integer | 10 | The ID of the drill plan. |

**Examples**

Sample request

```json
{ "PlanId":"10" }
```

Sample response `JSON` format Apsara Stack Resilience ASR for Zone-disaster Recovery

```json
{
 "Path":"/xxx/",
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "Data":{
  "ProcessAction":"RECOVERY_CHECK",
  "InstanceActions":[
   {
    "ProcessAction":"SWITCH",
    "SyncDelay":"{<br/>            \"value\": \"0\",<br/>            \"status\":
true<br/> }",
    "EndTime":1759211487000,
    "InstanceId":"rm-2ze8g2am9762",
    "StartTime":1759211487000,
    "SyncStatus":"{<br/>            \"value\": \"CheckInfo.IncreaseReplica\",<br/>
\"status\": true<br/> }",
    "Product":"RDS",
    "Step":2,
    "DestIdc":"amtest22",
    "ActionStatus":"INIT",
    "Result":"\"\"",
    "MasterLocation":"cn-wulan-env10-amtest10000-a",
    "ActionId":10,
    "InstanceAlias":"test",
    "TraceId":"9A506E30-DA33-43D6-AACC-C3F85435D890",
    "Id":1,
    "SourceIdc":"amtest21",
    "ConsumeTime":"120"
   }
```

`],`

```json
  "EndTime":1759211487000,
  "ProcessStatus":"FINISH",
  "Zone":"cn-wulan-env128-amtest217002-b",
  "PlanId":10,
  "StartTime":1759211487000,
  "ExecutionMode":"MANUAL",
  "ShowAction":"\t<br/>RECOVERY_CHECK",
  "PrevActionStatus":"[]",
  "ActionStatus":"NORMAL",
  "ProcessType":"DRILL_RECOVERY",
  "ActionUser":"999999999",
  "ProtectionGroupId":16,
  "SwitchDirection":"amtest21->amtest22",
  "CurrentStep":"1",
  "ProcessId":"1",
  "ConsumeTime":"120"
 },
 "ErrorCode":"500",
 "ErrorMessage":"\"\"",
 "Code":"200",
 "Cost":20,
 "Success":true
}<br/><br/><br/><br/><br/><br/><br/>
```

ASR for Zone-disaster Recovery Apsara Stack Resilience `XML` format

```xml
<Path>/xxx/</Path> <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data>
 <ProcessAction>RECOVERY_CHECK</ProcessAction>
 <InstanceActions>
  <ProcessAction>SWITCH</ProcessAction>
  <SyncDelay>{
            &quot;value&quot;: &quot;0&quot;,
            &quot;status&quot;: true
          }</SyncDelay>
   <EndTime>1759211487000</EndTime>
   <InstanceId>rm-2ze8g2am9762</InstanceId>
   <StartTime>1759211487000</StartTime>
   <SyncStatus>{
            &quot;value&quot;: &quot;CheckInfo.IncreaseReplica&quot;,
            &quot;status&quot;: true
          }</SyncStatus>
    <Product>RDS</Product>
    <Step>2</Step>
    <DestIdc>amtest22</DestIdc>
    <ActionStatus>INIT</ActionStatus>
    <Result>""</Result>
    <MasterLocation>cn-wulan-env10-amtest10000-a</MasterLocation>
    <ActionId>10</ActionId>
    <InstanceAlias>test</InstanceAlias>
    <TraceId>9A506E30-DA33-43D6-AACC-C3F85435D890</TraceId>
    <Id>1</Id>
    <SourceIdc>amtest21</SourceIdc>
    <ConsumeTime>120</ConsumeTime>
   </InstanceActions>
   <EndTime>1759211487000</EndTime>
   <ProcessStatus>FINISH</ProcessStatus>
   <Zone>cn-wulan-env128-amtest217002-b</Zone>
   <PlanId>10</PlanId>
   <StartTime>1759211487000</StartTime>
   <ExecutionMode>MANUAL</ExecutionMode>
   <ShowAction>
RECOVERY_CHECK</ShowAction>
    <PrevActionStatus>[]</PrevActionStatus>
    <ActionStatus>NORMAL</ActionStatus>
    <ProcessType>DRILL_RECOVERY</ProcessType>
    <ActionUser>999999999</ActionUser>
    <SwitchDirection>amtest21-&gt;amtest22</SwitchDirection>
    <CurrentStep>1</CurrentStep>
    <ProcessId>1</ProcessId>
    <ConsumeTime>120</ConsumeTime>
   </Data>
   <ErrorCode>500</ErrorCode>
   <ErrorMessage>&quot;&quot;</ErrorMessage>
   <Code>200</Code>
```

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| PlanId | Integ er | Body | Yes | 10 | The ID of the plan. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | String | 200 | The status code. A value of 200 indicates that the call was successful. |
| Message | String | success | The returned message. |
| ErrorMessage | String | "" | The error message. |

Apsara Stack Resilience ASR for Zone-disaster Recovery

```xml
   <Cost>20</Cost>
   <Success>true</Success>
```

#### CreateDisasterRecoveryProcess

Creates a fault recovery flow. After you create a protection group, you can call this operation to start the protection group flow for a fault scenario. Description Creates a fault recovery flow. After you create a protection group, you can call this operation to start the protection group flow for a fault scenario.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see the documentation about common request parameters.

**Request syntax**

```
POST /api/pop/v1/createDisasterRecoveryProcess HTTP/1.1
```

**Request parameters**

**Response parameters**

| SR for Zone-disa | ster Recovery |  |  |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | 500 | The error code. |
| Path | String | /xxx/ | The URI of the request. |
| Cost | Long | 20 | The time it took to complete the request. Unit: milliseconds (ms). |
| Data | Struct | {} | The returned data. |
| -ProcessId | String | 16 | The flow ID. |
| -ProcessAction | String | SWITCH | The flow action. |
| -PlanId | Integer | 18 | The ID of the fault recovery plan. |
| -ProcessType | String | DRILL RECOVER _ | The flow type. |

**Examples**

Sample request

```json
POST /api/pop/v1/createDisasterRecoveryProcess HTTP/1.1 { "PlanId":"10" }
```

Sample successful response `JSON` format Apsara Stack Resilience ASR for Zone-disaster Recovery

```json
{
 "Path":"/xxx/",
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "Data":{
  "ProcessAction":"SWITCH",
  "ProcessType":"DRILL_RECOVER",
  "PlanId":18,
  "ProcessId":"16"
 },
 "ErrorCode":"500",
 "ErrorMessage":"\"\"",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` format

```xml
<Path>/xxx/</Path> <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data>
 <ProcessAction>SWITCH</ProcessAction>
 <ProcessType>DRILL_RECOVER</ProcessType>
 <PlanId>18</PlanId>
 <ProcessId>16</ProcessId>
</Data> <ErrorCode>500</ErrorCode> <ErrorMessage>&quot;&quot;</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### CreateHdrReverse

Switches an HDR protection group. Description This operation switches an HDR protection group. Before you switch the group, obtain information about its recovery drill flow.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ProcessId | Integ er | Body | Yes | 10 | The process ID. |
| Product | Strin g | Body | Yes | HDR | The product name. |
| InstanceId | Strin g | Body | Yes | "xxxx" | The instance name. |
| RecoverOr iginal | Boole an | Body | Yes | true | Specifies whether to recover to the original host. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the request. true: The request was successful. Failed: false |
| Code | String | 200 | The status code. A value of 200 indicates that the call was successful. |
| Message | String | success | The returned message. |
| ErrorMessage | String | "" | The error message. |
| ErrorCode | String | 500 | The error code. |
| Path | String | /xxx/xxx | The URI of the request. |
| Cost | Long | 20 | The time consumed by the API call, in milliseconds (ms). |

ASR for Zone-disaster Recovery Apsara Stack Resilience

**Request parameters**

**Response data**

**Examples**

Sample request Apsara Stack Resilience ASR for Zone-disaster Recovery

```json
{ "ProcessId":"10", "Product":"HDR", "InstanceId":"xxxx", "RecoverOriginal":"true" }
```

Sample response `JSON` format

```json
{
 "Path":"/xxx/xxx",
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "ErrorCode":"500",
 "ErrorMessage":"\"\"",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` format

```xml
<Path>/xxx/xxx</Path> <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <ErrorCode>500</ErrorCode> <ErrorMessage>&quot;&quot;</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### GetDrillPlan

Call this operation to retrieve the details of a drill plan. The details include the products, instances, and zones that are included in the plan. Description This operation requires the PlanId parameter. Before you call this operation, call the ListDrillPlan operation to obtain a list of drill plans. From the list, obtain the PlanId of the drill plan for which you want to retrieve details.

**Request headers**

This operation uses common request headers and does not have any special request headers. For more information, see the Common request parameters document.

**Request syntax**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PlanId | Integ er | Body | Yes | 10 | The ID of the plan. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| Success | Boolean | true | The status of the response. true: The request was successful. Failed: false. |
| Code | String | 200 | The status code. A value of 200 indicates that the call was successful. |
| Message | String | success | The returned message. |
| ErrorMessage | String | "" | The error message. |
| ErrorCode | String | 500 | The error code. |
| Path | String | /xxx/xxx | The URI of the request. |
| Cost | Long | 20 | The time consumed by the API call. Unit: milliseconds (ms). |
| Data | Struct | {} | The returned data. |
| -PlanItems | Array | [] | The recovery steps. |
| --InstanceId | String | rm- bp1162kryivb8**** | The instance ID. |
| --InstanceAlias | String | test | The alias of the instance. |
| --Step | Integer | 1 | The step number. |

ASR for Zone-disaster Recovery Apsara Stack Resilience

**Request parameters**

**Response parameters**

| psara Stack Resil | ience |  | ASR for Zone-disaster Recovery |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| --Product | String | RDS | The cloud product. |
| --Info | String | {} | The message. |
| --Impacts | String | "product.drill.effect .RDS" | The impact of the switchover. |
| --FailoverType | Struct | {} | The switchover type. |
| ---value | String | "NONEED" | The content. |
| ---info | String | "InstancePrimaryZ oneMissMatch" | The message. |
| -Id | Integer | 10 | The ID of the plan. |
| -PlanName | String | name | The name of the drill plan. |
| - ProtectionGrou pId | Integer | 10 | The ID of the protection group. |
| - ProtectionGrou pName | String | test | The name of the protection group. |
| -Description | String | testDescription | The description. |
| - ExecutionMod e | String | MANUAL | The execution mode. |
| -Zone | String | cn-wulan-env10- amtest10000-a | The zone. |
| -GmtCreate | Long | 1756110161000 | The time when the plan was created. |
| -GmtModified | Long | 1756110161000 | The time when the plan was last modified. |
| -LastTime | Long | 1756110161000 | The time of the last operation. |
| - InPlanInstance Count | Integer | 10 | The number of instances included in the plan. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| - NotInPlanInsta nceCount | Integer | 10 | The number of instances not included in the plan. |
| -ExecuteCount | Integer | 10 | The number of executions. |
| - RunningProces sId | Integer | 10 | The ID of the process that is being executed. |

Apsara Stack Resilience

**Examples**

Request example

```json
{ "PlanId":"10" }
```

Response example `JSON` format Apsara Stack Resilience ASR for Zone-disaster Recovery

```json
{
 "Path":"/xxx/xxx",
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "Data":{
  "Description":"testDescription",
  "Zone":"cn-wulan-env10-amtest10000-a",
  "GmtModified":1756110161000,
  "ExecutionMode":"MANUAL",
  "PlanName":"name",
  "GmtCreate":1756110161000,
  "RunningProcessId":10,
  "InPlanInstanceCount":10,
  "ProtectionGroupId":10,
  "ProtectionGroupName":"test",
  "ExecuteCount":10,
  "Id":10,
  "NotInPlanInstanceCount":10,
  "PlanItems":[
   {
    "Impacts":"\"product.drill.effect.RDS\"",
    "InstanceId":"rm-bp1162kryivb8****",
    "InstanceAlias":"test",
    "Product":"RDS",
    "Step":1,
    "FailoverType":[
     {
      "value":"\"NONEED\"",
      "info":"\"InstancePrimaryZoneMissMatch\""
     }
```

`],`

```json
    "Info":"{}"
   }
```

`],`

```json
  "LastTime":1756110161000
 },
 "ErrorCode":"500",
 "ErrorMessage":"\"\"",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` format ASR for Zone-disaster Recovery Apsara Stack Resilience

```xml
<Path>/xxx/xxx</Path> <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data>
 <Description>testDescription</Description>
 <Zone>cn-wulan-env10-amtest10000-a</Zone>
 <GmtModified>1756110161000</GmtModified>
 <ExecutionMode>MANUAL</ExecutionMode>
 <PlanName>name</PlanName>
 <GmtCreate>1756110161000</GmtCreate>
 <RunningProcessId>10</RunningProcessId>
 <InPlanInstanceCount>10</InPlanInstanceCount>
 <ProtectionGroupName>test</ProtectionGroupName>
 <ExecuteCount>10</ExecuteCount>
 <Id>10</Id>
 <NotInPlanInstanceCount>10</NotInPlanInstanceCount>
 <PlanItems>
  <Impacts>&quot;product.drill.effect.RDS&quot;</Impacts>
  <InstanceId>rm-bp1162kryivb8****</InstanceId>
  <InstanceAlias>test</InstanceAlias>
  <Product>RDS</Product>
  <Step>1</Step>
  <FailoverType>
   <value>&quot;NONEED&quot;</value>
   <info>&quot;InstancePrimaryZoneMissMatch&quot;</info>
  </FailoverType>
  <Info>{}</Info>
 </PlanItems>
 <LastTime>1756110161000</LastTime>
</Data> <ErrorCode>500</ErrorCode> <ErrorMessage>&quot;&quot;</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### ListDrillPlan

This operation lists drill plans. You can query for a plan by its name. The response includes details about each plan, such as its execution mode and the zone where the drill is performed. Description

**Prerequisites**

<Prerequisites for calling this operation>

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PlanId | Integ er | Body | No | 1 | The ID of the drill plan. |
| PlanName | Strin g | Body | No | test | The name of the drill plan. |
| Execution Mode | Strin g | Body | No | MANUAL | The execution mode. |
| PageNum ber | Integ er | Body | No | 1 | The page number for the paged query. |
| PageSize | Integ er | Body | No | 100 | The number of entries per page for the paged query. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array | [] | The returned data. |
| -PlanId | Integer | 1 | The ID of the plan. |
| -PlanName | String | test | The name of the plan. |
| - ProtectionGrou pId | Integer | 2 | The ID of the protection group. |
| - ProtectionGrou pName | String | test | The name of the protection group. |
| -Description | String | test dr | The description. |
| - ExecutionMod e | String | MANUAL | The execution mode. |
| -Zone | String | cn-wulan-env10- amtest10000-a | The zone. |

Apsara Stack Resilience ASR for Zone-disaster Recovery

**Request parameters**

**Response parameters**

| A | SR for Zone-disa Developer Guide·A | ster Recovery PI reference |  | Apsara Stack Resilienc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -GmtCreate | Long | 1759211487000 | The time when the plan was created. |
| -GmtModified | Long | 1759211487000 | The time when the plan was last modified. |
| - RunningProces sId | Integer | 16 | The ID of the running process. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. true: The request was successful. Failed: false. |
| Code | String | 200 | The HTTP status code. A value of 200 indicates that the call was successful. |
| Message | String | success | The returned message. |
| ErrorMessage | String | "" | The error message. |
| ErrorCode | String | 500 | The error code. |
| Path | String | /xxx/xxx | The URI of the request. |
| Cost | Long | 20 | The time it took to process the request. Unit: ms. |
| TotalCount | Integer | 100 | The total number of records. |
| PageNumber | Integer | 1 | The current page number. |
| PageSize | Integer | 10 | The number of entries per page. |

**Examples**

Sample request Apsara Stack Resilience ASR for Zone-disaster Recovery

```
{ }
```

Sample response `JSON` format ASR for Zone-disaster Recovery Apsara Stack Resilience

```json
{
  "Code": "200",
  "Data": {
    "Item": [
      {
        "ExecutionMode": "MANUAL",
        "GmtCreate": 1759992973000,
        "GmtModified": 1759992973000,
        "PlanId": 6,
        "PlanName": "test",
        "ProtectionGroupId": 4,
        "ProtectionGroupName": "123123",
        "RunningProcessId": 6,
        "Zone": "cn-wulan-env128-amtest217002-b"
      },
      {
        "ExecutionMode": "AUTOMATIC",
        "GmtCreate": 1759211078000,
        "GmtModified": 1759211078000,
        "PlanId": 4,
        "PlanName": "bcmctest",
        "ProtectionGroupId": 3,
        "ProtectionGroupName": "bcmctest",
        "Zone": "cn-wulan-env128-amtest128001-a"
      },
      {
        "ExecutionMode": "MANUAL",
        "GmtCreate": 1757578962000,
        "GmtModified": 1757578962000,
        "PlanId": 3,
        "PlanName": "es",
        "ProtectionGroupId": 2,
        "ProtectionGroupName": "es-ab",
        "RunningProcessId": 3,
        "Zone": "cn-wulan-env128-amtest128001-a"
      }
```

]

```json
  },
  "Message": "success",
  "PageNumber": 1,
  "PageSize": 10,
  "RequestId": "AB3E6FFC-6467-4804-832C-E05E7C14D7A8",
  "Success": true,
  "TotalCount": 3
}
```

`XML` format Apsara Stack Resilience ASR for Zone-disaster Recovery

```xml
<Code>200</Code> <Data>
 <Item>
  <ExecutionMode>MANUAL</ExecutionMode>
  <GmtCreate>1759992973000</GmtCreate>
  <GmtModified>1759992973000</GmtModified>
  <PlanId>6</PlanId>
  <PlanName>test</PlanName>
  <ProtectionGroupName>123123</ProtectionGroupName>
  <RunningProcessId>6</RunningProcessId>
  <Zone>cn-wulan-env128-amtest217002-b</Zone>
 </Item>
 <Item>
  <ExecutionMode>AUTOMATIC</ExecutionMode>
  <GmtCreate>1759211078000</GmtCreate>
  <GmtModified>1759211078000</GmtModified>
  <PlanId>4</PlanId>
  <PlanName>bcmctest</PlanName>
  <ProtectionGroupName>bcmctest</ProtectionGroupName>
  <Zone>cn-wulan-env128-amtest128001-a</Zone>
 </Item>
 <Item>
  <ExecutionMode>MANUAL</ExecutionMode>
  <GmtCreate>1757578962000</GmtCreate>
  <GmtModified>1757578962000</GmtModified>
  <PlanId>3</PlanId>
  <PlanName>es</PlanName>
  <ProtectionGroupName>es-ab</ProtectionGroupName>
  <RunningProcessId>3</RunningProcessId>
  <Zone>cn-wulan-env128-amtest128001-a</Zone>
 </Item>
</Data> <Message>success</Message> <PageNumber>1</PageNumber> <PageSize>10</PageSize> <RequestId>AB3E6FFC-6467-4804-832C-E05E7C14D7A8</RequestId> <Success>true</Success> <TotalCount>3</TotalCount>
```

#### GetProcessCheck

You can call this operation to retrieve the check result of a flow execution. This check verifies the instance status before a switch. The result includes information such as synchronization latency, primary node location, and whether a drill action is involved. Description

**Prerequisites**

Before calling this operation, make sure that the drill plan flow exists. You can call the ListProcesses operation to obtain the ProcessId from the list of flows.

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ProcessId | Integ er | Body | Yes | 10 | The ID of the drill flow. |
| ProcessAc tion | Strin g | Body | Yes | SWITCH | The type of the flow action. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The returned status. true: The request was successful. The failed status is false. |
| Code | String | 200 | The status code. A value of 200 indicates that the call was successful. |
| Message | String | success | The returned message. |
| ErrorMessage | String | "" | The error message. |
| ErrorCode | String | 500 | The error code. |
| Path | String | /xxx/ | The URI of the request. |
| Cost | Long | 20 | The time it took to process the request, in milliseconds (ms). |
| Data | Struct | {} | The returned data. |

ASR for Zone-disaster Recovery Apsara Stack Resilience

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see the documentation for common request parameters.

**Request syntax**

**Request parameters**

**Response parameters**

| A | psara Stack Resil | ience |  | ASR for Zone-disaster Recovery Developer Guide·API referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| - PrevActionStat us | String | [] | The status of the preceding action. |
| - InstanceAction s | Array | [] | A list of instance information. |
| --ZoneInfo | String | cn-wulan-env10- amtest10000-a | The zone information. |
| --Id | Integer | 18 | The ID of the instance status. |
| --ActionId | Integer | 16 | The action ID. |
| -- ProcessAction | String | SWITCH CHECK _ | The flow action. |
| --SourceIdc | String | amtest21 | The source data center. |
| --DestIdc | String | amtest22 | The destination data center. |
| --Step | Integer | 1 | The step number. |
| --InstanceId | String | rm- 2ze8g2am97624** ** | The instance ID. |
| --InstanceAlias | String | test | The instance alias. |
| --Info | String | "" | The information message. |
| --Product | String | RDS | The cloud product. |
| --StartTime | Long | 1628265600000 | The start time. |
| --EndTime | Long | 1628265600000 | The end time. |
| --ActionStatus | String | INIT | The action status. |
| --Result | String | “” | The returned result. |
| -- ConsumeTime | String | 120 | The time consumed. |

| SR for Zone-disa Developer Guide·A | ster Recovery PI reference |  | Apsara Stack Resilienc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| --TraceId | String | 9A506E30-DA33- 43D6-AACC- C3F85435D890 | The request record ID. |
| -- MasterLocatio n | String | cn-wulan-env10- amtest10000-a | The location of the primary node. |
| --SyncDelay | String | { "value": "0", "status": true } | The latency. |
| --SyncStatus | String | { "value": "CheckInfo.Increas eReplica", "status": true } | The latency status. |
| --FailoverType | Struct | {} | The switch type. |
| ---value | String | AUTOMATIC | Content. |
| ---info | String | AutomaticFailover | The information message. |
| -ProcessStatus | String | FINISH | The flow status. |
| -ActionStatus | String | NORMAL | The action status. |
| -StartTime | Long | 1759211487000 | The start time. |
| -EndTime | Long | 1759211487000 | The end time. |
| -ConsumeTime | String | 120 | The execution time. |
| -CurrentStep | Integer | 1 | The current step. |

**Examples**

Request example

```json
{ "ProcessId":"10", "ProcessAction":"SWITCH" }
```

Successful response example `JSON` format Apsara Stack Resilience ASR for Zone-disaster Recovery

```json
{
  "Code": "200",
  "Data": {
    "ActionStatus": "SUCCESS",
    "ConsumeTime": "0",
    "CurrentStep": 1,
    "EndTime": 1760323989000,
    "InstanceActions": {
      "InstanceAction": [
        {
          "ActionId": 12,
          "ActionStatus": "NORMAL",
          "ConsumeTime": "0",
          "DestIdc": "amtest217",
          "EndTime": 1760323989000,
          "FailoverType": {
            "info": "InstancePrimaryZoneMissMatch",
            "value": "NONEED"
          },
          "Id": 12,
          "Info": {},
          "InstanceAlias": "rds-mysql80-classic",
          "InstanceId": "rm-jp7r3459uq299j520",
          "MasterLocation": {
            "value": "cn-wulan-env128-amtest128001-a",
            "status": true
          },
          "ProcessAction": "SWITCH_CHECK",
          "Product": "RDS",
          "Result": "",
          "SourceIdc": "amtest128",
          "StartTime": 1760323989000,
          "Step": 1,
          "SyncDelay": {
            "value": "0",
            "status": true
          },
          "SyncStatus": {
            "value": "CheckInfo.IncreaseReplica",
            "status": true
          },
          "TraceId": "1760323988819#rm-jp7r3459uq299j520#1#4F19DE7F-67E5-4F6C-AA06-
75CBB5DC7C65",
          "ZoneInfo": {
            "Item": [
              "cn-wulan-env128-amtest128001-a",
              "cn-wulan-env128-amtest217002-b"
```

]

```json
          }
        },
        {
          "ActionId": 12,
          "ActionStatus": "NORMAL",
          "ConsumeTime": "0",
```

ASR for Zone-disaster Recovery Apsara Stack Resilience

```json
          "DestIdc": "amtest217",
          "EndTime": 1760323989000,
          "FailoverType": {
            "info": "InstancePrimaryZoneMissMatch",
            "value": "NONEED"
          },
          "Id": 13,
          "Info": {},
          "InstanceAlias": "mysql-80-vpc",
          "InstanceId": "rm-jp72fab594a0x427u",
          "MasterLocation": {
            "value": "cn-wulan-env128-amtest128001-a",
            "status": true
          },
          "ProcessAction": "SWITCH_CHECK",
          "Product": "RDS",
          "Result": "",
          "SourceIdc": "amtest128",
          "StartTime": 1760323989000,
          "Step": 2,
          "SyncDelay": {
            "value": "0",
            "status": true
          },
          "SyncStatus": {
            "value": "CheckInfo.IncreaseReplica",
            "status": true
          },
          "TraceId": "1760323988819#rm-jp72fab594a0x427u#1#4F19DE7F-67E5-4F6C-AA06-
75CBB5DC7C65",
          "ZoneInfo": {
            "Item": [
              "cn-wulan-env128-amtest128001-a",
              "cn-wulan-env128-amtest217002-b"
```

]

```
          }
        }
```

]

```json
    },
    "PrevActionStatus": {
      "Item": [
        "{\"actionStatus\":\"finish\",\"actionType\":\"SWITCH_BACK_CHECK\"}",
        "{\"actionStatus\":\"finish\",\"actionType\":\"SWITCH_CHECK\"}",
        "{\"actionStatus\":\"finish\",\"actionType\":\"SWITCH\"}",
        "{\"actionStatus\":\"finish\",\"actionType\":\"SWITCH_BACK\"}",
        "{\"actionStatus\":\"finish\",\"actionType\":\"RECOVERY_CHECK\"}"
```

]

```json
    },
    "ProcessStatus": "FINISH",
    "StartTime": 1760323989000
  },
  "Message": "success",
  "RequestId": "4F19DE7F-67E5-4F6C-AA06-75CBB5DC7C65",
  "Success": true
```

Apsara Stack Resilience ASR for Zone-disaster Recovery

```
}
```

`XML` format

```xml
<Code>200</Code> <Data>
 <ActionStatus>SUCCESS</ActionStatus>
 <ConsumeTime>0</ConsumeTime>
 <CurrentStep>1</CurrentStep>
 <EndTime>1760323989000</EndTime>
 <InstanceActions>
  <InstanceAction>
   <ActionId>12</ActionId>
   <ActionStatus>NORMAL</ActionStatus>
   <ConsumeTime>0</ConsumeTime>
   <DestIdc>amtest217</DestIdc>
   <EndTime>1760323989000</EndTime>
   <FailoverType>
    <info>InstancePrimaryZoneMissMatch</info>
    <value>NONEED</value>
   </FailoverType>
   <Id>12</Id>
   <Info  />
   <InstanceAlias>rds-mysql80-classic</InstanceAlias>
   <InstanceId>rm-jp7r3459uq299j520</InstanceId>
   <MasterLocation>
    <value>cn-wulan-env128-amtest128001-a</value>
    <status>true</status>
   </MasterLocation>
   <ProcessAction>SWITCH_CHECK</ProcessAction>
   <Product>RDS</Product>
   <Result  />
   <SourceIdc>amtest128</SourceIdc>
   <StartTime>1760323989000</StartTime>
   <Step>1</Step>
   <SyncDelay>
    <value>0</value>
    <status>true</status>
   </SyncDelay>
   <SyncStatus>
    <value>CheckInfo.IncreaseReplica</value>
    <status>true</status>
   </SyncStatus>
   <TraceId>1760323988819#rm-jp7r3459uq299j520#1#4F19DE7F-67E5-4F6C-AA06-
75CBB5DC7C65</TraceId>
   <ZoneInfo>
    <Item>cn-wulan-env128-amtest128001-a</Item>
    <Item>cn-wulan-env128-amtest217002-b</Item>
   </ZoneInfo>
  </InstanceAction>
  <InstanceAction>
   <ActionId>12</ActionId>
   <ActionStatus>NORMAL</ActionStatus>
   <ConsumeTime>0</ConsumeTime>
```

ASR for Zone-disaster Recovery Apsara Stack Resilience /

```xml
   <DestIdc>amtest217</DestIdc>
   <EndTime>1760323989000</EndTime>
   <FailoverType>
    <info>InstancePrimaryZoneMissMatch</info>
    <value>NONEED</value>
   </FailoverType>
   <Id>13</Id>
   <Info  />
   <InstanceAlias>mysql-80-vpc</InstanceAlias>
   <InstanceId>rm-jp72fab594a0x427u</InstanceId>
   <MasterLocation>
    <value>cn-wulan-env128-amtest128001-a</value>
    <status>true</status>
   </MasterLocation>
   <ProcessAction>SWITCH_CHECK</ProcessAction>
   <Product>RDS</Product>
   <Result  />
   <SourceIdc>amtest128</SourceIdc>
   <StartTime>1760323989000</StartTime>
   <Step>2</Step>
   <SyncDelay>
    <value>0</value>
    <status>true</status>
   </SyncDelay>
   <SyncStatus>
    <value>CheckInfo.IncreaseReplica</value>
    <status>true</status>
   </SyncStatus>
   <TraceId>1760323988819#rm-jp72fab594a0x427u#1#4F19DE7F-67E5-4F6C-AA06-
75CBB5DC7C65</TraceId>
   <ZoneInfo>
    <Item>cn-wulan-env128-amtest128001-a</Item>
    <Item>cn-wulan-env128-amtest217002-b</Item>
   </ZoneInfo>
  </InstanceAction>
 </InstanceActions>
 <PrevActionStatus>
  <Item>
{&quot;actionStatus&quot;:&quot;finish&quot;,&quot;actionType&quot;:&quot;SWITCH_BACK_CHE &quot;}</Item>
  <Item>
{&quot;actionStatus&quot;:&quot;finish&quot;,&quot;actionType&quot;:&quot;SWITCH_CHECK&qu ;}</Item>
  <Item>
{&quot;actionStatus&quot;:&quot;finish&quot;,&quot;actionType&quot;:&quot;SWITCH&quot;} </Item>
  <Item>
{&quot;actionStatus&quot;:&quot;finish&quot;,&quot;actionType&quot;:&quot;SWITCH_BACK&quo }</Item>
  <Item>
{&quot;actionStatus&quot;:&quot;finish&quot;,&quot;actionType&quot;:&quot;RECOVERY_CHECK& ot;}</Item>
 </PrevActionStatus>
 <ProcessStatus>FINISH</ProcessStatus>
```

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ProcessId | Integ er | Body | Yes | 10 | The ID of the recovery drill process. |
| ProcessAc tion | Strin g | Body | Yes | SWITCH | The type of the process action. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | String | 200 | The status code. A value of 200 indicates that the call was successful. |

Apsara Stack Resilience ASR for Zone-disaster Recovery

```xml
 <StartTime>1760323989000</StartTime>
</Data> <Message>success</Message> <RequestId>4F19DE7F-67E5-4F6C-AA06-75CBB5DC7C65</RequestId> <Success>true</Success>
```

#### GetPrevProcess

This operation retrieves the status of the previous process in a recovery drill plan. It obtains information about the previous step but does not change the status of the process. Description Before calling this operation, confirm that the recovery drill plan process exists. Call the ListProcesses operation to obtain the ProcessId from the list of processes.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see the common request parameters document.

**Request syntax**

**Request parameters**

**Response parameters**

| SR for Zone-disa Developer Guide·A | ster Recovery PI reference |  | Apsara Stack Resilienc |
|---|---|---|---|
| Parameter | Type | Example | Description |
| Message | String | success | The returned message. |
| ErrorMessage | String | "" | The error message. |
| ErrorCode | String | 500 | The error code. |
| Path | String | /xxx/xxx | The URI of the request. |
| Cost | Long | 20 | The time consumed by the API call. Unit: milliseconds (ms). |
| Data | Struct | {} | The returned data. |
| - PrevActionStat us | String | [] | The status of the previous action. |
| - InstanceAction s | Array | [] | The list of instance information. |
| --ZoneInfo | String | cn-wulan-env10- amtest10000-a | The zone information. |
| --Id | Integer | 18 | The ID of the instance status. |
| --ActionId | Integer | 16 | The action ID. |
| -- ProcessAction | String | Process action | The process action. |
| --SourceIdc | String | amtest21 | The source data center. |
| --DestIdc | String | amtest22 | The destination data center. |
| --Step | Integer | 1 | The ordinal number of the step. |
| --InstanceId | String | rm- 2ze8g2am97624** ** | The instance ID. |
| --InstanceAlias | String | test | The instance alias. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| --Product | String | RDS | The cloud product. |
| --StartTime | Long | 1628265600000 | The start time. |
| --EndTime | Long | 1628265600000 | The end time. |
| --ActionStatus | String | INIT | The action status. |
| --Result | String | "" | The returned result. |
| -- ConsumeTime | String | 120 | The time consumed. |
| --TraceId | String | 9A506E30-DA33- 43D6-AACC- C3F85435D890 | The ID of the request record. |
| -- MasterLocatio n | String | cn-wulan-env10- amtest10000-a | The location of the primary node. |
| --SyncDelay | String | { "value": "0", "status": true } | The latency time. |
| --SyncStatus | String | { "value": "CheckInfo.Increas eReplica", "status": true } | The latency status. |
| --FailoverType | Struct | {} | The switchover type. |
| ---value | String | AUTOMATIC | The content. |
| ---info | String | AutomaticFailover | The prompt message. |
| -ProcessId | String | 4 | The process ID. |
| -ProcessType | String | DRILL RECOVERY _ | The process type. |
| -ProcessAction | String | RECOVERY CHECK _ | The process action. |
| - ExecutionMod e | String | MANUAL | The execution pattern. |

Apsara Stack Resilience

| SR for Zone-disa Developer Guide·A | ster Recovery PI reference |  | Apsara Stack Resilienc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -ActionStatus | String | NORMAL | The action status. |
| -ActionUser | String | 999999999 | The user who executed the action. |
| -StartTime | Long | 1759211487000 | The start time. |
| -EndTime | Long | 1759211487000 | The end time. |
| - SwitchDirectio n | String | amtest21- >amtest22 | The switchover direction. |
| -ConsumeTime | String | 120 | The execution time. |
| -ShowAction | String | RECOVERY CHECK _ | The process status displayed on the page. |
| -ProcessStatus | String | FINISH | The process status. |
| -CurrentStep | String | 1 | The current step. |
| - ProtectionGrou pId | Integer | 20 | The protection group ID. |
| -PlanId | Integer | 16 | The ID of the recovery drill plan. |
| -Zone | String | cn-wulan-env128- amtest217002-b | The zone for the recovery drill. |

**Examples**

Request example

```json
{ "ProcessId":"10", "ProcessAction":"SWITCH" }
```

Successful response example `JSON` format

```json
{
  "Code": "200",
  "Data": {
"ActionStatus":"SUCCESS",
```

Apsara Stack Resilience ASR for Zone-disaster Recovery

```json
    ActionStatus: SUCCESS,
    "ActionUser": "1933655883841513",
    "ConsumeTime": "0",
    "CurrentStep": 1,
    "EndTime": 1760324734000,
    "ExecutionMode": "MANUAL",
    "InstanceActions": {
      "InstanceAction": [
        {
          "ActionId": 19,
          "ActionStatus": "NORMAL",
          "ConsumeTime": "0",
          "DestIdc": "amtest217",
          "EndTime": 1760324734000,
          "FailoverType": {
            "info": "InstancePrimaryZoneMissMatch",
            "value": "NONEED"
          },
          "Id": 26,
          "InstanceAlias": "rds-mysql57-classic",
          "InstanceId": "rm-jp7lct7rd5l61b7t0",
          "MasterLocation": {
            "value": "cn-wulan-env128-amtest128001-a",
            "status": true
          },
          "ProcessAction": "SWITCH_CHECK",
          "Product": "RDS",
          "Result": "",
          "SourceIdc": "amtest128",
          "StartTime": 1760324734000,
          "Step": 1,
          "SyncDelay": {
            "value": "0",
            "status": true
          },
          "SyncStatus": {
            "value": "CheckInfo.IncreaseReplica",
            "status": true
          },
          "TraceId": "1760324733966#rm-jp7lct7rd5l61b7t0#1#AD59B157-3B17-4C4B-A0BE-
2A7772BABAD7",
          "ZoneInfo": {
            "Item": [
              "cn-wulan-env128-amtest128001-a",
              "cn-wulan-env128-amtest217002-b"
```

]

```
          }
        }
```

]

```json
    },
    "PlanId": 6,
    "PrevActionStatus": {
      "Item": [
        "{\"actionStatus\":\"finish\",\"actionType\":\"SWITCH_CHECK\"}",
        "{\"actionStatus\":\"process\",\"actionType\":\"SWITCH\"}"
```

ASR for Zone-disaster Recovery Apsara Stack Resilience ]

```json
    },
    "ProcessAction": "SWITCH",
    "ProcessId": 6,
    "ProcessStatus": "EXECUTING",
    "ProcessType": "DRILL_RECOVERY",
    "ProtectionGroupId": 4,
    "ShowAction": "SWITCH_CHECK",
    "StartTime": 1760324734000,
    "SwitchDirection": "amtest128->amtest217",
    "Zone": "cn-wulan-env128-amtest217002-b"
  },
  "Message": "success",
  "RequestId": "DC9C8651-9890-423E-8056-8E81F0B95FEE",
  "Success": true
}
```

`XML` format

```xml
<Code>200</Code> <Data>
 <ActionStatus>SUCCESS</ActionStatus>
 <ActionUser>1933655883841513</ActionUser>
 <ConsumeTime>0</ConsumeTime>
 <CurrentStep>1</CurrentStep>
 <EndTime>1760324734000</EndTime>
 <ExecutionMode>MANUAL</ExecutionMode>
 <InstanceActions>
  <InstanceAction>
   <ActionId>19</ActionId>
   <ActionStatus>NORMAL</ActionStatus>
   <ConsumeTime>0</ConsumeTime>
   <DestIdc>amtest217</DestIdc>
   <EndTime>1760324734000</EndTime>
   <FailoverType>
    <info>InstancePrimaryZoneMissMatch</info>
    <value>NONEED</value>
   </FailoverType>
   <Id>26</Id>
   <InstanceAlias>rds-mysql57-classic</InstanceAlias>
   <InstanceId>rm-jp7lct7rd5l61b7t0</InstanceId>
   <MasterLocation>
    <value>cn-wulan-env128-amtest128001-a</value>
    <status>true</status>
   </MasterLocation>
   <ProcessAction>SWITCH_CHECK</ProcessAction>
   <Product>RDS</Product>
   <Result  />
   <SourceIdc>amtest128</SourceIdc>
   <StartTime>1760324734000</StartTime>
   <Step>1</Step>
   <SyncDelay>
    <value>0</value>
<status>true</status>
```

Apsara Stack Resilience ASR for Zone-disaster Recovery

```xml
    <status>true</status>
   </SyncDelay>
   <SyncStatus>
    <value>CheckInfo.IncreaseReplica</value>
    <status>true</status>
   </SyncStatus>
   <TraceId>1760324733966#rm-jp7lct7rd5l61b7t0#1#AD59B157-3B17-4C4B-A0BE-
2A7772BABAD7</TraceId>
   <ZoneInfo>
    <Item>cn-wulan-env128-amtest128001-a</Item>
    <Item>cn-wulan-env128-amtest217002-b</Item>
   </ZoneInfo>
  </InstanceAction>
 </InstanceActions>
 <PlanId>6</PlanId>
 <PrevActionStatus>
  <Item>
{&quot;actionStatus&quot;:&quot;finish&quot;,&quot;actionType&quot;:&quot;SWITCH_CHECK&qu ;}</Item>
  <Item>
{&quot;actionStatus&quot;:&quot;process&quot;,&quot;actionType&quot;:&quot;SWITCH&quot;} </Item>
 </PrevActionStatus>
 <ProcessAction>SWITCH</ProcessAction>
 <ProcessId>6</ProcessId>
 <ProcessStatus>EXECUTING</ProcessStatus>
 <ProcessType>DRILL_RECOVERY</ProcessType>
 <ShowAction>SWITCH_CHECK</ShowAction>
 <StartTime>1760324734000</StartTime>
 <SwitchDirection>amtest128-&gt;amtest217</SwitchDirection>
 <Zone>cn-wulan-env128-amtest217002-b</Zone>
</Data> <Message>success</Message> <RequestId>DC9C8651-9890-423E-8056-8E81F0B95FEE</RequestId> <Success>true</Success>
```

#### GetProcessDetail

Call this operation to retrieve the details of a flow. The details include the products and instances involved in the recovery plan, the switch direction, the current execution step, and the status of the preceding action. Description

**Prerequisites**

Before calling this operation, make sure that the recovery plan flow exists. Call `CreateProcess` to create a recovery flow and obtain the `ProcessId`. You can also call `ListProcesses` to retrieve the `ProcessId` from the list of flows.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ProcessId | Integ er | Body | Yes | 10 | The ID of the flow. |
| ProcessAc tion | Strin g | Body | No | SWITCH | The type of the flow action. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| Success | Boolean | true | The status of the response. The operation was successful. failed: false |
| Code | String | 200 | The status code. A value of 200 indicates that the call was successful. |
| Message | String | success | The returned message. |
| ErrorMessage | String | "" | The error message. |
| ErrorCode | String | 500 | The error code. |
| Path | String | /xxx/xxx | The URI of the request. |
| Cost | Long | 20 | The time consumed by the request. Unit: milliseconds (ms). |
| Data | Struct | {} | The returned data. |
| - PrevActionStat us | String | [] | The status of the preceding action. |

ASR for Zone-disaster Recovery Apsara Stack Resilience

**Request syntax**

**Request parameters**

**Response parameters**

| psara Stack Resil | ience |  | ASR for Zone-disaster Recovery Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| - InstanceAction s | Array | [] | A list of instance statuses. |
| --Id | Integer | 18 | The ID of the instance. |
| --ActionId | Integer | 12 | The task ID. |
| -- ProcessAction | String | SWITCH | The flow action. |
| --SourceIdc | String | amtest12 | The source data center. |
| --DestIdc | String | amtest22 | The destination data center. |
| --Step | Integer | 1 | The step number. |
| --InstanceId | String | rm- 2ze8g2am97624** ** | The instance ID. |
| --InstanceAlias | String | test | The alias of the instance. |
| --Product | String | RDS | The product. |
| --StartTime | Long | 1628265600000 | The start time. |
| --EndTime | Long | 1628265600000 | The end time. |
| --ActionStatus | String | INIT | The status of the action. |
| --Result | String | "" | The returned result. |
| -- ConsumeTime | String | 20 | The time consumed. |
| --TraceId | String | 9A506E30-DA33- 43D6-AACC- C3F85435D890 | The ID of the execution record. |
| -- MasterLocatio n | String | cn-hangzhou-a | The location of the primary node. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| --SyncDelay | String | { "value": "0", "status": true } | The latency. |
| --SyncStatus | String | { "value": "CheckInfo.Increas eReplica", "status": true } | The latency status. |
| --FailoverType | Struct | {} | The switchover type. |
| ---value | String | AUTOMATIC | The content. |
| ---info | String | AutomaticFailover | The information. |
| -ProcessId | String | 4 | The ID of the flow. |
| -ProcessType | String | DRILL RECOVERY _ | The type of the flow. |
| -ProcessAction | String | RECOVERY CHECK _ | The flow action. |
| - ExecutionMod e | String | MANUAL | The execution mode. |
| -ActionStatus | String | NORMAL | The status of the action. |
| -ActionUser | String | 999999999 | The user who executes the action. |
| -StartTime | Long | 1759211487000 | The start time. |
| -EndTime | Long | 1759211487000 | The end time. |
| - SwitchDirectio n | String | amtest21- >amtest22 | The switchover direction. |
| -ConsumeTime | String | 20 | The time consumed for execution. |
| -ShowAction | String | RECOVERY CHECK _ | The flow status displayed on the page. |
| -ProcessStatus | String | FINISH | The status of the flow. |

Apsara Stack Resilience

| Parameter | Type | Example | Description |
|---|---|---|---|
| -CurrentStep | String | 1 | The current step. |
| - ProtectionGrou pId | Integer | 10 | The ID of the protection group. |
| -PlanId | Integer | 16 | The ID of the recovery plan. |
| -Zone | String | cn-hangzhou-a | The zone of the recovery drill. |

Apsara Stack Resilience

**Examples**

Request example

```json
{ "ProcessId":"10" }
```

Successful response example `JSON` format

```json
{
  "Code": "200",
  "Data": {
    "ActionStatus": "SUCCESS",
    "ActionUser": "1933655883841513",
    "ConsumeTime": "0",
    "CurrentStep": 1,
    "EndTime": 1759211487000,
    "ExecutionMode": "AUTOMATIC",
    "InstanceActions": {
      "InstanceAction": [
        {
          "ActionId": 16,
          "ActionStatus": "NORMAL",
          "ConsumeTime": "0",
          "DestIdc": "amtest128",
          "EndTime": 1759211487000,
          "FailoverType": {
            "info": "InstancePrimaryZoneMissMatch",
            "value": "NONEED"
          },
          "Id": 20,
          "InstanceAlias": "rds-mysql80-classic",
          "InstanceId": "rm-jp7r3459uq299j520",
          "MasterLocation": {
            "value": "cn-wulan-env128-amtest128001-a",
            "status": true
}
```

ASR for Zone-disaster Recovery Apsara Stack Resilience

```json
          },
          "ProcessAction": "RECOVERY_CHECK",
          "Product": "RDS",
          "Result": "",
          "SourceIdc": "amtest217",
          "StartTime": 1759211487000,
          "Step": 1,
          "SyncDelay": {
            "value": "0",
            "status": true
          },
          "SyncStatus": {
            "value": "CheckInfo.IncreaseReplica",
            "status": true
          },
          "TraceId": "1759211487345#rm-jp7r3459uq299j520#1#E0C7141D-5EBB-4E80-8595-
C16CF72D81C2"
        },
        {
          "ActionId": 16,
          "ActionStatus": "NORMAL",
          "ConsumeTime": "0",
          "DestIdc": "amtest128",
          "EndTime": 1759211487000,
          "FailoverType": {
            "info": "InstancePrimaryZoneMissMatch",
            "value": "NONEED"
          },
          "Id": 21,
          "InstanceAlias": "mysql-80-vpc",
          "InstanceId": "rm-jp72fab594a0x427u",
          "MasterLocation": {
            "value": "cn-wulan-env128-amtest128001-a",
            "status": true
          },
          "ProcessAction": "RECOVERY_CHECK",
          "Product": "RDS",
          "Result": "",
          "SourceIdc": "amtest217",
          "StartTime": 1759211487000,
          "Step": 2,
          "SyncDelay": {
            "value": "0",
            "status": true
          },
          "SyncStatus": {
            "value": "CheckInfo.IncreaseReplica",
            "status": true
          },
          "TraceId": "1759211487345#rm-jp72fab594a0x427u#1#E0C7141D-5EBB-4E80-8595-
C16CF72D81C2"
        }
```

]

```json
    },
    "PlanId": 4,
```

Apsara Stack Resilience ASR for Zone-disaster Recovery a d: ,

```json
    "PrevActionStatus": {
      "Item": [
        "{\"actionStatus\":\"finish\",\"actionType\":\"SWITCH_CHECK\"}",
        "{\"actionStatus\":\"finish\",\"actionType\":\"SWITCH\"}",
        "{\"actionStatus\":\"finish\",\"actionType\":\"SWITCH_BACK_CHECK\"}",
        "{\"actionStatus\":\"finish\",\"actionType\":\"SWITCH_BACK\"}",
        "{\"actionStatus\":\"finish\",\"actionType\":\"RECOVERY_CHECK\"}"
```

]

```json
    },
    "ProcessAction": "RECOVERY_CHECK",
    "ProcessId": 4,
    "ProcessStatus": "FINISH",
    "ProcessType": "DRILL_RECOVERY",
    "ProtectionGroupId": 3,
    "ShowAction": "RECOVERY_CHECK",
    "StartTime": 1759211487000,
    "SwitchDirection": "amtest217->amtest128",
    "Zone": "cn-wulan-env128-amtest128001-a"
  },
  "Message": "success",
  "RequestId": "FD418663-E79E-4196-AB7A-36922FC2D572",
  "Success": true
}
```

`XML` format

```xml
<Code>200</Code> <Data>
 <ActionStatus>SUCCESS</ActionStatus>
 <ActionUser>1933655883841513</ActionUser>
 <ConsumeTime>0</ConsumeTime>
 <CurrentStep>1</CurrentStep>
 <EndTime>1759211487000</EndTime>
 <ExecutionMode>AUTOMATIC</ExecutionMode>
 <InstanceActions>
  <InstanceAction>
   <ActionId>16</ActionId>
   <ActionStatus>NORMAL</ActionStatus>
   <ConsumeTime>0</ConsumeTime>
   <DestIdc>amtest128</DestIdc>
   <EndTime>1759211487000</EndTime>
   <FailoverType>
    <info>InstancePrimaryZoneMissMatch</info>
    <value>NONEED</value>
   </FailoverType>
   <Id>20</Id>
   <InstanceAlias>rds-mysql80-classic</InstanceAlias>
   <InstanceId>rm-jp7r3459uq299j520</InstanceId>
   <MasterLocation>
    <value>cn-wulan-env128-amtest128001-a</value>
    <status>true</status>
   </MasterLocation>
   <ProcessAction>RECOVERY_CHECK</ProcessAction>
<Prodct>RDS</Prodct>
```

ASR for Zone-disaster Recovery Apsara Stack Resilience

```xml
   <Product>RDS</Product>
   <Result  />
   <SourceIdc>amtest217</SourceIdc>
   <StartTime>1759211487000</StartTime>
   <Step>1</Step>
   <SyncDelay>
    <value>0</value>
    <status>true</status>
   </SyncDelay>
   <SyncStatus>
    <value>CheckInfo.IncreaseReplica</value>
    <status>true</status>
   </SyncStatus>
   <TraceId>1759211487345#rm-jp7r3459uq299j520#1#E0C7141D-5EBB-4E80-8595-
C16CF72D81C2</TraceId>
  </InstanceAction>
  <InstanceAction>
   <ActionId>16</ActionId>
   <ActionStatus>NORMAL</ActionStatus>
   <ConsumeTime>0</ConsumeTime>
   <DestIdc>amtest128</DestIdc>
   <EndTime>1759211487000</EndTime>
   <FailoverType>
    <info>InstancePrimaryZoneMissMatch</info>
    <value>NONEED</value>
   </FailoverType>
   <Id>21</Id>
   <InstanceAlias>mysql-80-vpc</InstanceAlias>
   <InstanceId>rm-jp72fab594a0x427u</InstanceId>
   <MasterLocation>
    <value>cn-wulan-env128-amtest128001-a</value>
    <status>true</status>
   </MasterLocation>
   <ProcessAction>RECOVERY_CHECK</ProcessAction>
   <Product>RDS</Product>
   <Result  />
   <SourceIdc>amtest217</SourceIdc>
   <StartTime>1759211487000</StartTime>
   <Step>2</Step>
   <SyncDelay>
    <value>0</value>
    <status>true</status>
   </SyncDelay>
   <SyncStatus>
    <value>CheckInfo.IncreaseReplica</value>
    <status>true</status>
   </SyncStatus>
   <TraceId>1759211487345#rm-jp72fab594a0x427u#1#E0C7141D-5EBB-4E80-8595-
C16CF72D81C2</TraceId>
  </InstanceAction>
 </InstanceActions>
 <PlanId>4</PlanId>
 <PrevActionStatus>
  <Item>
{&quot;actionStatus&quot;:&quot;finish&quot;,&quot;actionType&quot;:&quot;SWITCHCHECK&qu
```

Apsara Stack Resilience ASR for Zone-disaster Recovery

```xml
{&quot;actionStatus&quot;:&quot;finish&quot;,&quot;actionType&quot;:&quot;SWITCH_CHECK&qu ;}</Item>
  <Item>
{&quot;actionStatus&quot;:&quot;finish&quot;,&quot;actionType&quot;:&quot;SWITCH&quot;} </Item>
  <Item>
{&quot;actionStatus&quot;:&quot;finish&quot;,&quot;actionType&quot;:&quot;SWITCH_BACK_CHE &quot;}</Item>
  <Item>
{&quot;actionStatus&quot;:&quot;finish&quot;,&quot;actionType&quot;:&quot;SWITCH_BACK&quo }</Item>
  <Item>
{&quot;actionStatus&quot;:&quot;finish&quot;,&quot;actionType&quot;:&quot;RECOVERY_CHECK& ot;}</Item>
 </PrevActionStatus>
 <ProcessAction>RECOVERY_CHECK</ProcessAction>
 <ProcessId>4</ProcessId>
 <ProcessStatus>FINISH</ProcessStatus>
 <ProcessType>DRILL_RECOVERY</ProcessType>
 <ShowAction>RECOVERY_CHECK</ShowAction>
 <StartTime>1759211487000</StartTime>
 <SwitchDirection>amtest217-&gt;amtest128</SwitchDirection>
 <Zone>cn-wulan-env128-amtest128001-a</Zone>
</Data> <Message>success</Message> <RequestId>FD418663-E79E-4196-AB7A-36922FC2D572</RequestId> <Success>true</Success>
```

#### SwitchInstance

You can call this operation to retry a switch to a disaster recovery instance for a protection group. The operation performs an instance switch or switchback based on the scenario in the drill plan. Description

**Prerequisites**

Before you call this operation, call the GetProcessDetail operation to retrieve the ProcessId and ProcessAction information.

**Request headers**

This operation uses common request headers. No special request headers are used. For more information, see the documentation about common request parameters.

**Request syntax**

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ProcessId | Integ er | Body | Yes | 10 | The flow ID. |
| ProcessAc tion | Strin g | Body | Yes | SWITCH | The type of the flow action. |
| InstanceId s | Strin g | Body | Yes | rm-hg30ps8hg9vtcqf71r | The instance ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. The failed status is false. |
| Code | String | 200 | The status code. A value of 200 indicates that the call was successful. |
| Message | String | success | The returned message. |
| ErrorMessage | String | "" | The error message. |
| ErrorCode | String | 500 | The error code. |
| Path | String | /xx/xx | The URI of the request. |
| Cost | Long | 20 | The time consumed by the API call. Unit: milliseconds (ms). |

ASR for Zone-disaster Recovery Apsara Stack Resilience

**Response data**

**Examples**

Request example Apsara Stack Resilience ASR for Zone-disaster Recovery

```json
{ "ProcessId":"10", "ProcessAction":"SWITCH", "InstanceIds":"rm-hg30ps8hg9vtcqf71r" }
```

Successful response example `JSON` format

```json
{
 "Path":"/xx/xx",
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "ErrorCode":"500",
 "ErrorMessage":"\"\"",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` format

```xml
<Path>/xx/xx</Path> <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <ErrorCode>500</ErrorCode> <ErrorMessage>&quot;&quot;</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### SetProcessSwitchStep

This API is used to skip a failed batch and proceed to the next one during a manual batch switchover for a protection group. Description Before you call this API, call the GetProcessDetail operation to obtain the ProcessId and ProcessAction. You must also confirm the current failed switchover step.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request syntax**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ProcessId | Integ er | Body | Yes | 22 | The process ID. |
| ProcessAc tion | Strin g | Body | Yes | SWITCH | The type of process action. |
| Step | Integ er | Body | Yes | 2 | The step. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. The operation was successful. Status: Not failed. |
| Code | String | 200 | The status code. A value of 200 indicates that the call was successful. |
| Message | String | success | The returned message. |
| ErrorMessage | String | "" | The error message. |
| ErrorCode | String | 500 | The error code. |
| Path | String | /xxx/xxx | The URI of the request. |
| Cost | Long | 20 | The time it took to process the request. Unit: milliseconds (ms). |
| Data | Integer | 2 | The returned data. |

ASR for Zone-disaster Recovery Apsara Stack Resilience

**Request parameters**

**Response parameters**

**Examples**

Request example Apsara Stack Resilience ASR for Zone-disaster Recovery

```json
{ "ProcessId":"22", "ProcessAction":"SWITCH", "Step":"2" }
```

Response example `JSON` format

```json
{
 "Path":"/xxx/xxx",
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "Data":2,
 "ErrorCode":"500",
 "ErrorMessage":"\"\"",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` format

```xml
<Path>/xxx/xxx</Path> <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data>2</Data> <ErrorCode>500</ErrorCode> <ErrorMessage>&quot;&quot;</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```
