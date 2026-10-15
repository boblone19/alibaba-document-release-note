---
title: "资源编排 用户指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 412
source_pdf: "05_用户指南_enterprise-ascm-user-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/ros/zh/enterprise-ascm-user-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 资源编排 用户指南

资源编排

## 什么是资源编排服务

资源编排服务ROS（Resource Orchestration Service）是阿里云提供的一项简化云计算资源管理的服务。您可以遵循 ROS定义的模板规范编写资源栈模板，在模板中定义所需的云计算资源（例如：ECS实例、RDS数据库实例）、资源间的依赖关系等。ROS的编排引擎将根据模板自动完成所有资源的创建和配置，实现自动化部署及运维。 ROS模板是可读、易编写的文本文件。您可以直接编辑JSON格式文本，或者通过SVN、Git等版本控制工具控制模板的版本，以达到控制基础设施版本的目的。您可以通过API、SDK等方式将ROS的编排能力与自己的应用进行整合，实现基础设施即代码（Infrastructure as Code）。 ROS模板也是一种标准化的资源和应用交付方式。如果您是独立软件供应商（ISV），则可以通过ROS模板交付包含云资源和应用的整体系统和解决方案。ISV可以通过这种交付方式，整合阿里云的资源和ISV的软件系统，实现统一交付。 ROS通过资源栈（Stack）统一管理一组云资源（一个资源栈即为一组阿里云资源）。对于云资源的创建、删除、重新创建等操作，都可以以资源栈为单位来完成。 资源编排

## 登录资源编排控制台

**前提条件**

登录Apsara Uni-manager运营控制台前，确认您已从部署人员处获取Apsara Uni-manager运营控制台的服务域名地址。 推荐使用Chrome浏览器。

**操作步骤**

1. 在浏览器地址栏中，输入Apsara Uni-manager运营控制台的服务域名地址，按回车键。

**说明**

单击页面右上角的当前语言可以切换其它语言。 由于浏览器证书过期或环境开启HTTPS认证等出现多次单击继续访问或无Apsara Uni-manager运营控制台地址入口等现象，此时需要安装证书才能正常访问。单击页面右上角的**浏览器证书安装**，可打开浏览器证书安装指南。
2. 输入正确的用户名及密码。
资源编排

**说明**

请向运营管理员获取登录控制台的用户名和密码。 首次登录Apsara Uni-manager运营控制台时，需要修改登录用户名的密码，请按照提示完成密码修改。为提高安全性，密码长度必须为10~32位，且包含英文字母大小写、阿拉伯数字和特殊符号（感叹号（!）、 at（@）、井号（#）、美元符号（$）、百分号（%）等）。
3. 勾选**我已阅读并同意产品服务协议、隐私协议、用户协议**。

**说明**

登录页展示的链接文字为文档标题，单击链接文字，可查看协议的详细内容。
**产品服务协议**、**隐私协议**和**用户协议**仅在已发布时才会显示。如果三种类型协议都没有发布，则不需要执行该
操作。
4. 单击**账号登录**/**授权登录**。

**说明**

“授权登录”仅第三方认证的全局IdP设置启用时才会显示，且该显示名称可自定义，默认显示名称为“授权登录”。
5. 如果账号已激活MFA多因素认证，请根据以下两种情况进行操作：

**说明**

公网场景下，登录入口默认强制开启多因素认证。

**开启MFA后的首次登录**

a. 输入账号密码登录后，展示绑定虚拟MFA设备页面。 b. 在绑定虚拟MFA设备页面中，按页面提示步骤绑定虚拟MFA设备。 c. 登录成功，进入控制台。

**已开启并绑定MFA**

输入6位MFA码后单击**认证**。
6. 在页面顶部导航栏，选择**产品** > **开发工具** > **资源编排****ROS**。
资源编排

## 管理资源栈

### 创建资源栈

资源编排服务ROS（Resource Orchestration Service）可以通过创建资源栈来管理一组资源。本文为您介绍创建资源栈的两种方式。
1. 登录资源编排控制台。
2. 在左侧导航栏，单击**资源栈**。
3. 在**资源栈**页面，单击**创建资源栈**。
4. 在**选择模板**页面，选择**组织**、**资源集**和**区域**。
5. 选择模板录入方式，设置模板，然后单击**下一步**。
**输入模板**：在**准备模板**区域输入JSON格式的模板。
**我的模板**：选择已创建的模板。关于如何创建模板，请参见创建模板。
6. 在**配置模板参数**页面，输入资源栈名称和参数，然后单击**下一步**。

**说明**

根据模板的不同，您需要输入的参数将有所差异，请根据控制台提示输入参数信息。 您也可以单击**预览**，查看待创建的资源名称、资源类型和资源属性等信息。
7. 在**配置资源栈**页面，设置是否启用失败时回滚，并设置超时的时间，然后单击**下一步**。
8. 在**确认信息**页面，确认资源栈相关信息无误后，单击**提交**。
创建资源栈成功后，资源栈**状态**列显示**创建成功**。此时您可以单击资源栈ID，查询资源栈基础信息（例如：资源栈名称、 ID和创建时间）、事件、资源、输出、参数和模板等信息。 如果您已经创建了模板，可以通过以下方式快速创建资源栈。关于如何创建模板，请参见创建模板。
1. 登录资源编排控制台。
2. 在左侧导航栏，单击**我的模板**。
3. 在**我的模板**页面，单击目标模板右侧**操作**列的**创建栈**。
4. 在**选择模板**页面，选择**组织**、**资源集**和**区域**，然后单击**下一步**。
5. 在**配置模板参数**页面，输入资源栈名称和参数，然后单击**下一步**。
6. 在**配置资源栈**页面，设置是否启用失败时回滚，并设置超时的时间，然后单击**下一步**。
7. 在**确认信息**页面，确认资源栈相关信息无误后，单击**提交**。
创建资源栈成功后，资源栈**状态**列显示**创建成功**。此时您可以单击资源栈ID，查询资源栈基础信息（例如：资源栈名称、 ID和创建时间）、事件、资源、输出、参数和模板等信息。

### 查看资源栈

**前提条件**

**操作步骤**

1. 登录资源编排控制台。
2. 在左侧导航栏，单击**资源栈**。
3. 在**资源栈**页面，单击目标资源栈ID。
您可以通过**资源栈名称**、**资源栈****ID**和**标签**筛选获取目标资源栈。 资源编排在资源栈详情页面，您可以执行以下操作： 单击**参数**页签，查看创建资源栈时模板中指定的参数包括ROS提供的以ALIYUN::开始的伪参数。 单击**操作日志**页签，查看资源栈被用户访问以及使用行为，便于对历史操作进行分析和回溯。 您可以按**操作名称**、**操作人**、**执行状态**等过滤条件进一步筛查出关心的操作记录，支持的过滤条件如下表所示。

| 过滤条件 | 说明 |
|---|---|
| 操作人 | 输入执行变更操作的操作者。 |
| 操作名称 | 选择资源栈的变更操作名称，即API名称。 |
| 执行状态 | 选择执行状态为成功或失败。 |
| 操作源IP | 输入操作源IP。 |
| 操作时间 | 选择需要查看的时间范围。 |

**可选：**在目标操作记录的**操作**列，单击**操作详情**，可查看**基本信息**以及**API****调用详情**。

### 更新资源栈

当您只需要修改资源栈模板或资源栈配置，但不需要修改资源栈归属（包括组织、资源集和地域）时，可以选择更新资源资源编排

**前提条件**

**操作步骤**

1. 登录资源编排控制台。
2. 在左侧导航栏，单击**资源栈**。
3. 在**资源栈**页面，单击目标资源栈右侧**操作**列的**更新**。
4. 在**选择模板**页面，选择模板录入方式，更新模板，然后单击**下一步**。
**输入模板**：在**准备模板**区域输入更新后的JSON格式模板。
**我的模板**：选择已创建的模板。
5. 在**配置模板参数**页面，录入参数，然后单击**下一步**。

**说明**

根据模板的不同，您需要输入的参数将有所差异，请根据控制台提示输入参数信息。
6. 在**配置资源栈**页面，设置是否启用失败时回滚、超时的时间，然后单击**下一步**。

**说明**

超时设置的时间是以分钟为单位的正整数，数字范围为10~1440。
7. 在**确认信息**页面，确认更新后的资源栈相关信息无误后，单击**提交**。

### 重新创建资源栈

当您需要修改资源栈模板、资源栈配置和资源栈归属（包括组织、资源集和地域）时，可以重新创建资源栈。本文为您介绍

**前提条件**

**操作步骤**

1. 登录资源编排控制台。
2. 在左侧导航栏，单击**资源栈**。
3. 在**资源栈**页面，单击目标资源栈右侧**操作**列的**重新创建**。
4. 在**选择模板**页面，选择**组织**、**资源集**和**地域**。
5. 选择模板录入方式，更新模板，然后单击**下一步**。
**输入模板**：在**准备模板**区域输入更新后的JSON格式模板。
**我的模板**：选择已创建的模板。
6. 在**配置模板参数**页面，更改配置名称并输入参数，然后单击**下一步**。

**说明**

根据模板的不同，您需要输入的参数将有所差异，请根据控制台提示输入参数信息。 同一账号中资源栈名称不能重复。
7. 在**配置资源栈**页面，设置是否启用失败时回滚，并设置超时的时间，然后单击**下一步**。

**说明**

超时设置的时间是以分钟为单位的正整数，数字范围为10~1440。
8. 在**确认信息**页面，确认更新后的资源栈相关信息无误后，单击**提交**。
资源编排

### 删除资源栈

**前提条件**

**操作步骤**

1. 登录资源编排控制台。
2. 在左侧导航栏，单击**资源栈**。
3. 删除一个或多个资源栈。
i. 删除一个资源栈：单击目标资源栈右侧**操作**列的**删除**。
4. 在弹出的对话框，确认要删除的资源栈，然后选择**删除方式**。
5. 单击**删除**。
资源编排

## 管理模板

### 创建模板

资源编排服务ROS（Resource Orchestration Service）支持JSON格式的模板，用于创建资源栈。本文为您介绍如何创建模板。

**操作步骤**

1. 登录资源编排控制台。
2. 在左侧导航栏，选择**我的模板**。
3. 在**我的模板**页面，单击**创建模板**。
4. 在**创建模板**对话框，设置**模板名称**、**模板描述**、**组织**、**资源集**和**准备模板**。

| 参数名称 | 相关说明 |
|---|---|
| 模板名称 | 长度为2~255，以大小写字母开头，可包含大小写字母，数字、中划线（-）、下划线 （ ）。 _ |
| 组织 | 选择模板所属的组织。 |
| 资源集 | 选择模板所属的资源集。 |
| 共享范围 | 选择模板的共享范围。 |
| 模板描述 | 最大长度为256个字符。 |
| 准备模板 | 模板内容为JSON格式的文本文件，使用UTF-8编码。用于创建资源栈，是描述基础设施和架构的蓝图。可以在模板中定义资源和配置细节，并说明资源间的依赖关系。关于如何编写模板，请参见模板结构说明。 |

5. 单击**确定**。

### 编辑模板

您可以根据需要编辑模板名称、模板描述和模板内容。

**前提条件**

请确保您已经创建模板。具体操作，请参见创建模板。

**操作步骤**

1. 登录资源编排控制台。
2. 在左侧导航栏，选择**我的模板**。
3. 在筛选列表中，选择筛选选项，并在搜索栏输入相应信息，模板列表中将自动展示符合搜索条件的模板。

**说明**

支持通过**实例或****ID**、**标签筛选**查找目标模板。 您也可以单击高级筛选，同时选择多个筛选选项逐级过滤，以便快速查找模板。
4. 在**我的模板**页面，单击目标模板右侧**操作**列的**编辑**。
5. 在**编辑模板**对话框，编辑**模板名称**、**模板描述**和**准备模板**。
资源编排
6. 单击**确定**。

### 共享设置

您可以根据需要将已经创建的模板，共享给本资源集、本组织或下级组织。

**前提条件**

请确保您已经创建模板。具体操作，请参见创建模板。

**操作步骤**

1. 登录资源编排控制台。
2. 在左侧导航栏，选择**我的模板**。
3. 在**我的模板**页面，单击目标模板右侧**操作**列的**共享设置**。
4. 在**共享设置编辑**页面的**共享范围**下拉框中，根据您的需求选择**本组织及下级组织**、**本资源集共享**或**本组织共享**。
5. 单击确定。

### 删除模板

当您不再使用某个模板时，可以删除该模板。

**前提条件**

请确保您已经创建模板。具体操作，请参见创建模板。

**操作步骤**

1. 登录资源编排控制台。
2. 在左侧导航栏，单击**我的模板**。
3. 在**我的模板**页面，单击目标模板右侧**操作**列的**删除**。
4. 在弹出的对话框，确认要删除的模板，然后单击**删除**。
资源编排

## 查看操作日志

本文为您介绍如何查看操作日志，帮助您用户访问以及使用行为，便于对历史操作进行分析和回溯。

**操作步骤**

1. 登录资源编排控制台。
2. 在左侧导航栏，单击**操作日志**。
3. 在**操作日志**页面，您可查看在设置的起止时间内所有操作人的操作记录。
您可以在**高级筛选**中，按**资源类型**、**操作****IP**、起止时间等过滤条件进一步筛查出关心的操作记录。
4. 选择您要查看的记录，在右侧**详情**列并单击**查看**，可查看**基本信息**以及**实例详情**。
资源编排

## 模板语法

### 模板结构说明

模板是一个JSON格式的文本文件，使用UTF-8编码。模板用于创建资源栈，是描述基础设施和架构的蓝图。模板编辑者在模板中定义阿里云资源和配置细节，并说明资源间的依赖关系。

**ROS模板结构**

```json
{
  "ROSTemplateFormatVersion" : "2015-09-01",
```

`"Description" : "`模板的描述信息，可以用来解释模板的使用场景、架构等。`",`

```json
  "Metadata" : {
```

`//` 模板的元数据信息，例如：可以存放可视化的布局信息。

```json
  },
  "Parameters" : {
  },
  "Mappings" : {
```

`//` 定义映射信息表。映射信息是一种多层的映射结构。

```json
  },
  "Conditions": {
```

`//` 使用内部条件函数定义条件。这些条件确定何时创建关联的资源。

```json
  },
  "Resources" : {
```

`//` 所需资源的详细定义，包括资源间的依赖关系、配置细节等。

```json
  },
  "Outputs" : {
```

`//` 定义输出资源属性等有用信息。可以通过`API`或控制台获取输出的内容。

```
  }
}
```

**ROSTemplateFormatVersion（必选）**

ROS支持的模板版本号，当前版本号：2015-09-01。

**Description（可选）**

模板的描述信息。可用于说明模板的适用场景、架构说明等。 通常情况下，对模板进行详细描述，有利于模板的用户理解模板的内容。

**Metadata（可选）**

模板编写者可以使用Metadata来存放与模板相关的元数据信息，可以是JSON格式的任意内容。

**Parameters（可选）**

定义创建资源栈时，使用模板的用户可以定制化的参数。通常，模板的编辑者会把ECS的规格设计成一个参数，参数支持默认值。使用参数可以增强模板的灵活性，提高复用性。使用模板创建资源栈时，可以根据实际的评估结果来选择合适的规格。

**Mappings（可选）**

Mappings定义了一个多层的映射表，可以通过Fn::FindInMap函数来选择Key对应的值，或根据不同的输入参数值作为Key 来查找映射表。例如：您可以根据地域不同，自动查找Region-镜像映射表，从而找到适用的镜像。

**Conditions（可选）**

资源编排 Conditions使用Fn::And、Fn::Or、Fn::Not、Fn::Equals定义条件。多个条件之间用半角逗号（,）隔开。在创建或更新资源栈时，系统先计算模板中的所有条件，然后再创建资源。创建与 `true` 条件关联的所有资源，忽略与 `false` 条件关联的所有资源。

**Resources（可选）**

用于详细定义使用该模板创建的资源栈所包含的资源，包括资源间的依赖关系、配置细节等。

**Outputs（可选）**

定义输出资源属性等有用信息。可以通过API或控制台获取输出的内容。

### 概览

在创建模板时，使用参数（Parameters）可提高模板的灵活性和可复用性。创建资源栈时，可根据实际情况，替换模板中的某些参数值。

**语法**

每个参数由参数名称和参数属性组成。参数名称必须为英文字母、数字，并且在同一个模板中不能与其它参数名称重复。可以用**Label**字段来定义参数别名。 参数属性如下表所示。

| 参数属性 | 必须 | 描述 |  |  |  |
|---|---|---|---|---|---|
| Type | 是 | 参数的数据类型。取值： String ：字符串。例如： "ecs.s1.medium" 。 Number ：整数或浮点数。例如：3.14。 CommaDelimitedList ：一组用半角逗号（,）分隔的字符串，可通过 Fn::Select函数索引值。例如： "80, foo, bar" 。 Json ：一个JSON格式的字符串。例如： {"foo": "bar"} ， [1, 2, 3] 。 Boolean ：布尔值。例如： true 或者 false 。 ALIYUN::OOS::Parameter::Value ：存储在OOS参数仓库中的普通参数。例如： my image 。 _ ALIYUN::OOS::SecretParameter::Value ：存储在OOS参数仓库中的加密参数。例如： my password 。 _ 说明 ALIYUN::OOS::Parameter::Value 和 ALIYUN::OOS::SecretPa rameter::Value 不支持AllowedPattern校验。 |  |  |  |
|  |  |  | ALIYUN::OOS::SecretPa |  |  |
| Default | 否 | 在创建资源栈时，如果用户没有传入指定值，ROS会检查模板中是否定义默认值。如果已定义默认值，则使用默认值，否则报错。 说明默认值可以设置为 null ，表示该参数取值为空并且忽略对该参数的验证。 |  |  |  |
| AllowedValues | 否 | 包含参数允许值的列表。 |  |  |  |

|  |  | Json |
|---|---|---|
|  | 2, 3] |  |

| [1, |  |
|---|---|

|  |  |  | ALIYUN::OOS::Parameter::Value |
|---|---|---|---|
|  |  | rameter::Value |  |

资源编排

| AllowedPattern | 否 | 一个正则表达式，用于检查用户输入的字符串类型的参数是否匹配。如果用户输入的不是字符串类型，则报错。 如果使用以下特殊字符，需要在字符前输入两个反斜线（\\）进行转义： *.?+-$^[ ]( ){ }\|\/ 说明短划线（-）在紧挨边界时无需转义，例如：[a-z-]。 |
|---|---|---|
| MaxLength | 否 | 一个整数值，允许String类型使用的字符的最大数目。 |
| MinLength | 否 | 一个整数值，允许String类型使用的字符的最小数目。 |
| MaxValue | 否 | 一个数字值，允许Number类型使用的最大数字值。 |
| MinValue | 否 | 一个数字值，允许Number类型使用的最小数字值。 |
| NoEcho | 否 | 当调用查询资源栈时，是否输出参数值。如果将值设置为 true ，则只输出星号（*）。 |
| Description | 否 | 描述参数的字符串。 |
| ConstraintDescrip tion | 否 | 违反该参数约束条件时，说明该约束条件的字符串。 |
| Label | 否 | 参数别名，支持UTF-8字符。通过模板生成Web表单时，可映射为 label 。 |
| AssociationProper ty | 否 | 用于自动验证参数值的合法性，并且给参数提供可选值。 |
| AssociationProper tyMetadata | 否 | 为AssociationProperty定义约束条件，筛选出符合条件的结果。 该属性属于Map类型。 |
| Confirm | 否 | 当NoEcho取值为 true 时，参数是否需要二次输入确认。默认值为 false 。 说明只有String类型的参数，且NoEcho取值为 true 时，Confirm可以为 true 。 |
| TextArea | 否 | 参数是否支持换行。取值： true ：支持换行。 false （默认值）：不支持换行。 例如：以下代码表示参数Content支持换行。 ROSTemplateFormatVersion: '2015-09-01' Parameters: Content: Type: String TextArea: true Outputs: TestContent: Value: Ref: Content |

如果您需要为1个Web应用创建1个资源栈，包含1个负载均衡实例、2个ECS实例和1个RDS实例。如果该Web应用负载较高，可以在创建资源栈时，选择高配的ECS实例；否则可以在创建资源栈时，选择低配的ECS实例。您可以按照如下示例， 在模板中定义ECS实例规格参数： 资源编排

```
Parameters:
  InstanceType:
    Type: String
    AllowedValues:
      - ecs.t1.small
      - ecs.s1.medium
      - ecs.m1.medium
      - ecs.c1.large
    Default: ecs.t1.small
```

`Label: ECS`规格类型 `Description:` 请选择创建`ECS`示例的配置，默认为`ecs.t1.small`，可选`ecs.t1.small, ecs.s1.medium, ecs.m1.mediu`

```
m，ecs.c1.large。
```

示例中，定义的**InstanceType**参数允许用户在使用模板创建资源栈时，对**InstanceType**进行重新赋值。如果用户不设置参数值，则使用默认值： `ecs.t1.small` 。 在定义资源时，可以引用该参数：

```
Webserver:
  InstanceType:
    Ref: InstanceType
```

### 资源（Resources）

资源（Resources）用于描述资源栈中每个资源的属性和资源之间的依赖关系。一个Resources可以被其他资源和Outputs 所引用。

**语法**

Resources由资源ID和资源描述组成。资源描述用大括号（{ }）括起。如果声明多个资源，用半角逗号（,）分隔开。 Resources的语法结构示例如下：

```json
"Resources" : {
```

"资源`1 ID" : {` `"Type" : "`资源类型`",` `"Condition": "`是否创建此资源的条件"，

```json
        "Properties" : {
```

资源属性描述

```
        }
    },
```

"资源`2 ID" : {` `"Type" : "`资源类型`",` `"Condition": "`是否创建此资源的条件"，

```json
        "Properties" : {
```

资源属性描述

```
        }
    }
}
```

参数说明如下： 资源ID：在模板中具有唯一性。在创建模板其他部分时，可以通过资源ID引用该资源。 资源类型（Type）：表示正在声明的资源的类型。例如：ALIYUN::ECS::Instance表示阿里云ECS实例。 资源属性（Properties）：为资源指定的附加选项。例如：必须为每个阿里云ECS实例指定一个Image ID。 示例资源编排

```json
"Resources" : {
  "ECSInstance" : {
    "Type" : "ALIYUN::ECS::Instance",
    "Properties" : {
      "ImageId" : "m-25l0r****"
    }
  }
}
```

如果资源不需要声明任何属性，可以忽略该资源的属性部分。 属性值可以是文本字符串、字符串列表、布尔值、引用参数或者函数返回值。 声明不同的属性值类型示例如下：

```json
"Properties" : {
    "String" : "string",
    "LiteralList" : [ "value1", "value2" ],
    "Boolean" : "true"
    "ReferenceForOneValue" :  { "Ref" : "ResourceID" } ,
    "FunctionResultWithFunctionParams" : {
        "Fn::Join" : [ "%", [ "Key=", { "Ref" : "SomeParameter" } ] ] }
}
```

在模板中，设置DeletionPolicy属性，可以声明在资源栈被删除时保留某个资源。例如：设置在资源栈删除时保留ECS实例，可按照以下示例进行声明：

```json
"Resources" : {
  "ECSInstance" : {
    "Type" : "ALIYUN::ECS::Instance",
    "Properties" : {
      "ImageId" : "m-25l0r****"
    },
    "DeletionPolicy" : "Retain"
  }
}
```

在模板中，设置DependsOn属性，可以指定特定资源紧跟着另一个资源后创建。为某个资源添加DependsOn属性后，该资源仅在DependsOn属性中指定的资源之后创建。 以下示例中，WebServer将在DatabaseServer创建成功后才开始创建：

```json
{
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Resources" : {
    "WebServer": {
      "Type": "ALIYUN::ECS::Instance",
      "DependsOn": "DatabseServer"
    },
    "DatabseServer": {
      "Type": "ALIYUN::ECS::Instance",
      "Properties": {
        "ImageId" : "m-25l0r****",
        "InstanceType": "ecs.t1.small"
      }
    }
  }
}
```

在模板中，使用Condition属性可以指定是否创建此资源的条件。只有Condition所指定的条件值为true时，才会创建此资源。 以下示例中，根据MaxAmount的值判断否创建WebServer： 资源编排

```json
{
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Parameters": {
    "MaxAmount": {
      "Type": "Number",
      "Default": 1
    }
  },
  "Conditions": {
    "CreateWebServer": {"Fn::Not": {"Fn::Equals": [0, {"Ref": "MaxAmount"}]}}
  }
  "Resources" : {
    "WebServer": {
      "Type": "ALIYUN::ECS::InstanceGroup",
      "Condition": "CreateWebServer",
      "Properties": {
        "ImageId" : "m-25l0r****",
        "InstanceType": "ecs.t1.small"
        "MaxAmount": {"Ref": "MaxAmount"}
      }
    },
    "DatabseServer": {
      "Type": "ALIYUN::ECS::Instance",
      "Properties": {
        "ImageId" : "m-25l0r****",
        "InstanceType": "ecs.t1.small"
      }
    }
  }
}
```

**资源声明示例**

典型的资源声明示例如下： 资源编排

```json
"Resources" : {
    "WebServer": {
      "Type": "ALIYUN::ECS::Instance",
      "Properties": {
        "ImageId" : "m-25l0r****",
        "InstanceType": "ecs.t1.small",
        "SecurityGroupId": "sg-25zwc****",
        "ZoneId": "cn-beijing-b",
        "Tags": [{
            "Key": "Department1",
            "Value": "HumanResource"
        },{
            "Key": "Department2",
            "Value": "Finance"
        }
```

]

```json
      }
    },
    "ScalingConfiguration": {
      "Type": "ALIYUN::ESS::ScalingConfiguration",
      "Properties": {
        "ImageId": "ubuntu1404_64_20G_aliaegis_2015****.vhd",
        "InstanceType": "ecs.t1.small",
        "InstanceId": "i-25xhh****",
        "InternetChargeType": "PayByTraffic",
        "InternetMaxBandwidthIn": 1,
        "InternetMaxBandwidthOut": 20,
        "SystemDisk_Category": "cloud",
        "ScalingGroupId": "bwhtvpcBcKYac9fe3vd0****",
        "SecurityGroupId": "sg-25zwc****",
        "DiskMappings": [
            {
                "Size": 10
            },
            {
                "Category": "cloud",
                "Size": 10
            }
```

]

```
      }
    }
}
```

### 输出（Outputs）

在输出（Outputs）中，定义在调用查询资源栈接口时返回的值。例如：定义ECS实例ID的输出，然后可在调用查询资源栈的接口时，查看该实例ID。

**语法**

Outputs由输出ID和输出描述组成。所有输出描述都被括在大括号（{ }）里。如果声明多个输出项，则用半角逗号（,）分隔开。每一个输出项支持以数组形式输出多个值。请参见以下Outputs的语法结构示例代码： 资源编排

```json
"Outputs" : {
```

"输出`1 ID" : {` `"Description" : "`输出项的描述`",` `"Condition": "`是否输出此资源属性的条件`",` `"Value" : "`输出值的表达式"

```
  },
```

"输出`2 ID" : {` `"Description" : "`输出项的描述`",` `"Condition": "`是否输出此资源属性的条件`",`

```json
    "Value" : [
```

"输出值的表达式`1",` "输出值的表达式`2",`

```
      ...
```

]

```
  }
}
```

输出ID：输出项的标识符，在模板中具有唯一性。 Description（可选）：输出项的描述。 Value（必选）：在调用查询资源栈接口时，返回的属性值。 Condition（可选）：使用Condition属性可以指定是否需要创建某个资源和输出资源的信息。当Condition所指定的条件值为 `true` 时，才创建此资源和输出资源信息。 如以下代码所示，根据MaxAmount的值判断是否创建WebServer：

```json
{
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Parameters": {
    "MaxAmount": {
      "Type": "Number",
      "Default": 1
    }
  },
  "Conditions": {
    "CreateWebServer": {"Fn::Not": {"Fn::Equals": [0, {"Ref": "MaxAmount"}]}}
  }
  "Resources" : {
    "WebServer": {
      "Type": "ALIYUN::ECS::InstanceGroup",
      "Condition": "CreateWebServer",
      "Properties": {
        "ImageId" : "m-25l0r****",
        "InstanceType": "ecs.t1.small"
        "MaxAmount": {"Ref": "MaxAmount"}
      }
    }
  }
  "Outputs": {
    "WebServerIP": {
      "Condition": "CreateWebServer",
      "Value": {
        "Fn::GetAtt": ["WebServer", "PublicIps"]
      }
    }
  }
}
```

**示例**

在以下示例中，有2个输出项： 资源ID为WebServer的InstanceId属性。 资源ID为WebServer的PublicIp和PrivateIp属性。 资源编排

```json
"Outputs": {
  "InstanceId": {
    "Value" : {"Fn::GetAtt": ["WebServer", "InstanceId"]}
  },
  "PublicIp & PrivateIp": {
    "Value" : [
      {"Fn::GetAtt": ["WebServer", "PublicIp"]},
      {"Fn::GetAtt": ["WebServer", "PrivateIp"]}
```

]

```
  }
}
```

### 函数（Functions）

资源编排服务提供多个内置函数，帮助您管理您的资源栈。您可以在定义资源（Resources）和输出（Outputs）时，使用内部函数。

**Fn::Base64Encode**

内部函数Fn::Base64Encode返回输入字符串的Base64编码结果。 声明

```
"Fn::Base64Encode": "stringToEncode"
```

参数 `stringToEncode` ：转换成Base64的字符串。 返回值用Base64表示的原始字符串。 示例

```json
{"Fn::Base64Encode": "string to encode"} 返回： c3RyaW5nIHRvIGVuY29kZQ== 。
```

**Fn::Base64Decode**

内部函数Fn::Base64Decode返回Base64编码的字符串解码的结果。 声明

```json
{"Fn::Base64Decode": "stringToEncode"}
```

参数 `stringToDecode` ：将Base64编码的字符串解码。 返回值字符串。 示例

```json
{"Fn::Base64Decode": "c3RyaW5nIHRvIGVuY29kZQ=="}
```

返回： `string to encode` 。

**Fn::Base64**

内部函数Fn::Base64返回输入字符串的Base64编码结果。 声明

```
 "Fn::Base64": stringToEncode
```

参数 valueToEncode：转换成Base64的字符串。 资源编排返回值用Base64表示方法的原始字符串。 示例

```
 "Fn::Base64":"string to encode"
```

**Fn::FindInMap**

内部函数Fn::FindInMap返回与Mappings声明的双层映射中的键对应的值。 声明

```
"Fn::FindInMap": ["MapName", "TopLevelKey", "SecondLevelKey"]
```

参数 `MapName` ：Mappings中所声明映射的ID，包含键和值。 `TopLevelKey` ：第一级键，其值是一个键/值对列表。 `SecondLevelKey` ：第二级键，其值是一个字符串或者数字。 返回值分配给SecondLevelKey的值。 示例在创建名为WebServer的资源时，需要指定ImageId属性。在Mappings中，描述根据地域区分的ImageId映射。在 Parameters中，描述需要用户指定的地域。Fn::FindInMap会根据用户指定的地域，在RegionMap中查找对应的 ImageId映射，然后在映射中找到对应的ImageId。 MapName可自定义。在本示例中为 `RegionMap` 。 TopLevelKey设置为创建资源栈的地区。在本示例中，通过 `{ "Ref" : "regionParam" }` 确定。 SecondLevelKey设置为所需的架构。在本示例中为 `32` 。 资源编排

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "regionParam": {
```

`"Description": "`选择创建`ECS`的地域`",`

```json
      "Type": "String",
      "AllowedValues": [
        "hangzhou",
        "beijing"
```

]

```json
    }
  },
  "Mappings": {
    "RegionMap": {
      "hangzhou": {
        "32": "m-25l0rcfjo",
        "64": "m-25l0rcfj1"
      },
      "beijing": {
        "32": "m-25l0rcfj2",
        "64": "m-25l0rcfj3"
      }
    }
  },
  "Resources": {
    "WebServer": {
      "Type": "ALIYUN::ECS::Instance",
      "Properties": {
        "ImageId": {
          "Fn::FindInMap": [
            "RegionMap",
            {"Ref": "regionParam"},
            "32"
```

]

```json
        },
        "InstanceType": "ecs.t1.small",
        "SecurityGroupId": "sg-25zwc****",
        "ZoneId": "cn-beijing-b",
        "Tags": [
          {
            "Key": "key1",
            "Value": "value1"
          },
          {
            "Key": "key2",
            "Value": "value2"
          }
```

]

```
      }
    }
  }
}
```

支持的函数 Fn::FindInMap Ref

**Fn::GetAtt**

内部函数Fn::GetAtt返回模板中的资源的属性值。 声明资源编排

```
"Fn::GetAtt": ["resourceID", "attributeName"]
```

参数

| resourceID | ：目 |
|---|---|
| attributeName |  |

返回值属性值。 示例返回Resource ID为MyEcsInstance的ImageId属性。

```json
{"Fn::GetAtt" : ["MyEcsInstance" , "ImageID"]}
```

**Fn::Join**

内部函数Fn::Join将一组值连接起来，用特定分隔符隔开。 声明

```json
{"Fn::Join": ["delimiter", ["string1", "string2", ... ]]}
```

参数

| delimiter | ：分隔符。分隔符可以 |
|---|---|
| [ "string1", "string2", ... ] |  |

返回值被连接起来的字符串。 示例

```json
{"Fn::Join": [ ",", ["a", "b", "c"]]}
```

返回： `"a,b,c"` 。 支持的函数 Fn::Base64Encode Fn::GetAtt Fn::Join Fn::Select Ref

**Fn::Select**

内部函数Fn::Select通过索引返回数据元列表中的单个数据元。 声明数据元列表是一个数组：

```
"Fn::Select": ["index", ["value1", "value2", ... ]]
```

数据元列表是一个映射表：

```
"Fn::Select": ["index", {"key1": "value1", ... }]
```

参数 `index` ：待检索数据元的索引。如果数据元列表是一个数组，则索引是0到N-1之间的某个值（其中N代表阵列中元素的数量）。如果数据元列表是一个映射表，则索引是映射表中的某个键。 如果找不到索引对应的值，则返回空字符串。 返回值选定的数据元。 示例资源编排如果数据元列表是一个数组：

```json
{"Fn::Select": ["1", ["apples", "grapes", "oranges", "mangoes"]]}
```

返回： `"grapes"` 。 如果数据元列表是一个映射表：

```json
{"Fn::Select": ["key1", {"key1": "grapes", "key2": "mangoes"}]}
```

返回： `"grapes"` 。 如果数据元列表是一个CommaDelimitedList：

```json
"Parameters": {
  "userParam": {
    "Type": "CommaDelimitedList",
      "Default": "10.0.100.0/24, 10.0.101.0/24, 10.0.102.0/24"
  }
} "Resources": {
  "resourceID": {
      "Properties": {
          "CidrBlock": {"Fn::Select": ["0", {"Ref": "userParam"}]}
    }
  }
}
```

支持的函数对于Fn::Select索引值，您可以使用Ref函数。 对于对象的Fn::Select列表，您可以使用以下函数： Fn::Base64Encode Fn::FindInMap Fn::GetAtt Fn::Join Fn::Select Ref

**Ref**

内部函数Ref返回指定参数或资源的值。 如果指定参数是Resource ID，则返回资源的值。否则系统将认为指定参数是参数，将尝试返回参数的值。 声明

```json
"Ref": "logicalName"
```

参数 `logicalName` ：要引用的资源或参数的逻辑名称。 返回值资源的值或者参数的值。 示例使用Ref函数指定regionParam作为WebServer的RegionMap的地域参数。 资源编排

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "regionParam": {
```

`"Description": "`选择创建`ECS`的地域`",`

```json
      "Type": "String",
      "AllowedValues": [
        "hangzhou",
        "beijing"
```

]

```json
    }
  },
  "Mappings": {
    "RegionMap": {
      "hangzhou": {
        "32": "m-25l0rcfjo",
        "64": "m-25l0rcfj1"
      },
      "beijing": {
        "32": "m-25l0rcfj2",
        "64": "m-25l0rcfj3"
      }
    }
  },
  "Resources": {
    "WebServer": {
      "Type": "ALIYUN::ECS::Instance",
      "Properties": {
        "ImageId": {
          "Fn::FindInMap": [
            "RegionMap",
            {"Ref": "regionParam"},
            "32"
```

]

```json
        },
        "InstanceType": "ecs.t1.small",
        "SecurityGroupId": "sg-25zwc****",
        "ZoneId": "cn-beijing-b",
        "Tags": [
          {
            "Key": "tiantt",
            "Value": "ros"
          },
          {
            "Key": "tiantt1",
            "Value": "ros1"
          }
```

]

```
      }
    }
  }
}
```

支持的函数不能在Ref函数中使用任何函数。必须指定为资源逻辑ID的字符串。

**Fn::GetAZs**

内部函数Fn::GetAZs返回指定Region的可用区列表。 声明

```
"Fn::GetAZs": "region"
```

资源编排参数 `region` ：region ID。 返回值指定Region下的可用区列表。 示例在指定Region的第一个可用区内创建一个ECS实例。

```json
{
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Resources" : {
    "WebServer": {
      "Type": "ALIYUN::ECS::Instance",
      "Properties": {
        "ImageId": "centos7u2_64_40G_cloudinit_2016****.raw",
        "InstanceType": "ecs.n1.tiny",
        "SecurityGroupId": "sg-2zedcm7ep5quses0****",
        "Password": "Ros1****",
        "AllocatePublicIP": true,
        "InternetChargeType": "PayByTraffic",
        "InternetMaxBandwidthIn": 100,
        "InternetMaxBandwidthOut": 100,
        "SystemDiskCategory": "cloud_efficiency",
        "IoOptimized": "optimized",
        "ZoneId": {"Fn::Select": ["0", {"Fn::GetAZs": {"Ref": "ALIYUN::Region"}}]}
      }
    }
  },
  "Outputs": {
    "InstanceId": {
         "Value": {"Fn::GetAtt": ["WebServer","InstanceId"]}
    },
    "PublicIp": {
         "Value": {"Fn::GetAtt": ["WebServer","PublicIp"]}
    }
  }
}
```

支持的函数 Fn::Base64Encode Fn::FindInMap Fn::GetAtt Fn::Join Fn::Select Ref

**Fn::Replace**

内部函数Fn::Replace将字符串中指定子字符串用新字符串替换。 声明

```json
{"Fn::Replace": [{"object_key": "object_value"}, "object_string"]}
```

参数 `object_key` ：将要被替换的字符串。 `object_value` ：将要替换成的最终字符串。 `object_string` ：包含被替换 `object_key` 的字符串。 返回值被替换后的字符串。 资源编排示例所指定脚本中的print替换成echo。

```json
{
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Resources" : {
    "WebServer": {
      "Type": "ALIYUN::ECS::Instance",
      "Properties": {
        "ImageId" : "centos_7_2_64_40G_base_2017****.vhd",
        "InstanceType": "ecs.n1.medium",
        "SecurityGroupId": "sg-94q49****",
        "Password": "MytestPassword****",
        "IoOptimized": "optimized",
        "VSwitchId": "vsw-94vdv8****",
        "VpcId": "vpc-949uz****",
        "SystemDiskCategory": "cloud_ssd",
        "UserData": {"Fn::Replace": [{"print": "echo"},
         {"Fn::Join": ["", [
             "#!/bin/sh\n",
             "mkdir ~/test_ros\n",
             "print hello > ~/1.txt\n"
         ]]}]}
      }
    }
  },
  "Outputs": {
    "InstanceId": {
         "Value" : {"Fn::GetAtt": ["WebServer","InstanceId"]}
    },
    "PublicIp": {
         "Value" : {"Fn::GetAtt": ["WebServer","PublicIp"]}
    }
  }
}
```

支持的函数 Fn::Base64Encode Fn::GetAtt Fn::Join Fn::Select Ref

**Fn::Split**

内部函数Fn::Split通过指定分隔符对字符串进行切片，并返回所有切片组成的列表。 声明

```
"Fn::Split": ["delim", "original_string"]
```

参数

| delim | ：分隔符， |
|---|---|
| original string _ |  |

返回值返回切片后所有字符串组成的列表。 示例如果数据元列表是一个数组：

```json
{"Fn::Split": [";", "foo; bar; achoo"]} 返回： ["foo", " bar", "achoo "] 。
```

资源编排使用Fn::Split对InstanceIds进行切片：

```json
{
  "Parameters": {
    "InstanceIds": {
      "Type": "String",
      "Default": "instane1_id,instance2_id,instance2_id"
    }
  },
  "Resources": {
    "resourceID": {
      "Type": "ALIYUN::SLB::BackendServerAttachment",
      "Properties": {
        "BackendServerList": {
          "Fn::Split": [
            ",",
            {
              "Ref": "InstanceIds"
            }
```

]

```
        }
      }
    }
  }
}
```

支持的函数 Fn::Base64Encode Fn::FindInMap Fn::GetAtt Fn::Join Fn::Select Fn::Replace Fn::GetAZs Fn::If Ref

**Fn::Equals**

比较两个值是否相等。如果两个值相等，则返回true；如果不相等，则返回false。 声明

```json
{"Fn::Equals": ["value_1", "value_2"]}
```

参数 `value` ：要比较的任意类型的值。 返回值 true或false。 示例在Conditions中使用Fn::Equals定义条件。 资源编排

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "EnvType": {
      "Default": "pre",
      "Type": "String"
    }
  },
  "Conditions": {
    "TestEqualsCond": {
      "Fn::Equals": [
        "prod",
        {"Ref": "EnvType"}
```

]

```
    }
  }
}
```

支持的函数 Fn::Or Fn::Not Fn::Equals Fn::FindInMap Fn::And Ref

**Fn::And**

代表AND运算符，最少包含两个条件。如果所有指定条件计算为true，则返回true；如果任意条件计算为false，则返回 false。 声明

```json
{"Fn::And": ["condition", {...}]}
```

参数 `condition` ：计算为true或false的条件。 返回值 true或false。 示例在Conditions中使用Fn::And定义一个条件：

```json
{
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Parameters":{
    "EnvType":{
      "Default":"pre",
      "Type":"String"
    }
  },
  "Conditions": {
    "TestEqualsCond": {"Fn::Equals": ["prod", {"Ref": "EnvType"}]},
    "TestAndCond": {"Fn::And": ["TestEqualsCond", {"Fn::Equals": ["pre", {"Ref": "EnvType"}]}]}
  }
}
```

支持的函数 Fn::Or Fn::Not Fn::Equals Fn::FindInMap 资源编排 Fn::And Ref

**Fn::Or**

代表OR运算符，最少包含两个条件。如果任意一个指定条件计算为true，则返回true；如果所有条件都计算为false，则返回false。 声明

```json
{"Fn::Or": ["condition", {...}]}
```

参数 `condition` ：计算为true或false的条件。 返回值 true或false。 示例在Conditions中使用Fn::Or定义一个条件。

```json
{
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Parameters":{
    "EnvType":{
      "Default":"pre",
      "Type":"String"
    }
  },
  "Conditions": {
    "TestEqualsCond": {"Fn::Equals": ["prod", {"Ref": "EnvType"}]},
    "TestOrCond": {"Fn::And": ["TestEqualsCond", {"Fn::Equals": ["pre", {"Ref": "EnvType"}]}]}
  }
}
```

支持的函数 Fn::Or Fn::Not Fn::Equals Fn::FindInMap Fn::And Ref

**Fn::Not**

代表NOT运算符。对计算为false的条件，返回true；对计算为true的条件，返回false。 声明

```json
{"Fn::Not": "condition"}
```

参数 `condition` ：计算为true或false的条件。 返回值 true或false。 示例在Conditions中使用Fn::Not定义一个条件。 资源编排

```json
{
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Parameters":{
    "EnvType":{
      "Default":"pre",
      "Type":"String"
    }
  },
  "Conditions": {
    "TestNotCond": {"Fn::Not": {"Fn::Equals": ["pre", {"Ref": "EnvType"}]}}
  }
}
```

支持的函数 Fn::Or Fn::Not Fn::Equals Fn::FindInMap Fn::And Ref

**Fn::If**

如果指定的条件计算为true，则返回一个值；如果指定的条件计算为false，则返回另一个值。在模板Resources和Outputs 属性值中支持Fn::If内部函数。您可以使用 `ALIYUN::NoValue` 伪参数作为返回值来删除相应的属性。 声明

```json
{"Fn::If": ["condition_name", "value_if_true", "value_if_false"]}
```

参数

| condition name _ |  |
|---|---|
| value if true _ _ | ： |
| value if false _ _ |  |

示例根据输入的参数，确定是否创建数据盘。

```json
{
    "ROSTemplateFormatVersion":"2015-09-01",
    "Parameters":{
        "EnvType":{
            "Default":"pre",
            "Type":"String"
        }
    },
    "Conditions":{
        "CreateDisk":{
            "Fn::Equals":[
                "prod",
                {
                    "Ref":"EnvType"
                }
```

]

```json
        }
    },
    "Resources":{
        "WebServer":{
            "Type":"ALIYUN::ECS::Instance",
            "Properties":{
                "DiskMappings":{
                    "Fn::If":[
                        "CreateDisk",
```

资源编排 [

```json
                            {
                                "Category":"cloud_efficiency",
                                "DiskName":"FirstDataDiskName",
                                "Size":40
                            },
                            {
                                "Category":"cloud_ssd",
                                "DiskName":"SecondDataDiskName",
                                "Size":40
                            }
```

`],`

```json
                        {
                            "Ref":"ALIYUN::NoValue"
                        }
```

]

```json
                },
                "VpcId":"vpc-2zew9pxh2yirtzqxd****",
                "SystemDiskCategory":"cloud_efficiency",
                "SecurityGroupId":"sg-2zece6wcqriejf1v****",
                "SystemDiskSize":40,
                "ImageId":"centos_6_8_64_40G_base_2017****.vhd",
                "IoOptimized":"optimized",
                "VSwitchId":"vsw-2zed9txvy7h2srqo6****",
                "InstanceType":"ecs.n1.medium"
            }
        }
    },
    "Outputs":{
        "InstanceId":{
            "Value":{
                "Fn::GetAtt":[
                    "WebServer",
                    "InstanceId"
```

]

```json
            }
        },
        "ZoneId":{
            "Value":{
                "Fn::GetAtt":[
                    "WebServer",
                    "ZoneId"
```

]

```
            }
        }
    }
}
```

支持的函数 Fn::Or Fn::Not Fn::Equals Fn::FindInMap Fn::And Ref

**Fn::ListMerge**

合并多个列表为一个列表。 声明资源编排

```json
{"Fn::ListMerge": [["list_1_item_1", "list_1_imte_2", ...], ["list_2_item_1", "list_2_imte_2", ...] ]}
```

参数 `["list_1_item_1", "list_1_imte_2", ...]` ：将要合并的第一个列表。 `["list_2_item_1", "list_2_imte_2", ...]` ：将要和第一个列表合并的列表。 示例把两个ECS组挂载到同一个负载均衡实例上。

```json
{
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Resources" : {
    "LoadBalancer": {
      "Type": "ALIYUN::SLB::LoadBalancer",
      "Properties": {
        "LoadBalancerName": "ros",
        "AddressType": "internet",
        "InternetChargeType": "paybybandwidth",
      }
    },
    "BackendServer1": {
      "Type": "ALIYUN::ECS::InstanceGroup",
      "Properties": {
        "ImageId" : "m-2ze9uqi7wo61hwep****",
        "InstanceType": "ecs.t1.small",
        "SecurityGroupId": "sg-2ze8yxgempcdsq3****",
        "MaxAmount": 1,
        "MinAmount": 1
      }
    },
    "BackendServer2": {
      "Type": "ALIYUN::ECS::InstanceGroup",
      "Properties": {
        "ImageId" : "m-2ze9uqi7wo61hwep****",
        "InstanceType": "ecs.t1.small",
        "SecurityGroupId": "sg-2ze8yxgempcdsq3iu****",
        "MaxAmount": 1,
        "MinAmount": 1
      }
    },
    "Attachment": {
      "Type": "ALIYUN::SLB::BackendServerAttachment",
      "Properties": {
        "LoadBalancerId": {"Ref": "LoadBalancer"},
        "BackendServerList": { "Fn::ListMerge": [
            {"Fn::GetAtt": ["BackendServer1", "InstanceIds"]},
            {"Fn::GetAtt": ["BackendServer2", "InstanceIds"]}
```

]

```
        }
      }
    }
  }
}
```

支持的函数 Fn::Base64Encode Fn::GetAtt Fn::Join Fn::Select Ref 资源编排 Fn::If

**Fn::GetJsonValue**

解析JSON字符串，获取指定的Key在第一层所对应的值。 声明

```json
{"Fn::GetJsonValue": ["key", "json_string"]}
```

参数

| key | ：键值。 |
|---|---|
| json string _ |  |

示例 WebServer2从WebServer实例执行完UserData返回的JSON字符串中，获取对应的值。

```json
{
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Resources" : {
    "WebServer": {
      "Type": "ALIYUN::ECS::Instance",
      "Properties": {
        "ImageId" : "m-2ze45uwova5fedlu****",
        "InstanceType": "ecs.n1.medium",
        "SecurityGroupId": "sg-2ze7pxymaix640qr****",
        "Password": "Wenqiao****",
        "IoOptimized": "optimized",
        "VSwitchId": "vsw-2zei67xd9nhcqxze****",
        "VpcId": "vpc-2zevx9ios1rszqv0a****",
        "SystemDiskCategory": "cloud_ssd",
        "UserData": {"Fn::Join": ["", [
             "#!/bin/sh\n",
             "mkdir ~/test_ros\n",
             "print hello > ~/1.txt\n",
             "Fn::GetAtt": ["WaitConHandle", "CurlCli"],
             "\n",
             "Fn::GetAtt": ["WaitConHandle", "CurlCli"],
             " -d '{\\"id\\" : \\"1\\", \\"data\\": [\\"1111\\", \\"2222\\"]}'\n"
         ]]},
         "PrivateIpAddress": "192.168.XX.XX",
         "HostName": "userdata-1
      }
    },
    "WaitConHandle": {
    },
    "WaitCondition": {
        "Type": "ALIYUN::ROS::WaitCondition",
        "Properties": {
          "Handle": {"Ref": "WaitConHandle"},
          "Timeout": 900
        }
    },
    "WebServer2": {
      "Type": "ALIYUN::ECS::Instance",
      "Properties": {
        "ImageId" : "m-2ze45uwova5fedlu****",
        "InstanceType": "ecs.n1.medium",
        "SecurityGroupId": "sg-2ze7pxymaix640qr****",
        "Password": "Wenqiao****,
        "IoOptimized": "optimized",
        "VSwitchId": "vsw-2zei67xd9nhcqxzec****",
        "VpcId": "vpc-2zevx9ios1rszqv0a****",
"SystemDiskCategory":"cloudssd"
```

资源编排

```json
        SystemDiskCategory: cloud_ssd,
        "UserData":
          {"Fn::Join": ["", [
             "#!/bin/sh\n",
             "mkdir ~/test_ros\n",
             "echo hello > ~/1.txt\n",
             "server_1_token=",
             {"Fn::GetJsonValue": ["1", { "Fn::GetAtt": ["WaitCondition", "Data"]}]},
             "\n"
         ]]},
         "PrivateIpAddress": "192.168.XX.XX",
         "HostName": "userdata-2"
      }
    },
  },
  "Outputs": {
    "InstanceId": {
         "Value" : {"Fn::GetAtt": ["WebServer","InstanceId"]}
    },
    "PublicIp": {
         "Value" : {"Fn::GetAtt": ["WebServer","PublicIp"]}
    }
  }
}
```

支持的函数 Fn::Base64Encode Fn::GetAtt Fn::Join Fn::Select Ref Fn::If

**Fn::MergeMapToList**

将多个Mapping合并成一个以Mapping为元素的列表。 声明

```json
{"Fn::MergeMapToList": [{"key_1": ["key_1_item_1", "key_1_item_2", ...]}, {"key_2":["key_2_item_1", "key_2_item_2", ...]}, ... ]}
```

参数 `{"key_1": ["key_1_item_1", "key_1_item_2", ...]}` ：将要合并的第一个Mapping。 `"key_1"` 所对应的值必须是一个列表。 `"key_1"` 将是合并后的列表元素中，每个Mapping的一个键。其对应的值在第一个Mapping中将是 `"key_1_item_1"` ，在第二个Mapping中是 `"key_1_item_2"` ，以此类推。最终合并的列表长度是所有将要合并的参数Mapping中， `"key_x"` 所对应的列表中最长的长度。如果有的 `"key_y"` 所对应的列表长度比较短，会重复此列表的最后一个元素，使列表长度都达到最长。 `{"key_2": ["key_2_item_1", "key_2_item_2", ...]}` ：将要合并的第二个Mapping。 `"key_2"` 所对应的值必须是一个列表。 `"key_2"` 将是合并后的列表元素中每个Mapping的一个键。其对应的值在第一个Mapping中将是 `"key_2_item_1"` ，在第二个Mapping中是 `"key_2_item_2"` ，以此类推。 示例资源编排合并三个Mapping，每个Mapping中键值对应的列表长度一致。

```json
{
   "Fn::MergeMapToList": [
      {"key_1": ["kye_1_item_1", "kye_1_item_2"]},
      {"key_2": ["kye_2_item_1", "kye_2_item_2"]},
      {"key_3": ["kye_3_item_1", "kye_3_item_2"]}
```

]

```
}
```

最终的合并结果如下。 [

```json
   {
      "key_1": "kye_1_item_1",
      "key_2": "kye_2_item_1",
      "key_3": "kye_3_item_1"
    },
    {
      "key_1": "kye_1_item_2",
      "key_2": "kye_2_item_2",
      "key_3": "kye_3_item_2"
    }
```

] 合并三个Mapping，每个Mapping中键值对应的列表长度不一致。

```json
{
   "Fn::MergeMapToList": [
      {"key_1": ["kye_1_item_1", "kye_1_item_2"]},
      {"key_2": ["kye_2_item_1", "kye_2_item_2", "key_2_item_3"]},
      {"key_3": ["kye_3_item_1", "kye_3_item_2"]}
```

]

```
}
```

最终的合并结果如下。 [

```json
   {
      "key_1": "kye_1_item_1",
      "key_2": "kye_2_item_1",
      "key_3": "kye_3_item_1"
    },
    {
      "key_1": "kye_1_item_2",
      "key_2": "kye_2_item_2",
      "key_3": "kye_3_item_2"
    },
    {
      "key_1": "kye_1_item_2",
      "key_2": "kye_2_item_3",
      "key_3": "kye_3_item_2"
    }
```

] 资源编排以下模板示例中，把WebServer中创建的所有实例，都加入到一个负载均衡的虚拟服务器组中。

```json
{
    "ROSTemplateFormatVersion": "2015-09-01",
    "Resources": {
        "WebServer": {
          "Type": "ALIYUN::ECS::InstanceGroupClone",
          "Properties": {
              "SourceInstanceId": "i-xxxxx",
               "Password": "Hello****",
               "MinAmount": 1,
               "MaxAmount": 1
          }
        },
        "CreateVServerGroup": {
            "Type": "ALIYUN::SLB::VServerGroup",
            "Properties": {
                "LoadBalancerId": "lb-****",
                "VServerGroupName": "VServerGroup-****",
                "BackendServers": {
                   "Fn::MergeMapToList": [
                       {"Port": [6666, 9090, 8080]},
                       {"ServerId": {"Fn::GetAtt": ["WebServer", "InstanceIds"]}},
                       {"Weight": [20, 100]}
```

]

```
                }
            }
        }
    }
}
```

支持的函数 Fn::Base64Encode Fn::GetAtt Fn::Join Fn::Select Ref Fn::If Fn::ListMerge Fn::GetJsonValue

**Fn::Avg**

内部函数Fn::Avg对一组数求平均值。 声明

```json
{"Fn::Avg": [ndigits, [number1, number2, ... ]]}
```

参数

| ndigits | ：平均值保留几位小 |
|---|---|
| [ number1, number2, ... ] |  |

返回值给定一组数字的平均值。 示例

```json
{ "Fn::Avg": [ 1, [1, 2, 6.0] ] } { "Fn::Avg": [ 1, ['1', '2', '6.0'] ] }
```

返回：**3.0**。 支持的函数资源编排 Fn::GetAtt Ref

**Fn::SelectMapList**

内部函数Fn::SelectMapList返回一个由map中元素构成的列表。 声明

```json
{"Fn::SelectMapList": ["key2", [{"key1": "value1-1", "key3": "value1-3"}, {"key1": "value2-1", "key 2": "value2-2"}, {"key1": "value3-1", "key2": "value3-2"}, ...] ] }
```

参数

| key2 | ：在map中查询的key。 |
|---|---|
| [{ "key1": "value1-1", "key3": "value1-3" }, ... ] |  |

返回值对map_list中的每个map，取出key对应的值，合并成一个列表。 示例

```json
{
 "Fn::SelectMapList": [
   "key2",
```

[

```json
      {"key1": "value1-1", "key3": "value1-3"},
      {"key1": "value2-1", "key2": "value2-2"},
      {"key1": "value3-1", "key2": "value3-2"}
```

] ]

```
} 返回： ["value2-2","value3-2"] 。
```

**Fn::Add**

内部函数Fn::Add对参数进行求和。 声明

```json
{"Fn::Add": [{"Product": "ROS"}, {"Fn": "Add"}]}
```

参数参数为一个列表。 列表内元素可以是数字、列表、字典，但是所有元素必须是同一类型，至少2个元素。 返回值如果是数字类型，对参数进行求和；如果是列表类型，对参数进行拼接；如果是字典类型，对参数进行合并，key相同的情况下，后面的key值覆盖前面的key值。 示例

```json
{
 "Fn::Add": [
   {"Product": "ROS"},
   {"Fn": "Add"}
```

]

```
} 返回： {"Fn":"Add","Product":"ROS"} 。
```

### 映射（Mappings）

映射是一个Key-Value映射表。在模板的Resources和Outputs中，可以使用Fn::FindInMap内部函数，通过指定Key而获取映射表的Value。

**语法**

资源编排映射由Key-Value对组成。其中Key和Value可以为字符串类型或者数字类型。如果声明多个映射，用半角逗号（,）分隔开。每个映射的名称不能重复。映射须为纯数据，映射不会解析函数。

**示例**

正确的映射示例：

```json
"Mappings": {
    "ValidMapping": {
        "TestKey1": {"TestValu1": "value1"},
        "TestKey2": {"TestValu2": "value2"},
        1234567890: {"TestValu3": "value3"},
        "TestKey4": {"TestValu4": 1234}
    }
}
```

错误的映射示例：

```json
"Mappings": {
    "InvalidMapping1": {
        "ValueList": ["foo", "bar"],
          "ValueString": "baz"
    },
    "InvalidMapping2": ["foo", {"bar" : "baz"}],
    "InvalidMapping3": "foobar"
}
```

使用内部函数Fn::FindInMap返回对应的值示例： 资源编排

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "regionParam": {
```

`"Description": "`选择创建`ECS`的地域`",`

```json
      "Type": "String",
      "AllowedValues": [
        "hangzhou",
        "beijing"
```

]

```json
    }
  },
  "Mappings": {
    "RegionMap": {
      "hangzhou": {
        "32": "m-25l0rcfjo",
        "64": "m-25l0rcfj1"
      },
      "beijing": {
        "32": "m-25l0rcfj2",
        "64": "m-25l0rcfj3"
      }
    }
  },
  "Resources": {
    "WebServer": {
      "Type": "ALIYUN::ECS::Instance",
      "Properties": {
        "ImageId": {
          "Fn::FindInMap": [
            "RegionMap",
            {
              "Ref": "regionParam"
            },
            "32"
```

]

```json
        },
        "InstanceType": "ecs.t1.small",
        "SecurityGroupId": "sg-25zwc****",
        "ZoneId": "cn-beijing-b",
        "Tags": [
          {
            "Key": "Department1",
            "Value": "HumanResource"
          },
          {
            "Key": "Department2",
            "Value": "Finance"
          }
```

]

```
      }
    }
  }
}
```

### 条件（Conditions）

每一个条件项由Fn::And、Fn::Or、Fn::Not或Fn::Equals定义。根据您在创建或更新资源栈时，指定的输入参数值进行计算。在每个条件中，都可以引用其他条件、参数值或映射。在模板的Resources和Outputs部分，将条件与资源关联起来。 条件和资源的关联通过两种方式实现：Fn::If 函数或者资源的Condition字段。 资源编排

**语法**

每个条件由条件名和条件本身组成，其中条件名是字符串类型。条件是由Fn::And、Fn::Or、Fn::Not或Fn::Equals定义，在条件中可以引用其他条件。多个条件用半角逗号（,）隔开，每个条件名不能重复。 允许使用如下函数，但不能是最外层的函数： "Fn::Select"、 "Fn::Join"、 "Fn::Split"、"Fn::Replace"、"Fn::Base64Encode"、"Fn::Base64Decode"、 "Fn::MemberListToMap"、"Fn::If"、 "Fn::ListMerge"、 "Fn::GetJsonValue"、"Fn::MergeMapToList"、 "Fn::SelectMapList"、"Fn::Add"、"Fn::Avg"、"Fn::Str"、"Fn::Calculate"、"Ref"（仅参数引用）、"Fn:: FindInMap"。

**示例**

设置Conditions

```json
"Conditions" : {
       "DevEnv": {"Fn::Equals": ["Dev", {"Ref": "EnvType"}]},
       "UTEnv": {"Fn::Equals": ["UT", {"Ref": "EnvType"}]},
       "PREEnv": {"Fn::Not": {"Fn::Or": ["DevEnv", "UTEnv"]}},
       "ProdEnv": {"Fn::And": [{"Fn::Equals": ["Prod", {"Ref": "EnvType"}]}, "PREEnv"]}
}
```

关联Conditions和Resources 本示例中，根据EnvType参数值决定是否为ECS instance创建数据盘和OSS存储空间。

```json
{
    "ROSTemplateFormatVersion":"2015-09-01",
    "Parameters":{
        "EnvType":{
            "Default":"pre",
            "Type":"String"
        }
    },
    "Conditions":{
        "CreateProdRes":{
            "Fn::Equals":[
                "prod",
                {
                    "Ref":"EnvType"
                }
```

]

```json
        }
    },
    "Resources":{
        "WebServer":{
            "Type":"ALIYUN::ECS::Instance",
            "Properties":{
                "DiskMappings":{
                    "Fn::If":[
                        "CreateProdRes",
```

[

```json
                            {
                                "Category":"cloud_efficiency",
                                "DiskName":"FirstDataDiskName",
                                "Size":40
                            },
                            {
                                "Category":"cloud_ssd",
                                "DiskName":"SecondDataDiskName",
                                "Size":40
                            }
```

`],`

```json
                        {
                            "Ref":"ALIYUN::NoValue"
}
```

资源编排

```
                        }
```

]

```json
                },
                "VpcId":"vpc-2zew9pxh2yirtzqxd****",
                "SystemDiskCategory":"cloud_efficiency",
                "SecurityGroupId":"sg-2zece6wcqriejf1v****",
                "SystemDiskSize":40,
                "ImageId":"centos_6_8_64_40G_base_2017****.vhd",
                "IoOptimized":"optimized",
                "VSwitchId":"vsw-2zed9txvy7h2srqo6****",
                "InstanceType":"ecs.n1.medium"
            }
        },
        "OssBucket": {
            "Type": "ALIYUN::OSS::Bucket",
            "Condition": "CreateProdRes",
            "Properties": {
                "AccessControl": "private",
                "BucketName": "myprodbucket"
            }
        }
    },
    "Outputs":{
        "InstanceId":{
            "Value":{
                "Fn::GetAtt":[
                    "WebServer",
                    "InstanceId"
```

]

```json
            }
        },
        "OssDomain":{
            "Condition": "CreateProdRes",
            "Value":{
                "Fn::GetAtt":[
                    "OssBucket",
                    "DomainName"
```

]

```
            }
        }
    }
}
```

资源编排

## 资源类型

### ECS

#### ALIYUN::ECS::AutoSnapshotPolicy

**语法**

```json
{
  "Type" : "ALIYUN::ECS::AutoSnapshotPolicy",
  "Properties" : {
    "TimePoints" : String,
    "RepeatWeekdays" : String,
    "RetentionDays" : Integer,
    "DiskIds" : List,
    "Tags": List,
    "AutoSnapshotPolicyName" : String,
    "ResourceGroupId": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| TimePoints | List | 是 | 是 | 自动快照的创建时间点。 | 取值范围：0~23。表示00:00至 23:00共24个时间点，例如：1表示 01:00。 单位：小时。 当一天内需要创建多次自动快照时，可以传入多个时间点： 最多传入24个时间点。 多个时间点用格式为[0, 1, … 23]的列表表示，时间点之间用半角逗号（,）隔开。 |
| RepeatWeekd ays | List | 是 | 是 | 自动快照的重复日期。 | 取值：1~7，依次表示周一至周日。 周期：星期。 如果一星期内需要创建多次自动快照时，可设置多个时间点，多个时间点用[1, 2, … 7]的列表表示，多个时间点之间用半角逗号（,）隔开。最多设置7个时间点。 |
| RetentionDay s | Integer | 是 | 是 | 自动快照的保留时间。 | 取值范围： -1（默认值）：永久保存。 1~65,535：指定保存天数。 单位：天。 |
| DiskIds | List | 否 | 是 | 目标磁盘ID。 | 当您需要将自动快照策略应用于多块磁盘时，多块磁盘ID用["d- xxxxxxxxx", "d-yyyyyyyyy", … "d-zzzzzzzzz"]的列表表示，磁盘 ID之间用半角逗号（,）隔开。 |

资源编排

| ResourceGro upId | String | 否 | 是 | 快照所属的资源组ID。 | 无 |
|---|---|---|---|---|---|
| Tags | List | 否 | 是 | 标签。 | 最多支持添加20个标签。 更多信息，请参见Tags属性。 |
| AutoSnapshot PolicyName | String | 否 | 是 | 自动快照策略的名称。 | 长度为2~128个字符。必须以英文字母或汉字开头，不能以 http:// 和 https:// 开头。可包含英文字母、汉字、数字、半角冒号（:）、下划线（ ）或 _ 短划线（-）。 默认值：空。 |

**Tags语法**

```json
"Tags": [
  {
    "Key": String,
    "Value": String
  }
```

]

**Tags属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Key | String | 是 | 否 | 标签键。 | 长度为1~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |
| Value | String | 否 | 否 | 标签值。 | 长度为0~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |

**返回值**

Fn::GetAtt AutoSnapshotPolicyId：自动快照策略ID。

**示例**

`JSON` 格式

```json
{
 "ROSTemplateFormatVersion": "2015-09-01",
 "Parameters": {
  "TimePoints": {
   "Type": "CommaDelimitedList",
   "Description": "The automatic snapshot creation schedule, and the unit of measurement is hour. Val
ue range: [0, 23], which represents from 00:00 to 24:00, for example 1 indicates 01:00. When you want to schedule multiple automatic snapshot tasks for a disk in a day, you can set the TimePoints to an a rray.\nA maximum of 24 time points can be selected.\nThe format is a list of [0, 1, ..., 23] and the time points are separated by commas (,)."
  },
  "DiskIds": {
   "Type": "Json",
   "Description": "The disk ID. When you want to apply the automatic snapshot policy to multiple disk
s, you can set the DiskIds to an array. The format is list of [\"d-xxxxxxxxx\", \"d-yyyyyyyyy\", ..., \"d-zzzzzzzzz\"] and the IDs are separated by commas (,)."
```

资源编排

```json
  },
  "RetentionDays": {
   "Type": "Number",
   "Description": "The snapshot retention time, and the unit of measurement is day. Optional values:\
n-1: The automatic snapshots are retained permanently.\n[1, 65536]: The number of days retained.\nDef ault value: -1.",
   "MinValue": -1,
   "MaxValue": 65536
  },
  "RepeatWeekdays": {
   "Type": "Json",
   "Description": "The automatic snapshot repetition dates. The unit of measurement is day and the re
peating cycle is a week. Value range: [1, 7], which represents days starting from Monday to Sunday, f or example 1 indicates Monday. When you want to schedule multiple automatic snapshot tasks for a disk in a week, you can set the RepeatWeekdays to an array.\nA maximum of seven time points can be selecte d.\nThe format is a list of [1, 2, ..., 7] and the time points are separated by commas (,)."
  },
  "AutoSnapshotPolicyName": {
   "Type": "String",
   "Description": "The name of the automatic snapshot policy.\nIt can consist of [2, 128] English or
Chinese characters.\nMust begin with an uppercase or lowercase letter or a Chinese character. Can con tain numbers, periods (.), colons (:), underscores (_), and hyphens (-).\nCannot start with http:// o r https://.\nDefault value: null."
  },
  "Tags": {
   "Type": "Json",
   "Description": "Tags to attach to instance. Max support 20 tags to add during create instance. Eac
h tag with two properties Key and Value, and Key is required.",
   "MaxLength": 20
  }
 },
 "Resources": {
  "AutoSnapshotPolicy": {
   "Type": "ALIYUN::ECS::AutoSnapshotPolicy",
   "Properties": {
    "TimePoints": {
     "Ref": "TimePoints"
    },
    "DiskIds": {
     "Ref": "DiskIds"
    },
    "RetentionDays": {
     "Ref": "RetentionDays"
    },
    "RepeatWeekdays": {
     "Ref": "RepeatWeekdays"
    },
    "AutoSnapshotPolicyName": {
     "Ref": "AutoSnapshotPolicyName"
    },
    "Tags": {
     "Ref": "Tags"
    }
   }
  }
 },
 "Outputs": {
  "AutoSnapshotPolicyId": {
   "Description": "The automatic snapshot policy ID.",
   "Value": {
    "Fn::GetAtt": [
     "AutoSnapshotPolicy",
```

" S h `li` `d"` 资源编排

```
     "AutoSnapshotPolicyId"
```

]

```
   }
  }
 }
}
```

`YAML` 格式

```json
ROSTemplateFormatVersion: '2015-09-01' Parameters:
 AutoSnapshotPolicyName:
  Description: 'The name of the automatic snapshot policy.
   It can consist of [2, 128] English or Chinese characters.
   Must begin with an uppercase or lowercase letter or a Chinese character. Can
   contain numbers, periods (.), colons (:), underscores (_), and hyphens (-).
   Cannot start with http:// or https://.
   Default value: null.'
  Type: String
 DiskIds:
  Description: The disk ID. When you want to apply the automatic snapshot policy
   to multiple disks, you can set the DiskIds to an array. The format is list of
   ["d-xxxxxxxxx", "d-yyyyyyyyy", ..., "d-zzzzzzzzz"] and the IDs are separated
   by commas (,).
  Type: Json
 RepeatWeekdays:
  Description: 'The automatic snapshot repetition dates. The unit of measurement
   is day and the repeating cycle is a week. Value range: [1, 7], which represents
   days starting from Monday to Sunday, for example 1 indicates Monday. When you
   want to schedule multiple automatic snapshot tasks for a disk in a week, you
   can set the RepeatWeekdays to an array.
   A maximum of seven time points can be selected.
   The format is a list of [1, 2, ..., 7] and the time points are separated by
   commas (,).'
  Type: Json
 RetentionDays:
  Description: 'The snapshot retention time, and the unit of measurement is day.
   Optional values:
   -1: The automatic snapshots are retained permanently.
   [1, 65536]: The number of days retained.
   Default value: -1.'
  MaxValue: 65536
  MinValue: -1
  Type: Number
 Tags:
  Description: Tags to attach to instance. Max support 20 tags to add during create
   instance. Each tag with two properties Key and Value, and Key is required.
  MaxLength: 20
  Type: Json
 TimePoints:
  Description: 'The automatic snapshot creation schedule, and the unit of measurement
   is hour. Value range: [0, 23], which represents from 00:00 to 24:00, for example
   1 indicates 01:00. When you want to schedule multiple automatic snapshot tasks
```

资源编排

```
   for a disk in a day, you can set the TimePoints to an array.
   A maximum of 24 time points can be selected.
   The format is a list of [0, 1, ..., 23] and the time points are separated by
   commas (,).'
  Type: CommaDelimitedList
Resources:
 AutoSnapshotPolicy:
  Properties:
   AutoSnapshotPolicyName:
    Ref: AutoSnapshotPolicyName
   DiskIds:
    Ref: DiskIds
   RepeatWeekdays:
    Ref: RepeatWeekdays
   RetentionDays:
    Ref: RetentionDays
   Tags:
    Ref: Tags
   TimePoints:
    Ref: TimePoints
Outputs:
 AutoSnapshotPolicyId:
  Description: The automatic snapshot policy ID.
  Value:
   Fn::GetAtt:
   - AutoSnapshotPolicyId
```

更多示例，请参见：JSON示例和YAML示例。

#### ALIYUN::ECS::BandwidthPackage

ALIYUN::ECS::BandwidthPackage类型用于创建NAT网关使用的带宽包。

**语法**

```json
{
  "Type": "ALIYUN::ECS::BandwidthPackage",
  "Properties": {
    "Description": String,
    "NatGatewayId": String,
    "ZoneId": String,
    "BandwidthPackageName": String,
    "Bandwidth": Integer,
    "IpCount": Integer
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| NatGatewayId | String | 是 | 否 | 带宽包要绑定的 NAT网关ID | 无 |

资源编排

| Bandwidth | Integer | 是 | 否 | 带宽大小 | 取值范围：5~5000 单位：Mbps 默认值：5 Mbps |
|---|---|---|---|---|---|
| IpCount | Integer | 是 | 否 | 分配公网IP的个数 | 取值范围：1~5 |
| Description | String | 否 | 否 | 带宽包描述 | 长度为2~256个字符 |
| ZoneId | String | 否 | 否 | 所属地域下的可用区 | 无 |
| BandwidthPack ageName | String | 否 | 否 | 带宽包的名称 | 长度为2~128个字符。必须以英文字母或中文字符开头，可包含英文字母、数字、中文字符、下划线 （ ）、英文句点（.）和短 _ 划线（-）。 |

**返回值**

Fn::GetAtt BandwidthPackageId：带宽包的ID。 BandwidthPackageIps：带宽包的所有IP。

**示例**

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "BandwidthPackage": {
      "Type": "ALIYUN::ECS::BandwidthPackage",
      "Properties": {
        "BandwidthPackageName": "pkg_2",
        "Description": "my_bandwidth",
        "NatGatewayId": "ngw-h1xox****",
        "IpCount": 2,
        "Bandwidth": 5,
        "ZoneId": "cn-beijing-c"
      }
    }
  },
  "Outputs": {
    "BandwidthPackageId": {
         "Value": {"Fn::GetAttr": ["BandwidthPackage","BandwidthPackageId"]}
    },
    "BandwidthPackageIps": {
         "Value": {"Fn::GetAttr": ["BandwidthPackage","BandwidthPackageIps"]}
    }
  }
}
```

#### ALIYUN::ECS::Command

**语法**

资源编排

```json
{
  "Type": "ALIYUN::ECS::Command",
  "Properties": {
    "Name": String,
    "WorkingDir": String,
    "CommandContent": String,
    "Timeout": Integer,
    "Type": String,
    "Description": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Name | String | 否 | 是 | 命令名称，支持全字符集。长度不得超过30个字符。 | 无 |
| WorkingDir | String | 否 | 是 | 您创建的命令在ECS实例中运行的目录。 | 无 |
| CommandContent | String | 否 | 否 | 命令Base64编码后的内容。 当您传入请求参数 Type 后， 必须同时传入该参数。 该参数的值必须使用Base64 编码后传输，且脚本内容的大小在 Base64编码之后不能超过16 KB。 | 无 |
| Timeout | Integer | 否 | 是 | 您创建的命令在ECS实例中执行时最大的超时时间，单位为秒。 当因为某种原因无法运行您创建的命令时，会出现超时现象；超时后，会强制终止命令进程，即取消命令的PID。 默认值：3600 | 无 |
| Type | String | 是 | 否 | 命令的类型。 取值范围： RunBatScript：创建一个在 Windows实例中运行的Bat脚本。 RunPowerShellScript：创建一个在Windows实例中运行的 PowerShell脚本。 RunShellScript：创建一个在 Linux实例中运行的Shell脚本。 | 无 |
| Description | String | 否 | 是 | 命令描述，支持全字符集。长度不得超过100个字符。 | 无 |

**返回值**

Fn::GetAtt CommandId: 命令ID。

**示例**

```
{
```

资源编排

|  | "ROSTemplateFormatVersion": "2015-09-01", "Parameters": { "WorkingDir": { "Type": "String", "Description": "The path where command will be executed in the instance." }, "CommandContent": { "Type": "String", "Description": "The content of command. Content requires base64 encoding. Maximum size support 16KB." }, "Type": { "Type": "String", "Description": "The type of command." }, "Description": { "Type": "String", "Description": "The description of command." }, "Timeout": { "Type": "Number", "Description": "Total timeout when the command is executed in the instance. Input the time unit as second. Default is 3600s." }, "Name": { "Type": "String", "Description": "The name of command." } }, "Resources": { "Command": { "Type": "ALIYUN::ECS::Command", "Properties": { "WorkingDir": { "Ref": "WorkingDir" }, "CommandContent": { "Ref": "CommandContent" }, "Type": { "Ref": "Type" }, "Description": { "Ref": "Description" }, "Timeout": { "Ref": "Timeout" }, "Name": { "Ref": "Name" } } } }, "Outputs": { "CommandId": { "Description": "The id of command created.", "Value": { "Fn::GetAtt": [ "Command", "CommandId" ] |  |
|---|---|---|
|  | > 文档版本：20260729 57 |  |

资源编排

```
      }
    }
  }
}
```

#### ALIYUN::ECS::CustomImage

**语法**

```json
{
  "Type": "ALIYUN::ECS::CustomImage",
  "Properties": {
    "Description": String,
    "InstanceId": String,
    "ImageName": String,
    "ImageVersion": String,
    "SnapshotId": String,
    "Tag": List,
    "ResourceGroupId": String,
    "Platform": String,
    "DiskDeviceMapping": List,
    "Architecture": String
  }
}
```

**属性**

| 属性名称 | 类型 | 是否必需 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Description | String | 否 | 否 | 镜像的描述。 | 长度限制在256个字符内。默认值为空。不能以http://和 https://开头。 |
| InstanceId | String | 否 | 否 | 实例ID。 | 指定该参数则表示使用实例创建自定义镜像。 |
| ImageName | String | 否 | 否 | 镜像名称。 | 长度为[2, 128]。必须以大小字母或中文开头，可包含字母、汉字、数字、下划线（ ） _ 和连字符（-）。不能以 http:// 和 https:// 开头。 |
| ImageVersion | String | 否 | 否 | 镜像版本号。 | 长度为[1, 40]。 |
| SnapshotId | String | 否 | 否 | 快照ID。 | 指定该参数则表示使用快照创建自定义镜像。 如果同时指定该参数和InstanceId，则该参数将被忽略，系统会使用实例创建自定义镜像。 |
| Tag | List | 否 | 否 | 标签。 | 无 |
| ResourceGroupId | String | 否 | 否 | 自定义镜像所在的企业资源组ID。 | 无 |
| Platform | String | 否 | 否 | 指定数据盘快照做镜像的系统盘后，需要通过Platform确定系统盘的的操作系统发行版。 | 无 |

资源编排

| DiskDeviceMappin g | List | 否 | 否 | 镜像和快照的关系。 | 无 |
|---|---|---|---|---|---|
| Architecture | String | 否 | 否 | 指定数据盘快照做镜像的系统盘后，需要通过Architecture确定系统盘的系统架构。 | 取值范围： i386 x86 64（默认） _ |

**Tag语法**

```json
"Tag": [
  {
    "Key": String,
    "Value": String
  }
```

]

**Tag属性**

| 属性名称 | 类型 | 是否必需 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Key | String | 否 | 否 | 镜像的标签键。 | 一旦传入该值，则不允许为空字符串。最多支持64个字符，不能以aliyun和acs: 开头，不能包含 http://或者 https:// 。 |
| Value | String | 否 | 否 | 镜像的标签值。 | 一旦传入该值，可以为空字符串。最多支持128个字符，不能以aliyun和acs: 开头，不能包含 http:// 或者 https:// 。 |

**DiskDeviceMapping**

```json
"DiskDeviceMapping": [
  {
    "Device": String,
    "SnapshotId": String,
    "Size": Integer,
    "DiskType": String
  }
```

]

**DiskDeviceMapping属性**

| 属性名称 | 类型 | 是否必需 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Device | String | 否 | 否 | 指定 DiskDeviceMappin g在自定义镜像中的设备名称。 | 取值范围：/dev/xvda~/dev/xvdz |
| SnapshotId | String | 否 | 否 | 根据指定的快照创建自定义镜像。 | 无 |

资源编排

| Size | Integer | 否 | 否 | DiskDeviceMappin g磁盘的大小，单位为 GiB。 | 取值范围：5~2000。 如果不指定磁盘大小，默认为快照 （DiskDeviceMapping.N. SnapshotId）的大小。 如果没有指定快照 （DiskDeviceMapping.N. SnapshotId），默认磁盘大小为5 GiB。 如果指定了磁盘大小，必须大于等于对应快照 （DiskDeviceMapping.N. SnapshotId）的大小。 |
|---|---|---|---|---|---|
| DiskType | String | 否 | 否 | 指定 DiskDeviceMappin g在新镜像中的磁盘类型。您可以通过该参数使用数据盘快照做为镜像的系统盘，如果不指定，默认为快照对应的磁盘类型。 | 取值范围： system：系统盘。 data：数据盘。 |

**返回值**

Fn::GetAtt ImageId：自定义镜像 ID。

**示例**

资源编排

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "WebServer": {
      "Type": "ALIYUN::ECS::InstanceGroup",
      "Properties": {
        "VpcId": "vpc-2zevx9ios1rszqv0a****",
        "MinAmount": 1,
        "SecurityGroupId": "sg-2ze7pxymaix640qr****",
        "ImageId": {
          "Ref": "CustomImage"
        },
        "IoOptimized": "optimized",
        "SystemDisk_Description": "SystemDisk.Description",
        "SystemDisk_DiskName": "SystemDisk.DiskName",
        "SystemDisk_Category": "cloud_ssd",
        "VSwitchId": "vsw-2zei67xd9nhcqxzec****",
        "Password": "Wenqiao****",
        "InstanceType": "ecs.n1.medium",
        "MaxAmount": 1
      }
    },
    "CustomImage": {
      "Type": "ALIYUN::ECS::CustomImage",
      "Properties": {
        "InstanceId": "i-2zefq1f3ynnrr89q****",
        "SnapshotId": "s-2ze0ibk1pvak4mw6****",
        "ImageName": "image-test-****",
        "ImageVersion": "verison-6-1"
      }
    }
  },
  "Outputs": {
    "CustomImage": {
      "Value": {
        "Fn::GetAtt": [
          "CustomImage",
          "ImageId"
```

]

```json
      }
    },
    "InstanceIds": {
      "Value": {
        "Fn::GetAtt": [
          "WebServer",
          "InstanceIds"
```

]

```
      }
    }
  }
}
```

#### ALIYUN::ECS::DedicatedHost

**语法**

资源编排

```json
{
  "Type": "ALIYUN::ECS::DedicatedHost",
  "Properties": {
    "DedicatedHostType": String,
    "DedicatedHostName": String,
    "AutoReleaseTime": String,
    "Description": String,
    "AutoPlacement": String,
    "Tags": List,
    "ActionOnMaintenance": String,
    "NetworkAttributesSlbUdpTimeout": Integer,
    "ChargeType": String,
    "ResourceGroupId": String,
    "ZoneId": String,
    "NetworkAttributesUdpTimeout": Integer,
    "Quantity": Integer
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| DedicatedHostT ype | String | 是 | 否 | 专有宿主机规格。 | 无。 |
| DedicatedHostN ame | String | 否 | 否 | 专有宿主机的名称。 | 长度为2~128 个英文或中文字符。 必须以大小字母或中文开头，不能以 http:// 或 https:// 开头。 可以包含数字、 半角冒号、下划线和连字符。 |
| AutoReleaseTim e | String | 否 | 否 | 自动释放时间。如果不输入 AutoReleaseTim e 参数，表示取消自动释放，专有宿主机在预约时间点不再自动释放。 最短不能晚于当前时间半小时内。 最长不能超过当前时间三年以后。 如果秒 （ ss ）取值不是 00 ， 则自动取为当前分钟（ mm ） 开始时刻。 | 无。 |
| Description | String | 否 | 否 | 专有宿主机的描述。 | 无。 |

资源编排

| ZoneId |  | String |  |  | 否 |  |  | 否 |  |  | 专有宿主机所属的可用区。 默认值：空，表示由系统选择。 |  | 无。 |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ChargeType |  | String |  |  | 否 |  |  | 否 |  |  | 专有宿主机的计费方式。 |  | 取值范围： PostPaid：按量付费。 |  |  |
| AutoPlacement |  | String |  |  | 否 |  |  | 否 |  |  | 专有宿主机是否加入自动部署资源池。当您在专有宿主机上创建实例， 却不指定 DedicatedHostId 时，阿里云将自动从加入资源池的专有宿主机中，为您选取适合的宿主机部署实例。 |  | 取值范围： on off 说明若您不设置该参数，则默认为专有宿主机加入自动部署资源池。 若您不希望专有宿主机加入自动部署资源池，请将该参数设置为 off。 |  |  |
| Tags |  | List |  |  | 否 |  |  | 否 |  |  |  |  | 最多支持20个标签，格式： [{"Key": |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | [{"Key": |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | "tagKey", |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | "Value": |  |  |
|  |  |  |  |  |  |  |  |  |  |  | 用户自定义标签。 |  | "tagValue"}, |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | {"Key": |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | "tagKey2", |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | "Value": |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | "tagValue2"}] |  |  |
| ActionOnMainte nance |  | String |  |  | 否 |  |  | 否 |  |  | 当专有宿主机发生故障或者在线修复时，为其所宿实例设置迁移方案。 |  | 取值范围： Migrate：迁移实例到其他物理机并重新启动实例。 Stop：在当前专有宿主机上停止实例，确认无法修复专有宿主机后，迁移实例到其他物理机并重新启动实例。 当专有宿主机上挂载云盘存储时默认值为Migrate，当专有宿主机上挂载本地盘存储时默认值为Stop。 |  |  |
| NetworkAttribut esSlbUdpTimeou t |  | Integer |  |  | 否 |  |  | 否 |  |  | 负载均衡连接的 UDP会话超时时间。 |  | 取值范围： 15~310。 单位：秒。 |  |  |
| ResourceGroupI d |  | String |  |  | 否 |  |  | 否 |  |  | 专有宿主机要加入的资源组ID。 |  | 无。 |  |  |

资源编排

| NetworkAttribut esUdpTimeout | Integer | 否 | 否 | 为专有宿主机上运行的云服务设置用户访问的UDP会话超时时间。 | 取值范围： 15~310。 单位：秒。 |
|---|---|---|---|---|---|
| Quantity | Integer | 否 | 否 | 本次创建的专有宿主机的数量。 | 取值范围： 1~100。 默认值：1。 |

**返回值**

Fn::GetAtt OrderId: 订单ID。 DedicatedHostIds：主机ID列表。

**示例**

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "AutoRenewPeriod": {
      "Type": "Number",
      "Description": "The time period of auto renew. When the parameter InstanceChargeType is
PrePaid, it will take effect.It could be 1, 2, 3, 6, 12\. Default value is 1.",
      "AllowedValues": [
```

`1,` `2,` `3,` `6,` `],`

```json
      "Default": 1
    },
    "Description": {
      "Type": "String",
      "Description": "The description of host."
    },
    "ZoneId": {
      "Type": "String",
      "Description": "The zone to create the host."
    },
    "DedicatedHostName": {
      "Type": "String",
      "Description": "The name of the dedicated host, [2, 128] English or Chinese characters. It must
begin with an uppercase/lowercase letter or a Chinese character, and may contain numbers, '_' or '-'. It cannot begin with http:// or https://."
    },
    "ChargeType": {
      "Type": "String",
      "Description": "Instance Charge type, allowed value: Prepaid and Postpaid. If specified
Prepaid, please ensure you have sufficient balance in your account. Or instance creation will be fail ure. Default value is Postpaid.",
      "AllowedValues": [
        "PrePaid",
        "PostPaid"
```

`],`

```json
      "Default": "PostPaid"
    },
    "AutoRenew": {
      "Type": "String",
      "Description": "Whether renew the fee automatically? When the parameter InstanceChargeType is P
rePaid, it will take effect. Range of value:True: automatic renewal.False: no automatic renewal. Defa
```

资源编排

```json
ult value is False.",
      "AllowedValues": [
        "True",
        "False"
```

`],`

```json
      "Default": "False"
    },
    "Period": {
      "Type": "Number",
      "Description": "Prepaid time period. Unit is month, it could be from 1 to 9 or 12, 24, 36, 48,
60\. Default value is 1.",
      "AllowedValues": [
```

`1,` `2,` `3,` `4,` `5,` `6,` `7,` `8,` `9,`

```
        12,
        24,
        36,
        48,
```

`],`

```json
      "Default": 1
    },
    "DedicatedHostType": {
      "Type": "String",
      "Description": "The instance type of host."
    },
    "PeriodUnit": {
      "Type": "String",
      "Description": "Unit of prepaid time period, it could be Week/Month. Default value is Month.",
      "AllowedValues": [
        "Week",
        "Month"
```

`],`

```json
      "Default": "Month"
    },
    "AutoReleaseTime": {
      "Type": "String",
      "Description": "Auto release time for created host, Follow ISO8601 standard using UTC time. for
mat is 'yyyy-MM-ddTHH:mm:ssZ'. Not bigger than 3 years from this day onwards"
    }
  },
  "Resources": {
    "Host": {
      "Type": "ALIYUN::ECS::DedicatedHost",
      "Properties": {
          "Description": {
          "Ref": "Description"
        },
        "ZoneId": {
          "Ref": "ZoneId"
        },
        "DedicatedHostName": {
          "Ref": "DedicatedHostName"
        },
        "ChargeType": {
"Ref" "ChargeTpe"
```

资源编排

```json
          "Ref": "ChargeType"
        },
          "DedicatedHostType": {
          "Ref": "DedicatedHostType"
        },
        "PeriodUnit": {
          "Ref": "PeriodUnit"
        },
        "AutoReleaseTime": {
          "Ref": "AutoReleaseTime"
        }
      }
    }
  },
  "Outputs": {
    "OrderId": {
      "Description": "The order id list of created instance.",
      "Value": {
        "Fn::GetAtt": [
          "Host",
          "OrderId"
```

]

```json
      }
    },
    "DedicatedHostIds": {
      "Description": "The host id list of created hosts",
      "Value": {
        "Fn::GetAtt": [
          "Host",
          "DedicatedHostIds"
```

]

```
      }
    }
  }
}
```

#### ALIYUN::ECS::Disk

**语法**

资源编排

```json
{
  "Type": "ALIYUN::ECS::Disk",
  "Properties": {
    "StorageSetId": String,
    "Description": String,
    "Tags": List,
    "AutoSnapshotPolicyId": String,
    "Encrypted": Boolean,
    "DiskName": String,
    "DiskCategory": String,
    "ResourceGroupId": String,
    "KMSKeyId": String,
    "DeleteAutoSnapshot": Boolean,
    "SnapshotId": String,
    "StorageSetPartitionNumber": Integer,
    "PerformanceLevel": String,
    "ZoneId": String,
    "Size": Integer,
    "BurstingEnabled": Boolean,
    "ProvisionedIops": Integer,
    "MultiAttach": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ResourceGro upId | String | 否 | 是 | 云盘所在的资源组ID。 | 无 |
| ZoneId | String | 是 | 否 | 可用区ID。 | 无 |
| DiskName | String | 否 | 否 | 云盘的名称。 | 长度为2~128个字符。必须以英文字母或汉字开头，不能以 http:// 或 https:// 开头。可包含英文字母、汉字、数字、半角句号（.）、下划线（ ）和 _ 短划线（-）。 |
| Description | String | 否 | 否 | 云盘的描述。 | 长度为2~256个字符。不能以 http:// 或 https:// 开头。 |
| Tags | List | 否 | 否 | 标签。 | 最多支持20个标签。 更多信息，请参见Tags属性。 |
| DiskCategory | String | 否 | 否 | 云盘的类型。 | 取值： cloud（默认值）：普通云盘。 cloud efficiency：高效云盘。 _ cloud ssd：SSD云盘。 _ cloud essd：ESSD云盘。 _ |
| SnapshotId | String | 否 | 否 | 快照ID。 | 同时指定该参数和Size时，以该参数取值为准。 实际创建的云盘大小为指定快照的大小。 说明 2013年07月15 日及以前创建的快照不能用来创建云盘。 |

资源编排

| PerformanceL evel | String | 否 | 否 | ESSD云盘性能等级。 | 取值： PL0：单盘最高随机读写IOPS 1 万。 PL1（默认值）：单盘最高随机读写IOPS 5万。 PL2：单盘最高随机读写IOPS 10 万。 PL3：单盘最高随机读写IOPS 100万。 |
|---|---|---|---|---|---|
| Size | Integer | 否 | 否 | 云盘的大小。 | 取值范围： cloud：5~2000。 cloud efficiency： _ 20~32,768。 cloud ssd：20~32,768。 _ cloud essd：20~32,768。 _ 单位：GiB。 指定该参数后，其取值必须大于或等于指定快照的大小。 |
| BurstingEnabl ed | Boolean | 否 | 否 | 是否启用突发。 | 取值： true：启用。 false（默认值）：禁用。 |
| ProvisionedIo ps | Integer | 否 | 否 | 预配的IOPS。 | 无 |
| AutoSnapshot PolicyId | String | 否 | 否 | 自动快照策略 ID。 | 无 |
| Encrypted | Boolean | 否 | 否 | 是否加密云盘。 | 取值： true：加密。 false（默认值）：不加密。 |
| DeleteAutoSn apshot | Boolean | 否 | 否 | 删除云盘时是否删除自动快照。 | 取值范围： true（默认值）：删除云盘时同步删除自动快照。 false：删除云盘时不删除自动快照。 |
| StorageSetId | String | 否 | 否 | 存储集ID。 | 无 |
| KMSKeyId | String | 否 | 否 | 云盘使用的 KMS密钥ID。 | 无 |
| StorageSetPa rtitionNumber | Integer | 否 | 否 | 存储集分区数。 | 无 |
| MultiAttach | String | 否 | 否 | 是否开启多重挂载特性。 | 取值： Disabled（默认值）：不开启。 Enabled : 开启。目前仅ESSD云盘支持设置为Enabled。 说明开启多重挂载特性的云盘只支持按量付费。 |

**Tags语法**

资源编排

```json
"Tags" : [
  {
    "Value" : String,
    "Key" : String
  }
```

]

**Tags属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Key | String | 是 | 否 | 标签键。 | 长度为1~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或 https:// 。 |
| Value | String | 否 | 否 | 标签值。 | 长度为0~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或 https:// 。 |

**返回值**

Fn::GetAtt DiskId：云盘ID。 Status：云盘状态。

**示例**

`YAML` 格式

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  ZoneId:
    AssociationProperty: ALIYUN::ECS::Instance:ZoneId
    Type: String
    Label:
```

`zh-cn:` 交换机可用区

```
      en: VSwitch Availability Zone
Resources:
  DataDisk:
    Properties:
      Size: 10
      ZoneId:
        Ref: ZoneId
      DiskName: DataDisk
Outputs:
  DiskId:
    Value:
      Fn::GetAtt:
        - DataDisk
        - DiskId
  Status:
    Value:
      Fn::GetAtt:
        - DataDisk
        - Status
```

`JSON` 格式资源编排

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "ZoneId": {
      "AssociationProperty": "ALIYUN::ECS::Instance:ZoneId",
      "Type": "String",
      "Label": {
```

`"zh-cn": "`交换机可用区`",`

```json
        "en": "VSwitch Availability Zone"
      }
    }
  },
  "Resources": {
    "DataDisk": {
      "Type": "ALIYUN::ECS::Disk",
      "Properties": {
        "Size": 10,
        "ZoneId": {
          "Ref": "ZoneId"
        },
        "DiskName": "DataDisk"
      }
    }
  },
  "Outputs": {
    "DiskId": {
      "Value": {
        "Fn::GetAtt": [
          "DataDisk",
          "DiskId"
```

]

```json
      }
    },
    "Status": {
      "Value": {
        "Fn::GetAtt": [
          "DataDisk",
          "Status"
```

]

```
      }
    }
  }
}
```

更多示例，请参见：JSON示例和YAML示例。

#### ALIYUN::ECS::DiskAttachment

**语法**

资源编排

```json
{
  "Type": "ALIYUN::ECS::DiskAttachment",
  "Properties": {
    "InstanceId": String,
    "Device": String,
    "DeleteWithInstance": Boolean,
    "DiskId": String,
    "DeleteAutoSnapshot": Boolean
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| InstanceId | String | 是 | 否 | 需挂载磁盘的实例 ID | 无 |
| DiskId | String | 是 | 否 | 磁盘ID | 磁盘和ECS实例必须在同一个可用区。 |
| Device | String | 否 | 否 | 磁盘设备名 | 如不指定，则默认由系统按顺序分配，即从 /dev/xvdb 到 /dev/xvdz。 |
| DeleteWithInsta nce | Boolean | 否 | 否 | 磁盘是否随实例释放 | 取值： true：释放实例时，该磁盘随实例一起释放。 false：释放实例时，保留该磁盘，不随实例一起释放。 |
| DeleteAutoSnap shot | Boolean | 否 | 否 | 删除磁盘时是否删除自动快照 | 取值： true（默认值） false |

**返回值**

Fn::GetAtt DiskId：新建磁盘的ID。 Status：新建磁盘的状态。 Device：磁盘设备名。

**示例**

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "DiskAttachment": {
      "Type": "ALIYUN::ECS::DiskAttachment",
      "Properties": {
        "InstanceId": {
          "Ref": "InstanceId"
        },
        "Device": {
          "Ref": "Device"
        },
        "DeleteWithInstance": {
"Ref" "DeleteWithInstance"
```

资源编排

```json
          "Ref": "DeleteWithInstance"
        },
        "DiskId": {
          "Ref": "DiskId"
        }
      }
    }
  },
  "Parameters": {
    "InstanceId": {
      "Type": "String",
      "Description": "The instanceId to attach the disk."
    },
    "Device": {
      "Type": "String",
      "Description": "The device where the volume is exposed on the instance. could be /dev/xvd[a-z].
If not specification, will use default value."
    },
    "DeleteWithInstance": {
      "Type": "Boolean",
      "Description": "If property is true, the disk will be deleted while instance is deleted, if pro
perty is false, the disk will be retain after instance is deleted.",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

]

```json
    },
    "DiskId": {
      "Type": "String",
      "Description": "The disk id to attached."
    }
  },
  "Outputs": {
    "Status": {
      "Description": "The disk status now.",
      "Value": {
        "Fn::GetAtt": [
          "DiskAttachment",
          "Status"
```

]

```json
      }
    },
    "Device": {
      "Description": "The device where the volume is exposed on ecs instance.",
      "Value": {
        "Fn::GetAtt": [
          "DiskAttachment",
          "Device"
```

]

```json
      }
    },
    "DiskId": {
      "Description": "The disk id of created disk",
      "Value": {
        "Fn::GetAtt": [
          "DiskAttachment",
          "DiskId"
```

]

```
      }
    }
  }
```

资源编排

```
}
```

#### ALIYUN::ECS::ForwardEntry

**语法**

```json
{
  "Type": "ALIYUN::ECS::ForwardEntry",
  "Properties": {
    "ExternalIp": String,
    "ExternalPort": String,
    "ForwardTableId": String,
    "InternalIp": String,
    "IpProtocol": String,
    "InternalPort": String,
    "PortBreak": Boolean,
    "ForwardEntryName": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ExternalIp | String | 是 | 否 | 公网IP | ExternalIp必须已加入该DNAT所属 NAT网关上的共享带宽包。 |
| ExternalPort | String | 是 | 否 | 连接公网的端口 | 取值范围： 1~65,535。 |
| ForwardTableId | String | 是 | 否 | DNAT表的ID | 无 |
| InternalIp | String | 是 | 否 | 转发请求的目标IP | InternalIp是私网 IP。 |
| IpProtocol | String | 是 | 否 | 协议类型 | 取值： TCP UDP Any |
| InternalPort | String | 是 | 否 | 目标私网端口 | 取值范围： 1~65,535。 |

资源编排

| PortBreak | Boolean | 否 | 否 | 是否开启端口突破 | 取值： true：开启端口突破。 false（默认值）：不开启端口突破。 说明当DNAT条目和SNAT条目使用同一个公网IP地址时， 如果您想配置大于1024的端口号，您需要指定 PortBreak为 true。 |
|---|---|---|---|---|---|
| ForwardEntryNa me | String | 否 | 否 | DNAT规则的名称 | 长度为2~128个字符，必须以英文字母或汉字开头，但不能以 http:// 或 https:// 开头。 |

|  | http:// |
|---|---|
| https:// |  |

**返回值**

Fn::GetAtt ForwardEntryId：DNAT中每一个条目的ID。

**示例**

`JSON` 格式

```json
{
  "Parameters": {
    "ExternalPort": {
      "Type": "String",
      "Description": "Source port, now support [1-65535]|Any|x/y"
    },
    "ExternalIp": {
      "Type": "String",
      "Description": "Source IP, must belongs to bandwidth package internet IP"
    },
    "IpProtocol": {
      "Type": "String",
      "Description": "Supported protocol, Now support 'TCP|UDP|Any'",
      "AllowedValues": [
        "TCP",
        "UDP",
        "Any"
```

]

```json
    },
    "PortBreak": {
      "Type": "Boolean",
"Description":"Specifieswhethertoremovelimitsontheportrange.",
```

资源编排

```json
      Description: Specifies whether to remove limits on the port range.,
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

]

```json
    },
    "InternalPort": {
      "Type": "String",
      "Description": "Destination port, now support [1-65535]|Any|x/y"
    },
    "ForwardEntryName": {
      "Type": "String",
      "Description": "the name of the DNAT rule is 2-128 characters long and must start with a letter
or Chinese, but cannot begin with HTTP:// or https://."
    },
    "InternalIp": {
      "Type": "String",
      "Description": "Destination IP, must belong to VPC private IP"
    },
    "ForwardTableId": {
      "Type": "String",
      "Description": "Create forward entry in specified forward table."
    }
  },
  "ROSTemplateFormatVersion": "2015-09-01",
  "Outputs": {
    "ForwardEntryId": {
      "Description": "The id of created forward entry.",
      "Value": {
        "Fn::GetAtt": [
          "ForwardTableEntry",
          "ForwardEntryId"
```

]

```json
      }
    }
  },
  "Resources": {
    "ForwardTableEntry": {
      "Type": "ALIYUN::ECS::ForwardEntry",
      "Properties": {
        "ExternalPort": {
          "Ref": "ExternalPort"
        },
        "ExternalIp": {
          "Ref": "ExternalIp"
        },
        "IpProtocol": {
          "Ref": "IpProtocol"
        },
        "PortBreak": {
          "Ref": "PortBreak"
        },
        "InternalPort": {
          "Ref": "InternalPort"
        },
        "ForwardEntryName": {
          "Ref": "ForwardEntryName"
        },
        "InternalIp": {
          "Ref": "InternalIp"
        },
```

资源编排

```json
        "ForwardTableId": {
          "Ref": "ForwardTableId"
        }
      }
    }
  }
}
```

`YAML` 格式

```
Parameters:
  ExternalPort:
    Type: String
    Description: 'Source port, now support [1-65535]|Any|x/y'
  ExternalIp:
    Type: String
    Description: 'Source IP, must belongs to bandwidth package internet IP'
  IpProtocol:
    Type: String
    Description: 'Supported protocol, Now support ''TCP|UDP|Any'''
    AllowedValues:
      - TCP
      - UDP
      - Any
  PortBreak:
    Type: Boolean
    Description: Specifies whether to remove limits on the port range.
    AllowedValues:
      - 'True'
      - 'true'
      - 'False'
      - 'false'
  InternalPort:
    Type: String
    Description: 'Destination port, now support [1-65535]|Any|x/y'
  ForwardEntryName:
    Type: String
    Description: >-
      the name of the DNAT rule is 2-128 characters long and must start with a
      letter or Chinese, but cannot begin with HTTP:// or https://.
  InternalIp:
    Type: String
    Description: 'Destination IP, must belong to VPC private IP'
  ForwardTableId:
    Type: String
    Description: Create forward entry in specified forward table.
ROSTemplateFormatVersion: '2015-09-01' Outputs:
  ForwardEntryId:
    Description: The id of created forward entry.
    Value:
      'Fn::GetAtt':
        - ForwardTableEntry
        - ForwardEntryId
Resources:
  ForwardTableEntry:
    Properties:
      ExternalPort:
        Ref: ExternalPort
      ExternalIp:
        Ref: ExternalIp
```

资源编排

```
      IpProtocol:
        Ref: IpProtocol
      PortBreak:
        Ref: PortBreak
      InternalPort:
        Ref: InternalPort
      ForwardEntryName:
        Ref: ForwardEntryName
      InternalIp:
        Ref: InternalIp
      ForwardTableId:
        Ref: ForwardTableId
```

更多示例，请参见JSON示例和YAML示例。

#### ALIYUN::ECS::Instance

**语法**

```json
{
  "Type": "ALIYUN::ECS::Instance",
  "Properties": {
    "RamRoleName": String,
    "IoOptimized": String,
    "PrivateIpAddress": String,
    "KeyPairName": String,
    "SystemDiskDiskName": String,
    "Description": String,
    "Tags": List,
    "HostName": String,
    "ImageId": String,
    "ResourceGroupId": String,
    "VSwitchId": String,
    "Password": String,
    "InstanceType": String,
    "SystemDiskCategory": String,
    "UserData": String,
    "SystemDiskSize": Number,
    "ZoneId": String,
    "VpcId": String,
    "InstanceName": String,
    "InternetMaxBandwidthIn": Integer,
    "DeletionProtection": Boolean,
    "DeploymentSetId": String,
    "SecurityGroupId": String,
    "HpcClusterId": String,
    "SystemDiskDescription": String,
    "DiskMappings": List
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ResourceGroupId | String | 否 | 否 | 实例所在的资源组 ID。 | 无。 |

资源编排

| ImageId | String | 是 | 是 | ECS实例的镜像ID， 包括公共镜像、自定义镜像和云市场镜像。 | 在编辑模板时，只需要指定镜像类型或者镜像类型和版本，ROS就会自动选择适配的公共镜像ID。 可以用星号通配符 （*） 指代镜像ID 的某一部分。 以所有阿里云提供的Ubuntu的公共镜像为例，在给ECS实例指定公共镜像ID时，规则如下： 指定ubuntu，最终会匹配 ubuntu16 0402 64 20G aliba _ _ _ _ se 20170818.vhd。 _ 指定ubuntu 14，最终会匹配 _ ubuntu 14 0405 64 20G alib _ _ _ _ _ ase 20170824.vhd。 _ 指定ubuntu*14*32，最终会匹配 ubuntu 14 0405 32 40G alib _ _ _ _ _ ase 20170711.vhd。 _ 指定 ubuntu 16 0402 32，最 _ _ _ 终会匹配 ubuntu 16 0402 32 40G alib _ _ _ _ _ ase 20170711.vhd。 _ |
|---|---|---|---|---|---|
| InstanceType | String | 是 | 否 | ECS实例规格。 | 无。 |
| SecurityGroupId | String | 是 | 否 | 新建实例所属安全组。 | 无。 |
| Description | String | 否 | 否 | 描述信息。 | 最长256个字符。 |
| InstanceName | String | 否 | 否 | 实例名称。 | 最长128个字符，可包含英文、中文、数字、下划线（ ）、点（.）、 _ 连字符（-）。 |
| Password | String | 否 | 否 | ECS实例登录密码。 | 字符长度为8~30。 必须同时包含：大、小写字母，数字和特殊符号。 支持以下特殊字符：( ) ‘ ~ ! @ # $ % ^ & * - + = \| { } [ ] : ; ‘ < > , . ? / - 。如果指定该参数，请务必使用 HTTPS 协议调用 API， 以避免密码泄露。 |
| HostName | String | 否 | 否 | 云服务器的主机名。 | 最少2个字符。 点（.）和连字符（-）不能作为 hostname的首尾字符，且不能连续使用。 Windows平台支持最长15个字符， 支持字母（不限制大小写）、数字和连字符（-）；不支持点号（.）；不能全是数字。 其它（Linux 等）平台支持最长30个字符，支持多个点号（.），点之间为一段；每段可以由大小写字母、数字和连字符（-）组成。 |
| PrivateIpAddress | String | 否 | 否 | 在VPC网络环境下， 指定内网IP。IP地址不能与VPC网络下的其它实例重复。 | 无。 |
| InternetMaxBand widthIn | Integer | 否 | 否 | 公网最大入网带宽。 | 取值范围：1~100。 默认值：100。 单位：Mbps。 |

资源编排

| IoOptimized |  | String | 否 |  | 否 |  | 指定是否创建I/O优化实例。 | 取值范围： none（非 I/O 优化） optimized（I/O 优化） 默认值：none。 |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
| DiskMappings |  | List | 否 |  | 否 |  | 指定需要挂载的磁盘。 | 最多支持16块磁盘。 |  |  |
| SystemDiskCateg ory |  | String | 否 |  | 否 |  | 指定系统盘类型。 | 取值范围： cloud cloud efficiency _ cloud ssd _ ephemeral ssd _ |  |  |
| SystemDiskDescri ption |  | String | 否 |  | 否 |  | 系统盘描述信息。 | 无。 |  |  |
| SystemDiskDiskN ame |  | String | 否 |  | 否 |  | 系统盘名称。 | 无。 |  |  |
| SystemDiskSize |  | Number | 否 |  | 是 |  | 系统盘大小。单位： GB。 | 取值范围：40~500。 如果使用自定义镜像创建系统盘，需要保证系统盘大于自定义镜像大小。 |  |  |
| Tags |  | List | 否 |  | 否 |  |  | 最多支持 20 个标签，格式： [{“Key”:”tagKey”,”Value |  |  |
|  |  |  |  |  |  |  |  |  | [{“Key”:”tagKey”,”Value |  |
|  |  |  |  |  |  |  | 用户自定义标签。 | ”:”tagValue”}, |  |  |
|  |  |  |  |  |  |  |  | {“Key”:”tagKey2”,”Value”:”ta |  |  |
|  |  |  |  |  |  |  |  | gValue2”}] |  |  |
| UserData |  | String | 否 |  | 否 |  | 创建ECS实例时传递的用户数据。 | 内容需要限制在16KB以内，不需要 Base64，特殊字符需要使用 \ 转义。 |  |  |
| ZoneId |  | String | 否 |  | 否 |  | 可用区ID。 | 无。 |  |  |
| HpcClusterId |  | String | 否 |  | 否 |  | 实例所属的HPC集群 ID。 | 无。 |  |  |
| VpcId |  | String | 否 |  | 否 |  | VPC ID。 | 无。 |  |  |
| VSwitchId |  | String | 否 |  | 否 |  | VSwitch ID。 | 无。 |  |  |
| KeyPairName |  | String | 否 |  | 否 |  | ECS实例绑定的密钥对名称。 | Windows系统保留默认值为空。 在Linux系统中，如果指定该参数，Password的内容仍旧会被设置到实例中，但是密码登录方式会默认被禁止，采用密钥对验证登录。 |  |  |
| RamRoleName |  | String | 否 |  | 否 |  | 实例RAM角色名称。可以调用 ListRoles查询。 | 无。 |  |  |
| DeletionProtectio n |  | Boolean | 否 |  | 否 |  | 实例释放保护属性， 指定是否支持通过控制台或 API（DeleteInstan ce）释放实例。 | 取值范围： True False |  |  |
| DeploymentSetId |  | String | 否 |  | 是 |  | 部署集ID。 | 无。 |  |  |

**DiskMappings语法**

资源编排

```json
"DiskMappings": [
  {
    "Category": String,
    "DiskName": String,
    "Description": String,
    "Device": String,
    "SnapshotId": String,
    "Size": String
  }
```

]

**DiskMappings属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Size | String | 是 | 否 | 数据盘大小，单位： GB。 | 无。 |
| Category | String | 否 | 否 | 数据盘的类型。 | 取值范围： cloud cloud efficiency _ cloud ssd _ ephemeral ssd _ 默认值：cloud。 |
| DiskName | String | 否 | 否 | 数据盘的名称。 | 最长128个字符，可包含英文、中文、数字、下划线 （ ）、点（.）、连字符 _ （-）。 |
| Description | String | 否 | 否 | 描述信息。 | 取值范围：2~256，默认值为空。 |
| Device | String | 否 | 否 | 指定数据盘的设备名称。 | 如不指定，则默认由系统按顺序分配，即从/dev/xvdb 到/dev/xvdz。 |
| SnapshotId | String | 否 | 否 | 创建数据盘使用的快照。 | 无。 |

**Tags语法**

```json
"Tags": [
  {
    "Value": String,
    "Key": String
  }
```

]

**Tags属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Key | String | 是 | 否 | 无。 | 无。 |
| Value | String | 否 | 否 | 无。 | 无。 |

**返回值**

Fn::GetAtt InstanceId：实例ID。由系统生成，实例的全局唯一标识。 PrivateIp：VPC类型实例的私网IP。当NetworkType为VPC时，该参数生效。 资源编排 InnerIp：Classic类型实例的私网IP。当NetworkType为Classic时，该参数生效。 PublicIp：Classic类型实例的公网IP列表。当NetworkType为Classic时，该参数生效。 ZoneId：可用区ID。 HostName：实例的主机名称。

**示例**

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "WebServer": {
      "Type": "ALIYUN::ECS::Instance",
      "Properties": {
        "ImageId": "m-25l0rc****",
        "InstanceType": "ecs.t1.small",
        "SecurityGroupId": "sg-25zwc****",
        "ZoneId": "cn-beijing-b",
        "Tags": [{
            "Key": "tiantt",
            "Value": "ros"
        },{
            "Key": "tiantt1",
            "Value": "ros1"
        }
```

]

```json
      }
    }
  },
  "Outputs": {
    "InstanceId": {
         "Value": {"get_attr": ["WebServer","InstanceId"]}
    },
    "PublicIp": {
         "Value": {"get_attr": ["WebServer","PublicIp"]}
    }
  }
}
```

#### ALIYUN::ECS::InstanceClone

**语法**

资源编排

```json
{
  "Type": "ALIYUN::ECS::InstanceClone",
  "Properties": {
    "DeletionProtection": Boolean,
    "DiskMappings": List,
    "LoadBalancerIdToAttach": String,
    "Description": String,
    "BackendServerWeight": Integer,
    "Tags": List,
    "SecurityGroupId": String,
    "RamRoleName": String,
    "ImageId": String,
    "ResourceGroupId": String,
    "SpotPriceLimit": String,
    "InstanceChargeType": String,
    "SourceInstanceId": String,
    "Period": Number,
    "SpotStrategy": String,
    "Password": String,
    "InstanceName": String,
    "InternetMaxBandwidthIn": Integer,
    "ZoneId": String,
    "KeyPairName": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ResourceGroup Id | String | 否 | 否 | 实例所在的资源组ID。 | 无。 |
| SourceInstance Id | String | 是 | 否 | 待克隆的源ECS实例的 ID。 | 克隆实例规格、镜像、带宽收费方式、 带宽限制、网络类型等所有实例数据和设置。如果源ECS实例加入多个安全组，新实例会加入源实例的第一个安全组。 |
| BackendServer Weight | Integer | 否 | 否 | ECS实例在负载均衡器实例中的权重。 | 取值范围：[0, 100]，默认值是100。 |
| LoadBalancerId ToAttach | String | 否 | 否 | ECS实例待加入的负载均衡实例的ID。 | 无。 |
| Description | String | 否 | 否 | 描述信息。 | 最长256个字符。 |

资源编排

| ImageId | String | 否 | 是 | 用于启动ECS实例的镜像 ID，包括公共镜像、自定义镜像和云市场镜像。 | 在编辑模板时，仅需指定镜像的类型， 或类型和版本，ROS会自动选择适配的公共镜像ID。 可以用星号通配符 （\*） 指代镜像ID的某一部分。 以阿里云提供的全部Ubuntu公共镜像为例，在为ECS实例指定公共镜像ID时， 可以按照如下方式： 指定：ubuntu 最终会匹配： ubuntu16 0402 64 20G alibase 2 _ _ _ _ _ 0170818.vhd 指定：ubuntu 14 _ 最终会匹配： ubuntu 14 0405 64 20G alibase _ _ _ _ _ _ 20170824.vhd 指定：ubuntu*14*32 最终会匹配： ubuntu 14 0405 32 40G alibase _ _ _ _ _ _ 20170711.vhd 指定：ubuntu 16 0402 32 _ _ _ 最终会匹配： ubuntu 16 0402 32 40G alibase _ _ _ _ _ _ 20170711.vhd |
|---|---|---|---|---|---|
| SecurityGroupI d | String | 否 | 否 | 新建实例所属安全组。 | 无。 |
| InstanceName | String | 否 | 否 | 实例名称。 | 最长128个字符，可包含英文、中文、 数字、下划线（ ）、点（.）、连字符 _ （-）。 |
| Password | String | 否 | 否 | ECS实例登录密码。 | 长度为 [8, 30]。 必须同时包含大写或小写字母、数字和特殊字符。 特殊字符包括以下：( ) ' ~ ! @ # $ % ^ & * - + = \| { } [ ] : ; ‘ < > , . ? /。 如果指定该参数，必须使用HTTPS协议调用API，以免密码泄露。 |
| DiskMappings | List | 否 | 否 | 需要挂载的磁盘。 | 最多支持16块磁盘。 |
| Tags | List | 否 | 否 | 用户自定义标签。 | 最多支持20个标签，格式: [{"Key":"tagKey","Value":"tagValu e"}、 {"Key":"tagKey2","Value":"tagValu e2"}]。 |
| ZoneId | String | 否 | 否 | 可用区ID。 | 无 |
| InstanceCharge Type | String | 否 | 否 | 实例的付费方式。 | 可选值：Prepiad、Postpaid。 默认值：Postpaid。如果指定为 Prepaid，必须确保余额充足，否则创建失败。 |

资源编排

| Period | Number | 否 | 否 | 若 `InstanceChargeType ` 为 Prepaid，必须设置此参数；若 `InstanceChargeType ` 为 Postpaid，忽略此参数。 | 可选值：1-9、12、24、36，单位： 月。 |
|---|---|---|---|---|---|
| KeyPairName | String | 否 | 否 | ECS实例绑定的密钥对名称。 | Windows系统保留默认值为空。 在Linux系统中，如果指定该参数，Password的内容仍旧会被设置到实例中，但是密码登录方式会默认被禁止，采用密钥对验证登录。 |
| RamRoleName | String | 否 | 否 | 实例RAM角色名称。可以调用ListRoles查询。 | 无 |
| SpotPriceLimit | String | 否 | 否 | 设置实例的每小时最高价格。 | 支持最多3位小数，参数SpotStrategy取值为 SpotWithPriceLimit 时该参数生效。 |
| SpotStrategy | String | 否 | 否 | 按量付费实例的竞价策略。 | 参数 InstanceChargeType取值为 PostPaid 时生效。取值范围： NoSpot：正常按量付费实例。 SpotWithPriceLimit：设置上限价格的竞价实例。 SpotAsPriceGo：系统自动出价，最高不超过按量付费价格。 默认值：NoSpot。 |
| InternetMaxBa ndwidthIn | Integer | 否 | 否 | 公网入带宽最大值，单位为Mbit/s。 | 取值范围：[1,200]。 |
| DeletionProtect ion | Boolean | 否 | 否 | 实例释放保护属性，指定是否支持通过控制台或 API （DeleteInstance） 释放实例。 | 可用值：true、false。 |

**DiskMappings 语法**

```json
"DiskMappings": [
  {
    "Category": String,
    "DiskName": String,
    "Description": String,
    "Device": String,
    "SnapshotId": String,
    "Size": String
  }
```

]

**DiskMappings 属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Size | String | 是 | 否 | 数据盘大小，单位：GB。 | 无 。 |

资源编排

| Category | String | 否 | 否 | 数据盘类型。 | 可选值：cloud、 cloud efficiency、 _ cloud ssd、 _ ephemeral ssd。 _ 默认值：cloud。 |
|---|---|---|---|---|---|
| DiskName | String | 否 | 否 | 据盘名称。 | 最长128个字符，可包含英文、中文、数字、下划线 （ ）、点（.）、连字符 _ （-）。 |
| Description | String | 否 | 否 | 描述信息。 | 取值范围：[2, 256]，默认值为空。 |
| Device | String | 否 | 否 | 指定数据盘的设备名称。 | 如不指定，则默认由系统按顺序分配，即从/dev/xvdb 到/dev/xvdz。 |
| SnapshotId | String | 否 | 否 | 创建数据盘使用的快照。 | 无。 |

**Tags 语法**

```json
"Tags": [
  {
    "Value": String,
    "Key": String
  }
```

]

**Tags 属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Key | String | 是 | 否 | 标签键 ，不允许为空字符串。 最多支持64个字符，不能以 aliyun和acs:开头，不能包含 http://或者https://。 | 无。 |
| Value | String | 否 | 否 | 标签值 ，可以为空字符串。最多支持128个字符，不能以 aliyun和 acs: 开头，不能包含 http://或者https://。 | 无。 |

**返回值**

Fn::GetAtt InstanceId：实例ID。由系统生成，实例的全局唯一标识。 PrivateIp：VPC类型实例的私网IP。当NetworkType为VPC时，该参数生效。 InnerIp：Classic类型实例的私网IP。当 NetworkType为Classic时，该参数生效。 PublicIp：Classic类型实例的公网IP列表。当NetworkType为Classic时，该参数生效。 ZoneId：可用区ID。 HostName：实例的主机名称。

**示例**

资源编排

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "WebServer": {
      "Type": "ALIYUN::ECS::InstanceClone",
      "Properties": {
        "SourceInstanceId": "i-25zsk****",
        "SecurityGroupId": "sg-25zwc****",
        "ZoneId": "cn-beijing-b",
        "DiskMappings": [
            {"Size": 10, "Category": "cloud"},
            {"Size": 10, "Category": "cloud", "SnapshotId": "s-25wsw****"}
```

]

```json
      }
    }
  },
  "Outputs": {
    "InstanceId": {
         "Value": {"get_attr": ["WebServer","InstanceId"]}
    },
    "PublicIp": {
         "Value": {"get_attr": ["WebServer","PublicIp"]}
    }
  }
}
```

#### ALIYUN::ECS::InstanceGroup

**语法**

资源编排

```json
{
  "Type": "ALIYUN::ECS::InstanceGroup",
  "Properties": {
    "SystemDiskAutoSnapshotPolicyId": String,
    "DedicatedHostId": String,
    "LaunchTemplateName": String,
    "RamRoleName": String,
    "IoOptimized": String,
    "PrivateIpAddress": String,
    "KeyPairName": String,
    "SystemDiskDiskName": String,
    "Description": String,
    "Tags": List,
    "HostName": String,
    "ImageId": String,
    "ResourceGroupId": String,
    "VSwitchId": String,
    "EniMappings": List,
    "Password": String,
    "InstanceType": String,
    "MaxAmount": Integer,
    "AutoReleaseTime": String,
    "SystemDiskCategory": String,
    "UserData": String,
    "LaunchTemplateId": String,
    "LaunchTemplateVersion": String,
    "SystemDiskSize": Number,
    "ZoneId": String,
    "VpcId": String,
    "InternetMaxBandwidthIn": Integer,
    "DeletionProtection": Boolean,
    "DeploymentSetId": String,
    "Ipv6AddressCount": Integer,
    "SecurityGroupId": String,
    "HpcClusterId": String,
    "SystemDiskDescription": String,
    "Ipv6Addresses": List,
    "NetworkType": String,
    "DiskMappings": List,
    "SystemDiskPerformanceLevel": String,
    "StorageSetId": String,
    "StorageSetPartitionNumber": Integer,
    "SchedulerOptions": Map
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ResourceGroup Id | String | 否 | 是 | 实例所在的企业资源组ID。 | 无。 |
| HpcClusterId | String | 否 | 是 | 实例所属的HPC 集群ID。 | 无。 |

资源编排

| MaxAmount | Integer |  | 是 |  |  | 是 |  |  | 一次性创建ECS 实例的最大个数。 |  | 取值范围：1~100，必须大于等于MinAmount。 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MinAmount | String |  | 是 |  |  | 是 |  |  | 一次性创建ECS 实例的最小个数。 |  | 取值范围：1~100，必须小于等于MaxAmount。 |  |  |  |
| Description | String |  | 否 |  |  | 是 |  |  | 描述信息。 |  | 最长256个字符。 |  |  |  |
| InstanceType | String |  | 是 |  |  | 是 |  |  | ECS实例规格。 |  | 无。 |  |  |  |
| ImageId | String |  | 是 |  |  | 是 |  |  | 用于启动ECS实例的镜像ID，包括公共镜像、自定义镜像和云市场镜像。 |  | 支持通过模糊的方式指定公共镜像ID，而不需要指定一个完整的公共镜像ID。例如， 指定Ubuntu，最终会匹配 ubuntu 16 0402 64 _ _ _ _ 20G alibase 2017081 _ _ 8.vhd 指定ubuntu1432，最终会匹配 ubuntu 14 0405 32 _ _ _ _ 40G alibase 2017071 _ _ 1.vhd |  |  |  |
| SecurityGroupI d | String |  | 否 |  |  | 否 |  |  | 指定创建实例所属安全组。 |  | 无。 |  |  |  |
| InstanceName | String |  | 否 |  |  | 否 |  |  | 实例名称。 |  | 最长128个字符。可包含英文、中文、数字、下划线、 点号和连字符。通过 name prefix[begin _ _ |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | name prefix[begin _ _ |  |  |
|  |  |  |  |  |  |  |  |  |  |  | number,bits]name suff _ |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | ix |  |  |  |
| Password | String |  | 否 |  |  | 是 |  |  | ECS实例登录密 |  | 长度为8~30个字符。 必须同时包含三项（大、 小写字母，数字和特殊符号）。 支持以下特殊字符 ：( |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | ：( |  |
|  |  |  |  |  |  |  |  |  |  |  | ) ` ~ ! @ # $ % ^ |  |  |  |
|  |  |  |  |  |  |  |  |  | 码。 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | & * - + = \| { } [ |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | ] : ; ‘ < > , . ? |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | / |  |  |  |
| HostName | String |  | 否 |  |  | 否 |  |  | 主机名。 |  | 长度最少2个字符。点号和连字符不能作为hostname 的首尾字符，且不能连续使用。 |  |  |  |

资源编排

| AutoReleaseTi me | String |  | 否 |  | 否 | ECS实例自动释放的时间。 | 时间格式必须遵守ISO8601 规范，例如 "yyyy-MM- ddTHH:mm:ssZ" 。释放时间不能超过三年。 |  |
|---|---|---|---|---|---|---|---|---|
| PrivateIpAddre ss | String |  | 否 |  | 否 | 在VPC网络环境下，指定的内网 IP。 | IP地址不能与VPC网络下的其它实例重复。 |  |
| DiskMappings | List |  | 否 |  | 是 | 为ECS实例创建的数据盘。 | 无。 |  |
| InternetMaxBa ndwidthIn | Integer |  | 否 |  | 否 | 公网最大入网带宽。 | 单位：Mbps。 取值范围：1~100。 默认值：100。 |  |
| IoOptimized | String |  | 否 |  | 否 | 是否创建I/O优化实例。 | 取值范围： none（非 I/O 优化） optimized（I/O 优化） 默认值：none。 |  |
| SystemDiskCat egory | String |  | 否 |  | 是 | 系统盘类型。 | 取值范围： cloud：普通云盘 cloud efficiency：高效云 _ 盘 cloud ssd：SSD云盘 _ cloud essd：ESSD云盘 _ ephemeral ssd：本地 _ SSD盘 |  |
| SystemDiskDe scription | String |  | 否 |  | 是 | 系统盘描述信息。 | 无。 |  |
| SystemDiskDis kName | String |  | 否 |  | 是 | 系统盘名称。 | 无。 |  |
| SystemDiskSiz e | Number |  | 否 |  | 是 | 系统盘大小。 | 取值范围： 40GB~500GB。如果使用自定义镜像创建系统盘，需要保证系统盘大于自定义镜像大小。 |  |
| Tags | List |  | 否 |  |  |  | 最多支持20个标签，格式： [{"Key":"tagKey" |  |
|  |  |  |  |  |  |  |  | [{"Key":"tagKey" |
|  |  |  |  |  |  | 用户自定义标 | ,"Value":"tagValue"}, |  |
|  |  |  |  |  | 是 |  |  |  |
|  |  |  |  |  |  | 签。 | {"Key":"tagKey2","Val |  |
|  |  |  |  |  |  |  | ue":"tagValue2"}] |  |
| UserData | String |  | 否 |  | 是 | 创建ECS实例时传递的用户数据。 | 内容需要限制在16KB以内。无需用Base64转码， 特殊字符需要使用转义符。 |  |

|  |  | "yyyy-MM- |  |
|---|---|---|---|
| 间。 | ddTHH:mm:ssZ" |  |  |

资源编排

| ZoneId | String | 否 | 否 | 可用区ID。 | 无。 |
|---|---|---|---|---|---|
| VpcId | String | 否 | 否 | 虚拟专有网络 ID。 | 无。 |
| VSwitchId | String | 否 | 否 | VSwitch ID。 | 无。 |
| KeyPairName | String | 否 | 是 | ECS实例绑定的密钥对名称。 | 如果是Windows ECS实例，则忽略该参数。默认为空。如果已填写 KeyPairName，Password 的内容仍会被设置到实例中，但是Linux系统中的密码登录方式会被禁止。 |
| RamRoleName | String | 否 | 是 | 实例RAM角色名称。 | 您可以调用ListRoles查询实例RAM角色名称。 |
| DedicatedHostI d | String | 否 | 否 | 专有宿主机ID。 | 无。 |
| LaunchTemplat eName | String | 否 | 是 | 启动模板名称。 | 无。 |
| EniMappings | List | 否 | 是 | 附加到实例的弹性网卡。 | 附加到实例的弹性网卡个数最多为1个。 |
| LaunchTemplat eId | String | 否 | 是 | 启动模板ID。 | 无。 |
| LaunchTemplat eVersion | String | 否 | 是 | 启动模板的版本。 | 如果没有指定版本，则使用默认版本。 |
| NetworkType | String | 否 | 否 | ECS实例网络类型。 | 取值范围： vpc classic 默认值：classic。 |
| DeletionProtec tion | Boolean | 否 | 否 | 实例释放保护属性，指定是否支持通过控制台或 API（DeleteIns tance）释放实例。 | 取值范围： true false |
| DeploymentSe tId | String | 否 | 是 | 部署集ID。 | 无。 |
| StorageSetId | String | 否 | 否 | 存储集ID。 | 无 |
| StorageSetPart itionNumber | Integer | 否 | 否 | 存储集中的最大分区数量。 | 取值范围：大于等于 2。 |

资源编排

| SchedulerOptio ns | Map | 否 | 否 | 调度相关属性信息。 | 更多信息，请参见 SchedulerOptions属性 |
|---|---|---|---|---|---|

**DiskMappings语法**

```json
"DiskMappings": [
  {
    "Category": String,
    "DiskName": String,
    "Description": String,
    "Device": String,
    "SnapshotId": String,
    "Size": String,
    "Encrypted": String,
    "KMSKeyId": String,
    "PerformanceLevel": String,
    "AutoSnapshotPolicyId": String
  }
```

]

**DiskMappings属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |  |  |
|---|---|---|---|---|---|---|---|
| Size | String | 是 | 否 | 数据盘大小。 | 单位：GB。 |  |  |
| Category | String | 否 | 否 | 数据盘的类型。 | 取值范围： cloud cloud efficiency _ cloud ssd _ cloud essd _ ephemeral ssd _ 对于I/O优化实例，默认值为 cloud efficiency。对于非 _ I/O优化实例，默认值为 cloud。 |  |  |
| DiskName | String | 否 | 否 | 数据盘的名称。 | 最长128个字符。可包含英文、中文、数字、下划线、 点号和连字符。 |  |  |
| Description | String | 否 | 否 | 数据盘的描述。 | 长度为2~256个英文或中文字符。不能以 http:// 或 https: // 开头。 |  |  |
|  |  |  |  |  |  | https: |  |
| Device | String | 否 | 否 | 数据盘在ECS中的名称。 | 例如：/dev/xvd[a-z]。 |  |  |
| SnapshotId | String | 否 | 否 | 快照ID。 | 无。 |  |  |

|  |  | http:// |
|---|---|---|
|  | // |  |

资源编排

| Encrypted | Boolean | 否 | 否 | 数据盘是否加密。 | 取值范围： true false 默认值：false。 |
|---|---|---|---|---|---|
| KMSKeyId | String | 否 | 否 | 数据盘对应的 KMS密钥ID。 | 无。 |
| AutoSnapshotP olicyId | String | 否 | 是 | 自动快照策略 ID。 | 无。 |
| PerformanceLe vel | String | 否 | 否 | 创建ESSD云盘作为数据盘使用时，设置云盘的性能等级。 | PL1（默认）：单盘最高随机读写IOPS为5万。 PL2：单盘最高随机读写 IOPS为10万。 PL3：单盘最高随机读写 IOPS为100万。 |

**Tags语法**

```json
"Tags": [
  {
    "Value": String,
    "Key": String
  }
```

]

**Tags属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Key | String | 是 | 否 | 标签键。 | 长度为1~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |
| Value | String | 否 | 否 | 标签值。 | 长度为0~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |

**EniMappings语法**

```json
"EniMappings": [
  {
    "SecurityGroupId": String,
    "VSwitchId": String,
    "Description": String,
    "NetworkInterfaceName": String,
    "PrimaryIpAddress": String
  }
```

] 资源编排

**EniMappings属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |  |  |
|---|---|---|---|---|---|---|---|
| SecurityGroupI d | String | 是 | 是 | 安全组ID。 | 所属的安全组ID必须是同一个VPC下的安全组。 |  |  |
| VSwitchId | String | 是 | 否 | 交换机ID。 | 无。 |  |  |
| Description | String | 否 | 是 | 弹性网卡的描述信息。 | 长度为2~256个英文或中文字符，不能以 http:// 或 https: // 开头。 |  |  |
| NetworkInterfa ceName | String | 否 | 是 | 弹性网卡名称。 | 长度为2~128个英文或中文字符。 必须以大小字母或中文开头，不能以 http:// 或 htt ps:// 开头。 可以包含数字、半角冒号 （:）、下划线（ ）或者 _ 连字符（-）。 |  |  |
|  |  |  |  |  |  | htt |  |
| PrimaryIpAddr ess | String | 否 | 否 | 弹性网卡的主私有IP地址。 | 指定的IP必须是在所属交换机的地址段内的空闲地址。 如果不指定IP，则默认随机分配该交换机中的空闲地址。 |  |  |

|  |  | http:// |
|---|---|---|
|  | // |  |

| https: |  |
|---|---|

|  |  | http:// |
|---|---|---|
|  | ps:// |  |

**SchedulerOptions语法**

```json
"SchedulerOptions": [
  {
    "DedicatedHostClusterId": String,
  }
```

]

**SchedulerOptions属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| DedicatedHost ClusterId | String | 是 | 否 | 指定ECS实例所属的专有宿主机集群，系统会自动选择该专有宿主机集群中的一台专有宿主机部署ECS实例。 |  |

**返回值**

Fn::GetAtt InstanceIds：实例ID，是访问实例的唯一标识。由系统生成，全局唯一。 PrivateIps：VPC类型实例的私网IP列表。当NetworkType为VPC时，此参数生效。例如，一个带有格式的Json Array： ["172.16.XX.XX", "172.16.XX.XX", … "172.16.XX.XX"] ，最多100个IP，用半角逗号字符隔开。 资源编排 InnerIps：Classic类型实例的私网IP列表。当NetworkType为Classic时，此参数生效。例如，一个带有格式的Json Array： ["10.1.XX.XX", "10.1.XX.XX", … "10.1.XX.XX"] ，最多100个IP，用半角逗号字符隔开。 PublicIps：Classic类型实例的公网IP列表。当NetworkType为Classic时，此参数生效。例如，一个带有格式的Json Array： ["42.1.XX.XX", "42.1.XX.XX", … "42.1.XX.XX"] ，最多100个IP，用半角逗号字符隔开。 HostNames：所有实例的主机名称列表。 OrderId: 实例的订单ID列表。 ZoneIds: 可用区ID。 RelatedOrderIds: 已创建ECS实例的相关订单ID列表。

**示例**

```json
{
  "ROSTemplateFormatVersion":"2015-09-01",
  "Resources":{
    "WebServer": {
      "Type": "ALIYUN::ECS::InstanceGroup",
      "Properties": {
        "ImageId":"m-25l0r****",
        "InstanceType": "ecs.t1.small",
        "SecurityGroupId": "sg-25zwc****",
        "ZoneId": "cn-beijing-b",
        "MaxAmount":1,
        "MinAmount":1,
        "Tags": [{
            "Key": "tiantt",
            "Value": "ros"
        },{
            "Key": "tiantt1",
            "Value": "ros1"
        }
```

]

```json
      }
    }
  },
  "Outputs": {
    "InstanceIds": {
         "Value":{"get_attr": ["WebServer","InstanceIds"]}
    },
    "PublicIps": {
         "Value":{"get_attr": ["WebServer","PublicIps"]}
    }
  }
}
```

#### ALIYUN::ECS::InstanceGroupClone

ALIYUN::ECS::InstanceGroupClone类型用于克隆生产一组ECS实例。

**语法**

资源编排

```json
{
  "Type": "ALIYUN::ECS::InstanceGroupClone",
  "Properties": {
    "BackendServerWeight": Integer,
    "DiskMappings": List,
    "LaunchTemplateName": String,
    "SpotPriceLimit": String,
    "ResourceGroupId": String,
    "KeyPairName": String,
    "SystemDiskDiskName": String,
    "PeriodUnit": String,
    "Description": String,
    "Tags": List,
    "ImageId": String,
    "SpotStrategy": String,
    "SourceInstanceId": String,
    "EniMappings": List,
    "Password": String,
    "MaxAmount": Integer,
    "AutoReleaseTime": String,
    "SystemDiskCategory": String,
    "LoadBalancerIdToAttach": String,
    "LaunchTemplateId": String,
    "LaunchTemplateVersion": String,
    "ZoneId": String,
    "InstanceName": String,
    "InternetMaxBandwidthIn": Integer,
    "DeletionProtection": Boolean,
    "DeploymentSetId": String,
    "SecurityGroupId": String,
    "RamRoleName": String,
    "HpcClusterId": String,
    "SystemDiskDescription": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ResourceGroupI d | String | 否 | 否 | 实例所在的企业资源组 ID。 | 无。 |
| HpcClusterId | String | 否 | 是 | 实例所属的EHPC集群 ID。 | 无。 |
| SourceInstanceI d | String | 是 | 否 | 指定需要克隆的ECS实例ID。 | 将会克隆实例规格、镜像、带宽限制、网络类型等等。如果源ECS实例加入多个安全组，新的安全组会加入源实例的第一个安全组。 |
| MaxAmount | Integer | 是 | 是 | 指定最多创建多少个 ECS实例。 | 取值范围：1~100，必须大于等于MinAmount。 |
| MinAmount | String | 是 | 是 | 指定至少创建多少个 ECS实例。 | 取值范围：1~100，必须小于等于MaxAmount。 |
| BackendServer Weight | Integer | 否 | 否 | 指定ECS实例在负载均衡器实例中权重。 | 取值范围：0~100。默认值：100。 |
| LoadBalancerIdT oAttach | String | 否 | 否 | 指定ECS实例将加入到哪个负载均衡实例ID。 | 无。 |
| Description | String | 否 | 否 | 描述信息。 | 最长256个字符。 |

资源编排

|  | ImageId | String |  |  | 否 | 是 | 用于启动ECS实例的镜像ID，包括公共镜像、 自定义镜像和云市场镜像。 | 支持通过模糊的方式指定公共镜ID，而不需要指定一个完整的公共镜像ID。部署ECS实例时，只需在编辑模板中指定镜像的类型和版本或者只指定镜像类型，ROS会选择自动适配符合的公共镜像ID。在模糊镜像ID中，可以用通配符（\*）指代镜像ID的某一部分。 当您给ECS指定公共镜像ID时，可以按照如下方式： 指定：ubuntu，最终会匹配： ubuntu 16 0402 64 20G alibase 20170818 _ _ _ _ _ _ .vhd。 指定：ubuntu 14，最终会匹配： _ ubuntu 14 0405 64 20G alibase 20170824 _ _ _ _ _ _ .vhd。 指定：ubuntu1432，最终会匹配： ubuntu 14 0405 32 40G alibase 20170711 _ _ _ _ _ _ .vhd 指定：ubuntu 16 0402 32，最终会匹配： _ _ _ ubuntu 16 0402 32 40G alibase 20170711 _ _ _ _ _ _ .vhd |  |
|---|---|---|---|---|---|---|---|---|---|
|  | SecurityGroupId | String |  |  | 否 | 否 | 指定创建实例所属安全组。 | 无。 |  |
|  | InstanceName | String |  |  | 否 | 否 | 实例名称。 | 最长128个字符，可包含英文、中文、数字、下划线 （ ）、点号（.）、和连字符（-）。 _ |  |
|  | Password | String |  |  | 否 | 否 | ECS实例登录密码。 | 实例的密码。8~30个字符，必须同时包含三项 （大、小写字母，数字和特殊符号）。支持以下特殊字符：( ) ` ~ ! @ # $ % ^ & * - + = \| { } [ ] : ; ‘ < > , . ? /。如果传入Password参数，请务必使用 HTTPS协议调用API以避免可能发生的密码泄露。 |  |
|  | DiskMappings | List |  |  | 否 | 否 | 指定需要挂载的磁盘。 | 最多支持16块磁盘。 |  |
|  | Tags | List |  |  |  |  |  | 最多支持20个标签，格式如： [{"Key":"tagKey","Value":"tagValue"} |  |
|  |  |  |  |  |  |  |  |  | [{"Key":"tagKey","Value":"tagValue"} |
|  |  |  |  |  | 否 | 否 | 用户自定义标签。 | , |  |
|  |  |  |  |  |  |  |  | {"Key":"tagKey2","Value":"tagValue2"}] |  |
|  | ZoneId | String |  |  | 否 | 否 | 可用区ID。 | 无。 |  |
|  | KeyPairName | String |  |  | 否 | 否 | 给ECS实例绑定的密钥对名称。如果是 Windows ECS实例，则忽略该参数。默认为空。如果填写了 KeyPairName，Passw ord的内容仍旧会被设置到实例中，但是 Linux 中的密码登录方式会被初始化成禁止。 | 无。 |  |
|  | RamRoleName | String |  |  | 否 | 否 | 实例RAM角色名称。 | 您可以使用RAM APIListRoles查询实例RAM角色名称。 |  |
|  | SpotPriceLimit | String |  |  | 否 | 否 | 设置实例的每小时最高价格。 | 支持最大3位小数。参数SpotStrategy取值为 SpotWithPriceLimit 时生效。 |  |
|  | SystemDiskDisk Name | String |  |  | 否 | 是 | 系统盘名称。 | 长度为2~128个英文或中文字符。必须以大小字母或中文开头，不能以 http:// 或 https:// 开头，可以包含数字、半角冒号（:）、下划线（ ）或 _ 者连字符（-）。 |  |

资源编排

| PeriodUnit | String | 否 | 是 | 购买资源的时长。 | 取值范围： Week 当PeriodUnit 为Week时，Period取值：{“1”, “2”, “3”, “4”}，AutoRenewPeriod取值：{“1”, “2”, “3”}。 Month 当PeriodUnit为Month时，Period取值：{ “1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “12”, “24”, “36”,”48”,”60”}，AutoRenewPeriod取值：{“1”, “2”, “3”, “6”, “12”}。 默认值：Month。 |
|---|---|---|---|---|---|
| EniMappings | List | 否 | 是 | 附加到实例的弹性网卡。 | 最多1个。 |
| AutoReleaseTim e | String | 否 | 否 | 自动释放时间。按照 ISO8601标准表示，并需要使用UTC时间。格式为：yyyy-MM- ddTHH:mm:ssZ。 如果秒（ss）取值不是00，则自动取为当前分钟（mm）开始时。 最短释放时间为当前时间半小时之后。 最长释放时间不能超过当前时间三年。 如果不传入参数 AutoReleaseTime， 表示自动释放功能已取消，ECS实例不再自动释放。 | 无。 |
| SystemDiskCate gory | String | 否 | 是 | 系统盘的磁盘种类。 | 取值范围： cloud：普通云盘 cloud efficiency：高效云盘 _ cloud ssd：SSD 云盘 _ ephemeral ssd：本地 SSD 盘 _ cloud essd：ESSD 云盘。目前 ESSD 云盘正在 _ 火热公测中，仅部分地域下的可用区可以选购。 已停售的实例规格且非I/O优化实例默认值：cloud， 否则，默认值：cloud efficiency _ |
| LaunchTemplate Name | String | 否 | 是 | 启动模板名称。 | 无。 |
| LaunchTemplate Version | String | 否 | 是 | 启动模板的版本。如果没有指定版本，则使用默认版本。 | 无。 |
| InternetMaxBan dwidthIn | Integer | 否 | 否 | 公网入带宽最大值，单位为Mbit/s。 | 取值范围：1~200。 默认值：200。 |
| LaunchTemplate Id | String | 否 | 是 | 启动模板ID。 | 无。 |
| SystemDiskDesc ription | String | 否 | 是 | 系统盘描述。 | 长度为2~256个英文或中文字符，不能以 http:// 和 https:// 开头。默认值：空。 |
| DeletionProtecti on | Boolea n | 否 | 否 | 实例释放保护属性，指定是否支持通过控制台或 API（DeleteInstance ）释放实例。 | 取值范围： true false |

资源编排

| DeploymentSetI d | String | 否 | 是 | 部署集ID。 | 无。 |
|---|---|---|---|---|---|

**DiskMappings语法**

```json
"DiskMappings": [
  {
    "Category": String,
    "DiskName": String,
    "Description": String,
    "Encrypted": String,
    "KMSKeyId": String,
    "Device": String,
    "SnapshotId": String,
    "Size": String
  }
```

]

**DiskMappings属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Encrypted | String | 否 | 否 | 数据盘是否加密。 | 取值范围： true false 默认值 ：false |
| KMSKeyId | String | 否 | 否 | 数据盘对应的KMS密钥ID。 | 无。 |
| Size | String | 是 | 否 | 数据盘大小，单位：GB。 | 无。 |
| Category | String | 否 | 否 | 数据盘的类型。 | 取值范围： cloud cloud efficiency _ cloud ssd _ ephemeral ssdDefault _ |
| DiskName | String | 否 | 否 | 数据盘的名称。 | 最长128个字符，可包含英文、中文、数字、下划线 （ ）、点号（.）、和连字 _ 符（-）。 |
| Description | String | 否 | 否 | 描述信息。 | 取值范围：2~256，默认值是空。 |
| Device | String | 否 | 否 | 指定数据盘的在ECS服务器中的设备名称。 | 例如：/dev/xvd[a-z]。 |
| SnapshotId | String | 否 | 否 | 通过SnapshotId创建数据盘。 | 无。 |

**EniMappings 语法**

资源编排

```json
"EniMappings": [
  {
    "SecurityGroupId": String,
    "VSwitchId": String,
    "Description": String,
    "NetworkInterfaceName": String,
    "PrimaryIpAddress": String
  }
```

]

**EniMappings 属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |  |  |
|---|---|---|---|---|---|---|---|
| SecurityGroupId | String | 是 | 是 | 弹性网卡所属的安全组ID。 | 无。 |  |  |
| VSwitchId | String | 是 | 否 | 弹性网卡所属的虚拟交换机 ID。 | 无 。 |  |  |
| Description | String | 否 | 是 | 弹性网卡的描述。 | 长度为2~256个英文或中文字符，不能以 http:// 和 https: // 开头。 |  |  |
|  |  |  |  |  |  | https: |  |
| NetworkInterface Name | String | 否 | 是 | 弹性网卡名称。 | 无。 |  |  |
| PrimaryIpAddress | String | 否 | 否 | 弹性网卡的主IP地址。 | 无。 |  |  |

|  |  | http:// |
|---|---|---|
|  | // |  |

**Tags 语法**

```json
"Tags": [
  {
    "Value": String,
    "Key": String
  }
```

]

**Tags 属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Key | String | 是 | 否 | 无。 | 无。 |
| Value | String | 否 | 否 | 无。 | 无。 |

**返回值**

Fn::GetAtt InstanceIds：实例 ID。由系统生成，全局唯一。是访问实例的唯一标识。 PrivateIps：VPC 类型实例的私网 IP 列表。当 NetworkType 为 VPC 时，这个参数生效。一个带有格式的 Json Array: [“172.16.XX.XX”, ”172.16.XX.XX”, … “172.16.XX.XX”]。最多 100 个 IP，用半角逗号字符隔开。 InnerIps：Classic 类型实例的私网 IP 列表。当 NetworkType 为 Classic 时，这个参数生效。一个带有格式的 Json Array: [“10.1.XX.XX”, ”10.1.XX.XX”, … “10.1.XX.XX”]。最多 100 个 IP，用半角逗号字符隔开。 PublicIps：Classic 类型实例的公网 IP 列表。当 NetworkType 为 Classic 时，这个参数生效。一个带有格式的 Json Array: [“42.1.XX.XX”, ”42.1.XX.XX”, … “42.1.XX.XX”]。最多 100 个 IP，用半角逗号字符隔开。 HostNames：所有实例的主机名称列表。一个带有格式的 Json Array: [“host1”, “host2”,… “host3”]。 OrderId: 实例的订单ID列表。 ZoneIds: 可用区 ID。

**示例**

资源编排

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "WebServer": {
      "Type": "ALIYUN::ECS::InstanceGroupClone",
      "Properties": {
        "SourceInstanceId": "i-25zsk****",
        "ImageId": "m-25l0r****",
        "SecurityGroupId": "sg-25zwc****",
        "ZoneId": "cn-beijing-b",
        "MaxAmount": 1,
        "MinAmount": 1
      }
    }
  },
  "Outputs": {
    "InstanceIds": {
      "Value": {"get_attr": ["WebServer","InstanceIds"]}
    },
    "PublicIps": {
      "Value": {"get_attr": ["WebServer","PublicIps"]}
    }
  }
}
```

#### ALIYUN::ECS::Invocation

ALIYUN::ECS::Invocation类型用于为一台或多台ECS实例触发一条云助手命令。

**语法**

```json
{
  "Type": "ALIYUN::ECS::Invocation",
  "Properties": {
    "Timed": Boolean,
    "Frequency": String,
    "CommandId": String,
    "InstanceIds": List
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Timed | Boolean | 否 | 否 | 命令是否为周期执行。默认值： False。 | 无。 |
| Frequency | String | 否 | 否 | 周期任务的执行周期。 | 无。 |
| CommandId | String | 是 | 否 | 命令ID。 | 无。 |
| InstanceIds | List | 是 | 否 | 执行命令的实例列表。最多能指定20 台实例ID。 | 无。 |

**返回值**

Fn::GetAtt 资源编排 InvokeId: 命令进程执行ID。

**示例**

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "Timed": {
      "Type": "Boolean",
      "Description": "Whether it is timed execution. Default is False.",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

]

```json
    },
    "Frequency": {
      "Type": "String",
      "Description": "The frequency of timing execution (the shortest frequency is performed every 1
minute). It iss mandatory when Timing is True.The value rule follows the rules of the cron expression . "
    },
    "CommandId": {
      "Type": "String",
      "Description": "The id of command."
    },
    "InstanceIds": {
      "Type": "CommaDelimitedList",
      "Description": "The instance id list. Select up to 20 instances at a time.Instances selected ne
twork type must be VPC network, status must be running"
    }
  },
  "Resources": {
    "Invocation": {
      "Type": "ALIYUN::ECS::Invocation",
      "Properties": {
        "Timed": {
          "Ref": "Timed"
        },
        "Frequency": {
          "Ref": "Frequency"
        },
        "CommandId": {
          "Ref": "CommandId"
        },
        "InstanceIds": {
          "Fn::Split": [
            ",",
            {
              "Ref": "InstanceIds"
            },
            {
              "Ref": "InstanceIds"
            }
```

]

```json
        }
      }
    }
  },
  "Outputs": {
    "InvokeId": {
      "Description": "The id of command execution.",
```

资源编排 p ,

```json
      "Value": {
        "Fn::GetAtt": [
          "Invocation",
          "InvokeId"
```

]

```
      }
    }
  }
}
```

#### ALIYUN::ECS::JoinSecurityGroup

ALIYUN::ECS::JoinSecurityGroup类型用于将一个或多个ECS实例加入指定的安全组。

**语法**

```json
{
  "Type": "ALIYUN::ECS::JoinSecurityGroup",
  "Properties": {
    "InstanceId": String,
    "InstanceIdList": List,
    "SecurityGroupId": String,
    "NetworkInterfaceList": List
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| SecurityGroupId | String | 是 | 否 | 安全组ID。 | 无。 |
| InstanceId | String | 否 | 否 | 需要加入安全组的 ECS实例ID。 | 无。 |
| InstanceIdList | List | 否 | 是 | 需要加入安全组的多个ECS实例ID。 | 无。 |
| NetworkInterfac eList | List | 否 | 是 | 弹性网卡ID。 | 无。 |

**返回值**

Fn::GetAtt 无。

**示例**

`JSON` 格式资源编排

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "SG": {
      "Type": "ALIYUN::ECS::JoinSecurityGroup",
      "Properties": {
        "SecurityGroupId": "sg-m5eagh7rzys2z8sa****",
        "InstanceIdList": [
          "i-m5e505h9bgsio0wy****",
          "i-m5e505hio0wyjc6r****"
```

]

```
      }
    }
  }
}
```

`YAML` 格式

```
ROSTemplateFormatVersion: '2015-09-01' Resources:
  SG:
    Properties:
      SecurityGroupId: sg-m5eagh7rzys2z8sa****
      InstanceIdList:
      - i-m5e505h9bgsio0wy****
      - i-m5e505hio0wyjc6r****
```

#### ALIYUN::ECS::LaunchTemplate

**语法**

资源编排

```json
{
  "Type": "ALIYUN::ECS::LaunchTemplate",
  "Properties": {
    "LaunchTemplateName": String,
    "VersionDescription": String,
    "ImageId": String,
    "InstanceType": String,
    "SecurityGroupId": String,
    "NetworkType": String,
    "VSwitchId": String,
    "InstanceName": String,
    "Description": String,
    "InternetMaxBandwidthOut": Integer,
    "HostName": String,
    "ZoneId": String,
    "SystemDiskCategory": String,
    "SystemDiskSize": Number,
    "SystemDiskDiskName": String,
    "SystemDiskDescription": String,
    "IoOptimized": String,
    "InternetChargeType": String,
    "UserData": String,
    "KeyPairName": String,
    "RamRoleName": String,
    "AutoReleaseTime": String,
    "SpotStrategy": String,
    "SpotPriceLimit": String,
    "SecurityEnhancementStrategy": String,
    "DiskMappings": List,
    "NetworkInterfaces": List,
    "Tags": List,
    "TemplateTags": List,
    "TemplateResourceGroupId": String,
    "SecurityGroupIds": List,
    "ResourceGroupId": String,
    "SpotDuration": Integer,
    "ImageOwnerAlias": String,
    "Period": Integer,
    "Ipv6AddressCount": Integer,
    "PrivateIpAddress": String,
    "PasswordInherit": Boolean,
    "SystemDiskDeleteWithInstance": Boolean,
    "DeploymentSetId": String,
    "InstanceChargeType": String,
    "SystemDiskPerformanceLevel": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| LaunchTempl ateName | String | 是 | 否 | 实例启动模板名称。 | 长度为2~128个字符。必须以英文字母或汉字开头，不能以 http:// 和 https:// 开头。可包含英文字母、汉字、数字、半角冒号（:）、下划线（ ）和 _ 短划线（-）。 |

资源编排

| VersionDescri ption | String | 否 | 否 | 实例启动模板版本描述。 | 长度为2~128个字符。必须以英文字母或汉字开头，不能以 http:// 和 https:// 开头。 |
|---|---|---|---|---|---|
| ImageId | String | 否 | 否 | 镜像ID。 | 无 |
| InstanceType | String | 否 | 否 | 实例类型。 | 无 |
| SecurityGrou pId | String | 否 | 否 | 安全组ID。 | 无 |
| NetworkType | String | 否 | 否 | 实例网络类型。 | 取值： classic：经典网络。 vpc：专有网络。 |
| VSwitchId | String | 否 | 否 | 交换机ID。 | 当NetworkType取值为 vpc 时该参数有效。 |
| InstanceNam e | String | 否 | 否 | 实例名称。 | 长度为2~128个字符。必须以英文字母或汉字开头，不能以 http:// 和 https:// 开头。 |
| Description | String | 否 | 否 | 实例描述。 | 长度为2~128个字符。必须以英文字母或汉字开头，不能以 http:// 和 https:// 开头。 |
| InternetMaxB andwidthOut | Integer | 否 | 否 | 公网出网带宽最大值。 | 取值范围：0~100。 单位：Mbps。 |
| HostName | String | 否 | 否 | 实例主机名。 | 英文句点（.）和短划线（-）不能作为首尾字符，也不能连续使用。 取值要求： Windows实例：长度为2~15个字符。 不能全是数字。可包含英文字母、数字和短划线（-）。 其他类型实例（Linux等）：长度为2~64个字符。 可包含英文字母、数字和短划线（-）。 |
| ZoneId | String | 否 | 否 | 实例所属的可用区ID。 | 无 |
| SystemDiskC ategory | String | 否 | 否 | 系统盘类型。 | 取值： cloud：普通云盘。 cloud efficiency：高效云盘。 _ cloud ssd：SSD云盘。 _ ephemeral ssd：本地SSD盘。 _ |
| SystemDiskSi ze | Number | 否 | 否 | 系统盘大小。 | 取值范围：20~500。 单位：GB。 |
| SystemDiskDi skName | String | 否 | 否 | 系统盘名称。 | 长度为2~128个字符。必须以英文字母或汉字开头，不能以 http:// 和 https:// 开头。可包含英文字母、汉字、数字、半角冒号（:）、下划线（ ）和 _ 短划线（-）。 |

资源编排

| SystemDiskD escription | String | 否 | 否 | 系统盘描述。 | 长度为2~256个字符，不能以 http:// 和 https:// 开头。 |  |  |
|---|---|---|---|---|---|---|---|
| IoOptimized | String | 否 | 否 | 是否为I/O优化实例。 | 取值： none：非I/O优化实例。 optimized：I/O优化实例。 |  |  |
| InternetCharg eType | String | 否 | 否 | 网络付费类型。 | 取值： PayByBandwidth：按带宽计费。 PayByTraffic：按流量计费。 |  |  |
| UserData | String | 否 | 否 | 实例自定义数据。 | 需要以Base64方式编码，原始数据不超过16KB。 |  |  |
| KeyPairName | String | 否 | 否 | 密钥对名称。 | 仅Linux实例需要指定该参数，此时密码登录方式会被初始化为禁止。 |  |  |
| RamRoleNam e | String | 否 | 否 | 实例RAM角色名称。 | 无 |  |  |
| AutoReleaseT ime | String | 否 | 否 | 实例自动释放时间。 | 按照ISO8601标准表示。需要使用 UTC时间，格式为 yyyy-MM- ddTHH:mm:ssZ 。 |  |  |
|  |  |  |  |  |  | yyyy-MM- |  |
| SpotStrategy | String | 否 | 否 | 后付费实例的抢占策略。 | 当InstanceChargeType参数取值为PostPaid时该参数生效。 取值： NoSpot：正常按量付费实例。 SpotWithPriceLimit：设置上限价格的抢占式实例。 SpotAsPriceGo：系统自动出价，最高按量付费价格。 |  |  |
| SpotPriceLimi t | String | 否 | 否 | 设置实例的每小时最高价格。 | 支持最多3位小数。 |  |  |
| SecurityEnha ncementStrat egy | String | 否 | 否 | 是否开启安全加固。 | 取值： Active：开启。 Deactive：关闭。 |  |  |
| DiskMappings | List | 否 | 否 | 数据盘列表。 | 最多支持16个数据盘。 更多信息，请参见DiskMappings 属性。 |  |  |
| NetworkInterf aces | List | 否 | 否 | 弹性网卡列表。 | 最多支持8个弹性网卡。 更多信息，请参见NetworkInterfaces属性。 |  |  |
| Tags | List | 否 | 否 | 实例、安全组、 磁盘和网卡的标签列表。 | 最多支持20个标签。 更多信息，请参见Tags属性。 |  |  |
| TemplateTag s | List | 否 | 否 | 启动模板的标签列表。 | 最多支持20个标签。 更多信息，请参见TemplateTags 属性。 |  |  |
| TemplateRes ourceGroupId | String | 否 | 否 | 启动模板所在的资源组ID。 | 无 |  |  |

|  | ddTHH:mm:ssZ |
|---|---|

资源编排

| SecurityGrou pIds | List | 否 | 否 | 实例加入的一个或多个安全组。 | 取值与实例能够加入的安全组配额有关。 说明不支持同时指定 SecurityGroupId和 SecurityGroupIds。 |
|---|---|---|---|---|---|
| ResourceGro upId | String | 否 | 否 | 实例、块存储和弹性网卡所在的资源组ID。 | 无 |
| SpotDuration | Integer | 否 | 否 | 抢占式实例的保留时长。 | 取值范围：0~6。 默认值：1。 单位：小时。 说明如需设置取值为 2~6，请提交工单。 |
| ImageOwner Alias | String | 否 | 否 | 镜像来源。 | 取值范围： system：阿里云提供的公共镜像。 self：您创建的自定义镜像。 others：其他阿里云用户共享给您的镜像。 marketplace：镜像市场。 |
| Period | Integer | 否 | 否 | 购买资源的时长。 | InstanceChargeType取值为 PrePaid时该参数有效，且必须指定。 取值：1~9、12、24、36、48、 60。 单位：月。 |
| Ipv6AddressC ount | Integer | 否 | 否 | 为主网卡指定随机生成的IPv6 地址数量。 | 取值范围：1~10。 |
| PrivateIpAddr ess | String | 否 | 否 | 实例私网IP地址。 | 专有网络VPC类型ECS实例设置私网IP地址时，必须从交换机的空闲网段中选择。 |
| PasswordInhe rit | Boolean | 否 | 否 | 是否使用镜像预设的密码。 | 取值： true：使用。 false：不使用。 说明 PasswordInherit和 Password必须且只能指定其中一个参数。 |
| SystemDiskD eleteWithInst ance | Boolean | 否 | 否 | 系统盘是否随实例释放。 | 取值： true（默认）：释放。 false：不释放。 |
| DeploymentS etId | String | 否 | 否 | 部署集ID。 | 无 |
| InstanceChar geType | String | 否 | 否 | 实例的计费方式。 | 取值： PrePaid：预付费，包年包月。 PostPaid：后付费，按实际使用量付费。 |

资源编排

| SystemDiskP erformanceLe vel | String | 否 | 否 | 创建ESSD云盘作为系统盘使用时，云盘的性能等级。 | 取值： PL0（默认）：单盘最高随机读写IOPS 1万。 PL1：单盘最高随机读写IOPS 5 万。 PL2：单盘最高随机读写IOPS 10 万。 PL3：单盘最高随机读写IOPS 100万。 |
|---|---|---|---|---|---|

**DiskMappings语法**

```json
"DiskMappings": [
  {
    "Category": String,
    "DiskName": String,
    "Description": String,
    "SnapshotId": String,
    "Size": String,
    "Encrypted": String,
    "DeleteWithInstance": String,
    "PerformanceLevel": String
  }
```

]

**DiskMappings属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Category | String | 否 | 否 | 数据盘类型。 | 取值： cloud：普通云盘。 cloud efficiency：高效云盘。 _ cloud ssd：SSD云盘。 _ ephemeral ssd：本地SSD盘。 _ |
| DiskName | String | 否 | 否 | 数据盘名称。 | 长度为2~128个字符。必须以英文字母或汉字开头，不能以 http:// 和 https:// 开头。可包含英文字母、汉字、数字、半角冒号（:）、下划线（ ）和 _ 短划线（-）。 |
| Description | String | 否 | 否 | 数据盘描述。 | 长度为2~256个字符，不能以 http:// 和 https:// 开头。 |
| SnapshotId | String | 否 | 否 | 创建数据盘使用的快照。 | 无 |
| Size | String | 否 | 否 | 系统盘大小。 | 取值范围： cloud：5~2000。 cloud efficiency： _ 20~32768。 cloud ssd：20~32768。 _ ephemeral ssd：5~800。 _ 单位：GB。 |
| Encrypted | Boolean | 否 | 否 | 是否加密数据盘。 | 取值： true：加密。 false：不加密。 |

资源编排

| DeleteWithIns tance | Boolean | 否 | 否 | 数据盘是否随实例释放而释放。 | 取值： true：释放。 false：不释放。 |
|---|---|---|---|---|---|
| PerformanceL evel | String | 否 | 否 | 创建ESSD云盘作为数据盘使用时，云盘的性能等级。 | 取值： PL0（默认）：单盘最高随机读写IOPS 1万。 PL1：单盘最高随机读写IOPS 5 万。 PL2：单盘最高随机读写IOPS 10 万。 PL3：单盘最高随机读写IOPS 100万。 |

**NetworkInterfaces语法**

```json
"NetworkInterfaces": [
  {
    "PrimaryIpAddress": String,
    "VSwitchId": String,
    "SecurityGroupId": String,
    "NetworkInterfaceName": String,
    "Description": String
  }
```

]

**NetworkInterfaces属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| PrimaryIpAdd ress | String | 否 | 否 | 弹性网卡的主私有IP地址。 | 无 |
| VSwitchId | String | 否 | 否 | 弹性网卡所属的交换机ID。 | 无 |
| SecurityGrou pId | String | 否 | 否 | 弹性网卡所属的安全组ID。 | 无 |
| NetworkInterf aceName | String | 否 | 否 | 弹性网卡名称。 | 无 |
| Description | String | 否 | 否 | 弹性网卡描述信息。 | 长度为2~256个字符，不能以 http:// 和 https:// 开头。 |

**Tags语法**

```json
"Tags": [
  {
    "Value": String,
    "Key": String
  }
```

]

**Tags属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|

资源编排

| Key | String | 否 | 否 | 标签键。 | 长度为1~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |
|---|---|---|---|---|---|
| Value | String | 否 | 否 | 标签值。 | 长度为0~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |

**TemplateTags语法**

```json
"TemplateTags": [
  {
    "Value": String,
    "Key": String
  }
```

]

**TemplateTags属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Key | String | 否 | 否 | 标签键。 | 长度为1~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |
| Value | String | 否 | 否 | 标签值。 | 长度为0~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |

**返回值**

Fn::GetAtt LaunchTemplateId：实例启动模板ID。 LaunchTemplateName：实例启动模板名称。 DefaultVersionNumber：实例启动模板默认版本号。 LatestVersionNumber：实例启动模板最新版本号。

**示例**

`JSON` 格式

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Description": "Test ECS LaunchTemplate、AutoProvisioningGroup",
  "Parameters": {
    "VSwitchZoneId": {
      "AssociationProperty": "ALIYUN::ECS::Instance:ZoneId",
      "Type": "String"
    },
    "VpcId": {
      "Type": "String",
    },
    "VSwitchId": {
      "Type": "String",
      "AssociationProperty": "ALIYUN::ECS::VSwitch::VSwitchId",
      "AssociationPropertyMetadata": {
"ZoneId":"VSwitchZoneId",
```

资源编排

```json
oed: Swtc oed,
        "VpcId": "VpcId"
      }
    },
    "SecurityGroupId": {
      "AssociationProperty": "ALIYUN::ECS::SecurityGroup::SecurityGroupId",
      "Type": "String",
      "AssociationPropertyMetadata": {
        "VpcId": "VpcId"
      }
    },
    "LaunchTemplateName": {
      "Type": "String",
      "Default": "mytest"
    },
    "ImageId": {
      "Type": "String",
      "Default": "centos_7"
    },
    "InstanceType": {
      "Type": "String",
      "AssociationProperty": "ALIYUN::ECS::Instance::InstanceType",
      "Default": "ecs.c5.large"
    },
    "SystemDiskCategory": {
      "Type": "String",
      "Description": "Category of system disk. Default is cloud_efficiency. support
cloud|cloud_efficiency|cloud_ssd|cloud_essd|ephemeral_ssd.Old instances will not be changed.",
      "AssociationProperty": "ALIYUN::ECS::Disk::SystemDiskCategory",
      "AssociationPropertyMetadata": {
        "ZoneId": "VSwitchZoneId",
        "InstanceType": "InstanceType"
      },
      "Default": "cloud_essd"
    },
    "PayAsYouGoTargetCapacity": {
      "Type": "String",
      "Description": "The target capacity of pay-as-you-go instances in the auto provisioning group."
```

,

```json
      "Default": "1"
    },
    "TotalTargetCapacity": {
      "Type": "String",
      "Description": "The total target capacity of the auto provisioning group. The target capacity c
onsists\nof the following three parts:\nThe target capacity of pay-as-you-go instances specified by t he PayAsYouGoTargetCapacity parameter\nThe target capacity of preemptible instances specified by the SpotTargetCapacity parameter\nThe supplemental capacity besides PayAsYouGoTargetCapacity and SpotTarg etCapacity",
      "Default": "2"
    },
    "SpotTargetCapacity": {
      "Type": "String",
      "Description": "The target capacity of preemptible instances in the auto provisioning group.",
      "Default": "1"
    },
    "AutoProvisioningGroupName": {
      "Type": "String",
      "Description": "The name of the auto provisioning group to be created. It must be 2 to 128 char
acters\nin length. It must start with a letter but cannot start with http:// or https://.\nIt can con tain letters, digits, colons (:), underscores (_), and hyphens (-).",
      "Default": "mytest"
    },
    "SpotAllocationStrategy": {
```

资源编排

```json
      "Type": "String",
      "Description": "The scale-out policy for preemptible instances. Valid values:\nlowest-price: Th
e cost optimization policy the auto provisioning group follows to select instance\ntypes of the lowes t cost to create instances.\ndiversified: The distribution balancing policy the auto provisioning gro up follows to evenly create\ninstances across zones specified in multiple extended template configura tions.\nDefault value: lowest-price",
      "AllowedValues": [
        "diversified",
        "lowest-price"
```

`],`

```json
      "Default": "lowest-price"
    },
    "SpotInstancePoolsToUseCount": {
      "Type": "Number",
      "Description": "This parameter takes effect when the SpotAllocationStrategy parameter is set to
lowest-price. The auto provisioning group selects instance types of the lowest cost to create\ninstances.",
      "Default": null
    },
    "PayAsYouGoAllocationStrategy": {
      "Type": "String",
      "Description": "The scale-out policy for pay-as-you-go instances. Valid values:\nlowest-price:
The cost optimization policy the auto provisioning group follows to select instance\ntypes of the low est cost to create instances.\nprioritized: The priority-based policy the auto provisioning group fol lows to create instances.\nThe priority of an instance type is specified by the LaunchTemplateConfig.N.Priority parameter.\nDefault value: lowest-price",
      "AllowedValues": [
        "lowest-price",
        "prioritized"
```

`],`

```json
      "Default": "lowest-price"
    },
    "MaxSpotPrice": {
      "Type": "Number",
      "Description": "The global maximum price for preemptible instances in the auto provisioning gro
up.\nIf both the MaxSpotPrice and LaunchTemplateConfig.N.MaxPrice parameters are specified, the maxim um price is the lower value of the two.",
      "Default": 5
    },
    "DefaultTargetCapacityType": {
      "Type": "String",
      "Description": "The type of supplemental instances. When the total value of
PayAsYouGoTargetCapacity and SpotTargetCapacity is smaller than the value of TotalTargetCapacity, the auto provisioning group will create instances of the specified type to meet\nthe capacity requirement s. Valid values:\nPayAsYouGo: Pay-as-you-go instances.\nSpot: Preemptible instances.\nDefault value: Spot",
      "AllowedValues": [
        "PayAsYouGo",
        "Spot"
```

`],`

```json
      "Default": "PayAsYouGo"
    },
    "AutoProvisioningGroupType": {
      "Type": "String",
      "Description": "The type of the auto provisioning group. Valid values:\nrequest: One-time deliv
ery. After the auto provisioning group is started, it only attempts\nto create an instance cluster on ce. If the cluster fails to be created, the group\ndoes not try again.\nmaintain: The continuous deli very and maintain capacity type. After the auto provisioning group\nis started, it continuously attem pts to create and maintain the instance cluster.\nThe auto provisioning group compares the real-time and target capacity of the cluster.\nIf the cluster does not meet the target capacity, the group will create instances\nuntil the cluster meets the target capacity.\nDefault value: maintain",
      "AllowedValues": [
"maintain"
```

资源编排

```
        maintain,
        "request"
```

`],`

```json
      "Default": "maintain"
    },
    "ExcessCapacityTerminationPolicy": {
      "Type": "String",
      "Description": "The shutdown policy for excess preemptible instances followed when the capacity
of\nthe auto provisioning group exceeds the target capacity. Valid values:\nno-termination: Excess pr eemptible instances are not shut down.\ntermination: Excess preemptible instances are to be shut down . The action to be performed on these\nshutdown instances is specified by the SpotInstanceInterruptionBehavior parameter.\nDefault value: no-termination",
      "AllowedValues": [
        "no-termination",
        "termination"
```

`],`

```json
      "Default": "termination"
    },
    "TerminateInstances": {
      "Type": "Boolean",
      "Description": "Specifies whether to release instances of the auto provisioning group. Valid va
lues:\ntrue\nfalse\nDefault: false",
      "AllowedValues": [
        true,
        false
```

`],`

```json
      "Default": true
    },
    "TerminateInstancesWithExpiration": {
      "Type": "Boolean",
      "Description": "The shutdown policy for preemptible instances when the auto provisioning group
expires.\nValid values:\ntrue: shuts down preemptible instances. The action to be performed on these shutdown instances\nis specified by the SpotInstanceInterruptionBehavior parameter.\nfalse: does not shut down preemptible instances.\nDefault: false",
      "AllowedValues": [
        true,
        false
```

`],`

```json
      "Default": true
    }
  },
  "Resources": {
    "LaunchTemplate": {
      "Type": "ALIYUN::ECS::LaunchTemplate",
      "Properties": {
        "LaunchTemplateName": {
          "Ref": "LaunchTemplateName"
        },
        "VersionDescription": "Test create LaunchTemplate",
        "ImageId": {
          "Ref": "ImageId"
        },
        "InstanceType": {
          "Ref": "InstanceType"
        },
        "SystemDiskCategory": {
          "Ref": "SystemDiskCategory"
        },
        "SecurityGroupId": {
          "Ref": "SecurityGroupId"
        },
        "VSwitchId": {
          "Ref": "VSwitchId"
```

资源编排

```json
        }
      }
    },
    "AutoProvisioningGroup": {
      "DependsOn": "LaunchTemplate",
      "Type": "ALIYUN::ECS::AutoProvisioningGroup",
      "Properties": {
        "LaunchTemplateId": {
          "Fn::GetAtt": [
            "LaunchTemplate",
            "LaunchTemplateId"
```

]

```json
        },
        "LaunchTemplateVersion": "1",
        "TotalTargetCapacity": {
          "Ref": "TotalTargetCapacity"
        },
        "PayAsYouGoTargetCapacity": {
          "Ref": "PayAsYouGoTargetCapacity"
        },
        "SpotTargetCapacity": {
          "Ref": "SpotTargetCapacity"
        },
        "AutoProvisioningGroupName": {
          "Ref": "AutoProvisioningGroupName"
        },
        "SpotAllocationStrategy": {
          "Ref": "SpotAllocationStrategy"
        },
        "SpotInstancePoolsToUseCount": {
          "Ref": "SpotInstancePoolsToUseCount"
        },
        "LaunchTemplateConfig": [
          {
            "Priority": 1,
            "WeightedCapacity": 1,
            "VSwitchId": {
              "Ref": "VSwitchId"
            },
            "MaxPrice": 1
          }
```

`],`

```json
        "Description": "Test AutoProvisioningGroup",
        "PayAsYouGoAllocationStrategy": {
          "Ref": "PayAsYouGoAllocationStrategy"
        },
        "MaxSpotPrice": {
          "Ref": "MaxSpotPrice"
        },
        "DefaultTargetCapacityType": {
          "Ref": "DefaultTargetCapacityType"
        },
        "AutoProvisioningGroupType": {
          "Ref": "AutoProvisioningGroupType"
        },
        "ExcessCapacityTerminationPolicy": {
          "Ref": "ExcessCapacityTerminationPolicy"
        },
        "TerminateInstances": {
          "Ref": "TerminateInstances"
        },
        "TerminateInstancesWithExpiration": {
"Ref" "TerminateInstancesWithEpiration"
```

资源编排

```json
          "Ref": "TerminateInstancesWithExpiration"
        }
      }
    }
  },
  "Outputs": {
    "AutoProvisioningGroupId": {
      "Description": "The ID of the auto provisioning group.",
      "Value": {
        "Fn::GetAtt": [
          "AutoProvisioningGroup",
          "AutoProvisioningGroupId"
```

]

```json
      }
    },
    "LaunchTemplateId": {
      "Value": {
        "Fn::GetAtt": [
          "LaunchTemplate",
          "LaunchTemplateId"
```

]

```json
      }
    },
    "LaunchTemplateName": {
      "Value": {
        "Fn::GetAtt": [
          "LaunchTemplate",
          "LaunchTemplateName"
```

]

```json
      }
    },
    "DefaultVersionNumber": {
      "Value": {
        "Fn::GetAtt": [
          "LaunchTemplate",
          "DefaultVersionNumber"
```

]

```json
      }
    },
    "LatestVersionNumber": {
      "Value": {
        "Fn::GetAtt": [
          "LaunchTemplate",
          "LatestVersionNumber"
```

]

```
      }
    }
  }
}
```

更多示例，请参见创建ECS实例启动模板和创建弹性供应组的组合示例：JSON示例和YAML示例。

#### ALIYUN::ECS::NatGateway

**语法**

资源编排

```json
{
  "Type": "ALIYUN::ECS::NatGateway",
  "Properties": {
    "DeletionProtection": Boolean,
    "VpcId": String,
    "Description": String,
    "NatGatewayName": String,
    "NatType": String,
    "Duration": Number,
    "AutoPay": Boolean,
    "InstanceChargeType": String,
    "PricingCycle": String,
    "VSwitchId": String,
    "DeletionForce": Boolean,
    "Spec": String,
    "Tags": List,
    "EipBindMode": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| VpcId | String | 是 | 否 | 创建NAT网关的专有网络ID。 | 无 |
| VSwitchId | String | 否 | 否 | 专有网络下的虚拟交换机ID。 | 无 |
| Description | String | 否 | 否 | NAT网关的描述。 | 长度为2~256个字符。 |
| NatGatewayNam e | String | 否 | 否 | NAT网关的名称。 | 长度为2~128个字符。必须以英文字母或汉字开头，可包含英文字母、数字、汉字、下划线 （ ）、英文句点 _ （.）和短划线 （-）。 |
| NatType | String | 否 | 否 | NAT网关的类型。 | 取值： Normal：普通型NAT网关。 Enhanced：增强型NAT网关。 |

资源编排

| Duration | Number | 否 | 否 | 购买时长。 | 取值： 当PricingCycle 取值为Month 时：1~9。 当PricingCycle 取值为Year时： 1~3。 说明当 InstanceCh argeType参数取值为 PrePaid时， 该参数必选。 |
|---|---|---|---|---|---|
| AutoPay | Boolean | 否 | 否 | 是否自动付费。 | 取值： false：不开启自动付费，生成订单后需要到订单中心完成支付。 true：开启自动付费，自动支付订单。 说明当 InstanceCh argeType参数取值为 PrePaid时， 该参数必选。 |
| InstanceChargeT ype | String | 否 | 否 | 计费方式。 | 取值： PostPaid（默认值）：按量计费。 PrePaid：包年包月。 |
| PricingCycle | String | 否 | 否 | 包年包月的计费周期。 | 取值： Month（默认值）：按月付费。 Year：按年付费。 说明当 InstanceCh argeType参数取值为 PrePaid时， 该参数必选。 |

资源编排

| Spec | String | 否 | 否 | NAT网关的规格。 | 取值： Small（默认值）：小型。 Middle：中型。 Large：大型。 XLarge.1：超大型。 |
|---|---|---|---|---|---|
| DeletionProtecti on | Boolean | 否 | 否 | 是否启用删除保护。 | 取值： true false（默认值） |
| DeletionForce | Boolean | 否 | 否 | 是否强制删除网关中的SNAT和DNAT 条目，并解除EIP 绑定。 | 取值： true false（默认值） |
| Tags | List | 否 | 否 | 标签。 | 最多支持添加20个标签。 详情请参见Tags属性。 |
| EipBindMode | String | 否 | 否 | NAT网关的EIP绑定模式。 | 取值： MULTI BINDE _ D（默认值）： 多EIP网卡可见模式。 NAT：EIP普通模式，兼容IPv4 网关。 当NAT网关的 EIP绑定模式为 EIP普通模式时，NAT网关支持绑定的EIP数量上限为50 个，且EIP将占用NAT网关所在交换机的一个私网IP。 |

**Tags语法**

```json
"Tags": [
  {
    "Key": String,
    "Value": String
  }
```

]

**Tags属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|

资源编排

| Key | String | 是 | 否 | 标签键 | 长度为1~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或 https:// 。 |  |  |
|---|---|---|---|---|---|---|---|
| Value | String | 否 | 否 | 标签值 | 长度为0~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或 https:// 。 |  |  |

|  | aliyun |
|---|---|
| acs: |  |

|  | http:// |
|---|---|
| https:// |  |

|  | aliyun |
|---|---|
| acs: |  |

|  | http:// |
|---|---|
| https:// |  |

**返回值**

Fn::GetAtt ForwardTableId：端口转发表ID。 SNatTableId：SNAT源地址转换表ID。 NatGatewayId：NAT网关的唯一ID。 BandwidthPackageIps：共享带宽包IP。 BandwidthPackageIds：共享带宽包ID。

**示例**

`JSON` 格式

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "Description": {
      "Type": "String",
      "Description": "Description of the NAT gateway, [2, 256] characters. Do not fill or empty, the
default is empty."
    },
    "NatGatewayName": {
      "Type": "String",
      "Description": "Display name of the NAT gateway, [2, 128] English or Chinese characters, must s
tart with a letter or Chinese in size, can contain numbers, '_' or '.', '-'"
    },
    "InstanceChargeType": {
      "Type": "String",
      "Description": "The billing method. The default value is PostPaid (which means pay-as-you-go)."
```

,

```json
      "AllowedValues": [
        "PrePaid",
        "PostPaid"
```

`],`

```json
      "Default": "PostPaid"
    },
    "PricingCycle": {
      "Type": "String",
      "Description": "Price cycle of the resource. This property has no default value.",
      "AllowedValues": [
        "Month",
        "Year"
```

]

```
    },
```

资源编排 ,

```json
    "VSwitchId": {
      "Type": "String",
      "Description": "The VSwitch id to create NAT gateway."
    },
    "Duration": {
      "Type": "Number",
      "Description": "The subscription duration. While choose by pay by month, it could be from 1 to
9. While choose pay by year, it could be from 1 to 3.",
      "MinValue": 1,
      "MaxValue": 9,
      "Default": 1
    },
    "DeletionProtection": {
      "Type": "Boolean",
      "Description": "Whether to enable deletion protection.\nDefault to False.",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

`],`

```json
      "Default": false
    },
    "AutoPay": {
      "Type": "Boolean",
      "Description": "Specifies whether to enable automatic payment. Default is false.",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

`],`

```json
      "Default": false
    },
    "NatType": {
      "Type": "String",
      "Description": "The type of the NAT gateway. Valid values:\n- Normal: standard NAT gateway.\n-
Enhanced: enhanced NAT gateway.",
      "AllowedValues": [
        "Normal",
        "Enhanced"
```

]

```json
    },
    "DeletionForce": {
      "Type": "Boolean",
      "Description": "Whether force delete the relative snat and dnat entries in the net gateway and
unbind eips. Default value is false.",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

`],`

```json
      "Default": false
    },
    "VpcId": {
      "Type": "String",
      "Description": "The VPC id to create NAT gateway."
    },
    "Spec": {
      "Type": "String",
      "Description": "NAT gateway specification. Now support 'Small|Middle|Large|XLarge.1'"
```

资源编排

```json
    },
    "Tags": {
      "Type": "Json",
      "Description": "Tags to attach to natgateway. Max support 20 tags to add during create
natgateway. Each tag with two properties Key and Value, and Key is required.",
      "MaxLength": 20
    }
  },
  "Resources": {
    "NatGateway": {
      "Type": "ALIYUN::ECS::NatGateway",
      "Properties": {
        "Description": {
          "Ref": "Description"
        },
        "NatGatewayName": {
          "Ref": "NatGatewayName"
        },
        "InstanceChargeType": {
          "Ref": "InstanceChargeType"
        },
        "PricingCycle": {
          "Ref": "PricingCycle"
        },
        "VSwitchId": {
          "Ref": "VSwitchId"
        },
        "Duration": {
          "Ref": "Duration"
        },
        "DeletionProtection": {
          "Ref": "DeletionProtection"
        },
        "AutoPay": {
          "Ref": "AutoPay"
        },
        "NatType": {
          "Ref": "NatType"
        },
        "DeletionForce": {
          "Ref": "DeletionForce"
        },
        "VpcId": {
          "Ref": "VpcId"
        },
        "Spec": {
          "Ref": "Spec"
        },
        "Tags": {
          "Ref": "Tags"
        }
      }
    }
  },
  "Outputs": {
    "BandwidthPackageIds": {
      "Description": "The bandwidth package ids of created NAT gateway.",
      "Value": {
        "Fn::GetAtt": [
          "NatGateway",
          "BandwidthPackageIds"
```

]

```
}
```

资源编排

```json
      }
    },
    "NatGatewayId": {
      "Description": "The Id of created NAT gateway.",
      "Value": {
        "Fn::GetAtt": [
          "NatGateway",
          "NatGatewayId"
```

]

```json
      }
    },
    "SNatTableId": {
      "Description": "The SNAT table id.",
      "Value": {
        "Fn::GetAtt": [
          "NatGateway",
          "SNatTableId"
```

]

```json
      }
    },
    "BandwidthPackageIps": {
      "Description": "The allocated public IPs.",
      "Value": {
        "Fn::GetAtt": [
          "NatGateway",
          "BandwidthPackageIps"
```

]

```json
      }
    },
    "ForwardTableId": {
      "Description": "The forward table id.",
      "Value": {
        "Fn::GetAtt": [
          "NatGateway",
          "ForwardTableId"
```

]

```
      }
    }
  }
}
```

`YAML` 格式

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  Description:
    Type: String
    Description: >-
      Description of the NAT gateway, [2, 256] characters. Do not fill or empty,
      the default is empty.
  NatGatewayName:
    Type: String
    Description: >-
      Display name of the NAT gateway, [2, 128] English or Chinese characters,
      must start with a letter or Chinese in size, can contain numbers, '_' or
      '.', '-'
  InstanceChargeType:
    Type: String
    Description: >-
      The billing method. The default value is PostPaid (which means
      pay-as-you-go).
    AllowedValues:
-PrePaid
```

资源编排

```
       PrePaid
      - PostPaid
    Default: PostPaid
  PricingCycle:
    Type: String
    Description: Price cycle of the resource. This property has no default value.
    AllowedValues:
      - Month
      - Year
  VSwitchId:
    Type: String
    Description: The VSwitch id to create NAT gateway.
  Duration:
    Type: Number
    Description: >-
      The subscription duration. While choose by pay by month, it could be from
      1 to 9. While choose pay by year, it could be from 1 to 3.
    MinValue: 1
    MaxValue: 9
    Default: 1
  DeletionProtection:
    Type: Boolean
    Description: |-
      Whether to enable deletion protection.
      Default to False.
    AllowedValues:
      - 'True'
      - 'true'
      - 'False'
      - 'false'
    Default: false
  AutoPay:
    Type: Boolean
    Description: Specifies whether to enable automatic payment. Default is false.
    AllowedValues:
      - 'True'
      - 'true'
      - 'False'
      - 'false'
    Default: false
  NatType:
    Type: String
    Description: |-
      The type of the NAT gateway. Valid values:
      - Normal: standard NAT gateway.
      - Enhanced: enhanced NAT gateway.
    AllowedValues:
      - Normal
      - Enhanced
  DeletionForce:
    Type: Boolean
    Description: >-
      Whether force delete the relative snat and dnat entries in the net gateway
      and unbind eips. Default value is false.
    AllowedValues:
      - 'True'
      - 'true'
      - 'False'
      - 'false'
    Default: false
  VpcId:
    Type: String
    Description: The VPC id to create NAT gateway.
```

资源编排

```
  Spec:
    Type: String
    Description: NAT gateway specification. Now support 'Small|Middle|Large|XLarge.1'
  Tags:
    Type: Json
    Description: >-
      Tags to attach to natgateway. Max support 20 tags to add during create
      natgateway. Each tag with two properties Key and Value, and Key is
      required.
    MaxLength: 20
Resources:
  NatGateway:
    Properties:
      Description:
        Ref: Description
      NatGatewayName:
        Ref: NatGatewayName
      InstanceChargeType:
        Ref: InstanceChargeType
      PricingCycle:
        Ref: PricingCycle
      VSwitchId:
        Ref: VSwitchId
      Duration:
        Ref: Duration
      DeletionProtection:
        Ref: DeletionProtection
      AutoPay:
        Ref: AutoPay
      NatType:
        Ref: NatType
      DeletionForce:
        Ref: DeletionForce
      VpcId:
        Ref: VpcId
      Spec:
        Ref: Spec
      Tags:
        Ref: Tags
Outputs:
  BandwidthPackageIds:
    Description: The bandwidth package ids of created NAT gateway.
    Value:
      'Fn::GetAtt':
        - BandwidthPackageIds
  NatGatewayId:
    Description: The Id of created NAT gateway.
    Value:
      'Fn::GetAtt':
        - NatGatewayId
  SNatTableId:
    Description: The SNAT table id.
    Value:
      'Fn::GetAtt':
        - SNatTableId
  BandwidthPackageIps:
    Description: The allocated public IPs.
    Value:
'Fn::GetAtt':
```

资源编排

```
      'Fn::GetAtt':
        - BandwidthPackageIps
  ForwardTableId:
    Description: The forward table id.
    Value:
      'Fn::GetAtt':
        - ForwardTableId
```

#### ALIYUN::ECS::NetworkInterface

ALIYUN::ECS::NetworkInterface类型用于创建一个弹性网卡（ENI）。

**语法**

```json
{
  "Type": "ALIYUN::ECS::NetworkInterface",
  "Properties": {
    "Description": String,
    "SecurityGroupId": String,
    "PrimaryIpAddress": String,
    "ResourceGroupId": String,
    "VSwitchId": String,
    "NetworkInterfaceName": String,
    "Tags": List,
    "SecurityGroupIds": List,
    "PrivateIpAddresses": List,
    "SecondaryPrivateIpAddressCount": Integer
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ResourceGro upId | String | 否 | 是 | 资源组ID。 | 无 |
| SecurityGrou pId | String | 否 | 是 | 安全组ID。 | 安全组和弹性网卡必须在同一个专有网络中。 说明不支持同时指定 SecurityGroupId和 SecurityGroupIds。 |
| VSwitchId | String | 是 | 否 | 交换机ID。 | 无 |
| Description | String | 否 | 是 | 弹性网卡的描述信息。 | 长度为2~256个字符，不能以 http:// 和 https:// 开头。 |
| NetworkInterf aceName | String | 否 | 是 | 弹性网卡的名称。 | 长度为2~128个字符。必须以英文字母或汉字开头，不能以 http:// 和 https:// 开头。可包含英文字母、汉字、数字、半角冒号（:）、下划线（ ）和 _ 短划线（-）。 |
| PrimaryIpAdd ress | String | 否 | 否 | 弹性网卡的主私有IP地址。 | 指定IP地址必须是所属交换机地址段内的空闲地址，不指定则默认随机分配该交换机中的空闲地址。 |

资源编排

| SecondaryPri vateIpAddres sCount | Integer | 否 | 否 | 辅助私有IP地址数量。 | 无 |
|---|---|---|---|---|---|
| Tags | List | 否 | 是 | 标签。 | 最多支持添加20个标签。 更多信息，请参见Tags属性。 |
| SecurityGrou pIds | List | 否 | 是 | 一个或多个安全组ID。 | 安全组和弹性网卡必须在同一个专有网络中。 说明不支持同时指定 SecurityGroupId和 SecurityGroupIds。 |
| PrivateIpAddr esses | List | 否 | 否 | 从弹性网卡所属交换机的空闲IP 地址中选择一个或多个辅助私有 IP地址。 | 可以绑定的IP地址数量的取值范围： 弹性网卡处于可用（Available） 状态：1~10。 弹性网卡处于已绑定（InUse） 状态：受到实例规格限制。 |

**Tags语法**

```json
"Tags": [
  {
    "Key": String,
    "Value": String
  }
```

]

**Tags属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Key | String | 是 | 否 | 标签键。 | 长度为1~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或 https:// 。 |
| Value | String | 否 | 否 | 标签值。 | 长度为0~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或 https:// 。 |

**返回值**

Fn::GetAtt NetworkInterfaceId：弹性网卡ID。 MacAddress：弹性网卡的MAC地址。 PrivateIpAddress：弹性网卡的私有IP地址。 SecondaryPrivateIpAddresses：弹性网卡的辅助私有IP地址。

**示例**

`YAML` 格式资源编排

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  SecurityGroupId:
    Type: String
    AssociationProperty: ALIYUN::ECS::SecurityGroup::SecurityGroupId
    Label:
```

`zh-cn:` 安全组`ID`

```
      en: Security Group ID
  VSwitchId:
    AssociationProperty: ALIYUN::ECS::VSwitch::VSwitchId
    Type: String
    Label:
```

`zh-cn:` 网络交换机`ID`

```
      en: VSwitch ID
Resources:
  EniInstance:
    Properties:
      SecurityGroupId:
        Ref: SecurityGroupId
      VSwitchId:
        Ref: VSwitchId
      NetworkInterfaceName: TestNetworkInterface
Outputs:
  PrivateIpAddress:
    Description: The primary private ip address of your Network Interface.
    Value:
      Fn::GetAtt:
        - EniInstance
        - PrivateIpAddress
  SecondaryPrivateIpAddresses:
    Description: The secondary private IP addresses of your Network Interface.
    Value:
      Fn::GetAtt:
        - EniInstance
        - SecondaryPrivateIpAddresses
  MacAddress:
    Description: The MAC address of your Network Interface.
    Value:
      Fn::GetAtt:
        - EniInstance
        - MacAddress
  NetworkInterfaceId:
    Description: ID of your Network Interface.
    Value:
      Fn::GetAtt:
        - EniInstance
        - NetworkInterfaceId
```

`JSON` 格式

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "SecurityGroupId": {
      "Type": "String",
      "AssociationProperty": "ALIYUN::ECS::SecurityGroup::SecurityGroupId",
      "Label": {
```

`"zh-cn": "`安全组`ID",`

```json
        "en": "Security Group ID"
      }
    },
"Si hd" {
```

资源编排

```json
    "VSwitchId": {
      "AssociationProperty": "ALIYUN::ECS::VSwitch::VSwitchId",
      "Type": "String",
      "Label": {
```

`"zh-cn": "`网络交换机`ID",`

```json
        "en": "VSwitch ID"
      }
    }
  },
  "Resources": {
    "EniInstance": {
      "Type": "ALIYUN::ECS::NetworkInterface",
      "Properties": {
        "SecurityGroupId": {
          "Ref": "SecurityGroupId"
        },
        "VSwitchId": {
          "Ref": "VSwitchId"
        },
        "NetworkInterfaceName": "TestNetworkInterface"
      }
    }
  },
  "Outputs": {
    "PrivateIpAddress": {
      "Description": "The primary private ip address of your Network Interface.",
      "Value": {
        "Fn::GetAtt": [
          "EniInstance",
          "PrivateIpAddress"
```

]

```json
      }
    },
    "SecondaryPrivateIpAddresses": {
      "Description": "The secondary private IP addresses of your Network Interface.",
      "Value": {
        "Fn::GetAtt": [
          "EniInstance",
          "SecondaryPrivateIpAddresses"
```

]

```json
      }
    },
    "MacAddress": {
      "Description": "The MAC address of your Network Interface.",
      "Value": {
        "Fn::GetAtt": [
          "EniInstance",
          "MacAddress"
```

]

```json
      }
    },
    "NetworkInterfaceId": {
      "Description": "ID of your Network Interface.",
      "Value": {
        "Fn::GetAtt": [
          "EniInstance",
          "NetworkInterfaceId"
```

]

```
      }
    }
  }
}
```

资源编排更多示例，请参见创建一个弹性网卡、绑定弹性网卡到专有网络类型实例和授权弹性网卡的组合示例：JSON示例和YAML示例。

#### ALIYUN::ECS::NetworkInterfaceAttachment

ALIYUN::ECS::NetworkInterfaceAttachment类型用于绑定弹性网卡（ENI）到专有网络（VPC）类型实例上。

**语法**

```json
{
  "Type": "ALIYUN::ECS::NetworkInterfaceAttachment",
  "Properties": {
    "InstanceId": String,
    "NetworkInterfaceId": String,
    "TrunkNetworkInstanceId": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| InstanceId | String | 是 | 否 | 实例ID。 | 无 |
| NetworkInterf aceId | String | 是 | 否 | 弹性网卡ID。 | 无 |
| TrunkNetwor kInstanceId | String | 否 | 否 | Trunk网卡ID。 | 无 |

**返回值**

Fn::GetAtt NetworkInterfaceId：弹性网卡ID。 TrunkNetworkInstanceId：Trunk网卡ID。 InstanceId：实例ID。

**示例**

`JSON` 格式资源编排

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "InstanceId": {
      "Type": "String",
      "Description": "ECS instance id"
    },
    "TrunkNetworkInstanceId": {
      "Type": "String"
    },
    "NetworkInterfaceId": {
      "Type": "String",
      "Description": "Network interface id"
    }
  },
  "Resources": {
    "EniAttachment": {
      "Type": "ALIYUN::ECS::NetworkInterfaceAttachment",
      "Properties": {
        "InstanceId": {
          "Ref": "InstanceId"
        },
        "TrunkNetworkInstanceId": {
          "Ref": "TrunkNetworkInstanceId"
        },
        "NetworkInterfaceId": {
          "Ref": "NetworkInterfaceId"
        }
      }
    }
  },
  "Outputs": {
    "TrunkNetworkInstanceId": {
      "Description": "ID of Trunk Network Interface.",
      "Value": {
        "Fn::GetAtt": [
          "EniAttachment",
          "TrunkNetworkInstanceId"
```

]

```json
      }
    },
    "NetworkInterfaceId": {
      "Description": "ID of your Network Interface.",
      "Value": {
        "Fn::GetAtt": [
          "EniAttachment",
          "NetworkInterfaceId"
```

]

```
      }
    }
  }
}
```

`YAML` 格式资源编排

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  InstanceId:
    Type: String
    Description: ECS instance id
  TrunkNetworkInstanceId:
    Type: String
  NetworkInterfaceId:
    Type: String
    Description: Network interface id
Resources:
  EniAttachment:
    Type: 'ALIYUN::ECS::NetworkInterfaceAttachment'
    Properties:
      InstanceId:
        Ref: InstanceId
      TrunkNetworkInstanceId:
        Ref: TrunkNetworkInstanceId
      NetworkInterfaceId:
        Ref: NetworkInterfaceId
Outputs:
  TrunkNetworkInstanceId:
    Description: ID of Trunk Network Interface.
    Value:
      'Fn::GetAtt':
        - EniAttachment
        - TrunkNetworkInstanceId
  NetworkInterfaceId:
    Description: ID of your Network Interface.
    Value:
      'Fn::GetAtt':
        - EniAttachment
        - NetworkInterfaceId
```

更多示例，请参见创建一个弹性网卡、绑定弹性网卡到专有网络类型实例和授权弹性网卡的组合示例：JSON示例和YAML示例。

#### ALIYUN::ECS::NetworkInterfacePermission

ALIYUN::ECS::NetworkInterfacePermission类型用于授权弹性网卡。

**语法**

```json
{
  "Type": "ALIYUN::ECS::NetworkInterfacePermission",
  "Properties": {
    "NetworkInterfaceId": String,
    "AccountId": String,
    "Permission": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| NetworkInterfac eId | String | 是 | 否 | 弹性网卡ID。 | 无 |
| AccountId | String | 是 | 否 | 帐号ID。 | 无 |

资源编排

| Permission | String | 是 | 否 | 授权。 | 无 |
|---|---|---|---|---|---|

**返回值**

**Fn::GetAtt**

NetworkInterfacePermissionId: 授权弹性网卡ID。

**示例**

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "AccountId": {
      "Type": "String",
      "Description": "the account id"
    },
    "Permission": {
      "Type": "String",
      "Description": "the permission",
      "Default": "InstanceAttach"
    },
    "NetworkInterfaceId": {
      "Type": "String",
      "Description": "Network interface id"
    }
  },
  "Resources": {
    "EniPermission": {
      "Type": "ALIYUN::ECS::NetworkInterfacePermission",
      "Properties": {
        "AccountId": {
          "Ref": "AccountId"
        },
        "Permission": {
          "Ref": "Permission"
        },
        "NetworkInterfaceId": {
          "Ref": "NetworkInterfaceId"
        }
      }
    }
  },
  "Outputs": {
    "NetworkInterfacePermissionId": {
      "Description": "the network interface permission id",
      "Value": {
        "Fn::GetAtt": [
          "EniPermission",
          "NetworkInterfacePermissionId"
```

]

```
      }
    }
  }
}
```

#### ALIYUN::ECS::Route

**语法**

资源编排

```json
{
  "Type": "ALIYUN::ECS::Route",
  "Properties": {
    "DestinationCidrBlock": String,
    "RouteTableId": String,
    "NextHopId": String,
    "NextHopType": String,
    "NextHopList": List
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| DestinationCidrBlock | String | 是 | 否 | 自定义路由条目的目标网段。 | 无 |
| RouteTableId | String | 是 | 否 | 路由表ID。 | 无 |
| NextHopId | String | 否 | 否 | 自定义路由条目的下一跳实例ID。 | 无 |
| NextHopType | String | 否 | 否 | 自定义路由条目的下一跳类型。 | 取值： Instance（默认值）：ECS实例。 HaVip：高可用虚拟IP。 RouterInterface：路由器接口。 NetworkInterface：弹性网卡。 VpnGateway：VPN网关。 IPv6Gateway：IPv6网关。 NatGateway：NAT网关。 Attachment：转发路由器。 |
| NextHopList | List | 否 | 否 | 自定义路由条目的下一跳的列表。 | 如果指定了NextHopList，则该路由条目为ECMP路由条目。 取值范围：2~4。 更多信息，请参见NextHopList 属性。 |

**NextHopList 语法**

```json
"NextHopList": [
  {
    "NextHopId": String,
    "NextHopType": String
  }
```

]

**NextHopList 属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| NextHopId | String | 是 | 否 | ECMP路由条目的下一跳实例的ID。 | 无 |

资源编排

| NextHopType | String | 否 | 否 | ECMP路由条目的下一跳的类型。 | 取值：RouterInterface，表示路由器接口。 |
|---|---|---|---|---|---|

**返回值**

Fn::GetAtt 无

**示例**

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "ECSRoute": {
      "Type": "ALIYUN::ECS::Route",
      "Properties": {
        "RouteTableId": "vtb-25oud****",
        "DestinationCidrBlock": "172.16.XX.XX/24",
        "NextHopId": "i-25xzy****"
      }
    }
  }
}
```

更多示例，请参见为弹性网卡分配IPv6地址和创建自定义路由条目的组合示例：JSON示例和YAML示例。

#### ALIYUN::ECS::SNatEntry

**语法**

```json
{
  "Type": "ALIYUN::ECS::SNatEntry",
  "Properties": {
    "SNatTableId": String,
    "SNatIp": String,
    "SnatEntryName": String,
    "SourceCIDR": String,
    "SourceVSwitchId": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |  |  |
|---|---|---|---|---|---|---|---|
| SNatTableId | String | 是 | 是 | 源地址转换表ID。 | 无 |  |  |
| SNatIp | String | 是 | 是 | 用于源地址转换的公网IP。 | 必须是NAT网关中带宽包的 IP。每个NAT网关上的公网 IP，不能既存在于端口转发表中，也存在于SNAT表中。 |  |  |
| SnatEntryName | String | 否 | 是 | SNAT条目的名称。 | 长度为2~128个字符，必须以英文字母或汉字开头，但不能以 http:// 或 https: // 开头。 |  |  |
|  |  |  |  |  |  | https: |  |

|  |  | http:// |
|---|---|---|
|  | // |  |

资源编排

| SourceCIDR | String | 否 | 否 | 交换机或ECS实例的网段。 交换机粒度：指定交换机的网段（如 192.168.1.0/24），当交换机下的ECS实例发起互联网访问请求时，NAT 网关会为其提供SNAT服务（代理上网服务）。如果SnatIp仅指定了一个公网IP，ECS实例使用指定的公网IP访问互联网；如果SnatIp指定了多个公网 IP，ECS实例随机使用 SnatIp中的公网IP访问互联网。 ECS粒度：指定ECS实例的地址（如 192.168.1.1/32），当 ECS实例发起互联网访问请求时，NAT网关会为其提供SNAT服务（代理上网服务）。如果SnatIp仅指定了一个公网IP，ECS 实例使用指定的公网IP访问互联网；如果SnatIp指定了多个公网IP，ECS实例随机使用SnatIp中的公网IP访问互联网。 | 不能同时指定SourceCIDR 和SourceVSwtichId，必须指定其中之一。 |
|---|---|---|---|---|---|
| SourceVSwitchId | String | 否 | 是 | 可通过NAT网关的SNAT功能访问互联网的ECS实例所在的vSwitch ID。 | 不能同时指定SourceCIDR 和SourceVSwtichId，必须指定其中之一。 |

**返回值**

Fn::GetAtt SNatEntryId：源地址转换表中的表项ID。

**示例**

`JSON` 格式资源编排

```json
{
 "ROSTemplateFormatVersion": "2015-09-01",
 "Parameters": {
  "SourceVSwitchId": {
   "Type": "String",
   "Description": "Allow which switch can access internet."
  },
  "SnatEntryName": {
   "Type": "String",
   "Description": "he name of the SNAT rule is 2-128 characters long and must start with a letter or
Chinese, but cannot begin with HTTP:// or https://."
  },
  "SourceCIDR": {
   "Type": "String",
   "Description": "Specifies the network segment of the switch. For example, 10.0.0.1/24. This parame
ter and the SourceVSwtichId parameter are mutually exclusive and cannot appear at the same time."
  },
  "SNatTableId": {
   "Type": "String",
   "Description": "Create SNAT entry in specified SNAT table."
  },
  "SNatIp": {
   "Type": "String",
   "Description": "Source IP, must belongs to bandwidth package internet IP"
  }
 },
 "Resources": {
  "SNatTableEntry": {
   "Type": "ALIYUN::ECS::SNatEntry",
   "Properties": {
    "SourceVSwitchId": {
     "Ref": "SourceVSwitchId"
    },
    "SnatEntryName": {
     "Ref": "SnatEntryName"
    },
    "SourceCIDR": {
     "Ref": "SourceCIDR"
    },
    "SNatTableId": {
     "Ref": "SNatTableId"
    },
    "SNatIp": {
     "Ref": "SNatIp"
    }
   }
  }
 },
 "Outputs": {
  "SNatEntryId": {
   "Description": "The id of created SNAT entry.",
   "Value": {
    "Fn::GetAtt": [
     "SNatTableEntry",
     "SNatEntryId"
```

]

```
   }
  }
 }
}
```

资源编排 `YAML` 格式

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
 SourceVSwitchId:
  Type: String
  Description: Allow which switch can access internet.
 SnatEntryName:
  Type: String
  Description: >-
   he name of the SNAT rule is 2-128 characters long and must start with a
   letter or Chinese, but cannot begin with HTTP:// or https://.
 SourceCIDR:
  Type: String
  Description: >-
   Specifies the network segment of the switch. For example, 10.0.0.1/24.
   This parameter and the SourceVSwtichId parameter are mutually exclusive
   and cannot appear at the same time.
 SNatTableId:
  Type: String
  Description: Create SNAT entry in specified SNAT table.
 SNatIp:
  Type: String
  Description: 'Source IP, must belongs to bandwidth package internet IP'
Resources:
 SNatTableEntry:
  Properties:
   SourceVSwitchId:
    Ref: SourceVSwitchId
   SnatEntryName:
    Ref: SnatEntryName
   SourceCIDR:
    Ref: SourceCIDR
   SNatTableId:
    Ref: SNatTableId
   SNatIp:
    Ref: SNatIp
Outputs:
 SNatEntryId:
  Description: The id of created SNAT entry.
  Value:
   'Fn::GetAtt':
    - SNatTableEntry
    - SNatEntryId
```

#### ALIYUN::ECS::SecurityGroup

**语法**

资源编排

```json
{
  "Type": "ALIYUN::ECS::SecurityGroup",
  "Properties": {
    "VpcId": String,
    "Description": String,
    "SecurityGroupName": String,
    "Tags": List,
    "SecurityGroupEgress": List,
    "SecurityGroupIngress": List,
    "ResourceGroupId": String,
    "SecurityGroupType": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ResourceGro upId | String | 否 | 是 | 安全组所在的资源组ID。 | 无 |
| VpcId | String | 否 | 否 | 专有网络ID。 | 无 |
| Description | String | 否 | 否 | 安全组描述信息。 | 长度为2~256个字符。 |
| Tags | List | 否 | 是 | 安全组的标签。 | 最多支持20个标签。 更多信息，请参见Tags属性。 |
| SecurityGrou pName | String | 否 | 否 | 安全组名称。 | 不填则为空，默认值为空。 长度为2~128个字符。 必须以英文字母或汉字开头，不能以 http:// 和 https:// 开头。 可包含英文字母、汉字、数字、 半角句号（.）、下划线（ ）和 _ 短划线（-）。 |
| SecurityGrou pEgress | List | 否 | 是 | 安全组出方向的访问规则。 | 更多信息，请参见SecurityGroupEgress属性。 |
| SecurityGrou pIngress | List | 否 | 是 | 安全组入方向的访问规则。 | 更多信息，请参见SecurityGroupIngress属性。 |
| SecurityGrou pType | String | 否 | 否 | 安全组的类型。 | 取值： normal：基本安全组。 enterprise：高级安全组。 |

**Tags语法**

```json
"Tags": [
  {
    "Value" : String,
    "Key" : String
  }
```

]

**Tags属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|

资源编排

| Key | String | 是 | 否 | 标签键。 | 长度为1~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或 https:// 。 |
|---|---|---|---|---|---|
| Value | String | 否 | 否 | 标签值。 | 长度为0~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或 https:// 。 |

**SecurityGroupEgress语法**

```json
"SecurityGroupEgress": [
  {
    "Description": String,
    "PortRange": String,
    "SecurityGroupId": String,
    "NicType": String,
    "Priority": Integer,
    "DestGroupId": String,
    "DestCidrIp": String,
    "Policy": String,
    "IpProtocol": String,
    "DestGroupOwnerId": String,
    "Ipv6DestCidrIp": String,
    "DestPrefixListId": String
  }
```

]

**SecurityGroupEgress属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Description | String | 否 | 是 | 安全组规则的描述信息。 | 长度为1~512个字符。 |
| DestGroupOw nerId | String | 否 | 否 | 跨账号设置安全组规则时，目的端安全组所属的阿里云账号 ID。 | 如果未设置DestGroupOwnerId， 则认为您设置了其它安全组的访问权限。如果您已经设置参数 DestCidrIp，则参数 DestGroupOwnerId无效。 |
| IpProtocol | String | 是 | 否 | IP协议。 | 取值： tcp udp icmp gre all：同时支持四种协议。 |
| PortRange | String | 是 | 否 | IP协议相关的端口号范围。 | 目的端安全组开放的传输层协议相关的端口范围。取值： TCP/UDP协议：1~65,535。使用正斜线（/）分隔起始端口和终止端口。 正确示例：1/200。 错误示例：200/1。 ICMP协议：-1/-1。 GRE协议：-1/-1。 all：-1/-1。 |

资源编排

| SecurityGrou pId | String | 否 | 否 | 需要创建出方向规则的安全组 ID。 | 无 |
|---|---|---|---|---|---|
| NicType | String | 否 | 否 | 网络类型。 | 取值： internet（默认值） intranet |
| DestPrefixList Id | String | 否 | 否 | 需要设置出方向访问权限的目的端前缀列表 ID。 | 您可以调用云服务ECS的 DescribePrefixLists接口查询可以使用的前缀列表ID。 安全组的网络类型为经典网络时， 不支持设置前缀列表。 当您指定了DestCidrIp、 Ipv6DestCidrIp或DestGroupId参数中的任意一个时，将忽略该参数。 |
| Priority | Integer | 否 | 否 | 授权策略优先级。 | 取值范围：1~100。 默认值：1。 |
| DestGroupId | String | 否 | 否 | 同一地域内的目标安全组ID。 | DestGroupId或DestCidrIp参数必须指定一项。 如果两项都指定，则默认对 DestCidrIp进行授权。 如果指定了该参数，且没有指定 DestCidrIp，则NicType只能选择intranet。 |
| DestCidrIp | String | 否 | 否 | 目标IP地址范围。 | 必须采用CIDR格式来指定IP地址范围。 默认值： 0.0.0.0/0（表示不受限制）。 其它支持的格式，例如 10.159.XX.XX/12。 最多10个IP地址或地址段，用半角逗号（,）隔开。 说明仅支持IPv4。 |
| Policy | String | 否 | 否 | 授权策略。 | 取值： accept（默认值）：接受访问。 drop：拒绝访问。 |
| Ipv6DestCidrI p | String | 否 | 否 | 目标地址IPv6 CIDR地址段。 | 支持在CIDR格式和IPv6格式的IP地址范围。仅支持专有网络类型的IP 地址。 |

**SecurityGroupIngress语法**

资源编排

```json
"SecurityGroupIngress": [
  {
    "SourceGroupOwnerId": String,
    "Description": String,
    "PortRange": String,
    "SecurityGroupId": String,
    "NicType": String,
    "Ipv6SourceCidrIp": String,
    "Priority": Integer,
    "SourceGroupId": String,
    "Policy": String,
    "IpProtocol": String,
    "SourcePortRange": String,
    "SourceCidrIp": String,
    "SourcePrefixListId": String
  }
```

]

**SecurityGroupIngress属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| SourceGroup OwnerId | String | 否 | 否 | 源安全组所属的阿里云账号 ID。 | 无 |
| Description | String | 否 | 是 | 安全组规则的描述信息。 | 长度为1~512个字符。 |
| SourcePrefixL istId | String | 否 | 否 | 需要设置入方向访问权限的源端前缀列表ID。 | 您可以调用云服务ECS的 DescribePrefixLists查询可以使用的前缀列表ID。 安全组的网络类型为经典网络时， 不支持设置前缀列表。 当您指定了SourceCidrIp、 Ipv6DestCidrIp或DestGroupId参数中的任意一个时，将忽略该参数。 |
| IpProtocol | String | 是 | 否 | IP协议。 | 取值： tcp udp icmp gre all：同时支持四种协议。 |
| PortRange | String | 是 | 否 | IP协议相关的端口范围。 | 目的端安全组开放的传输层协议相关的端口范围。取值： TCP/UDP协议：1~65535。使用正斜线（/）间隔起始端口和终止端口。 正确示例：1/200。 错误示例：200/1。 ICMP协议：-1/-1。 GRE协议：-1/-1。 all：-1/-1。 |

资源编排

| SourceGroupI d | String | 否 | 否 | 同一地域内的源安全组ID。 | SourceGroupId或者SourceCidrIp 参数必须指定一项。 如果两项都指定，则默认对 SourceCidrIp授权。 如果指定了该参数，且没有指定 SourceCidrIp，则NicType只能选择intranet。 |
|---|---|---|---|---|---|
| SecurityGrou pId | String | 否 | 否 | 需要创建入方向规则的安全组 ID。 | 无 |
| NicType | String | 否 | 否 | 网络类型。 | 取值： internet（默认值） intranet |
| Priority | Integer | 否 | 否 | 授权策略优先级。 | 取值范围：1~100。 默认值：1。 |
| SourceCidrIp | String | 否 | 否 | 源IP地址范围。 | 必须采用CIDR格式来指定IP地址范围。 默认值：0.0.0.0/0（表示不受限制）。 其它支持的格式，例如 10.159.XX.XX/12。 最多10个IP地址或地址段，用半角逗号（,）隔开。 说明仅支持IPV4。 |
| Policy | String | 否 | 否 | 授权策略。 | 取值： accept（默认值）：接受访问。 drop：拒绝访问。 |
| SourcePortRa nge | String | 否 | 否 | 源端安全组开放的传输层协议相关的端口范围。 | 取值： TCP/UDP协议：取值为 1~65535。使用正斜线（/）间隔起始端口和终止端口。 正确示例：1/200。 错误示例：200/1。 ICMP协议：-1/-1。 GRE协议：-1/-1。 IpProtocol取值为all：-1/-1。 |
| Ipv6SourceCi drIp | String | 否 | 否 | 源IPv6 CIDR地址段。 | 仅支持专有网络类型的IP地址。支持在CIDR格式和IPv6格式的IP地址范围。 |

**返回值**

Fn::GetAtt SecurityGroupId：安全组ID。 SecurityGroupName：安全组名称。

**示例**

`YAML` 格式资源编排

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  VpcId:
    Type: String
    Label:
```

`zh-cn:` 现有`VPC`的实例`ID`

```
      en: Existing VPC Instance ID
Resources:
  SecurityGroup:
    Properties:
      VpcId:
        Ref: VpcId
      SecurityGroupName: TestSecurityGroupName
      SecurityGroupType: normal
      SecurityGroupIngress:
        - PortRange: 22/22
          IpProtocol: tcp
        - PortRange: 80/80
          IpProtocol: tcp
      SecurityGroupEgress:
        - PortRange: 443/443
          IpProtocol: tcp
Outputs:
  SecurityGroupName:
    Description: The name of security group.
    Value:
      Fn::GetAtt:
        - SecurityGroupName
  SecurityGroupId:
    Description: generated security group id for security group.
    Value:
      Fn::GetAtt:
        - SecurityGroupId
```

`JSON` 格式资源编排

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "VpcId": {
      "AssociationProperty": "ALIYUN::ECS::VPC::VPCId",
      "Type": "String",
      "Label": {
```

`"zh-cn": "`现有`VPC`的实例`ID",`

```json
        "en": "Existing VPC Instance ID"
      }
    }
  },
  "Resources": {
    "SecurityGroup": {
      "Type": "ALIYUN::ECS::SecurityGroup",
      "Properties": {
        "VpcId": {
          "Ref": "VpcId"
        },
        "SecurityGroupName": "TestSecurityGroupName",
        "SecurityGroupType": "normal",
        "SecurityGroupIngress": [
          {
            "PortRange": "22/22",
            "IpProtocol": "tcp"
          },
          {
            "PortRange": "80/80",
            "IpProtocol": "tcp"
          }
```

`],`

```json
        "SecurityGroupEgress": [
          {
            "PortRange": "443/443",
            "IpProtocol": "tcp"
          }
```

]

```json
      }
    }
  },
  "Outputs": {
    "SecurityGroupName": {
      "Description": "The name of security group.",
      "Value": {
        "Fn::GetAtt": [
          "SecurityGroup",
          "SecurityGroupName"
```

]

```json
      }
    },
    "SecurityGroupId": {
      "Description": "generated security group id for security group.",
      "Value": {
        "Fn::GetAtt": [
          "SecurityGroup",
          "SecurityGroupId"
```

]

```
      }
    }
  }
}
```

资源编排更多示例，请参见创建安全组和添加ECS到安全组的组合示例：JSON示例和YAML示例。

#### ALIYUN::ECS::SecurityGroupClone

**语法**

```json
{
  "Type": "ALIYUN::ECS::SecurityGroupClone",
  "Properties": {
    "DestinationRegionId": String,
    "VpcId": String,
    "Description": String,
    "SecurityGroupName": String,
    "SourceSecurityGroupId": String,
    "ResourceGroupId": String,
    "NetworkType": String,
    "SecurityGroupType": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ResourceGroupI d | String | 否 | 是 | 实例所在的资源组 ID。 | 无。 |
| SourceSecurityG roupId | String | 是 | 否 | 用于克隆的原始安全组ID。 | 根据新安全组的网络类型，克隆合适的安全组规则。 |
| NetworkType | String | 否 | 否 | 克隆的新安全组网络类型为经典网络。 | 取值：Classic。 |
| VpcId | String | 否 | 否 | 克隆的新安全组所属的VPC ID。 | 当同时指定VpcId 和NetworkType 时，NetworkTyp e的设置无效。 |
| Description | String | 否 | 否 | 安全组描述信息。 | 长度为2~256个字符。不能以http:// 或https://开头。 |
| SecurityGroupNa me | String | 否 | 否 | 安全组名称。 | 默认值为空。长度为2~128字符。必须以大小字母或中文开头，可包含字母、汉字、数字、 点号（.）、下划线 （ ）和连字符 _ （-），但不能以 http://或https:// 开头。 |
| DestinationRegi onId | String | 否 | 否 | 将安全组克隆到指定区域。 | 默认值： CURRENT。 |
| SecurityGroupTy pe | String | 否 | 否 | 安全组类型。 | 取值： normal：基本安全组。 enterprise：高级安全组。 |

资源编排

**返回值**

Fn::GetAtt SecurityGroupId：安全组ID。

**示例**

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "SecurityGroupClone": {
      "Type": "ALIYUN::ECS::SecurityGroupClone",
      "Properties": {
        "SourceSecurityGroupId": {
          "Ref": "SourceSecurityGroupId"
        },
        "VpcId": {
          "Ref": "VpcId"
        },
        "Description": {
          "Ref": "Description"
        },
        "SecurityGroupName": {
          "Ref": "SecurityGroupName"
        },
        "DestinationRegionId": {
          "Ref": "DestinationRegionId"
        },
        "NetworkType": {
          "Ref": "NetworkType"
        }
      }
    }
  },
  "Parameters": {
    "SourceSecurityGroupId": {
      "Type": "String",
      "Description": "Source security group ID is used to copy properties to clone new security
group. If the NetworkType and VpcId is not specified, the same security group will be cloned. If Netw orkType or VpcId is specified, only proper security group rules will be cloned."
    },
    "VpcId": {
      "Type": "String",
      "Description": "Physical ID of the VPC."
    },
    "Description": {
      "Type": "String",
      "Description": "Description of the security group, [2, 256] characters. Do not fill or empty, t
he default is empty."
    },
    "SecurityGroupName": {
      "Type": "String",
      "Description": "Display name of the security group, [2, 128] English or Chinese characters, mus
t start with a letter or Chinese in size, can contain numbers, '_' or '.', '-'"
    },
    "DestinationRegionId": {
      "Default": "CURRENT",
      "Type": "String",
      "Description": "Clone security group to the specified region. Default to current region."
    },
    "NetworkType": {
      "Type": "String",
      "Description": "Clone new security group as classic network type. If the VpcId is specified, th
```

资源编排 p yg p `yp` p p ,

```json
e value will be ignored.",
      "AllowedValues": [
        "Classic"
```

]

```json
    }
  },
  "Outputs": {
    "SecurityGroupId": {
      "Description": "Generated security group id of new security group.",
      "Value": {
        "Fn::GetAtt": [
          "SecurityGroupClone",
          "SecurityGroupId"
```

]

```
      }
    }
  }
}
```

#### ALIYUN::ECS::SecurityGroupEgress

ALIYUN::ECS::SecurityGroupEgress类型用于创建安全组出方向的访问规则。

**语法**

```json
{
  "Type": "ALIYUN::ECS::SecurityGroupEgress",
  "Properties": {
    "SecurityGroupId": String,
    "IpProtocol": String,
    "PortRange": String,
    "DestGroupId": String,
    "DestCidrIp": String,
    "Policy": String,
    "Priority": String,
    "NicType": String,
    "DestPrefixListId": String,
    "Description": String,
    "DestGroupOwnerId": String,
    "Ipv6DestCidrIp": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| IpProtocol | String | 是 | 否 | 传输层协议。 | 取值： tcp udp icmp gre all：同时支持四种协议。 |

资源编排

| PortRange | String | 是 | 否 | 目的端安全组开放的传输层协议相关的端口范围。 | 取值： TCP/UDP协议： 1~65535。使用正斜线（/） 隔开起始端口和终止端口。正确示例：1/200； 错误示例： 200/1。 ICMP协议：-1/- 1。 GRE协议：-1/- 1。 all：-1/-1。 |
|---|---|---|---|---|---|
| SecurityGroupId | String | 否 | 否 | 源端安全组ID。 | 无 |
| DestPrefixListId | String | 否 | 否 | 需要设置出方向访问权限的目的端前缀列表ID。 | 您可以调用云服务 ECS的 DescribePrefixLi sts查询可用的前缀列表ID。 当安全组的网络类型为经典网络时， 不支持设置前缀列表。 当您指定了 DestCidrIp、 Ipv6DestCidrIp或 DestGroupId参数中的任意一个时， 将忽略该参数。 |
| NicType | String | 否 | 否 | 网卡类型。 | 取值： internet（默认值）：公网网卡。 intranet：内网网卡。 当设置安全组之间互相访问时，即指定DestGroupId， 但未指定 DestCidrIp时，该参数取值为 intranet。 |
| Priority | Integer | 否 | 否 | 安全组规则优先级。 | 取值范围： 1~100。 默认值：1。 |

资源编排

| DestGroupId | String | 否 | 否 | 需要设置访问权限的目的端安全组 ID。 | 至少设置 DestGroupId或者 DestCidrIp其中一项。 如果指定 DestGroupId，但未指定 DestCidrIp，则 NicType取值为 intranet。 如果同时指定 DestGroupId和 DestCidrIp，则以 DestCidrIp的设置为准。 |
|---|---|---|---|---|---|
| DestCidrIp | String | 否 | 否 | 目的端IP地址范围。 | 支持IPv4格式的IP 地址范围。 |
| Policy | String | 否 | 否 | 设置访问权限。 | 取值： accept（默认值）：接受访问。 drop：拒绝访问。 |
| Description | String | 否 | 是 | 安全组规则的描述信息。 | 长度为1~512个字符。 |
| DestGroupOwne rId | String | 否 | 否 | 跨账户设置安全组规则时，目的端安全组所属的阿里云账号ID。 | 如果 DestGroupOwne rId未设置，则认为是设置您其他安全组的访问权限。如果您已经设置 DestCidrIp，则 DestGroupOwne rId的设置无效。 |
| Ipv6DestCidrIp | String | 否 | 否 | 目的端IPv6 CIDR 地址段。 | 支持CIDR格式和 IPv6格式的IP地址范围，且仅支持 VPC类型的IP地址。 |

**返回值**

Fn::GetAtt 无。

**示例**

`YAML` 格式资源编排

```
ROSTemplateFormatVersion: '2015-09-01' Description: Test ECS SecurityGroupEgress Parameters:
  SecurityGroupId:
    Type: String
    AssociationProperty: ALIYUN::ECS::SecurityGroup::SecurityGroupId
    Label:
```

`zh-cn:` 安全组`ID`

```
      en: Security Group ID
Resources:
  SgEgress:
    Properties:
      IpProtocol: all
      PortRange: '-1/-1'
      NicType: intranet
      SecurityGroupId:
        Ref: SecurityGroupId
```

`JSON` 格式

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Description": "Test ECS SecurityGroupEgress",
  "Parameters": {
    "SecurityGroupId": {
      "Type": "String",
      "AssociationProperty": "ALIYUN::ECS::SecurityGroup::SecurityGroupId",
      "Label": {
```

`"zh-cn": "`安全组`ID",`

```json
        "en": "Security Group ID"
      }
    }
  },
  "Resources": {
    "SgEgress": {
      "Type": "ALIYUN::ECS::SecurityGroupEgress",
      "Properties": {
        "IpProtocol": "all",
        "PortRange": "-1/-1",
        "NicType": "intranet",
        "SecurityGroupId": {
          "Ref": "SecurityGroupId"
        }
      }
    }
  }
}
```

#### ALIYUN::ECS::SecurityGroupIngress

ALIYUN::ECS::SecurityGroupIngress类型用于创建安全组入方向的访问规则。

**语法**

资源编排

```json
{
  "Type": "ALIYUN::ECS::SecurityGroupIngress",
  "Properties": {
    "SourceGroupOwnerId": String,
    "Description": String,
    "PortRange": String,
    "SecurityGroupId": String,
    "NicType": String,
    "Ipv6SourceCidrIp": String,
    "Priority": Integer,
    "SourceGroupId": String,
    "Policy": String,
    "IpProtocol": String,
    "SourcePortRange": String,
    "SourceCidrIp": String,
    "SourcePrefixListId": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| IpProtocol | String | 是 | 否 | IP协议。 | 取值： tcp udp icmp gre all：同时支持四种协议。 |
| PortRange | String | 是 | 否 | 目的端安全组开放的传输层协议相关的端口范围。 | 取值： TCP/UDP协议： 1~65535。使用正斜线（/） 隔开起始端口和终止端口。正确示例：1/200； 错误示例： 200/1。 ICMP协议：-1/- 1。 GRE协议：-1/- 1。 all：-1/-1。 |

资源编排

| SourcePrefixListI d | String | 否 | 否 | 需要设置入方向访问权限的目的端前缀列表ID。 | 您可以调用云服务 ECS的 DescribePrefixLi sts查询可以使用的前缀列表ID。 安全组的网络类型为经典网络时，不支持设置前缀列表。 当您指定了 SourceCidrIp、 Ipv6SourceCidrI p与 SourceFroupId参数中的任意一个时，将忽略该参数。 |
|---|---|---|---|---|---|
| SourceGroupId | String | 否 | 否 | 需要设置访问权限的源端安全组ID。 | 至少设置 SourceGroupId或者SourceCidrIp其中一项。 如果指定 SourceGroupId， 但未指定 SourceCidrIp，则参数NicType取值为intranet。 如果同时指定 SourceGroupId和 SourceCidrIp，则默认以 SourceCidrIp的设置为准。 |
| SecurityGroupId | String | 否 | 否 | 需要创建入规则的安全组ID。 | 无 |
| NicType | String | 否 | 否 | 网络类型。 | 取值： internet（默认值）：公网网卡。 intranet：内网网卡。 当设置安全组之间互相访问时，即指定DestGroupId但未指定DestCidrIp 时，该参数取值为 intranet。 |
| Priority | Integer | 否 | 否 | 安全组规则优先级。 | 取值范围： 1~100。 默认值：1。 |
| SourceCidrIp | String | 否 | 否 | 源端IPv4 CIDR地址段。 | 仅支持IPv4格式的 IP地址范围。 |
| Policy | String | 否 | 否 | 访问权限。 | 取值： accept（默认值）：接受访问。 drop：拒绝访问。 |

资源编排

| SourceGroupOw nerId | String | 否 | 否 | 跨账户设置安全组规则时，源端安全组所属的阿里云账户ID。 | 如果 SourceGroupOw nerId未设置，则默认设置您其他安全组的访问权限。 如果已经设置 SourceCidrIp，则 SourceGroupOw nerId的设置无效。 |
|---|---|---|---|---|---|
| Description | String | 否 | 是 | 安全组规则的描述信息。 | 长度为1~512个字符。 |
| SourcePortRang e | String | 否 | 否 | 源端安全组开放的传输层协议相关的端口范围。 | 取值： TCP/UDP协议： 1~65535。使用正斜线（/） 隔开起始端口和终止端口。正确示例：1/200； 错误示例： 200/1。 ICMP协议：-1/- 1。 GRE协议：-1/- 1。 all：-1/-1。 |
| Ipv6SourceCidrI p | String | 否 | 否 | 源端IPv6 CIDR地址段。 | 支持CIDR格式和 IPv6格式的IP地址范围。仅支持VPC 类型的IP地址。 |

**返回值**

Fn::GetAtt 无。

**示例**

`YAML` 格式资源编排

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  PortRange:
    Type: String
    Default: '-1/-1'
    Description: Ip protocol relative port range. For tcp and udp, the port rang is [1,65535], usin
g format '1/200'For icmp|gre|all protocel, the port range should be '-1/-1'
  SecurityGroupId:
    Type: String
    AssociationProperty: ALIYUN::ECS::SecurityGroup::SecurityGroupId
    Label:
```

`zh-cn:` 安全组`ID`

```
      en: Security Group ID
  SourceCidrIp:
    Type: String
    Description: Source CIDR Ip Address range. Only IPV4 supported.
    Default: 0.0.0.0/0
  IpProtocol:
    Type: String
    Description: Ip protocol for in rule.
    AllowedValues:
      - tcp
      - udp
      - icmp
      - gre
      - all
  NicType:
    Type: String
    Description: Network type, could be 'internet' or 'intranet'. Default value is internet.
    AllowedValues:
      - internet
      - intranet
Resources:
  SecurityGroupIngress:
    Properties:
      SecurityGroupId:
        Ref: SecurityGroupId
      SourceCidrIp:
        Ref: SourceCidrIp
      IpProtocol:
        Ref: IpProtocol
      NicType:
        Ref: NicType
      PortRange:
        Ref: PortRange
```

`JSON` 格式

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "PortRange": {
      "Type": "String",
      "Default": "-1/-1",
      "Description": "Ip protocol relative port range. For tcp and udp, the port rang is [1,65535],
using format '1/200'For icmp|gre|all protocel, the port range should be '-1/-1'"
    },
    "SecurityGroupId": {
       "Type": "String",
      "AssociationProperty": "ALIYUN::ECS::SecurityGroup::SecurityGroupId",
      "Label": {
```

"安全组 "h " " 资源编排 `"zh-cn": "`安全组`ID",`

```json
        "en": "Security Group ID"
      }
    },
    "SourceCidrIp": {
      "Type": "String",
      "Description": "Source CIDR Ip Address range. Only IPV4 supported.",
      "Default": "0.0.0.0/0"
    },
    "IpProtocol": {
      "Type": "String",
      "Description": "Ip protocol for in rule.",
      "AllowedValues": [
        "tcp",
        "udp",
        "icmp",
        "gre",
        "all"
```

]

```json
    },
    "NicType": {
      "Type": "String",
      "Description": "Network type, could be 'internet' or 'intranet'. Default value is internet.",
      "AllowedValues": [
        "internet",
        "intranet"
```

]

```json
    }
  },
  "Resources": {
    "SecurityGroupIngress": {
      "Type": "ALIYUN::ECS::SecurityGroupIngress",
      "Properties": {
        "SecurityGroupId": {
          "Ref": "SecurityGroupId"
        },
        "SourceCidrIp": {
          "Ref": "SourceCidrIp"
        },
        "IpProtocol": {
          "Ref": "IpProtocol"
        },
        "NicType": {
          "Ref": "NicType"
        },
        "PortRange": {
          "Ref": "PortRange"
        }
      }
    }
  }
}
```

#### ALIYUN::ECS::Snapshot

**语法**

资源编排

```json
{
  "Type": "ALIYUN::ECS::Snapshot",
  "Properties": {
    "SnapshotName": String,
    "Timeout": Integer,
    "Description": String,
    "DiskId": String,
    "Tags": List,
    "InstantAccess": Boolean,
    "InstantAccessRetentionDays": Integer,
    "ResourceGroupId": String,
    "RetentionDays": Integer
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| DiskId | String | 是 | 否 | 将要创建磁盘快照的磁盘ID。 | 无 |
| SnapshotNam e | String | 否 | 否 | 快照的显示名称。 | 长度为2~128个字符。必须以英文字母或汉字开头，不能以 http:// 和 https:// 开头。可包含英文字母、汉字、数字、半角冒号（:）、下划线（ ）或 _ 短划线（-）。 为防止和自动快照的名称冲突，不能以auto开头。 |
| Timeout | Integer | 否 | 否 | 创建快照的超时时间。 | 设置此时间会延长创建资源栈的超时时间。如果快照在指定的时间内没有创建完成，则整个资源栈将创建失败。请根据磁盘的大小和数据的多少，设置合理的超时时间。 取值范围：200~1440。 默认值：200。 单位：分钟。 |
| Description | String | 否 | 否 | 快照的描述。 | 长度为2~256个字符，不能以 http:// 和 https:// 开头。 默认值：空。 |
| ResourceGro upId | String | 否 | 是 | 磁盘快照所属的资源组ID。 | 无 |
| Tags | List | 否 | 是 | 标签。 | 最多支持添加20个标签。 更多信息，请参见Tags属性。 |

资源编排

| InstantAccess | Boolean | 否 | 否 | 是否开启快照极速可用功能。 | 取值： true：开启。仅ESSD云盘支持开启该功能。 false（默认值）：关闭。即创建标准快照。 |
|---|---|---|---|---|---|
| InstantAccess RetentionDay s | Integer | 否 | 否 | 设置快照极速可用功能的保留时间，保留时间到期后快照将自动释放。 | 该参数仅在InstantAccess取值为 true时生效。 取值范围：1~65,535。 单位：天。 |
| RetentionDay s | Integer | 否 | 否 | 设置快照的保留时间。 | 单位为天。保留时间到期后快照会被自动释放。 取值范围：1~65536。 默认值：空，表示快照不会被自动释放。 |

**Tags语法**

```json
"Tags": [
  {
    "Key": String,
    "Value": String
  }
```

]

**Tags属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Key | String | 是 | 否 | 标签键。 | 长度为1~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |
| Value | String | 否 | 否 | 标签值。 | 长度为0~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |

**返回值**

Fn::GetAtt SnapshotId：快照ID。 Arn：阿里云资源名称。

**示例**

YAML JSON 资源编排

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  DiskId:
    Type: String
Resources:
  Snapshot:
    Properties:
      Timeout: 300
      DiskId:
        Ref: DiskId
Outputs:
  SnapshotId:
    Description: The snapshot ID.
    Value:
      Fn::GetAtt:
        - SnapshotId
```

更多示例，请参见挂载ECS磁盘和创建磁盘快照的组合示例：YAML示例。

#### ALIYUN::ECS::SSHKeyPair

ALIYUN::ECS::SSHKeyPair类型用于创建SSH密钥对或导入已有的SSH密钥对。

**语法**

```json
{
  "Type": "ALIYUN::ECS::SSHKeyPair",
  "Properties": {
    "ResourceGroupId": String,
    "KeyPairName": String,
    "PublicKeyBody": String,
    "Tags": List
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ResourceGro upId | String | 否 | 是 | 实例所在的资源组ID。 | 无 |
| KeyPairName | String | 是 | 否 | 密钥对的名称。 | 长度为2~128个字符。必须以英文字母或汉字开头，不能以 http:// 和 https:// 开头。可包含英文字母、汉字、数字、半角冒号（:）、下划线（ ）和 _ 短划线（-）。 |
| PublicKeyBod y | String | 否 | 否 | 密钥对的公钥内容。 | 仅在导入密钥对时需要指定该参数。 |
| Tags | List | 否 | 是 | 标签。 | 最多支持添加20个标签。 更多信息，请参见Tags属性。 |

**Tags语法**

资源编排

```json
"Tags": [
  {
    "Key": String,
    "Value": String
  }
```

]

**Tags属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Key | String | 是 | 否 | 标签键。 | 长度为1~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |
| Value | String | 否 | 否 | 标签值。 | 长度为0~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |

**返回值**

Fn::GetAtt KeyPairFingerPrint：密钥对的指纹。根据RFC4716定义的公钥指纹格式，采用MD5信息摘要算法。 PrivateKeyBody：密钥对的私钥。未加密的PEM编码PKCS#8格式的RSA私钥内容。只有在第一次创建完成后有唯一的机会获取密钥对的私钥。如果是导入已有公钥，则不会有私钥信息。 KeyPairName：密钥对名称。

**示例**

`JSON` 格式

```json
{
 "ROSTemplateFormatVersion": "2015-09-01",
 "Parameters": {
  "KeyPairName": {
   "Type": "String",
   "Description": "SSH key pair name. It must be unique. [2, 128] characters. All character sets are
supported. Do not start with a special character, digit, http://, or https://. It can contain digits, \".\", \"_\", or \"-\"."
  },
  "ResourceGroupId": {
   "Type": "String",
   "Description": "Resource group id."
  },
  "Tags": {
   "Type": "Json",
   "Description": "Tags to attach to instance. Max support 20 tags to add during create instance. Eac
h tag with two properties Key and Value, and Key is required.",
   "MaxLength": 20
  },
  "PublicKeyBody": {
   "Type": "String",
   "Description": "SSH Public key. If PublicKeyBody is specified, existed public key body will be imp
orted instead of creating new SSH key pair."
  }
 },
 "Resources": {
  "SSHKeyPair": {
   "Type": "ALIYUN::ECS::SSHKeyPair",
   "Properties": {
```

资源编排

```json
    "KeyPairName": {
     "Ref": "KeyPairName"
    },
    "ResourceGroupId": {
     "Ref": "ResourceGroupId"
    },
    "Tags": {
     "Ref": "Tags"
    },
    "PublicKeyBody": {
     "Ref": "PublicKeyBody"
    }
   }
  }
 },
 "Outputs": {
  "KeyPairFingerPrint": {
   "Description": "The fingerprint of the key pair. The public key fingerprint format defined in RFC4
716: MD5 message digest algorithm. ",
   "Value": {
    "Fn::GetAtt": [
     "SSHKeyPair",
     "KeyPairFingerPrint"
```

]

```json
   }
  },
  "KeyPairName": {
   "Description": "SSH Key pair name.",
   "Value": {
    "Fn::GetAtt": [
     "SSHKeyPair",
     "KeyPairName"
```

]

```json
   }
  },
  "PrivateKeyBody": {
   "Description": "The private key of the key pair. Content of the RSA private key in the PKCS#8 form
at of the unencrypted PEM encoding. Refer to: https://www.openssl.org/docs/apps/pkcs8.html.User only can get the private key one time when and only when SSH key pair is created.",
   "Value": {
    "Fn::GetAtt": [
     "SSHKeyPair",
     "PrivateKeyBody"
```

]

```
   }
  }
 }
}
```

`YAML` 格式资源编排

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
 KeyPairName:
  Description: SSH key pair name. It must be unique. [2, 128] characters. All character
   sets are supported. Do not start with a special character, digit, http://, or
   https://. It can contain digits, ".", "_", or "-".
  Type: String
 PublicKeyBody:
  Description: SSH Public key. If PublicKeyBody is specified, existed public key
   body will be imported instead of creating new SSH key pair.
  Type: String
 ResourceGroupId:
  Description: Resource group id.
  Type: String
 Tags:
  Description: Tags to attach to instance. Max support 20 tags to add during create
   instance. Each tag with two properties Key and Value, and Key is required.
  MaxLength: 20
  Type: Json
Resources:
 SSHKeyPair:
  Properties:
   KeyPairName:
    Ref: KeyPairName
   PublicKeyBody:
    Ref: PublicKeyBody
   ResourceGroupId:
    Ref: ResourceGroupId
   Tags:
    Ref: Tags
Outputs:
 KeyPairFingerPrint:
  Description: 'The fingerprint of the key pair. The public key fingerprint format
   defined in RFC4716: MD5 message digest algorithm.'
  Value:
   Fn::GetAtt:
   - KeyPairFingerPrint
 KeyPairName:
  Description: SSH Key pair name.
  Value:
   Fn::GetAtt:
   - KeyPairName
 PrivateKeyBody:
  Description: 'The private key of the key pair. Content of the RSA private key
   in the PKCS#8 format of the unencrypted PEM encoding. Refer to:
https://www.openssl.org/docs/apps/pkcs8.html.User
   only can get the private key one time when and only when SSH key pair is created.'
  Value:
   Fn::GetAtt:
   - PrivateKeyBody
```

更多示例，请参见创建单个ECS实例、创建SSH密钥对和绑定SSH密钥和ECS实例的组合示例：JSON示例和YAML示例。

#### ALIYUN::ECS::SSHKeyPairAttachment

ALIYUN::ECS::SSHKeyPairAttachment类型用于绑定SSH密钥对到ECS实例。 资源编排

**语法**

```json
{
  "Type": "ALIYUN::ECS::SSHKeyPairAttachment",
  "Properties": {
    "InstanceIds": List,
    "KeyPairName": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| InstanceIds | List | 是 | 是 | 要绑定的ECS实例 ID列表 | ID之间用英文逗号 （,）分隔。 只支持Linux系统实例。 |
| KeyPairName | String | 是 | 否 | SSH密钥对的名称 | 无 |

**返回值**

Fn::GetAtt 无。

**示例**

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "SSHKeyPairAttachment": {
      "Type": "ALIYUN::ECS::SSHKeyPairAttachment",
      "Properties": {
        "KeyPairName": "ssh_key_pai****",
        "InstanceIds": [
          'i-2zeiofnh20hj8fej****',
          'i-2zebt3kfvxm28y9o****'
```

]

```
      }
    }
  }
}
```

#### ALIYUN::ECS::VPC

**语法**

资源编排

```json
{
  "Type": "ALIYUN::ECS::VPC",
  "Properties": {
    "Description": String,
    "Tags": List,
    "Ipv6CidrBlock": String,
    "EnableIpv6": Boolean,
    "ResourceGroupId": String,
    "VpcName": String,
    "CidrBlock": String,
    "Ipv6Isp": String,
    "UserCidr": String,
    "SecondaryCidrBlock": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ResourceGro upId | String | 否 | 是 | 资源组ID。 | 无 |
| VpcName | String | 否 | 是 | 专有网络名称。 | 长度为2~128个字符。必须以英文字母或汉字开头，不能以 http:// 或 https:// 开头。可包含英文字母、汉字、数字、下划线（ ）和短划线（-）。 _ |
| CidrBlock | String | 否 | 是 | 专有网络网段。 | 取值： 10.0.0.0/8 172.16.0.0/12 192.168.0.0/16及所包含的子网 |
| Description | String | 否 | 是 | 专有网络描述。 | 长度为2~256个字符。不能以 http:// 和 https:// 开头。 |
| Ipv6CidrBlock | String | 否 | 否 | 专有网络的 IPv6网段。 | 无 |
| EnableIpv6 | Boolean | 否 | 是 | 是否开启IPv6 网段。 | 取值： true：开启。 false（默认值）：关闭。 |
| Tags | List | 否 | 是 | 标签。 | 最多支持20个标签。 更多信息，请参见Tags属性。 |

资源编排

| Ipv6Isp | String | 否 | 否 | 专有网络的 IPv6地址段类型。 | 取值： BGP（默认值）：阿里云BGP IPv6。 ChinaMobile：中国移动（单线）。 ChinaUnicom：中国联通（单线）。 ChinaTelecom：中国电信（单线）。 说明如果是开通了单线带宽白名单的用户，该参数可以设置为 ChinaTelecom（中国电信）、ChinaUnicom（中国联通）和ChinaMobile（中国移动）。 |
|---|---|---|---|---|---|
| UserCidr | String | 否 | 否 | 用户网段。 | 如需定义多个网段，请使用半角逗号（,）分隔。最多支持3个网段。 |
| SecondaryCid rBlock | String | 否 | 否 | 辅助IPv4网段。 | 取值： 10.0.0.0/8 172.16.0.0/12 192.168.0.0/16及所包含的子网添加辅助IPv4网段时，需要遵循以下规则： 网段不能以0开头。 辅助IPv4网段不能与原有网段 （CidrBlock）相同。 子网掩码的长度必须为8~24比特。 |

**Tags语法**

```json
"Tags": [
  {
    "Value": String,
    "Key": String
  }
```

]

**Tags属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Key | String | 是 | 否 | 标签键。 | 长度为1~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或 https:// 。 |
| Value | String | 否 | 否 | 标签值。 | 长度为0~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或 https:// 。 |

**返回值**

Fn::GetAtt VpcId：专有网络ID。 资源编排 VRouterId：路由器ID。 RouteTableId：路由表ID。

**示例**

`YAML` 格式

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  CidrBlock:
    Type: String
    AssociationProperty: ALIYUN::VPC::VPC::CidrBlock
  VpcName:
    Type: String
    Description: Display name of the vpc instance, [2, 128] English or Chinese characters, must sta
rt with a letter or Chinese in size, can contain numbers, '_' or '.', '-' Resources:
  Vpc:
    Properties:
      CidrBlock:
        Ref: CidrBlock
      VpcName:
        Ref: VpcName
Outputs:
  VRouterId:
    Description: Router id of created VPC.
    Value:
      Fn::GetAtt:
        - Vpc
        - VRouterId
  RouteTableId:
    Description: The router table id of created VPC.
    Value:
      Fn::GetAtt:
        - Vpc
        - RouteTableId
  VpcId:
    Description: Id of created VPC.
    Value:
      Fn::GetAtt:
        - Vpc
        - VpcId
```

`JSON` 格式资源编排

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "CidrBlock": {
      "Type": "String",
      "AssociationProperty": "ALIYUN::VPC::VPC::CidrBlock"
    },
    "VpcName": {
      "Type": "String",
      "Description": "Display name of the vpc instance, [2, 128] English or Chinese characters, mus
t start with a letter or Chinese in size, can contain numbers, '_' or '.', '-'"
    }
  },
  "Resources": {
    "Vpc": {
      "Type": "ALIYUN::ECS::VPC",
      "Properties": {
        "CidrBlock": {
          "Ref": "CidrBlock"
        },
        "VpcName": {
          "Ref": "VpcName"
        }
      }
    }
  },
  "Outputs": {
    "VRouterId": {
      "Description": "Router id of created VPC.",
      "Value": {
        "Fn::GetAtt": [
          "Vpc",
          "VRouterId"
```

]

```json
      }
    },
    "RouteTableId": {
      "Description": "The router table id of created VPC.",
      "Value": {
        "Fn::GetAtt": [
          "Vpc",
          "RouteTableId"
```

]

```json
      }
    },
    "VpcId": {
      "Description": "Id of created VPC.",
      "Value": {
        "Fn::GetAtt": [
          "Vpc",
          "VpcId"
```

]

```
      }
    }
  }
}
```

更多示例，请参见创建专有网络、创建专有网络中的交换机、在SNAT列表中添加SNAT条目、创建共享带宽实例、添加EIP 到共享带宽中、创建IPv6网关和为IPv6地址购买公网带宽的组合示例：JSON示例和YAML示例。

#### ALIYUN::ECS::VSwitch

资源编排

**语法**

```json
{
  "Type": "ALIYUN::ECS::VSwitch",
  "Properties": {
    "VSwitchName": String,
    "VpcId": String,
    "Description": String,
    "Tags": List,
    "Ipv6CidrBlock": Integer,
    "ZoneId": String,
    "CidrBlock": String,
    "VpcIpv6CidrBlock": String,
    "ZoneType": String
  }
}
```

**属性**

|  | 属性名称 |  | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|---|---|
|  | VpcId |  | String | 是 | 否 | 要创建交换机的专有网络ID。 | 无 |
|  | ZoneId |  | String | 是 | 否 | 可用区ID。 | 无 |
|  | VSwitchNam e |  | String | 否 | 是 | 交换机名称。 | 长度为2~128个字符。必须以英文字母或汉字开头，不能以 http:// 或 https:// 开头。可包含英文字母、汉字、数字、下划线（ ）和短划线（-）。 _ |
|  |  | VSwitchNam |  |  |  |  |  |
|  | e |  |  |  |  |  |  |
|  | CidrBlock |  | String | 是 | 否 | 交换机网段。 | 必须是所属专有网络的子网段，并且没有被其他交换机占用。 |
|  |  | CidrBlock |  |  |  |  |  |
|  | Descriptio n |  | String | 否 | 是 | 交换机描述。 | 长度为2~256个字符。不能以 http:// 和 https:// 开头。 |
|  |  | Descriptio |  |  |  |  |  |
|  | n |  |  |  |  |  |  |
|  | Ipv6CidrBl ock |  | Integer | 否 | 否 | 交换机的IPv6 网段。 | 取值范围：0~255（十进制）。 交换机的IPv6网段掩码默认为64 位。 支持自定义VPC IPv6网段的最后8 位。 |
|  |  | Ipv6CidrBl | In |  |  |  |  |
|  | ock |  |  |  |  |  |  |
|  | Tags |  | List | 否 | 是 | 标签。 | 最多支持20个标签。 更多信息，请参见Tags属性。 |
|  | VpcIpv6Cid rBlock |  | String | 否 | 否 | 专有网络的 IPv6网段。 | 无 |
|  |  | VpcIpv6Cid | Strin |  |  |  |  |
|  | rBlock |  |  |  |  |  |  |
|  | ZoneType |  | String | 否 | 否 | 要查询的分区类型。 | 默认值： AvailabilityZone 。 |

**Tags语法**

资源编排

```json
"Tags": [
  {
    "Value": String,
    "Key": String
  }
```

]

**Tags属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Key | String | 是 | 否 | 标签键。 | 长度为1~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或 https:// 。 |
| Value | String | 否 | 否 | 标签值。 | 长度为0~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或 https:// 。 |

**返回值**

Fn::GetAtt CidrBlock：交换机的IPv4网段。 Ipv6CidrBlock：交换机的IPv6网段。 VSwitchId：交换机ID。

**示例**

`JSON` 格式资源编排

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "VSwitchZoneId": {
      "AssociationProperty": "ALIYUN::ECS::Instance:ZoneId",
      "Type": "String",
      "Description": "可用区ID",
      "Label": {
```

`"zh-cn": "`交换机可用区`",`

```json
        "en": "VSwitch Availability Zone"
      }
    }
  },
  "Resources": {
    "EcsVSwitch": {
      "Type": "ALIYUN::ECS::VSwitch",
      "Properties": {
        "VpcId": {
          "Ref": "EcsVpc"
        },
        "ZoneId": {
          "Ref": "VSwitchZoneId"
        },
        "CidrBlock": "192.168.0.0/24"
      }
    },
    "EcsVpc": {
      "Type": "ALIYUN::ECS::VPC",
      "Properties": {
        "CidrBlock": "192.168.0.0/16",
        "VpcName": {
          "Fn::Join": [
            "-",
```

[

```json
              "StackId",
              {
                "Ref": "ALIYUN::StackId"
              }
```

] ]

```json
        }
      }
    }
  },
  "Outputs": {
  }
}
```

更多示例，请参见创建专有网络、创建专有网络中的交换机、在SNAT列表中添加SNAT条目、创建共享带宽实例、添加EIP 到共享带宽中、创建IPv6网关和为IPv6地址购买公网带宽的组合示例：JSON示例和YAML示例。

### ESS

#### ALIYUN::ESS::AlarmTask

**语法**

资源编排

```json
{
  "Type": "ALIYUN::ESS::AlarmTask",
  "Properties": {
    "Statistics": String,
    "Name": String,
    "EvaluationCount": Integer,
    "Period": Integer,
    "MetricType": String,
    "ComparisonOperator": String,
    "Dimensions": List,
    "ScalingGroupId": String,
    "AlarmAction": List,
    "Threshold": Number,
    "MetricName": String,
    "GroupId": Integer,
    "Description": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Statistics | String | 否 | 否 | 统计方法，必须与定义的 metric一致，例如 Average。 | 可选值： Average,Minimum,Maxim um |
| Name | String | 否 | 是 | 报警规则名称。 | 无 |
| EvaluationCount | Integer | 否 | 否 | 连续探测几次都满足阈值条件时报警，默认3次。 | 最小为1。 |
| Period | Integer | 否 | 否 | 查询指标的周期，必须与定义的metric一致，默认 300，单位为秒 | 可用值： 60，120，300，900。 |
| MetricType | String | 否 | 否 | 标准类型。 | 可用值： sytem，custom。 |
| ComparisonOpera tor | String | 否 | 否 | 报警比较符。 | 只能为以下几种 <=，<，>，>= |
| Dimensions | List | 否 | 否 | 报警规则对应实例列表。 | 最少一个。 |
| ScalingGroupId | String | 是 | 否 | 伸缩组ID。 | 无 |
| AlarmAction | List | 是 | 是 | 报警动作列表。 | 最少1个，最多5个。 |
| Threshold | Number | 是 | 否 | 报警阈值，目前只开放数值类型功能。 | 无 |
| MetricName | String | 是 | 否 | 相应产品对应的监控项名称，参考各产品metric定义。 | 无 |
| GroupId | Integer | 否 | 否 | 组ID。 | 无 |
| Description | String | 否 | 是 | 描述。 | 无 |

**Dimensions语法**

资源编排

```json
"Dimensions": [
  {
    "DimensionKey": String,
    "DimensionValue": String
  }
```

]

**Dimensions属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| DimensionValue | String | 是 | 否 | 无 | 无 |
| DimensionKey | String | 是 | 否 | 无 | 无 |

**返回值**

Fn::GetAtt AlarmTaskId：报警任务ID。

**示例**

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "ComparisonOperator": {
      "Type": "String",
      "Description": "Comparison Operator",
      "AllowedValues": [
        ">=",
        "<=",
        ">",
        "<"
```

]

```json
    },
    "Description": {
      "Type": "String",
      "Description": "Description"
    },
    "ScalingGroupId": {
      "Type": "String",
      "Description": "The ID of the scaling group."
    },
    "MetricType": {
      "Type": "String",
      "Description": "Metric Type",
      "AllowedValues": [
        "system",
        "custom"
```

]

```json
    },
    "EvaluationCount": {
      "Type": "Number",
      "Description": "Evaluation Count",
      "MinValue": 1
    },
    "Period": {
      "Type": "Number",
      "Description": "Period",
      "AllowedValues": [
        60,
        120,
```

资源编排

```
        300,
```

]

```json
    },
    "Dimensions": {
      "Type": "CommaDelimitedList",
      "Description": "Dimensions",
      "MinLength": 1
    },
    "Statistics": {
      "Type": "String",
      "Description": "Statistics",
      "AllowedValues": [
        "Average",
        "Minimum",
        "Maximum"
```

]

```json
    },
    "Name": {
      "Type": "String",
      "Description": "Name"
    },
    "GroupId": {
      "Type": "Number",
      "Description": "Group Id"
    },
    "MetricName": {
      "Type": "String",
      "Description": "Metric Name"
    },
    "AlarmAction": {
      "Type": "CommaDelimitedList",
      "Description": "Alarm Actions",
      "MinLength": 1,
      "MaxLength": 5
    },
    "Threshold": {
      "Type": "Number",
      "Description": "Threshold"
    }
  },
  "Resources": {
    "AlarmTask": {
      "Type": "ALIYUN::ESS::AlarmTask",
      "Properties": {
        "ComparisonOperator": {
          "Ref": "ComparisonOperator"
        },
        "Description": {
          "Ref": "Description"
        },
        "ScalingGroupId": {
          "Ref": "ScalingGroupId"
        },
        "MetricType": {
          "Ref": "MetricType"
        },
        "EvaluationCount": {
          "Ref": "EvaluationCount"
        },
        "Period": {
          "Ref": "Period"
}
```

资源编排

```json
        },
        "Dimensions": {
          "Fn::Split": [
            ",",
            {
              "Ref": "Dimensions"
            },
            {
              "Ref": "Dimensions"
            }
```

]

```json
        },
        "Statistics": {
          "Ref": "Statistics"
        },
        "Name": {
          "Ref": "Name"
        },
        "GroupId": {
          "Ref": "GroupId"
        },
        "MetricName": {
          "Ref": "MetricName"
        },
        "AlarmAction": {
          "Fn::Split": [
            ",",
            {
              "Ref": "AlarmAction"
            },
            {
              "Ref": "AlarmAction"
            }
```

]

```json
        },
        "Threshold": {
          "Ref": "Threshold"
        }
      }
    }
  },
  "Outputs": {
    "AlarmTaskId": {
      "Description": "The alarm task ID",
      "Value": {
        "Fn::GetAtt": [
          "AlarmTask",
          "AlarmTaskId"
```

]

```
      }
    }
  }
}
```

#### ALIYUN::ESS::AlarmTaskEnable

ALIYUN::ESS::AlarmTaskEnable类型用于启动报警任务。当您的报警任务处于停止状态时，可以使用此接口启用报警任务。

**语法**

资源编排

```json
{
  "Type": "ALIYUN::ESS::AlarmTaskEnable",
  "Properties": {
    "AlarmTaskId": String,
    "Enable": Boolean
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| AlarmTaskId | String | 是 | 否 | 报警任务的ID。 | 无。 |
| Enable | Boolean | 是 | 是 | 是否启用。 | 无。 |

**返回值**

Fn::GetAtt 无

**示例**

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "Enable": {
      "Type": "Boolean",
      "Description": "Enable alarm task or not",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

]

```json
    },
    "AlarmTaskId": {
      "Type": "String",
      "Description": "The id of alarm task."
    }
  },
  "Resources": {
    "AlarmTaskEnable": {
      "Type": "ALIYUN::ESS::AlarmTaskEnable",
      "Properties": {
        "Enable": {
          "Ref": "Enable"
        },
        "AlarmTaskId": {
          "Ref": "AlarmTaskId"
        }
      }
    }
  },
  "Outputs": {}
}
```

#### ALIYUN::ESS::LifecycleHook

ALIYUN::ESS::LifecycleHook类型用于为一个伸缩组创建生命周期挂钩。 资源编排

**语法**

```json
{
  "Type": "ALIYUN::ESS::LifecycleHook",
  "Properties": {
    "LifecycleHookName": String,
    "NotificationArn": String,
    "HeartbeatTimeout": Integer,
    "NotificationMetadata": String,
    "ScalingGroupId": String,
    "DefaultResult": String,
    "LifecycleTransition": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| LifecycleHookNa me | String | 否 | 是 | 生命周期挂钩名称，不能与当前伸缩组其他生命周期挂钩重名。 | 长度为 [2, 40] 个英文或中文字符，以数字、大小字母或中文开头，可包含数字、 下划线（ ）、连字符（-） _ 和小数点（.）。 默认值：生命周期挂钩 ID。 |
| NotificationArn | String | 否 | 是 | 生命周期挂钩通知对象标识符。 | 目前我们支持消息服务 MNS 队列或主题，参数取值格式：acs:ess:{region}: {account-id}:{resource- relative-id}。 region ：伸缩组所在的地域 account-id ：阿里云账号 ID 例如： MNS 队列：acs:ess: {region}:{account- id}:queue/{queuenam e} MNS 主题：acs:ess: {region}:{account- id}:topic/{topicname} |
| HeartbeatTimeout | Integer | 否 | 是 | 生命周期挂钩为伸缩组活动设置的等待时间，等待状态超时后会执行下一步动作。 | 取值范围：[30, 21600]， 单位为秒。 默认值：600。 |

资源编排

| NotificationMetad ata | String | 否 |  |  |  | 伸缩活动的等待状态的固定字符串信息。 弹性伸缩每次推送消息到通知对象时，会同时发送您预先指定的 NotificationMetadata 参数值，便于管理和标记不同类别的通知信息。当您同时指定了 NotificationArn 参数时， NotificationMetad ata 参数方可生效。 |  |  | 参数长度不能超过 128 个字符。 |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  | NotificationMetadata |  |  |
|  |  |  |  |  | 是 |  |  |  |  |
|  |  |  |  |  |  |  |  | NotificationMetad |  |
|  |  |  |  |  |  | ata |  |  |  |
| ScalingGroupId | String | 是 |  |  | 否 | 伸缩组 ID。 |  |  | 无 |
| DefaultResult | String | 否 |  |  | 是 | 等待状态结束后的下一步动作。 当伸缩组发生弹性收缩活动 （ SCALE IN ）并触发多 _ 个生命周期挂钩时， DefaultResult=ABA NDON 的生命周期挂钩触发的等待状态结束时，会提前将其它对应的等待状态提前结束。其他情况下，下一步动作均以最后一个结束等待状态的下一步动作为准。 |  |  | 取值范围： CONTINUE：继续响应弹性扩张活动或者继续响应弹性收缩活动。 ABANDON：直接释放弹性扩张活动创建出来的 ECS 实例或者直接将弹性收缩活动中的 ECS 实例从伸缩组移除。 默认值：CONTINUE |
|  |  |  |  |  |  |  |  | DefaultResult=ABA | 性 |
|  |  |  |  |  |  | NDON |  |  |  |
| LifecycleTransitio n | String | 是 |  |  | 是 | 生命周期挂钩适用的伸缩活动类型。 |  |  | 取值范围： SCALE OUT：伸缩组弹 _ 性扩张活动 SCALE IN：伸缩组弹性 _ 收缩活动 |

**返回值**

Fn::GetAtt LifecycleHookId: 生命周期挂钩 ID。

**示例**

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "LifecycleHookName": {
      "Type": "String",
      "Description": "The name of the lifecycle hook. Each name must be unique within a scaling group
. The name must be 2 to 40 characters in length and can contain letters, numbers, Chinese characters, and special characters including underscores (_), hyphens (-) and periods (.).\nDefault value: Lifecy cle Hook ID",
      "AllowedPattern": "^[a-zA-Z0-9\\u4e00-\\u9fa5][-_.a-zA-Z0-9\\u4e00-\\u9fa5]{1,63}$"
    },
    "NotificationArn": {
      "Type": "String",
      "Description": "The Alibaba Cloud Resource Name (ARN) of the notification target that Auto Scal
ing will use to notify you when an instance is in the transition state for the lifecycle hook. This t arget can be either an MNS queue or an MNS topic. The format of the parameter value is acs:ess:{regio n}:{account-id}:{resource-relative-id}.\nregion: the region to which the scaling group locates\naccount-id: Alibaba Cloud ID\nFor example:\nMNS queue: acs:ess:{region}:{account-id}:queue/{ queuename}\nMNS topic: acs:ess:{region}:{account-id}:topic/{topicname}",
      "AllowedPattern": "^acs:ess:([a-zA-Z0-9-]+):(\\d+):(queue|topic)/([a-zA-Z0-9][a-zA-Z0-9-]
{0255})$"
```

资源编排

```json
{0,255})$",
      "MaxLength": 300
    },
    "ScalingGroupId": {
      "Type": "String",
      "Description": "The ID of the scaling group."
    },
    "LifecycleTransition": {
      "Type": "String",
      "Description": "The scaling activities to which lifecycle hooks apply Value range:\n SCALE_OUT:
scale-out event\n SCALE_IN: scale-in event",
      "AllowedValues": [
        "SCALE_OUT",
        "SCALE_IN"
```

]

```json
    },
    "HeartbeatTimeout": {
      "Type": "Number",
      "Description": "The time, in seconds, that can elapse before the lifecycle hook times out. If t
he lifecycle hook times out, the scaling group performs the default action (DefaultResult). The range is from 30 to 21,600 seconds. The default value is 600 seconds.\nYou can prevent the lifecycle hook f rom timing out by calling the RecordLifecycleActionHeartbeat operation. You can also terminate the li fecycle action by calling the CompleteLifecycleAction operation.",
      "MinValue": 30,
      "MaxValue": 21600
    },
    "NotificationMetadata": {
      "Type": "String",
      "Description": "The fixed string that you want to include when Auto Scaling sends a message abo
ut the wait state of the scaling activity to the notification target. The length of the parameter can be up to 128 characters. Auto Scaling will send the specified NotificationMetadata parameter along wi th the notification message so that you can easily categorize your notifications. The NotificationMetadata parameter will only take effect after you specify the NotificationArn parameter.
```

`",`

```json
      "MaxLength": 128
    },
    "DefaultResult": {
      "Type": "String",
      "Description": "The action that the scaling group takes when the lifecycle hook times out. Valu
e range:\n CONTINUE: the scaling group continues with the scale-in or scale-out process.\n ABANDON: t he scaling group stops any remaining action of the scale-in or scale-out event.\nDefault value: CONTI NUE\nIf the scaling group has multiple lifecycle hooks and one of them is terminated by the DefaultRe sult=ABANDON parameter during a scale-in event (SCALE_IN), the remaining lifecycle hooks under the sa me scaling group will also be terminated. Otherwise, the action following the wait state is the next action, as specified in the parameter DefaultResult, after the last lifecycle event under the same sc aling group.",
      "AllowedValues": [
        "CONTINUE",
        "ABANDON"
```

]

```json
    }
  },
  "Resources": {
    "LifecycleHook": {
      "Type": "ALIYUN::ESS::LifecycleHook",
      "Properties": {
        "LifecycleHookName": {
          "Ref": "LifecycleHookName"
        },
        "NotificationArn": {
          "Ref": "NotificationArn"
        },
        "ScalingGroupId": {
```

资源编排 g p

```json
          "Ref": "ScalingGroupId"
        },
        "LifecycleTransition": {
          "Ref": "LifecycleTransition"
        },
        "HeartbeatTimeout": {
          "Ref": "HeartbeatTimeout"
        },
        "NotificationMetadata": {
          "Ref": "NotificationMetadata"
        },
        "DefaultResult": {
          "Ref": "DefaultResult"
        }
      }
    }
  },
  "Outputs": {
    "LifecycleHookId": {
      "Description": "The lifecycle hook ID",
      "Value": {
        "Fn::GetAtt": [
          "LifecycleHook",
          "LifecycleHookId"
```

]

```
      }
    }
  }
}
```

#### ALIYUN::ESS::ScalingConfiguration

ALIYUN::ESS::ScalingConfiguration类型用于为伸缩组创建伸缩配置。

**语法**

资源编排

```json
{
  "Type": "ALIYUN::ESS::ScalingConfiguration",
  "Properties": {
    "PasswordInherit": Boolean,
    "DiskMappings": List,
    "RamRoleName": String,
    "IoOptimized": String,
    "InternetChargeType": String,
    "KeyPairName": String,
    "InstanceId": String,
    "InstanceTypes": List,
    "ImageId": String,
    "ResourceGroupId": String,
    "SpotStrategy": String,
    "InstanceType": String,
    "SystemDiskCategory": String,
    "SystemDiskSize": Integer,
    "SystemDiskAutoSnapshotPolicyId": String,
    "InternetMaxBandwidthOut": Integer,
    "InstanceName": String,
    "InternetMaxBandwidthIn": Integer,
    "ScalingConfigurationName": String,
    "UserData": String,
    "DeploymentSetId": String,
    "SecurityGroupId": String,
    "SpotPriceLimit": Number,
    "HpcClusterId": String,
    "ScalingGroupId": String,
    "SpotPriceLimitForInstanceType": Map,
    "TagList": List
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ResourceGroupId | String | 否 | 是 | 实例所在的资源组ID。 | 无。 |
| DeploymentSetId | String | 否 | 否 | 部署集ID。 | 无。 |
| HpcClusterId | String | 否 | 否 | 实例所属的EHPC集群ID。 | 无。 |
| ScalingGroupId | String | 是 | 否 | 伸缩配置所属的伸缩组ID。 | 无。 |
| DiskMappings | List | 否 | 是 | 需要挂载的磁盘。 | 最多支持16块磁盘。 |
| InternetChargeTy pe | String | 否 | 是 | 公网访问带宽计费方式。 | 取值范围： PayByBandwidth：按固定带宽计费 PayByTraffic：按流量计费默认值：PayByTraffic（按流量计费）。 |
| InternetMaxBand widthIn | Integer | 否 | 否 | 公网最大入网带宽。 | 单位：Mbps。 取值范围：1~100。 默认值：100。 |

资源编排

| InternetMaxBand widthOut | Integer | 否 | 是 | 公网最大出网带宽。 | 取值范围： 按固定带宽计费： 0~100。默认值：0。 按流量计费：1~200。此时，该参数为必选参数。 单位：Mbps。 |
|---|---|---|---|---|---|
| InstanceId | String | 否 | 否 | 伸缩配置的实例ID。 | 无。 |
| SystemDiskCateg ory | String | 否 | 是 | 系统盘类型。 | 取值范围： cloud：普通云盘。 cloud efficiency：高效 _ 云盘。 cloud ssd：SSD云盘。 _ ephemeral ssd：本地 _ SSD盘。 cloud essd：ESSD云 _ 盘。 当InstanceType为I系列的实例规格且实例属于非I/O优化实例时，默认值为cloud， 否则，默认值为 cloud efficiency。 _ |
| ImageId | String | 否 | 是 | 实例的镜像ID，包括公共镜像、自定义镜像和云市场镜像。 | 无。 |
| InstanceType | String | 否 | 是 | 实例规格。 | 无。 |
| SecurityGroupId | String | 否 | 是 | 实例所属的安全组。 | 无。 |
| IoOptimized | String | 否 | 是 | 是否创建I/O优化实例。 | 取值范围： none（非I/O优化） optimized（I/O优化） 默认值：none。 |
| ScalingConfigurati onName | String | 否 | 是 | 伸缩配置的名称。 | 2~64个英文或中文字符，以数字、大小写字母或中文开头，可包含数字、下划线（ ）、连字符 _ （-）或（.）。 在同一地域下同一伸缩组内伸缩配置名称唯一。 如果您没有指定本参数， 则默认使用伸缩配置的 ID。 |
| KeyPairName | String | 否 | 是 | 实例绑定的密钥对名称。 | 如果实例类型为Windows 实例，则此参数将被忽略，默认值为空。 如果实例类型为Linux实例，则密码登录方式会被初始化为禁止。 |
| RamRoleName | String | 否 | 是 | 实例RAM角色名称。 | 您可以使用RAM APIListRoles查询实例RAM 角色名称。 |

资源编排

| SystemDiskSize |  | Integer | 否 |  |  | 是 | 系统盘大小。 |  | 取值范围：40~500。 单位：GB。 如果使用自定义镜像创建系统盘，则系统盘大小必须大于自定义镜像大小。 |  |
|---|---|---|---|---|---|---|---|---|---|---|
| UserData |  | String | 否 |  |  | 是 | 创建实例时传递的用户数据。 |  | 内容需要限制在16KB以内， 无需Base64转码，特殊字符需要使用反斜杠转义。 |  |
| InstanceTypes |  | List | 否 |  |  | 是 | 多实例规格参数。如果指定了InstanceTypes，则 InstanceType无效。 |  | 一个伸缩配置内最多可以设置10种实例规格，优先级按列表元素的顺序依次降低。 当无法根据优先级较高的实例规格创建出实例时，弹性伸缩服务会自动选择下一优先级的实例规格来创建实例。 |  |
| PasswordInherit |  | Boolean | 否 |  |  | 是 | 是否使用镜像预设的密码。 |  | 使用此参数时，您需要确保所用镜像已经预设了密码。 |  |
| TagList |  | List | 否 |  |  |  |  |  | 标签以键值对方式传入，最多可以使用5组标签，格式为 {"key1": "value1", |  |
|  |  |  |  |  |  |  |  |  |  | {"key1": "value1", |
|  |  |  |  |  |  |  |  |  | "key2": "value2", ... |  |
|  |  |  |  |  |  |  |  |  | "key5": "value5"} |  |
|  |  |  |  |  |  | 是 | 实例标签。 |  |  |  |
| SpotStrategy |  | String | 否 |  |  | 是 | 后付费实例的抢占策略。 |  | 取值范围： NoSpot（正常按量付费实例） SpotWithPriceLimit（设置上限价格的抢占式实例） SpotAsPriceGo（系统自动出价，跟随当前市场实际价格）。 默认值：NoSpot。 |  |
| InstanceName |  | String | 否 |  |  | 是 | 基于当前伸缩配置创建的实例的名称。 |  | 无。 |  |
| SpotPriceLimit |  | Number | 否 |  |  | 是 | 实例每小时的最高价格。 |  | 支持最多3位小数。且仅当 SpotStrategy取值为 SpotWithPriceLimit时，此参数生效，并且此参数的取值可以被 SpotPriceLimitForInstanc eType的取值所覆盖。 |  |
| SpotPriceLimitForI nstanceType |  | Map | 否 |  |  |  |  |  | 格式为 {“<instance type 1 _ _ |  |
|  |  |  |  |  |  |  |  |  |  | {“<instance type 1 _ _ |
|  |  |  |  |  |  |  |  |  | >": <price limit 1>, _ _ |  |
|  |  |  |  |  |  |  |  |  | ..., |  |
|  |  |  |  |  |  | 是 | 抢占式实例的实例规格和对 |  | {“<instance type 10>": _ _ |  |
|  |  |  |  |  |  |  | 应的出价。 |  | <price limit 10>} _ _ |  |

资源编排

| SystemDiskAutoS napshotPolicyId | String | 否 | 是 | 数据盘使用的自动快照策略 ID。 | 无。 |
|---|---|---|---|---|---|

**DiskMappings语法**

```json
"DiskMappings": [
  {
    "Category": String,
    "Device": String,
    "SnapshotId": String,
    "Size": String,
    "Encrypted": String,
    "KMSKeyId": String,
    "Description": String,
    "DiskName": String
  }
```

]

**DiskMappings属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Size | String | 是 | 否 | 数据盘磁盘大小。 | 取值范围： cloud：5~2000 cloud efficiency： _ 20~32768 cloud ssd：20~32768 _ cloud essd：20~32768 _ ephemeral ssd：5~800 _ 指定此参数后，磁盘大小必须大于等于快照大小（快照通过 SnapshotId指定）。 单位：GiB。 |
| Category | String | 否 | 否 | 数据盘类型。 | 取值范围：cloud、 cloud efficiency、 _ cloud ssd、 _ ephemeral ssd、 _ cloud essd。对于I/O优化实 _ 例，默认值为 cloud efficiency；对于非I/O _ 优化实例，默认值为cloud。 |
| DiskName | String | 否 | 否 | 数据盘名称。 | 长度为2~128个字符。可以包含数字、半角冒号（:）、下划线（ ）或者连字符（-），必 _ 须以英文字母或中文开头，不能以 http:// 或 https:// 开头。 |
| Description | String | 否 | 否 | 数据盘描述。 | 长度为2~256个字符。不能以 http:// 或 https:// 开头。 |
| Device | String | 否 | 否 | 数据盘挂载点。 | 如果此参数值未指定，则默认将在自动创建ECS实例时由系统分配，取值从/dev/xvdb开始，到/dev/xvdz结束。 |

资源编排

| SnapshotId | String | 否 | 否 | 创建数据盘时使用的快照。 | 指定此参数后，Size会被忽略，实际创建的磁盘大小为指定快照的大小。如果快照创建于2013年7月15日或之前，调用快照会被拒绝，返回参数中会提示 InvalidSnapshot.TooOld。 |
|---|---|---|---|---|---|
| Encrypted | String | 否 | 否 | 数据盘是否加密。 | 默认值：false。 |
| KMSKeyId | String | 否 | 否 | 数据盘对应的KMS密钥ID。 | 无。 |

**返回值**

Fn::GetAtt ScalingConfigurationId：伸缩配置的ID。由系统生成，全局唯一。

**示例**

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "ScalingConfiguration": {
      "Type": "ALIYUN::ESS::ScalingConfiguration",
      "Properties": {
        "ImageId": "ubuntu1404_64_20G_aliaegis_2015****.vhd",
        "InstanceType": "ecs.t1.small",
        "InstanceId": "i-25xhh****",
        "InternetChargeType": "PayByTraffic",
        "InternetMaxBandwidthIn": 1,
        "InternetMaxBandwidthOut": 20,
        "SystemDisk_Category": "cloud",
        "ScalingGroupId": "bwhtvpcBcKYac9fe3vd0****",
        "SecurityGroupId": "sg-25zwc****",
        "DiskMappings": [
          {
            "Size": 10
          },
          {
            "Category": "cloud",
            "Size": 10
          }
```

]

```json
      }
    }
  },
  "Outputs": {
    "ScalingConfiguration": {
      "Value": {"get_attr": ["ScalingConfigurationId"]}
    }
  }
}
```

#### ALIYUN::ESS::ScalingGroup

ALIYUN::ESS::ScalingGroup类型用于创建伸缩组。伸缩组是具有相同应用场景的ECS实例的集合，创建成功后不会立即生效，需要使用ALIYUN::ESS::ScalingGroupEnable启用伸缩组，才能触发伸缩活动，执行伸缩规则。

**语法**

资源编排

```json
{
  "Type": "ALIYUN::ESS::ScalingGroup",
  "Properties": {
    "MultiAZPolicy": String,
    "DesiredCapacity": Integer,
    "NotificationConfigurations": List,
    "ProtectedInstances": List,
    "LaunchTemplateId": String,
    "LaunchTemplateVersion": String,
    "ScalingGroupName": String,
    "VSwitchIds": List,
    "DefaultCooldown": Integer,
    "MinSize": Integer,
    "GroupDeletionProtection": Boolean,
    "MaxSize": Integer,
    "InstanceId": String,
    "VSwitchId": String,
    "LoadBalancerIds": List,
    "StandbyInstances": List,
    "RemovalPolicys": List,
    "HealthCheckType": String,
    "DBInstanceIds": List,
    "Tags": List,
    "OnDemandPercentageAboveBaseCapacity": Integer,
    "CompensateWithOnDemand": Boolean,
    "ContainerGroupId": String,
    "ScalingPolicy": String,
    "SpotInstanceRemedy": Boolean,
    "SpotInstancePools": Integer,
    "OnDemandBaseCapacity": Integer,
    "GroupType": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| MinSize | Integer | 是 | 是 | 伸缩组内ECS实例个数的最小值。 | 取值范围：0~1000。 当伸缩组内ECS实例数小于MinSize 时，弹性伸缩会自动创建ECS实例。 |
| MaxSize | Integer | 是 | 是 | 伸缩组内ECS实例个数的最大值。 | 取值范围：0~1000。 当伸缩组内ECS实例数大于 MaxSize时，弹性伸缩会自动移出 ECS实例。 |
| ScalingGroup Name | String | 否 | 是 | 伸缩组的显示名称。 | 长度为2~64个字符。以数字、英文字母或汉字开头，可包含英文字母、汉字、数字、下划线（ ）、短 _ 划线（-）和半角句号（.）。 同一账号同一地域内名称唯一。 默认值：ScalingGroupId。 |
| LaunchTempl ateId | String | 否 | 是 | 实例启动模板 ID，用于指定伸缩组从实例启动模板获取启动配置信息。 | 无 |

资源编排

| LaunchTempl ateVersion | String | 否 | 是 | ECS实例启动模板的版本。 | 取值： 固定的模板版本号。 Default：始终使用模板默认版本。 Latest：始终使用模板最新版本。 |
|---|---|---|---|---|---|
| RemovalPolic ys | List | 否 | 是 | ECS实例移出伸缩组的策略。 | 取值： OldestInstance（默认值）：移出最早加入伸缩组的ECS实例。 NewestInstance：移出最新加入伸缩组的ECS实例。 OldestScalingConfiguration（ 默认值）：移出最早伸缩配置创建的ECS实例。 |
| VSwitchId | String | 否 | 否 | 交换机ID。 | 无 |
| LoadBalancer Ids | List | 否 | 是 | 负载均衡实例的 ID。 | 取值可以是由多台负载均衡实例ID 组成一个JSON数组，最多支持5个 ID，ID之间用半角逗号（,）隔开。 |
| DefaultCoold own | Integer | 否 | 是 | 一次伸缩活动 （添加或移出 ECS实例）结束后的一段冷却时间。 | 取值范围：0~86,400。 单位：秒。 默认值：300 。 冷却时间内，该伸缩组不执行其它的伸缩活动，仅针对云监控报警任务触发的伸缩活动有效。 |
| DBInstanceId s | List | 否 | 是 | 云数据库RDS 版实例的ID。 | 取值可以是由多台RDS实例ID组成一个JSON数组，最多支持8个 ID，ID之间用半角逗号（,）隔开。 |
| VSwitchIds | List | 否 | 否 | 多个交换机 ID。 | 最多可指定5个交换机ID。当指定 VSwitchIds时，将忽略VSwitchId 的值。交换机的优先级按照指定顺序依次减小。 当优先级较高的虚拟交换机所在可用区无法创建ECS实例时，自动选择下一优先级的虚拟交换机创建ECS实例。 |
| MultiAZPolicy | String | 否 | 否 | 多可用区伸缩组 ECS实例扩缩容策略。 | 取值： PRIORITY：根据您定义的虚拟交换机扩缩容。当优先级较高的虚拟交换机所在可用区无法创建 ECS实例时，自动使用下一优先级的虚拟交换机创建ECS实例。 BALANCE：在伸缩组指定的多可用区之间均匀分配ECS实例。 COST OPTIMIZED：按vCPU单 _ 价从低到高进行尝试创建。当伸缩配置设置了抢占式计费方式的多实例规格时，优先创建对应抢占式计费实例。当抢占式计费实例由于库存等原因无法创建时， 自动尝试以按量付费的方式创建。 |
| NotificationC onfigurations | List | 否 | 是 | 事件及资源变化通知的配置列表。 | 更多信息，请参见NotificationConfigurations属性。 |
| ProtectedInst ances | List | 否 | 是 | 伸缩组内处于保护模式的ECS实例个数。 | 最多支持1000个实例。 |

资源编排

| StandbyInsta nces | List | 否 | 是 | 伸缩组内处于备用模式的ECS实例个数。 | 最多支持1000个实例。 |
|---|---|---|---|---|---|
| HealthCheckT ype | String | 否 | 是 | 健康检查类型。 | 取值： ECS NONE |
| GroupDeletio nProtection | Boolean | 否 | 是 | 是否开启伸缩组删除保护。 | 取值： true：开启伸缩组删除保护，此时不能删除该伸缩组。 false（默认值）：关闭伸缩组删除保护。 |
| DesiredCapac ity | Integer | 否 | 是 | 伸缩组内ECS实例的期望数量， 伸缩组会自动将 ECS实例数量维持在期望实例数。 | 取值大于等于MinSize，小于等于 MaxSize。 |
| InstanceId | String | 否 | 否 | ECS实例的ID。 创建伸缩组时， 将从指定的实例获取所需的配置信息，并自动创建伸缩配置。 | 无 |
| Tags | List | 否 | 是 | 标签。 | 最多支持添加20个标签。 更多信息，请参见Tags属性。 |
| OnDemandPe rcentageAbov eBaseCapacit y | Integer | 否 | 是 | 超出的实例中按量实例应占的比例。 | 伸缩组满足最小按量实例数 （OnDemandBaseCapacity）要求后，超出的实例中按量实例应占的比例。 取值范围：0～100。 |
| Compensate WithOnDema nd | Boolean | 否 | 是 | 是否允许自动尝试创建满足ECS 实例数要求的按量实例。 | 当MultiAZPolicy取值为 COST OPTIMIZED时，如果因价 _ 格、库存等原因无法创建足够的抢占式实例，是否允许自动尝试创建满足ECS实例数要求的按量实例。 取值： true（默认值）：允许。 false：不允许。 |
| ContainerGro upId | String | 否 | 否 | ECI实例ID。 | 无 |
| ScalingPolicy | String | 否 | 否 | 指定伸缩组的回收模式。 | 取值： recycle：停机模式。 release：释放模式。 ScalingPolicy指定伸缩组的回收模式，但实例被移出伸缩组时的具体动作，由RemoveInstances的 RemovePolicy参数决定。 |

资源编排

| SpotInstance Remedy | Boolean | 否 | 是 | 是否开启补齐抢占式实例。 | 取值： true：开启补齐抢占式实例。 开启后，当收到抢占式实例将被回收的系统消息时，伸缩组将尝试创建新的实例，替换掉将被回收的抢占式实例。 false：未开启补齐抢占式实例。 |
|---|---|---|---|---|---|
| SpotInstance Pools | Integer | 否 | 是 | 指定可用实例规格的个数。 | 伸缩组将按成本最低的多个规格均衡创建抢占式实例。 取值范围：1~10。 |
| OnDemandBa seCapacity | Integer | 否 | 是 | 伸缩组所需要按量实例个数的最小值。 | 取值范围：0~1000。 当按量实例个数少于该值时，将优先创建按量实例。 |
| GroupType | String | 否 | 否 | 伸缩组管理的实例类型。 | 取值： ECS（默认值）：伸缩组内管理的伸缩为ECS实例。 ECI：伸缩组内管理的伸缩为ECI 实例。 |

**NotificationConfigurations语法**

```json
"NotificationConfigurations": [
  {
    "NotificationArn": String,
    "NotificationTypes": List
  }
```

]

**NotificationConfigurations属性**

| 属性名称 | 类型 | 必须 | 允许更新 |  | 描述 |  | 约束 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
| NotificationAr n | String | 是 | 否 |  | 生命周期挂钩通 |  | 取值格式： MNS队列： acs:ess: |  |  |  |
|  |  |  |  |  |  |  |  | acs:ess: |  |  |
|  |  |  |  |  |  | 挂钩通 | {region}:{account- |  |  |  |
|  |  |  |  |  | 知对象标识符， 支持消息服务 | 识符， |  |  |  |  |
|  |  |  |  |  |  |  | id}:queue/{queuename} |  | 。 |  |
|  |  |  |  |  | MNS队列或主题。 |  | MNS主题： | acs:ess: |  |  |
|  |  |  |  |  |  |  | {region}:{account- |  |  |  |
|  |  |  |  |  |  |  | id}:topic/{topicname} |  |  |  |
| NotificationTy pes | List | 是 | 否 |  | ESS事件和资源更改通知类型。 |  | 无 |  |  |  |

**Tags语法**

```json
"Tags": [
  {
    "Key": String,
    "Value": String
  }
```

]

**Tags属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|

资源编排

| Key | String | 是 | 否 | 标签键。 | 长度为1~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |
|---|---|---|---|---|---|
| Value | String | 否 | 否 | 标签值。 | 长度为0~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |

**返回值**

Fn::GetAtt ScalingGroupId：伸缩组的ID。 ScalingGroupName：伸缩组名称。

**示例**

`YAML` 格式

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  VPC:
    Type: String
    Label:
```

`zh-cn:` 现有`VPC`的实例`ID`

```
      en: Existing VPC Instance ID
  VSwitch:
    AssociationProperty: ALIYUN::ECS::VSwitch::VSwitchId
    Type: String
    Label:
```

`zh-cn:` 网络交换机`ID`

```
      en: VSwitch ID
    AssociationPropertyMetadata:
      VpcId: ${VPC}
  LaunchTemplateId:
    AssociationProperty: ALIYUN::ECS::LaunchTemplate::LaunchTemplateId
    Type: String
  MaxSize:
    Type: Number
    Description: 'Maximum number of ECS instances in the scaling group. Value range: [0, 1000].'
    MinValue: 0
    MaxValue: 1000
    Default: 3
  ScalingGroupName:
    Type: String
    Description: |-
      Name shown for the scaling group, which must contain 2-40 characters (English or Chinese). Th
e name must begin with a number, an upper/lower-case letter or a Chinese character and may contain numbers, "_", "-" or ".". The account name is unique in the same region.
      If this parameter is not specified, the default value is ScalingGroupId.
    AllowedPattern: ^[a-zA-Z0-9\u4e00-\u9fa5][-_.a-zA-Z0-9\u4e00-\u9fa5]{1,63}$
  MinSize:
    Type: Number
    Description: 'Minimum number of ECS instances in the scaling group. Value range: [0, 1000].'
    MinValue: 0
    MaxValue: 1000
    Default: 0
Resources:
  ScalingGroup:
Properties:
```

资源编排

```
    Properties:
      VpcId:
        Ref: VPC
      VSwitchId:
        Ref: VSwitch
      LaunchTemplateId:
        Ref: LaunchTemplateId
      MaxSize:
        Ref: MaxSize
      ScalingGroupName:
        Ref: ScalingGroupName
      MinSize:
        Ref: MinSize
Outputs:
  ScalingGroupId:
    Description: Scaling group Id
    Value:
      Fn::GetAtt:
        - ScalingGroupId
  ScalingGroupName:
    Description: Scaling group name
    Value:
      Fn::GetAtt:
        - ScalingGroupName
```

`JSON` 格式

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "VPC": {
      "AssociationProperty": "ALIYUN::ECS::VPC::VPCId",
      "Type": "String",
      "Label": {
```

`"zh-cn": "`现有`VPC`的实例`ID",`

```json
        "en": "Existing VPC Instance ID"
      }
    },
    "VSwitch": {
      "AssociationProperty": "ALIYUN::ECS::VSwitch::VSwitchId",
      "Type": "String",
      "Label": {
```

`"zh-cn": "`网络交换机`ID",`

```json
        "en": "VSwitch ID"
      },
      "AssociationPropertyMetadata": {
        "VpcId": "${VPC}"
      }
    },
    "LaunchTemplateId":{
      "AssociationProperty":"ALIYUN::ECS::LaunchTemplate::LaunchTemplateId",
      "Type":"String"
    },
    "MaxSize": {
      "Type": "Number",
      "Description": "Maximum number of ECS instances in the scaling group. Value range: [0, 1000].
```

`",`

```json
      "MinValue": 0,
      "MaxValue": 1000,
      "Default": 3
    },
```

资源编排

```json
    "ScalingGroupName": {
      "Type": "String",
      "Description": "Name shown for the scaling group, which must contain 2-40 characters (English
or Chinese). The name must begin with a number, an upper/lower-case letter or a Chinese character a nd may contain numbers, \"_\", \"-\" or \".\". The account name is unique in the same region.\nIf t his parameter is not specified, the default value is ScalingGroupId.",
      "AllowedPattern": "^[a-zA-Z0-9\\u4e00-\\u9fa5][-_.a-zA-Z0-9\\u4e00-\\u9fa5]{1,63}$"
    },
    "MinSize": {
      "Type": "Number",
      "Description": "Minimum number of ECS instances in the scaling group. Value range: [0, 1000].
```

`",`

```json
      "MinValue": 0,
      "MaxValue": 1000,
      "Default": 0
    }
  },
  "Resources": {
    "ScalingGroup": {
      "Type": "ALIYUN::ESS::ScalingGroup",
      "Properties": {
        "VpcId": {
          "Ref": "VPC"
        },
        "VSwitchId": {
          "Ref": "VSwitch"
        },
        "LaunchTemplateId": {
          "Ref": "LaunchTemplateId"
        },
        "MaxSize": {
          "Ref": "MaxSize"
        },
        "ScalingGroupName": {
          "Ref": "ScalingGroupName"
        },
        "MinSize": {
          "Ref": "MinSize"
        }
      }
    }
  },
  "Outputs": {
    "ScalingGroupId": {
      "Description": "Scaling group Id",
      "Value": {
        "Fn::GetAtt": [
          "ScalingGroup",
          "ScalingGroupId"
```

]

```json
      }
    },
    "ScalingGroupName": {
      "Description": "Scaling group name",
      "Value": {
        "Fn::GetAtt": [
          "ScalingGroup",
          "ScalingGroupName"
```

]

```
      }
    }
  }
}
```

资源编排

```
}
```

当伸缩组中仅定义了一个伸缩组配置，且伸缩组配置中包含依赖的其他资源，您需要在定义资源模板时为伸缩组设置 DependsOn属性，对伸缩组配置依赖的其他资源设置资源依赖关联。 伸缩组ScalingGroup设置DependsOn依赖关系到安全组SecurityGroup，因为伸缩组配置ScalingConfiguration依赖了安全组SecurityGroup资源。

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  VpcId:
    Type: String
  VSwitchId:
    AssociationProperty: ALIYUN::ECS::VSwitch::VSwitchId
    Type: String
    AssociationPropertyMetadata:
      VpcId: VpcId
  SystemDiskCategory:
    Type: String
    Default: cloud_essd
  InstanceType:
    Type: String
    Default: ecs.g6e.large
  ImageId:
    Type: String
    Default: centos_7_04_64_20G_alibase_201701015.vhd
Resources:
  ScalingGroupEnable:
    Properties:
      ScalingConfigurationId:
        Ref: ScalingConfiguration
      ScalingGroupId:
        Ref: ScalingGroup
      ScalingRuleArisExecuteVersion: 0
  SecurityGroup:
    Properties:
      SecurityGroupName:
        Ref: ALIYUN::StackName
      VpcId:
        Ref: VpcId
      SecurityGroupIngress:
        - PortRange: '-1/-1'
          Priority: 1
          SourceCidrIp: 0.0.X.X/0
          IpProtocol: all
          NicType: internet
      SecurityGroupEgress:
        - PortRange: '-1/-1'
          Priority: 1
          IpProtocol: all
          DestCidrIp: 0.0.X.X/0
          NicType: internet
        - PortRange: '-1/-1'
          Priority: 1
          IpProtocol: all
          DestCidrIp: 0.0.X.X/0
          NicType: intranet
  ScalingConfiguration:
    DependsOn: ScalingGroup
    Properties:
```

资源编排

```
      InstanceType:
        Ref: InstanceType
      ImageId:
        Ref: ImageId
      SystemDiskCategory:
        Ref: SystemDiskCategory
      SystemDiskSize: 100
      ScalingConfigurationName:
        Ref: ALIYUN::StackName
      ScalingGroupId:
        Ref: ScalingGroup
      SecurityGroupId:
        Ref: SecurityGroup
  ScalingGroup:
    DependsOn: SecurityGroup
    Properties:
      MaxSize: 3
      MinSize: 0
      DefaultCooldown: 15
      VpcId:
        Ref: VpcId
      VSwitchId:
        Ref: VSwitchId
Outputs: {}
```

更多示例，请参见创建伸缩组、创建伸缩规则、创建监控项报警任务、启动报警任务、为伸缩组创建生命周期挂钩和创建定时任务的组合示例：JSON示例和YAML示例。

#### ALIYUN::ESS::ScalingGroupEnable

**语法**

```json
{
  "Type": "ALIYUN::ESS::ScalingGroupEnable",
  "Properties": {
    "ScalingConfigurationId": String,
    "ScalingRuleArisExecuteVersion": Integer,
    "ScalingRuleAris": List,
    "ScalingGroupId": String,
    "RemoveInstanceIds": List,
    "InstanceIds": List
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ScalingGroupId | String | 是 | 否 | 伸缩组的ID | 无 |
| ScalingConfigura tionId | String | 否 | 否 | 需要在伸缩组内激活的伸缩配置的ID | 无 |
| InstanceIds | List | 否 | 是 | 启用后需要加入伸缩组的ECS实例的 ID | 最多支持20个 |

资源编排

| ScalingRuleArisE xecuteVersion | Integer | 否 | 是 | 伸缩规则标识符执行版本。改变属性会执行一次 ScalingRuleAris 中的所有的缩放规则。 | 最小值：0 |
|---|---|---|---|---|---|
| ScalingRuleAris | List | 否 | 是 | 伸缩规则的唯一标识符列表，查询结果会忽略失效的伸缩规则唯一标识符，并且不报错。 | 最多支持10个 |
| RemoveInstance Ids | List | 否 | 是 | 待删除ECS实例的 ID列表 | 最多支持1000个 |

**返回值**

Fn::GetAtt LifecycleState: 伸缩组的状态。 ScalingInstances: 伸缩组自动创建的实例。 ScalingGroupId: 伸缩组ID。 ScalingRuleArisExecuteResultInstancesRemoved: 通过执行伸缩规则aris删除实例。 ScalingRuleArisExecuteResultNumberOfAddedInstances: 通过执行伸缩规则aris添加的vm数量。 ScalingInstanceDetails: 伸缩实例的详细信息。 ScalingRuleArisExecuteErrorInfo: 执行伸缩规则aris的错误信息。 ScalingRuleArisExecuteResultInstancesAdded: 通过执行伸缩规则aris添加实例。

**示例**

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "ScalingGroupEnable": {
      "Type": "ALIYUN::ESS::ScalingGroupEnable",
      "Properties": {
        "ScalingGroupId": "r0HUqbJ411cc2eQw8bU****",
        "ScalingConfigurationId": "bJlLfdexm77Ldsyptmel****",
        "InstanceIds": "",
      }
    }
  },
  "Outputs": {
    "ScalingGroupEnable": {
      "Value": {"Fn::GetAtt": ["ScalingGroupEnable", "LifecycleState"]}
    }
  }
}
```

#### ALIYUN::ESS::ScalingRule

**语法**

资源编排

```json
{
  "Type": "ALIYUN::ESS::ScalingRule",
  "Properties": {
    "AdjustmentValue": Integer,
    "Cooldown": Integer,
    "ScalingGroupId": String,
    "AdjustmentType": String,
    "ScalingRuleName": String,
    "MetricName": String,
    "PredictiveTaskBufferTime": Integer,
    "ScalingRuleType": String,
    "PredictiveValueBuffer": Integer,
    "TargetValue": Number,
    "StepAdjustment": List,
    "PredictiveValueBehavior": String,
    "DisableScaleIn": Boolean,
    "InitialMaxSize": Integer,
    "MinAdjustmentMagnitude": Integer,
    "EstimatedInstanceWarmup": Integer,
    "PredictiveScalingMode": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| AdjustmentVal ue | Integer | 否 | 是 | 伸缩规则的调整值，适用于简单规则和步进规则。 | 不同调整方式对应的取值范围： QuantityChangeInCap acity：-500~500。 PercentChangeInCapa city：-100~10,000。 TotalCapacity： 0~1000。 说明任何情况下，单次调整的ECS实例台数都不能超过 500。 |
| Cooldown | Integer | 否 | 是 | 伸缩规则的冷却时间，仅适用于简单规则。 | 取值范围：0~86400。 单位：秒。 默认值：空。 |
| ScalingGroupId | String | 是 | 否 | 伸缩规则所属的伸缩组ID。 | 无 |
| AdjustmentTyp e | String | 否 | 是 | 伸缩规则的调整方式，适用于简单规则和步进规则。 | 取值： QuantityChangeInCap acity：增加或减少指定数量的ECS实例。 PercentChangeInCapa city：增加或减少指定比例的ECS实例。 TotalCapacity： 将当前伸缩组的ECS实例数量调整到指定数量。 |

资源编排

| ScalingRuleNa me | String | 否 | 是 | 伸缩规则的名称。 | 长度为2~64个字符，以数字、字母或汉字开头。可包含数字、字母、汉字、下划线（ ）、短划线（-）和英 _ 文句点（.）。 如果没有指定该参数，默认为ScalingRuleId的取值。 |
|---|---|---|---|---|---|
| MetricName | String | 否 | 否 | 预定义监控项， 适用于目标追踪规则和预测规则。 | 取值： 目标追踪规则： CpuUtilization：平均 CPU使用率。 ClassicInternetRx： 经典网络公网入流量平均值。 ClassicInternetTx： 经典网络公网出流量平均值。 VpcInternetRx：专有网络公网入流量平均值。 VpcInternetTx：专有网络公网出流量平均值。 IntranetRx：内网入流量平均值。 IntranetTx ：内网出流量平均值。 预测规则： CpuUtilization：平均 CPU使用率。 IntranetRx：内网入流量平均值。 IntranetTx ：内网出流量平均值。 |
| PredictiveTask BufferTime | Integer | 否 | 否 | 预测规则自动创建的预测任务， 默认在整点执行。您可以设置预启动时间提前执行预测任务， 预先准备资源。 | 取值范围：0~60。 单位：分钟。 默认值：0。 |

资源编排

| ScalingRuleTyp e | String | 否 | 否 | 伸缩规则类型。 | 取值： SimpleScalingRule（默认值）：简单规则。根据调整方式 （AdjustmentType）和调整值 （AdjustmentValue） 调整ECS实例数量。 TargetTrackingScaling Rule：目标追踪规则。根据预定义监控项 （MetricName）动态计算需要扩缩容的ECS实例数量，尽量将预定义监控项的指标值维持在目标值 （TargetValue）附近。 StepScalingRule： 步进规则，根据阈值和指标值提供分步扩展方式。 PredictiveScalingRule ：预测规则，基于机器学习能力分析伸缩组的历史监控数据预测未来监控指标值，并支持自动创建定时任务设置伸缩组边界。 |
|---|---|---|---|---|---|
| PredictiveValu eBuffer | Integer | 否 | 否 | PredictiveValu eBehavior为 PredictiveValu eOverrideMax WithBuffer时生效，预测值会按照该比例增加， 当增加后的值大于初始最大值时，会采用增加后的值。 | 取值范围：0~100。 默认值：0。 |
| TargetValue | Number | 否 | 否 | 目标值，适用于目标追踪规则和预测规则。 | TargetValue最多保留小数点后三位，且必须大于0。 |
| StepAdjustmen t | List | 否 | 否 | 分步步骤。 | 详情请参见StepAdjustment属性。 |
| PredictiveValu eBehavior | String | 否 | 否 | 预测规则最大值处理方式。 | 取值： MaxOverridePredictiv eValue（默认值）：初始最大值会覆盖预测值。 预测值大于初始最大值时，预测任务的最大值采用初始最大值。 PredictiveValueOverri deMax：预测值会覆盖初始最大值。预测值大于初始最大值时， 预测任务的最大值采用预测值。 PredictiveValueOverri deMaxWithBuffer：预测值会附加一定比例。预测值会按照 PredictiveValueBuffer 比例增加，当增加后的值大于初始最大值时，会采用增加后的值。 |
| DisableScaleIn | Boolean | 否 | 否 | 是否禁用缩容， 仅适用于目标追踪规则。 | 取值： true false（默认值） |

资源编排

| InitialMaxSize | Integer | 否 | 否 | 伸缩组实例数上限，和 PredictiveValu eBehavior结合使用。 | 默认值为伸缩组最大实例数 （MaxSize的取值）。 |
|---|---|---|---|---|---|
| MinAdjustment Magnitude | Integer | 否 | 否 | 伸缩规则最小调整实例数。 | 仅当伸缩规则类型为 SimpleScalingRule或 StepScalingRule，且 AdjustmentType为 PercentChangeInCapacit y时该参数生效。 |
| EstimatedInsta nceWarmup | Integer | 否 | 否 | 实例预热时间， 适用于目标追踪规则和步进规则。 | 取值范围：0~86,400。 单位：秒。 默认值：300。 处于预热状态的ECS实例将正常的加入伸缩组，但是期间将不会向云监控上报监控数据。 说明动态计算需要扩缩容的ECS实例数量时，处于预热状态的实例不计入现有实例数量。 |
| PredictiveScali ngMode | String | 否 | 否 | 预测规则的模式。 | 取值： PredictAndScale（默认值）：产生预测结果并创建预测任务。 PredictOnly：产生预测结果，但不会创建预测任务。 |

**StepAdjustment语法**

```json
"StepAdjustment": [
  {
    "MetricIntervalUpperBound": Number,
    "ScalingAdjustment": Integer,
    "MetricIntervalLowerBound": Number
  }
```

]

**StepAdjustment属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| MetricIntervalU pperBound | Number | 否 | 否 | 分步步骤的上边界，仅适用于步进规则。 | 取值范围：- 9.999999E18~9.999999 E18。 |
| ScalingAdjustm ent | Integer | 否 | 否 | 分步步骤对应的实例扩展数量， 仅适用于步进规则。 | 无 |
| MetricIntervalL owerBound | Number | 否 | 否 | 分步步骤的下边界，仅适用于步进规则。 | 取值范围：- 9.999999E18~9.999999 E18。 |

**返回值**

Fn::GetAtt 资源编排 ScalingRuleAri：伸缩规则的唯一标识符。 ScalingRuleId：伸缩规则的ID。由系统生成，全局唯一。

**示例**

`JSON` 格式

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "TargetValue": {
      "Type": "Number",
      "Description": "The target value of a metric. This parameter is required and applicable only to
target tracking scaling rules and predictive scaling rules. The value of TargetValue must be greater than 0 and can have a maximum of three decimal places."
    },
    "Cooldown": {
      "Type": "Number",
      "Description": "Cool-down time of a scaling rule. Value range: [0, 86,400], in seconds. The def
ault value is empty.",
      "MinValue": 0,
      "MaxValue": 86400
    },
    "ScalingGroupId": {
      "Type": "String",
      "Description": "ID of the scaling group of a scaling rule."
    },
    "PredictiveValueBehavior": {
      "Type": "String",
      "Description": "The action taken on the predicted maximum value. Valid values:\n-
MaxOverridePredictiveValue: uses the initial maximum capacity as the maximum value for forecast tasks when the predicted value is greater than the initial maximum capacity.\n - PredictiveValueOverrideMax: uses the predicted value as the maximum value for forecast tasks when the predicted value is greater than the initial maximum capacity.\n - PredictiveValueOverrideMaxWithBuffer: increases the predicted value with a ratio, which is specified by PredictiveValueBuffer. If the value after the increase is greater than the initial maximum capacit y, the value after the increase is used as the maximum value for forecast tasks.\n Default value: Max OverridePredictiveValue",
      "AllowedValues": [
        "MaxOverridePredictiveValue",
        "PredictiveValueOverrideMax",
        "PredictiveValueOverrideMaxWithBuffer"
```

]

```json
    },
    "MinAdjustmentMagnitude": {
      "Type": "Number",
      "Description": "The minimum number of ECS instances to be adjusted in a scaling rule. This para
meter takes effect only when the scaling rule type is SimpleScalingRule or StepScalingRule and Adjust mentType is PercentChangeInCapacity.",
      "MinValue": 0,
      "MaxValue": 20
    },
    "DisableScaleIn": {
      "Type": "Boolean",
      "Description": "Specifies whether to disable scale-in. This parameter is applicable only to
target tracking scaling rules.\n Default value: false",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

]

```
    },
```

资源编排

```json
    "StepAdjustment": {
      "Type": "Json",
      "Description": ""
    },
    "AdjustmentType": {
      "Type": "String",
      "Description": "Adjustment mode of a scaling rule. Optional values:\n-
QuantityChangeInCapacity: It is used to increase or decrease a specified number of ECS instances.\n- PercentChangeInCapacity: It is used to increase or decrease a specified proportion of ECS instances.\n- TotalCapacity: It is used to adjust the quantity of ECS instances in the current scalin g group to a specified value.",
      "AllowedValues": [
        "QuantityChangeInCapacity",
        "PercentChangeInCapacity",
        "TotalCapacity"
```

]

```json
    },
    "MetricName": {
      "Type": "String",
      "Description": "The predefined metric to monitor. This parameter is required and applicable onl
y to target tracking scaling rules and predictive scaling rules.\nValid values of a target tracking s caling rule:\n- CpuUtilization: the average CPU utilization- ClassicInternetRx: the average public ne twork inbound traffic over the classic network\n- ClassicInternetTx: the average public network outbo und traffic over the classic network\n- VpcInternetRx: the average public network inbound traffic ove r the VPC\n- VpcInternetTx: the average public network outbound traffic over the VPC\n- IntranetRx: t he average internal network inbound traffic\n- IntranetTx: the average internal network outbound traf fic\nValid values of a predictive scaling rule:\n- CpuUtilization: the average CPU utilization\n- Int ranetRx: the average internal network inbound traffic\n- IntranetTx: the average internal network out bound traffic",
      "AllowedValues": [
        "CpuUtilization",
        "ClassicInternetRx",
        "ClassicInternetTx",
        "VpcInternetRx",
        "VpcInternetTx",
        "IntranetRx",
        "IntranetTx"
```

]

```json
    },
    "ScalingRuleName": {
      "Type": "String",
      "Description": "Name shown for the scaling group, which is a string containing 2 to 40 English
or Chinese characters. It must begin with a number, a letter (case-insensitive) or a Chinese characte r and can contain numbers, \"_\", \"-\" or \".\". The account name in the same scaling group is uniqu e in the same region. If this parameter value is not specified, the default value is ScalingRuleId.",
      "AllowedPattern": "^[a-zA-Z0-9\\u4e00-\\u9fa5][-_.a-zA-Z0-9\\u4e00-\\u9fa5]{1,63}$"
    },
    "AdjustmentValue": {
      "Type": "Number",
      "Description": "Adjusted value of a scaling rule. Value range:\n- QuantityChangeInCapacity: [-5
00, 500]\n- PercentChangeInCapacity: [-100, 10000]\n- TotalCapacity: [0, 1000]",
      "MinValue": -500,
      "MaxValue": 10000
    },
    "InitialMaxSize": {
      "Type": "Number",
      "Description": "The maximum number of ECS instances in the scaling group, which is used
together with PredictiveValueBehavior.\n Default value: the same as the value of MaxSize",
      "MinValue": 0,
      "MaxValue": 1000
    },
    "ScalingRuleType": {
"Type":"String"
```

资源编排

```json
      Type: String,
      "Description": "The type of the scaling rule. Valid values:\n- SimpleScalingRule: scales ECS in
stances based on the values of AdjustmentType and AdjustmentValue.\n- TargetTrackingScalingRule: dyna mically calculates the number of ECS instances to be adjusted and tries to keep the value of a predef ined monitoring metric close to TargetValue.\n- StepScalingRule: scales ECS instances in steps based on specified thresholds and metric values.\n- PredictiveScalingRule: uses machine learning to analyze historical monitoring data of the scaling group and then predicts the future values of monitored metr ics, the rule then automatically creates scheduled tasks to set the boundary values for the scaling g roup.\n If this parameter value is not specified, the default value is SimpleScalingRule.",
      "AllowedValues": [
        "SimpleScalingRule",
        "TargetTrackingScalingRule",
        "StepScalingRule",
        "PredictiveScalingRule"
```

]

```json
    },
    "EstimatedInstanceWarmup": {
      "Type": "Number",
      "Description": "The warm-up period of the ECS instances. This parameter is applicable to target
tracking scaling rules and step scaling rules. The system adds ECS instances that are in the warm-up state to the scaling group, but does not report monitoring data during the warm-up period to CloudMon itor.\nNote: When calculating the number of ECS instances to be adjusted, the system does not count E CS instances in the warm-up state as part of the current capacity of the scaling group.\nValid values : 0 to 86400. Unit: seconds. Default value: 300.",
      "MinValue": 0,
      "MaxValue": 86400
    },
    "PredictiveScalingMode": {
      "Type": "String",
      "Description": "The mode of the predictive scaling rule. Valid values:\n- PredictAndScale:
generates forecasts and creates forecast tasks.\n- PredictOnly: generates forecasts but does not crea te forecast tasks.\nDefault value: PredictAndScale",
      "AllowedValues": [
        "PredictAndScale",
        "PredictOnly"
```

]

```json
    },
    "PredictiveTaskBufferTime": {
      "Type": "Number",
      "Description": "The amount of buffer time ahead of the forecast task execution time. By
default, all scheduled tasks that are automatically created for a predictive scaling rule are execute d at the beginning of each hour. You can set a buffer time to execute forecast tasks ahead of schedul e, so that resources can be prepared in advance. Valid values: 0 to 60. Unit: minutes.\n Default valu e: 0",
      "MinValue": 0,
      "MaxValue": 60
    },
    "PredictiveValueBuffer": {
      "Type": "Number",
      "Description": "The ratio of the increment to the predicted value when PredictiveValueBehavior
is set to PredictiveValueOverrideMaxWithBuffer. When the value after the increase is greater than the initial maximum capacity, the value after the increase is used for forecast tasks. Valid values: 0 to 100\n Default value: 0",
      "MinValue": 0,
      "MaxValue": 100
    }
  },
  "Resources": {
    "ScalingRule": {
      "Type": "ALIYUN::ESS::ScalingRule",
      "Properties": {
        "TargetValue": {
          "Ref": "TargetValue"
```

资源编排

```json
        },
        "Cooldown": {
          "Ref": "Cooldown"
        },
        "ScalingGroupId": {
          "Ref": "ScalingGroupId"
        },
        "PredictiveValueBehavior": {
          "Ref": "PredictiveValueBehavior"
        },
        "MinAdjustmentMagnitude": {
          "Ref": "MinAdjustmentMagnitude"
        },
        "DisableScaleIn": {
          "Ref": "DisableScaleIn"
        },
        "StepAdjustment": {
          "Ref": "StepAdjustment"
        },
        "AdjustmentType": {
          "Ref": "AdjustmentType"
        },
        "MetricName": {
          "Ref": "MetricName"
        },
        "ScalingRuleName": {
          "Ref": "ScalingRuleName"
        },
        "AdjustmentValue": {
          "Ref": "AdjustmentValue"
        },
        "InitialMaxSize": {
          "Ref": "InitialMaxSize"
        },
        "ScalingRuleType": {
          "Ref": "ScalingRuleType"
        },
        "EstimatedInstanceWarmup": {
          "Ref": "EstimatedInstanceWarmup"
        },
        "PredictiveScalingMode": {
          "Ref": "PredictiveScalingMode"
        },
        "PredictiveTaskBufferTime": {
          "Ref": "PredictiveTaskBufferTime"
        },
        "PredictiveValueBuffer": {
          "Ref": "PredictiveValueBuffer"
        }
      }
    }
  },
  "Outputs": {
    "ScalingRuleAri": {
      "Description": "Unique identifier of a scaling rule.",
      "Value": {
        "Fn::GetAtt": [
          "ScalingRule",
          "ScalingRuleAri"
```

]

```
      }
    },
```

`"S` `li`

```
RlId" {
```

资源编排

```json
    "ScalingRuleId": {
      "Description": "ID of a scaling rule, generated by the system and globally unique.",
      "Value": {
        "Fn::GetAtt": [
          "ScalingRule",
          "ScalingRuleId"
```

]

```
      }
    }
  }
}
```

`YAML` 格式

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  TargetValue:
    Type: Number
    Description: >-
      The target value of a metric. This parameter is required and applicable
      only to target tracking scaling rules and predictive scaling rules. The
      value of TargetValue must be greater than 0 and can have a maximum of
      three decimal places.
  Cooldown:
    Type: Number
    Description: >-
      Cool-down time of a scaling rule. Value range: [0, 86,400], in seconds.
      The default value is empty.
    MinValue: 0
    MaxValue: 86400
  ScalingGroupId:
    Type: String
    Description: ID of the scaling group of a scaling rule.
  PredictiveValueBehavior:
    Type: String
    Description: >-
      The action taken on the predicted maximum value. Valid values:
      - MaxOverridePredictiveValue: uses the initial maximum capacity as the
      maximum value for forecast tasks when the predicted value is greater than
      the initial maximum capacity.
       - PredictiveValueOverrideMax: uses the predicted value as the maximum value for forecast tasks
when the predicted value is greater than the initial maximum capacity.
       - PredictiveValueOverrideMaxWithBuffer: increases the predicted value with a ratio, which is s
pecified by PredictiveValueBuffer. If the value after the increase is greater than the initial maximu m capacity, the value after the increase is used as the maximum value for forecast tasks.
       Default value: MaxOverridePredictiveValue
    AllowedValues:
      - MaxOverridePredictiveValue
      - PredictiveValueOverrideMax
      - PredictiveValueOverrideMaxWithBuffer
  MinAdjustmentMagnitude:
    Type: Number
    Description: >-
      The minimum number of ECS instances to be adjusted in a scaling rule. This
      parameter takes effect only when the scaling rule type is
      SimpleScalingRule or StepScalingRule and AdjustmentType is
      PercentChangeInCapacity.
    MinValue: 0
    MaxValue: 20
  DisableScaleIn:
    Type: Boolean
```

D

```
iti
```

资源编排

```
    Description: >-
      Specifies whether to disable scale-in. This parameter is applicable only
      to target tracking scaling rules.
       Default value: false
    AllowedValues:
      - 'True'
      - 'true'
      - 'False'
      - 'false'
  StepAdjustment:
    Type: Json
    Description: ''
  AdjustmentType:
    Type: String
    Description: >-
      Adjustment mode of a scaling rule. Optional values:
      - QuantityChangeInCapacity: It is used to increase or decrease a specified
      number of ECS instances.
      - PercentChangeInCapacity: It is used to increase or decrease a specified
      proportion of ECS instances.
      - TotalCapacity: It is used to adjust the quantity of ECS instances in the
      current scaling group to a specified value.
    AllowedValues:
      - QuantityChangeInCapacity
      - PercentChangeInCapacity
      - TotalCapacity
  MetricName:
    Type: String
    Description: >-
      The predefined metric to monitor. This parameter is required and
      applicable only to target tracking scaling rules and predictive scaling
      rules.
      Valid values of a target tracking scaling rule:
      - CpuUtilization: the average CPU utilization- ClassicInternetRx: the
      average public network inbound traffic over the classic network
      - ClassicInternetTx: the average public network outbound traffic over the
      classic network
      - VpcInternetRx: the average public network inbound traffic over the VPC
      - VpcInternetTx: the average public network outbound traffic over the VPC
      - IntranetRx: the average internal network inbound traffic
      - IntranetTx: the average internal network outbound traffic
      Valid values of a predictive scaling rule:
      - CpuUtilization: the average CPU utilization
      - IntranetRx: the average internal network inbound traffic
      - IntranetTx: the average internal network outbound traffic
    AllowedValues:
      - CpuUtilization
      - ClassicInternetRx
      - ClassicInternetTx
```

资源编排

```
      - VpcInternetRx
      - VpcInternetTx
      - IntranetRx
      - IntranetTx
  ScalingRuleName:
    Type: String
    Description: >-
      Name shown for the scaling group, which is a string containing 2 to 40
      English or Chinese characters. It must begin with a number, a letter
      (case-insensitive) or a Chinese character and can contain numbers, "_",
      "-" or ".". The account name in the same scaling group is unique in the
      same region. If this parameter value is not specified, the default value
      is ScalingRuleId.
    AllowedPattern: '^[a-zA-Z0-9\u4e00-\u9fa5][-_.a-zA-Z0-9\u4e00-\u9fa5]{1,63}$'
  AdjustmentValue:
    Type: Number
    Description: |-
      Adjusted value of a scaling rule. Value range:
      - QuantityChangeInCapacity: [-500, 500]
      - PercentChangeInCapacity: [-100, 10000]
      - TotalCapacity: [0, 1000]
    MinValue: -500
    MaxValue: 10000
  InitialMaxSize:
    Type: Number
    Description: >-
      The maximum number of ECS instances in the scaling group, which is used
      together with PredictiveValueBehavior.
       Default value: the same as the value of MaxSize
    MinValue: 0
    MaxValue: 1000
  ScalingRuleType:
    Type: String
    Description: >-
      The type of the scaling rule. Valid values:
      - SimpleScalingRule: scales ECS instances based on the values of
      AdjustmentType and AdjustmentValue.
      - TargetTrackingScalingRule: dynamically calculates the number of ECS
      instances to be adjusted and tries to keep the value of a predefined
      monitoring metric close to TargetValue.
      - StepScalingRule: scales ECS instances in steps based on specified
      thresholds and metric values.
      - PredictiveScalingRule: uses machine learning to analyze historical
      monitoring data of the scaling group and then predicts the future values
      of monitored metrics, the rule then automatically creates scheduled tasks
      to set the boundary values for the scaling group.
       If this parameter value is not specified, the default value is SimpleScalingRule.
    AllowedValues:
      - SimpleScalingRule
      - TargetTrackingScalingRule
      - StepScalingRule
      - PredictiveScalingRule
  EstimatedInstanceWarmup:
    Type: Number
    Description: >-
      The warm-up period of the ECS instances. This parameter is applicable to
      target tracking scaling rules and step scaling rules. The system adds ECS
      instances that are in the warm-up state to the scaling group, but does not
```

资源编排

```
      report monitoring data during the warm-up period to CloudMonitor.
      Note: When calculating the number of ECS instances to be adjusted, the
      system does not count ECS instances in the warm-up state as part of the
      current capacity of the scaling group.
      Valid values: 0 to 86400. Unit: seconds. Default value: 300.
    MinValue: 0
    MaxValue: 86400
  PredictiveScalingMode:
    Type: String
    Description: |-
      The mode of the predictive scaling rule. Valid values:
      - PredictAndScale: generates forecasts and creates forecast tasks.
      - PredictOnly: generates forecasts but does not create forecast tasks.
      Default value: PredictAndScale
    AllowedValues:
      - PredictAndScale
      - PredictOnly
  PredictiveTaskBufferTime:
    Type: Number
    Description: >-
      The amount of buffer time ahead of the forecast task execution time. By
      default, all scheduled tasks that are automatically created for a
      predictive scaling rule are executed at the beginning of each hour. You
      can set a buffer time to execute forecast tasks ahead of schedule, so that
      resources can be prepared in advance. Valid values: 0 to 60. Unit:
      minutes.
       Default value: 0
    MinValue: 0
    MaxValue: 60
  PredictiveValueBuffer:
    Type: Number
    Description: >-
      The ratio of the increment to the predicted value when
      PredictiveValueBehavior is set to PredictiveValueOverrideMaxWithBuffer.
      When the value after the increase is greater than the initial maximum
      capacity, the value after the increase is used for forecast tasks. Valid
      values: 0 to 100
       Default value: 0
    MinValue: 0
    MaxValue: 100
Resources:
  ScalingRule:
    Properties:
      TargetValue:
        Ref: TargetValue
      Cooldown:
        Ref: Cooldown
      ScalingGroupId:
        Ref: ScalingGroupId
      PredictiveValueBehavior:
        Ref: PredictiveValueBehavior
      MinAdjustmentMagnitude:
        Ref: MinAdjustmentMagnitude
      DisableScaleIn:
        Ref: DisableScaleIn
      StepAdjustment:
        Ref: StepAdjustment
      AdjustmentType:
        Ref: AdjustmentType
MetricName:
```

资源编排

```
      MetricName:
        Ref: MetricName
      ScalingRuleName:
        Ref: ScalingRuleName
      AdjustmentValue:
        Ref: AdjustmentValue
      InitialMaxSize:
        Ref: InitialMaxSize
      ScalingRuleType:
        Ref: ScalingRuleType
      EstimatedInstanceWarmup:
        Ref: EstimatedInstanceWarmup
      PredictiveScalingMode:
        Ref: PredictiveScalingMode
      PredictiveTaskBufferTime:
        Ref: PredictiveTaskBufferTime
      PredictiveValueBuffer:
        Ref: PredictiveValueBuffer
Outputs:
  ScalingRuleAri:
    Description: Unique identifier of a scaling rule.
    Value:
      'Fn::GetAtt':
        - ScalingRuleAri
  ScalingRuleId:
    Description: 'ID of a scaling rule, generated by the system and globally unique.'
    Value:
      'Fn::GetAtt':
        - ScalingRuleId
```

#### ALIYUN::ESS::ScheduledTask

**语法**

```json
{
  "Type": "ALIYUN::ESS::ScheduledTask",
  "Properties": {
    "TaskEnabled": Boolean,
    "Description": String,
    "ScheduledTaskName": String,
    "LaunchExpirationTime": Integer,
    "LaunchTime": String,
    "RecurrenceEndTime": String,
    "RecurrenceType": String,
    "RecurrenceValue": String,
    "ScheduledAction": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|

资源编排

| TaskEnabled | Boolean | 否 | 是 | 是否启动定时任务 |  |  | 取值： true（默认值）：启动任务 false：停止任务 |  |  |
|---|---|---|---|---|---|---|---|---|---|
| Description | String | 否 | 是 | 定时任务的描述信息 |  |  | 长度为2~200个字符 |  |  |
| ScheduledTaskN ame | String | 否 | 是 | 定时任务的显示名称 |  |  | 长度为2~40个字符，以数字、字母或中文字符开头， 可包含数字、字母、中文字符、下划线（ ）、短划 _ 线（-）或英文句点 （.）。 同一用户账号同一地域内唯一。 如果没有指定该参数，默认为 ScheduledScalin gTaskId。 |  |  |
| LaunchExpiratio nTime | Integer | 否 | 是 | 定时任务触发操作失败后，在此时间内重试 |  |  | 取值范围： 0~21600。 单位：秒。 默认值：600。 |  |  |
| LaunchTime | String | 是 | 是 | 定时任务触发的时间点 |  |  | 格式为： YYYY- MM- DDThh:mmZ 。 按照ISO8601标准表示，并需要使用 UTC时间。 如果指定了 RecurrenceTy pe，则此属性指定的时间点，默认为循环执行的时间点。 如果未指定 RecurrenceTy pe，则按指定的日期和时间执行一次。 不能填写自创建或修改当天起90日后的时间。 |  |  |
|  |  |  |  |  |  |  |  | YYYY- |  |
|  |  |  |  |  |  |  | MM- |  |  |
|  |  |  |  |  |  |  | DDThh:mmZ |  |  |

资源编排

| RecurrenceEndTi me | String | 否 | 是 | 重复执行定时任务的结束时间 |  |  | 格式为： YYYY- MM- DDThh:mmZ 。 按照ISO8601标准表示，并需要使用 UTC时间。 不能填写自创建或修改当天起90日后的时间。 RecurrenceType 、 RecurrenceValu e和 RecurrenceEndT ime需要同时指定。 |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  | YYYY- |  |
|  |  |  |  |  |  |  | MM- |  |  |
|  |  |  |  |  |  |  | DDThh:mmZ |  |  |
| RecurrenceType | String | 否 | 是 | 重复执行定时任务的类型 |  |  | 取值： Daily：每多少天重复执行一次定时任务。 Weekly：每周指定几天重复执行一次定时任务。 Monthly：每月内指定几天重复执行一次定时任务。 Cron：按照指定的Cron表达式执行定时任务。 RecurrenceType 、 RecurrenceValu e和 RecurrenceEndT ime需要同时指定。 |  |  |

资源编排

| RecurrenceValu e | String | 否 | 是 | 重复执行定时任务的数值 | 取值： Daily：只能填一个值。取值范围：1~31。 Weekly：可以填入多个值。周日、周一……周六的值依次为： 0, 1,2,…, 6， 多天使用半角逗号（,）分隔。 Monthly：格式为A-B。A、B的取值范围为 1~31，并且B 必须大于等于 A。 Cron：表示 UTC时间，支持分、时、日、 月、星期的5域表达式，支持半角逗号（,）、 半角问号 （?）、连字符 （-）、星号 （*）、井号 （#）、正斜线 （/）、L和W。 RecurrenceType 、 RecurrenceValu e和 RecurrenceEndT ime需要同时指定。 |
|---|---|---|---|---|---|
| ScheduledAction | String | 是 | 是 | 定时任务触发时需要执行的操作 | 最大支持200个字符。 此处填写伸缩规则的唯一标识符。 |

**返回值**

Fn::GetAtt ScheduledTaskId：定时任务的ID，由系统生成，全局唯一。

**示例**

资源编排

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "ScheduledTask": {
      "Type": "ALIYUN::ESS::ScheduledTask",
      "Properties": {
        "TaskEnabled": "true",
        "Description": "scheduledtask",
        "ScheduledTaskName": "task1",
        "LaunchTime": "2014-08-17T16:52Z",
        "RecurrenceEndTime": "2014-08-17T16:55Z",
        "RecurrenceType": "Daily",
        "RecurrenceValue": "1",
        "ScheduledAction": "ari:acs:ess:cn-qingdao:1344371:scalingRule/cCBpdYdQuBe2cUxOdu6piOk"
      }
    }
  },
  "Outputs": {
    "ScheduledTaskId": {
      "Value": {
        "FN::GetAtt": [
          "ScheduledTask",
          "ScheduledTaskId"
```

]

```
      }
    }
  }
}
```

### KMS

#### ALIYUN::KMS::Alias

**语法**

```json
{
  "Type": "ALIYUN::KMS::Alias",
  "Properties": {
    "KeyId": String,
    "AliasName": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| KeyId | String | 是 | 否 | Key的全局唯一标识符。 | 无。 |
| AliasName | String | 是 | 否 | CMK 的别名，可以使用别名调用 Encrypt、 GenerateDataKe y、 DescribeKey。 | 前缀以外的字符长度：最小长度为 1 字符，最大长度为 255 字符。 - 必须包含前缀alias/。 |

**返回值**

资源编排

**Fn::GetAtt**

无。

**示例**

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "Alias": {
      "Type": "ALIYUN::KMS::Alias",
      "Properties": {
        "KeyId": {
          "Ref": "KeyId"
        },
        "AliasName": {
          "Ref": "AliasName"
        }
      }
    }
  },
  "Parameters": {
    "KeyId": {
      "Type": "String",
      "Description": "Globally unique identifier of the CMK."
    },
    "AliasName": {
      "MinLength": 1,
      "Type": "String",
      "Description": "- The display name of the key. You can use the alias to call APIs such as Encry
pt, GenerateDataKey, and DescribeKey. - Not including the prefix, the minimum length of an alias is 1 and the maximum length is 255. - The prefix alias/ must be included.",
      "MaxLength": 255
    }
  },
  "Outputs": {}
}
```

#### ALIYUN::KMS::Key

**语法**

```json
{
  "Type": "ALIYUN::KMS::Key",
  "Properties": {
    "KeyUsage": String,
    "Enable": Boolean,
    "PendingWindowInDays": Integer,
    "Description": String,
    "KeySpec": String,
    "EnableAutomaticRotation": Boolean,
    "RotationInterval": String,
    "ProtectionLevel": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|

资源编排

| KeyUsage | String | 否 | 否 | 密钥的用途。 | 取值： ENCRYPT/DEC RYPT：数据加密和解密。 SIGN/VERIFY ：产生和验证数字签名。 |
|---|---|---|---|---|---|
| Enable | Boolean | 否 | 是 | 将密钥设置为启用或禁用状态。 | 取值： true（默认值）：启用。 false：禁用。 |
| PendingWindowI nDays | Integer | 否 | 否 | 密钥预删除周期。 在这段时间内，您可以撤销删除处于待删除状态的密钥；预删除时间过后无法撤销删除。 | 取值范围： 7~30。 默认值：30。 单位：天。 |
| Description | String | 否 | 是 | 密钥的描述。 | 长度为0~8192个字符。 |
| KeySpec | String | 否 | 否 | 密钥的类型。 | 取值： Aliyun AES 2 _ _ 56 Aliyun SM4 _ RSA 2048 _ EC P256 _ EC P256K _ EC SM2 _ 说明在中国内地使用托管密码机创建的密钥， 默认为 Aliyun SM4 _ 类型，其余情况下默认为 Aliyun AES _ _ 256。 |
| EnableAutomatic Rotation | Boolean | 否 | 是 | 是否开启自动密钥轮转。 | 取值： true false（默认值） |

资源编排

| RotationInterval | String | 否 | 是 | 自动轮转的时间周期。例如： 365d 。 |  | 格式为 integer[uni t] ，其中 integer 表示时间长度， unit 表示时间单位。 合法的 unit 单位取值如下： d：天 h：小时 m：分钟 s：秒 7d或者604800s 均表示7天的周期。 取值范围：7~730 天。 |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  | integer[uni |  |
|  |  |  |  |  |  | t] |  |  |
| ProtectionLevel | String | 否 | 否 | 密钥的保护级别。 |  | 取值： SOFTWARE（ 默认值） HSM |  |  |

**返回值**

Fn::GetAtt KeyId：密钥的全局唯一标识符。

**示例**

`JSON` 格式

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "ProtectionLevel": {
      "Type": "String",
      "Description": "The protection level of the CMK to create. Valid value: SOFTWARE and HSM. When
this parameter is set to HSM:\nIf the Origin parameter is set to Aliyun_KMS, the CMK is created in Ma naged HSM.\nIf the Origin parameter is set to EXTERNAL, you can import external keys to Managed HSM."
    },
    "Description": {
      "Type": "String",
      "Description": "The description of the CMK. Length constraints: Minimum length of 0 characters.
Maximum length of 8192 characters.",
      "MinLength": 0,
      "MaxLength": 8192
    },
    "RotationInterval": {
      "Type": "String",
      "Description": "The time period for automatic rotation. The format is integer[unit], where inte
ger represents the length of time and unit represents the time unit. The legal unit units are: d (day ), h (hour), m (minute), s (second). 7d or 604800s both represent a 7-day cycle. Value: 7~730 days."
    },
    "EnableAutomaticRotation": {
      "Type": "Boolean",
      "Description": "Whether to enable automatic key rotation. Valid value: true/false (default)",
      "AllowedValues": [
        true,
        false
```

] 资源编排 ]

```json
    },
    "PendingWindowInDays": {
      "Type": "Number",
      "Description": "The waiting period, specified in number of days. During this period, you can ca
ncel the CMK in PendingDeletion status. After the waiting period expires, you cannot cancel the delet ion. The value must be between 7 and 30. Default value is 30.",
      "MinValue": 7,
      "MaxValue": 30,
      "Default": 30
    },
    "KeySpec": {
      "Type": "String",
      "Description": "Key type. Valid value:
Aliyun_AES_256/Aliyun_SM4/RSA_2048/EC_P256/EC_P256K/EC_SM2"
    },
    "Enable": {
      "Type": "Boolean",
      "Description": "Specifies whether the key is enabled. Defaults to true.",
      "AllowedValues": [
        true,
        false
```

`],`

```json
      "Default": true
    },
    "KeyUsage": {
      "Type": "String",
      "Description": "The intended use of the CMK. Default value: ENCRYPT/DECRYPT.",
      "Default": "ENCRYPT/DECRYPT"
    }
  },
  "Resources": {
    "Key": {
      "Type": "ALIYUN::KMS::Key",
      "Properties": {
        "ProtectionLevel": {
          "Ref": "ProtectionLevel"
        },
        "Description": {
          "Ref": "Description"
        },
        "RotationInterval": {
          "Ref": "RotationInterval"
        },
        "EnableAutomaticRotation": {
          "Ref": "EnableAutomaticRotation"
        },
        "PendingWindowInDays": {
          "Ref": "PendingWindowInDays"
        },
        "KeySpec": {
          "Ref": "KeySpec"
        },
        "Enable": {
          "Ref": "Enable"
        },
        "KeyUsage": {
          "Ref": "KeyUsage"
        }
      }
    }
  },
  "Outputs": {
```

资源编排

```json
    "KeyId": {
      "Description": "The globally unique identifier for the CMK.",
      "Value": {
        "Fn::GetAtt": [
          "Key",
          "KeyId"
```

]

```
      }
    }
  }
}
```

`YAML` 格式

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  ProtectionLevel:
    Type: String
    Description: >-
      The protection level of the CMK to create. Valid value: SOFTWARE and HSM.
      When this parameter is set to HSM:
      If the Origin parameter is set to Aliyun_KMS, the CMK is created in
      Managed HSM.
      If the Origin parameter is set to EXTERNAL, you can import external keys
      to Managed HSM.
  Description:
    Type: String
    Description: >-
      The description of the CMK. Length constraints: Minimum length of 0
      characters. Maximum length of 8192 characters.
    MinLength: 0
    MaxLength: 8192
  RotationInterval:
    Type: String
    Description: >-
      The time period for automatic rotation. The format is integer[unit], where
      integer represents the length of time and unit represents the time unit.
      The legal unit units are: d (day), h (hour), m (minute), s (second). 7d or
      604800s both represent a 7-day cycle. Value: 7~730 days.
  EnableAutomaticRotation:
    Type: Boolean
    Description: >-
      Whether to enable automatic key rotation. Valid value: true/false
      (default)
    AllowedValues:
      - true
      - false
  PendingWindowInDays:
    Type: Number
    Description: >-
      The waiting period, specified in number of days. During this period, you
      can cancel the CMK in PendingDeletion status. After the waiting period
      expires, you cannot cancel the deletion. The value must be between 7 and
      30. Default value is 30.
    MinValue: 7
    MaxValue: 30
    Default: 30
  KeySpec:
    Type: String
    Description: >-
```

资源编排

```
      Key type. Valid value:
      Aliyun_AES_256/Aliyun_SM4/RSA_2048/EC_P256/EC_P256K/EC_SM2
  Enable:
    Type: Boolean
    Description: Specifies whether the key is enabled. Defaults to true.
    AllowedValues:
      - true
      - false
    Default: true
  KeyUsage:
    Type: String
    Description: 'The intended use of the CMK. Default value: ENCRYPT/DECRYPT.'
    Default: ENCRYPT/DECRYPT
Resources:
  Key:
    Properties:
      ProtectionLevel:
        Ref: ProtectionLevel
      Description:
        Ref: Description
      RotationInterval:
        Ref: RotationInterval
      EnableAutomaticRotation:
        Ref: EnableAutomaticRotation
      PendingWindowInDays:
        Ref: PendingWindowInDays
      KeySpec:
        Ref: KeySpec
      Enable:
        Ref: Enable
      KeyUsage:
        Ref: KeyUsage
Outputs:
  KeyId:
    Description: The globally unique identifier for the CMK.
    Value:
      'Fn::GetAtt':
        - Key
        - KeyId
```

### NAS

#### ALIYUN::NAS::AccessGroup

**语法**

```json
{
  "Type": "ALIYUN::NAS::AccessGroup",
  "Properties": {
    "AccessGroupType": String,
    "AccessGroupName": String,
    "Description": String
  }
}
```

**属性**

资源编排

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| AccessGroupTyp e | String | 是 | 否 | 权限组类型。 | 可用值：Vpc、 Classic。 |
| AccessGroupNa me | String | 是 | 否 | 权限组名称。 | 以大、小写、数字、中横线开头， 最少3个字符，最多64个字符。 |
| Description | String | 否 | 是 | 权限组描述，默认和名称相同。 | 无。 |

**返回值**

**Fn::GetAtt**

AccessGroupName：权限组名称。

**示例**

资源编排

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "AccessGroup": {
      "Type": "ALIYUN::NAS::AccessGroup",
      "Properties": {
        "AccessGroupType": {
          "Ref": "AccessGroupType"
        },
        "AccessGroupName": {
          "Ref": "AccessGroupName"
        },
        "Description": {
          "Ref": "Description"
        }
      }
    }
  },
  "Parameters": {
    "AccessGroupType": {
      "Type": "String",
      "Description": "Permission group type, including the Vpc and Classic types",
      "AllowedValues": ["Vpc", "Classic"]
    },
    "AccessGroupName": {
      "AllowedPattern": "^[a-zA-Z0-9-]{3,64}$",
      "Type": "String",
      "Description": "Permission group name"
    },
    "Description": {
      "Type": "String",
      "Description": "Permission group description. It is the same as the permission group name by de
fault."
    }
  },
  "Outputs": {
    "AccessGroupName": {
      "Description": "Permission group name",
      "Value": {
        "Fn::GetAtt": ["AccessGroup", "AccessGroupName"]
      }
    }
  }
}
```

#### ALIYUN::NAS::AccessRule

**语法**

资源编排

```json
{
  "Type": "ALIYUN::NAS::AccessRule",
  "Properties": {
    "Priority": Integer,
    "UserAccessType": String,
    "AccessGroupName": String,
    "SourceCidrIp": String,
    "RWAccessType": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Priority | Integer | 否 | 是 | 优先级。 | 范围 1-100，默认值为1。 |
| UserAccessType | String | 否 | 是 | 用户权限类型。 | 可用值： no squash（默 _ 认）、 root squash和 _ all squash。 _ |
| AccessGroupNa me | String | 是 | 否 | 权限组名称。 | 无。 |
| SourceCidrIp | String | 是 | 是 | 地址或地址段。 | 无。 |
| RWAccessType | String | 否 | 是 | 读写权限类型。 | 可用值： RDWR（默认）、 RDONLY。 |

**返回值**

**Fn::GetAtt**

AccessRuleId：规则序号。

**示例**

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "AccessRule": {
      "Type": "ALIYUN::NAS::AccessRule",
      "Properties": {
        "Priority": {
          "Ref": "Priority"
        },
        "RWAccessType": {
          "Ref": "RWAccessType"
        },
        "UserAccessType": {
          "Ref": "UserAccessType"
        },
        "SourceCidrIp": {
          "Ref": "SourceCidrIp"
        },
        "AccessGroupName": {
          "Ref": "AccessGroupName"
        }
      }
    }
  },
```

资源编排

```json
  "Parameters": {
    "Priority": {
      "Default": 1,
      "Type": "Number",
      "Description": "Priority level. Range: 1-100. Default value: 1",
      "MaxValue": 100,
      "MinValue": 1
    },
    "RWAccessType": {
      "Default": "RDWR",
      "Type": "String",
      "Description": "Read-write permission type: RDWR (default), RDONLY",
      "AllowedValues": ["RDWR", "RDONLY"]
    },
    "UserAccessType": {
      "Default": "no_squash",
      "Type": "String",
      "Description": "User permission type: no_squash (default), root_squash, all_squash",
      "AllowedValues": ["no_squash", "root_squash", "all_squash"]
    },
    "SourceCidrIp": {
      "Type": "String",
      "Description": "Address or address segment"
    },
    "AccessGroupName": {
      "Type": "String",
      "Description": "Permission group name"
    }
  },
  "Outputs": {
    "AccessRuleId": {
      "Description": "Rule serial number",
      "Value": {
        "Fn::GetAtt": ["AccessRule", "AccessRuleId"]
      }
    }
  }
}
```

#### ALIYUN::NAS::FileSystem

**语法**

资源编排

```json
{
  "Type": "ALIYUN::NAS::FileSystem",
  "Properties": {
    "SnapshotId": String,
    "Description": String,
    "StorageType": String,
    "DeletionForce": Boolean,
    "EncryptType": Integer,
    "VpcId": String,
    "ZoneId": String,
    "Capacity": Integer,
    "Tags": List,
    "ProtocolType": String,
    "FileSystemType": String,
    "Bandwidth": Integer,
    "VSwitchId": String,
    "Duration": Integer,
    "ChargeType": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ProtocolTyp e | String | 是 | 否 | 协议类型。 | 取值： NFS：NFS协议。 SMB：SMB协议。 |
| StorageType | String | 是 | 否 | 存储类型。 | 取值： 当FileSystemType取值为 standard时： Performance：性能型。 Capacity：容量型。 当FileSystemType取值为 extreme或cpfs时： standard：标准型。 advance：高级型。 |
| DeletionForc e | Boolean | 否 | 是 | 是否强制删除。 | 取值： true：强制删除。 false（默认值）：不强制删除。 |
| Description | String | 否 | 是 | 文件系统描述。 | 长度为2~128个字符。必须以英文字母或汉字开头，不能以 http:// 和 https:// 开头。可包含英文字母、汉字、 数字、半角冒号（:）、下划线 （ ）和短划线（-）。 _ |
| ZoneId | String | 否 | 否 | 可用区ID。 | 无 |
| Tags | List | 否 | 是 | 标签。 | 每个实例最多绑定20个标签。 更多信息，请参见Tags属性。 |

资源编排

| SnapshotId | String | 否 | 否 | 快照ID。 | 可以通过指定SnapshotId从指定快照创建NAS实例，目前仅支持极速型NAS。 说明通过快照创建的文件系统版本需和快照源文件系统版本一致。如果不一致，可以执行以下步骤： 1. 把快照源文件数据拷贝到创建的文件系统中。 2. 拷贝完成后，把业务迁移到新的文件系统。 |
|---|---|---|---|---|---|
| EncryptType | Integer | 否 | 否 | 文件系统是否加密。使用KMS托管密钥，对文件系统落盘数据进行加密存储。在读写加密数据时，无需解密。 | 当FileSystemType取值为 standard或extreme时该参数有效。取值： 0：不加密。 1：加密。 |
| Capacity | Integer | 否 | 否 | 文件系统容量。 | 当FileSystemType取值为 extreme或cpfs时该参数有效且必须指定。取值范围： 当FileSystemType取值为 extreme时： 100~262,144。 当FileSystemType取值为 cpfs时：2048~512,000。 单位：GB。 |
| FileSystemT ype | String | 否 | 否 | 文件系统类型。 | 取值： standard（默认值）：通用型。 extreme：极速型。 cpfs：并行文件系统。 |
| VpcId | String | 否 | 否 | 专有网络ID，指定 VpcId和VSwitchId可以在创建文件系统实例的同时预配置一个默认挂载点。 | 当FileSystemType取值为cpfs 时，该参数必须指定。 |
| Bandwidth | Integer | 否 | 否 | 文件系统吞吐上限。 | 当FileSystemType取值为cpfs 时该参数必须指定，取值根据 Capacity确定。更多信息，请参见CPFS购买页面。 单位：Mbps。 |
| VSwitchId | String | 否 | 否 | 交换机ID，指定VpcId 和VSwitchId可以在创建文件系统实例的同时预配置一个默认挂载点。 | 当FileSystemType取值为cpfs 时该参数必须指定。 |

资源编排

| Duration | Integer | 否 | 否 | 包年包月时长。 | 当ChargeType取值为 Subscription时该参数有效且必须指定。当包年包月实例到期时未进行续费，实例会自动到期释放。取值： 1 2 3 6 12 36 单位：月。 |
|---|---|---|---|---|---|
| ChargeType | String | 否 | 否 | 付费类型。 | 取值： PayAsYouGo：按量付费。 Subscription：包年包月。 |

**Tags语法**

```json
"Tags": [
  {
    "Key": String,
    "Value": String
  }
```

]

**Tags属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Key | String | 是 | 否 | 标签键。 | 长度为1~128个字符，不能以 aliyun 和 acs: 开头， 不能包含 http:// 或 https:// 。 |
| Value | String | 否 | 否 | 标签值。 | 长度为0~128个字符，不能以 aliyun 和 acs: 开头， 不能包含 http:// 或 https:// 。 |

**返回值**

Fn::GetAtt FileSystemId：文件系统ID。

**示例**

`JSON` 格式资源编排

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Description": "Test NAS AccessGroupName、AccessRule、FileSystem、MountTarget",
  "Parameters": {
    "Description": {
      "Type": "String",
      "Description": "File system description.",
      "Default": "mytest"
    },
    "ProtocolType": {
      "Type": "String",
      "Description": "Type of protocol used.",
      "AllowedValues": [
        "NFS",
        "SMB"
```

`],`

```json
      "Default": "NFS"
    },
    "StorageType": {
      "Type": "String",
      "Description": "The file system type.",
      "AllowedValues": [
        "Performance",
        "Capacity"
```

`],`

```json
      "Default": "Capacity"
    }
  },
  "Resources": {
    "FileSystem": {
      "Type": "ALIYUN::NAS::FileSystem",
      "Properties": {
        "ProtocolType": {
          "Ref": "ProtocolType"
        },
        "StorageType": {
          "Ref": "StorageType"
        },
        "Description": {
          "Ref": "Description"
        }
      }
    }
  },
  "Outputs": {
    "FileSystemId": {
      "Description": "ID of the file system created",
      "Value": {
        "Fn::GetAtt": [
          "FileSystem",
          "FileSystemId"
```

]

```
      }
    }
  }
}
```

更多示例，请参见创建文件系统、创建权限组、创建权限规则和创建挂载点的组合示例：JSON示例和YAML示例。

#### ALIYUN::NAS::MountTarget

资源编排

**语法**

```json
{
  "Type": "ALIYUN::NAS::MountTarget",
  "Properties": {
    "Status": String,
    "VpcId": String,
    "FileSystemId": String,
    "VSwitchId": String,
    "NetworkType": String,
    "AccessGroupName": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Status | String | 否 | 是 | 状态。 | 可用值：Active 、 Inactive。 |
| VpcId | String | 否 | 否 | VPC 网络 ID。 | 无。 |
| FileSystemId | String | 是 | 否 | 文件系统 ID。 | 无。 |
| VSwitchId | String | 否 | 否 | 交换机 ID。 | 无。 |
| NetworkType | String | 是 | 否 | 网络类型。 | 可用值：Vpc、 Classic。 |
| AccessGroupNa me | String | 是 | 是 | 权限组名称。 | 无。 |

**返回值**

**Fn::GetAtt**

MountTargetDomain：挂载点域名。

**示例**

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "MountTarget": {
      "Type": "ALIYUN::NAS::MountTarget",
      "Properties": {
        "Status": {
          "Ref": "Status"
        },
        "VpcId": {
          "Ref": "VpcId"
        },
        "FileSystemId": {
          "Ref": "FileSystemId"
        },
        "VSwitchId": {
          "Ref": "VSwitchId"
        },
        "NetworkType": {
          "Ref": "NetworkType"
        },
        "AccessGroupName": {
```

资源编排

```json
          "Ref": "AccessGroupName"
        }
      }
    }
  },
  "Parameters": {
    "Status": {
      "Type": "String",
      "Description": "Status, including Active and Inactive",
      "AllowedValues": ["Active", "Inactive"]
    },
    "VpcId": {
      "Type": "String",
      "Description": "VPC network ID"
    },
    "FileSystemId": {
      "Type": "String",
      "Description": "File system ID"
    },
    "VSwitchId": {
      "Type": "String",
      "Description": "VSwitch ID."
    },
    "NetworkType": {
      "Type": "String",
      "Description": "Network type, including Vpc and Classic networks.",
      "AllowedValues": ["Vpc", "Classic"]
    },
    "AccessGroupName": {
      "Type": "String",
      "Description": "Permission group name"
    }
  },
  "Outputs": {
    "MountTargetDomain": {
      "Description": "Mount point domain name",
      "Value": {
        "Fn::GetAtt": ["MountTarget", "MountTargetDomain"]
      }
    }
  }
}
```

### OSS

#### ALIYUN::OSS::Bucket

**语法**

资源编排

```json
{
  "Type": "ALIYUN::OSS::Bucket",
  "Properties": {
    "AccessControl": String,
    "RefererConfiguration": Map,
    "ServerSideEncryptionConfiguration": Map,
    "CORSConfiguration": Map,
    "Tags": Map,
    "LoggingConfiguration": Map,
    "LifecycleConfiguration": Map,
    "StorageClass": String,
    "DeletionForce": Boolean,
    "WebsiteConfiguration": Map,
    "Policy": Map,
    "BucketName": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| BucketName | String | 是 | 否 | 存储空间名称。 | 长度为3~63个字符。必须以小写英文字母或数字开头和结尾，可包含小写英文字母、数字和短划线 （-）。 |
| AccessContro l | String | 否 | 是 | 访问权限。 | 取值： private（默认值）：私有。 public-read：公共读。 public-read-write：公共读写。 |
| CORSConfigu ration | Map | 否 | 否 | 跨域访问配置。 | 更多信息，请参见CORSConfiguration属性。 |
| LifecycleConfi guration | Map | 否 | 是 | 文件生命周期配置。 | 更多信息，请参见LifecycleConfiguration属性。 |
| LoggingConfi guration | Map | 否 | 否 | 日志存储配置。 | 更多信息，请参见LoggingConfiguration属性。 |
| RefererConfig uration | Map | 否 | 是 | 防盗链配置。 | 更多信息，请参见RefererConfiguration属性。 |
| DeletionForce | Boolean | 否 | 是 | 是否强制删除 OSS中的文件。 | 取值： true：强制删除。 false（默认值）：不强制删除。 |
| WebsiteConfi guration | Map | 否 | 否 | 静态托管页配置。 | 更多信息，请参见WebsiteConfiguration属性。 |
| ServerSideEn cryptionConfi guration | Map | 否 | 是 | 服务端加密规则配置。 | 更多信息，请参见ServerSideEncryptionConfigu ration属性。 |
| Tags | Map | 否 | 是 | 存储空间标签。 Key-Value形式的键值对。 | 最多设置20个标签。 Key长度为1~64个字节，不能以 http:// 、 https:// 或 Aliyun 开头。 Value长度为0~128个字节，必须为UTF-8编码。 |

|  | http:// |
|---|---|
| Aliyun |  |

资源编排

| StorageClass | String | 否 | 否 | 存储空间类型。 | 取值： Standard（默认值）：标准存储。 IA：低频访问。 Archive：归档存储。 |
|---|---|---|---|---|---|
| Policy | Map | 否 | 是 | 存储空间策略。 | 无 |

**CORSConfiguration语法**

```json
"CORSConfiguration": {
  "CORSRule": List
}
```

**CORSConfiguration属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| CORSRule | List | 否 | 否 | 跨域访问规则。 | 更多信息，请参见CORSRule属性。 |

**CORSRule语法**

```json
"CORSRule": [
  {
    "MaxAgeSeconds": Number,
    "AllowedMethod": List,
    "ExposeHeader": List,
    "AllowedOrigin": List,
    "AllowedHeader": List
  }
```

]

**CORSRule属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| AllowedHead er | List | 否 | 否 | 允许的跨域请求 Header。 | 取值： * Cache-Control Content-Language Content-Type Expires Last-Modified Pragma |
| AllowedMetho d | List | 否 | 否 | 允许的跨域请求的方法。 | 取值： * GET PUT POST DELETE HEAD |
| AllowedOrigin | List | 否 | 否 | 允许的跨域请求的来源。 | 无 |

资源编排

| ExposeHeade r | List | 否 | 否 | 允许用户从应用程序中访问的响应头。 | 不允许使用星号（*）。 |
|---|---|---|---|---|---|
| MaxAgeSeco nds | Number | 否 | 否 | 浏览器对特定资源的OPTIONS 请求返回结果的缓存时间。 | 无 |

**LifecycleConfiguration语法**

```json
"LifecycleConfiguration": {
  "Rule": List
}
```

**LifecycleConfiguration属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Rule | List | 是 | 否 | 生命周期规则。 | 更多信息，请参见Rule属性。 |

**Rule语法**

```json
"Rule": [
  {
    "Status": String,
    "AbortMultipartUpload": Map,
    "Expiration": Map,
    "Prefix": String,
    "ID": String
  }
```

]

**Rule属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ID | String | 否 | 否 | 规则的唯一 ID。 | 最长为255字节。当没有指定ID或者ID为空时，OSS会自动生成一个唯一值。 |
| Prefix | String | 是 | 否 | 规则所适用的前缀。 | 只有匹配前缀的对象才可能被该规则所影响。 |
| Status | String | 否 | 是 | 启用或停用规则。 | 取值： Enabled：启用规则。 Disabled：停用规则。 |
| Expiration | Map | 否 | 否 | 对象规则的过期属性。 | 更多信息，请参见Expiration属性。 |
| AbortMultipar tUpload | Map | 否 | 否 | 未完成分片上传的过期属性。 | 更多信息，请参见AbortMultipartUpload属性。 |

**Expiration语法**

```json
"Expiration":{
  "Days": Number,
  "CreatedBeforeDate": String,
  "Date": String
}
```

资源编排

**Expiration属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Days | Number | 否 | 否 | 对象最后修改后，规则将在多少天后生效。 | 以文件最后修改时间为起点开始计算，超过设定天数时即执行规则， 则将对象删除。如果设置时间为30 天，则最后修改日期为2016年01月 01日的对象会在2016年01月31日被后端程序删除。 |
| CreatedBefor eDate | String | 否 | 否 | 指定一个日期，OSS会对最后更新日期早于该日期的数据执行规则。 | 日期必须服从ISO8601的格式，且要求是UTC的零点。例如：2002- 10-11T00:00:00.000Z。 |

**AbortMultipartUpload语法**

```json
"AbortMultipartUpload": {
  "CreatedBeforeDate": String,
  "Days": Number
}
```

**AbortMultipartUpload属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Days | Number | 否 | 否 | 对象最后修改后，规则会在多少天后生效。 | 以文件最后修改时间为起点开始计算，超过设定天数时即执行规则， 则将对象删除。如果设置时间为30 天，则最后修改日期为2016年01月 01日的对象会在2016年01月31日被后端程序删除。 |
| CreatedBefor eDate | String | 否 | 否 | 规则在何时之前生效。 | 日期为ISO8601的格式，并且值为 UTC的零点。例如：2002-10- 11T00:00:00.000Z。 |

**LoggingConfiguration语法**

```json
"LoggingConfiguration": {
  "TargetBucket": String,
  "TargetPrefix": String
}
```

**LoggingConfiguration属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| TargetBucket | String | 否 | 否 | 存放访问日志的存储空间。 | 无 |
| TargetPrefix | String | 否 | 否 | 最终被保存的访问日志文件前缀。 | 无 |

**WebsiteConfiguration语法**

```json
"WebsiteConfiguration":{
  "IndexDocument": String,
  "ErrorDocument": String
}
```

**WebsiteConfiguration属性**

资源编排

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| IndexDocume nt | String | 否 | 否 | 托管的静态首页。 | 无 |
| ErrorDocume nt | String | 否 | 否 | 托管的静态错误页。 | 无 |

**RefererConfiguration语法**

```json
"RefererConfiguration":{
  "AllowEmptyReferer": String,
  "RefererList": List
}
```

**RefererConfiguration属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| AllowEmptyR eferer | Boolean | 否 | 否 | 是否允许 referer字段为空的请求访问。 | 取值： true（默认值）：允许r。 false：不允许。 |
| RefererList | List | 否 | 否 | 允许referer字段的白名单。 | 无 |

**ServerSideEncryptionConfiguration语法**

```json
"ServerSideEncryptionConfiguration":{
  "KMSMasterKeyID": String,
  "SSEAlgorithm": String
}
```

**ServerSideEncryptionConfiguration属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| KMSMasterKe yID | String | 否 | 否 | 密钥ID。 | 只有当SSEAlgorithm值为KMS， 且使用指定的密钥加密时，才需指定密钥ID。 |
| SSEAlgorithm | String | 是 | 否 | 服务端默认加密方式。 | 取值： KMS AES256 |

**返回值**

Fn::GetAtt Name：存储空间名称，全局唯一。 DomainName：通过公网访问存储空间的域名。 InternalDomainName：通过内网访问存储空间的域名。

**示例**

`JSON` 格式

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Description": "Test OSS Bucket",
  "Parameters": {
    "AccessControl": {
"Default":"private"
```

资源编排

```json
      Default: private,
      "Type": "String",
      "Description": "The access control list.",
      "AllowedValues": [
        "private",
        "public-read",
        "public-read-write"
```

]

```json
    },
    "BucketName": {
      "Type": "String",
      "Description": "bucket name."
    }
  },
  "Resources": {
    "Bucket": {
      "Type": "ALIYUN::OSS::Bucket",
      "Properties": {
        "AccessControl": {
          "Ref": "AccessControl"
        },
        "BucketName": {
          "Ref": "BucketName"
        }
      }
    }
  },
  "Outputs": {
    "InternalDomainName": {
      "Description": "The internal DNS name of the specified bucket.",
      "Value": {
        "Fn::GetAtt": [
          "Bucket",
          "InternalDomainName"
```

]

```json
      }
    },
    "Name": {
      "Description": "The name of Bucket",
      "Value": {
        "Fn::GetAtt": [
          "Bucket",
          "Name"
```

]

```json
      }
    },
    "DomainName": {
      "Description": "The public DNS name of the specified bucket.",
      "Value": {
        "Fn::GetAtt": [
          "Bucket",
          "DomainName"
```

]

```
      }
    }
  }
}
```

更多示例，请参见：JSON示例和YAML示例。

### RDS

资源编排

#### ALIYUN::RDS::Account

**语法**

```json
{
  "Type": "ALIYUN::RDS::Account",
  "Properties": {
    "AccountDescription": String,
    "DBInstanceId": String,
    "AccountPassword": String,
    "AccountType": String,
    "AccountName": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| AccountDescripti on | String | 否 | 是 | 账号描述。 | 长度为2~256个字符。以英文字母和汉字开头，可包含英文字母、汉字、 数字、下划线 （ ）和短划线 _ （-）。 |
| DBInstanceId | String | 是 | 否 | 实例ID。 | 无 |
| AccountPasswor d | String | 是 | 否 | 账号密码。 | 长度为8~32个字符。由大写英文字母、小写英文字母、数字、特殊字符中的任意三种组成。支持的特殊字符如下： !@#$&amp;%^ *() +-= _ |
| AccountType | String | 否 | 否 | 账号类型。 | 取值： Normal（默认值）：普通账号。 Super：高权限账号。 说明 SQL Server数据库高权限账号不支持删除。 |
| AccountName | String | 是 | 否 | 账号名称。 | 无 |

**返回值**

Fn::GetAtt AccountName：账号名称。 资源编排

**示例**

`JSON` 格式

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "AccountDescription": {
      "Type": "String",
      "Description": "Account remarks.\nIt cannot begin with http:// or https://.\nIt must start with
a Chinese character or English letter.\nIt can include Chinese and English characters/letters, unders cores (_), hyphens (-), and digits.\nThe length may be 2-256 characters."
    },
    "DBInstanceId": {
      "Type": "String",
      "Description": "RDS instance ID."
    },
    "AccountType": {
      "Type": "String",
      "Description": "Privilege type of account.\nNormal: Common privilege.\nSuper: High privilege. A
nd the default value is Normal.\nThis parameter is valid for MySQL 5.5/5.6 only.\nMySQL 5.7, SQL Serv er 2012/2016, PostgreSQL, and PPAS each can have only one initial account. Other accounts are created by the initial account that has logged on to the database.",
      "AllowedValues": [
        "Normal",
        "Super"
```

`],`

```json
      "Default": "Normal"
    },
    "AccountPassword": {
      "Type": "String",
      "Description": "The account password for the database instance. It may consist of letters, digi
ts, or underlines, with a length of 8 to 32 characters.",
      "MinLength": 8,
      "MaxLength": 32
    },
    "AccountName": {
      "Type": "String",
      "Description": "Account name, which must be unique and meet the following requirements:\nStart
with a letter;\nConsist of lower-case letters, digits, and underscores (_);\nContain no more than 16 characters.\nFor other invalid characters, see Forbidden keywords table."
    }
  },
  "Resources": {
    "Account": {
      "Type": "ALIYUN::RDS::Account",
      "Properties": {
        "AccountDescription": {
          "Ref": "AccountDescription"
        },
        "DBInstanceId": {
          "Ref": "DBInstanceId"
        },
        "AccountType": {
          "Ref": "AccountType"
        },
        "AccountPassword": {
          "Ref": "AccountPassword"
        },
        "AccountName": {
          "Ref": "AccountName"
        }
      }
```

资源编排

```json
    }
  },
  "Outputs": {
    "AccountName": {
      "Description": "Account name",
      "Value": {
        "Fn::GetAtt": [
          "Account",
          "AccountName"
```

]

```
      }
    }
  }
}
```

`YAML` 格式

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  AccountDescription:
    Type: String
    Description: >-
      Account remarks.
      It cannot begin with http:// or https://.
      It must start with a Chinese character or English letter.
      It can include Chinese and English characters/letters, underscores (_),
      hyphens (-), and digits.
      The length may be 2-256 characters.
  DBInstanceId:
    Type: String
    Description: RDS instance ID.
  AccountType:
    Type: String
    Description: >-
      Privilege type of account.
      Normal: Common privilege.
      Super: High privilege. And the default value is Normal.
      This parameter is valid for MySQL 5.5/5.6 only.
      MySQL 5.7, SQL Server 2012/2016, PostgreSQL, and PPAS each can have only
      one initial account. Other accounts are created by the initial account
      that has logged on to the database.
    AllowedValues:
      - Normal
      - Super
    Default: Normal
  AccountPassword:
    Type: String
    Description: >-
      The account password for the database instance. It may consist of letters,
      digits, or underlines, with a length of 8 to 32 characters.
    MinLength: 8
    MaxLength: 32
  AccountName:
    Type: String
```

资源编排

```
    Description: |-
      Account name, which must be unique and meet the following requirements:
      Start with a letter;
      Consist of lower-case letters, digits, and underscores (_);
      Contain no more than 16 characters.
      For other invalid characters, see Forbidden keywords table.
Resources:
  Account:
    Properties:
      AccountDescription:
        Ref: AccountDescription
      DBInstanceId:
        Ref: DBInstanceId
      AccountType:
        Ref: AccountType
      AccountPassword:
        Ref: AccountPassword
      AccountName:
        Ref: AccountName
Outputs:
  AccountName:
    Description: Account name
    Value:
      'Fn::GetAtt':
        - AccountName
```

#### ALIYUN::RDS::AccountPrivilege

**语法**

```json
{
  "Type": "ALIYUN::RDS::AccountPrivilege",
  "Properties": {
    "AccountPrivilege": String,
    "DBInstanceId": String,
    "DBName": String,
    "AccountName": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|

资源编排

| AccountPrivilege | String | 是 | 是 | 账号权限。 | 取值范围： ReadWrite：读写； ReadOnly：只读； DDLOnly：仅执行DDL，适用于MySQL和 MariaDB； DMLOnly：只执行DML，适用于MySQL和 MariaDB； DBOwner：数据库所有者，适用于SQL Server。 |
|---|---|---|---|---|---|
| DBInstanceId | String | 是 | 否 | 实例ID。 | 无。 |
| DBName | String | 是 | 否 | 需要授权访问的数据库名称。 | 无。 |
| AccountName | String | 是 | 否 | 账号名称。 | 无。 |

**返回值**

Fn::GetAtt 无。

**示例**

资源编排

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "AccountPrivilege": {
      "Type": "ALIYUN::RDS::AccountPrivilege",
      "Properties": {
        "AccountPrivilege": {
          "Ref": "AccountPrivilege"
        },
        "DBInstanceId": {
          "Ref": "DBInstanceId"
        },
        "DBName": {
          "Ref": "DBName"
        },
        "AccountName": {
          "Ref": "AccountName"
        }
      }
    }
  },
  "Parameters": {
    "AccountPrivilege": {
      "Type": "String",
      "Description": "RDS account privilege",
      "AllowedValues": ["ReadOnly", "ReadWrite", "DDLOnly", "DMLOnly", "DBOwner"]
    },
    "DBInstanceId": {
      "Type": "String",
      "Description": "RDS instance ID."
    },
    "DBName": {
      "Type": "String",
      "Description": "RDS database name"
    },
    "AccountName": {
      "Type": "String",
      "Description": "RDS account name."
    }
  },
  "Outputs": {}
}
```

#### ALIYUN::RDS::DBInstance

**语法**

```json
{
  "Type": "ALIYUN::RDS::DBInstance",
  "Properties": {
    "PeriodType": String,
    "Category": String,
    "PrivateIpAddress": String,
    "ResourceGroupId": String,
    "TargetDedicatedHostIdForSlave": String,
    "DBInstanceNetType": String,
    "DBTimeZone": String,
    "DedicatedHostGroupId": String,
    "EncryptionKey": String,
```

资源编排

```json
    "PreferredBackupPeriod": List,
    "SecurityIPList": String,
    "SecurityGroupId": String,
    "DBIsIgnoreCase": Integer,
    "DBInstanceStorage": Integer,
    "DBMappings": List,
    "Port": Integer,
    "ConnectionStringPrefix": String,
    "ConnectionStringType": String,
    "MultiAZ": Boolean,
    "MaintainTime": String,
    "Engine": String,
    "DBParamGroupId": String,
    "DBInstanceDescription": String,
    "Tags": Map,
    "TargetDedicatedHostIdForMaster": String,
    "EngineVersion": String,
    "ZoneId": String,
    "DBInstanceClass": String,
    "AllocatePublicConnection": Boolean,
    "PreferredBackupTime": String,
    "VSwitchId": String,
    "BackupPolicyMode": String,
    "Period": Integer,
    "PayType": String,
    "DBInstanceStorageType": String,
    "RoleARN": String,
    "MasterUserPassword": String,
    "MasterUserType": String,
    "VpcId": String,
    "MasterUsername": String,
    "ConnectionMode": String,
    "BackupRetentionPeriod": Number,
    "TargetDedicatedHostIdForLog": String,
    "SlaveZoneIds": List,
    "AutoRenew": Boolean,
    "SQLCollectorStatus": String,
    "SSLSetting": String,
    "LogBackupFrequency": String,
    "EnableBackupLog": Boolean,
    "ReleasedKeepPolicy": String,
    "ArchiveBackupRetentionPeriod": Integer,
    "ArchiveBackupKeepPolicy": String,
    "ArchiveBackupKeepCount": Integer,
    "LogBackupRetentionPeriod": Integer,
    "HighSpaceUsageProtection": String,
    "LocalLogRetentionSpace": Integer,
    "BackUpCategory": String,
    "CompressType": Integer,
    "LocalLogRetentionHours": Integer,
    "LogBackupLocalRetentionNumber": Integer,
    "ServerlessConfig": Map
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ResourceGroup Id | String | 否 | 是 | 资源组ID。 | 无 |

资源编排

| Engine | String | 是 | 否 | 数据库类型。 | 取值： MySQL SQLServer PostgreSQL PPAS MariaDB |
|---|---|---|---|---|---|
| DBInstanceStor age | Integer | 是 | 是 | 数据库存储空间。 | 取值： MySQL：5~1000。 SQLServer：10~1000。 PostgreSQL：5~2000。 PPAS：5~2000。 单位：GB。 说明每5 GB进行递增。 |
| EngineVersion | String | 是 | 否 | 数据库版本号。 | 取值： MySQL：5.5、5.6、5.7、8.0。 SQLServer：2008r2、 08r2 ent ha、2012、 _ _ 2012 ent ha、2012 std ha、 _ _ _ _ 2012 web、2014 std ha、 _ _ _ 2016 ent ha、2016 std ha、 _ _ _ _ 2016 web、2017 std ha、 _ _ _ 2017 ent、2019 ent。 _ _ PostgreSQL：9.4、10.0、11.0、 12.0。 PPAS：9.3、10.0。 MariaDB：10.3。 |
| Port | Integer | 否 | 是 | 实例端口。 | 无 |
| ConnectionStri ngPrefix | String | 否 | 是 | 连接地址的前缀。 | 长度为8~64个字符，可包含英文字母、 数字和短划线（-）。 |
| ConnectionStri ngType | String | 否 | 是 | 连接地址的类型。 | 取值： Inner：内网。 Public：公网。 |
| DBTimeZone | String | 否 | 否 | UTC时区。 | 取值范围：-12:59~+13:00。 说明如果不指定该参数，默认时区为地域默认时区。 本地SSD盘实例可以命名时区。 |
| DBParamGroup Id | String | 否 | 否 | 参数模板ID。 | 无 |
| Category | String | 否 | 否 | 实例系列。 | 取值： Basic：基础版。 HighAvailability：高可用版。 AlwaysOn：集群版。 Finance：三节点企业版。 |
| TargetDedicate dHostIdForMast er | String | 否 | 否 | 在专属集群内创建实例时，指定主实例的主机 ID。 | 无 |

资源编排

| DBIsIgnoreCase | Integer | 否 | 否 | 表名是否区分大小写。 | 取值： 0：区分大小写。 1（默认值）：不区分大小写。 |
|---|---|---|---|---|---|
| EncryptionKey | String | 否 | 否 | 同地域内的云盘加密的密钥ID。您可以在密钥管理服务控制台查看密钥ID， 也可以创建新的密钥。 | 传入该参数表示开启云盘加密（开启后无法关闭），并且需要传入RoleARN。 |
| MaintainTime | String | 否 | 否 | 实例的可维护时间段。 | 格式： HH:mmZ-HH:mmZ （UTC时间）。 |
| TargetDedicate dHostIdForSlav e | String | 否 | 否 | 在专属集群内创建实例时，指定备实例的主机 ID。 | 无 |
| DedicatedHost GroupId | String | 否 | 否 | 在专属集群内创建实例时，指定专属集群ID。 | 无 |
| DBInstanceStor ageType | String | 否 | 否 | 实例存储类型。 | 取值： local ssd：本地SSD盘（推荐）。 _ cloud ssd：SSD云盘。 _ cloud essd：ESSD云盘。 _ |
| RoleARN | String | 否 | 否 | 角色ARN。RDS通过该角色访问KMS。 | 无 |
| DBInstanceClas s | String | 是 | 是 | 实例规格。 | 无 |
| SecurityIPList | String | 是 | 是 | 允许访问该实例下所有数据库的IP白名单。 | 多个IP以半角逗号（,）间隔，不可以重复。最多支持1000个。 支持格式： IP地址形式，例如：10.23.XX.XX。 CIDR形式，例如： 10.23.XX.XX/24（无类域间路由，24表示了地址中前缀的长度，范围为1~32）。 |
| SecurityGroupI d | String | 否 | 是 | 关联的安全组ID。 | 最多支持关联3个安全组，多个安全组用半角逗号（,）隔开。清空安全组请指定空字符串。 |
| MultiAZ | Boolean | 否 | 否 | 该数据库实例是否支持多可用区。 | 取值： true：支持多可用区。 false：不支持多可用区。 |
| VpcId | String | 否 | 否 | 专有网络ID。 | 无 |
| DBMappings | List | 否 | 否 | 实例下创建新的数据库。 | 更多信息，请参见DBMappings属性。 |
| DBInstanceDes cription | String | 否 | 否 | 实例的描述或备注信息。 | 长度为2~256个字符。以英文字母或汉字开头，不能以 http:// 或 https:// 开头。 可包含汉字、英文字母、数字、下划线 （ ）和短划线（-）。 _ |

资源编排

| ConnectionMod e | String | 否 | 否 | 数据库的连接模式。 | 取值： Standard：标准访问模式。 Safe：高安全访问模式。 如果未指定该参数，则默认由RDS系统分配。 说明 SQL Server 2012/2016/2017只支持标准访问模式。 |
|---|---|---|---|---|---|
| MasterUsernam e | String | 否 | 否 | 数据库实例的主账号名称。 | 名称需要全局唯一。长度不超过16个字符。以英文字母开头，可包含英文字母、数字和下划线（ ）。 _ |
| MasterUserPass word | String | 否 | 否 | 数据库实例的主账号密码。 | 长度为8~32个字符。可包含英文字母、 数字和下划线（ ）。 _ |
| ZoneId | String | 否 | 否 | 可用区ID。 | 无 |
| DBInstanceNet Type | String | 否 | 否 | 数据库实例的网络类型。 | 取值 Internet：公网访问。 Intranet（默认值）：私网访问。 |
| VSwitchId | String | 否 | 否 | 交换机ID。 | 多个值用半角逗号（,）隔开。如果数据库类型为MariaDB，该参数必须指定。 |
| BackupPolicyM ode | String | 否 | 否 | 备份类型。 | 取值： DataBackupPolicy：数据备份。 LogBackupPolicy：日志备份。 |
| AllocatePublicC onnection | Boolean | 否 | 否 | 是否申请实例的外网连接串。 | 取值： true：申请实例的外网连接串。 false：不申请实例的外网连接串。 |
| PreferredBacku pTime | String | 否 | 否 | 备份时间。 | 格式： HH:mmZ- HH:mmZ 。 取值：00:00Z-01:00Z、01:00Z- 02:00Z、02:00Z-03:00Z、 03:00Z-04:00Z、04:00Z- 05:00Z、05:00Z-06:00Z、 06:00Z-07:00Z、07:00Z- 08:00Z、08:00Z-09:00Z、 09:00Z-10:00Z、10:00Z- 11:00Z、11:00Z-12:00Z、 12:00Z-13:00Z、13:00Z- 14:00Z、14:00Z-15:00Z、 15:00Z-16:00Z、16:00Z- 17:00Z、17:00Z-18:00Z、 18:00Z-19:00Z、19:00Z- 20:00Z、20:00Z-21:00Z、 21:00Z-22:00Z、22:00Z- 23:00Z、23:00Z-24:00Z。 |
| BackupRetentio nPeriod | Number | 否 | 否 | 备份保留天数。 | 取值范围：7~30。 单位：天。 默认值：7。 |
| PrivateIpAddres s | String | 否 | 否 | VSwitchId下的私网IP。 | 如果不指定该参数，系统将自动分配私网IP。 |

资源编排

| PreferredBacku pPeriod | List | 否 | 否 |  | 备份周期。 | 取值： Monday Tuesday Wednesday Thursday Friday Saturday Sunday |  |
|---|---|---|---|---|---|---|---|
| MasterUserTyp e | String | 否 | 否 |  | 主账号类型。 | 取值： Normal（默认值）：普通账号。 Super：高权限账号。 Sysadmin：管理员账号。 说明管理员账号只支持 SQLServer数据库。 |  |
| Tags | Map | 否 | 是 |  | Tag列表，包括TagKey 和TagValue。 | TagKey不能为空，TagValue可以为空。 格式示例： {“key1”:”value1”,“key2”:”” } 。 |  |
|  |  |  |  |  |  | } |  |
| PeriodType | String | 否 | 否 |  | 周期类型。 | 取值： Month（默认值） Year |  |
| PayType | String | 否 | 否 |  | 实例的付费类型。 | 取值： Postpaid：后付费，即按量付费。 Prepaid：预付费，即包年包月。 |  |
| Period | Integer | 否 | 否 |  | 预付费时长。 | 取值： 当参数PeriodType取值为Year时： 1~3。 当参数PeriodType取值为Month： 1~9。 |  |
| TargetDedicate dHostIdForLog | String | 否 | 否 |  | 在专属集群内创建实例时，指定日志实例的主机 ID。 | 无 |  |
| SlaveZoneIds | List | 否 | 否 |  | 高可用版或三节点企业版的备可用区。 | 最多指定两个备可用区，例如： ["zone-b"] 或 ["zone-b", "zone-c"] 。 为每个主可用区或者备可用区指定一个交换机，例如：ZoneId= "zone- a" 并且SlaveZoneIds= ["zone- c", "zone-b"] ，VSwitchID取值为 "vsw-zone-a,vsw-zone- c,vsw-zone-b" |  |
| SQLCollectorSt atus | String | 否 | 是 |  | 是否开启SQL洞察（SQL 审计）。 | 取值： Enable：开启SQL洞察。 Disabled：关闭SQL洞察。 |  |

| {“key1”:”value1”,“key2”:”” |  |
|---|---|

|  |  | ["zone-b"] |
|---|---|---|
|  | "zone-c"] |  |

| ["zone-b", |  |
|---|---|

|  | 业版 | a" |
|---|---|---|

资源编排

| SSLSetting | String | 否 | 否 | 实例的安全套接层 （SSL）链接设置。 | 取值： Disabled（默认值）：禁用SSL。 EnabledForPublicConnection：公网连接地址将受SSL证书保护。 说明该参数取值为 EnabledForPublicConnection 时，AllocatePublicConnectio n取值必须为true。 EnabledForInnerConnection：私网连接地址将受SSL证书保护。 |
|---|---|---|---|---|---|
| AutoRenew | Boolean | 否 | 否 | 是否自动续费。 | 仅在创建包年包月实例时传入。取值： true：自动续费。 false：不自动续费。 说明按月购买，则自动续费周期为1个月。 按年购买，则自动续费周期为1年。 |
| LogBackupFreq uency | String | 否 | 否 | 日志备份频率。 | 取值：LogInterval，表示每30分钟备份一次。 LogBackupFrequency的默认值与数据备份周期 PreferredBackupPeriod相同。 说明参数 LogBackupFrequency仅适用于 SQL Server。 |
| EnableBackupL og | Boolean | 否 | 否 | 是否启用日志备份功能。 | 取值： True：启用日志备份功能。 False：关闭日志备份功能说明当 BackupPolicyMode参数设置为 LogBackupPolicy时，必须指定该参数。 |
| ReleasedKeepP olicy | String | 否 | 否 | 实例释放后的归档备份保留策略。 | 取值： Lastest：仅保留最后存档的备份。 All：保留所有已存档的备份。 |
| ArchiveBackup RetentionPerio d | Integer | 否 | 否 | 归档备份的保留天数。 | 取值范围：30~1095。 单位：天。 |
| ArchiveBackup KeepPolicy | String | 否 | 否 | 归档备份的保留周期。 | 取值： ByMonth ByWeek KeepAll |
| ArchiveBackup KeepCount | Integer | 否 | 否 | 归档备份的保留个数。 | 取值： 当ArchiveBackupKeepPolicy取值为ByMonth时：1~31。 当ArchiveBackupKeepPolicy取值为ByWeek时：1~7。 当ArchiveBackupKeepPolicy取值为KeepAll时：无需指定该参数。 默认值：1。 |

资源编排

| LogBackupRete ntionPeriod | Integer | 否 | 否 | 日志备份保留天数。 | 取值范围：7~730。 日志备份保留期不能长于数据备份保留期。 说明如果启用了日志备份功能，您可以指定日志备份的保留期限。 |
|---|---|---|---|---|---|
| HighSpaceUsag eProtection | String | 否 | 否 | 指定当磁盘空间不足（实例超过80％或剩余空间少于5 GB）时是否强制删除日志备份文件 。 | 取值： Enable Disable 当BackupPolicyMode取值为 LogBackupPolicy时，必须指定该参数。 |
| LocalLogRetent ionSpace | Integer | 否 | 否 | 实例上允许存储日志备份文件的最大空间百分比。 | 取值范围：0~50。 如果日志备份文件的空间使用率超过该百分比，系统会提前删除记录备份文件，直到空间使用率降至此百分比以下。 说明当 BackupPolicyMode取值为 LogBackupPolicy时，必须指定该参数。 |
| BackUpCategor y | String | 否 | 否 | 是否启用二级备份功能。 | 取值： Flash：启用二级备份功能。 Standard：禁用二级备份功能。 |
| CompressType | Integer | 否 | 否 | 备份压缩方式。 | 取值： 1：使用zlib工具将备份压缩到.tar.gz 文件中。 4：使用QuickLZ工具将备份压缩到.xb.gz文件中。仅当实例运行 MySQL 5.6或5.7时，才支持此压缩格式。它可用于还原单个数据库和表。 8：使用QuickLZ工具将备份压缩为.xb.gz文件。仅当实例运行MySQL 8.0时，才支持此压缩格式。它不能用于还原单个数据库或表。 |
| LocalLogRetent ionHours | Integer | 否 | 否 | 本地日志备份保留小时数。 | 取值范围：0~168。 单位：小时。 0表示不在实例上保留日志备份文件。 说明当 BackupPolicyMode取值为 LogBackupPolicy时，必须指定该参数。 |
| LogBackupLoca lRetentionNum ber | Integer | 否 | 否 | 实例上可以保留的日志备份文件数。 | 取值范围：6~100。 默认值：60。 |
| ServerlessConfi g | Map | 否 | 否 | RDS Serverless实例的相关设置。 | 更多信息，请参见ServerlessConfig属性。 |

资源编排

**ServerlessConfig语法**

```json
"ServerlessConfig": {
    "SwitchForce": Boolean,
    "MaxCapacity": Number,
    "MinCapacity": Number,
    "AutoPause": Boolean
  }
```

**ServerlessConfig属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
|  |  |  |  | 是否开启 | 取值： true：开启。 false（默认）：不开启。 |

资源编排

| SwitchForce | Boolean | 否 | 否 | 是否开启 Serverless实例的强制弹性扩容和缩容。 | 说明开启该参数后， 实例进行强制扩容和缩容时会有 1分钟以内的闪断， 请您根据实际情况谨慎使用。 实例 RCU 的弹性扩容和缩容通常会立刻生效， 但在某些特殊情况下 （例如： |
|---|---|---|---|---|---|
|  |  |  |  |  | 大事务执行中） 无法即刻完成扩容和缩容， 此时可开启本参数进行强制扩容和缩容。 |
| MaxCapacity | Number | 是 | 否 | 实例RCU（RDS Capacity Unit） 自动扩容和缩容范围的最大值。 | 取值：0.5~8。 说明该参数的值必须大于等于 MinCapacity 参数。 |

资源编排

| MinCapacity | Number | 是 | 否 | 实例RCU自动扩容和缩容范围的最小值。 | 取值：0.5~8。 说明该参数的值必须小于等于 MaxCapacit y参数。 |
|---|---|---|---|---|---|
| AutoPause | Boolean | 否 | 否 | 是否开启 Serverless实例的智能暂停和启动。 | 取值： true：开启。 false（默认）：不开启。 说明如果10分钟无任何连接将进入暂停状态，当连接进入时会自动唤醒。 |

**DBMappings语法**

```json
"DBMappings": [
  {
    "DBDescription": String,
    "CharacterSetName": String,
    "DBName": String
  }
```

]

**DBMappings属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| CharacterSetName | String | 是 | 否 | 字符集。 | 取值： MySQL类型： utf8 gbk latin1 utf8mb4（适用于5.5版和 5.6版） SQLServer类型： Chinese PRC CI AS _ _ _ Chinese PRC CS AS _ _ _ SQL Latin1 General CP _ _ _ 1 CI AS _ _ SQL Latin1 General CP _ _ _ 1 CS AS _ _ Chinese PRC BIN _ _ |
| DBName | String | 是 | 否 | 数据库名称。 | 名称需要全局唯一。 长度不超过64个字符。以英文字母开头，可包含英文字母、数字和下划线（ ）。 _ |

资源编排

| DBDescription | String | 否 | 否 | 数据库描述。 | 长度为2~256个字符。以英文字母或汉字开头，不能以 http:// 或 https:// 开头。可包含汉字、英文字母、 数字、下划线（ ）和短划线 _ （-）。 |
|---|---|---|---|---|---|

**返回值**

Fn::GetAtt DBInstanceId：数据库实例ID。 InnerPort：数据库实例的内网端口。 InnerIPAddress：内网IP。 InnerConnectionString：内网连接地址。 PublicPort：数据库实例公网端口。 PublicConnectionString：公网连接地址。 PublicIPAddress：公网IP。

**示例**

`YAML` 格式资源编排

```
ROSTemplateFormatVersion: '2015-09-01' Description: Test RDS DBInstance Parameters:
  VpcId:
    Type: String
    Description:
      en: Please search the ID starting with (vpc-xxx) from console-Virtual Private Cloud
```

`zh-cn:` 现有虚拟专有网络的实例`ID`

```
    Label:
      en: VPC ID
```

`zh-cn:` 专有网络`VPC`实例`ID`

```
  VSwitchId:
    AssociationProperty: ALIYUN::ECS::VSwitch::VSwitchId
    AssociationPropertyMetadata:
      VpcId: ${VpcId}
      ZoneId: ${VSwitchZoneId}
    Type: String
    Description:
      en: Instance ID of existing business network switches, console-Virtual Private Cloud-VSwitche
s under query
```

`zh-cn:` 现有业务网络交换机的实例`ID`

```
    Label:
      en: VSwitch ID
```

`zh-cn:` 交换机实例`ID`

```
Resources:
  RDSInstance:
    DependsOn: VSwitch
    Properties:
      VpcId:
        Ref: VpcId
      VSwitchId:
        Ref: VSwitchId
      EngineVersion: '5.6'
      DBInstanceClass: rds.mysql.s2.large
      SecurityIPList: 0.0.0.0/0
      DBInstanceStorage: 5
      Engine: MySQL
      DBMappings:
        - CharacterSetName: utf8
          DBName: DBTest
Outputs:
  DBInstanceId:
    Value:
      Fn::GetAtt:
        - RDSInstance
        - DBInstanceId
```

`JSON` 格式

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Description": "Test RDS DBInstance",
  "Parameters": {
    "VpcId": {
      "AssociationProperty": "ALIYUN::ECS::VPC::VPCId",
      "Type": "String",
      "Description": {
        "en": "Please search the ID starting with (vpc-xxx) from console-Virtual Private Cloud",
```

`"zh-cn": "`现有虚拟专有网络的实例`ID"`

```
      },
```

"

```
bl" {
```

资源编排

```json
      "Label": {
        "en": "VPC ID",
```

`"zh-cn": "`专有网络`VPC`实例`ID"`

```json
      }
    },
    "VSwitchId": {
      "AssociationProperty": "ALIYUN::ECS::VSwitch::VSwitchId",
      "AssociationPropertyMetadata": {
        "VpcId": "${VpcId}",
        "ZoneId": "${VSwitchZoneId}"
      },
      "Type": "String",
      "Description": {
        "en": "Instance ID of existing business network switches, console-Virtual Private Cloud-VSw
itches under query",
```

`"zh-cn": "`现有业务网络交换机的实例`ID"`

```json
      },
      "Label": {
        "en": "VSwitch ID",
```

`"zh-cn": "`交换机实例`ID"`

```json
      }
    }
  },
  "Resources": {
    "RDSInstance": {
      "DependsOn": "VSwitch",
      "Type": "ALIYUN::RDS::DBInstance",
      "Properties": {
        "VpcId": {
          "Ref": "VpcId"
        },
        "VSwitchId": {
          "Ref": "VSwitchId"
        },
        "EngineVersion": "5.6",
        "DBInstanceClass": "rds.mysql.s2.large",
        "SecurityIPList": "0.0.0.0/0",
        "DBInstanceStorage": 5,
        "Engine": "MySQL",
        "DBMappings": [
          {
            "CharacterSetName": "utf8",
            "DBName": "DBTest"
          }
```

]

```json
      }
    }
  },
  "Outputs": {
    "DBInstanceId": {
      "Value": {
        "Fn::GetAtt": [
          "RDSInstance",
          "DBInstanceId"
```

]

```
      }
    }
  }
}
```

更多示例，请参见创建数据库实例、创建管理数据库的账号、授权账号访问数据库、修改数据库参数列表、修改实例访问白名单、为某个实例创建一个只读实例和在实例下创建数据库的组合示例：JSON示例和YAML示例。 资源编排

#### ALIYUN::RDS::DBInstanceParameterGroup

ALIYUN::RDS::DBInstanceParameterGroup类型用于修改RDS实例的参数。

**语法**

```json
{
  "Type": "ALIYUN::RDS::DBInstanceParameterGroup",
  "Properties": {
    "Forcerestart": String,
    "DBInstanceId": String,
    "Parameters": List
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| DBInstanceId | String | 是 | 否 | 实例ID。 | 无 |
| Parameters | List | 是 | 是 | 实例的参数。 | 更多信息，请参见Parameters属性。 |
| Forcerestart | String | 否 | 是 | 是否强制重启实例。 | 取值： true：强制重启。 false（默认值）：不强制重启。 |

**Parameters语法**

```json
"Parameters": [
  {
    "Key": String,
    "Value": String
  }
```

]

**Parameters属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Key | String | 是 | 否 | 参数名称。 | 无 |
| Value | String | 是 | 否 | 参数值。 | 无 |

**返回值**

Fn::GetAtt 无。

**示例**

`JSON` 格式资源编排

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "Parameters": {
      "Type": "Json",
      "Description": "Parameters to update for selected database instance.",
      "Default": {"delayed_insert_timeout":"600","max_length_for_sort_data":"2048"}
    },
    "DBInstanceId": {
      "Type": "String",
      "Description": "Database InstanceId to update properties."
      "Default": rm-uf6wjk5xxxxxxx
    },
    "Forcerestart": {
      "Type": "String",
      "Description": "whether restart database instance.",
      "AllowedValues": [
        "true",
        "false"
```

`],`

```json
      "Default": "false"
    }
  },
  "Resources": {
    "DBInstanceParameterGroup": {
      "Type": "ALIYUN::RDS::DBInstanceParameterGroup",
      "Properties": {
        "Parameters": {
          "Ref": "Parameters"
        },
        "DBInstanceId": {
          "Ref": "DBInstanceId"
        },
        "Forcerestart": {
          "Ref": "Forcerestart"
        }
      }
    }
  }
}
```

#### ALIYUN::RDS::DBInstanceSecurityIps

ALIYUN::RDS::DBInstanceSecurityIps类型用于修改实例访问白名单。

**语法**

```json
{
  "Type": "ALIYUN::RDS::DBInstanceSecurityIps",
  "Properties": {
    "DBInstanceId": String,
    "DBInstanceIPArrayName": String,
    "DBInstanceIPArrayAttribute": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|

资源编排

| DBInstanceId | String | 是 | 否 | 实例ID | 无 |
|---|---|---|---|---|---|
| DBInstanceIPArr ayAttribute | String | 是 | 是 | IP白名单分组的属性值。 | 控制台不显示带有 hidden标签的分组。 |
| DBInstanceIPArr ayName | String | 否 | 否 | IP白名单分组的名字 | 只支持小写字母和下划线（ ）。 默 _ 认为 Default 分组。 |

**返回值**

Fn::GetAtt SecurityIps：修改后的实例访问白名单。

**示例**

资源编排

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "DBInstanceSecurityIps": {
      "Type": "ALIYUN::RDS::DBInstanceSecurityIps",
      "Properties": {
        "DBInstanceIPArrayName": {
          "Ref": "DBInstanceIPArrayName"
        },
        "DBInstanceId": {
          "Ref": "DBInstanceId"
        },
        "DBInstanceIPArrayAttribute": {
          "Ref": "DBInstanceIPArrayAttribute"
        }
      }
    }
  },
  "Parameters": {
    "DBInstanceIPArrayName": {
      "Type": "String",
      "Description": "Group name of the security ips, only support lower characters and '_'. Advice u
se a new group name avoid effect your database system. If the properties is not specified, it will se t to default group, please be careful."
    },
    "DBInstanceId": {
      "Type": "String",
      "Description": "Database instance id to update security ips."
    },
    "DBInstanceIPArrayAttribute": {
      "Type": "String",
      "Description": "Security ips to add or remove."
    }
  },
  "Outputs": {
    "SecurityIps": {
      "Description": "The security ips of selected database instance.",
      "Value": {
        "Fn::GetAtt": [
          "DBInstanceSecurityIps",
          "SecurityIps"
```

]

```
      }
    }
  }
}
```

#### ALIYUN::RDS::PrepayDBInstance

**语法**

```json
{
  "Type": "ALIYUN::RDS::PrepayDBInstance",
  "Properties": {
    "DBMappings": List,
    "CouponCode": String,
    "MasterUsername": String,
    "PeriodType": String,
    "DBInstanceNetType": String,
```

资源编排

```json
    "MasterUserType": String,
    "AutoRenew": Boolean,
    "PreferredBackupTime": String,
    "PrivateIpAddress": String,
    "Engine": String,
    "MultiAZ": Boolean,
    "VpcId": String,
    "ConnectionMode": String,
    "ResourceGroupId": String,
    "VSwitchId": String,
    "BackupRetentionPeriod": Number,
    "Quantity": Number,
    "CommodityCode": String,
    "ZoneId": String,
    "AutoPay": Boolean,
    "Port": Integer,
    "ConnectionStringPrefix": String,
    "ConnectionStringType": String,
    "EngineVersion": String,
    "DBInstanceClass": String,
    "PreferredBackupPeriod": List,
    "DBInstanceStorage": Integer,
    "DBInstanceDescription": String,
    "Tags": Map,
    "Period": Number,
    "MasterUserPassword": String,
    "AllocatePublicConnection": Boolean,
    "SlaveZoneIds": List,
    "TargetDedicatedHostIdForMaster": String,
    "RoleARN": String,
    "DBInstanceStorageType": String,
    "Category": String,
    "DBParamGroupId": String,
    "EncryptionKey": String,
    "DBIsIgnoreCase": Integer,
    "SecurityGroupId": String,
    "TargetDedicatedHostIdForLog": String,
    "DBTimeZone": String,
    "DedicatedHostGroupId": String,
    "TargetDedicatedHostIdForSlave": String,
    "MaintainTime": String,
    "SQLCollectorStatus": String,
    "SSLSetting": String,
    "ArchiveBackupRetentionPeriod": Integer,
    "LogBackupRetentionPeriod": Integer,
    "EnableBackupLog": Boolean,
    "LogBackupLocalRetentionNumber": Integer,
    "ArchiveBackupKeepPolicy": String,
    "LocalLogRetentionHours": Integer,
    "HighSpaceUsageProtection": String,
    "CompressType": Integer,
    "LogBackupFrequency": String,
    "BackupPolicyMode": String,
    "ArchiveBackupKeepCount": Integer,
    "LocalLogRetentionSpace": Integer,
    "ReleasedKeepPolicy": String,
    "BackUpCategory": String
  }
}
```

**属性**

资源编排

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ResourceGroupId | String | 否 | 是 | 资源组ID。 | 无 |
| DBMappings | List | 否 | 否 | 实例下创建的数据库。 | 更多信息，请参见DBMappings 属性。 |
| CouponCode | String | 否 | 否 | 优惠码。 | 无 |
| MasterUsername | String | 否 | 否 | 数据库实例的数据库账号名称。 | 名称需要全局唯一。 长度为2~16个字符，以英文字母开头，以英文字母或数字结尾。 可包含英文字母、数字和下划线 （ ）。 _ |
| PeriodType | String | 是 | 否 | 周期类型。 | 取值： Year Month（默认值） |
| DBInstanceNetType | String | 否 | 否 | 数据库实例的网络类型。 | 取值： Internet：公网访问。 Intranet（默认值）：私网访问。 |
| MasterUserType | String | 否 | 否 | 数据库账号的权限类型。 | 取值： Normal（默认值）：普通账号。 Super：高权限账号。 Sysadmin：管理员账号。 说明管理员账号只支持SQLServer数据库。 |
| Port | Integer | 否 | 是 | 实例端口。 | 无 |
| ConnectionStringPre fix | String | 否 | 是 | 连接地址的前缀。 | 长度为8~64个字符，可包含英文字母、数字和短划线（-）。 |
| ConnectionStringTyp e | String | 否 | 是 | 连接地址的类型。 | 取值： Inner：内网。 Public：公网。 |
| PreferredBackupTim e | String | 否 | 否 | 备份时间。 | 格式：HH:mmZ-HH:mmZ。 取值：00:00Z-01:00Z、 01:00Z-02:00Z、02:00Z- 03:00Z、03:00Z-04:00至 23:00Z-24:00Z。 |
| PrivateIpAddress | String | 否 | 否 | 指定交换机下的私网IP地址。 | 如果不指定该参数，则系统自动分配私网IP地址。 |
| Engine | String | 是 | 否 | 数据类型。 | 取值： MySQL SQLServer PostgreSQL PPAS MariaDB |

资源编排

| MultiAZ | Boolean | 否 | 否 | 数据库实例是否支持多可用区。 | 取值： true false |
|---|---|---|---|---|---|
| VpcId | String | 否 | 否 | 专有网络ID。 | 无 |
| ConnectionMode | String | 否 | 否 | 数据库的连接模式。 | 取值： Standard：标准访问模式。 说明 SQL Server 2012/2016/2017只支持标准访问模式。 Safe（默认值）：高安全访问模式。 如果未指定该参数，则默认由 RDS系统分配。 |
| AutoRenew | Boolean | 否 | 否 | 实例是否自动续费。 | 取值： true false |
| VSwitchId | String | 否 | 否 | 交换机ID。 | 无 |
| BackupRetentionPeri od | Number | 否 | 否 | 备份保留天数。 | 无 |
| Quantity | Number | 否 | 否 | 创建的实例数量。 | 取值范围：1~99。 默认值：1。 |
| CommodityCode | String | 是 | 否 | 商品码。 | 取值： rds bards rords |
| ZoneId | String | 否 | 否 | 可用区ID。 | 无 |
| EngineVersion | String | 是 | 否 | 数据库版本号。 | 取值： MySQL：5.5、5.6、5.7、 8.0。 SQLServer：2008r2、 08r2 ent ha、2012、 _ _ 2012 ent ha、 _ _ 2012 std ha、2012 web、 _ _ _ 2014 std ha、 _ _ 2016 ent ha、 _ _ 2016 std ha、2016 web、 _ _ _ 2017 std ha、2017 ent、 _ _ _ 2019 ent。 _ PostgreSQL：9.4、10.0、 11.0、12.0。 PPAS：9.3、10.0。 MariaDB：10.3。 |
| DBInstanceClass | String | 是 | 是 | 实例规格。 | 例如：rds.mys2.large、 rds.mss1.large、 rds.pg.s1.small。 |

资源编排

| PreferredBackupPeri od | List | 否 | 否 | 备份周期。 |  | 取值： Monday Tuesday Wednesday Thursday Friday Saturday Sunday |  |  |
|---|---|---|---|---|---|---|---|---|
| DBInstanceStorage | Integer | 是 | 是 | 数据库存储空间。 |  | 取值： MySQL：5~1000。 SQLServer：10~1000。 PostgreSQL和PPAS： 5~2000。 单位：GB。 说明每5 GB进行递增。 |  |  |
| DBInstanceDescripti on | String | 否 | 否 | 实例的描述或备注信息。 |  | 长度为2~256个字符。以汉字或英文字母开头，不能以 http:// 或 https:// 开头。可以包含汉字、英文字母、数字、下划线（ ）和短划线 _ （-）。 |  |  |
| Tags | Map | 否 | 是 | 标签。 |  | 无 |  |  |
| Period | Number | 是 | 否 | 购买时长。 |  | 取值： 选择按月支付，取值范围： 1~9。 选择按年支付，取值范围： 1~3。 |  |  |
| MasterUserPassword | String | 否 | 否 | 数据库实例的数据库账号密码。 |  | 长度为8~32个字符。由大写英文字母、小写英文字母、数字和特殊字符中的任意三种组成。支持特殊字符 !@#$&amp;%^* () +-= 。 _ |  |  |
|  |  |  |  |  |  |  | !@#$&amp;%^* |  |
|  |  |  |  |  |  | () +-= _ |  |  |
| AllocatePublicConne ction | Boolean | 否 | 否 | 是否申请实例的外网连接地址。 |  | 取值： true false |  |  |
| AutoPay | Boolean | 否 | 否 | 是否自动付款。 |  | 取值： true false（默认值） |  |  |

资源编排

| SlaveZoneIds | List | 否 | 否 |  |  | 高可用版或三 |  | 最多指定两个备可用区，例如： ["zone-b"] 或 ["zone- b", "zone-c"] 。 为每个主可用区或者备可用区指定一个交换机，例如：ZoneId = "zone-a" 并且 SlaveZoneIds = ["zone- c", "zone- b"] ，VSwitchID取值为 "vsw-zone-a,vsw-zone- c,vsw-zone-b" 。 如果自动选择备可用区，取值为 ["Auto"] 或 ["Auto", "Auto"] 。此时只需要指定主可用区交换机ID，备可用区交换机会自动创建。 |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  | 版或三 | c", "zone- |  |  |
|  |  |  |  |  |  | 节点企业版的备可用区。 |  |  |  |  |
|  |  |  |  |  |  |  |  | b"] |  |  |
|  |  |  |  |  |  |  |  | 为 |  |  |
|  |  |  |  |  |  |  |  | c,vsw-zone-b" |  |  |
| TargetDedicatedHos tIdForMaster | String | 否 | 否 |  |  | 在专属集群内创建实例时， 指定主实例的主机ID。 |  | 无 |  |  |
| RoleARN | String | 否 | 否 |  |  | 角色ARN。该角色允许RDS 访问KMS。 |  | 无 |  |  |
| DBInstanceStorageT ype | String | 否 | 否 |  |  | 实例存储类型。 |  | 取值： local ssd：本地SSD盘（推 _ 荐）。 cloud ssd：SSD云盘。 _ cloud essd：ESSD云盘。 _ |  |  |
| Category | String | 否 | 否 |  |  | 实例系列。 |  | 取值： Basic：基础版。 HighAvailability：高可用版。 AlwaysOn：集群版。 Finance：三节点企业版。 |  |  |
| DBParamGroupId | String | 否 | 否 |  |  | 参数模板ID。 |  | 无 |  |  |
| EncryptionKey | String | 否 | 否 |  |  | 同地域内的云盘加密的密钥 ID。 |  | 您可以在密钥管理服务控制台查看密钥ID，也可以创建新的密钥。 |  |  |
| DBIsIgnoreCase | Integer | 否 | 否 |  |  | 表名是否区分大小写。 |  | 取值： 1（默认值）：不区分大小写。 0：区分大小写。 |  |  |
| SecurityGroupId | String | 否 | 是 |  |  | 关联的安全组 ID。 |  | 最多支持关联3个安全组，多个安全组用半角逗号（,）隔开。清空安全组请指定空字符串。 |  |  |
| TargetDedicatedHos tIdForLog | String | 否 | 否 |  |  | 在专属集群内创建实例时， 指定日志实例的主机ID。 |  | 无 |  |  |
| DBTimeZone | String | 否 | 否 |  |  | UTC时区。 |  | 取值范围：-12:59 ~ +13:00。 如果不指定该参数，默认时区为地域默认时区。 本地SSD盘实例可以命名时区。 |  |  |

| ["zone- |  |
|---|---|

|  | b", "zone-c"] |
|---|---|

| ["Auto", |  |
|---|---|

|  | "Auto"] |  |
|---|---|---|

资源编排

| DedicatedHostGroup Id | String | 否 | 否 | 在专属集群内创建实例时， 指定专属集群 ID。 | 无 |
|---|---|---|---|---|---|
| TargetDedicatedHos tIdForSlave | String | 否 | 否 | 在专属集群内创建实例时， 指定备实例的主机ID。 | 无 |
| MaintainTime | String | 否 | 否 | 实例的可维护时间段。 | 格式：HH:mmZ-HH:mmZ。 |
| SQLCollectorStatus | String | 否 | 是 | 是否开启SQL 洞察（SQL审计）。 | 取值： Enable：开启。 Disabled：关闭。 |
| SSLSetting | String | 否 | 否 | 实例的安全套接层（SSL） 链接设置。 | 取值： Disabled（默认值）：禁用 SSL。 EnabledForPublicConnecti on：公网连接地址将受SSL证书保护。 说明该参数取值为 EnabledForPublicConn ection 时，AllocatePublicCon nection取值必须为 true。 EnabledForInnerConnectio n：私网连接地址将受SSL证书保护。 |
| ArchiveBackupReten tionPeriod | Integer | 否 | 否 | 归档备份的保留天数。 | 无 |
| LogBackupRetention Period | Integer | 否 | 否 | 日志备份保留天数。 | 无 |
| EnableBackupLog | Boolean | 否 | 否 | 是否开启日志备份。 | 取值： true：开启 false：关闭 |
| LogBackupLocalRete ntionNumber | Integer | 否 | 否 | 本地Binlog保留个数。 | 无 |
| ArchiveBackupKeepP olicy | String | 否 | 否 | 归档备份的保留周期。 | 取值： ByMonth：月。 ByWeek：周。 KeepAll：全部保留。 归档备份的保留周期内能保存的备份个数由 ArchiveBackupKeepCount决定，默认为0。 说明当 BackupPolicyMode参数取值为DataBackupPolicy 时，该参数生效。 |
| LocalLogRetentionH ours | Integer | 否 | 否 | 本地日志备份保留小时数。 | 无 |

资源编排

| HighSpaceUsageProt ection | String | 否 | 否 | 实例使用空间大于80%，或者剩余空间小于5 GB时， 是否强制清理 Binlog。 | 取值： Disable：不清理。 Enable：清理。 |
|---|---|---|---|---|---|
| CompressType | Integer | 否 | 否 | 备份压缩方式。 | 取值： 0：不压缩。 1：zlib压缩。 2：并行zlib压缩。 4：quicklz压缩，开启了库表恢复。 8：MySQL8.0 quicklz压缩， 暂未支持库表恢复。 |
| LogBackupFrequenc y | String | 否 | 否 | 日志备份频率。 | 适用于SQL Server。 取值：LogInterval，表示每30 分钟备份一次。 说明默认与数据备份周期 PreferredBackupPeriod 一致。 |
| BackupPolicyMode | String | 否 | 否 | 备份类型。 | 取值： DataBackupPolicy：数据备份。 LogBackupPolicy：日志备份。 |
| ArchiveBackupKeep Count | Integer | 否 | 否 | 归档备份的保留个数。 | 无 |
| LocalLogRetentionSp ace | Integer | 否 | 否 | 本地日志最大空间使用率。 | 无 |
| ReleasedKeepPolicy | String | 否 | 否 | 已删除实例的归档备份保留策略。 | 取值： None：不保留。 Lastest：保留最后一个。 All：全部保留。 |
| BackUpCategory | String | 否 | 否 | 备份实例系列。 | 取值： Basic：基础版。 HighAvailability：高可用版。 AlwaysOn：集群版。 Finance：三节点企业版。 |

**DBMappings语法**

```json
"DBMappings": [
  {
    "DBDescription": String,
    "CharacterSetName": String,
    "DBName": String
  }
```

]

**DBMappings属性**

资源编排

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| DBDescription | String | 否 | 否 | 数据库描述。 | 长度为2~256个字符。以汉字或英文字母开头，不能以 http:// 或 https:// 开头。可包含汉字、英文字母、 数字、下划线（ ）和短划线 _ （-）。 |

资源编排

| CharacterSetName | String | 是 | 否 | 字符集。 | 取值： MySQL/MariaDB类型： utf8 gbk latin1 utf8mb4 SQLServer类型： Chinese PRC CI AS _ _ _ Chinese PRC CS AS _ _ _ SQL Latin1 General CP _ _ _ 1 CI AS _ _ SQL Latin1 General CP _ _ _ 1 CS AS _ _ Chinese PRC BIN _ _ PostgreSQL类型： KOI8U UTF8 WIN866 WIN874 WIN1250 WIN1251 WIN1252 WIN1253 WIN1254 WIN1255 WIN1256 WIN1257 WIN1258 EUC CN _ EUC KR _ EUC TW _ EUC JP _ EUC JIS 2004 _ _ KOI8R MULE INTERNAL _ LATIN1 LATIN2 LATIN3 LATIN4 LATIN5 LATIN6 LATIN7 LATIN8 LATIN9 LATIN10 ISO 8859 5 _ _ ISO 8859 6 _ _ ISO 8859 7 _ _ ISO 8859 8 _ _ SQL ASCII _ |
|---|---|---|---|---|---|
| DBName | String | 是 | 否 | 数据库名称。 | 名称需要全局唯一。 长度不超过64个字符。以小写英文字母开头，可包含小写英文字母、数字和下划线（ ）。 _ |

资源编排

**返回值**

Fn::GetAtt InnerPort：数据库实例的内网端口。 OrderId：订单ID。 PublicConnectionString：公网连接串。 InnerIPAddress：内网IP地址。 DBInstanceId：数据库实例ID。 PublicIPAddress：公网IP地址。 PublicPort：数据库实例公网端口。 InnerConnectionString：内网连接串。

**示例**

`JSON` 格式

```json
{
 "ROSTemplateFormatVersion": "2015-09-01",
 "Parameters": {
  "PeriodType": {
   "Type": "String",
   "Description": "Charge period for created instances.",
   "AllowedValues": [
    "Month",
    "Year"
```

`],`

```json
   "Default": "Month"
  },
  "ResourceGroupId": {
   "Type": "String",
   "Description": "Resource group id."
  },
  "ArchiveBackupRetentionPeriod": {
   "Type": "Number",
   "Description": "The number of days for which to retain archived backups. \n The default value 0 sp
ecifies not to enable the backup archiving function. Valid values: 30 to 1095.",
   "MinValue": 30,
   "MaxValue": 1095
  },
  "DBTimeZone": {
   "Type": "String",
   "Description": "The UTC time zone of the instance. Valid values: -12:00 to +12:00. The time zone m
ust be an integer value such as +08:00. Values such as +08:30 are not allowed."
  },
  "Port": {
   "Type": "Number",
   "Description": "The port of the database service.",
   "MinValue": 1,
   "MaxValue": 65535
  },
  "ArchiveBackupKeepCount": {
   "Type": "Number",
   "Description": "The number of archived backups that can be retained. Default value: 1. Valid value
s: \nThe value of this parameter ranges from 1 to 31 when the ArchiveBackupKeepPolicy \n parameter is set to ByMonth. \nThe value of this parameter ranges from 1 to 7 when the ArchiveBackupKeepPolicy \n parameter is set to ByWeek. \nNote You do not need to specify this parameter when the ArchiveBackupKeepPolicy \nparameter is set to KeepAll.",
   "MinValue": 1,
   "MaxValue": 31
  },
  "LogBackupRetentionPeriod": {
   "Type": "Number",
```

资源编排

```json
   "Description": "The number of days for which to retain log backup files. Valid values: 7 to 730. T
he log backup \n retention period cannot be longer than the data backup retention period.Note If you enable the log \n backup function, you can specify the log backup retention period. This applies only when the \n instance runs MySQL, PostgreSQL, or PPAS.",
   "MinValue": 7,
   "MaxValue": 730
  },
  "DBInstanceStorage": {
   "Type": "Number",
   "Description": "Database instance storage size. mysql is [5,1000]. sql server 2008r2 is [10,1000],
sql server 2012/2012_web/2016-web is [20,1000]. PostgreSQL and PPAS is [5,2000]. Increased every 5 GB , Unit in GB"
  },
  "DBMappings": {
   "Type": "Json",
   "Description": "Database mappings to attach to db instance."
  },
  "ConnectionStringPrefix": {
   "Type": "String",
   "Description": "The prefix of the endpoint. \nOnly the prefix of the CurrentConnectionString param
eter value can be modified.\nThe prefix must be 8 to 64 characters in length and can contain letters, digits, and hyphens (-). ",
   "AllowedPattern": "[a-zA-Z0-9-]{8,64}"
  },
  "MultiAZ": {
   "Type": "Boolean",
   "Description": "Specifies if the database instance is a multiple Availability Zone deployment. ",
   "AllowedValues": [
    "True",
    "true",
    "False",
    "false"
```

`],`

```json
   "Default": false
  },
  "Engine": {
   "Type": "String",
   "Description": "Database instance engine type. Support MySQL/SQLServer/PostgreSQL/PPAS/MariaDB now
.",
   "AllowedValues": [
    "MySQL",
    "SQLServer",
    "PostgreSQL",
    "PPAS",
    "MariaDB"
```

]

```json
  },
  "Tags": {
   "Type": "Json",
   "Description": "The tags of an instance.\nYou should input the information of the tag with the for
mat of the Key-Value, such as {\"key1\":\"value1\",\"key2\":\"value2\", ... \"key5\":\"value5\"}.\nAt most 5 tags can be specified.\nKey\nIt can be up to 64 characters in length.\nCannot begin with aliyu n.\nCannot begin with http:// or https://.\nCannot be a null string.\nValue\nIt can be up to 128 char acters in length.\nCannot begin with aliyun.\nCannot begin with http:// or https://.\nCan be a null s tring."
  },
  "DBInstanceDescription": {
   "Type": "String",
   "Description": "Description of created database instance."
  },
  "TargetDedicatedHostIdForMaster": {
   "Type": "String",
```

`"D`

```
iti
```

"

```
"Th
```

`ID`

```
fth
```

h tt

```
hihth
```

i t bl `if` t i i t 资源编排

```json
   "Description": "The ID of the host to which the instance belongs if you create a primary instance
in a host group."
  },
  "EngineVersion": {
   "Type": "String",
   "Description": "Database instance version of the relative engine type.Support MySQL:
5.5/5.6/5.7/8.0;\nSQLServer: 2008r2/2012/2012_ent_ha/2012_std_ha/2012_web/2016_ent_ha/2016_std_ha/2016_web/2017_std_ha/2017_ent;\nPo reSQL: 9.4/10.0/11.0/12.0;\nPPAS: 9.3/10.0;\nMariaDB: 10.3."
  },
  "DBInstanceClass": {
   "Type": "String",
   "Description": "Database instance type. Refer the RDS database instance type reference, such as 'r
ds.mys2.large', 'rds.mss1.large', 'rds.pg.s1.small' etc"
  },
  "ArchiveBackupKeepPolicy": {
   "Type": "String",
   "Description": "The period for which to retain archived backups. The number of archived backups th
at can \n be retained within the specified period is determined by the ArchiveBackupKeepCount paramet er. \n Default value: 0. Valid values: \nByMonth \n ByWeek \n KeepAll",
   "AllowedValues": [
    "ByMonth",
    "ByWeek",
    "KeepAll"
```

]

```json
  },
  "VSwitchId": {
   "Type": "String",
   "Description": "The vSwitch id of created instance. For VPC network, the property is required."
  },
  "BackupPolicyMode": {
   "Type": "String",
   "Description": "Backup type, \nDataBackupPolicy: data backup \nLogBackupPolicy: log backup",
   "AllowedValues": [
    "DataBackupPolicy",
    "LogBackupPolicy"
```

]

```json
  },
  "Period": {
   "Type": "Number",
   "Description": "Prepaid time period. While choose by pay by month, it could be from 1 to 9. While
choose pay by year, it could be from 1 to 3.",
   "MinValue": 1,
   "MaxValue": 9,
   "Default": 1
  },
  "LocalLogRetentionHours": {
   "Type": "Number",
   "Description": "The number of hours for which to retain log backup files on the instance. \nValid
values: 0 to 168. The value 0 specifies not to retain log backup files on the instance. \nYou can ret ain the default value. Note You must specify this parameter when the BackupPolicyMode \nparameter is set to LogBackupPolicy.",
   "MinValue": 0,
   "MaxValue": 168
  },
  "HighSpaceUsageProtection": {
   "Type": "String",
   "Description": "Specifies whether to forcibly delete log backup files when the space usage of the
\n instance exceeds 80% or the remaining space is less than 5 GB. Valid values: \n Enable and Disable . You can retain the default value. Note You must specify \n this parameter when the BackupPolicyMode parameter is set to LogBackupPolicy.",
   "AllowedValues": [
    "Enable",
```

资源编排 ,

```
    "Disable"
```

]

```json
  },
  "RoleARN": {
   "Type": "String",
   "Description": "The Alibaba Cloud Resource Name (ARN) provided to the service account of the insta
nce by your Alibaba Cloud account to connect to KMS. You can copy the ARN from the RAM console."
  },
  "MasterUserPassword": {
   "Type": "String",
   "Description": "The master password for the database instance. ",
   "MinLength": 8,
   "MaxLength": 32
  },
  "VpcId": {
   "Type": "String",
   "Description": "The VPC id of created database instance. For VPC network, the property is required
```

`."`

```json
  },
  "SSLSetting": {
   "Type": "String",
   "Description": "Secure Sockets Layer (SSL) link setting of the instance. Valid values:\nDisabled:
Disable SSL\nEnabledForPublicConnection: Public connection address will be protected by the SSL certi ficate. It requires AllocatePublicConnection is true.\nEnabledForInnerConnection: Private connection address will be protected by the SSL certificate.\nDefault value is Disabled.",
   "AllowedValues": [
    "Disabled",
    "EnabledForPublicConnection",
    "EnabledForInnerConnection"
```

`],`

```json
   "Default": "Disabled"
  },
  "MasterUsername": {
   "Type": "String",
   "Description": "The master user name for the database instance. "
  },
  "ConnectionMode": {
   "Type": "String",
   "Description": "Connection Mode for database instance,support 'Standard' and 'Safe' mode. Default
is RDS system assigns. "
  },
  "LocalLogRetentionSpace": {
   "Type": "Number",
   "Description": "The maximum percentage of space that is allowed to store log backup files on the i
nstance. \n If the space usage for log backup files exceeds this percentage, the system deletes earli er \n log backup files until the space usage falls below this percentage. Valid values:0 to 50. \n Yo u can retain the default value. Note You must specify this parameter when the \n BackupPolicyMode par ameter is set to LogBackupPolicy.",
   "MinValue": 0,
   "MaxValue": 50
  },
  "Category": {
   "Type": "String",
   "Description": "The edition of the instance. Valid values:\nBasic: specifies to use the Basic Edit
ion.\nHighAvailability: specifies to use the High-availability Edition.\nAlwaysOn: specifies to use t he Cluster Edition.\nFinance: specifies to use the Enterprise Edition.",
   "AllowedValues": [
    "Basic",
    "HighAvailability",
    "AlwaysOn",
    "Finance"
```

] 资源编排

```json
  },
  "PrivateIpAddress": {
   "Type": "String",
   "Description": "The private ip for created instance."
  },
  "TargetDedicatedHostIdForSlave": {
   "Type": "String",
   "Description": "The ID of the host to which the instance belongs if you create a secondary instanc
e in a host group."
  },
  "DBInstanceNetType": {
   "Type": "String",
   "Description": "Database instance net type, default is Intranet.Internet for public access, Intran
et for private access.",
   "AllowedValues": [
    "Internet",
    "Intranet"
```

`],`

```json
   "Default": "Intranet"
  },
  "ReleasedKeepPolicy": {
   "Type": "String",
   "Description": "The policy used to retain archived backups if the instance is released. Default va
lue: None. \n Valid values: \nLastest: Only the last archived backup is retained. \n All: All of the archived backups are retained.",
   "AllowedValues": [
    "Lastest",
    "All"
```

]

```json
  },
  "DedicatedHostGroupId": {
   "Type": "String",
   "Description": "The ID of the host group to which the instance belongs if you create an instance i
n a host group."
  },
  "AutoRenew": {
   "Type": "Boolean",
   "Description": "Auto renew the prepay instance. If the period type is by year, it will renew by ye
ar, else it will renew by month.",
   "AllowedValues": [
    "True",
    "true",
    "False",
    "false"
```

`],`

```json
   "Default": false
  },
  "EncryptionKey": {
   "Type": "String",
   "Description": "The ID of the encryption key that is used to encrypt data on SSDs in the region. Y
ou can view the encryption key ID in the Key Management Service (KMS) console. You can also create an encryption key."
  },
  "PreferredBackupPeriod": {
   "Type": "CommaDelimitedList",
   "Description": "The backup period. Separate multiple values with commas (,). The default value is
the original value. Valid values:Monday Tuesday Wednesday Thursday Friday Saturday Sunday Note When t he BackupPolicyMode parameter is set to DataBackupPolicy, this parameter is required."
  },
  "LogBackupLocalRetentionNumber": {
   "Type": "Number",
   "Description": "The number of log backup files that can be retained on the instance. \nDefault val
ue:60 Validvalues:6to100",
```

资源编排

```json
ue: 60. Valid values: 6 to 100.,
   "MinValue": 6,
   "MaxValue": 100
  },
  "SlaveZoneIds": {
   "Type": "Json",
   "Description": "List of slave zone ids can specify slave zone ids when creating the high-availabil
ity or enterprise edition instance. Meanwhile, VSwitchId needs to pass in the corresponding vswitch i d to the slave zone by order. For example, ZoneId = \"zone-a\" and SlaveZoneIds = [\"zone-c\", \"zone -b\"], then the VSwitchId must be \"vsw-zone-a,vsw-zone-c,vsw-zone-b\". Of course, you can also choos e automatic allocation, for example, ZoneId = \"zone-a\" and SlaveZoneIds = [\"Auto\", \"Auto\"], the n the VSwitchId must be \"vsw-zone-a,Auto,Auto\". The list contains up to 2 slave zone ids, separated by commas.",
   "MaxLength": 2
  },
  "DBIsIgnoreCase": {
   "Type": "Number",
   "Description": "Specifies whether table names are case-sensitive. Valid values:\n1: Table names ar
e not case-sensitive. This is the default value.\n0: Table names are case-sensitive."
  },
  "CommodityCode": {
   "Type": "String",
   "Description": "The CommodityCode of the order.",
   "AllowedValues": [
    "rds",
    "bards",
    "rords"
```

`],`

```json
   "Default": "rds"
  },
  "MaintainTime": {
   "Type": "String",
   "Description": "The period during which the maintenance performs. The format is HH:mmZ-HH:mmZ."
  },
  "DBParamGroupId": {
   "Type": "String",
   "Description": "The ID of the parameter template used by the instance."
  },
  "ZoneId": {
   "Type": "String",
   "Description": "selected zone to create database instance. You cannot set the ZoneId parameter if
the MultiAZ parameter is set to true."
  },
  "TargetDedicatedHostIdForLog": {
   "Type": "String",
   "Description": "The ID of the host to which the instance belongs if you create a log instance in a
host group."
  },
  "AllocatePublicConnection": {
   "Type": "Boolean",
   "Description": "If true, allocate public connection automate.",
   "AllowedValues": [
    "True",
    "true",
    "False",
    "false"
```

]

```json
  },
  "PreferredBackupTime": {
   "Type": "String",
   "Description": "The time when the backup task is performed. Format: yyyy-MM-ddZ-HH:mm:ssZ.Note Whe
n the BackupPolicyMode parameter is set to DataBackupPolicy, this parameter is required."
  },
```

资源编排

```json
  "SecurityGroupId": {
   "Type": "String",
   "Description": "The ID of the ECS security groups. \nEach RDS instance can be associated with up t
o three ECS security groups. \nYou must separate them with commas (,). \nTo delete an ECS Security gr oup, leave this parameter empty. \n"
  },
  "Quantity": {
   "Type": "Number",
   "Description": "The number of instance to be created, default is 1, max number is 99",
   "MinValue": 1,
   "MaxValue": 99,
   "Default": 1
  },
  "AutoPay": {
   "Type": "Boolean",
   "Description": "Automatic Payment. Default is false.",
   "AllowedValues": [
    "True",
    "true",
    "False",
    "false"
```

`],`

```json
   "Default": false
  },
  "DBInstanceStorageType": {
   "Type": "String",
   "Description": "The storage type of the instance. Valid values:\nlocal_ssd: specifies to use local
SSDs. This is the recommended storage type.\ncloud_ssd: specifies to use standard SSDs.\ncloud_essd: specifies to use enhanced SSDs."
  },
  "BackUpCategory": {
   "Type": "String",
   "Description": "Specifies whether to enable the second-level backup function. This function allows
a backup \nto be completed within seconds. Valid values: \nFlash: specifies to enable the second-leve l backup function. \n Standard: specifies to disable the second-level backup function.",
   "AllowedValues": [
    "Flash",
    "Standard"
```

]

```json
  },
  "CompressType": {
   "Type": "Number",
   "Description": "The format used to compress backups. Valid values: \n 1: The zlib tool is used to
compress backups into .tar.gz files. \n 4: The QuickLZ tool is used to compress backups into .xb.gz f iles. \nThis compression format is supported only when the instance runs MySQL 5.6 or 5.7. \nIt can b e used to restore individual databases and tables. \n 8: The QuickLZ tool is used to compress backups into .xb.gz files. \n This compression format is supported only when the instance runs MySQL 8.0. \nI t cannot be used to restore individual databases or tables."
  },
  "LogBackupFrequency": {
   "Type": "String",
   "Description": "The frequency at which to back up logs. Valid values: \nThe value LogInterval
specifies to back up logs every 30 minutes. \n The default value of this parameter is the same as the data backup frequency. \nNote The value LogInterval is supported only when the instance runs SQL Serv er."
  },
  "ConnectionStringType": {
   "Type": "String",
   "Description": "The endpoint type of the instance, allow values: Inner, Public",
   "AllowedValues": [
    "Inner",
    "Public"
```

] 资源编排 `],`

```json
   "Default": "Inner"
  },
  "CouponCode": {
   "Type": "String",
   "Description": "The coupon code of the order."
  },
  "MasterUserType": {
   "Type": "String",
   "Description": "Privilege type of account.\n Normal: Common privilege. \n Super: High privilege. \
nSysadmin: Super privileges (SA) (only supported by SQL Server)\nThe default value is Normal.",
   "AllowedValues": [
    "Normal",
    "Super",
    "Sysadmin"
```

`],`

```json
   "Default": "Normal"
  },
  "EnableBackupLog": {
   "Type": "Boolean",
   "Description": "Specifies whether to enable the log backup function. Valid values: \nTrue: specifi
es to enable the log backup function. \nFalse: specifies to disable the log backup function. \nNote Y ou must specify this parameter when the BackupPolicyMode parameter is set to LogBackupPolicy.",
   "AllowedValues": [
    "True",
    "true",
    "False",
    "false"
```

]

```json
  },
  "SQLCollectorStatus": {
   "Type": "String",
   "Description": "Specifies whether to enable or disable the SQL Explorer (SQL audit) feature. \nVal
id values:Enable | Disabled.",
   "AllowedValues": [
    "Enable",
    "Disabled"
```

]

```json
  },
  "BackupRetentionPeriod": {
   "Type": "Number",
   "Description": "The retention period of the data backup. Value range: 7 to 730. The default value
is the original value. Note When the BackupPolicyMode parameter is set to LogBackupPolicy, this param eter is required.",
   "Default": 7
  }
 },
 "Resources": {
  "PrepayDBInstance": {
   "Type": "ALIYUN::RDS::PrepayDBInstance",
   "Properties": {
    "PeriodType": {
     "Ref": "PeriodType"
    },
    "ResourceGroupId": {
     "Ref": "ResourceGroupId"
    },
    "ArchiveBackupRetentionPeriod": {
     "Ref": "ArchiveBackupRetentionPeriod"
    },
    "DBTimeZone": {
     "Ref": "DBTimeZone"
    },
```

资源编排

```json
    "Port": {
     "Ref": "Port"
    },
    "ArchiveBackupKeepCount": {
     "Ref": "ArchiveBackupKeepCount"
    },
    "LogBackupRetentionPeriod": {
     "Ref": "LogBackupRetentionPeriod"
    },
    "DBInstanceStorage": {
     "Ref": "DBInstanceStorage"
    },
    "DBMappings": {
     "Ref": "DBMappings"
    },
    "ConnectionStringPrefix": {
     "Ref": "ConnectionStringPrefix"
    },
    "MultiAZ": {
     "Ref": "MultiAZ"
    },
    "Engine": {
     "Ref": "Engine"
    },
    "Tags": {
     "Ref": "Tags"
    },
    "DBInstanceDescription": {
     "Ref": "DBInstanceDescription"
    },
    "TargetDedicatedHostIdForMaster": {
     "Ref": "TargetDedicatedHostIdForMaster"
    },
    "EngineVersion": {
     "Ref": "EngineVersion"
    },
    "DBInstanceClass": {
     "Ref": "DBInstanceClass"
    },
    "ArchiveBackupKeepPolicy": {
     "Ref": "ArchiveBackupKeepPolicy"
    },
    "VSwitchId": {
     "Ref": "VSwitchId"
    },
    "BackupPolicyMode": {
     "Ref": "BackupPolicyMode"
    },
    "Period": {
     "Ref": "Period"
    },
    "LocalLogRetentionHours": {
     "Ref": "LocalLogRetentionHours"
    },
    "HighSpaceUsageProtection": {
     "Ref": "HighSpaceUsageProtection"
    },
    "RoleARN": {
     "Ref": "RoleARN"
    },
    "MasterUserPassword": {
     "Ref": "MasterUserPassword"
}
```

资源编排

```json
    },
    "VpcId": {
     "Ref": "VpcId"
    },
    "SSLSetting": {
     "Ref": "SSLSetting"
    },
    "MasterUsername": {
     "Ref": "MasterUsername"
    },
    "ConnectionMode": {
     "Ref": "ConnectionMode"
    },
    "LocalLogRetentionSpace": {
     "Ref": "LocalLogRetentionSpace"
    },
    "Category": {
     "Ref": "Category"
    },
    "PrivateIpAddress": {
     "Ref": "PrivateIpAddress"
    },
    "TargetDedicatedHostIdForSlave": {
     "Ref": "TargetDedicatedHostIdForSlave"
    },
    "DBInstanceNetType": {
     "Ref": "DBInstanceNetType"
    },
    "ReleasedKeepPolicy": {
     "Ref": "ReleasedKeepPolicy"
    },
    "DedicatedHostGroupId": {
     "Ref": "DedicatedHostGroupId"
    },
    "AutoRenew": {
     "Ref": "AutoRenew"
    },
    "EncryptionKey": {
     "Ref": "EncryptionKey"
    },
    "PreferredBackupPeriod": {
     "Ref": "PreferredBackupPeriod"
    },
    "LogBackupLocalRetentionNumber": {
     "Ref": "LogBackupLocalRetentionNumber"
    },
    "SlaveZoneIds": {
     "Ref": "SlaveZoneIds"
    },
    "DBIsIgnoreCase": {
     "Ref": "DBIsIgnoreCase"
    },
    "CommodityCode": {
     "Ref": "CommodityCode"
    },
    "MaintainTime": {
     "Ref": "MaintainTime"
    },
    "DBParamGroupId": {
     "Ref": "DBParamGroupId"
    },
    "ZoneId": {
     "Ref": "ZoneId"
```

资源编排

```json
    },
    "TargetDedicatedHostIdForLog": {
     "Ref": "TargetDedicatedHostIdForLog"
    },
    "AllocatePublicConnection": {
     "Ref": "AllocatePublicConnection"
    },
    "PreferredBackupTime": {
     "Ref": "PreferredBackupTime"
    },
    "SecurityGroupId": {
     "Ref": "SecurityGroupId"
    },
    "Quantity": {
     "Ref": "Quantity"
    },
    "AutoPay": {
     "Ref": "AutoPay"
    },
    "DBInstanceStorageType": {
     "Ref": "DBInstanceStorageType"
    },
    "BackUpCategory": {
     "Ref": "BackUpCategory"
    },
    "CompressType": {
     "Ref": "CompressType"
    },
    "LogBackupFrequency": {
     "Ref": "LogBackupFrequency"
    },
    "ConnectionStringType": {
     "Ref": "ConnectionStringType"
    },
    "CouponCode": {
     "Ref": "CouponCode"
    },
    "MasterUserType": {
     "Ref": "MasterUserType"
    },
    "EnableBackupLog": {
     "Ref": "EnableBackupLog"
    },
    "SQLCollectorStatus": {
     "Ref": "SQLCollectorStatus"
    },
    "BackupRetentionPeriod": {
     "Ref": "BackupRetentionPeriod"
    }
   }
  }
 },
 "Outputs": {
  "InnerConnectionString": {
   "Description": "DB instance connection url by Intranet.",
   "Value": {
    "Fn::GetAtt": [
     "PrepayDBInstance",
     "InnerConnectionString"
```

]

```
   }
  },
```

资源编排

```json
  "DBInstanceId": {
   "Description": "The instance id of created database instance.",
   "Value": {
    "Fn::GetAtt": [
     "PrepayDBInstance",
     "DBInstanceId"
```

]

```json
   }
  },
  "InnerIPAddress": {
   "Description": "IP Address for created DB instance of Intranet.",
   "Value": {
    "Fn::GetAtt": [
     "PrepayDBInstance",
     "InnerIPAddress"
```

]

```json
   }
  },
  "PublicConnectionString": {
   "Description": "DB instance connection url by Internet.",
   "Value": {
    "Fn::GetAtt": [
     "PrepayDBInstance",
     "PublicConnectionString"
```

]

```json
   }
  },
  "PublicIPAddress": {
   "Description": "IP Address for created DB instance of Internet.",
   "Value": {
    "Fn::GetAtt": [
     "PrepayDBInstance",
     "PublicIPAddress"
```

]

```json
   }
  },
  "OrderId": {
   "Description": "The order id list of created instance.",
   "Value": {
    "Fn::GetAtt": [
     "PrepayDBInstance",
     "OrderId"
```

]

```json
   }
  },
  "PublicPort": {
   "Description": "Internet port of created DB instance.",
   "Value": {
    "Fn::GetAtt": [
     "PrepayDBInstance",
     "PublicPort"
```

]

```json
   }
  },
  "InnerPort": {
   "Description": "Intranet port of created DB instance.",
   "Value": {
    "Fn::GetAtt": [
     "PrepayDBInstance",
     "InnerPort"
```

]

```
   }
}
```

资源编排

```
  }
 }
}
```

`YAML` 格式

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
 AllocatePublicConnection:
  AllowedValues:
  - 'True'
  - 'true'
  - 'False'
  - 'false'
  Description: If true, allocate public connection automate.
  Type: Boolean
 ArchiveBackupKeepCount:
  Description: "The number of archived backups that can be retained. Default value:\
   \ 1. Valid values: \nThe value of this parameter ranges from 1 to 31 when the\
   \ ArchiveBackupKeepPolicy \n parameter is set to ByMonth. \nThe value of this\
   \ parameter ranges from 1 to 7 when the ArchiveBackupKeepPolicy \n parameter\
   \ is set to ByWeek. \nNote You do not need to specify this parameter when the\
   \ ArchiveBackupKeepPolicy \nparameter is set to KeepAll."
  MaxValue: 31
  MinValue: 1
  Type: Number
 ArchiveBackupKeepPolicy:
  AllowedValues:
  - ByMonth
  - ByWeek
  - KeepAll
  Description: "The period for which to retain archived backups. The number of archived\
   \ backups that can \n be retained within the specified period is determined\
   \ by the ArchiveBackupKeepCount parameter. \n Default value: 0. Valid values:\
   \ \nByMonth \n ByWeek \n KeepAll"
  Type: String
 ArchiveBackupRetentionPeriod:
  Description: "The number of days for which to retain archived backups. \n The\
   \ default value 0 specifies not to enable the backup archiving function. Valid\
   \ values: 30 to 1095."
  MaxValue: 1095
  MinValue: 30
  Type: Number
 AutoPay:
  AllowedValues:
  - 'True'
  - 'true'
  - 'False'
  - 'false'
  Default: false
  Description: Automatic Payment. Default is false.
  Type: Boolean
 AutoRenew:
  AllowedValues:
  - 'True'
  - 'true'
  - 'False'
  - 'false'
  Default: false
  Description: Auto renew the prepay instance. If the period type is by year, it
   will renew by year, else it will renew by month.
  Type: Boolean
BackUpCategory:
```

资源编排

```
 BackUpCategory:
  AllowedValues:
  - Flash
  - Standard
  Description: "Specifies whether to enable the second-level backup function. This\
   \ function allows a backup \nto be completed within seconds. Valid values: \n\
   Flash: specifies to enable the second-level backup function. \n Standard: specifies\
   \ to disable the second-level backup function."
  Type: String
 BackupPolicyMode:
  AllowedValues:
  - DataBackupPolicy
  - LogBackupPolicy
  Description: "Backup type, \nDataBackupPolicy: data backup \nLogBackupPolicy:\
   \ log backup"
  Type: String
 BackupRetentionPeriod:
  Default: 7
  Description: 'The retention period of the data backup. Value range: 7 to 730.
   The default value is the original value. Note When the BackupPolicyMode parameter
   is set to LogBackupPolicy, this parameter is required.'
  Type: Number
 Category:
  AllowedValues:
  - Basic
  - HighAvailability
  - AlwaysOn
  - Finance
  Description: 'The edition of the instance. Valid values:
   Basic: specifies to use the Basic Edition.
   HighAvailability: specifies to use the High-availability Edition.
   AlwaysOn: specifies to use the Cluster Edition.
   Finance: specifies to use the Enterprise Edition.'
  Type: String
 CommodityCode:
  AllowedValues:
  - rds
  - bards
  - rords
  Default: rds
  Description: The CommodityCode of the order.
  Type: String
 CompressType:
  Description: "The format used to compress backups. Valid values: \n 1: The zlib\
   \ tool is used to compress backups into .tar.gz files. \n 4: The QuickLZ tool\
   \ is used to compress backups into .xb.gz files. \nThis compression format is\
   \ supported only when the instance runs MySQL 5.6 or 5.7. \nIt can be used to\
   \ restore individual databases and tables. \n 8: The QuickLZ tool is used to\
   \ compress backups into .xb.gz files. \n This compression format is supported\
   \ only when the instance runs MySQL 8.0. \nIt cannot be used to restore individual\
   \ databases or tables."
  Type: Number
 ConnectionMode:
  Description: 'Connection Mode for database instance,support ''Standard'' and ''Safe''
   mode. Default is RDS system assigns. '
  Type: String
 ConnectionStringPrefix:
  AllowedPattern: '[a-zA-Z0-9-]{8,64}'
  Description: "The prefix of the endpoint. \nOnly the prefix of the CurrentConnectionString\
```

资源编排

```
   \ parameter value can be modified.\nThe prefix must be 8 to 64 characters in\
   \ length and can contain letters, digits, and hyphens (-). "
  Type: String
 ConnectionStringType:
  AllowedValues:
  - Inner
  - Public
  Default: Inner
  Description: 'The endpoint type of the instance, allow values: Inner, Public'
  Type: String
 CouponCode:
  Description: The coupon code of the order.
  Type: String
 DBInstanceClass:
  Description: Database instance type. Refer the RDS database instance type reference,
   such as 'rds.mys2.large', 'rds.mss1.large', 'rds.pg.s1.small' etc
  Type: String
 DBInstanceDescription:
  Description: Description of created database instance.
  Type: String
 DBInstanceNetType:
  AllowedValues:
  - Internet
  - Intranet
  Default: Intranet
  Description: Database instance net type, default is Intranet.Internet for public
   access, Intranet for private access.
  Type: String
 DBInstanceStorage:
  Description: Database instance storage size. mysql is [5,1000]. sql server 2008r2
   is [10,1000], sql server 2012/2012_web/2016-web is [20,1000]. PostgreSQL and
   PPAS is [5,2000]. Increased every 5 GB, Unit in GB
  Type: Number
 DBInstanceStorageType:
  Description: 'The storage type of the instance. Valid values:
   local_ssd: specifies to use local SSDs. This is the recommended storage type.
   cloud_ssd: specifies to use standard SSDs.
   cloud_essd: specifies to use enhanced SSDs.'
  Type: String
 DBIsIgnoreCase:
  Description: 'Specifies whether table names are case-sensitive. Valid values:
   1: Table names are not case-sensitive. This is the default value.
   0: Table names are case-sensitive.'
  Type: Number
 DBMappings:
  Description: Database mappings to attach to db instance.
  Type: Json
 DBParamGroupId:
  Description: The ID of the parameter template used by the instance.
  Type: String
 DBTimeZone:
  Description: 'The UTC time zone of the instance. Valid values: -12:00 to +12:00.
   The time zone must be an integer value such as +08:00. Values such as +08:30
   are not allowed.'
  Type: String
 DedicatedHostGroupId:
  Description: The ID of the host group to which the instance belongs if you create
aninstanceinahostgrop
```

资源编排

```
   an instance in a host group.
  Type: String
 EnableBackupLog:
  AllowedValues:
  - 'True'
  - 'true'
  - 'False'
  - 'false'
  Description: "Specifies whether to enable the log backup function. Valid values:\
   \ \nTrue: specifies to enable the log backup function. \nFalse: specifies to\
   \ disable the log backup function. \nNote You must specify this parameter when\
   \ the BackupPolicyMode parameter is set to LogBackupPolicy."
  Type: Boolean
 EncryptionKey:
  Description: The ID of the encryption key that is used to encrypt data on SSDs
   in the region. You can view the encryption key ID in the Key Management Service
   (KMS) console. You can also create an encryption key.
  Type: String
 Engine:
  AllowedValues:
  - MySQL
  - SQLServer
  - PostgreSQL
  - PPAS
  - MariaDB
  Description: Database instance engine type. Support MySQL/SQLServer/PostgreSQL/PPAS/MariaDB
   now.
  Type: String
 EngineVersion:
  Description: 'Database instance version of the relative engine type.Support MySQL:
   5.5/5.6/5.7/8.0;
   SQLServer:
2008r2/2012/2012_ent_ha/2012_std_ha/2012_web/2016_ent_ha/2016_std_ha/2016_web/2017_std_ha/2017_ent;
   PostgreSQL: 9.4/10.0/11.0/12.0;
   PPAS: 9.3/10.0;
   MariaDB: 10.3.'
  Type: String
 HighSpaceUsageProtection:
  AllowedValues:
  - Disable
  Description: "Specifies whether to forcibly delete log backup files when the space\
   \ usage of the \n instance exceeds 80% or the remaining space is less than 5\
   \ GB. Valid values: \n Enable and Disable. You can retain the default value.\
   \ Note You must specify \n this parameter when the BackupPolicyMode parameter\
   \ is set to LogBackupPolicy."
  Type: String
 LocalLogRetentionHours:
  Description: "The number of hours for which to retain log backup files on the\
   \ instance. \nValid values: 0 to 168. The value 0 specifies not to retain log\
   \ backup files on the instance. \nYou can retain the default value. Note You\
   \ must specify this parameter when the BackupPolicyMode \nparameter is set to\
   \ LogBackupPolicy."
  MaxValue: 168
  MinValue: 0
  Type: Number
 LocalLogRetentionSpace:
  Description: "The maximum percentage of space that is allowed to store log backup\
   \ files on the instance. \n If the space usage for log backup files exceeds\
```

资源编排

```
   \ this percentage, the system deletes earlier \n log backup files until the\
   \ space usage falls below this percentage. Valid values:0 to 50. \n You can\
   \ retain the default value. Note You must specify this parameter when the \n\
   \ BackupPolicyMode parameter is set to LogBackupPolicy."
  MaxValue: 50
  MinValue: 0
  Type: Number
 LogBackupFrequency:
  Description: "The frequency at which to back up logs. Valid values: \nThe value\
   \ LogInterval specifies to back up logs every 30 minutes. \n The default value\
   \ of this parameter is the same as the data backup frequency. \nNote The value\
   \ LogInterval is supported only when the instance runs SQL Server."
  Type: String
 LogBackupLocalRetentionNumber:
  Description: "The number of log backup files that can be retained on the instance.\
   \ \nDefault value: 60. Valid values: 6 to 100."
  MaxValue: 100
  MinValue: 6
  Type: Number
 LogBackupRetentionPeriod:
  Description: "The number of days for which to retain log backup files. Valid values:\
   \ 7 to 730. The log backup \n retention period cannot be longer than the data\
   \ backup retention period.Note If you enable the log \n backup function, you\
   \ can specify the log backup retention period. This applies only when the \n\
   \ instance runs MySQL, PostgreSQL, or PPAS."
  MaxValue: 730
  MinValue: 7
  Type: Number
 MaintainTime:
  Description: The period during which the maintenance performs. The format is HH:mmZ-HH:mmZ.
  Type: String
 MasterUserPassword:
  Description: 'The master password for the database instance. '
  MaxLength: 32
  MinLength: 8
  Type: String
 MasterUserType:
  AllowedValues:
  - Normal
  - Super
  - Sysadmin
  Default: Normal
  Description: "Privilege type of account.\n Normal: Common privilege. \n Super:\
   \ High privilege. \nSysadmin: Super privileges (SA) (only supported by SQL Server)\n\
   The default value is Normal."
  Type: String
 MasterUsername:
  Description: 'The master user name for the database instance. '
  Type: String
 MultiAZ:
  AllowedValues:
  - 'True'
  - 'true'
  - 'False'
  - 'false'
  Default: false
  Description: 'Specifies if the database instance is a multiple Availability Zone
   deployment. '
  Type: Boolean
 Period:
  Default: 1
  Description: Prepaid time period. While choose by pay by month, it could be from
```

资源编排

```
   1 to 9. While choose pay by year, it could be from 1 to 3.
  MaxValue: 9
  MinValue: 1
  Type: Number
 PeriodType:
  AllowedValues:
  - Month
  - Year
  Default: Month
  Description: Charge period for created instances.
  Type: String
 Port:
  Description: The port of the database service.
  MaxValue: 65535
  MinValue: 1
  Type: Number
 PreferredBackupPeriod:
  Description: The backup period. Separate multiple values with commas (,). The
   default value is the original value. Valid values:Monday Tuesday Wednesday Thursday
   Friday Saturday Sunday Note When the BackupPolicyMode parameter is set to DataBackupPolicy,
   this parameter is required.
  Type: CommaDelimitedList
 PreferredBackupTime:
  Description: 'The time when the backup task is performed. Format: yyyy-MM-ddZ-HH:mm:ssZ.Note
   When the BackupPolicyMode parameter is set to DataBackupPolicy, this parameter
   is required.'
  Type: String
 PrivateIpAddress:
  Description: The private ip for created instance.
  Type: String
 Quantity:
  Default: 1
  Description: The number of instance to be created, default is 1, max number is
  MaxValue: 99
  MinValue: 1
  Type: Number
 ReleasedKeepPolicy:
  AllowedValues:
  - Lastest
  - All
  Description: "The policy used to retain archived backups if the instance is released.\
   \ Default value: None. \n Valid values: \nLastest: Only the last archived backup\
   \ is retained. \n All: All of the archived backups are retained."
  Type: String
 ResourceGroupId:
  Description: Resource group id.
  Type: String
 RoleARN:
  Description: The Alibaba Cloud Resource Name (ARN) provided to the service account
   of the instance by your Alibaba Cloud account to connect to KMS. You can copy
   the ARN from the RAM console.
  Type: String
 SQLCollectorStatus:
  AllowedValues:
  - Disabled
  Description: "Specifies whether to enable or disable the SQL Explorer (SQL audit)\
   \ feature. \nValid values:Enable | Disabled."
  Type: String
 SSLSetting:
  AllowedValues:
-Disabled
```

资源编排

```
sabed
  - EnabledForPublicConnection
  - EnabledForInnerConnection
  Default: Disabled
  Description: 'Secure Sockets Layer (SSL) link setting of the instance. Valid values:
   Disabled: Disable SSL
   EnabledForPublicConnection: Public connection address will be protected by the
   SSL certificate. It requires AllocatePublicConnection is true.
   EnabledForInnerConnection: Private connection address will be protected by the
   SSL certificate.
   Default value is Disabled.'
  Type: String
 SecurityGroupId:
  Description: "The ID of the ECS security groups. \nEach RDS instance can be associated\
   \ with up to three ECS security groups. \nYou must separate them with commas\
   \ (,). \nTo delete an ECS Security group, leave this parameter empty. \n"
  Type: String
 SlaveZoneIds:
  Description: List of slave zone ids can specify slave zone ids when creating the
   high-availability or enterprise edition instance. Meanwhile, VSwitchId needs
   to pass in the corresponding vswitch id to the slave zone by order. For example,
   ZoneId = "zone-a" and SlaveZoneIds = ["zone-c", "zone-b"], then the VSwitchId
   must be "vsw-zone-a,vsw-zone-c,vsw-zone-b". Of course, you can also choose automatic
   allocation, for example, ZoneId = "zone-a" and SlaveZoneIds = ["Auto", "Auto"],
   then the VSwitchId must be "vsw-zone-a,Auto,Auto". The list contains up to 2
   slave zone ids, separated by commas.
  MaxLength: 2
  Type: Json
 Tags:
  Description: 'The tags of an instance.
   You should input the information of the tag with the format of the Key-Value,
   such as {"key1":"value1","key2":"value2", ... "key5":"value5"}.
   At most 5 tags can be specified.
   Key
   It can be up to 64 characters in length.
   Cannot begin with aliyun.
   Cannot begin with http:// or https://.
   Cannot be a null string.
   Value
   It can be up to 128 characters in length.
   Cannot begin with aliyun.
   Cannot begin with http:// or https://.
   Can be a null string.'
  Type: Json
 TargetDedicatedHostIdForLog:
  Description: The ID of the host to which the instance belongs if you create a
   log instance in a host group.
```

资源编排

```
  Type: String
 TargetDedicatedHostIdForMaster:
  Description: The ID of the host to which the instance belongs if you create a
   primary instance in a host group.
  Type: String
 TargetDedicatedHostIdForSlave:
  Description: The ID of the host to which the instance belongs if you create a
   secondary instance in a host group.
  Type: String
 VSwitchId:
  Description: The vSwitch id of created instance. For VPC network, the property
   is required.
  Type: String
 VpcId:
  Description: The VPC id of created database instance. For VPC network, the property
   is required.
  Type: String
 ZoneId:
  Description: selected zone to create database instance. You cannot set the ZoneId
   parameter if the MultiAZ parameter is set to true.
  Type: String
Resources:
 PrepayDBInstance:
  Properties:
   AllocatePublicConnection:
    Ref: AllocatePublicConnection
   ArchiveBackupKeepCount:
    Ref: ArchiveBackupKeepCount
   ArchiveBackupKeepPolicy:
    Ref: ArchiveBackupKeepPolicy
   ArchiveBackupRetentionPeriod:
    Ref: ArchiveBackupRetentionPeriod
   AutoPay:
    Ref: AutoPay
   AutoRenew:
    Ref: AutoRenew
   BackUpCategory:
    Ref: BackUpCategory
   BackupPolicyMode:
    Ref: BackupPolicyMode
   BackupRetentionPeriod:
    Ref: BackupRetentionPeriod
   Category:
    Ref: Category
   CommodityCode:
    Ref: CommodityCode
   CompressType:
    Ref: CompressType
   ConnectionMode:
    Ref: ConnectionMode
   ConnectionStringPrefix:
    Ref: ConnectionStringPrefix
   ConnectionStringType:
    Ref: ConnectionStringType
   CouponCode:
    Ref: CouponCode
   DBInstanceClass:
    Ref: DBInstanceClass
   DBInstanceDescription:
    Ref: DBInstanceDescription
   DBInstanceNetType:
    Ref: DBInstanceNetType
DBInstanceStorage:
```

资源编排

```
   DBInstanceStorage:
    Ref: DBInstanceStorage
   DBInstanceStorageType:
    Ref: DBInstanceStorageType
   DBIsIgnoreCase:
    Ref: DBIsIgnoreCase
   DBMappings:
    Ref: DBMappings
   DBParamGroupId:
    Ref: DBParamGroupId
   DBTimeZone:
    Ref: DBTimeZone
   DedicatedHostGroupId:
    Ref: DedicatedHostGroupId
   EnableBackupLog:
    Ref: EnableBackupLog
   EncryptionKey:
    Ref: EncryptionKey
   Engine:
    Ref: Engine
   EngineVersion:
    Ref: EngineVersion
   HighSpaceUsageProtection:
    Ref: HighSpaceUsageProtection
   LocalLogRetentionHours:
    Ref: LocalLogRetentionHours
   LocalLogRetentionSpace:
    Ref: LocalLogRetentionSpace
   LogBackupFrequency:
    Ref: LogBackupFrequency
   LogBackupLocalRetentionNumber:
    Ref: LogBackupLocalRetentionNumber
   LogBackupRetentionPeriod:
    Ref: LogBackupRetentionPeriod
   MaintainTime:
    Ref: MaintainTime
   MasterUserPassword:
    Ref: MasterUserPassword
   MasterUserType:
    Ref: MasterUserType
   MasterUsername:
    Ref: MasterUsername
   MultiAZ:
    Ref: MultiAZ
   Period:
    Ref: Period
   PeriodType:
    Ref: PeriodType
   Port:
    Ref: Port
   PreferredBackupPeriod:
    Ref: PreferredBackupPeriod
   PreferredBackupTime:
    Ref: PreferredBackupTime
   PrivateIpAddress:
    Ref: PrivateIpAddress
   Quantity:
    Ref: Quantity
   ReleasedKeepPolicy:
    Ref: ReleasedKeepPolicy
   ResourceGroupId:
    Ref: ResourceGroupId
   RoleARN:
```

资源编排

```
    Ref: RoleARN
   SQLCollectorStatus:
    Ref: SQLCollectorStatus
   SSLSetting:
    Ref: SSLSetting
   SecurityGroupId:
    Ref: SecurityGroupId
   SlaveZoneIds:
    Ref: SlaveZoneIds
   Tags:
    Ref: Tags
   TargetDedicatedHostIdForLog:
    Ref: TargetDedicatedHostIdForLog
   TargetDedicatedHostIdForMaster:
    Ref: TargetDedicatedHostIdForMaster
   TargetDedicatedHostIdForSlave:
    Ref: TargetDedicatedHostIdForSlave
   VSwitchId:
    Ref: VSwitchId
   VpcId:
    Ref: VpcId
   ZoneId:
    Ref: ZoneId
Outputs:
 DBInstanceId:
  Description: The instance id of created database instance.
  Value:
   Fn::GetAtt:
   - DBInstanceId
 InnerConnectionString:
  Description: DB instance connection url by Intranet.
  Value:
   Fn::GetAtt:
   - InnerConnectionString
 InnerIPAddress:
  Description: IP Address for created DB instance of Intranet.
  Value:
   Fn::GetAtt:
   - InnerIPAddress
 InnerPort:
  Description: Intranet port of created DB instance.
  Value:
   Fn::GetAtt:
   - InnerPort
 OrderId:
  Description: The order id list of created instance.
  Value:
   Fn::GetAtt:
   - OrderId
 PublicConnectionString:
  Description: DB instance connection url by Internet.
  Value:
   Fn::GetAtt:
   - PublicConnectionString
 PublicIPAddress:
Description IPAddressforcreatedDBinstanceofInternet
```

资源编排

```
  Description: IP Address for created DB instance of Internet.
  Value:
   Fn::GetAtt:
   - PublicIPAddress
 PublicPort:
  Description: Internet port of created DB instance.
  Value:
   Fn::GetAtt:
   - PublicPort
```

### Redis

#### ALIYUN::REDIS::Instance

**语法**

```json
 {
  "Type": "ALIYUN::REDIS::Instance",
  "Properties": {
    "VpcId": String,
    "EvictionPolicy": String,
    "BackupPolicy": Map,
    "ZoneId": String,
    "InstanceClass": String,
    "InstanceMaintainTime": Map,
    "Tags": List,
    "VpcPasswordFree": Boolean,
    "VSwitchId": String,
    "SecurityGroupId": String,
    "EngineVersion": String,
    "SSLEnabled": String,
    "Password": String,
    "InstanceName": String,
    "DeletionForce": Boolean,
    "Connections": Map,
    "ChargeType": String,
    "Period": Integer,
    "AutoRenewDuration": Integer,
    "ProductType": String
    "SecondaryZoneId": String,
    "ResourceGroupId": String,
    "PeriodUnit": String,
    "TairConfig": Map,
    "ShardCount": Integer,
    "NodeType": String,
    "DeletionProtection": Boolean
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|

资源编排

| EngineVersio n | String | 否 | 否 | 数据库版本。 | 取值： 2.8 说明已停售，请选择其他版本。 4.0 5.0 |
|---|---|---|---|---|---|
| InstanceClass | String | 否 | 是 | 实例规格。 | 更多信息，请参见实例规格概览。 |
| InstanceMaint ainTime | Map | 否 | 是 | 实例的可维护时间段。 | 无 |
| Tags | List | 否 | 是 | 标签。 | 每个实例最多可以绑定20个标签。 更多信息，请参见Tags属性。 |
| VpcPassword Free | Boolean | 否 | 否 | 是否启用免密码访问专有网络中的实例。 | 取值： true：启用。 false（默认值）：禁用。 |
| VpcId | String | 否 | 否 | 专有网络ID。 | 无 |
| EvictionPolicy | String | 否 | 否 | 数据逐出策略。 | 取值： noeviction：不删除任何key， 只是在写操作时返回错误。 allkeys-lru：优先删除掉最近最少使用的key。 volatile-lru：只从设置失效 （expire set）的key中选择最近最少使用的key进行删除。 allkeys-random：随机选择删除key。 volatile-random：只从设置失效（expire set）的key中，随机选择一些key进行删除。 volatile-ttl：只从设置失效 （expire set）的key中，选出存活时间（TTL）最短的key进行删除。 |
| ZoneId | String | 否 | 否 | 可用区ID。 | 当创建的实例属于专有网络时，该参数必须指定。 创建多可用区实例时，您可以调用查询支持的可用区接口查询支持的多可用区ID。 |
| VSwitchId | String | 否 | 否 | 专有网络下的交换机ID。 | 无 |
| SecurityGrou pId | String | 否 | 是 | 安全组ID。 | 最多支持设置10个ID，ID之间用半角逗号（,）分隔。 |

资源编排

| Password | String | 否 | 是 | 密码。 | 长度为8～30个字符，必须同时包含大写英文字母、小写英文字母和数字。 |
|---|---|---|---|---|---|
| SSLEnabled | String | 否 | 是 | SSL状态。 | 取值： Disable：关闭。 Enable：开启。 Update：更新证书。 |
| InstanceNam e | String | 否 | 是 | 实例名称。 | 长度为2~128个字符。必须以英文字母或汉字开头，可包含英文字母、数字、汉字、下划线（ ）、短 _ 划线（-）和半角句号（.）。 |
| DeletionForce | Boolean | 否 | 是 | 是否在回收时删除实例。 | 取值： true：回收时删除实例。 false（默认值）：回收时不删除实例。 |
| Connections | Map | 否 | 是 | 连接地址。 | 更多信息，请参见Connections属性。 |
| BackupPolicy | Map | 否 | 是 | 备份策略。 | 更多信息，请参见BackupPolicy属性。 |
| ChargeType | String | 否 | 否 | 实例付费类型。 | 取值： PostPaid（默认值）：后付费， 即按量付费。 PrePaid：预付费，即包年包月。 |
| Period | Integer | 否 | 否 | 付费周期。 | 取值：1~9、12、24、36、60。 单位：月。 |
| AutoRenewD uration | Integer | 否 | 是 | 自动续费时长。 | 取值范围：1~12。 单位：月。 当实例即将到期时，将根据该参数指定的时长自动续费。 说明当ChargeType取值为 PrePaid时该参数有效。 |

资源编排

| ProductType | String | 否 | 否 | 产品类型。 | 取值： Local：社区版实例（本地盘版） 或性能增强型（本地盘版）。 Tair rdb：性能增强型（云盘 _ 版）。 Tair scm：持久内存型。 _ Tair essd：容量存储型。 _ OnECS：社区版实例（云盘版）。 说明建议设置 ProductType 属性，能加快参数查询的速度。 |
|---|---|---|---|---|---|
| SecondaryZo neId | String | 否 | 是 | 备可用区ID。 | 可调用查询支持的可用区接口查询。 说明传入本参数可以实现主备数据节点分布在不同的可用区，实现跨可用区容灾，能够承受机房级别的故障。 |
| ResourceGro upId | String | 否 | 是 | 资源组ID。 | 无 |
| PeriodUnit | String | 否 | 否 | 时长单位。 | 取值： Year：年。 Month：月。 |
| TairConfig | Map | 否 | 否 | Tair配置。 | 更多信息，请参见TairConfig属性。 |
| ShardCount | Integer | 否 | 否 | 分片数。 | 本参数仅适用于创建云盘版集群架构实例，您可以通过该参数实现自定义分片数量。 |

资源编排

| NodeType | String | 否 | 否 | 节点类型。 | 取值： MASTER SLAVE：高可用 _ （双副本）。 STAND ALONE：单副本。 _ double：双副本。 single：单副本。 说明云原生版实例请选择MASTER SLAVE或STA _ ND ALONE，经典版实例请 _ 选择double或single。 |
|---|---|---|---|---|---|
| DeletionProte ction | Boolean | 否 | 是 | 是否已开启释放保护功能。 | 取值： true：已开启 false：未开启 |

**BackupPolicy语法**

```json
"BackupPolicy": {
  "PreferredBackupPeriod": "String",
  "PreferredBackupTime": "String",
  "EnableBackupLog": "Integer"
}
```

**BackupPolicy属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| PreferredBac kupPeriod | String | 是 | 是 | 备份周期。 | 取值： Monday：星期一。 Tuesday：星期二。 Wednesday：星期三。 Thursday：星期四。 Friday：星期五。 Saturday：星期六。 Sunday：星期日。 |
| PreferredBac kupTime | String | 是 | 是 | 备份时间。 | 格式： HH:mmZ-HH:mmZ 。 |
| EnableBacku pLog | Integer | 否 | 是 | 开启或关闭增量备份。 | 取值： 1：开启。 0（默认值）：关闭。 |

**InstanceMaintainTime语法**

资源编排

```json
"InstanceMaintainTime": {
  "MaintainStartTime": "String",
  "MaintainEndTime": "String"
}
```

**InstanceMaintainTime属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| MaintainStart Time | String | 否 | 否 | 可维护时间段的开始时间。 | 格式： HH:mmZ （UTC时间）。 例如：需要在北京时间凌晨1点开始，应设置为 17:00Z 。 |
| MaintainEndT ime | String | 否 | 否 | 可维护时间段的结束时间。 | 格式： HH:mmZ （UTC时间）。 例如：需要在北京时间凌晨2点结束，应设置为 18:00Z 。 说明开始时间和结束时间的间隔应为1小时，例如： MaintainStartTime 为 17:00Z ，MaintainEn dTime为 18:00Z 。 |

**Tags语法**

```json
"Tags": [
  {
    "Key": String,
    "Value": String
  }
```

]

**Tags属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Key | String | 是 | 否 | 标签键。 | 同账号同地域下标签键唯一。 |
| Value | String | 否 | 否 | 标签值。 | 无 |

**Connections语法**

```json
"Connections": {
  "VpcPrivateConnection": "Map",
  "ClassicInnerConnection": "Map",
  "DirectConnection": "Map",
  "PublicConnection": "Map"
}
```

**Connections属性**

资源编排

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| VpcPrivateCo nnection | Map | 否 | 是 | VPC内网地址。 | 更多信息，请参见VpcPrivateConnection属性。 |
| ClassicInnerC onnection | Map | 否 | 是 | 经典内网地址。 | 更多信息，请参见ClassicInnerConnection属性。 |
| DirectConnec tion | Map | 否 | 是 | 直接连接地址。 该实例是一个集群实例。您可以根据需要申请直接连接端点。 | 更多信息，请参见DirectConnection属性。 |
| PublicConnec tion | Map | 否 | 是 | 公共地址。 | 更多信息，请参见PublicConnection属性。 |

**VpcPrivateConnection语法**

```json
"VpcPrivateConnection": {
  "ConnectionPort": Integer,
  "ConnectionString": String
}
```

**VpcPrivateConnection属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ConnectionPo rt | Integer | 是 | 是 | 实例的 ApsaraDB服务端口号。 | 取值范围：1024~65535。 |
| ConnectionSt ring | String | 是 | 是 | 公共端点的前缀。 | 长度为8~64个字符，必须以小写英文字母开头。可包含小写英文字母和数字。 |

**PublicConnection语法**

```json
"PublicConnection": {
  "ConnectionPort": Integer,
  "ConnectionString": String
}
```

**PublicConnection属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ConnectionPo rt | Integer | 是 | 是 | 实例的 ApsaraDB服务端口号。 | 取值范围：1024~65535。 |

资源编排

| ConnectionSt ring | String | 是 | 是 | 公共端点的前缀。 | 长度为8~64个字符，必须以小写英文字母开头。可包含小写英文字母和数字。 |
|---|---|---|---|---|---|

**DirectConnection语法**

```json
"DirectConnection": {
  "ConnectionPort": Integer,
  "ConnectionString": String
}
```

**DirectConnection属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ConnectionPo rt | Integer | 是 | 是 | 实例的 ApsaraDB服务端口号。 | 取值范围：1024~65535。 |
| ConnectionSt ring | String | 是 | 是 | 公共端点的前缀。 | 长度为8~64个字符，必须以小写英文字母开头。可包含小写英文字母和数字。 |

**ClassicInnerConnection语法**

```json
"ClassicInnerConnection": {
  "ConnectionPort": Integer,
  "ConnectionString": String
}
```

**ClassicInnerConnection属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ConnectionPo rt | Integer | 是 | 是 | 实例的 ApsaraDB服务端口号。 | 取值范围：1024~65535。 |
| ConnectionSt ring | String | 是 | 是 | 公共端点的前缀。 | 长度为8~64个字符，必须以小写英文字母开头。可包含小写英文字母和数字。 |

**TairConfig语法**

```json
"TairConfig": {
  "Storage": "Integer",
  "StorageType": "String",
  "ShardCount": "Integer"
}
```

**TairConfig属性**

资源编排

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Storage | Integer | 否 | 否 | 云盘的存储空间。 | 不同的规格取值范围有所区别。更多信息，请参见磁盘型实例规格。 |
| StorageType | String | 否 | 否 | 存储类型。 | 取值： essd pl0 _ essd pl1 _ essd pl2 _ essd pl3 _ |
| ShardCount | Integer | 否 | 否 | 实例中的数据节点个数。 | 取值： 1：默认值，即表示创建的实例为标准架构，仅拥有1个数据节点。 2~32：传入该范围的值，即表示创建的实例为集群架构，拥有指定数量的数据节点。 |

**返回值**

Fn::GetAtt InstanceId：实例ID。 OrderId：实例订单ID。 ConnectionDomain：实例的私网连接地址。 InstanceName：实例名称。 InstanceClass：实例规格。 VpcId：专有网络ID。 Capacity：实例的存储容量。 InstanceType：实例的引擎版本。 ChargeType：实例的计费方式。 PackageType：计划类型。 Connections：实例支持的最大连接数。 ArchitectureType：架构类型。 NodeType：节点类型。 HasRenewChangeOrder：阿里云账号是否有待续订或扩容订单。 ResourceGroupId：资源组ID。 QPS：每秒访问次数，取值为当前规格实例的理论值。 ZoneId：实例所属的可用区ID。 Bandwidth：实例带宽。单位：Mbps。 EngineVersion：版本类型。 NetworkType：网络类型。 VSwitchId：交换机ID。 PrivateIp：实例的私网IP地址。 PublicConnectionString：实例的公共连接字符串。 VpcPrivateConnectionPort：VPC私有连接端口。 资源编排 ClassicInnerConnectionString：实例的经典内部连接字符串。 VpcPrivateConnectionString：实例的VPC私有连接字符串。 PublicConnectionPort：实例的公共连接端口。 DirectConnectionString：实例的直接连接字符串。 DirectConnectionPort：实例的直接连接端口。 ClassicInnerConnectionPort：实例的经典内连接端口。

**示例**

YAML JSON

```
ROSTemplateFormatVersion: '2015-09-01' Description: {} Parameters:
  VpcId:
    Type: String
  ZoneId:
    Type: String
    Description:
      en: Before you create an instance, confirm that the Availability Zone supports the
specifications of Redis resources.
    AssociationProperty: ALIYUN::ECS::Instance:ZoneId
    Label:
      en: Zone ID
```

`zh-cn:` 可用区

```
  VSwitchId:
    Type: String
    AssociationProperty: ALIYUN::ECS::VSwitch::VSwitchId
    AssociationPropertyMetadata:
      VpcId: ${VpcId}
      ZoneId: ${ZoneId}
Resources:
  RedisInstance:
    Properties:
      VpcId:
        Ref: VpcId
      VSwitchId:
        Ref: VSwitchId
      EvictionPolicy: noeviction
      ZoneId:
        Ref: ZoneId
      Password: Admin@123!
Outputs:
  InstanceId:
    Value:
      Fn::GetAtt:
        - InstanceId
```

更多示例，请参见创建云数据库 Tair（兼容 Redis）实例、设置Tair实例的IP白名单和创建有特定权限的账号的组合示例：YAML示例。

### ROS

资源编排

#### ALIYUN::ROS::WaitCondition

ALIYUN::ROS::WaitCondition类型用于创建处理UserData消息的实例。

**语法**

```json
{
  "Type": "ALIYUN::ROS::WaitCondition",
  "Properties": {
    "Count": Number,
    "Handle": String,
    "Timeout": Number,
    "ShowProgressEvent": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Handle | String | 是 | 否 | 引用 ALIYUN::ROS: :WaitConditio nHandle创建的实例 | 无 |
| Timeout | Number | 是 | 否 | 接收UserData 消息的超时时间 | 取值范围：1~43,200。 单位：秒。 |
| Count | Number | 否 | 是 | 接收UserData 消息的总数 | 无 |
| ShowProgress Event | String | 否 | 否 | 是否显示接收 UserData消息的进度事件 | 取值： EnabledIfCreateStack：在创建资源栈时显示进度事件。 Disabled：不显示进度事件。 |

**返回值**

Fn::GetAtt Data：JSON格式字符串，最近一次创建或更新后的信号数据。 JoinedErrorData：字符串，ErrorData信号内容的拼接。 ErrorData：JSON格式字符串，最近一次创建或更新后的错误信号数据。

**示例**

`JSON` 格式

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "ShowProgressEvent": {
      "Type": "String",
      "Description": "Whether to generate progress changed event. Default to Disabled.",
      "AllowedValues": [
        "EnabledIfCreateStack",
        "Disabled"
```

]

```json
    },
    "Timeout": {
      "Type": "Number",
      "Description": "The number of seconds to wait for the correct number of signals to arrive.",
```

资源编排

```json
      "MinValue": 1,
      "MaxValue": 43200
    },
    "Count": {
      "Type": "Number",
      "Description": "The number of success signals that must be received before the stack creation p
rocess continues.",
      "Default": 1
    },
    "Handle": {
      "Type": "String",
      "Description": "A reference to the wait condition handle used to signal this wait condition."
    }
  },
  "Resources": {
    "WaitCondition": {
      "Type": "ALIYUN::ROS::WaitCondition",
      "Properties": {
        "ShowProgressEvent": {
          "Ref": "ShowProgressEvent"
        },
        "Timeout": {
          "Ref": "Timeout"
        },
        "Count": {
          "Ref": "Count"
        },
        "Handle": {
          "Ref": "Handle"
        }
      }
    }
  },
  "Outputs": {
    "LastErrorData": {
      "Description": "JSON serialized dict containing data associated with wait condition error
signals sent to the handle backup by update last time.",
      "Value": {
        "Fn::GetAtt": [
          "WaitCondition",
          "LastErrorData"
```

]

```json
      }
    },
    "JoinedLastErrorData": {
      "Description": "String containing data associated with wait condition error signals sent to the
handle backup by update last time.",
      "Value": {
        "Fn::GetAtt": [
          "WaitCondition",
          "JoinedLastErrorData"
```

]

```json
      }
    },
    "LastData": {
      "Description": "JSON serialized dict containing data associated with wait condition signals
sent to the handle backup by update last time.",
      "Value": {
        "Fn::GetAtt": [
          "WaitCondition",
          "LastData"
```

]

```
}
```

资源编排

```json
      }
    },
    "JoinedErrorData": {
      "Description": "String containing data associated with wait condition error signals sent to the
handle.",
      "Value": {
        "Fn::GetAtt": [
          "WaitCondition",
          "JoinedErrorData"
```

]

```json
      }
    },
    "Data": {
      "Description": "JSON serialized dict containing data associated with wait condition signals
sent to the handle.",
      "Value": {
        "Fn::GetAtt": [
          "WaitCondition",
          "Data"
```

]

```json
      }
    },
    "ErrorData": {
      "Description": "JSON serialized dict containing data associated with wait condition error
signals sent to the handle.",
      "Value": {
        "Fn::GetAtt": [
          "WaitCondition",
          "ErrorData"
```

]

```
      }
    }
  }
}
```

`YAML` 格式

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  Count:
    Default: 1
    Description: The number of success signals that must be received before the stack
      creation process continues.
    Type: Number
  Handle:
    Description: A reference to the wait condition handle used to signal this wait
      condition.
    Type: String
  ShowProgressEvent:
    AllowedValues:
    - EnabledIfCreateStack
    - Disabled
    Description: Whether to generate progress changed event. Default to Disabled.
    Type: String
  Timeout:
    Description: The number of seconds to wait for the correct number of signals to
      arrive.
    MaxValue: 43200
    MinValue: 1
    Type: Number
Resources:
  WaitCondition:
Properties:
```

资源编排

```
    Properties:
      Count:
        Ref: Count
      Handle:
        Ref: Handle
      ShowProgressEvent:
        Ref: ShowProgressEvent
      Timeout:
        Ref: Timeout
Outputs:
  Data:
    Description: JSON serialized dict containing data associated with wait condition
      signals sent to the handle.
    Value:
      Fn::GetAtt:
      - Data
  ErrorData:
    Description: JSON serialized dict containing data associated with wait condition
      error signals sent to the handle.
    Value:
      Fn::GetAtt:
      - ErrorData
  JoinedErrorData:
    Description: String containing data associated with wait condition error signals
      sent to the handle.
    Value:
      Fn::GetAtt:
      - JoinedErrorData
  JoinedLastErrorData:
    Description: String containing data associated with wait condition error signals
      sent to the handle backup by update last time.
    Value:
      Fn::GetAtt:
      - JoinedLastErrorData
  LastData:
    Description: JSON serialized dict containing data associated with wait condition
      signals sent to the handle backup by update last time.
    Value:
      Fn::GetAtt:
      - LastData
  LastErrorData:
    Description: JSON serialized dict containing data associated with wait condition
      error signals sent to the handle backup by update last time.
    Value:
      Fn::GetAtt:
      - LastErrorData
```

#### ALIYUN::ROS::WaitConditionHandle

ALIYUN::ROS::WaitConditionHandle用于创建在自定义数据执行过程中发送信号和接收信号的实例。

**使用说明**

本文仅适用于资源栈更新场景，用于控制旧信号的删除。 资源编排

**语法**

```json
{
  "Type": "ALIYUN::ROS::WaitConditionHandle",
  "Properties": {
    "Count": Integer,
    "Mode": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Count | Integer | 否 | 是 | 准备接收的信号总数。 | 默认值为-1，表示该属性未生效。 当满足以下3个条件时，该属性生效： Mode取值为Full。 Count≥0。 信息通知成功，且未显示指定信号ID。 如果该属性生效，则信号ID为整数，从1开始递增。 例如：第一个信号ID为1，第二个信号ID为2，依次类推。 如果该属性生效，且存在非整数ID，则资源栈更新失败。 如果该属性生效，则ID>Count的旧信号将在更新前删除。 说明在需要通过更新资源栈进行弹性扩容或缩容的场景下，推荐与 ALIYUN::ROS::WaitConditio n的Count属性取值相同。 |
| Mode | String | 否 | 是 | 模式。 | 取值： Increment：所有旧信号将在更新前被删除。 说明更新过程中 ALIYUN::ROS::WaitCondi tion等待的信号数量 = ALIYUN::ROS::WaitCondi tion的Count属性的取值。 Full（默认值）：如果Count属性生效，会对旧信号进行删除。 说明更新过程中 ALIYUN::ROS::WaitCondi tion等待的信号数量 = ALIYUN::ROS::WaitCondi tion的Count属性取值 - 删除操作后剩余的旧信号的数量。 |

**返回值**

Fn::GetAtt CurlCli：该资源产生的curl命令。通过该命令发送自定义数据执行的结果或者状态到资源编排服务。 WindowsCurlCli：为Windows提供curl CLI命令前缀，可用于发送处理完成或失败的信号。由于Windows不支持curl命资源编排令，您需要先安装curl.exe并将其添加到PATH中。您可以通过添加 --data-binary "{\"status\": \" SUCCESS \"} 表示成功、添加 --data-binary "{\"status\": \" FAILURE \"} 表示失败。 PowerShellCurlCli：为PowerShell提供curl CLI命令前缀，可用于发送处理完成或失败的信号。由于此cmdlet是在

| 过 | $PSVersionTable.PSVersion |  |
|---|---|---|
| '{"status": " FAILURE "} |  | 表示 |

Headers：HTTP POST请求头，可用于发送处理完成或失败的信号。 URL：HTTP POST请求地址，可用于发送处理完成或失败的信号。

**说明**

CurlCli、WindowsCurlCli、PowerShellCurlCli的请求体中均可通过ID字段（字符串）信号明确指定信号ID。

```
例如： --data-binary "{\"status\": \" SUCCESS \", \"id\": \"test\"} 。
```

相同ID的信号会被当作同一信号，后面收到的信号会覆盖前面收到的。 如果没有指定ID，ROS会使用整数作为信号ID，这个整数=已有信号的数量+1。 通过 `status` 可以指定信号类型，包括 `SUCCESS` 、 `FAILURE` 、 `WARNING` 。 如果收到 `FAILURE` 信号，则资源栈操作失败。 如果在设定时间内，收到的信号数量未满足要求，则资源栈操作超时失败。 如果收到的信号数量满足了要求，且所有信号均为 `WARNING` ，则资源栈操作失败。 其他情况下，资源栈操作成功。

**示例**

`JSON` 格式

```json
{
 "ROSTemplateFormatVersion": "2015-09-01",
 "Parameters": {
  "Mode": {
   "Type": "String",
   "Description": "If set to Increment, all old signals will be deleted before update. In this mode,
WaitCondition.Count should reference an incremental value instead of a full value, such as ScalingGroupEnable.ScalingRuleArisExecuteResultNumberOfAddedInstances.\n\nIf set to Full, no old sign al will be deleted unless Count is set. In this mode, WaitCondition.Count should reference a full val ue, such as the same value with InstanceGroup.MaxAmount. It is recommended to use this mode with Coun t.\n\nDefault to Full.",
   "AllowedValues": [
    "Increment",
    "Full"
```

`],`

```json
   "Default": "Full"
  },
  "Count": {
   "Type": "Number",
   "Description": "There are 3 preconditions that make Count taking effect:\n1.Mode is set to Full.\n
2.Count >= 0.\n3.The id of signal is not specified. If so, it will be a self-increasing integer start ed from 1. For example, the id of the first signal is 1, the id of the second signal is 2, and so on. \n\nIf Count takes effect, signals with id > Count will be deleted before update.\nThe default value is -1, which means no effect.\nIt is recommended to quote the same value with WaitCondition.Count.",
   "Default": -1
  }
 },
 "Resources": {
  "WaitConditionHandle": {
   "Type": "ALIYUN::ROS::WaitConditionHandle",
   "Properties": {
    "Mode": {
     "Ref": "Mode"
    },
```

资源编排

```json
    "Count": {
     "Ref": "Count"
    }
   }
  }
 },
 "Outputs": {
  "CurlCli": {
   "Description": "Convenience attribute, provides curl CLI command prefix, which can be used for sig
nalling handle completion or failure. You can signal success by adding --data-binary '{\"status\": \" SUCCESS\"}' , or signal failure by adding --data-binary '{\"status\": \"FAILURE\"}'",
   "Value": {
    "Fn::GetAtt": [
     "WaitConditionHandle",
     "CurlCli"
```

]

```json
   }
  },
  "WindowsCurlCli": {
   "Description": "Convenience attribute, provides curl CLI command prefix for Windows, which can be
used for signalling handle completion or failure. As Windows does not support curl command, you need to install curl.exe and add it to PATH first. You can signal success by adding --data-binary \"{\\\"s tatus\\\": \\\"SUCCESS\\\"}\" , or signal failure by adding --data-binary \"{\\\"status\\\": \\\"FAILURE\\\"}\" ",
   "Value": {
    "Fn::GetAtt": [
     "WaitConditionHandle",
     "WindowsCurlCli"
```

]

```json
   }
  },
  "Headers": {
   "Description": "HTTP POST Headers used for signalling handle completion or failure.",
   "Value": {
    "Fn::GetAtt": [
     "WaitConditionHandle",
     "Headers"
```

]

```json
   }
  },
  "URL": {
   "Description": "HTTP POST URL used for signalling handle completion or failure.",
   "Value": {
    "Fn::GetAtt": [
     "WaitConditionHandle",
     "URL"
```

]

```json
   }
  },
  "PowerShellCurlCli": {
   "Description": "Convenience attribute, provides curl CLI command prefix for PowerShell, which can
be used for signalling handle completion or failure. As this cmdlet was introduced in PowerShell 3.0, ensure the version of PowerShell satisfies the constraint. (Show the version via $PSVersionTable.PSVersion.) You can signal success by adding -Body '{\"status\": \"SUCCESS\"}' , or s ignal failure by adding -Body '{\"status\": \"FAILURE\"}' ",
   "Value": {
    "Fn::GetAtt": [
     "WaitConditionHandle",
     "PowerShellCurlCli"
```

]

```
   }
  }
}
```

资源编排

```
 }
}
```

`YAML` 格式

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
 Mode:
  Type: String
  Description: >-
   If set to Increment, all old signals will be deleted before update. In
   this mode, WaitCondition.Count should reference an incremental value
   instead of a full value, such as
   ScalingGroupEnable.ScalingRuleArisExecuteResultNumberOfAddedInstances.
   If set to Full, no old signal will be deleted unless Count is set. In this
   mode, WaitCondition.Count should reference a full value, such as the same
   value with InstanceGroup.MaxAmount. It is recommended to use this mode
   with Count.
   Default to Full.
  AllowedValues:
   - Increment
   - Full
  Default: Full
 Count:
  Type: Number
  Description: >-
   There are 3 preconditions that make Count taking effect:
   1.Mode is set to Full.
   2.Count >= 0.
   3.The id of signal is not specified. If so, it will be a self-increasing
   integer started from 1. For example, the id of the first signal is 1, the
   id of the second signal is 2, and so on.
   If Count takes effect, signals with id > Count will be deleted before
   update.
   The default value is -1, which means no effect.
   It is recommended to quote the same value with WaitCondition.Count.
  Default: -1
Resources:
 WaitConditionHandle:
  Properties:
   Mode:
    Ref: Mode
   Count:
    Ref: Count
Outputs:
 CurlCli:
  Description: >-
   Convenience attribute, provides curl CLI command prefix, which can be used
   for signalling handle completion or failure. You can signal success by
   adding --data-binary '{"status": "SUCCESS"}' , or signal failure by adding
--data-binary'{"status":"FAILURE"}'
```

资源编排

```
databinary {status: FAILURE}
  Value:
   'Fn::GetAtt':
    - CurlCli
 WindowsCurlCli:
  Description: >-
   Convenience attribute, provides curl CLI command prefix for Windows, which
   can be used for signalling handle completion or failure. As Windows does
   not support curl command, you need to install curl.exe and add it to PATH
   first. You can signal success by adding --data-binary "{\"status\":
   \"SUCCESS\"}" , or signal failure by adding --data-binary "{\"status\":
   \"FAILURE\"}"
  Value:
   'Fn::GetAtt':
    - WindowsCurlCli
 Headers:
  Description: HTTP POST Headers used for signalling handle completion or failure.
  Value:
   'Fn::GetAtt':
    - Headers
 URL:
  Description: HTTP POST URL used for signalling handle completion or failure.
  Value:
   'Fn::GetAtt':
    - URL
 PowerShellCurlCli:
  Description: >-
   Convenience attribute, provides curl CLI command prefix for PowerShell,
   which can be used for signalling handle completion or failure. As this
   cmdlet was introduced in PowerShell 3.0, ensure the version of PowerShell
   satisfies the constraint. (Show the version via
   $PSVersionTable.PSVersion.) You can signal success by adding -Body
   '{"status": "SUCCESS"}' , or signal failure by adding -Body '{"status":
   "FAILURE"}'
  Value:
   'Fn::GetAtt':
    - PowerShellCurlCli
```

更多示例，请参见JSON示例和YAML示例。

#### ALIYUN::ROS::Stack

嵌套资源栈本身可以包含其他嵌套资源栈，构成一个资源栈层次结构。根资源栈是所有嵌套资源栈最终归属的父资源栈，根资源栈的模板称为顶层模板。ALIYUN::ROS::Stack类型在顶层模板中将资源栈作为资源进行嵌套。 您可以将嵌套资源栈模板中的一个资源栈的输出用作另一个资源栈的输入。您也可以使用Fn::GetAtt函数，将函数参数设置为嵌套资源栈的名称和Outputs.NestedStackOutputName格式的输出值，获取嵌套资源栈的输出。

**语法**

资源编排

```json
{
  "Type": "ALIYUN::ROS::Stack",
  "Properties": {
    "TemplateURL": String,
    "TemplateBody": String,
    "TemplateId": String,
    "TemplateVersion": String,
    "TimeoutMins": Number,
    "Parameters": Map,
    "ResourceGroupId": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 |  |  | 描述 | 约束 |
|---|---|---|---|---|---|---|---|
| TemplateURL | String | 否 | 是 |  |  |  | 模板主体的文件最大为524,288个字节，URL的最大长度为1024个字节。 URL必须指向位于Web服务器 （HTTP、HTTPS）或阿里云OSS存储空间中的模板。例如： oss://ros/template/dem o 、 oss://ros/template/de mo?RegionId=cn-hangzhou 。 OSS地域如未指定，默认与资源栈 RegionId相同。 您必须指定 TemplateURL 、 Templat eBody 或 TemplateId 其中一个。如果都指定，则使用 TemplateBody 。 |
|  |  |  |  |  |  |  | o |
|  |  |  |  |  |  | 模板主体的文件的位置。 |  |
| TemplateBod y | Map | 否 | 是 |  |  | 模板内容，用于简化模板的传递。 | 内容为原始数据，函数只在子模板中生效，不在当前模板中生效。 您必须指定 TemplateURL 、 Templat eBody 或 TemplateId 其中一个。如果都指定，则使用 TemplateBody 。 |
| TemplateId | String | 否 | 是 |  |  | 模板ID。 | 您必须指定 TemplateURL 、 Templat eBody 或 TemplateId 其中一个。如果都指定，则使用 TemplateBody 。 |
| TemplateVers ion | String | 否 | 是 |  |  | 模板版本名。 | 无 |
| TimeoutMins | Number | 否 | 是 |  |  | 创建或更新资源栈的超时时间。 | 单位：分。 默认值：60。 |
| Parameters | Map | 否 | 是 |  |  | 一组键值对，表示在创建此嵌套资源栈时传递给 ROS的参数。 | Parameters中的每个键都对应于嵌套资源栈模板中的参数名，每个值对应于参数取值。如果嵌套资源栈需要输入参数，则必须指定此参数。 |

| oss://ros/template/dem |  |  |
|---|---|---|
|  | oss://ros/template/de |  |

|  |  | TemplateURL |  |
|---|---|---|---|
|  | eBody |  |  |

| Templat |  |
|---|---|

|  |  | TemplateURL |  |
|---|---|---|---|
|  | eBody |  |  |

| Templat |  |
|---|---|

|  |  | TemplateURL |  |
|---|---|---|---|
|  | eBody |  |  |

| Templat |  |
|---|---|

资源编排

| ResourceGro upId | String | 否 | 否 | 资源组ID。 | 无 |
|---|---|---|---|---|---|

**返回值**

Fn::GetAtt 您可以通过以下代码，获取嵌套资源栈的输出。

```json
{
  "Fn::GetAtt": [
    "<nested_stack>",
    "Outputs.<nested_stack_output_name>"
```

]

```
}
```

| Ref | 引用嵌套资源栈资源时，将获得嵌套资源栈的ARN。例如： |
|---|---|

**示例**

子资源栈创建VPC、vSwitch、安全组示例（子资源栈模板保存至oss://ros/template/vpc.txt）

| YAML | 格式 |
|---|---|
| ROSTemplateFormatVersion: '2015-09-01' Description: One VPC, vSwitch, security group. Parameters: ZoneId: Type: String Description: The available zone SecurityGroupName: Type: String Description: The security group name Default: my-sg-name VpcName: Type: String Description: The VPC name MinLength: 2 MaxLength: 128 ConstraintDescription: '[2, 128] English or Chinese letters' Default: my-vpc-name VpcCidrBlock: Type: String AllowedValues: - 192.168.0.0/16 - 172.16.0.0/12 - 10.0.0.0/8 Default: 10.0.0.0/8 VSwitchCidrBlock: Type: String Description: The vSwitch subnet which must be within VPC Default: 10.0.10.0/24 UpdateVersion: Type: Number Default: 0 Resources: Vpc: Type: ALIYUN::ECS::VPC Properties: CidrBlock: Ref: VpcCidrBlock VpcName: Ref: VpcName |  |

资源编排

```
  VSwitch:
    Properties:
      CidrBlock:
        Ref: VSwitchCidrBlock
      ZoneId:
        Ref: ZoneId
      VpcId:
        Fn::GetAtt:
          - Vpc
          - VpcId
  SecurityGroup:
    Properties:
      SecurityGroupName:
        Ref: SecurityGroupName
      VpcId:
        Ref: Vpc
  WaitConditionHandle:
    Properties:
      UpdateVersion:
        Ref: UpdateVersion
Outputs:
  SecurityGroupId:
    Value:
      Fn::GetAtt:
        - SecurityGroupId
  VpcId:
    Value:
      Fn::GetAtt:
        - Vpc
        - VpcId
  VSwitchId:
    Value:
      Fn::GetAtt:
        - VSwitchId
```

| JSON | 格式 |
|---|---|
| { "ROSTemplateFormatVersion": "2015-09-01", "Description": "One VPC, vSwitch, security group.", "Parameters": { "ZoneId": { "Type": "String", "Description": "The available zone" }, "SecurityGroupName": { "Type": "String", "Description": "The security group name", "Default": "my-sg-name" }, "VpcName": { "Type": "String", "Description": "The VPC name", "MinLength": 2, "MaxLength": 128, "ConstraintDescription": "[2, 128] English or Chinese letters", "Default": "my-vpc-name" |  |

资源编排

```json
    },
    "VpcCidrBlock": {
      "Type": "String",
      "AllowedValues": [
        "192.168.0.0/16",
        "172.16.0.0/12",
        "10.0.0.0/8"
```

`],`

```json
      "Default": "10.0.0.0/8"
    },
    "VSwitchCidrBlock": {
      "Type": "String",
      "Description": "The vSwitch subnet which must be within VPC",
      "Default": "10.0.10.0/24"
    },
    "UpdateVersion": {
      "Type": "Number",
      "Default": 0
    }
  },
  "Resources": {
    "Vpc": {
      "Type": "ALIYUN::ECS::VPC",
      "Properties": {
        "CidrBlock": {
          "Ref": "VpcCidrBlock"
        },
        "VpcName": {
          "Ref": "VpcName"
        }
      }
    },
    "VSwitch": {
      "Type": "ALIYUN::ECS::VSwitch",
      "Properties": {
        "CidrBlock": {
          "Ref": "VSwitchCidrBlock"
        },
        "ZoneId": {
          "Ref": "ZoneId"
        },
        "VpcId": {
          "Fn::GetAtt": [
            "Vpc",
            "VpcId"
```

]

```json
        }
      }
    },
    "SecurityGroup": {
      "Type": "ALIYUN::ECS::SecurityGroup",
      "Properties": {
        "SecurityGroupName": {
          "Ref": "SecurityGroupName"
        },
        "VpcId": {
          "Ref": "Vpc"
        }
      }
    },
    "WaitConditionHandle": {
      "Type": "ALIYUN::ROS::WaitConditionHandle",
"Properties":{
```

资源编排

```json
      "Properties": {
        "UpdateVersion": {
          "Ref": "UpdateVersion"
        }
      }
    }
  },
  "Outputs": {
    "SecurityGroupId": {
      "Value": {
        "Fn::GetAtt": [
          "SecurityGroup",
          "SecurityGroupId"
```

]

```json
      }
    },
    "VpcId": {
      "Value": {
        "Fn::GetAtt": [
          "Vpc",
          "VpcId"
```

]

```json
      }
    },
    "VSwitchId": {
      "Value": {
        "Fn::GetAtt": [
          "VSwitch",
          "VSwitchId"
```

]

```
      }
    }
  }
}
```

父资源栈示例 `YAML` 格式

```
ROSTemplateFormatVersion: '2015-09-01' Description: One ECS instance. Parameters:
  ImageId:
    Default: centos_7
    Type: String
    Description: Image Id, represents the image resource to startup the ECS instance
  InstanceType:
    Type: String
    Description: The ECS instance type,
    Default: ecs.xn4.small
  ZoneId:
    Type: String
    Description: 'The available zone '
  InstanceChargeType:
    Type: String
    AllowedValues:
      - PrePaid
      - PostPaid
    Default: PostPaid
    Description: The instance charge type
  SecurityGroupName:
    Type: String
    Description: The security group name
    Default: my-sg-name
```

资源编排 y g

```
  NetworkInterfaceName:
    Type: String
    Description: The Network interface name
    Default: my-eni-name
  VpcName:
    Type: String
    Description: The VPC name
    MinLength: 2
    MaxLength: 128
    ConstraintDescription: '[2, 128] English or Chinese letters'
    Default: my-vpc-name
  IoOptimized:
    AllowedValues:
      - none
      - optimized
    Description: IO optimized, optimized is for the IO optimized instance type
    Type: String
    Default: optimized
  SystemDiskCategory:
    AllowedValues:
      - cloud
      - cloud_efficiency
      - cloud_ssd
    Description: 'System disk category: average cloud disk(cloud), efficient cloud
disk(cloud_efficiency) or SSD cloud disk(cloud_ssd)'
    Type: String
    Default: cloud_ssd
  VpcCidrBlock:
    Type: String
    AllowedValues:
      - 192.168.0.0/16
      - 172.16.0.0/12
      - 10.0.0.0/8
    Default: 10.0.0.0/8
  VSwitchCidrBlock:
    Type: String
    Description: The VSwitch subnet which must be within VPC
    Default: 10.0.10.0/24
  UpdateVersion:
    Type: Number
    Default: 0
Resources:
  NetworkStack:
    Properties:
      TemplateURL: oss://ros/template/vpc.txt
      TimeoutMins: 5
      Parameters:
        ZoneId:
          Ref: ZoneId
        SecurityGroupName:
          Ref: SecurityGroupName
        VpcName:
          Ref: VpcName
        VpcCidrBlock:
          Ref: VpcCidrBlock
        VSwitchCidrBlock:
          Ref: VSwitchCidrBlock
        UpdateVersion:
          Ref: UpdateVersion
  WebServer:
```

资源编排

```
    Properties:
      ImageId:
        Ref: ImageId
      InstanceType:
        Ref: InstanceType
      InstanceChargeType:
        Ref: InstanceChargeType
      SecurityGroupId:
        Fn::GetAtt:
          - NetworkStack
          - Outputs.SecurityGroupId
      VpcId:
        Fn::GetAtt:
          - NetworkStack
          - Outputs.VpcId
      VSwitchId:
        Fn::GetAtt:
          - NetworkStack
          - Outputs.VSwitchId
      IoOptimized:
        Ref: IoOptimized
      ZoneId:
        Ref: ZoneId
      SystemDisk_Category:
        Ref: SystemDiskCategory
      DiskMappings:
        - Category: cloud_ssd
          Size: 20
Outputs:
  InstanceId:
    Value:
      Fn::GetAtt:
        - WebServer
        - InstanceId
  PublicIp:
    Value:
      Fn::GetAtt:
        - WebServer
        - PublicIp
  SecurityGroupId:
    Value:
      Fn::GetAtt:
        - NetworkStack
        - Outputs.SecurityGroupId
  VpcId:
    Value:
      Fn::GetAtt:
        - NetworkStack
        - Outputs.VpcId
  VSwitchId:
    Value:
      Fn::GetAtt:
        - NetworkStack
        - Outputs.VSwitchId
  NetworkStackArn:
    Value:
      Ref: NetworkStack
```

`JSON` 格式

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
```

资源编排

```json
  "Description": "One ECS instance.",
  "Parameters": {
    "ImageId": {
      "Default": "centos_7",
      "Type": "String",
      "Description": "Image Id, represents the image resource to startup the ECS instance"
    },
    "InstanceType": {
      "Type": "String",
      "Description": "The ECS instance type,",
      "Default": "ecs.xn4.small"
    },
    "ZoneId": {
      "Type": "String",
      "Description": "The available zone "
    },
    "InstanceChargeType": {
      "Type": "String",
      "AllowedValues": [
        "PrePaid",
        "PostPaid"
```

`],`

```json
      "Default": "PostPaid",
      "Description": "The instance charge type"
    },
    "SecurityGroupName": {
      "Type": "String",
      "Description": "The security group name",
      "Default": "my-sg-name"
    },
    "NetworkInterfaceName": {
      "Type": "String",
      "Description": "The Network interface name",
      "Default": "my-eni-name"
    },
    "VpcName": {
      "Type": "String",
      "Description": "The VPC name",
      "MinLength": 2,
      "MaxLength": 128,
      "ConstraintDescription": "[2, 128] English or Chinese letters",
      "Default": "my-vpc-name"
    },
    "IoOptimized": {
      "AllowedValues": [
        "none",
        "optimized"
```

`],`

```json
      "Description": "IO optimized, optimized is for the IO optimized instance type",
      "Type": "String",
      "Default": "optimized"
    },
    "SystemDiskCategory": {
      "AllowedValues": [
        "cloud",
        "cloud_efficiency",
        "cloud_ssd"
```

`],`

```json
      "Description": "System disk category: average cloud disk(cloud), efficient cloud
disk(cloud_efficiency) or SSD cloud disk(cloud_ssd)",
      "Type": "String",
      "Default": "cloud_ssd"
```

资源编排

```json
    },
    "VpcCidrBlock": {
      "Type": "String",
      "AllowedValues": [
        "192.168.0.0/16",
        "172.16.0.0/12",
        "10.0.0.0/8"
```

`],`

```json
      "Default": "10.0.0.0/8"
    },
    "VSwitchCidrBlock": {
      "Type": "String",
      "Description": "The VSwitch subnet which must be within VPC",
      "Default": "10.0.10.0/24"
    },
    "UpdateVersion": {
      "Type": "Number",
      "Default": 0
    }
  },
  "Resources": {
    "NetworkStack": {
      "Type": "ALIYUN::ROS::Stack",
      "Properties": {
        "TemplateURL": "oss://ros/template/vpc.txt",
        "TimeoutMins": 5,
        "Parameters": {
          "ZoneId": {
            "Ref": "ZoneId"
          },
          "SecurityGroupName": {
            "Ref": "SecurityGroupName"
          },
          "VpcName": {
            "Ref": "VpcName"
          },
          "VpcCidrBlock": {
            "Ref": "VpcCidrBlock"
          },
          "VSwitchCidrBlock": {
            "Ref": "VSwitchCidrBlock"
          },
          "UpdateVersion": {
            "Ref": "UpdateVersion"
          }
        }
      }
    },
    "WebServer": {
      "Type": "ALIYUN::ECS::Instance",
      "Properties": {
        "ImageId": {
          "Ref": "ImageId"
        },
        "InstanceType": {
          "Ref": "InstanceType"
        },
        "InstanceChargeType": {
          "Ref": "InstanceChargeType"
        },
        "SecurityGroupId": {
          "Fn::GetAtt": [
            "NetworkStack",
```

资源编排

```
etwo Stac
```

,

```
            "Outputs.SecurityGroupId"
```

]

```json
        },
        "VpcId": {
          "Fn::GetAtt": [
            "NetworkStack",
            "Outputs.VpcId"
```

]

```json
        },
        "VSwitchId": {
          "Fn::GetAtt": [
            "NetworkStack",
            "Outputs.VSwitchId"
```

]

```json
        },
        "IoOptimized": {
          "Ref": "IoOptimized"
        },
        "ZoneId": {
          "Ref": "ZoneId"
        },
        "SystemDisk_Category": {
          "Ref": "SystemDiskCategory"
        },
        "DiskMappings": [
          {
            "Category": "cloud_ssd",
            "Size": 20
          }
```

]

```json
      }
    }
  },
  "Outputs": {
    "InstanceId": {
      "Value": {
        "Fn::GetAtt": [
          "WebServer",
          "InstanceId"
```

]

```json
      }
    },
    "PublicIp": {
      "Value": {
        "Fn::GetAtt": [
          "WebServer",
          "PublicIp"
```

]

```json
      }
    },
    "SecurityGroupId": {
      "Value": {
        "Fn::GetAtt": [
          "NetworkStack",
          "Outputs.SecurityGroupId"
```

]

```json
      }
    },
    "VpcId": {
      "Value": {
        "Fn::GetAtt": [
          "NetworkStack",
```

资源编排

```
          "Outputs.VpcId"
```

]

```json
      }
    },
    "VSwitchId": {
      "Value": {
        "Fn::GetAtt": [
          "NetworkStack",
          "Outputs.VSwitchId"
```

]

```json
      }
    },
    "NetworkStackArn": {
      "Value": {
        "Ref": "NetworkStack"
      }
    }
  }
}
```

更多示例，请参见：JSON示例和YAML示例。

### SLB

#### ALIYUN::SLB::AccessControl

**语法**

```json
{
  "Type": "ALIYUN::SLB::AccessControl",
  "Properties": {
    "AddressIPVersion": String,
    "AclName": String,
    "AclEntrys": List,
    "Tags": List,
    "ResourceGroupId": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| AddressIPVer sion | String | 否 | 否 | IP版本。 | 取值： ipv4 ipv6 |
| AclName | String | 是 | 是 | 访问控制策略组名称。 | 无 |
| ResourceGro upId | String | 否 | 是 | 访问控制策略组所属的资源组 ID。 | 无 |
| AclEntrys | List | 否 | 否 | 访问控制策略组的信息列表。 | 最多支持50个信息列表。 更多信息，请参见AclEntrys属性。 |

资源编排

| Tags | List | 否 | 是 | 标签。 | 最多支持添加20个标签。 更多信息，请参见Tags属性。 |
|---|---|---|---|---|---|

**AclEntrys语法**

```json
"AclEntrys": [
  {
    "comment": String,
    "entry": String
  }
```

]

**AclEntrys属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| comment | String | 否 | 否 | 访问控制条目备注。 | 无 |
| entry | String | 是 | 否 | IP地址或CIDR 网段。 | 无 |

**Tags语法**

```json
"Tags": [
  {
    "Key": String,
    "Value": String
  }
```

]

**Tags属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Key | String | 是 | 否 | 标签键。 | 长度为1~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |
| Value | String | 否 | 否 | 标签值。 | 长度为0~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |

**返回值**

Fn::GetAtt AclId：访问控制策略组ID。

**示例**

`JSON` 格式资源编排

```json
{
 "ROSTemplateFormatVersion": "2015-09-01",
 "Parameters": {
  "AclEntrys": {
   "Type": "Json",
   "Description": "A list of acl entrys. Each entry can be IP addresses or CIDR blocks. Max length: 5
0.",
   "MaxLength": 50
  },
  "AddressIPVersion": {
   "Type": "String",
   "Description": "IP version. Could be \"ipv4\" or \"ipv6\".",
   "AllowedValues": [
    "ipv4",
    "ipv6"
```

]

```json
  },
  "AclName": {
   "Type": "String",
   "Description": "The name of the access control list."
  },
  "Tags": {
   "Type": "Json",
   "Description": "Tags to attach to instance. Max support 20 tags to add during create instance. Eac
h tag with two properties Key and Value, and Key is required.",
   "MaxLength": 20
  }
 },
 "Resources": {
  "AccessControl": {
   "Type": "ALIYUN::SLB::AccessControl",
   "Properties": {
    "AclEntrys": {
     "Ref": "AclEntrys"
    },
    "AddressIPVersion": {
     "Ref": "AddressIPVersion"
    },
    "AclName": {
     "Ref": "AclName"
    },
    "Tags": {
     "Ref": "Tags"
    }
   }
  }
 },
 "Outputs": {
  "AclId": {
   "Description": "The ID of the access control list.",
   "Value": {
    "Fn::GetAtt": [
     "AccessControl",
     "AclId"
```

]

```
   }
  }
 }
}
```

`YAML` 格式资源编排

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
 AclEntrys:
  Description: 'A list of acl entrys. Each entry can be IP addresses or CIDR blocks.
   Max length: 50.'
  MaxLength: 50
  Type: Json
 AclName:
  Description: The name of the access control list.
  Type: String
 AddressIPVersion:
  AllowedValues:
  - ipv4
  - ipv6
  Description: IP version. Could be "ipv4" or "ipv6".
  Type: String
 Tags:
  Description: Tags to attach to instance. Max support 20 tags to add during create
   instance. Each tag with two properties Key and Value, and Key is required.
  MaxLength: 20
  Type: Json
Resources:
 AccessControl:
  Properties:
   AclEntrys:
    Ref: AclEntrys
   AclName:
    Ref: AclName
   AddressIPVersion:
    Ref: AddressIPVersion
   Tags:
    Ref: Tags
Outputs:
 AclId:
  Description: The ID of the access control list.
  Value:
   Fn::GetAtt:
   - AclId
```

更多示例，请参见：JSON示例和YAML示例。

#### ALIYUN::SLB::BackendServerAttachment

ALIYUN::SLB::BackendServerAttachment类型用于添加后端服务器。

**语法**

```json
{
  "Type": "ALIYUN::SLB::BackendServerAttachment",
  "Properties": {
    "LoadBalancerId": String,
    "BackendServers": List,
    "BackendServerList": List,
    "BackendServerWeightList": List
  }
}
```

**属性**

资源编排

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| LoadBalancerId | String | 是 | 否 | 负载均衡实例的唯一标识ID。 | 无 |
| BackendServerLi st | List | 否 | 是 | 需要添加的后端服务器列表。 | LoadBalancerId 和 BackendServer WeightList联合使用。ECS的实例ID 用半角逗号（,）分隔。 当指定 BackendServers 时，将忽略该值。 |
| BackendServer WeightList | List | 否 | 是 | 按顺序指定 BackendServerLi st中各ECS实例的权重。 | 不指定该值，则 BackendServerLi st中所有ECS实例权重都是 100；当 BackendServer WeightList长度小于 BackendServerLi st时， 则使用 BackendServer WeightList中的最后一个值配置 BackendServerLi st中剩余ECS实例的权重。 |
| BackendServers | List | 否 | 是 | 需要添加的后端服务器列表。 | 后端服务器（ECS 实例）必须在运行中才可以加入负载均衡实例。 详情请参见BackendServe rs属性。 |

**BackendServers语法**

```json
"BackendServers": [
  {
    "ServerId" : String,
    "Weight" : Integer,
    "Type": String,
    "ServerIp": String,
    "Description": String
  }
```

]

**BackendServers属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ServerId | String | 是 | 是 | ECS实例ID。 | 后端服务器（ECS 实例）必须在运行中才可以加入负载均衡实例，每次调用最多可添加20个后端服务器。 只有性能保障型实例支持添加eni类型的后端服务器。 |

资源编排

| Weight | Integer | 是 | 是 | ECS实例在SLB实例中的权重。 | 取值范围： 0~100。 默认值：100。 |
|---|---|---|---|---|---|
| ServerIp | String | 否 | 否 | 后端服务器IP。 | 无 |
| Type | String | 否 | 否 | 后端服务器类型。 | 取值： ecs：ECS实例 （默认值）。 eni：弹性网卡实例。 eci：弹性容器实例。 |
| Description | String | 否 | 是 | 后端服务器描述。 | 长度为1~80个字符，可包含英文字母、汉字、数字、 短划线（-）、正斜线（/）、英文句点 （.）和下划线 （ ）。 _ |

**返回值**

Fn::GetAtt BackendServers：所有加入负载均衡的后端服务器列表。 LoadBalancerId：负载均衡实例ID。

**示例**

`JSON` 格式

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "BackendServerList": {
      "Type": "Json",
      "Description": "The comma delimited instance id list.If the property \"BackendServers\" is sett
ing, this property will be ignored."
    },
    "LoadBalancerId": {
      "Type": "String",
      "Description": "The id of load balancer."
    },
    "BackendServerWeightList": {
      "Type": "CommaDelimitedList",
      "Description": "The comma delimited weight list. If no value specified will use 100. If the len
gth is small than \"BackendServerList\", it will copy the last one to fill the array.If the property \"BackendServers\" is setting, this property will be ignored."
    },
    "BackendServers": {
      "Type": "Json",
      "Description": "The list of ECS instance, which will attached to load balancer."
    }
  },
  "Resources": {
    "BackendServer": {
      "Type": "ALIYUN::SLB::BackendServerAttachment",
      "Properties": {
        "BackendServerList": {
          "Ref": "BackendServerList"
        },
        "LoadBalancerId": {
"Ref":"LoadBalancerId"
```

资源编排

```json
          Ref: LoadBalancerId
        },
        "BackendServerWeightList": {
          "Ref": "BackendServerWeightList"
        },
        "BackendServers": {
          "Ref": "BackendServers"
        }
      }
    }
  },
  "Outputs": {
    "LoadBalancerId": {
      "Description": "The id of load balancer.",
      "Value": {
        "Fn::GetAtt": [
          "BackendServer",
          "LoadBalancerId"
```

]

```json
      }
    },
    "BackendServers": {
      "Description": "The collection of attached backend server.",
      "Value": {
        "Fn::GetAtt": [
          "BackendServer",
          "BackendServers"
```

]

```
      }
    }
  }
}
```

`YAML` 格式资源编排

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  BackendServerList:
    Type: Json
    Description: >-
      The comma delimited instance id list.If the property "BackendServers" is
      setting, this property will be ignored.
  LoadBalancerId:
    Type: String
    Description: The id of load balancer.
  BackendServerWeightList:
    Type: CommaDelimitedList
    Description: >-
      The comma delimited weight list. If no value specified will use 100. If
      the length is small than "BackendServerList", it will copy the last one to
      fill the array.If the property "BackendServers" is setting, this property
      will be ignored.
  BackendServers:
    Type: Json
    Description: 'The list of ECS instance, which will attached to load balancer.'
Resources:
  BackendServer:
    Properties:
      BackendServerList:
        Ref: BackendServerList
      LoadBalancerId:
        Ref: LoadBalancerId
      BackendServerWeightList:
        Ref: BackendServerWeightList
      BackendServers:
        Ref: BackendServers
Outputs:
  LoadBalancerId:
    Description: The id of load balancer.
    Value:
      'Fn::GetAtt':
        - LoadBalancerId
  BackendServers:
    Description: The collection of attached backend server.
    Value:
      'Fn::GetAtt':
        - BackendServers
```

**7.9.3.**

#### ALIYUN::SLB::BackendServerToVServerGroupAddition

ALIYUN::SLB::BackendServerToVServerGroupAddition类型用于把后端服务器添加到已存在的服务器组中。

**语法**

资源编排

```json
{
  "Type": "ALIYUN::SLB::BackendServerToVServerGroupAddition",
  "Properties": {
    "BackendServers": List,
    "VServerGroupId": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| VServerGroup Id | String | 是 | 否 | 服务器组ID。 | 无 |
| BackendServ ers | List | 是 | 是 | 服务器列表。 | 更多信息，请参见BackendServers属性。 |

**BackendServers语法**

```json
"BackendServers": [
  {
    "ServerId": String,
    "Port": Integer,
    "Weight": Integer,
    "Type": String,
    "Description": String,
    "ServerIp": String
  }
```

]

**BackendServers属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ServerId | String | 是 | 是 | 后端服务器的实例ID。 | 无 |
| Port | Integer | 是 | 是 | 后端服务器使用的端口。 | 取值范围：1~65,535。 |
| Weight | Integer | 否 | 是 | 后端服务器的权重。 | 取值范围：0~100。 |
| Type | String | 否 | 是 | 后端服务器类型。 | 取值： ecs（默认值）：ECS实例。 eni：弹性网卡实例。 说明只有性能保障型实例支持添加ENI类型的后端服务器。 |
| Description | String | 否 | 是 | 后端服务器描述。 | 长度为1~80个字符，可包含英文字母、汉字、数字、短划线（-）、正斜线（/）、半角句号（.）和下划线 （ ）。 _ |
| ServerIp | String | 否 | 是 | 后端服务器的IP 地址。 | ECS或者ENI的实例IP地址。 |

**返回值**

Fn::GetAtt 资源编排 VServerGroupId：服务器组的ID。

**示例**

`JSON` 格式

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "VServerGroupId": {
      "Type": "String",
      "Description": "The ID of virtual server group."
    },
    "BackendServers": {
      "Type": "Json",
      "Description": "The list of a combination of ECS Instance-Port-Weight.Same ecs instance with di
fferent port is allowed, but same ecs instance with same port isn't."
    }
  },
  "Resources": {
    "BackendServerToVServerGroupAddition": {
      "Type": "ALIYUN::SLB::BackendServerToVServerGroupAddition",
      "Properties": {
        "VServerGroupId": {
          "Ref": "VServerGroupId"
        },
        "BackendServers": {
          "Ref": "BackendServers"
        }
      }
    }
  },
  "Outputs": {
    "VServerGroupId": {
      "Description": "The ID of virtual server group.",
      "Value": {
        "Fn::GetAtt": [
          "BackendServerToVServerGroupAddition",
          "VServerGroupId"
```

]

```
      }
    }
  }
}
```

`YAML` 格式资源编排

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  VServerGroupId:
    Type: String
    Description: The ID of virtual server group.
  BackendServers:
    Type: Json
    Description: >-
      The list of a combination of ECS Instance-Port-Weight.Same ecs instance
      with different port is allowed, but same ecs instance with same port
      isn't.
Resources:
  BackendServerToVServerGroupAddition:
    Type: 'ALIYUN::SLB::BackendServerToVServerGroupAddition'
    Properties:
      VServerGroupId:
        Ref: VServerGroupId
      BackendServers:
        Ref: BackendServers
Outputs:
  VServerGroupId:
    Description: The ID of virtual server group.
    Value:
      'Fn::GetAtt':
        - VServerGroupId
```

更多示例，请参见创建负载均衡监听、克隆负载均衡实例、上传证书、创建扩展域名、创建服务器组并添加后端服务器到负载均衡实例、为HTTP或HTTPS监听添加转发规则和将后端服务器添加到服务器组的组合示例：JSON示例和YAML示例。

#### ALIYUN::SLB::Certificate

ALIYUN::SLB::Certificate类型用于上传证书，支持ServerCertificate和CACertificate两种证书。

**重要**

一次只能上传一份CA证书内容（"CertificateType": "CA"）。 一次只能上传一份服务器证书和对应的私钥（"CertificateType": "Server"）。

**语法**

```json
{
  "Type": "ALIYUN::SLB::Certificate",
  "Properties": {
    "CertificateName": String,
    "Certificate": String,
    "AliCloudCertificateName": String,
    "PrivateKey": String,
    "ResourceGroupId": String,
    "CertificateType": String,
    "AliCloudCertificateId": String,
    "Tags": List
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|

资源编排

| ResourceGro upId | String | 否 | 是 | 资源组ID。 | 无 |
|---|---|---|---|---|---|
| CertificateNa me | String | 否 | 是 | 证书名称。 | 无 |
| Certificate | String | 是 | 否 | 需要上传证书的内容。 | 无 |
| AliCloudCertif icateName | String | 否 | 否 | 阿里云的云上证书名称。 | 无 |
| PrivateKey | String | 否 | 否 | 需要上传的私钥。 | 无 |
| AliCloudCertif icateId | String | 否 | 否 | 阿里云的云上证书ID。 | 使用阿里云的云上证书时，此参数为必选参数。 |
| CertificateTyp e | String | 否 | 否 | 证书类型。 | 取值： Server CA |
| Tags | List | 否 | 是 | 标签。 | 最多支持添加20个标签。 更多信息，请参见Tags属性。 |

**Tags语法**

```json
"Tags": [
  {
    "Key": String,
    "Value": String
  }
```

]

**Tags属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Key | String | 是 | 否 | 标签键。 | 长度为1~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |
| Value | String | 否 | 否 | 标签值。 | 长度为0~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |

**返回值**

Fn::GetAtt CertificateId：证书ID。 Fingerprint：证书的指纹。

**示例**

`JSON` 格式

```json
{
 "ROSTemplateFormatVersion": "2015-09-01",
 "Parameters": {
  "CertificateType": {
   "Type": "String",
```

资源编排

```json
   "Description": "The type of the certificate.",
   "AllowedValues": [
    "Server",
    "CA"
```

`],`

```json
   "Default": "Server"
  },
  "AliCloudCertificateName": {
   "Type": "String",
   "Description": "The name of the Alibaba Cloud certificate."
  },
  "PrivateKey": {
   "Type": "String",
   "Description": "The private key."
  },
  "ResourceGroupId": {
   "Type": "String",
   "Description": "Resource group id."
  },
  "CertificateName": {
   "Type": "String",
   "Description": "The name of the certificate."
  },
  "Tags": {
   "Type": "Json",
   "Description": "Tags to attach to instance. Max support 20 tags to add during create instance. Eac
h tag with two properties Key and Value, and Key is required.",
   "MaxLength": 20
  },
  "Certificate": {
   "Type": "String",
   "Description": "The content of the certificate public key."
  },
  "AliCloudCertificateId": {
   "Type": "String",
   "Description": "The ID of the Alibaba Cloud certificate."
  }
 },
 "Resources": {
  "SLBCertificate": {
   "Type": "ALIYUN::SLB::Certificate",
   "Properties": {
    "CertificateType": {
     "Ref": "CertificateType"
    },
    "AliCloudCertificateName": {
     "Ref": "AliCloudCertificateName"
    },
    "PrivateKey": {
     "Ref": "PrivateKey"
    },
    "ResourceGroupId": {
     "Ref": "ResourceGroupId"
    },
    "CertificateName": {
     "Ref": "CertificateName"
    },
    "Tags": {
     "Ref": "Tags"
    },
    "Certificate": {
     "Ref": "Certificate"
}
```

资源编排

```json
    },
    "AliCloudCertificateId": {
     "Ref": "AliCloudCertificateId"
    }
   }
  }
 },
 "Outputs": {
  "Fingerprint": {
   "Description": "The fingerprint of the certificate.",
   "Value": {
    "Fn::GetAtt": [
     "SLBCertificate",
     "Fingerprint"
```

]

```json
   }
  },
  "CertificateId": {
   "Description": "The ID of the certificate.",
   "Value": {
    "Fn::GetAtt": [
     "SLBCertificate",
     "CertificateId"
```

]

```
   }
  }
 }
}
```

`YAML` 格式

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
 AliCloudCertificateId:
  Description: The ID of the Alibaba Cloud certificate.
  Type: String
 AliCloudCertificateName:
  Description: The name of the Alibaba Cloud certificate.
  Type: String
 Certificate:
  Description: The content of the certificate public key.
  Type: String
 CertificateName:
  Description: The name of the certificate.
  Type: String
 CertificateType:
  AllowedValues:
  - CA
  Default: Server
  Description: The type of the certificate.
  Type: String
 PrivateKey:
  Description: The private key.
  Type: String
 ResourceGroupId:
  Description: Resource group id.
  Type: String
 Tags:
  Description: Tags to attach to instance. Max support 20 tags to add during create
   instance. Each tag with two properties Key and Value, and Key is required.
  MaxLength: 20
Type:Json
```

资源编排

```
  Type: Json
Resources:
 SLBCertificate:
  Properties:
   AliCloudCertificateId:
    Ref: AliCloudCertificateId
   AliCloudCertificateName:
    Ref: AliCloudCertificateName
   Certificate:
    Ref: Certificate
   CertificateName:
    Ref: CertificateName
   CertificateType:
    Ref: CertificateType
   PrivateKey:
    Ref: PrivateKey
   ResourceGroupId:
    Ref: ResourceGroupId
   Tags:
    Ref: Tags
Outputs:
 CertificateId:
  Description: The ID of the certificate.
  Value:
   Fn::GetAtt:
   - CertificateId
 Fingerprint:
  Description: The fingerprint of the certificate.
  Value:
   Fn::GetAtt:
   - Fingerprint
```

更多示例，请参见创建负载均衡监听、克隆负载均衡实例、上传证书、创建扩展域名、创建虚拟服务器组并添加后端服务器到负载均衡实例、为HTTP或HTTPS监听添加转发规则和将后端服务器添加到虚拟服务器组的组合示例：JSON示例和YAML 示例。

#### ALIYUN::SLB::DomainExtension

**语法**

```json
{
  "Type": "ALIYUN::SLB::DomainExtension",
  "Properties": {
    "Domain": String,
    "ListenerPort": Integer,
    "ServerCertificateId": String,
    "LoadBalancerId": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Domain | String | 是 | 否 | 域名。 | 无。 |

资源编排

| ListenerPort | Integer | 是 | 否 | 负载均衡实例 HTTPS监听的前端端口。 | 取值范围： 1~65535。 |
|---|---|---|---|---|---|
| ServerCertificate Id | String | 是 | 是 | 与域名对应的证书 ID。 | 无。 |
| LoadBalancerId | String | 是 | 否 | 负载均衡实例的 ID。 | 无。 |

**返回值**

Fn::GetAtt DomainExtensionId：创建的扩展域名ID。 ListenerPort：负载均衡实例前端使用的端口。

**示例**

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "DomainExtension": {
      "Type": "ALIYUN::SLB::DomainExtension",
      "Properties": {
        "Domain": "*.example.com",
        "ListenerPort": "443",
        "ServerCertificateId": "123157908552****_166f8204689_1714763408_70998****",
        "LoadBalancerId": "lb-bp1o94dp5i6earr9g****"
      }
    }
  },
  "Outputs": {
    "DomainExtensionId": {
      "Value": {
        "Fn::GetAtt": [
          "DomainExtension",
          "DomainExtensionId"
```

]

```json
      }
    },
    "ListenerPort": {
      "Value": {
        "Fn::GetAtt": [
          "DomainExtension",
          "ListenerPort"
```

]

```
      }
    }
  }
}
```

#### ALIYUN::SLB::Listener

**语法**

资源编排

```json
{
  "Type": "ALIYUN::SLB::Listener",
  "Properties": {
    "MasterSlaveServerGroupId": String,
    "AclStatus": String,
    "Protocol": String,
    "AclId": String,
    "ServerCertificateId": String,
    "HealthCheck": Map,
    "RequestTimeout": Integer,
    "IdleTimeout": Integer,
    "ListenerPort": Integer,
    "HttpConfig": Map,
    "Bandwidth": Integer,
    "AclType": String,
    "BackendServerPort": Integer,
    "Scheduler": String,
    "LoadBalancerId": String,
    "CACertificateId": String,
    "Persistence": Map,
    "VServerGroupId": String,
    "Description": String,
    "PortRange": List,
    "StartListener": Boolean,
    "EnableHttp2": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| MasterSlaveS erverGroupId | String | 否 | 否 | 主备服务器组 ID。 | 无 |
| AclStatus | String | 否 | 是 | 是否开启访问控制功能。 | 取值： on（默认值）：开启。 off：关闭。 |
| EnableHttp2 | String | 否 | 是 | 是否开启 HTTP2特性。 | 取值： on：开启。 off ：不开启。 |
| AclId | String | 否 | 是 | 监听绑定的访问策略组ID。 | 当AclStatus取值为on时，必须指定该参数。 |

资源编排

| AclType | String | 否 | 是 | 访问控制类型。 | 取值： white：仅转发来自所选访问控制策略组中设置的IP地址或地址段的请求。白名单适用于应用只允许特定IP访问的场景。设置白名单存在一定业务风险。一旦设置白名单，只有白名单中的IP可以访问负载均衡监听。如果开启了白名单访问，但访问策略组中没有添加任何IP，则负载均衡监听不会转发请求。 black：来自所选访问控制策略组中设置的IP地址或地址段的所有请求都不会转发。黑名单适用于应用只限制某些特定IP访问的场景。如果开启了黑名单访问，但访问策略组中没有添加任何IP， 则负载均衡监听会转发全部请求。当AclStatus参数取值为on 时，必须指定该参数。 |
|---|---|---|---|---|---|
| Protocol | String | 是 | 否 | 网络协议。 | 取值： http https tcp udp |
| ListenerPort | Integer | 是 | 否 | 负载均衡实例前端使用的端口。 | 取值范围：1~65,535。 |
| Bandwidth | Integer | 是 | 否 | 监听的带宽峰值。 | 取值范围：-1或1~1000。 单位：Mbps。 取值说明： 针对按固定带宽计费方式的公网类型实例，不同Listener上的 Bandwidth的峰值总和不能超出在创建负载均衡实例时设定的 Bandwidth值，且不能将 Listener上的Bandwidth值设置为-1。 针对按使用流量计费方式的公网类型实例，可以选择将Listener 上的Bandwidth值设置为-1，表示不限制带宽峰值。 |
| BackendServ erPort | Integer | 是 | 否 | 负载均衡实例后端使用的端口。 | 取值范围：1~65,535。 |
| LoadBalancer Id | String | 是 | 否 | 负载均衡实例的 ID。 | 无 |
| HealthCheck | Map | 否 | 否 | 健康检查设置。 | 更多信息，请参见HealthCheck属性。 |
| Persistence | Map | 否 | 是 | 相关参数的持久化。 | 更多信息，请参见Persistence属性。 |
| Scheduler | String | 否 | 否 | 调度算法。 | 取值： wrr（默认值）：权重值越高的后端服务器，被轮询到的次数（概率）也越高。 wlc：按照访问顺序依次将外部请求分发到后端服务器。 |
| CACertificateI d | String | 否 | 否 | CA证书ID。 | 只对HTTPS协议有效。 |

资源编排

| ServerCertific ateId | String | 否 | 是 | 服务器证书的 ID。 | 只对HTTPS协议有效，且必须指定该参数。 |
|---|---|---|---|---|---|
| VServerGroup Id | String | 否 | 否 | 服务器组ID。 | 无 |
| RequestTime out | Integer | 否 | 否 | 请求超时时间。 | 取值范围：1~180。 单位：秒。 |
| IdleTimeout | Integer | 否 | 否 | 连接空闲超时时间。 | 取值范围：1~60。 单位：秒。 |
| HttpConfig | Map | 否 | 否 | 用于配置HTTP 协议。 | 更多信息，请参见HttpConfig属性。 |
| Description | String | 否 | 否 | 监听的描述信息。 | 长度为1~80个字符。可包含英文字母、汉字、数字、短划线（-）、正斜线（/）、半角句号（.）和下划线 （ ）。 _ |
| PortRange | List | 否 | 否 | 监听的端口范围。 | 目前仅支持开启全端口监听，即 StartPort=1，EndPort=65,535 。 更多信息，请参见PortRange属性。 |
| StartListener | Boolean | 否 | 否 | 是否启动监听器。 | 取值： true（默认值）：启动。 false：不启动。 |

**HealthCheck 语法**

```json
"HealthCheck": {
  "Domain": String,
  "Interval": Integer,
  "URI": String,
  "HttpCode": String,
  "HealthyThreshold": Integer,
  "HealthCheckType": String,
  "Timeout": Integer,
  "UnhealthyThreshold": Integer,
  "Port": Integer,
  "Switch": String,
  "HealthCheckMethod": String
}
```

**HealthCheck属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|

资源编排

| Domain | String | 否 | 否 | 用于健康检查的域名。 | 取值： $ ip _ 用户自定义字符串：长度为 1~80个字符。可包含英文字母、数字、短划线（-）和半角句号（.）。 空说明用户设置此参数为$ ip或空时，负载均衡会使 _ 用各后端服务器的私网IP作为健康检查使用的域名。 |
|---|---|---|---|---|---|
| Interval | Integer | 否 | 否 | 健康检查的时间间隔。 | 取值范围：1~5。 单位：秒。 |
| URI | String | 否 | 否 | 用于健康检查的 URI。 | 长度为1~80个字符。必须以正斜线 （/）开头，可包含英文字母、数字、短划线（-）、正斜线（/）、半角句号（.）、百分号（%）、问号 （?）、井号（#）和and（&）。 |
| HttpCode | String | 否 | 否 | HTTP状态码。 | 取值： http 2xx（默认值） _ http 3xx _ http 4xx _ http 5xx _ 多个HTTP状态码之间用半角逗号 （,）分隔。 |
| HealthyThres hold | Integer | 否 | 否 | 判定健康检查结果为success的阈值。即，健康检查连续成功多少次后，将后端服务器的健康检查状态由fail改为success。 | 取值范围：1~10。 |
| HealthCheckT ype | String | 否 | 否 | 健康检查类型。 | 取值： tcp http |
| Timeout | Integer | 否 | 否 | 每次健康检查响应的最大超时时间。 | 取值范围：1~50。 单位：秒。 说明如果Timeout值小于Interval值，则Timeout 无效，超时时间为Interval的值。 |
| UnhealthyThr eshold | Integer | 否 | 否 | 判定健康检查结果为fail的阈值。即，健康检查连续失败多少次后，将后端服务器的健康检查状态由success 改为fail。 | 取值范围：1~10。 |
| Port | Integer | 否 | 否 | 用于健康检查的端口。 | 取值范围：0~65,535。 |

资源编排

| Switch | String | 否 | 否 | 是否启用健康检查。 | 取值： on：启用。 off：禁用。 说明当前仅对HTTP或 HTTPS协议有效。如果未设置 Switch，默认将禁用健康检查，除非已经配置了健康检查项目。 |
|---|---|---|---|---|---|
| HealthCheck Method | String | 否 | 否 | 健康检查方法。 | 取值： head get 说明当Protocol取值为https或http，且Switch取值为on时，该参数有效。 |

**Persistence语法**

```json
"Persistence": {
  "PersistenceTimeout": Integer,
  "CookieTimeout": Integer,
  "XForwardedFor": String,
  "XForwardedFor_SLBID": String,
  "XForwardedFor_proto": String,
  "XForwardedFor_SLBIP": String,
  "Cookie": String,
  "StickySession": String,
  "StickySessionType": String,
  "XForwardedFor_ClientSrcPort": String,
  "XForwardedFor_SLBPORT": String
}
```

**Persistence属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| StickySession | String | 否 | 是 | 是否开启会话保持。 | 取值： on：开启。 off：关闭。 |
| PersistenceTi meout | Integer | 否 | 是 | 连接持久化的超时时间。 | 取值范围：0~1000。 默认值：0。表示关闭。 单位：秒。 |
| CookieTimeo ut | Integer | 否 | 是 | Cookie超时时间。 | 取值范围：1~86,400。 单位：秒。 说明当 StickySession为on且 StickySessionType为insert 时，该参数必选。 |

资源编排

| XForwardedF or | String | 否 | 是 | 是否通过X- Forwarded- Fort头字段获取来访者真实IP。 | 取值： on：通过X-Forwarded-Fort头字段获取来访者真实IP。 off（默认值）：不通过X- Forwarded-Fort头字段获取来访者真实IP。 |
|---|---|---|---|---|---|
| XForwardedF or proto _ | String | 否 | 是 | 是否通过X- Forwarded- Proto头字段获取负载均衡实例的监听协议。 | 取值： on：通过X-Forwarded-Proto头字段获取负载均衡实例的监听协议。 off（默认值）：不通过X- Forwarded-Proto头字段获取负载均衡实例的监听协议。 |
| XForwardedF or SLBID _ | String | 否 | 是 | 是否通过SLB- ID头字段获取负载均衡实例 ID。 | 取值： on：通过SLB-ID头字段获取负载均衡实例ID。 off（默认值）：不通过SLB-ID头字段获取负载均衡实例ID。 |
| XForwardedF or SLBIP _ | String | 否 | 是 | 是否通过SLB- IP头字段获取客户端请求的真实 IP。 | 取值： on：通过SLB-IP头字段获取客户端请求的真实IP。 off（默认值）：不通过SLB-IP头字段获取客户端请求的真实IP。 |
| Cookie | String | 否 | 是 | 服务器上配置的 Cookie。 | 长度为1~200个字符，不能以美元符号（$）开头。可包含英文字母和数字，不能包含半角逗号（,）、半角分号（;）和空格（ ）。 说明当 StickySession为on且 StickySessionType为server 时，该参数必选。 |
| StickySession Type | String | 否 | 是 | Cookie的处理方式。 | 取值： insert：植入Cookie。 server：重写Cookie。 说明当 StickySession的值为on时， 必须指定该参数。 |
| XForwardedF or ClientSrcP _ ort | String | 否 | 是 | 是否通过X- Forwarded- Client-srcport 头字段获取客户端连接负载均衡实例所使用的端口。 | 取值： on：通过X-Forwarded-Client- srcport头字段获取客户端连接负载均衡实例所使用的端口。 off（默认值）：不通过X- Forwarded-Client-srcport头字段获取客户端连接负载均衡实例所使用的端口。 |
| XForwardedF or SLBPORT _ | String | 否 | 是 | 是否通过X- Forwarded- Proto头字段获取SLB实例使用的监听协议。 | 取值： on：通过X-Forwarded-Proto头字段获取SLB实例使用的监听协议。 off（默认值）：不通过X- Forwarded-Proto头字段获取 SLB实例使用的监听协议。 |

**HttpConfig语法**

资源编排

```json
"HttpConfig": {
  "ForwardPort": Integer,
  "ListenerForward": String
}
```

**HttpConfig属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ForwardPort | Integer | 否 | 否 | HTTP到HTTPS 监听转发端口。 | 取值范围：1~65,535。 默认值：443。 |
| ListenerForw ard | String | 否 | 否 | 是否将HTTP启用为HTTPS转发。 | 取值： on：启用。 off（默认值）：禁用。 |

**PortRange语法**

```json
"PortRange": [
  {
    "StartPort": Integer,
    "EndPort": Integer
  }
```

]

**PortRange属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| StartPort | Integer | 是 | 否 | 起始端口。 | 取值：1。 |
| EndPort | Integer | 是 | 否 | 结束端口。 | 取值：65,535。 |

**返回值**

Fn::GetAtt LoadBalancerId：负载均衡实例的唯一标识。 ListenerPortsAndProtocol：负载均衡实例前端使用的端口和协议。

**示例**

`JSON` 格式资源编排

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "LoadBalancerId": {
      "Type": "String",
```

`"Label": "`负载均衡实例的`ID",`

```json
      "Default": "slb-*****"
    }
  },
  "Resources": {
    "SlbListener": {
      "Type": "ALIYUN::SLB::Listener",
      "Properties": {
        "Persistence": {
          "CookieTimeout": 60,
          "StickySession": "on",
          "PersistenceTimeout": 180,
          "XForwardedFor": "off",
          "StickySessionType": "insert"
        },
        "ListenerPort": 80,
        "Bandwidth": -1,
        "HealthCheck": {
          "HttpCode": "http_2xx,http_3xx,http_4xx,http_5xx",
          "HealthCheckType": "tcp",
          "UnhealthyThreshold": 3,
          "Timeout": 5,
          "HealthyThreshold": 3,
          "Port": 80,
          "URI": "/",
          "Interval": 2
        },
        "LoadBalancerId": {
          "Ref": "LoadBalancerId"
        },
        "BackendServerPort": 80,
        "Protocol": "tcp"
      }
    }
  },
  "Outputs": {
  }
}
```

更多示例，请参见创建负载均衡监听、克隆负载均衡实例、上传证书、创建扩展域名、创建服务器组并添加后端服务器到负载均衡实例、为HTTP或HTTPS监听添加转发规则和将后端服务器添加到服务器组的组合示例：JSON示例和YAML示例。

#### ALIYUN::SLB::LoadBalancer

**语法**

资源编排

```json
{
  "Type": "ALIYUN::SLB::LoadBalancer",
  "Properties": {
    "DeletionProtection": Boolean,
    "AddressType": String,
    "Tags": List,
    "InternetChargeType": String,
    "Bandwidth": Integer,
    "SlaveZoneId": String,
    "ResourceGroupId": String,
    "AutoPay": Boolean,
    "VpcId": String,
    "PricingCycle": String,
    "LoadBalancerName": String,
    "Duration": Number,
    "VSwitchId": String,
    "LoadBalancerSpec": String,
    "MasterZoneId": String,
    "PayType": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ResourceGroupI d | String | 否 | 否 | 资源组ID。 | 无。 |
| DeletionProtecti on | Boolean | 否 | 否 | 删除保护。 | 取值范围： true false |
| VpcId | String | 否 | 否 | 专有网络ID。 | 无。 |
| SlaveZoneId | String | 否 | 否 | 该创建实例的备可用区ID。 | 无。 |

资源编排

| Bandwidth | Integer | 否 | 否 | 按固定带宽计费方式的公网类型实例的带宽峰值。 | 针对按固定带宽计费方式的公网类型实例，需要将当前设定值通过 Listener中的 Bandwidth参数进行分配后才能生效；针对按使用流量计费方式的公网类型实例的带宽峰值，请直接通过 Listener上 Bandwidth参数进行设定，此时本参数会被忽略。 取值范围： 1~1000（单位为 Mbps）。 默认值：1。 专有网络实例系统会统一按流量计费设置。 |
|---|---|---|---|---|---|
| AddressType | String | 否 | 否 | Address 类型。 | 取值范围： internet intranet 默认值： internet。 |
| VSwitchId | String | 否 | 否 | 专有网络下的虚拟交换机ID。 | 无。 |
| LoadBalancerNa me | String | 否 | 否 | 负载均衡实例的名称。 | 用户自定义字符串。长度限制为1- 80个字节，允许包含字母、数字、连字符（-)、正斜线 （/）、点号 （.）、和下划线 （ ）。不指定该 _ 参数时，默认由系统分配一个实例名称。 |
| InternetChargeT ype | String | 否 | 否 | 公网类型实例付费方式。 | 取值范围： paybybandwi dth paybytraffic 默认值： paybytraffic。 |
| MasterZoneId | String | 否 | 否 | 实例的主可用区 ID。 | 无 。 |

资源编排

| Tags | List | 否 | 否 | 负载均衡实例绑定的Tag列表，其结构是一个Json List，包含TagKey 和TagValue。 | 最多5个。 |
|---|---|---|---|---|---|
| LoadBalancerSp ec | String | 否 | 否 | 负载均衡实例的规格。 | 取值范围： slb.s1.small slb.s2.small slb.s2.mediu m slb.s3.small slb.s3.mediu m slb.s3.large 每个地域支持的规格不同。 |
| AutoPay | Boolean | 否 | 否 | 是否是自动支付预付费公网实例的账单。 | 取值范围： true false 默认值：false。 说明仅适用于中国站。 |
| PayType | String | 否 | 否 | 实例的计费类型。 | 取值范围： PayOnDeman d：按量付费 PrePay：预付费 |
| PricingCycle | String | 否 | 否 | 预付费公网实例的计费周期。 | 取值范围： month year 说明仅适用于中国站。 |
| Duration | Number | 否 | 否 | 预付费公网实例的购买时长。 | 取值范围： 如果 PricingCycle为 month，取值为 1~9。 如果 PricingCycle为 year，取值为 1~3。 说明仅适用于中国站。 |

**Tags 语法**

资源编排

```json
"Tags": [
  {
    "Value": String ,
    "Key": String
  }
```

]

**Tags 属性**

| 名称 | 类型 | 是否必需 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Key | String | 是 | 否 | 无。 | 无。 |
| Value | String | 否 | 否 | 无。 | 无。 |

**返回值**

**Fn::GetAtt**

LoadBalancerId：负载均衡实例的唯一标识。 NetworkType：负载均衡实例的网络类型，即vpc或classic。 AddressType：Address类型，即intranet或internet。 IpAddress：负载均衡实例的IP。 OrderId：订单ID。

**示例**

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "CreateLoadBalance": {
      "Type": "ALIYUN::SLB::LoadBalancer",
      "Properties": {
        "LoadBalancerName": "createdByHeat",
        "AddressType": "internet",
        "InternetChargeType": "paybybandwidth",
      }
    }
  },
  "Outputs": {
    "LoadBalanceDetails": {
      "Value": {
        "Fn::GetAtt": ["CreateLoadBalance", "LoadBalancerId"]}
    }
  }
}
```

#### ALIYUN::SLB::LoadBalancerClone

**语法**

资源编排

```json
{
  "Type": "ALIYUN::SLB::LoadBalancerClone",
  "Properties": {
    "Tags": List,
    "ResourceGroupId": String,
    "VSwitchId": String,
    "LoadBalancerName": String,
    "SourceLoadBalancerId": String,
    "TagsPolicy": String,
    "BackendServersPolicy": String,
    "BackendServers": List,
    "InstanceChargeType": String,
    "LoadBalancerSpec": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ResourceGroupI d | String | 否 | 否 | 资源组ID。 | 无 |
| VSwitchId | String | 否 | 否 | 交换机ID。 | 必须为源负载均衡实例所属专有网络下的交换机。不指定该参数时，将使用源负载均衡实例的交换机。 |
| SourceLoadBala ncerId | String | 是 | 否 | 将要克隆的负载均衡实例ID。 | 无 |
| BackendServers Policy | String | 否 | 否 | 克隆策略，指定配置新负载均衡实例需要监听的ECS实例以及各ECS实例的权重。 | 取值： clone（默认值）：把源负载均衡实例中监听的ECS实例和权重配置全部克隆到新的负载均衡实例中。 empty：不给新的负载均衡实例添加任何ECS实例。 append：既克隆源负载均衡实例中监听的ECS 实例和权重配置，也添加新的 ECS实例和权重配置到新的负载均衡实例。 replace：只添加新的ECS实例列表和权重配置而不克隆源负载均衡实例所监听的ECS实例列表和权重配置。 |
| BackendServers | List | 否 | 是 | 指定新添加的需要监听的ECS实例列表。 | 详情请参见BackendServe rs属性。 |

资源编排

| LoadBalancerNa me | String | 否 | 否 | 负载均衡实例名称。 | 用户自定义字符串。长度为1~80 个字符，可包含英文字母、数字、短划线（-）、正斜线 （/）、英文句点 （.）和下划线 （ ）。 _ |
|---|---|---|---|---|---|
| Tags | List | 否 | 否 | SLB实例标签。 | 标签以键值对方式传入，最多可以设置5组标签。 详情请参见Tags属性。 |
| TagsPolicy | String | 否 | 否 | 标签策略。 | 取值： clone：使用源负载均衡实例的标签。 empty（默认值）：不设置标签。 append：保留源实例标签并添加新标签。 replace：添加新标签，不保留源实例标签 。 |
| InstanceChargeT ype | String | 否 | 否 | 实例计费方式。 | 取值： PayBySpec（ 默认值）：按规格计费。 PayByCLCU： 按量计费。 说明当 PayType （实例付费模式） 取值为 PayOnDe mand（按量付费） 时，该参数生效。 |
| LoadBalancerSp ec | String | 否 | 否 | 负载均衡实例的规格。 | 取值： slb.s1.small（ 默认值） slb.s2.small slb.s2.mediu m slb.s3.small slb.s3.mediu m slb.s3.large slb.s3.xlarge slb.s3.xxlarge 不同地域支持的规格不同。 |

**BackendServers语法**

资源编排

```json
"BackendServers": [
  {
    "Type": String,
    "ServerId": String,
    "Description": String,
    "ServerIp": String,
    "Weight": Integer
  }
```

]

**BackendServers属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ServerId | String | 是 | 是 | 后端服务器ID。 | 后端服务器（ECS 实例）必须在运行中才可以加入负载均衡实例，每次调用最多可添加20个后端服务器。 只有性能保障型实例支持添加eni类型的后端服务器。 |
| Weight | Integer | 是 | 是 | ECS实例在负载均衡实例中的权重。 | 取值范围： 0~100。 默认值：100。 |
| ServerIp | String | 否 | 否 | 后端服务器IP地址。 | 无 |
| Type | String | 否 | 否 | 后端服务器类型。 | 取值： ecs：ECS实例 （默认值）。 eni：弹性网卡实例。 eci：弹性容器实例。 |
| Description | String | 否 | 是 | 后端服务器描述。 | 长度为1~80个字符，可包含英文字母、汉字、数字、 短划线（-）、正斜线（/）、英文句点 （.）和下划线 （ ）。 _ |

**Tags语法**

```json
"Tags": [
  {
    "Value": String,
    "Key": String
  }
```

]

**Tags属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|

资源编排

| Key | String | 是 | 否 | 标签键。 | 长度为1~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |  |  |
|---|---|---|---|---|---|---|---|
| Value | String | 否 | 否 | 标签值。 | 长度为0~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或者 https:// 。 |  |  |

|  | aliyun |
|---|---|
| acs: |  |

|  | aliyun |
|---|---|
| acs: |  |

**返回值**

Fn::GetAtt LoadBalancerId：新负载均衡实例的ID。

**示例**

`YAML` 格式

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  SourceSLBId:
    AssociationProperty: ALIYUN::SLB::Instance::InstanceId
    Type: String
    Description: Source load balancer id to clone
Resources:
  LoadBalancerClone:
    Properties:
      LoadBalancerName: DemoCloneLoadBalancer
      SourceLoadBalancerId:
        Ref: SourceSLBId
Outputs:
  LoadBalancerId:
    Description: The id of load balance generated
    Value:
      Fn::GetAtt:
        - LoadBalancerId
```

`JSON` 格式资源编排

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "SourceSLBId": {
      "AssociationProperty": "ALIYUN::SLB::Instance::InstanceId",
      "Type": "String",
      "Description": "Source load balancer id to clone"
    }
  },
  "Resources": {
    "LoadBalancerClone": {
      "Type": "ALIYUN::SLB::LoadBalancerClone",
      "Properties": {
        "LoadBalancerName": "DemoCloneLoadBalancer",
        "SourceLoadBalancerId": {
          "Ref": "SourceSLBId"
        }
      }
    }
  },
  "Outputs": {
    "LoadBalancerId": {
      "Description": "The id of load balance generated",
      "Value": {
        "Fn::GetAtt": [
          "LoadBalancerClone",
          "LoadBalancerId"
```

]

```
      }
    }
  }
}
```

#### ALIYUN::SLB::MasterSlaveServerGroup

ALIYUN::SLB::MasterSlaveServerGroup类型用于创建主备服务器组。

**重要**

一个主备服务器组只能包含两个ECS实例，一个为主服务器，另一个为备服务器。

**语法**

```json
{
  "Type": "ALIYUN::SLB::MasterSlaveServerGroup",
  "Properties": {
    "MasterSlaveServerGroupName": String,
    "MasterSlaveBackendServers": List,
    "LoadBalancerId": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| MasterSlaveServ erGroupName | String | 否 | 否 | 主备服务器组名称 | 无 |

资源编排

| MasterSlaveBac kendServers | List | 是 | 否 | 主备服务器组列表 | 最多可包含2个后端服务器。如果不指定该参数，则创建一个空的主备服务器组列表。 |
|---|---|---|---|---|---|
| LoadBalancerId | String | 是 | 否 | 负载均衡实例ID | 无 |

**MasterSlaveBackendServers语法**

```json
"MasterSlaveBackendServers": [
  {
    "ServerId": String,
    "Port": Integer,
    "Weight": Integer,
    "ServerType": String
  }
```

]

**MasterSlaveBackendServers属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ServerId | String | 是 | 否 | 要添加的ECS实例 ID或者ENI的实例 ID | 无 |
| ServerType | String | 否 | 否 | 服务器类型 | 取值： Master（默认值） Slave |
| Port | Integer | 是 | 否 | 后端服务器使用的端口 | 取值范围： 1~65535 |
| Weight | Integer | 是 | 否 | 后端服务器的权重 | 取值范围： 0~100 |

**返回值**

Fn::GetAtt MasterSlaveServerGroupId：主备服务器组ID。

**示例**

资源编排

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "MasterSlaveServerGroup": {
      "Type": "ALIYUN::SLB::MasterSlaveServerGroup",
      "Properties": {
        "MasterSlaveServerGroupName": "Group1",
        "MasterSlaveBackendServers": [
          {
            "ServerId": "vm****",
            "Port": "80",
            "Weight": "100",
            "ServerType": "Master"
          },
          {
            "ServerId": "vm****",
            "Port": "90",
            "Weight": "100",
            "ServerType": "Slave"
          }
```

`],`

```json
        "LoadBalancerId": "lb-bp1hv944r69al4j9j****"
      }
    }
  },
  "Outputs": {
    "MasterSlaveServerGroupId": {
      "Value": {
        "Fn::GetAtt": [
          "MasterSlaveServerGroup",
          "MasterSlaveServerGroupId"
```

]

```
      }
    }
  }
}
```

#### ALIYUN::SLB::Rule

**语法**

```json
{
  "Type": "ALIYUN::SLB::Rule",
  "Properties": {
    "ListenerPort": Integer,
    "RuleList": List,
    "LoadBalancerId": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ListenerPort | Integer | 是 | 否 | 负载均衡实例前端使用的监听端口 | 取值范围： 1~65535。 |

资源编排

| RuleList | List | 是 | 否 | 要添加的转发规则 | 一次请求中，最多可添加10条转发规则。 每条转发规则包含以下参数： RuleName Domain Url VServerGroup Id Domain和URL两者必须指定一个， 也可以同时指定。 Domain和URL的组合在同一个监听内必须唯一。 |
|---|---|---|---|---|---|
| LoadBalancerId | String | 是 | 否 | 负载均衡实例ID | 无 |

**RuleList语法**

```json
"RuleList": [
  {
    "Url": String,
    "Domain": String,
    "VServerGroupId": String,
    "RuleName": String
  }
```

]

**RuleList属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Url | String | 否 | 否 | 访问路径 | 长度为2~80个字符。 以正斜线（/） 开头，可包含字母、数字和以下特殊字符： -/.%?#& |
| Domain | String | 否 | 否 | 转发规则关联的请求域名 | 无 |
| VServerGroupId | String | 是 | 否 | 该转发规则的目标虚拟服务器组ID | 无 |
| RuleName | String | 是 | 否 | 转发规则名称 | 长度为1~40个字符，可包含字母、 数字和以下特殊字符： -/. _ 同一个监听内不同规则的名称必须唯一。 |

**返回值**

Fn::GetAtt 资源编排 Rules：转发规则列表。

**示例**

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "Rule": {
      "Type": "ALIYUN::SLB::Rule",
      "Properties": {
        "ListenerPort": {
          "Ref": "ListenerPort"
        },
        "RuleList": {
          "Fn::Split": [",", {
            "Ref": "RuleList"
          }, {
            "Ref": "RuleList"
          }]
        },
        "LoadBalancerId": {
          "Ref": "LoadBalancerId"
        }
      }
    }
  },
  "Parameters": {
    "ListenerPort": {
      "Type": "Number",
      "Description": "The front-end HTTPS listener port of the Server Load Balancer instance. Valid v
alue:\n1-65535",
      "MaxValue": 65535,
      "MinValue": 1
    },
    "RuleList": {
      "MinLength": 1,
      "Type": "CommaDelimitedList",
      "Description": "The forwarding rules to add.",
      "MaxLength": 10
    },
    "LoadBalancerId": {
      "Type": "String",
      "Description": "The ID of Server Load Balancer instance."
    }
  },
  "Outputs": {
    "Rules": {
      "Description": "A list of forwarding rules. Each element of rules contains \"RuleId\".",
      "Value": {
        "Fn::GetAtt": ["Rule", "Rules"]
      }
    }
  }
}
```

#### ALIYUN::SLB::VServerGroup

ALIYUN::SLB::VServerGroup类型用于创建服务器组并添加后端服务器到负载均衡实例。

**语法**

资源编排

```json
{
  "Type": "ALIYUN::SLB::VServerGroup",
  "Properties": {
    "VServerGroupName": String,
    "BackendServers": List,
    "LoadBalancerId": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| VServerGroup Name | String | 是 | 否 | 服务器组名称。 | 无 |
| BackendServ ers | List | 否 | 是 | 后端服务器列表。 | 最多添加20个ECS实例。 更多信息，请参见BackendServers属性。 |
| LoadBalancer Id | String | 是 | 否 | 负载均衡实例 ID。 | 无 |

**BackendServers语法**

```json
"BackendServers": [
  {
    "ServerId": String,
    "Port": Integer,
    "Weight": Integer,
    "Type": String,
    "Description": String,
    "ServerIp": String
  }
```

]

**BackendServers属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ServerId | String | 是 | 是 | 后端服务器的实例ID。 | 无 |
| Port | Integer | 是 | 是 | 后端服务器使用的端口。 | 取值范围：1~65,535。 |
| Weight | Integer | 否 | 是 | 后端服务器的权重。 | 取值范围：0~100。 |
| Type | String | 否 | 是 | 后端服务器类型。 | 取值： ecs（默认值）：ECS实例。 eni：弹性网卡实例。 |
| Description | String | 否 | 是 | 后端服务器描述。 | 长度为1~80个字符，支持英文字母、汉字、数字、短划线（-）、正斜线（/）、半角句号（.）和下划线 （ ）。 _ |
| ServerIp | String | 否 | 是 | 后端服务器的IP 地址。 | ECS或者ENI的实例IP。 |

**返回值**

资源编排 Fn::GetAtt VServerGroupId：服务器组的ID。 BackendServers：添加到负载均衡实例的后端服务器列表。

**示例**

`JSON` 格式

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "VServerGroupName": {
      "Type": "String",
      "Description": "Display name of the VServerGroup."
    },
    "LoadBalancerId": {
      "Type": "String",
      "Description": "The id of load balancer."
    },
    "BackendServers": {
      "Type": "Json",
      "Description": "The list of a combination of ECS Instance-Port-Weight.Same ecs instance with di
fferent port is allowed, but same ecs instance with same port isn't."
    }
  },
  "Resources": {
    "VServerGroup": {
      "Type": "ALIYUN::SLB::VServerGroup",
      "Properties": {
        "VServerGroupName": {
          "Ref": "VServerGroupName"
        },
        "LoadBalancerId": {
          "Ref": "LoadBalancerId"
        },
        "BackendServers": {
          "Ref": "BackendServers"
        }
      }
    }
  },
  "Outputs": {
    "VServerGroupId": {
      "Description": "The id of VServerGroup created.",
      "Value": {
        "Fn::GetAtt": [
          "VServerGroup",
          "VServerGroupId"
```

]

```json
      }
    },
    "BackendServers": {
      "Description": "Backend server list in this VServerGroup.",
      "Value": {
        "Fn::GetAtt": [
          "VServerGroup",
          "BackendServers"
```

]

```
      }
    }
  }
}
```

资源编排 `YAML` 格式

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  VServerGroupName:
    Type: String
    Description: Display name of the VServerGroup.
  LoadBalancerId:
    Type: String
    Description: The id of load balancer.
  BackendServers:
    Type: Json
    Description: >-
      The list of a combination of ECS Instance-Port-Weight.Same ecs instance
      with different port is allowed, but same ecs instance with same port
      isn't.
Resources:
  VServerGroup:
    Properties:
      VServerGroupName:
        Ref: VServerGroupName
      LoadBalancerId:
        Ref: LoadBalancerId
      BackendServers:
        Ref: BackendServers
Outputs:
  VServerGroupId:
    Description: The id of VServerGroup created.
    Value:
      'Fn::GetAtt':
        - VServerGroupId
  BackendServers:
    Description: Backend server list in this VServerGroup.
    Value:
      'Fn::GetAtt':
        - BackendServers
```

更多示例，请参见创建负载均衡监听、克隆负载均衡实例、上传证书、创建扩展域名、创建服务器组并添加后端服务器到负载均衡实例、为HTTP或HTTPS监听添加转发规则和将后端服务器添加到服务器组的组合示例：JSON示例和YAML示例。

### SLS

#### ALIYUN::SLS::Index

**语法**

```json
{
  "Type": "ALIYUN::SLS::Index",
  "Properties": {
    "ProjectName": String,
    "FullTextIndex": Map,
    "LogstoreName": String,
    "KeyIndices": List,
    "LogReduce": Boolean
  }
}
```

资源编排

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ProjectName | String | 是 | 否 | 日志项目名称。 | 长度为3~36个字符。必须以小写字母或数字开头和结尾，可包含小写字母、数字、短划线（-）和下划线 （ ）。 _ |
| FullTextIndex | Map | 是 | 是 | 全文索引配置。 | 详情请参见FullTextIndex属性。 |
| LogstoreNam e | String | 是 | 否 | 日志库名称。 | 无 |
| KeyIndices | List | 否 | 是 | 字段索引配置。 | 全文索引和字段索引至少配置一个。 详情请参见属性。 |
| LogReduce | Boolean | 否 | 是 | 是否启用日志分割。 | 取值： true false（默认值） |

**FullTextIndex语法**

```json
"FullTextIndex": {
  "CaseSensitive": Boolean,
  "Delimiter": String,
  "IncludeChinese": Boolean,
  "Enable": Boolean
}
```

**FullTextIndex属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Enable | Boolean | 是 | 是 | 是否启用全文索引。 | 取值： true（默认值） false |
| CaseSensitive | Boolean | 否 | 是 | 是否区分大小写。 | 取值： true false（默认值） |
| Delimiter | String | 否 | 是 | 分词符。 | 支持以下特殊字符： ,'";=()[]{}?@& <>/:\n\t\r |
| IncludeChines e | Boolean | 否 | 是 | 是否包含中文。 | 取值： true false（默认值） |

**KeyIndices语法**

资源编排

```json
"KeyIndices": [
  {
    "Name": String,
    "EnableAnalytics": Boolean,
    "Delimiter": String,
    "CaseSensitive": Boolean,
    "JsonKeyIndices": List,
    "Alias": String,
    "IncludeChinese": String,
    "Type": String
  }
```

]

**KeyIndices属性**

| 属性名称 | 类型 |  | 必须 |  |  | 允许更新 |  |  | 描述 |  | 约束 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Name | String |  | 是 |  |  | 是 |  |  | 字段名。 |  | 可以使用嵌套名，以英文句点（.） 分隔，例如：k1.k2.k3。 |  |
| EnableAnalyti cs | Boolean |  | 否 |  |  | 是 |  |  | 该字段是否开启统计。 |  | 取值： true（默认值） false |  |
| Delimiter | String |  | 否 |  |  | 是 |  |  | 分词符。 |  | 支持以下特殊字符： ,'";=()[]{}?@& <>/:\n\t\r |  |
| CaseSensitive | Boolean |  | 否 |  |  | 是 |  |  | 是否区分大小写。 |  | 取值： true false（默认值） 只有当Type参数取值为 text 或 json 时该参数生效。 |  |
| JsonKeyIndice s | List |  | 否 |  |  | 是 |  |  | JSON索引配置。格式： [{"key1 |  |  |  |
|  |  |  |  |  |  |  |  |  |  | [{"key1 | 支持的key为：Name、Alias、 |  |
|  |  |  |  |  |  |  |  |  | ": |  | 支持的key为：Name、Alias |  |
|  |  |  |  |  |  |  |  |  |  |  | Type和EnableAnalytics。 |  |
|  |  |  |  |  |  |  |  |  | "value1", |  | 详情请参见JsonKeyIndice |  |
|  |  |  |  |  |  |  |  |  |  |  | 详情请参见J |  |
|  |  |  |  |  |  |  |  |  | "key2": |  |  |  |
|  |  |  |  |  |  |  |  |  | "value2", |  |  |  |
|  |  |  |  |  |  |  |  |  | ...}] |  |  |  |
| Alias | String |  | 否 |  |  | 是 |  |  | 字段别名。 |  | 无 |  |
| IncludeChines e | Boolean |  | 否 |  |  | 是 |  |  | 是否包含中文。 |  | 取值： true false（默认值） 只有当Type参数取值为text时该参数生效。 |  |
| Type | String |  | 是 |  |  | 是 |  |  | 字段类型。 |  | 取值： text （默认值） long double json |  |

资源编排

**JsonKeyIndices语法**

```json
"JsonKeyIndices": [
  {
    "Type": String,
    "Alias": String,
    "EnableAnalytics": Boolean,
    "Name": String
  }
```

]

**JsonKeyIndices属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Name | String | 是 | 是 | 字段名。 | 无 |
| EnableAnalyti cs | Boolean | 否 | 是 | 是否支持查询分析。 | 取值： true false |
| Alias | String | 否 | 是 | 字段别名。 | 无 |
| Type | String | 是 | 是 | 字段类型。 | 无 |

**返回值**

Fn::GetAtt 无。

**示例**

`JSON` 格式

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "Index": {
      "Type": "ALIYUN::SLS::Index",
      "Properties": {
        "ProjectName": {
          "Ref": "ProjectName"
        },
        "FullTextIndex": {
          "Ref": "FullTextIndex"
        },
        "LogstoreName": {
          "Ref": "LogstoreName"
        },
        "KeyIndices": {
          "Ref": "KeyIndices"
        },
        "LogReduce": {
          "Ref": "LogReduce"
        }
      }
    }
  },
  "Parameters": {
    "ProjectName": {
      "Type": "String",
      "Description": "Project name:1. Only supports lowercase letters, numbers, hyphens (-) and under
scores()2 Muststartandendwithlowercaselettersandnumbers3 Thenamelengthis3-63charac
```

资源编排

```json
scores (_).2. Must start and end with lowercase letters and numbers.3. The name length is 363 charac ters.",
      "MinLength": 3,
      "MaxLength": 63
    },
    "FullTextIndex": {
      "Type": "Map",
      "Description": "Full-text indexing configuration.Full-text indexing and key indexing must have
at least one enabled."
    },
    "LogstoreName": {
      "Type": "String",
      "Description": "Logstore name:1. Only supports lowercase letters, numbers, hyphens (-) and unde
rscores (_).2. Must start and end with lowercase letters and numbers.3. The name length is 3-63 chara cters.",
      "MinLength": 3,
      "MaxLength": 63
    },
    "KeyIndices": {
      "Type": "List",
      "Description": "Key index configurations.Full-text indexing and key indexing must have at least
one enabled."
    },
    "LogReduce": {
      "Default": false,
      "Type": "Boolean",
      "Description": "Whether to enable log reduce. Default to false.",
      "AllowedValues": [
        true,
        false
```

]

```
    }
  }
}
```

`YAML` 格式资源编排

```
ROSTemplateFormatVersion: '2015-09-01' Resources:
  Index:
    Properties:
      ProjectName:
        Ref: ProjectName
      FullTextIndex:
        Ref: FullTextIndex
      LogstoreName:
        Ref: LogstoreName
      KeyIndices:
        Ref: KeyIndices
      LogReduce:
        Ref: LogReduce
Parameters:
  ProjectName:
    MinLength: 3
    MaxLength: 63
    Type: String
    Description: Project name:1. Only supports lowercase letters, numbers, hyphens
      (-) and underscores (_).2. Must start and end with lowercase letters and numbers.3.
      The name length is 3-63 characters.
  FullTextIndex:
    Type: Map
    Description: Full-text indexing configuration.Full-text indexing and key indexing
      must have at least one enabled.
  LogstoreName:
    MinLength: 3
    MaxLength: 63
    Type: String
    Description: Logstore name:1. Only supports lowercase letters, numbers, hyphens
      (-) and underscores (_).2. Must start and end with lowercase letters and numbers.3.
      The name length is 3-63 characters.
  KeyIndices:
    Type: List
    Description: Key index configurations.Full-text indexing and key indexing must
      have at least one enabled.
  LogReduce:
    Default: false
    Type: Boolean
    Description: Whether to enable log reduce. Default to false.
    AllowedValues:
    - true
    - false
```

#### ALIYUN::SLS::Logstore

**语法**

资源编排

```json
{
  "Type": "ALIYUN::SLS::Logstore",
  "Properties": {
    "ProjectName": String,
    "ShardCount": Integer,
    "AutoSplit": Boolean,
    "MaxSplitShard": Integer,
    "LogstoreName": String,
    "AppendMeta": Boolean,
    "TTL": Integer,
    "EnableTracking": Boolean,
    "PreserveStorage": Boolean,
    "EncryptConf": Map
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ProjectName | String | 是 | 否 | 要创建的日志库所属日志项目的名称。 | 长度为3~36个字符。 支持小写英文字母、数字、短划线 （-）、下划线（ ）。必须以小写英 _ 文字母或数字开头和结尾。 |
| ShardCount | Integer | 否 | 是 | 分区个数。 | 取值范围：1~100。 默认值：2。 单位：个。 |
| MaxSplitShar d | Integer | 否 | 是 | 自动分裂时，分裂出最大的分区个数。 | 取值范围：1~64。 当autoSplit为true时，必须指定 MaxSplitShard。 |
| LogstoreNam e | String | 是 | 否 | 日志库的名称。 | 在一个日志项目中，日志库的名称必须具有唯一性。 长度为3~36个字符。 支持小写英文字母、数字、短划线（-）、下划线（ ）。 _ 必须以小写英文字母或数字开头和结尾。 |
| AutoSplit | Boolean | 否 | 是 | 是否自动分裂分区。 | 取值： true：自动分裂分区。 false（默认值）：不自动分裂分区。 |
| TTL | Integer | 否 | 是 | 数据的保存时间。 | 取值范围：1~3600。 默认值：30。 单位：天。 |
| EnableTracki ng | Boolean | 否 | 是 | 是否开启 WebTracking 采集信息。 | 支持采集各种浏览器以及iOS或 Android App的信息。 取值： true：开启WebTracking采集信息。 false（默认值）：不开启 WebTracking采集信息。 |

资源编排

| PreserveStor age | Boolean | 否 | 是 | 是否永久保存日志。 | 取值： true：永久保存日志。如果取值为true，则TTL的设置不生效。 false（默认值）：不永久保存日志。 |
|---|---|---|---|---|---|
| AppendMeta | Boolean | 否 | 是 | 接收日志后，是否自动添加客户端外网IP和日志到达时间。 | 取值： true：自动添加客户端外网IP和日志到达时间。 false（默认值）：不自动添加客户端外网IP和日志到达时间。 |
| EncryptConf | Map | 否 | 否 | 数据加密配置。 | 更多信息，请参见EncryptConf语法和EncryptConf属性。 |

**EncryptConf语法**

```json
"EncryptConf": {
    "Enable": Boolean,
    "EncryptType": String,
    "UserCmkInfo": Map
}
```

**EncryptConf属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Enable | Boolean | 是 | 否 | 是否启用数据加密。 | 取值： true：启用数据加密。 false（默认值）：不启用数据加密。 |
| EncryptType | String | 是 | 否 | 加密算法。 | 取值： default：AES算法。 m4：国密算法。 |
| UserCmkInfo | Map | 否 | 否 | 如果指定了 UserCmkInfo ，则使用自带密钥（BYOK）加密或解密数据。 否则，将使用日志服务的服务密钥。 | 更多信息，请参见UserCmkInfo语法和UserCmkInfo属性。 |

**UserCmkInfo语法**

```json
"UserCmkInfo": {
    "CmkKeyId": String,
    "Arn": String,
    "RegionId": String
  }
```

**UserCmkInfo属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| CmkKeyId | String | 是 | 否 | BYOK密钥所属的CMK的ID。 | 无 |

资源编排

| Arn | String | 是 | 否 | CMK所在区域的ID。 | 无 |
|---|---|---|---|---|---|
| RegionId | String | 是 | 否 | RAM角色的 ARN。 | 无 |

**返回值**

Fn::GetAtt LogstoreName：日志库名称。

**示例**

`YAML` 格式

```
ROSTemplateFormatVersion: '2015-09-01' Description: Test SLS Logstore Parameters: {} Resources:
  SlsLogStore:
    Properties:
      LogstoreName: mytest
      PreserveStorage: true
      ProjectName: TestProject
      AppendMeta: true
      MaxSplitShard: 64
      AutoSplit: true
      EnableTracking: false
      ShardCount: 2
Outputs: {}
```

`JSON` 格式

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Description": "Test SLS Logstore",
  "Parameters": {
  },
  "Resources": {
    "SlsLogStore": {
      "Type": "ALIYUN::SLS::Logstore",
      "Properties": {
        "LogstoreName": "mytest",
        "PreserveStorage": true,
        "ProjectName": "TestProject",
        "AppendMeta": true,
        "MaxSplitShard": 64,
        "AutoSplit": true,
        "EnableTracking": false,
        "ShardCount": 2
      }
    }
  },
  "Outputs": {
  }
}
```

更多示例，请参见创建日志项目、创建日志库、创建索引、配置Logtail参数、创建日志服务ECS机器组、将日志配置应用于机器组、创建日志配置、将查询结果保存为快速查询和创建告警的组合示例：JSON示例和YAML示例。

#### ALIYUN::SLS::LogtailConfig

资源编排 ALIYUN::SLS::LogtailConfig类型用于配置采集数据时的Logtail参数。

**语法**

```json
{
  "Type": "ALIYUN::SLS::LogtailConfig",
  "Properties": {
    "ProjectName": String,
    "LogtailConfigName": String,
    "LogstoreName": String,
    "RawConfigData": Map,
    "CloneFrom": Map
  }
}
```

**属性**

| 属性名称 |  |  | 类型 |  | 必须 |  | 允许更新 |  | 描述 |  | 约束 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ProjectName |  |  | String |  | 是 |  | 否 |  | 日志项目名称。 |  | 无 |  |
| LogtailConfigNam e |  |  | String |  | 是 |  | 否 |  | Logtail配置名称。 |  | 同一项目下配置名称必须唯一。 长度为2~128个字符。必须以小写英文字母或者数字开头和结尾。可包含小写英文字母、数字、短划线（-）和下划线（ ）。 _ |  |
| LogstoreName |  |  | String |  | 是 |  | 否 |  | 日志库名称。 |  | 无 |  |
|  |  |  |  |  |  |  |  |  |  |  | 格式与SLS API GetConfig 的响应相同。 如果同时指定CloneFrom和 RawConfigData，Logtail Config的数据将会和 RawConfigData合并，RawConfigData中的 configName、outputType 和outputDetail会被忽略。 取值示例： {"configName": |  |
|  |  |  |  |  |  |  |  |  |  |  |  | {"configName": |
|  |  |  |  |  |  |  |  |  |  |  | "test-logtail- |  |
|  |  |  |  |  |  |  |  |  |  |  | config", |  |
|  |  |  |  |  |  |  |  |  |  |  | "createTime": |  |
|  |  |  |  |  |  |  |  |  |  |  | 1574843554, |  |
|  |  |  |  |  |  |  |  |  |  |  | "inputDetail": |  |
|  |  |  |  |  |  |  |  |  |  |  | {"acceptNoEnoughKeys": |  |
|  |  |  |  |  |  |  |  |  |  |  | false, |  |
|  |  |  |  |  |  |  |  |  |  |  | "adjustTimezone": |  |
|  |  |  |  |  |  |  |  |  |  |  | false, "advanced": { |  |
|  |  |  |  |  |  |  |  |  |  |  | "force multiconfig": _ |  |
|  |  |  |  |  |  |  |  |  |  |  | false }, |  |
|  |  |  |  |  |  |  |  |  |  |  | "autoExtend": true, |  |
|  |  |  |  |  |  |  |  |  |  |  | "delayAlarmBytes": 0, |  |
|  |  |  |  |  |  |  |  |  |  |  | "delaySkipBytes": 0, |  |
|  |  |  |  |  |  |  |  |  |  |  | "discardNonUtf8": |  |
|  |  |  |  |  |  |  |  |  |  |  | false, |  |
|  |  |  |  |  |  |  |  |  |  |  | "discardUnmatch": |  |
|  |  |  |  |  |  |  |  |  |  |  | false, |  |
|  |  |  |  |  |  |  |  |  |  |  | "dockerExcludeEnv": |  |
|  |  |  |  |  |  |  |  |  |  |  | {}, |  |
|  |  |  |  |  |  |  |  |  |  |  | "dockerExcludeLabel": |  |

资源编排

|  |  |  |  |  | {}, "dockerFile": |
|---|---|---|---|---|---|
|  |  |  |  |  | false, |
|  |  |  |  |  | "dockerIncludeEnv": |
|  |  |  |  |  | {}, |
|  |  |  |  |  | "dockerIncludeLabel": |
|  |  |  |  |  | {}, "enableRawLog": |
|  |  |  |  |  | false, "enableTag": |
|  |  |  |  |  | false, |
|  |  |  |  |  | "fileEncoding": |
|  |  |  |  |  | "utf8", |
|  |  |  |  |  | "filePattern": |
|  |  |  |  |  | "test.log*", |
|  |  |  |  |  | "filterKey": [], |
|  |  |  |  |  | "filterRegex": [], |
|  |  |  |  |  | "key": [ "time", |
|  |  |  |  |  | "logger", "level", |
| RawConfigData | Map | 否 | 是 | 原始配置数据。 | "request id", _ |
|  |  |  |  |  | "user id", |
|  |  |  |  |  | _ |
|  |  |  |  |  | "region id", _ |
|  |  |  |  |  | "content" ], |
|  |  |  |  |  | "localStorage": true, |
|  |  |  |  |  | "logPath": |
|  |  |  |  |  | "/var/log/test", |
|  |  |  |  |  | "logTimezone": "", |
|  |  |  |  |  | "logType": |
|  |  |  |  |  | "delimiter log", _ |
|  |  |  |  |  | "maxDepth": 100, |
|  |  |  |  |  | "maxSendRate": -1, |
|  |  |  |  |  | "mergeType": "topic", |
|  |  |  |  |  | "preserve": true, |
|  |  |  |  |  | "preserveDepth": 1, |
|  |  |  |  |  | "priority": 0, |
|  |  |  |  |  | "quote": "\u0001", |
|  |  |  |  |  | "sendRateExpire": 0, |
|  |  |  |  |  | "sensitive keys": [], _ |
|  |  |  |  |  | "separator": ",,,", |
|  |  |  |  |  | "shardHashKey": [], |
|  |  |  |  |  | "tailExisted": false, |
|  |  |  |  |  | "timeFormat": "", |
|  |  |  |  |  | "timeKey": "", |
|  |  |  |  |  | "topicFormat": "none" |
|  |  |  |  |  | }, "inputType": |
|  |  |  |  |  | "file", |
|  |  |  |  |  | "lastModifyTime": |
|  |  |  |  |  | 1574843554, |
|  |  |  |  |  | "logSample": "2019- |
|  |  |  |  |  | 11-27 |
|  |  |  |  |  | 10:48:23,160,,,MAIN,,, |
|  |  |  |  |  | INFO,,,98DCC51D-BE5D- |
|  |  |  |  |  | 49C7-B3FD- |
|  |  |  |  |  | 37B2BAEFB296,,,1234567 |
|  |  |  |  |  | 89,,,cn- |
|  |  |  |  |  | hangzhou,,,this is a |
|  |  |  |  |  | simple test.", |
|  |  |  |  |  | "outputDetail": { |
|  |  |  |  |  | "endpoint": "cn- |
|  |  |  |  |  | hangzhou- |
|  |  |  |  |  | intranet.log.aliyuncs. |
|  |  |  |  |  | com", "logstoreName": |
|  |  |  |  |  | "test-logstore", |
|  |  |  |  |  | "region": "cn- |
|  |  |  |  |  | hangzhou"}, |
| > 文档版本：20260 | 729 |  |  |  | 365 |

资源编排

|  |  |  |  |  | "outputType": |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  | "LogService"} |  |
| CloneFrom | Map | 否 | 是 | 克隆其他日志项目的 LogtailConfig。 | CloneFrom和 LogtailConfig必须指定一个。 更多信息，请参见CloneFrom属性。 |  |

**CloneFrom语法**

```json
"CloneFrom": {
  "ProjectName": String,
  "LogtailConfigName": String
}
```

**CloneFrom属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ProjectName | String | 是 | 是 | 日志项目名称。 | 无 |
| LogtailConfig Name | String | 是 | 是 | Logtail配置名称。 | 无 |

**返回值**

Fn::GetAtt Endpoint：Endpoint地址。 AppliedMachineGroups：日志采集配置的机器列表。 LogtailConfigName：Logtail配置名称。

**示例**

`JSON` 格式

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "LogtailConfig": {
      "Type": "ALIYUN::SLS::LogtailConfig",
      "Properties": {
        "ProjectName": {
          "Ref": "ProjectName"
        },
        "LogtailConfigName": {
          "Ref": "LogtailConfigName"
        },
        "LogstoreName": {
          "Ref": "LogstoreName"
        },
        "RawConfigData": {
          "Ref": "RawConfigData"
        },
        "CloneFrom": {
          "Ref": "CloneFrom"
        }
      }
    }
  },
  "Parameters": {
"ProjectName" {
```

资源编排

```json
    "ProjectName": {
      "MinLength": 3,
      "Type": "String",
      "Description": "Project name: 1. Only supports lowercase letters, numbers, hyphens (-) and unde
rscores (_). 2. Must start and end with lowercase letters and numbers. 3. The name length is 3-63 cha racters.",
      "MaxLength": 63
    },
    "LogtailConfigName": {
      "MinLength": 3,
      "Type": "String",
      "Description": "Logtail config name: 1. Only supports lowercase letters, numbers, hyphens (-) a
nd underscores (_). 2. Must start and end with lowercase letters and numbers. 3. The name length is 3 -63 characters.",
      "MaxLength": 63
    },
    "LogstoreName": {
      "MinLength": 3,
      "Type": "String",
      "Description": "Logstore name: 1. Only supports lowercase letters, numbers, hyphens (-) and und
erscores (_). 2. Must start and end with lowercase letters and numbers. 3. The name length is 3-63 ch aracters.",
      "MaxLength": 63
    },
    "RawConfigData": {
      "Type": "Json",
      "Description": "The format is the same as the response of SLS API GetConfig. Either CloneFrom o
r RawConfigData must be specified. If CloneFrom and RawConfigData are both specified, logtail config data will be merged from both with RawConfigData first. configName, outputType, outputDetail in data will be ignored.For example:\n{\"configName\": \"test-logtail-config\",\"createTime\": 1574843554,\"inputDetail\": { \"acceptNoEnoughKeys\": false, \"adjustTimezone\": false, \"advanced\": { \"force_multiconfig\": false }, \"autoExtend\": true, \"delayAlarmBytes\": 0, \"delaySkipBytes\": 0, \"discardNonUtf8\": false, \"discardUnmatch\": false, \"dockerExcludeEnv\": {}, \"dockerExcludeLabel\": {}, \"dockerFile\": false, \"dockerIncludeEnv\": {}, \"dockerIncludeLabel\": {}, \"enableRawLog\": false, \"enableTag\": false, \"fileEncoding\": \"utf8\", \"filePattern\": \"tes t.log*\", \"filterKey\": [], \"filterRegex\": [], \"key\": [ \"time\", \"logger\", \"level\", \"request_id\", \"user_id\", \"region_id\", \"content\" ], \"localStorage\": true, \"logPath\": \"/var/log/test\", \"logTimezone\": \"\", \"logType\": \"delimiter_log\", \"maxDepth\": 100, \"maxSendRate\": -1, \"mergeType\": \"topic\", \"preserve\": true, \"preserveDepth\": 1, \"priority\": 0, \"quote\": \"\\u0001\", \"sendRateExpire\": 0, \"sensitive_keys\": [], \"separator\": \",,,\", \"shardHashKey\": [], \"tailExisted\": false, \"timeFormat\": \"\", \"timeKey \": \"\", \"topicFormat\": \"none\"}, \"inputType\": \"file\", \"lastModifyTime\": 1574843554, \"logS ample\": \"2019-11-27 10:48:23,160,,,MAIN,,,INFO,,,98DCC51D-BE5D-49C7-B3FD- 37B2BAEFB296,,,123456789,,,cn-hangzhou,,,this is a simple test.\", \"outputDetail\": {\"endpoint\": \ "cn-hangzhou-intranet.log.aliyuncs.com\", \"logstoreName\": \"test-logstore\",\"region\": \"cn-hangzh ou\"}, \"outputType\": \"LogService\"}"
    },
    "CloneFrom": {
      "Type": "Json",
      "Description": "Clone logtail config data from existing logtail config. Either CloneFrom or Raw
ConfigData must be specified. If CloneFrom and RawConfigData are both specified, logtail config data will be merged from both with RawConfigData first."
    }
  },
  "Outputs": {
    "LogtailConfigName": {
     "Description": "Logtail config name.",
     "Value": {
      "Fn::GetAtt": [
       "LogtailConfig",
       "LogtailConfigName"
```

]

```
     }
```

资源编排

```json
    },
    "Endpoint": {
      "Description": "Endpoint address.",
      "Value": {
        "Fn::GetAtt": [
          "LogtailConfig",
          "Endpoint"
```

]

```json
      }
    },
    "AppliedMachineGroups": {
      "Description": "Applied machine groups.",
      "Value": {
        "Fn::GetAtt": [
          "LogtailConfig",
          "AppliedMachineGroups"
```

]

```
      }
    }
  }
}
```

`YAML` 格式

```
ROSTemplateFormatVersion: '2015-09-01' Resources:
  LogtailConfig:
    Properties:
      ProjectName:
        Ref: ProjectName
      LogtailConfigName:
        Ref: LogtailConfigName
      LogstoreName:
        Ref: LogstoreName
      RawConfigData:
        Ref: RawConfigData
      CloneFrom:
        Ref: CloneFrom
Parameters:
  ProjectName:
    MinLength: 3
    Type: String
    Description: 'Project name: 1. Only supports lowercase letters, numbers, hyphens
      (-) and underscores (_). 2. Must start and end with lowercase letters and numbers.
      3. The name length is 3-63 characters.'
    MaxLength: 63
  LogtailConfigName:
    MinLength: 3
    Type: String
    Description: 'Logtail config name: 1. Only supports lowercase letters, numbers,
      hyphens (-) and underscores (_). 2. Must start and end with lowercase letters
      and numbers. 3. The name length is 3-63 characters.'
    MaxLength: 63
  LogstoreName:
    MinLength: 3
    Type: String
    Description: 'Logstore name: 1. Only supports lowercase letters, numbers, hyphens
      (-) and underscores (_). 2. Must start and end with lowercase letters and numbers.
      3. The name length is 3-63 characters.'
    MaxLength: 63
  RawConfigData:
```

资源编排 g

```json
    Type: Json
    Description: |-
      The format is the same as the response of SLS API GetConfig. Either CloneFrom or RawConfigData
must be specified. If CloneFrom and RawConfigData are both specified, logtail config data will be mer ged from both with RawConfigData first. configName, outputType, outputDetail in data will be ignored. For example:
      {"configName": "test-logtail-config","createTime": 1574843554,"inputDetail": {
"acceptNoEnoughKeys": false, "adjustTimezone": false, "advanced": { "force_multiconfig": false }, " autoExtend": true, "delayAlarmBytes": 0, "delaySkipBytes": 0, "discardNonUtf8": false, "discardUnmatch": false, "dockerExcludeEnv": {}, "dockerExcludeLabel": {}, "dockerFile": false, "dock erIncludeEnv": {}, "dockerIncludeLabel": {}, "enableRawLog": false, "enableTag": false, "fileEncoding": "utf8", "filePattern": "test.log*", "filterKey": [], "filterRegex": [], "key": [ "t ime", "logger", "level", "request_id", "user_id", "region_id", "content" ], "localStorage" : true, "logPath": "/var/log/test", "logTimezone": "", "logType": "delimiter_log", "maxDepth": 100, " maxSendRate": -1, "mergeType": "topic", "preserve": true, "preserveDepth": 1, "priority": 0, "quote": "\u0001", "sendRateExpire": 0, "sensitive_keys": [], "separator": ",,,", "shardHashKey": [], "tailExi sted": false, "timeFormat": "", "timeKey": "", "topicFormat": "none"}, "inputType": "file", "lastModi fyTime": 1574843554, "logSample": "2019-11-27 10:48:23,160,,,MAIN,,,INFO,,,98DCC51D-BE5D-49C7-B3FD-37 B2BAEFB296,,,123456789,,,cn-hangzhou,,,this is a simple test.", "outputDetail": {"endpoint": "cn-hang zhou-intranet.log.aliyuncs.com", "logstoreName": "test-logstore","region": "cn-hangzhou"}, "outputType": "LogService"}
  CloneFrom:
    Type: Json
    Description: Clone logtail config data from existing logtail config. Either CloneFrom
      or RawConfigData must be specified. If CloneFrom and RawConfigData are both
      specified, logtail config data will be merged from both with RawConfigData first.
Outputs:
  Endpoint:
    Description: Endpoint address.
    Value:
      Fn::GetAtt:
      - Endpoint
  AppliedMachineGroups:
    Description: Applied machine groups.
    Value:
      Fn::GetAtt:
      - AppliedMachineGroups
  LogtailConfigName:
    Description: Logtail config name.
    Value:
      Fn::GetAtt:
      - LogtailConfigName
```

更多示例，请参见创建日志项目、在日志项目下创建日志库、为指定的Logstore创建索引、配置采集数据时的Logtail参数、创建日志服务机器组、将日志服务的日志配置应用于机器组、创建日志配置、将查询结果保存为快速查询和创建告警的组合示例：JSON示例和YAML示例。

#### ALIYUN::SLS::Savedsearch

**语法**

资源编排

```json
{
  "Type": "ALIYUN::SLS::Savedsearch",
  "Properties": {
    "Project": String,
    "Detail": Map
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Project | String | 是 | 否 | 日志项目名称 | 无 |
| Detail | Map | 是 | 是 | 查询详情 | 更多信息，请参见Detail属性。 |

**Detail语法**

```json
"Detail": {
  "SearchQuery": String,
  "Logstore": String,
  "DisplayName": String,
  "SavedsearchName": String,
  "Topic": String
}
```

**Detail属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| SearchQuery | String | 是 | 是 | 查询语句 | 无 |
| Logstore | String | 是 | 是 | 日志库 | 无 |
| DisplayName | String | 否 | 是 | 快速查询名称 | 长度为1~63个字符。 |
| SavedsearchNa me | String | 是 | 否 | 保存的查询名称 | 无 |
| Topic | String | 是 | 是 | 日志主题 | 无 |

**返回值**

Fn::GetAtt SavedsearchName：保存的查询名称

**示例**

`JSON` 格式资源编排

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "Project": {
      "Type": "String",
      "Description": "Project name"
    },
    "Detail": {
      "Type": "Json",
      "Description": ""
    }
  },
  "Resources": {
    "SavedSearch": {
      "Type": "ALIYUN::SLS::Savedsearch",
      "Properties": {
        "Project": {
          "Ref": "Project"
        },
        "Detail": {
          "Ref": "Detail"
        }
      }
    }
  },
  "Outputs": {
    "SavedsearchName": {
      "Description": "Savedsearch name.",
      "Value": {
        "Fn::GetAtt": [
          "SavedSearch",
          "SavedsearchName"
```

]

```
      }
    }
  }
}
```

`YAML` 格式资源编排

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
 Project:
  Type: String
  Description: Project name
 Detail:
  Type: Json
  Description: ''
Resources:
 SavedSearch:
  Properties:
   Project:
    Ref: Project
   Detail:
    Ref: Detail
Outputs:
 SavedsearchName:
  Description: Savedsearch name.
  Value:
   'Fn::GetAtt':
    - SavedsearchName
```

#### ALIYUN::SLS::Project

**语法**

```json
{
  "Type": "ALIYUN::SLS::Project",
  "Properties": {
    "Name": String,
    "Description": String,
    "Tags": List
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Name | String | 是 | 否 | 日志项目的名称。 | 长度为3~36个字符。必须以小写英文字母或数字开头和结尾。可包含小写英文字母、数字和短划线 （-）。 |
| Description | String | 否 | 否 | 日志项目的描述。 | 长度不超过64个字符。不支持特殊字符 <>'\" 。 |
| Tags | List | 否 | 是 | 标签。 | 最多支持20个标签。 更多信息，请参见Tags语法和Tags 属性。 |

**Tags语法**

资源编排

```json
"Tags": [
  {
    "Key": String,
    "Value": String
  }
```

]

**Tags属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Key | String | 是 | 否 | 标签键。 | 长度为1~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或 https:// 。 |
| Value | String | 否 | 否 | 标签值。 | 长度为0~128个字符，不能以 aliyun 和 acs: 开头，不能包含 http:// 或 https:// 。 |

**返回值**

Fn::GetAtt Name: 日志项目名称。

**示例**

`JSON` 格式资源编排

```json
{
 "ROSTemplateFormatVersion": "2015-09-01",
 "Parameters": {
  "Description": {
   "Type": "String",
   "Description": "Project description: <>'\"\\ is not supported, up to 64 characters.",
   "MaxLength": 64
  },
  "Tags": {
   "Type": "Json",
   "Description": "Tags to attach to project. Max support 20 tags to add during create project. Each
tag with two properties Key and Value, and Key is required.",
   "MaxLength": 20
  },
  "Name": {
   "Type": "String",
   "Description": "Project name:\n1. Only supports lowercase letters, numbers, hyphens (-) and unders
cores (_).\n2. Must start and end with lowercase letters and numbers.\n3. The name length is 3-63 cha racters.",
   "AllowedPattern": "^[a-zA-Z0-9_-]+$",
   "MinLength": 3,
   "MaxLength": 63
  }
 },
 "Resources": {
  "Project": {
   "Type": "ALIYUN::SLS::Project",
   "Properties": {
    "Description": {
     "Ref": "Description"
    },
    "Tags": {
     "Ref": "Tags"
    },
    "Name": {
     "Ref": "Name"
    }
   }
  }
 },
 "Outputs": {
  "Name": {
   "Description": "Project name.",
   "Value": {
    "Fn::GetAtt": [
     "Project",
     "Name"
```

]

```
   }
  }
 }
}
```

`YAML` 格式资源编排

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
 Description:
  Type: String
  Description: 'Project description: <>''"\ is not supported, up to 64 characters.'
  MaxLength: 64
 Tags:
  Type: Json
  Description: >-
   Tags to attach to project. Max support 20 tags to add during create
   project. Each tag with two properties Key and Value, and Key is required.
  MaxLength: 20
 Name:
  Type: String
  Description: >-
   Project name:
   1. Only supports lowercase letters, numbers, hyphens (-) and underscores
   (_).
   2. Must start and end with lowercase letters and numbers.
   3. The name length is 3-63 characters.
  AllowedPattern: '^[a-zA-Z0-9_-]+$'
  MinLength: 3
  MaxLength: 63
Resources:
 Project:
  Properties:
   Description:
    Ref: Description
   Tags:
    Ref: Tags
   Name:
    Ref: Name
Outputs:
 Name:
  Description: Project name.
  Value:
   'Fn::GetAtt':
    - Name
```

更多示例，请参见JSON示例和YAML示例。该示例可实现以下功能： 创建日志项目在日志项目下创建日志库为指定的Logstore创建索引配置采集数据时的Logtail参数创建日志服务机器组将日志服务的日志配置应用于机器组创建日志配置将查询结果保存为快速查询创建告警

### PAI

资源编排

#### ALIYUN::PAI::Service

**语法**

```json
{
  "Type": "ALIYUN::PAI::Service",
  "Properties": {
    "Develop": String,
    "ServiceConfig": Map,
    "Labels": Map
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| Develop | String | 否 | 否 | 是否进入开发模式。 | 取值： true：进入开发模式。 false：不进入开发模式。 |

资源编排

| ServiceConfig | Map | 是 | 是 | 服务的配置信息。 | 例如： { "metadata": { "cpu":1, "instance": 1, "memory":10 24 }, "name":"ech o", "processor _ entry":"lib echo.so", "processor _ path":"http ://oss-cn- hangzhou- zmf.aliyunc s.com/05924 7/echo proc _ essor relea _ se.tar.gz", "processor _ type":"cpp" } |
|---|---|---|---|---|---|
| Labels | Map | 否 | 是 | 服务标签列表。 | 例如： {"key":"val ue"} |

**返回值**

Fn::GetAtt ServiceGroup：服务所在的分组。 Message：服务的摘要信息。 Memory：每个实例申请的内存。 CurrentVersion：当前运行的模型版本。 RunningInstance：正在运行的服务的实例个数。 资源编排 Cpu：每个实例申请的CPU。 Image：服务的数据镜像。 Gpu：每个实例申请的GPU。 CallerUid：服务创建账号的UID。 Reason：服务的状态原因。 TotalInstance：服务的所有实例总个数。 ServiceConfig：服务的配置信息。 AccessToken：服务的请求Token。 InternetEndpoint：服务的公网Endpoint。 ResourceAlias：服务所在的资源组别名。 CreateTime：服务的创建时间。 Resource：服务所在的资源组。 Labels：服务标签列表。 ExtraData：服务的额外信息。 Namespace：服务所在的命名空间。 Weight：服务灰度发布的权重值。 Role：服务角色。 PendingInstance：被挂起的服务的实例个数。 LatestVersion：服务最新版本号。 ServiceName：服务的名字。 SafetyLock：服务安全锁。 UpdateTime：服务的更新时间。 ServiceUid：服务ID，同ServiceId。 RoleAttrs：服务角色额外属性。 ParentUid：服务创建账号的阿里云账号UID。 IntranetEndpoint：服务内网endpoint。

**示例**

`YAML` 格式

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  ServiceConfig:
    Type: Json
    Description: Service configuration information.
    Default:
      metadata:
        cpu: 1
        instance: 1
        memory: 1024
      name: echo
      processor_entry: libecho.so
      processor_path: http://oss-cn-hangzhou-zmf.aliyuncs.com/059247/echo_processor_release.tar.gz
      processor_type: cpp
  Labels:
    Type: Json
    Description: Service Tag.
    Default:
      key: value
Resources:
  ExtensionResource:
    Properties:
```

资源编排 p

```
      ServiceConfig:
        Ref: ServiceConfig
      Labels:
        Ref: Labels
Outputs:
  ServiceGroup:
    Description: Group to which the service belongs.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - ServiceGroup
  Message:
    Description: Latest information on services.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - Message
  Memory:
    Description: Memory of service (MB).
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - Memory
  CurrentVersion:
    Description: Current running version of the service.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - CurrentVersion
  RunningInstance:
    Description: Number of instances in service running.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - RunningInstance
  Cpu:
    Description: Number of service CPU cores.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - Cpu
  Image:
    Description: Service Deployment Mirroring.
    Value:
      Fn::GetAtt:
        - ExtensionResource
  Gpu:
    Description: Number of service GPU cards.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - Gpu
  CallerUid:
    Description: The ID of the service creator, which can be the ID of the RAM account.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - CallerUid
  Reason:
    Description: Service deployment failure reason.
    Value:
```

资源编排

```
      Fn::GetAtt:
        - ExtensionResource
        - Reason
  TotalInstance:
    Description: Total number of instances required by the service.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - TotalInstance
  ServiceConfig:
    Description: Service configuration information.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - ServiceConfig
  AccessToken:
    Description: Service Request authentication token.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - AccessToken
  InternetEndpoint:
    Description: Public network Endpoint of the service.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - InternetEndpoint
  ResourceAlias:
    Description: Name of the resource group where the service resides.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - ResourceAlias
  CreateTime:
    Description: Creation time of the service.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - CreateTime
  Resource:
    Description: The ID of the resource group to which the service belongs.
    Value:
      Fn::GetAtt:
        - ExtensionResource
  Labels:
    Description: Service Tag.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - Labels
  ExtraData:
    Description: Service Extra Information.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - ExtraData
  Namespace:
    Description: The namespace to which the service belongs.
    Value:
      Fn::GetAtt:
        - ExtensionResource
-Namespace
```

资源编排

```
         Namespace
  Weight:
    Description: Packet Service Traffic Weight.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - Weight
  Role:
    Description: Grouping Service Role.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - Role
  PendingInstance:
    Description: Number of instances where the service is not currently ready.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - PendingInstance
  LatestVersion:
    Description: The latest version of the service.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - LatestVersion
  ServiceName:
    Description: Service Name.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - ServiceName
  SafetyLock:
    Description: Service Security Lock Status.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - SafetyLock
  UpdateTime:
    Description: Service Last Updated.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - UpdateTime
  ServiceUid:
    Description: Unique Service ID.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - ServiceUid
  RoleAttrs:
    Description: Grouping Service Role Properties.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - RoleAttrs
  ParentUid:
    Description: Primary account ID of the creator.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - ParentUid
  IntranetEndpoint:
    Description: The intranet Endpoint of the service.
```

资源编排

```
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - IntranetEndpoint
```

`JSON` 格式

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "ServiceConfig": {
      "Type": "Json",
      "Description": "Service configuration information.",
      "Default": {
        "metadata": {
          "cpu": 1,
          "instance": 1,
          "memory": 1024
        },
        "name": "echo",
        "processor_entry": "libecho.so",
        "processor_path": "http://oss-cn-hangzhou-
zmf.aliyuncs.com/059247/echo_processor_release.tar.gz",
        "processor_type": "cpp"
      }
    },
    "Labels": {
      "Type": "Json",
      "Description": "Service Tag.",
      "Default": {"key":"value"}
    }
  },
  "Resources": {
    "ExtensionResource": {
      "Type": "ALIYUN::PAI::Service",
      "Properties": {
        "ServiceConfig": {
          "Ref": "ServiceConfig"
        },
        "Labels": {
          "Ref": "Labels"
        }
      }
    }
  },
  "Outputs": {
    "ServiceGroup": {
      "Description": "Group to which the service belongs.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "ServiceGroup"
```

]

```json
      }
    },
    "Message": {
      "Description": "Latest information on services.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "Message"
```

] 资源编排

```json
      }
    },
    "Memory": {
      "Description": "Memory of service (MB).",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "Memory"
```

]

```json
      }
    },
    "CurrentVersion": {
      "Description": "Current running version of the service.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "CurrentVersion"
```

]

```json
      }
    },
    "RunningInstance": {
      "Description": "Number of instances in service running.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "RunningInstance"
```

]

```json
      }
    },
    "Cpu": {
      "Description": "Number of service CPU cores.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "Cpu"
```

]

```json
      }
    },
    "Image": {
      "Description": "Service Deployment Mirroring.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "Image"
```

]

```json
      }
    },
    "Gpu": {
      "Description": "Number of service GPU cards.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "Gpu"
```

]

```json
      }
    },
    "CallerUid": {
      "Description": "The ID of the service creator, which can be the ID of the RAM account.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "CallerUid"
```

] 资源编排 ]

```json
      }
    },
    "Reason": {
      "Description": "Service deployment failure reason.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "Reason"
```

]

```json
      }
    },
    "TotalInstance": {
      "Description": "Total number of instances required by the service.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "TotalInstance"
```

]

```json
      }
    },
    "ServiceConfig": {
      "Description": "Service configuration information.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "ServiceConfig"
```

]

```json
      }
    },
    "AccessToken": {
      "Description": "Service Request authentication token.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "AccessToken"
```

]

```json
      }
    },
    "InternetEndpoint": {
      "Description": "Public network Endpoint of the service.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "InternetEndpoint"
```

]

```json
      }
    },
    "ResourceAlias": {
      "Description": "Name of the resource group where the service resides.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "ResourceAlias"
```

]

```json
      }
    },
    "CreateTime": {
      "Description": "Creation time of the service.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "CreateTime"
```

资源编排 ]

```json
      }
    },
    "Resource": {
      "Description": "The ID of the resource group to which the service belongs.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "Resource"
```

]

```json
      }
    },
    "Labels": {
      "Description": "Service Tag.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "Labels"
```

]

```json
      }
    },
    "ExtraData": {
      "Description": "Service Extra Information.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "ExtraData"
```

]

```json
      }
    },
    "Namespace": {
      "Description": "The namespace to which the service belongs.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "Namespace"
```

]

```json
      }
    },
    "Weight": {
      "Description": "Packet Service Traffic Weight.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "Weight"
```

]

```json
      }
    },
    "Role": {
      "Description": "Grouping Service Role.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "Role"
```

]

```json
      }
    },
    "PendingInstance": {
      "Description": "Number of instances where the service is not currently ready.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
```

资源编排

```
          "PendingInstance"
```

]

```json
      }
    },
    "LatestVersion": {
      "Description": "The latest version of the service.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "LatestVersion"
```

]

```json
      }
    },
    "ServiceName": {
      "Description": "Service Name.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "ServiceName"
```

]

```json
      }
    },
    "SafetyLock": {
      "Description": "Service Security Lock Status.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "SafetyLock"
```

]

```json
      }
    },
    "UpdateTime": {
      "Description": "Service Last Updated.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "UpdateTime"
```

]

```json
      }
    },
    "ServiceUid": {
      "Description": "Unique Service ID.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "ServiceUid"
```

]

```json
      }
    },
    "RoleAttrs": {
      "Description": "Grouping Service Role Properties.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "RoleAttrs"
```

]

```json
      }
    },
    "ParentUid": {
      "Description": "Primary account ID of the creator.",
      "Value": {
        "Fn::GetAtt": [
"ExtensionResource",
```

资源编排

```
teso esouce,
          "ParentUid"
```

]

```json
      }
    },
    "IntranetEndpoint": {
      "Description": "The intranet Endpoint of the service.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "IntranetEndpoint"
```

]

```
      }
    }
  }
}
```

### VPC

#### ALIYUN::VPC::EIP

**语法**

```json
{
  "Type": "ALIYUN::VPC::EIP",
  "Properties": {
    "Isp": String,
    "Period": Number,
    "ResourceGroupId": String,
    "AutoPay": Boolean,
    "InstanceChargeType": String,
    "PricingCycle": String,
    "InternetChargeType": String,
    "Bandwidth": Number
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| ResourceGroupI d | String | 否 | 否 | 资源组ID。 | 无。 |
| Bandwidth | Number | 否 | 否 | 带宽值。 | 如果不指定，则取默认值5Mbps。 |
| InternetChargeT ype | String | 否 | 否 | EIP的计费方式。 | 取值范围： PayByBandwidth：按带宽计费。 PayByTraffic：按流量计费。 默认值：PayByBandwidth。 |
| InstanceCharge Type | String | 否 | 否 | EIP的付费方式。 | 取值范围： Prepaid：预付费。 Postpaid：后付费。 默认值：Postpaid。 |

资源编排

| PricingCycle | String | 否 | 否 | 预付费的计费周期。 | 取值范围： Month：按月付费。 Year：按年付费。 默认值：Month。 说明 InstanceChargeType参数的值为 Prepaid时，该参数必选。 |
|---|---|---|---|---|---|
| Period | Number | 否 | 否 | 购买时长。 | 取值范围： 当选择按月付费时，取值范围为1~9。 当选择按年付费时，取值范围：1~3。 默认值：1。 说明 InstanceChargeType参数的值为Prepaid时，该参数必选。 |
| AutoPay | Boolean | 否 | 否 | 是否自动付费。 | 取值范围： false：不开启自动付费，生成订单后需要到订单中心完成支付。 true：开启自动付费，自动支付订单。 说明 InstanceChargeType参数的值为Prepaid时，该参数必选。 |
| Isp | String | 否 | 否 | 用于金融云的ISP 标签，仅对cn- hangzhou 地域有效。 | 如果您不是金融云用户，该参数会被忽略。 |

**返回值**

Fn::GetAtt EipAddress：分配的弹性公网IP。 AllocationId：弹性公网IP的实例ID。 OrderId：选择预付费时返回的订单号。

**示例**

资源编排

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "Eip": {
      "Type": "ALIYUN::VPC::EIP",
      "Properties": {
        "InternetChargeType": "PayByTraffic",
          "Bandwidth": 200
      }
    }
  },
  "Outputs": {
    "EipAddress": {
      "Value" : {"Fn::GetAtt": ["Eip", "EipAddress"]}
    },
    "AllocationId": {
      "Value" : {"Fn::GetAtt": ["Eip", "AllocationId"]}
    },
    "OrderId": {
      "Value" : {"Fn::GetAtt": ["Eip", "OrderId"]}
    }
  }
}
```

#### ALIYUN::VPC::EIPAssociation

ALIYUN::VPC::EIPAssociation用于为云产品实例绑定弹性公网IP（EIP）。

**语法**

```json
{
  "Type": "ALIYUN::VPC::EIPAssociation",
  "Properties": {
    "AllocationId": String,
    "InstanceId": String,
    "PrivateIpAddress": String,
    "Mode": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| AllocationId | String | 是 | 是 | 弹性公网IP的 ID。 | 无 |
| InstanceId | String | 是 | 是 | 云产品实例的 ID。 | 支持以下云产品实例类型： VPC类型的ECS实例。 VPC类型的SLB实例。 NAT网关。 高可用虚拟IP（HaVip）。 弹性网卡。 |
| PrivateIpAddr ess | String | 否 | 是 | 交换机网段内的一个私网IP地址。 | 如果不指定该参数，系统将根据 VPC ID和交换机ID自动分配一个私网IP地址。 |

资源编排

| Mode | String | 否 | 是 | 绑定模式。 | 取值： NAT（默认值）：NAT模式（普通模式）。 MULTI BINDED：多EIP网卡可 _ 见模式。 BINDED：EIP网卡可见模式。 |
|---|---|---|---|---|---|

**返回值**

Fn::GetAtt EipAddress：弹性公网IP的地址。 AllocationId：弹性公网IP的ID。

**示例**

`JSON` 格式

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Description": {
    "en": "Create a VPC type ECS and bind EIP (existing VPC).",
```

`"zh-cn": "`创建`VPC`类型`ECS`，并绑定`EIP`（已有`VPC`）。"

```json
  },
  "Parameters": {
    "VPC": {
      "AssociationProperty": "ALIYUN::ECS::VPC::VPCId",
      "Type": "String",
      "Description": {
        "en": "Please search the ID starting with (vpc-xxx) from console-Virtual Private Cloud.",
```

`"zh-cn": "`现有专有网络的实例`ID`，在专有网络控制台选择专有网络进行查询。"

```json
      },
      "Label": {
        "en": "VPC ID",
```

`"zh-cn": "`专有网络`VPC`实例`ID"`

```json
      }
    },
    "VSwitch": {
      "AssociationProperty": "ALIYUN::ECS::VSwitch::VSwitchId",
      "AssociationPropertyMetadata": {
        "VpcId": "VPC"
      },
      "Type": "String",
      "Description": {
        "en": "Existing VSwitch ID, query under console-VPC-VSwitch, <font color='red'>VSwitch must b
e under VPC. ECS will be created under this VSwitch.</font>",
```

`"zh-cn": "`现有交换机`ID`，在专有网络控制台选择交换机进行查询，`<font color='red'>`交换机必须在`VPC`下。`ECS`将创建在此交换机下。`</font>"`

```json
      },
      "Label": {
        "en": "VSwitch ID",
```

`"zh-cn": "`交换机实例`ID"`

```json
      }
    },
    "SecurityGroup": {
      "Type": "String",
      "AssociationProperty": "ALIYUN::ECS::SecurityGroup::SecurityGroupId",
      "Description": {
        "en": "Please search the business security group ID starting with (sg-xxx) from console-ECS-N
etwork & Security.",
```

`"zh-cn": "`现有业务安全组的实例`ID`，在`ECS`控制台选择安全组进行查询。`<br><font color='red'>`安全组必须归属在V `PC`下。`</font>"`

```
      },
```

资源编排

```json
      "Label": {
        "en": "Business Security Group ID",
```

`"zh-cn": "`业务安全组`ID"`

```json
      },
      "AssociationPropertyMetadata": {
        "VpcId": "VPC"
      }
    },
    "ECSPassword": {
      "NoEcho": true,
      "Type": "String",
      "Description": {
        "en": "Server login password, Length 8-30, must contain three (Capital letters, lowercase
letters, numbers, ()`~!@#$%^&*_-+=|{}[]:;'<>,.?/ Special symbol in).",
```

`"zh-cn": "`服务器登录密码，长度为8~30个字符，必须包含三项（大写英文字母、小写英文字母、数字和 ()`~!@#$%^&*_-+=|{}[]:;'<>,.?/ 中的特殊字符）。"

```json
      },
      "AllowedPattern": "[0-9A-Za-z\\_\\-\\&:;'<>,=%`~!@#\\(\\)\\$\\^\\*\\+\\|\\{\\}\\[\\]\\.\\?
\\/]+$",
      "Label": {
        "en": "Instance Password",
```

`"zh-cn": "`实例密码"

```json
      },
      "MinLength": 8,
      "ConstraintDescription": {
        "en": "Length 8-30, must contain three(Capital letters, lowercase letters, numbers,
()`~!@#$%^&*_-+=|{}[]:;'<>,.?/ Special symbol in).",
```

`"zh-cn": "`长度为8~30个字符，必须包含三项（大写英文字母、小写英文字母、数字和 ()`~!@#$%^&*_-+=|{} []:;'<>,.?/ 中的特殊字符）。"

```json
      },
      "MaxLength": 30,
      "Default": null
    },
    "EIPInternetChargeType": {
      "Type": "String",
      "AllowedValues": [
        "PayByBandwidth",
        "PayByTraffic"
```

`],`

```json
      "Description": {
        "en": "The charge type of EIP, PayByBandwidth；PayByTraffic.",
```

`"zh-cn": "`弹性公网`IP`的收费类型。`PayByBandwidth`：按带宽付费；`PayByTraffic`：按流量付费。"

```json
      },
      "Label": {
        "en": "EIP Charge Type",
```

`"zh-cn": "`弹性公网`IP`的收费类型"

```json
      },
      "Default": "PayByTraffic"
    },
    "ECSImageId": {
      "Type": "String",
      "AssociationProperty": "ALIYUN::ECS::Instance::ImageId",
      "Description": {
        "en": "Image ID，Please use Centos7.",
```

`"zh-cn": "`镜像`ID`，请使用`Centos7`。"

```json
      },
      "Label": {
        "en": "Image",
```

`"zh-cn": "`镜像"

```json
      },
      "Default": "ubuntu_14"
    },
"ECSZoneId":{
```

资源编排

```json
    ECSZoneId: {
      "AssociationProperty": "ALIYUN::ECS::Instance:ZoneId",
      "Type": "String",
      "Description": {
        "en": "Availability zone ID.<br><b>Note: <font color='blue'>Before selecting, please confirm
whether the availability zone supports the specification of creating ECS resources. It is recommended to be different from other switch availability zones</font></b ><br><font color='red'>The switch avai lability zone and the selected switch instance ID must be in the same availability zone.</font>",
```

`"zh-cn": "`可用区`ID`。`<br><b>`注： `<font color='blue'>`选择前请确认该可用区是否支持创建`ECS`资源的规格，建议与其他交换机可用区不同`</font></b><br><font color='red'>`交换机可用区和已选择的交换机实例`ID`必须在同一个可用区。`</font` `>"`

```json
      },
      "Label": {
        "en": "VSwitch Availability Zone",
```

`"zh-cn": "`交换机可用区"

```json
      }
    },
    "EIPBandwidth": {
      "Type": "Number",
      "Description": {
        "en": "EIP Bandwidth, Value range: [1,200], unit: Mbps.",
```

`"zh-cn": "`弹性公网`IP`带宽。取值范围：1~200，单位：`Mbps`。"

```json
      },
      "MinValue": 1,
      "Label": {
        "en": "EIP Bandwidth",
```

`"zh-cn": "`弹性公网`IP`带宽"

```java
      },
      "MaxValue": 200,
      "Default": 1
    },
    "ECSInstanceType": {
      "AssociationPropertyMetadata": {
        "ZoneId": "ECSZoneId",
        "InstanceChargeType": "InstanceChargeType"
      },
      "AssociationProperty": "ALIYUN::ECS::Instance::InstanceType",
      "Type": "String",
      "Description": {
        "en": "<font color='blue'><b>1.Before selecting the model please confirm that the current
available zone under the model is in stock, some models need to be reported in advance</b></font><br> <font color='blue'><b>2.List of optional models</font><br></b></font>[ecs.c5.large <font color='green'>2vCPU 4GiB Intranet bandwidth1Gbps In-grid sending and receiving packages30MillionPPS</font>]<br></b>[ecs.c5.xlarge <font color='green'>4vCPU 8GiB Intranet bandwidth1 .5Gbps In-grid sending and receiving packages50MillionPPS</font>]<br></b>[ecs.c5.2xlarge <font color= 'green'>8vCPU 16GiB Intranet bandwidth2.5Gbps In-grid sending and receiving packages80MillionPPS</font>]",
```

`"zh-cn": "<font color='blue'><b>1`、选择机型前请先确认当前可用区下该机型是否有货，部分机型需要提前报备。`</`

```
b></font><br><font color='blue'><b>2、取值：</font><br></b></font>[ecs.c5.large：<font
```

`color='green'>2vCPU 4 GiB`，内网带宽`1Gbps`、内网收发包`30`万`PPS`。`</font>]<br></b>[ecs.c5.xlarge`：`<font color='` `green'>4vCPU 8GiB`，内网带宽`1.5Gbps`、内网收发包`50`万`PPS`。`</font>]<br></b>[ecs.c5.2xlarge`： `<font` `color='green'>8vCPU 16 GiB`，内网带宽`2.5 Gbps`、内网收发包`80`万`PPS`。`</font>]"`

```json
      },
      "Label": {
        "en": "Instance Type",
```

`"zh-cn": "`实例规格"

```json
      }
    },
    "ECSDiskCategory": {
      "Type": "String",
      "Description": {
        "en": "<font color='blue'><b>Optional values:</b></font><br>[cloud_efficiency: <font
color='green'>Efficient Cloud Disk</font>]<br>[cloud_ssd: <font color='green'>SSD Cloud Disk</font>]<
```

资源编排

```
br>[cloud_essd: <font color='green'>ESSD Cloud Disk</font>]<br>[cloud: <font color='green'>Cloud Disk </font>]<br>[ephemeral_ssd: <font color='green'>Local SSD Cloud Disk</font>]",
        "zh-cn": "<font color='blue'><b>取值：</b></font><br>[cloud_efficiency: <font color='green'>高
效云盘</font>]<br>[cloud_ssd: <font color='green'>SSD云盘</font>]<br>[cloud_essd: <font color='green'>E SSD云盘</font>]<br>[cloud: <font color='green'>普通云盘</font>]<br>[ephemeral_ssd: <font color='green'>
```

本地`SSD`盘`</font>]"`

```json
      },
      "AssociationProperty": "ALIYUN::ECS::Disk::SystemDiskCategory",
      "AssociationPropertyMetadata": {
        "ZoneId": "ECSZoneId",
        "InstanceType": "ECSInstanceType"
      },
      "Label": {
        "en": "System Disk Type",
```

`"zh-cn": "`系统盘类型"

```json
      }
    },
    "ECSSysDiskSize": {
      "Type": "Number",
      "Description": {
        "en": "System disk size, range of values: 40-500, units: GB.",
```

`"zh-cn": "`系统盘大小，取值范围：40~500，单位：`GB`。"

```json
      },
      "MinValue": 40,
      "Label": {
        "en": "System Disk Space",
```

`"zh-cn": "`系统盘空间"

```json
      },
      "MaxValue": 500,
      "Default": 40
    },
    "InstanceChargeType": {
      "Type": "String",
      "Label": {
        "en": "Instance Charge Type",
```

`"zh-cn": "`实例的付费方式"

```json
      },
      "Description": {
        "en": "<font color='blue'><b>Optional values:</b></font><br>[PostPaid: <font
color='green'>Pay as you go.</font>]<br> [PrePaid: <font color='green'>Prepaid, monthly subscription. </font>]",
        "zh-cn": "<font color='blue'><b>取值：</b></font><br>[PostPaid: <font color='green'>按量付费。</
```

`font>]<br>[PrePaid: <font color='green'>`预付费，包年包月。`</font>]"`

```json
      },
      "AllowedValues": [
        "PostPaid",
        "PrePaid"
```

`],`

```json
      "Default": "PostPaid"
    },
    "KeyPairName": {
      "Type": "String",
      "AssociationProperty": "ALIYUN::ECS::KeyPair::KeyPairName",
      "Label": {
        "en": "Key Pair Name",
```

`"zh-cn": "`密钥对名称"

```json
      },
      "Description": {
        "en": "If it is a Windows ECS instance, ignore this parameter. The default is blank.<br>If yo
u have filled in <font color='green'>key pair name</font>, <font color='green'>instance password< The content of /font> will still be set in the instance, but the password login method in the Linux syste m will be forbidden.<br><font color='red'>Please enter the name of the existing key pair. If you use theinstancepasswordLogin thekeypairnamedoesnotneedtobefilledin</font>"
```

资源编排

```
the instance password Login, the key pair name does not need to be filled in.</font>,
```

`"zh-cn": "`如果是`Windows ECS`实例，则忽略该参数。默认为空。`<br>`如果已填写`<font color='green'>`密钥对名称< `/font>`，`<font color='green'>`实例密码`</font>`的内容仍会被设置到实例中，但是`Linux`系统中的密码登录方式会被禁止。`<br><` `font color='red'>`请输入已有密钥对的名称。如使用实例密码登录，密钥对名称不需要填写。`</font>"`

```json
      },
      "Default": null
    }
  },
  "Metadata": {
    "ALIYUN::ROS::Interface": {
      "ParameterGroups": [
        {
          "Parameters": [
            "VPC",
            "VSwitch",
            "SecurityGroup"
```

`],`

```json
          "Label": {
            "default": "VPC "
          }
        },
        {
          "Parameters": [
            "EIPBandwidth",
            "EIPInternetChargeType"
```

`],`

```json
          "Label": {
            "default": "EIP"
          }
        },
        {
          "Parameters": [
            "ECSZoneId",
            "ECSImageId",
            "ECSInstanceType",
            "ECSDiskCategory",
            "ECSSysDiskSize",
            "InstanceChargeType",
            "ECSPassword",
            "KeyPairName"
```

`],`

```json
          "Label": {
            "default": "ECS"
          }
        }
```

`],`

```json
      "TemplateTags": [
        "Specify the image Id and snapshot to create ECS instance."
```

]

```json
    }
  },
  "Resources": {
    "ECSInstanceGroup": {
      "Type": "ALIYUN::ECS::InstanceGroup",
      "Properties": {
        "IoOptimized": "optimized",
        "InstanceChargeType": {
          "Ref": "InstanceChargeType"
        },
        "ZoneId": {
          "Ref": "ECSZoneId"
        },
        "SystemDisk_Category": {
```

资源编排

```json
          "Ref": "ECSDiskCategory"
        },
        "SecurityGroupId": {
          "Ref": "SecurityGroup"
        },
        "VSwitchId": {
          "Ref": "VSwitch"
        },
        "MaxAmount": 1,
        "SystemDisk_Size": {
          "Ref": "ECSSysDiskSize"
        },
        "VpcId": {
          "Ref": "VPC"
        },
        "ImageId": {
          "Ref": "ECSImageId"
        },
        "InstanceType": {
          "Ref": "ECSInstanceType"
        },
        "AllocatePublicIP": "false",
        "Password": {
          "Ref": "ECSPassword"
        },
        "KeyPairName": {
          "Ref": "KeyPairName"
        }
      }
    },
    "ElasticIp": {
      "Type": "ALIYUN::VPC::EIP",
      "Properties": {
        "Bandwidth": {
          "Ref": "EIPBandwidth"
        },
        "InternetChargeType": {
          "Ref": "EIPInternetChargeType"
        }
      }
    },
    "ElasticIpAssociation": {
      "Type": "ALIYUN::VPC::EIPAssociation",
      "Properties": {
        "InstanceId": {
          "Fn::Select": [
```

`0,`

```json
            {
              "Fn::GetAtt": [
                "ECSInstanceGroup",
                "InstanceIds"
```

]

```
            }
```

]

```json
        },
        "AllocationId": {
          "Ref": "ElasticIp"
        }
      }
    }
  },
  "Outputs": {
```

`"V`

```
Id" {
```

资源编排

```json
    "VpcId": {
      "Description": "VPC Id",
      "Value": {
        "Ref": "VPC"
      }
    },
    "SecurityGroupId": {
      "Description": "Security Group Id",
      "Value": {
        "Ref": "SecurityGroup"
      }
    },
    "VSwitchId": {
      "Description": "VSwitch Id",
      "Value": {
        "Ref": "VSwitch"
      }
    },
    "EipAddress": {
      "Description": "IP address of created EIP.",
      "Value": {
        "Fn::GetAtt": [
          "ElasticIp",
          "EipAddress"
```

]

```
      }
    }
  }
}
```

`YAML` 格式

```
ROSTemplateFormatVersion: '2015-09-01' Description:
  en: Create a VPC type ECS and bind EIP (existing VPC).
```

`zh-cn:` 创建`VPC`类型`ECS`，并绑定`EIP`（已有`VPC`）。

```
Parameters:
  VPC:
    Type: String
    Description:
      en: Please search the ID starting with (vpc-xxx) from console-Virtual Private Cloud.
```

`zh-cn:` 现有专有网络的实例`ID`，在专有网络控制台选择专有网络进行查询。

```
    Label:
      en: VPC ID
```

`zh-cn:` 专有网络`VPC`实例`ID`

```
  VSwitch:
    AssociationProperty: ALIYUN::ECS::VSwitch::VSwitchId
    AssociationPropertyMetadata:
      VpcId: VPC
    Type: String
    Description:
      en: Existing VSwitch ID, query under console-VPC-VSwitch, <font color='red'>VSwitch must be und
er VPC. ECS will be created under this VSwitch.</font>
```

`zh-cn:` 现有交换机`ID`，在专有网络控制台选择交换机进行查询，`<font color='red'>`交换机必须在`VPC`下。`ECS`将创建在此交换机下。`</font>`

```
    Label:
      en: VSwitch ID
```

`zh-cn:` 交换机实例`ID`

```
  SecurityGroup:
    Type: String
    AssociationProperty: ALIYUN::ECS::SecurityGroup::SecurityGroupId
```

D

```
iti
```

资源编排

```
    Description:
      en: Please search the business security group ID starting with (sg-xxx) from console-ECS-Networ
k & Security.
```

`zh-cn:` 现有业务安全组的实例`ID`，在`ECS`控制台选择安全组进行查询。`<br><font color='red'>`安全组必须归属在`VPC`下。

```
</font>
    Label:
      en: Business Security Group ID
```

`zh-cn:` 业务安全组`ID`

```
    AssociationPropertyMetadata:
      VpcId: VPC
  ECSPassword:
    NoEcho: true
    Type: String
    Description:
      en: Server login password, Length 8-30, must contain three (Capital letters, lowercase letters,
numbers, ()`~!@#$%^&*_-+=|{}[]:;'<>,.?/ Special symbol in).
```

`zh-cn:` 服务器登录密码，长度为8~30个字符，必须包含三项（大写英文字母、小写英文字母、数字和 ()`~!@#$%^&*_-+=|{ }[]:;'<>,.?/ 中的特殊字符）。

```
    AllowedPattern: '[0-9A-Za-z\_\-\&:;''<>,=%`~!@#\(\)\$\^\*\+\|\{\}\[\]\.\?\/]+$'
    Label:
      en: Instance Password
```

`zh-cn:` 实例密码

```
    MinLength: 8
    ConstraintDescription:
      en: Length 8-30, must contain three (Capital letters, lowercase letters, numbers,
()`~!@#$%^&*_-+=|{}[]:;'<>,.?/ Special symbol in).
```

`zh-cn:` 长度为8~30个字符，必须包含三项（大写英文字母、小写英文字母、数字和 ()`~!@#$%^&*_-+=|{}[]:;'<>,.?/ 中的特殊字符）。

```
    MaxLength: 30
    Default: Null
  EIPInternetChargeType:
    Type: String
    AllowedValues:
      - PayByBandwidth
      - PayByTraffic
    Description:
      en: The charge type of EIP, PayByBandwidth；PayByTraffic.
```

`zh-cn:` 弹性公网`IP`的收费类型。`PayByBandwidth`：按带宽付费；`PayByTraffic`：按流量付费。

```
    Label:
      en: EIP Charge Type
```

`zh-cn:` 弹性公网`IP`的收费类型

```
    Default: PayByTraffic
  ECSImageId:
    Type: String
    AssociationProperty: ALIYUN::ECS::Instance::ImageId
    Description:
      en: Image ID，Please use Centos7.
```

`zh-cn:` 镜像`ID`，请使用`Centos7`。

```
    Label:
      en: Image
```

`zh-cn:` 镜像

```
    Default: ubuntu_14
  ECSZoneId:
    AssociationProperty: ALIYUN::ECS::Instance:ZoneId
    Type: String
    Description:
      en: 'Availability zone ID.<br><b>Note: <font color=''blue''>Before selecting, please confirm wh
ether the availability zone supports the specification of creating ECS resources. It is recommended t o be different from other switch availability zones</font></b ><br><font color=''red''>The switch ava ilability zone and the selected switch instance ID must be in the same availability zone.</font>'
```

`zh-cn:` 可用区`ID`。`<br><b>`注： `<font color='blue'>`选择前请确认该可用区是否支持创建`ECS`资源的规格，建议与其他交换机可用区不同`</font></b><br><font color='red'>`交换机可用区和已选择的交换机实例`ID`必须在同一个可用区。`</font>`

```
    Label:
```

资源编排

```
      en: VSwitch Availability Zone
```

`zh-cn:` 交换机可用区

```
  EIPBandwidth:
    Type: Number
    Description:
      en: 'EIP Bandwidth, Value range: [1,200], unit: Mbps.'
```

`zh-cn:` 弹性公网`IP`带宽。取值范围：1~200，单位：`Mbps`。

```
    MinValue: 1
    Label:
      en: EIP Bandwidth
```

`zh-cn:` 弹性公网`IP`带宽

```java
    MaxValue: 200
    Default: 1
  ECSInstanceType:
    AssociationPropertyMetadata:
      ZoneId: ECSZoneId
      InstanceChargeType: InstanceChargeType
    AssociationProperty: ALIYUN::ECS::Instance::InstanceType
    Type: String
    Description:
      en: <font color='blue'><b>1.Before selecting the model please confirm that the current
available zone under the model is in stock, some models need to be reported in advance</b></font><br> <font color='blue'><b>2.List of optional models</font><br></b></font>[ecs.c5.large <font color='green'>2vCPU 4GiB Intranet bandwidth1Gbps In-grid sending and receiving packages30MillionPPS</font>]<br></b>[ecs.c5.xlarge <font color='green'>4vCPU 8GiB Intranet bandwidth1 .5Gbps In-grid sending and receiving packages50MillionPPS</font>]<br></b>[ecs.c5.2xlarge <font color= 'green'>8vCPU 16GiB Intranet bandwidth2.5Gbps In-grid sending and receiving packages80MillionPPS</font>]
```

`zh-cn: <font color='blue'><b>1`、选择机型前请先确认当前可用区下该机型是否有货，部分机型需要提前报备。`</b></f`

```
ont><br><font color='blue'><b>2、取值：</font><br></b></font>[ecs.c5.large：<font color='green'>2vCPU
```

`4 GiB`，内网带宽`1Gbps`、内网收发包`30`万`PPS`。`</font>]<br></b>[ecs.c5.xlarge`：`<font color='green'>4vCPU 8GiB`， 内网带宽`1.5Gbps`、内网收发包`50`万`PPS`。`</font>]<br></b>[ecs.c5.2xlarge`： `<font color='green'>8vCPU 16 GiB`，内网带宽`2.5 Gbps`、内网收发包`80`万`PPS`。`</font>]`

```
    Label:
      en: Instance Type
```

`zh-cn:` 实例规格

```
  ECSDiskCategory:
    Type: String
    Description:
      en: '<font color=''blue''><b>Optional values:</b></font><br>[cloud_efficiency: <font
color=''green''>Efficient Cloud Disk</font>]<br>[cloud_ssd: <font color=''green''>SSD Cloud Disk</font>]<br>[cloud_essd: <font color=''green''>ESSD Cloud Disk</font>]<br>[cloud: <font color=''g reen''>Cloud Disk</font>]<br>[ephemeral_ssd: <font color=''green''>Local SSD Cloud Disk</font>]'
      zh-cn: '<font color=''blue''><b>取值：</b></font><br>[cloud_efficiency: <font color=''green''>高
效云盘</font>]<br>[cloud_ssd: <font color=''green''>SSD云盘</font>]<br>[cloud_essd: <font color=''green ''>ESSD云盘</font>]<br>[cloud: <font color=''green''>普通云盘</font>]<br>[ephemeral_ssd: <font color='' green''>本地SSD盘</font>]'
    AssociationProperty: ALIYUN::ECS::Disk::SystemDiskCategory
    AssociationPropertyMetadata:
      ZoneId: ECSZoneId
      InstanceType: ECSInstanceType
    Label:
      en: System Disk Type
```

`zh-cn:` 系统盘类型

```
  ECSSysDiskSize:
    Type: Number
    Description:
      en: 'System disk size, range of values: 40-500, units: GB.'
```

`zh-cn:` 系统盘大小，取值范围：40~500，单位：`GB`。

```
    MinValue: 40
    Label:
      en: System Disk Space
```

系统盘空间资源编排 `zh-cn:` 系统盘空间

```
    MaxValue: 500
    Default: 40
  InstanceChargeType:
    Type: String
    Label:
      en: Instance Charge Type
```

`zh-cn:` 实例的付费方式

```
    Description:
      en: '<font color=''blue''><b>Optional values:</b></font><br>[PostPaid: <font
color=''green''>Pay as you go.</font>]<br> [PrePaid: <font color=''green''>Prepaid, monthly subscript ion.</font>]'
      zh-cn: '<font color=''blue''><b>取值：</b></font><br>[PostPaid: <font color=''green''>按量付费。</
font>]<br>[PrePaid: <font color=''green''>预付费，包年包月。</font>]'
    AllowedValues:
      - PostPaid
      - PrePaid
    Default: PostPaid
  KeyPairName:
    Type: String
    AssociationProperty: ALIYUN::ECS::KeyPair::KeyPairName
    Label:
      en: Key Pair Name
```

`zh-cn:` 密钥对名称

```
    Description:
      en: If it is a Windows ECS instance, ignore this parameter. The default is blank.<br>If you hav
e filled in <font color='green'>key pair name</font>, <font color='green'>instance password< The cont ent of /font> will still be set in the instance, but the password login method in the Linux system wi ll be forbidden.<br><font color='red'>Please enter the name of the existing key pair. If you use the instance password Login, the key pair name does not need to be filled in.</font>
```

`zh-cn:` 如果是`Windows ECS`实例，则忽略该参数。默认为空。`<br>`如果已填写`<font color='green'>`密钥对名称 `</font>`，`<font color='green'>`实例密码`</font>`的内容仍会被设置到实例中，但是`Linux`系统中的密码登录方式会被禁止。 `<br><font color='red'>`请输入已有密钥对的名称。如使用实例密码登录，密钥对名称不需要填写。`</font>`

```
    Default: Null
Metadata:
  ALIYUN::ROS::Interface:
    ParameterGroups:
      - Parameters:
          - VPC
        Label:
          default: 'VPC '
      - Parameters:
          - EIPBandwidth
          - EIPInternetChargeType
        Label:
          default: EIP
      - Parameters:
          - ECSZoneId
          - ECSImageId
          - ECSInstanceType
          - ECSDiskCategory
          - ECSSysDiskSize
          - InstanceChargeType
          - ECSPassword
          - KeyPairName
        Label:
          default: ECS
    TemplateTags:
      - Specify the image Id and snapshot to create ECS instance.
Resources: ECSInstanceGroup:
```

资源编排

```
  ECSInstanceGroup:
    Properties:
      IoOptimized: optimized
      InstanceChargeType:
        Ref: InstanceChargeType
      ZoneId:
        Ref: ECSZoneId
      SystemDisk_Category:
        Ref: ECSDiskCategory
      SecurityGroupId:
        Ref: SecurityGroup
      VSwitchId:
        Ref: VSwitch
      MaxAmount: 1
      SystemDisk_Size:
        Ref: ECSSysDiskSize
      VpcId:
        Ref: VPC
      ImageId:
        Ref: ECSImageId
      InstanceType:
        Ref: ECSInstanceType
      AllocatePublicIP: 'false'
      Password:
        Ref: ECSPassword
      KeyPairName:
        Ref: KeyPairName
  ElasticIp:
    Properties:
      Bandwidth:
        Ref: EIPBandwidth
      InternetChargeType:
        Ref: EIPInternetChargeType
  ElasticIpAssociation:
    Properties:
      InstanceId:
        Fn::Select:
          - 0
          - Fn::GetAtt:
              - InstanceIds
      AllocationId:
        Ref: ElasticIp
Outputs:
  VpcId:
    Description: VPC Id
    Value:
      Ref: VPC
  SecurityGroupId:
    Description: Security Group Id
    Value:
      Ref: SecurityGroup
  VSwitchId:
    Description: VSwitch Id
    Value:
      Ref: VSwitch
  EipAddress:
    Description: IP address of created EIP.
    Value:
       Fn::GetAtt:
```

资源编排

```
        - ElasticIp
        - EipAddress
```

#### ALIYUN::VPC::PeeringRouterInterfaceBinding

ALIYUN::VPC::PeeringRouterInterfaceBinding类型用于绑定将要互联的两个路由器接口信息。

**语法**

```json
{
  "Type": "ALIYUN::VPC::PeeringRouterInterfaceBinding",
  "Properties": {
    "OppositeRouterId": String,
    "OppositeInterfaceId": String,
    "OppositeInterfaceOwnerId": String,
    "RouterInterfaceId": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| RouterInterfaceI d | String | 是 | 否 | 路由器接口ID。 | 无。 |
| OppositeInterfac eId | String | 是 | 否 | 连接对端的路由器接口ID。 | 无。 |
| OppositeRouterI d | String | 否 | 否 | 连接对端的路由器接口所属的路由器 ID。 | 无。 |
| OppositeInterfac eOwnerId | String | 否 | 否 | 连接对端路由器接口的持有者账号 ID。 | 无。 |

**返回值**

Fn::GetAtt RouterInterfaceId：路由器ID。

**示例**

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "InitiatorRouterInterfaceBinding": {
      "Type": "ALIYUN::VPC::PeeringRouterInterfaceBinding",
      "Properties": {
        "RouterInterfaceId": "ri-2zedgo0ih64g1me29****",
        "OppositeInterfaceId": "ri-2zex1tkyym98pjaor****",
        "OppositeRouterId": "vrt-2zexb35tzoriu0286****"
      }
    }
  }
}
```

资源编排

**7.12.4.**

#### ALIYUN::VPC::PeeringRouterInterfaceConnection

ALIYUN::VPC::PeeringRouterInterfaceConnection类型用于发起路由器接口链接。

**语法**

```json
{
  "Type": "ALIYUN::VPC::PeeringRouterInterfaceConnection",
  "Properties": {
    "OppositeInterfaceId": String,
    "RouterInterfaceId": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| OppositeInterfac eId | String | 是 | 否 | 接收端路由器接口的ID。 | 无。 |
| RouterInterfaceI d | String | 是 | 否 | 要发起连接的路由器接口的ID。 | 无。 |

**返回值**

Fn::GetAtt OppositeInterfaceId：接收端路由器接口的ID。 RouterInterfaceId：要发起连接的路由器接口的ID。

**示例**

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "InitiatorRouterInterfaceBinding": {
      "Type": "ALIYUN::VPC::PeeringRouterInterfaceConnection",
      "Properties": {
        "RouterInterfaceId": "ri-2zedgo0ih64g1me29****",
        "OppositeInterfaceId": "ri-2ze4k5n2aeardu8cy****"
      }
    }
  }
}
```

#### ALIYUN::VPC::RouterInterface

**语法**

资源编排

```json
{
  "Type": "ALIYUN::VPC::RouterInterface",
  "Properties": {
    "OppositeRegionId": String,
    "Description": String,
    "HealthCheckSourceIp": String,
    "RouterType": String,
    "AccessPointId": String,
    "RouterId": String,
    "Role": String,
    "OppositeInterfaceOwnerId": String,
    "OppositeAccessPointId": String,
    "OppositeInterfaceId": String,
    "HealthCheckTargetIp": String,
    "OppositeRouterId": String,
    "Spec": String,
    "OppositeRouterType": String,
    "Name": String,
    "PricingCycle": String,
    "Period": Number,
    "AutoPay": Boolean,
    "InstanceChargeType": String
  }
}
```

**属性**

| 属性名称 | 类型 | 必须 | 允许更新 | 描述 | 约束 |
|---|---|---|---|---|---|
| RouterId | String | 是 | 否 | 路由器ID。 | 无 |
| Role | String | 是 | 否 | 连接中扮演的角色。即， 是连接发起端还是连接接受端。 | 取值： InitiatingSide RouterType取值为 VBR时，该参数取值必须为InitiatingSide。 AcceptingSide OppositeRouterTyp e取值为VBR时，该参数取值必须为 AcceptingSide。 |
| RouterType | String | 否 | 否 | 所属的路由器类型。 | 取值： VRouter：VPC路由器。 VBR：边界路由器。 |
| AccessPointId | String | 否 | 否 | 所属的接入点ID。 | RouterType取值为VBR 时该参数必须指定，而且创建后不允许修改。在 RouterType取值为 VRouter时，不能指定该参数。 |

资源编排

| Spec | String | 否 | 否 | 路由器接口的规格。 | 可用的规格和对应的带宽如下： Mini.2：2Mbps Mini.5：5Mbps Small.1：10Mbps Small.2：20Mbps Small.5：50Mbps Middle.1：100Mbps Middle.2：200Mbps Middle.5：500Mbps Large.1：1000 Mbps Large.2：2000Mbps Large.5：5000 Mbps Xlarge.1： 10000Mbps Role取值为 InitiatingSide时，该参数必须指定。 Role参数取值为 AcceptingSide时，该参数取值默认为 Negative。 |
|---|---|---|---|---|---|
| OppositeRegi onId | String | 否 | 否 | 要连接的对端所在的地域。 | 无 |
| OppositeInter faceOwnerId | String | 否 | 是 | 连接对端路由器接口的持有者账号ID。 | 默认是当前用户的ID。 |
| OppositeInter faceId | String | 否 | 是 | 对端路由器接口ID。 | 无 |
| OppositeRout erId | String | 否 | 是 | 要连接的对端的路由器的 ID。 | 无 |
| OppositeRout erType | String | 否 | 是 | 要连接的对端路由器接口所属的路由器类型。 | 取值： VRouter：VPC路由器。 RouterType取值为 VBR时，该参数取值必须是VRouter。 VBR：边界路由器。 |
| OppositeAcce ssPointId | String | 否 | 否 | 对端所属的接入点ID。 | OppositeRouterType取值为VBR时该参数必须指定，而且创建后不允许修改。 OppositeRouterType取值为VRouter时，不能指定该参数。 说明 OppositeRouterTy pe取值为VBR时 OppositeRouterId 所指定的VBR必须在 OppositeAccessPo intId所指定的接入点内。 |

资源编排

| Description | String | 否 | 是 | 路由器接口描述。 | 长度为2~256个字符。不能以 http:// 和 http s:// 开头。 不填则为空，默认为空。 |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | http |  |
| Name | String | 否 | 是 | 路由器接口显示名称。 | 长度为2~128个字符。必须以英文字母或汉字开头，不能以 http:// 和 http s:// 开头。可包含英文字母、汉字、数字、英文句点（.）、下划线（ ） _ 和短划线（-）。 |  |  |
|  |  |  |  |  |  | http |  |
| HealthCheckS ourceIp | String | 否 | 否 | 专线容灾和ECMP场景下用来做专线健康检查的 Packet的源IP。 | 只对本端是VRouter，而且对端是VB的路由器接口有效。必须是本端 VRouter所在的VPC内的一个未被使用的IP。 HealthCheckSourceIp 与 HealthCheckTargetIp 必须同时指定，或同时不指定。 |  |  |
| HealthCheckT argetIp | String | 否 | 否 | 专线容灾和ECMP场景下用来做专线健康检查的 Packet的目标IP。 | 只对本端是VRouter，而且对端是VBR的路由器接口有效。通常可以用专线用户端CPE的IP（即对端 RI所在的VBR上的 PeerGatewayIp），也可以指定专线用户端的其他IP。 HealthCheckSourceIp 与 HealthCheckTargetIp 必须同时指定，或同时不指定。 |  |  |
| PricingCycle | String | 否 | 否 | 预付费的计费周期。 | 取值： Month：按月付费。 Year：按年付费。 |  |  |
| Period | Number | 否 | 否 | 购买时长。 | 取值： 当选择按月付费时，取值范围：1~9。 当选择按年付费时，取值范围：1~3。 |  |  |
| AutoPay | Boolean | 否 | 否 | 自动付款。 | 取值： true false（默认值） |  |  |
| InstanceChar geType | String | 否 | 否 | 实例的付费类型。 | 取值： Postpaid：后付费 （按量付费）。 Prepaid：预付费（包年包月）。 |  |  |

|  |  | http:// |
|---|---|---|
|  | s:// |  |

|  |  | http:// |
|---|---|---|
|  | s:// |  |

**返回值**

Fn::GetAtt RouterInterfaceId：路由器接口ID。

**示例**

资源编排 `JSON` 格式

```json
{
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "OppositeInterfaceId": {
      "Type": "String",
      "Description": "The ID of the peer router interface."
    },
    "OppositeInterfaceOwnerId": {
      "Type": "String",
      "Description": "Owner account ID of the connection peer RouterInterface. The default value is c
urrent user Id."
    },
    "Description": {
      "Type": "String",
      "Description": "Custom description of the RouterInterface, [2, 256] characters. Don't fill or e
mpty, the default is empty."
    },
    "OppositeRouterId": {
      "Type": "String",
      "Description": "The router ID of the connection peer RouterInterface."
    },
    "OppositeRegionId": {
      "Type": "String",
      "Description": "The region where the connection peer RouterInterface locates. The default value
is region where stack is created."
    },
    "PricingCycle": {
      "Type": "String",
      "Description": "Unit of the payment cycle. It could be Month (default) or Year.",
      "AllowedValues": [
        "Month",
        "Year"
```

]

```json
    },
    "InstanceChargeType": {
      "Type": "String",
      "Description": "The billing method of the router interface. Valid values: PrePaid
(Subscription), PostPaid (default, Pay-As-You-Go)",
      "AllowedValues": [
        "PrePaid",
        "PostPaid"
```

`],`

```json
      "Default": "PostPaid"
    },
    "HealthCheckSourceIp": {
      "Type": "String",
      "Description": "Source IP address of the packet for leased line HealthCheck in leased line disa
ster tolerance and ECMP scenarios. It is valid only for a VRouter RouterInterface with a peer on a VB R. The source IP address must be in the VPC of the local VRouter and is not used. HealthCheckSourceIp and HealthCheckTargetIp parameters must be both specified or left unspecified."
    },
    "Period": {
      "Type": "Number",
      "Description": "Prepaid time period. It could be from 1 to 9 when PricingCycle is Month, or 1 t
o 3 when PricingCycle is Year. Default value is 3.",
      "AllowedValues": [
```

`1,` `2,` `3,` `4,` 资源编排 `5,` `6,` `7,` `8,` ]

```json
    },
    "RouterId": {
      "Type": "String",
      "Description": "The router ID to create RouterInterface."
    },
    "AutoPay": {
      "Type": "Boolean",
      "Description": "Indicates whether automatic payment is enabled. Valid values:false: Automatic p
ayment is disabled. You need to go to Orders to make the payment once an order is generated. true: Au tomatic payment is enabled. The payment is automatically made.",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

]

```json
    },
    "Name": {
      "Type": "String",
      "Description": "Custom name of the RouterInterface, [2, 128] English or Chinese characters, mus
t start with a letter or Chinese in size, can contain numbers, '_' or '.', '-'"
    },
    "Role": {
      "Type": "String",
      "Description": "RouterInterface role. Now support 'InitiatingSide|AcceptingSide'. If
'RouterType' is specified as 'VBR', the value must be 'InitiatingSide'.If 'OppositeRouterType' is spe cified as 'VBR', the value must be 'AcceptingSide'.",
      "AllowedValues": [
        "InitiatingSide",
        "AcceptingSide"
```

]

```json
    },
    "OppositeRouterType": {
      "Type": "String",
      "Description": "Router type of the connection peer router. Now support 'VRouter|VBR'. If
'RouterType' is specified as 'VBR', the value must be 'VRouter'.",
      "AllowedValues": [
        "VRouter",
        "VBR"
```

`],`

```json
      "Default": "VRouter"
    },
    "RouterType": {
      "Type": "String",
      "Description": "Router type. Now support 'VRouter|VBR'",
      "AllowedValues": [
        "VRouter",
        "VBR"
```

`],`

```json
      "Default": "VRouter"
    },
    "AccessPointId": {
      "Type": "String",
      "Description": "Access point ID. If 'RouterType' is specified as 'VBR', the value is required."
    },
    "OppositeAccessPointId": {
      "Type": "String",
```

资源编排

```json
      "Description": "Access point ID of the connection peer RouterInterface. If 'OppositeRouterType'
is specified as 'VBR', the value is required."
    },
    "Spec": {
      "Type": "String",
      "Description": "RouterInterface specification. If 'Role' is specified as 'InitiatingSide', the
value is required. If 'Role' is specified as 'AcceptingSide', the value is set as 'Negative' by defau lt."
    },
    "HealthCheckTargetIp": {
      "Type": "String",
      "Description": "Target IP address of the packet for leased line HealthCheck in leased line disa
ster tolerance and ECMP scenarios. It is valid only for a VRouter RouterInterface with a peer on a VB R. Usually you can use the CPE IP address of the leased line user's client (that is, the PeerGatewayI P on the VBR of the peer RouterInterface), you can also specify another IP address of the leased line user's client as the HealthCheck target IP address. HealthCheckSourceIp and HealthCheckTargetIp param eters must be both specified or left unspecified."
    }
  },
  "Resources": {
    "RouterInterface": {
      "Type": "ALIYUN::VPC::RouterInterface",
      "Properties": {
        "OppositeInterfaceId": {
          "Ref": "OppositeInterfaceId"
        },
        "OppositeInterfaceOwnerId": {
          "Ref": "OppositeInterfaceOwnerId"
        },
        "Description": {
          "Ref": "Description"
        },
        "OppositeRouterId": {
          "Ref": "OppositeRouterId"
        },
        "OppositeRegionId": {
          "Ref": "OppositeRegionId"
        },
        "PricingCycle": {
          "Ref": "PricingCycle"
        },
        "InstanceChargeType": {
          "Ref": "InstanceChargeType"
        },
        "HealthCheckSourceIp": {
          "Ref": "HealthCheckSourceIp"
        },
        "Period": {
          "Ref": "Period"
        },
        "RouterId": {
          "Ref": "RouterId"
        },
        "AutoPay": {
          "Ref": "AutoPay"
        },
        "Name": {
          "Ref": "Name"
        },
        "Role": {
          "Ref": "Role"
        },
"OppositeRoterTpe" {
```

资源编排

```json
        "OppositeRouterType": {
          "Ref": "OppositeRouterType"
        },
        "RouterType": {
          "Ref": "RouterType"
        },
        "AccessPointId": {
          "Ref": "AccessPointId"
        },
        "OppositeAccessPointId": {
          "Ref": "OppositeAccessPointId"
        },
        "Spec": {
          "Ref": "Spec"
        },
        "HealthCheckTargetIp": {
          "Ref": "HealthCheckTargetIp"
        }
      }
    }
  },
  "Outputs": {
    "RouterInterfaceId": {
      "Description": "The ID of created RouterInterface.",
      "Value": {
        "Fn::GetAtt": [
          "RouterInterface",
          "RouterInterfaceId"
```

]

```
      }
    }
  }
}
```

`YAML` 格式

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  OppositeInterfaceId:
    Type: String
    Description: The ID of the peer router interface.
  OppositeInterfaceOwnerId:
    Type: String
    Description: >-
      Owner account ID of the connection peer RouterInterface. The default value
      is current user Id.
  Description:
    Type: String
    Description: >-
      Custom description of the RouterInterface, [2, 256] characters. Don't fill
      or empty, the default is empty.
  OppositeRouterId:
    Type: String
    Description: The router ID of the connection peer RouterInterface.
  OppositeRegionId:
    Type: String
    Description: >-
      The region where the connection peer RouterInterface locates. The default
      value is region where stack is created.
  PricingCycle:
    Type: String
    Description: Unit of the payment cycle. It could be Month (default) or Year.
All dVl
```

资源编排

```
    AllowedValues:
      - Month
      - Year
  InstanceChargeType:
    Type: String
    Description: >-
      The billing method of the router interface. Valid values: PrePaid
      (Subscription), PostPaid (default, Pay-As-You-Go)
    AllowedValues:
      - PrePaid
      - PostPaid
    Default: PostPaid
  HealthCheckSourceIp:
    Type: String
    Description: >-
      Source IP address of the packet for leased line HealthCheck in leased line
      disaster tolerance and ECMP scenarios. It is valid only for a VRouter
      RouterInterface with a peer on a VBR. The source IP address must be in the
      VPC of the local VRouter and is not used. HealthCheckSourceIp and
      HealthCheckTargetIp parameters must be both specified or left unspecified.
  Period:
    Type: Number
    Description: >-
      Prepaid time period. It could be from 1 to 9 when PricingCycle is Month,
      or 1 to 3 when PricingCycle is Year. Default value is 3.
    AllowedValues:
      - 1
      - 2
      - 3
      - 4
      - 5
      - 6
      - 7
      - 8
      - 9
  RouterId:
    Type: String
    Description: The router ID to create RouterInterface.
  AutoPay:
    Type: Boolean
    Description: >-
      Indicates whether automatic payment is enabled. Valid values:false:
      Automatic payment is disabled. You need to go to Orders to make the
      payment once an order is generated. true: Automatic payment is enabled.
      The payment is automatically made.
    AllowedValues:
      - 'True'
      - 'true'
      - 'False'
      - 'false'
  Name:
    Type: String
    Description: >-
      Custom name of the RouterInterface, [2, 128] English or Chinese
      characters, must start with a letter or Chinese in size, can contain
      numbers, '_' or '.', '-'
  Role:
    Type: String
    Description: >-
      RouterInterface role. Now support 'InitiatingSide|AcceptingSide'. If
      'RouterType' is specified as 'VBR', the value must be 'InitiatingSide'.If
      'OppositeRouterType' is specified as 'VBR', the value must be
      'AcceptingSide'.
```

资源编排 p g

```
    AllowedValues:
      - InitiatingSide
      - AcceptingSide
  OppositeRouterType:
    Type: String
    Description: >-
      Router type of the connection peer router. Now support 'VRouter|VBR'. If
      'RouterType' is specified as 'VBR', the value must be 'VRouter'.
    AllowedValues:
      - VRouter
      - VBR
    Default: VRouter
  RouterType:
    Type: String
    Description: Router type. Now support 'VRouter|VBR'
    AllowedValues:
      - VRouter
      - VBR
    Default: VRouter
  AccessPointId:
    Type: String
    Description: >-
      Access point ID. If 'RouterType' is specified as 'VBR', the value is
      required.
  OppositeAccessPointId:
    Type: String
    Description: >-
      Access point ID of the connection peer RouterInterface. If
      'OppositeRouterType' is specified as 'VBR', the value is required.
  Spec:
    Type: String
    Description: >-
      RouterInterface specification. If 'Role' is specified as 'InitiatingSide',
      the value is required. If 'Role' is specified as 'AcceptingSide', the
      value is set as 'Negative' by default.
  HealthCheckTargetIp:
    Type: String
    Description: >-
      Target IP address of the packet for leased line HealthCheck in leased line
      disaster tolerance and ECMP scenarios. It is valid only for a VRouter
      RouterInterface with a peer on a VBR. Usually you can use the CPE IP
      address of the leased line user's client (that is, the PeerGatewayIP on
      the VBR of the peer RouterInterface), you can also specify another IP
      address of the leased line user's client as the HealthCheck target IP
      address. HealthCheckSourceIp and HealthCheckTargetIp parameters must be
      both specified or left unspecified.
Resources:
  RouterInterface:
    Properties:
      OppositeInterfaceId:
        Ref: OppositeInterfaceId
      OppositeInterfaceOwnerId:
        Ref: OppositeInterfaceOwnerId
      Description:
        Ref: Description
      OppositeRouterId:
        Ref: OppositeRouterId
      OppositeRegionId:
        Ref: OppositeRegionId
      PricingCycle:
        Ref: PricingCycle
```

资源编排

```
      InstanceChargeType:
        Ref: InstanceChargeType
      HealthCheckSourceIp:
        Ref: HealthCheckSourceIp
      Period:
        Ref: Period
      RouterId:
        Ref: RouterId
      AutoPay:
        Ref: AutoPay
      Name:
        Ref: Name
      Role:
        Ref: Role
      OppositeRouterType:
        Ref: OppositeRouterType
      RouterType:
        Ref: RouterType
      AccessPointId:
        Ref: AccessPointId
      OppositeAccessPointId:
        Ref: OppositeAccessPointId
      Spec:
        Ref: Spec
      HealthCheckTargetIp:
        Ref: HealthCheckTargetIp
Outputs:
  RouterInterfaceId:
    Description: The ID of created RouterInterface.
    Value:
      'Fn::GetAtt':
        - RouterInterfaceId
```
