---
title: "智能体工厂 OpenTrek Agent Dev开发指南"
product_version: "V2.17.0"
doc_version: "20260902"
pdf_pages: 475
source_pdf: "05_Agent Dev开发指南_opentrek-agengt-dev-aistack-development-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/ai_stack/v_2_17_0_20260828/opentrek/zh/opentrek-agengt-dev-aistack-development-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 智能体工厂 OpenTrek Agent Dev开发指南

智能体工厂 OpenTrek 发指南

## Agent Dev开发指南

### 准备工作

本章节介绍使用接口前到准备工作。

#### 获取API_Key

开放接口使用API-Keys鉴权，是一种身份验证机制，用于控制对API的访问权限。在使用API调用前，您需要提供有效的密钥来证明其身份，以获得对API的访问权限。以下为您介绍如何获取应用中心接口的API- Keys。

**操作步骤**

1. 登录OpenTrek Dev。
2. 在左侧导航栏左边**集成开放** **> APP_KEY**。
3. 按照要求填对应的数据
智能体工厂 OpenTrek 发指南
4. 在**获取密钥**页面单击
图标复制密钥后可单击**确定**关闭窗口，生成的API-Key名称会在密钥列表显示。

**重要**

请将此密钥保存在安全且可访问的地方。 出于安全原因，密钥只展示一次，您关闭此窗口后将无法再次查看它，请及时复制保存。 如果您丢失了此密钥，需要重新执行以上并生成一个新的密钥。

### 平台功能类

平台管控区相关接口服务

#### 接口文档

##### 智能体管理

###### 智能体

###### 查询智能体版本列表

**接口概述**

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/agent/openapi/agent/version/pageQuery POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostAgentOpenapiAgentVersionPagequery

**请求头**

智能体工厂 OpenTrek 发指南

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| current | Integ er | Body | 是 | 1 | 当前页数，该参数必填 |
| pageSize | Integ er | Body | 是 | 10 | 每页条数，该参数必填 |
| agentCode | Strin g | Body | 是 | 905a3aaa-5797-47fb- ac71-b8dcd88b9ac0 | 智能体编码，该参数必填 |
| versionNa me | Strin g | Body | 是 | 1.0 | 版本名称模糊搜索，该参数必填 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | Object | 返回数据 | {} |
| total | Integer | 查询到的智能体版本总数 | 1 |
| list | List | 查询到的智能体版本列表 |  |
| agentCode | String | 智能体唯一编码 | a9c81580-8e93-42e1- b331-5cc6506c0093 |
| agentName | String | 智能体名称 | DB 随表召回 |

智能体工厂 OpenTrek 发指南

| agentDefinition | String | 智能体描述 | DB 随表召回 |
|---|---|---|---|
| versionName | String | 版本名称 | 知识库检查 |
| agentVersion | String | 版本编码 | 1757388497303 |
| agentStatus | String | 版本状态。DEV=设计中, ONLINE=已上线, OFFLINE=已下线 | DEV |
| gmtCreate | String | 创建时间 | 2025-08- 29T11:43:54.722+00: 00 |
| gmtModified | String | 修改时间 | 2025-08- 29T11:43:54.722+00: 00 |
| pageSize | Integer | 每页大小 | 60 |
| current | Integer | 目前所在页数 | 1 |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式

```json
{
  "errorMessages": [],
  "success": true,
  "data": {
    "extInfos": {},
    "total": 1,
    "list": [
      {
        "id": 759,
        "gmtCreate": "2025-11-11T12:19:54.315+00:00",
        "gmtModified": "2025-11-11T12:19:54.315+00:00",
        "tenant": "fmthktsjdb",
        "agentCode": "9456fd9d-1a55-43b0-b383-f1331e81e69d",
        "agentName": "testAgent",
        "agentVersion": "1762863594309",
        "versionName": "版本1",
        "agentDefinition": "testUpdate",
```

`"d` l "

```
{
```

智能体工厂 OpenTrek 发指南

```json
        "developer": {
          "id": null,
          "gmtCreate": null,
          "gmtModified": null,
          "tenant": null,
          "uniqueCode": "7b7d340c8ec04c9db0c8c072e3d5e690",
          "source": null,
          "outerId": null,
```

`"name": "`日常管理员"

```json
        },
        "pd": {
          "id": null,
          "gmtCreate": null,
          "gmtModified": null,
          "tenant": null,
          "uniqueCode": "7b7d340c8ec04c9db0c8c072e3d5e690",
          "source": null,
          "outerId": null,
```

`"name": "`日常管理员"

```json
        },
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
        },
        "modelConfig": null,
        "scriptConfig": {
          "engineName": null,
          "script": null
        },
        "availableToolsConfig": null,
        "createType": null,
        "method": null,
        "configMethod": null,
        "icon": null,
        "jumpUrl": null,
        "flowType": "workflow",
        "templateType": null,
        "canDeployTemplate": false
      }
```

`],`

```json
    "pageSize": 10,
    "current": 1,
    "totalPages": 1
  },
  "errorCode": null,
  "errorMsg": null,
  "extraData": null,
"traceId":null
```

智能体工厂 OpenTrek 发指南

```json
  traceId: null,
  "env": null,
  "other": null,
  "firstErrorMessage": null,
  "failure": false
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
|---|---|---|
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 写入记忆分区内容

**接口概述**

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/agent/openapi/memory/longTerm/partition/add POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostAgentOpenapiMemoryLongtermPartitionAdd

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| partitionCo de | Strin g | Body | 是 | 1111 | 分区编码，该参数必填 |
| storageKe y | Strin g | Body | 是 | key | 键值对-KEY，该参数必填 |
| storageVal ue | Strin g | Body | 是 | value | 键值对-VALUE，该参数必填 |

智能体工厂 OpenTrek 发指南

| storageCo ntent | Strin g | Body | 是 | example | 文本，该参数必填 |
|---|---|---|---|---|---|
| memoryUs erId | Strin g | Body | 是 | 1234 | 记忆用户ID，该参数必填 |
| status | Integ er | Body | 是 | 0 | 状态 0:正常 1:删除 2:禁用， 该参数必填 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | Object | 返回数据 | {} |
| memoryCode | String | 记忆编码 | a9c81580-8e93-42e1- b331-5cc6506c0093 |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式

```json
{
  "errorMessages": [],
  "success": false,
  "data": null,
  "errorCode": "-1",
```

`"errorMsg": "`记忆分区不存在`",`

```json
  "extraData": null,
  "traceId": null,
  "env": null,
  "other": null,
  "firstErrorMessage": null,
  "failure": false
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
|---|---|---|
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 创建智能体

**接口概述**

智能体工厂 OpenTrek 发指南

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/agent/openapi/agent/create POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostAgentOpenapiAgentCreate

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| agentNam e | Strin g | Body | 是 | DB 随表召回 | 智能体名称，该参数必填 |
| agentDesc | Strin g | Body | 是 | DB 随表召回 | 智能体描述，该参数必填 |

**返回参数**

| 字段 | 数据类型 | 描述 |
|---|---|---|
| success | Boolean | 是否成功 |
| data | Object | 返回数据 |
| agentCode | String | 智能体唯一编码 |
| agentName | String | 智能体名称 |
| agentDesc | String | 智能体描述 |

智能体工厂 OpenTrek 发指南

| workspaceCode | String | 所属工作空间编码 |
|---|---|---|
| gmtCreate | String | 创建时间 |
| gmtModified | String | 修改时间 |
| errorCode | String | 错误码 |
| errorMsg | String | 错误描述 |

**示例**

`JSON` 格式智能体工厂 OpenTrek 发指南

```json
{
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
    },
    "pd": {
      "id": null,
      "gmtCreate": null,
      "gmtModified": null,
      "tenant": null,
      "uniqueCode": "7b7d340c8ec04c9db0c8c072e3d5e690",
      "source": null,
      "outerId": null,
      "name": "daily_root"
    },
    "outputVersions": null,
    "workspaceCode": "fmthktsjdb",
    "agentApiLimitConfig": null
  },
  "errorCode": null,
  "errorMsg": null,
  "extraData": null,
  "traceId": null,
  "env": null,
  "other": null,
  "firstErrorMessage": null,
  "failure": false
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
|---|---|---|
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 创建智能体版本

**接口概述**

智能体工厂 OpenTrek 发指南

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/agent/openapi/agent/version/create POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostAgentOpenapiAgentVersionCreate

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| agentCode | Strin g | Body | 是 | 905a3aaa-5797-47fb- ac71-b8dcd88b9ac0 | 智能体编码，该参数必填 |
| versionNa me | Strin g | Body | 是 | 版本1 | 版本描述，该参数必填 |
| flowType | Strin g | Body | 是 | workflow | 创建模式，workflow=工作流，default=基于模版，该参数必填 |
| templateC ode | Strin g | Body | 是 | 3b7628cc51544996908b 6ea55ae07bc1 | 模版编码，创建模式为基于模版时必填 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | Object | 返回数据 | {} |

智能体工厂 OpenTrek 发指南

| agentCode | String | 智能体唯一编码 | a9c81580-8e93-42e1- b331-5cc6506c0093 |
|---|---|---|---|
| agentName | String | 智能体名称 | DB 随表召回 |
| agentVersion | String | 智能体版本 | 1759062292925 |
| versionName | String | 版本描述 | 版本1 |
| agentDesc | String | 智能体描述 | DB 随表召回 |
| workspaceCode | String | 所属工作空间编码 | baseline |
| gmtCreate | String | 创建时间 | 2025-08- 29T11:43:54.722+00: 00 |
| gmtModified | String | 修改时间 | 2025-08- 29T11:43:54.722+00: 00 |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式

```json
{
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
}
```

**文档补充说明**

智能体工厂 OpenTrek 发指南

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 删除智能体

智能体工厂 OpenTrek 发指南

**接口概述**

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/agent/openapi/agent/delete POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostAgentOpenapiAgentDelete

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| agentCode | Strin g | Body | 是 | a9c81580-8e93-42e1- b331-5cc6506c0093 | 智能体唯一编码，该参数必填 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式智能体工厂 OpenTrek 发指南

```json
{
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
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |

智能体工厂 OpenTrek 发指南

| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
|---|---|---|
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 编辑智能体

**接口概述**

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/agent/openapi/agent/update POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostAgentOpenapiAgentUpdate

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| agentCode | Strin g | Body | 是 | a9c81580-8e93-42e1- b331-5cc6506c0093 | 智能体唯一编码，该参数必填 |

智能体工厂 OpenTrek 发指南

| agentNam e | Strin g | Body | 是 | DB 随表召回 | 智能体名称，该参数必填 |
|---|---|---|---|---|---|
| agentDesc | Strin g | Body | 是 | DB 随表召回 | 智能体描述，该参数必填 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | Boolean | 是否成功 | true |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式

```json
{
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
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
|---|---|---|
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 编辑智能体版本

**接口概述**

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/agent/openapi/agent/version/update 智能体工厂 OpenTrek 发指南 POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostAgentOpenapiAgentVersionUpdate

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| agentCode | Strin g | Body | 是 | a9c81580-8e93-42e1- b331-5cc6506c0093 | 智能体唯一编码，该参数必填 |
| agentVersi on | Strin g | Body | 是 | 1759062292925 | 智能体版本，该参数必填 |
| versionNa me | Strin g | Body | 是 | 版本1 | 版本名称，该参数必填 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | Boolean | 是否成功 | true |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式智能体工厂 OpenTrek 发指南

```json
{
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
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |

智能体工厂 OpenTrek 发指南

| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
|---|---|---|
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 删除智能体版本

**接口概述**

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/agent/openapi/agent/version/delete POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostAgentOpenapiAgentVersionDelete

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| agentCode | Strin g | Body | 是 | a9c81580-8e93-42e1- b331-5cc6506c0093 | 智能体唯一编码，该参数必填 |

智能体工厂 OpenTrek 发指南

| agentVersi on | Strin g | Body | 是 | 1759062292925 | 智能体版本，该参数必填 |
|---|---|---|---|---|---|

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式

```json
{
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
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
|---|---|---|
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 查询智能体列表

**接口概述**

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/agent/openapi/agent/pageQuery POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostAgentOpenapiAgentPagequery

**请求头**

智能体工厂 OpenTrek 发指南

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| current | Integ er | Body | 是 | 1 | 当前页数，该参数必填 |
| pageSize | Integ er | Body | 是 | 10 | 每页条数，该参数必填 |
| agentNam e | Strin g | Body | 是 | 智能体 | 智能体名称模糊搜索，该参数必填 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | Object | 返回数据 | {} |
| total | Integer | 查询到的智能体总数 | 1 |
| list | List | 查询到的智能体列表 |  |
| agentCode | String | 智能体唯一编码 | a9c81580-8e93-42e1- b331-5cc6506c0093 |
| agentName | String | 智能体名称 | DB 随表召回 |
| agentDesc | String | 智能体描述 | DB 随表召回 |

智能体工厂 OpenTrek 发指南

| workspaceCode | String | 所属工作空间编码 | baseline |
|---|---|---|---|
| gmtCreate | String | 创建时间 | 2025-08- 29T11:43:54.722+00: 00 |
| gmtModified | String | 修改时间 | 2025-08- 29T11:43:54.722+00: 00 |
| pageSize | Integer | 每页大小 | 60 |
| current | Integer | 目前所在页数 | 1 |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式

```json
{
  "errorMessages": [],
  "success": true,
  "data": {
    "extInfos": {},
    "total": 1,
    "list": [
      {
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
        },
```

智能体工厂 OpenTrek 发指南

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
        },
        "outputVersions": null,
        "workspaceCode": "fmthktsjdb",
        "agentApiLimitConfig": null
      }
```

`],`

```json
    "pageSize": 10,
    "current": 1,
    "totalPages": 1
  },
  "errorCode": null,
  "errorMsg": null,
  "extraData": null,
  "traceId": null,
  "env": null,
  "other": null,
  "firstErrorMessage": null,
  "failure": false
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |

智能体工厂 OpenTrek 发指南

| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
|---|---|---|
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 工具

###### 编辑工具

###### 编辑工具

**接口概述**

###### 编辑工具

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/agent/openapi/tool/update POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostAgentOpenapiToolUpdate

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek 发指南

| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
|---|---|---|---|---|---|
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| name | Strin g | Body | 否 | 测试工具 | 工具名称 |
| desc | Strin g | Body | 否 | 测试工具 | 工具描述 |
| serviceCon fig | Json | Body | 否 | {} | 工具配置 |
| toolType | Strin g | Body | 否 | api | 工具类型 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | Object | 返回数据 | {} |
| code | String | 工具编码 | a9c81580-8e93-42e1- b331-5cc6506c0093 |
| name | String | 工具名称 | 测试工具 |
| desc | String | 工具描述 | 测试工具 |
| version | String | 工具版本 | 1759118429269 |
| serviceConfig | Object | 工具配置 | {} |

智能体工厂 OpenTrek 发指南

| workspaceCode | String | 所属工作空间编码 | baseline |
|---|---|---|---|
| gmtCreate | String | 创建时间 | 2025-08- 29T11:43:54.722+00: 00 |
| gmtModified | String | 修改时间 | 2025-08- 29T11:43:54.722+00: 00 |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式

```json
{
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
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
|---|---|---|
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 查询工具列表

**接口概述**

**前提条件（查看APP_KEY）**

查询工具列表。可以通过查看请求示例，点击 curl 命令示例右侧的调试按钮验证业务接口调用效果。

**接口调用地址**

POST http://{host}/gatectl/agent/openapi/tool/pageQuery

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek 发指南

| x-sfm- authorizati on | Strin g | Hea der | 否 | Bearer YOUR APP KEY _ _ | APP KEY _ |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| current | Integ er | Body | 是 | 1 | 当前页数，该参数必填 |
| pageSize | Integ er | Body | 是 | 10 | 每页条数，该参数必填 |
| toolCatego ry | Strin g | Body | 是 | my | 分类，my=我的工具，platform=平台工具，该参数必填 |
| toolType | Strin g | Body | 是 | my | 工具类型，api=API，MY MCP=m _ cp工具，knowledge=知识库，该参数必填 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | Object | 返回数据 | {} |
| total | Integer | 查询到的智能体总数 | 1 |
| list | List | 查询到的智能体列表 |  |
| code | String | 工具编码 | 10110baseline |

智能体工厂 OpenTrek 发指南

| name | String | 工具名称 | doc-parse |
|---|---|---|---|
| desc | String | 工具描述 | 内置文档解析工具 |
| workspaceCode | String | 所属工作空间编码 | baseline |
| gmtCreate | String | 创建时间 | 2025-08- 29T11:43:54.722+00: 00 |
| gmtModified | String | 修改时间 | 2025-08- 29T11:43:54.722+00: 00 |
| toolType | String | 工具类型 | MCP |
| toolSubType | String | 工具子类型 | doc-parse |
| serviceConfig | Object | 工具配置 |  |
| pageSize | Integer | 每页大小 | 60 |
| current | Integer | 目前所在页数 | 1 |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式

```json
{
  "errorMessages": [],
  "success": true,
  "data": {
    "marketCode": "system",
```

`"marketName": "`自定义模版`",`

```json
    "itemCode": "3b7628cc51544996808b6ea55ae07bc1",
```

`"itemName": "AutoBot`对话助手`",`

```json
    "itemLabels": [
```

"系统内置" `],`

```json
    "itemType": "agentTemplate",
    "targetCode": "851d5b0b-8393-497c-b909-1d3209efee74",
```

智能体工厂 OpenTrek 发指南

```json
    "targetName": "v1.0",
    "targetVersion": "1731573095677",
    "status": "online",
    "statusDesc": "已上架",
    "operatorId": null,
    "operatorName": null,
    "showDetail": {
      "skills": [
```

"支持接入用户已有业务`api",` "支持`OneRag`插件联动用户业务数据`",` "支持接入其他智能体实例" `],`

```json
      "usage": {
        "attachment": {},
        "configDesc": "无",
        "limitDesc": "无"
      },
```

`"description": "`综合问答能力`",`

```json
      "interfaceInfo": {
        "inputParams": [
          {
            "example": "bd962db7-b1c8-4466-a2cc-41b9b67cd94b 创建session接口的返回值unique
Code",
            "label": "sessionId",
            "name": "sessionId",
            "necessary": true,
            "type": "STRING"
          },
          {
            "example": "true",
```

`"label": "`是否流式`",`

```json
            "name": "stream",
            "necessary": true,
            "type": "BOOL"
          },
          {
```

`"example": "true` 默认每次输出新内容,不包含前序输出的文本`",` `"label": "`当`stream=true,`控制是否不追加新文本`",`

```json
            "name": "delta",
            "necessary": true,
            "type": "BOOL"
          },
          {
```

`"example": "false` 默认不返回`trace`记录`",` `"label": "`当`trace=true,`控制是否返回`trace`记录`",`

```json
            "name": "trace",
            "necessary": false,
            "type": "BOOL"
          },
          {
            "children": [
              {
```

`"example": "`帮我订一张明天从上海去苏黎世的机票`",` `"label": "`对话输入`",` 智能体工厂 OpenTrek 发指南

```json
                "name": "text",
                "necessary": true,
                "type": "STRING"
              },
              {
                "example": "{}",
```

`"label": "`扩展信息`",`

```json
                "name": "metadata",
                "necessary": false,
                "type": "OBJECT"
              },
              {
                "children": [
                  {
                    "example": "{}",
```

`"label": "`附件地址`",`

```json
                    "name": "url",
                    "necessary": true,
                    "type": "STRING"
                  },
                  {
                    "example": "{}",
```

`"label": "`附件名称`",`

```json
                    "name": "name",
                    "necessary": false,
                    "type": "STRING"
                  }
```

`],`

```json
                "example": "[]",
```

`"label": "`附件信息`",`

```json
                "name": "attachments",
                "necessary": false,
                "type": "LIST<Object>"
              }
```

`],` "example": "{\"text\":\"帮我订一张明天从上海去苏黎世的机票\",\"metadata\":{}, \"a

```
ttachments\":[{\"url\":\"\",\"name\":\"\"}]}",
```

`"label": "`请求消息体`",`

```json
            "name": "message",
            "necessary": true,
            "type": "OBJECT"
          }
```

`],`

```json
        "interfaceDesc": "无",
        "outputParams": [
          {
```

`"example": "message.delta` 输出文本块 `thought.delta` 思考过程块 `error` 错误信息 `",` `"label": "`数据类型`",`

```json
            "name": "object",
            "necessary": true,
            "type": "STRING"
          },
          {
"example":"assistant"
```

智能体工厂 OpenTrek 发指南

```json
            "example": "assistant",
            "label": "角色",
            "name": "role",
            "necessary": true,
            "type": "STRING"
          },
          {
            "example": "object=message.delta场景 : {\"type\":\"text\",\"text\":
```

{\"value\":\"智能体回答内容增量\"}}object=thought.delta场景 : {\"type\":\"text\",\"data\":\"思考内容增量\"} object=error场景 {\"errorMsg\": \"错误信息内容

```
\"} ",
```

`"label": "`数据内容`",`

```json
            "name": "content",
            "necessary": true,
            "type": "OBJECT"
          },
          {
            "example": "{\"key\":\"value\"}",
```

`"label": "`扩展字段`",`

```json
            "name": "metadata",
            "necessary": false,
            "type": "OBJECT"
          },
          {
            "example": "false|true",
```

`"label": "`流式`(object=message.delta)`场景标记文本输出是否结束`",`

```json
            "name": "end",
            "necessary": true,
            "type": "BOOL"
          },
          {
            "example": "-",
```

`"label": "`当前会话`ID",`

```json
            "name": "sessionId",
            "necessary": true,
            "type": "STRING"
          },
          {
            "example": "-",
```

`"label": "`当前运行的请求`ID",`

```json
            "name": "requestId",
            "necessary": true,
            "type": "STRING"
          },
          {
            "example": "true",
```

`"label": "`非流式-业务是否成功`",`

```json
            "name": "success",
            "necessary": true,
            "type": "BOOL"
          },
          {
            "children": [
              {
"children":[
```

智能体工厂 OpenTrek 发指南

```json
                children: [
                  {
                    "example": "assistant",
                    "label": "角色",
                    "name": "role",
                    "necessary": true,
                    "type": "STRING"
                  },
                  {
                    "example": "{\"key\":\"value\"}",
```

`"label": "`扩展字段`",`

```json
                    "name": "metadata",
                    "necessary": false,
                    "type": "OBJECT"
                  },
                  {
                    "children": [
                      {
                        "example": "text|image",
```

`"label": "`输出内容类型`",`

```json
                        "name": "type",
                        "necessary": true,
                        "type": "STRING"
                      },
                      {
                        "children": [
                          {
```

`"example": "`你好！有什么我能帮助你的吗？`",` `"label": "`输出文本`",`

```json
                            "name": "value",
                            "necessary": true,
                            "type": "STRING"
                          }
```

`],`

```json
                        "example": "{}",
```

`"label": "type=text` 场景的输出结构`",`

```json
                        "name": "text",
                        "necessary": true,
                        "type": "OBJECT"
                      },
                      {
                        "children": [
                          {
                            "example": "",
```

`"label": "`输出图片的地址`",`

```json
                            "name": "url",
                            "necessary": true,
                            "type": "STRING"
                          }
```

`],`

```json
                        "example": "{}",
```

`"label": "type=image` 场景的输出结构`",`

```json
                        "name": "image",
                        "necessary": true,
                        "type": "OBJECT"
```

智能体工厂 OpenTrek 发指南

```
                      }
```

`],`

```json
                    "example": "",
```

`"label": "`输出内容`",`

```json
                    "name": "content",
                    "necessary": true,
                    "type": "LIST<Object>"
                  }
```

`],`

```json
                "example": "{}",
```

`"label": "`非流式-输出文本响应`",`

```json
                "name": "message",
                "necessary": false,
                "type": "OBJECT"
              },
              {
                "children": [
                  {
                    "example": "assistant",
                    "label": "角色",
                    "name": "role",
                    "necessary": true,
                    "type": "STRING"
                  },
                  {
                    "children": [
                      {
                        "example": "",
```

`"label": "`输出文本`",`

```json
                        "name": "data",
                        "necessary": true,
                        "type": "STRING"
                      },
                      {
                        "example": "text",
```

`"label": "`输出内容类型,目前是常量 `text",`

```json
                        "name": "type",
                        "necessary": true,
                        "type": "STRING"
                      }
```

`],`

```json
                    "example": "",
```

`"label": "`输出内容`",`

```json
                    "name": "content",
                    "necessary": true,
                    "type": "OBJECT"
                  }
```

`],`

```json
                "example": "{}",
```

`"label": "`非流式-输出思考响应`",`

```json
                "name": "thoughts",
                "necessary": false,
                "type": "OBJECT"
              }
```

智能体工厂 OpenTrek 发指南 `],`

```json
            "example": "{}",
```

`"label": "`非流式-业务响应`",`

```json
            "name": "data",
            "necessary": false,
            "type": "OBJECT"
          },
          {
            "example": "true",
```

`"label": "`非流式-业务错误码`",`

```json
            "name": "errorCode",
            "necessary": false,
            "type": "BOOL"
          },
          {
            "example": "true",
```

`"label": "`非流式-业务错误描述`",`

```json
            "name": "errorMsg",
            "necessary": false,
            "type": "BOOL"
          }
```

]

```json
      },
      "type": "platform"
    },
    "config": null,
    "feature": {
      "templateType": "AutoBot"
    },
    "operateControl": null
  },
  "errorCode": null,
  "errorMsg": null,
  "extraData": null,
  "traceId": null,
  "env": null,
  "other": null,
  "firstErrorMessage": null,
  "failure": false
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
|---|---|---|
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 创建工具

###### 创建工具

**接口概述**

###### 创建工具

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/agent/openapi/tool/create 智能体工厂 OpenTrek 发指南 POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostAgentOpenapiToolCreate

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| name | Strin g | Body | 是 | 测试工具 | 工具名称，该参数必填 |
| desc | Strin g | Body | 是 | 测试工具 | 工具描述，该参数必填 |
| serviceCon fig | Json | Body | 是 | {} | 工具配置，该参数必填 |
| toolType | Strin g | Body | 是 | api | 工具类型，该参数必填 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | Object | 返回数据 | {} |
| code | String | 工具编码 | a9c81580-8e93-42e1- b331-5cc6506c0093 |
| name | String | 工具名称 | 测试工具 |

智能体工厂 OpenTrek 发指南

| desc | String | 工具描述 | 测试工具 |
|---|---|---|---|
| version | String | 工具版本 | 1759118429269 |
| serviceConfig | Object | 工具配置 | {} |
| workspaceCode | String | 所属工作空间编码 | baseline |
| gmtCreate | String | 创建时间 | 2025-08- 29T11:43:54.722+00: 00 |
| gmtModified | String | 修改时间 | 2025-08- 29T11:43:54.722+00: 00 |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式智能体工厂 OpenTrek 发指南

```json
{
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
    },
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
    },
    "shareWorkspaces": null,
    "allFlag": null
  },
  "errorCode": null,
  "errorMsg": null,
  "extraData": null,
  "traceId": null,
  "env": null,
  "other": null,
  "firstErrorMessage": null,
  "failure": false
}
```

**文档补充说明**

智能体工厂 OpenTrek 发指南

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 查询工具详情

智能体工厂 OpenTrek 发指南

**接口概述**

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/agent/openapi/tool/getOne POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostAgentOpenapiToolGetone

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| uniqueCod e | Strin g | Body | 是 | a9c81580-8e93-42e1- b331-5cc6506c0093 | 工具编码，该参数必填 |
| version | Strin g | Body | 是 | 1759118429269 | 工具版本，该参数必填 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | Object | 返回数据 | {} |
| code | String | 工具编码 | a9c81580-8e93-42e1- b331-5cc6506c0093 |

智能体工厂 OpenTrek 发指南

| name | String | 工具名称 | 测试工具 |
|---|---|---|---|
| desc | String | 工具描述 | 测试工具 |
| version | String | 工具版本 | 1759118429269 |
| serviceConfig | Object | 工具配置 | {} |
| workspaceCode | String | 所属工作空间编码 | baseline |
| gmtCreate | String | 创建时间 | 2025-08- 29T11:43:54.722+00: 00 |
| gmtModified | String | 修改时间 | 2025-08- 29T11:43:54.722+00: 00 |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式

```json
{
  "errorMessages": [],
  "success": true,
  "data": {
    "id": 141,
    "gmtCreate": "2025-09-18T02:35:40.599+00:00",
    "gmtModified": "2025-09-18T02:35:40.599+00:00",
    "tenant": "fmthktsjdb",
    "code": "3c31d315-43a1-47f7-81ab-12b0d75fd2ab",
    "workspaceCode": "fmthktsjdb",
```

`"name": "fangyu`测试-百度`",`

```json
    "version": "1757382560369",
    "desc": "fangyu测试",
    "toolType": "api",
    "toolSubType": null,
    "owner": {
      "id": null,
      "gmtCreate": null,
      "gmtModified": null,
      "tenant": null,
      "uniqueCode": "33ad2daf266d454a9cd1a9469a75c53d",
```

智能体工厂 OpenTrek 发指南

```json
      "source": null,
      "outerId": null,
      "name": "test"
    },
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
          {
            "fieldCode": "Content-Type",
            "fieldType": "CONSTANT",
            "fieldValue": "application/json",
            "fieldDesc": "",
            "flowEditable": false,
            "encrypt": false
          }
```

`],`

```json
        "requestToolApiFieldList": [
          {
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
          }
```

`],`

```json
        "responseToolApiFieldList": [
          {
            "fieldCode": "b",
            "fieldType": "STRING",
            "parentFieldCode": null,
            "required": false,
            "leaf": null,
            "flowEditable": true,
            "fieldDemo": null,
            "fieldDesc": "",
            "extend": null,
```

智能体工厂 OpenTrek 发指南

```json
            "refType": null,
            "refValue": "",
            "propertyValue": null,
            "children": null
          }
```

`],`

```json
        "asyncExecutorFlag": false,
        "mockResponse": null,
        "preHandle": null,
        "reasoningModel": null,
        "promptTemplate": null,
        "preHandlerScript": null,
        "httpMethod": "GET",
        "responseParserName": null,
        "returnByStream": false,
        "toolApiMetaConfigDTO": null,
        "browserExecution": null
      },
      "toolScriptConfig": null,
      "searchChunkConfig": null,
      "toolUseDetail": null,
      "mcpConfig": null
    },
    "shareWorkspaces": null,
    "allFlag": null
  },
  "errorCode": null,
  "errorMsg": null,
  "extraData": null,
  "traceId": null,
  "env": null,
  "other": null,
  "firstErrorMessage": null,
  "failure": false
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
|---|---|---|
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 删除工具

###### 删除工具

**接口概述**

###### 删除工具

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/agent/openapi/tool/delete POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostAgentOpenapiToolDelete

**请求头**

智能体工厂 OpenTrek 发指南

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| uniqueCod e | Strin g | Body | 是 | a9c81580-8e93-42e1- b331-5cc6506c0093 | 工具编码，该参数必填 |
| version | Strin g | Body | 是 | 1759118429269 | 工具版本，该参数必填 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式智能体工厂 OpenTrek 发指南

```json
{
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
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |

智能体工厂 OpenTrek 发指南

| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
|---|---|---|
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### Skill Hub

###### 查询Skill列表

分页查询空间Skill列表。

**接口概述**

分页查询空间Skill列表。 分页查询空间Skill列表。可以通过查看请求示例，点击 curl 命令示例右侧的调试按钮验证业务接口调用效果。

```
接口调用地址: POST http://IP:port/gatectl/agent/api/skill/queryPage
```

**请求头**

| 参数名称 | 类型 | 是否必选 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| x-sfm- workspacecode | String | 是 | 目标工作空间 | your workspace _ _ code |
| Content-Type | String | 是 | Content-Type | application/json |

**请求参数**

| 参数名称 | 类型 | 是否必选 | 描述 | 示例 |
|---|---|---|---|---|
| current | Integer | 是 | 当前页数。 | 1 |

智能体工厂 OpenTrek 发指南

| pageSize | Integer | 是 | 每页条数。 | 10 |
|---|---|---|---|---|
| skillCategory | String | 否 | Skill分类： workspace：空间级 platform：平台级 share：共享 | workspace |
| skillType | String | 否 | Skill类型，FILE/TOOL/WORKFLOW。 | FILE |
| keyword | String | 否 | 搜索关键词，匹配名称或别名。 |  |
| skillCode | String | 否 | Skill唯一标识。 |  |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功。 | true |
| data | Object | 返回数据。 | {} |
| data.total | Integer | 查询到的Skill总数。 | 1 |
| data.list | List | 查询到的Skill列表。 |  |
| data.list.skillCode | String | Skill唯一标识。 | sk-abc123 |
| data.list.name | String | Skill名称。 | 数据分析Skill |
| data.list.skillAlias | String | Skill别名。 | data-analysis |
| data.list.skillType | String | Skill类型。 | FILE |
| data.list.skillCategory | String | Skill分类。 | workspace |
| data.list.version | String | Skill版本。 | 1716800000000 |

智能体工厂 OpenTrek 发指南

| data.list.workspaceCo de | String | 所属工作空间编码。 | baseline |
|---|---|---|---|
| data.list.gmtCreate | String | 创建时间。 | 2025-08- 29T11:43:54.722+00: 00 |
| data.list.gmtModified | String | 修改时间。 | 2025-08- 29T11:43:54.722+00: 00 |
| data.pageSize | Integer | 每页大小。 | 10 |
| data.current | Integer | 目前所在页数。 | 1 |
| errorCode | String | 错误码。 |  |
| errorMsg | String | 错误描述。 |  |

**示例**

**curl命令示例**

```bash
curl -X 'POST' 'http://121.199.171.27:30226/gatectl/agent/api/skill/queryPage' \ -H 'Content-Type: application/json' \ -H 'x-sfm-workspacecode: xxx' \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -d '{"current": 1,"pageSize": 10,"skillCategory": "workspace","skillType": "FILE"}'
```

**返回数据**

智能体工厂 OpenTrek 发指南

```json
{"errorMessages":[],"success":true,"data":{"extInfos":{},"total":1,"list":[{"id":105,"s killCode":"c32e0b39-dfbe-45d7-89b2- 23226465a12a","skillVersion":"1780888817410","skillAlias":"asdf","name":"amap","descripti
```

`":"`使用高德地图`Web`服务`API`进行地点搜索、天气查询和路线规划。

```
","skillType":"FILE","zipUrl":null,"skillRefs":null,"skillMd":"---\nname:
```

amap\ndescription: 使用高德地图`Web`服务`API`进行地点搜索、天气查询和路线规划。\nhomepage:

```
https://lbs.amap.com/\nmetadata: {\"clawdbot\": {\"emoji\":\"\uD83D\uDDFA️\",\"requires\":{\"bins\":
```

[\"curl\"]},\"primaryEnv\":\"AMAP_KEY\"}}\n---\n\n# 高德地图 (Amap)\n\n本技能使用高德地图 `Web` 服务 `API` 提供丰富的地理位置服务。\n\n**重要：`**` 使用本技能前，你必须在高德开放平台申请一个 `Web` 服务 `API Key`，并将其设置为环境变量 `AMAP_KEY`。\n\n```bash\nexport AMAP_KEY=\"你的`Web`服务`API` Key\"\n```\n\nClawdbot 会自动读取这个环境变量来调用 `API`。\n\n## 何时使用 (触发条件)\n\n当用户提出以下类型的请求时，应优先使用本技能：\n- \"帮我查一下[城市]的天气\"\n- \"搜索[地点]附近的[东西]\"\n
  - \"查找[关键词]的位置\"\n- \"从`[A]`到`[B]`怎么走？\"\n- \"查询[地址]的经纬度\"\n- \"这个坐标[经度,
纬度]是哪里？\"\n\n## 核心功能与用法\n\n### 1. 天气查询\n\n用于查询指定城市的实时天气或天气预报。\n \n**注意：`** API` 需要城市的 `adcode`。如果不知道 `adcode`，可以先通过 `**`行政区划查询`**` 功能获取。\n \n#### 查询实时天气\n```bash\n# 将 [城市`adcode]` 替换为实际的行政区编码, 例如北京是 110000\ncurl

```
\"https://restapi.amap.com/v3/weather/weatherInfo?key=$AMAP_KEY&city=[城市adcode]&extens
```

ions=base\"\n```\n\n#### 查询天气预报\n```bash\n# 将 [城市`adcode]` 替换为实际的行政区编码\ncurl

```
\"https://restapi.amap.com/v3/weather/weatherInfo?key=$AMAP_KEY&city=[城市adcode]&extens
```

ions=all\"\n```\n\n### 2. 地点搜索 (POI)\n\n用于根据关键字在指定城市搜索地点信息。\n\n```bash\n
# 将 [关键词] 和 [城市] 替换为用户提供的内容\ncurl \"https://restapi.amap.com/v3/place/text?k
ey=$AMAP_KEY&keywords=[关键词`]&city=[`城市]\"\n```\n\n### 3. 驾车路径规划\n\n用于规划两个地点之间的驾车路线。\n\n**注意：`** API` 需要起终点的经纬度坐标。如果用户提供的是地址，需要先通过 `**`地理编码*
* 功能将地址转换为坐标。\n\n```bash\n# 将 [起点经纬度] 和 [终点经纬度] 替换为实际坐标，格式为 \"经

```
度,纬度\"\ncurl \"https://restapi.amap.com/v3/direction/driving?key=$AMAP_KEY&origin=[起
```

点经纬度`]&destination=[`终点经纬度]\"\n```\n\n### 4. 地理编码 (地址 → 坐标)\n\n将结构化的地址信息转换为经纬度坐标。\n\n```bash\n# 将 [地址] 替换为用户提供的地址\ncurl

```
\"https://restapi.amap.com/v3/geocode/geo?key=$AMAP_KEY&address=[地址]\"\n```\n\n### 5.
```

逆地理编码 (坐标 → 地址)\n\n将经纬度坐标转换为结构化的地址信息。\n\n```bash\n# 将 [经纬度] 替换为实

```
际坐标，格式为 \"经度,纬度\"\ncurl \"https://restapi.amap.com/v3/geocode/regeo?key=$AMAP_KE
```

`Y&location=[`经纬度]\"\n```\n\n### 6. 行政区划查询 (获取 adcode)\n\n用于查询省、市、区、街道的行政区划信息，包括 `adcode` 和边界。\n\n```bash\n# 将 [关键词] 替换为城市或区域名称，例如 \"北京市\"

```
\ncurl \"https://restapi.amap.com/v3/config/district?key=$AMAP_KEY&keywords=[关键词]&sub district=0\"\n```\n","scanReport":{"filePath":"agent/skill-files/8efb8fba-bb3b-4631-ae9 5-d89000ca0a8d/amap.zip","securityStatus":true,"insecurityReasons": []},"status":"PUBLISHED","masterFlag":true,"labels":null,"feature":{"exampleQuestions":
```

`["`如何查询商务出差目的地的实时天气？`","`怎样快速搜索公司周边的商务接待餐厅？`","`如何规划办公地到供应商工

```json
厂的最优路线？"]},"shareWorkspaces":["84e47d28-0570-4469-b729de76d89362f0"],"workspaceCode":"7a92789c-3882-43f5-be70- 87c84b7fbede","tenant":"baseline","gmtCreate":"2026-06- 08T03:20:17.410+00:00","gmtModified":"2026-06-08T03:20:17.410+00:00","creator":{"id":nu ll,"gmtCreate":null,"gmtModified":null,"tenant":null,"uniqueCode":"7551a976815b413bb85907 9b0677d7","source":null,"outerId":null,"name":"opentrek"},"modifier": {"id":null,"gmtCreate":null,"gmtModified":null,"tenant":null,"uniqueCode":"4e01afc2494d40 aff9145504a36a14","source":null,"outerId":null,"name":"长堤"},"skillCategory":"workspace","installStatus":null,"exampleQuestions":["如何查询商务出
```

差目的地的实时天气？`","`怎样快速搜索公司周边的商务接待餐厅？`","`如何规划办公地到供应商工厂的最优路线？`"],`

```json
"newVersionFlag":null}],"pageSize":10,"current":1,"totalPages":1},"errorCode":null,"error g":null,"extraData":null,"traceId":null,"env":null,"other":null,"errorMessage":null,"firs rrorMessage":null,"failure":false}
```

**错误码**

智能体工厂 OpenTrek 发指南

| HttpCode | 错误码 | 描述 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失。 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败，无效 APP KEY。 _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败，APP KEY 已过期。 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色不匹配. |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色已过期。 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径。 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册。 |
| 429 | GATEWAY LIMIT ! | 服务触发限流，请稍后再试。 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流，请稍后再试。 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失。 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配。 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败，不支持的鉴权方式。 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败，AK用户信息不匹配。 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败，用户角色不匹配。 |

###### 查询Skill详情

根据skillCode查询单个Skill的详细信息。 智能体工厂 OpenTrek 发指南

**接口概述**

根据skillCode查询单个Skill的详细信息。 根据skillCode查询单个Skill的详细信息。可以通过查看请求示例，点击 curl 命令示例右侧的调试按钮验证业务接口调用效果。

```
接口调用地址: POST http://IP:port/gatectl/agent/api/skill/getOne
```

**请求头**

| 参数名称 | 类型 | 是否必选 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| x-sfm- workspacecode | String | 是 | 目标工作空间 | your workspace _ _ code |
| Content-Type | String | 是 | Content-Type | application/json |

**请求参数**

| 参数名称 | 类型 | 是否必选 | 描述 | 示例 |
|---|---|---|---|---|
| skillCode | String | 是 | Skill唯一标识。 | bf1d378c-531d- 4927-be3f- 043440a4998b |
| skillVersion | String | 否 | Skill版本号，不传则查询最新版本。 | 1779441957363 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功。 | true |
| data | Object | Skill详情数据。 | {} |
| errorCode | String | 错误码。 |  |
| errorMsg | String | 错误描述。 |  |

**示例**

智能体工厂 OpenTrek 发指南

**curl命令示例**

```bash
curl -X 'POST' 'http://IP:port/gatectl/agent/api/skill/getOne' \ -H 'Content-Type: application/json' \ -H 'x-sfm-workspacecode: xxx' \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -d '{"skillCode": "sk-abc123"}'
```

**返回数据**

智能体工厂 OpenTrek 发指南

```json
{"errorMessages":[],"success":true,"data":{"id":105,"skillCode":"c32e0b39-dfbe-45d7-89b
```

`2-`

```
23226465a12a","skillVersion":"1780888817410","skillAlias":"asdf","name":"amap","descripti
```

`":"`使用高德地图`Web`服务`API`进行地点搜索、天气查询和路线规划。

```
","skillType":"FILE","zipUrl":"http://sfm-lite-0518.oss-cnhangzhou.aliyuncs.com/agent/skill-files/8efb8fba-bb3b-4631-ae95-d89000ca0a8d/amap.zip?E xpires=1784502958&OSSAccessKeyId=LTAI********************&Signature=wOgYbK1TpBsKTDKzk8AHh 2Wh0%3D","skillRefs":null,"skillMd":"---\nname: amap\ndescription: 使用高德地图Web服务API
```

进行地点搜索、天气查询和路线规划。\nhomepage: https://lbs.amap.com/\nmetadata: {\"clawdbot\":

```
{\"emoji\":\"\uD83D\uDDFA️\",\"requires\":{\"bins\":
```

[\"curl\"]},\"primaryEnv\":\"AMAP_KEY\"}}\n---\n\n# 高德地图 (Amap)\n\n本技能使用高德地图 `Web` 服务 `API` 提供丰富的地理位置服务。\n\n**重要：`**` 使用本技能前，你必须在高德开放平台申请一个 `Web` 服务 `API Key`，并将其设置为环境变量 `AMAP_KEY`。\n\n```bash\nexport AMAP_KEY=\"你的`Web`服务`API` Key\"\n```\n\nClawdbot 会自动读取这个环境变量来调用 `API`。\n\n## 何时使用 (触发条件)\n\n当用户提出以下类型的请求时，应优先使用本技能：\n- \"帮我查一下[城市]的天气\"\n- \"搜索[地点]附近的[东西]\"\n
  - \"查找[关键词]的位置\"\n- \"从`[A]`到`[B]`怎么走？\"\n- \"查询[地址]的经纬度\"\n- \"这个坐标[经度,
纬度]是哪里？\"\n\n## 核心功能与用法\n\n### 1. 天气查询\n\n用于查询指定城市的实时天气或天气预报。\n \n**注意：`** API` 需要城市的 `adcode`。如果不知道 `adcode`，可以先通过 `**`行政区划查询`**` 功能获取。\n \n#### 查询实时天气\n```bash\n# 将 [城市`adcode]` 替换为实际的行政区编码, 例如北京是 110000\ncurl

```
\"https://restapi.amap.com/v3/weather/weatherInfo?key=$AMAP_KEY&city=[城市adcode]&extens
```

ions=base\"\n```\n\n#### 查询天气预报\n```bash\n# 将 [城市`adcode]` 替换为实际的行政区编码\ncurl

```
\"https://restapi.amap.com/v3/weather/weatherInfo?key=$AMAP_KEY&city=[城市adcode]&extens
```

ions=all\"\n```\n\n### 2. 地点搜索 (POI)\n\n用于根据关键字在指定城市搜索地点信息。\n\n```bash\n
# 将 [关键词] 和 [城市] 替换为用户提供的内容\ncurl \"https://restapi.amap.com/v3/place/text?k
ey=$AMAP_KEY&keywords=[关键词`]&city=[`城市]\"\n```\n\n### 3. 驾车路径规划\n\n用于规划两个地点之间的驾车路线。\n\n**注意：`** API` 需要起终点的经纬度坐标。如果用户提供的是地址，需要先通过 `**`地理编码*
* 功能将地址转换为坐标。\n\n```bash\n# 将 [起点经纬度] 和 [终点经纬度] 替换为实际坐标，格式为 \"经

```
度,纬度\"\ncurl \"https://restapi.amap.com/v3/direction/driving?key=$AMAP_KEY&origin=[起
```

点经纬度`]&destination=[`终点经纬度]\"\n```\n\n### 4. 地理编码 (地址 → 坐标)\n\n将结构化的地址信息转换为经纬度坐标。\n\n```bash\n# 将 [地址] 替换为用户提供的地址\ncurl

```
\"https://restapi.amap.com/v3/geocode/geo?key=$AMAP_KEY&address=[地址]\"\n```\n\n### 5.
```

逆地理编码 (坐标 → 地址)\n\n将经纬度坐标转换为结构化的地址信息。\n\n```bash\n# 将 [经纬度] 替换为实

```
际坐标，格式为 \"经度,纬度\"\ncurl \"https://restapi.amap.com/v3/geocode/regeo?key=$AMAP_KE
```

`Y&location=[`经纬度]\"\n```\n\n### 6. 行政区划查询 (获取 adcode)\n\n用于查询省、市、区、街道的行政区划信息，包括 `adcode` 和边界。\n\n```bash\n# 将 [关键词] 替换为城市或区域名称，例如 \"北京市\"

```
\ncurl \"https://restapi.amap.com/v3/config/district?key=$AMAP_KEY&keywords=[关键词]&sub district=0\"\n```\n","scanReport":{"filePath":"agent/skill-files/8efb8fba-bb3b-4631-ae9 5-d89000ca0a8d/amap.zip","securityStatus":true,"insecurityReasons": []},"status":"PUBLISHED","masterFlag":true,"labels":null,"feature":{"exampleQuestions":
```

`["`如何查询商务出差目的地的实时天气？`","`怎样快速搜索公司周边的商务接待餐厅？`","`如何规划办公地到供应商工

```json
厂的最优路线？"]},"shareWorkspaces":["84e47d28-0570-4469-b729de76d89362f0"],"workspaceCode":"7a92789c-3882-43f5-be70- 87c84b7fbede","tenant":"baseline","gmtCreate":"2026-06- 08T03:20:17.410+00:00","gmtModified":"2026-06-08T03:20:17.410+00:00","creator":{"id":nu ll,"gmtCreate":null,"gmtModified":null,"tenant":null,"uniqueCode":"7551a976815b413bb85907 9b0677d7","source":null,"outerId":null,"name":"opentrek"},"modifier": {"id":null,"gmtCreate":null,"gmtModified":null,"tenant":null,"uniqueCode":"4e01afc2494d40 aff9145504a36a14","source":null,"outerId":null,"name":"长堤"},"skillCategory":"workspace","installStatus":null,"exampleQuestions":null,"newVersion ag":null},"errorCode":null,"errorMsg":null,"extraData":null,"traceId":null,"env":null,"ot r":null,"errorMessage":null,"firstErrorMessage":null,"failure":false}
```

**错误码**

智能体工厂 OpenTrek 发指南

| HttpCode | 错误码 | 描述 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失。 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败，无效 APP KEY。 _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败，APP KEY 已过期。 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色不匹配。 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色已过期。 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径。 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册。 |
| 429 | GATEWAY LIMIT ! | 服务触发限流，请稍后再试。 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流，请稍后再试。 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失。 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配。 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败，不支持的鉴权方式。 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败，AK用户信息不匹配。 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败，用户角色不匹配。 |

###### 查询Skill版本列表

查询指定Skill的所有版本列表。 智能体工厂 OpenTrek 发指南

**接口概述**

查询指定Skill的所有版本列表。 查询指定Skill的所有版本列表。可以通过查看请求示例，点击 curl 命令示例右侧的调试按钮验证业务接口调用效果。

```
接口调用地址: POST http://IP:port/gatectl/agent/api/skill/listVersions
```

**请求头**

| 参数名称 | 类型 | 是否必选 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| x-sfm- workspacecode | String | 是 | 目标工作空间 | your workspace _ _ code |
| Content-Type | String | 是 | Content-Type | application/json |

**请求参数**

| 参数名称 | 类型 | 是否必选 | 描述 | 示例 |
|---|---|---|---|---|
| skillCode | String | 是 | Skill唯一标识。 | c32e0b39-dfbe- 45d7-89b2- 23226465a12a |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功。 | true |
| data | List | Skill版本列表。 | [] |
| errorCode | String | 错误码。 | 400 |
| errorMsg | String | 错误描述。 | 错误 |

**示例**

**curl命令示例**

智能体工厂 OpenTrek 发指南

```bash
curl -X 'POST' 'http://IP:port/gatectl/agent/api/skill/listVersions' \ -H 'Content-Type: application/json' \ -H 'x-sfm-workspacecode: xxx' \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -d '{"skillCode": "sk-abc123"}'
```

**返回数据**

```json
{"errorMessages":[],"success":true,"data":[{"id":105,"skillCode":"c32e0b39-dfbe-45d7-89 b2- 23226465a12a","skillVersion":"1780888817410","skillAlias":"asdf","name":"amap","descripti
```

`":"`使用高德地图`Web`服务`API`进行地点搜索、天气查询和路线规划。

```
","skillType":"FILE","zipUrl":null,"skillRefs":null,"skillMd":"---\nname:
```

amap\ndescription: 使用高德地图`Web`服务`API`进行地点搜索、天气查询和路线规划。\nhomepage:

```
https://lbs.amap.com/\nmetadata: {\"clawdbot\": {\"emoji\":\"\uD83D\uDDFA️\",\"requires\":{\"bins\":
```

[\"curl\"]},\"primaryEnv\":\"AMAP_KEY\"}}\n---\n\n# 高德地图 (Amap)\n\n本技能使用高德地图 `Web` 服务 `API` 提供丰富的地理位置服务。\n\n**重要：`**` 使用本技能前，你必须在高德开放平台申请一个 `Web` 服务 `API Key`，并将其设置为环境变量 `AMAP_KEY`。\n\n```bash\nexport AMAP_KEY=\"你的`Web`服务`API` Key\"\n```\n\nClawdbot 会自动读取这个环境变量来调用 `API`。\n\n## 何时使用 (触发条件)\n\n当用户提出以下类型的请求时，应优先使用本技能：\n- \"帮我查一下[城市]的天气\"\n- \"搜索[地点]附近的[东西]\"\n
  - \"查找[关键词]的位置\"\n- \"从`[A]`到`[B]`怎么走？\"\n- \"查询[地址]的经纬度\"\n- \"这个坐标[经度,
纬度]是哪里？\"\n\n## 核心功能与用法\n\n### 1. 天气查询\n\n用于查询指定城市的实时天气或天气预报。\n \n**注意：`** API` 需要城市的 `adcode`。如果不知道 `adcode`，可以先通过 `**`行政区划查询`**` 功能获取。\n \n#### 查询实时天气\n```bash\n# 将 [城市`adcode]` 替换为实际的行政区编码, 例如北京是 110000\ncurl

```
\"https://restapi.amap.com/v3/weather/weatherInfo?key=$AMAP_KEY&city=[城市adcode]&extens
```

ions=base\"\n```\n\n#### 查询天气预报\n```bash\n# 将 [城市`adcode]` 替换为实际的行政区编码\ncurl

```
\"https://restapi.amap.com/v3/weather/weatherInfo?key=$AMAP_KEY&city=[城市adcode]&extens
```

ions=all\"\n```\n\n### 2. 地点搜索 (POI)\n\n用于根据关键字在指定城市搜索地点信息。\n\n```bash\n
# 将 [关键词] 和 [城市] 替换为用户提供的内容\ncurl \"https://restapi.amap.com/v3/place/text?k
ey=$AMAP_KEY&keywords=[关键词`]&city=[`城市]\"\n```\n\n### 3. 驾车路径规划\n\n用于规划两个地点之间的驾车路线。\n\n**注意：`** API` 需要起终点的经纬度坐标。如果用户提供的是地址，需要先通过 `**`地理编码*
* 功能将地址转换为坐标。\n\n```bash\n# 将 [起点经纬度] 和 [终点经纬度] 替换为实际坐标，格式为 \"经

```
度,纬度\"\ncurl \"https://restapi.amap.com/v3/direction/driving?key=$AMAP_KEY&origin=[起
```

点经纬度`]&destination=[`终点经纬度]\"\n```\n\n### 4. 地理编码 (地址 → 坐标)\n\n将结构化的地址信息转换为经纬度坐标。\n\n```bash\n# 将 [地址] 替换为用户提供的地址\ncurl

```
\"https://restapi.amap.com/v3/geocode/geo?key=$AMAP_KEY&address=[地址]\"\n```\n\n### 5.
```

逆地理编码 (坐标 → 地址)\n\n将经纬度坐标转换为结构化的地址信息。\n\n```bash\n# 将 [经纬度] 替换为实

```
际坐标，格式为 \"经度,纬度\"\ncurl \"https://restapi.amap.com/v3/geocode/regeo?key=$AMAP_KE
```

`Y&location=[`经纬度]\"\n```\n\n### 6. 行政区划查询 (获取 adcode)\n\n用于查询省、市、区、街道的行政区划信息，包括 `adcode` 和边界。\n\n```bash\n# 将 [关键词] 替换为城市或区域名称，例如 \"北京市\"

```
\ncurl \"https://restapi.amap.com/v3/config/district?key=$AMAP_KEY&keywords=[关键词]&sub district=0\"\n```\n","scanReport":{"filePath":"agent/skill-files/8efb8fba-bb3b-4631-ae9 5-d89000ca0a8d/amap.zip","securityStatus":true,"insecurityReasons": []},"status":"PUBLISHED","masterFlag":true,"labels":null,"feature":{"exampleQuestions":
```

`["`如何查询商务出差目的地的实时天气？`","`怎样快速搜索公司周边的商务接待餐厅？`","`如何规划办公地到供应商工

```json
厂的最优路线？"]},"shareWorkspaces":["84e47d28-0570-4469-b729de76d89362f0"],"workspaceCode":"7a92789c-3882-43f5-be70- 87c84b7fbede","tenant":"baseline","gmtCreate":"2026-06- 08T03:20:17.410+00:00","gmtModified":"2026-06-08T03:20:17.410+00:00","creator":{"id":nu ll,"gmtCreate":null,"gmtModified":null,"tenant":null,"uniqueCode":"7551a976815b413bb85907 9b0677d7","source":null,"outerId":null,"name":"opentrek"},"modifier": {"id":null,"gmtCreate":null,"gmtModified":null,"tenant":null,"uniqueCode":"4e01afc2494d40 aff9145504a36a14""source":null"outerId":null"name":"长
```

智能体工厂 OpenTrek 发指南

```
aff9145504a36a14,source:null,outerId:null,name:长堤"},"skillCategory":"workspace","installStatus":null,"exampleQuestions":null,"newVersion ag":null},{"id":93,"skillCode":"c32e0b39-dfbe-45d7-89b2- 23226465a12a","skillVersion":"1780556028331","skillAlias":"asdf","name":"amap","descripti
```

`":"`使用高德地图`Web`服务`API`进行地点搜索、天气查询和路线规划。

```
","skillType":"FILE","zipUrl":null,"skillRefs":null,"skillMd":"---\nname:
```

amap\ndescription: 使用高德地图`Web`服务`API`进行地点搜索、天气查询和路线规划。\nhomepage:

```
https://lbs.amap.com/\nmetadata: {\"clawdbot\": {\"emoji\":\"\uD83D\uDDFA️\",\"requires\":{\"bins\":
```

[\"curl\"]},\"primaryEnv\":\"AMAP_KEY\"}}\n---\n\n# 高德地图 (Amap)\n\n本技能使用高德地图 `Web` 服务 `API` 提供丰富的地理位置服务。\n\n**重要：`**` 使用本技能前，你必须在高德开放平台申请一个 `Web` 服务 `API Key`，并将其设置为环境变量 `AMAP_KEY`。\n\n```bash\nexport AMAP_KEY=\"你的`Web`服务`API` Key\"\n```\n\nClawdbot 会自动读取这个环境变量来调用 `API`。\n\n## 何时使用 (触发条件)\n\n当用户提出以下类型的请求时，应优先使用本技能：\n- \"帮我查一下[城市]的天气\"\n- \"搜索[地点]附近的[东西]\"\n
  - \"查找[关键词]的位置\"\n- \"从`[A]`到`[B]`怎么走？\"\n- \"查询[地址]的经纬度\"\n- \"这个坐标[经度,
纬度]是哪里？\"\n\n## 核心功能与用法\n\n### 1. 天气查询\n\n用于查询指定城市的实时天气或天气预报。\n \n**注意：`** API` 需要城市的 `adcode`。如果不知道 `adcode`，可以先通过 `**`行政区划查询`**` 功能获取。\n \n#### 查询实时天气\n```bash\n# 将 [城市`adcode]` 替换为实际的行政区编码, 例如北京是 110000\ncurl

```
\"https://restapi.amap.com/v3/weather/weatherInfo?key=$AMAP_KEY&city=[城市adcode]&extens
```

ions=base\"\n```\n\n#### 查询天气预报\n```bash\n# 将 [城市`adcode]` 替换为实际的行政区编码\ncurl

```
\"https://restapi.amap.com/v3/weather/weatherInfo?key=$AMAP_KEY&city=[城市adcode]&extens
```

ions=all\"\n```\n\n### 2. 地点搜索 (POI)\n\n用于根据关键字在指定城市搜索地点信息。\n\n```bash\n
# 将 [关键词] 和 [城市] 替换为用户提供的内容\ncurl \"https://restapi.amap.com/v3/place/text?k
ey=$AMAP_KEY&keywords=[关键词`]&city=[`城市]\"\n```\n\n### 3. 驾车路径规划\n\n用于规划两个地点之间的驾车路线。\n\n**注意：`** API` 需要起终点的经纬度坐标。如果用户提供的是地址，需要先通过 `**`地理编码*
* 功能将地址转换为坐标。\n\n```bash\n# 将 [起点经纬度] 和 [终点经纬度] 替换为实际坐标，格式为 \"经

```
度,纬度\"\ncurl \"https://restapi.amap.com/v3/direction/driving?key=$AMAP_KEY&origin=[起
```

点经纬度`]&destination=[`终点经纬度]\"\n```\n\n### 4. 地理编码 (地址 → 坐标)\n\n将结构化的地址信息转换为经纬度坐标。\n\n```bash\n# 将 [地址] 替换为用户提供的地址\ncurl

```
\"https://restapi.amap.com/v3/geocode/geo?key=$AMAP_KEY&address=[地址]\"\n```\n\n### 5.
```

逆地理编码 (坐标 → 地址)\n\n将经纬度坐标转换为结构化的地址信息。\n\n```bash\n# 将 [经纬度] 替换为实

```
际坐标，格式为 \"经度,纬度\"\ncurl \"https://restapi.amap.com/v3/geocode/regeo?key=$AMAP_KE
```

`Y&location=[`经纬度]\"\n```\n\n### 6. 行政区划查询 (获取 adcode)\n\n用于查询省、市、区、街道的行政区划信息，包括 `adcode` 和边界。\n\n```bash\n# 将 [关键词] 替换为城市或区域名称，例如 \"北京市\"

```
\ncurl \"https://restapi.amap.com/v3/config/district?key=$AMAP_KEY&keywords=[关键词]&sub district=0\"\n```\n","scanReport":{"filePath":"agent/skill-files/42e8ed34-6580-4217-ab4 1-ddf8428f06a1/amap.zip","securityStatus":true,"insecurityReasons": []},"status":"PUBLISHED","masterFlag":false,"labels":null,"feature":
```

`{"exampleQuestions":["`如何查询商务出差目的地的实时天气？`","`怎样快速搜索公司周边的商务接待餐厅？`","` 如何规划办公地到供应商工厂的最优路线？`"],"agentRelations":[]},"shareWorkspaces":["84e47d28-05`

```json
70-4469-b729-de76d89362f0"],"workspaceCode":"7a92789c-3882-43f5-be70- 87c84b7fbede","tenant":"baseline","gmtCreate":"2026-06- 04T06:53:48.331+00:00","gmtModified":"2026-06-08T03:20:17.408+00:00","creator":{"id":nu ll,"gmtCreate":null,"gmtModified":null,"tenant":null,"uniqueCode":"7551a976815b413bb85907 9b0677d7","source":null,"outerId":null,"name":"opentrek"},"modifier": {"id":null,"gmtCreate":null,"gmtModified":null,"tenant":null,"uniqueCode":"4e01afc2494d40 aff9145504a36a14","source":null,"outerId":null,"name":"长堤"},"skillCategory":"workspace","installStatus":null,"exampleQuestions":null,"newVersion ag":null},{"id":92,"skillCode":"c32e0b39-dfbe-45d7-89b2- 23226465a12a","skillVersion":"1780555679274","skillAlias":"asdf","name":"amap","descripti
```

`":"`使用高德地图`Web`服务`API`进行地点搜索、天气查询和路线规划。

```
","skillType":"FILE","zipUrl":null,"skillRefs":null,"skillMd":"---\nname:
```

amap\ndescription: 使用高德地图`Web`服务`API`进行地点搜索、天气查询和路线规划。\nhomepage:

```
https://lbs.amap.com/\nmetadata: {\"clawdbot\": {\"emoji\":\"\uD83D\uDDFA️\",\"requires\":{\"bins\":
```

智能体工厂 OpenTrek 发指南

```
{\eoj\:\\u83\u \,\ equ es\:{\b s\:
```

[\"curl\"]},\"primaryEnv\":\"AMAP_KEY\"}}\n---\n\n# 高德地图 (Amap)\n\n本技能使用高德地图 `Web` 服务 `API` 提供丰富的地理位置服务。\n\n**重要：`**` 使用本技能前，你必须在高德开放平台申请一个 `Web` 服务 `API Key`，并将其设置为环境变量 `AMAP_KEY`。\n\n```bash\nexport AMAP_KEY=\"你的`Web`服务`API` Key\"\n```\n\nClawdbot 会自动读取这个环境变量来调用 `API`。\n\n## 何时使用 (触发条件)\n\n当用户提出以下类型的请求时，应优先使用本技能：\n- \"帮我查一下[城市]的天气\"\n- \"搜索[地点]附近的[东西]\"\n
  - \"查找[关键词]的位置\"\n- \"从`[A]`到`[B]`怎么走？\"\n- \"查询[地址]的经纬度\"\n- \"这个坐标[经度,
纬度]是哪里？\"\n\n## 核心功能与用法\n\n### 1. 天气查询\n\n用于查询指定城市的实时天气或天气预报。\n \n**注意：`** API` 需要城市的 `adcode`。如果不知道 `adcode`，可以先通过 `**`行政区划查询`**` 功能获取。\n \n#### 查询实时天气\n```bash\n# 将 [城市`adcode]` 替换为实际的行政区编码, 例如北京是 110000\ncurl

```
\"https://restapi.amap.com/v3/weather/weatherInfo?key=$AMAP_KEY&city=[城市adcode]&extens
```

ions=base\"\n```\n\n#### 查询天气预报\n```bash\n# 将 [城市`adcode]` 替换为实际的行政区编码\ncurl

```
\"https://restapi.amap.com/v3/weather/weatherInfo?key=$AMAP_KEY&city=[城市adcode]&extens
```

ions=all\"\n```\n\n### 2. 地点搜索 (POI)\n\n用于根据关键字在指定城市搜索地点信息。\n\n```bash\n
# 将 [关键词] 和 [城市] 替换为用户提供的内容\ncurl \"https://restapi.amap.com/v3/place/text?k
ey=$AMAP_KEY&keywords=[关键词`]&city=[`城市]\"\n```\n\n### 3. 驾车路径规划\n\n用于规划两个地点之间的驾车路线。\n\n**注意：`** API` 需要起终点的经纬度坐标。如果用户提供的是地址，需要先通过 `**`地理编码*
* 功能将地址转换为坐标。\n\n```bash\n# 将 [起点经纬度] 和 [终点经纬度] 替换为实际坐标，格式为 \"经

```
度,纬度\"\ncurl \"https://restapi.amap.com/v3/direction/driving?key=$AMAP_KEY&origin=[起
```

点经纬度`]&destination=[`终点经纬度]\"\n```\n\n### 4. 地理编码 (地址 → 坐标)\n\n将结构化的地址信息转换为经纬度坐标。\n\n```bash\n# 将 [地址] 替换为用户提供的地址\ncurl

```
\"https://restapi.amap.com/v3/geocode/geo?key=$AMAP_KEY&address=[地址]\"\n```\n\n### 5.
```

逆地理编码 (坐标 → 地址)\n\n将经纬度坐标转换为结构化的地址信息。\n\n```bash\n# 将 [经纬度] 替换为实

```
际坐标，格式为 \"经度,纬度\"\ncurl \"https://restapi.amap.com/v3/geocode/regeo?key=$AMAP_KE
```

`Y&location=[`经纬度]\"\n```\n\n### 6. 行政区划查询 (获取 adcode)\n\n用于查询省、市、区、街道的行政区划信息，包括 `adcode` 和边界。\n\n```bash\n# 将 [关键词] 替换为城市或区域名称，例如 \"北京市\"

```
\ncurl \"https://restapi.amap.com/v3/config/district?key=$AMAP_KEY&keywords=[关键词]&sub district=0\"\n```\n","scanReport":{"filePath":"agent/skill-files/70083831-e2db-46f0-919 9-ddd5b4e85d72/amap.zip","securityStatus":true,"insecurityReasons": []},"status":"PUBLISHED","masterFlag":false,"labels":null,"feature":
```

`{"exampleQuestions":["`如何查询商务出差目的地的实时天气？`","`怎样快速搜索公司周边的商务接待餐厅？`","` 如何规划办公地到供应商工厂的最优路线？`"],"agentRelations":[{"agentCode":"f53cca02-cc33-48d8-8`

```json
57f-26da7f86b6d1","agentVersion":"1780555943159"},{"agentCode":"8fa53e58-0a1f-4e63-b24f -c6e894317234","agentVersion":"1780555847293"},{"agentCode":"8fa53e58-0a1f-4e63-b24f-c6 e894317234","agentVersion":"1780555901813"}]},"shareWorkspaces":null,"workspaceCode":"7a9 89c-3882-43f5-be70-87c84b7fbede","tenant":"baseline","gmtCreate":"2026-06- 04T06:47:59.276+00:00","gmtModified":"2026-06-08T02:27:01.925+00:00","creator":{"id":nu ll,"gmtCreate":null,"gmtModified":null,"tenant":null,"uniqueCode":"7551a976815b413bb85907 9b0677d7","source":null,"outerId":null,"name":"opentrek"},"modifier": {"id":null,"gmtCreate":null,"gmtModified":null,"tenant":null,"uniqueCode":"7551a976815b41 b859074c9b0677d7","source":null,"outerId":null,"name":"opentrek"},"skillCategory":"worksp e","installStatus":null,"exampleQuestions":null,"newVersionFlag":null}],"errorCode":null, rrorMsg":null,"extraData":null,"traceId":null,"env":null,"other":null,"errorMessage":null firstErrorMessage":null,"failure":false}
```

**错误码**

| HttpCode | 错误码 | 描述 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失。 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败，无效 APP KEY。 _ |
|---|---|---|
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败，APP KEY 已过期。 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色不匹配。 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色已过期。 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径。 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册。 |
| 429 | GATEWAY LIMIT ! | 服务触发限流，请稍后再试。 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流，请稍后再试。 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失。 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配。 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败，不支持的鉴权方式。 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败，AK用户信息不匹配。 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败，用户角色不匹配。 |

###### 扫描Skill ZIP包

扫描上传的Skill ZIP包，解析包内容。

**接口概述**

扫描上传的Skill ZIP包，解析包内容。 智能体工厂 OpenTrek 发指南扫描上传的Skill ZIP包，解析包内容并返回扫描报告。可以通过查看请求示例，点击 curl 命令示例右侧的调试按钮验证业务接口调用效果。

```
接口调用地址: POST http://IP:port/gatectl/agent/api/skill/scanZip
```

**请求头**

| 参数名称 | 类型 | 是否必选 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| x-sfm- workspacecode | String | 是 | 目标工作空间 | your workspace _ _ code |
| Content-Type | String | 是 | Content-Type | application/json |

**请求参数**

| 参数名称 | 类型 | 是否必选 | 描述 | 示例 |
|---|---|---|---|---|
| zipUrl | String | 是 | ZIP文件可访问的 URL。 | /path/to/skill.zip |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功。 | true |
| data | Object | 扫描报告。 | {} |
| errorCode | String | 错误码。 | 400 |
| errorMsg | String | 错误描述。 | 错误 |

**示例**

**curl命令示例**

```bash
curl -X 'POST' 'http://IP:port/gatectl/agent/api/skill/scanZip' \ -H 'Content-Type: application/json' \ -H 'x-sfm-workspacecode: xxx' \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -d '{"zipUrl": "http://xxx.com/xxx.zip"}'
```

智能体工厂 OpenTrek 发指南

**返回数据**

```json
{"errorMessages":[],"success":true,"data":{"filePath":"http://sfm-lite-0518.oss-cn-hang zhou.aliyuncs.com/agent/skill-files/14ccb74d-c0a0-4959-b7e2-72d8bc3df83e/skill-vetter.z ip? Expires=1780909046&OSSAccessKeyId=LTAI********************&Signature=5UCeINi8dgzWnDDvpO0% O7tl%2FZY%3D","securityStatus":true,"insecurityReasons": []},"errorCode":null,"errorMsg":null,"extraData":null,"traceId":null,"env":null,"other":n l,"errorMessage":null,"firstErrorMessage":null,"failure":false}
```

**错误码**

| HttpCode | 错误码 | 描述 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失。 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败，无效 APP KEY。 _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败，APP KEY 已过期。 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色不匹配。 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色已过期。 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径。 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册。 |
| 429 | GATEWAY LIMIT ! | 服务触发限流，请稍后再试。 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流，请稍后再试。 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失。 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配。 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败，不支持的鉴权方式。 |
|---|---|---|
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败，AK用户信息不匹配。 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败，用户角色不匹配。 |

###### 创建Skill

创建一个新的Skill。

**接口概述**

创建一个新的Skill。 创建一个新的Skill，支持ZIP/Tool/Workflow等模式。可以通过查看请求示例，点击 curl 命令示例右侧的调试按钮验证业务接口调用效果。

```
接口调用地址: POST http://IP:port/gatectl/agent/api/skill/create
```

**请求头**

| 参数名称 | 类型 | 是否必选 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| x-sfm- workspacecode | String | 是 | 目标工作空间 | your workspace _ _ code |
| Content-Type | String | 是 | Content-Type | application/json |

**请求参数**

| 参数名称 | 类型 | 是否必选 | 描述 | 示例 |
|---|---|---|---|---|
| skillAlias | String | 是 | Skill别名。 | my-skill |
| skillType | String | 是 | Skill类型，FILE/TOOL/W ORKFLOW。 | FILE |
| zipUrl | String | 否 | ZIP文件下载URL。 | http://***** |

智能体工厂 OpenTrek 发指南

| skillMd | String | 否 | Skill MD内容。 | 描述 |
|---|---|---|---|---|
| scanReport | Object | 否 | 扫描报告。 | {} |
| skillRefs | List | 否 | 关联的Agent/Tool 列表。 | [] |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功。 | true |
| data | Object | 创建的Skill数据。 | {} |
| data.skillCode | String | Skill唯一标识。 | sk-abc123 |
| data.skillAlias | String | Skill别名。 | my-skill |
| data.skillType | String | Skill类型。 | FILE |
| data.version | String | Skill版本。 | 1716800000000 |
| data.workspaceCode | String | 所属工作空间编码。 | baseline |
| data.gmtCreate | String | 创建时间。 | 2025-08- 29T11:43:54.722+00: 00 |
| errorCode | String | 错误码。 | 400 |
| errorMsg | String | 错误描述。 | 错误 |

**示例**

**curl命令示例**

```bash
curl -X 'POST' 'http://IP:port/gatectl/agent/api/skill/create' \ -H 'Content-Type: application/json' \ -H 'x-sfm-workspacecode: xxx' \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -d '{"skillAlias": "my-skill","skillType": "FILE","zipUrl": "http://xxx.com/xxx.zip"}'
```

智能体工厂 OpenTrek 发指南

**返回数据**

```json
{"errorMessages":[],"success":true,"data":{"id":118,"skillCode":"6a4b68c2-0774-4a40-a77 e-bfe1e5673d36","skillVersion":"1780906143961","skillAlias":"my-scanskill","name":"skill-vetter","description":"Security-first skill vetting for AI agents. Use before installing any skill from ClawdHub, GitHub, or other sources. Checks for red flags, permission scope, and suspicious patterns.","skillType":"FILE","zipUrl":null,"skillRefs":null,"skillMd":"---\nname: skil l-vetter\nversion: 1.0.0\ndescription: Security-first skill vetting for AI agents. Use before installing any skill from ClawdHub, GitHub, or other sources. Checks for red fla gs, permission scope, and suspicious patterns.\n---\n\n# Skill Vetter \uD83D\uDD12\n\nSecurity-first vetting protocol for AI agent skills. **Never install a skill without vetting it first.**\n\n## When to Use\n\n- Before installing any skill fr om ClawdHub\n- Before running skills from GitHub repos\n- When evaluating skills shared by other agents\n- Anytime you're asked to install unknown code\n\n## Vetting Protocol\n\n### Step 1: Source Check\n\n```\nQuestions to answer:\n- [ ] Where did this skill come from?\n- [ ] Is the author known/reputable?\n- [ ] How many downloads/stars does it have?\n- [ ] When was it last updated?\n- [ ] Are there reviews from other agen ts?\n```\n\n### Step 2: Code Review (MANDATORY)\n\nRead ALL files in the skill. Check f or these **RED FLAGS**:\n\n```\n\uD83D\uDEA8 REJECT IMMEDIATELY IF YOU SEE:\n─────────────────────────────────────────\n• curl/wget to unknown URLs\n• Sends d ata to external servers\n• Requests credentials/tokens/API keys\n• Reads ~/.ssh, ~/.aws , ~/.config without clear reason\n• Accesses MEMORY.md, USER.md, SOUL.md, IDENTITY.md\n• Uses base64 decode on anything\n• Uses eval() or exec() with external in put\n• Modifies system files outside workspace\n• Installs packages without listing the m\n• Network calls to IPs instead of domains\n• Obfuscated code (compressed, encoded, m inified)\n• Requests elevated/sudo permissions\n• Accesses browser cookies/sessions\n• Touches credential files\n─────────────────────────────────────────\n```\n\n### Step 3: Permission Scope\n\n```\nEvaluate:\n- [ ] What files does it need to read?\n- [ ] What files does it need to write?\n- [ ] What commands does it run?\n- [ ] Does it need netw ork access? To where?\n- [ ] Is the scope minimal for its stated purpose?\n```\n\n### S tep 4: Risk Classification\n\n| Risk Level | Examples | Action |\n|------------|-------- --|--------|\n| \uD83D\uDFE2 LOW | Notes, weather, formatting | Basic review, install O K |\n| \uD83D\uDFE1 MEDIUM | File ops, browser, APIs | Full code review required |\n| \ uD83D\uDD34 HIGH | Credentials, trading, system | Human approval required |\n|   EXTREM E | Security configs, root access | Do NOT install |\n\n## Output Format\n\nAfter vetti ng, produce this report:\n\n```\nSKILL VETTING REPORT\n═══════════════════════════════════════\nSkill: [name]\nSource: [ClawdHub / Git Hub / other]\nAuthor: [username]\nVersion: [version]\n───────────────────────────────────────\nMETRICS:\n• Downloads/Stars: [count ]\n• Last Updated: [date]\n• Files Reviewed: [count]\n───────────────────────────────────────\nRED FLAGS: [None / List them]\n\nPERMISSIONS NEEDED:\n• Files: [list or \"None\"]\n• Network: [list or \"None\" ] \n• Commands: [list or \"None\"]\n───────────────────────────────────────\nRISK LEVE L: [\uD83D\uDFE2 LOW / \uD83D\uDFE1 MEDIUM / \uD83D\uDD34 HIGH /   EXTREME]\n\nVERDICT: [  SAFE TO INSTALL / ⚠️ INSTALL WITH CAUTION /   DO NOT INSTALL]\n\nNOTES: [Any observat ions]\n═══════════════════════════════════════\n```\n\n## Quick Vet Commands\n\nFor Git Hub-hosted skills:\n```bash\n# Check repo stats\ncurl -s \"https://api.github.com/repos/OWNER/REPO\" | jq '{stars: .stargazers_count, forks: .fo rks_count, updated: .updated_at}'\n\n# List skill files\ncurl -s \"https://api.github.com/repos/OWNER/REPO/contents/skills/SKILL_NAME\" | jq '.[].name'\ n\n# Fetch and review SKILL.md\ncurl -s \"https://raw.githubusercontent.com/OWNER/REPO/main/skills/SKILL_NAME/SKILL.md\"\n```\n\n Trust Hierarchy\n\n1. **Official OpenClaw skills** → Lower scrutiny (still review)\n2.
**Highstarrepos(1000+)**
Moderatescrutiny\n3
**Knownauthors**
Moderatescruti
```

智能体工厂 OpenTrek 发指南

```
**High-star repos (1000+)** → Moderate scrutiny\n3. **Known authors** → Moderate scruti
ny\n4. **New/unknown sources** → Maximum scrutiny\n5. **Skills requesting credentials** → Human approval always\n\n## Remember\n\n- No skill is worth compromising security\n- When in doubt, don't install\n- Ask your human for high-risk decisions\n- Document what you vet for future reference\n\n---\n\n*Paranoia is a feature.* \uD83D\uDD12\uD83E\uDD80\n","scanReport":{"filePath":"http://sfm-lite-0518.oss-cn-hangz hou.aliyuncs.com/agent/skill-files/14ccb74d-c0a0-4959-b7e2-72d8bc3df83e/skill-vetter.zi
```

p?

```json
Expires=1780909046&OSSAccessKeyId=LTAI********************&Signature=5UCeINi8dgzWnDDvpO0% O7tl%2FZY%3D","securityStatus":true,"insecurityReasons": []},"status":"PUBLISHED","masterFlag":true,"labels":null,"feature":null,"shareWorkspaces" ull,"workspaceCode":"7a92789c-3882-43f5-be70- 87c84b7fbede","tenant":"baseline","gmtCreate":"2026-06- 08T08:09:03.962+00:00","gmtModified":"2026-06-08T08:09:03.962+00:00","creator":{"id":nu ll,"gmtCreate":null,"gmtModified":null,"tenant":null,"uniqueCode":"7551a976815b413bb85907 9b0677d7","source":null,"outerId":null,"name":"opentrek"},"modifier": {"id":null,"gmtCreate":null,"gmtModified":null,"tenant":null,"uniqueCode":"7551a976815b41 b859074c9b0677d7","source":null,"outerId":null,"name":"opentrek"},"skillCategory":"worksp e","installStatus":null,"exampleQuestions":null,"newVersionFlag":null},"errorCode":null," rorMsg":null,"extraData":null,"traceId":null,"env":null,"other":null,"errorMessage":null, irstErrorMessage":null,"failure":false}
```

**错误码**

| HttpCode | 错误码 | 描述 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失。 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败，无效 APP KEY。 _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败，APP KEY 已过期。 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色不匹配。 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色已过期。 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径。 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册。 |
| 429 | GATEWAY LIMIT ! | 服务触发限流，请稍后再试。 |

智能体工厂 OpenTrek 发指南

| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流，请稍后再试。 |
|---|---|---|
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失。 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配。 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败，不支持的鉴权方式。 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败，AK用户信息不匹配。 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败，用户角色不匹配。 |

###### 更新Skill

更新已有的Skill。

**接口概述**

更新已有的Skill。 更新已有的Skill信息。可以通过查看请求示例，点击 curl 命令示例右侧的调试按钮验证业务接口调用效果。

```
接口调用地址: POST http://IP:port/gatectl/agent/api/skill/update
```

**请求头**

| 参数名称 | 类型 | 是否必选 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| x-sfm- workspacecode | String | 是 | 目标工作空间 | your workspace _ _ code |
| Content-Type | String | 是 | Content-Type | application/json |

**请求参数**

| 参数名称 | 类型 | 是否必选 | 描述 | 示例 |
|---|---|---|---|---|

智能体工厂 OpenTrek 发指南

| skillCode | String | 是 | Skill唯一标识。 | sk-abc123 |
|---|---|---|---|---|
| skillAlias | String | 否 | Skill别名。 | my-skill-updated |
| skillType | String | 否 | Skill类型，FILE/TOOL/W ORKFLOW。 | FILE |
| zipUrl | String | 否 | ZIP文件下载URL。 | http://**** |
| skillMd | String | 否 | Skill MD内容。 | 内容 |
| scanReport | Object | 否 | 扫描报告。 | {} |
| skillRefs | List | 否 | 关联的Agent/Tool 列表。 | [] |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功。 | true |
| errorCode | String | 错误码。 | 400 |
| errorMsg | String | 错误描述. | 错误 |

**示例**

**curl命令示例**

```bash
curl -X 'POST' 'http://IP:port/gatectl/agent/api/skill/update' \ -H 'Content-Type: application/json' \ -H 'x-sfm-workspacecode: xxx' \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -d '{"skillCode": "sk-abc123","skillAlias": "my-skill-updated","zipUrl": "http://xxx.com/xxx.zip"}'
```

**返回数据**

```json
{"errorMessages": [],"success":true,"data":null,"errorCode":null,"errorMsg":null,"extraData":null,"traceId" ull,"env":null,"other":null,"errorMessage":null,"firstErrorMessage":null,"failure":false}
```

智能体工厂 OpenTrek 发指南

**错误码**

| HttpCode | 错误码 | 描述 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失。 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败，无效 APP KEY。 _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败，APP KEY 已过期。 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配。 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期。 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径。 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册。 |
| 429 | GATEWAY LIMIT ! | 服务触发限流，请稍后再试。 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流，请稍后再试。 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失。 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配。 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败，不支持的鉴权方式。 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败，AK用户信息不匹配。 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败，用户角色不匹配。 |

智能体工厂 OpenTrek 发指南

###### 删除Skill

删除指定的Skill。

**接口概述**

删除指定的Skill。 删除指定的Skill。可以通过查看请求示例，点击 curl 命令示例右侧的调试按钮验证业务接口调用效果。

```
接口调用地址: POST http://IP:port/gatectl/agent/api/skill/delete
```

**请求头**

| 参数名称 | 类型 | 是否必选 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| x-sfm- workspacecode | String | 是 | 目标工作空间 | your workspace _ _ code |
| Content-Type | String | 是 | Content-Type | application/json |

**请求参数**

| 参数名称 | 类型 | 是否必选 | 描述 | 示例 |
|---|---|---|---|---|
| skillCode | String | 是 | Skill唯一标识。 | sk-abc123 |
| skillVersion | String | 否 | Skill版本号，不传则删除所有版本。 |  |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功。 | true |
| errorCode | String | 错误码。 | 400 |
| errorMsg | String | 错误描述。 | 错误 |

**示例**

**curl命令示例**

智能体工厂 OpenTrek 发指南

```bash
curl -X 'POST' 'http://IP:port/gatectl/agent/api/skill/delete' \ -H 'Content-Type: application/json' \ -H 'x-sfm-workspacecode: xxx' \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -d '{"skillCode": "sk-abc123"}'
```

**返回数据**

```json
{"errorMessages": [],"success":true,"data":null,"errorCode":null,"errorMsg":null,"extraData":null,"traceId" ull,"env":null,"other":null,"errorMessage":null,"firstErrorMessage":null,"failure":false}
```

**错误码**

| HttpCode | 错误码 | 描述 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失。 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败，无效 APP KEY。 _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败，APP KEY 已过期。 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色不匹配。 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色已过期。 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径。 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册。 |
| 429 | GATEWAY LIMIT ! | 服务触发限流，请稍后再试。 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流，请稍后再试。 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失。 |

智能体工厂 OpenTrek 发指南

| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配。 |
|---|---|---|
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败，不支持的鉴权方式。 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败，AK用户信息不匹配。 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败，用户角色不匹配。 |

###### 分享Skill

将Skill分享到其他工作空间。

**接口概述**

将Skill分享到其他工作空间。 将Skill分享到其他工作空间。可以通过查看请求示例，点击 curl 命令示例右侧的调试按钮验证业务接口调用效果。

```
接口调用地址: POST http://IP:port/gatectl/agent/api/skill/share
```

**请求头**

| 参数名称 | 类型 | 是否必选 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| x-sfm- workspacecode | String | 是 | 目标工作空间 | your workspace _ _ code |
| Content-Type | String | 是 | Content-Type | application/json |

**请求参数**

| 参数名称 | 类型 | 是否必选 | 描述 | 示例 |
|---|---|---|---|---|
| skillCode | String | 是 | Skill唯一标识。 | sk-abc123 |
| shareWorkspaces | List | 否 | 目标工作空间列表。 | ["workspace-1", "workspace-2"] |

智能体工厂 OpenTrek 发指南

| allFlag | Boolean | 否 | 是否分享到所有空间。 | false |
|---|---|---|---|---|

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功。 | true |
| errorCode | String | 错误码。 | 400 |
| errorMsg | String | 错误描述。 | 错误 |

**示例**

**curl命令示例**

```bash
curl -X 'POST' 'http://IP:port/gatectl/agent/api/skill/share' \ -H 'Content-Type: application/json' \ -H 'x-sfm-workspacecode: xxx' \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -d '{"skillCode": "sk-abc123","shareWorkspaces": ["workspace-1"],"allFlag": false}'
```

**返回数据**

```json
{
    "skillCode": "d001c015-9008-456b-8f0b-28562902df11",
    "shareWorkspaces": [
        "84e47d28-0570-4469-b729-de76d89362f0"
```

`],`

```json
    "allFlag": false
}
```

**错误码**

| HttpCode | 错误码 | 描述 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失。 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败，无效 APP KEY。 _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败，APP KEY 已过期。 _ |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色不匹配。 |
|---|---|---|
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色已过期。 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径。 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册。 |
| 429 | GATEWAY LIMIT ! | 服务触发限流，请稍后再试。 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流，请稍后再试。 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失。 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配。 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败，不支持的鉴权方式。 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败，AK用户信息不匹配。 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败，用户角色不匹配。 |

###### 安装已分享的Skill

将已分享的Skill安装到当前工作空间。

**接口概述**

将已分享的Skill安装到当前工作空间。 将已分享的Skill安装到当前工作空间。可以通过查看请求示例，点击 curl 命令示例右侧的调试按钮验证业务接口调用效果。

```
接口调用地址: POST http://IP:port/gatectl/agent/api/skill/installShared
```

**请求头**

智能体工厂 OpenTrek 发指南

| 参数名称 | 类型 | 是否必选 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| x-sfm- workspacecode | String | 是 | 目标工作空间 | your workspace _ _ code |
| Content-Type | String | 是 | Content-Type | application/json |

**请求参数**

| 参数名称 | 类型 | 是否必选 | 描述 | 示例 |
|---|---|---|---|---|
| skillCode | String | 是 | Skill唯一标识。 | sk-abc123 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功。 | true |
| data | Object | 安装后的Skill数据。 | {} |
| errorCode | String | 错误码。 | 400 |
| errorMsg | String | 错误描述。 | 错误 |

**示例**

**curl命令示例**

```bash
curl -X 'POST' 'http://IP:port/gatectl/agent/api/skill/installShared' \ -H 'Content-Type: application/json' \ -H 'x-sfm-workspacecode: xxx' \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -d '{"skillCode": "sk-abc123"}'
```

**返回数据**

```json
{"errorMessages":[],"success":true,"data":{"id":142,"skillCode":"cf5241ac-911f-4c14-b74 d-eab4e04d8351","skillVersion":"1780920773649","skillAlias":"my-scanskill","name":"skill-vetter","description":"Security-first skill vetting for AI agents. Use before installing any skill from ClawdHub, GitHub, or other sources. Checks for red flags, permission scope, and suspicious
```

智能体工厂 OpenTrek 发指南

```
ags,pe sso scope,adsuspcous patterns.","skillType":"FILE","zipUrl":null,"skillRefs":null,"skillMd":"---\nname: skil l-vetter\nversion: 1.0.0\ndescription: Security-first skill vetting for AI agents. Use before installing any skill from ClawdHub, GitHub, or other sources. Checks for red fla gs, permission scope, and suspicious patterns.\n---\n\n# Skill Vetter \uD83D\uDD12\n\nSecurity-first vetting protocol for AI agent skills. **Never install a skill without vetting it first.**\n\n## When to Use\n\n- Before installing any skill fr om ClawdHub\n- Before running skills from GitHub repos\n- When evaluating skills shared by other agents\n- Anytime you're asked to install unknown code\n\n## Vetting Protocol\n\n### Step 1: Source Check\n\n```\nQuestions to answer:\n- [ ] Where did this skill come from?\n- [ ] Is the author known/reputable?\n- [ ] How many downloads/stars does it have?\n- [ ] When was it last updated?\n- [ ] Are there reviews from other agen ts?\n```\n\n### Step 2: Code Review (MANDATORY)\n\nRead ALL files in the skill. Check f or these **RED FLAGS**:\n\n```\n\uD83D\uDEA8 REJECT IMMEDIATELY IF YOU SEE:\n─────────────────────────────────────────\n• curl/wget to unknown URLs\n• Sends d ata to external servers\n• Requests credentials/tokens/API keys\n• Reads ~/.ssh, ~/.aws , ~/.config without clear reason\n• Accesses MEMORY.md, USER.md, SOUL.md, IDENTITY.md\n• Uses base64 decode on anything\n• Uses eval() or exec() with external in put\n• Modifies system files outside workspace\n• Installs packages without listing the m\n• Network calls to IPs instead of domains\n• Obfuscated code (compressed, encoded, m inified)\n• Requests elevated/sudo permissions\n• Accesses browser cookies/sessions\n• Touches credential files\n─────────────────────────────────────────\n```\n\n### Step 3: Permission Scope\n\n```\nEvaluate:\n- [ ] What files does it need to read?\n- [ ] What files does it need to write?\n- [ ] What commands does it run?\n- [ ] Does it need netw ork access? To where?\n- [ ] Is the scope minimal for its stated purpose?\n```\n\n### S tep 4: Risk Classification\n\n| Risk Level | Examples | Action |\n|------------|-------- --|--------|\n| \uD83D\uDFE2 LOW | Notes, weather, formatting | Basic review, install O K |\n| \uD83D\uDFE1 MEDIUM | File ops, browser, APIs | Full code review required |\n| \ uD83D\uDD34 HIGH | Credentials, trading, system | Human approval required |\n|   EXTREM E | Security configs, root access | Do NOT install |\n\n## Output Format\n\nAfter vetti ng, produce this report:\n\n```\nSKILL VETTING REPORT\n═══════════════════════════════════════\nSkill: [name]\nSource: [ClawdHub / Git Hub / other]\nAuthor: [username]\nVersion: [version]\n───────────────────────────────────────\nMETRICS:\n• Downloads/Stars: [count ]\n• Last Updated: [date]\n• Files Reviewed: [count]\n───────────────────────────────────────\nRED FLAGS: [None / List them]\n\nPERMISSIONS NEEDED:\n• Files: [list or \"None\"]\n• Network: [list or \"None\" ] \n• Commands: [list or \"None\"]\n───────────────────────────────────────\nRISK LEVE L: [\uD83D\uDFE2 LOW / \uD83D\uDFE1 MEDIUM / \uD83D\uDD34 HIGH /   EXTREME]\n\nVERDICT: [  SAFE TO INSTALL / ⚠️ INSTALL WITH CAUTION /   DO NOT INSTALL]\n\nNOTES: [Any observat ions]\n═══════════════════════════════════════\n```\n\n## Quick Vet Commands\n\nFor Git Hub-hosted skills:\n```bash\n# Check repo stats\ncurl -s \"https://api.github.com/repos/OWNER/REPO\" | jq '{stars: .stargazers_count, forks: .fo rks_count, updated: .updated_at}'\n\n# List skill files\ncurl -s \"https://api.github.com/repos/OWNER/REPO/contents/skills/SKILL_NAME\" | jq '.[].name'\ n\n# Fetch and review SKILL.md\ncurl -s \"https://raw.githubusercontent.com/OWNER/REPO/main/skills/SKILL_NAME/SKILL.md\"\n```\n\n Trust Hierarchy\n\n1. **Official OpenClaw skills** → Lower scrutiny (still review)\n2.
**High-star repos (1000+)** → Moderate scrutiny\n3. **Known authors** → Moderate scruti
ny\n4. **New/unknown sources** → Maximum scrutiny\n5. **Skills requesting credentials** → Human approval always\n\n## Remember\n\n- No skill is worth compromising security\n- When in doubt, don't install\n- Ask your human for high-risk decisions\n- Document what you vet for future reference\n\n---\n\n*Paranoia is a feature.* \uD83D\uDD12\uD83E\uDD80\n","scanReport":{"filePath":"http://sfm-lite-0518.oss-cn-hangz hou.aliyuncs.com/agent/skill-files/bc0d15d1-7374-4a49-badd-4bf50476dfba/skill-vetter.zi
```

智能体工厂 OpenTrek 发指南 p?

```json
Expires=1780921566&OSSAccessKeyId=LTAI********************&Signature=ik5oeP3Ae%2BX8yX5aKa cwT2%2Ba4%3D","securityStatus":true,"insecurityReasons": []},"status":"PUBLISHED","masterFlag":true,"labels":null,"feature":{"share":{"sourceSki llCode":"d001c015-9008-456b-8f0b- 28562902df11","sourceSkillVersion":"1780918391717","sourceSkillCategory":"share"}},"share rkspaces":null,"workspaceCode":"84e47d28-0570-4469-b729de76d89362f0","tenant":"baseline","gmtCreate":"2026-06- 08T12:12:53.649+00:00","gmtModified":"2026-06-08T12:12:53.649+00:00","creator":{"id":nu ll,"gmtCreate":null,"gmtModified":null,"tenant":null,"uniqueCode":"7551a976815b413bb85907 9b0677d7","source":null,"outerId":null,"name":"opentrek"},"modifier": {"id":null,"gmtCreate":null,"gmtModified":null,"tenant":null,"uniqueCode":"7551a976815b41 b859074c9b0677d7","source":null,"outerId":null,"name":"opentrek"},"skillCategory":"worksp e","installStatus":null,"exampleQuestions":null,"newVersionFlag":null},"errorCode":null," rorMsg":null,"extraData":null,"traceId":null,"env":null,"other":null,"errorMessage":null, irstErrorMessage":null,"failure":false}
```

**错误码**

| HttpCode | 错误码 | 描述 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失。 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败，无效 APP KEY。 _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败，APP KEY 已过期。 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色不匹配。 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色已过期。 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径。 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册。 |
| 429 | GATEWAY LIMIT ! | 服务触发限流，请稍后再试。 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流，请稍后再试。 |

智能体工厂 OpenTrek 发指南

| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失。 |
|---|---|---|
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配。 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败，不支持的鉴权方式。 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败，AK用户信息不匹配。 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败，用户角色不匹配。 |

###### 生成Skill MD

根据参数自动生成Skill的Markdown描述文档。

**接口概述**

根据参数自动生成Skill的Markdown描述文档。 根据参数自动生成Skill的Markdown描述文档。可以通过查看请求示例，点击 curl 命令示例右侧的调试按钮验证业务接口调用效果。

```
接口调用地址: POST http://IP:port/gatectl/agent/api/skill/generateSkillMD
```

**请求头**

| 参数名称 | 类型 | 是否必选 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| x-sfm- workspacecode | String | 是 | 目标工作空间 | your workspace _ _ code |
| Content-Type | String | 是 | Content-Type | application/json |

**请求参数**

| 参数名称 | 类型 | 是否必选 | 描述 | 示例 |
|---|---|---|---|---|
| skillAlias | String | 是 | Skill别名。 | my-skill |

智能体工厂 OpenTrek 发指南

| skillType | String | 是 | Skill类型。 | TOOL |
|---|---|---|---|---|
| skillRefs | List | 否 | 关联的Agent/Tool 列表。 | [] |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功。 | true |
| data | String | 生成的Skill MD内容。 | # My Skill ... |
| errorCode | String | 错误码。 | 400 |
| errorMsg | String | 错误描述。 | 错误 |

**示例**

**curl命令示例**

```bash
curl -X 'POST' 'http://IP:port/gatectl/agent/api/skill/generateSkillMD' \ -H 'Content-Type: application/json' \ -H 'x-sfm-workspacecode: xxx' \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -d '{"skillAlias": "my-skill","skillType": "FILE","enableLlm": true}'
```

**返回数据**

智能体工厂 OpenTrek 发指南

```json
{"errorMessages":[],"success":true,"data":"---\r\nname: \r\ndescription: \"Execute pl
```

`atform API tools via ibp-agent. Includes: (1)` 支持开发者将夸克搜索能力无缝集成至大模型应用中， 实现网页内容检索、实时资讯获取等功能。. \r\nUse when the user needs to call standardized

```
platform APIs for CRUD operations, data queries, or system integrations.\"\r\n---\r\n\r \n# Platform API Tool\r\n\r\nExecute platform API tools through ibp-agent's standardize d API gateway.\r\n\r\n## Tool Structure\r\n\r\nAn API Skill contains 1 tool definitions
```

:\r\n\r\n**Tool 1:**\n```json\n{\n\t\"desc\":\"支持开发者将夸克搜索能力无缝集成至大模型应用中， 实现网页内容检索、实时资讯获取等功能。\",\n\t\"toolParam\":

```
[\n\t\t{\n\t\t\t\"fieldCode\":\"query\",\n\t\t\t\"fieldType\":\"STRING\",\n\t\t\t\"requir
```

\":true,\n\t\t\t\"fieldDesc\":\"用户搜索信息

```
\",\n\t\t\t\"fieldDemo\":\"\"\n\t\t},\n\t\t{\n\t\t\t\"fieldCode\":\"whiteSites\",\n\t\t\t fieldType\":\"LIST_STRING\",\n\t\t\t\"required\":false,\n\t\t\t\"fieldDesc\":\"白名单站点
```

列表

```
\",\n\t\t\t\"fieldDemo\":\"baidu.com\"\n\t\t},\n\t\t{\n\t\t\t\"fieldCode\":\"startPublish Date\",\n\t\t\t\"fieldType\":\"STRING\",\n\t\t\t\"required\":false,\n\t\t\t\"fieldDesc\": 发布时间\",\n\t\t\t\"fieldDemo\":\"2025-07-01\"\n\t\t}\n\t]\n}\n```\n\n\r\n\r\n## Usage\r\n\r\nCall the `executePlatformApiTool` with toolCode, toolVersion, and toolPara m:\r\n\r\n```json\n[\n\t{\n\t\t\"toolParam\":\"{\\\"query\\\":{},\\\"whiteSites\\\":{}, \\\"startPublishedDate\\\":{}}\"\n\t}\n]\n```\n\r\n\r\n## toolParam Schema\r\n\r\nThe t oolParam is built from the tool's `toolParam` field definition:\r\n\r\n**Example fields :**\n\n### Tool: 10001baseline\n- `query` (string, required, non-leaf): 用户搜索信息\n- ` whiteSites` (list_string, optional, non-leaf): 白名单站点列表 - baidu.com\n- `startPublishedDate` (string, optional, non-leaf): 发布时间 - \"2025-07- 01\"\n\r\n\r\n**Rules:**\r\n- toolParam is a JSON string (escape quotes with \\\")\r\n-
**fieldCode**: Parameter name, use as JSON key\r\n- **fieldType**: Value type - string,
number, boolean, object, array\r\n- **required**: Must include if true, optional if fal se\r\n- **leaf**: true means basic type (direct value), false means object (has childre n)\r\n- **parentFieldCode**: Identifies parent for nested fields (e.g., \"product\" for product.name)\r\n- **fieldDesc**: Parameter description, helps understand purpose\r\n-
**fieldDemo**: Example value for reference\r\n- **refValue**: Default value - use when
model cannot extract suitable value from user input\r\n- **children**: Nested field def initions for object types (leaf=false)\r\n- For optional fields without user input, use `refValue` as default\r\n- If `refValue` exists and model cannot extract suitable value from user input, use it\r\n- Follow `fieldType` for value type (string, number, boolean , object, array)\r\n- For nested objects (leaf=false), build nested JSON structure and escape as string\r\n- Use `parentFieldCode` to identify the parent-child relationship\r\n\r\n## Notes\r\n\r\n- **toolCode**: The unique tool code from Tool Stru cture (code field)\r\n- **toolVersion**: The tool version from Tool Structure (version field)\r\n- **toolParam**: Must be a valid JSON string (escape quotes with \\\")\r\n- I nclude all `required=true` fields from toolParam schema\r\n- **refValue usage**: When m odel cannot extract suitable value from user input, use refValue as default\r\n- Respon se time is typically fast (milliseconds)\r\n- API tools are stateless\r\n- Timeout: 120 seconds\r\n","errorCode":null,"errorMsg":null,"extraData":null,"traceId":null,"env":null, ther":null,"errorMessage":null,"firstErrorMessage":null,"failure":false}
```

**错误码**

| HttpCode | 错误码 | 描述 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失。 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败，无效 APP KEY。 _ |
|---|---|---|
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败，APP KEY 已过期。 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色不匹配。 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色已过期。 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径。 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册。 |
| 429 | GATEWAY LIMIT ! | 服务触发限流，请稍后再试。 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流，请稍后再试。 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失。 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配。 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败，不支持的鉴权方式。 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败，AK用户信息不匹配。 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败，用户角色不匹配。 |

###### 智能体模板

###### 查询智能体模版详情

**接口概述**

智能体工厂 OpenTrek 发指南

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/agent/openapi/template/getOne POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostAgentOpenapiTemplateGetone

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| itemCode | Strin g | Body | 是 | 3b7628cc51544996908b 6ea55ae07bc1 | 模版编码，该参数必填 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | Object | 返回数据 | {} |
| itemCode | String | 模版编码 | 3b7628cc5154499690 8b6ea55ae07bc1 |
| itemName | String | 模版名称 | 对话助手 |
| agentDesc | String | 智能体描述 | DB 随表召回 |

智能体工厂 OpenTrek 发指南

| marketCode | String | 模版类型，system=平台模版，common=自定义模版 | system |
|---|---|---|---|
| showDetail | Object | 模版详情 |  |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式

```json
{
  "success": true,
  "errorCode": null,
  "errorMsg": null,
  "data": {
    "marketCode": "system",
```

`"marketName": "`自定义模版`",`

```json
    "itemCode": "3b7628cc51544996808b6ea55ae07bc1",
```

`"itemName": "AutoBot`对话助手`",` `"itemLabels": ["`系统内置`"],`

```json
    "itemType": "agentTemplate",
    "targetCode": "851d5b0b-8393-497c-b909-1d3209efee74",
    "targetName": "v1.0",
    "targetVersion": "1731573095677",
    "status": "online",
    "statusDesc": "已上架",
    "showDetail": {
      "type": "platform",
```

`"description": "`综合问答能力`",`

```json
      "skills": [
```

"支持接入用户已有业务`api",` "支持`OneRag`插件联动用户业务数据`",` "支持接入其他智能体实例" `],`

```json
      "usage": {
        "configDesc": "无",
        "limitDesc": "无"
      },
      "interfaceInfo": {
        "interfaceDesc": "无",
        "inputParams": [
          {
            "name": "sessionId",
            "label": "sessionId",
            "type": "STRING",
            "necessary": true,
            "example": "bd962db7-b1c8-4466-a2cc-41b9b67cd94b"
```

智能体工厂 OpenTrek 发指南

```json
          },
          {
            "name": "stream",
```

`"label": "`是否流式`",`

```json
            "type": "BOOL",
            "necessary": true,
            "example": "true"
          },
          {
            "name": "message",
```

`"label": "`请求消息体`",`

```json
            "type": "OBJECT",
            "necessary": true,
```

"example": "{\"text\":\"帮我订一张明天从上海去苏黎世的机票\"}",

```json
            "children": [
              {
                "name": "text",
```

`"label": "`对话输入`",`

```json
                "type": "STRING",
                "necessary": true
              }
```

]

```
          }
```

`],`

```json
        "outputParams": [
          {
            "name": "object",
```

`"label": "`数据类型`",`

```json
            "type": "STRING",
            "necessary": true,
            "example": "message.delta"
          },
          {
            "name": "role",
            "label": "角色",
            "type": "STRING",
            "necessary": true,
            "example": "assistant"
          },
          {
            "name": "sessionId",
```

`"label": "`当前会话`ID",`

```json
            "type": "STRING",
            "necessary": true
          }
```

]

```json
      }
    },
    "config": null,
    "feature": {
      "templateType": "AutoBot"
    }
  }
}
```

智能体工厂 OpenTrek 发指南

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

智能体工厂 OpenTrek 发指南

###### 查询智能体模板列表

**接口概述**

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/agent/openapi/template/pageQuery POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostAgentOpenapiTemplatePagequery

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| current | Integ er | Body | 是 | 1 | 当前页数，该参数必填 |
| pageSize | Integ er | Body | 是 | 10 | 每页条数，该参数必填 |
| name | Strin g | Body | 是 | 对话助手 | 模版名称模糊搜索，该参数必填 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |

智能体工厂 OpenTrek 发指南

| data | Object | 返回数据 | {} |
|---|---|---|---|
| total | Integer | 查询到的模版总数 | 1 |
| list | List | 查询到的模版列表 |  |
| itemCode | String | 模版编码 | 3b7628cc5154499690 8b6ea55ae07bc1 |
| itemName | String | 模版名称 | 对话助手 |
| agentDesc | String | 智能体描述 | DB 随表召回 |
| marketCode | String | 模版类型，system=平台模版，common=自定义模版 | system |
| showDetail | Object | 模版详情 |  |
| pageSize | Integer | 每页大小 | 60 |
| current | Integer | 目前所在页数 | 1 |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式

```json
{
  "success": true,
  "errorCode": null,
  "errorMsg": null,
  "data": {
    "total": 1,
    "current": 1,
    "pageSize": 10,
    "totalPages": 1,
    "list": [
      {
        "marketCode": "common",
```

`"marketName": "`自定义模版`",`

```json
        "itemCode": "79d39852ceb148b9a0afe674a2e6d38d",
```

智能体工厂 OpenTrek 发指南

```json
        "itemName": "whatsapp",
        "itemLabels": ["whatsapp"],
        "itemType": "agentTemplate",
        "targetCode": "22bb7850-78b2-4ce7-b29d-682460f6a6ed",
        "targetName": "工具",
        "targetVersion": "1740037093657",
        "status": "online",
        "statusDesc": "已上架",
        "showDetail": {
          "icon": "AGENT_ICON_6",
          "description": "whatsapp",
          "type": "custom",
          "usage": {
            "configDesc": "whatsapp",
            "limitDesc": "whatsapp"
          },
          "interfaceInfo": {
            "interfaceDesc": "whatsapp",
            "inputParams": [
              {
                "name": "sessionId",
                "label": "sessionId",
                "type": "STRING",
                "necessary": true,
                "example": "bd962db7-b1c8-4466-a2cc-41b9b67cd94b"
              }
```

`],`

```json
            "outputParams": [
              {
                "name": "object",
```

`"label": "`数据类型`",`

```json
                "type": "STRING",
                "necessary": true,
                "example": "message.delta"
              }
```

]

```json
          }
        },
        "config": {
          "agentCode": "22bb7850-78b2-4ce7-b29d-682460f6a6ed",
```

`"agentName": "lxj`智能体查看`",`

```json
          "versionName": "工具",
          "versionCode": "1740037093657"
        }
      }
```

]

```
  }
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
|---|---|---|
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

##### 提示词模板

###### 创建/更新提示词模版

智能体工厂 OpenTrek 发指南

**接口概述**

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/agent/openapi/prompt/save POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostAgentOpenapiPromptSave

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Integ er | Body | 是 | 12 | 提示词模版唯一标识（更新场景必填） |
| name | Strin g | Body | 是 | 测试 | 提示词模版名称，该参数必填 |
| labels | Repe atLis t | Body | 是 | ["职场效率"] | 分类标签，该参数必填 |
| frame | Strin g | Body | 是 | Custom | 提示词框架类型，Custom\|CRISPE\|Few- shot，该参数必填 |
| promptTe mp | Strin g | Body | 是 | 测试内容 | 提示词摘要，该参数必填 |

智能体工厂 OpenTrek 发指南

| prompt | Strin g | Body | 是 | {"prompt":"将此md内容转换为txt格式，只输出txt格式内容 ```markdown {{mdContent}} ```"} | 提示词模版内容，结构化json 格式，该参数必填 |
|---|---|---|---|---|---|

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式

```json
{
    "success": true,
    "errorCode": null,
    "errorMsg": null
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |

智能体工厂 OpenTrek 发指南

| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
|---|---|---|
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 发布提示词模版

**接口概述**

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/agent/openapi/prompt/deploy POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostAgentOpenapiPromptDeploy

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek 发指南

| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
|---|---|---|---|---|---|
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Integ er | Body | 是 | 1234 | 提示词模版唯一标识，该参数必填 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式

```json
{
    "success": true,
    "errorCode": null,
    "errorMsg": null
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
|---|---|---|
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 查询提示词分类

**接口概述**

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/agent/openapi/prompt/queryPromptTypes 智能体工厂 OpenTrek 发指南 POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostAgentOpenapiPromptQueryprompttypes

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| current | Integ er | Body | 是 | 1 | 当前页数，该参数必填 |
| pageSize | Integ er | Body | 是 | 10 | 每页条数，该参数必填 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | Object | 返回数据 | {} |
| total | Integer | 查询到的提示词分类总数 | 1 |
| list | List | 查询到的提示词分类列表 |  |
| code | String | 提示词分类唯一编码 | ZCXL |
| name | String | 提示词分类名称 | 职场效率 |
| pageSize | Integer | 每页大小 | 60 |

智能体工厂 OpenTrek 发指南

| current | Integer | 目前所在页数 | 1 |
|---|---|---|---|
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式

```json
{
    "success": true,
    "data": {
        "total": 1,
        "list": [
            {
                "id": null,
                "gmtCreate": "2025-06-17T07:20:49.621+00:00",
                "gmtModified": "2025-06-17T07:20:49.621+00:00",
                "code": "ZCXL",
```

`"name": "`职场效率`",`

```json
                "marketType": "promptTemplate",
                "desc": null,
                "owner": {
                    "userId": "503",
                    "userName": "test"
                },
                "modifiyUser": null,
                "recommendItems": null,
                "feature": null,
                "managers": null
            }
```

`],`

```json
        "pageSize": 10,
        "current": 1,
        "totalPages": 1
    },
    "errorCode": null,
    "errorMsg": null
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
|---|---|---|
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 删除提示词模版

**接口概述**

**接口调用地址**

POST 智能体工厂 OpenTrek 发指南 POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/agent/openapi/prompt/delete POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostAgentOpenapiPromptDelete

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Integ er | Body | 是 | 1234 | 提示词模版唯一标识，该参数必填 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式

```json
{
    "success": true,
    "errorCode": null,
    "errorMsg": null
}
```

**文档补充说明**

智能体工厂 OpenTrek 发指南

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 查询提示词模版列表

智能体工厂 OpenTrek 发指南

**接口概述**

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/agent/openapi/prompt/pageQuery POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostAgentOpenapiPromptPagequery

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| current | Integ er | Body | 是 | 1 | 当前页数，该参数必填 |
| pageSize | Integ er | Body | 是 | 10 | 每页条数，该参数必填 |
| type | Strin g | Body | 是 | custom | 提示词模版类型，custom: 我的提示词，platform: 平台提示词，该参数必填 |
| name | Strin g | Body | 是 | 测试名称 | 提示词名称，模糊搜索，该参数必填 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |

智能体工厂 OpenTrek 发指南

| data | Object | 返回数据 | {} |
|---|---|---|---|
| total | Integer | 查询到的提示词模版总数 | 1 |
| list | List | 查询到的提示词模版列表 |  |
| id | Integer | 提示词模版唯一编码 | 57 |
| name | String | 提示词模版名称 | md格式转txt |
| type | Integer | 提示词模版类型，custom: 我的提示词，system: 平台提示词 | custom: 我的提示词，system: 平台提示词 |
| labels | String | 分类标签 | ["职场效率"] |
| projectCode | String | 所属工作空间编码 | baseline |
| frame | String | 提示词框架类型，Custom\|CRISPE\|Fe w-shot | Custom |
| prompt | String | 提示词模版内容，结构化 json格式 | {"prompt":"将此md内容转换为txt格式，只输出 txt格式内容 `markdown {{mdContent}} ```"} |
| pageSize | Integer | 每页大小 | 60 |
| current | Integer | 目前所在页数 | 1 |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式智能体工厂 OpenTrek 发指南

```json
{
  "errorMessages": [],
  "success": true,
  "data": {
    "extInfos": {},
    "total": 1,
    "list": [
      {
        "id": 5,
        "projectCode": "fmthktsjdb",
```

`"name": "`神阳自定义`",`

```json
        "frame": "Custom",
```

"prompt": "{\"prompt\":\"你是一个`{{`学科`}}`教授，根据自己的专业知识回答用户问题。\"}", `"promptTemp": "`你是一个`{{`学科`}}`教授，根据自己的专业知识回答用户问题。`",`

```json
        "debugModel": "rsv-ik4zut8s",
        "debugModelVersion": "OPENTREK_MODEL_DEFAULT_VERSION",
```

"debugArgs": "{\"学科\":\"计算机\"}",

```json
        "debugStatus": "success",
```

`"debugResult": "`当然，我会尽力帮助你解答关于计算机科学的问题。请问你对哪方面感兴趣？例如编程语言、数据结构、算法、操作系统、网络、数据库等。`",`

```json
        "creatorId": null,
        "creator": null,
        "modified": null,
        "lastModified": null,
        "gmtCreate": "2025-07-21T07:00:33.013+00:00",
        "gmtModified": "2025-09-05T02:24:45.976+00:00",
        "isDel": false,
        "type": "custom",
        "labels": [
```

"营销文案`",` "职场效率" `],`

```json
        "operateControl": null
      }
```

`],`

```json
    "pageSize": 10,
    "current": 1,
    "totalPages": 1
  },
  "errorCode": null,
  "errorMsg": null,
  "extraData": null,
  "traceId": null,
  "env": null,
  "other": null,
  "firstErrorMessage": null,
  "failure": false
}
```

**文档补充说明**

智能体工厂 OpenTrek 发指南

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

##### 知识库管理

智能体工厂 OpenTrek 发指南

###### 知识库列表查询

**接口概述**

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/kortex/api/kb/list POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostKortexApiKbList

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Body | 是 | 1 | 当前请求页，该参数必填 |
| pageSize | Integ er | Body | 是 | 10 | 每页请求条数，该参数必填 |
| kbCode | Strin g | Body | 否 | qdqsajkhjn6x | 知识库唯一编码 |
| kbName | Strin g | Body | 否 | 测试图文知识库 | 知识库名称 |
| kbType | Integ er | Body | 否 | 100 | 知识库类型 |

**返回参数**

智能体工厂 OpenTrek 发指南

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | object | 返回数据 | {} |
| total | Integer | 查询到的知识库总数 | 1 |
| list | List | 查询到的知识库列表 |  |
| code | String | 知识库唯一编码 | qdqsajkhjn6x |
| name | String | 知识库名称 | 高柴测试图文知识库 |
| kbType | Integer | 知识库类型 | 100,"自定义知识库", 201,"文档知识库", 202,"Q知识库", 203,"图文知识库" |
| description | String | 知识库描述 | 高柴测试 |
| projectCode | String | 所属工作空间编码 | baseline |
| createTime | String | 创建时间 | 2025-07- 04T21:28:45.03314 |
| createUser | String | 创建者 | gaochai |
| pageSize | Integer | 每页大小 | 60 |
| current | Integer | 目前所在页数 | 1 |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式智能体工厂 OpenTrek 发指南

```json
{
    "success": true,
    "data": {
        "total": 1,
        "list": [
            {
                "id": 363,
                "code": "z7pn9wbtkpy0",
```

`"name": "`自定义知识库`",`

```json
                "kbType": 100,
```

`"description": "`测试自定义知识库创建`",`

```json
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
            }
```

`],`

```json
        "pageSize": 60,
        "current": 1
    },
    "errorCode": null,
    "errorMsg": null
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |

智能体工厂 OpenTrek 发指南

| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
|---|---|---|
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 共享知识库列表查询

查询共享知识库列表。

**前提条件**

获取当前工作空间被分享得到的知识库列表，支持根据知识库唯一编码、知识库名称或知识库类型进行筛选，支持分页参数。可以通过查看请求示例，单击curl 命令示例右侧的调试按钮验证业务接口调用效果。

**接口调用地址**

```
POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/kortex/api/kb/share/sharedlist POP_SDK[SysDomain]:pop-service.unimanager.svc.cluster.local POP_SDK[Action]:PostKortexApiKbShareSharedlist
```

**入参描述**

**Header传参**

智能体工厂 OpenTrek 发指南

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| Authorizatio n | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| x-sfm- workspacec ode | String | 是 | 目标工作空间 | your workspace code _ _ |
| Content- Type | String | 是 | Content- Type | application/json |

**Body传参**

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| pageIndex | Integer | 是 | 当前请求页。 | 1 |
| pageSize | Integer | 是 | 每页请求条数。 | 60 |
| kbCode | String | 否 | 知识库唯一编码。 | qdqsajkhjn6x |
| kbName | String | 否 | 知识库名称。 | 测试图文知识库。 |
| kbType | Integer | 否 | 知识库类型。 | 100,"自定义知识库"。 201,"文档知识库"。 202,"BI知识库"。 203,"图文知识库"。 |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功。 | true |
| data | object | 返回数据。 | {} |
| -total | Integer | 查询到的共享知识库总数。 | 1 |

智能体工厂 OpenTrek 发指南

| -list | List<Object> | 查询到的共享知识库列表。 | - |
|---|---|---|---|
| --kbCode | String | 知识库唯一编码。 | qdqsajkhjn6x |
| --kbName | String | 知识库名称。 | 测试图文知识库 |
| --kbType | Integer | 知识库类型。 | 203 |
| -- kbDescription | String | 知识库描述。 | 测试 |
| -- sourceWsCode | String | 来源工作空间编码。 | baseline |
| -- targetWsCode | String | 目标工作空间编码。 | workspace-a |
| -- targetWsNam e | String | 目标工作空间名称。 | 测试工作空间 |
| --disableFlag | Integer | 是否停用。 | 0 |
| -- sourceCreateU ser | String | 知识库创建者。 | gaochai |
| -- sourceCreateT ime | String | 知识库创建时间。 | 2025-07-04T21:28:45.03314 |
| --createTime | String | 共享创建时间。 | 2025-07-22T22:59:48.073965 |
| --createUser | String | 共享创建者。 | admin |
| -pageSize | Integer | 每页大小。 | 60 |
| -current | Integer | 目前所在页数。 | 1 |
| errorCode | String | 错误码。 | 400 |

智能体工厂 OpenTrek 发指南

| errorMsg | String | 错误描述。 | error |
|---|---|---|---|

**请求示例**

**JAR包依赖**

```xml
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-core</artifactId>
            <version>4.6.4</version>
        </dependency>
```

**调用示例**

智能体工厂 OpenTrek 发指南

```java
    public static void main(String[] args) {
        DefaultProfile profile = DefaultProfile.getProfile(
                "${region}",
                "${ak}",
                "${sk}");
        //HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        //clientConfig.setReadTimeoutMillis(100 * 1000);
        //clientConfig.setIgnoreSSLCerts(true);
        //profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        CommonRequest request = new CommonRequest();
        request.setSysAccept(FormatType.JSON);
        request.setHttpContentType(FormatType.JSON);
        request.setSysMethod(${api_method});
        request.setSysDomain("pop-service.unimanager.svc.cluster.local");
        request.setSysVersion("2025-11-10");
        request.setSysUriPattern("/gatectl/kortex/api/kb/share/sharedlist");
        //request.setSysProtocol(ProtocolType.HTTPS);
        // Header
        request.putHeadParameter("x-acs-popcode", "sfm");
        request.putHeadParameter("x-sfm-workspacecode","${x-sfm-workspacecode}");
        request.putHeadParameter("Content-Type","application/json");
        // Query
        request.putQueryParameter("test1", "query");
        // Path
        request.putPathParameter("test2", "path");
        // Body
        request.putBodyParameter("current",1);
        try {
            CommonResponse response = client.getCommonResponse(request);
            System.out.println(response.getData());
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
```

**响应示例**

**返回数据**

智能体工厂 OpenTrek 发指南

```json
{"success":true,"data":{"total":1,"list": [{"id":1,"kbCode":"z7pn9wbtkpy0","sourceWsCode":"source_workspace","targetWsCode":"baseli
```

`","targetWsName":"`默认工作空间`","kbName":"`自定义知识库`","kbDescription":"`测试自定义知识库共享"

```
,"kbType":100,"state":null,"disableFlag":0,"sourceCreateUserId":"gaochai","sourceCreateUs ":"gaochai","sourceCreateTime":"2025-07- 22T22:59:48.073965","createUserId":"gaochai","createUser":"gaochai","createTime":"2025- 07-23T10:00:00","updateUserId":"gaochai","updateUser":"gaochai","updateTime":"2025-07-2 3T10:00:00"}],"pageSize":10,"current":1},"errorCode":null,"errorMsg":null}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失。 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败，无效 APP KEY。 _ |
| 401 | GATEWAY APP KEY ALREADY EXPI _ RED! | 鉴权失败，APP KEY 已过期。 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败，当前 APP KEY 归属用户对应的角色 _ 不匹配。 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败，当前 APP KEY 归属用户对应的角色 _ 已过期。 |
| 403 | GATEWAY APP PATH NOT FOUND! _ | 无效的服务调用路径。 |
| 403 | GATEWAY APP PATH NOT REGISTE _ R! | 当前服务调用路径未注册。 |
| 429 | GATEWAY LIMIT ! | 服务触发限流，请稍后再试。 |
| 429 | GATEWAY LIMIT CURRENT CALL TY PE ! | 服务触发限流，请稍后再试. |
| 403 | GATEWAY HEADER PARAMETER MI SSING! | 业务所需必填参数缺失。 |
| 403 | GATEWAY PARAMETER WORKSPAC E NO MATCH! | 传递的工作空间编码与APP KEY归属用户关联 _ 的工作空间编码不匹配。 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败，不支持的鉴权方式。 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY AUTH USER NOT MATCH _ WRONG! | 鉴权失败，AK用户信息不匹配。 |
|---|---|---|
| 401 | GATEWAY AUTH USER ROLE WRO _ _ NG! | 鉴权失败，用户角色不匹配。 |

###### 知识库创建

**接口概述**

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/kortex/api/kb/create POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostKortexApiKbCreate

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| name | String | 是 | 知识库名称 | 测试 |
| description | String | 是 | 知识库描述 | 测试 |
| kbType | Integer | 是 | 知识库类型 | 100,"自定义知识库", 201,"文档知识库", 202,"Q知识库", 203,"图文知识库" |
| kbProperties | Object | 是 | 这6属性任何知识类类型,都必须的值需类型, 且没定知识库类型填) |  |
| processStrategy | Object | 是 | 文档知识库(属性非组能看) |  |

智能体工厂 OpenTrek 发指南

| chunkStrategyMe thod | String | 是 | 分段策略, 默认传递 default | default |
|---|---|---|---|---|
| processStrategy Method | String | 是 | 解析策略方式 (simple 基础解析只提取文档中文字), deep 深度解析增加图片、表格、公式等解析能力) | deep |
| processDeepConf igs | List | 是 | 解析策略方式 (simple 基础解析只提取文档中文字), deep 深度解析增加图片、表格、公式等解析能力) |  |
| key | String | 是 | 深度解析可开启解析能量类型 image ocr图片 _ OCR, table parse _ 表格解析, equation parse公 _ 式解析, if figure enhance _ _ 图片增强 |  |
| enable | String | 是 | 是否开启 | true |
| textModel | Object | 是 | 文档知识库(文本向量化模型)· 模型服务参数可以通过在平台手续描述,通用知识库详情接口详询知识,根据校级服务特性,组织后需以表格形式使的用,搜成号登必要的空间, 且一但确认步的可能影响生成,无法更改 |  |
| modelType | String | 是 | 模型类型,该该值暂特值是"EMBEDDING" 定型的模型类型 |  |
| invokeUrl | String | 是 | 模型调用的服务地址 |  |
| path | String | 是 | 模型调用的请求地址 |  |

智能体工厂 OpenTrek 发指南

| modelConfigMod e | String | 是 | 模型配置类型,可填入代传是 normal | normal |
|---|---|---|---|---|
| modelSource | String | 是 | 模型来源,可填入代传是 system | system |
| modelCode | String | 是 | 模型编码 |  |
| modelName | String | 是 | 模型名称 |  |
| visualProcess | Boolean | 是 | 图文知识库(是否开启智能解析) |  |
| visualProcessMod el | Object | 是 | 图文知识库(包含5 项格模型)·该模型上送 textModel, 必须填该 modelType=vlm 的模型配置; 模型服务参数可以通过在平台手续描述,通用知识库详情接口详询知识,根据校级服务特性,组织后需以表格形式的用,搜成号登必要的空间 |  |
| visualDescPromp t | String | 是 | 图文知识库(包含5 项格Prompt,用于还可有提述描述内容) | 请用简短的语言描述这图,不要带入情感和复数。 |
| visualIndexModel | Object | 是 | 图文知识库(包含5 项格化模型)·该模型上送 textModel, 必须填该 modelType=IM E _ MBEDDING 的模型配置; 模型服务参数可以通过在平台手续描述,通用知识库详情接口详询知识, 根据校级服务特性, 组织后需以表格形式使的用,搜成号登必要的空间,且一但确认步的可能影响生成,无法更改 |  |
| indexKTrigger | String | 是 | 图文知识库(图像化触发,默认传递 upload) | upload |

智能体工厂 OpenTrek 发指南

| kbSubmodels | List | 是 | 自定文知识库必传包括模型定义 |  |
|---|---|---|---|---|
| kbSubmodelNam e | Boolean | 是 | 自定文标准知识类名称 |  |
| kbSubmodelField s | List | 是 | 自定文标准知识类自定的属性项信息 |  |
| fieldName | String | 是 | 字段名称, 数据库字段全包含此, 配置接黔占位该租用 | matter name _ |
| fieldComment | String | 是 | 字段释义 | 事项名称 |
| fieldType | String | 是 | 字段类型 varchar(varchar _ 64 | varchar 256 _ |
| kbIndexes | List | 是 | 自定文标准知识类自定的索引项信息 |  |
| kbIndexEngineTy pe | String | 是 | 索引类型 builtin vector图像 _ 索引引擎, builtin es 定文索 _ 引引擎 | builtin vector _ |
| kbIndexName | String | 是 | 索引定文名称 | 事项名称配类 |
| kbIndexFields | List | 是 | 索引字段定义 |  |
| fieldName | String | 是 | 字段名称, 数据库字段全包含此, 配置接黔占位该租用 | matter name _ |
| fieldComment | String | 是 | 字段释义 | 事项名称 |
| fieldType | String | 是 | 字段类型 varchar(varchar _ 64 | varchar 256 _ |
| fieldIndexType | String | 是 | 字段索引类型 resource用于召回, retrieval用于检索 | resource |

智能体工厂 OpenTrek 发指南

| kbIndexPropertie s | Object | 是 | 文本向量化模型链接键 |  |
|---|---|---|---|---|
| model | Object | 是 | 文本向量化模型配置·结构同上述 textModel, 必须填该 modelType=EMB EDDING 的模型配置 |  |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | object | 返回数据 | {} |
| stats | Object | 创建详情 |  |
| kbCode | String | 知识库唯一编码 | y4fu5k9w5yI2 |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式

```json
{
    "success": true,
    "data": {
        "stats": {
            "metaAffects": {
                "kbIndex": {
                    "deletes": 0,
                    "inserts": 1
                },
                "kb": {
                    "inserts": 1
                },
                "kbSubmodelField": {
                    "deletes": 0,
                    "inserts": 2
                },
"kbSubmodel":{
```

智能体工厂 OpenTrek 发指南

```json
                kbSubmodel: {
                    "deletes": 0,
                    "inserts": 1
                },
                "kbIndexField": {
                    "deletes": 0,
                    "inserts": 2
                }
            },
            "ddlStats_smod": {
                "deletes": {
                },
                "fieldInserts": {
                },
                "inserts": {
                    "z7pn9wbtkpy0x6l8": {
                        "kbSubmodelEntity": {
                            "id": 458,
                            "kbCode": "z7pn9wbtkpy0",
                            "kbSubmodelCode": "z7pn9wbtkpy0x6l8",
```

`"kbSubmodelName": "`标准知识库`",`

```json
                            "projectCode": "17ac7ce4-23ad-413b-95f4-55732b15a4b7",
                            "createTime": "2025-07-22T22:59:48.086900569",
                            "createUser": "gaochai",
                            "updateTime": "2025-07-22T22:59:48.086903719",
                            "updateUser": "gaochai"
                        },
                        "kbSubmodelFieldEntities": [
                            {
                                "id": 3041,
                                "kbCode": "z7pn9wbtkpy0",
                                "kbSubmodelCode": "z7pn9wbtkpy0x6l8",
                                "fieldName": "matter_code",
                                "fieldType": "varchar_256",
```

`"fieldComment": "`事项编码`",`

```json
                                "fieldDefaultValue": null,
                                "fieldIndexExt": null,
                                "projectCode": "17ac7ce4-23ad-413b-95f4-55732b15a4b7",
                                "createTime": "2025-07-22T22:59:48.099405932",
                                "createUser": "gaochai",
                                "updateTime": "2025-07-22T22:59:48.099409152",
                                "updateUser": "gaochai"
                            },
                            {
                                "id": 3042,
                                "kbCode": "z7pn9wbtkpy0",
                                "kbSubmodelCode": "z7pn9wbtkpy0x6l8",
                                "fieldName": "matter_name",
                                "fieldType": "varchar_256",
```

`"fieldComment": "`事项名称`",`

```json
                                "fieldDefaultValue": null,
                                "fieldIndexExt": null,
                                "projectCode": "17ac7ce4-23ad-413b-95f4-55732b15a4b7",
```

智能体工厂 OpenTrek 发指南 p j ,

```json
                                "createTime": "2025-07-22T22:59:48.099419083",
                                "createUser": "gaochai",
                                "updateTime": "2025-07-22T22:59:48.099420433",
                                "updateUser": "gaochai"
                            }
```

]

```json
                    }
                }
            },
            "ddlStats_kbidx": {
                "deletes": {
                },
                "fieldInserts": {
                },
                "inserts": {
                    "z7pn9wbtkpy0w83n": {
                        "kbIndexEntity": {
                            "id": 721,
                            "kbCode": "z7pn9wbtkpy0",
                            "kbSubmodelCode": "z7pn9wbtkpy0x6l8",
                            "kbIndexCode": "z7pn9wbtkpy0w83n",
```

`"kbIndexName": "`事项名称匹配`",`

```json
                            "kbIndexEngineType": "builtin_vector",
                            "kbIndexProperties": "
{\"indexType\":\"vector\",\"dimensionSize\":1536,\"model\": {\"modelConfigMode\":\"normal\",\"modelCode\":\"rsv-e9modnqp\",\"modelName\":\"新版文本向量\",\"abilities\":[],\"modelExtParams\": [],\"modelType\":\"EMBEDDING\",\"modelSource\":\"system\",\"source\":\"system\",\"customM elMappings\":[],\"invokeUrl\":\"http://ai-gateway-svc:8090/v1/router/call/rsv-e9modnqp\ ",\"path\":\"/api/batch_predict_embeddings\"}}",
                            "projectCode": "17ac7ce4-23ad-413b-95f4-55732b15a4b7",
                            "createTime": "2025-07-22T22:59:48.11207465",
                            "createUser": "gaochai",
                            "updateTime": "2025-07-22T22:59:48.11207763",
                            "updateUser": "gaochai"
                        },
                        "kbIndexFieldEntities": [
                            {
                                "id": 2305,
                                "kbCode": "z7pn9wbtkpy0",
                                "kbSubmodelCode": "z7pn9wbtkpy0x6l8",
                                "kbIndexCode": "z7pn9wbtkpy0w83n",
                                "fieldName": "matter_code",
                                "fieldType": null,
                                "fieldIndexType": "resource",
                                "fieldIndexDefinition": "
{\"indexType\":\"vector\",\"dimensionSize\":1536,\"model\": {\"modelConfigMode\":\"normal\",\"modelCode\":\"rsv-e9modnqp\",\"modelName\":\"新版文本向量\",\"abilities\":[],\"modelExtParams\": [],\"modelType\":\"EMBEDDING\",\"modelSource\":\"system\",\"source\":\"system\",\"customM elMappings\":[],\"invokeUrl\":\"http://ai-gateway-svc:8090/v1/router/call/rsv-e9modnqp\ ",\"path\":\"/api/batch_predict_embeddings\"}}",
```

智能体工厂 OpenTrek 发指南

```json
                                "projectCode": "17ac7ce4-23ad-413b-95f4-55732b15a4b7",
                                "createTime": "2025-07-22T22:59:48.124616445",
                                "createUser": "gaochai",
                                "updateTime": "2025-07-22T22:59:48.124620155",
                                "updateUser": "gaochai"
                            },
                            {
                                "id": 2306,
                                "kbCode": "z7pn9wbtkpy0",
                                "kbSubmodelCode": "z7pn9wbtkpy0x6l8",
                                "kbIndexCode": "z7pn9wbtkpy0w83n",
                                "fieldName": "matter_name",
                                "fieldType": null,
                                "fieldIndexType": "retrieve",
                                "fieldIndexDefinition": "
{\"indexType\":\"vector\",\"dimensionSize\":1536,\"vectorFieldName\":\"sys_emb_matter_nam ",\"model\":{\"modelConfigMode\":\"normal\",\"modelCode\":\"rsve9modnqp\",\"modelName\":\"新版文本向量\",\"abilities\":[],\"modelExtParams\":[],\"modelT ype\":\"EMBEDDING\",\"modelSource\":\"system\",\"source\":\"system\",\"customModelMapping ":[],\"invokeUrl\":\"http://ai-gateway-svc:8090/v1/router/call/rsve9modnqp\",\"path\":\"/api/batch_predict_embeddings\"}}",
                                "projectCode": "17ac7ce4-23ad-413b-95f4-55732b15a4b7",
                                "createTime": "2025-07-22T22:59:48.124630415",
                                "createUser": "gaochai",
                                "updateTime": "2025-07-22T22:59:48.124631745",
                                "updateUser": "gaochai"
                            }
```

]

```json
                    }
                }
            }
        },
        "kbCode": "z7pn9wbtkpy0"
    },
    "errorCode": null,
    "errorMsg": null
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
|---|---|---|
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 知识库启用

**接口概述**

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/kortex/api/kb/enable POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostKortexApiKbEnable 智能体工厂 OpenTrek 发指南

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| code | Strin g | Body | 是 | rkiviej5rkm2 | 知识库唯一编码，该参数必填 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | object | 返回数据 | {} |
| kbEnable | Integer | 是否成功启用 | 0 |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式

```json
{
    "success": true,
    "data": {
        "kbEnable": 1
    },
    "errorCode": null,
    "errorMsg": null
}
```

智能体工厂 OpenTrek 发指南

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

智能体工厂 OpenTrek 发指南

###### 知识库删除

**接口概述**

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/kortex/api/kb/delete POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostKortexApiKbDelete

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| code | Strin g | Body | 是 | rkiviej5rkm2 | 知识库唯一编码，该参数必填 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | object | 返回数据 | {} |
| kb | Object | (自定义旧)知识库维度统计 |  |
| deletes | Integer | 删除数量 | 1 |

智能体工厂 OpenTrek 发指南

| kbSubmodel | Object | (自定义旧)知识库数据模型维度统计 |  |
|---|---|---|---|
| deletes | Integer | 删除数量 | 1 |
| kbSubmodelField | Object | (自定义旧)知识库数据模型字段维度统计 |  |
| deletes | Integer | 删除数量 | 1 |
| kbIndex | Object | (自定义旧)知识库索引维度统计 |  |
| deletes | Integer | 删除数量 | 1 |
| kbIndexField | Object | (自定义旧)知识库索引字段维度统计 |  |
| deletes | Integer | 删除数量 | 1 |
| monoDeletes | Object | (文档知识库 | 图文知识库)删除操作统计对象 |
| kb | Object | 知识库 |  |
| deletes | Integer | 删除数量 | 1 |
| kbSubmodel | Object | 知识库数据模型 |  |
| deletes | Integer | 删除数量 | 1 |
| kbSubmodelField | Object | 知识库数据模型字段 |  |
| deletes | Integer | 删除数量 | 1 |
| kbIndex | Object | 知识库索引 |  |
| deletes | Integer | 删除数量 | 1 |
| kbIndexField | Object | 知识库索引字段 |  |

智能体工厂 OpenTrek 发指南

| deletes | Integer | 删除数量 | 1 |
|---|---|---|---|
| kbdocFileDeletes | Integer | (文档知识库)删除的文件总数 | 0 |
| kbVisualFileDeletes | Integer | (图文知识库)删除的图片总数 | 0 |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式

```json
{
    "success": true,
    "data": {
        "monoDeletes": {
            "kbIndex": {
                "deletes": 2
            },
            "kb": {
                "deletes": 1
            },
            "kbSubmodelField": {
                "deletes": 9
            },
            "kbSubmodel": {
                "deletes": 1
            },
            "kbIndexField": {
                "deletes": 6
            }
        },
        "kbdocFileDeletes": 0
    },
    "errorCode": null,
    "errorMsg": null
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
|---|---|---|
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 知识库停用

**接口概述**

**接口调用地址**

智能体工厂 OpenTrek 发指南 POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/kortex/api/kb/disable POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostKortexApiKbDisable

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| code | Strin g | Body | 是 | rkiviej5rkm2 | 知识库唯一编码，该参数必填 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | object | 返回数据 | {} |
| kbDisable | Integer | 是否成功停用 | 1 |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式智能体工厂 OpenTrek 发指南

```json
{
    "success": true,
    "data": {
        "kbDisable": 1
    },
    "errorCode": null,
    "errorMsg": null
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |

| 智能体工厂 OpenTrek |  | Agent Dev 开发指南·Agent Dev开发指南 |
|---|---|---|

| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
|---|---|---|
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 知识库详情查询

**接口概述**

获取知识库的数据模型定义等详情数据

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/kortex/api/kb/mono/detail POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostKortexApiKbMonoDetail

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| code | Strin g | Body | 是 | rkiviej5rkm2 | 知识库唯一编码，该参数必填 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|

智能体工厂 OpenTrek 发指南

| success | Boolean | 是否成功 | true |
|---|---|---|---|
| data | object | 返回数据 | {} |
| code | String | 知识库唯一编码 | tzf5wnyvkfdg |
| name | String | 知识库名称 | 央久验证 |
| description | String | 知识库描述 | 年报文档 |
| kbType | Integer | 知识库类型 | 100,"自定义知识库", 201,"文档知识库", 202,"BI知识库", 203,"图文知识库" |
| kbProperties | Object | 知识库扩展属性, 见知识库创建接口相关同名字段释义 |  |
| kbSubmodels | List | 知识库数据模型, 见知识库创建接口相关同名字段释义 |  |
| kbSubmodelName | String | 自定义标准知识库名称 |  |
| kbSubmodelCode | String | 自定义标准知识库数据模型唯一编码 |  |
| kbSubmodelFields | List | 自定义标准知识库包含的属性信息 |  |
| fieldName | String | 字段名称, 数据库字段命名语法, 驼峰场景以下划线衔接 | matter name _ |
| fieldComment | String | 字段释义 | 事项名称 |
| fieldType | String | 字段类型 varchar\|varchar 64\|va _ rchar 256\|varchar 102 _ _ 4\|integer | varchar 1024 _ |
| fieldIndexExt | String | 索引相关扩展描述 | filter |

智能体工厂 OpenTrek 发指南

| kbSubmodelCode | String | 归属数据模型编码 |  |
|---|---|---|---|
| kbCode | String | 归属知识库编码 |  |
| kbIndexes | List | 自定义标准知识库包含的索引信息 |  |
| kbIndexCode | String | 索引存储唯一编码 |  |
| kbSubmodelCode | String | 归属数据模型编码 |  |
| kbCode | String | 归属知识库编码 |  |
| kbIndexEngineType | String | 索引类型 builtin vector: _ 向量索引引擎; builtin es:全文索引引擎 _ | builtin vector _ |
| kbIndexName | String | 索引定义名称 | 事项名称匹配 |
| kbIndexFields | List | 索引字段定义 |  |
| fieldName | String | 字段名称, 数据库字段命名语法, 驼峰场景以下划线衔接 | matter name _ |
| fieldIndexType | String | 字段索引类型 resource 用于召回; retrieve用于检索 | resource |
| kbIndexProperties | Object | 文本向量化模型数据封装 |  |
| model | Object | 文本向量化模型配置, 结构同上述 textModel, 必须选择 modelType=EMBEDDI NG 的模型配置 |  |
| indexType | String | 索引类型 vector\|es | vector |
| refRes | String | 知识库引用资源 |  |
| disableFlag | Integer | 是否启用 | 1 |

智能体工厂 OpenTrek 发指南

| createTime | String | 创建时间 | 2025-07- 16T15:00:24.192928 |
|---|---|---|---|
| createUser | String | 知识库创建者 | dke |

**示例**

`JSON` 格式

```json
{
    "success": true,
    "data": {
        "code": "z7pn9wbtkpy0",
```

`"name": "`自定义知识库`",` `"description": "`测试自定义知识库创建`",`

```json
        "kbType": 100,
        "kbProperties": null,
        "kbSubmodels": [
            {
                "kbSubmodelCode": "z7pn9wbtkpy0x6l8",
```

`"kbSubmodelName": "`标准知识库`",`

```json
                "kbSubmodelFields": [
                    {
                        "kbCode": "z7pn9wbtkpy0",
                        "kbSubmodelCode": "z7pn9wbtkpy0x6l8",
                        "fieldName": "matter_code",
                        "fieldType": "varchar_256",
```

`"fieldComment": "`事项编码`",`

```json
                        "fieldDefaultValue": null,
                        "fieldIndexExt": null
                    },
                    {
                        "kbCode": "z7pn9wbtkpy0",
                        "kbSubmodelCode": "z7pn9wbtkpy0x6l8",
                        "fieldName": "matter_name",
                        "fieldType": "varchar_256",
```

`"fieldComment": "`事项名称`",`

```json
                        "fieldDefaultValue": null,
                        "fieldIndexExt": null
                    }
```

`],`

```json
                "kbIndexes": [
                    {
                        "kbCode": "z7pn9wbtkpy0",
                        "kbSubmodelCode": "z7pn9wbtkpy0x6l8",
                        "kbIndexCode": "z7pn9wbtkpy0w83n",
```

`"kbIndexName": "`事项名称匹配`",`

```json
                        "kbIndexEngineType": "builtin_vector",
                        "kbIndexProperties": {
                            "indexType": "vector",
                            "dimensionSize": 1536,
                            "model": {
"abilities":[
```

智能体工厂 OpenTrek 发指南

```
                                abilities: [
```

`],` `"modelName": "`新版文本向量`",`

```json
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
                                "invokeUrl": "http://ai-gateway-
svc:8090/v1/router/call/rsv-e9modnqp",
                                "modelConfigMode": "normal",
                                "modelType": "EMBEDDING",
                                "source": "system"
                            }
                        },
                        "kbIndexFields": [
                            {
                                "fieldName": "matter_code",
                                "fieldIndexType": "resource"
                            },
                            {
                                "fieldName": "matter_name",
                                "fieldIndexType": "retrieve"
                            }
```

]

```
                    }
```

]

```
            }
```

`],`

```json
        "refRes": null,
        "disableFlag": 0,
        "createTime": "2025-07-22T22:59:48.073965",
        "updateTime": "2025-07-22T22:59:48.073969",
        "createUser": "gaochai"
    },
    "errorCode": null,
    "errorMsg": null
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
|---|---|---|
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 文档知识库文件列表查询

**接口概述**

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/kortex/api/kb/doc/file/list 智能体工厂 OpenTrek 发指南 POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostKortexApiKbDocFileList

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| current | Integ er | Body | 是 | 1 | 当前页码，该参数必填 |
| pageSize | Integ er | Body | 是 | 10 | 每页大小，该参数必填 |
| kbCode | Strin g | Body | 是 | h8qp21tb85pf | 知识库唯一编码，该参数必填 |
| fileCode | Strin g | Body | 否 | 1866347c49824f62ab061 576b8891806 | 文件代码 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | object | 返回数据 | {} |
| total | Integer | 查询到的文档总数 | 1 |
| list | List | 查询到的文档列表 |  |
| kbCode | String | 知识库code | h8qp21tb85pf |

智能体工厂 OpenTrek 发指南

| fileCode | String | 文档code | 1866347c49824f62ab 061576b8891806 |
|---|---|---|---|
| fileOriginalName | String | 文档原名 | 【情报附件】101330100230176 -漏洞验证.docx |
| filePath | String | 文档路径 | apsara/kortex/kb/doc/fi le/aopf27k2rZieth5u7c e8fhTN2p6j1DRn/【情报附件】101330100230176 -漏洞验证.docx |
| fileType | String | 文档类型 | docx |
| fileSize | String | 文档大小 |  |
| fileChecksum | String | fileChecksum |  |
| ownerId | String | 拥有者id | 48381f1dbff84ad8906 05177585ea7ff |
| fileOutputChunkPath | String | 文档解析出的chunk的路径 | kortex/kb/doc/file/186 6347c49824f62ab061 576b8891806/output/c hunk/chunk.jsonl |
| state | Integer | 状态 103 待转存;102 转存失败;0 待调度\|转存成功;100 进行中;200 成功;500 失败 | 200 |
| uploadType | Integer | 上传类型 1 - 手动上传, 2 - API上传 | API |
| refRes | String | 关联资源 |  |
| metadata | String | 元数据 |  |
| projectCode | String | 所属工作空间编码 | baseline |
| createTime | String | 创建时间 | 2025-07- 09T19:28:46.289265 |

智能体工厂 OpenTrek 发指南

| createUser | String | 创建者 | dke |
|---|---|---|---|
| pageSize | Integer | 每页大小 | 60 |
| current | Integer | 目前所在页数 | 1 |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式智能体工厂 OpenTrek 发指南

```json
{
    "success": true,
    "data": {
        "total": 1,
        "list": [
            {
                "kbCode": "kk062kg1t4hd",
                "fileCode": "7a3f64a3f22a4f12b2fe2557d3139595",
                "fileOriginalUrl": "https://ibp-deliver.oss-cn-
hangzhou.aliyuncs.com/%E3%80%8A%E6%88%91%E6%9B%BE%E8%B5%B0%E5%9C%A8%E5%B4%A9%E6%BA%83%E7% %84%E8%BE%B9%E7%BC%98%E3%80%8B_full.pdf",
```

`"fileOriginalName": "`《我曾走在崩溃的边缘》`_full.pdf",`

```json
                "filePath":
"kortex/kb/doc/file/kk062kg1t4hd/7a3f64a3f22a4f12b2fe2557d3139595/《我曾走在崩溃的边缘》_fu ll.pdf",
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
            }
```

`],`

```json
        "pageSize": 10,
        "current": 1
    },
    "errorCode": null,
    "errorMsg": null
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
|---|---|---|
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 知识库文件上传

**接口概述**

针对文档知识库和图文知识库可以通过该接口实现知识库源文件的写入

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/kortex/api/kb/file/data/sync 智能体工厂 OpenTrek 发指南 POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostKortexApiKbFileDataSync

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| kbCode | Strin g | Body | 是 | cozhklqn3omz | 知识库唯一编码，该参数必填 |
| kbType | Integ er | Body | 是 | 201 | 知识库类型，该参数必填 |
| referer | Strin g | Body | 否 | https://example.com | 文件地址存在防盗链场景可以传递应用来源验证 |
| fileInfo | Repe atLis t | Body | 是 | [] | 批量数据投递，该参数必填 |
| - fileOriginal Url | Strin g | Body | 否 | https://****/tmp/pic/8f1af 9cbaa9d9aee17a0c0bd94 4ef662.jpeg | 原始文件全路径URL地址; 平台支持白名单限制能力,受限地址访问会反馈响应"The current file address has been rejected"，该参数必填 |
| - fileOriginal Name | Strin g | Body | 否 | 风景.jpeg | 文件名称, 默认截取最后一个/ 之后的文本 |
| - fileOuterC ode | Strin g | Body | 否 | 111111111 | 文件外部唯一标识符,建议传递,用于返回内部fileCode映射以及预处理异常信息 |

智能体工厂 OpenTrek 发指南

| - fileOriginal Content | Strin g | Body | 否 | 风景 | 文件描述(图文知识库场景可传) |
|---|---|---|---|---|---|

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | object | 返回数据 | {} |
| insert | Integer | 异步待转存数量 | 0 |
| update | Integer | 更新数量 | 0 |
| insertMap | JSONObject | 文件编码映射, key: fileOuterCode, value: fileCode | {} |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式

```json
{
    "success": true,
    "data": {
        "insert": 1
    },
    "errorCode": null,
    "errorMsg": null,
    "traceId": null,
    "env": null,
    "ext": null
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
|---|---|---|
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 文档知识库删除文件

**接口概述**

智能体工厂 OpenTrek 发指南

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/kortex/api/kb/doc/file/delete POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostKortexApiKbDocFileDelete

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| kbCode | Strin g | Body | 是 | kk062kg1t4hd | 知识库唯一编码，该参数必填 |
| fileCode | Strin g | Body | 否 | 3fedc04432424c9886b1b bb69666b7ed | 文档代码（单个删除时使用， 与fileCodes二选一） |
| fileCodes | Repe atLis t | Body | 否 | ["3fedc04432424c9886b1 bbb69666b7ed", "394e8fa103844b3c96d6 810ae5bc6bed"] | 文档代码列表（批量删除时使用，与fileCode二选一） |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | object | 返回数据 | {} |
| affected | Integer | 受影响的数量 | 1 |

智能体工厂 OpenTrek 发指南

| errorCode | String | 错误码 | true |
|---|---|---|---|
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式

```json
{
    "success": true,
    "data": {
        "affected": 1
    },
    "errorCode": null,
    "errorMsg": null
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |

智能体工厂 OpenTrek 发指南

| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
|---|---|---|
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 文件重新解析

**接口概述**

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/kortex/api/kb/doc/file/reprocess POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostKortexApiKbDocFileReprocess

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

智能体工厂 OpenTrek 发指南

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| kbCode | Strin g | Body | 是 | kk062kg1t4hd | 知识库唯一编码，该参数必填 |
| fileCode | Strin g | Body | 否 | 3fedc04432424c9886b1b bb69666b7ed | 文件编码 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | object | 返回数据 | {} |
| updated | Integer | 受影响的数量 | 1 |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式

```json
{
    "success": true,
    "data": {
        "updated": 1
    },
    "errorCode": null,
    "errorMsg": null
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
|---|---|---|
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 文档知识库chunk明细列表查询

**接口概述**

**前提条件（查看APP_KEY）**

查询文档知识库中的chunk明细。可以通过查看请求示例，点击 curl 命令示例右侧的调试按钮验证业务接口调用效果。

**接口调用地址**

智能体工厂 OpenTrek 发指南 POST http://{host}/gatectl/kortex/api/kb/doc/chunk/list

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- authorizati on | Strin g | Hea der | 否 | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Body | 是 | 1 | 当前页码，该参数必填 |
| pageSize | Integ er | Body | 是 | 10 | 每页大小，该参数必填 |
| kbCode | Strin g | Body | 是 | h8qp21tb85pf | 知识库唯一编码，该参数必填 |
| keyword | Strin g | Body | 是 | 1 | 关键字查询，该参数必填 |
| code | Strin g | Body | 是 | 1 | 分段唯一编码，该参数必填 |
| fileCode | Strin g | Body | 是 | 1c1363763d8a44e1a4bf2 7b516f269c9 | 文件编码，该参数必填 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |

智能体工厂 OpenTrek 发指南

| data | object | 返回数据 | {} |
|---|---|---|---|
| total | Integer | 查询到的列表总数 | 39 |
| list | List | 查询到的列表 |  |
| file code _ | String | 文件code | 139ace527fad49d1b6 0642d927cf0734 |
| file name _ | String | 文档名 | 汇丰香港使用指南 2022.5(1).pdf |
| file path _ | String | 文档路径 | apsara/kortex/kb/doc/fi le/frflNcOUgYp21rtbw3 vsaXobOlFspojA/汇丰香港使用指南 2022.5(1).pdf |
| create user _ | String | 创建者 | gaochai |
| sys data id _ _ | String | 数据唯一id | 180eeed6-58a1-43da- 980a-21d50e65615e |
| sys create time _ _ | String | 创建时间 | 2025-07- 11T20:08:40.140449 |
| chunk upload type _ _ | Integer | 上传类型 | 1 |
| chunk content _ | String | chunk内容 - 召回后送入 LLM的prompt文本 |  |
| chunk representation _ | String | chunk内容 - 用于向量化的文本, 在retrieve阶段使用 |  |
| show content _ | String | chunk内容 - 带有bbox和 objects占位符的文本形式 |  |
| chunk bboxes _ | List | bbox坐标信息 |  |
| text bbox _ | List | 坐标 | [ 0.3115, 0.0683, 0.0285, 0.372 ] |

智能体工厂 OpenTrek 发指南

| text type _ | String | 文本类型 | docTitle |
|---|---|---|---|
| text content _ | String | 文本内容 | 汇丰香港账户使用指南 |
| page | Integer | 页数 | 1 |
| objects | List | 对象信息 - 表格,图片等 |  |
| start page _ | Integer | chunk序号 | 1 |
| chunk sort number _ _ | Integer | 页码 | 0 |
| title | String | 标题 |  |
| chapter title _ | String | 章节标题 |  |
| pageSize | Integer | 每页大小 | 60 |
| current | Integer | 目前所在页数 | 1 |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式

```json
{
    "success": true,
    "data": {
        "total": 1,
        "list": [
            {
                "file_code": "7a3f64a3f22a4f12b2fe2557d3139595",
```

`"file_name": "`《我曾走在崩溃的边缘》`_full.pdf",`

```json
                "file_path":
"kortex/kb/doc/file/kk062kg1t4hd/7a3f64a3f22a4f12b2fe2557d3139595/《我曾走在崩溃的边缘》_fu ll.pdf",
                "create_user": "gaochai",
                "sys_data_id": "88b3affd-5b56-4819-9ebd-a12e8ce46db1",
                "sys_create_time": "2025-07-22T23:51:58.250412",
                "chunk_upload_type": 1,
```

`"chunk_content": "`我曾走在;崩溃的;边缘;柳传志;徐小平;王强;鼎力推荐;中信出版集团我曾走在崩溃的边缘——俞敏洪亲述新东方创业发展之路俞敏洪著中信出版集团`",` 智能体工厂 OpenTrek 发指南曾走在崩溃的边缘俞敏洪亲述新东方创业发展之路俞敏洪著中信出版集团, `"chunk_representation": "`我曾走在;崩溃的;边缘;柳传志;徐小平;王强;鼎力推荐;中信出版集团我曾走在崩溃的边缘——俞敏洪亲述新东方创业发展之路俞敏洪著中信出版集团`",` `"show_content": "{object_1_figure_0}`我曾走在崩溃的边缘——俞敏洪亲述新东方创业发展之路俞敏洪著中信出版集团`",`

```json
                "chunk_bboxs": [
                    {
                        "text_bbox": [
                            0.2206,
                            0.2898,
                            0.0909,
                            0.5547
```

`],`

```json
                        "text_type": "docTitle",
```

`"text_content": "`我曾走在崩溃的边缘——俞敏洪亲述新东方创业发展之路`",`

```json
                        "page": 2
                    },
                    {
                        "text_bbox": [
                            0.2819,
                            0.2923,
                            0.0372,
                            0.4387
```

`],`

```json
                        "text_type": "line",
```

`"text_content": "`我曾走在崩溃的边缘`",`

```json
                        "page": 2
                    },
                    {
                        "text_bbox": [
                            0.2247,
                            0.3542,
                            0.0259,
                            0.549
```

`],`

```json
                        "text_type": "line",
```

"text_content": "——俞敏洪亲述新东方创业发展之路`",`

```json
                        "page": 2
                    },
                    {
                        "text_bbox": [
                            0.4567,
                            0.404,
                            0.0158,
                            0.0858
```

`],`

```json
                        "text_type": "paraText",
```

`"text_content": "`俞敏洪著`",`

```json
                        "page": 2
                    },
                    {
                        "text_bbox": [
                            0.4592,
                            0.4059,
                            0.0139,
```

智能体工厂 OpenTrek 发指南

```
                            0.0817
```

`],`

```json
                        "text_type": "line",
```

`"text_content": "`俞敏洪著`",`

```json
                        "page": 2
                    },
                    {
                        "text_bbox": [
                            0.442,
                            0.5114,
                            0.0177,
                            0.1152
```

`],`

```json
                        "text_type": "paraText",
```

`"text_content": "`中信出版集团`",`

```json
                        "page": 2
                    },
                    {
                        "text_bbox": [
                            0.4453,
                            0.5133,
                            0.0152,
                            0.1095
```

`],`

```json
                        "text_type": "line",
```

`"text_content": "`中信出版集团`",`

```json
                        "page": 2
                    }
```

`],`

```json
                "objects": [
                    {
                        "object_id": "object_1_figure_0",
                        "object_type": "figure",
                        "object_sub_type": "other",
```

`"object_content": "`我曾走在;崩溃的;边缘;柳传志;徐小平;王强;鼎力推荐;中信出版集团`",`

```json
                        "object_caption": "",
                        "object_bbox": "[0.0335,0.0019,0.9924,0.9346]",
                        "object_representation": "",
                        "object_path":
"kortex/kb/doc/file/7a3f64a3f22a4f12b2fe2557d3139595/output/chunk/objects/0_0_figure.jpg"
                        "page": 1
                    }
```

`],`

```json
                "start_page": 1,
                "chunk_sort_number": 0,
                "title": null,
                "chapter_title": null
            }
```

`],`

```json
        "pageSize": 10,
        "current": 1
    },
```

智能体工厂 OpenTrek 发指南

```json
    "errorCode": null,
    "errorMsg": null
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |
|---|---|---|

###### 文档知识库chunk内容修正

**接口概述**

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/kortex/api/kb/doc/chunk/edit POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostKortexApiKbDocChunkEdit

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| kbCode | Strin g | Body | 是 | cozhklqn3omz | 知识库唯一编码，该参数必填 |
| data | Json | Body | 是 | {} | 需要变更的数据集，该参数必填 |
| - chunk con _ tent | Strin g | Body | 否 | 用户购买了一台笔记本电脑 | chunk内容，该参数必填 |
| - sys data i _ _ d | Strin g | Body | 否 | 1234 | 数据唯一ID,文档知识库场景为分段code，该参数必填 |

| 智能体工厂 Ope | nTrek |  |  | Age | nt Dev 开发指南·Agent Dev开发指南 |
|---|---|---|---|---|---|

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | object | 返回数据 | {} |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式

```json
{
    "success": true,
    "data": null,
    "errorCode": null,
    "errorMsg": null
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |

智能体工厂 OpenTrek 发指南

| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
|---|---|---|
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 知识库数据查询

**接口概述**

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/kortex/api/kb/submodel/data/list POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostKortexApiKbSubmodelDataList

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek 发指南

| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
|---|---|---|---|---|---|
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| kbSubmod elCode | Strin g | Body | 是 | tttbnz21diense89 | 知识库数据模型编码,见知识库详情返回，该参数必填 |
| kbCode | Strin g | Body | 是 | sadfak2s | 知识库编码，该参数必填 |
| current | Integ er | Body | 是 | 1 | 分页页数，该参数必填 |
| pageSize | Integ er | Body | 是 | 10 | 每页条数，该参数必填 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | object | 返回数据 | {} |
| total | Integer | 查询到的知识库总数 | 1 |
| list | List | 查询到的知识库列表 |  |
| sys data id _ _ | String | 数据唯一ID; | true |
| sys create time _ _ | String | 创建时间 | true |
| sys source ids _ _ | String | 数据附加信息 | true |

智能体工厂 OpenTrek 发指南

| **** | String | 自定义的数据字段;例如我创建了一个自定义知识库, 定义了一个‘标准知识库’, 包含两个字段 matter code,matter n _ _ ame; | 自定义的数据字段对应的值 |
|---|---|---|---|
| pageSize | Integer | 每页大小 | 60 |
| current | Integer | 目前所在页数 | 1 |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式智能体工厂 OpenTrek 发指南

```json
{
    "total": 3,
    "list": [
        {
```

`"matter_name": "`井盖缺损`1",`

```json
            "sys_source_ids": "{\"kb_submodel\": \"true\", \"kb_submodel.sys_data_id\":
\"b724ba0f-a836-4f5e-88d8-c90dda96e3e6\"}",
            "sys_data_id": "b724ba0f-a836-4f5e-88d8-c90dda96e3e6",
            "matter_code": "CODE0003",
            "sys_create_time": "2025-07-22T15:44:14.592+00:00"
        },
        {
```

`"matter_name": "`噪音扰民`",`

```json
            "sys_source_ids": "{\"kb_submodel\": \"true\", \"kb_submodel.sys_data_id\":
\"d42ba34b-553c-4d7f-adc6-ef81ce65255f\"}",
            "sys_data_id": "d42ba34b-553c-4d7f-adc6-ef81ce65255f",
            "matter_code": "CODE0003",
            "sys_create_time": "2025-07-22T15:43:05.304+00:00"
        },
        {
```

`"matter_name": "`私搭乱建`",`

```json
            "sys_source_ids": "{\"kb_submodel\": \"true\", \"source_builtin_smod\":
\"true\", \"kb_submodel.sys_data_id\": \"d3a2163b-68de-400f-a2b3-dd312247207d\", \"sour ce_builtin_smod.sys_id\": \"1\"}",
            "sys_data_id": "d3a2163b-68de-400f-a2b3-dd312247207d",
            "matter_code": "CODE0002",
            "sys_create_time": "2025-07-22T15:17:58.050+00:00"
        }
```

`],`

```json
    "pageSize": 10,
    "current": 1
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
|---|---|---|
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 知识库数据变更

**接口概述**

按照知识库数据模型定义将数据写入知识库,支持增、删、改

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/kortex/api/kb/data/consumeBulk POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostKortexApiKbDataConsumebulk

**请求头**

智能体工厂 OpenTrek 发指南

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| kbCode | Strin g | Body | 是 | cozhklqn3omz | 知识库唯一编码，该参数必填 |
| kbSubmod elCode | Strin g | Body | 是 | 1234 | 知识库内容结构唯一编码, 通过知识库详情获取，该参数必填 |
| datasource NodeId | Strin g | Body | 是 | source builtin smod _ _ | 数据加工来源知识库文档由 DKE加工chunk的场景传递 source builtin dke; 其他场 _ _ 景传递 source builtin smod; 删除 _ _ 场景传递 kb submodel，该 _ 参数必填 |
| forceRepla ce | Bool ean | Body | 是 | false | 强制走replace语义，该参数必填 |
| data | Repe atLis t | Body | 是 | [] | 需要变更的数据集合，该参数必填 |
| -key | Repe atLis t | Body | 否 | [] | 数据key标识，该参数必填 |
| -operation | Strin g | Body | 否 | Insert\|Delete\|Update | 操作，注意在一个消息里面, operation需要相同，该参数必填 |

智能体工厂 OpenTrek 发指南

| -after | Json | Body | 否 | {} | 具体数据内容, 按照知识库不同组装的结构也不同, 当 Insert\|Update 需要将数据传在after节点, 注意Update不支持增量更新,每次更新需要传递全量数据模型字段定义; 当Delete 可不传, 但要保障 key节点有值，该参数必填 |
|---|---|---|---|---|---|

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | object | 返回数据 | {} |
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**示例**

`JSON` 格式

```json
{
    "success": true,
    "data": null,
    "errorCode": null,
    "errorMsg": null
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
|---|---|---|
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 文档知识库资源用量-汇总KPI接口

**接口概述**

**接口调用地址**

GET POP_SDK[SysMethod]:GET POP_SDK[SysUriPattern]:/gatectl/kortex/api/statistics/kpi POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:GetKortexApiStatisticsKpi

**请求头**

智能体工厂 OpenTrek 发指南

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| dataType | Strin g | Quer y | 否 | 201 | 数据类型 |
| startTime | Strin g | Quer y | 否 | 2025-01-20 | 统计时间点，格式：YYYY- MM-DD。该场景与 endTime 保持一致 |
| endTime | Strin g | Quer y | 否 | 2025-01-26 | 统计时间点，格式：YYYY- MM-DD。该场景与 startTime 保持一致, 结束时间未传则默认是今天 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| errorCode | Integer | 错误码 | 0 |
| errorMsg | String | 错误信息 | success |
| success | Boolean | 是否成功 | true |
| data | List | 核心指标数据列表 | [{"key": "fileCount", "label": "文件总数", "value": 1262}, ...] |
| key | String | 指标Key | fileCount\|fileSize\|token Count |
| label | String | 指标名称 | 原始文件总数 |

智能体工厂 OpenTrek 发指南

| value | Integer | 指标值 | 1262 |
|---|---|---|---|

**示例**

`JSON` 格式

```json
{
  "success": true,
  "data": [
    {
      "key": "fileCount",
```

`"label": "`文件总数`",`

```json
      "value": 1
    },
    {
      "key": "fileSize",
```

`"label": "`文件大小`",`

```json
      "value": 3532962
    },
    {
      "key": "tokenCount",
```

`"label": "Token`总数(仅统计文档类型`)",`

```json
      "value": "121036"
    }
```

`],`

```json
  "errorCode": null,
  "errorMsg": null
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |

智能体工厂 OpenTrek 发指南

| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
|---|---|---|
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 文档知识库资源用量-明细数据接口

**接口概述**

**接口调用地址**

GET POP_SDK[SysMethod]:GET POP_SDK[SysUriPattern]:/gatectl/kortex/api/statistics/details POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:GetKortexApiStatisticsDetails

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek 发指南

| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
|---|---|---|---|---|---|
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageNumb er | Integ er | Quer y | 是 | 1 | 当前页码，该参数必填 |
| pageSize | Integ er | Quer y | 是 | 10 | 每页显示的条目数，该参数必填 |
| dataType | Strin g | Quer y | 否 | 1 | 目前仅支持文档知识库，可不传 |
| startTime | Strin g | Quer y | 否 | 2025-01-20 | 统计时间点，格式：YYYY- MM-DD。该场景与 endTime 保持一致 |
| endTime | Strin g | Quer y | 否 | 2025-01-26 | 统计时间点，格式：YYYY- MM-DD。该场景与 startTime 保持一致, 结束时间未传则默认是今天 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| errorCode | Integer | 错误码 | 200 |
| errorMsg | String | 错误信息 | success |
| success | Boolean | 是否成功 | true |
| data | Object | 分页数据对象 | 0 |
| pageNumber | Integer | 当前页码 | 1 |

智能体工厂 OpenTrek 发指南

| pageSize | Integer | 每页显示的条目数 | 10 |
|---|---|---|---|
| totalCount | Integer | 总条目数 | 35 |
| columns | List | 列定义元数据 | [{"label": "数据类型", "value": "dataType"}] |
| label | String | 列的显示名称 | 数据类型 |
| value | String | 列的字段Key | dataType |
| list | List | 当前页的数据列表 | [{...}] |
| kbName | String | 知识库名称 | 海冲测试数据集 |
| fileCount | Integer | 原始文件数 | 15 |
| fileSize | Integer | 原始文件大小(Bytes) | 214748364800 |
| tokenCount | Integer | Token总数 | 100000 |

**示例**

`JSON` 格式智能体工厂 OpenTrek 发指南

```json
{
  "success": true,
  "data": {
    "columns": [
      {
```

`"label": "`知识库名称`",`

```json
        "value": "kbName"
      },
      {
```

`"label": "`原始文件数`",`

```json
        "value": "fileCount"
      },
      {
```

`"label": "`原始文件大小`",`

```json
        "value": "fileSize"
      },
      {
        "label": "Token总数",
        "value": "tokenCount"
      }
```

`],`

```json
    "pageNumber": 1,
    "pageSize": 10,
    "totalCount": 1,
    "list": [
      {
        "projectCode": "05bb2bad-689b-4518-9a50-53953c65d59a",
        "date": null,
        "fileCount": 1,
        "fileSize": 3532962,
        "fileOtherSizes": null,
        "tokenCount": 121036,
```

`"kbName": "`高柴验证`",`

```json
        "kbCode": "v8ocqajdnb16"
      }
```

]

```json
  },
  "errorCode": null,
  "errorMsg": null
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
|---|---|---|
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 文档知识库资源用量-图表趋势接口

获取趋势图所需的时间序列数据

**接口概述**

获取趋势图所需的时间序列数据。[图表趋势接口]

**接口调用地址**

GET POP_SDK[SysMethod]:GET POP_SDK[SysUriPattern]:/gatectl/kortex/api/statistics/trend 智能体工厂 OpenTrek 发指南 POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:GetKortexApiStatisticsTrend

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| startTime | Strin g | Quer y | 否 | 2025-08-30 | 筛选的开始时间，格式： YYYY-MM-DD。 |
| endTime | Strin g | Quer y | 否 | 2025-01-26 | 筛选的结束时间，格式： YYYY-MM-DD。默认是最近七天 |
| dataType | Strin g | Quer y | 否 | 201 | 目前仅支持文档知识库，可不传 |
| timeRange | Strin g | Quer y | 否 | last 7 days _ _ | 预设时间范围。可选值: last 7 days, _ _ last 30 days, _ _ last 90 days, _ _ last 180 days。提供此参数 _ _ 时会忽略startTime和 endTime |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| errorCode | Integer | 错误码 | 200 |
| errorMsg | String | 错误信息 | success |
| success | Boolean | 是否成功 | true |

智能体工厂 OpenTrek 发指南

| data | Object | 趋势数据 | {"dimensions": [{...}, {...}], "source": [[...], ...]} |
|---|---|---|---|
| dimensions | List | 固定结构返回:维度和指标的名称列表，定义了 source数组中每一列的含义。 | [{"key":"date","label":" 时间"}, {"key":"fileCount","lab el":"文件总数"}, {"key":"fileSize","label ":"文件大小"}, {"key":"tokenCount","l abel":"token总数"}] |
| source | List | 数据矩阵。每一行代表一个时间点，每一列的值与 dimensions数组中的名称一一对应。 | [["2025-08-30", 18000, 1572864, 23943], ["2025-01- 21", 22000, 2097152, 134667]] |

**示例**

`JSON` 格式智能体工厂 OpenTrek 发指南

```json
{
  "success": true,
  "data": {
    "dimensions": [
      {
        "key": "date",
```

`"label": "`时间"

```json
      },
      {
        "key": "fileCount",
```

`"label": "`文件总数"

```json
      },
      {
        "key": "fileSize",
```

`"label": "`文件大小"

```json
      },
      {
        "key": "tokenCount",
        "label": "token总数"
      }
```

`],`

```json
    "source": [
```

[

```
        "2025-08-29",
```

`1,`

```
        3532962,
        121036
```

`],` [

```
        "2025-08-30",
```

`1,`

```
        3532962,
        121036
```

`],` [

```
        "2025-08-31",
```

`1,`

```
        3532962,
        121036
```

`],` [

```
        "2025-09-01",
```

`1,`

```
        3532962,
        121036
```

] ]

```json
  },
  "errorCode": null,
  "errorMsg": null
}
```

**文档补充说明**

智能体工厂 OpenTrek 发指南

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 知识库元数据更新

更新知识库元数据信息。 智能体工厂 OpenTrek 发指南

**接口调用地址**

```
 POST
 POP_SDK[SysMethod]:POST
 POP_SDK[SysUriPattern]:/gatectl/kortex/api/kb/updateMateData
```

`POP_SDK[SysDomain]:`见产品`API`文档页详情

```
 POP_SDK[Action]:PostKortexApiKbUpdatematedata
```

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填。 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填。 |
| x-sfm- authorizati on | Strin g | Hea der | 否 | Bearer YOUR APP KEY _ _ | APP KEY _ |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| code | Strin g | Body | 是 | z7pn9wbtkpy0 | 知识库唯一编码，该参数必填。 |
| name | Strin g | Body | 否 | 测试知识库 | 知识库名称。 |
| description | Strin g | Body | 否 | 知识库描述 | 知识库描述。 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功。 | true |

智能体工厂 OpenTrek 发指南

| data | object | 返回数据。 | {} |
|---|---|---|---|
| errorCode | String | 错误码。 | 400 |
| errorMsg | String | 错误描述。 | error |

**示例**

```json
{
  "success": true,
  "data": null,
  "errorCode": null,
  "errorMsg": null
}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失。 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败，无效 APP KEY。 _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败，APP KEY 已过期。 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色不匹配。 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色已过期。 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径。 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册。 |
| 429 | GATEWAY LIMIT ! | 服务触发限流，请稍后再试。 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流，请稍后再试。 |

智能体工厂 OpenTrek 发指南

| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失。 |
|---|---|---|
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配。 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败，不支持的鉴权方式。 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败，AK用户信息不匹配。 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败，用户角色不匹配。 |

##### 数据中心

数据中心相关API的介绍说明

###### 数据管理

###### 获取数据集列表

**接口概述**

**接口调用地址**

GET POP_SDK[SysMethod]:GET POP_SDK[SysUriPattern]:/gatectl/data-engine/api/v2/datasets POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:GetDataEngineApiV2Datasets

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

智能体工厂 OpenTrek 发指南

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| keyword | Strin g | Quer y | 否 | mmlu | 搜索关键字 |
| tags | Strin g | Quer y | 否 | 1,2,3 | 数据集标签KeyID |
| pageNumb er | Integ er | Quer y | 否 | 1 | 列表的页码 |
| pageSize | Integ er | Quer y | 否 | 10 | 每页行数 |
| order | Strin g | Quer y | 否 | DESC | 排序方式 |
| orderBy | Strin g | Quer y | 否 | createdAt | 排序字段 |
| brief | Bool ean | Quer y | 否 | false | 数据集简述 |
| ownerId | Strin g | Quer y | 否 | 123456 | 用户ID |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | Object | 返回数据 |  |
| datasets | List | 数据集列表 |  |
| id | Integer | 数据集ID | 128 |
| code | String | 数据集Code | mmlu no train _ _ |

智能体工厂 OpenTrek 发指南

| name | String | 数据集名称 | dataset001 |
|---|---|---|---|
| description | String | 数据集描述 |  |
| parquetFileSize | Integer | 数据集大小 | 118019 |
| rowCount | Integer | 数据行数 | 36 |
| downloadCount | Integer | 下载次数 | 9 |
| tags | List | 标签列表 |  |
| id | Integer | 标签ID | 7 |
| name | String | 标签名称 | 多标签分类 |
| value | String | 标签值 |  |
| ownerId | String | 数据集所有者ID | 1631044****3440 |
| ownerName | String | 数据集所有者用户名 | admin |
| tenantCode | String | 租户Code | sfmboost |
| workspaceCode | String | 工作组Code | default workspace _ |
| createdAt | String | 创建时间 | 2021-01- 30T12:51:33.028Z |
| updatedAt | String | 更新时间 | 2021-01- 30T12:51:33.028Z |
| pageSize | Integer | 每页行数 | 20 |
| totalCount | Integer | 总数量 | 79 |
| pageNumber | Integer | 当前页码 | 1 |

智能体工厂 OpenTrek 发指南

**示例**

`JSON` 格式

```json
{
  "datasets": [
    {
      "id": 128,
      "code": "mmlu_no_train",
      "name": "dataset001",
      "description": "",
      "parquetFilesSize": 118019,
      "rowCount": 36,
      "downloadCount": 9,
      "tags": [
        {
          "id": 7,
```

`"name": "`多标签分类`",`

```json
          "value": ""
        },
        {
          "id": 202,
```

`"name": "`法语`",` `"value": "`法语标签值"

```
        }
```

`],`

```json
      "ownerId": "1631044****3440",
      "ownerName": "admin",
      "tenantCode": "sfmboost",
      "workspaceCode": "default_workspace",
      "createdAt": "2021-01-30T12:51:33.028Z",
      "updatedAt": "2021-01-30T12:51:33.028Z"
    }
```

`],`

```json
  "pageSize": 20,
  "totalCount": 79,
  "pageNumber": 1
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
|---|---|---|
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 新建数据集

**接口概述**

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/data-engine/api/v2/datasets POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostDataEngineApiV2Datasets 智能体工厂 OpenTrek 发指南

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| code | Strin g | Body | 是 | mmlu no train _ _ | 数据集code，该参数必填 |
| name | Strin g | Body | 否 | 数据集 | 数据集名称 |
| subset | Strin g | Body | 否 | default | 子集名称 |
| split | Strin g | Body | 否 | train | 切片名称 |
| description | Strin g | Body | 否 | 测试数据 | 数据集描述 |
| tags | Repe atLis t | Body | 否 | [{"id":1234, "value":"1w- 10w"}] | 标签列表 |
| -id | Integ er | Body | 否 | 1234 | 标签ID |
| -value | Strin g | Body | 否 | 1w-10w | 标签值 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|

智能体工厂 OpenTrek 发指南

| success | Boolean | 是否成功 | true |
|---|---|---|---|
| data | Object | 返回数据 | { "id": 99, "code": "mmlu no train" } _ _ |
| id | Integer | 数据集id | 99 |
| code | String | 数据集code | mmlu no train _ _ |

**示例**

`JSON` 格式

```json
{
  "success": true,
  "data": {
    "id": 99,
    "code": "mmlu_no_train"
  }
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |

智能体工厂 OpenTrek 发指南

| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
|---|---|---|
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 更新数据集

**接口概述**

**接口调用地址**

PUT POP_SDK[SysMethod]:PUT POP_SDK[SysUriPattern]:/gatectl/data-engine/api/v2/datasets POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PutDataEngineApiV2Datasets

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

智能体工厂 OpenTrek 发指南

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| code | Strin g | Body | 是 | mmlu no train _ _ | 数据集code，该参数必填 |
| name | Strin g | Body | 否 | 张三测试数据集 | 数据集名称 |
| description | Strin g | Body | 否 | testDescription | 数据集描述 |
| tags | Repe atLis t | Body | 否 | [{"id":123, "value":"1w- 10w"}] | 标签列表 |
| -id | Integ er | Body | 否 | 123 | 标签ID |
| -value | Strin g | Body | 否 | 1w-10w | 标签值 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | Boolean | 返回数据 | true |

**示例**

`JSON` 格式

```json
{
  "success": true,
  "data": true
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
|---|---|---|
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 删除数据集

**接口概述**

智能体工厂 OpenTrek 发指南

**接口调用地址**

DELETE POP_SDK[SysMethod]:DELETE POP_SDK[SysUriPattern]:/gatectl/data-engine/api/v2/datasets/[code] POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:DeleteDataEngineApiV2DatasetsCode

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| code | Strin g | Path | 是 | mmlu no train _ _ | 数据集Code，该参数必填 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | Boolean | 返回数据 | true |

**示例**

`JSON` 格式

```json
{
  "success": true,
  "data": true
}
```

**文档补充说明**

智能体工厂 OpenTrek 发指南

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 获取数据集详情

智能体工厂 OpenTrek 发指南

**接口概述**

**接口调用地址**

GET POP_SDK[SysMethod]:GET POP_SDK[SysUriPattern]:/gatectl/data-engine/api/v2/datasets/[code] POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:GetDataEngineApiV2DatasetsCode

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| code | Strin g | Path | 是 | mmlu no train _ _ | 数据集Code |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | Object | 返回数据 |  |
| code | String | 数据集Code | mmlu no train _ _ |
| name | String | 数据集名称 | 剑三测试数据集 |
| description | String | 数据集描述 |  |

智能体工厂 OpenTrek 发指南

| originalFileSize | Integer | 原始资源文件大小, 单位 bytes | 118019 |
|---|---|---|---|
| parquetFileSize | Integer | 数据集大小, 单位bytes | 118019 |
| rowCount | Integer | 数据行数 | 36 |
| downloadCount | Integer | 下载次数 | 9 |
| tags | List | 标签列表 |  |
| id | Integer | 标签ID | 123 |
| name | String | 标签名称 | size scale _ |
| value | String | 标签值 | lw-10w |
| subsets | List | 子集列表 |  |
| code | String | 子集Code | default |
| name | String | 子集名称 | default |
| parquetFileSize | Integer | 子集数据大小, 单位bytes | 0 |
| rowCount | Integer | 子集数据行数 | 19 |
| features | List | 字段列表 |  |
| columnName | String | 字段名称 | idx __ |
| columnType | String | 字段类型 | string |
| columnPhysicalType | String | 字段物理类型 | varchar |
| columnComment | String | 字段描述 | 数据项唯一标识 |
| splits | List | 切片列表 |  |

智能体工厂 OpenTrek 发指南

| code | String | 切片Code | train |
|---|---|---|---|
| subset | String | 所属子集 | default |
| name | String | 切片名称 | train |
| parquetFileSize | Integer | 切片数据大小, 单位bytes | 0 |
| rowCount | Integer | 切片数据行数 | 19 |
| dataFiles | List | 数据文件列表 | ["cat.jpg", "dog.jpg", "cet.jpg"] |
| producer | String | 数据来源标识: KN DATASET, _ KN PROCESS, _ KN LABEL, UNKNOWN _ | KN DATASET _ |
| ownerId | String | 数据集所有者ID | 1631044****3440 |
| ownerName | String | 数据集所有者用户名 | admin |
| tenantCode | String | 租户Code | sfmboost |
| workspaceCode | String | 工作组Code | default workspace _ |
| createdAt | String | 创建时间 | 2021-01- 30T12:51:33.028Z |
| updatedAt | String | 更新时间 | 2021-01- 30T12:51:33.028Z |
| repoPath | String | 数据集仓库地址 | sfm/dataset/baseline/ mmlu no train/main _ _ |
| parquetPath | String | 数据集parquet地址 | sfm/dataset/baseline/ mmlu no train/parque _ _ t |
| summaryModified | String | 数据集摘要最后修改时间 | 2021-01- 30T12:51:33.028Z |

智能体工厂 OpenTrek 发指南

**示例**

`JSON` 格式

```json
{
  "code": "mmlu_no_train",
```

`"name": "`张三测试数据集`",`

```json
  "description": "",
  "parquetFilesSize": 118019,
  "rowCount": 36,
  "downloadCount": 9,
  "tags": [
    {
      "id": 123,
      "name": "size_scale",
      "value": "1w-10w"
    }
```

`],`

```json
  "subsets": [
    {
      "code": "default",
      "name": "default",
      "parquetFilesSize": 0,
      "rowCount": 19,
      "features": [
        {
          "columnName": "__idx",
          "columnType": "string",
          "columnPhysicalType": "varchar",
          "columnComment": ""
        },
        {
          "columnName": "__content",
          "columnType": "string",
          "columnPhysicalType": "varchar",
          "columnComment": ""
        }
```

`],`

```json
      "splits": [
        {
          "code": "train",
          "subset": "default",
          "name": "train",
          "parquetFilesSize": 0,
          "rowCount": 19
        }
```

]

```
    }
```

`],`

```json
  "ownerId": "1631044****3440",
  "ownerName": "admin",
  "tenantCode": "sfmboost",
  "workspaceCode": "default_workspace",
  "createdAt": "2021-01-30T12:51:33.028Z",
"updatedAt":"2021-01-30T12:51:33.028Z",
```

智能体工厂 OpenTrek 发指南

```json
  updatedAt: 20210130T12:51:33.028Z,
  "repoPath": "sfm/dataset/baseline/mmlu_no_train/main",
  "parquetPath": "sfm/dataset/baseline/mmlu_no_train/parquet"
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |
|---|---|---|

###### 通知数据集文件增加

**接口概述**

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/data-engine/api/v2/datasets/[code]/files POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostDataEngineApiV2DatasetsCodeFiles

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| code | Strin g | Path | 是 | mmlu no train _ _ | 数据集Code |
| filePaths | Repe atLis t | Body | 是 | ["pdfs/1902.10909v1.pdf" ,"Ray -分布式计算框架架构设计详解 v2.pdf","pdfs/2406.02543 v1.pdf"] | 文件路径列表，该参数必填 |
| relative | Bool ean | Body | 是 | true | 是否为相对路径，该参数必填 |

**返回参数**

智能体工厂 OpenTrek 发指南

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | Object | 返回数据 |  |
| id | String | 任务ID | 510FF634FCE407EEA1 763854519FD3CE |
| completed | Boolean | 是否完成 | true |
| createTime | String | 创建时间 | 2024-10- 08T11:53:23.000Z |
| status | String | 任务状态：Success, Fail, Cancel | Success |
| response | Object | 任务响应数据 | {} |
| error | String | 错误信息 |  |
| progress | Integer | 执行进度 | 100 |

**示例**

`JSON` 格式

```json
{
  "success": true,
  "data": {
    "id": "510FF634FCE407EEA1763854519FD3CE",
    "completed": true,
    "createTime": "2024-10-08T11:53:23.000Z",
    "status": "Success",
    "response": {},
    "error": "",
    "progress": 100
  }
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
|---|---|---|
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 通知数据集文件删除

**接口概述**

智能体工厂 OpenTrek 发指南

**接口调用地址**

DELETE POP_SDK[SysMethod]:DELETE POP_SDK[SysUriPattern]:/gatectl/data-engine/api/v2/datasets/[code]/files POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:DeleteDataEngineApiV2DatasetsCodeFiles

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| code | Strin g | Path | 是 | mmlu no train _ _ | 数据集Code |
| filePaths | Repe atLis t | Body | 是 | ["pdfs/1902.10909v1.pdf" , "Ray -分布式计算框架架构设计详解 v2.pdf", "pdfs/2406.02543v1.pdf"] | 文件相对路径数组，该参数必填 |
| relative | Bool ean | Body | 是 | true | 是否为相对路径，该参数必填 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | Object | 返回数据 |  |
| id | String | 任务ID | 510FF634FCE407EEA1 763854519FD3CE |

智能体工厂 OpenTrek 发指南

| completed | Boolean | 是否执行完成 | true |
|---|---|---|---|
| createTime | String | 任务创建时间 | 2024-10- 08T11:53:23.000Z |
| status | String | 任务状态 | Success |
| response | Object | 任务生成的资源信息 | {} |
| error | String | 错误信息 |  |
| progress | Integer | 执行进度 | 100 |

**示例**

`JSON` 格式

```json
{
  "success": true,
  "data": {
    "id": "510FF634FCE407EEA1763854519FD3CE",
    "completed": true,
    "createTime": "2024-10-08T11:53:23.000Z",
    "status": "Success",
    "response": {},
    "error": "",
    "progress": 100
  }
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
|---|---|---|
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 获取数据集文件列表

分页查询数据集文件列表

**接口概述**

分页查询数据集文件列表[ListDatasetFiles]

**接口调用地址**

GET POP_SDK[SysMethod]:GET POP_SDK[SysUriPattern]:/gatectl/data-engine/api/v2/datasets/[code]/files POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:GetDataEngineApiV2DatasetsCodeFiles

**请求头**

智能体工厂 OpenTrek 发指南

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| code | Strin g | Path | 是 | COCO 2017 _ | 数据集Code |
| filePath | Strin g | Quer y | 否 | val | 文件路径 |
| relative | Bool ean | Quer y | 否 | true | 是否为相对路径 |
| pageNumb er | Integ er | Quer y | 否 | 1 | 页码 |
| pageSize | Integ er | Quer y | 否 | 10 | 每页数量 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | Object | 返回数据 |  |
| datasetFileInfos | List | 文件信息列表 |  |
| name | String | 文件名 | 000000000139.jpg |

智能体工厂 OpenTrek 发指南

| filepath | String | 文件路径 | sfm/dataset/baseline/o pentrek/COCO 2017/m _ ain/val/000000000139 .jpg |
|---|---|---|---|
| suffix | String | 文件后缀 | jpg |
| size | Integer | 文件大小 | 161811 |
| lastModified | Integer | 最后修改时间戳 | 1737106513 |
| pageSize | Integer | 每页数量 | 10 |
| totalCount | Integer | 总数 | 5000 |
| pageNumber | Integer | 当前页码 | 1 |

**示例**

`JSON` 格式

```json
{
  "success": true,
  "data": {
    "datasetFileInfos": [
      {
        "name": "000000000139.jpg",
        "filepath":
"sfm/dataset/baseline/opentrek/COCO_2017/main/val/000000000139.jpg",
        "suffix": "jpg",
        "size": 161811,
        "lastModified": 1737106513
      },
      {
        "name": "000000000285.jpg",
        "filepath":
"sfm/dataset/baseline/opentrek/COCO_2017/main/val/000000000285.jpg",
        "suffix": "jpg",
        "size": 335861,
        "lastModified": 1737106513
      }
```

`],`

```json
    "pageSize": 10,
    "totalCount": 5000,
    "pageNumber": 1
  }
}
```

智能体工厂 OpenTrek 发指南

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

智能体工厂 OpenTrek 发指南

###### 新建数据子集

**接口概述**

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/data-engine/api/v2/datasets/[code]/subsets POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostDataEngineApiV2DatasetsCodeSubsets

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，改参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| code | Strin g | Path | 是 | mmlu no train _ _ | 数据集Code |
| subset | Strin g | Body | 是 | default | 数据子集code，该参数必填 |
| dataFiles | Repe atLis t | Body | 是 | ["pdfs/1902.10909v1.pdf" ] | 关联数据文件列表，该参数必填 |
| autoUpdat e | Bool ean | Body | 是 | false | 是否自动更新视图，该参数必填 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|

智能体工厂 OpenTrek 发指南

| success | Boolean | 是否成功 | true |
|---|---|---|---|
| data | Object | 返回数据 |  |
| id | Integer | 子集ID | 278 |
| code | String | 子集Code | new yaml test _ _ |
| createdAt | String | 创建时间 | 2025-03- 06T11:41:33.271Z |
| updatedAt | String | 更新时间 | 2025-03- 06T11:41:33.271Z |
| workspaceCode | String | 工作组Code | opentrek |
| tenantCode | String | 租户Code | baseline |
| name | String | 子集名称 | 子集配置测试 |
| description | String | 子集描述 | 子集配置测试 |
| originalFileSize | Integer | 原始文件大小 | 0 |
| parquetFileSize | Integer | 数据视图大小 | 0 |
| rowCount | Integer | 数据行数 | 0 |
| downloadCount | Integer | 下载次数 | 0 |
| ownerId | String | 所有者ID | 20240813 |
| ownerName | String | 所有者名称 | admin |
| tags | List | 标签列表 | [] |

**示例**

`JSON` 格式智能体工厂 OpenTrek 发指南

```json
{
  "success": true,
  "data": {
    "id": 278,
    "code": "new_yaml_test",
    "createdAt": "2025-03-06T11:41:33.271Z",
    "updatedAt": "2025-03-06T11:41:33.271Z",
    "workspaceCode": "opentrek",
    "tenantCode": "baseline",
```

`"name": "`子集配置测试`",` `"description": "`子集配置测试`",`

```json
    "originalFilesSize": 0,
    "parquetFilesSize": 0,
    "rowCount": 0,
    "downloadCount": 0,
    "ownerId": "20240813",
    "ownerName": "admin",
    "tags": []
  }
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |

智能体工厂 OpenTrek 发指南

| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
|---|---|---|
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 更新数据子集

**接口概述**

**接口调用地址**

PUT POP_SDK[SysMethod]:PUT POP_SDK[SysUriPattern]:/gatectl/data-engine/api/v2/datasets/[code]/subsets POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PutDataEngineApiV2DatasetsCodeSubsets

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

智能体工厂 OpenTrek 发指南

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| code | Strin g | Path | 是 | mmlu no train _ _ | 数据集Code |
| subset | Strin g | Body | 是 | default | 数据子集code，该参数必填 |
| dataFiles | Repe atLis t | Body | 是 | ["pdfs/*.pdf"] | 关联数据文件列表，该参数必填 |
| autoUpdat e | Bool ean | Body | 是 | true | 是否自动更新视图，该参数必填 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | Object | 返回数据 |  |
| id | Integer | 数据集ID | 278 |
| code | String | 数据集Code | new yaml test _ _ |
| createdAt | String | 创建时间 | 2025-03- 06T11:41:33.271Z |
| updatedAt | String | 更新时间 | 2025-03- 06T11:41:33.271Z |
| workspaceCode | String | 工作组Code | opentrek |
| tenantCode | String | 租户Code | baseline |
| name | String | 数据集名称 | 子集配置测试 |
| description | String | 数据集描述 | 子集配置测试 |

智能体工厂 OpenTrek 发指南

| originalFileSize | Integer | 原始资源文件大小 | 0 |
|---|---|---|---|
| parquetFileSize | Integer | 数据集大小 | 0 |
| rowCount | Integer | 数据行数 | 0 |
| downloadCount | Integer | 下载次数 | 0 |
| ownerId | String | 所有者ID | 20240813 |
| ownerName | String | 所有者用户名 | admin |
| tags | List | 标签列表 | [] |

**示例**

`JSON` 格式

```json
{
  "success": true,
  "data": {
    "id": 278,
    "code": "new_yaml_test",
    "createdAt": "2025-03-06T11:41:33.271Z",
    "updatedAt": "2025-03-06T11:41:33.271Z",
    "workspaceCode": "opentrek",
    "tenantCode": "baseline",
```

`"name": "`子集配置测试`",` `"description": "`子集配置测试`",`

```json
    "originalFilesSize": 0,
    "parquetFilesSize": 0,
    "rowCount": 0,
    "downloadCount": 0,
    "ownerId": "20240813",
    "ownerName": "admin",
    "tags": []
  }
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
|---|---|---|
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 删除数据集子集

**接口概述**

**接口调用地址**

DELETE 智能体工厂 OpenTrek 发指南 POP_SDK[SysMethod]:DELETE POP_SDK[SysUriPattern]:/gatectl/data-engine/api/v2/datasets/[code]/subsets/[subsetCode] POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:DeleteDataEngineApiV2DatasetsCodeSubsetsSubsetcode

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| code | Strin g | Path | 是 | mmlu no train _ _ | 数据集Code |
| subsetCod e | Strin g | Path | 是 | mmlu no train _ _ | 数据子集Code |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | Boolean | 返回数据 | true |

**示例**

`JSON` 格式

```json
{
  "success": true,
  "data": true
}
```

**文档补充说明**

智能体工厂 OpenTrek 发指南

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 数据集子集列表

智能体工厂 OpenTrek 发指南

**接口概述**

**接口调用地址**

GET POP_SDK[SysMethod]:GET POP_SDK[SysUriPattern]:/gatectl/data-engine/api/v2/datasets/[code]/subsets POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:GetDataEngineApiV2DatasetsCodeSubsets

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| code | String | Path | 是 | mmlu no train _ _ | 数据集Code |
| built | Boolea n | Quer y | 否 | true | 是否只获取已构建好的子集 |
| subsets | Repea tList | Quer y | 否 | ["default"] | 子集列表 |
| pageNumber | Intege r | Quer y | 否 | 1 | 列表的页码 |
| pageSize | Intege r | Quer y | 否 | 20 | 分页查询时设置的每页行数 |
| keyword | String | Quer y | 否 | "image" | 关键字 |

**返回参数**

智能体工厂 OpenTrek 发指南

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | Object | 返回数据 |  |
| subsets | List | 子集列表 |  |
| code | String | 子集Code | image subset _ |
| name | String | 子集名称 | image subset _ |
| parquetFileSize | Integer | 子集数据大小, 单位bytes | 275025 |
| rowCount | Integer | 子集数据行数 | 5000 |
| features | List | 字段列表 |  |
| columnName | String | 字段名称 | idx __ |
| columnType | String | 字段类型 | string |
| columnPhysicalType | String | 字段物理类型 | varchar |
| columnComment | String | 字段描述 |  |
| splits | List | 切片列表 |  |
| code | String | 切片Code | train |
| subset | String | 所属子集 | image subset _ |
| name | String | 切片名称 | train |
| parquetFileSize | Integer | 切片数据大小, 单位bytes | 275025 |
| rowCount | Integer | 切片数据行数 | 5000 |

智能体工厂 OpenTrek 发指南

| sourceFiles | List | 源文件列表 | ["sfm/dataset/baseline /opentrek/COCO 2017/ _ main/**/*.jpg"] |
|---|---|---|---|
| lastModified | Integer | 最后修改时间 | 1737107658 |
| pageSize | Integer | 每页数量 | 2 |
| totalCount | Integer | 总数 | 2 |
| pageNumber | Integer | 当前页码 | 1 |

**示例**

`JSON` 格式

```json
{
  "success": true,
  "data": {
    "subsets": [
      {
        "code": "image_subset",
        "name": "image_subset",
        "parquetFilesSize": 275025,
        "rowCount": 5000,
        "features": [
          {
            "columnName": "__idx",
            "columnType": "string",
            "columnPhysicalType": "varchar",
            "columnComment": ""
          },
          {
            "columnName": "image",
            "columnType": "Image",
            "columnPhysicalType": "struct(bytes blob, path varchar)",
            "columnComment": ""
          }
```

`],`

```json
        "splits": [
          {
            "code": "train",
            "subset": "image_subset",
            "name": "train",
            "parquetFilesSize": 275025,
            "rowCount": 5000,
            "sourceFiles": [
              "sfm/dataset/baseline/opentrek/COCO_2017/main/**/*.jpg"
```

]

```
          }
```

] 智能体工厂 OpenTrek 发指南 `],`

```json
        "lastModified": 1737107658
      },
      {
        "code": "image_subset_annotation_dd52841...9d1e7925c5",
        "name": "image_subset_annotation_dd52841...9d1e7925c5",
        "parquetFilesSize": 8898,
        "rowCount": 14,
        "features": [
          {
            "columnName": "image",
            "columnType": "Image",
            "columnPhysicalType": "struct(bytes blob, path varchar)",
            "columnComment": ""
          },
          {
            "columnName": "label",
            "columnType": "string",
            "columnPhysicalType": "varchar",
            "columnComment": ""
          }
```

`],`

```json
        "splits": [
          {
            "code": "train",
            "subset": "image_subset_annotation_dd52841...9d1e7925c5",
            "name": "train",
            "parquetFilesSize": 8898,
            "rowCount": 14,
            "sourceFiles": [
"sfm/dataset/baseline/opentrek/COCO_2017/parquet/image_subset_annotation_dd528417ad82405f 5e969d1e7925c5/train/0000.parquet"
```

]

```
          }
```

`],`

```json
        "lastModified": 1737107659
      }
```

`],`

```json
    "pageSize": 2,
    "totalCount": 2,
    "pageNumber": 1
  }
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
|---|---|---|
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 数据集子集列表筛选

**接口概述**

**前提条件（查看APP_KEY）**

智能体工厂 OpenTrek 发指南数据集子集列表筛选。可以通过查看请求示例，点击 curl 命令示例右侧的调试按钮验证业务接口调用效果。

**接口调用地址**

POST https://{host}/gatectl/data-engine/api/v2/datasets/{datasetCode}/subsets/search

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- authorizati on | Strin g | Hea der | 否 | Bearer YOUR APP KEY _ _ | APP KEY _ |
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| code | String | Path | 是 | mmlu no train _ _ | 数据集Code |
| built | Boolea n | Body | 否 | true | 是否只获取已构建好的子集 |
| subsets | Repeat List | Body | 否 | ["default"] | 子集列表 |
| pageNumber | Integer | Body | 否 | 1 | 列表的页码 |
| pageSize | Integer | Body | 否 | 20 | 分页查询时设置的每页行数 |
| keyword | String | Body | 否 | "image" | 关键字 |
| sourceFileTypes | Repeat List | Body | 否 | ["parquet"] | 按子集split关联数据文件类型筛选 |

智能体工厂 OpenTrek 发指南

| featureFilters | Repeat List | Body | 否 | [{"featureFilter Method":"CONT AINS","features" : [{"columnName ":"image"}, {"columnName ":" idx","colum __ nType":"string" }]}] | 按schema筛选子集 |
|---|---|---|---|---|---|

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| code | String | 子集Code | image subset _ |
| name | String | 子集名称 | image subset _ |
| parquetFilesSize | Integer | 子集数据大小，单位 bytes | 275025 |
| rowCount | Integer | 子集数据行数 | 5000 |
| features | List | 字段列表 |  |
| columnName | String | 字段名称 | idx __ |
| columnType | String | 字段类型 | string |
| columnPhysicalType | String | 字段物理类型 | varchar |
| columnComment | String | 字段描述 |  |
| splits | List | 切片列表 |  |
| code | String | 切片Code | train |
| subset | String | 所属子集 | image subset _ |
| name | String | 切片名称 | train |

智能体工厂 OpenTrek 发指南

| parquetFilesSize | Integer | 切片数据大小，单位 bytes | 275025 |
|---|---|---|---|
| rowCount | Integer | 切片数据行数 | 5000 |
| sourceFiles | List | 源文件列表 | ["sfm/dataset/baseline /opentrek/COCO 2017/ _ main/**/* .jpg"] |
| lastModified | Integer | 最后修改时间 | 1737107658 |

**示例**

`JSON` 格式

```json
{
        "code": "image_subset",
        "name": "image_subset",
        "parquetFilesSize": 275025,
        "rowCount": 5000,
        "features": [
          {
            "columnName": "__idx",
            "columnType": "string",
            "columnPhysicalType": "varchar",
            "columnComment": ""
          },
          {
            "columnName": "image",
            "columnType": "Image",
            "columnPhysicalType": "struct(bytes blob, path varchar)",
            "columnComment": ""
          }
```

`],`

```json
        "splits": [
          {
            "code": "train",
            "subset": "image_subset",
            "name": "train",
            "parquetFilesSize": 275025,
            "rowCount": 5000,
            "sourceFiles": [
              "sfm/dataset/baseline/opentrek/COCO_2017/main/**/*.jpg"
```

]

```
          }
```

`],`

```json
        "lastModified": 1737107658
      }
```

**文档补充说明**

智能体工厂 OpenTrek 发指南

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 获取数据集预览数据

智能体工厂 OpenTrek 发指南

**接口概述**

**接口调用地址**

GET POP_SDK[SysMethod]:GET POP_SDK[SysUriPattern]:/gatectl/data-engine/api/v2/datasets/[code]/viewer POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:GetDataEngineApiV2DatasetsCodeViewer

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| code | Strin g | Path | 是 | mmlu no train _ _ | 数据集Code |
| subset | Strin g | Quer y | 否 | default | 子集Code |
| split | Strin g | Quer y | 否 | train | 切片Code |
| pageNumb er | Integ er | Quer y | 否 | 1 | 列表的页码 |
| pageSize | Integ er | Quer y | 否 | 10 | 分页查询时设置的每页行数 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|

智能体工厂 OpenTrek 发指南

| success | Boolean | 是否成功 | true |
|---|---|---|---|
| data | Object | 返回数据 |  |
| schema | List | 字段信息 |  |
| columnName | String | 字段名称 | pdf url _ |
| columnType | String | 字段类型 | string |
| columnPhysicalType | String | 字段物理类型 | varchar |
| data | List | 数据内容 | [["oss://xxx/tenant/dat aset/xxx/tmp/xxx.pdf", {"path": "tmp/xxx.pdf", "bytes": null}, 19849], ...] |
| status | String | 视图构建状态： BUILDING, BUILD FAILED, BUILT _ | BUILD FAILED _ |
| message | String | 错误信息 | ... |
| pageSize | Integer | 每页行数 | 100 |
| totalCount | Integer | 总行数 | 12389 |
| pageNumber | Integer | 当前页码 | 1 |

**示例**

`JSON` 格式智能体工厂 OpenTrek 发指南

```json
{
  "success": true,
  "data": {
    "schema": [
      {
        "columnName": "pdf_url",
        "columnType": "string",
        "columnPhysicalType": "varchar"
      },
      {
        "columnName": "file",
        "columnType": "Doc",
        "columnPhysicalType": "struct(bytes blob, path varchar)"
      },
      {
        "columnName": "size",
        "columnType": "int64",
        "columnPhysicalType": "int64"
      }
```

`],`

```json
    "data": [
```

[

```json
        "oss://xxx/tenant/dataset/xxx/tmp/xxx.pdf",
        {
          "path": "tmp/xxx.pdf",
          "bytes": null
        },
        19849
```

] `],`

```json
    "status": "BUILD_FAILED",
    "message": "...",
    "pageSize": 100,
    "totalCount": 12389,
    "pageNumber": 1
  }
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
|---|---|---|
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 获取图片下载地址

获取图片URL

**接口概述**

获取图片URL[GetImagePresignedUrl]

**接口调用地址**

GET POP_SDK[SysMethod]:GET POP_SDK[SysUriPattern]:/gatectl/data-engine/api/v2/files/image/presigned/url POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:GetDataEngineApiV2FilesImagePresignedUrl 智能体工厂 OpenTrek 发指南

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| datasetCo de | Strin g | Quer y | 是 | mmlu | 数据集Code |
| filePath | Strin g | Quer y | 是 | train/乌龟谭.jpeg | 文件相对路径 |
| width | Integ er | Quer y | 否 | 100 | 指定图片宽度 |
| height | Integ er | Quer y | 否 | 100 | 指定图片高度 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | Object | 返回数据 |  |
| url | String | 图片URL | https://oss-cn- hangzhou.aliyuncs.co m/.../%E4%B9%8C%E9 %BE%9F%E9%BE%9F %E6%BD%AD.jpeg? Signature=xxx |
| expiration | Integer | 有效期(秒) | 3600 |

智能体工厂 OpenTrek 发指南

| expireTime | String | 过期时间 | 2024-10- 08T11:53:23.000Z |
|---|---|---|---|

**示例**

`JSON` 格式

```json
{
  "success": true,
  "data": {
    "url": "https://oss-cn-hangzhou.aliyuncs.com/../%E4%B9%8C%E9%BE%9F%E6%BD%AD.jpeg?Si
gnature=xxx",
    "expiration": 3600,
    "expireTime": "2024-10-08T11:53:23.000Z"
  }
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |

智能体工厂 OpenTrek 发指南

| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
|---|---|---|
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 获取文件下载地址

**接口概述**

**接口调用地址**

GET POP_SDK[SysMethod]:GET POP_SDK[SysUriPattern]:/gatectl/data-engine/api/v2/files/presigned/url POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:GetDataEngineApiV2FilesPresignedUrl

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek 发指南

| datasetCo de | Strin g | Quer y | 是 | mmlu | 数据集Code |
|---|---|---|---|---|---|
| filePath | Strin g | Quer y | 是 | pdfs/1902.10909v1.pdf | 文件相对路径 |
| useShortUr l | Bool ean | Quer y | 否 | false | 是否返回短地址默认值： false |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | Object | 返回数据 |  |
| url | String | 预签名下载地址 | https://oss-cn- hangzhou.aliyuncs.co m/.../1902.10909v1.pd f?Signature=xxx |
| expiration | Integer | 有效期(秒) | 3600 |
| expireTime | String | 过期时间 | 2024-10- 08T11:53:23.000Z |

**示例**

`JSON` 格式

```json
{
  "success": true,
  "data": {
    "url": "https://oss-cn-hangzhou.aliyuncs.com/../1902.10909v1.pdf?Signature=xxx",
    "expiration": 3600,
    "expireTime": "2024-10-08T11:53:23.000Z"
  }
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
|---|---|---|
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 删除文件

**接口概述**

**接口调用地址**

DELETE 智能体工厂 OpenTrek 发指南 POP_SDK[SysMethod]:DELETE POP_SDK[SysUriPattern]:/gatectl/data-engine/api/v2/files POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:DeleteDataEngineApiV2Files

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| datasetCo de | Strin g | Quer y | 是 | mmlu | 数据集Code |
| filePaths | Repe atLis t | Quer y | 是 | ["train/乌龟谭.jpeg"] | 文件路径列表 |
| relative | Bool ean | Quer y | 否 | true | 是否使用相对路径 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | Object | 返回数据 | { "cnt": 1, "deletedFiles": ["train/ 乌龟潭.jpeg"] } |
| cnt | Integer | 删除文件数量 | 1 |
| deletedFiles | List | 已删除文件列表 | ["train/乌龟潭.jpeg"] |

智能体工厂 OpenTrek 发指南

**示例**

`JSON` 格式

```json
{
  "success": true,
  "data": {
    "cnt": 1,
    "deletedFiles": ["train/乌龟谭.jpeg"]
  }
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |

智能体工厂 OpenTrek 发指南

| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
|---|---|---|
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 获取文件上传授权凭证

**接口概述**

**接口调用地址**

GET POP_SDK[SysMethod]:GET POP_SDK[SysUriPattern]:/gatectl/data-engine/api/v2/files/upload/credential POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:GetDataEngineApiV2FilesUploadCredential

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| datasetCo de | Strin g | Quer y | 是 | mmlu | 数据集Code |

智能体工厂 OpenTrek 发指南

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | Object | 返回数据 |  |
| type | String | 存储类型 | oss |
| endpoint | String | 访问端点 | https://oss-cn- hangzhou.aliyuncs.co m |
| internalEndpoint | String | 内部访问地址 | xxx |
| externalEndpoint | String | 外部访问地址 | xxx |
| bucket | String | 存储桶名称 | kn-tenant-xxx |
| region | String | 区域 | xxx |
| accessKeyId | String | 访问密钥ID | xxx |
| accessKeySecret | String | 访问密钥 | xxx |
| stsToken | String | STS令牌 | xxx |
| expiration | Integer | 有效期(秒) | 3600 |
| expireTime | String | 过期时间 | 2024-10- 08T11:53:23.000Z |

**示例**

`JSON` 格式智能体工厂 OpenTrek 发指南

```json
{
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
  }
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |

智能体工厂 OpenTrek 发指南

| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
|---|---|---|
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 获取文件下载授权凭证

**接口概述**

**接口调用地址**

GET POP_SDK[SysMethod]:GET POP_SDK[SysUriPattern]:/gatectl/data-engine/api/v2/files/download/credential POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:GetDataEngineApiV2FilesDownloadCredential

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek 发指南

| datasetCo de | Strin g | Quer y | 是 | mmlu | 数据集Code |
|---|---|---|---|---|---|

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | Object | 返回数据 |  |
| type | String | 存储类型 | oss |
| endpoint | String | 访问端点 | https://oss-cn- hangzhou.aliyuncs.co m |
| internalEndpoint | String | 内部访问地址 | xxx |
| externalEndpoint | String | 外部访问地址 | xxx |
| bucket | String | 存储桶名称 | kn-tenant-xxx |
| region | String | 区域 | xxx |
| accessKeyId | String | 访问密钥ID | xxx |
| accessKeySecret | String | 访问密钥 | xxx |
| stsToken | String | 安全令牌 | xxx |
| expiration | Integer | 有效期(秒) | 3600 |
| expireTime | String | 过期时间 | 2024-10- 08T11:53:23.000Z |

**示例**

`JSON` 格式智能体工厂 OpenTrek 发指南

```json
{
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
  }
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |

智能体工厂 OpenTrek 发指南

| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
|---|---|---|
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 数据加工

###### 获取加工任务详情

**接口概述**

**接口调用地址**

GET POP_SDK[SysMethod]:GET POP_SDK[SysUriPattern]:/gatectl/data-engine/api/v2/process/tasks/[taskId] POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:GetDataEngineApiV2ProcessTasksTaskid

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek 发指南

| taskId | Integ er | Path | 是 | 123 | 任务ID |
|---|---|---|---|---|---|

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| id | Integer | 任务ID | 123 |
| name | String | 任务名称 | 自定义蒙牛文本清洗任务 |
| description | String | 任务描述 | 清洗干干净净的蒙牛任务 |
| editState | String | 任务编辑状态 | draft |
| type | String | 任务类型 | pipeline |
| dkeJobId | Integer | DKE作业ID | 231 |
| tplId | Integer | 模版ID | 12 |
| tplName | String | 模版名称 | 数据清洗 |
| tplCode | String | 模版Code | text clean _ |
| tplVersion | String | 模版版本 | v1.0.0 |
| operatorIds | List | 使用算子ID列表 | [12, 13, 14] |
| operators | List | 算子详情 | [] |
| config | Object | 任务配置 | {} |
| creatorId | String | 创建者ID | 1631044****3440 |
| creatorName | String | 创建者用户名 | admin |
| tenantCode | String | 租户Code | sfmboost |

智能体工厂 OpenTrek 发指南

| workspaceCode | String | 工作组Code | default workspace _ |
|---|---|---|---|
| createdAt | String | 创建时间 | 2021-01- 30T12:51:33.028Z |
| updatedAt | String | 更新时间 | 2021-01- 30T12:51:33.028Z |

**示例**

`JSON` 格式

```json
{
  "id": 123,
```

`"name": "`自定义蒙牛文本清洗任务`",` `"description": "`清洗干干净净的蒙牛任务`",`

```json
  "editState": "draft",
  "type": "pipeline",
  "dkeJobId": 231,
  "tplId": 12,
```

`"tplName": "`数据清洗`",`

```json
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
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
|---|---|---|
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 获取加工模版列表

**接口概述**

**接口调用地址**

GET POP_SDK[SysMethod]:GET POP_SDK[SysUriPattern]:/gatectl/data-engine/api/v2/process/templates POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:GetDataEngineApiV2ProcessTemplates

**请求头**

智能体工厂 OpenTrek 发指南

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| keyword | Strin g | Quer y | 否 | 数据清洗 | 搜索关键字 |
| type | Strin g | Quer y | 否 | pipeline | 模版类型 |
| pageNumb er | Integ er | Quer y | 否 | 1 | 列表的页码 |
| pageSize | Integ er | Quer y | 否 | 10 | 每页行数 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|

智能体工厂 OpenTrek 发指南

| templates | List | 模版列表 | [{"id": 128, "code": "text clean", "name": _ "数据清洗", "description": "数据清洗干干净净", "type": "pipeline", "icon": "", "tags": ["text", "LLM"], "version": "v1.0.0", "ownerId": "1631044****3440", "ownerName": "admin", "tenantCode": "sfmboost", "workspaceCode": "default workspace", _ "createdAt": "2021-01- 30T12:51:33.028Z", "updatedAt": "2021- 01- 30T12:51:33.028Z"}] |
|---|---|---|---|
| id | Integer | 模版ID | 128 |
| code | String | 模版Code | text clean _ |
| name | String | 模版名称 | 数据清洗 |
| description | String | 模版描述 | 数据清洗干干净净 |
| type | String | 模版类型 | pipeline |
| icon | String | 模版图标 |  |
| tags | List | 模版标签 | ["text", "LLM"] |

智能体工厂 OpenTrek 发指南

| version | String | 模版版本 | v1.0.0 |
|---|---|---|---|
| ownerId | String | 模版所有者ID | 1631044****3440 |
| ownerName | String | 模版所有者用户名 | admin |
| tenantCode | String | 租户Code | sfmboost |
| workspaceCode | String | 工作组Code | default workspace _ |
| createdAt | String | 创建时间 | 2021-01- 30T12:51:33.028Z |
| updatedAt | String | 更新时间 | 2021-01- 30T12:51:33.028Z |
| pageSize | Integer | 每页行数 | 20 |
| totalCount | Integer | 总数量 | 79 |
| pageNumber | Integer | 当前页码 | 1 |

**示例**

`JSON` 格式智能体工厂 OpenTrek 发指南

```json
{
  "templates": [
    {
      "id": 128,
      "code": "text_clean",
```

`"name": "`数据清洗`",` `"description": "`数据清洗干干净净`",`

```json
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
    }
```

`],`

```json
  "pageSize": 20,
  "totalCount": 79,
  "pageNumber": 1
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |

智能体工厂 OpenTrek 发指南

| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
|---|---|---|
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 新建加工任务

**接口概述**

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/data-engine/api/v2/process/tasks POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostDataEngineApiV2ProcessTasks

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

智能体工厂 OpenTrek 发指南

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| name | Strin g | Body | 是 | 自定义清洗任务 | 任务名称，该参数必填 |
| description | Strin g | Body | 否 | 自定义清洗任务 | 任务描述 |
| type | Strin g | Body | 是 | pipeline | 任务类型，该参数必填 |
| tplId | Integ er | Body | 是 | 12 | 模版ID，该参数必填 |
| tplName | Strin g | Body | 是 | 数据清洗 | 模版名称，该参数必填 |
| tplCode | Strin g | Body | 是 | text clean _ | 模版Code，该参数必填 |
| tplVersion | Strin g | Body | 是 | v1.0.0 | 模版版本，该参数必填 |
| config | Json | Body | 是 | {} | 任务配置，该参数必填 |
| - datasetIm port | Strin g | Body | 否 | sfm://dataset code/subse _ t | 输入数据集，该参数必填 |
| - datasetEx port | Strin g | Body | 否 | sfm://dataset code/subse _ t | 输出数据集，该参数必填 |
| -np | Integ er | Body | 否 | 1 | 计算并行度 |

智能体工厂 OpenTrek 发指南

| -process | Repe atLis t | Body | 否 | [{"word parser offline m _ _ _ apper": {"image ocr": _ false, "save file": false, _ "deep parse": true, _ "table parse": false, _ "equation parse": false, _ "image filter size": _ _ [3,3]}}, {"parser format offline _ _ _ mapper": {"persistent": true, "input feature key": _ _ "word parser", _ "input feature type": _ _ "word parser"}}] _ | pipeline配置，算子执行列表 |
|---|---|---|---|---|---|

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| id | Integer | 任务ID | 123 |

**示例**

`JSON` 格式

```json
{
  "id": 123
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |

智能体工厂 OpenTrek 发指南

| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
|---|---|---|
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 删除加工任务

**接口概述**

**接口调用地址**

DELETE POP_SDK[SysMethod]:DELETE POP_SDK[SysUriPattern]:/gatectl/data-engine/api/v2/process/tasks/[taskId] POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:DeleteDataEngineApiV2ProcessTasksTaskid

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek 发指南

| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
|---|---|---|---|---|---|
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskId | Integ er | Path | 是 | 123 | 任务ID |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |

**示例**

`JSON` 格式

```json
{"success": true}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |

智能体工厂 OpenTrek 发指南

| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
|---|---|---|
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 获取加工任务列表

**接口概述**

**接口调用地址**

GET POP_SDK[SysMethod]:GET POP_SDK[SysUriPattern]:/gatectl/data-engine/api/v2/process/tasks POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:GetDataEngineApiV2ProcessTasks

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek 发指南

| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
|---|---|---|---|---|---|
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| keyword | Strin g | Quer y | 否 | mmlu | 搜索关键字 |
| editState | Strin g | Quer y | 否 | draft | 任务编辑状态 |
| type | Strin g | Quer y | 否 | pipeline | 任务类型 |
| pageNumb er | Integ er | Quer y | 否 | 1 | 列表的页码 |
| pageSize | Integ er | Quer y | 否 | 10 | 每页行数 |
| order | Strin g | Quer y | 否 | DESC | 排序方式 |
| orderBy | Strin g | Quer y | 否 | createdAt | 排序字段 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|

智能体工厂 OpenTrek 发指南

| tasks | List | 任务列表 | [{"id": 123, "name": "自定义清洗任务", "description": "自定义清洗任务", "editState": "draft", "type": "pipeline", "dkeJobId": 231, "tplId": 12, "tplName": "数据清洗", "tplCode": "text clean", _ "tplVersion": "v1.0.0", "creatorId": "1631044****3440", "creatorName": "admin", "tenantCode": "sfmboost", "workspaceCode": "default workspace", _ "createdAt": "2021-01- 30T12:51:33.028Z", "updatedAt": "2021- 01- 30T12:51:33.028Z"}] |
|---|---|---|---|
| id | Integer | 任务ID | 123 |
| name | String | 任务名称 | 自定义清洗任务 |
| description | String | 任务描述 | 自定义清洗任务 |
| editState | String | 任务编辑状态 | draft |
| type | String | 任务类型 | pipeline |
| dkeJobId | Integer | DKE作业ID | 231 |
| tplId | Integer | 模板ID | 12 |
| tplName | String | 模板名称 | 数据清洗 |
| tplCode | String | 模板Code | text clean _ |

智能体工厂 OpenTrek 发指南

| tplVersion | String | 模板版本 | v1.0.0 |
|---|---|---|---|
| creatorId | String | 创建者ID | 1631044****3440 |
| creatorName | String | 创建者用户名 | admin |
| tenantCode | String | 租户Code | sfmboost |
| workspaceCode | String | 工作组Code | default workspace _ |
| createdAt | String | 创建时间 | 2021-01- 30T12:51:33.028Z |
| updatedAt | String | 更新时间 | 2021-01- 30T12:51:33.028Z |
| pageSize | Integer | 每页行数 | 20 |
| totalCount | Integer | 总数量 | 79 |
| pageNumber | Integer | 当前页码 | 1 |

**示例**

`JSON` 格式智能体工厂 OpenTrek 发指南

```json
{
  "tasks": [
    {
      "id": 123,
```

`"name": "`自定义清洗任务`",` `"description": "`自定义清洗任务`",`

```json
      "editState": "draft",
      "type": "pipeline",
      "dkeJobId": 231,
      "tplId": 12,
```

`"tplName": "`数据清洗`",`

```json
      "tplCode": "text_clean",
      "tplVersion": "v1.0.0",
      "creatorId": "1631044****3440",
      "creatorName": "admin",
      "tenantCode": "sfmboost",
      "workspaceCode": "default_workspace",
      "createdAt": "2021-01-30T12:51:33.028Z",
      "updatedAt": "2021-01-30T12:51:33.028Z"
    }
```

`],`

```json
  "pageSize": 20,
  "totalCount": 79,
  "pageNumber": 1
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |

智能体工厂 OpenTrek 发指南

| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
|---|---|---|
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 获取算子列表

**接口概述**

**接口调用地址**

GET POP_SDK[SysMethod]:GET POP_SDK[SysUriPattern]:/gatectl/data-engine/api/v2/operators POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:GetDataEngineApiV2Operators

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |

智能体工厂 OpenTrek 发指南

| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |
|---|---|---|---|---|---|

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| keyword | Strin g | Quer y | 否 | text | 搜索关键字 |
| type | Strin g | Quer y | 否 | Mapper | 算子类型 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| operators | List | 算子列表 |  |
| id | Integer | 算子ID | 1203 |
| name | String | 算子名称 | 文本增强 |
| code | String | 算子Code | opentrek text enhanc _ _ ement mapper _ |
| description | String | 算子描述 | 用来增强文本 |
| type | String | 算子类型 | Mapper |
| modalities | List | 支持的数据类型 | ["text"] |
| devices | List | 支持的设备类型 | ["CPU", "GPU"] |
| tags | List | 标签 | ["LLM"] |

智能体工厂 OpenTrek 发指南

| updateFeatures | List | 算子变更字段 | [{"columnName": "problem", "columnType": "string", "columnPhysicalType": "varchar", "columnComment": "用户提问"}, {"columnName": "param:solution", "columnType": "string", "columnPhysicalType": "varchar", "columnComment": "LLM回答"}] |
|---|---|---|---|
| columnName | String | 字段名称 | problem |
| columnType | String | 字段类型 | String |
| columnPhysicalType | String | 字段物理类型 | varchar |
| columnComment | String | 字段描述 | 用户提问 |
| params | List | 参数信息 | [{"type": "literal", "required": true, "key": "model", "defaultValue": "qwen- max", "desc": "Model to use for data generation.", "options": ["qwen- max", "qwen-vl"]}] |
| type | String | 参数类型 | literal |
| required | Boolean | 是否必填 | true |
| key | String | 参数Key | model |
| defaultValue | String | 默认值 | qwen-max |
| desc | String | 参数描述 | Model to use for data generation. |
| options | List | 可选值 | ["qwen-max", "qwen- vl"] |

智能体工厂 OpenTrek 发指南

| components | List | 前端组件配置 | [{"type": "Select", "required": true, "label": "模型名称", "key": "model", "desc": "对于当前表单项的简单描述", "defaultValue": "qwen-max", "options": [{"label": "通义千问", "value": "qwen-max", ...}]}] |
|---|---|---|---|
| type | String | 组件类型 | Select |
| required | Boolean | 是否必填 | true |
| label | String | 组件标签 | 模型名称 |
| key | String | 参数Key | model |
| desc | String | 组件描述 | 对于当前表单项的简单描述 |
| defaultValue | String | 默认值 | qwen-max |
| options | List | 选项列表 | [{"label": "通义千问", "value": "qwen-max", "desc": "通义千问是一个专门响应人类指令的大模型..."}] |
| label | String | 选项标签 | 通义千问 |
| value | String | 选项值 | qwen-max |
| desc | String | 选项描述 | 通义千问是一个专门响应人类指令的大模型，是一个灵活多变的全能型选手... |
| extra | Object | 扩展配置 | {"min": 0, "max": 10, "step": 1, "mode": "multiple"} |
| min | Integer | 最小值 | 0 |
| max | Integer | 最大值 | 10 |

智能体工厂 OpenTrek 发指南

| step | Integer | 步长 | 1 |
|---|---|---|---|
| mode | String | 模式 | multiple |
| pageSize | Integer | 每页行数 | 20 |
| totalCount | Integer | 总数量 | 79 |
| pageNumber | Integer | 当前页码 | 1 |

**示例**

`JSON` 格式

```json
{
  "operators": [
    {
      "id": 1203,
```

`"name": "`文本增强`",`

```json
      "code": "opentrek_text_enhancement_mapper",
```

`"description": "`用来增强文本`",`

```json
      "type": "Mapper",
      "modalities": ["text"],
      "devices": ["CPU", "GPU"],
      "tags": ["LLM"],
      "updateFeatures": [
        {
          "columnName": "problem",
          "columnType": "string",
          "columnPhysicalType": "varchar",
```

`"columnComment": "`用户提问"

```json
        },
        {
          "columnName": "param:solution",
          "columnType": "string",
          "columnPhysicalType": "varchar",
          "columnComment": "LLM回答"
        }
```

`],`

```json
      "params": [
        {
          "type": "literal",
          "required": true,
          "key": "model",
          "defaultValue": "qwen-max",
          "desc": "Model to use for data generation.",
          "options": ["qwen-max", "qwen-vl"]
        }
```

`],`

```json
      "components": [
```

智能体工厂 OpenTrek 发指南

```json
        {
          "type": "Select",
          "required": true,
```

`"label": "`模型名称`",`

```json
          "key": "model",
```

`"desc": "`对于当前表单项的简单描述`",`

```json
          "defaultValue": "qwen-max",
          "options": [
            {
```

`"label": "`通义千问`",`

```json
              "value": "qwen-max",
```

`"desc": "`通义千问是一个专门响应人类指令的大模型，是一个灵活多变的全能型选手，能够写邮件、周报、提纲，创作诗歌、小说、剧本、`coding`、制表、甚至角色扮演。"

```
            },
            {
```

`"label": "`通义千问`VL",`

```json
              "value": "qwen-vl",
```

`"desc": "`通义千问`VL`（`qwen-vl`）是阿里云研发的大规模视觉语言模型，可以以图像、文本、检测框作为输入，并以文本和检测框作为输出，支持中文多模态对话及多图对话。"

```
            }
```

`],`

```json
          "extra": {
            "min": 0,
            "max": 10,
            "step": 1,
            "mode": "multiple"
          }
        }
```

]

```
    }
```

`],`

```json
  "pageSize": 20,
  "totalCount": 79,
  "pageNumber": 1
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
|---|---|---|
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 获取任务运行实例信息

**接口概述**

**接口调用地址**

GET POP_SDK[SysMethod]:GET POP_SDK[SysUriPattern]:/gatectl/data-engine/api/v2/process/tasks/[taskId]/instances POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:GetDataEngineApiV2ProcessTasksTaskidInstances

**请求头**

智能体工厂 OpenTrek 发指南

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskId | Integ er | Path | 是 | 100 | 任务ID |
| runId | Integ er | Quer y | 是 | 1001 | 任务运行ID |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| data | List | 返回数据列表 | [{"id":667,"tenantCod e":"baseline","flowId": 555,"taskId":556,"task Code":"job 25204e0c2 _ 33c11f0aac656db6f3d 4393","taskName":"【 待验证】文本-数据解析- CHUNK 切分"...}] |
| id | Integer | 实例ID | 667 |
| tenantCode | String | 租户Code | baseline |
| flowId | Integer | 流程ID | 555 |
| taskId | Integer | 任务ID | 556 |
| taskCode | String | 任务Code | job 25204e0c233c11f _ 0aac656db6f3d4393 |

智能体工厂 OpenTrek 发指南

| taskName | String | 任务名称 | 【待验证】文本-数据解析-CHUNK 切分 |
|---|---|---|---|
| instanceCode | String | 实例Code | 556.250427.15:50.W6 hwdGl7j.250427 |
| instanceType | Integer | 实例类型 | 2 |
| duration | String | 执行时长 | 3s |
| taskVersion | String | 任务版本 | 1745740172030 |
| execType | String | 执行类型 | KN PROC _ |
| parents | Object | 父实例 | null |
| children | Object | 子实例 | null |
| status | Integer | 实例状态 (1:待执行, 2:执行中, 3:成功, 4:失败, 5: 超时, 6:排队中, 7:异常) | 4 |
| substatus | Integer | 子状态 | -1 |
| retry | Integer | 重试次数 | 0 |
| revision | Integer | 修订版本 | 0 |
| bizdate | String | 业务日期 | 2025-04-26 15:50:00 |
| plandate | String | 计划日期 | 2025-04-27 15:50:00 |
| execdate | String | 执行日期 | null |
| gmtCreate | String | 创建时间 | 2025-04-27 15:50:42 |
| gmtStart | String | 开始时间 | 2025-04-27 15:50:43 |
| gmtEnd | String | 结束时间 | 2025-04-27 15:50:46 |

智能体工厂 OpenTrek 发指南

| gmtHeartbeat | String | 心跳时间 | 2025-04-27 15:50:48 |
|---|---|---|---|
| createdBy | String | 创建人 | qingfu.zmq |
| rerun | Boolean | 是否重跑 | false |
| retryStrategy | Object | 重试策略 | null |
| priority | Integer | 优先级 | 10 |
| importDataset | Object | 导入数据集 | null |
| exportDataset | Object | 导出数据集 | null |
| pageSize | Integer | 分页大小 | 20 |
| totalCount | Integer | 总条数 | 79 |
| pageNumber | Integer | 当前页码 | 1 |

**示例**

`JSON` 格式智能体工厂 OpenTrek 发指南

```json
{
  "success": true,
  "data": [
    {
      "id": 667,
      "tenantCode": "baseline",
      "flowId": 555,
      "taskId": 556,
      "taskCode": "job_25204e0c233c11f0aac656db6f3d4393",
```

`"taskName": "`【待验证】文本-数据解析`-CHUNK` 切分`",`

```json
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
    }
```

]

```
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
|---|---|---|
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 运行加工任务

**接口概述**

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/data-engine/api/v2/process/tasks/[taskId]/run POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostDataEngineApiV2ProcessTasksTaskidRun 智能体工厂 OpenTrek 发指南

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| xlmGroupC ode | Strin g | Body | 是 | xxxx | 资源池Code，该参数必填 |
| specs | Json | Body | 是 | {"name": "CPU", "data": {"vCPU": 1, "Mem": "1GB"}} | 规格配置，该参数必填 |
| -vCPU | Integ er | Body | 否 | 1 | vCPU数量，该参数必填 |
| -Mem | Strin g | Body | 否 | 1GB | 内存大小，该参数必填 |
| -np | Integ er | Body | 否 | 1 | 并行度，该参数必填 |
| -GPU | Json | Body | 否 | {"NVIDIA-A100- SXM80GB": 1} | GPU规格，该参数必填 |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | Object | 返回数据 |  |
| id | Integer | 任务运行ID | 2357 |

智能体工厂 OpenTrek 发指南

**示例**

`JSON` 格式

```json
{
  "success": true,
  "data": {"id": 2357}
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |

| gent Dev 开发指南·Agent Dev开发指南 |  | 智能体工厂 OpenTre |
|---|---|---|

| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
|---|---|---|
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 发布任务

###### 发布任务

**接口概述**

发布任务[PublishProcessTask]

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/data-engine/api/v2/process/tasks/[taskId]/publish POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostDataEngineApiV2ProcessTasksTaskidPublish

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，改参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskId | Integ er | Path | 是 | 123 | 任务ID |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|

智能体工厂 OpenTrek 发指南

| success | Boolean | 是否成功 | true |
|---|---|---|---|

**示例**

`JSON` 格式

```json
{"success": true}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |

| gent Dev 开发指南·Agent Dev开发指南 |  | 智能体工厂 OpenTre |
|---|---|---|

| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
|---|---|---|
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 下线任务

###### 下线任务

**接口概述**

下线任务[UnpublishProcessTask]

**接口调用地址**

POST POP_SDK[SysMethod]:POST POP_SDK[SysUriPattern]:/gatectl/data-engine/api/v2/process/tasks/[taskId]/unpublish POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PostDataEngineApiV2ProcessTasksTaskidUnpublish

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskId | Integ er | Path | 是 | 123 | 任务ID |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|

智能体工厂 OpenTrek 发指南

| success | Boolean | 是否成功 | true |
|---|---|---|---|

**示例**

`JSON` 格式

```json
{"success": true}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |

| gent Dev 开发指南·Agent Dev开发指南 |  | 智能体工厂 OpenTre |
|---|---|---|

| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
|---|---|---|
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 获取加工模版详情

**接口概述**

**接口调用地址**

GET POP_SDK[SysMethod]:GET POP_SDK[SysUriPattern]:/gatectl/data-engine/api/v2/process/templates/[code] POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:GetDataEngineApiV2ProcessTemplatesCode

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| code | Strin g | Path | 是 | mmlu no train _ _ | 模版Code |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|

智能体工厂 OpenTrek 发指南

| id | Integer | 模版ID | 128 |
|---|---|---|---|
| code | String | 模版Code | text clean _ |
| name | String | 模版名称 | 数据清洗 |
| description | String | 模版描述 | 数据清洗 |
| type | String | 模版类型 | pipeline |
| icon | String | 模版图标 |  |
| tags | List | 模版标签 | ["text", "LLM"] |
| version | String | 模版版本 | v1.0.0 |
| operators | List | 算子列表 | [{}] |
| config | Object | 模版配置 | {} |
| ownerId | String | 模版所有者ID | 1631044****3440 |
| ownerName | String | 模版所有者用户名 | admin |
| tenantCode | String | 租户Code | sfmboost |
| workspaceCode | String | 工作组Code | default workspace _ |
| createdAt | String | 创建时间 | 2021-01- 30T12:51:33.028Z |
| updatedAt | String | 更新时间 | 2021-01- 30T12:51:33.028Z |

**示例**

`JSON` 格式智能体工厂 OpenTrek 发指南

```json
{
  "id": 128,
  "code": "text_clean",
```

`"name": "`数据清洗`",` `"description": "`数据清洗`",`

```json
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
}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |

智能体工厂 OpenTrek 发指南

| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
|---|---|---|
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 更新加工任务

**接口概述**

**接口调用地址**

PUT POP_SDK[SysMethod]:PUT POP_SDK[SysUriPattern]:/gatectl/data-engine/api/v2/process/tasks POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:PutDataEngineApiV2ProcessTasks

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

智能体工厂 OpenTrek 发指南

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Integ er | Body | 是 | 123 | 任务ID，该参数必填 |
| name | Strin g | Body | 是 | 自定义清洗任务 | 任务名称，该参数必填 |
| description | Strin g | Body | 否 | 自定义清洗任务 | 任务描述 |
| type | Strin g | Body | 是 | pipeline | 任务类型，该参数必填 |
| tplId | Integ er | Body | 是 | 12 | 模版ID，该参数必填 |
| tplName | Strin g | Body | 是 | 数据清洗 | 模版名称，该参数必填 |
| tplCode | Strin g | Body | 是 | text clean _ | 模版Code，该参数必填 |
| tplVersion | Strin g | Body | 是 | v1.0.0 | 模版版本，该参数必填 |
| config | Json | Body | 是 | {} | 任务配置，该参数必填 |
| - datasetIm port | Strin g | Body | 否 | sfm://dataset code/subse _ t | 输入数据集，该参数必填 |
| - datasetEx port | Strin g | Body | 否 | sfm://dataset code/subse _ t | 输出数据集，该参数必填 |
| -np | Integ er | Body | 否 | 1 | 计算并行度 |

智能体工厂 OpenTrek 发指南

| -process | Repe atLis t | Body | 否 | [{"word parser offline m _ _ _ apper": {"image ocr": _ false, "save file": false, _ "deep parse": true, _ "table parse": false, _ "equation parse": false, _ "image filter size": _ _ [3,3]}}, {"parser format offline _ _ _ mapper": {"persistent": true, "input feature key": _ _ "word parser", _ "input feature type": _ _ "word parser"}}] _ | pipeline配置，算子执行列表 |
|---|---|---|---|---|---|

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |

**示例**

`JSON` 格式

```
{success: true}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |

智能体工厂 OpenTrek 发指南

| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
|---|---|---|
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

###### 获取任务实例日志

**接口概述**

**接口调用地址**

GET POP_SDK[SysMethod]:GET POP_SDK[SysUriPattern]:/gatectl/dataengine/api/v2/process/tasks/instances/[instanceCode]/log POP_SDK[SysDomain]:见产品API文档页详情 POP_SDK[Action]:GetDataEngineApiV2ProcessTasksInstancesInstancecodeLog

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek 发指南

| x-sfm- workspace code | Strin g | Hea der | 是 | your workspace code _ _ | 目标工作空间，该参数必填 |
|---|---|---|---|---|---|
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type，该参数必填 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| instanceCo de | Strin g | Path | 是 | 1460.250701.17:34.JMR7 CCD57.250701 | 任务实例code |

**返回参数**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| log | String | 任务实例日志 | 2025-07-01 17:59:52.301073 +0800 CST --------------- ------------------- 2025- 07-01 18:05:30.643637 +0800 CST |

**示例**

`JSON` 格式

```json
{"log": "2025-07-01 17:59:52.301073 +0800 CST————————————2025-07-01 18:05:30.643637 +08 00 CST"}
```

**文档补充说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败,APP KEY 已过期 _ |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
|---|---|---|
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败,用户角色不匹配 |

### 应用集成类

平台租户区相关接口服务

#### 接口文档

##### 智能体

###### 创建session

**接口概述**

智能体工厂 OpenTrek 发指南您可以通过接口创建一个全新的agent会话，可以通过查看请求示例，点击 curl命令示例右侧的调试按钮验证业务接口调用效果。

**前提条件（查看APP_KEY）**

先进入菜单[主页->点击头像->APP_KEY]创建APP_KEY

**接口调用地址**

POST http://${endpoint}/gateway/agent/api/createSession ${endpoint}见产品API文档页面详情

**入参描述**

Header传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | 是 | Content-Type | application/json |

Body传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| agentCode | string | 是 | 智能体编码 | e36a0ab1-b673- 49d0-9534- 1480a147c691 |
| agentVersion | string | 否 | 智能体版本 | 1706863858334 |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | boolean | 是否成功 | true |
| data | object | 返回数据 | {"uniqueCode":"4bcaa 882-9c54-4b78-9057- 54db58591b5b"} |

**请求示例**

智能体工厂 OpenTrek 发指南

```json
curl -X 'POST' http://${endpoint}/gateway/agent/api/createSession \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -d '{
    "agentCode": "",
    "agentVersion": ""
}'
```

**响应示例**

```json
{
 "success": true,
 "data": {
  "uniqueCode": "4bcaa882-9c54-4b78-9057-54db58591b5b"
 },
 "errorCode": null,
 "errorMsg": null
}
```

**状态码说明**

网关异常状态码说明

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY E _ XPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 403 | GATEWAY APP PATH NOT FOUN _ D! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT REGI _ STER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSP ACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
|---|---|---|
| 401 | GATEWAY AUTH USER NOT MA _ TCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE W _ _ RONG! | 鉴权失败,用户角色不匹配 |
| 404 | GATEWAY ROUTE URL NOT FOU ND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应 |

###### 发起agent调用

**接口概述**

您可以通过接口在已有会话的基础上对agent进行提问，可以通过查看请求示例，点击 curl命令示例右侧的调试按钮验证业务接口调用效果。

**前提条件（查看APP_KEY）**

先进入菜单[主页->点击头像->APP_KEY]创建APP_KEY

**接口调用地址**

POST http://${endpoint}/gateway/agent/api/run ${endpoint}见产品API文档页面详情

**入参描述**

Header传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | 是 | Content-Type | application/json |

Body传参智能体工厂 OpenTrek 发指南

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| sessionId | String | 是 | sessionId | bd962db7-b1c8- 4466-a2cc- 41b9b67cd94b 创建session接口的返回值uniqueCode |
| stream | Boolean | 是 | 是否流式 | true |
| delta | Boolean | 是 | 当stream=true,控制是否不追加新文本 | true 默认每次输出新内容,不包含前序输出的文本 |
| trace | Boolean | 否 | 当trace=true,控制是否返回trace记录 | false 默认不返回 trace记录 |
| message | object | 是 | 请求消息体 | {"text":"帮我订一张明天从上海去苏黎世的机票","metadata": {}, "attachments": [{"url":"","name": ""}]} |
| text | string | 是 | 对话输入 | 帮我订一张明天从上海去苏黎世的机票 |
| metadata | Map | 否 | 扩展信息 | {} |
| attachments | List<Object> | 否 | 附件信息 | [] |
| url | string | 是 | 附件地址 | {} |
| name | string | 否 | 附件名称 | {} |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|

智能体工厂 OpenTrek 发指南

| object | string | 数据类型 | message.delta 输出文本块 thought.delta 思考过程块 error 错误信息 |
|---|---|---|---|
| role | string | 角色 | assistant |
| content | object | 数据内容 | object=message.delta 场景 : {"type":"text","text": {"value":"智能体回答内容增量"}} object=thought.delta 场景 : {"type":"text","data":" 思考内容增量"} object=error场景 {"errorMsg": "错误信息内容"} |
| metadata | object | 扩展字段 | {"key":"value"} |
| end | Boolean | 流式 (object=message.delt a)场景标记文本输出是否结束 | false\|true |
| sessionId | string | 当前会话ID | - |
| requestId | string | 当前运行的请求ID | - |
| id | object | 流式消息的业务唯一ID | 思考内容唯一ID\|最终答案信息的唯一ID; 思考内容支持在问答结束前输出多个,业务侧有多流输出的场景,可以进一步根据自定义的id前缀来区分呈现 |
| success | Boolean | 非流式-业务是否成功 | true |
| data | object | 非流式-业务响应 | {} |

智能体工厂 OpenTrek 发指南

| message | object | 非流式-输出文本响应 | {} |
|---|---|---|---|
| role | string | 角色 | assistant |
| metadata | object | 扩展字段 | {"key":"value"} |
| content | List<Object> | 输出内容 | 包含type、content |
| type | String | 输出内容类型 | text\|image |
| text | JSONObject | type=text 场景的输出结构 | {} |
| value | String | 输出文本 | 你好！有什么我能帮助你的吗？ |
| image | JSONObject | type=image 场景的输出结构 | {} |
| url | String | 输出图片的地址 |  |
| thoughts | object | 非流式-输出思考响应 | {} |
| role | string | 角色 | assistant |
| content | object | 输出内容 |  |
| data | String | 输出文本 |  |
| type | String | 输出内容类型,目前是常量 text | text |
| errorCode | Boolean | 非流式-业务错误码 | true |
| errorMsg | Boolean | 非流式-业务错误描述 | true |

**请求示例**

智能体工厂 OpenTrek 发指南

```json
curl -X 'POST' http://${endpoint}/gateway/agent/api/run \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -d '{
    "stream":true,
    "delta":true,
    "sessionId": "7af650e7-ed57-498d-8081-fe1dea5361fa",
    "message":{
```

`"text":"`帮我订一张明天从上海去苏黎世的机票`",`

```json
        "metadata":{},
        "attachments":[]
    }
}'
```

**响应示例**

**流式输出**

智能体工厂 OpenTrek 发指南

```json
data: {"object": "message.delta","end":false,"role": "assistant","sessionId":"de454297c547-440f-ae55-057a83a2d121","content": [{"type":"text","text": {"value": "智能体回答内容增量"}}],"metadata": {"key": "value"}} data: {"object": "thought.delta","role": "assistant","sessionId":"de454297-c547-440f-ae 55-057a83a2d121","content": {"type":"text","data":"思考内容增量"}} data: {"object": "error","role": "assistant","sessionId":"de454297-c547-440f-ae55-057a8 3a2d121","content": {"errorMsg": "错误信息内容"}} data:{"content":{"data":"您好","type":"text"},"id":"323ef0f2f57e445fbec343f62441c608","object":"thought.delta"} data:{"content": {"data":"！","type":"text"},"id":"323ef0f2f57e445fbec343f62441c608","object":"thought.delt "} data:{"content":{"data":"请问","type":"text"},"id":"323ef0f2f57e445fbec343f62441c608","object":"thought.delta"}
```

`data:{"content":{"data":"`有什么可以帮助您

```json
的？","type":"text"},"id":"323ef0f2f57e445fbec343f62441c608","object":"thought.delta"} data:{"content": {"data":"","type":"text"},"id":"323ef0f2f57e445fbec343f62441c608","object":"thought.delta data:{"content":[{"text":{"value":"您好"},"type":"text"}],"end":false,"gmtCreate":"2024- 09-19 11:52:56.012","id":"9b0a21677f4a4512935c0e96977f292b","metadata": {},"requestId":"6d511a54-d95f-419c-9d34- 02e86ea050e4","role":"assistant","sessionId":"7af650e7-ed57-498d-8081fe1dea5361fa","useage":{"uiTaskId":"23ce3bf3-5248-4293-8326bdb7f452a092"},"object":"message.delta"} data:{"content":[{"text":{"value":"！"},"type":"text"}],"end":false,"gmtCreate":"2024-0 9-19 11:52:56.012","id":"9b0a21677f4a4512935c0e96977f292b","metadata": {},"requestId":"6d511a54-d95f-419c-9d34- 02e86ea050e4","role":"assistant","sessionId":"7af650e7-ed57-498d-8081fe1dea5361fa","useage":{"uiTaskId":"23ce3bf3-5248-4293-8326bdb7f452a092"},"object":"message.delta"} data:{"content":[{"text":{"value":"请问"},"type":"text"}],"end":false,"gmtCreate":"2024- 09-19 11:52:56.012","id":"9b0a21677f4a4512935c0e96977f292b","metadata": {},"requestId":"6d511a54-d95f-419c-9d34- 02e86ea050e4","role":"assistant","sessionId":"7af650e7-ed57-498d-8081fe1dea5361fa","useage":{"uiTaskId":"23ce3bf3-5248-4293-8326bdb7f452a092"},"object":"message.delta"}
```

`data:{"content":[{"text":{"value":"`有什么可以帮助您

```
的？"},"type":"text"}],"end":false,"gmtCreate":"2024-09-19 11:52:56.012","id":"9b0a21677f4a4512935c0e96977f292b","metadata": {},"requestId":"6d511a54-d95f-419c-9d34- 02e86ea050e4","role":"assistant","sessionId":"7af650e7-ed57-498d-8081fe1dea5361fa","useage":{"uiTaskId":"23ce3bf3-5248-4293-8326bdb7f452a092"},"object":"message.delta"} data:{"content":[{"text":{"value":""},"type":"text"}],"end":true,"gmtCreate":"2024-09-1 9 11:52:56.012","id":"9b0a21677f4a4512935c0e96977f292b","metadata": {},"requestId":"6d511a54-d95f-419c-9d34- 02e86ea050e4","role":"assistant","sessionId":"7af650e7-ed57-498d-8081fe1dea5361fa","useage":{"uiTaskId":"23ce3bf3-5248-4293-8326bdb7f452a092"},"object":"message.delta"}
```

智能体工厂 OpenTrek 发指南

**响应示例**

**非流式输出**

```json
{
 "success": true,
 "data": {
  "message": {
   "role": "assistant",
   "content": [{
    "type": "text",
    "text": {
```

`"value": "`你好！有什么我能帮助你的吗？"

```json
    }
   },{
    "type": "image",
    "image": {
     "url": ""
    }
   }],
   "metadata": null
  },
  "thoughts": [{
    "role": "assistant",
    "content": {
     "type": "text",
     "data": ""
    }
   }
```

`],`

```json
  "error": null
 },
 "errorCode": null,
 "errorMsg": null
}
```

**状态码说明**

网关异常状态码说明

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY E _ XPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 403 | GATEWAY APP PATH NOT FOUN _ D! | 无效的服务调用路径 |

智能体工厂 OpenTrek 发指南

| 403 | GATEWAY APP PATH NOT REGI _ STER! | 当前服务调用路径未注册 |
|---|---|---|
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSP ACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT MA _ TCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE W _ _ RONG! | 鉴权失败,用户角色不匹配 |
| 404 | GATEWAY ROUTE URL NOT FOU ND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应 |

###### 终止session

**接口概述**

您可以通过调用该接口实现会话中断，可以通过查看请求示例，点击 curl命令示例右侧的调试按钮验证业务接口调用效果。

**前提条件（查看APP_KEY）**

先进入菜单[主页->点击头像->APP_KEY]创建APP_KEY

**接口调用地址**

POST http://${endpoint}/gateway/agent/api/clearSession ${endpoint}见产品API文档页面详情

**入参描述**

Header传参智能体工厂 OpenTrek 发指南

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | 是 | Content-Type | application/json |

Body传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| sessionId | string | 是 | 会话ID | de454297-c547- 440f-ae55- 057a83a2d121 创建session接口的返回值uniqueCode |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | boolean | 是否成功 | true |

**请求示例**

```json
curl -X 'POST' http://${endpoint}/gateway/agent/api/clearSession \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -d '{
    "sessionId": "de454297-c547-440f-ae55-057a83a2d121"
}'
```

**响应示例**

```json
{
  "success": true
}
```

**状态码说明**

网关异常状态码说明

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
|---|---|---|
| 401 | GATEWAY APP KEY ALREADY E _ XPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 403 | GATEWAY APP PATH NOT FOUN _ D! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT REGI _ STER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSP ACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT MA _ TCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE W _ _ RONG! | 鉴权失败,用户角色不匹配 |
| 404 | GATEWAY ROUTE URL NOT FOU ND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应 |

###### 删除session

**接口概述**

您可以通过调用该接口实现会话以及相关过程数据永久删除

**前提条件（查看APP_KEY）**

智能体工厂 OpenTrek 发指南先进入菜单[主页->点击头像->APP_KEY]创建APP_KEY

**接口调用地址**

POST http://${endpoint}/gateway/agent/api/deleteSession ${endpoint}见产品API文档页面详情

**入参描述**

Header传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | 是 | Content-Type | application/json |

Body传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| sessionId | string | 是 | 会话ID | de454297-c547- 440f-ae55- 057a83a2d121 创建session接口的返回值uniqueCode |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | boolean | 服务是否成功 | true |
| data | boolean | 业务是否成功 | true |

**请求示例**

```bash
curl -X 'POST' http://${endpoint}/gateway/agent/api/deleteSession \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -d '{ "sessionId": "de454297-c547-440f-ae55-057a83a2d121" }'
```

**响应示例**

```json
{
  "success": true ,"data": true
}
```

智能体工厂 OpenTrek 发指南

**状态码说明**

网关异常状态码说明

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY E _ XPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 403 | GATEWAY APP PATH NOT FOUN _ D! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT REGI _ STER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSP ACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT MA _ TCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE W _ _ RONG! | 鉴权失败,用户角色不匹配 |
| 404 | GATEWAY ROUTE URL NOT FOU ND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接 |

智能体工厂 OpenTrek 发指南

| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应 |
|---|---|---|

###### 工具异步回调

**接口概述**

您可以通过调用该接口实现在工具箱中注册异步API工具，当智能体执行过程中调用您注册工具时会在 header(key=idx-agent-task-id)中下发任务唯一标识，在您执行完成任务后，可以通过这个异步回调的接口完成工具调用

**前提条件（查看APP_KEY）**

先进入菜单[主页->点击头像->APP_KEY]创建APP_KEY

**接口调用地址**

POST http://${endpoint}/gateway/agent/api/taskFinishNotice ${endpoint}见产品API文档页面详情

**入参描述**

Header传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | 是 | Content-Type | application/json |

Body传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| success | boolean | 是 | 是否成功 | true |
| taskId | string | 是 | 任务id | de454297-c547- 440f-ae55- 057a83a2d121 调用工具 header(key=idx- agent-task-id)的值 |
| data | string | 是 | 任务结果 | 必须是json字符串格式,例如： {"reslut":"一步接口调用成功"} |

智能体工厂 OpenTrek 发指南

| errorCode | string | 否 | 错误信息code | 错误信息code |
|---|---|---|---|---|
| errorMsg | string | 否 | 错误信息 | 错误信息 |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | boolean | 是否成功 | true |

**请求示例**

```json
curl -X 'POST' http://${endpoint}/gateway/agent/api/taskFinishNotice \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -d '{
    "taskId": "de454297-c547-440f-ae55-057a83a2d121"
  ,"success": true
```

`,"data": "{"reslut":"`一步接口调用成功`"}"`

```
 }'
```

**响应示例**

```json
{
  "success": true
}
```

**状态码说明**

网关异常状态码说明

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY E _ XPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 403 | GATEWAY APP PATH NOT FOUN _ D! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT REGI _ STER! | 当前服务调用路径未注册 |

智能体工厂 OpenTrek 发指南

| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
|---|---|---|
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSP ACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT MA _ TCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE W _ _ RONG! | 鉴权失败,用户角色不匹配 |
| 404 | GATEWAY ROUTE URL NOT FOU ND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应 |

###### 调用结果反馈

**接口概述**

您可以针对Agent单次执行的结果进行反馈, 也可以针对本次执行的某个任务进行反馈

**前提条件（查看APP_KEY）**

先进入菜单[主页->点击头像->APP_KEY]创建APP_KEY

**接口调用地址**

POST http://${endpoint}/gateway/agent/api/feedback ${endpoint}见产品API文档页面详情

**入参描述**

Header传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|

智能体工厂 OpenTrek 发指南

| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
|---|---|---|---|---|
| Content-Type | String | 是 | Content-Type | application/json |

Body传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| sessionId | string | 是 | 会话ID |  |
| requestId | string | 是 | 请求ID |  |
| taskId | string | 是 | 任务ID |  |
| uniqueCode | string | 否 | 唯一ID, 更新反馈信息时传入 |  |
| subject | string | 是 | 反馈对象 | REQUEST-针对单次run的结果输出进行反馈, TASK-针对本次run中执行的某个任务进行反馈 |
| provider | object | 是 | 反馈者 |  |
| source | string | 是 | 反馈者来源 | USER-用户, AUTO EVALUATI _ ON-评测中心 |
| extendInfo | object | 否 | 反馈者扩展信息 |  |
| vote | string | 是 | 反馈结果 | LIKE-点赞, DISLIKE-点踩, NEUTRAL-中立 |
| extCommentsInfo | object | 否 | 反馈结果扩展信息 |  |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|

智能体工厂 OpenTrek 发指南

| success | boolean | 是否成功 |  |
|---|---|---|---|
| data | object | 反馈信息 |  |
| sessionId | string | 会话ID |  |
| requestId | string | 请求ID |  |
| taskId | string | 任务ID |  |
| uniqueCode | string | 唯一ID |  |
| subject | string | 反馈对象 | REQUEST-针对单次run 的结果输出进行反馈, TASK-针对本次run中执行的某个任务进行反馈 |
| provider | object | 反馈者 |  |
| source | string | 反馈者来源 | USER-用户, AUTO EVALUATION-评 _ 测中心 |
| extendInfo | object | 反馈者扩展信息 |  |
| vote | string | 反馈结果 | LIKE-点赞, DISLIKE-点踩, NEUTRAL-中立 |
| extCommentsInfo | object | 反馈结果扩展信息 |  |
| errorCode | string | 错误码 |  |
| errorMsg | string | 错误码 |  |

**请求示例**

智能体工厂 OpenTrek 发指南

```json
curl --location --request POST 'http://${endpoint}/gateway/agent/api/feedback' \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -d '{
    "sessionId": "87302f04-7617-41e4-b4c9-9028c3341dcg",
    "requestId": "e359512f-ba3a-46a7-b412-882d7e9f8b32",
    "taskId": "61e60082-690c-4548-a7ef-28d1ff6bb0f9",
    "subject": "TASK",
    "provider": {
        "source": "USER",
        "extendInfo": {}
    },
    "vote": "LIKE",
    "extCommentsInfo": {
        "comment": "123"
    }
}'
```

**响应示例**

```json
{
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
    },
    "vote": "LIKE",
    "extCommentsInfo": {
      "comment": "123"
    }
  },
  "errorCode": null,
  "errorMsg": null
}
```

**状态码说明**

网关异常状态码说明

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
|---|---|---|
| 401 | GATEWAY APP KEY ALREADY E _ XPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 403 | GATEWAY APP PATH NOT FOUN _ D! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT REGI _ STER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSP ACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT MA _ TCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE W _ _ RONG! | 鉴权失败,用户角色不匹配 |
| 404 | GATEWAY ROUTE URL NOT FOU ND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应 |

##### TrekAgent

###### 创建session

智能体工厂 OpenTrek 发指南

**接口概述**

创建TrekAgent会话，返回任务ID和会话ID。调用顺序第1步：调用本接口拿到taskId和sessionId。

**前提条件**

先进入菜单[主页->点击头像->APP_KEY]创建APP_KEY template参数必填；当template为TrekAgent时，relationCode必填。

**接口调用地址**

| POST http://${endpoint}/sfm-agent-studio/sfm-api- |  |
|---|---|

**入参描述**

**Header传参**

| 字段 | 数据类型 | 描述 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | 是 | Content-Type | application/json |

**Body传参**

| 字段 | 数据类型 | 描述 | 描述 | 示例 |
|---|---|---|---|---|
| template | string | 是 | 方案模板类型 | TrekClaw |
| relationCode | string | 是 | 关联编码 | 关联编码, 格式为 [TrekAgent智能体编码] [TrekAgent _ 智能体版本编码] |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | boolean | 是否成功 | true |
| data | object | 返回数据 | {"result":true,"taskId": "xxx","sessionId":"xxx" } |
| result | string | 结果 | true |

智能体工厂 OpenTrek 发指南

| taskId | string | 任务ID | 4bcaa882-9c54-4b78- 9057-54db58591b5b |
|---|---|---|---|
| sessionId | string | 会话ID | de454297-c547-440f- ae55-057a83a2d121 |
| errorCode | string | 错误码 |  |
| errorMsg | string | 错误信息 |  |

**请求示例**

```json
curl -X 'POST' http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/agent/auto/new/session/create \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -d '{
 "template": "TrekAgent",
 "relationCode": "relationCode123"
}'
```

**响应示例**

非流式输出

```json
{
  "success": true,
  "data": {
    "result": true,
    "taskId": "4bcaa882-9c54-4b78-9057-54db58591b5b",
    "sessionId": "de454297-c547-440f-ae55-057a83a2d121"
  },
  "errorCode": null,
  "errorMsg": null
}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY EXPIRED! _ | 鉴权失败,APP KEY 已过期 _ |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
|---|---|---|
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT FOUND! _ | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATC H! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT MATCH WRONG! _ | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE WRONG! _ _ | 鉴权失败,用户角色不匹配 |
| 404 | GATEWAY ROUTE URL NOT FOUND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CONNECTION REFUS _ _ _ _ E EXCEPTION _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO RESPONSE EXCE _ _ _ _ _ PTION | 目标服务无响应 |

###### 创建连接

**接口概述**

创建SSE长连接，用于接收TrekAgent的实时推送消息（如思考过程、工具调用、文本输出等）。调用顺序第2步：建立SSE连接，channelId使用随机UUID。 智能体工厂 OpenTrek 发指南

**前提条件**

先进入菜单[主页->点击头像->APP_KEY]创建APP_KEY 此接口为SSE流式接口，返回Content-Type为text/event-stream；channelId参数必填，需传入随机 UUID。

**接口调用地址**

```
 POST http://${endpoint}/sfm-agent-studio/sfm-api-
gateway/gateway/agent/auto/new/session/createNewChannel
```

**入参描述**

**Header传参**

| 字段 | 数据类型 | 描述 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | 是 | Content-Type | application/json |

**Body传参**

| 字段 | 数据类型 | 描述 | 描述 | 示例 |
|---|---|---|---|---|
| channelId | string | 是 | 通道ID | 4bcaa882-9c54- 4b78-9057- 54db58591b5b |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| data | object | 返回数据 | {"RESULT": "Connection successful"} |

**请求示例**

```json
curl -X 'POST' http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/agent/auto/new/createNewChannel \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -H 'Accept: text/event-stream' \ -d '{
    "channelId": "4bcaa882-9c54-4b78-9057-54db58591b5b"
}'
```

智能体工厂 OpenTrek 发指南

**响应示例**

SSE流式输出

```json
data: {"RESULT": "Connection successful"} data: {"action":"思考","actionParam": {"type":"thought","position":"pop","content":"..."}} data: {"RESULT": "<END>"}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY EXPIRED! _ | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT FOUND! _ | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATC H! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT MATCH WRONG! _ | 鉴权失败,AK用户信息不匹配 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY AUTH USER ROLE WRONG! _ _ | 鉴权失败,用户角色不匹配 |
|---|---|---|
| 404 | GATEWAY ROUTE URL NOT FOUND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CONNECTION REFUS _ _ _ _ E EXCEPTION _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO RESPONSE EXCE _ _ _ _ _ PTION | 目标服务无响应 |

###### 切换至指定session

**接口概述**

切换当前会话到指定session，会释放当前占用的连接并重新占用目标session的连接。调用顺序第3步：使

**前提条件**

先进入菜单[主页->点击头像->APP_KEY]创建APP_KEY taskId参数必填；channelId参数必填。

**接口调用地址**

| POST http://${endpoint}/sfm-agent-studio/sfm-api- |  |
|---|---|

**入参描述**

**Header传参**

| 字段 | 数据类型 | 描述 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | 是 | Content-Type | application/json |

**Body传参**

| 字段 | 数据类型 | 描述 | 描述 | 示例 |
|---|---|---|---|---|

智能体工厂 OpenTrek 发指南

| taskId | string | 是 | 任务ID | 4bcaa882-9c54- 4b78-9057- 54db58591b5b |
|---|---|---|---|---|
| channelId | string | 是 | 通道ID | 4bcaa882-9c54- 4b78-9057- 54db58591b5b |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | boolean | 是否成功 | true |
| data | object | 返回数据 | {"result":true,"taskId": "xxx","sessionId":"xxx" } |
| result | string | 结果 | true |
| taskId | string | 任务ID | 4bcaa882-9c54-4b78- 9057-54db58591b5b |
| sessionId | string | 会话ID | de454297-c547-440f- ae55-057a83a2d121 |
| errorCode | string | 错误码 |  |
| errorMsg | string | 错误信息 |  |

**请求示例**

```json
curl -X 'POST' http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/agent/auto/new/changeTask \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -d '{
    "taskId": "4bcaa882-9c54-4b78-9057-54db58591b5b",
    "channelId": "4bcaa882-9c54-4b78-9057-54db58591b5b"
}'
```

**响应示例**

非流式输出智能体工厂 OpenTrek 发指南

```json
{
  "success": true,
  "data": {
    "result": true,
    "taskId": "4bcaa882-9c54-4b78-9057-54db58591b5b",
    "sessionId": "de454297-c547-440f-ae55-057a83a2d121"
  },
  "errorCode": null,
  "errorMsg": null
}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY EXPIRED! _ | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT FOUND! _ | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATC H! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY AUTH USER NOT MATCH WRONG! _ | 鉴权失败,AK用户信息不匹配 |
|---|---|---|
| 401 | GATEWAY AUTH USER ROLE WRONG! _ _ | 鉴权失败,用户角色不匹配 |
| 404 | GATEWAY ROUTE URL NOT FOUND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CONNECTION REFUS _ _ _ _ E EXCEPTION _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO RESPONSE EXCE _ _ _ _ _ PTION | 目标服务无响应 |

###### 发起一次对话

**接口概述**

以Running方式提出一个问题，智能体会异步处理并通过已建立的SSE连接推送结果。调用顺序第4步：使用createTaskAndSolution返回的taskId和sessionId发起对话。

**前提条件**

先进入菜单[主页->点击头像->APP_KEY]创建APP_KEY sessionId参数必填；messages参数必填；前端只需传sessionId，taskId由系统自动补充。

**接口调用地址**

```
 POST http://${endpoint}/sfm-agent-studio/sfm-api-gateway/gateway/agent/auto/new/run
```

**入参描述**

**Header传参**

| 字段 | 数据类型 | 描述 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | 是 | Content-Type | application/json |

**Body传参**

| 字段 | 数据类型 | 描述 | 描述 | 示例 |
|---|---|---|---|---|

智能体工厂 OpenTrek 发指南

| sessionId | string | 是 | 会话ID | 4bcaa882-9c54- 4b78-9057- 54db58591b5b |
|---|---|---|---|---|
| taskId | string | 是 | 任务ID | 4bcaa882-9c54- 4b78-9057- 54db58591b5b |
| messages | List<Object> | 是 | 消息列表 | [{"content":"帮我订一张明天从上海去苏黎世的机票","role":"user"} ] |
| channelId | string | 是 | 通道ID | 4bcaa882-9c54- 4b78-9057- 54db58591b5b |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | boolean | 是否成功 | true |
| data | string | 返回数据 | "" |
| errorCode | string | 错误码 |  |
| errorMsg | string | 错误信息 |  |

**请求示例**

```json
curl -X 'POST' http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/agent/auto/new/run \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -d '{
    "sessionId": "de454297-c547-440f-ae55-057a83a2d121",
    "taskId": "4bcaa882-9c54-4b78-9057-54db58591b5b",
    "messages": [{
```

`"content": "`帮我订一张明天从上海去苏黎世的机票`",`

```json
        "role": "user"
    }],
    "channelId": "4bcaa882-9c54-4b78-9057-54db58591b5b"
}'
```

**响应示例**

智能体工厂 OpenTrek 发指南非流式输出

```json
{
  "success": true,
  "data": "",
  "errorCode": null,
  "errorMsg": null
}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY EXPIRED! _ | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT FOUND! _ | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATC H! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT MATCH WRONG! _ | 鉴权失败,AK用户信息不匹配 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY AUTH USER ROLE WRONG! _ _ | 鉴权失败,用户角色不匹配 |
|---|---|---|
| 404 | GATEWAY ROUTE URL NOT FOUND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CONNECTION REFUS _ _ _ _ E EXCEPTION _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO RESPONSE EXCE _ _ _ _ _ PTION | 目标服务无响应 |

###### 停止当前对话

**接口概述**

停止当前正在执行的对话。调用顺序第5步：在任务执行过程中调用此接口停止任务。

**前提条件**

先进入菜单[主页->点击头像->APP_KEY]创建APP_KEY sessionId参数必填。

**接口调用地址**

```
 POST http://${endpoint}/sfm-agent-studio/sfm-api-gateway/gateway/agent/auto/new/stop
```

**入参描述**

**Header传参**

| 字段 | 数据类型 | 描述 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | 是 | Content-Type | application/json |

**Body传参**

| 字段 | 数据类型 | 描述 | 描述 | 示例 |
|---|---|---|---|---|
| sessionId | string | 是 | 会话ID | 4bcaa882-9c54- 4b78-9057- 54db58591b5b |

**出参描述**

智能体工厂 OpenTrek 发指南

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | boolean | 是否成功 | true |
| data | boolean | 返回数据 | true |
| errorCode | string | 错误码 |  |
| errorMsg | string | 错误信息 |  |

**请求示例**

```json
curl -X 'POST' http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/agent/auto/new/stop \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -d '{
    "sessionId": "de454297-c547-440f-ae55-057a83a2d121"
}'
```

**响应示例**

非流式输出

```json
{
  "success": true,
  "data": true,
  "errorCode": null,
  "errorMsg": null
}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY EXPIRED! _ | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
|---|---|---|
| 403 | GATEWAY APP PATH NOT FOUND! _ | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATC H! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT MATCH WRONG! _ | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE WRONG! _ _ | 鉴权失败,用户角色不匹配 |
| 404 | GATEWAY ROUTE URL NOT FOUND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CONNECTION REFUS _ _ _ _ E EXCEPTION _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO RESPONSE EXCE _ _ _ _ _ PTION | 目标服务无响应 |

###### 分页查询历史消息

**接口概述**

分页查询会话的历史消息记录。

**前提条件**

先进入菜单[主页->点击头像->APP_KEY]创建APP_KEY taskId、pageIndex、pageSize参数必填智能体工厂 OpenTrek 发指南

**接口调用地址**

| GET http://${endpoint}/sfm-agent-studio/sfm-api- |  |
|---|---|

**入参描述**

**Header传参**

| 字段 | 数据类型 | 描述 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | 是 | Content-Type | application/json |

**Body传参**

| 字段 | 数据类型 | 描述 | 描述 | 示例 |
|---|---|---|---|---|
| taskId | string | 是 | 任务ID | 4bcaa882-9c54- 4b78-9057- 54db58591b5b |
| pageIndex | integer | 是 | 页码 | 1 |
| pageSize | integer | 是 | 每页记录数 | 10 |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | boolean | 是否成功 | true |
| data | List<Object> | 返回数据 | true |
| total | integer | 总记录数 | 100 |
| list | List<String> | 消息列表 | [] |
| errorCode | string | 错误码 |  |
| errorMsg | string | 错误信息 |  |

智能体工厂 OpenTrek 发指南

**请求示例**

```bash
curl -X 'GET' 'http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/agent/auto/new/pageListLatestMsg?taskId=4bcaa882-9c54-4b78-9057-54db585 91b5b&pageIndex=1&pageSize=10' \ -H 'Authorization: Bearer YOUR_APP_KEY'
```

**响应示例**

非流式输出

```json
{
  "success": true,
  "data": {
    "total": 100,
    "pageIndex": 1,
    "pageSize": 10,
    "list": ["..."]
  },
  "errorCode": null,
  "errorMsg": null
}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY EXPIRED! _ | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT FOUND! _ | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT REGISTER! _ | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |

智能体工厂 OpenTrek 发指南

| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
|---|---|---|
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATC H! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT MATCH WRONG! _ | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE WRONG! _ _ | 鉴权失败,用户角色不匹配 |
| 404 | GATEWAY ROUTE URL NOT FOUND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CONNECTION REFUS _ _ _ _ E EXCEPTION _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO RESPONSE EXCE _ _ _ _ _ PTION | 目标服务无响应 |

###### 刷新channel心跳

前端定期调用，维持channel活跃状态。建议在createNewChannel建立SSE连接后，定期（如每30秒） 调用此接口刷新通道，避免连接被回收。

**前提条件**

1. 登录OpenTrek Agent Dev控制台。
2. 在左侧导航栏中选择**集成** **> APP KEY**。
3. 单击**新建**创建APP Key。

**接口调用地址**

```
 GET http://${endpoint}/sfm-agent-studio/sfm-api-
gateway/gateway/agent/auto/new/open/channelRefresh
```

${endpoint}见产品API文档页面详情。

**入参描述**

Header传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|

智能体工厂 OpenTrek 发指南

| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
|---|---|---|---|---|
| Content-Type | String | 是 | Content-Type | application/json |

Query传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| channelId | string | 是 | 通道ID。 | 4bcaa882-9c54- 4b78-9057- 54db58591b5b |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | boolean | 是否成功。 | true |
| data | boolean | 返回数据。 | true |
| errorCode | string | 错误码。 | 400 |
| errorMsg | string | 错误信息。 | error |

**请求示例**

```bash
curl -X GET 'http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/agent/auto/new/open/channelRefresh?channelId=4bcaa882-9c54-4b78-9057-54 db58591b5b' -H 'Authorization: Bearer YOUR_APP_KEY'
```

**响应示例**

```json
{
 "success": true,
 "data": true,
 "errorCode": null,
 "errorMsg": null
}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失。 |
|---|---|---|
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败，无效 APP KEY。 _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败，APP KEY 已过期。 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色不匹配。 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色已过期。 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径。 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册。 |
| 429 | GATEWAY LIMIT ! | 服务触发限流，请稍后再试。 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流，请稍后再试。 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失。 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配。 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败，不支持的鉴权方式。 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败，AK用户信息不匹配。 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败，用户角色不匹配。 |
| 404 | GATEWAY ROUTE URL NOT FOUND! | 无效的目标服务地址。 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限，请稍后再试。 |

智能体工厂 OpenTrek 发指南

| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接。 |
|---|---|---|
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应。 |

###### 获取会话列表

分页查询当前登录用户的会话列表，支持按关键字、状态、解决方案编码、业务类型过滤。

**前提条件**

1. 登录OpenTrek Agent Dev控制台。
2. 在左侧导航栏中选择**集成** **> APP KEY**。
3. 单击**新建**创建APP Key。

**接口调用地址**

| POST http://${endpoint}/sfm-agent-studio/sfm-api- |  |
|---|---|

${endpoint}见产品API文档页面详情。

**入参描述**

Header传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | 是 | Content-Type | application/json |

Body传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| keyword | string | 否 | 关键字。 | 测试 |
| status | string | 否 | 会话状态。 | RUNNING |
| solutionCode | string | 否 | 解决方案编码。 | 3000 |
| bizType | string | 否 | 业务类型。 | dfs |

智能体工厂 OpenTrek 发指南

| pageIndex | integer | 是 | 页码。 | 1 |
|---|---|---|---|---|
| pageSize | integer | 是 | 每页记录数。 | 10 |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | boolean | 是否成功。 | true |
| data | object | 返回数据。 | {"total":100,"pageInde x":1,"pageSize":10,"list ":[...]} |
| errorCode | string | 错误码。 | 400 |
| errorMsg | string | 错误信息。 | error |

**请求示例**

```json
curl -X POST http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/agent/auto/new/open/task/list -H 'Authorization: Bearer YOUR_APP_KEY' - H 'Content-Type: application/json' -d '{
    "keyword": "",
    "status": "",
    "solutionCode": "",
    "bizType": "",
    "pageIndex": 1,
    "pageSize": 10
}'
```

**响应示例**

```json
{
 "success": true,
 "data": {
  "total": 1,
  "pageIndex": 1,
  "pageSize": 10,
  "list": []
 },
 "errorCode": null,
 "errorMsg": null
}
```

**状态码说明**

智能体工厂 OpenTrek 发指南

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失。 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败，无效 APP KEY。 _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败，APP KEY 已过期。 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色不匹配。 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色已过期。 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径。 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册。 |
| 429 | GATEWAY LIMIT ! | 服务触发限流，请稍后再试。 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流，请稍后再试。 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失。 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配。 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败，不支持的鉴权方式。 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败，AK用户信息不匹配。 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败，用户角色不匹配。 |
| 404 | GATEWAY ROUTE URL NOT FOUND! | 无效的目标服务地址。 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY LIMIT ! | 服务链接已达上限，请稍后再试。 |
|---|---|---|
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接。 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应。 |

###### 查询单个任务详情

根据taskId查询单个任务的详细信息，包括任务状态、标题、描述、耗时等。

**前提条件**

1. 登录OpenTrek Agent Dev控制台。
2. 在左侧导航栏中选择**集成** **> APP KEY**。
3. 单击**新建**创建APP Key。

**接口调用地址**

```
 POST http://${endpoint}/sfm-agent-studio/sfm-api-
gateway/gateway/agent/auto/new/open/task/desc
```

${endpoint}见产品API文档页面详情。

**入参描述**

Header传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | 是 | Content-Type | application/json |

Body传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| taskId | string | 是 | 任务ID。 | 4bcaa882-9c54- 4b78-9057- 54db58591b5b |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|

智能体工厂 OpenTrek 发指南

| success | boolean | 是否成功。 | true |
|---|---|---|---|
| data | object | 任务详情。 | {"taskId":"xxx","sessio nId":"xxx","status":"RU NNING"} |
| errorCode | string | 错误码。 | 400 |
| errorMsg | string | 错误信息。 | error |

**请求示例**

```json
curl -X POST http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/agent/auto/new/open/task/desc -H 'Authorization: Bearer YOUR_APP_KEY' - H 'Content-Type: application/json' -d '{
    "taskId": "4bcaa882-9c54-4b78-9057-54db58591b5b"
}'
```

**响应示例**

```json
{
 "success": true,
 "data": {
  "taskId": "4bcaa882-9c54-4b78-9057-54db58591b5b",
  "sessionId": "de454297-c547-440f-ae55-057a83a2d121",
  "status": "RUNNING",
```

`"name": "`任务标题"

```json
 },
 "errorCode": null,
 "errorMsg": null
}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失。 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败，无效 APP KEY。 _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败，APP KEY 已过期。 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色不匹配。 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色已过期。 |
|---|---|---|
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径。 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册。 |
| 429 | GATEWAY LIMIT ! | 服务触发限流，请稍后再试。 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流，请稍后再试。 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失。 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配。 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败，不支持的鉴权方式。 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败，AK用户信息不匹配。 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败，用户角色不匹配。 |
| 404 | GATEWAY ROUTE URL NOT FOUND! | 无效的目标服务地址。 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限，请稍后再试。 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接。 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应。 |

###### 删除任务

根据taskId删除指定任务，任务状态将被标记为已删除。

**前提条件**

智能体工厂 OpenTrek 发指南
1. 登录OpenTrek Agent Dev控制台。
2. 在左侧导航栏中选择**集成** **> APP KEY**。
3. 单击**新建**创建APP Key。

**接口调用地址**

| POST http://${endpoint}/sfm-agent-studio/sfm-api- |  |
|---|---|

${endpoint}见产品API文档页面详情。

**入参描述**

Header传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | 是 | Content-Type | application/json |

Body传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| taskId | string | 是 | 任务ID。 | 4bcaa882-9c54- 4b78-9057- 54db58591b5b |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | boolean | 是否成功。 | true |
| data | object | 返回数据。 | {"result":true} |
| errorCode | string | 错误码。 | 400 |
| errorMsg | string | 错误信息。 | error |

**请求示例**

智能体工厂 OpenTrek 发指南

```json
curl -X POST http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/agent/auto/new/open/task/delete -H 'Authorization: Bearer YOUR_APP_KEY' -H 'Content-Type: application/json' -d '{
    "taskId": "4bcaa882-9c54-4b78-9057-54db58591b5b"
}'
```

**响应示例**

```json
{
 "success": true,
 "data": {
  "result": true
 },
 "errorCode": null,
 "errorMsg": null
}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失。 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败，无效 APP KEY。 _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败，APP KEY 已过期。 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色不匹配。 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色已过期。 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径。 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册。 |
| 429 | GATEWAY LIMIT ! | 服务触发限流，请稍后再试。 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流，请稍后再试。 |

智能体工厂 OpenTrek 发指南

| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失。 |
|---|---|---|
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配。 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败，不支持的鉴权方式。 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败，AK用户信息不匹配。 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败，用户角色不匹配。 |
| 404 | GATEWAY ROUTE URL NOT FOUND! | 无效的目标服务地址。 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限，请稍后再试。 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接。 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应。 |

###### 更新任务信息

根据taskId更新指定任务的信息，支持修改任务名称、状态和已读状态。

**前提条件**

1. 登录OpenTrek Agent Dev控制台。
2. 在左侧导航栏中选择**集成** **> APP KEY**。
3. 单击**新建**创建APP Key。

**接口调用地址**

```
 POST http://${endpoint}/sfm-agent-studio/sfm-api-
gateway/gateway/agent/auto/new/open/task/update
```

${endpoint}见产品API文档页面详情。

**入参描述**

Header传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|

智能体工厂 OpenTrek 发指南

| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
|---|---|---|---|---|
| Content-Type | String | 是 | Content-Type | application/json |

Body传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| taskId | string | 是 | 任务ID。 | 4bcaa882-9c54- 4b78-9057- 54db58591b5b |
| name | string | 否 | 任务名称。 | 我的任务 |
| status | string | 否 | 任务状态。 | RUNNING |
| readStatus | boolean | 否 | 最新状态是否已读。 | true |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | boolean | 是否成功。 | true |
| data | object | 返回数据。 | {"result":true} |
| errorCode | string | 错误码。 | 400 |
| errorMsg | string | 错误信息。 | error |

**请求示例**

```json
curl -X POST http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/agent/auto/new/open/task/update -H 'Authorization: Bearer YOUR_APP_KEY' -H 'Content-Type: application/json' -d '{
    "taskId": "xxx",
```

`"name": "`我的任务`",`

```json
    "status": "RUNNING"
}'
```

智能体工厂 OpenTrek 发指南

**响应示例**

```json
{
 "success": true,
 "data": {
  "result": true
 },
 "errorCode": null,
 "errorMsg": null
}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失。 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败，无效 APP KEY。 _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败，APP KEY 已过期。 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色不匹配。 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色已过期。 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径。 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册。 |
| 429 | GATEWAY LIMIT ! | 服务触发限流，请稍后再试。 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流，请稍后再试。 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失。 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配。 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败，不支持的鉴权方式。 |
|---|---|---|
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败，AK用户信息不匹配。 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败，用户角色不匹配。 |
| 404 | GATEWAY ROUTE URL NOT FOUND! | 无效的目标服务地址。 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限，请稍后再试。 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接。 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应。 |

###### 统计任务状态

**前提条件**

1. 登录OpenTrek Agent Dev控制台。
2. 在左侧导航栏中选择**集成** **> APP KEY**。
3. 单击**新建**创建APP Key。

**接口调用地址**

| POST http://${endpoint}/sfm-agent-studio/sfm-api- |  |
|---|---|

${endpoint}见产品API文档页面详情。

**入参描述**

Header传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | 是 | Content-Type | application/json |

智能体工厂 OpenTrek 发指南 Body传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| solutionCode | string | 否 | 方案编码。 | 12344 |
| digitalCode | string | 否 | 数字人编码。 | 112 |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | boolean | 是否成功。 | true |
| data | object | 统计数据。 | {} |
| errorCode | string | 错误码。 | 400 |
| errorMsg | string | 错误信息。 | error |

**请求示例**

```json
curl -X POST http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/agent/auto/new/open/task/statistic -H 'Authorization: Bearer YOUR_APP_K EY' -H 'Content-Type: application/json' -d '{
    "solutionCode": "solution-abc123"
}'
```

**响应示例**

```json
{
 "success": true,
 "data": {},
 "errorCode": null,
 "errorMsg": null
}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失。 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败，无效 APP KEY。 _ |
|---|---|---|
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败，APP KEY 已过期。 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色不匹配。 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色已过期。 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径。 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册。 |
| 429 | GATEWAY LIMIT ! | 服务触发限流，请稍后再试。 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流，请稍后再试。 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失。 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配。 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败，不支持的鉴权方式。 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败，AK用户信息不匹配。 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败，用户角色不匹配。 |
| 404 | GATEWAY ROUTE URL NOT FOUND! | 无效的目标服务地址。 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限，请稍后再试。 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接。 |

智能体工厂 OpenTrek 发指南

| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应。 |
|---|---|---|

###### 获取会话文件树

**前提条件**

1. 登录OpenTrek Agent Dev控制台。
2. 在左侧导航栏中选择**集成** **> APP KEY**。
3. 单击**新建**创建APP Key。

**接口调用地址**

| GET http://${endpoint}/sfm-agent-studio/sfm-api- |  |
|---|---|

${endpoint}见产品API文档页面详情。

**入参描述**

Header传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | 是 | Content-Type | application/json |

Query传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| sessionId | string | 是 | 任务会话ID。 | de454297-c547- 440f-ae55- 057a83a2d121 |
| depth | integer | 否 | 扫描深度。 | 3 |
| parentPath | string | 否 | 父路径。 | /src |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|

智能体工厂 OpenTrek 发指南

| success | boolean | 是否成功。 | true |
|---|---|---|---|
| data | List | 文件树节点列表。 | [{"id":"xxx","name":"sr c","type":"folder"}] |
| errorCode | string | 错误码。 | 400 |
| errorMsg | string | 错误信息。 | error |

**请求示例**

```bash
curl -X GET 'http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/agent/auto/new/open/files/tree?sessionId=xxx&depth=3' -H 'Authorization: Bearer YOUR_APP_KEY'
```

**响应示例**

```json
{
 "success": true,
 "data": [
  {
   "id": "1",
   "name": "src",
   "type": "folder",
   "path": "/src",
   "children": []
  }
```

`],`

```json
 "errorCode": null,
 "errorMsg": null
}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失。 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败，无效 APP KEY。 _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败，APP KEY 已过期。 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色不匹配。 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色已过期。 |
|---|---|---|
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径。 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册。 |
| 429 | GATEWAY LIMIT ! | 服务触发限流，请稍后再试。 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流，请稍后再试。 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失。 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配。 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败，不支持的鉴权方式。 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败，AK用户信息不匹配。 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败，用户角色不匹配。 |
| 404 | GATEWAY ROUTE URL NOT FOUND! | 无效的目标服务地址。 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限，请稍后再试。 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接。 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应。 |

###### 获取文件下载链接

将会话沙箱NFS上的文件上传到OSS/MinIO，返回预签名下载URL。

**前提条件**

智能体工厂 OpenTrek 发指南
1. 登录OpenTrek Agent Dev控制台。
2. 在左侧导航栏中选择**集成** **> APP KEY**。
3. 单击**新建**创建APP Key。

**接口调用地址**

| GET http://${endpoint}/sfm-agent-studio/sfm-api- |  |
|---|---|

${endpoint}见产品API文档页面详情。

**入参描述**

Header传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | 是 | Content-Type | application/json |

Query传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| sessionId | string | 是 | 任务会话ID。 | de454297-c547- 440f-ae55- 057a83a2d121 |
| path | string | 是 | 文件路径。 | /src/App.tsx |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | boolean | 是否成功。 | true |
| data | string | 预签名下载URL。 | https://oss.example.co m/xxx?Expires=... |
| errorCode | string | 错误码。 | 400 |
| errorMsg | string | 错误信息。 | error |

**请求示例**

智能体工厂 OpenTrek 发指南

```bash
curl -X GET 'http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/agent/auto/new/open/files/download?sessionId=xxx&path=/src/App.tsx' -H 'Authorization: Bearer YOUR_APP_KEY'
```

**响应示例**

```json
{
 "success": true,
 "data": "https://oss.example.com/xxx?Expires=123&Signature=abc",
 "errorCode": null,
 "errorMsg": null
}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失。 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败，无效 APP KEY。 _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败，APP KEY 已过期。 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色不匹配。 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色已过期。 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径。 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册。 |
| 429 | GATEWAY LIMIT ! | 服务触发限流，请稍后再试。 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流，请稍后再试。 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失。 |

智能体工厂 OpenTrek 发指南

| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配。 |
|---|---|---|
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败，不支持的鉴权方式。 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败，AK用户信息不匹配。 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败，用户角色不匹配。 |
| 404 | GATEWAY ROUTE URL NOT FOUND! | 无效的目标服务地址。 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限，请稍后再试。 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接。 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应。 |

###### 查询短期记忆

根据sessionId和userId查询当前会话的短期记忆摘要。

**前提条件**

1. 登录OpenTrek Agent Dev控制台。
2. 在左侧导航栏中选择**集成** **> APP KEY**。
3. 单击**新建**创建APP Key。

**接口调用地址**

```
 GET http://${endpoint}/sfm-agent-studio/sfm-api-
gateway/gateway/agent/auto/new/open/memory/summary/get
```

${endpoint}见产品API文档页面详情。

**入参描述**

Header传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|

智能体工厂 OpenTrek 发指南

| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
|---|---|---|---|---|
| Content-Type | String | 是 | Content-Type | application/json |

Query传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| sessionId | string | 是 | 任务会话ID。 | de454297-c547- 440f-ae55- 057a83a2d121 |
| userId | string | 否 | 用户ID。 | 34567 |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | boolean | 是否成功。 | true |
| data | object | 返回数据。 | {"time":"2026-07- 08","summary":"..."} |
| errorCode | string | 错误码。 | 400 |
| errorMsg | string | 错误信息。 | error |

**请求示例**

```bash
curl -X GET 'http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/agent/auto/new/open/memory/summary/get?sessionId=xxx&userId=xxx' -H 'Au thorization: Bearer YOUR_APP_KEY'
```

**响应示例**

智能体工厂 OpenTrek 发指南

```json
{
 "success": true,
 "data": {
  "time": "2026-07-08 15:58:51",
```

`"summary": "`会话摘要内容"

```json
 },
 "errorCode": null,
 "errorMsg": null
}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失。 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败，无效 APP KEY。 _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败，APP KEY 已过期。 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色不匹配。 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色已过期。 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径。 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册。 |
| 429 | GATEWAY LIMIT ! | 服务触发限流，请稍后再试。 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流，请稍后再试。 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失。 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配。 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败，不支持的鉴权方式。 |
|---|---|---|
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败，AK用户信息不匹配。 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败，用户角色不匹配。 |
| 404 | GATEWAY ROUTE URL NOT FOUND! | 无效的目标服务地址。 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限，请稍后再试。 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接。 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应。 |

###### 更新短期记忆

根据sessionId和userId更新当前会话的短期记忆摘要。

**前提条件**

1. 登录OpenTrek Agent Dev控制台。
2. 在左侧导航栏中选择**集成** **> APP KEY**。
3. 单击**新建**创建APP Key。

**接口调用地址**

```
 POST http://${endpoint}/sfm-agent-studio/sfm-api-
gateway/gateway/agent/auto/new/open/memory/summary/update
```

${endpoint}见产品API文档页面详情。

**入参描述**

Header传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | 是 | Content-Type | application/json |

智能体工厂 OpenTrek 发指南 Body传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| sessionId | string | 是 | 任务会话ID。 | de454297-c547- 440f-ae55- 057a83a2d121 |
| userId | string | 否 | 用户ID。 | 34567 |
| summary | string | 是 | 记忆摘要内容。 | 会话摘要内容 |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | boolean | 是否成功。 | true |
| data | boolean | 是否成功更新。 | true |
| errorCode | string | 错误码。 | 400 |
| errorMsg | string | 错误信息。 | error |

**请求示例**

```json
curl -X POST http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/agent/auto/new/open/memory/summary/update -H 'Authorization: Bearer YOU R_APP_KEY' -H 'Content-Type: application/json' -d '{
    "sessionId": "xxx",
    "userId": "xxx",
```

`"summary": "`会话摘要内容"

```
}'
```

**响应示例**

```json
{
 "success": true,
 "data": true,
 "errorCode": null,
 "errorMsg": null
}
```

**状态码说明**

智能体工厂 OpenTrek 发指南

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失。 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败，无效 APP KEY。 _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败，APP KEY 已过期。 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色不匹配。 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色已过期。 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径。 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册。 |
| 429 | GATEWAY LIMIT ! | 服务触发限流，请稍后再试。 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流，请稍后再试。 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失。 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配。 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败，不支持的鉴权方式。 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败，AK用户信息不匹配。 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败，用户角色不匹配。 |
| 404 | GATEWAY ROUTE URL NOT FOUND! | 无效的目标服务地址。 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY LIMIT ! | 服务链接已达上限，请稍后再试。 |
|---|---|---|
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接。 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应。 |

##### 知识库检索

###### 文件元数据批量标注

为指定知识库下的文件批量标注用户元数据，支持文档知识库和图文知识库。

**接口概述**

为指定知识库下的文件批量标注用户元数据，支持文档知识库和图文知识库。

**前提条件**

仅支持文档知识库(kb_doc)和图文知识库(kb_visual)类型。 metadata 为元数据键值对，key 对应元数据定义的 name，value 为标注值。 接口会校验元数据是否在当前知识库可见范围内、值类型是否匹配、候选值是否合法；写入时为增量合并，同名 key 会覆盖原值。 单个文件最多支持 32 个元数据标注。

**接口调用地址**

```
 POST http://IP:port/sfm-agent-studio/sfm-api-
gateway/gateway/kortex/api/kb/metadata/annotateFileMetadata
```

**入参描述**

**Header传参**

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| x-sfm- workspacecode | String | 是 | 目标工作空间 | your workspace _ _ code |
| Content-Type | String | 是 | Content-Type | application/json |

**Body传参**

智能体工厂 OpenTrek 发指南

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| kbCode | String | 是 | 知识库编码。 | ozqn95a5936ycw kl |
| fileCodes | List | 是 | 目标文件编码列表。 | ["adaf2a92995b4 e439f68ebe3222 de9a1", "bfe2b1a3888c4f 529e79cdfa4330f 8b2"] |
| metadata | Object | 否 | 元数据键值对。 | {"region":"华东","file type":"p _ df","publish time _ ":"2025-01-01 00:00:00","score" :95} |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功。 | true |
| data | Object | 返回数据，成功时为空。 | null |
| errorCode | String | 错误码。 | KB METADATA UNSUP _ _ PORTED TYPE _ |
| errorMsg | String | 错误描述。 | Unsupported knowledge base type for metadata annotation: 3 |

**请求示例**

**curl命令示例**

```json
curl -X POST http://IP:port/sfm-agent-studio/sfm-apigateway/gateway/kortex/api/kb/metadata/annotateFileMetadata -H "Authorization: Bearer Y OUR_APP_KEY" -H "Content-Type: application/json" -H "x-sfm-workspacecode: baseline" -d '{"kbCode":"ozqn95a5936ycwkl","fileCodes": ["adaf2a92995b4e439f68ebe3222de9a1","bfe2b1a3888c4f529e79cdfa4330f8b2"],"metadata":{"re gion":"华东","file_type":"pdf","publish_time":"2025-01-01 00:00:00","score":95}}'
```

**响应示例**

智能体工厂 OpenTrek 发指南

```json
{"success":true,"data":null,"errorCode":null,"errorMsg":null}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失。 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败，无效 APP KEY。 _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败，APP KEY 已过期。 _ |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径。 |
| 429 | GATEWAY LIMIT! | 服务触发限流，请稍后再试。 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接。 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应。 |

###### 文件元数据过滤查询

根据文件元数据过滤条件查询匹配的 fileCode 列表，支持文档知识库和图文知识库。

**接口概述**

根据文件元数据过滤条件查询匹配的 fileCode 列表，支持文档知识库和图文知识库。

**前提条件**

仅支持文档知识库(kb_doc)和图文知识库(kb_visual)类型。通过元数据条件组构建AND/OR逻辑组合，精确筛选符合元数据标注要求的文件。

**接口调用地址**

```
 POST http://IP:port/sfm-agent-studio/sfm-api-
gateway/gateway/kortex/api/kb/metadata/filterFileCodes
```

**入参描述**

**Header传参**

智能体工厂 OpenTrek 发指南

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| x-sfm- workspacecode | String | 是 | 目标工作空间 | your workspace _ _ code |
| Content-Type | String | 是 | Content-Type | application/json |

**Body传参**

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| kbCode | String | 是 | 知识库编码。 | ozqn95a593 6ycwkl |
| operator | String | 是 | 条件组间逻辑操作符。 | AND |
| conditions | List | 是 | 条件组列表。 | - |
| innerOperat or | String | 是 | 条件组内逻辑操作符，可选值: AND(与), OR(或)。 | AND |
| rules | Array | 是 | 过滤规则列表。 | - |
| metadataNa me | String | 是 | 元数据key，对应元数据定义的 metadataCode。 | region |
| metadataTy pe | String | 是 | 元数据类型，用于GT/GTE/LT/LTE的类型转换。 | string |

智能体工厂 OpenTrek 发指南

| ruleType | String | 是 | 运算符类型： EQ：等于 NE：不等于 IN：包含 NOT IN：不包含 _ IS NULL：为空 _ IS NOT NULL：非空 _ _ LIKE：模糊匹配 GT：大于 GTE：大于等于 LT：小于 LTE：小于等于 LEN EQ：长度等于 _ LEN NE：长度不等于 _ LEN GT：长度大于 _ LEN GTE：长度大于等于 _ LEN LT：长度小于 _ LEN LTE：长度小于等于 _ | EQ |
|---|---|---|---|---|
| value | Object | 否 | 匹配值（单值），ruleType为 EQ/NE/GT/GTE/LT/LTE/LIKE/LEN xxx _ 时使用。 | 华东 |
| valueList | Array | 否 | 匹配值列表，ruleType为IN/NOT IN时 _ 使用。 | ["pdf","doc"] |
| valueSource | String | 否 | 值来源： constant：常量 reference：引用 function：函数 | constant |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功。 | true |
| data | List | 返回数据，匹配的 fileCode列表（已排序）。 | ["adaf2a92995b4e439 f68ebe3222de9a1", "bfe2b1a3888c4f529e 79cdfa4330f8b2"] |

智能体工厂 OpenTrek 发指南

| errorCode | String | 错误码。 | KB METADATA UNSUP _ _ PORTED TYPE _ |
|---|---|---|---|
| errorMsg | String | 错误描述. | Unsupported knowledge base type for metadata fileCode filtering: 3 |

**请求示例**

**curl命令示例**

```json
curl -X POST http://IP:port/sfm-agent-studio/sfm-apigateway/gateway/kortex/api/kb/metadata/filterFileCodes -H "Authorization: Bearer YOUR_A PP_KEY" -H "Content-Type: application/json" -H "x-sfm-workspacecode: baseline" -d '{"kb Code":"ozqn95a5936ycwkl","operator":"AND","conditions":[{"innerOperator":"AND","rules": [{"metadataName":"region","ruleType":"EQ","value":"华东"}, {"metadataName":"file_type","ruleType":"IN","valueList":["pdf","doc"]}]}]}'
```

**响应示例**

```json
{"success":true,"data": ["adaf2a92995b4e439f68ebe3222de9a1","bfe2b1a3888c4f529e79cdfa4330f8b2"],"errorCode":null, rrorMsg":null}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失。 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败，无效 APP KEY。 _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败，APP KEY 已过期。 _ |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径。 |
| 429 | GATEWAY LIMIT! | 服务触发限流，请稍后再试。 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接。 |

智能体工厂 OpenTrek 发指南

| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应。 |
|---|---|---|

###### 知识库检索

**接口概述**

知识库通用检索能力，包括文档知识库、自定义知识库、图文知识库

**前提条件（查看APP_KEY）**

先进入菜单[主页->点击头像->APP_KEY]创建APP_KEY

**接口调用地址**

POST http://${endpoint}/gateway/kortex/api/kb/mono/retrieve ${endpoint}见产品API文档页面详情

**入参描述**

Header传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| Content-Type | String | 是 | Content-Type | application/json |
| x-sfm- workspacecode | String | 是 | 目标工作空间 | your workspace _ _ code |

Body传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| kbIndexCode | String | 是 | 知识库索引code,见知识库详情返回结构 kbSubmodels[0]. kbIndexes[0].kbI ndexCode | tttbnz21diense89 |

智能体工厂 OpenTrek 发指南

| kbIndexRetrieveF ieldName | String | 是 | 检索字段 | 见知识库详情返回结构kbSubmodels 部分; 文档知识库固定传递 chunk represent _ ation; 图文知识库可传递 image path 或者 _ text; 自定义知识库库见知识库详情响应体中的 kbSubmodels[0]. kbIndexes 中 Retrieve类型字段; |
|---|---|---|---|---|
| query | String | 是 | 查询内容 | 字符串 |
| filters | JSONObject | 否 | 查询内容 | 扩展过滤项, 例如文档支持库,支持针对特定文档进行检索, 例如 {"file code": _ "aaa"} |
| score | Double | 是 | 最小分值 | 0.01 |
| limit | Integer | 是 | 返回条目 | 10 |

智能体工厂 OpenTrek 发指南

| advancedRules | Object | 否 | 高级规则配置，支持复杂的AND/OR 逻辑组合过滤条件 | {"operator":"AND ","conditions": [{"type":"simple" ,"simpleRule": {"fileName":"pla n code","ruleTyp _ eEnum":"EQ","fil eValue":"YCJ2024 100"}}, {"type":"nested", "advancedRules": {"operator":"AND ","conditions": [{"type":"simple" ,"simpleRule": {"fileName":"pla n name","ruleTy _ peEnum":"LIKE"," fileValue":"江南区"}}, {"type":"simple", "simpleRule": {"fileName":"are a name","ruleTy _ peEnum":"IN","fil eValueList":["江北区","江南区"]}}]}}]} |
|---|---|---|---|---|
| operator | String | 是 | 逻辑操作符，可选值: AND(与), OR(或) | AND |
| conditions | Array | 是 | 条件列表，每个条件可以是简单条件 (type=simple)或嵌套条件 (type=nested) | [{"type":"simple" ,...}, {"type":"nested", ...}] |
| type | String | 是 | 条件类型，可选值: simple(简单条件), nested(嵌套条件) | simple |

智能体工厂 OpenTrek 发指南

| simpleRule | Object | 否 | 简单规则定义 (type=simple时必填) | {"fileName":"pla n code","ruleTyp _ eEnum":"EQ","fil eValue":"YWC34 520000"} |
|---|---|---|---|---|
| fileName | String | 是 | 匹配的字段名 | plan code _ |
| ruleTypeEnum | String | 是 | 规则类型，可选值: EQ(等于), IN(包含), IS NOT NULL(非 _ _ 空), LIKE(模糊匹配) | EQ |
| fileValue | Object | 否 | 单个匹配值，ruleTypeEnu m为EQ/LIKE时使用 | YCJ2024520000 |
| fileValueList | Array | 否 | 多个匹配值列表，ruleTypeEnu m为IN时使用 | ["江南区","江北区"] |
| advancedRules | Object | 否 | 嵌套的高级检索规则(type=nested时必填)，支持递归嵌套 | {"operator":"AND ","conditions": [{"type":"simple" ,...}, {"type":"simple",. ..}]} |
| operator | String | 是 | 嵌套逻辑操作符， 可选值: AND, OR | AND |
| conditions | Array | 是 | 嵌套条件列表 | [...] |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | List<Object> | 返回数据,按照预先定义的 kbSubmodels结构返回 | [] |
| score | String | 得分 | true |

智能体工厂 OpenTrek 发指南

| sys source ids _ _ | String | 数据附加信息 | true |
|---|---|---|---|
| sys data id _ _ | String | 数据唯一ID; | true |
| sys create time _ _ | String | 创建时间 | true |
| **** | String | 动态的自定义召回字段;例如图文知识库召回的 file code、 _ image path、text; 文档 _ 知识库召回的 file code、 _ chunk bboxs、 _ show content、 _ chunk upload type、 _ _ chunk content 、 _ chunk sort number、 _ _ start page _ |  |
| metrics | Object | 性能指标 | {} |
| kbCode | String | 知识库编码 | xxx |
| totalTime | Long | 检索总耗时(ms) | 150 |
| chunksCount | Integer | 返回的chunk数量 | 10 |
| retrievalDetails | List<Object> | 详细检索指标 | [{"kbIndexCode":"yyy" ,"engineType":"builtin _ vector","embeddingTi me":50,"vectorRecallTi me":80,"retrievedChun ksCount":10}] |
| kbIndexCode | String | 索引编码 | ozqn95a5936ycwkl |
| engineType | String | 引擎类型 | builtin vector _ |
| embeddingTime | Long | 向量嵌入耗时(ms) | 50 |
| vectorRecallTime | Long | 向量召回耗时(ms) | 80 |
| textQueryTime | Long | 全文检索耗时(ms) | 60 |

智能体工厂 OpenTrek 发指南

| retrievedChunksCount | Integer | 该引擎实际召回的chunk 数量 | 10 |
|---|---|---|---|
| errorCode | String | 错误码 | true |
| errorMsg | String | 错误描述 | true |

**请求示例**

```json
curl -X 'POST' http://${endpoint}/gateway/kortex/api/kb/mono/retrieve \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -H 'x-sfm-workspacecode: baseline' \ -d '{
    "kbIndexCode":"qdqsajkhjn6xpn7z",
     "kbIndexRetrieveFieldName":"text",
```

`"query":"`草莓`",`

```json
      "score":0.01,
     "limit":10
}'
```

**响应示例**

```json
{"success":true,"data": [{"score":0.529308557510376,"file_code":"adaf2a92995b4e439f68ebe3222de9a1","sys_source_id :"{\"kb_submodel\": \"true\", \"kb_submodel.sys_data_id\": \"82aab26d-b1ff-40da-a3fc-bb adb5b3b439\"}","image_path":"apsara/kortex/kb/visual/file/wjtir7knghhr/SglptjTkqA35r12MoU xE91rWSEonTg/8f1af9cbaa9d9aee17a0c0bd944ef662.jpeg","sys_data_id":"82aab26d-b1ff-40da-a
```

`3fc-bbadb5b3b439","text":"`这是一张草莓的特写照片，草莓表面有水珠，背景是绿色的叶子。

```
","sys_create_time":"2025-07-04T13:28:58.122+00:00"}],"ext":"metrics":" {\'chunksCount\':3,\'retrievalDetails\: [{\'embeddingTime\:161,\'engineType\:\'builtin_vector\',\'kbCode\':\'ozqn95a5936y\',\'kbI exCode\':\'ozqn95a5936ycwkl\',\'retrievedChunksCount\':3,\'vectorRecallTime\':40}],\'tota ime\':234}","errorCode":null,"errorMsg":null}
```

**状态码说明**

网关异常状态码说明

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY E _ XPIRED! | 鉴权失败,APP KEY 已过期 _ |

智能体工厂 OpenTrek 发指南

| 403 | GATEWAY APP PATH NOT FOUN _ D! | 无效的服务调用路径 |
|---|---|---|
| 403 | GATEWAY APP PATH NOT REGI _ STER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSP ACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT MA _ TCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE W _ _ RONG! | 鉴权失败,用户角色不匹配 |
| 404 | GATEWAY ROUTE URL NOT FOU ND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应 |

###### 知识库批量检索

**接口概述**

支持同时检索多个知识库，每个知识库可配置不同的检索参数，最大支持10个知识库同时检索。

**前提条件（查看APP_KEY）**

先进入菜单[主页->点击头像->APP_KEY]创建APP_KEY

**接口调用地址**

POST http://${endpoint}/gateway/kortex/api/kb/mono/combination/retrieve ${endpoint}见产品API文档页面详情智能体工厂 OpenTrek 发指南

**入参描述**

Header传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| Content-Type | String | 是 | Content-Type | application/json |
| x-sfm- workspacecode | String | 是 | 目标工作空间 | your workspace _ _ code |

Body传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| combinationPara ms | List<object> | 是 | 检索参数列表 | [{"kbIndexCode": "xxx","kbIndexRe trieveFieldName" :"name","query": "测试","score":0.01," limit":10}] |
| kbIndexCode | String | 是 | 知识库索引code | tttbnz21dien |
| kbIndexRetrieveF ieldName | String | 是 | 检索字段 | name |
| query | String | 是 | 查询内容 | 测试查询 |
| score | Double | 是 | 最小分值 | 0.01 |
| limit | Integer | 是 | 返回条目 | 10 |
| mapBatchKey | String | 否 | 批量检索时的结果映射KEY，用于区分不同请求的结果 | kb1 |

智能体工厂 OpenTrek 发指南

| advancedRules | Object | 否 | 高级规则配置，支持复杂的AND/OR 逻辑组合过滤条件 | {"operator":"AND ","conditions": [{"type":"simple" ,"simpleRule": {"fileName":"pla n code","ruleTyp _ eEnum":"EQ","fil eValue":"YCJ2024 100"}}, {"type":"nested", "advancedRules": {"operator":"AND ","conditions": [{"type":"simple" ,"simpleRule": {"fileName":"pla n name","ruleTy _ peEnum":"LIKE"," fileValue":"江南区"}}, {"type":"simple", "simpleRule": {"fileName":"are a name","ruleTy _ peEnum":"IN","fil eValueList":["江北区","江南区"]}}]}}]} |
|---|---|---|---|---|
| operator | String | 是 | 逻辑操作符，可选值: AND(与), OR(或) | AND |
| conditions | Array | 是 | 条件列表，每个条件可以是简单条件 (type=simple)或嵌套条件 (type=nested) | [{"type":"simple" ,...}, {"type":"nested", ...}] |
| type | String | 是 | 条件类型，可选值: simple(简单条件), nested(嵌套条件) | simple |
| simpleRule | Object | 否 | 简单规则定义 (type=simple时必填) | {"fileName":"pla n code","ruleTyp _ eEnum":"EQ","fil eValue":"YWC34 520000"} |
| fileName | String | 是 | 匹配的字段名 | plan code _ |

智能体工厂 OpenTrek 发指南

| ruleTypeEnum | String | 是 | 规则类型，可选值: EQ(等于), IN(包含), IS NOT NULL(非 _ _ 空), LIKE(模糊匹配) | EQ |
|---|---|---|---|---|
| fileValue | Object | 否 | 单个匹配值，ruleTypeEnu m为EQ/LIKE时使用 | YCJ2024520000 |
| fileValueList | Array | 否 | 多个匹配值列表，ruleTypeEnu m为IN时使用 | ["江南区","江北区"] |
| advancedRules | Object | 否 | 嵌套的高级检索规则(type=nested时必填)，支持递归嵌套 | {"operator":"AND ","conditions": [{"type":"simple" ,...}, {"type":"simple",. ..}]} |
| operator | String | 是 | 嵌套逻辑操作符， 可选值: AND, OR | AND |
| conditions | Array | 是 | 嵌套条件列表 | [...] |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | List<Object> | 批量检索结果列表 | [] |
| mapBatchKey | String | 结果映射KEY（对应请求中的mapBatchKey） | kb1 |
| kbCode | String | 知识库编码 | xxx |
| kbIndexEngineType | String | 索引引擎类型 | builtin vector _ |

智能体工厂 OpenTrek 发指南

| kbIndexCode | String | 索引编码 | yyy |
|---|---|---|---|
| result | List<Map<String,Obje ct>> | 检索结果列表 | [{"score":0.85,"file co _ de":"xxx"}] |
| metrics | Object | 性能指标 | {} |
| kbCode | String | 知识库编码 | xxx |
| totalTime | Long | 检索总耗时(ms) | 150 |
| chunksCount | Integer | 返回的chunk数量 | 10 |
| retrievalDetails | List<Object> | 详细检索指标 | [] |
| kbIndexCode | String | 索引编码 | ozqn95a5936ycwkl |
| engineType | String | 引擎类型 | builtin vector _ |
| embeddingTime | Long | 向量嵌入耗时(ms) | 50 |
| vectorRecallTime | Long | 向量召回耗时(ms) | 80 |
| textQueryTime | Long | 全文检索耗时(ms) | 60 |
| retrievedChunksCount | Integer | 该引擎实际召回的chunk 数量 | 10 |
| errorCode | String | 错误码 |  |
| errorMsg | String | 错误描述 |  |

**请求示例**

智能体工厂 OpenTrek 发指南

```json
curl -X 'POST' http://${endpoint}/gateway/kortex/api/kb/mono/combination/retrieve \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -H 'x-sfm-workspacecode: baseline' \ -d '{
    "combinationParams":[
        {
            "kbCode":"kbcode1",
            "kbIndexRetrieveFieldName":"name",
```

`"query":"`测试查询`1",`

```json
            "score":0.01,
            "limit":5,
            "mapBatchKey":"kb1",
            "kbIndexEngineType":"builtin_vector"
        },
        {
            "kbCode":"kbcode2",
            "kbIndexRetrieveFieldName":"text",
```

`"query":"`测试查询`2",`

```json
            "score":0.01,
            "limit":5,
            "mapBatchKey":"kb2",
            "kbIndexEngineType":"builtin_es"
        }
```

]

```
}'
```

**响应示例**

```json
{"success":true,"data": [{"mapBatchKey":"kb1","kbCode":"o4jgjrg0997v","kbIndexEngineType":"builtin_vector","kbInd Code":"o4jgjrg0997vr4rd","result":[{"score":1,"sys_source_ids":"{\'kb_submodel\': \'tru e\', \'source_builtin_smod\': \'true\', \'kb_submodel.sys_data_id\': \'a8c07518-0f8f-4f f4-b5f4-a91781241cac\'}","name":"小明","sys_data_id":"a8c07518-0f8f-4ff4-b5f4-a91781241c ac","describe":"学生","age":12,"sys_create_time":"2026-03-13T07:16:57.661+00:00"},{"scor e":0.4903782308101654,"sys_source_ids":"{\'kb_submodel\': \'true\', \'source_builtin_smod\': \'true\', \'kb_submodel.sys_data_id\': \'5a8d1e92-ec8f-4316-aa 8b-7be48379733e\'}","name":"小刚","sys_data_id":"5a8d1e92-ec8f-4316-aa8b-7be48379733e"," describe":"工人","age":25,"sys_create_time":"2026-03-13T07:17:12.418+00:00"}],"metrics": {"kbCode":"o4jgjrg0997v","totalTime":412,"chunksCount":2,"retrievalDetails":[{"kbIndexC ode":"o4jgjrg0997vr4rd","engineType":"builtin_vector","embeddingTime":279,"vectorRecallTi ":94,"textQueryTime":null,"retrievedChunksCount":2}]}}],"errorCode":null,"errorMsg":null, raceId":null,"env":null,"ext":null}
```

**状态码说明**

网关异常状态码说明

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
|---|---|---|
| 401 | GATEWAY APP KEY ALREADY E _ XPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 403 | GATEWAY APP PATH NOT FOUN _ D! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT REGI _ STER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSP ACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT MA _ TCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE W _ _ RONG! | 鉴权失败,用户角色不匹配 |
| 404 | GATEWAY ROUTE URL NOT FOU ND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应 |

###### 文档知识库检索

**接口概述**

**前提条件（查看APP_KEY）**

智能体工厂 OpenTrek 发指南先进入菜单[主页->点击头像->APP_KEY]创建APP_KEY

**接口调用地址**

POST http://${endpoint}/gateway/kortex/api/kb/doc/retrieve ${endpoint}见产品API文档页面详情

**入参描述**

Header传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| Content-Type | String | 是 | Content-Type | application/json |
| x-sfm- workspacecode | String | 是 | 目标工作空间 | your workspace _ _ code |

Body传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| kbCode | String | 是 | 知识库编码 | tttbnz21dien |
| kbIndexEngineTy pe | String | 否 | 索引引擎类型，可选值: builtin vector(向 _ 量索引引擎), builtin es(全文索 _ 引引擎) | builtin vector _ |
| query | String | 是 | 查询内容 | 字符串 |
| score | Double | 是 | 最小分值 | 0.01 |
| limit | Integer | 是 | 返回条目 | 10 |
| filters | JSONObject | 否 | 过滤条件 | 扩展过滤项, {"file code": _ "aaa"} |
| chunkConfig | Object | 否 | Chunk扩展配置 | {"chunkBefore": 2, "chunkAfter": 2, "withNeighborCh unks": true} |

智能体工厂 OpenTrek 发指南

| chunkBefore | Integer | 否 | 返回前N个相邻 chunk数量，最大不超过5 | 2 |
|---|---|---|---|---|
| chunkAfter | Integer | 否 | 返回后N个相邻 chunk数量，最大不超过5 | 2 |
| withNeighborChu nks | Boolean | 否 | 是否返回相邻 chunk内容列表 | true |
| fusionType | String | 否 | 融合检索类型，可选值: lws(线性加权), rrf(互惠排名融合)。为空时表示不使用融合检索 | lws |
| fusionConfig | Object | 否 | 融合检索配置，只有fusionType不为空时才需要设置 | {"textScore": 0.5, "vectorScore": 0.5, "topKText": 20, "topKVec": 20, "topN": 10, "keywordWeight" : 0.5, "rankDiscount": 60} |
| topKText | Integer | 否 | 全文检索返回条数，默认使用limit | 20 |
| topKVec | Integer | 否 | 向量检索返回条数，默认使用limit | 20 |
| topN | Integer | 否 | 融合检索后返回条数，默认使用limit | 10 |
| textScore | Double | 否 | 全文检索分数阈值，融合检索时使用，默认0.5 | 0.5 |
| vectorScore | Double | 否 | 向量检索分数阈值，融合检索时使用，默认0.5 | 0.5 |

智能体工厂 OpenTrek 发指南

| keywordWeight | Float | 否 | 关键词权重(LWS时使用)，越大越偏向于全文检索- BM25，默认0.5 | 0.5 |
|---|---|---|---|---|
| rankDiscount | Integer | 否 | RRF名次衰减系数，越大越不看重头部排名，默认60 | 60 |
| needFileInfo | Boolean | 否 | 是否需要返回文件信息 | true |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | List<Object> | 返回数据,按照预先定义的 kbSubmodels结构返回 | [] |
| score | String | 检索结果的相关性得分， 根据检索类型不同含义不同，单引擎检索保持原始语义，融合检索经归一化处理用于统一评分标准。 1）单引擎检索：保持原始引擎的语义，向量检索为余弦相似度(0-1)，全文检索为BM25相关性得分；2）LWS融合：线性加权融合得分，经归一化处理；3）RRF融合：基于排名的互惠排名融合得分。 | 0.5 |
| sys data id _ _ | String | 数据唯一ID; | 59cc2523-8445-4f3a- 91f7-5e311f5530b2 |
| file name _ | String | 文件名称(当needFileInfo 为true时返回) | document.pdf |
| file url _ | String | 文件URL(当needFileInfo 为true时返回带有STS临时认证信息的地址) | https://example.com/fil es/document.pdf |
| file type _ | String | 文件类型(当needFileInfo 为true时返回) | pdf |

智能体工厂 OpenTrek 发指南

| sys create time _ _ | String | 数据创建时间; | 2023-04- 01T12:34:56Z |
|---|---|---|---|
| file code _ | String | 文件编码(当needFileInfo 为true时返回) | 123456 |
| chunk upload type _ _ | Integer | 上传类型 | 1 |
| chunk content _ | String | chunk内容 - 召回后送入 LLM的prompt文本 |  |
| show content _ | String | chunk内容 - 带有bbox和 objects占位符的文本形式 |  |
| chunk bboxs _ | List<Object> | bbox坐标信息 |  |
| text bbox _ | List<Double> | 坐标 | [ 0.3115, 0.0683, 0.0285, 0.372 ] |
| text type _ | String | 文本类型 | docTitle |
| text content _ | String | 文本内容 | 汇丰香港账户使用指南 |
| page | Integer | 页数 | 1 |
| start page _ | Integer | chunk序号 | 1 |
| chunk sort number _ _ | Integer | 页码 | 0 |
| beforeChunks | List<KbdocChunkNeig hbor> | 前N个相邻chunks(当 chunkBefore>0时返回) | [{"sysDataId":"xxx","fil eCode":"yyy","chunkC ontent":"内容"}] |
| afterChunks | List<KbdocChunkNeig hbor> | 后N个相邻chunks(当 chunkAfter>0时返回) | [{"sysDataId":"xxx","fil eCode":"yyy","chunkC ontent":"内容"}] |
| neighborChunkContent s | List<String> | 相邻chunk内容列表(当 withNeighborChunks为 true时返回) | ["前chunk内容","检索 chunk内容","后chunk内容"] |

智能体工厂 OpenTrek 发指南

| ext | Object | 扩展字段 | {} |
|---|---|---|---|
| metrics | Object | 性能指标 | {} |
| kbCode | String | 知识库编码 | ozqn95a5936y |
| totalTime | Long | 检索总耗时(ms) | 150 |
| chunksCount | Integer | 返回的chunk数量 | 10 |
| fusionType | String | 融合方法类型 | lws |
| rrfTime | Long | RRF融合耗时(ms)，仅 RRF融合时有值 | 20 |
| lwsTime | Long | LWS融合耗时(ms)，仅 LWS融合时有值 | 15 |
| fillTime | Long | 附加信息填充耗时(ms) | 30 |
| retrievalDetails | List<Object> | 详细检索指标 | [{"kbIndexCode":"ozq n95a5936ycwkl","engi neType":"builtin vecto _ r","embeddingTime":5 0,"vectorRecallTime":8 0,"retrievedChunksCo unt":10}] |
| kbIndexCode | String | 索引编码 | ozqn95a5936ycwkl |
| engineType | String | 引擎类型 | builtin vector _ |
| embeddingTime | Long | 向量嵌入耗时(ms) | 50 |
| vectorRecallTime | Long | 向量召回耗时(ms) | 80 |
| textQueryTime | Long | 全文检索耗时(ms) | 60 |
| retrievedChunksCount | Integer | 该引擎实际召回的chunk 数量 | 10 |

智能体工厂 OpenTrek 发指南

| errorCode | String | 错误码 |  |
|---|---|---|---|
| errorMsg | String | 错误描述 |  |

**请求示例**

```json
curl -X 'POST' http://${endpoint}/gateway/kortex/api/kb/doc/retrieve \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -H 'x-sfm-workspacecode: baseline' \ -d '{
    "kbIndexCode":"qdqsajkhjn6xpn7z",
     "kbIndexRetrieveFieldName":"text",
```

`"query":"`草莓`",`

```json
      "score":0.01,
     "limit":10
}'
```

**响应示例**

```json
{"success":true,"data":[{"sys_data_id":"eda55b8d-93e6-40b7-a6de- 19b49f97b6fd","file_code":"e8f574d28a854f31aa52fda0d18f713e","chunk_content":"xxxxxxxxxxx ","score":0.57709527},{"sys_data_id":"aafd75f6-e8cd-4f64-994f- 59cb51a3fe5b","file_code":"e8f574d28a854f31aa52fda0d18f713e","chunk_content":"xxxxxxxxxxx ,"score":0.53833395},{"sys_data_id":"2c162691-245b-4a9a-9b22ccf401de84b0","file_code":"e8f574d28a854f31aa52fda0d18f713e","chunk_content":"xxxxxxxxxxx "score":0.50306636}],"errorCode":null,"errorMsg":null,"traceId":null,"env":null,"ext":{ "metrics":"{'kbCode':'q82ni07qxpcg','chunksCount':3,'fillTime':0,'retrievalDetails':[{' embeddingTime':144,'engineType':'builtin_vector','kbIndexCode':'q82ni07qxpcgb765','retrie dChunksCount':3,'vectorRecallTime':49}],'totalTime':213}"}}
```

**状态码说明**

网关异常状态码说明

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY E _ XPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 403 | GATEWAY APP PATH NOT FOUN _ D! | 无效的服务调用路径 |

智能体工厂 OpenTrek 发指南

| 403 | GATEWAY APP PATH NOT REGI _ STER! | 当前服务调用路径未注册 |
|---|---|---|
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSP ACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT MA _ TCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE W _ _ RONG! | 鉴权失败,用户角色不匹配 |
| 404 | GATEWAY ROUTE URL NOT FOU ND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应 |

###### 文档知识库批量检索

**接口概述**

支持同时检索多个文档知识库，每个知识库可配置不同的检索参数，最大支持10个知识库同时检索。

**前提条件（查看APP_KEY）**

先进入菜单[主页->点击头像->APP_KEY]创建APP_KEY

**接口调用地址**

POST http://${endpoint}/gateway/kortex/api/kb/doc/combination/retrieve ${endpoint}见产品API文档页面详情

**入参描述**

Header传参智能体工厂 OpenTrek 发指南

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| Content-Type | String | 是 | Content-Type | application/json |
| x-sfm- workspacecode | String | 是 | 目标工作空间 | your workspace _ _ code |

Body传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| combinationPara ms | List<Object> | 是 | 检索参数列表 | [{"kbCode":"xxx" ,"query":"测试","score":0.01," limit":10}] |
| kbCode | String | 是 | 知识库编码 | tttbnz21dien |
| query | String | 是 | 查询内容 | 测试查询 |
| score | Double | 是 | 最小分值 | 0.01 |
| limit | Integer | 是 | 返回条目 | 10 |
| mapBatchKey | String | 否 | 批量检索时的结果映射KEY，用于区分不同请求的结果 | kb1 |
| kbIndexEngineTy pe | String | 否 | 索引引擎类型，可选值: builtin vector(向 _ 量索引引擎), builtin es(全文索 _ 引引擎) | builtin vector _ |
| chunkConfig | Object | 否 | Chunk扩展配置 | {"chunkBefore": 2, "chunkAfter": 2, "withNeighborCh unks": true} |

智能体工厂 OpenTrek 发指南

| chunkBefore | Integer | 否 | 返回前N个相邻 chunk数量，最大不超过5 | 2 |
|---|---|---|---|---|
| chunkAfter | Integer | 否 | 返回后N个相邻 chunk数量，最大不超过5 | 2 |
| withNeighborChu nks | Boolean | 否 | 是否返回相邻 chunk内容列表 | true |
| fusionType | String | 否 | 融合检索类型，可选值: lws(线性加权), rrf(互惠排名融合)。为空时表示不使用融合检索 | lws |
| fusionConfig | Object | 否 | 融合检索配置，只有fusionType不为空时才需要设置 | {"textScore": 0.5, "vectorScore": 0.5, "topKText": 20, "topKVec": 20, "topN": 10, "keywordWeight" : 0.5, "rankDiscount": 60} |
| topKText | Integer | 否 | 全文检索返回条数，默认使用limit | 20 |
| topKVec | Integer | 否 | 向量检索返回条数，默认使用limit | 20 |
| topN | Integer | 否 | 融合检索后返回条数，默认使用limit | 10 |
| textScore | Double | 否 | 全文检索分数阈值，融合检索时使用，默认0.5 | 0.5 |
| vectorScore | Double | 否 | 向量检索分数阈值，融合检索时使用，默认0.5 | 0.5 |

智能体工厂 OpenTrek 发指南

| keywordWeight | Float | 否 | 关键词权重(LWS融合时使用)，越大越偏向于全文检索- BM25，默认0.5 | 0.5 |
|---|---|---|---|---|
| rankDiscount | Integer | 否 | RRF名次衰减系数 (RRF融合时使用)， 越大越不看重头部排名，默认60 | 60 |
| needFileInfo | Boolean | 否 | 是否需要返回文件信息 | true |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | Boolean | 是否成功 | true |
| data | List<Object> | 批量检索结果列表 | [] |
| mapBatchKey | String | 结果映射KEY（对应请求中的mapBatchKey） | kb1 |
| kbCode | String | 知识库编码 | xxx |
| result | List<KbdocRetrieveIte m> | 检索结果列表 | [{"sys data id":"xxx"," _ _ file code":"yyy","chun _ k content":"内 _ 容","score":0.85}] |
| score | String | 检索结果的相关性得分， 根据检索类型不同含义不同，单引擎检索保持原始语义，融合检索经归一化处理用于统一评分标准。 1）单引擎检索：保持原始引擎的语义，向量检索为余弦相似度(0-1)，全文检索为BM25相关性得分；2）LWS融合：线性加权融合得分，经归一化处理；3）RRF融合：基于排名的互惠排名融合得分。 | 0.5 |

智能体工厂 OpenTrek 发指南

| sys data id _ _ | String | 数据唯一ID; | 59cc2523-8445-4f3a- 91f7-5e311f5530b2 |
|---|---|---|---|
| file name _ | String | 文件名称(当needFileInfo 为true时返回) | document.pdf |
| file url _ | String | 文件URL(当needFileInfo 为true时返回带有STS临时认证信息的地址) | https://example.com/fil es/document.pdf |
| file type _ | String | 文件类型(当needFileInfo 为true时返回) | pdf |
| sys create time _ _ | String | 数据创建时间; | 2023-04- 01T12:34:56Z |
| file code _ | String | 文件编码(当needFileInfo 为true时返回) | 123456 |
| chunk upload type _ _ | Integer | 上传类型 | 1 |
| chunk content _ | String | chunk内容 - 召回后送入 LLM的prompt文本 |  |
| show content _ | String | chunk内容 - 带有bbox和 objects占位符的文本形式 |  |
| chunk bboxs _ | List<Object> | bbox坐标信息 |  |
| text bbox _ | List<Double> | 坐标 | [ 0.3115, 0.0683, 0.0285, 0.372 ] |
| text type _ | String | 文本类型 | docTitle |
| text content _ | String | 文本内容 | 汇丰香港账户使用指南 |
| page | Integer | 页数 | 1 |
| start page _ | Integer | chunk序号 | 1 |

智能体工厂 OpenTrek 发指南

| chunk sort number _ _ | Integer | 页码 | 0 |
|---|---|---|---|
| beforeChunks | List<KbdocChunkNeig hbor> | 前N个相邻chunks(当 chunkBefore>0时返回) | [{"sysDataId":"xxx","fil eCode":"yyy","chunkC ontent":"内容"}] |
| afterChunks | List<KbdocChunkNeig hbor> | 后N个相邻chunks(当 chunkAfter>0时返回) | [{"sysDataId":"xxx","fil eCode":"yyy","chunkC ontent":"内容"}] |
| neighborChunkContent s | List<String> | 相邻chunk内容列表(当 withNeighborChunks为 true时返回) | ["前chunk内容","检索 chunk内容","后chunk内容"] |
| metrics | Object | 性能指标 | {} |
| kbCode | String | 知识库编码 | xxx |
| totalTime | Long | 检索总耗时(ms) | 150 |
| chunksCount | Integer | 返回的chunk数量 | 10 |
| fusionType | String | 融合方法类型 | lws |
| rrfTime | Long | RRF融合耗时(ms)，仅 RRF融合时有值 | 20 |
| lwsTime | Long | LWS融合耗时(ms)，仅 LWS融合时有值 | 15 |
| fillTime | Long | 附加信息填充耗时(ms) | 30 |
| retrievalDetails | List<Object> | 详细检索指标 | [] |
| kbIndexCode | String | 索引编码 | ozqn95a5936ycwkl |
| engineType | String | 引擎类型 | builtin vector _ |
| embeddingTime | Long | 向量嵌入耗时(ms) | 50 |
| vectorRecallTime | Long | 向量召回耗时(ms) | 80 |

智能体工厂 OpenTrek 发指南

| textQueryTime | Long | 全文检索耗时(ms) | 60 |
|---|---|---|---|
| retrievedChunksCount | Integer | 该引擎实际召回的chunk 数量 | 10 |
| success | Boolean | 是否检索成功 | true |
| errorMessage | String | 错误信息(检索失败时返回) | 知识库不存在 |
| errorCode | String | 错误码 |  |
| errorMsg | String | 错误描述 |  |

**请求示例**

```json
curl -X 'POST' http://${endpoint}/gateway/kortex/api/kb/doc/combination/retrieve \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -H 'x-sfm-workspacecode: baseline' \ -d '{
    "combinationParams":[
        {
            "kbCode":"kbcode1",
```

`"query":"`测试查询`1",`

```json
            "score":0.01,
            "limit":5,
            "mapBatchKey":"kb1"
        },
        {
            "kbCode":"kbcode2",
```

`"query":"`测试查询`2",`

```json
            "score":0.01,
            "limit":5,
            "mapBatchKey":"kb2",
            "fusionType":"lws",
            "topKText":20,
            "topKVec":20,
            "topN":5
        }
```

]

```
}'
```

**响应示例**

智能体工厂 OpenTrek 发指南

```json
{"success":true,"data":[{"mapBatchKey":"ozqn95a5936y","kbCode":"ozqn95a5936y","result": [{"sys_data_id":"59cc2523-8445-4f3a-91f7- 5e311f5530b2","file_code":"89549201e6e24b0f83a328863701b593","chunk_content":"xxxxxxxxxxx ,"score":0.5},{"sys_data_id":"ab4a788d-889e-4916-bc53d09ae943c12d","file_code":"89549201e6e24b0f83a328863701b593","chunk_content":"xxxxxxxxxxx ,"score":0.5},{"sys_data_id":"fe422a14-cecf-4fe8-a8ec- 1ae9c8760a21","file_code":"89549201e6e24b0f83a328863701b593","chunk_content":"xxxxxxxxxxx ,"score":0}],"metrics": {"kbCode":"ozqn95a5936y","totalTime":220,"chunksCount":3,"fusionType":"LWS","rrfTime":nul "lwsTime":0,"fillTime":0,"retrievalDetails": [{"kbIndexCode":"ozqn95a5936ysvdl","engineType":"builtin_es","embeddingTime":null,"vector callTime":null,"textQueryTime":21,"retrievedChunksCount":1}, {"kbIndexCode":"ozqn95a5936ycwkl","engineType":"builtin_vector","embeddingTime":153,"vect RecallTime":35,"textQueryTime":null,"retrievedChunksCount":2}]},"success":true,"errorMess e":null}],"errorCode":null,"errorMsg":null,"traceId":null,"env":null,"ext":null}
```

**状态码说明**

网关异常状态码说明

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY E _ XPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 403 | GATEWAY APP PATH NOT FOUN _ D! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT REGI _ STER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSP ACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY AUTH USER NOT MA _ TCH WRONG! | 鉴权失败,AK用户信息不匹配 |
|---|---|---|
| 401 | GATEWAY AUTH USER ROLE W _ _ RONG! | 鉴权失败,用户角色不匹配 |
| 404 | GATEWAY ROUTE URL NOT FOU ND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应 |

###### 数据表知识库检索服务

**接口概述**

根据查询文本在已构建好索引的知识库-数据表中进行向量或文本的检索。您可以通过查看请求示例，点击 curl命令示例右侧的调试按钮验证业务接口调用效果。

**前提条件（查看APP_KEY）**

先进入菜单[主页->点击头像->APP_KEY]创建APP_KEY

**接口调用地址**

POST http://${endpoint}/gateway/dext/api/retrieve/v1/search ${endpoint}见产品API文档页面详情

**入参描述**

Header传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| Content-Type | String | 是 | Content-Type | application/json |
| x-sfm- workspacecode | String | 是 | 目标工作空间 | your workspace _ _ code |

Body传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|

智能体工厂 OpenTrek 发指南

| dataPortfolioCode | String | 是 | 知识库code | 82168c22b87d49 4cb9b5e813e215 ae9b |
|---|---|---|---|---|
| domainName | String | 是 | 知识库下domain名称, 取值范围: table(表列信息), value(值), knowledge(知识), biSample(样例库/ICL), dimension(维度) | table |
| query | String | 是 | 查询的文本内容 | 西湖区 |
| returnNum | Integer | 是 | 返回数量, 最大不能超过100 | 10 |
| score | Double | 是 | 分数过滤阈值 |  |
| storeEngine | String | 是 | 索引类型, 包括: vector(向量), text(文本) | vector |
|  |  |  |  | domain - knowledge, storeEngine - vector { "domainFilters":{ "scopeOfAllTable s":false, "category":"术语解释", "tableCodes": ["e5e66de1d72a 48bab699a599dc f78040"], "columnCodes": ["e5e66de1d72a 48bab699a599dc f78040"] } } domainFilters参数解释: scopeOfAllTables : false - 限定为非全库, true - 限定为全库 category: 知识分组 tableCodes: 表 code, 来自知识库- 表接口, 为这条知识相关表, 相关字段所在的表 |

智能体工厂 OpenTrek 发指南

| domainFilters | JSONObject | 否 | 特定domain下可以支持的搜索filter参数, 不同domain支持的搜索范围不同, 具体支持范围见示例 | columnCodes: 字段code, 来自知识库-字段接口, 为这条知识相关的表 domain - value, storeEngine - text { "domainFilters":{ "tableCodes": ["66024e2bf0154 1da93e3bd04cdf 946a5"], "columnCodes": ["758f112ee7a84 f4684dd5a893dd f1430"] } } |
|---|---|---|---|---|
|  |  |  |  | domainFilters参数解释: tableCodes: 表 code, 来自知识库- 表接口, 为这个值所在的表 columnCodes: 字段code, 来自知识库-字段接口, 为这个值所在的字段 domain - dimension, storeEngine - text { "domainFilters":{ "dimDsCodes": ["3c2e30a6873b 4717890e0adf3c 70781c"] } } domainFilters参数解释: dimDsCodes: 维度表code, 来自字段接口出参, refDims |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | boolean | 接口是否调用成功 | true |
| data | Object | 数据节点 |  |
| items | JSONArray | 检索返回数据列表 | true |

智能体工厂 OpenTrek 发指南

| score | Double | 排序得分的浮点数，值越大相似性越高 | 0.334 |
|---|---|---|---|
| content | String | 召回的文本内容 | XX工厂第二车间 |
|  |  |  | table(表列信息) { "resources": { "schema": { "tables": [ { "table": { "columns": [ { "columnComment": "团队名称", "columnCode": "083b4109b21a4c58b 555e6885a320667", "columnName": "team name" _ } ], "tableCode": "2dda169434a342f6b6 233940e69c883a", "tableName": "llm dev inventory" _ _ } } ] } } } 参数解释: tableCode: 表code tableName: 原始表名 columnCode: 字段code columnName: 原始字段名 columnComment: 字段注释, 优先取页面手工修正的注释, 否则取源数据库中对应的注释 value(值) { "resources": { "value": { "columnCode": "eb19cfa9308b467c8f da8bc3ef84380c", "value": { "value": "张三" }, "tableName": "llm dev input invent _ _ _ ory", "columnName": "alias" } } } 参数解释: |

智能体工厂 OpenTrek 发指南

| resources | JSONObject | 召回的文本内容所在的结构化数据, 对于不同的 domain结构不同, 见示例 | columnCode: 字段code value: 源库中实际的 value tableName: 原始表名 columnName: 原始字段名 knowledge(知识) { "resources": { "knowledge": { "code": "ec231f17cfbc40e08af ef23c066c2d37", "name": "张三团队", "refRes": { "schema": { "columnCodes": [], "tables": [], "allTables": true, "tableCodes": [] } }, "content": "研发组，主管为张三" } } } 参数解释: code: 该条知识的系统 code name: 知识名称 content: 知识内容 refRes: 该条知识绑定的资源, 参考知识库资源查询 - 专家知识部分refRes节点解释 biSample(样例库/ICL) { "resources": { "biSample": { "code": "9fa48139fc60438898 56a06332e64e01", "query": " |
|---|---|---|---|
|  |  |  | 上周兵力大盘情况?", "sql": "select project name , _ sum(actual input) _ from llm dev inventory _ _ where week start >= _ DATE SUB(CURRENT _ _ DATE, INTERVAL 7 day) group by project name" _ } } } 参数解释: code: 该条样例的系统 code query: 样例库-query, 如'查询最高的分数' sql: 样例库-sql, 如'select max(score) from exam;' |

智能体工厂 OpenTrek 发指南

|  |  |  | dimension(维度) { "resources": { "dimension": { "dimDsCode": "9fa48139fc60438898 56a06332e64e01", "key": "1", "value": "男性" } } } 参数解释: dimDsCode: 知识库维度表对应的code key: 对应的维度键, 如'1' value: 对应的维度值, 如'男性' |
|---|---|---|---|

**请求示例**

```json
curl -X 'POST' http://${endpoint}/gateway/dext/api/retrieve/v1/search \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'x-sfm-workspacecode: test' \ -H 'Content-Type: application/json' \ -d '{
    "dataPortfolioCode":"543eec8256cf40418d18c009ad9b319b",
    "domainName":"dimension",
```

`"query":"`公司`",`

```json
    "returnNum":10,
    "score":0.52,
    "domainFilters":{
        "dimDsCodes":["3c2e30a6873b4717890e0adf3c70781c"]
    },
    "storeEngine":"text"
}'
```

**响应示例**

智能体工厂 OpenTrek 发指南

```json
{
    "success": true,
    "data": [
        {
            "score": 1.0809742,
            "indexCode": "94bff03a24df40138044a5da0e601cff",
            "dataPortfolioCode": "543eec8256cf40418d18c009ad9b319b",
            "domainName": "dimension",
```

`"content": "`华润置地有限公司`",`

```json
            "contentIndex": 0,
            "sysTag": null,
            "resources": {
                "dimension": {
                    "dimDsName": "3c2e30a6873b4717890e0adf3c70781c",
                    "dimDsCode": "3c2e30a6873b4717890e0adf3c70781c",
```

`"value": "`华润置地有限公司`",` `"key": "`华润置地有限公司"

```json
                }
            },
            "tag": null,
            "version": null
        },
        {
            "score": 1.0809742,
            "indexCode": "e4d32d35aca84ee18d940a5d411b5453",
            "dataPortfolioCode": "543eec8256cf40418d18c009ad9b319b",
            "domainName": "dimension",
```

`"content": "`碧桂园控股有限公司`",`

```json
            "contentIndex": 0,
            "sysTag": null,
            "resources": {
                "dimension": {
                    "dimDsName": "3c2e30a6873b4717890e0adf3c70781c",
                    "dimDsCode": "3c2e30a6873b4717890e0adf3c70781c",
```

`"value": "`碧桂园控股有限公司`",` `"key": "`碧桂园控股有限公司"

```json
                }
            },
            "tag": null,
            "version": null
        }
```

`],`

```json
    "errorCode": null,
    "errorMsg": null,
    "traceId": null,
    "env": null,
    "ext": null
}
```

**状态码说明**

网关异常状态码说明智能体工厂 OpenTrek 发指南

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY E _ XPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 403 | GATEWAY APP PATH NOT FOUN _ D! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT REGI _ STER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSP ACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT MA _ TCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE W _ _ RONG! | 鉴权失败,用户角色不匹配 |
| 404 | GATEWAY ROUTE URL NOT FOU ND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应 |

智能体工厂 OpenTrek 发指南

###### 数据表知识库资源查询-表

**接口概述**

通过API查询指定知识库下绑定的表的详细信息。您可以通过查看请求示例，点击 curl命令示例右侧的调试按钮验证业务接口调用效果。

**前提条件（查看APP_KEY）**

先进入菜单[主页->点击头像->APP_KEY]创建APP_KEY

**接口调用地址**

POST http://${endpoint}/gateway/dext/api/dp/refRes/schema/listTablesWithRelatedInfo ${endpoint}见产品API文档页面详情

**入参描述**

Header传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | 是 | Content-Type | application/json |
| x-sfm- workspacecode | String | 是 | 目标工作空间 | your workspace _ _ code |

Body传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| dpCode | String | 是 | 知识库code | 82168c22b87d49 4cb9b5e813e215 ae9b |
| current | Integer | 是 | 当前页数 | 1 |
| pageSize | Integer | 是 | 分页大小, 不能超过 1000 | 10 |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | boolean | 接口是否调用成功 | true |

智能体工厂 OpenTrek 发指南

| data | JSONObject | 数据节点 |  |
|---|---|---|---|
| total | Integer | 总条目数 | 100 |
| list | JSONArray | 检索返回数据列表 | true |
| dpCode | String | 知识库id | 2688caccbe93fdd26b6 6195ebf7c1f2d |
| tableCode | String | 表code, 为数据库中全局唯一code | ca2cbfb7928d59547a3 a28a044467b15 |
| tableName | String | 原始表名 | tbl student _ |
| tableCommentExt | String | 表注释, 优先取页面手工修正的注释, 否则取源数据库中对应的注释 | 学生表 |

**请求示例**

```json
curl -X 'POST' http://${endpoint}/gateway/dext/api/dp/refRes/schema/listTablesWithRelatedInfo \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'x-sfm-workspacecode: test' \ -H 'Content-Type: application/json' \ -d '{
    "dpCode": "543eec8256cf40418d18c009ad9b319b",
    "pageSize": 1000,
    "current": 1
}'
```

**响应示例**

智能体工厂 OpenTrek 发指南

```json
{
    "success": true,
    "data": {
        "total": 2,
        "list": [
            {
                "dpCode": "543eec8256cf40418d18c009ad9b319b",
                "tableCode": "66024e2bf01541da93e3bd04cdf946a5",
                "tableName": "dwd_mat_voucher",
```

`"tableCommentExt": "`物料凭证"

```json
            },
            {
                "dpCode": "543eec8256cf40418d18c009ad9b319b",
                "tableCode": "b3856941fbe0462b9b9e3dcb95d79886",
                "tableName": "zfsc_spzz_xs_qg_y",
```

`"tableCommentExt": "`住房市场_商品住宅销售情况_月，来源国家统计局"

```
            }
```

`],`

```json
        "pageSize": 1000,
        "current": 1
    },
    "errorCode": null,
    "errorMsg": null,
    "traceId": null,
    "env": null,
    "ext": null
}
```

**状态码说明**

网关异常状态码说明

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY E _ XPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 403 | GATEWAY APP PATH NOT FOUN _ D! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT REGI _ STER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |

智能体工厂 OpenTrek 发指南

| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
|---|---|---|
| 403 | GATEWAY PARAMETER WORKSP ACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT MA _ TCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE W _ _ RONG! | 鉴权失败,用户角色不匹配 |
| 404 | GATEWAY ROUTE URL NOT FOU ND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应 |

###### 数据表知识库资源查询-字段

**接口概述**

通过API查询指定知识库下指定表的字段详细信息。您可以通过查看请求示例，点击 curl命令示例右侧的调试按钮验证业务接口调用效果。

**前提条件（查看APP_KEY）**

先进入菜单[主页->点击头像->APP_KEY]创建APP_KEY

**接口调用地址**

POST http://${endpoint}/dext/api/dp/refRes/schema/listColumnsWithRelatedInfo ${endpoint}见产品API文档页面详情

**入参描述**

Header传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|

智能体工厂 OpenTrek 发指南

| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
|---|---|---|---|---|
| Content-Type | String | 是 | Content-Type | application/json |
| x-sfm- workspacecode | String | 是 | 目标工作空间 | your workspace _ _ code |

Body传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| dpCode | String | 是 | 知识库code | 82168c22b87d49 4cb9b5e813e215 ae9b |
| tableCode | String | 是 | 表code | 6174366442861c 023cba74c26321 cd8a |
| current | Integer | 是 | 当前页数 | 1 |
| pageSize | Integer | 是 | 分页大小, 不能超过 1000 | 10 |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | boolean | 接口是否调用成功 | true |
| data | JSONObject | 数据节点 |  |
| total | Integer | 总条目数 | 100 |
| list | JSONArray | 检索返回数据列表 | true |
| dpCode | String | 知识库id | 2688caccbe93fdd26b6 6195ebf7c1f2d |
| tableCode | String | 表code | ca2cbfb7928d59547a3 a28a044467b15 |

智能体工厂 OpenTrek 发指南

| columnCode | String | 字段code | ca2cbfb7928d59547a3 a28a044467b15 |
|---|---|---|---|
| columnName | String | 原始字段名 | col student name _ _ |
| columnCommentExt | String | 字段注释, 优先取页面手工修正的注释, 否则取源数据库中对应的注释 | 学生姓名 |
| tags | JSONObject | 知识库中维护的扩展配置, 格式为key: value | {"随表召回":"是"} |
| refDims.dims[*] | JSONArray | 相关维度, 为一个深层 jsonpath路径 |  |
| code | String | 维度表code |  |
| name | String | 维度表名称 |  |
| refDimType | Integer | 相关维度 |  |

**请求示例**

```json
curl -X 'POST' http://${endpoint}/gateway/dext/api/dp/refRes/schema/listColumnsWithRelatedInfo \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'x-sfm-workspacecode: test' \ -H 'Content-Type: application/json' \ -d '{
    "dpCode":"094107a115f64f5c8770aa1c3a0d0c3c",
    "tableCode":"08dc4cbfef7c477e8ab9f50417678fd4"
}'
```

**响应示例**

智能体工厂 OpenTrek 发指南

```json
{
    "success": true,
    "data": {
        "total": 20,
        "list": [
            {
                "dpCode": "094107a115f64f5c8770aa1c3a0d0c3c",
                "tableCode": "08dc4cbfef7c477e8ab9f50417678fd4",
                "columnCode": "e5e66de1d72a48bab699a599dcf78040",
                "columnName": "student_name",
                "columnCommentExt": "学生姓名",
                "tags": {
```

"随表召回`": "`是"

```json
                },
                "includeValue": 0,
                "refDims": {
                    "dims": [
                        {
                            "code": "0d57e22c692a4c83a4de24fb1bb064b9",
```

`"name": "`学生名单表`",`

```json
                            "refDimType": 1
                        }
```

]

```json
                }
            },
            {
                "dpCode": "094107a115f64f5c8770aa1c3a0d0c3c",
                "tableCode": "08dc4cbfef7c477e8ab9f50417678fd4",
                "columnCode": "e911596b0c8648378b41c22fcdabe7e8",
                "columnName": "score",
                "columnCommentExt": "考试成绩",
                "tags": null,
                "includeValue": 0,
                "refDims": null
            }
```

`],`

```json
        "pageSize": 10,
        "current": 1
    },
    "errorCode": null,
    "errorMsg": null,
    "traceId": null,
    "env": null,
    "ext": null
}
```

**状态码说明**

网关异常状态码说明

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
|---|---|---|
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY E _ XPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 403 | GATEWAY APP PATH NOT FOUN _ D! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT REGI _ STER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSP ACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT MA _ TCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE W _ _ RONG! | 鉴权失败,用户角色不匹配 |
| 404 | GATEWAY ROUTE URL NOT FOU ND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应 |

###### 数据表知识库资源查询-专家知识

**接口概述**

智能体工厂 OpenTrek 发指南通过API查询指定知识库下绑定的专家知识信息。您可以通过查看请求示例，点击 curl命令示例右侧的调试按钮验证业务接口调用效果。

**前提条件（查看APP_KEY）**

先进入菜单[主页->点击头像->APP_KEY]创建APP_KEY

**接口调用地址**

POST http://${endpoint}/gateway/dext/api/dp/refRes/flexExt/list ${endpoint}见产品API文档页面详情

**入参描述**

Header传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | 是 | Content-Type | application/json |
| x-sfm- workspacecode | String | 是 | 目标工作空间 | your workspace _ _ code |

Body传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| dpCode | String | 是 | 知识库code | 82168c22b87d49 4cb9b5e813e215 ae9b |
| current | Integer | 是 | 当前页数 | 1 |
| pageSize | Integer | 是 | 分页大小, 不能超过 1000 | 10 |
| scopeOfAllTables | Boolean | 否 | 是否整库过滤项: null -> 不限制; true -> 整库级别; false -> 非整库级别 | true |
| tableCodes | String[] | 否 | 过滤项: 表级知识和列级知识所在的 tableCodes |  |

智能体工厂 OpenTrek 发指南

| columnCodes | String[] | 否 | 过滤项: 列级知识所在的columnCodes |  |
|---|---|---|---|---|
| categories | String[] | 否 | 过滤项: 知识分组 |  |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | boolean | 接口是否调用成功 | true |
| data | JSONObject | 数据节点 |  |
| total | Integer | 总条目数 | 100 |
| list | JSONArray | 检索返回数据列表 | true |
| code | String | 知识code | 2688caccbe93fdd26b6 6195ebf7c1f2d |
| name | String | 知识名称 | 本院 |
| content | String | 知识内容 | 本院指的是用户所属的院区 |
| refRes | JSONObject | 该条知识绑定的资源 |  |
| schema | JSONObject | 绑定资源 - 表 |  |
| allTables | Boolean | 是否是整库级别, 为true 时, 标明为全库级别 |  |
| tableCodes | String[] | tables下所有表级知识和列级知识所在的 tableCodes |  |
| columnCodes | String[] | tables下所有列级知识所在的columnCodes |  |

智能体工厂 OpenTrek 发指南

| tables | JSONObject | 绑定的表级和列级适用范围, 与domain=table时, resources.schema.tabl es一致 |  |
|---|---|---|---|

**请求示例**

```json
curl -X 'POST' http://${endpoint}/gateway/dext/api/dp/refRes/flexExt/list \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'x-sfm-workspacecode: test' \ -H 'Content-Type: application/json' \ -d '{
    "current":1,
    "pageSize":10,
    "dpCode":"094107a115f64f5c8770aa1c3a0d0c3c",
    "scopeOfAllTables":true,
    "tableCodes":["08dc4cbfef7c477e8ab9f50417678fd4"],
    "columnCodes":["e5e66de1d72a48bab699a599dcf78040"],
```

`"categories":["`计算口径`"]`

```
}'
```

**响应示例**

智能体工厂 OpenTrek 发指南

```json
{
    "success": true,
    "data": {
        "total": 1,
        "list": [
            {
                "code": "263a188399a24bb282c7325b40d4a231",
```

`"name": "`本院`",` `"content": "`本院指的是用户所属的院区`",`

```json
                "datasourceCode": "5ca9ab2356b8419094983535587e5d03",
                "tags": null,
                "refRes": {
                    "schema": {
                        "allTables": false,
                        "tables": [
                            {
                                "tableCode": "08dc4cbfef7c477e8ab9f50417678fd4",
```

`"tableName": "`院区字典表`",`

```json
                                "allColumns": false,
                                "columns": [
                                    {
                                        "columnCode": "e5e66de1d72a48bab699a599dcf78040",
```

`"columnName": "`院区名称"

```
                                    }
```

]

```
                            }
```

`],`

```json
                        "tableCodes": [
                            "08dc4cbfef7c477e8ab9f50417678fd4"
```

`],`

```json
                        "columnCodes": [
                            "e5e66de1d72a48bab699a599dcf78040"
```

]

```
                    }
                }
            }
```

`],`

```json
        "pageSize": 10,
        "current": 1
    },
    "errorCode": null,
    "errorMsg": null,
    "traceId": null,
    "env": null,
    "ext": null
}
```

**状态码说明**

网关异常状态码说明

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
|---|---|---|
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY E _ XPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 403 | GATEWAY APP PATH NOT FOUN _ D! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT REGI _ STER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSP ACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT MA _ TCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE W _ _ RONG! | 鉴权失败,用户角色不匹配 |
| 404 | GATEWAY ROUTE URL NOT FOU ND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应 |

##### 高码智能体

智能体工厂 OpenTrek 发指南

###### 创建session

您可以通过接口创建一个全新的agent会话。

**前提条件**

1. 登录OpenTrek Agent Dev控制台。
2. 在左侧导航栏中选择**集成** **> APP KEY**。
3. 单击**新建**创建APP Key。
4. 在左侧导航栏中选择**开发** > **智能体** > **智能体开发**，进入智能体页面完成配置并获取智能体编码和版本编

**接口调用地址**

```
 POST http://${endpoint}/sfm-agent-studio/sfm-api-
gateway/gateway/agent/highcode/createSession
```

${endpoint}见产品API文档页面详情。

**入参描述**

Header传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | 是 | Content-Type | application/json |
| x-sfm-security- business | string | 是 | 智能体编码。 | e36a0ab1-b673- 49d0-9534- 1480a147c691 |
| x-sfm-security- business-version | string | 否 | 智能体版本编码。 | 1706863858334 |
| x-sfm-end-user-id | string | 否 | 终端用户ID。 | test-user |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | boolean | 是否成功。 | true |
| data | object | 返回数据。 | {"uniqueCode":"4bcaa 882-9c54-4b78-9057- 54db58591b5b"} |

智能体工厂 OpenTrek 发指南

**请求示例**

```bash
curl -X POST http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/agent/highcode/createSession -H 'Authorization: Bearer YOUR_APP_KEY' -H 'Content-Type: application/json' -H 'x-sfm-security-business: e36a0ab1-b673-49d0-9534-1 480a147c691'
```

**响应示例**

```json
{
 "success": true,
 "data": {
  "uniqueCode": "4bcaa882-9c54-4b78-9057-54db58591b5b"
 },
 "errorCode": null,
 "errorMsg": null
}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失。 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败，无效 APP KEY。 _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败，APP KEY 已过期。 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色不匹配。 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色已过期。 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径。 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册。 |
| 429 | GATEWAY LIMIT ! | 服务触发限流，请稍后再试。 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流，请稍后再试。 |

智能体工厂 OpenTrek 发指南

| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失。 |
|---|---|---|
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配。 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败，不支持的鉴权方式。 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败，AK用户信息不匹配。 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败，用户角色不匹配。 |
| 404 | GATEWAY ROUTE URL NOT FOUND! | 无效的目标服务地址。 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限，请稍后再试。 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接。 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应。 |

###### 发起agent调用

您可以通过接口在已有会话的基础上对agent进行提问。

**前提条件**

1. 登录OpenTrek Agent Dev控制台。
2. 在左侧导航栏中选择**集成** **> APP KEY**。
3. 单击**新建**创建APP Key。
4. 调用创建session接口获取返回值uniqueCode

**接口调用地址**

```
 POST http://${endpoint}/sfm-agent-studio/sfm-api-gateway/gateway/agent/highcode/process
```

${endpoint}见产品API文档页面详情。

**入参描述**

Header传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|

智能体工厂 OpenTrek 发指南

| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
|---|---|---|---|---|
| Content-Type | String | 是 | Content-Type | application/json |
| x-sfm-security- business | string | 否 | 智能体编码。 | e36a0ab1-b673- 49d0-9534- 1480a147c691 |
| x-sfm-security- business-version | string | 否 | 智能体版本编码。 | 1706863858334 |
| x-session-id | string | 是 | 会话ID。 | bd962db7-b1c8- 4466-a2cc- 41b9b67cd94b |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| sequence number _ | integer | 序列号。 | 106 |
| object | string | 类型标识。 | message |
| role | string | 角色。 | assistant |
| type | string | 类型。 | text |
| status | string | 状态。 | completed |
| error | object | 错误信息。 | {} |

**请求示例**

```bash
curl -X POST http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/agent/highcode/process -H 'Authorization: Bearer YOUR_APP_KEY' -H 'Cont ent-Type: application/json' -H 'x-session-id: bd962db7-b1c8-4466-a2cc-41b9b67cd94b'
```

**响应示例**

智能体工厂 OpenTrek 发指南

```json
{
 "sequence_number": 1,
 "object": "message",
 "role": "assistant",
 "type": "text",
 "status": "completed"
}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失。 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败，无效 APP KEY。 _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败，APP KEY 已过期。 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色不匹配。 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色已过期。 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径。 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册。 |
| 429 | GATEWAY LIMIT ! | 服务触发限流，请稍后再试。 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流，请稍后再试。 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失。 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配。 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败，不支持的鉴权方式。 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败，AK用户信息不匹配。 |
|---|---|---|
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败，用户角色不匹配。 |
| 404 | GATEWAY ROUTE URL NOT FOUND! | 无效的目标服务地址。 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限，请稍后再试。 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接。 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应。 |

###### 终止会话

您可以通过调用该接口实现会话中断。

**前提条件**

1. 登录OpenTrek Agent Dev控制台。
2. 在左侧导航栏中选择**集成** **> APP KEY**。
3. 单击**新建**创建APP Key。
4. 调用创建session接口获取返回值uniqueCode。

**接口调用地址**

| POST http://${endpoint}/sfm-agent-studio/sfm-api- |  |
|---|---|

${endpoint}见产品API文档页面详情。

**入参描述**

Header传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | 是 | Content-Type | application/json |

智能体工厂 OpenTrek 发指南

| x-sfm-security- business | string | 否 | 智能体编码。 | e36a0ab1-b673- 49d0-9534- 1480a147c691 |
|---|---|---|---|---|
| x-sfm-security- business-version | string | 否 | 智能体版本编码。 | 1706863858334 |
| x-session-id | string | 是 | 会话ID。 | de454297-c547- 440f-ae55- 057a83a2d121 |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | boolean | 是否成功。 | true |

**请求示例**

```bash
curl -X POST http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/agent/highcode/abortSession -H 'Authorization: Bearer YOUR_APP_KEY' -H 'Content-Type: application/json' -H 'x-session-id: ${sessionId}'
```

**响应示例**

```json
{
 "success": true
}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失。 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败，无效 APP KEY。 _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败，APP KEY 已过期。 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色不匹配。 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色已过期。 |
|---|---|---|
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径。 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册。 |
| 429 | GATEWAY LIMIT ! | 服务触发限流，请稍后再试。 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流，请稍后再试。 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失。 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配。 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败，不支持的鉴权方式。 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败，AK用户信息不匹配。 |
| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败，用户角色不匹配。 |
| 404 | GATEWAY ROUTE URL NOT FOUND! | 无效的目标服务地址。 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限，请稍后再试。 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接。 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应。 |

###### 清除会话

您可以通过调用该接口实现会话以及相关过程数据永久删除。

**前提条件**

智能体工厂 OpenTrek 发指南
1. 登录OpenTrek Agent Dev控制台。
2. 在左侧导航栏中选择**集成** **> APP KEY**。
3. 单击**新建**创建APP Key。

**接口调用地址**

```
 POST http://${endpoint}/sfm-agent-studio/sfm-api-
gateway/gateway/agent/highcode/clearSession
```

${endpoint}见产品API文档页面详情。

**入参描述**

Header传参

| 字段 | 数据类型 | 是否必填 | 描述 | 示例 |
|---|---|---|---|---|
| Authorization | String | 是 | APP KEY _ | Bearer YOUR APP KEY _ _ |
| Content-Type | String | 是 | Content-Type | application/json |
| x-sfm-security- business | string | 否 | 智能体编码。 | e36a0ab1-b673- 49d0-9534- 1480a147c691 |
| x-sfm-security- business-version | string | 否 | 智能体版本编码。 | 1706863858334 |
| x-session-id | string | 是 | 会话ID。 | de454297-c547- 440f-ae55- 057a83a2d121 |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | boolean | 服务是否成功。 | true |
| data | boolean | 业务是否成功。 | true |

**请求示例**

```bash
curl -X POST http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/agent/highcode/clearSession -H 'Authorization: Bearer YOUR_APP_KEY' -H 'Content-Type: application/json' -H 'x-session-id: ${sessionId}'
```

**响应示例**

智能体工厂 OpenTrek 发指南

```json
{
 "success": true,
 "data": true
}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失。 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败，无效 APP KEY。 _ |
| 401 | GATEWAY APP KEY ALREADY _ EXPIRED! | 鉴权失败，APP KEY 已过期。 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色不匹配。 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败，当前 APP KEY 归属用户 _ 对应的角色已过期。 |
| 403 | GATEWAY APP PATH NOT _ FOUND! | 无效的服务调用路径。 |
| 403 | GATEWAY APP PATH NOT _ REGISTER! | 当前服务调用路径未注册。 |
| 429 | GATEWAY LIMIT ! | 服务触发限流，请稍后再试。 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流，请稍后再试。 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失。 |
| 403 | GATEWAY PARAMETER WORKSPACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配。 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败，不支持的鉴权方式。 |
| 401 | GATEWAY AUTH USER NOT _ MATCH WRONG! | 鉴权失败，AK用户信息不匹配。 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY AUTH USER ROLE _ _ WRONG! | 鉴权失败，用户角色不匹配。 |
|---|---|---|
| 404 | GATEWAY ROUTE URL NOT FOUND! | 无效的目标服务地址。 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限，请稍后再试。 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接。 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应。 |

##### 记忆体

###### 记忆体 API

###### 检索记忆

在记忆体中根据 query 检索召回常驻记忆、检索记忆与用户记忆。

**前提条件**

常驻记忆固定召回, 建议放到 System Prompt; 检索记忆按 query 召回; 用户记忆按 query + memoryUserId 召回, 其中任一为空时 userResults 返回空。

**接口调用地址**

```
 POST http://${endpoint}/sfm-agent-studio/sfm-api-gateway/gateway/memory/v1/search
```

${endpoint}见产品API文档页面详情。

**入参描述**

Header传参

| 参数名称 | 类型 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|
| Authorizatio n | String | 是 | Bearer YOUR APP KEY _ _ | APP KEY _ |
| Content- Type | String | 是 | application/json | Content-Type |

Body传参智能体工厂 OpenTrek 发指南

| 参数名称 | 类型 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|
| sfmMemory Code | string | 是 |  | 记忆体编码 |
| query | string | 否 | 我喜欢喝什么咖啡 | 检索文本 |
| memoryUse rId | string | 否 |  | 用户ID |
| topK | integ er | 否 | 10 | 召回条数 |
| threshold | numb er | 否 |  | 分数过滤阈值 |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | boolean | 是否成功。true 表示业务调用成功；false 时请结合 errorCode/errorMsg/err orMessages 排查 | true |
| data | object | 返回数据。包含三类记忆召回结果 | {"residentResults": [],"retrievalResults": [],"userResults":[]} |
| - residentResults | array | 常驻记忆召回结果，固定召回 | [] |
| -- id | string | 记忆ID | r-001 |
| -- memory | string | 记忆内容 | 始终用礼貌、简洁的语言回复 |
| -- score | number | 召回分数，取值范围 0-1 | 1.0 |
| -- createdAt | string | 创建时间 | 2026-05-30 10:00:00 |
| -- updatedAt | string | 更新时间 | 2026-05-30 10:00:00 |

智能体工厂 OpenTrek 发指南

| - retrievalResults | array | 检索记忆召回结果，按 query 召回 | [] |
|---|---|---|---|
| -- id | string | 记忆ID | k-001 |
| -- memory | string | 记忆内容 | 美式咖啡含糖量较低 |
| -- score | number | 召回分数，取值范围 0-1 | 0.82 |
| -- createdAt | string | 创建时间 | 2026-05-30 10:00:00 |
| -- updatedAt | string | 更新时间 | 2026-05-30 10:00:00 |
| - userResults | array | 用户记忆召回结果，按 query + memoryUserId 召回，query 或 memoryUserId 任一为空时返回空 | [] |
| -- id | string | 记忆ID | u-001 |
| -- memory | string | 记忆内容 | 用户偏好低糖美式咖啡 |
| -- score | number | 召回分数，取值范围 0-1 | 0.91 |
| -- createdAt | string | 创建时间 | 2026-05-30 10:00:00 |
| -- updatedAt | string | 更新时间 | 2026-05-30 10:00:00 |
| errorCode | string | 错误码。success=false 时返回简要错误码, 详细错误见 errorMessages |  |
| errorMsg | string | 错误信息。 success=false 时返回可读错误描述 |  |
| errorMessages | array | 错误明细数组 | [] |
| traceId | string | 链路追踪ID, 排查问题时请提供此 ID | 0a1b2c3d-trace-id |

智能体工厂 OpenTrek 发指南

| env | string | 服务返回的环境标识, 如 prod/pre/test | prod |
|---|---|---|---|

**请求示例**

```json
curl -X 'POST' http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/memory/v1/search \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -d '{
    "sfmMemoryCode": "YOUR_MEMORY_CODE",
```

`"query": "`我喜欢喝什么咖啡`",`

```json
    "memoryUserId": "user_001",
    "topK": 10,
    "threshold": 0.5
}'
```

**响应示例**

智能体工厂 OpenTrek 发指南

```json
{
  "success": true,
  "data": {
    "residentResults": [
      {
        "id": "r-001",
```

`"memory": "`始终用礼貌、简洁的语言回复`",`

```json
        "score": 1.0,
        "createdAt": "2026-05-30 10:00:00",
        "updatedAt": "2026-05-30 10:00:00"
      }
```

`],`

```json
    "retrievalResults": [
      {
        "id": "k-001",
```

`"memory": "`美式咖啡含糖量较低`",`

```json
        "score": 0.82,
        "createdAt": "2026-05-30 10:00:00",
        "updatedAt": "2026-05-30 10:00:00"
      }
```

`],`

```json
    "userResults": [
      {
        "id": "u-001",
```

`"memory": "`用户偏好低糖美式咖啡`",`

```json
        "score": 0.91,
        "createdAt": "2026-05-30 10:00:00",
        "updatedAt": "2026-05-30 10:00:00"
      }
```

]

```json
  },
  "errorCode": null,
  "errorMsg": null,
  "errorMessages": [],
  "traceId": "0a1b2c3d-trace-id",
  "env": "prod"
}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY E _ XPIRED! | 鉴权失败,APP KEY 已过期 _ |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
|---|---|---|
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT FOUN _ D! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT REGI _ STER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSP ACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT MA _ TCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE W _ _ RONG! | 鉴权失败,用户角色不匹配 |
| 404 | GATEWAY ROUTE URL NOT FOU ND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应 |

智能体工厂 OpenTrek 发指南

###### 写入会话消息

将一批对话消息写入指定记忆体的会话中, 这些消息会用于生成记忆。

**前提条件**

单次最多 100 条消息; 相同 conversationId 会归属同一业务会话; metadata 可携带会话级扩展字段。

**接口调用地址**

```
 POST http://${endpoint}/sfm-agent-studio/sfm-api-gateway/gateway/memory/v1/addMessages
```

${endpoint}见产品API文档页面详情。

**入参描述**

Header传参

| 参数名称 | 类型 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|
| Authorizatio n | String | 是 | Bearer YOUR APP KEY _ _ | APP KEY _ |
| Content- Type | String | 是 | application/json | Content-Type |

Body传参

| 参数名称 | 类型 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|
| sfmMemory Code | string | 是 | sfm-mem-001 | 关联记忆体编码 |
| userId | string | 否 | u-1001 | 用户标识 |
| conversatio nId | string | 是 | conv-20260518-001 | 业务会话ID |
| metadata | objec t | 否 | {"channel":"web"} | 会话级扩展字段(JSON对象) |
| messages | array | 是 | [{"messageId":"m- 001","role":"user","content": "你好"}] | 消息列表, 单次最多 100 条 |
| -messageId | string | 否 | m-001 | 消息唯一ID |

智能体工厂 OpenTrek 发指南

| -role | string | 是 | user | 消息角色, 枚举值: user / assistant |
|---|---|---|---|---|
| -content | string | 是 | 你好 | 消息内容文本 |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | boolean | 是否成功。true 表示业务调用成功；false 时请结合 errorCode/errorMsg/err orMessages 排查 | true |
| data | boolean | 写入结果, true 表示成功 | true |
| errorCode | string | 错误码。success=false 时返回简要错误码, 详细错误见 errorMessages |  |
| errorMsg | string | 错误信息。 success=false 时返回可读错误描述 |  |
| traceId | string | 链路追踪ID, 排查问题时请提供此 ID | 0a1b2c3d-trace-id |
| env | string | 服务返回的环境标识, 如 prod/pre/test | prod |

**请求示例**

```json
curl -X 'POST' http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/memory/v1/addMessages \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -d '{
    "sfmMemoryCode": "YOUR_MEMORY_CODE",
    "userId": "user_001",
    "conversationId": "conv-20260518-001",
    "metadata": {"channel": "web"},
    "messages": [
        {"messageId": "m-001", "role": "user", "content": "你好"},
        {"messageId": "m-002", "role": "assistant", "content": "你好, 有什么可以帮你?"}
```

]

```
}'
```

智能体工厂 OpenTrek 发指南

**响应示例**

```json
{
  "success": true,
  "data": true,
  "errorCode": null,
  "errorMsg": null,
  "errorMessages": [],
  "traceId": "xxx",
  "env": "prod"
}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY E _ XPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT FOUN _ D! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT REGI _ STER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSP ACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
|---|---|---|
| 401 | GATEWAY AUTH USER NOT MA _ TCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE W _ _ RONG! | 鉴权失败,用户角色不匹配 |
| 404 | GATEWAY ROUTE URL NOT FOU ND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应 |

###### 新增记忆

在指定记忆体的分区中新增一条记忆条目。

**前提条件**

partitionType 支持 RESIDENT(常驻) / RETRIEVAL(检索) / USER(用户); USER 分区必须提供 memoryUserId。

**接口调用地址**

```
 POST http://${endpoint}/sfm-agent-studio/sfm-api-gateway/gateway/memory/v1/add
```

${endpoint}见产品API文档页面详情。

**入参描述**

Header传参

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Authorizati on | Strin g | Hea der | 是 | Bearer YOUR APP KEY _ _ | APP KEY _ |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type |

Body传参智能体工厂 OpenTrek 发指南

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| sfmMemor yCode | strin g | Body | 是 | sfm-mem-001 | 记忆体编码 |
| partitionTy pe | strin g | Body | 是 | RETRIEVAL | 分区类型: RESIDENT(常驻) / RETRIEVAL(检索) / USER(用户) |
| storageCo ntent | strin g | Body | 是 | 用户偏好低糖美式咖啡 | 记忆内容, 存入记忆库的原始文本 |
| memoryUs erId | strin g | Body | 否 | user 001 _ | 用户ID, USER 分区必填, 用于绑定记忆归属用户 |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | boolean | 是否成功。true 表示新增成功；false 时请结合 errorCode/errorMsg 排查 | true |
| data | object | 无业务数据返回, 固定为 null |  |
| errorCode | string | 错误码。success=false 时返回简要错误码 |  |
| errorMsg | string | 错误信息。 success=false 时返回可读错误描述 |  |
| traceId | string | 链路追踪ID, 排查问题时请提供此 ID | 0a1b2c3d-trace-id |
| env | string | 服务返回的环境标识, 如 prod/pre/test | prod |

**请求示例**

智能体工厂 OpenTrek 发指南

```json
curl -X 'POST' http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/memory/v1/add \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -d '{
    "sfmMemoryCode": "YOUR_MEMORY_CODE",
    "partitionType": "USER",
```

`"storageContent": "`用户偏好低糖美式咖啡`",`

```json
    "memoryUserId": "user_001"
}'
```

**响应示例**

```json
{
  "success": true,
  "data": null,
  "errorCode": null,
  "errorMsg": null,
  "errorMessages": [],
  "traceId": "xxx",
  "env": "prod"
}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY E _ XPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT FOUN _ D! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT REGI _ STER! | 当前服务调用路径未注册 |

智能体工厂 OpenTrek 发指南

| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
|---|---|---|
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSP ACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT MA _ TCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE W _ _ RONG! | 鉴权失败,用户角色不匹配 |
| 404 | GATEWAY ROUTE URL NOT FOU ND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应 |

###### 更新记忆

更新指定记忆体分区下某条记忆条目的内容。

**前提条件**

通过 sfmMemoryCode + partitionType + memoryCode 定位到具体记忆; USER 分区还需提供 memoryUserId。

**接口调用地址**

```
 POST http://${endpoint}/sfm-agent-studio/sfm-api-gateway/gateway/memory/v1/update
```

${endpoint}见产品API文档页面详情。

**入参描述**

Header传参智能体工厂 OpenTrek 发指南

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Authorizati on | Strin g | Hea der | 是 | Bearer YOUR APP KEY _ _ | APP KEY _ |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type |

Body传参

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| sfmMemor yCode | strin g | Body | 是 | sfm-mem-001 | 记忆体编码 |
| partitionTy pe | strin g | Body | 是 | RETRIEVAL | 分区类型: RESIDENT / RETRIEVAL / USER |
| memoryCo de | strin g | Body | 是 | k-001 | 记忆条目编码 |
| storageCo ntent | strin g | Body | 是 | 用户偏好无糖美式咖啡 | 更新后的记忆内容 |
| memoryUs erId | strin g | Body | 否 | user 001 _ | 用户ID, USER 分区必填 |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | boolean | 是否成功。true 表示更新成功；false 时请结合 errorCode/errorMsg 排查 | true |
| data | object | 无业务数据返回, 固定为 null |  |
| errorCode | string | 错误码。success=false 时返回简要错误码 |  |

智能体工厂 OpenTrek 发指南

| errorMsg | string | 错误信息。 success=false 时返回可读错误描述 |  |
|---|---|---|---|
| traceId | string | 链路追踪ID, 排查问题时请提供此 ID | 0a1b2c3d-trace-id |
| env | string | 服务返回的环境标识, 如 prod/pre/test | prod |

**请求示例**

```json
curl -X 'POST' http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/memory/v1/update \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -d '{
    "sfmMemoryCode": "YOUR_MEMORY_CODE",
    "partitionType": "USER",
    "memoryCode": "k-001",
```

`"storageContent": "`用户偏好无糖美式咖啡`",`

```json
    "memoryUserId": "user_001"
}'
```

**响应示例**

```json
{
  "success": true,
  "data": null,
  "errorCode": null,
  "errorMsg": null,
  "errorMessages": [],
  "traceId": "xxx",
  "env": "prod"
}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY E _ XPIRED! | 鉴权失败,APP KEY 已过期 _ |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
|---|---|---|
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT FOUN _ D! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT REGI _ STER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSP ACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT MA _ TCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE W _ _ RONG! | 鉴权失败,用户角色不匹配 |
| 404 | GATEWAY ROUTE URL NOT FOU ND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应 |

智能体工厂 OpenTrek 发指南

###### 删除记忆

批量删除指定记忆体分区下的一批记忆条目(逻辑删除)。

**前提条件**

根据 sfmMemoryCode + partitionType 定位分区, 按 memoryCodeList 批量将状态置为 DELETED(1); USER 分区还需提供 memoryUserId。

**接口调用地址**

```
 POST http://${endpoint}/sfm-agent-studio/sfm-api-gateway/gateway/memory/v1/delete
```

${endpoint}见产品API文档页面详情。

**入参描述**

Header传参

| 参数名称 | 类型 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|
| Authorizatio n | String | 是 | Bearer YOUR APP KEY _ _ | APP KEY _ |
| Content- Type | String | 是 | application/json | Content-Type |

Body传参

| 参数名称 | 类型 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|
| sfmMemory Code | string | 是 | sfm-mem-001 | 记忆体编码 |
| partitionTyp e | string | 是 | RETRIEVAL | 分区类型: RESIDENT / RETRIEVAL / USER |
| memoryCod eList | array | 是 | ["k-001","k-002"] | 待删除的记忆条目编码列表 |
| -item | string | 否 | k-001 | 记忆条目编码 |
| memoryUse rId | string | 否 | user 001 _ | 用户ID, USER 分区必填 |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|

智能体工厂 OpenTrek 发指南

| success | boolean | 是否成功。true 表示业务调用成功；false 时请结合 errorCode/errorMsg 排查 | true |
|---|---|---|---|
| data | object | 返回数据 | {"success":true} |
| - success | boolean | 删除是否成功 | true |
| errorCode | string | 错误码。success=false 时返回简要错误码 |  |
| errorMsg | string | 错误信息。 success=false 时返回可读错误描述 |  |
| traceId | string | 链路追踪ID, 排查问题时请提供此 ID | 0a1b2c3d-trace-id |
| env | string | 服务返回的环境标识, 如 prod/pre/test | prod |

**请求示例**

```json
curl -X 'POST' http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/memory/v1/delete \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -d '{
    "sfmMemoryCode": "YOUR_MEMORY_CODE",
    "partitionType": "USER",
    "memoryCodeList": ["k-001", "k-002"],
    "memoryUserId": "user_001"
}'
```

**响应示例**

```json
{
  "success": true,
  "data": {
    "success": true
  },
  "errorCode": null,
  "errorMsg": null,
  "errorMessages": [],
  "traceId": "xxx",
  "env": "prod"
}
```

智能体工厂 OpenTrek 发指南

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY E _ XPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT FOUN _ D! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT REGI _ STER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSP ACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT MA _ TCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE W _ _ RONG! | 鉴权失败,用户角色不匹配 |

智能体工厂 OpenTrek 发指南

| 404 | GATEWAY ROUTE URL NOT FOU ND! | 无效的目标服务地址 |
|---|---|---|
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应 |

###### 分页查询记忆

按分区分页查询指定记忆体下的记忆条目列表, 支持关键字搜索。

**前提条件**

current 从 1 开始; pageSize 默认 20; keyword 为空时不做关键字过滤; 返回结构为标准 PageResult, 列表在 data.list 中。

**接口调用地址**

```
 POST http://${endpoint}/sfm-agent-studio/sfm-api-gateway/gateway/memory/v1/list
```

${endpoint}见产品API文档页面详情。

**入参描述**

Header传参

| 参数名称 | 类型 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|
| Authorizatio n | String | 是 | Bearer YOUR APP KEY _ _ | APP KEY _ |
| Content- Type | String | 是 | application/json | Content-Type |

Body传参

| 参数名称 | 类型 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|
| sfmMemory Code | string | 是 | sfm-mem-001 | 记忆体编码 |
| partitionTyp e | string | 是 | RETRIEVAL | 分区类型: RESIDENT / RETRIEVAL / USER |

智能体工厂 OpenTrek 发指南

| keyword | string | 否 | 咖啡 | 关键字搜索文本 |
|---|---|---|---|---|
| current | integ er | 否 | 1 | 当前页码, 从 1 开始 |
| pageSize | integ er | 否 | 20 | 每页大小 |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| success | boolean | 是否成功。true 表示业务调用成功；false 时请结合 errorCode/errorMsg/err orMessages 排查 | true |
| data | object | 分页数据 | {"list": [],"total":0,"current":1, "pageSize":20} |
| - list | array | 记忆条目列表 | [] |
| --memoryCode | string | 记忆条目编码 | k-001 |
| --storageContent | string | 记忆内容文本 | 美式咖啡含糖量较低 |
| --retrievalCount | integer | 被检索命中次数 | 3 |
| --status | integer | 记忆状态: 0-正常 \| 1-删除 \| 2-禁用 \| 3-锁定 \| 4-合并中 \| 5-冻结 | 0 |
| --gmtModify | string | 最近更新时间 | 2026-05-30 10:00:00 |
| --memoryUserId | string | 所属用户ID(USER 分区使用) | user 001 _ |
| - total | integer | 总条数 | 120 |
| - current | integer | 当前页码 | 1 |

智能体工厂 OpenTrek 发指南

| - pageSize | integer | 每页大小 | 20 |
|---|---|---|---|
| - totalPages | integer | 总页数 | 6 |
| errorCode | string | 错误码。success=false 时返回简要错误码, 详细错误见 errorMessages |  |
| errorMsg | string | 错误信息。 success=false 时返回可读错误描述 |  |
| traceId | string | 链路追踪ID, 排查问题时请提供此 ID | 0a1b2c3d-trace-id |
| env | string | 服务返回的环境标识, 如 prod/pre/test | prod |

**请求示例**

```json
curl -X 'POST' http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/memory/v1/list \ -H 'Authorization: Bearer YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -d '{
    "sfmMemoryCode": "YOUR_MEMORY_CODE",
    "partitionType": "RETRIEVAL",
    "keyword": "咖啡",
    "current": 1,
    "pageSize": 20
}'
```

**响应示例**

智能体工厂 OpenTrek 发指南

```json
{
  "success": true,
  "data": {
    "list": [
      {
        "memoryCode": "k-001",
```

`"storageContent": "`美式咖啡含糖量较低`",`

```json
        "retrievalCount": 3,
        "status": 0,
        "gmtModify": "2026-05-30 10:00:00",
        "memoryUserId": "user_001"
      }
```

`],`

```json
    "total": 120,
    "current": 1,
    "pageSize": 20,
    "totalPages": 6
  },
  "errorCode": null,
  "errorMsg": null,
  "errorMessages": [],
  "traceId": "xxx",
  "env": "prod"
}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY E _ XPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT FOUN _ D! | 无效的服务调用路径 |

智能体工厂 OpenTrek 发指南

| 403 | GATEWAY APP PATH NOT REGI _ STER! | 当前服务调用路径未注册 |
|---|---|---|
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSP ACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT MA _ TCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE W _ _ RONG! | 鉴权失败,用户角色不匹配 |
| 404 | GATEWAY ROUTE URL NOT FOU ND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应 |

###### Mem0 兼容 API

###### 写入记忆

按照 Mem0 V3 协议写入对话消息并生成记忆，或直接将消息内容写为记忆。

**前提条件**

messages 和 app_id 必填；role 仅支持 user、assistant。infer 默认为 true，由消息推断记忆； infer=false 时逐条直接写入，user_id 非空写入用户记忆，否则写入检索记忆。

**接口调用地址**

智能体工厂 OpenTrek 发指南

```
 POST http://${endpoint}/sfm-agent-studio/sfm-api-
gateway/gateway/memory/mem0/v3/memories/add
```

${endpoint}见产品API文档页面详情。

**入参描述**

Header传参

| 参数名称 | 类型 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|
| Authorizatio n | String | 是 | Bearer YOUR APP KEY _ _ | APP KEY _ |
| Content- Type | String | 是 | application/json | Content-Type |

Body传参

| 参数名称 | 类型 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|
| messages | array | 是 | [{"role":"user","content":"记住我喜欢低糖美式咖啡"}] | [{"role":"user","content":"记住我喜欢低糖美式咖啡"}] |
| -role | string | 是 | 消息角色，仅支持 user / assistant | user |
| -content | string | 是 | 消息内容 | 记住我喜欢低糖美式咖啡 |
| user id _ | string | 否 | user-001 | 用户标识 |
| app id _ | string | 是 | YOUR MEMORY CODE _ _ | 记忆体编码 |
| run id _ | string | 否 | conversation-001 | 会话标识；为空时自动生成 |
| metadata | objec t | 否 | {"channel":"web"} | 会话级扩展字段 |
| infer | boole an | 否 | true | 是否从消息中推断记忆，默认 true |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|

智能体工厂 OpenTrek 发指南

| message | string | 处理结果说明 | Memory processing has been queued for background execution |
|---|---|---|---|
| status | string | 处理状态 | SUCCEEDED |
| event id _ | string | Mem0 事件标识；当前实现返回 null |  |

**请求示例**

curl命令示例：

```json
curl -X 'POST' http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/memory/mem0/v3/memories/add \ -H 'Authorization: Token YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -d '{
  "messages": [
```

`{"role": "user", "content": "`记住我喜欢低糖美式咖啡`"}` `],`

```json
  "user_id": "user-001",
  "app_id": "YOUR_MEMORY_CODE",
  "run_id": "conversation-001",
  "metadata": {"channel": "web"},
  "infer": true
}'
```

Mem0 Python 客户端调用示例： 智能体工厂 OpenTrek 发指南
# 安装依赖：`pip install mem0ai`

```python
from mem0 import MemoryClient
```

# url：将当前接口文档页面展示的 `API` 地址截断到 `/memory/mem0`；不要追加 `/v1`、`/v3` 或具体接口路径

```
url = "http://${endpoint}/sfm-agent-studio/sfm-api-gateway/gateway/memory/mem0"
```

# api_key：填写在 [主页 `->` 点击头像 `-> APP_KEY]` 创建的 `APP_KEY` 原值；客户端会自动添加 `Token` 前缀
，不要手动添加 `Token`

```
api_key = "YOUR_APP_KEY" client = MemoryClient(api_key=api_key, host=url) result = client.add(
    messages=[
```

`{"role": "user", "content": "`记住我喜欢低糖美式咖啡`"}` `],`

```
    user_id="user-001",
    app_id="YOUR_MEMORY_CODE",
    run_id="conversation-001",
    metadata={"channel": "web"},
    infer=True,
```

)

```python
print(result)
```

**响应示例**

```json
{
  "message": "Memory processing has been queued for background execution",
  "status": "SUCCEEDED",
  "event_id": null
}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY E _ XPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
|---|---|---|
| 403 | GATEWAY APP PATH NOT FOUN _ D! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT REGI _ STER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSP ACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT MA _ TCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE W _ _ RONG! | 鉴权失败,用户角色不匹配 |
| 404 | GATEWAY ROUTE URL NOT FOU ND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应 |

###### 检索记忆

按照 Mem0 V3 协议，根据查询文本和过滤条件检索记忆。 智能体工厂 OpenTrek 发指南

**前提条件**

query、filters.app_id 必填。filters 支持直接填写条件，或使用 AND 条件数组；仅支持 app_id、 user_id 的字符串等值过滤，不支持比较运算、通配符及其他字段。

**接口调用地址**

| POST http://${endpoint}/sfm-agent-studio/sfm-api- |  |
|---|---|

${endpoint}见产品API文档页面详情。

**入参描述**

Header传参

| 参数名称 | 类型 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|
| Authorizatio n | String | 是 | Bearer YOUR APP KEY _ _ | APP KEY _ |
| Content- Type | String | 是 | application/json | Content-Type |

Body传参

| 参数名称 | 类型 | 是否必选 | 示例 | 说明 |  |
|---|---|---|---|---|---|
| query | stri ng | 是 | 我喜欢喝什么咖啡 | 检索文本 |  |
| filters | obj ect | 是 | {"AND": [{"app id":"YOUR M _ _ EMORY CODE"}, _ {"user id":"user- _ 001"}]} | 过滤条件；支持直接对象或 AND 条件数组 |  |
| -app id _ | stri ng | 是 | YOUR MEMORY COD _ _ E | 记忆体编码 |  |
| -user id _ | stri ng | 否 | user-001 | 用户标识；指定后检索对应用户记忆 |  |
| top k _ | int ege r | 否 | 10 | 召回条数，默认 10 |  |

智能体工厂 OpenTrek 发指南

| threshol d | nu mb er | 否 | 0.5 | 分数过滤阈值，默认 0.1 |  |
|---|---|---|---|---|---|

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| results | array | 记忆结果列表 | [{"id":"memory- 001","memory":"用户偏好低糖美式咖啡","user id":"user- _ 001","score":0.91,"met adata":null,"categories ": [],"created at":"2026- _ 07- 21T02:00:00Z","updat ed at":"2026-07- _ 21T02:00:00Z"}] |
| - id | string | 记忆条目唯一标识 | memory-001 |
| - memory | string | 记忆内容 | 用户偏好低糖美式咖啡 |
| - user id _ | string | 用户标识 | user-001 |
| - score | number | 相似度分数 | 0.91 |
| - categories | array | 记忆分类列表 | [] |
| - created at _ | string | 创建时间，ISO-8601 格式 | 2026-07- 21T02:00:00Z |
| - updated at _ | string | 更新时间，ISO-8601 格式 | 2026-07- 21T02:00:00Z |

**请求示例**

curl命令示例智能体工厂 OpenTrek 发指南

```bash
curl -X 'POST' http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/memory/mem0/v3/memories/search \ -H 'Authorization: Token YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -d '{
```

`"query": "`我喜欢喝什么咖啡`",`

```json
  "filters": {
    "AND": [
      {"app_id": "YOUR_MEMORY_CODE"},
      {"user_id": "user-001"}
```

]

```json
  },
  "top_k": 10,
  "threshold": 0.5
}'
```

Mem0 Python 客户端调用示例
# 安装依赖：`pip install mem0ai`

```python
from mem0 import MemoryClient
```

# url：将当前接口文档页面展示的 `API` 地址截断到 `/memory/mem0`；不要追加 `/v1`、`/v3` 或具体接口路径

```
url = "http://${endpoint}/sfm-agent-studio/sfm-api-gateway/gateway/memory/mem0"
```

# api_key：填写在 [主页 `->` 点击头像 `-> APP_KEY]` 创建的 `APP_KEY` 原值；客户端会自动添加 `Token` 前缀
，不要手动添加 `Token`

```
api_key = "YOUR_APP_KEY" client = MemoryClient(api_key=api_key, host=url) result = client.search(
```

`query="`我喜欢喝什么咖啡`",`

```json
    filters={
        "AND": [
            {"app_id": "YOUR_MEMORY_CODE"},
            {"user_id": "user-001"},
```

]

```
    },
    top_k=10,
    threshold=0.5,
```

)

```python
print(result)
```

**响应示例**

智能体工厂 OpenTrek 发指南

```json
{
  "results": [
    {
      "id": "memory-001",
```

`"memory": "`用户偏好低糖美式咖啡`",`

```json
      "user_id": "user-001",
      "score": 0.91,
      "categories": [],
      "created_at": "2026-07-21T02:00:00Z",
      "updated_at": "2026-07-21T02:00:00Z"
    }
```

]

```
}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY E _ XPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT FOUN _ D! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT REGI _ STER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |

智能体工厂 OpenTrek 发指南

| 403 | GATEWAY PARAMETER WORKSP ACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
|---|---|---|
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT MA _ TCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE W _ _ RONG! | 鉴权失败,用户角色不匹配 |
| 404 | GATEWAY ROUTE URL NOT FOU ND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应 |

###### 分页查询记忆

**前提条件**

filters.app_id 必填，filters.user_id 可选；filters 仅支持字符串等值条件。page 和 page_size 从 1 开始且必须大于 0，默认分别为 1 和 10。结果按常驻记忆、用户记忆、检索记忆的顺序统一分页；未指定 user_id 时不查询用户记忆。

**接口调用地址**

| POST http://${endpoint}/sfm-agent-studio/sfm-api- |  |
|---|---|

${endpoint}见产品API文档页面详情。

**入参描述**

Header传参

| 参数名称 | 类型 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|
| Authorizatio n | String | 是 | Bearer YOUR APP KEY _ _ | APP KEY _ |

智能体工厂 OpenTrek 发指南

| Content- Type | String | 是 | application/json | Content-Type |
|---|---|---|---|---|

Body传参

| 参数名称 | 类型 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|
| filters | objec t | 是 | {"AND": [{"app id":"YOUR MEMORY _ _ _ CODE"},{"user id":"user- _ 001"}]} | 过滤条件；支持直接对象或 AND 条件数组 |
| -app id _ | string | 是 | YOUR MEMORY CODE _ _ | 记忆体编码 |
| -user id _ | string | 否 | user-001 | 用户标识；指定后包含对应用户记忆 |

Query传参

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| page | Integ er | Quer y | 否 | 1 | 页码，从 1 开始，默认 1 |
| page size _ | Integ er | Quer y | 否 | 10 | 每页条数，默认 10 |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| count | integer | 符合条件的记忆总数 | 21 |
| next | string | 下一页地址；无下一页时为 null | /memory/mem0/v3/me mories/? page=2&page size=1 _ 0 |
| previous | string | 上一页地址；无上一页时为 null |  |

智能体工厂 OpenTrek 发指南

| results | array | 当前页记忆列表 | [{"id":"memory- 001","memory":"用户偏好低糖美式咖啡","user id":"user- _ 001","categories": [],"updated at":"2026- _ 07-21T02:00:00Z"}] |
|---|---|---|---|
| - id | string | 记忆条目唯一标识 | memory-001 |
| - memory | string | 记忆内容 | 用户偏好低糖美式咖啡 |
| - user id _ | string | 用户标识 | user-001 |
| - score | number | 相关性得分；分页查询结果通常不返回 |  |
| - metadata | object | 记忆扩展字段；当前分页查询通常不返回 | {} |
| - categories | array | 记忆分类列表 | [] |
| - created at _ | string | 创建时间；当前分页查询通常不返回 |  |
| - updated at _ | string | 更新时间，ISO-8601 格式 | 2026-07- 21T02:00:00Z |

**请求示例**

curl命令示例： 智能体工厂 OpenTrek 发指南

```json
curl -X 'POST' 'http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/memory/mem0/v3/memories?page=1&page_size=10' \ -H 'Authorization: Token YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -d '{
  "filters": {
    "AND": [
      {"app_id": "YOUR_MEMORY_CODE"},
      {"user_id": "user-001"}
```

]

```
  }
}'
```

Mem0 Python 客户端调用示例：
# 安装依赖：`pip install mem0ai`

```python
from mem0 import MemoryClient
```

# url：将当前接口文档页面展示的 `API` 地址截断到 `/memory/mem0`；不要追加 `/v1`、`/v3` 或具体接口路径

```
url = "http://${endpoint}/sfm-agent-studio/sfm-api-gateway/gateway/memory/mem0"
```

# api_key：填写在 [主页 `->` 点击头像 `-> APP_KEY]` 创建的 `APP_KEY` 原值；客户端会自动添加 `Token` 前缀
，不要手动添加 `Token`

```json
api_key = "YOUR_APP_KEY" client = MemoryClient(api_key=api_key, host=url) result = client.get_all(
    filters={
        "AND": [
            {"app_id": "YOUR_MEMORY_CODE"},
            {"user_id": "user-001"},
```

]

```
    },
    page=1,
    page_size=10,
```

)

```python
print(result)
```

**响应示例**

智能体工厂 OpenTrek 发指南

```json
{
  "count": 21,
  "next": "/memory/mem0/v3/memories/?page=2&page_size=10",
  "previous": null,
  "results": [
    {
      "id": "memory-001",
```

`"memory": "`用户偏好低糖美式咖啡`",`

```json
      "user_id": "user-001",
      "categories": [],
      "updated_at": "2026-07-21T02:00:00Z"
    }
```

]

```
}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY E _ XPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT FOUN _ D! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT REGI _ STER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |

智能体工厂 OpenTrek 发指南

| 403 | GATEWAY PARAMETER WORKSP ACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
|---|---|---|
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT MA _ TCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE W _ _ RONG! | 鉴权失败,用户角色不匹配 |
| 404 | GATEWAY ROUTE URL NOT FOU ND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应 |

###### 查询单条记忆

**前提条件**

memoryId 路径参数必填。查询成功返回单个记忆对象；指定条目不存在时返回 HTTP 404。

**接口调用地址**

| GET http://${endpoint}/sfm-agent-studio/sfm-api- |  |
|---|---|

${endpoint}见产品API文档页面详情。

**入参描述**

Header传参

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Authorizati on | Strin g | Hea der | 是 | Bearer YOUR APP KEY _ _ | APP KEY _ |

智能体工厂 OpenTrek 发指南

| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type |
|---|---|---|---|---|---|

Body传参

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| memoryId | strin g | Body | 是 | memory-001 | 记忆条目唯一标识 |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| id | string | 记忆条目唯一标识 | memory-001 |
| memory | string | 记忆内容 | 用户偏好低糖美式咖啡 |
| user id _ | string | 用户标识；非用户记忆不返回 | user-001 |
| categories | array | 记忆分类列表 | [] |
| created at _ | string | 创建时间，ISO-8601 格式 | 2026-07- 21T02:00:00Z |
| updated at _ | string | 更新时间，ISO-8601 格式 | 2026-07- 21T02:00:00Z |

**请求示例**

curl命令示例：

```bash
curl -X 'GET' http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/memory/mem0/v1/memories/memory-001 \ -H 'Authorization: Token YOUR_APP_KEY'
```

Mem0 Python 客户端调用示例： 智能体工厂 OpenTrek 发指南
# 安装依赖：`pip install mem0ai`

```python
from mem0 import MemoryClient
```

# url：将当前接口文档页面展示的 `API` 地址截断到 `/memory/mem0`；不要追加 `/v1`、`/v3` 或具体接口路径

```
url = "http://${endpoint}/sfm-agent-studio/sfm-api-gateway/gateway/memory/mem0"
```

# api_key：填写在 [主页 `->` 点击头像 `-> APP_KEY]` 创建的 `APP_KEY` 原值；客户端会自动添加 `Token` 前缀
，不要手动添加 `Token`

```python
api_key = "YOUR_APP_KEY" client = MemoryClient(api_key=api_key, host=url) result = client.get(memory_id="memory-001") print(result)
```

**响应示例**

```json
{
  "id": "memory-001",
```

`"memory": "`用户偏好低糖美式咖啡`",`

```json
  "user_id": "user-001",
  "categories": [],
  "created_at": "2026-07-21T02:00:00Z",
  "updated_at": "2026-07-21T02:00:00Z"
}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY E _ XPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT FOUN _ D! | 无效的服务调用路径 |

智能体工厂 OpenTrek 发指南

| 403 | GATEWAY APP PATH NOT REGI _ STER! | 当前服务调用路径未注册 |
|---|---|---|
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSP ACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT MA _ TCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE W _ _ RONG! | 鉴权失败,用户角色不匹配 |
| 404 | GATEWAY ROUTE URL NOT FOU ND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应 |

###### 更新记忆

按照 Mem0 V1 协议更新指定记忆条目的内容。

**前提条件**

memoryId 路径参数和 text 必填。当前仅支持更新记忆文本，metadata 必须为空或不传。

**接口调用地址**

| PUT http://${endpoint}/sfm-agent-studio/sfm-api- |  |
|---|---|

${endpoint}见产品API文档页面详情。 智能体工厂 OpenTrek 发指南

**入参描述**

Header传参

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Authorizati on | Strin g | Hea der | 是 | Bearer YOUR APP KEY _ _ | APP KEY _ |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type |

Body传参

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| memoryId | strin g | Body | 是 | memory-001 | 记忆条目唯一标识 |
| text | strin g | Body | 是 | 用户偏好无糖美式咖啡 | 更新后的记忆内容 |
| metadata | obje ct | Body | 否 | {} | 当前不支持更新，必须为空或不传 |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| message | string | 操作结果说明 | Memory updated successfully |

**请求示例**

curl命令示例：

```bash
curl -X 'PUT' http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/memory/mem0/v1/memories/memory-001 \ -H 'Authorization: Token YOUR_APP_KEY' \ -H 'Content-Type: application/json' \ -d '{
```

`"text": "`用户偏好无糖美式咖啡"

```
}'
```

Mem0 Python 客户端调用示例： 智能体工厂 OpenTrek 发指南
# 安装依赖：`pip install mem0ai`

```python
from mem0 import MemoryClient
```

# url：将当前接口文档页面展示的 `API` 地址截断到 `/memory/mem0`；不要追加 `/v1`、`/v3` 或具体接口路径

```
url = "http://${endpoint}/sfm-agent-studio/sfm-api-gateway/gateway/memory/mem0"
```

# api_key：填写在 [主页 `->` 点击头像 `-> APP_KEY]` 创建的 `APP_KEY` 原值；客户端会自动添加 `Token` 前缀
，不要手动添加 `Token`

```
api_key = "YOUR_APP_KEY" client = MemoryClient(api_key=api_key, host=url) result = client.update(
    memory_id="memory-001",
```

`text="`用户偏好无糖美式咖啡`",` )

```python
print(result)
```

**响应示例**

```json
{
  "message": "Memory updated successfully"
}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY E _ XPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT FOUN _ D! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT REGI _ STER! | 当前服务调用路径未注册 |

智能体工厂 OpenTrek 发指南

| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
|---|---|---|
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSP ACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |
| 401 | GATEWAY AUTH USER NOT MA _ TCH WRONG! | 鉴权失败,AK用户信息不匹配 |
| 401 | GATEWAY AUTH USER ROLE W _ _ RONG! | 鉴权失败,用户角色不匹配 |
| 404 | GATEWAY ROUTE URL NOT FOU ND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应 |

###### 删除记忆

按照 Mem0 V1 协议删除指定记忆条目。

**前提条件**

memoryId 路径参数必填。删除成功后返回操作结果说明。

**接口调用地址**

```
 DELETE http://${endpoint}/sfm-agent-studio/sfm-api-
gateway/gateway/memory/mem0/v1/memories/{memoryId}
```

${endpoint}见产品API文档页面详情。

**入参描述**

Header传参智能体工厂 OpenTrek 发指南

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Authorizati on | Strin g | Hea der | 是 | Bearer YOUR APP KEY _ _ | APP KEY _ |
| Content- Type | Strin g | Hea der | 是 | application/json | Content-Type |

Body传参

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| memoryId | strin g | Body | 是 | memory-001 | 记忆条目唯一标识 |

**出参描述**

| 字段 | 数据类型 | 描述 | 示例 |
|---|---|---|---|
| message | string | 操作结果说明 | Memory deleted successfully |

**请求示例**

curl命令示例：

```bash
curl -X 'DELETE' http://${endpoint}/sfm-agent-studio/sfm-apigateway/gateway/memory/mem0/v1/memories/memory-001 \ -H 'Authorization: Token YOUR_APP_KEY'
```

Mem0 Python 客户端调用示例：
# 安装依赖：`pip install mem0ai`

```python
from mem0 import MemoryClient
```

# url：将当前接口文档页面展示的 `API` 地址截断到 `/memory/mem0`；不要追加 `/v1`、`/v3` 或具体接口路径

```
url = "http://${endpoint}/sfm-agent-studio/sfm-api-gateway/gateway/memory/mem0"
```

# api_key：填写在 [主页 `->` 点击头像 `-> APP_KEY]` 创建的 `APP_KEY` 原值；客户端会自动添加 `Token` 前缀
，不要手动添加 `Token`

```python
api_key = "YOUR_APP_KEY" client = MemoryClient(api_key=api_key, host=url) result = client.delete(memory_id="memory-001") print(result)
```

智能体工厂 OpenTrek 发指南

**响应示例**

```json
{
  "message": "Memory deleted successfully"
}
```

**状态码说明**

| Http状态返回码 | 错误描述 | 错误释义 |
|---|---|---|
| 401 | GATEWAY APP KEY MISSING! _ | 网关必填参数缺失 |
| 401 | GATEWAY APP KEY WRONG! _ | 鉴权失败,无效 APP KEY _ |
| 401 | GATEWAY APP KEY ALREADY E _ XPIRED! | 鉴权失败,APP KEY 已过期 _ |
| 401 | GATEWAY ROLE NOT MATCH! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色不匹配 |
| 401 | GATEWAY ROLE HAS EXPIRED! | 鉴权失败,当前 APP KEY 归属用户 _ 对应的角色已过期 |
| 403 | GATEWAY APP PATH NOT FOUN _ D! | 无效的服务调用路径 |
| 403 | GATEWAY APP PATH NOT REGI _ STER! | 当前服务调用路径未注册 |
| 429 | GATEWAY LIMIT ! | 服务触发限流,请稍后再试 |
| 429 | GATEWAY LIMIT CURRENT CALL TYPE ! | 服务触发限流,请稍后再试 |
| 403 | GATEWAY HEADER PARAMETER MISSING! | 业务所需必填参数缺失 |
| 403 | GATEWAY PARAMETER WORKSP ACE NO MATCH! | 传递的工作空间编码与APP KEY归 _ 属用户关联的工作空间编码不匹配 |
| 401 | GATEWAY AUTH TYPE WRONG! _ | 鉴权失败,不支持的鉴权方式 |

智能体工厂 OpenTrek 发指南

| 401 | GATEWAY AUTH USER NOT MA _ TCH WRONG! | 鉴权失败,AK用户信息不匹配 |
|---|---|---|
| 401 | GATEWAY AUTH USER ROLE W _ _ RONG! | 鉴权失败,用户角色不匹配 |
| 404 | GATEWAY ROUTE URL NOT FOU ND! | 无效的目标服务地址 |
| 401 | GATEWAY LIMIT ! | 服务链接已达上限,请稍后再试 |
| 500 | TARGET SERVICE ERROR CON _ _ _ NECTION REFUSE EXCEPTION _ _ | 目标服务拒绝连接 |
| 500 | TARGET SERVICE ERROR NO R _ _ _ _ ESPONSE EXCEPTION _ | 目标服务无响应 |
