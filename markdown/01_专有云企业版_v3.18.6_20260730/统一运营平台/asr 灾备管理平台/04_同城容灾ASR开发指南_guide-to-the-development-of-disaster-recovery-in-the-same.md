---
title: "灾备管理平台 同城容灾ASR开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 111
source_pdf: "04_同城容灾ASR开发指南_guide-to-the-development-of-disaster-recovery-in-the-same.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/asr/zh/guide-to-the-development-of-disaster-recovery-in-the-same.pdf"
converter: line-classifier (PyMuPDF)
---

# 灾备管理平台 同城容灾ASR开发指南

灾备管理中心流程说明

## API调用流程说明

阿里云专有云支持通过POP网关调用同城容灾管理平台ASR的API。

**流程图**

同城容灾管理平台ASR的API调用流程如下图所示。

**调用步骤**

1. 获取API信息。
2. 获取AccessKey ID和AccessKey Secret，获取方式请参见获取AccessKey。
3. 获取同城容灾管理平台ASR的Endpoint和Region ID，获取方式请参见获取API信息及其Endpoint。
4. 获取同城容灾管理平台ASR的SDK包和SDK核心库，获取方法请参见通过POP网关调用专有云API。
5. 调用同城容灾管理平台ASR的API接口。
灾备管理中心

## 准备工作

### 获取AccessKey

**背景信息**

AccessKey通过使用AccessKey ID和AccessKey Secret对称加密，实现验证某个请求发送者的身份的功能。其中AccessKey ID用于标识用户，AccessKey Secret是用户用于加密签名的字符串。 Apsara Uni-manager运营控制台提供了个人AccessKey和组织AccessKey。推荐使用个人账号 AccessKey调用接口。

**说明**

只有运营管理员和一级组织管理员可以获取组织AccessKey。

**获取个人账号AccessKey时，请确保登录的用户具备组织备份管理员角**

**色，否则可能导致接口调用失败。**

**获取个人账号AccessKey**

1. 登录Apsara Uni-manager运营控制台。
2. 在系统界面右上角，单击当前登录用户头像，单击**个人信息**。
3. 在**AccessKey**区域，您可以查看个人账户的AccessKey信息。

**重要**

AccessKey ID和AccessKey Secret是您访问云资源时的密钥，具有该账号完整的权限，请您妥善保管。

**获取组织AccessKey**

**警告**

个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限AccessKey，组织 AccessKey相对权限较大，需要管理员确认操作的安全性。
1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，单击**企业**。
灾备管理中心
3. 在左侧导航栏中，选择**资源管理**>**组织管理**。
4. 在组织结构中，单击目标一级组织名称。
5. 单击**管理****Accesskey**。
6. 在弹出的对话框中，查看组织AccessKey信息。

### 获取API信息及其Endpoint

首先，您需要了解产品开放API接口的相关信息，包括产品名称（code）、开放API接口名称、API版本。

**操作步骤**

1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏选择**平台运维** > **飞天基础运维平台** > **资源管理**。
3. 在左侧导航栏中选择**资源管理** > **产品集群运维**。
4. 在搜索框中输入bcmc。
5. 单击**集群详情**，进入详情页面，选择**终态配置**页签。
6. 选择kv.conf，单击**显示内容**查看并保存region值。
灾备管理中心
7. 选择**服务列表**页签，单击bcmc服务名称，进入服务bcmc详情页。
8. 获取asr.pop.open.endpoint的值并保存。

### 通过POP网关调用专有云API

#### Python版本

**环境要求**

安装 SDK 核心库 Core ，使用pip安装包依赖

**安装说明代码**

从开发者门户获取SDK包后可使用以下 Mavan 依赖配置进行管理：

```
pip install apsarastack_asr20250916.tar.gz
```

**安装说明文档**

**开发者门户获取 SDK**

1.登录 ASCM 的开发者门户，单击 SDK 示例。 2.SDK 类型下拉选择高级版，选择 Java 语言。 灾备管理中心 3.下方可看到示例代码，点击下载完整工程以获取示例项目及 SDK 包。

**导入 SDK 包**

1.通过以下任一方式创建 Maven 项目。 方式一：在 IDEA 中添加一个 Maven 项目。 灾备管理中心方式二：将已有的项目转换为 Maven 项目。 右键单击要转换的项目，并选择**Add Framework Support** ...。 选择 Maven，并单击 OK。 2.在项目根目录下创建 lib 包，将 Java SDK 包放入到 lib 目录下，如下图。 3.在项目目录下的 pom.xml 中，添加 Java SDK 依赖，代码请参考上文中《安装说明代码》部分。 4.查看 IDEA 右侧 Maven 栏，如图所示，表示已成功导入依赖。

**代码示例**

请参考示例，将某个 API 录入，注意保证代码通过，隐私信息泄露。

```java
# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import os import sys from typing import List from alibabacloud_tea_openapi import models as open_api_models from alibabacloud_tea_util import models as util_models from alibabacloud_darabonba_env.client import Client as EnvClient from alibabacloud_tea_console.client import Client as ConsoleClient from alibabacloud_tea_util.client import Client as UtilClient from apsarastackasr20250916.client import Client as SddpClient
```

灾备管理中心 _

```python
from apsarastack_asr20250916 import models as sddp_models class Sample:
    def __init__(self):
        pass
    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
        region_id: str,
    ) -> SddpClient:
        """
```

使用`AK&SK`初始化账号`Client`

```bash
        """
        config = open_api_models.Config()
        # endpoint
        config.endpoint = '<yourEndpoint>'
        # 您的AccessKey ID
        config.access_key_id = access_key_id
        # 您的AccessKey Secret
        config.access_key_secret = access_key_secret
```

# 您的可用区`ID`

```python
        config.region_id = region_id
        return SddpClient(config)
    @staticmethod
    def main(
        args: List[str],
    ) -> None:
```

# 特殊`Header`参数,设置组织`ID`和资源集`ID,`资源隔离使用，请根据实际修改
# 调用专有云`API`时，一般需要提供多个公共`Header`参数，包括：`x-acs-regionid`、`x-acs-`

```
organizationid、x-acs-resourcegroupid
```

# 额外参数需使用带`WithOptions`后缀的方法，例：

```
describeImagesWithOptions(describeImagesRequest, runtime)
        headers = {
            'x-acs-organizationid': '<yourOrganizationId>',
            'x-acs-resourcegroupid': '<yourResourceGroupId>',
            'x-acs-regionId': '<yourRegionId>',
        }
        extends_params = util_models.ExtendsParameters(
            headers=headers
```

)
# 创建并配置 `runtimeOptions`

```
        runtime_options = util_models.RuntimeOptions(
            extends_parameters=extends_params
```

)
# 为保障生产环境通信安全，建议您保持开启，若在测试环境必须忽略证书校验，可以通过运行时参数`igno`
`reSSL`设置
# 忽略对 `SSL` 证书的验证
灾备管理中心

```
        runtime_options.ignore_ssl = True
        client = Sample.create_client('<yourAccessKeyId>', '<yourAccessKeySECRET>', '<y
ourRegionId>')
        request = sddp_models.ListProtectionGroupRequest()
```

`request.page_number = 1 //` 该参数值为假设值，请您根据实际情况进行填写 `request.page_size = 10 //` 该参数值为假设值，请您根据实际情况进行填写 `request.protection_name = "bcmctest" //` 该参数值为假设值，请您根据实际情况进行填写

```
        response = client.list_protection_group_with_options(request, headers,
runtime_options)
        detail = response.body
        ConsoleClient.log(UtilClient.to_jsonstring(detail))
if __name__ == '__main__':
    Sample().main(sys.argv[1:])
```

**步骤示例**

1. 初始化配置对象Config 。 Config 对象存放 AccessKeyId、AccessKeySecret 、Endpoint 等配
置，Endpoint 可以在ASCM的开发者门户查询。

```python
@staticmethod def create_client(
        access_key_id: str,
        access_key_secret: str,
        region_id: str,
    ) -> SddpClient:
        """
```

使用`AK&SK`初始化账号`Client`

```bash
        """
        config = open_api_models.Config()
        # endpoint
        config.endpoint = '<yourEndpoint>'
        # 您的AccessKey ID
        config.access_key_id = access_key_id
        # 您的AccessKey Secret
        config.access_key_secret = access_key_secret
```

# 您的可用区`ID`

```
        config.region_id = region_id
        return SddpClient(config)
```

2. 实例化一个客户端，生成对象 client 。

```
client = Sample.create_client('<yourAccessKeyId>', '<yourAccessKeySECRET>', '<yourRegionId>')
```

`request.page_number = 1 //` 该参数值为假设值，请您根据实际情况进行填写 `request.page_size = 10 //` 该参数值为假设值，请您根据实际情况进行填写 `request.protection_name = "bcmctest" //` 该参数值为假设值，请您根据实际情况进行填写灾备管理中心
3. 创建对应 API 的 Request 。方法的命名规则为 API 方法名加上 Request 。例如获取保护组列表接口
ListProtectionGroup，对应的方法为ListProtectionGroupRequest。

```
request = sddp_models.ListProtectionGroupRequest()
```

4. 设置调用方法的header和运行时参数

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
# 创建并配置 `runtimeOptions`

```
 runtime_options = util_models.RuntimeOptions(
            extends_parameters=extends_params
```

)
# 为保障生产环境通信安全，建议您保持开启，若在测试环境必须忽略证书校验，可以通过运行时参数`ignoreSSL`设
置
# 忽略对 `SSL` 证书的验证

```
runtime_options.ignore_ssl = True
```

5. 通过 client 对象获得对应 request 响应 response 。

```
response = client.list_protection_group_with_options(request, headers, runtime_options) detail = response.body ConsoleClient.log(UtilClient.to_jsonstring(detail))
```

7.使用 try...except处理报错。

```
except Exception as e:
```

# 处理异常

```
   logging.error(e)
```

#### Java版本

**环境要求**

支持 JDK8~JDK19，Platform 支持：Linux、Mac、Windows。

**安装说明代码**

从开发者门户获取SDK包后可使用以下 Mavan 依赖配置进行管理：

```xml
<dependency>
       <groupId>com.aliyun.apsarastack</groupId>
       <artifactId>asr20250916</artifactId>
       <version>3.18.6-SP003-SNAPSHOT</version>
</dependency>
```

灾备管理中心

**安装说明文档**

**开发者门户获取 SDK**

1.登录 ASCM 的开发者门户，单击 SDK 示例。 2.SDK 类型下拉选择高级版，选择 Java 语言。 3.下方可看到示例代码，点击下载完整工程以获取示例项目及 SDK 包。

**导入 SDK 包**

1.通过以下任一方式创建 Maven 项目。 方式一：在 IDEA 中添加一个 Maven 项目。 灾备管理中心方式二：将已有的项目转换为 Maven 项目。 右键单击要转换的项目，并选择**Add Framework Support** ...。 选择 Maven，并单击 OK。 2.在项目根目录下创建 lib 包，将 Java SDK 包放入到 lib 目录下，如下图。 3.在项目目录下的 pom.xml 中，添加 Java SDK 依赖，代码请参考上文中《安装说明代码》部分。 4.查看 IDEA 右侧 Maven 栏，如图所示，表示已成功导入依赖。

**代码示例**

请参考示例，将某个 API 录入，注意保证代码通过，隐私信息泄露。

```java
import com.aliyun.apsarastack.asr20250916.Client; import com.aliyun.apsarastack.asr20250916.models.*; import com.aliyun.teautil.models.ExtendsParameters; import com.aliyun.teautil.models.RuntimeOptions; import com.google.gson.Gson; import java.util.HashMap; import java.util.Map; public class Sample {
    public static Client createClient() throws Exception {
```

灾备管理中心 `//`组织或者`ASCM`用户的`AK/SK`

```
        com.aliyun.teaopenapi.models.Config config = new
com.aliyun.teaopenapi.models.Config()
```

`//` 必填

```
                .setAccessKeyId("<yourAccessKeyID>")
```

`//` 必填

```
                .setAccessKeySecret("<yourAccessKeySecret>");
```

`// Endpoint` 产品的`POP` 接口对外的域名，

```
        config.endpoint = "<yourEndpoint>";
        return new Client(config);
    }
    public static void main(String[] args_) throws Exception {
        SwitchInstance();
    }
    public static void testSwitchInstance() throws Exception {
        Client client = createClient();
        SwitchInstanceRequest switchInstanceRequest = new SwitchInstanceRequest();
        RuntimeOptions runtime = new RuntimeOptions();
        Map<String, String> headers = new HashMap<String, String>();
```

`//` 组织`ID,` 资源组`ID,`从`ASCM`上获取当前账号的组织`ID,` 资源组`ID`信息

```
        headers.put("x-acs-organizationid", "<yourOrganizatioId>");
        headers.put("x-acs-resourcegroupid", "<yourResourceGroupID>");
        headers.put("x-acs-regionId", "<yourRegionID>");
        runtime.ignoreSSL = true;
        runtime.setExtendsParameters(new ExtendsParameters().setHeaders(headers));
```

switchInstanceRequest.setProcessId(97); // 该参数值为假设值，请您根据实际情况进行填写 switchInstanceRequest.setProcessAction("SWITCH"); // 该参数值为假设值，请您根据实际情况进行填写 switchInstanceRequest.setInstanceIds("oss-instance1"); // 该参数值为假设值，请您根据实际情况进行填写

```java
        try {
client.switchInstanceWithOptions(switchInstanceRequest, headers, runtime);
            System.out.println(new Gson().toJson(response.body));
        } catch (Exception error) {
```

`//` 错误 `message`

```java
            System.out.println(error.getMessage());
        }
    }
}
```

**步骤示例**

1. 初始化配置对象com.aliyun.teaopenapi.models.Config 。 Config 对象存放 AccessKeyId、
AccessKeySecret 、Endpoint 等配置，Endpoint 可以在ASCM的开发者门户查询。 灾备管理中心 `//`组织或者`ASCM`用户的`AK/SK`

```
com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config()
```

`//` 必填

```
    .setAccessKeyId("<yourAccessKeyID>")
```

`//` 必填

```
    .setAccessKeySecret("<yourAccessKeySecret>");
```

`// Endpoint` 产品的`POP` 接口对外的域名

```
config.endpoint = "<yourEndpoint>";
```

2. 实例化一个客户端，从 com.aliyun.apsarastack.asr20250916.Client类生成对象 client 。后续
request、response 从 com.aliyun.apsarastack.asr20250916.models 中获得。

```
Client client = new Client(config);
```

3. 创建对应 API 的 Request 。类的命名规则为 API 方法名加上 Request 。例如实例切换接口
SwitchInstance，对应的类为SwitchInstanceRequest。

```
SwitchInstanceRequest switchInstanceRequest = new SwitchInstanceRequest();
```

4. 设置调用方法的参数和header

```
RuntimeOptions runtime = new RuntimeOptions(); Map<String, String> headers = new HashMap<String, String>();
```

`//` 组织`ID,` 资源组`ID,`从`ASCM`上获取当前账号的组织`ID,` 资源组`ID`信息

```
headers.put("x-acs-organizationid", "<yourOrganizatioId>"); headers.put("x-acs-resourcegroupid", "<yourResourceGroupID>"); headers.put("x-acs-regionId", "<yourRegionID>"); runtime.ignoreSSL = true; runtime.setExtendsParameters(new ExtendsParameters().setHeaders(headers));
```

switchInstanceRequest.setProcessId(97); // 该参数值为假设值，请您根据实际情况进行填写 switchInstanceRequest.setProcessAction("SWITCH"); // 该参数值为假设值，请您根据实际情况进行填写 switchInstanceRequest.setInstanceIds("oss-instance1"); // 该参数值为假设值，请您根据实际情况进行填写
5. 通过 client 对象获得对应 request 响应 response 。

```java
client.switchInstanceWithOptions(switchInstanceRequest, headers, runtime); System.out.println(new Gson().toJson(response.body));
```

7.使用 catch() 处理报错。

```
except Exception as e:
```

# 处理异常

```
    logging.error(e)
```

#### SDK概览

**概览**

灾备管理中心文档中 SDK 关于 API 的示例代码仅供参考，各 API 的完整使用步骤与参数说明请参见开发者门户 SDK 示例和 OpenAPI 文档。

**SDK版本**

| 语言 | 版本号 | 发布时间 | 更新内容 |
|---|---|---|---|
| Java | 3.18.6-SP003 | 2025/09 | ASR开放保护组API演练接口 |
| Python | 3.18.6-SP003 | 2025/09 | ASR开放保护组API演练接口 |

**API列表**

当前 SDK 支持的 API 列表。

| API名称 | 所在版本 |
|---|---|
| ASR.CheckProductInstance.2025-09-16 | v3.18.6 |
| ASR.CloseProcess.2025-09-16 | v3.18.6 |
| ASR.CreateDisasterRecoveryProcess.2025-09-16 | v3.18.6 |
| ASR.CreateDrillProcess.2025-09-16 | v3.18.6 |
| ASR.CreateHdrReverse.2025-09-16 | v3.18.6 |
| ASR.CreateNextProcess.2025-09-16 | v3.18.6 |
| ASR.ExecuteProcess.2025-09-16 | v3.18.6 |
| ASR.GetDrillPlan.2025-09-16 | v3.18.6 |
| ASR.GetInstanceStatus.2025-09-16 | v3.18.6 |
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

|  | 灾备管理中心 | 同城容灾管理平台开发指南·准备工作 |  |
|---|---|---|---|

| API名称 | 所在版本 |
|---|---|
| ASR.ListProtectionGroupStatus.2025-09-16 | v3.18.6 |
| ASR.SetProcessSwitchStep.2025-09-16 | v3.18.6 |
| ASR.SwitchInstance.2025-09-16 | v3.18.6 |

**可用性说明**

在之前版本曾提供过的 API 中，有部分已不推荐使用，有部分已废弃不支持。本文主要阐述不推荐使用和已不支持的 API 情况。 对于不推荐使用的 API，并且仍会在 API 参考中阐述该接口的调用方法，IDE 中会带有过时标记。一般情况下，不推荐使用的 API 将不再在后续专有云版本中继续提供支持。 对于已不支持的 API，大部分均不存在替代接口，且不会在 API 参考中阐述该接口的调用方法；少部分已不支持的 API 有功能相似的替代 API 提供使用。 IDEA 会带上过时标记方便开发人员注意到过时 API，新用户不应该再使用这些接口。 灾备管理中心息

## 错误码信息

本章节介绍API接口调用时常见的错误码以及错误信息。 调用ASR API时可能遇到两类错误：SDK调用异常和后端业务执行异常。当请求POP接口出错时，系统会返回相应的错误提示，此类问题通常由接口调用方式不当引起，需根据提示调整请求参数。以下是常见的POP SDK异常说明。

| 状态码 | 错误码 | 错误提示 | 报错场景 |
|---|---|---|---|
| 404 | InvalidProduct.NotFou nd | Cannot find product according to your specified domain. | Domain不正确（通过Domain 找不到Product）。 |
| 404 | InvalidApi.NotFound | Specified api is not found,please check your url and method. | API不存在，或该API为Private 类型且当前用户未在授权名单中。 |
| 400 | InvalidProtocol.NeedSs l | Your request is denied as lack of ssl protect. | API必须使用HTTPS协议。 |
| 400 | Missing{ParameterNa me} | {ParameterName} is mandatory for this action. | 必填参数没有填（{}中替换成相应的参数名）。 |
| 404 | InvalidAccessKeyId.No tFound | Specified access key is not found. | AccessKeyId找不到。 |
| 400 | InvalidAccessKeyId.Ina ctive | Specified access key is disabled. | AccessKeyId被禁用。 |
| 400 | InvalidTimeStamp.For mat | Specified time stamp or date value is not well formatted. | 时间戳格式错误，请使用Date 或 Timestamp格式。 |
| 400 | InvalidTimeStamp.Expi red | Specified time stamp or date value is expired. | 时间戳已过期。请确保设备时间与服务器时间同步（允许偏差范围：15分钟以内）。 |
| 413 | PayloadTooLarge | The request payload is too large, the limitation is xxx bytes. | 请求体过大，超出限制（最大允许 xxx 字节）。请减少请求数据大小后重试。 |

对于后端业务异常，一般接口可以正常获取返回信息。然而，此时接口的返回信息中，Success字段显示为 false，同时异常信息将包含具体的错误信息，包括错误码（Error Code）和错误消息（Error Message）。请根据具体的错误信息与同城容灾研发团队联系，以便进行定位和处理。 灾备管理中心息

| Success | ErrorCode | ErrorMessage | 错误信息 |
|---|---|---|---|
| fasle | authenticationFailed | authenticationFailed | 请求鉴权失败，请检查凭证或权限配置。 |
| fasle | internalError | Internal Error | ASR服务内部发生错误， 请稍后重试或联系技术支持。 |
| fasle | instanceCheckError | Product instance check error | 产品实例校验异常，请确认实例状态是否正常。 |
| fasle | protectionGroupListError | ProtectionGroup list query error! | 无法获取保护组列表，请检查服务状态。 |
| fasle | protectionGroupStatisticsErro r | ProtectionGroup statistics error! | 无法获取保护组概览信息。 |
| fasle | protectionGroupStatusError | protectionGroupStatus Error！ | 保护组状态检查异常。 |
| fasle | protectionGroupDetailError | ProtectionGroup detail query error! | 保护组详细信息查看异常。 |
| fasle | recoveryProcessQueryError | Recovery process detail query error! | 流程信息查询异常。 |
| fasle | recoveryProcessTraceError | recovery process trace query error! | 切换日志查询异常。 |
| fasle | createNextRecoveryProcessE rror | Create next recovery process error! | 创建下一个恢复步骤失败，请检查当前流程状态。 |
| fasle | executeRecoveryProcessErro r | Execute recovery process error! | 执行恢复步骤失败，请确认操作条件是否满足。 |
| fasle | skipRecoveryProcessError | Skip recovery process step error! | 跳过恢复步骤失败，请确认是否允许跳过该步骤。 |
| fasle | recoveryProcessCloseError | Recovery process close error! | 关闭恢复流程失败，请确认流程未处于执行中状态。 |

灾备管理中心息

| fasle | switchInstanceError | switch instance error! | 实例切换操作异常，请检查目标实例状态。 |
|---|---|---|---|
| fasle | createHdrReverseError | Create hdr reverse error! | HDR保护组反向切换失败，请检查同步状态。 |

灾备管理中心

## API参考

### 保护组

#### ListProtectionGroup

该接口用于列出保护组的清单, 包括保护组的创建信息、涉及示例信息和当前状态。 接口说明

## 准备工作

该接口用于列出保护组的清单, 支持全量进行查询，如果传入参数如PageNumber，支持按照条件进行筛选。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PageNum ber | Integ er | Body | 否 | 1 | 页码。 |
| PageSize | Integ er | Body | 否 | 10 | 每页条数。 |
| Protection Name | Strin g | Body | 否 | test | 保护组名称 |
| CheckStat us | Strin g | Body | 否 | NORMAL | 检查状态 |
| Protection GroupId | Integ er | Body | 否 | 10 | 保护组id |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array | {} | 返回数据。 |
| - ProtectionGrou pId | Integer | 10 | 保护组id |

| 同城容灾管理平台开 | 发指南·API参考 |  | 灾备管理中心 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - ProtectionNam e | String | test | 保护组名 |
| -Description | String | test | 描述 |
| -CheckStatus | String | NORMAL | 检查状态 |
| -GmtCreate | Long | 1756107183000 | 创建时间 |
| -GmtModified | Long | 1756107183000 | 修改时间 |
| -CreateUid | String | 999999999 | 创建账号id |
| -AccountId | String | 999999999 | 主账号 |
| -Instances | String | rm-xxx | 实例名 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| Code | String | 200 | 状态码。 200：调用正常。 |
| Message | String | success | 返回信息。 |
| ErrorMessage | String | "" | 错误信息。 |
| ErrorCode | String | 500 | 错误码。 |
| Path | String | /xxx/ | 请求路径。 |
| Cost | Long | 20 | 接口耗时，单位：毫秒（ms）。 |
| TotalCount | Integer | 100 | 列表条目数。 |

| 灾备管理中心 |  |  | 同城容灾管理平台开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| PageNumber | Integer | 1 | 页码。 |
| PageSize | Integer | 10 | 每页行数。 |

**示例**

请求示例

```
{ }
```

正常返回示例 `JSON` 格式

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

`XML` 格式灾备管理中心

```xml
<Path>/xxx/</Path> <TotalCount>100</TotalCount> <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <Instances>rm-xxx</Instances>
 <GmtCreate>1756107183000</GmtCreate>
 <Description>test</Description>
 <AccountId>999999999</AccountId>
 <ProtectionGroupId>10</ProtectionGroupId>
 <ProtectionName>test</ProtectionName>
 <CheckStatus>NORMAL</CheckStatus>
 <GmtModified>1756107183000</GmtModified>
 <CreateUid>999999999</CreateUid>
</Data> <ErrorCode>500</ErrorCode> <ErrorMessage>&quot;&quot;</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### ListProtectionGroupStatistics

该接口用于查询保护组的概览信息，包含保护组的切换次数、涉及产品、示例和上次演练时间等。 接口说明

## 准备工作

该接口用于查询保护组的概览信息，包含保护组的切换次数、涉及产品、示例和上次演练时间等，使用该接

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /api/pop/v1/listProtectionGroupStatistics HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Protection GroupIds | Strin g | Body | 是 | 12 | 保护组ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| Code | String | 200 | 状态码。 200：调用正常。 |
| Message | String | success | 返回信息。 |
| ErrorMessage | String | "" | 错误信息。 |
| ErrorCode | String | 500 | 错误码。 |
| Path | String | /xxx/ | 请求路径。 |
| Cost | Long | 20 | 接口耗时，单位：毫秒（ms）。 |
| Data | Struct | {} | 返回数据。 |
| -Instances | Array | [] | 实例内容 |
| --Product | String | RDS | 云产品。 |
| --NormalCount | Integer | 10 | 产品正常实例数 |
| -- AbnormalCoun t | Integer | 10 | 产品异常实例数 |
| -DrillPlanCount | Integer | 10 | 演练计划数量 |
| -DrillCount | Integer | 10 | 演练次数 |
| -DrillSuccess | Integer | 10 | 演练成功次数 |
| -DrillFailure | Integer | 10 | 演练失败次数 |

|  | 同城容灾管理平台开 | 发指南·API参考 |  | 灾备管理中心 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - CrashPlanCou nt | Integer | 10 | 应急计划数量 |
| -CrashCount | Integer | 10 | 应急次数 |
| -CrashSuccess | Integer | 10 | 应急成功次数 |
| -CrashFailure | Integer | 10 | 应急失败次数 |
| - SwitchCheckC ount | Integer | 10 | 切换检查次数 |
| - RecoveryChec kCount | Integer | 10 | 恢复检查次数 |
| - SwitchBackCh eckCount | Integer | 10 | 回切检查次数 |
| -SwitchCount | Integer | 10 | 切换次数 |
| - SwitchBackCo unt | Integer | 10 | 回切次数 |
| - NonProcessCo unt | Integer | 10 | 无流程个数 |

**示例**

请求示例

```json
POST /api/pop/v1/listProtectionGroupStatistics HTTP/1.1 { "ProtectionGroupIds":"12" }
```

正常返回示例 `JSON` 格式灾备管理中心

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

`XML` 格式灾备管理中心

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

该接口用于列出保护组的状态, 主要用于获取当前保护组的状态是否正常。 接口说明

**注意事项**

接口返回信息中的 CanEdit 字段仅供前端白屏使用，使用API 调用无需关注。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /api/pop/v1/listProtectionGroupStatus HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Protection GroupIds | Strin g | Body | 是 | 10 | 保护组id。 |

灾备管理中心

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array | {} | 返回数据。 |
| - ProtectionGrou pId | Integer | 10 | 保护组ID。 |
| -Status | String | Normal | 保护组状态。 |
| -CanEdit | Boolean | true | 是否可编辑 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| Code | String | 200 | 状态码。 200：调用正常。 |
| Message | String | success | 返回信息。 |
| ErrorMessage | String | "" | 错误信息。 |
| ErrorCode | String | 500 | 错误码。 |
| Path | String | /xxx/ | 请求路径。 |
| Cost | Long | 20 | 接口耗时，单位：毫秒（ms）。 |

**示例**

请求示例

```json
POST /api/pop/v1/listProtectionGroupStatus HTTP/1.1 { "ProtectionGroupIds":"10" }
```

正常返回示例 `JSON` 格式灾备管理中心

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

`XML` 格式

```xml
<Path>/xxx/</Path> <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data>
 <Status>Normal</Status>
 <ProtectionGroupId>10</ProtectionGroupId>
 <CanEdit>true</CanEdit>
</Data> <ErrorCode>500</ErrorCode> <ErrorMessage>&quot;&quot;</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### GetProtectionGroup

获取保护组的详细信息，包括保护组中包含的产品信息和添加到保护组的实例信息接口说明

## 准备工作

调用该接口需要传递ProtectionGroupId 参数，建议先根据ListProtectionGroup的接口获取所有的保护组列表信息，根据实际创建的保护组名字获取对应的ProtectionGroupId 参数。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

灾备管理中心

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Protection GroupId | Integ er | Body | 是 | 10 | 保护组id。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8 | 请求ID。 |
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| Code | String | 200 | 请求返回代码，如为200则请求成功。 |
| Message | String | success | 附加信息。 |
| ErrorMessage | String | "" | 错误信息。 |
| ErrorCode | String | 500 | 错误码。 |
| Path | String | /xxx/xx | 请求路径。 |
| Cost | Long | 30 | 接口耗时，单位：毫秒（ms）。 |
| Data | Struct | {} | 返回数据。 |
| -Instances | Array | [] | 实例列表。 |
| --ZoneInfo | String | cn-wulan-env10- amtest10000-a | 可用区信息。 |
| --InstanceId | String | "rm-xx" | 实例ID。 |
| --InstanceAlias | String | "rm-xx" | 实例别名。 |
| --Product | String | RDS | 云产品Code。 |
| -- MasterLocatio n | String | cn-wulan-env10- amtest10000-a | 主节点位置 |

| 同城容灾管理平台开 | 发指南·API参考 |  | 灾备管理中心 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --CheckStatus | String | NORMAL | 示例状态。 |
| --CheckTime | Long | 1635143903000 | 最近检查时间戳。 |
| --Result | String | success | 返回结果。 |
| --Info | String | “ ” | 返回信息。 |
| -Id | Integer | 10 | 保护组id。 |
| - ProtectionNam e | String | test | 保护组名字。 |
| -Description | String | test | 描述。 |
| -CheckStatus | String | NORMAL | 检查状态。 |
| -GmtCreate | Long | 1756107183000 | 创建时间。 |
| -GmtModified | Long | 1756107183000 | 修改时间。 |
| -AccountId | String | 999999999 | 主账号id。 |
| -CreateUid | String | 999999999 | 创建人uid |
| -CanEdit | Boolean | true | 是否能编辑。 |

**示例**

请求示例

```json
{ "ProtectionGroupId":"10" }
```

正常返回示例 `JSON` 格式灾备管理中心

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
    "Info":"“ ”",
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

`XML` 格式灾备管理中心

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
  <Info>“ ”</Info>
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

该接口用于检查产品实例状态, 实例是否容灾，根据返回的实例信息可以判断实例是否支持容灾切换。 接口说明

## 准备工作

使用该接口时，请确认传入的实例信息归属组织， ASR侧并不进行实例的组织校验，请提前校验，避免越权问题。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

灾备管理中心

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| CloudProd uct | Strin g | Body | 是 | RDS | 云产品。 |
| InstanceId s | Strin g | Body | 是 | rm-2ze8g2am97624 | 实例ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8 | 请求ID。 |
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| Code | String | 200 | 状态码。 200：调用正常。 |
| Message | String | success | 返回信息。 |
| ErrorMessage | String | "" | 错误信息。 |
| ErrorCode | String | 500 | 错误码。 |
| Path | String | /xxx/xxx | 请求路径。 |
| Cost | Long | 20 | 接口耗时，单位：毫秒（ms）。 |
| Data | Struct | {} | 返回数据。 |
| -Instances | Array | [] | 实例列表。 |
| --InstanceId | String | rm- 2ze8g2am97624 | 实例ID。 |
| --Available | Boolean | true | 是否可用 |
| --Message | String | message | 返回信息。 |
| -CloudProduct | String | RDS | 云产品。 |

灾备管理中心

**示例**

请求示例

```json
{ "CloudProduct":"RDS", "InstanceIds":"rm-2ze8g2am97624" }
```

正常返回示例 `JSON` 格式

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

`XML` 格式

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

灾备管理中心

#### GetZoneInfo

该接口用于获取创建演练计划时可选的可用区信息。 接口说明

## 准备工作

该接口用于获取创建演练计划时可选的可用区信息, 用于保护组创建时获取可选的可用区时使用。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| Code | String | 200 | 状态码。 200：调用正常。 |
| Message | String | success | 返回信息。 |
| ErrorMessage | String | "" | 错误信息。 |
| ErrorCode | String | 500 | 错误码。 |
| Path | String | /xxx/ | 请求路径。 |
| Cost | Long | 20 | 接口耗时，单位：毫秒（ms）。 |
| Data | Struct | {} | 返回数据。 |
| -ZoneInfo | String | cn-wulan-env10- amtest10000-a | 可用区信息。 |

**示例**

灾备管理中心请求示例正常返回示例 `JSON` 格式

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

`XML` 格式

```xml
<Path>/xxx/</Path> <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data>
 <ZoneInfo>cn-wulan-env10-amtest10000-a</ZoneInfo>
</Data> <ErrorCode>500</ErrorCode> <ErrorMessage>&quot;&quot;</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

### 演练计划

#### ListProcesses

该接口用于列出演练流程的步骤信息，包括流程的类型、执行模式和当前状态。 接口说明

## 准备工作

该接口支持查询全部的流程信息，查询所有流程信息时无需传入参数。如果想要单独查询某个流程的信息，需要传入流程的ProcessId参数。该接口专用于升级场景的资源处理，客户使用API可以使用

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 灾备管理中心

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ProcessId | Integ er | Body | 否 | 1 | 流程ID。 |
| PlanName | Strin g | Body | 否 | test | 计划名。 |
| Execution Mode | Strin g | Body | 否 | MANUAL | 执行模式， |
| ProcessSt atus | Strin g | Body | 否 | EXECUTING | 流程状态。 |
| PageNum ber | Integ er | Body | 否 | 1 | 页码。 |
| PageSize | Integ er | Body | 否 | 100 | 每页条数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array | {} | 返回数据。 |
| -PgId | Integer | 10 | 保护组id |
| -PlanId | Integer | 16 | 演练计划ID. |
| -PlanName | String | test | 计划名称。 |
| -Zone | String | cn-wulan-env10- amtest10000-a | 可用区。 |
| -ProcessId | Integer | 5 | 流程id. |
| -ProcessType | String | DRILL RECOVERY _ | 流程类型。 |
| - ProtectionNam e | String | test | 保护组名。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - ExecutionMod e | String | MANUAL | 执行模式。 |
| -ProcessStatus | String | EXECUTING | 流程状态 |
| -AccountId | String | 999999999 | 主账号id |
| -CreateUid | String | 999999999 | 创建uid |
| -StartTime | Long | 1756112392000 | 开始时间。 |
| -EndTime | Long | 1756112392000 | 结束时间。 |
| -OrderId | Integer | 9 | 排序字段。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| Code | String | 200 | 状态码。 200：调用正常。 |
| Message | String | success | 返回信息。 |
| ErrorMessage | String | "" | 错误信息。 |
| ErrorCode | String | 500 | 错误码。 |
| Path | String | /xxx/ | 请求路径。 |
| Cost | Long | 20 | 接口耗时，单位：毫秒（ms）。 |
| TotalCount | Integer | 100 | 列表条目数。 |
| PageNumber | Integer | 1 | 页码。 |

| 灾备管理中心 |  |  | 同城容灾管理平台开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| PageSize | Integer | 10 | 每页行数。 |

**示例**

请求示例

```
{ }
```

正常返回示例 `JSON` 格式

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

`XML` 格式灾备管理中心

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

该接口用于列出演练流程的步骤信息，包括流程的类型、执行模式和当前状态。 接口说明

## 准备工作

该接口支持查询全部的演练流程信息，查询所有流程信息时无需传入参数。如果想要单独查询某个流程的信息，需要传入流程的ProcessId参数。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ProcessId | Integ er | Body | 否 | 1 | 流程ID。 |

| 灾备管理中心 |  |  |  | 同城容 | 灾管理平台开发指南·API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PlanName | Strin g | Body | 否 | test | 计划名。 |
| Execution Mode | Strin g | Body | 否 | MANUAL | 执行模式， |
| ProcessSt atus | Strin g | Body | 否 | EXECUTING | 流程状态。 |
| PageNum ber | Integ er | Body | 否 | 1 | 页码。 |
| PageSize | Integ er | Body | 否 | 10 | 每页条数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array | {} | 返回数据。 |
| -PgId | Integer | 1 | 保护组id |
| -PlanId | Integer | 1 | 演练计划ID. |
| -PlanName | String | test | 计划名称。 |
| -Zone | String | cn-wulan-env10- amtest10000-a | 可用区。 |
| -ProcessId | Integer | 5 | 流程id. |
| -ProcessType | String | DRILL RECOVERY _ | 流程类型。 |
| - ProtectionNam e | String | test | 保护组名。 |
| - ExecutionMod e | String | MANUAL | 执行模式。 |
| -ProcessStatus | String | EXECUTING | 流程状态 |
| -AccountId | String | 999999999 | 主账号id |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -CreateUid | String | 999999999 | 创建uid |
| -StartTime | Long | 1756112392000 | 开始时间。 |
| -EndTime | Long | 1756112392000 | 结束时间。 |
| -OrderId | Integer | 9 | 排序字段。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| Code | String | 200 | 状态码。 200：调用正常。 |
| Message | String | success | 返回信息。 |
| ErrorMessage | String | "" | 错误信息。 |
| ErrorCode | String | 500 | 错误码。 |
| Path | String | /xxx/ | 请求路径。 |
| Cost | Long | 1000 | 接口耗时，单位：毫秒（ms）。 |
| TotalCount | Integer | 100 | 列表条目数。 |
| PageNumber | Integer | 1 | 页码。 |
| PageSize | Integer | 10 | 每页行数。 |

**示例**

请求示例灾备管理中心

```
{ }
```

正常返回示例 `JSON` 格式

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

`XML` 格式灾备管理中心

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

该接口用于关闭流程,在保护组演练流程执行完之后关闭，或者在异常情况下提前关闭流程。 接口说明

## 准备工作

该接口用于关闭流程，需要提前获取流程的ProcessId。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ProcessId | Integ er | Body | 是 | 10 | 流程id |

灾备管理中心

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| IsForce | Boole an | Body | 是 | false | 是否强制关闭 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| Code | String | 200 | 状态码。 200：调用正常。 |
| Message | String | success | 返回信息。 |
| ErrorMessage | String | "" | 错误信息。 |
| ErrorCode | String | 500 | 错误码。 |
| Path | String | /xxx/ | 请求路径。 |
| Cost | Long | 20 | 接口耗时，单位：毫秒（ms）。 |
| Data | Struct | {} | 返回数据。 |
| -ProcessId | String | 10 | 流程id |
| -ProcessAction | String | SWITCH | 演练动作。 |
| -PlanId | Integer | 10 | 计划ID。 |
| -ProcessType | String | SWITCH | 流程类型。 |

**示例**

请求示例灾备管理中心

```json
{ "ProcessId":"10", "IsForce":"false" }
```

正常返回示例 `JSON` 格式

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

`XML` 格式

```xml
<Path>/xxx/</Path> <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data>
 <ProcessAction>SWITCH</ProcessAction>
 <ProcessType>SWITCH</ProcessType>
 <PlanId>10</PlanId>
 <ProcessId>10</ProcessId>
</Data> <ErrorCode>500</ErrorCode> <ErrorMessage>&quot;&quot;</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### CreateDrillProcess

该接口用于针对演练计划创建演练流程，开启流程后，可以进行保护组的切换动作。 接口说明

## 准备工作

该接口用于针对演练计划创建演练流程，使用前需要获取演练计划的 PlanId。 灾备管理中心

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PlanId | Integ er | Body | 是 | 10 | 计划ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| Code | String | 200 | 状态码。 200：调用正常。 |
| Message | String | success | 返回信息。 |
| ErrorMessage | String | "" | 错误信息。 |
| ErrorCode | String | 500 | 错误码。 |
| Path | String | /xxx/ | 请求路径。 |
| Cost | Long | 20 | 接口耗时，单位：毫秒（ms）。 |
| Data | Struct | {} | 返回数据。 |
| -ProcessId | String | 10 | 流程id |
| -ProcessAction | String | SWITCH CHECK _ | 流程类型 |

| 同城容灾管理平台开 | 发指南·API参考 |  | 灾备管理中心 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -PlanId | Integer | 4 | 计划id |
| -ProcessType | String | DRILL RECOVERY _ | 流程类型 |

**示例**

请求示例

```json
{ "PlanId":"10" }
```

正常返回示例 `JSON` 格式

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

`XML` 格式灾备管理中心

```xml
<Path>/xxx/</Path> <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data>
 <ProcessAction>SWITCH_CHECK</ProcessAction>
 <ProcessType>DRILL_RECOVERY</ProcessType>
 <PlanId>4</PlanId>
 <ProcessId>10</ProcessId>
</Data> <ErrorCode>500</ErrorCode> <ErrorMessage>&quot;&quot;</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### GetProcessTrace

该接口用于获取流程日志，主要用于获取保护组切换过程中的切换日志。 接口说明

## 准备工作

该接口用于获取流程日志，使用该接口前需要获取保护组切换的流程ProcessId和执行切换的接口中返回的的TraceId。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ProcessId | Integ er | Body | 是 | 10 | 流程id |
| TraceId | Strin g | Body | 是 | 1760325130967#rm- jp7lct7rd5l61b7t0#1#61 5E81E0-82CA-40C3- 8AC0-F002591EFC1C | 执行记录ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array | {} | 返回数据。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -TraceId | String | 9A506E30-DA33- 43D6-AACC- C3F85435D890 | 执行记录ID |
| -Product | String | RDS | 云产品。 |
| -ActionType | String | SWITCH | 动作类型。 |
| -StepName | String | dr service check | 步骤名称。 |
| -StepMsg | String | dr service status is good | 步骤信息。 |
| -GmtCreated | Long | 1760325133000 | 创建时间。 |
| -GmtModified | Long | 1760325133000 | 修改时间。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| Code | String | 200 | 状态码。 200：调用正常。 |
| Message | String | success | 返回信息。 |
| ErrorMessage | String | "" | 错误信息。 |
| ErrorCode | String | 500 | 错误码。 |
| Path | String | /xxx/ | 请求路径。 |
| Cost | Long | 20 | 接口耗时，单位：毫秒（ms）。 |

**示例**

请求示例灾备管理中心

```json
{ "ProcessId":"10", "TraceId":"1760325130967#rm-jp7lct7rd5l61b7t0#1#615E81E0-82CA-40C3-8AC0-F002591EFC1C" }
```

正常返回示例 `JSON` 格式

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

`XML` 格式

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

灾备管理中心

#### ExecuteProcess

该接口用于开始执行切换流程，主要用于保护组的切换和切回流程中，执行切换和切回的步骤。 接口说明

## 准备工作

该接口用于开始执行切换流程，使用该接口前需要提前获取ProcessId 和ProcessAction 参数信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ProcessId | Integ er | Body | 是 | 10 | 流程id |
| ProcessAc tion | Strin g | Body | 是 | SWITCH | 流程动作 |
| Step | Integ er | Body | 是 | 1 | 步骤号 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| Code | String | 200 | 状态码。 200：调用正常。 |
| Message | String | success | 返回信息。 |
| ErrorMessage | String | "" | 错误信息。 |
| ErrorCode | String | 500 | 错误码。 |

| 灾备管理中心 |  |  | 同城容灾管理平台开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Path | String | /xxx/ | 请求路径。 |
| Cost | Long | 20 | 接口耗时，单位：毫秒（ms）。 |

**示例**

请求示例

```json
{ "ProcessId":"10", "ProcessAction":"SWITCH", "Step":"1" }
```

正常返回示例 `JSON` 格式

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

`XML` 格式

```xml
<Path>/xxx/</Path> <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <ErrorCode>500</ErrorCode> <ErrorMessage>&quot;&quot;</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### CreateNextProcess

该接口用于演练流程进入下一个步骤。 接口说明

## 准备工作

该接口用于演练流程进入下一个步骤，调用该接口前需要获取ProcessId、ProcessAction 的信息。 灾备管理中心

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ProcessId | Integ er | Body | 是 | 10 | 流程id |
| ProcessAc tion | Strin g | Body | 是 | SWITCH | 流程动作类型 |
| IsForce | Boole an | Body | 是 | true | 是否强制 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| Code | String | 200 | 状态码。 200：调用正常。 |
| Message | String | success | 返回信息。 |
| ErrorMessage | String | "" | 错误信息。 |
| ErrorCode | String | 500 | 错误码。 |
| Path | String | /xxx/ | 请求路径。 |
| Cost | Long | 20 | 接口耗时，单位：毫秒（ms）。 |
| Data | Struct | {} | 返回数据。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -ProcessId | String | 10 | 流程id。 |
| -ProcessAction | String | SWITCH | 流程动作类型。 |
| - ProtectionGrou pId | Integer | 6 | 保护组id。 |

**示例**

请求示例

```json
{ "ProcessId":"10", "ProcessAction":"SWITCH", "IsForce":"true" }
```

正常返回示例 `JSON` 格式

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

`XML` 格式灾备管理中心

```xml
<Path>/xxx/</Path> <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data>
 <ProcessAction>SWITCH</ProcessAction>
 <ProtectionGroupId>6</ProtectionGroupId>
 <ProcessId>10</ProcessId>
</Data> <ErrorCode>500</ErrorCode> <ErrorMessage>&quot;&quot;</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### GetInstanceStatus

该接口用于获取实例状态信息，用于获取保护组的实例主节点位置和RPO 等信息。 接口说明

## 准备工作

该接口用于获取加入保护组实例的状态，需要提前获取演练流程的ProcessId 参数。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ProcessId | Integ er | Body | 是 | 10 | 流程id。 |
| ProcessAc tion | Strin g | Body | 是 | SWITCH | 流程类型。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |

|  | 灾备管理中心 |  |  | 同城容灾管理平台开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Code | String | 200 | 状态码。 200：调用正常。 |
| Message | String | success | 返回信息。 |
| ErrorMessage | String | "" | 错误信息。 |
| ErrorCode | String | 500 | 错误码。 |
| Path | String | /xxx/ | 请求路径。 |
| Cost | Long | 20 | 接口耗时，单位：毫秒（ms）。 |
| Data | Struct | {} | 返回数据。 |
| - PrevActionStat us | String | [] | 前序动作的状态 |
| - InstanceAction s | Array | [] | 实例状态列表. |
| --Id | Integer | 1 | 实例状态id |
| --ActionId | Integer | 10 | 动作id。 |
| -- ProcessAction | String | RECOVERY CHECK _ | 流程动作。 |
| --SourceIdc | String | amtest21 | 源机房。 |
| --DestIdc | String | amtest22 | 目的机房。 |
| --Step | Integer | 1 | 步骤序号。 |
| --InstanceId | String | rm- bp1162kryivb8**** | 实例ID。 |
| --InstanceAlias | String | test | 实例别称 |
| --Info | String | "" | 提示信息 |

| 同城容灾管理平台开 | 发指南·API参考 |  | 灾备管理中心 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --Product | String | RDS | 云产品 |
| --StartTime | Long | 1759211487000 | 开始时间。 |
| --EndTime | Long | 1759211487000 | 结束时间。 |
| --ActionStatus | String | INIT | 动作状态。 |
| --Result | String | “” | 返回结果。 |
| -- ConsumeTime | String | 120 | 耗时 |
| --TraceId | String | 9A506E30-DA33- 43D6-AACC- C3F85435D890 | 请求记录ID。 |
| -- MasterLocatio n | String | cn-wulan-env10- amtest10000-a | 主节点位置。 |
| --SyncDelay | String | { "value": "0", "status": true } | 延迟时间。 |
| --SyncStatus | String | { "value": "CheckInfo.Increas eReplica", "status": true } | 延迟状态。 |
| --FailoverType | Struct | {} | 切换类型。 |
| ---value | String | AUTOMATIC | 内容。 |
| ---info | String | AutomaticFailover | 提示信息。 |
| -ProcessStatus | String | FINISH | 流程状态。 |
| -ActionStatus | String | INIT | 动作状态。 |
| -StartTime | Long | 1759211487000 | 开始时间。 |
| -EndTime | Long | 1759211487000 | 结束时间。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -ConsumeTime | String | 120 | 执行耗时。 |
| -CurrentStep | Integer | 1 | 当前步骤。 |

**示例**

请求示例

```json
{ "ProcessId":"10", "ProcessAction":"SWITCH" }
```

正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "Path":"/xxx/",
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "Data":{
  "InstanceActions":[
   {
    "ProcessAction":"RECOVERY_CHECK",
    "SyncDelay":"{            \"value\": \"0\",            \"status\": true          }",
    "EndTime":1759211487000,
    "InstanceId":"rm-bp1162kryivb8****",
    "StartTime":1759211487000,
    "SyncStatus":"{            \"value\": \"CheckInfo.IncreaseReplica\",            \"st
atus\": true }",
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
    "Info":"\"\"",
    "DestIdc":"amtest22",
    "ActionStatus":"INIT",
    "Result":"“”",
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
 "ErrorMessage":"\"\"",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式灾备管理中心

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
    <Info>&quot;&quot;</Info>
    <DestIdc>amtest22</DestIdc>
    <ActionStatus>INIT</ActionStatus>
    <Result>“”</Result>
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
  <ErrorMessage>&quot;&quot;</ErrorMessage>
  <Code>200</Code>
  <Cost>20</Cost>
  <Success>true</Success>
```

#### GetProcessEntry

该接口用于获取演练流程步骤信息，包括实例状态，动作状态，流程步骤等。 灾备管理中心接口说明

## 准备工作

该接口用于获取演练流程步骤信息，使用该接口前需要获取演练计划的 PlanId 参数，可以使用

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PlanId | Integ er | Body | 是 | 10 | 计划ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| Code | String | 200 | 响应码。 |
| Message | String | success | 返回信息。 |
| ErrorMessage | String | "" | 错误信息。 |
| ErrorCode | String | 500 | 错误码。 |
| Path | String | /xxx/ | 请求路径。 |
| Cost | Long | 20 | 接口耗时，单位：毫秒（ms）。 |
| Data | Struct | {} | 返回数据。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - PrevActionStat us | String | [] | 前序动作的状态。 |
| - InstanceAction s | Array | [] | 实例信息列表。 |
| --Id | Integer | 1 | 实例状态id |
| --ActionId | Integer | 10 | 动作id。 |
| -- ProcessAction | String | SWITCH | 流程动作。 |
| --SourceIdc | String | amtest21 | 源机房。 |
| --DestIdc | String | amtest22 | 目的机房。 |
| --Step | Integer | 2 | 步骤序号。 |
| --InstanceId | String | rm-2ze8g2am9762 | 实例ID。 |
| --InstanceAlias | String | test | 实例别称 |
| --Product | String | RDS | 云产品 |
| --StartTime | Long | 1759211487000 | 开始时间。 |
| --EndTime | Long | 1759211487000 | 结束时间。 |
| --ActionStatus | String | INIT | 动作状态。 |
| --Result | String | “” | 返回结果。 |
| -- ConsumeTime | String | 120 | 耗时。 |
| --TraceId | String | 9A506E30-DA33- 43D6-AACC- C3F85435D890 | 请求记录ID。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- MasterLocatio n | String | cn-wulan-env10- amtest10000-a | 主节点位置。 |
| --SyncDelay | String | { "value": "0", "status": true } | 延迟时间。 |
| --SyncStatus | String | { "value": "CheckInfo.Increas eReplica", "status": true } | 延迟状态。 |
| -ProcessId | String | 1 | 流程ID |
| -ProcessType | String | DRILL RECOVERY _ | 流程类型。 |
| -ProcessAction | String | RECOVERY CHECK _ | 流程动作。 |
| - ExecutionMod e | String | MANUAL | 执行模式。 |
| -ActionStatus | String | NORMAL | 动作状态。 |
| -ActionUser | String | 999999999 | 执行动作的用户。 |
| -StartTime | Long | 1759211487000 | 开始时间。 |
| -EndTime | Long | 1759211487000 | 结束时间。 |
| - SwitchDirectio n | String | amtest21- >amtest22 | 切换方向。 |
| -Zone | String | cn-wulan-env128- amtest217002-b | 演练可用区。 |
| -ConsumeTime | String | 120 | 执行耗时。 |
| -ShowAction | String | RECOVERY CHECK _ | 页面显示的流程状态。 |
| -ProcessStatus | String | FINISH | 流程状态。 |
| -CurrentStep | String | 1 | 当前步骤。 |

| 灾备管理中心 |  |  | 同城容灾管理平台开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - ProtectionGrou pId | Integer | 16 | 保护组ID。 |
| -PlanId | Integer | 10 | 演练计划id |

**示例**

请求示例

```json
{ "PlanId":"10" }
```

正常返回示例 `JSON` 格式灾备管理中心

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
    "SyncDelay":"{            \"value\": \"0\",            \"status\": true          }",
    "EndTime":1759211487000,
    "InstanceId":"rm-2ze8g2am9762",
    "StartTime":1759211487000,
    "SyncStatus":"{            \"value\": \"CheckInfo.IncreaseReplica\",            \"st
atus\": true }",
    "Product":"RDS",
    "Step":2,
    "DestIdc":"amtest22",
    "ActionStatus":"INIT",
    "Result":"“”",
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
  "ShowAction":"\tRECOVERY_CHECK",
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
}
```

灾备管理中心 `XML` 格式

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
    <Result>“”</Result>
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
    <ProtectionGroupId>16</ProtectionGroupId>
    <SwitchDirection>amtest21-&gt;amtest22</SwitchDirection>
    <CurrentStep>1</CurrentStep>
    <ProcessId>1</ProcessId>
    <ConsumeTime>120</ConsumeTime>
   </Data>
   <ErrorCode>500</ErrorCode>
   <ErrorMessage>&quot;&quot;</ErrorMessage>
   <Code>200</Code>
t20/C
```

t 灾备管理中心

```xml
   <Cost>20</Cost>
   <Success>true</Success>
```

#### CreateDisasterRecoveryProcess

该接口用于创建故障恢复流程。 接口说明

## 准备工作

该接口用于创建故障恢复流程，用于创建保护组后开始故障场景的保护组流程。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /api/pop/v1/createDisasterRecoveryProcess HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PlanId | Integ er | Body | 是 | 10 | 计划ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| Code | String | 200 | 状态码。 200：调用正常。 |
| Message | String | success | 返回信息。 |
| ErrorMessage | String | "" | 错误信息。 |
| ErrorCode | String | 500 | 错误码。 |
| Path | String | /xxx/ | 请求路径。 |

|  | 灾备管理中心 |  |  | 同城容灾管理平台开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Cost | Long | 20 | 接口耗时，单位：毫秒（ms）。 |
| Data | Struct | {} | 返回数据。 |
| -ProcessId | String | 16 | 流程ID |
| -ProcessAction | String | SWITCH | 流程动作。 |
| -PlanId | Integer | 18 | 故障恢复计划ID。 |
| -ProcessType | String | DRILL RECOVER _ | 流程类型。 |

**示例**

请求示例

```json
POST /api/pop/v1/createDisasterRecoveryProcess HTTP/1.1 { "PlanId":"10" }
```

正常返回示例 `JSON` 格式

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

`XML` 格式灾备管理中心

```xml
<Path>/xxx/</Path> <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data>
 <ProcessAction>SWITCH</ProcessAction>
 <ProcessType>DRILL_RECOVER</ProcessType>
 <PlanId>18</PlanId>
 <ProcessId>16</ProcessId>
</Data> <ErrorCode>500</ErrorCode> <ErrorMessage>&quot;&quot;</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### CreateHdrReverse

该接口用于对HDR 保护组切换。 接口说明

## 准备工作

该接口用于进行HDR保护组的切换，切换前需要获取HDR保护组的演练流程信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ProcessId | Integ er | Body | 是 | 10 | 流程id。 |
| Product | Strin g | Body | 是 | HDR | 产品名 |
| InstanceId | Strin g | Body | 是 | "xxxx" | 实例名 |
| RecoverOr iginal | Boole an | Body | 是 | true | 恢复到原主机。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| Code | String | 200 | 状态码。 200：调用正常。 |
| Message | String | success | 返回信息。 |
| ErrorMessage | String | "" | 错误信息。 |
| ErrorCode | String | 500 | 错误码。 |
| Path | String | /xxx/xxx | 请求路径。 |
| Cost | Long | 20 | 接口耗时，单位：毫秒（ms）。 |

**示例**

请求示例

```json
{ "ProcessId":"10", "Product":"HDR", "InstanceId":""xxxx"", "RecoverOriginal":"true" }
```

正常返回示例 `JSON` 格式

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

灾备管理中心 `XML` 格式

```xml
<Path>/xxx/xxx</Path> <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <ErrorCode>500</ErrorCode> <ErrorMessage>&quot;&quot;</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### GetDrillPlan

该接口用于获取演练计划的详细信息，包括演练计划涉及的产品、实例和可用区信息等。 接口说明

## 准备工作

该接口需要传入PlanId 参数，使用该接口前可以根据ListDrillPlan接口获取演练计划信息列表，从中得到需要获取详细信息的的PlanId 。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PlanId | Integ er | Body | 是 | 10 | 计划ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| Code | String | 200 | 状态码。 200：调用正常。 |
| Message | String | success | 返回信息。 |

| 灾备管理中心 |  |  | 同城容灾管理平台开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ErrorMessage | String | "" | 错误信息。 |
| ErrorCode | String | 500 | 错误码。 |
| Path | String | /xxx/xxx | 请求路径。 |
| Cost | Long | 20 | 接口耗时，单位：毫秒（ms）。 |
| Data | Struct | {} | 返回数据。 |
| -PlanItems | Array | [] | 恢复步骤 |
| --InstanceId | String | rm- bp1162kryivb8**** | 实例ID。 |
| --InstanceAlias | String | test | 实例别名。 |
| --Step | Integer | 1 | 步骤。 |
| --Product | String | RDS | 云产品。 |
| --Info | String | {} | 提示信息。 |
| --Impacts | String | "product.drill.effect .RDS" | 切换影响。 |
| --FailoverType | Struct | {} | 切换类型。 |
| ---value | String | "NONEED" | 内容。 |
| ---info | String | "InstancePrimaryZ oneMissMatch" | 提示信息。 |
| -Id | Integer | 10 | 计划ID。 |
| -PlanName | String | name | 演练计划名 |
| - ProtectionGrou pId | Integer | 10 | 保护组id |

| 同城容灾管理平台开 | 发指南·API参考 |  | 灾备管理中心 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - ProtectionGrou pName | String | test | 保护组名 |
| -Description | String | testDescription | 描述。 |
| - ExecutionMod e | String | MANUAL | 执行模式。 |
| -Zone | String | cn-wulan-env10- amtest10000-a | 可用区。 |
| -GmtCreate | Long | 1756110161000 | 创建时间。 |
| -GmtModified | Long | 1756110161000 | 修改时间。 |
| -LastTime | Long | 1756110161000 | 上次操作时间。 |
| - InPlanInstance Count | Integer | 10 | 计划中包含的实例数。 |
| - NotInPlanInsta nceCount | Integer | 10 | 计划中不包含的实例数。 |
| -ExecuteCount | Integer | 10 | 执行次数。 |
| - RunningProces sId | Integer | 10 | 正在执行的流程id。 |

**示例**

请求示例

```json
{ "PlanId":"10" }
```

正常返回示例 `JSON` 格式灾备管理中心

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

`XML` 格式灾备管理中心

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
 <ProtectionGroupId>10</ProtectionGroupId>
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

该接口用于列出当前的演练计划，支持按照计划名称单独查询，查询结果包括演练计划的执行模式、演练可用区场景等信息。 接口说明

## 准备工作

<接口使用的前置动作>

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

灾备管理中心

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PlanId | Integ er | Body | 否 | 1 | 演练计划ID |
| PlanName | Strin g | Body | 否 | test | 演练计划名称。 |
| Execution Mode | Strin g | Body | 否 | MANUAL | 执行模式。 |
| PageNum ber | Integ er | Body | 否 | 1 | 分页查询页码。 |
| PageSize | Integ er | Body | 否 | 100 | 分页查询大小。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array | [] | 返回数据。 |
| -PlanId | Integer | 1 | 计划ID。 |
| -PlanName | String | test | 计划名称。 |
| - ProtectionGrou pId | Integer | 2 | 保护组ID。 |
| - ProtectionGrou pName | String | test | 保护组名称。 |
| -Description | String | test dr | 描述 |
| - ExecutionMod e | String | MANUAL | 执行模式。 |
| -Zone | String | cn-wulan-env10- amtest10000-a | 可用区。 |
| -GmtCreate | Long | 1759211487000 | 创建时间。 |
| -GmtModified | Long | 1759211487000 | 修改时间。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - RunningProces sId | Integer | 16 | 运行中的流程id。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| Code | String | 200 | 状态码。 200：调用正常。 |
| Message | String | success | 返回信息。 |
| ErrorMessage | String | "" | 错误信息。 |
| ErrorCode | String | 500 | 错误码。 |
| Path | String | /xxx/xxx | 请求路径。 |
| Cost | Long | 20 | 接口耗时，单位：毫秒（ms）。 |
| TotalCount | Integer | 100 | 总记录数。 |
| PageNumber | Integer | 1 | 当前页码。 |
| PageSize | Integer | 10 | 分页大小。 |

**示例**

请求示例

```
{ }
```

正常返回示例 `JSON` 格式灾备管理中心

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

`XML` 格式灾备管理中心

```xml
<Code>200</Code> <Data>
 <Item>
  <ExecutionMode>MANUAL</ExecutionMode>
  <GmtCreate>1759992973000</GmtCreate>
  <GmtModified>1759992973000</GmtModified>
  <PlanId>6</PlanId>
  <PlanName>test</PlanName>
  <ProtectionGroupId>4</ProtectionGroupId>
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
  <ProtectionGroupId>3</ProtectionGroupId>
  <ProtectionGroupName>bcmctest</ProtectionGroupName>
  <Zone>cn-wulan-env128-amtest128001-a</Zone>
 </Item>
 <Item>
  <ExecutionMode>MANUAL</ExecutionMode>
  <GmtCreate>1757578962000</GmtCreate>
  <GmtModified>1757578962000</GmtModified>
  <PlanId>3</PlanId>
  <PlanName>es</PlanName>
  <ProtectionGroupId>2</ProtectionGroupId>
  <ProtectionGroupName>es-ab</ProtectionGroupName>
  <RunningProcessId>3</RunningProcessId>
  <Zone>cn-wulan-env128-amtest128001-a</Zone>
 </Item>
</Data> <Message>success</Message> <PageNumber>1</PageNumber> <PageSize>10</PageSize> <RequestId>AB3E6FFC-6467-4804-832C-E05E7C14D7A8</RequestId> <Success>true</Success> <TotalCount>3</TotalCount>
```

#### GetProcessCheck

该接口用于获取流程执行检查结果，用于在切换前检查实例的状态，包含同步延迟、主节点位置、是否涉及演练动作等信息。 接口说明

## 准备工作

调用该接口前，请确认演练计划流程存在，建议使用ListProcesses在流程信息列表结果中获取 ProcessId。 灾备管理中心

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ProcessId | Integ er | Body | 是 | 10 | 演练流程ID。 |
| ProcessAc tion | Strin g | Body | 是 | SWITCH | 流程动作类型。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| Code | String | 200 | 状态码。 200：调用正常。 |
| Message | String | success | 返回信息。 |
| ErrorMessage | String | "" | 错误信息。 |
| ErrorCode | String | 500 | 错误码。 |
| Path | String | /xxx/ | 请求路径。 |
| Cost | Long | 20 | 接口耗时，单位：毫秒（ms）。 |
| Data | Struct | {} | 返回数据。 |
| - PrevActionStat us | String | [] | 前序动作的状态。 |

| 同城容灾管理平台开 | 发指南·API参考 |  | 灾备管理中心 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - InstanceAction s | Array | [] | 实例信息列表。 |
| --ZoneInfo | String | cn-wulan-env10- amtest10000-a | 可用区信息。 |
| --Id | Integer | 18 | 实例状态id。 |
| --ActionId | Integer | 16 | 动作id。 |
| -- ProcessAction | String | SWITCH CHECK _ | 流程动作。 |
| --SourceIdc | String | amtest21 | 源机房。 |
| --DestIdc | String | amtest22 | 目的机房。 |
| --Step | Integer | 1 | 步骤序号。 |
| --InstanceId | String | rm- 2ze8g2am97624** ** | 实例ID。 |
| --InstanceAlias | String | test | 实例别名。 |
| --Info | String | "" | 提示信息。 |
| --Product | String | RDS | 云产品。 |
| --StartTime | Long | 1628265600000 | 开始时间。 |
| --EndTime | Long | 1628265600000 | 结束时间。 |
| --ActionStatus | String | INIT | 动作状态。 |
| --Result | String | “” | 返回结果。 |
| -- ConsumeTime | String | 120 | 耗时 |
| --TraceId | String | 9A506E30-DA33- 43D6-AACC- C3F85435D890 | 请求记录ID。 |

| 灾备管理中心 |  |  | 同城容灾管理平台开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- MasterLocatio n | String | cn-wulan-env10- amtest10000-a | 主节点位置。 |
| --SyncDelay | String | { "value": "0", "status": true } | 延迟时间。 |
| --SyncStatus | String | { "value": "CheckInfo.Increas eReplica", "status": true } | 延迟状态。 |
| --FailoverType | Struct | {} | 切换类型。 |
| ---value | String | AUTOMATIC | 内容。 |
| ---info | String | AutomaticFailover | 提示信息。 |
| -ProcessStatus | String | FINISH | 流程状态。 |
| -ActionStatus | String | NORMAL | 动作状态。 |
| -StartTime | Long | 1759211487000 | 开始时间。 |
| -EndTime | Long | 1759211487000 | 结束时间。 |
| -ConsumeTime | String | 120 | 执行耗时。 |
| -CurrentStep | Integer | 1 | 当前步骤。 |

**示例**

请求示例

```json
{ "ProcessId":"10", "ProcessAction":"SWITCH" }
```

正常返回示例 `JSON` 格式

```json
{
  "Code": "200",
  "Data": {
```

灾备管理中心

```json
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
          "InstanceAlias": "rds-mysql80-经典",
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
          "DestIdc": "amtest217",
          "EndTime": 1760323989000,
          "FailoverType": {
```

灾备管理中心

```json
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
}
```

灾备管理中心 `XML` 格式

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
   <InstanceAlias>rds-mysql80-经典</InstanceAlias>
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
   <DestIdc>amtest217</DestIdc>
   <EndTime>1760323989000</EndTime>
Fil
```

T 灾备管理中心

```xml
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
 <StartTime>1760323989000</StartTime>
</Data> <Message>success</Message>
```

灾备管理中心

```xml
<Message>success</Message> <RequestId>4F19DE7F-67E5-4F6C-AA06-75CBB5DC7C65</RequestId> <Success>true</Success>
```

#### GetPrevProcess

该接口用于获取前一个流程状态，用于获取演练计划上一步的信息，该接口仅获取上一步信息，并不会改变演练计划流程的实际状态。 接口说明

## 准备工作

调用该接口前，请确认演练计划流程存在，建议使用ListProcesses在流程信息列表结果中获取 ProcessId。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ProcessId | Integ er | Body | 是 | 10 | 演练流程ID。 |
| ProcessAc tion | Strin g | Body | 是 | SWITCH | 流程动作类型。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| Code | String | 200 | 状态码。 200：调用正常。 |
| Message | String | success | 返回信息。 |
| ErrorMessage | String | "" | 错误信息。 |

| 灾备管理中心 |  |  | 同城容灾管理平台开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ErrorCode | String | 500 | 错误码。 |
| Path | String | /xxx/xxx | 请求路径。 |
| Cost | Long | 20 | 接口耗时，单位：毫秒（ms）。 |
| Data | Struct | {} | 返回数据。 |
| - PrevActionStat us | String | [] | 前序动作的状态。 |
| - InstanceAction s | Array | [] | 实例信息列表。 |
| --ZoneInfo | String | cn-wulan-env10- amtest10000-a | 可用区信息。 |
| --Id | Integer | 18 | 实例状态id。 |
| --ActionId | Integer | 16 | 动作id。 |
| -- ProcessAction | String | 流程动作 | 流程动作。 |
| --SourceIdc | String | amtest21 | 源机房。 |
| --DestIdc | String | amtest22 | 目的机房。 |
| --Step | Integer | 1 | 步骤序号。 |
| --InstanceId | String | rm- 2ze8g2am97624** ** | 实例ID。 |
| --InstanceAlias | String | test | 实例别名。 |
| --Product | String | RDS | 云产品。 |
| --StartTime | Long | 1628265600000 | 开始时间。 |
| --EndTime | Long | 1628265600000 | 结束时间。 |

| 同城容灾管理平台开 | 发指南·API参考 |  | 灾备管理中心 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --ActionStatus | String | INIT | 动作状态。 |
| --Result | String | “” | 返回结果。 |
| -- ConsumeTime | String | 120 | 耗时 |
| --TraceId | String | 9A506E30-DA33- 43D6-AACC- C3F85435D890 | 请求记录ID。 |
| -- MasterLocatio n | String | cn-wulan-env10- amtest10000-a | 主节点位置。 |
| --SyncDelay | String | { "value": "0", "status": true } | 延迟时间。 |
| --SyncStatus | String | { "value": "CheckInfo.Increas eReplica", "status": true } | 延迟状态。 |
| --FailoverType | Struct | {} | 切换类型。 |
| ---value | String | AUTOMATIC | 内容。 |
| ---info | String | AutomaticFailover | 提示信息。 |
| -ProcessId | String | 4 | 流程ID。 |
| -ProcessType | String | DRILL RECOVERY _ | 流程类型。 |
| -ProcessAction | String | RECOVERY CHECK _ | 流程动作。 |
| - ExecutionMod e | String | MANUAL | 执行模式。 |
| -ActionStatus | String | NORMAL | 动作状态。 |
| -ActionUser | String | 999999999 | 执行动作的用户。 |
| -StartTime | Long | 1759211487000 | 开始时间。 |

| 灾备管理中心 |  |  | 同城容灾管理平台开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -EndTime | Long | 1759211487000 | 结束时间。 |
| - SwitchDirectio n | String | amtest21- >amtest22 | 切换方向。 |
| -ConsumeTime | String | 120 | 执行耗时。 |
| -ShowAction | String | RECOVERY CHECK _ | 页面显示的流程状态。 |
| -ProcessStatus | String | FINISH | 流程状态。 |
| -CurrentStep | String | 1 | 当前步骤。 |
| - ProtectionGrou pId | Integer | 20 | 保护组ID。 |
| -PlanId | Integer | 16 | 演练计划id |
| -Zone | String | cn-wulan-env128- amtest217002-b | 演练可用区。 |

**示例**

请求示例

```json
{ "ProcessId":"10", "ProcessAction":"SWITCH" }
```

正常返回示例 `JSON` 格式

```json
{
  "Code": "200",
  "Data": {
    "ActionStatus": "SUCCESS",
    "ActionUser": "1933655883841513",
    "ConsumeTime": "0",
    "CurrentStep": 1,
    "EndTime": 1760324734000,
    "ExecutionMode": "MANUAL",
    "InstanceActions": {
      "InstanceAction": [
        {
```

灾备管理中心

```json
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
          "InstanceAlias": "rds-mysql57-经典",
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

]

```json
    },
    "ProcessAction": "SWITCH",
    "ProcessId": 6,
    "ProcessStatus": "EXECUTING",
    "ProcessType": "DRILL_RECOVERY",
    "ProtectionGroupId": 4,
    "ShowAction": "SWITCH_CHECK",
```

灾备管理中心

```json
    "StartTime": 1760324734000,
    "SwitchDirection": "amtest128->amtest217",
    "Zone": "cn-wulan-env128-amtest217002-b"
  },
  "Message": "success",
  "RequestId": "DC9C8651-9890-423E-8056-8E81F0B95FEE",
  "Success": true
}
```

`XML` 格式

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
   <InstanceAlias>rds-mysql57-经典</InstanceAlias>
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
   </SyncDelay>
   <SyncStatus>
    <value>CheckInfo.IncreaseReplica</value>
    <status>true</status>
   </SyncStatus>
   <TraceId>1760324733966#rm-jp7lct7rd5l61b7t0#1#AD59B157-3B17-4C4B-A0BE-
2A7772BABAD7</TraceId>
   <ZoneInfo>
```

灾备管理中心

```xml
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
 <ProtectionGroupId>4</ProtectionGroupId>
 <ShowAction>SWITCH_CHECK</ShowAction>
 <StartTime>1760324734000</StartTime>
 <SwitchDirection>amtest128-&gt;amtest217</SwitchDirection>
 <Zone>cn-wulan-env128-amtest217002-b</Zone>
</Data> <Message>success</Message> <RequestId>DC9C8651-9890-423E-8056-8E81F0B95FEE</RequestId> <Success>true</Success>
```

#### GetProcessDetail

该接口用于获取流程细节信息，包括演练计划涉及的产品、示例、切换方向、当前执行步骤、前序动作的状态。 接口说明

## 准备工作

调用该接口前，请确认演练计划流程存在，使用CreateProcess创建演练流程获取ProcessId，或者使用

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ProcessId | Integ er | Body | 是 | 10 | 流程id |

|  | 灾备管理中心 |  |  |  | 同城容 | 灾管理平台开发指南·API参考 |  |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ProcessAc tion | Strin g | Body | 否 | SWITCH | 流程动作类型 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| Code | String | 200 | 状态码。 200：调用正常。 |
| Message | String | success | 返回信息。 |
| ErrorMessage | String | "" | 错误信息。 |
| ErrorCode | String | 500 | 错误码。 |
| Path | String | /xxx/xxx | 请求路径。 |
| Cost | Long | 20 | 接口耗时，单位：毫秒（ms）。 |
| Data | Struct | {} | 返回数据。 |
| - PrevActionStat us | String | [] | 前序动作的状态。 |
| - InstanceAction s | Array | [] | 实例状态列表。 |
| --Id | Integer | 18 | 实例id。 |
| --ActionId | Integer | 12 | 任务id。 |
| -- ProcessAction | String | SWITCH | 流程动作。 |

| 同城容灾管理平台开 | 发指南·API参考 |  | 灾备管理中心 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --SourceIdc | String | amtest12 | 源机房。 |
| --DestIdc | String | amtest22 | 目的机房。 |
| --Step | Integer | 1 | 步骤号。 |
| --InstanceId | String | rm- 2ze8g2am97624** ** | 实例ID。 |
| --InstanceAlias | String | test | 实例别名。 |
| --Product | String | RDS | 产品。 |
| --StartTime | Long | 1628265600000 | 开始时间。 |
| --EndTime | Long | 1628265600000 | 结束时间。 |
| --ActionStatus | String | INIT | 动作状态。 |
| --Result | String | "" | 返回结果。 |
| -- ConsumeTime | String | 20 | 耗时。 |
| --TraceId | String | 9A506E30-DA33- 43D6-AACC- C3F85435D890 | 执行记录id。 |
| -- MasterLocatio n | String | cn-hangzhou-a | 主节点位置。 |
| --SyncDelay | String | { "value": "0", "status": true } | 延迟时间。 |
| --SyncStatus | String | { "value": "CheckInfo.Increas eReplica", "status": true } | 延迟状态 |
| --FailoverType | Struct | {} | 切换类型。 |
| ---value | String | AUTOMATIC | 内容。 |

| 灾备管理中心 |  |  | 同城容灾管理平台开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---info | String | AutomaticFailover | 提示信息。 |
| -ProcessId | String | 4 | 流程id。 |
| -ProcessType | String | DRILL RECOVERY _ | 流程类型。 |
| -ProcessAction | String | RECOVERY CHECK _ | 流程动作。 |
| - ExecutionMod e | String | MANUAL | 执行模式。 |
| -ActionStatus | String | NORMAL | 动作状态。 |
| -ActionUser | String | 999999999 | 执行动作的用户。 |
| -StartTime | Long | 1759211487000 | 开始时间。 |
| -EndTime | Long | 1759211487000 | 结束时间。 |
| - SwitchDirectio n | String | amtest21- >amtest22 | 切换方向。 |
| -ConsumeTime | String | 20 | 执行耗时。 |
| -ShowAction | String | RECOVERY CHECK _ | 页面显示的流程状态。 |
| -ProcessStatus | String | FINISH | 流程状态。 |
| -CurrentStep | String | 1 | 当前步骤。 |
| - ProtectionGrou pId | Integer | 10 | 保护组ID。 |
| -PlanId | Integer | 16 | 演练计划id |
| -Zone | String | cn-hangzhou-a | 演练可用区。 |

**示例**

灾备管理中心请求示例

```json
{ "ProcessId":"10" }
```

正常返回示例 `JSON` 格式

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
          "InstanceAlias": "rds-mysql80-经典",
          "InstanceId": "rm-jp7r3459uq299j520",
          "MasterLocation": {
            "value": "cn-wulan-env128-amtest128001-a",
            "status": true
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
```

灾备管理中心

```json
C16CF72D81C2
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
```

灾备管理中心 ,

```json
    "SwitchDirection": "amtest217->amtest128",
    "Zone": "cn-wulan-env128-amtest128001-a"
  },
  "Message": "success",
  "RequestId": "FD418663-E79E-4196-AB7A-36922FC2D572",
  "Success": true
}
```

`XML` 格式

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
   <InstanceAlias>rds-mysql80-经典</InstanceAlias>
   <InstanceId>rm-jp7r3459uq299j520</InstanceId>
   <MasterLocation>
    <value>cn-wulan-env128-amtest128001-a</value>
    <status>true</status>
   </MasterLocation>
   <ProcessAction>RECOVERY_CHECK</ProcessAction>
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
```

灾备管理中心

```xml
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
```

灾备管理中心

```xml
 ProcessId4/ProcessId
 <ProcessStatus>FINISH</ProcessStatus>
 <ProcessType>DRILL_RECOVERY</ProcessType>
 <ProtectionGroupId>3</ProtectionGroupId>
 <ShowAction>RECOVERY_CHECK</ShowAction>
 <StartTime>1759211487000</StartTime>
 <SwitchDirection>amtest217-&gt;amtest128</SwitchDirection>
 <Zone>cn-wulan-env128-amtest128001-a</Zone>
</Data> <Message>success</Message> <RequestId>FD418663-E79E-4196-AB7A-36922FC2D572</RequestId> <Success>true</Success>
```

#### SwitchInstance

该接口用于保护组切换步骤中重试切换容灾实例，按照演练计划的演练场景，进行实例的切换和切回。 接口说明

## 准备工作

执行该API前，建议根据 GetProcessDetail 接口获取ProcessId 和ProcessAction 的信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ProcessId | Integ er | Body | 是 | 10 | 流程id |
| ProcessAc tion | Strin g | Body | 是 | SWITCH | 流程动作类型 |
| InstanceId s | Strin g | Body | 是 | rm-hg30ps8hg9vtcqf71r | 实例id |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| Code | String | 200 | 状态码。 200：调用正常。 |
| Message | String | success | 返回信息。 |
| ErrorMessage | String | "" | 错误信息。 |
| ErrorCode | String | 500 | 错误码。 |
| Path | String | /xx/xx | 请求路径。 |
| Cost | Long | 20 | 接口耗时，单位：毫秒（ms）。 |

**示例**

请求示例

```json
{ "ProcessId":"10", "ProcessAction":"SWITCH", "InstanceIds":"rm-hg30ps8hg9vtcqf71r" }
```

正常返回示例 `JSON` 格式

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

`XML` 格式灾备管理中心

```xml
<Path>/xx/xx</Path> <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <ErrorCode>500</ErrorCode> <ErrorMessage>&quot;&quot;</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### SetProcessSwitchStep

本API用于在保护组手动批次切换的场景下，手动跳过失败的切换批次，进行下一批次的切换动作。 接口说明

## 准备工作

执行该API前，建议根据 GetProcessDetail 接口获取ProcessId 和ProcessAction 的信息，同时确认当前失败的切换步骤批次。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ProcessId | Integ er | Body | 是 | 22 | 流程id |
| ProcessAc tion | Strin g | Body | 是 | SWITCH | 流程动作类型 |
| Step | Integ er | Body | 是 | 2 | 步骤 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Code | String | 200 | 状态码。 200：调用正常。 |
| Message | String | success | 返回信息。 |
| ErrorMessage | String | "" | 错误信息。 |
| ErrorCode | String | 500 | 错误码。 |
| Path | String | /xxx/xxx | 请求路径。 |
| Cost | Long | 20 | 接口耗时，单位：毫秒（ms）。 |
| Data | Integer | 2 | 返回数据。 |

**示例**

请求示例

```json
{ "ProcessId":"22", "ProcessAction":"SWITCH", "Step":"2" }
```

正常返回示例 `JSON` 格式

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

`XML` 格式灾备管理中心

```xml
<Path>/xxx/xxx</Path> <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data>2</Data> <ErrorCode>500</ErrorCode> <ErrorMessage>&quot;&quot;</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```
